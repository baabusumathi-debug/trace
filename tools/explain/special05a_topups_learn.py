# SPECIAL05A top-up cards — Explain v3 ("Learn" depth), same fields and voice as special05a_learn.py.
# Fields: sub, step (index into special05a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source questions: trace/test/data/qbank.json topups["SPECIAL05A"] (src lists) with stems and keys from map/doct_gt_distinct_all.jsonl and map/out/all_rows.json.
# CGT papers record cohort 0% where no data exist; those percentages are not quoted.
# Checked online 13 Nov 2026: Gurd criteria reproduction (minor: tachycardia >110, pyrexia >38.5 °C; 1 major + 4 minor); NEXUS low-risk criteria and the Canadian C-spine rule
# (Stiell 2003: 99.4% vs 90.7%; CCR high-risk age ≥65, dangerous mechanism, paraesthesia; low-risk criteria; rotation 45°); EAST 2015 thoracotomy; Cochrane FAST accuracy.
# Review 13 Nov 2026 re-checked: Gurd & Wilson >110, Stiell 2003, EAST 2012 BCI, STASCIS, retrograde cystogram ≥300 mL, IO flow (Ong 2009/BestBETs), MSD BTAI targets.
# From memory, not reopened: AAST grading, WSES/EAST NOM success rates, EAST 2012 blunt cardiac injury guideline, EAST 2015 BTAI (TEVAR, anti-impulse), Denis three-column model,
# STASCIS (Fehlings 2012), CT pancreatic sensitivity (DocT explanation gives 47–79%), AUA/EAU retrograde cystography volume (≥300–350 mL), ESVS permissive hypotension in rAAA,
# IO flow rates, Levine–Edwards and transverse-ligament rules for C2/C1 stability.

T = {}

T['T_0ef120e7'] = dict(
  sub="Trauma → Abdomen → Blunt abdominal trauma: operate, embolise or watch",
  step=5,
  intro="Step 5 found the bleeding; this card decides what to do with an abdominal source. The rule underneath all seven bank questions is that physiology, not the CT grade, decides between theatre and non-operative care, and that FAST and CT each have blind spots (air, bowel, pancreas) that the stems are built around. Every one of the seven was answered poorly (27–56% where recorded).",
  parts=[
    ('a', "**Unstable or peritonitis → laparotomy.** A patient who does not respond to resuscitation, or has peritonism, has bleeding or contamination that only surgery will control; CT in an unstable patient wastes time."),
    ('b', "**Stable or transient responder with solid-organ injury, any grade (e.g. grade III spleen or liver with a blush) → non-operative in ICU/HDU + IR angioembolisation; NOM succeeds in over 80–90%; avoid large crystalloid boluses; vaccinate after splenectomy or major splenic embolisation.** Most liver and spleen injuries stop bleeding on their own, and the grade does not exclude non-operative care if the patient is stable. A contrast blush means active arterial bleeding, which is the indication for embolisation, because observation alone fails more often when a blush is present. Non-operative care is only safe in a monitored bed with IR, theatre and blood available. Large crystalloid volumes are not given ‘prophylactically’; they dilute clotting and raise the pressure against a fresh clot. Liver function tests do not guide management."),
    ('c', "**Free air on CT, or seat-belt sign + free fluid without solid-organ injury, bowel wall thickening or mesenteric haematoma → hollow-viscus injury → laparoscopy if stable / laparotomy (FAST sees fluid, not air, and misses it).** Free fluid with no solid-organ source means the fluid came from somewhere else, usually bowel or mesentery crushed against the spine by a lap belt. A negative FAST does not exclude it, and neither does the absence of free air. Repeating FAST or admitting for observation with morphine delays a perforation."),
    ('d', "**Pancreas: FAST misses, early CT 50–80% sensitive, amylase unreliable; duct status decides → MRCP, ERCP diagnostic AND therapeutic; body/tail duct disruption → distal pancreatectomy.** The pancreas lies in the retroperitoneum, invisible to FAST, and early CT misses many injuries. An amylase can be normal with an injury and raised without one. What decides treatment is whether the main duct is broken, and ERCP both shows the duct and lets it be stented."),
    ('e', "**Day 3–10 after liver NOM: fever, RUQ pain, rising bilirubin = bile leak/biloma (CT/US collection, HIDA confirms) → percutaneous drainage ± ERCP stent; falling Hb = delayed bleed; GI bleed + RUQ pain + jaundice = haemobilia → embolise.** Bile leaking from a torn duct collects and becomes infected over days, so fever with a rising bilirubin points to biloma. Haemobilia is an arterial–biliary fistula bleeding into the gut (Quincke’s triad)."),
  ],
  table=dict(title="Who goes where", head=["Patient", "Decision"], rows=[
    ["Unstable, non-responder, or peritonitis", "**laparotomy**"],
    ["Stable, solid organ any grade, blush", "**NOM in ICU + angioembolisation**"],
    ["Stable, solid organ, no blush", "NOM, serial examination and Hb"],
    ["Free air, or free fluid without solid injury + tender", "**laparoscopy (stable) or laparotomy**"],
  ]),
  mimic=[
    ("Biloma vs delayed haemorrhage vs haemobilia", "Biloma: fever, pain, rising bilirubin at day 3–10. Delayed bleed: falling Hb, shock. Haemobilia: GI bleeding with RUQ pain and jaundice."),
  ],
  traps=[
    ("“Grade IV spleen: splenectomy”", "Grade does not decide; this patient (HR 102, BP 90/60, conscious) was keyed for embolisation (27% right). If he were a non-responder, laparotomy would be right."),
    ("“Grade III with a blush: NOM with bed rest and serial Hb only”", "A blush is active bleeding; observation alone fails more often, so embolise."),
    ("“Pneumoperitoneum in a stable patient: CT angiography” or ‘laparotomy only’", "Free air needs operative exploration; laparoscopy or laparotomy are both acceptable (keyed ‘A or C’, 38% right)."),
    ("“CT detects over 95% of pancreatic injuries” or “normal amylase rules it out”", "Early CT sensitivity is only about 50–80% and amylase is unreliable (39% right)."),
    ("“Seat-belt sign, mesenteric haematoma, free fluid, negative FAST: admit and observe”", "Persistent tenderness with fluid and no solid-organ injury is hollow-viscus injury: laparotomy (56%)."),
  ],
  decode=[
    ("Seat-belt bruise, FAST negative, CT: no solid injury, free fluid, mesenteric haematoma, persistent pain [DocT GT]", "Surgical consultation and laparotomy."),
    ("Stable, grade III liver laceration with a small blush [DocT GT]", "Admit to surgical ICU with IR consultation (55%)."),
    ("Five days after liver NOM: fever, pain, rising bilirubin [DocT GT]", "Biloma (50%)."),
    ("Stable pancreatic trauma: which statement is true? [DocT GT]", "ERCP is both diagnostic and therapeutic."),
  ],
  punch="Physiology decides, not the CT grade: unstable or peritonitic goes to theatre, a stable solid-organ injury is watched in ICU and embolised if there is a blush. Free air, or fluid without a solid-organ source, is bowel until proven otherwise.",
)

