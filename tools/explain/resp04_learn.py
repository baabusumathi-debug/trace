# RESP04 — Explain v3 ("Learn" depth): acute respiratory failure in the immunocompromised, bronchopleural fistula and air leak, and the brain-dead lung donor. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP04.md (12 questions; RSC-19 post-HSCT lung asked 4 times, RSC-20 CT patterns 3 times). Fields as TOX01, plus SPINE, PRIMER and step.
# Cards with no linked question get short explanations with [pattern] decode items.
# Trial figures checked online on 10 Nov 2026: Hilbert 2001, Antonelli 2000, Lemiale 2015, HIGH 2018, FLORALI post hoc and FLORALI-IM 2022, EFRAIM 2017 and its ARDS analysis,
# LUNG SAFE immunocompromised analysis, Schmidt ECMO cohort, BMT CTN 0403 (etanercept), Keklik 2018 (DAH), Mascia 2010, French donor cohort (AJRCCM 2020), post-apnoea-test recruitment study.

SPINE = [
  ("Who fails, and from what", "In the immunocompromised patient with respiratory failure infection causes most cases, bacteria first, and the kind of immune defect predicts which organism; a cause left undetermined carries a worse outcome."),
  ("The transplant lung by calendar", "After stem-cell transplant the date tells you the likely cause: neutropenic infection, engraftment syndrome and alveolar haemorrhage in the first month, CMV, Pneumocystis and idiopathic pneumonia syndrome to day 100, and bronchiolitis obliterans after that."),
  ("Pattern to pathogen", "On CT, ground glass points to Pneumocystis or a virus, nodules to moulds and Nocardia, and the non-invasive tests come before a risky bronchoscopy."),
  ("Support and outcome", "NIV and high-flow oxygen have not lowered mortality in the large trials, so they are time-limited trials, and once ARDS develops it is ventilated as any ARDS, with organ failures and an undetermined cause, not neutropenia, predicting death."),
  ("The leaking lung", "Flow through a bronchopleural fistula follows the transpulmonary pressure and the time it is applied, so the ventilator and the drain are set to keep that pressure low, with lung isolation, high-frequency ventilation and bronchoscopic plugs or valves for leaks that persist."),
  ("The brain-dead lung donor", "Only a small share of donors yield lungs, because brain death injures them and ventilation can add to it; protective donor ventilation and an apnoea test on CPAP roughly doubled the lungs harvested."),
]

PRIMER = "Each arm of immunity guards against its own set of organisms: neutrophils clear bacteria and moulds, T cells control viruses, Pneumocystis and intracellular organisms, and antibodies with the spleen clear encapsulated bacteria. After a stem-cell transplant the patient is neutropenic until engraftment, the day the donor marrow starts making neutrophils, usually in the second to fourth week; T-cell and antibody immunity take months to return. The P/F ratio (PaO₂ divided by FiO₂) grades hypoxaemia, and in the Berlin definition ARDS is mild at 200–300, moderate at 100–200 and severe below 100 mmHg. Transpulmonary pressure is airway minus pleural pressure, the pressure that holds the lung open and that pushes gas through any hole in it."

L = {}

L['RSC-17'] = dict(
  sub="Respiratory → Immunocompromised → Causes of acute respiratory failure",
  step=1,
  intro="The deck opens with the question every immunocompromised patient with new hypoxaemia poses: what is it? Most causes are infections and treatable, so the cause, not the oxygen device, decides the outcome.",
  parts=[
    ('a', "**Infectious about 60%; non-infectious about 25%.** The non-infectious share is drug toxicity, the disease itself infiltrating the lung, haemorrhage and heart failure; the rest stay unexplained."),
    ('b', "**Bacterial infection 33%; then viral 13%, Pneumocystis 8%, invasive aspergillosis 7%, disease-related infiltrates 7%, cardiogenic 3%.** Ordinary bacteria still come first even in deep immunosuppression, so empirical antibacterial cover is never omitted. In EFRAIM (1,611 patients, 2017) the order was the same: bacterial 29.5%, viral 15.4%, fungal 14.7%."),
    ('c', "**15% undetermined, and an undetermined cause carries a worse outcome.** If the cause is not found, it is not treated. In EFRAIM an undetermined cause (13.2%) was linked to both intubation and hospital death, which is why the diagnostic work-up (RSC-20d) is part of the treatment."),
    ('d', "**The type and mechanism of immunosuppression, and the nature, phase and duration of treatment.** The defect predicts the organism (RSC-18), and the phase matters: a neutropenic patient in the first weeks of chemotherapy is at risk of different organisms from one on long-term steroids or months after a transplant (RSC-19)."),
  ],
  mimic=[
    ("Infection vs the disease or drug itself", "Infiltrates may be leukaemic or lymphomatous infiltration, drug pneumonitis or haemorrhage; these are found only by looking for them once infection has been sought."),
  ],
  traps=[
    ("“In the immunocompromised, opportunistic organisms are the commonest cause”", "Ordinary bacterial infection is the single commonest cause; Pneumocystis and aspergillosis follow well behind."),
  ],
  decode=[
    ("[pattern] Commonest identified cause of acute respiratory failure in immunocompromised patients?", "Bacterial infection."),
    ("[pattern] Which factor in the work-up is linked to higher mortality?", "Failure to identify the cause."),
  ],
  punch="Bacteria are the commonest cause, the immune defect predicts the rest, and an undetermined cause carries a worse outcome, so finding it matters more than the oxygen device.",
)

