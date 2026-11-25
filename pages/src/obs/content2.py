# Written layer v2: core (numbered teaching flow), structured mimic pairs, decision trees.
# Pair: (A, B, [shared], [(feature, a, b)])  — a feature starting with '!' is the deciding split.
# Tree: {'start': shared presentation, 'q': question, 'b': [ {'a': answer, 'dx': name, 'c': clue} | {'a': answer, 'q':..., 'b': [...]} ]}

CORE, PAIRS, TREES = {}, {}, {}

K = ('OBS01', 1)
CORE[K] = [
 "Obstetric patients are **1–4.5%** of ICU admissions; mortality **5–20%**; **70%** of maternal deaths are preventable.",
 "Commonest reason for ICU: **pre-eclampsia/eclampsia** (~75%), then medical disease, then haemorrhage.",
 "Diseases **of** pregnancy: pre-eclampsia, HELLP, fatty liver, amniotic fluid embolism, peripartum cardiomyopathy, obstetric haemorrhage, chorioamnionitis/septic abortion, magnesium toxicity, tocolytic pulmonary oedema, OHSS.",
 "Diseases **worsened by** pregnancy: ARDS, **aspiration**, pulmonary embolism, urosepsis, hepatitis E, varicella pneumonia, falciparum malaria, H1N1, cerebral venous thrombosis, DKA, valve disease, pulmonary hypertension.",
 "Why it is hard: altered physiology, pregnancy-specific diseases, **the fetus**, and clinicians' unfamiliarity.",
 "The obstetric lethal triad is **hypotension, hypoxia, anaemia**: the three determinants of oxygen delivery to mother and fetus.",
 "Heart disease (top-up): NYHA III–IV mothers are ~10% of cardiac patients but **~85% of cardiac deaths**; pregnancy is contraindicated in PAH, EF **<30%**, severe MS, symptomatic AS, Marfan aorta **>45 mm**.",
]
PAIRS[K] = [
 ("Obstetric lethal triad", "Trauma lethal triad", ["Both are 'lethal triads' that kill by spiralling together"],
  [("!Components", "Hypotension, hypoxia, anaemia", "Hypothermia, acidosis, coagulopathy"),
   ("Logic", "Determinants of oxygen delivery", "Determinants of clotting failure"),
   ("Stem cue", "Set in pregnancy", "Set in trauma")]),
]

K = ('OBS01', 2)
CORE[K] = [
 "**Heart:** cardiac output **+40–50%** (stroke volume first, then heart rate **+15–25%**); blood volume **+45%**; SVR **−20%**; diastolic falls mid-pregnancy; CVP unchanged; O₂ consumption **+30–40%**.",
 "**Lung:** tidal volume **+40%**, **FRC −20%**, vital capacity **unchanged**; progesterone drives the extra ventilation.",
 "**Gas:** pH **7.40–7.47**, PaCO₂ **~30**, HCO₃ **18–22**: a compensated respiratory alkalosis. A PaCO₂ of **40** in a breathless woman means she is **tiring**, and the low bicarbonate leaves less buffer.",
 "**Blood:** plasma rises more than red cells → dilutional Hb **~10.5–11** with normal MCV and ferritin. Fibrinogen **4–6 g/L**: hypercoagulable, so **≤2 g/L is already DIC**.",
 "**Kidney:** GFR **+50%**, creatinine **0.4–0.8** → a creatinine of **1.0 is abnormal**.",
 "**Gut:** lax lower oesophageal sphincter and slow transit → **aspiration** risk.",
 "**Aortocaval compression** from **~20 weeks**: lying flat, the uterus squeezes the IVC (less preload) and aorta → hypotension and poor placental flow. Fix: **left uterine displacement**, a wedge under the **right** hip; **manual** displacement in arrest.",
 "**Heart sounds:** S3, loud split S1 and a soft ejection murmur are normal; **any diastolic murmur, fixed split S2 or S4** is disease.",
]
PAIRS[K] = [
 ("Normal pregnancy", "Early sepsis", ["High cardiac output", "Low SVR", "Fast pulse", "Warm peripheries"],
  [("Temperature", "Normal", "Fever"),
   ("!Resp rate", "Up to ~20", "**≥25**"),
   ("!Systolic BP", "Lowish but >90", "**≤90**"),
   ("Lactate / mentation", "Normal", "Raised / altered")]),
 ("Normal pregnant gas", "'Normal-looking' gas in a breathless woman", ["Bicarbonate ~20", "pH looks acceptable"],
  [("!PaCO₂", "**~30**", "**40**"),
   ("pH", "~7.44", "~7.36"),
   ("Meaning", "Compensated respiratory alkalosis", "Relative **hypoventilation**: she is tiring")]),
 ("Supine hypotension", "Haemorrhage", ["Pregnant, lying flat", "Hypotension and tachycardia"],
  [("!Left uterine displacement", "BP recovers **within a minute**", "No recovery"),
   ("Next step", "Keep her displaced", "Look for bleeding (incl. concealed)")]),
 ("Normal pregnancy coagulation", "Early DIC", ["Platelets normal or slightly low", "A fibrinogen a non-pregnant range calls 'normal'"],
  [("!Fibrinogen", "**4–6 g/L**", "**≤2 g/L**"),
   ("Setting", "Healthy pregnancy", "Abruption, AFE, massive PPH")]),
]
TREES[K] = [
 {'start': "A value looks abnormal in a pregnant woman", 'q': "Is it inside the PREGNANT normal range?", 'b': [
   {'a': "Yes", 'dx': "Physiology", 'c': "CO +45%, SVR −20%, Hb ~11, creatinine 0.4–0.8, PaCO₂ ~30, HCO₃ 18–22, fibrinogen 4–6"},
   {'a': "No, even if it is a 'normal adult' value", 'q': "Which one?", 'b': [
     {'a': "PaCO₂ 40", 'dx': "Tiring", 'c': "asthma, pneumonia"},
     {'a': "Creatinine 1.0", 'dx': "Renal impairment", 'c': "pre-eclampsia, sepsis"},
     {'a': "Fibrinogen ≤2", 'dx': "DIC", 'c': "abruption, AFE, PPH"},
     {'a': "Diastolic murmur", 'dx': "Heart disease", 'c': "echo"}]}]},
 {'start': "Pregnant >20 weeks, hypotensive lying flat", 'q': "Left uterine displacement: BP back within a minute?", 'b': [
   {'a': "Yes", 'dx': "Aortocaval compression", 'c': "keep her displaced"},
   {'a': "No", 'dx': "Bleeding or sepsis", 'c': "look for it now"}]},
]

