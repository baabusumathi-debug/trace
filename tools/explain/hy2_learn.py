# HY2 — Explain v3 ("Learn" depth): high yield cardiology — tachyarrhythmias, bradycardia and devices, cardiac arrest and post-ROSC care, ACS and cardiogenic shock,
# anticoagulant reversal, vasopressors, pulmonary embolism, PA-catheter shock profiles, mechanical circulatory support, true/false sweep. No mnemonics or hooks.
# Driven by qpack/HY2.md (116 question links; CAR-25 shock profiles asked 30 times, CAR-21 anticoagulant reversal 21, CAR-02 SVT 9, CAR-18 cardiogenic shock 7, CAR-03 WPW 6,
# CAR-07 digoxin 5). CAR-12, CAR-24 and CAR-27 have no linked question and get short explanations with [pattern] decode items.
# Card layer (cvs_cardlayer.json "HY2|<code>") lines and cross notes read and agreed with; the one `fix` in trace/test/data/qbank.json (CAR-15: AHA 2025 dropped the SBP target) is applied and FLAGGED.
# Checked online on 19 Nov 2026:
#  - AHA 2025 Part 11 Post-Cardiac Arrest Care (cpr.heart.org): MAP ≥65 mmHg (COR 1), no SBP target any more; FiO₂ 100% until SpO₂ reliable, then SpO₂ 90–98% / PaO₂ 60–105 (2a);
#    PaCO₂ 35–45 (1); protocolised temperature control for ALL who do not follow commands, any rhythm or location (1), 32–37.5 °C (1), for at least 36 h (2a), rewarm no faster than 0.5 °C/h (2b),
#    no prehospital cold fluids (3); emergent angiography for ST elevation (1), reasonable for shock/recurrent VT/ongoing ischaemia (2a), not for the rest (3); routine seizure prophylaxis not
#    recommended (3); electrographic status epilepticus ≥10 continuous min or ≥20% of any 60 min (ACNS 2021); multimodal prognosis ≥72 h after normothermia and sedation off.
#  - AHA 2025 Part 9 Adult ALS: adrenaline 1 mg every 3–5 min; non-shockable as soon as feasible, shockable after initial defibrillation attempts fail (2a); amiodarone or lidocaine (2b);
#    vasopressin, routine calcium and bicarbonate no benefit (3); vector change and double sequential defibrillation usefulness not established (2b); magnesium for recurrent polymorphic VT (2b);
#    cardioversion AF ≥200 J (2a), flutter 200 J (2b); vagal manoeuvres and adenosine for regular narrow-complex tachycardia (1), lower adenosine dose may suffice via central line or
#    after heart transplant; pre-excited AF: digoxin, non-DHP CCB, β-blockers and IV amiodarone harmful (3). Bradycardia algorithm: atropine 1 mg every 3–5 min to 3 mg; dopamine
#    5–20 µg/kg/min, adrenaline 2–10 µg/min, transcutaneous pacing.
#  - AHA/AAP 2025 paediatric BLS: two-finger infant technique removed (heel of one hand or two-thumb encircling); with an advanced airway 20–30 breaths/min (1 every 2–3 s); AED for all
#    paediatric arrests, attenuator preferred under 8 years.
#  - ESC 2023 ACS: lysis if PPCI not possible within 120 min of diagnosis, bolus within 10 min; angiography 2–24 h after successful lysis; rescue PCI if <50% ST resolution at 60–90 min;
#    cardiogenic shock: immediate angiography and IRA PCI (I); fibrinolysis should be considered in STEMI + shock if PPCI not available within 120 min and mechanical complications excluded (IIa);
#    routine IABP not recommended.
#  - Trials: IABP-SHOCK II (30-day mortality 39.7 vs 41.3%), CULPRIT-SHOCK (death or RRT at 30 days 45.9 vs 55.4%), ECLS-SHOCK (30-day death 47.8 vs 49.0%), DanGer Shock (NEJM 2024; Impella CP in
#    STEMI shock, 180-day death 45.8 vs 58.5%, HR 0.74; composite safety 24.0 vs 6.2%, moderate or severe bleeding 21.8 vs 11.9%, limb ischaemia 5.6 vs 1.1%, RRT 41.9 vs 26.7%; ACC trial summary), SOAP II (dopamine more arrhythmias, worse in cardiogenic subgroup),
#    PEITHO (tenecteplase in intermediate-high PE: decompensation 1.6 vs 5.0%, death 1.2 vs 1.8% NS, haemorrhagic stroke 2.0 vs 0.2%, major bleeding 11.5 vs 2.4%), DOSE-VF.
#  - ESC 2019 acute PE remains the ESC guideline (no ESC replacement found); AHA/ACC 2026 acute PE guideline (Circulation, 24 Mar 2026) introduces clinical categories A–E (C1–C3 by RV and troponin,
#    D incipient failure/normotensive shock, E1 hypotension/shock, E2 refractory shock or arrest): systemic lysis harmful in A–C2, unclear in C3, may be considered in D, reasonable in E.
#  - Andexanet alfa: ANNEXA-I (NEJM 2024) haemostatic efficacy 67.0 vs 53.1%, thrombotic events 10.3 vs 5.6%, ischaemic stroke 6.5 vs 1.5%; US sales ended 22 Dec 2025 after an FDA safety
#    communication on post-marketing thrombosis (14.6 vs 6.9%; AABB news 23 Dec 2025); 4F-PCC is the US alternative for Xa-inhibitor bleeding.
#  - ESC 2024 AF: CHA₂DS₂-VA (sex removed); DOACs contraindicated with mechanical valves and moderate–severe rheumatic MS; 3 weeks of anticoagulation or TOE before elective cardioversion, 4 weeks after;
#    early cardioversion without prior anticoagulation or TOE not for AF lasting ≥24 h (the old threshold was 48 h; ACC/AHA 2023 keeps 48 h).
# Second (independent) review, 19 Nov 2026: AHA 2025 bradycardia algorithm (atropine 1 mg q3–5 min to 3 mg, dopamine 5–20 µg/kg/min, adrenaline 2–10 µg/min) and electrical cardioversion
#    algorithm (narrow 100 J, AF 200 J, flutter 200 J, monomorphic VT 100 J) confirmed on cpr.heart.org; AHA 2025 Part 9 text: 1 mg adenosine may be adequate via a central line or after
#    transplant. IABP-SHOCK II, CULPRIT-SHOCK (death alone 43.3 vs 51.6%), ECLS-SHOCK (bleeding 23.4 vs 9.6%, vascular 11.0 vs 3.8%), DOSE-VF (n 405) and REVERT (43 vs 17%) confirmed.
#    ESC 2023 ACS fondaparinux: I (NSTE-ACS without early angiography), III (STEMI during PPCI), IIa (with streptokinase); no separate class for non-reperfused STEMI.
#    CCB poisoning consensus: St-Onge, Crit Care Med 2017 (high-dose insulin first line with calcium and vasopressors; lipid second line).

SPINE = [
  ("Fast rhythms: shock or drug", "An unstable tachycardia gets synchronised electricity at once; a stable one is sorted by whether it uses the AV node, and the drug is chosen by the node, the accessory pathway, the strength of the ventricle and the QT."),
  ("Slow rhythms and devices", "Atropine works only where the vagus acts, so infranodal block and the denervated heart go straight to chronotropes and pacing; long term, EF and QRS width choose the ICD and CRT."),
  ("Arrest and after ROSC", "Survival comes from uninterrupted good compressions and early shocks, with drugs secondary; after ROSC the care protects the brain: MAP ≥65, normal oxygen and CO₂, temperature control, angiography for ST elevation."),
  ("ACS, shock and the drugs", "Time to PCI decides lysis or transfer, shock is revascularised and supported with noradrenaline and inotropes, and every anticoagulant has its own reversal agent."),
  ("PE, profiles and support", "In PE hypotension, not RV strain or troponin, decides lysis; on a PA catheter the RAP–PAWP pairing with CO and SVR names the shock; support devices are ranked by flow."),
]

PRIMER = "‘Unstable’ in any arrhythmia algorithm means the rate itself is causing hypotension, altered mentation, ischaemic chest pain, acute heart failure or shock; that, not the rate number, sends the patient to electricity. The AV node conducts decrementally (the faster it is driven, the slower it conducts), which protects the ventricles; an accessory pathway has no such brake, and drugs that slow the node act only on rhythms that pass through it. In arrest, coronary perfusion pressure (aortic diastolic minus right atrial pressure) is generated only by compressions and collapses within seconds of a pause. On a PA catheter, RAP (or CVP) reflects right-sided filling and PAWP left-sided filling; with cardiac output and SVR (MAP = CO × SVR) these four numbers separate the four kinds of shock."

L = {}

L['CAR-01'] = dict(
  sub="Cardiology → Tachyarrhythmias → Unstable AF: synchronised cardioversion",
  step=1,
  intro="The deck starts with the first fork of every tachycardia algorithm: is the patient unstable? Here fast AF has produced hypotension, crackles and hypoxaemia, so the rhythm is the cause of the shock and the question is how fast you can remove it.",
  parts=[
    ('a', "**Unstable tachycardia = synchronised cardioversion NOW. Immediate synchronised DC cardioversion; do not wait for TOE or 3 weeks of anticoagulation — give heparin, but shock first.** At 160/min the ventricle has too little diastole to fill, the atrial kick is gone, and output falls; the rise in left atrial pressure gives the crackles. A drug takes minutes to work and every rate-control drug (diltiazem, metoprolol) is a negative inotrope or vasodilator that lowers the pressure further; a shock works in one beat. The thrombo-embolic rules (3 weeks of anticoagulation or TOE to exclude left atrial thrombus) exist to protect stable patients from an elective procedure; in shock the risk of waiting is greater than the risk of a stroke, so heparin is started and the patient is shocked. Synchronisation times the shock to the R wave so it does not fall on the T wave and induce VF."),
    ('b', "**Biphasic energies (AHA 2025): flutter 200 J may be reasonable (COR 2b; older 50–100 J); AF ≥200 J (COR 2a; older 120–200 J); other narrow regular (SVT) 100 J (algorithm; older 50–100 J); monomorphic VT with pulse 100 J; polymorphic VT/VF unsynchronised = defibrillate.** AHA 2025 raised the starting energy for AF because the first shock succeeds more often at higher energy, and repeated failed shocks add nothing but delay; energy is then increased if the shock fails. Polymorphic VT cannot be synchronised (the machine cannot find a consistent R wave), so it is treated as VF."),
  ],
  mimic=[
    ("Unstable vs stable AF", "Unstable (hypotension, pulmonary oedema, ischaemia, altered mentation): cardiovert now. Stable: rate control, and anticoagulation rules (CAR-05b) before any elective cardioversion."),
    ("Sepsis-driven AF vs AF causing the shock", "In septic shock new AF is often a consequence; still, if the AF itself drops the pressure (BP falling with the onset of AF), the algorithm answer is cardioversion. Amiodarone is the stable or post-shock option."),
  ],
  traps=[
    ("“IV diltiazem or metoprolol to control the rate first”", "Both lower the BP further; with hypotension and crackles they can precipitate arrest. Only 48% chose cardioversion on the mini test."),
    ("“Heparin, then delayed cardioversion” or “TOE first”", "Thrombus rules apply to stable patients. In shock you anticoagulate and shock in the same minute."),
    ("“Synchronised cardioversion at 100 J” for AF (DocT QBank key)", "Cardioversion is the right choice and the key stands among its options; but AHA 2025 starts AF at ≥200 J. If the stem offers 200 J, take it."),
    ("“Amiodarone 150 mg bolus” in unstable post-operative AF (GT2o)", "A drug is the stable-patient path; with BP 73/34 the answer is synchronised cardioversion (87% got it)."),
  ],
  decode=[
    ("Irregular tachycardia 140, BP 70/40, basal crackles — first-line? [DocT QBank, 80% right]", "Synchronised cardioversion; not heparin, diltiazem or metoprolol."),
    ("Post-thoracotomy new AF 167/min, BP 73/34, onset 5 min ago [DocT GT, 87%]", "Synchronised cardioversion; amiodarone and procainamide are for stable patients."),
    ("Septic ICU patient, new AF 155, BP down to 90/60 [DocT GT]", "Immediate synchronised cardioversion (the key quotes 120–200 J, the pre-2025 AF range)."),
  ],
  punch="If the rate is causing the shock, cardiovert now with heparin on board and skip the TOE; AHA 2025 starts AF at 200 J or more and synchronises every shock except for polymorphic VT and VF.",
)

