# SPECIAL01 — Explain v3 ("Learn" depth): the brain-dead organ donor — donation in India and the law, preconditions, brainstem reflexes, the apnoea test,
# ancillary tests, certification in India, what brainstem death does to the body, donor targets, pressors, hormones, diabetes insipidus, ventilation, other care,
# contraindications, expanded-criteria donors and cold ischaemia.
# No mnemonics or hooks. Driven by the real questions in qpack/SPECIAL01.md (32 question links; DONOR-03 reflexes asked 10 times, DONOR-05 ancillary tests 6,
# DONOR-02 preconditions and DONOR-04 apnoea test 4 each, DONOR-06 certification and DONOR-07 the dying brainstem 3 each). DONOR-01, 08, 09, 11–15, 17, 18 have no
# linked question and get short explanations with [pattern] decode items.
# No `fix` entries exist for SPECIAL01 in trace/test/data/qbank.json (checked 13 Nov 2026).
# DONOR-04's answer has a line beginning "a T-piece", which check_learn.py reads as part letter a; so DONOR-04 has a single part 'a' covering all five steps.
# Checked online on 13 Nov 2026:
#  - AAN/AAP/CNS/SCCM 2023 BD/DNC guideline (Greer et al., Neurology 2023), via Guideline Central summary, PulmApp and MSD Manual tables: core temperature ≥36 °C;
#    adults SBP ≥100 AND MAP ≥75 mmHg; at least 5 half-lives for CNS depressants (longer with renal/hepatic dysfunction, obesity, prior hypothermia); wait 24 h after
#    rewarming if temperature was ≤35.5 °C; one examination in adults, two exams and two apnoea tests by two clinicians at least 12 h apart in children;
#    apnoea test: baseline PaCO2 35–45 and pH 7.35–7.45, 100% O2 ≥10 min, ABG at 8–10 min, consistent = PaCO2 ≥60 AND ≥20 above baseline with pH <7.30;
#    ECMO: sweep 0.2–1 L/min (or exogenous CO2), VA-ECMO sample both sites, VV-ECMO distal arterial line; ancillary tests accepted: 4-vessel catheter angiography,
#    radionuclide perfusion scintigraphy (SPECT/planar), TCD in adults only; NOT accepted: EEG, evoked potentials, CT angiography, MRI/MRA.
#  - THO (Amendment) Act 2011 text (indiacode.nic.in): tissues added; section 3(1A) required inquiry in ICU and duty to inform the retrieval centre; proviso to 3(6):
#    where no neurologist or neurosurgeon is available, an independent surgeon or physician AND an anaesthetist or intensivist, not on the transplant team.
#  - Indian certification: board of four (RMP in charge of the hospital, independent nominated RMP, neurologist/neurosurgeon, treating RMP), two sets of tests at least
#    6 h apart in adults, Form 10, longer interval in children at the board's discretion (Free Press Journal on the Centre's 2024 advisory; Omnicuris; MOHAN Foundation).
#  - Donation rates 2024: Spain 53.9 pmp, USA 49.7 pmp (Spanish Government/ONT, Aug 2025); India about 0.8 pmp (2024 reports).
#  - Donor management (Ciardi et al., JHLT Open 2025 review, quoting SCCM/ACCP/AOPO 2015, JHLT 2020 and Canadian 2020): MAP >60 (Canada >65); vasopressin 0.01–0.04 U/min;
#    methylprednisolone 15 mg/kg or 1 g or 250 mg then 100 mg/h; low-dose hydrocortisone 300 mg then 100 mg 8-hourly as an alternative; Hb >7 g/dL; glucose <180;
#    Na 130–150 (SCCM) / 135–150 (JHLT) / 135–155 (Canada); desmopressin if normotensive with DI; VT 6–8 mL/kg, PEEP 8–10, PIP <35 (JHLT); temperature 36–37 (JHLT) or
#    34–35 °C if no thoracic organs (Canada); routine levothyroxine shows no benefit in two RCTs.
#  - Levothyroxine RCT (Dhar et al., NEJM 2023): 838 brain-dead potential heart donors with haemodynamic instability, 30 µg/h for ≥12 h vs saline; hearts transplanted
#    54.9% vs 53.2% (no difference); 30-day graft survival similar; more severe hypertension and tachycardia with levothyroxine.
# From standard references without a fresh check (confident unless stated): Cushing triad; cold caloric technique (about 50 mL ice water, observe 1 min, 5 min between ears);
# CO2 rises about 3 mmHg/min during apnoea; EEG electrocerebral silence (no activity over 2 µV, 30 min); TCD patterns; radionuclide 'hollow skull'; frequency table
# (DONOR-08) as standard teaching; Crystal City 2002 hormone doses (T4 20 µg then 10 µg/h; T3 4 µg then 3 µg/h; vasopressin 1 U then 0.5–4 U/h); desmopressin IV 1–4 µg then
# 1–2 µg 6-hourly; Mascia JAMA 2010 donor lung trial (eligible lungs about 95% vs 54%, harvested 54% vs 27%); Niemann NEJM 2015 donor hypothermia; UNOS 2002 ECD definition
# and KDPI from 2014; HOPE Act (USA, 2013); Maastricht categories; cold ischaemia limits.

SPINE = [
  ("Donation in India and the law", "India donates under one organ donor per million because potential donors are not identified and declared, and the law (THOA 1994, amended 2011, Rules 2014) makes the ICU doctor responsible for asking."),
  ("Preconditions before any testing", "Brainstem death can be tested only when the cause is known and irreversible and every reversible look-alike — cold, drugs, paralysis, shock, metabolic upset — has been excluded."),
  ("The clinical exam and apnoea test", "Every brainstem reflex must be absent and the patient must not breathe when the PaCO₂ has risen to at least 60 mmHg; spinal reflexes are allowed, posturing is not."),
  ("Ancillary tests and certification", "Ancillary flow studies are used only when the exam or apnoea test cannot be completed, and in India a board of four certifies death after two sets of tests at least 6 hours apart."),
  ("What brainstem death does to the body", "As the brainstem dies, a brief sympathetic storm injures the heart and lungs, then loss of sympathetic tone, diabetes insipidus and hypothermia cause the hypotension that loses organs."),
  ("Keeping and choosing the organs", "Donor care switches from protecting the brain to perfusing every other organ — volume, vasopressin, hormones, lung-protective ventilation — and then each organ is judged on its own against a short list of absolute contraindications."),
]

PRIMER = "Brain death, or death by neurological criteria, is the irreversible loss of all brain function including the brainstem; Indian and UK law use the term brainstem death, and it is legally death. The heart can keep beating for hours to days because it has its own pacemaker, as long as the ventilator supplies oxygen. The brainstem carries the cranial nerve reflexes and the respiratory centre, which is why the diagnosis rests on absent reflexes and an apnoea test. Once death is declared the patient becomes a potential donor, and the ICU’s task changes from saving the brain to keeping the other organs alive."

L = {}

