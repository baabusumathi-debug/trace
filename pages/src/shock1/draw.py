# -*- coding: utf-8 -*-
"""Hand-drawn SVG diagrams: heart, circulation, echo views, traces, curves."""
NAVY='#1c3461'; RED='#b3261e'; AMB='#a35a00'; GRN='#2e6b3a'; TEAL='#00707d'; GREY='#5a6472'
BLU='#c9dcf5'; PINK='#f3cdc9'; MUT='#8a97b4'

def _t(x,y,s,sz=11,anc='middle',w=600,fill='#1d1d1f'):
    return '<text x="%s" y="%s" font-size="%s" text-anchor="%s" font-weight="%s" fill="%s">%s</text>'%(x,y,sz,anc,w,fill,s)

# ---------------------------------------------------------------- heart
def heart(marks=None, caption=''):
    """Clean schematic of the four chambers, valves and the direction of flow.
    Right heart on the viewer's left. marks: list of (x, y, label, colour, anchor)."""
    m = marks or []
    s = ['<svg viewBox="0 0 500 330" class="dg" role="img">']
    s.append('<defs><marker id="hf" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker></defs>' % GREY)
    def ch(x, y, w, h, lab, col, fill, sw=2.5, sz=17):
        return ('<rect x="%s" y="%s" width="%s" height="%s" rx="20" fill="%s" stroke="%s" stroke-width="%s"/>' % (x, y, w, h, fill, col, sw)
                + _t(x + w / 2, y + h / 2 + 6, lab, sz, 'middle', 800, col))
    s.append(ch(118, 66, 112, 68, 'RA', NAVY, BLU))
    s.append(ch(118, 176, 112, 92, 'RV', NAVY, BLU))
    s.append(ch(296, 66, 112, 68, 'LA', RED, PINK))
    s.append(ch(284, 176, 136, 102, 'LV', RED, PINK, 6, 19))
    s.append(_t(352, 258, 'thick wall = the pump', 9.5, 'middle', 600, RED))
    s.append(_t(174, 56, 'RIGHT HEART', 10, 'middle', 800, NAVY))
    s.append(_t(352, 56, 'LEFT HEART', 10, 'middle', 800, RED))
    def valve(x, y, lab):
        return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="4.5" stroke-linecap="round"/>' % (x - 27, y, x + 27, y, GREY)
                + _t(x, y - 15, lab, 9.5, 'middle', 700, GREY)
                + '<path d="M%s %s L%s %s" stroke="%s" stroke-width="2.5" marker-end="url(#hf)"/>' % (x, y + 4, x, y + 18, GREY))
    s.append(valve(174, 155, 'tricuspid valve'))
    s.append(valve(352, 155, 'mitral valve'))
    def vvalve(x, y, lab, anc):
        return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="4.5" stroke-linecap="round"/>' % (x, y - 15, x, y + 15, GREY)
                + _t(x + (9 if anc == 'start' else -9), y + 28, lab, 9.5, anc, 700, GREY))
    def arrow(x1, y, x2, lab, col):
        return ('<path d="M%s %s L%s %s" stroke="%s" stroke-width="3.5" marker-end="url(#hf)"/>' % (x1, y, x2, y, GREY)
                + _t((x1 + x2) / 2, y - 12, lab, 10, 'middle', 700, col))
    s.append(arrow(34, 100, 112, 'from the body', NAVY))
    s.append(arrow(112, 222, 34, 'to the lungs', NAVY))
    s.append(vvalve(106, 222, 'pulmonary valve', 'end'))
    s.append(arrow(478, 100, 414, 'from the lungs', RED))
    s.append(arrow(426, 226, 486, 'to the body', RED))
    s.append(vvalve(430, 226, 'aortic valve', 'start'))
    for i, mk in enumerate(m):
        x, y, lab, col = mk[0], mk[1], mk[2], mk[3]
        s.append('<circle cx="%s" cy="%s" r="13" fill="%s" stroke="#fff" stroke-width="2.5"/>' % (x, y, col))
        s.append(_t(x, y + 5, str(i + 1), 13, 'middle', 800, '#fff'))
    if caption: s.append(_t(250, 318, caption, 10.5, 'middle', 700, GREY))
    out = ''.join(s) + '</svg>'
    if m:
        out += '<ol class="pins">' + ''.join(
            '<li style="--c:%s"><span>%d</span>%s</li>' % (mk[3], i + 1, mk[2]) for i, mk in enumerate(m)) + '</ol>'
    return out

