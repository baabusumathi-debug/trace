# GI05 review (second, independent check), 20 Nov 2026

Files checked: gi05_learn.py (13 cards; no Top-up cards for GI05) against cards/GI05.jsonl, qpack/GI05.md and gi_cardlayer.json. Letters and bold restatements match the cards in every part. `check_learn.py GI05` passes.

Sources opened online: WSACS 2013 (Kirkpatrick, Intensive Care Med 39:1190; Springer text and the WSACS-hosted PDF); WSES 2018 open abdomen (Coccolini, WJES 13:7, eScholarship PDF); Balogh 2003 J Trauma abstract (QxMD); Hong 2002 Br J Surg abstract (Scilit) and EMJ 2008 review; StatPearls, Abdominal Compartment Syndrome; OpenAnesthesia ICU one-pager; VUMC trauma IAH protocol; NHS Scotland IAH algorithm; LA County burn ACS protocol (reproduces the WSACS 2007 risk table); Ann Transl Med 2019 commentary on Mahjoub 2010 and Beurton 2019.
Blocked or not opened: PMC full text of WSACS 2013 (captcha), so the algorithm figure itself was not seen; Europe PMC; LITFL; WSES on BMC (eScholarship copy used instead).

## The writer's unverified points, settled
- **Stop measuring when consistently under 12 (IAH-11 e):** supported. Below 12 there is no IAH by definition. WSACS-based protocols stop routine measurement: VUMC writes "Discontinue" for IAP under 12, and the NHS Scotland/WSACS 2007 algorithm says observe and recheck if the patient deteriorates. The WSACS 2013 figure could not be opened. The card stands, and the explanation now gives the reason.
- **4–6 h interval:** supported. OpenAnesthesia: "continuously or every 4–6 hours"; VUMC: q4–6 h; StatPearls: every 6 h. The WSACS 2013 text itself says only "serial or continuous". The card's "4 hours" is the low end, which is harmless (flag kept).
- **Balogh incidence (IAH-06):** Balogh 2003: 188 shocked torso-trauma patients, ACS 14% (6% primary, 8% secondary). The 1% of all trauma ICU admissions comes from another study, Hong 2002 (706 trauma ICU patients: ACS 1%, IAH 2%). The 9% is Balogh 2002; I did not re-open it. The numeric predictor cut-offs come from the 2003 full text and could not be re-checked; the abstract confirms which variables predicted each type.
- **Oliguria at 15 / anuria at 30:** confirmed. StatPearls: "oliguria can occur at an IAP of 15 mm Hg and anuria at pressures of 30 mm Hg".
- **WSES timing of fascial closure:** WSES says close "as soon as possible" (1C), and early closure is the strategy (1B). "Early fascial closure is commonly defined as occurring within 4–7 days" is in the body text and is not a graded recommendation. Re-exploration should come "no later than 24–48 h" (1C). WSACS 2013: "early or at least same-hospital-stay" closure (1D).
- **PLR with raised IAP:** confirmed. Mahjoub 2010: an IAP of 16 or more was the only factor linked to a false-negative PLR. Beurton 2019: AUROC 0.60 with IAH vs 0.98 without.

