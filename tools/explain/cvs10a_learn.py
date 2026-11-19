# CVS10A — Explain v3 ("Learn" depth): ACS part I — myocardial injury vs infarction, the cellular course of ischaemic injury, ischaemic and non-ischaemic causes of a troponin
# rise, MI types 1–5 (Fourth Universal Definition, 2018), the Fifth Universal Definition (2026: primary, secondary, procedure-related MI, MINOCA, sex-specific 99th centile),
# epidemiology, ischaemic vs non-cardiac chest pain, the differentials of acute chest pain and the bedside examination.
# No mnemonics or hooks. Driven by qpack/CVS10A.md (15 question links; MI-09 procedural MI asked 3 times; MI-04, MI-05, MI-16 and MI-17 twice each; MI-02, MI-07, MI-10, MI-11 once).
# MI-01, MI-03, MI-06, MI-08, MI-12, MI-13, MI-14, MI-15, MI-18 and MI-19 have no linked question and get short explanations with [pattern] decode items.
# Card layer (cvs_cardlayer.json): lines and cross notes for MI-02 (posterior STEMI vs NSTEMI), MI-04 (stroke troponin, post-alteplase antiplatelets) and MI-17 (DocT ‘ibuprofen and
# reassure’ key) read and taught in the traps. No `fix` entries exist for CVS10A in trace/test/data/qbank.json (checked 19 Nov 2026).
# Checked online on 19 Nov 2026:
#  - Fourth Universal Definition of MI (Thygesen, EHJ 2018; full text as hosted by sfmu.org): clinical MI = acute myocardial injury (abnormal cTn) with evidence of acute ischaemia;
#    acute injury = rise and/or fall of cTn with ≥1 value >99th centile URL; chronic = persistently raised, stable; ‘diminished cellular glycogen, relaxed myofibrils and sarcolemmal
#    disruption are the first ultrastructural changes … seen as early as 10–15 min after the onset of ischaemia’; necrosis progresses subendocardium → subepicardium over several hours;
#    Table 1 causes of a troponin rise (ischaemic: plaque disruption; reduced perfusion: spasm/microvascular dysfunction, embolism, dissection, sustained bradyarrhythmia, hypotension/shock,
#    respiratory failure, severe anaemia; increased demand: sustained tachyarrhythmia, severe hypertension ± LVH; cardiac and systemic non-ischaemic lists as on MI-04); type 2 example
#    ‘acute GI bleed with a precipitous drop in haemoglobin’; type 4a >5× URL within 48 h with normal baseline, >20% rise if baseline raised and stable/falling, plus new ischaemic ECG,
#    new Q waves, imaging loss of viable myocardium/RWMA, or angiographic flow-limiting complication; type 5 >10× URL within 48 h, plus new Q waves, angiographic new graft/native occlusion
#    or imaging loss of viable myocardium/RWMA (new ischaemic ECG change is NOT a type 5 criterion; isolated new Q waves suffice if cTn rising but <10×); sex-specific 99th centiles
#    already ‘recommended for hs-cTn assays’ in 2018.
#  - Fifth Universal Definition of MI (Mills, Newby, Zaman et al., ESC/ACC/AHA/WHF; EHJ, JACC and Circulation; ESC Congress, Munich, 28–30 Aug 2026; ESC news page, consultantlive and
#    healio summaries): types 1–5 replaced by primary, secondary and procedure-related MI; primary = acute coronary pathology incl. atherothrombosis, SCAD, embolism, vasospasm, and stent
#    thrombosis/restenosis/graft failure >30 days after a procedure; secondary = supply–demand imbalance from another acute condition with obstructive CAD without acute coronary pathology
#    and/or new RWMA or loss of viability; procedure-related = complication of any percutaneous or surgical cardiac procedure within 30 days, no biomarker multiple, same criteria for PCI
#    and CABG; former type 3 assigned by setting or post-mortem; sex-specific 99th centile URLs required; MINOCA = myocardial injury with non-obstructive coronary arteries, a working diagnosis.
#  - AHA/ACC/ACEP 2025 ACS guideline (hendrickhealth.org PDF): ACS usually plaque rupture or erosion; UA = transient ischaemia without troponin-detected necrosis; NSTEMI partial occlusion,
#    subendocardial; STEMI complete occlusion, transmural; ECG within 10 min (1, B-NR); a nondiagnostic first ECG does not exclude ACS; type 2 MI, SCAD and MINOCA in separate documents.
#  - ESC 2023 ACS (Byrne, EHJ 2023): checked earlier today for CVS10B (ECG ≤10 min, hs-cTn 0 h/1 h or 0 h/2 h); NSTE-ACS = NSTEMI + UA, UA increasingly rare with hs-cTn.
# From standard references without a fresh check (confident unless said): subendocardial vulnerability (compression in systole, end of the perfusion line); Reimer–Jennings wavefront in
# dogs (subendocardial necrosis from about 20–40 min, largely transmural by 3–6 h); Takotsubo features; stroke/SAH catecholamine injury and the 24 h antiplatelet hold after alteplase (AHA/ASA
# 2019); INTERHEART (Yusuf, Lancet 2004: nine factors, about 90% of population attributable risk); chest-pain likelihood ratios (Swap & Nagurney, JAMA 2005: right-arm/shoulder radiation
# about 4.7, both arms 4.1; sharp, pleuritic, positional or palpation-reproduced pain about 0.2–0.3); AHA/ACC 2021 chest pain guideline (‘cardiac, possible cardiac, non-cardiac’ in
# place of ‘atypical’). Not verified: the card’s ‘above age 35, ~20% of deaths’ (WHO gives IHD about 16% of all deaths); ‘non-sustained VT’ as the most common peri-infarct arrhythmia (notes);
# the 2026 procedure list and ‘treated territory’ wording on MI-13, and the critics’ point in its watch line.
# Second review (19 Nov 2026): UDMI 2026 points re-checked against ACC journal scan (published online 28 Aug 2026, JACC), SOLACI ESC 2026 summary and ACDIS summary: three categories;
#    late (>30 d) stent/graft failure = primary (de novo disease); type 3 has no designated type, classify by setting or post-mortem, MI presumable from ischaemic presentation + new
#    ischaemic ECG or Q waves; procedure-related = within 30 days, troponin multiples no longer confirmatory, coronary complication required, plus new RWMA/viability loss in some scenarios;
#    MINOCA = myocardial injury with non-obstructive coronary arteries, a working diagnosis; sex-specific troponin thresholds. Full text (PMC, JACC) could not be opened; the exact procedure list,
#    ‘treated territory’ and the type of setting needing imaging remain unverified. Swap & Nagurney LRs and Henrikson nitrate figures not re-checked online (search limit reached).

