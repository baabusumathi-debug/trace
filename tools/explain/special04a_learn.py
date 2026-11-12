# SPECIAL04A — Explain v3 ("Learn" depth): pharmacokinetics principles in the critically ill — absorption, volume of distribution, hydrophilic vs lipophilic drugs, obesity,
# hypoalbuminaemia, hepatic clearance, augmented renal clearance, renal replacement therapy, PK/PD indices and targets, and putting a dose together.
# No mnemonics or hooks. Driven by the real questions in qpack/SPECIAL04A.md (24 question links; PK-05 and PK-11 asked 4 times, PK-01, PK-02 and PK-08 three times each).
# Fields as TOX01, plus SPINE, PRIMER and step. PK-03 and PK-04 have no linked question and get short explanations with [pattern] decode items.
# qbank.json `cards` entries for this deck carry chips, lines and one `cross` note (PK-11: the DocT CKD key is wrong); no `fix` entries (checked 13 Nov 2026).
# Checked online on 13 Nov 2026:
#  - Augmented renal clearance: CrCl >130 mL/min/1.73 m² (Pharmacy Times review; Med Intensiva 2018 review); ARC score (Udy) age ≤50 = 6, trauma = 3, SOFA ≤4 = 1; 0–6 low, 7–10 high risk;
#    ARCTIC score for trauma (creatinine <62 µmol/L 3, male 2, age <56 4 or 56–75 3; >6 high risk); prevalence 14–80% by ICU type (Udy 2013: 58% of septic/trauma patients with a normal creatinine; ARCTIC points not re-verified in review); equations inadequate,
#    timed urine collection (2–24 h; usually 8 h); loading dose unchanged; meropenem 2 g 8-hourly, pip-tazo 4.5 g 4–6-hourly, extended/continuous infusion.
#  - Vancomycin 2020 consensus (ASHP/IDSA/PIDS/SIDP, summary by Clinician.com): AUC24/MIC(BMD) 400–600 for serious MRSA, assume MIC 1 mg/L, Bayesian monitoring with 1–2 levels preferred,
#    trough 15–20 targets abandoned, loading 20–35 mg/kg (max 3 g) in the seriously ill, obese loading 20–25 mg/kg (max 3 g), continuous infusion an alternative (target 20–25 mg/L).
#  - BLING III (Dulhunty, JAMA 2024; summary by The Bottom Line): 7,202 patients, pip-tazo or meropenem, 90-day mortality 24.9% vs 26.8%, difference −1.9% (95% CI −4.9 to 1.1), p = 0.08;
#    clinical cure 55.7% vs 50.0% (p < 0.001). Companion meta-analysis (Abdul-Aziz, JAMA 2024; Contagion Live summary): 18 RCTs, 9,108 patients, 90-day mortality RR 0.86 (95% credible interval 0.72–0.98).
#  - Surviving Sepsis Campaign 2026 (Crit Care Med, 23 Mar 2026; Epocrates and Guideline Central summaries): STRONG recommendation for prolonged beta-lactam infusion for maintenance after an
#    initial bolus (upgraded from the 2021 weak recommendation).
#  - Hypoalbuminaemia (Ulldemolins, Clin Pharmacokinet 2011): incidence up to 40–50%; highly bound (>70%) include ceftriaxone 85–95%, ertapenem 85–95%, flucloxacillin 95%, daptomycin 90–93%,
#    teicoplanin 90–95%; vancomycin MODERATELY bound (30–60%); ceftriaxone Vd and clearance about doubled (Joynt); Vd rise dominates, so higher or loading doses early.
#  - Beta-lactam TDM target (Guilhaumou, Crit Care 2019, French societies): free concentration 4–8 × MIC for 100% of the dosing interval.
#  - Polymyxin consensus 2019 (Tsuji): colistin AUCss,24h about 50 mg·h/L (Css,avg about 2 mg/L); CMS load 300 mg CBA (about 9 MIU); polymyxin B preferred systemically.
#  - Daptomycin in obesity: label and ACCP guidance use total (actual) body weight (UNMC ID blog 2022).
#  - ECMO (LITFL): circuit sequestration greatest for lipophilic and highly protein-bound drugs (fentanyl, midazolam, propofol, voriconazole); priming haemodilution affects small-Vd drugs.
# Second review 13 Nov 2026: see special04a_review.md (metoprolol ratio, phenytoin feed break, ARC wording, linezolid clearance, daptomycin/linezolid targets corrected).
# From standard references without a fresh check (confident): one-compartment equations (loading dose = Cp × Vd; half-life = 0.693 × Vd ÷ CL); hepatic clearance = Q × ER, high-ER drugs
# (fentanyl, morphine, propofol, lidocaine, propranolol) flow-dependent, low-ER drugs (phenytoin, warfarin, diazepam) depend on fu × CLint; the Benet–Hoener rule on when binding changes matter;
# phenytoin ~90% bound, free level 1–2 mg/L, Winter–Tozer correction; CRRT clearance ≈ sieving coefficient (≈ fu) × effluent rate; aminoglycoside Cmax/MIC 8–10; fluoroquinolone AUC/MIC 125
# (Gram-negatives) and 30–50 (Gram-positives); Craig’s fT>MIC 40% carbapenems, 50% penicillins, 60–70% cephalosporins; aminoglycoside adjusted weight = IBW + 0.4 × (TBW − IBW);
# ceftolozane-tazobactam 3 g 8-hourly for HAP/VAP (double the cIAI/cUTI dose); tigecycline 100 mg load; inflammation (IL-6) down-regulates CYP3A4 more than glucuronidation.

SPINE = [
  ("Getting the drug in", "In shock the gut and the skin lose their blood supply, so oral, enteral and subcutaneous drugs are absorbed unpredictably and critical drugs go intravenously."),
  ("Where the drug goes", "Capillary leak, fluids and low albumin expand the space hydrophilic drugs must fill, so the same dose gives a lower level and the loading dose has to be bigger."),
  ("How the body clears it", "The liver clears high-extraction drugs in proportion to its blood flow and low-extraction drugs by its enzymes, while the young septic or injured kidney may clear far more than the creatinine suggests."),
  ("Clearance by the machine", "Renal replacement therapy removes small, poorly bound, hydrophilic drugs in proportion to the effluent rate, so doses set for anuria are often too low on CRRT."),
  ("What the bug needs", "Beta-lactams kill by time above the MIC, aminoglycosides by peak height and vancomycin and fluoroquinolones by total exposure, and each has a target number."),
  ("Putting the dose together", "The volume sets the loading dose whatever the kidneys are doing, the eliminating organ sets the maintenance, the drug’s killing pattern sets how it is infused, and levels check the result."),
]

