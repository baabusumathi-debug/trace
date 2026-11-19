# CVS10E — Explain v3 ("Learn" depth): ACS V, what changed in the 2025/2026 guidance — UDMI 2018 → UDMI 2026 (numbers that died), classifying cases under UDMI 2026, ACC/AHA 2025
# antiplatelet changes, the beta-blocker trials in preserved/mildly reduced EF, revascularisation and shock, troponin pathways, lipids, rehabilitation and anaemia.
# No mnemonics or hooks. Driven by qpack/CVS10E.md (2 question links, both on MI-71: DocT GT GT1o early stent thrombosis, cohort 48%; NEET 2025 recall stent thrombosis at 2 months).
# MI-70, MI-72, MI-73, MI-74, MI-75 and MI-76 have no linked question and get short explanations with [pattern] decode items.
# One Top-up card (T_08cd9563, retroperitoneal bleed) is in cvs10e_topups_learn.py. No `fix` entries for CVS10E in trace/test/data/qbank.json (checked 19 Nov 2026).
# cvs_cardlayer.json `lines` for MI-71 (DocT GT stent thrombosis; Marrow SCAD/FMD) read and covered.
# Checked online on 19 Nov 2026:
#  - Fifth Universal Definition of MI (2026; ESC Congress, Aug 2026; Eur Heart J doi 10.1093/eurheartj/ehag101) via the ESC Congress news page and the ConsultantLive/HCPLive summary
#    (28 Aug 2026): types 1–5 replaced by primary, secondary and procedure-related MI; type 3 no longer separate, fatal MI classified by setting or post-mortem findings; procedure-related MI =
#    acute ischaemia and injury due to a complication within 30 days of a percutaneous or surgical cardiac procedure, no biomarker threshold, same criteria for PCI and CABG; restenosis, stent
#    thrombosis and graft failure >30 days = primary MI; primary MI includes SCAD, vasospasm, embolism; secondary MI confirmed by obstructive CAD without acute coronary pathology and/or injury
#    enough to cause a new RWMA or loss of viability; sex-specific 99th percentile URLs; MINOCA now a working diagnosis referring to myocardial injury, reclassified if MI is later confirmed.
#    The AHA ‘Top things to know’ page could not be opened.
#  - ACC/AHA/ACEP/NAEMSP/SCAI 2025 ACS guideline (Rao et al., Circulation 2025;151:e771; full PDF read in parts via accga.org copy, plus Hendrick Health ‘at a glance’ and a Cleveland/OSU
#    lecture): DAPT ≥1 year if not high bleeding risk (1, A); ticagrelor monotherapy ≥1 month after PCI in those who tolerated DAPT with ticagrelor (1, A); switch ticagrelor/prasugrel →
#    clopidogrel after 1 month (2b); SAPT after 1 month in high bleeding risk (2b); prasugrel or ticagrelor for PCI in NSTE-ACS and STEMI (1); upstream clopidogrel or ticagrelor if angiography
#    >24 h in NSTE-ACS (2b, B-NR); early (<24 h) oral beta-blocker in ACS without contraindications (1, A), benefit established for LVEF <40%, duration in preserved EF unclear; radial over
#    femoral (1, A); IVUS/OCT for stenting of left main or complex lesions (1, A); emergency culprit revascularisation in shock (1, B-R); routine non-culprit PCI at the index procedure in shock
#    (3: Harm, B-R; STEMI and NSTE-ACS); microaxial flow pump in selected STEMI with severe/refractory shock (2a, B-R); routine IABP or VA-ECMO (3: No benefit, B-R); MCS as bridge to surgery
#    for mechanical complications (2a); ACS with shock admitted to a CICU (1, C-EO); mechanical complications managed where cardiac surgery is available (1, C-EO); high-intensity statin (1, A);
#    non-statin if LDL-C ≥70 mg/dL on maximal statin (1, A), reasonable at 55–69 (2a, B-R); concurrent ezetimibe at start 2b; fasting lipid panel 4–8 weeks after starting/changing (1, C-LD);
#    cardiac rehab referral before discharge (1, A), home-based a reasonable alternative (2a, B-R); transfusion to Hb ≥10 g/dL in anaemia may be reasonable (2b, B-R); colchicine 2b.
#  - ESC/EAS 2025 dyslipidaemia focused update (ESC Council for Cardiology Practice summary): LDL-C goals unchanged from 2019; in ACS already on therapy, intensify during the index admission
#    (I, C); therapy-naive, consider high-intensity statin + ezetimibe during admission if the goal is unlikely with statin alone (IIa, B); bempedoic acid added; Lp(a) once in life (IIa, B).
#  - REDUCE-AMI (PCRonline summary of NEJM 2024): n 5,020, LVEF ≥50%, obstructive CAD, 95% PCI; death or MI 7.9 vs 8.3%, HR 0.96, median 3.5 years.
#  - REBOOT (herzmedizin.de ESC 2025 report): n 8,505, LVEF >40%; death/MI/HF 22.5 vs 21.7 per 1,000 patient-years, HR 1.04 (0.89–1.22). Signal of more events in women (HealthDay headline).
#  - BETAMI-DANBLOCK (same report): n 5,574, LVEF ≥40%; 14.2 vs 16.3%, HR 0.85 (0.75–0.98).
#  - LVEF 40–<50% pooled analysis (same report; cvs10d header for trial sizes): n 1,885 (REBOOT, BETAMI, DANBLOCK, CAPITAL-RCT); HR 0.75 (0.58–0.97); 10.7 vs 14.4% (card figure).
#  - ABYSS (ACC summary of ESC 2024 / NEJM): n 3,698, LVEF ≥40%, MI ≥6 months earlier (median 2.9 years); interruption vs continuation: death/MI/stroke/CV admission 23.8 vs 21.1%,
#    non-inferiority not shown; no gain in quality of life.
#  - DanGer Shock and ESC 2023 classes as checked in cvs10d/cvs10c/cvs10b headers (19 Nov 2026): 180-day death 45.8 vs 58.5%; ESC 2023 hs-cTn 0 h/1 h or 0 h/2 h (I, B), 0 h/3 h an
#    alternative without a class; ESC 2023 DAPT 12 months (I, A); pretreatment if invasive >24 h IIb; prasugrel over ticagrelor IIa B.
# Second review (19 Nov 2026, cvs10e_review.md): ESC 2023 wording re-read on the Eur Heart J full text (0 h/1 h best, 0 h/2 h second-best, 0 h/3 h alternative; complete revascularisation
#  recommended in STEMI within 45 days / should be considered in NSTE-ACS; intravascular imaging should be considered; SAPT after 3–6 months should be considered; HBR monotherapy after 1 month
#  may be considered; pretreatment >24 h may be considered; prasugrel in preference to ticagrelor should be considered). Shock-centre transfer: ACC 2025 shock year-in-review attributes it to
#  the ACC 2025 concise clinical guidance, not the ACS guideline; Cleveland Clinic summary calls it Class 1. MINT, REBOOT sex analysis and the chest pain guideline from memory (no fresh check).
# From standard references without a fresh check (confident unless said): UDMI 2018 type 4a/5 thresholds (>5× and >10× the 99th URL within 48 h, plus new ischaemic evidence); ESC 2023
# P2Y12-monotherapy after 3–6 months (IIa) and de-escalation (IIb); ESC 2023 complete revascularisation in stable STEMI (I, A; index or within 45 days) and IVUS/OCT (IIa) — moderately sure;
# ULTIMATE-DAPT and TWILIGHT (ticagrelor monotherapy, less bleeding, no ischaemic penalty); MINT (2023: liberal ≥10 g/dL vs restrictive 7–8 g/dL in MI with anaemia, 30-day death/MI 14.5 vs
# 16.9%, RR 1.15, P 0.07); DanGer Shock selection (STEMI, lactate ≥2.5, LVEF <45%, comatose OHCA and RV shock excluded); AHA/ACC 2021 chest pain guideline (hs-cTn repeat 1–3 h, conventional
# 3–6 h). The AHA ACLS ACS algorithm wording ‘recheck at 1 h or 3 h’ is from the course card ACLS-57 and was not re-read in the 2025 AHA text. LDL conversion 70 mg/dL ≈ 1.8 mmol/L, 55 ≈ 1.4.

