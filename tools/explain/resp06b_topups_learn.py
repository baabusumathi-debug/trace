# RESP06B top-up cards — Explain v3 ("Learn" depth), same fields and voice as resp06b_learn.py.
# Fields: sub, step (index into resp06b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions: Recall25:Q16 (NEET 2025 recall, rifampicin then warfarin, death from PE) with Marrow QB11-Q03 (same concept, linked to PE-20);
# Marrow QB24-Q02 (post-op femur fracture: dyspnoea, confusion, axillary and conjunctival petechiae → fat embolism syndrome) with Marrow QB59-Q01/Q11 (which is not a major Gurd criterion → retinal changes).
# Checked online 11 Nov 2026: rifampicin lowers rivaroxaban AUC about 50%; Gurd criteria (major and minor lists, 1 major + 4 minor rule), 24–72 h onset, petechial distribution, mechanical and biochemical theories, supportive care, early fixation, steroids not effective as treatment (LITFL).
# Second check 11 Nov 2026 (see resp06b_review.md): rifampicin–warfarin time course and dose multiple (Eur J Clin Pharmacol case series), dabigatran AUC −66% and apixaban AUC −54% with rifampicin, Gurd rule forms (LITFL, WikEM; Insights Imaging 2021), steroid prophylaxis meta-analysis (Bederman 2009).
T = {}

T['T_51989536'] = dict(
  sub="Respiratory → Pulmonary embolism → Rifampicin and anticoagulants",
  step=3,
  intro="Step 3 says every PE patient is anticoagulated, and the drug only works at the right level. Rifampicin is the strongest common inducer of drug metabolism, and a patient on TB treatment who is started on warfarin can stay unprotected for days while looking treated. The NEET 2025 recall and a Marrow question both give the death and ask why.",
  parts=[
    ('a', "**Rifampicin is a potent CYP2C9/3A4 (and P-gp) inducer: warfarin is cleared fast, the INR stays sub-therapeutic and the clot propagates.** Rifampicin switches on the genes for these enzymes through the nuclear pregnane X receptor, so the effect starts within days and keeps building for weeks (the warfarin requirement reaches its plateau at about 4 weeks), then fades over about 4 weeks after rifampicin is stopped. The more potent S-warfarin is cleared mainly by CYP2C9. The usual loading dose then never reaches an INR of 2–3, and if heparin is stopped on schedule after 5 days the patient is left with almost no anticoagulation."),
    ('b', "**Needs 2–3 times the warfarin dose with close INR checks, or a parenteral agent (LMWH).** In one case series the median requirement rose about 2.6-fold, and some patients need more. The danger repeats in reverse: when rifampicin stops, enzyme levels fall over weeks and the same high dose overshoots, so the INR must be followed down as well. LMWH and fondaparinux are not metabolised by the liver and are unaffected, which makes them the simplest choice during TB treatment."),
    ('c', "**DOACs interact too (levels fall) — avoid them with rifampicin.** Rivaroxaban and apixaban are cleared partly by CYP3A4 and P-gp, edoxaban mainly through P-gp, and dabigatran is a P-gp substrate; rifampicin lowers rivaroxaban exposure by about half, apixaban by about 54% and dabigatran by about 66%. With no routine level to monitor, the labels say to avoid combining them with strong inducers."),
  ],
  mimic=[
    ("Inducers vs inhibitors with warfarin", "Rifampicin, carbamazepine, phenytoin and St John’s wort lower the INR (clot); amiodarone, fluconazole, metronidazole and co-trimoxazole raise it (bleed)."),
  ],
  traps=[
    ("“He died because the PE was too large for anticoagulation” or “warfarin is prothrombotic at the start”", "The early protein C dip is real, but it is covered by the heparin overlap; the question’s point is that rifampicin kept the INR low, so he was never anticoagulated."),
    ("“Switch to a DOAC to avoid the interaction”", "DOAC levels fall with rifampicin as well; use LMWH, or warfarin at a much higher dose with close INR checks."),
  ],
  decode=[
    ("TB patient on rifampicin starts warfarin for DVT and dies of PE on day 7 — why? [NEET 2025 recall]", "Rifampicin enzyme induction kept warfarin levels and the INR sub-therapeutic."),
    ("TB on rifampin, then warfarin, dies of PE — trigger? [Marrow]", "Rifampin (CYP induction lowers warfarin)."),
  ],
  punch="Rifampicin induces CYP2C9, CYP3A4 and P-gp, so warfarin and the DOACs fall to useless levels; give LMWH, or warfarin at 2–3 times the dose with close INR checks, and never assume a normal loading dose is working.",
)

