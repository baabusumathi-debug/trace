# CVS10C — Explain v3 ("Learn" depth): ACS III, reperfusion — initial work-up, oxygen and pain relief, nitrates, early drugs, STEMI time targets and the strategy clock,
# after fibrinolysis, NSTE-ACS risk groups and invasive timing, PCI basics, radial vs femoral, PCI complications, P2Y12 inhibitors, antithrombotic targets, anticoagulation in PPCI,
# the ESC 2023 antithrombotic map, fibrinolytic doses, fibrinolysis recommendations, lysis contraindications, lysis time windows, CABG in ACS.
# No mnemonics or hooks. Driven by qpack/CVS10C.md (38 question links; MI-41 strategy clock asked 10 times, MI-38 nitrates 5, MI-53 lysis contraindications 5, MI-40 and MI-48 three each).
# MI-42, MI-43, MI-44, MI-45, MI-49, MI-51, MI-52 and MI-54 have no linked question and get short explanations with [pattern] decode items.
# No Top-up cards for CVS10C in cvs_topups.json. No `fix` entries for CVS10C in trace/test/data/qbank.json (checked 19 Nov 2026). cvs_cardlayer.json `lines` and `cross` read and used
# (MI-36, 38, 39, 41, 46, 47, 48, 53, 55).
# Checked online on 19 Nov 2026 (ESC 2023 ACS guideline, Byrne et al., Eur Heart J 2023;44:3720 — recommendation text read through a full-text copy and a university lecture deck quoting it):
#  - Oxygen if SaO₂ <90% I C; routine oxygen not recommended if SaO₂ >90% III A; IV opioids IIa C; mild tranquilliser in very anxious patients IIa C; IV beta-blocker (preferably metoprolol)
#    at presentation in PPCI patients without acute HF, SBP >120 mmHg, IIa A. Aspirin LD 150–300 mg oral or 75–250 mg IV (Table 6). Nitrates not in hypotension, marked brady- or tachycardia.
#  - 12-lead ECG at FMC, interpreted ≤10 min, I B. PPCI over lysis if diagnosis-to-PCI <120 min I A; aims <60 min to wire (PCI centre), <90 min (transferred), <10 min to lytic bolus.
#    Lysis within 12 h of symptoms if no contraindication I A; pre-hospital, as soon as possible I A; fibrin-specific agent I B; half-dose tenecteplase ≥75 y IIa B; aspirin + clopidogrel I A
#    (clopidogrel 300 mg, 75 mg if >75 y); anticoagulation until revascularisation (or hospital stay up to 8 days) I A. Transfer to a PCI centre immediately after lysis I A; rescue PCI for
#    failed lysis (<50% ST resolution at 60–90 min, instability, worsening ischaemia, persistent pain) I A; emergency angiography for HF/shock I A; angiography ± PCI of the IRA 2–24 h after
#    successful lysis I A. Late STEMI 12–48 h routine PPCI IIa B.
#  - NSTE-ACS: immediate invasive (<2 h) for very high risk I C; early (<24 h) for high risk IIa A (was I A in 2020); selective approach without high-risk criteria I A.
#    High-risk list: confirmed NSTEMI, dynamic ST/T changes, transient ST elevation, GRACE >140 (also in Ferreira-González et al. appraisal, PMC11012418).
#  - Radial access standard I A; DES over BMS I A; routine thrombus aspiration III A.
#  - UFH bolus 70–100 IU/kg during PCI I C; enoxaparin as alternative in STEMI PPCI IIa A; bivalirudin (full-dose post-PCI infusion) IIa A; fondaparinux in PPCI III B.
#    NSTE-ACS: fondaparinux I B if angiography not anticipated within 24 h; enoxaparin as alternative to UFH if within 24 h IIa B.
#  - P2Y12 pretreatment before PPCI IIb B; routine pretreatment in NSTE-ACS (early invasive) III A; pretreatment if invasive >24 h IIb C. Prasugrel over ticagrelor for PCI IIa B.
#    GP IIb/IIIa for no-reflow or thrombotic complication IIa C; GP IIb/IIIa pretreatment III A; cangrelor in P2Y12-naive patients IIb A. DAPT 12 months default I A. Prior stroke = prasugrel CI.
#  - Emergency CABG for ACS-related shock when PCI of the IRA is not feasible/unsuccessful I B; resume DAPT ≥12 months after CABG I C.
#  - ACC/AHA 2025 ACS guideline (Rao et al., Circulation/JACC Feb 2025), from summaries (Hendrick Health “at a glance”, Medical Dialogues, Cardioteca): prasugrel or ticagrelor preferred
#    over clopidogrel for PCI (1); DAPT ≥12 months if not high bleeding risk (1); ticagrelor monotherapy from ≥1 month after PCI (1); radial preferred; ECG within 10 min of FMC; FMC-to-device
#    <90 min; lysis if PCI not possible within 120 min; angiography 2–24 h after successful lysis; oxygen only if SpO₂ <90%; invasive strategy during admission for intermediate/high risk.
# Could not open: the ESC full text on academic.oup.com and the ACC/AHA full text on ahajournals.org / jacc.org (blocked or failed). From standard references without a fresh check
# (confident unless said): ACC/AHA door-to-needle ≤30 min, door-in–door-out ≤30 min, aspirin 162–325 mg chewed; ACC/AHA 2013 absolute/relative lysis contraindication lists (ischaemic stroke
# <3 months, closed head trauma <3 months, intracranial surgery <2 months absolute; major surgery <3 weeks, CPR >10 min relative); ESC 2017 lysis contraindication table (matches card);
# fibrinolytic doses (SK 1.5 MU over 30–60 min; accelerated alteplase 15 mg + 0.75 mg/kg max 50 + 0.5 mg/kg max 35; reteplase 10 + 10 U 30 min apart; tenecteplase 30–50 mg by weight);
# STREAM-2 (half-dose TNK ≥60 y); DETO2X-AMI (n 6,629, 1-year death 5.0 vs 5.1%); AVOID; COMMIT (early IV metoprolol: more cardiogenic shock); METOCARD-CNIC; IMPRESSION (morphine delays
# ticagrelor absorption); PLATO dyspnoea ~14% vs ~8%; TRITON-TIMI 38 (prior stroke/TIA net harm with prasugrel); ACCOAST; ISAR-REACT 5 (1-year death/MI/stroke 6.9 vs 9.3%); OASIS-5
# (major bleeding ~2.2 vs 4.1%, catheter thrombosis → UFH bolus at PCI); TASTE, TOTAL (more stroke with aspiration); MATRIX, RIVAL, RIFLE-STEACS (cardiac mortality 5.2 vs 9.2%); BRIDGE
# (cangrelor bridging); ACC/AHA 2021 revascularisation (stop clopidogrel/ticagrelor ≥24 h before urgent CABG); P2Y12 elective holds 3/5/7 days; riociguat–nitrate contraindication.

# Independent review 19 Nov 2026: ACC/AHA 2025 full text read (Tables 7, 13, 14; sections 5.3, 5.3.2, 6): aspirin LD 162–325 mg; FMC-to-device ≤90 / ≤120 min transfer;
#   no door-to-needle figure stated (≤30 min is 2013 ACCF/AHA); lysis contraindications and fibrinolytic doses as 2013; ESC 2017 STEMI text: re-occlusion I B, bivalirudin in HIT I C, half-dose TNK ≥75.
#   Trials checked: RIFLE-STEACS (ACC summary), ATOLL (ESC press release), TREAT (ACC summary), STREAM elderly ICH analysis.

SPINE = [
  ("First minutes: ECG, monitor, relieve", "Get a 12-lead ECG read within 10 minutes, keep a defibrillator at hand because early deaths are from VF, give oxygen only to the hypoxaemic, and use nitrates and opioids only for symptoms, never as proof of the diagnosis."),
  ("The reperfusion clock decides", "If the wire can cross within 120 minutes of diagnosis do primary PCI; if not, lyse within 10 minutes and send the patient on to a PCI centre anyway."),
  ("Fibrinolysis: drug, limits, follow-through", "Use a fibrin-specific agent within 12 hours of symptoms, halve tenecteplase over 75, pair it with aspirin and clopidogrel, check bleeding contraindications first, and judge success at 60–90 minutes: rescue PCI if it failed, angiography at 2–24 hours if it worked."),
  ("NSTE-ACS: timing by risk", "Without ST elevation the question is not whether to reperfuse now but how fast to do angiography: under 2 hours if very high risk, under 24 hours if high risk, otherwise during the admission or selectively."),
  ("PCI: the procedure and its harms", "Primary PCI is radial access, a drug-eluting stent in the culprit artery and no routine thrombus aspiration; its complications are local, coronary and contrast-related, and femoral access adds the retroperitoneal bleed."),
  ("Antithrombotics and surgery", "Each drug hits one step of clotting; UFH covers the procedure, prasugrel or ticagrelor with aspirin covers the next 12 months, and before CABG the long-acting P2Y12 blocker is the drug to stop."),
]

