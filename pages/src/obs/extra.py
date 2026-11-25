# Hand-written layer: gap-fill facts (from non-hit cards), decision trees, image slots, key-vs-guideline flags
# Keyed by (deck, step)

GAP = {
 ('OBS01',1): ["Obstetric patients are **1–4.5%** of ICU admissions; mortality **5–20%**; about **70%** of maternal deaths are preventable (OBS-01).",
               "Two kinds of illness: diseases of pregnancy itself (pre-eclampsia, HELLP, AFE, PPCM, AFLP, haemorrhage) and ordinary diseases made worse by it (ARDS, aspiration, PE, urosepsis, malaria, hepatitis E, CVT) (OBS-02)."],
 ('OBS01',2): ["**Respiratory (OBS-04):** tidal volume **+40%**, **FRC −20%**, vital capacity **unchanged**; driven by progesterone. Low FRC + high O₂ use = fast desaturation (GT-4 Q29).",
               "**Normal pregnant ABG (OBS-05):** pH **7.40–7.47**, PaCO₂ **about 30**, HCO₃ **18–22**: a compensated respiratory alkalosis. So a PaCO₂ of **40** in a breathless pregnant woman means she is tiring."],
 ('OBS01',3): ["**MEOWS (OBS-09) red triggers:** RR **<10 or >30**, SBP **>180 or <90**, HR **>120 or <40**, responds to pain only. One red or two yellow = call.",
               "**Obstetric qSOFA (OBS-10):** SBP **≤90**, RR **≥25**, anything other than alert (non-pregnant: SBP ≤100, RR ≥22). Thresholds shift because her normal BP is lower and her rate faster."],
 ('OBS01',5): ["**Radiation (OBS-14):** chest X-ray **<0.1 mGy**; CTPA **0.01–0.66 mGy**; abdominal/pelvic CT **10–50 mGy**; no fetal harm expected below **50 mGy**. Never withhold a needed scan."],
 ('OBS02A',4): ["**Magnesium regimen (OBS-23):** load **4–6 g IV over 15–20 min**, then **1–2 g/h**, until **24 h after delivery** or the last fit; target **2–3.5 mmol/L (4.8–8.4 mg/dL)**. Monitor knee jerk, RR, urine. A further fit on magnesium: another **2 g** bolus, not a benzodiazepine first. Cut the infusion in renal impairment."],
 ('OBS02B',3): ["**Why bleeding is under-estimated (OBS-34):** blood volume **+45%**, so 1–1.5 L goes before BP falls; visual estimates are unreliable; normal pregnant fibrinogen is **4–6 g/L**, so **<2 g/L** is already dangerous → early fibrinogen and MTP. The fibrinogen of 130 mg/dL in GT-2 Q26 was the planted clue."],
 ('OBS02B',5): ["**Peripartum cardiomyopathy (OBS-38):** heart failure in the **last month of pregnancy to 5 months postpartum**, no other cause, **EF <45%** (not 30%). Before delivery: beta-blocker, diuretic, **hydralazine + nitrates** (no ACE inhibitor/ARB); after delivery ACE inhibitors allowed; bromocriptine and anticoagulation if EF very low. Persistent LV dysfunction = poor prognosis; it recurs."],
 ('OBS02B',6): ["**OHSS (OBS-40/41):** gonadotropin-driven capillary leak → third-space loss with **haemoconcentration**. Moderate = ascites on scan; severe = clinical ascites, Hct **>0.45**; critical = tense ascites, Hct **>0.55**, anuria, clot, ARDS. Treat: support, paracentesis for tense ascites, **DVT prophylaxis for all**, no diuretics while haemoconcentrated."],
}

