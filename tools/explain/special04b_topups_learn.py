# SPECIAL04B top-up cards — Explain v3 ("Learn" depth), same fields and voice as special04b_learn.py.
# Fields: sub, step (index into special04b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source questions (the top-up's own src): DocT GT CGT2 Q137 and Q138 (polymyxin vs daptomycin mechanism; full stems not found in map/out), DocT GT2o Q147 (which antibiotic needs dose
# adjustment in stage 5 CKD — keyed cefazolin, 24% right), DocT GT6 Q12 (aminoglycoside nephrotoxicity; full stem not found).
# Checked 13 Nov 2026 (review): nephrotoxicity incidence 'up to 10–25%' (StatPearls); daptomycin CK weekly and 48-hourly at CrCl <30 per label. From standard references without a fresh check (confident): polymyxins bind lipid A and displace Ca²⁺/Mg²⁺ from LPS; daptomycin calcium-dependent membrane insertion, inactivated by
# pulmonary surfactant, CK monitoring; aminoglycoside uptake by megalin in the proximal tubule, non-oliguric AKI after 5–7 days in roughly 10–25%, saturable uptake favouring once-daily dosing,
# magnesium and potassium wasting. Renal-adjustment lists checked against standard references; nafcillin/oxacillin, ceftriaxone, linezolid, moxifloxacin, doxycycline, clindamycin,
# metronidazole, rifampicin, tigecycline and azithromycin need no renal change.
T = {}

T['T_c2609f9d'] = dict(
  sub="Pharmacology → Antibacterials → Membrane-active antibiotics: polymyxins vs daptomycin",
  step=4,
  intro="Step 4 covered the polymyxins as concentration-dependent killers; this top-up sets them beside daptomycin, the other antibiotic that kills by attacking a bacterial membrane rather than the cell wall. Two DocT GT questions ask what each binds and what each cannot be used for.",
  parts=[
    ('a', "**Polymyxin B/colistin: cationic detergent binds lipid A of LPS → disrupts Gram-negative outer and inner membranes → rapid concentration-dependent killing (CRAB, CRE, DTR-Pseudomonas); nephro- and neurotoxic.** The positively charged polymyxin displaces the calcium and magnesium that hold lipopolysaccharide together, so the outer membrane becomes leaky, and the drug then breaks the inner membrane like a detergent. Gram-positives have no LPS, so they are untouched. The same membrane action on proximal tubular cells and nerve endings causes the toxicity (PK-17)."),
    ('b', "**Daptomycin: calcium-dependent lipopeptide inserts into the Gram-positive membrane → rapid depolarisation → DNA/RNA/protein synthesis stop, no cell-wall action (MRSA bacteraemia, VRE).** With calcium it forms complexes in the cytoplasmic membrane that leak potassium, so the cell depolarises and dies quickly without lysing. Gram-negatives are protected by their outer membrane. It is concentration-dependent, dosed at 6 mg/kg or 8–12 mg/kg once daily (PK-19 h)."),
    ('c', "**Daptomycin catch: inactivated by surfactant (useless in pneumonia); CK monitoring (myopathy).** Pulmonary surfactant is itself a lipid layer that binds and inactivates daptomycin in the alveoli, so it fails in pneumonia even though it is active in the blood (it is still used for septic emboli to the lung from right-sided endocarditis). It causes myopathy and rhabdomyolysis, so creatine kinase is checked weekly and statins are often paused; it can also cause eosinophilic pneumonia."),
    ('d', "**Contrast: vancomycin and β-lactams act on the cell wall.** Vancomycin binds the D-Ala-D-Ala end of peptidoglycan precursors and β-lactams block the penicillin-binding proteins, so both stop wall synthesis and kill slowly; this wall damage is also what lets aminoglycosides in (PK-15 c)."),
  ],
  mimic=[
    ("Polymyxin vs daptomycin", "Both attack membranes and are concentration-dependent. Polymyxin: Gram-negative, binds lipid A, kidney and nerve toxicity. Daptomycin: Gram-positive, needs calcium, muscle toxicity, fails in the lung."),
  ],
  traps=[
    ("“Daptomycin for MRSA pneumonia”", "Surfactant inactivates it; use linezolid or vancomycin."),
    ("“Daptomycin inhibits cell-wall synthesis”", "It depolarises the membrane; vancomycin and β-lactams are the wall drugs."),
    ("“Polymyxins act on Gram-positive organisms”", "They need lipid A, which only Gram-negatives have."),
  ],
  decode=[
    ("Mechanism of polymyxin B / of daptomycin? [DocT GT]", "Polymyxin: binds lipid A and disrupts the Gram-negative membranes. Daptomycin: calcium-dependent membrane depolarisation."),
    ("Daptomycin for VRE, myalgia on day 7 — which test? [pattern]", "Creatine kinase."),
  ],
  punch="Polymyxins break Gram-negative membranes through lipid A and hurt kidneys and nerves; daptomycin depolarises Gram-positive membranes with calcium, hurts muscle and is switched off by surfactant, so never for pneumonia.",
)

