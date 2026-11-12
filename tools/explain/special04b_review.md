# SPECIAL04B — independent review of special04b_learn.py and special04b_topups_learn.py (13 Nov 2026)

Checker: `python3 check_learn.py SPECIAL04B` → `SPECIAL04B 11 cards 11 entries OK`, `v3 spine 6 steps OK`.
Top-ups (no checker) checked by hand and by script: every part starts with the bold restated card answer (all 11 parts match the card text in out/review_data.json), all mimic/trap/decode pairs have 2 items, punch 218, 238 and 223 characters (limit 320), no banned phrases.

## Changes (card: what was wrong → what it says now; source)

### Factual
- PK-13 c (part, FLAG): writer flagged "aminoglycosides penetrate eschar well" as unverifiable and said eschar is reached poorly → the claim is supported; part now explains it (small water-soluble molecules, measurable eschar levels in every patient on gentamicin/tobramycin, effect on eschar flora); FLAG rewritten. Source: Polk et al., "Gentamicin and tobramycin penetration into burn eschar" (UTMB, 1983).
- PK-15 a (part, FLAG): "the card's 'aminoglycosides penetrate tissues well' is not right" → "only partly right": they reach interstitial fluid and burn eschar but not cells, lung ELF, CSF, bone or pus. Source: as above.
- PK-15 d (part, FLAG): "87.5" left unexplained, aminoglycoside "AUC/MIC about 80–100" given as a figure I could not find → 125 = Forrest 1993 (ciprofloxacin AUIC in seriously ill patients); ~87 = Drusano 2004 (levofloxacin, nosocomial pneumonia, eradication); pneumococcus 30–40; aminoglycoside AUC/MIC kept without a number. Sources: Forrest et al., AAC 1993;37:1073; Drusano et al. 2004 abstract; ANSM 2011 aminoglycoside guidance (Cmax/MIC ≥8–10).
- PK-16 a: added that the 2019 consensus gives colistin protein binding ~50% (card 60%). Source: Tsuji 2019 polymyxin consensus (PMC7437259).
- PK-16 b: nebulised CMS stated as standard → weak consensus recommendation for XDR HAP/VAP, ESCMID advises against routine nebulised antibiotics. Intraventricular 125,000 IU (~4.1 mg CBA) confirmed. Source: Tsuji 2019, R33–R35.
- PK-16 c: "nephrotoxicity rises steeply" above 2 mg/L → "becomes more likely" (steepness not stated in source). Source: Tsuji 2019, R2.
- PK-16 e (part, FLAG): EU label renal bands added (CrCl 30–50: 5.5–7.5 MU/day; 10–30: 4.5–5.5; <10: 3.5), showing the card's 4 and 2 MU/day are below both label and consensus; CRRT dose added (consensus 440 mg CBA ≈ 13.3 MU/day, 220 mg 12-hourly). Sources: Colomycin SmPC 4.2 (emc); Tsuji 2019 R14; UNMC colistin page.
- PK-18 a and table: vancomycin on intermittent HD "to a pre-dialysis level" and table "load 20–35 mg/kg" (that is the ICU load, not an HD figure) → load by actual weight, pre-dialysis level 15–20 mg/L. Source: Rybak 2020 consensus, table 2 rows 12–14.
- PK-18 e: "erythromycin and clarithromycin behave as time-dependent" stated as fact → "older teaching classes them as time-dependent".
- PK-19 b (part, FLAG): "the 10 mg/kg end is used only with levels" (unsourced) → gentamicin 5–7 mg/kg standard, ANSM up to 8 mg/kg in severe sepsis with a peak of 30–40 mg/L; the card's 10 mg/kg is above guideline doses, so a first-dose peak level is essential. Source: ANSM 2011 aminoglycoside guidance; burn review (MDPI 2023, gentamicin 7 mg/kg).
- PK-20 trap, table, FLAG: "IDSA/CDC advise amphotericin B deoxycholate or flucytosine" for C. auris UTI → IDSA 2016 for fluconazole-resistant Candida cystitis (written for C. glabrata/C. krusei, applied to C. auris by extension); CDC gives echinocandins first for invasive C. auris, no UTI-specific advice, and advises against treating asymptomatic candiduria; check susceptibility because some C. auris isolates resist amphotericin. Table row now "C. glabrata, C. krusei; by extension C. auris", "amphotericin B deoxycholate or flucytosine". Sources: CDC "Treatment and Management of C. auris Infections"; IDSA 2016 as summarised on the UNMC ID blog (AmB-d 0.3–0.6 mg/kg 1–7 days, flucytosine 25 mg/kg qds, liposomal does not reach urine).
- PK-22 d: "colistin [uses] the lower of ideal and actual weight" → "older colistin formulas used" it (2019 consensus uses a fixed 300 mg CBA load). Source: Tsuji 2019 R9.

