# ENDO01A: independent review, 22 Nov 2026

Files checked: `endo01a_learn.py` (13 cards) and `endo01a_topups_learn.py` (2 top-ups), against `cards/ENDO01A.jsonl`, `endo_topups.json["ENDO01A"]`, `endo_cardlayer.json` and `qpack/ENDO01A.md`.
`check_learn.py ENDO01A` gives OK (13/13, spine 6 steps OK). I checked the top-ups by hand: every part starts with the bold top-up line, the letters a–e follow the `a` list, each pair has 2 items, and the punches are 179 and 136 characters.

The checks found no wrong mechanism and no wrong key. All letters and bold restatements match the cards. Every trap matches the qpack cohort figures. The changes are: guideline positions that were missing or simplified (JTA 2016), unverified figures now confirmed or corrected, two overstated top-up lines, and the Burch–Wartofsky heart-rate band.

## Changes (card: what was wrong → what it says now; source)

- ENDO-01 a: said "perchlorate and radioiodine act at this step" (radioiodine does not block the symporter) → now says perchlorate blocks the symporter and radioiodine enters the gland through it. Standard physiology.
- ENDO-04 a: "storm is rare (about 0.2–0.8 per 100,000 a year)" mixed a per-hospitalised rate with a population rate, and the card's 1% / 3:1 had no context → now gives US NIS 2016–2020 figures (2.5% of thyrotoxicosis admissions, about 72% women, in-hospital mortality 3–5%), Japan 11%, reviews 10–25%, and population incidence of about 0.6–1 per 100,000 a year. Sources: Seo et al., Am Surg 2024; Akamizu 2012; Endotext.
- ENDO-05 b: "altered mentation is a strong predictor of death" (not verified) → now says CNS signs make the Japanese criteria definite and score up to 30 on Burch–Wartofsky.
- ENDO-06 b: added that reproductions of the 1993 table differ on the first heart-rate band (99–109 vs 90–109; MDCalc prints 90–109) and that the other bands are the same. Sources: MDCalc review; a 2017 reproduction citing Burch–Wartofsky 1993.
- ENDO-07 b: TS2 definition was incomplete → added "or a TS1 picture before hormone results". Akamizu 2012 / JTA criteria.
- ENDO-07 d: said the card's "from 90" is wrong (writer's FLAG) → now says both versions circulate and the FLAG is about the mismatch between the two cards, not a clear error.
- ENDO-07 g: "bilirubin cut-off was the one item added" → "the only change between the first and final criteria concerned the bilirubin > 3 mg/dL threshold". Akamizu 2012 abstract.
- ENDO-08 a: the JTA 2016 β-blocker position was missing → added: β₁-selective drugs first (landiolol or esmolol IV, bisoprolol 2.5–5 mg/day orally), propranolol not recommended for the tachycardia, rate target ≤130, digitalis for AF. JTA/JES 2016 full text.
- ENDO-08 b: the PTU preference was given without its source → now gives the ATA 2016 preference and doses, and adds that JTA 2016 accepts methimazole 60 mg or PTU 600 mg/day and finds methimazole no worse. JTA 2016; Endotext.
- ENDO-08 c: added JTA 60 mg/day (IV methimazole 30 mg/day in Japan) next to ATA 60–80 mg/day.
- ENDO-08 d: added that JTA 2016 gives iodide (about 200 mg/day) at the same time as the thionamide; ATA 2016's "at least 1 h after" stays the exam answer. JTA 2016.
- ENDO-08 e: the steroid dose had no source → now gives ATA 300 mg IV then 100 mg 8-hourly, and JTA 300 mg/day or dexamethasone 8 mg/day. JTA 2016; Endotext.
- ENDO-08 mimic, PTU vs methimazole mimic and trap 1: "JTA prefers landiolol or esmolol at Killip III or more" was a simplification → now says JTA uses short-acting landiolol or esmolol for fast rates in heart failure, with digitalis for AF, and prefers β₁-selective drugs. JTA 2016 Recommendations 8–9.
- ENDO-09 b: "ATA 2016 and most guidelines" → names ATA and JTA, and gives each one's iodine timing.
- ENDO-09 e: "if all fails, plasma exchange" → JTA 2016: consider plasma exchange if there is no improvement in 24–48 h; thyroidectomy last.
- ENDO-09 mimic (levothyroxine overdose): "thionamides and iodine do nothing" → blocking synthesis or release does nothing, but PTU, propranolol and steroids still reduce conversion.
- ENDO-09 trap 1: reader-facing text quoted "the qpack note" → reworded as "Some argue methimazole is the odd one out…". The key (iodine) is still defended. Both ATA and JTA accept methimazole.
- ENDO-10 a: added incidence of 0.22 per million/year (Western) and 1.08 per million/year (Japan), Japanese in-hospital mortality of about 30%, and that the card's 0.01% could not be traced. Sources: patient.info; Endotext "Myxedema and coma".
- ENDO-10 d: there was no temperature cut-off → hypothermia is defined in reviews as below 35–35.5 °C, lower is worse, and the card's 33 °C is not a standard cut-off; the mechanism is added. Sources: patient.info; 2024 Popoveniuc-score review; Endotext.
- ENDO-12 b: "ATA 2014 figures" was not verified → confirmed (T4 200–400 µg load; T3 5–20 µg then 2.5–10 µg 8-hourly). Added that 1.6 µg/kg × 75% ≈ 1.2 µg/kg/day IV, and that older texts load 300–500 µg. Sources: EMCrit IBCC citing Jonklaas 2014; Endotext.
- T_2b8a9a37 a: added that the firm deiodinase changes are type 1 down and type 3 up, while type 2 changes are inconsistent. Endotext NTI; StatPearls.
- T_2b8a9a37 c: T4 < 4 µg/dL was "about 50%" with no source → confirmed "up to about 50%"; added < 2 µg/dL about 80% and that the link is an association, not a cause. Endotext NTI; StatPearls.
- T_2b8a9a37 d: TSH overshoot "10–20" → transiently above normal, usually below 20; TSH > 20 makes primary disease likelier. StatPearls.
- T_2b8a9a37 e: "trials have shown no benefit" → "have not shown benefit"; added "retest at least 6 weeks after discharge" (some sources). StatPearls.
- T_38ffd8d5 a: "because thyroid function is usually normal" (overstated) → most reported cases have subclinical or overt hypothyroidism, but the encephalopathy does not track thyroid function. Chong 2003 data as summarised on Wikipedia.
- T_38ffd8d5 c: CSF protein is raised in many cases but not all; the EEG is abnormal in nearly all; prion disease added to the exclusions.
- T_38ffd8d5 d, e: these parts only restated the top-up → added the reported regimens (IV methylprednisolone 1 g/day for 3–7 days, or prednisolone 50–150 mg/day, then a slow taper; relapse is common) and that there are no controlled trials.
- Header comments of both files: the "from memory" lists are replaced with what was confirmed online today.

