# CVS07C — Explain v3 ("Learn" depth): neuroprognostication after cardiac arrest — when to prognosticate and what must be excluded first, the principles (no single test,
# false positive rate near zero, multimodal, open mind), clinical examination, EEG and SSEP N20, biomarkers (NSE, S-100B, NfL) and the NSE cut-off muddle, CT vs MRI, monitoring
# methods, and the algorithms: entry, the six ERC criteria, the overall route from an unresponsive patient, the brain death limb and the summary of routes.
# No mnemonics or hooks. Driven by qpack/CVS07C.md (9 question links on 6 cards; PCA-47, PCA-49 and PCA-54 asked twice each, PCA-50, PCA-53 and PCA-55 once; the GT1o day-6 question is
# linked to both PCA-49 and PCA-53). PCA-41, 42, 43, 44, 45, 46, 48, 51, 52 and 56 have no linked question and get short explanations with [pattern] decode items.
# No Top-up cards for this deck (cvs_topups.json has no CVS07C key). qbank.json has a `fix` for PCA-49 only (MRI 2–5 d ERC / 2–7 d AHA; the card has since been corrected to 2–7 d and
# repeat CT at 72–96 h). cvs_cardlayer.json `lines` and `cross` notes for PCA-47, 49, 50, 54 and 55 were read and used.
# Checked online on 19 Nov 2026:
#  - ERC–ESICM 2025 post-resuscitation care (Nolan, Intensive Care Med 2025;51:2213–2288, full text): consider prognostication in patients not awake and obeying commands (GCS motor <6) at
#    ≥72 h after ROSC; Table 1: algorithm entry extended to all unconscious patients, M ≤5 (2021 was M ≤3); poor outcome likely if ≥2 of: bilaterally absent pupillary AND corneal reflexes
#    ≥72 h (pupillometer if available); bilaterally absent N20 ≥24 h (time after ROSC does not affect SSEP specificity; can be recorded from day 1); highly malignant EEG (suppressed background
#    ± periodic discharges, burst suppression; ACNS terms) used only after 24 h; NSE >60 µg/L at 48 h and/or 72 h, serial samples 24/48/72 h, measure free haemoglobin and discard haemolysed
#    samples (red cells contain NSE); status myoclonus (continuous generalised myoclonus ≥30 min) within 72 h, record EEG during jerks; diffuse and extensive anoxic injury on CT/MRI:
#    marked GM/WM ratio reduction on CT (RCUK 2025 algorithm: at any time), repeat CT at 72–96 h if the first is negative and the patient still unconscious; extensive diffusion restriction on MRI at 2–7 days.
#    NfL, GFAP and tau NOT recommended (no consistent thresholds); S-100B not recommended. Awakening usually within the first days of ROSC (exact figure not re-verified in review), late awakening
#    still possible; propofol and other sedatives may need ≥24 h off; World Brain Death Project: examine after ≥5 elimination half-lives of the longest-acting drug; brain death in 5–10%
#    of those who die after conventional CPR. Indeterminate: observe and re-evaluate. Good-outcome signs: M 4–5 early, normal NSE, no DWI restriction, continuous normal-voltage EEG.
#  - ERC–ESICM 2021 (from the 2025 text and standard references): same six criteria, entry M ≤3 at ≥72 h, MRI at 2–5 days; temperature: fever prevention (>37.7 °C) for ≥72 h.
#  - AHA 2025 Part 11 Post-Cardiac Arrest Care (cpr.heart.org): multimodal, never a single finding (COR 1); delay until adequate time has passed (COR 1); consolidate at a minimum of 72 h after
#    normothermia (2a), typically ≥5 days after ROSC if hypothermic temperature control was used; absent pupillary light reflex ≥72 h, quantitative pupillometry ≥72 h, absent corneal
#    reflexes ≥72 h (all 2b); undifferentiated myoclonus uncertain; high NSE or NfL within 72 h (2b, new
#    for NfL), normal NSE within 72 h favourable (2b); status epilepticus continuing ≥72 h (2b); burst suppression off sedation ≥72 h (2b); bilaterally absent N20 at ≥48 h (2b); absent EEG
#    reactivity within 72 h should NOT be used (3); continuous EEG background without discharges within 72 h favourable (2b); reduced GWR on CT (2b, no timing); extensive restricted
#    diffusion or reduced ADC on MRI at 2–7 days (2b), absence at 2–7 days favourable (2b); organ donation considered in all who meet neurological criteria for death and before planned WLST (1).
#  - Westhall, Neurology 2016 (PMC4836886): highly malignant = suppressed background <10 µV for 100% of the recording without discharges, suppression with continuous periodic discharges,
#    burst-suppression (suppression <10 µV in >50%, 50–99%) ± discharges; malignant = periodic/rhythmic patterns, discontinuous, low-voltage (<20 µV), reversed gradient, unreactive; benign =
#    none of these. 103 patients, EEG at median 77 h: highly malignant in 37%, all poor outcome (specificity 100%, sensitivity 50%).
# From standard references without a fresh check (worded softly): World Brain Death Project 2020 (Greer, JAMA): coma, absent brainstem reflexes, apnoea at PaCO₂ ≥60 mmHg with pH <7.30 (or ≥20 above
# baseline), core temperature ≥36 °C, SBP ≥100 mmHg; AAN 2006 (Wijdicks) NSE >33 µg/L days 1–3 from the pre-cooling era; NfL is an axonal cytoskeletal protein; N20 is the cortical
# (primary somatosensory) response to median nerve stimulation.
# Second review (19 Nov 2026) re-checked: RCUK 2025 and 2021 neuroprognostication algorithms, AHA 2025 Part 11 web text and neuroprognostication diagram, Westhall 2016 abstract,
# Frontiers Med 2026 review of ERC–ESICM 2025, WBDP 2020 summaries (pH <7.30 with PaCO₂ ≥60; SBP ≥100 or MAP ≥60).
# Could not trace: the card’s ‘47’ NSE figure (PCA-48), the ‘around 50%’ CT oedema incidence (PCA-50) and the ‘5–10 days’ recovery window (PCA-43).

