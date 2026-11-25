# -*- coding: utf-8 -*-
import json, re, html, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', 'shock1.html')
import vis as V, draw as D
from content import SECTIONS, TITLE, SUB, TRAPS

S1 = {q['q']: q for q in json.load(open(os.path.join(HERE, 'S1.json')))}

def esc(s): return html.escape(s, quote=False)

def md(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return s

def parse(text):
    """Pull [[keys]] and {{boxes}} out of a lesson; return (keys, boxes, prose)."""
    keys = re.findall(r'\[\[(.+?)\]\]', text, re.S)
    boxes = re.findall(r'\{\{(.+?)\}\}', text, re.S)
    prose = re.sub(r'\{\{.+?\}\}', '', text, flags=re.S)
    prose = re.sub(r'\[\[(.+?)\]\]', r'\1', prose, flags=re.S)
    prose = re.sub(r'\n{3,}', '\n\n', prose).strip()
    return [k.strip() for k in keys], [b.strip() for b in boxes], prose

def box_html(b):
    lines = [l for l in b.split('\n') if l.strip()]
    rows = [l for l in lines if ' | ' in l]
    if len(rows) >= 2:
        head = [c.strip() for c in rows[0].split('|')]
        h = '<div class="gw"><table class="ct"><tr>%s</tr>' % ''.join('<th>%s</th>' % md(c) for c in head)
        for r in rows[1:]:
            h += '<tr>%s</tr>' % ''.join('<td>%s</td>' % md(c.strip()) for c in r.split('|'))
        h += '</table></div>'
        pre = [l for l in lines if ' | ' not in l]
        return ('<div class="cardbox">%s%s</div>' % (''.join('<div>%s</div>' % md(l) for l in pre), h))
    return '<div class="cardbox">%s</div>' % ''.join('<div>%s</div>' % md(l) for l in lines)

def wrapsvg(x):
    return ('<figure class="vis"><div class="svgw">%s</div></figure>' % x) if x.lstrip().startswith('<svg') else x

def prose_html(p):
    return ''.join('<p>%s</p>' % md(x.strip()) for x in p.split('\n') if x.strip())

def keys_html(ks, lab='Carry this'):
    if not ks: return ''
    return '<div class="keys"><div class="lbl">%s</div>%s</div>' % (
        lab, ''.join('<div class="key1">%s</div>' % md(k) for k in ks))

# ---------------------------------------------------------------- screens
screens = []   # (id, kind, html, label)
tiles = []     # for the packet view

n_card = 0
for si, sec in enumerate(SECTIONS):
    src = S1[sec['q']]
    # ---- opener
    ok, ob, op = parse(src['open']['text'])
    h = ['<div class="shead"><span class="sn">%s</span><h2>%s</h2></div>' % (esc(sec['n']), esc(sec['title']))]
    h.append('<div class="spine"><div class="lbl">What this section settles</div><ol>%s</ol></div>' %
             ''.join('<li>%s</li>' % md(x) for x in src['spine']))
    h += [wrapsvg(x) for x in sec['opener']]
    h.append(keys_html(ok))
    h.append('<details class="lesson"><summary>Read the opening lesson</summary>%s</details>' % prose_html(op))
    screens.append(('%s-open' % sec['id'], 'open', ''.join(h), '%s · opening' % sec['n']))
    tiles.append(('sec', sec, '%s-open' % sec['id']))
    # ---- cards
    for ci, c in enumerate(sec['cards']):
        st = src['steps'][ci]
        assert st['card'] == c['code'], (st['card'], c['code'])
        n_card += 1
        ks, bs, pr = parse(st['lesson']['text'])
        deck, code = c['code'].split('|')
        h = ['<div class="chead"><span class="code">%s</span><span class="deck">%s</span>'
             '<span class="pos">card %d of 25</span></div><h2>%s</h2>' % (esc(code), esc(deck), n_card, esc(c['t']))]
        h.append(keys_html(ks))
        h += [wrapsvg(x) for x in c['vis']]
        for b in bs: h.append(box_html(b))
        h.append('<details class="lesson"><summary>Read the lesson behind this card</summary>%s</details>' % prose_html(pr))
        if st.get('bridge'):
            h.append('<div class="bridge"><span>next</span>%s</div>' % md(st['bridge']))
        screens.append(('%s-%s' % (sec['id'], code), 'card', ''.join(h), '%s · %s' % (code, c['t'])))
        tiles.append(('card', dict(code=code, deck=deck, t=c['t'], n=n_card), '%s-%s' % (sec['id'], code)))

# ---- closing
last = S1['P12-105']
ck, cb, cp = parse(last['close']['text'])
h = ['<div class="shead"><span class="sn">Closing</span><h2>Walk back through it</h2></div>']
h.append(V.three({'filling': ('read', 'the IVC, the leg raise, the CVP'),
                  'pump': ('read', 'the wedge with a low index, the echo'),
                  'squeeze': ('read', 'warm or cold, the SVR')},
                 'You can now read which number failed',
                 note='The definitions told you when a failing pump counts as shock. The bedside told you the same story with your hands. The catheter wrote it in four columns, the probe showed it in pictures, and the last four cards asked whether filling was still worth giving.'))
h.append('<div class="lbl" style="margin:18px 0 2px">The six traps NEET has actually set — hear the wrong answer first</div>')
for i, (stem, wrong, right) in enumerate(TRAPS):
    h.append('<div class="trap"><div class="tnum">%d</div><div class="tbody">'
             '<div class="tstem">%s</div>'
             '<div class="twrong"><span>tempting</span><s>%s</s></div>'
             '<button class="rv">Show what is actually going on</button><div class="ans" hidden>%s</div>'
             '</div></div>' % (i + 1, md(stem), md(wrong), md(right)))
h.append(keys_html(ck, 'And the two the closing lesson spells out'))
h.append('<details class="lesson"><summary>Read the closing lesson</summary>%s</details>' % prose_html(cp))
h.append('<div class="bridge"><span>next</span>Shock II: you can read which number has failed. What do you push with?</div>')
screens.append(('CLOSE', 'close', ''.join(h), 'Closing lesson'))
tiles.append(('util', dict(t='Closing lesson', s='walk back through the packet, and the six traps'), 'CLOSE'))

# ---- drill
d = last['drill']
h = ['<div class="shead"><span class="sn">Check</span><h2>The closing questions</h2></div>'
     '<div class="sub">Answer each one in your head before you open it. The numbers are there on purpose.</div>']
for i, x in enumerate(d):
    h.append('<div class="dq"><div class="dn">%d</div><div class="dbody"><div class="dqq">%s</div>'
             '<button class="rv">Show answer</button><div class="ans" hidden>%s</div></div></div>' % (i + 1, md(x['q']), md(x['a'])))
screens.append(('DRILL', 'drill', ''.join(h), 'Closing questions (%d)' % len(d)))
tiles.append(('util', dict(t='Closing questions', s='%d of them' % len(d)), 'DRILL'))

# ---------------------------------------------------------------- packet view
pk = ['<div class="phead"><div class="sub">%s</div>'
      '<button class="walk" data-go="%s">▶  Walk the whole packet</button>'
      '<div class="hint">The walk runs in order: each section’s opening lesson, its cards, then the closing lesson and the closing questions. Or tap any card to open it alone.</div></div>' % (
      esc(SUB), screens[0][0])]
i = 0
for t in tiles:
    if t[0] == 'sec':
        if i: pk.append('</div>')
        sec = t[1]
        pk.append('<div class="secblk"><button class="sectile" data-go="%s"><span class="sn">%s</span>%s<span class="go">opening lesson →</span></button><div class="tiles">' % (
            t[2], esc(sec['n']), esc(sec['title'])))
        i += 1
    elif t[0] == 'card':
        c = t[1]
        pk.append('<button class="tile" data-go="%s"><span class="tn">%d</span><span class="tc">%s</span>%s</button>' % (
            t[2], c['n'], esc(c['code']), esc(c['t'])))
    else:
        if i: pk.append('</div></div>'); i = 0
        u = t[1]
        pk.append('<button class="utile" data-go="%s"><b>%s</b><span>%s</span></button>' % (t[2], esc(u['t']), esc(u.get('s', ''))))
if i: pk.append('</div></div>')

# ---------------------------------------------------------------- page
body = ['<section class="view" id="HOME">%s</section>' % ''.join(pk)]
for i, (sid, kind, h, lab) in enumerate(screens):
    prev = screens[i - 1][0] if i else 'HOME'
    nxt = screens[i + 1][0] if i + 1 < len(screens) else None
    nav = ('<div class="nav"><button class="go" data-go="%s">←  back</button>'
           '<span class="pill">%d / %d</span>'
           '%s</div>') % (prev, i + 1, len(screens),
                          ('<button class="go nxt" data-go="%s">next  →</button>' % nxt) if nxt else '<button class="go nxt" data-go="HOME">finish  ✓</button>')
    body.append('<section class="view" id="%s" hidden><div class="top"><button class="home">←  All cards</button>'
                '<span class="where">%s</span></div>%s%s</section>' % (sid, esc(lab), h, nav))

CSS = open(os.path.join(HERE, 'style.css')).read()
# what makes it an installable page with the desk: its manifest, the desk styles, the worker and desk.js
HEAD = ('<link rel="manifest" href="shock1.webmanifest"><meta name="theme-color" content="#1c3461">'
        '<link rel="apple-touch-icon" href="icons/shock1-192.png"><link rel="stylesheet" href="css/ink.css">'
        '<link rel="stylesheet" href="css/desk.css">')
TAIL = ("""<script>if('serviceWorker' in navigator&&location.protocol!=='file:'){addEventListener('load',function(){"""
        """navigator.serviceWorker.register('sw.js',{scope:'./'}).then(function(r){r.addEventListener('updatefound',function(){"""
        """var n=r.installing;n&&n.addEventListener('statechange',function(){if(n.state==='installed'&&navigator.serviceWorker.controller)"""
        """location.reload()})})}).catch(function(){})})}</script><script type="module" src="js/desk.js"></script>""")
JS = open(os.path.join(HERE, 'app.js')).read()
page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s</title><style>%s</style>%s</head><body>
<header><h1>%s</h1></header><main>%s</main><script>%s</script>%s</body></html>""" % (
    esc(TITLE), CSS, HEAD, esc(TITLE), ''.join(body), JS, TAIL)
open(OUT, 'w').write(page)
print('screens', len(screens), 'cards', n_card, 'bytes', len(page))
