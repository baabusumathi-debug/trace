# GI02A — Explain v3 ("Learn" depth): acute pancreatitis, part 1 — causes, pathogenesis, diagnosis (two of three), amylase vs lipase, the revised Atlanta classification,
# the determinant-based classification, local and systemic complications and the 4-week collections, Ranson, BISAP, the CT severity index, other severity markers, imaging, ERCP and a sweep.
# No mnemonics or hooks. Driven by qpack/GI02A.md (28 question links; PANC-12 imaging asked 6 times, PANC-01 causes 5, PANC-09 BISAP 4, PANC-05 revised Atlanta 3).
# PANC-02, PANC-06 and PANC-13 have no linked question and get short explanations with [pattern] decode items.
# The card layer (gi_cardlayer.json, GI02A|…) lines and cross notes were read and the explanations agree with them; no `fix` entries exist for GI02A in trace/test/data/qbank.json (checked 20 Nov 2026).
# Fields as TOX01, plus SPINE, PRIMER and step. Table cards (no lettered parts) take parts a, b, c… in the order of the card’s rows or lines.
# Checked online on 20 Nov 2026:
#  - ACG 2024 acute pancreatitis guideline (Tenner, Am J Gastroenterol 2024; full text PDF and MDCalc summary): diagnosis by two of three (pain, lipase or amylase >3× ULN, imaging); lipase preferred,
#    amylase alone unreliable; CT/MRI reserved for unclear diagnosis or failure to improve within 48–72 h; transabdominal ultrasound in all to look for gallstones; triglycerides considered causal
#    preferably >1,000 mg/dL; tumour to be considered after 40 when no cause; repeat ultrasound, MRI and/or EUS for idiopathic AP, EUS superior with MRCP complementary; MRCP or EUS before ERCP
#    for suspected duct stones; ERCP within 24 h for cholangitis; medical therapy over ERCP within 72 h without cholangitis; risk factors BUN >20 mg/dL, haematocrit >44%, SIRS, age, obesity,
#    comorbidity; BISAP no better than BUN and SIRS; scores and imaging alone are not accurate; rectal indomethacin 100 mg for post-ERCP pancreatitis prevention (high risk).
#  - Revised Atlanta 2012 (Banks, Gut 2013; Radiopaedia summary): collections — acute peripancreatic fluid collection and acute necrotic collection in the first 4 weeks, pseudocyst and walled-off
#    necrosis (encapsulated) after 4 weeks; ‘pancreatic abscess’ abandoned; gas the best imaging sign of infection; early phase (week 1) graded by organ failure, late phase by local complications.
#  - Determinant-based classification (Dellinger, Ann Surg 2012; full text): mild = no necrosis and no organ failure; moderate = sterile necrosis and/or transient organ failure; severe = infected
#    necrosis or persistent organ failure; critical = infected necrosis and persistent organ failure; organ failure by SOFA ≥2 (or inotropes, creatinine ≥2.0 mg/dL, P/F ≤300); persistent ≥48 h.
#  - BISAP (Wu, Gut 2008; full text): BUN >25 mg/dL, impaired mental status, SIRS, age >60, pleural effusion, within 24 h; derivation 17,922, validation 18,256 admissions; mortality under 1%
#    below 2, about 2% at 2, rising from 5% to 20% at 3 or more.
#  - Balthazar CTSI (Radiology 1990; 88 patients): maximum 10; CTSI 0–3 mortality 3%, morbidity 8%; 7–10 mortality 17%, morbidity 92%.
#  - Ranson (Radiopaedia): admission age >55, WBC >16,000, glucose >200 mg/dL (11 mmol/L), LDH >350, AST >250; 48 h haematocrit fall >10%, BUN rise >5 mg/dL, calcium <8 mg/dL, PaO₂ <60,
#    base deficit >4, sequestration >6 L; mortality 0–2 <1%, 3–4 16%, ≥5 >40% (bands differ between sources).
#  - CAP lipase/amylase guidance: lipase rises in 4–8 h, peaks at 24 h, normal in 7–14 days; amylase rises in 5–8 h, normal in 1–5 days (half-life 10–12 h); amylase specificity 20–60%; lipase
#    sensitivity and specificity 80–100%; ordering both adds nothing.
#  - ALT and gallstone aetiology (BestBETs): Tenner 1994 ALT >150 IU/L specificity 96%, sensitivity 48%, PPV 95%; Levy 2005 meta-analysis ALT >3× ULN PPV 92%, sensitivity 61%.
# Second check (reviewer, 20 Nov 2026, online): modified Marshall table (MSD Manual, after Banks 2013): score 2 = P/F 201–300, creatinine 170–310 µmol/L (1.9–3.6 mg/dL), SBP <90 not
# fluid-responsive; revised Atlanta mortality with early persistent organ failure about 36–50% (GPnotebook summary of Banks 2013); APEC (Schepens, Lancet 2020, abstract): 232 patients with
# predicted severe gallstone AP (APACHE II ≥8, Imrie ≥3 or CRP >150 mg/L) without cholangitis, urgent ERCP with sphincterotomy within 24 h vs conservative, death or major complications
# 38% vs 44% (RR 0.87, 95% CI 0.64–1.18), cholangitis 2% vs 10%; gallstone Ranson (Wikipedia/Wikiwand summary of Ranson 1979/1982): age >70, WBC >18,000, glucose >220, LDH >400, AST >250;
# haematocrit fall >10%, BUN rise >2, calcium <8, base deficit >4–5, fluid >4 L, no PaO₂; urine trypsinogen-2 meta-analysis (Hepatobiliary Pancreat Dis Int 2013, 18 studies): pooled
# sensitivity 80%, specificity 92%. APACHE II ≥8 is the Atlanta 1992 cut-off; IAP/APA 2013 recommends persistent SIRS (>48 h) rather than APACHE II or CRP for prediction.
# From standard references without a fresh check (confident): CECT best at 72–96 h (WSES 2019); ESGE post-ERCP prevention (rectal diclofenac or
# indomethacin 100 mg, Ringer’s lactate, pancreatic stent in high risk); falsely normal amylase in hypertriglyceridaemia; sentinel loop and colon cut-off sign; macroamylasaemia.
# Not verified and not restated as fact: the card’s Ranson mortality bands and its 13–35% mortality figure (see FLAGS).