# ---------------------------------------------------------------- circulation loop
def loop(block=None, reads=True, title='Where the catheter reads each of the four numbers'):
    """Circulation loop with the four catheter readings marked."""
    s=['<svg viewBox="0 0 640 318" class="dg" role="img">']
    if title: s.append(_t(320,14,title,12,'middle',800,NAVY))
    # boxes
    def box(x,y,w,h,lab,col,fill):
        return ('<rect x="%s" y="%s" width="%s" height="%s" rx="9" fill="%s" stroke="%s" stroke-width="2"/>'%(x,y,w,h,fill,col)
                + _t(x+w/2,y+h/2+5,lab,13,'middle',800,col))
    s.append(box(40,186,110,60,'Body (veins)',GREY,'#eef1f6'))
    s.append(box(190,186,100,60,'Right heart',NAVY,BLU))
    s.append(box(330,186,110,60,'Lungs',TEAL,'#dff1f3'))
    s.append(box(480,186,110,60,'Left heart',RED,PINK))
    s.append(box(190,56,400,52,'Arteries  —  squeeze (SVR)',AMB,'#fbf0df'))
    # arrows
    def ar(x1,y1,x2,y2,col=GREY,w=3):
        return '<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" marker-end="url(#ah)"/>'%(x1,y1,x2,y2,col,w)
    s.insert(1,'<defs><marker id="ah" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker></defs>'%GREY)
    s.append(ar(152,216,186,216)); s.append(ar(292,216,326,216))
    s.append(ar(442,216,476,216))
    s.append('<path d="M535 184 L535 112" fill="none" stroke="%s" stroke-width="3" marker-end="url(#ah)"/>'%GREY)
    s.append('<path d="M190 82 L95 82 L95 182" fill="none" stroke="%s" stroke-width="3" marker-end="url(#ah)"/>'%GREY)
    if reads:
        def tag(x,y,lab,sub,col):
            return ('<rect x="%s" y="%s" width="118" height="38" rx="7" fill="#fff" stroke="%s" stroke-width="2"/>'%(x,y,col)
                    + _t(x+59,y+16,lab,11,'middle',800,col) + _t(x+59,y+30,sub,9.5,'middle',600,GREY))
        s.append(tag(181,262,'RAP (CVP)','filling, right',NAVY))
        s.append(tag(471,262,'PAWP (wedge)','filling, left',RED))
        s.append(tag(330,134,'CO','the pump',GRN))
        
        
    if block:
        bx = dict(pe=(310,212,'BLOCK: PE'), tamponade=(340,166,'BLOCK: tamponade'),
                  lv=(535,216,'PUMP fails'), volume=(95,216,'FILLING fails'), svr=(390,82,'SQUEEZE fails'))[block]
        x,y,lab = bx
        if block=='tamponade':
            s.append('<ellipse cx="340" cy="216" rx="200" ry="56" fill="none" stroke="%s" stroke-width="4" stroke-dasharray="7 5"/>'%RED)
            s.append(_t(340,162,lab,12,'middle',800,RED))
        else:
            s.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="6"/>'%(x-16,y-22,x+16,y+22,RED))
            s.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="6"/>'%(x+16,y-22,x-16,y+22,RED))
            s.append(_t(x,y-32,lab,12,'middle',800,RED))
    return ''.join(s)+'</svg>'

# ---------------------------------------------------------------- Frank-Starling
def starling(mark=None, note_steep='fluid HELPS here', note_flat='fluid only floods the lungs', title='The Frank–Starling curve: is this heart still on the steep part?'):
    s=['<svg viewBox="0 0 460 296" class="dg" role="img">']
    if title: s.append(_t(230,14,title,11.5,'middle',800,NAVY))
    s.append('<line x1="60" y1="251" x2="430" y2="251" stroke="%s" stroke-width="2"/>'%GREY)
    s.append('<line x1="60" y1="251" x2="60" y2="46" stroke="%s" stroke-width="2"/>'%GREY)
    s.append(_t(245,282,'FILLING  (preload)',11,'middle',800,GREY))
    s.append('<text x="22" y="156" font-size="11" font-weight="700" fill="%s" transform="rotate(-90 22 156)" text-anchor="middle">STROKE VOLUME</text>'%GREY)
    s.append('<path d="M60 246 C130 244 175 111 250 86 C320 66 390 64 428 62" fill="none" stroke="%s" stroke-width="4"/>'%NAVY)
    s.append('<path d="M70 245 C130 242 170 126 196 108" fill="none" stroke="%s" stroke-width="9" opacity=".3"/>'%GRN)
    s.append('<path d="M300 74 C350 66 395 63 424 62" fill="none" stroke="%s" stroke-width="9" opacity=".3"/>'%RED)
    s.append(_t(132,136,'steep',12,'middle',800,GRN))
    s.append(_t(132,152,note_steep,9.5,'middle',600,GRN))
    s.append(_t(366,102,'flat',12,'middle',800,RED))
    s.append(_t(366,118,note_flat,9.5,'middle',600,RED))
    if mark:
        for x,y,lab,col in mark:
            s.append('<circle cx="%s" cy="%s" r="7" fill="%s" stroke="#fff" stroke-width="2"/>'%(x,y,col))
            s.append(_t(x,y-14,lab,10.5,'middle',800,col))
    return ''.join(s)+'</svg>'