### Minor / wording
- PK-12 b: "caspofungin behaves the same way" and "newer polymethylpentene oxygenators and coated tubing bind less" (not verified) → voriconazole only; losses vary with circuit materials and fall as sites saturate.
- PK-13 a: hypermetabolic phase "lasts weeks to months" → "can persist for months, in large burns for a year or more". Source: MDPI 2023 burn dosing review (flow phase from about day 5, up to 1–3 years).
- PK-13 b: highly bound once-daily drugs "are the ones that fail" → "most at risk".
- PK-18 mimic: teicoplanin half-life "about a week" → "4–7 days". Source: Targocid SmPC (100–170 h).
- PK-16, PK-15, PK-19, PK-20 FLAGS and the file header comment updated; top-up header comment and T_29b5a652 FLAG given their source.

### Checked and left unchanged
- Polymyxin consensus 2019: load 300 mg CBA (~9 MIU) over 0.5–1 h; first maintenance 12–24 h later; 300–360 mg CBA/day in two doses; renal table (UNMC reproduction: 50–60: 245, 30–40: 195, 10–20: 160, 5–10: 145, 0: 130 mg CBA/day; maintenance 12 h after load, 24 h if CrCl ≤40); target Css,avg ~2 mg/L; polymyxin B load 2.0–2.5 mg/kg TBW, 1.25–1.5 mg/kg 12-hourly, no renal adjustment, none on RRT; PMB preferred systemic, colistin for lower UTI; 5 of 6 studies more nephrotoxicity with colistin — all confirmed.
- EU colistin label: 9 MIU load including renal impairment and RRT; 9 MIU/day in 2–3 doses; 9 MIU ≈ 300 mg CBA ≈ 720 mg CMS; half-life 9–18 h in the critically ill (card 14 h fits).
- Vancomycin 2020: AUC 400–600; load 20–35 mg/kg actual weight max 3 g; obese 20–25 mg/kg max 3 g; CRRT load 20–25 mg/kg, 7.5–10 mg/kg 12-hourly at 20–25 mL/kg/h; continuous infusion 15–20 then 30–40 mg/kg/day — confirmed (PMC7358040 table 2).
- Teicoplanin SmPC: 6 mg/kg ×3 standard, 12 mg/kg ×3–5 bone/joint and endocarditis; renal adjustment from day 4; not removed by HD; Vss 0.7–1.4 L/kg; 87.6–90.8% bound — confirmed.
- Meropenem US label: 1 h room temperature in saline (15 h refrigerated), 3 h in water (13 h refrigerated); 2% bound; half-life 1 h — confirmed.
- Amikacin 25–30 mg/kg in septic shock, Cmax/MIC 8–10, peak 60–80 mg/L, trough <2.5 mg/L — confirmed (Ann Intensive Care 2016 amikacin study citing French guidance; ANSM 2011).
- Burns: ebb phase 48 h, flow phase from about day 5; gentamicin 7, tobramycin 10 mg/kg; vancomycin 40–70 mg/kg/day to AUC 400–600; linezolid 8-hourly — confirmed (MDPI 2023 review).
- Voriconazole trough 1–5.5 mg/L, >5.5 neurotoxicity; posaconazole ≥0.7 prophylaxis, ≥1 treatment, no established toxic level, 3.75 mg/L suggested upper limit; SBECD accumulation of debated significance, toxicity only in animals; isavuconazole no routine TDM — confirmed (Stanford SHC antifungal TDM guidance).
- Aminoglycoside nephrotoxicity "up to 10–25%" — confirmed (StatPearls); card's 10–30% left with the existing FLAG.
- From standard references, not re-opened today: isavuconazole 200 mg 8-hourly ×6 then daily; daptomycin label 4–6 mg/kg, 48-hourly at CrCl <30, CK weekly; azithromycin half-life 68 h and AUC/MIC index; ARC ≥130 mL/min/1.73 m²; ertapenem 85–95% bound, half-life 4 h; liposomal amphotericin brain-tissue (not CSF) levels.
- Not re-verified (left flagged): amphotericin and echinocandin Cmax/MIC figures; fluconazole AUC/MIC 25–44 / 55–100.

