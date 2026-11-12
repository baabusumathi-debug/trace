# SPECIAL03 — Explain v3 ("Learn" depth): nutrition in the ICU — the metabolic response, why the gut is fed, assessment and NUTRIC, when and how to start EN, access,
# contraindications, formulas, energy measurement, targets, micronutrients, refeeding, intolerance, EN vs PN, when to give PN, overfeeding, true/false.
# No mnemonics or hooks. Driven by the real questions in qpack/SPECIAL03.md (22 question links; NUT-09 asked 4 times, NUT-04 and NUT-14 three times each,
# NUT-05, NUT-12 and NUT-13 twice). NUT-01, 02, 03, 10 and 17 have no linked question and get short explanations with [pattern] decode items.
# qbank.json cards["SPECIAL03|…"] has no `fix` entries; its `lines`/`cross` notes (NUT-06, 08, 09, 11, 14, 16) were read and used.
# Checked online on 13 Nov 2026:
#  - ESPEN practical and partially revised ICU guideline (Singer, Clin Nutr 2023;42:1671), full text: early EN within 48 h (R6); early EN over early PN (R7); delay EN if shock uncontrolled,
#    uncontrolled hypoxaemia/hypercapnia/acidosis, active upper GI bleeding, overt bowel ischaemia, high-output fistula without distal access, abdominal compartment syndrome,
#    gastric aspirate >500 mL/6 h (R11); low-dose EN as soon as shock is controlled; PN within 3–7 days if EN contraindicated (R17); PN not started until all strategies to improve EN
#    tolerance tried (R18); SPN timing suggested days 4–7 (commentary); indirect calorimetry to measure EE (R19); hypocaloric ≤70% of EE early (R23), 80–100% of measured EE after day 3 (R24);
#    protein 1.3 g/kg/day progressively (R25); enteral glutamine only in burns >20% TBSA and trauma, not in other ICU patients (R30–32); post-pyloric if intolerance not solved by prokinetics (R16);
#    IV erythromycin first-line prokinetic (R55); refeeding hypophosphataemia: restrict energy for 48 h then increase gradually (R59), electrolytes 2–3 times daily (R58).
#  - ASPEN/SCCM 2021–22 update (Compher, JPEN 2022): 12–25 kcal/kg in the first 7–10 days; protein 1.2–2.0 g/kg/day kept from 2016; either PN or EN acceptable; do not start SPN before day 7.
#  - EFFORT Protein (Heyland, Lancet 2023; 1,329 patients): ≥2.2 vs ≤1.2 g/kg/day prescribed (1.6 vs 0.9 delivered); no difference in discharge alive; 60-day mortality 34.6 vs 32.1% (NS);
#    worse outcomes with high protein in baseline AKI and higher SOFA (subgroups, hypothesis-generating).
#  - NUTRIREA-2 (Reignier, Lancet 2018; 2,410 ventilated patients in shock): 28-day mortality 37 vs 35% (NS); EN arm more vomiting, diarrhoea, bowel ischaemia 2% vs <1% (19 vs 5, HR 3.84),
#    acute colonic pseudo-obstruction 1% vs <1% (11 vs 3, HR 3.7).
#  - NUTRIREA-3 (Lancet Respir Med 2023; ~3,000): 6 kcal/kg and 0.2–0.4 g/kg vs 25 kcal/kg and 1.0–1.3 g/kg; 90-day mortality 41.3 vs 42.8% (NS); low arm faster readiness for discharge, fewer GI complications.
#  - CALORIES (Harvey, NEJM 2014; 2,388): early PN vs EN within 36 h; 30-day mortality 33.1 vs 34.2%; no difference in infections; PN less hypoglycaemia and vomiting.
#  - TARGET (NEJM 2018; 3,914 analysed): 1.5 vs 1.0 kcal/mL; 90-day mortality 26.8 vs 25.7% (NS).
#  - EDEN (JAMA 2012; 1,000 ALI): trophic ~400 kcal/day (10 mL/h start) for 6 days vs full; VFDs 14.9 vs 15.0; 60-day mortality 23.2 vs 22.2%.
#  - PermiT (Arabi, NEJM 2015; 894): 40–60% vs 70–100% with the same protein (1.2–1.5 g/kg); 90-day mortality 27.2 vs 28.9% (NS).
#  - EPaNIC (Casaer, NEJM 2011; 4,640): late PN (day 8) vs early: fewer new infections 22.8 vs 26.2%, more discharged alive from ICU by day 8, lower cost, no mortality difference.
#  - NICE CG32 refeeding: high risk = one of BMI <16, weight loss >15% in 3–6 months, little or no intake >10 days, low K/PO4/Mg before feeding; or two of BMI <18.5, loss >10%, intake little >5 days,
#    alcohol or drugs (insulin, chemotherapy, antacids, diuretics); start ≤10 kcal/kg/day, 5 kcal/kg/day in extreme cases (BMI <14, negligible intake >15 days); thiamine 200–300 mg daily.
# From memory, not re-checked online (confident unless marked): NUTRIC bands and cut-offs (Heyland 2011; modified ≥5 high risk, Rahman 2016); NRS-2002 ≥3 at risk, ≥5 high risk (ASPEN 2016);
#  Harris-Benedict coefficients; Weir equation; RQ range 0.67–1.3; indirect calorimetry unreliable at FiO2 >0.6; ESPEN lipid ≤1.5 g/kg/day and glucose ≤5 mg/kg/min; propofol 1.1 kcal/mL;
#  ASPEN 2016 obesity targets (11–14 kcal/kg actual weight BMI 30–50, 22–25 kcal/kg IBW BMI >50; protein 2.0 g/kg IBW BMI 30–40, up to 2.5 BMI ≥40); ESPEN adjusted body weight in obesity;
#  REDOXS (NEJM 2013; glutamine raised mortality); Heidegger SPN trial (Lancet 2013); Doig refeeding RCT (Lancet Respir Med 2015); Puthucheary muscle-wasting data (JAMA 2013);
#  phosphate conversion (mg/dL × 0.323 = mmol/L); ASPEN 2020 refeeding consensus; Harrison quick REE (men 900 + 10W, women 700 + 7W).
# Independent review 13 Nov 2026 (special03_review.md): NUTRIC/mNUTRIC cut-offs, ASPEN 2016 risk/obesity/SPN, ASPEN 2022, AARC IC limits, ESPEN 2023 R13/R27/R29/R40/R55/R59,
#  REDOXS, Heidegger, Doig, EPaNIC, EFFORT, NUTRIREA-3, TARGET, NICE CG32 re-checked online; Freka length not confirmed (see FLAG).

SPINE = [
  ("Catabolism you cannot switch off", "Critical illness drives stress hormones, insulin resistance and muscle breakdown to make glucose, and feeding cannot suppress that early production, so full feeding in the first days overfeeds."),
  ("Who is at nutritional risk", "Weight, intake and muscle tell you who is malnourished, oedema makes skinfolds and bioimpedance useless, and a high NUTRIC score (6 or more, or 5 or more without IL-6) picks those who gain most from feeding."),
  ("Start the gut early, gently", "Give low-dose enteral feed within 24–48 hours through the stomach unless shock is uncontrolled or the gut is ischaemic, obstructed or inaccessible, and advance slowly."),
  ("How much energy and protein", "Measure energy with indirect calorimetry where possible, give no more than about 70% of it early and 80–100% after day 3, and build protein towards 1.3 g/kg/day."),
  ("When feeding itself harms", "Refeeding a starved patient crashes phosphate, intolerance shows as residuals, distension or diarrhoea, and hidden calories and excess glucose overfeed."),
  ("When to use the vein", "Parenteral nutrition is as safe as enteral when dosed sensibly, but it is kept for an unusable gut or a failing enteral route, and in a well-nourished patient it can wait until about day 8."),
]

PRIMER = "A critically ill patient’s energy expenditure is set by his illness, not by what he eats, and in the first days his liver makes much of the glucose he needs whatever he is fed. Energy is counted in kcal per kg per day and protein in g per kg per day, using actual weight in most patients and an ideal or adjusted weight in the obese. The two routes are enteral (into the gut, by tube: gastric or post-pyloric) and parenteral (into a vein, usually central). The two guideline bodies quoted throughout are ESPEN (European, 2019, partly revised 2023) and ASPEN/SCCM (American, 2016, updated 2022); where they differ, the DocT stems linked to this deck mostly use ASPEN numbers."