# ---------------------------------------------------------------- arterial traces
def traces():
    def w(x0,y0,osc,lab,sub,sys,col):
        p=['<g transform="translate(%s,%s)">'%(x0,y0)]
        p.append('<rect x="0" y="-6" width="178" height="104" rx="8" fill="#fff" stroke="%s" stroke-width="2"/>'%col)
        p.append(_t(89,14,lab,11.5,'middle',800,col))
        d='M10 76 L34 76 L40 30 L48 44 L56 38 L66 74 L80 76'
        if osc=='under': d='M10 76 L34 76 L40 16 L46 56 L52 26 L58 52 L64 34 L70 48 L78 74 L90 76'
        if osc=='over':  d='M10 76 L36 76 C44 62 52 58 62 58 C74 58 80 68 88 76 L96 76'
        p.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.4"/>'%(d,col))
        # flush square
        p.append('<path d="M96 76 L104 76 L104 24 L124 24 L124 76" fill="none" stroke="%s" stroke-width="2" stroke-dasharray="3 3"/>'%GREY)
        if osc=='opt':   p.append('<path d="M124 76 L130 88 L136 70 L142 79 L150 76 L168 76" fill="none" stroke="%s" stroke-width="2.4"/>'%col)
        if osc=='under': p.append('<path d="M124 76 L128 92 L132 60 L136 88 L140 64 L144 86 L148 68 L152 82 L158 76 L168 76" fill="none" stroke="%s" stroke-width="2.4"/>'%col)
        if osc=='over':  p.append('<path d="M124 76 C134 76 140 78 150 76 L168 76" fill="none" stroke="%s" stroke-width="2.4"/>'%col)
        p.append(_t(89,110,sub,9.5,'middle',600,GREY))
        p.append(_t(89,124,sys,9.5,'middle',700,col))
        return ''.join(p)+'</g>'
    s=['<svg viewBox="0 0 580 168" class="dg" role="img">']
    s.append(w(4,16,'opt','Optimal','1–2 oscillations, each ≤ ⅓ of the last','systolic and diastolic true',GRN))
    s.append(w(198,16,'under','Underdamped (ringing)','many oscillations — long, narrow or soft tubing','systolic too HIGH, diastolic too low',RED))
    s.append(w(392,16,'over','Overdamped','no oscillation — bubble, clot or kink','systolic too LOW, diastolic too high',AMB))
    s.append(_t(290,162,'In both failures the MEAN pressure stays close to the truth',10.5,'middle',700,NAVY))
    return ''.join(s)+'</svg>'

# ---------------------------------------------------------------- tubing / natural frequency
def tubing():
    s=['<svg viewBox="0 0 560 190" class="dg" role="img">']
    s.append(_t(140,20,'HIGH natural frequency — trace is honest',11.5,'middle',800,GRN))
    s.append('<rect x="30" y="38" width="220" height="26" rx="13" fill="#dff1f3" stroke="%s" stroke-width="3"/>'%GRN)
    s.append(_t(140,56,'WIDE · SHORT · STIFF',11,'middle',800,GRN))
    s.append(_t(140,84,'rings fast, well above the pulse',10,'middle',600,GREY))
    s.append(_t(420,20,'LOW natural frequency — trace rings',11.5,'middle',800,RED))
    s.append('<rect x="310" y="44" width="230" height="14" rx="7" fill="#f6e3e1" stroke="%s" stroke-width="3"/>'%RED)
    s.append(_t(425,54,'NARROW · LONG · SOFT',9.5,'middle',800,RED))
    s.append(_t(425,84,'falls among the pulse’s harmonics → resonance',10,'middle',600,GREY))
    s.append('<line x1="24" y1="104" x2="536" y2="104" stroke="%s" stroke-width="1"/>'%'#d5dbe8')
    s.append(_t(140,126,'overshoot: none',10.5,'middle',700,GRN))
    s.append('<path d="M60 170 L84 170 L90 136 L98 150 L106 144 L116 168 L130 170 L160 170 L166 136 L174 150 L182 144 L192 168 L206 170" fill="none" stroke="%s" stroke-width="2.4"/>'%GRN)
    s.append(_t(425,126,'overshoot: systolic reads FALSELY HIGH',10.5,'middle',700,RED))
    s.append('<path d="M322 170 L344 170 L350 122 L358 162 L364 130 L372 160 L380 140 L392 168 L406 170 L430 170 L436 122 L444 162 L450 130 L458 160 L466 140 L478 168 L492 170" fill="none" stroke="%s" stroke-width="2.4"/>'%RED)
    s.append('<line x1="316" y1="122" x2="500" y2="122" stroke="%s" stroke-width="1.4" stroke-dasharray="4 4"/>'%RED)
    s.append('<line x1="54" y1="136" x2="212" y2="136" stroke="%s" stroke-width="1.4" stroke-dasharray="4 4"/>'%GRN)
    return ''.join(s)+'</svg>'