L['RSC-18'] = dict(
  sub="Respiratory → Immunocompromised → Immune defect and typical infections",
  step=1,
  intro="Step 1 continues: the kind of immune defect narrows the list of organisms before any test returns. Each defect removes one line of defence, and the organisms that line normally handles take over.",
  parts=[
    ('a', "**Neutrophil defect (acute leukaemia, chemotherapy): Gram-negative and Gram-positive bacteria, Candida, Aspergillus.** Neutrophils kill extracellular bacteria and the hyphae of moulds. Without them, gut and skin bacteria invade within days, and Aspergillus becomes the threat after about 10 days of profound neutropenia. Long-term steroids add to this risk, because they impair neutrophil and macrophage killing too."),
    ('b', "**T-cell defect (steroids, calcineurin inhibitors, lymphoma, transplant): Pneumocystis, CMV and herpes viruses, mycobacteria, Nocardia, Listeria, Legionella, Cryptococcus.** T cells control organisms that live inside cells or that need cell-mediated immunity, so the infections are slower, opportunistic and often reactivations. A patient on long-term prednisone with a lung nodule and a brain lesion has Nocardia (RSC-20)."),
    ('c', "**B-cell or antibody defect (myeloma, CLL, rituximab, asplenia): encapsulated bacteria — pneumococcus, H. influenzae.** A capsule resists phagocytosis unless antibody and complement coat it, and the spleen removes coated bacteria from the blood. Without antibody or spleen, pneumococcal pneumonia and sepsis can be fulminant."),
  ],
  mimic=[
    ("Neutropenia vs T-cell defect", "Neutropenia: acute, bacterial and mould infection within weeks of chemotherapy. T-cell defect: subacute Pneumocystis, viral, mycobacterial and Nocardia infection on steroids or after transplant."),
  ],
  traps=[
    ("“Aspergillus is a T-cell infection”", "Invasive aspergillosis follows neutropenia (and steroids); neutrophils kill hyphae (RSC-29b)."),
    ("“Pneumocystis follows neutropenia”", "Pneumocystis follows loss of T-cell immunity: steroids, transplant, lymphoma, HIV."),
  ],
  decode=[
    ("[pattern] Prolonged neutropenia after induction chemotherapy, new nodules — likely organism?", "Aspergillus."),
    ("[pattern] On rituximab or after splenectomy, fulminant pneumonia — likely organism?", "Pneumococcus (encapsulated bacteria)."),
  ],
  punch="Neutropenia lets in bacteria, Candida and Aspergillus; a T-cell defect lets in Pneumocystis, viruses, mycobacteria and Nocardia; an antibody or spleen defect lets in encapsulated bacteria.",
)

