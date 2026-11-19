# CVS10B — Explain v3 ("Learn" depth): ACS part II — ECG and biomarkers. Initial diagnosis timings (ESC 2023), J-point thresholds, posterior and RV leads, Sgarbossa and the LBBB
# algorithm, left main and NSTE-ACS patterns, ST-elevation shapes, non-ACS ST-T changes, culprit artery by leads, troponin T vs I, biomarker kinetics, high-sensitivity troponin,
# the 0 h/3 h and 0 h/1 h (2 h) algorithms, imaging in ACS, echo wall motion by artery.
# No mnemonics or hooks. Driven by qpack/CVS10B.md (24 question links; MI-28 culprit artery asked 9 times, MI-22 posterior/RV MI 4, MI-25 and MI-30 three each).
# MI-20, MI-23, MI-29, MI-31, MI-32, MI-33 and MI-34 have no linked question and get short explanations with [pattern] decode items.
# Card layer (cvs_cardlayer.json) lines for MI-22, MI-25, MI-27, MI-28, MI-30 read and covered; the MI-30 `fix` (troponin, not CK-MB, for re-infarction) is taught and FLAGGED.
# Checked online on 19 Nov 2026:
#  - Fourth Universal Definition of MI (Thygesen, EHJ 2018; ECG section as reproduced by tomwademd.net): new J-point elevation in 2 contiguous leads ≥1 mm in all leads except V2–V3, where
#    ≥2 mm men ≥40, ≥2.5 mm men <40, ≥1.5 mm women at any age; ST depression ≥0.5 mm horizontal/downsloping; T inversion >1 mm with prominent R or R/S >1; V7–V9 ≥0.5 mm (≥1 mm men <40);
#    V3R/V4R ≥0.5 mm (≥1 mm men <30); re-infarction >20% troponin rise from a stable or falling raised value; Q-wave criteria (V2–V3 >0.02 s or QS; elsewhere ≥0.03 s and ≥1 mm deep).
#  - ESC 2023 ACS (Byrne, EHJ 2023; recommendations as summarised in a university lecture PDF, umk.pl): ECG ≤10 min of FMC (I, B); ECG monitoring with defibrillator capacity in suspected
#    STEMI (I, B); V3R, V4R, V7–V9 in inferior STEMI or suspected total occlusion with inconclusive standard leads (I, B); hs-cTn immediately, results within 60 min (I, B); 0 h/1 h or
#    0 h/2 h algorithms (I, B), extra testing at 3 h if inconclusive; CCTA or stress imaging when hs-cTn normal/uncertain, ECG normal, pain-free (IIa, A); routine early CCTA not
#    recommended (III, B); emergency TTE in shock or suspected mechanical complication (I, C); triage echo in uncertainty without delaying the cath lab (IIa, C).
#  - ESC 2023 Supplementary Table S4 (trillium.de copy): 0 h/1 h hs-cTnT Elecsys very low <5, low <12, no Δ1h <3, high ≥52, Δ1h ≥5 ng/L; hs-cTnI Architect <4, <5, Δ <2, ≥64, Δ ≥6;
#    0 h/2 h hs-cTnT <5, <14, Δ2h <4, ≥52, Δ2h ≥10; hs-cTnI <4, <6, Δ <2, ≥64, Δ ≥15.
#  - LBBB (emDOCs update): Sgarbossa 5/3/2, score ≥3 specificity about 98% (meta-analysis), sensitivity about 20%; Smith-modified ST/S ≤ −0.25 sensitivity 91%, specificity 90%;
#    ACCF/AHA 2013 removed new LBBB in isolation as a STEMI criterion. Cai 2013 (Am Heart J, ‘The LBBB puzzle’) is the source of the card’s LBBB algorithm.
# Reviewer check, 19 Nov 2026: ESC 2023 full text (EHJ 2023;44:3720, sochicar.cl copy): 0 h/1 h or 0 h/2 h (I, B), extra testing at 3 h (I, B); the 0 h/3 h algorithm is ‘an alternative
#    where the 0 h/1 h or 0 h/2 h algorithms are not available’, with no class of its own, and ‘appears to balance efficacy and safety less well’ (ESC 2020 had given it IIa); ‘only CK-MB,
#    myosin-binding protein C and copeptin may have clinical relevance’, with limited incremental value over cTn; defibrillator-capable monitoring also I, B in suspected ACS with other ECG
#    changes or ongoing pain; Wellens’ sign named in the NSTE-ACS ECG section; LBBB/RBBB/paced rhythm with suspected ongoing ischaemia managed like STEMI. CMR in MINOCA without a clear
#    cause after angiography (I, B; J Clin Med 2024 appraisal table, PMC11012418). Kaier 2017 (Circulation, APACE, PMC5642333): cMyC AUC 0.92, equal to hs-cTnT/I; rule-out at presentation
#    32% vs 25% (hs-cTnT); better than hs-cTnT in presenters within 3 h. BIC-8 (Möckel 2015; tctmd): copeptin <10 pmol/L + negative troponin allowed early discharge, non-inferior MACE.
#    Cytoplasmic pools about 6% (cTnT) and 3% (cTnI) (Babuin & Jaffe, CMAJ 2005). AHA/ACC 2025: new LBBB in isolation is not a STEMI equivalent; V7–V9 for suspected circumflex occlusion.
# From standard references without a fresh check (confident unless said): troponin complex functions (C binds Ca²⁺, I inhibits actomyosin ATPase, T binds tropomyosin); cTnT from one
# manufacturer (Roche, 99th centile 14 ng/L) vs many cTnI assays with different cut-offs; cTnT re-expression in diseased skeletal
# muscle; marker kinetics (textbook ranges); RCA supplies the AV node in about 85–90%; posteromedial papillary muscle single PDA supply; first septal perforator and right bundle;
# Wellens/de Winter features; Spodick sign and the V6 ST/T ratio >0.25 for pericarditis; Takotsubo ECG (ST elevation in about 40–45%, later deep T inversion); ASE 2015 17-segment
# coronary territories.

SPINE = [
  ("The first ten minutes", "Anyone with suspected ACS gets a 12-lead ECG read within 10 minutes and, if STEMI is possible, a defibrillator-capable monitor; a clear STEMI goes to reperfusion without waiting for troponin."),
  ("Reading ST elevation correctly", "ST elevation counts only at the J point, in two contiguous leads, above age- and sex-specific thresholds, and the leads that show it name the wall and the artery, including the posterior and right ventricular walls that the standard leads miss."),
  ("Occlusion the ST rule misses", "LBBB, pacing, left main ischaemia and the proximal LAD patterns can hide an occluded or critically narrowed artery, so they have their own criteria and algorithms."),
  ("ST changes that are not ACS", "Shape, distribution, PR depression and the clinical picture separate STEMI from early repolarisation, pericarditis and the many non-ischaemic causes of ST and T changes."),
  ("Troponin: biology and timing", "Cardiac troponin is the marker of myocardial injury because it is cardiac-specific and lingers, while CK-MB and myoglobin rise and clear faster; high-sensitivity assays detect it within an hour of injury."),
  ("Fast algorithms and imaging", "Serial hs-troponin at 0 and 1 or 2 hours rules NSTEMI in or out, and echo, CT and MRI find the wall motion, the alternative diagnosis and the cases the ECG and troponin leave unresolved."),
]