L = {}

L['NUT-01'] = dict(
  sub="Nutrition → Metabolism → The stress response",
  step=1,
  intro="Step 1 is why ICU feeding works differently from ordinary feeding. Illness switches the body into a catabolic state in which it breaks itself down for fuel and does not listen to incoming food. Every later decision about how much and how fast follows from this.",
  parts=[
    ('a', "**Stress hormones (cortisol, glucagon, adrenaline) and insulin resistance.** These counter-regulatory hormones, with cytokines such as IL-6 and TNF, push the liver to release glucose and the tissues to resist insulin, so glucose stays high for the brain, immune cells and wounds. Stress hyperglycaemia is the visible result."),
    ('b', "**Catabolism: glycogenolysis, gluconeogenesis from amino acids, lactate and glycerol, proteolysis (muscle to liver), lipolysis; hyperglycaemia.** Glycogen lasts about a day, so after that glucose is made from amino acids taken out of muscle, which is why the patient wastes fast."),
    ('c', "**The body makes 50–75% of its glucose needs itself early on; feeding cannot switch this off.** In health, eating suppresses hepatic glucose output; in critical illness it does not. Full feeding in the first days is added on top of this endogenous supply, so the patient is overfed even when the figure on the chart says 100%. That is the reason for ESPEN’s hypocaloric start (no more than 70% of expenditure early, NUT-10)."),
    ('d', "**Energy expenditure rises about 10–15% in critical illness and about 50% in trauma.** Expenditure is raised less than most people assume, and sedation, ventilation and paralysis lower it further; burns raise it most. Overestimating needs is the commoner error."),
    ('e', "**Early protein may be essential: 0.8 g/kg/day, building to over 1.2.** Protein loss cannot be stopped by feeding, but delivery of amino acids may limit how much muscle is used. EFFORT Protein (2023) found no benefit from pushing to 2.2 g/kg/day and possible harm in patients with AKI, so the target is moderate and reached gradually."),
  ],
  mimic=[
    ("Stress response vs simple starvation", "In starvation insulin falls, ketones rise and protein is spared; feeding reverses it. In critical illness insulin resistance and proteolysis continue whatever is fed."),
  ],
  traps=[
    ("“Feeding to 100% from day 1 stops the catabolism”", "Endogenous glucose production continues, so early full feeding overfeeds without sparing muscle."),
  ],
  decode=[
    ("Why is hypocaloric feeding advised in the first days of critical illness? [pattern]", "Endogenous glucose production (50–75% of needs) is not suppressed by feeding, so full feeding overfeeds."),
  ],
  punch="Early in critical illness the body feeds itself from its own muscle and the feed cannot stop it, so the first days are fed gently and protein is built up rather than calories pushed.",
)

L['NUT-02'] = dict(
  sub="Nutrition → Metabolism → Why the gut is fed",
  step=1,
  intro="Still in step 1: the gut is not only a route for calories but an organ that deteriorates when unused. That is the case for preferring enteral to parenteral nutrition when both are possible.",
  parts=[
    ('a', "**Without luminal nutrition: villous atrophy, enterocyte apoptosis and inflammatory infiltration.** Enterocytes take much of their fuel straight from the lumen (glutamine, short-chain fatty acids), so an empty gut thins its own lining."),
    ('b', "**Dysbiosis, loss of gut immune function (GALT) and bacterial translocation.** The gut holds a large share of the body’s lymphoid tissue; an atrophic, leaky mucosa lets bacteria and endotoxin cross, which is thought to feed sepsis and organ failure."),
    ('c', "**Early EN reduces infections.** Meta-analyses of early versus delayed EN show fewer infections, which is why ESPEN and ASPEN both recommend starting within 24–48 hours. Against parenteral nutrition the gap is smaller than once believed: CALORIES (2014) found no difference in infections when PN was not overfed (NUT-14)."),
  ],
  mimic=[
    ("Benefit of early EN vs benefit of EN over PN", "Early EN versus late EN: fewer infections. EN versus PN at similar calories: mortality and infections similar in CALORIES and NUTRIREA-2."),
  ],
  traps=[
    ("“PN causes more infections because it is PN”", "Older trials overfed with PN and hyperglycaemia; at matched, moderate doses the infection difference largely disappears."),
  ],
  decode=[
    ("Main physiological reason to prefer enteral feeding [pattern]", "Preserves the mucosal barrier and gut immunity, reducing translocation and infection."),
  ],
  punch="An unused gut atrophies and leaks, so feeding it early is treatment for the barrier as much as nutrition.",
)

L['NUT-03'] = dict(
  sub="Nutrition → Assessment → What to measure",
  step=2,
  intro="Step 2 asks who is at risk. In the ICU the usual ward tools fail because the patient is oedematous and cannot answer questions, so assessment leans on history, muscle and illness severity.",
  parts=[
    ('a', "**Gather weight and weight history, pre-admission intake, BMI, body composition, electrolytes, illness severity, comorbidities, drugs (propofol), expected stay, days in hospital before ICU, and signs of oedema, wasting or micronutrient deficiency.** Weight loss and poor intake before admission identify the malnourished and those at refeeding risk (NUT-12). Days in hospital before ICU and severity are themselves NUTRIC items (NUT-04). Propofol is listed because its lipid is a source of calories (NUT-16)."),
    ('b', "**Skinfold thickness, bioimpedance and mid-arm muscle circumference are unreliable in ICU (oedema).** Fluid in the tissues thickens skinfolds and limbs and changes the electrical resistance bioimpedance measures, so all three misread body composition after resuscitation."),
    ('c', "**CT or ultrasound muscle thickness; urea:creatinine ratio (rises with muscle catabolism).** A CT slice at L3 or ultrasound of the quadriceps measures muscle directly and is not distorted much by oedema. A rising urea with a stable creatinine reflects protein breakdown."),
    ('d', "**NUTRIC (critically ill).** NUTRIC is the ICU-specific risk score. NRS-2002 is the other score in ASPEN guidance (3 or more at risk, 5 or more high risk). ESPEN adds that any patient in ICU for more than 48 hours should be considered at risk of malnutrition."),
  ],
  mimic=[
    ("Nutritional risk vs malnutrition", "Risk scores (NUTRIC, NRS-2002) predict who benefits from feeding; malnutrition is diagnosed from weight loss, low BMI and reduced muscle (GLIM criteria)."),
  ],
  traps=[
    ("“Bioimpedance gives reliable body composition in ICU”", "Oedema makes it unreliable (NUT-17c)."),
    ("“Albumin measures nutritional status in ICU”", "Albumin falls with inflammation and dilution; it is a marker of illness, not of nutrition."),
  ],
  decode=[
    ("Which method of assessing nutritional status is reliable in an oedematous ICU patient? [pattern]", "CT or ultrasound muscle measurement, not skinfolds, bioimpedance or albumin."),
  ],
  punch="Oedema defeats skinfolds and bioimpedance, so ICU assessment rests on history, muscle imaging and a risk score built from illness severity.",
)

