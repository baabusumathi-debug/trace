# CVS10D — Explain v3 ("Learn" depth): ACS IV, complications and after-care — monitoring after PCI, long-term drugs by LVEF, ventricular arrhythmias (mechanism, management,
# ESC classes), AV block after MI, acute heart failure in ACS, cardiogenic shock in STEMI, the device-trial trail, the three ruptures, VSR timing, LV aneurysm, GRACE, TIMI, GRACE vs TIMI.
# No mnemonics or hooks. Driven by qpack/CVS10D.md (21 question links; MI-64 ruptures asked 7 times, MI-58 ventricular arrhythmias 4, MI-61 and MI-62 three each, MI-60 two,
# MI-57 and MI-66 one each). MI-56, MI-59, MI-63, MI-65, MI-67, MI-68 and MI-69 have no linked question and get short explanations with [pattern] decode items.
# No Top-up cards for CVS10D in cvs_topups.json. No `fix` entries for CVS10D in trace/test/data/qbank.json (checked 19 Nov 2026). cvs_cardlayer.json `lines` and `cross` read and used
# (MI-58, MI-60, MI-61, MI-62).
# Checked online on 19 Nov 2026:
#  - ESC 2023 ACS guideline (Byrne et al., Eur Heart J 2023;44:3720; body text read on academic.oup.com, recommendation tables not rendered): ECG monitoring ≥24 h after symptom onset in
#    high-risk patients (all STEMI); LVEF measured before discharge in all ACS; mechanical complications 0.27% of STEMI and 0.06% of NSTEMI, in-hospital mortality 42.4% and 18%; surgery
#    preferred; IABP ‘should be considered’ while awaiting surgery; LV thrombus >9% after anterior STEMI (CMR up to 12.2% anterior, 6.3% all STEMI), OAC (warfarin or NOAC) ‘should be
#    considered for 3–6 months’ guided by repeat imaging; haemodynamically significant VT/VF in 6–8% of STEMI; sustained VT/VF after 48 h → ICD evaluation; no primary-prevention ICD within
#    40 days; IRA-only PCI at the index procedure in shock (CULPRIT-SHOCK); routine IABP not recommended without mechanical complications; MCS role unclear; acute HF in ACS raises renal,
#    respiratory and infective complications and death. Beta-blockers I A for LVEF ≤40% regardless of HF symptoms (ESC Council for Cardiology Practice summary); benefit with LVEF >40% ‘not
#    well established’, maintenance ‘should be considered’. Short-term MCS IIb C, IABP for mechanical complications IIa C (MDPI Cardiogenetics/JCDD 2026 review quoting ESC 2023).
#  - ACC/AHA 2025 ACS guideline (Rao et al.), via the same review and Guideline Central: microaxial flow pump reasonable (2a, B-R) in selected STEMI with severe/refractory shock; MCS for
#    mechanical complications with instability 2a; routine IABP and routine VA-ECMO 3: No Benefit; oral beta-blocker within 24 h if no contraindication; high-intensity statin.
#  - ESC 2022 ventricular arrhythmias guideline (Zeppenfeld et al., Eur Heart J 2022;43:3997; section 7.1.1 body text): urgent reperfusion is the most important therapy; beta-blockers
#    recommended to prevent VA; IV amiodarone ‘should be considered’ for recurrent haemodynamically relevant VA; lidocaine ‘may be considered’ if beta-blocker and amiodarone fail;
#    prophylactic antiarrhythmics not beneficial and possibly harmful; ablation for recurrent VF triggered by similar PVCs; no routine wearable defibrillator early post-MI; early routine
#    ICD in the first 40 days did not reduce mortality.
#  - Trials: DanGer Shock (355 analysed, STEMI shock): 180-day death 45.8 vs 58.5%; more bleeding, limb ischaemia, RRT. ECLS-SHOCK (n 420): 30-day death 47.8 vs 49.0%; 78% resuscitated
#    before randomisation. IABP-SHOCK II (n 600): no 30-day, 1-year or 6-year difference. Beta-blocker meta-analysis LVEF 40–49% (REBOOT 979, BETAMI 422, DANBLOCK 430, CAPITAL-RCT 54;
#    n 1,885; ESC Congress 2025): death/MI/HF 10.7 vs 14.4%, HR 0.75 (0.58–0.97).
# From standard references without a fresh check (confident unless said): DanGer Shock HR 0.74, NNT 8, safety composite 24.0 vs 6.2% (RR 4.74); IABP-SHOCK II 39.7 vs 41.3%;
# REDUCE-AMI (LVEF ≥50%, n 5,020, no benefit); REBOOT (LVEF >40%, n 8,505, no benefit); BETAMI-DANBLOCK (LVEF ≥40%, n 5,574, fewer death/MI, HR ≈0.85); SHOCK trial (early
# revascularisation: 30-day 46.7 vs 56.0% NS, 6-month 50.3 vs 63.1%); CULPRIT-SHOCK (30-day death/RRT 45.9 vs 55.4%); SOAP II (dopamine more arrhythmias, worse in the cardiogenic
# subgroup); OptimaCC (epinephrine more refractory shock than norepinephrine after MI); DIG; EPHESUS; GRACE (Granger 2003 in-hospital model with Killip class and arrest; Eagle 2004
# post-discharge 6-month model, nine variables); TIMI UA/NSTEMI (Antman 2000; event rates 4.7/8.3/13.2/19.9/26.2/40.9%); AHA 2021 statement on mechanical complications (posteromedial
# papillary muscle 6–12 times more often, single PDA supply; VSR anterior → apical, inferior → basal septum); AHA 2025 ACLS bradycardia (atropine 1 mg, max 3 mg; epinephrine or dopamine
# infusion; pacing). ESC 2023 classes for ACEi (I A selected / IIa A all) and MRA (card: I B) and the MI-59 class list (ESC 2017 STEMI wording) were not re-read in the 2023 tables.
# Second-check review 19 Nov 2026 (ESC 2023 ACS full text, recommendation tables 9, 10, 14, 16 read): MRA I A (not I B); ACEi I A / IIa A; beta-blocker I A / IIa B; repeat LVEF
# 6–12 weeks I C; IV beta-blocker and/or amiodarone for polymorphic VT/VF I B; LV thrombus OAC 3–6 months IIa C; IABP for mechanical complications IIa C; IRA-only PCI in shock I B;
# permanent pacing if high-degree AV block persists ≥5 days I C, no pacing if it resolves III B. DanGer Shock (Wiki Journal Club / NEJM 2024): 360 randomised, 355 analysed; HR 0.74 (0.55–0.99),
# NNT 8; safety composite (severe bleeding, limb ischaemia, haemolysis, device failure, worsening AR) 24.0 vs 6.2%, RR 4.74; RRT 41.9 vs 26.7%. ACC/AHA 2025: microaxial pump 2a in STEMI with
# severe or refractory shock, MCS for mechanical complications 2a B-NR (CardioNerds summary). REBOOT n 8,505, LVEF >40%, no difference (CNIC); BETAMI-DANBLOCK n 5,574, HR 0.85 (0.75–0.98),
# driven by fewer MIs, death unchanged (ESC Hot Line); pooled LVEF 40–49% n 1,885, HR 0.75 (ESC Hot Line). STS VSR repair: operative mortality 54.1% within 7 days, 18.4% later (Arnaoutakis 2012).

