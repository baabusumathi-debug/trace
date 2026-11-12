# SPECIAL05B — independent review of special05b_learn.py and special05b_topups_learn.py (13 Nov 2026)

Checker: `python3 check_learn.py SPECIAL05B` → `SPECIAL05B 14 cards 14 entries OK`, `v3 spine 6 steps OK`.
Top-ups (no checker) checked by hand: every part starts with the bold restated answer, all mimic/trap/decode pairs have 2 items, punch 238, 245 and 185 characters (limit 320), no banned phrases.

## Changes (card: what was wrong → what it says now; source)

### Factual
- POLY-11 b (part, decode, header comment, new FLAG): Cosgriff figures (pH <7.1 OR 12.3, temp <34 °C OR 8.7, ISS >25 OR 7.7, SBP <70 OR 5.8, all four 98%) were taught as predictors of death / 98% mortality → they predict life-threatening coagulopathy (PT and PTT >2× normal) in 58 massively transfused patients; 98% incidence of that coagulopathy with all four. Decode now asks the predictor of life-threatening coagulopathy. Source: Cosgriff et al., J Trauma 1997 abstract (Scilit record).
- POLY-15 e (part, header comment, FLAG): "A later trial targeting MAP 50 vs 65 during surgery reduced early post-operative deaths" → that was the Morrison 2011 interim (1/44 vs 8/46); the final Carrick 2016 report (n 168) found no difference in 24-h (p 0.27) or 30-day (p 0.48) mortality. Source: Carrick, J Trauma Acute Care Surg 2016;80:886 (UTMB abstract); Morrison 2011 appraisal (WUSTL journal club).
- POLY-20 d (part, FLAG): PATCH-Trauma "reduced deaths at 24 hours and 28 days" stated as a finding → lower as secondary outcomes (RR 0.69 and 0.79, CIs just excluding 1), 6-month mortality not significant. Source: PATCH-Trauma, NEJM 2023 (WikiJournalClub summary).
- POLY-23 d (part, FLAG): "the warning about large saline volumes is from the previous edition" → the 6th edition recommends 0.9% saline or balanced crystalloid (1B), and its rationale limits saline to about 1–1.5 L, so the card's "avoid excess 0.9% saline" is consistent with the rationale. Source: Rossaint et al., Crit Care 2023 (6th edition full text, Rec. 15).
- POLY-21 d (part, FLAG): watch line "concentrate lowered 6-h mortality" flagged as untraceable → traced to Wafaisade 2013 (TraumaRegister DGU matched pairs, 6-h mortality 10.5% vs 16.7%, discharge mortality no different); explanation now says it is registry data, not a trial; CRYOSTAT-2 figures (25.3% vs 26.1%) added. Source: Wafaisade, J Trauma Acute Care Surg 2013;74:387; AABB summary of CRYOSTAT-2 (JAMA 2023).
- POLY-13 a (part, FLAG): lactate sensitivity 0.81 / specificity 0.73 could not be traced; the closest source (Dezman 2015, lactate ≥3 mmol/L, 24-h death) gives 0.86 / 0.73 → explanation now says figures vary between cohorts and cites the 0.86/0.73 figure. Source: Dezman et al., J Trauma Acute Care Surg 2015 abstract.
- POLY-19 mimic (and FLAG): added that Cochrane reviews (mostly cardiac surgery) suggest lower mortality with TEG/ROTEM on very low-certainty evidence; the card's watch line "Cochrane found no proven mortality benefit" is out of date (flagged). ITACTIC outcome stated precisely. Source: Cochrane CD007871 (update May 2026, RR 0.76, very low certainty); ITACTIC (Critical Care Reviews summary: 67% vs 64%, p 0.51).
- T_c9721678 b (part, FLAG): Geerts comparison given without the UFH schedule → enoxaparin 30 mg 12-hourly vs UFH 5000 U 12-hourly, DVT 31% vs 44%, proximal 6% vs 15%, no significant excess of major bleeding, not powered for PE (card says "fewer DVT and PE"). Source: Geerts, NEJM 1996 abstract.

