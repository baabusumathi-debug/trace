# OBS02B top-up cards — Explain v3 ("Learn" depth), same fields and voice as obs02b_learn.py.
# Fields: sub, step (index into obs02b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source questions: map/out/all_rows.json — DocT GT2 Q95 (admission haemorrhage risk; keyed ‘Moderate risk’, 23% right, key disputed), Marrow QB53-Q03 (shock index with significant
# blood loss in PPH: 0.9–1.1), DocT GT2 Q130 (NYHA class III in the third trimester: ‘accounts for most cardiac deaths’, 100% right).
# Checked online 12 Nov 2026: obstetric shock index thresholds (Nathan/El Ayadi, PLoS One 2016, 958 women with hypovolaemic shock from obstetric haemorrhage: ≥0.9 referral, ≥1.4 urgent
# intervention, ≥1.7 high chance of adverse outcome); admission haemorrhage risk table in the ACOG Safe Motherhood version (medium: prior caesarean or uterine surgery, multiple gestation,
# >4 births, prior PPH, large fibroids, EFW >4000 g, BMI >40, haematocrit <30% with other risks; intrapartum medium: chorioamnionitis, prolonged oxytocin, magnesium; high: praevia or
# low-lying placenta, suspected accreta, known coagulopathy, active bleeding, platelets <70,000, two or more medium factors; type and screen for medium, type and cross for high);
# ESC 2025 pregnancy guideline summaries (mWHO 2.0; Pregnancy Heart Team from class II–III; class IV: counselling on very high risk with shared decision-making including termination).
# Not re-opened (quoted from ESC 2018 and standard teaching): the mWHO class IV list and its numbers (EF <30%, Marfan aorta >45 mm, bicuspid aorta >50 mm), event rate 40–100% in class IV,
# the ‘10% of patients, 85% of deaths’ figure for NYHA III–IV (older obstetric series).
# Second check (12 Nov 2026, independent reviewer): AWHONN risk table v1.1 opened (as reproduced in PMC8289851): high risk includes haematocrit <30 with other risk factors and platelets <100,000;
# medium includes chorioamnionitis, polyhydramnios, EFW >4 kg and BMI >35; two or more medium items = high. The card is therefore AWHONN except for BMI (>40 is the ACOG Safe Motherhood cut-off)
# and the unqualified haematocrit. Full DocT GT2 Q95 stem read: prior caesarean, chorioamnionitis in a PREVIOUS pregnancy, polyhydramnios now.
T = {}

