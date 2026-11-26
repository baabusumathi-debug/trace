# -*- coding: utf-8 -*-
"""Drawings for the trauma page. Read ../DIAGRAMS.md first: body drawings face the viewer, so
the patient's RIGHT is on the viewer's LEFT. Words for numbered pins go in the list under the
drawing, never on a line."""
import os, importlib.util
_spec = importlib.util.spec_from_file_location('draw1', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shock1', 'draw.py'))
_d1 = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_d1)
_t, NAVY, RED, GRN, AMB, TEAL, GREY = _d1._t, _d1.NAVY, _d1.RED, _d1.GRN, _d1.AMB, _d1.TEAL, _d1.GREY

def _pin(x, y, n, col):
    return ('<circle cx="%s" cy="%s" r="11" fill="%s" stroke="#fff" stroke-width="2.5"/>' % (x, y, col)
            + _t(x, y + 4, str(n), 11.5, 'middle', 800, '#fff'))
def pins(items):
    return '<ol class="pins">' + ''.join('<li style="--c:%s"><span>%d</span><div>%s</div></li>' % (c, i + 1, t) for i, (t, c) in enumerate(items)) + '</ol>'

def fast():
    """Torso facing the viewer: liver on the viewer's LEFT (patient's right), spleen on the viewer's RIGHT."""
    s = ['<svg viewBox="0 0 420 380" class="dg" role="img">']
    s.append(_t(70, 22, "patient's RIGHT", 9.5, 'middle', 700, GREY))
    s.append(_t(350, 22, "patient's LEFT", 9.5, 'middle', 700, GREY))
    # trunk
    s.append('<path d="M120 36 Q210 22 300 36 L322 120 Q330 220 314 300 Q300 350 210 360 Q120 350 106 300 Q90 220 98 120 Z" fill="#f6f1ea" stroke="%s" stroke-width="2"/>' % GREY)
    # sternum and costal margins
    s.append('<rect x="202" y="44" width="16" height="104" rx="6" fill="#e7ddd0" stroke="%s" stroke-width="1.5"/>' % GREY)
    s.append('<path d="M206 150 Q160 186 112 204 M214 150 Q260 186 308 204" fill="none" stroke="%s" stroke-width="1.5" stroke-dasharray="5 4"/>' % GREY)
    # lungs (faint), heart slightly to the patient's left
    s.append('<path d="M126 50 Q164 44 196 56 L196 150 Q160 168 118 176 Q108 110 126 50 Z" fill="#eaf1fb" stroke="#b9c9e0" stroke-width="1.5"/>')
    s.append('<path d="M294 50 Q256 44 224 56 L224 150 Q260 168 302 176 Q312 110 294 50 Z" fill="#eaf1fb" stroke="#b9c9e0" stroke-width="1.5"/>')
    s.append('<path d="M196 118 Q236 104 254 132 Q256 160 224 170 Q200 172 192 150 Z" fill="#f6dcdc" stroke="%s" stroke-width="1.5"/>' % RED)
    # liver (patient's right = viewer's left), spleen (viewer's right), both kidneys, bladder
    s.append('<path d="M112 186 Q170 176 214 190 Q200 232 150 240 Q118 236 108 214 Z" fill="#ecd9c6" stroke="#b08a63" stroke-width="1.5"/>')
    s.append(_t(150, 214, 'liver', 9, 'middle', 700, '#7a5a3a'))
    s.append('<path d="M286 190 Q312 196 312 224 Q304 246 282 240 Q272 214 286 190 Z" fill="#e8d3e3" stroke="#a37c99" stroke-width="1.5"/>')
    s.append(_t(332, 214, '← spleen', 9, 'start', 700, '#7d5873'))
    s.append('<ellipse cx="150" cy="262" rx="14" ry="22" fill="#efe2d6" stroke="#b08a63" stroke-width="1.2"/>')
    s.append('<ellipse cx="270" cy="262" rx="14" ry="22" fill="#efe2d6" stroke="#b08a63" stroke-width="1.2"/>')
    s.append('<ellipse cx="210" cy="330" rx="30" ry="18" fill="#e3edf5" stroke="#8fa6c9" stroke-width="1.5"/>')
    s.append(_t(210, 334, 'bladder', 8.5, 'middle', 700, NAVY))
    # windows: 1 pericardial (subxiphoid), 2 RUQ, 3 LUQ, 4 pelvis, 5-6 anterior chests (eFAST)
    for x, y, n, c in ((210, 176, 1, RED), (118, 246, 2, AMB), (302, 228, 3, AMB), (210, 302, 4, NAVY), (160, 92, 5, TEAL), (260, 92, 6, TEAL)):
        s.append(_pin(x, y, n, c))
    return ''.join(s) + '</svg>' + pins([
        ('<b>Pericardial</b>, under the xiphisternum: blood around the heart', RED),
        ('<b>Right upper quadrant</b>: Morison’s pouch, between liver and right kidney', AMB),
        ('<b>Left upper quadrant</b>: splenorenal, higher and more posterior than the right', AMB),
        ('<b>Pelvis</b>: behind the bladder (pouch of Douglas or rectovesical)', NAVY),
        ('<b>Right chest</b>, anterior: lung sliding — eFAST only', TEAL),
        ('<b>Left chest</b>, anterior: lung sliding — eFAST only', TEAL)])

