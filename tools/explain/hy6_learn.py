# HY6 — Explain v3 ("Learn" depth): high yield GI — feeding the critically ill, refeeding and nutritional markers, stress ulcer prophylaxis and mobilisation, intra-abdominal
# hypertension and abdominal compartment syndrome, acute pancreatitis (diagnosis, imaging, management), the acute abdomen in the ICU, upper GI bleeding, variceal haemorrhage,
# lower GI bleeding, acute liver failure (definition, King’s, ICU care), decompensated cirrhosis (SBP, HRS-AKI, paracentesis), true/false sweep. No mnemonics or hooks.
# Driven by qpack/HY6.md (54 question links; GIN-08 upper GI bleeding asked 12 times, GIN-09 variceal bundle 7, GIN-10 lower GI bleeding 7, GIN-04 IAH/ACS 6, GIN-01 and GIN-02 four each).
# GIN-14 has no linked question and gets a short explanation with [pattern] decode items.
# Card layer (gi_cardlayer.json "HY6|<code>") lines read and agreed with; no `fix` entries for HY6 in trace/test/data/qbank.json (checked 20 Nov 2026).
# Checked online on 20 Nov 2026:
#  - ESPEN practical and partially revised ICU guideline (Singer, Clin Nutr 2023; full text): early EN within 48 h (Rec 6); low-dose EN once shock is controlled with fluids and vasopressors (Rec 11);
#    hypocaloric, not exceeding 70% of EE, in the early phase (Rec 23); 80–100% of measured EE after day 3 (Rec 24); 1.3 g/kg/day protein delivered progressively (Rec 25); supplemental PN
#    weighed case by case in the first week, commentary puts the optimal timing at days 4–7 (Rec 10); PN within 3–7 days if oral and EN are contraindicated (Rec 17).
#  - ASPEN 2022 (Compher, JPEN; ASPEN factsheet): 12–25 kcal/kg/day in the first 7–10 days (no outcome difference higher vs lower); protein 1.2–2.0 g/kg/day carried over from 2016;
#    either EN or PN acceptable in the first week; do not start supplemental PN before day 7 (strong, high quality).
#  - SCCM/ASHP 2024 stress-related GI bleeding guideline (sccm.org): coagulopathy, shock and chronic liver disease are risk factors; ventilation alone is not firmly one; SUP suggested with risk
#    factors and in neurocritical care; suggested against in enterally fed low-risk patients; PPI or H2RA; enteral or IV; low dose; stop when the risk factor resolves and before ICU transfer out.
#  - REVISE (Cook, NEJM 2024; thebottomline.org.uk): n 4,821 ventilated; IV pantoprazole 40 mg daily vs placebo; clinically important UGIB 1.0% vs 3.5% (HR 0.30, NNT 40); 90-day mortality
#    29.1% vs 30.9% (NS); VAP 23.2 vs 23.8%, C. difficile 1.2 vs 0.7% (NS).
#  - ACG 2024 acute pancreatitis guideline (Tenner; MDCalc summary): transabdominal ultrasound for biliary aetiology; moderately aggressive fluids; early oral feeding within 24–48 h in mild AP;
#    no prophylactic antibiotics in severe AP; medical therapy over early ERCP without cholangitis.
#  - ACG–CAG 2022 antithrombotics in GI bleeding (Abraham, PMC8966740): warfarin-associated GIB — suggest against FFP; no recommendation for or against PCC vs no PCC, PCC preferred over FFP if a
#    reversal agent is used; suggest against vitamin K; do not hold secondary-prevention aspirin, resume on the day haemostasis is confirmed; suggest against platelet transfusion on antiplatelets.
#  - Baveno VII / review (Cleve Clin J Med 2024): vasoactive drug 2–5 days; ceftriaxone 1 g/day; Hb target 7–8; no FFP or platelets; endoscopy within 12 h; pre-emptive TIPS within 72 h for
#    Child C 10–13 or Child B 8–9 with active bleeding; García-Pagán 2010 (n 63): bleeding-free 97% vs 50% at 1 year, higher survival; IPD meta-analysis 1-year survival HR 0.43.
#  - ADQI–ICA 2024 AKI in cirrhosis (Nadim, J Hepatol 2024; PMC11193657): the fixed 48-h albumin challenge is no longer required; if volume status is unclear, a fluid challenge (albumin
#    1–1.5 g/kg of 20–25%, or crystalloid) and HRS-AKI if no improvement within 24 h; terlipressin first line with albumin (infusion 2–12 mg/day or 1–2 mg 6-hourly), noradrenaline second line;
#    increase dose if creatinine has not fallen 25% at 24 h; HRS-AKI / AKD / CKD replace type 1 and type 2.
#  - EASL 2017 ALF guideline (easl.eu): INR >1.5 with HE, no prior liver disease; hyperacute (HE within 7 days of jaundice), acute (8–28 days), subacute (5–12 weeks); hypertonic saline to
#    sodium 145–155 in the cited trial (Murphy 2004), routine sodium 140–145/150; CRRT rather than intermittent dialysis; NAC in early stages even in non-paracetamol ALF (benefit in mild HE only);
#    routine FFP not supported, only for procedures or bleeding.
# From standard references without a fresh check (confident unless said): EFFORT Protein (Heyland, Lancet 2023: ≥2.2 vs ≤1.2 g/kg, no benefit, worse with AKI or high SOFA); PRECISe (Bels, Lancet 2024:
# 2.0 vs 1.3 g/kg, worse health-related quality of life); EPaNIC 2011 (late PN on day 8 better than early); NUTRIREA-2/-3; NICE CG32 refeeding criteria and 10 kcal/kg (5 in extreme cases);
# WSACS 2013 definitions; Revised Atlanta 2012; WATERFALL (NEJM 2022: fluid overload 20.5% vs 6.3%, no difference in severity); POINTER 2021; PANTER 2010; TENSION 2018; APEC 2020;
# Villanueva 2013 (NEJM: Hb 7 vs 9 in UGIB, 6-week survival 95% vs 91%); TRIGGER 2015 (cluster feasibility, Hb 8 vs 10); Lau 2020 (NEJM: endoscopy ≤6 h no better than 6–24 h);
# ESGE 2021 NVUGIH (GBS ≤1 outpatient; shock index >1 = instability; VKA + instability → vitamin K + PCC); AIMS65 items; ACG 2023 lower GI bleeding (CTA first in ongoing haematochezia);
# King’s College criteria and Bernal 2002 lactate; Lee 2009 (NAC in non-paracetamol ALF, coma I–II transplant-free survival 52% vs 30%); Squires 2013; Larsen 2016 (HVPE); Sort 1999
# (albumin in SBP: HRS 10% vs 33%, death 10% vs 29%); CONFIRM 2021 (HRS reversal 32% vs 17%, respiratory-failure deaths 11% vs 2%); EASL 2018 (SBP culture negative in up to 60%; the verified source is EASL 2010).
# Not verified: the card’s ‘lactate above 2.5 = higher risk’ (GIN-08e) and ‘empty left iliac fossa’ in sigmoid volvulus (GIN-07c) are kept as card wording.
# Second check (20 Nov 2026, from trial abstracts and summaries): WATERFALL (20 mL/kg + 3 mL/kg/h vs 10 mL/kg only if hypovolaemic + 1.5 mL/kg/h; overload 20.5% vs 6.3%; moderately
#  severe/severe 22.1% vs 17.3%, NS; stopped at first interim, n 248); Villanueva 2013 (n 889; Hb <7 target 7–9 vs <9; 6-week survival 95% vs 91%, HR 0.55; rebleeding 10% vs 16%);
#  Lee 2009 (n 173; overall 3-week survival 70% vs 66% NS; TFS 40% vs 27%; coma I–II 52% vs 30%; III–IV 9% vs 22%); Squires 2013 (n 184; 1-year survival 73% vs 82% NS; 1-year TFS 35% vs 53%);
#  Sort 1999 (renal impairment 10% vs 33%; in-hospital death 10% vs 29%; 3-month 22% vs 41%); CONFIRM (n 300; HRS reversal 32% vs 17%; respiratory deaths 11% vs 2%); EFFORT Protein (≥2.2 vs
#  ≤1.2 g/kg; discharge alive NS; worse with AKI and SOFA ≥9); PRECISe (2.0 vs 1.3 g/kg; worse EQ-5D-5L utility at 180 days, more GI intolerance); Larsen 2016 (n 182; TFS HR 0.56; hospital
#  survival 58.7% vs 47.8%); EASL 2010 ascites guideline (‘culture negative in as many as 60%’, albumin 1.5 then 1 g/kg, 8 g/L after LVP); ASPEN 2022 factsheet (no supplemental PN before day 7,
#  strong/high); SCCM/ASHP 2024 (sccm.org summary); terlipressin 2 mg 4-hourly for the first 48 h, then 1 mg 4-hourly (Clin Endosc review citing guidelines). PANTER 40% vs 69% and the Atlanta
#  persistent organ failure mortality (36–50%) from memory.