L['NUT-04'] = dict(
  sub="Nutrition → Assessment → The NUTRIC score",
  step=2,
  intro="Still in step 2: NUTRIC is the score that is calculated in exam stems. It was built to find the ICU patients in whom more nutrition changes mortality, so it scores how sick and how vulnerable the patient is rather than what he weighs. All three real questions are arithmetic or application of the high-risk cut-off.",
  parts=[
    ('a', "**Age under 50 / 50–74 / 75+ scores 0 / 1 / 2.** Older patients have less muscle reserve and lose it faster."),
    ('b', "**APACHE II under 15 / 15–19 / 20–27 / 28+ scores 0 / 1 / 2 / 3.** Severity of acute illness carries the most points."),
    ('c', "**SOFA under 6 / 6–9 / 10+ scores 0 / 1 / 2.** Organ failure adds to APACHE because it captures what develops after admission."),
    ('d', "**Comorbidities 0–1 / 2+ scores 0 / 1.** Chronic disease lowers reserve."),
    ('e', "**Days from hospital admission to ICU 0 / 1+ scores 0 / 1.** Days on the ward before ICU are usually days of poor intake, so they stand in for pre-existing deficit."),
    ('f', "**IL-6 under 400 / 400+ scores 0 / 1.** It marks inflammation, but it is rarely measured and adds little."),
    ('g', "**High risk: 6–10 with IL-6, or 5–9 on the modified score without IL-6; these patients have worse outcomes and benefit most from aggressive feeding. Low: 0–5 or 0–4.** The original validation showed that in high scorers more delivered calories went with lower mortality, while in low scorers it made no difference. ASPEN therefore advises that high-risk patients (NUTRIC 5 or more, or NRS-2002 5 or more) or the severely malnourished be advanced to goal as quickly as tolerated over 24–48 hours, while low-risk, well-nourished patients need no specialised nutrition for the first week."),
  ],
  table=dict(title="Worked example from the GT stem", head=["Item", "Value", "Points"], rows=[
    ["Age", "68", "1"], ["APACHE II", "25", "2"], ["SOFA", "9", "1"], ["Comorbidities", "2", "1"], ["Hospital to ICU", "2 days", "1"], ["**Total (modified)**", "", "**6: high risk**"],
  ]),
  mimic=[
    ("NUTRIC vs NRS-2002", "NUTRIC: ICU-specific, built from severity (APACHE, SOFA), no weight or intake. NRS-2002: weight loss, intake and BMI plus disease severity and age 70 or more; used on wards and by ASPEN alongside NUTRIC."),
  ],
  traps=[
    ("“5 or 7” for age 68, APACHE 25, SOFA 9, two comorbidities, two days in hospital (59–63% right)", "Common slips: APACHE 25 scores 2 (20–27 band), not 1 or 3; SOFA 9 is still in the 6–9 band (1); two days before ICU scores 1. Total 6."),
    ("“Young multitrauma” or “elderly elective lobectomy” is the patient to feed to goal fastest (26% right)", "Feed to goal in 24–48 h by NUTRIC risk: the 76-year-old with urosepsis and renal failure scores on age (2), severity, SOFA and comorbidity. A 24-year-old scores little on age; an elective lobectomy has a short, low-severity stay."),
    ("“A modified NUTRIC of 5 is low risk”", "On the modified score 5 or more is high risk; on the original with IL-6 the cut-off is 6."),
  ],
  decode=[
    ("68-year-old, septic shock, APACHE II 25, SOFA 9, two comorbidities, ICU 2 days after admission — NUTRIC? [DocT GT ×2]", "6 (high risk on the modified score). Score each band carefully."),
    ("Which patient should have EN advanced to goal within 24–48 h rather than waiting up to a week? [DocT GT]", "The one with the highest NUTRIC: 76-year-old with COPD, hypertension, urosepsis and renal failure (26%)."),
  ],
  punch="Add age, APACHE, SOFA, comorbidities and days before ICU: 5 or more without IL-6 is high risk, and those patients are fed to goal within 24–48 hours while low scorers can wait.",
)

L['NUT-05'] = dict(
  sub="Nutrition → Enteral feeding → When to start",
  step=3,
  intro="Step 3 is starting the gut. The rule is early but gentle: begin within 24–48 hours at a low rate, and hold only when the circulation cannot yet support the gut. The two real questions test the timing and the true reasons to delay.",
  parts=[
    ('a', "**Early EN within 24–48 h of ICU admission, at low dose.** ESPEN (2019, kept in 2023) and ASPEN both recommend it in a patient who cannot eat. Bowel sounds, flatus and extubation are not prerequisites; the gut absorbs before peristalsis can be heard."),
    ('b', "**Advance gradually and avoid early rapid advancement to full target (ESPEN).** Full early feeding overfeeds (NUT-01) and NUTRIREA-3 (2023) found that a deliberately low intake in the first week (about 6 kcal/kg) did as well on survival as 25 kcal/kg, with faster recovery and fewer GI complications."),
    ('c', "**On vasopressors: low-dose (trophic, 10–20 mL/h) EN if shock is controlled on small or moderate doses; withhold if shock is uncontrolled.** ESPEN delays EN when shock is uncontrolled and perfusion goals are not met, and starts low-dose EN as soon as shock is controlled with fluids and vasopressors, watching for signs of bowel ischaemia. Being on a vasopressor is therefore not itself a reason to delay. ESPEN’s other reasons to delay are uncontrolled hypoxaemia, hypercapnia or acidosis, active upper GI bleeding, overt bowel ischaemia, a high-output fistula without distal access, abdominal compartment syndrome and a gastric aspirate over 500 mL in 6 hours."),
    ('d', "**NUTRIREA-2: early full-dose EN in shock gave about 4-fold more bowel ischaemia and colonic pseudo-obstruction.** In 2,410 ventilated patients in shock, normocaloric EN versus PN gave the same 28-day mortality (37 vs 35%), but bowel ischaemia was 2% vs under 1% (19 vs 5 patients) and acute colonic pseudo-obstruction 1% vs under 1%, with more vomiting and diarrhoea. The lesson is not to avoid EN in shock but not to push it to full dose: digestion raises splanchnic oxygen demand that a hypoperfused gut cannot meet."),
  ],
  mimic=[
    ("Trophic vs full EN", "Trophic: 10–20 mL/h (EDEN about 400 kcal/day) to keep the mucosa fed. Full: the calculated target. EDEN (2012) found no difference in ventilator-free days or mortality between them for 6 days in lung injury."),
  ],
  traps=[
    ("“On vasopressors, so delay EN” (72% right)", "Vasopressors alone do not delay feeding; uncontrolled shock does. The answer was the high-output fistula that cannot be bypassed."),
    ("“Wait for bowel sounds” or “until extubated” (81% right)", "Neither is required; start within 24–48 h."),
    ("“Lactate 2 mmol/L means delay”", "A normal lactate supports starting; a rising lactate on escalating vasopressors is the warning."),
  ],
  decode=[
    ("TBI, stable, soft abdomen, briefly on vasopressors now off, 24 h after admission — when to start EN? [DocT GT]", "Within 24–48 h of ICU admission (81%)."),
    ("In which situation is EN delayed? [DocT GT]", "High-output fistula that cannot be bypassed (72%); not vasopressors as such, not a lactate of 2, not a stable patient."),
  ],
  punch="Start low-dose feed within 24–48 hours once shock is controlled, even on modest vasopressors; delay for uncontrolled shock, ischaemia, obstruction or a fistula with no distal access, and never push to full dose early in shock.",
)

L['NUT-06'] = dict(
  sub="Nutrition → Enteral feeding → Access",
  step=3,
  intro="Still in step 3: where the tube goes. The stomach is the default because it is easy and physiological; the tube moves beyond the pylorus when the stomach will not empty or when aspiration risk is high, and a permanent route is chosen when feeding will last more than a month.",
  parts=[
    ('a', "**Nasogastric: short-term default.** It is quick to place at the bedside, and the stomach tolerates bolus or continuous feed. ESPEN and ASPEN both make gastric feeding the standard first route."),
    ('b', "**Post-pyloric (nasojejunal): gastric intolerance despite prokinetics; acute pancreatitis; placed under endoscopic guidance (Freka tube 110–120 cm).** Gastroparesis in critical illness affects the stomach more than the small bowel, so jejunal feed is absorbed when gastric feed sits. ESPEN uses it when intolerance is not solved by prokinetics. ESPEN and ASPEN also accept high aspiration risk as an indication: prior aspiration, a ventilated patient who must lie flat or prone, poor gastric emptying. The tube length on the card could not be confirmed: Fresenius Kabi lists its endoscopically placed Freka nasojejunal tubes (Endolumina, EasyIn) at 270 cm, cut to length after placement, so treat 110–120 cm as an approximate working length rather than the tube itself. In pancreatitis gastric feeding is acceptable for most; jejunal feeding is used when the stomach does not tolerate it."),
    ('c', "**PEG or PEJ: feeding expected over 4 weeks.** Nasal tubes beyond a month cause sinusitis, nasal ulceration and displacement."),
    ('d', "**Surgical gastrostomy: ascites, altered anatomy, or at the time of surgery.** Ascites stops the stomach adhering to the abdominal wall and leaks around a percutaneous tube; an obstructing tumour or previous surgery may make endoscopy impossible."),
  ],
  mimic=[
    ("Post-pyloric for intolerance vs for aspiration risk", "Both are accepted indications. Intolerance: high residuals despite prokinetics (NUT-13). Aspiration risk: prior aspiration pneumonia or a ventilated patient at high risk."),
  ],
  traps=[
    ("“Ventilated COPD with prior aspiration pneumonia — continue nasogastric feeding”", "High aspiration risk is itself an indication for post-pyloric feeding (Marrow)."),
    ("“PEG when feeding is expected for over a week”", "Over 4 weeks (NUT-17f)."),
  ],
  decode=[
    ("Ventilated COPD patient with previous aspiration pneumonia — feeding route? [Marrow]", "Post-pyloric feeding."),
    ("Long-term feeding needed, tense ascites — route? [pattern]", "Surgical gastrostomy (PEG is contraindicated by ascites)."),
  ],
  punch="Stomach first; past the pylorus for intolerance that prokinetics do not fix or for high aspiration risk; a gastrostomy when feeding will last more than 4 weeks, surgical if there is ascites.",
)