# ---------------------------------------------------------------- chest with the three windows
def windows(active=None):
    s = ['<svg viewBox="0 0 440 310" class="dg" role="img">']
    s.append('<path d="M140 40 q80 -16 160 0 l16 136 q-12 64 -96 68 q-84 -4 -96 -68 z" fill="#fdf7f2" stroke="%s" stroke-width="2.5"/>' % GREY)
    for i in range(5):
        s.append('<path d="M146 %s q74 14 148 0" fill="none" stroke="#e8ddd2" stroke-width="7"/>' % (68 + i * 24))
    s.append('<line x1="220" y1="38" x2="220" y2="188" stroke="#e8ddd2" stroke-width="11"/>')
    s.append(_t(220, 30, 'sternum', 9.5, 'middle', 700, GREY))
    s.append('<path d="M206 94 q54 -10 70 52 q10 58 -42 70 q-58 8 -68 -52 q-6 -52 40 -70 z" fill="%s" stroke="%s" stroke-width="2.5"/>' % (PINK, RED))
    s.append(_t(232, 156, 'heart', 11, 'middle', 800, RED))
    pts = [(186, 100, '1  parasternal', 'PLAX', 'end', -22, 4),
           (246, 208, '2  apical', 'A4C', 'start', 22, 4),
           (218, 246, '3  subcostal', 'SUB', 'middle', 0, 32)]
    for x, y, lab, key, anc, dx, dy in pts:
        on = (active == key)
        col = RED if on else GREY
        s.append('<circle cx="%s" cy="%s" r="15" fill="%s" stroke="#fff" stroke-width="3"/>' % (x, y, col))
        s.append(_t(x, y + 5, '◉', 13, 'middle', 800, '#fff'))
        s.append('<text x="%s" y="%s" font-size="11" text-anchor="%s" font-weight="%s" fill="%s">%s</text>' % (
            x + dx, y + dy, anc, 800 if on else 700, col, lab))
    s.append(_t(220, 300, 'ultrasound cannot cross air — these are the three gaps where lung does not cover the heart', 9.5, 'middle', 600, GREY))
    return ''.join(s) + '</svg>'

# ---------------------------------------------------------------- echo slices
def _pins(m):
    if not m: return ''
    return '<ol class="pins">' + ''.join('<li style="--c:%s"><span>%d</span>%s</li>' % (x[3], i+1, x[2]) for i, x in enumerate(m)) + '</ol>'

def _pin(x, y, i, col):
    return ('<circle cx="%s" cy="%s" r="12" fill="%s" stroke="#fff" stroke-width="2.5"/>' % (x, y, col)
            + _t(x, y + 5, str(i), 12.5, 'middle', 800, '#fff'))

def _sector(w=440, h=290, top=16, pad=30):
    return '<path d="M%s %s L%s %s L%s %s z" fill="#111827" stroke="%s" stroke-width="2"/>' % (w/2, top, pad, h-24, w-pad, h-24, GREY)

def plax(fluid=False):
    s = ['<svg viewBox="0 0 440 300" class="dg" role="img">', _sector()]
    s.append(_t(220, 10, 'PARASTERNAL LONG AXIS · marker to the RIGHT SHOULDER', 10, 'middle', 800, NAVY))
    s.append('<path d="M158 78 q74 -10 128 18 q10 26 -22 32 q-70 8 -106 -12 q-16 -20 0 -38 z" fill="#2a3a56" stroke="#8fa6c9" stroke-width="2"/>')
    s.append(_t(212, 104, 'RV', 13, 'middle', 800, '#9fc0e8'))
    s.append('<path d="M126 124 q84 -14 150 8" fill="none" stroke="#c9d4e6" stroke-width="6"/>')
    s.append('<path d="M112 140 q96 -16 154 26 q24 48 -26 70 q-88 20 -124 -26 q-20 -44 -4 -70 z" fill="#1d2b44" stroke="#8fa6c9" stroke-width="2"/>')
    s.append(_t(174, 196, 'LV', 15, 'middle', 800, '#e7b2ad'))
    s.append('<path d="M282 150 q52 -4 56 36 q2 36 -42 38 q-44 -2 -44 -38 q0 -32 30 -36 z" fill="#2a3a56" stroke="#8fa6c9" stroke-width="2"/>')
    s.append(_t(298, 192, 'LA', 13, 'middle', 800, '#e7b2ad'))
    s.append('<path d="M262 60 q56 -4 66 40 q4 26 -24 32" fill="none" stroke="#e7b96a" stroke-width="8"/>')
    s.append(_t(330, 48, 'aortic root', 9.5, 'middle', 800, '#e7b96a'))
    s.append('<path d="M252 112 L300 88" stroke="#e7b96a" stroke-width="5"/>')
    s.append('<circle cx="352" cy="232" r="19" fill="#3a2630" stroke="#e08a84" stroke-width="2.5"/>')
    s.append(_t(352, 236, 'DAo', 10, 'middle', 800, '#e08a84'))
    m = [(252, 112, 'aortic valve — the LVOT is measured just below it', '#a35a00'),
         (244, 146, 'mitral valve', '#5a6472'),
         (198, 124, 'septum', '#5a6472'),
         (352, 232, 'descending aorta, cut across — the landmark', '#b3261e')]
    if fluid:
        s.append('<path d="M300 208 q36 -20 64 -2" fill="none" stroke="#7fd4e8" stroke-width="9"/>')
        s.append('<path d="M352 258 q36 10 58 -2" fill="none" stroke="#d9b3f0" stroke-width="9"/>')
        m += [(318, 200, 'fluid IN FRONT of the DAo = PERICARDIAL', '#00707d'),
              (380, 258, 'fluid BEHIND it = PLEURAL', '#6a3fa0')]
    for i, p in enumerate(m): s.append(_pin(p[0], p[1], i + 1, p[3]))
    return ''.join(s) + '</svg>' + _pins(m)

