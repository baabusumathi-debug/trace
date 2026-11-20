# GI02B — Explain v3 ("Learn" depth): acute pancreatitis, part 2 — fluid resuscitation and WATERFALL (design and definitions), pain and nutrition, antibiotics, the timeline,
# the lung, ventilating with intra-abdominal hypertension, the step-up approach, indications to intervene on a sterile collection, surgery and cholecystectomy, immunomodulation and a sweep.
# No mnemonics or hooks. Driven by qpack/GI02B.md (16 question links; PANC-17 pain and nutrition asked 4 times; PANC-14, PANC-18, PANC-22 and PANC-23 twice each).
# PANC-15, PANC-16 and PANC-19 have no linked question and get short explanations with [pattern] decode items.
# The card layer (gi_cardlayer.json, GI02B|…) lines and cross notes were read and the explanations agree with them; no `fix` entries exist for GI02B in trace/test/data/qbank.json (checked 20 Nov 2026).
# Fields as TOX01, plus SPINE, PRIMER and step. Table cards (no lettered parts) take parts a, b, c… in the order of the card’s rows or lines.
# Checked online on 20 Nov 2026:
#  - WATERFALL protocol (de-Madaria, Pancreatology/PMC 2020, read): hypovolaemia = one or more of creatinine >1.1 mg/dL or BUN >20, haematocrit >44%, a rise in creatinine/BUN from the previous value,
#    urine <0.75 mL/kg/h, SBP <90 with no other cause, clinical dehydration; aggressive 20 mL/kg over 2 h then 3 mL/kg/h; moderate 10 mL/kg over 2 h only if hypovolaemic, then 1.5 mL/kg/h;
#    extra boluses (20 or 10 mL/kg) only if urine <0.5 mL/kg/h or SBP <90; overload checked at 3 h, then checkpoints at 12, 24, 48 and 72 h; fluid overload = at least two of three criteria
#    (haemodynamic/imaging evidence, dyspnoea, signs), ARDS to be excluded; action = reduce or stop LR, diuretics/oxygen at discretion, ICU if refractory; oral diet when pain <5/10 and the patient feels able;
#    moderate arm may stop fluids after 8 h of tolerated feeding (as early as 20 h).
#  - WATERFALL results (NEJM 2022; Bottom Line summary): 249 of 744 planned randomised, stopped by the DSMB for harm; moderately severe or severe AP 22.1% vs 17.3% (adjusted RR 1.30, 0.78–2.18);
#    cumulative LR at 48 h 7.8 vs 5.5 L; fluid overload 20.5% vs 6.3% (adjusted RR 2.85, 1.36–5.94) — confirmed by second reviewer 20 Nov 2026 (ACP Gastroenterology summary; Northwestern PCCM summary).
#  - ACG 2024 (Tenner; guideline summaries): moderately aggressive fluids, reassess within 6 h and over 24–48 h; LR over saline; early oral feeding within 24–48 h in mild AP, low-fat solid diet;
#    enteral over parenteral in severe AP; nasogastric preferred over nasojejunal; against prophylactic antibiotics and against FNA; antibiotics used to delay drainage beyond 4 weeks; no routine antifungals;
#    cholecystectomy before discharge in mild biliary AP; delay intervention about 4 weeks; minimally invasive over open; medical therapy over ERCP within 72 h without cholangitis.
#  - IAP/APA 2013 (full text): fluids 5–10 mL/kg/h initially; no IV antibiotic prophylaxis (1B); no routine FNA (false negatives 12–25%); NG or NJ (2A); PN second line; delay intervention ≥4 weeks (1C);
#    sterile indications: obstruction by walled-off necrosis ~4–8 weeks, persistent symptoms >8 weeks, disconnected duct with symptomatic collection >8 weeks; ACS = sustained IAP >20 with new organ failure,
#    IAH >12 mmHg, grades I–IV; decompression only for sustained IAP >25 refractory to medical measures, leaving the retroperitoneum and lesser sac intact.
#  - WSES 2019 (Leppäniemi, full text): source of PANC-23 lists (after 4 weeks: ongoing organ failure without infected necrosis, obstruction, disconnected duct, symptomatic or growing pseudocyst;
#    after 8 weeks: ongoing pain) and PANC-24 surgical indications (ACS, bleeding when endovascular fails, bowel ischaemia or necrotising cholecystitis, bowel fistula into a collection, step-up);
#    no routine prophylaxis (1A); carbapenems only in the very critically ill (carbapenem-resistant Klebsiella); no routine antifungals (1B); procalcitonin the most sensitive test for infection (2A);
#    first CT at 72–96 h, repeat only if deteriorating or not improving; gastric and jejunal feeding both safe (1A); avoid TPN; index-admission cholecystectomy in mild gallstone AP (1A), deferred with collections (2C).
#  - EPIPAN (Crit Care 2023): 148 enrolled, 135 analysed; ventilator-free days to day 30 no different (median 30 vs 30); longer invasive ventilation with epidural in those ventilated.
#  - Regli et al., Ann Intensive Care 2019 (ventilation in IAH): abdomino-thoracic transmission about 50% (range 20–60%); Vt 6–8 mL/kg PBW; optimal PEEP unknown, higher PEEP may be needed;
#    driving pressure under 14 ‘not unreasonable’; plateau target − 7 + 0.7 × IAP (30 with IAP 20 → 37); IAH changes transpulmonary pressure little; inspiratory transpulmonary pressure <25.
#  - PANTER (NEJM 2010; WikiJournalClub): n 88; major complications or death 40% vs 69%; multiple organ failure 12% vs 40%; incisional hernia 7% vs 24%; new diabetes 16% vs 38%; mortality 19% vs 16% (NS).
#  - POINTER (NEJM 2021): n 104; Comprehensive Complication Index 57 vs 58; mortality 13% vs 10%; interventions 4.4 vs 2.6; 39% of the postponed arm needed antibiotics only.
#  - Pancreatic encephalopathy meta-analysis (2023, 68 cohorts): pooled incidence 11% of AP, mortality 43%.
# Second review (20 Nov 2026), checked online: TENSION (Lancet 2018 abstract): n 98, major complications or death 43% vs 45%, mortality 18% vs 13%, fistula and stay lower with endoscopy
# (fistula 5% vs 32% from the paper, as the card layer gives it); MERINO (JAMA 2018): 30-day mortality 23/187 (12.3%) vs 7/191 (3.7%); PROPATRIA (Lancet 2008): mortality 24 (16%) vs 9 (6%),
# bowel ischaemia in 9 probiotic patients (8 fatal) and none on placebo; PONCHO (Lancet 2015): readmission for gallstone complications or death 6/128 (5%) vs 23/136 (17%);
# WATERFALL protocol (Bolado, Front Med 2020): overload = at least two of three criteria, no ‘suspected/definite’ category; CytoSorb (manufacturer): hydrophobic molecules up to about 60 kDa
# (cytokines, myoglobin, bilirubin, ticagrelor, rivaroxaban); EPIPAN abstract: invasive ventilation 14 vs 6 days with epidural (p 0.02); Regli 2019 full text: transmission about 50% (20–60%),
# driving pressure ‘under 14 not unreasonable’ in the text but ‘maximum 15’ in the conclusions; Cochrane CD012959 (2020): CVVH for severe AP, 3 RCTs, 219 patients, effect on death uncertain,
# high-volume vs standard CVVH little or no difference. Ringer’s lactate calcium: about 1.4 mmol/L (2.7 mEq/L, US formulation); Hartmann’s 2 mmol/L (standard pharmacopoeia values).
# Not traced: the card’s 17-study high-volume haemofiltration meta-analysis (restated, with the Cochrane review as the counterweight).

