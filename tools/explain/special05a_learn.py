# SPECIAL05A — Explain v3 ("Learn" depth): polytrauma assessment — epidemiology and the timing of death, the Berlin definition, field triage, injury and physiological scores,
# mechanism and injury pattern, the primary survey (A–B, then C–E with adjuncts), ATLS classes of haemorrhagic shock, and resequenced resuscitation (circulation before airway).
# No mnemonics or hooks. Driven by qpack/SPECIAL05A.md (25 question links: POLY-07 asked 13 times, POLY-10 five, POLY-09 four, POLY-08 two, POLY-05 once; POLY-01 to 04 and POLY-06 never).
# Fields as TOX01, plus SPINE, PRIMER and step. Cards with no linked question get short explanations with [pattern] decode items.
# `fix` entries read from trace/test/data/qbank.json (cards["SPECIAL05A|…"]) for POLY-05, 07, 08, 09, 10; POLY-10 carries the cross-note on the Marrow phenylephrine key.
# Checked online 13 Nov 2026:
#  - ATLS 11th edition (launched Sept 2025; journalfeed, Mayo Clinic, SGEM, MedCof summaries): xABCDE with exsanguinating external haemorrhage first; crystalloid minimised as a bridge
#    (one summary: at most 1 L) then balanced 1:1:1 or whole blood; TXA within 3 h, 1 g bolus + 1 g infusion; video laryngoscopy preferred, pre-induction volume and vasopressors to avoid
#    peri-intubation hypotension; selective spinal motion restriction; head and spine merged into D; hypocalcaemia added to the lethal triad (MedCof summary only; not confirmed in review, so the text no longer attributes it to ATLS 11). The 11th-edition shock-class
#    table and responder bands could NOT be opened; the explanation teaches the 10th-edition table (WikEM reproduction: arrows, base deficit 0 to −2 / −2 to −6 / −6 to −10 / ≤−10).
#  - WHO injuries and violence fact sheet: about 4.4 million injury deaths a year, nearly 8% of all deaths; 3 of the top 5 causes of death at age 5–29 are injuries.
#  - Gunst/Demetriades LA County (4,151 deaths): 50.2% within the first hour, 18.3% 1–6 h after admission, 7.6% after a week; trimodal pattern ‘does not apply’.
#  - Berlin definition (Pape, J Trauma 2014): AIS ≥3 in ≥2 regions + ≥1 of SBP ≤90, GCS ≤8, BE ≤−6.0, PTT ≥40 s or INR ≥1.4, age ≥70; mortality 18.7% overall.
#  - ACS-COT 2021 National Guideline for Field Triage (handout): red/yellow lists and SBP by age as on the card.
#  - LITFL trauma scores: AIS 1–6, ISS from 6 regions, AIS 6 → 75; RTS codes 0–4, weights 0.9368 GCS, 0.7326 SBP, 0.2908 RR; T-RTS 0–12, <11 → trauma centre; TRISS = age, ISS, RTS, blunt/penetrating.
#  - EMTRAS (Raum 2009): age, prehospital GCS, base excess, prothrombin time, each 0–3; AUC 0.83. No cut-off found for ‘over 8’.
#  - Cochrane 2018 (CD012669) POCUS in blunt trauma: sensitivity 74%, specificity 96% (adults 78/97); negative scan does not rule out. eFAST meta-analysis (CJEM 2019): pneumothorax 69/99,
#    pericardial effusion 91/94, free fluid 74/98. Goldberg: about 100–200 mL minimum detectable.
#  - GCS-P = GCS − pupil reactivity score (0, 1, 2), range 1–15 (Brennan 2018).
#  - EAST 2015 emergency department thoracotomy recommendations. AO Spine/Praxis 2024 SCI guideline: MAP ≥75–80, not above 90–95, for 3–7 days.
#  - Canadian C-spine rule and NEXUS (Stiell 2003: 99.4% vs 90.7%); Canadian CT head rule (verified but not used: no linked question).
#  - Tertiary survey review (Keijzers 2012): type I missed injuries 4.3% overall.
# From memory, not reopened: Trunkey 1983 percentages (about 50/30/20), Deakin & Low 2000 (pulse–pressure estimates overestimate), ATLS responder bands (review: 10th ed. rapid <15%, transient 15–40%, none >40%; 9th ed. 10–20 / 20–40), ATLS needle decompression site (4th/5th intercostal space anterior to mid-axillary line in adults), massive haemothorax thresholds (1,500 mL or 200 mL/h for 2–4 h), CRASH-2,
#  ISS >15 as major trauma, shock index normal 0.5–0.7, AANS/CNS 2013 MAP 85–90 for 7 days, blast injury categories, induction dose reduction in shock.

SPINE = [
  ("Who dies from trauma, and when", "Bleeding and brain injury kill most trauma patients, and most of those deaths happen in the first hours, which is why the first hour of care is organised so rigidly."),
  ("Defining and triaging the injured", "Polytrauma means serious injury in two regions plus a physiological failure, and field triage sends the patient with deranged vital signs or a high-risk injury pattern to the highest-level centre."),
  ("Scoring the damage", "Anatomical scores (AIS, ISS, NISS) count the injuries, physiological scores (RTS) measure the derangement, and TRISS combines them to compare outcomes between centres, not to triage."),
  ("Mechanism predicts the injuries", "The way the energy was delivered tells you which injuries to look for before the examination finds them."),
  ("The primary survey", "xABCDE treats each threat to life as it is found, in the order in which it would kill: catastrophic bleeding, airway, breathing, circulation, disability, exposure."),
  ("Grading and resuscitating shock", "Haemorrhagic shock is graded by how much blood has gone, and the shocked patient gets blood, not crystalloid, and has the circulation filled before the airway is taken."),
]

