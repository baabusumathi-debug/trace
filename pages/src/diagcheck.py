# -*- coding: utf-8 -*-
"""Diagram check for a built study page. Run after every build, before anything is pushed.

    python3 diagcheck.py ../shock1.html            # report + crops in ./diagcheck-out/

For every <svg> on every screen it measures, in the real browser:
  1. TEXT ON TEXT   — two labels whose boxes overlap
  2. TEXT OUTSIDE   — a label running past the edge of the drawing (it gets cut off)
  3. TEXT ON LINES  — a label sitting across drawn lines or outlines: the drawing is
                      rendered without its words and the edges under each label are counted
  4. HTML ON SVG    — words in the page (captions, pins, notes) laid over a drawing
  5. IDS            — every arrowhead/gradient id defined once and referenced correctly
It writes a crop of every flagged drawing so each one can be looked at, and exits non-zero
if anything is flagged. Anatomy (which side, which border, which chamber is nearest the probe)
cannot be measured — that is the checklist in DIAGRAMS.md, read against each crop.
"""
import asyncio, json, os, sys
from playwright.async_api import async_playwright

PAGE = sys.argv[1]
OUT = sys.argv[2] if len(sys.argv) > 2 else 'diagcheck-out'
EDGE_LIMIT = 0.06        # share of a label's box covered by drawn edges before it counts as "on lines"

JS = r"""
async (vid) => {
  const view = document.getElementById(vid);
  const res = [];
  const svgs = [...view.querySelectorAll('svg')].filter(s => s.getBoundingClientRect().width > 40);
  for (let si = 0; si < svgs.length; si++) {
    const svg = svgs[si], R = svg.getBoundingClientRect();
    const texts = [...svg.querySelectorAll('text')].filter(t => t.textContent.trim());
    const box = t => { const r = t.getBoundingClientRect(); return { x: r.left - R.left, y: r.top - R.top, w: r.width, h: r.height, s: t.textContent.trim() }; };
    const B = texts.map(box);
    const issues = [];
    // 1 text on text
    for (let i = 0; i < B.length; i++) for (let j = i + 1; j < B.length; j++) {
      const a = B[i], b = B[j];
      const ox = Math.min(a.x + a.w, b.x + b.w) - Math.max(a.x, b.x), oy = Math.min(a.y + a.h, b.y + b.h) - Math.max(a.y, b.y);
      if (ox > 2 && oy > 2 && ox * oy > 0.12 * Math.min(a.w * a.h, b.w * b.h)) issues.push(['TEXT ON TEXT', a.s + '  ×  ' + b.s, [a, b]]);
    }
    // 2 text outside the drawing
    for (const a of B) if (a.x < -1 || a.y < -1 || a.x + a.w > R.width + 1 || a.y + a.h > R.height + 1) issues.push(['TEXT OUTSIDE', a.s, [a]]);
    // 3 text on lines: draw the svg without its words, look for edges under each label
    const k = 2, W = Math.round(R.width * k), H = Math.round(R.height * k);
    const c = svg.cloneNode(true); c.querySelectorAll('text').forEach(t => t.remove());
    c.setAttribute('width', W); c.setAttribute('height', H);
    if (!c.getAttribute('xmlns')) c.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
    const img = new Image();
    const url = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(new XMLSerializer().serializeToString(c));
    const ok = await new Promise(r => { img.onload = () => r(true); img.onerror = () => r(false); img.src = url; });
    if (ok) {
      const cv = document.createElement('canvas'); cv.width = W; cv.height = H;
      const g = cv.getContext('2d'); g.fillStyle = '#fff'; g.fillRect(0, 0, W, H); g.drawImage(img, 0, 0, W, H);
      const d = g.getImageData(0, 0, W, H).data;
      const lum = (x, y) => { const i = (y * W + x) * 4; return 0.3 * d[i] + 0.59 * d[i + 1] + 0.11 * d[i + 2]; };
      for (const a of B) {
        const x0 = Math.max(1, Math.round((a.x + 1) * k)), y0 = Math.max(1, Math.round((a.y + 2) * k));
        const x1 = Math.min(W - 2, Math.round((a.x + a.w - 1) * k)), y1 = Math.min(H - 2, Math.round((a.y + a.h - 2) * k));
        let e = 0, n = 0;
        for (let y = y0; y < y1; y++) for (let x = x0; x < x1; x++) {
          n++;
          const gx = Math.abs(lum(x + 1, y) - lum(x - 1, y)), gy = Math.abs(lum(x, y + 1) - lum(x, y - 1));
          if (gx + gy > 60) e++;
        }
        // a share of the box covered, OR one line running right through it (thin lines cover little area)
        let rowsHit = 0, colsHit = 0;
        for (let y = y0; y < y1; y++) { let r = 0; for (let x = x0; x < x1; x++) { const gx = Math.abs(lum(x + 1, y) - lum(x - 1, y)), gy = Math.abs(lum(x, y + 1) - lum(x, y - 1)); if (gx + gy > 60) { r = 1; break; } } rowsHit += r; }
        for (let x = x0; x < x1; x++) { let c = 0; for (let y = y0; y < y1; y++) { const gx = Math.abs(lum(x + 1, y) - lum(x - 1, y)), gy = Math.abs(lum(x, y + 1) - lum(x, y - 1)); if (gx + gy > 60) { c = 1; break; } } colsHit += c; }
        const bh = y1 - y0, bw = x1 - x0;
        const through = bh > 4 && rowsHit >= 0.8 * bh || bw > 4 && colsHit >= 0.8 * bw;
        if (n > 20 && (e / n > %EDGE% || through)) issues.push(['TEXT ON LINES', a.s + '  (' + (through ? 'a line runs through it' : Math.round(100 * e / n) + '% of its box') + ')', [a]]);
      }
    }
    // 4 page text laid over the drawing
    const fig = svg.closest('figure, .vis, .svgw') || svg.parentElement;
    for (const el of view.querySelectorAll('p, li, span, b, div, h3, h4')) {
      if (svg.contains(el) || el.contains(svg) || !el.childNodes.length) continue;
      if (![...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) continue;
      const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
      const ox = Math.min(r.right, R.right) - Math.max(r.left, R.left), oy = Math.min(r.bottom, R.bottom) - Math.max(r.top, R.top);
      if (ox > 4 && oy > 4) issues.push(['HTML ON SVG', el.textContent.trim().slice(0, 60), [{ x: r.left - R.left, y: r.top - R.top, w: r.width, h: r.height }]]);
    }
    if (issues.length) svg.setAttribute('data-dc', si);
    res.push({ si, issues, title: (svg.closest('figure, .vis, section') || svg).querySelector('h3,h4,.vt,figcaption') ? (svg.closest('figure, .vis, section').querySelector('h3,h4,.vt,figcaption').textContent.trim().slice(0, 70)) : '' });
  }
  // 5 page text on page text anywhere on the screen (boxes, flows, grids built from HTML)
  const runs = [];
  const tw = document.createTreeWalker(view, NodeFilter.SHOW_TEXT, { acceptNode: n => n.textContent.trim() && !n.parentElement.closest('svg') ? 1 : 2 });
  for (let n; (n = tw.nextNode());) {
    const cs = getComputedStyle(n.parentElement); if (cs.visibility === 'hidden' || +cs.opacity === 0) continue;
    const rg = document.createRange(); rg.selectNodeContents(n);
    for (const r of rg.getClientRects()) if (r.width > 2 && r.height > 2) runs.push({ n, r, s: n.textContent.trim().slice(0, 40) });
  }
  const pageIssues = [];
  for (let i = 0; i < runs.length; i++) for (let j = i + 1; j < runs.length; j++) {
    const a = runs[i], b = runs[j]; if (a.n === b.n) continue;
    const ox = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left), oy = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
    if (ox > 3 && oy > Math.min(a.r.height, b.r.height) * 0.35) pageIssues.push(['PAGE TEXT ON TEXT', a.s + '  ×  ' + b.s]);
  }
  if (pageIssues.length) res.push({ si: -1, issues: pageIssues.map(x => [x[0], x[1], []]), title: 'page text' });
  return res;
}
""".replace('%EDGE%', str(EDGE_LIMIT))

