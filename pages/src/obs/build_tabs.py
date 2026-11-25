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

TILES, PRIMER = [], {}
body, nav, cardcount, stats = [], [], 0, {'hit': 0, 'top': 0, 'tr': 0, 'mi': 0, 'de': 0}
for dk, dtitle in DECKS:
    D = E[dk]
    spine = D['spine']
    nav.append('<a href="#%s">%s</a>' % (dk, dk))
    PRIMER[dk] = (dtitle, D['primer'])
    cards = D['cards']
    tops = Q['topups'].get(dk, [])
    for si, (stitle, stext) in enumerate(spine):
        step = si + 1
        sid = '%s-s%d' % (dk, step)
        incards = [c for c, v in cards.items() if v.get('step') == step]
        hits = [c for c in incards if (dk + '|' + c) in Q['cards'] and c in C]
        tsteps = [t for t in tops if TOPUP_STEP.get(t['topic']) == step]
        B = {'top': [], 'm': [], 't': [], 'c': [], 'a': []}
        TILES.append((dk, step, sid, stitle))
        B['top'].append('<div class="concept">%s</div>' % inl(stext))
        if GAP.get((dk, step)):
            B['top'].append('<div class="gap"><div class="lbl">Also needed for the concept (from non-hit cards)</div><ul>' + ''.join('<li>%s</li>' % inl(g) for g in GAP[(dk, step)]) + '</ul></div>')
        if FLAG.get((dk, step)):
            B['top'].append('<div class="flag"><div class="lbl">Key vs guideline</div><ul>' + ''.join('<li>%s</li>' % inl(g) for g in FLAG[(dk, step)]) + '</ul></div>')
        for (iid, it, ip, ic) in IMG.get((dk, step), []):
            B['top'].append('<div class="img" id="%s"><div class="lbl">%s · %s</div><div class="slot">Image slot. Prompt is in the Image prompts section at the end.</div></div>' % (iid, iid, html.escape(it)))
        # mimics
        mims = [(c, m) for c in incards for m in cards[c].get('mimic', [])]
        for t in tsteps:
            for m in (t.get('x') or {}).get('mimic', []): mims.append(('TU', m))
        if mims or TREE.get((dk, step)):
            if TREE.get((dk, step)):
                tid = nid()
                B['m'].append('<button class="tg" data-t="%s">Show the decision tree</button><div class="treebox" id="%s" hidden>%s</div>' % (tid, tid, tree_html(TREE[(dk, step)])))
            for c, (mt, mx) in mims:
                stats['mi'] += 1
                B['m'].append(mimic_html(mt, mx).replace('<div class="mt">', '<div class="mt"><span class="src">%s</span> ' % c, 1))
        # traps
        trs = [(c, t) for c in incards for t in cards[c].get('traps', [])]
        for t in tsteps:
            for tr in (t.get('x') or {}).get('traps', []): trs.append(('TU', tr))
        if trs:
            for c, (w, why) in trs:
                stats['tr'] += 1
                B['t'].append('<div class="trap2"><div class="wrong"><span class="src">%s</span> <s>%s</s></div><button class="rv">Why wrong?</button><div class="ans" hidden>%s</div></div>' % (c, inl(w), inl(why)))
        # hit cards
        if hits or tsteps:
            pass
        for c in sorted(hits, key=lambda x: -heat(Q['cards'][dk + '|' + x])):
            stats['hit'] += 1
            v = cards[c]; h = Q['cards'][dk + '|' + c]; q, a, w = C[c]
            hn = heat(h); fl = '🔥' * min(3, max(1, hn // 2)) if hn else ''
            ex = []
            if v.get('intro'): ex.append('<div class="intro"><b>Before the card:</b> %s</div>' % inl(v['intro']))
            B['c'].append('<div class="card" id="%s-%s"><div class="ch"><b>%s</b> <span class="heat">%s</span> %s <button class="mk" data-k="%s">Missed</button></div>' % (dk, c, c, fl, chips(h), c))
            B['c'].append(''.join(ex))
            B['c'].append('<div class="cq">%s</div><button class="rv">Show answer</button><div class="ans" hidden>%s' % (md(q), md(a)))
            if w: B['c'].append('<div class="watch"><b>Watch:</b> %s</div>' % inl(w))
            if v.get('why'):
                B['c'].append('<details><summary>Why, part by part</summary><ul>' + ''.join('<li><b>%s</b> %s</li>' % (html.escape(p[0]), inl(p[1])) for p in v['why']) + '</ul></details>')
            if v.get('table'):
                tb = v['table']
                B['c'].append('<details><summary>%s</summary><div class="gw"><table><tr>%s</tr>%s</table></div></details>' % (inl(tb.get('title', 'Table')), ''.join('<th>%s</th>' % inl(x) for x in tb['head']), ''.join('<tr>' + ''.join('<td>%s</td>' % inl(x) for x in r) + '</tr>' for r in tb['rows'])))
            if h.get('lines'):
                B['c'].append('<div class="tul"><div class="lbl">Top-up lines</div><ul>' + ''.join('<li>%s</li>' % inl(l) for l in h['lines']) + '</ul></div>')
            if v.get('traps'):
                B['c'].append('<details><summary>Traps on this card (%d)</summary><ul>' % len(v['traps']) + ''.join('<li><s>%s</s> → %s</li>' % (inl(x[0]), inl(x[1])) for x in v['traps']) + '</ul></details>')
            if v.get('punch'): B['c'].append('<div class="punch">%s</div>' % inl(v['punch']))
            B['c'].append('</div></div>')
        for t in tsteps:
            stats['top'] += 1
            x = t.get('x') or {}
            tid = 'TU-' + t['id']
            B['c'].append('<div class="card tu" id="%s"><div class="ch"><b>Top-up</b> · %s <span class="chip">%s</span> <button class="mk" data-k="%s">Missed</button></div>' % (tid, html.escape(t['topic']), html.escape(t.get('banks', '')), tid))
            if x.get('intro'): B['c'].append('<div class="intro"><b>Before the card:</b> %s</div>' % inl(x['intro']))
            a = t['a'] if isinstance(t['a'], list) else [t['a']]
            B['c'].append('<div class="cq">%s</div><button class="rv">Show answer</button><div class="ans" hidden><ul>%s</ul>' % (inl(t['q']), ''.join('<li>%s</li>' % inl(re.sub(r'^-\s*', '', l)) for l in a)))
            if x.get('punch'): B['c'].append('<div class="punch">%s</div>' % inl(x['punch']))
            B['c'].append('</div></div>')
        # sweep cards in last step of OBS02B
        if dk == 'OBS02B' and step == len(spine):
            B['c'].append('<h4>Final sweep (not hits, pure trap training)</h4>')
            for c in ['OBS-42', 'OBS-43']:
                q, a, w = SWEEP[c]
                B['c'].append('<div class="card" id="%s-%s"><div class="ch"><b>%s</b> <button class="mk" data-k="%s">Missed</button></div><div class="cq">%s</div><button class="rv">Show answer</button><div class="ans" hidden>%s%s</div></div>' % (dk, c, c, c, md(q), md(a), ('<div class="watch">%s</div>' % inl(w)) if w else ''))
        # exam check
        des = [(c, d) for c in incards for d in cards[c].get('decode', [])]
        des += [(c, (p['q'], p['a'])) for c in incards for p in cards[c].get('parts', [])]
        for t in tsteps:
            for d in (t.get('x') or {}).get('decode', []): des.append(('TU', d))
        if des:
            for c, (st, key) in des:
                stats['de'] += 1
                p = pct(key); fl = ' <span class="low">only %d%% right</span>' % p if p is not None and p < 50 else ''
                k = 'Q-%s-%d' % (c, stats['de'])
                B['a'].append('<div class="dq"><div class="stem"><span class="src">%s</span> %s%s</div><button class="rv">Show key</button> <button class="mk" data-k="%s">Missed</button><div class="ans" hidden>%s</div></div>' % (c, inl(st), fl, k, inl(key)))
        cnt = {'m': len(B['m']) - (1 if TREE.get((dk, step)) else 0), 't': len(B['t']), 'c': sum(1 for x in B['c'] if 'class="card' in x), 'a': len(B['a'])}
        tabs = [('m', 'Mimics'), ('t', 'Traps'), ('c', 'Cards'), ('a', 'Asked')]
        body.append('<section class="view con" id="%s" hidden><div class="vh"><button class="home">← Concepts</button> <span class="sn">%s · %d</span> <b>%s</b></div>' % (sid, dk, step, html.escape(stitle)))
        body.append(''.join(B['top']))
        body.append('<div class="tabs">' + ''.join('<button class="tab" data-p="%s-%s">%s <span class="cnt">%d</span></button>' % (sid, k, n, cnt[k]) for k, n in tabs) + '</div>')
        for k, n in tabs:
            inner = ''.join(B[k]) or '<div class="empty">Nothing here for this concept.</div>'
            body.append('<div class="pane" id="%s-%s" hidden>%s</div>' % (sid, k, inner))
        body.append('<div class="vf"><button class="done" data-s="%s">Mark concept done ✓</button></div></section>' % sid)

# image prompts section
ip = ['<section class="view deck" id="IMGS" hidden><div class="vh"><button class="home">← Concepts</button> <b>Image prompts</b></div><div class="sub">Paste each prompt into ChatGPT or Gemini, save the picture as its slot number (e.g. IMG-01.png), and send them back to me. Check each against its list.</div>']
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

CSS += """
body{background:#f3f5f9}
.view{background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:12px 0}
.vh{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:8px;font-size:15.5px}
button.home{font-size:13px;padding:4px 10px}
.tabs{display:flex;gap:6px;margin:12px 0 8px;position:sticky;top:52px;background:#fff;padding:6px 0;z-index:5;border-bottom:1px solid var(--line)}
.tab{flex:1;font-size:13.5px;padding:7px 4px;border-radius:8px}
.tab.on{background:var(--acc);color:#fff}
.cnt{font-size:11px;opacity:.8}
.pane{min-height:120px}
.empty{color:var(--mut);font-size:14px;padding:20px 0;text-align:center}
.vf{text-align:center;margin:16px 0 4px}
button.done{font-size:14px;padding:8px 18px}
button.done.on{background:#2e7d32;border-color:#2e7d32;color:#fff}
.dk{margin:14px 0 6px}
.dk h2{font-size:16px;margin:0 0 4px}
.dk details{font-size:13.5px;color:#444;margin-bottom:6px}
.tiles{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:8px}
.tile{text-align:left;border:1px solid #cfd8ea;border-radius:10px;padding:10px 12px;background:#fff;color:var(--ink);font-size:14px;line-height:1.35;cursor:pointer}
.tile .tn2{font-size:11.5px;color:var(--mut);display:block;margin-bottom:2px}
.tile.ok{background:#e8f5e9;border-color:#2e7d32}
.tile.ok .tn2::after{content:"  ✓ done";color:#2e7d32;font-weight:700}
.prog{height:8px;background:#e5e9f0;border-radius:6px;overflow:hidden;margin:6px 0 2px}.prog i{display:block;height:100%;background:#2e7d32}
.util{display:flex;gap:8px;margin-top:12px}.util .tile{flex:1;text-align:center}
"""
JS = """
var tilesDone=function(){try{return JSON.parse(localStorage.getItem('obsdone')||'{}')}catch(e){return {}}};
function setDone(m){try{localStorage.setItem('obsdone',JSON.stringify(m))}catch(e){}}
function load(){try{return JSON.parse(localStorage.getItem('obsmiss')||'{}')}catch(e){return {}}}
function save(m){try{localStorage.setItem('obsmiss',JSON.stringify(m))}catch(e){}}
function show(id,tab){document.querySelectorAll('.view').forEach(function(v){v.hidden=v.id!==id});
 if(id!=='HOME'){var v=document.getElementById(id);var ps=v.querySelectorAll('.pane');if(ps.length){var t=tab||ps[0].id;ps.forEach(function(p){p.hidden=p.id!==t});v.querySelectorAll('.tab').forEach(function(b){b.classList.toggle('on',b.dataset.p===t)});}}
 window.scrollTo(0,0);paint();}
function route(){var h=location.hash.slice(1);if(!h||!document.getElementById(h))h='HOME';var el=document.getElementById(h);
 if(el&&el.classList.contains('view'))show(h);else{var v=el.closest('.view'),p=el.closest('.pane');show(v.id,p?p.id:null);el.scrollIntoView();}}
window.addEventListener('hashchange',route);
document.addEventListener('click',function(ev){var b=ev.target.closest('button,a');if(!b)return;
 if(b.classList.contains('tile')&&b.dataset.go){location.hash=b.dataset.go;}
 if(b.classList.contains('home')){location.hash='HOME';}
 if(b.classList.contains('tab')){var v=b.closest('.view');show(v.id,b.dataset.p);}
 if(b.classList.contains('rv')){var a=b.nextElementSibling;while(a&&!a.classList.contains('ans'))a=a.nextElementSibling;if(a)a.hidden=!a.hidden;}
 if(b.classList.contains('tg')){var t=document.getElementById(b.dataset.t);t.hidden=!t.hidden;b.textContent=t.hidden?'Show the decision tree':'Hide the decision tree';}
 if(b.classList.contains('mk')){var k=b.dataset.k,m=load();if(m[k])delete m[k];else m[k]=(b.closest('[id]')||{}).id||'';save(m);paint();}
 if(b.classList.contains('done')){var d=tilesDone(),s=b.dataset.s;if(d[s])delete d[s];else d[s]=1;setDone(d);if(d[s])location.hash='HOME';else paint();}
 if(b.id==='mclr'&&confirm('Clear the miss list?')){save({});paint();}
});
function paint(){var m=load(),ks=Object.keys(m),d=tilesDone();
 document.querySelectorAll('button.mk').forEach(function(b){b.classList.toggle('on',!!m[b.dataset.k]);b.textContent=m[b.dataset.k]?'Missed ✓':'Missed'});
 document.querySelectorAll('.tile[data-go]').forEach(function(t){t.classList.toggle('ok',!!d[t.dataset.go])});
 document.querySelectorAll('button.done').forEach(function(b){b.classList.toggle('on',!!d[b.dataset.s]);b.textContent=d[b.dataset.s]?'Done ✓ (tap to undo)':'Mark concept done ✓'});
 var n=document.querySelectorAll('.tiles .tile.ok').length,T=document.querySelectorAll('.tiles .tile').length;
 document.getElementById('pc').textContent=n+' of '+T+' concepts done';document.getElementById('pb').style.width=(100*n/T)+'%';
 document.getElementById('ml').innerHTML=ks.length?ks.map(function(k){return '<li><a href="#'+m[k]+'">'+k+'</a></li>'}).join(''):'<li>Nothing marked yet.</li>';document.getElementById('mc').textContent=ks.length;}
route();
"""
home = ['<section class="view" id="HOME"><div class="prog"><i id="pb"></i></div><div class="sub" id="pc"></div>']
for dk, dtitle in DECKS:
    home.append('<div class="dk"><h2>%s · %s</h2><details><summary>Before you start</summary>%s</details><div class="tiles">' % (dk, html.escape(dtitle), inl(PRIMER[dk][1])))
    for (d2, st, sid, stt) in TILES:
        if d2 == dk:
            home.append('<button class="tile" data-go="%s"><span class="tn2">Concept %d</span>%s</button>' % (sid, st, html.escape(stt)))
    home.append('</div></div>')
home.append('<div class="util"><button class="tile" data-go="MISS">Miss list (<span id="mc">0</span>)</button><button class="tile" data-go="IMGS">Image prompts</button></div></section>')
home.append('<section class="view" id="MISS" hidden><div class="vh"><button class="home">← Concepts</button> <b>Miss list</b> <button id="mclr" style="font-size:11.5px;padding:2px 8px">Clear</button></div><ul id="ml"></ul></section>')
page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Obstetrics · NEET-SS concept page, with tricks</title><style>%s</style></head><body>
<header><h1>Obstetrics · NEET-SS, with tricks</h1></header>
<main>%s
%s
</main><script>%s</script></body></html>""" % (CSS, '\n'.join(home), '\n'.join(body), JS)
open('/home/claude/obs/obs.html', 'w').write(page)
print(stats, len(page), len(TILES))