SPINE = [
  ("Ruling in faster: troponin timing", "ESC 2023 repeats high-sensitivity troponin at 1 or 2 hours, not 3; the 3-hour schedule survives only as a fallback and in the AHA ACLS algorithm."),
  ("The definition was rebuilt", "UDMI 2026 drops numbered types, troponin multiples for procedures and the 48-hour window, uses sex-specific limits, and calls MINOCA an injury until a cause is found."),
  ("Classifying the case", "A troponin rise is sorted by setting: an acute coronary event is primary MI, an outside stress on obstructive CAD or a new wall-motion defect is secondary MI, a complication within 30 days of a procedure is procedure-related, and anything without ischaemic proof is injury."),
  ("Antiplatelets: dropping aspirin early", "ACC/AHA 2025 keeps 12 months of DAPT as the default with prasugrel or ticagrelor, but lets the patient drop aspirin and stay on ticagrelor alone from one month to cut bleeding."),
  ("The artery, the access and shock", "Treat every significant lesion in stable patients, image complex ones, go radial, but in shock open only the culprit, use a microaxial pump only in selected STEMI shock, and never IABP or VA-ECMO routinely."),
  ("After the ward: beta-blocker, lipids, rehab", "Beta-blockers help when LVEF is below 50% and not clearly above it; LDL-C at or above 70 mg/dL on a maximal statin mandates another agent, rehab is referred before discharge, and Hb 10 g/dL may be a reasonable target."),
]