PRIMER = "The ECG shows the myocardium’s electrical response to ischaemia in real time, but only for the walls the electrodes face, and conduction disease can mask it. Troponin shows that myocytes have been damaged, but it needs time to appear in the blood and is raised by many conditions other than an infarct. Acute MI is diagnosed as a rise and/or fall of troponin with at least one value above the 99th centile plus evidence of ischaemia (symptoms, ECG change, imaging or thrombus). The deck works through the two tests: how to read the ECG fast and correctly, and how to time and interpret troponin."

L = {}

L['MI-20'] = dict(
  sub="ACS → Diagnosis → Initial timings (ESC 2023)",
  step=1,
  intro="Step 1 is what happens in the first minutes after a patient with chest pain arrives. Every one of these timings exists because an occluded artery loses myocardium by the minute and the occluded patient may fibrillate before anything else is done.",
  parts=[
    ('a', "**12-lead ECG recorded and interpreted within 10 minutes of first medical contact (I, B).** The ECG is the only test that identifies an occlusion at the bedside, and the STEMI clock (first contact to wire crossing) runs from that recording."),
    ('b', "**Monitoring with defibrillator capability for all patients with suspected STEMI, as soon as possible (I, B).** Ventricular fibrillation is most frequent in the first hours of an acute occlusion, often before the patient reaches hospital. ESC 2023 extends the same monitoring (also I, B) to suspected ACS with other ECG changes or ongoing pain, and to anyone once MI is diagnosed."),
    ('c', "**Extra leads (V3R, V4R, V7–V9) in inferior STEMI, or suspected total occlusion with inconclusive standard leads (I, B).** The standard 12 leads do not face the right ventricle or the posterior wall, so an RV infarct or a circumflex occlusion can be missed (MI-22)."),
    ('d', "**hs-cTn drawn immediately, with results within 60 minutes of sampling (I, B).** The 0 h/1 h and 0 h/2 h algorithms (MI-33) only work if the first result is back fast enough for the repeat sample to be meaningful."),
    ('e', "**No: frank ST elevation means immediate reperfusion; waiting for biomarkers is unnecessary.** Troponin may still be normal in the first hour of an occlusion, and every minute of delay costs myocardium. STEMI is an ECG diagnosis."),
  ],
  mimic=[
    ("STEMI vs NSTE-ACS at triage", "STEMI is decided on the ECG and goes to reperfusion; NSTE-ACS is decided on serial troponin and risk."),
  ],
  traps=[
    ("“Confirm the STEMI with a troponin before activating the cath lab”", "Troponin may be normal early; the ECG alone triggers reperfusion."),
  ],
  decode=[
    ("Chest pain, ST elevation in two contiguous leads, troponin pending: next step? [pattern]", "Immediate reperfusion (primary PCI); do not wait for troponin."),
    ("Within how many minutes must the first ECG be recorded and read? [pattern]", "10 minutes from first medical contact."),
  ],
  punch="ECG within 10 minutes, a defibrillator on anyone who might be occluded, troponin results within an hour, and a STEMI never waits for the troponin.",
)

L['MI-21'] = dict(
  sub="ACS → ECG → J-point thresholds for ST elevation",
  step=2,
  intro="Step 2 begins with how ST elevation is measured. The thresholds come from the Fourth Universal Definition of MI and are set above the J-point elevation that healthy people show, which is highest in V2–V3, in young men. The one real question is the plain pattern (ST elevation V1–V4 with raised troponin = STEMI, 97% right); the exam detail lies in the numbers.",
  parts=[
    ('a', "**At the J point (end of QRS, start of ST), against the isoelectric baseline, usually the PR segment.** The J point is the one fixed landmark; the ST segment then slopes into the T wave, so measuring later would overcall elevation. The PR (or TP) segment is the baseline because it is electrically silent."),
    ('b', "**Two contiguous leads (same territory, same artery).** One lead can be noise; two adjacent leads looking at the same wall make it an injury current from one arterial territory."),
    ('c', "**V2–V3: men under 40, 2.5 mm; men 40 and over, 2.0 mm; women, 1.5 mm.** V2–V3 sit closest to the heart and normally show some J-point elevation, most in young men and least in women; the thresholds stop that normal pattern being called a STEMI. The cut is at 40: a 40-year-old man uses 2.0 mm. Women use 1.5 mm at any age."),
    ('d', "**1 mm in all other leads, in the absence of LBBB or LVH.** LBBB and LVH distort repolarisation and produce secondary ST elevation, so the standard rule cannot be applied; LBBB has its own criteria (MI-23). The thresholds apply to new or presumed new elevation."),
  ],
  mimic=[
    ("STEMI vs early repolarisation in V2–V3", "Early repolarisation stays under the age/sex thresholds or has a notched J point and concave ST; STEMI exceeds them with convex ST and often reciprocal depression (MI-26)."),
  ],
  traps=[
    ("“A 40-year-old man needs 2.5 mm in V2–V3”", "Under 40 is 2.5 mm; at 40 and over it is 2.0 mm."),
    ("“Measure ST elevation 80 ms after the J point”", "The Universal Definition measures at the J point itself."),
  ],
  decode=[
    ("Chest pain, ST elevation V1–V4, troponin raised [DocT QBank, 97%]", "STEMI (anterior)."),
    ("Woman, 1.6 mm J-point elevation in V2 and V3: meets STEMI criteria? [pattern]", "Yes; women need 1.5 mm in V2–V3."),
  ],
  punch="Measure at the J point, in two contiguous leads: 1 mm in most leads, and in V2–V3 2.5 mm for men under 40, 2 mm for men 40 and over, 1.5 mm for women.",
)