PRIMER = "Volume of distribution (Vd) is the volume a drug would need to fill to give the concentration measured in plasma; it is a ratio (amount in the body ÷ plasma concentration), not a real space, so a drug that hides in fat or tissue has a Vd far larger than the patient. Clearance (CL) is the volume of plasma cleared of drug per unit time, and the two together set the half-life (0.693 × Vd ÷ CL). The first dose is sized by Vd (dose = target concentration × Vd) and the doses that follow are sized by clearance. Only the free, unbound drug acts on bacteria and receptors, is filtered and is metabolised, and the minimum inhibitory concentration (MIC) is the lowest free concentration that stops a given organism growing."

L = {}

L['PK-01'] = dict(
  sub="Special topics → Pharmacokinetics → Absorption in the critically ill",
  step=1,
  intro="Step 1 is getting the drug into the circulation at all. In a well patient a tablet or a subcutaneous injection behaves predictably; in shock the body diverts blood away from the gut and the skin to keep the heart and brain perfused, so anything placed in those beds sits there. The three real questions test three variants of this: a subcutaneous drug in shock, a high first-pass drug switched to IV, and a drug that binds to enteral feed. Most of the cohort got all three wrong.",
  parts=[
    ('a', "**PK determinants: Vd, clearance, Cmax, Cmin, AUC₀₋₂₄.** Vd and clearance are properties of the patient and the drug; Cmax (the peak), Cmin (the trough) and the area under the concentration–time curve over 24 hours are the exposures that result from a given dose. Each antibiotic’s effect is tied to one of these exposures (PK-09), which is why the changes in this deck matter."),
    ('b', "**Why absorption falls: shock (gut blood flow diverted), mucosal atrophy, poor motility (opioids, electrolytes), raised gastric pH (PPI, H2 blockers), reduced pancreatic function.** Splanchnic vasoconstriction in shock and on vasopressors cuts the blood flow that carries absorbed drug away. An unused gut atrophies, opioids and low potassium or magnesium slow emptying, and acid suppression stops drugs that need acid to dissolve (itraconazole capsules, ketoconazole) from going into solution. The same vasoconstriction affects the skin, so subcutaneous drugs are absorbed poorly too: on vasopressors subcutaneous enoxaparin gives low anti-Xa levels, and an IV heparin infusion is the safer choice."),
    ('c', "**Drug–feed interactions: warfarin, phenytoin, tetracyclines, minocycline, ciprofloxacin, fluconazole bind to enteral feed.** Phenytoin binds to feed proteins and to the tube, so starting continuous feeds can drop its level sharply; hold the feed for about 2 hours before and after each dose (UK Specialist Pharmacy Service advice), or give it IV, and recheck the level. Ciprofloxacin and the tetracyclines chelate the calcium, magnesium and iron in the feed. Warfarin binds to feed protein, and its effect falls even with low-vitamin-K feeds, so the INR drifts when feeds start or stop. Fluconazole is the weakest member of this list: it is still well absorbed through a feeding tube (see FLAGS)."),
  ],
  mimic=[
    ("Poor absorption vs high first-pass metabolism", "Poor absorption means less drug reaches the portal blood. High first-pass metabolism means plenty is absorbed but the gut wall and liver destroy most of it before it reaches the systemic circulation, so the IV dose is much smaller than the oral one (oral bioavailability of metoprolol is about 50%, and its label puts oral to IV doses for the same beta-blockade at about 2.5 : 1, so 5 mg IV matches roughly 12.5 mg orally)."),
    ("Enteral feed vs hypoalbuminaemia as the cause of a phenytoin problem", "Feeds lower absorption, so the patient under-doses and seizes. Low albumin raises the free fraction, so the patient is at risk of toxicity at a ‘normal’ total level (PK-05)."),
  ],
  traps=[
    ("“In shock, oral mycophenolate or sublingual tacrolimus is the absorption worry” (35% right)", "With bowel sounds and bowel movements the gut is working, and sublingual and IV routes bypass the problem. The drug to worry about is subcutaneous enoxaparin, because vasopressors shut down skin perfusion."),
    ("“High first-pass drug: increase the IV dose” (31% right)", "The opposite: IV skips gut-wall and hepatic extraction, so far less is needed; give a smaller IV dose (metoprolol, propranolol, diltiazem, verapamil, morphine)."),
    ("“Seizure on day 5 on phenytoin with albumin 1.5 g/dL — hypoalbuminaemia” (20% right)", "Low albumin raises free phenytoin and risks toxicity, not seizures. Enteral feeds started on day 3 bound the phenytoin and dropped the level. Kidney dysfunction does not matter much (phenytoin is hepatically cleared), and modestly raised liver enzymes do not lower its level."),
  ],
  decode=[
    ("Septic shock on vasopressors, transplant drugs and an anticoagulant — which route are you most concerned about? [DocT GT]", "Subcutaneous enoxaparin: skin perfusion falls on vasopressors."),
    ("Oral form has significant first-pass metabolism — how should the IV dose differ? [DocT GT]", "Decrease it."),
    ("On oral phenytoin, enteral feeds started on day 3, seizure on day 5, albumin low — most likely cause? [DocT GT]", "Enteral tube feeds."),
  ],
  extra=[
    dict(q="Why does a low-albumin patient on phenytoin seize after feeds start, when low albumin should raise free phenytoin?", a="Low albumin changes the split between bound and free drug; the feed changes how much drug is absorbed. Absorption falls, so total and free levels both drop."),
  ],
  punch="In shock, give critical drugs IV: the gut and the skin are the first beds the body shuts down. A high first-pass drug needs a smaller IV dose, and starting enteral feeds can quietly drop phenytoin, warfarin and ciprofloxacin levels.",
)

