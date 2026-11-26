# -*- coding: utf-8 -*-
"""Build pages/trauma.html from content.py + the cards (cards.jsonl, from Drive) + data/explain.json
+ data/qbank.json. It fails if a card or top-up is missing or placed twice, or if a blank breaks
the rules in ../CLOZE.md; it writes recall-read.txt for the read-through with recall on."""
import json, re, html, os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..', '..')
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', 'trauma.html')
def _load(name, path):
    sp = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
M = _load('trauma_content', os.path.join(HERE, 'content.py'))
DR = _load('trauma_draw', os.path.join(HERE, 'draw.py'))
E = json.load(open(os.path.join(ROOT, 'data', 'explain.json')))['decks']
Q = json.load(open(os.path.join(ROOT, 'data', 'qbank.json')))
C = {}
for l in open(os.path.join(HERE, 'cards.jsonl')):
    if l.strip():
        r = json.loads(l); C[(r['deck'], r['code'])] = r

# ------------------------------------------------------------------ text
CZ = re.compile(r'\{\?(.+?)(?:\|(.+?))?\?\}')
def inl(s, cz=True):
    s = html.escape(s, quote=False)
    if cz:
        s = CZ.sub(lambda m: '<span class="cz" tabindex="0"><span class="czw">%s</span><span class="czg">%s</span></span>' % (m.group(1), '(%s)' % m.group(2) if m.group(2) else '?'), s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'<i>\1</i>', s)
    return s
def plain(s):
    s = re.sub(r'\*\*|<[^>]+>', '', s)
    return html.unescape(s)
def md(s):
    out, tb = [], []
    def flush():
        if tb:
            rows = [[c.strip() for c in r.strip().strip('|').split('|')] for r in tb]
            h = '<tr>' + ''.join('<th>%s</th>' % inl(c, False) for c in rows[0]) + '</tr>'
            b = ''.join('<tr>' + ''.join('<td>%s</td>' % inl(c, False) for c in r) + '</tr>' for r in rows[1:])
            out.append('<div class="gw"><table class="ct">%s%s</table></div>' % (h, b)); tb.clear()
    for l in s.split('\n'):
        if ' | ' in l: tb.append(l); continue
        flush()
        if l.strip(): out.append('<div class="ln">%s</div>' % inl(l, False))
    flush()
    return ''.join(out)
def pct(s):
    m = re.findall(r'(\d{1,3})% (?:right|chose|correct)', s) or re.findall(r'\((\d{1,3})%\)', s)
    return min(int(x) for x in m) if m else None
def heat(h): return sum(c.get('n', 1) for c in h.get('chips', [])) if h else 0
def chips(h): return ''.join('<span class="chip">%s ×%d</span>' % (html.escape(c['t']), c['n']) for c in (h or {}).get('chips', []))

