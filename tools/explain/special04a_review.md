# SPECIAL04A — independent review of special04a_learn.py and special04a_topups_learn.py (13 Nov 2026)

Checker: `python3 check_learn.py SPECIAL04A` → `SPECIAL04A 11 cards 11 entries OK`, `v3 spine 6 steps OK`.
Top-up (no checker) checked by hand: T_8c9e16fa parts a–d each start with the bold restated card line (verbatim), all mimic/trap/decode pairs have 2 items, punch 245 characters (limit 320), no banned phrases.

## Changes (card: what was wrong → what it says now; source)

### Factual
- PK-01 mimic: "metoprolol 5 mg IV is roughly 25–50 mg orally" → oral bioavailability about 50%, label oral:IV ratio about 2.5 : 1, so 5 mg IV ≈ 12.5 mg orally. Source: Lopressor injection prescribing information (clinical pharmacology).
- PK-01 c: phenytoin feed break "1–2 hours" → "about 2 hours before and after each dose". Source: NHS Specialist Pharmacy Service, Managing interactions between medicines and enteral feeds (phenytoin and ciprofloxacin 2 h; warfarin 1–2 h).
- PK-01 c: "the vitamin K in the feed also opposes [warfarin]" → effect falls even with low-vitamin-K feeds (binding is the main mechanism); added that fluconazole is still well absorbed by tube. Source: NHS SPS (as above); Nicolau et al. 1995, fluconazole relative bioavailability 77% via feeding tube in surgical ICU patients.
- PK-03 c: hydrophilic = renal clearance stated without exception → added that linezolid is the misfit (about 30% unchanged in urine, about 65% of clearance non-renal, no renal dose change). Source: Zyvox prescribing information (Vd 40–50 L, binding 31%).
- PK-07 a: "some authors call it clinically important only above 150 in women or 160 in men" — could not be found → removed; replaced with "some studies require it on more than half of measurements". "30–65% of those with a normal creatinine" could not be traced → Udy 2013 figure: 58% of septic/trauma patients with a normal plasma creatinine (86% of trauma patients). Source: Udy et al., Crit Care 2013;17:R35; ARC review, Pharmaceutics 2017 (14–80% prevalence, >130 mL/min/1.73 m²).
- PK-07 c: "8 hours is usual; 2–24 hours accepted" → "8–24 hours; at least one 8-hour collection in patients at risk". Source: Pharmaceutics 2017 ARC review.
- PK-10 g: "this target is not something examiners ask for" (no content) → AUC/MIC is the index most studies use; the quoted number varies widely, know the index. FLAG updated: card's AUC/MIC 100 unverified; some reviews quote about 666 for S. aureus. Source: EUCAST daptomycin rationale; BCIDP PK/PD summary (AUC24/MIC 666–1,000).
- PK-10 i: "AUC/MIC of about 80–120 predicted success best" overstated → retrospective association with higher success at AUC/MIC 80–120 and with levels above the MIC for the whole interval; indices closely correlated. Source: Rayner et al., Clin Pharmacokinet 2003.
- PK-11 FLAG and header: meta-analysis interval called "95% CI" → 95% credible interval (Bayesian; posterior probability of benefit 99.1%). Source: Abdul-Aziz et al., JAMA 2024 (PMC11170459).

### Structural / minor
- PK-05 mimic: Winter–Tozer given as the only correction → noted it is the classic form, revised versions exist, measured free level more reliable. Source: ClinCalc phenytoin correction (revised equations).
- T_8c9e16fa intro: "about 400 times the size of an antibiotic" → "several hundred times the size of a typical antibiotic" (150 kDa vs 0.4 kDa for meropenem but 1.45 kDa for vancomycin).
- New FLAGS added for PK-01 (fluconazole) and PK-03 (linezolid); header comments updated.