T['T_dc8269d6'] = dict(
  sub="Trauma → Complications → Fat embolism syndrome",
  step=4,
  intro="Step 4 linked mechanism to injury; a long-bone or pelvic fracture predicts this delayed complication. Fat from the marrow enters the circulation, blocks capillaries and then triggers an inflammatory reaction, which explains both the delay of a day or more and the three organs affected. Five bank questions test two things: which features are major Gurd criteria, and that treatment is supportive with early fixation.",
  parts=[
    ('a', "**24–72 h after long-bone or pelvic fracture (also IM nailing, liposuction, sickle crisis).** The delay reflects the time it takes fat globules to be broken down to free fatty acids that injure the endothelium. Intramedullary reaming forces more marrow into the veins."),
    ('b', "**Gurd MAJOR: respiratory insufficiency, cerebral signs, petechial rash (non-dependent; only about 1/3).** The lung is the first capillary bed reached; fat passing through it (or through a patent foramen ovale) reaches the brain and skin. The rash appears on the upper chest, axillae, neck and conjunctivae, and is present in only about a third of patients."),
    ('c', "**MINOR: tachycardia over 120, fever, retinal changes, jaundice, renal change, fall in Hb or platelets, high ESR, fat macroglobulinaemia; need 1 major + 4 minor.** Tachycardia and retinal changes are the two minor criteria that bank questions offer as ‘major’. Gurd and Wilson’s criteria set the tachycardia threshold at over 110 a minute and fever at over 38.5 °C."),
    ('d', "**Clinical diagnosis: CT chest non-specific (ground glass), MRI brain ‘starfield’ DWI; fat in urine or BAL supportive only.** No test confirms FES; imaging and laboratory tests are done to exclude other causes (missed head injury, pneumothorax, pulmonary embolism). The MRI pattern of many small diffusion-restricting dots supports it."),
    ('e', "**Supportive care (O₂/ventilation, haemodynamics); early fracture fixation (24 h or less) limits further embolisation; no proven role for steroids, heparin or IVC filters.** Lung-protective ventilation for the ARDS-like picture. A filter cannot catch fat, heparin does not dissolve it, and steroids have no outcome evidence as treatment."),
  ],
  mimic=[
    ("FES vs pulmonary embolism", "FES: 24–72 h after fracture, with confusion and petechiae. PE: later, usually without rash or encephalopathy, and a filling defect on CT angiography."),
  ],
  traps=[
    ("“Tachycardia is a major Gurd criterion”", "It is minor (47% right on DocT GT)."),
    ("“Retinal changes are a major criterion”", "Minor (Marrow, asked twice)."),
    ("“Diagnosis is made with CT of the chest”", "That was the false statement: FES is a clinical diagnosis of exclusion (69% right)."),
    ("“Give steroids or heparin, or place an IVC filter”", "None is proven; treatment is supportive with early fixation."),
  ],
  decode=[
    ("ORIF of femur, sudden tachycardia, hypotension, hypoxia — all are major Gurd criteria EXCEPT [DocT GT]", "Tachycardia."),
    ("Day 1 after femoral fixation: confusion, dyspnoea, petechiae on neck and trunk — all true EXCEPT [DocT GT]", "‘Diagnosis is made with CT of the chest’."),
    ("Bilateral femur fractures, day 2, confusion, petechiae, P/F 150 — management? [DocT GT]", "Supportive care with early operative fixation."),
  ],
  punch="Fat embolism is hypoxia, confusion and a non-dependent petechial rash 24–72 hours after a long-bone fracture; it is diagnosed clinically and treated by support and early fixation, and tachycardia and retinal changes are minor criteria.",
)