PRIMER = "Trauma care rests on one principle: treat the injury that will kill first before the diagnosis is complete. The primary survey (xABCDE) finds and treats immediate threats; the secondary survey is the full head-to-toe examination and history; the tertiary survey, within 24 hours, catches what both missed. Shock in trauma is bleeding until proven otherwise, and the systolic pressure is a late sign because vasoconstriction holds it until about a third of the blood volume has gone. Severity is described two ways: anatomically (how bad the injuries are) and physiologically (how deranged the patient is)."

L = {}

L['POLY-01'] = dict(
  sub="Trauma → Epidemiology → Burden and the timing of death",
  step=1,
  intro="Step 1 sets the scene: who dies after injury, from what, and when. The timing matters because it decides where effort pays: deaths in the first minutes are prevented only by prevention, deaths in the first hours by fast resuscitation, and late deaths by good intensive care.",
  parts=[
    ('a', "**Over 5 million deaths a year worldwide; a leading cause of death in the young (15–29).** The current WHO figure is about 4.4 million injury deaths a year, nearly 8% of all deaths, and three of the five leading causes of death between 5 and 29 years are injuries (road traffic injury, homicide and suicide). The ‘5 million’ figure comes from older WHO reports."),
    ('b', "**Trimodal: immediate (at scene), early (hours: bleeding, brain), late (days–weeks: sepsis, organ failure).** Trunkey’s description (1983), with the commonly quoted split: about half die within minutes from unsurvivable brain, high cord, heart or great-vessel injury; about a third die in the first hours from treatable bleeding, haematomas and haemopneumothorax, the target of the ‘golden hour’; the rest die after days to weeks from sepsis and multiple organ failure."),
    ('c', "**With modern systems, bimodal: early (neurological injury, blood loss) and late (organ dysfunction).** Better intensive care has shrunk the late peak. In a Los Angeles County study of 4,151 trauma deaths, 50% died in the first hour, 18% in the first 1–6 hours after admission and under 8% after a week, so the authors rejected the trimodal pattern; timing depended on mechanism and the body region injured. A Dallas County series (Gunst 2010) found 61% immediate, 29% early and only about 10% late deaths, and called the distribution bimodal."),
    ('d', "**Blood loss and neurological injury.** Brain injury causes the most deaths overall, but haemorrhage is the leading cause of preventable early death, which is why bleeding control now comes before the airway (POLY-10)."),
  ],
  mimic=[
    ("Leading cause of trauma death vs leading cause of preventable trauma death", "Brain injury kills most; haemorrhage is the commonest death that good care can prevent."),
  ],
  traps=[
    ("“Most trauma deaths happen days later from sepsis”", "The late peak is the smallest and has shrunk further with modern intensive care; most deaths are in the first hours."),
  ],
  decode=[
    ("Classic distribution of trauma deaths, and which peak the trauma system can change [pattern]", "Trimodal; the early (second) peak of bleeding and expanding haematomas."),
    ("Two leading causes of early trauma death [pattern]", "Haemorrhage and brain injury."),
  ],
  punch="Most trauma deaths happen early, from bleeding and brain injury; the early deaths from bleeding are the ones a trauma system can prevent.",
)

L['POLY-02'] = dict(
  sub="Trauma → Definitions → Polytrauma (Berlin definition)",
  step=2,
  intro="Step 2 begins with the word itself. ‘Polytrauma’ used to mean anything from two fractures to a high ISS. The Berlin consensus (2014) tied it to anatomy plus physiology, because a patient with two serious injuries and a deranged physiology has a much higher mortality than one with the same injuries and normal physiology.",
  parts=[
    ('a', "**AIS 3 or more in 2 or more body regions, plus 1 or more of: SBP 90 mmHg or less; INR 1.4 or more or APTT 40 s or more; GCS 8 or less; base excess −6 or worse; age 70 or more.** AIS 3 is ‘serious’, so the anatomical half requires two genuinely significant injuries in separate regions. The physiological half adds one marker of systemic failure: shock, coagulopathy, coma, acidosis or the reduced reserve of age. In the German registry used to build it (28,211 patients), mortality was 18.7% overall, and each physiological criterion on its own was associated with a mortality of over a third."),
  ],
  mimic=[
    ("Polytrauma vs multiple injuries", "Several injuries without a physiological criterion are ‘multiple injuries’; the Berlin definition requires the systemic response as well."),
    ("Berlin definition vs ISS over 15", "ISS over 15 is purely anatomical and can be reached from one region; Berlin needs two regions and physiology."),
  ],
  traps=[
    ("“Two severe injuries are enough to call it polytrauma”", "Not under Berlin: one physiological criterion (SBP ≤90, GCS ≤8, BE ≤−6, INR ≥1.4 or APTT ≥40 s, age ≥70) is also required."),
  ],
  decode=[
    ("Which is NOT a Berlin polytrauma criterion: SBP ≤90, GCS ≤8, base excess ≤−6, lactate ≥4, age ≥70? [pattern]", "Lactate; base excess is the acidosis marker used."),
  ],
  punch="Berlin polytrauma is two serious injuries (AIS ≥3 in two regions) plus one sign that the body is failing: shock, coagulopathy, coma, acidosis or age 70 or more.",
)

