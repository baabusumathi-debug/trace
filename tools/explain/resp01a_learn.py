# RESP01A — Explain v3 ("Learn" depth): ARDS I — Definition, Epidemiology & Pathology. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP01A.md. Fields as TOX01, plus SPINE, PRIMER and step.

SPINE = [
  ("Insults that injure the lung", "ARDS follows a direct insult to the alveolar epithelium, such as pneumonia or aspiration, or an indirect one reaching the lung through the blood, such as sepsis or pancreatitis."),
  ("Diffuse alveolar damage in stages", "The injured lung passes from exudative oedema with hyaline membranes, through type II cell proliferation, to fibrosis in some patients."),
  ("Leaky barrier, shunt, small lung", "Protein-rich oedema floods alveoli that stay perfused, so hypoxaemia is from shunt and resists oxygen, and the lung left aerated is small rather than stiff."),
  ("Defining it: AECC to Berlin", "Berlin defines ARDS by four criteria — onset within a week, bilateral opacities, oedema not fully cardiac, and P/F ≤300 on PEEP ≥5 — and dropped the wedge pressure and the term ALI."),
  ("Grading, global reach and burden", "P/F grades it mild, moderate or severe; the 2023 definition stretches it to non-intubated patients and settings without blood gases; LUNG SAFE shows it is common, mostly moderate and under-recognised."),
  ("Mimics, prognosis and review", "Several conditions meet Berlin criteria without being ARDS, and BAL, echo and CT separate them — which matters because some respond to steroids."),
]

PRIMER = "The P/F ratio is arterial PO₂ in mmHg divided by FiO₂ as a fraction (PaO₂ 60 on FiO₂ 0.5 gives 120); the lower it is, the worse the oxygenation, and it is only comparable when PEEP is stated. PEEP is the pressure held in the airways at the end of expiration; it keeps collapsed alveoli open, so it changes the P/F ratio. Shunt means blood flowing past alveoli that receive no gas at all, whereas V/Q mismatch means alveoli that are ventilated, but too little for their blood flow — extra oxygen corrects the second, not the first. Compliance is the change in lung volume per unit of pressure; a low value means each breath needs more pressure."

L = {}

L['ARDS-01'] = dict(
  sub="Respiratory → ARDS → Landmarks",
  step=4,
  intro="Before the definitions, the landmarks that frame them. ARDS was first a bedside description, then a consensus definition revised twice, and all along it has had one histological picture behind it.",
  parts=[
    ('a', "**Ashbaugh, 1967 (12 patients; Lancet).** Ashbaugh and colleagues described adults with acute tachypnoea, cyanosis refractory to oxygen, stiff lungs and diffuse infiltrates after varied insults — the features that every later definition tried to pin down."),
    ('b', "**AECC 1994 → Berlin 2012 → new global definition 2023.** AECC gave the first shared criteria; Berlin fixed its gaps (timing, PEEP, wedge pressure, ALI) — see ARDS-05; the 2023 definition widened it to non-intubated patients and low-resource settings (ARDS-06)."),
    ('c', "**Diffuse alveolar damage with hyaline membranes.** Hyaline membranes are layers of fibrin and cell debris lining the alveoli, laid down in the exudative stage (ARDS-08). A post-mortem lung at one week shows them."),
  ],
  mimic=[
    ("Diffuse alveolar damage vs ARDS", "DAD is the pathology, ARDS the clinical syndrome; only about half of patients who meet clinical criteria show DAD at autopsy (one criticism of Berlin, ARDS-05)."),
  ],
  traps=[
    ("“Hyaline membranes mark the fibrotic stage”", "They are the hallmark of the early exudative stage, within the first week."),
  ],
  decode=[
    ("[pattern] Histological hallmark of ARDS / post-mortem lung at one week", "Diffuse alveolar damage with hyaline membranes."),
    ("[pattern] Order of ARDS definitions", "AECC 1994, Berlin 2012, global definition 2023."),
  ],
  punch="ARDS is a clinical syndrome defined by consensus — AECC, Berlin, then the 2023 global definition — and its pathology, when present, is diffuse alveolar damage with hyaline membranes.",
)

L['ARDS-02'] = dict(
  sub="Respiratory → ARDS → Epidemiology (LUNG SAFE)",
  step=5,
  intro="Once ARDS could be graded, LUNG SAFE asked how often it occurs and how well it is treated. It is the study behind the statements that ARDS is common and under-recognised.",
  parts=[
    ('a', "**459 ICUs, 50 countries, 29,144 patients.** A four-week, prospective snapshot of ICU admissions in the winter of 2014 (Bellani, JAMA 2016) — large enough to give real-world proportions rather than trial figures."),
    ('b', "**Mild 30.0%, moderate 46.6%, severe 23.4%.** Moderate is the commonest grade; severe is the smallest group."),
    ('c', "**Common (about 10% of ICU admissions, 23% of ventilated patients) and under-recognised and under-treated; hospital mortality about 40%.** Clinicians recognised only about 60% of cases, fewer in mild ARDS, plateau pressure was often not measured, and few patients with severe ARDS were proned. Mortality rose with grade."),
  ],
  mimic=[
    ("LUNG SAFE mortality vs Berlin mortality", "Berlin’s 27/32/45% come from the definition’s own validation cohort (ARDS-04); LUNG SAFE’s overall hospital mortality is about 40%."),
  ],
  traps=[
    ("“Severe ARDS is the commonest grade”", "Moderate is, at 46.6% (ARDS-13d)."),
  ],
  decode=[
    ("[pattern] Commonest Berlin grade in LUNG SAFE", "Moderate."),
    ("[pattern] Key message of LUNG SAFE", "ARDS is common and under-recognised, and lung-protective measures are under-used."),
  ],
  punch="LUNG SAFE: ARDS affects about one in ten ICU admissions, is mostly moderate, is missed in about 40% of cases, and kills about 40% in hospital.",
)