T['T_bb4f16eb'] = dict(
  sub="Trauma → Chest → Blunt aortic injury, blunt cardiac injury and posterior sternoclavicular dislocation",
  step=4,
  intro="Step 4 predicted injuries from the mechanism; rapid deceleration (a fall, a frontal crash) predicts injury to the structures in the mediastinum. The five bank questions test the imaging choice and the CXR signs of aortic injury, and who can be cleared of cardiac injury. The cohort did badly on both: 36% on the imaging question and 27% on cardiac clearance.",
  parts=[
    ('a', "**Aorta: deceleration tear at the isthmus. CXR clues: mediastinum over 8 cm, lost aortic knob, apical cap, left haemothorax, trachea/NG deviated RIGHT, LEFT main bronchus depressed, 1st/2nd rib fracture; a normal CXR does not exclude → CT angiography (not TTE/TEE).** The isthmus, just beyond the left subclavian, is where the mobile arch meets the descending aorta fixed by the ligamentum arteriosum, so shear concentrates there. The haematoma lies to the left of the trachea and above the left main bronchus, so it pushes the trachea and NG tube to the right and the left bronchus down. No CXR finding is sensitive enough on its own, so a normal film does not exclude injury after a major deceleration. CT angiography is the test; TOE needs sedation and a cleared spine and misses parts of the arch."),
    ('b', "**Aortic treatment: anti-impulse (HR under 100, SBP under 100) + TEVAR; minimal intimal injury observed.** A beta-blocker first (esmolol), then a vasodilator if needed, lowers the shear on the torn wall until it is repaired; many sources set tighter targets than the card, a heart rate of about 60–80 and a systolic pressure of 100 mmHg or less. Endovascular repair has replaced open repair because it has lower mortality and less paraplegia."),
    ('c', "**Blunt cardiac injury: screen all with ECG + troponin I; both normal → ruled out, no telemetry (EAST); abnormal → monitor 24–48 h, echo if hypotension or arrhythmia; sternal fracture alone does not predict BCI.** The danger of a cardiac contusion is arrhythmia, which usually announces itself with an abnormal admission ECG; EAST recommends an ECG for every patient in whom blunt cardiac injury is suspected, and troponin I routinely. EAST (2012) states that a normal ECG with a normal troponin I rules out blunt cardiac injury, so no serial testing or telemetry is needed; a normal ECG with a raised troponin still needs a monitored bed, and echocardiography is for haemodynamic instability or a persistent new arrhythmia."),
    ('d', "**Posterior SC dislocation threatens great vessels, trachea, oesophagus → CXR + CT angiography, reduction with CT-surgery backup.** The medial clavicle displaced backwards lies against the brachiocephalic vessels and trachea; a missing medial clavicle prominence after a steering-wheel or shoulder impact is the clue."),
  ],
  mimic=[
    ("Aortic injury vs other causes of a wide mediastinum", "A supine AP film widens any mediastinum; the specific signs are a lost aortic knob, rightward tracheal or NG deviation, and a depressed LEFT bronchus."),
  ],
  traps=[
    ("“Definitive evaluation of BTAI is with TTE or TEE”", "That was the false statement; CT angiography is the test (36% right)."),
    ("“Depression of the right main bronchus suggests aortic injury”", "The left main bronchus is depressed; ‘right’ was the false statement."),
    ("“Normal ECG and troponin I at 8 h: start serial troponins or 72-h telemetry”", "Both normal rules out blunt cardiac injury: discharge (27% right)."),
    ("“A sternal fracture means cardiac contusion”", "A sternal fracture alone does not predict BCI."),
  ],
  decode=[
    ("Fall from 20 ft, widened mediastinum — all true about BTAI EXCEPT [DocT GT]", "‘TTE or TEE for definitive evaluation’."),
    ("Blunt chest trauma, normal ECG, troponin I under 1.5 ng/mL at 8 h — next? [DocT GT]", "Discharge with follow-up."),
    ("Stable BCI with abnormal ECG and raised troponin — plan? [Marrow]", "Serial ECG and troponin with echocardiography."),
    ("Unrestrained driver, medial clavicle deformity, SC joint not felt — management? [Marrow]", "Chest X-ray then CT angiography."),
  ],
  punch="Deceleration tears the aorta at the isthmus: the haematoma pushes the trachea right and the left bronchus down, CT angiography confirms, and TEVAR follows anti-impulse control. A normal ECG and troponin together rule out blunt cardiac injury.",
)

