# GI concept page content (22 Nov 2026): pancreatitis, gut failure, mesenteric ischaemia, abdominal pressure.
# Card question and watch text from Drive cards.jsonl; the answer is built from the explanation's
# bold restatements, which keep the final card wording part by part (cardfix already applied).

PAGE = dict(title='GI · NEET-SS, with tricks', doc='GI (pancreas, gut, ischaemia, abdominal pressure) · NEET-SS concept page')

C = {}  # (deck, code) -> (q, watch)
C[('GI02A', 'PANC-01')] = ("**Acute pancreatitis: causes.**\na Commonest\nb Second\nc The full list\nd Drugs named in your notes\ne No gallstones, no alcohol: what to check", "Azathioprine, thiazides, furosemide, oestrogens and tetracycline are the other classic drugs.")
C[('GI02A', 'PANC-03')] = ("**Diagnosis (Atlanta): two of three.**", "If pain and enzymes are both present, imaging is NOT needed for diagnosis. Highest risk of death: persistent organ failure with infected necrosis.")
C[('GI02A', 'PANC-04')] = ("**Amylase vs lipase:**", "Lipase stays up longer: the better test in a late presenter. Urine amylase is raised for up to 2 weeks. Urine trypsinogen-2 dipstick: sensitivity 80%, specificity 92%. Enzyme LEVEL does not grade severity.")
C[('GI02A', 'PANC-05')] = ("**Revised Atlanta classification (2012):**", "The cut-off is 48 HOURS. Organ failure = modified Marshall score of 2 or more in the respiratory, cardiovascular or renal system.")
C[('GI02A', 'PANC-07')] = ("**Complications of acute pancreatitis:**", "The 4-week collection table explains the timing of drainage.")
C[('GI02A', 'PANC-08')] = ("**Ranson's criteria (11):**", "Five at admission, six at 48 hours: it cannot be completed before 48 hours. Amylase and lipase are not in it.")
C[('GI02A', 'PANC-09')] = ("**BISAP score:**", "Five items, scored in the first 24 hours: the bedside score. Your notes give 2 as the significant cut-off; most sources use 3 or more. Age cut-off is 60 here, 55 in Ranson.")
C[('GI02A', 'PANC-10')] = ("**CT severity index (Balthazar):**", "Necrosis carries more points (6) than inflammation (4). A CT severity index of 3 or more needs a follow-up scan.")
C[('GI02A', 'PANC-11')] = ("**Other severity markers:**\na APACHE II\nb C-reactive protein\nc Indication for ICU\nd Simple early markers", "CRP peaks at 48–72 hours, so it is a day-2 marker.")
C[('GI02A', 'PANC-12')] = ("**Imaging in acute pancreatitis:**\na Ultrasound\nb Contrast CT\nc Follow-up CT\nd MRI: advantages\ne MRI: disadvantages\nf Endoscopic ultrasound", "An early CT under-estimates necrosis: necrosis takes 72 hours to demarcate. Early CT is for diagnostic doubt only.")
C[('GI02B', 'PANC-14')] = ("**Fluid resuscitation in acute pancreatitis:**\na Fluid of choice and why\nb The traditional teaching\nc Its risks\nd Current practice", "Avoid Ringer's lactate only in hypercalcaemic pancreatitis.")
C[('GI02B', 'PANC-17')] = ("**Pain and nutrition:**\na Analgesia\nb When to avoid NSAIDs\nc Epidural\nd Route of feeding and why\ne Mild disease\nf Tube feeding\ng Parenteral nutrition", "Nasogastric feeding is as good as nasojejunal. Probiotics: shorter stay only; no effect on other outcomes.")
C[('GI02B', 'PANC-18')] = ("**Antibiotics in acute pancreatitis:**\na Prophylaxis\nb Indication\nc The diagnostic difficulty\nd Guiding marker\ne Drug of choice\nf Antifungals", "Gas in a collection on CT is the best imaging sign of infected necrosis; routine needle aspiration is no longer advised.")
C[('GI02B', 'PANC-20')] = ("**The lung in pancreatitis:**\na Why ARDS develops\nb The enzyme and its target\nc Ventilation\nd Other findings", "")
C[('GI02B', 'PANC-21')] = ("**Ventilating with intra-abdominal hypertension:**\na Fraction of abdominal pressure transmitted to the thorax\nb Mechanics\nc Tidal volume\nd PEEP\ne Driving pressure\nf Plateau pressure\ng The tool that settles it", "Two corrections: this one raises the plateau TARGET; the IAH chapter corrects the MEASURED plateau (plateau − 0.5 × IAP): IAH-09.")
C[('GI02B', 'PANC-22')] = ("**Necrotising pancreatitis: the step-up approach.**", "Step-up vs open surgery (PANTER): less organ failure, fewer incisional hernias, less new-onset diabetes. VARD = video-assisted retroperitoneal debridement.")
C[('GI02B', 'PANC-23')] = ("**Indications to intervene on a collection without proven infection:**", "The two numbers: 4 weeks and 8 weeks.")
C[('GI02B', 'PANC-24')] = ("**Surgery and cholecystectomy:**\na Indications for surgery\nb Mild gallstone pancreatitis\nc Severe pancreatitis", "Bleeding (pseudoaneurysm): angio-embolisation first, surgery second.")
C[('GI03', 'GUT-03')] = ("**The gut as the “motor” of multiple organ failure:**", "Enteral feeding preserves villus architecture and reduces translocation: the reason to feed early.")
C[('GI03', 'GUT-05')] = ("**Imaging the ICU abdomen:**\na Ultrasound\nb Abdominal X-ray\nc Dilated bowel: the 3-6-9 rule\nd High risk of perforation\ne What to look for on contrast CT", "")
C[('GI03', 'GUT-07')] = ("**Treating gastroparesis:**\na Prokinetics and their receptors\nb Non-drug measures\nc Indications for a post-pyloric tube\nd Duration of prokinetics", "ESICM: a single residual over 200 mL is high; hold gastric feeds above 500 mL. Erythromycin's effect fades by 72 hours; it prolongs QT.")
C[('GI03', 'GUT-08')] = ("**Bowel sounds, paralysis and Ogilvie's syndrome:**\na How to auscultate\nb Lower GI paralysis\nc Hyperperistalsis suggests\nd Ogilvie's syndrome\ne Its drug\nf Preventing paralysis", "Neostigmine 2 mg IV over 3–5 minutes with ECG monitoring and atropine at hand; colonoscopic decompression if it fails or the caecum exceeds 12 cm.")
C[('GI03', 'GUT-09')] = ("**Diarrhoea in the ICU: definition.**", "First steps: stop laxatives and prokinetics, review drugs and feed, exclude C. difficile.")
C[('GI03', 'GUT-12')] = ("**Management by AGI grade:**", "Re-evaluate 6-hourly at first, then 12-hourly. Watch for refeeding syndrome when feeding restarts.")
C[('GI04', 'MES-06')] = ("**Risk factors and history:**\na Source of most emboli\nb Patient factors\nc ICU settings\nd History pointing to thrombosis\ne History pointing to venous thrombosis", "")
C[('GI04', 'MES-08')] = ("**Acute small bowel ischaemia vs acute colonic ischaemia:**", "")
C[('GI04', 'MES-10')] = ("**Gastrointestinal tonometry:**\na Principle\nb Measurement\nc Normal\nd Standing", "It is rarely used in practice: slow, and confounded by feed and acid.")
C[('GI04', 'MES-11')] = ("**Imaging:**\na Plain film\nb Doppler ultrasound\nc Test of choice\nd Contrast rule\ne CT signs\nf Normal CT, high suspicion\ng Peritonitis", "Do not withhold contrast CT for kidney injury when the diagnosis is suspected.")
C[('GI04', 'MES-13')] = ("**Treatment by cause and by peritonitis:**", "Endovascular therapy has no role once peritonitis is present. Resect only clearly dead bowel, leave the abdomen open, and take a SECOND LOOK.")
C[('GI05', 'IAH-01')] = ("**Intra-abdominal pressure:**\na Definition\nb Normal\nc Chronically raised baseline\nd Gold standard\ne Frequency", "")
C[('GI05', 'IAH-02')] = ("**Measuring bladder pressure (modified Kron):**", "Children: 1 mL/kg, minimum 3 mL, maximum 25 mL; your notes print 0.5 mL/kg. More than 25 mL falsely raises the reading.")
C[('GI05', 'IAH-03')] = ("**Definitions and grades:**", "Compartment syndrome is NOT a grade: it is pressure plus organ failure. Hypertension alone does not predict organ failure.")
C[('GI05', 'IAH-04')] = ("**Abdominal perfusion pressure:**\na Formula\nb Target\nc The renal equivalent", "Abdominal pressure counts twice in the filtration gradient, which is why the kidney fails first. WSACS 2013 made no formal recommendation on using perfusion pressure as a target.")
C[('GI05', 'IAH-08')] = ("**End-organ effects:**", "The gut effect is a vicious circle: oedema raises pressure, pressure causes more oedema.")
C[('GI05', 'IAH-10')] = ("**Medical management: five options.**", "Start at IAP of 12 or more. Enteral feed is minimised while pressure is high.")
C[('GI05', 'IAH-11')] = ("**The WSACS algorithm:**\na IAP 12 or more\nb IAP over 20 with new organ failure\nc Primary compartment syndrome\nd Secondary or recurrent\ne Resolution", "No exact pressure threshold for opening the abdomen is established: generally persistent grade III–IV with organ dysfunction.")

