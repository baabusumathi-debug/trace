# RESP07B top-up cards — Explain v3 ("Learn" depth), same fields and voice as resp07b_learn.py.
# Fields: sub, step (index into resp07b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from map/out/all_rows.json and the DocT GT/QBank files (the top-up's own src) plus qpack/RESP07B.md.
# Checked online 11 Nov 2026: lung abscess — antibiotics alone succeed in about two-thirds, invasive drainage considered after 7–14 days without improvement, abscesses ≥6 cm respond less well
# (≥8 cm suggested for early drainage), percutaneous drainage best for peripheral abscesses (major complications ~8%, mainly pneumothorax, risk highest when the catheter crosses normal lung),
# surgery after failed drainage, for bronchopleural fistula, empyema or uncontrolled haemoptysis (mortality up to ~11%).
# Second check (11 Nov 2026): lung abscess 3–6 weeks (sometimes longer) with a β-lactam/β-lactamase inhibitor or clindamycin, stopped by clinical and imaging response; amoebic empyema from rupture of a liver
# abscess through the diaphragm, metronidazole the key drug; BTS 2023: 25–50 mL for cytology, image-guided taps, blind biopsy not done; cytology ~60% on first sample, a second sample adds some yield.
# Still standard teaching only: lung isolation with a double-lumen tube, luminal agents and left-lobe drainage for amoebic abscess.
T = {}

T['T_39c583be'] = dict(
  sub="Respiratory → Pleura and lung → Lung abscess failing antibiotics",
  step=5,
  intro="Step 5 is about infection in and around the pleura, and a lung abscess is the infected cavity just inside it. Most close with antibiotics because they drain through the bronchus; the Marrow question gives an abscess that is growing while the patient stays septic despite antibiotics and asks for the next step.",
  parts=[
    ('a', "**Most resolve with 3–6 weeks of antibiotics covering aspiration flora (a β-lactam/β-lactamase inhibitor or clindamycin) plus postural drainage.** The usual abscess follows aspiration, so the organisms are mouth anaerobes and streptococci, and the cavity empties through its own airway; positioning helps it drain. Antibiotics alone succeed in about two-thirds, fever usually settles within days, and treatment continues until the cavity has closed or left a small stable scar on imaging."),
    ('b', "**Percutaneous (CT- or ultrasound-guided) drainage if the abscess is expanding, sepsis persists, it is very large (>6–8 cm), it is under tension, the patient fails to wean, or pus spills into the other lung.** An abscess that is not improving after 7–14 days of antibiotics, or one 6 cm or larger, is less likely to close alone. A catheter drains best a peripheral abscess abutting the pleura, where it need not cross normal lung; crossing normal lung is the main risk factor for complications (pneumothorax, empyema, bronchopleural fistula). A central abscess with an airway connection can be drained endoscopically instead."),
    ('c', "**Surgery for failed drainage, massive haemoptysis or suspected cancer; isolate the lungs with a double-lumen tube.** Resection is a last resort because its mortality is substantial; it is also indicated for a bronchopleural fistula or empyema. At induction pus or blood can pour from the abscess into the healthy lung, so the anaesthetist isolates the lungs with a double-lumen tube (or a bronchial blocker) and keeps the diseased side down until it is controlled."),
  ],
  mimic=[
    ("Lung abscess vs empyema on CT", "Abscess: round, thick irregular wall, acute angle with the chest wall, vessels end at the wall. Empyema: lenticular, compresses lung, obtuse angle, split pleura sign. Drain an empyema with a chest tube; most abscesses need only antibiotics."),
    ("Lung abscess vs cavitating cancer", "Cancer: older smoker, thick nodular wall, no response to antibiotics; bronchoscopy or biopsy."),
  ],
  traps=[
    ("“Surgical resection” as the next step for an expanding abscess with sepsis", "Percutaneous drainage comes first; surgery is for failed drainage, haemoptysis or cancer."),
    ("“Continue the same antibiotics longer”", "An abscess that is expanding with ongoing sepsis has failed medical treatment and needs drainage."),
  ],
  decode=[
    ("Expanding lung abscess, worsening sepsis on antibiotics — next step? [Marrow]", "Percutaneous drainage."),
    ("[pattern] Lung abscess needing resection — airway plan?", "Double-lumen tube to protect the other lung."),
  ],
  punch="A lung abscess usually closes with weeks of anaerobic cover because it drains through its bronchus; drain it percutaneously when it grows, stays septic or is very large, and resect only when drainage fails, behind a double-lumen tube.",
)

