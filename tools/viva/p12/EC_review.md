# P12 EC (ECG foundation) — review log, 24 Nov 2026

Two packets, as the prompt allowed, because the depth rule made one packet too long to keep full explanations: **EC1** (wiring, waves, cameras, ischaemia and its mimics) and **EC2** (blocks, bundle branches, short circuits, antiarrhythmics, electrolytes, QT, poisons, temperature and hormones). Both sit after Shock II (S2) and before ACS I (A1).

## Files
- `P12_EC1_pack.json`, `P12_EC2_pack.json`: P12 draft schema (questions → open/steps/spine/close, drill, traps, mimics, new_cards, card_flags), the same shape `assemble.py` reads from `<CODE>_draft.json`.

## Size
- **EC1**: 5 sections, 27 steps, about 126 spoken minutes (105,598 characters), 25 drill items, 31 traps, 24 mimics, 16 new cards (V12-045 to V12-060), 2 card corrections.
  - P12-1101 The wiring: a relay built from two kinds of cell (3 steps)
  - P12-1102 Two action potentials become the waves (4 steps)
  - P12-1103 Leads as cameras: one rule explains axis, R waves and hypertrophy (6 steps)
  - P12-1104 Ischaemia through the cameras: injury current, territories and the hidden infarcts (7 steps)
  - P12-1105 ST and T changes that are not a blocked artery: pericardium, lungs, brain and the scar (7 steps)
- **EC2**: 7 sections, 43 steps, about 159 spoken minutes (133,864 characters), 33 drill items, 65 traps, 34 mimics, 16 new cards (V12-061 to V12-076), 4 card corrections.
  - P12-1201 Blocks as one story: the level of the block decides everything (8 steps)
  - P12-1202 One level lower: bundle branches, fascicles and the paced heart (4 steps)
  - P12-1203 Short circuits: how fast rhythms form, and the shape each one draws (7 steps)
  - P12-1204 Antiarrhythmics hung on the same action potential (5 steps)
  - P12-1205 What changes the waves I: potassium, calcium and magnesium (8 steps)
  - P12-1206 The QT: what it measures, what stretches it, and torsades (5 steps)
  - P12-1207 Poisons that write on the ECG: sodium channels, digoxin and the node blockers (6 steps)

## Assembly notes for the Trace chat
- Section codes: EC1 uses P12-1101 to P12-1105, EC2 uses P12-1201 to P12-1207 (unused numbers; the order in the package must still be S2 → EC1 → EC2 → A1). New cards V12-045 to V12-076 (no clash with V12-001 to V12-044). Steps reference two existing V12 cards from later packets: V12-016 (RY) and V12-020 (DR); their card text lives in those drafts.
- `assemble.py` label map needs: `'EC1':'ECG I: the wiring, the waves and the cameras'`, `'EC2':'ECG II: blocks, short circuits, drugs and what changes the waves'`, and the input path for these two files.
- Packet openings (P12-1101, P12-1201) and closes (P12-1105, P12-1207) are written. EC2's close hands over to ACS I.
- **Two small edits in existing packets** so the series still flows:
  - S2 close, last paragraph: replace "So the next packet steps back to the start. Before the shock, there's the infarct. How do you recognise it?" with "So the next packets step back to the start. Before the shock, there's the infarct, and before the infarct, the ECG that shows it. That's where we go next." (EC1 opens on this line.)
  - A1 open: replace "Shock Two ended with a question: before the shock, there's the infarct, so how do you recognise it? Here's the order you'll learn it in." with "You can now read the wiring, the waves and the cameras. So, the question Shock Two left open: before the shock there's the infarct. How do you recognise it? Here's the order you'll learn it in."
- Optional callbacks (not required): A1's MI-27 lesson says the card puts takotsubo only under ST depression; the corrected card lists it under ST elevation too. RH's CVS-07 lesson says "In ACS I, ST elevation meant…": EC1 now teaches that first.
- Drill: EC2 carries 33 items (above the usual 25) so that every named exam miss sits in the closing check, as the prompt asked.
- Lesson length: most foundation lessons run 3,300 to 4,000 spoken characters (all under the 4,000 cap); total listening is long by design (full depth, no dilution).