SPINE = [
  ("Injury first, infarction second", "A troponin above the 99th centile means myocardial injury; it becomes infarction only when the injury is acute and there is evidence of acute ischaemia."),
  ("How ischaemia kills myocytes", "Ischaemic damage starts within minutes in the subendocardium and spreads outward over hours, so the time to reperfusion decides how much wall dies."),
  ("Types 1–5 (UDMI 2018)", "The 2018 definition sorts MI by mechanism: plaque thrombosis, supply–demand mismatch, death before blood tests, PCI and CABG, each with its own troponin and evidence rules."),
  ("The 2026 redefinition", "The Fifth Universal Definition replaces the numbers with primary, secondary and procedure-related MI, demands objective evidence for secondary MI, and uses sex-specific troponin limits."),
  ("The patient with chest pain", "Pressure-like, diffuse, exertional pain with radiation and autonomic symptoms raises the probability of MI, while sharp, pleuritic, one-finger or palpation-reproduced pain lowers it but never excludes it."),
  ("Mimics and bedside clues", "Aortic dissection, pericarditis and PE are the mimics that change treatment, and the arms’ blood pressures, the lungs, a new murmur and a rub point to them or to a complication."),
]

PRIMER = "Cardiac troponin is a structural protein of the cardiac myocyte that leaks into the blood when the cell membrane is damaged, for any reason; the 99th centile of a healthy reference population is the upper limit of normal. A value is ‘acute’ when serial samples show a rise and/or fall, and ‘chronic’ when it is persistently raised but stable. Ischaemia is the imbalance between oxygen supply through the coronary arteries and myocardial demand. This deck builds the definition of MI from those three ideas and then turns to how the patient presents."

L = {}

L['MI-01'] = dict(
  sub="ACS → Definition → Injury vs infarction",
  step=1,
  intro="Step 1 is the distinction on which every later card rests. Troponin tells you that myocytes are damaged; it does not tell you why. Infarction is one specific cause of that damage: ischaemia.",
  parts=[
    ('a', "**Acute myocardial INJURY (abnormal biomarkers, troponin) + evidence of acute myocardial ISCHAEMIA.** The injury must be acute (a rise and/or fall, with at least one value above the 99th centile), and the ischaemia must be shown by symptoms, new ischaemic ECG change, new Q waves, new imaging loss of myocardium or wall motion, or thrombus. Without both halves it is not MI."),
    ('b', "**Myocardial cell death resulting from prolonged ischaemia.** The pathologist’s definition is the end state: necrosis with the time course of ischaemia (MI-02). The clinical definition is how that death is recognised in a living patient."),
    ('c', "**Myocardial INJURY only - not infarction.** A troponin rise alone is the starting point of a differential (MI-03, MI-04), not a diagnosis; myocarditis, sepsis, PE or renal failure raise it without any coronary event."),
  ],
  mimic=[
    ("Acute MI vs acute non-ischaemic injury", "Both have a dynamic troponin; only MI has ischaemic evidence (symptoms, ECG, imaging, thrombus)."),
  ],
  traps=[
    ("“Raised troponin in a septic patient = NSTEMI”", "It is myocardial injury until ischaemic evidence is found (MI-12)."),
  ],
  decode=[
    ("Raised troponin, no ischaemic symptoms or ECG change: diagnosis? [pattern]", "Myocardial injury, not MI."),
  ],
  punch="Troponin defines injury; injury that is acute and ischaemic defines infarction.",
)

L['MI-02'] = dict(
  sub="ACS → Pathology → Cellular course of ischaemic injury",
  step=2,
  intro="Step 2 is what happens inside the wall after the artery closes. The subendocardium dies first because it is the most vulnerable layer, and necrosis then advances toward the epicardium; this wavefront is why the ECG divides infarcts into subendocardial (NSTEMI) and transmural (STEMI), which is what the one real question tests.",
  parts=[
    ('a', "**↓cellular glycogen, relaxed myofibrils, sarcolemmal disruption.** Without oxygen the myocyte switches to anaerobic glycolysis and burns its glycogen; ATP falls, so the myofibrils relax and contraction stops within about a minute; failing membrane pumps and calcium overload then disrupt the sarcolemma, which is the point at which troponin leaks out."),
    ('b', "**As early as 15-20 minutes after ischaemia onset.** The Fourth Universal Definition puts these first ultrastructural changes ‘as early as 10–15 min’ after the onset of ischaemia (see FLAGS); in animal models irreversible injury of the subendocardium follows at about 20–40 minutes."),
    ('c', "**ENDOCARDIUM → EPICARDIUM.** The subendocardium is compressed hardest during systole, has the highest oxygen demand and sits at the far end of the perfusion line from the epicardial arteries, so it is the first to be starved. Over several hours the necrosis spreads outward. A partially occluded artery or a short occlusion leaves a subendocardial infarct (NSTEMI); a sustained complete occlusion makes it transmural (STEMI), which is why ST elevation marks full-thickness injury."),
    ('d', "**Timely reperfusion therapy.** Opening the artery stops the wavefront where it is, so the salvaged outer wall is proportional to how early flow returns. Collateral flow and ischaemic preconditioning slow the wave and widen the window."),
  ],
  mimic=[
    ("NSTEMI vs STEMI by pathology", "NSTEMI: subendocardial (non-transmural) necrosis, partial occlusion; STEMI: transmural necrosis, complete occlusion."),
    ("Anterior subendocardial ischaemia vs posterior STEMI", "Both give ST depression in V1–V3; posterior STEMI has tall R waves, upright T waves and ST elevation ≥0.5 mm in V7–V9 (MI-22)."),
  ],
  traps=[
    ("“ST depression in V1–V3 with raised troponin is always NSTEMI (subendocardial)”", "Marrow keys subendocardial injury, but depression confined to V1–V3 may be a posterior STEMI (transmural): if the stem gives tall R in V1–V2 or ST elevation in V7–V9, pick posterior STEMI; otherwise NSTEMI."),
    ("“Necrosis starts at the epicardium, next to the occluded artery”", "It starts in the subendocardium, farthest from the epicardial arteries, and moves outward."),
  ],
  decode=[
    ("ST depression V1–V3 + positive biomarkers: mechanism of injury? [Marrow]", "Subendocardial (non-transmural) ischaemic injury; exclude posterior STEMI."),
    ("In which direction does ischaemic necrosis spread? [pattern]", "Endocardium to epicardium, over hours."),
  ],
  punch="Myocytes stop contracting in about a minute, show structural damage in 10–20 minutes, and die from the subendocardium outward over hours; reperfusion is what stops the wave.",
)