def a4c(mode='normal'):
    s = ['<svg viewBox="0 0 440 300" class="dg" role="img">', _sector()]
    s.append(_t(220, 10, 'APICAL FOUR-CHAMBER · probe at the APEX, marker to the LEFT', 10, 'middle', 800, NAVY))
    s.append(_t(220, 34, 'apex is NEAREST the probe', 9, 'middle', 600, '#9aa3b5'))
    rvx = 92 if mode == 'rv' else 58
    s.append('<path d="M212 48 L%s 150 q-10 36 26 38 L212 186 z" fill="#2a3a56" stroke="#8fa6c9" stroke-width="2"/>' % (212 - rvx))
    s.append(_t(212 - rvx * 0.55, 136, 'RV', 13, 'middle', 800, '#9fc0e8'))
    lvf = '#3a2a2a' if mode == 'poor' else '#1d2b44'
    lvx = 104 if mode == 'poor' else 86
    s.append('<path d="M228 48 L%s 150 q10 36 -26 38 L228 186 z" fill="%s" stroke="%s" stroke-width="%s"/>' % (228 + lvx, lvf, '#e08a84' if mode == 'poor' else '#8fa6c9', 3 if mode == 'poor' else 2))
    s.append(_t(228 + lvx * 0.55, 136, 'LV', 15, 'middle', 800, '#e7b2ad'))
    s.append('<line x1="150" y1="190" x2="212" y2="190" stroke="#c9d4e6" stroke-width="5"/>')
    s.append('<line x1="228" y1="190" x2="296" y2="190" stroke="#c9d4e6" stroke-width="5"/>')
    s.append('<path d="M158 196 L212 196 L212 248 q-40 2 -54 -24 z" fill="#2a3a56" stroke="#8fa6c9" stroke-width="2"/>')
    s.append(_t(184, 226, 'RA', 12, 'middle', 800, '#9fc0e8'))
    s.append('<path d="M286 196 L228 196 L228 248 q44 2 58 -24 z" fill="#1d2b44" stroke="#8fa6c9" stroke-width="2"/>')
    s.append(_t(258, 226, 'LA', 12, 'middle', 800, '#e7b2ad'))
    m = [(181, 190, 'tricuspid valve', '#5a6472'), (262, 190, 'mitral valve', '#5a6472')]
    if mode == 'tapse':
        s.append('<line x1="150" y1="34" x2="150" y2="268" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="7 5"/>')
        m += [(150, 190, 'M-mode through the LATERAL TRICUSPID RING = TAPSE (≤17 mm abnormal)', '#a35a00')]
    if mode == 'rv':
        m += [(150, 96, 'RV as big as the LV (ratio >1) = right ventricular strain, as in PE', '#b3261e')]
    if mode == 'doppler':
        s.append('<line x1="220" y1="34" x2="220" y2="268" stroke="#7fd4e8" stroke-width="2.5" stroke-dasharray="6 4"/>')
        m += [(220, 214, 'inflow and the TR jet run ALONG the beam here — so Doppler is measured in this view', '#00707d')]
    if mode == 'poor':
        m += [(332, 136, 'dilated, poorly contracting LV: the pump number, seen directly', '#b3261e')]
    for i, p in enumerate(m): s.append(_pin(p[0], p[1], i + 1, p[3]))
    return ''.join(s) + '</svg>' + _pins(m)

