# A1 (ACS I, recognising the infarct): fact-check review, 23 Nov 2026

What I checked: the packet open (P12-301), 32 step lessons, five section openings, six spines, the close (P12-306), 25 drill items, 42 traps, 32 mimics, new card V12-004 and 11 card flags. After the edits I re-validated with python. The JSON is valid. Section titles and step order match the pack, with V12-004 after MI-34. Every lesson is 150–4,000 spoken characters. No paragraph is over 1,200, no takeaway over 300, no box over 400 and no bridge over 160. Spoken text has no digits or symbols. The last step's bridge is null. Spoken total: about 82,700 characters, roughly 98 minutes (the addendum sets no time target).

Overall the draft is accurate. I found no wrong number, threshold or key in the lessons, drill, traps or mimics. The writer's Fifth UDMI claims all check out.

## Factual fixes (1)

1. **MI-71 lesson, SCAD patient.** Old: "She is young or middle-aged, often around childbirth, with few risk factors." New: "…with few risk factors, and sometimes pregnant or recently delivered." Only a minority of SCAD cases (about 5–17% in registries) are pregnancy-associated, so "often" overstated it. Source: SCAD registry literature (from knowledge, not fetched).

## Minor fixes (3) and precision additions

2. **MI-28 lesson, pathological Q wave.** Added after the teaching answer of 40 ms or more than 25% of R: "The Universal Definition sets a lower bar: thirty milliseconds wide and one millimetre deep in two contiguous leads, or any Q wave wider than twenty milliseconds in V two and V three." Source: UDMI 2018 Table 3 (ahajournals full text).
3. **MI-22 lesson, V4R.** "The Universal Definition accepts half a millimetre" became "…half a millimetre, or one millimetre in men under thirty." Source: UDMI 2018 text on V3R and V4R.
4. **P12-306 close, type 3 takeaway.** "…before any blood could be taken for troponin" became "…before blood could be taken for troponin, or before it could rise." This makes it match the MI-08 lesson and the UDMI wording.
5. **Card-flag text updated** (MI-25, MI-09, MI-08, MI-05). It now gives the sources I verified and drops the writer's "from memory" caveat on the 6-lead figure.

## Verified (no change needed)

- **Fifth UDMI exists.** It was published 28 Aug 2026 in JACC and EHJ (Mills et al., ESC/ACC/AHA/WHF) and released at ESC 2026. Sources: ACC journal scan, ESC page, Healio, TCTMD, Epocrates, EMJ Reviews (Oct 2026). The draft's claims all match:
  - Primary, secondary and procedure-related categories replace the types.
  - Primary MI includes SCAD, embolism, vasospasm, and stent thrombosis, restenosis or graft failure more than 30 days after a procedure.
  - Secondary MI needs obstructive CAD without acute coronary pathology, and/or a new RWMA or loss of viable myocardium.
  - Procedure-related MI is within 30 days, with unified criteria for PCI and surgery. Fixed troponin multiples are no longer diagnostic.
  - Type 3 is removed and classified by setting or post-mortem findings.
  - Sex-specific 99th centile: "recommended" in 2018, "mandatory" in 2026. The draft's "2018 recommended, 2026 requires" is correct.
  - MINOCA now means myocardial **injury** with non-obstructive coronary arteries, a working diagnosis.
- **UDMI 2018** (full text):
  - V2–V3 J-point thresholds: 2.5 mm men <40, 2 mm men ≥40, 1.5 mm women; 1 mm in other leads.
  - V7–V9 ≥0.5 mm.
  - Type 4a >5×, type 5 >10×, within 48 h, plus ancillary criteria; the >20% rule for a raised baseline.
  - Reinfarction: a >20% rise in the second sample, taken 3–6 h later.
  - Type 3 is reclassified as type 1 if autopsy finds a fresh thrombus.
  - Multilead ST depression with aVR/V1 elevation: **6 leads**.
- **ESC 2023 ACS** (EHJ-ACVC reprint, full text):
  - Left main/multivessel pattern: ≥6 leads.
  - 0 h/3 h is "an alternative where 0 h/1 h or 0 h/2 h are not available".
  - Single-sample rule-out only if pain began >3 h before the 0 h sample.
  - BBB or paced rhythm with suspected ongoing ischaemia is managed like STEMI.
  - CCTA is not first-line in suspected NSTE-ACS.
- **ESC 2020 NSTE-ACS:** ≥6 leads (Termedia review). ESC 2017 STEMI used 8.
- **Chest-pain likelihood ratios** (AFP 2017 table: Chun 2004, Panju 1998, Goodacre 2002):
  - Right arm or shoulder 4.7; both arms 4.1–7.1; left arm 1.8–2.3.
  - Pleuritic 0.2; sharp 0.3; positional 0.3; palpation 0.2–0.4.
  - The draft's "four to five", "about two" and "a fifth" are fine.
- **From knowledge (consistent):**
  - Troponin subunit roles; hs-cTnT 14 ng/L; cTnI more specific.
  - Marker kinetics.
  - ESC hs-cTnT 0 h/1 h cut-offs: <5 (pain >3 h), or <12 with Δ<3; ≥52 or Δ≥5.
  - Sgarbossa points 5/3/2. A score ≥3 has specificity about 90–98% and sensitivity about 20–36%. Smith's ST/S ≤ −0.25 raises sensitivity.
  - Territories, the III > II RCA rule, Takotsubo, apical HCM.
  - MINOCA 5–10% (AHA 2019: 5–6%; ESC: 1–14%), its criteria and CMR in work-up.
- **Open and close agree with the lessons.** All 25 drill answers are correct and unambiguous (D20's 7–10-day tail points only to troponin I).

## Not verified

- AHA 2025 ACLS "recheck at 1 h or 3 h" (MI-75 card): not fetched. It is consistent with the AHA 2021 chest-pain guideline (hs-cTn 1–3 h, conventional assay 3–6 h).
- Class of CMR in MINOCA (ESC 2023 I, B, on V12-004): from knowledge. The fetched text confirmed the role, not the class. The same applies to the class of CCTA (IIa).
- Fifth UDMI full text (JACC/EHJ): not reachable. Everything above rests on concordant secondary reports.
- The lesson's "MINOCA … in some the cause was a pulmonary embolus" and "many type 2 become injury" are reasonable but are not stated in a fetched source.

## Final card flags (11)

| Card | Issue |
|---|---|
| MI-29 | Rows reversed (troponin T/I roles; single versus multiple reference levels). |
| MI-30 | CK-MB for reinfarction is old teaching; current answer is troponin (>20% rise); no mention of cMyC or copeptin. |
| MI-25 | 8 leads (ESC 2017) versus 6 (UDMI 2018, ESC 2020 and 2023). Verified. |
| MI-27 | Takotsubo only in the ST-depression column; it presents with ST elevation. |
| MI-19 | Free wall rupture listed as a murmur; NSVT versus VPBs. |
| MI-09 | Type 5 ancillary list; Fifth UDMI procedure-related criteria (secondary sources). |
| MI-05 | "Usually without significant CAD" is loose; numbered types replaced in 2026 (confirmed). |
| MI-08 | Type 3 retired in 2026 (confirmed); GT8 Q21 keys type 3. |
| MI-22 | UDMI thresholds V7–V9 ≥0.5 mm (≥1 mm men <40); V3R/V4R ≥0.5 mm (≥1 mm men <30). |
| MI-32 | 0 h/3 h is a fallback in ESC 2023 (confirmed wording). |
| MI-16 | Disputed DocT key (ibuprofen and reassurance). |