L['CAR-02'] = dict(
  sub="Cardiology → Tachyarrhythmias → Stable SVT: vagal, adenosine, verapamil",
  step=1,
  intro="Once the patient is stable, the question becomes which part of the conduction system the rhythm uses. A regular narrow tachycardia at 180 with no visible P waves is usually a circuit through the AV node, so anything that briefly blocks the node will break it — and anything it does not break reveals itself.",
  parts=[
    ('a', "**Vagal manoeuvres (modified Valsalva).** Vagal tone slows AV-nodal conduction and can interrupt a circuit that runs through the node. In REVERT the modified Valsalva (strain against 40 mmHg for 15 s semi-recumbent, then lie flat with the legs raised to 45° for 15 s) converted about 43% vs 17% with the standard manoeuvre; the leg raise adds venous return, which increases the vagal reflex after the strain. Carotid sinus massage is an alternative: supine, on ECG, one side only (right first) for 5–10 s, never with a carotid bruit or a recent TIA or stroke, because pressure can dislodge plaque."),
    ('b', "**Adenosine 6 mg rapid push + flush; then 12 mg (may repeat 12 mg once).** Adenosine acts on A1 receptors in the AV node, opening potassium channels and blocking conduction for a few seconds; its half-life is under 10 seconds, so it must reach the heart as a bolus, through a proximal vein with a fast flush. AHA 2025 notes that 1 mg may be enough via a central line or after heart transplant (the drug reaches the heart undiluted, and denervated receptors are supersensitive); dipyridamole and carbamazepine potentiate it, theophylline and caffeine blunt it. Warn the patient of a brief sense of doom, flushing and chest tightness."),
    ('c', "**IV verapamil (or diltiazem) — adenosine can trigger bronchospasm.** Adenosine acting on A1/A2B receptors in the airways can provoke bronchospasm in asthma; a non-dihydropyridine calcium channel blocker blocks the node through L-type calcium channels instead, with no airway effect. It is safe only with a normal ventricle and no pre-excitation (CAR-03, CAR-04)."),
    ('d', "**AVNRT — re-entry within the AV node (slow + fast pathways); P hidden in the QRS.** In typical (slow–fast) AVNRT the impulse goes down the slow pathway and up the fast one, so atria and ventricles are activated at the same time and the retrograde P wave is buried in, or just after, the QRS (pseudo-S in II, III, aVF; pseudo-r′ in V1). AVRT uses an accessory pathway, needs a longer loop and shows a separate retrograde P in the ST segment; a delta wave in sinus rhythm gives it away."),
  ],
  mimic=[
    ("AVNRT vs AVRT vs atrial tachycardia", "AVNRT: P hidden or just after QRS. AVRT: P clearly in the ST segment, delta wave between attacks. Atrial tachycardia: a distinct P before each QRS, unaffected by blocking the node."),
    ("Adenosine terminates vs adenosine unmasks", "Node-dependent rhythms (AVNRT, AVRT) stop. Atrial flutter and atrial tachycardia continue in the atria; ventricular slowing reveals flutter waves at about 300/min."),
  ],
  traps=[
    ("“Asthmatic with SVT — adenosine”", "Verapamil (or diltiazem) instead; only 7% chose it on the mini test."),
    ("“Stable SVT — adenosine 6 mg first”", "Vagal manoeuvres come first in a stable patient (only 50% in DocT QBank; 93–98% when asked plainly)."),
    ("“Re-entry via an accessory pathway” for retrograde P inverted in II, III, aVF at 180/min", "That P-wave picture is typical AVNRT, re-entry within the node (42% right in AIM1)."),
    ("“Take a deep breath before straining” (Marrow false statement)", "The manoeuvre is a sustained strain (40 mmHg for 15 s), not a deep inspiratory effort."),
  ],
  decode=[
    ("Stable narrow-complex tachycardia 180–190/min — first step? [DocT QBank 50%; DocT GT 93–98%]", "Vagal manoeuvres."),
    ("Regular 180, narrow, inverted P in II, III, aVF — mechanism? [DocT GT AIM1, 42%]", "Re-entry within the AV node (AVNRT)."),
    ("Adenosine 6 mg slows the rate and reveals sawtooth waves at 300/min [DocT GT]", "Atrial flutter with 2:1 conduction."),
    ("Carotid sinus massage — important contraindication? [DocT GT, 100%]", "Carotid bruit (or prior TIA/stroke)."),
  ],
  punch="Stable regular narrow tachycardia: modified Valsalva, then adenosine 6 then 12 mg as a fast push, verapamil if asthmatic; AVNRT hides its P wave in the QRS, and anything adenosine slows but does not stop is atrial.",
)

L['CAR-03'] = dict(
  sub="Cardiology → Tachyarrhythmias → WPW and pre-excited AF",
  step=1,
  intro="The AV node is the brake that protects the ventricles from fast atrial rhythms. In WPW a second, unbraked connection exists, and every rule about nodal blockers flips when AF runs down it.",
  parts=[
    ('a', "**Short PR, delta wave (slurred QRS upstroke), wide QRS.** The accessory pathway conducts without the nodal delay, so part of the ventricle is activated early (short PR, under 120 ms) and slowly through muscle (the slurred delta wave); the rest arrives through the normal system and the QRS is a fusion, hence wide."),
    ('b', "**Adenosine, verapamil, diltiazem, β-blockers, digoxin — blocking the AV node sends every AF beat down the accessory pathway → VF.** The node and the pathway compete for each atrial impulse; block the node and the pathway, which has a short refractory period and no decremental brake, takes all of them, at rates up to 300/min, which can degenerate into VF. Verapamil and digoxin also shorten the pathway’s refractory period. AHA 2023 and 2025 add IV amiodarone to the harmful list (COR 3), because its early effect is mainly nodal."),
    ('c', "**Unstable → cardioversion. Stable → procainamide (or ibutilide).** These drugs slow conduction or prolong refractoriness in the accessory pathway itself, so the ventricular rate falls without removing the competition. Definitive treatment is catheter ablation of the pathway."),
    ('d', "**Flecainide (class Ic) — blocks conduction in the accessory pathway.** A sodium channel blocker slows conduction in pathway tissue; ESC lists flecainide or propafenone as alternatives for pre-excited AF, and it is used to prevent AVRT. It is contraindicated with structural or ischaemic heart disease (CAST: excess deaths after MI). Its commonest dose-related non-cardiac effect is blurred vision, with dizziness (Marrow)."),
  ],
  mimic=[
    ("Pre-excited AF vs VT", "Pre-excited AF: irregularly irregular, broad complexes that vary in width beat to beat, rates up to 250–300 in a young person. VT: regular, uniform complexes."),
    ("Orthodromic AVRT vs pre-excited AF in WPW", "Orthodromic AVRT is regular and narrow (down the node, up the pathway): vagal manoeuvres and adenosine are allowed. The ban on nodal blockers applies to pre-excited AF (irregular and broad)."),
  ],
  traps=[
    ("“Verapamil is THE contraindicated drug” (DocT GT AIM1 Q36 / GT4 Q56, 45–54%)", "Verapamil is the classic answer to pick, but adenosine, esmolol and IV amiodarone in the same options are also harmful (AHA class 3); the item has more than one correct option."),
    ("“AV nodal dual pathway” for delta waves and short PR (GT4, 39%)", "Dual nodal pathways cause AVNRT and leave a normal ECG between attacks; a delta wave means an accessory AV pathway."),
  ],
  decode=[
    ("Delta wave, short PR, wide QRS in sinus rhythm — underlying abnormality? [DocT GT, 39% and 90%]", "Accessory AV pathway."),
    ("Known WPW, AF with rapid response — contraindicated drug? [DocT GT ×2, 45–54%]", "Verapamil (but adenosine, esmolol and IV amiodarone are also harmful)."),
    ("PR 100 ms and slurred QRS after rate control [DocT QBank, 77%]", "WPW syndrome."),
    ("Blurred vision during PSVT treatment — which drug? [Marrow]", "Flecainide."),
  ],
  punch="In pre-excited AF block the pathway, never the node: cardiovert if unstable, procainamide or ibutilide if stable, and no adenosine, verapamil, diltiazem, β-blocker, digoxin or IV amiodarone.",
)

L['CAR-04'] = dict(
  sub="Cardiology → Tachyarrhythmias → AF rate control with low EF",
  step=1,
  intro="Still in the stable tachycardia branch, the next variable is the ventricle. With an ejection fraction of 30% the output depends on the contractility left, so the drug that slows the rate must not also weaken the heart.",
  parts=[
    ('a', "**Verapamil, diltiazem — negatively inotropic; precipitate decompensation.** Non-dihydropyridine calcium channel blockers block L-type calcium channels in myocardium as well as in the node, so they reduce contractility; ESC advises against them when LVEF is below 40%. They should also not follow an IV β-blocker (additive block and hypotension), and they are banned in pre-excited AF (Marrow: diltiazem contraindicated in all three)."),
    ('b', "**Dronedarone — ↑ mortality in NYHA IV, recent decompensation, or permanent AF.** ANDROMEDA (recently decompensated, severe HF) and PALLAS (permanent AF) were stopped early for excess deaths, stroke and heart failure."),
    ('c', "**β-blocker (if not decompensated), digoxin, amiodarone.** A β-blocker is the long-term rate-control drug in HFrEF, but IV β-blockade in a patient who is acutely decompensated (wet, borderline pressure) can tip him into shock. Digoxin slows the node by raising vagal tone without negative inotropy, and amiodarone slows the rate with little effect on contractility; both are the acute choice when the patient is congested. Dobutamine speeds AV conduction and can provoke a fast ventricular rate in AF; giving digoxin first prevents it (Marrow)."),
  ],
  mimic=[
    ("Compensated vs decompensated HFrEF with AF", "Compensated: β-blocker. Decompensated (wet, low pressure): IV amiodarone or digoxin for rate, diuretic for congestion; no IV β-blocker or calcium channel blocker."),
  ],
  traps=[
    ("“Beta-blocker therapy” for AF 130 in HFrEF admitted with worsening dyspnoea (DocT QBank key, 39%)", "Disputed key: the patient is decompensating, so an IV β-blocker is avoided now; amiodarone or digoxin for rate and IV diuretic for congestion. A β-blocker is right once he is compensated."),
    ("“Dronedarone is fine for rhythm control in severe HF”", "It raises mortality in NYHA IV, recent decompensation and permanent AF; only 12% got it on the mini test."),
    ("“Verapamil is acceptable rate control with EF 30%”", "It is not recommended (only 24% got it); see CAR-27b."),
  ],
  decode=[
    ("Septic shock, AF 170, severe LV dysfunction, borderline BP — least suitable IV rate-control drug? [DocT GT]", "Verapamil."),
    ("HFrEF, AF with RVR, worsening dyspnoea, BP 110/70 [DocT QBank, 39%]", "Key: β-blocker; if decompensated, amiodarone or digoxin."),
    ("Low-EF AF developed RVR on dobutamine — what would have prevented it? [Marrow]", "Digoxin before dobutamine."),
  ],
  punch="With a weak ventricle, rate-control drugs must not depress contractility: no verapamil or diltiazem, no dronedarone in NYHA IV; use digoxin or amiodarone when decompensated, and a β-blocker once compensated.",
)