SPINE = [
  ("Feeding the critically ill gut", "Feed the gut early, give less than the full target in the first week because the body is still making its own glucose, and in the starved patient start very low because refeeding pulls phosphate into cells."),
  ("Prevention bundle: SUP and mobilisation", "Acid suppression is for patients with real bleeding risk and stops when the risk does, while mobilisation starts as soon as the safety screen allows."),
  ("The abdomen under pressure", "Rising abdominal pressure, pancreatitis and the surgical abdomen all hide behind sedation and shock, so the ICU finds them by measurement, imaging at the right time, and a low threshold to drain or decompress."),
  ("Bleeding: restrict, scope, stop", "In GI bleeding transfuse to about 7–8, give the drugs before the scope, scope early, and when endoscopy cannot reach or stop the bleed let interventional radiology or TIPS do it."),
  ("The failing liver, acute and chronic", "Acute liver failure kills through the brain, so prognosis, ammonia and sodium matter more than the INR; decompensated cirrhosis kills through infection and the kidney, so SBP is treated at once and albumin protects the kidney."),
  ("Sweep: the reflexes that fail", "The exam tests the instinctive wrong move — early PN, endless SUP, diuretics for ACS, early CT, prophylactic antibiotics, fixing the INR, waiting for cultures — so each must be unlearned."),
]

PRIMER = "Critical illness changes how the gut and liver behave: the stressed body breaks down muscle and makes its own glucose whatever is fed, the gut barrier weakens when it is left empty, and the splanchnic circulation is the first to be sacrificed in shock. In cirrhosis the portal pressure is high and the circulation is vasodilated, so extra volume raises variceal pressure and anything that lowers effective blood volume (infection, bleeding, paracentesis) threatens the kidney. A prolonged INR in liver disease reflects low synthesis of both pro- and anticoagulant factors, so it measures liver function, not bleeding risk. Abdominal signs are muted by sedation, opioids and ventilation, which is why pressures, lactate and imaging replace the examining hand."

L = {}

L['GIN-01'] = dict(
  sub="GI → Nutrition → Timing, targets and supplemental PN",
  step=1,
  intro="Step 1 starts with feeding, because every patient in the ICU needs a plan by day 2. The early catabolic phase is the key idea: the body makes its own glucose from muscle whatever you give, so full feeding in week 1 adds to it rather than replacing it. The four real questions test the arithmetic of the target, the 70% rule in week 1 and the day-8 rule for parenteral nutrition.",
  parts=[
    ('a', "**Within 24–48 h once haemodynamically stable — low or stable vasopressor doses are not a contraindication.** Enteral feeding keeps the mucosa fed from the lumen, which preserves the tight junctions, gut-associated immune tissue and blood flow. ESPEN 2023 recommends early EN within 48 h and allows low-dose EN as soon as shock is controlled with fluids and vasopressors; uncontrolled shock, rising doses or rising lactate are the reasons to wait, because feeding raises gut oxygen demand and in NUTRIREA-2 full early EN in shock brought more bowel ischaemia without saving lives."),
    ('b', "**Energy in week 1: 12–25 kcal/kg/day (ASPEN 2022), full target ~25 kcal/kg later. Protein 1.2–2.0 g/kg/day (ASPEN) or 1.3 g/kg/day reached progressively (ESPEN 2023). Avoid early high protein: EFFORT Protein (≥2.2 g/kg) no benefit, possible harm with AKI or high SOFA; PRECISe (2.0 vs 1.3) worse functional recovery.** Without indirect calorimetry the full target is 25–30 kcal/kg/day of actual body weight, which is why an 80 kg trauma patient needs 2,000–2,400 kcal (only 2,100 fits). Protein targets came down because amino acids in the acute phase are not built into muscle; they are oxidised, raise urea and may suppress autophagy, the cell’s clean-up process. PRECISe found worse health-related quality of life at the higher dose."),
    ('c', "**Hypocaloric early (≤ 70% of target), reaching 80–100% after day 3.** Endogenous glucose production in the first days covers a large part of energy need and is not switched off by feeding, so a ‘full’ prescription becomes overfeeding (hyperglycaemia, more CO₂, liver fat). ESPEN states it as not exceeding 70% of expenditure early, then 80–100% after day 3. So a 60 kg patient on day 2: 25 × 60 = 1,500 kcal, and 70% = 1,050 kcal."),
    ('d', "**Only if enteral feeding falls short by day 4–7 (ESPEN 3–7; ASPEN 7).** EPaNIC (2011) is the reason: starting PN on day 8 instead of day 3 meant fewer infections, shorter ICU stay and faster recovery. ASPEN 2022 recommends not starting supplemental PN before day 7 in patients who are not malnourished; ESPEN weighs it case by case and places it around days 4–7. A severely malnourished patient who cannot be fed enterally is the exception: PN can start early but slowly."),
  ],
  mimic=[
    ("Supplemental PN vs PN when EN is impossible", "Supplemental PN tops up a failing EN and waits until day 4–7 (ASPEN after day 7); PN for a patient who cannot be fed enterally starts within 3–7 days, earlier if he is malnourished."),
    ("Full target vs week-1 target", "25–30 kcal/kg is the full goal; in week 1 you give at most 70% of it (or 12–25 kcal/kg)."),
  ],
  traps=[
    ("“Day 3, failed EN, hypermetabolic — start total or supplemental PN now to avoid the deficit”", "EPaNIC showed early PN harms (more infections, longer stay); the deficit in week 1 is tolerated. Delay PN to day 8 and keep trying trophic EN. Naven lost GT4 Q11 on exactly this."),
    ("“80 kg patient: 1,500 or 1,800 kcal is the target” (68% got GT1o wrong)", "The question asks the daily goal, not the week-1 delivery: 25–30 kcal/kg gives 2,000–2,400. When the stem says ‘day 2’ or ‘first week’, apply the 70% rule instead."),
    ("“High protein (>2.0 g/kg) from day 1 prevents muscle wasting”", "EFFORT Protein and PRECISe found no benefit and signals of harm, especially with AKI; protein is built up progressively to about 1.3 g/kg."),
  ],
  decode=[
    ("80 kg intubated trauma patient — daily calorie goal for tube feeding? [DocT GT, 32% right]", "25–30 kcal/kg → about 2,100 kcal/day."),
    ("60 kg COPD patient on day 2 of ventilation — calories to give? [DocT GT]", "25 × 60 = 1,500; ≤70% in week 1 → 1,050 kcal."),
    ("Faecal peritonitis, noradrenaline 0.2, EN failed on day 3 — next step per EPaNIC? [DocT GT]", "Delay PN until day 8; continue trophic EN."),
    ("Septic cachexia — nutrition plan to prevent atrophy? [NEET 2024]", "High-protein, hypocaloric enteral feeding."),
  ],
  punch="Feed the gut within 48 h, give no more than 70% of the 25–30 kcal/kg target in week 1, build protein to about 1.3 g/kg, and keep PN back until day 8 unless the patient is malnourished.",
)

