# CCM01 review (second, independent check, 22 Nov 2026)

Checked: all 38 cards in cards/CCM01.jsonl against ccm01_learn.py and qpack/CCM01.md, plus consistency with endo02a_learn.py. No Top-up cards. `check_learn.py CCM01` passes: 38/38, spine 6 steps OK.

## Changes (card: what was wrong → what it says now; source)

Factual
- GLU-03 b: said CoV >20% predicts death "independently of mean glucose" in ICU patients in general → now says this holds only in patients without diabetes, with no independent risk in diabetics; punch changed to match. (Krinsley et al., Crit Care 2013;17:R37, 44,964 patients, 23 ICUs.)
- GLU-04 b and punch: the time-in-range claim gave no source detail and no diabetic caveat → now says single-centre cohort of 3,297; non-diabetics above about 80% TIR at 70–140 had mortality 8.5% vs 15.7%, independent after adjustment; no link in diabetics; an association, not a tested target. (Krinsley & Preiser, Crit Care 2015;19:179.)
- GLU-05: figures were "the card's, not traced" → traced to the Leuven Surgical admission data (75% above 110 mg/dL, 12% above 200 mg/dL, ventilated surgical patients). Intro and part b now name the source and say other populations differ. (Van den Berghe, NEJM 2001, full text.)
- GLU-14 c: said cytokines "override" cortisol feedback, which is why cortisol stays high. That contradicts the low ACTH the same card teaches → now says feedback keeps working (so ACTH falls), and cortisol stays high because of direct IL-6 action on the adrenal and slower cortisol breakdown. (Boonen et al., NEJM 2013; the DocT key line.)
- GLU-18 a: "less insulin cleared by the liver" was given as a reason cirrhosis raises glucose, but less clearance raises insulin levels → now says hepatic and muscle insulin resistance plus small glycogen stores; the high insulin from reduced clearance does not overcome the resistance.
- GLU-28 b, trap, decode, punch: said "most guidance (SCCM 2012, ADA) keeps checks every 1–2 h" → now says the ADA hospital chapter asks for checks every 30 min to 2 h while IV insulin runs, and 4-hourly fits a stable patient on SC insulin. The unverified SCCM 2012 attribution is removed. The trap now targets the card's 4-hourly and gives the exam-day rule. (ADA Standards, hospital chapter, dc18-S014 text; SCCM 2024.)
- GLU-30 c and decode: said all patients got "early, high-dose IV glucose (parenteral nutrition was started early)" and "most" had cardiac surgery → now says IV glucose 200–300 g/day from admission, then parenteral, mixed or enteral feeding from the next day; about 63% cardiac surgery. (NEJM 2001 full text.)
- GLU-34 b, decode, punch: said the oral-nutrition exclusion "could not be confirmed" → confirmed: patients able to take oral nutrition were excluded (with expected ICU stay of 3 days or more as the inclusion). (Healio report of the NEJM 2006 trial; PubMed abstract for the 3-day inclusion.)
- GLU-35 b: "hypoglycaemia was an independent risk factor for death in this trial" could not be verified, and the investigators reported no detectable harm → softened: no immediate harm was reported, but later cohorts (Krinsley 2007, NICE-SUGAR 2012) linked even one severe episode with death.

Minor or depth
- GLU-12 a: removed the unsupported claim that sepsis raises glucose more than "an equally stressful sterile insult" → now says inflammation raises glucose both through hormones and at the insulin receptor.
- GLU-16 d: "absolute in DKA, relative in HHS" → "absolute or severe in DKA, relative in HHS, where enough insulin remains to block ketogenesis" (ADA 2024 hyperglycaemic crises consensus).
- GLU-26 c: added LUCID, which the writer could not confirm: 419 type 2 diabetics, liberal 180–252 vs 108–180 mg/dL; hypoglycaemia under 72 mg/dL 5% vs 18% (IRR 0.21); 90-day mortality 29.5% vs 24.9% (P = 0.29); no patient-centred benefit. (Poole et al., Am J Respir Crit Care Med 2022, Flinders abstract.) Matches endo02a.
- GLU-32 b: added Leuven Surgical hypoglycaemia (≤40 mg/dL) 39 vs 6 patients, 5.1% vs 0.8% (NEJM 2001 full text).
- Header: added the second-check sources and dates; updated the "not verified" list.

