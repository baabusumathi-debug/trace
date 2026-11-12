# SPECIAL01 — independent review of special01_learn.py and special01_topups_learn.py (13 Nov 2026)

Checker: `python3 check_learn.py SPECIAL01` → `SPECIAL01 18 cards 18 entries OK`, `v3 spine 6 steps OK`.
Top-up (no checker) checked by hand: all three parts start with the bold restated answer line in order, all mimic/trap/decode pairs have 2 items, punch 208 characters (limit 320), no banned phrases.

## Changes (card: what was wrong → what it says now; source)

### Factual
- DONOR-09 e (part, FLAG): "mild hypothermia … harms the heart" was unsupported → Niemann NEJM 2015 benefit stated (DGF 28% vs 39%, 34–35 °C vs 36.5–37.5 °C), a later three-arm trial found donor hypothermia inferior to kidney machine perfusion, effect on thoracic organs untested. Source: The Bottom Line summary of Niemann 2015; OHSU record of "Hypothermia or Machine Perfusion in Kidney Donors" (NEJM).
- DONOR-09 e: "sodium over 155 is linked to worse liver graft function" stated flat → linked to early liver graft dysfunction in older series, later series less consistent. Source: Totsuka, Liver Transpl Surg 1999 (doi 10.1002/lt.500050510) and later Liver Transpl cohorts.
- DONOR-12 b (part, FLAG): "low-dose hydrocortisone (300 mg then 100 mg 8-hourly) was non-inferior in one study" → dose removed (not traceable); observational comparisons found similar pressor needs, lung function and organ yield with less hyperglycaemia; accepted by some guidelines. Source: Dhar et al., J Crit Care 2012 (PMID 22762934), Cureus poster 299 (132 donors).
- DONOR-16 a: "a CD4 count of 180 shows HIV infection" (a low CD4 alone does not prove HIV) → "in the Marrow stem the CD4 count of 180 is the clue to HIV infection with AIDS". Source: qpack DONOR-16 stem and note.
- DONOR-17 b: "ECD kidneys have about 1.7 times the risk of graft failure" → ECD defined as relative risk of graft failure above 1.7 vs an ideal donor (UNOS 2002 definition).
- DONOR-07 e: "the posterior pituitary fails first" → fails more often than the anterior (its supply is entirely intracranial); the timing claim was not supportable.
- DONOR-04 a: "in a known CO₂ retainer the target is 20 above his own baseline" → his own baseline is used; when uncertain, an ancillary test is the safer route. Source: MSD Manual table of the 2023 guideline (use the patient's baseline in chronic hypercarbia).
- DONOR-05 e (part, FLAG): "the 2023 guideline says they should not be used" → the guideline does not accept CTA/MRA because they are not validated. Source: UAB 2025 brain-death policy built on the 2023 guideline ("have not been validated"); PulmApp summary.
- DONOR-01 a (part, FLAG): "about 4 lakh die waiting" unexplained → stated as an estimate; the Health Ministry figure usually quoted is about 5 lakh a year; gap to Spain "nearly 60-fold" → "more than 60-fold" (53.9 / 0.8). Source: Asian Age (Health Ministry, 2017) "5 lakh die each year due to lack of organs"; La Moncloa (Aug 2025): Spain 53.9, USA 49.7 pmp in 2024; Tribune/NOTTO 2024: India under 1 pmp, 1,128 deceased donors.
- T_59eb957d c (part, FLAG, header): category V "in the Madrid addition" and euthanasia "in the modified Paris 2013 version" → V as unexpected in-hospital arrest was the 2000 addition; Madrid 2011 has I–IV only; euthanasia is the Belgian 2012 modification (Detry), mentioned only in a footnote of Paris 2013, which folds in-hospital arrests into IB/IIB and makes IV controlled or uncontrolled. Source: Thuong et al., Transpl Int 2016 (tri.12776), tables 2–4; Wikipedia NHBD table (V added 2000).

### Minor
- DONOR-15 trap: "antibiotics for 24–48 h" contradicted the card's 48 h → "about 48 h before retrieval".
- DONOR-02 FLAG: "drug-level cut-offs not re-checked" → confirmed (barbiturate <10 µg/mL, VUMC 2023 algorithm; thiopentone <5 mg/L, ICSI 2025).
- DONOR-09, DONOR-12 FLAGS updated to match the parts.

### Checked and left unchanged
- 2023 AAN/AAP/CNS/SCCM guideline: core ≥36 °C; adults SBP ≥100 and MAP ≥75; 24 h after rewarming if ≤35.5 °C; one exam and one apnoea test in adults; children two exams and two apnoea tests ≥12 h apart; apnoea test 100% O₂ ≥10 min, baseline PaCO₂ 35–45 / pH 7.35–7.45, consistent with PaCO₂ ≥60 AND ≥20 above baseline with pH <7.30; O₂ 6 L/min by catheter or CPAP; ECMO sweep 0.2–1 L/min, VA-ECMO gases from circuit and distal arterial line; accepted ancillary tests 4-vessel angiography, radionuclide perfusion, TCD (adults only); EEG and evoked potentials not accepted. Sources: PulmApp summary; UAB policy 2025; MSD Manual table. (The MSD table still lists EEG; it mixes older paediatric criteria — PulmApp and UAB both state EEG is not acceptable.) Five half-lives for depressants: not reproduced by the pages opened, kept from the writer's Guideline Central check.
- THO (Amendment) Act 2011, s 3(1A) required inquiry and duty to inform the retrieval centre; s 3(6) board (RMP in charge, independent nominated specialist, neurologist/neurosurgeon, treating RMP) and proviso (surgeon or physician and anaesthetist or intensivist, not on the recipient's transplant team) — confirmed (advocatekhoj bare act). Form 10: six hours minimum between tests in adults, longer in children at the experts' discretion — confirmed (SOTTO Goa Form 10). What happens when the family declines is not in the Act or Form 10; part d already marks it as "per your notes".
- Dhar NEJM 2023 levothyroxine: 838 donors, 30 µg/h ≥12 h, hearts transplanted 54.9% vs 53.2%, 30-day graft survival similar, more severe hypertension and tachycardia — confirmed (2 Minute Medicine).
- Mascia JAMA 2010: 118 donors, eligible 95% vs 54%, harvested 54% vs 27%, VT 6–8, PEEP 8–10, CPAP apnoea tests, closed suction — confirmed (Università del Piemonte Orientale record).
- PaCO₂ rise about 3 mmHg/min (Deranged Physiology); cold caloric at least 50 mL ice water (ICSI 2025; some protocols 60 mL) — consistent.
- Hormone doses: T4 20 µg then 10 µg/h; T3 3 µg/h; vasopressin 0.5–4 U/h (>2.4 U/h risks regional ischaemia); methylprednisolone 15 mg/kg — confirmed (ANZICS; LAC-USC protocol). T3 4 µg bolus and IV desmopressin 1–4 µg then 1–2 µg 6-hourly are standard Crystal City/SCCM figures, not re-opened.
- HOPE Act (2013), KDPI replacing ECD/SCD (2014), cold ischaemia times, Cushing triad — standard; not changed.

## Final FLAGS — special01_learn.py
- DONOR-01: comparison figures dated (2024: Spain 53.9, USA 49.7 pmp; India about 0.8). Amendment is THO (Amendment) Act 2011; Rules 2014 put it into effect. "About 4 lakh die waiting" is an estimate; usual Health Ministry figure about 5 lakh.
- DONOR-02: Card agrees with 2023 guideline (≥36 °C, SBP ≥100); guideline adds MAP ≥75, 5 half-lives, 24 h after rewarming from ≤35.5 °C. Linked Marrow key (post-OHCA, no TTM yet) disputed. Drug-level cut-offs confirmed.
- DONOR-03: Card correct.
- DONOR-04: 2023 guideline needs PaCO₂ ≥60 AND ≥20 above baseline with pH <7.30 (card "or" is older wording). ECMO apnoea testing not on the card.
- DONOR-05: 2023 guideline no longer accepts EEG or evoked potentials; accepts angiography, radionuclide perfusion, TCD (adults); does not accept CTA/MRA (not validated). Radionuclide scan not on card. Linked DocT GT key uses PET, not a standard ancillary test.
- DONOR-06: Board per Act and 2011 proviso; Form 10, 6 h in adults confirmed; US 2023 one exam in adults. d ("per your notes") not verifiable; practice varies.
- DONOR-07: Cushing's triad also includes irregular respiration (added as extra).
- DONOR-09: Hb 10 / Hct 30% is old (SCCM 2015, Canada 2020: Hb >7). Glucose 80–150 tighter than SCCM <180. Temperature and sodium nuance as above.
- DONOR-12: Routine thyroid hormone not supported (NEJM 2023). Vasopressin 0.5–4 U/h exceeds SCCM 0.01–0.04 U/min. Low-dose hydrocortisone an alternative on observational evidence.
- DONOR-14: PEEP 5–10 lower than Mascia/JHLT (8–10).
- DONOR-15: Hct over 30% dated (Hb 7).
- DONOR-16: HBsAg-positive as absolute is dated; HIV-to-HIV transplantation allowed under the US HOPE Act and in South Africa.
- DONOR-17: 50–59 row printed under STANDARD; it is an ECD rule. KDPI replaced ECD/SCD in the USA in 2014.
- DONOR-18: Lungs 4–6 h conservative (many sources 6–8 h).

## Final FLAGS — special01_topups_learn.py
- T_59eb957d: Card correct. Category V differs by version (unexpected in-hospital arrest in the 2000 addition; euthanasia in the Belgian 2012 modification, footnote only in Paris 2013). Category IV is uncontrolled or controlled in Paris 2013.
