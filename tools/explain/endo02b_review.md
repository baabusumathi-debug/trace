# ENDO02B review (second, independent check), 22 Nov 2026

Files checked: endo02b_learn.py (23 cards) and endo02b_topups_learn.py (T_6f96ae33), checked against cards/ENDO02B.jsonl, qpack/ENDO02B.md and endo_cardlayer.json. Letters and bold restatements match the cards on every card. `check_learn.py ENDO02B` prints OK (23/23, spine 6). The top-up file loads.

Sources re-read: ADA 2006 consensus (scispace PDF, Table 1); ADA 2009 consensus text (slideshare copy) and its flowchart as WikiDoc reproduces it; 2024 consensus (PMC11343900, Diabetologia twin); ISPAD 2022 ch. 11 (Stony Brook PDF); JBDS HHS quick-reference guide (MKUH NHS PDF); Mayo Clinic review of DKA in pregnancy.

## Changes
Factual:
- DKA-17 a: said that 100 mmol of 8.4% bicarbonate in 400 mL water is "roughly isotonic". That was wrong: it is about 400 mOsm/L, still hypertonic, diluted from about 2000 mOsm/L (arithmetic; ADA 2009 regimen).
- DKA-11 a: said nothing against the card's HHS water deficit of 100–150 mL/kg. It now says the ADA table gives 100–200 mL/kg (about 9 L, against 6 L in DKA) (Kitabchi 2006 Table 1, carried into 2009).
- DKA-11 d: added that the 2009 and 2024 texts put the average phosphate deficit at about 1 mmol/kg, against the table's 5–7 (ADA 2009 text; 2024 consensus).
- DKA-19 b: said "0.5–1% of paediatric DKA, mortality up to a quarter". It now says 0.5–0.9% and 21–24% (ISPAD 2022), and adult incidence under 0.1% (2024 consensus).
- DKA-18 b: said the 2024 threshold was "low phosphate". It now says "<1.0 mmol/L with muscle weakness such as respiratory or cardiac compromise", which is the 2024 consensus wording, and points out the unit clash with ADA 2009's 1.0 mg/dL (0.32 mmol/L).
- DKA-16 a: removed "2024 adds glucose ideally below 200" from the resolution criteria. Neither the writer's header nor my re-read supports it (2024 consensus).
- DKA-15 a: removed the reason "bolus kept for when IV access is delayed", which I could not verify. It now says the bolus is optional because it adds nothing once 0.1 U/kg/h runs.
- DKA-05 b: removed "at 3.0 mmol/L, sensitivity and specificity exceed 90%", which I could not verify.
- DKA-02 b: "mixed crises carry the highest mortality of the three in that data" was not in the 2024 text. It now reads "linked with higher mortality than DKA alone".
- DKA-12 b: the 2024 rule "0.45% only if osmolality is not falling" now says it comes from the HHS section, and adds "an early sodium rise is not by itself a reason for hypotonic fluid" (2024 consensus).

Minor or depth:
- DKA-15 b: added why the ADA 2009 rule uses 0.14 U/kg/h.
- DKA-15 e: added that 200–300 comes from the ADA 2009 flowchart while its text says 250–300, and that JBDS aims for 10–15 mmol/L with a fall of 5 mmol/L/h or less (JBDS HHS guide).
- DKA-18 c: 4.5 mmol/h now cited to ADA 2009 as "maximum generally regarded as safe", with the hypocalcaemia mechanism.
- DKA-23 b: JBDS insulin start made exact (0.05 U/kg/h once glucose stops falling; at once if BHB >1 mmol/L), and the 2024 consensus noted as only mentioning this approach.
- DKA-14 c, d: "never in severe DKA" changed to "IV needed in severe DKA and HHS"; "prevents rebound / shortens resolution" softened to "reduces rebound".
- DKA-12 a: 250 mL boluses now for older adults, heart failure or dialysis (2024 wording).
- DKA-02 a: ICU criteria now match the 2024 wording (severe DKA, HHS, altered mental status).
- DKA-01 c, DKA-03 d: "glucose often over 1000" changed to "can exceed 1000".
- DKA-21 trap: "contraindicated in pregnancy" changed to "not used in pregnancy".
- Top-up T_6f96ae33 d: "no buffer left" made precise. The Winter's and Henderson–Hasselbalch arithmetic re-checked correct (pH 7.15 / 6.72).
- Header: second-review source list added, replacing the "blocked / from memory" lines.