SPINE = [
  ("Watch the first two days", "After reperfusion the patient stays on a monitor for 24–48 hours because the early killers are arrhythmia and re-occlusion, and an echo before discharge sets the LVEF that decides the drugs and the device."),
  ("Ventricular arrhythmias by timing", "Early VT/VF comes from ischaemia and is treated by reperfusion, potassium, magnesium and a beta-blocker; AIVR at reperfusion is benign; antiarrhythmics are never given prophylactically."),
  ("AV block by territory", "Inferior MI blocks the AV node, which recovers; anterior MI blocks the His–Purkinje system, which does not respond to atropine and needs pacing."),
  ("Pump failure and shock", "Lost myocardium causes congestion or low output; shock is treated by opening the culprit artery first, then drugs, with routine IABP and VA-ECMO of no benefit and Impella helping only selected STEMI shock."),
  ("Mechanical complications", "Around days 1–7 the necrotic wall can tear — free wall, septum or papillary muscle — and present as sudden collapse or sudden pulmonary oedema with a new murmur; the answer is echo, a bridge and surgery."),
  ("Risk scores and lifelong drugs", "GRACE (nine weighted variables, death at 6 months, >140 high risk) and TIMI (seven one-point items, 14-day events) grade the risk; a high-dose statin and 12 months of DAPT go to everyone, and beta-blocker, ACE inhibitor and MRA follow the LVEF."),
]

PRIMER = "Once the artery is open, the infarct still threatens the patient in three ways. Electrically, ischaemic and then scarred myocardium fires abnormally or blocks conduction; mechanically, necrotic muscle softens over the first days and can tear; and as a pump, lost myocardium leaves too little forward output. Coronary anatomy predicts most of it: the RCA supplies the AV node in most people, LAD septal branches supply the His bundle and bundle branches, and the posteromedial papillary muscle depends on a single artery. ESC classes read as I ‘recommended’, IIa ‘should be considered’, IIb ‘may be considered’, III ‘not recommended’; CVS10C covered reperfusion itself."

L = {}

L['MI-56'] = dict(
  sub="Cardiology → ACS → Monitoring and follow-up",
  step=1,
  intro="Step 1 is the bridge from the cath lab to discharge. No real question is linked; the testable points are why the monitor stays on and when LVEF is measured and measured again.",
  parts=[
    ('a', "**24–48 hours.** Most VF after STEMI happens in the first hours to 48 hours, while ischaemic borders are electrically unstable; ESC 2023 asks for ECG monitoring for at least 24 hours after symptom onset in every STEMI and other high-risk patient, longer if reperfusion was late or incomplete or LVEF is low."),
    ('b', "**Detect arrhythmias; detect re-infarction (repeat ST elevation / ST-T change).** A new ST rise in the stented territory is stent thrombosis until proved otherwise and goes straight back to the lab (MI-41)."),
    ('c', "**1–2 days post-PCI; follow-up echo for LVEF later.** The early echo gives LVEF (which sets the drugs, MI-57) and looks for mechanical complications and LV thrombus. Stunned myocardium recovers over weeks, so if LVEF is ≤40% ESC repeats it 6–12 weeks after full revascularisation and medical therapy before deciding on an ICD; the notes’ ‘3–6 weeks’ is older wording."),
    ('d', "**Prevent recurrence and CAD progression — sugar control, lifestyle change.** Smoking cessation, exercise-based cardiac rehabilitation, diet and weight, blood pressure and glucose control sit alongside the drugs."),
  ],
  mimic=[
    ("Early (pre-discharge) echo vs repeat echo at 6–12 weeks", "The first finds the LVEF and complications; the second decides the ICD, because stunned muscle may have recovered."),
  ],
  traps=[
    ("“ICD before discharge for LVEF 30% on day 2”", "Primary-prevention ICD is not given within 40 days of MI; repeat LVEF first."),
  ],
  decode=[
    ("Uncomplicated PPCI — minimum monitored period? [pattern]", "At least 24 hours (24–48 hours)."),
    ("Post-MI LVEF 35% on day 2 — when to reassess before an ICD? [pattern]", "6–12 weeks after revascularisation and optimal medical therapy."),
  ],
  punch="Keep the monitor on for 24–48 hours because VF and stent thrombosis come early; measure LVEF before discharge and again at 6–12 weeks if it was low, because that second number decides the ICD.",
)

L['MI-57'] = dict(
  sub="Cardiology → ACS → Secondary prevention drugs",
  step=6,
  intro="Step 6: what the patient takes for life. The one real question (47% right) asks which drug improves prognosis in post-MI HFrEF; the card sorts every drug by LVEF so the answer drops out.",
  parts=[
    ('a', "**Oral beta-blocker: I, A if LVEF ≤40% or HF; IIa, B if LVEF >40%.** Blocking catecholamines lowers oxygen demand, raises the VF threshold and lets the remodelling ventricle recover; with low LVEF the old trials cut death by over 20%. Above 40% the evidence is now split: REDUCE-AMI (LVEF ≥50%) and REBOOT (LVEF >40%) showed no overall benefit, BETAMI-DANBLOCK (LVEF ≥40%) showed fewer events (HR 0.85, mainly fewer reinfarctions, with no difference in death), and a pooled analysis of LVEF 40–49% (n 1,885) cut death, MI or HF from 14.4% to 10.7% (HR 0.75). So the case is strong at ≤49% and weak at ≥50% (MI-73)."),
    ('b', "**ACE inhibitor: I, A if LVEF ≤40% or HF (also diabetes, hypertension, CKD); IIa, A in all others.** ACE inhibition limits angiotensin-driven dilatation and fibrosis of the infarcted ventricle; an ARB (valsartan, VALIANT) is the alternative if intolerant."),
    ('c', "**MRA: I, B — LVEF ≤40% AND HF (or diabetes).** ESC 2023 now grades this I, A (LVEF ≤40% with HF or diabetes). Aldosterone drives fibrosis and potassium loss despite an ACE inhibitor; eplerenone in EPHESUS cut death and CV admissions in exactly this group. Check potassium and creatinine first."),
    ('d', "**High-dose statin: I, A — all.** Given regardless of LVEF or baseline cholesterol, as early as possible; ESC targets LDL-C <1.4 mmol/L (55 mg/dL) and a 50% fall, adding ezetimibe then a PCSK9 inhibitor if needed."),
    ('e', "**DAPT: 12 months — all.** Aspirin plus a P2Y12 inhibitor (prasugrel or ticagrelor preferred) by default for 12 months, shortened for high bleeding risk (CVS10C)."),
  ],
  mimic=[
    ("Prognostic drugs vs symptomatic drugs in post-MI HFrEF", "Beta-blocker, ACE inhibitor/ARNI, MRA and SGLT2 inhibitor prolong life; nitrates, digoxin and diuretics relieve symptoms only."),
  ],
  traps=[
    ("“Intravenous milrinone” for an EF of 25% with dyspnoea", "Only 47% chose the beta-blocker. Inotropes raise oxygen demand and arrhythmias and increase long-term mortality; they are a bridge in shock, not prognostic therapy."),
    ("“Digoxin” or “nitrates” to improve prognosis", "Digoxin reduced HF admissions but not death (DIG); nitrates treat angina only."),
    ("“Beta-blocker is Class I for every post-MI patient”", "Only for LVEF ≤40%; above that ESC gives IIa and the newest trials disagree."),
  ],
  decode=[
    ("Post-MI, EF 25%, stable but breathless — which therapy improves long-term prognosis? [DocT QBank]", "Oral beta-blocker (the only prognostic option offered)."),
    ("Post-MI, LVEF 35% with HF on ACE inhibitor and beta-blocker — what to add? [pattern]", "An MRA (eplerenone/spironolactone)."),
  ],
  punch="Everyone gets a high-dose statin and 12 months of DAPT; LVEF ≤40% adds a beta-blocker and ACE inhibitor as Class I, and an MRA if there is HF. Inotropes, digoxin and nitrates never improve prognosis.",
)