L['ARDS-03'] = dict(
  sub="Respiratory → ARDS → Berlin definition",
  step=4,
  intro="This is the definition that every case vignette is checked against. Each of its four criteria answers one question: is it acute, is it both lungs, is it more than heart failure, and how bad is the oxygenation on a standard amount of PEEP?",
  parts=[
    ('a', "**Within 1 week of a known insult, or of new or worsening respiratory symptoms.** In practice most patients become hypoxic within hours to a day or two of the insult; the one-week window is wide so that almost every case is captured. So a vignette of respiratory failure 3–4 days after pancreatitis or septic shock is well within it."),
    ('b', "**Bilateral opacities on chest X-ray or CT, not fully explained by effusion, collapse or nodules.** Unilateral opacity points to pneumonia, collapse or effusion, not ARDS. A CXR with diffuse bilateral alveolar shadowing in a ventilated patient is the textbook image."),
    ('c', "**Not fully explained by cardiac failure or fluid overload; if no risk factor is present, an objective test (echo) is needed.** The word is ‘fully’: hydrostatic oedema may coexist, so a raised wedge pressure does not exclude ARDS. When there is a clear risk factor (sepsis, pancreatitis, trauma), the clinical judgement is enough; when there is none, echo must show the heart is not the cause."),
    ('d', "**P/F ≤300 on PEEP or CPAP ≥5 cmH₂O.** PEEP recruits collapsed alveoli and raises PaO₂, so a P/F ratio means little unless the PEEP is known; Berlin sets a floor of 5 cmH₂O. The grade within ≤300 is ARDS-04."),
  ],
  table=dict(title="Checking a vignette against Berlin", head=["Criterion", "Satisfied by", "Not satisfied by"], rows=[["Timing", "≤1 week of insult", "chronic symptoms >1 month"], ["Imaging", "**bilateral** opacities", "unilateral infiltrate"], ["Origin", "not **fully** cardiac (echo if no risk factor)", "LV failure explaining it all"], ["Oxygenation", "P/F ≤300 on PEEP ≥5", "PEEP <5"]]),
  mimic=[
    ("ARDS vs pre-eclamptic pulmonary oedema", "Both give bilateral infiltrates in HELLP; a normal LV on echo with P/F 170 and a risk factor makes it ARDS."),
    ("ARDS vs amniotic fluid embolism", "AFE is a sudden cardiorespiratory collapse during labour or just after delivery, with hypotension and DIC — not hypoxaemia developing with a normal LV, as in this vignette."),
  ],
  traps=[
    ("“Berlin needs PAWP ≤18 mmHg” or “PAWP >18 completes the definition”", "Wedge pressure is not in Berlin; >18 would point towards a cardiac cause, and the required criterion is ‘respiratory failure not fully explained by cardiac failure’."),
    ("“Post-partum HELLP with bilateral infiltrates is just pulmonary oedema”", "About a fifth of the cohort missed this, and pulmonary oedema is the obvious pull. Once echo shows no LV failure, the oedema is not fully cardiac and the four criteria are met — it is ARDS."),
    ("“The 1-week window means symptoms usually appear late”", "Most patients are symptomatic within the first day; one week is the outer limit, not the usual time."),
  ],
  decode=[
    ("Bilateral opacities, P/F 180 on PEEP 6 after pancreatitis — which further finding is needed? [DocT GT]", "Respiratory failure not fully explained by cardiac failure or fluid overload."),
    ("Post-partum HELLP, P/F 170, bilateral infiltrates, normal LV on echo — diagnosis? [DocT GT]", "ARDS: all four criteria are met."),
    ("Ventilated patient, diffuse bilateral shadowing on CXR — diagnosis? [DocT QBank]", "ARDS."),
    ("After an injury, when do ARDS symptoms usually begin? [Marrow]", "Within 24 hours (the Berlin limit is 1 week)."),
  ],
  punch="Berlin asks four things — within a week, both lungs, not fully cardiac, and P/F ≤300 on PEEP ≥5; no wedge pressure is needed, and a normal echo is required only when there is no risk factor.",
  extra=[dict(q="After an insult, when do ARDS symptoms usually begin?", a="**Usually within 24 hours** (Marrow key); the Berlin window of 1 week is the limit that captures almost all cases.")],
)