SPINE = [
  ("Moderate Ringer’s, not a flood", "Fluids rescue the early pancreas only up to a point; WATERFALL showed that pushing them harder triples fluid overload without improving outcome, so give Ringer’s lactate moderately and to targets."),
  ("Analgesia and feeding the gut", "Pain is treated generously and multimodally, and the gut is fed early by mouth or nasogastric tube because a fed gut keeps its barrier and stops the bacteria that infect necrosis."),
  ("Infection comes late, and is proven", "Necrosis becomes infected in the second to fourth week, not on admission, so antibiotics are held for proven or strongly suspected infection and then chosen to penetrate necrosis."),
  ("The lung and the tight abdomen", "The lung is the organ that fails most often, through cytokines, fluid and enzymatic loss of surfactant, and a tense abdomen stiffens the chest wall so the ventilator must be set with that in mind."),
  ("Delay, drain, then step up", "Necrosis is left alone until it walls off at about four weeks, then infected or obstructing collections are drained first and debrided by the least invasive route, with open surgery last."),
  ("Adjuncts and the sweep", "Blood purification has not lowered long-term mortality, and the common wrong beliefs are saline, aggressive fluid, prophylactic carbapenems, parenteral feeding and early debridement."),
]

PRIMER = "The revised Atlanta classification (2012) grades acute pancreatitis by organ failure: mild has none, moderately severe has organ failure that resolves within 48 hours or local complications, and severe has organ failure lasting beyond 48 hours. The disease runs in two phases: an early phase of about a week driven by sterile inflammation (SIRS) and organ failure, and a late phase driven by local complications. Collections without necrosis are acute peripancreatic fluid collections that may mature into pseudocysts; collections with necrosis are acute necrotic collections that wall off after about four weeks into walled-off necrosis. GI02A covered cause, diagnosis and severity; this deck is what the ICU does about it."

L = {}

