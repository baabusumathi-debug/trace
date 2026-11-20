# GI06 review (second, independent check), 20 Nov 2026

Files checked: gi06_learn.py (22 cards) and gi06_topups_learn.py (T_cc325a06, T_6144df58, T_b7c7f544), against cards/GI06.jsonl, qpack/GI06.md and gi_cardlayer.json. Letters and bold restatements match the cards in every part. `check_learn.py GI06` passes; the top-ups file loads with parts a–d in the order of each `a` list.

Sources reopened online:
- Kyoto consensus full text (APASL/AARC, Hepatol Int 2025;19:1–69, doi 10.1007/s12072-024-10773-4, Springer).
- AASLD press release, 30 Oct 2026: "Acute-on-Chronic Liver Failure: A Global Multi-Society Consensus on Definitions", Hepatology, doi 10.1097/HEP.0000000000001891. Also the HCPLive report of the same date.
- AARC derivation abstract (Choudhury, Hepatol Int 2017, via BVS) and an AARC calculator for the point cut-offs.
- CANONIC abstract (Moreau, Gastroenterology 2013, Bern repository).
- EF-CLIF report on the APACHE trial (25 Aug 2026).
- Muciño-Bermejo (Ann Hepatol 2012) on AKI causes.
- "Bridging the critically ill patient with ACLF" review (Univ. Barcelona repository): ventilation limits and transplant contraindications.

Blocked or unopened: PubMed (Kyoto abstract, Garcia-Tsao 2008), the Springer AARC 2017 full text, and PMC tables (captcha).

## Changes (gi06_learn.py)
- **Kyoto 2025 and global 2026 claims (factual, verified):** both exist.
  - Kyoto is a real APASL consensus (Hepatol Int 2025). It proposes ACLF as bilirubin >5 and INR ≥1.5, then ascites/HE within 28 days, "with or without kidney dysfunction (serum creatinine >1.5 mg/dl)". The card's watch line is correct.
  - The global multi-society definition (AASLD, EASL, APASL, ALEH, SOLDA) was released on 30 Oct 2026 in Hepatology (AASLD release). The card and the writer's figures for it match the HCPLive summary.
  - Nothing was removed.
- **ACLF-03 a (precision):** now says the Kyoto creatinine >1.5 is part of a *proposed* redefinition. The consensus's own statements prefer AKI staging with urine output over an absolute creatinine (Kyoto full text, 3.3.2–3.3.4).
- **ACLF-02 extra (factual, unverifiable):** removed "it sits beside, not in place of, the regional systems". Added the F3-or-more substrate and the exclusion of vasopressors given only for HRS-AKI (HCPLive / AASLD).
- **ACLF-08 a (factual):** the writer said CANONIC's no-ACLF group died at 4.7%/14% and flagged the card's 1.9% as unmatched. The CANONIC abstract gives no-ACLF 28-day mortality as **1.9%**, so the card is right. The text is corrected and the ACLF-08 FLAG is removed.
- **ACLF-09 c (factual):** the claim that NACSELD's specificity "is why it is used to judge futility" was not supported. It now says some reviews present it that way, but EASL 2023 bases futility on CLIF-C ACLF >70 or ≥4 organ failures at days 3–7. The punch is reworded. FLAG added.
- **ACLF-14 a (factual):** "AKI in up to 60% of hospitalised cirrhotics" → "roughly a fifth to a half", with the mechanism added. Muciño-Bermejo gives 20% on admission and up to 49%; one higher figure of 70% conflicts within that same paper.
- **ACLF-14 b (factual/depth):** the cause shares are now marked as rounded and variable between series. Muciño-Bermejo/Wong: prerenal 32%, ATN 35%, HRS 20% + 6%. Garcia-Tsao: about two-thirds prerenal (a third of those HRS), about a third intrinsic, post-renal <1%. FLAG added.
- **ACLF-17 b (factual, untraced):** the 89% one-year ventilated mortality could not be traced to any source. The text now says so and explains why mortality is high. FLAG added.
- **ACLF-17 c (factual):** the PEEP ≤10 / FiO2 ≤40% limits are now described as centre-specific. The Bridging review gives FiO2 <50% with P/F >150–200 as the usual requirement; P/F <150 marks futility. Added why: the graft does not fix the lung, and high PEEP impairs venous return. FLAG added.
- **ACLF-19 d and trap (factual, added):** the APACHE RCT is now included. It was presented at EASL Congress 2026 and is not yet published: 274 high-risk ACLF patients, mostly grade 1b–2; plasma exchange with 5% albumin vs standard care; 90-day death without transplant 37.8% vs 49.6% (EF-CLIF). The exam answer stays "not routine outside trials" (EASL 2023). The card's survival figures remain untraced and the FLAG is kept. The rodenticide figure did not match the one paediatric low-volume plasma exchange series found (J Clin Exp Hepatol 2023: 6/8 Kochi-eligible children survived).
- **ACLF-13 d (factual):** added that eltrombopag, the drug the card names, is not used before procedures, because it caused portal vein thrombosis in ELEVATE; avatrombopag and lusutrombopag are used. The FLAG is extended.
- **ACLF-16 d (minor):** the severe portopulmonary hypertension bar is now "mPAP ≥50, or ≥35 with PVR ≥5 WU despite treatment" (ILTS practice). It previously said "above 35 despite treatment".
- **ACLF-06 e (minor):** "terlipressin counts only if given for shock" was unverified. It is replaced by the mechanism and by the 2026 global-definition rule (vasopressors for HRS-AKI alone are not counted).
- **ACLF-11 e (minor):** "PPIs accumulate" → "PPI use is linked to HE", plus "use only for a clear indication".
- **Header:** added a second-review block listing sources, and updated the list of figures that remain untraced.