### Checked and left unchanged
- BLING III: 7,202 patients, pip-tazo or meropenem, 90-day mortality 24.9% vs 26.8% (−1.9%, 95% CI −4.9 to 1.1, p = 0.08); clinical cure 55.7% vs 50.0% (p < 0.001) — confirmed (The Bottom Line summary of Dulhunty, JAMA 2024).
- Meta-analysis: 18 RCTs, 9,108 patients, 90-day mortality RR 0.86 (0.72–0.98); clinical cure RR 1.16 — confirmed (PMC full text).
- SSC 2026 adult guideline: exists, Critical Care Medicine, 23 March 2026; strong recommendation for prolonged β-lactam infusion for maintenance after an initial bolus, upgraded from 2021 — confirmed (Epocrates; Guideline Central).
- Vancomycin 2020 consensus: AUC24/MIC 400–600, MIC assumed 1 mg/L, load 20–35 mg/kg (max 3 g) in the seriously ill, obesity 20–25 mg/kg actual weight (max 3 g), troughs 15–20 dropped, continuous infusion 20–25 mg/L — confirmed (Clinician.com summary).
- Polymyxin 2019 consensus: colistin AUCss,24h about 50 mg·h/L (Css,avg about 2 mg/L total), higher exposure raises AKI, CMS load 300 mg CBA (about 9 MIU), polymyxin B preferred systemically — confirmed (Medical Dialogues summary of Tsuji 2019).
- ARC: >130 mL/min/1.73 m²; ARC score age ≤50 = 6, multi-trauma = 3, SOFA ≤4 = 1, bands 0–3/4–6/7–10 — confirmed (Udy 2013). ARCTIC appears only in the header comment; point values not re-verified.
- Protein binding (Ulldemolins, Clin Pharmacokinet 2011): ceftriaxone 85–95%, ertapenem 85–95%, flucloxacillin 95%, daptomycin 90–93%, teicoplanin 90–95%, vancomycin 30–60% (moderate); hypoalbuminaemia 40–50%; Joynt ceftriaxone Vd and clearance about doubled — confirmed.
- Daptomycin in obesity: label and ACCP use total body weight — confirmed (UNMC ID blog 2022).
- Craig fT>MIC (carbapenems 40%, penicillins 50%, cephalosporins 60–70%), 100% fT>4–5 × MIC in critical illness, FQ fAUC/MIC ≥125 Gram-negative and 30–50 pneumococcus, aminoglycoside Cmax/MIC 8–10 — consistent with BCIDP PK/PD summary and Deranged Physiology.
- French 2019 consensus: free concentration 4–8 × MIC for 100% of the interval — confirmed (HealthManagement summary of Guilhaumou 2019). ESICM/ISAC 2020 position paper recommends routine TDM of aminoglycosides, β-lactams and vancomycin — confirmed (Lund record abstract).
- Ceftolozane-tazobactam: 1.5 g 8-hourly cIAI/cUTI, 3 g 8-hourly HABP/VABP — confirmed (Zerbaxa PI).
- Tigecycline: 100 mg then 50 mg 12-hourly; Child-Pugh C 25 mg 12-hourly after the same load; Vss 7–9 L/kg — confirmed (Tygacil PI).
- CRRT: convective clearance = SC × ultrafiltrate rate (diffusive: saturation coefficient × dialysate rate) — confirmed (Frontiers Pharmacol 2020). Front-loaded β-lactam doses in the first 24–48 h regardless of organ function — confirmed (Crit Care 2014 review, cc13938).
- Monoclonal antibodies: Vd a few litres above plasma volume, proteolysis main route, saturable TMDD, no renal/CYP clearance, FcRn salvage, ADAs speed clearance — consistent with mAb PK review; IgG1 half-life about 3 weeks is standard teaching.
- Not freshly verified (standard references, left as written): aminoglycoside Vd 0.25 → ≥0.4 L/kg in sepsis; free phenytoin 1–2 mg/L; extraction ratio cut-offs 0.3/0.7; ECMO sequestration of lipophilic/highly bound drugs.

## Final FLAGS — special04a_learn.py
- PK-01: Fluconazole is the weakest member of the feed-binding list (relative bioavailability 77% via tube in ICU patients).
- PK-03: Linezolid is listed as hydrophilic and renally cleared; its Vd is about total body water and about 65% of its clearance is non-renal.
- PK-04: Daptomycin is dosed on total (actual) body weight per label and ACCP, not lean weight; β-lactams are usually not weight-dosed.
- PK-05: Vancomycin is only moderately bound (30–60%), so it fits the highly bound list poorly.
- PK-08: "SLED removes antibiotics more efficiently than CRRT" holds per hour of treatment, not necessarily per day.
- PK-10: Vancomycin target is AUC/MIC 400–600 (card says 400). Colistin "AUC/MIC 53–141" unverified; consensus target AUC about 50 mg·h/L. Linezolid "40–80% fT>MIC" unverified (clinical data: AUC/MIC 80–120 and 100% T>MIC). Daptomycin "AUC/MIC 100" unverified; published targets vary (some reviews about 666).
- PK-11: "Large RCTs show no distinct advantage" outdated (BLING III clinical cure benefit; 2024 meta-analysis RR 0.86, 95% credible interval 0.72–0.98; SSC 2026 strong recommendation). DocT GT CKD question keys the false "vancomycin load decreased in CKD".
- No flags: PK-02, PK-06, PK-07, PK-09.

## Final FLAGS — special04a_topups_learn.py
- None. T_8c9e16fa agrees with standard mAb pharmacokinetics.