L['RSC-19'] = dict(
  sub="Respiratory → Immunocompromised → Lung complications after stem-cell transplant",
  step=2,
  intro="Step 2 narrows to the patient after a haematopoietic stem-cell transplant (HSCT), the card asked most often in this deck. Immunity returns in a predictable order — neutrophils at engraftment, T cells over months, antibodies last — so the number of days since transplant tells you which infections and which non-infectious syndromes to expect. The questions test the non-infectious syndromes, each defined by its timing and by what the lavage does or does not show.",
  parts=[
    ('a', "**About two-thirds of patients.** Most reviews give 30–60%, depending on the transplant and the era, so two-thirds is at the high end; lung complications account for about half of transplant-related deaths."),
    ('b', "**Pre-engraftment (first month): bacterial, fungal and viral infection; drug toxicity, engraftment syndrome, diffuse alveolar haemorrhage.** The patient is neutropenic, so bacteria and moulds dominate (RSC-18). Engraftment syndrome comes within 96 hours of neutrophil engraftment: by Spitzer's criteria, three major features (fever without infection, an erythematous rash, non-cardiogenic pulmonary oedema with hypoxaemia) or two major plus one minor (weight gain, liver or renal dysfunction, transient encephalopathy). The returning neutrophils release cytokines and make capillaries leak; it responds to steroids. Diffuse alveolar haemorrhage (DAH) is diagnosed at bronchoscopy, when successive lavage aliquots return progressively bloodier; haemoptysis is uncommon despite the name. It affects about 5–12% of recipients, with a median onset that varies by series from about day 11 to day 30, and it carries a high mortality and is treated with high-dose methylprednisolone and correction of platelets and clotting."),
    ('c', "**Early post-engraftment (to day 100): CMV, fungal and Pneumocystis infection; acute GVHD, idiopathic pneumonia syndrome, radiation pneumonitis.** Neutrophils are back but T cells are not, so the T-cell organisms take over. Idiopathic pneumonia syndrome (IPS) is widespread alveolar injury — multilobar infiltrates, symptoms and signs of pneumonia, a raised A–a gradient or new oxygen need — with no active lower respiratory infection and no cardiac failure, acute renal failure or iatrogenic fluid overload to explain it (ATS 2011). It usually appears within the first 120 days, with a median onset of about day 21–65 in different series; donor T cells and TNF-α drive it as well as conditioning toxicity, and mortality is 60–80%, above 95% once ventilated. Treatment is high-dose steroids with antimicrobials continued; etanercept was added on the basis of the TNF-α link, but the adult phase III trial (BMT CTN 0403, 34 patients) closed early for slow accrual and showed no difference in response at day 28 (62.5% with etanercept vs 66.7% with placebo)."),
    ('d', "**Late (after day 100): encapsulated bacteria, fungal and viral infection; bronchiolitis obliterans (chronic GVHD), post-transplant lymphoproliferative disorder.** Antibody and splenic function are the last to recover, so pneumococcus returns. Bronchiolitis obliterans syndrome is the lung form of chronic GVHD: an obstructive defect (FEV₁/FVC <0.7 and FEV₁ <75% predicted) with air trapping on expiratory CT, appearing a median of about a year after transplant."),
  ],
  table=dict(title="The non-infectious syndromes, by what decides them", head=["Syndrome", "When", "What decides it"], rows=[["Engraftment syndrome", "within 96 h of neutrophil recovery", "fever, rash, capillary-leak lung; steroid-responsive"], ["Diffuse alveolar haemorrhage", "first month", "**progressively bloodier lavage aliquots**"], ["Idiopathic pneumonia syndrome", "usually <120 days", "alveolar injury with infection, cardiac, renal and fluid causes **excluded**"], ["Bronchiolitis obliterans", "after day 100", "obstruction and air trapping (chronic GVHD)"]]),
  mimic=[
    ("Engraftment syndrome vs acute GVHD", "Both cause fever and rash and both respond to steroids. Engraftment syndrome comes with neutrophil recovery and brings capillary-leak lung; acute GVHD targets skin, gut and liver, and whether it injures the lung directly is not accepted."),
    ("DAH vs IPS", "Both are diffuse, non-infectious and early. DAH is defined by blood in the lavage; IPS is the diagnosis left when lavage shows neither blood nor organisms."),
  ],
  traps=[
    ("“Rash, fever and lung infiltrates at 4 weeks: acute GVHD of the lung and skin”", "This picture at neutrophil recovery is engraftment syndrome; acute GVHD targets skin, gut and liver, and acute lung GVHD is not an accepted entity. DocT keys GVHD because engraftment syndrome is not offered — the least wrong option, chosen by 59%."),
    ("“DAH is diagnosed by more than 20% haemosiderin-laden macrophages in a lavage taken in the first 24 hours”", "Haemosiderin-laden macrophages take 48–72 hours to appear; the early, defining finding is aliquots that become progressively bloodier."),
    ("“IPS is purely conditioning toxicity, or needs documented lung GVHD”", "Donor T cells and TNF-α contribute, and GVHD is not required; IPS is a diagnosis of exclusion."),
    ("“Stop the antibiotics once the lavage is negative”", "Antimicrobials are continued while steroids start, because a negative lavage does not exclude every infection."),
    ("“Iatrogenic fluid overload is an IPS criterion”", "It is an exclusion: fluid overload, cardiac failure and renal failure must be absent (93% got this right)."),
    ("“DAH is a late complication” (RSC-29c)", "It belongs to the first month."),
  ],
  decode=[
    ("ALL, 4 weeks post-HSCT, fever, maculopapular rash, respiratory distress, lavage negative, perivascular lymphocytes on skin biopsy [DocT, 59% right]", "GVHD of skin and lung as keyed; engraftment syndrome is the better answer whenever it is offered."),
    ("Post-HSCT, sudden dyspnoea and haemoptysis — which lavage finding is most diagnostic of DAH? [DocT GT]", "Successive aliquots that become progressively more blood-stained."),
    ("Day 20, bilateral infiltrates, no cardiac failure, lavage negative for all organisms — true statement about IPS? [DocT GT]", "High-dose steroids with possible etanercept, because TNF-α drives IPS."),
    ("Which is NOT a criterion for IPS? [DocT GT, 93% right]", "Iatrogenic fluid overload (it is an exclusion)."),
  ],
  punch="After stem-cell transplant the day decides the cause: engraftment syndrome and alveolar haemorrhage in the first month, idiopathic pneumonia syndrome before day 100 once infection, heart, kidney and fluid are excluded, and bronchiolitis obliterans after.",
)