# Key-vs-guideline / corrected-figure flags shown inside the concept
FLAG = {
 ('OBS01',4): ["**NEET 2025 recall** keys emergency cricothyrotomy after two failed attempts with difficult mask ventilation. Guideline (OAA/DAS): difficult-but-possible ventilation → **supraglottic airway**; front of neck only when oxygenation fails (CICO). Pick the key if it is the only CICO-type option."],
 ('OBS01',5): ["**DocT GT** keys tidal volume **8–9 mL/kg** for ARDS in pregnancy (3% right). Correct practice: **6 mL/kg PBW**, plateau <30; the real pregnancy change is **no permissive hypercapnia** and SpO₂ **≥95%**.",
               "**Phenylephrine** is the bare answer to 'vasopressor of choice in pregnancy' (spinal hypotension at caesarean). In **septic shock**, noradrenaline first, as in any adult."],
 ('OBS02A',3): ["**'Magnesium first'** is DocT's key for BP 180/110 with pulmonary oedema. In practice magnesium, an antihypertensive and furosemide start together; diuretics are banned only for oedema **without** lung congestion."],
 ('OBS02B',4): ["Card figures corrected: AFE incidence **2–6 per 100,000** (old card 3.3), mortality **about 20%** now (old 15–85%); 'perimortem caesarean' is now **resuscitative delivery**, done by 5 min.",
                "**DocT** keys AFE pulmonary oedema as 'cardiogenic' while its own explanation says non-cardiogenic: it is **mixed** (early capillary leak, then phase-2 LV failure)."],
}