### Minor
- POLY-11 punch: "acid halves enzyme activity" → "acid cripples the clotting enzymes" (factor VIIa and Xa/Va lose most activity near pH 7.0, more than half).
- POLY-15 a: added that the European SBP 80–90 target equals MAP 50–60 in the guideline. Source: Rossaint 2023, Rec. 13.
- POLY-18 d (and FLAG): "TASH 16 or more means over 50%" → "roughly 50%, the usual activation threshold" (logistic model gives ≈47% at 16). Source: TASH score documentation (Metricgate), Yücel 2006 model.
- T_c9721678 a, FLAG: added European 6th edition Rec. 37 (drug prophylaxis plus IPC within 24 h of bleeding control, 1B).
- T_9f6a04d7 b: added PCV21 alone as an accepted option (ACIP 2024). Source: MMWR 2024;73(36).
- Top-ups header comment: reviewer's online checks recorded.

### Checked and left unchanged (all confirmed online)
- TOWAR (NEJM, 20 May 2026, doi 10.1056/NEJMoa2602167): cluster-randomised, 1,020 enrolled (993 mITT), up to 2 units LTOWB vs components on air transport; 30-day mortality 25.9% whole blood vs 20.5% components, not significant after adjustment. Explanation ("not better than components") is right. Source: AABB news 20 May 2026.
- UK-REBOA (JAMA 2023): n 90, ~97% blunt, 90-day mortality 54% (25/46) vs 42% (18/43), OR 1.58, posterior probability of harm 86.9%, stopped at the harm rule. Source: PMC10570916.
- CRYOSTAT-2: 28-day mortality 25.3% vs 26.1%; penetrating subgroup 16.2% vs 10%. 1,604 randomised (1,531 analysed).
- CRASH-2: bleeding deaths RR 0.68 (≤1 h), 0.79 (1–3 h), 1.44 (>3 h). Source: Lancet 2011 (LSHTM repository).
- PROPPR: 24-h 12.7 vs 17.0%, 30-day 22.4 vs 26.1% (NS); exsanguination 9.2 vs 14.6% (p 0.03); haemostasis 86.1 vs 78.1% (p 0.006). Source: WikEM / WikiJournalClub.
- PROMMTT: ratios <1:2 had 3–4× the risk of death in the first 6 h (hazard ratios); no association after 24 h. Source: PMC3740072.
- PAMPer: 23.2% vs 33.0% (search results, NEJM 2018); not re-opened in full.
- Bickell 1994: survival to discharge 70% (203/289) vs 62% (193/309), p 0.04, SBP <90 prehospital. Source: Critical Care Reviews.
- European 6th edition: SBP 80–90 (1B), MAP ≥80 in GCS ≤8 (1C), noradrenaline (1C) and dobutamine (1C), Hb 70–90 g/L (1C), FFP:RBC ≥1:2 or fibrinogen/cryo + RBC (1C), high platelet:RBC (2B), TXA (1A), fibrinogen if Clauss ≤1.5 g/L (1C) with 3–4 g = 15–20 single-donor cryo units (2C), platelets >50 with ongoing bleeding and >100 in TBI (2C), ionised Ca in the normal range with calcium chloride (1C; <0.9 and <0.8 thresholds in rationale), rFVIIa not first line (1B), REBOA "be considered" (2C), extraperitoneal packing (1C), no recommendation on prehospital blood.
- ATLS 10th base deficit bands: I 0 to −2, II −2 to −6, III −6 to −10, IV −10 or less; BP first falls in class III. Source: WikEM template.
- AO Spine/Praxis 2024: MAP lower limit 75–80, upper 90–95 mmHg, 3–7 days (weak). AO Spine 2017: 24-h MPSS within 8 h "offered as an option"; not after 8 h; no 48-h infusion. NASCIS III: 48 h better only in the 3–8 h subgroup.
- SAFE-TBI: 24-month mortality 33.2% (71/214) vs 20.4% (42/206); severe TBI 41.8% vs 22.2%.
- ITACTIC: no difference in primary outcome or mortality.
- TASH: 7 variables, 0–28, threshold 16. Lethal triad thresholds (34 °C, pH 7.2) and Jurkovich <32 °C ≈100% (secondary source only; primary abstract not opened).
- ISS/NISS and Berlin definition statements are correct.
- Compartment syndrome: delta-P = diastolic − compartment pressure, decompress under 30 mmHg (McQueen & Court-Brown, JBJS Br 1996).
- Shatz 1998: better functional antibody with 14-day vaccination (IgG similar at 1, 7, 14 days).
- PREVENT CLOT (NEJM 2023): 12,211; aspirin 81 mg bd vs enoxaparin 30 mg bd; death 0.78% vs 0.73%, DVT 2.51% vs 1.71%, PE 1.49% each.
- Not checked online today (standard references, left as written): CRASH-3 numbers, CHEST RRT 7.0 vs 5.8%, CRYSTAL, FIRST, Moore fibrinolysis phenotypes, ABC score 75%/86%, Brohi ~25% ACoTS, OPSI ~50% mortality.