L['ARDS-04'] = dict(
  sub="Respiratory → ARDS → Berlin severity grades",
  step=5,
  intro="Once the four criteria are met, the P/F ratio on PEEP ≥5 sets the grade. The grade is asked directly, inside an ABG you must calculate yourself, and as the gate for non-invasive support.",
  parts=[
    ('a', "**Mild 201–300, moderate 101–200, severe ≤100 (all on PEEP ≥5).** Each band includes its upper limit: 300 is mild, 200 is moderate, 100 is severe. Always calculate P/F from the FiO₂ given — PaO₂ 58 on FiO₂ 0.75 is 77, severe, however unremarkable 58 looks."),
    ('b', "**Mortality 27%, 32% and 45%.** These are the figures from Berlin’s validation cohort; the step from moderate to severe is the largest."),
    ('c', "**Mild only: non-invasive CPAP may satisfy the PEEP criterion; moderate and severe need invasive ventilation in the original Berlin wording.** A non-invasive mask leaks and gives an unreliable FiO₂ and PEEP, so Berlin accepted it only at the mildest end. That is also where a trial of NIV is reasonable; in moderate–severe ARDS, shock or refractory hypoxaemia, NIV often fails and the delayed intubation is associated with higher mortality (in LUNG SAFE, NIV was linked to higher ICU mortality when P/F was below 150). A HACOR score >5 after one hour of NIV predicts failure."),
  ],
  table=dict(title="Grading the questions you were asked", head=["Data", "P/F", "Grade"], rows=[["PaO₂/FiO₂ 180, PEEP 8", "180", "**moderate**"], ["PaO₂ 58, FiO₂ 0.75", "77", "**severe**"], ["P/F exactly 200", "200", "**moderate**"], ["P/F 100–200 asked for ‘severe’", "—", "does **not** satisfy severe"]]),
  mimic=[
    ("Severe hypoxaemia vs the acid–base disorder in the same ABG", "pH 7.295, PaCO₂ 63, HCO₃⁻ 29.8 is a partly compensated respiratory acidosis, but P/F 77 is the dominant and life-threatening finding."),
  ],
  traps=[
    ("“The ABG shows a compensated respiratory acidosis” (only 37% of the cohort got this right)", "There is a respiratory acidosis with partial metabolic compensation — pH is still low, so it is not fully compensated — but the question is about ARDS, and P/F 58/0.75 = 77 is severe hypoxaemia. DocT’s explanation that the gas shows ‘no acid–base disturbance’ is wrong; the key (severe hypoxaemia) is still the best answer."),
    ("“P/F 100–200 is severe”", "100–200 is moderate; severe is ≤100. This is the NEET 2024 recall."),
    ("“NIV suits moderate ARDS with distress” or “refractory severe ARDS”", "NIV is reasonable only in mild ARDS without contraindications. Note that the keyed option calls P/F 200 ‘mild’; by Berlin, 200 is moderate — the option is still the best of the four."),
  ],
  decode=[
    ("Septic shock, bilateral opacities, echo normal, P/F 180 on PEEP 8 — severity? [DocT GT]", "Moderate (101–200)."),
    ("COVID ARDS, ABG shown — interpretation? [DocT QBank, DocT GT]", "Calculate PaO₂/FiO₂ from the FiO₂ on the slip; 77 = severe hypoxaemia."),
    ("Which does NOT satisfy severe ARDS? [NEET 2024, DocT GT]", "P/F 100–200 (that is moderate)."),
    ("When is NIPPV appropriate in ARDS? [DocT QBank]", "Mild ARDS with no contraindications."),
  ],
  punch="Grade on PEEP ≥5: >200 to 300 mild, >100 to 200 moderate, ≤100 severe — calculate P/F from the FiO₂ in the stem, and keep NIV for mild ARDS only.",
)