T['T_7ad33eb9'] = dict(
  sub="Respiratory → Pleura → Amoebic empyema",
  step=5,
  intro="Step 5 includes an infected pleural space that starts below the diaphragm. An amoebic liver abscess sits mostly in the right lobe, high under the dome, so it can burst through the diaphragm into the right pleura. The Marrow question gives the giveaway fluid and asks for the treatment.",
  parts=[
    ('a', "**Amoebic liver abscess ruptured into the pleura (amoebic empyema).** Right pleural effusion, right upper quadrant tenderness, often fever and a large tender liver, and aspirated fluid that is thick and chocolate-brown (‘anchovy sauce’): liquefied liver, not true pus, and often without visible amoebae. Serology for Entamoeba histolytica supports it. A smaller sympathetic effusion, without rupture, is commoner and needs no drainage."),
    ('b', "**Chest-tube drainage plus metronidazole, then a luminal agent (paromomycin or diloxanide); drain the liver abscess if large or in the left lobe.** Metronidazole kills tissue trophozoites but leaves cysts in the bowel, so a luminal agent follows to prevent relapse. Once the abscess has ruptured into the pleura, the space is full of thick material that drugs alone will not clear, so it is drained like any empyema. A left-lobe abscess is drained because it can rupture into the pericardium."),
    ('c', "**An uncomplicated amoebic liver abscess usually needs metronidazole alone.** Unlike a pyogenic abscess, the amoebic one responds to drugs; aspiration is kept for a large abscess at risk of rupture, a left-lobe abscess, or no response in a few days."),
  ],
  mimic=[
    ("Amoebic vs pyogenic empyema", "Amoebic: anchovy-sauce fluid from a ruptured liver abscess, sterile on routine culture, right side, metronidazole. Pyogenic: pus with bacteria, low pH and glucose, from pneumonia, broad antibiotics."),
  ],
  traps=[
    ("“Metronidazole alone” for an amoebic abscess that has burst into the pleura", "Rupture into the pleura needs a chest tube as well as drugs."),
  ],
  decode=[
    ("Right effusion with chocolate-brown fluid and RUQ tenderness — next step? [Marrow]", "Chest tube drainage plus drug therapy (metronidazole, then a luminal agent)."),
  ],
  punch="Anchovy-sauce fluid in a right effusion with a tender liver is an amoebic abscess that has burst into the pleura: drain the chest and give metronidazole, then a luminal agent, whereas an intact amoebic abscess usually needs drugs alone.",
)

T['T_67b32ead'] = dict(
  sub="Respiratory → Pleura → Work-up of a pleural effusion",
  step=3,
  intro="Steps 2 and 3 in order: find the fluid, then tap it and decide whether it is a transudate or an exudate. The DocT question shows an effusion and asks which test is NOT part of the routine work-up (71% right).",
  parts=[
    ('a', "**Imaging: chest X-ray (blunted angles), ultrasound (most sensitive, guides the tap), contrast CT (pleural thickening, malignancy).** The film raises the question (PLEU-15), ultrasound confirms it, shows septations and makes the tap safe (BTS 2023: image-guide every tap), and contrast CT, ideally before the fluid is fully drained, shows the pleura, the lung and the mediastinum (PLEU-16)."),
    ('b', "**Diagnostic thoracocentesis: Light’s criteria, cells, culture, cytology, pH and glucose.** Light’s criteria sort transudate from exudate (PLEU-17); the chemistry and cells point to the cause of an exudate (PLEU-19, 20). Send fluid in blood-culture bottles as well as a plain pot when infection is suspected, 25–50 mL for cytology (BTS 2023; less lowers sensitivity), and the pH in a blood-gas analyser. ADA belongs in the panel in India."),
    ('c', "**Undiagnosed exudate after 2 taps → thoracoscopy with pleural biopsy.** Cytology finds malignancy in only about 60% from the first sample, a second sample adds some yield, and repeating it further adds little (BTS 2023: a negative result warrants further investigation); tuberculosis is often missed by fluid culture. A biopsy under direct vision (or image-guided) diagnoses both, and thoracoscopy allows talc poudrage at the same sitting (PLEU-23)."),
    ('d', "**Bronchoscopy is NOT routine; only for an endobronchial lesion, haemoptysis or suspected collapse.** Bronchoscopy sees the airways, not the pleura, so it adds little to an isolated effusion. It earns its place when there are signs of an airway tumour: haemoptysis, a mass on CT, or a collapsed lobe with the mediastinum pulled towards the effusion rather than pushed away."),
  ],
  mimic=[
    ("Thoracoscopy vs bronchoscopy in an undiagnosed exudate", "Thoracoscopy sees and biopsies the pleura; bronchoscopy sees the airways and is kept for haemoptysis, collapse or a central mass."),
  ],
  traps=[
    ("“Bronchoscopy for every undiagnosed effusion”", "Not routine; it is the test DocT keys as not part of the work-up."),
    ("“Keep tapping for cytology”", "After two negative samples, move to biopsy."),
  ],
  decode=[
    ("Effusion on the image — which is NOT part of the diagnostic work-up? [DocT GT]", "Bronchoscopy (71%)."),
    ("[pattern] Exudate, two negative cytology samples — next?", "Thoracoscopy with pleural biopsy."),
  ],
  punch="Work up an effusion by imaging, an ultrasound-guided tap read with Light’s criteria and chemistry, and thoracoscopic biopsy if two taps fail; bronchoscopy is only for haemoptysis, collapse or an airway lesion.",
)

FLAGS = {}
FLAGS['T_39c583be'] = "Card is consistent with current reviews (checked: 3–6 weeks, sometimes 8 or more, of a β-lactam/β-lactamase inhibitor or clindamycin; invasive drainage after 7–14 days without improvement or for abscesses ≥6 cm). No disagreement."
