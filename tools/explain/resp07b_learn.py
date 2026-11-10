# RESP07B — Explain v3 ("Learn" depth): the pleura, part 2 — what an effusion does, finding it (film, ultrasound, CT), Light’s criteria and causes, pleural fluid chemistry and cells,
# parapneumonic effusion and pleural infection, malignant effusion, haemothorax and urgent thoracotomy, re-expansion pulmonary oedema. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP07B.md (19 questions; PLEU-17 Light’s criteria and PLEU-19 fluid chemistry asked 5 times each, PLEU-16 and PLEU-26 twice). Fields as TOX01, plus SPINE, PRIMER and step.
# Continues RESP07A (pneumothorax), whose story ended with draining the pleural space. Cards with no linked question get short explanations with [pattern] decode items.
# Figures checked online on 11 Nov 2026: Light’s criteria identify ~98% of exudates but label ~25% of transudates as exudates (Porcel, Curr Opin Pulm Med 2013); albumin gradient >1.2 g/dL
# reclassifies 83% of mislabelled cardiac effusions, protein gradient >3.1 g/dL 55%; BTS 2023 pleural infection pH ≤7.2 drain, >7.2 to <7.4 measure LDH and consider a drain if >900 IU/L
# (supporting: glucose ≤4.0 mmol/L, septation, contrast enhancement, large volume), pH ≥7.4 no drain, glucose <3.3 mmol/L if pH unavailable; small-bore (≤14 F) initial drain; VATS over thoracotomy;
# tPA 10 mg + DNase 5 mg twice daily for 3 days, single agents and streptokinase not recommended; antibiotics “2 to 6 weeks”, optimal length unknown; RAPID (PILOT, 542 patients: 3-month
# mortality 2.3% / 9.2% / 29.3% for scores 0–2 / 3–4 / 5–7); MIST2 (Rahman NEJM 2011: 210 patients, opacity −29.5% vs −17.2%, surgical referral 4% vs 16%, DNase alone 39%, stay 11.8 vs 24.8 days);
# ADA in India (meta-analysis of 40 studies, 3,524 patients: sensitivity 94%, specificity 89% at about 40 IU/L), BTS 2023 ADA advice by prevalence; BTS 2023 MPE (IPC or talc first-line by choice,
# IPC if >25% non-expandable, slurry or poudrage); TAPPS (330 patients, failure 24% vs 22% at 90 days); TIME2 (106 patients, breathlessness equal at 42 days, stay 0 vs 4 days, repeat procedures 6% vs 22%,
# more adverse events with IPC); AMPLE (146 patients, hospital days 10 vs 12, effusion-related 1 vs 4); haemothorax thoracotomy at >1500 mL initially or >200 mL/h for 2–4 h, tube 28–32 F;
# EAST: VATS for retained haemothorax within 3–7 days, >1500 mL in 24 h prompts exploration; Feller-Kopman 2007 (185 patients, clinical REPO 0.5%, radiographic 2.2%, unrelated to volume or pressure);
# Lentz 2019 (Lancet Respir Med, 128 patients: manometry did not change chest discomfort; pneumothorax ex vacuo 10% vs 0); BTS clinical statement: ~1.5 L per attempt, stop for chest tightness,
# pain, persistent cough or worsening breathlessness, symptomatic REPO <1%; Mahfood series REPO mortality ~20%; Balik formula 20 × distance (mm), supine 15°, end-expiration; ultrasound reliably
# detects >20 mL; PA film ~200 mL, lateral ~50 mL.
# Second check (11 Nov 2026, see resp07b_review.md): Krell & Rodarte 1985 and Dechman 1994 (dogs: lung takes ~1/3 of the fluid at both FRC and TLC); PLEASE study (Muruganandan 2020);
# Blackmore 1996 (meniscus ~50 mL lateral, ~200 mL PA, ~500 mL hides the diaphragm); Yang 1992 patterns; Leung CT criteria; Balik 2006; Bielsa 2012; Indian ADA meta-analysis (40 studies, 3,524 patients);
# eosinophilic effusion series (malignancy the commonest single cause); MIST1 (454 patients); Akulian 2022 bleeding (4.1%, 9.6% on anticoagulation); TAPPS, TIME2, AMPLE, Feller-Kopman 2007,
# Lentz 2019, Mahfood 1988 (11 of 53 fatal), EAST 2011 retained haemothorax, MSD/ATLS thoracotomy thresholds and 28–32 F tube. Still from standard teaching only: retained clot >1/3, drain removal volumes.

SPINE = [
  ("Fluid that squeezes lung and heart", "An effusion is housed mostly by the chest wall expanding, so breathlessness comes more from a flattened diaphragm than from lost lung, and a large one can compress the heart like tamponade."),
  ("Finding the fluid", "Fluid falls to the posterior costophrenic sulcus first, so the lateral film sees less than the PA film, the supine film sees least, and ultrasound detects the smallest volumes and shows whether the fluid is free, septated or echogenic."),
  ("Transudate or exudate", "Light’s criteria call an effusion an exudate if any one of three protein and LDH tests is positive, which catches nearly every exudate but mislabels a quarter of transudates, mostly heart failure after diuretics."),
  ("Reading the fluid", "Once it is an exudate, glucose, pH, LDH, lipids, amylase, ADA and the dominant cell point to the cause: low pH and glucose to infection, rheumatoid or cancer, triglyceride to chyle, ADA and lymphocytes to tuberculosis."),
  ("Infection and cancer in the space", "An infected effusion with pH ≤7.2 or pus needs a drain, then tPA with DNase or VATS if it will not clear, while a malignant effusion is palliated by a talc pleurodesis or an indwelling catheter."),
  ("Blood, and draining safely", "A haemothorax is pleural fluid with half the blood haematocrit, it goes to theatre for 1.5 L at once or 200 mL/h for 2–4 h, and every large drainage is stopped when the patient feels chest tightness."),
]

PRIMER = "RESP07A dealt with air in the pleural space; this deck deals with fluid. Pleural fluid is filtered from the systemic capillaries of the parietal pleura and leaves through lymphatic stomata, and those lymphatics can raise their flow many times before fluid builds up, so an effusion means either filtration that overwhelms them or lymphatics that are blocked. When the capillaries are normal and only the pressures are wrong (high hydrostatic pressure in heart failure, low oncotic pressure in hypoalbuminaemia) the fluid is a low-protein transudate; when the pleura itself is inflamed or invaded, protein and cells leak through and the fluid is an exudate. Normal pleural fluid is alkaline (pH about 7.6), low in protein and rich in macrophages, so every value in this deck is read against that baseline."

L = {}