L['ARDS-05'] = dict(
  sub="Respiratory → ARDS → AECC vs Berlin",
  step=4,
  intro="Berlin was written to fix the AECC definition, so each change answers a known flaw. The examiners’ favourite is the wedge pressure, because old keys still use it.",
  parts=[
    ('a', "**AECC: ‘acute’ undefined, P/F ≤300 = ALI and ≤200 = ARDS, PEEP not considered, PAOP ≤18 mmHg, bilateral infiltrates on X-ray, no risk factor. Berlin: within 1 week, ALI removed (now mild ARDS), three P/F grades, PEEP ≥5 required, wedge removed, X-ray or CT with exclusions, risk factor included.** The wedge was dropped because pulmonary artery catheters are rarely used and because hydrostatic and permeability oedema often coexist — a PAOP above 18 does not exclude ARDS, and one below 18 does not prove it. PEEP was added because the same patient’s P/F changes with it."),
    ('b', "**Remaining criticisms: PEEP level and ventilator settings not standardised, no set timing for the gas; needs PEEP, ABG and imaging (unusable in low-resource settings); P/F varies with PEEP and FiO₂; poor X-ray agreement between readers; weak correlation with diffuse alveolar damage at autopsy.** The resource and blood-gas problems are what the 2023 global definition answers (ARDS-06)."),
  ],
  mimic=[
    ("ARDS vs cardiogenic pulmonary oedema", "Under Berlin, they are separated by the clinical picture and echo, not by a wedge cut-off."),
  ],
  traps=[
    ("“A wedge above 18 mmHg rules out ARDS”", "That is AECC thinking. Under Berlin the wedge is gone and a raised PAOP can coexist with ARDS (ARDS-03 watch). A low wedge (Marrow’s keyed 16 mmHg) still favours non-cardiogenic oedema, so pick it when it is offered — it supports ARDS, it does not define it."),
    ("“ALI is a Berlin category”", "It was renamed mild ARDS (ARDS-13c)."),
  ],
  decode=[
    ("Which finding separates ARDS from cardiogenic pulmonary oedema? [Marrow]", "Keyed PCWP 16 mmHg (below the AECC 18): a low wedge favours non-cardiogenic oedema; Berlin itself uses echo and clinical judgement instead."),
    ("[pattern] Which AECC feature did Berlin remove?", "Wedge pressure ≤18 and the term ALI."),
  ],
  punch="Berlin fixed AECC by defining ‘acute’ as one week, adding PEEP ≥5, grading severity, and dropping both the wedge pressure and ‘ALI’ — so a wedge cut-off answer is AECC thinking.",
)

L['ARDS-06'] = dict(
  sub="Respiratory → ARDS → 2023 global definition",
  step=5,
  intro="Berlin needed a ventilator, a blood gas and an X-ray, so it missed patients on high-flow oxygen and most patients in low-resource settings. The 2023 global definition keeps Berlin’s core and adds ways in.",
  parts=[
    ('a', "**Non-intubated patients are included if on HFNO ≥30 L/min or NIV/CPAP with ≥5 cmH₂O.** High-flow oxygen became the common support for hypoxaemic patients during COVID-19, and Berlin could not count them. Non-intubated patients are not graded by severity."),
    ('b', "**SpO₂/FiO₂ ≤315, valid only when SpO₂ is ≤97%.** Above 97% the oxyhaemoglobin curve is flat, so SpO₂ no longer tracks PaO₂ and the ratio is meaningless."),
    ('c', "**Lung ultrasound is accepted for bilateral opacities** (performed by a trained operator), which brings imaging to the bedside where X-ray or CT is not available."),
    ('d', "**No PEEP, flow or device requirement in resource-limited settings (follows the Kigali modification).** In Kigali, a definition using S/F and ultrasound, without PEEP, identified ARDS where blood gases and ventilators were scarce."),
  ],
  mimic=[
    ("P/F vs S/F cut-offs", "P/F 300, 200, 100 correspond to S/F 315, 235, 148."),
  ],
  traps=[
    ("“The 2023 definition changed the P/F cut-offs”", "They are unchanged at 300, 200, 100."),
    ("“S/F can be used at any saturation”", "Only when SpO₂ ≤97%."),
  ],
  decode=[
    ("[pattern] Patient on HFNO 40 L/min with bilateral opacities — ARDS by which definition?", "The 2023 global definition, not Berlin."),
    ("[pattern] S/F threshold for ARDS", "≤315, with SpO₂ ≤97%."),
  ],
  punch="The 2023 definition keeps Berlin’s cut-offs but admits HFNO ≥30 L/min, S/F ≤315 (SpO₂ ≤97%) and lung ultrasound, and drops PEEP and device requirements where resources are limited.",
)

L['ARDS-07'] = dict(
  sub="Respiratory → ARDS → Risk factors",
  step=1,
  intro="The story starts with the insult. The lung can be injured from the airway side, damaging the alveolar epithelium first, or from the blood side, where circulating inflammatory mediators damage the capillary endothelium first. That side of entry is the whole basis of the direct/indirect split.",
  parts=[
    ('a', "**Direct: pneumonia, aspiration of gastric contents, lung contusion, inhalational injury, near-drowning, pulmonary vasculitis, transfusion (TRALI). Indirect: non-pulmonary sepsis, major trauma, pancreatitis, severe burns, non-cardiogenic shock, drug overdose.** Ask whether the injury reached the lung through the airway or the lung itself (direct) or through the blood (indirect). Pancreatitis injures the lung through circulating enzymes and cytokines, so it is indirect; aspiration, pneumonia and smoke reach the alveoli through the airway, so they are direct. Most sources place transfusion (TRALI) with the indirect causes, because antibodies in donor plasma reach the lung through the blood."),
    ('b', "**Pneumonia and sepsis are the commonest causes (then aspiration).** In LUNG SAFE, pneumonia accounted for well over half of cases. The more severe the illness, the higher the risk: trauma patients with APACHE II ≥16 have about 2.5 times the risk, and the commonest causes in trauma are lung contusion, multiple fractures and chest-wall trauma (Harrison’s)."),
  ],
  mimic=[
    ("Pulmonary contusion vs major trauma", "Contusion is a direct cause (the lung is struck); trauma without lung injury is indirect, through shock and transfusion."),
    ("Severe burns vs inhalational injury", "The burn itself is indirect; smoke reaching the airway is direct."),
  ],
  traps=[
    ("“Inhalational injury is an indirect cause”", "Smoke reaches the alveoli through the airway, so it is direct; the burn of the skin is indirect."),
    ("“The first danger in a burn with bronchial blisters is ARDS”", "The immediate complication is laryngeal oedema; pneumonia and ARDS come at about 4–5 days, and subglottic stenosis, bronchiectasis and bronchiolitis obliterans later."),
  ],
  decode=[
    ("Which is an indirect cause of ARDS? [DocT GT]", "Acute pancreatitis (aspiration, pneumonia and inhalation are direct)."),
    ("Burn with bronchial blisters — immediate complication of inhalation injury? [Marrow]", "Laryngeal oedema."),
    ("APACHE II score that raises ARDS risk 2.5-fold in trauma? [Marrow]", "≥16."),
  ],
  punch="Direct causes reach the alveolus through the airway, indirect ones through the blood; pneumonia and sepsis lead the list, and pancreatitis is the classic indirect cause.",
  extra=[dict(q="Inhalation injury: timeline of complications?", a="**Immediate: laryngeal oedema**; at about 4–5 days: pneumonia and ARDS; late: subglottic stenosis, bronchiectasis, bronchiolitis obliterans (Marrow).")],
)

