# ENDO02A review (second, independent check), 22 Nov 2026

Files checked: endo02a_learn.py (22 cards) and endo02a_topups_learn.py (2 top-ups), against cards/ENDO02A.jsonl, qpack/ENDO02A.md and endo_cardlayer.json. check_learn.py ENDO02A: OK (22/22, spine 6). Letters and bold restatements match the cards on every card. Traps were kept; their correct side was checked.

Sources opened: ADA Standards of Care 2024 Section 16 (Diabetes Care 2024;47 Suppl 1:S295, PMC10725815). The 2025 and 2026 Section 16 pages on PMC were behind a bot check, so the 2024 text is the latest read. Also opened: the SCCM 2024 glycaemic control guideline page; the Leuven II abstract (NEJM 2006); VISEP (wikijournalclub and the Relias summary); the Crit Care 2014 trial table (cc13998); CONTROLING (The Bottom Line summary of Intensive Care Med 2021); Krinsley and Grover (Crit Care Med 2007, abstract); and the Endocrine Society 2009 hypoglycaemia guideline (JCEM 94:709). PubMed VISEP and the GLUCONTROL repository page were blocked.

## Changes

Factual:
- GLY-12 b and trap, and the GLY-12 FLAG: said "ADA and most protocols check every 1–2 h on an infusion". Now: ADA calls checks every 30 min to 2 h the required standard while IV insulin runs, and SCCM 2024 says at least hourly during instability (ADA 2024 S16; SCCM 2024).
- GLY-11 c and the GLY-11 FLAG: said CONTROLING was "stopped for futility". Now: it was stopped at about half its planned size (49%) because benefit was unlikely and harm was possible; 90-day survival did not differ (CONTROLING, ICM 2021).
- GLY-19 a: said 6.9% severe hypoglycaemia in the NICE-SUGAR intensive arm. Now 6.8% vs 0.5%, the primary 2009 paper's figure, which matches GLY-15 (NEJM 2009; cc13998 table).
- GLY-19 c: said "a single severe episode roughly doubled the adjusted odds of death". Now: severe hypoglycaemia (<40) had an adjusted OR of 2.28, and "even a single episode" was independently associated with death (Krinsley 2007 abstract).
- GLY-15 trap 3: said "poor pre-admission control … are the risk markers", which is not established. Now: the GT key treats the statement as false; the recognised markers are diabetes, insulin, severity of illness, septic shock, renal failure and longer stay, and good prior control is not one of them (Krinsley 2007 risk factors). This still agrees with the card-layer line's point that tight control alone is not the driver.
- GLY-20 a: said "bicarbonate-buffered fluid contains no glucose and no lactate" as a universal rule. Now: many bicarbonate fluids are glucose-free and, unlike lactate fluids, give no gluconeogenic substrate; glucose is also lost in the effluent. Some bicarbonate fluids do contain glucose.

Minor or additions:
- GLY-14 c: added the VISEP starch figures (AKI 34.9% vs 22.8%, RRT 31.0% vs 18.8%) and the mechanism. Part d (insulin arm stopped by the DSMB for hypoglycaemia; HES arm stopped at the interim analysis for renal failure and a trend to higher mortality) was confirmed (wikijournalclub; Relias).
- GLY-13 d: added the Leuven II severe hypoglycaemia figure (18.7% vs 3.1%). "Independent risk factor for death" softened to "associated with death". The abstract confirms 40.0% vs 37.3%, 52.5% → 43.0% at ≥3 days, and higher mortality with intensive therapy at <3 days.
- GLY-16 e: "the Leuven benefit is now thought to have depended on IV glucose" is now attributed as the TGC-fast authors' suggestion.
- GLY-01 mimic: added that ADA (since 2024) uses 100–180 for non-critically ill ward patients and keeps 140–180 for the ICU (ADA 2024 S16).
- Header: the ADA source changed from the "2019 MDCalc text" to the ADA 2024 S16 text. Added the second-check sources. Removed CONTROLING, Krinsley and ISO 15197 from the "not verified" list. ISO 15197:2013 is now stated as 95% within ±15 mg/dL below 100 and ±15% at 100 or more; this is the standard text, which I know well but did not open online.
- Top-up T_d6d166b0 e: added the Endocrine Society 2009 cut-offs at glucose <55: insulin ≥3 µU/mL, C-peptide ≥0.6 ng/mL, proinsulin ≥5 pmol/L, β-hydroxybutyrate ≤2.7 mmol/L (JCEM 2009, read). The header was updated, and the NICTH points (pro-IGF-II, insulin suppressed, high IGF-II:IGF-I ratio) were confirmed.
- Top-up T_a674f960 b: the SGLT2 stop time now reads FDA 3 days (canagliflozin, dapagliflozin, empagliflozin), 4 for ertugliflozin, hence ADA's "3–4 days" (ADA 2024 S16 cites the FDA).