L['POLY-03'] = dict(
  sub="Trauma → Triage → Field triage (ACS-COT 2021)",
  step=2,
  intro="Still in step 2: before any score is calculated, the paramedic decides where the patient goes. The 2021 national field triage guideline sorts criteria into two colours. Red criteria (injury pattern, mental state, vital signs) predict a need for the highest-level centre; yellow criteria (mechanism and special situations) predict a need for a trauma centre of any level.",
  parts=[
    ('a', "**Red, to the highest-level trauma centre: penetrating head, neck, torso or proximal limb; skull deformity, spinal injury with deficit, flail chest, pelvic fracture, 2 or more proximal long-bone fractures, amputation above wrist or ankle, tourniquet; motor GCS under 6, RR under 10 or over 29, SpO₂ under 90%; SBP below 70 + 2 × age (0–9), below 90 or HR above SBP (10–64), below 110 or HR above SBP (65+).** These are the findings that predict the need for an operation, intensive care or immediate resuscitation. The pressure threshold is higher in the elderly because a ‘normal’ 110 in a hypertensive 75-year-old on a beta-blocker may already be shock; HR above SBP is a shock index over 1 (POLY-10)."),
    ('b', "**Yellow, to a trauma centre: ejection, intrusion over 12 in (occupant) or 18 in (any site), extrication; death in the same compartment, unrestrained child, rider separated, pedestrian thrown or run over; fall over 10 ft; anticoagulants, pregnancy over 20 weeks, burns with trauma, low falls in the young or old.** Mechanism alone predicts serious injury less well than anatomy or physiology, so it earns a trauma centre but not necessarily the top level. The special situations are patients in whom a small injury becomes dangerous (anticoagulated head injury) or who need specialist care (pregnancy)."),
  ],
  mimic=[
    ("Red vs yellow", "Red is what the patient has (injury, vital signs); yellow is what happened to the patient (mechanism) or who the patient is."),
  ],
  traps=[
    ("“SBP under 90 is the hypotension threshold at every age”", "From 65 years the field threshold is under 110, or HR above SBP."),
  ],
  decode=[
    ("Which field finding mandates the highest-level trauma centre: fall from 12 ft, ejection, motor GCS 5, anticoagulant use? [pattern]", "Motor GCS 5 (red); the others are yellow."),
  ],
  punch="Red criteria describe the patient’s injuries and vital signs and send him to the highest-level centre; yellow criteria describe the mechanism or the patient’s vulnerability and send him to a trauma centre.",
)

L['POLY-04'] = dict(
  sub="Trauma → Injury scores → AIS, ISS and NISS",
  step=3,
  intro="Step 3 turns injuries into numbers. All three anatomical scores start from the AIS, a dictionary that gives every individual injury a severity from 1 to 6. The difference between ISS and NISS is only which three injuries are counted.",
  parts=[
    ('a', "**AIS: severity of each injury, 1 minor to 6 unsurvivable.** 1 minor, 2 moderate, 3 serious, 4 severe, 5 critical, 6 unsurvivable with current treatment. It describes one injury and says nothing about the patient as a whole."),
    ('b', "**ISS: sum of the squares of the highest AIS in the 3 most injured body regions; range 0–75 (any AIS 6 → 75); over 15 = major trauma.** There are six ISS regions (head and neck, face, chest, abdomen and pelvic contents, limbs and bony pelvis, external). Squaring makes the score rise steeply with severity, matching the steep rise in mortality. Only one injury per region counts, so two serious injuries in the same region contribute only the worse one. An injured patient scores at least 1; 0 means no injury."),
    ('c', "**NISS: sum of the squares of the 3 worst injuries in any region; 0–75; better for penetrating torso injury and TBI.** A gunshot that injures liver, bowel and kidney, or a head with a subdural, contusion and a skull fracture, puts several serious injuries in one region. ISS ignores all but one of them; NISS counts them, so it predicts mortality better in exactly those patients."),
  ],
  mimic=[
    ("ISS vs NISS", "ISS: the worst injury in each of the three worst regions. NISS: the three worst injuries wherever they are. NISS is always equal to or higher than ISS."),
  ],
  traps=[
    ("“ISS adds up every injury the patient has”", "Only three regions, and only the worst injury in each."),
  ],
  decode=[
    ("AIS 4 head, AIS 3 chest, AIS 2 limb: ISS? [pattern]", "16 + 9 + 4 = 29, major trauma (over 15)."),
    ("Stab wound with three serious abdominal organ injuries: which score captures it best? [pattern]", "NISS."),
  ],
  punch="ISS takes the worst injury from each of the three worst regions; NISS takes the three worst injuries anywhere, so it sees multiple injuries within one region. An ISS over 15 is major trauma.",
)