## Exam misses and where each is taught (all also in traps; all in a closing check)
| Miss | Packet / step |
|---|---|
| GT1 Q16 WPW orthodromic AVRT | EC2 P12-1203 HY2/CAR-03 |
| GT1 Q24 AV block statements | EC2 P12-1201 V12-061, ACLS-36 |
| GT1 Q84 vagal manoeuvre statements | EC1 P12-1101 V12-047; EC2 P12-1203 V12-016 |
| GT1 Q3 Schwartz score | EC2 P12-1206 V12-072 |
| GT1 Q147 safe agent in long QT (propofol) | EC2 P12-1204 V12-068, P12-1206 V12-073 |
| GT1 Q51 Wellens | EC1 P12-1104 V12-059 |
| GT1 Q139 TCA QRS threshold in a child | EC2 P12-1207 V12-074 |
| GT1 Q36 NAGMA with high potassium (type 4 RTA) | EC2 P12-1205 V12-070 |
| GT1 Q119, Q26 (hypocalcaemia on digoxin; suxamethonium) | EC2 P12-1205 |
| GT7 Q99, GT8 Q54 digoxin Fab (K above 5; Fab during arrest) | EC2 P12-1207 HY2/CAR-07 |
| GT7 Q100 bidirectional VT | EC2 P12-1207 CAR-07 |
| GT7 Q102 cocaine wide QRS, GT8 Q52 propranolol QRS 160 | EC2 P12-1207 V12-074 |
| GT7 Q94, Q96, GT8 Q90, GT8 Q82 (CCB, HIE, diltiazem, levosimendan on beta-blocker) | EC2 P12-1207 V12-020 |
| GT7 Q130 Brugada ICD | EC2 P12-1206 HY2/CAR-06 |
| GT7 Q110 arsenic QT; GT8 Q55 OP QTc; GT8 Q73 lithium; GT8 Q98 theophylline | EC2 P12-1206 V12-073, P12-1207 V12-075 |
| GT8 Q16 AF in aortic stenosis (atrial kick) | EC2 P12-1203 V12-066 |
| INI Sep-4 Q76 Daniel score | EC1 P12-1105 RVF-26 |
| INI Sep-4 Q67 low K with low Mg | EC2 P12-1205 MGP-03 |
| INI Sep-4 Q44 CVP in AF (no a wave) | EC2 P12-1203 V12-066, P12-1201 V12-062 |
| INI Sep-4 Q33 dialysate K 1 mEq/L | EC2 P12-1205 V12-070 |
| INI GT2 Q75 rhythm 2 × 2 grid | EC2 P12-1203 V12-065 |
| INI GT2 Q8 SR verapamil (whole bowel irrigation); GT2 Q80 hypercalcaemia | EC2 P12-1207, P12-1205 |
| INI GT4 Q1 RV infarct (V4R) | EC1 P12-1104 MI-22 |
| INI GT4 Q10 adrenaline via cAMP | EC1 P12-1101 V12-047 |

INI-SS papers read: Sep-4 PYT, GT2, GT3, GT4 (the "GT 1" folder holds only a question paper, no analysis; no later INI GT folder exists). GT3 had no ECG miss.