Settled (no text change needed):
- ADA 2009 figures:
  - 0.14 U/kg/h without a bolus: confirmed.
  - The 10% first-hour rule, then a 0.14 U/kg bolus: confirmed.
  - K bands 3.3 / 5.2 (text "5.0–5.2"; 5.3 was ADA 2006): confirmed.
  - Phosphate <1.0 mg/dL at 4.5 mmol/h: confirmed.
  - Bicarbonate at pH <6.9, 100 mmol in 400 mL with 20 mEq KCl over 2 h: confirmed.
  - Insulin 0.02–0.05 U/kg/h once dextrose is added: confirmed.
  - 0.5–0.8 U/kg/day: confirmed.
- Morris 1986: the "small RCT at pH 6.9–7.14" is consistent with ADA 2009, which describes 21 patients at pH 6.9–7.1.
- Glaser 2001 risk factors (hypocapnia, high urea, bicarbonate): agree with ISPAD 2022.
- PECARN FLUID: no difference in mental status or cerebral injury with fast vs slow fluids or 0.9% vs 0.45% saline (1389 episodes). The writer's text is correct.
- ISPAD 2022 doses confirmed: mannitol 0.5–1 g/kg over 10–15 min, and 3% saline 2.5–5 mL/kg over 10–15 min. ISPAD's severe grade is pH <7.1 or HCO3 <5, which supports the DKA-05 trap.
- JBDS HHS targets confirmed: glucose 10–15 mmol/L in 24 h; Na fall ≤10 mmol/L in 24 h; osmolality fall 3–8 mOsm/kg/h.
- Fetal mortality in DKA in pregnancy: the card's 9–35% agrees with the literature (Mayo review 10–35%). No flag.
- 2024 consensus figures confirmed:
  - Mortality 0.20–1.04%, with HHS 5–10 times higher.
  - DKA 38%, HHS 35%, mixed 27%.
  - Euglycaemic DKA about 10%.
  - SGLT2-associated DKA about 4% in type 1.
  - K ≤2.5 linked to threefold mortality.
  - LMWH prophylaxis.
  - Overlap of 1–2 h.
  - 0.5–0.6 U/kg/day.

## Final FLAGS
- DKA-02: ICU 13% untraceable (2024 gives no %). Overlap one-third agrees.
- DKA-04: card percentages are older ranges. The 2024 ranges are infection 14–58% (DKA) and 30–60% (HHS); insulin omission 41–60% is US data only.
- DKA-05: the card-layer phrase "card's 250 mg/dL" is out of date; the card is fine.
- DKA-06: the AG grading is ADA 2009. 2024 grades by pH, HCO3 and BHB; HHS is pH ≥7.3 and HCO3 ≥15.
- DKA-08: phosphate is usually normal or high at presentation, not low. "Pseudohyponatraemia" here is really translocational.
- DKA-11: card HHS water 100–150 mL/kg does not match the ADA table's 100–200 (new firm flag). The phosphate deficit in the table (5–7) differs from the ~1 mmol/kg in the text.
- DKA-12: card d "no crystalloid proven better" vs 2024's faster resolution with balanced crystalloids; the 0.45% rule (2024 HHS section); HHS dextrose at 250 not confirmable from the 2024 text.
- DKA-13: card matches 2024. Watch line confirmed (5.2 = ADA 2009, 5.3 = ADA 2006). The DocT "falsely elevated" wording is loose.
- DKA-15: a and b confirmed ADA 2009. e is the ADA 2009 flowchart (text 250–300); 2024 sets no HHS target; JBDS 10–15 mmol/L.
- DKA-16: 0.5–0.8 is ADA 2009; 2024 says 0.5–0.6 (0.3 if high risk). The overlap agrees.
- DKA-18: b and c confirmed ADA 2009. The 2024 text says "<1.0 mmol/l" with weakness or cardiorespiratory compromise, possibly a unit slip.
- DKA-19: "large fluid volumes" weakened by PECARN FLUID. ISPAD gives 0.5–0.9% and 21–24%. The DocT adult-HHS key is best-of-options only.
- DKA-21: DocT glucose 240 = euglycaemic DKA follows the old 250 cut-off.
- DKA-22: "HHS more common than DKA" is Marrow only.
- Top-ups: no flags.