PRIMER = "This deck is a list of changes, so the old rule and the new one are learnt side by side and the exam question decides which it wants. ACC/AHA grade recommendations 1 (recommended), 2a (reasonable), 2b (may be reasonable) and 3 (No benefit or Harm); ESC grades I, IIa (should be considered), IIb (may be considered) and III. The Fourth Universal Definition (2018) sorted MI into types 1–5; the Fifth (2026, published August 2026) replaces them, so older keys still use the types. American guidance gives LDL-C in mg/dL: 70 mg/dL is about 1.8 mmol/L and 55 mg/dL about 1.4 mmol/L, the ESC goal."

L = {}

L['MI-70'] = dict(
  sub="Cardiology → ACS → UDMI 2018 to UDMI 2026",
  step=2,
  intro="Step 2 is the rebuilt definition. No real question is linked yet (the definition is three months old); the card is a translation table, and the testable point is why each old element went.",
  parts=[
    ('a', "**Types 1–5 → primary / secondary / procedure-related.** The numbers mixed mechanism (type 1 plaque, type 2 supply–demand) with setting (4 and 5 procedures) and outcome (3 death). The 2026 scheme sorts by setting only: an acute coronary event, an outside stress, or a procedure."),
    ('b', "**Type 3 → removed; classify fatal MI by setting / autopsy.** Type 3 was a death before troponin could be drawn; it told you nothing about cause. The death is now filed under whichever setting the history or post-mortem shows."),
    ('c', "**>5× / >10× URL → no troponin multiples; complication and/or imaging evidence.** Troponin rises after almost every PCI and every CABG, so a multiple of the URL could not separate a real infarct from expected procedural injury. Procedure-related MI now needs an identifiable complication (side-branch loss, dissection, graft failure, no-reflow) with ischaemia and injury, and the same criteria apply to PCI and surgery."),
    ('d', "**48 h window → 30 days.** Early stent thrombosis and graft failure happen within the first month, after the 48 hours had closed; 30 days captures them as procedure-related. Beyond 30 days the event is new disease and counts as primary MI (MI-71)."),
    ('e', "**One 99th URL → sex-specific 99th URL.** Women have lower normal troponin concentrations, so a single cut-off set largely on men under-recognised injury in women; the 2026 task force calls sex-specific limits necessary."),
    ('f', "**MINOCA = infarction → MINOCA = injury, a working diagnosis.** Most patients labelled MINOCA turn out to have myocarditis, Takotsubo or a non-cardiac cause. The label now means ‘injury with non-obstructive coronaries, cause not yet found’; once a cause is proven the patient is reclassified (primary, secondary, procedure-related or a non-MI diagnosis)."),
  ],
  mimic=[
    ("UDMI 2018 type 2 vs UDMI 2026 secondary MI", "Type 2 accepted supply–demand ischaemia on symptoms or ECG; secondary MI needs obstructive CAD on coronary assessment or a new wall-motion defect / loss of viability on imaging."),
  ],
  traps=[
    ("“PCI-related MI: troponin >5 × URL within 48 h”", "That is UDMI 2018 type 4a. Under UDMI 2026 there is no multiple and the window is 30 days; read which definition the stem assumes (watch line)."),
  ],
  decode=[
    ("[pattern] Which UDMI 2018 element was abolished outright in 2026?", "Type 3 (fatal MI), and the troponin multiples for PCI and CABG."),
    ("[pattern] Time window for procedure-related MI under the 2026 definition?", "30 days after the percutaneous or surgical cardiac procedure."),
  ],
  punch="UDMI 2026 classifies MI by setting, not by number: no type 3, no 5× or 10× multiples, a 30-day procedural window, sex-specific 99th percentiles, and MINOCA demoted to injury until proven otherwise.",
)

