# SPECIAL04B — Explain v3 ("Learn" depth): pharmacokinetics of anti-infectives in the ICU — drug handling on ECMO and in burns, β-lactams and carbapenems, fluoroquinolones vs
# aminoglycosides, colistin dosing, colistin vs polymyxin B, glycopeptides and others, empirical ICU and CRRT doses, antifungal penetration and levels, true/false sweep.
# No mnemonics or hooks. Driven by the real questions in qpack/SPECIAL04B.md (7 question links: PK-18 and PK-20 twice each; PK-19, PK-21, PK-22 once; PK-12 to PK-17 never asked).
# Unasked cards get short explanations with [pattern] decode items. Fields as TOX01, plus SPINE, PRIMER and step.
# qbank.json `cards` entries for SPECIAL04B (checked 13 Nov 2026): PK-18 line (vancomycin on CRRT → TDM), PK-20 cross (C. auris lower UTI key disputed), PK-21 cross (voriconazole key wrong). No `fix` entries.
# Checked online on 13 Nov 2026:
#  - Polymyxin international consensus (Tsuji, Pharmacotherapy 2019; PMC7437259): CMS load 300 mg CBA (~9 MIU) over 0.5–1 h, first maintenance 12–24 h later; maintenance 300–360 mg CBA/day
#    (~9–10.9 MIU) in two doses with normal renal function; renal table in mg CBA/day (≥90: 360; 50–60: 245; 30–40: 195; 10–20: 160; 5–10: 145; 0: 130); target Css,avg 2 mg/L; polymyxin B load
#    2.0–2.5 mg/kg total body weight, maintenance 1.25–1.5 mg/kg 12-hourly, NO renal adjustment (also on RRT); polymyxin B preferred for systemic infection, colistin for lower UTI;
#    intraventricular CMS 125,000 IU (~4.1 mg CBA) daily, polymyxin B 5 mg daily. UNMC colistin page: maintenance starts 12 h after the load (24 h if CrCl ≤40); 2 MIU = 160 mg CMS = 60 mg CBA.
#  - Vancomycin 2020 ASHP/IDSA/PIDS/SIDP consensus (Rybak; PMC7358040 table 2): AUC/MIC 400–600 (MIC 1), trough-only 15–20 no longer recommended; load 20–35 mg/kg actual weight, max 3 g, in the
#    critically ill; maintenance 15–20 mg/kg 8–12-hourly; obese load 20–25 mg/kg actual weight, max 3 g; continuous infusion load 15–20 then 30–40 mg/kg/day; CRRT (effluent 20–25 mL/kg/h)
#    load 20–25 mg/kg, initial maintenance 7.5–10 mg/kg 12-hourly, levels within 24 h.
#  - Meropenem US label (Pfizer): in 0.9% saline for infusion stable up to 1 h at room temperature (15 h refrigerated); in water for bolus up to 3 h (13 h refrigerated).
#  - Teicoplanin UK SmPC: load 6 mg/kg 12-hourly × 3 (standard) or 12 mg/kg 12-hourly × 3–5 (bone/joint, endocarditis), then 6 or 12 mg/kg daily; renal adjustment only from day 4; not removed
#    by haemodialysis, slowly by peritoneal dialysis; half-life 100–170 h; Vss 0.7–1.4 L/kg; 88–91% bound; ~80% unchanged in urine.
#  - Azole TDM (Stanford SHC guidance): voriconazole trough 1–5.5 mg/L, toxicity above 5.5; posaconazole prophylaxis ≥0.7, treatment ≥1 mg/L, no established toxic level, some licensing
#    authorities suggest an upper limit of 3.75 mg/L; IV SBECD accumulation in renal failure of debated significance (toxicity only in animal studies); isavuconazole no routine TDM.
#  - Burns (PMC11571861, 2024 review): ebb phase first 48 h (leak, raised Vd of hydrophilic drugs, poor absorption); flow/hypermetabolic phase from about day 5 (other sources: 48–72 h) with high
#    cardiac output and raised renal and hepatic clearance; hypoalbuminaemia raises free fraction; gentamicin 7 mg/kg, tobramycin 10 mg/kg, pip-tazo 4.5 g 6-hourly over 4 h, cefepime 2 g 8-hourly
#    over 4 h, meropenem 1–2 g 8-hourly, vancomycin 40–70 mg/kg/day to AUC 400–600, linezolid 600 mg 8-hourly. Review 13 Nov: aminoglycosides reach burn eschar (Polk et al., UTMB); ANSM 2011 aminoglycosides (Cmax/MIC 8–10, genta up to 8 mg/kg);
#    EU colistin SmPC renal bands confirmed; Forrest 1993 (AUIC 125), Drusano 2004 (levofloxacin AUC/MIC ≥87); CDC C. auris page has no UTI advice.
# From standard references without a fresh check (confident unless stated): ARC = CrCl ≥130 mL/min/1.73 m²; aminoglycoside Vd ~0.25 L/kg rising to 0.35–0.5 in sepsis, Cmax/MIC 8–10, amikacin
#  25–30 mg/kg and gentamicin 5–7 mg/kg once daily; β-lactam targets (carbapenems 40% fT>MIC, penicillins 50%, cephalosporins 60–70%; 100% fT>MIC, or >4× MIC, in the critically ill); ertapenem
#  85–95% bound, half-life ~4 h; ceftriaxone 85–95% bound, dual renal/biliary; FQ AUC/MIC ≥125 Gram-negative, ~30–50 pneumococcus; levofloxacin ~85% renal unchanged; moxifloxacin hepatic,
#  avoid in severe hepatic impairment (EU SmPC); linezolid ~100% oral, ~31% bound, ~30% renal unchanged; tigecycline Vd 7–9 L/kg, 71–89% bound, biliary; azithromycin half-life ~68 h, AUC/MIC;
#  colistin plasma half-life ~14 h in the critically ill (Plachouras 2009); polymyxins differ by one amino acid (D-Phe in PMB, D-Leu in colistin); ECMO sequestration of lipophilic (logP >2)
#  and highly protein-bound drugs (Shekar); fluconazole ~80% renal unchanged, CSF ~70–80% of serum; voriconazole <2% unchanged in urine; isavuconazole 200 mg 8-hourly × 6 then daily, >99% bound;
#  IDSA 2016 Candida cystitis: fluconazole, or amphotericin B deoxycholate 0.3–0.6 mg/kg ± flucytosine for resistant species; daptomycin 6 mg/kg (8–10 for complicated), 48-hourly at CrCl <30/HD.
#  Less sure: the card’s amphotericin and echinocandin Cmax/MIC figures; EMA colistin renal bands (CrCl 30–50 5.5–7.5 MU/day, 10–30 4.5–5.5, <10 3.5) quoted from memory.

SPINE = [
  ("Load by volume, maintain by clearance", "The loading dose depends only on the volume of distribution, which sepsis enlarges, and the maintenance dose on clearance, which AKI lowers and augmented renal clearance raises, so a sick patient needs a full or bigger load even when his kidneys have failed."),
  ("ECMO and burns stretch both", "ECMO priming and burn leak swell the volume, the circuit soaks up lipophilic drugs, and the hyperdynamic burn patient clears drugs fast, so standard doses run low and levels guide the rest."),
  ("β-lactams: time above the MIC", "β-lactams kill by the time the free level stays above the MIC, so in the ICU they are loaded and then given as extended or continuous infusions, more often when clearance is augmented."),
  ("Concentration killers: aminoglycosides and polymyxins", "Aminoglycosides and polymyxins kill by how high the level goes, so they are given as one large dose that ignores renal function, and only the later doses or interval are cut."),
  ("Gram-positive drugs and the ICU dose table", "Vancomycin is dosed on actual weight to an AUC of 400–600 with a load and then levels, while linezolid, tigecycline and teicoplanin each have one kinetic quirk that the exam asks."),
  ("Antifungals: where they go, what level", "Fluconazole reaches urine, eye and CSF, echinocandins reach none of them, and voriconazole and posaconazole are dosed to trough levels with oral routes preferred in renal failure."),
]