L['PLEU-14'] = dict(
  sub="Respiratory → Pleura → Physiological effects of an effusion",
  step=1,
  intro="Step 1 asks what an effusion does to the patient before asking what caused it. The surprise is that the lung loses much less volume than the fluid takes up, because the chest wall moves out to make room, so the breathlessness has to be explained by something else.",
  parts=[
    ('a', "**Chest-wall expansion accommodates most of the fluid; lung volume falls by only one-third of the fluid volume at FRC and one-fifth at TLC.** The chest wall springs outward at FRC, so adding fluid pushes it further out rather than squeezing the lung. In the dog experiments behind these figures (Krell and Rodarte 1985; Dechman 1994) the lung gave up about one-third of the added volume and the chest wall expanded by about two-thirds, at TLC as well as at FRC. A litre of fluid therefore costs the lung only a few hundred millilitres, which is why gas exchange is often only modestly impaired by a large effusion and changes little after it is drained."),
    ('b', "**The diaphragm is flattened, then inverted: an unfavourable length–tension relation, so dyspnoea improves after thoracentesis even if gas exchange changes little.** A flat or inverted dome shortens the muscle fibres and loses the curvature that turns tension into pressure, so each breath takes more effort. Draining the fluid restores the dome; the patient feels better at once although the PaO₂ may hardly move. In the PLEASE study (Muruganandan 2020) a flattened or everted hemidiaphragm, or absent or paradoxical movement, on ultrasound before drainage independently predicted relief of breathlessness afterwards, whether or not the lung re-expanded."),
    ('c', "**Raised pleural pressure → lung collapse, higher pulmonary vascular resistance, RV failure; a tamponade-like picture that reverses with drainage.** A large effusion raises the pressure around the heart and compresses the collapsed lung’s vessels. The right ventricle fills less and faces a higher afterload, and the echo can show diastolic collapse of the right-sided chambers without any pericardial fluid. In a ventilated patient with unexplained hypotension and a large effusion, drainage can restore the blood pressure."),
    ('d', "**Tension hydrothorax: a massive unilateral effusion compressing the mediastinum; mostly malignant.** It behaves like a tension pneumothorax made of fluid: the mediastinum is pushed away, venous return falls, and the patient may be shocked. Drainage relieves it; drain it in stages (PLEU-26)."),
  ],
  mimic=[
    ("Tension hydrothorax vs tension pneumothorax", "Both push the mediastinum away and drop venous return. Hydrothorax: dull percussion, fluid on ultrasound, usually malignant. Pneumothorax: hyperresonance, no sliding, lung point."),
  ],
  traps=[
    ("“An effusion makes you breathless because it collapses the lung”", "The chest wall takes most of the volume; the flattened diaphragm and its poor mechanics explain most of the breathlessness, and they are what drainage fixes."),
  ],
  decode=[
    ("[pattern] Why does dyspnoea improve after thoracentesis when the PaO₂ barely changes?", "The diaphragm recovers its dome and its length–tension relation."),
    ("[pattern] Ventilated patient, large effusion, hypotension, RV diastolic collapse without pericardial fluid", "Tamponade physiology from the effusion; drain it."),
  ],
  punch="The chest wall, not the lung, makes room for most of an effusion; the breathlessness comes from a flattened diaphragm, and a big one can tamponade the heart, so drainage helps more than the gas exchange predicts.",
)

L['PLEU-15'] = dict(
  sub="Respiratory → Pleura → Detecting an effusion on examination and film",
  step=2,
  intro="Step 2 starts with the chest X-ray. Free fluid falls to the lowest point, which in an upright patient is the posterior costophrenic sulcus, so the lateral film shows it before the PA film does, and the supine film, where the fluid spreads along the back, shows it last.",
  parts=[
    ('a', "**Examination is normal below about 300 mL.** Dullness, reduced breath sounds and reduced vocal resonance need a few hundred millilitres between the lung and the chest wall."),
    ('b', "**Posterior sulcus blunted at 75 mL (lateral view); lateral sulcus at 175 mL.** The posterior sulcus is the deepest point, so it fills first, and only the lateral film sees it. The figures most often quoted now come from Blackmore (1996): a meniscus on the lateral film at about 50 mL and on the PA film at about 200 mL; the order, lateral view before PA, is what is tested."),
    ('c', "**About 500 mL obscures the diaphragm.** By then the meniscus rises up the lateral chest wall and the hemidiaphragm outline is lost. A subpulmonic effusion collects under the lung and mimics a raised hemidiaphragm, with its peak shifted laterally; a lateral decubitus film or ultrasound shows the fluid."),
    ('d', "**Supine film: a blunted costophrenic angle (earliest), a homogeneous veil-like density over the lung, a lost hemidiaphragm outline, less visible lower-lobe vessels, an apparent elevation of the hemidiaphragm.** Supine, the fluid layers posteriorly behind the lung, so it shows as a haze through which vessels can still be seen, with no meniscus and no air bronchograms. The supine film misses a good deal of fluid, so in the ICU ultrasound has replaced it for detection (PLEU-16)."),
  ],
  mimic=[
    ("Supine effusion vs consolidation", "Effusion: a graded veil with vessels visible through it, no air bronchograms. Consolidation: dense opacity with air bronchograms, vessels obscured."),
  ],
  traps=[
    ("“The PA film is the most sensitive plain film”", "The lateral film sees fluid in the posterior sulcus first; ultrasound beats both."),
  ],
  decode=[
    ("[pattern] Smallest effusion seen on a lateral film vs a PA film?", "About 50–75 mL lateral; about 175–200 mL PA."),
    ("[pattern] Supine ICU film with a haze over one hemithorax through which vessels are visible", "Layering effusion."),
  ],
  punch="Fluid fills the posterior sulcus first, so the lateral film sees it before the PA film, the supine film shows only a veil, and the examination misses anything below about 300 mL.",
)

L['PLEU-16'] = dict(
  sub="Respiratory → Pleura → Ultrasound and CT for pleural effusion",
  step=2,
  intro="Step 2 moves to the tests that see much more than a film. Ultrasound finds a few tens of millilitres, shows whether the fluid is free or partitioned, and guides the needle; CT shows what the pleura and the lung behind it look like. The two questions linked here both test one ultrasound sign, and the trap is what it does and does not prove.",
  parts=[
    ('a', "**Volume (mL) = 20 × interpleural distance (mm) at the lung base, at end-expiration.** This is Balik’s formula, measured in the supine patient with the trunk raised about 15°, the probe on the posterior axillary line, as the largest distance between visceral and parietal pleura. It is an estimate for deciding whether there is enough fluid to tap or drain, not a precise volume. Ultrasound reliably detects effusions above about 20 mL."),
    ('b', "**Four patterns: anechoic; complex non-septated; complex septated; homogeneously echogenic.** Complex means echoes within the fluid (strands, debris); septated means fibrin strands crossing it to form a honeycomb; homogeneously echogenic means uniformly bright, swirling fluid, typical of pus or blood. In Yang’s series (1992) transudates were anechoic, an anechoic effusion could be either, and the three other patterns were always exudates (the card’s watch line); later series report occasional echogenic transudates, so the fluid analysis still decides."),
    ('c', "**Ultrasound beats CT at detecting septations, and it guides thoracentesis.** Thin fibrin strands are often invisible on CT but plain on ultrasound, and septations predict that a simple drain may fail (PLEU-21). BTS 2023 says every pleural procedure for fluid should be image-guided, which has cut the pneumothorax and organ-puncture rate."),
    ('d', "**Contrast CT separates pleural thickening from fluid and a mass from a loculated effusion; pleural enhancement suggests an exudate.** In empyema, the thickened, enhancing visceral and parietal layers are separated by fluid (the split pleura sign). Leung’s CT features of malignant pleural disease are circumferential thickening, nodular thickening, parietal thickening of more than 1 cm and mediastinal pleural involvement, each highly specific (about 88–100%) but individually insensitive. CT density helps only for blood: fluid of about 35 HU or more strongly suggests a haemothorax (PLEU-24), while transudates and exudates overlap too much to be separated by density."),
  ],
  mimic=[
    ("Sinusoid sign vs barcode sign", "Sinusoid: on M-mode the lung line swings towards the pleural line with each breath, so there is free fluid. Barcode: no sliding (RESP07A, PLEU-08)."),
    ("Effusion vs consolidation on ultrasound", "Effusion: an echo-free or echoic space with the sinusoid sign and a floating lung. Consolidation: tissue-like lung with air bronchograms, no sinusoid sign."),
  ],
  traps=[
    ("“The sinusoid sign proves a transudate”", "It proves free-flowing, low-viscosity fluid, nothing more. DocT keys ‘simple transudative effusion’ as the best of its options (61% right), but an anechoic free effusion can equally be an exudate; only the fluid analysis decides (PLEU-17)."),
    ("“A viscous empyema or organised haemothorax gives a sinusoid sign”", "Septated or thick collections damp the swing; the sign belongs to free fluid."),
    ("“Anechoic means transudate”", "Anechoic can be either; it is the complex and echogenic patterns that are always exudates."),
  ],
  decode=[
    ("POCUS in sepsis: dependent anechoic collection that moves sinusoidally with breathing — what does it mean? [DocT]", "Simple (free-flowing) effusion (61%); it does not prove a transudate."),
    ("Sinusoid sign on lung ultrasound [NEET 2024]", "Pleural effusion."),
    ("[pattern] Which is better than CT at showing septations?", "Ultrasound."),
  ],
  punch="Ultrasound measures the effusion (20 × the gap in mm), shows septations better than CT, and its sinusoid sign means free fluid, not a transudate; any complex or echogenic pattern is an exudate.",
)

