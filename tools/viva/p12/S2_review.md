# S2 (Shock II) fact-check review, 23 Nov 2026

Checked: the packet open (P12-201), every one of the 28 step lessons, the five section openings, all six spines, the close (P12-206), the 25 drill items, the 51 traps, the 28 mimics, new cards V12-002 and V12-003, and the card flags. After the edits I re-ran the checks with python. The JSON is valid. The step order matches the pack, with V12-002 after CS-29 and V12-003 after SEP-27. Every lesson is between 150 and 4,000 spoken characters. No paragraph is over 1,200 characters, no takeaway over 300, no box over 400, and no bridge over 160. The spoken text has no digits or symbols, and the takeaways stay under a quarter of each lesson. The spoken total is about 57,700 characters, roughly 69 minutes: above the 60-minute target but under the 80-minute ceiling.

## Factual fixes (7)

1. **P12-201 open, the GT-miss count.** Old: "Two of the questions in this packet were misses in your grand tests". New: "Five of the questions…". gt_misses lists five missed items: GT7 Q83, GT7 Q84, GT7 Q87 with GT8 Q82 (one item, missed twice), GT7 Q95 and GT8 Q16.
2. **V12-002, the same count inside the lesson.** Old: "Three questions you missed in your grand tests sit inside one heart cell" (the lesson later says "the two you got wrong"). New: "Three of your grand test questions sit inside one heart cell, and you missed two of them." GT7 Q85 was not a miss.
3. **CS-35 takeaway, SHOCK.** Old: "a significant survival benefit … at six months and one year, fifty point three against sixty-three point one percent". New: "a significant fall in mortality … at six months, fifty point three against sixty-three point one percent, and the benefit held at one year." The 50.3 vs 63.1% figures are *6-month mortality*, not survival and not the 1-year figures. I also added "at thirty days" to the 38% vs 79% PCI line. Source: Hochman, NEJM 1999 (full text from Harvard DASH): n 302; 30-day mortality 46.7 vs 56.0%, P 0.11; 6-month 50.3 vs 63.1%, P 0.027; successful vs unsuccessful PTCA 38 vs 79% at 30 days. The P12-204 spine and trap 37 now carry the 30-day figures too.
4. **P12-204 open takeaway, spine line 1, and trap 36.** Old: "only early reperfusion has been shown to improve survival" / "Only early reperfusion has proven survival benefit". This contradicts CS-46 and ACLS-85, where DanGer Shock (Impella CP) lowered mortality. New: "early reperfusion is the treatment with the strongest proof that it saves lives". Trap 36's truth now names DanGer Shock as the one device exception. The packet open's "the one treatment that actually saves lives" was softened the same way.
5. **CS-26 takeaway and P12-202 spine.** Old: "Dopamine is never the modern answer in cardiogenic shock". New: "no longer the first choice". The old line contradicted CS-32 (AR: dopamine and pacing), CS-31 (RV shock) and CS-33 (bradycardia). The spine now says it survives for bradycardia and, on the card, for AR.
6. **V12-003 and the V12-003 card, the ESC attribution.** Old: "The European heart failure guideline agrees that either may be preferred over dobutamine" and, on the card, "ESC 2021: either may be preferred over dobutamine on a β-blocker". New: "levosimendan or a phosphodiesterase three inhibitor may be considered to reverse the effect of a beta-blocker". The card now says "ESC HF guideline 2016, IIb C". Source: the ESC 2016 HF recommendation (class IIb, C), confirmed through a 2018 review (Cardiovasc Drugs Ther, doi 10.1007/s10557-018-6838-2). I could not confirm the ESC 2021 wording (see Unverified). I also reworded the NEET 2024 line: the pack logs that question as a "false statement" item, so the lesson no longer calls it "the true statement". It now says the question turned on milrinone acting downstream of the receptor.
7. **Isoproterenol, "its only role is as a bridge to pacing"** (V12-002 lesson, mimic 2, V12-002 card). New: "in shock, mainly a bridge to pacing in bradycardia". It has other uses, such as torsades and the denervated transplanted heart.

## Minor fixes (6)

- **SEP-27.** "the only strong recommendation on the ladder" became "the only drug on the ladder with a strong recommendation to give it". The renal-dose dopamine "recommend against" is also strong (SSC 2016).
- **SEP-27.** "Stopping vasopressin first has caused more hypotension" became "In retrospective studies, stopping vasopressin first caused more hypotension". This matches the pack's own bank line.
- **CS-29.** Levosimendan "costs less oxygen and provokes fewer arrhythmias" became "in theory costs less oxygen and provokes fewer arrhythmias". In SURVIVE, AF was more common with levosimendan than with dobutamine.
- **CS-31.** The warm and wet subtype "often after an arrest" became "often with an inflammatory response after the infarct, or after an arrest" (AHA 2017 statement).
- **CS-32.** "At the end of Shock One" became "In Shock One". The AS atrial-kick case is taught at CS-13, which ends section one of Shock I, not the packet.
- **CS-48.** "Routine use is class three, like the balloon" became "In the American guideline of twenty twenty-five, routine use is class three…". Source: ACC "Cardiogenic Shock and MCS: Year in Review 2025": in the 2025 ACC/AHA ACS guideline, routine VA-ECMO and routine IABP are class 3 (no benefit) and the microaxial pump is 2a.

