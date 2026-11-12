# SPECIAL03 — independent review of special03_learn.py and special03_topups_learn.py (13 Nov 2026)

Checker: `python3 check_learn.py SPECIAL03` → `SPECIAL03 17 cards 17 entries OK`, `v3 spine 6 steps OK`.
Top-up (no checker) checked by hand: all four parts start with the bold restated answer and match the card lines in order; every mimic, trap and decode item is a 2-item pair; punch is 193 characters (limit 320); no mnemonics.
Fidelity: every bold restatement in special03_learn.py matches its card answer letter by letter; no changes needed.

## Changes (card: what was wrong → what it says now; source)

### Factual
- NUT-07 b, trap, FLAG: ESPEN was said to recommend "low-dose EN" in spinal cord injury, abdominal trauma, TBI, ECMO, prone position, open abdomen and diarrhoea → "early EN" (ESPEN's low-dose recommendation, R39, covers hypothermia, intra-abdominal hypertension without ACS and acute liver failure). Neuromuscular blockade dropped from the list (not in the R40 wording seen). Source: ESPEN 2023 practical guideline (Singer, Clin Nutr 2023), Rec. 8 (R40) and Rec. 12 (R39).
- NUT-13: "ESPEN gives low-dose EN in diarrhoea" → "ESPEN recommends early EN even with diarrhoea". Source: same, R40.
- NUT-13: erythromycin "for up to about 3 days" → 24–48 hours, prokinetics stopped after 3 days because they lose effect. Source: ESPEN 2023, Rec. 55 commentary.
- NUT-09 d (and NUT-09 FLAG): ESPEN adjusted body weight "ideal weight plus a third of the excess" → "ideal weight plus 20–25% of the excess", used for energy and protein 1.3 g/kg/day. Source: ESPEN 2023, Rec. 52 and commentary.
- NUT-12 e (and NUT-12 FLAG): Doig trial "calorie restriction improved survival" → primary outcome (days alive after ICU discharge) neutral; 60-day mortality lower as a secondary outcome; 339 patients; restriction began at about 480 kcal/day for 2 days. Source: Doig, Lancet Respir Med 2015 (The Bottom Line summary: 39.9 vs 44.8 days, p = 0.19; alive at day 60 91% vs 79%).
- NUT-12 b: refeeding hypophosphataemia "usually defined in ICU studies" → the Doig trial definition stated as such (<0.65 mmol/L, a fall of >0.16 mmol/L, within 72 h). Source: as above.
- NUT-12 e: "many units give IV phosphate below about 0.6 mmol/L" (unsourced) → IV for severe (<0.3 mmol/L), symptoms or an unreliable oral/enteral route, which in ventilated tube-fed patients often extends IV use to moderate levels (0.3–0.6 mmol/L). Source: Gloucestershire NHS hypophosphataemia guideline (moderate 0.3–0.6, severe <0.3; IV for severe, symptomatic or when oral route inappropriate).
- NUT-10 a: "the lower arms had fewer GI complications" (stated for all four trials) → only where reported: EDEN, NUTRIREA-3, and TARGET (more vomiting 18.9 vs 15.7% and larger residuals with 1.5 kcal/mL). Source: TARGET, NEJM 2018 (full text); NUTRIREA-3 ISICEM 2023 report (less vomiting, diarrhoea, bowel ischaemia, liver dysfunction in low arm).
- NUT-15 b: ASPEN 2022 "do not start SPN before day 7" → adds that this does not apply to the malnourished or those with little lean mass. Source: ASPEN 2021/22 guideline factsheet (nutritioncare.org).
- NUT-16 a: "glucose ≤5 mg/kg/min (ESPEN, ASPEN), lipid ≤1.5 g/kg/day (ESPEN) or 20–30% of calories" → ESPEN glucose/carbohydrate ≤5 mg/kg/min and IV lipid ≤1.5 g/kg/day counting non-nutritional lipid such as propofol; 20–30% described as common practice, not a guideline limit; ASPEN attribution removed (not confirmed). Source: ESPEN 2023 Rec. 27 and Rec. 29 (commentary also confirms propofol 1.1 kcal/mL).
- NUT-06 b (and FLAG): Freka tube 110–120 cm could not be verified → kept in the bold restatement (card text) and followed by a softening sentence: Freka endoscopic nasojejunal tubes (Endolumina, EasyIn) are listed at 270 cm and cut to length after placement. Source: Fresenius Kabi UK product pages; Deranged Physiology (short-term jejunal tubes about 100–150 cm).
- NUT-06 b: high aspiration risk as a post-pyloric indication attributed to ASPEN only → ESPEN and ASPEN. Source: ESPEN 2023 Rec. 13; ASPEN 2016.
- T_3d23a130 a: added the primary figure behind "only about 10%": Harper's autopsy series 131 cases, triad 16%, no recorded signs 19%; Caine criteria noted as derived in alcohol-dependent patients. Source: Harper, J Neurol Neurosurg Psychiatry 1986 (PMC abstract); CMAJ 2014 review (Box 1).
- T_3d23a130 c and FLAG: regimen attribution softened: EFNS "at least 200 mg three times daily IV" confirmed; the 500 mg tds then 250 mg daily schedule described as the commonly quoted high-dose regimen (Thomson/RCP 2002, Sechi and Serra 2007), originals not opened; some UK protocols use two pairs of Pabrinex tds for 5–7 days. Source: CMAJ 2014; BNSSG NHS Pabrinex protocol v5.2.

### Minor
- PRIMER: "the exam usually follows ASPEN numbers in DocT stems" (unverifiable generalisation) → "the DocT stems linked to this deck mostly use ASPEN numbers".
- NUT-09 a: indirect calorimetry "typically 15–30 minutes" → AARC steady state: 5 minutes with ≤5% variation in gas readings, longer if not. Source: AARC CPG Metabolic Measurement during Mechanical Ventilation (2004).
- NUT-09 b: ESPEN "20–25 kcal/kg/day as the eventual target" → ESPEN's fallback weight-based estimate when nothing can be measured, at ≤70% early. Source: ESPEN 2023 Rec. 21 commentary.
- NUT-10 b: EFFORT Protein "associated with harm in AKI or higher SOFA" → "signals of harm … (exploratory subgroups)". Source: EFFORT Protein, Lancet 2023 (AKI interaction RR 1.4 for 60-day mortality, hypothesis-generating).
- NUT-14 d: "PN often over 900 mOsm/L" → standard PN is far above the roughly 850–900 mOsm/L a peripheral vein tolerates (ESPEN 850, ASPEN 900).
- Header comments of both files updated to record what was re-checked.

### Checked and left unchanged (confirmed online)
- NUTRIC: original 0–10, high risk ≥6; modified 0–9, high risk ≥5 (Heyland 2011; Rahman 2016, as cited by Jeong, Nutrients 2018). Band values match Heyland 2011 as known; no open source reproduced the full table today (one R-package page gives wrong bands).
- ASPEN 2016: high risk NRS-2002 ≥5 or NUTRIC ≥5 without IL-6; low risk NRS-2002 ≤3 or NUTRIC ≤5; high risk advanced to goal over 24–48 h; low risk no specialised nutrition in week 1; SPN considered after 7–10 days if EN <60%; exclusive PN as soon as possible in high-risk patients when EN impossible; GRV not routine, no holds below 500 mL; post-pyloric for high aspiration risk; obesity 11–14 kcal/kg actual (BMI 30–50), 22–25 kcal/kg IBW (BMI >50), protein 2.0 g/kg IBW (BMI 30–40) up to 2.5 (≥40). Sources: Guideline Central summary of McClave 2016; Nestlé summary.
- ASPEN 2021/22: 12–25 kcal/kg in days 1–7/10; protein 1.2–2.0 g/kg kept; EN or PN acceptable.
- AARC: open-circuit IC inaccurate at FiO₂ >0.60; valid RQ 0.67–1.3; leaks (circuit, cuff, chest tube, BPF) and dialysis invalidate.
- ESPEN 2023: early EN within 48 h; delay-EN list (R11) exactly as written; ICU >48 h = at risk; IC recommended; ≤70% early; protein 1.3 g/kg progressively; glutamine R30–32 (burns >20% TBSA, trauma 0.2–0.3 g/kg for 5 days, not others); SPN days 4–7 (commentary, not clearly established); PN within 3–7 days if EN contraindicated; refeeding R58/R59; post-pyloric R16; propofol 1.1 kcal/mL.
- REDOXS: multi-organ failure, IV + enteral glutamine; 28-day mortality 32.4 vs 27.3% (p = 0.05), in-hospital and 6-month mortality significantly higher (criticalcarereviews.com).
- Heidegger 2013: EN <60% on day 3, SPN days 4–8, 305 patients, infections days 9–28 27 vs 38% (HR 0.65).
- EPaNIC: 4,640; new infections 22.8 vs 26.2%; ICU discharge alive by day 8 75.2 vs 71.7%; no mortality difference; lower cost. Note: early PN started on ICU day 3 (after IV glucose days 1–2) — the card's "day 1–2" watch line is loose but the explanation does not repeat it.
- EFFORT Protein: 1,329; delivered 1.6 vs 0.9 g/kg; 60-day mortality 34.6 vs 32.1% (NS).
- NUTRIREA-3: 3,044 enrolled; 90-day mortality 41.3 vs 42.8%; readiness for ICU discharge 8 vs 9 days.
- TARGET: 90-day mortality 26.8 vs 25.7% (523/1,948 vs 505/1,966).
- NICE CG32 1.4.6/1.4.8: risk criteria, ≤10 kcal/kg/day, 5 kcal/kg/day in extreme cases (BMI <14, negligible intake >15 days), full needs by 4–7 days, thiamine 200–300 mg daily — all exactly as written.
- From standard references, not re-opened today (confident): NRS-2002 ≥3 at risk; Harris-Benedict coefficients (rounded correctly); Weir; RQ substrate values; propofol 1.1 kcal/mL (also in ESPEN text); NUTRIREA-2, CALORIES, PermiT and EDEN figures (writer's online check; numbers agree with the published abstracts as known); MRI specific but insensitive in Wernicke's; PN arithmetic in NUT-16 (re-calculated: 300 g dextrose ≈ 3 mg/kg/min in 70 kg; 1,200 mL 20% lipid = 2,400 kcal, 240 g ≈ 3.4 g/kg/day).

## Final FLAGS — special03_learn.py
- NUT-01: e ‘0.8 g/kg/day, building to over 1.2’ fits ESPEN’s progressive 1.3 g/kg/day; EFFORT Protein found no benefit from ≥2.2 g/kg/day and harm signals in AKI and high SOFA. ‘10–15% / 50% rise in expenditure’ are teaching approximations.
- NUT-05: Card agrees with ESPEN 2019/2023 and NUTRIREA-2. Card does not list ESPEN’s other reasons to delay; the fistula is in NUT-07’s watch line and was asked.
- NUT-06: Card omits high aspiration risk as a post-pyloric indication (ESPEN R13, ASPEN 2016; asked by Marrow); added. ‘Acute pancreatitis’ as a post-pyloric indication is dated. ‘Freka tube 110–120 cm’ not verified: endoscopic Freka NJ tubes are 270 cm, cut after placement.
- NUT-07: Relative list conflicts with ESPEN 2019/2023, which recommends early EN (not withholding) in spinal cord injury, abdominal trauma with confirmed continuity, TBI, prone position, open abdomen and diarrhoea, and delays EN in active upper GI bleeding until it stops.
- NUT-09: d ‘use ideal body weight’ is ASPEN-style (ASPEN uses actual weight for BMI 30–50); ESPEN uses adjusted body weight (IBW + 20–25% of excess). DocT key (2,100 kcal) follows ASPEN 2016; ASPEN 2022 and ESPEN make a lower first-week dose correct. IC limits and Harrison quick REE not on the card; added.
- NUT-11: Marrow zinc key debatable; ESPEN still allows enteral glutamine in burns >20% TBSA and trauma.
- NUT-12: e ‘500 kcal/day or 25%, four 25% steps’ is one local schedule; NICE ≤10 kcal/kg/day (5 in extreme cases) to full needs in 4–7 days; ESPEN restricts for 48 h (Doig: primary outcome neutral, 60-day mortality lower as secondary). Marrow IV-phosphate key at 1.8 mg/dL conflicts with oral-first ward tables; defensible in ventilated ICU patients.
- NUT-13: Card ladder agrees with ESPEN; Marrow key goes straight to post-pyloric for severe ARDS. GRV 500 mL/6 h is ESPEN; ASPEN discourages routine GRV.
- NUT-14: ‘Steatosis (lipid over 50%)’ unclear (mainly glucose/calorie excess). Rebound hypoglycaemia and hyperglycaemia-as-sepsis added. Marrow hyponatraemia key doubtful.
- NUT-15: 60% trigger is ASPEN 2016/Heidegger; ESPEN case by case (days 4–7); ASPEN 2022 not before day 7 except in the malnourished.
- NUT-16: Marrow PN key gives about 2,400 kcal and 240 g lipid per day if lipid runs 24 h, above ESPEN ≤1.5 g/kg/day; bank arithmetic wrong.
- No flags: NUT-02, NUT-03, NUT-04, NUT-08, NUT-10, NUT-17.

## Final FLAGS — special03_topups_learn.py
- T_3d23a130: Card sound. ‘~10%’: Harper found 16% (131 cases); 10–20% usual range. 500 mg tds × 3 days then 250 mg daily is the commonly quoted high-dose schedule (Thomson/RCP 2002; Sechi and Serra 2007), without trial basis; originals not opened. EFNS: at least 200 mg tds IV. UK protocols vary.
