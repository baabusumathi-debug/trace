# CVS09 top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs09_learn.py.
# Fields: sub, step (index into cvs09_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source question: DocT GT GT2o Q57 (TS270342, cohort 30%), read in full from map/doct_gt_distinct_all.jsonl (stem, options, key C, DocT explanation citing ASRA 2018).
# Checked online on 19 Nov 2026: ASRA 2018 (OpenAnesthesia summary): dabigatran 72 h (CrCl ≥80), 96 h (50–79), 120 h (30–49), avoid neuraxial if CrCl <30; rivaroxaban and apixaban 72 h;
# clopidogrel 5–7 days; aspirin continued.
# From standard references without a fresh check: ASRA 2018 LMWH (prophylactic 12 h, therapeutic 24 h) and IV UFH (4–6 h with a normal aPTT) intervals; dabigatran ~80% renal clearance.
T = {}

T['T_e50055cb'] = dict(
  sub="Cardiology → Aortic repair → Spinal drain and anticoagulant holds",
  step=6,
  intro="Step 6 protects the spinal cord, and a lumbar CSF drain is one of the tools (AD-28). A drain is a neuraxial catheter, so it carries the same risk of spinal haematoma as an epidural, and the same ASRA stop times apply. The Grand Test question asks which drug history makes a drain most dangerous after TEVAR; only 30% picked dabigatran.",
  parts=[
    ('a', "**Aspirin alone: no hold; clopidogrel 5–7 days.** Aspirin on its own does not measurably raise the risk of spinal haematoma. Clopidogrel blocks the P2Y12 receptor irreversibly, so platelet function returns only as new platelets are made, over 5–7 days."),
    ('b', "**Enoxaparin prophylactic 12 h, therapeutic 24 h; IV UFH 4–6 h with a normal aPTT.** LMWH has a predictable half-life, so the interval scales with the dose. IV heparin wears off within hours, but the aPTT confirms it."),
    ('c', "**Apixaban, rivaroxaban: 72 h.** At least five half-lives (apixaban about 12 h, rivaroxaban about 5–9 h); ASRA 2018 does not adjust this hold for renal function."),
    ('d', "**Dabigatran: 120 h (5 days) by default (72 h only if CrCl >80 and no other risk), the longest hold.** Dabigatran is cleared about 80% by the kidney, so its half-life lengthens as renal function falls. ASRA gives 72 h for CrCl ≥80, 96 h for 50–79 and 120 h for 30–49, and advises against a neuraxial procedure below 30. Stopped only 4 days earlier, it is the one drug in the question whose hold may not have been met."),
  ],
  mimic=[
    ("Dabigatran vs factor Xa inhibitors", "Xa inhibitors: 72 h for everyone; dabigatran: 72–120 h depending on CrCl, 120 h if renal function is unknown or impaired."),
  ],
  traps=[
    ("“Apixaban stopped 3 days before” (70% chose a wrong option)", "Three days is the full 72-hour hold, so it is compliant."),
    ("“Enoxaparin prophylaxis 14 hours before”", "The prophylactic interval is 12 hours, so 14 hours is safe."),
    ("“Aspirin the morning of surgery”", "Aspirin alone does not need to be stopped."),
  ],
  decode=[
    ("TEVAR for contained rupture, paraparesis on day 1, spinal drain — which drug history carries the highest haematoma risk? [DocT GT]", "Dabigatran stopped 4 days before (30%): under the 120-hour default hold."),
    ("Minimum dabigatran hold before neuraxial catheter with normal renal function [pattern]", "72 h if CrCl ≥80 and no other risk; otherwise up to 120 h."),
  ],
  punch="A spinal drain follows the neuraxial rules: no hold for aspirin, 12/24 h for LMWH, 72 h for apixaban and rivaroxaban, and up to 120 h for renally cleared dabigatran, the longest and the one most often under-held.",
)
