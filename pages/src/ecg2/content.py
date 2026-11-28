# -*- coding: utf-8 -*-
"""ECG II (EC2, P12-1201 … 1207): the visual structure for each card. The lesson text comes from
the packet (EC2.json, taken from data/viva/P12.json); the traps come from the writer's draft."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(HERE, '..', 'shock1'))
sys.path.insert(0, HERE)
import vis as V
import draw as D
from vis import inl

TITLE = 'ECG II · blocks, short circuits, drugs and what changes the waves'
SUB = 'NEET cardiology · P12 · EC2 · the faults on the wiring you built in ECG I'

DRAFT = json.load(open(os.path.join(HERE, '..', '..', '..', 'tools', 'viva', 'p12', 'EC2_draft.json')))

def hook(lines, title='Hook: how to keep it'):
    """The memory hooks for a card: short lines, each with its handle in bold."""
    h = '<div class="hk">%s</div>' % ''.join('<div class="hk1">%s</div>' % inl(l) for l in lines)
    return ('<figure class="vis hook"><figcaption>✦ %s</figcaption>%s</figure>' % (inl(title), h))

import re
def is_exam(a):
    """Only a real exam source is shown as 'Asked'; the draft's own notes are not."""
    return bool(re.search(r'\b(GT\d*|NEET|INI|AIIMS|PYQ|DocT|Marrow|Q\d+|20\d\d)\b', a or ''))

def calcium_first(html):
    """In a split, column A is drawn blue and B orange. The drawings give calcium amber and sodium
    navy, so for a calcium-vs-sodium split the two colours are swapped to match."""
    return html.replace('class="ca"', 'class="cX"').replace('class="cb"', 'class="ca"').replace('class="cX"', 'class="cb"')

def traps_for(code):
    """The traps the draft ties to this card: the tempting answer first, the truth on a tap."""
    out = []
    for t in DRAFT['traps']:
        mine = [c for c in t.get('cards', []) if c in PAGE_CARDS]
        if mine and mine[-1] == code:          # each trap once, on the last of its cards on this page
            out.append('<div class="trap"><div class="tnum">!</div><div class="tbody">'
                       '<div class="tstem">%s</div>'
                       '<div class="twrong"><span>tempting</span><s>%s</s></div>'
                       '<button class="rv">Show what is actually true</button><div class="ans" hidden>%s</div>'
                       '</div></div>' % (inl('Asked: ' + t['asked']) if is_exam(t.get('asked', '')) else 'A trap NEET sets', inl(t['trap']), inl(t['truth'])))
    if not out: return ''
    return '<div class="lbl" style="margin:18px 0 2px">The trap on this card</div>' + ''.join(out)


IMG = os.path.join(HERE, '..', '..', '..', 'data', 'viva', 'img', 'P12')
_PN = [0]
def pic(name, title='', note='', fix=()):
    """One of the packet's own pictures (data/viva/img/P12/P12_EC_<name>.svg), inlined. Its ids are made
    unique per use, because an arrowhead defined in a hidden screen does not draw."""
    import re
    svg = open(os.path.join(IMG, 'P12_EC_%s.svg' % name)).read()
    svg = re.sub(r'<\?xml[^>]*\?>', '', svg).strip()
    for a, b in fix:
        assert a in svg, a
        svg = svg.replace(a, b)
    _PN[0] += 1; pre = 'p%d_' % _PN[0]
    ids = re.findall(r'\bid="([^"]+)"', svg)
    for i in ids:
        svg = svg.replace('id="%s"' % i, 'id="%s%s"' % (pre, i)).replace('#%s)' % i, '#%s%s)' % (pre, i)).replace('"#%s"' % i, '"#%s%s"' % (pre, i))
    svg = re.sub(r'<svg\b([^>]*?)\swidth="[^"]*"', r'<svg\1', svg, count=1)
    svg = re.sub(r'<svg\b([^>]*?)\sheight="[^"]*"', r'<svg\1', svg, count=1)
    svg = svg.replace('<svg', '<svg class="dg" role="img"', 1)
    svg = re.sub(r'(\d+\.\d)\d+', r'\1', svg)          # one decimal is plenty on screen
    svg = re.sub(r'\n\s*', '\n', svg)
    return V.raw(svg, title=title, note=note)


ANCHOR = V.steps([('Blocks', 'the level decides'), ('Bundles and pacing', 'one level lower'),
                  ('Short circuits', 'how fast rhythms form'), ('Antiarrhythmics', 'on the same action potential'),
                  ('K⁺, Ca²⁺, Mg²⁺', 'what changes the waves'), ('The QT', 'and torsades'), ('Poisons', 'Na⁺ channels, digoxin, node blockers')],
                 title='ECG II on one line: the wiring of ECG I, under attack',
                 note='Every fault comes back to the two cells: a tired calcium node, or a sodium wire that fails all at once.')

