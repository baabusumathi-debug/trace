# -*- coding: utf-8 -*-
"""ECG I drawings. Every trace is computed from one beat model (no hand-typed wiggles), so
an interval that is labelled is the interval that is drawn."""
import math
NAVY='#1c3461'; RED='#b3261e'; AMB='#a35a00'; GRN='#2e6b3a'; TEAL='#00707d'; GREY='#5a6472'
MUT='#8a97b4'; INK='#1d1d1f'; GRID1='#f1d9d6'; GRID5='#e2a9a3'

def _t(x, y, s, sz=11, anc='middle', w=600, fill=INK):
    return '<text x="%s" y="%s" font-size="%s" text-anchor="%s" font-weight="%s" fill="%s">%s</text>' % (x, y, sz, anc, w, fill, s)

_N = [0]
def _arrowdef(col=GREY):
    _N[0] += 1; i = 'ea%d' % _N[0]
    return i, ('<defs><marker id="%s" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto">'
               '<path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker></defs>' % (i, col))

# ---------------------------------------------------------------- the beat model
def _g(t, c, a, w):
    return a * math.exp(-((t - c) / w) ** 2)

def beat_mv(t, pr=0.16, qrs=1.0, p=True, v=True, st=0.0, tamp=0.3):
    """Voltage (mV) at t seconds after the P wave starts. pr: PR interval (P onset to QRS onset).
    qrs: width factor (1 = narrow). p/v: draw the P wave / the ventricular complex."""
    y = 0.0
    if p: y += _g(t, 0.05, 0.2, 0.022)
    if v:
        o = pr
        k = qrs
        y += _g(t, o + 0.012 * k, -0.08, 0.008 * k) + _g(t, o + 0.040 * k, 1.05, 0.011 * k) + _g(t, o + 0.068 * k, -0.25, 0.010 * k)
        if st: y += st * (1 / (1 + math.exp(-(t - (o + 0.085 * k)) / 0.006))) * (1 / (1 + math.exp((t - (o + 0.30)) / 0.03)))
        y += _g(t, o + 0.27 + 0.03 * (k - 1), tamp, 0.045)
    return y

def strip(beats, secs, x0, y0, pxs=150.0, mvpx=40.0, col=INK, sw=2.0, grid=True, h=None):
    """beats: list of dict(t=start time, pr, qrs, p, v ...). Returns (svg, info) where info gives
    the x of each P onset and QRS onset, so labels are placed from the model."""
    s = []
    H = h or int(2.2 * mvpx)
    if grid:
        W = secs * pxs
        sm = pxs * 0.04
        n = int(W / sm + 0.5)
        for i in range(n + 1):
            x = x0 + i * sm
            s.append('<line x1="%.1f" y1="%s" x2="%.1f" y2="%s" stroke="%s" stroke-width="%s"/>' % (x, y0 - H * 0.62, x, y0 + H * 0.38, GRID5 if i % 5 == 0 else GRID1, 1 if i % 5 == 0 else 0.6))
        m = int(H / sm + 0.5)
        for j in range(m + 1):
            yy = y0 - H * 0.62 + j * sm
            if yy > y0 + H * 0.38 + 0.1: break
            s.append('<line x1="%s" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"/>' % (x0, yy, x0 + W, yy, GRID1, 0.6))
    pts = []
    N = int(secs * 400)
    for i in range(N + 1):
        t = secs * i / N
        v = 0.0
        for b in beats:
            tt = t - b['t']
            if -0.05 < tt < 0.75:
                v += beat_mv(tt, **{k: b[k] for k in b if k != 't'})
        pts.append('%.1f,%.1f' % (x0 + t * pxs, y0 - v * mvpx))
    s.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>' % (' '.join(pts), col, sw))
    info = [dict(p=x0 + b['t'] * pxs, q=(x0 + (b['t'] + b.get('pr', 0.16)) * pxs) if b.get('v', True) else None) for b in beats]
    return ''.join(s), info

