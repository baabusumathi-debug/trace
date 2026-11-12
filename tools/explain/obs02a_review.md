# OBS02A — independent review, 12 Nov 2026

Files checked: `obs02a_learn.py` (15 cards), `obs02a_topups_learn.py` (2 top-ups) against `cards/OBS02A.jsonl`, `qbank.json → topups["OBS02A"]` and `qpack/OBS02A.md`.
`check_learn.py OBS02A` → OK (15/15, spine 6 steps OK). Top-ups checked by hand: every part starts with the bold restated line and matches the card line exactly, all pairs have 2 items, punch 234 and 194 characters, no banned phrases.

No outright wrong fact was found in the writer's text. The changes below are corrections of overstatement, a mis-stated stem, unverified items now confirmed or softened, and added depth.

## Changes (card: what was wrong → what it says now; source)

- OBS-17 c: "endothelium stops making nitric oxide and prostacyclin" (overstated) → "makes less nitric oxide and prostacyclin and becomes leaky". Standard pathophysiology (ACOG PB 222).
- OBS-18 trap "lowering to normal": target given as a firm "about 140–150/90–100" (not confirmed online; older ACOG text says 140–160/90–100) → "out of the severe range, to roughly 140–150/90–100, not to normal", with the reason (no placental autoregulation). ACOG CO 767 from memory; could not be opened today.
- OBS-19 c: "the limit used in NICE guidance for total maintenance fluid" (unverified, vague) → states NICE's rule exactly: in severe pre-eclampsia limit maintenance fluid to 80 mL/hour unless other ongoing losses such as haemorrhage, no volume expansion; mechanism added. NICE NG133 (confirmed online).
- OBS-20 e: "expectant care means … magnesium" read as continuous magnesium, and the part gave no reason for waiting → now gives the reason (each week before 34 lowers prematurity risk) and "magnesium while she is assessed and the steroids are given". ACOG PB 222.
- OBS-20 mimic (absent vs reversed flow): timing was from memory → confirmed and attributed: absent flow 33–34 weeks, reversed 30–32 weeks; "persistent" reversed flow is ACOG's wording. SMFM Consult Series 52 (2020); ACOG PB 222 Box 4.
- OBS-21 trap 1: said the stem had "a normal glucose and INR" (the stem gives neither) → "no hypoglycaemia, coagulopathy or encephalopathy in the stem". qpack DocT QBank question.
- OBS-23 a: added the NICE variant so a differently worded stem is recognised: 4 g over 5–15 minutes, then 1 g/hour. NICE NG133 (confirmed online).
- OBS-27 trap (plasma exchange): "category III" was from memory → confirmed and attributed: ASFA category III (role not established) for HELLP, category I for TTP. ASFA 2023 guidelines.
- OBS-28 f: Swansea "six or more of fourteen" was from memory → confirmed, text unchanged. Ch'ng 2002 criteria as reproduced in current references.
- Header comment of `obs02a_learn.py`: "from memory only" list rewritten to show what is now confirmed and what is still from memory.
- T_7bbda3e4 b: "stillbirth, preterm birth and maternal ICU admission did not differ" (ICU admission not a reported figure) → "serious maternal complications were few and did not differ significantly (3.7% vs 2.0%), and neither did perinatal death or preterm birth"; added why severe hypertension matters (stroke risk). CHIPS, NEJM 2015 (figures confirmed: primary outcome 31.4% vs 30.7%, severe hypertension 40.6% vs 27.5%).
- T_7bbda3e4 d: composite described incompletely → full composite (progression to severe hypertension or proteinuria, HELLP, eclampsia, pulmonary oedema, thromboembolism, abruption, major postpartum haemorrhage), nearly all the difference being progression; no deaths or eclampsia. HYPITAT, Lancet 2009 (confirmed: 756 women, 38 centres, 31% vs 44%, RR 0.71).
- T_7bbda3e4 e: "treat to DBP 85" was restated but not explained; HYPITAT-II was from memory → adds that DBP 85 is the ISSHP target, and the confirmed HYPITAT-II result (respiratory distress syndrome 5.7% vs 1.7%, maternal outcome 1.1% vs 3.1%, not significant). HYPITAT-II, Lancet 2015; ISSHP 2021 (from memory).
- T_7bbda3e4 mimic (CHAP): from memory, "severe pre-eclampsia and early preterm birth" → confirmed and made exact: composite of severe pre-eclampsia, indicated preterm birth before 35 weeks, abruption, fetal or neonatal death, 30% vs 37%, no more small babies; ACOG now treats chronic hypertension from 140/90. CHAP, NEJM 2022 (2,408 women; 30.2% vs 37.0%; SGA 11.2% vs 10.4%).
- Header comment of `obs02a_topups_learn.py`: updated in the same way; HYPITAT caesarean percentages (14% vs 19%) remain unconfirmed and are not in the text.
- T_f2d95d0c: no change (ADA 4–12 weeks postpartum OGTT and screening at least every 3 years as the writer checked).

