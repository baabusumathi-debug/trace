# GI03 — Explain v3 ("Learn" depth): the gut in critical illness — functions and absorption, villus microcirculation, the gut as the motor of multiple organ failure, how common GI
# symptoms are, imaging the ICU abdomen, gastroparesis (causes, treatment), bowel sounds, lower GI paralysis and Ogilvie’s syndrome, ICU diarrhoea (definition, osmotic vs secretory),
# ESICM acute gastrointestinal injury (AGI) grades and their management, true/false sweep.
# No mnemonics or hooks. Driven by qpack/GI03.md (14 question links: GUT-05 imaging 4, GUT-08 paralysis/Ogilvie 3, GUT-03 barrier 2; GUT-06, -07, -09, -10, -12 one each).
# GUT-01, -02, -04, -11 and -13 have no linked question and get short explanations with [pattern] decode items.
# No `fix` entries exist for GI03 in trace/test/data/qbank.json (checked 20 Nov 2026). The card-layer `lines` and `cross` notes in gi_cardlayer.json were read and are covered:
# GUT-05 (abscess → contrast CT; NG tube in a bronchus), GUT-07 (GT key on venting gastrostomy is wrong), GUT-08 (ileus mechanism; post-laparotomy ileus care), GUT-09 (keep feeding),
# GUT-12 (drug review first, no antimotility agent until C. difficile is excluded).
# Checked online on 20 Nov 2026:
#  - ESICM Working Group on Abdominal Problems, Reintam Blaser, Intensive Care Med 2012;38:384–394 (PMC full text): AGI I risk (post-op nausea/vomiting, absent bowel sounds after
#    surgery, reduced motility in early shock) → early EN within 24–48 h (1B), limit motility-impairing drugs; II dysfunction (gastroparesis with high GRV or reflux, lower GI paralysis,
#    diarrhoea, IAH grade I 12–15 mmHg, visible blood, feeding intolerance) → start or continue EN, treat the cause, prokinetics, post-pyloric if prokinetics fail; III failure (persisting
#    intolerance, worsening dilatation, IAH grade II 15–20, APP under 60) → look for undiagnosed abdominal pathology, avoid early supplemental PN in the first 7 days (2B); IV (bowel
#    necrosis, bleeding with haemorrhagic shock, Ogilvie’s, ACS needing decompression) → no conservative approach, laparotomy or other emergency intervention.
#    GRV: single value over 200 mL ‘large’ → bedside evaluation, do not stop feeds for 200–500 mL alone; stop gastric feeds above 500 mL in one measurement; metoclopramide and/or
#    erythromycin IV for high GRV (1B); routine prokinetics not recommended (1A). Feeding intolerance: under 20 kcal/kg/day enterally within 72 h. Lower GI paralysis: no stool for 3 or more
#    consecutive days without mechanical obstruction. Bowel sounds: auscultate at least 1 min in TWO quadrants, repeat within a short time; 5–35/min normal; hyperperistalsis = bowel trying
#    to overcome obstruction. Diarrhoea: 3 or more loose/liquid stools a day with stool weight over 200–250 g/day (or over 250 mL/day). Dilatation: colon over 6 cm, caecum over 9 cm,
#    small bowel over 3 cm. Ogilvie’s: neostigmine IV considered if caecum over 10 cm and no improvement in 24 h (2B); colonoscopic decompression if no improvement in 24–48 h (1C);
#    conservative/colonoscopic care 48–72 h unless caecum over 12 cm (2C). GI bleeding clinically evident 5–25%, clinically important 1.5–4% of ventilated patients. Up to 62% of ICU
#    patients have at least one GI symptom.
#  - Reintam Blaser, Intensive Care Med 2013 (40 ICUs, 377 ventilated patients): at least one GI symptom in 60.2% in week 1 (44.6% on day 1); two or more concurrent 20% (36% in the earlier
#    single-centre study); three or more (‘GI failure’) 6.4%, 28-day mortality 62.5% vs 28.9%; day-1 GI failure OR 3.19 for death; number of symptoms independently predicted death on days 2 and 7.
#  - GIDS (Reintam Blaser, Clin Nutr 2021; 540 patients, 11 ICUs): 0–4 score built on AGI, additive to SOFA for 28- and 90-day mortality (HR about 1.4).
#  - ESPEN 2023 ICU guideline (Singer, Clin Nutr 2023;42:1671): early EN within 48 h; delay EN if gastric aspirate over 500 mL/6 h; IV erythromycin first-line prokinetic (commentary:
#    100–250 mg three times daily, 24–48 h, stop after three days), metoclopramide 10 mg two to three times daily or the combination; post-pyloric feeding if intolerance is not solved by
#    prokinetics; hypocaloric EN not exceeding 70% of EE early, up to 80–100% after day 3; supplemental PN timing days 4–7; protein 1.3 g/kg/day; continuous rather than bolus EN (less diarrhoea).
#  - ASCRS 2021 colonic volvulus/ACPO guideline: perforation or ischaemia 3–15%, risk with caecum over 12 cm and distension over 6 days (0%, 7%, 23% for under 12, 12–14, over 14 cm);
#    conservative care first (resolves 70–90%), avoid oral osmotic/stimulant laxatives; neostigmine 2–5 mg IV over 1–5 min (trial: 2 mg over 2–5 min), about 90% response, bradycardia 5–9%,
#    atropine or glycopyrrolate at hand, cardiac monitoring; contraindicated in ischaemia/perforation, pregnancy, uncontrolled arrhythmia, active bronchospasm; colonoscopic decompression
#    (perforation 1–3%) with a decompression tube if neostigmine fails or is contraindicated.
#  - Stool osmotic gap 290 − 2(Na + K): over 100 osmotic, under 50 secretory, 50–100 indeterminate (some texts use over 125 for osmotic).
# From standard references without a fresh check (confident): absorption sites (GUT-01); villus counter-current exchange (GUT-02); gut–lymph hypothesis (Deitch); ileus mediators (nitric
# oxide, VIP, IL-6, sympathetic overactivity); ASPEN/SCCM 2016 (do not use GRV routinely; if used, do not hold feeds for GRV under 500 mL); ESICM 2017 early EN guideline (delay EN in
# uncontrolled shock, uncontrolled hypoxaemia and acidosis, uncontrolled upper GI bleeding, GRV over 500 mL/6 h, bowel ischaemia or obstruction, ACS, high-output fistula without distal access); NG tube position confirmed by X-ray or aspirate pH 5.5 or less;
# Chilaiditi sign; erythromycin QT prolongation and tachyphylaxis; loperamide risk in C. difficile (toxic megacolon).
# Independent review (20 Nov 2026): ESICM 2017 early EN guideline abstract (Reintam Blaser, Intensive Care Med 2017;43:380) re-read: delay EN in uncontrolled shock, uncontrolled
# hypoxaemia and acidosis, uncontrolled upper GI bleeding, gastric aspirate over 500 mL/6 h, bowel ischaemia, bowel obstruction, abdominal compartment syndrome, high-output fistula
# without distal access. Reintam Blaser 2013 abstract/full text re-read: two or more concurrent symptoms 20%, GI failure 6.4%, no single symptom an independent predictor (absent
# bowel sounds and GI bleeding most strongly associated). ESPEN 2023 text re-read (prokinetics, energy, SPN days 4–7). Magnesium is absorbed mainly in the distal small bowel and colon.