K = ('OBS01', 3)
CORE[K] = [
 "Her baseline has moved (lower BP, faster breathing), so **adult thresholds miss her**.",
 "**MEOWS** is a colour-band chart: **1 red or 2 yellow** = urgent review; nothing is added up (unlike NEWS).",
 "MEOWS red triggers: RR **<10 or >30**, SBP **<90 or >180**, HR **<40 or >120**, temperature **<35 or >38**, responds to pain only.",
 "**Obstetric qSOFA** (sepsis screen): SBP **≤90**, RR **≥25**, anything other than alert.",
 "Standard qSOFA is SBP ≤100, RR ≥22, GCS <15: in pregnancy the **BP cut-off moves down and the RR cut-off moves up**.",
]
PAIRS[K] = [
 ("Obstetric qSOFA", "Standard qSOFA", ["Three bedside items", "Altered mentation in both"],
  [("Systolic BP", "**≤90**", "≤100"),
   ("!Resp rate", "**≥25**", "≥22"),
   ("Mentation", "Anything other than alert", "GCS <15")]),
 ("MEOWS", "NEWS", ["Bedside observation charts that trigger review"],
  [("!Method", "Colour bands: **1 red or 2 yellow**", "Points **added up** to a score"),
   ("Ranges", "Pregnant", "Non-pregnant")]),
 ("Obstetric qSOFA", "MEOWS", ["Both used on the obstetric ward"],
  [("!Purpose", "Screens for **sepsis** organ dysfunction", "Catches **any** deterioration"),
   ("Size", "3 items", "Full observation chart")]),
]

K = ('OBS01', 4)
CORE[K] = [
 "**The view is harder:** airway **oedema, mucosal engorgement, friable capillaries** (the GT answer), big breasts, weight → intubation **2.5–3×** harder.",
 "**The time is shorter:** **FRC −20%** (small store) + O₂ use **+30–40%** (fast drain) → she desaturates 'despite adequate pre-oxygenation'.",
 "**The stomach is full:** lax sphincter, slow transit → rapid sequence induction.",
 "Prepare: tube **6.5–7.0**, short-handled laryngoscope, ramped position, full pre-oxygenation.",
 "Plan (OAA/DAS): mask ventilation allowed at **<20 cmH₂O**; **2 attempts** at intubation (+1 by an expert); then declare failed intubation.",
 "Failed intubation → **oxygenate**: supraglottic airway (**max 2** attempts) or mask → then decide **proceed or wake**.",
 "Cannot oxygenate → **CICO**: 100% O₂, full paralysis, **front-of-neck access** through the cricothyroid membrane.",
]
PAIRS[K] = [
 ("Failed intubation", "Can't intubate, can't oxygenate", ["The tube will not pass"],
  [("!Oxygenation by SGA/mask", "**Works**", "**Fails**, saturation falling"),
   ("Next", "Supraglottic airway, then proceed or wake", "Front-of-neck access")]),
 ("Obstetric airway (OAA/DAS)", "General adult (DAS)", ["Same order: intubate → SGA → CICO"],
  [("!Intubation attempts", "**2 + 1** (expert)", "3 + 1"),
   ("SGA attempts", "**2**", "3")]),
 ("Difficulty from the airway", "Difficulty from time", ["Both make obstetric intubation dangerous"],
  [("Cause", "Oedema, friable mucosa, breasts", "Low FRC, high O₂ use"),
   ("!Answered by", "Equipment and position", "Pre-oxygenation and a limit on attempts")]),
]
TREES[K] = [
 {'start': "Obstetric GA: the tube will not pass", 'q': "Attempts used? (max 2, +1 by an expert)", 'b': [
   {'a': "Declare failed intubation", 'q': "Can you oxygenate by SGA (max 2) or mask?", 'b': [
     {'a': "Yes", 'dx': "Failed intubation", 'c': "decide: proceed with surgery or wake"},
     {'a': "No, SpO₂ falling", 'dx': "CICO", 'c': "100% O₂, full paralysis, front-of-neck access"}]}]},
]

