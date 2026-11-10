# RESP06A — Explain v3 ("Learn" depth): pulmonary embolism, part 1 — VTE deaths and risk factors, natural history, pathophysiology, high-risk PE, presentation, ECG, Wells and revised Geneva, D-dimer, CTPA and V/Q, echo and compression ultrasound, the diagnostic pathway. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP06A.md (33 questions; PE-12 echo and CUS asked 6 times, PE-13 pathway 5, PE-11 CTPA 4, PE-03/06/07/08 3 each). Fields as TOX01, plus SPINE, PRIMER and step.
# The story ends where risk stratification begins; treatment and risk classes are RESP06B (PE-14 to PE-26).
# Checked online on 11 Nov 2026: ESC/ERS 2019 PE guideline text (VTE deaths 34%/59%/7%; 30–50% obstruction, TXA2 and serotonin, mPAP 40; haemodynamic instability; normal SaO2 in ≤40%, normal A–a gradient ~20%; sinus tachycardia ~40%;
# revised Geneva items and cut-offs; age × 10 µg/L; YEARS thresholds; PIOPED II 83%/96% and NPV/PPV by probability; V/Q rules; echo NPV 40–50%, RV dilatation ≥25%, 60/60 and McConnell definitions, TAPSE <16 mm;
# CUS shows DVT in 30–50%, incomplete compressibility; bedside TTE first in instability; anticoagulate without delay in high or intermediate probability; CTEPH 0.1–9.1% in 2 years; recurrence 2.5%/yr vs 4.5%/yr; ‘provoked/unprovoked’ no longer supported; no CT venography),
# ADJUST-PE (0.3% failure; ≥75 years 6.4% → 29.7% excluded), PEGeD (2,017 patients, imaging 51.9% → 34.3%), PERC items and PROPER, Ende-Verhaar 2017 CTEPH meta-analysis, McConnell 1996 / Kurzyna 2002 / Casazza 2005,
# 2025 ECG meta-analysis (24 studies, 7,467 patients), ACCP surgical risk tiers, PE share of hospital deaths (JRSM 2011).
# Second review 11 Nov 2026 (resp06a_review.md): VITAE abstract (Cohen 2007), Heit 2000 (12.9%/22.8%/30.4%; 8.3% at 90 d, 10.1% at 180 d), Sweetland 2009 (peak in week 3), Cook 2005 (four factors), Kurzyna 2002 and McConnell 1996 counts, Casazza 2005,
# ESC 2019 text (10/30/65%, 40% sinus tachycardia, V/Q diagnostic in 30–50%), JRSM 2011 autopsy figures, ACCP 2008 tiers. Not found online: source of the card's symptom and ECG percentages (softened in the text).

SPINE = [
  ("Who clots, and who dies", "Venous thromboembolism comes from surgery, immobility, cancer and the ICU’s own exposures on top of any inherited tendency, and most VTE deaths are sudden or never diagnosed in life."),
  ("What follows the first clot", "After a first event recurrence stays lifelong and takes the same form, and a few survivors are left with chronic thromboembolic pulmonary hypertension."),
  ("From obstruction to RV failure", "Acute PE kills by right-ventricular pressure overload once a third to a half of the bed is blocked, so high-risk PE is defined by the circulation — arrest, obstructive shock or persistent hypotension — not by the size of the clot."),
  ("The bedside picture", "Symptoms, gases, the chest X-ray and the ECG are non-specific: sinus tachycardia is the commonest ECG finding, S1Q3T3 is present in only about one in five, and a normal saturation does not exclude PE."),
  ("Probability first, then D-dimer", "Wells or revised Geneva sets the pre-test probability, and only in low or intermediate probability can a normal D-dimer, age-adjusted over 50, rule PE out."),
  ("Imaging and the pathway", "Stable patients go to CTPA (or V/Q) according to probability, unstable ones to bedside echo, a proximal DVT on ultrasound is enough to treat, and anticoagulation starts while tests proceed; what is found then feeds risk stratification."),
]

PRIMER = "Deep vein thrombosis and pulmonary embolism are one disease, venous thromboembolism (VTE): most emboli come from proximal leg veins, and finding a clot in either place commits the patient to the same anticoagulation. The right ventricle is a thin-walled chamber built for a low-pressure circuit, so it tolerates volume well but fails quickly when afterload rises suddenly, and its own coronary flow depends on aortic pressure exceeding RV pressure. A test’s negative and positive predictive values change with the pre-test probability: the same negative result is reassuring when PE is unlikely and misleading when it is likely, which is why every pathway starts with a clinical probability score. D-dimer is reported in µg/L (fibrinogen-equivalent units), which equals ng/mL; the usual cut-off is 500."

L = {}

L['PE-01'] = dict(
  sub="Respiratory → Pulmonary embolism → Deaths from VTE",
  step=1,
  intro="Step 1 starts with why PE is chased so hard: most patients who die of it are never diagnosed in life. The figures come from VITAE, a 2004 modelling study of six European Union countries (Cohen 2007), which estimated about 370,000 VTE-related deaths a year and is quoted in the ESC 2019 guideline.",
  parts=[
    ('a', "**34% die suddenly (sudden fatal PE).** These patients die within hours of the event, before any treatment can act, so prevention — thromboprophylaxis — is the only effective measure for them."),
    ('b', "**59% are undiagnosed during life.** Death follows a PE that nobody suspected, often in a patient admitted for something else, because the symptoms are non-specific (PE-06)."),
    ('c', "**Only 7% are correctly diagnosed before death.** The remaining minority were recognised and treated yet still died."),
    ('d', "**Provoked: a known risk factor in the weeks to 3 months before; unprovoked: no trigger, with a higher recurrence rate.** The distinction decides how long to anticoagulate (RESP06B): a major transient factor such as surgery carries the lowest recurrence once treated, an event with no identifiable factor a higher one. ESC 2019 no longer uses the words provoked and unprovoked; it speaks of transient or reversible, persistent, or no identifiable risk factors, with the same consequences."),
  ],
  mimic=[],
  traps=[
    ("“PE causes 10% of hospital deaths”", "That widely quoted figure comes from autopsy series of the 1970s and 1980s; a UK hospital review of 2007–08 (JRSM 2011) attributed 2.0% of autopsied adult inpatient deaths (14 of 696), and about 1% of all inpatient deaths, to PE."),
  ],
  decode=[
    ("[pattern] Of VTE-related deaths, what share were diagnosed before death?", "About 7%; 59% were undiagnosed and 34% were sudden."),
    ("[pattern] PE with no identifiable risk factor — consequence for treatment?", "Higher recurrence, so extended anticoagulation is considered."),
  ],
  punch="Most VTE deaths are sudden (34%) or never diagnosed (59%); only 7% are recognised in life, which is why prevention and a low threshold to test matter.",
)