L['MI-71'] = dict(
  sub="Cardiology → ACS → Classifying cases under UDMI 2026",
  step=3,
  intro="Step 3 puts the new definition to work. Both real questions are stent thrombosis presenting as STEMI, one hours after PCI (48% right) and one at two months; the classification changes with the clock, the treatment does not.",
  parts=[
    ('a', "**Stent thrombosis, day 10 → procedure-related MI (≤30 days).** It is a complication of the procedure inside the 30-day window. Classification aside, a new ST rise in the stented territory is a STEMI and goes straight back to the lab."),
    ('b', "**Stent thrombosis, 6 months → PRIMARY MI (>30 days).** After 30 days stent thrombosis, restenosis and graft failure are treated as de novo coronary disease and filed as primary MI. The NEET 2025 stem (stent 2 months earlier) is therefore a primary MI."),
    ('c', "**SCAD → PRIMARY MI.** Primary MI now covers every acute coronary pathology, not only plaque rupture: SCAD, vasospasm and coronary embolism are included. In 2018 SCAD sat under type 2 (supply), which is why it is the trap. SCAD affects mainly young and middle-aged women, often peripartum, and many have fibromuscular dysplasia, so renal, iliac and cerebral arteries are screened (Marrow line)."),
    ('d', "**GI bleed + known obstructive CAD + new RWMA → SECONDARY MI.** The bleed (anaemia, hypotension) is the outside stress; obstructive CAD without an acute coronary lesion and a new wall-motion defect each confirm secondary MI. The treatment is the bleed and the haemoglobin, not antithrombotics."),
    ('e', "**Sepsis, no ischaemic evidence → myocardial INJURY, not MI.** Troponin rises in sepsis from inflammation, tachycardia and hypotension; without obstructive CAD or a new wall-motion defect there is no proof that ischaemia caused it. In 2018 many such cases were called type 2 MI."),
    ('f', "**Non-obstructive coronaries, cause unknown → MINOCA, a working diagnosis.** Next comes the search for the cause, with CMR first (ESC 2023 I, B), then reclassification."),
  ],
  table=dict(title="Stent thrombosis: the clock files it, the ECG treats it", head=["Timing", "UDMI 2026", "Management"], rows=[["≤30 days after PCI", "procedure-related MI", "STEMI pathway: DAPT load, heparin, urgent angiography and PCI"], [">30 days after PCI", "primary MI", "the same"]]),
  mimic=[
    ("Secondary MI vs myocardial injury", "Both follow an outside stress; secondary MI needs obstructive CAD or a new RWMA/loss of viability, injury has neither."),
    ("SCAD vs atherothrombotic primary MI", "Both are primary MI; SCAD is a young woman, often peripartum or with FMD, few risk factors, and is usually managed conservatively unless flow is lost."),
  ],
  traps=[
    ("“Intravenous nitroglycerin” or “transthoracic echo” first for new chest pain and ST elevation after PCI", "Only 48% chose urgent repeat angiography. New ST elevation in the stented territory is acute stent thrombosis, a STEMI; nitrates, observation or echo only delay reperfusion."),
    ("“Thrombolysis” for stent thrombosis with ST elevation", "Stent thrombus is platelet-rich and responds poorly to lysis; load DAPT, anticoagulate and send for primary PCI. Heparin alone or a beta-blocker is not reperfusion."),
    ("“SCAD is a supply–demand (secondary) MI”", "That was 2018 type 2; in 2026 SCAD is an acute coronary pathology, a primary MI."),
    ("“Sepsis with a troponin rise is a secondary MI”", "Not without ischaemic proof (obstructive CAD or a new RWMA); it is injury."),
  ],
  decode=[
    ("New chest pain and ST elevation in the stented territory hours after PCI — next step? [DocT GT]", "Urgent repeat coronary angiography (acute stent thrombosis)."),
    ("DES 2 months ago, anterior ST elevation, suspected stent thrombosis — immediate management? [NEET 2025]", "DAPT with urgent PCI; under UDMI 2026 it is a primary MI (>30 days)."),
    ("[pattern] Septic shock, troponin rise, normal coronaries, no wall-motion change — UDMI 2026 label?", "Myocardial injury, not MI."),
  ],
  punch="File stent thrombosis by the clock (≤30 days procedure-related, later primary), file SCAD as primary, demand secondary MI to show obstructive CAD or a new RWMA, and treat every stent thrombosis with ST elevation as a STEMI: DAPT and the cath lab, not lysis.",
)