SPINE = [
  ("Wait, then exclude confounders", "Prognosis is not judged before 72 hours, and only once temperature, sedatives, glucose and CO₂ have been corrected, because each of them can make a recoverable brain look dead."),
  ("No single test, zero false positives", "A false prediction of poor outcome leads to withdrawal of care from someone who would have woken, so no test is used alone and the accepted false positive rate is close to zero."),
  ("Examination, EEG and SSEP", "Absent pupillary and corneal reflexes at 72 hours, a highly malignant EEG after 24 hours and bilaterally absent N20 are the clinical and electrical signs of devastating injury."),
  ("Biomarkers and imaging", "Serum NSE above 60 µg/L at 48–72 hours and diffuse anoxic injury on CT or diffusion MRI add evidence that sedatives cannot fake, but haemolysis and timing can."),
  ("The ERC algorithm", "An unconscious patient at 72 hours without confounders who has two or more of the six criteria is likely to have a poor outcome; with fewer, observe and re-evaluate."),
  ("Brain death is a different road", "If every brainstem reflex is absent the question is not prognosis but death by neurological criteria, which is declared under the World Brain Death Project rules and local law."),
]

PRIMER = "After ROSC most comatose survivors who die in hospital die because life-sustaining treatment is withdrawn on a prediction of poor neurological outcome, so the prediction itself decides survival. Neuroprognostication is therefore about avoiding a false positive: calling poor outcome in a patient who would have recovered. ‘Comatose’ or ‘unconscious’ here means not obeying commands, a Glasgow Coma Scale motor score below 6. ‘Poor outcome’ in the studies means death, vegetative state or severe disability (CPC 3–5, or mRS 4–6)."

L = {}

L['PCA-41'] = dict(
  sub="Neuroprognostication → Timing → How long to wait",
  step=1,
  intro="Step 1 starts with the clock. Prognosis is never judged on day 1, because cooling, sedatives and the brain’s own early recovery all make the first days misleading. No question is linked; the exam asks the 72-hour figure and what it is counted from.",
  parts=[
    ('a', "**After TTM, wait 72 hours for neuroprognostication.** Hypothermia slows the clearance of sedatives and opioids, and the stunned brain can take days to show what it will become, so tests read too early give false-poor results."),
    ('b', "**Give adequate time after ROSC: 72 hours after euthermia.** Two clocks now exist. AHA 2025 says consolidate prognosis at least 72 h after normothermia, which is typically 5 days or more after ROSC if the patient was cooled. ERC–ESICM 2025 counts 72 h or later from ROSC, provided confounders are excluded. The safe exam answer is whichever is later; with fever prevention alone the two coincide."),
    ('c', "**ERC/ESICM 2021: emphasis on PCI in OHCA, TTM at 36 °C, neurological assessment after sufficient time and multimodality, rehabilitation and post-discharge care.** The ‘36 °C’ point is out of date: ERC–ESICM 2021 recommended only active fever prevention (above 37.7 °C) for at least 72 h, and 2025 says ≤37.5 °C for 36–72 h (CVS07B, PCA-28/29)."),
  ],
  mimic=[
    ("72 h after ROSC vs 72 h after normothermia", "ERC–ESICM counts from ROSC; AHA counts from normothermia and sedation off. After 24 h at 33 °C and rewarming, the AHA clock ends about 2 days later."),
  ],
  traps=[
    ("“Prognosticate at 24 h if the patient is still in coma”", "Too early: only EEG patterns and N20 can be used from 24 h, and only as part of a ≥72 h decision."),
  ],
  decode=[
    ("[pattern] Earliest time to make a neuroprognostic decision after cardiac arrest", "At least 72 h (after ROSC per ERC–ESICM; after normothermia per AHA), and later if confounders persist."),
  ],
  punch="Do not decide on prognosis before 72 hours, and if the patient was cooled or sedated, count from normothermia and sedation off; when in doubt, wait longer.",
)

L['PCA-42'] = dict(
  sub="Neuroprognostication → Principles → No single test, zero false positives",
  step=2,
  intro="Step 2 is the attitude behind every test. The cost of a false prediction is withdrawal of care from a patient who would have recovered, and the deciding doctor can never see that patient’s recovery. No question is linked.",
  parts=[
    ('a', "**Complex, especially with TTM and the drugs used.** Cooling slows drug metabolism, and propofol, midazolam, opioids and neuromuscular blockers all suppress the exact signs being examined (motor response, reflexes, EEG background)."),
    ('b', "**Avoid a pessimistic prediction attitude; examine with an open mind.** The self-fulfilling prophecy: if poor outcome is predicted and care withdrawn, the patient dies, and the study counts this as a ‘true’ prediction. This bias inflates the apparent accuracy of every predictor."),
    ('c', "**No one test singularly predicts poor outcome; the false positive rate should be 0 with a narrow 95% CI.** Zero is the ideal. In practice ERC–ESICM accepted predictors with a false positive rate below 5% and a narrow confidence interval (PCA-43), and makes up for the residual error by needing two of them (PCA-53). A narrow CI matters because a 0% rate from 30 patients can still hide a real rate of 10%."),
    ('d', "**Use multi-modal testing; more sensitive, though evidence is limited.** Combining independent tests catches more patients with poor outcome and makes it less likely that one confounded test drives the decision."),
    ('e', "**In doubt, consider prolonged repeated observation.** Patients who meet no criterion are indeterminate, not ‘good’; ERC–ESICM 2025 says observe and re-evaluate, and some of them do wake late."),
  ],
  mimic=[
    ("Specificity vs false positive rate", "False positive rate = 1 − specificity: the share of patients who recover yet test ‘poor’. The guideline target is on this, not on sensitivity."),
  ],
  traps=[
    ("“A single highly specific test such as absent N20 is enough to withdraw care”", "Every guideline requires a multimodal decision; ERC–ESICM needs at least two criteria."),
  ],
  decode=[
    ("[pattern] Most important statistical property of a test used to predict poor outcome after arrest", "A false positive rate close to 0 with a narrow 95% CI, not high sensitivity."),
  ],
  punch="Because a false positive means withdrawing care from someone who would have woken, no test is used alone and the acceptable false positive rate is near zero; when unsure, keep observing.",
)