PRIMER = "Volume of distribution (Vd) is the apparent volume a drug spreads into: hydrophilic drugs (β-lactams, aminoglycosides, glycopeptides, polymyxins) stay in plasma and interstitial water, so their Vd swells with fluid and capillary leak, while lipophilic drugs (fluoroquinolones, linezolid, tigecycline, azoles) spread into cells and fat. The loading dose is Vd × target concentration and does not depend on the kidneys; the maintenance dose is clearance × target, so renal failure changes only the later doses. Each antimicrobial kills by one PK/PD index: time the free level spends above the MIC (fT>MIC, β-lactams), the peak over the MIC (Cmax/MIC, aminoglycosides), or the area under the curve over the MIC (AUC/MIC, vancomycin, fluoroquinolones, polymyxins, linezolid). Augmented renal clearance (ARC) means a creatinine clearance of 130 mL/min/1.73 m² or more, common in young trauma, burn and sepsis patients."

L = {}

L['PK-12'] = dict(
  sub="Pharmacology → Special circuits → Drug handling on ECMO",
  step=2,
  intro="Step 2 takes the rule of step 1 to its extreme. The ECMO circuit adds litres of priming fluid, and its tubing and oxygenator bind some drugs, while the patient is septic, hypoalbuminaemic and often in organ failure. The card lists four forces and what each does to the dose; no real question is linked, so this is the short version.",
  parts=[
    ('a', "**Priming and haemodilution: ↑ Vd of hydrophilic drugs (β-lactams, aminoglycosides) → bigger load.** The circuit is primed with crystalloid, colloid or blood and adds this to the patient’s plasma volume at once, so a drug that stays in body water is diluted and its first peak is low. The fix is a larger first dose; clearance is unchanged by the prime itself."),
    ('b', "**Circuit sequestration: lipophilic drugs (fluoroquinolones, fentanyl, midazolam, propofol) are bound and lost → bigger load, more often.** Lipophilic and highly protein-bound drugs stick to the PVC tubing and the oxygenator membrane until binding sites saturate, which acts as a large extra volume and keeps removing drug from the blood. Voriconazole behaves the same way. How much is lost varies with the circuit materials and falls as binding sites saturate, so sedative needs often rise early and the dose has to be retitrated later."),
    ('c', "**Low albumin: ↑ free fraction of highly bound drugs (teicoplanin, ceftriaxone) → load, give more often.** With less albumin more drug is unbound; unbound drug is both active and the part the kidney can filter, so it is cleared faster and the total level falls between doses. The free fraction, not the total, sits above or below the MIC."),
    ('d', "**Sepsis and organ failure: ↑ Vd and ↓ clearance of hydrophilic, renal or hepatic drugs → load, then stretch the interval.** Capillary leak enlarges Vd, so the load is still full or larger; AKI or liver failure slows elimination, so it is the interval or the maintenance dose that is reduced, guided by levels where they exist (vancomycin, aminoglycosides)."),
  ],
  mimic=[
    ("Sequestration vs haemodilution", "Haemodilution affects hydrophilic drugs and is a one-off fall at the start of the circuit. Sequestration affects lipophilic or highly bound drugs and keeps removing drug until the circuit saturates."),
    ("ECMO vs CRRT drug loss", "CRRT removes small, unbound, hydrophilic drugs by filtration; ECMO adsorbs lipophilic drugs. A patient on both can lose both kinds."),
  ],
  traps=[
    ("“Hydrophilic drugs bind to the ECMO circuit”", "Sequestration is a property of lipophilic and highly protein-bound drugs (PK-22 i); hydrophilic drugs are affected by dilution, not binding."),
    ("“Reduce the load because the patient is in renal failure on ECMO”", "The load follows Vd, which is larger; only the maintenance follows clearance."),
  ],
  decode=[
    ("[pattern] Which drug is most sequestered by the ECMO circuit — fentanyl, gentamicin, meropenem, vancomycin?", "Fentanyl: lipophilic and highly bound."),
    ("[pattern] Patient on VA-ECMO needs ever-higher midazolam and fentanyl in the first days — why?", "Circuit sequestration of lipophilic drugs, on top of raised Vd."),
  ],
  punch="On ECMO, hydrophilic drugs are diluted and lipophilic ones are soaked up by the circuit, so both need a bigger first dose; organ failure changes only how often the next doses come.",
)

L['PK-13'] = dict(
  sub="Pharmacology → Special circuits → Antibiotics in burns",
  step=2,
  intro="Still step 2: a major burn changes kinetics twice. In the first two days the patient is in burn shock with a leak and a low GFR; after that he becomes hyperdynamic and clears drugs faster than almost any other ICU patient. No real question is linked; the point to carry is that standard doses usually run low after the first two days.",
  parts=[
    ('a', "**Early (first 48 h): hypovolaemia, low albumin, low GFR. Late (after 48–72 h): hyperdynamic, raised cardiac output, high renal and non-renal clearance, low albumin, liver dysfunction.** In the ebb phase capillary leak and large volumes of resuscitation fluid raise the Vd of hydrophilic drugs while poor perfusion lowers renal clearance. In the flow (hypermetabolic) phase cardiac output and renal and hepatic blood flow rise and ARC is common, so drugs are cleared fast; reviews date its onset from 48–72 h to about day 5, and it can persist for months, in large burns for a year or more. The low albumin persists throughout."),
    ('b', "**Highly bound drugs (ertapenem, daptomycin, ceftriaxone, oxacillin): high free levels, fast clearance → subtherapeutic.** Without albumin, more of the dose is free, so more is filtered and cleared quickly; the free level is briefly high and then falls below the MIC well before the next dose. Once-daily highly bound drugs such as ertapenem and ceftriaxone are the ones most at risk of running out before the next dose."),
    ('c', "**Aminoglycosides penetrate eschar well; usual β-lactam doses inadequate.** Aminoglycosides are small, water-soluble molecules that diffuse through the oedematous interstitium; biopsies of burn eschar in patients on gentamicin or tobramycin found measurable tissue levels in every patient, with an effect on the eschar flora. They are still dosed by weight with peak and trough levels, often at gentamicin 7 mg/kg or tobramycin 10 mg/kg daily and sometimes more often, because clearance is high. For β-lactams the fix is the top of the dose range given as extended infusions (piperacillin–tazobactam 4.5 g 6-hourly over 4 h, cefepime 2 g 8-hourly, meropenem 1–2 g 8-hourly)."),
    ('d', "**Vancomycin: ↑ Vd and clearance; standard doses rarely hit targets → TDM. Higher linezolid and colistin doses.** Burn patients often need 40–70 mg/kg/day of vancomycin to reach an AUC of 400–600, so it is given after a load with early levels; linezolid is commonly given 8-hourly instead of 12-hourly."),
  ],
  mimic=[
    ("Early vs late burn phase", "Early: leak, low GFR, raised Vd, normal or slow clearance. Late: hyperdynamic, ARC, fast clearance. Both have low albumin."),
  ],
  traps=[
    ("“Burn patients need lower doses because of renal hypoperfusion”", "Only in the first 48 h; afterwards clearance is high and standard doses fail."),
    ("“A high free fraction means toxicity, so reduce highly bound antibiotics”", "For renally cleared antibiotics the extra free drug is cleared quickly and levels end up low; the toxicity concern applies to narrow-window drugs such as phenytoin."),
  ],
  decode=[
    ("[pattern] Day 7 after a 50% burn, vancomycin troughs low on standard dosing — why?", "Hyperdynamic phase with augmented renal clearance and raised Vd; increase the dose and dose to levels."),
  ],
  punch="After the first two days a burn patient clears antibiotics fast, so give the top doses as extended infusions and dose vancomycin and aminoglycosides by levels.",
)

