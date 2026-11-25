import json, re, html, sys, importlib
sys.path.insert(0, '/home/claude/endo')
from vis import VIS, render_vis

T = '/home/claude/lmv/trace/data/'
E = json.load(open(T + 'explain.json'))['decks']
Q = json.load(open(T + 'qbank.json'))
M = importlib.import_module(sys.argv[1] if len(sys.argv) > 1 else 'content_gi')
OUT = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/endo/gi.html'

def inl(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'<i>\1</i>', s)
    return s

def clean(s):
    # drop writer-facing flag markers now that the flags are decided
    s = re.sub(r'\s*\((?:new )?FLAG[^)]*\)', '', s)
    s = re.sub(r';\s*FLAG[^.;]*', '', s)
    s = re.sub(r'\s*\(see FLAGS\)', '', s)
    return s

def md(s):
    lines = s.replace('\\n', '\n').split('\n')
    out, tb = [], []
    def flush():
        if tb:
            rows = [[c.strip() for c in r.strip().strip('|').split('|')] if r.strip().startswith('|') else [c.strip() for c in r.split('|')] for r in tb]
            h = '<tr>' + ''.join('<th>%s</th>' % inl(c) for c in rows[0]) + '</tr>'
            b = ''.join('<tr>' + ''.join('<td>%s</td>' % inl(c) for c in r) + '</tr>' for r in rows[1:])
            out.append('<div class="gw"><table class="ct">%s%s</table></div>' % (h, b)); tb.clear()
    for l in lines:
        if ' | ' in l or l.strip().endswith(' |') or l.strip().startswith('| '):
            tb.append(l); continue
        flush()
        if l.strip(): out.append('<div class="ln">%s</div>' % inl(l))
    flush()
    return ''.join(out)

def heat(h):
    return sum(c.get('n', 1) for c in h.get('chips', [])) if h else 0

def chips(h):
    if not h or not h.get('chips'): return ''
    return ''.join('<span class="chip">%s ×%d</span>' % (html.escape(c['t']), c['n']) for c in h['chips'])

def pct(s):
    m = re.findall(r'(\d{1,3})% (?:right|chose|correct)', s) or re.findall(r'\((\d{1,3})%\)', s) or re.findall(r'(\d{1,3})–\d{1,3}% right', s)
    return min(int(x) for x in m) if m else None

PAL = ['#1f5fbf', '#c0561e', '#2e7d32', '#6d4c41', '#00838f', '#ad1457']
def dtree(t, depth=0):
    h = ''
    if depth == 0:
        h += '<div class="dt"><div class="dt-start">%s</div><div class="dt-arrow">▼</div>' % inl(t['start'])
    h += '<div class="dt-q">%s</div><div class="dt-row">' % inl(t['q'])
    for i, br in enumerate(t['b']):
        col = PAL[i % len(PAL)]
        h += '<div class="dt-b" style="--c:%s"><div class="dt-a">%s</div><div class="dt-arrow">▼</div>' % (col, inl(br['a']))
        if 'q' in br: h += dtree(br, depth + 1)
        else: h += '<div class="dt-dx"><b>%s</b>%s</div>' % (inl(br['dx']), ('<span>%s</span>' % inl(br['c'])) if br.get('c') else '')
        h += '</div>'
    h += '</div>'
    if depth == 0: h += '</div>'
    return h

def pair_html(p):
    A, B, shared, rows = p
    sh = '<div class="pv-same"><div class="pv-lbl">= Same in both</div><div class="pv-chips">' + ''.join('<span>%s</span>' % inl(x) for x in shared) + '</div></div>'
    body = ''
    for f, a, b in rows:
        key = f.startswith('!'); f = f.lstrip('!')
        body += '<tr class="%s"><th>%s%s</th><td>%s</td><td>%s</td></tr>' % ('key' if key else '', '★ ' if key else '', inl(f), inl(a), inl(b))
    tb = '<div class="pv-lbl pv-diff">≠ How they differ <span class="pv-hint">★ = the row that decides</span></div><table class="pv-t"><tr><th></th><th class="ca">A · %s</th><th class="cb">B · %s</th></tr>%s</table>' % (inl(A), inl(B), body)
    return '<div class="pv"><div class="pv-h"><span class="ca">A · %s</span> <i>vs</i> <span class="cb">B · %s</span></div>%s%s</div>' % (inl(A), inl(B), sh, tb)