# ---------------------------------------------------------------- the relay road
def relay(mode='plain'):
    """The conduction system as one road, top to bottom, with each level's artery on the left and
    its back-up rate on the right. mode='vagus' shades where the vagus has a grip."""
    aid, adef = _arrowdef(NAVY)
    s = ['<svg viewBox="0 0 680 480" class="dg" role="img">', adef]
    def box(x, y, w, h, t, sub='', col=NAVY, fill='#eef3fb', sw=2, sz=13):
        r = '<rect x="%s" y="%s" width="%s" height="%s" rx="9" fill="%s" stroke="%s" stroke-width="%s"/>' % (x, y, w, h, fill, col, sw)
        if sub:
            r += _t(x + w / 2, y + h / 2 - 2, t, sz, 'middle', 800, col) + _t(x + w / 2, y + h / 2 + 12, sub, 9.5, 'middle', 600, GREY)
        else:
            r += _t(x + w / 2, y + h / 2 + 5, t, sz, 'middle', 800, col)
        return r
    def arr(x1, y1, x2, y2, col=NAVY, w=2.2):
        return '<path d="M%s %s L%s %s" stroke="%s" stroke-width="%s" fill="none" marker-end="url(#%s)"/>' % (x1, y1, x2, y2, col, w, aid)
    if mode == 'vagus':
        s.append('<rect x="196" y="28" width="288" height="190" rx="12" fill="#e9f2ec" stroke="%s" stroke-width="1.5" stroke-dasharray="5 4"/>' % GRN)
        s.append('<rect x="196" y="224" width="288" height="234" rx="12" fill="#f7f4ee" stroke="%s" stroke-width="1.5" stroke-dasharray="2 4"/>' % GREY)
    # column heads
    s.append(_t(92, 18, 'ARTERY THAT FEEDS IT', 10, 'middle', 800, GREY))
    s.append(_t(340, 18, 'ONE BEAT, TOP TO BOTTOM', 10, 'middle', 800, NAVY))
    s.append(_t(590, 18, 'BACK-UP RATE', 10, 'middle', 800, GREY))
    # centre: the road
    s.append(box(255, 36, 170, 36, 'SA node', 'high RA, where the SVC enters'))
    s.append(arr(340, 72, 340, 92))
    s.append(box(255, 94, 170, 36, 'Atria', 'a ripple; Bachmann bundle → LA'))
    s.append(arr(340, 130, 340, 158))
    # fibrous ring with its one door
    s.append('<rect x="200" y="172" width="92" height="12" fill="#cfd5df"/><rect x="388" y="172" width="92" height="12" fill="#cfd5df"/>')
    s.append(_t(246, 200, 'fibrous ring', 9.5, 'middle', 700, GREY))
    s.append(_t(246, 211, 'conducts nothing', 9.5, 'middle', 600, GREY))
    s.append('<rect x="294" y="160" width="92" height="38" rx="9" fill="#fff3e0" stroke="%s" stroke-width="3"/>' % AMB)
    s.append(_t(340, 177, 'AV node', 13, 'middle', 800, AMB))
    s.append(_t(340, 191, 'the ONE door', 9.5, 'middle', 700, AMB))
    s.append(_t(434, 200, 'SLOW: 0.05 m/s', 9.5, 'middle', 800, AMB))
    s.append(_t(434, 211, 'holds ~0.1 s', 9.5, 'middle', 600, AMB))
    s.append(arr(340, 198, 340, 228))
    s.append(box(285, 230, 110, 30, 'His bundle', sz=12))
    # three cables
    s.append('<path d="M340 260 L340 268 M340 268 L262 296 M340 268 L412 280" stroke="%s" stroke-width="2.4" fill="none"/>' % NAVY)
    s.append('<path d="M412 280 L376 296 M412 280 L474 296" stroke="%s" stroke-width="2.4" fill="none"/>' % NAVY)
    s.append(_t(428, 274, 'left bundle', 9.5, 'start', 700, NAVY))
    s.append(box(214, 298, 96, 38, 'right', 'bundle', sz=11.5))
    s.append(box(330, 298, 92, 38, 'left anterior', 'fascicle (thin)', sz=11))
    s.append(box(428, 298, 92, 38, 'left posterior', 'fascicle (broad)', sz=11))
    for x in (262, 376, 474):
        s.append(arr(x, 336, x, 356))
    s.append(box(214, 358, 306, 36, 'Purkinje net', 'under the endocardium · FASTEST, 2–4 m/s'))
    s.append(arr(367, 394, 367, 414))
    s.append(box(214, 416, 306, 36, 'Ventricular muscle', 'endocardium → epicardium (inside out)'))
    s.append(_t(367, 472, 'the septum fires first, from its LEFT side to its right', 9.5, 'middle', 600, GREY))
    # left: arteries
    def lab2(x, y, a, b, col=INK, colb=GREY, w=800):
        return _t(x, y, a, 11.5, 'middle', w, col) + (_t(x, y + 14, b, 9.5, 'middle', 600, colb) if b else '')
    s.append(lab2(92, 52, 'RCA 60% · LCx 40%', 'the SA node artery'))
    s.append('<line x1="176" y1="54" x2="250" y2="54" stroke="%s" stroke-width="1" stroke-dasharray="3 3"/>' % MUT)
    s.append(lab2(92, 176, 'RCA 90%', 'the AV node artery · NOT the LAD', RED, GREY))
    s.append('<line x1="176" y1="179" x2="196" y2="179" stroke="%s" stroke-width="1" stroke-dasharray="3 3"/>' % MUT)
    s.append(lab2(92, 312, 'LAD', 'the cables run in the septum'))
    s.append('<line x1="176" y1="316" x2="209" y2="316" stroke="%s" stroke-width="1" stroke-dasharray="3 3"/>' % MUT)
    s.append(_t(92, 370, 'inferior MI → the node', 9.5, 'middle', 700, GREY))
    s.append(_t(92, 384, 'anterior MI → the cables', 9.5, 'middle', 700, GREY))
    # right: back-up rates
    def rate(y, n, who):
        return (_t(590, y, n, 17, 'middle', 800, NAVY) + _t(590, y + 15, who, 9.5, 'middle', 600, GREY))
    s.append(rate(54, '60–100', 'SA node'))
    s.append(arr(590, 76, 590, 162, GREY, 1.6))
    s.append(_t(600, 122, '−20', 10, 'start', 800, GREY))
    s.append(rate(180, '40–60', 'AV junction'))
    s.append(arr(590, 202, 590, 404, GREY, 1.6))
    s.append(_t(600, 306, '−20', 10, 'start', 800, GREY))
    s.append(rate(430, '20–40', 'ventricle'))
    s.append(_t(590, 466, 'the fastest one wins', 9.5, 'middle', 700, GREY))
    if mode == 'vagus':
        s.append(_t(340, 222, '', 1))
    s.append('</svg>')
    return ''.join(s)