## Changes (gi06_topups_learn.py)
- **T_cc325a06 c (minor):** "jaundice largely unconjugated" → mixed jaundice, with a haemolytic unconjugated component on top of alcohol-related liver disease. Added a cautious mechanism. Header note added.
- Verified, no change: Maddrey DF = 4.6 × (PT − control) + bilirubin (mg/dL), with ≥32 = severe; MELD >20; prednisolone 40 mg/day for 28 days after infection or bleeding is excluded; Lille >0.45 at day 7 = non-response, stop steroids. The benzodiazepine choice (lorazepam/oxazepam, glucuronidation only), thiamine before glucose, and the AD/NAD split by hospital admission are all correct.

## Verified, no change needed
- **AARC (ACLF-05):** cut-offs are correct. Bilirubin <15/15–25/>25; HE 0/I–II/III–IV; INR <1.8/1.8–2.5/>2.5; lactate <1.5/1.5–2.5/>2.5; creatinine <0.7/0.7–1.5/>1.5. Grades are 5–7/8–10/11–15, with 28-day mortality 12.7/44.5/85.9%. "≥11 at baseline or persisting in week 1 among non-survivors" matches the abstract.
- **NACSELD (ACLF-04):** 30-day survival 51.3/36/23% with 2/3/4 failures gives the card's mortality of 49/64/77%.
- **COSSH (ACLF-04, ACLF-09):** 1,322 patients; the formula and the grade mortalities (23/61/93%) are consistent.
- **Other card content:** the CLIF-OF table, EASL-CLIF grade rules, TAM items, PORTICO, Cavallin, CONFIRM/FDA SpO2 <90%, ESC/ERS 2022 PH definition, HPS grading and orthodeoxia, and the AGA 2021 statements are all correct as written.
- **Traps:** kept, and their truth sides were checked. The DocT keys disputed in the card layer are named the same way in the traps: platelets before endoscopy (ACLF-13), PCC lacking factor VII (ACLF-13) and CVP 22 from portal hypertension (ACLF-17).

## Final FLAGS
- ACLF-02: NACSELD's 507-patient cohort was prospective; "post-hoc" fits only the later analysis that derived the organ-failure definition.
- ACLF-04: CLIF-C row (20/30/80%) is rounded from CANONIC (22.1/32.0/76.7%) and differs slightly from ACLF-08. Minor.
- ACLF-09: "NACSELD best for judging futility" is not a guideline position; EASL 2023 uses CLIF-C ACLF >70 or ≥4 organ failures at days 3–7.
- ACLF-12 b: 20–30 kcal/kg is below EASL 2023 (30–35 kcal/kg/day or 1–1.4 × REE; protein up to 2 g/kg in the critically ill).
- ACLF-13 d: platelets or TPO-RA at 20,000–50,000 before an invasive procedure is out of date for low-risk procedures (AGA 2021, EASL 2022, AASLD 2024). The TPO-RA named, eltrombopag, is not used for this (portal vein thrombosis in ELEVATE); avatrombopag and lusutrombopag are. b: AGA makes no recommendation on viscoelastic testing to predict procedural bleeding. The DocT keys (platelets before endoscopy; PCC lacks VII) are outdated.
- ACLF-14: cause shares (50/30/20/1) are rounded and vary by series; the order is right.
- ACLF-15 d: 14 days is the maximum course (ICA–ADQI 2024). Non-response is judged earlier: no improvement after 48 h at the maximum tolerated dose.
- ACLF-16: orthodeoxia is usually a fall of >5% or >4 mmHg PaO2; "3–4 cycles" is where the window starts (3–6 counts); mPAP >25 is the old cut-off (now >20 with PVR >2 WU).
- ACLF-17: b, the 89% one-year ventilated mortality, is untraced. c: transplant ventilation limits are centre-specific; a review gives FiO2 <50% and P/F >150–200.
- ACLF-19: the Wilson and rodenticide rows are ALF, not ACLF, and the survival figures are untraced. APACHE (EASL Congress 2026, unpublished: 37.8% vs 49.6% 90-day death without transplant, grades 1b–2) may change the "not outside trials" position.
- Removed: ACLF-08. The card's no-ACLF 1.9% is CANONIC's own figure.