L['PLEU-17'] = dict(
  sub="Respiratory → Pleura → Light’s criteria",
  step=3,
  intro="Step 3 is the first fork after a tap: is this a transudate, where the pleura is healthy and the cause lies elsewhere (heart, liver, kidney), or an exudate, where the pleura itself is diseased and must be investigated? Light’s criteria (1972) answer it with three numbers, and five real questions test them in three ways: the criteria themselves, applying them to a set of results, and the mechanism behind an exudate. The detail that separates strong answers is why the criteria overcall exudates and how to rescue a heart-failure effusion that looks exudative.",
  parts=[
    ('a', "**Pleural/serum protein >0.5; pleural/serum LDH >0.6; pleural LDH greater than two-thirds of the upper limit of normal for serum LDH.** Protein in the fluid reflects capillary leak: a healthy pleura lets little through, so the ratio stays low. LDH reflects local inflammation and cell turnover in the pleura. The third criterion uses the laboratory’s upper limit of normal for serum LDH, not the patient’s own serum value (the card’s watch line corrects the notes): with an upper limit of 320 U/L, the cut-off is 213 U/L, and a pleural LDH of 300 U/L meets it."),
    ('b', "**Any one criterion = exudate.** The test was built to miss no exudate, because a missed exudate is a missed cancer, tuberculosis or empyema. Requiring all three would raise specificity but let exudates through; the exam phrasing ‘all three must be met’ is false (PLEU-27a)."),
    ('c', "**Sensitivity 97%, specificity 85%.** The figures vary between series, but the pattern does not: Light’s criteria identify about 98% of exudates and label about a quarter of transudates as exudates (Porcel 2013). High sensitivity, modest specificity: a negative result (no criterion met) is a reliable transudate; a positive one may be a transudate in disguise."),
    ('d', "**Heart failure after diuresis looks exudative; a serum minus pleural albumin gradient >1.2 g/dL shows it is a transudate.** Diuretics remove water from the pleural space faster than protein and LDH, so the fluid concentrates and crosses the 0.5 and 0.6 ratios. The albumin gradient asks a different question — how much less albumin is in the fluid than in the blood — and a gap of more than 1.2 g/dL says the capillary barrier is intact. In Bielsa’s series (2012) Light’s criteria mislabelled 29% of cardiac and 18% of hepatic transudates; the albumin gradient reclassified about 83% of the mislabelled cardiac effusions; the serum–pleural protein gradient >3.1 g/dL does the same job less well (about 55%). A raised serum NT-proBNP supports heart failure (BTS 2023). For a hepatic hydrothorax that looks exudative, a pleural/serum albumin ratio below 0.6 works better (about 77% reclassified, against 62% for the albumin gradient)."),
  ],
  table=dict(title="Applying Light’s criteria to a stem", head=["Value given", "Exudate if", "Note"], rows=[["Pleural/serum protein", "**>0.5**", "convert units first: 80 g/L ÷ 60 g/L = 1.33"], ["Pleural/serum LDH", "**>0.6**", "4000 ÷ 500 = 8"], ["Pleural LDH", "**> two-thirds of the serum upper limit of normal**", "ULN 320 → cut-off 213 U/L"], ["Any one met", "**exudate**", "none met = transudate"], ["Exudate in a diuresed heart-failure patient", "check **albumin gradient >1.2 g/dL**", "if so, treat as transudate"]]),
  mimic=[
    ("Exudate vs pseudo-exudate (diuresed heart failure)", "Both meet Light’s criteria. Pseudo-exudate: known heart failure on diuretics, ratios just over the cut-offs, albumin gradient >1.2 g/dL, high NT-proBNP. True exudate: gradient ≤1.2 g/dL."),
    ("Transudate vs exudate by mechanism", "Transudate: raised hydrostatic or lowered oncotic pressure across a normal pleura. Exudate: raised capillary permeability and blocked lymphatic drainage in a diseased pleura."),
  ],
  traps=[
    ("“Heart failure” for an exudate in a patient with heart disease", "The DocT stem lists heart disease among his comorbidities, but pleural protein 80 g/L against serum 60 and LDH 4000 against 500 are exudate values, and weight loss with a very high LDH points to malignancy (77% and 81% right across two sittings). Heart failure, renal failure and cirrhosis all give transudates."),
    ("“Malignant effusion is from raised hydrostatic pressure or low oncotic pressure”", "Those make transudates; tumour on the pleura raises capillary permeability and blocks lymphatic drainage, and the lymphatic block is why it keeps coming back (94% right)."),
    ("“Thoracic duct disruption” for a malignant exudate", "That gives chyle, with triglyceride >110 mg/dL (PLEU-19)."),
    ("“Pleural LDH less than two-thirds of the upper limit” or ratios below the cut-offs as exudate findings", "All reversed; only ‘protein ratio >0.5’ is right in the PYQ."),
    ("“Compare pleural LDH with the patient’s serum LDH for the third criterion”", "It is compared with the upper limit of normal for serum LDH."),
  ],
  decode=[
    ("Weight loss, effusion, pleural LDH 4000 and protein 80 g/L vs serum 500 and 60 g/L — diagnosis? [DocT; DocT GT]", "Malignancy (77–81%)."),
    ("Metastatic breast cancer, protein ratio 0.65, LDH ratio 0.75, cytology positive — pathophysiology? [DocT GT]", "Raised vascular permeability and impaired lymphatic drainage (94%)."),
    ("By Light’s criteria, which finding indicates an exudate? [DocT GT PYQ]", "Pleural/serum protein >0.5."),
    ("Light’s criteria [NEET 2024]", "Exudate if any: protein ratio >0.5, LDH ratio >0.6, LDH > two-thirds of the upper limit of normal."),
  ],
  extra=[dict(q="Heart-failure patient on furosemide, effusion meets Light’s protein criterion only — next test?", a="Serum minus pleural albumin; a gradient >1.2 g/dL means a transudate (serum NT-proBNP supports it).")],
  punch="Light’s criteria call an exudate on any one of protein ratio >0.5, LDH ratio >0.6 or pleural LDH above two-thirds of the serum upper limit, so they catch nearly every exudate but overcall diuresed heart failure, which an albumin gradient >1.2 g/dL rescues.",
)

L['PLEU-18'] = dict(
  sub="Respiratory → Pleura → Causes of pleural effusion",
  step=3,
  intro="Step 3 sorts the causes by mechanism. A transudate means the pleura is innocent and the problem is pressure — the heart, the liver, the kidney, the protein level — so you treat the cause. An exudate means the pleura is diseased and you look for infection, cancer, tuberculosis or inflammation.",
  parts=[
    ('a', "**Transudate: LV failure (commonest), cirrhosis, hypoalbuminaemia, nephrotic syndrome, peritoneal dialysis, hypothyroidism, mitral stenosis; rare — constrictive pericarditis, urinothorax, Meigs.** Heart failure is the commonest cause of any effusion, usually bilateral, larger on the right. A hepatic hydrothorax is ascites drawn through small diaphragmatic defects by the negative pleural pressure, so it is usually right-sided and can occur with little visible ascites. Peritoneal dialysis fluid crosses the same way and has a very high glucose. A urinothorax is the one transudate with a low pH and a pleural/serum creatinine ratio above 1. Meigs’ syndrome (ovarian fibroma, ascites, effusion) is often exudative by Light’s criteria in practice."),
    ('b', "**Exudate: malignancy, parapneumonic, tuberculosis, pulmonary embolism, autoimmune pleuritis, benign asbestos effusion, pancreatitis, post-MI, post-CABG.** Parapneumonic and malignant effusions are the commonest exudates in most series; in India tuberculosis is a leading cause of a lymphocytic exudate in a young adult (PLEU-19, 20). Pulmonary embolism usually gives a small exudate, though some are transudates. Lung and breast cancer and lymphoma cause most malignant effusions. Pancreatitis gives a left-sided effusion with a high amylase; post-MI (Dressler) and post-CABG effusions are inflammatory and usually left-sided."),
  ],
  mimic=[
    ("Heart failure vs malignancy as the cause of an effusion in an older patient", "Heart failure: bilateral, transudate, cardiomegaly, high NT-proBNP. Malignancy: often unilateral and large, exudate, weight loss, very high LDH, low glucose and pH when extensive."),
  ],
  traps=[
    ("“Heart failure, renal failure or cirrhosis” for an exudate", "All three produce transudates; an exudate with weight loss points to malignancy (DocT, 77%)."),
  ],
  decode=[
    ("Weight loss, effusion with exudative protein and LDH, comorbid heart disease — diagnosis? [DocT]", "Malignancy (77%)."),
    ("[pattern] Right-sided transudate in cirrhosis with little ascites", "Hepatic hydrothorax."),
  ],
  punch="Transudates come from pressure problems with a normal pleura — heart failure first, then liver, kidney and low protein — and exudates from a diseased pleura: infection, cancer, tuberculosis, embolism and inflammation.",
)