L['ARDS-08'] = dict(
  sub="Respiratory → ARDS → Pathological stages",
  step=2,
  intro="After the insult, the lung goes through a sequence of injury, attempted repair and, in some patients, scarring. The stage explains what you see at the bedside: flooding early, stiff lungs with dead space and pulmonary hypertension late.",
  parts=[
    ('a', "**Exudative (first 7 days), proliferative (from about 7–10 days), fibrotic (after 10–14 days).** These are your notes’ timings; other texts give proliferative as days 7–21 and fibrotic after 3 weeks. The stages overlap, and many patients recover after the proliferative stage without fibrosis."),
    ('b', "**Exudative: type I cell and endothelial injury, protein-rich oedema, neutrophils, hyaline membranes. Proliferative: type II pneumocyte hyperplasia, fibroblasts, oedema organises. Fibrotic: collagen, obliterated architecture, pulmonary hypertension.** Type I cells cover the alveolus and die easily; type II cells are the progenitors that multiply to re-line it, so their hyperplasia is a sign of repair. When repair fails, fibrosis (fibrosing alveolitis) replaces alveoli and capillaries: compliance falls further, dead space rises, the pulmonary vascular bed is lost and pulmonary hypertension follows, with a risk of pneumothorax."),
  ],
  mimic=[
    ("Fibrotic ARDS vs organising pneumonia", "Organising pneumonia is a separate entity with plugs of granulation tissue, patchy consolidation and a brisk steroid response; two weeks of ventilation with falling compliance, dead space, pulmonary hypertension and linear opacities is ARDS going fibrotic."),
    ("Fibrotic ARDS vs pulmonary embolism", "PE raises dead space and pulmonary pressures, but does not lower compliance or give linear opacities."),
  ],
  traps=[
    ("“Organising pneumonia” or “bronchiolitis obliterans” for the two-week ventilator-dependent patient", "31% missed this. The combination of low compliance, high dead space, new pulmonary hypertension and linear opacities after two weeks is the fibrotic stage — fibrosing alveolitis."),
    ("“Type II pneumocytes proliferate in the fibrotic stage”", "They proliferate in the proliferative stage (ARDS-13f)."),
  ],
  decode=[
    ("ARDS, ventilator-dependent at 2 weeks, low compliance, high dead space, new pulmonary hypertension, linear opacities — pathology? [DocT GT]", "Fibrosing alveolitis (fibrotic stage)."),
    ("COVID on MV, died at 1 week — post-mortem lung? [Marrow]", "Thick fibrin layer lining alveoli: hyaline membranes (exudative stage)."),
  ],
  punch="Exudative oedema with hyaline membranes in week one, type II cell repair after it, and in some a fibrotic stage that brings low compliance, dead space and pulmonary hypertension.",
)

