# RESP06B review (second check, 11 Nov 2026)

Files: `resp06b_learn.py`, `resp06b_topups_learn.py`. Card text unchanged. `check_learn.py RESP06B`: OK.

## Changes (F = factual, m = minor)

### resp06b_learn.py
1. **PE-16c (F)**: said the clinical predictors "come from registries such as ICOPER". → Now: ICOPER found age >70, cancer, heart failure, COPD, SBP <90, RR >20 and RV hypokinesis; neurological immobilisation and concomitant DVT come from later cohorts such as RIETE. Source: Goldhaber, Lancet 1999 (ICOPER abstract, QxMD).
2. **PE-17a (m)**: "arrest at induction is common" → "arrest can follow induction" (overstated). Source: ESC 2019 §6.1.
3. **PE-18a (m)**: 2026 AHA/ACC "prefers LMWH even in more severe PE" → "recommends LMWH over UFH (Class 1) for almost all patients, including the more severe categories". Source: LITFL "Goodbye massive and submassive"; emDocs 2026 guideline summary.
4. **PE-18d (m)**: heparin resistance "usually" antithrombin deficiency → "often". Non-specific protein binding and inflammation also cause it. Source: The Blood Project, heparin resistance.
5. **PE-19c (m)**: added confirmed bleeding figures. Hokusai-VTE: major plus CRNM bleeding 8.5% vs 10.3%, major bleeding 1.4% vs 1.6% (not significant). RE-COVER: major bleeding 1.6% vs 1.9%, any bleeding lower. Sources: ACC summary of Hokusai-VTE; Wiki Journal Club RE-COVER; ASCO Post (AMPLIFY 0.6% vs 1.8%); ACC EINSTEIN-PE page (major bleeding 1.1–1.2% vs 2.2%; composite 10.3% vs 11.4%).
6. **PE-19 mimic (F)**: said all Xa inhibitors are "reversed by andexanet" → "andexanet reverses apixaban and rivaroxaban". It is not licensed for edoxaban.
7. **PE-20c (F)**: said ESC gives extended treatment for "a persistent factor" in the same breath as recurrence and APS (Class I). → Now: open-ended treatment for recurrence not linked to a major transient factor and for APS; extended treatment "should be considered" for no factor, a persistent factor, or a minor transient factor (IIa). Source: ESC 2019 §8.
8. **PE-21d (F)**: "PEITHO-3 … results expected around 2027" could not be confirmed. → "is no longer recruiting and has not yet reported". Source: trial registry (Veeva CT listing: active, not recruiting; alteplase 0.6 mg/kg, max 50 mg, over 15 min vs placebo).
9. **PE-21d (m)**: HI-PEITHO now gives 544 patients and the primary composite (4.0% vs 10.3%, RR 0.39), led by decompensation (3.7% vs 10.3%). Sources: Critical Care Reviews trial summary; idw-online press release (NEJM, 28 Mar 2026; ACC.26).
10. **PE-23b (F)**: HI-PEITHO population "intermediate-risk" → "intermediate-high-risk". Added that major bleeding did not differ significantly (4.1% vs 2.2–3.0%), as well as no ICH. Source: Critical Care Reviews.
11. **PE-23b (F)**: catheter lysis "about a tenth or less of the systemic dose" (unverified exact fraction) → "a small fraction of the systemic dose".
12. **PE-25c (F)**: said "the perfusion scan gives the fetus slightly more" than CTPA. That is not supported: ESC Table 12 ranges overlap (CTPA 0.05–0.5 mGy). The unit statement was also tightened. ESC 2019 itself writes the threshold as "50–100 mSv". Absorbed fetal dose is properly mGy, numerically equal for X-rays. The real difference is the maternal breast dose (CTPA 3–10 mGy). Source: ESC 2019 full text, §9 and Table 12.
13. **Header comment (m)**: the "from memory" lines were replaced by a note of what was verified.

### resp06b_topups_learn.py
14. **T_51989536a (F)**: rifampicin induction "builds over about a week and fades over 2–4 weeks". → Now: it starts within days and keeps building, with the warfarin requirement plateauing at about 4 weeks; it fades over about 4 weeks after stopping. Source: rifampicin–warfarin case series, Eur J Clin Pharmacol 2021 (doi 10.1007/s00228-020-03057-x).
15. **T_51989536b (m)**: added that the median warfarin requirement rose about 2.6-fold (same source). This is consistent with the card's 2–3 times.
16. **T_51989536c (F)**: said edoxaban is "cleared by CYP3A4 and P-gp". Edoxaban is mainly a P-gp substrate with minimal CYP3A4 metabolism. Exposure falls now given as rivaroxaban about 50%, apixaban about 54%, dabigatran about 66%. Sources: apixaban–rifampin PK study (AUC −54%); dabigatran label data (AUC −66%).
17. **T_cc286408a (F)**: petechiae frequency "about a fifth to half" (unverified) → "often absent and fade within days".
18. **T_cc286408b (F)**: "Gurd's original rule … plus fat macroglobulinaemia; 'two major' is a teaching variant" was unverified as worded. → Now: the most quoted form is 1 major + 4 minor (LITFL, WikEM), and many reviews also accept 2 major, as the card does (Insights Imaging 2021, Table 1: "2 major or 1 major and 4 minor").
19. **T_cc286408c (m)**: steroid evidence made specific: Bederman 2009 meta-analysis, 6 trials and 389 patients, RR 0.22 for FES, no mortality effect, poor-quality trials. Steroids are ineffective as treatment (LITFL). Source: Can J Surg 2009;52:386.
20. **FLAGS (m)**: T_cc286408 flag removed. The card's rule ("≥2 major, or 1 major + ≥4 minor") is published in reviews, so the card is not wrong.