L['PANC-14'] = dict(
  sub="Acute pancreatitis → Fluids → Ringer’s lactate, moderate and goal-directed",
  step=1,
  intro="Step 1 is the first thing done for every patient: fluid. Inflamed pancreas leaks plasma into the retroperitoneum and the gut wall, and the old belief was that flooding the circulation early would protect the pancreatic microcirculation and prevent necrosis. Both Grand Test questions test whether you know that this belief has been replaced.",
  parts=[
    ('a', "**Ringer’s lactate: fewer ICU admissions, shorter stay, lower CRP, less organ failure.** Large volumes of 0.9% saline cause a hyperchloraemic acidosis, and acidosis activates trypsinogen and worsens inflammation in experimental pancreatitis; lactate is metabolised to bicarbonate, and balanced fluid lowered CRP and SIRS in small trials and meta-analyses. ACG 2024 suggests Ringer’s lactate over saline, and WATERFALL used it in both arms."),
    ('b', "**Early aggressive fluids.** Older guidance (IAP/APA 2013: 5–10 mL/kg/h until targets are met) assumed that more fluid early would protect the microcirculation and prevent necrosis. That came from retrospective data in which the sickest patients, who received the most fluid, also did worst, so cause and effect were never separated."),
    ('c', "**Respiratory failure and abdominal compartment syndrome.** The capillaries are already leaking, so extra fluid ends up in the lungs, the bowel wall and the retroperitoneum. A swollen gut and retroperitoneum raise intra-abdominal pressure, which cuts renal and splanchnic perfusion and stiffens the chest wall (PANC-21)."),
    ('d', "**Moderate, goal-directed resuscitation.** After WATERFALL (PANC-15), ACG 2024 suggests ‘moderately aggressive’ fluids: about 1.5 mL/kg/h, a 10 mL/kg bolus only if hypovolaemic, and frequent reassessment (within 6 hours, then over 24–48 hours) against urine output above 0.5 mL/kg/h and a falling haematocrit and BUN. A falling BUN is the most useful laboratory target because a rising BUN in the first day predicts death."),
  ],
  mimic=[
    ("Moderate fluids in pancreatitis vs 30 mL/kg in septic shock", "Pancreatitis without shock gets 10 mL/kg only if hypovolaemic, then 1.5 mL/kg/h; the sepsis bolus is for hypotension or high lactate."),
  ],
  traps=[
    ("“Early aggressive IV crystalloid is the most important early step” (DocT GT, keyed)", "It is the best of four poor options (antibiotics, necrosectomy, TPN are worse), but ‘aggressive’ is the WATERFALL loser; if ‘moderate goal-directed Ringer’s lactate’ is offered, it wins."),
    ("“Aggressive 0.9% saline boluses”", "Saline adds a hyperchloraemic acidosis and aggressive volume adds overload; 69% chose the keyed Ringer’s answer."),
    ("“Restrict fluids until electrolytes normalise”", "Too little is also harmful: hypovolaemia worsens pancreatic and renal perfusion; the target is enough, not none."),
  ],
  decode=[
    ("Severe pancreatitis, hypotension, hypoxaemia, rising creatinine; options are antibiotics, aggressive crystalloid, necrosectomy, TPN [DocT GT]", "Crystalloid — the only option that treats the early phase."),
    ("Preferred early fluid approach in severe pancreatitis [DocT GT]", "Ringer’s lactate at a moderate rate (keyed 3 mL/kg/h, which was WATERFALL’s aggressive maintenance rate; still the best option there)."),
  ],
  extra=[dict(q="When is Ringer’s lactate avoided?", a="In hypercalcaemic pancreatitis, because it contains calcium (about 1.4 mmol/L in the US formulation, 2 mmol/L in Hartmann’s); the concern is theoretical, since that is less than the normal plasma total calcium (2.2–2.6 mmol/L), but a calcium-free crystalloid is used to avoid adding any. Saline is also chosen when there is metabolic alkalosis from heavy vomiting.")],
  punch="Give Ringer’s lactate, give it moderately, and judge it by urine, haematocrit and BUN: the inflamed capillaries leak whatever you add, so too much fluid becomes lung water and abdominal pressure.",
)

L['PANC-15'] = dict(
  sub="Acute pancreatitis → Fluids → The WATERFALL trial",
  step=1,
  intro="Step 1 rests on one trial. WATERFALL (NEJM 2022) is the reason ‘aggressive fluids’ became the wrong answer, and examiners quote its arms and its result.",
  parts=[
    ('a', "**Bolus: 20 mL/kg (aggressive) vs 10 mL/kg only if hypovolaemic, none if not (moderate).** The bolus was given over 2 hours. The moderate arm gave nothing up front to a patient without hypovolaemia (PANC-16 defines it)."),
    ('b', "**Then 3 mL/kg/h vs 1.5 mL/kg/h.** For a 70 kg adult that is about 210 vs 105 mL/h; by 48 hours the aggressive arm had received a median of 7.8 L and the moderate arm 5.5 L."),
    ('c', "**Fluid overload 20.5% vs 6.3%; Ringer’s lactate in both arms, checkpoints at 12, 24, 48 and 72 hours; three times the overload, no better outcomes; primary outcome 22.1% vs 17.3% (NS); stopped at interim (249 of 744 planned) for harm.** The primary outcome was moderately severe or severe pancreatitis; it was not significantly different but leaned towards harm with aggressive fluid, so the safety board stopped the trial because there was harm without any sign of benefit. Overload was also checked at 3 hours before the first checkpoint."),
  ],
  mimic=[],
  traps=[
    ("“WATERFALL favoured aggressive fluids”", "It is the opposite: aggressive fluid caused about three times the overload and was stopped early (PANC-25 b)."),
  ],
  decode=[
    ("Which strategy did WATERFALL support, and why was it stopped? [pattern]", "Moderate, goal-directed Ringer’s lactate; stopped for harm (overload) in the aggressive arm with no benefit."),
    ("Moderate arm rates [pattern]", "10 mL/kg bolus only if hypovolaemic, then 1.5 mL/kg/h."),
  ],
  punch="WATERFALL: doubling the fluid rate tripled fluid overload and did not make pancreatitis less severe, so the trial stopped early and moderate Ringer’s became the standard.",
)

L['PANC-16'] = dict(
  sub="Acute pancreatitis → Fluids → WATERFALL definitions",
  step=1,
  intro="Step 1 in detail: ‘goal-directed’ means fluid given against defined triggers and stopped against defined harms. These are WATERFALL’s rules, and they are the bedside version of moderate resuscitation.",
  parts=[
    ('a', "**Hypovolaemia = one or more of: creatinine above 1.1 mg/dL or BUN above 20; haematocrit above 44%; urine under 0.75 mL/kg/h; systolic BP under 90; clinical dehydration.** A high haematocrit and BUN mean the plasma is concentrated by the leak into the third space. The protocol also counts a rise in creatinine or BUN from the previous value."),
    ('b', "**Repeat 10 mL/kg over 2 hours if systolic BP under 90 or urine under 0.5 mL/kg/h.** Extra boluses are kept for real hypoperfusion, not for a high heart rate or pain alone."),
    ('c', "**Three criteria: imaging or invasive evidence (wedge over 18, CVP over 12, cardiac index under 2.2), symptoms (dyspnoea), signs (oedema, rales, raised JVP); one = suspected, two = definite.** The protocol defines overload as at least two of the three, and asks that ARDS is excluded, since it gives the same picture. ‘One = suspected’ is not a protocol category (FLAG)."),
    ('d', "**Reduce or stop the infusion.** Diuretics and oxygen were at the clinician’s discretion, with ICU review if signs persist."),
  ],
  mimic=[
    ("Fluid overload vs ARDS in pancreatitis", "Both give dyspnoea and crackles; overload has high filling pressures and responds to stopping fluid, ARDS (PANC-20) does not."),
  ],
  traps=[
    ("“Tachycardia alone is a trigger for another bolus”", "The rebolus triggers are systolic BP under 90 or urine under 0.5 mL/kg/h."),
  ],
  decode=[
    ("Which finding defines hypovolaemia in a goal-directed protocol? [pattern]", "Haematocrit above 44%, BUN above 20 or creatinine above 1.1, low urine, SBP under 90."),
  ],
  punch="Fluid is triggered by concentration or low output (haematocrit over 44%, BUN over 20, urine under 0.5–0.75 mL/kg/h, SBP under 90) and stopped as soon as two signs of overload appear.",
)