# decided flags (22 Nov): patch the bold leads where the card wording is outdated
LEAD_FIX = {
('GI03', 'GUT-07', 'd'): 'Short course: 24–48 h, stop by day 3 (ESPEN 2023); older texts allow up to 5 days. Tachyphylaxis either way.',
('GI03', 'GUT-08', 'a'): 'Auscultate for at least 1 minute in at least two quadrants, repeated (ESICM 2012).',
}
WHY_FIX = {
('GI03', 'GUT-07', 'd'): (', which is shorter than the card’s limit (see FLAGS)', ''),
('GI03', 'GUT-08', 'a'): (' (see FLAGS)', ''),
}

GROUPS = [
dict(id='PAN', title='Acute pancreatitis', decks=['GI02A', 'GI02B'], primer='GI02A',
 map=dict(title='Pancreatitis: where it goes wrong and where you act', arrow='leads to', kb='what goes wrong', ka='what you do', ki='✓', levels=[
  ('Trigger', 'stones, alcohol, triglycerides, calcium, ERCP, drugs', ['Duct obstruction, acinar injury or faulty enzyme transport'], ['Ultrasound for stones on day 1; triglycerides if no stones or alcohol', 'ERCP only for cholangitis or a blocked duct']),
  ('Acinar cell', 'trypsin switched on inside the cell', ['Lipase: fat necrosis, low calcium', 'Elastase: bleeding', 'Phospholipase A₂: surfactant loss'], ['Diagnose: pain + lipase > 3× normal (two of three)']),
  ('Whole body, week 1', 'sterile SIRS', ['Organ failure (lung first): under or over 48 h sets the grade'], ['Moderate Ringer’s, analgesia, feed by day 3', 'No prophylactic antibiotics']),
  ('Gland, weeks 2–4 and later', 'necrosis and collections', ['Infected necrosis (gas on CT)', 'Bleeding pseudoaneurysm', 'Abdominal compartment syndrome'], ['Carbapenem; step-up after the wall forms (~4 weeks)', 'Embolise a bleed first'])],
  feedback='Two waves of death: early from organ failure, late from infected necrosis. Every timing rule (72 h, 48 h, day 3, 4 weeks) comes from that calendar.'),
 drill=[
  ("Typical pain, lipase 4× normal, no CT yet", "Acute pancreatitis", "Two of three criteria; imaging is not needed."),
  ("Day 1: ALT 420, AST 180", "Gallstone pancreatitis", "ALT > 150 points to stones; ultrasound next."),
  ("Respiratory failure that resolves at 30 h, peripancreatic collection", "Moderately severe (Revised Atlanta)", "Transient organ failure and/or local complications."),
  ("Renal failure persisting for 4 days", "Severe (Revised Atlanta)", "Organ failure beyond 48 h."),
  ("Persistent organ failure plus infected necrosis", "Critical (determinant-based)", "‘Critical’ exists only in the determinant-based system."),
  ("Encapsulated fluid-only collection at 6 weeks after oedematous pancreatitis", "Pseudocyst", "Fluid + wall + > 4 weeks."),
  ("Necrotic collection without a wall on day 10", "Acute necrotic collection", "Walled-off necrosis only after about 4 weeks."),
  ("Week 3: new deterioration and gas in the collection", "Infected necrosis", "Carbapenem, then step-up (drain first)."),
  ("Day 5: fluctuating confusion and myoclonus; glucose and sodium normal", "Pancreatic encephalopathy", "A diagnosis of exclusion: give thiamine to cover Wernicke’s."),
  ("Day 3: bruising of the flanks", "Grey Turner’s sign", "Retroperitoneal blood from haemorrhagic necrotising pancreatitis; seen in < 5%."),
 ]),
dict(id='GUT', title='The gut in critical illness', decks=['GI03'], primer='GI03',
 map=dict(title='The ICU gut: where it fails and what you do', arrow='leads to', kb='what goes wrong', ka='what you do', ki='✓', levels=[
  ('Splanchnic flow', 'cut first when output falls', ['Villus tip hypoxia: the mucosa fails first, lactate rises late'], ['Restore flow; avoid needless vasoconstriction']),
  ('Mucosal barrier', 'mucin, tight junctions, secretory IgA', ['Translocation; toxic lymph reaches the lung first'], ['Early enteral feeding']),
  ('Motility', 'stomach, small bowel, colon', ['Gastroparesis, paralysis (3 days), Ogilvie’s'], ['Correct causes → erythromycin → post-pyloric tube', 'Neostigmine for Ogilvie’s']),
  ('Whole-gut grade', 'AGI I–IV', ['Grade III failure; grade IV with distant organ failure'], ['Feed → treat → search → operate'])],
  feedback='The gut is the motor of multiple organ failure, and feeding is the cheapest way to protect its barrier.'),
 drill=[
  ("No stool for 3 days, no mechanical obstruction", "Lower GI paralysis", "Correct causes, cut opioids, laxatives."),
  ("Massive colonic dilatation, caecum 13 cm, no obstruction on CT", "Ogilvie’s at risk of perforation", "Neostigmine, then colonoscopic decompression."),
  ("Gastric residual 600 mL despite erythromycin", "Failed prokinetic: post-pyloric feeding", "Hold gastric feed above 500 mL."),
  ("Persistent feed intolerance, IAP 17, no other organ failure", "AGI grade III", "Search for a hidden abdominal cause."),
  ("Bowel ischaemia with shock", "AGI grade IV", "Stop enteral feed and intervene."),
  ("Diarrhoea stops when the feed is held", "Osmotic diarrhoea", "Wide osmotic gap (> 100)."),
  ("Litres of watery stool despite fasting", "Secretory diarrhoea", "Narrow gap (< 50); test for infection."),
  ("Gas under the right hemidiaphragm with haustra in it, patient well", "Chilaiditi sign", "Colon between liver and diaphragm, not free air."),
 ]),
dict(id='MES', title='Mesenteric ischaemia', decks=['GI04'], primer='GI04',
 map=dict(title='Mesenteric ischaemia: where it goes wrong and what you do', arrow='leads to', kb='what goes wrong', ka='what you do', ki='✓', levels=[
  ('Arteries and veins', 'coeliac, SMA, IMA; mesenteric veins', ['Embolus beyond the middle colic', 'Thrombosis at the SMA origin', 'Venous thrombosis'], ['Heparin early', 'Endovascular if no peritonitis; bypass/stent for thrombosis']),
  ('Microcirculation', 'vasospasm in low flow', ['Non-occlusive (NOMI): shock, high-dose vasopressors'], ['Restore flow, stop constrictors, intra-arterial papaverine']),
  ('Mucosa → wall', 'villus tip first, then transmural', ['Lactate late; pneumatosis + portal venous gas = dead bowel'], ['Biphasic CT angiography now; peritonitis → laparotomy, second look']),
  ('Reperfusion', 'xanthine oxidase free radicals', ['Hyperkalaemia, acidosis, hypotension'], ['Anticipate when flow returns'])],
  feedback='Pain out of proportion to a soft abdomen is the window; once there is peritonism, the bowel is dead.'),
 drill=[
  ("AF, sudden severe periumbilical pain, soft abdomen", "Embolic acute mesenteric ischaemia", "CT angiography at once."),
  ("Months of post-prandial pain and weight loss, now acute", "Thrombotic AMI (on chronic ischaemia)", "Stent or antegrade bypass."),
  ("After cardiac surgery on high-dose noradrenaline, rising lactate, patent SMA", "Non-occlusive mesenteric ischaemia", "Restore flow, stop constrictors, papaverine."),
  ("Thrombophilia, pain waxing and waning over days", "Mesenteric venous thrombosis", "Heparin, then 3–6 months of anticoagulation."),
  ("Older, mild left-sided pain, bloody diarrhoea within 24 h, not very sick", "Colonic ischaemia", "Colonoscopy, not CT angiography."),
  ("Pneumatosis with portal venous gas", "Transmural infarction", "Laparotomy."),
  ("Widening gastric-to-arterial PCO₂ gap", "Gut mucosal ischaemia", "Tonometry: CO₂ not washed out."),
 ]),
dict(id='IAH', title='Abdominal pressure', decks=['GI05'], primer='GI05',
 map=dict(title='Abdominal pressure: where it rises and what it does', arrow='acts on', kb='what goes wrong', ka='what you do', ki='✓', levels=[
  ('Abdominal contents', 'fluid, blood, oedema, gas', ['More contents: ascites, ileus, packs, capillary leak'], ['Drain, decompress the gut, stop the positive balance']),
  ('Abdominal wall', 'compliance', ['Burn eschar, tight closure, tense muscles'], ['Sedation, analgesia, neuromuscular block; head of bed ≤ 30°']),
  ('Organs inside', 'APP = MAP − IAP', ['Kidney first (MAP − 2 × IAP): oliguria at 15, anuria at 30', 'Gut flow falls'], ['Keep APP ≥ 60']),
  ('Chest and brain', 'about half transmitted', ['CVP, wedge and plateau read falsely high; ICP rises'], ['Use transmural values (− 0.5 × IAP)'])],
  feedback='The abdomen is a closed box: once its compliance is used up, a little more volume gives a lot more pressure.'),
 drill=[
  ("IAP 14 mmHg", "IAH grade I", "12–15."),
  ("IAP 23 sustained, new oliguria", "Abdominal compartment syndrome", "> 20 with new organ dysfunction."),
  ("IAP 28, no new organ failure", "IAH grade IV (not ACS)", "ACS needs organ failure."),
  ("MAP 70, IAP 15", "APP 55 (low); filtration gradient 40", "APP = MAP − IAP; FG = MAP − 2 × IAP."),
  ("Damage-control laparotomy with packs, IAP 25, anuria", "Primary ACS", "Decompress early."),
  ("Burns, 15 L of crystalloid, IAP 24, oliguria", "Secondary ACS", "Medical measures first; decompress if refractory."),
  ("CVP 18 with IAP 20", "Transmural CVP ≈ 8", "Not volume-full."),
 ]),
]