## Final FLAGS — special04b_learn.py
- PK-13: c is supported (Polk et al., eschar biopsies). a: hypermetabolic onset 48–72 h on the card, about day 5 in a recent review; both stated.
- PK-14: a 'biliary for pip-tazo matters' unclear (piperacillin mainly renal, needs renal adjustment); usual Vd 0.2–0.3 L/kg. d: US meropenem label 1 h at room temperature in saline (3 h in water). Card line break creates a separate part 'h'.
- PK-15: Nature row only partly right (aminoglycosides reach interstitial fluid and eschar but not cells, lung ELF, CSF, bone, pus). Moxifloxacin avoided in severe hepatic impairment. Aminoglycoside target is Cmax/MIC 8–10; split by organism non-standard. FQ 125 (Forrest 1993) and ~87 (Drusano 2004).
- PK-16: Consensus load 300 mg CBA (~9 MU); card's 9–12 MU / 12 MU at 70 kg is higher. EU label 4.5 MU 12-hourly; consensus 300–360 mg CBA/day, first maintenance 12–24 h after load. Card's renal cuts below both consensus and EU label for CrCl <30. Protein binding ~50% (consensus), not 60%. CRRT 440 mg CBA/day not on card. Nebulised CMS weak/contested.
- PK-18: Vancomycin row 2009-era (2020: AUC 400–600, load 20–35 mg/kg max 3 g, CRRT 7.5–10 mg/kg 12-hourly). Teicoplanin Vss 0.7–1.4, half-life 100–170 h, standard load 6 mg/kg ×3. Azithromycin index AUC/MIC. DocT QBank key (linezolid for MRSA CLABSI on HD, 49%) conflicts with IDSA.
- PK-19: Vancomycin CRRT row under-doses modern CRRT; load 25–30 vs consensus 20–35 mg/kg. Gentamicin 7–10 mg/kg above guideline doses (5–7; ANSM up to 8).
- PK-20: Liposomal amphotericin 'high CNS levels' = brain tissue, CSF low; poor urine levels. DocT key (anidulafungin for C. auris lower UTI, 82%) conflicts with the card's own rule and IDSA 2016 by extension; CDC has no UTI-specific advice.
- PK-21: Voriconazole range 1–5.5 mg/L; posaconazole ≥0.7/≥1 mg/L, 3.5–4 is near the 3.75 upper limit; SBECD 'neurotoxicity' not established. DocT voriconazole key wrong (choose mucormycosis option). Amphotericin/echinocandin Cmax/MIC figures not re-verified.
- No flags: PK-12, PK-17, PK-22.

## Final FLAGS — special04b_topups_learn.py
- T_29b5a652: '10–30% of courses' — usual quoted range up to 10–25% (StatPearls); card figure kept.
- No flags: T_c2609f9d, T_5ceb5d71.