def subcostal(eff=False):
    s = ['<svg viewBox="0 0 440 290" class="dg" role="img">']
    s.append('<path d="M70 26 L370 26 L312 256 L128 256 z" fill="#111827" stroke="%s" stroke-width="2"/>' % GREY)
    s.append(_t(220, 16, 'SUBCOSTAL · probe under the XIPHISTERNUM, through the liver', 10, 'middle', 800, NAVY))
    s.append('<path d="M74 30 L366 30 L352 78 L86 78 z" fill="#3b3a2e" stroke="#9a8f6a" stroke-width="2"/>')
    s.append(_t(220, 60, 'LIVER', 11, 'middle', 800, '#d8cc9a'))
    s.append('<path d="M128 108 q70 -16 96 26 q16 42 -26 58 q-64 16 -86 -28 q-10 -36 16 -56 z" fill="#2a3a56" stroke="#8fa6c9" stroke-width="2"/>')
    s.append(_t(170, 152, 'RV', 13, 'middle', 800, '#9fc0e8'))
    s.append('<path d="M240 106 q62 -10 72 30 q8 36 -34 48 q-54 10 -64 -30 q-6 -36 26 -48 z" fill="#1d2b44" stroke="#8fa6c9" stroke-width="2"/>')
    s.append(_t(280, 150, 'LV', 13, 'middle', 800, '#e7b2ad'))
    s.append('<path d="M140 198 q58 -8 66 20 q4 24 -34 28 q-44 2 -48 -22 q-2 -22 16 -26 z" fill="#2a3a56" stroke="#8fa6c9" stroke-width="2"/>')
    s.append(_t(172, 224, 'RA', 12, 'middle', 800, '#9fc0e8'))
    s.append('<path d="M240 200 q52 -6 58 22 q4 22 -32 24 q-40 0 -42 -22 q0 -20 16 -24 z" fill="#1d2b44" stroke="#8fa6c9" stroke-width="2"/>')
    s.append(_t(270, 224, 'LA', 12, 'middle', 800, '#e7b2ad'))
    s.append(_t(220, 278, 'the liver carries sound well, so this window survives inflated lung and works in arrest', 9.5, 'middle', 600, GREY))
    m = [(142, 112, 'the RIGHT heart lies nearest the probe', '#1c3461')]
    if eff:
        s.append('<path d="M112 96 q110 -34 216 16 q16 104 -96 124 q-128 4 -134 -86 q-2 -36 14 -54 z" fill="none" stroke="#7fd4e8" stroke-width="11" opacity=".9"/>')
        m += [(112, 150, 'effusion all round', '#00707d'), (212, 196, 'the right atrium collapses in diastole', '#a35a00')]
    for i, p in enumerate(m): s.append(_pin(p[0], p[1], i + 1, p[3]))
    return ''.join(s) + '</svg>' + _pins(m)

def ivc(state='plethoric'):
    s = ['<svg viewBox="0 0 440 250" class="dg" role="img">']
    s.append('<rect x="20" y="24" width="400" height="188" rx="8" fill="#111827" stroke="%s" stroke-width="2"/>' % GREY)
    s.append(_t(220, 16, 'SUBCOSTAL IVC · marker towards the HEAD', 10, 'middle', 800, NAVY))
    s.append('<path d="M28 36 L412 36 L412 76 L28 76 z" fill="#3b3a2e"/>')
    s.append(_t(220, 60, 'LIVER', 10, 'middle', 800, '#d8cc9a'))
    wide = state != 'collapsing'
    h1 = 32 if wide else 13
    s.append('<path d="M34 %s L268 %s q34 -2 48 -18 L330 108 L330 148 L316 166 q-16 14 -48 12 L34 %s z" fill="#0b1220" stroke="#7fd4e8" stroke-width="2.5"/>' % (128 - h1, 128 - h1, 128 + h1))
    s.append(_t(150, 132, 'IVC', 13, 'middle', 800, '#7fd4e8'))
    s.append('<path d="M330 90 q60 -8 64 38 q2 42 -46 46 q-42 0 -46 -38 q-2 -38 28 -46 z" fill="#2a3a56" stroke="#8fa6c9" stroke-width="2"/>')
    s.append(_t(356, 136, 'RA', 12, 'middle', 800, '#9fc0e8'))
    s.append('<line x1="150" y1="32" x2="150" y2="204" stroke="#ffd166" stroke-width="2.5" stroke-dasharray="7 5"/>')
    if wide:
        s.append(_t(220, 236, 'WIDE (over 2.1 cm) and barely moving  →  right atrial pressure HIGH, about 15', 11, 'middle', 800, NAVY))
    else:
        s.append('<path d="M40 120 L266 120" stroke="#9fd0a6" stroke-width="2.5" stroke-dasharray="5 4"/>')
        s.append(_t(220, 236, 'SMALL (2.1 cm or less), collapsing over 50% on a sniff  →  right atrial pressure LOW, about 3', 11, 'middle', 800, GRN))
    return ''.join(s) + '</svg>'

