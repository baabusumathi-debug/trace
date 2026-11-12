# OBS01 top-up cards — Explain v3 ("Learn" depth), same fields and voice as obs01_learn.py.
# Fields: sub, step (index into obs01_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# The top-up's answer lines are restated in bold at the start of each part (a–d, in the order of its four answer lines); disagreements go in FLAGS, not in the text.
# Source questions read in map/doct_gt_distinct_all.jsonl (the top-up's own src): GrandT1 Q47 and AIM1 Q73 (uncontrolled asthma → pre-eclampsia, 65%), CGT1 Q44 (FEV1 55%, night symptoms,
# two emergency visits → oral corticosteroids plus inhaled therapy), GT3 Q149 / GT4 Q29 (mild asthma: GT3 mis-keyed ‘oral steroids’, 0% right; GT4 keys inhaled β2-agonist),
# plus related DocT GT questions used for traps and extra: GT2 Q40 (low birth weight, 93%), GT3 Q47 (status asthmaticus, PaO2 58, PaCO2 42, exhausted → intubate, 93%),
# GT3 Q73 (avoid 15-methyl PGF2α, 53%), CGT6 Q88 (avoid IV labetalol), CGT6 Q89 (avoid methylergonovine).
# Checked 12 Nov 2026: the question files above. Not re-checked online (standard guidance I am sure of: GINA and NAEPP asthma-in-pregnancy advice): treat as outside pregnancy, budesonide the inhaled
# steroid with the most pregnancy safety data, keep SpO2 95% or more in an attack, PaCO2 above about 35 mmHg already abnormal in pregnancy, carboprost contraindicated in asthma.
T = {}