L['MI-03'] = dict(
  sub="ACS → Definition → Ischaemic causes of a troponin rise",
  step=1,
  intro="Step 1 continues with the ischaemic branch of a troponin rise. The Fourth Universal Definition (Table 1) divides it into one coronary event and a list of supply–demand imbalances; the split is what separates type 1 from type 2 MI (MI-05).",
  parts=[
    ('a', "**Atherosclerotic plaque disruption with thrombosis.** Rupture or erosion exposes thrombogenic plaque and a thrombus narrows or occludes the artery. This is type 1 MI."),
    ('b', "**Reduced perfusion: coronary spasm or microvascular dysfunction, coronary embolism, coronary artery dissection, sustained bradyarrhythmia, hypotension or shock, respiratory failure, severe anaemia.** Each lowers oxygen delivery to the myocardium without a plaque event: flow falls (spasm, embolism, dissection, slow rate, low pressure) or the oxygen content of the blood falls (hypoxaemia, anaemia). Under UDMI 2018 these are type 2 mechanisms; UDMI 2026 moves spasm, embolism and dissection to primary MI (MI-11)."),
    ('c', "**Increased O2 demand: sustained tachyarrhythmia, severe hypertension ± LVH.** Tachycardia raises demand and shortens diastole, when the left ventricle is perfused; hypertension and a hypertrophied wall raise wall tension and demand."),
  ],
  mimic=[
    ("Plaque thrombosis vs supply–demand imbalance", "Thrombus on angiography or intracoronary imaging means plaque disruption (type 1); a clear acute stressor with no thrombus means imbalance (type 2)."),
  ],
  traps=[
    ("“Coronary embolism and SCAD are type 1 because they are coronary”", "In UDMI 2018 they are supply-side type 2 causes; only in 2026 are they primary MI."),
  ],
  decode=[
    ("Septic shock, troponin rising, ST depression, no thrombus at angiography: mechanism? [pattern]", "Supply–demand imbalance (reduced perfusion, hypotension); type 2 / secondary MI."),
  ],
  punch="One cause is the plaque; everything else that starves or overworks the myocardium is supply–demand imbalance.",
)

L['MI-04'] = dict(
  sub="ACS → Definition → Non-ischaemic myocardial injury",
  step=1,
  intro="Step 1 ends with the troponin rises that have nothing to do with coronary ischaemia. Two real questions come from this list: Takotsubo after an emotional shock, and a troponin rise after stroke. In both the wrong answer is to treat the troponin as an ACS.",
  parts=[
    ('a', "**Cardiac: heart failure, myocarditis, cardiomyopathy (any type), Takotsubo, coronary revascularisation, other cardiac procedures, catheter ablation, defibrillator shocks, cardiac contusion.** Wall stress and stretch (heart failure), inflammation (myocarditis), catecholamine toxicity (Takotsubo) and direct trauma (procedures, ablation, shocks, contusion) all damage the membrane without coronary occlusion."),
    ('b', "**Systemic: sepsis or infection, chronic kidney disease, stroke or SAH, PE or pulmonary hypertension, infiltrative disease (amyloid, sarcoid), chemotherapy, critical illness, strenuous exercise.** Sepsis injures myocytes through cytokines and hypotension; CKD gives a chronic, stable elevation (reduced clearance plus structural heart disease), so the delta matters more than the value; stroke and SAH release a catecholamine surge (especially insular strokes); PE strains and injures the right ventricle. Most are chronic or acute injury, not MI, unless ischaemic evidence appears."),
  ],
  table=dict(title="Takotsubo vs anterior STEMI",
    head=["Feature", "Takotsubo", "Anterior STEMI"],
    rows=[["Trigger", "Emotional or physical stress, mostly post-menopausal women", "Plaque rupture, any trigger"],
          ["Troponin", "Modest, out of proportion to the wall motion abnormality", "Proportional to the infarct"],
          ["Angiography", "No obstructive lesion or thrombus", "Culprit occlusion"],
          ["Wall motion", "Apical ballooning with basal hyperkinesis, beyond one artery’s territory", "One coronary territory"],
          ["Course", "Recovers over weeks; LVOT obstruction possible", "Scar if not reperfused"]]),
  mimic=[
    ("Takotsubo vs anterior STEMI", "Takotsubo has unobstructed coronaries and apical ballooning that crosses territories; it is a diagnosis made at angiography."),
    ("Stroke-related troponin vs NSTEMI", "A neurogenic troponin rise usually has no ischaemic symptoms and follows the stroke; NSTEMI has an ischaemic picture."),
  ],
  traps=[
    ("“ST elevation after bad news = inferior MI”", "With unobstructed coronaries and an emotional trigger it is Takotsubo; treat LVOT obstruction with fluids, phenylephrine and beta-blockers, not inotropes."),
    ("“Troponin up after alteplase for stroke: start DAPT for NSTEMI”", "It is usually neurogenic injury; no antiplatelet for 24 h after alteplase. Marrow keys 21-day DAPT for a wake-up stroke given alteplase: 21-day DAPT is for minor stroke (NIHSS ≤3) or high-risk TIA without lysis, and wake-up stroke needs MRI mismatch before lysis. If minor and not lysed, pick DAPT; after alteplase, pick ‘no antiplatelet for 24 h’."),
  ],
  decode=[
    ("Woman, chest pain after her son’s death, ST elevation, no obstructive lesion [DocT GT · PYQ]", "Takotsubo cardiomyopathy."),
    ("Stroke treated with alteplase, troponin raised: cause and drug plan [Marrow]", "Stroke-related myocardial injury; hold antiplatelets 24 h after alteplase, statin now."),
  ],
  punch="Heart failure, myocarditis, Takotsubo, sepsis, CKD, stroke and PE all raise troponin without a coronary event; treat the cause, not the number.",
)

L['MI-05'] = dict(
  sub="ACS → Classification → MI types 1–5 (UDMI 2018)",
  step=3,
  intro="Step 3 opens with the 2018 classification by mechanism, set beside the syndromic labels used at the bedside. The two real questions here are the syndromic ones: chest pain, no ST elevation, troponin raised.",
  table=dict(title="UDMI 2018 types and syndromic labels",
    head=["Label", "What decides it"],
    rows=[["Type 1", "Plaque disruption with thrombus"],
          ["Type 2", "Supply–demand imbalance without plaque thrombosis"],
          ["Type 3", "Death before troponin could be measured"],
          ["Type 4 / 5", "Procedure-related (PCI / CABG), with troponin multiples"],
          ["STEMI vs NSTE-ACS", "ECG: persistent ST elevation or not"],
          ["NSTEMI vs unstable angina", "Troponin: above the 99th centile with a rise/fall, or not"]]),
  parts=[
    ('a', "**Type 1: Atherothrombotic - STEMI and NSTEMI, significant CAD.** The classic ACS; it can present with or without ST elevation (MI-06)."),
    ('b', "**Type 2: O2 supply/demand mismatch, usually without significant CAD.** The trigger is an acute stressor, not a plaque event (MI-07). Many patients with type 2 MI do have fixed coronary disease that the stress unmasks, which the 2018 definition allows and the 2026 definition makes a criterion (MI-12; see FLAGS)."),
    ('c', "**Type 3: Sudden cardiac death before biomarkers obtained.** Defined so that a fatal MI is not lost from the statistics for want of a blood sample (MI-08)."),
    ('d', "**Type 4: PCI-related.** Subdivided into 4a (procedural), 4b (stent thrombosis) and 4c (restenosis), with troponin multiples (MI-09)."),
    ('e', "**Type 5: CABG-related.** A higher troponin multiple, because cardiac surgery itself releases troponin (MI-09). Syndromically, **STEMI vs NSTE-ACS** is decided by the ECG; within NSTE-ACS, **NSTEMI** has a troponin rise and **unstable angina** does not. With high-sensitivity assays much of what was called unstable angina is now detected as NSTEMI, so UA is becoming less common (ESC 2023)."),
  ],
  mimic=[
    ("NSTEMI vs unstable angina", "Same pain and ECG; only troponin above the 99th centile with a rise/fall separates them."),
    ("NSTEMI vs STEMI", "Persistent ST elevation (or an equivalent) decides STEMI; T inversion or ST depression with troponin is NSTEMI."),
  ],
  traps=[
    ("“Lateral T inversion with troponin up = unstable angina”", "Unstable angina by definition has no troponin rise; raised troponin makes it NSTEMI (71% right)."),
    ("“T-wave inversion means STEMI”", "Only persistent ST elevation (or an equivalent) is STEMI."),
  ],
  decode=[
    ("Woman with risk factors, chest pain, lateral T inversion, troponin raised [DocT QBank, 71%]", "NSTEMI."),
    ("Smoker, 40 min crushing pain, no ST elevation, troponin raised on repeat [DocT GT AIM1, 85%]", "NSTEMI."),
  ],
  punch="The ECG separates STEMI from NSTE-ACS, troponin separates NSTEMI from unstable angina, and the mechanism gives the type number.",
)