L['ARDS-09'] = dict(
  sub="Respiratory → ARDS → Pathophysiology",
  step=3,
  intro="Each bedside feature of ARDS follows from one event: the alveolar–capillary barrier leaks. Fluid and protein flood the alveoli, the flooded units stay perfused, and the lung left over is small. The questions test whether you can name the mechanism behind each sign.",
  parts=[
    ('a', "**Increased permeability of the alveolar–capillary barrier, not raised hydrostatic pressure.** Injured endothelium and epithelium let protein through, so the oedema fluid is rich in protein, close to plasma. In cardiogenic oedema the barrier is intact and a high capillary pressure (PCWP 24 in the vignette) pushes out a protein-poor transudate — the mechanism keyed in the heart-failure question."),
    ('b', "**Shunt: flooded and collapsed alveoli are perfused but not ventilated.** Blood through those units never meets the inspired gas, however much oxygen is given; and blood leaving the healthy units is already nearly saturated, so it cannot carry extra to make up. With a large shunt, PaO₂ barely rises on 100% oxygen. In V/Q mismatch, low-ventilation units still receive some gas, so extra oxygen does correct them. PEEP, by re-opening alveoli, is what reduces shunt."),
    ('c', "**Loss of aerated lung and surfactant dysfunction.** Fewer open alveoli means each breath goes into a smaller lung (ARDS-10), and damaged surfactant raises surface tension so alveoli collapse."),
    ('d', "**Microvascular thrombosis and over-distension of the remaining aerated units; a high dead-space fraction predicts mortality.** Clots in capillaries leave ventilated alveoli unperfused, and over-stretched alveoli compress their own capillaries. Both waste ventilation, PaCO₂ rises, and the dead-space fraction is an independent predictor of death."),
  ],
  table=dict(title="Which mechanism the stem points to", head=["Stem", "Mechanism"], rows=[["Hypoxaemia unresponsive to 100% O₂", "**shunt**"], ["Hypoxaemia that corrects with O₂", "V/Q mismatch"], ["High PaCO₂, low minute ventilation", "hypoventilation"], ["PCWP 24, Kerley B, cardiomegaly", "raised hydrostatic pressure"]]),
  mimic=[
    ("Permeability vs hydrostatic oedema", "ARDS: protein-rich exudate, normal heart. Heart failure: protein-poor transudate, raised wedge, Kerley B lines, cardiomegaly."),
  ],
  traps=[
    ("“Hypoxaemia unresponsive to 100% oxygen in pneumonia is V/Q mismatch” (only half the cohort chose shunt)", "Failure to respond to oxygen is the signature of shunt. V/Q mismatch improves with oxygen."),
    ("“ARDS hypoxaemia is mainly V/Q mismatch”", "It is mainly shunt. One DocT question keys V/Q mismatch only because shunt is not offered — shunt is the extreme end of V/Q mismatch (V/Q of zero), so that key is defensible; choose shunt whenever it is an option."),
  ],
  decode=[
    ("Severe pneumonia, hypoxaemia unresponsive to 100% oxygen — mechanism? [DocT GT]", "Shunt physiology."),
    ("Ventilated multilobar pneumonia, persistent hypoxaemia — mechanism? [Marrow]", "Shunt: perfused, unventilated alveoli."),
    ("ARDS, PaO₂ 52 on FiO₂ 0.6, options without shunt [DocT GT]", "V/Q mismatch as the nearest answer."),
    ("Heart failure, PCWP 24 — why pulmonary oedema? [DocT GT]", "Raised hydrostatic pressure, not increased permeability."),
  ],
  punch="A leaky barrier gives protein-rich oedema; perfused but flooded alveoli give shunt that oxygen cannot fix; fewer open alveoli lower compliance; and clotted, over-stretched units raise dead space, which predicts death.",
)

L['ARDS-10'] = dict(
  sub="Respiratory → ARDS → The baby lung",
  step=3,
  intro="The loss of aerated lung from ARDS-09 has a consequence for every breath you set. CT showed that the ARDS lung is not uniformly stiff: it is a small lung that still works, sitting on top of flooded, collapsed lung.",
  parts=[
    ('a', "**Gattinoni (CT studies).** CT of ARDS lungs showed dense collapse in the dependent regions and near-normal aeration in a small non-dependent region."),
    ('b', "**The ARDS lung is small, not stiff: only a small non-dependent portion stays aerated, the size of a child’s lung.** The ventilated lung of an adult with severe ARDS may be as small as a young child’s."),
    ('c', "**Compliance reflects the volume of aerated lung; the aerated part has near-normal compliance.** A low respiratory compliance means fewer open alveoli, not stiffer ones."),
    ('d', "**A normal tidal volume over-distends the baby lung, hence low tidal volume and driving-pressure limits.** 500 mL into a lung the size of a child’s stretches it injuriously; tidal volume is set at 6 mL/kg predicted body weight, and driving pressure (tidal volume divided by compliance) measures how large the breath is relative to the lung that is open."),
  ],
  mimic=[
    ("Baby lung vs sponge lung", "The baby lung is functional, not anatomical: the oedematous lung is heavy, and its own weight collapses the dependent parts, so the aerated region moves when the patient is turned — the reason proning helps."),
  ],
  traps=[
    ("“The ARDS lung is uniformly stiff”", "It is small, not stiff (ARDS-13g)."),
  ],
  decode=[
    ("[pattern] Who described the baby lung, and what does compliance reflect?", "Gattinoni; the volume of aerated lung."),
    ("[pattern] Why low tidal volume in ARDS?", "A normal tidal volume over-distends the small aerated lung."),
  ],
  punch="The ARDS lung is small, not stiff: compliance measures how much lung is open, so tidal volume must be scaled to that small lung.",
)