def vagus_map():
    """The road again, with the vagus's grip shaded: dense above the door, sparse below it."""
    sv = relay('vagus')
    add = (_t(206, 152, 'VAGUS:', 10, 'start', 800, GRN) + _t(206, 165, 'dense', 10, 'start', 800, GRN) +
           _t(207, 240, 'vagus: sparse', 10, 'start', 800, GREY))
    return sv.replace('</svg>', add + '</svg>')

# ---------------------------------------------------------------- the two cells
def _ap_node(t):
    """SA-node-like potential over one cycle of 0.8 s, starting at max diastolic -60."""
    c = 0.8; t = t % c
    if t < 0.42: return -60 + (20 * (t / 0.42) ** 1.4)        # phase 4: drifts up to -40
    if t < 0.52: return -40 + 50 * ((t - 0.42) / 0.10) ** 1.2   # phase 0: slow upstroke (Ca)
    if t < 0.80:
        u = (t - 0.52) / 0.28
        return 10 - 70 * (1 - (1 - u) ** 2.2)                   # phase 3: back to -60
    return -60

def _ap_muscle(t):
    """Ventricular potential: flat at -90, sudden upstroke, notch, plateau, repolarisation."""
    t = t % 0.8
    if t < 0.10: return -90
    if t < 0.104: return -90 + 115 * ((t - 0.10) / 0.004)      # phase 0
    if t < 0.13: return 25 - 17 * ((t - 0.104) / 0.026)         # phase 1
    if t < 0.33: return 8 - 10 * ((t - 0.13) / 0.20)            # phase 2: plateau
    if t < 0.45:
        u = (t - 0.33) / 0.12
        return -2 - 88 * (u ** 1.3)                             # phase 3
    return -90