L['POLY-05'] = dict(
  sub="Trauma → Scores → Physiological and combined scores",
  step=3,
  intro="Still in step 3: anatomy alone ignores how the patient is coping, so physiological scores measure the derangement and combined scores join the two. The one real question tests what each score is for, and the wrong statement was that TRISS is used for field triage.",
  parts=[
    ('a', "**RTS: RR, SBP and GCS, each coded 0–4; weighted 0.29, 0.73, 0.94; triage RTS (0–12) under 11 = severe.** Each variable is coded (GCS 13–15 = 4, SBP over 89 = 4, RR 10–29 = 4, down to 0). The triage version simply adds the codes, and a total under 11 means transfer to a trauma centre. The weighted version (0.9368 × GCS + 0.7326 × SBP + 0.2908 × RR codes) predicts survival and is used inside TRISS; GCS carries the biggest weight because brain injury is the strongest physiological predictor of death."),
    ('b', "**EMTRAS: age, GCS, base excess, prothrombin time; over 8 = high mortality.** Each of the four is scored 0–3 (total 0–12), and all are available within minutes of arrival in the emergency department, which is its point: a mortality estimate before any anatomical diagnosis is complete. It discriminated well in its validation (area under the curve 0.83). The ‘over 8’ cut-off on the card could not be confirmed."),
    ('c', "**TRISS: RTS + ISS + age (+ blunt or penetrating); benchmarking trauma care.** It gives each patient a probability of survival. Comparing the deaths a centre actually had with the deaths TRISS predicted tells you whether that centre does better or worse than expected; patients who die despite a high predicted survival are reviewed. It needs the ISS, which is not known until imaging or surgery is done, so it cannot be used in the field."),
    ('d', "**Others: anatomical AIS, ISS, NISS, ICISS; physiological APACHE, SOFA; combined ASCOT.** ICISS multiplies survival risk ratios derived from ICD injury codes. ASCOT is a refinement of TRISS that uses the anatomic profile instead of ISS."),
  ],
  mimic=[
    ("Triage RTS vs coded (weighted) RTS", "Triage RTS is the simple sum (0–12) used to decide destination; weighted RTS predicts survival and feeds TRISS."),
    ("RTS vs ISS", "RTS is physiological and can change minute to minute; ISS is anatomical and fixed once the injuries are known."),
  ],
  traps=[
    ("“TRISS is used for triage in the field”", "This was the incorrect statement in the DocT GT question. TRISS needs the ISS, which is known only after imaging or surgery; it is for audit and benchmarking."),
    ("“ISS includes physiology”", "ISS is purely anatomical; RTS supplies the physiology."),
    ("“Respiratory rate carries the heaviest weight in RTS”", "GCS does (0.94), then SBP (0.73), then RR (0.29)."),
  ],
  decode=[
    ("Trauma scores: which is incorrect — RTS measures physiological derangement; ISS is purely anatomical; AIS 6 is unsurvivable; TRISS is used for field triage? [DocT GT]", "TRISS for field triage is the incorrect statement."),
    ("Which variable carries the most weight in the RTS? [pattern]", "GCS."),
  ],
  punch="RTS measures physiology and triages, ISS measures anatomy, and TRISS combines both with age and mechanism to benchmark a centre’s outcomes; it cannot be used in the field.",
)

L['POLY-06'] = dict(
  sub="Trauma → Mechanism → Mechanism and injury pattern",
  step=4,
  intro="Step 4: the mechanism tells you which injuries to look for before the examination finds them. Each pattern follows from which part of the body met which part of the car, or from how a pressure wave behaves.",
  parts=[
    ('a', "**Windshield (spider web): head, scalp and face, cervical spine.** The unrestrained head strikes the glass, so the neck is loaded in flexion or extension."),
    ('b', "**Steering wheel: neck soft tissue, sternal fracture, myocardial contusion, pneumo- and haemothorax, flail chest, abdominal injury.** The chest decelerates against the wheel; the same deceleration is the setting for aortic injury at the isthmus (top-up on blunt mediastinal injury)."),
    ('c', "**Dashboard: knee, femur, posterior hip dislocation, pelvis; head and C-spine.** Force travels up the femur from the flexed knee and drives the femoral head out backwards; check the patella, femoral shaft and hip in every front-seat occupant with a knee abrasion."),
    ('d', "**Lateral impact: head, C-spine, torso, pelvis, proximal limbs.** There is little crumple zone at the side, so intrusion injures the near side: lateral compression pelvic fractures, rib fractures and spleen or liver depending on the side."),
    ('e', "**Blast (primary wave): air–tissue interfaces — eardrum rupture, pneumothorax and blast lung, bowel perforation.** The pressure wave damages organs where tissue meets gas. A ruptured eardrum marks significant exposure, but an intact one does not exclude blast lung. In blast terminology, secondary injury means fragments (penetrating), tertiary means being thrown, quaternary means burns and the rest; this is a different use of ‘secondary’ from the card’s watch line, where secondary injury means the physiological insult (hypoxia, hypotension, hypothermia, coagulopathy) that follows any injury."),
  ],
  mimic=[
    ("Primary blast injury vs secondary blast injury", "Primary: pressure wave, gas-filled organs. Secondary: fragments, penetrating wounds, the commonest blast injury."),
  ],
  traps=[
    ("“Intact eardrums exclude blast lung”", "Eardrum rupture is a marker of exposure, not a reliable screen; blast lung can occur with intact drums."),
  ],
  decode=[
    ("Front-seat passenger, knee abrasion, leg shortened, internally rotated and adducted [pattern]", "Dashboard injury: posterior hip dislocation."),
    ("Explosion survivor with ear pain, dyspnoea, and abdominal pain hours later [pattern]", "Primary blast injury: eardrum, blast lung, bowel perforation."),
  ],
  punch="The contact point predicts the injury: windshield → head and neck, wheel → chest, dashboard → knee to hip, side impact → pelvis, and a blast wave → the eardrum, lung and bowel.",
)