L['CAR-05'] = dict(
  sub="Cardiology → Tachyarrhythmias → AF anticoagulation and rate vs rhythm",
  step=1,
  intro="AF kills mostly through stroke, not through the rate. This card asks which anticoagulant, when it is safe to cardiovert, and whether controlling rhythm rather than rate changes the stroke risk.",
  parts=[
    ('a', "**Warfarin (INR 2–3; mechanical mitral 2.5–3.5). DOACs are contraindicated; aspirin is inadequate.** Moderate–severe rheumatic mitral stenosis stagnates blood in a large left atrium, and a mechanical valve adds a thrombogenic surface; DOAC trials excluded both, and in mechanical valves dabigatran (RE-ALIGN) caused more thrombosis and more bleeding than warfarin. For non-valvular AF the risk score decides: ESC 2024 uses CHA₂DS₂-VA (sex removed); in CHA₂DS₂-VASc, which the question tests, male sex scores 0 and the other items are heart failure 1, hypertension 1, age ≥75 2, diabetes 1, stroke/TIA 2, vascular disease 1, age 65–74 1, female sex 1."),
    ('b', "**3 weeks of anticoagulation, or TOE to exclude LA thrombus — then 4 weeks after.** Thrombus forms in the left atrial appendage after about 48 hours of AF, and a successful cardioversion can dislodge it; after cardioversion the atrium is stunned and contracts poorly for weeks, so anticoagulation continues for at least 4 weeks whatever the stroke score. ESC 2024 now sets the line at 24 hours: without prior anticoagulation or a TOE, early cardioversion is not advised once AF has lasted 24 hours or more (ACC/AHA 2023 keeps 48 hours)."),
    ('c', "**No difference in mortality, stroke or quality of life; rate control → fewer rehospitalisations.** In AFFIRM and RACE most strokes occurred in patients whose anticoagulation was stopped or subtherapeutic, so anticoagulation, not rhythm, decides stroke risk; rhythm control cost more admissions for cardioversion and drug toxicity. EAST-AFNET 4 (2020) later found that early rhythm control within a year of diagnosis lowered cardiovascular events, which is why current guidelines offer it earlier."),
  ],
  mimic=[
    ("Valvular vs non-valvular AF", "Valvular (moderate–severe MS or mechanical valve): warfarin only. Bioprosthetic valves, other native valve disease: DOACs allowed."),
  ],
  traps=[
    ("“Male sex scores a point in CHA₂DS₂-VASc”", "Female sex scores 1, male 0 (Marrow)."),
    ("“Dabigatran is acceptable in rheumatic MS with AF” (CAR-27c)", "Warfarin; only 36% chose it on the mini test."),
    ("“Rhythm control reduces stroke”", "AFFIRM/RACE: no difference; rate control’s only win was fewer readmissions (24% right)."),
  ],
  decode=[
    ("AF stroke-risk score does NOT include which factor? [Marrow]", "Male sex."),
    ("[pattern] AF of unknown duration, stable, planned cardioversion", "3 weeks of anticoagulation or TOE, then 4 weeks after."),
  ],
  punch="Rheumatic MS or a mechanical valve means warfarin, never a DOAC; stable AF over 48 h needs 3 weeks of anticoagulation or a TOE before cardioversion and 4 weeks after; rate versus rhythm does not change stroke.",
)

L['CAR-06'] = dict(
  sub="Cardiology → Tachyarrhythmias → Torsades, long QT and Brugada",
  step=1,
  intro="The last rhythm decision in step 1 is the QT. Polymorphic VT on a long QT is a repolarisation disease, so the drugs that treat ordinary VT make it worse; Brugada is a sodium-channel disease that kills at rest.",
  parts=[
    ('a', "**Magnesium sulphate 2 g IV; overdrive pacing or isoprenaline if recurrent; defibrillate if pulseless.** Torsades starts from early after-depolarisations during a prolonged plateau, driven by L-type calcium current; magnesium suppresses them even when serum magnesium is normal. Raising the heart rate (pacing at 90–110 or isoprenaline) shortens the QT and removes the pauses that trigger it. AHA 2025 gives magnesium as COR 2b. Correct potassium to the high-normal range."),
    ('b', "**Amiodarone, procainamide, sotalol — all prolong QT further.** Any class Ia or III drug lengthens repolarisation. In drug-induced torsades the treatment is to stop the drug (e.g. levofloxacin, and hold dofetilide until the QTc is normal); because the cause is reversible, no ICD is needed (Marrow)."),
    ('c', "**SCN5A loss of function (sodium channel). Coved ST elevation ≥2 mm with a NEGATIVE T in V1–V2.** Less sodium current in the right ventricular outflow epicardium lets the transient outward current dominate, producing the coved ST and the substrate for phase-2 re-entry. The type 1 pattern may be spontaneous or unmasked by fever or a sodium channel blocker (ajmaline, flecainide, procainamide challenge); a saddle-back ST with a positive T is not diagnostic."),
    ('d', "**At rest, sleep, fever. Treat fever aggressively; ICD for survivors.** High vagal tone and fever both reduce sodium current further, so VF strikes at night. An ICD is indicated after arrest and also after arrhythmic syncope (Marrow); quinidine (blocks the transient outward current) if an ICD is refused or for recurrent shocks, and isoprenaline for an electrical storm."),
  ],
  mimic=[
    ("Torsades (long QT) vs polymorphic VT with a normal QT", "Long QT: magnesium, pacing, stop QT drugs. Normal QT (usually ischaemia): treat ischaemia, amiodarone or β-blocker; urgent angiography."),
    ("Brugada vs CPVT", "Brugada: sodium channel, death at rest or in sleep, coved ST in V1–V2. CPVT: RyR2 calcium leak, death on exercise or emotion, normal resting ECG, bidirectional VT (CAR-07)."),
  ],
  traps=[
    ("“Positive T wave in the right precordial leads” as a Brugada feature", "The type 1 pattern has a negative T; only 57% knew it."),
    ("“Quinidine gives the greatest reduction in sudden death” for a Brugada arrest survivor", "An ICD does; quinidine is the adjunct."),
    ("“ICD for drug-induced polymorphic VT”", "Remove the cause; ICD only when there is no reversible cause."),
  ],
  decode=[
    ("Survivor of nocturnal arrest, normal heart, coved ST V1–V3 — greatest reduction in sudden death? [DocT GT]", "ICD implantation."),
    ("On IV amiodarone for AF, sudden syncope, torsades — which correction? [DocT GT, 91%]", "IV magnesium sulphate."),
    ("Brugada with recurrent syncope — best therapy? [Marrow]", "ICD."),
    ("Polymorphic VT on levofloxacin + dofetilide [Marrow]", "Stop levofloxacin, hold dofetilide until the QTc normalises; no ICD."),
  ],
  punch="Torsades is treated with magnesium, a faster rate and removal of QT-prolonging drugs; Brugada is SCN5A with coved ST and a negative T in V1–V2, kills at rest or with fever, and needs an ICD after arrest or arrhythmic syncope.",
)

L['CAR-07'] = dict(
  sub="Cardiology → Tachyarrhythmias → Digoxin toxicity",
  step=1,
  intro="Digoxin closes step 1 because it causes both fast and slow rhythms at once. The questions test the ECG, the antidote and the one laboratory value that predicts death.",
  parts=[
    ('a', "**Down-sloping ‘reverse tick’ ST in V4–V6, short QT, PAT with block, bidirectional VT, any brady/AV block.** The reverse tick and short QT are digoxin effect (at therapeutic levels too); toxicity shows as rhythms. Digoxin inhibits Na-K ATPase, raising intracellular sodium and so calcium (delayed after-depolarisations and ectopy), while raising vagal tone slows the SA and AV nodes; fast atria with a blocked node give atrial tachycardia with block, and alternating ventricular foci give bidirectional VT."),
    ('b', "**Peaked T waves — that is hyperkalaemia.** Digoxin flattens or inverts T waves and shortens QT; a peaked T means the potassium is high, which itself is a marker of severe acute poisoning (part d)."),
    ('c', "**Digoxin-specific Fab: life-threatening arrhythmia, K above 5–5.5 in acute toxicity, end-organ damage.** Fab fragments bind digoxin with higher affinity than Na-K ATPase, pulling it off the pump within 30–60 minutes; a typical empirical dose is about 10 vials in acute poisoning and fewer in chronic. Bradycardia can be bridged with atropine while Fab is given (Marrow); calcium is not needed for the hyperkalaemia because Fab corrects it, and it is avoided unless the potassium is immediately life-threatening."),
    ('d', "**Hyperkalaemia (acute poisoning blocks Na-K ATPase) — predicts death.** With the pump blocked, potassium cannot enter cells, so serum K rises in proportion to the poisoning. In the pre-Fab era (Bismuth 1973) a K above 5.5 mmol/L carried a very high mortality, a stronger predictor than the ECG or the digoxin level. In chronic toxicity it is the reverse: HYPOkalaemia (diuretics) increases digoxin binding and toxicity."),
  ],
  mimic=[
    ("Bidirectional VT: digoxin toxicity vs CPVT", "Digoxin: older patient on digoxin, GI symptoms, hyperkalaemia. CPVT: young, exercise- or emotion-triggered syncope, RyR2 or calsequestrin mutation; β-blockers (nadolol) first line, flecainide added, ICD reserved."),
  ],
  traps=[
    ("“High-degree AV block or a digoxin level >1 ng/mL portends a poor prognosis”", "Potassium >5.5 does (only 29% got it). The level is drawn too early in acute poisoning to mean much."),
    ("“Calcium gluconate first for K 5.8 on digoxin”", "Fab is the treatment (71% right); it corrects the potassium and the arrhythmia together."),
    ("“Beta-blockers are contraindicated” in exercise-induced bidirectional VT", "That is CPVT, where β-blockers are first line; this was the ‘except’ answer (42%)."),
  ],
  decode=[
    ("Digoxin, K 5.8, slow ventricular response with PVCs, confusion — initial step? [DocT QBank, 71%]", "Digoxin-specific antibody fragments."),
    ("Acute digoxin overdose — which feature portends a poor prognosis? [DocT GT, 29%]", "Serum potassium >5.5 mmol/L."),
    ("Young man, exercise syncope, bidirectional VT — all true EXCEPT [DocT GT, 42%]", "‘β-blockers contraindicated’ (they are first line)."),
    ("Drug of choice for severe digoxin toxicity [DocT GT PYQ]", "Digoxin immune Fab."),
  ],
  punch="Digoxin toxicity shows as ectopy plus block, bidirectional VT or atrial tachycardia with block; peaked T means hyperkalaemia, a K above 5.5 in acute poisoning predicts death, and Fab is the answer.",
)

L['CAR-08'] = dict(
  sub="Cardiology → Bradycardia → Atropine, chronotropes and pacing",
  step=2,
  intro="Step 2 turns to slow rhythms. Atropine is the first drug only because most symptomatic bradycardia is vagal and above the His bundle; the card teaches the doses and where that assumption fails.",
  parts=[
    ('a', "**Atropine 1 mg IV, repeat every 3–5 min.** Atropine blocks muscarinic receptors at the SA and AV nodes, lifting vagal tone. The 1 mg dose replaced the old 0.5 mg; doses below 0.5 mg can cause paradoxical slowing."),
    ('b', "**3 mg total.** At about 0.04 mg/kg the vagus is fully blocked, so more atropine adds only anticholinergic toxicity."),
    ('c', "**Dopamine 5–20 µg/kg/min, or adrenaline 2–10 µg/min, or transcutaneous pacing.** If atropine fails the problem is not vagal, so the next step acts directly on β₁ receptors or bypasses conduction with pacing. They are alternatives; while pacing is being set up, start an infusion. Isoprenaline is a direct β-agonist used in some settings (e.g. denervated heart) but is not in the AHA algorithm."),
    ('d', "**Mobitz II / complete heart block with wide QRS (infranodal), and the transplanted heart (denervated).** Below the AV node the His–Purkinje system has little vagal innervation, so atropine cannot help and can worsen the conduction ratio by speeding the sinus rate. A transplanted heart has no vagal supply: atropine, glycopyrrolate and indirect agents such as ephedrine fail, and atropine can even provoke high-grade block; use isoprenaline, adrenaline or pacing. Sinus node dysfunction early after transplant (up to half of patients) comes from surgical injury to the donor node and usually settles within weeks to 3 months."),
  ],
  mimic=[
    ("Vagal (nodal) vs infranodal bradycardia", "Nodal: narrow QRS, sinus brady or Mobitz I, responds to atropine. Infranodal: Mobitz II or CHB with wide escape, go straight to pacing."),
  ],
  traps=[
    ("“Administer more atropine” after three 1 mg doses (GT2o, 35%)", "3 mg is the maximum; next is dopamine or adrenaline while pacing comes."),
    ("“Isoproterenol” or “noradrenaline” while waiting for pacing (GT2o)", "Dopamine is the algorithm answer; noradrenaline adds afterload with little chronotropy."),
    ("“Adrenaline 2–10 µg/kg/min”", "It is 2–10 µg/min (34% right); dopamine is the one dosed per kg."),
  ],
  decode=[
    ("Post-CABG pericarditis, HR 33, BP 62/36, three doses of atropine, waiting for TCP [DocT GT, 35%]", "Dopamine infusion."),
    ("Heart transplant 3 years ago, intraoperative bradycardia — best drug? [Marrow]", "Isoprenaline (direct-acting)."),
  ],
  punch="Atropine 1 mg every 3–5 min to 3 mg, then dopamine 5–20 µg/kg/min, adrenaline 2–10 µg/min or pacing; atropine is useless below the node and in the denervated heart.",
)