L['MI-06'] = dict(
  sub="ACS → Classification → Type 1 MI",
  step=3,
  intro="Step 3 continues with the type that is ‘ACS’ in the everyday sense. The criteria are the general MI rule plus one criterion unique to type 1: a visible thrombus.",
  parts=[
    ('a', "**Atherothrombotic CAD, precipitated by plaque disruption (rupture or erosion).** Rupture of a thin fibrous cap or erosion of the endothelium over a plaque exposes thrombogenic material, and thrombus forms on it."),
    ('b', "**Rise and/or fall of cTn with at least one value above the 99th percentile URL.** The dynamic change proves the injury is acute; one high value alone could be chronic."),
    ('c', "**At least one of: symptoms of acute myocardial ischaemia; new ischaemic ECG changes; new pathological Q waves; imaging evidence of new loss of viable myocardium or new RWMA; coronary thrombus on angiography, intracoronary imaging or autopsy.** The first four are shared with type 2; thrombus is the type 1-specific criterion, because it proves the plaque mechanism directly."),
  ],
  mimic=[
    ("Type 1 vs type 2 at angiography", "Thrombus or a ruptured plaque points to type 1; a clean or fixed-stenosis artery with a clear stressor points to type 2."),
  ],
  traps=[
    ("“Q waves are needed to diagnose type 1 MI”", "Any one of the five supporting criteria is enough; symptoms alone with a dynamic troponin suffice."),
  ],
  decode=[
    ("Which criterion is specific to type 1 MI? [pattern]", "Coronary thrombus on angiography, intracoronary imaging or autopsy."),
  ],
  punch="Type 1 is a dynamic troponin over the 99th centile plus one ischaemic criterion, and only type 1 counts a thrombus as proof.",
)

L['MI-07'] = dict(
  sub="ACS → Classification → Type 1 vs type 2 MI",
  step=3,
  intro="Step 3 turns to the commonest classification problem in ICU: is the MI the plaque or the stress? The one real question is a hypertensive patient with chest pain, a normal ECG and a small troponin rise, and the cohort split between NSTEMI, unstable angina and dissection.",
  parts=[
    ('a', "**Type 1: plaque disruption with thrombosis; Type 2: supply-demand mismatch WITHOUT atherothrombotic plaque disruption.** In type 1 the artery is the problem; in type 2 the artery may be normal or fixed-narrowed, and the problem is a stressor that lowers supply or raises demand beyond what it can deliver. Treatment follows: antithrombotics and revascularisation for type 1, correction of the stressor for type 2."),
    ('b', "**Acute GI bleed: precipitous fall in haemoglobin.** Oxygen content falls and tachycardia raises demand; anticoagulating this patient as a type 1 ACS would worsen the bleed. Other common ICU examples: septic shock, rapid AF, hypoxaemia, a hypertensive surge."),
    ('c', "**Coronary thrombus: type 1 lists thrombus as a criterion; type 2 requires NO coronary thrombus on angiography, intracoronary imaging or autopsy.** Thrombus is the direct evidence of a plaque event; its absence, with a credible stressor, is what makes the label type 2."),
  ],
  mimic=[
    ("Type 2 MI vs non-ischaemic injury", "Type 2 still needs ischaemic evidence (symptoms, ECG, imaging); a troponin rise in sepsis without it is injury."),
    ("Hypertensive NSTEMI vs aortic dissection", "Check BP in both arms, pain character and mediastinum before antithrombotics."),
  ],
  traps=[
    ("“Normal ECG and only slightly raised troponin = unstable angina”", "Any troponin above the 99th centile with a rise/fall plus ischaemic symptoms is NSTEMI, even with a normal ECG (68% right). With BP 180/110 and no prior CAD, think type 2 from a hypertensive surge."),
    ("“Severe hypertension and chest pain: aortic dissection”", "Possible, and must be excluded before antithrombotics, but the stem gives nothing specific (no tearing pain or arm BP difference); NSTEMI is the keyed answer."),
  ],
  decode=[
    ("BP 180/110, chest pain, normal ECG, troponin slightly raised [DocT QBank, 68%]", "NSTEMI (consider type 2 from the hypertensive surge; exclude dissection)."),
    ("Upper GI bleed, Hb 6, ST depression, troponin rising [pattern]", "Type 2 MI (secondary MI in 2026 if CAD or new RWMA is shown); transfuse, no anticoagulation."),
  ],
  punch="Type 1 is the plaque and gets antithrombotics; type 2 is the stressor and gets the stressor fixed; a thrombus decides between them.",
)

L['MI-08'] = dict(
  sub="ACS → Classification → Type 3 MI",
  step=3,
  intro="Step 3 continues with the patient who dies before the troponin can be measured. Type 3 exists so that these deaths are counted as MI in registries and trials.",
  parts=[
    ('a', "**Cardiac death with symptoms suggesting ischaemia, without biomarker data.** The troponin criterion cannot be met because the patient died before a sample was taken or before troponin had time to rise."),
    ('b', "**Ischaemic symptoms + new ischaemic ECG changes or VF.** VF in the first hours of an occlusion is the commonest mechanism of sudden death in acute MI."),
    ('c', "**Death before blood samples could be taken; MI may be found at autopsy.** Fresh thrombus or early necrosis at post-mortem confirms it. UDMI 2026 removes type 3 as a separate type: a fatal MI is assigned primary, secondary or procedure-related by its setting or post-mortem findings, and where no biomarkers or imaging exist MI may still be presumed from an ischaemic presentation with new ischaemic ECG changes or pathological Q waves (MI-10)."),
  ],
  mimic=[
    ("Type 3 MI vs type 1 MI with death after sampling", "If a troponin was obtained and rising before death, it is type 1 (or 2); type 3 has no biomarker data."),
  ],
  traps=[
    ("“Type 3 MI is the silent MI found on later imaging”", "Type 3 is death before biomarkers; silent MI is a prior MI found on ECG or imaging."),
  ],
  decode=[
    ("Collapse in VF after 20 min of chest pain, died before bloods: MI type? [pattern]", "Type 3 (UDMI 2018); classified by setting or autopsy in 2026."),
  ],
  punch="Type 3 is the ischaemic cardiac death without a troponin, and 2026 folds it back into the other categories.",
)

