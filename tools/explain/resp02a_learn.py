# RESP02A — Explain v3 ("Learn" depth): COPD — Pathophysiology, Presentation & Severity, Non-invasive Ventilation. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP02A.md (44 questions; COPD-10 asked 13 times). Fields as TOX01, plus SPINE, PRIMER and step.

SPINE = [
  ("The lesion: narrow airways, lost recoil", "COPD is fixed expiratory airflow limitation from narrowed small airways and emphysema, so compliance rises and recoil falls — the opposite of ARDS — and it fails as type 2 (hypercapnic) failure."),
  ("Trapped air and intrinsic PEEP", "Because a long time constant (resistance × compliance) meets a short expiratory time, each breath starts before the last has emptied, leaving intrinsic PEEP that the patient must overcome before every breath."),
  ("Positive pressure and the heart", "Positive pressure on a hyperinflated chest cuts venous return and raises right-ventricular afterload, so blood pressure falls, worst just after intubation."),
  ("Recognising and grading severity", "The ratio FEV₁/FVC <0.7 diagnoses COPD and FEV₁ grades it, but in an exacerbation it is mental state, effort and the blood gas — a ‘normal’ PaCO₂ in asthma — that mark danger."),
  ("NIV first, set up properly", "In a COPD exacerbation with hypercapnic acidosis (pH <7.35), NIV with controlled oxygen (SpO₂ 88–92%) is the first treatment and roughly halves mortality."),
  ("When NIV fails, intubate", "Recheck the gas at 1–2 hours; a pH or rate that is not improving, falling consciousness, secretions or shock mean intubation, while a low presenting pH alone does not bar a closely watched trial."),
]

PRIMER = "Spirometry compares FEV₁ (volume blown out in the first second) with FVC (the whole forced breath): in airflow obstruction FEV₁ falls more than FVC, so the ratio drops below 0.7, whereas in restrictive disease such as ILD both fall and the ratio is normal or high. Compliance is the change in volume per unit change in pressure; emphysema destroys elastic tissue, so the lung is floppy (high compliance) and has little recoil to drive air out. Type 2 respiratory failure means a raised PaCO₂ (>45 mmHg, 6 kPa); the pH shows how acute it is, because the kidneys take days to retain bicarbonate, so a low pH means the rise is recent. On NIV, the inspiratory pressure (IPAP) minus the expiratory pressure (EPAP, equivalent to PEEP) is the pressure support that generates each tidal volume."

L = {}

L['COPD-01'] = dict(
  sub="Respiratory → COPD → The basic lesion",
  step=1,
  intro="The deck starts with the lesion, because everything later — trapped air, intrinsic PEEP, hypercapnia — follows from it. COPD narrows the small airways and destroys the elastic tissue that normally pulls them open and pushes air out.",
  parts=[
    ('a', "**Irreversible expiratory airflow limitation.** The limit is on expiration: inspiration is active and holds the airways open, whereas expiration relies on recoil and the airways narrow as the chest pressure rises. ‘Irreversible’ means not fully reversible with bronchodilators, which separates it from asthma (COPD-05)."),
    ('b', "**Raised resistance of small conducting airways (small-airway disease, chronic bronchitis), and raised lung compliance with loss of elastic recoil from emphysema.** Inflammation, mucus and fibrosis narrow the airway lumen. Emphysema removes the alveolar walls that tether small airways open, so they collapse during expiration, and removes the recoil that drives air out — the lung becomes easy to inflate (high compliance) but slow to empty."),
    ('c', "**Peripheral airways below 2 mm diameter.** They contribute little to total resistance in health, so much of the disease is silent on simple tests until it is advanced."),
    ('d', "**Smoke and pollutants → oxidative stress, neutrophil inflammation and inactivated anti-proteases → proteolytic destruction; alpha-1 antitrypsin deficiency is the genetic form.** Neutrophil elastase digests the alveolar wall and alpha-1 antitrypsin normally neutralises it; oxidants in smoke inactivate it. In the inherited deficiency the emphysema is panacinar, basal and early; in smokers it is centrilobular and upper-lobe."),
  ],
  mimic=[
    ("Emphysema vs ARDS", "Emphysema: compliance up, recoil down, slow emptying. ARDS: compliance down, fast emptying."),
  ],
  traps=[
    ("“Lung compliance is reduced in emphysema” (COPD-14a)", "It is increased: the elastic tissue is destroyed, so the lung inflates easily but recoils poorly."),
  ],
  decode=[
    ("[pattern] Compliance and recoil in emphysema compared with fibrosis or ARDS", "Emphysema raises compliance and lowers recoil; fibrosis and ARDS lower compliance."),
  ],
  punch="COPD is fixed expiratory airflow limitation from narrowed small airways (<2 mm) and emphysema; emphysema raises compliance and removes recoil, so the lung empties slowly.",
)