Checked and left as written: all ACOG PB 222 doses and cut-offs on OBS-15, 16, 18, 23, 24; Magpie figures on OBS-25 (10,141 women, 0.8% vs 1.9%, RR 0.42, NNT 91, mortality not significant); Collaborative Eclampsia Trial (worded as "roughly halved" and "two-thirds"); Tennessee and Mississippi tables on OBS-27; PRES ("most women with eclampsia who are imaged"); all decode lines and cohort percentages against the qpack; both keys called disputed (DocT "magnesium first" with pulmonary oedema; Marrow "controlled plasma volume expansion") are correctly described.

## Final FLAGS

- OBS-15: Card agrees with ACOG PB 222 (2020). Additions only: proteinuria also met by PCR ≥0.3 or dipstick 2+; ACOG's "cerebral symptoms" is a new headache unresponsive to medication; ISSHP also accepts uteroplacental dysfunction. No disagreement.
- OBS-16: The unclear digit is 12 weeks (correct). Marrow key counts early gestational age as a marker of severe disease, which is not an ACOG severe feature. DocT says "up to 40%" of gestational hypertension progresses; ACOG says up to 50%.
- OBS-17: Watch line lists vitamins C and E for prevention: trials negative, not recommended by ACOG/WHO. Aspirin and (where intake is low) calcium are the evidence-based measures.
- OBS-18: Table matches ACOG PB 222. DocT CGT2 key says nifedipine "10–30 mg"; card and ACOG say 10–20 mg. Option C of that question is also true.
- OBS-19: "Avoid diuretics" needs its exception (pulmonary oedema). 80 mL/h is NICE NG133's figure for severe pre-eclampsia (confirmed; ACOG gives no number). Two disputed keys: DocT "magnesium" alone as initial management of BP 180/110 with pulmonary oedema; Marrow "controlled plasma volume expansion" (dated).
- OBS-20: Table is the 2011 Sibai / 2013 ACOG Task Force algorithm. ACOG PB 222 lists HELLP, persistent symptoms and persistent reversed end-diastolic flow as precluding expectant care, and says "before viability" not "under 24 weeks". The two DocT HELLP keys follow different versions. Card puts reversed flow in the 48-hour row; SMFM 2020 gives 30–32 weeks for reversed and 33–34 weeks for absent flow.
- OBS-21 (new): Table agrees with the Sibai/ACOG Task Force criteria. Watch-line mortality figures (perinatal 5–11.8%, maternal up to 1.8%) could not be traced to a source and are not restated.
- OBS-22: Timing percentages restated as on the card, not re-verified (series differ). Card b "20%": ACOG gives 20–38%.
- OBS-23: Card "over 15–20 minutes" is the Sibai wording; ACOG says 20–30 minutes; NICE uses 4 g over 5–15 minutes then 1 g/hour. "Another 2 g bolus": ACOG 2–4 g over 5 minutes. ACOG's therapeutic range is 4.8–9.6 mg/dL.
- OBS-25: Card "relative risk about 0.41": published figure is 0.42. Marrow tests the myasthenia contraindication, which the card only implies.
- OBS-27: Card "LDH at least twice normal": Tennessee and ACOG say LDH ≥600 IU/L. Watch-line incidence differs from reviews (10–20% of severe pre-eclampsia; 0.5–0.9% of pregnancies). DocT stem calls platelets of 70,000 "class I"; Mississippi class 1 is ≤50,000, so that is class 2. Plasma exchange "category III" is right (ASFA 2023; TTP is category I); the plasma exchange key is right only because persistent worsening suggests TTP.
- OBS-29: Table holds. Platelets in fatty liver are often mildly low before overt DIC (the DocT stem gives 100,000); glucose, INR and ammonia decide.
- T_7bbda3e4: Card accurate (CHIPS 27.5% vs 40.6%; HYPITAT 31% vs 44%). CHIPS is NEJM 2015; the DocT explanation cites the Lancet. "Deliver at 37 weeks" also rests on HYPITAT-II and ACOG PB 222. "Treat to DBP 85" is the ISSHP target; ACOG, after CHAP, states its threshold as 140/90.
- T_f2d95d0c: Card says OGTT at 6–12 weeks; current ADA and ACOG wording is 4–12 weeks (NICE: fasting glucose at 6–13 weeks). Either is acceptable in an exam.

## Not confirmed online today (kept soft in the text)

- ACOG post-treatment range 140–150/90–100 (CO 767 could not be opened; an older ACOG summary gives 140–160/90–100).
- ISSHP 2021 diastolic target of 85 and the ACOG 2022 change to a 140/90 threshold after CHAP (from memory).
- Collaborative Eclampsia Trial percentages, OBS-22 timing percentages, OBS-21 mortality figures, HYPITAT caesarean rates (last two are not in the explanation text).
- The HYPITAT-II and CHAP PubMed/PMC pages were blocked; figures were confirmed from the Utrecht University repository record and a published trial summary.