PRIMER = "An acute coronary syndrome is a ruptured or eroded plaque with thrombus on it; when the thrombus occludes the artery the ECG shows ST elevation (STEMI) and myocardium dies from the endocardium outwards over hours, so every minute to reopening counts. Reperfusion is either mechanical (primary PCI, a wire and stent across the clot) or pharmacological (fibrinolysis, a plasminogen activator dissolving the fibrin). A clot has two parts that need two kinds of drug: platelets (aspirin, P2Y12 inhibitors, GP IIb/IIIa inhibitors) and fibrin from the coagulation cascade (heparins, bivalirudin, fondaparinux). Without ST elevation (NSTE-ACS) the artery is usually not fully occluded, and the decision is how soon to take the patient for angiography. CVS10A and CVS10B covered definitions, ECG and biomarkers; this deck is treatment."

L = {}

L['MI-36'] = dict(
  sub="Cardiology → ACS → Initial work-up",
  step=1,
  intro="Step 1 starts at first medical contact. The ECG decides which pathway the patient enters, and the monitor is there because the first hour is when he is most likely to die. The one real question asks what kills STEMI patients before they reach hospital.",
  parts=[
    ('a', "**12-lead ECG interpreted within 10 minutes.** ESC 2023 makes this Class I (B) at the point of first medical contact, and both ESC and ACC/AHA use the same 10-minute target. The ECG is what separates STEMI (go to reperfusion, MI-40) from NSTE-ACS (risk-stratify, MI-43); troponin is never awaited for a STEMI decision."),
    ('b', "**Continuous ECG monitoring with a defibrillator available, because of the risk of VT/VF.** Acute ischaemia makes the border zone electrically unstable (re-entry around dying tissue, raised automaticity, potassium leak). Most early STEMI deaths, within the first 24 hours and mostly in the first hour, are from ventricular fibrillation, often before the patient reaches hospital. That is why transport from first contact must be defibrillator-capable."),
    ('c', "**Cardiac biomarkers, haemogram, electrolytes, lipid profile, renal and liver function, HbA1c if diabetic.** Troponin (high-sensitivity, on the 0/1 h or 0/2 h algorithm) makes the NSTEMI diagnosis; the haemoglobin and platelets set bleeding risk before antithrombotics; potassium and magnesium matter for arrhythmia; creatinine sets drug doses and contrast risk; the lipid profile is most accurate when drawn early."),
  ],
  mimic=[
    ("Early death in STEMI vs later death", "First hours: VF (electrical). Days later: pump failure and mechanical complications (free wall rupture, VSD, papillary muscle rupture)."),
  ],
  traps=[
    ("“Most prehospital STEMI deaths are from cardiogenic shock or rupture”", "They are from VF, mostly in the first hour; shock and rupture kill later."),
  ],
  decode=[
    ("Commonest cause of prehospital death in STEMI? [Marrow]", "Ventricular fibrillation."),
    ("Within what time must the first ECG be read after first medical contact? [pattern]", "10 minutes."),
  ],
  punch="Read the ECG within 10 minutes, because it chooses the pathway, and keep a defibrillator beside the patient, because the first hour of STEMI kills by VF.",
)

L['MI-37'] = dict(
  sub="Cardiology → ACS → Oxygen and symptom relief",
  step=1,
  intro="Still in step 1: treating symptoms without harming the patient. One real question tests the oxygen threshold, which one in three got wrong by reflexively giving oxygen to a patient who was not hypoxaemic.",
  parts=[
    ('a', "**Oxygen if SaO₂ <90% or PaO₂ <60 mmHg: Class I, C.** Below 90% the oxyhaemoglobin curve is on its steep part, so oxygen delivery to ischaemic myocardium falls quickly and correcting it helps."),
    ('b', "**SaO₂ ≥90%: routine oxygen not recommended, Class III, A (no benefit).** Hyperoxia constricts coronary arteries and raises reactive oxygen species. DETO2X-AMI (about 6,600 patients with SpO₂ ≥90%) found no difference in 1-year death (5.0% vs 5.1%), and AVOID suggested larger infarcts with oxygen. The ESC text says SaO₂ >90%; the card’s ≥90% is the same rule in practice."),
    ('c', "**IV morphine 5–10 mg, titrated IV opioids Class IIa, C; they cut sympathetic drive and oxygen consumption.** Pain drives catecholamines, heart rate and myocardial oxygen demand. The catch: opioids slow gastric emptying, so oral P2Y12 inhibitors are absorbed later and platelet inhibition is delayed (shown with ticagrelor in IMPRESSION). That is why opioids are only IIa and should be titrated, not given routinely."),
    ('d', "**A mild tranquilliser, usually a benzodiazepine, in very anxious patients: Class IIa, C.** The aim is the same as with opioids: lower sympathetic tone."),
  ],
  mimic=[
    ("SaO₂ <90% vs ≥90%", "The same number flips the class: below it oxygen is Class I, at or above it oxygen is Class III."),
  ],
  traps=[
    ("“Low-flow nasal oxygen at 2 L/min is harmless at SaO₂ 95%”", "Any routine oxygen without hypoxaemia is Class III; the DocT key is to withhold it (66% right)."),
    ("“Morphine is a Class I part of the ACS bundle”", "It is IIa and delays oral P2Y12 absorption."),
  ],
  decode=[
    ("ACS patient, SaO₂ 95% — which oxygen strategy? [DocT GT]", "Withhold oxygen."),
    ("Below what saturation is oxygen indicated in ACS? [pattern]", "SaO₂ <90% (PaO₂ <60 mmHg)."),
  ],
  punch="Oxygen only below 90%; above that it adds nothing and may harm. Opioids and benzodiazepines are IIa, and opioids slow the oral P2Y12 load.",
)

L['MI-38'] = dict(
  sub="Cardiology → ACS → Nitrates",
  step=1,
  intro="Step 1 again: nitrates relieve ischaemic pain but can collapse the circulation in the wrong patient, and their effect proves nothing about the diagnosis. Five real questions test exactly these two points, and both DocT questions were got right by fewer than half.",
  parts=[
    ('a', "**0.4 mg (0.3–0.6 mg) sublingual, every 5 minutes, up to 3 doses.** Glyceryl trinitrate releases nitric oxide, raising cGMP in vascular smooth muscle; at low doses it is mainly a venodilator, so it lowers preload and wall tension (less oxygen demand), and it also dilates epicardial coronaries and collaterals. The notes’ ‘5 mg’ is a source error (card watch line)."),
    ('b', "**Hypotension, tachycardia, right ventricular MI, recent phosphodiesterase-inhibitor use.** Each of these turns preload reduction into shock. An RV infarct is preload-dependent: the failing RV needs a high filling pressure to push blood through the lungs, so venodilation drops LV filling and the pressure falls (give fluid instead). PDE-5 inhibitors (sildenafil, vardenafil within 24 h; tadalafil within 48 h) block cGMP breakdown, so a nitrate causes profound hypotension; riociguat, a soluble guanylate cyclase stimulator, acts on the same pathway and is also a contraindication. ESC adds marked bradycardia, and ACC/AHA use SBP <90 mmHg (or ≥30 below baseline) and HR <50 or >100."),
    ('c', "**Nothing: relief does not confirm or exclude MI; biomarkers are needed.** Nitrates relax all smooth muscle, so oesophageal spasm also eases, and an MI may improve partly. The diagnosis comes from the ECG and serial high-sensitivity troponin."),
  ],
  mimic=[
    ("Nitrate in hypertensive acute heart failure vs nitrate in RV infarct", "Lowering preload rescues the congested LV in hypertensive AHF; it collapses the preload-dependent RV infarct."),
    ("Unstable angina vs oesophageal spasm with a normal ECG and negative troponin", "Until serial hs-troponin and risk stratification rule out ACS, unstable angina is the working diagnosis; spasm is a diagnosis of exclusion."),
  ],
  traps=[
    ("“Hypotension 10 minutes after nitroglycerin in inferior STEMI is a medication reaction”", "46% chose this. The nitrate unmasked a preload-dependent RV infarct: it is cardiogenic shock (key B). Check right-sided leads (V4R) before nitrates in inferior STEMI."),
    ("“Chest pain relieved by nitroglycerin, normal ECG, negative troponin → oesophageal spasm”", "DocT keys spasm (33% right), but the key is debatable: nitrate relief proves nothing, and with a single negative troponin unstable angina is the classic answer. If the stem says serial troponins are negative and ACS is ruled out, pick spasm; otherwise pick unstable angina."),
    ("“Hypotension after a nitrate is only a PDE-5 inhibitor problem”", "Riociguat (sGC stimulator) does the same; Marrow keys it."),
  ],
  decode=[
    ("Inferior STEMI, aspirin + nitroglycerin + morphine, BP falls to 60/30 in 10 min — why? [DocT QBank]", "Cardiogenic shock from an RV infarct unmasked by preload reduction."),
    ("Inferior STEMI, hypotension, clear lungs, normal LV — next step? [Marrow]", "Normal saline bolus; no nitrates."),
    ("Hypotension after SL nitrate — which drug interacted? [Marrow]", "Riociguat."),
    ("Chest pain relieved by nitroglycerin, normal ECG, negative troponin — most likely? [DocT QBank]", "Keyed oesophageal spasm; the defensible answer is unstable angina until serial troponins rule out ACS."),
  ],
  punch="A nitrate lowers preload, so it is dangerous wherever preload is holding the pressure up: hypotension, RV infarct, and any drug that already floods the NO–cGMP pathway. Whether it relieves the pain tells you nothing.",
)

