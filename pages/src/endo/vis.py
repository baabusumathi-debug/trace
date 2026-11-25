# Visual blocks for the endocrine page: data here, rendering in render_vis.

VIS = {
'GRID_TSH': dict(kind='grid', title='Read TSH against free T4', rlab='TSH', clab='Free T4',
  rows=['Low', 'Normal', 'High'], cols=['Low', 'Normal', 'High'],
  cells=[
   [('Central hypothyroidism', 'or severe non-thyroidal illness'), ('Subclinical hyperthyroidism', 'also illness, dopamine, steroids, first trimester'), ('Primary hyperthyroidism', '**undetectable** TSH in overt disease')],
   [('Central hypothyroidism', 'TSH **inappropriately normal**; or illness'), ('Euthyroid', 'a low T3 alone = mild illness'), ('TSH-secreting adenoma', 'the pituitary is the source')],
   [('Primary hypothyroidism', '**> 100** in myxoedema coma'), ('Subclinical hypothyroidism', 'or recovery from illness (**< 20**)'), ('TSH-secreting adenoma', 'TSH not suppressed')]],
  note='Primary thyroid disease moves TSH and T4 in opposite directions: the two corners for overt disease, the middle column for subclinical. TSH low or normal with a low T4, or TSH not suppressed with a high T4, points to the pituitary, illness or drugs.'),
'NTI_TIMELINE': dict(kind='timeline', title='Non-thyroidal illness over time', steps=[
  ('Hours–days', 'Mild illness', '**T3 falls, reverse T3 rises**; TSH and T4 normal', 'type 1 deiodinase down, type 3 up'),
  ('Severe or long', 'Severe illness', '**T4 falls, TSH low or normal**', 'TRH suppressed: a transient central hypothyroidism; T4 < 4 µg/dL ≈ 50% mortality'),
  ('Recovery', 'Overshoot', '**TSH rises, usually < 20**', 'the axis restarts; not primary hypothyroidism'),
  ('4–6 weeks later', 'Recheck', '**Repeat thyroid tests**', 'treat only TSH > 20 with a low free T4')]),
'DRUG_SITES': dict(kind='stations', title='Where each storm drug acts', stations=[
  ('Trap iodide', 'sodium–iodide symporter', ['perchlorate']),
  ('Organify and couple', 'thyroid peroxidase', ['**PTU / methimazole**', 'iodine excess (Wolff–Chaikoff)']),
  ('Store and release', 'colloid proteolysis', ['**iodine**, ≥ 1 h after the thionamide', 'lithium']),
  ('Convert T4 → T3', 'deiodinase in the tissues', ['**hydrocortisone**', 'PTU', 'propranolol']),
  ('Act on the tissue', 'up-regulated β₁-receptors', ['**propranolol** (esmolol if the EF is low)'])],
  note='Thionamides stop new hormone but not the release of stored colloid, which keeps leaking for weeks; that is why iodine is added. Cholestyramine blocks enterohepatic recycling. Aspirin frees hormone from TBG, so use paracetamol.'),
'BWPS_LADDER': dict(kind='ladder', title='Burch–Wartofsky: what the total means', rungs=[
  ('≥ 45', 'Thyroid storm', 'treat now'),
  ('25–44', 'Impending storm', 'treat if the patient is sick'),
  ('< 25', 'Storm unlikely', 'look for another cause')],
  note='30-point items: temperature ≥ 104 °F (40 °C), seizure or coma. Delirium scores 20, AF adds 10, a precipitant adds 10.'),
'STORM_ORDER': dict(kind='timeline', title='The storm sequence, and why each step sits where it does', steps=[
  ('First', 'β-blocker', '**Propranolol** 60–80 mg 4-hourly (IV 1–2 mg); **esmolol** if the EF is low', 'acts in minutes on the primed heart; also cuts T4→T3'),
  ('Next', 'Thionamide', '**PTU** 500–1000 mg, then 250 mg 4-hourly (or methimazole 60–80 mg/day)', 'stops new synthesis before any iodine arrives'),
  ('+ 1 hour', 'Iodine', '**Lugol’s or SSKI** (SSKI 5 drops 6-hourly)', 'shuts off release; earlier, it would be substrate for new hormone'),
  ('Any time', 'Hydrocortisone', '**300 mg IV, then 100 mg 8-hourly**', 'cuts T4→T3 (the keyed role) and covers adrenal reserve'),
  ('Throughout', 'Support', '**Paracetamol** (not aspirin), cooling, fluids; treat the trigger', 'infection is the commonest trigger'),
  ('24–48 h, no better', 'Rescue', '**Plasma exchange**, then emergency thyroidectomy', 'removes circulating hormone when the drugs fail')]),
'FOUR_HYPOS': dict(kind='chips', title='The pattern to recognise: everything low', items=[
  ('Hypothermia', '< 35 °C: less heat production'),
  ('Hypoventilation', 'CO₂ retention: blunted drive, weak muscles'),
  ('Hyponatraemia', 'low GFR plus ADH'),
  ('Hypoglycaemia', 'low gluconeogenesis; check cortisol'),
  ('Bradycardia', 'low voltage, long QT, T-wave inversion'),
  ('Obtundation', 'what makes it a ‘coma’')],
  note='An elderly patient, winter, a trigger (infection, cold, sedative), and four or five of these: send TSH, free T4 and cortisol, then treat.'),
'MYX_ORDER': dict(kind='timeline', title='Myxoedema coma: the order of treatment', steps=[
  ('1', 'Airway and infection', '**Intubate** if obtunded or hypercapnic; cultures and empirical antibiotics', 'aspiration and hidden infection kill'),
  ('2', 'Hydrocortisone', '**IV, about 100 mg 8-hourly**, after drawing a cortisol', 'thyroxine speeds cortisol clearance and can precipitate adrenal crisis'),
  ('3', 'IV levothyroxine', '**200–400 µg load**, then about 1.6 µg/kg/day × 75%; ± T3 5–20 µg', 'refills the T4 pool without overloading a slow heart'),
  ('Support', 'Warmth, sodium, glucose', '**Passive** rewarming; 3% saline boluses if severe; dextrose', 'active external warming causes vasodilatory collapse'),
  ('Never', 'Avoid', '**Sedatives**, active external rewarming, iodine, insulin', 'sedatives deepen hypoventilation')]),
}