L['NUT-07'] = dict(
  sub="Nutrition → Enteral feeding → Contraindications",
  step=3,
  intro="Still in step 3: when the gut cannot be used. The absolute group are situations in which feed would harm the bowel itself; the relative group mean ‘feed with care, often at a low rate’. The real question, shared with NUT-05, asks which situation delays EN.",
  parts=[
    ('a', "**Absolute: severe (uncontrolled) shock, bowel ischaemia, abdominal compartment syndrome, perforation or obstruction.** In each, feed either cannot pass or adds oxygen demand and distension to a gut that is already failing. ESPEN’s ‘delay EN’ list adds uncontrolled hypoxaemia, hypercapnia or acidosis, active upper GI bleeding, a high-output fistula without distal access and a gastric aspirate over 500 mL in 6 hours."),
    ('b', "**Relative: GI intolerance, upper GI bleeding, short bowel syndrome, spinal cord injury and abdominal trauma.** ESPEN treats active upper GI bleeding as a reason to delay until it stops, then feed. For spinal cord injury and abdominal trauma once gut continuity is confirmed, ESPEN actually recommends early EN rather than withholding it, as it does in TBI, ECMO, prone position, an open abdomen and diarrhoea. A high-output fistula with no access beyond it is the classic additional reason to delay: feed above it simply pours out."),
  ],
  mimic=[
    ("Proximal vs distal fistula", "Proximal high-output with no distal access: delay EN or feed beyond the fistula. Distal low-output: EN can usually continue."),
  ],
  traps=[
    ("“Vasopressors are a contraindication to EN”", "Only uncontrolled shock is; controlled shock gets low-dose EN (NUT-05)."),
    ("“Spinal cord injury or open abdomen means no EN”", "ESPEN recommends early EN in both."),
  ],
  decode=[
    ("In which situation is enteral nutrition delayed? [DocT GT]", "High-output fistula that cannot be bypassed (72%)."),
  ],
  punch="Withhold EN when the bowel is ischaemic, obstructed, perforated, under compartment pressure or bypassed by a high-output fistula, or when shock is uncontrolled; most other ‘contraindications’ mean feed slowly.",
)

L['NUT-08'] = dict(
  sub="Nutrition → Enteral feeding → Formulas",
  step=3,
  intro="Still in step 3: what goes down the tube. Formulas differ in how far their nutrients have been pre-digested. The one real question is about fat absorption in pancreatic insufficiency, which is why the MCT row matters most.",
  parts=[
    ('a', "**Elemental: free amino acids, glucose and oligosaccharides, MCT fat, no fibre; used in malabsorption.** Nothing needs digesting, so it suits a gut that cannot digest, at the cost of high osmolality (diarrhoea) and price."),
    ('b', "**Semi-elemental: peptides (hydrolysed), oligosaccharides, MCT, no fibre; used in poor absorption.** Peptides are absorbed by their own transporter and well tolerated in a damaged mucosa."),
    ('c', "**Polymeric: whole protein, polysaccharides, long-chain fat, fibre available; the standard formula.** ESPEN and ASPEN advise a standard polymeric formula for almost every ICU patient; peptide formulas have shown no outcome advantage."),
    ('d', "**Why MCT in malabsorption.** Medium-chain triglycerides are hydrolysed with little need for pancreatic lipase or bile, absorbed without forming micelles or chylomicrons, and go straight into portal blood. They are the fat of choice in pancreatic insufficiency, cholestasis, cirrhosis, short bowel and chylothorax. Long-chain and omega-6 rich fats all need lipase and bile. Energy-dense formulas (1.5 kcal/mL) give more calories in less volume, but TARGET (2018) found no survival benefit and more residuals and vomiting."),
  ],
  mimic=[
    ("MCT vs LCT", "MCT: portal vein, no bile or chylomicrons, no essential fatty acids. LCT: lymph via chylomicrons, needs lipase and bile, supplies essential fatty acids."),
  ],
  traps=[
    ("“Pure long-chain triglycerides” or “high total fat” for steatorrhoea despite enzymes", "Both need lipase and bile; MCT is the answer."),
    ("“Elemental formula should be routine in ICU”", "Standard polymeric is the default; elemental only for genuine malabsorption."),
  ],
  decode=[
    ("Chronic pancreatitis and cirrhosis, steatorrhoea despite enzymes — which lipid improves fat absorption? [DocT GT]", "Medium-chain triglycerides."),
  ],
  punch="Standard polymeric feed for nearly everyone; the less the gut can digest, the more pre-digested the formula, and MCT is the fat that needs no lipase, bile or lymph.",
)

L['NUT-09'] = dict(
  sub="Nutrition → How much → Measuring energy needs",
  step=4,
  intro="Step 4 is how much to give, and it starts with how much the patient burns. This is the most-asked card in the deck: two questions on the target in kcal/kg, two on what indirect calorimetry measures and when it fails, and one on a quick equation. The reasoning that links them is simple: measure if you can, estimate if you must, and know what the estimate is based on.",
  parts=[
    ('a', "**Indirect calorimetry is the gold standard: it measures VO₂ and VCO₂ (Weir equation, RQ).** The analyser samples inspired and expired gas over a short steady-state period at rest (AARC accepts 5 minutes if the gas readings vary by 5% or less, longer if not) and converts oxygen consumption and carbon dioxide production into energy expenditure with the Weir equation, then extrapolates to 24 hours. ESPEN (2019, 2023) recommends it whenever available, because equations are wrong by 20% or more in a large share of ICU patients. The respiratory quotient (VCO₂/VO₂) is about 1.0 for carbohydrate, 0.7 for fat and 0.8 for protein; above 1 means lipogenesis from overfeeding. Physiological values lie between about 0.67 and 1.3, so a result outside that range means the measurement is wrong, not the patient. It becomes unreliable at FiO₂ above 0.6, because the analyser cannot resolve the small inspired–expired oxygen difference, and with air leaks (bronchopleural fistula, chest drain, cuff leak), during RRT or ECMO (which remove CO₂ outside the lungs), and when the patient is not in steady state. A pulmonary artery catheter gives VO₂ by the Fick method, but that is not indirect calorimetry and underestimates it."),
    ('b', "**Harris-Benedict: men 66 + 13.7W + 5H − 6.8A; women 655 + 9.6W + 1.8H − 4.7A (W kg, H cm, A years).** It predicts resting expenditure in health and needs a stress factor in illness. Age is subtracted because metabolic rate falls with age. A quicker version in Harrison is men 900 + 10W and women 700 + 7W, so a 50 kg man has about 1,400 kcal/day. In the ICU, guidelines more often use a simple weight-based estimate: ASPEN 2016 25–30 kcal/kg/day; ASPEN 2022 12–25 kcal/kg/day in the first 7–10 days; ESPEN, when nothing can be measured, a simple 20–25 kcal/kg/day, given at no more than 70% of it early."),
    ('c', "**Stress factors: pneumonia with ARDS 1.2–1.3; minor surgery 1.1–1.3; major surgery 1.2–1.4; multiple trauma 1.4–1.6; trauma with closed head injury 1.5–1.7.** The resting value is multiplied by these to estimate illness-related expenditure. They are rough, which is one more reason to measure."),
    ('d', "**Obesity: use ideal body weight.** Fat burns little energy, so actual weight overestimates needs. ASPEN gives 11–14 kcal/kg of actual weight per day for BMI 30–50 and 22–25 kcal/kg of ideal weight for BMI over 50, with protein 2.0 g/kg of ideal weight (up to 2.5 when BMI is 40 or more). ESPEN uses an adjusted body weight (its 2023 commentary: ideal weight plus 20–25% of the excess) for energy and for protein (1.3 g/kg/day)."),
  ],
  table=dict(title="Estimating energy at the bedside", head=["Method", "What it gives", "Limits"], rows=[
    ["Indirect calorimetry", "measured REE", "FiO₂ >0.6, air leak, RRT/ECMO, not at steady state"],
    ["25–30 kcal/kg (ASPEN 2016)", "the goal in DocT stems", "overfeeds early in the stress phase"],
    ["12–25 kcal/kg (ASPEN 2022) / ≤70% early (ESPEN)", "first-week dose", "—"],
    ["Harris-Benedict × stress factor", "REE × illness", "error 20% or more in ICU"],
  ]),
  mimic=[
    ("Indirect calorimetry vs Fick VO₂ from a PA catheter", "Calorimetry measures gas exchange at the mouth or tube; Fick calculates VO₂ from cardiac output and the arteriovenous oxygen difference and misses lung oxygen consumption."),
    ("Indirect vs direct calorimetry", "Direct calorimetry measures heat released in a sealed chamber; it is a research tool."),
  ],
  traps=[
    ("“1,800 kcal/day” or “1,500” for an 80-kg ventilated trauma patient (32% right)", "The key uses 25–30 kcal/kg (2,000–2,400), so 2,100 is the only option in range. Under ESPEN’s early hypocaloric approach or ASPEN 2022’s 12–25 kcal/kg, 1,800 or 1,500 would be a reasonable first-week dose, so read whether the stem asks for the goal or the early dose."),
    ("“Measures O₂ consumption and CO₂ production over 24 hours” (44% right)", "It measures at rest over a short steady-state period and extrapolates."),
    ("“FiO₂ 0.40” or “measurement duration” explains an RQ of 1.55", "FiO₂ 0.90 does: above 0.6 the analyser error explodes; any RQ above about 1.3 is an artefact."),
  ],
  decode=[
    ("39-year-old 80-kg intubated trauma patient — daily calorie goal for tube feeding? [DocT GT]", "2,100 kcal/day (25–30 kcal/kg), 32%."),
    ("Indirect calorimetry determines energy expenditure by measuring? [DocT GT]", "O₂ consumption and CO₂ production at rest (44%)."),
    ("Ventilated, indirect calorimetry RQ 1.55 — which factor explains the unreliable result? [DocT GT]", "FiO₂ 0.90."),
    ("Resting energy expenditure of a 50-kg man? [Marrow]", "1,400 kcal (900 + 10 × 50)."),
  ],
  punch="Indirect calorimetry measures resting VO₂ and VCO₂ and fails at high FiO₂, leaks and extracorporeal circuits; when it is unavailable the goal is 25–30 kcal/kg, with less in the first days.",
)