# ------------------------------------------------------------------ visuals (markup of the GI page)
def render_vis(v):
    k = v['kind']; t = '<div class="vt">%s</div>' % inl(v['title'])
    note = '<div class="vn">%s</div>' % inl(v['note']) if v.get('note') else ''
    if k == 'svg':
        return '<div class="vis v-svg">%s<div class="svgw">%s</div>%s</div>' % (t, getattr(DR, v['key'])(), note)
    if k == 'stations':
        parts = []
        for i, st in enumerate(v['stations']):
            if i: parts.append('<div class="st-ar">%s</div>' % html.escape(v.get('mark', '→')))
            parts.append('<div class="st-s"><div class="st-n">%d</div><div class="st-h">%s</div><div class="st-w">%s</div>%s</div>' % (
                i + 1, inl(st['h']), inl(st.get('w', '')), ''.join('<div class="st-d">%s</div>' % inl(d) for d in st['d'])))
        return '<div class="vis v-stations">%s<div class="st">%s</div>%s</div>' % (t, ''.join(parts), note)
    if k == 'timeline':
        return '<div class="vis v-timeline">%s<div class="tl">%s</div>%s</div>' % (t, ''.join(
            '<div class="tl-s"><div class="tl-w">%s</div><div class="tl-b"><div class="tl-h">%s</div><div>%s</div>%s</div></div>' % (
                inl(w), inl(h), inl(d), ('<div class="tl-y">%s</div>' % inl(y)) if y else '') for w, h, d, y in v['steps']), note)
    if k == 'ladder':
        return '<div class="vis v-ladder">%s<div class="ld">%s</div>%s</div>' % (t, ''.join(
            '<div class="ld-r ld-%d"><div class="ld-x">%s</div><div class="ld-l"><b>%s</b><span>%s</span></div></div>' % (
                min(i, 2), inl(x), inl(h), inl(d)) for i, (x, h, d) in enumerate(v['rungs'])), note)
    if k == 'chips':
        return '<div class="vis v-chips">%s<div class="cp">%s</div>%s</div>' % (t, ''.join(
            '<div class="cp-i"><b>%s</b><span>%s</span></div>' % (inl(a), inl(b)) for a, b in v['items']), note)
    if k == 'grid':
        head = '<tr><th class="g2c">%s</th>%s</tr>' % (inl(v.get('rlab', '')), ''.join('<th>%s</th>' % inl(c) for c in v['cols']))
        body = ''.join('<tr><th>%s</th>%s</tr>' % (inl(r), ''.join('<td><b>%s</b>%s</td>' % (inl(a), ('<span>%s</span>' % inl(b)) if b else '') for a, b in cells)) for r, cells in v['rows'])
        return '<div class="vis v-grid">%s<div class="gw"><table class="g2">%s%s</table></div>%s</div>' % (t, head, body, note)
    raise ValueError(k)
def vis_text(v):
    """everything a visual prints, for the giveaway check"""
    k = v['kind']; xs = [v['title'], v.get('note', '')]
    if k == 'svg': xs.append(plain(getattr(DR, v['key'])()))
    if k == 'stations':
        for st in v['stations']: xs += [st['h'], st.get('w', '')] + st['d']
    if k == 'timeline':
        for s in v['steps']: xs += list(s)
    if k == 'ladder':
        for r in v['rungs']: xs += list(r)
    if k == 'chips':
        for a, b in v['items']: xs += [a, b]
    if k == 'grid':
        xs += v['cols']
        for r, cells in v['rows']: xs += [r] + [x for c in cells for x in c]
    return xs

PAL = ['#1f5fbf', '#c0561e', '#2e7d32', '#6d4c41', '#00838f', '#ad1457']
def dtree(t, depth=0):
    h = ''
    if depth == 0: h += '<div class="dt"><div class="dt-start">%s</div><div class="dt-arrow">▼</div>' % inl(t['start'])
    h += '<div class="dt-q">%s</div><div class="dt-row">' % inl(t['q'])
    for i, br in enumerate(t['b']):
        h += '<div class="dt-b" style="--c:%s"><div class="dt-a">%s</div><div class="dt-arrow">▼</div>' % (PAL[i % len(PAL)], inl(br['a']))
        if 'q' in br: h += dtree(br, depth + 1)
        else: h += '<div class="dt-dx"><b>%s</b>%s</div>' % (inl(br['dx']), ('<span>%s</span>' % inl(br['c'])) if br.get('c') else '')
        h += '</div>'
    h += '</div>'
    if depth == 0: h += '</div>'
    return h
def pair_html(p):
    A, B, shared, rows = p
    sh = '<div class="pv-same"><div class="pv-lbl">= Same in both</div><div class="pv-chips">' + ''.join('<span>%s</span>' % inl(x) for x in shared) + '</div></div>'
    body = ''.join('<tr class="%s"><th>%s%s</th><td>%s</td><td>%s</td></tr>' % ('key' if f.startswith('!') else '', '★ ' if f.startswith('!') else '', inl(f.lstrip('!')), inl(a), inl(b)) for f, a, b in rows)
    tb = '<div class="pv-lbl pv-diff">≠ How they differ <span class="pv-hint">★ = the row that decides</span></div><table class="pv-t"><tr><th></th><th class="ca">A · %s</th><th class="cb">B · %s</th></tr>%s</table>' % (inl(A), inl(B), body)
    return '<div class="pv"><div class="pv-h"><span class="ca">A · %s</span> <i>vs</i> <span class="cb">B · %s</span></div>%s%s</div>' % (inl(A), inl(B), sh, tb)

