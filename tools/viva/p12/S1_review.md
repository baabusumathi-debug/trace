# S1 (Shock I) fact-check review, 23 Nov 2026

Checked: every lesson (open, all 25 steps, close), the spines, all 25 drill items, the 42 traps, the 28 mimics, the new card V12-001 and the card flags. Structure, order and caps were re-validated with python after the edits. The JSON is valid, the step order matches the pack, every lesson is 150 to 4,000 spoken characters, no paragraph is over 1,200, no takeaway is over 300, no box is over 400, and the spoken text has no digits or symbols.

## Factual fixes (8)

1. **CS-12, post-cardiotomy timing.** Old: "the output is at its lowest some six to twelve hours after bypass". New: "the output falls over the first hours, classically to a low point around four to six hours after bypass, recovering over the next day". The six to twelve hours in the bank line is when the stem presents, not the nadir. Source: standard cardiac anaesthesia teaching (Breisblatt, JACC 1990: dysfunction is common and recovers). I could not get the exact nadir hour from the web; see Unverified.
2. **CAR-25, RV infarct called an obstruction.** In the takeaway, "is an obstruction before the left heart" became "is a block or a failure before the left heart". In the GT4 trap line, "is obstructive" became "is obstructive, or a failing right ventricle". A right ventricular infarct gives the same high RAP and low PAWP, but it is pump failure, not obstruction.
3. **Same fix elsewhere.** The P12-103 spine line, drill item 1, trap 14 and the close's trap one now all say "obstruction (PE) or RV failure (RV infarct)". The close's "the block sits between the two sides of the heart" became "a pulmonary embolism blocking the way, or a right ventricular infarct failing to pump".
4. **ECHO-19, ASE 2025 top band.** Old: "a vein wider than two point five centimetres that doesn't move at all can be taken as twenty". New: "that collapses by less than half, with dilated hepatic veins, can be taken as twenty". Source: ASE 2025 right heart guideline, Table 4 (IVC >25 mm, <50% collapse, dilated hepatic veins). The card flag for ECHO-19 was corrected to match.
5. **ECHO-27, TAPSE.** Old: "below seventeen millimetres is abnormal". New: "seventeen millimetres or less is abnormal". Source: ASE 2025 says normal is >1.70 cm, and Table 1 grades ≤1.7 cm as mildly abnormal. ASE 2015 said <17 mm, so a "17 mm" option is right under either version.
6. **Close, the spiral.** Old: "a failing pump makes itself worse, because a low pressure starves its own coronary arteries". New: "because the body's own rescue, the sympathetic system and renin, raises the afterload and the filling that the injured heart has to work against". The old line is true physiology, but CS-17 teaches the neurohormonal spiral, so the close now matches the step.
7. **Close, trap two.** "Warm and wet" became "Warm and wet, in heart failure". Without that, it contradicted CS-18, where warm and wet *shock* needs norepinephrine.
8. **CS-08, SCAI attribution.** Old: "Three details from the update of twenty twenty-two". New: "Three details from the current version, the update of twenty twenty-two". The 2022 table has lactate ≥2 for stage C and ≥8 with pH <7.2 (base deficit >10) for stage E, but I could not confirm that these thresholds were new in 2022, so they are no longer presented as additions. The CS-08 card flag was reworded the same way.

## Minor fixes (11)

- **CS-06 takeaway, drill 10, trap 3, mimic 1.** The wedge "above fifteen" / ">15" became "fifteen or more" / "≥15", to match the SHOCK definition (≥15) used in CS-03 and the close.
- **HDM-13 and trap 21.** "an intermittent output" became "a thermodilution output, continuous on some models", because continuous cardiac output PA catheters exist. The point (no EVLW, so PiCCO) is unchanged.
- **ECHO-27.** The A4C marker is now "pointing to the patient's left, towards the left shoulder and armpit", the standard 3 o'clock position. The card says left shoulder, which is acceptable.
- **ECHO-36.** "four goals" became "four imaging goals … and a last step of relating what you saw to the clinical picture". FATE (Jensen 2004) has five steps.
- **CS-22, drill 21, trap 34.** Kerley B "about one centimetre" / "~1 cm" became "one to two centimetres" / "1–2 cm".
- **Drill 11.** The label "(2022)" became "(2022 version)".

## Verified and left as written