L['COPD-02'] = dict(
  sub="Respiratory → COPD → Dynamic hyperinflation",
  step=2,
  intro="The slow-emptying lung of COPD-01 becomes dangerous when the next breath arrives too soon. Air left behind from each breath accumulates until the lung sits at a higher volume, and that trapped air explains intrinsic PEEP, the high work of breathing and the hypotension after intubation.",
  parts=[
    ('a', "**The next breath starts before expiration is complete, so end-expiratory volume climbs above FRC with each breath (raised RV and FRC).** Normally expiration ends at the relaxed volume of the respiratory system. If flow is still going when inspiration begins, the leftover volume is added to the next breath; the volume climbs until the extra recoil at the higher volume pushes the tidal volume out in the time available, and the lung settles at that new, higher end-expiratory volume. On the ventilator, the flow–time trace shows expiratory flow that does not return to zero before the next breath."),
    ('b', "**High expiratory resistance; short expiratory time; low elastic recoil; respiratory muscle dysfunction.** Resistance and low recoil slow the emptying; a fast rate, a long inspiration or a large tidal volume shortens the time allowed. A high minute ventilation (fever, acidosis, anxiety, over-ventilation by the clinician) is the commonest avoidable cause."),
    ('c', "**Time constant = resistance × compliance; both are high in COPD, so emptying is slow.** One time constant empties about 63% of the volume, two about 86%, three about 95% — so roughly three are needed for near-complete emptying. Diseases with low compliance (ILD, ARDS) have short time constants and empty quickly, which is why auto-PEEP belongs to obstructive, not restrictive, disease."),
    ('d', "**Intrinsic PEEP, higher elastic work of breathing, barotrauma, cardiovascular compromise, patient–ventilator dyssynchrony, misread pressures.** The trapped volume leaves alveolar pressure above zero at end-expiration (intrinsic PEEP, COPD-03); breathing at a high volume puts the muscles at a disadvantage and on the stiff upper part of the pressure–volume curve; high intrathoracic pressure cuts venous return (COPD-04) and is transmitted to the vessels, so CVP and pulmonary artery occlusion pressure read falsely high. Hypotension with a high wedge pressure can therefore come from trapped air, not a failing left ventricle."),
  ],
  table=dict(title="Ventilator changes that lengthen expiration", head=["Change", "Why it helps"], rows=[["**Lower respiratory rate**", "the largest gain in expiratory time per breath"], ["Lower tidal volume", "less volume to empty"], ["Higher inspiratory flow / shorter Ti", "the breath is delivered faster, leaving more time to exhale"], ["Bronchodilators, suction", "lower resistance, so a shorter time constant"], ["Accept permissive hypercapnia", "lower minute ventilation is the price of less trapping"]]),
  mimic=[
    ("Dynamic hyperinflation vs left-ventricular failure", "Both raise the wedge pressure and lower blood pressure; with trapping the expiratory flow does not reach zero and a disconnection briefly restores the pressure."),
  ],
  traps=[
    ("“Auto-PEEP results most commonly from distal airway obstruction in ILD or hypersensitivity pneumonitis” (65% right)", "ILD lowers compliance and shortens the time constant, so the lung empties fast; auto-PEEP comes from high resistance and high compliance, as in COPD and asthma."),
    ("“Hypotension with raised PAOP in a ventilated COPD patient is LV failure”", "Trapped air raises intrathoracic pressure, which lowers venous return and is transmitted into the PA catheter reading; the flow trace not returning to zero is the clue."),
    ("“Intubated asthmatic, pH 7.16, PaCO₂ 66: raise the rate to clear CO₂”", "A faster rate shortens expiration and worsens trapping. Lower the rate, raise inspiratory flow and accept the hypercapnia. The keyed option’s phrase ‘metabolic compensation’ is wrong: a bicarbonate of 25 means an acute, uncompensated respiratory acidosis."),
  ],
  decode=[
    ("Ventilated COPD, hypotension, raised PAOP, expiratory flow persisting into the next breath — mechanism? [DocT GT]", "Dynamic hyperinflation."),
    ("All true about mechanical ventilation EXCEPT [DocT QBank]", "The false one: auto-PEEP commonly from ILD. Peak pressure reflects resistance and compliance; plateau reflects compliance only."),
    ("Intubated asthmatic, worsening pH 7.16, PaCO₂ 66 — disorder and change? [Marrow]", "Acute respiratory acidosis; lower the rate (to about 20) and increase inspiratory flow."),
    ("Why does auto-PEEP happen? [NEET 2024]", "Incomplete exhalation because expiratory time is too short for the time constant."),
  ],
  punch="Dynamic hyperinflation is air that a slow-emptying lung (high resistance × high compliance) cannot get out before the next breath; the fix is more expiratory time — lower rate, faster inspiration, accept hypercapnia — never a faster rate.",
)

L['COPD-03'] = dict(
  sub="Respiratory → COPD → Intrinsic PEEP and the work of breathing",
  step=2,
  intro="Trapped air leaves a positive pressure in the alveoli at the end of expiration (COPD-02). This card asks what that pressure costs the patient with every breath, and the one question tests why adding external PEEP helps.",
  parts=[
    ('a', "**The patient must first generate a negative pressure equal to intrinsic PEEP before any flow or trigger occurs: an inspiratory threshold load.** Flow into the lung needs alveolar pressure below the pressure at the airway opening. With PEEPi of 8, the muscles must lower alveolar pressure by 8 cmH₂O simply to reach zero flow, and only then can the ventilator sense the effort; much of the effort is wasted, and weak efforts fail to trigger at all. External PEEP set below PEEPi (commonly up to about 80% of it) raises the circuit pressure, so the gap the patient must overcome shrinks; because the narrowed airways limit flow, this does not add to the trapped volume as long as it stays below PEEPi."),
    ('b', "**A larger pressure gradient is needed for a given flow (resistance); more dead space, so a higher minute volume is needed for a normal CO₂.** Emphysema creates ventilated but poorly perfused units, so a larger share of each breath is wasted, and the patient must breathe more to clear the same CO₂ — which shortens expiration and worsens the trapping."),
    ('c', "**Flattened diaphragm and altered chest-wall geometry; resistive loads; hypoxaemia and acidosis impair muscle metabolism; cachexia; steroids and malnutrition.** A flattened diaphragm has short fibres and a large radius of curvature, so it generates little pressure for its tension. Supply is limited while demand is high, so fatigue and hypercapnia follow."),
  ],
  mimic=[
    ("Ineffective triggering vs double triggering", "Ineffective (missed) triggering comes from PEEPi: efforts appear as dips in the flow trace with no breath. Double triggering is two breaths for one effort, from an inspiratory time shorter than the patient’s."),
  ],
  traps=[
    ("“External PEEP lengthens expiratory time”", "It does not change expiratory time; it narrows the gap between alveolar and circuit pressure, lowering the threshold load."),
    ("“External PEEP increases the gradient between alveoli and circuit”", "It reduces it; that is how it helps the patient trigger."),
  ],
  decode=[
    ("AECOPD on BiPAP, distressed, failing to trigger — how does external PEEP reduce work of breathing? [DocT GT]", "It reduces the threshold load imposed by PEEPi, so the patient’s effort reaches the trigger sooner."),
  ],
  punch="Intrinsic PEEP is a threshold the patient must pull through before every breath; external PEEP set just below it lowers that threshold without adding hyperinflation.",
)