# ------------------------------------------------------------------ the blank check (../CLOZE.md)
problems, readout = [], []
def norm(s): return re.sub(r'\s+', ' ', s.replace('−', '-').replace('–', '-').lower()).strip()
def check_blanks(Cn, lines, others):
    """lines: every visible text line that may hold blanks; others: other visible text on the screen"""
    blanks = []
    for ln in lines:
        bs = CZ.findall(ln)
        if not bs: continue
        if len(bs) > 2: problems.append((Cn['id'], 'three or more blanks in one line', ln))
        open_words = len(re.findall(r'[A-Za-z0-9]+', plain(CZ.sub(' ', ln))))
        if open_words < 4: problems.append((Cn['id'], 'fewer than 4 open words', ln))
        for a, lab in bs:
            if len(a.split()) > 4: problems.append((Cn['id'], 'answer longer than 4 words', a))
            blanks.append((a, ln))
    # giveaway: the answer printed anywhere else on the screen, with every blank covered
    covered = [norm(plain(CZ.sub(' ▢ ', x))) for x in lines + others]
    for a, ln in blanks:
        na = norm(a)
        pat = re.compile(r'(?<![\w])' + re.escape(na) + r'(?![\w])')
        hits = [x for x in covered if pat.search(x)]
        if hits and a not in M.WAIVE.get(Cn['id'], {}):
            problems.append((Cn['id'], 'answer “%s” is printed elsewhere on the screen' % a, hits[0][:140]))
    return blanks