K = ('OBS01', 5)
CORE[K] = [
 "Organ support is **the same as any adult**, with a few changes for the fetus.",
 "Ventilation: Vt **6 mL/kg PBW**, plateau **<30**; SpO₂ **≥95%** (PaO₂ **>70**) because the fetus sits on the steep part of its curve.",
 "**No permissive hypercapnia**: keep PaCO₂ near **30–32**, since maternal CO₂ acidifies the fetus. Prone is allowed; refractory → **VV-ECMO**; delivery may help the mother.",
 "Circulation: two large-bore cannulae, lines **above the diaphragm** (avoid femoral), uterus displaced; shock gets **noradrenaline** as in any adult.",
 "Fetal lung: **betamethasone 12 mg IM × 2, 24 h apart** (before 34 weeks).",
 "Imaging is never withheld: chest X-ray **<0.1 mGy**, CTPA **0.01–0.66 mGy**, abdominal/pelvic CT **10–50 mGy**; no fetal harm expected below **50 mGy**.",
 "Asthma (top-up): treat exactly as outside pregnancy (SABA, ICS, steroids, IV Mg); hypoxia harms the fetus more than any drug.",
]
PAIRS[K] = [
 ("Pregnant ARDS", "Other ARDS", ["Vt 6 mL/kg PBW", "Plateau <30"],
  [("!SpO₂ target", "**≥95%** (PaO₂ >70)", "88–95%"),
   ("CO₂", "**Avoid** permissive hypercapnia", "Permissive hypercapnia accepted")]),
 ("Spinal hypotension at caesarean", "Shock in a pregnant ICU patient", ["Pregnant and hypotensive"],
  [("!Vasopressor", "**Phenylephrine**", "**Noradrenaline**"),
   ("Cause", "Sympathetic block", "Sepsis, bleeding, heart")]),
 ("Betamethasone", "Beclomethasone", ["Both are steroids"],
  [("Crosses placenta active?", "Yes (also dexamethasone)", "No (inhaled)"),
   ("!Use", "**Fetal lung maturity**", "Asthma control")]),
 ("CT pulmonary angiogram", "V/Q scan", ["Both low fetal dose"],
  [("Mother's breast dose", "Higher", "Lower"),
   ("!Choose when", "Chest film abnormal or unstable", "Chest film normal")]),
]

K = ('OBS02A', 1)
CORE[K] = [
 "Hypertension = **≥140/90 on two readings 4 h apart**.",
 "Found **before 20 weeks** (or still there **>12 weeks** after delivery) → **chronic**.",
 "New **after 20 weeks**, no proteinuria, no organ dysfunction → **gestational**.",
 "After 20 weeks + proteinuria **≥300 mg/24 h** OR any organ feature → **pre-eclampsia**. Organ features: platelets **<100,000**, creatinine **>1.1** or doubled, transaminases **×2**, pulmonary oedema, cerebral or visual symptoms. **Proteinuria is no longer required.**",
 "Chronic hypertension that gains proteinuria or severe features → **superimposed** pre-eclampsia.",
 "Severe = **≥160/110** or organ injury; the **amount** of proteinuria never grades severity.",
 "Pre-eclampsia + **seizure** → **eclampsia**.",
]
PAIRS[K] = [
 ("Pre-eclampsia", "Gestational hypertension", ["New hypertension after 20 weeks"],
  [("!Proteinuria or organ dysfunction", "**Present** (either one)", "**Neither**")]),
 ("Chronic hypertension", "Gestational hypertension", ["Hypertension in pregnancy, no proteinuria"],
  [("Onset", "**Before 20 weeks**", "After 20 weeks"),
   ("!12 weeks postpartum", "**Still there**", "**Gone**")]),
 ("Severe pre-eclampsia", "Eclampsia", ["May have BP ≥160/110", "Headache, visual symptoms"],
  [("!Seizure", "**No**", "**Yes**")]),
]
TREES[K] = [
 {'start': "Hypertension (≥140/90 twice) in pregnancy", 'q': "When did it start?", 'b': [
   {'a': "Before 20 weeks", 'q': "New proteinuria or severe features later?", 'b': [
     {'a': "No", 'dx': "Chronic", 'c': "persists >12 wk postpartum"},
     {'a': "Yes", 'dx': "Superimposed pre-eclampsia", 'c': ""}]},
   {'a': "After 20 weeks", 'q': "Proteinuria ≥300 mg or any organ feature?", 'b': [
     {'a': "No", 'dx': "Gestational", 'c': "gone by 12 wk"},
     {'a': "Yes", 'dx': "Pre-eclampsia", 'c': "≥160/110 or organ injury = severe; + seizure = eclampsia"}]}]},
]