## Card corrections found (his existing cards)
- **CVS10B|MI-25** — wrong: (ESC 2023; older keys: 8 leads, UDMI 2018 / ESC 2017) — correct: (ESC 2023 and UDMI 2018: 6 leads; older key: 8 leads, ESC 2017 STEMI) — source: Fourth Universal Definition of MI 2018: ST depression ≥1 mm in 6 leads, with ST elevation in aVR and/or V1
- **HY2|CAR-24** — wrong: Daniel table and watch line '= 8 (key C)' without the T-depth rows — correct: Add: T inversion depth points in V1–V3 (V2 and V3 at least 1 point each when inverted ≥1 mm), Q in III = 1, T inversion in III = 1; 8 stays the keyed answer for HR >100 + incomplete RBBB + TWI V1–V4 — source: Daniel KR et al. Chest 2001;120:474–81
- **ELEC03B|MGP-07** — wrong: SERUM MAGNESIUM (MMOL/L) ... Over 4 Hyporeflexia (knee jerk lost near 10) ... Over 5 ... Over 10 ... Over 13 — correct: The ladder 4, 5, 10, 13 is in mEq/L (the original card and Marino's table): hyporeflexia >4 mEq/L, first-degree AV block >5, complete heart block >10, cardiac arrest >13 mEq/L. In mmol/L these are 2, 2.5, 5 and 6.5. Restore the heading to mEq/L; 'knee jerk lost near 10' refers to about 10 mg/dL (about 4 mmol/L) in obstetric texts and should carry its unit. (in mmol/L the ladder is about 2, 2.5, 5, 6.5; 'knee jerk lost near 10' is 10 mg/dL) — source: Original deck card ELEC03B MGP-07 in /home/claude/decks (heading MEQ/L); Wikipedia Hypermagnesemia consequences list (4.0, >5.0, >10.0, >13.0 mEq/L), matching Marino, The ICU Book.
- **TOX01|TOX-07** — wrong: QTc <440 ms — correct: Not wrong but an older single cut-off. Current sex-specific upper limits are about 450 ms in men and 460 ms in women (ESC 2022 diagnoses LQTS at QTc ≥480 ms); the lesson teaches both figures. Consider adding '(≤450 men, ≤460 women)'. — source: ESC 2022 ventricular arrhythmia and SCD guideline; Schwartz score bands (Merck Manual table).
- **HY2|CAR-07** — wrong: K above 5–5.5 in acute toxicity (Fab indication) — correct: Minor: sources agree on potassium >5.0 mmol/L as the Fab threshold in acute poisoning (GT7 Q99 keyed 'potassium above 5 mEq/L'); 5.5 is the Bismuth 1973 mortality figure. Also add 'cardiac arrest' to the indications (AHA 2023; GT8 Q54). — source: Pincus M. Management of digoxin toxicity. Aust Prescr 2016 (indications agreed by all sources: life-threatening arrhythmia, cardiac arrest, K⁺ >5.0 mmol/L).
- **HY2|CAR-02** — wrong: then 12 mg (may repeat 12 mg once) — correct: then a single 12 mg dose (AHA 2010–2025); ESC 2019 allows up to 18 mg — source: AHA 2025 adult tachycardia algorithm
- **NEURO03|NEURO-80** (soft, outside ECG scope, not changed here): the non-ECG rows (fludrocortisone class 2a, glucose 80–120 mg/dL) read as 2012 AHA/ASA wording; check against the 2023 AHA/ASA aSAH guideline when the neurology packet is built.

## Fact-check: edits made (independent checker, then applied)
- EC1 · P12-1101 / V12-045 / lesson: Guyton, the text NEET keys most, gives 0.3-0.5 m/s for working muscle; 0.5-1 excludes it. Name both textbook figures. — source: Guyton & Hall 14e ch.10 (atrial/ventricular muscle 0.3-0.5 m/s, Purkinje 1.5-4.0, AV node 0.02-0.05); Ganong 26e table 29-1 (ventricular muscle 1 m/s, Purkinje 4, AV node 0.05)
- EC1 · P12-1101 / V12-045 / lesson: Same correction in the on-screen box. — source: Guyton & Hall 14e ch.10 (atrial/ventricular muscle 0.3-0.5 m/s, Purkinje 1.5-4.0, AV node 0.02-0.05); Ganong 26e table 29-1 (ventricular muscle 1 m/s, Purkinje 4, AV node 0.05)
- EC1 · new_card V12-045 a[3]: Same correction on the card. — source: Guyton & Hall 14e ch.10 (atrial/ventricular muscle 0.3-0.5 m/s, Purkinje 1.5-4.0, AV node 0.02-0.05); Ganong 26e table 29-1 (ventricular muscle 1 m/s, Purkinje 4, AV node 0.05)
- EC1 · P12-1101 / V12-047 / bridge: Digit in text that may be voiced; every other bridge and lesson writes numbers in words. — source: Brief (voice rule)
- EC1 · P12-1104 / V12-058 / lesson: Lesson taught only the classic 0.04 s for non-V2-V3 leads; current UDMI figure is 0.03 s and 1 mm deep (the new card already has it). An MCQ quoting UDMI keys 0.03. — source: Thygesen et al., Fourth Universal Definition of MI (2018), Table 3 (Q-wave criteria) and section on right precordial leads; Eur Heart J 2019;40:237
- EC1 · P12-1104 / V12-058 / lesson: Box brought in line with the card and UDMI. — source: Thygesen et al., Fourth Universal Definition of MI (2018), Table 3 (Q-wave criteria) and section on right precordial leads; Eur Heart J 2019;40:237
- EC1 · P12-1104 / CVS10B|MI-22 / lesson: UDMI qualifier (>=1 mm in men <30 y) is on the card but missing from the lesson. — source: Thygesen et al., Fourth Universal Definition of MI (2018), Table 3 (Q-wave criteria) and section on right precordial leads; Eur Heart J 2019;40:237
- EC1 · P12-1103 / V12-056 / lesson: Names the 2017 term NEET may still key and the 2026 rename (AERP); adds the under-16 juvenile exception that the criteria state explicitly. — source: International Criteria 2017 (Drezner/Sharma, Br J Sports Med 2017;51:704; JACC 2017;69:1057); ACC Expert Analysis '2026 International Criteria for ECG Interpretation in Athletes', 29 Oct 2026, https://www.acc.org/Latest-in-Cardiology/Articles/2026/10/29/11/45/2026-International-Criteria-For-ECG-Interpretation-in-Athletes
- EC1 · new_card V12-056 a[5]: Same update on the card. — source: International Criteria 2017 (Drezner/Sharma, Br J Sports Med 2017;51:704; JACC 2017;69:1057); ACC Expert Analysis '2026 International Criteria for ECG Interpretation in Athletes', 29 Oct 2026, https://www.acc.org/Latest-in-Cardiology/Articles/2026/10/29/11/45/2026-International-Criteria-For-ECG-Interpretation-in-Athletes
- EC1 · P12-1105 / CVS06B|RVF-26 / lesson: Strict Daniel scoring of this stem is at least 10 (V2 and V3 inversion score >=1 each), which crosses the >=10 cut-off; the learner must know 8 is the key for the simplified stem and why a stem with depths scores higher. — source: Daniel KR et al., Chest 2001;120:474-81 (T inversion V1: <1 mm 0, 1-2 mm 1, >2 mm 2; V2 and V3: <1 mm 1, 1-2 mm 2, >2 mm 3; Q in III 1; T in III 1; max 21; >=10 gives sPAP >50 mmHg, specificity 97.7%, sensitivity 23.5%)
- EC1 · drill 24: Same qualifier. — source: Daniel KR et al., Chest 2001;120:474-81 (T inversion V1: <1 mm 0, 1-2 mm 1, >2 mm 2; V2 and V3: <1 mm 1, 1-2 mm 2, >2 mm 3; Q in III 1; T in III 1; max 21; >=10 gives sPAP >50 mmHg, specificity 97.7%, sensitivity 23.5%)
- EC1 · trap 27: Same qualifier. — source: Daniel KR et al., Chest 2001;120:474-81 (T inversion V1: <1 mm 0, 1-2 mm 1, >2 mm 2; V2 and V3: <1 mm 1, 1-2 mm 2, >2 mm 3; Q in III 1; T in III 1; max 21; >=10 gives sPAP >50 mmHg, specificity 97.7%, sensitivity 23.5%)
- EC2 · P12-1206 / V12-072 / lesson: GT1 Q3 as described (syncope while swimming, QTc 485, family history of sudden death) sums to 5.5 by the published score; 6.5 needs a second relative with definite LQTS. Learner must be able to pick either. — source: Schwartz PJ, Crotti L. Circulation 2011;124:2181 (QTc>=480 = 3; syncope with stress = 2; family member with definite LQTS = 1; unexplained SCD <30 in immediate family = 0.5; same relative not counted twice)
- EC2 · trap 45: Same point: the key is only reachable with both family items. — source: Schwartz PJ, Crotti L. Circulation 2011;124:2181
- EC2 · new_card V12-072 a[6]: Same point on the card. — source: Schwartz PJ, Crotti L. Circulation 2011;124:2181
- EC2 · drill 18: Keeps the drill consistent with the lesson. — source: Schwartz PJ, Crotti L. Circulation 2011;124:2181
- EC2 · P12-1201 / HY2|CAR-08 / lesson: Lesson teaches only the AHA 2020/2025 first dose (1 mg). ERC 2021/2025 and AHA 2015 and earlier use 0.5 mg (500 micrograms); NEET may key either. — source: ERC Guidelines 2025 ALS bradycardia algorithm (atropine 500 mcg IV, repeat to 3 mg); AHA 2020/2025 adult bradycardia algorithm (1 mg, max 3 mg)
- EC2 · P12-1205 / V12-070 / lesson: Current consensus (2024) uses 3.5 mmol/L; ADA 2009 and Harrison-based keys use 3.3 mEq/L. Brief requires the older keyed figure to be named. — source: Umpierrez GE et al. Hyperglycemic crises in adults with diabetes: a consensus report. Diabetes Care 2024;47:1257; Kitabchi AE et al. Diabetes Care 2009;32:1335
- EC2 · new_card V12-070 a[0]: Same point on the card. — source: Diabetes Care 2024;47:1257; Diabetes Care 2009;32:1335
- EC2 · P12-1207 / V12-020 / lesson: As written the lesson's own table (dihydropyridines 'least' cardiac depression) contradicts the key 'minimal cardiac depression'; the discriminator in the stem is 'intermediate vasodilation'. — source: GT8 Q90 stem and key; Goodman & Gilman CCB comparison table (contractility suppression: verapamil 4, diltiazem 2, nifedipine 1); Rang & Dale (diltiazem intermediate in selectivity)
- EC2 · trap 59: Makes explicit why the dihydropyridine options are wrong. — source: GT8 Q90; Goodman & Gilman
- EC2 · P12-1204 / CVS08B|ACLS-32 / lesson: AHA 2025 Part 9 recommendation still reads 'IV amiodarone, procainamide, or sotalol' (COR 2b) for stable wide-complex tachycardia; only the algorithm sidebar drops sotalol. 'No longer lists' alone invites a wrong true/false. — source: AHA 2025 Part 9 Adult ALS, wide-complex tachycardia recommendations (cpr.heart.org) and 2025 Adult Tachycardia With a Pulse algorithm
- EC2 · trap 5: Decision on the disputed key: anterior MI second-degree block is infranodal; added the qualifier for a stem that draws a Wenckebach pattern. — source: ESC 2023 ACS and ESC 2021 pacing guidelines (AV block in anterior MI is infra-Hisian, high mortality); Braunwald; DocT explanation in EC2_pack.json
- EC2 · trap 21: Source precision, verified against the 2025 text. — source: AHA 2025 Part 9 Adult ALS, pre-excited AF/flutter recommendation 3 (COR 3: Harm, LOE C-LD); Brugada J et al. ESC 2019 SVT guideline

## Decided against changing, and points resting on a weaker source
- Purkinje 2-4 m/s (Guyton 1.5-4.0): inside range, not MCQ-changing.
- "Sokolow-Lyon >= 35" vs "> 35" in some texts: both keyed; left.
- Right axis defined as beyond +90 (some texts +100/+110 for adults): matches the -30 to +90 normal range NEET uses.
- Wellens angiography "within about a day" (ESC high-risk NSTE-ACS under 24 h) vs "immediate" in StatPearls: guideline-consistent; GT key was admit for urgent angiography.
- de Winter "two in every hundred LAD occlusions" (source: anterior MIs): equivalent.
- S1Q3T3 "one or two in ten" (series range 10-25%): left.
- Pericarditis classic ECG "up to 60%": ESC 2015 figure, kept; ESC 2025 text not retrieved.
- Wellens "deepest V2-V3" vs Kosuge's ACS peak at V3-V4: Wellens is defined on V2-V3; the III + V1 rule is the tested discriminator and is stated.
- Low-voltage list places constriction under "less muscle current": mechanism arguable, list membership correct.
- V7-V9 "1 mm in men under 40" is in the box and drill but not spoken: adequate.
- MI-27 lesson remark on older notes listing stress cardiomyopathy only under ST depression: the card still lists it in both columns; consistent with the lesson.
- "Oldest rule" for Sokolow-Lyon (Lewis index is older): style.
- Lead names, S1 Q3 T3, M2 in spoken text: unavoidable alphanumerics, readable.
- Dialysate potassium 1 mmol/L: kept as "keyed" (options were 0, 1, 4, 5); many units now prefer 2 for safety, lesson already says routine baths are 2-3.
- "Never phenytoin" in TCA poisoning: kept (standard toxicology and the GT key), although AHA 2025 text mentions phenytoin case reports as a class Ib drug.
- Theophylline ventricular irritability keyed amiodarone (GT8 Q98): kept with esmolol named for SVT, as written.
- Orthodromic AVRT in WPW "vagal, adenosine, nodal blocker": kept as the GT key; guidelines add caution (adenosine can precipitate AF) but the sequence stands.
- Magnesium for torsades is only COR 2b in AHA 2025 and IV calcium in hyperkalaemic arrest is 2b "not well established": no change, lessons concern treatment before arrest and exam keys are unchanged.
- LAFB axis -45 (older texts -30): left as current criterion.
- "Every source agrees" on three Fab indications: slight overstatement, left.
- Voice: only lead names (V1 to V6) and gene names (KCNQ1, KCNH2, SCN5A) contain digits in spoken text; treated as the packet convention, not flagged as edits.
- de Winter as an ESC 2023 STEMI-equivalent pattern rests on a secondary source (guideline supplementary figure); taught as current practice either way.
- GT1 Q3 (Schwartz): the stem as summarised sums to 5.5; the GT key is 6.5. Taught 6.5 with the item breakdown that gives it, and told him to pick 5.5 if the stem has one relative only.
- Exact GT1 stems for Q16, Q24, Q84 and Q147 were not available (only one-line summaries); lessons teach the standard true and false statements around each keyed answer.
- Dialysate potassium 1 mEq/L taught as the INI key (low, not zero); the exact figure varies by unit.
- Hypothermia rhythm thresholds taught as rough guides matching the Arrest packet's V12-035 and ERC 2025 staging.

## Figures (added 24 Nov, after the figure audit)
- 46 figures: 22 in EC1 and 24 in EC2. The calcium figure is shown at two steps, so 47 steps carry a picture. Each is attached as `lesson.pic` with `lesson.cap`, the way Trace already shows lesson figures. Lesson text is unchanged, so the fact-checked wording still stands.
- Files: SVGs in Drive › Trace › P12_EC_img, named `P12_EC_<topic>.svg`. The Trace chat copies them to `data/viva/img/P12/`, or wherever the package's figures live.
- All figures are synthetic, drawn to standard morphology on 25 mm/s paper, and colour-blind safe: a black trace, emphasis in blue or orange, always with a label, arrow or line style.
- Known simplifications: the relay heart is schematic. In the 12-lead grids (territories, aVR) the complexes are drawn at 0.7–0.8 of normal size so all 12 fit; the ST shifts stay true to scale. The pre-excited AF beats are stylised. A few beats keep a tiny notch at the J point.
- Steps without a figure, and why, are in the audit message in the chat: they are lists or decisions, where a picture would only repeat the words.