L['PK-14'] = dict(
  sub="Pharmacology → Antibacterials → β-lactams and carbapenems",
  step=3,
  intro="Step 3 is the time-dependent drugs. β-lactams kill only while the free level stays above the MIC, and peaks above about 4–5 times the MIC add nothing, so the question is always how to keep the level up between doses in a patient whose Vd and clearance are both raised. No real question is linked to this card.",
  parts=[
    ('a', "**Hydrophilic, low Vd (0.1–0.6 L/kg in your notes), doubled in the critically ill; mainly renal clearance (ceftriaxone is biliary).** In healthy people most β-lactams have a Vd of about 0.2–0.3 L/kg, the extracellular water; leak and fluid can double it, so the first dose must be full. Most are filtered and secreted by the kidney, so they need maintenance changes in AKI and run low with ARC. Piperacillin–tazobactam is mostly renal with some biliary excretion and still needs renal adjustment; ceftriaxone is cleared by both bile and kidney and needs no renal adjustment."),
    ('b', "**Moderate protein binding (20–50%) for most.** The exceptions are the highly bound ones: ceftriaxone and ertapenem (85–95%), oxacillin and flucloxacillin (about 90–95%) and cefazolin (about 80%). For these, low albumin raises clearance and shortens the time above the MIC (PK-13 b)."),
    ('c', "**Carbapenems: half-life about 1 h, low protein binding (2–20%). Ertapenem: 95% bound, half-life 4 h (once daily).** Meropenem is about 2% bound and imipenem about 20%, so their short half-lives require 8-hourly (meropenem) or 6-hourly (imipenem) dosing. Ertapenem’s binding gives it a long half-life and once-daily dosing, but it also makes it the carbapenem most likely to fail in hypoalbuminaemia, and it does not cover Pseudomonas or Acinetobacter."),
    ('d', "**Reconstituted meropenem and imipenem are stable only 1–4** hours at room temperature, so a single bag cannot run for 24 hours. The US meropenem label allows 1 hour at room temperature once diluted in saline for infusion and 3 hours in water for a bolus; imipenem in saline lasts about 4 hours."),
    ('h', "**h at room temperature: infuse within 1–3 h.** This is why carbapenems are given as 3-hour extended infusions (prepared freshly for each dose) rather than continuous infusions; piperacillin–tazobactam and cefepime are more stable and can run continuously. The watch line gives the target: about 40% of the dosing interval with the free level above the MIC for carbapenems (50% for penicillins, 60–70% for cephalosporins), and in the critically ill or with MDR organisms 100% fT>MIC, with maximal killing at 4–5 × MIC."),
  ],
  mimic=[
    ("Meropenem vs ertapenem", "Meropenem: 2% bound, half-life 1 h, 8-hourly, covers Pseudomonas. Ertapenem: about 95% bound, half-life 4 h, once daily, no Pseudomonas or Acinetobacter cover."),
    ("Extended vs continuous infusion", "Extended (3–4 h) suits unstable drugs such as meropenem; continuous suits stable ones such as piperacillin–tazobactam. Both always start with a loading dose."),
  ],
  traps=[
    ("“Ceftriaxone needs renal dose reduction”", "It is cleared by bile as well as kidney; no renal adjustment."),
    ("“Run meropenem as a 24-hour continuous infusion from one bag”", "It degrades within hours at room temperature; use 3-hour infusions or bags changed every few hours."),
  ],
  decode=[
    ("[pattern] Which carbapenem is once daily and why? Which one fails in severe hypoalbuminaemia?", "Ertapenem, because it is about 95% protein bound (half-life 4 h); the same binding makes its free level fall fast when albumin is low."),
    ("[pattern] PK/PD target of meropenem?", "Time above the MIC: 40% fT>MIC, 100% in the critically ill."),
  ],
  punch="β-lactams are hydrophilic, renally cleared and time-dependent: load fully, then keep the free level above the MIC with extended infusions, remembering that meropenem lasts only an hour or two in the bag.",
)

L['PK-15'] = dict(
  sub="Pharmacology → Antibacterials → Fluoroquinolones vs aminoglycosides",
  step=4,
  intro="Step 4 is the concentration-dependent drugs, and this card sets the two classes side by side: one lipophilic and orally available, one hydrophilic and needing levels. No real question is linked; PK-22 b and h and PK-19 a carry the asked points about aminoglycosides.",
  parts=[
    ('a', "**Nature: fluoroquinolones lipophilic, large Vd, oral 70–90% bioavailable; aminoglycosides hydrophilic.** Fluoroquinolones enter cells and tissues, so lung and prostate levels exceed plasma, and the oral dose gives levels close to IV (levofloxacin and moxifloxacin almost 100%). The card’s ‘aminoglycosides penetrate tissues well’ is only partly right: they reach the interstitial fluid of well-perfused tissues and even burn eschar, but they stay in extracellular water (Vd about 0.25 L/kg), barely enter cells, reach lung epithelial lining fluid, CSF and bone poorly, and are inactivated in acidic, anaerobic pus, which is why they are nebulised for pneumonia or given intraventricularly for ventriculitis."),
    ('b', "**Clearance: ciprofloxacin and levofloxacin renal unchanged; moxifloxacin hepatic, no renal adjustment. Aminoglycosides renal; half-life 1.5–3.5 h.** Levofloxacin is about 85% excreted unchanged, so its dose falls in AKI; ciprofloxacin is partly renal. Moxifloxacin needs no renal change but is avoided in severe liver failure. Aminoglycosides are filtered unchanged, so their half-life lengthens in step with falling GFR."),
    ('c', "**Killing: both concentration-dependent; fluoroquinolones by AUC/MIC; aminoglycosides with a post-antibiotic effect and synergy with cell-wall drugs.** The post-antibiotic effect means bacterial growth stays suppressed for hours after the level falls below the MIC, which is what makes once-daily dosing work. β-lactams and glycopeptides damage the wall and let the aminoglycoside in, hence the synergy used in enterococcal endocarditis."),
    ('d', "**Key ratio: fluoroquinolone AUC/MIC over 87.5–125; aminoglycosides AUC/MIC for Enterobacterales, peak/MIC for Pseudomonas.** For Gram-negatives the classic fluoroquinolone target is an AUC24/MIC of 125 or more (ciprofloxacin in seriously ill patients, Forrest 1993), and about 87 or more predicted eradication with levofloxacin in nosocomial pneumonia (Drusano 2004), which is where the lower figure comes from; for pneumococcus about 30–40 is enough. For aminoglycosides the standard target is a peak (Cmax) of 8–10 times the MIC, with AUC/MIC used by some dosing programmes; the split by organism is the notes’ framing."),
    ('e', "**TDM: yes for aminoglycosides, especially in renal dysfunction.** A peak (after the first dose) checks efficacy and a trough or a timed level guides the interval; a high trough means drug is building up in the renal cortex and inner ear. Fluoroquinolones are not routinely monitored."),
  ],
  mimic=[
    ("Levofloxacin vs moxifloxacin", "Levofloxacin: renal, reduce in AKI, covers Pseudomonas. Moxifloxacin: hepatic, no renal change, poor urine levels and no Pseudomonas cover."),
  ],
  traps=[
    ("“Aminoglycosides penetrate tissues well”", "They are hydrophilic and penetrate lung, CSF and abscesses poorly; this is a card statement to unlearn (FLAGS)."),
    ("“Moxifloxacin for a urinary infection in AKI”", "No renal adjustment, but also little reaches the urine."),
  ],
  decode=[
    ("[pattern] Which fluoroquinolone needs no renal dose adjustment?", "Moxifloxacin."),
    ("[pattern] Why can aminoglycosides be given once daily?", "Concentration-dependent killing plus a post-antibiotic effect, with less cortical uptake when the trough is low."),
  ],
  punch="Fluoroquinolones are lipophilic and oral, aminoglycosides hydrophilic and monitored; both kill by concentration, and the aminoglycoside’s post-antibiotic effect is what allows one big daily dose.",
)