L['CAR-09'] = dict(
  sub="Cardiology → Bradycardia → Pacing decisions and paediatric bradycardia",
  step=2,
  intro="Once atropine is set aside, the question is how quickly to pace. The level of the block decides it in adults; in children the cause (hypoxia) changes the whole response.",
  parts=[
    ('a', "**Permanent pacemaker — His–Purkinje disease, high risk of complete block and sudden death.** Mobitz II (constant PR, sudden dropped beat) is infranodal; it progresses unpredictably to complete heart block with a slow, unreliable ventricular escape. With symptoms and no reversible cause (drugs, ischaemia, hyperkalaemia) it needs a permanent pacemaker."),
    ('b', "**Pacing (transcutaneous now, transvenous next); chronotropes as a bridge.** In an unstable infranodal block transcutaneous pacing is the immediate step; it is uncomfortable and capture must be confirmed by a pulse, so transvenous pacing follows. Atropine rarely helps and must not delay pacing; dobutamine is not the rescue."),
    ('c', "**Start CPR and give adrenaline 0.01 mg/kg IV/IO (max 1 mg).** In children bradycardia is usually the last stage of hypoxia; heart rate below 60 with poor perfusion despite good oxygenation and ventilation behaves as an impending arrest, so compressions start. Adrenaline 0.01 mg/kg is 0.1 mL/kg of 0.1 mg/mL. Atropine (0.02 mg/kg) is only for increased vagal tone or primary AV block."),
  ],
  mimic=[
    ("Adult vs child bradycardia with poor perfusion", "Adult: atropine, chronotropes, pacing. Child: oxygenate and ventilate first; if HR still <60 with poor perfusion, CPR and adrenaline."),
  ],
  traps=[
    ("“Transvenous pacemaker placement” as the initial intervention for unstable Mobitz II (GT4, 43%)", "Transcutaneous pacing first, as the bridge; transvenous takes time."),
    ("“Atropine” for unstable Mobitz II", "It acts on the node, not below it."),
    ("“Atropine or dopamine” for the child with HR 46 and poor perfusion", "CPR and adrenaline (22% right)."),
  ],
  decode=[
    ("Septic ICU patient, syncope, Mobitz II on strip, BP 75/40 — initial intervention? [DocT GT, 43%]", "Transcutaneous pacing."),
  ],
  punch="Symptomatic Mobitz II needs a permanent pacemaker and, if unstable, transcutaneous pacing now; a child with HR below 60 and poor perfusion despite oxygen and ventilation gets CPR and adrenaline 0.01 mg/kg.",
)

L['CAR-10'] = dict(
  sub="Cardiology → Devices → ICD and CRT in heart failure",
  step=2,
  intro="The long-term end of step 2: which patients with a weak heart get a device. The ICD prevents arrhythmic death; CRT treats the electrical delay that makes the ventricle contract out of step.",
  parts=[
    ('a', "**LVEF ≤35%, NYHA II–III, on GDMT ≥3 months, more than 40 days after MI (90 after revascularisation).** These criteria come from MADIT-II and SCD-HeFT; three months of therapy lets the EF recover first, and early ICDs after MI (DINAMIT, IRIS) did not lower mortality because early deaths are often non-arrhythmic. NYHA IV patients are excluded unless they are CRT candidates, since they die of pump failure. A survivor of VF/VT arrest without a reversible cause is a different decision: a secondary-prevention ICD, whatever the EF (AVID, CIDS, CASH: ICD beat amiodarone)."),
    ('b', "**QRS width — LBBB with QRS ≥150 ms (plus EF ≤35%).** Left bundle branch block makes the septum contract before the lateral wall, wasting work; pacing both ventricles resynchronises them. Benefit is greatest with LBBB and QRS ≥150 ms (class I); between 130 and 149 ms it is weaker; under 130 ms CRT does not help and may harm (EchoCRT)."),
    ('c', "**Echo mechanical dyssynchrony, tissue Doppler, or EF alone.** Trials selecting by echo measures (PROSPECT, EchoCRT) failed: the measures were unreproducible and narrow-QRS patients did not benefit."),
  ],
  mimic=[
    ("Primary vs secondary prevention ICD", "Primary: no prior event, EF ≤35% on optimal therapy, >40 days after MI. Secondary: survived VF/VT arrest or haemodynamically unstable VT with no reversible cause, regardless of EF."),
  ],
  traps=[
    ("“Amiodarone for secondary prevention” after a resuscitated arrest with EF 30%", "ICD evaluation; ICD beats amiodarone on mortality (71% right in GT3)."),
    ("“Echo dyssynchrony selects for CRT”", "QRS width does (26% right)."),
  ],
  decode=[
    ("Resuscitated OHCA, no MI, LVEF 30% — next step to reduce long-term mortality? [DocT GT, 71%]", "Refer for ICD."),
    ("Dilated cardiomyopathy, QRS 180 ms, LBBB — diagnosis? [DocT QBank, 84%]", "HFrEF (the CRT candidate)."),
  ],
  punch="Primary-prevention ICD needs EF ≤35% on 3 months of therapy and more than 40 days after MI; arrest survivors get one regardless of EF; CRT is chosen by QRS width (LBBB ≥150 ms), not by echo.",
)

L['CAR-11'] = dict(
  sub="Cardiology → Arrest → Adult BLS sequence",
  step=3,
  intro="Step 3 starts at the collapse. The BLS sequence is built around one physiological fact: coronary perfusion during arrest exists only while someone is compressing, so every step is ordered to get compressions and a shock going and keep them going.",
  parts=[
    ('a', "**Scene safe → check responsiveness → shout for help, activate the emergency system, send for the AED → then check breathing and pulse together, ≤10 s → no pulse: CPR 30:2, attach the AED as soon as it arrives.** Help and the AED come before the pulse check because the commonest early shockable rhythm needs a defibrillator, and a lone rescuer cannot fetch it later without stopping CPR. Pulse checks by professionals are unreliable, so the check is limited to 10 seconds; gasping (agonal breathing) is not normal breathing and counts as arrest."),
    ('b', "**Pulse but abnormal breathing → 1 breath every 6 s, recheck pulse every 2 min.** That is 10 breaths a minute, enough to oxygenate without raising intrathoracic pressure and cutting venous return; consider naloxone if opioids are suspected. If the pulse is lost, start CPR."),
    ('c', "**‘No shock advised’ → resume CPR immediately for 2 min. No pulse check.** After any analysis or shock, compressions resume at once; a pause to feel for a pulse lowers coronary perfusion pressure, which takes many compressions to rebuild, and a rhythm that has just changed rarely produces a palpable pulse in the first seconds anyway."),
  ],
  mimic=[
    ("Respiratory arrest vs cardiac arrest", "Definite pulse, gasping: rescue breathing 1 every 6 s. No definite pulse in 10 s: CPR 30:2."),
  ],
  traps=[
    ("“Begin 30:2” when a definite pulse is present with gasping", "Rescue breathing only, 1 breath every 6 s (CGT2, CGT5)."),
    ("“Check pulse first” or “repeat shock” after one shock for VF", "Resume CPR for 2 minutes (CGT5)."),
    ("“Check breathing and pulse, then shout for help”", "Help and AED first (63% right on the mini test)."),
  ],
  decode=[
    ("Unresponsive, definite carotid pulse, only gasping — next step? [DocT GT]", "1 breath every 6 s, reassess pulse every 2 min."),
    ("Collapse in ICU, apnoeic with gasps, no definite pulse in 10 s [DocT GT]", "Start CPR."),
    ("AED shows VF, one shock delivered — next action? [DocT GT]", "Resume CPR for 2 min."),
  ],
  punch="Shout and send for the AED before checking breathing and pulse for 10 s; with a pulse but abnormal breathing give 1 breath every 6 s, and after any analysis or shock resume CPR straight away for 2 minutes.",
)

L['CAR-12'] = dict(
  sub="Cardiology → Arrest → CPR numbers (AHA 2025)",
  step=3,
  intro="The numbers of CPR follow the cause of arrest: adults usually arrest from a cardiac rhythm with oxygen still in the blood, children usually from hypoxia.",
  parts=[
    ('a', "**30:2, one or two rescuers.** In adult arrest the blood is still oxygenated for the first minutes, so compressions matter more than breaths."),
    ('b', "**One rescuer 30:2; two rescuers 15:2 (pre-pubertal).** Paediatric arrest is mostly asphyxial, so with two rescuers the extra breaths are worth the extra pauses; a lone rescuer keeps 30:2 to limit the time changing between tasks."),
    ('c', "**Continuous compressions; adult 1 breath every 6 s, child/infant every 2–3 s.** With an advanced airway compressions no longer pause; AHA 2025 gives 20–30 breaths/min for infants and children."),
    ('d', "**Heel of one hand, or two-thumb encircling — the two-finger technique was removed.** Two fingers rarely reach one third of the chest depth (about 4 cm in infants)."),
    ('e', "**Attach immediately; paediatric pads/attenuator if available, else adult pads (not touching).** AHA 2025: an attenuator is preferred under 8 years, but a standard AED is better than none."),
  ],
  mimic=[],
  traps=[
    ("“8-year-old, one healthcare provider — 15:2”", "One rescuer is 30:2 at any age; 15:2 needs two rescuers (71% right)."),
  ],
  decode=[
    ("[pattern] Infant arrest, two rescuers — ratio and technique?", "15:2, two-thumb encircling (or heel of one hand); not two fingers."),
    ("[pattern] Child with advanced airway in CPR — ventilation rate?", "1 breath every 2–3 s (20–30/min) with continuous compressions."),
  ],
  punch="Adults 30:2 whatever the number of rescuers; children 30:2 alone and 15:2 with two; with an airway 1 breath every 6 s in adults and every 2–3 s in children; the two-finger infant technique is gone.",
)