L['POLY-07'] = dict(
  sub="Trauma → Primary survey → Airway and breathing",
  step=5,
  intro="Step 5 is the primary survey, and this is the most asked card in the deck (13 questions). The principle tested again and again is order: find the threat that kills first and treat it on the spot, before moving to the next letter. Airway with spinal protection comes before breathing, and the bank tests it with stems full of distracting injuries (a skull fracture, an unstable pelvis, a quiet hemithorax) in which the airway is the first job.",
  parts=[
    ('a', "**A: look for obstruction and foreign bodies; definitive airway if GCS 8 or less or protection doubtful; manual in-line stabilisation; surgical airway if intubation fails.** The airway is escalated in steps: suction blood and debris, jaw thrust (preferred to chin lift because it moves the neck least), an oral or nasal airway, then a cuffed tube in the trachea by rapid sequence intubation with manual in-line stabilisation (the front of the collar opened), and a surgical airway when intubation fails and oxygenation cannot be maintained. That last step is scalpel cricothyroidotomy (DAS Plan D: scalpel, bougie, tube). A GCS of 8 or less means the patient cannot protect the airway: eyes to pain (2), moaning (2) and withdrawal (4) add up to 8, which is an indication to intubate even when the vital signs are normal. The cervical spine is protected in A; it is examined later, in the secondary survey."),
    ('b', "**Intubate for: obstruction, severe TBI, disrupted chest wall (flail), haemorrhage, aspiration.** These are the situations in which the airway will be lost or ventilation will fail: an airway already closing (burns, haematoma, failed basic manoeuvres), a brain that cannot protect it and needs controlled CO₂, a chest wall that cannot ventilate, and a shocked patient who needs theatre. Flail chest by itself is an indication only when breathing fails: most flail segments are managed with good analgesia (a thoracic epidural is the most effective) and oxygen or non-invasive support; the hypoxia comes mainly from the underlying contusion."),
    ('c', "**B: expose neck and chest; find tension pneumothorax, massive haemothorax, open pneumothorax, tracheobronchial injury; oxygen by reservoir mask; SpO₂ over 94%.** Tension pneumothorax is a clinical diagnosis: absent breath sounds, hyper-resonance, distress, hypotension and a stiff chest to ventilate (falling compliance). It is decompressed at once, without an X-ray (needle in the 4th/5th intercostal space just anterior to the mid-axillary line in adults, or a finger thoracostomy), followed by a chest tube. Massive haemothorax (over 1,500 mL on insertion, or about 200 mL an hour for 2–4 hours) means thoracotomy. An open pneumothorax gets a dressing taped on three sides, then a tube away from the wound."),
  ],
  table=dict(title="Traumatic arrest and penetrating chest injury", head=["Situation", "Action"], rows=[
    ["Penetrating injury in the ‘box’ with shock", "**pericardial ultrasound first**; tamponade → thoracotomy"],
    ["Penetrating chest, Beck’s triad, globular heart", "tamponade: pericardiocentesis as the bedside step; **definitive care is surgical**"],
    ["Penetrating thoracic arrest with signs of life", "**resuscitative thoracotomy** (EAST: strong recommendation)"],
    ["Blunt arrest, asystole, over 10 min CPR, no cardiac motion on POCUS", "**stop**; thoracotomy not recommended"],
  ]),
  mimic=[
    ("Tension pneumothorax vs massive haemothorax", "Both: absent breath sounds and shock. Tension: hyper-resonant, distended neck veins. Haemothorax: dull to percussion, flat neck veins."),
    ("Tension pneumothorax vs tamponade", "Both: shock and distended neck veins. Tension: one side silent and hyper-resonant. Tamponade: both sides normal, muffled heart sounds."),
  ],
  traps=[
    ("“Cervical spine examination is part of the primary survey”", "The spine is protected during A (manual in-line stabilisation, collar) but examined in the secondary survey; exsanguinating haemorrhage (x), breathing (B) and GCS (D) are all primary-survey items."),
    ("“Shocked, quiet right chest, compromised airway, unstable pelvis: insert a 32F chest tube first” [NEET 2025]", "With no distended neck veins or crepitus the chest is not a tension pneumothorax, and the airway is compromised: A comes before B, so intubate with in-line stabilisation first."),
    ("“Advanced airway first, then suction and basic manoeuvres”", "Escalate in order: suction, jaw thrust, adjunct, tube, surgical airway."),
    ("“Flail chest: the main insult is the contusion, so put in a chest tube”", "A chest tube treats air or blood in the pleura, not a contusion. The pair that matches is abnormal chest wall mechanics with epidural analgesia [NEET 2025]."),
    ("“Tamponade after a gunshot: the definitive treatment is pericardiocentesis”", "Keyed so because surgery was not offered; in trauma the clot often cannot be aspirated and the injury needs repair by thoracotomy or sternotomy."),
    ("“Blunt arrest with 10 minutes of asystole: open the chest”", "No cardiac activity on ultrasound after more than 10 minutes of CPR in blunt trauma means stop."),
  ],
  decode=[
    ("Head injury: eyes open to pain, moaning, withdraws to pain, vitals normal — next step? [DocT GT; NEET 2025]", "GCS 8 (E2 V2 M4): prepare for intubation (94% right). Not suturing, mannitol or burr holes."),
    ("Shocked polytrauma: airway compromised, diminished right breath sounds without JVD, unstable pelvis, blood at the meatus — next step? [NEET 2025]", "Intubation with in-line cervical stabilisation; airway before chest tube, DPL or burr holes."),
    ("Sequence of airway management with cervical spine control [NEET 2025]", "Suction → jaw thrust/chin lift → OPA/NPA → cuffed tube ± RSI or surgical airway."),
    ("Stab in the mediastinal ‘box’ with shock; gunshot to the left chest with Beck’s triad; decreased breath sounds and poor compliance [DocT GT; NEET 2025]", "Pericardial ultrasound then thoracotomy (91%); tamponade → pericardiocentesis as offered; tension pneumothorax → needle decompression."),
  ],
  extra=[
    dict(q="Hanging, stridor, two failed intubations, SpO₂ falling: next? [Marrow]", a="Cricothyroidotomy (scalpel technique, DAS Plan D)."),
  ],
  punch="The airway comes first unless a limb is exsanguinating: a GCS of 8 or a compromised airway means intubation with in-line stabilisation before the chest tube. Tension pneumothorax is decompressed on clinical signs, without waiting for an X-ray.",
)