L['MI-39'] = dict(
  sub="Cardiology → ACS → Early drugs",
  step=1,
  intro="The last part of step 1 is the drugs given on arrival, before the reperfusion decision. The one real question tests the contraindications to an IV beta-blocker, which are wider than the card lists.",
  parts=[
    ('a', "**Aspirin 300 mg on arrival.** Aspirin acetylates platelet COX-1 irreversibly, so thromboxane A2 production stops for the life of the platelet; a loading dose works within minutes, faster still when chewed. ESC 2023 gives 150–300 mg oral (75–250 mg IV); ACC/AHA use 162–325 mg chewed. Both are right in their own system."),
    ('b', "**A P2Y12 inhibitor loading dose: prasugrel, ticagrelor or clopidogrel.** Aspirin blocks only one platelet activation pathway; ADP acting on P2Y12 is the other main amplifier, so the two together (DAPT) are needed. Timing of this load is a separate question (MI-50: routine pretreatment is not recommended in NSTE-ACS)."),
    ('c', "**High-dose statin: atorvastatin 80 mg.** High-intensity statin is started early regardless of cholesterol (Class I); the benefit is plaque stabilisation and LDL lowering, and early starting improves long-term adherence."),
    ('d', "**Tachycardia with SBP >120 mmHg: IV metoprolol (limits infarct size); avoid in heart failure and hypotension.** Slowing the heart lowers oxygen demand and lengthens diastole, so less myocardium dies (METOCARD-CNIC, before primary PCI); ESC 2023 gives it IIa A in PPCI patients without acute heart failure and with SBP >120. The danger is a patient whose output depends on his heart rate: in COMMIT early IV metoprolol caused excess cardiogenic shock, mostly in the first day and in those with heart failure, low pressure or tachycardia. Contraindications therefore go beyond the card: signs of HF or low output, risk of shock (age >70, HR >110, SBP <120), PR >240 ms or second/third-degree block, and active asthma or bronchospasm."),
  ],
  mimic=[
    ("Tachycardia from ischaemia and pain vs compensatory tachycardia of low output", "The first is a target for a beta-blocker; the second is what keeps a failing heart’s output up, and blocking it causes shock (COMMIT)."),
  ],
  traps=[
    ("“The only contraindications to an IV beta-blocker in STEMI are heart failure and hypotension”", "Heart block (PR >240 ms, second/third degree), bronchospasm and high shock risk are also contraindications; Marrow’s ‘all except’ question keys ‘none of the above’."),
  ],
  decode=[
    ("Contraindications to a beta-blocker in STEMI — all of the following except? [Marrow]", "None of the above: HF/low LVEF, heart block, hypotension and asthma all count."),
    ("Aspirin loading dose in ACS (ESC)? [pattern]", "150–300 mg oral; ACC/AHA 162–325 mg chewed."),
  ],
  punch="Aspirin, a P2Y12 load and a high-dose statin go in early for everyone; an IV beta-blocker only for a tachycardic, normotensive patient with no failure, no block and no bronchospasm.",
)

L['MI-40'] = dict(
  sub="Cardiology → ACS → STEMI time targets",
  step=2,
  intro="Step 2 is the clock that decides reperfusion. Myocardium is lost with every minute of occlusion, and three real questions turn on one number: whether the wire can cross within 120 minutes of diagnosis.",
  parts=[
    ('a', "**FMC → ECG and diagnosis: ≤10 minutes.** The clock for reperfusion starts at diagnosis, so delay here pushes everything else."),
    ('b', "**Diagnosis → wire: choose PPCI over lysis if achievable within ≤120 minutes.** Primary PCI opens about 90% of arteries and has less intracranial bleeding than lysis, but its advantage is lost if it comes too late; 120 minutes is the delay at which lysis given now is roughly as good. This is a decision threshold (Class I, A), not a target."),
    ('c', "**Diagnosis → wire at a PCI centre: ≤60 minutes.**"),
    ('d', "**Diagnosis → wire, transferred: ≤90 minutes.** Transfer adds time, so the target is looser; the targets are what a system should achieve, not cut-offs for choosing."),
    ('e', "**Diagnosis → lytic bolus: ≤10 minutes.** If lysis is chosen, its benefit falls steeply with time, so it must not wait (ideally pre-hospital, MI-52). In the American system the 2025 ACC/AHA ACS guideline sets FMC-to-device ≤90 minutes (≤120 minutes with transfer) and lysis when PCI will take more than 120 minutes; its door-to-needle goal of ≤30 minutes comes from the 2013 ACCF/AHA STEMI guideline and the AHA ACS algorithm."),
    ('f', "**Lysis → evaluation of efficacy: 60–90 minutes.** By then a successful lysis has resolved ST elevation by ≥50%."),
    ('g', "**Lysis → angiography: 2–24 hours.** This is the routine angiography after successful lysis (MI-42)."),
  ],
  table=dict(title="Which number answers which question", head=["Number", "Meaning"], rows=[["10 min", "FMC → ECG; diagnosis → lytic bolus"], ["**120 min**", "**the choice**: PPCI if the wire can cross by then, otherwise lyse"], ["60 min", "target at a PCI centre"], ["90 min", "target if transferred"], ["60–90 min", "judge lysis"], ["2–24 h", "angiography after successful lysis"]]),
  mimic=[
    ("120 min vs 90 min", "120 is the decision threshold between PPCI and lysis; 90 is the target for transferred patients."),
  ],
  traps=[
    ("“Transfer for PCI regardless of delay” with an expected 160-minute delay", "Beyond 120 minutes lyse first (77% right); PCI follows anyway."),
    ("“Thrombolysis” in a STEMI at a PCI-capable centre", "When PCI is available within 120 minutes it beats lysis; the 95%-right question keys primary PCI."),
  ],
  decode=[
    ("Anterior STEMI, door-to-balloon expected 160 min — best initial management? [DocT QBank]", "Immediate thrombolysis before transfer."),
    ("Inferior or anterior STEMI, troponin up, no delay mentioned — treatment? [DocT QBank]", "Immediate primary PCI."),
  ],
  punch="Ask one question at diagnosis: can the wire cross within 120 minutes? If yes, primary PCI (aim 60 or 90 minutes); if no, lytic bolus within 10 minutes.",
)

