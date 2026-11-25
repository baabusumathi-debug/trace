# -*- coding: utf-8 -*-
"""Hand-drawn SVGs for Shock II. Shared pieces (_t, the palette, the Starling curve) come from
shock1/draw.py so the two pages look and behave the same. Read ../DIAGRAMS.md before changing one."""
import os, importlib.util
_spec = importlib.util.spec_from_file_location('draw1', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shock1', 'draw.py'))
draw1 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(draw1)
_t, NAVY, RED, AMB, GRN, TEAL, GREY, BLU, PINK, starling = (draw1._t, draw1.NAVY, draw1.RED, draw1.AMB, draw1.GRN, draw1.TEAL,
                                                       draw1.GREY, draw1.BLU, draw1.PINK, draw1.starling)

# Arrowhead ids must be unique on the page: the study page hides every screen but one, and an
# arrow pointing at an id defined inside a hidden screen draws no head. Each drawing gets its own set.
_N = [0]
def _arrowdefs(*cols):
    _N[0] += 1
    return '<defs>' + ''.join(
        '<marker id="%s" markerWidth="9" markerHeight="9" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 z" fill="%s"/></marker>' % (_mid(c), c)
        for c in cols) + '</defs>'
def _mid(col): return 's2m%d%s' % (_N[0], col.strip('#'))
def _ar(x1, y1, x2, y2, col, w=2.5, dash=''):
    return '<path d="M%s %s L%s %s" stroke="%s" stroke-width="%s" fill="none"%s marker-end="url(#%s)"/>' % (
        x1, y1, x2, y2, col, w, (' stroke-dasharray="%s"' % dash) if dash else '', _mid(col))
def _box(x, y, w, h, lab, col, fill='#fff', sz=11, sub='', subsz=9):
    s = '<rect x="%s" y="%s" width="%s" height="%s" rx="8" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y, w, h, fill, col)
    if sub:
        s += _t(x + w / 2, y + h / 2 - 1, lab, sz, 'middle', 800, col) + _t(x + w / 2, y + h / 2 + 12, sub, subsz, 'middle', 600, GREY)
    else:
        s += _t(x + w / 2, y + h / 2 + 4, lab, sz, 'middle', 800, col)
    return s

# ---------------------------------------------------------------- the heart cell and the vessel cell
def _pin(x, y, n, col):
    return ('<circle cx="%s" cy="%s" r="11" fill="%s" stroke="#fff" stroke-width="2.5"/>' % (x, y, col)
            + _t(x, y + 4, str(n), 11.5, 'middle', 800, '#fff'))
def pins(items):
    """the words for numbered pins, under the drawing (no word ever sits on a line)"""
    return '<ol class="pins">' + ''.join('<li style="--c:%s"><span>%d</span>%s</li>' % (c, i + 1, t) for i, (t, c) in enumerate(items)) + '</ol>'

def cell(mode='path'):
    """mode: 'path' — the β1 and α1 pathways; 'drugs' — where each inotrope acts; 'blocked' — on a β-blocker."""
    s = ['<svg viewBox="0 0 560 338" class="dg" role="img">', _arrowdefs(NAVY, RED, GRN, TEAL)]
    s.append('<rect x="8" y="30" width="356" height="300" rx="18" fill="#f4f7fc" stroke="%s" stroke-width="2"/>' % NAVY)
    s.append(_t(186, 22, 'HEART MUSCLE CELL · β1', 11, 'middle', 800, NAVY))
    s.append('<rect x="376" y="30" width="176" height="300" rx="18" fill="#fbf3f2" stroke="%s" stroke-width="2"/>' % RED)
    s.append(_t(464, 22, 'VESSEL WALL · α1', 11, 'middle', 800, RED))
    chain = [(48, 'β1 receptor', ''), (98, 'Gs', 'stimulatory G protein'), (146, 'adenylate cyclase', ''),
             (194, 'cAMP', 'broken down by PDE-3'), (242, 'protein kinase A', 'phosphorylates 4 targets')]
    for i, (y, lab, sub) in enumerate(chain):
        s.append(_box(126, y, 120, 36, lab, NAVY, '#fff', 11, sub, 8))
        if i: s.append(_ar(186, y - 12, 186, y - 2, NAVY, 2))
    s.append(_t(66, 112, 'CONTRACT HARDER', 9, 'middle', 800, GRN))
    s.append(_t(66, 124, 'inotropy', 9, 'middle', 600, GREY))
    s.append(_box(18, 134, 96, 32, 'L-type Ca²⁺', GRN, '#eef7ef', 10, 'channel', 8))
    s.append(_box(18, 176, 96, 32, 'ryanodine', GRN, '#eef7ef', 10, 'receptor (SR)', 8))
    s.append(_t(306, 112, 'RELAX FASTER', 9, 'middle', 800, TEAL))
    s.append(_t(306, 124, 'lusitropy', 9, 'middle', 600, GREY))
    s.append(_box(258, 134, 96, 32, 'phospholamban', TEAL, '#e9f5f6', 10, 'frees SERCA2a', 8))
    s.append(_box(258, 176, 96, 32, 'troponin I', TEAL, '#e9f5f6', 10, 'lets go of Ca²⁺', 8))
    # PKA to its targets: elbows round the outside, clear of every word
    s.append('<path d="M126 260 L66 260 L66 214" fill="none" stroke="%s" stroke-width="1.8" marker-end="url(#%s)"/>' % (GRN, _mid(GRN)))
    s.append('<path d="M246 260 L306 260 L306 214" fill="none" stroke="%s" stroke-width="1.8" marker-end="url(#%s)"/>' % (TEAL, _mid(TEAL)))
    # the myofilament, where calcium meets troponin C
    s.append(_box(18, 272, 96, 30, 'troponin C', GREY, '#fff', 10, 'the filament', 8))
    s.append(_t(186, 320, 'all four PKA targets handle calcium — none is myosin', 9.5, 'middle', 700, NAVY))
    vchain = [(48, 'α1 receptor', ''), (98, 'Gq', ''), (146, 'phospholipase C', ''), (194, 'IP3 + DAG', 'Ca²⁺ out of store · PKC'), (242, 'CONSTRICTS', '')]
    for i, (y, lab, sub) in enumerate(vchain):
        s.append(_box(404, y, 120, 36, lab, RED, '#fff', 11, sub, 8))
        if i: s.append(_ar(464, y - 12, 464, y - 2, RED, 2))
    s.append(_t(464, 320, 'not cAMP: that is the β arm', 9.5, 'middle', 700, RED))
    if mode == 'blocked':
        s.append('<rect x="118" y="41" width="136" height="50" rx="10" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="6 4"/>' % RED)
        s.append(_t(108, 64, '✕ β-blocker', 9.5, 'end', 800, RED))
        s.append(_t(108, 76, 'sits here', 9, 'end', 600, RED))
    if mode in ('drugs', 'blocked'):
        if mode == 'drugs': s.append(_pin(126, 48, 1, NAVY))
        s.append(_pin(246, 212, 2, AMB))
        s.append(_pin(114, 287, 3, GRN))
    return ''.join(s) + '</svg>'

CELL_DRUGS = [('<b>Dobutamine, epinephrine</b>: AT the β1 receptor, so cAMP rises', NAVY),
              ('<b>Milrinone</b>: blocks PDE-3, so cAMP is not broken down — no receptor needed', AMB),
              ('<b>Levosimendan</b>: sensitises troponin C at the filament — no extra calcium enters', GRN)]
CELL_BLOCKED = [('<b>Dobutamine, epinephrine</b> start at the blocked receptor: blunted', NAVY),
                ('<b>Milrinone</b> works below the receptor (PDE-3): still works', AMB),
                ('<b>Levosimendan</b> works at the filament (troponin C): still works — the key', GRN)]

# ---------------------------------------------------------------- transmural pressure
def transmural():
    s = ['<svg viewBox="0 0 520 250" class="dg" role="img">', _arrowdefs(NAVY, RED, GRN)]
    def panel(x0, lab, pl, col):
        p = ['<g transform="translate(%s,0)">' % x0]
        p.append(_t(120, 20, lab, 11, 'middle', 800, col))
        p.append('<rect x="14" y="32" width="212" height="170" rx="22" fill="#f3f6fb" stroke="%s" stroke-width="2"/>' % GREY)
        p.append(_t(24, 50, 'chest', 9, 'start', 700, GREY))
        p.append('<path d="M120 62 q58 4 62 58 q-2 56 -62 64 q-58 -8 -62 -64 q4 -54 62 -58 z" fill="%s" stroke="%s" stroke-width="2.5"/>' % (PINK, RED))
        p.append(_t(120, 106, 'LV', 13, 'middle', 800, RED))
        p.append(_t(120, 124, 'inside 100', 10, 'middle', 700, RED))
        p.append(_t(120, 140, '(aortic pressure)', 8.5, 'middle', 600, GREY))
        p.append(_t(120, 196, 'around the heart  %s' % pl, 10, 'middle', 800, NAVY))
        tm = 100 - int(pl.replace('+', '').replace('−', '-'))
        p.append('<rect x="34" y="210" width="172" height="34" rx="8" fill="#fff" stroke="%s" stroke-width="2"/>' % col)
        p.append(_t(120, 225, 'the wall must make', 9, 'middle', 700, GREY))
        p.append(_t(120, 239, '100 − (%s) = %d' % (pl, tm), 11, 'middle', 800, col))
        return ''.join(p) + '</g>'
    s.append(panel(10, 'BREATHING ON ITS OWN', '−5', RED))
    s.append(panel(270, 'POSITIVE PRESSURE', '+10', GRN))
    s.append(_ar(246, 120, 276, 120, NAVY, 3))
    return ''.join(s) + '</svg>'

# ---------------------------------------------------------------- bar charts for the trials and the culprit vessel
def bars(rows, title='', unit='%', maxv=100, w=520, labw=150, note_col=GREY):
    """rows: (label, value, colour, side-text). Horizontal bars, value written at the end of each bar."""
    h = 30 + 34 * len(rows)
    s = ['<svg viewBox="0 0 %s %s" class="dg" role="img">' % (w, h)]
    if title: s.append(_t(w / 2, 16, title, 11, 'middle', 800, NAVY))
    span = w - labw - 70
    for i, (lab, v, col, side) in enumerate(rows):
        y = 30 + 34 * i
        s.append(_t(labw - 8, y + 16, lab, 10.5, 'end', 700, '#1d1d1f'))
        bw = span * v / maxv
        s.append('<rect x="%s" y="%s" width="%.1f" height="22" rx="4" fill="%s"/>' % (labw, y + 2, bw, col))
        s.append(_t(labw + bw + 6, y + 17, ('%s%s' % (v, unit)) + (('  ' + side) if side else ''), 10.5, 'start', 800, col))
    return ''.join(s) + '</svg>'

# ---------------------------------------------------------------- PV loops for the three machines
def pvloops():
    s = ['<svg viewBox="0 0 560 250" class="dg" role="img">']
    def panel(x0, lab, sub, loop, col, ea_steep=False):
        p = ['<g transform="translate(%s,0)">' % x0]
        p.append(_t(90, 18, lab, 11, 'middle', 800, col))
        p.append(_t(90, 31, sub, 8.5, 'middle', 600, GREY))
        p.append('<line x1="20" y1="214" x2="172" y2="214" stroke="%s" stroke-width="1.5"/>' % GREY)
        p.append('<line x1="20" y1="214" x2="20" y2="44" stroke="%s" stroke-width="1.5"/>' % GREY)
        p.append(_t(96, 230, 'volume →', 8.5, 'middle', 700, GREY))
        p.append('<text x="12" y="130" font-size="8.5" font-weight="700" fill="%s" transform="rotate(-90 12 130)" text-anchor="middle">pressure →</text>' % GREY)
        # baseline failing-heart loop (dashed): EDV 140, ESV 100 in px space
        base = 'M100 196 L148 192 L148 104 Q126 90 104 108 L100 196 Z'
        p.append('<path d="%s" fill="none" stroke="#8a94a6" stroke-width="2" stroke-dasharray="5 4"/>' % base)
        p.append('<path d="%s" fill="%s" fill-opacity=".12" stroke="%s" stroke-width="3"/>' % (loop, col, col))
        return ''.join(p) + '</g>'
    # IABP: slightly lower, slightly wider (lower ejection pressure, larger stroke volume)
    s.append(panel(0, 'BALLOON PUMP', 'slightly lower and wider', 'M94 196 L148 192 L148 112 Q124 100 98 116 L94 196 Z', NAVY))
    # Impella / TandemHeart: smaller, shifted left (unloaded)
    s.append(panel(186, 'IMPELLA · TANDEMHEART', 'smaller, shifted LEFT', 'M64 202 L104 200 L104 136 Q86 128 68 140 L64 202 Z', GRN))
    # peripheral VA ECMO: shifted right and up, narrower
    s.append(panel(372, 'PERIPHERAL VA ECMO', 'shifted RIGHT and UP, narrower', 'M138 192 L168 186 L168 76 Q156 62 140 80 L138 192 Z', RED))
    s.append(_t(280, 246, 'dashed grey = the failing heart before the machine · solid = with it', 9.5, 'middle', 700, GREY))
    return ''.join(s) + '</svg>'

# ---------------------------------------------------------------- the balloon pump: where it lies and what it does to the trace
def iabp():
    s = ['<svg viewBox="0 0 580 300" class="dg" role="img">']
    # where it lies: ascending aorta (left), arch with three branches, descending aorta (right)
    s.append(_t(120, 16, 'WHERE IT LIES', 11, 'middle', 800, NAVY))
    s.append('<path d="M58 262 L58 120 Q58 64 112 64 Q166 64 166 120 L166 276" fill="none" stroke="%s" stroke-width="22" stroke-linecap="round" opacity=".25"/>' % RED)
    for x in (92, 112, 132):
        s.append('<line x1="%s" y1="56" x2="%s" y2="32" stroke="%s" stroke-width="7" opacity=".25"/>' % (x, x, RED))
    s.append(_t(140, 34, '← left subclavian', 8.5, 'start', 700, GREY))
    s.append(_t(140, 45, '(the 3rd branch)', 8.5, 'start', 600, GREY))
    s.append('<line x1="178" y1="228" x2="202" y2="228" stroke="%s" stroke-width="7" opacity=".25"/>' % RED)
    s.append(_t(206, 232, 'renal arteries', 8.5, 'start', 700, GREY))
    s.append(_t(44, 284, 'from the heart', 8.5, 'start', 700, GREY))
    s.append('<rect x="158" y="104" width="16" height="104" rx="8" fill="#cfe0f7" stroke="%s" stroke-width="2"/>' % NAVY)
    s.append('<line x1="166" y1="208" x2="166" y2="296" stroke="%s" stroke-width="2"/>' % NAVY)
    s.append(_t(188, 112, 'tip ~2 cm below', 8.5, 'start', 700, NAVY))
    s.append(_t(188, 123, 'the left subclavian', 8.5, 'start', 700, NAVY))
    s.append(_t(188, 156, '30–50 mL, helium', 8.5, 'start', 800, NAVY))
    s.append(_t(188, 196, 'lower end above', 8.5, 'start', 700, NAVY))
    s.append(_t(188, 207, 'the renals', 8.5, 'start', 700, NAVY))
    s.append(_t(176, 292, '7–8 Fr femoral sheath', 8.5, 'start', 700, GREY))
    # the trace, 1:2 so an unassisted beat sits beside an assisted one
    X = 318
    s.append(_t(X + 128, 16, 'WHAT IT DOES TO THE PRESSURE', 11, 'middle', 800, NAVY))
    s.append('<line x1="%s" y1="258" x2="%s" y2="258" stroke="%s" stroke-width="1.2"/>' % (X, X + 256, GREY))
    pts = ('M{0} 214 L{1} 214 L{2} 120 Q{3} 110 {4} 126 L{5} 150 '      # own systole, then the notch
           'L{6} 92 Q{7} 82 {8} 102 '                                  # inflation at the notch: augmented diastolic peak
           'L{9} 232 '                                                 # deflation: the dip below the unassisted end-diastole
           'L{10} 136 Q{11} 128 {12} 142 L{13} 156 Q{14} 182 {15} 214')  # assisted systole (lower), notch, run-off
    xs = [X, X + 12, X + 26, X + 33, X + 42, X + 54, X + 70, X + 78, X + 88, X + 126, X + 142, X + 149, X + 158, X + 168, X + 200, X + 236]
    s.append('<path d="%s" fill="none" stroke="%s" stroke-width="2.8"/>' % (pts.format(*xs), NAVY))
    s.append('<line x1="%s" y1="214" x2="%s" y2="214" stroke="%s" stroke-width="1.2" stroke-dasharray="4 4"/>' % (X, X + 250, GREY))
    s.append(_t(X + 250, 228, 'unassisted end-diastole', 8, 'end', 600, GREY))
    for (x, y, n, c) in ((X + 26, 100, 1, GREY), (X + 54, 170, 2, GREY), (X + 78, 66, 3, NAVY), (X + 126, 250, 4, GRN), (X + 149, 110, 5, GRN)):
        s.append(_pin(x, y, n, c))
    s.append(_t(X + 128, 282, 'time →', 9, 'middle', 700, GREY))
    return ''.join(s) + '</svg>'

IABP_PINS = [("the patient's own systole, unassisted", GREY),
             ('the dicrotic notch: the aortic valve closes — the balloon inflates HERE', GREY),
             ('diastolic augmentation: higher than systole → coronary flow ↑ (supply)', NAVY),
             ('deflation just before systole: the assisted end-diastolic dip, below the unassisted one', GRN),
             ('the assisted systole is LOWER: the ventricle ejects against less → afterload ↓ (demand)', GRN)]

# ---------------------------------------------------------------- where each machine takes blood and returns it
def devmap(kind):
    """kind: impella | tandem | ecmo. Front-on schematic: right heart on the viewer's left, as in Shock I.
    Words for the cannulas go in the numbered list under the drawing (DEV_PINS)."""
    s = ['<svg viewBox="0 0 520 330" class="dg" role="img">', _arrowdefs(NAVY, RED, GRN, AMB)]
    s.append(_box(70, 70, 96, 58, 'RA', NAVY, BLU, 14))
    s.append(_box(70, 150, 96, 80, 'RV', NAVY, BLU, 14))
    s.append(_box(196, 70, 70, 58, 'LA', RED, PINK, 14))
    s.append(_box(196, 150, 112, 92, 'LV', RED, PINK, 15))
    s.append('<line x1="181" y1="76" x2="181" y2="236" stroke="%s" stroke-width="3" stroke-dasharray="4 3"/>' % GREY)
    s.append(_t(181, 256, 'septum', 8.5, 'middle', 700, GREY))
    # aorta: root rising from the LV, the arch, the descending aorta down to the femoral artery
    s.append('<path d="M284 150 L284 58 Q284 30 314 30 Q400 30 400 58 L400 314" fill="none" stroke="%s" stroke-width="16" stroke-linejoin="round" opacity=".22"/>' % RED)
    s.append('<line x1="272" y1="140" x2="296" y2="140" stroke="%s" stroke-width="3.5"/>' % GREY)
    s.append(_t(414, 30, 'arch', 8.5, 'start', 700, GREY))
    s.append(_t(414, 210, 'descending', 8.5, 'start', 700, GREY))
    s.append(_t(414, 221, 'aorta', 8.5, 'start', 700, GREY))
    s.append(_t(388, 314, 'femoral artery', 8.5, 'end', 700, GREY))
    s.append(_t(58, 314, 'femoral vein', 8.5, 'start', 700, GREY))
    s.append('<line x1="118" y1="128" x2="118" y2="146" stroke="%s" stroke-width="2"/>' % GREY)
    if kind == 'impella':
        s.append('<path d="M296 226 L284 160 L284 112" fill="none" stroke="%s" stroke-width="6" stroke-linecap="round"/>' % GRN)
        s.append(_ar(284, 118, 284, 98, GRN, 3))
        s.append(_pin(296, 226, 1, GRN)); s.append(_pin(310, 140, 2, GREY)); s.append(_pin(260, 98, 3, GRN))
    elif kind == 'tandem':
        s.append('<path d="M40 314 L40 118 L214 118" fill="none" stroke="%s" stroke-width="5" stroke-linejoin="round"/>' % AMB)
        s.append('<circle cx="214" cy="118" r="5" fill="%s"/>' % AMB)
        s.append('<rect x="430" y="246" width="74" height="30" rx="8" fill="#fff4e0" stroke="%s" stroke-width="2"/>' % AMB)
        s.append(_t(467, 265, 'pump', 10, 'middle', 800, AMB))
        s.append('<path d="M40 314 L40 324 L467 324 L467 276" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="5 4"/>' % AMB)
        s.append(_ar(430, 262, 410, 262, AMB, 3))
        s.append(_pin(40, 200, 1, AMB)); s.append(_pin(181, 140, 2, AMB)); s.append(_pin(467, 232, 3, AMB))
    elif kind == 'ecmo':
        s.append('<path d="M40 314 L40 100 L96 100" fill="none" stroke="%s" stroke-width="5" stroke-dasharray="8 4"/>' % NAVY)
        s.append('<circle cx="96" cy="100" r="5" fill="%s"/>' % NAVY)
        s.append('<rect x="430" y="240" width="84" height="38" rx="8" fill="#fde8e6" stroke="%s" stroke-width="2"/>' % RED)
        s.append(_t(472, 256, 'pump +', 9, 'middle', 800, RED))
        s.append(_t(472, 269, 'oxygenator', 9, 'middle', 800, RED))
        s.append('<path d="M40 314 L40 324 L472 324 L472 278" fill="none" stroke="%s" stroke-width="3" stroke-dasharray="8 4"/>' % NAVY)
        s.append(_ar(430, 262, 410, 262, RED, 3))
        s.append(_ar(400, 196, 400, 120, RED, 3.5))
        s.append(_pin(40, 200, 1, NAVY)); s.append(_pin(472, 226, 2, RED)); s.append(_pin(376, 160, 3, RED))
    return ''.join(s) + '</svg>'

DEV_PINS = {
    'impella': [('<b>inlet</b> in the LV cavity: it takes blood FROM the left ventricle', GRN),
                ('it lies ACROSS the aortic valve — so a mechanical valve or tight stenosis bars it', GREY),
                ('<b>outlet</b> in the ascending aorta: blood goes forwards, as the heart sends it → the LV empties (unloads)', GRN)],
    'tandem':  [('a long cannula up the <b>femoral vein</b> into the RA', AMB),
                ('<b>through the atrial septum</b> (transseptal puncture): it drains the LEFT ATRIUM', AMB),
                ('a pump <b>beside the leg</b> returns it to the <b>femoral artery</b> — already oxygenated, so no oxygenator', AMB)],
    'ecmo':    [('venous cannula: <b>femoral vein → right atrium</b> (dashed = before the oxygenator)', NAVY),
                ('<b>pump + oxygenator</b>: the only machine that does gas exchange', RED),
                ('returned to the femoral artery, it runs <b>BACKWARDS up the aorta</b>, against the LV — afterload ↑', RED)],
}

# ---------------------------------------------------------------- Harlequin: two streams meet in the aorta
def harlequin():
    s = ['<svg viewBox="0 0 520 312" class="dg" role="img">', _arrowdefs(NAVY, RED, GREY)]
    # aorta: root, arch with three branches, descending to the legs
    s.append('<path d="M150 200 L150 96 Q150 52 200 52 Q250 52 250 96 L250 290" fill="none" stroke="#c9ced8" stroke-width="26" stroke-linejoin="round"/>')
    s.append(_box(96, 200, 108, 50, 'LV', RED, PINK, 13, 'recovering', 8.5))
    s.append(_t(150, 274, 'failing lungs: the blood it ejects', 8.5, 'middle', 700, GREY))
    s.append(_t(150, 285, 'is NOT oxygenated', 8.5, 'middle', 800, NAVY))
    # three branches, the first one the right arm
    for x, lab, l2 in ((170, 'brachiocephalic', '→ RIGHT ARM, right carotid'), (200, 'left carotid', ''), (228, 'left subclavian', '→ left arm')):
        s.append('<line x1="%s" y1="44" x2="%s" y2="14" stroke="#c9ced8" stroke-width="9"/>' % (x, x))
    s.append(_t(166, 10, '1st branch: RIGHT arm', 9, 'end', 800, NAVY))
    # heart's own blood (dashed navy) going up and round the first branches
    s.append('<path d="M150 196 L150 96 Q150 64 186 58" fill="none" stroke="%s" stroke-width="5" stroke-dasharray="7 5"/>' % NAVY)
    s.append('<line x1="170" y1="44" x2="170" y2="18" stroke="%s" stroke-width="4" stroke-dasharray="5 4"/>' % NAVY)
    # ECMO blood (solid red) coming up from the groin
    s.append('<path d="M250 290 L250 110" fill="none" stroke="%s" stroke-width="5"/>' % RED)
    s.append(_ar(250, 160, 250, 118, RED, 3))
    # mixing zone
    s.append('<rect x="226" y="72" width="48" height="30" rx="6" fill="#fff" stroke="%s" stroke-width="2" stroke-dasharray="3 3"/>' % GREY)
    s.append(_t(284, 84, '← the two streams meet here', 9, 'start', 800, GREY))
    s.append(_t(284, 96, 'the stronger the heart, the further down', 8.5, 'start', 600, GREY))
    # legends with symbols, not colour alone
    s.append('<line x1="300" y1="150" x2="330" y2="150" stroke="%s" stroke-width="4" stroke-dasharray="7 5"/>' % NAVY)
    s.append(_t(338, 154, "heart's own output (dark)", 9.5, 'start', 700, NAVY))
    s.append('<line x1="300" y1="172" x2="330" y2="172" stroke="%s" stroke-width="4"/>' % RED)
    s.append(_t(338, 176, 'ECMO blood from the groin (bright)', 9.5, 'start', 700, RED))
    s.append('<rect x="296" y="200" width="214" height="62" rx="9" fill="#f6f8fc" stroke="%s" stroke-width="1.5"/>' % NAVY)
    s.append(_t(304, 218, 'RIGHT hand SpO₂ 84%', 10.5, 'start', 800, NAVY))
    s.append(_t(304, 234, 'left foot SpO₂ 99%', 10.5, 'start', 800, RED))
    s.append(_t(304, 252, 'fix: return cannula in the jugular = VAV', 9.5, 'start', 800, GRN))
    s.append(_t(262, 290, 'from the femoral', 8.5, 'start', 700, RED))
    s.append(_t(262, 300, 'ECMO cannula', 8.5, 'start', 700, RED))
    return ''.join(s) + '</svg>'