L['PCA-43'] = dict(
  sub="Neuroprognostication → Principles → Confounders, entry and most robust predictors",
  step=1,
  intro="Step 1 again: before any test is read, the patient must be free of the four reversible things that mimic brain injury. No question is linked; the card mixes the current entry criterion with the older stepwise approach.",
  parts=[
    ('a', "**Most patients improve in 5–10 days, rarely after that.** ERC–ESICM 2025 puts it more precisely: most patients who wake do so within the first few days after ROSC, but late awakening (often from slow clearance of sedatives, especially with renal or hepatic failure) is well described, and the chance of waking falls the longer coma lasts. The ‘5–10 days’ is the chapter’s figure, not a guideline number."),
    ('b', "**No major confounders: temperature, drugs, sugar, PCO₂.** Hypothermia, residual sedatives or paralysis, hypo- or hyperglycaemia and hyper- or hypocapnia all depress consciousness reversibly. Residual sedation is the one that catches people out, especially with renal or hepatic failure; ERC–ESICM notes sedatives may need to be off for at least 24 h. Severe hypotension, sodium, uraemia and sepsis count too."),
    ('c', "**Use an algorithm, for post-arrest comatose patients with GCS motor ≤5 (not obeying commands) at ≥72 h: ERC–ESICM 2025; was ≤3 in 2021.** The 2025 change widens entry to every patient not obeying commands; M 4–5 early is itself a sign of possible recovery, so these patients rarely meet two criteria."),
    ('d', "**Start with the most robust predictors first (FPR <5% with narrow 95% CI): pupillary reflex and SSEP (bilateral N20).** This stepwise ‘robust first’ order is the 2015 ERC–ESICM algorithm. Since 2021 there is no hierarchy: any two of the six criteria are enough (PCA-53). Absent pupillary reflexes and absent N20 remain the most specific signs."),
    ('e', "**Then: status myoclonus, EEG, NSE.** In 2015 these were the ‘less robust’ group; they are now criteria of equal weight, with imaging the sixth."),
  ],
  mimic=[
    ("2015 stepwise algorithm vs 2021/2025 algorithm", "2015: robust predictors first, then others. 2021/2025: two or more of six criteria, with no order."),
  ],
  traps=[
    ("“Only M ≤3 patients enter prognostication”", "That was 2021; ERC–ESICM 2025 includes M ≤5, i.e. anyone not obeying commands (PCA-52)."),
  ],
  decode=[
    ("[pattern] Which factor must be excluded before neuroprognostication? (options: sedation, hypothermia, hypoglycaemia, hypercapnia)", "All of them; residual sedation is the one most often missed."),
  ],
  punch="Exclude temperature, drugs, glucose and CO₂ as causes of coma first, then apply the algorithm to anyone not obeying commands at 72 hours; the ‘robust predictors first’ order is the 2015 version.",
)

L['PCA-44'] = dict(
  sub="Neuroprognostication → Clinical examination → Components",
  step=3,
  intro="Step 3 starts at the bedside. Examination is cheap and repeatable but is the part most distorted by sedatives and paralysis, so only the most specific findings count. No question is linked.",
  parts=[
    ('a', "**GCS and motor response.** Absent or extensor motor response at 72 h is sensitive but has a high false positive rate, so ERC–ESICM uses it only as the entry gate (M ≤5), not as a criterion. AHA 2025 says withdrawal motor response or better supports a good outcome."),
    ('b', "**Pupillary reflex, absent at 72 hours, indicates poor outcome.** The pupillary light reflex needs an intact midbrain; bilateral absence at ≥72 h is very specific. Quantitative pupillometry (NPi) is recommended because the eye can miss a small, slow reaction."),
    ('c', "**Corneal reflex.** Less specific than the pupil because opioids and neuromuscular blockers can abolish it; that is why the ERC criterion needs pupillary AND corneal absence together (PCA-53)."),
    ('d', "**Status myoclonus.** Continuous generalised myoclonus for at least 30 minutes, within 72 h (ERC–ESICM 2025); record an EEG during the jerks, because some myoclonus (Lance–Adams) is compatible with recovery."),
    ('e', "**Status epilepticus.** AHA 2025: status epilepticus continuing at ≥72 h supports poor outcome; isolated seizures have uncertain value."),
  ],
  mimic=[
    ("Status myoclonus vs Lance–Adams syndrome", "Status myoclonus is early, continuous and generalised in deep coma with a malignant EEG; Lance–Adams is later action myoclonus in a patient who is waking."),
  ],
  traps=[
    ("“Preserved pupillary reflexes mean a good outcome”", "AHA 2025 lists only absent reflexes, as a predictor of poor outcome; preserved reflexes are not a favourable sign, because many patients with intact brainstem reflexes still have severe cortical injury."),
  ],
  decode=[
    ("[pattern] Clinical sign at 72 h with the highest specificity for poor outcome", "Bilaterally absent pupillary light reflex (ideally confirmed by pupillometry)."),
  ],
  punch="Of the examination findings, bilaterally absent pupillary reflexes at 72 hours are the most specific; motor response decides who enters the algorithm, not who has a poor outcome.",
)