SPINE = [
  ("Stones, alcohol, then the rest", "Gallstones and alcohol cause most acute pancreatitis, and when neither is present the next checks are triglycerides, calcium, drugs and a recent ERCP."),
  ("Trypsin switched on too early", "Every cause ends in trypsin activated inside the acinar cell, which digests the gland and sets off the enzymes that cause fat necrosis and bleeding."),
  ("Two of three makes it", "Typical pain plus lipase or amylase above three times normal makes the diagnosis without any imaging, and lipase is the better enzyme because it is specific and stays up longer."),
  ("Grade by how long organs fail", "Revised Atlanta grades by organ failure: none is mild, failure that resolves within 48 hours or local complications is moderately severe, and failure beyond 48 hours is severe."),
  ("Predicting who will get worse", "Ranson, BISAP, APACHE II, CRP, BUN and haematocrit estimate risk early, but they predict severity; only the course of organ failure defines it."),
  ("Imaging for cause, then for necrosis", "Ultrasound on admission looks for gallstones, contrast CT after 72 hours shows necrosis and collections, and ERCP is a treatment for cholangitis, not a test."),
]

PRIMER = "The pancreas makes its digestive enzymes as inactive precursors (zymogens) and keeps a trypsin inhibitor inside the acinar cell, because trypsin is the enzyme that switches all the others on; acute pancreatitis is what happens when that protection fails. The disease runs in two phases: in the first week the harm comes from a sterile systemic inflammatory response and organ failure, and after that from local complications such as necrosis and its infection. Severity is therefore defined by organ failure and its duration, measured with the modified Marshall score (respiratory, cardiovascular and renal systems, a score of 2 or more is failure). Figures here follow the revised Atlanta classification (2012) and the ACG 2024 guideline, which the exam keys use."

L = {}

L['PANC-01'] = dict(
  sub="Acute pancreatitis → Aetiology → Causes",
  step=1,
  intro="Step 1 is the cause, because the cause decides what you do next: gallstones need ultrasound, ERCP if there is cholangitis and a cholecystectomy; triglycerides need lowering; a drug needs stopping. Five linked questions test this card, and they test the less common causes more than the common ones: post-ERCP pancreatitis twice, hypertriglyceridaemia, an ‘except’ list and the liver-test pattern of a gallstone.",
  parts=[
    ('a', "**Gallstones (40–70%).** A small stone passing through the ampulla blocks the pancreatic duct for a short time, and the gland keeps secreting against the block (PANC-02). The clue on the first day is the liver test pattern: an ALT above 150 IU/L (about three times normal) with a raised ALP and bilirubin. In Tenner’s series an ALT above 150 had a positive predictive value of 95%, but it is present in only about half, so a normal ALT does not exclude stones. Ultrasound confirms them (PANC-12)."),
    ('b', "**Alcohol (25–35%).** Alcohol injures the acinar cell directly and makes secretions viscous so that protein plugs form in small ducts; it usually takes years of heavy drinking, and an attack in a heavy drinker is often on a background of chronic pancreatitis. An AST higher than ALT points to alcohol, the reverse of the gallstone pattern."),
    ('c', "**Idiopathic, Gallstones, Ethanol, Trauma, Steroids, Mumps, Autoimmune, Scorpion sting, Hypercalcaemia and Hypertriglyceridaemia, ERCP, Drugs.** The list is used in ‘all except’ questions. Hypercalcaemia (for example, hyperparathyroidism) raises calcium inside the acinar cell and in pancreatic juice, which favours premature trypsinogen activation and calcium stones in the ducts; hyperthyroidism is not a cause, which was the GT7 answer. Pancreatic cancer is not on the list but causes pancreatitis by blocking the duct, so it counts as associated and must be looked for after 40 (PANC-12). ERCP causes pancreatitis in about 3–15% (higher in difficult cannulation, pancreatic-duct injection and young women): it is the commonest complication of ERCP, and new epigastric pain with enzymes above three times normal within hours of the procedure is the pattern."),
    ('d', "**Didanosine, valproate, ACE inhibitors, mesalamine.** Drugs cause only a few per cent of cases and are diagnosed by exclusion and by resolution on stopping. Azathioprine, thiazides, furosemide, oestrogens and tetracycline are the other classic drugs (the card’s watch line)."),
    ('e', "**Serum triglycerides: causal above 1,000 mg/dL.** ACG 2024 says triglycerides should be measured when there are no gallstones and no significant alcohol history, and taken as the cause preferably above 1,000 mg/dL. Free fatty acids released from triglyceride by pancreatic lipase injure the acinar cells and the capillaries. The stem gives it away with milky (lactescent) serum; the lipaemia can also make the measured amylase falsely normal, so lipase and the clinical picture carry the diagnosis."),
  ],
  mimic=[
    ("Post-ERCP pancreatitis vs post-ERCP cholangitis or perforation", "Pancreatitis: epigastric pain within hours with enzymes above three times normal. Cholangitis: fever, jaundice, raised ALP and bilirubin. Perforation: free gas, often retroperitoneal, on imaging."),
    ("Gallstone vs alcohol pancreatitis on day 1", "Gallstone: ALT above 150 with raised ALP and bilirubin, older woman, stones on ultrasound. Alcohol: AST above ALT, heavy drinking, often previous attacks."),
  ],
  traps=[
    ("“Post-ERCP pancreatitis is caused by contrast toxicity”", "The AIM1 key (68% right) is contrast toxicity, but the main mechanism is mechanical: papillary trauma and swelling from cannulation and hydrostatic pressure from injecting the pancreatic duct, with some chemical injury from contrast. Contrast toxicity is the best of the options offered, so accept it in that question."),
    ("Hypercalcaemia or pancreatic cancer as the ‘except’ answer", "Both are associated (calcium activates trypsinogen; a tumour blocks the duct). Hyperthyroidism is the one with no link (GT7, 66% right)."),
    ("“Milky serum and high triglycerides in a pancreatitis means alcohol caused it”", "Alcohol can raise triglycerides modestly, but lactescent serum with very high triglycerides points to hyperlipoproteinaemia as the cause (CGT6)."),
  ],
  decode=[
    ("Epigastric pain, tachycardia and raised amylase 6 hours after ERCP for duct stones [DocT QBank]", "Acute pancreatitis (87%): the commonest ERCP complication. Prevention is rectal indomethacin or diclofenac 100 mg, Ringer’s lactate and a pancreatic-duct stent in high-risk cases."),
    ("Pancreatitis with lactescent serum and very high triglycerides: aetiology [DocT GT]", "Hyperlipoproteinaemia (hypertriglyceridaemia)."),
    ("All are associated with acute pancreatitis except [DocT GT]", "Hyperthyroidism."),
    ("ALT 270 above AST with raised ALP and bilirubin [Marrow]", "Gallstones; confirm with ultrasound."),
  ],
  punch="Gallstones first and alcohol second; an ALT above 150 points to stones and AST above ALT to alcohol, and with neither, check triglycerides above 1,000, calcium, drugs and a recent ERCP.",
)