L['MI-58'] = dict(
  sub="Cardiology → ACS → Ventricular arrhythmias after MI",
  step=2,
  intro="Step 2 sorts ventricular arrhythmias by when they appear, because timing tells you the mechanism and the treatment. All four real questions ask the mechanism of VT at 48 hours, which the card does not state: the answer is abnormal automaticity.",
  parts=[
    ('a', "**Accelerated idioventricular rhythm — reperfusion + enhanced automaticity of ventricular pacemaker cells; BENIGN, usually no treatment.** Washout of the opened artery speeds normal Purkinje pacemakers until they outrun the sinus node: a regular wide-complex rhythm only a little faster than sinus, which gives way when the sinus rate rises. It is a marker that reperfusion worked; suppressing it with an antiarrhythmic can leave no rhythm at all."),
    ('b', "**VT unstable: immediate cardioversion + correct K⁺ and Mg²⁺.** Pulseless VT is treated as VF on the arrest algorithm. Potassium is kept at 4 mmol/L or above and magnesium in the high-normal range, because low levels lower the threshold for every mechanism."),
    ('c', "**VT stable: correct electrolytes; beta-blocker or amiodarone.** Catecholamines drive early post-MI VT, so a beta-blocker treats the cause; amiodarone suppresses recurrence. Recurrent VT means ongoing ischaemia until angiography proves otherwise (MI-59)."),
    ('d', "**NSVT: correct electrolytes; beta-blocker.** Runs of NSVT in the first 48 hours are common and do not predict late sudden death; they need no antiarrhythmic and no ICD decision."),
  ],
  table=dict(title="Mechanism by time after MI", head=["Window", "Rhythm", "Mechanism"], rows=[["Minutes–hours (acute ischaemia)", "VF, polymorphic VT", "re-entry in ischaemic tissue"], ["At reperfusion", "AIVR", "**enhanced normal automaticity** (Purkinje pacemakers)"], ["24–72 h", "PVCs, NSVT, VT", "**abnormal automaticity** in partly depolarised ischaemic myocytes and Purkinje fibres (± triggered activity)"], ["Weeks–years", "sustained monomorphic VT", "**re-entry around scar**"], ["Any time, other causes", "torsades / digoxin VT", "EADs (long QT) / DADs (Ca²⁺ overload)"]]),
  mimic=[
    ("AIVR vs slow VT", "AIVR runs near the sinus rate, starts and stops with sinus slowing and is harmless; VT is faster and sustained."),
    ("Enhanced normal vs abnormal automaticity", "Normal automaticity is a pacemaker cell firing faster (AIVR); abnormal automaticity is a working myocyte, partly depolarised by ischaemia, that starts firing on its own (VT at 24–72 h)."),
  ],
  traps=[
    ("“Re-entry” for VT 48 hours after MI", "61–67% got the NSVT version right. Re-entry is the mechanism of very early VF and of late scar VT; at 24–72 hours abnormal automaticity is the best answer. Re-entry is still the main mechanism of sustained post-MI VT overall, so choose it only when the stem is weeks to years after MI."),
    ("“Enhanced normal automaticity” for VT at 48 hours", "That is AIVR at reperfusion; VT at 48 hours comes from non-pacemaker cells, which is abnormal automaticity."),
    ("“Early or delayed afterdepolarisations”", "EADs belong to long QT and torsades; DADs to digoxin and calcium overload. Neither is the post-MI answer."),
    ("Treating AIVR with amiodarone or lidocaine", "It is benign and a sign of reperfusion; suppressing it can unmask asystole."),
  ],
  decode=[
    ("VT 48 hours after a large anterior MI — mechanism? [DocT GT ×2]", "Abnormal automaticity (83–87% right)."),
    ("Stable NSVT 48 hours after MI — mechanism? [DocT GT ×2]", "Abnormal automaticity, not re-entry (61–67% right)."),
    ("Wide regular rhythm at 80/min just after the artery is opened — action? [pattern]", "AIVR: none."),
  ],
  extra=[dict(q="Mechanism of ventricular arrhythmia 24–72 h after MI? [DocT GT ×4]", a="Abnormal automaticity of partly depolarised ischaemic myocytes and Purkinje fibres, driven by catecholamines and low K⁺/Mg²⁺; AIVR is enhanced normal automaticity; late monomorphic VT is scar re-entry.")],
  punch="Read the clock: VF in the first hours is ischaemic re-entry, AIVR at reperfusion is harmless enhanced automaticity, VT at 24–72 hours is abnormal automaticity, and VT weeks later is scar re-entry. Early arrhythmias need electrolytes, a beta-blocker and an open artery, not prophylactic drugs.",
)