T['T_82a35a02'] = dict(
  sub="Obstetrics → Medical disease in pregnancy → Asthma",
  step=5,
  intro="Step 5’s rule, that treating the mother properly is how the fetus is protected, is tested most often through asthma, the commonest chronic medical disease in pregnancy. The Grand Tests ask three things: what uncontrolled asthma costs (pre-eclampsia), how treatment is stepped by severity, and when an attack has become respiratory failure. The trap behind all three is under-treatment out of fear for the fetus.",
  parts=[
    ('a', "**Poor control (maternal hypoxia) → pre-eclampsia (the most consistent risk), gestational hypertension, caesarean, fetal growth restriction, preterm birth; good control removes most of the risk.** Repeated maternal hypoxia and systemic inflammation impair placental perfusion and endothelial function, which is the route to pre-eclampsia and to a small or early baby. The risks track severity and exacerbations, not the diagnosis itself: women whose asthma is well controlled have outcomes close to those of women without asthma. Asthma worsens in roughly a third of pregnancies, often because preventer treatment is stopped."),
    ('b', "**Treat as outside pregnancy: mild → inhaled SABA ± low-dose ICS (budesonide best studied); add LABA, then oral steroids for severe or uncontrolled disease; theophylline alone is inadequate.** The stepwise scheme is unchanged. Inhaled salbutamol and inhaled steroids have large safety records in pregnancy, budesonide the largest, and a woman already controlled on another inhaled steroid stays on it. Current GINA advice (since 2019) is that no adult, pregnant or not, is treated with a reliever alone, because even mild asthma can produce a severe attack and an inhaled steroid is what prevents it; so in practice the ‘± low-dose ICS’ on the card is the rule, and ‘inhaled β₂-agonist’ is the answer only because the older tiered scheme below is what DocT keys. The DocT scheme grades by lung function: FEV₁ or peak flow above 80% with brief symptoms is mild (inhaled β₂-agonist); 60–80% is moderate (add an inhaled steroid); below 60% with night symptoms, limited activity and emergency visits is severe, where an oral steroid course is added to full inhaled therapy. The small risks attributed to oral steroids are outweighed by the harm of an uncontrolled attack."),
    ('c', "**Acute attack: O₂ to SpO₂ ≥95%, nebulised SABA + ipratropium, systemic steroids, IV magnesium; a ‘normal’ PaCO₂ of about 40 signals failure (normal pregnant PaCO₂ about 30).** The drugs are those of any severe attack; only the targets move. The saturation target is higher because fetal oxygenation falls before the mother looks hypoxic (OBS-12). The PaCO₂ is read against her baseline of 30 (OBS-05): a value above about 35 is already retention, and 40 or more with exhaustion, altered sensorium or a PaO₂ under 60 mmHg means intubation, with left uterine displacement and the airway precautions of OBS-08. Magnesium and adrenaline are adjuncts, not substitutes for ventilation."),
    ('d', "**Hypoxia harms the fetus more than any asthma drug.** This is the principle that answers every management question on the topic. No standard asthma drug is withheld in pregnancy, and stepping treatment down ‘for the baby’ is the commonest cause of the attacks that do the damage."),
  ],
  table=dict(title="Asthma in pregnancy by severity (as DocT grades it)", head=["Severity", "Features", "Treatment"], rows=[["Mild", "FEV₁/PEFR **>80%**, brief symptoms", "**inhaled β₂-agonist** (± low-dose inhaled steroid)"], ["Moderate", "FEV₁/PEFR **60–80%**, symptoms more than twice a week", "**inhaled steroid + inhaled β₂-agonist**"], ["Severe", "FEV₁/PEFR **<60%**, night symptoms, limited activity, emergency visits", "inhaled therapy **+ oral corticosteroid course**"], ["Acute severe", "PaCO₂ rising to ~40, exhaustion, PaO₂ <60", "O₂ to SpO₂ ≥95%, nebulisers, systemic steroid, magnesium; **intubate**"]]),
  mimic=[
    ("Acute asthma vs physiological breathlessness of pregnancy", "Physiological: no wheeze, normal peak flow and saturation (spirometry is unchanged by pregnancy, OBS-04). Asthma: wheeze, reduced peak flow, response to a bronchodilator."),
    ("Wheeze and breathlessness in late pregnancy: asthma vs pulmonary oedema", "Pulmonary oedema (pre-eclampsia, tocolytics, peripartum cardiomyopathy, mitral stenosis): crackles, orthopnoea, hypertension or a murmur, no past asthma, poor response to a bronchodilator."),
  ],
  traps=[
    ("“Oral steroids for mild asthma in pregnancy” (DocT GT3 key, 0% right)", "A mis-key: DocT’s own explanation and the repeat of the same question in GT4 give inhaled β₂-agonist. Oral steroids are for severe disease or an exacerbation."),
    ("“Inhaled steroid and β₂-agonist” for FEV₁ 55% with night symptoms and two emergency visits", "That is the moderate tier; FEV₁ below 60% with frequent exacerbations is severe, and the key is oral corticosteroids plus inhaled therapy."),
    ("“Theophylline alone”", "Never adequate as sole treatment at any severity."),
    ("“Gestational diabetes”, “placenta praevia” or “hyperemesis” as the complication of uncontrolled asthma", "The keyed maternal complication is pre-eclampsia (65% right); the fetal one is low birth weight (93%), not macrosomia or malformations."),
    ("“PaCO₂ 42 is normal, so continue nebulisers”", "In a pregnant asthmatic 42 is 12 above baseline; with exhaustion and altered sensorium the key is intubation (93%)."),
    ("“Avoid systemic steroids and magnesium in pregnancy”", "Both are used as in any severe attack; hypoxia is the greater danger."),
  ],
  decode=[
    ("22 weeks, known asthma, worsening wheeze: which maternal complication if it stays uncontrolled? [DocT GT ×2]", "Pre-eclampsia (65%)."),
    ("Pregnant, persistent wheeze, night waking, FEV₁ 55%, two emergency visits this month: management? [DocT GT]", "Oral corticosteroids and inhaled therapy (severe asthma)."),
    ("Which treatment is suitable for mild asthma in pregnancy? [DocT GT ×2]", "Inhaled β₂-agonist (GT4 key); the GT3 copy is mis-keyed as oral steroids."),
    ("Third trimester, status asthmaticus, PaO₂ 58, PaCO₂ 42, exhausted, altered sensorium: next step? [DocT GT]", "Intubate and ventilate (93%)."),
  ],
  extra=[dict(q="Which obstetric drugs are avoided in a pregnant woman with asthma?", a="15-methyl PGF₂α (carboprost), which causes bronchospasm (53% right); DocT also keys methylergonovine/ergometrine as to be avoided, and IV labetalol (a non-selective β-blocker) for severe hypertension, where hydralazine or nifedipine is used instead. Oxytocin and prostaglandins E₁ and E₂ are safe.")],
  punch="Uncontrolled asthma in pregnancy leads to pre-eclampsia and a small or preterm baby, so treat it exactly as outside pregnancy by severity, keep saturation at 95% or more in an attack, and read a PaCO₂ of 40 as failure because her normal is 30.",
)

FLAGS = {}
FLAGS['T_82a35a02'] = "Top-up text is consistent with GINA/NAEPP advice (treat as outside pregnancy; budesonide best studied; SpO2 95% or more). One currency point: ‘mild → inhaled SABA ± low-dose ICS’ follows the older NAEPP tiers that DocT keys; GINA since 2019 no longer recommends SABA-only treatment at any step, in pregnancy as elsewhere, so the top-up could read ‘mild → low-dose ICS-containing treatment with a reliever (DocT keys inhaled β2-agonist)’. Two notes: DocT GT3 Q149 keys ‘oral steroids’ for MILD asthma (0% right, a mis-key; GT4 Q29 keys inhaled β2-agonist), and DocT’s severe tier also lists sustained-release theophylline as an add-on, which current guidelines rarely use. The top-up could add the drugs to avoid in asthma that DocT GT tests (carboprost, ergot alkaloids, IV labetalol); explanation adds them as extra."