# Decision trees: node = (text, [children]); leaf text may carry the deciding clue
TREE = {
 ('OBS01',2): ("Pregnant woman with an 'abnormal-looking' value: physiology or disease?", [
   ("Is the value inside the pregnant normal range?", [
     ("Yes → physiology: CO +40–50%, SVR −20%, Hb ~10.5–11, creatinine 0.4–0.8, PaCO₂ ~30, HCO₃ 18–22, fibrinogen 4–6 g/L", []),
     ("No → disease, even if it is a 'normal adult' number", [
       ("PaCO₂ 40 → **tiring** (asthma, pneumonia)", []),
       ("Creatinine 1.0 → **renal impairment** (pre-eclampsia, sepsis)", []),
       ("Fibrinogen 2 g/L → **consumptive coagulopathy** (abruption, AFE, PPH)", []),
       ("Diastolic murmur / fixed split S2 → **pathological** (MS, ASD): echo", [])])]),
   ("Hypotension when lying flat after 20 weeks?", [
     ("Recovers within a minute of **left uterine displacement** → aortocaval compression", []),
     ("Does not recover → **bleeding or sepsis**: look for it", [])])]),
 ('OBS01',4): ("Tube will not pass at obstetric GA", [
   ("Attempts used: max **2** (+1 by expert)", []),
   ("Can you oxygenate?", [
     ("Yes, by SGA (max 2 attempts) or mask → **failed intubation**: decide **proceed or wake**", []),
     ("No, saturation falling → **CICO**: 100% O₂, full paralysis, **front-of-neck access**", [])])]),
 ('OBS02A',1): ("Hypertension in pregnancy: which disorder?", [
   ("Present before pregnancy / **before 20 weeks** / beyond 12 weeks postpartum → **chronic**", [
     ("+ new proteinuria or severe features after 20 weeks → **superimposed pre-eclampsia**", []),
     ("Family history, obesity, no secondary clue → **essential**", [])]),
   ("New **after 20 weeks**", [
     ("No proteinuria, no organ dysfunction → **gestational hypertension**", []),
     ("Proteinuria ≥300 mg/day **or** any organ feature → **pre-eclampsia**", [
       ("BP ≥160/110 or organ injury → **severe** (the amount of proteinuria does not grade severity)", []),
       ("+ seizure → **eclampsia** (headache, hyperreflexia, visual change alone = still severe pre-eclampsia)", [])])])]),
 ('OBS02A',3): ("Severe pre-eclampsia: when to deliver?", [
   ("Eclampsia, pulmonary oedema, DIC, renal failure, abruption, non-reassuring fetus → **deliver now**, any gestation", []),
   ("**≥34 weeks** (or <24 weeks) → **deliver**", []),
   ("33 weeks, stable HELLP, FGR <5th centile, reversed EDF, PPROM → **steroids, deliver after 48 h**", []),
   ("24–32+6 weeks, stable → **steroids, expectant**, deliver by 33+6", [])]),
 ('OBS02A',4): ("Pregnant woman: seizure or respiratory depression on the ward", [
   ("Reflexes?", [
     ("**Brisk**, hyperreflexia/clonus → **eclampsia**: magnesium (2 g more if already on it)", []),
     ("**Absent**, flaccid, slow breathing, oliguria → **magnesium toxicity**: stop, **calcium gluconate 1 g**", [])]),
   ("Known epilepsy, missed drugs, normal BP and urine → **epilepsy** (still treat as eclampsia if unsure)", [])]),
 ('OBS02A',5): ("Seizure in pregnancy that doesn't fit plain eclampsia (focal, prolonged, not waking, <20 weeks, late postpartum) → MRI", [
   ("Bilateral symmetric **parieto-occipital** T2/FLAIR, **no** diffusion restriction → **PRES**", []),
   ("Restricted diffusion in **one arterial territory** → **infarct**", []),
   ("Venous infarct, haemorrhage, **empty-delta** sign → **CVT**", []),
   ("Blood → **intracranial haemorrhage**; fever + CSF → **meningitis/encephalitis**", [])]),
 ('OBS02A',6): ("Third trimester, RUQ pain, raised enzymes", [
   ("Liver **working**? (glucose, INR, ammonia normal)", [
     ("Yes + haemolysis + **early low platelets** + hypertension → **HELLP**", [
       ("Severe RUQ/shoulder-tip pain, AST in hundreds → **subcapsular haematoma**: image now", []),
       ("Still worsening **>72 h after delivery**, neuro signs, ADAMTS13 <10% → **TTP/aHUS**: plasma exchange", [])])]),
   ("Liver **failing**: **low glucose, high INR and ammonia**, encephalopathy, platelets normal until DIC → **acute fatty liver**", [])]),
 ('OBS02B',1): ("Bleeding (or shock) before delivery", [
   ("**Painful**, hard tender ('woody') uterus, shock out of proportion, low fibrinogen → **abruption** (scan often normal; bleeding may be concealed)", []),
   ("**Painless**, bright red, soft uterus, previous section → **placenta praevia** (scan diagnostic; no PV exam first)", []),
   ("Sudden pain, **contractions stop**, fetal parts palpable, scarred uterus in labour → **uterine rupture**", [])]),
 ('OBS02B',2): ("Postpartum haemorrhage: feel the uterus first", [
   ("**Soft, boggy** → **tone** (atony, commonest): massage, oxytocin, second uterotonic", [
     ("Asthmatic → **no carboprost**", []),
     ("Hypertensive / pre-eclampsia → **no ergometrine**", []),
     ("Both → **misoprostol** (safe in either)", [])]),
   ("**Firm** uterus, still bleeding → **trauma**: tear, haematoma", []),
   ("**No fundus**, vaginal mass, shock out of proportion → **inversion**: stop uterotonics, replace at once", []),
   ("Bulky uterus, open os, day 2 → **tissue** (retained products: mass with Doppler flow)", []),
   ("Blood not clotting → **thrombin**: fibrinogen, plasma, platelets", [])]),
 ('OBS02B',4): ("Sudden collapse in labour or just after delivery", [
   ("Hypoxia + hypotension/arrest → seizure → **DIC, bleeding from IV sites**, within 30 min of placenta, no fever → **amniotic fluid embolism** (echo: acute RV dilatation)", []),
   ("Visible or concealed bleeding first, then shock → **haemorrhage** (PPH, abruption, rupture)", []),
   ("Fever, tachycardia, source (chorioamnionitis, pyelonephritis, endometritis) → **sepsis**", []),
   ("Slow onset breathlessness, EF <45%, late pregnancy to 5 months postpartum → **PPCM**", [])]),
}