L['MI-22'] = dict(
  sub="ACS → ECG → Posterior and right ventricular MI",
  step=2,
  intro="Step 2 continues with the two walls the standard leads do not face. The posterior wall shows its injury only as a mirror image in V1–V3, and the right ventricle only in right-sided leads. Four real questions test the territory of an inferior/posterior pattern, its mechanical consequence (acute mitral regurgitation) and RV-infarct shock.",
  parts=[
    ('a', "**ST depression in V1–V3 with a positive terminal T wave.** V1–V3 face the anterior wall, so posterior ST elevation appears in them inverted: ST depression, with the tall R wave (R/S ≥1 in V1–V2) as the mirror of a posterior Q wave and an upright T as the mirror of posterior T inversion. Horizontal ST depression maximal in V1–V3 in a patient with pain is a posterior STEMI until V7–V9 say otherwise."),
    ('b', "**V7 posterior axillary line, V8 posterior scapular (mid-scapular) line, V9 paraspinal, all at the level of V6.** They continue the horizontal plane of V4–V6 round the back so that the posterior wall is faced directly."),
    ('c', "**0.5 mm in V7–V9, usually the LEFT CIRCUMFLEX.** The threshold is low because the posterior leads are far from the heart and record small voltages; the Universal Definition uses 1 mm in men under 40 for better specificity. The circumflex (or the RCA in a right-dominant system via its posterolateral branches) supplies the posterior wall, and circumflex occlusions are the ones most often missed on the standard ECG."),
    ('d', "**Right mid-clavicular line, 5th intercostal space (mirror of V4).** V4R faces the free wall of the right ventricle."),
    ('e', "**1 mm in V4R strongly suggests RV infarction.** RV infarction means a proximal RCA occlusion, above the RV marginal branches, and it accompanies about a third to a half of inferior infarcts. The Universal Definition accepts 0.5 mm in V3R/V4R (1 mm in men under 30); 1 mm is the more specific classic cut. The elevation is transient, so record V4R early in every inferior STEMI."),
  ],
  mimic=[
    ("Posterior STEMI vs anterior ischaemia (NSTE-ACS)", "Both give ST depression in V1–V3; posterior STEMI has tall R waves, upright T waves and ST elevation in V7–V9, and is an occlusion needing reperfusion."),
    ("RV-infarct shock vs LV cardiogenic shock", "RV infarct: high RAP, clear lungs, dilated RV; LV shock: high wedge pressure and pulmonary oedema."),
  ],
  traps=[
    ("“The dyspnoea after posterior MI is from LV systolic dysfunction”", "With a new apical holosystolic murmur, crackles and a preserved BP it is acute ischaemic mitral regurgitation: the posteromedial papillary muscle has a single supply (the PDA) and fails first (69% right)."),
    ("“Shock from RV infarction is due to distal RCA occlusion”", "It needs a PROXIMAL RCA occlusion, above the RV marginal branches; distal occlusion spares the RV (this was the incorrect statement)."),
    ("“Anterior territory, because the changes are in V1–V3”", "ST depression with tall R in V1–V3 is the posterior wall seen in mirror image."),
  ],
  decode=[
    ("Inferior pattern, III > II, reciprocal depression in aVL: which territory? [DocT QBank, 77%]", "Inferior (RCA)."),
    ("Chest pressure, new apical holosystolic murmur, crackles, BP preserved, posterior changes: mechanism of dyspnoea? [DocT GT]", "Acute mitral regurgitation from posteromedial papillary muscle ischaemia."),
    ("Incorrect statement about shock from RV infarction [Marrow]", "‘Due to distal RCA occlusion’; it is proximal."),
    ("Match MI location to leads: posterior? [Marrow]", "Tall R and ST depression in V1–V2 (R/S ≥1)."),
  ],
  extra=[
    dict(q="What does RV-infarct shock look like and how is it treated?", a="Proximal RCA occlusion: high RAP with a dilated RV, clear lungs and often mild to moderate LV dysfunction. Give volume to a RAP of about 10–15 mmHg, then an inotrope; avoid nitrates and diuretics, keep AV synchrony (pace if blocked), and reperfuse (RVF-16 onward; MI-38)."),
  ],
  punch="The posterior wall shows itself as ST depression with tall R and upright T in V1–V3, confirmed by 0.5 mm elevation in V7–V9; the right ventricle shows itself in V4R, and its infarct means a proximal RCA, a preload-dependent patient and no nitrates.",
)

L['MI-23'] = dict(
  sub="ACS → ECG → Sgarbossa criteria in LBBB",
  step=3,
  intro="Step 3 is occlusion hidden behind a conduction disturbance. In LBBB the ST segment normally moves opposite to the QRS (appropriate discordance), so the ordinary 1 mm rule fails; Sgarbossa looks for ST changes that break that expected pattern.",
  table=dict(title="Sgarbossa criteria (LBBB or ventricular pacing)",
    head=["Criterion", "Points", "Why it means infarction"],
    rows=[["Concordant ST elevation ≥1 mm where QRS is positive", "5", "LBBB never puts ST elevation in the same direction as the QRS"],
          ["Concordant ST depression ≥1 mm in V1–V3", "3", "V1–V3 have a negative QRS in LBBB; ST depression there is the wrong direction"],
          ["Discordant ST elevation ≥5 mm where QRS is negative", "2", "Discordance is expected; only its excess is suspicious, so it scores least"]]),
  parts=[
    ('a', "**Concordant ST elevation ≥1 mm in leads with a positive QRS (5); concordant ST depression ≥1 mm in V1–V3 (3); discordant ST elevation ≥5 mm in leads with a negative QRS (2).** The two concordant criteria are changes LBBB itself cannot produce. The discordant criterion is only an exaggeration of normal LBBB, which is why it carries the fewest points; Smith’s modification replaces it with an ST/S ratio of −0.25 or less, which is more sensitive (MI-24)."),
    ('b', "**Score ≥3 gives >90% specificity for MI.** A positive score effectively rules in infarction (specificity about 90% in the original study and about 98% in pooled data), but sensitivity is only about 20–35%, so a score below 3 does not rule it out."),
    ('c', "**Ventricular paced rhythm (RV pacing looks like LBBB): the rules apply but are less specific; RBBB may also confound.** An RV pacing lead activates the ventricles from the right, the same sequence as LBBB. ESC 2023 asks that LBBB or paced rhythm with suspected ongoing ischaemia be managed like STEMI."),
    ('d', "**NEW LBBB warrants investigation for ischaemia or infarction.** The 2013 ACCF/AHA guideline stopped treating new or presumed new LBBB in isolation as a STEMI equivalent, because most such patients have no occlusion and old ECGs are often missing; the decision is made on instability, Sgarbossa and serial testing (MI-24). AHA/ACC 2025 says the same: new LBBB in isolation is not diagnostic of MI."),
  ],
  mimic=[
    ("LBBB with MI vs uncomplicated LBBB", "Uncomplicated LBBB has proportionate discordant ST changes; MI shows concordance or excessive discordance."),
  ],
  traps=[
    ("“A Sgarbossa score of 0 excludes MI”", "Sensitivity is low; use serial ECGs, troponin and echo."),
  ],
  decode=[
    ("LBBB, 1.5 mm concordant ST elevation in V5–V6: Sgarbossa score and meaning? [pattern]", "5 points, ≥3: high specificity for MI; treat as STEMI."),
  ],
  punch="In LBBB look for what LBBB cannot do: concordant ST elevation (5) or ST depression in V1–V3 (3); a score of 3 rules MI in but a lower score does not rule it out.",
)