L['PK-02'] = dict(
  sub="Special topics → Pharmacokinetics → Volume of distribution in sepsis",
  step=2,
  intro="Step 2 asks where the drug goes once it is in. A hydrophilic antibiotic cannot cross cell membranes, so it stays in the extracellular water, and sepsis expands that water: leaky capillaries let fluid into the tissues, the resuscitation adds litres, and drains and circuits add more. The same dose is diluted into a bigger space. The real questions check whether you know this changes the dose and not the interval, and whether you can calculate a load.",
  parts=[
    ('a', "**Vd = the apparent volume a drug would need to fill at its plasma concentration (dose ÷ concentration).** It is a ratio, not an anatomical space. For a one-compartment drug, the dose needed for a target peak is Cmax × Vd: with a Vd of 0.6 L/kg in a 70-kg patient, Vd is 42 L, and a Cmax of 12 mg/L needs 12 × 42 = 504 mg."),
    ('b', "**Sepsis: capillary leak + aggressive fluids + drains and circuits → extracellular water expands → hydrophilic drugs (confined to that water) dilute.** An aminoglycoside’s Vd of about 0.25 L/kg in health often rises towards 0.4 L/kg or more in septic shock, so a standard dose gives a lower peak than expected. Lipophilic drugs are already spread through cells and fat, so a few extra litres of extracellular water hardly change their much larger Vd."),
    ('c', "**Shown for aminoglycosides, β-lactams, vancomycin; higher APACHE II → larger Vd.** The sicker the patient, the more leak and the more fluid, so the gap between the expected and the actual level is widest in the patients who most need an effective first dose."),
    ('d', "**So: loading doses must be bigger (Vd sets the loading dose; clearance sets the maintenance).** A larger Vd also lengthens the half-life (0.693 × Vd ÷ CL), so the drug lingers at a lower level. The answer to a larger Vd is a bigger dose, not a more frequent one. In an anuric, fluid-overloaded patient, the amikacin dose goes up because of the Vd, and the anuria lengthens the interval until the next dose; it never shrinks the first one."),
  ],
  mimic=[
    ("Larger Vd vs lower clearance", "Larger Vd: lower peak, same total removal, so give a bigger dose. Lower clearance: drug accumulates, so give the same load and extend the interval or lower the maintenance."),
    ("Hydrophilic vs lipophilic drugs in sepsis", "Hydrophilic drugs (β-lactams, aminoglycosides, glycopeptides) have a small Vd that rises in sepsis. Lipophilic drugs (fluoroquinolones) have a large Vd that barely changes (PK-03)."),
  ],
  traps=[
    ("“Anuric septic shock on amikacin: decrease the dose for renal function” (14% right)", "Renal failure lengthens the interval, never the load; the expanded Vd from leak and 3 L of fluid needs a bigger dose."),
    ("“Increase the dosing frequency because of the increased Vd”", "Frequency is set by clearance; a larger Vd is answered with a bigger dose, and in anuria the doses must come less often, not more."),
    ("“Decrease the dose because of decreased protein binding”", "Aminoglycosides are barely protein bound (under 10–20%), so binding is irrelevant here."),
    ("“Critical illness decreases the Vd of hydrophilic drugs” (NEET 2025 distractor)", "It increases it. The keyed answer to that recall is altered protein binding (PK-05)."),
  ],
  decode=[
    ("Septic shock, anuric, volume-overloaded after 3 L, broadened to meropenem, amikacin, daptomycin, micafungin — amikacin dose consideration? [DocT GT]", "Increase the dose because of the increased Vd."),
    ("Vd 0.6 L/kg, 70 kg, target Cmax 12 mg/L — loading dose? [DocT GT]", "504 mg (12 × 0.6 × 70)."),
    ("Which PK change in critically ill poisoned patients most complicates management? [NEET 2025]", "Altered plasma protein binding; the Vd of hydrophilic drugs rises, it does not fall."),
  ],
  punch="Sepsis pours water into the space hydrophilic drugs occupy, so the same dose gives a lower level. A bigger Vd needs a bigger dose, not a shorter interval, and failing kidneys never shrink the first dose.",
)

L['PK-03'] = dict(
  sub="Special topics → Pharmacokinetics → Hydrophilic vs lipophilic antibiotics",
  step=2,
  intro="Step 2 continues with the property that predicts how sepsis will change a drug. Whether an antibiotic dissolves in water or in fat decides where it goes, which organ clears it and how much critical illness disturbs it. No real question tests this table directly, but it is the reason behind PK-02, PK-07 and PK-08.",
  parts=[
    ('a', "**Examples: hydrophilic — β-lactams, aminoglycosides, glycopeptides, linezolid, colistin; lipophilic — fluoroquinolones, macrolides, lincosamides, tigecycline.**"),
    ('b', "**Vd: hydrophilic low, rises in sepsis; lipophilic high, little change.** Hydrophilic drugs stay in the extracellular water, which leak and fluids expand. Lipophilic drugs enter cells and fat; tigecycline’s Vd is several litres per kilogram."),
    ('c', "**Clearance: hydrophilic renal; lipophilic hepatic.** A water-soluble drug is filtered and leaves in urine unchanged; a fat-soluble drug is reabsorbed in the tubule and must first be metabolised by the liver. Linezolid does not fit this row: only about 30% leaves unchanged in urine and about two-thirds of its clearance is non-renal, which is why it needs no renal dose change (see FLAGS)."),
    ('d', "**Cell penetration: hydrophilic poor, lipophilic good.** So intracellular organisms (Legionella, Chlamydia, Mycoplasma) need a lipophilic drug such as a macrolide or a fluoroquinolone."),
    ('e', "**In sepsis: hydrophilic — bigger load, clearance follows the kidneys (ARC or AKI); lipophilic — dose by liver function.** Hydrophilic drugs are hit twice in critical illness: a larger Vd and a clearance that may rise (PK-07) or fall (PK-08)."),
  ],
  mimic=[
    ("Hydrophilic drug on CRRT vs lipophilic drug on ECMO", "CRRT removes small, poorly bound hydrophilic drugs. The ECMO circuit absorbs lipophilic, highly bound drugs (fentanyl, midazolam, propofol, voriconazole)."),
  ],
  traps=[
    ("“Fluoroquinolones need a bigger loading dose in sepsis”", "Their large Vd barely changes; the loading-dose problem belongs to hydrophilic drugs."),
  ],
  decode=[
    ("Which antibiotic’s Vd changes most in septic shock? [pattern]", "A hydrophilic one: an aminoglycoside, a β-lactam or vancomycin, not a fluoroquinolone."),
    ("Which antibiotic needs hepatic, not renal, dose adjustment? [pattern]", "A lipophilic one, for example tigecycline."),
  ],
  punch="Water-soluble antibiotics live in the extracellular water and leave by the kidney, so sepsis changes both their volume and their clearance. Fat-soluble ones live in tissue, leave by the liver and change little.",
)