- **SHOCK trial (Hochman 1999):** SBP <90 for ≥30 min or support, urine <30 mL/h or cool extremities, CI ≤2.2 with PCWP ≥15.
- **ESC 2016 sign lists, and ESC 2021 / HFA 2020:** cardiogenic shock is hypoperfusion from primary cardiac dysfunction, and "hypoperfusion is not always accompanied by hypotension". Confirmed in the HFA 2020 position statement (Chioncel, EJHF); the ESC 2021 page itself could not be fetched.
- **SCAI 2022:** B has normal lactate, C has lactate ≥2, E has lactate ≥8 with pH <7.2, and E is actual or impending circulatory collapse. The arrest modifier is cardiac arrest with coma (GCS <9, concern for anoxic brain injury). Source: Guideline Central summary of the 2022 update.
- **ASE 2015/2025 RAP bands:** 2.1 cm and 50%, giving 3, 8 and 15. Secondary indices: RA enlargement, IAS bulging, restrictive filling, tricuspid E/e′ >6, hepatic vein systolic filling fraction <55%. RV is normally no more than two thirds of the LV.
- **Forrester:** CI 2.2 and PCWP 18; mortality from a few percent up to about half. The four-quadrant shock grid (AHA 2017) and its SVR pattern are correct.
- **Damping physics:** a long, narrow or compliant line lowers the natural frequency, giving overshoot and a falsely high systolic. Underdamped reads the systolic high and the diastolic low; overdamped is the reverse. A higher amplitude ratio means less damping, which matches the card's ratio-to-ζ values.
- **Fluid responsiveness:** PLR ≥10% CO/SV (ETCO₂ ≥5%, about 300 mL, from 45°), PPV >13%, IVC distensibility >18% ((max−min)/min), tidal volume challenge ΔPPV ≥3.5, EEO >5%, mini-challenge VTI >10%, recruitment SV fall ≥30%, and the ROC families.
- **Other numbers:** Bernoulli and the RVSP of 59 ≈ 60; TRV >2.8 (ESC/ERS 2022); average E/e′ >14 (ASE 2016); PPCM EF <45%; alcohol >80 g/day for >5 years; atrial kick 15–20% rising to about 40%; vascular pedicle >70 mm; the BNP list and sacubitril; the BCI screening rule.
- **Bank figures:** all the bank percentages and question counts in the lessons match the pack's decode lines.
- **Open and close:** apart from fixes 6 and 7, their numbers agree with the steps.
- **Drill:** the answers are correct and unambiguous after the edits above.

## Could not verify

- **The exact LCOS nadir hour** (four to six hours) is from standard texts, not fetched.
- **Whether the SCAI lactate thresholds** for stage C (≥2) and stage E (≥8, pH <7.2) were already in the 2019 table. The text now avoids the claim.
- **The full text of ESC 2021** could not be fetched; the definition was confirmed through HFA 2020 and secondary sources.
- **Whether ASE 2025 still frames the secondary indices** as moving the 8 mmHg estimate to 3 or 15. This is in the writer's ECHO-19 flag; I did not confirm it in the fetched part of the guideline.
- **The ROC ranges in FR-03** are the card's own figures. Published meta-analyses give higher values for PPV and PLR (about 0.9 to 0.95), but the ranking is right.

## Card flags (final list; cards not edited)

1. **CVS03|CS-05** gives the ESC 2016 definition (SBP <90 with adequate volume). ESC 2021 does not require hypotension.
2. **CVS03|CS-08** gives the arrest modifier in its 2019 wording (CPR including defibrillation). In 2022 it is cardiac arrest with coma, meaning concern for anoxic brain injury. The card also omits the typical lactate values (C ≥2; E ≥8, pH <7.2).
3. **CVS05B|ECHO-19** lists RVH among the secondary indices of raised RAP. ASE 2025 lists RA enlargement, IAS bulging, restrictive RV filling, tricuspid E/e′ >6 and hepatic vein SFF <55%. It also gives a 20 mmHg band (IVC >2.5 cm, <50% collapse, dilated hepatic veins).
4. **CVS05B|ECHO-40** is mismatched with other cards. It gives the normal IVC as <20 mm (vs 2.1 cm), uses older E/e′ teaching ("normal <8–10"; raised is now >14), and puts TI <2.5 beside the PH threshold of >2.8. "TVI" here means tissue velocity imaging.
5. **CVS03|CS-11** asks for "four non-ischaemic myocardial causes", but its answer list starts with chronic ischaemia.
6. **New, minor: HY2|CAR-25.** The heading "High RAP + LOW PAWP = obstruction before the left heart" leaves out RV failure (RV infarct), which gives the same pair. This is not added to card_flags in the JSON; add it if wanted.