L['PLEU-19'] = dict(
  sub="Respiratory → Pleura → Pleural fluid chemistry cut-offs",
  step=4,
  intro="Step 4 reads the fluid once Light’s criteria have called it an exudate. Each test answers a separate question: is something burning glucose and making acid (pH, glucose, LDH)? Is there fat in the fluid (triglyceride, cholesterol)? Did something leak in from the gut (amylase)? Is it tuberculosis (ADA)? Five questions use this card, and they come as a set of fluid results with one value that decides the answer, so the skill is spotting which value matters.",
  parts=[
    ('a', "**Protein <3 g/dL points to a transudate.** This is the old single cut-off. It misclassifies more effusions than Light’s criteria, so use it only as a rough screen; protein in an exudate is often above 3 g/dL, and very high protein (above 7–8 g/dL) suggests myeloma or Waldenström’s."),
    ('b', "**LDH >1000 IU/L points to empyema, rheumatoid effusion or malignancy.** LDH is released by dying neutrophils and tumour cells, so a very high value means intense inflammation or a heavy tumour load. In parapneumonic effusion BTS 2023 uses LDH >900 IU/L, measured when the pH is borderline (7.2–7.4), as a reason to consider a drain (PLEU-21)."),
    ('c', "**Cholesterol >55 mg/dL (the notes also give >45) points to an exudate.** Cholesterol is a large molecule that crosses only a leaky pleura, so it is an extra exudate test, useful in the diuresed heart-failure patient. A very high cholesterol (above about 200 mg/dL) with cholesterol crystals and a low triglyceride is a pseudochylothorax: a long-standing effusion (old tuberculosis, rheumatoid) in a thickened pleura, milky but not chyle."),
    ('d', "**Triglyceride >110 mg/dL means chylothorax; <50 mg/dL excludes it; 50–110 needs lipoprotein analysis for chylomicrons.** Chyle is lymph from the thoracic duct, carrying dietary fat as chylomicrons, so the triglyceride is high and the cells are mostly lymphocytes. Trauma and surgery (oesophagectomy, cardiac surgery) and lymphoma are the main causes; in a patient with CLL or lymphoma, a milky, lymphocytic, high-triglyceride fluid is chylothorax. A fasting patient’s chyle may be clear, so the triglyceride decides, not the colour."),
    ('e', "**Glucose <60 mg/dL (3.3 mmol/L) or a pleural/serum ratio <0.5 points to rheumatoid effusion, empyema, malignancy, tuberculosis or oesophageal rupture.** Glucose falls when it is consumed faster than it diffuses in: by bacteria and neutrophils in empyema, by tumour cells, or across a thickened pleura in rheumatoid disease, where glucose is often below 30 mg/dL and can be near zero. An exudate with normal glucose points away from these, towards an uncomplicated parapneumonic effusion, pulmonary embolism or most other exudates."),
    ('f', "**pH <7.2 means empyema or a complicated parapneumonic effusion.** Normal fluid is about 7.6, so 7.2 reflects a large acid load from glycolysis by neutrophils and bacteria. Measure it anaerobically in a heparinised syringe in a blood-gas analyser, not with pH paper or a laboratory meter; residual air or delay raise the pH, and lidocaine or excess heparin lower it. BTS 2023: pH ≤7.2 → drain; 7.2 to 7.4 → measure LDH and consider a drain if >900 IU/L; ≥7.4 → no drain; if pH cannot be measured, glucose <3.3 mmol/L. Low pH also occurs in rheumatoid effusion, malignancy (where it predicts short survival and failed pleurodesis), tuberculosis and oesophageal rupture."),
    ('g', "**Raised amylase points to pancreatitis, oesophageal rupture or malignancy.** Pancreatic amylase comes from pancreatitis or a pancreaticopleural fistula; salivary amylase comes from a ruptured oesophagus, where the fluid also has a very low pH and food particles, or from an adenocarcinoma."),
    ('h', "**ADA >35–50 U/L points to tuberculosis.** Adenosine deaminase comes from activated T lymphocytes. A meta-analysis of 40 Indian studies (3,524 patients) found a pooled sensitivity of 94% and specificity of 89%; 40 IU/L was the commonest cut-off, and the authors judged it better at excluding tuberculosis than at confirming it. BTS 2023: in high-prevalence populations ADA may be used to diagnose tuberculous pleurisy; in low-prevalence ones it is mainly an exclusion test. So in India a lymphocytic exudate with ADA above 40 is treated as tuberculosis, with culture and, if doubt remains, pleural biopsy. ADA is also raised in empyema (neutrophilic), lymphoma and rheumatoid effusion; a very high value (above about 250) suggests empyema or lymphoma rather than tuberculosis."),
  ],
  table=dict(title="Which value decides the stem", head=["Fluid picture", "Decisive value", "Answer"], rows=[["Milky, lymphocytic, afebrile, CLL", "**triglyceride >110 mg/dL**", "chylothorax"], ["Milky, chronic thick pleura, crystals", "**cholesterol >200 mg/dL, triglyceride <110**", "pseudochylothorax"], ["Fever, cloudy fluid", "**pH <7.2** (blood-gas analyser), glucose <60", "complicated effusion or empyema → drain"], ["Very low glucose (<30), high LDH, joints", "**glucose**", "rheumatoid effusion"], ["Lymphocytic exudate, young, India", "**ADA >40 U/L**", "tuberculosis"], ["Exudate, normal glucose", "**glucose >60**", "not empyema, rheumatoid or cancer; think embolism or uncomplicated parapneumonic"]]),
  mimic=[
    ("Chylothorax vs pseudochylothorax", "Both milky. Chylothorax: triglyceride >110 mg/dL, chylomicrons, lymphocytes, acute (trauma, surgery, lymphoma). Pseudochylothorax: cholesterol >200 mg/dL with crystals, triglyceride low, years-old effusion in a thick pleura."),
    ("Chylothorax vs empyema", "Both can look white. Empyema: pus with neutrophils, low pH and glucose, high LDH, fever. Chylothorax: normal pH and glucose, low LDH, lymphocytes."),
    ("Rheumatoid effusion vs empyema", "Both have low glucose, low pH and high LDH. Rheumatoid: glucose often near zero, sterile, joint disease, often a pseudochylous chronic effusion. Empyema: fever, organisms, pus."),
  ],
  traps=[
    ("“Pseudochylothorax” for a milky effusion with triglyceride 240 mg/dL", "Triglyceride above 110 is chyle; cholesterol 110 is not in the pseudochylous range (above 200). 38% missed this DocT GT question."),
    ("“Empyema” or “parapneumonic” for milky fluid", "pH 7.45, glucose 95 and LDH 110 rule out an infected effusion; lymphocytes and high triglyceride in a CLL patient make it chylothorax."),
    ("“Rheumatoid” with pH 7.45 (Marrow)", "Marrow keys rheumatoid arthritis for LDH 500, pH 7.45 and low glucose because of the low glucose, but a rheumatoid effusion classically has a pH below 7.2 as well. For Marrow pick its key; know the full rheumatoid picture: very low glucose, high LDH, low pH."),
    ("“Pulmonary embolism” for an exudate with glucose 65 (Marrow)", "The point is that normal glucose argues against empyema, rheumatoid and malignancy; but an uncomplicated parapneumonic effusion also has normal glucose, so the key leans on the rest of the stem. For Marrow pick its key."),
    ("“pH by litmus paper or a lab meter”", "Only the blood-gas analyser value counts; Marrow keys ‘pH 7.2 by ABG analyser’ as the empyema finding."),
  ],
  decode=[
    ("CLL, 800 mL milky fluid, pH 7.45, LDH 110, glucose 95, triglyceride 240, cholesterol 110, 90% lymphocytes [DocT GT]", "Chylothorax (62%)."),
    ("Effusion with LDH 500, pH 7.45, low glucose — cause? [Marrow]", "Rheumatoid arthritis (key; low glucose is the clue)."),
    ("Exudate (protein ratio 0.6), glucose 65 — cause? [Marrow]", "Pulmonary embolism (normal glucose excludes the low-glucose causes)."),
    ("Homeless teenager who injects drugs, haemoptysis, effusion, hilar nodes [Marrow]", "Tuberculosis: lymphocytic exudate, ADA >40, confirm by culture."),
    ("Pleural fluid finding most suggestive of empyema [Marrow]", "pH 7.2 by blood-gas analyser."),
  ],
  extra=[dict(q="Pleural fluid pH: which method?", a="Anaerobic heparinised sample in a blood-gas analyser; air or delay raise it, lidocaine lowers it.")],
  punch="Read the one value that decides: pH ≤7.2 and glucose <60 for infection, very low glucose for rheumatoid, triglyceride >110 for chyle, cholesterol >200 with low triglyceride for pseudochyle, amylase for pancreas or oesophagus, and ADA >40 in a lymphocytic exudate for tuberculosis.",
)