L['PE-02'] = dict(
  sub="Respiratory → Pulmonary embolism → Risk factors for VTE",
  step=1,
  intro="Step 1 continues with who clots. Each risk factor acts on stasis, the vessel wall or the clotting system, and the ICU adds its own exposures on top of the general and inherited ones. The two real questions test exactly this split: an ICU exposure against inherited options, and inherited against acquired thrombophilia.",
  parts=[
    ('a', "**ICU-acquired: sepsis, central venous catheter, pharmacological paralysis, mechanical ventilation, vasopressors, heart or renal failure and dialysis, blood products (platelets, recombinant factor VIIa).** Paralysis and sedation remove the calf-muscle pump; a catheter injures the vein and is a surface for clot; sepsis activates coagulation; vasopressors are thought to impair the absorption of subcutaneous heparin and mark severity. In a large medical–surgical ICU cohort (Cook 2005) the independent risk factors were a personal or family history of VTE, end-stage renal failure, platelet transfusion and vasopressor use."),
    ('b', "**Inherited: factor V Leiden, prothrombin 20210A, deficiency of protein C, protein S or antithrombin, dysfibrinogenaemia.** Factor V Leiden makes factor Va resistant to activated protein C and is the commonest inherited cause in white populations; the prothrombin mutation raises prothrombin levels; antithrombin deficiency is the strongest and can cause heparin resistance."),
    ('c', "**Acquired thrombophilia: antiphospholipid syndrome, heparin-induced thrombocytopenia, myeloproliferative disease.** These arise during life, not in the genes. Paroxysmal nocturnal haemoglobinuria (PNH) belongs here too: it is caused by a somatic (acquired) PIGA mutation in a marrow stem cell, so it is acquired even though it is a mutation, and it causes thrombosis at unusual sites such as the hepatic veins."),
  ],
  mimic=[
    ("Inherited vs acquired thrombophilia", "Inherited: factor V Leiden, prothrombin 20210A, protein C, S and antithrombin deficiency. Acquired: antiphospholipid syndrome, HIT, myeloproliferative neoplasms (polycythaemia vera) and PNH."),
  ],
  traps=[
    ("“ICU patient with a CVC, vasopressors and renal failure: his PE is due to a prothrombin mutation, protein C deficiency or family history”", "The question asks which of his ICU exposures contributed: vasopressor therapy. Only 26% chose it. A family history is a real risk factor too (Cook 2005), but nothing in the stem gives one."),
    ("“PNH is an inherited hypercoagulable state” [NEET 2024 recall]", "PNH is acquired (somatic mutation), as are polycythaemia vera and APS; all three options were acquired, and the recall keyed PNH, presumably because it is the one caused by a mutation. Pick PNH if forced, knowing it is acquired."),
  ],
  decode=[
    ("ICU patient, central venous catheter, vasopressors, acute renal failure, sudden hypoxia — which most likely contributed to his PE? [DocT GT, 26% right]", "Vasopressor therapy: the listed ICU-acquired factor, not an inherited one."),
    ("Inherited hypercoagulable state: PNH, PV or APS? [NEET 2024 recall]", "Keyed PNH, although all three are acquired."),
  ],
  punch="ICU patients clot from catheters, paralysis, ventilation, vasopressors, renal failure and transfusion on top of the general risks; factor V Leiden and protein C, S and antithrombin deficiency are inherited, while APS, HIT, myeloproliferative disease and PNH are acquired.",
)

L['PE-03'] = dict(
  sub="Respiratory → Pulmonary embolism → Natural history, recurrence and CTEPH",
  step=2,
  intro="Step 2 follows the patient who survives the first clot. Three things can happen next: the risk window after surgery closes slowly, the clot can recur for life, and in a few the clot does not resolve and leaves pulmonary hypertension. The questions go to that last outcome — what causes chronic thromboembolic pulmonary hypertension (CTEPH), where it is classified, and how it is treated.",
  parts=[
    ('a', "**DVT risk is highest in the first 2 weeks after surgery and stays raised for 2–3 months.** Clot forms during and soon after the operation, while tissue injury, venous stasis and immobility coincide. In the Million Women Study (Sweetland 2009), measured as admission with clinical VTE, the risk was highest in the first 6 weeks, peaked in the third week and was still clearly raised at 7–12 weeks. That is why prophylaxis is not stopped at discharge after high-risk operations such as hip or knee arthroplasty or cancer surgery (extended prophylaxis), and why surgery in the previous 3 months counts as a transient risk factor."),
    ('b', "**CTEPH: 1.5%, within 24 months (ESC 2019 range 0.1–9.1%).** ESC 2019 gives a cumulative incidence of 0.1–9.1% in the first 2 years. Pooled estimates differ by who is counted: 0.56% of all patients with acute PE, but 3.2% of survivors followed after 6 months of treatment and 2.8% of survivors without major comorbidity (Ende-Verhaar 2017); about 2–4% of survivors is the usual figure. CTEPH is an organised, fibrotic clot that the body failed to lyse, plus remodelling of the small vessels it left open. It is suspected when breathlessness persists or returns beyond 3 months of anticoagulation; a V/Q scan is the screening test (a normal perfusion scan excludes it), and right-heart catheterisation (by the 2022 ESC/ERS definition, mean PA pressure above 20 mmHg with PAWP 15 mmHg or below and PVR above 2 Wood units, after at least 3 months of effective anticoagulation) and pulmonary angiography confirm it."),
    ('c', "**Recurrence: early (within 6 months, usually on anticoagulation) 8%; late 13% at 1 year, 23% at 5 years, 30% at 10 years.** The 13%, 23% and 30% match the Olmsted County population cohort (Heit 2000: 12.9% at 1 year, 22.8% at 5 years, 30.4% at 10 years), which counted possible as well as probable or definite recurrences; in the same cohort cumulative recurrence was 8.3% at 90 days and 10.1% at 180 days. ESC 2019 frames late risk per year after stopping anticoagulation: about 2.5% a year after PE with a transient risk factor and about 4.5% a year when no risk factor, cancer or thrombophilia is found. Recurrence is lifelong, so the question at 3 months is always whether to continue."),
    ('d', "**The same form as the first: PE follows PE, DVT follows DVT; commoner after unprovoked events.** A patient whose first event was PE is likely to have a PE again, which is why a first PE with no identifiable risk factor weighs towards indefinite anticoagulation."),
  ],
  mimic=[
    ("CTEPH vs acute PE on echo", "Both enlarge the right heart. CTEPH has a hypertrophied RV that can generate a mean PA pressure well above 40 mmHg and an organised clot; an acute PE in a previously normal RV cannot exceed about 40 mmHg (PE-04)."),
    ("CTEPH (group 4) vs PAH (group 1)", "Both are precapillary. CTEPH shows mismatched perfusion defects on V/Q and organised clot; idiopathic PAH has a normal or patchy, non-segmental perfusion scan."),
  ],
  traps=[
    ("“A massive saddle embolus is the commonest embolic cause of secondary pulmonary hypertension”", "A massive embolus kills or lyses. The keyed answer is multiple small recurrent emboli (51% right). In current understanding most CTEPH follows incomplete resolution of a recognised acute PE with small-vessel remodelling, and about a quarter of patients have no known PE; the option ‘multiple small recurrent emboli’ captures this best. Air and fat emboli are acute and leave no chronic PH."),
    ("“Prior clot, now a large PA thrombus with severe PH: WHO group 1 or 3”", "Chronic thromboembolic disease is WHO group 4 (56% right)."),
    ("“Persistent clot and PH after 9 months of anticoagulation: continue anticoagulation or thrombolyse”", "Organised clot does not lyse. Operable CTEPH needs pulmonary endarterectomy, with lifelong anticoagulation; inoperable or distal disease gets balloon pulmonary angioplasty or riociguat, and transplant is the last resort."),
  ],
  decode=[
    ("Which form of PE is the commonest cause of secondary pulmonary hypertension? [DocT, 51% right]", "Multiple small recurrent pulmonary emboli."),
    ("PE ‘a long time ago’, a few months of blood thinners, now enlarged right heart, severe TR, large PA thrombus, severe PH — WHO group? [DocT GT, 56% right]", "Group 4 (CTEPH)."),
    ("Persistent clot and PH at 9 months on anticoagulation — next step? [Marrow]", "Pulmonary thromboendarterectomy."),
  ],
  extra=[
    dict(q="How is CTEPH treated?", a="Lifelong anticoagulation in all. Pulmonary endarterectomy at an expert centre is the treatment of choice for operable (proximal) disease and can cure it; inoperable or residual disease is treated with balloon pulmonary angioplasty and riociguat; lung transplant if these fail."),
  ],
  punch="After a first VTE recurrence is lifelong and takes the same form, and about 2–4% of PE survivors develop CTEPH (WHO group 4) — screened by V/Q, confirmed by catheter, treated by endarterectomy.",
)