L['DONOR-01'] = dict(
  sub="Special situations → Organ donation → Donation in India",
  step=1,
  intro="Step 1 is why this deck exists: most potential donors in India are lost before anyone asks. The gap is not the law, which has recognised brainstem death since 1994, but identification and declaration in the ICU, which is the intensivist’s job.",
  parts=[
    ('a', "**About 0.8 per million population (up from 0.05), vs about 35–36 in Croatia and Spain (USA about 21); about 4 lakh die each year waiting.** India’s deceased-donor rate was still about 0.8 per million in 2024. The comparison figures on the card are about a decade old: in 2024 Spain reached about 54 per million and the USA about 50, so the gap is now more than 60-fold. The number who die waiting is an estimate, not a registry count; the figure most often quoted by the Health Ministry is about 5 lakh a year."),
    ('b', "**THOA 1994 recognised brainstem death; amended to include tissues (THOTA, in force 2014); NOTTO, ROTTO, SOTTO.** The Transplantation of Human Organs Act 1994 made brainstem death legal death for the purpose of donation and banned organ trade. The 2011 amendment added tissues, made the ICU doctor ask every eligible family about donation (required inquiry) and inform the retrieval centre, and allowed a substitute when no neurologist is available (DONOR-06). The Rules of 2014 put the amendment into practice; NOTTO (national), ROTTO (regional) and SOTTO (state) run the registry and allocation."),
    ('c', "**Brainstem death, or a catastrophic irreversible brain injury heading for it.** The donor pool is mainly road-traffic head injury, intracranial haemorrhage and hypoxic brain injury; identifying them before the brainstem dies allows the organs to be protected through the storm."),
    ('d', "**Identify donors, declare brain death, and keep the organs viable.** Each of the three is a point of loss: a donor not recognised, a death not tested, or organs lost to untreated hypotension and diabetes insipidus (DONOR-07)."),
  ],
  mimic=[
    ("Brainstem death (India, UK) vs whole-brain death (USA)", "The clinical tests are the same; the legal wording differs, and the US 2023 guideline speaks of loss of all brain function including the brainstem."),
  ],
  traps=[
    ("“India’s low rate is due to the absence of a law on brain death”", "Brainstem death has been legal since 1994; the losses are in identification, declaration and donor care."),
    ("“Asking the family about donation is optional”", "Since the 2011 amendment the ICU doctor must ask, and the hospital must inform the retrieval centre."),
  ],
  decode=[
    ("Which Indian Act recognised brainstem death? [pattern]", "THOA 1994; tissues added by the 2011 amendment, Rules 2014."),
    ("The intensivist’s duties in deceased donation [pattern]", "Identify the potential donor, certify brainstem death, request donation and maintain the donor."),
  ],
  punch="India’s donors are lost in the ICU, not in the law: the brainstem-dead patient must be recognised, tested, asked about and kept perfused.",
)

L['DONOR-02'] = dict(
  sub="Special situations → Brain death → Preconditions",
  step=2,
  intro="Step 2 is the gate before any test. A brainstem examination only means death when nothing else could be suppressing the brainstem, so the stems give a patient who looks brain-dead and ask what must be fixed first. Four real questions test this: cold, sedative infusions, a CT read as death, and residual sedation after cardiac arrest.",
  parts=[
    ('a', "**Irreversible coma of known cause, matching neuroimaging.** The cause must be catastrophic and enough to explain loss of all brainstem function — haemorrhage, trauma, hypoxic injury — and the scan must fit. A CT showing global oedema (loss of grey–white differentiation, effaced sulci and cisterns) supplies that cause but never diagnoses death; the clinical exam and apnoea test still do."),
    ('b', "**No CNS depressants (phenobarbitone under 10 µg/mL; thiopentone under 5 mg/L).** Sedatives abolish brainstem reflexes reversibly. If a level cannot be measured, wait at least five elimination half-lives (2023 guideline), longer after a prolonged infusion, in renal or hepatic failure, obesity or after hypothermia — midazolam’s active metabolite accumulates in renal failure. If waiting is not possible, an ancillary flow study is used (DONOR-05)."),
    ('c', "**No residual paralysis (train-of-four if needed).** A paralysed patient has no motor response and no breathing; a train-of-four with four twitches excludes neuromuscular block."),
    ('d', "**No severe acid–base, electrolyte or endocrine disturbance.** Severe hypo- or hypernatraemia, hypoglycaemia, uraemia, hepatic encephalopathy and myxoedema can deepen coma; they must be corrected or judged not to explain the picture."),
    ('e', "**Temperature over 36 °C; SBP over 100 mmHg.** Cold depresses brainstem reflexes and slows drug clearance; the 2023 guideline requires a core temperature of 36 °C or more and, after temperature fell to 35.5 °C or below, waits 24 hours after rewarming. Adults also need a systolic of 100 or more and a MAP of 75 or more, because low perfusion can depress the brainstem reversibly."),
    ('f', "**No spontaneous breathing (apnoeic on the ventilator).** A patient triggering the ventilator is not brain-dead; check that the ventilator is not auto-triggering from cardiac oscillation before calling a breath."),
  ],
  mimic=[
    ("Brainstem death vs severe hypothermia (drowning in cold water)", "Both give fixed pupils and absent reflexes; rewarm to at least 36 °C, then test."),
    ("Brainstem death vs locked-in state or krait-bite paralysis", "Locked-in (ventral pontine lesion) keeps consciousness and vertical eye movement; krait and fulminant Guillain–Barré paralyse the cranial nerves and limbs peripherally, so the patient looks brain-dead but the brain is intact."),
    ("Global cerebral oedema on CT vs brain death", "CT shows the cause; only the clinical tests (or a flow study) show death."),
  ],
  traps=[
    ("“Core 30 °C with absent reflexes — repeat the exam in 2 hours or perform an EEG”", "Cold invalidates both; rewarm to at least 36 °C first (68% on DocT)."),
    ("“GCS 3, absent reflexes, diffuse grey–white loss on CT — brain death”", "The CT diagnosis is global cerebral oedema; death needs the clinical tests (64% on DocT)."),
    ("“On midazolam and fentanyl infusions — proceed to the apnoea test”", "Stop the sedatives, wait at least five half-lives and reassess (88% on DocT)."),
    ("“Post-cardiac arrest, comatose on propofol and fentanyl — no temperature control until sedation is excluded” (Marrow key)", "The key is disputed: AHA and ERC recommend temperature control for every comatose patient after ROSC. Sedation delays brain-death testing and prognostication, not temperature control."),
  ],
  decode=[
    ("Cold-water drowning, core 30 °C, absent brainstem reflexes, apnoea test deferred — next step? [DocT]", "Rewarm to at least 36 °C."),
    ("RTA, GCS 3, absent reflexes, CT with diffuse grey–white loss — diagnosis? [DocT]", "Global cerebral oedema, not brain death."),
    ("SAH, fixed pupils, on midazolam and fentanyl — next step? [DocT]", "Stop sedatives, wait and reassess."),
    ("Post-OHCA, propofol/fentanyl, GCS 3T — what follows? [Marrow]", "Exclude residual sedation before brain-death testing; temperature control is still given."),
  ],
  punch="A brain-dead-looking patient is not tested until the cause is known and cold, drugs, paralysis, shock and metabolic upset are excluded; the scan shows the cause, never the death.",
)