L['MI-59'] = dict(
  sub="Cardiology → ACS → Ventricular arrhythmia recommendations",
  step=2,
  intro="Step 2 as a class list. No real question is linked; the testable ends are the Class I treatments (beta-blocker, revascularisation) and the Class III ‘prophylactic antiarrhythmics’.",
  parts=[
    ('a', "**IV beta-blocker for polymorphic VT / VF: I, B.** Polymorphic VT during an MI is ischaemic and catecholamine-driven; a beta-blocker removes the trigger. ESC 2022 also recommends beta-blockers to prevent VA, and ESC 2023 words this row ‘IV beta-blocker and/or amiodarone’ for polymorphic VT/VF (I, B)."),
    ('b', "**Prompt complete revascularisation for recurrent VT / VF: I, C.** Ongoing ischaemia keeps the substrate unstable; ESC 2022 calls urgent reperfusion the most important therapy."),
    ('c', "**IV amiodarone for recurrent polymorphic VT: I, C; for recurrent VT despite repeated cardioversion: IIa, C.** Amiodarone blocks potassium, sodium and calcium channels and has a beta-blocking effect, so it lengthens refractoriness and suppresses recurrence with little negative inotropy. The card follows the 2017 STEMI list. ESC 2023 merges it into the beta-blocker row (‘IV beta-blocker and/or amiodarone’, I, B), while the 2022 VA guideline says IV amiodarone ‘should be considered’ for recurrent haemodynamically relevant VA (IIa)."),
    ('d', "**Transvenous overdrive pacing: IIa, C; RF ablation then ICD for recurrent VT / VF / storm: IIa, C.** Pacing faster than the VT suppresses it; ablation works best when the VF is triggered each time by the same Purkinje PVC."),
    ('e', "**Lidocaine if the above fail: IIb, C.** A sodium-channel blocker that acts best on ischaemic, partly depolarised tissue; third line."),
    ('f', "**Prophylactic antiarrhythmics: III, B; treating asymptomatic, irrelevant VAs: III, C.** Prophylactic lidocaine reduced VF in old trials but did not reduce, and tended to increase, mortality, partly through bradycardia and asystole; class IC drugs given for post-MI ectopy increased death (CAST)."),
  ],
  mimic=[
    ("Electrical storm vs single VT episode", "Storm is three or more sustained episodes in 24 hours: sedation, beta-blocker, amiodarone, revascularise, then pacing or ablation."),
  ],
  traps=[
    ("“Prophylactic lidocaine after MI”", "Class III: fewer VF episodes, but no fall in deaths and a trend to more."),
  ],
  decode=[
    ("Recurrent polymorphic VT on day 1 of STEMI — first measures? [pattern]", "IV beta-blocker, correct K⁺/Mg²⁺, urgent angiography and revascularisation; amiodarone next."),
    ("Prophylactic antiarrhythmic after MI — class? [pattern]", "III (harmful)."),
  ],
  punch="Treat the cause first: an IV beta-blocker and an open artery are Class I, amiodarone, pacing and ablation come next, lidocaine last, and prophylactic antiarrhythmics are Class III.",
)

L['MI-60'] = dict(
  sub="Cardiology → ACS → AV block after MI",
  step=3,
  intro="Step 3: the level of the block follows the artery. Both real questions are about the inferior–anterior split; one has a wrong key and the other has two true options.",
  parts=[
    ('a', "**Proximal block: 1st degree, Mobitz I; RCA (inferior MI); usually transient, resolves with reperfusion; pacemaker not typically needed.** The RCA supplies the AV node in most people, and inferior MI adds vagal (Bezold–Jarisch) tone and adenosine release at the node. Nodal block has a narrow junctional escape at 40–60/min that keeps the patient perfused, responds to atropine and usually recovers within days. Inferior MI can also cause complete heart block at the node; it behaves the same way and still usually resolves."),
    ('b', "**Distal block: 3rd degree; LAD (anterior MI); life-threatening; pacemaker often required.** Septal branches of the LAD supply the His bundle and bundle branches, so block here means a large septal infarct. Mobitz II or new bifascicular block warns of it; the escape is wide and slow (under 40/min) and unreliable. Atropine works on the node only and may worsen infranodal block by speeding the atrial rate."),
    ('c', "**Bradycardia / high-grade block with haemodynamic intolerance: IV positive chronotropes (epinephrine, vasopressin and/or atropine) — I, C; temporary pacing if they fail — I, C; urgent angiography if no prior reperfusion — I, C.** Drugs buy minutes, the pacing wire gives a dependable rate, and reopening the artery treats the cause. AHA 2025 ACLS doses: atropine 1 mg every 3–5 minutes to 3 mg, then epinephrine infusion or pacing. ESC 2023 adds that a permanent pacemaker is recommended only if high-degree block persists at least 5 days after MI (I, C), and pacing is not recommended once the block has resolved (III, B), because most post-MI block recovers."),
  ],
  mimic=[
    ("Mobitz I vs Mobitz II after MI", "Mobitz I (progressive PR lengthening) is nodal, inferior and benign; Mobitz II (fixed PR, sudden dropped beat) is infranodal, anterior and needs pacing."),
    ("Narrow vs wide escape in complete block", "Narrow escape at 40–60/min means a junctional pacemaker above the block (inferior); wide at under 40/min means a ventricular pacemaker below it (anterior)."),
  ],
  traps=[
    ("DocT GT keys “Mobitz I, benign, resolves with atropine” for block after an ANTERIOR MI", "The key contradicts its own explanation. Block after anterior MI is infranodal (LAD, His–Purkinje), does not respond to atropine and needs pacing: choose the His–Purkinje/transvenous pacing option."),
    ("“Anterior MI most commonly produces 2nd and 3rd degree block”", "Only 15% got this question right. Inferior MI causes more AV block of every degree, including complete block; anterior block is rarer but far more dangerous."),
    ("Two true options: “AV block transiently develops in 10–25%” and “inferior MI most commonly produces 1st and 2nd degree block”", "Both are true; the key is the transient-block statement, so pick it when both appear."),
    ("“Anterior MI gives a narrow-complex escape”", "Anterior block is below the His bundle, so the escape is wide."),
  ],
  decode=[
    ("Anterior MI with this ECG (block) — level and management? [DocT GT]", "His–Purkinje; transvenous pacing (key says Mobitz I/atropine, which is wrong)."),
    ("True statement about AV block in acute MI? [DocT GT]", "Transient AV block occurs in 10–25% (keyed); the inferior-MI statement is also true."),
    ("Inferior MI, complete heart block, narrow escape at 50/min, BP 70 — sequence? [pattern]", "Atropine/epinephrine, then temporary pacing; reperfuse if not already done."),
  ],
  punch="Inferior MI blocks the AV node: narrow escape, atropine works, it recovers. Anterior MI blocks the His–Purkinje system: wide escape, atropine fails, pace. If haemodynamics fail, chronotropes then a pacing wire then the cath lab, all Class I.",
)