L['RSC-20'] = dict(
  sub="Respiratory → Immunocompromised → CT pattern and diagnostic work-up",
  step=3,
  intro="Step 3 turns the clinical picture into a diagnosis. CT narrows the organism by pattern, and the questions pair a pattern with the immune defect and ask for the organism or the test that confirms it.",
  parts=[
    ('a', "**Ground-glass opacities: Pneumocystis, viral (CMV), atypical bacteria.** These organisms fill alveoli with fluid and protein and thicken the interstitium without solid consolidation. Ground glass with interlobular septal thickening (crazy paving) in a patient on steroids, cyclophosphamide or after transplant is Pneumocystis until proven otherwise; it is confirmed by immunofluorescence or PCR on lavage or induced sputum, and a raised serum beta-D-glucan supports it."),
    ('b', "**Nodules with or without cavitation: Aspergillus, mucormycosis, Nocardia, mycobacteria, S. aureus.** Angioinvasive moulds infarct lung around a nodule: a halo of ground glass (haemorrhage) appears early in neutropenia and an air crescent later, as neutrophils return; mucormycosis may show a reversed halo. Nocardia gives nodules or cavities and spreads to the brain, so a lung nodule with a brain lesion in a patient on long-term steroids is Nocardia; the brain is imaged in every case and treatment is high-dose co-trimoxazole (with imipenem or amikacin for brain or severe disease) for 6–12 months, and at least 12 months when the patient is immunosuppressed or the brain is involved."),
    ('c', "**Consolidation: bacterial pneumonia, aspergillosis.** Lobar or segmental consolidation is usually bacterial, the commonest cause overall (RSC-17)."),
    ('d', "**Non-invasive tests first (induced sputum, nasopharyngeal viral PCR, urinary Legionella antigen, serum galactomannan and beta-D-glucan, echo, BNP); bronchoscopy only for diagnostic uncertainty, because it is risky on high oxygen.** Lavage in a hypoxaemic patient can precipitate intubation. Each test answers a specific question: galactomannan for Aspergillus, beta-D-glucan for Pneumocystis and other fungi, echo and BNP for a cardiac cause."),
  ],
  table=dict(title="Pattern to organism", head=["CT", "Think of", "Confirm with"], rows=[["Ground glass, crazy paving", "**Pneumocystis**, CMV", "lavage immunofluorescence or PCR; beta-D-glucan"], ["Nodule with halo or air crescent", "**Aspergillus**", "galactomannan (serum or lavage)"], ["Nodule or cavity + brain lesion, on steroids", "**Nocardia**", "culture; image the brain"], ["Lobar consolidation", "bacteria", "cultures, urinary antigens"]]),
  mimic=[
    ("Pneumocystis vs CMV pneumonitis", "Both cause ground glass after transplant; crazy paving with a high beta-D-glucan favours Pneumocystis, and CMV is shown by PCR or antigen in blood and lavage."),
    ("Nocardia vs tuberculosis", "Both cavitate; a lung lesion with a brain lesion in a steroid-treated patient points to Nocardia."),
  ],
  traps=[
    ("“Sarcoidosis on prednisone, seizure, lung nodule and brain lesion — tuberculosis or sarcoid”", "The lung-and-brain combination on long-term steroids is Nocardia. Only 19% chose it on DocT GT."),
    ("“Ground glass in the immunocompromised: send a serum galactomannan”", "Galactomannan detects Aspergillus, which gives nodules; ground glass and crazy paving call for lavage for Pneumocystis."),
    ("“Crazy paving 4 months after lung transplant is CMV”", "CMV also gives ground glass, but crazy paving is keyed as Pneumocystis (68% right)."),
    ("“Bronchoscopy first in every immunocompromised patient with infiltrates”", "Non-invasive tests come first; lavage on high oxygen can tip the patient into intubation."),
  ],
  decode=[
    ("Systemic sclerosis on cyclophosphamide, insidious dyspnoea, ground glass with septal thickening (crazy paving), antibiotics failed — confirmatory test? [DocT, 71% right]", "Lavage for Pneumocystis immunofluorescence."),
    ("4 months after lung transplant, fever, dry cough, crazy paving on HRCT — organism? [DocT, 68% right]", "Pneumocystis."),
    ("Sarcoidosis on prednisone 10–60 mg for a year, seizure, 2.5 cm lung nodule and 3 cm brain lesion [DocT GT, 19% right]", "Nocardiosis."),
  ],
  punch="Ground glass means Pneumocystis or a virus, nodules mean moulds or Nocardia, and a lung lesion with a brain lesion on steroids means Nocardia; non-invasive tests come before bronchoscopy.",
)

L['RSC-21'] = dict(
  sub="Respiratory → Immunocompromised → NIV and high-flow oxygen: the evidence",
  step=4,
  intro="Step 4 asks how to support the failing lung. Intubation used to carry a very high mortality in these patients, so avoiding it with a mask was attractive; the small early trials supported that, and the larger modern trials did not.",
  parts=[
    ('a', "**Early trials: NIV better than oxygen, but small and with a high control mortality.** Antonelli (2000, 40 solid-organ transplant recipients): intubation 20% vs 70%, ICU mortality 20% vs 50%. Hilbert (2001, 52 patients with infiltrates, fever and hypoxaemia): intubation 46% vs 77%, ICU mortality 38% vs 69%, hospital mortality 50% vs 81%. Control mortality that high reflects an era when intubating these patients was often fatal."),
    ('b', "**Lemiale 2015 (374 patients): NIV vs oxygen, no difference in mortality.** Day-28 mortality was 24.1% with NIV vs 27.3% with oxygen alone; intubation (38.2% vs 44.8%), ICU-acquired infection and length of stay did not differ either. With modern care control mortality had fallen to about a quarter, leaving far less room for NIV to help."),
    ('c', "**HIGH trial 2018 (776 patients): high-flow vs standard oxygen, no difference in mortality.** Day-28 mortality was 35.6% vs 36.1% and intubation 38.7% vs 43.8% (not significant); only oxygenation was better with high flow. Among the 82 immunocompromised patients in FLORALI, a post hoc analysis found intubation in 65% with NIV (alternating with high flow) vs 31% with high flow alone and 43% with standard oxygen; but FLORALI-IM (2022, 299 patients) then found NIV alternating with high flow no better or worse than high flow alone (day-28 mortality 35% vs 36%)."),
    ('d', "**LUNG SAFE: NIV used more often first-line in the immunocompromised (20.9% vs 15.9%), and failed more often.** About half of those given NIV were intubated, and in LUNG SAFE their mortality matched that of patients intubated at once; other cohorts (Azoulay 2014, ARDS in malignancy) found NIV failure linked to higher mortality."),
    ('e', "**A time-limited trial of NIV or high flow in early or mild disease; invasive ventilation with shock, renal failure or high work of breathing.** The risk is a late intubation after hours of large, injurious breaths. ERS/ATS 2017 still says “we suggest early NIV for immunocompromised patients with ARF” (conditional, moderate certainty, weighted by the early trials); ERS 2022 conditionally prefers high flow over NIV in hypoxaemic failure generally."),
  ],
  mimic=[
    ("Where NIV works vs where it fails", "It works where positive pressure reverses the problem: COPD hypercapnia (COPD-10), cardiogenic pulmonary oedema, high-risk extubation. It fails in severe hypoxaemia and in an exacerbation of ILD, where stiff lungs do not recruit."),
  ],
  traps=[
    ("“NIV helps an exacerbation of interstitial lung disease”", "Stiff, non-recruitable lungs make NIV fail in most patients, and it delays intubation; ILD is the condition where NIV is NOT useful [NEET 2025]."),
    ("“Hilbert proved that NIV saves immunocompromised patients”", "Its control mortality of 69–81% belongs to another era; Lemiale (2015) found no difference."),
    ("“The HIGH trial showed lower mortality with high flow” (RSC-29d)", "No difference: 35.6% vs 36.1%."),
    ("“NIV failure was linked to higher mortality in LUNG SAFE”", "In LUNG SAFE mortality after NIV failure matched that of primary intubation; the excess appears in other cohorts."),
  ],
  decode=[
    ("NIV is NOT useful in which: ILD exacerbation, cardiogenic pulmonary oedema, COPD exacerbation, high-risk post-extubation? [NEET 2025]", "ILD exacerbation."),
    ("[pattern] Immunocompromised, hypoxaemic, no shock — what did Lemiale 2015 or HIGH 2018 show?", "No difference in mortality with NIV or high flow."),
  ],
  punch="Early small trials favoured NIV, but Lemiale, HIGH and FLORALI-IM found no mortality benefit from NIV or high flow, so either is a time-limited trial and shock, renal failure or tiring mean intubation.",
)