CONCEPTS = [
# ---------------- pancreatitis ----------------
dict(id='PAN1', group='PAN', title='Cause and diagnosis', steps=[('GI02A', 1), ('GI02A', 2), ('GI02A', 3)], tops=[],
summary='Every cause ends in trypsin switched on inside the acinar cell; two of three criteria make the diagnosis, and lipase is the enzyme to trust.',
core=[
 "**Gallstones (40–70%)** then **alcohol (25–35%)** cause most attacks. With neither, check **triglycerides (causal above 1,000 mg/dL)**, **calcium**, drugs and a recent **ERCP**.",
 "Day-1 liver tests hint at the cause: **ALT above 150** points to stones, **AST above ALT** to alcohol. So the first scan is an **ultrasound for gallstones**.",
 "Every route (duct obstruction, acinar injury, faulty enzyme transport) ends in **trypsin activated inside the acinar cell**, and trypsin switches the other enzymes on.",
 "**Lipase** causes **fat necrosis**, which saponifies calcium, so **calcium falls**; **elastase** digests vessel walls and causes **bleeding**.",
 "Diagnosis is **two of three**: typical **pain**, **lipase or amylase above 3× normal**, typical **CT or MRI**. With pain and enzymes, **no imaging is needed**.",
 "**Lipase is the better test**: pancreas-specific, up in 4–8 h and raised for **8–14 days**. Amylase comes from many tissues and normalises in **3–4 days**, so a late presenter can have a normal amylase.",
 "**The enzyme level does not grade severity.** 80–85% of attacks are mild (mortality under 1–3%); the 20% that are moderate or severe carry 13–35%.",
],
flag=["**A raised amylase is not specific:** a perforated ulcer or mesenteric ischaemia can raise it. When the picture does not fit, CT decides."],
vis=['P_CASCADE', 'P_ENZYMES'],
pairs=[
 ('Gallstone pancreatitis', 'Alcohol pancreatitis', ['Epigastric pain to the back', 'Lipase above 3× normal'],
  [('!Day-1 liver tests', 'ALT above 150', 'AST above ALT, raised GGT'),
   ('First test', 'Ultrasound for stones', 'History; triglycerides if unclear'),
   ('Specific step', 'Cholecystectomy in the same admission if mild; ERCP only for cholangitis', 'Abstinence; thiamine')]),
 ('Pancreatitis', 'Perforated ulcer', ['Sudden epigastric pain', 'Raised amylase', 'Shock'],
  [('!Free gas', 'None', 'Under the diaphragm (erect X-ray or CT)'),
   ('Lipase', 'Above 3× and specific', 'Usually below 3×'),
   ('Abdomen', 'Tender, often soft early', 'Board-like rigidity'),
   ('Treatment', 'Fluids, analgesia, feeding', 'Resuscitation and surgery')]),
 ('Lipase', 'Amylase', ['Rise within hours', 'Above 3× normal counts', 'Level does not grade severity'],
  [('!Stays raised', '8–14 days', '3–4 days'),
   ('Source', 'Pancreas only', 'Salivary gland, bowel, ovary, fat, muscle'),
   ('False positives', 'Few', 'Renal disease, appendicitis, cholecystitis')]),
],
gate=[
 ("Typical pain and lipase 4× normal. Is CT needed to diagnose?", "No. Two of three criteria are met; CT is for doubt, or after 72 h for complications."),
 ("Day 5, amylase normal, lipase high. Pancreatitis?", "Yes. Amylase normalises in 3–4 days; lipase stays up for 8–14."),
 ("No stones, no alcohol. First blood test?", "Serum triglycerides (causal above 1,000 mg/dL), then calcium."),
]),

dict(id='PAN2', group='PAN', title='Grading and predicting severity', steps=[('GI02A', 4), ('GI02A', 5)], skip=[('GI02A', 'PANC-07')], tops=[('GI02A', 'T_9299d85e')],
summary='Severity is defined by how long organs fail; the scores only predict it.',
core=[
 "**Revised Atlanta (2012)** grades by organ failure. **Mild**: none, and no complications. **Moderately severe**: organ failure that resolves **within 48 h**, and/or local or systemic complications. **Severe**: organ failure **beyond 48 h**.",
 "Organ failure means a **modified Marshall score of 2 or more** in the **respiratory, cardiovascular or renal** system: three systems only.",
 "The **determinant-based** system adds infection and has **four grades**; **critical** = persistent organ failure **and** infected necrosis. Infected necrosis alone is already **severe** there, but only moderately severe in Atlanta.",
 "Scores predict; they do not define. **Ranson** has 11 items, **5 at admission and 6 at 48 h**, so it is complete only at **48 h**. 3 or more predicts severe disease, 6 or more about 40% mortality, and it contains no amylase or lipase.",
 "**BISAP** is the bedside score in the **first 24 h**: **BUN above 25, impaired mental state, SIRS, age above 60, pleural effusion**. **3 or more** marks a sharp rise in deaths.",
 "Single markers: **APACHE II of 8 or more**; **CRP above 150 mg/L at 48 h** predicts necrosis; **haematocrit above 44%** or a **rising BUN** on day 1 shows third-space loss.",
 "The **CT severity index** adds the Balthazar grade (0–4) to necrosis (**0, 2, 4 or 6**), for a maximum of **10**. Necrosis weighs more, and **7–10** carries about **17%** mortality.",
 "**Cullen and Grey Turner** signs (retroperitoneal blood) mean haemorrhagic necrotising disease but appear in **under 5%**: useful when present, useless when absent.",
],
flag=["**BISAP cut-off:** the notes give 2; most sources and the exam use **3 or more**.", "**Age:** above 55 in Ranson, above 60 in BISAP. A favourite swap."],
vis=['P_ATLANTA', 'P_SCORES'],
pairs=[
 ('Transient organ failure', 'Persistent organ failure', ['Modified Marshall of 2 or more', 'Respiratory, cardiovascular or renal'],
  [('!Duration', 'Resolves within 48 h', 'Beyond 48 h'),
   ('Atlanta grade', 'Moderately severe', 'Severe'),
   ('Mortality', 'Low', 'Up to about 30%')]),
 ('Revised Atlanta', 'Determinant-based', ['Organ failure counts', 'Mild means none of anything'],
  [('!Infected necrosis without organ failure', 'Moderately severe', 'Severe'),
   ('Grades', 'Three', 'Four (adds critical)'),
   ('Critical', 'Does not exist', 'Persistent organ failure and infected necrosis')]),
 ('Ranson', 'BISAP', ['Predict severity and death', 'Both include age'],
  [('!Complete at', '48 h', '24 h'),
   ('Items', '11 (5 + 6)', '5'),
   ('Age cut-off', 'Above 55', 'Above 60'),
   ('Contents', 'WBC, glucose, AST, LDH; then haematocrit fall, BUN rise, calcium, PaO₂, base deficit, fluid', 'BUN, mental state, SIRS, age, pleural effusion')]),
],
gate=[
 ("Organ failure for 36 h, no collections. Grade?", "Moderately severe: the failure was transient (under 48 h)."),
 ("Which score cannot be completed before 48 hours?", "Ranson: six of its 11 items are taken at 48 h."),
 ("Infected necrosis, no organ failure: Atlanta grade vs determinant-based grade?", "Moderately severe (Atlanta) vs severe (determinant-based)."),
]),

dict(id='PAN3', group='PAN', title='Imaging and collections', steps=[('GI02A', 6)], extra=[('GI02A', 'PANC-07')], tops=[],
summary='Ultrasound on day 1 for the cause, contrast CT after 72 hours for necrosis; collections are named by necrosis and by the 4-week wall.',
core=[
 "**Ultrasound** on admission (within 48 h) looks for the **cause**: gallstones and a dilated duct.",
 "**Contrast CT** is the gold standard for necrosis and collections, but only **after 72 h**: necrosis takes that long to demarcate, so an early CT under-calls it. An early CT is for diagnostic doubt only.",
 "Repeat CT at **7–10 days** if the CT severity index is 3 or more, on deterioration, or before any intervention.",
 "**MRI** avoids radiation and iodinated contrast (pregnancy, AKI) and shows **duct disruption**, but is **poor at showing gas**. **EUS** finds small duct stones that CT and ultrasound miss.",
 "Collections are named by two questions: **necrosis or not**, and **before or after 4 weeks**. Fluid: **APFC → pseudocyst**. Necrosis: **acute necrotic collection → walled-off necrosis**.",
 "That **4-week wall** is why drainage waits. **ERCP is a treatment, not a test**: only for **cholangitis** (within 24 h) or **persisting biliary obstruction**.",
],
flag=["**Routine ERCP** in gallstone pancreatitis is the trap; the indication is cholangitis or a blocked duct."],
vis=['P_COLLECTIONS', 'P_IMAGING'],
pairs=[
 ('Pseudocyst', 'Walled-off necrosis', ['Encapsulated', 'After about 4 weeks'],
  [('!Contents', 'Fluid only', 'Solid necrotic debris and fluid'),
   ('Arises from', 'Interstitial oedematous pancreatitis', 'Necrotising pancreatitis'),
   ('Best to see debris', 'MRI or EUS', 'MRI or EUS (CT under-calls debris)'),
   ('Intervention', 'Only if symptomatic, growing or obstructing', 'Drain, then debride if infected or obstructing')]),
 ('Necrotising pancreatitis', 'Interstitial oedematous', ['Enlarged, inflamed pancreas'],
  [('!Enhancement on CT', 'Non-enhancing areas', 'Uniform enhancement'),
   ('Best seen', 'After 72 h', 'Any time'),
   ('CT index necrosis points', '2, 4 or 6 by extent', '0')]),
],
gate=[
 ("Day 2, severe pancreatitis, CT shows no necrosis. Reassured?", "No. Necrosis demarcates after 72 h; an early CT under-calls it."),
 ("Encapsulated fluid-only collection 6 weeks after oedematous pancreatitis?", "A pseudocyst."),
 ("Gallstone pancreatitis without cholangitis: ERCP?", "No. ERCP only for cholangitis or persisting obstruction."),
]),

dict(id='PAN4', group='PAN', title='Fluids, pain and feeding', steps=[('GI02B', 1), ('GI02B', 2)], tops=[],
summary='Moderate Ringer’s to targets, generous analgesia, and an early-fed gut: a fed gut keeps bacteria out of the necrosis.',
core=[
 "**Ringer’s lactate** is the fluid: fewer ICU admissions, less organ failure and a lower CRP than saline. Avoid it only in hypercalcaemic pancreatitis.",
 "Inflamed capillaries leak whatever you give, so **moderate, goal-directed** fluid wins. **WATERFALL**: aggressive fluid (20 mL/kg, then 3 mL/kg/h) tripled **fluid overload (20.5% vs 6.3%)** with no better outcome.",
 "Moderate means a **10 mL/kg bolus only if hypovolaemic**, then **1.5 mL/kg/h**, reassessed at 12, 24, 48 and 72 h.",
 "Hypovolaemia markers: **haematocrit above 44%, BUN above 20, creatinine above 1.1, urine under 0.75 mL/kg/h, SBP under 90**. Slow or stop at **two signs of overload**.",
 "Pain: **multimodal**, patient-controlled; **no NSAIDs in AKI**. An **epidural** is opioid-sparing and linked to less AKI and organ failure.",
 "Mild disease: **on-demand oral feeding**, not nil by mouth. No oral intake by **day 3**: **nasogastric** feeding (as good as nasojejunal; nasojejunal for gastroparesis). **Parenteral nutrition is avoided.**",
],
flag=["**Septic-shock habit:** 30 mL/kg is the sepsis rule, not the pancreatitis rule. WATERFALL gives 10 mL/kg, and only to the hypovolaemic.", "**Fluid overload in WATERFALL** = at least two of the three criteria; the notes’ ‘one = suspected’ is not a protocol category (decided 22 Nov)."],
vis=['P_FIRST72'],
pairs=[
 ('Aggressive (WATERFALL)', 'Moderate (WATERFALL)', ['Ringer’s lactate', 'Checkpoints at 12, 24, 48, 72 h'],
  [('!Fluid overload', '20.5%', '6.3%'),
   ('Bolus', '20 mL/kg', '10 mL/kg only if hypovolaemic'),
   ('Then', '3 mL/kg/h', '1.5 mL/kg/h'),
   ('Outcome', 'No better', 'Same severity, less harm')]),
 ('Pancreatitis fluids', 'Septic-shock fluids', ['Capillary leak', 'Crystalloid first'],
  [('!First bolus', '10 mL/kg, only if hypovolaemic', '30 mL/kg'),
   ('Preferred fluid', 'Ringer’s lactate', 'Balanced crystalloid'),
   ('Harm of too much', 'Lung water, abdominal compartment syndrome', 'Overload, worse ARDS')]),
 ('Nasogastric feeding', 'Nasojejunal feeding', ['Enteral beats parenteral', 'Start by day 3 if not eating'],
  [('!Outcome', 'Equivalent', 'Equivalent'),
   ('Use', 'First choice', 'Gastroparesis or intolerance'),
   ('Placement', 'Bedside', 'Endoscopic or radiological')]),
],
gate=[
 ("Severe pancreatitis, normotensive, haematocrit 46%. What bolus?", "10 mL/kg Ringer’s (a hypovolaemia marker is present), then 1.5 mL/kg/h; not 20 mL/kg."),
 ("Day 3, still not eating. Feed how?", "Nasogastric enteral feeding; avoid parenteral nutrition."),
 ("Pancreatitis pain with AKI. Which analgesic to avoid?", "NSAIDs."),
]),

dict(id='PAN5', group='PAN', title='Infection, lung and the tight abdomen', steps=[('GI02B', 3), ('GI02B', 4)], tops=[('GI02B', 'T_305a0e05')],
summary='Early fever is inflammation, not infection; infected necrosis comes late and gets a carbapenem. The lung fails first, and a tense abdomen changes how you ventilate.',
core=[
 "Deaths come in two waves: **weeks 1–2 from SIRS and organ failure**, **after 2 weeks from infected necrosis**.",
 "**No prophylactic antibiotics**, even in severe necrotising disease: they prevent neither infected necrosis nor death.",
 "Suspect infected necrosis with **late deterioration** (weeks 2–4) or **gas in a collection on CT**. **Procalcitonin** helps hold antibiotics early; routine needle aspiration is no longer advised.",
 "Then a **carbapenem**: it penetrates necrosis and covers ESBL Gram-negatives. **Antifungals are not routine.**",
 "The **lung** fails most often: SIRS, fluid and **phospholipase A₂ digesting surfactant (DPPC)** cause ARDS, often with a **left pleural effusion**. Try non-invasive support, then **lung-protective** ventilation.",
 "A **tense abdomen** passes **20–60%** of its pressure to the chest, so the chest wall, not the lung, is stiff. Keep **6–8 mL/kg** and **driving pressure under 15**, set PEEP by compliance (often higher), and allow a plateau target of **target − 7 + 0.7 × IAP**. An **oesophageal balloon** settles it.",
 "**Pancreatic encephalopathy** (confusion and myoclonus in the first 2 weeks) is a diagnosis of exclusion: rule out **Wernicke’s** (give thiamine), glucose, sodium and alcohol withdrawal.",
],
flag=["**Two plateau corrections:** this one raises the plateau **target** (− 7 + 0.7 × IAP); the abdominal-pressure chapter corrects the **measured** plateau (plateau − 0.5 × IAP). Don’t mix them."],
vis=['P_PHASES'],
pairs=[
 ('Early fever (SIRS)', 'Infected necrosis', ['Fever', 'Raised white cells and CRP', 'Tachycardia'],
  [('!Timing', 'Week 1', 'Weeks 2–4'),
   ('CT', 'Necrosis without gas', 'Gas in the collection'),
   ('Procalcitonin', 'Low', 'High'),
   ('Action', 'No antibiotics', 'Carbapenem, then step-up')]),
 ('Stiff lung (ARDS)', 'Stiff chest wall (IAH)', ['High plateau pressure', 'Hypoxaemia'],
  [('!Transpulmonary pressure', 'High', 'Normal or low'),
   ('Cause', 'Cytokines, fluid, phospholipase A₂', 'Abdomen pushing up the diaphragm'),
   ('Response', 'Lower tidal volume, cap the plateau', 'Treat the IAP; higher PEEP and plateau allowance')]),
 ('ARDS', 'Fluid overload', ['Bilateral infiltrates', 'Hypoxaemia'],
  [('!Filling pressures', 'Normal', 'High (CVP above 12, wedge above 18)'),
   ('Response to a diuretic', 'Little', 'Improves'),
   ('Fluid balance', 'Any', 'Strongly positive')]),
],
gate=[
 ("Severe necrotising pancreatitis, day 2. Prophylactic meropenem?", "No. Prophylaxis prevents neither infected necrosis nor death."),
 ("Day 18, deterioration, gas in the collection. Next?", "A carbapenem, then step-up (drain first)."),
 ("Which enzyme breaks down surfactant in pancreatitis?", "Phospholipase A₂ (it digests dipalmitoyl phosphatidylcholine)."),
]),

dict(id='PAN6', group='PAN', title='Necrosis: delay, drain, step up', steps=[('GI02B', 5), ('GI02B', 6)], tops=[],
summary='Wait for the wall, drain first, debride by the least invasive route, and open last.',
core=[
 "**Sterile necrosis** is treated without intervention, and any intervention is **delayed to weeks 3–4** so the collection walls off.",
 "**Step-up**: (1) **percutaneous or endoscopic drainage** for infected necrosis with deterioration; (2) **minimally invasive necrosectomy** (VARD or endoscopic transgastric); (3) **open necrosectomy last**.",
 "**PANTER** (step-up vs open): major complications **69% → 40%**, fewer hernias and less new diabetes, the same mortality.",
 "A **sterile** collection is touched only for a reason. After **4 weeks**: persistent organ failure, **obstruction** (gastric outlet, bile duct, bowel), a **disconnected duct**, or a symptomatic or growing **pseudocyst**. After **8 weeks**: ongoing pain.",
 "Surgery is for failure of everything else: **abdominal compartment syndrome**, **bleeding when embolisation fails**, bowel ischaemia or fistula.",
 "A **bleeding pseudoaneurysm** goes to **CT angiography and embolisation first**, surgery second.",
 "**Mild gallstone pancreatitis**: cholecystectomy in the **same admission**. **Severe**: **defer** it until collections settle.",
 "Blood purification (high-volume haemofiltration, CytoSorb) improves haemodynamics or short-term numbers, but **not long-term mortality**.",
],
flag=["**Delay is the rule**, but infected necrosis with deterioration can be drained earlier (step 1); debridement still waits for the wall."],
vis=['P_STEPUP', 'P_WHEN'],
pairs=[
 ('Pseudoaneurysm bleed', 'Haemorrhagic pancreatitis', ['Bleeding, falling Hb, shock'],
  [('!Timing', 'Late (weeks)', 'Early (days)'),
   ('Source', 'Eroded artery (splenic, gastroduodenal)', 'Diffuse retroperitoneal'),
   ('First step', 'CT angiography → embolisation', 'Resuscitate, correct coagulopathy')]),
 ('Disconnected duct', 'Partial duct leak', ['Duct injury from necrosis', 'Persistent collection or fistula'],
  [('!Duct', 'Fully transected', 'Partly breached'),
   ('Treatment', 'Long-term transmural drainage or distal resection', 'A bridging pancreatic stent')]),
 ('Mild gallstone pancreatitis', 'Severe gallstone pancreatitis', ['Gallstones are the cause', 'Recurrence if left'],
  [('!Cholecystectomy', 'Same admission', 'Deferred until collections settle'),
   ('ERCP', 'Only for cholangitis or obstruction', 'Same')]),
],
gate=[
 ("Infected walled-off necrosis, deteriorating at week 4. First step?", "Percutaneous or endoscopic drainage (step 1), not open surgery."),
 ("Asymptomatic 5 cm pseudocyst at 6 weeks?", "Leave it. Intervene only if symptomatic, growing or obstructing."),
 ("Mild gallstone pancreatitis: when is the cholecystectomy?", "During the index admission."),
]),

# ---------------- gut ----------------
dict(id='GUT1', group='GUT', title='The gut barrier', steps=[('GI03', 1), ('GI03', 2)], tops=[('GI03', 'T_142d1a37')],
summary='In the ICU the gut matters as a barrier: low flow kills the villus tip first, the barrier leaks, and toxic lymph reaches the lung.',
core=[
 "The gut absorbs, but in the ICU its **barrier** (mucosa, mucin) and **immune** roles (gut lymphoid tissue, secretory IgA) matter more.",
 "Each segment has its loss: **duodenum** iron and calcium; **jejunum** most nutrients; **terminal ileum B12 and bile salts** (resection → B12 deficiency and bile-salt diarrhoea); **colon** water, sodium, short-chain fatty acids.",
 "Splanchnic flow is cut first when output falls, and the **villus tip** dies first: the central arteriole fountains out at the tip, and **counter-current exchange** shunts oxygen to the venule before it arrives.",
 "So **mucosal ischaemia comes before transmural ischaemia**, and **lactate rises late**.",
 "The sequence: **hypoperfusion → resuscitation → ischaemia–reperfusion and oedema → barrier loss**. Bacteria and endotoxin then **translocate** into portal blood and lymph.",
 "**Toxic lymph** travels up the thoracic duct and reaches the **lung first**: the gut is the motor of multiple organ failure.",
 "The defence is **early enteral feeding**: it keeps the villi intact and cuts translocation.",
 "The diaphragm clears peritoneal fluid and bacteria through **stomata** into lymph on expiration, so peritoneal infection reaches the blood fast. **IAH and ventilation** splint it and slow clearance.",
],
flag=[],
vis=['G_BARRIER'],
pairs=[
 ('Mucosal ischaemia', 'Transmural ischaemia', ['Low splanchnic flow'],
  [('!Lactate', 'Normal', 'Raised'),
   ('Serosa', 'Looks pink', 'Dark, necrotic'),
   ('Signs', 'Feed intolerance, translocation', 'Peritonism, perforation'),
   ('Reversible', 'Yes', 'No')]),
 ('Terminal ileal loss', 'Duodenal loss', ['Malabsorption after resection'],
  [('!Deficiency', 'B12 and bile salts (bile-salt diarrhoea)', 'Iron, calcium, folate'),
   ('Typical setting', 'Crohn’s, ileal resection, stoma', 'Gastric bypass, duodenal disease')]),
],
gate=[
 ("Which part of the villus dies first, and why?", "The tip: counter-current exchange shunts oxygen away before it reaches the tip."),
 ("Toxic gut lymph reaches which organ first?", "The lung, via the thoracic duct."),
 ("Single best defence of the gut barrier?", "Early enteral feeding."),
]),

dict(id='GUT2', group='GUT', title='The sick abdomen: imaging and perforation', steps=[('GI03', 3)], tops=[('GI03', 'T_6e2cdcbd'), ('GI03', 'T_a1086ece'), ('GI03', 'T_e215de25'), ('GI03', 'T_ce178f52'), ('GI03', 'T_dc881b68'), ('GI03', 'T_051129df')],
summary='The ICU abdomen lies on examination, so numbers and imaging decide; the perforation site sets the contamination.',
core=[
 "Most ICU patients have a GI symptom; **three or more at once** is gut failure and predicts lower survival.",
 "The bedside abdomen is unreliable under sedation and ventilation, so **imaging decides**: ultrasound for fluid and organs, X-ray for tubes and loops.",
 "The **3-6-9 rule**: small bowel above **3 cm**, colon above **6 cm**, caecum above **9 cm** is dilated; a **caecum above 12 cm** risks perforation.",
 "**Contrast CT** whenever sepsis may be abdominal: free air or fluid, thick wall, **pneumatosis**, reduced mesenteric flow.",
 "Visceral pain follows embryology: **foregut → epigastrium, midgut → periumbilical, hindgut → hypogastrium**; parietal pain localises.",
 "Bacteria increase down the gut (stomach under 10³/mL, colon **10¹¹–10¹²**, mostly anaerobes), so a **colonic perforation** gives the worst faecal peritonitis.",
 "**Perforated ulcer**: sudden epigastric pain, shoulder-tip pain, board-like abdomen; an **erect chest X-ray** shows free gas in about 75–85% (CT if negative).",
 "Named pictures: a contained small **oesophageal perforation** in a stable patient is treated **without surgery** (stent or clip, nil by mouth, antibiotics and an antifungal). Crepitus, gas in tissues and shock mean **Clostridium perfringens** (debride; penicillin plus clindamycin). Bleeding 2 weeks after a Whipple means a **pseudoaneurysm**: CT angiography and embolisation.",
],
flag=[],
vis=['G_369', 'G_PAINMAP'],
pairs=[
 ('Pneumoperitoneum', 'Chilaiditi sign', ['Gas under the right diaphragm on X-ray'],
  [('!Haustra or folds in the gas', 'No', 'Yes (colon between liver and diaphragm)'),
   ('Patient', 'Peritonitic', 'Usually well'),
   ('Next', 'CT or surgery', 'Nothing')]),
 ('Ultrasound', 'CT', ['Look for collections and free fluid'],
  [('!Limited by bowel gas and obesity', 'Yes', 'No'),
   ('Bedside', 'Yes', 'Needs transport'),
   ('Best for', 'Free fluid, superficial collections, gallbladder', 'Deep collections, free air, ischaemia')]),
],
gate=[
 ("Caecum 10 cm on X-ray. Dilated? At risk?", "Dilated (above 9 cm); the perforation risk starts above 12 cm."),
 ("Which perforation gives the heaviest contamination?", "The distal colon: 10¹¹–10¹² bacteria/mL, mostly anaerobes."),
 ("Stable patient, small contained oesophageal perforation after endoscopy?", "No surgery: stent or clip, nil by mouth, antibiotics and an antifungal."),
]),

dict(id='GUT3', group='GUT', title='Gastroparesis, paralysis and Ogilvie’s', steps=[('GI03', 4)], tops=[],
summary='Most ICU dysmotility is made by what we give or fail to correct. Remove it, give a short prokinetic course, then a tube past the pylorus; Ogilvie’s gets neostigmine.',
core=[
 "ICU gastroparesis is mostly **transient and made by us**: **opioids**, β- and α₂-agonists, **high glucose**, low potassium or magnesium, acidosis. The lasting causes are diabetes, renal failure, vagotomy and scleroderma.",
 "It shows as **high gastric residuals**: a single residual above **200 mL** is high; **hold gastric feed above 500 mL**.",
 "Treat in order: **correct glucose and electrolytes, cut opioids and sedatives** → **erythromycin** (motilin agonist) ± **metoclopramide** (D₂ antagonist) → a **post-pyloric tube** (residual above 500 mL or failed prokinetics).",
 "Prokinetics are a **short course**: tachyphylaxis (erythromycin fades by 72 h; ESPEN 2023 says 24–48 h, stop by day 3), and erythromycin prolongs QT.",
 "**Lower GI paralysis** = **no stool for 3 days** without mechanical obstruction; hyperperistalsis suggests obstruction.",
 "**Ogilvie’s** = massive **colonic** dilatation without obstruction. Correct the causes, then give **neostigmine 2 mg IV** with ECG monitoring and atropine at hand; **colonoscopic decompression** if it fails or the **caecum is above 12 cm**.",
 "Prevention: correct electrolytes and glucose, avoid fluid overload, **minimise opioids and sedatives**, early low-dose enteral feeding, laxatives.",
],
flag=["**Prokinetic duration (card fixed 22 Nov):** the card said up to 5 days; ESPEN 2023 says 24–48 h, stop by day 3. Answer ‘short course, tachyphylaxis’.", "**Bowel sounds (card fixed):** ESICM 2012 says at least 1 minute in at least two quadrants, repeated; not every quadrant."],
vis=['G_GASTRO', 'G_OGILVIE'],
pairs=[
 ('Erythromycin', 'Metoclopramide', ['Prokinetic for feed intolerance', 'Short course (tachyphylaxis)'],
  [('!Receptor', 'Motilin agonist', 'Dopamine D₂ antagonist'),
   ('Main risk', 'QT prolongation, antibiotic resistance', 'Extrapyramidal effects, QT'),
   ('Order', 'First choice', 'Add-on or alternative')]),
 ('Ogilvie’s', 'Mechanical obstruction or volvulus', ['Massive colonic dilatation', 'Distension, no stool'],
  [('!Mechanical cause on CT', 'None', 'Transition point or twist'),
   ('Treatment', 'Neostigmine, decompression', 'Endoscopic detorsion or surgery'),
   ('Neostigmine', 'Yes', 'Contraindicated')]),
 ('Ogilvie’s', 'Toxic megacolon', ['Colonic dilatation'],
  [('!Cause', 'Motility failure', 'Colitis (C. difficile, IBD)'),
   ('Systemic toxicity', 'Not typical', 'Fever, tachycardia, toxic'),
   ('Neostigmine', 'Yes', 'No: treat the colitis')]),
],
gate=[
 ("Gastric residual 550 mL after 3 days of erythromycin. Next?", "Post-pyloric (nasojejunal) feeding."),
 ("Ogilvie’s: the drug, and the safety precautions?", "Neostigmine 2 mg IV over 3–5 min, with ECG monitoring and atropine at hand."),
 ("Definition of lower GI paralysis?", "No stool for 3 days without mechanical obstruction."),
]),

dict(id='GUT4', group='GUT', title='Diarrhoea and AGI grading', steps=[('GI03', 5), ('GI03', 6)], tops=[],
summary='Diarrhoea is defined by number, weight and form, and is not a reason to stop feeding; the AGI grade tells you to feed, treat, search or operate.',
core=[
 "ICU diarrhoea = **3 or more loose stools a day**, **above 200 g/day**, **Bristol 5–7**.",
 "First step: **stop laxatives and prokinetics, review drugs and feed, test for C. difficile**, and **keep feeding**. No antimotility agent until C. difficile is excluded.",
 "**Fasting separates them**: **osmotic** diarrhoea stops with fasting (osmotic gap above 100); **secretory** diarrhoea is large, plasma-like and ignores fasting (gap under 50). Gap = 290 − 2 × (Na + K).",
 "**AGI (ESICM 2012)**: **I risk** (transient), **II dysfunction** (needs intervention), **III failure** (no response to intervention), **IV failure with distant organ dysfunction** (life-threatening).",
 "Abdominal pressure maps onto it: **AGI II ≈ IAH grade I (12–15)**, **AGI III ≈ IAH grade II (15–20)**, and **abdominal compartment syndrome is AGI IV**.",
 "Act by grade: **I, feed**. **II, keep feeding, treat the symptom, measure IAP** (50–80% of needs early, 80–100% by day 3). **III, search for hidden abdominal pathology**; minimal feed, supplemental PN after day 4–7. **IV, stop enteral feed**, decompress, then endoscopy, IR or **laparotomy**.",
 "Reassess **6-hourly**, then 12-hourly, and watch for **refeeding syndrome** when feeding restarts.",
],
flag=[],
vis=['G_AGI'],
pairs=[
 ('Osmotic diarrhoea', 'Secretory diarrhoea', ['Watery stools', 'Feeds and drugs can cause both'],
  [('!Fasting', 'Stops', 'Continues'),
   ('Osmotic gap', 'Above 100', 'Under 50'),
   ('Volume', 'Moderate', 'Litres, plasma-like'),
   ('Causes', 'Hyperosmolar feed, sorbitol-containing drugs, fast transit', 'Infection, C. difficile toxin, bile acids, inflammation')]),
 ('AGI III', 'AGI IV', ['Gut failure despite treatment'],
  [('!Distant organ dysfunction', 'No', 'Yes'),
   ('Examples', 'Persistent feed intolerance, IAP 15–20', 'Ischaemia, bleeding with shock, Ogilvie’s, ACS'),
   ('Feeding', 'Minimal trial; PN after day 4–7', 'Stop enteral feed'),
   ('Action', 'Search for the cause', 'Intervene: surgery, IR, endoscopy')]),
 ('Diarrhoea on enteral feed', 'Feed intolerance', ['Fed patient with GI symptoms'],
  [('!Stop the feed?', 'No', 'Reduce or hold gastric feed'),
   ('First step', 'Drug review, C. difficile test', 'Prokinetic, then post-pyloric tube')]),
],
gate=[
 ("Ventilated, 4 liquid stools a day on feed. Stop the feed?", "No. Stop laxatives and prokinetics, review drugs, test for C. difficile, keep feeding."),
 ("Persistent feed intolerance, IAP 18, no other organ failure. AGI grade?", "Grade III."),
 ("Abdominal compartment syndrome is which AGI grade?", "Grade IV."),
]),

# ---------------- mesenteric ischaemia ----------------
dict(id='MES1', group='MES', title='Anatomy and the four causes', steps=[('GI04', 1), ('GI04', 2), ('GI04', 3)], tops=[],
summary='Three arteries, two watersheds, four causes: each with its own patient and its own pain. Colonic ischaemia is a separate, milder disease.',
core=[
 "**Coeliac**: stomach, liver, proximal duodenum. **SMA**: distal duodenum, **all the small bowel**, right and proximal transverse colon. **IMA**: distal transverse colon to the upper rectum.",
 "The watersheds fail first in low flow: **Griffiths’ point = splenic flexure**, **Sudeck’s point = rectosigmoid**.",
 "The SMA leaves the aorta at an acute angle, so **emboli lodge there**, usually **beyond the middle colic**, sparing the proximal jejunum; a thrombosis sits at the origin.",
 "The gut tolerates a **50%** fall in flow (75% for up to 12 h) by extracting more oxygen; injury starts below a **MAP of 45**. The **mucosa dies first** while the serosa still looks pink.",
 "Reperfusion adds a **xanthine oxidase free-radical** injury: expect **high potassium, acidosis and hypotension** when flow returns.",
 "Four causes: **embolism (25–50%: AF, sudden pain)**; **thrombosis (15–40%: post-prandial pain, weight loss)**; **non-occlusive (20–25%: shock, high-dose vasopressors, cardiac surgery, dialysis)**, the ICU’s own and the deadliest; **venous (under 10%: thrombophilia, cirrhosis, pancreatitis; pain waxing and waning)**.",
 "The sign of all four: **pain out of proportion** to a soft abdomen. **Peritonism means infarction.**",
 "**Colonic ischaemia** is different: older (90% over 60), not very sick, **mild left-sided tenderness and bloody diarrhoea within 24 h**, and the test is **colonoscopy**. Aortic surgery causes ischaemic colitis, not NOMI.",
],
flag=[],
vis=['M_CAUSES'],
pairs=[
 ('Small bowel ischaemia', 'Colonic ischaemia', ['Ischaemic bowel', 'Older patients with vascular disease'],
  [('!Bleeding', 'Uncommon until late', 'Rectal bleeding early'),
   ('How sick', 'Severely ill', 'Not severely ill'),
   ('Pain vs signs', 'Severe pain, little tenderness', 'Mild pain, tenderness present'),
   ('Test', 'CT angiography', 'Colonoscopy')]),
 ('Embolic SMA occlusion', 'Thrombotic SMA occlusion', ['Acute mesenteric ischaemia'],
  [('!Site', 'Beyond the middle colic (spares proximal jejunum)', 'At the origin (whole SMA territory)'),
   ('History', 'AF, sudden pain', 'Post-prandial pain, weight loss'),
   ('Repair', 'Aspiration or embolectomy', 'Stent or bypass')]),
 ('NOMI', 'Embolism (septic ICU patient)', ['ICU patient, abdominal pain, acidosis'],
  [('!Vessels on CT angiography', 'Patent, narrowed, spastic', 'Filling defect'),
   ('Setting', 'Shock, high-dose vasopressors', 'AF'),
   ('Treatment', 'Restore flow, stop constrictors, papaverine into the SMA', 'Aspiration or embolectomy')]),
],
gate=[
 ("AF, sudden severe periumbilical pain, soft abdomen. Diagnosis until proven otherwise?", "Embolic acute mesenteric ischaemia."),
 ("The watershed at the splenic flexure is called?", "Griffiths’ point (Sudeck’s is the rectosigmoid)."),
 ("Older patient, mild left-sided pain, bloody diarrhoea, not very sick. Test?", "Colonoscopy: this is colonic ischaemia."),
]),

dict(id='MES2', group='MES', title='Diagnosis and treatment', steps=[('GI04', 4), ('GI04', 5)], tops=[],
summary='No blood test rules it in or out: suspicion goes straight to biphasic CT angiography, peritonitis straight to theatre. Restore flow by the cause, resect only dead bowel, look again.',
core=[
 "No blood test confirms or excludes AMI: **D-dimer** is sensitive (96%) but non-specific; **I-FABP** is specific (93%) but insensitive; **lactate is late**, a sign of transmural infarction.",
 "**Biphasic CT angiography** is the test (sensitivity 94%, specificity 95%): **no oral contrast**, and **don’t withhold contrast for AKI**.",
 "CT signs: arterial filling defect, non-enhancing or thick wall, dilatation; **pneumatosis with portal venous gas = dead bowel**.",
 "**Peritonitis → laparotomy without imaging.** A normal CT with high suspicion → **catheter angiography** (especially for NOMI).",
 "**Tonometry** reads the mucosa’s CO₂: a widening **gastric-to-arterial PCO₂ gap** (normal under 7 mmHg) means gut ischaemia. The card calls it the only valid test, but it is rarely used.",
 "General care: fluids, NG decompression, broad-spectrum antibiotics, **weight-based unfractionated heparin**. **Avoid vasopressin, high-dose noradrenaline and digoxin**; if an inotrope is needed, use **dobutamine, low-dose dopamine or milrinone**.",
 "**Peritonitis decides the route.** None → **endovascular** (aspiration or stent; mortality about 25% vs 40% open in observational data). Peritonitis → **open**: restore flow first, **resect only dead bowel**, leave the abdomen open, **second look**.",
 "By cause: thrombosis → **stent or antegrade bypass** (vein, not PTFE, in a contaminated field); venous → **heparin**, then anticoagulation for **3–6 months** (lifelong with thrombophilia); **NOMI → restore flow, stop constrictors, papaverine into the SMA**.",
],
flag=["**D-dimer:** older teaching used a normal D-dimer to rule AMI out; **ESVS 2025 no longer accepts it**."],
vis=['M_TESTS', 'M_PATH'],
pairs=[
 ('Inodilators', 'Vasopressors', ['Support the circulation in AMI'],
  [('!Splanchnic flow', 'Preserved or increased', 'Reduced'),
   ('Drugs', 'Dobutamine, milrinone, low-dose dopamine', 'Vasopressin, high-dose noradrenaline'),
   ('Use in AMI', 'Preferred', 'Avoid (and avoid digoxin)')]),
 ('Endovascular', 'Open repair', ['Restore flow first'],
  [('!Peritonitis', 'Absent', 'Present'),
   ('Mortality (observational)', 'About 25%', 'About 40%'),
   ('Bowel', 'Later resection in about 14%', 'Resect dead bowel, second look')]),
 ('Rising mucosal PCO₂', 'Rising arterial PCO₂', ['A raised CO₂ reading'],
  [('!Mucosal-to-arterial gap', 'Widens', 'Unchanged'),
   ('Meaning', 'Gut hypoperfusion', 'Hypoventilation')]),
],
gate=[
 ("Suspected AMI, creatinine 2.4. Contrast CT?", "Yes: biphasic CT angiography without oral contrast; don’t withhold it for AKI."),
 ("AMI on noradrenaline and needing an inotrope. Which?", "Dobutamine (or milrinone, low-dose dopamine); avoid vasopressin and digoxin."),
 ("Embolic AMI with peritonitis. Stent?", "No: laparotomy, embolectomy, resect dead bowel, second look."),
]),

# ---------------- abdominal pressure ----------------
dict(id='IAH1', group='IAH', title='Measure and define', steps=[('GI05', 1), ('GI05', 2)], tops=[],
summary='Abdominal pressure is a number from the bladder: 12 is hypertension, and over 20 with a new failing organ is compartment syndrome.',
core=[
 "Normal IAP in the critically ill is **5–7 mmHg**; obesity and pregnancy raise the baseline **without** organ effects.",
 "Measure through the **bladder** (the gold standard), **every 4 h** while at risk: **supine**, zero at the **mid-axillary line**, instil **at most 25 mL** of saline, wait **30–60 s**, read at **end-expiration** with a **relaxed abdominal wall**.",
 "Every departure pushes the reading **up**: more saline, head up, abdominal muscles contracting.",
 "**IAH = sustained or repeated IAP of 12 or more**: **grade I 12–15, II 16–20, III 21–25, IV above 25**.",
 "**ACS = sustained IAP above 20 with new organ dysfunction.** It is not a grade: even grade IV without organ failure is only IAH.",
 "**APP = MAP − IAP** (target **60 or more**). The kidney feels IAP twice, **filtration gradient = MAP − 2 × IAP**, so it fails first.",
],
flag=["**Children:** 1 mL/kg (minimum 3, maximum 25 mL); the notes print 0.5 mL/kg."],
vis=['I_GRADES', 'I_KRON'],
pairs=[
 ('IAH grade IV', 'Abdominal compartment syndrome', ['Very high abdominal pressure'],
  [('!New organ failure', 'Not required', 'Required'),
   ('Pressure', 'Above 25', 'Above 20, sustained'),
   ('Action', 'Medical measures', 'Find the cause; decompress if refractory')]),
 ('Mid-axillary zero (WSACS)', 'Symphysis zero (original Kron)', ['Bladder pressure'],
  [('!Zero point', 'Mid-axillary line', 'Symphysis pubis'),
   ('Position', 'Supine', 'Varied'),
   ('Standard now', 'Yes', 'No')]),
 ('Oliguria from IAH', 'Acute tubular necrosis', ['Oliguria, rising creatinine'],
  [('!Urine sodium', 'Low', 'High'),
   ('IAP', '15 or more', 'Normal'),
   ('Fix', 'Lower the IAP', 'Supportive')]),
],
gate=[
 ("IAP 22, no new organ failure. Compartment syndrome?", "No: IAH grade III. ACS needs new organ dysfunction."),
 ("MAP 75, IAP 20. APP and filtration gradient?", "APP 55 (below 60); filtration gradient 35."),
 ("Maximum saline instilled to measure bladder pressure?", "25 mL."),
]),

dict(id='IAH2', group='IAH', title='Causes, effects and management', steps=[('GI05', 3), ('GI05', 4), ('GI05', 5)], tops=[],
summary='Pressure rises when the abdomen holds more or gives less. It lowers output while CVP and airway pressures read high. Treat medically first; decompress refractory compartment syndrome.',
core=[
 "**Primary** ACS starts **in the abdomen or pelvis** (trauma, damage-control laparotomy, packs): early surgery or radiology. **Secondary** comes from **massive resuscitation** elsewhere (burns, sepsis): medical first. **Recurrent** returns after treatment of either.",
 "Four groups of cause: **less wall compliance** (burn eschar, tight closure), **more intraluminal contents** (ileus, gastric distension), **more abdominal contents** (ascites, blood, packs), **capillary leak with fluid resuscitation**. In trauma, **3 L or more of crystalloid** predicts both types.",
 "Effects: **venous return and cardiac output fall**; the chest stiffens (high peak and plateau pressures); **oliguria at 15, anuria at 30 mmHg**; gut flow falls and oedema raises the pressure further; **ICP rises**.",
 "The numbers that rise mislead: about half of IAP reaches the chest, so **CVP and wedge read falsely high**. Transmural CVP = **CVP − 0.5 × IAP**, or use volumetric indices.",
 "Medical steps from **IAP 12**: **relax the wall** (sedation, analgesia, neuromuscular block; head of bed ≤ 30°), **empty the gut** (NG, rectal tube, prokinetics), **drain collections** (paracentesis, percutaneous), **stop the positive balance** (diuretics, ultrafiltration).",
 "ACS: find the cause. A perforation or bleed is opened now; fluid-driven disease is drained and dried first; **decompressive laparotomy** with temporary closure if organ failure persists (usually grade III–IV).",
 "Stop measuring when IAP stays **under 12**. Protocolised WSACS care raised survival **from 50% to 72%**. Expect **reperfusion** (hypotension, high potassium, acidosis) on decompression.",
],
flag=["**No fixed pressure threshold** for laparotomy: persistent grade III–IV with organ dysfunction is the usual trigger.", "**Two plateau corrections:** measured plateau − 0.5 × IAP (this chapter) vs plateau target − 7 + 0.7 × IAP (pancreatitis chapter)."],
vis=['I_EFFECTS', 'I_STEPS'],
pairs=[
 ('Primary ACS', 'Secondary ACS', ['IAP above 20 with organ failure'],
  [('!Origin', 'In the abdomen or pelvis', 'Outside the abdomen'),
   ('Setting', 'Damage-control laparotomy, packs, bleeding', 'Massive resuscitation: burns, sepsis'),
   ('Diagnosis', 'Expected', 'Elusive, late'),
   ('Treatment', 'Early surgery or radiology', 'Medical first')]),
 ('High CVP from IAH', 'High CVP from volume overload', ['CVP is high'],
  [('!Transmural CVP', 'Normal or low', 'High'),
   ('Cardiac output', 'Low', 'Normal or high'),
   ('Response', 'Lower the IAP; fluid if needed', 'Diuresis')]),
 ('Percutaneous drainage', 'Decompressive laparotomy', ['Lower the IAP'],
  [('!When', 'Free fluid or ascites driving IAH', 'Refractory ACS or a surgical cause'),
   ('How', 'Bedside', 'Open abdomen with temporary closure')]),
],
gate=[
 ("IAP 18, CVP 16. Is the patient full?", "Not necessarily: transmural CVP ≈ 16 − 9 = 7."),
 ("Burns patient after 12 L of crystalloid develops ACS. Primary or secondary?", "Secondary."),
 ("At what IAP does oliguria appear?", "About 15 mmHg (anuria at about 30)."),
]),
]

DECISIONS_NOTE = 'GI flags decided 22 Nov: GUT-07 d, GUT-08 a fixed; PANC-16 c, GUT-01, GUT-04 c noted.'