L['GIN-02'] = dict(
  sub="GI → Nutrition → Refeeding syndrome and nutritional markers",
  step=1,
  intro="Step 1 has a danger built in: the starved patient. During starvation the body runs on fat, insulin is low and intracellular phosphate, potassium and magnesium are depleted although serum levels look normal. The first carbohydrate load releases insulin, which drives these ions into cells to make ATP and glycogen, and the serum levels crash. The four questions ask the consequence (heart failure, weaning failure), the ion responsible and the order of replacement.",
  parts=[
    ('a', "**BMI below 16, weight loss above 15%, little intake for above 10 days, or low K/PO4/Mg before feeding.** These are NICE’s single high-risk criteria; two of the lesser ones (BMI under 18.5, weight loss over 10%, little intake over 5 days, alcohol misuse or drugs such as insulin, chemotherapy, antacids or diuretics) also make a patient high risk. Chronic alcohol use, a nursing-home resident with quadriplegia and the frail elderly are the exam’s typical patients."),
    ('b', "**10 kcal/kg/day (5 if extreme), thiamine before feeding, build up over 4–7 days.** Starting low limits the insulin surge; 5 kcal/kg is for BMI under 14 or negligible intake for over 15 days. Thiamine is the cofactor that carbohydrate metabolism uses up, so feeding a depleted patient can precipitate Wernicke’s encephalopathy or wet beriberi. Potassium, phosphate and magnesium are replaced as they fall, and fluid is restricted because insulin also causes sodium and water retention."),
    ('c', "**Hypophosphataemia (plus low K, low Mg) — insulin drives them into cells.** Phosphate is needed for ATP and 2,3-DPG, so its loss weakens every muscle: the diaphragm (failure to wean), the myocardium (acute heart failure within days of starting feeds), skeletal muscle (rhabdomyolysis), plus haemolysis, confusion and seizures. Hypokalaemia and hypomagnesaemia cause the arrhythmias and the long QT, but the respiratory muscle weakness is the phosphate."),
    ('d', "**Prealbumin (half-life 2–3 days). Albumin (~20 days) reflects inflammation, not recent intake.** A short half-life means the level responds within days to a change in intake. Both are negative acute-phase proteins, though: the liver makes less of them when CRP is high, so in the inflamed ICU patient a low prealbumin may mean inflammation, which is why ASPEN does not use either as a nutrition marker. Transferrin (8–10 days) sits in between."),
  ],
  mimic=[
    ("Refeeding hypophosphataemia vs critical illness weakness", "Refeeding weakness appears 2–4 days after feeds start in a starved patient with a falling phosphate; ICU-acquired weakness comes with sepsis, steroids and immobility and a normal phosphate."),
    ("Refeeding heart failure vs volume overload or PE", "Phosphate-driven failure follows the start of feeding in a frail or starved patient; check phosphate before blaming cor pulmonale or a clot."),
  ],
  traps=[
    ("“Low calcium and low phosphate: give IV phosphate first” (76% got GT2o wrong)", "Phosphate given into a hypocalcaemic patient binds calcium (calcium-phosphate precipitation) and deepens hypocalcaemia and tetany. Give IV calcium first, then IV phosphate; phosphate below 1 mg/dL is severe and oral replacement is too slow."),
    ("“Prealbumin is useless in the ICU, so albumin is the better marker” (only 34% picked prealbumin)", "For short-term change the answer is prealbumin, because of its 2–3-day half-life; albumin changes too slowly to show a response to feeding."),
    ("“Weakness and long QT after refeeding = hypokalaemia or hypomagnesaemia”", "Those explain the ECG; respiratory muscle weakness and failure to wean are hypophosphataemia (ATP depletion)."),
  ],
  decode=[
    ("Quadriplegic nursing-home patient on new tube feeds: Ca 7.0, PO₄ 0.9, Mg 1.6 — replacement strategy? [DocT GT, 24% right]", "IV calcium first, then IV phosphate."),
    ("Frail 82-year-old, NG feeds started, left heart failure at 24 h — cause? [DocT GT, 57% right]", "Low phosphate."),
    ("Alcoholic with pancreatitis, 8 days poor intake, weak and failing to wean 48 h after EN — which ion? [DocT GT]", "Hypophosphataemia."),
    ("Severe ARDS, BMI 16, volume overloaded — feeding strategy? [Marrow]", "Low-rate EN (10 kcal/kg), advance slowly."),
  ],
  punch="In the starved patient, insulin from the first feed pulls phosphate into cells, and the diaphragm and heart fail; start at 10 kcal/kg with thiamine first, replace phosphate (after calcium if both are low), and track short-term change with prealbumin.",
)

L['GIN-03'] = dict(
  sub="GI → ICU bundle → Stress ulcer prophylaxis and early mobilisation",
  step=2,
  intro="Step 2 is the preventive bundle. Stress ulcers come from splanchnic hypoperfusion: a mucosa short of blood cannot keep its mucus and bicarbonate barrier, and acid does the rest. Prophylaxis helps only when that risk is real, and it carries costs (pneumonia, C. difficile), so the questions test who gets it and when it stops.",
  parts=[
    ('a', "**Coagulopathy, shock, chronic liver disease (SCCM/ASHP 2024; ventilation alone is not a firm risk factor). Older lists: ventilated above 48 h, TBI/burns, prior GI bleed. PPI (e.g. esomeprazole) or H2RA, enteral or IV — whichever is feasible.** The 2024 guideline names those three as the risk factors and also suggests SUP in neurocritical care. Either drug class is first line (PPIs lower bleeding more; their effect on mortality in the sickest is uncertain), at low dose (esomeprazole or pantoprazole 40 mg/day or less), by whichever route works. REVISE, published after the guideline, found that IV pantoprazole 40 mg in ventilated patients cut clinically important bleeding from 3.5% to 1.0% without changing mortality, pneumonia or C. difficile, so ventilation is again a reasonable indication. High-dose steroids in acute spinal cord injury raised GI bleeding about 1.5-fold in NASCIS II, which is why the steroid-treated SCI patient is the one who most needs SUP; early enteral feeding itself lowers the risk."),
    ('b', "**When risk factors resolve — never continue it after ICU discharge (↑ C. difficile, pneumonia).** Acid is a defence against swallowed bacteria; removing it allows gastric colonisation, aspiration pneumonia and C. difficile. SCCM/ASHP make stopping SUP before transfer out of the ICU a good practice statement, because a PPI started in the ICU is otherwise continued for months without a reason."),
    ('c', "**Progressive assisted mobilisation (sit, stand, march). Passive range of motion is for sedated/unstable patients.** The safety screen (awake and cooperative, low or no vasopressor, FiO₂ ≤0.6 and PEEP ≤10) is passed here: PEEP 8 and no pressors. An MRC sum score of 52/60 is near-normal strength (below 48 defines ICU-acquired weakness), so he can bear weight and should progress to standing and marching on the spot."),
  ],
  mimic=[
    ("SUP indication vs routine", "A risk factor (coagulopathy, shock, chronic liver disease, neuro-critical illness, high-dose steroids) justifies it; an enterally fed low-risk patient does not."),
    ("Active vs passive mobilisation", "Active, progressive mobilisation for the awake patient who passes the screen; passive range of motion for the sedated or unstable."),
  ],
  traps=[
    ("“SUP must be given IV”", "Enteral and IV are equally acceptable; use whichever is feasible. Naven lost GT4 Q6 on ‘IV only’."),
    ("“Continue the PPI after ICU discharge to prevent late bleeding”", "Stop when the risk resolves, and before transfer out; continuing it adds pneumonia and C. difficile with no benefit. GT4 Q8 was lost here."),
    ("“Early enteral feeding in acute SCI is a reason for SUP”", "Enteral feeding protects the mucosa and lowers the risk; chronic SCI years after injury needs no SUP."),
  ],
  decode=[
    ("Which acute spinal cord injury patient most needs SUP? [DocT GT, 85% right]", "The one on high-dose corticosteroids."),
    ("[pattern] Awake, MRC 52/60, off pressors, PEEP 8 — which mobilisation?", "Progressive active mobilisation (sit, stand, march)."),
  ],
  extra=[
    dict(q="What did REVISE add to the 2024 guideline?", a="In 4,821 invasively ventilated adults, IV pantoprazole 40 mg daily lowered clinically important upper GI bleeding (1.0% vs 3.5%, NNT 40) with no difference in 90-day mortality (29.1% vs 30.9%), VAP or C. difficile."),
  ],
  punch="Give SUP only to patients with a real bleeding risk (coagulopathy, shock, liver disease, steroids, often ventilation), by any route, and stop it when the risk goes and before ICU discharge.",
)

L['GIN-04'] = dict(
  sub="GI → Abdomen → Intra-abdominal hypertension and abdominal compartment syndrome",
  step=3,
  intro="Step 3 opens with the abdomen as a closed box. When its pressure rises it compresses the IVC (less venous return), the renal veins and parenchyma (oliguria), pushes up the diaphragm (high airway pressures) and lowers gut perfusion, which swells the bowel further. The six questions test the definition, the unit, and the hardest point: when to cut.",
  parts=[
    ('a', "**Normal 5–7 mmHg; grade I 12–15; II 16–20; III 21–25; IV above 25.** These are the WSACS 2013 grades; intra-abdominal hypertension is a sustained IAP of 12 mmHg or more. All are in mmHg: 1 mmHg is 1.36 cmH₂O, so a bladder pressure of 22 cmH₂O is only about 16 mmHg (grade II)."),
    ('b', "**ACS = sustained IAP above 20 + new organ dysfunction.** The organ failure is what makes it a syndrome: IAP of 22 mmHg in a comfortable burns patient passing 60 mL/h is IAH, not ACS. Primary ACS comes from disease in the abdomen (perforation, bleeding, pancreatitis); secondary from outside it (massive resuscitation, burns, sepsis capillary leak)."),
    ('c', "**Measure via bladder: ≤ 25 mL saline, supine, end-expiration, zero at mid-axillary line. Abdominal perfusion pressure = MAP − IAP (aim ≥ 60).** More saline or a head-up position falsely raises the reading; contraction of the abdominal wall does too, which is why the patient must be relaxed. APP works like cerebral perfusion pressure: a MAP of 65 with IAP 24 gives APP 41, well below 60."),
    ('d', "**NG/rectal decompression, sedation ± NMB, drain ascites percutaneously, negative balance → decompressive laparotomy for refractory ACS.** The medical steps lower the volume inside the box or make its wall more compliant. Laparotomy is for ACS that persists despite them, except when the cause itself is surgical: a perforated viscus or a bleeding abdomen needs laparotomy now, which both controls the source and decompresses."),
  ],
  mimic=[
    ("IAH vs ACS", "IAH is a number (≥12 mmHg); ACS is above 20 with new organ failure."),
    ("Surgical-cause ACS vs medical ACS", "Perforation or bleeding → immediate laparotomy; pancreatitis or over-resuscitation → medical measures and percutaneous drainage first, laparotomy if refractory."),
    ("ACS vs tension pneumoperitoneum or ileus", "Ileus is distension without organ failure; tension pneumoperitoneum is free air under pressure, a cause of ACS treated by needle or open decompression."),
  ],
  traps=[
    ("“Oliguric ACS: give a loop diuretic”", "The kidney is failing from venous and parenchymal compression, not overload it can clear; a diuretic does not lower IAP. Naven lost INI-SS Q30 on this (88% got it)."),
    ("“Perforated ulcer, IAP 26, oliguric and hypotensive: decompressive laparotomy after conservative measures fail” (DocT keys this twice)", "The key is wrong on clinical grounds: a perforation needs source control, so laparotomy is immediate (B). DocT keys B for the identical concept elsewhere and its own explanation says ‘urgent’. On exam day choose immediate laparotomy when there is a surgical cause."),
    ("“Bladder pressure 22 with no organ dysfunction = ACS”", "Without new organ failure it is IAH; and check the unit, because 22 cmH₂O is about 16 mmHg."),
    ("“Pancreatitis, 12 L in 24 h, IAP 24, oliguria — APP above 60 so continue conservatively”", "APP is 65 − 24 = 41; with organ failure this is ACS. DocT keys immediate laparotomy; guidelines go through percutaneous drainage first, but of the four options B is still best."),
  ],
  decode=[
    ("Perforated diverticulitis, septic shock, IAP 22, oliguria, high peak pressure — what is this? [DocT QBank, 90% right]", "Abdominal compartment syndrome."),
    ("Perforated duodenal ulcer, IAP 26, oliguric, hypotensive — next step? [DocT QBank 65%; DocT GT]", "Keyed ‘decompressive laparotomy after failed conservative measures’; the right answer is immediate laparotomy."),
    ("Sudden pain, septic shock, IAP 25, falling urine output — next step? [DocT QBank, 64% right]", "Immediate laparotomy and decompression."),
    ("Which scenario is most consistent with ACS? [DocT GT, 75% right]", "The massively transfused trauma patient with an open abdomen, rising peak pressures and minimal urine — organ failure decides, not the bladder number."),
  ],
  punch="ACS is IAP above 20 with new organ failure; lower the pressure medically and drain fluid percutaneously, but a surgical cause or refractory ACS goes for laparotomy, and a diuretic is never the answer.",
)