L['MI-24'] = dict(
  sub="ACS → ECG → LBBB algorithm",
  step=3,
  intro="Step 3 continues with what to do when LBBB and chest pain arrive together. The algorithm (Cai and colleagues, 2013, after the ACCF/AHA guideline dropped new LBBB as an automatic STEMI equivalent) asks three questions in order, and any ‘yes’ means reperfusion. The one real question (91% right) is the first step: a shocked patient does not wait for criteria.",
  parts=[
    ('a', "**Haemodynamic instability or acute HF? Yes → primary PCI or fibrinolysis.** A patient in shock or pulmonary oedema with LBBB and ischaemic pain has too much to lose from waiting; the occlusion is presumed and treated."),
    ('b', "**Sgarbossa ≥3?** Concordant ST change is highly specific for MI in LBBB (MI-23); a positive score means reperfusion."),
    ('c', "**ST/S ratio ≤ −0.25?** This is Smith’s modification: discordant ST elevation that is a quarter or more of the depth of the preceding S wave. It scales the threshold to the QRS size, which makes it more sensitive (about 80–90% in the derivation and validation studies) than the fixed 5 mm, with similar or better specificity."),
    ('d', "**If all three are no: serial ECGs, serial troponin, bedside echo.** Most LBBB with chest pain is not an occlusion; time, troponin trend and a regional wall-motion abnormality sort out the rest."),
    ('e', "**Abnormal → coronary angiography; normal → non-invasive evaluation.**"),
  ],
  mimic=[
    ("This LBBB algorithm vs the 0 h/3 h rule-out", "The notes title this flowchart as the 3-hour NSTEMI rule-out; that is MI-32."),
  ],
  traps=[
    ("“New LBBB in shock: repeat the ECG in 15 minutes or trend troponins”", "Instability is the first branch; treat as a STEMI equivalent now."),
  ],
  decode=[
    ("Chest pain, new LBBB, hypotensive and in cardiogenic shock: next step? [DocT GT, 91%]", "Treat as STEMI equivalent (reperfusion)."),
    ("Stable, LBBB, Sgarbossa 0, ST/S −0.15: next? [pattern]", "Serial ECG, troponin and echo."),
  ],
  punch="LBBB with chest pain: unstable, Sgarbossa ≥3 or ST/S ≤ −0.25 means reperfusion; otherwise serial ECG, troponin and echo decide between angiography and non-invasive testing.",
)

L['MI-25'] = dict(
  sub="ACS → ECG → Left main and NSTE-ACS patterns",
  step=3,
  intro="Step 3 ends with ischaemia that does not elevate the ST segment in a territory. Diffuse subendocardial ischaemia (left main or three-vessel) shows widespread ST depression, and NSTE-ACS shows ST depression or T inversion, or nothing at all. Three real questions test that NSTEMI is a troponin diagnosis, with any or no ECG change.",
  parts=[
    ('a', "**ST depression ≥1 mm in 8 or more leads + ST elevation in aVR and/or V1 → left main, left main equivalent or severe three-vessel ischaemia.** Global subendocardial ischaemia produces an injury vector pointing towards the cavity, which the many leads see as ST depression and aVR (facing the cavity) sees as elevation. It is a high-risk NSTE-ACS pattern, not a STEMI, and it calls for urgent angiography."),
    ('b', "**ST depression of 0.5 mm, horizontal or downsloping.** Upsloping J-point depression is common with tachycardia; horizontal or downsloping depression of 0.5 mm in two contiguous leads is the ischaemic shape. Deeper (≥1 mm) and more widespread depression carries more risk."),
    ('c', "**T-wave inversion in leads with a prominent R wave or R/S ratio >1.** The Universal Definition asks for inversion deeper than 1 mm in two contiguous leads. Shallow inversion (under 1 mm) in leads with a dominant R is a low-likelihood finding."),
  ],
  mimic=[
    ("NSTEMI vs unstable angina", "Both can have the same ECG; NSTEMI has troponin above the 99th centile with a rise or fall, unstable angina does not."),
    ("Left main pattern vs STEMI", "ST elevation only in aVR (± V1) with widespread depression is diffuse ischaemia, not a territorial occlusion."),
  ],
  traps=[
    ("“Normal ECG, so unstable angina”", "Troponin above the 99th centile with a rise or fall makes it NSTEMI whatever the ECG shows (68% right). With BP 180/110 and no prior CAD, think of a type 2 MI and exclude aortic dissection (BP in both arms, pain character) before antithrombotics."),
    ("“Lateral T inversion with raised troponin is unstable angina”", "Raised troponin with ischaemic symptoms is NSTEMI (71% right)."),
  ],
  decode=[
    ("Chest pain, BP 180/110, ECG no changes, troponin slightly raised [DocT QBank, 68%]", "NSTEMI."),
    ("Chest pain, lateral T inversion, troponin raised, stable [DocT QBank, 71%]", "NSTEMI."),
    ("Finding NOT indicating high likelihood of ACS [Marrow]", "T inversion under 1 mm in leads with a dominant R wave."),
  ],
  extra=[
    dict(q="Which findings make ACS likely?", a="High likelihood: prior documented angina or known CAD, a transient MR murmur or hypotension during pain, new ST deviation ≥1 mm or T inversion in multiple precordial leads. Low likelihood: T flattening or inversion under 1 mm in leads with a dominant R."),
  ],
  punch="Widespread ST depression with ST elevation in aVR is left main or three-vessel ischaemia; otherwise NSTE-ACS shows 0.5 mm horizontal depression or T inversion in R-dominant leads, and a normal ECG with a troponin rise is still NSTEMI.",
)

L['MI-26'] = dict(
  sub="ACS → ECG → ST-elevation patterns",
  step=4,
  intro="Step 4 is ST elevation that is not an occlusion. The shape of the segment and what surrounds it (PR segment, J point, reciprocal change, territory) separate the four common patterns. The one real question is the athlete with concave elevation and a raised J point.",
  table=dict(title="ST elevation: the discriminating features",
    head=["Pattern", "Distribution", "Reciprocal change", "Other"],
    rows=[["STEMI", "One arterial territory", "Yes", "Convex, evolves over hours, Q waves"],
          ["Early repolarisation", "V2–V5 (± inferior)", "No (except aVR)", "Notched/slurred J point, stable over time, young men"],
          ["Pericarditis", "Widespread", "Only aVR (± V1)", "PR depression (PR elevation in aVR), ST/T in V6 >0.25"],
          ["LBBB", "Leads with negative QRS", "Discordant by design", "Broad QRS; use Sgarbossa"]]),
  parts=[
    ('a', "**STEMI: convex upward; ST and T blend into one dome, may have T inversion with the elevation, Q waves.** Transmural injury lifts the whole ST segment into the T wave; elevation confined to one territory, with reciprocal depression opposite, makes it an occlusion."),
    ('b', "**Early repolarisation: concave, with a notched, slurred or well-demarcated J point.** It reflects early repolarisation of part of the epicardium, is common in young men and athletes, has no reciprocal depression and does not change over time."),
    ('c', "**Pericarditis: concave upward, PR depression, ST/T ratio >25%.** Epicardial inflammation affects the whole surface (widespread elevation) and the atria (PR depression, with PR elevation in aVR). An ST/T height ratio above 0.25 in V6 favours pericarditis over early repolarisation."),
    ('d', "**LBBB: discordant, ST opposite to the main QRS vector.** This is secondary repolarisation from abnormal depolarisation, not injury (MI-23)."),
  ],
  mimic=[
    ("Early repolarisation vs pericarditis", "Both concave; pericarditis has PR depression, widespread leads and an ST/T ratio >0.25 in V6 (CVS-08, CVS-09)."),
  ],
  traps=[
    ("“Concave ST elevation in a young athlete is myocarditis or Brugada”", "Brugada is coved elevation in V1–V2 only; myocarditis comes with symptoms and troponin. Asymptomatic, concave, J-point elevation without reciprocal change is early repolarisation."),
  ],
  decode=[
    ("Asymptomatic 29-year-old athlete, 0.15 mV J-point elevation V3–V5, concave, no reciprocal change [DocT GT]", "Early repolarisation."),
  ],
  punch="Convex, territorial and with reciprocal depression is STEMI; concave with a notched J point is early repolarisation; concave, widespread and with PR depression is pericarditis.",
)