L['MI-09'] = dict(
  sub="ACS → Classification → Procedure-related MI (types 4 and 5, UDMI 2018)",
  step=3,
  intro="Step 3 ends with MI caused by the treatment. This is the most-asked card in the deck: three real questions, and in the hardest only 23% of the cohort answered correctly. Every PCI and every CABG releases some troponin, so the definition sets a higher bar and demands a second, independent sign that a real infarct occurred.",
  parts=[
    ('a', "**Type 4a: normal baseline, cTn >5 × 99th URL within ≤48 h of the procedure.** Small rises from side-branch trauma and microembolisation are expected after PCI; the multiple is set so that only a large rise counts. Any rise above the 99th centile but without the further evidence is ‘procedural myocardial injury’."),
    ('b', "**Raised but stable (≤20% variation) or falling baseline: post-procedure rise >20% and the value still >5× (PCI) or >10× (CABG).** If troponin is already high from the presenting ACS, a further 20% rise is the minimum that a new event produces beyond analytical and biological variation."),
    ('c', "**4b = stent or scaffold thrombosis; 4c = restenosis.** 4b is diagnosed with the type 1 criteria plus angiographic or autopsy proof of thrombus in the stent; 4c is focal or diffuse in-stent restenosis or a complex lesion with a troponin rise, no other culprit. UDMI 2026 moves these to procedure-related if within 30 days and primary MI after 30 days (MI-10)."),
    ('d', "**Type 5: cTn >10 × 99th URL within ≤48 h of CABG.** Cardiac surgery itself (handling, cardioplegia, cannulation) causes more troponin release than PCI, so the bar is higher."),
    ('e', "**Plus new ischaemic evidence: new ischaemic ECG change, new Q waves, imaging loss of viable myocardium or new RWMA, or an angiographic flow-limiting complication (dissection, vessel or side-branch occlusion, thrombus, lost collateral flow, distal embolisation).** This is the half that people forget. For type 5 the 2018 list is narrower: new pathological Q waves, angiographic new graft or native-vessel occlusion, or imaging loss of viable myocardium/RWMA; new ST-T change alone does not count after CABG, because pericarditis and surgery make it common (see FLAGS). Isolated new Q waves meet type 5 even if troponin is rising but below 10×."),
  ],
  table=dict(title="Procedure-related MI, UDMI 2018",
    head=["", "Type 4a (PCI)", "Type 5 (CABG)"],
    rows=[["Normal baseline", ">5× 99th URL", ">10× 99th URL"],
          ["Raised stable/falling baseline", ">20% rise and >5×", ">20% rise and >10×"],
          ["Window", "≤48 h", "≤48 h"],
          ["Plus one of", "Ischaemic ECG, Q waves, imaging, angiographic complication", "Q waves, new graft/native occlusion, imaging"],
          ["Troponin only, no evidence", "Procedural myocardial injury", "Procedural myocardial injury"]]),
  mimic=[
    ("Type 4a MI vs procedural myocardial injury", "Both can exceed 5×; only 4a has new ECG, Q-wave, imaging or angiographic evidence."),
    ("Type 4b vs type 1 after PCI", "Thrombus inside the stent is 4b; a new plaque rupture elsewhere is type 1."),
  ],
  traps=[
    ("“hs-cTn 6× URL after elective PCI, asymptomatic, ECG and echo normal = type 4a MI”", "The troponin bar is met but no ischaemic evidence is present, so it is myocardial injury without infarction (only 23% right)."),
    ("“Any troponin above the 99th centile after PCI is periprocedural MI”", "That defines procedural injury; MI needs >5× (PCI) or >10× (CABG) plus evidence."),
  ],
  decode=[
    ("Elective PCI, normal baseline, hs-cTn 6× URL, no ECG or wall motion change: classify [DocT GT2, 23%]", "Myocardial injury without infarction."),
    ("MI from stent thrombosis on angiography or autopsy [Marrow]", "Type 4b (2018); 2026: procedure-related ≤30 days, primary >30 days."),
    ("Post-CABG inferior MI, cTn >10× URL [Marrow]", "Type 5."),
  ],
  punch="After PCI it takes more than 5× the 99th centile, after CABG more than 10×, within 48 hours, and always a second sign; troponin alone is procedural injury.",
)

L['MI-10'] = dict(
  sub="ACS → Classification → UDMI 2018 → UDMI 2026 mapping",
  step=4,
  intro="Step 4 opens with the Fifth Universal Definition (ESC/ACC/AHA/WHF, published at the ESC Congress in late August 2026). It keeps the definition of MI but replaces the five numbers with three categories based on where the problem starts: the coronary artery, a condition outside it, or a procedure. The one linked Marrow question is keyed on the 2018 numbering; question banks written before August 2026 will still use the old types, so answer a numbered-type question with the 2018 number.",
  parts=[
    ('a', "**Type 1 → PRIMARY MI.** Atherothrombosis remains the core of primary MI."),
    ('b', "**Type 2 → SECONDARY MI.** But with stricter evidence (MI-12)."),
    ('c', "**Type 3 → Removed: classify by setting or autopsy.** A death is assigned to whichever of the three categories the circumstances or the post-mortem support."),
    ('d', "**Types 4a and 5 → PROCEDURE-RELATED MI.** One definition for PCI and CABG, without troponin multiples (MI-13)."),
    ('e', "**4b / 4c within 30 days → procedure-related.** Early stent thrombosis or restenosis is a complication of the procedure."),
    ('f', "**4b / 4c / graft failure after 30 days → PRIMARY MI.** Late failure is treated as new coronary disease in the treated vessel, so it moves out of the procedural category."),
  ],
  mimic=[
    ("Early vs late stent thrombosis (2026)", "≤30 days: procedure-related; >30 days: primary."),
  ],
  traps=[
    ("“Stent thrombosis is always procedure-related MI”", "Only within 30 days; after 30 days it is primary MI. In a 2018-keyed question, stent thrombosis is type 4b."),
  ],
  decode=[
    ("MI from stent thrombosis on angiography/autopsy [Marrow]", "Type 4b (2018 key); 2026: procedure-related if ≤30 days, primary if >30 days."),
    ("Graft occlusion 2 years after CABG: 2026 category? [pattern]", "Primary MI."),
  ],
  punch="Type 1 becomes primary, type 2 secondary, types 4a and 5 procedure-related, type 3 disappears, and late stent or graft failure becomes primary.",
)