L['PANC-02'] = dict(
  sub="Acute pancreatitis → Pathogenesis → Three routes to trypsin activation",
  step=2,
  intro="Step 2 explains why such different causes produce the same disease. Whether the duct is blocked, the acinar cell is poisoned or enzyme transport goes wrong, the result is trypsin switched on inside the cell instead of in the duodenum. No real question tests this card, but it explains two findings that are asked: fat necrosis with low calcium, and haemorrhage.",
  parts=[
    ('a', "**Duct obstruction (gallstone, ampullary block, chronic alcohol): interstitial oedema, impaired flow, ischaemia.** The acinar cell keeps secreting against a closed duct; pressure rises, the gland swells and its microcirculation fails."),
    ('b', "**Acinar cell injury (alcohol, drugs, trauma, ischaemia, virus): release of pro-enzymes and lysosomal hydrolases.** The injured cell leaks its enzymes into the gland and blood."),
    ('c', "**Defective intracellular transport (metabolic, alcohol, duct obstruction): pro-enzymes delivered to lysosomes.** When zymogen granules fuse with lysosomes, the lysosomal enzyme cathepsin B converts trypsinogen to trypsin inside the cell, and the cell’s own trypsin inhibitor is overwhelmed."),
    ('d', "**Common event: premature activation of trypsin inside the acinar cell.** Trypsin activates every other zymogen, so one enzyme switched on early starts the whole cascade and the gland digests itself. The histological hallmark is acinar cell destruction."),
    ('e', "**Lipase and phospholipase: fat necrosis. Elastase: haemorrhage. Proteases: proteolysis.** Lipase splits peripancreatic fat into fatty acids that bind calcium as soaps (saponification), which is one reason the calcium falls (PANC-08). Elastase dissolves the elastic tissue of vessel walls, which is why necrotising pancreatitis can bleed into the retroperitoneum (the Grey Turner and Cullen signs, top-up)."),
  ],
  mimic=[
    ("Low calcium from saponification vs from low albumin", "Saponification lowers ionised calcium; low albumin lowers total calcium only. Both occur, and neither reflects volume."),
  ],
  traps=[
    ("“Amylase activation is the initiating event”", "Trypsin is the trigger because it activates the others; amylase is a marker, not a cause of injury."),
  ],
  decode=[
    ("Central event common to all causes of acute pancreatitis [pattern]", "Premature intracellular activation of trypsinogen to trypsin."),
    ("Enzyme responsible for fat necrosis, or for haemorrhage [pattern]", "Lipase and phospholipase for fat necrosis; elastase for vessel damage and haemorrhage."),
  ],
  punch="Every route ends in trypsin switched on inside the acinar cell; lipase then causes fat necrosis and low calcium, and elastase eats vessel walls and causes bleeding.",
)

L['PANC-03'] = dict(
  sub="Acute pancreatitis → Diagnosis → Two of three (Atlanta)",
  step=3,
  intro="Step 3 is making the diagnosis, and the rule is short: two of three. The point the exam presses is what follows from it — that a patient with typical pain and high enzymes needs no scan to make the diagnosis. That question was answered correctly by only 41% of the cohort.",
  parts=[
    ('a', "**Abdominal pain consistent with the disease.** Acute, persistent, severe epigastric pain, often radiating to the back and eased by sitting forward, because the pancreas lies on the posterior abdominal wall."),
    ('b', "**Serum amylase and/or lipase more than 3 times the upper limit of normal.** The threefold threshold is there because smaller rises occur in many other abdominal conditions and in renal failure (PANC-04)."),
    ('c', "**Characteristic findings on CT or MRI.** Imaging is needed only when one of the other two is missing: a patient who presents late with normal enzymes, or atypical pain. ACG 2024 reserves CT or MRI for an unclear diagnosis or a patient who fails to improve within 48–72 hours."),
    ('d', "**Outcome: 80–85% mild (mortality under 1–3%); about 20% moderate or severe (mortality 13–35%).** Most attacks are mild and settle in days. Death concentrates in persistent organ failure: revised Atlanta quotes about 36–50% when organ failure lasts beyond 48 hours, and the highest risk is persistent organ failure with infected necrosis (the ‘critical’ grade of PANC-06)."),
  ],
  mimic=[
    ("Pancreatitis vs perforated ulcer with a raised amylase", "A perforation can raise amylase, usually below three times normal, and the X-ray shows free gas under the diaphragm. Sudden onset with board-like rigidity favours perforation."),
    ("Pancreatitis vs aortic aneurysm or mesenteric ischaemia", "Pain eased by leaning forward with lipase above three times normal is pancreatitis (CGT4); an aneurysm or ischaemia does not raise lipase to that level and shows on CT angiography."),
  ],
  traps=[
    ("“Do a contrast CT to confirm the diagnosis”", "With pain and lipase five times normal, two criteria are met; no imaging is needed initially (41% right). A CT on day 1 adds radiation and contrast, and underestimates necrosis, which takes about 72 hours to show (PANC-12). Ultrasound is still done, but to find gallstones, not to diagnose pancreatitis; in this stem there is ‘no biliary disease’, so the key is no imaging."),
  ],
  decode=[
    ("Alcoholic, epigastric pain to the back, lipase 5× normal, no biliary disease: next diagnostic step [DocT QBank]", "No further imaging required initially (41%)."),
    ("Alcoholic, pain relieved by leaning forward, normal liver tests, lipase 520 U/L, CT shown [DocT GT]", "Pancreatitis."),
  ],
  punch="Pain plus lipase or amylase above three times normal is the diagnosis; imaging is the third criterion, used only when one of the other two is missing.",
)