L['RSC-22'] = dict(
  sub="Respiratory → Immunocompromised → ARDS: ventilation and outcome",
  step=4,
  intro="Step 4 continues once the patient has ARDS. About one in five patients with ARDS in LUNG SAFE was immunocompromised, and their hospital mortality was higher (52.4% vs 36.2%) despite similar severity; the card asks what predicts it.",
  parts=[
    ('a', "**No: the same ARDSNet strategy, and plateau, driving pressure and compliance predict mortality as usual.** In the EFRAIM ARDS analysis (789 patients, hospital mortality 56.3%) higher driving pressure and plateau pressure and lower compliance were each linked to death, and tidal volume was not; the rules of ARDS-19 and ARDS-26 apply unchanged."),
    ('b', "**Vasopressors, renal replacement therapy, ARDS of undetermined cause.** Each raised the odds of death (adjusted odds ratios about 1.9, 2.0 and 1.7 in EFRAIM); organ failure beyond the lung and an untreated cause (RSC-17c) are what kill."),
    ('c', "**Not linked: neutropenia and the type of underlying disease.** Neither neutropenia on admission nor the kind of malignancy or immunosuppression predicted death once organ failures were counted, so neither is a reason to withhold ICU care."),
    ('d', "**ECMO: 6-month survival 30%; worst with haematological malignancy; better with a recently diagnosed immunodeficiency.** In 203 immunocompromised patients given ECMO (Schmidt), cannulation within 30 days of the diagnosis was linked to lower mortality, so ECMO is kept for patients with a realistic prognosis (ARDS-35)."),
  ],
  mimic=[],
  traps=[
    ("“Neutropenia predicts mortality in immunocompromised ARDS” (RSC-29a)", "It was not linked once vasopressors, renal replacement and an undetermined cause were counted."),
  ],
  decode=[
    ("[pattern] Immunocompromised ARDS — which factor is NOT associated with mortality?", "Neutropenia (or the type of underlying disease)."),
  ],
  punch="Immunocompromised ARDS is ventilated as any ARDS, and death follows vasopressors, renal replacement and an undetermined cause, not neutropenia or the type of disease.",
)

L['RSC-23'] = dict(
  sub="Respiratory → Air leak → Bronchopleural fistula",
  step=5,
  intro="Step 5 moves from infection to a mechanical problem: a hole between the airway and the pleura. On a ventilator, gas goes out through the hole rather than into the lung, and the questions test when a leak means an airway injury and when air outside the lung can be watched.",
  parts=[
    ('a', "**A communication between a bronchus and the pleural cavity with a persistent air leak (beyond 24 hours).** In ventilated patients a leak lasting more than 24 hours is the usual threshold; after lung surgery, a prolonged air leak is usually defined as one lasting beyond 5–7 days."),
    ('b', "**Lung resection, trauma, mechanical ventilation, ARDS, spontaneous pneumothorax, radiation or radiofrequency ablation, infection.** Resection leaves a bronchial stump that can break down; necrotising infection and ARDS weaken the lung, and positive pressure forces gas through any weak point."),
    ('c', "**Loss of PEEP and of tidal volume (expired below inspired), hypoxaemia, persistent surgical emphysema or pneumomediastinum, bubbling in the water seal.** The difference between inspired and expired tidal volume measures the leak per breath. After chest trauma a persistent large leak, or a pneumothorax that recurs despite a working drain, means a tracheobronchial injury until bronchoscopy proves otherwise."),
    ('d', "**Mortality 27–50% (other reviews 18–67%).** The 67% comes from an older series in which 39 of 1,700 ventilated patients had a leak beyond 24 hours, ventilated with tidal volumes far larger than today's (about 14 mL/kg); with lung-protective ventilation the figures are lower."),
  ],
  mimic=[
    ("Air leak through the lung vs air outside it", "A fistula leaks into the pleura and bubbles in the drain. Pneumomediastinum and pneumopericardium in ARDS are air tracking along the bronchovascular sheaths (barotrauma, ARDS-18); if the patient is stable they are watched, not drained."),
  ],
  traps=[
    ("“An occult pneumothorax needs a drain, especially on positive-pressure ventilation”", "A stable occult (CT-only) pneumothorax can be observed even on positive pressure (OPTICC)."),
    ("“Every traumatic haemothorax needs a drain and VATS”", "Only a retained collection (more than about 300 mL) after tube drainage needs VATS."),
    ("“Pneumopericardium in ARDS needs pericardiocentesis”", "Without haemodynamic compromise it is observed with serial chest X-rays; drainage is for tamponade."),
  ],
  decode=[
    ("Trauma, right haemopneumothorax with rib fractures, chest drain inserted — true statement? [DocT GT, 65% right]", "A persistent air leak or recurrent pneumothorax should prompt evaluation for tracheobronchial injury."),
    ("ARDS with pneumomediastinum and pneumopericardium, haemodynamically stable — intervention? [Marrow]", "Observe with serial chest X-rays."),
  ],
  punch="A leak lasting beyond 24 hours on the ventilator is a bronchopleural fistula, shown by expired volume below inspired; after trauma it means an airway injury until bronchoscopy says otherwise, while stable air in the mediastinum is watched.",
)