SPINE = [
  ("What the gut does", "The gut absorbs, but in the ICU its more important jobs are being a barrier and an immune organ, and each absorptive site has a deficiency that follows its loss."),
  ("Ischaemic villus, leaky barrier", "Counter-current exchange leaves the villus tip short of oxygen, so the mucosa dies first in shock, the barrier fails, and bacteria, endotoxin and toxic lymph drive distant organ failure."),
  ("Recognising the sick abdomen", "Most ICU patients have a GI symptom, three at once predicts death, and bedside examination is unreliable, so the 3-6-9 rule, the 12 cm caecum and contrast CT decide who has a surgical problem."),
  ("Stomach and bowel stop moving", "Gastroparesis and lower GI paralysis come mostly from things we give or fail to correct (opioids, catecholamines, glucose, potassium), so the first treatment is to correct them, then a prokinetic, then a tube past the pylorus; Ogilvie’s gets neostigmine."),
  ("Diarrhoea: drugs before bugs", "ICU diarrhoea is defined by number, weight and consistency; the first step is a drug and feed review and a C. difficile test, not stopping the feed, and fasting separates osmotic from secretory."),
  ("Grading and acting: AGI I–IV", "ESICM grades the gut as risk, dysfunction, failure, and failure with distant organ damage, and the grade tells you whether to feed more, treat the symptom, search for a hidden cause or operate."),
]

PRIMER = "The gut is rarely the reason a patient is admitted to the ICU, but it is affected in most of them, and unlike the kidney or lung it has no single number that tells you it is failing. Its blood flow is the first to be cut when cardiac output falls, because splanchnic vasoconstriction protects the brain and heart, and it is often the last to recover. Feeding, motility and the mucosal barrier are linked: a gut that is not fed loses its villi, and a gut that cannot move cannot be fed. Intra-abdominal pressure (IAP) is measured through the bladder; 12 mmHg or more is intra-abdominal hypertension (GI05)."

L = {}

L['GUT-01'] = dict(
  sub="Gut in critical illness → Physiology → Functions and absorption sites",
  step=1,
  intro="Step 1 sets out what the gut normally does, so that each later failure has a meaning. No real question tests this card directly; it is the background for the barrier (GUT-03) and for the deficiencies that follow resection.",
  parts=[
    ('a', "**Functions: assimilation of water and nutrients; barrier (mucosa, mucin); immune (GALT, secretory IgA); exocrine; endocrine.** In critical illness the barrier and immune roles matter most: the mucosa and its mucin layer keep luminal bacteria out, and gut-associated lymphoid tissue is the body’s largest immune organ. These are the functions that enteral feeding protects (GUT-03)."),
    ('b', "**Stomach: water, alcohol, copper; makes intrinsic factor. Duodenum: iron, calcium, magnesium, folate.** Iron and calcium are taken up where the pH is still low and active transporters are concentrated, so duodenal bypass or disease causes iron-deficiency anaemia. Magnesium is the weak entry: most of it is absorbed further down, through paracellular routes in the distal jejunum and ileum and through TRPM6 channels in the colon (see FLAGS), which is why ileal resection and high-output stomas cause hypomagnesaemia. Intrinsic factor is made by parietal cells; without it B12 cannot be absorbed further down."),
    ('c', "**Jejunum: most sugars, amino acids, fatty acids, water-soluble vitamins. Ileum: vitamin B12, bile salts.** The jejunum has the largest absorptive surface. The terminal ileum alone carries the receptors for the B12–intrinsic factor complex and for bile-salt reabsorption, so it cannot be replaced by the rest of the bowel."),
    ('d', "**Colon: water, sodium, short-chain fatty acids, vitamin K.** Short-chain fatty acids made by colonic bacteria from fibre are the main fuel of colonocytes; antibiotics that remove these bacteria are one reason for ICU diarrhoea (GUT-10)."),
  ],
  mimic=[
    ("Terminal ileal loss vs duodenal loss", "Ileum: B12 deficiency and bile-salt diarrhoea. Duodenum: iron and calcium deficiency."),
  ],
  traps=[
    ("“B12 is absorbed in the stomach because intrinsic factor is made there”", "Intrinsic factor is made in the stomach; the complex is absorbed in the terminal ileum."),
  ],
  decode=[
    ("Ileal resection — which deficiency and which diarrhoea? [pattern]", "B12 deficiency and bile-salt diarrhoea (the watch line)."),
  ],
  punch="Each segment absorbs something the others cannot replace: iron and calcium in the duodenum, B12 and bile salts in the terminal ileum. In the ICU the gut’s barrier and immune roles matter more than absorption.",
)