L['DONOR-03'] = dict(
  sub="Special situations → Brain death → Brainstem reflexes",
  step=3,
  intro="Step 3 is the examination itself. Each reflex tests a stretch of the brainstem from midbrain to medulla, so all must be absent; the most-asked card in the deck (ten real questions) turns on two points — what an absent doll’s-eye response means, and which movements are still allowed because they come from the spinal cord.",
  parts=[
    ('a', "**Pupils fixed to bright light.** The light reflex runs through the optic nerve to the midbrain and back through the third nerve, so a non-reactive pupil means the midbrain is gone. In brain death the pupils are usually mid-position or dilated; pinpoint pupils suggest drugs or a pontine lesion instead."),
    ('b', "**Corneal and gag; cough to tracheal suction.** The corneal reflex tests the fifth and seventh nerves in the pons; gag and cough test the ninth and tenth in the medulla. Cough is tested with a suction catheter passed down to the carina, the strongest stimulus available in an intubated patient."),
    ('c', "**Oculocephalic (doll’s eyes; only if the cervical spine is cleared) and oculovestibular (cold caloric).** Both use the vestibular nuclei and the pathways between the third, fourth and sixth nerve nuclei. In a comatose patient with an intact brainstem, turning the head sends the eyes the opposite way; eyes that stay fixed in the midline when the head is turned mean brainstem dysfunction, not hemispheric damage. In the caloric test about 50 mL of ice water in each ear (head up 30°, intact drum) normally drives slow deviation toward the cold ear; no movement over a minute of observation is consistent with brain death."),
    ('d', "**No facial grimace to supraorbital or TMJ pressure; no motor response to pain in all four limbs.** Pain in the face travels in the fifth nerve and the grimace leaves through the seventh, so any facial movement means a working pons. A facial movement to limb stimulation is also a brainstem response and excludes brain death. Decerebrate or decorticate posturing needs an intact brainstem and also excludes it."),
    ('e', "**Spinal reflexes are allowed (limb withdrawal, Lazarus sign).** The spinal cord survives brain death, so triple flexion of the legs, a Babinski response, finger flexion, undulating toe movements and the Lazarus sign (arms rising and crossing the chest, often during the apnoea test) are compatible. Sweating, tachycardia and a normal pressure without pressors also do not exclude it. Seizures do (they need a cortex)."),
  ],
  table=dict(title="Compatible with brain death or not", head=["Finding", "Origin", "Brain death?"], rows=[
    ["Triple flexion, Babinski, Lazarus sign", "spinal cord", "**compatible**"],
    ["Sweating, tachycardia, normal BP off pressors", "spinal sympathetic outflow", "**compatible**"],
    ["Decerebrate or decorticate posturing", "brainstem", "excludes"],
    ["Facial movement to limb stimulation, grimace", "pons (V, VII)", "excludes"],
    ["Seizure activity", "cortex", "excludes"],
  ]),
  mimic=[
    ("Spinal reflex vs posturing", "Triple flexion is stereotyped and local to the stimulated limb; posturing is a pattern of all limbs organised by the brainstem."),
    ("Absent doll’s eyes in coma vs locked-in syndrome", "Locked-in patients are awake with vertical gaze and blinking preserved; absent oculocephalic responses in a comatose patient mean brainstem dysfunction."),
  ],
  traps=[
    ("“Minimal triple flexion means she does not meet brain-death criteria” (59% on DocT GT)", "Triple flexion is a spinal reflex; with absent cranial nerve reflexes and a positive apnoea test (PaCO₂ 20 above baseline) the exam is consistent with brain death, no ancillary test needed."),
    ("“Eyes fixed midline when the head is turned — cerebral hemispheric dysfunction or locked-in” (60–72%)", "Hemispheric coma leaves doll’s eyes intact; their absence means brainstem dysfunction."),
    ("“Decerebrate posturing is compatible with brain death”", "It needs a working brainstem; the Lazarus sign is the compatible finding (78–85%)."),
    ("“The apnoea test is not mandatory”", "It is the false statement: it is part of every determination unless it cannot be done, when an ancillary test replaces it."),
    ("“No breathing after cardiac arrest is enough, even with pupil, corneal and cough reflexes present”", "Any brainstem reflex excludes brain death (97% right)."),
  ],
  decode=[
    ("Head briskly turned, eyes stay midline — what does this signify? [DocT ×1, DocT GT ×2]", "Brainstem dysfunction."),
    ("Which finding is compatible with brain death? (Lazarus, decerebrate posturing, facial movement to limb stimulus, EEG seizures) [DocT GT ×2]", "Lazarus sign with arm flexion."),
    ("SAH, all cranial reflexes absent, minimal triple flexion, apnoea test PaCO₂ +20 — most true? [DocT GT]", "Consistent with brain death."),
    ("Child: finding NOT consistent with brain death [Marrow]", "Decorticate or decerebrate posturing; in brain death which reflex is typically preserved? Spinal reflexes [DocT GT]."),
  ],
  punch="Every reflex that runs through the brainstem — pupils, cornea, gag, cough, eye movements, facial grimace — must be absent; movements that come from the spinal cord, such as triple flexion and the Lazarus sign, are allowed, while posturing is not.",
)

L['DONOR-04'] = dict(
  sub="Special situations → Brain death → Apnoea test",
  step=3,
  intro="Step 3 ends with the apnoea test, which tests the medullary respiratory centre with the strongest stimulus it has, carbon dioxide. Real questions ask the PaCO₂ threshold, whether the test is mandatory, and how to do it on ECMO, which the card does not cover.",
  parts=[
    ('a', "**Stable, PaCO₂ 35–45; pre-oxygenate with FiO₂ 1.0 for over 10 min to PaO₂ over 200, PEEP 5; disconnect with oxygen at the carina (6 L/min) or a T-piece with CPAP 10; ABG at 8–10 min; positive if no breathing with PaCO₂ 60 or more, or a rise of 20 or more.** Starting from normal CO₂ makes the test valid and predictable: in apnoea the PaCO₂ rises by about 3 mmHg a minute, so 8–10 minutes takes it from 40 past 60. Pre-oxygenation fills the lungs with oxygen so that apnoeic oxygenation keeps the saturation up while CO₂ climbs; CPAP keeps the alveoli open in a donor whose lungs will be needed. The 2023 AAN/SCCM guideline requires the PaCO₂ to be 60 or more AND at least 20 above baseline, with pH under 7.30; the card’s ‘or’ is the older adult wording. In a known CO₂ retainer his own baseline is used; when that baseline is uncertain an ancillary test is the safer route. The test is stopped at once if he takes a breath; if pressure, rhythm or saturation fail, an ABG is drawn, he is reconnected, and an ancillary test is used instead. On ECMO the test is still done: oxygenate through the ventilator (or CPAP 10 on the tube) and the membrane at FiO₂ 1.0, and cut the sweep gas to 0.2–1 L/min so CO₂ rises; on VA-ECMO gases are taken from both the arterial line and the circuit."),
  ],
  table=dict(title="The apnoea test, step by step", head=["Step", "What", "Why"], rows=[
    ["Before", "PaCO₂ 35–45, pH 7.35–7.45, SBP ≥100", "a valid start and a stable patient"],
    ["Pre-oxygenate", "FiO₂ 1.0 ≥10 min", "oxygen reserve for apnoeic oxygenation"],
    ["Apnoea", "catheter O₂ or CPAP 10; watch chest and abdomen", "CO₂ rises about 3 mmHg/min"],
    ["ABG at 8–10 min", "**PaCO₂ ≥60 and ≥20 above baseline, pH <7.30** (2023)", "maximal stimulus to the medulla"],
    ["Abort", "breath (test negative); hypotension, arrhythmia, desaturation", "reconnect; ancillary test"],
  ]),
  mimic=[
    ("Ventilator auto-triggering vs a real breath", "Cardiac oscillation or a circuit leak can trigger the ventilator; disconnection, or CPAP without a backup rate, shows whether the patient breathes."),
  ],
  traps=[
    ("“PaCO₂ of 45 or 50 confirms brain death”", "The threshold is 60 mmHg (Marrow), and in the 2023 guideline also 20 above baseline."),
    ("“The apnoea test is not mandatory” (87% saw this was false)", "It is required whenever it can be done safely; only an aborted or impossible test is replaced by an ancillary test."),
    ("“ECMO is a contraindication to the apnoea test”", "Reduce the sweep gas to 0.5–1 L/min (Marrow; 0.2–1 in the 2023 guideline) and oxygenate by CPAP 10 through the tube."),
  ],
  decode=[
    ("Apnoea test: PaCO₂ level confirming brain death [Marrow]", "60 mmHg (with a rise of 20 above baseline)."),
    ("Apnoea test on VV-ECMO — strategy that keeps oxygenation while CO₂ rises [Marrow ×2]", "Sweep 0.5–1 L/min plus CPAP 10 via the tube."),
    ("Not true regarding brain death [DocT]", "‘Apnoea test not mandatory’."),
  ],
  punch="Start at normal CO₂, pre-oxygenate, stop ventilating, and call death only if he does not breathe once the PaCO₂ is at least 60 and 20 above baseline; on ECMO, turn the sweep down rather than skip the test.",
)