L['PANC-04'] = dict(
  sub="Acute pancreatitis → Diagnosis → Amylase vs lipase",
  step=3,
  intro="Step 3 continues with the enzymes. Both rise within hours, but lipase is made almost only by the pancreas and is cleared slowly, so it is more specific and stays raised longer. Both linked questions, including the NEET 2024 recall, ask simply for the best marker: lipase.",
  parts=[
    ('a', "**Rises: amylase 2–12 hours; lipase 4–8 hours.** Both are up by the time most patients arrive, so timing of the rise rarely decides anything."),
    ('b', "**Peaks: amylase 12–72 hours; lipase 24 hours.**"),
    ('c', "**Normalises: amylase 3–4 days; lipase 8–14 days.** Amylase is a small molecule cleared by the kidney with a half-life of about 10–12 hours, so it can be back to normal by the time a late presenter arrives; lipase is reabsorbed by the renal tubule and persists. This is why lipase is the test for someone who has had pain for several days."),
    ('d', "**Specificity: amylase low (salivary gland, bowel, ovary, fat, muscle); lipase high.** Amylase is made in many tissues; its specificity is only about 20–60%, while lipase reaches 80–100% at the diagnostic threshold. ACG 2024 prefers lipase and says amylase alone is unreliable; ordering both adds nothing over lipase."),
    ('e', "**False positives: amylase in renal disease, appendicitis, cholecystitis; lipase fewer, not none — renal failure (both enzymes), bowel obstruction or ischaemia, perforated ulcer, cholecystitis, DKA.** Bowel ischaemia and perforation leak enzymes from the gut lumen into the peritoneum; renal failure slows clearance. These rises are usually below three times normal, which is why the diagnostic threshold is set at three. In macroamylasaemia, amylase bound to immunoglobulin cannot be filtered: serum amylase is high and urine amylase low, with no pancreatitis."),
    ('f', "**Urine amylase raised for up to 2 weeks; urine trypsinogen-2 dipstick sensitivity 80%, specificity 92%; enzyme level does not grade severity.** Trypsinogen-2 is a small protein that is filtered and poorly reabsorbed, so it appears in urine within hours; the 80% and 92% are the pooled figures of an 18-study meta-analysis (2013), which makes the dipstick a quick bedside aid but not good enough to replace serum lipase. The size of the rise reflects how much enzyme leaked, not how much inflammation or necrosis there is, so a lipase of 10 times normal is not worse than 4 times. Severity comes from organ failure (PANC-05) and the scores (PANC-08 to PANC-11)."),
  ],
  mimic=[
    ("Amylase raised from salivary gland vs pancreas", "Salivary (mumps, parotitis) raises amylase with a normal lipase; the pancreas raises both."),
  ],
  traps=[
    ("“A higher enzyme level means more severe pancreatitis”", "Enzyme level has no prognostic value (also the GT8 explanation); it is a diagnostic test only."),
    ("“Normal amylase on day 4 excludes pancreatitis”", "Amylase may already be normal by day 3–5; lipase stays up for one to two weeks. In hypertriglyceridaemia the amylase can also be falsely normal (PANC-01)."),
  ],
  decode=[
    ("Most sensitive and specific biochemical marker of acute pancreatitis [DocT GT]", "Serum lipase."),
    ("Marker for pancreatitis [NEET 2024]", "Lipase."),
  ],
  punch="Lipase is the test: it comes only from the pancreas and stays raised for one to two weeks, while amylase comes from many tissues and is gone in a few days; neither level tells you severity.",
)

L['PANC-05'] = dict(
  sub="Acute pancreatitis → Classification → Revised Atlanta (2012)",
  step=4,
  intro="Step 4 is grading, and revised Atlanta grades by one thing above all: how long organ failure lasts. The 48-hour line separates a transient storm from failure that will kill. Three linked questions test the scoring system that defines organ failure, the grade of a stem, and which organ failures matter most; that last one has a disputed key.",
  parts=[
    ('a', "**Mild: no organ failure, no local or systemic complications.** Usually settles within a week; mortality is very low."),
    ('b', "**Moderately severe: transient organ failure (under 48 h) and/or local or systemic complications, without persistent organ failure.** A patient with sterile necrosis and no organ failure, or one whose renal failure recovers by 36 hours, sits here. Mortality is low but the stay is long."),
    ('c', "**Severe: persistent organ failure (over 48 h), single or multiple; local complications usually present.** Persistent organ failure is the strongest predictor of death; revised Atlanta quotes about 36–50%, and multiple organ failure is worse than single. Necrosis alone does not make it severe in this system; the persistent failure does. In the AIM1 stem (necrosis with renal failure for 72 hours) the answer is severe (86% right)."),
    ('d', "**Organ failure = modified Marshall score of 2 or more in the respiratory, cardiovascular or renal system.** A score of 2 means a P/F ratio of 201–300, a creatinine of about 1.9–3.6 mg/dL (170–310 µmol/L), or a systolic pressure under 90 that does not respond to fluid. Atlanta chose modified Marshall because it is simple and needs no ventilator or drug data; the determinant-based classification uses SOFA instead (PANC-06). In the CGT2 stem (P/F under 300, creatinine 2.1, vasopressors) the system that defines persistent organ failure is modified Marshall."),
  ],
  mimic=[
    ("Modified Marshall vs SOFA vs BISAP or Ranson", "Modified Marshall defines organ failure in revised Atlanta; SOFA does it in the determinant-based system; BISAP and Ranson predict severity and cannot define it."),
    ("Transient vs persistent organ failure", "The same organ, failing for under 48 hours or for 48 hours or more. The grade cannot be final until 48 hours have passed."),
  ],
  traps=[
    ("“Hepatic and coagulation dysfunction is the combination most predictive of death”", "This is the GT5 key (50% right) but it has no guideline basis: Atlanta and modified Marshall score only respiratory, cardiovascular and renal failure, and death tracks persistent and multiple organ failure. Respiratory failure is the commonest single failure. If a persistent multi-organ, respiratory–cardiovascular–renal option is offered, pick it; with the GT5 options, accept the bank key."),
    ("“Necrosis on CT makes it severe”", "In revised Atlanta, necrosis without persistent organ failure is moderately severe; ‘necrotising pancreatitis without failure’ is a description, not a grade."),
    ("“SOFA defines organ failure in Atlanta”", "SOFA is the determinant-based system’s tool; Atlanta uses modified Marshall."),
  ],
  decode=[
    ("P/F under 300, creatinine 2.1, SBP 85 on vasopressors: best system to define persistent organ failure [DocT GT]", "Modified Marshall score."),
    ("Post-pancreatitis MODS: combination most predictive of mortality [DocT GT]", "Keyed hepatic plus coagulation dysfunction (50%); disputed — see trap."),
    ("Pancreatic necrosis with persistent renal failure for 72 hours: classification [DocT GT]", "Severe acute pancreatitis (86%)."),
  ],
  punch="Revised Atlanta grades by how long organs fail: none is mild, under 48 hours or local complications is moderately severe, and 48 hours or more, scored by modified Marshall, is severe.",
)