L['PE-04'] = dict(
  sub="Respiratory → Pulmonary embolism → How acute PE kills",
  step=3,
  intro="Step 3 explains why a clot in the lung stops the heart. The lung tolerates a small clot well; the problem is the right ventricle, which meets a sudden rise in afterload it was never built for. The one real question tests the limit of what an unconditioned RV can generate.",
  parts=[
    ('a', "**Death is from RV pressure overload and failure.** The lung itself rarely infarcts badly because it has a dual blood supply; the circulation fails at the right ventricle."),
    ('b', "**30–50% of the cross-sectional area must be occluded before pulmonary artery pressure rises.** The pulmonary bed has a large reserve: unused vessels are recruited and distended, so small emboli raise resistance little. Past a third to a half, resistance climbs steeply."),
    ('c', "**Vasoconstriction from thromboxane A2 and serotonin adds to the mechanical obstruction.** Platelets in the clot release these mediators, so pulmonary vascular resistance rises more than the clot alone would explain; pre-existing heart or lung disease lowers the threshold further."),
    ('d', "**The RV spiral: RV dilates → tricuspid regurgitation, wall tension and oxygen demand rise; the septum shifts, LV preload and output fall → hypotension → RV coronary perfusion falls → RV ischaemia.** The two ventricles share the septum and the pericardium, so a dilated RV squeezes the LV (ventricular interdependence). Falling aortic pressure while RV pressure is high removes the gradient that perfuses the RV wall, and an ischaemic RV fails further — the loop that turns a stable patient into an arrest within hours."),
    ('e', "**Hypoxaemia from V/Q mismatch (dead space plus over-perfused units), low mixed venous saturation, right-to-left shunt through a PFO, and atelectasis from surfactant loss.** Blood diverted from blocked vessels over-perfuses the rest, lowering V/Q there; low cardiac output lowers mixed venous saturation, which lowers arterial saturation through any shunt; raised right atrial pressure can open a patent foramen ovale. The blocked segments are dead space, so end-tidal CO₂ falls (PE-07’s intra-operative case)."),
  ],
  mimic=[
    ("Acute PE vs chronic pulmonary hypertension", "An unconditioned RV cannot generate a mean PA pressure above about 40 mmHg; a higher value means a hypertrophied RV and chronic disease (CTEPH, PE-03)."),
  ],
  traps=[
    ("“Acute collapse in PE is explained by a mean PA pressure >40 mmHg” [DocT GT key]", "Physiologically wrong: a previously normal RV fails before it can reach 40 mmHg; a value that high implies chronic PH. The better answer is occlusion of a large part of the bed (the option ‘>40%’, within the 30–50% range) with acute RV failure. 73% followed the key."),
    ("“Increased LV afterload causes the collapse”", "LV preload falls (septal shift, low RV output); the afterload that rises is the RV’s."),
  ],
  decode=[
    ("Large PE after hip surgery, hypotensive, dilated RV — which finding explains the collapse? [DocT GT, 73% chose the key]", "Keyed mean PA pressure >40 mmHg; the right answer is pulmonary artery occlusion beyond 30–50% with acute RV failure."),
  ],
  punch="Acute PE kills through the right ventricle: once 30–50% of the bed is blocked, afterload rises past what a thin RV can meet (it cannot generate a mean PA pressure above about 40 mmHg), the septum squeezes the LV and RV ischaemia closes the loop.",
)

L['PE-05'] = dict(
  sub="Respiratory → Pulmonary embolism → High-risk PE: the definition",
  step=3,
  intro="Step 3 ends where the RV spiral shows itself at the bedside. Because death comes from RV failure, ESC defines high-risk PE by the state of the circulation, and any one of three presentations is enough. This definition is the first branch of the diagnostic pathway (PE-13) and of the risk classes in RESP06B.",
  parts=[
    ('a', "**Cardiac arrest.** The end of the RV spiral; reperfusion is considered during resuscitation."),
    ('b', "**Obstructive shock: systolic BP <90 mmHg or vasopressors needed to keep it ≥90 despite adequate filling, AND end-organ hypoperfusion (altered mentation, cold clammy skin, oliguria or anuria, raised lactate).** The pattern is that of obstruction: high filling pressures (CVP), low cardiac output, high systemic vascular resistance as the body vasoconstricts, low mixed venous saturation and a raised lactate."),
    ('c', "**Persistent hypotension: systolic BP <90 mmHg or a fall of ≥40 mmHg lasting >15 minutes, not caused by new arrhythmia, hypovolaemia or sepsis.** The time limit separates sustained failure from a transient dip, and the exclusions keep other causes of low pressure from being labelled PE."),
  ],
  mimic=[
    ("Obstructive vs cardiogenic shock", "Both have high filling pressures, low output and high SVR. In obstructive shock the pump is normal and the outflow is blocked (PE, tamponade, tension pneumothorax); echo shows a dilated RV with a small, vigorous LV rather than a failing LV."),
  ],
  traps=[
    ("“High-risk PE means a large or saddle clot on CT”", "Risk is set by the haemodynamics; a saddle embolus in a normotensive patient is not high-risk."),
  ],
  decode=[
    ("Massive PE with shock: high filling pressures, low CO, high SVR, high lactate, low SvO₂ — shock category? [DocT GT]", "Obstructive shock."),
  ],
  punch="High-risk PE is cardiac arrest, obstructive shock (SBP <90 or vasopressors with hypoperfusion) or persistent hypotension (SBP <90 or a ≥40 mmHg fall for >15 minutes) — defined by the circulation, not by the clot.",
)

