# -*- coding: utf-8 -*-
"""Visual renderers for the Shock I page. Each returns an HTML block."""
import html, re

def inl(s):
    s = html.escape(str(s), quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    return s

P = dict(navy='#1c3461', red='#b3261e', amber='#a35a00', green='#2e6b3a',
         teal='#00707d', grey='#5a6472', ink='#1d1d1f', line='#d5dbe8', soft='#f6f8fc')

def wrap(title, body, note=''):
    h = '<figure class="vis">'
    if title: h += '<figcaption>%s</figcaption>' % inl(title)
    h += body
    if note: h += '<div class="vn">%s</div>' % inl(note)
    return h + '</figure>'

# ---------- the three numbers: the packet's anchor ----------
def three(states, title='The three numbers', note='', caption=None):
    """states: dict of filling/pump/squeeze -> (arrow, text). arrow in ok/up/down/fail"""
    sym = {'ok': ('=', 'normal'), 'up': ('▲', 'raised'), 'down': ('▼', 'low'),
           'fail': ('✕', 'FAILED FIRST'), 'na': ('?', 'not yet'), 'read': ('✓', 'you can read it')}
    h = '<div class="three">'
    for k, lab in (('filling', 'FILLING'), ('pump', 'PUMP'), ('squeeze', 'SQUEEZE')):
        st, txt = states.get(k, ('na', ''))
        s, w = sym[st]
        h += ('<div class="tn tn-%s"><div class="tn-h"><span class="tn-s">%s</span> %s</div>'
              '<div class="tn-w">%s</div><div class="tn-t">%s</div></div>') % (st, s, lab, w, inl(txt))
        if k != 'squeeze': h += '<div class="tn-x">×</div>' if k == 'pump' else '<div class="tn-x">→</div>'
    h += '</div>'
    if caption: h += '<div class="vcap">%s</div>' % inl(caption)
    return wrap(title, h, note)

# ---------- flowchart ----------
def flow(nodes, title='', note='', dir='v'):
    """nodes: list of (kind, text, sub). kind: start|step|bad|good|q|end"""
    h = '<div class="flow flow-%s">' % dir
    for i, n in enumerate(nodes):
        kind, t = n[0], n[1]
        sub = n[2] if len(n) > 2 else ''
        if i: h += '<div class="fa">%s</div>' % ('▼' if dir == 'v' else '▶')
        h += '<div class="fn fn-%s"><div class="fn-t">%s</div>%s</div>' % (
            kind, inl(t), ('<div class="fn-s">%s</div>' % inl(sub)) if sub else '')
    return wrap(title, h + '</div>', note)

# ---------- decision branch ----------
def branch(start, q, bs, title='', note=''):
    """bs: list of (answer, result, comment)"""
    cols = [P['navy'], P['red'], P['amber'], P['green'], P['teal'], P['grey']]
    h = '<div class="br"><div class="br-s">%s</div><div class="fa">▼</div><div class="br-q">%s</div><div class="br-row">' % (inl(start), inl(q))
    for i, b in enumerate(bs):
        c = cols[i % len(cols)]
        h += '<div class="br-b" style="--c:%s"><div class="br-a">%s</div><div class="fa">▼</div><div class="br-d"><b>%s</b>%s</div></div>' % (
            c, inl(b[0]), inl(b[1]), ('<span>%s</span>' % inl(b[2])) if len(b) > 2 and b[2] else '')
    return wrap(title, h + '</div></div>', note)

# ---------- vicious cycle ----------
def cycle(nodes, title='', note='', center='', oppose=None):
    h = '<div class="cyc">'
    if center: h += '<div class="cyc-c">%s</div>' % inl(center)
    h += '<ol class="cyc-l">'
    for n in nodes:
        t = n[0]; s = n[1] if len(n) > 1 else ''
        h += '<li><div class="cyc-t">%s</div>%s</li>' % (inl(t), ('<div class="cyc-s">%s</div>' % inl(s)) if s else '')
    h += '</ol><div class="cyc-back">↺ back to the top: the output falls further</div>'
    if oppose: h += '<div class="cyc-op">⊣ pushing the other way: %s</div>' % inl(oppose)
    return wrap(title, h + '</div>', note)

# ---------- grid ----------
def grid(rows, cols, cells, title='', rlab='', clab='', note='', wide=False):
    corner = (inl(rlab) + ' ↓' if rlab else '') + (('<br>' + inl(clab) + ' →') if clab else '')
    h = '<div class="gw"><table class="g2%s"><tr><th class="g2c">%s</th>%s</tr>' % (
        ' wide' if wide else '', corner, ''.join('<th>%s</th>' % inl(c) for c in cols))
    for r, row in zip(rows, cells):
        h += '<tr><th>%s</th>%s</tr>' % (inl(r), ''.join(
            '<td class="%s"><b>%s</b>%s</td>' % (c[2] if len(c) > 2 else '', inl(c[0]),
            ('<span>%s</span>' % inl(c[1])) if len(c) > 1 and c[1] else '') for c in row))
    return wrap(title, h + '</table></div>', note)

# ---------- ladder ----------
def ladder(rungs, title='', note='', rev=False):
    h = '<div class="ld">'
    n = len(rungs)
    for i, r in enumerate(rungs):
        h += '<div class="ld-r ld-%d" style="margin-right:%d%%"><div class="ld-x">%s</div><div class="ld-l"><b>%s</b>%s</div></div>' % (
            i % 5, (n - 1 - i) * 7 if not rev else i * 7, inl(r[0]), inl(r[1]),
            ('<span>%s</span>' % inl(r[2])) if len(r) > 2 and r[2] else '')
    return wrap(title, h + '</div>', note)

# ---------- table ----------
def table(head, rows, title='', note='', wide=False):
    h = '<div class="gw"><table class="ct%s"><tr>%s</tr>' % (' wide' if wide else '', ''.join('<th>%s</th>' % inl(c) for c in head))
    for r in rows:
        cls = ''
        if r and str(r[0]).startswith('!'):
            cls = ' class="key"'; r = [str(r[0])[1:]] + list(r[1:])
        h += '<tr%s>%s</tr>' % (cls, ''.join('<td>%s</td>' % inl(c) for c in r))
    return wrap(title, h + '</table></div>', note)

# ---------- A vs B ----------
def split(a, b, rows, same=None, title='', note=''):
    h = '<div class="pv"><div class="pv-h"><span class="ca">A · %s</span> <i>vs</i> <span class="cb">B · %s</span></div>' % (inl(a), inl(b))
    if same:
        h += '<div class="pv-same"><div class="pv-lbl">= Same in both</div><div class="pv-chips">%s</div></div>' % ''.join(
            '<span>%s</span>' % inl(x) for x in same)
    h += '<div class="pv-lbl pv-diff">≠ How they differ <span class="pv-hint">★ = the row that decides</span></div><table class="pv-t">'
    h += '<tr><th></th><th class="ca">%s</th><th class="cb">%s</th></tr>' % (inl(a), inl(b))
    for f, x, y in rows:
        key = str(f).startswith('!'); f = str(f).lstrip('!')
        h += '<tr class="%s"><th>%s%s</th><td>%s</td><td>%s</td></tr>' % ('key' if key else '', '★ ' if key else '', inl(f), inl(x), inl(y))
    return wrap(title, h + '</table></div>', note)

# ---------- numbered steps ----------
def steps(items, title='', note='', horiz=False):
    h = '<div class="st %s">' % ('st-h' if horiz else '')
    for i, it in enumerate(items):
        if i and horiz: h += '<div class="st-ar">→</div>'
        h += '<div class="st-s"><div class="st-n">%d</div><div class="st-h2">%s</div>%s</div>' % (
            i + 1, inl(it[0]), ('<div class="st-w">%s</div>' % inl(it[1])) if len(it) > 1 and it[1] else '')
    return wrap(title, h + '</div>', note)

# ---------- chips ----------
def chips(items, title='', note='', cols=3):
    h = '<div class="cp" style="--c:%d">' % cols
    for it in items:
        h += '<div class="cp-i"><b>%s</b>%s</div>' % (inl(it[0]), ('<span>%s</span>' % inl(it[1])) if len(it) > 1 and it[1] else '')
    return wrap(title, h + '</div>', note)

def raw(svg, title='', note=''):
    return wrap(title, '<div class="svgw">%s</div>' % svg, note)