L['PANC-17'] = dict(
  sub="Acute pancreatitis → Supportive care → Analgesia and nutrition",
  step=2,
  intro="Step 2 is the most asked card in this deck. Two old reflexes are tested: ‘rest the pancreas’ (nil by mouth, then parenteral nutrition) and ‘avoid opioids’. Both are wrong, and the questions check which route of feeding, when and in whom.",
  parts=[
    ('a', "**Multimodal analgesia; patient-controlled analgesia.** Paracetamol, an NSAID when the kidneys allow, and opioids by PCA. Opioids do not worsen outcome in pancreatitis (the sphincter of Oddi concern has no clinical basis), but they slow the gut. With ileus and a nasogastric tube on suction, give analgesia intravenously, because nothing is absorbed from the stomach."),
    ('b', "**Avoid NSAIDs in acute kidney injury.** NSAIDs block the prostaglandins that keep the afferent arteriole open when renal perfusion is low, which is exactly the hypovolaemic pancreatitis kidney. Of the NSAIDs, ketorolac carries the highest renal risk; IV diclofenac is acceptable when the kidneys are normal or near normal (Marrow key)."),
    ('c', "**Epidural: opioid-sparing; lower kidney injury and organ failure in observational studies only (EPIPAN RCT 2023: no benefit).** Thoracic sympathetic block improves splanchnic blood flow, which is why it looked helpful. EPIPAN (148 ICU patients) found no difference in ventilator-free days; in those who needed ventilation the epidural arm was ventilated longer."),
    ('d', "**Enteral: maintains the gut barrier, prevents bacterial translocation.** Most infected necrosis is caused by gut organisms (E. coli, Klebsiella, enterococci) that cross an ischaemic, unfed bowel wall. Feeding the lumen keeps the mucosa perfused and the barrier intact, and lowers infection and organ failure compared with parenteral nutrition."),
    ('e', "**On-demand oral feeding rather than nil by mouth.** In mild disease the patient eats when he feels able; ACG 2024 suggests a low-fat solid diet within 24–48 hours (AGA 2018 says within 24 hours). Resting the pancreas has never been shown to help and prolongs stay."),
    ('f', "**If no oral intake for 3 days: nasogastric (nasojejunal for gastroparesis).** Nasogastric feeding is as safe as nasojejunal (IAP/APA 2013, WSES 2019) and easier to place, because it needs no endoscopic or radiological guidance; a jejunal tube is kept for gastric outlet compression or delayed emptying."),
    ('g', "**Parenteral nutrition is avoided.** It is used only when enteral feeding is impossible, not tolerated or not meeting needs, because it carries line sepsis and loses the barrier benefit."),
  ],
  mimic=[
    ("Nasogastric vs nasojejunal feeding", "Equal in safety and outcome; NJ only for gastric outlet obstruction or gastroparesis."),
  ],
  traps=[
    ("“Enteral nutrition via the jejunal route only” (DocT GT)", "Only 57% chose ‘gastric or jejunal’: the jejunal-only belief is the live error; gastric feeding is equally safe."),
    ("“Mild alcoholic pancreatitis: analgesia, IV fluids, NPO, antiemetics” (Marrow key)", "Out of date: ACG 2024 and AGA advise early oral feeding as tolerated, not nil by mouth; if early oral feeding is offered, pick it."),
    ("“Ketorolac is the NSAID of choice when CKD is mild”", "Ketorolac is the most nephrotoxic NSAID; in mild CKD with ileus the Marrow key is IV diclofenac, and with AKI no NSAID."),
    ("“Probiotics prevent infected necrosis”", "PROPATRIA (predicted severe AP) found higher mortality with probiotics, 16% vs 6%, with bowel ischaemia only in the probiotic arm."),
  ],
  decode=[
    ("Severe AP, tolerating oral diet poorly: preferred feeding [DocT GT]", "Early enteral nutrition within 48 hours (94%)."),
    ("Severe alcoholic AP: appropriate nutrition [DocT GT]", "Enteral by gastric or jejunal route (57%)."),
    ("Mild alcoholic AP: best management [Marrow]", "Analgesia, fluids, antiemetics and early oral feeding; the bank’s NPO key is outdated."),
    ("AP with ileus, NG suction, early CKD: analgesic [Marrow]", "IV diclofenac — IV because of ileus, not ketorolac."),
  ],
  punch="Treat pain fully with multimodal analgesia (no NSAID in AKI), let mild patients eat, tube-feed the stomach after three days without intake, and avoid parenteral nutrition: the fed gut keeps bacteria out of the necrosis.",
)