L['MI-41'] = dict(
  sub="Cardiology → ACS → Strategy clock",
  step=2,
  intro="Step 2 as a flow chart. This is the most asked card in the deck (ten real questions): almost all are the same decision, PPCI if timely and lysis if not, plus two on stent thrombosis, which is a STEMI and goes to the lab.",
  parts=[
    ('a', "**Time to PCI?** The first and only decision after a STEMI diagnosis is whether the wire can cross within 120 minutes (MI-40). Distance, transport and lab availability all feed into it."),
    ('b', "**Primary PCI: alert and transfer to a PCI centre; wire crossing by 90 minutes.** Bypassing the emergency department and taking the patient straight to the lab saves time; at a PCI centre the aim is 60 minutes."),
    ('c', "**Fibrinolysis: bolus within 10 minutes, then transfer to a PCI centre.** Lysis is a bridge, not the end of treatment: every lysed patient is moved to a PCI centre immediately (ESC Class I, A), because a third or more fail to reperfuse and some re-occlude."),
    ('d', "**At 60–90 minutes: reperfusion criteria met? No → rescue PCI.** Failure means less than 50% ST resolution, ongoing pain, or haemodynamic or electrical instability (MI-42). A second dose of lytic does not help."),
    ('e', "**Yes → routine PCI strategy at 2–24 hours.** The lysed artery still sits on a ruptured plaque with residual stenosis; angiography within 2–24 hours lowers re-infarction without the bleeding of immediate PCI on a fully lytic state."),
  ],
  mimic=[
    ("Stent thrombosis vs post-PCI pain without new ST change", "New ST elevation in the stented territory is stent thrombosis, a STEMI: back to the lab. Pain with an unchanged ECG gives time for other causes."),
    ("Rescue PCI vs routine PCI after lysis", "Rescue: lysis failed, go now. Routine: lysis worked, go at 2–24 hours."),
  ],
  traps=[
    ("“Immediate transfer for primary PCI” when the PCI centre is 150 km or 4 hours away", "The delay is well over 120 minutes: lyse, then transfer (NEET 2025, Marrow)."),
    ("“Intravenous nitroglycerin, observation or echo first” for new ST elevation after a stent", "Only 48% chose repeat angiography. Acute stent thrombosis is a STEMI; anything else delays reperfusion."),
    ("“Thrombolysis” for stent thrombosis", "Platelet-rich stent thrombus responds poorly to lysis; load DAPT, anticoagulate and do urgent PCI (NEET 2025)."),
    ("Marrow’s ‘PCI at 3–24 h’ after lysis", "Its explanation says 3–24 h; ESC says 2–24 h. The answer, lysis then transfer, is unaffected."),
  ],
  decode=[
    ("STEMI, PCI centre 150 km away (or 4 h, or door-to-balloon 160 min) — next step? [NEET 2025] [Marrow] [DocT GT]", "Thrombolysis, then transfer to a PCI centre."),
    ("STEMI with PCI available — most appropriate treatment? [DocT QBank]", "Primary PCI."),
    ("DES 2 months ago, sudden anterior ST elevation — immediate management? [NEET 2025]", "DAPT with urgent PCI."),
    ("New chest pain and ST elevation hours after a successful circumflex stent — next step? [DocT GT]", "Urgent repeat coronary angiography."),
  ],
  punch="One decision: PCI within 120 minutes, or lyse within 10 and transfer. After lysis, failure means rescue PCI now and success means angiography at 2–24 hours; stent thrombosis is a STEMI and goes straight back to the lab.",
)

L['MI-42'] = dict(
  sub="Cardiology → ACS → After fibrinolysis",
  step=3,
  intro="Step 3 follows the lysed patient. Lysis never ends the treatment; what happens next depends on how the patient looks at 60–90 minutes. No real question is linked, but the branches are the same ones MI-41 tests.",
  parts=[
    ('a', "**HF or shock: emergency angiography ± PCI, Class I, A.** Shock after lysis means a large area is still ischaemic or a mechanical complication is present; only opening the artery or fixing the defect helps."),
    ('b', "**Failed lysis: rescue PCI immediately — <50% ST resolution at 60–90 minutes, or instability, or worsening ischaemia; Class I, A.** ST resolution is a bedside marker of tissue reperfusion; under 50% means the artery is probably still shut."),
    ('c', "**Successful lysis: angiography ± PCI of the infarct-related artery at 2–24 hours, Class I, A.** The plaque and residual stenosis are still there."),
    ('d', "**Recurrent ischaemia or re-occlusion: emergency angiography ± PCI, Class I, B.**"),
    ('e', "**Watchful waiting after lysis raises re-infarction; routine PCI after lysis reduces it.** Trials of early routine angiography after lysis against an ischaemia-guided approach (such as CARESS-in-AMI and TRANSFER-AMI) found less re-infarction and recurrent ischaemia, without more bleeding."),
  ],
  mimic=[
    ("Rescue PCI vs facilitated PCI", "Rescue is for failed lysis. Immediate PCI on top of successful lysis (facilitated PCI) is not recommended: more bleeding, no benefit."),
  ],
  traps=[
    ("“Successful lysis needs no angiography”", "Watchful waiting raises re-infarction; angiography at 2–24 hours is Class I."),
  ],
  decode=[
    ("Lysed anterior STEMI, ST resolution 30% at 90 min — next step? [pattern]", "Immediate rescue PCI."),
    ("Lysed STEMI, ST resolved, pain-free — when angiography? [pattern]", "Within 2–24 hours."),
  ],
  punch="After lysis, failure or shock means the lab now, success means the lab in 2–24 hours; nobody is simply watched.",
)

L['MI-43'] = dict(
  sub="Cardiology → ACS → NSTE-ACS risk groups",
  step=4,
  intro="Step 4 changes the question: without ST elevation the artery is usually not fully closed, so the decision is how fast to do angiography, and risk sets the speed. No real question is linked; the class change in ESC 2023 is the likely target.",
  parts=[
    ('a', "**Very high risk: haemodynamic instability or cardiogenic shock, recurrent or refractory chest pain, acute HF from ongoing ischaemia, life-threatening arrhythmia or arrest after presentation, mechanical complications, recurrent dynamic ECG changes.** Each means myocardium is dying now or the patient may not survive the wait, so these behave like a STEMI."),
    ('b', "**High risk: confirmed NSTEMI (ESC algorithms), GRACE >140, transient ST elevation, dynamic ST/T changes.** A rising troponin or a changing ECG marks an active thrombus."),
    ('c', "**Very high risk: immediate transfer and invasive strategy (<2 hours).** Class I, C."),
    ('d', "**High risk: early (<24 hours) invasive strategy, IIa.** ESC 2023 downgraded this from I (2020) to IIa, A, because trials of early versus delayed angiography showed no mortality benefit overall (benefit only in subgroups such as GRACE >140)."),
    ('e', "**Non-high risk: selective or inpatient invasive strategy, Class I.** The Class I recommendation is to do angiography during the admission (or selectively after non-invasive testing), not within 24 hours. ACC/AHA 2025 similarly recommend an invasive approach during the admission for intermediate- and high-risk patients."),
  ],
  mimic=[
    ("Very high-risk NSTE-ACS vs STEMI", "Both go to the lab within 2 hours; but lysis is never used in NSTE-ACS, because the artery is not occluded and lysis adds bleeding without benefit."),
  ],
  traps=[
    ("“Early invasive strategy within 24 hours is Class I in high-risk NSTE-ACS”", "It is IIa in ESC 2023; the Class I is for an invasive strategy during the admission."),
  ],
  decode=[
    ("NSTEMI with refractory pain and hypotension despite treatment — timing of angiography? [pattern]", "Immediate, within 2 hours."),
    ("Stable NSTEMI with rising troponin, GRACE 150 — timing? [pattern]", "Early, within 24 hours (IIa)."),
  ],
  punch="In NSTE-ACS, risk sets the clock: very high risk under 2 hours (I), high risk under 24 hours (only IIa now), everyone else during the admission or selectively.",
)

