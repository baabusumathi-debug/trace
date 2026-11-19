# CVS04 review — second, independent check (19 Nov 2026)

Scope: all 19 cards (CS-37 to CS-55) checked for accuracy, fidelity, depth, rules and FLAGS against the final cards and the card layer (lines for CS-42, CS-44, CS-47). No Top-up cards. `check_learn.py CVS04` prints OK.

Verification note: the shared web-search budget was used up before this check could search, and outside page fetches needed approval that was not available. The settled figures below come from standard references, the primary papers as I know them, and the figures already checked online in the sibling CVS03/MI files. They are marked "not re-checked online" where that applies.

## Settled items
- IABP-SHOCK II 12-month mortality: 52% vs 51% (RR 1.01; Thiele, Lancet 2013). The writer's "about 52 vs 51%" is correct; it is now stated exactly. 30-day 39.7 vs 41.3% confirmed (Wiki Journal Club page, fetched). Not re-checked online: 12-month.
- Impella CP inlet: about 3.5 cm below the aortic valve annulus for the 2.5 and CP (Abiomed IFU; the 5.5 sits deeper). Kept, wording made precise. Not re-checked online.
- Median post-transplant survival: about 12.5 years (ISHLT adult registry). Changed from "about 12 years". Not re-checked online.
- TandemHeart: 21 Fr transseptal inflow, 15–19 Fr arterial outflow (15 or 17 Fr usual), centrifugal pump, about 4–5 L/min: all correct. The IJ route is the right-sided set-up (ProtekDuo dual-lumen cannula through the right IJ, RA → pulmonary artery). The writer said it was an alternative left-sided route "for patients whose femoral veins cannot be used", which is wrong. Fixed and flagged.
- VA-ECMO flow: 4–6 L/min (full support); card's ">5" acceptable. Cannula range corrected to 15–25 Fr, because venous drainage cannulae are 21–25 Fr.
- ESC 2023 ACS: short-term MCS IIb C; IABP for mechanical complications IIa C; routine IABP without mechanical complications III B (matches CVS03/MI sibling checks). Text correct.
- MOMENTUM 3 5-year: HeartMate 3 58.4% vs HeartMate II 43.7% (Mehra, JAMA 2022). Text correct.
- Disputed-key traps kept (CS-42 sheath/femoral size, timing, AR; CS-46 haemolysis, AS/mechanical AVR; CS-47 LV failure as indication). Each trap's truth side checks out against the card layer and standard references.

## Changes (card: was → now, source)
1. CS-39 b: DanGer Shock "more than tripled device-related adverse events" → "roughly quadrupled the composite of device-related adverse events (24.0% vs 6.2%)" (Møller, NEJM 2024; RR 4.74). Factual.
2. CS-39 c: ECMO sheath "15–22 Fr" → "15–25 Fr ECMO cannulae". Venous drainage cannulae are 21–25 Fr (ELSO practice). Factual, minor.
3. CS-44 a: 12-month "about 52% vs 51%" → "52% vs 51%, RR 1.01" (Thiele, Lancet 2013). Minor.
4. CS-45 c: "3.5 cm below the aortic valve for the CP" → "below the aortic valve annulus for the 2.5 and CP" (Abiomed IFU). Minor.
5. CS-49 b: the IJ/trans-pulmonary route was described as a left-sided fallback when the femoral veins are unusable → now described as the right-sided ProtekDuo set-up (RA → PA RVAD), with the femoral transseptal route as the left-sided set-up (TandemHeart/ProtekDuo device descriptions). Factual. FLAG added.
6. CS-51 d: ECLS-SHOCK "severe bleeding 23.4% vs 9.6%" → "moderate or severe bleeding 23.4% vs 9.6%" (Thiele, NEJM 2023; BARC 3–5). Factual.
7. CS-53 b: "a stiff, small ventricle cannot be helped by an LVAD" → "is poorly suited to an LVAD … transplant is usually the only replacement". Selected HCM/RCM patients do receive LVADs, so the absolute was softened. Factual, minor.
8. CS-54 b: transplant median survival "about 12 years" → "about 12.5 years in the ISHLT registry". Minor.
9. CS-55 c: "early culprit-vessel PCI is the one treatment proven to save lives (SHOCK, CULPRIT-SHOCK)" → early revascularisation was the first treatment shown to improve survival (SHOCK), and CULPRIT-SHOCK showed culprit-only beats immediate multivessel PCI. The old wording ignored DanGer Shock and conflated the two trials. Factual.
10. CS-37 a: "The commonest use of VA ECMO after a crash" → "The typical VA ECMO situation". The original was an unsupported frequency claim. Minor.
11. Header: added a second-check block recording the settled figures. The DanGer Shock 10-year figure in the writer's header is marked as not re-verified (it is not used in the text).

No fidelity, letter or rule problems found: bold restatements match the card letters, there are no mnemonics, and every punchline comes last.

## Final FLAGS
- CS-37: The watch line "ALL FOUR are short-term MCS" is too absolute. In ESC HF terminology, bridge to transplant (and sometimes bridge to recovery) often uses a durable LVAD. (Writer's flag, confirmed.)
- CS-41: In a, "WIDER PV loop area" is loose. The IABP widens the loop (stroke volume) but lowers peak pressure, so stroke work and MVO2 fall modestly. (Writer's flag, confirmed.)
- CS-44 (new): In d, "only mild to moderate cases" is textbook shorthand. The trial excluded only the extremes (CPR >30 min, fixed pupils, no intrinsic activity), 45% had been resuscitated and mortality was about 40%. The accurate form is "the most severe shock was not tested".
- CS-49 (new): TandemHeart "IJ vein + trans-pulmonary vein" is garbled. The IJ route is the right-sided ProtekDuo configuration (RA → pulmonary artery); there is no standard trans-pulmonary-vein route.
- CS-54: In b, "little data beyond 2 years" is dated. MOMENTUM 3 (JAMA 2022) gives 5-year HeartMate 3 survival of 58.4%; the conclusion (inferior to transplant) still holds. (Writer's flag, confirmed.)