L['PE-06'] = dict(
  sub="Respiratory → Pulmonary embolism → Clinical presentation, gases and chest X-ray",
  step=4,
  intro="Step 4 is what the patient looks like, and the message is how little that settles. Every symptom of PE is common in patients without PE, the saturation and gradient can be normal, and the film is usually near normal. The questions test which tests are usually abnormal, the blood gas of PE, and the rare film signs.",
  parts=[
    ('a', "**Dyspnoea 50%, pleuritic chest pain 39%, cough 23%, signs of DVT 24%, haemoptysis 8%, syncope 6%.** Reported frequencies vary widely between series (PIOPED, for example, reported dyspnoea in 73% and pleuritic pain in 66%), so the order matters more than the exact figure. Pleuritic pain and haemoptysis come from small peripheral emboli that infarct the lung next to the pleura; syncope comes from a large central clot that drops cardiac output, so it marks a more dangerous embolus. Tachypnoea and tachycardia are the commonest signs."),
    ('b', "**Saturation is normal in up to 40% and the A–a gradient in about 20%.** A normal SpO₂ or gradient does not exclude PE. The typical gas is hypoxaemia with hypocapnia and respiratory alkalosis: dead space and reflex drive make the patient hyperventilate, and the clear chest on examination separates it from pneumonia and fibrosis."),
    ('c', "**The chest X-ray is non-specific; its value is to rule out other causes.** It is often normal or shows atelectasis, a small effusion or a raised hemidiaphragm. The named signs are specific but rare: Westermark sign (focal oligaemia beyond an embolus), Hampton hump (a pleural-based wedge of infarction) and Fleischner (Palla) sign (an enlarged central pulmonary artery). A normal film also makes a perfusion-only scan interpretable (PE-11)."),
  ],
  mimic=[
    ("PE vs fibrosing alveolitis", "Both give type 1 failure with low PaCO₂. A clear chest favours PE; fine bibasal ‘velcro’ crackles and clubbing favour fibrosis."),
    ("Westermark sign vs generalised oligaemia", "Westermark is focal oligaemia beyond an embolus; generalised oligaemia suggests pulmonary hypertension or pulmonary stenosis, and a unilateral hyperlucent lung Macleod syndrome."),
  ],
  traps=[
    ("“A normal saturation or ABG argues against PE”", "Saturation is normal in up to 40%; the test most likely to be abnormal is the D-dimer (sensitivity above 95%), not the gas, SpO₂ or ECG (77% right)."),
    ("“Weeks of breathlessness, PaO₂ 8.4 kPa, PaCO₂ 4.0 kPa, pH 7.51, clear chest: fibrosing alveolitis or atypical pneumonia”", "Hypoxaemia with respiratory alkalosis and a clear chest, afebrile, is pulmonary thromboembolism (here recurrent). Only 36% chose it."),
  ],
  decode=[
    ("Which test is most likely to be abnormal in PE: ABG, SpO₂, ECG or D-dimer? [DocT, 77% right]", "D-dimer."),
    ("58-year-old non-smoker, a month of breathlessness, afebrile, normal breath sounds, pH 7.51, PaO₂ 8.4 kPa, PaCO₂ 4.0 kPa — diagnosis? [DocT, 36% right]", "Pulmonary thromboembolism."),
    ("CXR report: ‘pulmonary oligaemia consistent with the Westermark sign’ — what is suggested? [DocT GT, 83% right]", "Pulmonary embolism."),
  ],
  punch="PE has no discriminating symptom, saturation is normal in up to 40% and the film is usually near normal; hypoxaemia with a low PaCO₂ and a clear chest is the gas, and Westermark, Hampton and Fleischner are rare but specific film signs.",
)

L['PE-07'] = dict(
  sub="Respiratory → Pulmonary embolism → The ECG",
  step=4,
  intro="Step 4 continues with the ECG. A sudden rise in RV afterload produces a set of right-heart strain changes, but they appear mainly with large emboli, so the commonest finding is the least specific one. The questions test exactly that gap between the famous sign and the frequent one.",
  parts=[
    ('a', "**Sinus tachycardia, 44%.** ESC 2019 gives about 40%; a 2025 meta-analysis (24 studies, 7,467 patients) pooled 31%. Older series often reported non-specific ST–T changes as frequently as tachycardia, which is why exam options pair them as ‘tachycardia or non-specific ST–T changes’."),
    ('b', "**T inversion in V1–V4 and in II, III, aVF: 34%.** Over the right precordial leads it reflects RV strain and ischaemia; it is the commonest strain sign in large PE and is linked to RV dysfunction and a worse outcome. The 2025 meta-analysis pooled 18% for T inversion in V1–V3 across all PE."),
    ('c', "**S1Q3T3 20%; complete or incomplete RBBB 18%; right axis 16%; P pulmonale 9%; atrial tachyarrhythmias 8%.** S1Q3T3 (an S wave in I, a Q wave and inverted T in III) reflects acute rotation and dilatation of the RV; RBBB reflects stretch of the right bundle. The meta-analysis pooled 15% for S1Q3T3 and 14% for RBBB. These numbers vary by series; the order is what is tested."),
    ('d', "**The most specific finding is simultaneous T inversion in the inferior and right precordial leads.** Anterior T inversion alone is common in anterior ischaemia; the same change in the inferior leads at the same time points to the right ventricle, which spans both territories."),
  ],
  mimic=[
    ("PE vs anterior ischaemia (Wellens-type T waves)", "Both invert T waves in V1–V4. Simultaneous inferior T inversion, sinus tachycardia and RBBB favour PE; ST elevation or a culprit territory favours ischaemia."),
  ],
  traps=[
    ("“Breathless after a 7-hour flight with calf pain: the commonest ECG finding is S1Q3T3”", "Commonest is tachycardia with non-specific ST–T changes; S1Q3T3 is in about one in five. Only 37% chose it."),
    ("“Smoker in respiratory failure, BP 140/90, HR 115, CVP 18 — this is PE” [DocT key]", "Keyed PE (27%), but a normal pressure with a high CVP fits a COPD exacerbation with cor pulmonale just as well, and DocT’s explanation wrongly calls the patient hypotensive. Choose PE only if forced; the item is ambiguous."),
    ("“IV heparin is the treatment of choice for shock from PE straight after spine surgery”", "This is the statement least likely true: shock means high-risk PE needing reperfusion, and with lysis contraindicated after spinal surgery that means surgical or catheter embolectomy (RESP06B); heparin is the background, not the treatment of choice. 42% got this right."),
  ],
  decode=[
    ("36-year-old, breathless at rest two days after a 7-hour flight, left calf pain — commonest ECG finding? [DocT, 37% right]", "Tachycardia with non-specific ST–T changes."),
    ("Smoker, acute respiratory failure, BP 140/90, HR 115, CVP 18 — most likely cause? [DocT, 27% right]", "Keyed acute PE; ambiguous."),
    ("After spinal surgery: SpO₂ 86%, HR 124, BP 85/41, EtCO₂ 15 — which statement about PE is LEAST likely true? [DocT GT, 42% right]", "‘IV heparin is the treatment of choice’; S1Q3T3 in under about 20%, dead-space V/Q mismatch and uncommon haemoptysis are all true."),
  ],
  punch="Sinus tachycardia (with non-specific ST–T change) is the commonest ECG finding in PE; S1Q3T3 is present in only about one in five, and T inversion in the inferior and right precordial leads together is the most specific.",
)

