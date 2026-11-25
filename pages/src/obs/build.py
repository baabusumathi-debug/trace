import json, re, html, sys
sys.path.insert(0, '/home/claude/obs')
from cards import C, SWEEP
from extra import GAP, FLAG, TREE, IMG, TOPUP_STEP

T = '/home/claude/lmv/trace/data/'
E = json.load(open(T + 'explain.json'))['decks']
Q = json.load(open(T + 'qbank.json'))
DECKS = [('OBS01', 'Physiology, recognition, airway, organ support'),
         ('OBS02A', 'Hypertensive disorders, eclampsia, HELLP and fatty liver'),
         ('OBS02B', 'Haemorrhage, AFE, sepsis, heart, arrest, OHSS')]

def inl(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'<i>\1</i>', s)
    return s

def md(s):
    lines = s.replace('\\n', '\n').split('\n')
    out, tb = [], []
    def flush():
        if tb:
            rows = [[c.strip() for c in r.split('|')] for r in tb]
            h = '<tr>' + ''.join('<th>%s</th>' % inl(c) for c in rows[0]) + '</tr>'
            b = ''.join('<tr>' + ''.join('<td>%s</td>' % inl(c) for c in r) + '</tr>' for r in rows[1:])
            out.append('<div class="gw"><table>%s%s</table></div>' % (h, b)); tb.clear()
    for l in lines:
        if ' | ' in l or l.strip().endswith(' |') or l.strip().startswith('| '):
            tb.append(l); continue
        flush()
        if l.strip(): out.append('<div class="ln">%s</div>' % inl(l))
    flush()
    return ''.join(out)

def heat(h):
    n = sum(c.get('n', 1) for c in h.get('chips', [])) if h else 0
    return n

def chips(h):
    if not h or not h.get('chips'): return ''
    return ''.join('<span class="chip">%s ×%d</span>' % (html.escape(c['t']), c['n']) for c in h['chips'])

def pct(s):
    m = re.findall(r'(\d{1,3})% (?:right|chose|correct)', s) or re.findall(r'\((\d{1,3})%\)', s)
    return min(int(x) for x in m) if m else None

def tree_html(node, top=True):
    t, kids = node
    li = '<div class="tn">%s</div>' % inl(t)
    if kids:
        li += '<ul>' + ''.join('<li>%s</li>' % tree_html(k, False) for k in kids) + '</ul>'
    return ('<div class="tree"><div class="troot">%s</div>%s</div>' % (inl(t), '<ul>' + ''.join('<li>%s</li>' % tree_html(k, False) for k in kids) + '</ul>')) if top else li

def mimic_html(title, text):
    names = [n.strip() for n in re.split(r'\s+vs\.?\s+', title)]
    body = None
    if len(names) == 2:
        sent = re.split(r'(?<=\.)\s+', text)
        shared = ''
        rest = text
        if sent and sent[0].lower().startswith('both'):
            shared, rest = sent[0], ' '.join(sent[1:])
        # find "<word>:" markers in rest
        marks = [(m.start(), m.group(1)) for m in re.finditer(r'(?:^|(?<=\.\s))([A-Z][^:.]{1,60}):\s', rest)]
        if len(marks) >= 2:
            a0, b0 = marks[0][0], marks[1][0]
            A, B = rest[a0:b0].strip(), rest[b0:].strip()
            body = ('<div class="shared">%s</div>' % inl(shared) if shared else '') + \
                   '<div class="two"><div class="side">%s</div><div class="side">%s</div></div>' % (inl(A), inl(B))
            if a0 > 0: body = '<div class="shared">%s</div>' % inl(rest[:a0]) + body
    if body is None: body = '<div class="mtext">%s</div>' % inl(text)
    return '<div class="mim"><div class="mt">%s</div>%s</div>' % (inl(title), body)

ids = {'n': 0}
def nid():
    ids['n'] += 1; return 'x%d' % ids['n']

