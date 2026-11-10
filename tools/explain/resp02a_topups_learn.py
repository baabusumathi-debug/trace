# RESP02A top-up cards — Explain v3 ("Learn" depth), same fields and voice as resp02a_learn.py.
# Fields: sub, step (index into resp02a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from map/out/all_rows.json and the DocT GT/QBank files (the top-up's own src) plus qpack/RESP02A.md.
T = {}

T['T_ade9b5a5'] = dict(
  sub="Respiratory → COPD → Chest X-ray of emphysema",
  step=1,
  intro="Step 1 says emphysema destroys elastic recoil, so compliance rises. The chest X-ray shows the result: a chest that rests at a larger volume than normal. The exam gives the film with a COPD history and asks you to name it, and the signs below are what you look for.",
  parts=[
    ('a', "**Flat hemidiaphragms (>6 anterior or >10 posterior ribs above them).** The over-expanded lung pushes the diaphragm down and flattens its dome; counting ribs above the mid-clavicular diaphragm is the simplest measure of hyperinflation."),
    ('b', "**Wide retrosternal air space on the lateral film; long, narrow vertical heart.** On the lateral film the clear space behind the sternum widens (more than about 2.5 cm) as lung fills it. The low diaphragm pulls the heart down into a long, narrow shape."),
    ('c', "**Pruned peripheral vessels; bullae.** Destroyed alveolar walls take their capillaries with them, so vessels thin out quickly toward the periphery; bullae are avascular air spaces over 1 cm across with walls under 1 mm thick, seen as lucent areas bounded by hairline curves."),
    ('d', "**Why: lost elastic recoil raises FRC and RV, so the chest sits at high volume; acute asthma can hyperinflate too.** FRC is where inward recoil of lung balances outward recoil of the chest wall; weaker lung recoil moves that balance to a higher volume. Air trapping in an asthma attack does the same, temporarily."),
  ],
  mimic=[
    ("Emphysema vs pneumonia vs pulmonary embolism", "Pneumonia shows consolidation; PE usually leaves the film near normal; emphysema is the large, dark, vessel-poor chest."),
  ],
  traps=[
    ("“Acute asthma shows normal lung volumes”", "DocT’s explanation says so, and it is wrong: air trapping hyperinflates the chest in a severe attack; the history (smoker, COPD) is what points to emphysema."),
  ],
  decode=[
    ("60-year-old with COPD, worsening dyspnoea, CXR shown — diagnosis? [DocT]", "COPD with emphysema (86%)."),
    ("Smoker, RR 36, PaO₂ 55, PaCO₂ 70, CXR hyperinflation and flat diaphragms [DocT GT]", "Type 2 respiratory failure due to COPD (94%)."),
  ],
  punch="Emphysema is lost recoil, so the chest rests at high volume: low flat diaphragms, a wide retrosternal space, a narrow heart and thinned peripheral vessels.",
)