L['PK-16'] = dict(
  sub="Pharmacology → Antibacterials → Colistin dosing",
  step=4,
  intro="Still step 4: colistin is the concentration-dependent drug with the most awkward kinetics. It is given as an inactive prodrug that converts slowly, so without a load the active drug sits below target for two to three days, the very days a carbapenem-resistant infection kills. No real question is linked, but PK-22 a tests the load.",
  parts=[
    ('a', "**Given as colistimethate (CMS), an inactive prodrug; peak colistin about 7 h after a dose; half-life 14 h → steady state takes 2–3 days without a load; about 60% protein bound.** CMS is cleared mainly by the kidney, and only the part that is not excreted hydrolyses to active colistin. The 2019 consensus quotes colistin protein binding as about 50%, a little below the card’s 60%. Five half-lives of 14 hours is about 3 days, which is why the load matters. Doses are written in million units (MU) of CMS or mg of colistin base activity (CBA): 1 MU is about 30–33 mg CBA, so 9 MU is roughly 300 mg CBA."),
    ('b', "**Poor penetration into lung, CSF, bone, pleura → nebulise (intrathecal for CNS).** Colistin is a large polycationic molecule, so systemic levels in alveolar fluid and CSF are low. Nebulised CMS is added for XDR ventilator pneumonia (a weak consensus recommendation; ESCMID advises against routine nebulised antibiotics), and for ventriculitis CMS is given intraventricularly (consensus about 125,000 IU, roughly 4 mg CBA, daily) alongside IV dosing."),
    ('c', "**PD index: fAUC/MIC.** The consensus target is an average steady-state plasma colistin of about 2 mg/L. Above that, nephrotoxicity becomes more likely, so the therapeutic window is narrow."),
    ('d', "**Loading 9 MU (9–12 MU by ideal weight; 12 MU for 70 kg), independent of renal function.** The 2019 international consensus gives a fixed load of 300 mg CBA, about 9 MU, infused over 30–60 minutes. The older weight-based formula (with ideal or actual weight, whichever is lower) gives about 280 mg CBA, roughly 9 MU, for 70 kg, so the card’s 12 MU for 70 kg is higher than either source. What is asked is the rule: the load fills Vd, so it is never reduced in AKI (PK-22 a)."),
    ('e', "**4.5 MU every 12 h, starting 24 h after the load (consensus 12–24 h); cut by eGFR (30–60: 3 MU; 10–30: 2 MU; under 10: 1 MU, every 12 h).** 4.5 MU 12-hourly is the European label dose of 9 MU a day; the consensus gives 300–360 mg CBA (9–10.9 MU) a day in two doses, with the first maintenance dose 12–24 hours after the load (12 h with normal kidneys). In renal failure the consensus reductions are smaller than the card’s: about 195 mg CBA (roughly 6 MU) a day at CrCl 30–40, 160 mg (about 5 MU) at 10–20, and about 130–145 mg (about 4 MU) under 10, so the card’s 2 MU a day under 10 would under-dose. The European label’s bands are similar: 5.5–7.5 MU a day at CrCl 30–50, 4.5–5.5 MU at 10–30 and 3.5 MU under 10, so both sources give more than the card at the bottom. CRRT removes CMS and colistin, so patients on CRRT need more than the anuric dose: the consensus gives 440 mg CBA (about 13 MU) a day, 220 mg 12-hourly."),
  ],
  mimic=[
    ("CMS dose units", "MU (million units of CMS) and mg CBA are different scales: 9 MU ≈ 300 mg CBA ≈ 720 mg CMS. Confusing them gives a two- to three-fold error."),
  ],
  traps=[
    ("“Halve the colistin load in AKI”", "The load depends on Vd, not on the kidneys (PK-22 a)."),
    ("“Start maintenance straight after the load”", "The first maintenance dose comes 12–24 h later, at the usual interval."),
  ],
  decode=[
    ("[pattern] Colistin loading dose for a 70 kg patient with CRAB pneumonia and creatinine 3?", "9 MU (300 mg CBA), whatever the renal function; maintenance reduced for CrCl, nebulised CMS added."),
    ("[pattern] Why give a loading dose of colistin?", "CMS is a slowly converting prodrug and colistin’s half-life is about 14 h, so without a load the level is subtherapeutic for 2–3 days."),
  ],
  punch="Colistin is a slow prodrug, so load 9 MU (300 mg CBA) whatever the kidneys do, start maintenance 12–24 hours later, and cut only the maintenance for renal failure.",
)

L['PK-17'] = dict(
  sub="Pharmacology → Antibacterials → Colistin vs polymyxin B",
  step=4,
  intro="Step 4 again: the two polymyxins are almost the same molecule (they differ by one amino acid) but reach the body in opposite ways. Colistin arrives as a prodrug cleared by the kidney; polymyxin B arrives active and is barely excreted in urine. That single difference decides which one to use where. No real question is linked.",
  parts=[
    ('a', "**Form: colistin as a prodrug (CMS → colistin); polymyxin B as the active drug.** Polymyxin B reaches target levels quickly after a load and its plasma levels are predictable; CMS converts slowly and variably."),
    ('b', "**Renal handling: CMS cleared by the kidneys → high urine levels; polymyxin B undergoes tubular reabsorption → low urine levels, no renal adjustment.** Because most CMS is filtered into the urine and converts there, the bladder sees high colistin levels. Polymyxin B is cleared mainly by non-renal routes, so the 2019 consensus doses it on total body weight (load 2–2.5 mg/kg, then 1.25–1.5 mg/kg 12-hourly) with no change for renal failure or RRT."),
    ('c', "**Plasma levels: colistin slow and variable; polymyxin B predictable.** This is why polymyxin B is preferred when the blood level is what matters."),
    ('d', "**Toxicity: colistin more nephrotoxic; polymyxin B less nephrotoxic, with neurotoxicity and skin pigmentation.** Both damage the proximal tubule and can cause paraesthesia and neuromuscular blockade; observational data favour polymyxin B for renal toxicity. Skin hyperpigmentation is a polymyxin B effect."),
    ('e', "**Best for: colistin for urinary infection; polymyxin B for systemic infection (bloodstream, pneumonia).** This is the consensus recommendation, and it follows directly from row b."),
  ],
  mimic=[
    ("Colistin vs polymyxin B in a CRE urinary infection", "Colistin: high urine levels. Polymyxin B: little reaches the urine."),
  ],
  traps=[
    ("“Polymyxin B needs renal dose reduction like colistin”", "It is not renally cleared; consensus gives no adjustment, even on dialysis."),
    ("“Polymyxin B for a lower urinary tract infection”", "Its urine levels are low; colistin is the polymyxin for the bladder."),
  ],
  decode=[
    ("[pattern] Which polymyxin for CRE pyelonephritis, and which for CRAB bacteraemia?", "Colistin (CMS) for the urine; polymyxin B for the blood."),
  ],
  punch="Colistin is a kidney-cleared prodrug, so it suits the urine and needs renal adjustment; polymyxin B is active, non-renally cleared and predictable, so it suits blood and lung and is never renally reduced.",
)