L['CAR-13'] = dict(
  sub="Cardiology → Arrest → Arrest drugs",
  step=3,
  intro="Drugs come after compressions and shocks in the arrest algorithm, and their timing differs by rhythm for a reason: in VF the shock is the treatment, in PEA and asystole there is nothing to shock.",
  parts=[
    ('a', "**Adrenaline 1 mg after the 2nd shock, every 3–5 min. Amiodarone 300 mg, then 150 mg (or lidocaine 1–1.5 mg/kg, then 0.5–0.75).** AHA 2025 words it as adrenaline ‘after initial defibrillation attempts have failed’ (2a), and amiodarone or lidocaine as COR 2b (ALPS: survival to admission higher, no significant difference in survival to discharge). Lidocaine, a class Ib drug, acts only on ventricular tissue: its sodium-channel block depends on the long ventricular action potential, so it is useless in AF (Marrow)."),
    ('b', "**Adrenaline 1 mg as soon as possible, every 3–5 min. No shock, no amiodarone.** Adrenaline’s α effect raises aortic diastolic pressure and so coronary perfusion pressure; in non-shockable arrest earlier adrenaline is linked to more ROSC and survival (PARAMEDIC-2, all rhythms: better 30-day survival, but more survivors with severe neurological disability)."),
    ('c', "**Adrenaline 0.01 mg/kg; amiodarone 5 mg/kg; lidocaine 1 mg/kg.** Amiodarone may be repeated up to three doses in children."),
    ('d', "**CPR quality (depth, rate, recoil, pauses under 10 s) and standard shocks. Vector change / double sequential defibrillation: usefulness not established (AHA 2025, COR 2b; one trial, DOSE-VF).** DOSE-VF (2022) found more survival to discharge with double sequential (30.4%) and vector change (21.7%) than standard shocks (13.3%), but it was a single, small trial, so AHA 2025 left both at 2b. Vasopressin, routine calcium and routine bicarbonate add nothing (COR 3)."),
  ],
  mimic=[
    ("Shockable vs non-shockable: when adrenaline", "Shockable: after the second shock (failed initial defibrillation). Non-shockable: as soon as possible."),
  ],
  traps=[
    ("“Shock or amiodarone” in PEA at 76/min with no pulse", "Adrenaline 1 mg (61% right); PEA is never shocked."),
    ("“No amiodarone available — procainamide”", "Lidocaine is the alternative (65%)."),
    ("“Paediatric lidocaine 0.1 mg/kg”", "1 mg/kg (51%)."),
  ],
  decode=[
    ("AF on ECG — which drug cannot be used? [Marrow]", "Lignocaine (class Ib, ventricular only)."),
  ],
  punch="Shockable: adrenaline 1 mg after the second shock and amiodarone 300 then 150 mg or lidocaine; non-shockable: adrenaline as soon as possible; in refractory VF CPR quality matters most, and double sequential shocks remain unproven (2b).",
)

L['CAR-14'] = dict(
  sub="Cardiology → Arrest → Special circumstances: the extra drug",
  step=3,
  intro="In some arrests the standard algorithm cannot work because a drug or toxin blocks the pathway that adrenaline uses. Each extra drug here bypasses or removes that block.",
  parts=[
    ('a', "**Glucagon 1–5 mg IV — plus fluids. Not IM adrenaline in arrest; not sugammadex as monotherapy.** Glucagon acts on its own G-protein receptor and switches on adenylate cyclase directly, raising cAMP even when β-receptors are blocked; it is given slowly (it causes vomiting) and can be followed by an infusion. In arrest, adrenaline is IV, not IM. Sugammadex does not treat rocuronium anaphylaxis by itself. In β-blocker poisoning glucagon is the classic drug of choice, but many toxicologists now put high-dose insulin first, as the calcium channel blocker consensus does (St-Onge, Crit Care Med 2017)."),
    ('b', "**Calcium, high-dose insulin, vasopressors; lipid emulsion if refractory.** Calcium overcomes the channel block in part; high-dose insulin (1 U/kg bolus, then infusion, with glucose) restores myocardial carbohydrate use, which the poisoned heart depends on; lipid emulsion is reserved for refractory cases."),
    ('c', "**20% lipid emulsion 1.5 mL/kg bolus.** Then 0.25 mL/kg/min, repeat the bolus for persistent instability, to a maximum of about 12 mL/kg. Lipid pulls lipophilic bupivacaine out of the heart and supplies fatty acids. Run standard ALS alongside, with smaller adrenaline doses (≤1 µg/kg); propofol is not a substitute."),
    ('d', "**Naloxone — but never ahead of compressions.** In an opioid arrest the heart has stopped from hypoxia; naloxone may help a patient with a pulse but does not restart a heart, so CPR and ventilation come first."),
  ],
  mimic=[
    ("Glucagon vs high-dose insulin in β-blocker or CCB poisoning", "Glucagon bypasses the β-receptor; high-dose insulin is the stronger inotrope in both and is first line in the calcium channel blocker consensus."),
  ],
  traps=[
    ("“More adrenaline or noradrenaline” for β-blocker shock unresponsive to catecholamines", "Glucagon (37% right on the mini test); catecholamines need the receptor that is blocked."),
    ("“Epinephrine or bicarbonate” as drug of choice in bupivacaine arrest", "Lipid emulsion."),
  ],
  decode=[
    ("Chronic β-blocker, profound bradycardia and shock despite fluids and catecholamines — DOC? [DocT GT PYQ]", "Glucagon."),
    ("Seizures then bradycardia and arrest after bupivacaine nerve block — DOC? [DocT GT PYQ]", "Lipid emulsion."),
  ],
  punch="Glucagon bypasses β-blockade by activating adenylate cyclase directly; CCB poisoning needs calcium and high-dose insulin; local anaesthetic arrest needs 20% lipid 1.5 mL/kg; naloxone never comes before compressions.",
)

L['CAR-15'] = dict(
  sub="Cardiology → Post-ROSC → Targets for the comatose survivor",
  step=3,
  intro="After ROSC the heart has restarted, but the outcome is decided by the brain. Every target on this card protects a brain that has lost autoregulation and is primed for secondary injury.",
  parts=[
    ('a', "**MAP ≥65, SBP ≥90 mmHg.** Without autoregulation, cerebral flow follows pressure, so hypotension adds ischaemia. AHA 2025 now gives only MAP ≥65 mmHg (COR 1) and has dropped the SBP target; no particular vasopressor is recommended. Higher MAP targets (BOX, NEUROPROTECT) did not improve outcome."),
    ('b', "**SpO₂ 90–98% (PaO₂ 60–105); PaCO₂ 35–45.** 100% oxygen until saturation can be measured reliably, then titrate down: hypoxaemia kills neurons, while hyperoxia adds free radicals at reperfusion. Low CO₂ constricts cerebral vessels and reduces flow; high CO₂ raises ICP. Pulse oximetry can overestimate in darker skin."),
    ('c', "**32–37.5 °C, any rhythm, any location; at least 36 h (2025); rewarm no faster than 0.5 °C/h; prevent fever.** TTM-2 found no difference between 33 °C and normothermia with active fever prevention, so the range is wide; what matters is avoiding fever, which increases neuronal death. It applies to every patient who does not follow commands, including PEA, asystole and in-hospital arrest. Rewarming is slow because a fast rise raises cerebral metabolic demand while oxygen delivery is still fragile, and causes vasodilatory hypotension and rebound hyperkalaemia as potassium moves out of cells. An automated device at about 0.25 °C/h takes about 16 hours for 4 °C; manual rewarming takes about 24 hours (Marrow)."),
    ('d', "**Seizure ≥10 min continuous, or seizures for ≥20% of any 60 min.** This is the ACNS 2021 definition of electrographic status epilepticus. AHA 2025: prompt EEG in all who do not follow commands; treat clinical seizures; no routine prophylaxis. Status epilepticus persisting at or beyond 72 h, burst suppression off sedation, bilaterally absent pupillary and corneal reflexes at ≥72 h, absent N20 SSEPs and high NSE support a poor outcome, only in a multimodal assessment at least 72 hours after normothermia."),
    ('e', "**STEMI, or cardiogenic shock / suspected coronary cause — not everyone.** Emergent angiography for ST elevation (COR 1); reasonable for shock, recurrent ventricular arrhythmias or ongoing ischaemia (2a). For comatose patients without these, COACT and TOMAHAWK found no benefit from immediate angiography over a delayed approach (COR 3)."),
  ],
  mimic=[
    ("Post-arrest rewarming vs accidental hypothermia afterdrop", "Post-arrest: slow rewarming to protect the brain. Afterdrop (core temperature falling as cold peripheral blood returns) belongs to accidental hypothermia."),
  ],
  traps=[
    ("“Strict 32–34 °C” or “PEA excluded from temperature control”", "Outdated: 32–37.5 °C for all comatose patients, any rhythm (GT4 Q60)."),
    ("“36 °C for 12 h”", "At least 36 hours of temperature control (the GT4 miss)."),
    ("“Slow rewarming prevents a fall in potassium and post-rewarming diuresis”", "Rewarming RAISES potassium; the main reason is cerebral metabolic demand outstripping delivery (only 45% chose that)."),
    ("“No upper-limb motor response always means a poor outcome”", "Absent or extensor arm response is of uncertain value; arms weak with legs moving may be a watershed (man-in-a-barrel) injury, and a short arrest can recover fully."),
  ],
  decode=[
    ("Rationale for slow controlled rewarming after therapeutic hypothermia [DocT QBank, 45%]", "Rapid rewarming abruptly raises cerebral metabolic demand → secondary brain injury."),
    ("Post-arrest coma: finding most specific for poor prognosis [Marrow]", "Status epilepticus during active cooling (with other signs, at ≥72 h)."),
    ("Rewarming 33 → 37 °C with ice packs, no automated device — timeframe? [Marrow]", "About 24 hours."),
    ("Revived after 20 min arrest — NOT true [Marrow]", "‘No upper-limb motor response always means poor outcome’."),
  ],
  punch="After ROSC keep MAP ≥65, SpO₂ 90–98% and PaCO₂ 35–45, control temperature at 32–37.5 °C for at least 36 h in every comatose patient, rewarm at ≤0.5 °C/h, and take only STEMI or shock straight to the lab.",
)

L['CAR-16'] = dict(
  sub="Cardiology → Arrest → ECMO configurations",
  step=3,
  intro="When neither the heart nor CPR can maintain flow, ECMO takes over. The configuration follows which organ has failed: VV supports the lungs and relies on the patient’s heart; VA replaces the heart as well.",
  parts=[
    ('a', "**VA-ECMO. (‘Arteriovenous ECMO’ is not a mode.)** In refractory arrest there is no cardiac output to carry blood oxygenated in a vein, so blood must be returned into the arterial tree. ECPR is usually femoro-femoral, started within about 60 minutes of collapse in selected witnessed arrests."),
    ('b', "**VV-ECMO.** Blood is drained from and returned to the venous system; the native heart pumps the oxygenated blood through the lungs and body."),
    ('c', "**VA-ECMO — the only percutaneous device giving full heart + lung support (up to ~7 L/min).** Biventricular failure and fulminant myocarditis need both ventricles replaced, and VA-ECMO is the fastest route; it works in any rhythm, even VF."),
    ('d', "**Convert to VA (or V-AV).** If cardiogenic shock develops on VV, the heart can no longer move the oxygenated blood; adding an arterial return cannula (V-AV) or converting to VA provides circulatory support."),
    ('e', "**↑ LV afterload → LV distension, pulmonary oedema → vent the LV (Impella, IABP).** Retrograde arterial flow up the aorta pushes against the aortic valve. A weak LV that cannot open it distends, its wall stress and oxygen demand rise, pulmonary oedema worsens and the stagnant blood can clot; an Impella or IABP unloads it. Routine VA-ECMO in infarct-related shock did not lower 30-day mortality in ECLS-SHOCK (47.8% vs 49.0%) and caused more moderate or severe bleeding (23.4% vs 9.6%) and vascular complications (11.0% vs 3.8%)."),
  ],
  mimic=[
    ("VV vs VA", "VV: lungs only, heart must work, no haemodynamic support. VA: heart and lungs, but raises LV afterload."),
  ],
  traps=[
    ("“ECPR uses VV-ECMO” (CAR-27h)", "VA; with no cardiac output, venous return of oxygenated blood goes nowhere (GT4 Q72 lost)."),
    ("“VA-ECMO lowers LV afterload”", "It raises it (43% right)."),
  ],
  decode=[
    ("Severe ARDS with cardiogenic shock after MI — preferred device? [DocT GT, 88%]", "VA-ECMO."),
  ],
  punch="Lungs alone: VV; heart failing, or arrest: VA (or convert VV to V-AV); VA-ECMO’s cost is a higher LV afterload, so the LV may need venting with an Impella or IABP.",
)