T['T_c9b689d4'] = dict(
  sub="Obstetrics → Haemorrhage → Admission risk and the shock index",
  step=3,
  intro="Step 3 explained why obstetric bleeding is recognised late. These are the two tools that answer that problem: a risk table applied on admission, so that blood is ready before the bleeding starts, and the shock index, which moves before the systolic pressure does. Each has one bank question: a GT stem asking for the risk category (only 23% matched the key, and the key is disputed), and a Marrow stem asking which shock index means significant loss.",
  parts=[
    ('a', "**Medium risk: prior caesarean or uterine surgery, multiple gestation, more than 4 vaginal births, chorioamnionitis, prior PPH, fibroids, estimated fetal weight over 4 kg, BMI over 40, polyhydramnios.** Each item is a reason for the uterus to contract poorly (over-distension from twins, a large baby or polyhydramnios; an exhausted or infected muscle; fibroids; high parity) or to bleed from a scar. One of these alone makes atony more likely but not probable, so the blood bank response is a type and screen. The cut-offs differ a little between versions of the table: AWHONN itself counts a BMI over 35, the ACOG version over 40."),
    ('b', "**High risk: praevia or low-lying placenta, suspected accreta, haematocrit under 30%, platelets under 100,000, active bleeding, coagulopathy, OR two or more medium factors → cross-match 2 units, plan for massive transfusion.** In the AWHONN table the haematocrit under 30% counts only when another risk factor is present. These are conditions in which heavy bleeding is expected (an abnormally sited or invading placenta, bleeding already under way) or cannot be tolerated or stopped (little red-cell reserve, poor clotting). The rule that is asked is the last one: medium factors add up, and two or more make the woman high risk. High risk means blood cross-matched and available and the haemorrhage plan reviewed before delivery."),
    ('c', "**Shock index = heart rate ÷ systolic pressure: normal 0.5–0.7 (pregnancy 0.7–0.9).** Early in bleeding the pulse rises while vasoconstriction holds the systolic pressure, so the ratio changes while each number alone still looks acceptable. The normal range is higher in pregnancy because the resting heart rate is faster and the pressure a little lower."),
    ('d', "**≥0.9–1.1 = significant loss; >1.4–1.7 = urgent transfusion or massive transfusion protocol.** A pulse equal to or above the systolic pressure (index about 1) in a bleeding parturient means substantial loss whatever the pressure reads. In the validation study of 958 women with obstetric haemorrhage, an index of 0.9 or more identified those needing referral, 1.4 or more the need for urgent intervention, and 1.7 or more a high chance of death or severe morbidity."),
  ],
  table=dict(title="Admission risk and what the blood bank does", head=["Risk", "Who", "Blood bank"], rows=[
    ["Low", "no uterine scar, singleton, ≤4 vaginal births, no bleeding disorder, no prior PPH", "hold a sample"],
    ["Medium", "one medium factor", "**type and screen**"],
    ["High", "any high factor, **or ≥2 medium factors**", "**cross-match 2 units**, plan MTP"],
  ]),
  mimic=[
    ("Shock index vs systolic pressure alone", "A pulse of 115 with a pressure of 105/60 passes on pressure alone but gives an index of 1.1, which is significant loss."),
    ("Risk table vs shock index", "The table is applied before bleeding, to prepare blood; the index is applied during bleeding, to judge how much has gone."),
  ],
  traps=[
    ("“Moderate risk” for a G5P4 with a previous caesarean plus other medium factors (DocT GT key, 23% right)", "The stem gives a previous caesarean, chorioamnionitis in a previous pregnancy, and polyhydramnios now. DocT keys moderate, saying none of these is a high-risk item. But the caesarean scar and the polyhydramnios are two medium factors (the past chorioamnionitis does not count for this labour, and four previous births is not ‘more than 4’), and by the AWHONN table two or more medium factors make her high risk. ‘High risk’ is the better answer and the key is disputed; the stem is repeated in a later GT with the same key, so know what DocT expects."),
    ("“Normal shock index is the same in pregnancy”", "It is 0.7–0.9 in pregnancy against 0.5–0.7 otherwise, so 0.8 is not abnormal in a parturient."),
    ("“Wait for the systolic pressure to fall below 90 before transfusing”", "She can lose 1–1.5 L before that happens (OBS-34); an index of 0.9 or more is the earlier trigger."),
    ("“Shock index 0.5–0.7” or “0.7–0.9” as the value showing significant loss", "Those are the normal ranges, non-pregnant and pregnant; the Marrow answer is 0.9–1.1."),
  ],
  decode=[
    ("G5P4 in labour, previous caesarean, chorioamnionitis in a previous pregnancy, polyhydramnios on ultrasound — haemorrhage risk category? [DocT GT ×2]", "Keyed moderate (23%); two medium factors (scar, polyhydramnios) are high risk by the AWHONN table."),
    ("Shock index associated with significant blood loss in PPH? [Marrow]", "0.9–1.1."),
    ("PPH, pulse 130, pressure 90/50 — shock index and action? [pattern]", "1.4: urgent transfusion and massive transfusion protocol."),
  ],
  punch="Two medium factors make a woman high risk and earn a cross-match before she bleeds. Once she is bleeding, a pulse that has reached the systolic pressure means significant loss, and 1.4 means transfuse now.",
)