L['ARDS-11'] = dict(
  sub="Respiratory → ARDS → Mimics and work-up",
  step=6,
  intro="Berlin is a syndrome definition, so anything that fills both lungs with fluid, blood, cells or protein in under a week can meet it. The mimics matter because their treatment is different — steroids, plasma exchange, lavage — and the bronchoalveolar lavage is usually what tells them apart.",
  parts=[
    ('a', "**Cardiogenic pulmonary oedema; diffuse alveolar haemorrhage; acute eosinophilic pneumonia; acute interstitial pneumonia (Hamman–Rich); cryptogenic organising pneumonia; acute hypersensitivity pneumonitis; drug-induced lung disease; lymphangitic carcinomatosis.** Each gives acute bilateral opacities and hypoxaemia, so each can pass all four Berlin criteria, especially when there is no clear risk factor."),
    ('b', "**Echo and BNP (cardiac cause); CT chest; bronchoalveolar lavage (eosinophils, haemosiderin-laden macrophages, organisms, malignant cells); lung biopsy rarely.** In diffuse alveolar haemorrhage, the lavage becomes more bloody with each aliquot and shows >20% haemosiderin-laden macrophages; the next step is the systemic cause — ANCA vasculitis, anti-GBM disease, SLE or antiphospholipid syndrome. In acute eosinophilic pneumonia, BAL eosinophils are >25%, typically in a young man who has recently started smoking, with negative cultures; IV methylprednisolone works within 12–48 h. In pulmonary alveolar proteinosis, the lavage is milky with PAS-positive lipoproteinaceous material and CT shows crazy paving; it is treated by whole-lung lavage (± inhaled GM-CSF)."),
    ('c', "**Trauma-related ARDS: better survival. Pulmonary vs extrapulmonary: similar. Hyperinflammatory phenotype: worse than hypoinflammatory. COVID-19 ARDS: similar mortality, longer ventilation and stay.** The hyperinflammatory phenotype has higher inflammatory markers (IL-6, IL-8), more shock and lower bicarbonate. Trauma patients are usually younger and have a reversible insult."),
  ],
  table=dict(title="What the lavage shows", head=["BAL finding", "Diagnosis", "Treatment"], rows=[["Increasingly bloody, >20% haemosiderin-laden macrophages", "**diffuse alveolar haemorrhage**", "find the cause; pulse methylprednisolone ± cyclophosphamide/rituximab; plasma exchange for anti-GBM disease and selected vasculitis"], ["Eosinophils >25%", "**acute eosinophilic pneumonia**", "IV methylprednisolone"], ["Milky, PAS-positive material", "**alveolar proteinosis**", "whole-lung lavage"]]),
  mimic=[
    ("Diffuse alveolar haemorrhage vs alveolar proteinosis", "Haemosiderin-laden macrophages vs PAS-positive material."),
    ("Polyarteritis nodosa vs ANCA vasculitis", "PAN is a medium-vessel vasculitis that spares the lung; the small-vessel ANCA vasculitides cause capillaritis and DAH."),
  ],
  traps=[
    ("“PAN on prednisone explains the alveolar haemorrhage” or “aspirin explains it” (59% wrong)", "PAN spares the lung, and low-dose aspirin alone does not cause DAH. Three first-trimester miscarriages point to antiphospholipid syndrome, a recognised cause of DAH."),
    ("“PAS-positive lavage is diffuse alveolar haemorrhage”", "PAS-positive material is alveolar proteinosis; DAH shows haemosiderin-laden macrophages."),
    ("“A new smoker with BAL eosinophils 35% needs antibiotics or ECMO first”", "This is acute eosinophilic pneumonia: IV methylprednisolone."),
  ],
  decode=[
    ("Intubated, bilateral GGO, haemorrhagic secretions, BAL >50% haemosiderin-laden macrophages — which history supports it? [DocT GT]", "Three first-trimester miscarriages (antiphospholipid syndrome)."),
    ("Bilateral infiltrates, BAL PAS-positive material — which ARDS mimic? [DocT GT]", "Pulmonary alveolar proteinosis."),
    ("Young recent smoker, ARDS picture, BAL eosinophils 35% — next step? [Marrow]", "IV methylprednisolone."),
  ],
  punch="When Berlin criteria are met without a clear risk factor, look for a mimic — and the lavage usually names it: blood for DAH, eosinophils for eosinophilic pneumonia, PAS-positive material for proteinosis.",
)

