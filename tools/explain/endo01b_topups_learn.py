# ENDO01B top-up cards — Explain v3 ("Learn" depth), same fields and voice as endo01b_learn.py.
# Fields: sub, step (index into endo01b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions: each top-up’s own src, read from doct_gt_distinct_all.jsonl and doct_qbank_all.jsonl (stems, options, keys, cohort %), 22 Nov 2026.
# Second-reviewer checks on 22 Nov 2026: Endocrine Society 2014 PPGL guideline (full-text PDF, richtlijnendatabase.nl): plasma free metanephrines ~97% sensitive in NIH cohorts (Lenders 2002:
#   99% sensitivity, 89% specificity), urinary fractionated metanephrines 97%/91%; sample supine after ≥30 min (seated ≈2.8× more false positives); ≥3-fold elevations rarely false positive;
#   pre-operative treatment 7–14 days with high-salt diet and fluids; labetalol not as initial therapy (paradoxical hypertension); MRI in pregnancy, MIBG and PET contraindicated.
# Bancos 2021 (Lancet Diabetes Endocrinol; Leiden repository full text): 249 pregnancies; maternal death 1%, fetal death 9% (3/230 and 20/230); catecholamine complications 14%; unrecognised
#   PPGL OR 27 for adverse outcome, no α-blockade OR 3.6, surgery during pregnancy OR 0.9 (no benefit); 1971 review 48% maternal and 54% fetal mortality, later reviews 5–17% (2013: 8%).
# NANETS 2017 small-bowel NET surgical consensus (Howe, Pancreas; eScholarship manuscript): routine prophylactic octreotide not shown to prevent crisis; intra-operative infusions of 100–500 µg/h
#   in practice; studies used 250–500 µg IV boluses; treat hypotension with octreotide and vasopressors (generally vasopressin and phenylephrine).
# Labetalol IV β:α about 7:1 and the critical-illness cortisol physiology (Boonen, NEJM 2013) from standard references.
T = {}

T['T_fa1bba17'] = dict(
  sub="Endocrine → Adrenal medulla → Phaeochromocytoma",
  step=2,
  intro="The adrenal crisis of step 2 has a mirror image in the medulla: too much catecholamine instead of too little cortisol. Twelve Grand Test and QBank questions ask the same three things — recognise it, confirm it with the right test, and block alpha before beta.",
  parts=[
    ('a', "**Paroxysmal headache, palpitations and sweating with episodic severe hypertension; crises are triggered by surgery, tumour handling, steroids, metoclopramide, beta-blockers and contrast. In pregnancy the episodic pattern with normal labs separates it from pre-eclampsia.** Bursts of catecholamine release explain the paroxysms; a crisis can end in pulmonary oedema, cerebral haemorrhage or cardiovascular collapse. Pre-eclampsia gives sustained hypertension with proteinuria, low platelets or raised transaminases, not paroxysms with normal tests."),
    ('b', "**Confirm with plasma free (fractionated) metanephrines, sensitivity 96–100% — COMT converts catecholamines continuously, so they stay high between bursts; 24-h urine metanephrines are the alternative.** Catecholamines themselves are released in bursts and cleared in minutes, so a normal value between bursts misleads; metanephrines are made inside the tumour all the time. The Endocrine Society quotes about 97% sensitivity for plasma free metanephrines (99% in the original series) and 97% for urinary fractionated metanephrines, so a normal plasma result virtually excludes the tumour. Blood is drawn supine after at least 30 minutes; seated sampling gives about three times as many false positives."),
    ('c', "**Image only after biochemistry (>3–4× upper limit is near-diagnostic); MRI in pregnancy (no MIBG or CT). Untreated in pregnancy, maternal and fetal mortality approaches 40–50% (crises at labour or anaesthesia), so remove the tumour laparoscopically in the second trimester or at caesarean section.** Imaging first finds incidental adrenal masses that may not secrete; a rise of three times the upper limit or more is rarely a false positive. The 40–50% is historical: a 1971 review found 48% maternal and 54% fetal mortality. The largest modern cohort (Bancos 2021, 249 pregnancies) found maternal death in 1% and fetal death in about 9%; the risk was concentrated in tumours not recognised during pregnancy (odds ratio 27 for an adverse outcome) and in women not given α-blockade, while surgery during pregnancy did not improve outcomes. The danger is an unrecognised tumour at labour or anaesthesia (FLAG)."),
    ('d', "**Alpha-blockade FIRST: phenoxybenzamine or doxazosin for 10–14 days with liberal salt and fluid; IV phentolamine 1–5 mg (or nitroprusside, nicardipine, clevidipine) for a crisis.** The Endocrine Society gives 7–14 days of pre-operative treatment. Chronic vasoconstriction shrinks the plasma volume; alpha-blockade with a high-salt diet and fluid lets it expand before surgery. Phentolamine works in 1–2 minutes and lasts minutes, so it suits an emergency; phenoxybenzamine is oral and slow, and is for preparation."),
    ('e', "**Beta-blocker only AFTER alpha-blockade, and never labetalol first (beta:alpha about 7:1 leaves alpha unopposed). After removal expect hypotension and hypoglycaemia.** Blocking β₂-mediated vasodilatation alone leaves α-constriction unopposed and the pressure climbs; the Endocrine Society warns that labetalol as initial therapy can cause paradoxical hypertension. After the tumour is out, the catecholamine drive vanishes (hypotension, from a vasodilated, under-filled circulation) and insulin is no longer suppressed (rebound hypoglycaemia)."),
  ],
  mimic=[
    ("Phaeochromocytoma vs pre-eclampsia", "Phaeo: paroxysms, normal labs, may appear before 20 weeks. Pre-eclampsia: sustained hypertension after 20 weeks with proteinuria or organ dysfunction."),
    ("Phaeochromocytoma vs sympathomimetic toxicity", "Same physiology and the same phentolamine; the history (cocaine, amphetamine) and the lack of recurrent episodes separate them."),
  ],
  traps=[
    ("Adrenal mass found at nephrectomy, BP 225/135 — “24-h urine catecholamines” or “plasma catecholamines” (13% right)", "Plasma fractionated metanephrines: highest sensitivity and negative predictive value."),
    ("Phaeo crisis with pulmonary oedema — “phenoxybenzamine” or “labetalol” (44% right)", "IV phentolamine: phenoxybenzamine is oral and slow; labetalol is mainly a beta-blocker."),
    ("Paraganglioma crisis — “labetalol” (GrandT1 Q141 keys this; Q140 keys phentolamine, 60%)", "Q141’s key is wrong; the answer is phentolamine."),
  ],
  decode=[
    ("Pregnant at 24–34 weeks with paroxysmal hypertension, sweating, palpitations, normal labs [DocT GT ×4]", "Phaeochromocytoma (68–75% right)."),
    ("Most important pre-operative step [DocT QBank, 91%]", "Alpha-blockade."),
    ("Pre-operative BP control, options labetalol, esmolol, phentolamine, clonidine [DocT GT ×3]", "Phentolamine (the only alpha-blocker offered)."),
  ],
  punch="Paroxysms with normal labs mean phaeochromocytoma: confirm with plasma metanephrines, give phentolamine for the crisis, phenoxybenzamine and salt for 10–14 days before surgery, and a beta-blocker only after the alpha-blockade.",
)