L['MI-44'] = dict(
  sub="Cardiology → ACS → PCI basics",
  step=5,
  intro="Step 5 opens the lab. No real question is linked to this card; what is asked about PCI is the stent type and that thrombus aspiration is no longer routine.",
  parts=[
    ('a', "**Restore perfusion by balloon angioplasty or stenting.**"),
    ('b', "**Access → angiogram (culprit vessel) → intervention (stent, balloon, aspiration if needed) → periprocedural drugs.** The culprit is identified from the ECG territory and the angiographic appearance (occlusion, thrombus, ruptured plaque)."),
    ('c', "**Drug-eluting stent: less thrombosis and restenosis than bare-metal.** The drug (an antiproliferative such as everolimus or zotarolimus) suppresses the neointimal growth that causes restenosis; current DES also have lower stent thrombosis than bare-metal stents. ESC 2023: DES in preference to bare-metal in all cases, Class I, A."),
    ('d', "**Not routine; selectively for large clot burden.** Routine thrombus aspiration is Class III, A: TASTE and TOTAL showed no mortality benefit, and TOTAL found more stroke, probably from thrombus dislodged into the aorta."),
    ('e', "**No absolute contraindication; relative: renal dysfunction (contrast), active infection, high bleeding risk, contrast allergy.** In a STEMI the benefit of opening the artery outweighs these; they change preparation (hydration, steroid premedication, radial access), not the decision."),
  ],
  mimic=[
    ("Restenosis vs stent thrombosis", "Restenosis is gradual neointimal growth over months, with recurrent angina; stent thrombosis is sudden occlusion, usually in the first 30 days, presenting as STEMI."),
  ],
  traps=[
    ("“Thrombus aspiration is routine in primary PCI”", "Class III, A; selective use only."),
  ],
  decode=[
    ("Which stent is recommended in primary PCI? [pattern]", "Drug-eluting stent, in all cases (I, A)."),
  ],
  punch="Primary PCI means a drug-eluting stent in the culprit, no routine aspiration, and no absolute contraindication.",
)

L['MI-45'] = dict(
  sub="Cardiology → ACS → Radial vs femoral",
  step=5,
  intro="Still in step 5: where the catheter goes in. No real question is linked, but the femoral bleeding questions on MI-46 are the other side of this card.",
  parts=[
    ('a', "**Bleeding, vascular complications (pseudoaneurysm), need for transfusion; better overall survival.** The radial artery is superficial and compressible over bone, and a bleed there cannot track into the retroperitoneum; in ACS patients loaded with antithrombotics, access-site bleeding is the main avoidable bleed, and bleeding itself raises mortality. ESC 2023: radial access is the standard, Class I, A."),
    ('b', "**MATRIX.** MATRIX (about 8,400 ACS patients) found fewer major bleeds and transfusions with radial access, and also lower all-cause mortality."),
    ('c', "**RIVAL and RIFLE-STEACS.** RIVAL’s overall primary outcome was neutral, with fewer vascular complications and a benefit in the STEMI subgroup; RIFLE-STEACS (STEMI) found lower cardiac mortality (about 5% vs 9%), less bleeding and a shorter hospital stay, which is the cost benefit."),
    ('d', "**Only when radial is not feasible; higher complication risk.** Examples are a poor radial pulse, need for large-bore devices or mechanical support, or a failed radial attempt."),
  ],
  mimic=[
    ("Radial complication vs femoral complication", "Radial: artery occlusion, spasm, small haematoma. Femoral: retroperitoneal bleed, pseudoaneurysm, AV fistula."),
  ],
  traps=[
    ("“Radial access only reduces bleeding, not death”", "MATRIX and RIFLE-STEACS both showed lower mortality."),
  ],
  decode=[
    ("Preferred access for PCI in ACS, and the trial behind it? [pattern]", "Radial (I, A); MATRIX."),
  ],
  punch="Radial access is the standard because ACS patients are fully anticoagulated and a compressible artery cannot bleed into the retroperitoneum; femoral is for when radial cannot be done.",
)

L['MI-46'] = dict(
  sub="Cardiology → ACS → PCI complications",
  step=5,
  intro="Step 5 ends with what goes wrong after PCI. The one real question is the retroperitoneal bleed, and the card layer adds how to tell it from tamponade and stent thrombosis.",
  parts=[
    ('a', "**Local: bleeding, haematoma, infection, pseudoaneurysm, compartment syndrome.** A femoral puncture above the inguinal ligament cannot be compressed against the femoral head, so blood tracks into the retroperitoneum: back or flank pain and hypotension with little groin swelling. Diagnose with non-contrast CT; radial access avoids it."),
    ('b', "**Coronary: dissection, embolism, spasm.** A wire or balloon can dissect or perforate the coronary; a perforation fills the pericardium and causes tamponade, sometimes hours later."),
    ('c', "**Contrast: contrast nephropathy, allergic reaction, CHF.** Contrast is a volume and osmotic load (heart failure) and damages the renal medulla; hydration and limiting volume are the prevention."),
    ('d', "**Others: access-vessel dissection, stroke, death.** Catheters crossing the aortic arch can dislodge atheroma or thrombus to the brain."),
  ],
  table=dict(title="Hypotension after PCI: reading the stem", head=["Clue", "Diagnosis", "First test"], rows=[["Femoral access, back/flank pain, little groin swelling", "**retroperitoneal haematoma**", "non-contrast CT"], ["Radial access, no new ECG change", "**tamponade** from coronary or wire perforation", "bedside echo"], ["New ST elevation in the stented territory", "**stent thrombosis**", "repeat angiography"]]),
  mimic=[
    ("Retroperitoneal haematoma vs groin haematoma", "A groin haematoma is visible and compressible; a retroperitoneal bleed shows only as pain and shock."),
  ],
  traps=[
    ("“Retroperitoneal bleed” after a radial PCI", "It belongs to femoral access; after a radial case think tamponade."),
  ],
  decode=[
    ("2 h after femoral catheterisation: hypotension and back pain — diagnosis? [Marrow]", "Retroperitoneal bleeding."),
    ("Hypotension hours after an uncomplicated radial PCI, ECG unchanged — first test? [pattern]", "Bedside echo for tamponade."),
  ],
  punch="Shock after PCI has three main answers: retroperitoneal bleed if femoral, tamponade if a coronary was perforated, stent thrombosis if the ST segments rise again.",
)

L['MI-47'] = dict(
  sub="Cardiology → ACS → P2Y12 inhibitors",
  step=6,
  intro="Step 6 begins with the second antiplatelet. Two real questions test the drugs’ side effects and contraindications, and both were got right by less than half: ticagrelor dyspnoea (30%) and prasugrel after TIA (49%).",
  parts=[
    ('a', "**Clopidogrel and prasugrel; ticagrelor is NOT — a reversible, direct-acting agent (cyclopentyl-triazolopyrimidine).** Thienopyridines are prodrugs whose active metabolite binds P2Y12 irreversibly, so their effect lasts the platelet’s life. Clopidogrel needs two CYP steps (CYP2C19), so its effect is slow and variable; prasugrel needs one, so it is faster and stronger. Ticagrelor is active itself and binds reversibly, so its effect wears off in 3–5 days."),
    ('b', "**Prasugrel or ticagrelor over clopidogrel (superior efficacy); clopidogrel if unavailable or contraindicated.** TRITON-TIMI 38 and PLATO showed fewer ischaemic events (PLATO also lower mortality), at the cost of more bleeding. Clopidogrel remains the drug with lysis (MI-52) and with oral anticoagulants."),
    ('c', "**Prior stroke or TIA; avoid in older patients.** In TRITON-TIMI 38 patients with prior stroke or TIA had net harm, with more intracranial bleeding. At 75 years or more, or under 60 kg, prasugrel is generally not recommended; if used, the maintenance dose is 5 mg."),
    ('d', "**Prior haemorrhagic stroke; liver disease.** Ticagrelor is contraindicated after any intracranial haemorrhage; it is cleared by hepatic CYP3A4, so the label contraindicates severe hepatic impairment and ESC advises against it (and prasugrel) in moderate-to-severe liver disease. Its other effects come from blocking adenosine reuptake (ENT1): dyspnoea in about 14% in PLATO (vs about 8% with clopidogrel), with normal saturation, examination, ECG and CT, usually mild and self-limiting; and ventricular pauses."),
  ],
  mimic=[
    ("Ticagrelor dyspnoea vs pulmonary embolism or heart failure after MI", "Ticagrelor dyspnoea has normal SpO₂, examination, ECG and imaging, and follows the drug; PE and HF do not."),
  ],
  traps=[
    ("“Aspirin or metoprolol causes the dyspnoea” 12 hours after PCI with normal SpO₂, exam, ECG and CT", "Only 30% chose ticagrelor; the adenosine effect is the cause."),
    ("“Clopidogrel, ticagrelor or cangrelor is contraindicated after a TIA”", "Only prasugrel is (49% right)."),
    ("“Ticagrelor is a thienopyridine”", "It is a reversible, direct-acting cyclopentyl-triazolopyrimidine."),
  ],
  decode=[
    ("Post-PCI patient on aspirin, ticagrelor, metoprolol, atorvastatin: breathless with normal SpO₂, ECG and CT — culprit? [DocT GT]", "Ticagrelor."),
    ("ACS with a recent TIA, planned for PCI — which P2Y12 inhibitor is contraindicated? [DocT GT]", "Prasugrel."),
  ],
  punch="Prasugrel and ticagrelor beat clopidogrel; prasugrel is out after any stroke or TIA and in the old, ticagrelor is reversible and causes dyspnoea and pauses through adenosine.",
)

