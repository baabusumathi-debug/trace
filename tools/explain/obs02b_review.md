# OBS02B — independent review of obs02b_learn.py and obs02b_topups_learn.py (12 Nov 2026)

Checker: `python3 check_learn.py OBS02B` → `OBS02B 14 cards 14 entries OK`, `v3 spine 6 steps OK`.
Top-ups (no checker) checked by hand: every part starts with the bold restated answer, all mimic/trap/decode pairs have 2 items, punch 205 and 234 characters (limit 320), no banned phrases.

## Changes (card: what was wrong → what it says now; source)

### Factual
- OBS-30 (trap, decode, FLAG): "ACOG/SMFM plan caesarean at 34+0 to 35+6 weeks with recurrent bleeds" is not an ACOG/SMFM praevia recommendation (that window is ACOG's for accreta) → ACOG/SMFM 36+0–37+6 for uncomplicated praevia; RCOG 34+0–36+6 when there has been bleeding; conclusion (caesarean defensible at 36 weeks, key disputed) unchanged. Source: ACOG Committee Opinion 831 (2021) timing table; RCOG GTG 27a (2018) section 4.8.
- OBS-43 c (part, table, mimic, FLAG): obstetric qSOFA systolic cut-off written as "90 mmHg or less" → "under 90 mmHg". Source: SOMANZ 2017 omqSOFA (SBP <90, RR ≥25, not alert).
- OBS-37 d (part, trap, extra, FLAG): pyelonephritis course "10–14 days" → 14 days in total (ACOG), Marrow's 7–10 noted; added why a short course fails; suppression changed from "then suppression" to "consider suppression". Source: ACOG Clinical Consensus No. 4 (2023).
- OBS-33 f: internal iliac ligation "succeeds in only about half" stated as fact → "about 40–60% in the older series of internal iliac ligation alone, against about 85% when ligation and devascularisation procedures are pooled". Source: Clark 1985 (42%); Doumouchtsis 2007 systematic review (ligation/devascularisation 84.6%, embolisation 90.7%, balloon 84.0%, compression sutures 91.7%).
- OBS-33 b, mimic, extra: transient responder "20–40%" and rapid responder "under 20%" → "roughly 15–40%" and "under about 15–20%". Source: ATLS 10th edition (rapid <15%, transient 15–40%); 9th edition gave 10–20% and 20–40%.
- T_c9b689d4 (trap, decode): stem misdescribed as "prior caesarean with chorioamnionitis and polyhydramnios" → previous caesarean, chorioamnionitis in a previous pregnancy, polyhydramnios now; the two counting medium factors are the scar and the polyhydramnios; noted the stem repeats (GT5) with the same key. Source: full DocT GT2 Q95 stem and explanation in map/doct_gt_distinct_all.jsonl.
- T_c9b689d4 (FLAG, parts a and b, header comment): FLAG said platelets <100,000 and haematocrit <30% as high-risk items are "CMQCC wording, not AWHONN" → they are AWHONN items (haematocrit only "with other risk factors"); the real differences from AWHONN are the dropped qualifier and BMI (>35 in AWHONN; >40 is ACOG Safe Motherhood). Parts a and b now state these two points. Source: AWHONN PPH Risk Assessment Table v1.1 (as reproduced in PMC8289851, Table 1); ACOG Safe Motherhood Initiative risk table (rev. Oct 2015).

### Structural / minor
- OBS-43: parts stopped at h; i and j were only in the table and `extra` → added parts ('i', "**False: by 5 minutes.** …") and ('j', "**False: under 45%.** …") with the why; removed the two duplicate `extra` items; intro no longer says i and j are elsewhere; two traps added for i and j. Source: AHA 2020/2025 maternal arrest algorithm; ESC PPCM definition (EF <45%).
- OBS-43 g, h: parts were a bare restatement with a cross-reference → one sentence of mechanism added to each.
- OBS-31 trap: wrong belief was worded "Primary PPH lasts up to 6 weeks" (not a belief anyone holds) → "Secondary PPH ends at 6 weeks as a fixed fact", corrected with RCOG/ACOG 12 weeks. Source: RCOG GTG 52; ACOG PB 183.
- OBS-32 trap: "BP 90/60 and no asthma" → "no mention of asthma" (the stem is silent; it does not say she has no asthma). Source: qpack OBS-32, first question.
- OBS-33 f: balloon "about 85%" and embolisation "about 90%" kept, now worded "of reported cases" (case-series data). Source: Suarez 2020 meta-analysis (85.9%); Doumouchtsis 2007 (90.7%).
- OBS-38 FLAG: added that bromocriptine (watch line) is a weak recommendation in ESC 2018 and an evidence gap in ESC 2025.
- OBS-30, OBS-37, OBS-43 FLAGS and both file header comments updated to match the above.

### Checked and left unchanged
- WHO/FIGO/ICM 2025: 500 mL retained, act at 300 mL with any abnormal vital sign — confirmed (WHO news release, 5 Oct 2025).
- WOMAN: 20,060 women; death from bleeding 1.5% vs 1.9%; 1 g IV, repeat after 30 minutes — confirmed (AFP summary of Lancet 2017). The within-3-hours figures (1.2% vs 1.7%), no benefit after 3 hours and no fall in hysterectomy are from the Lancet abstract as I know it; the pages I could open did not reproduce them.
- PPCM: ESC EORP registry 6% mortality at 6 months and Elkayam 2001 (persistent dysfunction: about a fifth died; recovered: about a fifth relapsed) match the published figures as I know them; PubMed would not load, so not re-opened today.
- SMFM 2016 AFE criteria, Charbit 2007 (fibrinogen <2 g/L), carboprost 250 µg every 15–90 min to 2 mg, methylergonovine 0.2 mg every 2–4 h, misoprostol 600–1,000 µg, calcium doses in magnesium toxicity, RCOG GTG 5 OHSS grading, obstetric shock index thresholds (El Ayadi 2016: ≥0.9, ≥1.4, ≥1.7): consistent with the sources.
- ESC 2025 mWHO 2.0 class IV table could not be opened (ESC site blocks fetching; two summaries do not list it). Confirmed from summaries only: Pregnancy Heart Team from class II–III, class IV handled by counselling and shared decision-making including termination (class I), left uterine displacement ≥20 weeks and IV access above the diaphragm (class I), heart-failure drugs for at least 12 months after recovery of PPCM (IIa), bromocriptine an evidence gap. The class IV list and numbers stay attributed to ESC 2018.
- "NYHA III–IV = 10% of patients, 85% of cardiac deaths": no primary source found; it is DocT's explanation verbatim. Left as the card states it, flagged.
- Keys called wrong or debatable by the writer (praevia at 36 weeks; carboprost over ergometrine at BP 90/60; misoprostol over methylergonovine in the asthmatic; methylergonovine as the asthma drug; internal iliac ligation vs compression sutures; "cardiogenic" oedema in AFE; "moderate risk" in the top-up): each checked against the real stem and the guideline; all are fairly called debatable.

Not editable by me but wrong: qpack/OBS02B.md, OBS-30 second question, `line` and `key_note` both say "ACOG/SMFM … 34+0 to 35+6 with recurrent bleeds". That window is accreta. The key_note's conclusion still stands.

## Final FLAGS — obs02b_learn.py
- OBS-30: Card sound. DocT key disputed: stable praevia with a repeat bleed at 36 weeks keyed "hospitalisation and pelvic rest" (21% right); ACOG/SMFM deliver uncomplicated praevia at 36+0–37+6, RCOG at 34+0–36+6 after bleeding.
- OBS-31: >500 mL is the traditional WHO definition; ACOG ≥1,000 mL or hypovolaemia; RCOG minor 500–1,000, major >1,000; WHO/FIGO/ICM 2025 adds action at 300 mL with an abnormal vital sign. Watch line ends secondary PPH at 6 weeks; RCOG/ACOG say 12. Inversion management (asked three times) is not on the card.
- OBS-32: Card lacks carboprost's interval and maximum (every 15–90 min, 8 doses = 2 mg), asked twice. Misoprostol 1,000 µg is the top of ACOG's range; WHO/FIGO 800 µg sublingual. Three linked keys debatable.
- OBS-33: Uterine massage listed in active management (WHO 2012 no longer recommends sustained massage after oxytocin; delayed cord clamping). Tranexamic acid only in the watch line. One stem keyed two ways in two DocT tests.
- OBS-35: a 3.3/100,000 within the published 2–6 range; b "15–85%" spans old registries and modern studies (about 20%); e could name the SMFM 2016 criteria.
- OBS-36: Card agrees with current view; linked DocT key says "cardiogenic" oedema while its explanation says non-cardiogenic (it is mixed).
- OBS-37: c "VA-ECMO has reduced mortality" rests on case series. Pyelonephritis management not on the card; Marrow 7–10 days vs ACOG 14.
- OBS-38: c mortality 20–50% is from older series (now about 5–10%; registry 6% at 6 months); incidence varies by region; a ESC definition has no fixed months; d other drugs also avoided; bromocriptine is a weak recommendation / evidence gap.
- OBS-39: Card agrees with AHA 2020/2025; current term resuscitative hysterotomy; d could give the calcium dose.
- OBS-42: Watch line "cystitis with penicillin allergy → cephalexin" follows a GT key; acceptable only if the allergy was not severe.
- OBS-43: No error in the card; obstetric qSOFA is RR ≥25, SBP <90, altered mentation. Parts now a–j.
- No flags: OBS-34, OBS-40, OBS-41 (card text agrees with Charbit/RCOG GTG 5).

## Final FLAGS — obs02b_topups_learn.py
- T_c9b689d4: Matches AWHONN v1.1 except the haematocrit item (AWHONN: <30 AND other risk factors) and BMI (AWHONN >35; card's >40 is the ACOG version, which also uses platelets <70,000 and puts haematocrit <30% in medium). Omits some AWHONN items. "Two or more medium = high" is in both versions; the DocT key ("moderate", GT2 Q95, repeated GT5) conflicts with it. Shock index thresholds agree with El Ayadi 2016; "0.9–1.1" is the Marrow answer.
- T_88bbc332: "Contraindicated in mWHO IV" is ESC 2018 wording; ESC 2025 (mWHO 2.0) frames class IV as counselling and shared decision-making including termination. The class IV list on the card is a selection. The 10% / 85% figure could not be traced to a primary source.