L['GUT-02'] = dict(
  sub="Gut in critical illness → Physiology → Villus microcirculation",
  step=2,
  intro="Step 2 begins with the anatomy that makes the gut fail early in shock. No real question asks this card directly, but it explains why the mucosa dies before the wall and why lactate is a late sign of bowel ischaemia (GI04).",
  parts=[
    ('a', "**Coeliac trunk, superior and inferior mesenteric arteries, with anastomoses between each pair; venous drainage to the portal vein.** The arcades between the three trunks protect against a slow occlusion, which is why chronic narrowing of one artery is usually silent. Portal drainage means that bacteria and toxins crossing the mucosa go first to the liver (GUT-03)."),
    ('b', "**A central arteriole fans out at the tip like a fountain into descending venules.** Blood enters the villus at its base and travels to the tip in a single central vessel, then returns in venules that run close and parallel to it."),
    ('c', "**Oxygen shunts from arteriole to venule along the way (counter-current exchange), so the tension falls towards the tip.** Because the incoming and outgoing vessels lie side by side, oxygen diffuses directly from one to the other and bypasses the tip. At normal flow this costs little; when flow slows, the transit time lengthens and more oxygen is shunted, so the tip becomes hypoxic first."),
    ('d', "**The tip of the villus: lowest oxygen, highest demand.** The tip carries the mature absorptive cells, which have the highest metabolic rate. Low supply and high demand at the same place mean the tip sloughs first, and the barrier opens there."),
  ],
  mimic=[
    ("Mucosal vs transmural ischaemia", "Mucosal injury comes first and may be reversible; transmural necrosis follows prolonged ischaemia and is when lactate, peritonism and perforation appear."),
  ],
  traps=[
    ("“The villus base is the most vulnerable part”", "It is the tip (GUT-13 a)."),
  ],
  decode=[
    ("Which part of the intestinal mucosa is first injured in low-flow states, and why? [pattern]", "The villus tip, because of counter-current oxygen shunting."),
  ],
  punch="Oxygen short-circuits from arteriole to venule before it reaches the tip, so in low flow the villus tip dies first, the mucosa fails before the wall, and lactate rises late.",
)

L['GUT-03'] = dict(
  sub="Gut in critical illness → Pathophysiology → Gut as the motor of multiple organ failure",
  step=2,
  intro="Step 2 continues from the hypoxic villus tip to the whole patient. Once the mucosa is breached, the gut stops containing its bacteria and becomes a source of inflammation for distant organs. Both real questions are DocT GT: one asks what caused intra-abdominal sepsis after long antibiotic use (barrier loss, 80% right), the other asks the mechanism of ICU dysmotility (nitric oxide and VIP, 69% right).",
  parts=[
    ('a', "**Loss of barrier function.** Hypoperfusion, reperfusion and oedema open the tight junctions and slough the villus tips (GUT-02). This is the step every exam answer hangs on: an infection from gut organisms in a critically ill patient is attributed to disruption of the mucosal barrier."),
    ('b', "**Changes in intestinal microbiota.** Antibiotics, acid suppression, opioids and absent feeding replace normal commensals with pathogenic, often resistant organisms (Enterococcus, Gram-negative bacilli, Candida). Overgrowth on its own does not cause sepsis; it supplies the organisms, and the broken barrier lets them through."),
    ('c', "**Translocation of bacteria and endotoxin to portal blood and lymphatics.** What crosses the mucosa reaches the liver through the portal vein, where Kupffer cells release cytokines, or the mesenteric lymph nodes. In injured patients, portal venous blood rarely grows bacteria, which is why the emphasis moved from whole bacteria in the portal blood to what travels in the lymph (the next part)."),
    ('d', "**Formation of toxic lymph (reaches the lung first, via the thoracic duct).** Mesenteric lymph from the injured gut carries inflammatory lipids and proteins that bypass the liver and enter the systemic venous blood through the thoracic duct at the left venous angle (where the left subclavian and internal jugular veins join), so the pulmonary capillaries are the first bed they meet. This is the gut–lymph explanation for why ARDS so often follows shock and major abdominal surgery."),
    ('e', "**Dysregulated apoptosis and proliferation.** In sepsis the epithelium dies faster and renews more slowly, so the barrier cannot repair itself while the insult continues."),
    ('f', "**Sequence: hypoperfusion, then resuscitation (fluids, vasopressors), then ischaemia–reperfusion and oedema, then barrier loss.** Our treatment is part of the injury: reperfusion releases oxygen radicals, large volumes cause bowel oedema and raise IAP, and vasopressors keep splanchnic flow low. Enteral feeding works against the sequence: luminal nutrients feed enterocytes, keep villus height and stimulate IgA, which is the reason to feed early (the watch line)."),
  ],
  mimic=[
    ("Barrier loss vs commensal overgrowth", "Overgrowth supplies the organisms; barrier loss is what lets them cause infection. Asked what contributed to intra-abdominal sepsis, choose barrier disruption."),
    ("ICU ileus mechanism vs parasympathetic tone", "Ileus is driven by inflammatory mediators and sympathetic overactivity; parasympathetic activity promotes peristalsis."),
  ],
  traps=[
    ("“Overgrowth of commensal flora caused the intra-abdominal sepsis after prolonged antibiotics”", "Overgrowth is the tempting distractor because the stem mentions antibiotics, but it only supplies the organisms; the keyed and correct answer is disruption of the mucosal barrier (80% right)."),
    ("“Increased parasympathetic tone reduces peristalsis after aortic surgery”", "Parasympathetic (vagal) tone drives peristalsis. Atony comes from nitric oxide, VIP and IL-6 released by the inflamed, handled bowel, plus sympathetic overactivity and opioids."),
    ("“Whey-based or casein-based formula explains the dysmotility”", "Formula type is not the mechanism."),
  ],
  decode=[
    ("ICU patient on prolonged antibiotics develops intra-abdominal sepsis — main contributing factor? [DocT GT]", "Disruption of the gut mucosal barrier (80% right)."),
    ("Post-AAA repair, on vasopressors, distended, high residuals — mechanism of impaired motility? [DocT GT]", "Increased nitric oxide and VIP suppress the migrating motor complex (69% right)."),
  ],
  extra=[
    dict(q="Why does the bowel stop moving after major surgery or in sepsis?", a="Handling and inflammation activate muscularis macrophages, which release IL-6 and induce nitric oxide synthase; nitric oxide and VIP are inhibitory neurotransmitters that relax smooth muscle and stop the migrating motor complex. Sympathetic overactivity, catecholamine infusions and opioids add to this. That is why the treatment is to reduce opioids and correct electrolytes, and why neostigmine (more acetylcholine) works in Ogilvie’s (GUT-08)."),
  ],
  punch="Shock and our resuscitation break the mucosal barrier; antibiotics change what lies behind it; bacteria, endotoxin and toxic lymph then reach the liver and lung. Barrier loss is the answer, and early enteral feeding is the defence.",
)