L['COPD-04'] = dict(
  sub="Respiratory → COPD → Positive pressure and the circulation",
  step=3,
  intro="Trapped air already raises intrathoracic pressure (COPD-02); positive-pressure ventilation adds more. This card explains why the blood pressure falls, and the one question tests the same physiology in ARDS: what raises pulmonary vascular resistance.",
  parts=[
    ('a', "**Raised intrathoracic pressure → less venous return (preload); hyperinflation compresses alveolar vessels and hypoxia constricts them → higher RV afterload.** Venous return depends on the gradient from the veins to the right atrium; raising pleural pressure narrows it. Pulmonary vascular resistance is lowest near FRC: above it, alveolar vessels are stretched and squeezed by the distended alveoli, so positive pressure on an over-inflated lung raises the resistance the right ventricle pumps against."),
    ('b', "**RV dilates, septum shifts left (ventricular interdependence) → LV filling falls.** The two ventricles share a septum and the pericardium, so a distended right ventricle leaves less room for the left."),
    ('c', "**Fall in blood pressure, worst just after intubation.** At that moment sedatives remove sympathetic tone, the patient is often dry after days of poor intake, and bagging is usually too fast, adding trapped air. If the pressure falls, disconnect the ventilator for 30–60 seconds: if it recovers as the chest empties, trapping was the cause; if not, think of tension pneumothorax."),
  ],
  mimic=[
    ("Trapping vs tension pneumothorax after intubation", "Both cause hypotension and high pressures; disconnection restores the blood pressure in trapping but not in a tension pneumothorax, which needs decompression."),
  ],
  traps=[
    ("“Decreased alveolar pressure raises PVR”", "Higher alveolar pressure compresses alveolar vessels and raises PVR; prostacyclin and systemic vasodilators lower it."),
  ],
  decode=[
    ("Ventilated severe ARDS, new RV dysfunction, rising PA pressures with stable left-sided pressures — what raised PVR? [DocT GT]", "Positive-pressure ventilation."),
    ("[pattern] COPD hypotensive minutes after intubation — first step?", "Disconnect from the ventilator and let the chest empty; then slower rate, fluid."),
  ],
  punch="Positive pressure on a hyperinflated chest cuts venous return and squeezes the alveolar vessels, so the right ventricle fails to fill and to empty; when the pressure falls after intubation, disconnect first.",
)

L['COPD-05'] = dict(
  sub="Respiratory → COPD → Asthma versus COPD",
  step=1,
  intro="The two obstructive diseases look alike at the bedside, but they differ in inflammation, reversibility and the way they fail. The questions test the last: an old smoker with hyperinflation and a high PaCO₂ has type 2 failure from COPD.",
  parts=[
    ('a', "**Asthma: eosinophils, mast cells, T-lymphocytes; COPD: neutrophils, macrophages.** Asthma is driven by type 2 (Th2) inflammation, which is why it responds to steroids; COPD inflammation is neutrophilic and responds less. A raised blood eosinophil count in COPD marks those most likely to benefit from inhaled steroids: the benefit grows with the count and is clearest at ≥300/µL (COPD-07)."),
    ('b', "**Asthma reversible (becomes fixed with time); COPD irreversible.** Long-standing asthma remodels the airway and the obstruction can become fixed, so reversibility alone does not always separate them."),
    ('c', "**Airway hyper-responsiveness, with mucosal oedema, mucus hypersecretion and wall thickening.** The airways narrow too much and too easily in response to triggers."),
    ('d', "**Type 2 (hypercapnic).** V/Q mismatch with a large dead space, a high CO₂ load and tiring muscles cannot be matched by ventilation, so PaCO₂ rises. Acute asthma, by contrast, usually starts with a low PaCO₂ from hyperventilation (COPD-08)."),
  ],
  mimic=[
    ("Acute asthma vs AECOPD on the gas", "Asthma: low PaCO₂ early, so a normal value is ominous. COPD: often a high PaCO₂, and the pH says whether it is acute."),
  ],
  traps=[
    ("“PaO₂ 55, PaCO₂ 70 with hyperinflation is type 1 failure or acute asthma” (89% right)", "A raised PaCO₂ defines type 2; a 72-year-old smoker with flat diaphragms points to COPD."),
    ("“In mild asthma, submucosal mast cells are fewer and mainly tryptase–chymase type” (87% right)", "That pattern belongs to severe asthma; mild asthma keeps tryptase-only mast cells, as in normal lung."),
  ],
  decode=[
    ("Smoker, RR 36, cyanosed, PaO₂ 55, PaCO₂ 70, hyperinflated chest X-ray — diagnosis? [DocT QBank]", "Type 2 respiratory failure due to COPD."),
    ("All true about asthma pathology EXCEPT [DocT GT]", "The statement placing reduced, tryptase–chymase mast cells in mild asthma."),
  ],
  punch="Asthma is eosinophilic, reversible and hyper-responsive; COPD is neutrophilic and fixed, and its exacerbations fail as type 2 (hypercapnic) failure.",
)