L['NUT-10'] = dict(
  sub="Nutrition → How much → Energy and protein over time",
  step=4,
  intro="Still in step 4: the targets change as the patient moves from the acute catabolic phase to recovery. The card’s schedule is the hypocaloric-then-build approach that the large trials of the last decade support.",
  parts=[
    ('a', "**Early (first days): 20 kcal/kg/day, hypocaloric; protein starts at 0.8 g/kg/day.** ESPEN gives no more than 70% of expenditure early. Trials comparing less with more in the first week (EDEN, PermiT, TARGET, NUTRIREA-3) showed no mortality difference; where GI tolerance was reported the lower arms did better (fewer GI events with trophic feeding in EDEN and with low intake in NUTRIREA-3, more vomiting and larger residuals with the energy-dense feed in TARGET)."),
    ('b', "**End of week 1: 25 kcal/kg/day; protein ramps to over 1.2–1.3 g/kg/day.** ESPEN increases to 80–100% of measured expenditure after day 3 and gives 1.3 g/kg/day protein progressively; ASPEN gives 1.2–2.0 g/kg/day. EFFORT Protein (2023) found that prescribing 2.2 g/kg/day or more did not improve outcomes, with signals of harm in patients with AKI or higher SOFA scores (exploratory subgroups)."),
    ('c', "**Recovery (anabolic): 30 kcal/kg/day with high-protein formulas (protein without excess non-protein calories).** Only now can the body build muscle, so energy and protein rise and rehabilitation begins."),
  ],
  mimic=[
    ("Permissive underfeeding vs trophic feeding", "PermiT: 40–60% of calories with full protein. EDEN: trophic about 400 kcal/day with little protein. Neither changed mortality."),
  ],
  traps=[
    ("“More protein is always better”", "EFFORT Protein found no benefit from high doses and possible harm in AKI; monitor urea and renal function when pushing protein."),
  ],
  decode=[
    ("Energy and protein target in the first days of critical illness [pattern]", "Hypocaloric (about 20 kcal/kg or ≤70% of measured expenditure), protein built progressively towards 1.3 g/kg/day."),
  ],
  punch="Low calories and modest protein early, 25 kcal/kg and about 1.3 g/kg by the end of the first week, and more of both only when the patient turns anabolic.",
)

L['NUT-11'] = dict(
  sub="Nutrition → How much → Micronutrients and immunonutrition",
  step=4,
  intro="Still in step 4: the small components. Basic replacement is routine; pharmacological doses meant to modify the illness have mostly failed, and one of them harmed. The single real question is about a low zinc level, which tests how plasma levels behave in inflammation.",
  parts=[
    ('a', "**Trace elements and vitamins support metabolism, immunity, antioxidant defence and wound healing.** Requirements rise with losses (burns, drains, fistulae, CRRT), while plasma levels of zinc, selenium, iron and vitamin C fall in inflammation because they move into tissues, not because stores are empty. A low level with a high CRP is therefore hard to interpret."),
    ('b', "**Early IV multi-trace elements and multivitamins alongside EN, plus thiamine 100–300 mg.** Daily maintenance doses are given with PN and when EN covers too little. Thiamine (100–300 mg a day for the first days) is given to those at risk of refeeding or alcohol-related deficiency (NUT-12)."),
    ('c', "**Not routinely recommended: glutamine, arginine, taurine, omega-3, γ-linolenic acid, carnitine; pharmacological vitamin C, E, β-carotene, selenium and zinc.** REDOXS (2013) found that high-dose glutamine increased mortality in multi-organ failure. ESPEN still allows enteral glutamine in burns over 20% of body surface and in trauma, and says it should not be given to other ICU patients."),
  ],
  mimic=[
    ("Deficiency vs redistribution", "Deficiency: losses or poor intake, clinical signs (rash, poor wound healing, diarrhoea for zinc). Redistribution: low plasma level with raised CRP and no signs."),
  ],
  traps=[
    ("“Plasma zinc is low, so give pharmacological zinc”", "Marrow keys ‘monitor zinc, no treatment yet’: low plasma zinc in acute illness is mostly redistribution. Replace when deficiency is clinically likely or losses are high. The Marrow explanation contradicts its key, and 0.2 µg/mL is very low, so the key is debatable."),
    ("“Routine glutamine improves outcome”", "Not recommended; harmful in REDOXS (NUT-17h)."),
  ],
  decode=[
    ("Severe TBI on tube feeds, day 7 zinc 0.2 µg/mL — management? [Marrow]", "Monitor zinc; no treatment yet (keyed). Supplement if signs of deficiency or high losses."),
  ],
  punch="Give maintenance trace elements, vitamins and thiamine; a low plasma level in inflammation is often redistribution, and pharmacological ‘immunonutrition’, glutamine above all, is not routine.",
)

