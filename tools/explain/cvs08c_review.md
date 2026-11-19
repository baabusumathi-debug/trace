# CVS08C review (independent fact-check, 19 Nov 2026)

Files checked: cvs08c_learn.py (18 cards), cvs08c_topups_learn.py (4 Top-ups). check_learn.py CVS08C: OK (18/18, spine 6).

## Changes

- ACLS-41 c: said the advanced devices lie "beyond the glottic opening" (an SGA sits above it) → now "inserted into the pharynx (SGA) or the trachea (tube)". [minor, anatomy]
- ACLS-42 c: post-ROSC PaO2 missing → adds AHA 2025 PaO2 60–105 mmHg with SpO2 90–98% (AHA 2025 Part 11, 2a), and ERC–ESICM 2025 PaO2 75–100 mmHg with SpO2 94–98% (RCUK 2025 post-resuscitation guideline).
- ACLS-44 c: ERC ≥30 mmHg was unverified → confirmed and expanded: ERC 2025 physiology-guided CPR aims for diastolic ≥30 mmHg (arterial line) and ETCO2 ≥25 mmHg (RCUK 2025 adult ALS guideline). FLAG reworded.
- ACLS-45 e: "trials of vasopressin with epinephrine and steroids showed no better survival" (oversimplified) → mechanism (V1 vs α) added; the vasopressin + methylprednisolone combination in IHCA raised ROSC but not survival.
- ACLS-46 a: ALPS "both raised survival to admission" (not confirmed) → removed; now gives the real figures: discharge survival 24.4% amiodarone, 23.7% lidocaine, 21.0% placebo (ns); bystander-witnessed subgroup 27.7/27.8 vs 22.7% (ACC trial summary, MDedge). ERC dosing added (amiodarone after the 3rd and 5th shocks; lidocaine 100 then 50 mg, RCUK 2025).
- ACLS-46 d: fidelity error. The bold restatement said "Lidocaine is class Ib", but the card prints only "Amiodarone (class III)" → bold now restates the card's class III, then gives lidocaine Ib; the amiodarone mechanism moved here from part a. New FLAG.
- ACLS-49 c: "Airway role is not rotated" (invented; AHA does not say this) → now says only that the compressor and AED roles are set to swap, and why ventilation is a separate job.
- ACLS-53 e: ELSO figure imprecise → AHA 2025 Part 10: 55% is survival of 42 obstetric patients given ECLS for arrest; for ECPR itself the figure is 29%; 87% is 30-day survival in 57 patients cannulated. New FLAG on the card's wording.
- ACLS-54 d: "driveline or flat battery is the commonest fault" (unsupported) → softened to "faults fixable at the bedside in seconds".
- ACLS-55 c: alternatives to ice water added (AHA 2025 Part 10: tepid water 8–17 °C or tarp-assisted ice water, 2a). Stopping cooling at 38.6 °C confirmed (2a, C-LD).
- ACLS-55 trap: "Defibrillate and give antiarrhythmics at 29 °C" → split. Under AHA 2025 (one shock, then defer further shocks and epinephrine until ≥30 °C, 2b) the option "defibrillate once and rewarm" is defensible; the exam-day answer stays the keyed "continue CPR, withhold antiarrhythmics". ERC 2025 rules confirmed (3 shocks then delay until >30 °C; no adrenaline <30 °C unless ECPR is imminent; interval 6–10 min at 30–35 °C, RCUK 2025 special circumstances).
- ACLS-56 d: prognostication timing "72 h after ROSC or normothermia" → AHA 2025: consolidate ≥72 h after normothermia and stopping sedation; ERC–ESICM counts from ROSC. Temperature control for ≥36 h (AHA 2025, 2a) added; the why added. Trap aligned.
- Header: the reviewer's sources and dates added; the "not checked" list trimmed.
- Top-up T_cbaf1745 d (drowning): the card's "<60 min" has no guideline source → explanation now gives the Tipton & Golden 2011 thresholds (30 min in water >6 °C, 90 min in water ≤6 °C), and notes that AHA and ERC 2025 give no single cut-off. New FLAG. Header updated (ERC 2025: 5 breaths with 100% O2).

## Confirmed without change
- AHA 2025 hypothermia: HOPE <0.1 predicts death, ICE >12 predicts survival; ECLS without arrest if core <28 °C (2b); ECLS rewarming at 1.5–5 °C/h.
- Asthma: ECLS 2a, volatile anaesthetics 2b, survival 83.5–100%.
- LVAD: MAP >50 or PETCO2 >20 mmHg; compressions class 1.
- AFE: balanced MTP and TXA, both class 1. Upper-limb access 2a. Calcium on magnesium 2a. Fetal monitors removed.
- 2026 AHA/ASA stroke guideline: tenecteplase 0.25 mg/kg (max 25 mg) or alteplase 0.9 mg/kg within 4.5 h (COR 1); initial brain scan within 25 min of arrival (AHA news release).
- Tryptase 1.2 × baseline + 2 ng/mL (the 20% + 2 rule, Valent 2012 consensus): correct.
- ERC adrenaline after the 3rd shock; AHA after the 2nd.
- The heat-stroke trap (DocT key of 36 °C is wrong; AHA 2025 stops at 38.6 °C) is correct.

## Final FLAGS

**cvs08c_learn.py**
- ACLS-41: SGA/i-gel/Combitube are ACLS "advanced", not ATLS "definitive", airways.
- ACLS-42: Card correct. The NEET 2025 key (chest X-ray for "best verification") shows depth only; capnography is the standard.
- ACLS-44: Card correct. AHA 2025 sets no diastolic target; ERC 2025 uses ≥30 mmHg and ETCO2 ≥25. The DocT ">20 mmHg" is AHA 2020.
- ACLS-46: In d, the card gives a class only for amiodarone (III); lidocaine is Ib. The DocT eclamptic-VF key is disputed: lidocaine + Mg is equally correct.
- ACLS-52: The DocT key "give magnesium promptly" is wrong: stop magnesium and give calcium.
- ACLS-53: In e, the 55% is ELSO ECLS survival in 42 obstetric arrests; ECPR itself is 29%. The DocT "HELP trial" does not exist.
- ACLS-55: The DocT key "cool to 36 °C" is wrong (38.6 °C). The card-layer line "AHA more permissive" in hypothermia is outdated. In the 29 °C VF question, "defibrillate once" is also defensible.
- ACLS-58: "rtPA" is dated: tenecteplase or alteplase per the 2026 AHA/ASA guideline; the scan should be within 25 min.

**cvs08c_topups_learn.py**
- T_cbaf1745: In d, "submerged <60 min" is not a guideline figure. The thresholds are 30 min (water >6 °C) and 90 min (water ≤6 °C), from Tipton & Golden 2011.