L['PLEU-20'] = dict(
  sub="Respiratory → Pleura → Pleural fluid differential count",
  step=4,
  intro="Step 4 continues with the cells. The dominant cell tells you how old and what kind the process is: neutrophils for an acute insult, lymphocytes for a chronic one, eosinophils mostly for air or blood in the space.",
  parts=[
    ('a', "**Neutrophilia: parapneumonic effusion, pancreatitis, subphrenic abscess, lupus pleuritis, and pulmonary embolism.** Any acute pleural injury brings neutrophils first, including early tuberculosis, so a neutrophilic tap does not exclude it."),
    ('b', "**Eosinophilia, >10%: haemothorax, pulmonary infarction, benign asbestos effusion, parasites, fungal infection, drugs, and pneumothorax.** Air or blood in the space is the classic cause, including air or blood from a previous tap, so repeated taps can make the fluid eosinophilic. In modern series, though, malignancy is the commonest single cause of an eosinophilic effusion, with idiopathic and parapneumonic effusions next, so eosinophilia does not exclude cancer. It does make tuberculosis less likely, because a tuberculous effusion rarely has more than 10% eosinophils."),
    ('c', "**Lymphocytosis, >85%: tuberculosis, lymphoma, sarcoidosis, rheumatoid pleurisy; a lymphocytic effusion is >50%.** Above 50% lymphocytes, think chronic: tuberculosis and malignancy first, plus chylothorax, post-CABG and yellow-nail syndrome. Above 85%, tuberculosis and lymphoma lead; in India a lymphocytic exudate with a high ADA is tuberculosis until proved otherwise (PLEU-19h)."),
  ],
  mimic=[
    ("Tuberculous vs malignant lymphocytic exudate", "Both lymphocytic. Tuberculosis: younger, ADA >40, scanty mesothelial cells. Malignancy: older, ADA low, cytology or biopsy positive."),
  ],
  traps=[
    ("“Eosinophilic effusion means parasites”", "Parasites are a rare cause; it usually means air or blood in the space (including from a previous tap) or malignancy."),
  ],
  decode=[
    ("[pattern] Lymphocytic exudate (90%) with ADA 70 in a young Indian adult", "Tuberculous pleurisy."),
    ("[pattern] Eosinophilic effusion after a pneumothorax or repeated taps", "Air or blood in the pleura; not a separate disease."),
  ],
  punch="Neutrophils mean an acute process, eosinophils mean air, blood or often malignancy but rarely tuberculosis, and lymphocytes over 85% mean tuberculosis or lymphoma.",
)

L['PLEU-21'] = dict(
  sub="Respiratory → Pleura → Parapneumonic effusion",
  step=5,
  intro="Step 5 starts with the commonest infected space. A pneumonia makes the pleura leaky; at first the fluid is sterile and clears with antibiotics, but if bacteria get in, they consume glucose, produce acid, and lay down fibrin that walls the fluid into pockets. The question is when that process needs a tube.",
  parts=[
    ('a', "**Uncomplicated (free-flowing, sterile; antibiotics alone); complicated (bacterial invasion, septations); empyema (frank pus).** These are stages of one process: exudative (sterile, free), fibrinopurulent (bacteria, falling pH and glucose, fibrin septations), and organising (a thick peel that traps the lung). Frank pus is empyema whatever its chemistry."),
    ('b', "**A chest tube is mandated by pus, a positive Gram stain, pH <7.20, glucose <60 mg/dL, LDH >1000, or a complex septated pattern on ultrasound.** BTS 2023 states it as: pH ≤7.2 → drain if there is a safe pocket; pH above 7.2 but below 7.4 → measure LDH, and consider a drain if it is above 900 IU/L, especially with glucose ≤4.0 mmol/L, septations, pleural enhancement on CT or a large effusion; pH ≥7.4 → no drain; if pH cannot be measured, glucose below 3.3 mmol/L (60 mg/dL) suggests a complicated effusion. So the card’s LDH >1000 is the older stand-alone threshold; LDH now counts mainly when the pH is borderline."),
    ('c', "**No septations: small-bore catheter. Septations: large-bore.** BTS 2023 now recommends a small-bore drain (14 F or smaller) for the initial drainage of pleural infection in general, flushed regularly, because small tubes drain as well as large ones and hurt less; septations are dealt with by fibrinolytics or surgery rather than by a bigger tube (PLEU-22)."),
    ('d', "**Remove the tube when sepsis has resolved and drainage is <200 mL/day.** The aim is a dry space and a well patient; a tube that has stopped draining while a collection remains on imaging is blocked or the fluid is loculated, not ‘finished’."),
  ],
  mimic=[
    ("Uncomplicated vs complicated parapneumonic effusion", "Uncomplicated: free-flowing, pH ≥7.4, glucose normal, no organisms; antibiotics only. Complicated: pH ≤7.2 or Gram stain positive or septations; drain."),
    ("Empyema vs lung abscess on CT", "Empyema: lenticular, compresses lung, split pleura sign, obtuse angle with the chest wall. Abscess: round, thick wall within lung, acute angle (see top-up on lung abscess)."),
  ],
  traps=[
    ("“After a failed drain and tPA/DNase, open thoracotomy or a second tube”", "VATS debridement: less morbidity and shorter stay than open decortication (Marrow; BTS 2023 prefers VATS over thoracotomy)."),
    ("“Septated, so put in a large-bore tube”", "BTS 2023 uses small-bore tubes first; septations call for fibrinolytics or surgery."),
  ],
  decode=[
    ("Failed drain plus fibrinolytics in a septated empyema — surgical approach? [Marrow]", "VATS debridement."),
    ("[pattern] Pneumonia, effusion, pH 7.1 on blood-gas analyser — next step?", "Chest drain."),
    ("[pattern] pH 7.3, LDH 1200, septations on ultrasound", "Consider a drain (BTS 2023 intermediate pH)."),
  ],
  punch="A parapneumonic effusion needs a drain when it is pus, Gram-positive, pH ≤7.2 or septated (or pH 7.2–7.4 with LDH >900); start small-bore, and send failures to fibrinolytics, then VATS.",
)