L['PANC-18'] = dict(
  sub="Acute pancreatitis → Infection → Antibiotics",
  step=3,
  intro="Step 3 is where most antibiotic errors happen. The early fever and high counts of pancreatitis are sterile inflammation; infection of necrosis is a later event. The questions take this for granted and ask which drug once infection is shown, adding a resistance twist.",
  parts=[
    ('a', "**Prophylaxis is not recommended: no effect on infected necrosis or mortality, even in severe disease.** Randomised trials and meta-analyses show no fall in infected necrosis or death, and prophylaxis selects resistant bacteria and Candida. IAP/APA 2013, WSES 2019 and ACG 2024 all advise against it."),
    ('b', "**Only for proven or strongly suspected infected necrosis (or another infection such as cholangitis).** Antibiotics are also used in infected necrosis to buy time until the collection walls off (POINTER: 39% of patients managed this way never needed drainage)."),
    ('c', "**SIRS mimics infection: fever and raised markers do not discriminate.** In the first week the cytokine storm alone causes fever, leucocytosis and high CRP. Infection is suspected when the patient deteriorates after initial stabilisation, typically in week 2–4, and is supported by gas in the collection on CT. Routine fine-needle aspiration is no longer advised: it misses 12–25% of infections and rarely changes management."),
    ('d', "**Procalcitonin: reduces antibiotic use in the early inflammatory phase.** It rises more with bacterial infection than with sterile inflammation; WSES calls it the most sensitive laboratory test for pancreatic infection, and procalcitonin-guided stopping lowers antibiotic use without harm."),
    ('e', "**Carbapenems: penetrate necrosis; cover aerobic and anaerobic Gram-negatives and Gram-positives.** Poorly perfused necrosis lets few drugs in; carbapenems, quinolones and metronidazole reach useful levels. With a history of ESBL-producing Klebsiella, a carbapenem is the clear choice: in MERINO, piperacillin-tazobactam for ESBL bacteraemia had higher 30-day mortality than meropenem (12.3% vs 3.7%). WSES advises keeping carbapenems for the critically ill because of carbapenem-resistant Klebsiella."),
    ('f', "**Antifungals are not routine; Candida in infected necrosis marks higher mortality.** Candida in necrosis usually follows prolonged broad-spectrum antibiotics; it is treated when cultured, not prevented."),
  ],
  mimic=[
    ("Early fever in pancreatitis vs infected necrosis", "Early (week 1) fever is SIRS; infection is a late deterioration with gas on CT."),
  ],
  traps=[
    ("“Piperacillin-tazobactam for infected necrosis with prior ESBL Klebsiella”", "MERINO: pip-tazo is not a carbapenem substitute for ESBL organisms; 72% chose meropenem."),
    ("“Prophylactic carbapenem in severe necrotising pancreatitis”", "Not recommended (PANC-25 c); antibiotics only for infection."),
  ],
  decode=[
    ("Necrotising AP, gas on CT, Gram-negative rods on FNA, shock, prior ESBL Klebsiella: initial antibiotic [DocT QBank]", "Meropenem (MERINO)."),
    ("Day 7, gas in pancreatic necrosis: best initial antibiotic [Marrow]", "Imipenem — gas in the collection means infected necrosis, and carbapenems penetrate it."),
  ],
  punch="No antibiotic until necrosis is infected (late deterioration, gas on CT); then a carbapenem, because it reaches the necrosis and, after MERINO, it is the only safe choice against ESBL organisms.",
)

L['PANC-19'] = dict(
  sub="Acute pancreatitis → Course → The timeline",
  step=3,
  intro="Step 3 depends on time: what you do in pancreatitis is decided by which week it is. This table puts the decks’ numbers in order.",
  parts=[
    ('a', "**First 48 hours: ultrasound; decides transient vs persistent organ failure.** Ultrasound looks for gallstones (biliary cause), and the 48-hour line separates moderately severe from severe disease (revised Atlanta)."),
    ('b', "**After 72 hours: CT shows necrosis.** Necrosis takes 3–4 days to declare itself; an early CT underestimates it, so CT is done at 72–96 hours unless the diagnosis is in doubt."),
    ('c', "**Day 3: start tube feeding if not eating** (PANC-17 f)."),
    ('d', "**7–10 days: repeat CT in severe disease.** WSES and ACG advise repeat CT when the patient deteriorates or fails to improve, rather than on a fixed schedule."),
    ('e', "**Weeks 1–2: early deaths from SIRS and organ failure.** The first peak of deaths is the sterile inflammatory phase."),
    ('f', "**After 2 weeks: late deaths from infected necrosis.** The second peak follows infection of necrosis and its complications."),
    ('g', "**Week 4 onwards: collections wall off; intervene now.** A mature wall lets the necrosis be drained and debrided safely (PANC-22)."),
  ],
  mimic=[],
  traps=[
    ("“CT on admission to grade severity”", "Necrosis is not yet visible; early CT is only for diagnostic doubt."),
  ],
  decode=[
    ("Best time for the first contrast CT to assess necrosis [pattern]", "72–96 hours after onset."),
    ("Cause of late deaths in pancreatitis [pattern]", "Infected necrosis (after about 2 weeks)."),
  ],
  punch="Deaths come in two waves, early from organ failure and late from infected necrosis, and the calendar sets the actions: CT after 72 hours, feed by day 3, intervene after four weeks.",
)