L['MI-61'] = dict(
  sub="Cardiology → ACS → Acute heart failure in ACS",
  step=4,
  intro="Step 4 starts with the pump. Lost myocardium gives either congestion with a blood pressure, or low output with hypotension; the three real questions test the first-line move in each.",
  parts=[
    ('a', "**Diuretics, vasodilators, NIV.** In pulmonary oedema with a good or high blood pressure the problem is often redistribution into the lungs under high afterload, not excess total water. IV nitroglycerin reduces preload at low dose and afterload at high dose, works in minutes and is titratable; CPAP/NIV recruits flooded alveoli and lowers LV afterload. Loop diuretics help the overloaded but act more slowly."),
    ('b', "**Vasopressor for hypotension (norepinephrine); inotrope for output (dobutamine).** Norepinephrine raises perfusion pressure with less tachycardia and arrhythmia than dopamine (SOAP II, worse in the cardiogenic subgroup) and less refractory shock than epinephrine after MI (OptimaCC). Dobutamine is added when output stays low once pressure is restored. ESC grades both only IIb, because no inotrope or pressor has been shown to improve survival."),
    ('c', "**Longer stay, more mechanical ventilation, more RRT.** ESC 2023 links acute HF in ACS with renal failure, respiratory failure, pneumonia and death; Killip class rises with each step (I no HF; II S3 or rales <50% of the fields; III frank pulmonary oedema; IV shock), and so does mortality."),
    ('d', "**Pulmonary congestion; cardiogenic shock / low output / hypotension.** The first is ‘wet and warm’, the second ‘wet and cold’. Both need emergency echo and angiography (ESC 2023), because a mechanical complication or an occluded artery may be the cause."),
  ],
  mimic=[
    ("Hypertensive pulmonary oedema (SCAPE) vs cardiogenic shock", "High BP: nitrates and NIV, avoid pressors. Low BP and cold periphery: norepinephrine, then inotrope, revascularise; nitrates are contraindicated."),
  ],
  traps=[
    ("“Loop diuretic and wait” in BP 180/100 pulmonary oedema", "Too slow and aims at the wrong problem; 65% chose nitrates with NIV."),
    ("“Intubate now” in an alert patient with SpO₂ 88%", "Try NIV first; intubate for NIV failure, exhaustion or a falling GCS."),
    ("IV hydralazine or labetalol for hypertensive pulmonary oedema", "Hydralazine is unpredictable and causes reflex tachycardia; labetalol’s beta-blockade depresses a failing LV (94% chose nitroglycerin)."),
    ("“Dopamine” as the first vasopressor in post-MI shock", "76% chose norepinephrine. Dopamine causes more arrhythmia and was associated with higher mortality in cardiogenic shock."),
  ],
  decode=[
    ("Pink frothy sputum, BP 180/100, SpO₂ 88%, alert — next step? [DocT GT]", "Nitrates and NIV."),
    ("Hypertensive pulmonary oedema, BP 210/120 — initial drug? [DocT GT]", "IV nitroglycerin."),
    ("Post-MI cardiogenic shock — first-line vasopressor? [DocT GT]", "Norepinephrine."),
  ],
  extra=[dict(q="Killip class III vs IV? [Marrow line]", a="III is frank pulmonary oedema (rales over more than half the lung fields); IV is cardiogenic shock.")],
  punch="Congestion with a pressure gets nitrates and NIV (diuretic if overloaded); low output and hypotension gets norepinephrine first and dobutamine for output, then the artery opened. Each Killip class up raises mortality.",
)

L['MI-62'] = dict(
  sub="Cardiology → ACS → Cardiogenic shock in STEMI (ESC)",
  step=4,
  intro="Step 4 in classes. All three real questions ask the one thing that saves life in post-MI shock: opening the artery, by PCI even when the patient looks too sick.",
  parts=[
    ('a', "**Immediate PCI; emergency CABG if unsuitable / PCI fails: I, B.** Shock is a large ischaemic territory failing; only reperfusion stops it. In the SHOCK trial early revascularisation did not reach significance at 30 days but saved about 13 lives per 100 at 6 months. CULPRIT-SHOCK then showed that PCI of the culprit artery only, with any other lesions staged later, beat immediate multivessel PCI (ESC 2023: culprit-only at the index procedure, Class I)."),
    ('b', "**Arterial line, immediate Doppler echo, early heart-team repair of mechanical complications, O₂ / ventilation by gases: I, C.** The echo separates LV failure from RV infarction, tamponade, VSR and acute MR, each of which changes treatment."),
    ('c', "**Fibrinolysis if PPCI not possible <120 min (mechanical cause excluded): IIa, C.** Lysis works poorly at low perfusion pressure, but is better than no reperfusion when the lab is far."),
    ('d', "**IABP for shock from mechanical complications: IIa, C.** Deflating just before systole lowers afterload, which reduces the regurgitant or shunt fraction and improves forward flow while awaiting surgery."),
    ('e', "**PA catheter (IIb, B), ultrafiltration (IIb, B), inotropes / vasopressors (IIb, C), short-term MCS (IIb, C).** Each can be used but none has shown a survival benefit; ESC 2023 keeps short-term MCS at IIb, C, while ACC/AHA 2025 makes a microaxial flow pump IIa in selected STEMI shock (MI-63)."),
    ('f', "**Routine IABP: III, B.** IABP-SHOCK II (n 600) found no mortality benefit at 30 days, 1 year or 6 years."),
  ],
  mimic=[
    ("Shock from LV pump failure vs from a mechanical complication", "Pump failure: PCI ± MCS, no routine IABP. Mechanical complication (new murmur, tamponade): IABP is IIa as a bridge to surgery."),
    ("Inferior STEMI shock with clear lungs", "Think RV infarction: fluids, avoid nitrates, reperfuse."),
  ],
  traps=[
    ("“Immediate fibrinolysis” when PCI is available in 75 minutes", "Within 120 minutes primary PCI wins, and in shock even more so."),
    ("“Routine IABP” in STEMI shock", "Class III since IABP-SHOCK II; only for mechanical complications."),
    ("“Multivessel PCI at the index procedure” in shock (the notes call it IIa)", "CULPRIT-SHOCK: culprit-only first; stage the rest."),
  ],
  decode=[
    ("STEMI with cardiogenic shock, door-to-balloon 75 min — reperfusion strategy? [DocT GT]", "Primary PCI."),
    ("Treatment of choice: STEMI with cardiogenic shock? [Marrow]", "Revascularisation with PCI (I, B); routine IABP III."),
    ("Inferior STEMI with shock — next step? [Marrow]", "Primary PCI."),
  ],
  extra=[dict(q="Who gets shock after MI, and what predicts death? [Marrow line]", a="Older age, anterior MI, multivessel disease, prior MI, diabetes, prior HF; a first posterior or inferior infarct with shock suggests a mechanical complication or RV infarction. Lactate >2 mmol/L and admission glucose independently predict death.")],
  punch="In STEMI shock open the culprit artery now (PCI, or CABG if not feasible), echo immediately and fix any mechanical lesion; routine IABP is Class III, and drugs, PA catheters and MCS are only IIb.",
)