L['MI-11'] = dict(
  sub="ACS → UDMI 2026 → Primary MI",
  step=4,
  intro="Step 4 continues with primary MI, the 2026 heir of type 1, now widened to every acute coronary abnormality. The linked GT question is the ordinary NSTEMI stem, which shows that the syndromic labels used for treatment are unaffected by the new categories.",
  parts=[
    ('a', "**Acute myocardial injury + symptoms or other evidence of acute ischaemia.** The core definition of MI is unchanged from 2018."),
    ('b', "**Rise and/or fall of cTn I or T with one value above the SEX-SPECIFIC 99th URL.** Women have a lower normal troponin, so a single cut-off missed MI in women; 2018 recommended sex-specific limits for hs assays, 2026 requires them (MI-14)."),
    ('c', "**Atherothrombosis (rupture or erosion), SCAD, coronary embolism, vasospasm, late stent thrombosis / restenosis / graft failure (>30 days).** What they share is an acute abnormality of the coronary artery itself, found by angiography, intracoronary imaging or functional testing. SCAD, embolism and spasm were type 2 supply causes in 2018 (MI-03); now they are primary."),
    ('d', "**Within the coronary circulation itself.** The category is defined by the site where the pathology begins, not by whether there is plaque."),
  ],
  mimic=[
    ("Primary vs secondary MI", "Primary: an acute coronary abnormality; secondary: an outside condition plus fixed CAD or new RWMA, with no acute coronary lesion."),
  ],
  traps=[
    ("“SCAD in a young woman is type 2 / secondary MI”", "In 2026 SCAD is primary MI (an acute coronary pathology); in 2018 it was a type 2 supply cause."),
    ("“Crushing pain, no ST elevation, troponin up = unstable angina”", "A troponin rise makes it NSTEMI (85% right)."),
  ],
  decode=[
    ("Smoker, 40 min crushing pain, no ST elevation, troponin raised on repeat [DocT GT AIM1, 85%]", "NSTEMI."),
    ("Coronary vasospasm causing MI: 2026 category? [pattern]", "Primary MI."),
  ],
  punch="Primary MI is any acute lesion of the coronary artery itself, now including SCAD, embolism, spasm and late stent or graft failure, diagnosed against a sex-specific troponin limit.",
)

L['MI-12'] = dict(
  sub="ACS → UDMI 2026 → Secondary MI",
  step=4,
  intro="Step 4 continues with the category that most concerns ICU. In 2018 a septic or bleeding patient with a troponin rise and some ischaemic feature was easily labelled type 2; secondary MI now asks for objective support.",
  parts=[
    ('a', "**O2 supply-demand imbalance due to an alternative acute condition.** The trigger is outside the coronary artery: anaemia, hypoxaemia, shock, tachyarrhythmia, hypertension."),
    ('b', "**AND obstructive CAD without acute coronary pathology and/or new or presumed-new RWMA or absent viable myocardium.** Fixed CAD is the substrate that the stress unmasks, or the imaging shows that myocardium actually died in an ischaemic pattern."),
    ('c', "**Severe anaemia, hypoxaemia, hypotension, shock, sustained tachyarrhythmia, severe hypertension, major physiological stress.** The same stressors as the 2018 supply and demand lists, minus the coronary causes that moved to primary MI."),
    ('d', "**Myocardial INJURY - not MI.** Troponin rise plus stress without CAD or imaging evidence stays injury; it is still prognostically important but is not labelled infarction."),
  ],
  mimic=[
    ("Secondary MI vs acute myocardial injury in sepsis", "Secondary MI needs obstructive CAD or a new ischaemic RWMA; without them it is injury."),
  ],
  traps=[
    ("“Septic shock with a troponin rise is type 2 MI”", "Under 2026 it is injury unless CAD or new RWMA is shown."),
  ],
  decode=[
    ("Septic shock, troponin rising, echo normal, no CAD known: 2026 label? [pattern]", "Acute myocardial injury, not secondary MI."),
  ],
  punch="Secondary MI is a stressor plus proof (obstructive CAD or a new ischaemic wall motion abnormality); a stressor plus troponin alone is injury.",
)

L['MI-13'] = dict(
  sub="ACS → UDMI 2026 → Procedure-related MI",
  step=4,
  intro="Step 4 continues with the 2026 replacement for types 4a and 5. It drops the arbitrary troponin multiples and asks instead for a visible complication or new myocardial loss.",
  parts=[
    ('a', "**Within 30 DAYS of the intervention, in the treated territory.** In 2018 only types 4a and 5 had a window (48 h); stent thrombosis (4b) and restenosis (4c) were separate types at any time. 2026 puts every procedural complication in the first 30 days into one category, and treats later stent or graft failure as new (primary) coronary disease."),
    ('b', "**PCI, coronary angiography, CABG, valve surgery, structural interventions, catheter ablation, other cardiac procedures.** Any percutaneous or surgical cardiac procedure."),
    ('c', "**Acute myocardial injury + a coronary complication of the procedure and/or new RWMA or loss of viable myocardium on imaging.** The core requirement is evidence of a procedural coronary complication (for example a side-branch or graft occlusion, dissection or distal embolisation); in some settings the document also asks for new RWMA or loss of viable myocardium on imaging. The proof is anatomical or functional, not a troponin threshold."),
    ('d', "**Dropped: the troponin multiples (5× PCI, 10× CABG) and the 48 h window; one definition for PCI and CABG.** Troponin is released by almost every PCI and every CABG, so a numerical multiple separated infarction from expected procedural release only arbitrarily, and the 5× and 10× bars were never matched across assays. The concern noted on the card is that, without a fixed troponin bar, a small infarct with no visible complication and no imaging may go unrecorded."),
  ],
  mimic=[
    ("Procedure-related MI 2026 vs type 4a 2018", "2026: 30 days, no multiple, complication or imaging required; 2018: 48 h, >5× plus evidence."),
  ],
  traps=[
    ("“2026 still needs >5× URL after PCI”", "The multiples are gone; the bar is a complication or new imaging loss."),
  ],
  decode=[
    ("Procedure-related MI window under UDMI 2026? [pattern]", "30 days."),
  ],
  punch="Procedure-related MI in 2026 is injury plus a complication or new wall loss within 30 days of any cardiac procedure, with no troponin multiple.",
)

L['MI-14'] = dict(
  sub="ACS → UDMI 2026 → Other changes",
  step=4,
  intro="Step 4 ends with the changes outside the classification: how troponin is read, what MINOCA means, and how acute and chronic injury differ.",
  parts=[
    ('a', "**Sex-specific 99th percentile URL: women have lower normal troponin; a single cut-off under-recognised MI in women.** A unisex limit sits near the male value, so a woman’s abnormal troponin could fall below it. 2018 recommended sex-specific limits for hs assays; 2026 makes them required for injury and MI alike."),
    ('b', "**MINOCA = Myocardial INJURY with Non-Obstructive Coronary Arteries (was ‘infarction’).** Many patients so labelled turn out to have myocarditis, Takotsubo syndrome, another cardiomyopathy or pulmonary embolism rather than infarction; calling them all ‘infarction’ prejudged the answer."),
    ('c', "**A WORKING diagnosis, not a final one: find the cause.** CMR and intracoronary imaging sort it into MI (then classified primary or secondary) or a non-ischaemic diagnosis."),
    ('d', "**Acute = dynamic rise/fall; chronic = persistently raised, no significant dynamic change.** Chronic elevation (CKD, heart failure, LVH) is stable; acute injury rises or falls between samples, which is why serial testing is essential."),
  ],
  mimic=[
    ("Acute vs chronic injury in CKD", "Both may have a raised first value; only the acute has a significant change on repeat."),
  ],
  traps=[
    ("“MINOCA is a final diagnosis of infarction”", "It is now ‘injury’ and a working diagnosis that must be resolved."),
  ],
  decode=[
    ("What does the ‘I’ in MINOCA stand for under UDMI 2026? [pattern]", "Injury."),
  ],
  punch="Read troponin against a sex-specific limit, treat MINOCA as a question still open, and let the change between samples separate acute from chronic injury.",
)