L['PE-08'] = dict(
  sub="Respiratory → Pulmonary embolism → Wells score",
  step=5,
  intro="Step 5 begins the diagnosis proper: before any test, set the pre-test probability, because it decides whether a D-dimer can be trusted (PE-10) and how to read the CT (PE-11). The Wells score is the most used rule, and the real questions are arithmetic — and two of them are keyed wrongly.",
  parts=[
    ('a', "**Clinical signs of DVT 3; alternative diagnosis less likely than PE 3; heart rate >100 1.5; surgery or immobilisation in the past 4 weeks 1.5; previous PE or DVT 1.5; haemoptysis 1; active cancer 1.** Immobilisation means bed rest for at least 3 days, so a recent hospital admission usually counts. The ‘alternative diagnosis less likely’ item is the subjective one, and it carries as many points as DVT signs, so whether the stem says ‘no alternative diagnosis is more likely’ decides the total."),
    ('b', "**Three-level: low <2; intermediate 2–6; high >6.** ESC prints 0–1, 2–6 and ≥7; with half-points, 6.5 counts as high. The prevalence of PE is roughly 10%, 30% and 65% in the three groups."),
    ('c', "**Two-level: PE unlikely ≤4; PE likely >4 (ESC prints 0–4 and ≥5).** The two-level form is what pathways use: unlikely goes to D-dimer, likely goes to CTPA (PE-13)."),
    ('d', "**Simplified (one point each): unlikely 0–1, likely ≥2.** The same seven items each score 1, which removes the half-points and makes it quicker at the bedside; it is used only as a two-level rule, so ‘likely’ leads to CTPA and ‘unlikely’ to D-dimer, as in the full version."),
  ],
  table=dict(title="Working the two real stems", head=["Stem", "Points", "Total and category"], rows=[["Knee replacement 2 weeks ago, HR 112, DVT signs, no alternative more likely", "3 + 3 + 1.5 + 1.5", "**9: high (>6)**"], ["Leg swelling and tenderness, HR 110, admitted for pneumonia 2 weeks ago, no prior VTE, haemoptysis or cancer", "3 + 1.5 + 1.5 (+3 only if PE is judged most likely)", "**6: intermediate (three-level), PE likely (two-level)**; 9 if the item is counted"]]),
  mimic=[
    ("Wells vs revised Geneva", "Wells includes the subjective ‘alternative diagnosis less likely’; Geneva is fully objective (PE-09)."),
  ],
  traps=[
    ("“6 points — high probability” [DocT GT key]", "6 is intermediate in the three-level Wells (2–6; high is >6) and ‘PE likely’ in the two-level form. DocT keys ‘6 — high’ and its explanation adds to 9, so the key is internally inconsistent. Pick 6 if the number is asked; know the category is intermediate. 36–40% followed the key."),
    ("“Wells and Geneva are accurate in ventilated ICU patients”", "Neither was validated in critically ill patients (PE-11)."),
  ],
  decode=[
    ("63-year-old, pleuritic pain, right leg swelling and tenderness, HR 110, hospitalised for pneumonia 2 weeks ago — Wells score? [DocT GT, twice, 36% and 40% right]", "Keyed ‘6 points — high’; 6 is right as a number, but the category is intermediate."),
    ("Knee replacement 2 weeks ago, HR 112, DVT signs, no alternative more likely — interpretation? [DocT GT]", "High probability (9 points, >6)."),
  ],
  punch="Wells gives 3 each for DVT signs and ‘PE most likely’, 1.5 each for HR >100, recent surgery or immobilisation and prior VTE, and 1 each for haemoptysis and cancer; >6 is high, and ≤4 versus >4 is the two-level split pathways use.",
)

L['PE-09'] = dict(
  sub="Respiratory → Pulmonary embolism → Revised Geneva score",
  step=5,
  intro="Step 5 continues with the other validated rule. It does the same job as Wells but removes the clinician’s judgement, so two people scoring the same patient get the same number.",
  parts=[
    ('a', "**Geneva is fully objective: no ‘alternative diagnosis less likely’ item; it adds age >65 and grades heart rate.** Because every item can be checked, it suits protocols and scoring by non-specialists."),
    ('b', "**Previous PE or DVT 3; heart rate 75–94 = 3, ≥95 = 5; surgery or fracture within 1 month 2; haemoptysis 2; active cancer 2; unilateral leg pain 3; pain on deep venous palpation with unilateral oedema 4; age >65 = 1.** Note the heart-rate thresholds differ from Wells (75 and 95, not 100)."),
    ('c', "**Low 0–3, intermediate 4–10, high ≥11; two-level unlikely 0–5, likely ≥6; simplified unlikely 0–2, likely ≥3.** In the simplified version every item scores 1 (heart rate ≥95 scores 2), with a three-level split of 0–1, 2–4 and ≥5."),
  ],
  mimic=[
    ("Geneva vs Wells heart-rate item", "Wells: >100 for 1.5. Geneva: 75–94 for 3 and ≥95 for 5."),
  ],
  traps=[
    ("“The revised Geneva score includes ‘alternative diagnosis less likely’”", "That is the Wells item; Geneva has none, which is its point."),
  ],
  decode=[
    ("[pattern] Which PE probability score uses only objective items and includes age >65?", "Revised Geneva."),
  ],
  punch="Revised Geneva is Wells without the judgement call: objective items, age >65 and graded heart rate, with high at ≥11 and ‘PE likely’ at ≥6.",
)