## Changes
- IAH-01 e (factual): said screening is triggered by two or more risk factors → now WSACS 2013 recommends measuring with any risk factor (1C); the two-or-more trigger was the 2007 algorithm. Source: WSACS 2013 text.
- IAH-02 intro and trap (minor): "the rest chose the symphysis" / "main wrong choice" was not supported by the qpack, which has no distractor percentages → now just lists the distractors.
- IAH-02 d (minor, tone): "500 mL is absurd" → "the 500 mL distractor would grossly overestimate IAP".
- IAH-03 trap GT1o (factual/clarity): the trap said 22 cmH2O is under 20 mmHg but still accepted the keyed C, which also reads 22 cmH2O, without comment → now it says that, taken literally, none of options A–C reaches ACS, that the question almost certainly means mmHg, and that organ failure decides it. D is now called grade III IAH. Flag updated.
- IAH-06 b–d (factual attribution): "Figures are from the Houston (Balogh) series" also covered the 1%, which is from Hong 2002 → each figure is now attributed (Hong 2002; Balogh 2003 14% = 6% + 8%; Balogh 2002 9%), and the predictors confirmed by the Balogh 2003 abstract are added. Sources: Scilit/EMJ; QxMD abstract.
- IAH-07 c (factual): the capillary-leak group was given as massive transfusion, sepsis, pancreatitis, acidosis and hypothermia, while head of bed and prone position were called "also" → now it is labelled the WSACS 2007 table and its members are listed as in that table (fluid over 5 L/24 h, polytransfusion, acidosis, hypothermia, coagulopathy, sepsis, pancreatitis, damage-control laparotomy). Head of bed over 30°, prone position, high BMI and respiratory failure go under reduced wall compliance. Source: LA County protocol reproducing the WSACS table.
- IAH-08 d (factual): "The gut is the first organ to become ischaemic" sat badly with "the kidney fails first" (IAH-04 watch) → now "gut perfusion falls early, at moderate pressures, often before urine output falls".
- IAH-09 d (depth): PLR false negatives now have their mechanism and data (Mahjoub ≥16 mmHg; Beurton AUROC 0.60 vs 0.98), plus the advice to measure IAP before trusting a negative PLR. Source: Ann Transl Med 2019.
- IAH-10 e (minor): "keep APP at least 60" → now called an observational target, since WSACS 2013 makes no recommendation on APP.
- IAH-11 d (factual): "A burn patient with intra-abdominal fluid and ACS needs laparotomy" was too absolute → now percutaneous drainage is a reasonable first step when the fluid can be drained (WSACS 2013, 2C/2D), with laparotomy if organ failure persists. The GT1o trap now reads "of the options given".
- IAH-11 trap TAC and extra (factual): "WSES 2018 ideally within 4–7 days" → now: as soon as possible (1C), with early closure commonly defined as within 4–7 days (text, not graded). Added that the WSES 24–48 h figure is the re-look interval, not the closure time. The extra now includes re-exploration every 24–48 h. Source: WSES 2018 PDF.
- Header: added the second-review sources and what was not re-opened.

## Verified, no change needed
- Definitions, grades, ACS > 20 + new organ dysfunction, APP = MAP − IAP, FG = MAP − 2 × IAP, primary/secondary/recurrent, the 25 mL maximum, the paediatric 1 mL/kg (min 3, max 25), mid-axillary zero, end-expiration, supine (WSACS 2013).
- PCD 2C vs nothing and 2D vs laparotomy; plasma:RBC 2D; decompressive laparotomy 1D; no recommendation on diuretics, RRT, albumin or APP (WSACS 2013, as the writer listed).
- Cheatham 2010: 478 patients, survival 50% → 72%, fascial closure 59% → 81% (the writer checked this; consistent).
- The DocT key errors (perforated ulcer: immediate laparotomy, B) and the CGT4 pancreatitis nuance: the explanation agrees with the card-layer `cross` and `lines`.

## Final FLAGS
- IAH-03: Card correct. The DocT perforated-ulcer key (C) is wrong; immediate laparotomy is right. GT1o: options A–C are in cmH2O (22 cmH2O ≈ 16 mmHg), so the keyed C is literally under the threshold. The question means mmHg, and C wins on organ failure.
- IAH-11: Card correct (4 h vs 4–6 h is harmless; the stop-below-12 rule is supported by WSACS-based protocols). The DocT perforated-ulcer key C is wrong; the answer is B, immediate laparotomy. The TAC "48–72 h" key is not a guideline closure figure: WSACS says early or same-admission, and WSES says as soon as possible, with early closure "commonly defined" as within 4–7 days. The card-layer line's "ideally 4–7 days" slightly overstates WSES. The CGT4 pancreatitis key "immediate" overstates stepwise care but is the best option given.
- IAH-04: Card correct. APP ≥ 60 is observational; WSACS 2013 makes no recommendation.
- IAH-09: The transmural plateau of −0.5 × IAP is Malbrain teaching; some sources subtract the whole IAP. Not an error.
- IAH-06 (new, minor): part a combines two studies (Hong 2002 1%; Balogh 2003 14%). The predictor cut-offs could not be re-checked online.