K = ('OBS02A', 2)
CORE[K] = [
 "Shallow **trophoblast invasion** → the spiral arteries stay **narrow and muscular**.",
 "The under-perfused placenta becomes **ischaemic**.",
 "It releases **sFlt-1 and soluble endoglin**, which are anti-angiogenic.",
 "These cause systemic **endothelial dysfunction**, the root of every sign.",
 "Kidney: **glomerular endotheliosis** → proteinuria. Liver: microcirculatory failure → HELLP. Brain: oedema → headache, PRES, stroke. Vessels: **high SVR**, angiotensin-sensitive, contracted plasma volume.",
 "Risk: primigravida, diabetes, chronic hypertension, BMI **>30**, cardiovascular disease. Prevention: **low-dose aspirin**, calcium.",
]
PAIRS[K] = [
 ("Normal pregnancy", "Pre-eclampsia", ["Pregnant circulation"],
  [("!SVR", "**Low**", "**High**"),
   ("Plasma volume", "Expanded", "**Contracted** (leaky)"),
   ("Angiotensin II", "Resistant", "Sensitive"),
   ("GFR", "High", "Reduced")]),
]

K = ('OBS02A', 3)
CORE[K] = [
 "The only cure is **delivery**. Until then there are two separate jobs: the **antihypertensive prevents stroke**, **magnesium prevents seizures**.",
 "Treat **≥160/110** within 30–60 min: **IV labetalol** 10–20 mg, then 20–80 mg every 10–30 min (max **300 mg**).",
 "Asthma, bradycardia or heart block → **hydralazine** 5 mg IV, or **oral nifedipine** 10–20 mg. No ACE inhibitors/ARBs; avoid atenolol; nitroprusside last.",
 "Fluid: she is volume-depleted but leaky → **≤80 mL/h**, no diuretics unless pulmonary oedema; oliguria is watched, not challenged.",
 "Deliver **now** at any gestation for eclampsia, pulmonary oedema, DIC, renal failure, abruption, non-reassuring fetus; deliver at **≥34 weeks**.",
 "33 weeks, stable HELLP, FGR <5th centile, reversed end-diastolic flow, PPROM → **steroids, deliver after 48 h**. 24–33+6 weeks and stable → **expectant**.",
 "Non-severe disease (top-up): **CHIPS** → treat to diastolic **85**; **HYPITAT** → deliver at **37 weeks**.",
 "GDM after delivery (top-up): **stop insulin** (placental hormones gone); OGTT at **6–12 weeks**.",
]
PAIRS[K] = [
 ("Antihypertensive", "Magnesium", ["Both started in severe pre-eclampsia"],
  [("!Job", "Prevents **stroke**", "Prevents **seizures**"),
   ("Lowers BP?", "Yes", "Not usefully")]),
 ("Oliguria of pre-eclampsia", "Hypovolaemic oliguria", ["Low urine output"],
  [("Cause", "Renal vasospasm, leak", "Blood loss, sepsis"),
   ("!Fluid challenge", "**No**: watch it", "**Yes**: give volume")]),
 ("Pulmonary oedema of pre-eclampsia", "Peripartum cardiomyopathy", ["Breathless, crackles, peripartum"],
  [("BP", "**Severely high**", "Normal or low"),
   ("!Ejection fraction", "Preserved", "**<45%**"),
   ("Treatment", "Furosemide, vasodilator, deliver", "Heart-failure therapy")]),
 ("Absent end-diastolic flow", "Reversed end-diastolic flow", ["High placental resistance with growth restriction"],
  [("!Deliver at", "~33–34 weeks", "~**30–32** weeks (worse)")]),
]
TREES[K] = [
 {'start': "Severe pre-eclampsia: when to deliver?", 'q': "Is anything failing?", 'b': [
   {'a': "Eclampsia, pulmonary oedema, DIC, renal failure, abruption, bad CTG", 'dx': "Deliver now", 'c': "any gestation"},
   {'a': "Nothing failing", 'q': "Gestation?", 'b': [
     {'a': "≥34 wk (or <24)", 'dx': "Deliver", 'c': ""},
     {'a': "33 wk, HELLP, FGR, REDF, PPROM", 'dx': "Steroids → deliver at 48 h", 'c': ""},
     {'a': "24–32+6 wk", 'dx': "Steroids, expectant", 'c': "deliver by 33+6"}]}]},
]