L['PK-18'] = dict(
  sub="Pharmacology → Antibacterials → Glycopeptides, tigecycline, linezolid, azithromycin",
  step=5,
  intro="Step 5 is the Gram-positive drugs. Each has one kinetic fact that the exam turns into a question: vancomycin is renally cleared and dosed to levels, teicoplanin has a very long half-life, tigecycline lives in tissue rather than blood, and linezolid needs no renal change. Both real questions are about the renally impaired patient, and one of them shows how that last fact misleads.",
  parts=[
    ('a', "**Vancomycin: Vd 0.4–0.9 L/kg; 80–90% renal unchanged; half-life 4–6 h; AUC/MIC 400; obese: actual weight; load 25–30 mg/kg; CVVHD every 36–48 h.** Vancomycin is filtered unchanged, so its clearance tracks creatinine clearance; with ARC levels run low, in AKI they accumulate. The 2020 consensus targets an AUC/MIC of 400–600 (MIC 1) and no longer uses a trough of 15–20 alone. The load is 20–35 mg/kg of actual body weight (max 3 g) in the critically ill, 20–25 mg/kg in obesity, then 15–20 mg/kg 8–12-hourly. On CRRT (effluent 20–25 mL/kg/h) the consensus gives a load of 20–25 mg/kg and 7.5–10 mg/kg 12-hourly, with levels within 24 h; the card’s 36–48-hourly interval belongs to older, low-intensity CRRT. On intermittent haemodialysis it is given after each session, aiming for a pre-dialysis level of 15–20 mg/L."),
    ('b', "**Teicoplanin: Vd 0.9–1.4; half-life about 150 h (14 days to steady state); load 12 mg/kg 12-hourly × 3–5, then 12 mg/kg daily (CRRT 6); glomerular filtration; not removed by HD or CAPD.** Teicoplanin is about 90% albumin bound, which gives it its very long half-life (100–170 h). Without a load it would take two weeks to reach steady state, so it is loaded 12-hourly (6 mg/kg × 3 for ordinary infections, 12 mg/kg × 3–5 for bone, joint and endocarditis). Renal adjustment starts only from day 4, and haemodialysis does not remove it."),
    ('c', "**Tigecycline: lipophilic, Vd 7–10 L/kg; biliary; about 80% bound; AUC/MIC; low serum levels → higher doses.** It moves into tissue so completely that blood levels are low, which is why it is a poor choice for bacteraemia and why a 200 mg load and 100 mg 12-hourly are used for MDR infections. Biliary elimination means no renal adjustment."),
    ('d', "**Linezolid: oral about 100%; 30% bound; 30% renal, 70% metabolised; no renal adjustment; AUC/MIC.** Oral and IV doses are interchangeable. Its metabolites accumulate in renal failure (more thrombocytopenia), but the dose is not changed. It is bacteriostatic against staphylococci, which matters for bacteraemia."),
    ('e', "**Azithromycin: long half-life (about 64–68 h); once daily; macrolides Cmax/MIC (notes).** The long half-life comes from huge uptake into cells, which allows once-daily dosing and short courses. Its PK/PD index is usually given as AUC/MIC rather than Cmax/MIC; older teaching classes erythromycin and clarithromycin as time-dependent."),
  ],
  table=dict(title="MRSA bacteraemia in a patient on haemodialysis", head=["Drug", "Role", "How to dose"], rows=[
    ["Vancomycin", "**first line**", "load by actual weight, then after each session to a pre-dialysis level of 15–20 mg/L"],
    ["Daptomycin", "**first line** (alternative)", "6 mg/kg (8–10 if complicated) every 48 h, after dialysis"],
    ["Linezolid", "salvage or step-down", "no change, but bacteriostatic"],
    ["Ceftaroline", "salvage, often with daptomycin", "renally adjusted"],
  ]),
  mimic=[
    ("Vancomycin vs teicoplanin", "Vancomycin: half-life 4–6 h, dosed to AUC, removed by high-flux dialysis and CRRT. Teicoplanin: half-life 4–7 days, 12-hourly loading, not removed by haemodialysis."),
    ("Tigecycline vs linezolid", "Both need no renal change. Tigecycline: tissue drug with low blood levels, biliary. Linezolid: full oral bioavailability, good blood and lung levels."),
  ],
  traps=[
    ("“Linezolid” keyed for MRSA CLABSI with septic shock on haemodialysis (49% right)", "The key is disputed. Its only advantage is no renal adjustment; it is bacteriostatic and IDSA guidance makes vancomycin or daptomycin first line for MRSA bacteraemia, with renal failure handled by dosing vancomycin to levels or daptomycin 48-hourly. The AVERT trial in the stem is irrelevant. Pick linezolid only if neither vancomycin nor daptomycin is offered."),
    ("“De-escalate” or “rapid diagnostics” for low vancomycin levels on CRRT", "A low level is a dosing problem: therapeutic drug monitoring with AUC-guided dosing (82% right)."),
    ("“Dose vancomycin on ideal body weight in obesity”", "Actual weight, with the load capped at 3 g (PK-22 d)."),
  ],
  decode=[
    ("ICU patient on CRRT, subtherapeutic vancomycin despite standard dosing — which stewardship strategy? [DocT GT]", "Therapeutic drug monitoring (82%): AUC-guided dosing to 400–600 after a load, adjusted for effluent rate."),
    ("AKI on haemodialysis, MRSA CLABSI, septic shock — initial therapy? [DocT QBank]", "Keyed linezolid (49%); by guideline, vancomycin (load, then to levels) or daptomycin (48-hourly)."),
    ("[pattern] Which glycopeptide is not removed by haemodialysis and needs 12-hourly loading?", "Teicoplanin."),
  ],
  punch="Vancomycin is renally cleared, so load on actual weight and dose to an AUC of 400–600 with levels, especially on CRRT; ‘no renal adjustment’ makes linezolid convenient but not the first choice for MRSA bacteraemia.",
)