L['GIN-05'] = dict(
  sub="GI → Pancreas → Diagnosis and imaging in acute pancreatitis",
  step=3,
  intro="Step 3 continues with pancreatitis, the commonest cause of a hostile abdomen in the ICU. The diagnosis is clinical and biochemical, and imaging is used for a reason, not by reflex. The three questions test that CT is not needed to diagnose, and when it becomes useful.",
  parts=[
    ('a', "**Any 2 of 3: typical pain, lipase/amylase above 3× normal, imaging.** Typical pain is acute, constant epigastric pain radiating to the back, often eased by leaning forward. Pain plus a lipase over three times normal already makes the diagnosis, so imaging is not needed to prove it."),
    ('b', "**Lipase — more specific, stays up longer.** Lipase comes almost only from the pancreas and stays raised for 1–2 weeks; amylase also comes from salivary glands and other organs and falls within 3–5 days, so a late presenter may have a normal amylase. Amylase can also be normal in alcohol-related and hypertriglyceridaemic pancreatitis. The height of either enzyme does not predict severity."),
    ('c', "**Transabdominal ultrasound — to find gallstones (changes management).** Gallstones decide ERCP (if cholangitis) and cholecystectomy in the same admission to prevent recurrence. ACG 2024 and IAP/APA advise ultrasound in every patient, including the alcohol drinker, because a second cause is common."),
    ('d', "**Diagnostic doubt at admission, or after 72–96 h if not improving (necrosis takes days to declare).** Pancreatic necrosis develops over 2–3 days, so a CT on day 1 underestimates it; it also adds a contrast load to a kidney already at risk and does not change early treatment. The CT at 72 h or later in the patient who is not improving looks for necrosis, collections and complications."),
  ],
  mimic=[
    ("Pancreatitis vs perforation, mesenteric ischaemia, aortic aneurysm", "Pain eased by leaning forward plus lipase over 3× normal is pancreatitis; this is the one situation for an admission CT, when the diagnosis is in doubt."),
  ],
  traps=[
    ("“Alcoholic, lipase 5×, typical pain, no biliary disease: no further imaging required initially” (DocT keys this; 41% right)", "Imaging is not needed for the diagnosis, which is what the key means, but ACG and IAP/APA still advise ultrasound in every patient to look for gallstones. If the question asks what is needed to diagnose, choose ‘no imaging’; contrast CT on admission is wrong either way."),
    ("“Contrast CT on admission to stage severity”", "Too early to show necrosis and adds a contrast risk; CT after 72–96 h if the patient is not improving. Naven lost GT2 Q53 on the timing (32%)."),
    ("“Non-contrast CT or MRI to look for necrosis at 72 h”", "Necrosis is defined by lack of enhancement, so contrast is needed; contrast-enhanced CT is the standard (80% got it)."),
  ],
  decode=[
    ("Alcoholic, epigastric pain to the back, lipase 5× normal — next step in diagnosis? [DocT QBank, 41% right]", "No further imaging needed to diagnose (2 of 3 met)."),
    ("Persistent pain 72 h after admission — best imaging for necrosis or collections? [DocT QBank, 80% right]", "Contrast-enhanced CT."),
    ("Alcoholic, pain relieved leaning forward, normal LFTs, lipase 520 — diagnosis? [DocT GT, 84% right]", "Acute pancreatitis (2 of 3 criteria without the image)."),
  ],
  punch="Pancreatitis is diagnosed by pain plus lipase over three times normal; ultrasound looks for stones, and contrast CT waits 72–96 hours unless the diagnosis itself is in doubt.",
)

L['GIN-06'] = dict(
  sub="GI → Pancreas → Severity and management of acute pancreatitis",
  step=3,
  intro="Step 3 then treats the pancreatitis. Almost every element of management changed in the last 15 years towards doing less: less fluid, earlier feeding, no prophylactic antibiotics, and later, gentler intervention for necrosis. The one real question tests feeding.",
  parts=[
    ('a', "**Mild: no organ failure. Moderately severe: transient organ failure (below 48 h) or local complications. Severe: persistent organ failure above 48 h.** Revised Atlanta 2012 grades by organ failure (modified Marshall score 2 or more in the lung, kidney or circulation) and its duration, because persistent failure carries most of the deaths (a third to a half of these patients die); exacerbation of a comorbid disease also makes it moderately severe."),
    ('b', "**Moderate goal-directed Ringer’s lactate (WATERFALL: aggressive = more overload, no benefit).** WATERFALL compared a 20 mL/kg bolus then 3 mL/kg/h with 1.5 mL/kg/h (bolus 10 mL/kg only if hypovolaemic); it stopped early with fluid overload in 20.5% vs 6.3% and no reduction in severe disease. Large volumes also drive abdominal compartment syndrome (GIN-04). Ringer’s lactate is preferred over saline because it may reduce systemic inflammation."),
    ('c', "**Early oral/enteral feeding within 24–72 h.** Feeding the gut keeps the barrier intact and reduces bacterial translocation into necrosis, which lowers infection; it does not ‘stimulate’ the pancreas harmfully. ACG 2024 advises oral feeding within 24–48 h as tolerated in mild disease; in severe disease, enteral (nasogastric is as safe as nasojejunal) beats parenteral."),
    ('d', "**No prophylaxis. ERCP within 24 h only for cholangitis.** Prophylactic antibiotics do not prevent infected necrosis or death. Early ERCP without cholangitis did not help even in predicted severe gallstone pancreatitis (APEC 2020); cholangitis is an obstructed, infected duct that needs drainage."),
    ('e', "**Antibiotics (carbapenem) → delay intervention ~4 weeks (walled-off) → step-up: drain, then necrosectomy.** Infected necrosis is suspected with new fever and gas in the collection, around weeks 2–4. Waiting until the collection is walled off makes intervention safer; POINTER found no benefit from immediate drainage. Step-up (percutaneous or endoscopic drainage first, necrosectomy only if needed) cut major complications or death from 69% to 40% versus primary open necrosectomy in PANTER, and the endoscopic route caused fewer fistulas (TENSION)."),
  ],
  mimic=[
    ("Moderately severe vs severe", "The clock: organ failure that resolves within 48 h is moderately severe; beyond 48 h it is severe."),
  ],
  traps=[
    ("“Keep NPO until pain and enzymes settle”", "Early feeding within 24–72 h is better (94% got this); nil by mouth increases infection."),
    ("“Parenteral nutrition first-line in severe pancreatitis”", "Enteral beats parenteral, with fewer infections; PN only if EN fails."),
    ("“Aggressive fluids in the first 24 h prevent necrosis”", "WATERFALL showed only more overload; moderate goal-directed fluid."),
  ],
  decode=[
    ("Severe pancreatitis tolerating oral diet poorly — preferred feeding? [DocT GT, 94% right]", "Early enteral nutrition within 48 h."),
    ("[pattern] Organ failure lasting 36 h, then recovered — Atlanta grade?", "Moderately severe."),
  ],
  punch="Grade by how long organ failure lasts, give moderate Ringer’s lactate, feed the gut early, give no prophylactic antibiotics, ERCP only for cholangitis, and wait about four weeks before stepping up for infected necrosis.",
)