K = ('OBS02A', 4)
CORE[K] = [
 "A seizure in pregnancy is **eclampsia until proven otherwise**; **20%** had no prior pre-eclampsia. Antepartum **53%**, intrapartum 19%, postpartum **28%**.",
 "The fit lasts **60–90 s**; fetal bradycardia usually recovers, so stabilise the mother first.",
 "Airway, left lateral, prevent injury, then **MgSO₄ 4–6 g IV over 15–20 min**, then **1–2 g/h** until **24 h** after delivery or the last fit.",
 "Another fit on magnesium → **2 g more** magnesium, not a benzodiazepine first.",
 "Toxicity ladder (mg/dL): therapeutic **5–9** → **>9 knee jerk lost** → **>12 breathing stops** → **>30 cardiac arrest**. Antidote: **calcium gluconate 1 g IV**.",
 "Bedside monitoring: knee jerk, RR, urine output. Renal impairment: same load, **lower maintenance**.",
 "How it works: cerebral vasodilatation, NMDA block, less ACh release (so it **potentiates NMBs**). It is **not an antihypertensive**.",
 "Evidence: **Magpie** (~10,000, prevention): eclampsia **−58%**. **Collaborative Eclampsia Trial** (treatment): magnesium beat diazepam and phenytoin.",
]
PAIRS[K] = [
 ("Eclampsia", "Magnesium toxicity", ["On the labour ward, often on a Mg infusion", "Collapse or altered consciousness"],
  [("!Reflexes", "**Brisk**, clonus", "**Absent**, flaccid"),
   ("Breathing", "Post-ictal", "Slow, shallow"),
   ("Urine", "Variable", "Often oliguric"),
   ("Do", "Give 2 g more Mg", "Stop Mg, **calcium gluconate**")]),
 ("Eclampsia", "Epilepsy", ["Seizure in pregnancy"],
  [("BP / proteinuria", "Raised", "Normal"),
   ("History", "No seizures before", "Known epilepsy, missed drugs"),
   ("!If unsure", "**Treat as eclampsia**", "")]),
 ("Magpie (2002)", "Collaborative Eclampsia Trial (1995)", ["Both proved magnesium"],
  [("!Question", "**Prevention** in pre-eclampsia", "**Treatment** after a fit"),
   ("Comparator", "Placebo", "Diazepam, phenytoin"),
   ("Result", "Eclampsia −58%", "Recurrent fits roughly halved")]),
 ("Magnesium", "Benzodiazepine", ["Anticonvulsant in eclampsia"],
  [("!Role", "**First line**, prevents recurrence", "Only if fits continue despite Mg"),
   ("Sedation", "None", "Sedates mother and baby")]),
]
TREES[K] = [
 {'start': "Pregnant woman: seizure or slow breathing on the ward", 'q': "Check the knee jerk", 'b': [
   {'a': "Brisk, clonus, BP high", 'dx': "Eclampsia", 'c': "Mg 4–6 g (2 g more if already on it)"},
   {'a': "Absent, flaccid, slow RR, oliguria", 'dx': "Magnesium toxicity", 'c': "stop Mg, calcium gluconate 1 g"},
   {'a': "Normal BP and urine, known epilepsy", 'dx': "Epilepsy", 'c': "still treat as eclampsia if unsure"}]},
]

K = ('OBS02A', 5)
CORE[K] = [
 "Most eclamptic MRIs show **PRES**: bilateral, symmetric **parieto-occipital** vasogenic oedema, **no restricted diffusion**, reverses in days to weeks.",
 "Image when the fit does not fit eclampsia: **focal** signs, prolonged or not waking, **before 20 weeks**, late postpartum, or fits despite magnesium.",
 "Differentials: **cerebral venous thrombosis** (puerperium; headache, focal signs, haemorrhagic venous infarcts, **empty-delta** sign), haemorrhage, infarct, meningitis/encephalitis, tumour or trophoblastic disease, drugs or withdrawal.",
 "The seizure itself is managed the same: airway, prevent injury, **magnesium**, avoid polypharmacy, then the delivery plan.",
 "Naming: **PRES** is the imaging diagnosis (the answer when an MRI is shown); 'hypertensive encephalopathy' is the clinical syndrome.",
]
PAIRS[K] = [
 ("PRES", "Acute infarct", ["Seizure or deficit, bright lesion on MRI"],
  [("Distribution", "Bilateral, symmetric, **posterior**", "One arterial territory"),
   ("!Diffusion", "**No restriction**", "**Restricted**"),
   ("Course", "Reverses", "Permanent")]),
 ("PRES", "Cerebral venous thrombosis", ["Postpartum headache and seizures"],
  [("Pattern", "Symmetric oedema", "Asymmetric, **haemorrhagic** infarcts"),
   ("!Key sign", "Posterior oedema", "**Empty-delta** sign, clot on venography"),
   ("Treat", "BP control + Mg", "**Anticoagulate**")]),
 ("PRES", "Hypertensive encephalopathy", ["Same patient"],
  [("!What it names", "The **imaging** diagnosis", "The **clinical** syndrome")]),
]
TREES[K] = [
 {'start': "Seizure in pregnancy that doesn't fit plain eclampsia → MRI", 'q': "What does the MRI show?", 'b': [
   {'a': "Bilateral posterior oedema, no restriction", 'dx': "PRES", 'c': "BP + Mg"},
   {'a': "Restriction in one arterial territory", 'dx': "Infarct", 'c': ""},
   {'a': "Venous infarct, empty delta", 'dx': "CVT", 'c': "anticoagulate"},
   {'a': "Blood / fever + CSF", 'dx': "Haemorrhage / infection", 'c': ""}]},
]