L['COPD-06'] = dict(
  sub="Respiratory → COPD → Acute exacerbation",
  step=4,
  intro="An exacerbation is what brings the COPD patient to the ICU. The card defines it and lists its cause and severity signs; the questions test how often bacteria are found and which single sign marks a severe attack.",
  parts=[
    ('a', "**Worsening of respiratory symptoms that leads to a change in medication.** This is the older operational GOLD wording. Since 2023 GOLD uses the Rome definition: dyspnoea and/or cough and sputum that worsen over 14 days or less, often with tachypnoea or tachycardia, caused by infection, pollution or another insult."),
    ('b', "**Increased dyspnoea, increased sputum volume, increased sputum purulence (Anthonisen).** All three make a type 1 exacerbation; Anthonisen found antibiotics helped most when purulence was present. GOLD suggests antibiotics when purulence is accompanied by more dyspnoea or more sputum, or when the patient needs ventilation."),
    ('c', "**Infection: respiratory viruses; Haemophilus influenzae, Streptococcus pneumoniae, Moraxella catarrhalis.** Rhinovirus is the commonest virus. Bacteria are found in the lower airways in about half of exacerbations, but many patients are colonised when stable, so a positive sputum does not prove a bacterial cause. Pseudomonas appears in very severe disease."),
    ('d', "**Accessory muscle use, paradoxical chest-wall movement, new or worse central cyanosis, peripheral oedema, haemodynamic instability, altered mental status.** Altered mental status is the most important single sign: it means CO₂ narcosis or exhaustion, so the patient needs a blood gas, escalation and readiness to intubate (COPD-10, COPD-12)."),
  ],
  mimic=[
    ("Exacerbation vs pneumonia, pulmonary embolism or heart failure", "These cause or mimic exacerbations and are looked for in every admission; a new infiltrate makes it pneumonia."),
  ],
  traps=[
    ("“Sputum colour grades severity”", "Purulence suggests bacteria and guides antibiotics; severity is graded by effort, mental state, haemodynamics and the gas."),
    ("“Bacteria in sputum prove a bacterial exacerbation”", "Colonisation is common; about half of exacerbations have lower-airway bacteria."),
  ],
  decode=[
    ("Share of AECOPD with organisms in the lower airways [Marrow]", "About 50%."),
    ("Most important sign of a severe COPD exacerbation [Marrow]", "Change in mental status."),
  ],
  punch="An exacerbation is a short-term worsening of dyspnoea, sputum and purulence, mostly infective; altered mental status is the sign that it is severe.",
)

L['COPD-07'] = dict(
  sub="Respiratory → COPD → GOLD spirometric grades",
  step=4,
  intro="Spirometry makes the diagnosis and grades airflow limitation, but the grade does not choose the treatment. The questions test the cut-offs, the obstructive pattern and the ABE groups that decide discharge inhalers.",
  parts=[
    ('a', "**Post-bronchodilator FEV₁/FVC <0.7.** The ratio, not FEV₁, diagnoses obstruction; post-bronchodilator values remove the reversible part, so a low ratio that persists is fixed limitation. ILD and other restrictive diseases reduce both volumes and keep the ratio normal or high."),
    ('b', "**GOLD 1 mild ≥80; 2 moderate 50–79; 3 severe 30–49; 4 very severe <30 (FEV₁ % predicted).** Each boundary value belongs to the milder grade: FEV₁ of exactly 50% is GOLD 2, and exactly 30% is GOLD 3."),
  ],
  table=dict(title="Grade versus group: which decides the inhaler (GOLD 2025)", head=["Group", "Exacerbations in the past year", "Symptoms", "Start with"], rows=[["A", "0–1 moderate, none admitted", "mMRC 0–1, CAT <10", "a bronchodilator"], ["B", "0–1 moderate, none admitted", "mMRC ≥2, CAT ≥10", "LABA + LAMA"], ["**E**", "**≥2 moderate or ≥1 admitted**", "any", "**LABA + LAMA**; add ICS if eosinophils ≥300/µL"]]),
  mimic=[
    ("GOLD grade vs ABE group", "The grade (1–4) describes airflow; the group (A, B, E) comes from symptoms and exacerbations and chooses therapy."),
  ],
  traps=[
    ("“FEV₁ 50% is GOLD 3” (only 64% right)", "GOLD 3 is 30–49%; 50% is the bottom of GOLD 2."),
    ("“Discharge after an admitted exacerbation on salbutamol alone, or straight to triple therapy” (only 40% right)", "One hospitalised exacerbation puts him in group E: LABA + LAMA. Inhaled steroid is added only if eosinophils are ≥300/µL, because it raises pneumonia risk."),
    ("“Low FEV₁ with low ratio is ILD or restriction”", "A low ratio is obstruction; restriction keeps the ratio normal or high."),
  ],
  decode=[
    ("FEV₁/FVC <0.7, FEV₁ 50% predicted — GOLD grade? [DocT QBank]", "GOLD 2."),
    ("Admitted COPD exacerbation — discharge inhalers? [DocT QBank]", "LABA + LAMA (formoterol plus tiotropium)."),
    ("Low FEV₁, FEV₁/FVC <0.7 — diagnosis? [NEET 2025]", "COPD."),
  ],
  punch="A post-bronchodilator FEV₁/FVC below 0.7 diagnoses COPD and FEV₁ grades it (≥80, 50–79, 30–49, <30), but exacerbation history and symptoms (group E) choose LABA + LAMA at discharge.",
)