def psax(mode='normal'):
    s = ['<svg viewBox="0 0 400 270" class="dg" role="img">']
    s.append('<rect x="18" y="22" width="364" height="202" rx="8" fill="#111827" stroke="%s" stroke-width="2"/>' % GREY)
    s.append(_t(200, 14, 'PARASTERNAL SHORT AXIS, papillary muscle level', 10, 'middle', 800, NAVY))
    if mode == 'd':
        s.append('<path d="M150 72 q86 0 86 52 q0 54 -86 54 q-58 0 -58 -54 q0 -52 58 -52 z" fill="#1d2b44" stroke="#e08a84" stroke-width="3.5"/>')
        s.append(_t(170, 130, 'LV', 15, 'middle', 800, '#e7b2ad'))
        s.append('<path d="M88 72 q-42 52 0 104 q36 -52 0 -104 z" fill="#2a3a56" stroke="#8fa6c9" stroke-width="2.5"/>')
        s.append(_t(70, 130, 'RV', 12, 'middle', 800, '#9fc0e8'))
        s.append(_t(200, 246, 'the septum is FLATTENED: the LV is a D, not a circle', 11, 'middle', 800, '#b3261e'))
        s.append(_t(200, 262, 'the right ventricle is overloaded — PE or RV failure', 10, 'middle', 600, GREY))
    else:
        r = 52 if mode == 'hyper' else 60
        s.append('<circle cx="196" cy="124" r="%s" fill="#1d2b44" stroke="#8fa6c9" stroke-width="3"/>' % r)
        if mode == 'hyper':
            s.append('<circle cx="196" cy="124" r="14" fill="#3a2630" stroke="#e08a84" stroke-width="2"/>')
        s.append(_t(196, 124 if mode != 'hyper' else 86, 'LV', 13, 'middle', 800, '#e7b2ad'))
        s.append('<circle cx="172" cy="150" r="9" fill="#6b7f9f"/><circle cx="222" cy="150" r="9" fill="#6b7f9f"/>')
        s.append('<path d="M126 74 q-44 50 0 100" fill="#2a3a56" stroke="#8fa6c9" stroke-width="2.5"/>')
        s.append(_t(104, 126, 'RV', 12, 'middle', 800, '#9fc0e8'))
        if mode == 'hyper':
            s.append(_t(200, 246, 'the walls almost meet in systole — the “kissing” papillary muscles', 11, 'middle', 800, '#a35a00'))
            s.append(_t(200, 262, 'only hypovolaemia if the DIASTOLIC size is small too', 10, 'middle', 600, GREY))
        else:
            s.append(_t(200, 246, 'a round septum is normal; every LV wall is seen at once', 10.5, 'middle', 800, '#1c3461'))
    return ''.join(s) + '</svg>'

# ---------------------------------------------------------------- lung / film
def blines(mode='b'):
    s=['<svg viewBox="0 0 460 230" class="dg" role="img">']
    def pane(x,lab,kind,col):
        p=['<g transform="translate(%s,0)">'%x]
        p.append('<rect x="0" y="26" width="200" height="164" rx="7" fill="#101624" stroke="%s" stroke-width="2"/>'%GREY)
        p.append(_t(100,20,lab,10.5,'middle',800,col))
        p.append('<rect x="34" y="56" width="18" height="22" fill="#4c5366"/><rect x="148" y="56" width="18" height="22" fill="#4c5366"/>')
        p.append(_t(43,50,'rib',8.5,'middle',700,'#9aa3b5'))
        p.append('<line x1="10" y1="84" x2="190" y2="84" stroke="#e8edf5" stroke-width="4"/>')
        p.append(_t(100,100,'pleural line',8.5,'middle',700,'#e8edf5'))
        if kind=='b':
            for bx in (72,100,128):
                p.append('<path d="M%s 86 L%s 186" stroke="#eaf3ff" stroke-width="7" opacity=".85"/>'%(bx,bx))
            p.append(_t(100,206,'≥3 B-lines + sliding present',9.5,'middle',800,col))
        elif kind=='a':
            for ay in (118,152,184):
                p.append('<line x1="18" y1="%s" x2="182" y2="%s" stroke="#9fb3cc" stroke-width="3" opacity=".8"/>'%(ay,ay))
            p.append(_t(100,206,'A-lines: dry lung',9.5,'middle',800,col))
        else:
            for ay in (118,152,184):
                p.append('<line x1="18" y1="%s" x2="182" y2="%s" stroke="#9fb3cc" stroke-width="3" opacity=".8"/>'%(ay,ay))
            p.append(_t(100,206,'NO sliding and NO B-lines',9.5,'middle',800,col))
        return ''.join(p)+'</g>'
    s.append(pane(6,'WET · interstitial oedema','b','#7fd4e8'))
    s.append(pane(248,'PNEUMOTHORAX (the mimic)','p','#e08a84'))
    s.append(_t(230,226,'a pneumothorax abolishes BOTH the sliding and the B-lines',10,'middle',800,NAVY))
    return ''.join(s)+'</svg>'