K = ('OBS02A', 6)
CORE[K] = [
 "**HELLP** is the endothelial disease in the liver and blood: **haemolysis** (schistocytes, LDH **≥600**), **AST >70**, **platelets <100,000** (Tennessee).",
 "It occurs in **20%** of pre-eclamptics; RUQ/epigastric pain is a **stretched liver capsule** → risk of **subcapsular haematoma** and rupture.",
 "In HELLP the liver **still works**: glucose and INR normal until DIC.",
 "**Acute fatty liver**: third trimester, **microvesicular** fat, true **liver failure**: **hypoglycaemia**, high **INR and ammonia**, encephalopathy; platelets normal until DIC; linked to fetal **LCHAD** deficiency.",
 "Both are treated by **delivery** (+ steroids for the fetal lung). Plasma exchange is only **category III** for HELLP.",
 "Still worsening **>72 h after delivery** → think **TTP/aHUS** (ADAMTS13 **<10%**) → plasma exchange.",
]
PAIRS[K] = [
 ("HELLP", "Acute fatty liver", ["Third trimester", "RUQ pain, raised enzymes", "Treated by delivery"],
  [("!Glucose", "Normal", "**Low**"),
   ("INR / ammonia", "Normal (until DIC)", "**High**: true liver failure"),
   ("Platelets", "**Low early**", "Normal until DIC"),
   ("Haemolysis", "**Yes**", "No"),
   ("Encephalopathy", "No", "**Yes**")]),
 ("HELLP", "TTP", ["Schistocytes", "Low platelets"],
  [("Transaminases", "Raised", "Near-normal"),
   ("Neuro signs, fever", "No", "Yes"),
   ("!After delivery", "**Improves within 72 h**", "**Does not improve**"),
   ("ADAMTS13", "Normal", "**<10%**")]),
 ("HELLP", "DIC", ["Low platelets"],
  [("!PT, APTT, fibrinogen", "**Normal** early", "**Abnormal**")]),
 ("Acute fatty liver", "Hepatitis E", ["Jaundice, liver failure in pregnancy"],
  [("Trimester", "Third", "Any"),
   ("Transaminases", "Up to ~1,000", "Thousands"),
   ("!Delivery", "**Cures it**", "Does not")]),
]
TREES[K] = [
 {'start': "Third trimester, RUQ pain, raised enzymes", 'q': "Is the liver working? (glucose, INR, ammonia)", 'b': [
   {'a': "Yes: normal", 'q': "Haemolysis + low platelets?", 'b': [
     {'a': "Yes", 'dx': "HELLP", 'c': "deliver"},
     {'a': "+ shoulder pain, shock", 'dx': "Subcapsular haematoma", 'c': "image now"},
     {'a': "Worse >72 h after delivery", 'dx': "TTP / aHUS", 'c': "ADAMTS13, plasma exchange"}]},
   {'a': "No: low glucose, high INR & ammonia", 'dx': "Acute fatty liver", 'c': "deliver"}]},
]

K = ('OBS02B', 1)
CORE[K] = [
 "**Abruption:** painful bleeding, **woody tender uterus**, dark and often **concealed** blood, shock **out of proportion**, **low fibrinogen**; ultrasound is **often normal**.",
 "**Placenta praevia:** **painless bright red** bleeding, soft uterus, previous section; ultrasound diagnostic; no vaginal exam before the scan.",
 "**Uterine rupture:** scarred uterus in labour, sudden pain then **contractions stop**, fetal parts palpable, FAST positive.",
 "**Vasa praevia:** bleeding at membrane rupture; the blood is **fetal**, so the fetus is bradycardic while the mother is stable.",
 "Abruption drives DIC: pregnant fibrinogen is 4–6, so **<2 g/L is danger**.",
 "GT trap: 'no vaginal bleeding, ultrasound negative' with a tender uterus = **concealed abruption**.",
]
PAIRS[K] = [
 ("Abruption", "Placenta praevia", ["Antepartum haemorrhage, third trimester"],
  [("!Pain", "**Painful**, woody uterus", "**Painless**, soft uterus"),
   ("Blood", "Dark, may be concealed", "Bright red, visible"),
   ("Shock", "Out of proportion", "Matches visible loss"),
   ("Ultrasound", "**Often normal**", "Diagnostic"),
   ("Fibrinogen", "Low", "Normal")]),
 ("Abruption", "Uterine rupture", ["Pain and shock in late pregnancy"],
  [("!Contractions", "Uterus hard, **still contracting**", "**Stop**"),
   ("Scar", "No", "Previous scar"),
   ("FAST", "Negative", "Positive"),
   ("Fetal parts", "Not felt", "Palpable")]),
 ("Placenta praevia", "Vasa praevia", ["Painless bleeding from a low-lying source"],
  [("!Whose blood", "Mother's", "**Fetus's**"),
   ("When", "Any time", "At membrane rupture"),
   ("Who decompensates", "Mother", "Fetus (bradycardia)")]),
]
TREES[K] = [
 {'start': "Bleeding (or shock) before delivery", 'q': "Pain? Feel the uterus", 'b': [
   {'a': "Painful, woody, tender", 'dx': "Abruption", 'c': "scan often normal, low fibrinogen"},
   {'a': "Painless, soft", 'dx': "Placenta praevia", 'c': "scan diagnostic, no PV exam"},
   {'a': "Pain, then contractions stop, scarred uterus", 'dx': "Uterine rupture", 'c': "FAST positive"},
   {'a': "Bleeding at ROM, fetus bradycardic", 'dx': "Vasa praevia", 'c': "fetal blood"}]},
]