# Image slots: (deck, step) -> list of (id, title, prompt, checklist)
IMG = {
 ('OBS01',2): [("IMG-01","Aortocaval compression: supine vs left uterine displacement",
   "Medical illustration, clean flat vector style, white background, NO TEXT OR LABELS. Two side-by-side cross-sections of a woman at 30 weeks of pregnancy lying on her back, viewed from the feet looking up. Left panel: the gravid uterus resting directly on the spine, flattening the inferior vena cava (blue, on the patient's right) and partly compressing the aorta (red, on the patient's left). Right panel: a hand pushing the uterus up and to the patient's left, so the inferior vena cava is round and open again and the aorta is free. Anatomically correct sides.",
   "IVC is on the patient's RIGHT, aorta on the LEFT · uterus shifted to the patient's LEFT in panel 2 · no text in the image")],
 ('OBS02A',2): [("IMG-02","Spiral arteries: normal remodelling vs pre-eclampsia",
   "Medical illustration, clean vector style, white background, NO TEXT OR LABELS. Two side-by-side panels showing the placental bed. Left: normal pregnancy, trophoblast cells invading deep into the uterine wall and converting the spiral arteries into wide, funnel-shaped, low-resistance vessels delivering slow, abundant blood to the placenta. Right: pre-eclampsia, shallow trophoblast invasion, spiral arteries stay narrow and muscular, thin jets of blood, a pale, ischaemic placenta releasing small particles into the mother's blood.",
   "Left vessels wide and funnel-shaped · right vessels narrow and coiled · invasion depth clearly deeper on the left · no text")],
 ('OBS02A',5): [("IMG-03","PRES on MRI",
   "Do NOT generate this with AI. Use a real case: radiopaedia.org → search 'posterior reversible encephalopathy syndrome' → pick an axial FLAIR showing bilateral, symmetric parieto-occipital white-matter hyperintensity. Save the image (note the case author for credit).",
   "Real scan, axial FLAIR · bilateral and symmetric · posterior (parieto-occipital) · subcortical white matter")],
 ('OBS02B',1): [("IMG-04","Abruption vs praevia vs rupture",
   "Medical illustration, clean vector style, white background, NO TEXT OR LABELS. Three side-by-side sagittal cross-sections of a pregnant uterus at term. Panel 1: placenta on the upper uterine wall partly separated, with a dark red blood clot trapped behind it (concealed bleeding), no blood at the cervix. Panel 2: placenta lying low, covering the internal cervical os, bright red blood trickling through the cervix. Panel 3: a torn lower uterine segment at an old scar, the fetus partly outside the uterus in the abdominal cavity.",
   "Panel 1 clot BEHIND the placenta, cervix dry · Panel 2 placenta OVER the os · Panel 3 tear at the lower segment, fetus partly out · no text")],
 ('OBS02B',2): [("IMG-05","Uterine inversion",
   "Medical illustration, clean vector style, white background, NO TEXT OR LABELS. Two sagittal cross-sections of the postpartum pelvis. Left: normal involuting uterus, fundus palpable above the pubic bone. Right: complete uterine inversion, the fundus turned inside-out and pushed down through the cervix into the vagina, appearing as a red mass at the introitus, with an empty space where the fundus should be in the abdomen.",
   "Fundus missing from the abdomen in panel 2 · inverted fundus visible in the vagina · no text"),
  ("IMG-06","Placenta accreta spectrum on ultrasound",
   "Prefer a real image: radiopaedia.org → search 'placenta accreta ultrasound' → choose one showing placental lacunae and loss of the retroplacental clear zone, ideally with bladder-line interruption. If you must generate: grayscale obstetric ultrasound style, NO TEXT, low anterior placenta with multiple irregular dark vascular lacunae, absent hypoechoic clear zone between placenta and myometrium, irregular bladder wall.",
   "Lacunae (dark irregular spaces) · no clear zone behind the placenta · bladder line interrupted · prefer real")],
}

TOPUP_STEP = {'Asthma in pregnancy':5, 'CHIPS and HYPITAT':3, 'Gestational diabetes after delivery':3, 'PPH risk and the shock index':3, 'Heart disease in pregnancy':5}