L['PANC-06'] = dict(
  sub="Acute pancreatitis → Classification → Determinant-based vs revised Atlanta",
  step=4,
  intro="Step 4 has a second system, published the same year. The determinant-based classification adds the local determinant, infected necrosis, as an equal partner to organ failure, which gives it a fourth grade. No real question tests it yet; the likely question is which system has a ‘critical’ grade.",
  parts=[
    ('a', "**Mild: no organ failure AND no necrosis.**"),
    ('b', "**Moderate: transient organ failure AND/OR sterile necrosis.**"),
    ('c', "**Severe: persistent organ failure OR infected necrosis.** Either determinant alone is enough. Infected necrosis without organ failure is severe here but only moderately severe in revised Atlanta."),
    ('d', "**Critical: persistent organ failure AND infected necrosis.** This combination carries the highest mortality of any group, which is why it gets its own grade."),
    ('e', "**Determinant-based: four grades, two determinants (organ failure; necrosis and its infection). Revised Atlanta: three grades, severe defined by organ failure alone.** The determinant-based system defines organ failure by SOFA 2 or more (or inotropes, creatinine 2.0 mg/dL or more, P/F 300 or less), persistent at 48 hours or more."),
  ],
  mimic=[
    ("Determinant-based ‘severe’ vs Atlanta ‘severe’", "Determinant-based: persistent organ failure or infected necrosis. Atlanta: persistent organ failure only."),
  ],
  traps=[
    ("“Revised Atlanta has a critical grade”", "Only the determinant-based system does (PANC-13 d)."),
  ],
  decode=[
    ("Persistent organ failure with infected necrosis: grade in the determinant-based classification [pattern]", "Critical."),
    ("Infected necrosis, no organ failure: grade in each system [pattern]", "Severe (determinant-based); moderately severe (revised Atlanta)."),
  ],
  punch="The determinant-based system weighs infected necrosis equally with persistent organ failure and has four grades, ending in critical when both are present; revised Atlanta has three and counts organ failure alone.",
)

L['PANC-07'] = dict(
  sub="Acute pancreatitis → Classification → Local and systemic complications",
  step=4,
  intro="Step 4 also names what can go wrong locally, because local complications move a patient from mild to moderately severe. The collections are named by two things: whether there is necrosis inside, and whether 4 weeks have passed. The one linked question turns on that 4-week line.",
  parts=[
    ('a', "**Local: acute peripancreatic fluid collection, pseudocyst, pancreatic or peripancreatic necrosis (sterile or infected).** Suspect one when pain persists or recurs, enzymes rise again, or fever and organ failure appear after initial improvement; then image."),
    ('b', "**Systemic: organ failure (respiratory, cardiovascular, renal) or exacerbation of a pre-existing disease (COPD, heart failure, chronic liver disease).** An exacerbation of a comorbidity counts as a systemic complication and is enough for moderately severe."),
    ('c', "**Interstitial oedematous: acute peripancreatic fluid collection under 4 weeks; pseudocyst over 4 weeks.** Fluid without necrosis has no wall at first; after about 4 weeks granulation tissue forms a capsule and it becomes a pseudocyst. Most early collections resolve on their own."),
    ('d', "**Necrotising: acute necrotic collection under 4 weeks; walled-off necrosis over 4 weeks.** These contain solid debris as well as fluid. Waiting for the wall is why drainage and debridement are delayed to about 4 weeks (GI02B, PANC-22). Infection is suspected from gas in the collection on CT; the term ‘pancreatic abscess’ has been abandoned."),
  ],
  mimic=[
    ("Pseudocyst vs walled-off necrosis", "Both are encapsulated and appear after 4 weeks. A pseudocyst is pure fluid after interstitial pancreatitis; walled-off necrosis contains solid debris after necrotising pancreatitis (MRI or ultrasound shows the debris best)."),
    ("Pseudocyst vs cystic neoplasm", "A pseudocyst follows an attack of pancreatitis; a mucinous cystic neoplasm has no such history and often septations or a solid component."),
  ],
  traps=[
    ("“Three weeks after pancreatitis, a well-defined anechoic collection is a pseudocyst”", "By revised Atlanta it is still an acute peripancreatic fluid collection until 4 weeks; that option was not offered, so pseudocyst (82% right) is the best answer. Walled-off necrosis is wrong because the lesion is anechoic (no debris)."),
  ],
  decode=[
    ("Abdominal fullness 3 weeks after pancreatitis, large anechoic well-defined collection [DocT QBank]", "Pancreatic pseudocyst (82%); strictly an acute peripancreatic fluid collection before 4 weeks."),
  ],
  punch="Collections are named by necrosis and by time: fluid becomes a pseudocyst and necrosis becomes walled-off necrosis once a wall forms at about 4 weeks, which is why intervention waits that long.",
)

L['PANC-08'] = dict(
  sub="Acute pancreatitis → Severity scores → Ranson’s criteria",
  step=5,
  intro="Step 5 is predicting who will get worse, and Ranson’s is the oldest score. Its weakness is built in: six of its eleven items are measured at 48 hours, so it cannot be completed until two days have passed. The one linked question asks which finding in an ARDS picture is a Ranson item.",
  parts=[
    ('a', "**On admission: age over 55, white cells over 16,000, glucose over 200 mg/dL, AST over 250, LDH over 350.** These reflect age and the intensity of the initial inflammation and cell injury."),
    ('b', "**Within 48 hours: haematocrit fall over 10%, BUN rise over 5 mg/dL, calcium under 8 mg/dL, PaO₂ under 60 mmHg, base deficit over 4, fluid needs over 6 L.** These reflect what the disease has done by 48 hours: fluid lost into the third space (the high BUN and the fluid need), lung injury (the PaO₂), shock (the base deficit) and fat necrosis (the low calcium, PANC-02). The haematocrit item is a fall, measured after resuscitation; a high haematocrit on admission (over 44%) is a different marker (PANC-11)."),
    ('c', "**Under 3: mortality 0–3%. 3–5: 11–15%. 6 or more: 40%.** Sources band these differently (another common version is 0–2 under 1%, 3–4 about 16%, 5–6 about 40%, 7 or more near 100%); the message is the same: 3 or more predicts severe disease. The card gives the non-gallstone criteria. Ranson’s gallstone version raises the cut-offs (admission: age over 70, white cells over 18,000, glucose over 220, LDH over 400, AST over 250; 48 hours: haematocrit fall over 10%, BUN rise over 2, calcium under 8, base deficit over 5 in most sources, fluid over 4 L) and has no PaO₂ item, so it has ten items, not eleven."),
  ],
  mimic=[
    ("Ranson vs BISAP", "Ranson: 11 items over 48 hours, lab-heavy. BISAP: 5 items within 24 hours, at the bedside (PANC-09). Ranson’s age cut-off is 55, BISAP’s 60."),
  ],
  traps=[
    ("“Amylase, lipase or CRP is a Ranson item”", "None is; enzymes do not grade severity (PANC-04) and CRP is a separate day-2 marker (PANC-11)."),
    ("Age over 40 or 45 as the Ranson age", "The cut-off is 55 (Marrow distractors)."),
  ],
  decode=[
    ("Severe alcoholic pancreatitis with an ARDS picture: poor prognostic sign [Marrow]", "PaO₂ under 60 mmHg (a Ranson 48-hour item)."),
  ],
  punch="Ranson has five admission items and six 48-hour items, so it is complete only at 48 hours; 3 or more predicts severe disease, and it contains no amylase, lipase or CRP.",
)