K = ('OBS02B', 2)
CORE[K] = [
 "PPH = **>500 mL** (massive **>1,000–1,500**); primary within 24 h, secondary 24 h to 6 weeks.",
 "Four Ts: **Tone** (atony, commonest), **Trauma**, **Tissue**, **Thrombin**.",
 "Prevent with **active management of the third stage**: oxytocin at delivery, controlled cord traction, massage.",
 "Ladder: resuscitate → **bimanual massage + oxytocin** (20 IU/L) → **TXA 1 g within 3 h** (WOMAN) → second uterotonic → blood and factors → **balloon tamponade** → B-Lynch, ligation, embolisation → **hysterectomy**.",
 "Second uterotonic by patient: **methylergonovine 0.2 mg IM** (not in hypertension/pre-eclampsia); **carboprost 0.25 mg IM** (not in asthma); **misoprostol 1,000 µg PR** (safe in both).",
 "Uterine inversion: **no fundus** felt, mass in the vagina, shock out of proportion → stop uterotonics, **replace at once**.",
 "Stable → embolisation; unstable → theatre. Accreta at caesarean → hysterectomy.",
]
PAIRS[K] = [
 ("Atony", "Uterine inversion", ["Shock right after delivery"],
  [("!Fundus", "Large, **soft**, above umbilicus", "**Not felt** abdominally"),
   ("Vagina", "Bleeding", "**Mass** filling it"),
   ("Do", "Massage, uterotonics", "**Stop** uterotonics, replace")]),
 ("Atony", "Genital tract tear", ["Bleeding after delivery"],
  [("!Uterus", "**Soft**, boggy", "**Firm**"),
   ("Bleeding", "Pooling, clots", "Steady, bright")]),
 ("Methylergonovine", "Carboprost", ["Second-line uterotonics"],
  [("Class", "Ergot", "PGF2α"),
   ("!Avoid in", "**Hypertension**, pre-eclampsia", "**Asthma**"),
   ("If both", "Misoprostol", "Misoprostol")]),
 ("Embolisation", "Laparotomy", ["Same ongoing PPH"],
  [("!Patient", "**Stable** enough for radiology", "**Unstable**")]),
]
TREES[K] = [
 {'start': "Postpartum haemorrhage", 'q': "Feel the uterus", 'b': [
   {'a': "Soft, boggy", 'q': "Second uterotonic: any contraindication?", 'b': [
     {'a': "Asthma", 'dx': "No carboprost", 'c': "ergot or misoprostol"},
     {'a': "Hypertension", 'dx': "No ergometrine", 'c': "carboprost or misoprostol"},
     {'a': "Both", 'dx': "Misoprostol", 'c': ""}]},
   {'a': "Firm", 'dx': "Trauma", 'c': "tear, haematoma"},
   {'a': "No fundus, vaginal mass", 'dx': "Inversion", 'c': "stop uterotonics, replace"},
   {'a': "Bulky, os open, day 2", 'dx': "Tissue", 'c': "retained products"},
   {'a': "Not clotting", 'dx': "Thrombin", 'c': "fibrinogen, plasma, platelets"}]},
]

K = ('OBS02B', 3)
CORE[K] = [
 "Blood volume **+45%**, so her BP holds until **1–1.5 L** has gone: tachycardia comes first.",
 "**Shock index** = HR ÷ SBP: pregnant normal **0.7–0.9**; **≥0.9–1.1** = significant loss; **>1.4–1.7** = urgent transfusion/MTP.",
 "Visual estimates are unreliable, and bleeding can be **concealed**.",
 "Normal pregnant fibrinogen is **4–6 g/L**, so **<2 g/L** is already dangerous → early fibrinogen, MTP. (GT-2 Q26: a fibrinogen of 130 mg/dL was the clue.)",
 "High risk on admission (AWHONN): praevia, suspected accreta, Hct **<30%**, platelets **<100,000**, active bleeding, coagulopathy, or **≥2 medium** factors → crossmatch 2 units, plan MTP.",
]
PAIRS[K] = [
 ("DIC", "HELLP", ["Low platelets"],
  [("!PT, APTT, fibrinogen", "**Abnormal**", "Normal until late"),
   ("Haemolysis, liver enzymes", "—", "**Yes**")]),
 ("DIC", "Acute fatty liver", ["Prolonged PT, low fibrinogen"],
  [("!Mechanism", "**Consumption**", "**Failed synthesis**"),
   ("Glucose, ammonia", "Normal", "Low glucose, high ammonia, jaundice first")]),
]