L['GUT-04'] = dict(
  sub="Gut in critical illness → Assessment → How common GI symptoms are",
  step=3,
  intro="Step 3 starts with how often the gut is involved. No real question tests this card; the point an examiner would test is that GI symptoms are common and that their number, not any single one, predicts death.",
  parts=[
    ('a', "**Most ICU patients have at least one GI complaint.** ESICM 2012 puts it at up to 62% of ICU patients for at least one day. Absent bowel sounds, high gastric residuals, vomiting, diarrhoea, distension and bleeding are the usual ones."),
    ('b', "**More than 50% of mechanically ventilated patients have at least one.** In the 2013 multicentre study of 377 ventilated patients in 40 ICUs, 60% had at least one symptom during the first week (45% on day 1). Sedation, opioids, catecholamines and immobility explain why ventilated patients are most affected."),
    ('c', "**More than 20% have three or four.** In the multicentre study, two or more concurrent symptoms occurred in 20% (36% in the earlier single-centre study), and three or more in about 6%; the card’s figure fits two or more better (see FLAGS)."),
    ('d', "**Three or more concurrent GI symptoms: clearly lower survival.** In that study, three or more at once (‘GI failure’) carried a 28-day mortality of 62.5% vs 28.9%, and the number of symptoms predicted death independently of SOFA. This is the basis of grading the gut as an organ (GUT-11)."),
  ],
  mimic=[
    ("Clinically evident vs clinically important GI bleeding", "Evident (visible blood) in 5–25% of ICU patients; important (haemodynamic change or transfusion) in about 1.5–4% of ventilated patients."),
  ],
  traps=[
    ("“A single GI symptom such as absent bowel sounds predicts mortality”", "In the multicentre study no single symptom was an independent predictor; absent bowel sounds and bleeding were the most strongly associated, but it is the number of concurrent symptoms that predicts outcome."),
  ],
  decode=[
    ("How many concurrent GI symptoms mark worse ICU survival? [pattern]", "Three or more."),
  ],
  punch="Most ventilated patients have a GI symptom; three or more at once is gut failure and roughly doubles mortality.",
)

L['GUT-05'] = dict(
  sub="Gut in critical illness → Assessment → Imaging the ICU abdomen",
  step=3,
  intro="Step 3 needs imaging because the ICU abdomen cannot be examined well: the patient is sedated, the wound hurts and peritonism may be absent. Four Marrow questions link here, all asking which test or what next once something is seen: free air, a suspected abscess, diverticulitis, and free air that is not free air (Chilaiditi).",
  parts=[
    ('a', "**Ultrasound: free fluid, perfusion, organ structure; bedside.** It needs no transport and finds free fluid, gallbladder disease, hydronephrosis and the bladder, but gas and dressings defeat it in the post-operative abdomen. It is a screening tool, not the test that excludes a collection."),
    ('b', "**Abdominal X-ray: tube position; dilated loops.** Its main ICU use is to confirm where a feeding tube lies: a nasogastric tube is checked by X-ray or an aspirate pH of 5.5 or less before any feed. If a patient desaturates and airway pressures rise just after insertion and the film shows the tube in a bronchus, stop the feed, remove the tube and re-insert it under direct or video-laryngoscope vision, then confirm again; never advance it, and a cuffed tracheal tube does not prevent this. An erect chest film also shows free gas under the diaphragm."),
    ('c', "**Dilated bowel, the 3-6-9 rule: small bowel over 3 cm; colon over 6 cm; caecum over 9 cm.** These are the ESICM definitions of dilatation. The caecum has the widest diameter and so, by Laplace’s law, the highest wall tension for any pressure, which is why it is the part that perforates."),
    ('d', "**High risk of perforation: caecum over 12 cm.** Above 12 cm, and more so when distension has lasted more than 6 days, ischaemia and perforation become likely; this is the threshold for decompression in Ogilvie’s (GUT-08)."),
    ('e', "**Contrast CT: free air or fluid; wide bowel; thick wall; pneumatosis; reduced or interrupted mesenteric flow.** CT is the definitive test for the septic post-operative abdomen: it finds and guides drainage of an abscess, shows anastomotic leak and diverticular perforation, and the CT angiogram phase shows mesenteric ischaemia (GI04). Plain films and ultrasound are insensitive in this setting."),
  ],
  mimic=[
    ("Pneumoperitoneum vs Chilaiditi sign", "Chilaiditi is colon lying between liver and diaphragm: gas under the right hemidiaphragm with haustra visible, no peritonism, and CT shows no free air. Treat conservatively (nasogastric decompression, bowel rest)."),
    ("Ultrasound vs CT for a post-operative abscess", "Ultrasound is limited by gas and wounds; contrast CT is definitive and guides percutaneous drainage."),
  ],
  traps=[
    ("“Free air on X-ray in a cirrhotic — go to laparotomy” when CT shows none", "That is Chilaiditi; treat with nasogastric decompression and observation."),
    ("“Sigmoidoscopy or colonoscopy to confirm acute diverticulitis”", "Endoscopy risks perforation in the acute phase; contrast CT of abdomen and pelvis is the test."),
    ("“A tube in the bronchus can be withdrawn a little and advanced again blind”", "Remove it, re-insert under vision and confirm before any feed."),
  ],
  decode=[
    ("Febrile and septic 2 days after open appendicectomy — test to establish the pathology? [Marrow]", "Contrast CT abdomen (abscess)."),
    ("LLQ pain, fever, WBC 34,000 — next step? [Marrow]", "Contrast-enhanced CT abdomen and pelvis (diverticulitis)."),
    ("Cirrhotic, free air on X-ray but none on CT — next step? [Marrow]", "Nasogastric decompression; Chilaiditi."),
    ("Alcoholic, chronic epigastric pain, free air under the diaphragm? [Marrow]", "Perforated peptic ulcer (T_a1086ece)."),
  ],
  punch="The bedside abdomen lies in the ICU, so imaging decides: X-ray for tubes and loops (3-6-9, caecum 12 cm is the danger), and contrast CT whenever sepsis may be coming from the abdomen.",
)