L['PK-04'] = dict(
  sub="Special topics → Pharmacokinetics → Dosing weight in obesity",
  step=2,
  intro="Step 2 includes the obese patient, in whom the question is how much of the extra weight the drug actually spreads into. Fat holds little water, so a hydrophilic drug does not distribute into it fully, but lean mass, blood volume and kidney size also rise with obesity. No real question tests this card; it is a likely recall item.",
  parts=[
    ('a', "**Aminoglycosides: adjusted body weight.** Adjusted weight = ideal weight + 0.4 × (total − ideal): aminoglycosides distribute into extracellular water, and about 40% of the excess weight behaves like lean tissue for them. Dosing on total weight would give toxic peaks; on ideal weight, low ones."),
    ('b', "**β-lactams, daptomycin: lean body weight.** In practice β-lactams are not dosed by weight: obese patients get the top of the usual dose range, often as an extended infusion. Daptomycin is the exception that does not fit the card. Its label and most guidance use total (actual) body weight (see FLAGS)."),
    ('c', "**Vancomycin: total (actual) body weight.** Vancomycin’s Vd and clearance both rise with total weight, so the load is 20–25 mg/kg of actual weight in obesity, capped at 3 g (2020 consensus), and later doses are set by AUC-guided monitoring."),
  ],
  mimic=[
    ("Loading vs maintenance in obesity", "The load follows Vd and so the weight the drug distributes into. Maintenance follows clearance, which rises less than the weight does, so it is adjusted by levels."),
  ],
  traps=[
    ("“Vancomycin in obesity: dose on ideal weight”", "That under-loads; vancomycin loads are on actual weight, capped at 3 g."),
    ("“Aminoglycosides on total weight in obesity”", "This overshoots the peak and raises toxicity; use adjusted weight."),
  ],
  decode=[
    ("Obese patient, gentamicin once daily — which weight? [pattern]", "Adjusted body weight."),
    ("Obese patient with MRSA bacteraemia — vancomycin loading weight? [pattern]", "Actual (total) body weight, maximum 3 g."),
  ],
  punch="Aminoglycosides use adjusted weight, vancomycin uses actual weight with a 3 g cap, and β-lactams get the top of the range by infusion. Obesity also predicts β-lactam and linezolid failure, because fixed doses are spread through a larger body.",
)

L['PK-05'] = dict(
  sub="Special topics → Pharmacokinetics → Hypoalbuminaemia and protein binding",
  step=2,
  intro="Step 2 ends with protein binding, which decides how much of the drug in the plasma is free to act and free to be cleared. Albumin falls early and steeply in critical illness, so the free fraction of highly bound acidic drugs rises. The four real questions test two consequences: a total level that looks therapeutic while the free level is toxic (phenytoin), and which drugs a binding change really matters for.",
  parts=[
    ('a', "**Low albumin in 40–50% of septic patients.** Albumin falls through capillary leak, reduced hepatic synthesis in the acute-phase response and dilution by fluids, and the fall is often below 25 g/L."),
    ('b', "**Highly bound drugs: more free fraction → bigger Vd and faster clearance → low troughs.** Only free drug crosses into tissues and is filtered by the glomerulus. When albumin falls, the extra free drug spreads into the expanded interstitium and is cleared faster, so total levels drop; in hypoalbuminaemic patients on ceftriaxone both Vd and clearance roughly double. For a time-dependent antibiotic the trough falls below the MIC early in the interval. The rise in Vd is the dominant effect, so give the full loading dose and, for β-lactams, dose more often or by continuous infusion."),
    ('c', "**Matters for ceftriaxone, daptomycin, flucloxacillin, vancomycin (also ertapenem, teicoplanin).** These bind more than 70%: ceftriaxone and ertapenem 85–95%, flucloxacillin about 95%, daptomycin and teicoplanin about 90%. Vancomycin is only moderately bound (30–60%), so it belongs on this list less than the others (see FLAGS). The same reasoning applies outside antibiotics to phenytoin and valproate."),
    ('d', "**Albumin falls but α₁-acid glycoprotein rises (binds basic drugs) in critical illness.** Albumin carries acidic drugs (phenytoin, warfarin, ceftriaxone). α₁-acid glycoprotein is an acute-phase protein that carries basic drugs (lidocaine and other local anaesthetics), so their free fraction can fall in inflammation."),
  ],
  table=dict(title="When does a binding change alter the free (active) level?", head=["Drug type", "Example", "Effect of a fall in binding"], rows=[
    ["Low extraction, any route", "phenytoin, valproate, warfarin", "free level returns to normal as clearance of the free drug rises; **only the total falls** (reading trap)"],
    ["High extraction, given IV", "IV lidocaine, fentanyl, propofol", "clearance is set by liver blood flow, so the total stays put and **the free level rises** (real effect)"],
    ["Narrow therapeutic index", "phenytoin", "the transient rise in free drug can still cause toxicity"],
  ]),
  mimic=[
    ("Total vs free phenytoin", "Total measures bound plus free; only free (normal 1–2 mg/L) acts. In low albumin or uraemia a total of 10 mg/L can carry a free level that is toxic. Measure free phenytoin, or correct the total (Winter–Tozer: total ÷ (0.2 × albumin g/dL + 0.1), using 0.1 × albumin in end-stage renal disease; this is the classic form, revised versions exist, and a measured free level is more reliable)."),
    ("Low albumin vs uraemia", "Both raise free phenytoin: low albumin by removing binding sites, uraemia because retained toxins displace the drug from albumin."),
  ],
  traps=[
    ("“A total phenytoin of 10 mg/L is therapeutic, so the signs are not toxicity”", "In dialysis patients the free fraction rises from about 10% to 20–30%, so the free level is high (89–100% right on DocT GT)."),
    ("“The total level is low, so increase the phenytoin dose”", "Chasing the total in hypoalbuminaemia causes toxicity; dose by the free level."),
    ("“High protein affinity” or “low fu, oral use” is what makes binding changes matter (55% right)", "For a low-extraction or oral drug the free level re-equilibrates; it is the high-extraction drug given IV (and narrow-index drugs) where a change in binding lastingly changes the free concentration."),
    ("“More free drug means more effect”", "For antibiotics, the extra free drug is cleared faster, so the net result is underdosing of time-dependent drugs."),
  ],
  decode=[
    ("Haemodialysis, phenytoin total 10 mg/L, signs of toxicity — explanation? [DocT GT ×2]", "Increased fraction unbound."),
    ("Which drug characteristic makes protein-binding changes most clinically relevant? [DocT GT]", "High extraction, IV use."),
    ("Critically ill poisoned patient — which PK change most complicates management? [NEET 2025]", "Alterations in plasma protein binding (hypoalbuminaemia, acidosis and uraemia raise the free fraction of phenytoin, valproate and warfarin)."),
  ],
  punch="Low albumin raises the free fraction. For an antibiotic, that extra free drug spreads out and is cleared, so levels fall. For phenytoin, it means a ‘therapeutic’ total can hide a toxic free level, so measure the free drug.",
)