L['DONOR-05'] = dict(
  sub="Special situations → Brain death → Ancillary tests",
  step=4,
  intro="Step 4 is what to do when the clinical exam cannot be finished. Ancillary tests do not replace the clinical diagnosis; they stand in for the part that could not be done, and the six real questions ask which test, when, and what it shows.",
  parts=[
    ('a', "**Only when the clinical exam cannot be completed (facial trauma, cervical injury) or the apnoea test is inconclusive or aborted; one test suffices.** Smashed eyes, ears or face, a high cervical injury, or a patient too unstable or hypoxic for the apnoea test are the usual reasons; residual drugs that cannot be waited out are another. The clinical exam is still done as far as possible."),
    ('b', "**Four-vessel cerebral angiography: no intracranial filling of carotid or vertebral arteries.** When intracranial pressure exceeds arterial pressure, contrast stops at the skull base. Angiography is the reference standard; a radionuclide perfusion scan showing no uptake in the brain (the ‘hollow skull’) is accepted equally in the 2023 guideline."),
    ('c', "**EEG: no reactivity to intense stimuli.** Brain death gives an isoelectric EEG (electrocerebral silence, no activity over 2 µV) over a full montage, off sedation. But EEG records only the cortex, not the brainstem, and is abolished by drugs and cold, so the 2023 AAN/SCCM guideline no longer accepts EEG (or evoked potentials) as an ancillary test; some other national codes still do."),
    ('d', "**TCD: reverberating flow or small systolic spikes; absent flow is NOT reliable (bone window).** Oscillating flow (forward in systole, reversed in diastole) or small early systolic spikes mean blood moves in and out without perfusing the brain. Absent signals may only mean no acoustic window, which is common. TCD is accepted in adults only."),
    ('e', "**Evidence for CT or MR angiography is insufficient.** The 2023 guideline does not accept them, because they have not been validated: CT angiography can show residual filling in a dead brain and its criteria are not standardised."),
  ],
  mimic=[
    ("Flow studies vs EEG", "Flow studies (angiography, scintigraphy, TCD) show no blood reaches the brain and are not affected by drugs; EEG shows cortical silence only and is affected by sedatives and cold."),
  ],
  traps=[
    ("“Apnoea test aborted — he does not meet criteria”", "The aborted test is replaced by an ancillary test; complete clinical exam plus a supportive study confirms death (56% on DocT GT). The study in that stem was PET, which is not a standard ancillary test; the accepted ones are angiography, radionuclide perfusion and TCD."),
    ("“Severe facial trauma, apnoea test impossible — MRA, CTA or BAEP confirms brain death”", "Four-vessel cerebral angiography is the confirmatory test (53–66% on DocT)."),
    ("“EEG is part of every brain-death determination”", "It is ancillary only when the clinical exam is incomplete, and no longer accepted at all in the 2023 US guideline (Marrow)."),
    ("“No TCD signal confirms brain death”", "It may be no bone window; only oscillating flow or systolic spikes count."),
  ],
  decode=[
    ("Midface fractures, apnoea test unsafe, investigation shown — what does it indicate? [DocT, DocT GT ×2]", "Cerebral angiography: confirmatory of brain death."),
    ("Apnoea test aborted for instability, whole-brain PET shows no activity — most correct? [DocT GT]", "Meets criteria: clinical exam consistent and the ancillary study supports it."),
    ("Not routinely included in brain-death determination [Marrow]", "EEG."),
    ("Suspected brain death after anoxic injury — expected EEG [Marrow]", "Isoelectric."),
  ],
  punch="Ancillary tests fill in only the part of the exam that could not be done; a flow study showing no blood entering the skull is the answer, EEG is out in the 2023 guideline, and an absent TCD signal proves nothing.",
)

L['DONOR-06'] = dict(
  sub="Special situations → Brain death → Certification in India",
  step=4,
  intro="Step 4 continues with who signs. The Indian law sets a board of four and two sets of tests six hours apart; the three real questions (one DocT stem, asked three times) ask what is needed to confirm death after a first positive test.",
  parts=[
    ('a', "**A board of four: doctor in charge, hospital administrator, a nominated physician, surgeon or intensivist, and a neurologist or neurosurgeon (or anaesthetist/intensivist if none).** In the Act the four are the registered medical practitioner in charge of the hospital (medical superintendent), an independent specialist nominated from a panel approved by the Appropriate Authority, a neurologist or neurosurgeon from the panel, and the doctor treating the patient. Where no neurologist or neurosurgeon is available, the 2011 amendment lets the hospital nominate an independent surgeon or physician and an anaesthetist or intensivist. None may belong to the transplant team for that recipient, so that the people declaring death gain nothing from it."),
    ('b', "**Two examinations with apnoea tests, at least 6 hours apart.** The board performs the full set of tests twice and records them on Form 10; in children the interval is longer at the board’s discretion. The US 2023 guideline differs: one examination is enough in adults, while children need two examinations by two clinicians at least 12 hours apart."),
    ('c', "**Counsel the family about brain death and donation after the first test.** The six hours give the family time to understand that death is being confirmed; the 2011 amendment makes the request for donation a duty of the ICU doctor."),
    ('d', "**Family unwilling: tests still done, certification withheld, care continued until cardiac death (per your notes).** Indian law frames brainstem-death certification around donation, and what is done when donation is declined varies between hospitals and states; the deck follows your notes here."),
  ],
  mimic=[
    ("India and UK vs US 2023", "India: board of four, two sets of tests 6 h apart. US: one exam in adults, two exams 12 h apart in children; ancillary tests in neither unless the exam is incomplete."),
  ],
  traps=[
    ("“Repeat the apnoea test after 24 hours”, “EEG confirmation” or “MRI brain”", "None is required; DocT keys two clinical examinations by different physicians (57–69%), which matches the Indian two sets of tests by the board."),
    ("“A transplant surgeon can sit on the board”", "Members must not belong to the transplant team for the recipient."),
  ],
  decode=[
    ("Massive ICH, no pupillary, corneal or oculocephalic responses, apnoea test PaCO₂ 62, no confounders — what is required to confirm brain death? [DocT, DocT GT ×2]", "Two clinical examinations by different physicians (in India, the board’s two sets at least 6 h apart; an adult US determination would need only one)."),
    ("Composition of the brainstem-death board in India [pattern]", "Medical superintendent, independent nominated specialist, neurologist or neurosurgeon, treating doctor; none from the transplant team."),
  ],
  punch="In India four doctors, none from the transplant team, test twice at least six hours apart and sign Form 10; EEG, MRI and a 24-hour wait are not part of it.",
)

L['DONOR-07'] = dict(
  sub="Special situations → Brain death → Pathophysiology",
  step=5,
  intro="Step 5 is what happens to the body as the brainstem dies, which explains every problem in donor management. The real questions ask about the first stage — the Cushing reflex of impending herniation — and how to tell it from the storm that follows.",
  parts=[
    ('a', "**Rising ICP → herniation; brainstem damage runs pons → medulla (rostral to caudal).** As the brain swells and herniates, ischaemia moves down from the midbrain through the pons to the medulla, and each level’s function is lost in turn; the autonomic picture changes as it goes."),
    ('b', "**Cushing reflex: hypertension + bradycardia.** Brainstem ischaemia drives a sympathetic surge to push blood into the skull, and the high pressure triggers a baroreflex bradycardia through the still-working vagal nucleus. The full triad adds irregular or slow breathing from the failing respiratory centre, and the pulse pressure widens — for example HR 48, BP 165/70, RR 10. It is a late sign of impending herniation."),
    ('c', "**Autonomic storm: the vagal nucleus dies → unopposed sympathetic surge: tachycardia, hypertension, catecholamines → contraction-band necrosis, Takotsubo, arrhythmias, neurogenic pulmonary oedema.** Once the medulla dies the brake is gone and the heart rate rises. A catecholamine surge many times normal causes subendocardial ischaemia and myocyte calcium overload (contraction-band necrosis), and a sudden rise in left atrial pressure plus capillary injury floods the lungs."),
    ('d', "**Loss of sympathetic tone: vasodilatation, hypotension.** With the brainstem dead, the spinal sympathetic outflow loses its drive, so vessels dilate and the injured heart cannot compensate."),
    ('e', "**Hypothalamic–pituitary failure: hypothermia, diabetes insipidus, low T3, cortisol, insulin (hyperglycaemia); inflammation (IL-6, TNF); DIC.** The posterior pituitary, whose blood supply is entirely intracranial, fails more often than the anterior, so vasopressin falls and diabetes insipidus follows; temperature control is lost; necrotic brain releases tissue factor, causing DIC."),
  ],
  mimic=[
    ("Cushing reflex vs the autonomic storm", "Cushing: hypertension with BRADYcardia and irregular breathing while the vagus still works. Storm: hypertension with TACHYcardia after the vagal nucleus has died."),
  ],
  traps=[
    ("“Tachycardia is part of Cushing’s triad”", "The triad is hypertension, bradycardia and irregular respiration; tachycardia belongs to the later storm."),
    ("“The storm is what loses organs”", "The storm is brief; the hypotension that follows is what loses organs (card’s watch line)."),
  ],
  decode=[
    ("Cushing’s triad includes all EXCEPT [DocT GT]", "Tachycardia."),
    ("TBI with hypertension, bradycardia and irregular respirations — what is it called? [DocT GT]", "Cushing reflex (98%)."),
    ("Severe TBI, GCS 6: vital signs of impending herniation [Marrow]", "HR 48, BP 165/70, RR 10."),
  ],
  punch="Herniation gives the Cushing response first (high pressure, slow pulse, irregular breathing), then the vagus dies and a brief tachycardic storm injures heart and lungs, and then loss of tone, diabetes insipidus and cold bring the hypotension.",
  extra=[dict(q="What completes Cushing’s triad beyond the card’s hypertension and bradycardia?", a="**Irregular or depressed respiration**, with a widened pulse pressure; it signals impending herniation.")],
)