L['GUT-06'] = dict(
  sub="Gut in critical illness → Symptoms → Causes of gastroparesis",
  step=4,
  intro="Step 4 is the gut that stops moving, starting with the stomach. The causes split into lasting disease and transient, reversible triggers, and in the ICU it is almost always the transient ones. The one real question (DocT GT) gives a diabetic with glucose 350 who has just started clonidine; the answer is to fix the triggers, although DocT keys a venting gastrostomy.",
  parts=[
    ('a', "**Lasting: diabetes mellitus, renal insufficiency, post-vagotomy, systemic sclerosis and dermatomyositis, functional dyspepsia.** Diabetes damages the vagus and the interstitial cells of Cajal that pace the stomach; vagotomy removes the motor supply directly; scleroderma replaces smooth muscle with fibrosis; uraemia slows the stomach through toxins and autonomic neuropathy."),
    ('b', "**Transient: opioids; beta-agonists, alpha-2 agonists; hyperglycaemia; low potassium, low magnesium; acidosis; stress, head injury, burns.** Opioids act on gut μ receptors; beta-agonists and alpha-2 agonists (clonidine, dexmedetomidine) relax smooth muscle or inhibit acetylcholine release; acute hyperglycaemia itself slows emptying, even in non-diabetics; low potassium and magnesium weaken smooth-muscle contraction. Head injury and burns produce a catecholamine surge. Each of these can be removed, so they are the first things to look for. The card’s watch line notes that beta-agonists (not beta-blockers) slow emptying."),
  ],
  mimic=[
    ("Gastroparesis vs gastric outlet obstruction", "Both give large gastric contents; endoscopy or CT shows no mechanical obstruction in gastroparesis."),
  ],
  traps=[
    ("“Percutaneous venting gastrostomy is the best next step” (DocT GT key)", "The key is wrong: only 7% chose it. Hyperglycaemia and a new alpha-2 agonist are reversible triggers; dietary change and glycaemic control (option B) come first, venting gastrostomy only for refractory disease."),
    ("“Beta-blockers slow gastric emptying”", "Beta-agonists do; the notes misprint it (the watch line)."),
  ],
  decode=[
    ("Type 1 DM, new clonidine, glucose 350, retained gastric contents, no obstruction — best next step besides reviewing drugs? [DocT GT]", "Dietary modification and glycaemic control (key D, venting gastrostomy, is wrong)."),
  ],
  punch="Most ICU gastroparesis is transient and made by us: opioids, catecholamines, alpha-2 agonists, high glucose, low potassium or magnesium. Find and remove the trigger before any tube.",
)

L['GUT-07'] = dict(
  sub="Gut in critical illness → Treatment → Gastroparesis",
  step=4,
  intro="Step 4 continues with what to do once the stomach is not emptying. The order is fixed: correct the cause, then a prokinetic, then a tube past the pylorus. The one real question (DocT GT, the same diabetic on clonidine) tests the order, and its key jumps straight to a venting gastrostomy.",
  parts=[
    ('a', "**Erythromycin (motilin-receptor agonist) and metoclopramide (dopamine D2 antagonist).** Erythromycin mimics motilin and triggers strong antral contractions of the migrating motor complex; ESPEN 2023 makes it the first-line ICU prokinetic (100–250 mg IV three times daily). Metoclopramide blocks D2 receptors and releases acetylcholine in the upper gut; it is used alone or with erythromycin, and the combination works better than either. Erythromycin prolongs QT and promotes resistance; metoclopramide can cause extrapyramidal effects."),
    ('b', "**Correct electrolytes and glucose; cut opioids and sedatives.** These remove the causes listed on GUT-06. In the GT stem this is the answer: control the glucose, stop or change the clonidine, adjust the diet."),
    ('c', "**Post-pyloric tube: gastric residual over 500 mL; gastroparesis; failed prokinetics.** ESICM 2012 and ESPEN 2023 put post-pyloric feeding after prokinetics have failed, not as first choice. A single residual over 200 mL calls for bedside review, not stopping the feed; above 500 mL the gastric feed is held (the watch line). ASPEN/SCCM 2016 advise against using residuals as part of routine monitoring."),
    ('d', "**Maximum 5 days: tachyphylaxis.** Motilin receptors down-regulate, so erythromycin loses most of its effect by about 72 hours (the watch line). ESPEN 2023 suggests using it for 24–48 hours and stopping after three days, which is shorter than the card’s limit (see FLAGS)."),
  ],
  mimic=[
    ("Erythromycin vs metoclopramide", "Erythromycin: motilin agonist, first line in ESPEN, QT prolongation. Metoclopramide: D2 antagonist, extrapyramidal effects."),
  ],
  traps=[
    ("“Venting gastrostomy is the best next step” (DocT GT key D)", "The key is wrong: with a reversible trigger in the stem, correct it first (glucose, the alpha-2 agonist, diet), then a prokinetic; venting gastrostomy is a last resort."),
    ("“Stop gastric feeds for a residual of 250 mL”", "Over 200 mL means review at the bedside; stop only above 500 mL."),
    ("“Erythromycin can be continued for weeks”", "Its effect fades within about 3 days."),
  ],
  decode=[
    ("Type 1 DM, new clonidine, glucose 350, retained gastric contents — best next step? [DocT GT]", "Glycaemic control and dietary change; key D (venting gastrostomy) is wrong."),
    ("ICU feed intolerance not solved by prokinetics — next? [pattern]", "Post-pyloric feeding."),
  ],
  punch="Gastroparesis treatment runs in order: remove the cause, give erythromycin (with or without metoclopramide) for a few days, then pass a tube beyond the pylorus. A venting gastrostomy is for refractory disease only.",
)