T['T_465b75d2'] = dict(
  sub="Endocrine → Adrenal physiology → Zones and cortisol action",
  step=1,
  intro="Step 1 rests on knowing which zone makes what and what drives it, because that is why secondary failure spares aldosterone. Two QBank questions test the zones and the mechanism of cortisol.",
  parts=[
    ('a', "**Zona glomerulosa: aldosterone, driven by angiotensin II and potassium — which is why it is SPARED in secondary adrenal insufficiency.** ACTH has only a minor, short-term effect on it; renin–angiotensin and potassium keep it working when ACTH is gone (ENDO-14)."),
    ('b', "**Zona fasciculata: cortisol (ACTH-driven). Zona reticularis: androgens.** Glomerulosa is outermost, then fasciculata, then reticularis next to the medulla; the two inner zones depend on ACTH and atrophy without it."),
    ('c', "**Medulla: adrenaline and noradrenaline (chromaffin cells, sympathetic ganglion origin).** The medulla is a modified sympathetic ganglion; cortisol flowing through it from the cortex induces the enzyme (PNMT) that turns noradrenaline into adrenaline."),
    ('d', "**Cortisol binds a cytoplasmic receptor; the complex enters the nucleus and alters gene transcription — hence the delay of hours.** It is lipid-soluble and crosses the membrane; the effect needs new proteins, so the full effect of a dose takes hours. Fast non-genomic effects exist but are not the main mechanism."),
    ('e', "**About 90% is bound to CBG and albumin; only free cortisol is active.** Total cortisol therefore follows the binding proteins, which fall in critical illness (next card)."),
  ],
  mimic=[
    ("Steroid vs peptide hormone action", "Steroids and thyroid hormone act through intracellular receptors and gene transcription (hours); peptides such as ACTH act on membrane receptors and second messengers (minutes)."),
  ],
  traps=[
    ("“Aldosterone comes from the zona fasciculata” (56% right)", "From the zona glomerulosa, the outermost layer."),
    ("“Cortisol acts through membrane receptors” (83% right)", "Through cytoplasmic receptors and gene transcription."),
  ],
  decode=[
    ("Which layer of the adrenal cortex makes aldosterone? [DocT QBank]", "Zona glomerulosa."),
    ("Primary mechanism of cortisol on target cells? [DocT QBank]", "Altering gene transcription through cytoplasmic receptors."),
  ],
  punch="Aldosterone comes from the outer zone under renin and potassium, cortisol from the middle zone under ACTH, and cortisol acts slowly through a cytoplasmic receptor that changes gene transcription.",
)