L['MI-63'] = dict(
  sub="Cardiology → ACS → MCS trial trail",
  step=4,
  intro="Step 4 through the trials. No real question is linked; the pattern is ‘which device improved survival in AMI shock’, and only one did, in one population.",
  parts=[
    ('a', "**IABP-SHOCK II (n 600): no 30-day mortality benefit (39.7% vs 41.3%).** The balloon adds only about 0.5 L/min, too little for a failing LV; no benefit at 1 or 6 years either."),
    ('b', "**ECLS-SHOCK (n 420): VA-ECMO — no 30-day benefit (47.8% vs 49.0%).** Full flow, but retrograde aortic flow raises LV afterload, and bleeding and vascular complications rose; most patients had been resuscitated from arrest before randomisation."),
    ('c', "**DANGER-SHOCK (n 360, STEMI shock): Impella CP — 180-day death 45.8% vs 58.5%, HR 0.74, NNT 8.** The microaxial pump takes blood from the LV and ejects it into the aorta, so it unloads the ventricle while adding flow. The population was narrow: STEMI with LVEF <45%, lactate ≥2.5 mmol/L and SBP <100 mmHg or a vasopressor; comatose out-of-hospital arrest survivors (GCS <8), severe RV failure and mechanical complications were excluded. 360 were randomised and 355 analysed."),
    ('d', "**More bleeding, limb ischaemia, RRT (safety composite RR 4.7).** The safety composite (severe bleeding, limb ischaemia, haemolysis, device failure, worsening aortic regurgitation) was 24.0% vs 6.2%; RRT was a separate outcome (41.9% vs 26.7%). A large-bore arterial sheath and pump haemolysis cost kidneys and limbs, so the benefit needs selection and an experienced centre."),
    ('e', "**Microaxial flow pump reasonable (IIa) in selected AMI shock; routine IABP / VA-ECMO not recommended.** ACC/AHA 2025 words the pump recommendation for STEMI with severe or refractory shock (2a, B-R), mirroring the DanGer Shock population, and gives routine IABP and routine VA-ECMO 3: No Benefit. ESC 2023, written before DanGer Shock, still gives short-term MCS IIb, C."),
  ],
  mimic=[
    ("Impella vs VA-ECMO", "Impella unloads the LV; VA-ECMO gives full flow but raises LV afterload and may need venting."),
  ],
  traps=[
    ("“IABP-SHOCK II showed benefit in resource-limited settings” (notes)", "It showed no benefit anywhere; the notes are wrong."),
  ],
  decode=[
    ("Which MCS device reduced mortality in STEMI cardiogenic shock in an RCT? [pattern]", "Impella CP (DanGer Shock)."),
    ("ECLS-SHOCK result? [pattern]", "No 30-day mortality benefit from routine VA-ECMO; more bleeding."),
  ],
  punch="IABP and VA-ECMO did not reduce death in AMI shock; Impella CP did, in carefully selected non-comatose STEMI shock, at the price of more bleeding, limb ischaemia and RRT.",
)

L['MI-64'] = dict(
  sub="Cardiology → ACS → The three ruptures",
  step=5,
  intro="Step 5 is the most asked card in the deck (seven real questions). Necrotic muscle is softest before collagen is laid down, so the wall, septum or papillary muscle can tear in the first days to a week; the presentation and the echo tell you which, and the stem’s wording (‘next’ vs ‘definitive’) decides between a bridge and surgery.",
  parts=[
    ('a', "**Presents: free wall — sudden pain + collapse, EMD; VSR — rapid AHF / shock, days 1–7; papillary — sudden pulmonary oedema ± shock.** Free wall rupture fills the pericardium in minutes, so the rhythm continues without output (PEA). VSR shunts left to right, flooding the lungs and starving the systemic circulation. Papillary rupture flails a mitral leaflet and the LV empties into a small, non-compliant left atrium."),
    ('b', "**Finding: haemopericardium, tamponade; new loud systolic murmur (VSR); murmur not always obvious, posteromedial muscle (papillary).** The posteromedial muscle depends on one artery (the PDA, usually from the RCA), so it ruptures after inferior or posterior MI; the anterolateral has a dual supply. In acute MR the LA pressure rises so fast that the murmur may be short and soft, so a quiet heart with flash pulmonary oedema still means echo. Echo also shows the VSR jet, and a step-up in oxygen saturation from right atrium to pulmonary artery confirms the shunt."),
    ('c', "**Manage: free wall — pericardiocentesis (bridge) → wall repair + patch; VSR — IABP bridge → surgery, percutaneous closure; papillary — diuretic, vasodilator / inotrope ± IABP → MVR / repair.** The IABP lowers afterload, which cuts the regurgitant and shunt fraction and raises forward flow without the extra afterload a vasopressor adds. Surgery is the definitive treatment for all three (ESC 2023: surgery preferred, IABP IIa, C while awaiting it; ACC/AHA 2025: short-term MCS as a bridge, 2a)."),
    ('d', "**Mortality: free wall 75–80%; VSR early surgery 20–40%; papillary 20–25%.** **Free wall rupture <1%; risk — older age, no reperfusion, late lysis.** For VSR the card’s figure is optimistic: registry operative mortality is about 54% when repair is within 7 days (MI-65). ESC 2023 puts all mechanical complications at 0.27% of STEMI with 42.4% in-hospital mortality; late lysis can turn an ischaemic infarct haemorrhagic and weaken it further."),
  ],
  table=dict(title="Reading the stem", head=["Clue", "Diagnosis", "Next step"], rows=[["PEA or sudden hypotension, pericardial effusion with tamponade", "**free wall rupture**", "pericardiocentesis as bridge, immediate surgery"], ["New loud holosystolic murmur, thrill, shock, O₂ step-up RA→PA", "**VSR**", "IABP/MCS, surgery or closure"], ["Flash pulmonary oedema, soft or new apical murmur, inferior/posterior MI", "**papillary muscle rupture (acute MR)**", "IABP (next), mitral surgery (definitive)"]]),
  mimic=[
    ("VSR vs papillary muscle rupture", "Both give a new systolic murmur and shock. VSR is loud with a thrill at the left sternal edge and an O₂ step-up; papillary MR is apical, often soft, with severe pulmonary oedema. Echo decides."),
    ("Free wall rupture vs post-MI pericarditis effusion", "Rupture gives sudden tamponade and PEA; pericarditis gives a small effusion and pleuritic pain."),
  ],
  traps=[
    ("“Norepinephrine” for inferior STEMI with a systolic murmur, pulmonary oedema and shock", "Only 38% chose IABP. A pressor raises afterload and worsens the regurgitant flow; the IABP lowers afterload and supports coronary perfusion, and is IIa for mechanical complications."),
    ("“Valve replacement” as the ‘next’ step for papillary rupture with pulmonary oedema", "Only 44% chose IABP. When IABP is offered and the stem says ‘next’, stabilise first; surgery is definitive."),
    ("“Diuretics and observe” or “vasodilator and reassess in 48 hours” for partial papillary rupture with hypotension", "62% chose urgent mitral surgery. Without an IABP option, the answer is urgent surgery; medical therapy alone is fatal."),
    ("“Pulmonary embolism” or “LV systolic dysfunction” for dyspnoea with a new apical holosystolic murmur after posterior MI", "69% chose acute MR; a new apical murmur with crackles and a preserved BP is papillary dysfunction until echo says otherwise."),
  ],
  decode=[
    ("PEA / sudden hypotension days after a large STEMI, echo shows tamponade or haemopericardium — cause? [DocT GT ×2]", "LV free wall rupture."),
    ("Post-MI flash pulmonary oedema, papillary muscle rupture on echo — next step? [DocT GT] [Marrow]", "IABP if offered as the next step; otherwise urgent mitral repair/replacement."),
    ("Posterior MI with new apical holosystolic murmur and crackles — mechanism of dyspnoea? [DocT GT]", "Acute mitral regurgitation."),
    ("Inferior STEMI, murmur, pulmonary oedema, cold and hypotensive — intervention? [DocT GT]", "Intra-aortic balloon pump."),
  ],
  punch="Sudden PEA with tamponade is free wall rupture; a new murmur with shock is VSR or papillary rupture, sorted by echo. Lower afterload with an IABP as the next step and send for surgery as the definitive one; avoid pressors that raise afterload.",
)

