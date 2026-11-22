# ENDO01B review (second, independent check), 22 Nov 2026

Files changed: `endo01b_learn.py`, `endo01b_topups_learn.py`. `check_learn.py ENDO01B` OK (10 cards, spine 6 steps). Top-ups: 5 entries, letters a–e match `endo_topups.json`.
The bold restatements match the card answers on all 10 cards and 5 top-ups, and the letters line up. No mnemonics. Punchlines come last.

## Changes, main file
- Header: added a reviewer block listing the sources checked online today, with dates (SSC 2026, SSC 2021, ADRENAL, APROCCHSS, Endocrine Society PAI 2016 full text, Association of Anaesthetists 2020 Table 2, Vinclair 2008). The "unchecked" list is now marked as since checked.
- ENDO-16c: said "Surviving Sepsis 2021 and 2026 decide by the vasopressor need" → now says SSC 2021 (ongoing vasopressor need) and SSC 2026 (conditional suggestion, low certainty) decide on the clinical picture of shock, not a cortisol level. Source: sccm.org SSC 2026 guideline page (Crit Care Med, 23 Mar 2026); Guideline Central and UMEM summaries.
- ENDO-17b: said "usual guidance is about 1 L in the first hour" → now gives the guideline's figure: 1000 mL of isotonic saline within the first hour (Endocrine Society PAI 2016, Table 3).
- ENDO-17d: said "taper over 1–3 days" (not in the guideline) → now says reduce to 100 mg the next day, then taper to oral 15–25 mg/day once the patient is eating (Endocrine Society PAI 2016).
- ENDO-17 table, **factual**: the row "Minor procedure: usual dose ± a single 25–50 mg" was replaced. Association of Anaesthetists 2020 gives body-surface and intermediate surgery the same 100 mg IV at induction plus 200 mg/24 h (or dexamethasone 6–8 mg), then double the oral dose for 48 h. Bowel preparation alone keeps the usual dose. Table title changed to "different settings". Source: Woodcock 2020, Table 2 (Oxford ORA full text).
- ENDO-17 etomidate trap: said "for hours to a day or more" (vague) → now says the effect is greatest at 12–24 h and largely reversed by 48 h (80% at 12 h, 9% at 48 h). Source: Vinclair 2008, Intensive Care Med.
- ENDO-18b: added that etomidate suppression is largely reversed by 48 h (same source).
- ENDO-18c: SSC 2026 now described as a conditional suggestion with certainty downgraded from moderate to low. Its summaries give no new dose or threshold, so the 2021 regimen stands (sccm.org; UMEM). The SSC 2021 threshold (noradrenaline/adrenaline ≥0.25 µg/kg/min for ≥4 h, 200 mg/day) was confirmed only on secondary summaries (open-exam-prep; AAFP gives the 200 mg/day and the 4 h).
- ENDO-18d: figures confirmed (APROCCHSS 43.0 vs 49.1%; ADRENAL 27.9 vs 28.8%, OR 0.95). Added the fludrocortisone dose and duration (50 µg daily, 7 days). Replaced "ended ventilation sooner" with the precise findings: shock reversal 3 vs 4 days, a shorter first ventilation episode, and less transfusion (37.0 vs 41.7%). Source: ADRENAL NEJM 2018 full text (Adelaide repository); NEJM Journal Watch.
- FLAGS: added ENDO-17 (card-layer lines are wrong or conflicting: the minor-procedure dose, and etomidate duration given as 6–48 h in one line and 24–72 h in another). Added ENDO-18 (SSC 2026 is real; dose and threshold are SSC 2021's).

## Changes, top-ups file
- Header: "octreotide crisis dosing as in NANETS guidance" was wrong (NANETS does not give 50–100 µg) → replaced with what was actually checked: ES PPGL 2014, Bancos 2021, NANETS 2017.
- T_fa1bba17 b: "sensitivity 96–100%" kept as the card's wording. Added the guideline figures: about 97% for plasma (99% in Lenders 2002) and 97% for urinary fractionated metanephrines. Also added supine sampling after ≥30 min (seated gives ≈2.8× the false positives). Source: Endocrine Society 2014 PPGL full text.
- T_fa1bba17 c, **factual**: pregnancy mortality "40–50%" is now described as historical (1971 review: 48% maternal, 54% fetal). Added Bancos 2021 (249 pregnancies): maternal death 1%, fetal death about 9%, unrecognised tumour OR 27, no α-blockade OR 3.6, surgery in pregnancy OR 0.9 (no benefit). Also added that a rise of 3× or more is rarely a false positive (ES 2014).
- T_fa1bba17 d: added that the Endocrine Society says 7–14 days of blockade (the card says 10–14).
- T_fa1bba17 e: added the ES warning that labetalol as initial therapy can cause paradoxical hypertension.
- T_022928ac trap: "CRH … rise[s]" was not supported → removed. Now: CBG falls from the start and cortisol half-life rises.
- T_0daf26c0 d, **factual**: the card's "50–100 µg bolus then 50–100 µg/h" is marked as older textbook dosing. NANETS 2017 describes 250–500 µg IV boluses and 100–500 µg/h infusions in practice, and says prophylactic octreotide has not been shown to prevent crisis.
- T_0daf26c0 e: vasopressin or phenylephrine for hypotension is now attributed to NANETS 2017.

## Checked and found right (no change)
- Autoimmune share: card-layer says 80–90%; Endocrine Society says "up to 90% in Western countries".
- Fludrocortisone is unnecessary above 50 mg/24 h of hydrocortisone.
- Crisis doses: 100 mg IV, then 200 mg/24 h.
- Maintenance dose: hydrocortisone 15–25 mg/day.
- Peri-operative cover applies at prednisolone ≥5 mg for ≥4 weeks: 100 mg at induction, 200 mg/24 h, then double the oral dose for 48 h.
- ADRENAL and APROCCHSS mortality figures.
- 2017 CIRCI cut-offs: delta under 9 µg/dL, random under 10 µg/dL.
- Annane 2000 non-responder group.
- Copeptin cut-offs: 21.4, 4.9 and 3.8 pmol/L.
- Lithium mechanism: ENaC entry and GSK-3β inhibition.
- Desmopressin causes hyponatraemia.
- Amiloride is first for lithium DI.

## Final FLAGS
**Main file:**
- ENDO-14: secondary disease "Na, K normal". Potassium is normal, but sodium is often low (cortisol lack leaves ADH unsuppressed).
- ENDO-15: c names only steroid withdrawal. A patient still on chronic prednisone (≥5 mg/day) who becomes septic also needs stress dosing.
- ENDO-16: "random cortisol over 20 excludes" holds only outside critical illness; it also affects sweep item ENDO-23b. b could add the ES peak cut-off (<18 µg/dL / 500 nmol/L).
- ENDO-17: the card is right. The card-layer minor-procedure line (25–50 mg) is pre-2020. The card-layer etomidate durations conflict; the evidence is that suppression is reversible by 48 h.
- ENDO-18: the card is right. SSC 2026 is real (Crit Care Med, March 2026): a conditional suggestion with low certainty, and no new dose or threshold.
- ENDO-20: sarcoid is listed only under nephrogenic; it is primarily central.
- ENDO-22: the card does not say that amiloride is first for lithium DI. The two DocT keys conflict.

**Top-ups:**
- T_fa1bba17: the 40–50% pregnancy mortality is historical; the modern figures are about 1% maternal and 9% fetal. The blockade duration in ES 2014 is 7–14 days. GrandT1 Q141's labetalol key is wrong.
- T_0daf26c0: the octreotide 50–100 µg doses are older. NANETS 2017 describes 250–500 µg boluses and 100–500 µg/h infusions, and prophylaxis is unproven.

## Not verifiable today
- **SSC 2021 threshold:** confirmed only on secondary summaries. The primary rationale page and the PMC full texts were behind reCAPTCHA.
- **SSC 2026 full text:** no dose or threshold could be seen.
- **SCCM/ESICM 2017 ">0.1 µg/kg/min" and "250 µg over 1 µg":** kept as the writer checked them, not re-fetched.