L['COPD-08'] = dict(
  sub="Respiratory → Asthma → Severe exacerbation criteria",
  step=4,
  intro="Severity in asthma is judged at the bedside and confirmed by peak flow and the gas. The six questions turn on one point above all: a breathless asthmatic should have a low PaCO₂, so a normal one means he is tiring.",
  parts=[
    ('a', "**Cannot complete a sentence in one breath; accessory muscle use; RR >30; HR >120; pulsus paradoxus; no response to treatment.** These are the GINA-style severe features. Pulsus paradoxus comes from large negative swings in pleural pressure that pool blood in the lungs and shift the septum on inspiration, so it is present while the patient can still generate effort (COPD-09)."),
    ('b', "**PEFR ≤50% of predicted.** Peak flow is the objective measure of airflow; it is checked again after treatment."),
    ('c', "**PaO₂ <60 mmHg (8 kPa) on air; PaCO₂ >45 mmHg (6 kPa).** Early in an attack the drive to breathe is high and PaCO₂ is low. A PaCO₂ that rises to normal (about 40–45) means ventilation can no longer keep up — the muscles are failing. Grading differs by guideline: BTS calls a normal PaCO₂ ‘life-threatening’ and a raised one ‘near-fatal’."),
  ],
  table=dict(title="BTS/SIGN (2019) levels in adult acute asthma", head=["Level", "Any one of"], rows=[["Acute severe", "PEF 33–50%; RR ≥25; HR ≥110; cannot complete sentences"], ["**Life-threatening**", "**PEF <33%; SpO₂ <92%; PaO₂ <8 kPa; ‘normal’ PaCO₂**; silent chest, cyanosis, poor effort; arrhythmia; exhaustion, altered consciousness; hypotension"], ["Near-fatal", "raised PaCO₂, or needing ventilation with raised inflation pressures"]]),
  mimic=[
    ("Normal PaCO₂ in asthma vs in COPD", "In asthma it marks fatigue; in COPD a high PaCO₂ may be chronic, and the pH decides."),
  ],
  traps=[
    ("“PaCO₂ 42 after bronchodilators means a successful response or is normal” (only 41% right)", "In acute asthma PaCO₂ should be low; normal means impending respiratory failure."),
    ("“PaCO₂ 42, pH 7.35 means asthma with normal ventilation” (74% right)", "Same point: in a breathless asthmatic who cannot speak, a normal PaCO₂ is the warning."),
    ("“PEF 68% after 2 h in the ED: discharge”", "That is short of the usual emergency-department discharge bar, a PEF above 70% sustained for an hour after the last bronchodilator; and patients discharged after less than about 2 hours of treatment relapse often. Observe and recheck."),
  ],
  decode=[
    ("Acute asthma, PaCO₂ 42 after bronchodilators — implication? [DocT GT, two tests]", "Impending respiratory failure."),
    ("Severe wheeze, cannot speak, RR 28, PaCO₂ 42, pH 7.35 [DocT QBank]", "Asthma exacerbation with impending respiratory failure."),
    ("Which finding marks life-threatening asthma? [Marrow]", "PaO₂ 7.7 kPa (below 8 kPa)."),
    ("ED asthma, PEF 68% after 2 h — disposition? [Marrow]", "Observe for 2 more hours and recheck PEF and symptoms."),
  ],
  punch="Severe asthma is RR >30, HR >120, PEF ≤50%, and words not sentences; in that patient a PaCO₂ that is ‘normal’ means he is tiring and about to fail.",
)

L['COPD-09'] = dict(
  sub="Respiratory → Asthma → Imminent respiratory arrest",
  step=4,
  intro="Beyond ‘severe’ is the asthmatic about to stop breathing. The danger is that he can look better: quieter, calmer, less pulsus — because he can no longer move air or generate effort.",
  parts=[
    ('a', "**Silent chest, weak respiratory effort.** Wheeze needs airflow; when flow almost stops, the chest goes quiet."),
    ('b', "**Paradoxical thoraco-abdominal movement.** The fatigued diaphragm is sucked up by the accessory muscles, so the abdomen moves in on inspiration."),
    ('c', "**Confusion or coma.** Hypercapnia and hypoxaemia; a drowsy asthmatic is not resting."),
    ('d', "**Bradycardia and hypotension.** Late signs of hypoxia and of trapped air impeding venous return; arrest follows."),
    ('e', "**Cyanosis.** Central cyanosis appears only when a large amount of haemoglobin is deoxygenated (roughly 5 g/dL in capillary blood), so it is a late sign of severe hypoxaemia, and it is easily missed in anaemia."),
    ('f', "**Absence of pulsus paradoxus.** Pulsus needs large swings of pleural pressure; when the muscles fail, the swings and the pulsus vanish."),
  ],
  mimic=[
    ("Improving vs exhausted asthmatic", "Both get quieter. Improvement brings better PEF, easier speech and a clear sensorium; exhaustion brings drowsiness, poor effort and a rising PaCO₂."),
  ],
  traps=[
    ("“Absent pulsus or a quiet chest is reassuring” (COPD-14d)", "Together with drowsiness they mark imminent arrest."),
  ],
  decode=[
    ("Asthmatic now sleeping, less wheeze, pulsus falls from 14 to 5 — next step? [Marrow]", "ABG now and prepare to intubate."),
  ],
  punch="Silent chest, drowsiness, bradycardia and a pulsus that disappears mean the muscles have failed, not that the asthma has eased: intubate.",
)