T['T_5ceb5d71'] = dict(
  sub="Pharmacology → Antibacterials → Antibiotics needing no renal adjustment",
  step=1,
  intro="Step 1 said that renal failure changes only the maintenance dose; this top-up asks which drugs escape even that, because they leave the body by the liver or bile. The DocT GT question asked which drug needs adjustment in stage 5 CKD, and only 24% chose cefazolin, so the renally cleared ‘simple’ drugs are the ones people miss.",
  parts=[
    ('a', "**No change: ceftriaxone, linezolid, moxifloxacin, azithromycin, doxycycline, clindamycin, metronidazole, rifampicin, tigecycline, nafcillin/oxacillin.** These are cleared by the liver or bile, so their exposure does not rise as GFR falls. Ceftriaxone is the cephalosporin with dual biliary and renal excretion; nafcillin and oxacillin are the antistaphylococcal penicillins cleared by the liver; linezolid and moxifloxacin keep their usual doses (PK-18 d, PK-15 b)."),
    ('b', "**Adjust maintenance dose/interval (never the load): cefazolin, cefepime, ceftazidime, pip-tazo, carbapenems, aminoglycosides, vancomycin, levo/ciprofloxacin, co-trimoxazole, fluconazole, aciclovir.** These are filtered or secreted unchanged, so their half-life lengthens as GFR falls; cefepime causes encephalopathy, aciclovir crystal nephropathy and neurotoxicity, and fluconazole’s maintenance is halved below a CrCl of 50. The first dose stays full because it fills the Vd (step 1)."),
  ],
  mimic=[
    ("Cefazolin vs ceftriaxone", "Cefazolin: renal, reduce in CKD 5 (given after dialysis). Ceftriaxone: biliary and renal, no change."),
    ("Levofloxacin vs moxifloxacin", "Levofloxacin: renal, reduce. Moxifloxacin: hepatic, no change."),
  ],
  traps=[
    ("Missing cefazolin as the drug that needs adjustment in stage 5 CKD (24% right)", "Cefazolin is almost entirely renally excreted; the distractors (ceftriaxone, linezolid, doxycycline and the like) are non-renal."),
    ("“Reduce the loading dose in renal failure”", "Only maintenance changes; the load depends on Vd."),
  ],
  decode=[
    ("Which antibiotic requires dose adjustment in a stage 5 CKD patient? [DocT GT]", "Cefazolin."),
    ("[pattern] Which needs no renal adjustment: ceftriaxone, cefepime, levofloxacin, vancomycin?", "Ceftriaxone."),
  ],
  punch="Drugs leaving by liver or bile keep their dose in renal failure — ceftriaxone, linezolid, moxifloxacin, doxycycline, clindamycin, oxacillin; renally cleared ones such as cefazolin and cefepime have their maintenance cut, never their load.",
)

T['T_29b5a652'] = dict(
  sub="Pharmacology → Antibacterials → Aminoglycoside nephrotoxicity",
  step=4,
  intro="Step 4 explained why aminoglycosides are given as one big daily dose; this top-up is the toxicity that rule is built to limit. The DocT GT question asks for its mechanism and pattern, which differ from most drug-induced AKI.",
  parts=[
    ('a', "**Freely filtered, taken up by proximal tubule (megalin) and stored in the renal cortex.** The cationic aminoglycoside binds megalin on the brush border, is taken into lysosomes and builds up, eventually injuring the cell. The uptake is saturable, so a single high peak loads the cortex no more than several smaller doses, while a long low trough keeps uptake going; this is the reason once-daily dosing is less nephrotoxic."),
    ('b', "**AKI after 5–7 days, NON-oliguric, in 10–30% of courses even with therapeutic levels.** Because the damage is tubular and builds up slowly, creatinine rises after about a week of treatment and urine output is usually preserved, with a concentrating defect. Risk rises with longer courses, high troughs, volume depletion, older age and other nephrotoxins."),
    ('c', "**Can appear or progress AFTER the drug is stopped (cortical depot).** The drug stored in the cortex is released slowly, so creatinine can keep rising for days after the last dose; recovery is usual but slow."),
    ('d', "**Tubular wasting: low Mg, K, Ca.** Proximal and distal tubular injury causes magnesium wasting, which in turn drives potassium and calcium loss; check and replace magnesium first."),
    ('e', "**Prevent: once-daily dosing, trough monitoring, avoid other nephrotoxins.** Keep courses short (stop after 3–5 days or when susceptibilities allow), keep the trough low (gentamicin under 1 mg/L, amikacin under about 2.5–5 mg/L), keep the patient filled, and avoid adding vancomycin, contrast, NSAIDs or loop diuretics where possible."),
  ],
  mimic=[
    ("Aminoglycoside AKI vs contrast AKI", "Aminoglycoside: after 5–7 days, non-oliguric, low magnesium, may progress after stopping. Contrast: within 24–72 h, often transient."),
    ("Aminoglycoside AKI vs acute interstitial nephritis", "AIN: rash, fever, eosinophils, white cell casts, after β-lactams or PPIs; aminoglycoside injury is tubular necrosis without allergic features."),
  ],
  traps=[
    ("“Aminoglycoside AKI is oliguric and immediate”", "It is typically non-oliguric and appears after about a week."),
    ("“Creatinine will improve as soon as the drug is stopped”", "The cortical store can keep injuring the tubule for days."),
    ("“Divided dosing is safer for the kidney”", "Uptake is saturable and continues while the trough stays up; once-daily dosing is safer."),
  ],
  decode=[
    ("Aminoglycoside nephrotoxicity — mechanism and pattern? [DocT GT]", "Megalin-mediated proximal tubular uptake into the cortex; non-oliguric AKI after 5–7 days with magnesium wasting, which may progress after stopping."),
    ("[pattern] Elderly on gentamicin, creatinine 2.6, vomiting — next step?", "Stop gentamicin and give volume."),
  ],
  punch="Aminoglycosides are pumped into the proximal tubule by megalin and stored in the cortex, so the AKI is late, non-oliguric, magnesium-wasting and can worsen after stopping; one daily dose with a low trough is the protection.",
)

FLAGS = {
  'T_29b5a652': "‘10–30% of courses’: the usual quoted range is about 10–25% (StatPearls, aminoglycosides); the explanation keeps the card’s figure.",
}