Totals: 20 changes, of which 11 factual (1, 6, 7, 8, 10, 11, 12, 14, 16, 17, 18) and 9 minor.

## Confirmed as written
- **sPESI and PESI**: items and points; 1.0% vs 10.9% 30-day mortality; classes.
- **ESC 2019 Table 9** (RV support): fluids ≤500 mL over 15–30 min; noradrenaline 0.2–1.0 µg/kg/min; dobutamine 2–20 µg/kg/min; ECMO with embolectomy. The guideline adds that HFNC or NIV is preferred and that ECMO with anticoagulation alone is "controversial".
- **ESC 2019 Table 10**:
  - Regimens: rtPA, SK and UK as on the card. Tenecteplase is not listed ("none approved for PE").
  - Contraindications: absolute and relative lists match the card.
  - Lysis window: 48 h, still useful at 6–14 days.
  - CPR: continue for at least 60–90 min after lysis in arrest.
- **ESC 2019 other wording**:
  - LMWH and fondaparinux are preferred over UFH. UFH is reserved for instability, CrCl ≤30 or severe obesity.
  - INR 2–3 on 2 consecutive days.
  - RV/LV ratio >1.0.
  - Pregnancy: ≥6 weeks post-partum and ≥3 months in total; LMWH or warfarin in breastfeeding, NOACs not recommended; LMWH dosed on early-pregnancy weight; lysis only for life-threatening PE.
- **Tenecteplase**: weight bands 30–50 mg in 5 mg steps per 10 kg (WikEM); PEITHO used a weight-adjusted 30–50 mg bolus (Valerio 2019 review).
- **PEITHO** (journalclub.wustl.edu summary of abstract): 1,005 patients; 2.6% vs 5.6%; 7-day death 1.2% vs 1.8%; 30-day death 2.4% vs 3.2%; extracranial major bleeding 6.3% vs 1.2%; stroke 2.4% vs 0.2%, 10 of 12 haemorrhagic.
- **Other trials**:
  - PREPIC 8-year: PE 6.2% vs 15.1%; DVT 35.7% vs 27.5%; no survival difference.
  - PREPIC2: 399 patients; recurrent PE at 3 months 3.0% vs 1.5%; RR 2.0; p 0.50.
  - TRAPS: stroke 7% and MI 5% vs 0%; composite 22% (ITT) or 19% (as treated) vs 3%; stopped early.
  - Artemis: 498 women; VTE 0.21%; CTPA avoided in 39% overall, 65% in the first trimester and 32% in the third.
  - HOME-PE: 1,975 patients; non-inferior; home-treated composite 1.33% vs 1.11%.
- **Hestia**: 11 items. Writer's examples are correct.
- **D-dimer in pregnancy**: 0% of third-trimester women are below 500 ng/mL (Kline 2005, via BestBets).
- **2026 AHA/ACC guideline**: categories A–E; LMWH over UFH Class 1; DOAC over VKA, except thrombotic APS and Child-Pugh C.
- **UFH and fondaparinux**: UFH half-life about 1–1.5 h. Fondaparinux half-life 17–21 h and contraindicated at CrCl <30. Heparin resistance defined as >35,000 U/day, with factor VIII and fibrinogen causing pseudo-resistance.
- **Fat embolism**: Gurd major and minor lists; onset at 24–72 h.

## Final FLAGS
- **PE-14**: Card right. The DocT GT key 'Class IV' is wrong: 70 + 10 + 10 + 20 + 20 = 130, which is Class V. Minor: the watch line says 'RR >30', but PESI uses ≥30. *(unchanged)*
- **PE-18**: Card a follows ESC 2019. The 2026 AHA/ACC guideline recommends LMWH over UFH (Class 1) for almost all patients, including the severe categories. Consider adding the fondaparinux and heparin-resistance facts. *(wording corrected: "categories C–E1" softened)*
- **PE-19**: The watch line is inaccurate on bleeding:
  - EINSTEIN-PE halved major bleeding (1.1% vs 2.2%).
  - Hokusai-VTE did not lower major bleeding (1.4% vs 1.6%), only major plus CRNM bleeding (8.5% vs 10.3%).
  - RE-COVER major bleeding was similar.
  - The DocT TRAPS line mixes outcomes (12% vs 0% thromboembolic; 19–22% vs 3% composite).

  *(now verified, no longer "from memory")*
- **PE-20**: The card's provoked/unprovoked framing differs from ESC 2019's risk-factor categories. Consider adding the rifampicin interaction. *(unchanged)*
- **PE-21**: Update, not an error:
  - PEITHO-3 is active, not recruiting, with no results. The "expected 2027" claim was removed.
  - HI-PEITHO: 544 patients, intermediate-high risk; composite 4.0% vs 10.3%; decompensation 3.7% vs 10.3%; no ICH; no mortality difference.
  - 2026 AHA/ACC: advanced therapy may be considered in category D, unclear in C3, and harmful in A–C2.
  - Tenecteplase is not in the ESC regimen table.

  *(reworded: the "Class 2a in E, 2b in D and C3" claim was unverified and replaced)*
- **PE-23**: The Marrow key 'haemorrhagic stroke' is doubtful. *(unchanged)*
- **PE-24**: Card right. Consider adding imaging of filter thrombus. *(unchanged)*
- **PE-25**: The writer's claim that ESC gives the threshold in mGy is wrong: ESC 2019 itself writes "50–100 mSv". Only the unit nicety remains, which is minor. Consider adding Artemis/YEARS and post-partum duration. *(corrected)*
- **T_cc286408**: Removed. The card's Gurd rule is a published form.