L['CAR-17'] = dict(
  sub="Cardiology → ACS → STEMI without on-site PCI: pharmaco-invasive strategy",
  step=4,
  intro="Step 4 begins with the commonest ACS decision outside a PCI centre. Primary PCI is better than lysis only if it can be done quickly; the card gives the time limit and what follows lysis.",
  parts=[
    ('a', "**If PCI cannot happen within 120 min of diagnosis → lyse (within 10 min of diagnosis; door-to-needle ≤30 min).** Beyond about 120 minutes of delay the advantage of PCI over lysis is lost to the extra myocardium that dies waiting (ESC 2023). Lysis works best early, when the thrombus is fresh and fibrin-poor, and is given within 12 hours of symptom onset. ESC targets the bolus within 10 minutes of the diagnostic ECG; the AHA target is door-to-needle within 30 minutes."),
    ('b', "**Transfer for angiography 2–24 h after lysis (mini test: 3–24 h). Not before 2–3 h (bleeding peak).** Lysis opens the artery in about half to two thirds of patients but leaves the ruptured plaque, so routine early angiography prevents re-occlusion; within the first hours the lytic state makes arterial puncture and PCI more likely to bleed and gave no benefit (facilitated PCI)."),
    ('c', "**Below 50% ST resolution at 60–90 min, ongoing pain or instability → immediate rescue PCI.** ST resolution is the bedside marker of tissue reperfusion; failure to resolve by half means the artery is probably still closed. Repeat lysis is not effective."),
  ],
  mimic=[
    ("Rescue PCI vs pharmaco-invasive PCI", "Rescue: lysis failed, go now. Pharmaco-invasive: lysis worked, angiography in 2–24 h."),
  ],
  traps=[
    ("“Transfer for PCI regardless of delay” when door-to-balloon is 160 min", "Lyse first (77% right); ‘regardless of delay’ applies to cardiogenic shock (CAR-18a)."),
    ("“1 h” or “48 h” for angiography after successful lysis", "2–24 h; the mini test answer was 12 h (34% right)."),
  ],
  decode=[
    ("Anterior STEMI, door-to-balloon expected 160 min — best initial management? [DocT QBank, 77%]", "Immediate thrombolysis before transfer."),
    ("Anterior STEMI 1 h, nearest PCI centre 150 km away [NEET 2025 recall]", "Thrombolysis."),
  ],
  punch="If PCI cannot happen within 120 minutes of diagnosis, lyse within 10 minutes, then transfer for angiography at 2–24 h, or go for rescue PCI at once if ST elevation has not fallen by half at 60–90 minutes.",
)

L['CAR-18'] = dict(
  sub="Cardiology → ACS → STEMI with cardiogenic shock",
  step=4,
  intro="Shock changes the reperfusion rule of CAR-17: lysis needs a perfusion pressure to reach the clot, so the priority becomes mechanical revascularisation. The card then chooses the vasoactive drug by the blood pressure and by any β-blockade.",
  parts=[
    ('a', "**Immediate transfer for PCI/CABG, whatever the delay. Culprit-only PCI (CULPRIT-SHOCK).** In the SHOCK trial early revascularisation improved long-term survival; lytics work poorly at low perfusion pressure. CULPRIT-SHOCK found culprit-only PCI better than immediate multivessel PCI (death or renal replacement at 30 days 45.9% vs 55.4%). ESC 2023 adds that fibrinolysis should be considered (IIa) if primary PCI is not possible within 120 minutes and mechanical complications are excluded; lysing and transferring are not exclusive."),
    ('b', "**Dobutamine — low output without frank hypotension.** Dobutamine is a β₁ inotrope with β₂ vasodilation, so it raises output but can drop the blood pressure; it needs a pressure to start from. ESC also places an inotrope first in wet-cold patients with borderline pressure."),
    ('c', "**Noradrenaline first, then add the inotrope.** Below SBP 90 (MAP <65) coronary and organ perfusion depend on pressure; noradrenaline raises it with less tachycardia and fewer arrhythmias than dopamine (SOAP II, worse outcome with dopamine in its cardiogenic subgroup) or adrenaline (OptimaCC: more refractory shock)."),
    ('d', "**Milrinone — PDE3 works downstream of the blocked β-receptor.** Milrinone inhibits phosphodiesterase III, so cAMP rises without needing the β-receptor; it also increases calcium reuptake into the sarcoplasmic reticulum (lusitropy) and dilates veins and arteries, so it lowers the BP. Levosimendan also keeps working under β-blockade, by sensitising troponin C to calcium and opening K-ATP channels."),
    ('e', "**Not routinely (IABP-SHOCK II: no mortality benefit).** 30-day mortality 39.7% vs 41.3%, with no difference at 6 years. Of the devices, only the Impella CP has improved survival in STEMI shock (DanGer Shock: 180-day death 45.8% vs 58.5%), at the cost of more moderate or severe bleeding (21.8% vs 11.9%), limb ischaemia (5.6% vs 1.1%) and renal replacement (41.9% vs 26.7%) (CAR-26)."),
  ],
  mimic=[
    ("Milrinone vs levosimendan vs dobutamine", "Dobutamine: β₁ agonist, blunted by β-blockers. Milrinone: PDE3, raises cAMP beyond the receptor. Levosimendan: calcium sensitiser, no cAMP. Both of the latter work in β-blocked patients and both vasodilate."),
  ],
  traps=[
    ("“Lyse because the PCI centre is 3.5 h away”", "With shock, transfer for revascularisation (only 9% right); ESC allows lysis as a bridge if PCI is beyond 120 min."),
    ("“Dopamine” as the inotrope for BP 80/50 in ADHF (DocT QBank key, 38%)", "Outdated: dopamine caused more arrhythmias and deaths in cardiogenic shock (SOAP II). Noradrenaline for the pressure, dobutamine for the output."),
    ("“Start a vasopressor such as noradrenaline” for HFrEF at SBP 85 (DocT QBank keys dobutamine, 58%)", "DocT follows ESC (inotrope first with borderline SBP); this card follows AHA/SCAI (noradrenaline below SBP 90). Low output with borderline SBP: dobutamine. Shock with MAP <65: noradrenaline first."),
    ("“Selective β₁ stimulation” or “troponin C sensitisation” for the drug that improves CO, venodilates and enhances SR calcium reuptake (GT2, 50%)", "PDE3 inhibition, raising cAMP: milrinone."),
  ],
  decode=[
    ("Large anterior STEMI, BP 72/40, rising lactate — intervention with the strongest survival impact? [DocT GT]", "Early coronary reperfusion."),
    ("On dobutamine, BP keeps falling (85/55) [DocT QBank, 90%]", "Add a vasopressor such as noradrenaline."),
    ("ADHF on chronic β-blocker, CO low despite high-dose dobutamine [DocT GT]", "Levosimendan."),
    ("STEMI with shock, PCI centre door-to-balloon 75 min [DocT GT]", "Primary PCI."),
  ],
  punch="STEMI with shock goes for revascularisation of the culprit whatever the delay; dobutamine if the pressure holds, noradrenaline first if it does not, milrinone or levosimendan if β-blocked, and no routine IABP.",
)

L['CAR-19'] = dict(
  sub="Cardiology → ACS → Right ventricular infarction",
  step=4,
  intro="Not every infarct shock is a failing left ventricle. In an inferior STEMI with clear lungs and a high JVP, the right ventricle has stopped pushing, and the treatment is nearly the opposite of LV failure.",
  parts=[
    ('a', "**RV infarction; ST elevation in V4R.** The right coronary artery usually supplies the RV; a proximal occlusion causes inferior STEMI with RV involvement. ST elevation ≥1 mm in V4R is the most sensitive ECG sign and fades within hours; echo shows a dilated, hypokinetic RV."),
    ('b', "**Cautious crystalloid bolus while arranging primary PCI.** A stunned RV moves blood through the lungs only if it is filled at a higher pressure; without that the LV is underfilled and output falls. Fluid is given in small boluses, because an over-distended RV bulges the septum into the LV and lowers output again."),
    ('c', "**Nitrates, diuretics, morphine, β-blockers — all drop preload.** Venodilation or diuresis removes the filling pressure the RV depends on; a sudden collapse after sublingual nitrate is the classic presentation."),
    ('d', "**Dobutamine; keep AV synchrony (pace if heart block).** Inferior infarcts often cause AV block; losing atrial contraction removes a large part of RV filling, so sequential pacing helps more than ventricular pacing alone."),
  ],
  mimic=[
    ("RV infarct vs LV cardiogenic shock", "RV: clear lungs, high JVP, Kussmaul sign, preload-dependent, give fluid. LV: crackles, high PAWP, avoid fluid."),
  ],
  traps=[
    ("“Medication-related adverse reaction” for collapse to 60/30 after nitrate in inferior STEMI", "The nitrate unmasked a preload-dependent RV infarct: cardiogenic shock (46% right; the distractor also drew about 46%)."),
  ],
  decode=[
    ("Inferior STEMI given aspirin, nitrate and morphine; BP falls from 160/90 to 60/30 [DocT QBank, 46%]", "Cardiogenic shock (RV infarction)."),
  ],
  punch="Inferior STEMI with hypotension, clear lungs and a high JVP is RV infarction: confirm with V4R, give cautious fluid, avoid nitrates, diuretics and morphine, use dobutamine and keep AV synchrony while PCI is arranged.",
)

L['CAR-20'] = dict(
  sub="Cardiology → ACS → Antithrombotics, nitrates and troponin",
  step=4,
  intro="Four separate ACS decisions sit on this card, each tested by a different trap: the anticoagulant when nobody is reperfused, the IV P2Y12 inhibitor, the nitrate ban, and troponin in kidney disease.",
  parts=[
    ('a', "**Fondaparinux (OASIS-6) — less death/re-MI, no extra major bleeding. Not alone during primary PCI (catheter thrombosis).** Fondaparinux is an indirect factor Xa inhibitor given once daily; in STEMI patients without primary PCI it lowered death or re-infarction without more bleeding. It does not inhibit thrombin at the catheter tip, so if the patient goes to PCI a bolus of UFH is added. ESC 2023 recommends fondaparinux (class I) in NSTE-ACS when early angiography is not planned, advises against it during primary PCI (class III) and gives it IIa alongside streptokinase; it has no separate class for unreperfused STEMI, so the card’s answer rests on OASIS-6."),
    ('b', "**Cangrelor — onset seconds, offset ~1 h.** Cangrelor is the only IV P2Y12 inhibitor: reversible, half-life 3–6 minutes, platelet function back within about an hour. Morphine and vomiting delay gut absorption of oral P2Y12 inhibitors, and IV cangrelor bypasses the gut. It is also the bridge when DAPT must stop for urgent surgery after a recent stent (BRIDGE)."),
    ('c', "**No nitrates within 24 h (sildenafil) / 48 h (tadalafil) — profound hypotension.** Both nitrates and PDE5 inhibitors raise cGMP in vascular smooth muscle; together they cause severe vasodilation."),
    ('d', "**Chronically raised; diagnose MI by a rise and/or fall (dynamic change), not a single value.** Chronic kidney disease and chronic myocardial injury raise baseline troponin; the Fourth Universal Definition requires a rise and/or fall with at least one value above the 99th percentile, plus clinical evidence of ischaemia."),
  ],
  mimic=[
    ("Cangrelor vs GP IIb/IIIa inhibitors", "Cangrelor blocks P2Y12, reversible, offset about an hour. Eptifibatide and tirofiban block GP IIb/IIIa; abciximab binds platelets for days."),
  ],
  traps=[
    ("“Enoxaparin or UFH” as the best anticoagulant when no reperfusion is given", "Fondaparinux (23% right)."),
    ("“Tirofiban or eptifibatide” as IV P2Y12 bridging", "Cangrelor (35% right on the mini test; 80% in GT2)."),
    ("“A single troponin above the 99th percentile in CKD 4 = MI”", "A dynamic rise and/or fall is needed (GT3 lost)."),
  ],
  decode=[
    ("Recent stent, on DAPT, septic shock needing urgent surgery — IV antiplatelet bridge? [DocT GT, 80%]", "Cangrelor infusion."),
  ],
  punch="No reperfusion: fondaparinux; IV P2Y12: cangrelor (also the surgical bridge); no nitrates within 24 h of sildenafil or 48 h of tadalafil; in CKD diagnose MI by a troponin rise and/or fall.",
)