L['COPD-10'] = dict(
  sub="Respiratory → COPD → NIV in an exacerbation",
  step=5,
  intro="This is the most-asked card of the deck: 13 questions, almost all a COPD patient with a blood gas and four options. NIV is the first treatment for an exacerbation with hypercapnic acidosis, because it does the extra work the tiring muscles cannot, while bronchodilators, steroids and antibiotics take effect.",
  parts=[
    ('a', "**Initial treatment of choice.** For acute or acute-on-chronic hypercapnic failure in an exacerbation, ERS/ATS (2017) give a strong recommendation for bilevel NIV, and GOLD agrees. Inspiratory pressure unloads the muscles and enlarges the tidal volume; expiratory pressure offsets intrinsic PEEP (COPD-03), so less effort triggers each breath; the patient breathes slower and deeper and PaCO₂ falls. It is started alongside full medical treatment and controlled oxygen, not after the drugs have failed, and it is not a substitute for intubation in a patient who is arresting or cannot protect the airway."),
    ('b', "**Respiratory distress (dyspnoea, accessory muscles, paradoxical abdominal motion, tachypnoea) and hypercapnic acidosis, pH <7.35.** The acidosis is the key: a raised PaCO₂ with a normal pH is chronic, compensated by bicarbonate, and needs controlled oxygen, not NIV. A pH below 7.35 with PaCO₂ above 45 mmHg (BTS: >6.5 kPa persisting despite optimal medical treatment) means the rise is acute. A low pH alone does not bar a trial (COPD-12). Drowsiness from CO₂ narcosis is only a relative contraindication: a rousable patient can have a closely watched trial, because the narcosis often lifts within 1–2 hours. Cardiogenic pulmonary oedema alongside is an extra reason for NIV, not a contraindication."),
    ('c', "**Intubation risk down by 65%; mortality down by 46%; shorter stay; fewer treatment failures.** These are the Cochrane review figures (Osadnik 2017: 17 trials, 1264 patients): intubation RR 0.36 (one intubation avoided for every 5 treated), mortality RR 0.54 (one death avoided for every 12), hospital stay about 3 days shorter. This is why ‘NIV delays intubation and raises mortality’ is false for COPD — the opposite of its record in ILD or severe hypoxaemia."),
  ],
  table=dict(title="Reading the gas in a COPD exacerbation", head=["Gas", "Meaning", "Action"], rows=[["High PaCO₂, pH ≥7.35", "chronic, compensated", "controlled oxygen (SpO₂ 88–92%), medical treatment"], ["**pH <7.35, PaCO₂ >45**", "**acute hypercapnic failure**", "**NIV** with medical treatment"], ["pH <7.25", "severe acidosis, higher failure rate", "NIV trial in ICU/HDU with intubation at hand"], ["Arrest, peri-arrest, cannot protect the airway, pH extreme (e.g. 6.9)", "NIV unsafe", "intubate"]]),
  mimic=[
    ("COPD vs ILD exacerbation", "COPD hypercapnia responds to pressure support; stiff, non-recruitable ILD lungs often fail NIV, and a failed trial only delays intubation."),
    ("NIV vs HFNC in hypercapnic COPD", "ERS (2022) suggests trying NIV before HFNC; HFNC is a fallback when NIV is not tolerated."),
  ],
  traps=[
    ("“pH 7.28, PaCO₂ 75, RR 30, anxious: intubate” (DocT key; only 23% chose it)", "The key is wrong. An awake patient with pH 7.28 is a textbook NIV case; intubation is for failure of NIV, arrest, falling consciousness, secretions or shock."),
    ("“High-flow oxygen, a non-rebreather at 15 L or 6 L/min by cannula” (50–62% right on several stems)", "More oxygen worsens hypercapnia (COPD-11b); target SpO₂ 88–92% and treat the acidosis with NIV."),
    ("“BiPAP in such patients raises mortality by delaying intubation, or lengthens stay”", "In COPD it lowers intubation, mortality and length of stay."),
    ("“Coexisting cardiogenic pulmonary oedema is a contraindication”", "It is an indication; positive pressure helps both."),
    ("“Altered mental status is an absolute contraindication”", "It is relative; a rousable patient with CO₂ narcosis can be trialled under close watch, with intubation if he does not improve. The DocT key (D) is right in calling it relative."),
    ("“Steroids and antibiotics first” or “inhaled corticosteroids”", "Steroids and antibiotics are given alongside but do not correct the acidosis now; inhaled steroids have no role in the acute event."),
  ],
  decode=[
    ("Smoker, accessory muscles, prolonged expiration, pH 7.32, PaCO₂ 52 — most likely to benefit? [DocT QBank, DocT GT]", "NIV — pH below 7.35 with a raised PaCO₂, even modestly."),
    ("COPD, pH 7.28, PaCO₂ 75, PaO₂ 50–55 on 2 L — next step? [DocT QBank, DocT GT, four versions]", "Start NIV, not more oxygen and not intubation (one DocT key says intubate; it is wrong)."),
    ("COPD, pH 7.27, PaCO₂ 90, somnolent but rousable, possible pulmonary oedema, on BiPAP — which is true? [DocT GT, two tests]", "His altered mental status is a relative contraindication."),
    ("Confused but rousable, pH 7.26, PaCO₂ 61, HCO₃ 30 — next step? [DocT GT]", "Bilevel NIV."),
    ("NIV is NOT useful in which condition? [NEET 2025]", "ILD exacerbation — not COPD, cardiogenic oedema or high-risk post-extubation."),
  ],
  extra=[
    dict(q="Where does NIV work, and where does it fail? [NEET 2025]", a="It works where positive pressure reverses the problem: hypercapnic COPD, cardiogenic pulmonary oedema, high-risk extubation. It fails in ILD/IPF exacerbation (stiff lungs that will not recruit) and delays intubation in severe hypoxaemia."),
  ],
  punch="In a COPD exacerbation, a pH below 7.35 with a raised PaCO₂ means NIV first, with controlled oxygen; it cuts intubation by about two-thirds and death by nearly half, and drowsiness from CO₂ is only a relative bar.",
)