L['MI-72'] = dict(
  sub="Cardiology → ACS → ACC/AHA 2025 antiplatelet changes",
  step=4,
  intro="Step 4: the antiplatelet rules after PCI. No real question is linked; the testable change is which drug is dropped early, and that ESC and ACC/AHA drop different ones.",
  parts=[
    ('a', "**Aspirin + oral P2Y12 for at least 12 months — default.** ACC/AHA 2025 gives DAPT for at least 1 year (1, A) in patients not at high bleeding risk, because stent thrombosis and new plaque events cluster in the first year."),
    ('b', "**Tolerating DAPT → switch to TICAGRELOR MONOTHERAPY ≥1 month after PCI (to reduce bleeding).** Class 1, A. Once the stent is covered, aspirin adds bleeding more than protection on top of a potent P2Y12 inhibitor; ticagrelor-alone trials (TWILIGHT, ULTIMATE-DAPT) cut bleeding without more ischaemic events. Lesser options are 2b: switching ticagrelor or prasugrel to clopidogrel after 1 month, or single antiplatelet therapy after 1 month if bleeding risk is high."),
    ('c', "**Ticagrelor or prasugrel; clopidogrel if these cannot be used.** Class 1 for PCI in STEMI and NSTE-ACS, for fewer MACE and stent thromboses; ACC/AHA names no preference between the two, whereas ESC 2023 prefers prasugrel for patients going to PCI (IIa, B; ISAR-REACT 5). Clopidogrel is for those who cannot take them (prior stroke for prasugrel, oral anticoagulation, high bleeding risk)."),
    ('d', "**NSTE-ACS with angiography delayed >24 h → clopidogrel or ticagrelor.** It is 2b (‘may be considered’). Routine pretreatment before early angiography is not advised: the anatomy may send the patient to CABG, and prasugrel is not used before the anatomy is known. ESC 2023 also gives pretreatment beyond 24 hours IIb."),
  ],
  mimic=[
    ("ESC 2023 vs ACC/AHA 2025 at the end of DAPT", "ESC: 12 months of DAPT, then usually aspirin alone; single antiplatelet therapy, preferably a P2Y12 inhibitor, after 3–6 months ‘should be considered’ (IIa) if event-free and not high ischaemic risk, and aspirin or P2Y12 monotherapy after 1 month ‘may be considered’ (IIb) only in high bleeding risk; de-escalation in the first 30 days is not recommended. ACC/AHA: can drop aspirin at 1 month and continue ticagrelor alone."),
  ],
  traps=[
    ("“After 1 month of DAPT, continue aspirin alone” as the ACC/AHA bleeding-reduction option", "The Class 1 option keeps ticagrelor and drops aspirin (watch line)."),
  ],
  decode=[
    ("[pattern] ACS, PCI, tolerating ticagrelor-based DAPT, worried about bleeding — ACC/AHA 2025 option at 1 month?", "Stop aspirin, continue ticagrelor alone (1, A)."),
    ("[pattern] NSTE-ACS, angiography planned at 48 h — P2Y12 before the lab?", "Clopidogrel or ticagrelor may be considered (2b); not prasugrel."),
  ],
  punch="Default DAPT is 12 months with prasugrel or ticagrelor; ACC/AHA 2025 lets the patient drop aspirin and stay on ticagrelor alone from 1 month, whereas ESC keeps aspirin at the end.",
)