T['T_88bbc332'] = dict(
  sub="Obstetrics → Heart → Heart disease in pregnancy: who dies and when",
  step=5,
  intro="Step 5 dealt with a heart that fails because of pregnancy (OBS-38). This card is about the heart that was already diseased. Pregnancy demands a 30–50% rise in cardiac output and a larger blood volume, and a heart that cannot raise its output, or a circulation with a fixed obstruction, decompensates. The one GT question asks what NYHA class III in the third trimester implies.",
  parts=[
    ('a', "**About 85%; NYHA I–II mortality is under 1%.** Women in NYHA class III–IV are only about a tenth of pregnant women with heart disease but account for about 85% of the cardiac deaths. Functional class measures reserve: a woman breathless on minimal exertion before pregnancy has nothing left to meet the extra output, while one in class I–II usually tolerates it. The figures come from older obstetric series but the conclusion holds: symptoms at rest or on slight exertion carry most of the mortality."),
    ('b', "**Pregnancy is contraindicated in mWHO class IV: pulmonary arterial hypertension, ejection fraction under 30%, severe mitral stenosis or symptomatic aortic stenosis, Marfan aorta over 45 mm.** The modified WHO classification grades the lesion, not the symptoms, and class IV carries a maternal cardiac event rate of about 40–100%. The members share one of three problems. A fixed obstruction cannot pass the extra output: in mitral stenosis the faster heart rate shortens filling and left atrial pressure rises to pulmonary oedema; in aortic stenosis output cannot rise; in pulmonary hypertension the right ventricle fails. A weak ventricle (ejection fraction under 30%, or previous peripartum cardiomyopathy with residual impairment) cannot generate it. A fragile aorta may dissect under the higher stroke volume and hormonal change in the wall. Regurgitant lesions and left-to-right shunts are tolerated much better, because the fall in systemic resistance in pregnancy reduces their load."),
    ('c', "**Peak danger: late second and third trimester, labour, and the first days postpartum (autotransfusion).** Blood volume and cardiac output reach their peak at about 28–32 weeks. In labour each contraction pushes several hundred millilitres of blood from the uterus into the circulation, and pain raises heart rate and pressure. Immediately after delivery the emptied uterus contracts and the vena cava is decompressed, so venous return rises abruptly, and over the next days fluid moves back from the tissues. A woman with mitral stenosis or a weak ventricle therefore develops pulmonary oedema most often just after delivery, not during it."),
  ],
  mimic=[
    ("NYHA class vs mWHO class", "NYHA grades symptoms (I none, IV at rest). mWHO grades the lesion’s risk (I no added risk, IV extremely high risk). A woman can be NYHA I with an mWHO IV lesion, for example a dilated Marfan aorta."),
    ("Stenotic vs regurgitant valve lesions in pregnancy", "Stenosis is tolerated badly (fixed output, tachycardia shortens filling). Regurgitation is tolerated well (lower systemic resistance reduces the regurgitant volume)."),
  ],
  traps=[
    ("“The risk ends once the baby is delivered”", "The first hours and days postpartum are a peak, from autotransfusion and fluid returning from the tissues."),
    ("“A regurgitant lesion is as dangerous as a stenotic one”", "Stenotic lesions and pulmonary hypertension are the dangerous ones."),
    ("“NYHA III–IV patients are the majority of cardiac deaths because they are the majority of cardiac patients”", "They are about 10% of patients and about 85% of deaths."),
  ],
  decode=[
    ("Pregnant woman with NYHA class III heart failure in the third trimester — which statement best describes this group? [DocT GT]", "Accounts for most cardiac deaths (100% right)."),
    ("Which cardiac condition is a contraindication to pregnancy? [pattern]", "Pulmonary arterial hypertension, EF under 30%, severe mitral stenosis, severe symptomatic aortic stenosis, Marfan aorta over 45 mm (mWHO IV)."),
    ("Mitral stenosis, well in labour, pulmonary oedema minutes after delivery — why? [pattern]", "Autotransfusion from the contracted uterus and relief of caval compression raise venous return."),
  ],
  punch="NYHA III–IV is a tenth of the patients and most of the deaths. Fixed obstruction, a weak ventricle and a fragile aorta are the mWHO IV lesions, and the dangerous times are the third trimester, labour and the first days after delivery.",
)

FLAGS = {
  'T_c9b689d4': "The list matches the AWHONN table (v1.1) with two differences: AWHONN’s high-risk haematocrit item is ‘haematocrit <30 AND other risk factors’ (the card drops the qualifier), and AWHONN’s obesity cut-off is BMI >35 (the card’s >40 is the ACOG Safe Motherhood version, which also puts haematocrit <30% in the medium group and uses platelets <70,000). The card omits AWHONN’s other medium items (induction of labour, fetal demise, family history of PPH) and the high-risk item ‘more than one previous PPH’. The asked rule (two or more medium factors = high risk) is in both versions. The DocT GT key for the linked stem (‘moderate’, GT2 Q95, repeated in GT5) conflicts with that rule; DocT’s own table omits it. Shock index thresholds agree with El Ayadi/Nathan, PLoS One 2016 (≥0.9, ≥1.4, ≥1.7); ‘0.9–1.1’ as a band is the Marrow answer.",
  'T_88bbc332': "‘Pregnancy contraindicated in mWHO IV’ is the ESC 2018 wording; the ESC 2025 guideline (mWHO 2.0) keeps class IV as extremely high risk but frames it as counselling and shared decision-making, including termination. The class IV list on the card is a selection (also: previous PPCM with residual impairment, systemic right ventricle with impaired function, bicuspid aorta >50 mm, vascular Ehlers–Danlos, severe coarctation, complicated Fontan). The ‘10% / 85%’ figure is from older obstetric series and could not be traced to a primary source.",
}