T['T_d82a3b56'] = dict(
  sub="Trauma → Spine → Incomplete spinal cord syndromes",
  step=5,
  intro="Step 5 examined the spinal level under D. The incomplete cord syndromes follow from where the three main tracts run: the corticospinal tract (motor) and dorsal columns (proprioception, vibration) stay on the same side until the brainstem, while the spinothalamic tract (pain, temperature) crosses within a segment or two of entry. Which modality is lost on which side therefore locates the lesion.",
  parts=[
    ('a', "**Brown-Séquard (hemisection, stab): ipsilateral motor and proprioception loss, contralateral pain/temperature loss; best prognosis.** Cutting one half of the cord takes the uncrossed motor and dorsal-column fibres of that side and the already-crossed spinothalamic fibres from the other side."),
    ('b', "**Central cord (elderly, hyperextension on spondylosis): arms more than legs (arm fibres medial), sacral sparing.** The commonest incomplete syndrome. In the cervical cord the fibres for the arms lie nearest the centre, so central damage weakens the arms most; sacral fibres lie outermost and are spared."),
    ('c', "**Anterior cord (flexion injury; anterior spinal artery infarct after thoracic aortic repair): motor and pain/temperature lost, proprioception spared; worst prognosis.** The single anterior spinal artery supplies the front two-thirds; the dorsal columns have their own paired posterior arteries and are spared. After aortic surgery this gives flaccid paraplegia below the level of the infarct, with loss of pain and temperature below it and preserved joint position and vibration sense."),
    ('d', "**Posterior cord: proprioception and vibration lost only.** Rare after trauma; motor power and pain sensation are preserved."),
  ],
  mimic=[
    ("Brown-Séquard vs anterior cord", "Brown-Séquard: losses split between the two sides. Anterior cord: bilateral motor and pain loss with proprioception preserved on both sides."),
  ],
  traps=[
    ("“Post-aortic repair cord infarct: bilateral loss of proprioception”", "That is the posterior pattern; anterior spinal artery infarct spares proprioception. The keyed answer was flaccid paralysis at T8 (54%); its wording ‘complete loss of sensory function’ overstates the deficit, since dorsal columns are spared."),
    ("“Central cord affects the legs more than the arms”", "Arms more than legs, because the arm fibres lie centrally."),
  ],
  decode=[
    ("Stab in the back: ipsilateral weakness and proprioception loss, contralateral pain/temperature loss below T8 [DocT GT]", "Brown-Séquard (78%)."),
    ("Elderly fall backwards, arms weaker than legs, sacral sensation preserved [DocT GT]", "Central cord syndrome (83%)."),
    ("Most likely finding after thoracic aneurysm repair cord infarction [DocT GT]", "Flaccid paraplegia at the level with motor and pain/temperature loss (anterior cord)."),
  ],
  punch="Where the deficit falls locates the lesion: split sides are a hemisection, arms worse than legs is central cord, and motor plus pain loss with preserved proprioception is anterior cord, the worst prognosis.",
)