def kerley():
    s=['<svg viewBox="0 0 420 260" class="dg" role="img">']
    s.append('<rect x="14" y="18" width="392" height="206" rx="8" fill="#0d0f14" stroke="%s" stroke-width="2"/>'%GREY)
    s.append('<path d="M46 40 q66 -14 84 26 q16 92 -16 150 q-54 10 -70 -40 q-14 -78 2 -136 z" fill="#1a1f2b" stroke="#6d7892" stroke-width="2"/>')
    s.append('<path d="M374 40 q-66 -14 -84 26 q-16 92 16 150 q54 10 70 -40 q14 -78 -2 -136 z" fill="#1a1f2b" stroke="#6d7892" stroke-width="2"/>')
    s.append('<path d="M172 60 q38 -16 76 0 q14 64 -4 136 q-34 16 -68 0 q-18 -70 -4 -136 z" fill="#2b3142" stroke="#8c97af" stroke-width="2"/>')
    s.append(_t(210,210,'big heart',10,'middle',800,'#cfd7e6'))
    for i,(y) in enumerate((150,168,186)):
        s.append('<line x1="34" y1="%s" x2="66" y2="%s" stroke="#eaf3ff" stroke-width="3.5"/>'%(y,y))
        s.append('<line x1="354" y1="%s" x2="386" y2="%s" stroke="#eaf3ff" stroke-width="3.5"/>'%(y,y))
    s.append(_t(64,132,'B lines',10,'middle',800,'#eaf3ff'))
    s.append(_t(72,144,'1–2 cm · horizontal · basal',8.5,'middle',700,'#9fb3cc'))
    for (x1,y1,x2,y2) in ((70,72,124,96),(66,96,120,116),(344,72,292,96)):
        s.append('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="#ffd166" stroke-width="3"/>'%(x1,y1,x2,y2))
    s.append(_t(150,70,'A lines',10,'middle',800,'#ffd166'))
    s.append(_t(150,58,'longer · deep · towards the hila',8.5,'middle',700,'#ffd166'))
    s.append(_t(210,244,'Kerley lines are THICKENED, OEDEMATOUS INTERLOBULAR SEPTA — not lymphatics',10,'middle',800,NAVY))
    return ''.join(s)+'</svg>'

# ---------------------------------------------------------------- passive leg raise
def plr():
    s=['<svg viewBox="0 0 560 250" class="dg" role="img">']
    def man(x,y,ang,lab,sub,col):
        p=['<g transform="translate(%s,%s)">'%(x,y)]
        if ang==45:
            p.append('<path d="M10 100 L96 40" stroke="%s" stroke-width="12" stroke-linecap="round"/>'%col)
            p.append('<circle cx="104" cy="34" r="11" fill="%s"/>'%col)
            p.append('<path d="M10 100 L96 100" stroke="%s" stroke-width="12" stroke-linecap="round"/>'%col)
            p.append(_t(100,120,'45°',10,'middle',800,col))
        else:
            p.append('<path d="M10 72 L96 72" stroke="%s" stroke-width="12" stroke-linecap="round"/>'%col)
            p.append('<circle cx="104" cy="72" r="11" fill="%s"/>'%col)
            p.append('<path d="M10 72 L-70 30" stroke="%s" stroke-width="12" stroke-linecap="round"/>'%col)
            p.append(_t(-40,16,'legs up 45°',10,'middle',800,col))
        p.append(_t(50,126,lab,11,'middle',800,col))
        p.append(_t(50,140,sub,9.5,'middle',600,GREY))
        return ''.join(p)+'</g>'
    s.append(man(36,20,45,'START','semi-recumbent, trunk at 45°',NAVY))
    s.append('<path d="M186 86 L262 86" stroke="%s" stroke-width="4" marker-end="url(#pa)"/>'%GRN)
    s.append('<defs><marker id="pa" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker></defs>'%GRN)
    s.append(_t(224,74,'tilt the BED, don’t touch him',9.5,'middle',800,GRN))
    s.append(man(396,20,0,'TILTED','trunk flat, legs raised',GRN))
    s.append('<rect x="28" y="198" width="504" height="46" rx="9" fill="#eef5ef" stroke="%s" stroke-width="2"/>'%GRN)
    s.append(_t(280,216,'about 300 mL of his own blood, in 60–90 s, fully reversible',10.5,'middle',800,GRN))
    s.append(_t(280,234,'measure CARDIAC OUTPUT or STROKE VOLUME — never the blood pressure',10,'middle',800,RED))
    s.append(_t(280,186,'POSITIVE = a rise of 10% or more   (end-tidal CO₂: 5% or more)',12,'middle',800,NAVY))
    return ''.join(s)+'</svg>'