L['PANC-09'] = dict(
  sub="Acute pancreatitis → Severity scores → BISAP",
  step=5,
  intro="Step 5 continues with the bedside score. BISAP was built from about 18,000 admissions to predict death using only what is available in the first 24 hours. Four linked questions test it: two ask what is in it, one what a high score means, and one why BUN is there.",
  parts=[
    ('a', "**BUN over 25 mg/dL.** A high or rising BUN is prerenal azotaemia from fluid lost into the retroperitoneum and gut, so it measures intravascular depletion; ACG uses BUN over 20 mg/dL, or rising at 24 hours, as a risk marker on its own. In the GT8 stem (haemoconcentration, tachycardia, flat neck veins) raised BUN and creatinine is the lab finding of depletion (81% right)."),
    ('b', "**Impaired mental status.** Any disorientation, lethargy, somnolence, stupor or coma; it reflects systemic toxicity or shock."),
    ('c', "**SIRS.** Two or more of pulse over 90, respiratory rate over 20 or PaCO₂ under 32, temperature over 38 or under 36 °C, white cells over 12,000 or under 4,000. Persistent SIRS beyond 48 hours predicts organ failure and death."),
    ('d', "**Age over 60.**"),
    ('e', "**Pleural effusion.** On chest X-ray or CT; usually left-sided, from enzyme-rich fluid and capillary leak, and a marker of severe inflammation."),
    ('f', "**Score under 2: mortality 0–0.5%; 2: 2%; 3 or more: 5–20%.** In the original study mortality was under 1% below 2, about 2% at 2, and rose sharply from 5% to 20% at 3 or more, so 3 is the usual cut-off for high risk. A score of 4 therefore means a high risk of death (58% right). ACG 2024 notes that BISAP is no better than simply watching BUN and SIRS."),
  ],
  mimic=[
    ("BISAP vs Ranson items", "BISAP: BUN, mental status, SIRS, age 60, pleural effusion. Ranson: age 55, white cells, glucose, AST, LDH, then haematocrit, BUN, calcium, PaO₂, base deficit, fluid. Haematocrit, calcium and LDH are Ranson, not BISAP."),
  ],
  traps=[
    ("“CRP over 150 is part of BISAP (or of Ranson)”", "CRP is in neither; it is a separate day-2 marker (PANC-11). The key (D, 71% right) is correct, but DocT’s explanation wrongly says CRP is in Ranson."),
    ("“BISAP 4 means moderately severe pancreatitis”", "BISAP predicts mortality; it does not assign an Atlanta grade, which needs the duration of organ failure. The answer is high risk of death."),
    ("“Hypocalcaemia or a high amylase marks volume depletion”", "Low calcium comes from saponification and low albumin, and amylase has no prognostic value; BUN tracks the volume (GT8)."),
  ],
  decode=[
    ("BISAP score of 4: which is NOT a BISAP criterion — age over 60, pleural effusion, BUN over 25, CRP over 150 [DocT QBank]", "CRP over 150 (71%)."),
    ("BISAP includes — haematocrit, pleural effusion, calcium, LDH [DocT GT]", "Pleural effusion."),
    ("Haemoconcentration, tachycardia, collapsed neck veins: lab finding of intravascular depletion [DocT GT]", "Raised BUN and creatinine (81%)."),
    ("BISAP score of 4: most likely outcome [DocT GT]", "High risk of mortality (58%)."),
  ],
  punch="BISAP is five bedside items in the first 24 hours — BUN over 25, impaired mental status, SIRS, age over 60, pleural effusion — and 3 or more marks a sharp rise in the risk of death.",
)

L['PANC-10'] = dict(
  sub="Acute pancreatitis → Severity scores → CT severity index (Balthazar)",
  step=5,
  intro="Step 5 also has an imaging score. The CT severity index adds two things the contrast CT shows: how inflamed the gland and its surroundings are, and how much of the gland has died. Necrosis is weighted more because dead pancreas is what becomes infected and what kills. Both linked questions show a CT and both were often missed (39% and 60%); one key is disputed.",
  parts=[
    ('a', "**Normal pancreas 0 points; no necrosis 0.** Balthazar grade A."),
    ('b', "**Enlarged pancreas 1; necrosis under 30%: 2.** Grade B is focal or diffuse enlargement."),
    ('c', "**Peripancreatic inflammation 2; necrosis 30–50%: 4.** Grade C is stranding in the peripancreatic fat without a collection."),
    ('d', "**One fluid collection 3; necrosis over 50%: 6.** Grade D is a single collection. Necrosis is seen as parenchyma that fails to enhance with contrast, which is why the scan must wait until about 72 hours, when necrosis has declared itself (PANC-12)."),
    ('e', "**Two or more collections 4.** Grade E also includes gas in or next to the pancreas."),
    ('f', "**Maximum 10. Mortality 0–1: 0%; 2–3: 3%; 4–6: 6%; 7–10: 17%.** In Balthazar’s 1990 series a CTSI of 0–3 had 3% mortality and 8% morbidity, and 7–10 had 17% mortality and 92% morbidity. A CTSI of 3 or more needs a follow-up scan (PANC-12 c)."),
  ],
  mimic=[
    ("Necrotising vs interstitial oedematous pancreatitis on CT", "Necrotising: areas of the gland that do not enhance. Interstitial: the whole gland enhances, with surrounding stranding or fluid."),
    ("Balthazar CTSI vs modified CTSI", "The modified index (Mortele) scores inflammation 0, 2 or 4, necrosis 0, 2 (up to 30%) or 4 (over 30%) and adds 2 for extrapancreatic complications; the card and the questions use Balthazar."),
  ],
  traps=[
    ("“Day 4, hypotension, rising white cells, CT: interstitial oedematous or haemorrhagic pancreatitis”", "Non-enhancing gland on a day-4 contrast CT in a deteriorating patient is necrosis (only 39% right). ‘Haemorrhagic pancreatitis’ is not an Atlanta category, and a pseudocyst cannot form before 4 weeks."),
    ("“A peripancreatic collection plus 30–50% necrosis scores 6”", "This is the DocT key (60% right), which scored the collection as 2. In Balthazar a single collection is 3, so collection plus 30–50% necrosis is 7. If the CT shows a discrete collection, the answer is 7; if only peripancreatic inflammation, 6."),
  ],
  decode=[
    ("Gallstone pancreatitis, day 4, hypotension and rising white cells; contrast CT shown [DocT QBank]", "Pancreatic necrosis (39%)."),
    ("Day 5 worsening pain and fever; CT shown; approximate CTSI [DocT QBank]", "Keyed 6 (60%); recalculate from the findings — collection 3 or inflammation 2, plus necrosis 2, 4 or 6."),
  ],
  punch="The CT severity index adds Balthazar grade (0–4) to necrosis (0, 2, 4 or 6) for a maximum of 10; necrosis weighs more, and 7 or more carries about 17% mortality.",
)