L['MI-65'] = dict(
  sub="Cardiology → ACS → VSR surgery timing",
  step=5,
  intro="Step 5 narrowed to the septum. No real question is linked; the testable point is the timing trade-off — early surgery sews into friable necrotic muscle, late surgery risks death while waiting.",
  parts=[
    ('a', "**Anterior or posterolateral MI (per notes).** Anterior MI (LAD) tears the apical septum, usually a simple defect; inferior MI (RCA/PDA) tears the basal inferior septum, a more complex defect often with RV infarction and a worse outcome. The usual pairing in guidelines and reviews is anterior and inferior."),
    ('b', "**Early surgery: high mortality (20–40%) — for refractory symptoms.** The necrotic edges hold sutures poorly before scar forms, so early repair carries higher mortality and residual leaks; a patient in refractory shock has no other option. The card’s figure is low: in the STS registry operative mortality was 54% when repair was within 7 days of MI and 18% after that, partly because the sickest are operated on first."),
    ('c', "**Late surgery: risk of rupture extension and death while waiting — if responding to therapy.** Delaying lets the edges fibrose and improves repair, but the defect can enlarge; this route is only for those stable on IABP or MCS and drugs."),
    ('d', "**Percutaneous closure.** A septal occluder device, used in selected anatomy, as a bridge or for residual defects after surgery."),
  ],
  mimic=[
    ("Apical (anterior MI) vs basal (inferior MI) VSR", "Apical is simpler to repair; basal is complex and carries a worse prognosis."),
  ],
  traps=[
    ("“Wait 4–6 weeks for every VSR”", "Only if the patient is stable; in refractory shock operate now despite the risk."),
  ],
  decode=[
    ("Post-MI VSR in refractory shock despite IABP — timing of surgery? [pattern]", "Emergency surgery."),
    ("Post-MI VSR stable on support — strategy? [pattern]", "Delayed surgery (or percutaneous closure) once the edges have scarred."),
  ],
  punch="Early VSR repair is a dangerous operation on soft tissue and is reserved for those who cannot wait; delayed repair is safer for the stable, provided the defect does not extend.",
)

L['MI-66'] = dict(
  sub="Cardiology → ACS → LV aneurysm",
  step=5,
  intro="Step 5 at the slow end. Instead of tearing, a transmural scar can thin and bulge, and it shows on the ECG as an ST elevation that never settles. The one real question (46% right) tests the Q wave, the permanent part of the scar.",
  parts=[
    ('a', "**<5% of AMI; anteroseptal / apical LV.** Large anterior transmural infarcts without timely reperfusion; with prompt PCI aneurysm has become uncommon."),
    ('b', "**Persistent ST elevation; Q waves.** The akinetic scar keeps the ST segment raised for weeks after the event, and the dead myocardium leaves Q waves. With no new pain and no new troponin rise, this is a fixed scar, not a new infarct (MI-27)."),
    ('c', "**LV thrombus (apex) → systemic embolism → long-term oral anticoagulation.** Stasis in the akinetic apex forms thrombus (over 9% after anterior STEMI). ESC 2023 says OAC (warfarin or a NOAC) ‘should be considered for 3–6 months’, guided by repeat echo or CMR, rather than indefinitely."),
    ('d', "**Large aneurysm, recurrent thromboembolism, mural / apical thrombus.** Aneurysmectomy is also considered for refractory heart failure or ventricular arrhythmias arising from the aneurysm."),
  ],
  mimic=[
    ("True aneurysm vs pseudoaneurysm", "A true aneurysm is a wide-necked bulge of scar that rarely ruptures; a pseudoaneurysm is a contained free wall rupture with a narrow neck, walled by pericardium, and needs surgery because it ruptures."),
    ("Old MI vs acute MI on ECG", "Q waves without ST elevation mean an old, healed infarct; ST elevation with symptoms or rising troponin is acute; persistent ST elevation with Q waves weeks later is aneurysm."),
  ],
  traps=[
    ("“Acute coronary syndrome” for Q waves in I, aVL and V5 with exertional dyspnoea", "Only 46% chose old MI. Q waves are permanent scar; acute ischaemia needs ST or T changes and a matching story."),
    ("“Re-infarction — reperfuse” for ST elevation weeks after an anterior MI", "Persistent ST elevation with deep Q waves and no new troponin rise is aneurysm."),
  ],
  decode=[
    ("Known CAD, fatigue, ECG with Q waves in I, aVL, V5 — diagnosis? [DocT QBank]", "Old (lateral) myocardial infarction."),
    ("ST elevation still present 6 weeks after an anterior MI — cause? [pattern]", "LV aneurysm."),
  ],
  extra=[dict(q="What makes a Q wave pathological? [DocT QBank]", a="The classic definition is at least 40 ms wide or deeper than 25% of the following R wave, in two or more contiguous leads. The Fourth Universal Definition uses a lower bar: Q ≥30 ms and ≥1 mm deep (in V2–V3, any Q over 20 ms or a QS complex) in two contiguous leads.")],
  punch="Persistent ST elevation with Q waves weeks after an anterior MI is an aneurysm, not a new infarct; its danger is apical thrombus and embolism, treated with oral anticoagulation (ESC: 3–6 months), and surgery is for the large or embolising aneurysm.",
)

L['MI-67'] = dict(
  sub="Cardiology → ACS → GRACE score",
  step=6,
  intro="Step 6 starts with grading the risk. No real question is linked; GRACE is tested through its cut-off of 140 and through the contrast with TIMI (MI-69).",
  parts=[
    ('a', "**Background: age, history of heart failure, history of AMI. Admission / stay: heart rate, systolic BP, ST depression, serum creatinine, elevated cardiac enzymes, no in-hospital PCI.** These are the nine variables of the post-discharge (6-month) nomogram. The original in-hospital GRACE model uses eight: age, heart rate, systolic BP, creatinine, Killip class, cardiac arrest at admission, ST deviation and raised enzymes. Each variable is weighted, so age and haemodynamics count far more than any single item."),
    ('b', "**6-month mortality after ACS.** The current calculator (GRACE 2.0) also gives in-hospital and 1-year figures."),
    ('c', "**GRACE >140 = high risk (early invasive, MI-43; discharge threshold, MI-32).** In NSTE-ACS, GRACE >140 is one of the high-risk features that call for angiography within 24 hours; below 140, with a negative rule-out and no pain, early discharge is acceptable."),
  ],
  mimic=[
    ("GRACE vs Killip", "Killip is a bedside HF class (one of GRACE’s in-hospital inputs); GRACE combines many variables into a mortality estimate."),
  ],
  traps=[
    ("“GRACE predicts 14-day events”", "That is TIMI; GRACE predicts death, here at 6 months."),
  ],
  decode=[
    ("NSTEMI, GRACE 160, stable — timing of angiography? [pattern]", "Early invasive, within 24 hours."),
  ],
  punch="GRACE weights nine variables into the risk of death at 6 months; above 140 the patient is high risk and goes for angiography within 24 hours.",
)