T['T_a8369bdb'] = dict(
  sub="Respiratory → Asthma → Tracheomalacia and EDAC as asthma mimics",
  step=4,
  intro="Step 4 is about recognising severity, but it starts with being sure the disease is asthma. A patient who keeps arriving in ‘status asthmaticus’, needs a tube, and is easy to ventilate as soon as the tube is in, has a large-airway problem the tube has bypassed.",
  parts=[
    ('a', "**Suspect tracheomalacia or excessive dynamic airway collapse (EDAC): the tube stents the collapsing airway, so the ‘bronchospasm’ vanishes on intubation.** In tracheomalacia the cartilage is weak; in EDAC the posterior membrane bows inward. Either way the central airway collapses on forced expiration and cough, causing wheeze and obstruction. A tube holds that segment open, while true asthma persists below the tube."),
    ('b', "**Diagnose by dynamic bronchoscopy after extubation (forced expiration/cough) or dynamic expiratory CT — an inspiratory CT can be normal.** The collapse happens only on expiration, so the test must be done while the patient breathes out forcefully; the usual threshold is a fall in airway lumen of more than 50% on expiration, although some healthy people exceed it, so the finding must match the symptoms; bronchoscopy needs the tube out because the tube itself splints the airway."),
    ('c', "**Vocal-cord dysfunction is the other mimic (speech therapy); treat EDAC with CPAP, stenting or tracheobronchoplasty.** In vocal-cord dysfunction the cords close paradoxically on inspiration, shown by laryngoscopy during symptoms, and it is treated with speech therapy. In EDAC, CPAP acts as a pneumatic stent; stenting or surgery is for severe cases."),
  ],
  mimic=[
    ("EDAC vs vocal-cord dysfunction", "Both mimic asthma and both settle with a tube; EDAC is expiratory, central airway collapse seen on dynamic bronchoscopy, vocal-cord dysfunction is inspiratory cord closure seen on laryngoscopy."),
  ],
  traps=[
    ("“Inspiratory CT is normal, so the airway is normal”", "The collapse is expiratory; only a dynamic expiratory CT or bronchoscopy shows it."),
    ("“Speech therapy”", "That treats vocal-cord dysfunction; first show the airway on bronchoscopy once extubated."),
  ],
  decode=[
    ("Recurrent ‘status asthmaticus’ that settles once intubated — next investigation? [Marrow]", "Bronchoscopy once extubated."),
  ],
  punch="If the ‘asthma’ disappears the moment the tube is in, the tube has splinted a collapsing central airway; look for it with dynamic bronchoscopy after extubation.",
)

T['T_a68aceb6'] = dict(
  sub="Respiratory → Lung function → Restrictive pattern in IPF",
  step=1,
  intro="Step 1 sets COPD as the lung that has lost its recoil. Idiopathic pulmonary fibrosis is the opposite lesion: the lung has too much recoil, so every volume shrinks. The exam tests this by asking which volumes fall.",
  parts=[
    ('a', "**Restrictive: TLC, FRC, RV, FEV₁ and FVC all reduced; FEV₁/FVC normal or raised (increased elastic recoil).** A stiff lung cannot be expanded, so TLC falls, and it recoils to a smaller FRC and RV. FEV₁ and FVC fall in proportion to the smaller lung; stiff lung and traction on the airways push expiratory flow, so the ratio stays normal or rises. A low TLC is what proves restriction."),
    ('b', "**DLCO reduced early (thickened membrane); desaturation on exercise.** Fibrosis thickens the alveolar membrane and destroys capillary bed, so gas transfer falls, often before volumes do. On exercise, faster blood flow leaves less time to equilibrate across the thickened membrane, so SpO₂ drops."),
    ('c', "**Volumes fall further as the lung stiffens.** Falling FVC and DLCO over time track progression and prognosis."),
  ],
  mimic=[
    ("Fibrotic lung vs chest-wall or muscle restriction", "Both lower TLC; in obesity, kyphoscoliosis or neuromuscular weakness the lung itself is normal, so DLCO corrected for volume (KCO) is normal or raised."),
  ],
  traps=[
    ("“Low FEV₁ means obstruction”", "FEV₁ falls in restriction too; it is the ratio that separates them — under 0.7 is COPD, normal or high is restriction."),
    ("“Residual volume rises in IPF”", "RV rises in obstruction (air trapping); in IPF all volumes fall."),
  ],
  decode=[
    ("PFT in idiopathic pulmonary fibrosis will show: reduced TLC, FRC, RV, or all? [DocT GT]", "All of the above (83%)."),
    ("Low FEV₁ and FEV₁/FVC <0.7 — COPD, ILD, restrictive disease or normal? [NEET 2025 recall]", "COPD; ILD keeps the ratio normal or high."),
  ],
  punch="Fibrosis is too much recoil: every volume falls, the FEV₁/FVC ratio stays normal or rises, and gas transfer falls early.",
)

FLAGS = {}