L['PK-06'] = dict(
  sub="Special topics → Pharmacokinetics → Hepatic clearance",
  step=3,
  intro="Step 3 turns to how the body removes the drug, starting with the liver. Hepatic clearance is liver blood flow multiplied by the fraction of drug the liver extracts in one pass, and that one number divides drugs into two families that respond to critical illness quite differently. The two real questions ask which change matters for fentanyl, and when a change in binding matters.",
  parts=[
    ('a', "**Extraction ratio: flow-limited high; capacity-limited low.** A high-extraction drug (above about 0.7: fentanyl, morphine, propofol, lidocaine, propranolol) is almost completely removed in one pass. A low-extraction drug (below about 0.3: phenytoin, warfarin, diazepam) mostly passes through unchanged."),
    ('b', "**Clearance depends on: flow-limited — liver blood flow (shock lowers it); capacity-limited — enzyme activity (CYP3A4) and protein binding.** If the liver removes almost all the drug it receives, the only way to change clearance is to change how much blood arrives: clearance ≈ hepatic blood flow. If it removes little, clearance depends on the free fraction and on how fast the enzymes work (fu × intrinsic clearance), and blood flow hardly matters."),
    ('c', "**Sensitive to: flow-limited — haemodynamics; capacity-limited — inflammation, binding changes.** In shock, low cardiac output and vasopressors cut liver blood flow, so fentanyl, morphine and lidocaine accumulate. Inflammation (IL-6) down-regulates CYP enzymes, so capacity-limited drugs slow down in sepsis, and a fall in binding speeds their clearance."),
  ],
  mimic=[
    ("High-extraction drug IV vs orally", "Given IV, its clearance follows liver blood flow. Given orally, most is removed on first pass, so liver disease or portosystemic shunting raises bioavailability sharply and the oral dose must fall (PK-01)."),
  ],
  traps=[
    ("“Fentanyl is most affected by decreased intrinsic clearance or fewer hepatocytes” (47% right)", "Fentanyl is high-extraction: the liver has spare enzyme capacity, so the limit is blood flow. Decreased hepatic blood flow is the answer."),
    ("“Decreased protein binding is the main issue for fentanyl”", "For a high-extraction drug, binding changes do not change total clearance. They change the free level (PK-05), not the clearance this stem asks about."),
  ],
  decode=[
    ("Fentanyl, a high-extraction drug, is most influenced by which critical-illness change? [DocT GT]", "Decreased hepatic blood flow."),
    ("Which drug characteristic makes protein-binding changes most clinically relevant? [DocT GT]", "High extraction, IV use (PK-05)."),
  ],
  extra=[
    dict(q="Watch line: which phase of hepatic metabolism suffers more in inflammation, and which antibiotics are reduced in hepatic dysfunction?", a="Phase I (CYP oxidation) more than phase II (glucuronidation). Reduce tigecycline (keep the 100 mg load, halve the maintenance in severe impairment), rifampicin and metronidazole."),
  ],
  punch="High-extraction drugs such as fentanyl, morphine and lidocaine are cleared at the rate blood reaches the liver, so shock makes them accumulate. Low-extraction drugs depend on enzymes and binding, so inflammation and low albumin change them.",
)

L['PK-07'] = dict(
  sub="Special topics → Pharmacokinetics → Augmented renal clearance",
  step=3,
  intro="Step 3 continues with the kidney, and with the surprise that it often clears drugs faster than normal in the critically ill. A young patient with trauma, a head injury, burns or sepsis has a high cardiac output and high renal blood flow, and his glomerular filtration can run at 150–200 mL/min with a normal creatinine. Renally cleared antibiotics then leave the body too fast. Both real questions are about recognising the resulting underdosing and fixing it.",
  parts=[
    ('a', "**Definition: creatinine clearance over 130 mL/min.** The accepted threshold is over 130 mL/min/1.73 m²; some studies require it on more than half of measurements rather than once. It is common: 14–80% of ICU patients depending on the unit and the definition, and in one study of septic and trauma patients with a normal plasma creatinine, 58% had it (86% of the trauma patients)."),
    ('b', "**Who: young polytrauma, TBI, meningitis, post-operative, burns, VAP, pregnancy.** The common thread is a hyperdynamic circulation from systemic inflammation, often with plenty of fluid, in a young person with good renal reserve. Age under 50, trauma, male sex and a low severity score (SOFA 4 or less) are the consistent predictors. The ARC score adds age ≤50 (6 points), trauma (3) and SOFA ≤4 (1): 7–10 is high risk."),
    ('c', "**Measurement: Cockcroft-Gault, MDRD, CKD-EPI are not valid; use measured urinary creatinine clearance.** These equations assume a stable creatinine and a normal relationship between muscle mass and creatinine, and they are built for diseased kidneys. A timed urine collection (8–24 hours; at least one 8-hour collection in patients at risk) is the bedside measure, repeated because ARC changes from day to day."),
    ('d', "**Drugs affected: vancomycin, aminoglycosides, β-lactams — subtherapeutic levels, treatment failure.** They are hydrophilic and renally cleared, so their clearance tracks the GFR. Time-dependent β-lactams suffer most, because a fast clearance means the level falls below the MIC early in each interval."),
    ('e', "**Response: higher or more frequent doses; extended infusions; TDM.** For example, meropenem 2 g 8-hourly as an extended infusion, piperacillin-tazobactam 4.5 g 6-hourly or 4-hourly (or continuously), and AUC-guided vancomycin. The loading dose does not change. Extended or continuous infusion keeps the level above the MIC despite the fast clearance; cutting the dose or giving standard short boluses does the opposite."),
  ],
  mimic=[
    ("ARC vs AKI", "Both change renal clearance of the same drugs, in opposite directions. AKI is suspected from a rising creatinine, but ARC is hidden behind a normal one, so it is missed unless clearance is measured."),
  ],
  traps=[
    ("“Trauma patient with CrCl 145 on pip-tazo: standard intermittent dosing” (37% right)", "At that clearance standard boluses leave long periods below the MIC; extended (or continuous) infusion is the fix. Reducing the dose is the opposite of what is needed."),
    ("“Switch to aminoglycoside monotherapy”", "Aminoglycosides are also cleared faster in ARC, and monotherapy for septic shock is inadequate."),
    ("“Poor response despite susceptibility means resistance was induced” (51% right)", "In the critically ill the commonest reason is underdosing. Standard-dose ceftolozane-tazobactam is a clear example: the VAP dose is 3 g 8-hourly, double the dose for intra-abdominal or urinary infection, and leak plus ARC lower levels further."),
    ("“A normal creatinine means normal clearance”", "A young trauma patient with a normal creatinine may clear 200 mL/min."),
  ],
  decode=[
    ("45-year-old trauma patient, CrCl 145 mL/min/1.73 m², pip-tazo for septic shock — which intervention optimises therapy? [DocT GT]", "Extended-infusion dosing."),
    ("Pseudomonas VAP on standard-dose ceftolozane-tazobactam, susceptible, poor response — best explanation? [DocT GT]", "Drug underdosing in critically ill patients."),
  ],
  punch="Young, injured or septic patients often clear renally excreted antibiotics far faster than their normal creatinine suggests. Measure the clearance, keep the full load, and give β-lactams more often or by extended infusion.",
)