T['T_cc286408'] = dict(
  sub="Respiratory → Embolism → Fat embolism syndrome",
  step=6,
  intro="Step 6 closes with the embolus that is not a clot. After a long-bone or pelvic fracture, marrow fat enters torn veins and lodges in the lung, and in some patients passes on to the brain and skin. It looks like PE on day 2 after a fracture, but it is diagnosed clinically and treated by support alone. The Marrow questions test the clinical picture and which features are major Gurd criteria.",
  parts=[
    ('a', "**24–72 h after long-bone or pelvic fracture: hypoxaemia, confusion, petechiae (axillae, conjunctivae).** Respiratory failure usually comes first and the rash last. Two mechanisms combine: fat globules block small vessels (mechanical), and lipase breaks the fat into free fatty acids that injure the capillary endothelium (biochemical), which explains the delay of a day or more and the ARDS-like lung. Fat passes to the systemic circulation through a patent foramen ovale or through the lung capillaries, causing confusion and petechiae; the petechiae lie on the upper body because fat floats to the non-dependent branches of the aortic arch. They are often absent and fade within days."),
    ('b', "**Gurd major: petechial rash, respiratory insufficiency (PaO₂ <60), CNS depression; diagnosis is ≥2 major, or 1 major + ≥4 minor (tachycardia, fever, retinal fat, fat in urine, falling platelets or haemoglobin, high ESR).** Retinal changes, jaundice and renal changes are minor criteria, not major ones, which is what the Marrow ‘all except’ questions turn on. The form most often quoted (LITFL, WikEM) is at least one major plus four minor criteria; many reviews also accept two major criteria, as the card does. No test confirms the diagnosis: fat in urine or sputum is non-specific, and MRI of the brain may show a ‘starfield’ of small diffusion lesions."),
    ('c', "**Prevention: early fracture fixation; treatment is supportive (oxygen, lung-protective ventilation); steroids are not recommended.** Fixing the fracture early, ideally within 24 hours, stops repeated release of marrow fat. Support means oxygen, ventilation as for ARDS and avoiding hypovolaemia; most patients recover fully if hypoxic brain injury is avoided. Prophylactic steroids reduced FES in a meta-analysis of small, poor-quality trials (Bederman 2009: six trials, 389 patients, no effect on mortality), so they are not routinely recommended, and they are considered ineffective as treatment of established FES."),
  ],
  mimic=[
    ("Fat embolism vs thrombotic PE after a fracture", "Both cause hypoxia within days; FES adds confusion and petechiae, typically at 24–72 h, while CTPA is usually clear. PE comes from a DVT, is usually later, and shows a filling defect."),
    ("Fat embolism vs head injury after trauma", "Both cause confusion; in FES the patient was lucid after the injury and deteriorates at 24–72 h, with hypoxia and petechiae and a CT head without a bleed."),
  ],
  traps=[
    ("“Retinal changes are a major Gurd criterion”", "They are minor; the three major ones are petechial rash, respiratory insufficiency and cerebral involvement."),
    ("“Treat fat embolism with heparin or steroids”", "Treatment is supportive; heparin raises free fatty acids and bleeding risk, and steroids are not recommended."),
  ],
  decode=[
    ("After femur fracture surgery: dyspnoea, confusion, axillary and conjunctival petechiae — diagnosis? [Marrow]", "Fat embolism syndrome."),
    ("Major (Gurd) criteria for fat embolism syndrome — all except? [Marrow]", "Retinal changes (a minor criterion)."),
  ],
  punch="Hypoxaemia, confusion and upper-body petechiae 24–72 h after a long-bone fracture are fat embolism syndrome: the Gurd major criteria are respiratory failure, cerebral signs and rash, and care is early fixation and support, not steroids.",
)

FLAGS = {}