L['PLEU-22'] = dict(
  sub="Respiratory → Pleura → Treating pleural infection",
  step=5,
  intro="Step 5 continues with treatment once the drain is in. Three things clear a pleural infection: antibiotics that reach the organisms, drainage of the pus, and breaking down the fibrin and the thick fluid that stop it draining. The question linked here tests the third, and the trial behind it, MIST2.",
  parts=[
    ('a', "**Antibiotics for at least 3 weeks (the notes say 4–10 weeks); cover anaerobes; hospital-acquired empyema also needs MRSA and Gram-negative cover; a macrolide only if atypicals are strongly suspected; intrapleural antibiotics not recommended (BTS 2010).** Anaerobes are common in pleural infection and often fail to grow, so cover is given regardless (for example cefuroxime with metronidazole, or co-amoxiclav). The optimal length is not established: courses of roughly 2 to 6 weeks are usual, recent trials suggest shorter courses may suffice in patients who settle without surgery, and the clinical and radiological response guides it. Atypical organisms rarely cause empyema. Aminoglycosides penetrate pus poorly and are inactivated at low pH. Risk is stratified with the RAPID score (renal: urea; age; purulence; infection source; dietary: albumin): in the PILOT validation (542 patients) 3-month mortality was 2.3%, 9.2% and 29.3% for low, medium and high scores. Non-purulent fluid scores higher than pus in RAPID."),
    ('b', "**MIST2: tPA 10 mg plus DNase 5 mg intrapleurally, twice daily for 3 days.** Each dose is instilled through the drain, which is clamped for about an hour and then opened. tPA activates plasminogen and dissolves the fibrin septations; DNase cuts the free DNA from dead neutrophils that makes pus viscous. BTS 2023: consider the combination when drainage has stopped but a collection remains; single agents and streptokinase are not recommended."),
    ('c', "**Better radiographic clearance, fewer surgical referrals, shorter hospital stay; either drug alone was ineffective.** In MIST2 (Rahman, NEJM 2011; 210 patients, 2×2 factorial) the pleural opacity fell by 29.5% with tPA plus DNase vs 17.2% with placebo; surgical referral at 3 months was 4% vs 16%; hospital stay was 11.8 vs 24.8 days. DNase alone had more surgical referrals than placebo (39%). The earlier MIST1 trial (Maskell, NEJM 2005; 454 patients) of streptokinase alone showed no benefit in death, surgery, radiology or hospital stay, which is why BTS 2010 advised against routine fibrinolytics (the card’s watch line)."),
    ('d', "**Main adverse effect: intrapleural bleeding, 2–12%.** MIST2 itself recorded two pleural haemorrhages among its 210 patients. In the largest series (Akulian 2022, about 1,800 patients) bleeding occurred in 4.1% overall and 9.6% of those on therapeutic anticoagulation, falling to 2.6% when anticoagulation was withheld; half-dose tPA did not lower it. So check clotting, hold anticoagulants where possible, and watch the drain for blood."),
  ],
  table=dict(title="MIST2 arms (Rahman, NEJM 2011)", head=["Arm", "Opacity change", "Surgical referral"], rows=[["Placebo", "−17.2%", "16%"], ["tPA alone", "not significant", "6%"], ["DNase alone", "not significant", "**39%**"], ["**tPA + DNase**", "**−29.5%**", "**4%**"]]),
  mimic=[
    ("tPA vs DNase role", "tPA breaks septations; DNase thins the pus. Only together do they work."),
  ],
  traps=[
    ("“Intrapleural antibiotics” or “streptokinase” for a loculated empyema", "Neither is recommended; tPA plus DNase reduces surgical referral (Marrow)."),
    ("“DNase alone thins pus, so it is enough”", "In MIST2 DNase alone had the most surgical referrals."),
    ("“BTS says no fibrinolytics”", "That was BTS 2010, before MIST2; BTS 2023 recommends considering tPA plus DNase."),
  ],
  decode=[
    ("Loculated empyema despite a drain — what reduces surgical referral? [Marrow]", "Intrapleural tPA plus DNase."),
    ("[pattern] MIST2 regimen?", "tPA 10 mg + DNase 5 mg twice daily for 3 days."),
  ],
  punch="Pleural infection needs anaerobic cover for weeks, drainage, and, if pockets remain, tPA with DNase together, which in MIST2 cut surgical referral from 16% to 4% and halved the stay; neither drug works alone.",
)

L['PLEU-23'] = dict(
  sub="Respiratory → Pleura → Malignant pleural effusion",
  step=5,
  intro="Step 5 ends with the other diseased pleura. A malignant effusion means the tumour has reached the pleura, so the aim is palliation: relieve breathlessness with the fewest procedures and days in hospital. The trials since 2010 have changed how the options are ranked.",
  parts=[
    ('a', "**Commonest exudate after age 60; implies disseminated disease; up to 25% are asymptomatic.** Tumour on the pleura raises capillary permeability and blocks the lymphatic stomata and mediastinal nodes that drain the space, which is why the fluid is an exudate and why it recurs after drainage (DocT GT, 94%). Lung and breast cancer and lymphoma cause most cases; survival depends on the tumour and the patient’s fitness, estimated by the LENT score (BTS 2023)."),
    ('b', "**Options for a recurrent symptomatic effusion: chest drain with talc pleurodesis; thoracoscopic talc insufflation; indwelling pleural catheter (for patients unfit for anaesthesia or thoracoscopy); pleurectomy after failed pleurodesis; pleuroperitoneal shunt last.** BTS 2023 offers patients with an expandable lung a choice of talc pleurodesis or an indwelling pleural catheter (IPC) as first-line treatment, not an IPC only for the unfit. In TIME2 (106 patients) breathlessness improved equally at 6 weeks, the IPC group spent no initial days in hospital vs 4, and needed fewer further procedures (6% vs 22%), at the cost of more adverse events, mainly infection. In AMPLE (146 patients) total hospital days were 10 vs 12 and effusion-related days 1 vs 4 with the IPC. If more than about a quarter of the lung will not re-expand (non-expandable lung), talc cannot work and an IPC is preferred."),
    ('c', "**Talc succeeds in about 90%.** That is the older figure from case series. In TAPPS (330 patients) pleurodesis failed at 90 days in 24% with talc slurry and 22% with thoracoscopic poudrage, so success is closer to three in four, and slurry and poudrage are equivalent; BTS 2023 allows either, and poudrage is done during a diagnostic thoracoscopy if one is planned anyway."),
    ('d', "**If life expectancy is under 3 months, repeated therapeutic thoracentesis (BTS 2010: under 1 month).** The reasoning is to avoid an admission for pleurodesis in someone with little time. BTS 2023 recommends a definitive option (talc pleurodesis or an IPC) over repeated aspiration, especially when prognosis is better, because repeated aspiration commits the patient to many procedures as the fluid returns."),
  ],
  mimic=[
    ("Talc pleurodesis vs IPC", "Talc: one admission, aims to seal the space, needs an expandable lung, fewer adverse events. IPC: day case, works with non-expandable lung, drained at home, more infections, may produce spontaneous pleurodesis."),
  ],
  traps=[
    ("“Raised hydrostatic pressure” or “low oncotic pressure” as the mechanism", "Those cause transudates; malignancy raises permeability and blocks lymphatic drainage (94% right)."),
    ("“An IPC is only for patients unfit for thoracoscopy”", "BTS 2023 offers it as a first-line choice alongside talc."),
  ],
  decode=[
    ("Metastatic breast cancer, large exudative effusion with malignant cells — pathophysiology? [DocT GT]", "Increased vascular permeability and impaired lymphatic drainage (94%)."),
    ("[pattern] Recurrent malignant effusion, lung does not re-expand after drainage — best option?", "Indwelling pleural catheter."),
  ],
  punch="A malignant effusion means pleural spread and recurs because the lymphatics are blocked; offer talc (slurry or poudrage, about three-quarters succeed) or an indwelling catheter as first-line choices, the catheter if the lung will not re-expand.",
)