SECTIONS = [
# =========================================================== 1
dict(id='F1', q='P12-1201', n='Section 1',
 title='Blocks as one story: the level of the block decides everything',
 opener=[V.raw(D.blocks(), title='Five strips, two kinds of failure',
               note='Same atrial rate in every row: only what crosses changes. A tired calcium node (first degree, Wenckebach) lengthens the PR before it fails. A broken sodium wire below it (Mobitz II) fails with no warning. 2:1 hides the trend. Complete block is two clocks.')],
 cards=[
  dict(code='V12-061', t='A tired gate or a broken wire', vis=[
    pic('mobitz', title='Mobitz I and Mobitz II'),
    V.branch('A P wave with no QRS', 'What was the PR doing in the beats before it?',
             [('Lengthening, then the drop; the next PR is the shortest', 'THE NODE', 'Mobitz I: calcium cells tiring · usually benign'),
              ('Constant, then a sudden drop', 'BELOW THE NODE', 'Mobitz II: a sodium wire failing · progresses, pace')],
             title='Find the level first'),
    V.table(['Manoeuvre', 'Block in the node', 'Block below the node'],
            [['!Atropine, exercise', '✓ improve it (more vagal release, faster node)', '✕ no help, or WORSE (more P waves arrive at a broken wire)'],
             ['Carotid sinus massage', '✕ worsens it (more vagus on the node)', 'may improve it (fewer P waves arrive)']],
            title='Opposite responses, because the vagus grips only the node'),
    hook(['**Longer, longer, longer, drop: that’s a Wenckebach.** The node tires and rests.',
          '**Mobitz II is the broken wire:** no warning, and what is left below is an unreliable escape.',
          '**Atropine helps the node and hurts the wire. Carotid massage does the opposite.**']),
    'TRAPS']),
  dict(code='CVS08B|ACLS-35', t='Is the sinus node still in charge?', vis=[
    pic('sa_exit', title='SA exit block against sinus arrest'),
    V.split('Sinus bradycardia', 'Junctional rhythm',
            [('Who is in charge', 'the sinus node, firing slowly', 'the AV junction (40–60): the back-up took over'),
             ('!The P wave', 'upright in II, before every QRS, normal PR', 'INVERTED in II, III, aVF: before, hidden in, or after the QRS'),
             ('QRS', 'narrow', 'narrow (it still uses the wiring)'),
             ('Causes', 'sleep, training, drugs; hypoxia, inferior MI, raised ICP, hypothyroid', 'hyperkalaemia, severe sinus bradycardia, SA exit block')],
            title='Who is pacing?',
            note='The junctional P is inverted because the impulse runs backwards up the atria, away from lead II.'),
    V.branch('A pause in sinus rhythm', 'How long is it, against the P–P interval?',
             [('An exact multiple of P–P', 'SA EXIT BLOCK', 'the node fired on time; the impulse failed to leave it'),
              ('No relation to P–P', 'SINUS ARREST', 'the node did not fire')],
             title='The one NEET asks'),
    hook(['**Backwards P = junction:** away from lead II, so inverted.',
          '**Exit block keeps time:** the pause is 2 × or 3 × the P–P exactly.']),
    'TRAPS']),
  dict(code='CVS08B|ACLS-36', t='The official names, and the block that hides its level', vis=[
    pic('av_blocks', title='First degree, 2 : 1, high grade'),
    V.table(['Clue', 'Points to the NODE', 'Points BELOW the node'],
            [['QRS width', 'narrow', 'wide'],
             ['PR of the conducted beats', 'long', 'normal'],
             ['The company it keeps', 'a sleeping athlete, an inferior MI', 'an anterior MI, an elderly patient with a bundle branch block'],
             ['!Atropine or exercise', 'conduction improves', 'no change, or worse']],
            title='2 : 1 block cannot be named from the PR: four clues give the level'),
    V.chips([('First degree', 'PR > 0.20 s, every P conducts: send home (only 39% chose discharge)'),
             ('High-grade', '2 or more CONSECUTIVE P waves not conducted'),
             ('NEET 2025', 'Mobitz I = progressive PR lengthening, then a dropped QRS'),
             ('Marrow, backwards', 'NOT seen in Mobitz I: worsening with atropine')],
            title='Stems already asked', cols=2),
    hook(['**One large square is the PR’s ceiling.** Over it, with every P conducted: first degree, and nothing is blocked.',
          '**2 : 1 hides the trend.** Ask the QRS, the story and the atropine response.']),
    'TRAPS']),
  dict(code='V12-062', t='Complete block: two clocks', vis=[
    pic('chb', title='P waves and QRS complexes on separate clocks'),
    V.branch('P waves and QRS complexes, no relationship', 'Which chamber is faster?',
             [('The atria, and nothing gets through', 'COMPLETE BLOCK', 'more P waves than QRS'),
              ('The ventricles', 'AV DISSOCIATION', 'not block: VT, an accelerated junctional rhythm')],
             title='Dissociation is not always block'),
    V.split('Junctional escape', 'Ventricular escape',
            [('!Level of the block', 'the AV node', 'His–Purkinje'),
             ('QRS · rate', 'narrow · 40–60', 'WIDE · 20–40'),
             ('Atropine', 'some response', 'none'),
             ('Reliability', 'fair', 'POOR: asystole risk')],
            title='The escape gives the level'),
    hook(['**Two clocks, each regular, neither listening.** The PR changes at random because there is no PR.',
          '**Narrow 40–60 sits under the node. Wide 20–40 sits under the wire, and may stop.**']),
    'TRAPS']),
  dict(code='CVS10D|MI-60', t='Heart block after an infarct: the artery gives the level', vis=[
    V.split('Inferior MI', 'Anterior MI',
            [('Artery → tissue', 'RCA (9 in 10) → the calcium NODE', 'LAD septal branches → the sodium WIRING'),
             ('Mechanism', 'partly a vagal reflex + adenosine on the node, not all damage', 'a large part of the septum destroyed: a big infarct already'),
             ('!Warning signs', 'first degree, Wenckebach', 'new RBBB, new bifascicular block, Mobitz II'),
             ('If complete', 'narrow escape 40–60', 'wide escape under 40'),
             ('Atropine', '✓ works', '✕ fails, and may worsen it'),
             ('Course', 'usually recovers within days, especially once the artery is open', 'pace')],
            title='The artery tells you the level'),
    hook(['**Inferior = node = usually kind. Anterior = wire = always worrying.**']),
    'TRAPS']),
  dict(code='HY2|CAR-08', t='Atropine: a bet that the slowness is vagal and nodal', vis=[
    V.branch('Symptomatic bradycardia', 'Will atropine work?',
             [('Sinus bradycardia, block in the node', 'YES', 'it removes vagal tone'),
              ('Block below the node', 'NO', 'the vagus barely touches the wiring'),
              ('A transplanted heart', 'NO', 'denervated: isoprenaline, adrenaline or pacing')],
             title='Atropine blocks a receptor; it stimulates nothing'),
    V.chips([('Atropine', '1 mg IV every 3–5 min, to 3 mg (full vagal block)'),
             ('ERC, and AHA before 2020', 'start 0.5 mg, same 3 mg ceiling: if 1 mg is not offered, 0.5 mg is the answer'),
             ('Too little', 'under 0.5 mg can paradoxically SLOW the heart'),
             ('If atropine fails', 'dopamine (dosed per kg) · adrenaline 2–10 µg/min (NO per kg: only 34% got it) · pacing')],
            title='The numbers', cols=2),
    hook(['**Atropine only lifts the vagal foot off the brake.**',
          '**Adrenaline for bradycardia: 2–10 micrograms a minute, never per kilogram.**']),
    'TRAPS']),
  dict(code='HY2|CAR-09', t='Pacing: pads first, and a child is different', vis=[
    V.branch('Unstable: Mobitz II or complete block with shock', 'What is the INITIAL intervention?',
             [('Transcutaneous pacing', 'YES', 'pads take a minute (only 43% chose it)'),
              ('A transvenous wire first', 'NO', 'better, but slow to place: it comes NEXT'),
              ('Atropine', 'NO', 'works on the node, not below it')],
             title='The grand-test question',
             note='Order: pads now → transvenous wire → a chronotrope as the bridge. Mobitz II with syncope and no reversible cause → permanent pacemaker; the European guideline paces Mobitz II even without symptoms.'),
    V.split('Adult bradycardia', 'Child bradycardia',
            [('!Usual cause', 'a conduction problem', 'the last stage of HYPOXIA'),
             ('First move', 'atropine, pads', 'oxygenate and ventilate'),
             ('If still < 60 with poor perfusion', '', 'treat as an arrest about to happen: compressions + adrenaline 0.01 mg/kg')],
            title='A child’s slow heart is running out of oxygen'),
    hook(['**Pads before wire.**', '**A slow child is a hypoxic child until proved otherwise.**']),
    'TRAPS']),
  dict(code='CVS08B|ACLS-40', t='Four reversible causes, looked for at once', vis=[
    V.table(['Cause', 'What it does', 'The point NEET tests'],
            [['Ischaemia', 'the artery gives the level', 'RCA → node · LAD → wiring'],
             ['!Nodal drugs', 'CCBs, β-blockers, digoxin all act on the calcium node: effects ADD', 'metoprolol + digoxin: digoxin is the partner (through the vagus)'],
             ['Hypoxia', 'late and ominous', 'the usual cause in a child'],
             ['!Electrolytes, above all K⁺', 'partly depolarises EVERY cell: slows SA, atria, node and ventricle together', 'slow, wide, strange rhythm in kidney failure = hyperkalaemia until proved otherwise']],
            title='While you give atropine and reach for the pads'),
    hook(['**Nodal drugs add up at the node:** β-blocker + calcium blocker + digoxin.',
          '**Potassium picks no level: it slows everything at once.**']),
    'TRAPS']),
 ]),
# =========================================================== 2
dict(id='F2', q='P12-1202', n='Section 2',
 title='One level lower: bundle branches, fascicles and the paced heart',
 opener=[V.branch('One wire fails below the His bundle', 'What does the ECG show?',
            [('A bundle branch', 'WIDE QRS', '≥ 0.12 s: no beat dropped; the last part of the QRS points to the blocked side'),
             ('A fascicle', 'AXIS SWINGS', 'the QRS stays narrow: anterior → left axis, posterior → right axis')],
            title='No beat is lost: the shape changes')],
 cards=[
  dict(code='V12-063', t='Bundle branch block: the late wave points to the blocked side', vis=[
    pic('bbb', title='RBBB and LBBB in V1 and V6'),
    V.split('Right bundle branch block', 'Left bundle branch block',
            [('What changes', 'only the END: the RV is reached late, unopposed', 'the BEGINNING too: the septum fires right to left'),
             ('!V1', 'rSR′, an “M”', 'deep QS or rS'),
             ('V6, lead I', 'wide slurred S', 'broad notched R, NO septal q'),
             ('Axis', 'normal (the LV was activated normally)', ''),
             ('ST–T', 'opposite to the late wave', 'opposite to the main QRS: ST UP in V1–V3 is EXPECTED')],
            same=['QRS ≥ 0.12 s (incomplete: same shape, 0.10–0.12 s)'],
            title='Read V1 first',
            note='A right-ventricular paced rhythm looks like LBBB: the RV fires first and the left is reached late, muscle to muscle.'),
    hook(['**WiLLiaM and MaRRoW:** LBBB = W in V1, M in V6; RBBB = M in V1, W in V6.',
          '**ST–T runs away from the QRS in any bundle branch block:** secondary change, not injury.']),
    'TRAPS']),
  dict(code='V12-064', t='Three wires: fascicles, and when to pace', vis=[
    pic('fascicular', title='Left anterior and left posterior fascicular block'),
    V.split('Left anterior fascicle', 'Left posterior fascicle',
            [('Built', 'long, thin, one supply (LAD): blocked OFTEN', 'short, broad, double supply: blocked RARELY'),
             ('!Axis', 'LEFT, −45° or beyond (the commonest cause of LAD)', 'RIGHT, +90° or beyond'),
             ('I, aVL', 'qR', 'rS'),
             ('II, III, aVF', 'rS (small r, deep S)', 'qR'),
             ('Before you call it', '', 'exclude RVH, PE and lateral MI first')],
            same=['QRS < 0.12 s: the axis swings towards the region activated LATE'],
            title='Two fascicles, two axes'),
    V.branch('Left axis deviation', 'How do the inferior leads BEGIN?',
             [('Small r, then deep S', 'LAFB', 'the wave starts downward, then sweeps up'),
              ('With a Q', 'INFERIOR MI', 'dead inferior wall')],
             title='Fascicular block or an old inferior infarct?'),
    V.table(['Finding', 'Means', 'Action'],
            [['RBBB + left axis', 'bifascicular block (RBBB + LAFB commonest)', 'watch'],
             ['Bifascicular block + syncope', 'the third wire may be failing', 'EP study: HV ≥ 70 ms → pacemaker'],
             ['!ALTERNATING bundle branch block', 'all three wires failing', 'permanent pacemaker, even without symptoms (class I)']],
            title='Counting the wires'),
    hook(['**The anterior fascicle is a thin wire with one artery:** it breaks first.',
          '**RBBB + left axis = two wires down.** Alternating BBB = three: pace.']),
    'TRAPS']),
  dict(code='CVS10B|MI-23', t='Seeing an infarct through LBBB: Sgarbossa', vis=[
    pic('sgarbossa', title='Look for what the block cannot do'),
    V.table(['Finding (LBBB or RV pacing)', 'Why it cannot be the block', 'Points'],
            [['!Concordant ST elevation ≥ 1 mm, QRS upright', 'the block pushes that ST DOWN: only injury lifts it', '5'],
             ['Concordant ST depression ≥ 1 mm in V1–V3', 'wrong direction there (QRS down, ST should be up): a posterior MI seen through the block', '3'],
             ['Discordant ST elevation ≥ 5 mm, QRS down', 'the right direction, only too much', '2']],
            title='Sgarbossa: ≥ 3 points = infarction (specificity > 90%)',
            note='Appropriate discordance makes the ordinary 1 mm rule useless in LBBB.'),
    hook(['**5 · 3 · 2: same way up, wrong way in V1–V3, too much the right way.**']),
    'TRAPS']),
  dict(code='CVS10B|MI-24', t='Chest pain with LBBB: three questions, any yes = reperfuse', vis=[
    V.steps([('Unstable, or in acute heart failure?', 'YES → reperfuse now (90% got this)'),
             ('Sgarbossa ≥ 3?', 'YES → reperfuse'),
             ('Smith: ST elevation ≥ ¼ of the S wave?', 'ST/S ≤ −0.25 → reperfuse')],
            title='The LBBB pathway, in order',
            note='Smith scaled Sgarbossa’s fixed 5 mm to the size of the S wave: far more sensitive (about 80–90%). The minus sign only says ST and S point opposite ways. Wrong options: repeat the ECG, trend the troponin.'),
    hook(['**In LBBB, the patient’s state is the first criterion.** Shock with chest pain and LBBB = STEMI equivalent.',
          '**Smith: a quarter of the S.**']),
    'TRAPS']),
 ]),
# =========================================================== 3
dict(id='F3', q='P12-1203', n='Section 3',
 title='Short circuits: how fast rhythms form, and the shape each one draws',
 opener=[V.table(['Mechanism', 'What happens', 'Behaviour', 'Example'],
            [['Automaticity', 'phase 4 steeper (catecholamines, fever, hypoxia, ischaemia, low K⁺), or cells that should not fire do', 'warms up, cools down; a shock does nothing lasting', 'sinus tachycardia, focal atrial tachycardia, AIVR after reperfusion'],
             ['Triggered activity', 'a beat provoked by the one before (afterdepolarisations)', 'needs a long AP (early) or Ca²⁺ overload (late)', 'torsades (long QT), digoxin toxicity'],
             ['!Re-entry', 'a loop: two paths, one-way block, slow conduction', 'starts and stops ABRUPTLY', 'AVNRT, AVRT, flutter, scar VT']],
            title='Three ways a rhythm goes wrong')],
 cards=[
  dict(code='V12-065', t='Re-entry, and the 2 × 2 grid', vis=[
    pic('reentry_grid', title='A loop, and where it lies'),
    V.table(['', 'REGULAR', 'IRREGULAR'],
            [['!NARROW', 'sinus tachycardia, AVNRT, orthodromic AVRT, atrial tachycardia, flutter with fixed block', 'AF, flutter with variable block, MAT'],
             ['!WIDE', 'VT, SVT with bundle branch block, antidromic AVRT', 'pre-excited AF, AF with bundle branch block, polymorphic VT']],
            title='Sort every tachycardia twice: width, then regularity',
            note='A loop through the node (AVNRT, AVRT) is always REGULAR and ends with adenosine. An irregular narrow tachycardia is atrial.'),
    hook(['**A loop needs three things: two roads, a one-way block, and a slow lap** so the first road recovers.',
          '**Where the loop lies draws the ECG:** node (AVNRT) · node + pathway (AVRT) · right atrium (flutter) · scar (VT).']),
    'TRAPS']),
  dict(code='HY2|CAR-02', t='AVNRT and AVRT: where the P wave hides', vis=[
    pic('avnrt_avrt', title='Same rate, different P'),
    V.split('AVNRT', 'Orthodromic AVRT',
            [('The loop', 'inside the node: down slow, up fast', 'down the node, back up an accessory pathway'),
             ('!The P wave', 'fired with the QRS: hidden, or a false S (inferior) / false r′ (V1)', 'a separate P in the ST segment'),
             ('RP interval', '< 70 ms', '> 70 ms')],
            same=['regular, narrow, abrupt · both stop with adenosine or a vagal manoeuvre'],
            title='Two loops through the node'),
    V.branch('SVT in a patient with asthma', 'Instead of adenosine?',
             [('Verapamil or diltiazem', 'YES', 'if the ventricle is normal and there is NO pre-excitation'),
              ('Adenosine', 'NO', 'bronchospasm')],
             title='The exception NEET asks'),
    hook(['**AVNRT turns inside the node, so atria and ventricles fire together:** the P hides.',
          '**AVRT has a longer lap:** the P sits out in the ST.']),
    'TRAPS']),
  dict(code='HY2|CAR-03', t='WPW: a wire with no brake', vis=[
    pic('wpw', title='Short PR, delta wave'),
    V.branch('WPW with a tachycardia', 'What shape is it?',
             [('Narrow and regular (orthodromic AVRT)', 'TREAT THE NODE', 'the node is in the loop: vagal, adenosine, then a nodal blocker'),
              ('Fast, IRREGULAR, wide (pre-excited AF)', 'BLOCK THE PATHWAY', 'unstable: shock · stable: procainamide or ibutilide')],
             title='The ban on nodal blockers is for one rhythm only',
             note='In pre-excited AF: NO adenosine, verapamil, diltiazem, β-blocker, digoxin or IV amiodarone. Slowing the node pushes every impulse down the brakeless pathway, towards VF.'),
    V.chips([('Short PR', '< 0.12 s: a patch of ventricle fires early'), ('Delta wave', 'that early wave creeps muscle to muscle: a slurred start'),
             ('Fusion QRS', 'a little wide, ST–T pointing the other way'), ('Mimics', 'a downward delta looks like an old Q; a left pathway gives a tall R in V1')],
            title='Why WPW looks the way it does', cols=2,
            note='A grand test asked what lies behind a short PR and a delta wave: an accessory AV pathway. Only 39% chose it.'),
    hook(['**The pathway is plain sodium muscle: no delay, no brake.** The node is the only brake left; never take it away in pre-excited AF.']),
    'TRAPS']),
  dict(code='V12-016', t='Vagal manoeuvres and adenosine: two keys to one lock', vis=[
    V.split('Vagal manoeuvre', 'Adenosine',
            [('Receptor on the nodal cell', 'M2 (acetylcholine)', 'A1'),
             ('!What opens', 'the SAME K⁺ channel', 'the SAME K⁺ channel'),
             ('Effect', 'the calcium gate held shut for seconds', 'the same'),
             ('Ventricular rhythms', 'no effect', 'no effect: not a VT treatment')],
            title='Different keys, one lock'),
    V.chips([('Valsalva works on RELEASE', 'blood surges back, pressure overshoots, baroreceptors fire, the vagus slows the node'),
             ('Carotid massage', 'one side, 5–10 s; never with a bruit or a previous stroke'),
             ('Reduce the first adenosine dose', 'central line, heart transplant, dipyridamole, carbamazepine'),
             ('Never adenosine for', 'an irregular or polymorphic wide tachycardia')],
            title='The fine print, asked as statements', cols=2),
    hook(['**Strain, then let go: the slowing comes on release.**',
          '**Adenosine ends a loop that uses the node, and nothing else.**']),
    'TRAPS']),
  dict(code='V12-066', t='Flutter, fibrillation, MAT: the node only decides how much gets through', vis=[
    pic('flutter_af_mat', title='Three atrial rhythms'),
    V.table(['Rhythm', 'The atria', 'What you see', 'Clue'],
            [['!Flutter', 'one big loop round the tricuspid valve (through the cavotricuspid isthmus), ~300/min', 'sawtooth, no flat baseline (down in II, III, aVF; up in V1)', 'regular narrow at almost exactly 150 = flutter 2:1'],
             ['AF', 'chaos, 350–600/min', 'NO P waves, irregularly irregular', 'slow and REGULAR AF on digoxin = complete block'],
             ['MAT', 'several foci', '≥ 3 P-wave shapes, rate > 100, irregular', 'lung disease']],
            title='Atrial rhythms',
            note='Adenosine REVEALS flutter (the sawtooth stands alone during the pause); it never cures it.'),
    hook(['**150, regular, narrow: look for the hidden flutter wave in the QRS or T.**',
          '**Three P shapes = MAT. No P at all = AF.**']),
    'TRAPS']),
  dict(code='CVS08A|ACLS-15', t='Wide and regular: prove the ventricle', vis=[
    pic('vt', title='Independence proves VT'),
    V.chips([('AV dissociation', 'P waves marching at their own slower rate'),
             ('Capture beat', 'a sinus impulse gets through: one narrow normal beat'),
             ('Fusion beat', 'a sinus impulse meets the VT beat halfway: a hybrid QRS')],
            title='Three proofs: two clocks, the lower one faster', cols=3),
    V.branch('A regular wide tachycardia, not proven either way', 'What do you treat it as?',
             [('VT', 'YES', 'after an infarct it is VT until proved otherwise'),
              ('SVT with aberrancy: give verapamil', 'NO', 'NEVER: verapamil into VT can kill')],
             title='If in doubt'),
    hook(['**One scar loop, the same path every lap:** identical wide complexes, regular.',
          '**Capture and fusion beats are the sinus node knocking on the door.**']),
    'TRAPS']),
  dict(code='CVS08A|ACLS-17', t='Ventricular fibrillation: no organised wave, no output', vis=[
    V.chips([('What it is', 'the loop breaks into many wandering wavelets'),
             ('How it starts', 'an early beat in the vulnerable period near the T peak'),
             ('What you see', 'chaotic deflections; NO identifiable P, QRS or T; “rate” 150–500 is only how fast the line wobbles'),
             ('Output', 'none: the rhythm that cannot support perfusion'),
             ('Coarse → fine', 'with time, as the muscle runs out of energy: a poorer outlook'),
             ('Fine VF', 'STILL shocked: NEET’s wrong statement says it is too late')],
            title='The card, line by line', cols=2),
    hook(['**VT is one loop; VF is the loop shattered.**', '**Fine VF is still VF: shock it.**']),
    'TRAPS']),
 ]),
# =========================================================== 4
dict(id='F4', q='P12-1204', n='Section 4',
 title='Antiarrhythmics hung on the same action potential',
 opener=[V.steps([('Class I · sodium', 'phase 0 → the QRS widens'), ('Class II · β-blockers', 'phase 4 and the node → slower, longer PR'),
                  ('Class III · potassium', 'phase 3 → the QT lengthens'), ('Class IV · calcium', 'the node → slower, longer PR')],
                 title='Four classes = the four handles of ECG I', horiz=True,
                 note='“Some Block Potassium Channels”: Sodium, Beta, Potassium, Calcium. Each drug’s danger is its own class showing itself.')],
 cards=[
  dict(code='V12-067', t='Vaughan Williams on the action potential', vis=[
    pic('vaughan_williams', title='Where each class grips'),
    V.table(['Class', 'Drugs', 'Current', 'ECG'],
            [['Ia', 'quinidine, procainamide', 'Na⁺ + K⁺', 'QRS ↑, QT ↑'],
             ['Ib', 'lidocaine, mexiletine', 'Na⁺, lets go FAST', 'little change'],
             ['!Ic', 'flecainide, propafenone', 'Na⁺, lets go SLOWLY (use-dependent)', 'QRS ↑↑'],
             ['II', 'β-blockers', 'phase 4, node', 'rate ↓, PR ↑'],
             ['!III', 'amiodarone, sotalol', 'K⁺', 'QT ↑'],
             ['IV', 'verapamil, diltiazem', 'Ca²⁺, node', 'rate ↓, PR ↑']],
            title='The classes, and the wave each one moves'),
    V.split('Class Ic', 'Pure class III',
            [('!Worse at', 'FAST rates (use dependence: no time to let go)', 'SLOW rates (reverse use dependence)'),
             ('The danger', 'slowed conduction in a SCARRED ventricle → VT (CAST)', 'torsades after bradycardia and pauses'),
             ('So', 'structurally normal hearts only', 'watch the QT, the K⁺ and the rate')],
            title='Two dangers that run in opposite directions'),
    hook(['**Class I widens the QRS · III stretches the QT · II and IV slow the node.**',
          '**Ic hates fast hearts and scars; III hates slow hearts and pauses.**']),
    'TRAPS']),
  dict(code='V12-068', t='The heart chooses the drug', vis=[
    V.table(['The heart', 'Use', 'Never'],
            [['Structurally normal (AF → sinus)', 'flecainide or propafenone, WITH a nodal blocker (Ic can make a slow flutter conducted 1:1)', ''],
             ['!Scar or failure', 'AMIODARONE (hardly depresses contraction)', 'flecainide, verapamil, diltiazem, dronedarone'],
             ['!Pre-excited AF', 'procainamide, ibutilide, or a shock', 'adenosine, verapamil, diltiazem, β-blocker, digoxin, IV amiodarone'],
             ['Long QT, torsades', 'magnesium', 'amiodarone, sotalol, procainamide'],
             ['Brugada', 'quinidine (the one exception)', 'flecainide, procainamide'],
             ['Any wide tachycardia', '', 'verapamil']],
            title='Every rule is one drug’s danger meeting one heart’s weakness'),
    V.chips([('Safe anaesthetic', 'propofol'), ('Lengthen the QT', 'sevoflurane, ondansetron, droperidol'), ('Long-term drug', 'nadolol or propranolol')],
            title='Congenital long QT in theatre', cols=3),
    hook(['**Flecainide for the normal heart, amiodarone for the scarred one, procainamide for the pathway, magnesium for torsades.**']),
    'TRAPS']),
  dict(code='CVS08B|ACLS-31', t='Adenosine: the ten-second test of the node', vis=[
    V.branch('Adenosine given for a narrow regular tachycardia', 'What happens?',
             [('It stops', 'THE NODE WAS IN THE LOOP', 'AVNRT, AVRT, some atrial tachycardias'),
              ('It slows, then the rhythm returns', 'ATRIAL', 'look for flutter waves in the pause')],
             title='Read the pause'),
    V.chips([('6 mg', 'rapid push into a large vein, chased at once with a saline flush'), ('12 mg', 'if 6 mg fails (Marrow’s next step)'),
             ('3 mg', 'the reduced first dose through a central line'), ('Half-life', 'under 10 seconds: a slow injection is destroyed on the way')],
            title='The doses follow from the half-life', cols=2),
    hook(['**Adenosine converts what uses the node and unmasks everything else.**']),
    'TRAPS']),
  dict(code='CVS08B|ACLS-32', t='Three IV drugs for a stable wide tachycardia', vis=[
    V.table(['Drug', 'Dose', 'Stop or avoid when', 'Its class showing'],
            [['Procainamide (Ia)', '20–50 mg/min, then 1–4 mg/min', 'arrhythmia stops · BP falls · QRS widens > 50% · 17 mg/kg; avoid with a long QT, heart failure', 'Na⁺ block (QRS) + K⁺ block (QT)'],
             ['Amiodarone', '150 mg over 10 min, then 1 mg/min for 6 h', 'no bar on this card: the default for a diseased heart', ''],
             ['!Sotalol (β-blocker + III)', '100 mg (1.5 mg/kg) over 5 min', 'avoid with a long QT', 'serious effect: QT prolongation and TORSADES (NEET asked)']],
            title='Each stopping rule is the drug’s own class'),
    hook(['**Procainamide: stop at a QRS one and a half times as wide.**', '**Sotalol’s danger is a potassium-channel danger: torsades.**']),
    'TRAPS']),
  dict(code='HY2|CAR-27', t='Stable lets you choose a drug; the patient chooses which', vis=[
    V.branch('Four statements from the sweep', 'True or false?',
             [('Adenosine first-line for SVT in an asthmatic', 'NO', 'bronchospasm: verapamil or diltiazem'),
              ('Verapamil for rate control with an EF of 30%', 'NO', 'class IV weakens a weak ventricle'),
              ('Maximum atropine dose is 3 mg', 'YES', 'the vagal hand fully lifted'),
              ('Nodal blocker in pre-excited AF', 'NO', 'block the pathway, never the node')],
             title='Each false one applies a correct default to the exception'),
    hook(['**The airway, the ventricle and the pathway veto the drug.**']),
    'TRAPS']),
 ]),
# =========================================================== 5
dict(id='F5', q='P12-1205', n='Section 5',
 title='What changes the waves I: potassium, calcium and magnesium',
 opener=[V.raw(D.electrolytes(), title='Eight beats, one scale: each change moves one wave',
               note='The faint dashed line in each panel is the normal beat. Potassium moves the T (and, when high, the sodium waves too); calcium moves only the ST; magnesium hides behind both.')],
 cards=[
  dict(code='V12-069', t='Potassium sets the resting potential, and acts twice', vis=[
    pic('potassium_membrane', title='High K⁺ lifts rest towards threshold; calcium lifts the threshold'),
    V.steps([('First: phase 3 runs faster', 'tall, narrow, tented T · short QT'),
             ('Then: Na⁺ channels inactivate', 'P vanishes, PR and QRS widen, then a sine wave')],
            title='High potassium, in two acts', horiz=True,
            note='High K⁺ and a sodium-channel blocker draw the same wide slurred QRS: both leave the ventricle short of working sodium channels.'),
    V.branch('Hyperkalaemia with ECG change', 'What does IV calcium do?',
             [('Lowers the potassium', 'NO', 'the number does not move'),
              ('Restores the gap between rest and threshold', 'YES', 'within minutes: it protects the heart')],
             title='Calcium is given for the ECG, not for the number'),
    hook(['**Potassium is the resting potential.** More outside, less leaks out, the cell rests nearer threshold.',
          '**Act 1 is the T; act 2 is the sodium waves (P, PR, QRS).**']),
    'TRAPS']),
  dict(code='ELEC02|KAL-10', t='The hyperkalaemia ladder, and why the trace decides', vis=[
    pic('hyperk', title='The ladder'),
    V.steps([('> 6.0', 'tall peaked T, short QT'), ('> 7.5', 'long PR, flat P, wide QRS'), ('> 9.0', 'no P, sine wave'), ('Then', 'standstill or VF')],
            title='Potassium (mmol/L) → ECG', horiz=True,
            note='A rough ladder, never a promise: stages can be skipped, from peaked T straight to arrest.'),
    V.steps([('Calcium', 'protect the membrane'), ('Shift', 'drive K⁺ into cells'), ('Remove', 'out of the body')],
            title='Any ECG change: in this order', horiz=True),
    hook(['**The trace decides the urgency; the laboratory number does not.**',
          '**6 · 7.5 · 9: T, then the sodium waves, then a sine.**']),
    'TRAPS']),
  dict(code='V12-070', t='Where high potassium comes from', vis=[
    V.split('Shift out of cells', 'Failed excretion',
            [('Why it matters', '98% of body K⁺ is inside cells: a small leak, a big number', 'the kidney cannot get rid of it'),
             ('Causes', 'acidosis (mineral far more than lactic or keto), no insulin, high osmolality', 'renal failure, too little aldosterone effect')],
            title='Only two ways up'),
    V.chips([('DKA paradox', 'serum K⁺ high or normal, body deeply SHORT: insulin drops it fast'),
             ('Before insulin', 'check K⁺; below 3.5, replace potassium first'),
             ('NAGMA + HIGH K⁺', 'type 4 RTA: too little aldosterone effect (types 1 and 2 waste K⁺: low)'),
             ('Emergency dialysate', 'K⁺ 1 mmol/L, NOT zero: too steep a fall is itself arrhythmogenic')],
            title='Four keyed facts', cols=2),
    hook(['**Type 4 is the high-potassium RTA.**', '**Dialysate K⁺: one, not none.**']),
    'TRAPS']),
  dict(code='ELEC02|KAL-06', t='Low potassium: the film run backwards', vis=[
    pic('hypok', title='Low potassium'),
    V.steps([('≈ 2.8', 'flat T (earliest)'), ('≈ 2.5', 'U wave (V2–V3)'), ('≈ 2.0', 'U taller than T, ST depression'),
             ('≈ 1.7', 'T and U fused: a long QU'), ('Then', 'torsades, VT, VF')],
            title='Potassium (mmol/L) → ECG', horiz=True,
            note='The QT looks long but it is really a QU. Replace magnesium alongside potassium (three cards on).'),
    hook(['**A tall wave after a flat T is a U wave, not a peaked T.**', '**Low K⁺ = slow phase 3: flat T, big U, long QU.**']),
    'TRAPS']),
  dict(code='ELEC03A|CAL-04', t='Low calcium stretches the ST, not the T', vis=[
    pic('calcium', title='Calcium moves only the ST'),
    V.split('Low calcium', 'Low K⁺ or a QT drug',
            [('!Which part is long', 'the ST segment (the plateau)', 'the T itself, stretched and flattened'),
             ('T wave', 'NORMAL shape and size', 'flat, broad (with a U in low K⁺)'),
             ('Torsades', 'uncommon (repolarisation stays even)', 'the real risk')],
            same=['a long QT'],
            title='Same interval, different part',
            note='Why: the L-type channel is partly shut by the calcium that enters; less calcium, the channel stays open longer, the plateau lasts longer. Also bradycardia, hypotension, heart failure.'),
    hook(['**QRS is sodium, ST is calcium, T is potassium.** Low calcium stretches the ST and leaves the T alone.']),
    'TRAPS']),
  dict(code='ELEC03A|CAL-10', t='High calcium: the plateau cut short', vis=[
    V.chips([('Short ST, short QT', 'the T seems to rise straight out of the QRS'),
             ('Very high', 'a J (Osborn) wave at a NORMAL temperature, a wider QRS'),
             ('The nodes', 'bradycardia, AV block, arrest'),
             ('Digoxin', 'more toxic: it works by loading the cell with calcium')],
            title='The exact reverse of low calcium', cols=2,
            note='DocT asked: the trap of calling the QT long in hypercalcaemia, and Osborn waves at a normal temperature.'),
    hook(['**Calcium and the QT move in OPPOSITE directions.**', '**Osborn wave + normal temperature: think high calcium.**']),
    'TRAPS']),
  dict(code='ELEC03B|MGP-03', t='Low magnesium: treated without being seen', vis=[
    V.table(['Magnesium’s job', 'When it is missing'],
            [['cofactor of the Na⁺/K⁺ pump', 'the pump falters'],
             ['!plugs the collecting duct’s K⁺ channel', 'the plug comes out: infused K⁺ pours into the urine'],
             ['release and action of PTH', 'PTH fails: calcium falls']],
            title='Three jobs, so three borrowed signs',
            note='Its ECG signs are mostly those of the potassium and calcium it drags down, plus torsades.'),
    hook(['**A low potassium that will not correct is a low magnesium.** Replace both together.']),
    'TRAPS']),
  dict(code='ELEC03B|MGP-07', t='High magnesium: a natural calcium antagonist', vis=[
    V.steps([('> 4 mEq/L', 'reflexes reduced (the knee jerk goes first)'), ('> 5', 'first-degree block'), ('> 10', 'complete heart block'), ('> 13', 'cardiac arrest')],
            title='Rising magnesium', horiz=True,
            note='1 mEq/L = 0.5 mmol/L = 1.2 mg/dL. This ladder (Marino) is in mEq/L; the card’s “mmol” heading is a slip, and obstetric texts quote higher levels: learn the ORDER. Antidote: calcium.'),
    hook(['**Think of a slow verapamil overdose plus a weak neuromuscular junction.**', '**Check the knee jerk before every dose.**']),
    'TRAPS']),
 ]),
# =========================================================== 6
dict(id='F6', q='P12-1206', n='Section 6',
 title='The QT: what it measures, what stretches it, and torsades',
 opener=[V.steps([('Measure it', 'QRS onset → T end'), ('Correct it', 'for the rate'), ('Find what stretched it', 'a gene, a drug, an ion'),
                  ('Treat torsades', 'magnesium, rate, remove the cause')],
                 title='One interval, four questions', horiz=True,
                 note='The QT is the ventricle’s action potential seen from outside: from the first sodium channel opening to the last potassium channel closing.')],
 cards=[
  dict(code='V12-071', t='Measuring and correcting the QT', vis=[
    pic('qt_measure', title='The tangent method'),
    V.chips([('Which lead', 'the longest QT with a clean T end: usually II or V5'),
             ('Where the T ends', 'draw down its steepest falling slope; where it meets the baseline'),
             ('The U wave', 'leave it out'),
             ('Bazett', 'QTc = QT ÷ √RR (s): OVERcorrects fast, UNDERcorrects slow; Fridericia (cube root) is better at the extremes')],
            title='Three rules and a correction', cols=2),
    V.table(['QTc', 'Meaning'],
            [['≤ 450 ms men, ≤ 460 ms women', 'normal'],
             ['!> 500 ms, or a rise > 60 ms', 'HIGH torsades risk: stop QT drugs, correct K⁺ and Mg²⁺'],
             ['< about 340–360 ms', 'short QT']],
            title='The lines that matter'),
    hook(['**Five hundred, or sixty more.**', '**Bazett exaggerates at both ends:** too long when fast, too short when slow.']),
    'TRAPS']),
  dict(code='V12-072', t='Congenital long QT: ask what he was doing when he collapsed', vis=[
    pic('lqt_types', title='Three diseases, one finding'),
    V.table(['Type', 'Gene · current', 'Trigger', 'T wave'],
            [['!LQT1', 'KCNQ1 · slow K⁺ LOST (the exercise reserve)', 'EXERCISE, SWIMMING', 'broad'],
             ['!LQT2', 'KCNH2 (hERG) · rapid K⁺ LOST', 'sudden NOISE, emotion, POSTPARTUM', 'notched, low'],
             ['!LQT3', 'SCN5A · late Na⁺ GAINED (a leak)', 'SLEEP, rest', 'long ST, late T']],
            title='The trigger names the type'),
    V.chips([('QTc ≥ 480', '3'), ('Torsades', '2'), ('Syncope with stress', '2'), ('High probability', '≥ 3.5')],
            title='Schwartz score: the big items', cols=4,
            note='QTc 460–479 = 2; 450–459 (men) = 1; QTc ≥ 480 at 4 min of exercise recovery, T alternans, notched T in 3 leads, syncope without stress, a relative with LQTS = 1 each; slow rate for age, deafness, family sudden death under 30 = 0.5. ≤ 1 low; 1.5–3 intermediate.'),
    hook(['**1 swims, 2 is startled (or just delivered), 3 sleeps.**', '**1 and 2 lose potassium; 3 leaks sodium.**']),
    'TRAPS']),
  dict(code='V12-073', t='Acquired long QT: one door, many drugs', vis=[
    V.table(['Family', 'Names'],
            [['Antiarrhythmics', 'class Ia, class III'],
             ['Antimicrobials', 'macrolides, fluoroquinolones, azoles, chloroquine, quinine'],
             ['Psychiatric', 'IV haloperidol, droperidol, ziprasidone, quetiapine, citalopram, TCAs'],
             ['Antiemetics', 'ondansetron, domperidone'],
             ['Others', 'methadone, arsenic trioxide, volatile anaesthetics']],
            title='They all block hERG (the rapid K⁺ current)',
            note='hERG’s inner cavity is unusually wide and sticky, so unrelated molecules all block it. An acquired long QT is a borrowed LQT2: worse with a slow heart, after a pause, with low K⁺.'),
    V.split('Vulnerable patient', 'What you do',
            [('', 'low K⁺, low Mg²⁺, slow heart, FEMALE', 'stop the drug, correct the ions, keep the rate UP')],
            title='A blocked channel in a vulnerable patient'),
    V.chips([('Safe', 'propofol'), ('Avoid', 'sevoflurane and other volatiles, ondansetron, droperidol, ketamine'), ('Continue', 'the β-blocker')],
            title='Congenital long QT under anaesthesia', cols=3),
    hook(['**Many drugs, one door: hERG.**', '**Propofol for the long QT.**']),
    'TRAPS']),
  dict(code='CVS08A|ACLS-16', t='Torsades: an afterdepolarisation becomes a rhythm', vis=[
    pic('torsades', title='Twisting of the points'),
    V.split('Polymorphic VT', 'Torsades de pointes',
            [('The QT', 'NORMAL', 'LONG'),
             ('Commonest cause', 'ischaemia or infarction', 'a drug, an ion, a gene'),
             ('Onset', '', 'short–long–short: an early afterdepolarisation after a pause')],
            same=['QRS changes beat to beat in height, axis and width'],
            title='Torsades is the long-QT member of the family'),
    V.branch('Torsades', 'What do you give?',
             [('Magnesium 2 g', 'YES', 'first'),
              ('Raise the rate (pacing, isoprenaline)', 'YES', 'a fast heart shortens the QT'),
              ('Amiodarone, procainamide, sotalol', 'NO', 'each lengthens the QT'),
              ('Pulseless or sustained', 'SHOCK', 'UNsynchronised: it cannot sync to a twisting QRS')],
             title='Treat the long QT, not just the rhythm',
             note='Marrow: if the long QT had a removable cause (a drug, an ion), remove it: no ICD needed.'),
    hook(['**Magnesium, rate, remove.**', '**Never fight torsades with a drug that lengthens the QT.**']),
    'TRAPS']),
  dict(code='HY2|CAR-06', t='Brugada: a sodium channel that fails early', vis=[
    pic('brugada', title='Type 1 diagnoses; type 2 only suggests'),
    V.split('Long QT', 'Brugada',
            [('Which phases', 'phase 3', 'phases 0 and 1 (SCN5A LOSS of function)'),
             ('!The ECG', 'long QT', 'COVED ST ≥ 2 mm into a negative T in V1–V2 (saddle-back with a positive T is NOT diagnostic)'),
             ('Unmasked by', 'pauses, low K⁺, QT drugs', 'FEVER, sleep, sodium-channel blockers'),
             ('After a survived arrest', 'remove the cause, or ICD', 'ICD (class I)')],
            same=['a normal echo: the fault is in a channel'],
            title='Two channel diseases side by side'),
    V.chips([('Quinidine', 'blocks the outward current of the notch: the adjunct for repeated shocks or a refused ICD'),
             ('Isoprenaline', 'for an electrical storm'), ('Fever', 'always treated'),
             ('Avoid', 'flecainide, procainamide (sodium blockers)')],
            title='Brugada’s drugs', cols=2),
    hook(['**Brugada lives in V1–V2:** coved, at least 2 mm, into a negative T.', '**Fever unmasks it, sodium blockers unmask it, quinidine is the one sodium-ish drug that helps.**']),
    'TRAPS']),
 ]),
# =========================================================== 7
dict(id='F7', q='P12-1207', n='Section 7',
 title='Poisons that write on the ECG: sodium channels, digoxin and the node blockers',
 opener=[V.table(['On the ECG', 'Channel', 'Think of'],
            [['!Wide QRS, tall R in aVR', 'SODIUM', 'tricyclic, cocaine, carbamazepine, propranolol'],
             ['!Long QT', 'POTASSIUM (hERG)', 'antipsychotics, citalopram, macrolides, azoles, sotalol, ondansetron'],
             ['!Slow rate, AV block', 'the NODES', 'β-blocker, verapamil, diltiazem, digoxin']],
            title='Read the poison from the trace: an overdose is an antiarrhythmic class in excess')],
 cards=[
  dict(code='V12-074', t='Sodium-channel poisoning: a class I drug over the whole heart', vis=[
    pic('tca', title='The terminal R in aVR'),
    V.chips([('QRS ≥ 100 ms', 'predicts SEIZURES'), ('QRS ≥ 160 ms', 'predicts VENTRICULAR arrhythmia'),
             ('Terminal R in aVR ≥ 3 mm', '(R/S in aVR > 0.7): the same warning'), ('Also', 'deep slurred S in I and aVL, sinus tachycardia, long QT, Brugada-like V1–V2')],
            title='The numbers', cols=2,
            note='Why aVR: the long thin right bundle suffers most, so the RV is activated last, up and to the right: towards aVR.'),
    V.branch('A wide QRS from a sodium-channel poison', 'What do you give?',
             [('Sodium bicarbonate 1–2 mmol/kg', 'YES', 'to a pH of about 7.5'),
              ('A class Ia or Ic drug', 'NO', 'more sodium block'),
              ('Physostigmine', 'NO', ''),
              ('Phenytoin', 'NO', '')],
             title='One answer, three nevers'),
    hook(['**100 fits, 160 VT.**', '**The last 40 ms points at aVR.**']),
    'TRAPS']),
  dict(code='TOX01|TOX-07', t='Three pictures, three channels', vis=[
    V.branch('An ECG in a poisoned patient', 'What has changed?',
             [('The QRS is wide', 'SODIUM', 'bicarbonate'),
              ('The QT is long', 'POTASSIUM', 'stop the drug; magnesium and potassium'),
              ('The rate is slow', 'THE NODES', 'atropine, then the antidote for that drug')],
             title='Name the channel before the drug',
             note='Normal QRS is under 120 ms, but in poisoning you act at 100. Slow uneven conduction is the ground for VT, as in a scar. Asked 15 times.'),
    hook(['**Wide = sodium · long = potassium · slow = node.**']),
    'TRAPS']),
  dict(code='HY2|CAR-07', t='Digoxin: slows the node, excites the muscle', vis=[
    pic('digoxin', title='Effect is not toxicity'),
    V.split('Digoxin EFFECT', 'Digoxin TOXICITY',
            [('What you see', 'scooped ST, short QT, slightly long PR', 'RHYTHMS: ectopy plus block'),
             ('!Signature', '', 'BIDIRECTIONAL VT'),
             ('Others', '', 'ventricular ectopics and bigeminy (commonest), atrial tachycardia with block, accelerated junctional, regularised AF (= complete block), any AV block')],
            title='The ST tells you it is there; the rhythm tells you it is too much',
            note='A peaked T is NEVER digoxin: it is hyperkalaemia.'),
    V.split('Acute overdose', 'Chronic toxicity',
            [('!Potassium', 'K⁺ > 5 marks severity → Fab', 'LOW K⁺, low Mg²⁺ or high Ca²⁺ bring it on')],
            title='Potassium means opposite things'),
    hook(['**One blocked pump, two effects:** calcium loads the muscle, the vagus slows the node.',
          '**Fab still works in an arrest: give it and keep compressing.**']),
    'TRAPS']),
  dict(code='V12-020', t='β-blockers and calcium blockers: the node, the pump, the vessels', vis=[
    V.table(['Drug', 'Heart (node, pump)', 'Vessels'],
            [['Verapamil', 'strongest', 'moderate'], ['Diltiazem', 'less', 'intermediate'], ['Amlodipine, nifedipine', 'least', 'STRONGEST']],
            title='Where each one hits'),
    V.split('Verapamil, diltiazem, β-blocker', 'Amlodipine',
            [('Picture', 'SLOW, blocked, WEAK', 'WARM, vasodilated, FAST'),
             ('First drug', 'high-dose insulin (plus calcium, glucagon for β)', 'NORADRENALINE')],
            title='Two overdoses that look different'),
    V.branch('High-dose insulin in calcium-blocker shock', 'How does it work?',
             [('It opens calcium channels', 'NO', ''),
              ('It restores the heart’s use of glucose', 'YES', 'the energy fix, not a channel fix'),
              ('It narrows a wide QRS', 'NO', 'nor do calcium or glucagon')],
             title='The mechanism NEET asks'),
    hook(['**Verapamil poisons the heart, amlodipine the vessels.**', '**Insulin feeds the heart; it does not unblock it.**']),
    'TRAPS']),
  dict(code='V12-075', t='Other poisons: name the channel or the nerve first', vis=[
    V.steps([('Early', 'nicotinic (ganglia): brief sinus tachycardia, hypertension'),
             ('Then', 'muscarinic, the vagus written large: bradycardia, long PR, AV block'),
             ('Days later', 'long QT, torsades')],
            title='Organophosphates in three phases', horiz=True,
            note='A long QTc may mark greater severity; it does not prove it.'),
    V.table(['Poison', 'ECG'],
            [['Lithium', 'flat T, sinus node pauses'], ['Theophylline', 'tachycardias, MAT, low K⁺ (adenosine fails: theophylline blocks its receptor)'],
             ['Arsenic, hydrofluoric acid', 'long QT'], ['Loperamide, diphenhydramine', 'wide QRS AND long QT']],
            title='The rest of the card'),
    hook(['**Organophosphate: fast, then slow, then long.**']),
    'TRAPS']),
  dict(code='V12-076', t='Hypothermia: every interval lengthens', vis=[
    pic('osborn', title='The Osborn wave'),
    V.steps([('< 35 °C', 'shivering artefact, sinus bradycardia'), ('< 32 °C', 'slow AF, Osborn wave, long PR, QRS, QT'), ('< 28 °C', 'VF risk'), ('< about 24 °C', 'asystole')],
            title='Core temperature → ECG', horiz=True,
            note='The Osborn (J) wave is a hump at the J point, the same way up as the QRS, and taller the colder the patient.'),
    hook(['**Cold slows every channel, so every interval lengthens at once.**',
          '**Everything that changes the ECG acts on a phase, on the node or the wire, or on what a lead can see.**']),
    'TRAPS']),
 ]),
]