L['GUT-08'] = dict(
  sub="Gut in critical illness → Symptoms → Bowel sounds, paralysis and Ogilvie’s",
  step=4,
  intro="Step 4 reaches the lower gut, where ileus becomes Ogilvie’s syndrome when the colon dilates without an obstruction. Three real DocT GT questions link here: the mechanism of ICU dysmotility, the caecal size and duration that predict perforation, and naming acute colonic pseudo-obstruction from a 13 cm caecum.",
  parts=[
    ('a', "**Auscultate for 1 minute over each of the 4 quadrants.** ESICM 2012 actually says at least 1 minute in two quadrants, repeated at least once within a short time (see FLAGS); normal is about 5–35 sounds a minute. Listen before palpating, which stimulates peristalsis. Present bowel sounds do not prove the gut is working; in the multicentre study absent bowel sounds were among the symptoms most strongly associated with death, although no single symptom predicted it independently."),
    ('b', "**Lower GI paralysis: 3 days without stool, with no mechanical obstruction.** This is the ESICM definition. The cut-off is pragmatic: no stool on the first one or two ICU days is common and not in itself abnormal, and obstruction must be excluded because the treatment (laxatives, prokinetics) would be wrong for it."),
    ('c', "**Hyperperistalsis suggests bowel obstruction.** Loud, frequent, high-pitched sounds are the bowel trying to push past a blockage; their absence later can mean it has given up or become ischaemic."),
    ('d', "**Ogilvie’s syndrome: acute colonic pseudo-obstruction, massive colonic dilatation without a mechanical cause.** The mechanism is autonomic: sympathetic overactivity and parasympathetic suppression of the distal colon, with nitric oxide and VIP released by inflammation, opioids and surgery (GUT-03). It follows major surgery, trauma, sepsis and cardiac illness. Mechanical obstruction must be excluded, usually by CT or water-soluble contrast enema. Perforation risk rises with a caecum over 12 cm and distension for more than 6 days: in the ASCRS 2021 data ischaemia or perforation occurred in 0%, 7% and 23% at under 12, 12–14 and over 14 cm. It is AGI grade IV (GUT-11)."),
    ('e', "**Its drug: neostigmine.** It inhibits acetylcholinesterase, so more acetylcholine reaches the colon and restores the parasympathetic drive that is missing; about 90% decompress. The watch line gives the standard regimen: 2 mg IV over 3–5 minutes, with ECG monitoring and atropine or glycopyrrolate at hand for bradycardia. ESICM suggests it when the caecum is over 10 cm and there is no improvement in 24 hours; colonoscopic decompression follows if it fails. It is contraindicated in ischaemia or perforation, pregnancy, uncontrolled arrhythmia and active bronchospasm."),
    ('f', "**Preventing paralysis: correct electrolytes and glucose, avoid fluid overload, minimise opioids and sedatives, early low-dose enteral feeding, laxatives.** Bowel oedema from excess fluid and low potassium both weaken contraction. ESICM advises starting laxatives early or prophylactically. After laparotomy the same measures, nil by mouth, nasogastric decompression and mobilisation treat ordinary post-operative ileus; relaparotomy is for signs of obstruction, leak or ischaemia (fever, peritonism, rising lactate) or failure to settle."),
  ],
  mimic=[
    ("Ogilvie’s vs mechanical large bowel obstruction or volvulus", "Ogilvie’s has no transition point or twist on CT and no obstruction on contrast enema."),
    ("Ogilvie’s vs toxic megacolon", "Toxic megacolon is colitis (C. difficile, ulcerative colitis) with systemic toxicity and bloody diarrhoea; Ogilvie’s is non-inflammatory dilatation."),
  ],
  traps=[
    ("“Caecum 8 cm for 3 days is the highest perforation risk”", "Risk depends on size over 12 cm and duration over 6 days; 13 cm for 7 days is the answer (73% right)."),
    ("“Increased parasympathetic tone causes the atony”", "The colon lacks parasympathetic drive; that is why neostigmine works."),
    ("“Ogilvie’s is treated with atropine”", "Atropine blocks acetylcholine and would worsen it; it is kept at hand for neostigmine’s bradycardia (GUT-13 f)."),
  ],
  decode=[
    ("Ogilvie’s syndrome — finding with the highest risk of caecal perforation? [DocT GT]", "Caecal diameter 13 cm for 7 days."),
    ("Ventilated, distended, caecum 13 cm, no mechanical obstruction — diagnosis? [DocT GT]", "Acute colonic pseudo-obstruction."),
    ("Post-AAA, vasopressors, no stool or flatus, high residuals — mechanism? [DocT GT]", "Nitric oxide and VIP suppress the migrating motor complex."),
  ],
  punch="No stool for 3 days without obstruction is paralysis; massive colonic dilatation without obstruction is Ogilvie’s. Correct the causes, give neostigmine, and decompress before the caecum passes 12 cm for long.",
)

L['GUT-09'] = dict(
  sub="Gut in critical illness → Symptoms → Diarrhoea: definition",
  step=5,
  intro="Step 5 is the opposite problem, the gut that empties too fast. Diarrhoea needs a definition because loose stools are common on enteral feeds. The one real question (Marrow) asks what to do when a fed ARDS patient develops diarrhoea: keep feeding at the same rate.",
  parts=[
    ('a', "**Three or more stools a day.** ESICM defines diarrhoea as three or more loose or liquid stools a day, together with the weight criterion; frequency alone does not count if the stools are formed."),
    ('b', "**Stool weight of 200 g/day or more.** ESICM gives 200–250 g/day (or over 250 mL/day). Weight is the objective measure, and faecal management systems make it measurable."),
    ('c', "**Consistency 5–7 on the Bristol stool chart.**"),
    ('d', "**Bristol: 1–2 constipated; 3–4 normal; 5 soft blobs; 6 mushy; 7 liquid, no solid pieces.** Consistency reflects transit time: the faster the transit, the less water the colon absorbs."),
  ],
  mimic=[
    ("Diarrhoea on enteral feed vs feed intolerance", "Diarrhoea alone is not intolerance; feeding continues while the cause is sought."),
  ],
  traps=[
    ("“Diarrhoea on enteral feeding: stop or slow the feed”", "Keep the same rate; the feed is rarely the cause and stopping it starves the gut."),
    ("“Raise the feed density or rate, give fluid boluses, or add supplemental PN”", "None of these; supplemental PN is not started before day 7 for this."),
  ],
  decode=[
    ("ARDS patient on NG feeds develops diarrhoea — next step? [Marrow]", "Continue the current feed rate; review drugs and test for C. difficile."),
  ],
  punch="ICU diarrhoea is three or more loose stools with over 200 g a day (Bristol 5–7). It is not a reason to stop the feed: keep feeding, stop laxatives and prokinetics, and test for C. difficile.",
)