L['DONOR-08'] = dict(
  sub="Special situations → Brain death → Frequency of donor problems",
  step=5,
  intro="Step 5 in numbers: once the brainstem is dead, almost every donor becomes cold, most become hypotensive and most develop diabetes insipidus. The figures tell you what to expect and therefore what to treat before it happens.",
  parts=[
    ('a', "**Hypothermia, 100%: hypothalamic failure.** Heat production and vasoconstriction are lost, and the vasodilated donor loses heat to cold fluids and air."),
    ('b', "**Hypotension, 80–97%: vasoplegia, hypovolaemia, myocardial dysfunction.** Loss of sympathetic tone, fluid lost through diabetes insipidus and earlier osmotic therapy, and the stunned heart after the storm all add up."),
    ('c', "**Diabetes insipidus, 65–90%: posterior pituitary failure.** Vasopressin stops, so dilute urine pours out (DONOR-13)."),
    ('d', "**Arrhythmias, 25–32%: catecholamines, myocardial injury.** Also driven by cold and electrolyte shifts from diabetes insipidus."),
    ('e', "**Pulmonary oedema, 15–20%: endothelial injury.** Neurogenic pulmonary oedema from the storm, plus aspiration and contusion."),
    ('f', "**Cardiac arrest, small: prolonged hypotension, arrhythmia.** It is the end point of untreated hypotension, and the reason donor care starts at once."),
  ],
  mimic=[
    ("Hypotension from vasoplegia vs from diabetes insipidus", "Vasoplegia: warm, low SVR; diabetes insipidus: high dilute urine output and a rising sodium."),
  ],
  traps=[
    ("“Diabetes insipidus is an occasional complication”", "It occurs in most donors (65–90%)."),
  ],
  decode=[
    ("Commonest physiological problem after brainstem death [pattern]", "Hypothermia (all), then hypotension and diabetes insipidus."),
  ],
  punch="Expect every donor to be cold, most to be hypotensive and most to pour out dilute urine; treat them before they cost organs.",
)

L['DONOR-09'] = dict(
  sub="Special situations → Donor management → Targets",
  step=6,
  intro="Step 6 begins with the goals. The ‘rule of 100’ (systolic 100, urine 100 mL/h, PaO₂ 100, haemoglobin 10, glucose 100) is an old teaching frame; current guidelines keep the pressure, urine and oxygen goals but are more restrictive with blood and more relaxed with glucose.",
  parts=[
    ('a', "**SBP 100–120 / MAP over 60–70; CVP 8–10 mmHg.** SCCM 2015 and the heart–lung guidelines set MAP over 60, the Canadian over 65; the UK bundle 60–80. CVP is a guide only; dynamic assessment and echo are better (DONOR-10)."),
    ('b', "**Urine over 100 mL/h (1–3 mL/kg/h).** Urine output shows kidney perfusion, but a very high output is diabetes insipidus, not good perfusion."),
    ('c', "**PaO₂ over 100; SpO₂ over 95%; PaCO₂ 35–45, pH 7.35–7.45.** Normal gas exchange with the lowest FiO₂ that achieves it protects the lungs for retrieval (DONOR-14)."),
    ('d', "**Haemoglobin 10 g/dL (Hct 30%); glucose about 100 (80–150 on insulin).** Both are older targets: SCCM 2015 and the Canadian guideline transfuse only below 7 g/dL, and SCCM accepts glucose under 180 mg/dL; the aim is to avoid severe hyperglycaemia, which worsens osmotic diuresis and pancreatic graft function."),
    ('e', "**Temperature over 35 °C (aim 36.5); sodium 135–155; potassium 4–5.** Normothermia (36–37 °C) is the thoracic-organ target. Mild hypothermia (34–35 °C) reduced delayed kidney graft function in one trial (Niemann, NEJM 2015: 28% vs 39%), but a later trial found it inferior to machine perfusion of the kidney, and its effect on thoracic organs is untested, so the Canadian guideline uses it only when thoracic organs are not being retrieved. Donor sodium over 155 was linked to early liver graft dysfunction in older series (later series are less consistent)."),
  ],
  mimic=[
    ("Brain-protection targets vs donor targets", "Before death: osmotherapy, high sodium and permissive hypernatraemia. After death: normal sodium and generous perfusion of every other organ."),
  ],
  traps=[
    ("“Transfuse every donor to haemoglobin 10”", "Current guidelines use 7 g/dL; 10 is the old rule of 100."),
  ],
  decode=[
    ("Haemodynamic target in the brain-dead donor [pattern]", "MAP over 60–70 (SBP about 100), urine over 1 mL/kg/h."),
  ],
  punch="Perfuse every organ: MAP over 60–70, urine about 1–3 mL/kg/h, normal oxygen and CO₂, normal sodium and temperature; the haemoglobin 10 of the ‘rule of 100’ is now 7.",
)

L['DONOR-10'] = dict(
  sub="Special situations → Donor management → Haemodynamics",
  step=6,
  intro="Step 6 continues with the circulation, where most donors are lost. The one real question links to a separate card but tests the same physiology: a heart without vagal input does not respond to atropine.",
  parts=[
    ('a', "**Autonomic storm: transient; only short-acting drugs (esmolol).** The storm lasts minutes to hours and is followed by hypotension, so a long-acting β-blocker would leave the donor hypotensive afterwards; esmolol can be switched off within minutes."),
    ('b', "**Bradycardia: atropine does not work (vagal nuclei dead) → adrenaline, isoprenaline, pacing.** Atropine works only by blocking vagal tone, and the vagus has no tone to block. Direct β-agonists and pacing act on the heart itself, which is why the same rule applies to the denervated heart after transplantation."),
    ('c', "**Tachyarrhythmia: cardioversion, amiodarone; correct electrolytes, volume, temperature.** Cold, hypokalaemia, hypomagnesaemia and high catecholamine doses drive the arrhythmias; correcting them is the first treatment."),
    ('d', "**Fluids: balanced crystalloid; avoid big saline loads (hyperchloraemia); half-normal saline with 5% dextrose for hypernatraemia; avoid synthetic colloids (kidney); albumin acceptable.** Hydroxyethyl starch causes osmotic tubular injury and delayed kidney graft function in recipients; free water corrects the sodium lost from diabetes insipidus."),
    ('e', "**Assess dynamically (echo, urine); CVP alone misleads.** Echo shows whether the problem is an empty heart, a weak one or dilated vessels, which decides fluid, inotrope or vasopressor (DONOR-11). A poor echo early after the storm often recovers, so it should not by itself exclude the heart."),
  ],
  mimic=[
    ("Donor bradycardia vs vagal bradycardia", "Vagal: responds to atropine. Brain-dead donor or denervated transplanted heart: atropine and glycopyrrolate fail; give isoprenaline or adrenaline, or pace."),
  ],
  traps=[
    ("“Atropine for bradycardia in a heart transplant recipient or brain-dead donor”", "No vagal tone to block; the answer is isoprenaline (Marrow)."),
    ("“Labetalol or metoprolol for the storm”", "The storm ends in hypotension; use esmolol or nothing."),
  ],
  decode=[
    ("Heart transplant 3 years ago, intraoperative bradycardia — best drug? [Marrow]", "Isoprenaline (direct β-agonist)."),
    ("Brain-dead donor, HR 35 — atropine given without effect, next? [pattern]", "Adrenaline or isoprenaline, or pacing."),
  ],
  punch="The donor’s heart has no vagus: atropine fails and direct β-agonists or pacing work; treat the brief storm with esmolol only, fill with balanced crystalloid, and judge volume by echo, not CVP.",
)