L['PCA-45'] = dict(
  sub="Neuroprognostication → EEG → Recording and malignant patterns",
  step=3,
  intro="Step 3, the electrical picture. EEG shows how much cortex is working and catches seizures, but sedatives suppress it, so the timing and the exact pattern matter. No question is linked.",
  parts=[
    ('a', "**Continuous EEG is useful; at least daily EEG if the patient is not waking up.** ERC–ESICM 2025: EEG from day 1, routine or continuous, to detect seizures and to prognosticate. Continuous recording shows how the background evolves, which a single snapshot cannot."),
    ('b', "**Patterns: responsive or unresponsive, status epilepticus, periodic waveforms (burst suppression).** Westhall’s standardised classification (Neurology 2016) is what the guideline means by ‘highly malignant’: a suppressed background (<10 µV throughout) with or without periodic discharges, or burst-suppression (suppression in more than half the recording). In Westhall’s 103 patients (EEG at a median of 77 h), 37% had a highly malignant EEG and all of them had a poor outcome: specificity 100%, sensitivity 50%."),
    ('c', "**Poor prognosis on EEG: unequivocal seizures at 72 hours, absence of background activity. AHA 2025 addition, a favourable predictor: a continuous EEG background without discharges within 72 h supports a good prognosis.** ERC–ESICM 2025 uses highly malignant patterns only after 24 h, because earlier suppression may be drug or cooling effect. AHA 2025 counts burst suppression only off sedation at ≥72 h and says absent EEG reactivity within 72 h should not be used."),
  ],
  table=dict(title="Westhall EEG categories after cardiac arrest", head=["Category", "Patterns", "Meaning"], rows=[["Highly malignant", "**Suppressed background (<10 µV) ± periodic discharges; burst-suppression**", "Poor outcome (an ERC criterion after 24 h)"], ["Malignant", "Periodic or rhythmic patterns; discontinuous, low-voltage or unreactive background", "Sensitive, not specific: not a criterion alone"], ["Benign", "None of the above; continuous, normal voltage", "Supports recovery"]]),
  mimic=[
    ("Absent background vs absent reactivity", "Absent background (suppression) is a criterion; absent reactivity alone is not (AHA 2025, COR 3)."),
  ],
  traps=[
    ("“Any seizure on post-arrest EEG means poor outcome”", "AHA 2025: the prognostic value of seizures is uncertain; status epilepticus persisting at ≥72 h is what counts."),
  ],
  decode=[
    ("[pattern] EEG pattern after 24 h that predicts poor outcome", "Suppressed background with or without periodic discharges, or burst suppression (highly malignant, Westhall)."),
  ],
  punch="A suppressed or burst-suppressed EEG after 24 hours off the effect of drugs predicts poor outcome, while a continuous background without discharges within 72 hours now counts for the patient.",
)

L['PCA-46'] = dict(
  sub="Neuroprognostication → SSEP → N20",
  step=3,
  intro="Step 3’s most specific electrical test. The N20 is the cortical response to median nerve stimulation; if it is gone on both sides, the somatosensory cortex has died. No question is linked.",
  parts=[
    ('a', "**Bilateral absence of the N20 wave indicates a poor sign.** Stimulating the median nerve at the wrist produces peripheral (Erb’s point) and cervical responses, then the N20 over the primary somatosensory cortex about 20 ms later. If the peripheral and cervical waves are present but N20 is absent bilaterally, the signal reaches the brain but the cortex does not respond. Unilateral absence may be technical or focal. Sedatives barely affect N20, which is why it is so specific; noise from muscle activity can hide it, and paralysis improves the recording. ERC–ESICM 2025 accepts it at ≥24 h (specificity is not time-dependent); AHA 2025 says ≥48 h."),
  ],
  mimic=[
    ("Absent N20 vs absent pupils", "Both are the most specific signs; N20 is less affected by drugs, pupils need no equipment."),
  ],
  traps=[
    ("“A present N20 predicts good outcome”", "A preserved N20 does not predict recovery: many patients with a present N20 still have a poor outcome, because the test is highly specific but has low sensitivity."),
  ],
  decode=[
    ("[pattern] Single most specific test for poor outcome after cardiac arrest", "Bilaterally absent N20 on SSEP."),
  ],
  punch="Bilaterally absent N20 with preserved peripheral responses means the cortex is not receiving the signal and is one of the most specific predictors; one side alone does not count.",
)

L['PCA-47'] = dict(
  sub="Neuroprognostication → Biomarkers → NSE, S-100B and NfL",
  step=4,
  intro="Step 4 turns to blood tests, the one modality that sedatives and paralytics cannot fake. Both GT5 questions test the cell each marker comes from and what else raises it.",
  parts=[
    ('a', "**NSE is released following injury from neurones; S-100B from glial tissue.** Neurone-specific enolase is a glycolytic enzyme in neuronal cytoplasm, so it leaks when neurones die. S-100B is a calcium-binding protein of astrocytes. NSE is also present in red cells and platelets, which is why haemolysis raises it falsely; ERC–ESICM 2025 says measure free haemoglobin and discard haemolysed samples (relevant on ECMO)."),
    ('b', "**NSE is better studied.** It is the only biomarker in the ERC–ESICM algorithm (PCA-53). ERC–ESICM 2025 does not recommend S-100B, because thresholds are inconsistent."),
    ('c', "**Not influenced by sedatives and NMBD.** This is their value: the clinical examination and most of the EEG are confounded by exactly those drugs (PCA-43)."),
    ('d', "**Tested at 24 hours and 72 hours.** ERC–ESICM 2025 advises serial samples at 24, 48 and 72 h; the threshold in the algorithm is read at 48 and/or 72 h (PCA-48)."),
    ('e', "**Serial increasing values are a better predictor than a single value. AHA 2025 addition: neurofilament light chain (NfL) is now included as a serum biomarker for neuroprognostication.** A rise from 24 to 48 h means continuing neuronal death; a falling value suggests a one-off release or haemolysis. NfL is a cytoskeletal protein of large myelinated axons, so it marks axonal injury (GT5 boxer question). AHA 2025 allows high NSE or NfL within 72 h (COR 2b), but ERC–ESICM 2025 does not recommend NfL yet because no consistent threshold exists."),
  ],
  table=dict(title="Brain injury biomarkers", head=["Marker", "Source", "Note"], rows=[["NSE", "**Neuronal cytoplasm** (also red cells, platelets)", "Haemolysis raises it falsely; ERC criterion >60 µg/L"], ["S-100B", "**Astrocytes (glia)**", "Not recommended (ERC–ESICM 2025)"], ["NfL", "**Axons** (large myelinated)", "AHA 2025: yes; ERC–ESICM 2025: not yet"], ["GFAP", "Astrocytes", "Not recommended"]]),
  mimic=[
    ("NSE vs NfL", "NSE: neuronal cell body, falsely raised by haemolysis. NfL: axonal structure, also raised in traumatic and neurodegenerative injury."),
  ],
  traps=[
    ("“Raised NfL in a boxer means glial scarring or blood-brain barrier closure”", "NfL is axonal; glial injury is S-100B or GFAP (GT5, 69% right)."),
    ("“S-100B is the biomarker falsely raised by haemolysis”", "It is NSE, because red cells contain enolase (GT5, 71% right)."),
  ],
  decode=[
    ("Raised CSF neurofilament light chain after repeated bouts suggests? [DocT GT]", "Axonal injury (69% right)."),
    ("Neuronal injury marker known for false positives from haemolysis? [DocT GT]", "NSE (71% right)."),
  ],
  punch="NSE comes from neurones (and red cells, so haemolysis fakes it), S-100B from glia and NfL from axons; biomarkers are useful because no drug alters them, and a rising series counts more than one value.",
)