L['NUT-12'] = dict(
  sub="Nutrition → How much → Refeeding syndrome",
  step=5,
  intro="Step 5 is when feeding itself harms, and refeeding is the classic case. A starved patient has adapted to burning fat; when carbohydrate arrives, insulin rises and pulls electrolytes into cells faster than the depleted body can supply them. Both real questions ask how to manage it: one a low phosphate, the other a malnourished patient about to be fed.",
  parts=[
    ('a', "**Feeding after severe malnutrition: insulin drives phosphate, potassium and magnesium into cells.** Total body stores are low but plasma levels can be normal before feeding. Insulin moves these ions into cells and phosphate is consumed to make ATP and 2,3-DPG for glycolysis, so plasma levels fall within 2–3 days."),
    ('b', "**Labs: low phosphate, potassium and magnesium; thiamine deficiency.** Phosphate is the defining one. In the ICU refeeding trial (Doig 2015) refeeding hypophosphataemia was defined as a fall below 0.65 mmol/L (2.0 mg/dL), by more than 0.16 mmol/L, within 72 hours of starting feed. To convert, mg/dL × 0.323 gives mmol/L, so 1.8 mg/dL is about 0.58 mmol/L."),
    ('c', "**Effects: arrhythmia, cardiomyopathy, hypotension, respiratory and muscle weakness, kidney dysfunction, confusion, seizures, Wernicke’s.** Without phosphate, muscle (including the diaphragm and heart) cannot make ATP, so weaning fails and the heart fails; low potassium and magnesium add arrhythmias; salt and water retention with carbohydrate refeeding adds fluid overload."),
    ('d', "**Risk: eating disorders, chronic illness with malnutrition, alcohol, prolonged starvation.** NICE CG32 gives high risk as one of: BMI under 16, unintentional weight loss over 15% in 3–6 months, little or no intake for over 10 days, or low potassium, phosphate or magnesium before feeding; or two of: BMI under 18.5, weight loss over 10%, little intake for over 5 days, alcohol misuse or drugs such as insulin, chemotherapy, antacids or diuretics."),
    ('e', "**Prevention: thiamine first; restrict fluid and calories (500 kcal/day or 25% of target); advance in four 25% steps; replace and monitor electrolytes.** The schedules differ by source. NICE starts at no more than 10 kcal/kg/day (5 kcal/kg/day in extreme cases such as BMI under 14) and reaches full needs over 4–7 days, with thiamine 200–300 mg daily. ESPEN: when refeeding hypophosphataemia appears in ICU, restrict energy for 48 hours and then increase gradually, with electrolytes checked 2–3 times a day; in the Doig trial (339 patients) this restriction, starting at about 480 kcal/day for 2 days, did not change the primary outcome (days alive after ICU discharge) but 60-day mortality, a secondary outcome, was lower. Thiamine goes in before carbohydrate in a planned feed, because glucose metabolism uses it up. Treat low phosphate by severity: IV replacement for severe levels (under about 0.3 mmol/L, 1 mg/dL), for symptoms, or when the oral or enteral route is unreliable, which in ventilated, tube-fed ICU patients often makes IV the choice for moderate levels (0.3–0.6 mmol/L) too."),
  ],
  mimic=[
    ("Refeeding hypophosphataemia vs ICU hypophosphataemia from other causes", "Refeeding: within 72 h of starting or increasing feed in a malnourished patient. Others: diuretics, RRT, DKA treatment, respiratory alkalosis, sepsis."),
  ],
  traps=[
    ("“Oral phosphate for 1.8 mg/dL in a tube-fed MOF patient”", "Marrow keys IV potassium phosphate. Ward tables reserve IV for under 1.0 mg/dL or symptoms, but in critical illness enteral absorption is unreliable and the patient is often ventilated, so IV is the ICU answer; the qpack notes the conflict."),
    ("“Malnourished BMI 16 with ARDS — start full feeding to reverse the deficit”", "BMI under 16 is high refeeding risk: low-rate EN (about 10 kcal/kg), advanced slowly, with thiamine and electrolytes (Marrow)."),
    ("“Start glucose before thiamine” in a planned refeed", "Thiamine first (NUT-17e). In hypoglycaemic coma glucose is never delayed (TOX-01)."),
  ],
  decode=[
    ("MOF on tube feeds, day 5 phosphate 1.8 mg/dL — best management? [Marrow]", "IV potassium phosphate (keyed); oral absorption is poor in critical illness."),
    ("Severe ARDS, malnourished (BMI 16), volume overloaded — feeding strategy? [Marrow]", "Low-rate EN, advance slowly."),
  ],
  punch="In a starved patient insulin from the first feed drives phosphate into cells; give thiamine first, start low (about 10 kcal/kg), build over days, check phosphate, potassium and magnesium often, and give phosphate IV in the ICU.",
  extra=[
    dict(q="NICE CG32 high refeeding risk — one criterion?", a="BMI <16, weight loss >15% in 3–6 months, little or no intake >10 days, or low K/PO₄/Mg before feeding. Two criteria: BMI <18.5, loss >10%, little intake >5 days, alcohol or insulin, chemotherapy, antacids, diuretics."),
  ],
)

L['NUT-13'] = dict(
  sub="Nutrition → Problems → Feeding intolerance",
  step=5,
  intro="Still in step 5: feed that the gut will not take. The approach depends on where the problem sits: the stomach that will not empty, the small bowel that distends, or the colon that empties too much. Both real questions are about what to do next, one with high residuals and one with diarrhoea.",
  parts=[
    ('a', "**Gastric (vomiting, large GRV, distension): stop or slow EN, then prokinetics, then post-pyloric feeding if there is no bowel distension. Small bowel (distension, no stool, rising IAP): stop EN or keep a low rate, measure IAP, laxatives and prokinetics. Lower GI: diarrhoea — keep EN (low rate if severe), stop laxatives, find the trigger (C. difficile); consider Ogilvie’s and ischaemia. GRV over 500 mL in 6 h is intolerance; routine GRV checks are no longer recommended.** For the stomach, ESPEN makes IV erythromycin the first-line prokinetic (metoclopramide is the alternative, or both together) for 24–48 hours, stopping prokinetics after 3 days because they lose effect, and moves to post-pyloric feeding when prokinetics do not solve it; a severe ARDS patient, ventilated and often prone, at high aspiration risk can go straight to a post-pyloric tube (NUT-06). In the small bowel, rising intra-abdominal pressure with distension is the route to abdominal compartment syndrome, which is a reason to stop EN (NUT-07). Diarrhoea in ICU is usually from drugs (laxatives, sorbitol-containing syrups, antibiotics) or infection, rarely the feed alone; stopping EN does not cure it and leaves the patient unfed, so ESPEN recommends early EN even with diarrhoea. On residuals, ESPEN delays EN when the gastric aspirate exceeds 500 mL in 6 hours and adds a prokinetic; ASPEN advises against routine GRV monitoring and, where it is still used, not to hold feed for a GRV under 500 mL, because residuals correlate poorly with aspiration and checking them mostly stops feeding."),
  ],
  table=dict(title="Where the intolerance sits", head=["Level", "Signs", "Action"], rows=[
    ["Stomach", "vomiting, GRV >500 mL/6 h", "slow EN → erythromycin ± metoclopramide → **post-pyloric**"],
    ["Small bowel", "distension, no stool, rising IAP", "stop or low-rate EN, measure IAP, laxatives + prokinetics"],
    ["Colon", "diarrhoea", "**keep EN at low rate**, stop laxatives, test C. difficile; think Ogilvie’s, ischaemia"],
  ]),
  mimic=[
    ("High GRV vs bowel obstruction or ischaemia", "High GRV alone with a soft abdomen: prokinetic or post-pyloric. Distension, pain, rising lactate or IAP: stop feed and look for ischaemia; never push post-pyloric into an ischaemic gut."),
  ],
  traps=[
    ("“Septic patient with large watery stools — stop the feed”", "Reduce the rate (Marrow keys 20 mL/h), stop laxatives and send C. difficile; keep feeding."),
    ("“Hold feed for any GRV over 250 mL”", "The threshold is 500 mL (in 6 h for ESPEN), and routine checks are discouraged."),
    ("“Prokinetics before post-pyloric” vs the Marrow key", "The card ladder uses prokinetics first; Marrow keys post-pyloric for severe ARDS with high residuals at 12 h. If prokinetics are offered and aspiration risk is not stressed, prokinetics; if the stem stresses ventilated, severe ARDS or failed prokinetics, post-pyloric."),
  ],
  decode=[
    ("Severe ARDS on trickle feeds, high gastric residuals at 12 h — next step? [Marrow]", "Post-pyloric feeding tube (keyed)."),
    ("Septic patient on tube feeds, large watery stools every 2 h — next step? [Marrow]", "Reduce feed rate to 20 mL/h (and test for C. difficile)."),
  ],
  punch="Slow the feed, add erythromycin, then go past the pylorus for a stomach that will not empty; for diarrhoea keep feeding at a low rate and find the drug or bug; 500 mL is the only residual that matters.",
)