L['PLEU-24'] = dict(
  sub="Respiratory → Pleura → Haemothorax",
  step=6,
  intro="Step 6 turns to blood in the pleural space. The single question here gives a dense effusion on CT in an anticoagulated, hypotensive patient after a fall, and asks you to recognise blood from its density before any tap.",
  parts=[
    ('a', "**Diagnostic criterion: pleural fluid haematocrit >50% of blood haematocrit.** Very little blood makes fluid look red, so colour alone means little; a bloodstained effusion from cancer or infarction usually has a haematocrit of a few per cent. An older haemothorax dilutes with reactive fluid, so its haematocrit may fall below half. On CT, simple fluid is close to water density, while a density of about 35 HU or more strongly suggests blood, and clot is denser still; a dense effusion with hypotension after trauma or on an anticoagulant is a haemothorax until proved otherwise."),
    ('b', "**Massive haemothorax: >1.5 L.** ATLS means 1500 mL on immediate drainage (the card’s watch line corrects the notes’ ‘over 24 h’), and it is an indication for thoracotomy (PLEU-25). The patient is in haemorrhagic shock with a dull hemithorax and flat neck veins, unlike tension pneumothorax."),
    ('c', "**Drain: large, 28–30 Fr, mid-axillary line.** ATLS 10th edition gives 28–32 Fr, in the 5th space just anterior to the mid-axillary line, inserted by blunt dissection; a large tube resists clotting. Smaller tubes (14 Fr pigtails) are increasingly used in stable patients. Prophylactic antibiotics are given for drains in penetrating trauma, and a malpositioned drain may be withdrawn but never pushed further in, because the outer part is no longer sterile."),
    ('d', "**A drain is NOT inserted with clinical or radiological signs of aortic dissection or transection.** Case reports describe massive bleeding and death when the chest of a patient with a torn aorta is drained before the bleeding is controlled, because the clotted, contained haemothorax is limiting the leak. Such a patient needs CT angiography and control of the aorta (stent graft or surgery) first, then drainage."),
  ],
  mimic=[
    ("Haemothorax vs tension pneumothorax in trauma", "Both shocked with reduced breath sounds. Haemothorax: dull, flat neck veins. Tension: hyperresonant, distended neck veins."),
    ("Haemothorax vs bloodstained effusion", "Haemothorax: haematocrit >50% of blood. Bloodstained effusion (cancer, infarction, trauma of the tap): haematocrit a few per cent."),
  ],
  traps=[
    ("“Transudate” or “empyema” for a dense effusion after a fall on apixaban", "35 HU is blood density; transudates are near water. 84% chose haemothorax."),
    ("“1.5 L over 24 hours defines massive haemothorax”", "ATLS means on immediate drainage."),
  ],
  decode=[
    ("Fall on apixaban, hypotension, large right effusion of 35 HU on CT — diagnosis? [DocT GT]", "Haemothorax (84%)."),
    ("[pattern] Bloody pleural fluid: what makes it a haemothorax?", "Pleural haematocrit >50% of blood haematocrit."),
  ],
  punch="A haemothorax is pleural fluid with more than half the blood haematocrit, dense on CT; drain it with a large tube in the 5th space, but not when the aorta may be torn.",
)

L['PLEU-25'] = dict(
  sub="Respiratory → Pleura → Urgent thoracotomy for haemothorax",
  step=6,
  intro="Step 6 continues with the decision that follows the drain: is the bleeding from a vessel that needs a surgeon? Most haemothoraces stop with drainage alone, because the low-pressure lung vessels seal once the lung is up; ongoing loss means systemic arteries (intercostal, internal mammary) or the heart and great vessels.",
  parts=[
    ('a', "**Haemodynamic instability despite resuscitation.** Physiology decides more than any volume: a patient who keeps needing blood goes to theatre."),
    ('b', "**Initial drainage >1500 mL.** That volume at once means a major vessel. Because blood may clot in the chest, a small output from a patient who remains shocked does not reassure."),
    ('c', "**Continued bleeding >200 mL/h for 2–4 h.** Measured once the initial volume is out; ATLS adds a persistent need for transfusion."),
    ('d', "**Continued bleeding >1500 mL/day.** EAST guidance treats 1500 mL in 24 hours as a trigger to consider surgical exploration."),
    ('e', "**Retained clot filling more than one-third of the pleural space.** A retained haemothorax is a nidus for empyema and later a fibrothorax that traps the lung. Clotted haemothorax with a persistent effusion is treated by VATS rather than open thoracotomy (the card’s watch line), ideally within the first 3–7 days (EAST), before the clot organises; intrapleural fibrinolysis is an alternative, especially when surgery carries high risk. A second chest tube is not recommended for retained clot."),
  ],
  mimic=[
    ("Massive haemothorax vs retained haemothorax", "Massive: active bleeding, >1500 mL at once or >200 mL/h, open thoracotomy. Retained: clot left after drainage, stable patient, VATS within days."),
  ],
  traps=[
    ("“Insert a second tube for retained clot”", "Early VATS is recommended instead."),
  ],
  decode=[
    ("[pattern] Trauma, chest drain yields 1700 mL at once — next step?", "Thoracotomy."),
    ("[pattern] Drain output 250 mL/h for 3 h after the initial evacuation", "Thoracotomy."),
    ("[pattern] Stable, clotted haemothorax on day 3 despite a drain", "VATS evacuation."),
  ],
  punch="Go to theatre for instability, 1500 mL at once, 200 mL/h for 2–4 h, 1500 mL in a day, or clot filling a third of the chest, and clear a retained clot by VATS within the first week.",
)

L['PLEU-26'] = dict(
  sub="Respiratory → Pleura → Re-expansion pulmonary oedema",
  step=6,
  intro="Step 6 ends with the danger of draining too much, too fast. Two questions test it: one asks you to recognise re-expansion pulmonary oedema after a tap, and one asks when to stop draining, which only 11% got right. The answer has moved from a fixed volume to the patient’s symptoms.",
  parts=[
    ('a', "**Mechanism: a sudden fall in pleural pressure → hydrostatic shift, plus ischaemia–reperfusion capillary leak.** As the collapsed lung is pulled open, very negative pleural pressure sucks fluid into its interstitium, and the capillaries of a lung that was hypoxic for days leak when it is reperfused. The oedema is in the re-expanded lung only: unilateral B-lines and consolidation on ultrasound, usually within the first hour and up to 24 hours. Mortality in older mixed series was up to about 20%."),
    ('b', "**Risk factors: collapse for more than 3 days, large volume, rapid drainage.** Also younger age and a large or tension pneumothorax re-expanded quickly. These are tendencies, not rules: in Mahfood’s review (1988) about a third of cases followed a short collapse or re-expansion without suction. And in a prospective study of 185 large-volume thoracenteses (Feller-Kopman 2007), clinical re-expansion oedema occurred in only 0.5% and radiographic oedema in 2.2%, and it was not related to the volume removed or the pleural pressure. Symptomatic re-expansion oedema follows fewer than 1% of drainages."),
    ('c', "**Drain no faster than 500 mL/h, maximum 1.5 L.** The 1.5 L is per drainage session, not per day (the card’s watch line). The BTS clinical statement keeps about 1.5 L as the usual limit for one aspiration, allows more in expert hands, and makes the symptoms the stopping rule: stop for chest tightness, pain, persistent cough or worsening breathlessness, even before the planned volume. Pleural manometry has not been shown to prevent re-expansion oedema: in the Lentz trial (2019; 128 patients randomised) manometry-guided drainage did not reduce chest discomfort compared with symptom-guided drainage, though there were fewer pneumothoraces with manometry (0 vs 10%, all asymptomatic). Chest discomfort reflects the steep fall in pleural pressure as fluid comes out of a lung that cannot follow."),
    ('d', "**Prevention and treatment: CPAP 5–10 cmH₂O, oxygen, NIV if needed.** Stop the drainage (or clamp the drain), give oxygen, take a film, and support with CPAP or high-flow oxygen, ventilating if needed; diuretics play little part because the problem is leak and suction, not fluid overload. It usually resolves in 24–72 hours."),
    ('e', "**A chest drain is removed (general rule) when the lung is fully expanded and output is <100 mL/day.** For fluid, the threshold is a small daily output with the lung up; for air, the leak must have stopped (RESP07A, PLEU-12)."),
  ],
  table=dict(title="When to stop a therapeutic tap", head=["Stopping rule", "Status", "Why"], rows=[["**Chest tightness, pain, persistent cough, worse breathlessness**", "**BTS: stop**", "signals a steep fall in pleural pressure (non-expandable lung or impending oedema)"], ["Fixed 1 L", "old rule", "volume does not predict oedema; asymptomatic drainage beyond 1–1.5 L is safe"], ["Manometry below −20 cmH₂O", "not routine", "did not reduce discomfort in a trial; not shown to prevent oedema"], ["A single cough", "not a reason alone", "common as the lung re-expands; persistent cough is"]]),
  mimic=[
    ("Re-expansion oedema vs non-expandable lung", "Both cause chest discomfort during drainage. Re-expansion oedema: hypoxaemia, unilateral B-lines and consolidation within hours. Non-expandable lung: the lung cannot follow, pleural pressure plunges, pneumothorax ex vacuo, no oedema."),
    ("Re-expansion oedema vs post-procedure haemothorax or pneumothorax", "Haemothorax: re-accumulating echogenic fluid, falling haemoglobin. Pneumothorax: absent sliding. Re-expansion oedema: B-lines and consolidation in the drained lung."),
  ],
  traps=[
    ("“Stop at 1 L”", "Only 11% chose the right answer (chest discomfort) on DocT GT; most stopped at a fixed volume. Volume alone does not predict re-expansion oedema; symptoms are the stopping rule."),
    ("“Stop when the manometer reads below −20 cmH₂O”", "Manometry did not reduce discomfort (Lentz 2019) and has not been shown to prevent oedema; it is not routine."),
    ("“Stop when the patient coughs”", "A brief cough is common as the lung re-expands; it is persistent cough with tightness or breathlessness that stops the tap."),
  ],
  decode=[
    ("Large malignant effusion drained under ultrasound — when to stop to maximise drainage and minimise complications? [DocT GT]", "When the patient complains of chest discomfort (11%)."),
    ("Acute hypoxaemia 2 h after a large tap; ultrasound shows unilateral interstitial syndrome with consolidation [DocT GT]", "Re-expansion pulmonary oedema (88%)."),
  ],
  punch="Re-expansion oedema is rare, unilateral and early; stop any large drainage when the patient feels chest tightness, pain or persistent cough, keep to about 1.5 L a session, and treat with oxygen and CPAP.",
)