L['COPD-11'] = dict(
  sub="Respiratory → COPD → Setting up NIV",
  step=5,
  intro="NIV helps only if the settings match the obstructed lung. Each setting on the card serves the same aim as the ventilator changes in COPD-02: unload the muscles, offset intrinsic PEEP and leave time to breathe out, while keeping oxygen controlled.",
  parts=[
    ('a', "**Pressure support; inspiratory pressure 6–8 cmH₂O, PEEP 3–5 cmH₂O. Patient seated and reassured; avoid leaks.** The inspiratory pressure above PEEP produces the tidal volume; PEEP (EPAP) offsets intrinsic PEEP and flushes CO₂ from the mask. Starting low helps the patient accept the mask; pressures are then raised quickly. BTS/ICS (2016) starts higher, at an IPAP of about 15 cmH₂O (EPAP commonly 3–5), and raises it to 20–30 cmH₂O within 10–30 minutes, faster when the acidosis is worse; a full face mask is the usual first interface. Leaks cause missed triggers and prolonged inspiration."),
    ('b', "**FiO₂ for SaO₂ ≥88% (88–92%).** Too much oxygen raises PaCO₂. The main reason is worsening V/Q matching: oxygen releases hypoxic vasoconstriction, so blood goes to poorly ventilated units and dead space rises. The Haldane effect (oxygenated haemoglobin holds less CO₂) adds a smaller share, about a quarter in Aubier’s studies; loss of hypoxic drive matters least."),
    ('c', "**Inspiratory trigger 0.5–1 L/min; expiratory trigger (cycling) at 50% of peak inspiratory flow.** A sensitive trigger lowers the effort needed. In COPD the inspiratory flow falls slowly, so cycling at the usual 25% keeps inspiration going after the patient has started to breathe out; cycling at 50% ends it earlier and gives more time to exhale."),
    ('d', "**Raise pressures in steps of 1–2 cmH₂O to RR <25/min and tidal volume 6–8 mL/kg.** A falling rate and an adequate tidal volume show the muscles are unloaded; the gas at 1–2 hours confirms it (COPD-12)."),
  ],
  mimic=[
    ("BiPAP vs CPAP", "BiPAP gives two pressures, supporting inspiration and holding PEEP in expiration; CPAP gives one constant pressure and does not add ventilation, so it does not lower PaCO₂."),
  ],
  traps=[
    ("“PaCO₂ rises on 4 L/min oxygen because of the Haldane effect” (DocT key; 59% chose it)", "Haldane contributes, but most of the rise comes from worsening V/Q mismatch and dead space; loss of hypoxic drive is the least. The DocT key is B (Haldane); on physiology, increased dead space (C) is the better answer."),
    ("“BiPAP delivers a constant pressure, high-frequency oscillation or fixed-flow oxygen” (93–98% right)", "Those describe CPAP, HFOV and a cannula; BiPAP is two levels of pressure."),
  ],
  decode=[
    ("COPD on 4 L/min oxygen, PaCO₂ rises within 1 h — mechanism? [DocT GT]", "Keyed: Haldane effect; physiologically, V/Q worsening with more dead space dominates."),
    ("Primary mechanism by which BiPAP improves oxygenation and work of breathing [DocT QBank, two versions]", "Two levels of positive pressure (IPAP and EPAP) supporting inspiration and expiration."),
    ("Smoker, pH 7.32, PaCO₂ 52 — most likely to benefit? [DocT QBank]", "NIV (COPD-10)."),
  ],
  punch="Set NIV to unload and to empty: enough inspiratory pressure for RR <25 and 6–8 mL/kg, PEEP to offset intrinsic PEEP, early cycling (50%), and oxygen only to SpO₂ 88–92%.",
)

L['COPD-12'] = dict(
  sub="Respiratory → COPD → NIV failure and intubation",
  step=6,
  intro="NIV saves most patients, but failure caught late is deadly, so NIV is a trial with a deadline. The questions test when to judge it, what predicts success and when the starting gas is so bad that the tube comes first.",
  parts=[
    ('a', "**After 2 hours (2–4 h).** BTS/ICS (2016) asks for a blood gas before and after starting NIV, and most protocols recheck it at 1–2 hours and after any change in settings. An early fall in respiratory rate and rise in pH (within the first few hours; BTS cites 4 h) is the best predictor of success, so the first recheck shows the trend and the 2–4 h window confirms it."),
    ('b', "**Worsening pH or respiratory rate; deteriorating mental status; cannot clear secretions; hypotension; uncorrected hypoxaemia.** First fix what can be fixed — mask fit, leak, pressures, asynchrony; if the patient is still worsening, the trial has failed."),
    ('c', "**NIV failure; respiratory arrest or impending arrest; persistent or worsening acidosis (pH <7.25) despite NIV; reduced consciousness; cannot clear secretions; haemodynamic instability.** The 7.25 cut-off applies to the pH on NIV, not at presentation: a low starting pH is not a bar to a closely watched trial in a unit where intubation is immediately available (BTS). An extreme gas such as pH 6.9 with PaCO₂ 110, or a peri-arrest patient, goes straight to intubation. After intubation, ventilate as in COPD-02 and expect a fall in blood pressure (COPD-04)."),
  ],
  table=dict(title="The pH numbers that are confused", head=["pH", "Where it belongs"], rows=[["<7.35", "start NIV in an exacerbation"], ["<7.25 **despite NIV**", "intubate"], ["7.30", "lower limit of the ARDSNet target"], ["7.15–7.20", "usual floor for permissive hypercapnia"]]),
  mimic=[
    ("Failure of NIV vs failure to fit NIV", "Leak, a poor mask or asynchrony are fixed first; failure is worsening despite a working set-up."),
  ],
  traps=[
    ("“pH 7.28 at presentation means intubate” (DocT key; only 23% chose it)", "The key is wrong; pH 7.28 in an awake patient is for NIV. Intubate for pH <7.25 that persists despite NIV."),
    ("“Continue NIV, give naloxone or try HFNC when he becomes somnolent with minimal effort on NIV” (98% right)", "Worsening consciousness with poor effort on NIV is failure: intubate."),
    ("“A presenting pH below 7.25 always bars NIV”", "BTS allows a trial with intubation at hand; but at pH 6.9 with PaCO₂ 110 intubation is the safe answer."),
  ],
  decode=[
    ("NIV started; over 30 min more somnolent with minimal effort — next step? [DocT GT]", "Endotracheal intubation."),
    ("Early finding most predictive of NIV success [DocT GT]", "Improved gas exchange within 2 hours."),
    ("COPD, pH 6.9, PaCO₂ 110 — management? [NEET 2025]", "Immediate intubation and ventilation."),
    ("COPD, pH 7.28, PaCO₂ 75 — next step? [DocT QBank]", "NIV (one version keys intubation; it is wrong)."),
  ],
  punch="Judge NIV by the gas at 1–2 hours: a pH still below 7.25, falling consciousness, secretions or shock mean intubate, but a low presenting pH alone does not.",
)