L['GUT-10'] = dict(
  sub="Gut in critical illness → Symptoms → Osmotic vs secretory diarrhoea",
  step=5,
  intro="Step 5 then separates the two mechanisms, because the cause decides the treatment. The one real question (DocT GT) is about the first step in new watery diarrhoea in a fed septic patient on antibiotics: a drug review, stopping prokinetics (65% right).",
  parts=[
    ('a', "**Volume: osmotic moderate; secretory large (litres).** In osmotic diarrhoea, unabsorbed solute holds water in the lumen, and the volume is limited by how much solute is given. In secretory diarrhoea the epithelium actively pumps chloride and water out, which can reach litres a day."),
    ('b', "**Stool: osmotic soft; secretory watery, plasma-like (high sodium chloride).** Secreted fluid resembles plasma, so its sodium and potassium account for almost all of the stool osmolality. The stool osmotic gap, 290 − 2 × (Na + K), is over 100 in osmotic and under 50 in secretory diarrhoea (the watch line; some texts use 125 for osmotic)."),
    ('c', "**Fasting: osmotic improves; secretory no change.** Stopping the feed removes the solute, so osmotic diarrhoea settles; secretion continues regardless. This is a diagnostic test, not a treatment: in the ICU the feed is continued (GUT-09)."),
    ('d', "**Causes: osmotic — high-osmolar feed or drugs, fast transit, small absorptive area, intolerance; secretory — infection, mucosal inflammation, colonic toxins, bile acid malabsorption.** In the ICU the commonest osmotic causes are drugs: sorbitol in liquid medicines, magnesium salts, lactulose, and prokinetics that speed transit. Secretory causes are C. difficile and other infections, and bile acids reaching the colon after ileal disease or resection (GUT-01)."),
    ('e', "**Other: osmotic — flatulence (carbohydrate); secretory — dehydration, electrolyte loss.** Fermentation of unabsorbed carbohydrate gives gas; litres of plasma-like fluid cause hypovolaemia, hypokalaemia and a normal-anion-gap acidosis from bicarbonate loss."),
  ],
  mimic=[
    ("Osmotic vs secretory", "Fasting stops osmotic diarrhoea and the osmotic gap is over 100; secretory continues on fasting with a gap under 50."),
  ],
  traps=[
    ("“Start loperamide to reduce stool frequency”", "Not before C. difficile is excluded: antimotility agents hold toxin in the colon and risk toxic megacolon."),
    ("“Stop enteral nutrition or switch to TPN until the diarrhoea settles”", "Keep feeding; the first step is a drug review."),
    ("“Secretory diarrhoea improves with fasting”", "Osmotic improves; secretory does not (GUT-13 e)."),
  ],
  decode=[
    ("Septic, on antibiotics and EN, new watery stools, afebrile, C. difficile pending — next step? [DocT GT]", "Review medications and consider stopping prokinetics (65% right)."),
  ],
  punch="Osmotic diarrhoea stops when the solute stops and has a wide osmotic gap; secretory diarrhoea is large, plasma-like and ignores fasting. In the ICU, review drugs first and give no antimotility agent until C. difficile is excluded.",
)

L['GUT-11'] = dict(
  sub="Gut in critical illness → AGI grading → ESICM grades I–IV",
  step=6,
  intro="Step 6 brings the symptoms together into one grade so that the gut can be scored like other organs. No real question tests the table directly; examiners would ask which grade a given scenario is, and the boundary between III and IV is the one most often confused.",
  parts=[
    ('a', "**Grade I, risk of dysfunction: transient, self-limiting (post-operative nausea, absent bowel sounds after surgery).** ESICM also includes reduced motility in the early phase of shock. The gut is threatened but expected to recover; the action is to feed early."),
    ('b', "**Grade II, dysfunction: needs intervention to meet nutrient and fluid needs (gastroparesis with high residuals, lower GI paralysis, diarrhoea, IAP 12–15, visible blood).** The gut works only with help. Feeding intolerance (under 20 kcal/kg/day enterally by 72 hours) belongs here, and IAP 12–15 is IAH grade I (GI05)."),
    ('c', "**Grade III, failure: function not restored despite intervention (persistent feed intolerance, bowel dilatation, IAP 15–20).** Treatment has been tried and failed; ESICM adds an abdominal perfusion pressure under 60 mmHg. IAP 15–20 is IAH grade II."),
    ('d', "**Grade IV, failure with distant organ dysfunction: immediately life-threatening (bowel ischaemia, bleeding with shock, Ogilvie’s, abdominal compartment syndrome).** What defines grade IV is that the gut is now causing other organs to fail, so it needs an emergency procedure. Abdominal compartment syndrome is IAP over 20 with new organ failure, which is why it sits here and not in grade III."),
  ],
  mimic=[
    ("AGI III vs IV", "III: the gut alone has failed despite treatment. IV: gut failure is now causing distant organ failure or is immediately life-threatening (ACS, ischaemia, bleeding with shock)."),
  ],
  traps=[
    ("“Abdominal compartment syndrome is AGI grade III”", "It is grade IV, because new organ failure is part of its definition (GUT-13 g)."),
  ],
  decode=[
    ("Persistent feed intolerance despite prokinetics, IAP 17 — AGI grade? [pattern]", "Grade III."),
    ("IAP 24 with new oliguria — AGI grade? [pattern]", "Grade IV (abdominal compartment syndrome)."),
  ],
  extra=[
    dict(q="Has AGI grading been replaced?", a="ESICM researchers later built the Gastrointestinal Dysfunction Score (GIDS, Clinical Nutrition 2021), a 0–4 score on the same scaffold that adds to SOFA in predicting 28- and 90-day mortality. AGI I–IV is still the grading the exam uses."),
  ],
  punch="Risk, dysfunction, failure, and failure with distant organ damage: grade II needs help, grade III does not respond to it, and grade IV is the gut making other organs fail.",
)