L['MI-27'] = dict(
  sub="ACS → ECG → Non-ACS causes of ST and T changes",
  step=4,
  intro="Step 4 widens to every non-ischaemic cause of ST and T changes. Most share one mechanism: either abnormal depolarisation (bundle branch block, pacing, LVH) forces abnormal repolarisation, or the myocardium or pericardium is injured or inflamed without a coronary occlusion. The one real question was about Takotsubo, which the card places only in the ST depression column.",
  parts=[
    ('a', "**ST elevation: pericarditis, myocarditis, cor pulmonale/RV strain, LV aneurysm, HCM, hypothermia, paced rhythm, LVH, LBBB, RBBB, PE, MVP, Brugada, early repolarisation.** LV aneurysm gives persistent elevation with Q waves weeks after an anterior infarct; hypothermia gives J (Osborn) waves; Brugada gives coved elevation in V1–V2. Stress (Takotsubo) cardiomyopathy also belongs here: it presents with ST elevation in a large share of cases."),
    ('b', "**ST depression: hypokalaemia, digoxin effect, LVH, LBBB, paced rhythm, myocardial diseases, stress cardiomyopathy, myocardial contusion.** Digoxin gives a scooped (sagging) depression; hypokalaemia gives depression with U waves; LVH gives strain-pattern depression with asymmetric T inversion in the lateral leads."),
    ('c', "**T inversion: persistent juvenile pattern, Stokes-Adams syncope, post-tachycardia, post pacemaker insertion, intracranial pathology, pericarditis.** These are repolarisation memory (after tachycardia or pacing) or autonomic effects (deep, wide ‘cerebral’ T waves with long QT after subarachnoid haemorrhage); in pericarditis T inversion follows once the ST elevation resolves."),
  ],
  mimic=[
    ("Takotsubo vs anterior STEMI", "Both have ST elevation and troponin; in Takotsubo the wall-motion abnormality extends beyond one coronary territory and the coronaries are unobstructed."),
  ],
  traps=[
    ("“The ECG in Takotsubo never shows ST elevation”", "False: it mimics STEMI with ST elevation and troponin release, followed by deep T inversion."),
  ],
  decode=[
    ("Takotsubo ventriculogram: false statement? [Marrow]", "‘ECG never shows ST elevation’."),
  ],
  extra=[
    dict(q="What else does the exam ask about Takotsubo and apical HCM?", a="Takotsubo: wall-motion abnormality beyond one territory, unobstructed coronaries, contraction-band necrosis, recovery within weeks; variants are apical (typical), mid-ventricular, basal (reverse; post-operative or catecholamine-driven), focal and RV; men are fewer but do worse. Apical HCM (Yamaguchi): giant precordial T inversion (over 10 mm) with a spade-shaped LV cavity; lower sudden-death risk than septal HCM."),
  ],
  punch="Most non-ACS ST-T changes come from abnormal depolarisation or non-coronary injury; Takotsubo is the one that imitates STEMI most closely, with ST elevation, troponin and a wall-motion abnormality that crosses territories.",
)

L['MI-28'] = dict(
  sub="ACS → ECG → Culprit artery by lead group",
  step=2,
  intro="Step 2 ends with the leads naming the artery. Each lead faces a wall, each wall has a usual artery, and the variations (dominance, wrap-around LAD, conduction blocks) are what the exam asks. Nine real questions hit this card, more than any other in the deck: territory, culprit artery, new RBBB, and old versus acute infarction.",
  parts=[
    ('a', "**I, aVL, V5–V6: lateral, LCx or a diagonal branch of the LAD.** High lateral (I, aVL) is often the first diagonal; lower lateral (V5–V6) the circumflex. ST elevation here with ST depression in V1–V3 suggests a circumflex occlusion that also involves the posterior wall (MI-22)."),
    ('b', "**II, III, aVF: inferior, RCA and/or LCx.** The RCA gives the PDA in about 80–90% of people (right-dominant or co-dominant circulations). Elevation III > II with reciprocal depression in aVL/I points to the RCA (lead III faces rightward); II ≥ III with elevation in I, aVL or V5–V6 points to the circumflex. The RCA also supplies the AV node in about 90%, hence the bradycardia and AV block of inferior MI, and its proximal occlusion adds RV infarction (V4R)."),
    ('c', "**V1–V4: anterior/septal, LAD.** The first septal perforator supplies the right bundle, so ST elevation in V1 with a NEW RBBB means a PROXIMAL LAD occlusion; a distal LAD lesion gives V3–V4 elevation without RBBB. Anterior STEMI with new bundle branch block carries a large infarct and a high risk of shock."),
  ],
  mimic=[
    ("RCA vs LCx inferior MI", "RCA: III > II, reciprocal aVL depression, RV involvement; LCx: II ≥ III, lateral elevation."),
    ("Old vs acute infarction", "Pathological Q waves without ST elevation are healed scar; ST elevation is acute injury."),
  ],
  traps=[
    ("“Q waves in I, aVL, V5 in a breathless man with known CAD: acute coronary syndrome”", "Q waves without ST elevation mean an OLD lateral infarct (only 46% right). Q waves are permanent scar."),
    ("“STEMI: give thrombolysis”", "Primary PCI is preferred when it can be delivered in time (73% right); fibrinolysis is for when PCI cannot be done within 120 minutes of diagnosis."),
    ("“Inferior STEMI with CVP 14 and shock: PE”", "Inferior STEMI with a raised CVP and shock is the RV-infarct picture (91% right)."),
  ],
  decode=[
    ("Shock, CVP 14, ST elevation II, III, aVF [DocT QBank, 91%]", "Acute inferior MI."),
    ("ST elevation in I, aVL (and V1), chest pain: next step [DocT QBank, 73%]", "Primary PCI."),
    ("Breathless known-CAD patient, Q waves in I, aVL, V5 [DocT QBank, 46%]", "Old myocardial infarction."),
    ("ST elevation >2.5 mm in V1 with RBBB: culprit [Marrow ×2]", "Proximal LAD."),
  ],
  extra=[
    dict(q="What makes a Q wave pathological?", a="Commonly taught: 40 ms or wider, or deeper than 25% of the following R, in two contiguous leads. The Universal Definition is stricter in its wording: any Q in V2–V3 over 20 ms or a QS complex; elsewhere 30 ms or more and 1 mm deep in two contiguous leads; and a tall R (40 ms, R/S ≥1) in V1–V2 for a posterior scar."),
  ],
  punch="Lateral leads mean circumflex or diagonal, inferior leads RCA (III > II) or circumflex (II ≥ III), anterior leads LAD; ST elevation in V1 with a new RBBB is the proximal LAD, and Q waves without ST elevation are old scar.",
)