L['PE-10'] = dict(
  sub="Respiratory → Pulmonary embolism → D-dimer",
  step=5,
  intro="Step 5 now uses the probability. D-dimer is a fibrin breakdown product, raised whenever clot is made and lysed — by PE, but also by almost any illness. So it is a rule-out test whose value depends entirely on the pre-test probability set in PE-08 and PE-09.",
  parts=[
    ('a', "**Its strength is a high negative predictive value; quantitative ELISA sensitivity >95%; a moderately sensitive assay is valid only in low probability.** A normal result in a patient unlikely to have PE excludes it without imaging; a raised one means nothing on its own. Point-of-care assays are less sensitive (about 88%), so they are trusted only when probability is low."),
    ('b', "**Age-adjusted cut-off: age × 10 µg/L over 50.** D-dimer rises with age, so a fixed 500 µg/L excludes few elderly patients. In ADJUST-PE (3,346 patients) the age-adjusted cut-off missed 1 of 331 patients with values between 500 and their cut-off (0.3%), and in those aged 75 or more it raised the share excluded from 6.4% to 29.7%. Two pathways adjust the cut-off to probability instead: YEARS (no YEARS item — DVT signs, haemoptysis, PE most likely — and D-dimer <1000 ng/mL, or one or more items and <500) and PEGeD (low probability, Wells 0–4, <1000; moderate, Wells 4.5–6, <500), which in 2,017 outpatients cut chest imaging from 51.9% to 34.3% with no VTE at 3 months in those excluded. In a very low-probability patient the PERC rule (age <50, HR <100, SpO₂ ≥95%, no haemoptysis, no oestrogen, no prior VTE, no unilateral leg swelling, no surgery or trauma needing hospital care in 4 weeks) avoids the D-dimer altogether."),
    ('c', "**Do not use it in high clinical probability (a normal result does not exclude PE); of limited use in hospitalised patients.** When PE is likely, even a sensitive test leaves too many missed cases, so go straight to CTPA. In inpatients, and above all in the ICU, D-dimer is almost always raised, so a negative is rare and a positive is meaningless."),
    ('d', "**False positives: cancer, sepsis or inflammation, trauma, bleeding, surgery, pregnancy, necrosis.** Every one makes and breaks down fibrin."),
  ],
  mimic=[],
  traps=[
    ("“76-year-old, pleuritic pain, fever 38°C, WCC 14, right basal shadowing, femur surgery 2 months ago, D-dimer normal — CT chest”", "Fever, leucocytosis and consolidation make pneumonia the likelier diagnosis, the surgery is beyond the 4-week Wells window, so probability is not high and a normal D-dimer excludes PE: start IV antibiotics. Only 31% chose this."),
    ("“A negative high-sensitivity D-dimer rules out PE in a ventilated ICU patient”", "D-dimer is almost always raised in the ICU and is not validated there; image if PE is suspected (PE-11)."),
  ],
  decode=[
    ("Which test is most likely to be abnormal in PE? [DocT, 77% right]", "D-dimer (high sensitivity)."),
    ("76-year-old, fever, WCC 14, basal shadowing, normal D-dimer, surgery 2 months ago — next step? [DocT, 31% right]", "IV antibiotics; PE is excluded."),
  ],
  punch="D-dimer only rules out, and only when probability is low or intermediate; over 50 use age × 10 µg/L, never use it in high probability, and in hospital or ICU patients it is almost always raised.",
)

L['PE-11'] = dict(
  sub="Respiratory → Pulmonary embolism → CTPA and V/Q scan",
  step=6,
  intro="Step 6 is imaging. CT pulmonary angiography is the workhorse, but the question pack shows what is really tested: that its predictive values depend on pre-test probability, that it stays the test of choice in the ICU, and when a V/Q scan is a sensible alternative.",
  parts=[
    ('a', "**CTPA sensitivity 83% and specificity 96% (PIOPED II).** The 83% belongs to the early multidetector scanners of PIOPED II; modern scanners resolve smaller vessels. In ventilated ICU patients sensitivity may fall further, because the patient cannot hold their breath and the ventilator can interrupt the contrast bolus, but CTPA remains the reference test there."),
    ('b', "**Segmental or more proximal clot is diagnostic; isolated subsegmental defects may need further tests.** Small subsegmental defects have the most false positives and inter-observer disagreement, so they are confirmed (for example by leg ultrasound) and judged with the clinical picture."),
    ('c', "**Negative predictive value 96% in low, 89% in intermediate and only 60% in high probability; positive predictive value 92–96% in intermediate or high, only 58% in low.** This is pre-test probability at work: a negative CT in a patient who very probably has PE leaves a real chance of PE, and a positive CT in a patient who very probably does not may be false. A result that disagrees with the clinical probability needs another test."),
    ('d', "**V/Q: a normal perfusion scan excludes PE; a high-probability scan confirms it; the rest are non-diagnostic. With a normal chest X-ray a perfusion scan alone is enough.** Perfusion defects in a ventilated region (mismatch) mean embolism; planar V/Q is diagnostic (normal or high probability) in only about 30–50% of emergency patients, whereas SPECT is non-diagnostic in under 3%. It uses less radiation and no contrast, so it suits pregnancy, contrast allergy and renal failure — but the patient must be stable, ventilation imaging must be possible, and the chest film should be clear. CT venography is not recommended as an add-on to CTPA."),
  ],
  mimic=[
    ("CTPA vs V/Q", "CTPA shows the clot and alternative diagnoses, needs contrast and gives more radiation (3–10 mSv). V/Q needs no contrast (about 2 mSv) and suits the young, the pregnant and renal failure, but needs a mobile patient and a clear film."),
  ],
  traps=[
    ("“Stage 4 CKD, so order a V/Q scan” (ventilated, septic, on vasopressors)", "A ventilated ICU patient cannot have a V/Q scan; stable with high probability goes to CTPA (74% right)."),
    ("“Rule out PE because he is on prophylactic anticoagulation”", "Prophylaxis lowers but does not remove risk."),
    ("“In the ICU a negative D-dimer, a negative leg ultrasound or a Wells score settles it”", "D-dimer is almost always raised, a negative leg scan does not exclude PE, and Wells and Geneva are not validated in critically ill patients; CTPA remains the reference test, with sensitivity reduced by motion and the lack of a breath-hold."),
  ],
  decode=[
    ("Swollen right leg, sudden chest pain, CT angiogram shown — diagnosis? [DocT and DocT GT, 86% and 100% right]", "Pulmonary embolism (filling defect in the pulmonary artery)."),
    ("Obese, CKD 4, ventilated, on vasopressors, day 3: pleuritic pain, haemoptysis, loud P2, precordial T inversion, D-dimer up — next step? [DocT GT, 74% right]", "CT pulmonary angiography."),
    ("Ventilated for 10 days on prophylactic LMWH, HR 120, SpO₂ 98% → 90% — most accurate statement on diagnosis? [DocT GT]", "CTPA is the gold standard, but motion and no breath-hold may reduce its sensitivity."),
  ],
  punch="CTPA (83% sensitive, 96% specific in PIOPED II) is diagnostic at segmental level or above, but a negative scan in high probability has an NPV of only 60%; a normal perfusion scan excludes PE, and V/Q is for the stable, mobile patient with a clear film.",
)