L['GIN-07'] = dict(
  sub="GI → Abdomen → The acute abdomen in the ICU",
  step=3,
  intro="Step 3 ends with the surgical abdomen hidden by critical illness. Sedation, opioids and ventilation remove guarding and tenderness, so these diagnoses arrive as fever, a rising lactate or unexplained shock. The three questions test acalculous cholecystitis twice and bowel obstruction once.",
  parts=[
    ('a', "**IV antibiotics + percutaneous cholecystostomy (not cholecystectomy in an unstable patient).** Acalculous cholecystitis is ischaemia of the gallbladder wall plus bile stasis (fasting, TPN, opioids, shock). It affects mainly older men and the critically ill, gangrene and perforation come early, and mortality is 10–50% versus about 1% for calculous disease. A tube placed under ultrasound drains it with no anaesthetic. Ultrasound first (wall over 3.5 mm, distension, pericholecystic fluid, sludge); if ultrasound and CT are equivocal, HIDA scintigraphy is the most accurate test, although fasting and TPN give false positives."),
    ('b', "**Strangulation → contrast CT, resuscitation, antibiotics, urgent surgery (no conservative trial).** Continuous (not colicky) pain, fever, a rising white count, localised tenderness or shock mean the bowel’s blood supply is compromised; drip-and-suck is only for uncomplicated adhesive obstruction."),
    ('c', "**Sigmoid volvulus → endoscopic decompression if no peritonitis.** The typical patient is elderly, bedridden, often on psychiatric drugs, with chronic constipation and a long redundant sigmoid on a narrow mesentery that can twist. He presents with massive tympanic distension, colicky pain and absolute constipation, and the rectum is empty on examination; the X-ray shows the ‘coffee bean’ loop rising out of the pelvis. A flexible scope untwists it and a rectal tube is left; recurrence is common, so sigmoid resection usually follows in the same admission. Peritonitis or dusky mucosa means surgery."),
    ('d', "**Acute mesenteric ischaemia → CT angiography → revascularisation/laparotomy.** Pain out of proportion to the examination is the early sign, before the bowel wall dies; AF suggests an embolus to the SMA. Lactate rises late, so a normal lactate does not exclude it; CTA is done at once."),
    ('e', "**Graded-compression ultrasound (MRI next).** No radiation; if ultrasound does not show the appendix, MRI without gadolinium is next, and CT only if MRI is unavailable."),
  ],
  mimic=[
    ("Acalculous vs calculous cholecystitis", "Acalculous: critically ill, older men, no stones, high mortality, cholecystostomy; calculous: stones, women, cholecystectomy."),
    ("Sigmoid vs caecal volvulus", "Sigmoid: elderly, bedridden, endoscopic detorsion; caecal: younger, needs surgery (right hemicolectomy)."),
  ],
  traps=[
    ("“Acalculous cholecystitis is more common in women” (85% got GT7 wrong)", "That is calculous disease; acalculous affects mainly older men and the critically ill. Mortality up to 50%, RUQ tenderness absent in about 75% at first and ultrasound about 90% specific are all true."),
    ("“Unstable acalculous cholecystitis → laparoscopic cholecystectomy”", "Too risky in shock; percutaneous cholecystostomy (only 36% chose it)."),
    ("“SBO with fever and focal tenderness after 2 days: observe 3 more days”", "Signs of strangulation demand operation (88% got this)."),
    ("“Sigmoid volvulus → emergency laparotomy” (49% right)", "Endoscopic decompression first if there is no peritonitis."),
  ],
  decode=[
    ("ICU patient, thick-walled gallbladder and pericholecystic fluid, CT inconclusive — confirmatory test? [DocT GT, 69% right]", "HIDA (cholescintigraphy)."),
    ("Acalculous cholecystitis — all true EXCEPT? [DocT GT, 15% right]", "‘More common in women’ is false."),
    ("Complete SBO with fever, leucocytosis and worse local tenderness after 2 days — next? [DocT GT, 88% right]", "Emergency operation."),
  ],
  punch="In the ICU the surgical abdomen announces itself by fever, lactate and shock; drain the acalculous gallbladder percutaneously, operate on strangulation, scope the sigmoid volvulus, and CTA the patient with pain out of proportion.",
)

L['GIN-08'] = dict(
  sub="GI → Bleeding → Upper GI bleeding on warfarin with cirrhosis",
  step=4,
  intro="Step 4 is GI bleeding, and this card is the most-asked in the deck (12 questions). The scene combines three temptations — a low Hb, a high INR and a cirrhotic — and each tempts over-treatment. The questions return again and again to the transfusion threshold and to the score that predicts death.",
  parts=[
    ('a', "**Hb 7–8 g/dL — over-transfusion raises portal pressure.** In Villanueva 2013, transfusing at Hb below 7 (target 7–9) instead of below 9 improved 6-week survival (95% vs 91%) and reduced rebleeding; in cirrhosis the liberal arm had a rise in portal pressure, because extra volume fills a high-pressure portal system. With ischaemic heart disease the threshold is about 8 (ESGE, ACG); TRIGGER (2015) only showed that a restrictive policy (below 8 vs below 10) was feasible and safe."),
    ('b', "**Early endoscopy (within 12 h variceal / 24 h non-variceal).** For non-variceal bleeding, endoscopy within 24 h after resuscitation; scoping within 6 h did not lower mortality (Lau 2020). Suspected varices (any cirrhotic) are scoped within 12 h, after vasoactive drug and antibiotic (GIN-09)."),
    ('c', "**Stop warfarin; no routine FFP (the cirrhotic INR does not predict bleeding); PCC + low-dose vitamin K only if unstable; don’t delay endoscopy for INR.** In cirrhosis the INR measures low pro-coagulant factors but ignores the equally low anticoagulants (protein C, antithrombin), so haemostasis is ‘rebalanced’. FFP adds volume (higher portal pressure) without fixing it. The ESGE 2021 line is the card’s: in a haemodynamically unstable patient on a vitamin K antagonist give IV vitamin K and PCC. ACG–CAG 2022 goes further: it suggests against FFP and vitamin K and makes no recommendation for PCC, preferring PCC over FFP only if a reversal agent is used."),
    ('d', "**No — count is normal.** Antiplatelet patients do not benefit from platelet transfusion either (ACG–CAG suggests against it, with a possible increase in mortality)."),
    ('e', "**Glasgow–Blatchford 0–1 = outpatient; shock index ≥ 0.9 = massive bleed; lactate above 2.5 = higher risk.** Glasgow–Blatchford (urea, Hb, SBP, pulse, melaena, syncope, liver and heart disease) predicts the need for intervention and is calculated before endoscopy. AIMS65 (albumin below 3 g/dL, INR above 1.5, altered mental status, SBP 90 or less, age 65 or more) predicts death. Full Rockall needs endoscopic findings; MELD is a cirrhosis score. Shock index is HR/SBP (normal 0.5–0.7): a rising heart rate with a falling pressure shows that compensation is failing, which is why it flags a large bleed before the Hb falls. ESGE uses a shock index above 1 to define haemodynamic instability; the card’s 0.9 and lactate 2.5 are not guideline cut-offs, but a raised lactate on arrival reflects tissue hypoperfusion and goes with higher mortality in observational series."),
  ],
  table=dict(title="Which GI bleeding score answers which question",
    head=["Score", "Built from", "Predicts"],
    rows=[["Glasgow–Blatchford", "Urea, Hb, SBP, pulse, melaena, syncope, liver/heart disease", "Need for intervention; 0–1 can go home"],
          ["AIMS65", "Albumin <3, INR >1.5, altered mentation, SBP ≤90, age ≥65", "In-hospital (and 30-day) death"],
          ["Rockall (full)", "Age, shock, comorbidity + endoscopic diagnosis and stigmata", "Rebleeding and death after endoscopy"],
          ["MELD", "Bilirubin, creatinine, INR (± Na)", "Cirrhosis mortality, not the bleed"]]),
  mimic=[
    ("Dieulafoy lesion vs ulcer, GAVE, AVM", "Dieulafoy is a large-calibre submucosal artery bursting through a tiny mucosal defect with no ulcer around it, usually high on the lesser curve; GAVE is striped antral ectasia; an AVM is a tangle of small vessels."),
  ],
  traps=[
    ("“After resuscitation, which score best predicts 30-day mortality? — Glasgow–Blatchford” (75% got it wrong)", "Glasgow–Blatchford predicts the need for intervention; AIMS65 predicts death. Rockall needs the endoscopy."),
    ("“IHD patient with UGIB, Hb 8.1: transfuse below 9 or 10 (TRIGGER)” (28% right in the QBank, 63% in the GT)", "With heart disease the threshold is about 8, so at 8.1 he is not transfused yet. TRIGGER did not set that number; it tested feasibility of below 8 vs below 10."),
    ("“Cirrhotic with CABG, Hb 7.8: transfuse below 9” (40% right)", "DocT keys below 7; with coronary disease many guidelines accept about 8, but 9 is wrong because it raises portal pressure. Of these options, 7 is the best."),
    ("“Correct the INR with FFP before endoscopy”", "Delays the scope and raises portal pressure; the cirrhotic INR does not predict bleeding."),
  ],
  decode=[
    ("Shock index is defined as? [DocT QBank, 66% right]", "HR/SBP."),
    ("Haematemesis, HR 130, BP 70/40, lactate 4.5 — score for 30-day mortality? [DocT QBank, 25% right]", "AIMS65."),
    ("Massive haematemesis, pulsatile arterial lesion in the stomach without an ulcer base? [DocT QBank, 58% right]", "Dieulafoy lesion."),
    ("Cirrhotic, Hb 7.5, stable; why avoid over-transfusion in varices? [DocT QBank and GT ×6, 78–100% right]", "Restrictive Hb <7 — over-transfusion raises portal pressure and rebleeding."),
  ],
  punch="In upper GI bleeding transfuse at Hb 7 (about 8 with heart disease), scope within 24 h (12 h if varices), don’t chase the cirrhotic INR, and remember that Glasgow–Blatchford predicts intervention while AIMS65 predicts death.",
)