## Final FLAGS — special05b_learn.py
- POLY-11: b Cosgriff odds ratios and 98% predict life-threatening coagulopathy, not death; the card's "predictors of death" / "98% mortality" is a misreading.
- POLY-13: c base excess bands are an older scheme; ATLS 10th class bands taught. a 0.81/0.73 untraced; Dezman 2015 gives 0.86/0.73.
- POLY-15: a SBP 70–90 vs European SBP 80–90 (1B). Last line (SBP 60–70 lowers 28-day mortality) matches no trial; evidence is Bickell 1994 and the MAP 50 vs 65 trial (interim benefit, no mortality difference in the final report).
- POLY-16: d REBOA taught without evidence; UK-REBOA stopped for harm (54% vs 42%); European 2C.
- POLY-18: DocT GT stem prints options B and C identically; intended answer 1:1:1 with platelets. TASH 16 ≈ 50%, not "over 50%".
- POLY-19: stop points from notes are more generous/older than European targets. Watch line's Cochrane statement out of date (Cochrane 2016/2026 lower mortality, very low certainty, mostly cardiac surgery); ITACTIC neutral in trauma.
- POLY-20: Card correct; PATCH-Trauma could be added (6-month function neutral; secondary 24-h/28-day mortality lower).
- POLY-21: Watch line's 6-h mortality benefit is registry data (Wafaisade 2013), no discharge benefit; CRYOSTAT-2 published and neutral (25.3% vs 26.1%).
- POLY-22: a ionised Ca >0.9 is the transfusion-hypocalcaemia threshold; European target normal range. c AO Spine 2017 still offers 24-h MPSS within 8 h; AANS/CNS 2013 recommend against.
- POLY-23: h platelets >100 with ongoing bleeding is 5th-edition wording (6th: >50 bleeding, >100 TBI). d "avoid excess saline" not in the 6th edition recommendation but consistent with its rationale.
- POLY-24: h reason incomplete: ISS sums the squares.

## Final FLAGS — special05b_topups_learn.py
- T_356f55ec: delta-P under 30 is McQueen's diastolic gradient; some use MAP − compartment pressure under 30–40. "Within 6 h" standard teaching. Stems not opened.
- T_9f6a04d7: ACIP 2024 also accepts PCV21 (now in the explanation). OPSI mortality ~50% is the commonly quoted figure (range ~40–70%).
- T_c9721678: card compares with UFH 8-hourly; Geerts used 12-hourly and showed fewer DVT, not fewer PE. European 6th edition: drug prophylaxis plus IPC within 24 h of bleeding control.