L['PK-19'] = dict(
  sub="Pharmacology → Antibacterials → Empirical ICU and CRRT doses",
  step=5,
  intro="Step 5 ends with the dose table, where steps 1, 3 and 4 become numbers. Two rules run through it: the first dose is the same or bigger in the critically ill whatever the kidneys, and on CRRT only the maintenance falls. The one real question asks how amikacin is given in septic shock.",
  parts=[
    ('a', "**Amikacin: 25–30 mg/kg once, then TDM; CRRT 12–15 mg/kg, interval by TDM.** A single large dose gives a peak of 8–10 times the MIC (about 60–80 mg/L), uses the post-antibiotic effect, and lets the trough fall low, which reduces uptake into the renal cortex and inner ear. Sepsis raises Vd, so the critically ill need the top of the range on actual weight (adjusted weight if obese). Your notes print 30 mg/kg."),
    ('b', "**Gentamicin: 7–10 mg/kg; CRRT 3–4 mg/kg, then TDM.** Extended-interval gentamicin is usually 5–7 mg/kg, with 7 mg/kg the common ICU and burn dose; French guidance allows up to 8 mg/kg in severe sepsis, aiming at a peak of 30–40 mg/L (8–10 times the MIC). The card’s 10 mg/kg is above these recommendations, so a peak level after the first dose is essential."),
    ('c', "**Meropenem: 1 g load, then 1 g 8-hourly as extended or continuous infusion (ARC: 6–8-hourly); CRRT 0.5–1 g 8–12-hourly.** 2 g 8-hourly is used for Pseudomonas with high MICs and for meningitis. Stability limits continuous infusion (PK-14 d)."),
    ('d', "**Piperacillin–tazobactam: 4.5 g load, then 4.5 g 6-hourly (ARC: 4–6-hourly); CRRT 4.5 g 8-hourly.** Given as extended (over 3–4 h) or continuous infusion after the load."),
    ('e', "**Cefepime: 2 g load, then 2 g 8-hourly (ARC 6–8); CRRT 1–2 g 12-hourly.** Cefepime accumulates in renal failure and causes encephalopathy and non-convulsive status, so the renal adjustment matters more than for other β-lactams."),
    ('f', "**Ciprofloxacin 400 mg 8-hourly, levofloxacin 750 mg daily, moxifloxacin 400 mg daily; CRRT ciprofloxacin 400 mg 12-hourly.** Moxifloxacin is unchanged on CRRT (hepatic, PK-15 b)."),
    ('g', "**Vancomycin: load 25–30 mg/kg, then 15–20 mg/kg 8–12-hourly; CRRT 20 mg/kg load, then 10–15 mg/kg 24–48-hourly.** The 2020 consensus gives 20–35 mg/kg (max 3 g) as the load and, on CRRT at effluent 20–25 mL/kg/h, 7.5–10 mg/kg 12-hourly to levels; the card’s 24–48-hourly interval under-doses modern CRRT (PK-18 a)."),
    ('h', "**Daptomycin: 10–12 mg/kg; CRRT 8 mg/kg 24–48-hourly.** Licensed doses are 4–6 mg/kg; 8–12 mg/kg is used for bacteraemia, endocarditis and in the critically ill. It is inactivated by surfactant, so never for pneumonia; check creatine kinase weekly."),
    ('i', "**Linezolid: 600 mg 8–12-hourly; usual on CRRT.** 600 mg 12-hourly is standard; 8-hourly is used with ARC, burns or obesity."),
  ],
  mimic=[
    ("What changes on CRRT", "Unchanged: β-lactam and vancomycin loads, linezolid, moxifloxacin. Reduced: β-lactam maintenance, aminoglycoside doses and intervals, vancomycin maintenance, ciprofloxacin."),
  ],
  traps=[
    ("“Divide amikacin into 5 mg/kg three times a day” or “continuous infusion at 10 µg/mL”", "Both throw away the peak that drives killing and raise the trough that drives toxicity; amikacin is given once daily at 25–30 mg/kg."),
    ("“Avoid aminoglycosides in sepsis because ATN is certain”", "A short once-daily course with level monitoring has a modest risk; the absolute wording is the giveaway."),
  ],
  decode=[
    ("Septic shock, 70 kg, amikacin in combination — preferred dosing in the acute phase? [DocT GT]", "One large daily dose of 25–30 mg/kg to maximise Cmax/MIC."),
    ("[pattern] Which antibiotic dose is NOT changed on CRRT?", "The loading dose of any of them; for maintenance, linezolid and moxifloxacin."),
  ],
  punch="In the septic patient the first dose is always full: amikacin 25–30 mg/kg once, vancomycin 20–35 mg/kg, β-lactams at full dose; CRRT trims only the doses that follow.",
)

L['PK-20'] = dict(
  sub="Pharmacology → Antifungals → Antifungal penetration",
  step=6,
  intro="Step 6 is the antifungals, and the first question is always where the drug goes. Choosing an antifungal for Candida in the urine, eye or brain is a penetration question before it is a spectrum question. Both real questions are Candida in the bladder, and the second key is disputed.",
  parts=[
    ('a', "**Fluconazole: nearly everywhere — CSF, eye, urine.** It is small, water-soluble and poorly protein bound, and about 80% is excreted unchanged in the urine, so bladder levels are many times the MIC; CSF and vitreous levels are about 70–80% of serum. It is the drug of choice for susceptible Candida cystitis and pyelonephritis, and the step-down for Candida endophthalmitis and meningitis."),
    ('b', "**Voriconazole: not into urine.** It is metabolised in the liver and less than 2% appears unchanged in urine, so it does not treat Candida UTI, although it does reach the eye and CNS well."),
    ('c', "**Echinocandins: poor in urine, CSF and vitreous.** They are large, highly protein-bound molecules cleared by slow non-renal degradation, so very little reaches the urine, CSF or eye. They are first line for candidaemia but should not be relied on for cystitis, endophthalmitis or meningitis."),
    ('d', "**Liposomal amphotericin: high serum and CNS levels.** The liposome gives high blood levels and good brain tissue levels (it is used for cryptococcal meningitis and CNS candidiasis), though CSF levels themselves are low. Liposomal amphotericin reaches the urine poorly; for Candida cystitis by a fluconazole-resistant species the IDSA choice is amphotericin B deoxycholate (0.3–0.6 mg/kg, with or without bladder irrigation) or flucytosine."),
  ],
  table=dict(title="Candida site and drug", head=["Site", "Use", "Avoid"], rows=[
    ["Bladder or kidney, susceptible", "**fluconazole**", "echinocandin, voriconazole"],
    ["Bladder, fluconazole-resistant (C. glabrata, C. krusei; by extension C. auris)", "**amphotericin B deoxycholate** or flucytosine", "echinocandin (low urine levels)"],
    ["Bloodstream", "**echinocandin**", ""],
    ["Eye or CNS", "liposomal amphotericin ± flucytosine, then fluconazole or voriconazole", "echinocandin"],
  ]),
  mimic=[
    ("Liposomal vs deoxycholate amphotericin", "Liposomal: less nephrotoxic, better tissue and CNS levels, poor urine levels. Deoxycholate: reaches the urine, so it is the amphotericin for resistant Candida cystitis."),
  ],
  traps=[
    ("“Caspofungin” for symptomatic Candida UTI", "Echinocandins barely reach the urine; fluconazole is the answer."),
    ("“Anidulafungin” keyed for lower UTI by C. auris (82% chose it)", "The key is disputed: an echinocandin reaches the bladder poorly, and IDSA 2016 advises amphotericin B deoxycholate (± bladder irrigation) or flucytosine for fluconazole-resistant Candida cystitis; it was written for C. glabrata and C. krusei and is applied to C. auris by extension. CDC’s echinocandin-first advice is for invasive C. auris, gives nothing specific for the bladder, and advises against treating C. auris in urine without symptoms. If amphotericin is offered for a symptomatic bladder infection, pick it, after checking susceptibility, since some C. auris isolates resist amphotericin."),
    ("“Voriconazole” for Candida UTI", "It is not excreted unchanged in urine."),
  ],
  decode=[
    ("ICU patient, symptomatic Candida UTI, no fungus ball or abscess — agent with high urinary concentrations? [DocT GT]", "Fluconazole."),
    ("Drug of choice for lower UTI by Candida auris? [DocT GT]", "Keyed anidulafungin (82%); by IDSA logic, amphotericin B deoxycholate."),
  ],
  punch="Fluconazole goes everywhere, including the bladder; echinocandins treat the blood but not the urine, eye or CSF; for a resistant Candida in the bladder, amphotericin deoxycholate is the drug that gets there.",
)