L['PE-12'] = dict(
  sub="Respiratory → Pulmonary embolism → Echocardiography and compression ultrasound",
  step=6,
  intro="Step 6 continues at the bedside, the card asked most often in this deck. Ultrasound looks for the two consequences of PE: a right ventricle under pressure overload, and the clot’s source in the leg veins. The questions test which echo signs point to acute PE rather than to other causes of a big RV, what a negative scan means, and what to do with a proximal DVT.",
  parts=[
    ('a', "**RV overload: RV/LV ratio >1; septal flattening; McConnell sign (RV free-wall hypokinesia with the apex spared); 60/60 sign (pulmonary ejection acceleration time <60 ms with a tricuspid gradient <60 mmHg); TAPSE <16 mm; S′ <9.5 cm/s; dilated IVC; mobile right-heart thrombus.** A flattened septum gives the D-shaped LV in short axis. McConnell sign is thought to reflect the apex being tethered to a hyperdynamic LV; in the original study (85 patients with RV dysfunction, 13 with PE) it was 77% sensitive and 94% specific, but in a later cohort of 100 suspected PE (Kurzyna 2002) it was only 19% sensitive, and it is seen in about two-thirds of RV infarctions (Casazza 2005), so it does not separate PE from RV infarction. The 60/60 sign combines a short acceleration time (a pressure-loaded pulmonary artery) with a tricuspid gradient that is only modestly raised (an RV that cannot generate high pressure): that pairing means acute pressure overload, not chronic PH or RV infarction. In the same Kurzyna cohort it was specific (94%) but insensitive (25%). A mobile thrombus in the right heart is a direct sign and strengthens the case for reperfusion."),
    ('b', "**Stable patient: echo is not recommended for diagnosis (negative predictive value only 40–50%; RV dilatation in only 25%). Unstable patient: no RV overload excludes PE as the cause of shock; clear RV overload justifies reperfusion if CT is not feasible.** In a stable patient a normal RV does not exclude PE, because most emboli are too small to strain it. In shock the logic reverses: a PE big enough to cause shock must strain the RV, so a normal RV points elsewhere, and a strained RV in a patient too sick for CT is enough to treat as high-risk PE (PE-13). In stable patients echo is used afterwards for risk stratification (RESP06B)."),
    ('c', "**Compression ultrasound finds DVT in 30–50% of patients with PE; incomplete compressibility is the only validated criterion; a proximal DVT is enough to anticoagulate.** A vein that will not flatten under the probe contains clot. A proximal DVT in a patient with suspected PE confirms VTE, and the treatment is the same, so no CTPA is needed to start anticoagulation. A negative scan does not exclude PE, because the whole clot may already have embolised. Lung ultrasound adds a third window: small pleural-based wedge-shaped hypoechoic consolidations are infarcts, and RV dilatation, a non-compressible vein and subpleural infarcts together are far more specific than any one."),
  ],
  table=dict(title="Which echo sign answers which question", head=["Question", "Sign", "Why"], rows=[["Most suggestive of acute PE", "**RV (and RA) dilatation**", "the direct effect of sudden afterload"], ["PE rather than RV infarction", "**60/60 sign**", "needs a pressure-loaded pulmonary artery; RV infarction has a normal one, and McConnell sign occurs in both"], ["PE vs chronic pulmonary hypertension", "RV wall thickness, TR gradient", "chronic PH has a thick RV and a TR gradient well above 60 mmHg"], ["Not expected in acute PE", "left atrial enlargement, concentric LVH", "chronic left-sided disease"]]),
  mimic=[
    ("Acute PE vs RV infarction", "Both give RV dilatation, low TAPSE and McConnell sign; the 60/60 sign, a normal right-sided ECG (no ST elevation in V4R) and a DVT favour PE."),
    ("PE vs tamponade", "Both cause obstructive shock with a high CVP; tamponade shows a pericardial effusion with RV diastolic collapse, PE a dilated RV with a small LV."),
  ],
  traps=[
    ("“McConnell sign is the most specific sign of PE versus RV infarction”", "McConnell sign appears in about two-thirds of RV infarctions; the 60/60 sign is the discriminator. TAPSE <15 mm and a D-shaped LV occur in any RV overload."),
    ("“RV hypokinesia with preserved apex in a man with stented CAD is acute MI” [NEET 2025 recall]", "Keyed pulmonary embolism: McConnell sign with acute dyspnoea. The coronary history tempts towards MI, and RV infarction can show the same pattern, but the recall’s answer is PE."),
    ("“A negative leg scan rules PE out”", "DVT is found in only 30–50% of PE; normal LV function is expected in PE, and bilateral pleural sliding only excludes pneumothorax."),
    ("“Proximal DVT found: confirm with CTPA or wait for echo before treating”", "A proximal DVT in suspected PE is enough to start anticoagulation (85% right)."),
  ],
  decode=[
    ("ICU patient, sudden hypoxia and hypotension, multiorgan ultrasound — which finding most supports PE? [DocT, 86% right]", "Subpleural infarcts with RV dilatation."),
    ("Obstructive shock after a long flight, RV:LV ratio 1.2 — most specific for PE rather than RV infarction? [DocT GT]", "The 60/60 sign."),
    ("Suspected PE, venous ultrasound shows proximal DVT — next step? [DocT GT, 85% right]", "Start anticoagulation immediately."),
    ("Echo finding most suggestive of acute PE: hyperdynamic small LV, concentric LVH, RA/RV dilatation, effusion with RV collapse? [DocT GT, PYQ]", "RA/RV dilatation."),
    ("Stented CAD, acute dyspnoea, RV hypokinesia with preserved apical contraction — diagnosis? [NEET 2025 recall]", "Pulmonary embolism (McConnell sign)."),
    ("Least likely in acute PE: LA enlargement, RV strain, Westermark sign, McConnell sign? [NEET 2025 recall]", "Left atrial enlargement."),
  ],
  punch="Echo shows the strained RV — dilatation, septal flattening, McConnell sign, 60/60 sign — and the 60/60 sign, not McConnell, separates PE from RV infarction; in shock a normal RV excludes PE, and a proximal DVT on compression ultrasound is enough to anticoagulate.",
)

