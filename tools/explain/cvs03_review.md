# CVS03 (Cardiogenic Shock I): independent fact-check, 19 Nov 2026

Files checked: cvs03_learn.py (36 cards), cvs03_topups_learn.py (T_62274f28). Fidelity of bold restatements to the cards, and lettering, checked for all 36 cards and the top-up: no mismatches. Cohort percentages in traps/decodes spot-checked against qpack/CVS03.md and doct_qbank_all.jsonl. `check_learn.py CVS03` OK.

## Changes

- CS-10 d: mechanical complications “typically days 2–7” → “usually within the first week (classically days 3–5, but in the reperfusion era often within the first 24 hours)”, after a first, late-presenting or unreperfused infarct (standard teaching; bimodal timing in the reperfusion era). Minor.
- CS-26 trap: “nitroprusside is an arterial dilator” → “potent balanced arterial and venous dilator that needs arterial-line titration and carries cyanide/thiocyanate risk; kept for refractory hypertension or acute valve regurgitation” (pharmacology standard). Factual.
- CS-24 d: added the source for the volume claim. Shaefi 2015 (JAHA, US inpatient sample): adjusted in-hospital mortality was about 37% in the highest-volume quartile vs 42% in hospitals treating ≤27 cases a year. The card’s “>100” cut-off itself could not be traced, so the text does not claim it. Minor.
- CS-35 a: “about a third of the early group had CABG” → “well over a third of those revascularised had CABG” (Wiki Journal Club SHOCK: 60% PCI / 40% CABG). Minor.
- CS-35 f: Webb 2003 figures now say which time point they are. They are one-year mortality: 39% if PCI succeeded vs 85% if it failed; 38/55/100% for TIMI 3/2/0–1 (Webb, JACC 2003 abstract). Card’s 35% vs 80% still not traceable; flag kept. Minor.
- CS-36 c: “At 1 year death and dialysis were no longer significantly different” → “At 1 year the mortality gap (50.0% vs 56.9%) was no longer statistically significant”. The 1-year death-or-RRT composite was not checked, so it is no longer mentioned (CULPRIT-SHOCK 1-year results, ACC summary of the ESC 2018 presentation). Factual.
- CS-05 b: added that the card’s five clinical and three laboratory signs are the ESC 2021 list; only the hypotension requirement has gone (MDPI J Clin Med 2023 review quoting ESC 2021: signs as listed, and “shock may be present even without hypotension”). Minor.
- Header: new “second check” block. It records what was verified, including the ESC 2016 flowchart’s 95%/5% and the SHOCK registry culprit-vessel figures. The two items it had wrongly called “not re-checked” (95/5 and >100) were removed.
- FLAGS CS-26: “95%/5% not verified” → verified. The 95%/5% is the ESC 2016 summary card flowchart’s split for congestion present vs absent. ESC-HF-LT registry at admission: wet-warm 69.9%, wet-cold 19.8%, so about 90% wet.
- FLAGS CS-35: Webb 2003 figures labelled one-year.
- Top-up T_62274f28 trap: “70% picked otherwise, most choosing the β-blocker” → “only 30% chose the key”. The question data give the cohort-correct % only, not the distractor split. Minor.

## Points the writer could not verify: settled

- ESC 2021 HF definition: hypoperfusion from primary cardiac dysfunction. The clinical signs are cold sweated extremities, oliguria, mental confusion, dizziness and narrow pulse pressure. The laboratory signs are raised creatinine, metabolic acidosis and raised lactate. Hypoperfusion is “not always accompanied by hypotension” (ESC 2021 column of the PMC11198174 comparison table; MDPI 2023 review). ESC 2021 sorts acute HF into four presentations. I found nothing showing that ESC 2021 adopts the SCAI classes, and the text does not claim that it does. The explanations were already correct.
- CS-26 95%/5%: verified as above. The card is right to quote it from ESC 2016.
- CS-24 >100 cases/year: not traced. The supporting study (Shaefi 2015) uses quartiles; the lowest is ≤27 a year, and I could not get the top-quartile cut-off (the PMC page was blocked). The direction of the claim is correct.
- CS-34 culprit-vessel mortality: verified exactly. SHOCK registry (Wong et al., JACC 2000): LM 78.6%, SVG 69.7%, Cx 42.4%, LAD 42.3%, RCA 37.4%; left main 15.5%, three-vessel 53.4%.
- CS-35 SHOCK: verified. 30-day mortality 46.7% vs 56.0% (p 0.11); 6-month 50.3% vs 63.1% (p 0.027); under 75 at 30 days 41.4% vs 56.8%. Webb 2003: one-year mortality 39% vs 85% with successful vs failed PCI. The card’s 35% vs 80% is still untraced.
- Also confirmed: SCAI 2022 descriptors (B normal lactate; C lactate ≥2 and CI <2.2; E lactate ≥8 and pH <7.2; arrest modifier = arrest with coma). ACC/AHA 2025 ACS: microaxial pump 2a in selected AMI-CS; routine IABP and routine VA-ECMO 3 (no benefit). DanGer Shock 10-year follow-up 52.5% vs 68.8%. ESC 2023: staged non-culprit PCI IIa in CS. SHARC/CCCTN 2024: AMI-CS 27%, HF-CS 59%, de novo 28% of HF-CS.

## Final FLAGS (unchanged in substance except CS-26 and CS-35 wording)

- CS-01: ‘de novo HF one third’ and AMI-first ordering are from older series. 2024 SHARC registry: AMI-CS 27%, HF-CS 59%.
- CS-05: ‘SBP <90 with adequate volume’ is the ESC 2016 wording. ESC 2021 does not require hypotension. The same applies to the ESC column of CS-07.
- CS-06: the card is correct. The card-layer line credits the 1.8/2.2 split CI to the SHOCK trial, but the trial used CI ≤2.2 and PCWP ≥15.
- CS-08 f: the arrest modifier as written is the 2019 wording. The 2022 update defines it as arrest with coma, and adds the three-axis model.
- CS-14 a: AMI 80% is the older figure; contemporary data give about 27%.
- CS-26: the card follows the ESC 2016 algorithm. AHA/SCAI/ACC-AHA 2025 start norepinephrine first in hypotensive shock. The DocT dopamine key is outdated. 95/5 verified.
- CS-29 d: ‘reduced calcium flux’ for levosimendan is loose (it sensitises troponin C without raising calcium). The DocT ‘decrease dobutamine’ key is disputed.
- CS-30: the card is correct. Two DocT keys are outdated or disputed: dopamine, and ‘decrease dobutamine’.
- CS-35 d: 50.3% vs 63.1% are 6-month figures. f: 35% vs 80% is untraced; Webb 2003 gives one-year 39% vs 85%.