L['MI-48'] = dict(
  sub="Cardiology → ACS → Antithrombotic targets",
  step=6,
  intro="Step 6 maps every antithrombotic to the step of clotting it blocks; that map answers the reversal and bridging questions. Three real questions test it, and the card layer adds aspirin’s irreversibility and the GP IIb/IIIa timings.",
  parts=[
    ('a', "**Aspirin: thromboxane A2 (COX).** Aspirin acetylates platelet COX-1 irreversibly, and platelets have no nucleus to make more, so thromboxane A2 production stops for the platelet’s life (7–10 days). An absent aggregation response to arachidonic acid confirms the effect. Recovery needs new platelets (about 10% a day), so urgent bleeding needs platelet transfusion. NSAIDs block COX-1 reversibly."),
    ('b', "**Clopidogrel, prasugrel, ticagrelor, cangrelor: P2Y12 ADP receptor.** Cangrelor is the only IV P2Y12 inhibitor: reversible, half-life 3–6 minutes, platelet function back within about an hour. That makes it the bridge when a recent-stent patient must stop oral P2Y12 for urgent surgery (BRIDGE), and an option in P2Y12-naive patients during PCI (IIb, A)."),
    ('c', "**Eptifibatide, tirofiban: GP IIb/IIIa.** GP IIb/IIIa is the final common pathway, the fibrinogen receptor that links platelets, so blocking it stops aggregation whatever the trigger. Eptifibatide inhibits platelets within about 15 minutes, half-life about 2.5 hours, function back in 4–8 hours. Renal dosing differs: eptifibatide infusion halved when CrCl <50 mL/min and contraindicated on dialysis; tirofiban halved when CrCl <30; abciximab needed none. Today they are bail-out drugs for no-reflow or thrombotic complications during PCI (IIa, C)."),
    ('d', "**Rivaroxaban, apixaban, edoxaban, fondaparinux: factor Xa.** The oral agents block Xa directly; fondaparinux does so indirectly through antithrombin."),
    ('e', "**UFH, enoxaparin: Xa and thrombin.** Both work through antithrombin. UFH chains are long enough to bridge antithrombin and thrombin, so anti-Xa and anti-IIa activity are about equal; enoxaparin’s shorter chains act mainly on Xa (ratio about 3–4 to 1). Protamine fully reverses UFH, only partly enoxaparin."),
    ('f', "**Dabigatran, bivalirudin: thrombin (direct).** They bind thrombin without antithrombin, so they also inhibit clot-bound thrombin and do not interact with platelet factor 4 (hence bivalirudin in HIT, MI-49)."),
  ],
  mimic=[
    ("Cangrelor vs eptifibatide/tirofiban as an IV bridge", "Cangrelor replaces the oral P2Y12 blocker; GP IIb/IIIa inhibitors act on a different receptor and are bail-out drugs, not bridges."),
  ],
  traps=[
    ("“Tirofiban or eptifibatide” as the IV bridge for a patient on clopidogrel needing surgery", "They block GP IIb/IIIa, not P2Y12; cangrelor is the answer (80% right)."),
    ("“Aspirin inhibits COX-1 reversibly”", "Irreversibly; that is why its effect lasts the platelet’s life and transfusion is needed."),
    ("Abciximab", "No longer marketed in most countries; it bound irreversibly. Eptifibatide and tirofiban remain."),
  ],
  decode=[
    ("Recent stent, on aspirin + clopidogrel, needs urgent surgery — IV bridging agent? [DocT GT]", "Cangrelor infusion."),
    ("On aspirin 81 mg, GI bleed, absent response to arachidonic acid — mechanism? [DocT GT]", "Irreversible COX-1 inhibition."),
    ("Eptifibatide bolus + infusion — time to platelet inhibition? [Marrow]", "About 15 minutes."),
  ],
  punch="Aspirin hits thromboxane for the platelet’s life, the P2Y12 drugs hit ADP (cangrelor is the IV, reversible one), the GP IIb/IIIa drugs hit the final common pathway, and the anticoagulants hit Xa, thrombin or both.",
)

L['MI-49'] = dict(
  sub="Cardiology → ACS → Anticoagulation in PPCI",
  step=6,
  intro="Step 6 again: the anticoagulant during primary PCI. No real question is linked; the classic test is that fondaparinux is harmful here although it is Class I in conservatively managed NSTE-ACS (MI-50).",
  parts=[
    ('a', "**UFH bolus 70–100 U/kg: preferred, routine, Class I, C.** It is cheap, its effect can be measured in the lab (ACT) and protamine reverses it. With a GP IIb/IIIa inhibitor the dose is lower (50–70 U/kg)."),
    ('b', "**Enoxaparin IV 0.5 mg/kg: IIa, A.** ATOLL compared it with UFH in primary PCI: the primary composite narrowly missed significance (28% vs 34%, p = 0.07), but death, recurrent MI or urgent revascularisation fell (6.7% vs 11.3%) with similar major bleeding."),
    ('c', "**Bivalirudin: routine IIa, A; in HIT I, C.** A direct thrombin inhibitor with a short half-life and less bleeding; ESC 2023 makes it an alternative to UFH with a full-dose infusion continued after PCI (that removed the excess early stent thrombosis seen in older trials). It does not interact with platelet factor 4, so it is the agent of choice in heparin-induced thrombocytopenia."),
    ('d', "**Fondaparinux: NOT recommended, possible harm, Class III, B.** In OASIS-6, primary PCI with fondaparinux alone caused catheter thrombosis, because it does not inhibit thrombin directly and the contact system in catheters generates thrombin."),
    ('e', "**Generally not; limited to the periprocedural period.** Once the artery is stented and the patient is on DAPT, continued anticoagulation adds bleeding without benefit, unless there is another indication (LV thrombus, AF, mechanical valve)."),
  ],
  mimic=[
    ("Fondaparinux in PPCI vs in NSTE-ACS with delayed angiography", "Class III in PPCI (catheter thrombosis); Class I in NSTE-ACS when angiography is >24 h away, with a UFH bolus given if PCI follows."),
  ],
  traps=[
    ("“Fondaparinux is a good anticoagulant for primary PCI”", "Class III, B."),
  ],
  decode=[
    ("Anticoagulant of choice for primary PCI in a patient with HIT? [pattern]", "Bivalirudin (I, C)."),
    ("Which anticoagulant is not recommended in primary PCI? [pattern]", "Fondaparinux (III, B)."),
  ],
  punch="UFH 70–100 U/kg is the default in primary PCI, enoxaparin and bivalirudin are IIa alternatives (bivalirudin is I in HIT), fondaparinux is harmful, and the anticoagulant stops when the procedure ends.",
)