def mimic_html(src, title, text):
    return '<div class="mim"><div class="mt"><span class="src">%s</span> %s</div><div class="mtext">%s</div></div>' % (src, inl(title), inl(clean(text)))

ids = {'n': 0}
def nid():
    ids['n'] += 1; return 'x%d' % ids['n']

stats = {'hit': 0, 'top': 0, 'lines': 0, 'tr': 0, 'pairs': 0, 'de': 0, 'gate': 0, 'concepts': 0}
seen_hits, seen_tops = set(), set()
home, body = [], []

for G in M.GROUPS:
    gid = G['id']
    dk = G['decks'][0]
    D = E[G['primer']]
    tiles = []
    for C in [c for c in M.CONCEPTS if c['group'] == gid]:
        stats['concepts'] += 1
        sid = C['id']
        # cards in the concept: all cards on its spine steps + extras
        incards = []
        for (d, st) in C['steps']:
            for code, v in E[d]['cards'].items():
                if v.get('step') == st: incards.append((d, code, v))
        skip = set(C.get('skip', []))
        incards = [x for x in incards if (x[0], x[1]) not in skip]
        for (d, code) in C.get('extra', []):
            incards.append((d, code, E[d]['cards'][code]))
        hits = [(d, c, v) for (d, c, v) in incards if (d + '|' + c) in Q['cards']]
        for d, c, v in hits:
            assert (d, c) in M.C, ('missing card text', d, c)
        tops = []
        for (td, ti) in C['tops']:
            xt = {t['id']: t for t in E[td].get('topups', [])}[ti]
            qt = {t['id']: t for t in Q['topups'].get(td, [])}.get(ti, {})
            tops.append((xt, qt))
        B = {'top': [], 'm': [], 't': [], 'c': [], 'a': []}
        tiles.append((sid, C['title'], len(hits) + len(tops)))
        # --- top: summary, core, flags, visuals, gate
        B['top'].append('<div class="concept">%s</div>' % inl(C['summary']))
        B['top'].append('<div class="rc"><div class="sec">The concept, in order</div><ol class="flow">' + ''.join('<li>%s</li>' % inl(x) for x in C['core']) + '</ol></div>')
        if C.get('flag'):
            B['top'].append('<div class="flag"><div class="lbl">Key vs guideline</div><ul>' + ''.join('<li>%s</li>' % inl(g) for g in C['flag']) + '</ul></div>')
        for vk in C.get('vis', []):
            B['top'].append('<div class="rc">%s</div>' % render_vis(VIS[vk], inl))
        if C.get('gate'):
            g = '<div class="gate"><div class="lbl">Gate: answer these before the tabs</div>'
            for i, (q, a) in enumerate(C['gate']):
                stats['gate'] += 1
                g += '<div class="gq"><span class="gn">%d</span> %s <button class="rv">Show answer</button><div class="ans" hidden>%s</div></div>' % (i + 1, inl(q), inl(a))
            B['top'].append(g + '</div>')
        # --- mimics
        for tr in C.get('trees', []):
            tid = nid()
            B['m'].append('<button class="tg" data-t="%s">Show the decision tree</button><div class="treebox" id="%s" hidden>%s</div>' % (tid, tid, dtree(tr)))
        for p in C.get('pairs', []):
            B['m'].append(pair_html(p)); stats['pairs'] += 1
        mims = [(c, m) for (d, c, v) in incards for m in v.get('mimic', [])]
        for t, _ in tops:
            for m in t['x'].get('mimic', []): mims.append(('Top-up', m))
        if mims:
            B['m'].append('<details class="more"><summary>More pairs from the cards (%d)</summary>' % len(mims) + ''.join(mimic_html(c, mt, mx) for c, (mt, mx) in mims) + '</details>')
        # --- traps, lowest % right first
        trs = [(c, t) for (d, c, v) in incards for t in v.get('traps', [])]
        for t, _ in tops:
            for tr in t['x'].get('traps', []): trs.append(('Top-up', tr))
        def tkey(x):
            p = pct(x[1][1]); return (0, p) if p is not None else (1, 0)
        trs = sorted(trs, key=tkey)
        def trap_html(c, w, why):
            p = pct(why); tag = ' <span class="low">%d%% right</span>' % p if p is not None and p < 70 else ''
            return '<div class="trap2"><div class="wrong"><span class="src">%s</span> <s>%s</s>%s</div><button class="rv">Why wrong?</button><div class="ans" hidden>%s</div></div>' % (c, inl(w), tag, inl(clean(why)))
        for c, (w, why) in trs[:5]:
            stats['tr'] += 1; B['t'].append(trap_html(c, w, why))
        if len(trs) > 5:
            stats['tr'] += len(trs) - 5
            B['t'].append('<details class="more"><summary>More traps (%d)</summary>' % (len(trs) - 5) + ''.join(trap_html(c, w, why) for c, (w, why) in trs[5:]) + '</details>')
        # --- hit cards by heat
        for d, c, v in sorted(hits, key=lambda x: -heat(Q['cards'][x[0] + '|' + x[1]])):
            stats['hit'] += 1; seen_hits.add(d + '|' + c)
            h = Q['cards'][d + '|' + c]; q, w = M.C[(d, c)]
            lines = []
            for part, txt in v.get('why', []):
                lead = M.LEAD_FIX.get((d, c, part))
                if not lead:
                    mm = re.match(r'\*\*(.+?)\*\*', txt)
                    lead = mm.group(1) if mm else ''
                if lead: lines.append('**%s** %s' % (part, lead))
            a = '\n'.join(lines)
            hn = heat(h); fl = '🔥' * min(3, max(1, hn // 3)) if hn else ''
            why = []
            for part, txt in v.get('why', []):
                fx = M.WHY_FIX.get((d, c, part))
                if fx: txt = txt.replace(fx[0], fx[1])
                if (d, c, part) in M.LEAD_FIX:
                    txt = re.sub(r'^\*\*.+?\*\*', '**' + M.LEAD_FIX[(d, c, part)] + '**', txt)
                why.append((part, clean(txt)))
            B['c'].append('<div class="card" id="%s-%s"><div class="ch"><b>%s</b> <span class="dkl">%s</span> <span class="heat">%s</span> %s <button class="mk" data-k="%s">Missed</button></div>' % (sid, c, c, d, fl, chips(h), c))
            if v.get('intro'): B['c'].append('<div class="intro"><b>Before the card:</b> %s</div>' % inl(clean(v['intro'])))
            B['c'].append('<div class="cq">%s</div><button class="rv">Show answer</button><div class="ans" hidden>%s' % (md(q), md(a)))
            if w: B['c'].append('<div class="watch"><b>Watch:</b> %s</div>' % inl(w))
            if why:
                B['c'].append('<details><summary>Why, part by part</summary><ul class="why">' + ''.join('<li><b class="pl">%s</b> %s</li>' % (html.escape(p), inl(t)) for p, t in why) + '</ul></details>')
            if v.get('table'):
                tb = v['table']
                B['c'].append('<details><summary>%s</summary><div class="gw"><table class="ct"><tr>%s</tr>%s</table></div></details>' % (inl(tb.get('title', 'Table')), ''.join('<th>%s</th>' % inl(x) for x in tb['head']), ''.join('<tr>' + ''.join('<td>%s</td>' % inl(x) for x in r) + '</tr>' for r in tb['rows'])))
            if h.get('lines'):
                stats['lines'] += len(h['lines'])
                B['c'].append('<div class="tul"><div class="lbl">Top-up lines</div><ul>' + ''.join('<li>%s</li>' % inl(l) for l in h['lines']) + '</ul></div>')
            if h.get('cross'):
                B['c'].append('<div class="cross"><div class="lbl">Crossfire: bank key vs guideline</div><ul>' + ''.join('<li>%s</li>' % inl(l) for l in h['cross']) + '</ul></div>')
            if v.get('traps'):
                B['c'].append('<details><summary>Traps on this card (%d)</summary><ul>' % len(v['traps']) + ''.join('<li><s>%s</s> → %s</li>' % (inl(x[0]), inl(clean(x[1]))) for x in v['traps']) + '</ul></details>')
            if v.get('punch'): B['c'].append('<div class="punch">%s</div>' % inl(v['punch']))
            B['c'].append('</div></div>')
        for t, qt in tops:
            stats['top'] += 1; seen_tops.add(t['id'])
            x = t['x']; tid = sid + '-TU-' + t['id']
            rec = ' <span class="chip">NEET 25 recall</span>' if qt.get('recall') else ''
            B['c'].append('<div class="card tu" id="%s"><div class="ch"><b>Top-up</b> · %s <span class="chip">%s</span> <span class="chip">%d questions</span>%s <button class="mk" data-k="%s">Missed</button></div>' % (tid, html.escape(t['topic']), html.escape(t.get('banks', '')), t.get('n', 0), rec, 'TU ' + t['topic'][:28]))
            if x.get('intro'): B['c'].append('<div class="intro"><b>Before the card:</b> %s</div>' % inl(clean(x['intro'])))
            ans = [re.sub(r'^-\s*', '', l) for l in t['a']]
            B['c'].append('<div class="cq">%s</div><button class="rv">Show answer</button><div class="ans" hidden><ul>%s</ul>' % (inl(t['q']), ''.join('<li>%s</li>' % inl(l) for l in ans)))
            if x.get('why'):
                B['c'].append('<details><summary>Why, part by part</summary><ul class="why">' + ''.join('<li><b class="pl">%s</b> %s</li>' % (html.escape(p), inl(clean(tx))) for p, tx in x['why']) + '</ul></details>')
            if x.get('traps'):
                B['c'].append('<details><summary>Traps on this card (%d)</summary><ul>' % len(x['traps']) + ''.join('<li><s>%s</s> → %s</li>' % (inl(y[0]), inl(clean(y[1]))) for y in x['traps']) + '</ul></details>')
            if x.get('punch'): B['c'].append('<div class="punch">%s</div>' % inl(x['punch']))
            B['c'].append('</div></div>')
        # --- asked: real bank questions first, practice items folded
        des = [(c, dd) for (d, c, v) in incards for dd in v.get('decode', [])]
        des += [(c, (p['q'], p['a'])) for (d, c, v) in incards for p in (v.get('parts') or [])]
        for t, _ in tops:
            for dd in t['x'].get('decode', []): des.append(('Top-up', dd))
        real = [x for x in des if '[pattern]' not in x[1][0]]
        prac = [x for x in des if '[pattern]' in x[1][0]]
        def dq_html(c, st, key):
            stats['de'] += 1
            p = pct(key); fl = ' <span class="low">only %d%% right</span>' % p if p is not None and p < 50 else ''
            k = 'Q-%s-%d' % (c, stats['de'])
            return '<div class="dq" id="%s-%s"><div class="stem"><span class="src">%s</span> %s%s</div><button class="rv">Show key</button> <button class="mk" data-k="%s">Missed</button><div class="ans" hidden>%s</div></div>' % (sid, k, c, inl(st), fl, k, inl(clean(key)))
        for c, (st, key) in real: B['a'].append(dq_html(c, st, key))
        if prac:
            B['a'].append('<details class="more"><summary>Practice items written from the cards, not bank questions (%d)</summary>' % len(prac) + ''.join(dq_html(c, st.replace(' [pattern]', ''), key) for c, (st, key) in prac) + '</details>')
        cnt = {'m': len(C.get('pairs', [])), 't': len(trs), 'c': len(hits) + len(tops), 'a': len(real)}
        tabs = [('m', 'Mimics'), ('t', 'Traps'), ('c', 'Cards'), ('a', 'Asked')]
        body.append('<section class="view con" id="%s" hidden><div class="vh"><button class="home">← Concepts</button> <span class="sn">%s</span> <b>%s</b> <button class="rall" title="Reveal all hidden facts in this concept">Reveal all</button></div>' % (sid, G['title'], html.escape(C['title'])))
        body.append(''.join(B['top']))
        body.append('<div class="tabs">' + ''.join('<button class="tab" data-p="%s-%s">%s <span class="cnt">%d</span></button>' % (sid, k, n, cnt[k]) for k, n in tabs) + '</div>')
        for k, n in tabs:
            inner = ''.join(B[k]) or '<div class="empty">Nothing here for this concept.</div>'
            body.append('<div class="pane" id="%s-%s" hidden>%s</div>' % (sid, k, inner))
        body.append('<div class="vf"><button class="done" data-s="%s">Mark concept done ✓</button></div></section>' % sid)
    # --- group extras: axis map and pattern drill
    ax = G['map']
    a = '<section class="view" id="%s-AXIS" hidden><div class="vh"><button class="home">← Concepts</button> <span class="sn">%s</span> <b>%s</b></div><div class="rc"><div class="axis">' % (gid, G['title'], html.escape(ax['title']))
    for i, (lvl, makes, breaks, drugs) in enumerate(ax['levels']):
        if i: a += '<div class="ax-arrow">▼ <span>%s</span></div>' % ax.get('arrow', 'drives')
        a += '<div class="ax-row"><div class="ax-lvl"><b>%s</b><span>%s</span></div><div class="ax-side">' % (inl(lvl), inl(makes))
        a += ''.join('<div class="ax-brk"><span class="ax-ic">✕</span> %s</div>' % inl(b) for b in breaks)
        a += ''.join('<div class="ax-drug"><span class="ax-ic">%s</span> %s</div>' % (ax.get('ki', '⊘'), inl(dd)) for dd in drugs)
        a += '</div></div>'
    a += '<div class="ax-fb">⟲ %s</div><div class="ax-key"><span class="ax-brk sm"><span class="ax-ic">✕</span> %s</span> <span class="ax-drug sm"><span class="ax-ic">%s</span> %s</span></div></div></div></section>' % (inl(ax['feedback']), ax.get('kb', 'where it breaks'), ax.get('ki', '⊘'), ax.get('ka', 'where drugs act'))
    body.append(a)
    dr = '<section class="view" id="%s-DRILL" hidden><div class="vh"><button class="home">← Concepts</button> <span class="sn">%s</span> <b>Pattern drill</b></div><div class="sub">Read the pattern, name it, then tap. Mark the ones you miss.</div>' % (gid, G['title'])
    for i, (pat, ans, why) in enumerate(G['drill']):
        k = '%s-drill-%d' % (gid, i + 1)
        dr += '<div class="drl" id="%s"><div class="dp"><span class="gn">%d</span> %s</div><button class="rv">Name it</button> <button class="mk" data-k="%s">Missed</button><div class="ans" hidden><b>%s.</b> %s</div></div>' % (k, i + 1, inl(pat), k, inl(ans), inl(why))
    body.append(dr + '</section>')
    home.append('<div class="dk"><h2>%s</h2><details><summary>Before you start</summary>%s</details><div class="gtools"><button class="gtile" data-go="%s-AXIS">✕✓ Disease map</button><button class="gtile" data-go="%s-DRILL">▶ Pattern drill (%d)</button></div><div class="tiles">' % (html.escape(G['title']), inl(D['primer']), gid, gid, len(G['drill'])))
    for i, (sid, tt, n) in enumerate(tiles):
        home.append('<button class="tile" data-go="%s"><span class="tn2">Concept %d · %d cards</span>%s</button>' % (sid, i + 1, n, html.escape(tt)))
    home.append('</div></div>')

# coverage check: every hit card and top-up of the group decks appears exactly once
for G in M.GROUPS:
    for dk in G['decks']:
        want = {k for k in Q['cards'] if k.startswith(dk + '|')}
        miss = want - seen_hits
        assert not miss, ('hit cards not placed', miss)
        tw = {t['id'] for t in Q['topups'].get(dk, [])}
        assert not (tw - seen_tops), ('top-ups not placed', tw - seen_tops)
assert len(seen_hits) == stats['hit'], 'a hit card was placed twice'

CSS = open('/home/claude/endo/style.css').read()
JS = open('/home/claude/endo/app.js').read().replace("var K='endo.';", "var K='gi.';")
page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title><style>%s</style></head><body>
<header><h1>%s</h1><button id="rcbtn" title="Hide the bold facts in the concept and visuals; tap one to reveal it">Recall mode: off</button></header>
<main><section class="view" id="HOME"><div class="prog"><i id="pb"></i></div><div class="sub" id="pc"></div>%s
<div class="util"><button class="gtile" data-go="MISS">Miss list (<span id="mc">0</span>)</button></div></section>
<section class="view" id="MISS" hidden><div class="vh"><button class="home">← Concepts</button> <b>Miss list</b> <button id="mclr" style="font-size:11.5px;padding:2px 8px">Clear</button></div><ul id="ml"></ul></section>
%s
</main><script>%s</script></body></html>""" % (M.PAGE['doc'], CSS, M.PAGE['title'], '\n'.join(home), '\n'.join(body), JS)
open(OUT, 'w').write(page)
print(stats, len(page))