L['GIN-09'] = dict(
  sub="GI → Bleeding → The variceal haemorrhage bundle",
  step=4,
  intro="Step 4 narrows to the bleed that kills cirrhotics. Varices bleed because portal pressure is high, so every part of the bundle either lowers that pressure (vasoactive drug, restrictive transfusion, TIPS), treats the infection that triggers bleeding, or seals the vessel. The seven questions test order: what comes before the scope, and what comes after it fails.",
  parts=[
    ('a', "**Terlipressin 2 mg 4-hourly for 24–48 h, then 1 mg 4-hourly … (or octreotide 50 µg bolus + 50 µg/h) — start before endoscopy, continue 2–5 days.** Terlipressin (a vasopressin analogue) and octreotide (a somatostatin analogue) constrict the splanchnic arterioles, so less blood reaches the portal system and the variceal pressure falls. Started at the first suspicion, before the scope, they improve bleeding control and make the endoscopy easier. Terlipressin is avoided in ischaemic heart and peripheral vascular disease because it also constricts coronary and limb vessels."),
    ('b', "**Ceftriaxone 1 g/day (up to 7 days) — ↓ infection, rebleeding and death.** Bacterial infection is present or develops in up to half of bleeding cirrhotics; endotoxin raises portal pressure and impairs clotting, so infection both triggers and sustains bleeding. Ceftriaxone is preferred in advanced cirrhosis and where quinolone resistance is common."),
    ('c', "**Restrictive transfusion (Hb 7); avoid FFP.** Target 7–8. Volume raises portal pressure and rebleeding (Villanueva); FFP and platelets do not correct cirrhotic haemostasis and add volume."),
    ('d', "**Endoscopic band ligation within 12 h.** Banding is better than sclerotherapy for oesophageal varices; a protected airway first if he is drowsy or vomiting blood. Gastric (fundal) varices take cyanoacrylate glue."),
    ('e', "**Pre-emptive TIPS within 72 h (ideally < 24 h) for Child C 10–13, Child B > 7 with active bleeding, or HVPG ≥ 20 mmHg.** TIPS decompresses the portal system directly. In García-Pagán 2010, early TIPS in high-risk patients raised 1-year freedom from rebleeding to 97% vs 50% and improved survival; an individual-patient meta-analysis confirmed lower 1-year mortality. Child C 14–15 is excluded because TIPS cannot save a liver that far gone."),
    ('f', "**Uncontrolled → covered oesophageal stent (preferred) or balloon tamponade (≤ 24 h) as bridge to rescue TIPS.** A Sengstaken–Blakemore tube compresses the varices mechanically; it stops bleeding in most but rebleeding on deflation is common and pressure necrosis or perforation follows prolonged use, so it is only a bridge (under 24 h, with the airway secured). A self-expanding covered stent controls bleeding as well with fewer complications."),
  ],
  mimic=[
    ("Variceal vs non-variceal bleed in a cirrhotic", "Any cirrhotic with portal hypertension and a big haematemesis is treated as variceal until the scope says otherwise, despite NSAIDs or known GAVE."),
    ("Pre-emptive vs rescue TIPS", "Pre-emptive: after successful banding, within 72 h, in high-risk patients; rescue: for bleeding that drugs and banding fail to control."),
  ],
  traps=[
    ("“Unstable Child C bleeder after initial resuscitation — immediate endoscopy” (59% right)", "The vasoactive drug comes first and is the keyed answer; antibiotics also start before the scope, and endoscopy follows within 12 h."),
    ("“Varices seen — best initial drug is a PPI or a β-blocker”", "Octreotide or terlipressin. PPIs do not lower portal pressure; β-blockers are for prevention, and lower the BP in an acute bleed."),
    ("“Child B, MELD 22 after banding — band every 2 weeks or β-blocker only improves survival” (62% right)", "Pre-emptive TIPS (García-Pagán) improves long-term outcome."),
    ("“Cirrhotic with NSAID use and mild GAVE — gastric ulcer or gastritis”", "The setting (portal hypertension, ascites, massive bleed) makes varices the working diagnosis (60% got it)."),
  ],
  decode=[
    ("Child C, haematemesis, BP 80/50 — after initial resuscitation, next step? [DocT QBank, 59% right]", "IV octreotide infusion (antibiotics too)."),
    ("Child B, MELD 22, stabilised after endoscopy — what improves long-term outcome (García-Pagán)? [DocT QBank, 62% right]", "TIPS within 24–72 h."),
    ("Massive variceal bleeding uncontrolled by banding and drugs — next step? [DocT GT ×2, 100% right]", "Sengstaken–Blakemore tube (or covered stent) as a bridge to rescue TIPS."),
  ],
  punch="In variceal bleeding the drug and the ceftriaxone go in before the scope, transfuse to only 7–8, band within 12 h, give high-risk patients pre-emptive TIPS within 72 h, and use a tube or stent only as a bridge to rescue TIPS.",
)

L['GIN-10'] = dict(
  sub="GI → Bleeding → Lower GI bleeding localised on CT angiography",
  step=4,
  intro="Step 4 moves below the ligament of Treitz. Most lower GI bleeds (diverticular, angiodysplasia) stop on their own; the problem is the brisk one that keeps going. The seven questions sort the right next step by two things: is he stable, and has the source been found?",
  parts=[
    ('a', "**Selective transcatheter embolisation. Laparotomy only if embolisation fails.** CTA has shown the bleeding vessel, so catheter angiography goes straight to that artery and blocks it with coils or particles, as distally as possible to limit bowel ischaemia. ACG 2023 puts CTA first in ongoing haematochezia because it detects bleeding of about 0.3–0.5 mL/min and guides the catheter; catheter angiography alone needs a faster bleed (about 0.5–1 mL/min). Surgery is the last resort, and a blind subtotal colectomy carries high mortality."),
  ],
  table=dict(title="Lower GI bleeding: next step by stability and what is known",
    head=["Situation", "Next step"],
    rows=[["Stable", "Colonoscopy within 24 h after bowel prep; treat the lesion there (clips, bands ± adrenaline)"],
          ["Unstable or ongoing, source unknown", "CT angiography first (if it causes no delay), then embolisation"],
          ["CTA shows extravasation", "Selective catheter embolisation"],
          ["Colonoscopy fails to control", "Angiographic embolisation"],
          ["Shocked, high urea:creatinine", "Exclude an upper source with OGD first"],
          ["Embolisation fails or not available", "Surgery (segmental if localised)"]]),
  mimic=[
    ("Upper vs lower source in haematochezia", "A high urea out of proportion to creatinine (ratio over 30) means digested blood from above: blood protein absorbed in the gut becomes urea in the liver while GFR is unchanged. About 10–15% of severe haematochezia is upper GI."),
    ("Tagged red-cell scan vs CTA", "Red-cell scintigraphy is slow, non-therapeutic and localises poorly but detects very slow intermittent bleeding (0.1–0.5 mL/min); CTA is fast and guides embolisation."),
  ],
  traps=[
    ("“Unstable haematochezia, colonoscopy shows diverticula but no active site — mesenteric angiography” (85% got it wrong; 15% right)", "Without a known source, CTA comes first because it is quicker and more sensitive; catheter angiography follows a positive CTA. DocT’s explanation contradicts itself on stability, but CTA stands for the unstable patient."),
    ("“Stable diverticular bleed seen at colonoscopy — embolisation or resection”", "Treat it at the colonoscopy (clips or band ligation ± adrenaline); polyethylene glycol is the prep, not a treatment. About 60% got this right."),
    ("“CTA-localised bleed — laparotomy”", "Embolise first; Naven lost GT4 Q66 choosing laparotomy in 8 seconds."),
  ],
  decode=[
    ("CTA shows sigmoid extravasation, ongoing bleeding and hypotension — next? [DocT QBank, 74% right]", "Mesenteric angiography with embolisation."),
    ("Massive haematochezia, unstable after failed endoscopic therapy — next? [DocT QBank 85%; DocT GT 80%]", "Angiographic embolisation."),
    ("Stable, painless haematochezia, diverticular bleed at colonoscopy — intervention? [DocT QBank and GT, ~60% right]", "Endoscopic clipping."),
    ("Cirrhotic after a GI bleed, rising urea with stable creatinine — why? [DocT GT, 100% right]", "Digested blood is absorbed as protein and converted to urea."),
  ],
  punch="A lower GI bleed that CTA has localised goes to selective embolisation; the stable patient gets a colonoscopy that treats, the unstable one with no source gets CTA first, and surgery waits until both fail.",
)