L['PK-21'] = dict(
  sub="Pharmacology → Antifungals → PK/PD indices and drug levels",
  step=6,
  intro="Step 6 continues with how hard and how often to give each antifungal, and which ones need levels. The polyenes and echinocandins kill by peak; the azoles by exposure over time, with voriconazole and posaconazole dosed to troughs. The one real question is about voriconazole, and its key is wrong.",
  parts=[
    ('a', "**Amphotericin B: Cmax/MIC 2–4 (lipid 5; liposomal over 40); concentration-dependent.** Its killing rises with the peak and it has a long post-antifungal effect, so it is given once daily at a high dose (liposomal 3–5 mg/kg)."),
    ('b', "**Echinocandins: Cmax/MIC (5–7 parapsilosis/glabrata; 10–20 albicans); AUC/MIC; large, infrequent doses.** They are concentration-dependent and fungicidal against Candida, so a loading dose and once-daily dosing are standard; there is no renal adjustment."),
    ('c', "**Voriconazole: trough 1–2 mg/L (effective); over 4.5–6 toxic; hepatic; IV cyclodextrin accumulates in renal failure.** The usual target range is a trough of 1–5.5 mg/L, with more than 1–2 needed for efficacy and visual hallucinations, encephalopathy and hepatotoxicity above about 5.5. Its metabolism by CYP2C19 is genetically variable and non-linear, hence TDM. The IV form is carried in sulfobutylether-β-cyclodextrin (SBECD), which is renally cleared and accumulates when CrCl is under 50, so oral voriconazole is preferred in renal failure; the clinical harm of SBECD is debated and has been shown only in animals. Voriconazole is fungistatic against Candida and has no activity against Mucorales."),
    ('d', "**Posaconazole: trough over 0.5–1 mg/L; over 98% bound; Vd 5–25 L/kg; IV cyclodextrin, renal accumulation, neurotoxicity.** Current targets are a trough of 0.7 mg/L or more for prophylaxis and 1 mg/L or more for treatment. The 3.5–4 mg/L your notes mention elsewhere is not a protective level: some licensing authorities suggest about 3.75 mg/L as an upper limit (pseudo-hyperaldosteronism, hypertension and hypokalaemia at high levels). Its IV form contains the same SBECD as voriconazole."),
    ('e', "**Isavuconazole: load 200 mg 8-hourly × 6, then 200 mg daily; renal safe; over 90% bound; no cyclodextrin.** The IV form is a water-soluble prodrug (isavuconazonium), so it needs no cyclodextrin and no renal adjustment, and TDM is not routine. It covers Aspergillus and Mucorales and shortens rather than prolongs the QT."),
    ('f', "**Fluconazole: AUC/MIC 25–44 (preclinical); 55–100 (clinical).** In practice this is the dose/MIC ratio: a daily dose in mg at least 100 times the MIC, so higher doses (800 mg load, then 400–800 mg daily, or 12 mg/kg) are used in the critically ill and for less-susceptible species."),
  ],
  mimic=[
    ("Voriconazole vs isavuconazole in renal failure", "Voriconazole IV: SBECD accumulates, so switch to oral. Isavuconazole IV: no cyclodextrin, no change."),
    ("Voriconazole vs posaconazole vs isavuconazole for mucormycosis", "Voriconazole: no activity. Posaconazole and isavuconazole: active, used for step-down or salvage after liposomal amphotericin."),
  ],
  traps=[
    ("“Oral voriconazole is preferred in renal dysfunction” keyed as the INCORRECT statement", "The key is wrong: that statement is true, because the IV SBECD accumulates. The false statements are ‘IV voriconazole is preferred in renal dysfunction’, ‘first line for mucormycosis’ (amphotericin B is; voriconazole has no mucor activity) and ‘fungicidal against Candida’ (it is fungistatic). If the mucor option is offered, it is the clearest incorrect statement."),
    ("“Posaconazole target trough 3.5–4 mg/L”", "That is near the suggested upper limit; the targets are 0.7 (prophylaxis) and 1 mg/L (treatment)."),
  ],
  decode=[
    ("Which of the following is incorrect about voriconazole? (oral preferred in renal dysfunction / IV preferred in renal dysfunction / first line for mucor / fungicidal against Candida) [DocT GT]", "Keyed A, which is actually true; choose the mucormycosis statement."),
    ("[pattern] Which mould-active azole needs no renal adjustment of its IV form?", "Isavuconazole (no cyclodextrin)."),
  ],
  punch="Amphotericin and echinocandins kill by peak, so give big daily doses; voriconazole is dosed to a trough of 1–5.5 mg/L and switched to oral in renal failure because of its cyclodextrin, and it never treats mucor.",
)