L['RSC-24'] = dict(
  sub="Respiratory → Air leak → Ventilator and drain strategy",
  step=5,
  intro="Step 5 continues with how to ventilate around the hole. Every setting is judged by one question: does it raise or lower the pressure pushing gas through the fistula, and for how long?",
  parts=[
    ('a', "**The transpulmonary pressure gradient (airway minus pleural pressure) and the duration of inspiration.** Flow through the fistula follows the pressure across it and the time that pressure is applied, so peak and mean airway pressure, PEEP and inspiratory time all feed the leak (ARDS-28)."),
    ('b', "**Peak pressure <30; tidal volume 4–6 mL/kg (3–4 for one lung); lowest possible PEEP; short inspiratory time; low rate; permissive hypercapnia; pressure support or spontaneous breathing if tolerated.** Small breaths and a short inspiration shorten the time the gradient is high; low PEEP removes the gradient during expiration; a low rate reduces the number of high-pressure periods per minute. Spontaneous breathing lowers mean airway pressure most, so early weaning is part of the treatment."),
    ('c', "**Avoid negative suction: water seal only. Check the tube’s position and patency; consider an unexpandable lung. Intrapleural pressure can be matched to PEEP.** Suction makes pleural pressure more negative, which widens the gradient and keeps the fistula open. Applying positive pressure to the drain during expiration, equal to PEEP, removes the expiratory gradient."),
  ],
  mimic=[],
  traps=[
    ("“Chest-drain suction helps a bronchopleural fistula heal” (RSC-29e)", "Suction widens the gradient and increases flow through the fistula; water seal only."),
    ("“High PEEP is used with an air leak” (RSC-29f)", "The lowest PEEP that keeps oxygenation acceptable."),
  ],
  decode=[
    ("[pattern] Ventilated patient with a large bronchopleural fistula — which change reduces the leak?", "Lower PEEP, smaller tidal volume, shorter inspiratory time, water seal instead of suction."),
  ],
  punch="Whatever lowers airway pressure, or the time it is applied, lowers the leak: small breaths, short inspiration, minimal PEEP, spontaneous breathing, and a drain on water seal rather than suction.",
)

L['RSC-25'] = dict(
  sub="Respiratory → Air leak → Lung isolation and high-frequency ventilation",
  step=5,
  intro="When the leak is too large for ordinary settings, the healthy lung can be separated from the leaking one, or breaths made so small that little gas escapes. The questions test high-frequency jet ventilation and the bedside check of a double-lumen tube.",
  parts=[
    ('a', "**Double-lumen tube; single-lumen tube with a bronchial blocker; endobronchial blocker (Arndt).** Isolation lets each lung be ventilated separately, or the leaking one rested. The bronchial limb goes into the healthy lung, away from the fistula and any suture line, so that lung is protected from spill and ventilated without pushing gas through the hole. A left-sided tube is the usual default, because the right upper lobe bronchus arises close to the carina and is easily blocked, but a left-sided fistula (such as a left pneumonectomy stump) needs a right-sided tube or a blocker. If a double-lumen tube is thought to have moved, position is checked by bedside fibreoptic bronchoscopy, not by transporting the patient."),
    ('b', "**Synchronous: the same rate to both lungs, with different tidal volume, flow, PEEP and FiO₂. Asynchronous: everything differs, including the mode.** Two ventilators are used; synchronous ventilation links them so both lungs inflate together. Each lung gets settings matched to its own mechanics, so the leaking lung can take small volumes and low PEEP."),
    ('c', "**High-frequency ventilation: tidal volume 2–5 mL/kg at 100–200/min; it raises airway impedance and so lowers fistula flow; weak evidence, selected patients. These are jet-ventilation figures; oscillation runs at 3–15 Hz.** Jet ventilation pulses small jets near the dead-space volume with passive expiration, keeping peak pressure low, so less gas passes through the fistula with each breath. It is not recommended for adult ARDS (OSCAR and OSCILLATE, ARDS-34); its niche is the large leak and airway surgery. VV-ECMO allows ultra-protective ventilation and may let the fistula close."),
  ],
  mimic=[
    ("Jet ventilation vs oscillation", "Jet: small pulses at high rates (the card gives 100–200 a minute; devices and reports vary, and neonatal jets run faster), passive expiration. Oscillation: 3–15 Hz (180–900 a minute), active expiration, high mean airway pressure."),
  ],
  traps=[
    ("“Jet ventilation gives larger tidal volumes, or removes the need for PEEP”", "It gives very small volumes at high rates; minimising lung injury is its theory, not a proven benefit in ARDS (93% right)."),
    ("“Suspected double-lumen tube migration: take the patient for a chest X-ray or CT”", "Confirm at the bedside with a fibreoptic bronchoscope."),
  ],
  decode=[
    ("Severe influenza ARDS, considering high-frequency jet ventilation — primary advantage? [DocT, 93% right]", "Very small tidal volumes at high rates, minimising ventilator-induced lung injury."),
    ("After thoracic surgery, suspected double-lumen tube migration — next step? [Marrow]", "Bedside flexible bronchoscopy."),
  ],
  punch="A large leak is managed by isolating the lungs, ventilating each to its own needs, or making the breaths so small with jet ventilation that little gas escapes, with ECMO as the last step.",
)