def two_cells():
    s = ['<svg viewBox="0 0 640 300" class="dg" role="img">']
    def panel(x0, f, title, sub, col, notes):
        W, H = 270, 170; y0 = 52
        r = ['<rect x="%s" y="20" width="%s" height="262" rx="12" fill="#fff" stroke="%s" stroke-width="2"/>' % (x0, W + 30, col)]
        r.append(_t(x0 + (W + 30) / 2, 40, title, 13, 'middle', 800, col))
        def Y(mv): return y0 + (25 - mv) / 120.0 * H
        def X(t): return x0 + 36 + t / 1.6 * (W - 20)
        for mv, lab in ((0, '0'), (-40, '−40'), (-90, '−90')):
            r.append('<line x1="%s" y1="%.1f" x2="%s" y2="%.1f" stroke="#e3e8f2" stroke-width="1"/>' % (x0 + 34, Y(mv), x0 + W + 18, Y(mv)))
            r.append(_t(x0 + 30, Y(mv) + 3.5, lab, 9, 'end', 600, MUT))
        pts = ' '.join('%.1f,%.1f' % (X(t / 400.0), Y(f(t / 400.0))) for t in range(0, 641))
        r.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.6"/>' % (pts, col))
        for (t, mv, txt, dx, dy, anc) in notes:
            r.append(_t(X(t) + dx, Y(mv) + dy, txt, 9.5, anc, 700, GREY))
        r.append(_t(x0 + (W + 30) / 2, 252, sub[0], 11, 'middle', 800, col))
        r.append(_t(x0 + (W + 30) / 2, 268, sub[1], 9.5, 'middle', 600, GREY))
        return ''.join(r)
    s.append(panel(10, _ap_node, 'CALCIUM cell · SA and AV node',
                   ('slow · tires · fails with a WARNING', 'Ca²⁺ upstroke, no flat resting line'), AMB,
                   [(0.20, -52, 'drifts up', 0, 22, 'middle'), (0.50, -10, 'slow Ca²⁺', -8, 0, 'end')]))
    s.append(panel(330, _ap_muscle, 'SODIUM cell · everything else',
                   ('fast · all or none · fails SUDDENLY', 'Na⁺ upstroke, flat rest at −90'), NAVY,
                   [(0.62, -90, 'flat −90', 0, -8, 'middle'), (0.104, 10, 'Na⁺ jump', 8, 0, 'start')]))
    s.append(_t(320, 296, 'same axes: mV against time, 1.6 s', 9, 'middle', 600, MUT))
    return ''.join(s) + '</svg>'

def fail_pair():
    """How each cell fails, on the strip: the node lengthens then drops; the cable drops without warning."""
    aid, adef = _arrowdef(RED)
    s = ['<svg viewBox="0 0 640 312" class="dg" role="img">', adef]
    def row(y, prs, title, sub, col, label_drop):
        r = [_t(14, y - 66, title, 12, 'start', 800, col), _t(14, y - 51, sub, 9.5, 'start', 600, GREY)]
        beats = []; t = 0.08
        for pr in prs:
            beats.append(dict(t=t, pr=pr if pr else 0.16, v=bool(pr)))
            t += 0.80
        g, info = strip(beats, 4.0, 30, y + 10, pxs=150, mvpx=40)
        r.append(g)
        for b, pr in zip(info, prs):
            if pr:
                r.append(_t((b['p'] + b['q']) / 2, y + 50, '%.2f' % pr, 9.5, 'middle', 800, col))
            else:
                px = b['p'] + 0.05 * 150
                r.append('<rect x="%.1f" y="%s" width="64" height="15" rx="3" fill="#fff"/>' % (px - 32, y - 36))
                r.append(_t(px, y - 24, label_drop, 10, 'middle', 800, RED))
                r.append('<path d="M%.1f %s L%.1f %s" stroke="%s" stroke-width="1.6" marker-end="url(#%s)"/>' % (px, y - 20, px, y - 4, RED, aid))
        r.append(_t(26, y + 50, 'PR', 9, 'end', 700, MUT))
        return ''.join(r)
    s.append(row(96, [0.16, 0.24, 0.30, None, 0.16], 'Calcium cell (the node) fails like a TIRED WORKER',
                 'PR grows beat by beat, then one P is not conducted: Mobitz I (Wenckebach)', AMB, 'P, no QRS'))
    s.append(row(246, [0.16, 0.16, 0.16, None, 0.16], 'Sodium cable (below the node) fails like a LIGHT SWITCH',
                 'PR never changes, then a P is suddenly not conducted: Mobitz II', NAVY, 'P, no QRS'))
    return ''.join(s) + '</svg>'