L['CAR-21'] = dict(
  sub="Cardiology → Anticoagulation → Reversal agents and doses",
  step=4,
  intro="Bleeding on an anticoagulant is the most-asked single topic in the deck after shock profiles. Each drug has its own reversal because each works at a different point in the cascade.",
  parts=[
    ('a', "**Dabigatran → idarucizumab 5 g IV: specific, immediate. Side effects: delirium, fever, constipation, hypoKALAEMIA.** Idarucizumab is a humanised antibody fragment that binds dabigatran about 350 times more tightly than thrombin, reversing it within minutes (given as 2 × 2.5 g). Its listed adverse effects include hypokalaemia, delirium, constipation, pyrexia and pneumonia; hyperkalaemia is not one."),
    ('b', "**Xa inhibitors (apixaban, rivaroxaban) → andexanet alfa; or 4F-PCC 50 U/kg. Ciraparantag = investigational.** Andexanet is a decoy factor Xa that binds the drug. In ANNEXA-I (2024, ICH) it gave better haemostatic efficacy than usual care (67.0% vs 53.1%) but more thrombotic events (10.3% vs 5.6%; ischaemic stroke 6.5% vs 1.5%), and US sales ended in December 2025 after an FDA safety warning on thrombosis; 4F-PCC is now the usual choice where andexanet is unavailable. INR does not measure Xa inhibitor effect, and vitamin K does nothing for a DOAC."),
    ('c', "**Warfarin + major bleed → 4F-PCC (25–50 U/kg by INR) + vitamin K 10 mg IV. FFP only if no PCC.** PCC supplies factors II, VII, IX and X (plus proteins C and S) in a small volume and corrects the INR in minutes; FFP needs large volumes, thawing and hours. Typical PCC dosing is 25 U/kg for INR 2–4, 35 for 4–6 and 50 above 6. Vitamin K takes 6–12 hours but prevents the INR rebounding once PCC wears off. Without bleeding: INR 4.5–10, hold 1–2 doses (low-dose oral vitamin K only if bleeding risk is high); INR above 10, oral vitamin K 2.5–5 mg."),
    ('d', "**Heparin (UFH) → protamine 1 mg per 100 U given in the last 2–3 h (max 50 mg): full reversal.** Protamine is a basic protein that binds acidic heparin; UFH’s half-life is about 60–90 minutes, so only recent units are counted."),
    ('e', "**Enoxaparin → protamine 1 mg per mg if dose <8 h ago; 0.5 mg/mg if 8–12 h: only ~60% reversal; none after 12 h.** Protamine binds the long chains that carry anti-thrombin activity; LMWH’s short chains, which carry the anti-Xa activity, escape, so reversal is partial."),
  ],
  mimic=[
    ("Specific vs non-specific reversal", "Specific: idarucizumab (dabigatran), andexanet (Xa inhibitors), protamine (heparins). Non-specific: PCC (warfarin; Xa inhibitors where andexanet is unavailable)."),
  ],
  traps=[
    ("“Factor VII is not in PCC” (GT7 key, 59%)", "Outdated: modern 4-factor PCC contains II, VII, IX and X; only the old 3-factor PCC lacks VII."),
    ("“FFP + vitamin K” for warfarin ICH (Marrow key, recent stroke)", "Marrow argues PCC is prothrombotic and PCC trials excluded recent MI/stroke; AHA/ESO still prefer 4F-PCC + IV vitamin K for life-threatening bleeding. Pick FFP only if the stem stresses a recent thrombotic event and asks for the ‘safest’ agent."),
    ("“Delay endoscopy until the INR is normal” or “FFP” for melaena at INR 2.8 (AIM1, 53%)", "PCC (with vitamin K) and do not delay endoscopy."),
    ("“Hyperkalaemia is an adverse effect of idarucizumab”", "Hypokalaemia is; hyperkalaemia is the ‘not seen’ answer (45%)."),
    ("“Protamine after enoxaparin given 14 h ago”", "None after 12 h; 1 mg/mg within 8 h, 0.5 mg/mg at 8–12 h (INI-SS lost, 35%)."),
  ],
  decode=[
    ("Dabigatran, massive GI bleed or ICH — reversal? [DocT QBank / GT ×5, 86–87%]", "Idarucizumab."),
    ("Rivaroxaban or apixaban bleed — specific reversal? [DocT QBank / GT, 75–94%]", "Andexanet alfa; or 4F-PCC (aPCC also keyed)."),
    ("Warfarin, life-threatening bleed or ICH, INR 4–10 [DocT QBank / GT ×6]", "4F-PCC + IV vitamin K."),
    ("Mechanical mitral valve, INR 8.4, no bleeding, CKD, aspirin [DocT GT]", "Hold 1–2 doses + oral vitamin K 2–2.5 mg."),
  ],
  punch="Dabigatran: idarucizumab 5 g; Xa inhibitors: andexanet or 4F-PCC 50 U/kg; warfarin with major bleeding: 4F-PCC plus IV vitamin K 10 mg; heparin: protamine 1 mg per 100 U; enoxaparin: protamine, partial and none after 12 h.",
)

L['CAR-22'] = dict(
  sub="Cardiology → Vasopressors → Phenylephrine, vasopressin, methylene blue",
  step=4,
  intro="Shock pharmacology ends with what to add or switch when noradrenaline is not enough, or is causing harm. Each answer depends on which receptor or pathway the drug uses.",
  parts=[
    ('a', "**Phenylephrine — pure α1, no β1 chronotropy (INI-SS key).** If noradrenaline’s β₁ effect drives a tachyarrhythmia, a pure α-agonist keeps the vascular tone without stimulating the heart; the reflex from the rise in pressure may even slow the rate. It can lower cardiac output by raising afterload, so it is a specific-situation drug, not first line."),
    ('b', "**When noradrenaline reaches 0.25–0.5 µg/kg/min.** Surviving Sepsis 2021 suggests adding vasopressin in this range rather than escalating noradrenaline. Septic shock causes a relative vasopressin deficiency, and V1 receptors still work when adrenergic receptors are down-regulated by acidosis and high catecholamine levels."),
    ('c', "**Inhibits endothelial and inducible NO synthase and downstream soluble guanylate cyclase → less cGMP → vasoconstriction.** Vasoplegia (bypass, liver transplant, sepsis) is driven by NO → sGC → cGMP → smooth-muscle relaxation, plus K-ATP channel opening; methylene blue blocks it at two points. Other rescue agents: vasopressin, angiotensin II (ATHOS-3) and hydroxocobalamin (scavenges NO and H₂S). Angiotensin I is an inactive precursor needing ACE and is not a vasopressor drug."),
  ],
  mimic=[
    ("Angiotensin II vs angiotensin I", "Angiotensin II is the licensed vasopressor (ATHOS-3); angiotensin I is the precursor."),
  ],
  traps=[
    ("“Methylene blue raises NO synthase activity” or acts on adrenergic receptors", "It inhibits NOS and sGC; only 7% picked the correct statement."),
    ("“Angiotensin I raises MAP in vasoplegia”", "It is the LEAST likely (17% right): an inactive precursor, not a drug."),
    ("“Noradrenaline” for flutter or AF with RVR in septic shock or stroke", "Phenylephrine avoids β-stimulation (31% right in INI-SS)."),
  ],
  decode=[
    ("Liver-kidney transplant, vasoplegia on high-dose noradrenaline — LEAST likely to raise MAP? [DocT GT, 17%]", "Angiotensin I."),
    ("Ischaemic stroke, MAP 58 after fluids, AF with RVR — preferred vasopressor? [DocT GT]", "Phenylephrine, to avoid β-stimulation."),
  ],
  punch="When noradrenaline drives a tachyarrhythmia switch to pure α phenylephrine; add vasopressin at 0.25–0.5 µg/kg/min; methylene blue inhibits NO synthase and guanylate cyclase, and angiotensin I is not a vasopressor.",
)

L['CAR-23'] = dict(
  sub="Cardiology → Pulmonary embolism → ESC risk classes and treatment",
  step=5,
  intro="Step 5 opens with the decision that most PE questions test: who gets lysis. The ESC classes are built around one fact — death in PE comes from RV failure, and only established haemodynamic failure justifies the bleeding risk of systemic lysis.",
  parts=[
    ('a', "**High: SBP below 90 (or fall ≥40, or pressors) / arrest → systemic thrombolysis (alteplase 100 mg over 2 h).** ESC 2019 defines high risk as cardiac arrest, obstructive shock (SBP <90 or vasopressors with end-organ hypoperfusion) or persistent hypotension (SBP <90 or a fall ≥40 mmHg for more than 15 minutes, not from another cause). The RV is already failing, so dissolving the clot is worth the bleeding risk; an accelerated 0.6 mg/kg over 15 min (max 50 mg) is the alternative, used in arrest. Surgical or catheter embolectomy if lysis is contraindicated or fails."),
    ('b', "**Intermediate-high: normotensive + RV dysfunction AND troponin → anticoagulate, monitor; rescue lysis if decompensates.** In PEITHO, tenecteplase in this group reduced decompensation (1.6% vs 5.0%) but did not change mortality (1.2% vs 1.8%) and caused haemorrhagic stroke in 2.0% vs 0.2% and major bleeding in 11.5% vs 2.4%. So these patients are anticoagulated (usually LMWH) in a monitored bed and lysed only if they become hypotensive."),
    ('c', "**Intermediate-low: one or neither of RV / troponin; PESI III–V → anticoagulate on ward.**"),
    ('d', "**Low: sPESI 0 → early discharge, DOAC.** The AHA/ACC 2026 PE guideline renames these groups as categories A–E (C1–C3 by RV and troponin, D incipient failure, E hypotension or arrest); systemic lysis is harmful up to C2, unclear in C3 and reasonable in E. The rule is the same: hypotension, not imaging or biomarkers, earns lysis."),
  ],
  mimic=[
    ("Intermediate-high vs high risk", "Both have a strained RV and raised troponin; only high risk has hypotension or shock. BP 96/58 is still intermediate-high."),
  ],
  traps=[
    ("“RV strain + troponin with BP 96/58 → lysis”", "Anticoagulate and monitor (INI-SS correct; GT4 Q26 you chose lysis)."),
  ],
  decode=[
    ("APS, saddle PE, hypotensive, RV hypokinesis despite heparin [Marrow]", "rtPA (alteplase 100 mg over 2 h)."),
  ],
  punch="In PE hypotension decides lysis: high risk (shock, SBP <90 or arrest) gets alteplase 100 mg over 2 hours; intermediate-high (RV strain plus troponin, normotensive) gets anticoagulation and monitoring, with rescue lysis only if it decompensates.",
)

L['CAR-24'] = dict(
  sub="Cardiology → Pulmonary embolism → D-dimer, subsegmental PE, Daniel score",
  step=5,
  intro="Three diagnostic points around PE severity: how to read a D-dimer in older patients, what to do with a tiny clot, and how the ECG scores RV strain.",
  parts=[
    ('a', "**Age × 10 µg/L (FEU) if above 50 years.** D-dimer rises with age, so a fixed 500 µg/L cut-off excludes few older patients; ADJUST-PE showed the age-adjusted cut-off safely rules out PE in more of them (only in low or intermediate clinical probability)."),
    ('b', "**Clinical surveillance, no anticoagulation (repeat leg ultrasound).** CHEST 2021 suggests surveillance over anticoagulation for isolated subsegmental PE with no proximal DVT and low recurrence risk; anticoagulate if cancer, immobility, poor reserve or a positive leg scan."),
    ('c', "**Daniel ECG score: HR >100 = 2; incomplete RBBB = 2; complete RBBB = 3; T inversion in all of V1–V4 = 4; S1Q3T3 (complete) = 2; score ≥10 = severe pulmonary hypertension.** Each item reflects RV pressure overload; the full score also adds points for the depth of T inversion in each of V1–V3 and for each part of S1Q3T3, to a maximum of 21. A score ≥10 suggests systolic PA pressure above about 50 mmHg."),
  ],
  mimic=[],
  traps=[
    ("“Anticoagulate every subsegmental PE”", "Isolated, no DVT, low risk: surveillance (only 17% right)."),
  ],
  decode=[
    ("[pattern] HR 118, incomplete RBBB, T inversion V1–V4 — Daniel score?", "2 + 2 + 4 = 8."),
    ("[pattern] 70-year-old, low pretest probability — D-dimer cut-off?", "700 µg/L (age × 10)."),
  ],
  punch="Use an age × 10 µg/L D-dimer cut-off above 50, watch isolated low-risk subsegmental PE with repeat leg scans, and add the Daniel ECG points (tachycardia 2, RBBB 2 or 3, T inversion V1–V4 4) to grade RV strain.",
)