L['MI-15'] = dict(
  sub="ACS → Epidemiology → Burden and INTERHEART",
  step=5,
  intro="Step 5 begins with who gets MI. The INTERHEART study (52 countries) showed that a short list of modifiable factors explains most of the risk everywhere.",
  parts=[
    ('a', "**IHD is the leading cause of death globally above age 35, ~20% of all deaths.** This is the notes’ figure and could not be traced to a primary source; WHO puts ischaemic heart disease at about 13–16% of all deaths worldwide at all ages (2019–2021 estimates), still the single leading cause, and the share is higher in middle and old age because IHD deaths are concentrated there."),
    ('b', "**INTERHEART: smoking, abnormal lipids, hypertension, diabetes, obesity, physical activity, alcohol, psychosocial factors, diet.** Together they explain about 90% of the population attributable risk of a first MI in men and women, across regions and ages. Lipids (ApoB/ApoA1 ratio) and smoking are the strongest; abdominal obesity is the measure used; regular activity, daily fruit and vegetables and moderate alcohol were protective."),
  ],
  mimic=[
    ("INTERHEART vs Framingham", "INTERHEART is a case-control study across 52 countries naming nine modifiable factors; Framingham is a US cohort that built risk scores."),
  ],
  traps=[
    ("“Family history is one of the nine INTERHEART factors”", "It is not; the nine are all potentially modifiable."),
  ],
  decode=[
    ("Which is not an INTERHEART risk factor? [pattern]", "A non-modifiable one such as family history or age."),
  ],
  punch="Nine modifiable factors, led by lipids and smoking, explain about 90% of first-MI risk worldwide.",
)

L['MI-16'] = dict(
  sub="ACS → Presentation → Ischaemic chest pain",
  step=5,
  intro="Step 5 continues at the bedside. Ischaemic pain is visceral: the heart’s afferents enter the cord with those of the chest wall, arm and jaw, so the pain is diffuse, felt as pressure, and referred. Two real questions test which features raise the probability of MI, and one is a DocT key that should not be followed.",
  parts=[
    ('a', "**Pressure-like, squeezing, tightness.** Visceral pain is poorly localised and described as heaviness rather than pain; many patients deny ‘pain’ altogether."),
    ('b', "**Exertion or emotional stress.** Both raise heart rate and blood pressure and so oxygen demand; pain that settles with rest is anginal in character."),
    ('c', "**Diffuse, retrosternal: a patient who cannot point with one finger is more likely to have MI.** Visceral afferents do not map to a point; pain localised to a fingertip is more likely somatic (MI-17)."),
    ('d', "**Left arm, jaw, shoulders, upper back.** Referral along the shared T1–T4 and cervical segments. Radiation to the right arm or both arms raises the likelihood of MI even more than radiation to the left (likelihood ratios about 4–5)."),
    ('e', "**Dyspnoea: diabetics and elderly (also silent MI).** Autonomic neuropathy and age blunt visceral pain, so breathlessness, fatigue or collapse may be the only symptom; women also present more often with accompanying symptoms."),
    ('f', "**Nausea / vomiting, diaphoresis, light-headedness, syncope.** Vagal and sympathetic activation; diaphoresis and vomiting raise the likelihood of MI."),
  ],
  mimic=[
    ("Ischaemic pain vs chest-wall pain", "Ischaemic: diffuse pressure, exertional, referred; chest wall: localised, reproduced by palpation, but palpation tenderness does not exclude MI."),
  ],
  traps=[
    ("“Exertional pain relieved by rest with chest-wall tenderness: ibuprofen and reassure”", "DocT keys this (45% right), but exertional pain relieved by rest with a family history is anginal, and tenderness is found in a minority of MIs; safe practice is aspirin + ECG + troponin first. If an ECG/troponin option is offered, pick it."),
    ("“Radiation to the right arm argues against MI”", "It raises the likelihood of MI, more than left-arm radiation."),
  ],
  decode=[
    ("Which chest pain feature does NOT raise MI likelihood: nausea, sharp, pressure, right arm radiation? [DocT GT6, 76%]", "Described as sharp."),
    ("Young man, exertional pain relieved by rest, left sternal tenderness, father died of MI: next step [DocT QBank, 45%]", "DocT keys ibuprofen and reassurance; the safe answer is aspirin and troponin with an ECG."),
  ],
  punch="Diffuse pressure, brought on by effort, radiating to either arm or the jaw, with sweating or nausea, is ischaemic until proved otherwise; in diabetics and the elderly it may be only breathlessness.",
)

L['MI-17'] = dict(
  sub="ACS → Presentation → Features favouring non-cardiac pain",
  step=5,
  intro="Step 5 continues with the features that lower the probability of MI. Each one is somatic or pleural rather than visceral. None of them excludes ACS, and the two real questions test exactly that.",
  parts=[
    ('a', "**Pleuritic: sharp or knife-like, with breathing or cough.** The parietal pleura and pericardium have somatic innervation; pain that varies with breathing points there (pericarditis, PE, pleurisy). Likelihood ratio for MI about 0.2."),
    ('b', "**Primary location in the mid or lower abdomen.** Cardiac pain rarely lies below the epigastrium."),
    ('c', "**Localised with ONE FINGER.** Somatic pain can be pinpointed; visceral pain cannot."),
    ('d', "**Reproduced by movement or palpation.** Points to the chest wall, but reproducible tenderness occurs in a minority of MIs, so it lowers probability without excluding it."),
    ('e', "**Fleeting: seconds or less.** Ischaemia lasts minutes; a pain of a few seconds is unlikely to be ischaemic."),
    ('f', "**Radiating to the lower limbs or above the mandible.** Outside the dermatomes that share the heart’s afferents; lower-limb radiation should also raise aortic dissection."),
  ],
  mimic=[
    ("Sharp pleuritic pain: pericarditis vs PE vs MI", "Positional and relieved sitting forward is pericarditis; with tachycardia and hypoxaemia, PE; MI is unlikely but not excluded."),
  ],
  traps=[
    ("“Chest-wall tenderness rules out ACS”", "DocT keys ‘ibuprofen and reassure’ (45% right), but tenderness does not exclude ACS, and exertional pain relieved by rest with a family history is anginal; ECG + troponin (and aspirin) first. If such an option is offered, pick it."),
    ("“Sharp pain raises the likelihood of MI”", "Sharp pain lowers it (76% right); pressure, nausea and radiation raise it."),
  ],
  decode=[
    ("All raise MI likelihood except: nausea, sharp, pressure, right arm radiation [DocT GT6, 76%]", "Sharp."),
    ("Exertional pain relieved by rest, left sternal tenderness, family history: next step [DocT QBank, 45%]", "DocT keys ibuprofen and reassure; the safe answer is aspirin + troponin."),
  ],
  punch="Pleuritic, one-finger, palpation-reproduced, fleeting or oddly placed pain lowers the probability of MI, but none of these features excludes it without an ECG and troponin.",
)