## Verified and left as written

- **SOAP II:** n 1,679; same 28-day mortality; arrhythmias 24 vs 12%; more deaths in the cardiogenic subgroup.
- **CULPRIT-SHOCK (2017):** n 706; 30-day death or RRT; ARR 9.5%. Complete revascularisation evidence comes from PRAMI, CvLPRIT and DANAMI-3-PRIMULTI.
- **IABP-SHOCK II (2012):** n 600; 39.7 vs 41.3%; neutral at 1 and 6 years. The six-variable risk score is correct (prior stroke is in it, prior MI is not).
- **ECLS-SHOCK (2023):** n 420; 47.8 vs 49.0%; more bleeding.
- **DanGer Shock (2024):** n 360; 180-day mortality 45.8 vs 58.5%; more bleeding, limb ischaemia and RRT; 2a in ACC/AHA 2025.
- **β1 pathway:** Gs, cAMP, PKA, then the L-type channel and ryanodine receptor (inotropy) and phospholamban and troponin I (lusitropy). MLCK inhibition belongs to smooth muscle.
- **α1 pathway:** Gq, PLC, IP3 and DAG.
- **Other drugs:** the milrinone renal adjustment; levosimendan (troponin C, K-ATP, active metabolite); omecamtiv versus serelaxin; OptimaCC; methylene blue (NOS and sGC); hydroxocobalamin; ATHOS-3; vasopressin added at norepinephrine 0.25–0.5.
- **IABP:** 7–8 Fr sheath (ACC handbook: usually 7.5 Fr); about 0.5 L/min; tip about 2 cm below the left subclavian and above the renals; contraindications (moderate–severe AR, dissection, severe PVD); ECG or pressure triggering; the timing-error table.
- **Impella CP:** 14 Fr sheath (2.5 uses 13 Fr). Contraindications: mechanical AV, severe AS (relative), LV thrombus. Haemolysis.
- **TandemHeart:** transseptal LA inflow, femoral arterial return, up to about 5 L/min; contraindications VSD, RV failure, AR, PVD, LA thrombus.
- **VA ECMO:** Harlequin and right-hand monitoring, VAV, LV distension and venting, ECPELLA, the distal perfusion cannula.
- **PV-loop shifts** on CS-40.
- **Open and close:** after the edits above, both agree with the steps. The close's six traps match the lessons.
- **Drill:** all 25 answers are correct and unambiguous. Drill 22 (SHOCK "benefit at 6 months, not 30 days") is right.

## Could not verify

- **The ESC 2021 HF guideline text on β-blocked patients.** The full text could not be fetched (PMC was blocked and the supplement does not cover it). The lesson now cites the guideline's position in the 2016 wording, without a year.
- **Impella CP "peak flow 4.3 L/min"** (card figure). The ACC handbook confirms the sheath sizes but not the flow.
- **SSC 2021 "suggest against terlipressin"** (card SEP-27) was not re-fetched.
- **The 1-year SHOCK PCI figures in the CS-35 flag** (Webb 2003: 39 vs 85%) were not fetched. The 1-year overall survival claim (Hochman JAMA 2001: 46.7 vs 33.6%) is from memory.
- **The culprit-vessel mortality figures on CS-34** (SHOCK registry) are the card's own.
- **Note, not an error:** the ACLS-85 lesson and the close both end on the same "next packet: the infarct" teaser. The orchestrator may want to trim one.

## Card flags (final; unchanged in the JSON)

1. **CVS03|CS-26:** ESC 2016 algorithm (inotrope first when SBP <90) versus norepinephrine-first practice (AHA/SCAI, ACC/AHA 2025).
2. **CVS03|CS-35:** 50.3 vs 63.1% is unlabelled 6-month mortality; 35 vs 80% is rounded from 38 vs 79% at 30 days (verified).
3. **CVS04|CS-45:** the 9 Fr / 4.3 L/min figures are for the Impella CP, unnamed on the card; the sheath is 14 Fr.
4. **CVS08E|ACLS-85:** should say that only the IABP needs a regular rhythm.
5. **CVS03|CS-31:** dopamine is still listed for RV shock.

No new flags are needed. One correction is outside the JSON: the V12-003 card line that attributed the β-blocker rule to "ESC 2021" has been fixed in new_cards (fix 6).
