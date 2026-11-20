# GI07A review: independent fact-check (20 Nov 2026)

Checked `gi07a_learn.py` against `cards/GI07A.jsonl`, `qpack/GI07A.md` and `gi_cardlayer.json`. No Top-up cards. Letters and bold restatements matched the card on all 16 cards. `check_learn.py GI07A`: OK (16/16, spine 6).

## Changes

Factual:
- CLD-05 d: cirrhotic cardiomyopathy diastolic criterion said "several of" the four echo criteria. Now "three or more of four". It also says the 2020 criteria list QT/ECG changes only as a research area, not a criterion. (Izzy et al., Hepatology 2020, as tabulated on encyclopedia.pub entry 8094.)
- CLD-05 f: POPH haemodynamics said "mean PAP >20, PVR >3 WU", which mixes two definitions. Now ESC/ERS 2022 (mPAP >20, PVR >2 WU, wedge ≤15), with the older ILTS 2016 definition (mPAP ≥25, PVR ≥3 WU) noted. The transplant thresholds are now anchored to Krowka's mortality bands: 25–35 none, 35–50 50%, >50 100%. Contraindication now reads about 45–50 or more. (MDPI Diagnostics 2025;15:1821 review.)
- CLD-08 d/e: MELD 3.0 had no detail. It now gives female sex 1.33 points, albumin bounded 1.5–3.5 g/dL, interaction terms, Na 125–137, creatinine cap 4.0 → 3.0, C-statistic 0.869 vs 0.862, and US allocation from 13 July 2023. (Kim, Gastroenterology 2021;161:1887; OPTN/HRSA implementation FAQ.) "Myers 2011" year removed because it could not be confirmed.
- CLD-08 f (and FLAG): checked the dialysis rule. For MELD/MELD-Na, 2 or more dialysis treatments in the prior week set creatinine to 4.0 (Kim 2021). For MELD 3.0, 2 or more dialyses in 7 days or CRRT set it to 3.0 (radathand MELD 3.0 calculator, a secondary source; the OPTN calculator guide could not be fetched). The writer's text was right; the FLAG stands.
- CLD-10 a: Villanueva was presented as variceal-specific. It now says the trial covered all upper GI bleeders: threshold 7 vs 9 g/dL, 6-week survival 95% vs 91% (HR 0.55), rebleeding 10% vs 16%. In cirrhosis the survival benefit was in Child A/B only, not C, and HVPG rose only in the liberal arm. (Critical Care 2013 journal-club critique, cc13020.)
- CLD-10 a: "a nasogastric tube is not part of Baveno VII" was imprecise. Now "Baveno VII advises caution with nasogastric tubes (6.11) and recommends erythromycin 250 mg IV 30–120 min before endoscopy (6.19)". The FLAG wording is updated to match. (Baveno VII pre-proof PDF, unipd repository.)
- CLD-10 e: "a stent bridges for up to 24 hours" was wrong for SEMS; the 24-hour limit applies to tamponade. Now: tube about 24 h at most, stent can stay longer, SEMS as effective and safer (Baveno VII 6.29). The pre-emptive TIPS criteria, including HVPG >20, are confirmed (6.27).
- CLD-11 c: removed the unverified "holds about 600 mL" for the Linton–Nachlas tube. The text now explains how the balloon works.
- CLD-11 b/e: inflation figures checked: gastric balloon 50 mL test then 250–300 mL (Minnesota 450–500 mL), oesophageal 30–45 mmHg. Added about 90% initial control and kept "about half rebleed on deflation". (StatPearls; LITFL.)
- CLD-12 b: "start variceal prophylaxis before anticoagulation" in PVT was stated too firmly. Baveno VII's cirrhosis-PVT statements do not set this order. Now: prophylaxis is put in place and anticoagulation follows without long delay, starting with LMWH, then LMWH, VKA or DOAC (Baveno VII 9.11).
- CLD-14 b: salt equivalent "5–6.5 g" changed to "4.6–6.9 g" for 80–120 mmol/day (EASL 2018), with the reason not to restrict harder.
- CLD-15 b/c: the side distribution is now 85% right, 13% left, 2% bilateral. The mechanism is now gaps in the tendinous diaphragm stretched into blebs by ascites, not "thinner on the right, liver against it". The SBEM criteria now include "exclude pneumonia/parapneumonic effusion" for the culture-negative >500 criterion. (Annals of Hepatology hepatic hydrothorax review.)

Minor (depth/clarity):
- CLD-03 c: the bare restatement now explains what the free pressure contains.
- CLD-03 trap 2: now explains why it is pre- and not post-sinusoidal.
- CLD-04 a/b: the "two-thirds / a third" split, which could not be confirmed, is softened to "larger fixed part" and "often quoted as about a quarter".
- CLD-09 c, e: bare restatements now have a why.
- CLD-13 c: "peritonitis" (low SAAG) is now distinguished from SBP (high SAAG).
- Header: second-check sources and dates added.

Verified and left as written: D'Amico 1/3/20/57% (Zipprich, Liver Int 2012, citing D'Amico J Hepatol 2006); Lau NEJM 2007 (endotherapy 19.1% vs 28.4%, no difference in rebleeding, surgery or death); Baveno VII 6.2, 6.5, 6.9, 6.36–6.38; HPS criteria; HALT-IT, ATTIRE and ANSWER figures; Wiesner MELD bands.

## Final FLAGS (unchanged in substance)
- CLD-08: f, the pre-dialysis creatinine, is not the allocation rule. Two dialyses in a week (or CRRT) set creatinine to 4.0, or 3.0 in MELD 3.0. d: US allocation is MELD 3.0 since July 2023.
- CLD-09: the table percentages come from an untraceable single series; most series put variceal bleeding at up to about 70%.
- CLD-10: a, "correct fibrinogen by TEG" and the NG tube, are not Baveno VII (6.37, 6.11, 6.19). e: SEMS is an equal, safer bridge. The Marrow key (emergent endoscopy) is disputed.
- CLD-12: the antifibrinolytic row is printed twice. The DocT key (TIPS first-line secondary prophylaxis) is wrong; EVL + NSBB is correct.
- CLD-14: d, the albumin target, is outdated (ATTIRE). e: "vaptans also reduce ascites" is unsupported. f: terlipressin is for HRS-AKI, not refractory ascites. The qpack DocT line misstates the ATTIRE target as 3.5 g/dL (it was 3.0).

Could not fetch: the PubMed abstracts (D'Amico, Villanueva, Lau; permission prompt timed out), the OPTN MELD calculator guide (redirected), the PMC cirrhotic-cardiomyopathy table (captcha). Secondary sources were used instead.