L['GIN-11'] = dict(
  sub="GI → Liver failure → Definition, subtypes and King’s College criteria",
  step=5,
  intro="Step 5 turns to the failing liver, starting with acute liver failure in a previously normal liver. Its danger is speed: the faster the failure, the more ammonia reaches an unadapted brain, so cerebral oedema dominates. The two questions test the definition and the tool that selects for transplant.",
  parts=[
    ('a', "**ALF = coagulopathy + encephalopathy, no prior liver disease: INR ≥ 1.5 + encephalopathy, no cirrhosis, illness below 26 weeks.** Encephalopathy is the defining feature: severe acute liver injury without it is not ALF. The ‘no cirrhosis’ rule separates ALF from ACLF (except Wilson’s, vertically acquired HBV and autoimmune hepatitis presenting acutely, which are allowed). PT 25 s in a jaundiced, confused patient with no history is ALF."),
    ('b', "**Hyperacute (below 7 days): paracetamol — most cerebral oedema but best spontaneous survival.** O’Grady sorts by the jaundice-to-encephalopathy interval: hyperacute within 7 days, acute 8–28 days, subacute 5–12 weeks. The fast form has the highest ammonia and most brain swelling but the liver regenerates if the patient survives; subacute ALF has little oedema but rarely recovers without transplant."),
    ('c', "**King’s — paracetamol: arterial pH below 7.30 after fluids, OR all of INR above 6.5 (PT above 100 s) + creatinine above 3.4 mg/dL + grade III–IV encephalopathy (modified: lactate above 3.5 at 4 h or 3.0 after fluids).** Acidosis after resuscitation reflects a liver that cannot clear lactate. The criteria are highly specific but miss some who will die, so failing to meet them does not mean the patient is safe."),
    ('d', "**King’s — non-paracetamol: INR above 6.5, OR any 3 of age below 10 or above 40; drug/indeterminate cause; jaundice → encephalopathy above 7 days; INR above 3.5; bilirubin above 17.5 mg/dL.** Here a slower course (over 7 days) and an indeterminate or drug-induced cause predict death, the opposite of paracetamol, because the slowly failing liver does not regenerate."),
  ],
  mimic=[
    ("ALF vs ACLF vs hepatic encephalopathy", "ALF: no prior liver disease; ACLF: known chronic liver disease or cirrhosis with an acute insult; HE is a feature of either, not a diagnosis of the liver."),
  ],
  traps=[
    ("“Jaundice, confusion, PT 25 s, high ammonia, no liver history — hepatic encephalopathy” (41% got it wrong)", "HE describes the brain; the syndrome is acute liver failure, because the liver was previously normal."),
    ("“MELD or ammonia decides transplant in paracetamol ALF”", "King’s College criteria are the standard prognostic tool (81% right); MELD is a cirrhosis score."),
  ],
  decode=[
    ("Paracetamol ALF, encephalopathic, INR >6.5 — most important prognostic indicator for transplant? [DocT QBank, 81% right]", "King’s College criteria."),
    ("Jaundice, confusion, PT 25 s, no liver disease, high ammonia — diagnosis? [DocT QBank, 59% right]", "Acute liver failure."),
  ],
  punch="ALF is INR ≥1.5 plus encephalopathy in a previously normal liver within 26 weeks; the hyperacute paracetamol form swells the brain most but recovers best, and King’s College criteria pick who needs a transplant.",
)

L['GIN-12'] = dict(
  sub="GI → Liver failure → ICU management of acute liver failure",
  step=5,
  intro="Step 5 continues with keeping the ALF patient alive until the liver recovers or a graft arrives. Ammonia that the liver cannot clear is taken up by astrocytes and turned into glutamine, which draws water in and swells the brain; most of ICU care is aimed at that chain. The single question tests NAC.",
  parts=[
    ('a', "**N-acetylcysteine: proven in paracetamol ALF. In adult non-paracetamol ALF it improves transplant-free survival only in coma grade I–II (52% vs 30%); no benefit in grade III–IV and no overall survival benefit (Lee 2009). Paediatric non-paracetamol ALF: no survival benefit and lower 1-year transplant-free survival (35% vs 53%), worst under 2 years (Squires 2013).** In paracetamol poisoning NAC restores glutathione; in other ALF it is thought to act through better microcirculation and antioxidant effects, which helps only before the brain is deeply affected. EASL 2017 advises NAC early even in non-paracetamol cases. A young patient with AST in the thousands, low bilirubin and early confusion is presumed paracetamol until proven otherwise, so NAC is started empirically."),
    ('b', "**Hypertonic saline to Na 145–155 (not 155–160); mannitol 0.5–1 g/kg if ICP rises.** Raising sodium makes plasma hyperosmolar and pulls water out of the brain; Murphy 2004 targeted 145–155 in high-risk patients and reduced ICP surges. Above 155 adds no benefit and risks osmotic damage. Mannitol is for ICP surges, if serum osmolality is below 320."),
    ('c', "**Early CRRT to clear ammonia; intubate grade III–IV for airway protection.** Arterial ammonia above 150 µmol/L with grade III–IV encephalopathy marks a high risk of cerebral oedema; continuous (not intermittent) RRT removes ammonia steadily without the osmotic shifts of intermittent dialysis. High-volume plasma exchange removes ammonia, cytokines and other toxins while replacing clotting factors: in Larsen 2016 (182 patients, three daily exchanges of about 15% of ideal body weight) it improved transplant-free survival in hospital (HR 0.56; overall survival 59% vs 48%), with no gain in those who went on to transplant."),
    ('d', "**No — only for bleeding or procedures (INR is a prognostic marker).** Bleeding in ALF is uncommon because anticoagulant factors fall too; FFP adds volume, raises ICP risk and destroys the INR’s value in King’s criteria and in tracking recovery."),
  ],
  mimic=[
    ("NAC in paracetamol vs non-paracetamol ALF", "Paracetamol: always, at any grade; non-paracetamol adults: helps in grade I–II only; children: no benefit, possible harm."),
  ],
  traps=[
    ("“Prophylactic hypertonic saline to sodium 155–160”", "The target is 145–155; this was the wrong statement in the GI mini test."),
    ("“Methylprednisolone or heparin empirically in hyperacute ALF”", "Steroids only for autoimmune hepatitis; the empiric drug is NAC (83% right)."),
  ],
  decode=[
    ("22-year-old, AST 5,116, ALT 4,300, INR 2.1, falling consciousness — empiric drug? [DocT GT, 83% right]", "N-acetylcysteine."),
  ],
  punch="In ALF give NAC early (paracetamol at any grade, others only in grade I–II), keep sodium 145–155, start CRRT for high ammonia, intubate grade III–IV, and leave the INR alone unless bleeding.",
)