def ids_check(path):
    # an id defined twice resolves to the first copy, which may sit in a hidden screen and draw nothing
    import re
    h = open(path, encoding='utf-8').read()
    defs = re.findall(r'<(?:marker|linearGradient|radialGradient|clipPath|pattern)[^>]*\sid="([^"]+)"', h)
    refs = set(re.findall(r'url\(#([^)]+)\)', h))
    dup = sorted(set(i for i in defs if defs.count(i) > 1)); miss = sorted(refs - set(defs))
    for i in dup: print('   DUPLICATE ID   %s — define it once per drawing (arrowheads vanish on hidden screens)' % i)
    for i in miss: print('   MISSING ID     url(#%s) points at nothing' % i)
    return len(dup) + len(miss)

async def main():
    os.makedirs(OUT, exist_ok=True)
    url = 'file://' + os.path.abspath(PAGE)
    total = 0
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox'])
        for vw in (390, 800):
            pg = await b.new_page(viewport={'width': vw, 'height': 1000})
            await pg.goto(url); await pg.wait_for_timeout(300)
            await pg.add_style_tag(content='.dk-toast{display:none}')
            ids = await pg.evaluate("[...document.querySelectorAll('section.view')].map(v=>v.id)")
            for vid in ids:
                await pg.evaluate("id=>document.querySelectorAll('section.view').forEach(v=>v.hidden=v.id!==id)", vid)
                await pg.evaluate("document.querySelectorAll('details').forEach(d=>d.open=true);document.querySelectorAll('.ans').forEach(a=>a.hidden=false)")
                await pg.wait_for_timeout(40)
                res = await pg.evaluate(JS, vid)
                for r in res:
                    if not r['issues']: continue
                    total += len(r['issues'])
                    print('\n[%dpx] %s · drawing %d  %s' % (vw, vid, r['si'] + 1, r['title']))
                    for kind, what, _ in r['issues']: print('   %-14s %s' % (kind, what))
                    if r['si'] < 0:
                        await pg.screenshot(path=os.path.join(OUT, '%s_page_%d.png' % (vid, vw)), full_page=True); continue
                    el = await pg.query_selector('section#%s svg[data-dc="%d"]' % (vid, r['si']))
                    if el: await el.screenshot(path=os.path.join(OUT, '%s_%d_%d.png' % (vid, r['si'] + 1, vw)))
            await pg.close()
        await b.close()
    total += ids_check(PAGE)
    print('\n%d issue(s)' % total)
    sys.exit(1 if total else 0)

asyncio.run(main())