T['T_eb298c8d'] = dict(
  sub="Trauma → Spine → Column injury: stability and mechanism",
  step=4,
  intro="Step 4 tied mechanism to injury; in the spine the mechanism also predicts stability. Stability means whether the column can hold its shape under normal load without endangering the cord, and the three-column model judges it by how many columns are broken. The three bank questions were each answered by only 34–53%.",
  parts=[
    ('a', "**Three columns: anterior (ALL + front half of body), middle (back half + PLL), posterior (arch, ligaments). Wedge compression = anterior only, stable.** A compression fracture crushes the front of the body under flexion and axial load; the middle column is intact, so the canal is not narrowed and the patient is usually neurologically intact."),
    ('b', "**Burst = anterior + middle (retropulsion can hit the cord); Chance (flexion–distraction, lap belt) = all three, UNSTABLE, with hollow-viscus or mesenteric injury.** In a burst the posterior wall of the body breaks and fragments can be pushed back into the canal. In a Chance fracture the body is folded over a lap belt and the posterior elements are pulled apart, so all three columns fail; the same belt crushes bowel and mesentery (see the blunt abdominal trauma top-up)."),
    ('c', "**Facets: unilateral jump (flexion + rotation, under 50% translation, cord often spared) vs bilateral (flexion + distraction, over 50%, cord injury usual, unstable).** One jumped facet narrows the canal a little; both jumped facets displace the body by half its depth or more and compress the cord."),
    ('d', "**Subluxation = ligamentous instability: in-line immobilisation, CT for bone, MRI for cord, disc, ligament and epidural haematoma; early decompression and fixation (under 24 h, STASCIS).** Displacement of one vertebra on another means the ligaments have failed. CT shows bone; only MRI shows the cord, disc and ligaments. In cervical cord injury, STASCIS (Fehlings 2012) found a 2-grade or greater AIS improvement in 19.8% of patients decompressed within 24 hours against 8.8% decompressed later."),
  ],
  mimic=[
    ("Burst vs wedge compression", "Wedge: front of the body only, posterior wall intact, stable. Burst: posterior wall broken, risk of retropulsion."),
  ],
  traps=[
    ("“Chance fractures are often stable”", "False: all three columns fail (38% right)."),
    ("“Subluxation with anterior displacement: collar and CT are enough”", "Unstable; MRI and early surgery are needed (53% right)."),
    ("“Backward fall onto the head with quadriparesis: hyperextension and rotation”", "DocT keys bilateral jumped facets from hyperflexion–distraction based on the MRI (34% right); the image decides, and without it a backward fall in the elderly suggests central cord."),
  ],
  decode=[
    ("Which is false: compression fracture neurologically intact; Chance with visceral injury; burst affects anterior and middle; Chance often stable [DocT GT]", "‘Chance fractures are often stable’."),
    ("C-spine fracture with subluxation and anterior displacement — management and imaging? [DocT GT]", "Surgery, with MRI for the soft tissues."),
  ],
  punch="Stability depends on the columns: wedge is anterior only and stable, burst adds the middle column, and Chance breaks all three, comes with bowel injury and is unstable. Subluxation means ligament failure, so get an MRI and early fixation.",
)

T['T_702a80b1'] = dict(
  sub="Trauma → Spine → C-spine clearance and C1/C2 fractures",
  step=5,
  intro="Step 5 protected the spine during A; this card is about when that protection can stop without imaging, and about the two upper cervical fractures that are named in stems. Both clearance rules were derived to stop imaging the many alert patients who have no injury without missing the few who do.",
  parts=[
    ('a', "**NEXUS: no imaging if no midline tenderness, normal alertness, not intoxicated, no focal deficit, no distracting injury (Canadian rule adds age 65 or more, dangerous mechanism, rotation 45°).** NEXUS requires all five low-risk criteria. The Canadian C-spine rule works in three steps: any high-risk factor (age 65 or more, dangerous mechanism, limb paraesthesia) → image; no low-risk factor (simple rear-end collision, sitting in the ED, walking since the injury, delayed neck pain, no midline tenderness) → image; otherwise the patient must actively rotate 45° each way. In a head-to-head study (Stiell 2003) the Canadian rule was more sensitive (99.4% vs 90.7%) and more specific (45.1% vs 36.8%)."),
    ('b', "**If imaging: CT (not plain films); MRI for deficit or ligament concern.** CT misses far fewer fractures than plain films; MRI shows cord, disc and ligaments."),
    ('c', "**Hangman’s: bilateral C2 pedicle/pars fractures from hyperextension–distraction; canal widens, cord often spared.** The fracture separates the body of C2 from its arch, which enlarges the canal, so many patients are neurologically intact. Hyperextension–distraction is the judicial-hanging mechanism; road traffic collisions, now the commonest cause, usually add axial loading to the hyperextension."),
    ('d', "**Jefferson: C1 ring burst from axial load (diving); lateral masses overhang C2 on the open-mouth view.** The skull drives the lateral masses of the atlas outwards; the ring breaks in several places."),
    ('e', "**Both unstable: collar, CT/MRI, spinal surgery.** Treat both as unstable until a spinal surgeon has assessed them; stability depends on the displacement in a hangman’s fracture and on whether the transverse ligament has ruptured in a Jefferson fracture."),
  ],
  mimic=[
    ("Hangman’s vs Jefferson", "Hangman’s: C2, hyperextension, cord often spared. Jefferson: C1 ring, axial load."),
    ("NEXUS vs Canadian C-spine rule", "NEXUS: five clinical criteria, any age. Canadian: adds age, mechanism and an active rotation test, and is more sensitive."),
  ],
  traps=[
    ("“Alert, no neck pain, no deficit, sober, no distracting injury: CT or a collar anyway”", "He meets all NEXUS criteria: no imaging (65% right)."),
    ("“Bilateral C2 fracture is a Jefferson fracture”", "Jefferson is C1; bilateral C2 pedicle fractures are hangman’s (63%)."),
  ],
  decode=[
    ("Alert crash victim, no neck pain, no deficit, not intoxicated, no distracting injury — next? [DocT GT]", "No imaging required."),
    ("Head-on collision, bilateral fracture of C2 — name? [DocT GT]", "Hangman’s fracture."),
  ],
  punch="An alert, sober patient with no midline tenderness, deficit or distracting injury needs no imaging under NEXUS; otherwise CT. A hangman’s fracture is bilateral C2 pars from hyperextension, and a Jefferson fracture is a C1 ring burst from axial load.",
)