L['MI-68'] = dict(
  sub="Cardiology → ACS → TIMI score",
  step=6,
  intro="Step 6 with the simpler tool. No real question is linked; the test is usually the variables, especially aspirin use, which surprises people.",
  parts=[
    ('a', "**Age ≥65, ≥3 CAD risk factors, known CAD (stenosis ≥50%), aspirin in the last 7 days, ≥2 rest-angina episodes in 24 h, ST deviation, elevated cardiac markers.** Aspirin use counts because an ACS that breaks through aspirin marks a more aggressive, more thrombotic disease."),
    ('b', "**Death, new / recurrent MI, or urgent revascularisation through 14 days.** A short-term composite, not mortality at 6 months."),
    ('c', "**0–1 → 4.7%; 2 → 8.3%; 3 → 13.2%; 4 → 19.9%; 5 → 26.2%; 6–7 → 40.9%.** The risk climbs steeply with each point, which is why higher scores were linked to greater benefit from enoxaparin and an early invasive approach."),
  ],
  mimic=[
    ("TIMI UA/NSTEMI score vs TIMI STEMI score", "The STEMI score is a different, weighted tool for 30-day mortality; the seven one-point items are the UA/NSTEMI score."),
  ],
  traps=[
    ("“Aspirin use lowers the TIMI score”", "It adds a point."),
  ],
  decode=[
    ("Which is a TIMI UA/NSTEMI variable — aspirin in the last 7 days, heart rate, creatinine? [pattern]", "Aspirin in the last 7 days."),
  ],
  punch="TIMI gives one point for each of seven items, aspirin use included, and predicts death, MI or urgent revascularisation at 14 days, from 4.7% at 0–1 points to 40.9% at 6–7.",
)

L['MI-69'] = dict(
  sub="Cardiology → ACS → GRACE vs TIMI",
  step=6,
  intro="Step 6 as a comparison. No real question is linked; the classic slip is giving TIMI the 6-month figure that belongs to GRACE.",
  parts=[
    ('a', "**GRACE 9 variables; TIMI 7.**"),
    ('b', "**GRACE: weighted points → nomogram; TIMI: 1 point each (0–7).** Weighting makes GRACE more accurate, which is why ESC prefers it; TIMI is quicker at the bedside."),
    ('c', "**GRACE: mortality at 6 months; TIMI: death / MI / urgent revasc at 14 days.**"),
    ('d', "**GRACE: ESC risk group (>140), discharge in 0/3 h algorithm; TIMI: UA / NSTEMI stratification.**"),
  ],
  mimic=[
    ("Mortality endpoint vs composite endpoint", "GRACE predicts death alone; TIMI predicts a composite of death, MI and urgent revascularisation."),
  ],
  traps=[
    ("“TIMI predicts 6-month mortality” (the notes)", "6 months and mortality belong to GRACE; TIMI is a 14-day composite."),
  ],
  decode=[
    ("Score preferred by ESC for NSTE-ACS risk, with cut-off? [pattern]", "GRACE, >140 high risk."),
  ],
  punch="GRACE is weighted, nine variables, death at 6 months and the ESC tool; TIMI is seven one-point items and a 14-day composite.",
)

FLAGS = {
  'MI-56': "c: ‘follow-up echo for LVEF later’ is fine; the watch line is right that ESC now times the repeat LVEF at 6–12 weeks after revascularisation (the notes’ 3–6 weeks is older). The explanation gives 6–12 weeks.",
  'MI-57': "c: MRA ‘I, B’ is the ESC 2017 level; ESC 2023 Table 16 grades MRA for LVEF ≤40% with HF or diabetes I, A. ACE inhibitor (I, A selected / IIa, A all) and beta-blocker (I, A / IIa, B) are confirmed. Beta-blocker IIa for LVEF >40% is now contested (watch line correct); the explanation gives REDUCE-AMI, REBOOT, BETAMI-DANBLOCK and the 40–49% pooled analysis.",
  'MI-59': "c: ‘IV amiodarone for recurrent polymorphic VT I, C’ is ESC 2017 STEMI wording. ESC 2023 ACS merges it into ‘IV beta-blocker and/or amiodarone for polymorphic VT/VF’ (I, B); ESC 2022 VA says IV amiodarone ‘should be considered’ for recurrent haemodynamically relevant VA (IIa). f: ‘prophylactic antiarrhythmics III, B’ is also 2017 wording (ESC 2023 keeps only ‘asymptomatic, irrelevant VAs’ III, C; ESC 2022 says other AADs are not recommended). The explanation gives the current wording.",
  'MI-60': "a: ‘Proximal — 1st degree, Mobitz I’ and ‘Distal — 3rd degree’ is a simplification. Inferior MI also causes complete heart block (nodal, narrow escape, usually transient) and in absolute numbers more often than anterior MI; distal block includes Mobitz II and new bifascicular block. Both DocT GT keys are faulty (cardlayer cross): CGT4 keys Mobitz I/atropine for anterior MI (wrong), GT6 has two true options. Traps say so.",
  'MI-62': "e: the IIb list (PA catheter, ultrafiltration, inotropes/vasopressors) is ESC 2017 STEMI; ESC 2023 keeps short-term MCS IIb, C and IABP for mechanical complications IIa, C. ACC/AHA 2025 now makes a microaxial flow pump 2a in selected STEMI shock. Watch line on complete revascularisation is right (CULPRIT-SHOCK; ESC 2023 culprit-only at the index procedure).",
  'MI-63': "c: DanGer Shock randomised 360 and analysed 355; fine as written. d: ‘More bleeding, limb ischaemia, RRT (safety composite RR 4.7)’ reads as if RRT were in the composite; the composite was severe bleeding, limb ischaemia, haemolysis, device failure and worsening AR (24.0 vs 6.2%), and RRT was a separate outcome (41.9 vs 26.7%). e: ACC/AHA 2025 words the pump recommendation for STEMI (severe or refractory shock), not all AMI shock. Notes errors already listed in the watch line.",
  'MI-64': "Mortality row: ‘VSR early surgery 20–40%’ understates it; STS registry operative mortality was 54.1% for repair within 7 days of MI and 18.4% after (Arnaoutakis 2012). The explanation says so.",
  'MI-65': "a: ‘anterior or posterolateral’ (per notes) should read anterior or INFERIOR: anterior MI gives apical VSR, inferior MI basal inferoseptal VSR. b: early-surgery mortality ‘20–40%’ is low (STS 54% within 7 days). The explanation says both.",
  'MI-66': "c: ‘long-term oral anticoagulation’ is stronger than ESC 2023, which says OAC should be considered for 3–6 months once LV thrombus is found, guided by repeat imaging (IIa). The explanation keeps the card’s wording and states the guideline.",
  'MI-67': "a: the nine variables are the post-discharge 6-month GRACE nomogram (Eagle 2004); the in-hospital GRACE model (with Killip class and cardiac arrest, eight variables) is the one behind the >140 threshold. Not wrong; the explanation separates them.",
}