# ---------------------------------------------------------------- ECG II: the five blocks on one time scale
def blocks():
    """Five rows on one time scale, each computed from the beat model. Atrial rate is the same in every
    row (P every 0.8 s, except 2:1 at 0.6 s), so the only thing that changes is what crosses."""
    aid, adef = _arrowdef(RED)
    rows = [
        ('First degree', 'every P conducts, slowly: PR 0.28 s', NAVY,
         [dict(t=0.1 + 0.8 * i, pr=0.28) for i in range(5)], ['0.28'] * 5, None),
        ('Mobitz I (Wenckebach) · the NODE tires', 'PR lengthens, then one P is not conducted', AMB,
         [dict(t=0.1, pr=0.16), dict(t=0.9, pr=0.26), dict(t=1.7, pr=0.32), dict(t=2.5, v=False), dict(t=3.3, pr=0.16)],
         ['0.16', '0.26', '0.32', None, '0.16'], 3),
        ('Mobitz II · a WIRE breaks below the node', 'PR fixed, then a P drops without warning; QRS often wide', RED,
         [dict(t=0.1, pr=0.16, qrs=1.7), dict(t=0.9, pr=0.16, qrs=1.7), dict(t=1.7, pr=0.16, qrs=1.7), dict(t=2.5, v=False), dict(t=3.3, pr=0.16, qrs=1.7)],
         ['0.16', '0.16', '0.16', None, '0.16'], 3),
        ('2 : 1 block · the PR trend is hidden', 'never two conducted beats in a row: QRS width, story and response give the level', GREY,
         [dict(t=0.1 + 0.6 * i, pr=0.18, v=(i % 2 == 0)) for i in range(7)], ['0.18', None, '0.18', None, '0.18', None, '0.18'], None),
        ('Complete block · two clocks', 'P waves regular, QRS regular and slower, no relation; this escape is wide (ventricular)', NAVY,
         [dict(t=0.1 + 0.72 * i, v=False) for i in range(6)] + [dict(t=0.55 + 1.65 * i - 0.16, pr=0.16, p=False, qrs=1.7) for i in range(3)], None, None),
    ]
    H = 132
    s = ['<svg viewBox="0 0 640 %d" class="dg" role="img">' % (len(rows) * H + 6), adef]
    for k, (name, sub, col, beats, prs, drop) in enumerate(rows):
        y = 56 + k * H
        s.append(_t(14, y - 40, name, 12, 'start', 800, col))
        s.append(_t(14, y - 26, sub, 9.5, 'start', 600, GREY))
        g, info = strip(beats, 4.0, 30, y + 26, pxs=150, mvpx=34)
        s.append(g)
        if prs:
            s.append(_t(26, y + 66, 'PR', 9, 'end', 700, MUT))
            for b, pr in zip(info, prs):
                if pr:
                    s.append(_t((b['p'] + b['q']) / 2, y + 66, pr, 9.5, 'middle', 800, col))
        for b, bt in zip(info, beats):
            if bt.get('v') is False and k in (1, 2, 3):
                px = b['p'] + 0.05 * 150
                if k == 3:
                    s.append(_t(px, y + 66, 'P', 9.5, 'middle', 800, RED))
                else:
                    s.append('<rect x="%.1f" y="%s" width="64" height="15" rx="3" fill="#fff"/>' % (px - 32, y - 18))
                    s.append(_t(px, y - 6, 'P, no QRS', 10, 'middle', 800, RED))
                    s.append('<path d="M%.1f %s L%.1f %s" stroke="%s" stroke-width="1.6" marker-end="url(#%s)"/>' % (px, y - 2, px, y + 16, RED, aid))
        if k == 4:
            qx = [b['q'] + 0.07 * 150 * 1.7 for b, bt in zip(info, beats) if bt.get('v') is not False]
            for x in qx:
                s.append(_t(x, y + 66, 'QRS', 9.5, 'middle', 800, RED))
            for b, bt in zip(info, beats):
                px = b['p'] + 0.05 * 150
                if bt.get('v') is False and all(abs(px - x) > 30 for x in qx):
                    s.append(_t(px, y + 66, 'P', 9.5, 'middle', 800, NAVY))
    s.append('</svg>')
    return ''.join(s)