# ------------------------------------------------------------------ build
placed_cards, placed_tops, stats = set(), set(), dict(concepts=0, cards=0, hits=0, tops=0, blanks=0, traps=0, asked=0, pairs=0)
home, body = [], []
for G in M.GROUPS:
    D = E[G['primer']]
    tiles = []
    for Cn in [c for c in M.CONCEPTS if c['group'] == G['id']]:
        stats['concepts'] += 1; sid = Cn['id']
        incards = [(d, c, E[d]['cards'][c]) for d, c in Cn['cards']]
        tops = []
        for d, tid in Cn['tops']:
            xt = {t['id']: t for t in E[d].get('topups', [])}[tid]
            qt = {t['id']: t for t in Q['topups'].get(d, [])}.get(tid, {})
            tops.append((d, xt, qt))
        for d, c, v in incards:
            assert (d, c) not in placed_cards, ('card placed twice', d, c); placed_cards.add((d, c))
        for d, t, _ in tops:
            assert t['id'] not in placed_tops, ('top-up placed twice', t['id']); placed_tops.add(t['id'])
        B = {'top': [], 'm': [], 't': [], 'c': [], 'a': []}
        # --- the notes: summary, the concept in order, the visuals
        B['top'].append('<div class="concept">%s</div>' % inl(Cn['summary']))
        B['top'].append('<div class="rcbar"><button class="rall">Reveal all</button><button class="rcov">Cover all again</button><span class="rcnote">Tap a box to uncover it. The tabs below stay shut until you open one.</span></div>')
        B['top'].append('<div class="rc"><div class="sec">The concept, in order</div><ol class="flow">' + ''.join('<li>%s</li>' % inl(x) for x in Cn['core']) + '</ol></div>')
        for v in Cn.get('vis', []): B['top'].append('<div class="rc">%s</div>' % render_vis(v))
        vis_lines = [x for v in Cn.get('vis', []) for x in vis_text(v)]
        bl = check_blanks(Cn, Cn['core'] + vis_lines, [Cn['summary'], Cn['title']])
        stats['blanks'] += len(bl)
        readout.append('\n==== %s · %s\n%s' % (sid, Cn['title'], plain(Cn['summary'])))
        for x in Cn['core'] + [y for y in vis_lines if CZ.search(y)]:
            readout.append('  - ' + plain(CZ.sub(lambda m: '[_____ %s]' % ('(%s)' % m.group(2) if m.group(2) else '?'), x)))
        # --- mimics: pairs, trees, then the cards' own pairs
        for tr in Cn.get('trees', []):
            tid = sid + '-tree'
            B['m'].append('<button class="tg" data-t="%s">Show the decision tree</button><div class="treebox" id="%s" hidden>%s</div>' % (tid, tid, dtree(tr)))
        for p in Cn.get('pairs', []): B['m'].append(pair_html(p)); stats['pairs'] += 1
        mims = [(c, m) for d, c, v in incards for m in v.get('mimic', [])] + [('Top-up', m) for d, t, _ in tops for m in t['x'].get('mimic', [])]
        if mims:
            B['m'].append('<details class="more"><summary>More pairs from the cards (%d)</summary>' % len(mims) + ''.join(
                '<div class="mim"><div class="mt"><span class="src">%s</span> %s</div><div class="mtext">%s</div></div>' % (c, inl(a, False), inl(b, False)) for c, (a, b) in mims) + '</details>')
        # --- traps, lowest % right first
        trs = [(c, t) for d, c, v in incards for t in v.get('traps', [])] + [('Top-up', tr) for d, t, _ in tops for tr in t['x'].get('traps', [])]
        trs.sort(key=lambda x: (0, pct(x[1][1])) if pct(x[1][1]) is not None else (1, 0))
        for c, (w, why) in trs:
            p = pct(why); tag = ' <span class="low">%d%% right</span>' % p if p is not None and p < 70 else ''
            B['t'].append('<div class="trap2"><div class="wrong"><span class="src">%s</span> <s>%s</s>%s</div><button class="rv">Why wrong?</button><div class="ans" hidden>%s</div></div>' % (c, inl(w, False), tag, inl(why, False)))
        stats['traps'] += len(trs)
        # --- cards: every card of the concept, the most-asked first; then the top-ups
        def card_html(d, c, v):
            h = Q['cards'].get(d + '|' + c); r = C[(d, c)]
            hn = heat(h); fl = '🔥' * min(3, max(1, hn // 3)) if hn else ''
            x = ['<div class="card%s" id="%s-%s"><div class="ch"><b>%s</b> <span class="dkl">%s</span> <span class="heat">%s</span> %s%s <button class="mk" data-k="%s">Missed</button></div>' % (
                '' if hn else ' cold', sid, c, c, d, fl, chips(h), '' if hn else '<span class="chip">not yet asked</span>', c)]
            if v.get('intro'): x.append('<div class="intro"><b>Before the card:</b> %s</div>' % inl(v['intro'], False))
            x.append('<div class="cq">%s</div><button class="rv">Show answer</button><div class="ans" hidden>%s' % (md(r['q']), md(r['a'])))
            if r.get('watch'): x.append('<div class="watch"><b>Watch:</b> %s</div>' % inl(r['watch'].replace('\n', ' '), False))
            if v.get('why'): x.append('<details><summary>Why, part by part</summary><ul class="why">' + ''.join('<li><b class="pl">%s</b> %s</li>' % (html.escape(p), inl(t, False)) for p, t in v['why']) + '</ul></details>')
            if v.get('table'):
                tb = v['table']
                x.append('<details><summary>%s</summary><div class="gw"><table class="ct"><tr>%s</tr>%s</table></div></details>' % (inl(tb.get('title', 'Table'), False), ''.join('<th>%s</th>' % inl(y, False) for y in tb['head']), ''.join('<tr>' + ''.join('<td>%s</td>' % inl(y, False) for y in rr) + '</tr>' for rr in tb['rows'])))
            if h and h.get('lines'): x.append('<div class="tul"><div class="lbl">Top-up lines</div><ul>' + ''.join('<li>%s</li>' % inl(l, False) for l in h['lines']) + '</ul></div>')
            if h and h.get('cross'): x.append('<div class="cross"><div class="lbl">Crossfire: bank key vs guideline</div><ul>' + ''.join('<li>%s</li>' % inl(l, False) for l in h['cross']) + '</ul></div>')
            if v.get('punch'): x.append('<div class="punch">%s</div>' % inl(v['punch'], False))
            x.append('</div></div>')
            return ''.join(x), hn
        made = sorted((card_html(d, c, v) for d, c, v in incards), key=lambda z: -z[1])
        for hcode, hn in made:
            B['c'].append(hcode); stats['cards'] += 1; stats['hits'] += 1 if hn else 0
        for d, t, qt in tops:
            stats['tops'] += 1; x = t['x']; tid = sid + '-TU-' + t['id']
            B['c'].append('<div class="card tu" id="%s"><div class="ch"><b>Top-up</b> · %s <span class="chip">%s</span> <span class="chip">%d questions</span> <button class="mk" data-k="%s">Missed</button></div>' % (
                tid, html.escape(t['topic']), html.escape(t.get('banks', '')), t.get('n', 0), 'TU ' + t['topic'][:28]))
            ans = [re.sub(r'^-\s*', '', l) for l in t['a']]
            B['c'].append('<div class="cq">%s</div><button class="rv">Show answer</button><div class="ans" hidden><ul>%s</ul>' % (inl(t['q'], False), ''.join('<li>%s</li>' % inl(l, False) for l in ans)))
            if x.get('why'): B['c'].append('<details><summary>Why, part by part</summary><ul class="why">' + ''.join('<li><b class="pl">%s</b> %s</li>' % (html.escape(p), inl(tx, False)) for p, tx in x['why']) + '</ul></details>')
            B['c'].append('</div></div>')
        # --- asked: the banks' real questions first, practice items folded
        des = [(c, dd) for d, c, v in incards for dd in v.get('decode', [])] + [(c, (p['q'], p['a'])) for d, c, v in incards for p in (v.get('parts') or [])]
        des += [('Top-up', dd) for d, t, _ in tops for dd in t['x'].get('decode', [])]
        real = [x for x in des if '[pattern]' not in x[1][0]]; prac = [x for x in des if '[pattern]' in x[1][0]]
        def dq(c, st, key, i):
            p = pct(key); fl = ' <span class="low">only %d%% right</span>' % p if p is not None and p < 50 else ''
            k = 'Q-%s-%d' % (sid, i)
            return '<div class="dq" id="%s-%s"><div class="stem"><span class="src">%s</span> %s%s</div><button class="rv">Show key</button> <button class="mk" data-k="%s">Missed</button><div class="ans" hidden>%s</div></div>' % (sid, k, c, inl(st, False), fl, k, inl(key, False))
        for i, (c, (st, key)) in enumerate(real): B['a'].append(dq(c, st, key, i + 1))
        stats['asked'] += len(real)
        if prac: B['a'].append('<details class="more"><summary>Practice items written from the cards, not bank questions (%d)</summary>' % len(prac) + ''.join(dq(c, st.replace(' [pattern]', ''), key, 100 + i) for i, (c, (st, key)) in enumerate(prac)) + '</details>')
        cnt = {'m': len(Cn.get('pairs', [])) + len(Cn.get('trees', [])), 't': len(trs), 'c': len(incards) + len(tops), 'a': len(real)}
        tabs = [('m', 'Mimics'), ('t', 'Traps'), ('c', 'Cards'), ('a', 'Asked')]
        tiles.append((sid, Cn['title'], len(incards) + len(tops), sum(1 for d, c, v in incards if (d + '|' + c) in Q['cards']) + len(tops)))
        body.append('<section class="view con" id="%s" hidden><div class="vh"><button class="home">← Concepts</button> <span class="sn">%s</span> <b>%s</b></div>' % (sid, html.escape(G['title'].split(':')[0]), html.escape(Cn['title'])))
        body.append(''.join(B['top']))
        body.append('<div class="tabs">' + ''.join('<button class="tab" data-p="%s-%s">%s <span class="cnt">%d</span></button>' % (sid, k, n, cnt[k]) for k, n in tabs) + '</div>')
        for k, n in tabs:
            body.append('<div class="pane" id="%s-%s" hidden>%s</div>' % (sid, k, ''.join(B[k]) or '<div class="empty">Nothing here for this concept.</div>'))
        body.append('<div class="vf"><button class="done" data-s="%s">Mark concept done ✓</button></div></section>' % sid)
    spine = ''.join('<li><b>%s.</b> %s</li>' % (html.escape(a), html.escape(b)) for a, b in D.get('spine', []))
    home.append('<div class="dk"><h2>%s</h2><details><summary>Before you start</summary><p>%s</p><ol>%s</ol></details><div class="tiles">' % (html.escape(G['title']), inl(D['primer'], False), spine))
    for i, (sid, tt, n, nh) in enumerate(tiles):
        home.append('<button class="tile" data-go="%s"><span class="tn2">Concept %d · %d cards</span>%s</button>' % (sid, i + 1, n, html.escape(tt)))
    home.append('</div></div>')

# coverage: every card and every top-up of both decks, exactly once
for dk in ('SPECIAL05A', 'SPECIAL05B'):
    miss = {(dk, c) for c in E[dk]['cards']} - placed_cards
    assert not miss, ('cards not placed', sorted(miss))
    tmiss = {t['id'] for t in E[dk].get('topups', [])} - placed_tops
    assert not tmiss, ('top-ups not placed', tmiss)
assert all(k.split('|')[0] in ('SPECIAL05A', 'SPECIAL05B') for k in Q['cards'] if k.startswith('SPECIAL05'))

open(os.path.join(HERE, 'recall-read.txt'), 'w').write('Every concept as it reads with recall on. For each blank: would I know what is asked? Is there only one right answer?\n' + '\n'.join(readout) + '\n')
if problems:
    print('BLANK PROBLEMS (%d) — see ../CLOZE.md' % len(problems))
    for p in problems: print('  [%s] %s :: %s' % p)
    sys.exit(1)

CSS = open(os.path.join(HERE, 'style.css')).read()
JS = open(os.path.join(HERE, 'app.js')).read()
P = M.PAGE
HEAD = ('<link rel="manifest" href="%s.webmanifest"><meta name="theme-color" content="%s"><link rel="apple-touch-icon" href="icons/%s-192.png">'
        '<link rel="stylesheet" href="css/ink.css"><link rel="stylesheet" href="css/desk.css">' % (P['slug'], P['theme'], P['slug']))
TAIL = ("<script>if('serviceWorker' in navigator&&location.protocol!=='file:'){addEventListener('load',function(){"
        "navigator.serviceWorker.register('sw.js',{scope:'./'}).then(function(r){r.addEventListener('updatefound',function(){"
        "var n=r.installing;n&&n.addEventListener('statechange',function(){if(n.state==='installed'&&navigator.serviceWorker.controller)"
        "location.reload()})})}).catch(function(){})})}</script><script type=\"module\" src=\"js/desk.js\"></script>")
page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title><style>%s</style>%s</head><body>
<header><h1>%s</h1><button id="rcbtn" title="Cover the chosen facts in the notes; tap a box to uncover it">Recall: off</button></header>
<main><section class="view" id="HOME"><div class="prog"><i id="pb"></i></div><div class="sub" id="pc"></div><div class="dk-all">Read the notes open, write beside them, then switch Recall on and test yourself. Every card of both decks is inside its concept; the ones the banks asked carry a 🔥.</div>%s
<div class="util"><button class="gtile" data-go="MISS">Miss list (<span id="mc">0</span>)</button></div></section>
<section class="view" id="MISS" hidden><div class="vh"><button class="home">← Concepts</button> <b>Miss list</b> <button id="mclr" style="font-size:11.5px;padding:2px 8px">Clear</button></div><div id="mclrq" hidden style="margin:6px 0">Clear every mark? <button id="mclry">Yes, clear</button></div><ul id="ml"></ul></section>
%s
</main><script>%s</script>%s</body></html>""" % (P['doc'], CSS, HEAD, P['title'], '\n'.join(home), '\n'.join(body), JS, TAIL)
open(OUT, 'w').write(page)
print(stats, len(page))