L['PK-08'] = dict(
  sub="Special topics → Pharmacokinetics → Antibiotics on renal replacement therapy",
  step=4,
  intro="Step 4 is clearance by a machine. When the kidneys fail, the filter takes over part of their job, but it is a sieve with fixed rules: it removes what is small, free in the plasma and not hidden in the tissues, and it removes it in proportion to how much effluent is made. The real questions test the commonest reason for dose change in the ICU and, twice, what to do when CRRT starts on a drug dosed for anuria.",
  parts=[
    ('a', "**What decides removal: protein binding, hydrophilicity, RRT mode, filter porosity, flows.** Only free drug passes the membrane, so the sieving coefficient is roughly the unbound fraction (1 − protein binding). Most antibiotics (vancomycin about 1.5 kDa included) are far below the cut-off of a high-flux filter, so size rarely limits removal. Extracorporeal clearance ≈ sieving coefficient × effluent rate: a 25%-bound drug at 25–35 mL/kg/h is cleared at roughly 25–35 mL/min, more than the CrCl under 20 its dose was set for. A large Vd means only a small share of the body’s drug is in the plasma at any moment, which matters for short intermittent sessions (and rebound after them) more than for continuous therapy. Removal matters most for drugs normally cleared by the kidneys."),
    ('b', "**Predictability: hard to predict; easier on CRRT than SLED; risk of over- and under-dosing.** On CRRT, clearance is steady and can be estimated from the effluent rate, but delivered dose falls with filter clotting and downtime. For β-lactams underdosing is the greater danger, because their therapeutic index is wide and failure to treat the infection kills."),
    ('c', "**Early dosing: β-lactams — use full (non-AKI) doses for the first 48 h; higher doses, extended infusion.** In the first two days the Vd is at its largest, the kidneys may recover, and the machine adds clearance. Cutting β-lactam doses for the creatinine during this period is the common error."),
    ('d', "**SLED removes antibiotics more efficiently than CRRT or intermittent HD, especially small, renally cleared, poorly bound drugs (β-lactams).** During a session SLED clears drug at a high rate, close to that of intermittent haemodialysis and higher than CRRT, then stops. So time doses to come after the session or give a supplement, rather than assuming steady removal (see FLAGS on the word ‘efficiently’)."),
    ('e', "**Aminoglycosides: higher dose, infrequent; TDM.** Give the full Vd-based load for the peak, then redose only when the level has fallen, because the trough drives toxicity. For vancomycin, use a weight-based load and then AUC-guided levels on CRRT."),
  ],
  mimic=[
    ("CRRT vs ECMO circuit", "CRRT removes small, poorly bound hydrophilic drugs into the effluent. The ECMO circuit absorbs lipophilic and highly protein-bound drugs (fentanyl, midazolam, propofol, voriconazole) onto the oxygenator and tubing, and its priming volume dilutes small-Vd drugs."),
    ("Continuous vs intermittent therapy", "On CRRT, Vd barely limits removal over a day. In intermittent HD the short session clears mainly the plasma, so large-Vd drugs rebound from the tissues after it."),
  ],
  traps=[
    ("“Maintain the dose because of the large Vd” for a 25%-bound, small, 60%-renally-cleared drug on CVVHD (39% right)", "On continuous therapy, removal depends on the free fraction and the effluent rate, not on Vd; the machine adds about 25–35 mL/min of clearance to a dose set for CrCl under 20, so increase it. DocT’s own explanation hints that a large Vd limits removal; that applies to intermittent dialysis."),
    ("“Changes in protein binding are the commonest reason to adjust ICU drug doses” (60% right)", "Reduced renal clearance (AKI or CKD) is. Most antibiotics, LMWH and many opioid metabolites are renally eliminated."),
    ("“Subtherapeutic vancomycin on CRRT: de-escalate or use rapid diagnostics”", "A low level is a dosing problem; the stewardship answer is therapeutic drug monitoring (82% right)."),
  ],
  decode=[
    ("Which change in critically ill patients most often makes dose adjustment necessary? [DocT GT]", "Decreased renal clearance."),
    ("New CRE drug dosed for CrCl <20, CVVHD started; 60% renal, Vd 3 L/kg, 25% bound, small — change? [DocT GT]", "Increase the dose because of low protein binding and small molecular weight."),
    ("On CRRT, subtherapeutic vancomycin despite standard dosing — stewardship strategy? [DocT GT]", "Therapeutic drug monitoring."),
  ],
  punch="A filter clears free, small, hydrophilic drugs in proportion to the effluent rate, so a drug dosed for anuria is often too low once CRRT starts. Give full β-lactam doses for the first 48 hours and let levels guide aminoglycosides and vancomycin.",
)

L['PK-09'] = dict(
  sub="Special topics → Pharmacodynamics → Time- vs concentration-dependent killing",
  step=5,
  intro="Step 5 moves from what the body does to the drug to what the drug must do to the bacterium. Antibiotics fall into three killing patterns, and each pattern names the exposure (from PK-01) that predicts success. Getting the pattern right decides whether you lengthen the infusion, raise the peak or raise the daily total. The one real question tests the pairs, and only 23% got it.",
  parts=[
    ('a', "**Time-dependent: index %fT>MIC; β-lactams, carbapenems, linezolid, erythromycin, clarithromycin, lincosamides; extended or continuous infusion; PAE minimal to moderate.** Above about 4 × MIC, β-lactam killing does not get faster, so what counts is how long the free level stays above the MIC. With little post-antibiotic effect against Gram-negatives, regrowth starts as soon as the level falls below it."),
    ('b', "**Concentration-dependent: index Cmax/MIC; aminoglycosides, fluoroquinolones, daptomycin, metronidazole; big dose, long interval; PAE prolonged.** The higher the peak, the faster and more complete the kill. The long post-antibiotic effect suppresses regrowth after levels fall, which is why aminoglycosides are given once daily. The low trough before the next dose also limits renal and ear toxicity."),
    ('c', "**Concentration + time: index AUC₀₋₂₄/MIC; fluoroquinolones, glycopeptides, linezolid, tigecycline, azithromycin, tetracyclines, colistin; enough total daily dose; PAE moderate.** What matters is the total exposure over the day, so the daily dose is set to reach the target, however it is divided. The card puts fluoroquinolones and linezolid in two columns because both indices predict their effect; AUC/MIC is the better predictor for both, and exams still call fluoroquinolones ‘concentration-dependent’."),
  ],
  mimic=[
    ("Vancomycin vs aminoglycoside", "Vancomycin is AUC-dependent, not peak-dependent, so it is monitored by AUC (formerly trough). Aminoglycosides are peak-dependent and dosed once daily for a high Cmax."),
  ],
  traps=[
    ("“Vancomycin is concentration-dependent” (option B)", "Vancomycin is AUC/MIC-dependent; calling it concentration-dependent makes B wrong even though cefazolin is time-dependent."),
    ("“Daptomycin is time-dependent” (option C)", "Daptomycin is concentration-dependent (Cmax/MIC and AUC/MIC), like amikacin."),
    ("“Levofloxacin is time-dependent” (option D)", "Fluoroquinolones are concentration-dependent (AUC/MIC); meropenem is time-dependent."),
  ],
  decode=[
    ("Which correctly pairs the pharmacodynamics with the antibacterial agents? [DocT GT]", "Oxacillin (time-dependent), moxifloxacin (concentration-dependent) — 23% right."),
  ],
  punch="β-lactams need time above the MIC, aminoglycosides need a high peak and vancomycin needs total daily exposure. That is why β-lactams go by extended infusion, aminoglycosides once daily and vancomycin by AUC.",
)