L['MI-73'] = dict(
  sub="Cardiology → ACS → Beta-blockers after MI without reduced EF",
  step=6,
  intro="Step 6 starts with the drug whose old rule (everyone after MI) came from the pre-reperfusion era. No real question is linked; four recent trials answer whether reperfused patients with good LVEF still need it.",
  parts=[
    ('a', "**REDUCE-AMI: LVEF ≥50% → no benefit.** 5,020 patients with obstructive CAD, 95% treated by PCI: death or MI 7.9% vs 8.3% (HR 0.96) over a median 3.5 years. With a small infarct and a normal ventricle there is little arrhythmic or remodelling substrate for the drug to act on."),
    ('b', "**REBOOT (~8,000): LVEF >40%, no HF → no benefit overall; signal at 40–49%.** 8,505 patients: death, reinfarction or HF admission HR 1.04 (0.89–1.22). A prespecified sex analysis suggested more events with beta-blockers in women, mainly those with preserved EF, and none in men; it is hypothesis-generating, not a reason to withhold the drug when LVEF is reduced."),
    ('c', "**BETAMI-DANBLOCK (~5,500): LVEF ≥40% → fewer events (14.2% vs 16.3%).** 5,574 patients, HR 0.85 (0.75–0.98), median follow-up about 3.5 years. Unlike REDUCE-AMI it included patients with mildly reduced EF (40–49%), where the benefit is concentrated; like the other trials it was open-label."),
    ('d', "**LVEF 40–49% (4 trials) → 25% relative reduction in death / MI / HF (10.7% vs 14.4%).** The pooled analysis of 1,885 patients with mildly reduced EF from REBOOT, BETAMI, DANBLOCK and CAPITAL-RCT gave HR 0.75 (0.58–0.97). The benefit lies where the ventricle is damaged; it fades as LVEF normalises."),
  ],
  mimic=[
    ("Starting vs stopping", "REDUCE-AMI and REBOOT ask whether to start after a reperfused MI with good LVEF; ABYSS asks whether to stop years later: interruption (LVEF ≥40%, MI a median 2.9 years before) failed non-inferiority (23.8% vs 21.1%), mostly CV admissions, with no quality-of-life gain."),
  ],
  traps=[
    ("“A long-term beta-blocker improves outcome in every post-MI patient”", "Proven long-term benefit is for LVEF ≤40% (I, A in both guidelines) and, from the 2025 pooled data, 40–49%; at LVEF ≥50% REDUCE-AMI and REBOOT show none. The guidelines predate REBOOT: ESC 2023 gives routine beta-blockers regardless of LVEF IIa, and ACC/AHA 2025 still advises starting an oral beta-blocker within 24 hours in all ACS without contraindications (1, A), mainly against reinfarction and arrhythmia, leaving the duration in preserved EF open."),
  ],
  decode=[
    ("[pattern] Reperfused STEMI, LVEF 58%, no HF — does a long-term beta-blocker improve outcome?", "No clear benefit (REDUCE-AMI, REBOOT)."),
    ("[pattern] Post-MI LVEF 45% — beta-blocker?", "Yes: mildly reduced EF benefits (pooled analysis, HR 0.75)."),
  ],
  punch="After a reperfused MI the beta-blocker earns its place when LVEF is below 50% and has no proven benefit when LVEF is preserved; stopping one years later has not been shown to be safe (ABYSS).",
)