L['PANC-11'] = dict(
  sub="Acute pancreatitis → Severity scores → APACHE II, CRP, haematocrit and BUN",
  step=5,
  intro="Step 5 ends with the markers that are not dedicated pancreatitis scores. Each has its moment: haematocrit and BUN on admission, APACHE II at any time, CRP on day 2. Two linked questions test them; the APACHE II question was missed by more than half the cohort.",
  parts=[
    ('a', "**APACHE II above 8: severe disease, likely organ failure.** The usual cut-off is 8 or more (Atlanta 1992). APACHE II can be calculated on admission and repeated daily, which is its advantage over Ranson; its drawback is complexity. A score of 18 in pancreatitis means predicted severe pancreatitis (46% right). The cut-off is still in use: the APEC trial (2020) defined predicted severe disease as APACHE II 8 or more, Imrie 3 or more, or CRP over 150 mg/L."),
    ('b', "**C-reactive protein above 150 mg/L: predicts pancreatic necrosis (sensitivity and specificity 80%).** CRP is made by the liver under interleukin-6 drive, so it lags the inflammation and peaks at 48–72 hours; measured on admission it is too early. It is not part of BISAP or Ranson."),
    ('c', "**Indication for ICU: persistent organ dysfunction or failure despite adequate fluid resuscitation.** The trigger is failure that does not respond to fluid, not a score."),
    ('d', "**Simple early markers: haematocrit above 44% and a rising BUN.** Both measure haemoconcentration from fluid lost into the third space. A haematocrit that fails to fall with fluids, or a BUN that rises at 24 hours, signals a worse course (ACG 2024)."),
  ],
  mimic=[
    ("Prediction vs classification", "APACHE II, CRP, BISAP and Ranson predict severity early; revised Atlanta classifies it, and only after 48 hours of organ failure."),
  ],
  traps=[
    ("“APACHE II 18 means moderate systemic illness”", "In a pancreatitis stem, APACHE II of 8 or more predicts severe pancreatitis; the key is severe (46% right). The generic ‘systemic illness’ options are distractors."),
    ("“CRP over 150 is a BISAP item”", "It is a separate marker, best at 48 hours (PANC-09)."),
  ],
  decode=[
    ("Alcoholic pancreatitis in ICU, APACHE II 18: interpretation [DocT QBank]", "Severe pancreatitis (46%)."),
    ("Which is NOT a BISAP criterion — CRP over 150 among the options [DocT QBank]", "CRP over 150 (71%)."),
  ],
  punch="APACHE II of 8 or more predicts severe disease at any time, CRP over 150 at 48 hours predicts necrosis, and a haematocrit over 44% or a rising BUN on day 1 shows the third-space loss.",
)

L['PANC-12'] = dict(
  sub="Acute pancreatitis → Imaging → Which test, and when",
  step=6,
  intro="Step 6 is imaging, the most-asked card in the deck (six questions). The rule is that each test has a job and a time: ultrasound finds the cause on day 1, contrast CT finds necrosis after 72 hours, MRI and EUS answer questions CT cannot. Most wrong answers come from imaging too early or ordering ERCP as a test.",
  parts=[
    ('a', "**Ultrasound: to find the cause (gallstones), on admission or within 48 hours.** ACG 2024 suggests it in every patient, because a gallstone cause changes management (ERCP if cholangitis, cholecystectomy before discharge). Bowel gas often hides the pancreas itself, so ultrasound is not used to grade the disease. A plain abdominal film is not a diagnostic test either; it may show a sentinel loop (a dilated jejunal loop in the left upper quadrant from localised ileus) or the colon cut-off sign, but its real job is to exclude free gas."),
    ('b', "**Contrast CT: gold standard for grading, necrosis and collections; best after 72 hours.** Necrosis is gland that does not enhance, and it takes about 72 hours (WSES: 72–96 hours) to demarcate, so an early scan underestimates it. ACG 2024 reserves CT for an unclear diagnosis or a patient not improving within 48–72 hours. A non-contrast CT cannot show necrosis."),
    ('c', "**Follow-up CT: 7–10 days after the first scan if the CT severity index is 3 or more; on deterioration; before an intervention.** In practice the trigger that matters is clinical: new fever, organ failure or sepsis prompts a scan to look for infected necrosis (gas) or bleeding."),
    ('d', "**MRI advantages: no radiation or iodinated contrast (pregnancy, kidney injury); shows duct disruption and the cause.** MRCP shows bile duct stones and the pancreatic duct (divisum, strictures, a disconnected duct), and MRI shows solid debris in a collection better than CT."),
    ('e', "**MRI disadvantages: slower; less sensitive for gas in collections.** A critically ill patient may not tolerate a long scan, and gas, the sign of infection, is seen best on CT."),
    ('f', "**Endoscopic ultrasound: when CT and ultrasound miss common bile duct stones.** EUS finds microlithiasis, sludge and small tumours. In idiopathic pancreatitis, ACG 2024 advises repeat ultrasound, MRI and/or EUS, calls EUS superior with MRCP complementary, and says a tumour must be considered after 40. ERCP is not a diagnostic test: it causes pancreatitis in 3–15%."),
  ],
  table=dict(
    title="Which test answers which question",
    head=["Question", "Test", "When"],
    rows=[
      ["Is it gallstones?", "**ultrasound**", "admission, within 48 h"],
      ["Is there necrosis or a collection?", "**contrast CT**", "after 72 h, or on deterioration"],
      ["Pregnant or kidney injury; duct anatomy?", "**MRI/MRCP**", "when CT is unsuitable"],
      ["Idiopathic: microlithiasis, small tumour?", "**EUS**", "after the attack; especially over 40"],
      ["Cholangitis or persisting obstruction?", "**ERCP** (treatment)", "within 24 h for cholangitis"],
    ],
  ),
  mimic=[
    ("EUS vs MRCP in idiopathic pancreatitis", "EUS has the higher yield for microlithiasis and small tumours; MRCP (secretin-enhanced) is better for duct anatomy such as pancreas divisum. Over 40, EUS comes first."),
    ("Acute vs chronic pancreatitis imaging", "In suspected chronic pancreatitis (recurrent attacks, new diabetes, smoker), CT comes first for calcification and duct dilatation, with MRCP or EUS if CT is normal (Marrow)."),
  ],
  traps=[
    ("“Contrast CT now to diagnose it”", "Pain and lipase already make the diagnosis; no further imaging is needed initially (41% right, PANC-03)."),
    ("“Day 4 CT in a deteriorating patient shows interstitial pancreatitis or haemorrhagic pancreatitis”", "The scan is shown because the patient deteriorated after 72 hours: the answer is necrosis (39% right, PANC-10)."),
    ("“MRCP is the first test for idiopathic recurrent pancreatitis”", "This is the DocT key (61% right) and MRCP is acceptable, but ACG and AGA rank EUS at least level with MRCP and ahead of it after 40. If both are offered and the patient is over 40, pick EUS; if only MRCP is offered, take it."),
    ("“The sentinel loop means small bowel obstruction”", "A single dilated jejunal loop in the left upper quadrant of an alcoholic with epigastric pain is localised ileus next to the inflamed pancreas (66% right)."),
  ],
  decode=[
    ("Alcoholic, lipase 5× normal, no biliary disease: next step in diagnosis [DocT QBank]", "No further imaging required initially (41%)."),
    ("Persistent pain at 72 hours: best test for necrosis or collections [DocT QBank]", "Contrast-enhanced CT (80%)."),
    ("Alcoholic, epigastric pain, dilated air-filled loop in the left upper quadrant on X-ray [DocT QBank]", "Acute pancreatitis — sentinel loop (66%)."),
    ("Idiopathic recurrent pancreatitis, normal ultrasound: next anatomical test [DocT QBank]", "Keyed MRCP (61%); EUS equally or more correct after 40."),
    ("Day 4 deterioration, contrast CT shown [DocT QBank]", "Pancreatic necrosis (39%)."),
    ("Recurrent pancreatitis, new diabetes, thin smoker: diagnostic test [Marrow]", "CT abdomen (chronic pancreatitis; also excludes a tumour)."),
  ],
  punch="Ultrasound on day 1 finds gallstones, contrast CT after 72 hours finds necrosis, MRI and EUS answer the questions CT cannot, and ERCP treats rather than diagnoses.",
)