# ---------------------------------------------------------------- ECG II: the electrolyte grid
def _beat2(t, pr=0.16, pa=0.2, qrs=1.0, st=0.0, ta=0.3, tw=1.0, tdel=0.0, ua=0.0, sdep=0.0, p=True, sine=False):
    """One beat with every handle exposed: P height (pa), QRS width (qrs), ST length (tdel shifts the T),
    T height/width (ta, tw), U wave (ua), ST depression (sdep)."""
    if sine:   # QRS and T merged into one slow oscillation
        if 0.12 < t < 0.72:
            u = (t - 0.12) / 0.6
            return 0.55 * math.sin(2 * math.pi * u) * math.sin(math.pi * u) ** 0.6
        return 0.0
    y = 0.0
    if p: y += _g(t, 0.05, pa, 0.022 * (1 + (0.2 - pa)))
    o = pr; k = qrs
    y += _g(t, o + 0.012 * k, -0.08, 0.008 * k) + _g(t, o + 0.040 * k, 1.0 / max(1, k ** 0.35), 0.011 * k) + _g(t, o + 0.068 * k, -0.25, 0.010 * k)
    tc = o + 0.27 + 0.03 * (k - 1) + tdel
    if sdep: y -= sdep * (1 / (1 + math.exp(-(t - (o + 0.085 * k)) / 0.008))) * (1 / (1 + math.exp((t - tc) / 0.03)))
    y += _g(t, tc, ta, 0.045 * tw)
    if ua: y += _g(t, tc + 0.16, ua, 0.04)
    return y

def electrolytes():
    panels = [
        ('Normal', 'the reference beat', NAVY, dict()),
        ('K⁺ > 6', 'tall, NARROW, tented T · short QT', RED, dict(ta=0.75, tw=0.55, tdel=-0.04)),
        ('K⁺ > 7.5', 'flat P · long PR · wide QRS', RED, dict(pa=0.06, pr=0.26, qrs=1.8, ta=0.6, tw=0.7)),
        ('K⁺ > 9', 'no P · sine wave', RED, dict(sine=True)),
        ('K⁺ ≈ 2.8', 'the T flattens first', AMB, dict(ta=0.1, tw=1.2)),
        ('K⁺ ≈ 2.0', 'U taller than T · ST depression', AMB, dict(ta=0.06, tw=1.2, ua=0.3, sdep=0.1)),
        ('Low Ca²⁺', 'LONG ST, normal T · long QT', TEAL, dict(tdel=0.12)),
        ('High Ca²⁺', 'SHORT ST · short QT', TEAL, dict(tdel=-0.08)),
    ]
    cols, W, H = 4, 156, 150
    s = ['<svg viewBox="0 0 640 %d" class="dg" role="img">' % (2 * H + 8)]
    for i, (name, sub, col, kw) in enumerate(panels):
        cx, cy = 4 + (i % cols) * (W + 4), 4 + (i // cols) * (H + 4)
        s.append('<rect x="%s" y="%s" width="%s" height="%s" rx="10" fill="#fff" stroke="%s" stroke-width="%s"/>' % (cx, cy, W, H, col if i else '#c9d1e0', 2 if i else 1.5))
        s.append(_t(cx + W / 2, cy + 18, name, 12, 'middle', 800, col))
        s.append(_t(cx + W / 2, cy + H - 10, sub, 9, 'middle', 700, GREY))
        x0, y0, pxs, mv = cx + 10, cy + 88, 160.0, 46.0
        sm = pxs * 0.04
        for j in range(int((W - 20) / sm) + 1):
            x = x0 + j * sm
            s.append('<line x1="%.1f" y1="%s" x2="%.1f" y2="%s" stroke="%s" stroke-width="%s"/>' % (x, cy + 30, x, cy + H - 26, GRID5 if j % 5 == 0 else GRID1, 0.8 if j % 5 == 0 else 0.5))
        for j in range(int((H - 56) / sm) + 1):
            yy = cy + 30 + j * sm
            s.append('<line x1="%s" y1="%.1f" x2="%s" y2="%.1f" stroke="%s" stroke-width="0.5"/>' % (x0, yy, x0 + W - 20, yy, GRID1))
        if i:  # the normal beat, faint, under every changed one
            ref = ' '.join('%.1f,%.1f' % (x0 + t / 400.0 * pxs, y0 - _beat2(t / 400.0 + 0.0) * mv) for t in range(0, int((W - 20) / pxs * 400)))
            s.append('<polyline points="%s" fill="none" stroke="#9aa6bd" stroke-width="1.4" stroke-dasharray="3 3"/>' % ref)
        pts = ' '.join('%.1f,%.1f' % (x0 + t / 400.0 * pxs, y0 - _beat2(t / 400.0, **kw) * mv) for t in range(0, int((W - 20) / pxs * 400)))
        s.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.2" stroke-linejoin="round"/>' % (pts, INK))
    s.append('</svg>')
    return ''.join(s)