L['MI-74'] = dict(
  sub="Cardiology → ACS → Revascularisation, imaging, access and shock (ACC/AHA 2025)",
  step=5,
  intro="Step 5 is what is done to the arteries. No real question is linked; the testable point is that complete revascularisation reverses in shock, and that devices help only in a narrow group.",
  parts=[
    ('a', "**Recommended (I), index or staged; not in cardiogenic shock (culprit-only, CS-36).** Non-culprit lesions in a stable patient cause later MI, so treating them cuts MACE (COMPLETE): Class 1 in selected stable STEMI and in NSTE-ACS without left main disease or a plan for CABG. In shock routine non-culprit PCI at the index procedure is 3: Harm in both, because the extra contrast and time raised death or renal replacement in CULPRIT-SHOCK."),
    ('b', "**Class 1 to guide PCI.** 1, A for stenting the left main or complex lesions: IVUS or OCT shows stent under-expansion and malapposition that angiography misses, the causes of stent thrombosis and restenosis."),
    ('c', "**Radial preferred.** 1, A: fewer bleeds, fewer vascular complications and lower death than femoral, because the radial artery is superficial and compressible (the femoral retroperitoneal bleed is the Top-up)."),
    ('d', "**Reasonable (IIa) in selected patients — DANGER-SHOCK (MI-63).** 2a, B-R in STEMI with severe or refractory LV-dominant shock: DanGer Shock cut 180-day death (45.8% vs 58.5%) but with more bleeding, limb ischaemia and renal failure, and it excluded comatose cardiac-arrest survivors and RV shock."),
    ('e', "**Not recommended (III).** Routine IABP or VA-ECMO is 3: No benefit (IABP-SHOCK II, ECLS-SHOCK: no survival gain). VA-ECMO raises afterload on a failing LV; it is a rescue tool, not routine."),
    ('f', "**Transfer to shock centres (Class 1).** Shock outcomes are better where the team, round-the-clock PCI, mechanical support and cardiac surgery are all available, so the sickest patients are moved to such a hub early. Some guideline summaries (Cleveland Clinic) report this as a Class 1 recommendation, but the classed shock statements in the ACC/AHA 2025 text are about revascularisation and devices; the hub-and-spoke model with early transfer of refractory shock to a Level 1 shock centre comes from the ACC 2025 concise clinical guidance on cardiogenic shock, which carries no class (see FLAGS). The exam answer is still a centre with shock expertise."),
  ],
  mimic=[
    ("Stable multivessel ACS vs multivessel ACS in shock", "Stable: treat all significant lesions, at the index procedure or staged. Shock: culprit only at the index procedure."),
    ("ACC/AHA 2025 vs ESC 2023 classes", "ESC 2023: complete revascularisation is recommended (I) in stable STEMI, at the index PCI or within 45 days, but only ‘should be considered’ (IIa) in NSTE-ACS; intravascular imaging ‘should be considered’ (IIa). ACC/AHA 2025 makes both Class 1."),
  ],
  traps=[
    ("“Complete revascularisation at the index procedure in cardiogenic shock”", "3: Harm (CULPRIT-SHOCK); the notes’ shock table is outdated here (watch line)."),
    ("“Impella for every AMI shock”", "Only selected STEMI LV shock (DanGer criteria), at the price of more complications."),
  ],
  decode=[
    ("[pattern] STEMI in shock, three-vessel disease — what to stent at the index procedure?", "The culprit only."),
    ("[pattern] AMI shock — routine IABP?", "No (3: No benefit, IABP-SHOCK II)."),
  ],
  punch="Treat all significant lesions in the stable patient but only the culprit in shock, image complex lesions, go radial, and reserve a microaxial pump for selected STEMI shock; routine IABP and VA-ECMO bring no survival benefit.",
)

L['MI-75'] = dict(
  sub="Cardiology → ACS → hs-cTn repeat intervals",
  step=1,
  intro="Step 1 is how fast an NSTEMI can be ruled in or out. No real question is linked; the trap is that three sources give three intervals and the stem tells you which one it wants.",
  parts=[
    ('a', "**ESC 2023: 0 h / 1 h (preferred) or 0 h / 2 h — I, B.** A high-sensitivity assay measures troponin in most healthy people, so a small change over an hour separates an evolving infarct from stable chronic injury; assay-specific cut-offs (e.g. a very low hs-cTnT <5 ng/L at 0 h, if pain began more than 3 hours earlier) give rule-in and rule-out at 1 or 2 hours, and an inconclusive result gets a further test at 3 hours."),
    ('b', "**Notes (older ESC): 0 h / 3 h — MI-32.** It used the 99th percentile at presentation and 3 hours; ESC 2023 keeps it only as an alternative where the 1 h or 2 h algorithms are not available, with no class, because it balances safety and speed less well."),
    ('c', "**AHA 2025 ACLS: recheck at 1 h OR 3 h — ACLS-57.** The course algorithm leaves the interval to the local assay; the AHA/ACC chest pain guideline gives 1–3 hours for high-sensitivity and 3–6 hours for conventional troponin."),
  ],
  mimic=[
    ("High-sensitivity vs conventional troponin repeat", "High-sensitivity: 1–2 hours (ESC) or 1–3 hours (AHA/ACC); conventional: 3–6 hours."),
  ],
  traps=[
    ("“ESC recommends 0 h / 3 h” in an ESC-framed question", "ESC 2023 wants 0 h / 1 h or 0 h / 2 h; 3 h is a fallback (watch line)."),
  ],
  decode=[
    ("[pattern] Per ESC 2023, preferred repeat interval for hs-cTn in suspected NSTE-ACS?", "1 hour (0 h / 1 h), or 2 hours (0 h / 2 h)."),
  ],
  punch="ESC 2023 repeats hs-cTn at 1 or 2 hours; the 3-hour schedule survives as a fallback in ESC and in the AHA ACLS algorithm, so answer by the source the stem names.",
)