L['PLEU-27'] = dict(
  sub="Respiratory → Pleura → Review: true or false",
  step=3,
  intro="This review runs through the deck from step 2 (imaging) to step 6 (blood and safe drainage), starting with Light’s criteria at step 3. Each statement is a belief the real questions show people hold.",
  parts=[
    ('a', "**False: any one of Light’s criteria is enough for an exudate.** The test is built for sensitivity (PLEU-17)."),
    ('b', "**True: volume in mL = 20 × interpleural distance in mm, at the base at end-expiration.** Balik’s estimate (PLEU-16)."),
    ('c', "**True: pleural triglyceride above 110 mg/dL supports chylothorax; below 50 excludes it.** Between, look for chylomicrons (PLEU-19)."),
    ('d', "**True: pleural pH below 7.2 calls for drainage.** BTS 2023 writes it as ≤7.2, measured in a blood-gas analyser (PLEU-21)."),
    ('e', "**False: intrapleural antibiotics are not recommended in empyema.** Intrapleural tPA with DNase is (PLEU-22)."),
    ('f', "**True: haemothorax means a pleural haematocrit above 50% of the blood haematocrit.** (PLEU-24)"),
    ('g', "**True: drainage above 200 mL/h is an indication for thoracotomy.** For 2–4 hours after the initial evacuation (PLEU-25)."),
    ('h', "**False: re-expansion oedema is likelier after a long collapse, beyond 3 days.** A lung that was collapsed for days leaks when it is reperfused (PLEU-26)."),
  ],
  mimic=[
    ("Chylothorax vs pseudochylothorax", "Triglyceride >110 vs cholesterol >200 with low triglyceride."),
  ],
  traps=[
    ("“All three Light’s criteria must be met”", "Any one."),
  ],
  decode=[
    ("[pattern] True or false: pH below 7.2 in a parapneumonic effusion is an indication to drain", "True."),
  ],
  punch="Any one Light’s criterion makes an exudate, 20 × the gap in mm estimates volume, triglyceride >110 is chyle, pH ≤7.2 means drain, intrapleural antibiotics are out, haematocrit >50% is blood, 200 mL/h for hours means theatre, and long collapse risks re-expansion oedema.",
)

FLAGS = {}
FLAGS['PLEU-14'] = "Card a: ‘one-fifth at TLC’ is not supported by the dog studies usually cited (Krell & Rodarte 1985; Dechman 1994), which found the lung gives up about one-third of the added volume at both FRC and TLC. Explanation restates the card and gives the study result."
FLAGS['PLEU-15'] = "Card b gives 75 mL (posterior sulcus, lateral view) and 175 mL (lateral sulcus); the thresholds most often quoted now are ~50 mL on the lateral film and ~200 mL on the PA film (Blackmore 1996, verified). Not wrong, a different older series; explanation gives both."
FLAGS['PLEU-17'] = "Card c (sensitivity 97%, specificity 85%) is within the published range, but specificity is often lower: Porcel 2013 says Light’s criteria identify ~98% of exudates and mislabel ~25% of transudates. Card d could add the protein gradient >3.1 g/dL (reclassifies ~55% vs 83% for the albumin gradient) and serum NT-proBNP (BTS 2023). Explanation adds them."
FLAGS['PLEU-18'] = "Minor: Meigs’ syndrome (card a, ‘rare transudate’) is often exudative by Light’s criteria, and pulmonary embolism (card b) is usually but not always an exudate; urinothorax is the transudate with low pH. Explanation says so."
FLAGS['PLEU-19'] = "Card f (pH <7.2) should carry the BTS 2023 scheme: pH ≤7.2 drain; >7.2 to <7.4 measure LDH, consider drain if >900 IU/L; ≥7.4 no drain; glucose <3.3 mmol/L if no pH; measure in a blood-gas analyser. Two Marrow keys are disputed: rheumatoid arthritis for LDH 500, pH 7.45, low glucose (RA effusion classically has pH <7.2), and pulmonary embolism for an exudate with glucose 65 (uncomplicated parapneumonic also has normal glucose). Pseudochylothorax (cholesterol >200, crystals) is not on the card; DocT GT tests it as the distractor."
FLAGS['PLEU-20'] = "Card b omits malignancy, the commonest single cause of an eosinophilic effusion in modern series (air and blood are the classic causes). Explanation adds it."
FLAGS['PLEU-21'] = "Dated on two points. b: ‘LDH >1000’ as a stand-alone drain criterion is the older Light threshold; BTS 2023 uses LDH >900 IU/L only when pH is >7.2 and <7.4. c: ‘septations → large-bore’ — BTS 2023 recommends a small-bore drain (≤14 F) for initial drainage of pleural infection; septations are treated with tPA/DNase or VATS. Watch line could add the Marrow point: after failed drain and fibrinolytics, VATS rather than open surgery."
FLAGS['PLEU-22'] = "Card a is BTS 2010 (‘at least 3 weeks’); the optimal duration is not established (2–6 weeks is usual; a BTS 2023 figure could not be confirmed online), and BTS 2023 adds the RAPID score (verified PILOT mortality 2.3/9.2/29.3%). Card d ‘bleeding 2–12%’: MIST2 recorded two pleural haemorrhages among 210 patients; the largest series (Akulian 2022) found 4.1% overall and 9.6% on therapeutic anticoagulation, so the range is plausible but its top end applies to anticoagulated patients. Watch line ‘BTS 2010 said no routine fibrinolytics’ is right; BTS 2023 now recommends considering tPA + DNase."
FLAGS['PLEU-23'] = "Dated. b: IPC is no longer reserved for the unfit — BTS 2023 offers IPC or talc as first-line by patient choice (TIME2, AMPLE), IPC preferred if >25% non-expandable lung; pleurectomy and pleuroperitoneal shunt are rarely used. c: ‘talc ~90%’ is the old case-series figure; TAPPS (330 patients) found 90-day failure 24% (slurry) vs 22% (poudrage). d: BTS 2023 prefers a definitive option over repeated aspiration, and IPC suits a short prognosis. Explanation restates the card and teaches the current position."
FLAGS['PLEU-24'] = "Card c ‘28–30 Fr’: ATLS 10th gives 28–32 Fr; smaller (14 Fr pigtail) tubes are increasingly used in stable patients. Card d (no drain with signs of aortic injury) is supported by case reports of exsanguination on drainage before aortic control. CT density (fresh blood ~30–45 HU) is not on the card; DocT GT tests it."
FLAGS['PLEU-26'] = "Card c gives a fixed limit (≤500 mL/h, max 1.5 L) but no symptom rule; the DocT GT key (11% right) and the BTS clinical statement make chest tightness, pain, persistent cough or worsening breathlessness the stopping rule, with ~1.5 L per attempt as a guide; manometry is not routine (Lentz 2019). Feller-Kopman 2007: clinical REPO 0.5%, unrelated to volume or pleural pressure. Explanation adds this."