L['PK-10'] = dict(
  sub="Special topics → Pharmacodynamics → PK/PD targets",
  step=5,
  intro="Step 5 puts numbers on the killing patterns. Each target is the exposure that predicted cure (or a fixed amount of bacterial kill) in animal and clinical studies; critically ill patients and resistant organisms need the upper end. The two real questions are both about matching the dosing strategy to the target: a big once-daily aminoglycoside dose, and a prolonged meropenem infusion.",
  parts=[
    ('a', "**β-lactams: 50–70% fT>MIC (penicillins, cephalosporins).** About 50% for penicillins and 60–70% for cephalosporins is needed for maximal killing in classic animal studies."),
    ('b', "**Carbapenems: 40% fT>MIC.** Carbapenems kill faster and have some post-antibiotic effect, so less time is needed."),
    ('c', "**Critically ill / MDR: 100% fT>MIC; maximal killing at 4–5 × MIC.** In the critically ill, levels need to stay above the MIC for the whole interval. French guidance (2019) aims for a free level of 4–8 × MIC throughout; the higher concentration also helps prevent resistance and reach tissues."),
    ('d', "**Aminoglycosides: Cmax/MIC 8–10.** A peak 8–10 times the MIC gives the best kill and limits resistance. In septic shock that means a large once-daily dose (amikacin 25–30 mg/kg; DocT keys this) because the Vd is large."),
    ('e', "**Fluoroquinolones: AUC/MIC 125 (Gram-negatives); Cmax/MIC 10.** For Gram-positives (pneumococcus) about 30–50 is enough; 125 is the Gram-negative target from ciprofloxacin studies (see the card’s watch line on 87.5)."),
    ('f', "**Vancomycin: AUC/MIC 400 (Staph aureus).** The 2020 consensus target is AUC₂₄/MIC 400–600, assuming an MIC of 1 mg/L, estimated with Bayesian software from 1–2 levels. Above 600, kidney injury becomes more likely. Trough targets of 15–20 mg/L have been dropped (see FLAGS)."),
    ('g', "**Daptomycin: Cmax/MIC; AUC/MIC 100.** It is concentration-dependent, and AUC/MIC is the index most studies use. The number quoted varies widely between studies and reviews, so know the index rather than the figure (see FLAGS)."),
    ('h', "**Colistin: AUC/MIC 53–141 (Pseudomonas).** The 2019 international polymyxin consensus states the clinical target as an AUC of about 50 mg·h/L (an average steady-state level of about 2 mg/L), which is also the point above which kidney injury rises. That is the number to quote (see FLAGS)."),
    ('i', "**Linezolid: 40–80% fT>MIC; AUC/MIC.** In a retrospective study of seriously ill patients, success was higher at an AUC/MIC of about 80–120 and when levels stayed above the MIC for the whole interval; the two indices were closely correlated."),
  ],
  mimic=[
    ("Extended infusion vs higher bolus dose of a β-lactam", "Doubling a 30-minute bolus raises the peak, which β-lactams do not need, and adds little time above the MIC. Extending the infusion buys time above the MIC with the same daily dose."),
  ],
  traps=[
    ("“Amikacin 5 mg/kg three times daily to keep a steady trough”", "Divided doses lower the peak and keep the trough up, which loses the Cmax/MIC effect and raises toxicity; give one large daily dose."),
    ("“Continuous aminoglycoside infusion at 10 µg/mL”", "Concentration-dependent drugs need a high peak and a low trough, the opposite of a flat infusion."),
    ("“Meropenem: bolus for a high Cmax/MIC” or “rely on the PAE for long intervals”", "Carbapenems are time-dependent; the answer is extended or continuous infusion for fT>MIC."),
    ("“Double the 30-minute meropenem dose to beat the Vd”", "A bigger bolus mostly raises the peak; extended infusion is the PD answer."),
  ],
  decode=[
    ("Amikacin in septic shock, 70 kg — preferred strategy in the acute phase? [DocT GT]", "A large once-daily dose (25–30 mg/kg) to maximise Cmax/MIC."),
    ("Meropenem in septic shock after big fluids, CrCl 120 — most consistent with stewardship? [DocT GT]", "Continuous or extended infusion to maximise fT>MIC."),
    ("Vancomycin target for serious MRSA infection? [pattern]", "AUC₂₄/MIC 400–600 (2020 consensus)."),
  ],
  punch="β-lactams need the free level above the MIC for the whole interval in the critically ill, aminoglycosides a peak 8–10 times the MIC and vancomycin an AUC of 400–600. Choose the infusion method that hits that number.",
)