T['T_022928ac'] = dict(
  sub="Endocrine → Adrenal insufficiency → The axis in critical illness",
  step=3,
  intro="Step 3 explains why the critically ill patient breaks the usual tests. Two QBank questions test the changes: what drives cortisol after the first days, and which protein falls.",
  parts=[
    ('a', "**Early: CRH, ACTH and cortisol all rise.** The acute stress response is centrally driven by cytokines, pain and hypotension."),
    ('b', "**After a few days ACTH falls while cortisol stays high — the ACTH–cortisol dissociation.** High cortisol feeds back on the pituitary, so ACTH falls; cortisol stays up by other routes."),
    ('c', "**Drivers: paracrine and cytokine (IL-6) stimulation of the adrenal cortex, plus slower cortisol breakdown as hepatic and renal enzymes are suppressed.** Cytokines, endothelin and other local factors stimulate the cortex directly, and the liver and kidney inactivate cortisol more slowly (reduced A-ring reductase and 11β-HSD2 activity), so its half-life lengthens. Prolonged low ACTH may later let the cortex atrophy."),
    ('d', "**CBG FALLS (cleaved by neutrophil elastase, synthesis reduced), so free cortisol rises further and a total cortisol underestimates activity.** Neutrophil elastase cuts CBG at sites of inflammation, releasing cortisol where it is needed; hypoalbuminaemia lowers binding too."),
    ('e', "**Consequence: a single total cortisol cannot diagnose CIRCI in the ICU.** A low total may be a low CBG with adequate free cortisol, and a normal total may still be too little for tissue resistance (ENDO-16, ENDO-18)."),
  ],
  mimic=[
    ("Low ACTH in critical illness vs secondary insufficiency", "In critical illness cortisol is high and ACTH low (feedback); in secondary insufficiency both are low."),
  ],
  traps=[
    ("“ACTH primarily regulates cortisol synthesis in critical illness” (36% right)", "Paracrine and cytokine pathways do, with reduced breakdown; ACTH falls after the first days."),
    ("Which falls in critical illness — “ACTH” instead of CBG (43% right)", "The key is CBG, which falls from the start. ACTH also falls after the first days, so the option is not absurd, but CBG falls from the start and cortisol half-life rises; pick CBG."),
  ],
  decode=[
    ("In critical illness, what primarily regulates adrenal cortisol synthesis? [DocT QBank]", "Paracrine pathways (cytokines, endothelin)."),
    ("In critical illness, which is DECREASED — ACTH, CRH, CBG, cortisol half-life? [DocT QBank]", "Cortisol-binding globulin."),
  ],
  punch="In prolonged critical illness cortisol stays high while ACTH falls, driven by cytokines and slower breakdown, and CBG falls, so a single total cortisol tells you little about what the tissues receive.",
)

T['T_bc5d58f3'] = dict(
  sub="Endocrine → Adrenal and renin → Reninoma",
  step=1,
  intro="Step 1 uses aldosterone’s driver, renin, to place a lesion; the same logic separates primary aldosteronism from renin excess. One Grand Test question tested it, and only 19% got it.",
  parts=[
    ('a', "**Reninoma (juxtaglomerular cell tumour) causing secondary hyperaldosteronism.** The tumour secretes renin autonomously, so angiotensin II and aldosterone are both high."),
    ('b', "**Pattern rule: primary aldosteronism = high aldosterone with LOW renin; renovascular disease or reninoma = BOTH high.** In primary aldosteronism the excess aldosterone expands the volume and suppresses renin, so the ratio is high; when renin is the driver, the ratio is normal."),
    ('c', "**Hypokalaemia comes with metabolic ALKALOSIS, not acidosis.** Aldosterone makes the collecting duct secrete both potassium and hydrogen ions."),
    ('d', "**Diagnose with CT (small hypovascular cortical mass), not ultrasound.** The tumours are small and easily missed on ultrasound; renal artery stenosis is excluded at the same time."),
    ('e', "**Blood pressure is very hard to control until resection; ACE inhibitors or ARBs help most. Alpha-before-beta is a phaeochromocytoma rule, not a reninoma rule.** Blocking the angiotensin step treats the cause until the tumour is removed, which cures it."),
  ],
  mimic=[
    ("Reninoma vs renal artery stenosis", "Both have high renin and aldosterone; imaging shows a renal mass in one and a narrowed artery in the other."),
    ("Reninoma vs phaeochromocytoma", "Both cause severe hypertension in the young; metanephrines are normal in reninoma."),
  ],
  traps=[
    ("“Should undergo alpha-blockade before beta-blockade” (19% right)", "That is phaeochromocytoma; metanephrines are normal here. The true statement is that BP is hard to control before resection."),
    ("“Concurrent metabolic acidosis”", "Hyperaldosteronism gives alkalosis."),
  ],
  decode=[
    ("Young man, BP 215/125, hypokalaemia, high renin and aldosterone with a normal ratio, normal metanephrines, juxtaglomerular mass [DocT GT]", "Reninoma: BP is often difficult to control before resection."),
  ],
  punch="High aldosterone with low renin is primary aldosteronism; both high means renin is the driver — renal artery stenosis or, with a renal mass and normal metanephrines, a reninoma, cured only by removal.",
)