L['MI-76'] = dict(
  sub="Cardiology → ACS → Lipids, rehabilitation and anaemia (ACC/AHA 2025)",
  step=6,
  intro="Step 6 ends with the long-term prescriptions. No real question is linked; the testable points are the two LDL thresholds with different classes and the haemoglobin of 10.",
  parts=[
    ('a', "**High-intensity statin for all.** 1, A, regardless of baseline LDL-C (atorvastatin 40–80 mg or rosuvastatin 20–40 mg), because the benefit tracks the absolute LDL-C reduction and ACS patients are at the highest risk."),
    ('b', "**LDL-C ≥70 mg/dL → add ezetimibe / PCSK9 inhibitor / inclisiran / bempedoic acid (I).** 1, A on a maximally tolerated statin; each further fall in LDL-C lowers events (IMPROVE-IT, FOURIER, ODYSSEY OUTCOMES)."),
    ('c', "**LDL-C 55–69 mg/dL (IIa).** 2a, B-R. 55 mg/dL (1.4 mmol/L) is the ESC goal, so the American guideline has moved towards it without making it a mandate. The ESC 2025 focused update keeps the goals and adds earlier combination: intensify during the index admission if already treated (I, C); start statin plus ezetimibe in hospital if the goal looks unreachable with statin alone (IIa, B)."),
    ('d', "**Fasting panel at 4–8 weeks after starting or changing therapy.** 1, C-LD: by then the statin effect is complete, so the result decides whether to add a non-statin agent."),
    ('e', "**Refer before discharge (I); home-based if centre unavailable.** Referral before discharge is 1, A, because patients referred later often never attend; home-based rehabilitation is a reasonable alternative (2a)."),
    ('f', "**Transfusion to maintain Hb 10 g/dL may be reasonable.** 2b, B-R in ACS with anaemia and no active bleeding. Anaemia lowers oxygen delivery to an ischaemic myocardium; in MINT, a liberal target (≥10 g/dL) gave fewer 30-day deaths or MIs than restrictive (7–8 g/dL), 14.5% vs 16.9% (RR 1.15 for restrictive, P 0.07), so the difference fell short of significance and the class is only 2b. This is an exception to the general ICU threshold of 7 g/dL, which was never tested in acute MI."),
  ],
  mimic=[
    ("Hb threshold: ACS vs general ICU", "ACS with anaemia: aiming for 10 g/dL may be reasonable (MINT). General ICU: transfuse below 7 g/dL (TRICC)."),
  ],
  traps=[
    ("“LDL-C 60 mg/dL on maximal statin: adding ezetimibe is Class 1”", "55–69 mg/dL is 2a (reasonable); Class 1 begins at ≥70 mg/dL (watch line)."),
    ("“Restrictive transfusion (Hb 7) in acute MI with anaemia”", "ACS is the exception: Hb 10 g/dL may be reasonable."),
  ],
  decode=[
    ("[pattern] Post-ACS on atorvastatin 80 mg, LDL-C 82 mg/dL — next step?", "Add a non-statin agent (1, A)."),
    ("[pattern] NSTEMI, Hb 8.2 g/dL, no bleeding — transfusion target?", "Hb 10 g/dL may be reasonable (2b, MINT)."),
  ],
  punch="High-intensity statin for all, add a non-statin agent at LDL-C ≥70 (Class 1) and consider one at 55–69 (2a), recheck at 4–8 weeks, refer to rehab before discharge, and in ACS anaemia aim for Hb 10, not 7.",
)

FLAGS = {
  'MI-74': "f: ‘Transfer to shock centres (Class 1)’ — disputed. No classed shock-centre transfer recommendation was found in the ACC/AHA 2025 ACS text (writer read sections 8.1–8.2 and 10.1; ACC’s 2025 shock year-in-review attributes early transfer of refractory shock to Level 1 shock centres to the ACC 2025 concise clinical guidance, which has no classes). A Cleveland Clinic summary does call it Class 1, so keep the card’s answer for exams but treat the class as unconfirmed. b: Class 1 (1, A) is for left main or complex lesions, not every PCI.",
  'MI-73': "b: ‘signal at 40–49%’ — the clear 40–49% benefit is from the 2025 pooled analysis (REBOOT contributed part of it); REBOOT alone was neutral overall, with a possible harm signal in women. Minor; the explanation separates the two.",
}