K = ('OBS02B', 4)
CORE[K] = [
 "**Amniotic fluid embolism:** in labour, at delivery or **within 30 min**: sudden **hypoxia → hypotension/arrest → seizures → DIC** (bleeding from IV sites).",
 "Incidence **2–6 per 100,000**; mortality **~20%** now (older series up to 85%).",
 "Mechanism (the exam answer): a **systemic inflammatory, anaphylactoid** response to fetal material; **not** mechanical, **not** IgE. Phase 1: pulmonary vasospasm, RV failure, hypoxia. Phase 2: LV failure, DIC.",
 "Diagnosis is clinical, by exclusion. Treat: multi-organ support, **massive transfusion + TXA**, RV support, emergency delivery; arrest → **resuscitative delivery by 5 min**; **VA-ECMO** as rescue.",
 "Sepsis sources specific to pregnancy: **chorioamnionitis**, **pyelonephritis** (progesterone dilates the ureters), **endometritis**, pneumonia.",
]
PAIRS[K] = [
 ("Amniotic fluid embolism", "Pulmonary embolism", ["Sudden hypoxia and hypotension", "Dilated RV on echo"],
  [("Timing", "Labour or **≤30 min** after", "Usually days postpartum"),
   ("!Early DIC, seizures", "**Yes**", "**No**"),
   ("Treat", "Support", "Anticoagulate or lyse")]),
 ("Amniotic fluid embolism", "Anaphylaxis", ["Mast-cell and complement mediators", "Collapse"],
  [("IgE", "No", "Yes"),
   ("!DIC", "**The rule**", "**Absent**"),
   ("Trigger", "Fetal material", "A drug; rash, wheeze")]),
 ("Chorioamnionitis", "Endometritis", ["Fever, tender uterus"],
  [("!When", "**Before** delivery", "**After** delivery"),
   ("Clue", "Fetal tachycardia", "Foul lochia")]),
]
TREES[K] = [
 {'start': "Sudden collapse in labour or just after delivery", 'q': "What came with it?", 'b': [
   {'a': "Hypoxia → seizure → bleeding from IV sites, ≤30 min", 'dx': "AFE", 'c': "echo: acute RV dilatation"},
   {'a': "Visible or concealed bleeding first", 'dx': "Haemorrhage", 'c': "PPH, abruption, rupture"},
   {'a': "Fever, source", 'dx': "Sepsis", 'c': "chorio, pyelo, endometritis"},
   {'a': "Breathless over days, EF <45%", 'dx': "PPCM", 'c': ""}]},
]

K = ('OBS02B', 5)
CORE[K] = [
 "**Peripartum cardiomyopathy:** heart failure from the **last month of pregnancy to 5 months postpartum**, no other cause, **EF <45%**; about 1 in 3,500.",
 "Before delivery: β-blocker, diuretic, **hydralazine + nitrates**, digoxin; **no ACE inhibitor/ARB** (allowed after delivery). Very low EF: bromocriptine and anticoagulation.",
 "Persistent LV dysfunction = poor prognosis; it **recurs**, so counsel on contraception.",
 "**Arrest:** standard ACLS (compressions, energy, drug doses **unchanged**) + continuous **manual left uterine displacement**, IV **above the diaphragm**, expert airway, 1 breath every 6 s.",
 "On magnesium? **Stop it, give calcium.** Detach fetal monitors, call the neonatal team.",
 "Fundus at or above the umbilicus → **resuscitative delivery by 5 min**, done for the mother. Causes A–H: Anaesthetic, Bleeding, Cardiovascular, Drugs, Embolic, Fever, General, Hypertension.",
]
PAIRS[K] = [
 ("Peripartum cardiomyopathy", "Pre-eclampsia with pulmonary oedema", ["Peripartum pulmonary oedema"],
  [("!Ejection fraction", "**<45%**", "Preserved"),
   ("BP", "Normal or low", "**High**")]),
 ("Peripartum cardiomyopathy", "Postpartum pulmonary embolism", ["Breathless after delivery"],
  [("Onset", "Over days, orthopnoea", "Sudden"),
   ("!Ventricle", "**LV** poor", "**RV** strain"),
   ("Lungs", "Crackles", "Clear")]),
 ("Vasopressor in arrest", "Vasopressor for spinal hypotension", ["Pregnant and hypotensive"],
  [("!Drug", "**Adrenaline**", "**Phenylephrine**")]),
]

K = ('OBS02B', 6)
CORE[K] = [
 "**OHSS:** gonadotropin/hCG drives a **capillary leak** → ascites, **haemoconcentration**, oliguria and clots.",
 "Grade by ascites and haematocrit: moderate = ascites on scan; severe = clinical ascites, Hct **>0.45**, oliguria; critical = tense ascites, Hct **>0.55**, anuria, thrombosis, ARDS.",
 "Treat: support, **paracentesis** for tense ascites, **DVT prophylaxis for all**, no diuretics while haemoconcentrated.",
 "**Reading the stem:** one planted phrase decides. 'No asthma' → carboprost or labetalol. 'BP still 176/114 after Mg' → now labetalol. 'No bleeding, USG negative, tender uterus' → concealed abruption. 'Hypoglycaemia with jaundice' → fatty liver. 'Despite pre-oxygenation' → low FRC, high O₂ use.",
]
PAIRS[K] = [
 ("OHSS", "Torsion or ruptured cyst", ["Pain and big ovaries after stimulation"],
  [("Pain", "Diffuse, bloating", "Sudden, one-sided"),
   ("!Haematocrit", "**Rises**", "**Falls** (if bleeding)")]),
 ("Oliguria of OHSS", "Oliguria of fluid overload", ["Low urine output"],
  [("!Haematocrit", "**High**", "Normal or low"),
   ("Treat", "Volume + paracentesis", "Diuretic")]),
 ("Severe OHSS", "Critical OHSS", ["Ascites, haemoconcentration"],
  [("Ascites", "Clinical", "Tense"),
   ("!Haematocrit", ">0.45", "**>0.55**"),
   ("Extras", "Oliguria", "Anuria, thrombosis, ARDS")]),
]