body, nav, cardcount, stats = [], [], 0, {'hit': 0, 'top': 0, 'tr': 0, 'mi': 0, 'de': 0}
for dk, dtitle in DECKS:
    D = E[dk]
    spine = D['spine']
    nav.append('<a href="#%s">%s</a>' % (dk, dk))
    body.append('<section class="deck" id="%s"><h2>%s · %s</h2>' % (dk, dk, html.escape(dtitle)))
    body.append('<div class="primer"><b>Before you start:</b> %s</div>' % inl(D['primer']))
    body.append('<div class="map"><b>Concepts:</b><ol>' + ''.join('<li><a href="#%s-s%d">%s</a></li>' % (dk, i + 1, html.escape(s[0])) for i, s in enumerate(spine)) + '</ol></div>')
    cards = D['cards']
    tops = Q['topups'].get(dk, [])
    for si, (stitle, stext) in enumerate(spine):
        step = si + 1
        sid = '%s-s%d' % (dk, step)
        incards = [c for c, v in cards.items() if v.get('step') == step]
        hits = [c for c in incards if (dk + '|' + c) in Q['cards'] and c in C]
        tsteps = [t for t in tops if TOPUP_STEP.get(t['topic']) == step]
        body.append('<section class="con" id="%s"><h3><span class="sn">%s · %d</span> %s</h3>' % (sid, dk, step, html.escape(stitle)))
        body.append('<div class="concept">%s</div>' % inl(stext))
        if GAP.get((dk, step)):
            body.append('<div class="gap"><div class="lbl">Also needed for the concept (from non-hit cards)</div><ul>' + ''.join('<li>%s</li>' % inl(g) for g in GAP[(dk, step)]) + '</ul></div>')
        if FLAG.get((dk, step)):
            body.append('<div class="flag"><div class="lbl">Key vs guideline</div><ul>' + ''.join('<li>%s</li>' % inl(g) for g in FLAG[(dk, step)]) + '</ul></div>')
        for (iid, it, ip, ic) in IMG.get((dk, step), []):
            body.append('<div class="img" id="%s"><div class="lbl">%s · %s</div><div class="slot">Image slot. Prompt is in the Image prompts section at the end.</div></div>' % (iid, iid, html.escape(it)))
        # mimics
        mims = [(c, m) for c in incards for m in cards[c].get('mimic', [])]
        for t in tsteps:
            for m in (t.get('x') or {}).get('mimic', []): mims.append(('TU', m))
        if mims or TREE.get((dk, step)):
            body.append('<h4>Close mimics</h4>')
            if TREE.get((dk, step)):
                tid = nid()
                body.append('<button class="tg" data-t="%s">Show the decision tree</button><div class="treebox" id="%s" hidden>%s</div>' % (tid, tid, tree_html(TREE[(dk, step)])))
            for c, (mt, mx) in mims:
                stats['mi'] += 1
                body.append(mimic_html(mt, mx).replace('<div class="mt">', '<div class="mt"><span class="src">%s</span> ' % c, 1))
        # traps
        trs = [(c, t) for c in incards for t in cards[c].get('traps', [])]
        for t in tsteps:
            for tr in (t.get('x') or {}).get('traps', []): trs.append(('TU', tr))
        if trs:
            body.append('<h4>Traps: why is this wrong?</h4>')
            for c, (w, why) in trs:
                stats['tr'] += 1
                body.append('<div class="trap2"><div class="wrong"><span class="src">%s</span> <s>%s</s></div><button class="rv">Why wrong?</button><div class="ans" hidden>%s</div></div>' % (c, inl(w), inl(why)))
        # hit cards
        if hits or tsteps:
            body.append('<h4>Hit cards</h4>')
        for c in sorted(hits, key=lambda x: -heat(Q['cards'][dk + '|' + x])):
            stats['hit'] += 1
            v = cards[c]; h = Q['cards'][dk + '|' + c]; q, a, w = C[c]
            hn = heat(h); fl = '🔥' * min(3, max(1, hn // 2)) if hn else ''
            ex = []
            if v.get('intro'): ex.append('<div class="intro"><b>Before the card:</b> %s</div>' % inl(v['intro']))
            body.append('<div class="card" id="%s-%s"><div class="ch"><b>%s</b> <span class="heat">%s</span> %s <button class="mk" data-k="%s">Missed</button></div>' % (dk, c, c, fl, chips(h), c))
            body.append(''.join(ex))
            body.append('<div class="cq">%s</div><button class="rv">Show answer</button><div class="ans" hidden>%s' % (md(q), md(a)))
            if w: body.append('<div class="watch"><b>Watch:</b> %s</div>' % inl(w))
            if v.get('why'):
                body.append('<details><summary>Why, part by part</summary><ul>' + ''.join('<li><b>%s</b> %s</li>' % (html.escape(p[0]), inl(p[1])) for p in v['why']) + '</ul></details>')
            if v.get('table'):
                tb = v['table']
                body.append('<details><summary>%s</summary><div class="gw"><table><tr>%s</tr>%s</table></div></details>' % (inl(tb.get('title', 'Table')), ''.join('<th>%s</th>' % inl(x) for x in tb['head']), ''.join('<tr>' + ''.join('<td>%s</td>' % inl(x) for x in r) + '</tr>' for r in tb['rows'])))
            if h.get('lines'):
                body.append('<div class="tul"><div class="lbl">Top-up lines</div><ul>' + ''.join('<li>%s</li>' % inl(l) for l in h['lines']) + '</ul></div>')
            if v.get('traps'):
                body.append('<details><summary>Traps on this card (%d)</summary><ul>' % len(v['traps']) + ''.join('<li><s>%s</s> → %s</li>' % (inl(x[0]), inl(x[1])) for x in v['traps']) + '</ul></details>')
            if v.get('punch'): body.append('<div class="punch">%s</div>' % inl(v['punch']))
            body.append('<a class="back" href="#%s">↑ back to the concept</a></div></div>' % sid)
        for t in tsteps:
            stats['top'] += 1
            x = t.get('x') or {}
            tid = 'TU-' + t['id']
            body.append('<div class="card tu" id="%s"><div class="ch"><b>Top-up</b> · %s <span class="chip">%s</span> <button class="mk" data-k="%s">Missed</button></div>' % (tid, html.escape(t['topic']), html.escape(t.get('banks', '')), tid))
            if x.get('intro'): body.append('<div class="intro"><b>Before the card:</b> %s</div>' % inl(x['intro']))
            a = t['a'] if isinstance(t['a'], list) else [t['a']]
            body.append('<div class="cq">%s</div><button class="rv">Show answer</button><div class="ans" hidden><ul>%s</ul>' % (inl(t['q']), ''.join('<li>%s</li>' % inl(re.sub(r'^-\s*', '', l)) for l in a)))
            if x.get('punch'): body.append('<div class="punch">%s</div>' % inl(x['punch']))
            body.append('<a class="back" href="#%s">↑ back to the concept</a></div></div>' % sid)
        # sweep cards in last step of OBS02B
        if dk == 'OBS02B' and step == len(spine):
            body.append('<h4>Final sweep (not hits, pure trap training)</h4>')
            for c in ['OBS-42', 'OBS-43']:
                q, a, w = SWEEP[c]
                body.append('<div class="card" id="%s-%s"><div class="ch"><b>%s</b> <button class="mk" data-k="%s">Missed</button></div><div class="cq">%s</div><button class="rv">Show answer</button><div class="ans" hidden>%s%s</div></div>' % (dk, c, c, c, md(q), md(a), ('<div class="watch">%s</div>' % inl(w)) if w else ''))
        # exam check
        des = [(c, d) for c in incards for d in cards[c].get('decode', [])]
        des += [(c, (p['q'], p['a'])) for c in incards for p in cards[c].get('parts', [])]
        for t in tsteps:
            for d in (t.get('x') or {}).get('decode', []): des.append(('TU', d))
        if des:
            body.append('<h4>How they actually asked it</h4>')
            for c, (st, key) in des:
                stats['de'] += 1
                p = pct(key); fl = ' <span class="low">only %d%% right</span>' % p if p is not None and p < 50 else ''
                k = 'Q-%s-%d' % (c, stats['de'])
                body.append('<div class="dq"><div class="stem"><span class="src">%s</span> %s%s</div><button class="rv">Show key</button> <button class="mk" data-k="%s">Missed</button><div class="ans" hidden>%s</div></div>' % (c, inl(st), fl, k, inl(key)))
        body.append('<a class="back" href="#%s">↑ deck top</a></section>' % dk)
    body.append('</section>')

# image prompts section
ip = ['<section class="deck" id="IMGS"><h2>Image prompts</h2><div class="sub">Paste each prompt into ChatGPT or Gemini, save the picture as its slot number (e.g. IMG-01.png), and send them back to me. Check each against its list.</div>']
for k in IMG:
    for (iid, it, p, ck) in IMG[k]:
        ip.append('<div class="ipr"><b>%s · %s</b> <a href="#%s">(slot)</a><pre>%s</pre><div class="ck"><b>Check:</b> %s</div></div>' % (iid, html.escape(it), iid, html.escape(p), html.escape(ck)))
ip.append('</section>')
body += ip

CSS = open('/home/claude/skel/skel.html').read()
CSS = CSS[CSS.index('<style>') + 7:CSS.index('</style>')]
CSS += """
section.deck{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:18px 0}
.primer{background:#f4f0fb;border-left:4px solid #6a4fc4;padding:8px 12px;border-radius:4px;font-size:14.5px;margin:6px 0}
section.con{border-top:2px solid var(--acc);margin-top:22px;padding-top:6px}
.sn{font-size:12px;color:#fff;background:var(--acc);border-radius:10px;padding:1px 8px;vertical-align:middle}
.concept{font-size:16px;font-weight:500;background:#eef3ff;padding:8px 12px;border-radius:8px;margin:6px 0}
h4{margin:16px 0 6px;font-size:14.5px;text-transform:uppercase;letter-spacing:.04em;color:var(--mut)}
.lbl{font-size:12px;font-weight:700;text-transform:uppercase;color:var(--mut);margin-bottom:2px}
.gap{background:#f6f8f6;border-left:4px solid #2e7d32;padding:6px 12px;border-radius:4px;font-size:14.5px;margin:6px 0}
.flag{background:#fdecea;border-left:4px solid var(--warm);padding:6px 12px;border-radius:4px;font-size:14.5px;margin:6px 0}
.gap ul,.flag ul,.tul ul{margin:2px 0;padding-left:18px}
.img .slot{border:2px dashed #b0b8c8;border-radius:8px;padding:18px;text-align:center;color:var(--mut);font-size:13.5px}
.mim{border:1px solid #d9dfeb;border-radius:8px;margin:8px 0;overflow:hidden}
.mt{background:#f1f5fe;padding:6px 10px;font-weight:700;font-size:14.5px}
.shared{color:var(--mut);font-size:13.5px;padding:6px 10px;border-bottom:1px dashed var(--line)}
.two{display:grid;grid-template-columns:1fr 1fr}
.side{padding:8px 10px;font-size:14.5px}.side+.side{border-left:1px solid var(--line)}
.mtext{padding:8px 10px;font-size:14.5px}
@media(max-width:640px){.two{grid-template-columns:1fr}.side+.side{border-left:0;border-top:1px solid var(--line)}}
.src{font-size:11px;color:var(--mut);font-weight:600;background:#f2f2f2;border-radius:6px;padding:0 5px}
.trap2{border-left:3px solid var(--warm);padding:4px 10px;margin:6px 0;background:#fffafa}
.wrong s{color:var(--warm);text-decoration-thickness:1.5px}
.ans{margin-top:6px;font-size:14.5px}
button.rv,button.tg{font-size:12.5px;padding:3px 10px;margin-top:4px}
button.mk{font-size:11.5px;padding:2px 8px;border-color:#999;color:#666;float:right}
button.mk.on{background:var(--warm);border-color:var(--warm);color:#fff}
.card{border:1px solid #cfd8ea;border-radius:10px;padding:10px 12px;margin:10px 0;background:#fcfdff}
.card.tu{border-color:#e0a800;background:#fffdf5}
.ch{font-size:14px;margin-bottom:4px}
.chip{font-size:11px;background:#eef3ff;border-radius:8px;padding:1px 6px;margin-left:4px;color:#334}
.heat{font-size:13px}
.intro{font-size:13.5px;color:#444;background:#f7f7f7;padding:5px 8px;border-radius:6px;margin:4px 0}
.cq{font-size:15px;margin:4px 0}
.ln{margin:2px 0}
.watch{font-size:14px;background:var(--tr);padding:5px 8px;border-radius:4px;margin:6px 0}
.tul{background:#eef7ff;border-left:4px solid var(--acc);padding:6px 10px;border-radius:4px;margin:6px 0;font-size:14px}
.punch{font-weight:600;background:#e8f5e9;padding:6px 10px;border-radius:6px;margin:8px 0;font-size:14.5px}
.punch::before{content:"Punch: ";color:#2e7d32}
.back{font-size:12px;color:var(--acc);display:inline-block;margin-top:4px}
.dq{border-bottom:1px solid #f0f0f0;padding:6px 0}
.stem{font-size:14.5px}.low{background:var(--warm);color:#fff;border-radius:8px;padding:0 6px;font-size:11.5px;margin-left:4px}
.treebox{margin:6px 0 10px}
.tree{border:1px solid #d9dfeb;border-radius:8px;padding:10px;background:#fbfcff;font-size:14px}
.troot{font-weight:700;background:var(--acc);color:#fff;border-radius:6px;padding:6px 10px;display:inline-block}
.tree ul{list-style:none;margin:0;padding-left:22px;border-left:2px solid #b9c7e6;margin-left:10px}
.tree li{position:relative;padding:6px 0 0 10px}
.tree li::before{content:"";position:absolute;left:-2px;top:16px;width:12px;border-top:2px solid #b9c7e6}
.tn{display:inline-block;background:#fff;border:1px solid #cfd8ea;border-radius:6px;padding:4px 8px}
.ipr{border:1px solid var(--line);border-radius:8px;padding:8px 10px;margin:8px 0}
.ipr pre{white-space:pre-wrap;background:#f6f6f6;padding:8px;border-radius:6px;font-size:13px}
.ck{font-size:13.5px}
#miss{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px 14px;margin:12px 0}
#miss ul{margin:4px 0;padding-left:18px;font-size:14px}
"""
JS = """
function tg(e){var n=e.nextElementSibling;n.hidden=!n.hidden;}
document.addEventListener('click',function(ev){var b=ev.target;
 if(b.classList.contains('rv')){var a=b.parentNode.querySelector(':scope > .ans')||b.nextElementSibling;while(a&&!a.classList.contains('ans'))a=a.nextElementSibling;if(a){a.hidden=!a.hidden;}}
 if(b.classList.contains('tg')){var t=document.getElementById(b.dataset.t);t.hidden=!t.hidden;b.textContent=t.hidden?'Show the decision tree':'Hide the decision tree';}
 if(b.classList.contains('mk')){var k=b.dataset.k,m=load();if(m[k])delete m[k];else m[k]=(b.closest('[id]')||{}).id||'';save(m);paint();}
});
function load(){try{return JSON.parse(localStorage.getItem('obsmiss')||'{}')}catch(e){return {}}}
function save(m){try{localStorage.setItem('obsmiss',JSON.stringify(m))}catch(e){}}
function paint(){var m=load(),ks=Object.keys(m);document.querySelectorAll('button.mk').forEach(function(b){b.classList.toggle('on',!!m[b.dataset.k]);b.textContent=m[b.dataset.k]?'Missed ✓':'Missed'});
 var l=document.getElementById('ml');l.innerHTML=ks.length?ks.map(function(k){return '<li><a href="#'+m[k]+'">'+k+'</a></li>'}).join(''):'<li>Nothing marked yet.</li>';document.getElementById('mc').textContent=ks.length;}
document.getElementById('mclr').onclick=function(){if(confirm('Clear the miss list?')){save({});paint();}};
var oa=document.getElementById('oa');oa.onclick=function(){var on=!oa.classList.contains('on');oa.classList.toggle('on');document.querySelectorAll('.ans').forEach(function(a){a.hidden=!on});oa.textContent=on?'Hide all answers':'Show all answers'};
paint();
"""
page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Obstetrics for NEET-SS: concepts, mimics and traps, with tricks</title><style>%s</style></head><body>
<header><h1>Obstetrics · NEET-SS concept page, with tricks</h1><button id="oa">Show all answers</button><nav>%s <a href="#miss">Miss list</a> <a href="#IMGS">Images</a></nav></header>
<main>
<section class="blk"><h2>How to use this</h2><div class="map"><ol>
<li>Each concept follows your deck's own spine. Read the <b>concept line</b> and the green box first.</li>
<li><b>Close mimics</b> build the concept: read each pair side by side; open the <b>decision tree</b> to see how they all split.</li>
<li><b>Traps:</b> say why the struck-out option is wrong before you tap.</li>
<li><b>Hit cards</b> (🔥 = bank hits): try the question, then reveal. Top-up lines are in blue.</li>
<li><b>How they asked it</b> is the exam check; red tags mark questions most people got wrong.</li>
<li>Tap <b>Missed</b> on anything you get wrong; it stays in the Miss list.</li></ol></div></section>
<section id="miss"><b>Miss list (<span id="mc">0</span>)</b> <button id="mclr" style="font-size:11.5px;padding:2px 8px">Clear</button><ul id="ml"></ul></section>
%s
</main><script>%s</script></body></html>""" % (CSS, ' '.join(nav), '\n'.join(body), JS)
open('/home/claude/obs/obs.html', 'w').write(page)
print(stats, len(page))