L['MI-50'] = dict(
  sub="Cardiology → ACS → ESC 2023 antithrombotic map",
  step=6,
  intro="Step 6 as one map. Two real questions test it: whether to pre-treat with a P2Y12 inhibitor before angiography, and which anticoagulant to use before angiography in NSTEMI.",
  parts=[
    ('a', "**NSTE-ACS, angiography <24 hours: UFH (I); enoxaparin (IIa).** UFH is easily reversed and is what the lab will use anyway; enoxaparin is an alternative (IIa, B)."),
    ('b', "**NSTE-ACS, angiography >24 hours: fondaparinux (I).** In OASIS-5 fondaparinux 2.5 mg daily matched enoxaparin for efficacy at 9 days with about half the major bleeding (about 2.2% vs 4.1%), and lower 30-day mortality, which followed the bleeding difference. If PCI follows, a full UFH bolus is added because of catheter thrombosis (MI-49)."),
    ('c', "**Aspirin I; P2Y12 before PPCI IIb; routine P2Y12 pretreatment in NSTE-ACS III.** In NSTE-ACS the anatomy is unknown until angiography, and some patients turn out to need CABG (where the P2Y12 blocker adds bleeding) or have no coronary cause. ACCOAST gave prasugrel before angiography and found no fewer ischaemic events but more bleeding; ISAR-REACT 5 used prasugrel without pretreatment in NSTE-ACS and still beat ticagrelor. If angiography is expected after 24 hours, pretreatment may be considered (IIb, C)."),
    ('d', "**Prasugrel over ticagrelor (IIa) when proceeding to PCI.** ISAR-REACT 5: death, MI or stroke at 1 year 6.9% vs 9.3%, without more bleeding."),
    ('e', "**Aspirin + P2Y12 for 12 months (I), then aspirin alone (I).** Shortening is allowed by bleeding risk (ESC: 1-month DAPT in high bleeding risk IIb; 3–6 months IIa). ACC/AHA 2025 add that patients who tolerated ticagrelor-based DAPT can switch to ticagrelor monotherapy from 1 month after PCI (Class 1); see MI-72."),
  ],
  mimic=[
    ("Fondaparinux: Class I vs Class III", "Class I as the anticoagulant in NSTE-ACS with angiography >24 h; Class III as the sole anticoagulant in primary PCI."),
  ],
  traps=[
    ("“Pre-treatment with a P2Y12 inhibitor is mandatory in NSTEMI”", "Routine pretreatment in NSTE-ACS going for early angiography is Class III; withhold until the anatomy is known (ACCOAST, ISAR-REACT 5)."),
    ("“UFH is superior to enoxaparin” or “enoxaparin is contraindicated for invasive strategy”", "Neither is true. DocT keys fondaparinux’s safety advantage over enoxaparin as the only true statement; note that with angiography within 24 hours ESC 2023 prefers UFH, and fondaparinux is the choice when angiography is beyond 24 hours."),
  ],
  decode=[
    ("NSTEMI for urgent invasive strategy — pre-treat with a P2Y12 inhibitor? [DocT GT]", "Generally withhold (especially prasugrel) until the anatomy is known."),
    ("Stable NSTEMI awaiting angiography — which anticoagulant statement is true? [DocT GT]", "Fondaparinux has less major bleeding than enoxaparin (OASIS-5)."),
  ],
  punch="Aspirin for all, P2Y12 at the time of PCI rather than before, prasugrel preferred, UFH if angiography is within 24 hours and fondaparinux if later, then 12 months of DAPT unless bleeding risk shortens it.",
)

L['MI-51'] = dict(
  sub="Cardiology → ACS → Fibrinolytic doses",
  step=3,
  intro="Step 3 turns to lysis itself. No real question is linked; doses are asked as recall, and the tenecteplase bands and its half dose in the elderly are the usual targets.",
  parts=[
    ('a', "**Streptokinase 1.5 million units IV over 30–60 minutes.** Not fibrin-specific: it activates circulating plasminogen as well as clot-bound, so it causes systemic fibrinolysis and hypotension, and it is antigenic: antibodies form within days and persist, so it is not repeated (ACC/AHA: not within 6 months)."),
    ('b', "**Alteplase: 15 mg bolus → 0.75 mg/kg over 30 minutes (max 50 mg) → 0.5 mg/kg over 60 minutes (max 35 mg).** The accelerated 90-minute regimen; the maximum total is 100 mg, which a patient of 67 kg or more receives as fixed 15 + 50 + 35 mg. Its short half-life is why it needs an infusion."),
    ('c', "**Reteplase 10 U + 10 U boluses 30 minutes apart.** A longer half-life allows two boluses."),
    ('d', "**Tenecteplase: single weight-based bolus, 30 mg <60 kg, 35 mg 60–69, 40 mg 70–79, 45 mg 80–89, 50 mg ≥90 kg; half-dose if ≥75 years.** Tenecteplase is the most fibrin-specific and longest-acting, so one bolus suffices, which makes it the pre-hospital agent. In STREAM, intracranial bleeding in the elderly was 3 of 42 before the protocol halved their dose and none of 93 after it (non-randomised, hypothesis-generating); ESC gives half-dose IIa, B."),
  ],
  mimic=[
    ("Streptokinase vs fibrin-specific agents", "Streptokinase: systemic lysis, hypotension, allergy, cheap. Fibrin-specific agents: clot-bound plasminogen, bolus dosing, preferred (I, B)."),
  ],
  traps=[
    ("“Full-dose tenecteplase for an 80-year-old”", "Half dose from 75 years (ESC ≥75). Do not confuse it with the clopidogrel rule after lysis, which drops the 300 mg load only above 75."),
  ],
  decode=[
    ("Tenecteplase dose for a 72 kg patient aged 60? [pattern]", "40 mg single bolus."),
  ],
  punch="Tenecteplase is one weight-based bolus of 30–50 mg, halved from 75 years; alteplase is the 90-minute three-step infusion; streptokinase is 1.5 million units and not fibrin-specific.",
)

L['MI-52'] = dict(
  sub="Cardiology → ACS → Fibrinolysis recommendations",
  step=3,
  intro="Step 3: how lysis is given. No real question is linked; the likely test is that the P2Y12 partner for lysis is clopidogrel.",
  parts=[
    ('a', "**As soon as possible after diagnosis, preferably pre-hospital: Class I, A.** The benefit of lysis falls fastest in the first hours (MI-54); giving it in the ambulance saves the most myocardium."),
    ('b', "**Fibrin-specific agent (tenecteplase, alteplase, reteplase): Class I, B.** They act mainly on fibrin-bound plasminogen, giving better patency than streptokinase."),
    ('c', "**Half-dose tenecteplase: IIa, B.** Intracranial haemorrhage rises with age (MI-51)."),
    ('d', "**Aspirin + clopidogrel 300 mg.** ESC 2023 Class I, A. Clopidogrel is the P2Y12 inhibitor tested at the time of lysis (CLARITY, COMMIT); prasugrel has not been tested with lysis, and ticagrelor only when started a median of about 11 hours afterwards in patients under 75 (TREAT: no more major bleeding than clopidogrel). More potent platelet inhibition given with the lytic risks intracranial bleeding. Over 75 years, clopidogrel 75 mg without the 300 mg load."),
    ('e', "**Continue anticoagulation until revascularisation.** ESC: until revascularisation, or for the hospital stay up to 8 days, Class I, A. Enoxaparin (IV bolus then subcutaneous) was better than UFH with lysis in ExTRACT-TIMI 25."),
  ],
  mimic=[
    ("P2Y12 with lysis vs with PCI", "Lysis: clopidogrel. PCI: prasugrel or ticagrelor."),
  ],
  traps=[
    ("“Ticagrelor or prasugrel with tenecteplase”", "Clopidogrel is the partner for lysis."),
  ],
  decode=[
    ("STEMI being lysed: which P2Y12 inhibitor and dose? [pattern]", "Clopidogrel 300 mg (75 mg if >75 years) with aspirin."),
  ],
  punch="Lyse early, ideally pre-hospital, with a fibrin-specific drug (half-dose tenecteplase if old), add aspirin and clopidogrel, and anticoagulate until revascularisation.",
)