L['PANC-20'] = dict(
  sub="Acute pancreatitis → Organ failure → The lung",
  step=4,
  intro="Step 4 starts with the lung, the organ that fails most often in pancreatitis. The one real question works backwards from markers of severity to name the complication.",
  parts=[
    ('a', "**ARDS from SIRS, fluid overload and surfactant degradation.** Activated enzymes and cytokines (IL-1, IL-6, TNF) leave the pancreas in portal blood and in lymph; the thoracic duct empties lymph into the venous return, so the lung is the first capillary bed it meets. Neutrophils injure the alveolar capillary membrane, and excess fluid (PANC-14) adds to the leak."),
    ('b', "**Pancreatic phospholipase A2 enters the circulation and breaks down dipalmitoyl phosphatidylcholine.** DPPC (lecithin) is the main surface-active lipid of surfactant; with less of it, alveoli collapse at end-expiration, compliance falls and shunt rises."),
    ('c', "**A trial of non-invasive support first; then lung-protective ventilation.** High-flow oxygen or NIV can tide over the early phase in a cooperative patient; if he fails, the ARDS rules apply (6 mL/kg, plateau under 30, PEEP), adjusted for a tense abdomen (PANC-21)."),
    ('d', "**Other findings: left-sided pleural effusion, basal atelectasis, raised diaphragm.** Inflammation tracks through the diaphragm to the left pleura; the effusion is rich in amylase. A distended abdomen pushes the diaphragm up and collapses the bases."),
  ],
  mimic=[
    ("ARDS vs fluid overload in pancreatitis", "Overload has high filling pressures and clears with less fluid; ARDS is a permeability leak with normal filling pressures."),
  ],
  traps=[
    ("“Hypocalcaemia or calcification is the complication” (Marrow explanation)", "The bank’s explanation discusses these, but the stem asks for the complication of severe disease: ARDS."),
  ],
  decode=[
    ("Raised urinary trypsinogen-2 / TAP and flank bruising: which complication? [Marrow]", "ARDS — both mark severe, necrotising disease."),
  ],
  punch="The pancreatitis lung is ARDS from cytokines, extra fluid and phospholipase A2 digesting surfactant; support it non-invasively first, then ventilate it as ARDS.",
)

L['PANC-21'] = dict(
  sub="Acute pancreatitis → Organ failure → Ventilating with intra-abdominal hypertension",
  step=4,
  intro="Step 4 continues with the abdomen pressing on the chest. Fluid, ileus and retroperitoneal oedema raise intra-abdominal pressure, and that pressure stiffens the chest wall, so the usual airway-pressure limits mislead. The one real question has a key that most guidance does not support.",
  parts=[
    ('a', "**20–60% of abdominal pressure is transmitted to the thorax.** About half on average, so an IAP of 20 mmHg adds roughly 10 mmHg to pleural pressure."),
    ('b', "**Chest wall compliance, lung volumes and FRC fall; atelectasis; airway pressures rise.** The diaphragm is pushed up, compressing the bases. The higher airway pressure is spent mostly on the stiff chest wall, not on the lung."),
    ('c', "**Tidal volume 6–8 mL/kg** of predicted body weight, as in any injured lung; there are no IAH-specific trials."),
    ('d', "**PEEP by best respiratory system compliance; higher pressures are needed to recruit.** The pressing abdomen collapses the bases, and PEEP that counters it reopens them. The best PEEP is unknown; Regli and colleagues note that PEEP of about half the IAP (in cmH2O) may be appropriate, and advise setting it by best compliance, so it is often higher, not lower."),
    ('e', "**Driving pressure under 15 cmH2O.** Regli and colleagues (2019) give 15 as the maximum in their conclusions and call under 14 ‘not unreasonable’ in the text. Driving pressure is tidal volume divided by respiratory system compliance, so it tracks lung strain; they also advise using it to avoid excessive PEEP, not to push PEEP up."),
    ('f', "**Adjusted plateau target = plateau target − 7 + 0.7 × IAP (mmHg): target 30 with IAP 20 allows 37.** Since part of the plateau goes to the chest wall, a higher plateau can still mean safe lung stress. This raises the ceiling; IAH-09 instead corrects the measured value."),
    ('g', "**Oesophageal balloon: measures transpulmonary pressure.** Oesophageal pressure approximates pleural pressure, so airway minus oesophageal pressure is the pressure across the lung itself; aim for inspiratory transpulmonary pressure under about 25 cmH2O and a PEEP that keeps end-expiratory transpulmonary pressure just positive."),
  ],
  mimic=[
    ("High plateau from a stiff lung vs from a stiff chest wall", "Only the oesophageal balloon tells them apart: a high transpulmonary pressure means lung stress, a normal one with high plateau means chest wall."),
  ],
  traps=[
    ("“Reduce PEEP to the lowest tolerable level” (DocT QBank, keyed, 66%)", "The key is debatable: WSACS 2013 makes no such recommendation and reviews set PEEP by compliance or transpulmonary pressure, often higher. If ‘titrate PEEP to compliance or oesophageal pressure’ is offered, pick it; otherwise the bank wants ‘reduce PEEP’."),
    ("“Increase tidal volume to fix the hypercapnia”", "Larger volumes raise lung strain; lung-protective volumes stay at 6–8 mL/kg."),
  ],
  decode=[
    ("Trauma, IAH (bladder 21 mmHg), worsening compliance, high plateau: preferred ventilatory strategy [DocT QBank]", "Bank key: lowest tolerable PEEP; better answer: PEEP to best compliance or transpulmonary pressure, protective volumes, and treat the IAH."),
  ],
  punch="A tense abdomen makes the chest wall stiff, so high airway pressures do not all reach the lung: keep 6–8 mL/kg, set PEEP by compliance or an oesophageal balloon (often higher), and allow a higher plateau ceiling.",
)