L['CAR-25'] = dict(
  sub="Cardiology → Haemodynamics → Shock profiles on a PA catheter",
  step=5,
  intro="This is the most-asked card in the deck (30 questions). Four numbers name the shock: RAP (right filling), PAWP (left filling), cardiac output and SVR. Each type of shock starts with one failure, and the other numbers follow from the body’s response to it.",
  parts=[
    ('a', "**Hypovolaemic: RAP ↓, PAWP ↓, CO ↓, SVR ↑.** Too little volume: both filling pressures fall, output falls, and sympathetic vasoconstriction raises SVR. A child may stay normotensive by tachycardia and high SVR until late."),
    ('b', "**Cardiogenic (LV): RAP ↑/N, PAWP ↑, CO ↓, SVR ↑.** The pump fails: blood backs up behind the LV (high PAWP, pulmonary oedema), output falls, SVR rises. Low output means more oxygen extraction, so ScvO₂ is low and the peripheries are cold."),
    ('c', "**Distributive (early): RAP ↓/N, PAWP ↓/N, CO ↑, SVR ↓.** Vessels dilate first; output rises to compensate, so the skin is warm, the pulse pressure wide and the ScvO₂ normal or high. Sepsis is the commonest cause of high-output hypotension; others are liver failure, anaphylaxis, thyrotoxicosis, AV fistula, beriberi. Neurogenic shock is distributive too, but with bradycardia and low CO from lost sympathetic tone."),
    ('d', "**Obstructive — PE: RAP ↑, PAWP ↓/N, CO ↓, SVR ↑.** The block lies between the right heart and the left: pressure piles up behind it (high RAP) while the left atrium is starved (low PAWP). High RAP with low PAWP means obstruction before the left heart."),
    ('e', "**Obstructive — tamponade: RAP ↑, PAWP ↑ (equal), CO ↓, SVR ↑.** Fluid around the heart compresses all four chambers, so the diastolic pressures equalise (RAP = RV diastolic = PAWP); the LV is small, the IVC plethoric, the pulse pressure narrow. A massive pleural effusion (tension hydrothorax) behaves the same way: high CVP with obstructive shock, treated by drainage."),
  ],
  table=dict(title="Shock profiles", head=["Shock", "RAP", "PAWP", "CO", "SVR"], rows=[["Hypovolaemic", "↓", "↓", "↓", "↑"], ["Cardiogenic (LV)", "↑/N", "↑", "↓", "↑"], ["Distributive (early)", "↓/N", "↓/N", "↑", "↓"], ["Obstructive — PE", "↑", "↓/N", "↓", "↑"], ["Obstructive — tamponade", "↑", "↑ (equal)", "↓", "↑"]]),
  mimic=[
    ("Hypovolaemic vs obstructive PE", "Both have low PAWP and high SVR; RAP separates them — low in hypovolaemia, high in PE."),
    ("Cold low-flow vs warm distributive", "Cold, low ScvO₂: low output (cardiogenic, hypovolaemic). Warm, wide pulse pressure, normal or high ScvO₂: distributive."),
  ],
  traps=[
    ("“Hypovolaemic” for RAP 14, PAWP 6, high SVRI (GT4 Q75)", "Hypovolaemia would make both pressures LOW; high RAP with low PAWP is obstructive."),
    ("“Septic shock” for cold peripheries, oliguria and LOW ScvO₂, CVP 10 (DocT QBank key, 60%)", "Disputed key: low ScvO₂ with cold peripheries means low output, i.e. cardiogenic; only early unresuscitated sepsis gives a low ScvO₂."),
    ("“Cirrhosis with portal hypertension” as the cause of CVP 22 (DocT QBank / GT6 key)", "Wrong physiology: portal pressure sits upstream of the liver, and cirrhosis is hyperdynamic with a normal-low CVP. CVP 22 means right-heart failure or volume overload — ‘AKI with fluid overload’ is the physiological answer."),
    ("“Acute PE” for CVP 18, BP 140/90, acute respiratory failure in a smoker (DocT key, 27–44%)", "Ambiguous item: a normal BP makes it at most intermediate-risk PE, and COPD with cor pulmonale fits equally. Pick PE if the stem gives SBP <90 or RV strain with a clear chest; COPD if wheeze and chronic hypercapnia."),
    ("“Pulsus paradoxus” or “electrical alternans” as what best confirms tamponade (GT2, 73%)", "On a catheter, equalisation of diastolic pressures."),
  ],
  decode=[
    ("BP 80/50 with CVP 15 after MI; CVP 18 with low EF [DocT QBank / GT, 88–100%]", "Cardiogenic shock."),
    ("Septic shock: MAP 60, SvO₂ 80%, CO high, SVR low [DocT GT ×3, 84–100%]", "Distributive."),
    ("Large effusion on X-ray, BP 85/55, CVP 15–18 [DocT QBank, 79–85%]", "Obstructive shock from massive pleural effusion."),
    ("Hypovolaemic vs cardiogenic by CVP, PCWP, CI, SVR [NEET 2025 recall]", "Hypovolaemic ↓↓↓↑; cardiogenic ↑↑↓↑."),
  ],
  extra=[dict(q="Need EVLW and continuous cardiac output — which monitor? (INI-SS, lost)", a="Transpulmonary thermodilution with pulse-contour analysis (e.g. PiCCO); a PA catheter gives intermittent CO and PAWP but not extravascular lung water.")],
  punch="Read RAP against PAWP first: both low is hypovolaemia, PAWP high is LV failure, RAP high with PAWP low is PE, all equal is tamponade; then CO and SVR separate warm distributive shock from the cold low-output kinds.",
)

L['CAR-26'] = dict(
  sub="Cardiology → Mechanical support → Devices by flow",
  step=5,
  intro="The deck ends with machines that take over the pump. They differ in how much flow they add, which ventricle they support, and whether they need the heart’s own rhythm.",
  parts=[
    ('a', "**IABP: LV, ~0.5–1 L; ↓ afterload, ↑ coronary perfusion; no routine benefit in shock.** The balloon inflates in diastole (raising coronary perfusion) and deflates before systole (lowering afterload). It needs a regular rhythm or pressure trigger to time this, so a very irregular rhythm degrades it; IABP-SHOCK II showed no mortality benefit."),
    ('b', "**Impella CP: LV, ~3.5–4 L; pulls blood LV → aorta; can vent the LV on VA-ECMO.** A microaxial pump across the aortic valve unloads the LV directly and works independently of the rhythm. DanGer Shock (2024): in STEMI with shock, routine Impella CP lowered 180-day death (45.8% vs 58.5%) but increased moderate or severe bleeding, limb ischaemia and renal replacement."),
    ('c', "**Impella RP / TandemHeart RA–PA: RV, ~4 L; right-sided support.** For isolated RV failure (RV infarct, after LVAD, PE) blood is moved from the right atrium or IVC to the pulmonary artery."),
    ('d', "**VA-ECMO: heart + lungs, up to ~7 L; biventricular failure, ECPR, fulminant myocarditis.** The only device that gives full circulatory and respiratory support and keeps working even in VF; it raises LV afterload (CAR-16e)."),
  ],
  mimic=[
    ("Rhythm-dependent vs rhythm-independent devices", "Only the IABP needs synchrony; Impella, TandemHeart and VA-ECMO are continuous-flow."),
  ],
  traps=[
    ("“Impella CP” as the only device that supports without cardiac synchrony (CGT6 key)", "Disputed: TandemHeart and VA-ECMO are also continuous-flow and rhythm-independent; only the IABP needs synchrony."),
    ("“Impella gives the highest flow with LV support”", "VA-ECMO does (23% right)."),
  ],
  decode=[
    ("Refractory cardiogenic shock, recurrent fast AF — device effective without synchrony? [DocT GT]", "Key: Impella CP (TandemHeart and VA-ECMO also correct)."),
  ],
  punch="IABP adds under 1 L/min and needs a regular rhythm, Impella CP about 3.5–4 L and improved survival in STEMI shock (DanGer Shock), and VA-ECMO gives up to 7 L with full heart and lung support.",
)

L['CAR-27'] = dict(
  sub="Cardiology → Sweep → True or false",
  step=5,
  intro="The sweep checks nine statements, one from each part of the deck. Each turns on a single detail from an earlier card.",
  parts=[
    ('a', "**False — verapamil; adenosine can trigger bronchospasm** (CAR-02c)."),
    ('b', "**False — negatively inotropic; avoid with EF below 40%** (CAR-04a)."),
    ('c', "**False — warfarin; DOACs contraindicated** (CAR-05a)."),
    ('d', "**False — hyperkalaemia; digoxin = reverse tick, short QT** (CAR-07b)."),
    ('e', "**True — 1 mg every 3–5 min** (CAR-08)."),
    ('f', "**False — resume CPR for 2 min straight away** (CAR-11c)."),
    ('g', "**True — rescue PCI if lysis fails** (CAR-17)."),
    ('h', "**False — VA; the heart must be bypassed** (CAR-16a)."),
    ('i', "**False — anticoagulate; lysis only if hypotensive** (CAR-23)."),
  ],
  mimic=[],
  traps=[
    ("“Every tachycardia drug is safe if the patient is stable”", "Stability lets you use a drug, but the node (WPW), the ventricle (low EF) and the airway (asthma) still decide which one."),
  ],
  decode=[
    ("[pattern] True/false on arrhythmia, arrest and PE rules", "Mark each statement on its own before reading the options."),
  ],
  punch="Most errors here come from applying a default to the exception: no adenosine in asthma, no verapamil with low EF, no DOAC in rheumatic MS, no pulse check after analysis, no VV for ECPR, no lysis without hypotension.",
)

FLAGS = {}
FLAGS['CAR-15'] = "a: ‘SBP ≥90 mmHg’ is out of date — AHA 2025 Part 11 gives only MAP ≥65 mmHg (COR 1) and dropped the SBP target (verified fix in qbank.json). Explanation says so."
FLAGS['CAR-03'] = "b: the banned list omits IV amiodarone, which AHA 2023 and 2025 list with digoxin, non-DHP CCBs and β-blockers as harmful in pre-excited AF (COR 3). Explanation adds it."
FLAGS['CAR-18'] = "a: ‘immediate transfer whatever the delay’ follows ACC/AHA; ESC 2023 adds that fibrinolysis should be considered (IIa) in STEMI with shock if primary PCI cannot be done within 120 min and mechanical complications are excluded. Not wrong as the exam answer; explanation gives both."
FLAGS['CAR-21'] = "Xa-inhibitor row: US sales of andexanet alfa ended on 22 Dec 2025 after an FDA safety communication on thrombosis (ANNEXA-I: thrombotic events 10.3 vs 5.6%); 4F-PCC 50 U/kg is now the usual alternative. Consider noting it on the card; explanation does."
FLAGS['CAR-05'] = "b: the card’s ‘above 48 h’ threshold is ACC/AHA 2023; ESC 2024 lowered it to 24 h (no early cardioversion without prior anticoagulation or TOE once AF has lasted ≥24 h). Explanation says so. Not errors: ESC 2024 replaces CHA₂DS₂-VASc with CHA₂DS₂-VA (sex removed), but the Marrow line still teaches VASc, which is what the question tests; c could add EAST-AFNET 4 (early rhythm control lowered CV events). Explanation gives both."
FLAGS['CAR-23'] = "Not an error: the AHA/ACC 2026 acute PE guideline renames the risk groups as categories A–E (systemic lysis harmful A–C2, unclear C3, reasonable E). Card follows ESC 2019, still current. Explanation mentions it."