T['T_403270d5'] = dict(
  sub="Trauma → Chest → Pulmonary contusion and flail chest",
  step=5,
  intro="Step 5 dealt with breathing in the primary survey; this card covers the chest injury that worsens over the following days. Contused lung is bruised parenchyma: blood and plasma fill the alveoli, compliance falls and shunt rises. The flail segment is the visible part, but the contusion beneath it causes most of the hypoxia.",
  parts=[
    ('a', "**Contusion (not the flail) drives hypoxaemia: may be absent on the first CXR, blossoms at 24–72 h, resolves in 5–7 days unless pneumonia or ARDS.** Most contusions are visible on the chest film within about 6 hours, but CT shows them earlier and better, and small ones can be missed on the first film; the bleeding and oedema accumulate over the first day or two, and the shadowing then clears over about a week. A lesion that worsens after that is infection or ARDS."),
    ('b', "**Judicious fluids (colloid NOT better), multimodal/regional analgesia, physiotherapy, HFNC/NIV if alert.** Excess fluid of any kind worsens oxygenation in leaky lung, and no study shows colloid is better than crystalloid. Pain makes the patient splint and retain secretions, so regional analgesia (epidural or paravertebral) and physiotherapy prevent the slide into pneumonia."),
    ('c', "**Distress with SpO₂ about 85%, rising work or shock → intubate, PEEP to recruit, lung-protective volumes.** Non-invasive ventilation suits an alert patient with mild failure; a patient in distress with established contusion needs a tube, and PEEP reopens the flooded alveoli."),
    ('d', "**No prophylactic antibiotics or steroids; rib fixation for selected flail, not first step.** Neither prevents pneumonia or ARDS. Surgical fixation helps selected flail segments but does nothing for the contusion."),
  ],
  mimic=[
    ("Contusion vs ARDS", "Contusion: within hours, at the impact site, resolves in a week. ARDS: bilateral, develops later, lasts longer."),
  ],
  traps=[
    ("“Colloid is preferred over crystalloid in pulmonary contusion”", "That was the false statement; avoid over-resuscitation with any fluid (81% right)."),
    ("“Flail chest, SpO₂ 85%, distress: NIV and morphine” or “an epidural”", "In distress with contusion, intubate and set PEEP; the epidural treats pain, not the contusion (30% right)."),
  ],
  decode=[
    ("Rib fractures with contusions in the SICU — all true EXCEPT [DocT GT]", "‘Colloid is preferred over crystalloid’."),
    ("77-year-old, paradoxical right chest, SpO₂ 85%, HR 122 — next? [DocT GT]", "Intubation with PEEP adjustment."),
  ],
  punch="The contusion under the flail drives the hypoxia, worsens over 24–72 hours and is not helped by colloid; the alert patient gets analgesia and support, and the distressed one is intubated with PEEP.",
)