L['PANC-22'] = dict(
  sub="Acute pancreatitis → Intervention → The step-up approach",
  step=5,
  intro="Step 5 is the main surgical lesson of pancreatitis: do less, later. Early open necrosectomy of soft, unwalled necrosis bled and killed; the step-up approach waits, drains and debrides only what still needs it. Both questions ask what a trial proved.",
  parts=[
    ('a', "**Sterile necrosis: non-operative.** Most sterile necrosis resolves; entering it risks infecting it."),
    ('b', "**Delay any intervention to the 3rd or 4th week if stable, so the collection walls off.** Early necrosis is solid, poorly demarcated and next to inflamed vessels, so early surgery causes bleeding and organ failure. POINTER (NEJM 2021) found no advantage of immediate drainage over postponed drainage with antibiotics, and postponement needed fewer interventions (2.6 vs 4.4)."),
    ('c', "**Step 1: percutaneous or endoscopic drainage, for clinical deterioration with imaging evidence of infected necrosis.** Draining the pus controls sepsis; in PANTER about a third of patients needed nothing more."),
    ('d', "**Step 2: minimally invasive necrosectomy: VARD, or endoscopic transgastric.** VARD follows the percutaneous drain track into the retroperitoneum; the endoscopic route goes through the stomach wall into walled-off necrosis. TENSION (2018): endoscopic step-up equalled surgical step-up for major complications or death (43% vs 45%) with fewer pancreatic fistulas (5% vs 32%) and a shorter stay."),
    ('e', "**Step 3: open necrosectomy, last: high complication and death rates.** PANTER (2010): step-up vs open necrosectomy, major complications or death 40% vs 69%, new multiple organ failure 12% vs 40%, incisional hernia 7% vs 24%, new diabetes 16% vs 38%; mortality was not different (19% vs 16%)."),
  ],
  mimic=[
    ("Infected pancreatic necrosis vs other intra-abdominal sepsis", "Necrosis waits about 4 weeks and is drained first; perforation, abscess or ischaemic bowel get source control within hours."),
    ("PANTER vs TENSION", "PANTER: step-up beats open necrosectomy; TENSION: endoscopic step-up equals surgical step-up, with fewer fistulas."),
  ],
  traps=[
    ("“Early necrosectomy improves outcomes”", "Early surgery is what the step-up approach replaced; only 51% chose the PANTER answer (step-up reduces morbidity)."),
    ("“PANTER showed lower mortality”", "It lowered major complications, not death."),
    ("“TENSION: endoscopy had fewer complications overall”", "The primary composite did not differ; only fistulas and stay favoured endoscopy. It is still the best option offered."),
  ],
  decode=[
    ("True statement about PANTER [DocT QBank]", "Step-up approach reduces morbidity (51%)."),
    ("Summary of TENSION [DocT QBank]", "Endoscopic step-up associated with fewer complications (fistula), 79%."),
  ],
  punch="Wait for the wall, drain first, debride by the least invasive route, and open only last: step-up cut major complications from 69% to 40% without changing mortality.",
)

L['PANC-23'] = dict(
  sub="Acute pancreatitis → Intervention → Sterile collections: when to intervene",
  step=5,
  intro="Step 5 also covers sterile collections. Most settle, so intervention needs a reason: a mechanical problem, a patient who does not recover, or a duct that cannot heal. Both questions are about the pancreatic duct.",
  parts=[
    ('a', "**After 4 weeks: ongoing organ failure without signs of infected necrosis.** A patient who is still failing at four weeks without proven infection often has infected necrosis that tests have missed, and by now the collection has walled off enough to be drained safely."),
    ('b', "**Gastric outlet, biliary or intestinal obstruction by walled-off necrosis.** A large collection compresses the duodenum, stomach or bile duct; IAP/APA gives 4–8 weeks."),
    ('c', "**Disconnected duct syndrome.** Necrosis of the neck of the gland transects the main duct; the viable tail keeps secreting into the necrotic cavity or out of a drain, so collections recur and an external fistula persists. A transpapillary stent cannot bridge a complete gap; first line is EUS-guided transmural drainage with long-term indwelling plastic stents, and distal pancreatectomy is the definitive operation. IAP/APA places this indication at over 8 weeks; the card follows WSES 2019."),
    ('d', "**Symptomatic or growing pseudocyst.** A pseudocyst has no necrosis; size alone is not an indication."),
    ('e', "**After 8 weeks: ongoing pain or discomfort.**"),
  ],
  mimic=[
    ("Disconnected duct vs partial duct leak", "Disconnected: the duct is cut through, so a stent cannot bridge it; transmural drainage or distal pancreatectomy. Partial leak: duct in continuity, so an ERCP transpapillary stent bridges the leak."),
  ],
  traps=[
    ("“Octreotide is the definitive treatment of a disconnected tail”", "It lowers output but cannot reconnect the duct; definitive surgery is distal pancreatectomy (72%)."),
    ("“External drainage alone for an amylase-rich high-output drain with a partial leak on ERCP”", "Only 57% chose the pancreatic duct stent; the stent turns the external fistula into internal drainage."),
  ],
  decode=[
    ("High-output drain after necrotising AP, disconnected tail on CT: definitive management [DocT QBank]", "Distal pancreatectomy (EUS transmural drainage is first line if offered)."),
    ("Amylase-rich high-output drain, leak on ERCP [DocT QBank]", "Pancreatic duct stenting."),
  ],
  punch="A sterile collection is touched only for a reason: organ failure that persists, obstruction, a disconnected duct or a symptomatic pseudocyst after four weeks, or pain after eight; a cut duct needs drainage or resection, a partial leak a stent.",
)