I checked these and left them as written: synthesis steps; T3/T4 half-lives, potency and free fractions; TSH patterns; the Riedel FLAG; Burch–Wartofsky bands and thresholds; JTA criteria (fever ≥ 38, HR ≥ 130, heart failure items, bilirubin > 3); ATA 2016 storm doses (Endotext); paracetamol not aspirin (JTA 2016 Recommendation 5); the order of storm treatment; myxoedema hydrocortisone-first logic, passive rewarming and acquired von Willebrand; the hyponatraemia mechanism; all cohort percentages and decode lines against the qpack.

## Final FLAGS

- ENDO-03: Riedel thyroiditis is not a recognised cause of destructive thyrotoxicosis. "Secondary hypothyroid: TSH low" is better written "low or inappropriately normal".
- ENDO-04: "1% of hospitalised hyperthyroid patients" is an older figure; US NIS 2016–2020 gives 2.5%, with about 72% women. Mortality of 10% matches Japan (10.7–11%); recent US in-hospital mortality is 3–5%. Not wrong for the exam.
- ENDO-07: Burch–Wartofsky "from 90" does not match ENDO-06 (99–109). Both versions circulate (MDCalc prints 90–109), so the deck is inconsistent rather than one card being wrong.
- ENDO-08: Methimazole "10–50 mg 6-hourly" is unclear and probably low (ATA 60–80 mg/day, JTA 60 mg/day). Lithium: some sources give 8-hourly. "PTU preferred" and "iodine ≥ 1 h after" are ATA 2016 positions; JTA 2016 accepts methimazole and gives iodide with the thionamide. JTA does not recommend propranolol for the tachycardia. The GT5 key stands, with esmolol equally supported. The card-layer "Killip ≥ III" wording is a simplification.
- ENDO-09: The card calls iodine "second line"; ATA and JTA both make it part of the initial regimen. The GT2o key (iodine) is defended over the qpack note's methimazole.
- ENDO-10 (new): The prevalence of 0.01% could not be traced (published incidence is about 0.22 per million/year in the West and 1.08 per million/year in Japan). Hypothermia "under 33 °C" is not a standard cut-off (reviews use below 35–35.5 °C). "TSH usually over 100" is not a defining criterion.
- ENDO-11: The ECG row leaves out T-wave flattening or inversion (DocT's key). "Hyponatraemia (high ADH)" gives only the secondary mechanism.
- T_2b8a9a37 (new): "Cuts type 1 and 2 deiodinase": the firm changes are type 1 down and type 3 up; type 2 changes are inconsistent. The "10–20" TSH overshoot is not a fixed range (usually below 20).
- T_38ffd8d5 (new): "Usually EUTHYROID" is overstated; most reported cases have subclinical or overt hypothyroidism. Methylprednisolone regimens run 3–7 days.

Could not open: the ATA 2016 and ATA 2014 full texts (PMC blocked by a browser check). Their doses were confirmed through secondary sources that cite them (Endotext, EMCrit). The exact dose of the ATA 2014 hydrocortisone recommendation was not seen; "about 100 mg 8-hourly" rests on Endotext and patient.info. The original 1993 Burch–Wartofsky paper was not seen, so the 90 vs 99 band cannot be settled.