L['DONOR-11'] = dict(
  sub="Special situations → Donor management → Vasopressors",
  step=6,
  intro="Step 6, the pressor choice. The donor’s hypotension is largely loss of vasopressin and sympathetic tone, so replacing vasopressin first treats the cause and the diabetes insipidus together.",
  parts=[
    ('a', "**Restore volume first.** Diabetes insipidus, prior mannitol and bleeding leave most donors dry; pressors on an empty circulation constrict the organ beds."),
    ('b', "**MAP still under 60: is it low SVR or low cardiac output?** Echo or a cardiac output monitor answers this, and the answer chooses the drug."),
    ('c', "**Vasopressin first line (about 2.4 U/h = 0.04 U/min) for low SVR.** The brain-dead donor has low vasopressin levels, so a physiological dose restores tone, spares catecholamines (which down-regulate β-receptors and injure the myocardium) and treats diabetes insipidus. SCCM 2015 gives 0.01–0.04 U/min."),
    ('d', "**Still low: LVEF over 45% → norepinephrine or phenylephrine; LVEF under 45% → inotrope (dobutamine, dopamine, adrenaline).** A good ventricle with dilated vessels needs constriction; a weak ventricle needs inotropy."),
    ('e', "**Unstable: PA catheter or cardiac output monitor (CI over 2.4, PCWP 8–12, SVV under 12%), then hormone replacement.** Persisting instability is the indication for full hormone therapy (DONOR-12)."),
  ],
  mimic=[
    ("Vasopressin vs desmopressin in the donor", "Vasopressin acts on V1 (vessels) and V2 (kidney), so it treats hypotension and DI; desmopressin is V2-selective and treats DI without raising pressure."),
  ],
  traps=[
    ("“Norepinephrine is the first drug in the donor, as in septic shock”", "Vasopressin is the first-line pressor for the vasodilated donor because it replaces a hormone that is missing."),
  ],
  decode=[
    ("Brain-dead donor, MAP 55 after fluids, polyuria — first pressor? [pattern]", "Vasopressin, 0.01–0.04 U/min."),
  ],
  punch="Fill the donor, then replace the vasopressin he has lost; add norepinephrine if the heart is good and an inotrope if it is weak, and keep catecholamines low.",
)

L['DONOR-12'] = dict(
  sub="Special situations → Donor management → Hormone replacement",
  step=6,
  intro="Step 6, the hormones the dead pituitary no longer drives. Vasopressin and steroids are well established; thyroid hormone, long part of the standard package, failed in a large trial.",
  parts=[
    ('a', "**Vasopressin: 1 U bolus, then 0.5–4 U/h, for vasoplegia and DI.** The upper end (4 U/h, about 0.07 U/min) is above the SCCM range of 0.01–0.04 U/min; higher doses risk splanchnic and coronary constriction."),
    ('b', "**Methylprednisolone: 15 mg/kg at diagnosis, repeated every 24 h (or 250 mg then 100 mg/h), for hypocortisolism, inflammation and lung yield.** High-dose steroid dampens the cytokine surge after brain death and is associated with better oxygenation and more lungs retrieved. Low-dose hydrocortisone regimens gave similar pressor needs, lung function and organ yield with less hyperglycaemia in observational comparisons, and some guidelines accept them as an alternative."),
    ('c', "**Insulin: infusion to glucose 80–150, for hyperglycaemia.** Steroids, catecholamines, dextrose-containing fluids and insulin resistance raise glucose; SCCM accepts under 180 mg/dL."),
    ('d', "**T4: 20 µg bolus, then 10 µg/h (or 300–400 µg by tube 8-hourly), for low T3 and cardiac function.** In the 2023 NEJM trial (838 unstable brain-dead potential heart donors, levothyroxine 30 µg/h for at least 12 h vs saline), the proportion of hearts transplanted was the same (about 55% vs 53%) and levothyroxine caused more severe hypertension and tachycardia. Thyroid hormone is now reserved for donors with persistent instability or poor ventricular function, not given routinely."),
    ('e', "**T3: 4 µg bolus, then 3 µg/h (controversial).** T3 acts faster than T4 but has no better evidence; SCCM 2015 called either acceptable."),
  ],
  mimic=[
    ("Low T3 in the donor vs true hypothyroidism", "Brain death gives a sick-euthyroid pattern (low T3, normal or low TSH and T4); replacement trials have not shown more organs."),
  ],
  traps=[
    ("“Routine thyroid hormone increases hearts transplanted”", "The 2023 trial found no increase and more hypertension and tachycardia."),
  ],
  decode=[
    ("Which hormone replacement in the donor improves lung yield? [pattern]", "Methylprednisolone 15 mg/kg."),
    ("Routine levothyroxine in unstable brain-dead heart donors — effect? [pattern]", "No more hearts transplanted (NEJM 2023)."),
  ],
  punch="Give vasopressin for tone and DI, methylprednisolone for inflammation and lungs, and insulin for glucose; thyroid hormone is now kept for the persistently unstable donor, because a large trial found no extra hearts.",
)

L['DONOR-13'] = dict(
  sub="Special situations → Donor management → Diabetes insipidus",
  step=6,
  intro="Step 6, the commonest endocrine failure after brainstem death. Vasopressin stops when the posterior pituitary dies, so the kidneys pour out dilute urine, the donor becomes hypovolaemic and the sodium climbs.",
  parts=[
    ('a', "**Urine over 4 mL/kg/h; Na over 145; serum osmolality over 300; urine osmolality under 300 or specific gravity under 1.005.** The pattern is high volume of dilute urine with concentrated blood; that combination separates it from an osmotic or diuretic polyuria, in which the urine is not dilute."),
    ('b', "**65–90% of donors.** It is the rule, not the exception (DONOR-08)."),
    ('c', "**Desmopressin presumptively after 2 h of urine over 4 mL/kg/h (mannitol and furosemide excluded): 10 µg nasal, 1–2 puffs 4-hourly; or vasopressin 0.5–2 U/h.** Desmopressin is V2-selective and has no pressor effect, so it suits the normotensive donor; IV desmopressin (about 1–4 µg, then 1–2 µg 6-hourly) is easier to titrate in ICU than the nasal route. In the hypotensive donor vasopressin treats both problems (DONOR-11)."),
    ('d', "**Urine 30–200 mL/h; replace free water (half-saline, dextrose).** Matching losses with hypotonic fluid brings the sodium down; check glucose, as dextrose loads can cause hyperglycaemia and a new osmotic diuresis."),
  ],
  mimic=[
    ("DI vs osmotic or diuretic polyuria", "DI: urine osmolality under 300, sodium rising. Mannitol, glucose or furosemide: urine not dilute; check before giving desmopressin."),
  ],
  traps=[
    ("“Treat high urine output with more saline”", "Saline adds sodium; the loss is free water, and the fix is a V2 agonist plus hypotonic fluid."),
  ],
  decode=[
    ("Donor, urine 500 mL/h, Na 158, urine osmolality 150, BP normal — treatment? [pattern]", "Desmopressin plus free water."),
  ],
  punch="Dilute urine pouring out with a rising sodium is diabetes insipidus: desmopressin if the pressure is normal, vasopressin if it is low, and free water to bring the sodium below 155.",
)