L['GIN-13'] = dict(
  sub="GI → Liver failure → Decompensated cirrhosis: SBP, HRS-AKI and paracentesis",
  step=5,
  intro="Step 5 ends with the cirrhotic who decompensates. The circulation is already vasodilated and the kidney is kept going by renin, angiotensin and noradrenaline; infection, diuretics or a large paracentesis drop effective volume further and tip it into AKI. The three questions test treating SBP at once and the first step in cirrhotic AKI.",
  parts=[
    ('a', "**Ascitic PMN 312 cells/mm³, culture pending → start ceftriaxone/cefotaxime now — cultures are negative in 30–40%.** PMN 250/mm³ or more is SBP whatever the culture shows (PMN = total WBC × % neutrophils); culture-negative neutrocytic ascites is treated the same way, and EASL (2010 ascites guideline) notes that, despite sensitive methods, culture is negative in as many as 60% of patients with clinical SBP and a raised neutrophil count; bedside inoculation of blood-culture bottles raises the yield, so series that use it report fewer culture-negative cases. Delay raises mortality. Cefotaxime 2 g 8-hourly or ceftriaxone covers the gut Gram-negatives; hospital-acquired SBP or septic shock needs broader cover (e.g. piperacillin-tazobactam or a carbapenem)."),
    ('b', "**1.5 g/kg day 1, 1 g/kg day 3 (if creatinine above 1, BUN above 30 or bilirubin above 4) — prevents HRS.** SBP triggers vasodilation and a fall in effective volume; albumin expands the circulation and binds endotoxin. In Sort 1999 (126 patients, all on cefotaxime) it cut renal impairment from 33% to 10%, in-hospital death from 29% to 10% and 3-month death from 41% to 22%. EASL gives it to all patients with SBP; AASLD restricts it to those criteria."),
    ('c', "**Stop diuretics/nephrotoxins, volume if needed (albumin 1 g/kg), reassess at 24 h, then terlipressin + albumin.** The first step in any cirrhotic AKI is removing the cause: stop diuretics, NSAIDs, nephrotoxins and β-blockers, treat infection, replace losses. ADQI–ICA 2024 dropped the fixed 48-hour albumin challenge: if volume status is unclear, give a fluid challenge, and if creatinine or urine output has not improved within 24 h, it is HRS-AKI. Terlipressin with albumin is first line (CONFIRM: HRS reversal 32% vs 17%), but more deaths from respiratory failure mean avoiding it with SpO₂ below 90%, volume overload, ACLF grade 3 or creatinine 5 mg/dL or more; noradrenaline is the alternative."),
    ('d', "**Albumin 6–8 g per litre removed if above 5 L.** Removing over 5 L causes post-paracentesis circulatory dysfunction (renin activation, hyponatraemia, AKI, early recurrence); albumin prevents it better than other expanders."),
  ],
  mimic=[
    ("SBP vs secondary bacterial peritonitis", "Secondary (a perforation or abscess) has 2 of: total protein over 1 g/dL, glucose under 50 mg/dL, LDH above the serum upper limit, or several organisms; it needs imaging and surgery, not just cefotaxime."),
    ("Prerenal AKI vs HRS-AKI", "Prerenal improves within 24 h of stopping diuretics and replacing volume; HRS-AKI does not, with no shock, nephrotoxin or structural cause."),
  ],
  traps=[
    ("“PMN 320, Gram stain negative — lactulose and hold antibiotics, or metronidazole plus ciprofloxacin” (61% got it wrong)", "PMN over 250 is SBP: empirical cefotaxime now. Protein 1.0 g/dL and glucose 75 do not suggest secondary peritonitis, so anaerobic cover is not needed; oral ciprofloxacin is for prophylaxis."),
    ("“First step in early cirrhotic AKI: start vasoconstrictor” (31% got it wrong)", "Stage 1A is monitoring and removing risk factors; terlipressin only once HRS-AKI is established. The linked explanation still quotes the 2015 rule of 48 h of albumin 1 g/kg; ADQI–ICA 2024 shortened it to a 24-h reassessment."),
  ],
  decode=[
    ("Cirrhosis with SBP on paracentesis — antibiotic? [DocT QBank, 88% right]", "IV cefotaxime."),
    ("Febrile, hypotensive cirrhotic, ascitic PMN 320, Gram stain negative — next step? [DocT QBank, 39% right]", "Empirical cefotaxime."),
    ("First step in initial AKI in cirrhosis? [DocT GT, 69% right]", "Monitor and remove risk factors."),
  ],
  punch="In decompensated cirrhosis treat PMN ≥250 as SBP at once with cefotaxime and albumin, take away the cause of AKI first and give terlipressin with albumin only when it proves to be HRS, and replace 6–8 g of albumin per litre after a large tap.",
)

L['GIN-14'] = dict(
  sub="GI → Sweep → Nine true/false statements",
  step=6,
  intro="Step 6 gathers the reflexes the deck has dismantled. Each false statement is a plausible instinct (more nutrition, more acid suppression, more imaging, more reversal); each true one is the counter-intuitive guideline answer.",
  parts=[
    ('a', "**F — day 4–7.** Early PN worsened outcomes in EPaNIC; supplemental PN waits until EN has fallen short for 4–7 days (ASPEN after day 7) (GIN-01)."),
    ('b', "**F — stop when risk resolves.** Continuing SUP adds pneumonia and C. difficile; stop before ICU transfer out (GIN-03)."),
    ('c', "**F — decompress (drain, NMB, laparotomy).** The failing kidney in ACS is compressed, not overloaded (GIN-04)."),
    ('d', "**F — only if doubt, or after 72 h.** Necrosis is not visible early, and the diagnosis needs only pain plus lipase (GIN-05)."),
    ('e', "**F — no benefit; treat proven infection.** Prophylaxis does not prevent infected necrosis or death (GIN-06)."),
    ('f', "**F — early endoscopy; no routine reversal.** The cirrhotic INR does not predict bleeding; reversal is only for the unstable warfarin patient and must not delay the scope (GIN-08)."),
    ('g', "**T — laparotomy if it fails.** The localised vessel is embolised selectively (GIN-10)."),
    ('h', "**T — early-grade encephalopathy.** True only for adults in coma grade I–II; not in grade III–IV and not in children (GIN-12)."),
    ('i', "**F — PMN ≥ 250 = treat now.** Cultures are often negative and delay costs lives (GIN-13)."),
  ],
  mimic=[
    ("Statement h vs a blanket ‘NAC works in all ALF’", "The true version carries the grade I–II qualifier; ‘improves overall survival’ or ‘in children’ makes it false."),
  ],
  traps=[
    ("“NAC helps non-paracetamol ALF” marked false because ‘it’s only for paracetamol’", "It is true in adults with early-grade encephalopathy (Lee 2009); read the qualifier."),
  ],
  decode=[
    ("[pattern] Statements I–IV on GI critical care — which are correct?", "Mark each true or false on its own before reading the option combinations."),
    ("[pattern] All of the following are true EXCEPT (early PN, SUP after discharge, diuretics for ACS)", "Each is a reflex the guidelines reject."),
  ],
  punch="Late PN, short SUP, decompression not diuretics, late CT, no prophylactic antibiotics, no routine INR reversal, embolise the localised bleed, NAC for early-grade ALF and antibiotics for PMN ≥250 without waiting.",
)

FLAGS = {
  'GIN-03': "a: the card (following SCCM/ASHP 2024) says ventilation alone is not a firm risk factor; REVISE (NEJM 2024, published after the guideline) found IV pantoprazole in ventilated patients cut clinically important bleeding 1.0% vs 3.5% without changing mortality. Not wrong, but now incomplete; the explanation adds REVISE.",
  'GIN-04': "Card is correct. Two linked DocT items (QBank and CGT4, perforated duodenal ulcer with IAP 26) key ‘decompressive laparotomy after failure of conservative measures’; with a perforation the right answer is immediate laparotomy, which DocT itself keys for the identical concept. The CGT4 pancreatitis item keys ‘immediate laparotomy’ although guidelines go through percutaneous drainage first; still the best option offered.",
  'GIN-05': "Card is correct (ultrasound in every patient). The linked DocT QBank key ‘no further imaging required initially’ for an alcoholic with lipase 5× is defensible only for making the diagnosis; ACG 2024 and IAP/APA still advise ultrasound for gallstones.",
  'GIN-08': "c: ‘PCC + low-dose vitamin K only if unstable’ follows ESGE 2021; ACG–CAG 2022 suggests against vitamin K and FFP and makes no recommendation for PCC. e: ‘shock index ≥0.9 = massive bleed’ and ‘lactate above 2.5 = higher risk’ could not be traced to a guideline (ESGE 2021 defines instability as shock index above 1; raised lactate predicts death only in observational series with varying cut-offs). Kept as card wording; read them as approximate.",
  'GIN-09': "1: the terlipressin line repeats a step (‘then 1 mg 4-hourly for 24–48 h, then 1 mg 4-hourly’); the guideline regimen is 2 mg 4-hourly for the first 48 h (until bleeding is controlled), then 1 mg 4-hourly to prevent rebleeding, for 2–5 days in all. 5: Baveno VII writes the HVPG criterion as above 20 mmHg (card: ≥20), a trivial difference.",
  'GIN-07': "c: the stem’s ‘empty left iliac fossa’ could not be traced to a standard description of sigmoid volvulus (massive tympanic distension, left iliac fossa tenderness, an empty capacious rectum, coffee-bean X-ray); the classic ‘empty iliac fossa’ is right-sided (Dance’s sign in intussusception). The answer (sigmoid volvulus → endoscopic decompression) is unaffected.",
  'GIN-13': "a: ‘cultures are negative in 30–40%’ is at the low end; EASL 2010 says ascitic culture is negative in as many as 60% of patients with clinical SBP and a raised neutrophil count, while bedside blood-culture-bottle inoculation gives lower figures. Not wrong for the exam (the point, treat without waiting, stands). c: the linked GT2 explanation uses the 2015 ICA rule (48 h of albumin 1 g/kg); the card’s 24-h reassessment matches ADQI–ICA 2024.",
}