L['COPD-13'] = dict(
  sub="Respiratory → Asthma → NIV in an exacerbation",
  step=5,
  intro="NIV works in COPD; whether it works in asthma is less clear. The mechanisms are plausible, but the trials are small, so it is a cautious trial at most and never a reason to delay intubation.",
  parts=[
    ('a', "**Possible direct bronchodilating effect.** Positive pressure may splint the airways open."),
    ('b', "**Offsets intrinsic PEEP, limiting dynamic hyperinflation.** As in COPD-03, external PEEP lowers the threshold load."),
    ('c', "**Recruits collapsed alveoli; improves V/Q mismatch.** Mucus plugs and airway closure leave perfused units unventilated; positive pressure can reopen some of them, so less blood passes through poorly ventilated lung and oxygenation improves."),
    ('d', "**Reduces the work of breathing.** Pressure support takes over part of the effort of tiring muscles."),
  ],
  mimic=[
    ("Asthma vs COPD for NIV", "COPD: strong evidence and a strong recommendation. Asthma: weak evidence; ERS/ATS (2017) make no recommendation."),
  ],
  traps=[
    ("“NIV is standard first-line in severe asthma, as in COPD”", "The evidence is weak; a patient with features of imminent arrest (COPD-09) needs intubation."),
  ],
  decode=[
    ("[pattern] How might NIV help in acute asthma, and how strong is the evidence?", "It offsets PEEPi and unloads the muscles; evidence is weak compared with COPD."),
  ],
  punch="NIV may help asthma by offsetting intrinsic PEEP and unloading the muscles, but the evidence is weak, so it is a closely watched trial and never a delay to intubation.",
)

L['COPD-14'] = dict(
  sub="Respiratory → COPD → Revision: true or false",
  step=6,
  intro="A sweep through the deck. Each statement turns on one detail from an earlier card.",
  parts=[
    ('a', "**False — compliance is increased in emphysema; recoil is lost** (COPD-01)."),
    ('b', "**True — time constant = resistance × compliance, and both are high in COPD** (COPD-02)."),
    ('c', "**True — GOLD 3 (severe) is FEV₁ 30–49% predicted** (COPD-07)."),
    ('d', "**False — absent pulsus paradoxus in severe asthma is a sign of imminent arrest** (COPD-09)."),
    ('e', "**False — PaCO₂ 44 in acute severe asthma should be low; this is fatigue** (COPD-08)."),
    ('f', "**False — NIV starts below pH 7.35; pH <7.25 despite NIV means intubate** (COPD-10, COPD-12)."),
    ('g', "**True — positive pressure compresses alveolar vessels and raises RV afterload** (COPD-04)."),
  ],
  mimic=[],
  traps=[
    ("“A normal PaCO₂ in a severe asthmatic is reassuring” (74% right)", "It means ventilation is failing to keep up."),
  ],
  decode=[
    ("Severe wheeze, cannot speak, PaCO₂ 42, pH 7.35 — explanation? [DocT QBank]", "Impending respiratory failure."),
    ("[pattern] True/false on COPD numbers", "Compliance up in emphysema; GOLD 3 is 30–49%; NIV at pH <7.35, intubate at <7.25 despite NIV."),
  ],
  punch="Most errors here come from direction: compliance rises in emphysema, a normal PaCO₂ or absent pulsus in asthma is bad, and 7.35 starts NIV while 7.25 on NIV ends it.",
)

FLAGS = {}
FLAGS['COPD-02'] = "Marrow asthma-ventilation key (lower RR, raise flow) is right, but its wording ‘metabolic compensation’ is wrong: HCO₃ 25 means acute, uncompensated respiratory acidosis. Card is right."
FLAGS['COPD-06'] = "Card a uses the older GOLD definition (symptoms leading to a change in medication). Since GOLD 2023 the Rome definition is used: dyspnoea and/or cough and sputum worsening over ≤14 days, often with tachypnoea/tachycardia. Consider updating; explanation gives both."
FLAGS['COPD-08'] = "Card c lists PaCO₂ >45 as a ‘severe’ criterion (older GINA table); in BTS a normal PaCO₂ is life-threatening and a raised one near-fatal. Marrow also tests PaO₂ <8 kPa as life-threatening; the watch’s BTS list could add PaO₂ <8 kPa, exhaustion, arrhythmia, hypotension. Explanation gives the BTS table."
FLAGS['COPD-10'] = "One DocT QBank key (pH 7.28, PaCO₂ 75, RR 30, anxious) says intubate; GOLD and ERS/ATS 2017 make this an NIV case. Card is right; key is wrong (repeated under COPD-12)."
FLAGS['COPD-11'] = "DocT GT8 keys the Haldane effect for O₂-induced hypercapnia; physiological studies attribute most of the rise to V/Q worsening and dead space (option C). Card a’s starting pressures (6–8 over 3–5) are low against BTS/ICS 2016 (IPAP about 15, raised to 20–30 within 10–30 min); the watch already notes it, though BTS gives no fixed EPAP of 3 (3–5 is common practice). Card is not wrong."
FLAGS['COPD-12'] = "Same wrong DocT key as COPD-10 (intubate at presenting pH 7.28). NEET 2025 keys intubation at pH 6.9/PaCO₂ 110, consistent with the card’s spirit. Card is right."