L['POLY-08'] = dict(
  sub="Trauma → Primary survey → Circulation, disability, exposure and adjuncts",
  step=5,
  intro="Still in step 5: C, D and E, and the tests done alongside them. Two questions link here: one asks which item is not part of the primary survey, the other which structure FAST does not image. Both test the limits of a fast examination: what it is meant to find and what it cannot.",
  parts=[
    ('a', "**C: hypotension after injury = bleeding until proven otherwise; palpable radial pulse ≈ SBP 70 (your notes), carotid ≈ 60; find the source (eFAST, CT angiography); large-bore IV; blood gas and Hb at the bedside.** Blood is lost into five places: externally, the chest, the abdomen, the pelvis and retroperitoneum, and long-bone fractures. The chest X-ray, pelvic X-ray and eFAST search three of them in minutes. The traditional ATLS teaching is radial 80, femoral 70, carotid 60 mmHg; a study of hypovolaemic patients (Deakin and Low, BMJ 2000) showed these overestimate the true pressure, so a palpable radial pulse does not prove a safe pressure. An early haemoglobin can be normal because the blood lost has not yet been replaced by fluid; the base deficit and lactate are better early markers."),
    ('b', "**D: GCS (mild 13–14 in notes, standard 13–15; moderate 9–12; severe 8 or less); pupils (one dilated = ipsilateral herniation; both = brainstem herniation, toxins, hypotension); lateralising signs; spinal level.** The standard classification is mild 13–15. The GCS-Pupils score subtracts the number of unreactive pupils (0, 1 or 2) from the GCS, giving a range of 1–15, because pupil reactivity adds prognostic information that the GCS lacks. A unilateral dilated pupil usually lies on the side of the mass lesion (uncal herniation compressing the third nerve)."),
    ('c', "**E: undress fully; prevent hypothermia.** Hypothermia impairs clotting enzymes and platelets and joins acidosis and coagulopathy in the lethal triad; many authors now add hypocalcaemia (the ‘lethal diamond’), because citrate in transfused blood binds calcium and low ionised calcium impairs clotting and contractility. Warm the room, fluids and blood."),
    ('d', "**Adjuncts: ECG, SpO₂, capnography, ABG, urinary and gastric catheters, chest X-ray, eFAST, DPL.** FAST looks for free fluid in four windows: pericardial (subxiphoid), right upper quadrant (Morison’s pouch), left upper quadrant (splenorenal) and pelvis; eFAST adds both anterior chests for pneumothorax. It does not image the brain, the retroperitoneum (pancreas, kidneys) or hollow-viscus injury, and it needs roughly 100–250 mL of fluid to become positive. In blunt trauma a Cochrane review found a sensitivity of about 74–78% and a specificity of 96–97%: a positive scan in a shocked patient sends him to theatre, but a negative scan does not exclude injury. No urinary catheter before a urethrogram if there is blood at the meatus; the gastric tube goes by mouth if a basal skull fracture is possible."),
    ('e', "**Secondary survey: AMPLE history, head-to-toe, trauma CT.** It begins only when the primary survey is complete and the patient is responding. A tertiary survey (repeat full examination and review of all imaging, usually within 24 hours and when the patient is awake) finds injuries missed by the first two, in about 4% of patients in a systematic review."),
  ],
  mimic=[
    ("FAST vs eFAST", "FAST: four windows for free fluid. eFAST: the same plus both pleural spaces for pneumothorax and haemothorax."),
    ("FAST vs DPL", "Both look for intraperitoneal blood; FAST is non-invasive and repeatable, DPL is more sensitive but invasive and misses the retroperitoneum."),
  ],
  traps=[
    ("“FAST can assess the brain” or “FAST excludes pancreatic and renal injury”", "FAST has four windows for free fluid; it sees neither the brain nor the retroperitoneum."),
    ("“A negative FAST rules out abdominal injury”", "Sensitivity is only about 75%; a stable patient with a negative scan still needs CT if injury is suspected."),
    ("“A palpable radial pulse means SBP is at least 80”", "The pulse rule overestimates pressure in hypovolaemia."),
  ],
  decode=[
    ("Which structure is NOT assessed in a standard FAST: heart, liver–kidney interface, brain, spleen–kidney interface? [DocT PYQ]", "Brain."),
    ("Primary survey includes all except: breathing, exsanguinating haemorrhage, cervical spine examination, GCS [DocT GT]", "Cervical spine examination (protected in A, examined in the secondary survey)."),
  ],
  punch="Shock after injury is bleeding until proven otherwise, and the source is searched in five places. FAST sees free fluid in four windows, not the brain or the retroperitoneum, and a negative scan does not exclude injury.",
)