L['PK-11'] = dict(
  sub="Special topics → Pharmacokinetics → Antibiotic dosing in the critically ill",
  step=6,
  intro="Step 6 puts the deck together into a prescription. The loading dose answers ‘how big is the space?’ (step 2), the maintenance answers ‘how fast is it cleared?’ (steps 3–4), the method of infusion answers ‘what does the bug need?’ (step 5), and the level answers ‘did it work?’. The four real questions test each piece, and one of them is keyed wrongly.",
  parts=[
    ('a', "**Loading dose for aminoglycosides, β-lactams, glycopeptides, tigecycline, colistin: sized by Vd, independent of renal function.** The first dose fills the volume, and the kidneys have not yet had any time to act, so their function cannot affect it. Examples: vancomycin 20–35 mg/kg of actual weight (maximum 3 g) in the seriously ill; colistin 300 mg colistin base activity (about 9 million IU); tigecycline 100 mg."),
    ('b', "**Maintenance: by the eliminating organ (kidneys, liver).** Renally cleared drugs follow measured clearance, high in ARC (PK-07), low in AKI, added to by RRT (PK-08). Hepatically cleared drugs follow liver function (PK-06)."),
    ('c', "**Time-dependent: bolus then continuous or extended (4 h) infusion; best studied with pip-tazo and meropenem (also vancomycin, ceftriaxone, cefepime); large RCTs show no distinct advantage, meta-analyses conflict (BLING III: no significant 90-day mortality difference).** The bolus reaches the target at once; the infusion keeps the level above the MIC. BLING III (JAMA 2024, 7,202 patients on pip-tazo or meropenem) found 90-day mortality of 24.9% with continuous infusion vs 26.8% with intermittent (p = 0.08), but clinical cure was higher (55.7% vs 50.0%). The companion meta-analysis of 18 trials (9,108 patients) found lower 90-day mortality with prolonged infusion (RR 0.86). The 2026 Surviving Sepsis Campaign guideline now makes a strong recommendation for prolonged infusion for maintenance after a loading bolus. So ‘no distinct advantage’ is outdated (see FLAGS)."),
    ('d', "**Aminoglycosides: large once-daily dose on adjusted weight.** The goal is a high peak (Cmax/MIC 8–10) with a drug-free period before the next dose: amikacin 25–30 mg/kg in septic shock, repeated by level, not by the clock, if the kidneys fail."),
    ('e', "**TDM: established for aminoglycosides and vancomycin; useful for β-lactams in ARC.** For vancomycin, AUC-guided dosing (Bayesian) has replaced troughs. β-lactam TDM aims for 100% fT>MIC (free level 4–8 × MIC in French guidance). International position papers now recommend it in the critically ill wherever it is available, not only in ARC: on RRT, in obesity, on ECMO and for resistant organisms."),
  ],
  mimic=[
    ("Load vs maintenance in AKI", "AKI never changes the load; it lengthens the interval or lowers the maintenance. ARC is the reverse: same load, more frequent or prolonged maintenance."),
  ],
  traps=[
    ("“The loading dose of vancomycin needs to be decreased in CKD” — the DocT GT key (9% right)", "The key is wrong: the load depends on Vd, not renal function. Of the other options, reducing tobramycin in CKD and cisatracurium not being prolonged (Hofmann elimination is organ-independent) are both true, and propofol induction does not need a big cut. The bank’s pasted explanation is about morphine. Pick the true statement; know that the bank keys A."),
    ("“Standard-dose ceftolozane-tazobactam failed because of resistance induction” (51% right)", "Underdosing in the critically ill is the answer; the VAP dose is double the standard one."),
    ("“Cut the first dose because of AKI”", "Renal function changes the interval, never the load."),
    ("“Extended infusion makes no difference — BLING III was negative”", "Its primary outcome narrowly missed significance, clinical cure was better, the meta-analysis shows a mortality benefit, and SSC 2026 recommends it strongly."),
  ],
  decode=[
    ("Drug dosed for CrCl <20, CVVHD started; small, 25% bound — dose change? [DocT GT]", "Increase it (PK-08)."),
    ("Which statement on drug dosing in CKD is correct? [DocT GT]", "Keyed ‘vancomycin load decreased’ — wrong; the load is Vd-based. True: tobramycin reduction, cisatracurium unaffected."),
    ("Amikacin in septic shock — preferred strategy? [DocT GT]", "Large once-daily dose (25–30 mg/kg)."),
    ("Pseudomonas VAP, standard-dose ceftolozane-tazobactam, poor response — why? [DocT GT]", "Underdosing in the critically ill."),
  ],
  punch="Load by volume whatever the kidneys show, maintain by the clearing organ, infuse β-lactams over hours, give aminoglycosides once a day, and check with levels.",
)

FLAGS = {
  'PK-01': "Fluconazole is listed as binding to enteral feed. Its absorption through a feeding tube is well preserved in ICU patients (relative bioavailability 77% vs IV in surgical ICU patients, 1995), so it is the weakest member of the list; the evidence for feed interactions is strongest for phenytoin, ciprofloxacin, the tetracyclines and warfarin.",
  'PK-03': "Linezolid is listed as hydrophilic with renal clearance. Its Vd (40–50 L) is about total body water, not extracellular water, and about 65% of its clearance is non-renal (30% unchanged in urine), so it needs no renal dose change. It fits the ‘hydrophilic’ column only loosely.",
  'PK-04': "‘β-lactams, daptomycin: lean body weight.’ Daptomycin’s label and ACCP guidance use total (actual) body weight in obesity (adjusted weight is an alternative some use). β-lactams are not usually dosed by any weight: obese patients get the top of the dose range, often by extended infusion.",
  'PK-05': "Vancomycin is only moderately protein bound (30–60%; Ulldemolins 2011), so it sits uneasily in a list of highly bound drugs whose levels fall in hypoalbuminaemia. The highly bound examples are ceftriaxone, ertapenem, flucloxacillin, daptomycin and teicoplanin.",
  'PK-08': "‘SLED removes antibiotics more efficiently than CRRT’ holds for clearance per hour of treatment. Total daily removal depends on session length and the CRRT effluent dose, so the comparison is not absolute. The practical point is to time doses around the session.",
  'PK-10': "Vancomycin: the card gives AUC/MIC 400. The 2020 ASHP/IDSA/PIDS/SIDP consensus target is AUC₂₄/MIC 400–600 (MIC assumed 1 mg/L), with Bayesian monitoring and no trough targets. Colistin ‘AUC/MIC 53–141’ could not be verified; the 2019 polymyxin consensus target is an AUC of about 50 mg·h/L (Css,avg about 2 mg/L). Linezolid ‘40–80% fT>MIC’ is unverified (clinical data favour AUC/MIC about 80–120). Daptomycin ‘AUC/MIC 100’ is unverified; published targets vary widely and some reviews quote much higher totals for S. aureus (AUC/MIC about 666).",
  'PK-11': "‘Large RCTs show no distinct advantage, meta-analyses conflict’ is outdated. BLING III (2024) narrowly missed significance for 90-day mortality (24.9% vs 26.8%, p = 0.08) but improved clinical cure. The 2024 JAMA meta-analysis (18 RCTs, 9,108 patients) found lower 90-day mortality (RR 0.86, 95% credible interval 0.72–0.98, Bayesian). SSC 2026 gives a strong recommendation for prolonged β-lactam infusion. Also: the DocT GT CKD question keys the false statement ‘vancomycin load decreased in CKD’ (bank error, 9% right).",
}