L['MI-29'] = dict(
  sub="ACS → Biomarkers → Troponin T vs troponin I",
  step=5,
  intro="Step 5 opens with why troponin is the marker of myocardial injury. The troponin complex regulates contraction on the thin filament, and the cardiac isoforms of T and I differ from the skeletal ones, which is what makes them cardiac-specific. The card’s first and third rows are reversed relative to the biochemistry (see FLAGS); the bold keeps the card’s wording.",
  parts=[
    ('a', "**Card: troponin T inhibits actin-myosin interaction; troponin I binds tropomyosin.** These are the wrong way round. Troponin T binds tropomyosin and anchors the complex; troponin I is the inhibitory unit that blocks actomyosin ATPase; troponin C binds calcium, which releases the inhibition and allows contraction."),
    ('b', "**Troponin T lower, troponin I higher sensitivity/specificity (per the notes).** The specificity point has a reason: diseased or regenerating skeletal muscle can re-express cardiac troponin T, so cTnT can be raised in myopathies, whereas cardiac troponin I is not expressed in skeletal muscle. Both are raised by CKD, more so cTnT."),
    ('c', "**Card: troponin T, multiple assay-dependent reference levels; troponin I, single.** This is reversed. Troponin T is made by one manufacturer (Roche), with a single 99th centile of 14 ng/L for the hs assay; troponin I is measured by many assays from different manufacturers, each with its own 99th centile, so cTnI results cannot be compared between laboratories."),
    ('d', "**Cytoplasmic pool: troponin T 6%, troponin I 3%.** These are the classic figures (about 6% and 3%); more recent work suggests the early-releasable pool is larger and less clearly ‘cytoplasmic’. Most troponin is bound in the sarcomere; the small free cytoplasmic pool leaks out first after injury, and the structural pool is released slowly as myofibrils break down, which is why troponin stays raised for days and cTnT longest (MI-30)."),
  ],
  mimic=[
    ("Troponin T vs I in a patient with myositis", "cTnT may be raised from skeletal muscle; cTnI is cardiac-specific."),
  ],
  traps=[
    ("“Troponin I binds tropomyosin”", "Troponin T binds tropomyosin; troponin I inhibits actomyosin ATPase."),
  ],
  decode=[
    ("Which troponin subunit inhibits actomyosin ATPase? [pattern]", "Troponin I."),
    ("Raised troponin in a patient with muscular dystrophy and no chest pain: which assay is more cardiac-specific? [pattern]", "Troponin I."),
  ],
  punch="T binds tropomyosin, I inhibits, C binds calcium; cardiac troponin I is the more cardiac-specific, and troponin T, from a single manufacturer, has the single cut-off.",
)

L['MI-30'] = dict(
  sub="ACS → Biomarkers → Kinetics of troponin, CK-MB and myoglobin",
  step=5,
  intro="Step 5 continues with the timing of each marker, which follows from where it sits in the cell and how it is cleared. Small cytoplasmic molecules (myoglobin) leak and clear fast; structural proteins (troponin) leak slowly and for days. Three real questions test troponin I’s kinetics, the newer early markers and re-infarction.",
  parts=[
    ('a', "**Troponin T: rises 3–12 h, peaks 12–48 h, normal by 14 days.** The cytoplasmic pool gives the early rise, and the slow breakdown of the structural pool gives a second plateau and the long tail; cTnT’s larger pool and slower release keep it up longest. With hs assays the rise is detectable within 1–3 h (MI-31)."),
    ('b', "**Troponin I: rises 3–12 h, peaks 24 h, normal by 10 days.** The notes’ general table says ‘7–10 days’; the DocT question uses rise 3–6 h, peak 12–24 h, back by 7–10 days, which is troponin I."),
    ('c', "**CK-MB: rises 4–6 h, peaks 24 h, normal by 48–72 h; less specific (skeletal muscle).** Skeletal muscle contains some CK-MB, so it is raised by muscle injury. Its quick return to normal was why it used to be used for re-infarction; current guidance (the Fourth Universal Definition, ESC/ACC) uses troponin: a rise of more than 20% from an already raised value that is stable or falling, sampled at symptom onset and 3–6 h later. CK-MB is used only where troponin is unavailable (see FLAGS)."),
    ('d', "**Myoglobin: rises 2–4 h, peaks 8–12 h, normal by 24 h; earliest riser.** Small (17 kDa), cytoplasmic and cleared by the kidney, so it appears and disappears fastest; it is in every muscle, so it is not specific and adds little to hs-troponin."),
  ],
  table=dict(title="Why each marker behaves as it does",
    head=["Marker", "Where it sits", "Consequence"],
    rows=[["Myoglobin", "Cytoplasm of all muscle", "Earliest, shortest, not cardiac-specific"],
          ["CK-MB", "Cytoplasm, mainly heart", "Back to normal in 2–3 days; skeletal muscle raises it"],
          ["Troponin", "Mostly bound to the sarcomere", "Cardiac-specific, raised 7–14 days"]]),
  mimic=[
    ("Re-infarction on day 3: troponin vs CK-MB", "Both guidelines now use a >20% troponin rise; CK-MB only if troponin is unavailable."),
  ],
  traps=[
    ("“The marker that rises at 3–6 h and returns in 7–10 days is CK-MB”", "CK-MB is back to normal in 48–72 h; that profile is troponin I (69% right)."),
    ("“Myoglobin or BNP is the early add-on to hs-troponin”", "The keyed answer is cardiac myosin-binding protein C (cMyC): cardiac-restricted, more abundant and released faster than troponin (57% right). In the APACE cohort cMyC matched hs-troponin overall (AUC about 0.92) and ruled out more patients at presentation (about 32% vs 25% with hs-cTnT), with an advantage in those presenting within 3 hours. Copeptin is the other early add-on: a negative copeptin with a negative troponin allowed safe early discharge in BIC-8, and its value is greatest when only a conventional troponin assay is available. ESC 2023 names CK-MB, cMyC and copeptin as the only other markers with possible relevance, but with limited value beyond hs-troponin; IMA, BNP and microRNA-208b are not used to diagnose MI."),
    ("“CK-MB is the best marker for re-infarction on day 3”", "Troponin is (the Marrow key); the card’s CK-MB line follows older teaching."),
  ],
  decode=[
    ("Rises 3–6 h, peaks 12–24 h, baseline in 7–10 days [DocT QBank, 69%]", "Troponin I."),
    ("Biomarker that rises earlier than troponin and improves rule-in/rule-out with it [DocT GT, 57%]", "cMyC."),
    ("Best biomarker for re-infarction on day 3 [Marrow]", "Troponin I (>20% rise)."),
  ],
  punch="Myoglobin is first and gone in a day, CK-MB is gone in 2–3 days, troponin lasts 10–14 days; re-infarction is now a >20% troponin rise, not a CK-MB peak.",
)