T['T_0daf26c0'] = dict(
  sub="Endocrine → Neuroendocrine → Carcinoid syndrome and crisis",
  step=2,
  intro="Another endocrine crisis that sits beside step 2: amines released by a neuroendocrine tumour. The Grand Test question turns on where the tumour drains.",
  parts=[
    ('a', "**Mediators (serotonin, histamine, bradykinin, prostaglandins) must reach the systemic circulation — usually only after liver metastases, because the liver inactivates gut-derived amines.** Gut tumours drain into the portal vein, and the liver (monoamine oxidase) clears their amines before they reach the body; metastases in the liver release straight into the hepatic veins."),
    ('b', "**Exception: bronchial, ovarian and retroperitoneal primaries drain outside the portal system, so they cause the syndrome WITHOUT metastases.** Their venous blood reaches the systemic circulation directly."),
    ('c', "**Features: flushing, diarrhoea, bronchospasm, right-sided valve fibrosis (tricuspid regurgitation, pulmonary stenosis).** Histamine and bradykinin cause flushing and wheeze, serotonin diarrhoea and fibrosis; the lung inactivates serotonin, so the left heart is usually spared unless the primary is bronchial or there is a shunt."),
    ('d', "**Crisis (anaesthesia, tumour handling): octreotide 50–100 µg IV bolus, then 50–100 µg/h.** Octreotide stops mediator release at the somatostatin receptors. Those are older textbook doses: NANETS 2017 describes intra-operative infusions of 100–500 µg/h and IV boluses of 250–500 µg in practice, and notes that routine prophylactic octreotide has not been shown to prevent crisis, so the team must be ready to treat it (FLAG)."),
    ('e', "**Avoid catecholamines and histamine releasers; use vasopressin or phenylephrine for hypotension.** Catecholamines can trigger further mediator release from the tumour and worsen the crisis, which is why NANETS treats the hypotension with octreotide plus vasopressin or phenylephrine; morphine and atracurium release histamine."),
  ],
  mimic=[
    ("Carcinoid crisis vs anaphylaxis under anaesthesia", "Both give flushing, bronchospasm and hypotension; a known neuroendocrine tumour or tumour handling points to carcinoid, where adrenaline may worsen it and octreotide treats it."),
  ],
  traps=[
    ("“Carcinoid syndrome only occurs with liver metastases” (91% recognised as FALSE)", "Bronchial, ovarian and retroperitoneal tumours bypass the liver."),
  ],
  decode=[
    ("Which statement about neuroendocrine tumours is FALSE? [DocT GT]", "Carcinoid syndrome only occurs in the presence of liver metastases."),
  ],
  punch="Carcinoid syndrome needs amines to bypass the liver — through liver metastases or a primary outside the portal system — and a crisis is treated with octreotide, not with catecholamines.",
)

FLAGS = {
  'T_fa1bba17': "c: ‘maternal and fetal mortality approaches 40–50%’ is historical (1971 review: 48% maternal, 54% fetal); Bancos 2021 (249 pregnancies) found maternal death 1% and fetal death about 9%, with risk concentrated in unrecognised tumours (OR 27) and no α-blockade (OR 3.6); surgery during pregnancy did not improve outcome (OR 0.9). Consider ‘historically up to 50% if unrecognised; now about 1% maternal, 9% fetal’. d: Endocrine Society 2014 gives 7–14 days of pre-operative blockade, not 10–14. Also: GrandT1 Q141 keys labetalol for a paraganglioma crisis while Q140 (same stem) keys phentolamine; phentolamine is right.",
  'T_0daf26c0': "d: octreotide 50–100 µg bolus then 50–100 µg/h are older textbook doses; NANETS 2017 describes 250–500 µg IV boluses and 100–500 µg/h infusions in practice and says routine prophylaxis has not been shown to prevent crisis. Consider ‘octreotide IV bolus (often 100–500 µg) and infusion, plus vasopressin or phenylephrine’.",
}