L['NUT-14'] = dict(
  sub="Nutrition → Problems and PN → Enteral vs parenteral",
  step=6,
  intro="Step 6 is the vein. Older teaching that PN is dangerous came from trials that overfed it with glucose; at matched, moderate doses CALORIES and NUTRIREA-2 found the same mortality with either route. The differences that remain are cost, the gut barrier, the central line and metabolic complications, and the three real questions are all about the last two.",
  parts=[
    ('a', "**Cost: enteral lower, parenteral higher.** PN needs sterile compounding, a line and more monitoring."),
    ('b', "**Physiology: enteral is physiological and preserves the gut barrier; parenteral bypasses the gut.** NUT-02 gives the reason."),
    ('c', "**Infection: enteral lower; parenteral has CLABSI.** The line is the main infection risk. CALORIES (2014, 2,388 patients) found no difference in infections or 30-day mortality (33.1 vs 34.2%) when PN was dosed modestly, with less hypoglycaemia and vomiting on PN. A sudden new hyperglycaemia in a patient on unchanged PN often heralds catheter-related sepsis: infection causes insulin resistance before fever appears."),
    ('d', "**Access: enteral needs no central line; parenteral needs a central line, PICC or midline.** Standard PN is hyperosmolar, far above the roughly 850–900 mOsm/L a peripheral vein tolerates, so it needs a central vein; only dilute peripheral PN can use a peripheral vein."),
    ('e', "**Specific risks: enteral aspiration and bowel ischaemia; parenteral hyperglycaemia, steatosis (lipid over 50%) and hypertriglyceridaemia.** Hyperglycaemia is the commonest metabolic complication of PN, so it is the answer when offered. Refeeding hypophosphataemia, hypokalaemia and hypomagnesaemia are next. Hepatic steatosis comes mainly from excess calories, especially glucose beyond about 5 mg/kg/min, which is turned into fat; high soybean lipid doses add cholestasis. Other PN complications are cholestasis and gallbladder sludge (no enteral stimulus to empty it). Stopping PN abruptly can cause rebound hypoglycaemia, because insulin secreted in response to the glucose load outlasts it; taper the infusion or run 10% dextrose and check glucose."),
    ('f', "**PN advantage: avoids aspiration and bowel ischaemia.** In NUTRIREA-2 the PN arm had less vomiting, bowel ischaemia and colonic pseudo-obstruction than full-dose EN in shock."),
  ],
  mimic=[
    ("Rebound hypoglycaemia vs other causes of sudden obtundation after stopping PN", "Check glucose first: high circulating insulin with no incoming glucose makes it the immediate cause, treated with IV glucose."),
  ],
  traps=[
    ("“Hyponatraemia is the lab abnormality associated with TPN”", "Marrow keys it, but the key is doubtful: hyperglycaemia is the commonest metabolic complication of TPN, then refeeding hypophosphataemia and hypokalaemia. If hyperglycaemia is offered, choose it."),
    ("“Trauma patient on TPN, line pulled, obtunded 4 h later — CT head first”", "Give IV glucose: rebound hypoglycaemia after an abrupt stop (Marrow)."),
    ("“Stable PN, glucose suddenly rises — the PN is too concentrated”", "Nothing changed in the bag; new hyperglycaemia points to infection, usually the line (Marrow)."),
  ],
  decode=[
    ("Post-laparotomy TPN through a central line — associated lab abnormality? [Marrow]", "Keyed hyponatraemia; hyperglycaemia is the better answer when offered."),
    ("Trauma, on TPN, line removed for an infected site, obtunded 4 h later — next step? [Marrow]", "IV glucose (rebound hypoglycaemia)."),
    ("Gunshot wound, ventilated on unchanged TPN, day 6 glucose rises sharply — cause? [Marrow]", "Infection (catheter sepsis)."),
  ],
  punch="Dosed sensibly, PN is as safe as EN for survival; its problems are the line and glucose, so new hyperglycaemia on steady PN means sepsis and an abrupt stop means rebound hypoglycaemia.",
)

L['NUT-15'] = dict(
  sub="Nutrition → Problems and PN → When to start PN",
  step=6,
  intro="Still in step 6: when PN is added. The trials say that hurrying it in a well-nourished patient does harm, while waiting too long in a starved patient with a useless gut also harms. The single real question names EPaNIC, so the answer follows that trial.",
  parts=[
    ('a', "**Supplemental PN when EN covers under 60% of target despite efforts.** The 60% figure is ASPEN 2016’s threshold (consider SPN if EN cannot meet more than 60% of energy and protein needs after 7–10 days) and the trigger in the Heidegger SPN trial (EN under 60% by day 3, SPN from day 4). ESPEN says PN should not be started until every reasonable strategy to improve EN tolerance has been tried, and weighs supplemental PN case by case, suggesting days 4–7."),
    ('b', "**Timing: low risk after about day 7 (ASPEN); high risk or EN contraindicated, early (ESPEN, within 3–7 days).** ASPEN 2022 recommends not starting SPN before day 7 of ICU admission, except in the malnourished or those with little lean mass, where clinical judgement applies. EPaNIC (2011, 4,640 patients) found that late PN from day 8 led to fewer new infections (22.8 vs 26.2%), more patients discharged alive from ICU by day 8 and lower cost than early PN, with no mortality difference. When EN is impossible, ESPEN starts PN within 3–7 days, and ASPEN starts it as soon as possible in the severely malnourished or high-risk patient."),
    ('c', "**Absolute contraindications: adequate oral intake, or EN meeting targets.** PN then adds only line risk."),
    ('d', "**Relative contraindications: no central access, substrate intolerance (renal, cardiac or hepatic failure), terminal illness.** Fluid volume, glucose and lipid loads can be hard to give in these patients, and in terminal illness PN rarely changes the outcome."),
    ('e', "**Separate infusions or all-in-one bags.** All-in-one (three-chamber) bags have fewer line manipulations and lower contamination risk; separate infusions allow flexible lipid and glucose doses."),
  ],
  mimic=[
    ("Supplemental PN vs total PN", "Supplemental: adds to inadequate EN. Total: the only source, when the gut cannot be used."),
  ],
  traps=[
    ("“Start TPN immediately on day 3 to avoid caloric debt” (EPaNIC stem)", "In a well-nourished patient (BMI 26) in shock, delay PN until day 8 and keep trying trophic EN."),
    ("“Start supplemental PN to 100% of target by day 4”", "Full early feeding overfeeds in the acute phase (NUT-01); EPaNIC and ASPEN 2022 favour waiting."),
    ("“Post-pyloric tube with protein over 2 g/kg/day”", "Post-pyloric is reasonable, but over 2 g/kg/day was not beneficial in EFFORT Protein; the option is wrong on dose."),
  ],
  decode=[
    ("Faecal peritonitis, septic shock on noradrenaline 0.2 µg/kg/min, BMI 26, failed EN on day 3 — by EPaNIC, next step? [DocT GT]", "Delay PN until day 8 while continuing trophic EN."),
  ],
  punch="In a well-nourished patient, PN waits until about day 8 (EPaNIC, ASPEN 2022) while trophic EN continues; the malnourished patient with no usable gut gets it early.",
)