T['T_25010a36'] = dict(
  sub="Trauma → Genitourinary → Imaging kidney, bladder and urethra",
  step=5,
  intro="Step 5 listed the urinary catheter among the adjuncts; this card is about when it must wait, and which test answers which question. The order follows the anatomy from the outside in: urethra first (before a catheter is passed), then bladder, then kidney. One GT question was answered correctly by only 15%.",
  parts=[
    ('a', "**Blood at the meatus, perineal haematoma, high-riding prostate → retrograde urethrogram BEFORE a Foley.** A catheter pushed blindly through a torn urethra can turn a partial tear into a complete one."),
    ('b', "**Stable with flank pain or haematuria → contrast CT with delayed phase (gold standard for renal injury; not KUB/IVP).** CT grades the parenchymal injury, and the delayed (excretory) phase shows urine leaking from the collecting system."),
    ('c', "**Pelvic fracture + gross haematuria → retrograde CT cystogram (300–350 mL or more by gravity); clamped-catheter passive filling misses ruptures.** A rupture only leaks contrast when the bladder is fully distended. Clamping the catheter and waiting for diluted IV contrast to fill it does not distend it enough, so small tears are missed."),
    ('d', "**Extraperitoneal rupture → catheter 10–14 days; intraperitoneal → surgical repair.** Extraperitoneal leaks (the usual type with pelvic fractures) heal with drainage, unless the bladder neck is involved, bone fragments lie in the bladder, or the rectum or vagina is also injured; those are repaired. Intraperitoneal rupture, from a blow to a full bladder that bursts at the dome, leaks urine into the peritoneum and needs repair."),
  ],
  mimic=[
    ("Intraperitoneal vs extraperitoneal rupture", "Intraperitoneal: blow to a full bladder, dome, contrast outlines bowel, repair. Extraperitoneal: pelvic fracture, contrast in the perivesical tissues, catheter drainage."),
  ],
  traps=[
    ("“IV contrast CT with delayed bladder images after clamping the catheter”", "Passive filling under-distends the bladder; a retrograde CT cystogram is needed (only 15% right)."),
    ("“Retrograde urethrogram” when the catheter passed easily and there was no blood at the meatus", "The urethra is already shown to be intact; the question is the bladder."),
  ],
  decode=[
    ("Side impact, pubic rami fractures, catheter passes easily and drains gross blood, FAST positive splenorenal, stable [DocT GT]", "Contrast CT abdomen and pelvis plus retrograde CT cystogram."),
    ("Flank pain, ecchymosis, haematuria after a bike collision — imaging? [Marrow]", "Contrast-enhanced CT."),
  ],
  punch="Image from the outside in: urethrogram before a catheter if there is blood at the meatus, a retrograde cystogram filled to at least 300 mL for pelvic fracture with haematuria, and contrast CT with a delayed phase for the kidney.",
)

T['T_f27b84e1'] = dict(
  sub="Trauma → Shock → Suspected ruptured abdominal aortic aneurysm",
  step=6,
  intro="Step 6 dealt with shock from bleeding; this is the non-traumatic version that appears in the same bank. An elderly smoker with hypotension and back or flank pain is a ruptured aneurysm until shown otherwise, and the only question is how to confirm it without delaying control.",
  parts=[
    ('a', "**Bedside focused aortic ultrasound, then straight to theatre/EVAR.** Ultrasound in the resuscitation room shows whether an aneurysm is present in minutes; in the right patient that is enough to call the vascular team. A stable patient goes for CT angiography to plan endovascular repair."),
    ('b', "**No CT or departmental ultrasound in an unstable patient; permissive hypotension until control.** Leaving the resuscitation room delays control. Raising the pressure to normal with fluid can blow out the retroperitoneal clot that is containing the leak, so a lower pressure is accepted as long as the patient is conscious."),
  ],
  mimic=[
    ("Ruptured AAA vs renal colic", "Both: flank pain in an older man. Hypotension or a pulsatile mass makes it the aneurysm; never call it colic before the aorta has been scanned."),
  ],
  traps=[
    ("“CT angiography first” in a hypotensive patient", "Only when stable; unstable patients go to theatre after bedside ultrasound."),
  ],
  decode=[
    ("Hypotensive elderly smoker, flank pain, suspected ruptured AAA — next step? [Marrow]", "Focused bedside abdominal ultrasound."),
  ],
  punch="Hypotension with back or flank pain in an older smoker is a ruptured aneurysm: confirm it with bedside ultrasound, keep the pressure low, and go to theatre without stopping for CT.",
)