L['PK-22'] = dict(
  sub="Pharmacology → Sweep → True or false",
  step=1,
  intro="This sweep comes back to step 1, the rule under the whole deck: the first dose depends on how much water the drug spreads into, and only the later doses depend on the kidneys. The one real question was answered correctly by only 14%: an anuric, fluid-overloaded patient in septic shock, and the majority reached for ‘decrease the amikacin dose’.",
  parts=[
    ('a', "**False: the colistin load is independent of renal function.** The load fills the volume of distribution; renal function decides only the maintenance (PK-16 d, e)."),
    ('b', "**True: sepsis raises the Vd of aminoglycosides.** Aminoglycosides distribute in extracellular water, normally about 0.25 L/kg. Capillary leak, fluid resuscitation and oedema can raise this to 0.35–0.5 L/kg, so a standard dose gives a lower peak and may miss the Cmax/MIC of 8–10. The answer is a larger single dose by weight (amikacin 25–30 mg/kg). Anuria lowers clearance, which changes when the next dose is given (by levels, often days later), not the size of the first."),
    ('c', "**False: ARC is a creatinine clearance over 130 mL/min/1.73 m².** It is common in young patients with trauma, burns, sepsis or brain injury and causes subtherapeutic β-lactam and vancomycin levels; serum creatinine looks normal or low, so it is found only by measuring an 8- or 24-hour urinary creatinine clearance."),
    ('d', "**False: vancomycin is dosed on total body weight.** It distributes into lean and some adipose tissue, so actual weight predicts its Vd. The load is capped (20–25 mg/kg, max 3 g, in obesity) and the maintenance is then set by AUC. Aminoglycosides, by contrast, use adjusted body weight in obesity, and older colistin formulas used the lower of ideal and actual weight."),
    ('e', "**True: meropenem is time-dependent.** Its index is fT>MIC (PK-14), so extended infusions and shorter intervals help; a higher single peak does not."),
    ('f', "**False: echinocandins barely reach the urine and do not suit Candida UTI.** Fluconazole, or amphotericin B deoxycholate for resistant species (PK-20)."),
    ('g', "**False: linezolid needs no renal adjustment.** Its metabolites accumulate in renal failure but the dose stays at 600 mg (PK-18 d)."),
    ('h', "**True: aminoglycosides have a post-antibiotic effect.** Bacterial regrowth is suppressed for hours after the level falls below the MIC, which allows once-daily dosing (PK-15 c)."),
    ('i', "**False: lipophilic drugs, not hydrophilic ones, are sequestered by the ECMO circuit.** Hydrophilic drugs are affected by haemodilution and raised Vd (PK-12)."),
  ],
  table=dict(title="Amikacin in an anuric, fluid-overloaded patient in septic shock", head=["Variable", "Change", "What it alters"], rows=[
    ["Vd (leak, 3 L of fluid, oedema)", "**↑**", "**first dose: increase**"],
    ["Renal clearance (anuric)", "↓", "interval: redose by levels"],
    ["Protein binding", "negligible for aminoglycosides", "nothing"],
  ]),
  mimic=[
    ("Load vs maintenance in AKI", "Load: depends on Vd, unchanged or bigger. Maintenance: depends on clearance, reduced or spaced."),
  ],
  traps=[
    ("“Decrease the amikacin dose because of diminished renal clearance” (the commonest wrong answer; 14% right)", "That is the maintenance rule applied to the first dose. In shock with fluid overload Vd is up, so the dose is increased (option C) and the interval is lengthened by levels."),
    ("“Increase the dosing frequency because of the increased Vd”", "Vd changes the dose size, clearance changes the frequency; an anuric patient needs less frequent, not more frequent, doses."),
    ("“Decrease the dose because of decreased protein binding”", "Aminoglycosides are barely protein bound, so albumin is irrelevant."),
    ("“ARC is CrCl over 90”", "90 is normal; ARC starts at 130."),
  ],
  decode=[
    ("Septic shock on noradrenaline and vasopressin, 3 L of Ringer’s, anuric, volume overloaded; started on meropenem, amikacin, daptomycin, micafungin — amikacin dose consideration? [DocT GT]", "Increase the dose because of the increased Vd (14%); the anuria lengthens the interval."),
    ("[pattern] Obese patient, vancomycin load — which weight?", "Actual (total) body weight, capped at 3 g."),
  ],
  punch="Size the first dose by the volume, time the next one by the clearance: a septic, fluid-overloaded, anuric patient gets more amikacin up front and waits longer for the second dose.",
)

FLAGS = {
  'PK-13': "c: ‘Aminoglycosides penetrate eschar well’ is supported by eschar biopsy data (Polk et al., gentamicin and tobramycin penetration into burn eschar: measurable levels in all patients). a: onset of the hypermetabolic phase is given as 48–72 h on the card and about day 5 in a 2024 review; both stated.",
  'PK-14': "a: ‘biliary for pip-tazo matters’ is unclear; piperacillin is mainly renal with a minor biliary route and still needs renal adjustment; usual Vd is 0.2–0.3 L/kg. d: the US meropenem label allows only 1 h at room temperature in saline (3 h in water). The card’s line break makes ‘h’ a separate part letter; explanation treats it as the infusion-time half of d and adds the watch-line PD targets there.",
  'PK-15': "Nature row: ‘aminoglycosides penetrate tissues well’ is wrong — they are hydrophilic (Vd ~0.25 L/kg) and penetrate lung, CSF, bone and abscesses poorly. Clearance row: moxifloxacin needs no renal adjustment but is avoided in severe hepatic impairment. Key-ratio row: the standard aminoglycoside target is Cmax/MIC 8–10 (ANSM 2011; AUC/MIC used by some programmes); the split by organism is non-standard. Fluoroquinolone ‘87.5–125’: 125 is Forrest 1993 (ciprofloxacin), ~87 is Drusano 2004 (levofloxacin, nosocomial pneumonia). Nature row is only partly wrong: aminoglycosides do reach interstitial fluid and burn eschar.",
  'PK-16': "d: the 2019 international consensus gives a fixed load of 300 mg CBA (~9 MU); ‘9–12 MU by ideal weight, 12 MU for 70 kg’ is higher than both the consensus and the old weight formula (~280 mg CBA ≈ 9 MU at 70 kg). e: 4.5 MU 12-hourly is the EMA dose; consensus is 300–360 mg CBA (9–10.9 MU)/day, first maintenance 12–24 h after the load (12 h with normal kidneys). The card’s renal cuts are deeper than both the consensus table (~5 MU/day at 10–20, ~4 MU/day under 10) and the EU label (4.5–5.5 MU/day at CrCl 10–30, 3.5 MU under 10) vs card 4 and 2 MU/day. ‘About 60% protein bound’: the consensus gives ~50%. CRRT (not on card): consensus 440 mg CBA/day. b: nebulised CMS is a weak consensus recommendation that ESCMID opposes.",
  'PK-18': "Vancomycin row is 2009-era: 2020 consensus targets AUC/MIC 400–600 (not 400 alone), load 20–35 mg/kg actual weight max 3 g (obese 20–25), and on CRRT 7.5–10 mg/kg 12-hourly after a 20–25 mg/kg load, not 36–48-hourly. Teicoplanin: SmPC gives Vss 0.7–1.4 L/kg, half-life 100–170 h, standard load 6 mg/kg × 3 (12 mg/kg × 3–5 for bone/joint and endocarditis). Azithromycin PD index is AUC/MIC rather than Cmax/MIC. Linked DocT QBank key (linezolid for MRSA CLABSI on HD, 49%) conflicts with IDSA: vancomycin or daptomycin first line.",
  'PK-19': "Vancomycin CRRT row (10–15 mg/kg 24–48-hourly) under-doses modern CRRT; 2020 consensus: 7.5–10 mg/kg 12-hourly to levels at effluent 20–25 mL/kg/h. Vancomycin load 25–30 mg/kg vs consensus 20–35 mg/kg (critically ill), max 3 g. Gentamicin 7–10 mg/kg: standard extended-interval dosing is 5–7 mg/kg (7 in sepsis and burns; ANSM up to 8 mg/kg in severe sepsis, peak 30–40 mg/L); 10 mg/kg is above guideline doses.",
  'PK-20': "Liposomal amphotericin ‘high CNS levels’ refers to brain tissue; CSF levels are low. Liposomal amphotericin has poor urine levels; the amphotericin for Candida cystitis is deoxycholate. Linked DocT GT key (anidulafungin for C. auris lower UTI, 82%) conflicts with the card’s own rule and with IDSA 2016 for fluconazole-resistant Candida cystitis (amphotericin B deoxycholate or flucytosine; written for C. glabrata/krusei, applied to C. auris by extension). CDC gives echinocandins first for invasive C. auris and no UTI-specific advice; some C. auris isolates are amphotericin-resistant.",
  'PK-21': "Voriconazole: usual trough range 1–5.5 mg/L, toxicity above ~5.5 (card ‘1–2 effective, over 4.5–6 toxic’ is close). Posaconazole: targets ≥0.7 (prophylaxis) and ≥1 mg/L (treatment); the notes’ 3.5–4 mg/L is near the suggested upper limit (3.75), not a protective level. ‘Neurotoxicity’ from IV SBECD is not established (harm shown only in animals, renal). Linked DocT GT key for voriconazole is wrong (the keyed ‘incorrect’ statement is true; choose the mucormycosis option). Amphotericin and echinocandin Cmax/MIC figures not re-verified.",
}