L['NUT-16'] = dict(
  sub="Nutrition → Problems → Overfeeding",
  step=5,
  intro="Back to step 5: harm from too much. Overfeeding is easy in the ICU because calories come from sources nobody counts and because the stressed body is already making glucose. The one real question asks for a sensible dextrose–lipid prescription, which is really a test of the limits.",
  parts=[
    ('a', "**Harms: hyperglycaemia, raised CO₂ production (harder weaning), liver steatosis.** Carbohydrate beyond what can be oxidised is turned into fat (lipogenesis), which produces extra CO₂ (RQ over 1) and loads the lungs of a patient being weaned; the fat is stored in the liver. ESPEN keeps glucose (PN) or carbohydrate (EN) at or below 5 mg/kg/min and IV lipid, counting non-nutritional sources such as propofol, at or below 1.5 g/kg/day; in practice lipid is commonly about 20–30% of calories."),
    ('b', "**Hidden calories: propofol (1.1 kcal/mL in lipid), dextrose infusions, citrate.** Propofol 1% is in a 10% lipid emulsion: 20 mL/h gives about 530 kcal/day, so the PN lipid should be cut. 5% dextrose gives 50 g (170 kcal) per litre. Citrate used for anticoagulation of CRRT is metabolised and adds calories."),
    ('c', "**Obesity: feed by ideal body weight, hypocaloric and high-protein.** ASPEN gives obese patients fewer calories and more protein per kg of ideal weight (NUT-09d), so that fat is used while muscle is protected."),
  ],
  mimic=[
    ("Overfeeding vs refeeding", "Overfeeding: too much for any patient, hyperglycaemia, CO₂ and steatosis. Refeeding: even modest feed in a starved patient, electrolyte crash."),
  ],
  traps=[
    ("“The Marrow PN regimen is fine because it is keyed” (12.5% dextrose 100 mL/h + 20% lipid 50 mL/h)", "Over 24 h that is 300 g dextrose (about 3 mg/kg/min in 70 kg, acceptable) but 1,200 mL of 20% lipid, about 2,400 kcal and 240 g fat (over 3 g/kg/day), far above the limits. The key only fits if the lipid runs for part of the day; the Marrow explanation’s arithmetic is wrong."),
    ("“Propofol only sedates”", "It is a lipid source and must be counted."),
  ],
  decode=[
    ("Post bowel resection, starting TPN — most appropriate dextrose and lipid composition? [Marrow]", "Keyed 12.5% dextrose 100 mL/h + 20% lipid 50 mL/h; check against glucose ≤5 mg/kg/min and lipid 20–30% of calories."),
    ("Failed weaning, high PaCO₂, on full PN with propofol [pattern]", "Overfeeding raises CO₂ production; count the propofol and reduce carbohydrate."),
  ],
  punch="Count every calorie, including propofol, dextrose and citrate; keep glucose under 5 mg/kg/min and lipid modest, because excess becomes fat in the liver and CO₂ in the lungs.",
  extra=[
    dict(q="PN arithmetic for 70 kg — 12.5% dextrose at 100 mL/h?", a="2,400 mL × 0.125 = 300 g/day ≈ 1,020 kcal; 300,000 mg ÷ 70 ÷ 1,440 ≈ 3 mg/kg/min (limit 5). 20% lipid ≈ 2 kcal/mL."),
  ],
)

L['NUT-17'] = dict(
  sub="Nutrition → Sweep → True or false",
  step=6,
  intro="The last card runs back through the whole story, one statement per step. Each false statement is a distractor from an earlier card.",
  parts=[
    ('a', "**True: early EN is started within 24–48 h.** ESPEN within 48 h, ASPEN within 24–48 h (NUT-05)."),
    ('b', "**False: full-dose EN is not safe on high-dose vasopressors; low-dose only, and only if shock is controlled.** NUTRIREA-2 showed more bowel ischaemia with full-dose EN in shock."),
    ('c', "**False: bioimpedance is unreliable in ICU (oedema).** NUT-03."),
    ('d', "**True: a modified NUTRIC of 6 is high risk.** The modified cut-off is 5 or more (NUT-04)."),
    ('e', "**False: in refeeding, thiamine comes first.** Carbohydrate uses up thiamine and can precipitate Wernicke’s (NUT-12)."),
    ('f', "**False: PEG is for feeding expected over 4 weeks, not 1 week.** NUT-06."),
    ('g', "**True: supplemental PN is considered when EN gives under 60% of target.** NUT-15; timing after about day 7 in the well-nourished."),
    ('h', "**False: routine glutamine is not recommended.** REDOXS showed harm; ESPEN keeps enteral glutamine only for burns and trauma (NUT-11)."),
  ],
  mimic=[
    ("Modified vs original NUTRIC cut-off", "Modified (no IL-6): 5 or more. Original (with IL-6): 6 or more."),
  ],
  traps=[
    ("“PEG after 1 week”", "4 weeks."),
    ("“Thiamine after the first feed”", "Before."),
  ],
  decode=[
    ("Which statement about ICU nutrition is true? [pattern]", "Early low-dose EN within 24–48 h; mNUTRIC ≥5 high risk; SPN when EN <60% of target."),
  ],
  punch="Three statements are true: early EN in 24–48 hours, a modified NUTRIC of 6 is high risk, and supplemental PN is considered below 60% of target; the rest are distractors from earlier cards.",
)

FLAGS = {
  'NUT-01': "e: ‘0.8 g/kg/day, building to over 1.2’ fits ESPEN’s progressive 1.3 g/kg/day; EFFORT Protein (2023) found no benefit from ≥2.2 g/kg/day and harm signals in AKI and high SOFA. ‘10–15% / 50% rise in expenditure’ are teaching approximations.",
  'NUT-05': "Card agrees with ESPEN 2019/2023 and NUTRIREA-2 (bowel ischaemia HR 3.84, 19 vs 5; pseudo-obstruction HR 3.7). Card does not list ESPEN’s other reasons to delay (uncontrolled hypoxaemia/hypercapnia/acidosis, active upper GI bleed, high-output fistula without distal access, GRV >500 mL/6 h); the fistula is in NUT-07’s watch line and was asked.",
  'NUT-06': "Card omits high aspiration risk as an indication for post-pyloric feeding (ESPEN 2023 R13, ASPEN 2016; asked by Marrow); added. ‘Acute pancreatitis’ as a post-pyloric indication is dated: gastric feeding is acceptable in most, jejunal if gastric intolerance. ‘Freka tube 110–120 cm’ could not be verified: Fresenius Kabi lists the endoscopic Freka nasojejunal tubes (Endolumina, EasyIn) at 270 cm, cut after placement; 110–120 cm may be an insertion depth.",
  'NUT-07': "Relative list conflicts with ESPEN 2019/2023, which recommends early EN (not withholding) in spinal cord injury, abdominal trauma with confirmed GI continuity, TBI, prone position, open abdomen and diarrhoea, and delays EN in active upper GI bleeding until it stops. Explanation says so.",
  'NUT-09': "d: ‘Obesity: use ideal body weight’ is ASPEN-style (and ASPEN uses actual weight, 11–14 kcal/kg, for BMI 30–50); ESPEN uses adjusted body weight (IBW + 20–25% of excess). The linked DocT GT key (2,100 kcal = 25–30 kcal/kg) follows ASPEN 2016; ASPEN 2022 (12–25 kcal/kg in the first 7–10 days) and ESPEN (≤70% early) would make a lower first-week dose correct, so the key depends on reading ‘goal’. Indirect calorimetry limits (FiO₂ >0.6, leaks, RRT/ECMO, RQ 0.67–1.3) and Harrison’s quick REE are not on the card; added.",
  'NUT-11': "Linked Marrow key (zinc 0.2 µg/mL → monitor only) is debatable: the level is very low and Marrow’s explanation contradicts its key. ESPEN 2023 still allows enteral glutamine in burns >20% TBSA and trauma (card says ‘not routinely recommended’, which is right for unselected patients).",
  'NUT-12': "e: ‘500 kcal/day or 25% of target, four 25% steps’ is one local schedule; NICE CG32 starts at ≤10 kcal/kg/day (5 in extreme cases) reaching full needs in 4–7 days, with thiamine 200–300 mg daily; ESPEN restricts energy for 48 h after refeeding hypophosphataemia (Doig 2015: primary outcome neutral, 60-day mortality lower as a secondary outcome). Linked Marrow key (IV phosphate for 1.8 mg/dL) conflicts with ward oral-first tables (qpack note); IV is defensible in ventilated ICU patients.",
  'NUT-13': "Card ladder (prokinetics before post-pyloric) agrees with ESPEN (erythromycin first-line); the linked Marrow key goes straight to post-pyloric for severe ARDS. ‘GRV >500 mL in 6 h’ is ESPEN; ASPEN discourages routine GRV and says not to hold feed below 500 mL.",
  'NUT-14': "‘Steatosis (lipid over 50%)’ is unclear: PN steatosis is driven mainly by excess calories, especially glucose; high soybean lipid doses cause cholestasis. Card omits rebound hypoglycaemia on abrupt stop and new hyperglycaemia as a sign of catheter sepsis (both asked by Marrow); added. Linked Marrow key (hyponatraemia as the TPN lab abnormality) is doubtful: hyperglycaemia is commonest.",
  'NUT-15': "‘Supplemental PN when EN <60%’ is the ASPEN 2016/Heidegger trigger; ESPEN 2019/2023 weighs SPN case by case (days 4–7) and ASPEN 2022 recommends not starting SPN before day 7. Card’s timing line matches. EPaNIC figures added from the trial.",
  'NUT-16': "Linked Marrow key (12.5% dextrose 100 mL/h + 20% lipid 50 mL/h) gives about 2,400 kcal and 240 g of lipid per day if the lipid runs 24 h, above ESPEN (≤1.5 g/kg/day) and ASPEN limits; the explanation’s arithmetic in the bank is wrong (as the qpack note says). Glucose/lipid limits are not on the card; added.",
}