T['T_8867bce4'] = dict(
  sub="Trauma → Shock → Intraosseous access in haemorrhagic shock",
  step=6,
  intro="Step 6 needs blood going in fast, and vasoconstricted, collapsed veins are the usual obstacle. The marrow cavity drains into the systemic veins and does not collapse, so a needle in it works like a non-collapsible vein. The one bank question was answered correctly by everyone.",
  parts=[
    ('a', "**Intraosseous needle (proximal humerus or tibia): in place in under 1 min, takes blood products and all drugs; humeral flow approaches a 16G line under pressure.** Insertion is quick and needs little skill. Flow is driven by a pressure bag. In patients, humeral and tibial lines under pressure both ran at roughly 150–165 mL/min (Ong 2009), and the evidence that the humerus is faster is inconsistent; this is useful but less than a large-bore peripheral cannula, so the card’s comparison with a 16G line is generous."),
    ('b', "**Then large-bore central access when time allows.** Rapid infusion catheters or central lines give the highest flows for a massive transfusion. The internal jugular is awkward under a collar, so the femoral or subclavian route is usual in trauma."),
    ('c', "**Avoid a fractured bone or a limb distal to a vascular injury.** Fluid would leak out of the fracture or out of the injured vessel instead of reaching the heart."),
  ],
  mimic=[
    ("IO vs central line in shock", "IO: seconds, minimal skill, moderate flow. Central line or rapid infusion catheter: minutes, more skill, highest flow."),
  ],
  traps=[
    ("“After two failed peripheral attempts, attempt a subclavian or IJ line”", "Takes longer and needs more skill; the IJ is hindered by the collar. IO first (100% right)."),
  ],
  decode=[
    ("Polytrauma in haemorrhagic shock, two failed peripheral attempts — next? [DocT GT]", "Insert an intraosseous needle."),
  ],
  punch="When peripheral access fails in shock, put in an intraosseous needle (humerus or tibia) within a minute, avoiding a fractured or vascularly injured limb, and add large-bore central access when time allows.",
)

FLAGS = {
  'T_0ef120e7': "b: ‘stable OR transient responder’ for NOM is broader than most guidance; WSES/EAST reserve NOM for haemodynamically stable or stabilised patients, and a transient responder qualifies only where IR is immediately available. One linked key (GT6 Q129, BP 90/60, HR 102 → embolisation) depends on calling the patient a responder.",
  'T_dc8269d6': "c: Gurd and Wilson give tachycardia over 110 a minute and pyrexia over 38.5 °C (card: over 120). Teaching versions vary (some list pulmonary oedema or hypoxia among the major criteria).",
  'T_bb4f16eb': "b: anti-impulse targets vary; commonly quoted targets are HR 60–80 and SBP ≤100 mmHg (MSD Manual), tighter than the card’s HR under 100. c: EAST 2012 also says a normal ECG with raised troponin I needs a monitored bed; the 24–48 h duration is common practice, not an EAST figure.",
  'T_d82a3b56': "c: in anterior spinal artery infarction the paraplegia is below the level of the lesion, not ‘at’ it. GT2o Q58 keys ‘flaccid paralysis at T8 with complete loss of sensory and motor function’ for anterior spinal artery infarction; strictly the dorsal columns are spared, so the sensory loss is not complete.",
  'T_eb298c8d': "b: in Denis’s scheme a flexion–distraction (Chance) injury fails the middle and posterior columns in tension, with the anterior column sometimes acting as a hinge; ‘all three columns’ is the common teaching shorthand. d: STASCIS studied cervical cord injury only. GT7 Q8 key (bilateral jumped facets, hyperflexion–distraction) depends on an MRI image not seen; the stem’s backward fall in a 65-year-old fits hyperextension central cord better.",
  'T_702a80b1': "c: hyperextension–distraction is the judicial-hanging mechanism; in road collisions hyperextension with axial loading is usual. a: the Canadian rule also has paraesthesia as a high-risk factor and five low-risk criteria before the rotation test. e: ‘both unstable’ is a safe working rule, but a minimally displaced hangman’s fracture (Levine–Edwards type I) and a Jefferson fracture with an intact transverse ligament are stable.",
  'T_403270d5': "a: most contusions are visible on CXR within about 6 h (CT earlier); ‘may be absent on first CXR’ applies to small ones. DocT says they develop over 24–48 h; the card’s 24–72 h is the wider range. Resolution is usually within about a week (often 3–7 days).",
  'T_f27b84e1': "a: ‘straight to theatre/EVAR’ — EVAR normally needs CT angiography for planning; in the unstable patient without CT, open repair or on-table angiography is used.",
  'T_8867bce4': "a: ‘humeral flow approaches a 16G line under pressure’ is overstated: human data give about 150–165 mL/min under pressure for both humeral and tibial sites (Ong 2009), with no consistent humeral advantage (BestBETs); a 16G peripheral cannula flows faster.",
}