L['RSC-26'] = dict(
  sub="Respiratory → Air leak → Bronchoscopic closure",
  step=5,
  intro="If the leak persists and the patient cannot go to surgery, the hole can be plugged from inside the airway. The technique depends on the size and site of the defect.",
  parts=[
    ('a', "**Small defects (<5 mm): occlusive material — fibrin glue, gel foam, tetracycline, autologous blood patch.** A small hole can be sealed directly, or made to scar shut by inflammation."),
    ('b', "**Proximal defects: airway stents, Watanabe spigots, Amplatzer occluder.** A stent covers a hole in the trachea or a main bronchus; an occluder device plugs a larger stump fistula. Watanabe spigots are silicone plugs placed in the bronchus that leads to the leak, and are also used for peripheral leaks."),
    ('c', "**Distal defects: one-way endobronchial valves.** The valve lets air and secretions out during expiration but stops air entering, so the segment beyond collapses and the leak seals. The leaking segment is found by blocking segmental bronchi in turn with a balloon until the bubbling stops; in one series of 40 patients (Travaline 2009) the leak resolved or decreased in about 93%."),
  ],
  mimic=[],
  traps=[
    ("“One-way valves are for proximal stump defects”", "Valves are for distal leaks; proximal defects need stents or occluders (RSC-29g)."),
  ],
  decode=[
    ("[pattern] Persistent distal air leak in a patient unfit for surgery — bronchoscopic option?", "One-way endobronchial valves."),
  ],
  punch="Small holes are glued, proximal defects are stented or occluded, and distal leaks are closed with one-way valves that collapse the segment beyond.",
)

L['RSC-27'] = dict(
  sub="Respiratory → Lung donor → Why so few donor lungs",
  step=6,
  intro="The last step is the brain-dead patient whose lungs could save someone else. The lung is the organ most often lost during donor care, because brain death and the ICU stay injure it before retrieval.",
  parts=[
    ('a', "**Only 15–25% of donors yield lungs.** Far fewer than kidneys or liver, because the lungs are exposed to aspiration, infection and ventilator injury as well as the effects of brain death. The usual ideal criterion is a PaO₂ above 300 mmHg on FiO₂ 1.0 and PEEP 5 cmH₂O, though no firm lower limit has been defined."),
    ('b', "**Sympathetic storm (neurogenic pulmonary oedema, inflammation), then atelectasis, aspiration, trauma, ventilator-associated pneumonia and VILI.** As the brainstem herniates a catecholamine surge raises systemic and left atrial pressure, forcing fluid into the lung and damaging capillaries; brain death then releases inflammatory mediators that injure the lung further. The ICU adds collapse, infection and ventilator injury."),
    ('c', "**Extended donor criteria; ex vivo lung perfusion; optimised donor management.** Ex vivo perfusion ventilates and perfuses retrieved lungs outside the body, so marginal lungs can be assessed and improved before transplant. Donor management is the part the ICU controls (RSC-28)."),
  ],
  mimic=[],
  traps=[
    ("“Donor lungs are lost mainly to the original trauma”", "Most are lost to brain-death injury and to what happens in the ICU, much of which can be prevented."),
  ],
  decode=[
    ("[pattern] What share of brain-dead donors yield transplantable lungs?", "About 15–25%."),
  ],
  punch="Only 15–25% of donors yield lungs, because the sympathetic storm and then collapse, aspiration, infection and ventilator injury damage them; better donor care and ex vivo perfusion recover more.",
)