L['POLY-09'] = dict(
  sub="Trauma → Shock → ATLS classes of haemorrhagic shock",
  step=6,
  intro="Step 6 grades the shock. The ATLS classes match a fraction of lost blood volume (about 70 mL/kg, roughly 5 L in a 70 kg adult) to the signs it produces. The four real questions all land on class III, and the cohort did worst (57%) when it had to convert that class into millilitres. The key physiological point: pressure holds until about 30% has gone, so a normal pressure does not mean a normal volume.",
  parts=[
    ('a', "**Blood loss: I under 15% (750 mL); II 15–30% (750–1,500); III 30–40% (1,500–2,000); IV over 40% (2,000+).** Loss up to 15% is covered by venoconstriction. Between 15 and 30% arterial constriction raises the diastolic pressure and holds the systolic; beyond 30% compensation fails."),
    ('b', "**Pulse: I under 100; II 100–120; III 120–140; IV over 140.** Tachycardia is the earliest sign, but it is blunted by beta-blockers, pacemakers, fitness and old age, and in one large series about 29% of hypotensive trauma patients had a relative bradycardia, probably vagal; so a normal pulse does not exclude major loss."),
    ('c', "**BP: I normal; II normal; III falls; IV low.** The first fall in systolic pressure marks class III, about 30% loss. That is why hypotension is a late sign and why a hypotensive trauma patient has already lost 1.5 L."),
    ('d', "**Pulse pressure: I normal or wide; II narrow; III narrow; IV narrow.** In class II the diastolic rises with vasoconstriction while the systolic holds, so the narrowed pulse pressure is the only change in the pressure."),
    ('e', "**RR: I 14–20; II 20–30; III 30–40; IV over 35.** Breathing rises with the metabolic acidosis. (The original table overlaps between III and IV.)"),
    ('f', "**Urine (mL/h): I over 30; II 20–30; III 5–15; IV negligible.** Urine of 5–15 mL an hour is class III."),
    ('g', "**Mind: I slightly anxious; II mildly anxious; III anxious, confused; IV confused, lethargic.** Confusion appears with cerebral hypoperfusion in class III."),
  ],
  table=dict(title="Response to the first fluid or blood (ATLS)", head=["Response", "Estimated loss", "Meaning and action"], rows=[
    ["Rapid responder", "minimal: under 15% (10th ed.); under 20% in older editions", "bleeding stopped; type-specific blood on standby"],
    ["**Transient responder**", "**about 15–40% (10th ed.; 20–40% earlier), ongoing**", "**still bleeding: blood products, MTP, source control**"],
    ["Minimal or no response", "over 40%", "immediate transfusion and surgery; consider non-haemorrhagic shock"],
  ]),
  mimic=[
    ("Class II vs class III", "Class II: pulse up to 120, systolic normal, pulse pressure narrow, mind normal. Class III: systolic falls, urine 5–15 mL/h, confusion."),
    ("Haemorrhagic vs neurogenic shock", "Haemorrhage: tachycardia, cold and pale. Cord injury at T6 or above: hypotension with bradycardia and warm skin (POLY-10)."),
  ],
  traps=[
    ("“SBP 75, urine 10 mL/h, restless: 2,000–3,000 mL lost”", "That is class III, 1,500–2,000 mL (30–40%); only 57% chose it on DocT GT."),
    ("“HR 120, BP 80/60, confused, base deficit −8: class II”", "The fall in systolic pressure and confusion put it in class III, and the base deficit of −6 to −10 agrees (72% right)."),
    ("“Transient responder: start vasopressors”", "Transient response means ongoing bleeding; give blood and find the source. Vasopressors do not replace volume."),
  ],
  decode=[
    ("Gunshot to the leg, tourniquet, HR 120, BP 80/60, confused, base deficit −8 — class? [DocT GT]", "Class III (72%)."),
    ("Postpartum bleeding, SBP 75, restless, urine 10 mL in an hour — volume lost? [DocT GT]", "1,500–2,000 mL (57%)."),
    ("Road accident, anxious and confused, pulse 130, RR 30, urine 10 mL/h — class? [NEET 2025]", "Class III."),
    ("Postpartum bleed, BP improves after 1 L then falls within 15 minutes, HR rising — next? [DocT GT]", "Transient responder: continue resuscitation and transfuse (93%)."),
  ],
  punch="Systolic pressure first falls in class III, at about 30% loss, around 1,500–2,000 mL in an adult. A transient responder is still bleeding and needs blood and source control, not vasopressors.",
)

