# HY2 — independent review of hy2_learn.py and hy2_topups_learn.py (19 Nov 2026)

Checker: `python3 check_learn.py HY2` → `HY2 27 cards 27 entries OK`, `v3 spine 5 steps OK`. Top-ups (3 cards: T_6ad11458, T_74c38a9d, T_6ad11458b) checked by hand: letters follow the `a` lists, every part opens with the bold restated answer, pairs have 2 items, no banned phrases. No changes were needed there.

## Changes (card: what was wrong → what it says now; source)

### Factual
- CAR-21 b (and header, FLAG): ANNEXA-I was said to show "thrombotic events 14.6% vs 6.9%" → ANNEXA-I (NEJM 2024) showed haemostatic efficacy 67.0 vs 53.1%, thrombotic events 10.3 vs 5.6%, ischaemic stroke 6.5 vs 1.5%. The 14.6 vs 6.9% figure is post-marketing data from the FDA safety communication. "Withdrawn after ANNEXA-I" → US sales ended 22 Dec 2025 after the FDA warning. Sources: NCS Currents ANNEXA-I summary; AABB news, 23 Dec 2025.
- CAR-05 b (and header, new FLAG): no mention of the ESC 2024 threshold → added that ESC 2024 advises against early cardioversion without prior anticoagulation or TOE once AF has lasted ≥24 h (previously 48 h). ACC/AHA 2023 keeps 48 h. Source: Rev Esp Cardiol commentary on ESC 2024 AF guideline.
- CAR-14 a and mimic: "the 2020 expert consensus ranks high-dose insulin above glucagon" in β-blocker poisoning could not be traced → the text now says many toxicologists put high-dose insulin first, as the CCB consensus does (St-Onge, Crit Care Med 2017: insulin first line with calcium and vasopressors, lipid second line). Source: UMEM pearl on St-Onge consensus.
- CAR-02 b: "a lower first dose may suffice via a central line or after transplant" → AHA 2025 says 1 mg may be adequate (the drug arrives undiluted, and denervated receptors are supersensitive). Source: AHA 2025 Part 9 supportive text (cpr.heart.org).
- Header (DanGer Shock): "severe bleeding 20.1 vs 3.4%" → composite safety 24.0 vs 6.2%, moderate or severe bleeding 21.8 vs 11.9% (limb ischaemia 5.6 vs 1.1%, RRT 41.9 vs 26.7% were already right). CAR-18 e and CAR-26 b now say "moderate or severe bleeding", and CAR-18 e gives the figures. Source: ACC DanGer Shock trial summary.

### Minor
- CAR-16 e: added ECLS-SHOCK figures for moderate or severe bleeding (23.4 vs 9.6%) and vascular complications (11.0 vs 3.8%). Source: ACC ECLS-SHOCK summary.
- CAR-20 a: added the ESC 2023 classes for fondaparinux: I in NSTE-ACS when early angiography is not planned, III during primary PCI, IIa with streptokinase. ESC 2023 gives no separate class for unreperfused STEMI, so the card's answer rests on OASIS-6. Source: ESC 2023 ACS guideline, Recommendation Tables 5 and 7.
- Header: the reviewer's online checks are recorded with the date.

### Checked and left unchanged (all confirmed online)
- AHA 2025 bradycardia algorithm: atropine 1 mg every 3–5 min up to 3 mg; dopamine 5–20 µg/kg/min; adrenaline 2–10 µg/min; pacing. Isoprenaline is not in it. The Part 9 text gives no doses: atropine 2a, adrenergic agonists 2b. Source: cpr.heart.org 2025 bradycardia algorithm (accessible version).
- AHA 2025 electrical cardioversion algorithm: narrow-complex 100 J, AF 200 J, flutter 200 J, monomorphic VT 100 J, polymorphic VT defibrillate. Part 9 text: AF ≥200 J (2a), flutter 200 J (2b). This matches the CAR-01 table.
- AHA 2025 Part 9 also confirms: pre-excited AF (digoxin, non-DHP CCB, β-blockers, IV amiodarone COR 3 Harm); adrenaline as soon as feasible in non-shockable and after failed initial defibrillation in shockable (2a); amiodarone/lidocaine 2b; vector change and DSED 2b; magnesium for recurrent polymorphic VT with long QT 2b (3 with a normal QT).
- AHA 2025 Part 11: MAP ≥65 (COR 1), with the SBP target removed; SpO₂ 90–98% / PaO₂ 60–105 (2a); PaCO₂ 35–45 (1); 32–37.5 °C (1) for at least 36 h (2a); rewarm ≤0.5 °C/h (2b); emergent angiography for ST elevation (1), for shock or recurrent VT or ischaemia (2a), not otherwise (3); no seizure prophylaxis (3); prognosis ≥72 h (2a). The CAR-15 FLAG is correct.
- Trials: IABP-SHOCK II 39.7 vs 41.3% (RR 0.96); CULPRIT-SHOCK 45.9 vs 55.4% (death alone 43.3 vs 51.6%); ECLS-SHOCK 47.8 vs 49.0%; DOSE-VF 30.4 / 21.7 / 13.3% (n 405); REVERT 43 vs 17% (40 mmHg for 15 s, then flat with legs at 45° for 15 s); DanGer Shock 45.8 vs 58.5% (HR 0.74); PEITHO decompensation 1.6 vs 5.0% and major bleeding 11.5 vs 2.4%. Sources: ACC trial pages, WikiJournalClub, TheBottomLine, MDedge.
- ESC 2023 ACS: fibrinolysis in STEMI with cardiogenic shock if PPCI is not available within 120 min and mechanical complications are excluded (IIa, C); routine IABP III (B); MCS IIb. The CAR-18 FLAG is correct.
- AHA/ACC 2026 acute PE guideline (Circulation, 24 Mar 2026): categories A–E; lysis Class 3 Harm in A–C2, unclear in C3, may be considered in D, reasonable in E. The CAR-23 explanation and FLAG are correct. Source: LITFL summary.
- Trap "truth" sides (DocT/Marrow disputed keys in CAR-03, -04, -18, -21, -25, -26) agree with the cvs_cardlayer cross lines and with the guidelines above.
- Could not open: PubMed abstract of PEITHO (permission timed out). PEITHO figures were confirmed through MDedge instead; death 1.2 vs 1.8% is from memory and was left as written.

## Final FLAGS
- CAR-15 a: the SBP ≥90 target is out of date. AHA 2025 gives MAP ≥65 only.
- CAR-03 b: the banned list leaves out IV amiodarone, which is COR 3 Harm in pre-excited AF (AHA 2023/2025).
- CAR-18 a: "transfer whatever the delay" is the ACC/AHA answer. ESC 2023 adds IIa lysis in shock if PPCI is not possible within 120 min. This is not an exam error.
- CAR-21: andexanet is off the US market (22 Dec 2025, FDA thrombosis warning; ANNEXA-I thrombotic events 10.3 vs 5.6%). 4F-PCC is now the usual alternative.
- CAR-05 b (new): "above 48 h" is ACC/AHA 2023. ESC 2024 lowered the threshold to 24 h. Not errors on the same card: CHA₂DS₂-VA in ESC 2024; EAST-AFNET 4 could be added.
- CAR-23: not an error. AHA/ACC 2026 renames the PE risk groups as categories A–E.
- Top-ups: no FLAGS.
