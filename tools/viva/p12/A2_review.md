# A2 (ACS II) fact-check review, 23 Nov 2026

Checked: the packet open (P12-401), all 39 step lessons (including V12-010 and V12-011), the five section openings, all six spines, the close (P12-406), 25 drill items, 52 traps, 31 mimics, both new cards and 14 card flags.

After the edits, python confirms: the JSON is valid; the step order matches the pack, with V12-010 after MI-50 and V12-011 after MI-58; every lesson is 150–4,000 spoken characters (MI-64 is 4,200 raw but under 4,000 once its box is excluded); no paragraph, takeaway, box or bridge is over its cap. The only digits in spoken text sit inside abbreviations (PaO2, CYP2C19, V5, PCSK9, P2Y12). Spoken total is about 88,500 characters, roughly 105 minutes.

## Factual fixes (5)

1. **HY2|CAR-18.** Old: "And the only treatment ever shown to save lives in shock is revascularisation." New: "And revascularisation is the treatment with the strongest proof that it saves lives in shock." The old line contradicts DanGer Shock (Impella CP lowered 180-day mortality), which Shock II teaches. This is the same fix made in S2.
2. **Tirofiban renal threshold (MI-48 lesson; V12-010 lesson and box).** Old: halve the infusion "below thirty" (CrCl <30). New: "at a clearance of sixty or below" (CrCl ≤60). Source: ESC 2023 ACS guideline, Table 6, fetched from academic.oup.com: "For CrCl ≤60 mL/min: LD, 25 mcg/kg i.v. over 5 min followed by a maintenance infusion of 0.075 mcg/kg/min" (half of 0.15). The <30 figure belongs to the old low-dose label.
3. **MI-72 and mimic 15, ESC DAPT.** Old: "The European guideline still says twelve months of both, and then usually aspirin alone." New: "The European default is still twelve months of both. It also allows a single antiplatelet, preferably the P2Y12 inhibitor, after three to six months in a patient who is event-free and not at high ischaemic risk, class two a." The mimic was changed to match. Source: ESC 2023, the IIa A de-escalation recommendation. This is from my own knowledge; the fetched sections did not include it.
4. **MI-57, ACE inhibitor above LVEF 40%.** Old: "The ACE inhibitor drops to class two a." New: "…unless there is diabetes, hypertension or kidney disease, which keep it at class one." The box row is now "IIa (I if DM, HTN, CKD)". Source: ESC 2023: ACE inhibitors are I A with HF, LVEF ≤40%, diabetes, hypertension or CKD, and IIa A for all others.
5. **MI-50, ISAR-REACT 5 and prasugrel.** Old: "ISAR-REACT five gave prasugrel only at PCI, once the anatomy was known, and it beat ticagrelor". New: "ISAR-REACT five, which in NSTE-ACS gave prasugrel only at PCI, once the anatomy was known, beat a ticagrelor strategy". The STEMI arm got prasugrel upfront. In the same lesson, the takeaway "Prasugrel is never given before the anatomy is known" now opens "In NSTE-ACS, …", because ESC 2023 gives P2Y12 pretreatment before primary PCI in STEMI a IIb.

## Minor fixes (6)

- **CAR-20.** Cangrelor "Onset in seconds" became "Onset within about two minutes".
- **MI-42.** "meant more re-infarction" became "and in their pooled analysis … meant more recurrent ischaemia and re-infarction". TRANSFER-AMI's benefit was mainly recurrent ischaemia; the meta-analyses show the re-infarction difference.
- **MI-73.** "The guidelines were written before the newest trials" became "Both guidelines were written before most of these trials reported". ACC/AHA (Feb 2025) postdates REDUCE-AMI.
- **CAR-18.** "And never dopamine" became "And not dopamine as the first choice". This keeps it consistent with the S2 dopamine fix (bradycardia use).
- **MI-55.** Added "Abciximab … needs at least twelve hours, though it's rarely used now" and a box row "Abciximab ≥12 h". The pack's bank line asks for it, and trap 32 already has it.
- **JSON layout.** The file was re-serialised with indent=1. The content is otherwise unchanged.

## Verified and left as written