def reboa():
    """The aorta from the arch to the bifurcation, branches on the left, zones on the right."""
    s = ['<svg viewBox="0 0 460 400" class="dg" role="img">']
    X = 200
    # arch and aorta
    s.append('<path d="M120 70 Q120 30 170 30 Q%d 30 %d 70 L%d 330" fill="none" stroke="%s" stroke-width="26" stroke-linejoin="round" opacity=".22"/>' % (X, X, X, RED))
    # bifurcation into the common iliacs
    s.append('<path d="M%d 326 L%d 384 M%d 326 L%d 384" stroke="%s" stroke-width="16" opacity=".22" stroke-linecap="round"/>' % (X, X - 46, X, X + 46, RED))
    # branches
    s.append('<line x1="184" y1="34" x2="184" y2="8" stroke="%s" stroke-width="7" opacity=".3"/>' % RED)
    s.append(_t(176, 14, 'left subclavian', 9, 'end', 700, GREY))
    for y, lab in ((150, 'coeliac trunk'), (176, 'superior mesenteric'), (214, 'renal arteries (lowest)')):
        s.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="6" opacity=".3"/>' % (X - 14, y, X - 52, y, RED))
        s.append(_t(X - 58, y + 4, lab, 9, 'end', 700, GREY))
    s.append('<line x1="%d" y1="214" x2="%d" y2="214" stroke="%s" stroke-width="6" opacity=".3"/>' % (X + 14, X + 40, RED))
    s.append(_t(X - 58, 362, 'common iliacs', 9, 'end', 700, GREY))
    # zone brackets on the right
    def zone(y1, y2, n, lab, sub, col):
        return ('<path d="M%d %d L%d %d L%d %d L%d %d" fill="none" stroke="%s" stroke-width="2.5"/>' % (X + 56, y1, X + 66, y1, X + 66, y2, X + 56, y2, col)
                + _t(X + 78, (y1 + y2) / 2 - 8, 'Zone %s · %s' % (n, lab), 11, 'start', 800, col)
                + ''.join(_t(X + 78, (y1 + y2) / 2 + 6 + 11 * i, part, 9, 'start', 600, GREY) for i, part in enumerate(sub.split(': '))))
    s.append(zone(48, 146, 1, 'descending thoracic', 'left subclavian → coeliac: for ABDOMINAL bleeding', NAVY))
    s.append(zone(152, 216, 2, 'visceral', 'coeliac → lowest renal: not used', GREY))
    s.append(zone(222, 324, 3, 'infrarenal', 'lowest renal → bifurcation: for PELVIC bleeding', GRN))
    s.append(_t(X, 398, 'balloon passed up from the femoral artery', 9, 'middle', 700, GREY))
    return ''.join(s) + '</svg>'