## Items the writer could not verify, now settled
- NICE-SUGAR: 6,104 patients; 81–108 vs <180 mg/dL; 90-day mortality 27.5% vs 24.9% (P = 0.02); 28-day 22.3% vs 20.8% (NS); severe hypoglycaemia 6.8% vs 0.5% (ACC trial summary). OR 1.14 and the 144–180 rule for the conventional arm were not re-read (both standard; neither is in the explanations as a key figure).
- ADA hypoglycaemia levels: level 1 54–69 (<70), level 2 <54, level 3 = needs third-party help, no number (Endotext Oct 2024; ADA hospital chapter). The card and the explanation are right.
- ADA monitoring on IV insulin: every 30 min to 2 h (ADA hospital chapter text).
- Krinsley TIR and CV: see GLU-03 and GLU-04 above.
- Leuven Surgical hypoglycaemia: 5.1% vs 0.8%.
- GLU-05 prevalence: Leuven Surgical admission data, 75% and 12%.
- LUCID: see GLU-26 above.
- Still unverified (kept, standard figure): Leuven Medical control-arm severe hypoglycaemia 3.1% (18.7% intensive confirmed, Crit Care 2009 review). The ADA non-critically ill target is 100–180 mg/dL in recent editions (Endotext abstract) against 140–180 in the older MDCalc text. This appears only in the header, not in any card explanation.

## Consistency with endo02a_learn.py (not edited)
Targets (start ≥180, target 140–180, SCCM 2024 against 80–139), hypoglycaemia levels, NICE-SUGAR, Leuven, VISEP, LUCID, CONTROLING and monitoring (the endo02a file now also says 30 min–2 h) agree. Discrepancies in endo02a:
1. GLY-02 a: "most strongly in patients without diabetes" understates Krinsley 2013, where CV >20% was independently linked to mortality only in non-diabetics.
2. GLY-03 a: says the 75%/12% figures are only "the card's figures". They are the Leuven Surgical (2001) admission data.
3. GLY-13 d: "severe hypoglycaemia … was itself associated with death" in Leuven Medical was not verified. The investigators reported no detectable adverse effects. Soften it the way ccm01 GLU-35 now reads.
4. Header: NICE-SUGAR control arm is written as "<180". The protocol aimed at ≤180 (144–180). Trivial.
5. GLY-13 a: "both arms received early parenteral glucose and nutrition by local practice". Leuven Surgical gave a fixed 200–300 g/day of IV glucose from admission, then feeding by a standard schedule. Minor.

## Final FLAGS
- GLU-02: Card correct (ADA <70, <54, level 3). The card-layer Marrow line saying "this card uses <60 mg/dL" is out of date. Crossfire's exam rule is kept.
- GLU-14: Incomplete. IL-6 also acts directly on the adrenal cortex (DocT key, 67% right).
- GLU-27: Card correct for ICU. The Marrow ward question's "sliding-scale SC insulin" key is outdated (ADA: basal or basal-bolus plus correction).
- GLU-28: "4th hourly once stabilised" is longer than guidance while IV insulin runs (ADA every 30 min–2 h; SCCM 2024 at least hourly during instability).
- GLU-35: "No difference in primary or secondary endpoints" is wrong. Mortality did not differ, but morbidity fell (kidney injury, ventilation, ICU and hospital stay).
- GLU-38: Incomplete. The insulin arm was itself stopped early for hypoglycaemia (17.0% vs 4.1%).
- Removed: GLU-34. The card is right: patients able to take oral nutrition were excluded.