L['PCA-48'] = dict(
  sub="Neuroprognostication → Biomarkers → The NSE cut-off conflict",
  step=4,
  intro="Step 4, the number to quote. NSE thresholds vary with the assay, the timing and the population, so different sources give different figures. No question is linked; the exam number is the ERC one.",
  parts=[
    ('a', "**Biomarkers section: 33 vs 47, from different studies.** 33 µg/L is the older AAN 2006 figure from the era before cooling, when it was set at days 1–3; later cohorts treated with temperature control needed higher thresholds to keep false positives near zero."),
    ('b', "**Reasons for the discrepancy: different technique, other sources of the marker, kinetics not clear.** Assays differ between laboratories; red cells and platelets add NSE (haemolysis, PCA-47); and the peak timing varies between patients."),
    ('c', "**ERC algorithm: NSE >60 at 48 h and/or 72 h.** This is the guideline figure in both 2021 and 2025."),
    ('d', "**The unit: NSE is reported in micrograms per litre (µg/L), not mg/L.** A threshold printed in mg/L is out by a factor of a thousand."),
  ],
  mimic=[
    ("High NSE vs normal NSE", "NSE >60 µg/L at 48–72 h supports poor outcome; a normal NSE (around 17 µg/L or less) within 72 h supports a good outcome (AHA 2025, ERC–ESICM 2025)."),
  ],
  traps=[
    ("“NSE >33 µg/L at 24 h predicts poor outcome”", "An older, pre-cooling figure; the current threshold is >60 µg/L at 48 and/or 72 h."),
  ],
  decode=[
    ("[pattern] NSE threshold and timing in the ERC–ESICM algorithm", ">60 µg/L at 48 h and/or 72 h."),
  ],
  punch="Quote NSE >60 µg/L at 48 and/or 72 hours as the guideline figure; older lower figures come from different assays and an era before temperature control.",
)

L['PCA-49'] = dict(
  sub="Neuroprognostication → Imaging → CT vs MRI",
  step=4,
  intro="Step 4, imaging. CT shows swelling, MRI shows dying cells, and each has a window. The GT1o day-6 question (41% right) is keyed on MRI, and GT6 asks the MRI day window.",
  parts=[
    ('a', "**MRI is more sensitive.** Diffusion-weighted imaging detects cytotoxic oedema (cells swelling as their ion pumps fail) before the tissue changes density on CT."),
    ('b', "**DWI, measure ADC.** Restricted diffusion appears bright on DWI and dark on the ADC map; a low ADC confirms true restriction rather than T2 ‘shine-through’. AHA 2025 accepts extensive restricted diffusion or reduced ADC at 2–7 days."),
    ('c', "**Hyperintensity in cortex and basal ganglia.** The cortex (especially occipital and the perirolandic areas), basal ganglia, thalamus and hippocampus have the highest metabolic demand and fail first. GT1o’s key is ‘MRI can assist, and the cortex is the most commonly affected area’."),
    ('d', "**MRI at 2–7 days after arrest; early CT can show reduced grey-white ratio; if the first CT is normal and the patient is still unconscious, repeat at 72–96 h.** Before day 2 diffusion changes may not have appeared fully; after about a week the ADC pseudo-normalises and injury is underestimated. AHA 2025 and ERC–ESICM 2025 both use 2–7 days; ERC–ESICM 2021 said 2–5 days. The repeat CT at 72–96 h is ERC–ESICM 2025."),
  ],
  mimic=[
    ("CT vs MRI after arrest", "CT: early, quick, shows oedema and lost grey-white ratio, low sensitivity early. MRI: 2–7 days, more sensitive, shows cytotoxic injury."),
  ],
  traps=[
    ("“EEG is the most accurate prognostic test” (GT1o option A)", "No single test is ‘the most accurate’; bilateral absent N20 is the most specific one."),
    ("“No corneal responses at day 6 means no recovery” (option B)", "Corneal absence alone is not enough: ERC needs absent pupillary AND corneal reflexes plus a second criterion."),
    ("“NSE can be used at day 6” (option C)", "The guideline threshold is set for 48 h and/or 72 h; a day-6 value is outside the window the cut-off was validated for, and temperature control can alter NSE kinetics, so ‘not affected by cooling’ is also too strong."),
    ("“MRI immediately after arrest” or ‘days 2–5 only’ (GT6)", "Too early shows nothing. DocT keys days 3–7 (69% right). The 2025 guidelines say 2–7 days; 2–5 days is ERC–ESICM 2021. Pick 2–7 if offered. With these four options, pick DocT’s 3–7 (inside the current 2–7 window); choose 2–5 only if the stem is explicitly framed on ERC–ESICM 2021."),
  ],
  decode=[
    ("Post-arrest day 6, limited recovery: which is most correct? [DocT GT]", "MRI can assist with prognosis, and the cortex is the most commonly affected region (41% right)."),
    ("On what day is MRI brain advised after cardiac arrest? [DocT GT]", "Key: days 3–7 (69% right); guideline window 2–7 days."),
  ],
  punch="CT is early and shows swelling; diffusion MRI at 2–7 days is more sensitive and shows restriction in the cortex and basal ganglia; repeat a normal early CT at 72–96 hours if the patient is still unconscious.",
)