L['PANC-24'] = dict(
  sub="Acute pancreatitis → Intervention → Surgery and cholecystectomy",
  step=5,
  intro="Step 5 ends with the few things surgery still does, and with gallstones. The real question is a bleed: a pseudoaneurysm eroding into a collection, where imaging and the radiologist come before the surgeon.",
  parts=[
    ('a', "**Surgery as the last rung of step-up; abdominal compartment syndrome; bleeding when embolisation fails; bowel ischaemia; bowel fistula.** Enzymes erode the splenic, gastroduodenal or pancreaticoduodenal arteries into pseudoaneurysms that rupture into a collection, the gut or the peritoneum. The sign is shock, a falling haemoglobin, a suddenly enlarging collection or blood in a drain; CT angiography finds the vessel and angio-embolisation stops it, with surgery only if that fails. Decompression for ACS (sustained IAP over 20 with new organ failure, IAP/APA reserves it for over 25 refractory to medical measures) leaves the retroperitoneum and lesser sac intact."),
    ('b', "**Mild gallstone pancreatitis: laparoscopic cholecystectomy during the index admission.** Waiting invites recurrence: in PONCHO, same-admission surgery lowered readmission for gallstone complications or death (5% vs 17%)."),
    ('c', "**Severe pancreatitis: deferred until collections resolve or stabilise and inflammation settles.** Operating through inflamed tissue and collections risks infecting them; IAP/APA suggests waiting about 6 weeks if collections persist."),
  ],
  mimic=[
    ("Pseudoaneurysm bleed vs haemorrhagic pancreatitis", "A pseudoaneurysm is a sudden, often late bleed with a falling Hb and enlarging collection, found on CT angiography; haemorrhagic necrosis is early and diffuse."),
  ],
  traps=[
    ("“Immediate laparotomy for a bleed into a collection”", "CT angiography then embolisation first; surgery only if that fails or he cannot be stabilised."),
  ],
  decode=[
    ("Recurrent pancreatitis with a prior collection, now shock and Hb 6.5: next step [Marrow]", "CT angiogram (then angio-embolisation)."),
  ],
  punch="Surgery in pancreatitis is for failure of everything else; a bleeding pseudoaneurysm goes to CT angiography and embolisation first, mild gallstone pancreatitis gets its gallbladder out before discharge, and severe disease waits.",
)

L['PANC-25'] = dict(
  sub="Acute pancreatitis → Adjuncts → Immunomodulation and true/false sweep",
  step=6,
  intro="Step 6 closes the deck. Since cytokines drive the early phase, removing them from the blood was an obvious idea; it has not worked. The sweep then lists the deck’s commonest wrong beliefs. The one real question asks what CytoSorb does.",
  parts=[
    ('a', "**High-volume haemofiltration (17 studies): lowers short-term (under 4 weeks) but not long-term mortality. CytoSorb: improves haemodynamics; no effect on mortality. a F: Ringer’s lactate is preferred, not saline.** The haemofiltration figure comes from one meta-analysis; the Cochrane review (2020; 3 randomised trials, 219 patients) could not tell whether haemofiltration changes in-hospital death, and found little or no difference between high-volume and standard doses. CytoSorb is a cartridge of porous polymer beads that adsorbs hydrophobic molecules of small to middle size (up to about 60 kDa, by the manufacturer’s figure): cytokines, myoglobin, bilirubin and some drugs. It is not specific for endotoxin. Saline adds chloride and acidosis (PANC-14)."),
    ('b', "**F: aggressive fluids caused more overload with no benefit** (WATERFALL, PANC-15)."),
    ('c', "**F: prophylactic carbapenem is not recommended** (PANC-18)."),
    ('d', "**F: enteral feeding is first line; parenteral nutrition is avoided** (PANC-17)."),
    ('e', "**F: infected necrosis is not debrided in week 1; delay to weeks 3–4** (PANC-22)."),
    ('f', "**T: open necrosectomy is the last step.**"),
    ('g', "**F: in severe disease cholecystectomy is deferred** (PANC-24)."),
  ],
  mimic=[
    ("CytoSorb vs polymyxin B haemoperfusion", "CytoSorb adsorbs cytokines and other mid-sized molecules; polymyxin B (EUPHRATES) binds endotoxin."),
  ],
  traps=[
    ("“CytoSorb is proven to reduce mortality”", "No trial has shown that; 59% got the mechanism right."),
    ("“CytoSorb removes only endotoxins”", "That describes polymyxin B haemoperfusion."),
    ("“CytoSorb should be started more than 24 hours after shock”", "Where it is used, it is started early (within about 24 hours)."),
  ],
  decode=[
    ("Septic shock on CytoSorb within 12 hours: true statement [DocT GT]", "Adsorbs small to middle-weight molecules (59%)."),
  ],
  punch="Removing cytokines from blood improves haemodynamics but not long-term survival; the deck’s answers are Ringer’s, moderate volume, no prophylaxis, enteral feeding, delay, and open surgery last.",
)

FLAGS = {
  'PANC-15': "The line ‘Primary outcome (moderately severe or severe pancreatitis): 22.1% vs 17.3% (NS). Stopped at interim (249 of 744 planned) for harm.’ is printed twice on the card. Minor: the protocol also checks for overload at 3 hours before the 12-hour checkpoint.",
  'PANC-16': "c: the WATERFALL protocol defines fluid overload as at least two of the three criteria (with ARDS excluded); ‘one = suspected’ is not a protocol category. a: the protocol also counts a rise in creatinine or BUN from the previous value as hypovolaemia.",
  'PANC-17': "Card correct. The Marrow key (‘NPO’ for mild AP, as the qpack records it) is out of date, and the trap says so. The card-layer cross note is inconsistent with the qpack: it calls the Marrow key ‘early oral feeding within 24 h’ and says ACG 2024 advises ‘within 24 h’; ACG 2024 says within 24–48 hours with a low-fat diet (AGA 2018 says within 24 hours).",
  'PANC-21': "Card correct (Regli 2019 conclusions give a maximum driving pressure of 15 cmH2O; the text’s ‘under 14’ is a softer suggestion). The DocT key ‘reduce PEEP to the lowest tolerable level’ is debatable (card layer agrees).",
  'PANC-23': "Card correct (matches WSES 2019). IAP/APA 2013 differs on timing: obstruction at about 4–8 weeks and disconnected duct with a symptomatic collection at over 8 weeks. The explanation mentions both.",
}