L['POLY-10'] = dict(
  sub="Trauma → Resuscitation → Circulation before airway",
  step=6,
  intro="Still in step 6: what to do once shock is recognised, and why the order changes. Induction drugs and positive pressure remove the vascular tone and venous return that keep a bleeding patient alive, so intubating before filling the circulation can cause arrest. The five questions test the shock index, the reduced induction dose, and neurogenic shock, where only 28% chose the key.",
  parts=[
    ('a', "**Control massive external bleeding first (step 1 of 5).** Tourniquet, wound packing or a junctional device before anything else: this is the ‘x’ of xABCDE, now formal in the 11th ATLS edition. It applies to catastrophic external bleeding; an obstructed airway still comes first. (2) **Basic airway manoeuvres; intubate immediately only for dangerous hypoxia or a dynamic airway injury.** Oxygen and basic manoeuvres buy minutes while the circulation is filled. An expanding neck haematoma, an inhalational burn or a failing airway cannot wait. (3) **Look for occult shock: SBP under 110, shock index over 1 (HR ÷ SBP), flat IVC with bleeding, lactate over 4 or base deficit over 6, loss of central pulses, cold limbs.** The shock index is heart rate divided by systolic pressure; normal is 0.5–0.7. It rises while the pressure is still ‘acceptable’, because the pulse climbs before the pressure falls. A pulse of 128 with a pressure of 105 gives 1.2, which is occult hypovolaemia even with normal mentation, a lactate of 1.8 and a capillary refill of 2 seconds. (4) **Shock: blood products and TXA, bind the pelvis, decompress the chest, treat tamponade; vasopressors if neurogenic shock.** Crystalloid only as a short bridge (the 11th edition minimises it), then balanced components (1:1:1) or whole blood, with tranexamic acid within 3 hours of injury (1 g over 10 minutes, then 1 g over 8 hours). Neurogenic shock follows cord injury at T6 or above: hypotension with bradycardia and warm peripheries. Other causes of shock must still be excluded first, spinal precautions kept, and the whole spine imaged when the sensory level is thoracic. After volume, noradrenaline is commonly preferred because its β₁ effect supports the heart rate as well as the tone; the pure α-agonist phenylephrine can cause reflex bradycardia and worsen it. No guideline names a single agent of choice. MAP targets: 85–90 mmHg for 7 days in the 2013 AANS/CNS guideline; the 2024 AO Spine guideline suggests at least 75–80 and not above 90–95 for 3–7 days. (5) **Then intubate with 25–50% of the usual induction dose and a full paralytic dose; watch for peri-intubation collapse.** In any shock, septic as well as haemorrhagic, the circulation is slow and the central volume small, so a normal dose reaches the brain and heart at high concentration and abolishes the sympathetic tone that holds the pressure. The paralytic dose is not reduced (and may be increased), because slow circulation delays its onset. Ketamine is not automatically safe: in a catecholamine-depleted patient it can still drop the pressure. Etomidate is not ‘strictly avoided’; the mortality effect of a single dose is unproven."),
  ],
  mimic=[
    ("Shock index vs systolic pressure alone", "HR 128, SBP 105: pressure looks acceptable, the index is 1.2."),
    ("Neurogenic vs spinal shock", "Neurogenic shock is haemodynamic (hypotension, bradycardia). Spinal shock is neurological: temporary loss of reflexes below the lesion."),
  ],
  traps=[
    ("“Shock index = HR × SBP”", "It is HR ÷ SBP (66% right on DocT)."),
    ("“Neurogenic shock with a mid-chest sensory level: CT head and neck”", "That is the wrong (‘except’) option: a thoracic level needs imaging of the whole spine. Only 28% chose it; the others are all correct steps."),
    ("“Phenylephrine is the pressor of choice in neurogenic shock”", "This is the Marrow key, but noradrenaline is usually preferred because phenylephrine can worsen bradycardia; choose phenylephrine only when the stem has no bradycardia and noradrenaline is not offered."),
    ("“Etomidate must be avoided in septic shock”", "Not proven; the correct statement is to reduce the induction dose to about a quarter to a half."),
  ],
  decode=[
    ("Shock index is defined as: HR × SBP, SV × SBP, HR/SBP, SV/SBP [DocT QBank]", "HR/SBP (66%)."),
    ("HR 128, SBP 105, normal mentation — which parameter most suggests occult hypovolaemia? [DocT GT]", "Shock index 1.2."),
    ("Fall from a balcony, HR 50, BP 80/40, mid-chest sensory level — all are appropriate EXCEPT? [DocT GT]", "CT of only the head and neck (28%)."),
    ("Septic shock on noradrenaline, RSI planned — most accurate statement? [DocT GT]", "Reduce the induction dose to 1/4–1/2."),
  ],
  extra=[
    dict(q="Cervical cord injury, MAP under 60, HR 74: best pressor? [Marrow]", a="Marrow keys phenylephrine (pure α₁) because the heart rate is not low; noradrenaline is preferred in practice and whenever there is bradycardia."),
  ],
  punch="Stop the external bleeding, fill the circulation with blood and TXA, then intubate with a quarter to half the induction dose. A shock index over 1 means occult shock while the pressure still looks acceptable.",
)

FLAGS = {
  'POLY-01': "a: ‘over 5 million deaths a year’ is the older WHO figure; the current WHO fact sheet gives about 4.4 million (nearly 8% of deaths), with injuries 3 of the top 5 causes of death at 5–29 years (the card says 15–29).",
  'POLY-04': "Range: an injured patient’s ISS is 1–75 (0 only with no injury); the card’s 0–75 is acceptable but most references write 1–75.",
  'POLY-05': "b: EMTRAS (age, GCS, base excess, prothrombin time, each 0–3) confirmed; the ‘over 8 = high mortality’ cut-off could not be traced to the source paper.",
  'POLY-06': "Watch line uses ‘primary/secondary injury’ in the general sense (mechanical vs the physiological insult that follows); in blast injury ‘secondary’ means fragment injury. Explained to avoid confusion.",
  'POLY-08': "a: ‘radial ≈ SBP 70’ in the notes differs from the traditional ATLS teaching (radial 80, femoral 70, carotid 60), and all overestimate (the watch line already says so). d: ‘mild 13–14’ is non-standard; mild TBI is GCS 13–15.",
  'POLY-09': "The card prints the older numeric ATLS table (8th/9th editions). The 10th edition replaced the numbers with direction arrows and added base deficit (0 to −2, −2 to −6, −6 to −10, ≤−10) and need for blood products; I could not open the 11th-edition table. The RR rows overlap (III 30–40, IV over 35), inherited from the original table. Responder bands (explanation table, not on the card): 10th edition rapid <15%, transient 15–40%, none >40%; the DocT explanation’s <20% / 20–40% are the 9th-edition bands.",
  'POLY-10': "d: Marrow keys phenylephrine for neurogenic shock (qbank fix cross-note); noradrenaline is preferred, especially with bradycardia. MAP target differs between AANS/CNS 2013 (85–90 for 7 days) and AO Spine 2024 (≥75–80, ≤90–95, 3–7 days). a: xABCDE puts catastrophic external bleeding first, but an obstructed airway still comes first (NEET 2025 stem).",
}