L['PCA-50'] = dict(
  sub="Neuroprognostication → Imaging → CT findings",
  step=4,
  intro="Step 4, what the CT shows. Global hypoxia swells the grey matter until it looks like white matter. The Marrow hanging question tests what that means for management.",
  parts=[
    ('a', "**Cerebral oedema: around 50% incidence.** Reported rates vary widely with how long after arrest the CT is done; early CT is often normal, which is why a negative first scan is repeated (PCA-49)."),
    ('b', "**Attenuation of the grey-white matter interface.** Grey matter (cortex, basal ganglia) uses more energy, so it swells first; its density falls towards that of white matter, the boundary fades and sulci and cisterns efface. A reduced grey-white ratio is the measurable form; ERC–ESICM 2025 uses a marked reduction, and repeats a normal early CT at 72–96 h if the patient is still unconscious."),
  ],
  mimic=[
    ("Global anoxic injury vs focal stroke or haematoma", "Anoxic injury is diffuse and symmetrical with no mass to remove; a focal lesion may have a surgical answer."),
  ],
  traps=[
    ("“Neurosurgical consult” for diffuse loss of grey-white differentiation after hanging", "There is no surgical target; the step is multimodal prognostication and counselling the family (Marrow)."),
  ],
  decode=[
    ("Hanging, GCS 3, CT loss of grey-white differentiation: diagnosis and step? [Marrow]", "Anoxic brain injury; family education and prognostication, not surgery."),
  ],
  punch="Diffuse loss of grey-white differentiation on CT means global anoxic injury with nothing to operate on, so the response is prognostication and honest discussion with the family.",
)

L['PCA-51'] = dict(
  sub="Neuroprognostication → Monitoring → Matching changes to methods",
  step=3,
  intro="Step 3, the wider monitoring picture. Each post-arrest change in the brain has a tool that detects it; only EEG and SSEP are part of the guideline algorithm. No question is linked.",
  parts=[
    ('a', "**Electrical phenomena (N20, SSEPs): EEG.** EEG and evoked potentials measure cortical function directly (PCA-45, PCA-46)."),
    ('b', "**ICP becoming high pressure: ICP monitoring.** Diffuse oedema after arrest can raise ICP, though invasive monitoring is rarely used here."),
    ('c', "**Normoxia becoming hypoxia: brain oxygen monitoring.** Brain tissue oxygen (PbtO₂) or near-infrared spectroscopy shows whether supply meets demand."),
    ('d', "**Balanced metabolism becoming metabolic imbalance: metabolic tracing.** After reperfusion, neurones shift towards anaerobic glycolysis and release excitatory glutamate; trends in glucose, lactate and glutamate (on microdialysis, or FDG-PET in research) track this. It is a research and neurocritical-care tool, not part of the prognostic algorithm."),
    ('e', "**Mitochondrial function, measured by the lactate:pyruvate ratio: microdialysis.** A high lactate:pyruvate ratio with normal oxygen points to mitochondrial failure rather than lack of supply."),
  ],
  mimic=[
    ("Raised lactate:pyruvate ratio: ischaemia vs mitochondrial dysfunction", "Low pyruvate and low tissue oxygen mean ischaemia; normal or high pyruvate with adequate oxygen means mitochondrial failure."),
  ],
  traps=[
    ("“Microdialysis measures oxygen”", "It samples extracellular metabolites (lactate, pyruvate, glucose, glutamate); oxygen needs a PbtO₂ probe."),
  ],
  decode=[
    ("[pattern] Monitoring method for mitochondrial dysfunction in brain injury", "Cerebral microdialysis, lactate:pyruvate ratio."),
  ],
  punch="Each brain change has its monitor: EEG for electrical activity, ICP probes for pressure, oxygen probes for hypoxia and microdialysis for mitochondrial function through the lactate:pyruvate ratio.",
)

L['PCA-52'] = dict(
  sub="Neuroprognostication → ERC algorithm → Entry conditions",
  step=5,
  intro="Step 5 opens the ERC algorithm. Four conditions must all be true before the six criteria are applied; each closes off a way a recoverable brain might be misjudged. No question is linked.",
  parts=[
    ('a', "**Resuscitation from cardiac arrest.** The criteria were validated in post-anoxic coma; trauma, stroke and drug coma have different courses."),
    ('b', "**Targeted temperature management and rewarming complete.** Cooling slows drug clearance and suppresses EEG and reflexes."),
    ('c', "**Unconscious patient, M ≤5 at ≥72 hours (ERC–ESICM 2025; was M ≤3 in 2021).** Anyone not obeying commands now enters, so fewer patients are left out of a structured assessment."),
    ('d', "**Without confounders.** Sedation, paralysis, hypothermia, severe hypotension, hypoglycaemia, and metabolic or respiratory derangements (PCA-43)."),
  ],
  mimic=[
    ("Algorithm entry vs brain death testing", "Entry to prognosis needs some brainstem function; absence of all brainstem reflexes sends the patient to brain death testing instead (PCA-54)."),
  ],
  traps=[
    ("“Entry needs GCS motor ≤3”", "That is 2021; 2025 is M ≤5."),
  ],
  decode=[
    ("[pattern] Entry condition to the ERC–ESICM 2025 prognostication algorithm", "Unconscious (M ≤5) at ≥72 h after ROSC, rewarmed, confounders excluded."),
  ],
  punch="The ERC algorithm applies only to a post-arrest patient who has been rewarmed, is still not obeying commands at 72 hours (M ≤5 since 2025) and has no confounders.",
)