L['MI-31'] = dict(
  sub="ACS → Biomarkers → High-sensitivity troponin",
  step=5,
  intro="Step 5 ends with what the high-sensitivity assays changed. They measure troponin in most healthy people, so a very low value excludes injury and a small rise is detected within an hour, which is what makes the fast algorithms of step 6 possible.",
  parts=[
    ('a', "**First-generation limits: low sensitivity and specificity, poor NPV, poor in early or small injury.** Older assays could not detect troponin until hours after onset, so an early normal result excluded nothing, and patients had to wait 6–12 h for a repeat."),
    ('b', "**NPV of a single hs-cTn 95%, nearly 100% with a repeat at 1 h or 2 h.** A very low value on arrival (if pain started more than 3 h earlier) or a low value that does not rise in 1–2 h makes MI very unlikely (MI-33)."),
    ('c', "**Single-baseline cut-off 3–5 ng/L for hs-cTnT vs 14 ng/L.** 14 ng/L is the 99th centile of the hs-cTnT assay, the diagnostic threshold for injury; 3–5 ng/L is around the assay’s limit of detection, and ESC uses under 5 ng/L as the ‘very low’ single-sample rule-out."),
    ('d', "**Performs better in CKD.** ‘Better’ means better than the conventional assays: hs-cTn keeps high diagnostic accuracy and a safe rule-out in renal dysfunction. CKD itself raises baseline troponin, so a single value over the 99th centile is common without MI; compared with normal renal function, specificity and the share of patients ruled out are lower, and the change between samples (the delta) matters more than the absolute value."),
    ('e', "**Also risk-stratifies ACS, heart failure and stable CAD.** Any detectable troponin reflects myocardial stress or injury, and higher levels predict death in these conditions."),
  ],
  mimic=[
    ("Very low vs very high hs-cTn", "Very low rules out (NPV); very high rules in (PPV); the same assay does both at opposite ends."),
  ],
  traps=[
    ("“A troponin above the 99th centile means MI”", "It means myocardial injury; MI needs a rise or fall plus evidence of ischaemia."),
  ],
  decode=[
    ("hs-cTnT 4 ng/L, pain began 6 h ago, normal ECG: [pattern]", "Rule out on the single sample (very low, pain over 3 h)."),
  ],
  punch="hs-troponin turns a single very low value into a rule-out and a 1–2 h change into a rule-in; above the 99th centile it means injury, not necessarily infarction.",
)

L['MI-32'] = dict(
  sub="ACS → Biomarkers → 0 h/3 h hs-cTn algorithm",
  step=6,
  intro="Step 6 starts with the older of the fast pathways. ESC 2023 keeps the 0 h/3 h algorithm only as an alternative where the 0 h/1 h or 0 h/2 h algorithms are not available, without a class of its own (ESC 2020 had given it IIa). It compares the result with the 99th centile (ULN) and uses symptom duration: troponin released by an infarct over 6 hours old should already be detectable.",
  parts=[
    ('a', "**hs-cTn below ULN and pain over 6 h: pain-free, GRACE <140, differentials excluded → discharge or stress testing.** Six hours is long enough for an infarct to have raised hs-troponin, so a single normal value suffices."),
    ('b', "**Below ULN and pain under 6 h: retest at 3 h.** The infarct may be too young to show."),
    ('c', "**Delta change with at least one value above ULN → invasive.** A rise or fall over 3 h with a value above the 99th centile is an acute injury, and with an ischaemic picture an NSTEMI."),
    ('d', "**Discharge: pain-free, GRACE <140, differentials excluded.** GRACE under 140 is low-risk."),
    ('e', "**hs-cTn over 5 × ULN with a typical presentation → straight to invasive.** A value that high is rarely chronic. A raised baseline that does not change on retest is chronic injury (CKD, heart failure): work up differential diagnoses."),
  ],
  mimic=[
    ("Acute vs chronic myocardial injury", "Acute injury shows a rise or fall; chronic injury is a stable raised value."),
  ],
  traps=[
    ("“The 0 h/3 h pathway is the current ESC first choice”", "ESC 2023 recommends the 0 h/1 h or 0 h/2 h algorithms (I, B), with a 3 h sample only when those are inconclusive. The 0 h/3 h pathway (ESC 2015; IIa in 2020) is now only a fallback where the faster algorithms are unavailable, because it balances efficacy and safety less well (MI-33)."),
  ],
  decode=[
    ("hs-cTn below ULN, pain began 2 h ago: next step? [pattern]", "Repeat at 3 h."),
  ],
  punch="Below the ULN with pain over 6 hours, a low-risk patient can go home; under 6 hours, repeat at 3 hours, and a change with a value over the ULN means invasive management.",
)