L['MI-18'] = dict(
  sub="ACS → Presentation → Differentials of acute chest pain",
  step=6,
  intro="Step 6 is what else the chest pain could be. The three mimics matter most because each can produce ST change or troponin and each is harmed by the ACS treatment: dissection and pericarditis by anticoagulation or lysis, PE by being missed.",
  parts=[
    ('a', "**Cardiac: ischaemia or infarction, aortic dissection, pericarditis.** All three produce chest pain with possible ECG change; dissection can occlude the right coronary and mimic inferior STEMI."),
    ('b', "**Pulmonary: PE and other causes of pulmonary hypertension.** RV strain raises troponin and gives anterior T inversion."),
    ('c', "**Chest wall trauma: myocardial or pericardial contusion, traumatic valve injury, aortic injury.** Blunt chest trauma can raise troponin and cause arrhythmia."),
    ('d', "**Non-cardiac: gastrointestinal, musculoskeletal.** Oesophageal spasm can respond to nitrates (see the Top-up card)."),
    ('e', "**The three important mimics: aortic dissection, pericarditis, pulmonary embolism.** Pericarditis vs STEMI is on CVS-08 and dissection vs ACS on AD-15."),
  ],
  mimic=[
    ("Inferior STEMI vs type A dissection involving the RCA", "Tearing pain, arm BP difference, pulse deficit, wide mediastinum or aortic regurgitation; lysis is lethal."),
  ],
  traps=[
    ("“ST elevation always means ACS”", "Dissection and pericarditis both elevate ST; check before antithrombotics."),
  ],
  decode=[
    ("Which three conditions are the important mimics of ACS? [pattern]", "Aortic dissection, pericarditis, PE."),
  ],
  punch="Before treating chest pain as ACS, exclude the three mimics that the treatment would harm: dissection, pericarditis and PE.",
)

L['MI-19'] = dict(
  sub="ACS → Examination → Bedside findings in suspected ACS",
  step=6,
  intro="Step 6 ends with the examination. In uncomplicated ACS the examination is often normal; its value is in finding a mimic or a complication that changes management.",
  parts=[
    ('a', "**BP difference between arms → aortic dissection.** A flap involving the subclavian origin lowers pressure on one side; a difference over about 20 mmHg or a pulse deficit should halt antithrombotics until imaging."),
    ('b', "**Rales / crepitations or raised JVP → heart failure.** Pulmonary congestion signals LV failure and a higher Killip class; raised JVP with clear lungs suggests RV infarction."),
    ('c', "**New systolic murmur → mechanical complication: papillary muscle rupture (MR), VSD, free wall rupture.** Papillary muscle rupture (usually posteromedial, after inferior MI) gives acute MR with pulmonary oedema; septal rupture gives a harsh murmur, often with a thrill, and a left-to-right shunt; free wall rupture usually presents as tamponade and PEA rather than a murmur (see FLAGS). These occur in the first days and are rare in the reperfusion era; urgent echo is indicated."),
    ('d', "**Pericardial rub or effusion → pericarditis.** Either a mimic or early post-infarct pericarditis over a transmural infarct; Dressler’s syndrome comes weeks later."),
    ('e', "**Most common peri-infarct arrhythmia (notes, ch. 28): non-sustained VT.** Ischaemic and reperfused myocardium is electrically unstable (raised automaticity, triggered activity and re-entry at the border zone, plus catecholamines and low potassium or magnesium), so ventricular ectopy and runs of NSVT are very common in the first 24–48 h. Counted strictly, isolated ventricular premature beats are the commonest rhythm disturbance of all, atrial fibrillation the commonest supraventricular one, and VF the commonest cause of early death (see FLAGS). Early NSVT needs correction of potassium and magnesium and beta-blockade, not antiarrhythmic drugs, and does not on its own predict later sudden death."),
  ],
  mimic=[
    ("Acute MR vs VSD after MI", "Both give a new systolic murmur and shock; echo shows a flail leaflet (MR) or a septal shunt with a step-up in oxygen saturation (VSD)."),
  ],
  traps=[
    ("“A new murmur after MI is functional, recheck tomorrow”", "A new systolic murmur after MI is a mechanical complication until echo says otherwise."),
    ("“The commonest arrhythmia after MI is VF”", "VF is the commonest cause of early sudden death, not the commonest arrhythmia; the notes give NSVT, and textbooks counting every event give ventricular premature beats. Pick NSVT if VPBs are not offered, VPBs if they are."),
  ],
  decode=[
    ("Day 3 after inferior MI, sudden pulmonary oedema, new apical pansystolic murmur [pattern]", "Papillary muscle rupture with acute MR; urgent echo and surgery."),
  ],
  punch="Arm pressures for dissection, lungs and JVP for failure, a new murmur for a mechanical complication, a rub for pericarditis; each changes what you do next.",
)

FLAGS = {
  'MI-02': "b: the Fourth Universal Definition puts the first ultrastructural changes (glycogen loss, relaxed myofibrils, sarcolemmal disruption) ‘as early as 10–15 min’ after the onset of ischaemia; the card says 15–20 minutes. The explanation gives the guideline figure.",
  'MI-05': "b: ‘usually without significant CAD’ understates type 2; the 2018 definition explicitly includes fixed atherosclerosis with supply–demand imbalance, and many type 2 patients have CAD (which 2026 makes a criterion for secondary MI). Not wrong as a contrast with type 1, but the explanation says so.",
  'MI-09': "e: the card applies one evidence list to both types; under UDMI 2018 type 5 accepts only new pathological Q waves, angiographic new graft or native occlusion, or imaging loss of viable myocardium/RWMA — new ischaemic ECG (ST-T) change and the ‘flow-limiting complication’ list belong to type 4a.",
  'MI-13': "c: possible overstatement of ‘and/or’. Summaries of UDMI 2026 (SOLACI, ESC 2026) say a procedural coronary complication is required and new RWMA / loss of viable myocardium is needed in addition in certain scenarios, which reads as ‘and, in some settings’ rather than ‘or’. Full text not opened; check before relying on the ‘imaging alone’ reading.",
  'MI-15': "a: ‘leading cause of death above age 35, ~20% of all deaths’ could not be traced to a primary source; WHO gives ischaemic heart disease about 13–16% of all deaths worldwide at all ages (2019–2021). The leading-cause part is right; treat the 20% as approximate.",
  'MI-19': "e: ‘non-sustained VT’ as the most common peri-infarct arrhythmia is the notes’ answer; standard texts give isolated ventricular premature beats as the commonest rhythm disturbance after MI (AF the commonest supraventricular one, VF the commonest cause of early death). Explanation keeps the card and names both. Also c: free wall rupture usually presents as tamponade and PEA, not as a new systolic murmur; the murmur causes are papillary muscle rupture and VSD (a contained rupture/pseudoaneurysm may give a murmur).",
}