L['DONOR-14'] = dict(
  sub="Special situations → Donor management → Ventilation",
  step=6,
  intro="Step 6, the lungs, the organ most often lost. Lungs are injured by the storm, aspiration, atelectasis and the apnoea test, and a protective strategy has been shown to double the number retrieved.",
  parts=[
    ('a', "**Volume control; VT 6–8 mL/kg predicted weight (UK bundle 4–8); PEEP 5–10; peak pressure under 30.** In the donor lung-protection trial (Mascia, JAMA 2010) VT 6–8 mL/kg with PEEP 8–10, CPAP during apnoea tests and closed suction made far more lungs eligible and about doubled those retrieved (54% vs 27%). The heart–lung guideline uses PEEP 8–10 and peak pressure under 35."),
    ('b', "**FiO₂ 1.0 at first, down to 0.4; SpO₂ over 95% or PaO₂ over 90; PaCO₂ 35–45.** The lowest FiO₂ that keeps oxygenation safe avoids absorption atelectasis and allows a true assessment of the lungs (the PaO₂ on FiO₂ 1.0 is used to judge them)."),
    ('c', "**Recruitment after apnoea tests, disconnections and suctioning; head up 30–45°; bronchoscopy and toilet.** Each disconnection collapses alveoli; recruitment and CPAP during the apnoea test reverse it; bronchoscopy clears aspirated material and plugs."),
    ('d', "**Atelectasis, V/Q mismatch, neurogenic pulmonary oedema.** Diuretics and conservative fluid help the oedema once the circulation is secure."),
  ],
  mimic=[
    ("Donor ventilation vs ARDS ventilation", "The same lung-protective principles; the donor adds recruitment after each apnoea test and bronchoscopy before retrieval."),
  ],
  traps=[
    ("“High tidal volumes keep the donor lungs open”", "Protective VT 6–8 mL/kg with PEEP retrieves more lungs."),
  ],
  decode=[
    ("Ventilator strategy that increases lungs retrieved from brain-dead donors [pattern]", "VT 6–8 mL/kg, PEEP 8–10, CPAP for apnoea tests, closed suction, recruitment."),
  ],
  punch="Ventilate the donor as you would an ARDS patient — low tidal volume, PEEP, low FiO₂ — and recruit after every apnoea test and disconnection; it doubles the lungs retrieved.",
)

L['DONOR-15'] = dict(
  sub="Special situations → Donor management → Other care",
  step=6,
  intro="Step 6, the remaining systems. Most of donor care is ordinary ICU care kept going after death, with a few donor-specific rules on infection and blood.",
  parts=[
    ('a', "**Temperature: prevent (easier than reversing); keep over 35.8 °C; active warming below 34 °C.** Cold causes arrhythmias, coagulopathy and cold diuresis; warm fluids and blankets from the start."),
    ('b', "**Blood: correct bleeding and coagulopathy; Hct over 30%.** DIC from brain tissue factor is common; give products for bleeding. The haematocrit target of 30% is older; current guidelines transfuse below haemoglobin 7 g/dL."),
    ('c', "**Infection transmission under 1–5%; bacteraemia is NOT a contraindication if pathogen-specific antibiotics are given 48 h before retrieval (recipient treated 7–10 days); no prophylactic antibiotics.** A treated, identified bacterium is a manageable risk; an unidentified infection of the brain is not (DONOR-16)."),
    ('d', "**VTE, GI, kidneys, drugs: LMWH or UFH; PPI; CRRT for overload, acidosis, hyperkalaemia; avoid nephrotoxic and hepatotoxic drugs.** The aim is to hand over organs in the best state possible."),
  ],
  mimic=[
    ("Treated bacteraemia vs undiagnosed CNS infection", "Treated bacteraemia: donation proceeds. Unexplained meningitis or encephalitis: absolute contraindication."),
  ],
  traps=[
    ("“Donor bacteraemia excludes donation”", "Not if pathogen-specific antibiotics have run for about 48 h before retrieval and the recipient is treated."),
  ],
  decode=[
    ("Brain-dead donor with MSSA bacteraemia on antibiotics for 48 h — proceed? [pattern]", "Yes; treat the recipient as well."),
  ],
  punch="Keep the donor warm, treat coagulopathy and identified infection, protect the kidneys; a treated bacteraemia does not stop donation.",
)

L['DONOR-16'] = dict(
  sub="Special situations → Donor criteria → Contraindications",
  step=6,
  intro="Step 6, who cannot donate. The list of absolute contraindications is short — infections that cannot be treated or screened and cancers that spread — and almost everything else is judged organ by organ.",
  parts=[
    ('a', "**Absolute: HIV, HTLV.** These cannot be cured in the recipient. In the Marrow stem the CD4 count of 180 is the clue to HIV infection with AIDS, which stops donation in India; some countries (the USA under the HOPE Act, South Africa) now transplant HIV-positive organs into HIV-positive recipients."),
    ('b', "**Absolute: rabies, measles, adenovirus, parvovirus; herpes encephalitis; LCMV; undiagnosed fever, encephalitis, meningitis, flaccid paralysis.** Unexplained neurological illness may be rabies, West Nile or LCMV, all of which have killed recipients; the cause must be known before donation."),
    ('c', "**Absolute: HBsAg positive (per your notes).** This is now relative: HBsAg-positive organs are used in HBsAg-positive or immune recipients with antiviral prophylaxis, and HCV-positive organs are used with direct-acting antivirals."),
    ('d', "**Absolute: grade 3–4 CNS tumours, choriocarcinoma, melanoma.** These spread through the blood; high-grade brain tumours are risky especially after a shunt or craniotomy. A small, treated, localised renal cell carcinoma is not a contraindication."),
    ('e', "**Not a contraindication: bacteraemia treated 48 h; anti-HBc with HBsAg negative; age (no upper limit); hypertension, diabetes (assess each organ).** Anti-HBc-positive livers carry latent virus and go to immune recipients with prophylaxis; kidneys and hearts carry little risk."),
  ],
  mimic=[
    ("Localised treated tumour vs metastasising tumour", "Treated small RCC or in-situ cancers: acceptable. Melanoma, choriocarcinoma, high-grade glioma: absolute."),
  ],
  traps=[
    ("“The past localised RCC is the reason to stop”", "It is not; the CD4 count of 180 (HIV) is (Marrow)."),
    ("“HBsAg positive always excludes donation”", "Not any more for matched or consenting recipients."),
  ],
  decode=[
    ("Hanging, brainstem-dead donor, past localised RCC, CD4 180 — donation status? [Marrow]", "Stop: CD4 count indicates HIV/AIDS."),
  ],
  punch="Untreatable infection (HIV, rabies, unexplained encephalitis) and spreading cancer (melanoma, choriocarcinoma, high-grade glioma) exclude donation; age, treated bacteraemia and a treated small tumour do not.",
)