L['PCA-53'] = dict(
  sub="Neuroprognostication → ERC algorithm → The six criteria",
  step=5,
  intro="Step 5’s core. Six independent signs, each with its own time, and two are needed. The GT1o day-6 question (41% right) tests this card: corneal absence alone, and EEG as ‘the best test’, were the wrong choices.",
  parts=[
    ('a', "**No pupillary AND corneal reflex at ≥72 h.** Both together; the corneal reflex alone is too easily lost to opioids and paralysis. ERC–ESICM recommends a pupillometer when available."),
    ('b', "**Bilaterally absent N20 SSEP at ≥24 h.** Specificity is not affected by time after ROSC (PCA-46); AHA 2025 says ≥48 h."),
    ('c', "**Highly malignant EEG at >24 h (suppressed background ± periodic discharges, or burst suppression).** After 24 h, because earlier suppression may still be drug or cooling effect (PCA-45)."),
    ('d', "**NSE >60 at 48 h and/or 72 h.** In µg/L (PCA-48)."),
    ('e', "**Status myoclonus ≤72 h.** The only criterion defined by early appearance: continuous generalised myoclonus of at least 30 minutes within 72 h; record EEG during it."),
    ('f', "**Diffuse and extensive anoxic injury on brain CT/MRI.** A marked reduction in grey-white ratio on CT (repeated at 72–96 h if the first scan was normal), or extensive diffusion restriction on MRI at 2–7 days (PCA-49)."),
    ('g', "**At least 2 required: yes, poor outcome likely; no, observe and re-evaluate.** Two independent signs make it very unlikely that one confounded test drives a withdrawal decision; ‘likely’, not ‘certain’."),
  ],
  table=dict(title="ERC–ESICM criteria and their timing", head=["Criterion", "Timing"], rows=[["Pupillary AND corneal reflexes absent", "**≥72 h**"], ["Bilateral absent N20", "**≥24 h**"], ["Highly malignant EEG", "**>24 h**"], ["NSE >60 µg/L", "**48 h and/or 72 h**"], ["Status myoclonus", "**≤72 h** (within)"], ["Diffuse anoxic injury", "CT within 72 h; MRI 2–7 days"]]),
  mimic=[
    ("Poor outcome ‘likely’ vs brain death", "Two criteria give a probability that permits a WLST discussion; brain death is a declaration of death (PCA-56)."),
  ],
  traps=[
    ("“EEG is the most accurate test” (GT1o)", "No single test decides; absent N20 is the most specific."),
    ("“Absent corneal responses at day 6 mean no recovery” (GT1o)", "It needs pupillary absence too, and a second criterion."),
  ],
  decode=[
    ("Day 6 after VF arrest and 24 h cooling, limited recovery: which statement is most correct? [DocT GT]", "MRI can assist with prognosis, the cortex being most often affected (41% right)."),
  ],
  punch="Poor outcome is likely when two of six criteria are met: absent pupillary and corneal reflexes at 72 hours, absent N20 from 24 hours, a highly malignant EEG after 24 hours, NSE above 60 at 48–72 hours, status myoclonus within 72 hours, or diffuse anoxic injury on imaging.",
)

L['PCA-54'] = dict(
  sub="Neuroprognostication → Algorithm → Route from the unresponsive patient",
  step=6,
  intro="Step 6 lays out the whole road from ROSC, of which prognostication is only one branch. Both Marrow questions sit on it: residual sedation, and donation after circulatory death.",
  parts=[
    ('a', "**Unresponsive patient after ROSC: suspected neurological cause of arrest?** Subarachnoid haemorrhage, stroke or trauma can cause the arrest; finding it changes everything that follows."),
    ('b', "**Yes: brain CT.** Before temperature control, to find a lesion that needs a different treatment."),
    ('c', "**No: TTM, then unresponsive after rewarming, then exclude confounders, particularly residual sedation.** Temperature control goes to every comatose survivor; sedation delays the examination, not the cooling."),
    ('d', "**All brainstem reflexes absent? Pupillary, corneal, oculocephalic, cough.** These test the midbrain, pons and medulla in turn."),
    ('e', "**Yes: brain death pathway. No: neuroprognostication, WLST at any time, then evaluate for organ donation; circulatory death at any time, then evaluate for organ donation.** AHA 2025 (COR 1): consider organ donation in every patient who meets brain death criteria and before planned WLST. Donation after circulatory death: the treating team withdraws treatment, circulatory death follows, a no-touch period of a few minutes, then retrieval; the donation team never leads the WLST decision."),
  ],
  mimic=[
    ("Donation after brain death vs after circulatory death", "Brain death donors are dead by neurological criteria with the heart beating; circulatory death donors die after planned WLST."),
  ],
  traps=[
    ("“Comatose on propofol and fentanyl with pinpoint pupils: neither temperature control option is indicated yet” (Marrow key)", "Disputed: AHA and ERC give temperature control to all comatose survivors. Sedation delays prognosis and brain death testing, not temperature control. If asked about starting temperature control, start it; if about prognosis, wait for sedation to clear."),
    ("“The donation team should lead the withdrawal discussion”", "WLST is decided and carried out by the treating team; donation is raised separately."),
  ],
  decode=[
    ("Post-OHCA on propofol/fentanyl, GCS 3T, pinpoint pupils: what next? [Marrow]", "Key ‘neither TTM option yet’ (disputed); the real point is that sedation must clear before any neurological judgement."),
    ("Severe TBI, not brain dead, family requests withdrawal: management? [Marrow]", "Offer donation after circulatory death."),
  ],
  punch="Suspect a neurological cause and scan first; otherwise control temperature, rewarm and clear sedation, then check the brainstem: all reflexes absent leads to brain death testing, some present to prognostication, and organ donation is considered on every branch.",
)