L['RSC-28'] = dict(
  sub="Respiratory → Lung donor → Ventilating the donor",
  step=6,
  intro="Step 6 continues with what the ICU can change. The donor’s lungs are injured lungs, so the same protective principles apply, with the apnoea test as an extra hazard.",
  parts=[
    ('a', "**Volume control; tidal volume 6–8 mL/kg PBW; rate 8–16; PEEP 5–10; FiO₂ 100% then down to 40%.** Protective volumes limit stretch, PEEP prevents collapse, and FiO₂ is lowered to avoid absorption atelectasis and oxygen toxicity."),
    ('b', "**PaCO₂ 35–45 mmHg; peak pressure <30.** Normocapnia avoids acidosis in a circulation that is already unstable; protective-ventilation protocols usually state the 30 cmH₂O limit as a plateau pressure."),
    ('c', "**Protective ventilation (tidal volume ≤8 and PEEP ≥8) raised the odds of lung procurement (odds ratio 1.43).** In a French national cohort of 1,626 brain-dead donors (2020) recipients’ 1-year survival did not differ (82.7% vs 82.3%). In Mascia’s trial (JAMA 2010, 118 donors) tidal volume 6–8 mL/kg PBW, PEEP 8–10, an apnoea test on CPAP and closed suction, compared with 10–12 mL/kg and PEEP 3–5, raised the share of donors with eligible lungs from 54% to 95% and lungs harvested from 27% to 54%, with similar 6-month recipient survival (69% vs 75%)."),
    ('d', "**Closed suction, positioning, VAP bundle. Kidneys want fluid; lungs want restriction.** Disconnection for an apnoea test or open suction collapses the lung; a recruitment manoeuvre after the apnoea test reversed the fall in P/F in a small study. Fluid is given to a euvolaemic target rather than liberally, because the lung leaks."),
  ],
  mimic=[],
  traps=[
    ("“The apnoea test is done disconnected from the ventilator”", "Disconnection collapses the lung; Mascia used CPAP during the test, then re-recruited."),
  ],
  decode=[
    ("[pattern] Brain-dead donor — which ventilation strategy increased lungs harvested?", "Tidal volume 6–8 mL/kg PBW, PEEP 8–10, apnoea test on CPAP, closed suction (Mascia 2010)."),
  ],
  punch="Ventilate the donor as an injured lung: 6–8 mL/kg PBW, PEEP 8–10, apnoea test on CPAP, closed suction; in Mascia’s trial this doubled the lungs harvested.",
)

L['RSC-29'] = dict(
  sub="Respiratory → Immunocompromised, air leak and donor → Revision: true or false",
  step=6,
  intro="A sweep through the deck. Each statement turns on one detail from an earlier card.",
  parts=[
    ('a', "**False — neutropenia is not linked to mortality** in immunocompromised ARDS (RSC-22c)."),
    ('b', "**True — with Candida and bacteria** (RSC-18a)."),
    ('c', "**False — diffuse alveolar haemorrhage comes in the first 30 days** (RSC-19b)."),
    ('d', "**False — no difference in mortality** with high flow vs standard oxygen (RSC-21c)."),
    ('e', "**False — water seal only;** suction widens the gradient through the fistula (RSC-24c)."),
    ('f', "**False — the lowest possible PEEP** (RSC-24b)."),
    ('g', "**True — one-way valves close distal defects** (RSC-26c)."),
  ],
  mimic=[],
  traps=[
    ("“Settings that protect the ARDS lung also suit a fistula”", "Protective volumes do, but the higher PEEP of ARDS feeds the leak; with a fistula PEEP is kept as low as possible."),
  ],
  decode=[
    ("[pattern] True/false on immunocompromised failure and air leak", "Neutropenia not predictive, Aspergillus after neutropenia, DAH early, HIGH no difference, no suction, low PEEP, valves distal."),
  ],
  punch="In the immunocompromised the cause and organ failures decide outcome, not neutropenia or the oxygen device; with a fistula, everything that lowers airway and pleural pressure gradients lowers the leak.",
)

FLAGS = {}
FLAGS['RSC-19'] = "Watch gives DAH ‘median day 11’ (and RSC-29c ‘first 30 days’), the classic teaching; later series differ — a review gives median day 19 (range 5–34) and a large cohort (Keklik, Haematologica 2018: 5% of 1,228 allogeneic recipients) median day 30 (range 3–168). Card a’s ‘two-thirds’ is above the 30–60% most reviews give. Card c lists acute GVHD as an early lung complication; acute lung GVHD is not an accepted entity (acute GVHD targets skin, gut and liver). Also: DocT’s 4-week rash + lung key (‘GVHD of lung and skin’) is least wrong; engraftment syndrome, not on the card, fits better. Consider adding ‘engraftment syndrome: within 96 h of neutrophil recovery, fever, rash, capillary-leak lung’ to the card."
FLAGS['RSC-21'] = "Not an error but incomplete: FLORALI-IM (Lancet Respir Med 2022, 299 patients) found NIV alternating with high flow no better than high flow alone (day-28 mortality 35% vs 36%), and ERS 2022 conditionally prefers high flow over NIV in hypoxaemic failure. Consider adding. Watch’s LUNG SAFE point is verified (mortality after NIV failure matched primary intubation)."
FLAGS['RSC-26'] = "Card b lists Watanabe spigots under proximal defects; they are segmental silicone plugs used mostly, like valves, for peripheral (distal) leaks. Explanation notes both uses."
FLAGS['RSC-25'] = "Card a gives no rule for the side of a double-lumen tube; with a fistula the bronchial limb goes to the healthy lung, so a left-sided fistula needs a right-sided tube or blocker (the Marrow note ‘left DLT has wider safety margin’ is the elective default only). Card c’s jet figures (2–5 mL/kg at 100–200/min) could not be confirmed against a single source; devices and reports vary. Explanation notes both."
FLAGS['RSC-28'] = "Card b says ‘peak pressure <30’; donor protocols, like ARDS rules, usually set the 30 cmH₂O limit on plateau pressure. Minor; explanation notes it."