L['DONOR-17'] = dict(
  sub="Special situations → Donor criteria → Standard vs expanded criteria (kidney)",
  step=6,
  intro="Step 6, the marginal donor. Expanded-criteria kidneys fail sooner than standard ones, but a recipient still lives longer with one than on dialysis, so they are used.",
  parts=[
    ('a', "**Standard (SCD): under 50 (any cause of brain death).** A standard donor is any donor who does not meet expanded criteria, so a 50–59-year-old with fewer than two risk factors is also standard."),
    ('b', "**Expanded (ECD): 60 or older; or 50–59 with 2 of hypertension, creatinine over 1.5, death from stroke.** The card’s table prints the 50–59 row under the standard column; it is an expanded-criteria rule (UNOS 2002). ECD was defined as a donor whose kidneys carry a relative risk of graft failure above 1.7 compared with an ideal donor. The USA replaced the ECD label with the continuous Kidney Donor Profile Index in 2014."),
  ],
  mimic=[
    ("ECD vs DCD", "ECD is about donor age and vascular risk; DCD is donation after circulatory death, a different route with more delayed graft function."),
  ],
  traps=[
    ("“A 55-year-old hypertensive who died of a stroke is a standard donor”", "Two risk factors at 50–59 make it expanded criteria."),
  ],
  decode=[
    ("Definition of an expanded-criteria kidney donor [pattern]", "Age 60 or more, or 50–59 with two of hypertension, creatinine over 1.5 mg/dL, death from stroke."),
  ],
  punch="Expanded-criteria means 60 or older, or 50–59 with two of hypertension, creatinine over 1.5 and stroke death; such kidneys fail sooner but still beat dialysis.",
)

L['DONOR-18'] = dict(
  sub="Special situations → Donor criteria → Cold ischaemia time",
  step=6,
  intro="Step 6 ends with the clock. Once the organ is cold-flushed, metabolism slows but does not stop, and each organ tolerates a different time; the order matters more than the exact hours.",
  parts=[
    ('a', "**Heart: 4 h (shortest).** Myocardium has high energy needs and little anaerobic reserve; normothermic machine perfusion can extend this."),
    ('b', "**Lungs: 4–6 h.** Many centres accept 6–8 h; ex-vivo lung perfusion extends it further."),
    ('c', "**Liver: 8–12 h.** Beyond about 12 h primary non-function and biliary injury become more likely."),
    ('d', "**Intestine: 8–12 h.** The mucosa is very sensitive to ischaemia; shorter times are preferred."),
    ('e', "**Pancreas: 12–18 h.** Longer times increase graft pancreatitis and thrombosis."),
    ('f', "**Kidney: 24 h (up to 36; longest).** Tubules tolerate cold best; delayed graft function rises with time, and machine perfusion helps."),
  ],
  mimic=[
    ("Cold vs warm ischaemia", "Warm ischaemia (from circulatory arrest to cold flush) is far more damaging per minute; it is the main problem in DCD."),
  ],
  traps=[
    ("“The liver tolerates cold ischaemia longest”", "The kidney does (24–36 h); the heart least (about 4 h)."),
  ],
  decode=[
    ("Organ with the shortest acceptable cold ischaemia time [pattern]", "Heart (about 4 h); longest: kidney (24–36 h)."),
  ],
  punch="Heart about 4 hours, lungs 4–6, liver and intestine 8–12, pancreas 12–18, kidney 24–36: heart shortest, kidney longest.",
)

FLAGS = {
  'DONOR-01': "a: comparison figures are dated — in 2024 Spain had 53.9 and the USA 49.7 deceased donors per million (ONT/Spanish Government, 2025); India about 0.8 is current. b: the amendment is the THO (Amendment) Act 2011 (tissues, required inquiry in ICU, substitute board members); the 2014 Rules put it into effect. ‘About 4 lakh die each year waiting’ is an estimate; the Health Ministry figure usually quoted is about 5 lakh a year.",
  'DONOR-02': "Card agrees with the 2023 AAN/AAP/CNS/SCCM guideline (≥36 °C, SBP ≥100); the guideline also requires MAP ≥75 in adults, 5 half-lives for depressants, and 24 h after rewarming if temperature was ≤35.5 °C. Linked Marrow key (post-OHCA, ‘neither TTM option indicated yet’) is disputed: AHA/ERC give temperature control to all comatose post-arrest patients. Drug-level cut-offs match published protocols (barbiturate <10 µg/mL; thiopentone <5 mg/L, ICSI 2025).",
  'DONOR-03': "Card correct. Marrow note adds what is taught here: posturing excludes brain death; spinal reflexes, sweating, tachycardia and normal BP without pressors are compatible.",
  'DONOR-04': "Step 5: the 2023 AAN/SCCM guideline requires PaCO₂ ≥60 AND ≥20 above baseline with pH <7.30; the card’s ‘or’ is the older adult wording. Apnoea testing on ECMO (asked twice by Marrow) is not on the card: sweep 0.2–1 L/min in the 2023 guideline (Marrow: 0.5–1 L/min + CPAP 10), VA-ECMO gases from both sites.",
  'DONOR-05': "c: the 2023 AAN/SCCM guideline no longer accepts EEG (or evoked potentials) as an ancillary test; accepted tests are 4-vessel catheter angiography, radionuclide perfusion scintigraphy and TCD (adults only). e: the guideline does not accept CTA or MRA as ancillary tests because they are not validated (stronger than ‘insufficient evidence’). Radionuclide perfusion scan not on the card. Linked DocT GT key (whole-brain PET as the supporting study) uses a test that is not a standard ancillary test.",
  'DONOR-06': "a: the Act’s board is the RMP in charge of the hospital, an independent nominated specialist, a neurologist or neurosurgeon, and the treating RMP; the 2011 proviso substitutes an independent surgeon or physician AND an anaesthetist or intensivist when no neurologist/neurosurgeon is available, none from the transplant team. b: correct for India (Form 10, 6 h in adults); the US 2023 guideline needs only one exam in adults (two, 12 h apart, in children). d (‘per your notes’) could not be verified; practice when donation is declined varies.",
  'DONOR-07': "Cushing’s triad also includes irregular/depressed respiration (asked by DocT GT and Marrow); the card gives only hypertension and bradycardia. Added as extra.",
  'DONOR-09': "Haemoglobin 10 g/dL (Hct 30%) is the old ‘rule of 100’: SCCM/ACCP/AOPO 2015 and Canadian 2020 use Hb >7 g/dL. Glucose 80–150 is tighter than SCCM (<180 mg/dL). Temperature: JHLT 2020 36–37 °C; Canadian 2020 34–35 °C only when thoracic organs are not retrieved (Niemann 2015 benefit for kidneys; a later trial found donor hypothermia inferior to kidney machine perfusion). Sodium 135–155: the >155 liver-graft link comes from older series.",
  'DONOR-12': "T4: the 2023 NEJM RCT (838 unstable potential heart donors, levothyroxine 30 µg/h vs saline) showed no increase in hearts transplanted (54.9% vs 53.2%) and more severe hypertension and tachycardia; routine thyroid hormone is no longer supported. Vasopressin 0.5–4 U/h exceeds the SCCM 2015 range (0.01–0.04 U/min = 0.6–2.4 U/h). Low-dose hydrocortisone is accepted by some guidelines as an alternative to methylprednisolone (observational evidence only).",
  'DONOR-14': "a: PEEP 5–10 is lower than the donor trial and JHLT 2020 (8–10 cmH₂O, PIP <35).",
  'DONOR-15': "b: Hct over 30% is dated; current guidelines transfuse below Hb 7 g/dL.",
  'DONOR-16': "‘HBsAg positive’ as absolute (per your notes) is dated: HBsAg-positive and HCV-positive organs are now used for matched or consenting recipients with antivirals (the card’s watch line says this). HIV is absolute in India, but HIV-positive-to-HIV-positive transplantation is permitted in the USA (HOPE Act) and South Africa.",
  'DONOR-17': "Table layout: the row ‘50–59 with 2 of: hypertension, creatinine >1.5, death from stroke’ is printed under the STANDARD column; it is an EXPANDED-criteria rule (UNOS 2002). A standard donor is any donor not meeting ECD criteria. The USA replaced ECD/SCD with KDPI in 2014.",
  'DONOR-18': "Lungs 4–6 h is conservative (many sources 6–8 h); otherwise standard. Card already marks these ranges as standard teaching.",
}