L['ARDS-12'] = dict(
  sub="Respiratory → ARDS → COVID-19 ARDS",
  step=3,
  intro="COVID-19 tested the ideas of ARDS-09 and ARDS-10. In the early phase some patients were deeply hypoxaemic with fairly normal compliance, which pointed to a vascular problem rather than flooding alone.",
  parts=[
    ('a', "**Often relatively preserved compliance despite severe hypoxaemia in the early phase.** Much of the hypoxaemia came from perfusion going to poorly ventilated lung rather than from loss of aerated volume. Gattinoni proposed two types: L (low elastance, so near-normal compliance; low lung weight; little to recruit) and H (high elastance, heavy lung, large shunt, recruitable). Larger cohorts (Grasselli, Lombardy; Ferrando, Spain; both 2020) then found compliance in ventilated COVID ARDS spread over the same wide range as classical ARDS, with no separate groups, and no trial has tested ventilation guided by L or H."),
    ('b', "**Prominent endothelial injury and microthrombosis; hypoxaemia from loss of hypoxic vasoconstriction.** Normally, vessels to poorly ventilated alveoli constrict and send blood elsewhere; when that reflex is lost, blood keeps flowing through poorly ventilated lung."),
    ('c', "**RECOVERY: dexamethasone 6 mg for 10 days lowered 28-day mortality in patients on oxygen or ventilation.** The dose was 6 mg once daily for up to 10 days (or until discharge). The largest benefit was in ventilated patients; there was no benefit in patients not on oxygen."),
  ],
  mimic=[
    ("COVID vs classical ARDS", "Mortality is similar; ventilation and stay are longer in COVID (ARDS-11c)."),
  ],
  traps=[
    ("“COVID ARDS needs a different ventilation strategy”", "Ventilation is the same: low tidal volume and proning, as for any ARDS."),
    ("“Type L COVID ARDS should be ventilated with larger tidal volumes”", "This was proposed from the L/H model, but compliance did not split into two groups in large cohorts and no trial supports it; standard lung-protective ventilation applies."),
  ],
  decode=[
    ("[pattern] Steroid with mortality benefit in COVID-19 on oxygen or ventilation", "Dexamethasone 6 mg for 10 days (RECOVERY)."),
    ("[pattern] COVID pneumonia, severe hypoxaemia, near-normal compliance, little recruitability — which type?", "Type L in Gattinoni’s model; type H is low compliance, heavy lung and recruitable. Large cohorts did not confirm two separate groups."),
  ],
  punch="Early COVID ARDS may keep near-normal compliance because its hypoxaemia is partly vascular, but it is ventilated like any ARDS, and dexamethasone helps those on oxygen or ventilation.",
)

L['ARDS-13'] = dict(
  sub="Respiratory → ARDS → Revision: true or false",
  step=6,
  intro="A sweep through the deck. Each statement turns on one detail from an earlier card.",
  parts=[
    ('a', "**False — PAOP ≤18 was AECC.** Berlin removed the wedge pressure (ARDS-05)."),
    ('b', "**True — P/F 200 on PEEP 5 is moderate (101–200).** Each band includes its upper limit (ARDS-04)."),
    ('c', "**False — ALI was removed; it is now mild ARDS** (ARDS-05)."),
    ('d', "**False — moderate is the commonest grade in LUNG SAFE, 46.6%** (ARDS-02)."),
    ('e', "**True — hyaline membranes belong to the exudative stage, the hallmark of diffuse alveolar damage** (ARDS-08)."),
    ('f', "**False — type II pneumocytes proliferate in the proliferative stage** (ARDS-08)."),
    ('g', "**False — the ARDS lung is small, not stiff (baby lung)** (ARDS-10)."),
  ],
  mimic=[],
  traps=[
    ("“P/F 200 is mild”", "Exactly 200 is moderate; exactly 300 is mild; exactly 100 is severe."),
  ],
  decode=[
    ("[pattern] Statements about Berlin vs AECC", "Wedge pressure and ALI belong to AECC only."),
    ("[pattern] Statements about pathology stages", "Hyaline membranes early, type II hyperplasia next, collagen last."),
  ],
  punch="Most errors on ARDS statements come from AECC leftovers (wedge, ALI), band edges (200 is moderate) and stage order (membranes, then type II cells, then fibrosis).",
)

FLAGS = {}
FLAGS['ARDS-04'] = "WATCH ‘PEEP below 5 and not on HFNO: cannot be graded by Berlin’ mixes two definitions: Berlin does not accept HFNO at all; HFNO ≥30 L/min counts only under the 2023 global definition, which does not grade non-intubated patients. Separately, the DocT NIV question’s keyed option calls P/F 200 ‘mild’ (it is moderate), and DocT’s ABG explanation (‘no acid–base disturbance’) is wrong: pH 7.295/PaCO₂ 63/HCO₃⁻ 29.8 is a partly compensated respiratory acidosis; the key (severe hypoxaemia, P/F 77) stands."
FLAGS['ARDS-05'] = "Marrow key ‘PCWP 16 mmHg separates ARDS from cardiogenic oedema’ rests on the AECC wedge rule (≤18). A low wedge still favours non-cardiogenic oedema, so the key is acceptable as the best option, but it is not a Berlin criterion and a raised PAOP can coexist with ARDS. The card is right."
FLAGS['ARDS-07'] = "Card places transfusion (TRALI) in the DIRECT column; most sources (e.g. Ware & Matthay) class transfusion as an indirect (extrapulmonary) cause, as the injury reaches the lung through the blood. The explanation says so."
FLAGS['ARDS-09'] = "DocT AIM2 keys ‘V/Q mismatch’ for ARDS hypoxaemia on FiO₂ 0.6; the card (rightly) says shunt. The key is defensible only because shunt is not offered."