L['PCA-55'] = dict(
  sub="Neuroprognostication → Algorithm → Brain death limb",
  step=6,
  intro="Step 6, the other road. When the whole brain including the brainstem has stopped working, the question is no longer outcome but death. Marrow asks which criteria can declare it.",
  parts=[
    ('a', "**Signs of brain death: fixed dilated pupils, diabetes insipidus, cardiovascular changes.** Hypothalamic and posterior pituitary failure stops ADH release, so polyuria and hypernatraemia follow; loss of brainstem control causes a catecholamine surge, then vasoplegia and hypotension."),
    ('b', "**CT: severe cerebral oedema and brainstem herniation.** This is the CT that turns the question from prognosis to brain death testing."),
    ('c', "**Follow the World Brain Death Project recommendations.** The 2020 consensus: coma of known irreversible cause, absent brainstem reflexes and a positive apnoea test (no breathing when PaCO₂ reaches ≥60 mmHg with pH <7.30, or ≥20 mmHg above baseline in chronic CO₂ retainers), after prerequisites (core temperature ≥36 °C, systolic ≥100 mmHg or MAP ≥60 mmHg, no confounding drugs, at least five half-lives of the longest-acting sedative). Spinal reflexes may persist. EEG and blood-flow studies are ancillary, used when the clinical examination cannot be completed."),
    ('d', "**Brain death confirmed according to local legislation.** The criteria are international; the declaration is local (in India, under the Transplantation of Human Organs Act, by a board of doctors)."),
    ('e', "**Evaluate for organ donation.** AHA 2025, COR 1."),
  ],
  mimic=[
    ("Brain death vs locked-in syndrome", "Locked-in patients are conscious with vertical eye movements and blinking preserved; a ventral pontine lesion, not loss of the whole brain."),
  ],
  traps=[
    ("“An isoelectric EEG is required to declare brain death”", "The diagnosis is clinical; EEG is ancillary. Marrow’s key (isoelectric EEG, absent brainstem reflexes, positive apnoea test) lists what can be used, not what is mandatory."),
    ("“Preserved spinal reflexes exclude brain death”", "They may persist because the spinal cord is intact."),
  ],
  decode=[
    ("Which criteria can be used to declare brain death? [Marrow]", "Absent brainstem reflexes and a positive apnoea test in coma, with isoelectric EEG as an ancillary test."),
  ],
  punch="Brain death is a clinical diagnosis of coma, absent brainstem reflexes and a positive apnoea test once confounders are excluded; diabetes insipidus is one of its signs, EEG is ancillary and the declaration follows local law.",
)

L['PCA-56'] = dict(
  sub="Neuroprognostication → Summary → Which route applies",
  step=6,
  intro="Step 6’s summary: four findings, four routes. The difference between them is the point; no question is linked.",
  parts=[
    ('a', "**Suspected neurological cause: brain CT first, not TTM first.** A bleed or stroke needs its own treatment."),
    ('b', "**All brainstem reflexes absent: brain death determination.** This is a test for death, not a prognosis."),
    ('c', "**Reflexes present, M ≤3 at ≥72 h, no confounders: ERC prognostication algorithm (the six criteria).** M ≤3 is the 2021 entry; ERC–ESICM 2025 uses M ≤5 (PCA-52)."),
    ('d', "**Fewer than 2 criteria met: observe and re-evaluate.** Indeterminate is not ‘good’; repeat examination and tests over the following days."),
  ],
  mimic=[
    ("Brain death vs poor prognosis", "Brain death is death; poor prognosis is a probability that allows a WLST discussion but is not death."),
  ],
  traps=[
    ("“Fewer than two criteria means a good outcome”", "It means not yet known; some of these patients recover, some do not."),
  ],
  decode=[
    ("[pattern] Comatose at 72 h, brainstem reflexes present, one criterion met: next step?", "Observe and re-evaluate; do not withdraw on one criterion."),
  ],
  punch="Neurological cause goes to CT first, absent brainstem reflexes to brain death testing, a patient not obeying commands at 72 hours to the six criteria, and fewer than two criteria to further observation.",
)

FLAGS = {}
FLAGS['PCA-41'] = "Card c: ‘TTM at 36 °C’ reflects the TTM-trial era (ERC–ESICM 2015: constant 32–36 °C); ERC–ESICM 2021 recommended fever prevention (>37.7 °C) for ≥72 h only, and 2025 ≤37.5 °C for 36–72 h."
FLAGS['PCA-43'] = "Card d/e: ‘start with the most robust predictors first (FPR <5%)’ is the 2015 stepwise algorithm; since 2021 any two of six criteria, no order. Card a’s ‘5–10 days’ is untraced; most patients who wake do so within the first few days, and late awakening is well described."
FLAGS['PCA-49'] = "Card correct (2–7 days matches AHA 2025 and ERC–ESICM 2025; repeat CT 72–96 h is ERC–ESICM 2025). The card-layer cross line saying ERC–ESICM 2025 uses 2–5 days is wrong: 2–5 days is 2021."
FLAGS['PCA-53'] = "Watch line says ‘reflexes and NSE at ≥72 h’; NSE is read at 48 h and/or 72 h (the card answer itself is right)."
FLAGS['PCA-54'] = "Marrow key ‘neither TTM option indicated yet’ in a sedated comatose survivor is disputed: AHA and ERC give temperature control to all comatose patients; sedation delays prognosis, not cooling."
FLAGS['PCA-56'] = "Row c gives M ≤3 (2021); ERC–ESICM 2025 entry is M ≤5, as PCA-43 and PCA-52 already say."