## Verified as written (no change)
- SCCM 2024: good practice to treat persistent glucose ≥180; conditional, moderate certainty against 80–139 vs 140–200; IV infusion over SC (very low certainty); monitoring ≤1-hourly during instability (low); explicit decision support (moderate); individualised targets only as a research recommendation; no statement on point-of-care devices; CGM is left to research.
- ADA: HbA1c for anyone with glucose >140 if none in the past 3 months; insulin from ≥180; 140–180, with 110–140 for selected patients; level 1 54–69, level 2 <54, level 3 needing assistance.
- NICE-SUGAR 6104 patients, 27.5% vs 24.9%. 2012 follow-up: HR 1.41 and 2.10, with distributive shock. VISEP hypoglycaemia 17.0% vs 4.1% and 90-day mortality 39.7% vs 35.4%. GLUCONTROL 1101 patients, 8.7% vs 2.7%, 17.2% (intensive) vs 15.3%, stopped for protocol violations.
- Cryer's thresholds; the ADAG equation; the metformin eGFR cut-offs and ACR contrast advice.

## Not verified (left soft, or as the card gives it)
- Current ADA 2025/2026 wording: the pages were blocked. As far as I know the ICU targets are unchanged from 2024.
- Card figures on GLY-03 (75% / 12%), GLY-17 (meter non-agreement 1.4–27.1% and 0–12.3%; 95% vs 79% accuracy in hypotension), GLY-18 (AACE/ACE 2016 CGM statement) and GLY-19 (19% / 32% incidence).
- LUCID and TGC-fast figures: taken from the writer's online check; not re-opened.

## Final FLAGS
- GLY-01: the card gives hyperglycaemia as >180–200, but ADA's inpatient definition is >140 (which triggers HbA1c), and 180 is the insulin start. "Below 110 not recommended" is too low: SCCM 2024 advises against 80–139, so the floor is 140. ADA still allows 110–140 in selected patients.
- GLY-06: the card routes IL-6 only to the pituitary. IL-6 also stimulates the adrenal cortex directly, and TNF-α blunts the adrenal response to ACTH.
- GLY-11: "check HbA1c when >180" is wrong; ADA says when glucose is >140 or diabetes is known, if none was done in the past 3 months. No guideline uses HbA1c-tiered targets; LUCID and CONTROLING (stopped early, benefit unlikely and harm possible) showed no benefit.
- GLY-12: "then 4-hourly once stable" does not fit an IV infusion. ADA says every 30 min to 2 h; SCCM says ≤1-hourly during instability.
- GLY-18: "samples every 15 min" describes older devices; current sensors read every 1–5 min. SCCM 2024 makes no CGM recommendation. The AACE/ACE 2016 statement was not verified.
- GLY-21: the DocT GT (GrandT1) key of oral glucose for a confused ICU patient at 48 mg/dL is disputed; IV dextrose 25 g is the safer answer unless a safe swallow is explicit. Card a's "steroids" applies only to adrenal insufficiency.
- Top-up T_a674f960 (comment only, not a card error): the FDA also advises stopping metformin at the time of contrast for eGFR 30–60, liver disease, alcoholism, heart failure or intra-arterial contrast. The UKPDS late macrovascular benefit is fair.