L['PANC-13'] = dict(
  sub="Acute pancreatitis → Imaging → ERCP and a true/false sweep",
  step=6,
  intro="Step 6 ends with ERCP and a sweep of the deck’s commonest wrong beliefs. ERCP is not routine in gallstone pancreatitis: it is indicated for cholangitis (within 24 hours, ACG 2024) or a bile duct that stays blocked. The APEC trial (Lancet 2020) showed that urgent ERCP in predicted severe biliary pancreatitis without cholangitis did not reduce major complications or death (38% vs 44%), because by the time the patient arrives the stone has usually passed into the duodenum; it did reduce later cholangitis (2% vs 10%), which shows that ERCP treats the bile duct, not the pancreas. No real question tests this card; its statements are the distractors of other cards.",
  parts=[
    ('a', "**False: CT is not required — two of three, imaging optional.** See PANC-03."),
    ('b', "**False: lipase lasts longer.** Amylase is cleared in days, lipase in one to two weeks (PANC-04)."),
    ('c', "**False: persistent organ failure means over 48 hours.** PANC-05."),
    ('d', "**False: ‘critical’ is in the determinant-based classification only.** PANC-06."),
    ('e', "**False: BISAP has five items.** Ranson has eleven (PANC-08, PANC-09)."),
    ('f', "**True: over 50% necrosis scores 6 on the CT index.** PANC-10."),
    ('g', "**False: CT is best after 72 hours.** Necrosis needs time to demarcate (PANC-12)."),
  ],
  mimic=[
    ("Gallstone pancreatitis with cholangitis vs without", "With cholangitis (fever, jaundice, raised bilirubin): ERCP within 24 hours. Without: medical treatment, and ERCP only for persisting obstruction; MRCP or EUS first if a duct stone is suspected."),
  ],
  traps=[
    ("“Early ERCP for every patient with gallstone pancreatitis”", "Only for cholangitis or persisting obstruction; APEC showed no benefit without cholangitis, and ERCP itself causes pancreatitis."),
  ],
  decode=[
    ("Biliary pancreatitis: indication for urgent ERCP [pattern]", "Cholangitis (within 24 hours) or persisting biliary obstruction."),
    ("True or false sweep of thresholds: 48 hours, five BISAP items, 72-hour CT [pattern]", "Each threshold as on the card."),
  ],
  punch="ERCP is for cholangitis or a blocked duct, not for every gallstone pancreatitis; and the numbers to hold are two of three, 48 hours, five BISAP items, 6 points for over 50% necrosis and CT after 72 hours.",
)

FLAGS = {
  'PANC-01': "Card is correct. AIM1 key ‘pancreatic duct contrast toxicity’ for post-ERCP pancreatitis: the main mechanism is mechanical (papillary trauma, hydrostatic injection pressure) with some chemical injury; contrast toxicity is only the best of the options. Marrow’s ALT >150 = gallstone point is added in part a (Tenner 1994 PPV 95%, sensitivity 48%).",
  'PANC-03': "d: ‘13–35%’ for moderate or severe disease could not be traced; revised Atlanta quotes about 36–50% for persistent organ failure (severe), with moderately severe much lower. The explanation restates the card and gives the Atlanta figure.",
  'PANC-05': "Card is correct. GT5 key (hepatic + coagulation dysfunction most predictive of death in MODS) has no guideline basis; Atlanta/Marshall count respiratory, cardiovascular and renal failure, and death tracks persistent and multiple organ failure. Trap says so.",
  'PANC-07': "Card is correct. DocT QBank keys ‘pseudocyst’ at 3 weeks; by revised Atlanta it is still an acute peripancreatic fluid collection until 4 weeks (not offered), so pseudocyst is only the best option.",
  'PANC-08': "Mortality bands vary by source; the card’s (under 3: 0–3%, 3–5: 11–15%, 6+: 40%) is a textbook version, another common one is 0–2 <1%, 3–4 ~16%, 5–6 ~40%, 7+ ~100%. Card lists the non-gallstone criteria; the gallstone set differs (age >70, no PaO₂).",
  'PANC-09': "Card is correct. DocT QBank explanation (CRP question) wrongly puts CRP in Ranson; the key itself is right. Card mortality ‘under 2: 0–0.5%’ is consistent with Wu 2008 (under 1%).",
  'PANC-10': "Card is correct. DocT QBank CTSI key of 6 scores a peripancreatic collection as 2; Balthazar scores one collection 3, so collection + 30–50% necrosis = 7. Pick 7 if a discrete collection is shown, 6 if only inflammation.",
  'PANC-11': "a: the standard APACHE II cut-off is 8 or more (Atlanta 1992), the card says ‘above 8’; minor.",
  'PANC-12': "Card is correct. DocT QBank keys MRCP as the sole first-line test in idiopathic recurrent pancreatitis; ACG 2024 calls EUS superior (MRCP complementary) and stresses tumour exclusion after 40. Pick EUS if both are offered and the patient is over 40.",
}