- **Oxygen:** <90% (I) and ≥90% routine (III). DETO2X: about 6,600 patients, 5.0 vs 5.1% at 1 year. AVOID: larger infarcts.
- **Opioids:** ESC 2023 "should be considered" (IIa), with the morphine 5–10 mg dose quoted (fetched). Trap 3 is right.
- **IV metoprolol:** IIa at presentation, no AHF, SBP >120 (fetched). The COMMIT shock excess and the METOCARD-CNIC result are right.
- **Nitrates:** the PDE-5 windows (24 and 48 h), riociguat, and 0.4 mg every 5 min ×3.
- **Aspirin:** ESC 150–300 mg, ACC/AHA 162–325 mg.
- **Times:** 120-minute decision; 60 and 90 minute targets; 10 minutes to ECG and to bolus; 60–90 min for the reperfusion check; 2–24 h angiography after successful lysis (fetched). Lysis within 12 h.
- **Lytic doses:** tenecteplase weight bands (30–50 mg), half dose ≥75; alteplase 15 mg, then 0.75 mg/kg (max 50), then 0.5 mg/kg (max 35); reteplase 10+10 U; SK 1.5 MU.
- **With lysis:** clopidogrel 300 mg (75 mg, no load, >75 y); enoxaparin ≥75 y no bolus, 0.75 mg/kg. ExTRACT-TIMI 25.
- **Lysis contraindications:** the ESC absolute and relative lists are correct. ACC/AHA uses ischaemic stroke <3 months as absolute and major surgery <3 weeks as relative, so the AVM-key reasoning holds.
- **Renal doses:** enoxaparin CrCl <30, 1 mg/kg once daily (fetched); fondaparinux avoid <20 (fetched); bivalirudin <30, 1 mg/kg/h (fetched); UFH 70–100 U/kg (fetched).
- **Prasugrel:** 5 mg if <60 kg or ≥75 (fetched).
- **ESC 2023 classes:** prasugrel over ticagrelor IIa; routine pretreatment in NSTE-ACS III; STEMI pretreatment IIb; early invasive <24 h IIa A; immediate invasive for very high risk (fetched).
- **Trial results:** OASIS-5 (2.2 vs 4.1% bleeding; lower 30-day mortality); OASIS-6; ACCOAST; ISAR-REACT 5 (6.9 vs 9.3%); TRITON (stroke/TIA harm); PLATO (dyspnoea 13.8 vs 7.8%; lower mortality).
- **Antiplatelet pharmacology:** cangrelor t½ 3–6 min; eptifibatide halve <50, none on dialysis.
- **Pre-CABG stop times:** eptifibatide and tirofiban 2–4 h; clopidogrel and ticagrelor ≥24 h urgent; 3/5/7 days elective; aspirin continued.
- **ACC/AHA 2025** (hospital summary of the guideline, fetched): ticagrelor monotherapy ≥1 month (COR 1); prasugrel or ticagrelor with no preference; upstream clopidogrel or ticagrelor if angiography >24 h; LDL ≥70 (1) and 55–69 (2a); lipid recheck at 4–8 weeks; Hb 10 "may be reasonable"; complete revascularisation; imaging for complex lesions; microaxial pump in selected shock; cardiac rehab.
- **Scores:** GRACE has 9 variables on the 6-month nomogram and 8 in the in-hospital version, with >140 high risk. TIMI has 7 items, a 14-day outcome, and 4.7% at 0–1 vs 40.9% at 6–7.
- **Radial trials:** MATRIX 8,404; RIVAL; RIFLE-STEACS.
- **VT mechanism by timing (V12-011):** abnormal automaticity at 24–72 h (surviving partly depolarised Purkinje fibres and myocytes) is correct classic electrophysiology.
- **AV block:** inferior is nodal, anterior infranodal; inferior causes more block; permanent pacing only if the block persists beyond 5 days.
- **Killip classes.**
- **Shock trials:** SHOCK (about 13 per 100 at 6 months); IABP-SHOCK II (600 patients; 30-day, 1-year and 6-year results).
- **ESC 2023 shock classes:** lysis in shock IIa; IABP for a mechanical complication IIa; routine IABP III.
- **RV infarct:** V4R ≥1 mm.
- **Mechanical complications:** posteromedial papillary muscle on a single supply. VSR registry (STS) mortality 54% within 7 days vs 18% after.
- **LV thrombus:** OAC 3–6 months (ESC IIa).
- **MRA:** I A, EPHESUS.
- **Beta-blocker trials:** REDUCE-AMI, REBOOT, BETAMI-DANBLOCK (14.2 vs 16.3%), and the pooled LVEF 40–49 analysis (n about 1,885; 14.4 → 10.7%).
- **MINT:** liberal Hb 10, a trend, p 0.07.
- **Open, section openings and close:** they agree with the steps. The five GT misses are three in this packet (GT7 Q104, GT7 Q109, GT8 Q26) plus the two levosimendan misses; GT7 Q116 is correctly not called a miss. The bank counts quoted (nine on MI-41, six on MI-64) match the pack.
- **Drill:** all 25 answers are correct and unambiguous.

## Could not verify

- **ESC 2023, mild tranquilliser class.** The lesson, spine and trap say IIa. I believe it is IIa C, but it was not in the fetched sections.
- **ESC 2023, eptifibatide below CrCl 30** (whether the table says "not recommended"). The lesson follows the label (<50 halve; dialysis contraindicated).
- **ESC 2023, enoxaparin floor.** The "not recommended below eGFR 15" line in V12-010 was not seen in the fetched text.
- **ESC 2023 shock table, PA catheter IIb and arterial line I.** These are the card's grades; not fetched.
- **Free wall rupture mortality 75–80% and papillary muscle 20–25%.** These are the card's figures.
- **AV block "transient in 10–25%".** This is a bank key and is high against modern series, which put high-degree block at about 3–7%.
- **ACC/AHA 2025, door-to-needle ≤30 min.** The CAR-17 card flag calls it the "older 2013 figure". I believe 2025 keeps it, so the flag wording may be slightly off. The lesson is fine either way.
- **ACC/AHA 2025, the class for transfer to a shock centre.** The existing MI-74 flag stands.
- **ACC/AHA 2025, oral beta-blocker classes by LVEF.** Not fetched. MI-73 says only that both guidelines still support beta-blockers.

## Card flags (final, unchanged)

MI-39, MI-38, MI-47, MI-55, MI-58, MI-60, MI-61, CAR-18, MI-64, MI-65, MI-66, MI-57, MI-74, CAR-17, as in the JSON. No new flags. The tirofiban figure was a lesson error, not a card error.