L['MI-33'] = dict(
  sub="ACS → Biomarkers → ESC 0 h/1 h (or 2 h) algorithm",
  step=6,
  intro="Step 6 continues with the current ESC pathway. It uses assay-specific cut-offs far below the 99th centile and the absolute change over 1 or 2 hours, and sorts patients into three groups.",
  table=dict(title="ESC 2023 cut-offs, hs-cTnT (Elecsys), ng/L",
    head=["Algorithm", "Rule-out", "Rule-in"],
    rows=[["0 h/1 h", "0 h <5 (pain >3 h), or 0 h <12 and Δ1h <3", "0 h ≥52, or Δ1h ≥5"],
          ["0 h/2 h", "0 h <5 (pain >3 h), or 0 h <14 and Δ2h <4", "0 h ≥52, or Δ2h ≥10"]]),
  parts=[
    ('a', "**Suspected NSTEMI without an indication for immediate invasive angiography.** Patients with STEMI or very high-risk features (shock, refractory pain, arrhythmia) go to the cath lab without the algorithm."),
    ('b', "**Rule-out: very low initial hs-cTn, OR low initial + no rise at 1 h or 2 h.** NPV is over 99%; the very-low single sample is valid only if pain began more than 3 hours earlier."),
    ('c', "**Rule-in: high initial hs-cTn, OR a rise at 1 h or 2 h.** PPV is around 70%, so clinical context still matters; confirmed NSTEMI goes to early invasive angiography."),
    ('d', "**Everyone else: OBSERVE, managed by hs-cTn levels and the clinical picture.** ESC 2023 repeats hs-cTn at 3 h and considers echo; CCTA or angiography follow depending on risk (MI-34)."),
  ],
  mimic=[
    ("0 h/1 h vs 0 h/3 h", "0 h/1 h uses low assay-specific cut-offs and absolute deltas; 0 h/3 h uses the ULN and symptom duration (MI-32)."),
  ],
  traps=[
    ("“Rule out on one very low value even if pain started 1 hour ago”", "The single-sample rule-out needs symptom onset over 3 hours earlier."),
  ],
  decode=[
    ("hs-cTnT 0 h 8, 1 h 9 ng/L, pain-free, normal ECG: [pattern]", "Rule-out (low and Δ <3)."),
    ("hs-cTnT 0 h 30, 1 h 31 ng/L: [pattern]", "Observe zone."),
  ],
  punch="Very low, or low without a rise in 1–2 hours, rules out; high, or a rise, rules in; the rest are observed, and the whole pathway is for patients who do not already need the cath lab.",
)

L['MI-34'] = dict(
  sub="ACS → Diagnosis → Imaging in ACS",
  step=6,
  intro="Step 6 ends with imaging, which finds what the ECG and troponin cannot: a regional wall-motion abnormality, an alternative diagnosis that would be harmed by antithrombotics, or an obstructed artery in a patient with inconclusive tests.",
  parts=[
    ('a', "**TTE: regional wall motion abnormality; it must NOT delay transfer for STEMI.** Ischaemic myocardium stops contracting within seconds, before ECG change; a normal echo during pain makes significant ischaemia unlikely. ESC 2023 asks for emergency echo in shock or suspected mechanical complications (I, C) and triage echo in uncertainty without delaying the cath lab (IIa, C)."),
    ('b', "**CTPA / CT aortogram: rule out PE and aortic dissection.** Both present with chest pain, troponin rise and sometimes ST changes, and dissection would be made worse by antithrombotics."),
    ('c', "**CCTA: exclude ACS when ECG and troponin are normal or inconclusive (ESC IIa).** Its strength is its NPV: no coronary plaque means no ACS. ESC 2023 IIa, A for low-to-intermediate likelihood patients with non-elevated or uncertain hs-cTn, a normal ECG and no recurrent pain; routine early CCTA is not recommended."),
    ('d', "**CMR: gadolinium enhancement shows scar and perfusion defects, and alternative diagnoses such as myocarditis.** Ischaemic scar starts at the subendocardium; myocarditis enhances mid-wall or subepicardially; Takotsubo shows oedema without scar. CMR is the key test in MINOCA: ESC 2023 recommends it when the cause is not clear after angiography (I, B)."),
  ],
  mimic=[
    ("Ischaemic vs non-ischaemic enhancement on CMR", "Ischaemic: subendocardial or transmural in a coronary territory; myocarditis: subepicardial or mid-wall."),
  ],
  traps=[
    ("“CCTA is for NSTEMI patients without chest pain”", "It is for patients with suspected ACS whose ECG and troponin are normal or inconclusive."),
  ],
  decode=[
    ("Chest pain, normal ECG, hs-cTn in the observe zone, pain-free: next test? [pattern]", "CCTA (or stress imaging)."),
  ],
  punch="Echo for wall motion and complications without delaying the cath lab, CT for PE and dissection, CCTA to exclude ACS when the tests are equivocal, and CMR for scar and the alternative diagnosis.",
)

L['MI-35'] = dict(
  sub="ACS → Echo → Wall motion abnormality by artery",
  step=6,
  intro="Step 6 includes the echo map of coronary territories. Each standard view cuts through walls supplied by a known artery, so a regional wall-motion abnormality points to the culprit. The one real question asks why the parasternal short axis is the view for wall motion.",
  parts=[
    ('a', "**Apical 4-chamber: septum and apex, LAD; lateral wall, LCx (occasionally RCA).** The septum seen in A4C is the inferoseptum; its basal part is often RCA territory, while the mid and apical parts and the apex are LAD."),
    ('b', "**Apical 2-chamber: inferior wall, RCA.** The opposite wall in this view, the anterior wall, is LAD territory."),
    ('c', "**Parasternal short axis: inferior, RCA; anterior (superior), LAD; lateral, LCx.** At mid-papillary level the short axis cuts across all three territories at once (the anterior and anteroseptal walls are LAD, the inferior and inferoseptal walls RCA, the lateral walls LCx), which is why it is the single best view for regional wall motion."),
  ],
  mimic=[
    ("Regional vs global hypokinesis", "Regional abnormality in one territory points to a coronary cause; global hypokinesis to cardiomyopathy, sepsis or myocarditis; abnormality crossing territories, to Takotsubo."),
  ],
  traps=[
    ("“The short axis view is for the LVOT gradient or stroke volume”", "Those come from apical views with Doppler; PSAX is for regional wall motion (61% right)."),
  ],
  decode=[
    ("Probe rotated 90° clockwise from PLAX, circular LV: main advantage? [DocT QBank, 61%]", "Evaluating LV regional wall motion."),
  ],
  punch="The mid short axis shows all three coronary territories at once: anterior LAD, lateral LCx, inferior RCA.",
)

FLAGS = {
  'MI-22': "e (and c): 1 mm in V4R is the classic, more specific cut; the Fourth Universal Definition accepts ≥0.5 mm in V3R/V4R (≥1 mm in men under 30), and for V7–V9 uses 0.5 mm but 1 mm in men under 40. Not wrong, but incomplete; the explanation gives both.",
  'MI-27': "Stress (Takotsubo) cardiomyopathy is listed only under ST depression; it commonly presents with ST elevation (the Marrow question keys ‘never shows ST elevation’ as false). LVH appears twice in the ST depression column (a source duplicate).",
  'MI-29': "Rows a and c are reversed: troponin T binds tropomyosin and troponin I inhibits actomyosin ATPase; troponin T (one manufacturer) has a single reference level, while troponin I has multiple assay-dependent ones. The explanation teaches the correct biochemistry.",
  'MI-31': "d: ‘performs better in CKD’ holds only against conventional assays; compared with normal renal function, hs-cTn specificity and the share ruled out are lower in CKD, and the delta matters more. Wording is ambiguous, not wrong; the explanation states it plainly.",
  'MI-30': "CK-MB ‘used for re-infarction’ is outdated: the Fourth Universal Definition and ESC 2023 use troponin (>20% rise from a stable or falling raised value); CK-MB only if troponin is unavailable (agrees with the qbank fix and the Marrow key).",
}