# put each card's traps where it says 'TRAPS'
PAGE_CARDS = [c['code'] for sec in SECTIONS for c in sec['cards']]
for sec in SECTIONS:
    for c in sec['cards']:
        c['vis'] = [traps_for(c['code']) if v == 'TRAPS' else v for v in c['vis']]

TRAPS = [
 ('WPW with a regular, narrow tachycardia', 'Nodal drugs are banned', 'The node is part of this circuit: vagal manoeuvre, adenosine, then a nodal blocker. The ban is for pre-excited AF.'),
 ('Unstable Mobitz II', 'Atropine first', 'The block lies below the node, where the vagus does not reach. Pace through the skin as the bridge.'),
 ('Congenital long QT, going for an anaesthetic', 'Sevoflurane', 'Volatile agents lengthen the QT. Propofol is the safe agent.'),
 ('A tricyclic overdose in a child', 'A different QRS cut-off for children', 'The same 100 ms, and a child’s QRS is normally narrower, so 100 is clearly wide.'),
 ('Acute digoxin overdose: the marker of severity', 'The bradycardia, or the level', 'A potassium above 5: the marker of severity and an indication for Fab. Fab still works in an arrest.'),
 ('Torsades', 'Amiodarone', 'It blocks potassium and lengthens the QT further. Give magnesium, raise the rate, stop the drug that caused it.'),
]