L['PE-13'] = dict(
  sub="Respiratory → Pulmonary embolism → The diagnostic pathway",
  step=6,
  intro="Step 6 closes by putting the deck together. The first branch is the circulation (PE-05): an unstable patient may not survive a trip to CT, so the test must come to the bedside. In a stable patient the pre-test probability (PE-08) decides whether D-dimer (PE-10) or CTPA (PE-11) comes first. Whatever the branch, treatment does not wait for the answer when PE is likely.",
  parts=[
    ('a', "**Haemodynamic instability: bedside echo first. RV dysfunction → CTPA if immediately available and the patient can be moved, otherwise treat as high-risk PE. No RV dysfunction → look for another cause.** Echo answers the one question that matters in shock — is the RV strained? — in minutes (PE-12b). Bedside compression ultrasound can add a proximal DVT. Once CTPA confirms PE, or echo alone if CT is impossible, reperfusion follows (RESP06B)."),
    ('b', "**Stable, low or intermediate probability (PE unlikely): D-dimer; if positive, CTPA.** A negative D-dimer (age-adjusted over 50, or by YEARS or PEGeD) ends the work-up without imaging; a positive one leads to CTPA, and a normal CTPA then excludes PE."),
    ('c', "**Stable, high probability (PE likely): CTPA directly, no D-dimer.** A normal D-dimer cannot exclude PE here, so measuring it only delays the scan. A negative CTPA in high probability (NPV 60%) may need further testing."),
    ('d', "**Anticoagulation starts without delay in high or intermediate probability, while the tests proceed; unfractionated heparin at once if unstable.** The risk of an untreated PE in the hours of work-up outweighs the bleeding risk of a few doses of heparin. Unfractionated heparin is used in the unstable patient because it is short-acting and reversible and reperfusion may follow within hours; in a stable patient LMWH is usual, and in pregnancy LMWH or heparin is given (warfarin crosses the placenta)."),
  ],
  table=dict(title="The pathway", head=["Patient", "First test", "Then"], rows=[["Unstable", "**bedside echo**", "RV strain: CTPA if feasible, else treat as high-risk PE; no strain: another cause"], ["Stable, PE unlikely", "**D-dimer**", "negative: stop; positive: CTPA"], ["Stable, PE likely", "**CTPA**", "positive: treat; negative but suspicion high: further tests"], ["Any, intermediate or high probability", "**anticoagulate now**", "UFH if unstable"]]),
  mimic=[],
  traps=[
    ("“Hypotensive, haemoptysis, JVD, raised troponin: CT angiogram first” [Marrow key]", "ESC 2019 puts bedside echo first in instability; CTPA only if immediately available and the patient can travel. Pick echo whenever it is offered; if it is not, CTPA is the best of the remaining options."),
    ("“Pregnant woman with strongly suspected PE: wait for imaging, or start warfarin”", "Begin heparin immediately (81–100% right); warfarin is teratogenic, and aspirin and oxygen alone do not treat PE."),
    ("“Stable, high probability: measure a D-dimer first”", "A normal D-dimer cannot exclude PE when it is likely; go straight to CTPA."),
  ],
  decode=[
    ("Ventilated, on vasopressors for septic shock, CKD 4, day 3: pleuritic pain, haemoptysis, loud P2 — next step? [DocT GT, 74% right]", "CT pulmonary angiography."),
    ("32 weeks pregnant, sudden dyspnoea, pleuritic pain, hypoxia, PE strongly suspected — initial step? [DocT GT, twice, 81% and 100% right]", "Begin IV heparin immediately."),
    ("Day 10 after colectomy, SBP 90, SpO₂ 87% — immediate test? [Marrow]", "CTPA (high probability, not shocked)."),
    ("On the pill, smoker, hypotensive, haemoptysis, raised JVP and troponin — next step? [Marrow]", "Keyed CT angiogram; by ESC 2019 bedside echo comes first if offered."),
  ],
  punch="Unstable: bedside echo, and RV strain alone justifies treatment if CT is not feasible. Stable and unlikely: D-dimer, then CTPA if positive. Stable and likely: CTPA directly. Anticoagulate at once whenever probability is intermediate or high.",
)

FLAGS = {}
FLAGS['PE-01'] = "Card d uses ‘provoked/unprovoked’; ESC 2019 no longer supports these terms and classifies by transient or reversible (major or minor), persistent, or no identifiable risk factor. Consequences are the same; explanation notes the newer wording."
FLAGS['PE-02'] = "NEET 2024 recall keys PNH as an ‘inherited’ hypercoagulable state; PNH is acquired (somatic PIGA mutation), as are PV and APS. Card c omits PNH from acquired thrombophilias — consider adding it."
FLAGS['PE-03'] = "Card a says DVT risk is highest in the first 2 weeks after surgery; in the Million Women Study (Sweetland, BMJ 2009) the risk of admission with VTE peaked in the third postoperative week and stayed raised to 12 weeks — consider ‘first few weeks (peak about week 3)’. Card b gives CTEPH 1.5% within 24 months; ESC 2019 range 0.1–9.1% is verified, but pooled estimates are 0.56% of all comers and 3.2% of survivors (Ende-Verhaar 2017), so ~2–4% of survivors is the usual teaching figure; the card’s 1.5% sits low. Card c’s 13%/23%/30% match Heit 2000 (12.9%/22.8%/30.4%, including possible recurrences), but in that cohort recurrence within 6 months was 10.1% (8.3% at 90 days), not 8%; ESC 2019 expresses late recurrence per year (≈2.5%/yr transient factor, ≈4.5%/yr no factor). Marrow note: consider adding CTEPH treatment (endarterectomy + lifelong anticoagulation; BPA/riociguat if inoperable)."
FLAGS['PE-04'] = "Card is right; DocT GT keys ‘mean PA pressure >40 mmHg’ as the cause of collapse, which contradicts the card’s own watch line. Explanation teaches the card and names the key as wrong."
FLAGS['PE-07'] = "Card figures (sinus tachycardia 44%, T inversion 34%, S1Q3T3 20%, RBBB 18%) are from a single series whose source could not be identified online; ESC 2019 says ~40% for sinus tachycardia and a 2025 meta-analysis (24 studies, 7,467 patients) pooled 31%, 15% (S1Q3T3), 18% (TWI V1–V3), 14% (RBBB). Order unchanged. DocT key ‘PE’ for the BP 140/90, CVP 18 smoker stem is ambiguous (COPD with cor pulmonale fits equally)."
FLAGS['PE-08'] = "DocT GT (twice) keys ‘6 points — high probability’: 6 is intermediate on the three-level Wells (2–6) and ‘likely’ on the two-level; DocT’s explanation totals 9. Card cut-offs are right."
FLAGS['PE-13'] = "Marrow keys CT angiography first for suspected PE with hypotension; card (ESC 2019) says bedside echo first, CTPA only if immediately available and feasible. Explanation teaches the card and how to answer when echo is not offered."