from vis_gi import VIS_GI
VIS.update(VIS_GI)


def render_vis(v, inl):
    k = v['kind']
    h = '<div class="vis v-%s"><div class="vt">%s</div>' % (k, inl(v['title']))
    if k == 'grid':
        corner = inl(v['rlab']) + ((' ↓<br>' + inl(v['clab']) + ' →') if v['clab'] else '')
        h += '<div class="gw"><table class="g2%s"><tr><th class="g2c">%s</th>%s</tr>' % (' wide' if v.get('wide') else '', corner, ''.join('<th>%s</th>' % inl(c) for c in v['cols']))
        for r, row in zip(v['rows'], v['cells']):
            h += '<tr><th>%s</th>%s</tr>' % (inl(r), ''.join('<td><b>%s</b>%s</td>' % (inl(a), ('<span>%s</span>' % inl(b)) if b else '') for a, b in row))
        h += '</table></div>'
    elif k == 'timeline':
        h += '<div class="tl">'
        for when, what, do, why in v['steps']:
            h += '<div class="tl-s"><div class="tl-w">%s</div><div class="tl-b"><div class="tl-h">%s</div><div>%s</div>%s</div></div>' % (inl(when), inl(what), inl(do), ('<div class="tl-y">why: %s</div>' % inl(why)) if why else '')
        h += '</div>'
    elif k == 'stations':
        h += '<div class="st">'
        for i, (name, where, drugs) in enumerate(v['stations']):
            if i: h += '<div class="st-ar">→</div>'
            h += '<div class="st-s"><div class="st-n">%d</div><div class="st-h">%s</div><div class="st-w">%s</div>%s</div>' % (i + 1, inl(name), inl(where), ''.join('<div class="st-d">%s %s</div>' % (v.get('mark', '⊘'), inl(d)) for d in drugs))
        h += '</div>'
    elif k == 'ladder':
        h += '<div class="ld">'
        for i, (rng, lab, act) in enumerate(v['rungs']):
            h += '<div class="ld-r ld-%d"><div class="ld-x">%s</div><div class="ld-l"><b>%s</b><span>%s</span></div></div>' % (i, inl(rng), inl(lab), inl(act))
        h += '</div>'
    elif k == 'chips':
        h += '<div class="cp">' + ''.join('<div class="cp-i"><b>%s</b><span>%s</span></div>' % (inl(a), inl(b)) for a, b in v['items']) + '</div>'
    if v.get('note'): h += '<div class="vn">%s</div>' % inl(v['note'])
    return h + '</div>'