L['MI-53'] = dict(
  sub="Cardiology → ACS → Lysis contraindications",
  step=3,
  intro="Step 3: who must not be lysed. Five real questions test this list, often in PE or rural STEMI stems; the hidden difficulty is that different guidelines draw the stroke and surgery windows differently.",
  parts=[
    ('a', "**Absolute: prior ICH or stroke of unknown origin at any time; ischaemic stroke in the preceding 6 months; CNS damage, neoplasm or AVM; major trauma, surgery or head injury within 1 month; GI bleeding within 1 month; known bleeding disorder (excluding menses); aortic dissection; non-compressible puncture in 24 h (liver biopsy, LP).** The common thread is a site that would bleed catastrophically (brain, aorta, a fresh wound) once fibrin is dissolved everywhere. Aortic dissection matters because it can mimic STEMI (inferior ST elevation when the flap involves the right coronary)."),
    ('b', "**Relative: TIA in the preceding 6 months; oral anticoagulant therapy; pregnancy or within 1 week post-partum; refractory hypertension (SBP >180 and/or DBP >110); advanced liver disease; infective endocarditis; active peptic ulcer; prolonged or traumatic resuscitation.** Here the risk is weighed against the benefit. Marrow adds active diabetic haemorrhagic retinopathy as relative; a previous MI is not a contraindication; CPR counts only if prolonged (over 10 minutes) or traumatic."),
  ],
  table=dict(title="Same patient, different list", head=["Item", "ESC (STEMI and PE)", "ACC/AHA (STEMI)"], rows=[["Ischaemic stroke", "**absolute <6 months**", "absolute <3 months"], ["Major surgery or trauma", "**absolute <1 month** (ESC PE 2019: <3 weeks)", "relative <3 weeks"], ["Head trauma / intracranial surgery", "absolute <1 month", "absolute <3 months / <2 months"], ["SBP >180 / DBP >110", "relative", "relative (absolute if unresponsive)"], ["AVM, prior ICH", "**absolute in every list**", "**absolute in every list**"]]),
  mimic=[
    ("Ischaemic stroke vs TIA within 6 months", "Same window, different class: stroke absolute, TIA relative."),
  ],
  traps=[
    ("“Prior ischaemic stroke 5 months ago” or “surgery 2 weeks ago” offered beside a known AVM", "Under the ESC list (this card) both are absolute too; the GT key is AVM (75% right) because it is absolute in every guideline. When several look absolute, pick the one no list disputes."),
    ("“SBP >180 mmHg” or “warfarin and aspirin” as absolute", "Both are relative; previous haemorrhagic stroke is absolute (68% right)."),
    ("“Only contraindicated if on anticoagulation” for massive PE with ischaemic stroke 2 months ago", "Ischaemic stroke within 6 months is absolute in ESC PE and STEMI rules (71% right); stroke-lysis rules use 3 months."),
  ],
  decode=[
    ("Absolute contraindication to thrombolysis in STEMI? [DocT QBank]", "Previous haemorrhagic stroke."),
    ("Rural anterior STEMI, transfer 3 h — which is an absolute contraindication? [DocT GT]", "Known arteriovenous malformation."),
    ("Massive PE with shock, ischaemic stroke 2 months ago — eligibility? [DocT GT]", "Absolute contraindication."),
    ("Post-op day 2 MI with hypotension — what is NOT recommended? [Marrow]", "Thrombolytic therapy (surgery within 1 month)."),
  ],
  extra=[dict(q="Contraindication to fibrinolysis in acute MI among the options? [Marrow]", a="Active diabetic haemorrhagic retinopathy (relative); previous MI is not a contraindication.")],
  punch="Lysis dissolves fibrin everywhere, so anything that would bleed into the brain, aorta or a fresh wound rules it out; brain lesions and prior ICH are absolute in every list, and stroke within 6 months is absolute but TIA is only relative.",
)

L['MI-54'] = dict(
  sub="Cardiology → ACS → Lysis time windows",
  step=3,
  intro="Step 3: when lysis still works. No real question is linked; the card also corrects a mix-up in the notes between the lysis window and the post-lysis angiography window.",
  parts=[
    ('a', "**Within 2 hours of symptom onset.** A fresh thrombus is fibrin-rich and loose; over hours it becomes organised and cross-linked, so lytics dissolve it less well, while the myocardium at risk is already dying. Lives saved per 1,000 treated fall steeply after the first 2–3 hours."),
    ('b', "**PCI preferred over fibrinolysis after 3 hours.** As lysis loses effect with time, the mechanical approach keeps its patency rate, so PCI wins when it can be done within the 120-minute window."),
    ('c', "**Up to 12 hours: still effective, reduced benefit.** ESC: lysis within 12 hours of symptoms if PPCI cannot be done in time (I, A). Beyond 12 hours the risk outweighs the benefit; late STEMI (12–48 h) goes to PCI (IIa, B)."),
    ('d', "**≤10 minutes from diagnosis to bolus.**"),
    ('e', "**The window for angiography after SUCCESSFUL lysis (MI-42).** 2–24 hours is not a window for giving lysis."),
  ],
  mimic=[
    ("Lysis window vs post-lysis angiography window", "Lysis: up to 12 hours of symptoms. Angiography after successful lysis: 2–24 hours after the lytic."),
  ],
  traps=[
    ("“Lysis is effective within 2–24 hours”", "A notes error; lysis is for symptoms ≤12 hours."),
  ],
  decode=[
    ("STEMI with 14 h of symptoms, no PCI nearby, pain settling — lyse? [pattern]", "No; beyond 12 hours lysis is not indicated, transfer for PCI."),
  ],
  punch="Lysis works best in the first 2 hours and not at all usefully after 12; 2–24 hours is the angiography window after lysis, not a window for giving it.",
)

L['MI-55'] = dict(
  sub="Cardiology → ACS → CABG in ACS",
  step=6,
  intro="The deck ends with surgery, where the antiplatelet drugs become the problem. Both real questions ask how long before urgent CABG each drug must be stopped.",
  parts=[
    ('a', "**Anatomy unsuitable for PCI, failed PCI, mechanical complications (coronary dissection, VSD, papillary muscle rupture).** Left main or complex multivessel disease is the commonest anatomical reason."),
    ('b', "**Higher mortality (non-randomised data).** Operating in the first days means bypass on freshly infarcted, reperfusion-injured myocardium, in a patient loaded with antiplatelets."),
    ('c', "**After 3–7 days.** For a stable patient, waiting lets the infarct settle and the P2Y12 blocker wear off."),
    ('d', "**Refractory ischaemia, cardiogenic shock.** ESC: emergency CABG for ACS-related shock when PCI of the infarct artery is not feasible or has failed (I, B)."),
    ('e', "**A second antiplatelet is typically given after the procedure.** ESC 2023: resume DAPT after CABG for at least 12 months (I, C), because the ACS risk is still there."),
  ],
  table=dict(title="Stopping antiplatelets before CABG", head=["Drug", "Urgent CABG", "Elective CABG"], rows=[["Aspirin", "**continue**", "continue"], ["Clopidogrel, ticagrelor", "**stop ≥24 h** (ACC/AHA I)", "ticagrelor ≥3 days, clopidogrel ≥5 days"], ["Prasugrel", "most potent and irreversible: delay surgery if possible", "≥7 days"], ["Eptifibatide, tirofiban", "**stop 2–4 h**", "—"], ["Abciximab (historical)", "≥12 h", "—"]]),
  mimic=[
    ("Short-acting GP IIb/IIIa inhibitors vs oral P2Y12 blockers before surgery", "Eptifibatide and tirofiban are reversible and renally cleared, so platelets recover within hours; oral P2Y12 blockers need a day to a week."),
  ],
  traps=[
    ("“Continue ticagrelor until surgery” or “stop 2–4 hours before”", "Stop at least 24 hours before urgent on-pump CABG."),
    ("“Stop eptifibatide 24 hours before”", "Only 2–4 hours are needed."),
  ],
  decode=[
    ("NSTEMI on aspirin + ticagrelor, left main disease, urgent CABG — ticagrelor? [DocT GT]", "Stop 24 hours before."),
    ("STEMI on eptifibatide, urgent CABG — minimum stop time? [DocT GT]", "2–4 hours."),
  ],
  punch="CABG in ACS is for anatomy PCI cannot fix, failed PCI, mechanical complications or shock. Before urgent surgery keep aspirin, stop clopidogrel or ticagrelor 24 hours and eptifibatide or tirofiban 2–4 hours, and restart DAPT afterwards.",
)

FLAGS = {
  'MI-38': "b: not wrong, but incomplete. Riociguat (sGC stimulator) is also a nitrate contraindication (Marrow, two questions), and ESC adds marked bradycardia. Consider adding; the explanation gives both. DocT QBank ‘nitrate-relieved pain, normal ECG, negative troponin → oesophageal spasm’ key is debatable (cardlayer cross line); the trap says so.",
  'MI-39': "d: ESC’s indication is any PPCI patient without acute HF and with SBP >120 mmHg (IIa A), not tachycardia specifically. Also, the contraindications to an IV beta-blocker are wider than ‘heart failure and hypotension’: PR >240 ms or second/third-degree block, active bronchospasm and high shock risk (age >70, HR >110, SBP <120; COMMIT). Marrow keys them. Consider adding; the explanation gives them.",
  'MI-45': "c: the trial attribution is loose. MATRIX itself also showed lower all-cause mortality; RIVAL’s overall primary outcome was neutral (fewer vascular complications, benefit in the STEMI subgroup); RIFLE-STEACS showed lower cardiac mortality and shorter stay. Not wrong enough to change; the explanation says it.",
  'MI-53': "Card follows the ESC list and is correct for it. The DocT GT question (rural STEMI) keys AVM while also offering ischaemic stroke 5 months ago and surgery 2 weeks ago, both absolute under ESC (<6 months, <1 month) but not under ACC/AHA (<3 months; surgery <3 weeks relative). The trap explains choosing the item absolute in every list.",
}