L['GUT-12'] = dict(
  sub="Gut in critical illness → AGI grading → Management by grade",
  step=6,
  intro="Step 6 ends with what each grade asks of you. The one real question (DocT GT) is a grade II problem, new diarrhoea in a fed septic patient, and tests the first action: review drugs, keep feeding, no loperamide until C. difficile is excluded (65% right).",
  parts=[
    ('a', "**Grade I: fix fluids and electrolytes; start or increase enteral feed; cut drugs that slow the gut.** ESICM recommends enteral feeding within 24–48 hours (1B), and limiting catecholamines and opioids where possible; feeding protects the villi (GUT-03)."),
    ('b', "**Grade II: treat the symptom (prokinetic, laxative, post-pyloric tube); measure IAP; feed to 50–80% of needs in the acute phase, 80–100% by day 3.** Enteral feeding is started or continued, not stopped. For diarrhoea, the treatment of the symptom is a drug review: stop prokinetics, laxatives, sorbitol-containing syrups and magnesium salts, and test for C. difficile. Antimotility agents (loperamide, diphenoxylate) are avoided until infection is excluded, because in invasive or C. difficile colitis they raise the risk of bacteraemia and toxic megacolon. ESPEN 2023 frames the energy target as no more than 70% of expenditure early and up to 80–100% after day 3."),
    ('c', "**Grade III: look for undiagnosed abdominal pathology; treat IAH; retry minimal enteral feed; consider supplemental parenteral nutrition after day 4–7.** Persistent failure despite treatment means a hidden cause until proved otherwise: cholecystitis, peritonitis, a collection, ischaemia, so this is when CT is done (GUT-05). Minimal (trophic) feeding is kept for its effect on the mucosa. ESICM 2012 advised avoiding supplemental PN in the first 7 days; ESPEN 2023 puts its timing at days 4–7."),
    ('d', "**Grade IV: stop enteral feed, open the nasogastric tube; endoscopy, interventional radiology or laparotomy.** Feeding an ischaemic or compartment-bound gut adds oxygen demand it cannot meet; the ESICM 2017 enteral feeding guideline suggests delaying EN in uncontrolled shock, uncontrolled hypoxaemia and acidosis, uncontrolled upper GI bleeding, gastric aspirate over 500 mL in 6 hours, bowel ischaemia, bowel obstruction, abdominal compartment syndrome, and a high-output fistula without distal feeding access. There is no conservative treatment for grade IV: the cause is removed by a procedure. Re-evaluate 6-hourly at first, and watch for refeeding syndrome when feeding restarts (the watch line)."),
  ],
  mimic=[
    ("Grade II diarrhoea vs grade IV gut", "Grade II: keep feeding and treat the cause. Grade IV: stop feeding and intervene."),
  ],
  traps=[
    ("“Initiate loperamide” for new ICU diarrhoea", "Not until C. difficile is excluded (toxic megacolon); the first step is a drug review."),
    ("“Hold EN and start TPN” or “stop EN until the diarrhoea resolves”", "Feeding continues in grade II; stopping it is for grade IV."),
  ],
  decode=[
    ("Septic, on antibiotics and EN, new watery stools, C. difficile test pending — most appropriate next step? [DocT GT]", "Review medications and consider stopping prokinetics."),
    ("Persistent feed intolerance despite prokinetics — what must you look for? [pattern]", "Undiagnosed abdominal pathology (AGI III)."),
  ],
  punch="Grade I: feed. Grade II: keep feeding and treat the symptom (in diarrhoea, review the drugs first). Grade III: search for a hidden abdominal cause. Grade IV: stop the feed and intervene.",
)

L['GUT-13'] = dict(
  sub="Gut in critical illness → Sweep → True or false",
  step=6,
  intro="Step 6 closes with a sweep of the deck. No real question links to it, but each statement is a version of a distractor from the linked questions: the wrong part of the villus, the wrong caecal size, the wrong drug in Ogilvie’s and the wrong AGI grade.",
  parts=[
    ('a', "**False: the tip, not the base, is most prone to ischaemia.** Counter-current exchange removes oxygen before blood reaches the tip (GUT-02)."),
    ('b', "**True: three or more GI symptoms predict worse survival.** In the multicentre study 28-day mortality was 62.5% vs 28.9% (GUT-04)."),
    ('c', "**False: the caecum is dilated over 9 cm; 12 cm risks perforation.** Over 6 cm is the threshold for the rest of the colon (GUT-05)."),
    ('d', "**True: erythromycin is a motilin agonist.** It is the first-line ICU prokinetic, effective for about 3 days (GUT-07)."),
    ('e', "**False: osmotic diarrhoea improves with fasting.** Secretory diarrhoea continues (GUT-10)."),
    ('f', "**False: Ogilvie’s is treated with neostigmine.** Atropine is kept ready to treat neostigmine’s bradycardia (GUT-08)."),
    ('g', "**False: abdominal compartment syndrome is AGI grade IV.** New organ failure is part of its definition (GUT-11)."),
    ('h', "**False: bowel paralysis means three days without stool.** With mechanical obstruction excluded (GUT-08)."),
  ],
  mimic=[
    ("Caecum 9 cm vs 12 cm", "9 cm: dilated. 12 cm (especially over 6 days): risk of perforation."),
  ],
  traps=[
    ("“Atropine for Ogilvie’s”", "Neostigmine; atropine is its antidote."),
  ],
  decode=[
    ("Which AGI grade is abdominal compartment syndrome? [pattern]", "Grade IV."),
  ],
  punch="Tip not base, 9 cm dilated and 12 cm dangerous, erythromycin is a motilin agonist, fasting helps osmotic diarrhoea, neostigmine not atropine, ACS is grade IV, paralysis is 3 days.",
)

FLAGS = {
  'GUT-01': "Duodenum row lists magnesium. Magnesium is absorbed mainly in the distal jejunum and ileum (paracellular) and in the colon (TRPM6/7), not chiefly in the duodenum; iron, calcium (active transport) and folate are correct. Minor.",
  'GUT-04': "c: ‘more than 20% have three or four symptoms’ could not be confirmed. In the ESICM multicentre study (Reintam Blaser 2013, 377 ventilated patients) two or more concurrent symptoms occurred in 20% (36% in the earlier single-centre study) and three or more in 6.4%; the 20% figure fits two or more. The explanation states this.",
  'GUT-07': "d: ‘maximum 5 days’ is longer than ESPEN 2023, which suggests erythromycin for 24–48 h and stopping after three days; the card’s own watch line says its effect fades by 72 h. Not a card error otherwise: the linked DocT GT (GT1o Q52) keys D, venting gastrostomy, which is wrong as a next step; the answer is B (glycaemic control and diet, with the clonidine reviewed). The same key affects GUT-06.",
  'GUT-08': "a: ESICM 2012 says auscultate for at least 1 minute in TWO quadrants, repeated at least once within a short time; the card says each of 4 quadrants. Neostigmine regimen in the watch line agrees with ASCRS 2021 (2–5 mg IV over 1–5 min; trial dose 2 mg).",
  'GUT-12': "b: the ‘50–80% acute, 80–100% by day 3’ targets are not in ESICM 2012; the current ESPEN 2023 wording is no more than 70% of energy expenditure early and up to 80–100% after day 3. c: ESICM 2012 itself advised avoiding supplemental PN in the first 7 days; ‘day 4–7’ matches ESPEN 2023.",
}
