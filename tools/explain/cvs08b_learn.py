# CVS08B — Explain v3 ("Learn" depth): BLS & ACLS II — electrical therapy. Defibrillation energy (adult, paediatric), pads, refractory VF (vector change, DSED, head-up CPR),
# cardioversion vs defibrillation, 2025 cardioversion energies and practicalities, the tachycardia-with-pulse algorithm (instability, narrow, wide, adenosine, infusions, AF/flutter with RVR),
# post-arrest targets, bradycardias and AV blocks, the bradycardia algorithm, its infusions, transcutaneous pacing and causes.
# No mnemonics or hooks. Driven by qpack/CVS08B.md (71 question links; ACLS-33 AF/flutter with RVR asked 13 times, ACLS-29 narrow-complex 9, ACLS-37 bradycardia algorithm 8,
# ACLS-36 AV blocks 7, ACLS-28 and ACLS-30 six each, ACLS-26 five). ACLS-22, -23, -24, -38 and -39 have no linked question and get short explanations with [pattern] decode items.
# Card layer (cvs_cardlayer.json, CVS08B|*) lines and cross notes read and used: ACLS-27, -28, -29, -30, -31, -33, -35, -36, -37, -39.
# Checked online on 19 Nov 2026:
#  - AHA 2025 Part 9 Adult ALS (cpr.heart.org): biphasic preferred (2a); unknown setting → maximal dose may be considered (2b); higher energy for 2nd and later shocks may be considered (2b);
#    vector change and DSED usefulness not established (2b, B-R; evidence essentially DOSE-VF, positive by intention-to-treat, not by treatment received); routine pacing in established
#    arrest not recommended (3: No Benefit); head-up CPR not recommended except in trials (3: No Benefit, C-LD). AF cardioversion initial ≥200 J (2a, B-R; biphasic 200 J >90% cumulative
#    success; low-energy monophasic shocks more likely to provoke VF); flutter 200 J (2b, C-LD; 50 J succeeds 50–75%, 200 J nearly 100%). Adenosine for regular NCT (1); vagal manoeuvres (1);
#    diltiazem/verapamil for stable regular NCT (2a). WCT: adenosine for stable regular monomorphic WCT for treatment or diagnosis (2b); adenosine in unstable WCT 3: Harm; verapamil and
#    diltiazem in WCT 3: Harm; amiodarone, procainamide or sotalol may be considered (2b). Sustained polymorphic VT → immediate unsynchronised shock (1); routine magnesium for polymorphic VT
#    with normal QT 3: No Benefit. AF/flutter with RVR: unstable → immediate cardioversion (1); IV β-blocker or non-DHP CCB for rate control (1); IV amiodarone useful in the critically ill (2a);
#    pre-excited AF: digoxin, non-DHP CCB, β-blockers, IV amiodarone 3: Harm (may increase ventricular response and cause VF); LV systolic dysfunction with decompensated HF: non-DHP CCB and IV
#    β-blocker 3: Harm; AF/flutter >48 h unanticoagulated risks thromboembolism. Bradycardia: threshold now typically <50/min; treat reversible causes (1); atropine (2a); TCP as a bridge (2b);
#    adrenergic infusions (2b); temporary transvenous pacing for refractory unstable bradycardia (2a).
#  - AHA 2025 algorithms (accessible versions, cpr.heart.org): tachyarrhythmia (rate typically ≥150; five instability features; unstable → synchronised cardioversion, consider adenosine if
#    regular narrow; stable → QRS ≥0.12 s wide; adenosine 6 mg then 12 mg; procainamide 20–50 mg/min to suppression, hypotension, QRS +50% or 17 mg/kg, maintenance 1–4 mg/min, avoid with long QT
#    or CHF; amiodarone 150 mg over 10 min, 1 mg/min for 6 h; sotalol NOT printed in the 2025 algorithm). Electrical cardioversion (>150 prepare; ≤150 generally not needed; SpO2 monitor,
#    suction, IV, intubation equipment; AF 200 J, flutter 200 J, narrow 100 J, monomorphic VT 100 J, polymorphic VT unsynchronised; resynchronise after each shock; go unsynchronised if
#    delayed and critical). Bradycardia (atropine 1 mg every 3–5 min, max 3 mg; dopamine 5–20 mcg/kg/min, taper slowly; adrenaline 2–10 mcg/min; TCP; transvenous pacing with expert
#    consultation; causes: ischaemia/infarction, drugs/toxins (CCB, β-blocker, digoxin), hypoxia, electrolytes (hyperkalaemia)).
#  - AHA 2025 Post-cardiac arrest care: 100% O2 until SpO2 reliable (1); SpO2 90–98%, PaO2 60–105 (2a); PaCO2 35–45 (1); MAP ≥65 (1; SBP target removed); temperature control 32–37.5 °C in patients
#    unresponsive to verbal commands (1), for at least 36 h (2a); emergent angiography with persistent ST elevation (1); angiography before discharge in suspected cardiac cause (1);
#    multimodal prognostication ≥72 h after normothermia (2a).
#  - AHA 2025 PALS: initial 2–4 J/kg (2 J/kg for ease of teaching, 2a); subsequent 4 J/kg (2b), higher levels may be considered, not above 10 J/kg or the adult maximum.
#  - AHA 2025 BLS/ALS summary (CHEST Physician): pads anterolateral or anteroposterior; electrode diameter >8 cm in adults; bra guidance.
# Reviewer check, 19 Nov 2026 (cpr.heart.org Part 9 and PALS; ERC 2025 ALS, Resuscitation 215:110769; ERC 2025 PALS algorithm; RCUK 2025 post-resuscitation guideline based on ERC–ESICM 2025;
#  first10em DOSE-VF summary; thebottomline REVERT; wikijournalclub PROCAMIO; NEUROPROTECT AHA 2018 report): DOSE-VF (NEJM 2022, n 405 of 930 planned, stopped early by COVID; 13.3% / 21.7% / 30.4%;
#  AHA notes no benefit by treatment received); ERC 2025: consider vector change after 3 failed shocks, DSED not routine; ERC 2025 cardioversion: AF maximum output, flutter/SVT 70–120 J, VT 120–150 J;
#  ERC 2025 bradycardia: atropine 500 mcg to 3 mg, isoprenaline 5 mcg/min or adrenaline 2–10 mcg/min; REVERT (Lancet 2015) 43% vs 17%; PALS 2025 SVT cardioversion 0.5–1 J/kg then 2 J/kg (2a);
#  ERC 2025 paediatric 4 J/kg every shock, escalate to max 8 J/kg (360 J) in refractory VF; ERC–ESICM 2025 fever prevention ≤37.5 °C for 36–72 h; PROCAMIO (EHJ 2017, n 74: termination 67% vs 38%,
#  MACE 9% vs 41%, benefit also in structural heart disease); AHA 2025 polymorphic VT: immediate unsynchronised shock for sustained PMVT (1, B-NR), no stability qualifier.
# From standard references without a fresh check (confident): adenosine half-life under 10 s, 3 mg via central line/transplant/dipyridamole; TTM (2013) and TTM2 (2021); BOX (2022); COACT (2019),
# TOMAHAWK (2021); anticoagulation 3 weeks before and 4 weeks after cardioversion of AF ≥48 h (ESC 2024 AF); esmolol pharmacology; SA exit block patterns; Mobitz I vs II level of block.

SPINE = [
  ("Defibrillation: dose and delivery", "An unsynchronised shock depolarises enough myocardium at once to stop fibrillation, so what matters is enough current through the heart: the right energy, large pads in either position, and nothing that delays the first shock."),
  ("Synchronised cardioversion", "In an organised rhythm with a pulse the shock is timed to the R wave so it never lands on the vulnerable T wave, and in 2025 AF and flutter start at 200 J because low energies fail and can provoke VF."),
  ("Tachycardia: unstable, then QRS", "Instability sends any tachycardia to the shock; a stable one is sorted by QRS width and regularity, which decides whether vagal manoeuvres, adenosine, nodal blockers or antiarrhythmics are safe."),
  ("After ROSC: the targets", "After ROSC the brain is protected by avoiding the second hits: hypotension, hypoxia, hyperoxia, abnormal CO₂ and fever, with temperature control for at least 36 hours."),
  ("Reading the slow rhythm", "Where the block lies (sinus node, AV node or below it) is read from the P–QRS relationship and the QRS width, and the level of block predicts whether it will progress and whether atropine can help."),
  ("Treating the bradycardia", "Symptomatic bradycardia gets atropine, then pacing or an adrenergic infusion, then transvenous pacing, while the reversible cause (ischaemia, drugs, hypoxia, potassium) is treated alongside."),
]

PRIMER = "Electrical therapy works by depolarising a large mass of myocardium at once so the sinus node can take over again. A shock that lands during the T wave (the vulnerable period, when cells are partly repolarised) can itself start VF, which is why shocks in a patient with an organised rhythm are synchronised to the R wave and shocks in VF cannot be. The AHA tachycardia and bradycardia algorithms both start with the same question: is the rhythm causing hypotension, altered mentation, shock, ischaemic chest pain or acute heart failure? CVS08A covered BLS, the cardiac arrest algorithm and arrest drugs; this deck covers the shocks, the rhythms with a pulse and the care after ROSC."

L = {}

L['ACLS-21'] = dict(
  sub="ACLS → Defibrillation → Energy",
  step=1,
  intro="Step 1 is getting enough current through the fibrillating heart. The energy rules are simple once the logic is clear: biphasic shocks are more efficient, so less energy is needed, and when in doubt the highest available dose is the safer error. The one real question tests whether pregnancy changes any of this.",
  parts=[
    ('a', "**A device that delivers a therapeutic dose of electrical energy to the heart to force it to produce a more normal cardiac rhythm.** The shock depolarises a critical mass of myocardium simultaneously, ending the chaotic re-entry of VF; the sinus node or another pacemaker then has a chance to take over. It does not ‘restart’ an asystolic heart, which is why asystole is not shocked."),
    ('b', "**Biphasic: follow the manufacturer’s recommendation (e.g. initial 120–200 J); if unknown, use the maximum available.** Biphasic waveforms reverse the current half-way through the pulse, which defibrillates at lower energy with less myocardial injury; AHA 2025 prefers biphasic over monophasic (2a). Devices differ (rectilinear, truncated exponential), so the effective dose is device-specific; if the setting is not known, the maximal dose may be considered (2b), because under-dosing a fibrillating heart costs more than the small risk of a high shock."),
    ('c', "**Second and subsequent doses should be equivalent, and higher doses may be considered.** AHA 2025 tells you to follow the manufacturer’s fixed or escalating protocol (2a) and allows higher energy for later shocks (2b). A failed first shock suggests high transthoracic impedance or a hard-to-defibrillate substrate, so escalating where the device allows is reasonable."),
    ('d', "**Monophasic: 360 J.** Monophasic current flows one way only and is less efficient, so the full 360 J is used for every shock."),
  ],
  mimic=[
    ("Defibrillation vs synchronised cardioversion energy", "Defibrillation uses the device’s maximum or recommended dose unsynchronised; cardioversion uses rhythm-specific lower doses timed to the R wave (ACLS-26)."),
  ],
  traps=[
    ("“Halve the dose, or avoid shocks, in pregnancy”", "Transthoracic impedance is not meaningfully changed in pregnancy and little current reaches the fetus; standard adult doses are used without modification (81% got this)."),
    ("“Only biphasic is acceptable”", "Biphasic is preferred, but a monophasic device at 360 J is still recommended to treat VF; any defibrillator is better than delay."),
  ],
  decode=[
    ("Third-trimester woman in VF — which statement on defibrillation is true? [DocT QBank]", "Standard energy doses, no modification."),
    ("Biphasic device, manufacturer dose not known [pattern]", "Use the maximum available energy."),
  ],
  punch="Use the manufacturer’s biphasic dose or, if unknown, the maximum; monophasic is 360 J. Pregnancy changes nothing about the energy.",
)

L['ACLS-22'] = dict(
  sub="ACLS → Defibrillation → Paediatric doses",
  step=1,
  intro="Still step 1, scaled to the child. Paediatric doses are weight-based because current needed rises with body size, and the ceiling stops a large child getting more than an adult.",
  parts=[
    ('a', "**First shock: 2 J/kg.** AHA 2025 allows 2–4 J/kg for the first shock and teaches 2 J/kg for simplicity (2a)."),
    ('b', "**Second shock: 4 J/kg.** A failed first shock is followed by 4 J/kg (2b)."),
    ('c', "**Subsequent shocks: 4 J/kg.** AHA 2025 keeps 4 J/kg for refractory VF but adds that higher levels may be considered. ERC 2025 uses 4 J/kg for every shock, from the first, and for VF that persists after repeated shocks allows stepwise escalation to at most 8 J/kg (maximum 360 J)."),
    ('d', "**Maximum: 10 J/kg or the adult dose.** Whichever is reached first; in a 40 kg adolescent 10 J/kg would be 400 J, above most adult devices, so the adult dose is the ceiling."),
  ],
  mimic=[
    ("Paediatric defibrillation vs paediatric cardioversion", "Defibrillation starts at 2 J/kg; synchronised cardioversion for SVT with cardiopulmonary compromise starts at 0.5–1 J/kg, then 2 J/kg (AHA 2025 PALS, 2a). The ERC uses 1 J/kg, then 2 J/kg."),
  ],
  traps=[
    ("“4 J/kg is the fixed ceiling”", "AHA 2025 allows higher doses for refractory VF, up to 10 J/kg or the adult maximum; the card’s 2 → 4 → 4 is the default sequence, not a ban on going higher."),
  ],
  decode=[
    ("Child in VF, first shock — energy? [pattern]", "2 J/kg (2–4 J/kg acceptable)."),
    ("Refractory paediatric VF after two shocks [pattern]", "4 J/kg, may go higher, never above 10 J/kg or the adult dose."),
  ],
  punch="Two, then four joules per kilogram, more only if refractory, and never beyond 10 J/kg or the adult dose.",
)

L['ACLS-23'] = dict(
  sub="ACLS → Defibrillation → Pads (2025)",
  step=1,
  intro="Step 1 again: the energy only works if it crosses the heart. Pad position and size decide how much of the current takes that path rather than skirting it through the chest wall.",
  parts=[
    ('a', "**Anterolateral or anteroposterior — both acceptable.** Each places the heart between the pads; trials have not shown one to be clearly better for VF, so the choice follows access (anteroposterior suits a pacing patient, a large breast or a device in the right pectoral area)."),
    ('b', "**Electrode diameter greater than 8 cm in adults.** Larger pads lower transthoracic impedance and spread current, so more of it reaches the myocardium with less skin burn."),
    ('c', "**It might be reasonable to adjust the position of a bra rather than remove it.** Pads must touch skin and avoid underwire, but the delay and reluctance that come with removing clothing cost more; women receive bystander defibrillation less often, partly for this reason."),
  ],
  mimic=[
    ("Anteroposterior vs vector change", "Anteroposterior is an acceptable first-choice position; vector change is moving pads from anterolateral to anteroposterior after failed shocks (ACLS-24)."),
  ],
  traps=[
    ("“Anteroposterior is only for cardioversion”", "Both positions are acceptable for defibrillation in 2025."),
  ],
  decode=[
    ("Which pad positions are acceptable for adult defibrillation? [pattern]", "Anterolateral or anteroposterior."),
    ("Female collapse, rescuer hesitant about clothing [pattern]", "Adjust the bra, do not delay removing it."),
  ],
  punch="Either position, pads over 8 cm, and move clothing rather than delay the shock.",
)

L['ACLS-24'] = dict(
  sub="ACLS → Refractory VF → Vector change, DSED, head-up CPR",
  step=1,
  intro="The last part of step 1 is the patient whose VF survives three standard shocks. The new tools change where or how much current is delivered, and the guideline is cautious because the evidence is one trial.",
  parts=[
    ('a', "**Vector change defibrillation: usefulness not established.** Moving the pads from anterolateral to anteroposterior sends current through a different path, which may capture myocardium the first vector missed (2b)."),
    ('b', "**Double sequential defibrillation (DSED): usefulness not established.** Two defibrillators fire in rapid sequence from two pad sets, delivering more energy along two vectors (2b)."),
    ('c', "**The basis is a single small RCT supporting both, with outstanding questions.** DOSE-VF (2022, n 405) found survival to discharge 13.3% with standard shocks, 21.7% with vector change and 30.4% with DSED, but it was small (405 of a planned 930, stopped early because of COVID-related staffing problems), and AHA 2025 notes the benefit held by intention-to-treat, not when patients were analysed by the treatment they actually received. ERC 2025 reads the same trial differently: it suggests considering a vector change (anteroposterior pads) after three failed shocks, but does not recommend routine DSED. One positive trial is not enough to call a therapy established."),
    ('d', "**Head-up CPR is not recommended except in clinical trials.** No RCTs exist, only observational studies at serious risk of bias (3: No Benefit)."),
  ],
  mimic=[
    ("Refractory VF vs recurrent VF", "Refractory VF never terminates despite shocks; recurrent VF terminates and then returns, which points to a trigger (ischaemia, electrolytes) rather than an energy problem."),
  ],
  traps=[
    ("“DSED is the 2025 treatment for refractory VF”", "It may be considered, but its usefulness is not established; the standard remains good CPR, standard shocks, adrenaline and amiodarone or lidocaine."),
  ],
  decode=[
    ("Refractory VF after three shocks: 2025 status of DSED or vector change? [pattern]", "May be considered; usefulness not established (one small RCT)."),
    ("Head-up CPR in adult arrest [pattern]", "Not recommended outside trials."),
  ],
  punch="Vector change and DSED rest on one small positive trial, so both are ‘not established’; head-up CPR belongs only in trials.",
)

L['ACLS-25'] = dict(
  sub="ACLS → Cardioversion vs defibrillation",
  step=2,
  intro="Step 2 is the shock given to a heart that still has an organised rhythm. The whole difference from defibrillation is timing: a shock that lands on the T wave of a beating heart can cause the VF you are trying to avoid.",
  parts=[
    ('a', "**Cardioversion is synchronised, delivered on the peak of the R wave; defibrillation has no synchronisation.** The device senses the R wave and fires a few milliseconds later, when the ventricle is fully depolarised and refractory, so the shock cannot strike the vulnerable period."),
    ('b', "**Cardioversion: VT with a pulse, AF, flutter; defibrillation: VF and polymorphic VT.** Polymorphic VT has QRS complexes of varying shape, so the device cannot pick a reliable R wave; it may sense a T wave or fail to fire, which is why it is treated as VF."),
    ('c', "**Synchronisation helps prevent the R-on-T phenomenon.** The relative refractory period on the upslope of the T wave is when parts of the ventricle are excitable and parts are not, the substrate for re-entry; a shock there can induce VF."),
  ],
  mimic=[
    ("Synchronised vs unsynchronised mode on the same device", "Sync must be switched on, and many devices drop it after each shock, so it must be reselected (ACLS-27)."),
  ],
  traps=[
    ("“Sync on the T wave or the P wave”", "On the R wave; the T wave is exactly what sync avoids."),
  ],
  decode=[
    ("Synchronised cardioversion — shock timed to which wave? [Marrow]", "The R wave, to avoid R-on-T."),
  ],
  punch="Synchronise on the R wave whenever there is an organised QRS; VF and polymorphic VT have none, so they get unsynchronised shocks.",
)

L['ACLS-26'] = dict(
  sub="ACLS → Cardioversion → 2025 energies",
  step=2,
  intro="Step 2 continues with how much energy the synchronised shock needs. The 2025 change is that AF and flutter both start at 200 J: starting low saves nothing and fails more often. Five questions test this, two of them still keyed to the older numbers.",
  parts=[
    ('a', "**Atrial fibrillation: 200 J.** AHA 2025: an initial setting of at least 200 J is reasonable (2a). Pooled biphasic trials found 200 J gave over 90% cumulative success, more efficiently than starting low, with no extra myocardial injury. AF has many small wavelets spread across both atria, so it needs a large current to depolarise all the atrial tissue."),
    ('b', "**Atrial flutter: 200 J.** Flutter is a single macro-re-entry circuit and is easier to terminate (50 J succeeds 50–75% of the time), but 200 J succeeds nearly always, so AHA 2025 suggests 200 J here too (2b)."),
    ('c', "**Narrow-complex tachycardia: 100 J.** Regular SVT (AVNRT, AVRT) is a small circuit through the node and terminates easily."),
    ('d', "**Monomorphic VT: 100 J.** An organised ventricular circuit with a reliable R wave to sync on."),
    ('e', "**Polymorphic VT: unsynchronised, high-energy shock (defibrillation).** AHA 2025 recommends an immediate unsynchronised shock for sustained polymorphic VT (1); sync cannot lock on. The rationale line on the card is the reason for higher starting doses: low-energy shocks provoked VF in AF and AF in flutter."),
  ],
  table=dict(title="2025 synchronised cardioversion, adult",
    head=["Rhythm", "Energy", "Why"],
    rows=[["AF", "≥200 J", "Multiple wavelets, need large atrial mass depolarised"],
          ["Flutter", "200 J", "Low energy works often, 200 J nearly always"],
          ["Narrow regular SVT", "100 J", "Small nodal circuit"],
          ["Monomorphic VT", "100 J", "Organised, reliable R wave"],
          ["Polymorphic VT", "Unsynchronised, defibrillation dose", "No R wave to track"]]),
  mimic=[
    ("AHA 2025 vs ERC 2025 cardioversion energies", "AHA: AF at least 200 J, flutter 200 J, narrow SVT and monomorphic VT 100 J. ERC 2025: maximum output for AF, 70–120 J for flutter and SVT, 120–150 J for VT with a pulse. The bank keys for this card follow AHA."),
    ("Polymorphic VT with a pulse vs torsades that self-terminates", "Sustained polymorphic VT is shocked unsynchronised; recurrent self-terminating torsades with a long QT is treated with IV magnesium 2 g and removing QT-prolonging drugs."),
  ],
  traps=[
    ("“Unstable AF: start at 120–200 J” (DocT CGT4 key)", "That is the pre-2025 range; AHA 2025 starts AF at 200 J or more. Pick cardioversion; if both are offered, the 2025 answer is ≥200 J."),
    ("“Unstable AF: synchronised cardioversion at 100 J” (DocT QBank key)", "Cardioversion is right, the energy is old; 100 J is for narrow regular SVT and monomorphic VT."),
    ("“Polymorphic VT with a pulse: synchronised 100 J or magnesium”", "AHA 2025 recommends an immediate unsynchronised shock for sustained polymorphic VT (1) with no stability qualifier, because it regards every form of polymorphic VT, whatever the QT, as haemodynamically and electrically unstable. Magnesium is for torsades with a long QT and gives no benefit when the QT is normal."),
  ],
  decode=[
    ("Unstable AF, 2025 initial energy? [DocT GT]", "≥200 J biphasic."),
    ("BP 75/40, HR 180, regular broad QRS, no P waves [DocT QBank]", "Synchronised cardioversion (81%); for monomorphic VT, 100 J."),
    ("Polymorphic VT with a pulse — most critical action? [DocT GT]", "Immediate unsynchronised shock."),
    ("Septic ICU patient, new AF 155/min, BP falling to 90/60 [DocT GT]", "Synchronised cardioversion; the key says 120–200 J, 2025 says ≥200 J."),
  ],
  punch="AF and flutter now start at 200 J, narrow SVT and monomorphic VT at 100 J, and polymorphic VT is defibrillated. Low energies fail and can provoke the next arrhythmia.",
)

L['ACLS-27'] = dict(
  sub="ACLS → Cardioversion → Practicalities",
  step=2,
  intro="Step 2 ends with doing the cardioversion safely. The questions test when to shock at once, that sedation is given whenever feasible, and the anticoagulation that follows AF cardioversion.",
  parts=[
    ('a', "**Ventricular rate over 150/min: prepare for immediate cardioversion; generally not needed at 150 or below.** At rates under 150 a healthy heart is rarely made unstable by the rate itself, so instability below that suggests another cause (sepsis, bleeding, hypoxia) driving a compensatory tachycardia; shocking it will not help. The main 2025 algorithm says ‘typically ≥150/min’."),
    ('b', "**At the bedside: oxygen saturation monitor, suction, IV line, intubation equipment.** Sedation can cause apnoea or aspiration, and the shock can cause bradycardia or VF, so airway and resuscitation equipment must be at hand."),
    ('c', "**Prerequisites: consent, sedation/analgesia, rule out left atrial clot.** Sedate whenever feasible, even when unstable, unless it would dangerously delay the shock. LA clot matters in AF or flutter of 48 hours or more or unknown duration: restoring atrial contraction can expel it. Then anticoagulate for 3 weeks before (or exclude clot by TOE) and at least 4 weeks after, because the atria stay stunned after sinus rhythm returns. An unstable patient is cardioverted at once with heparin started alongside."),
    ('d', "**Resynchronise after each cardioversion; if synchronisation is delayed and the patient is critical, go to unsynchronised shocks.** Many devices revert to unsynchronised mode after a shock. If the device cannot sense the R wave and the patient is deteriorating, a defibrillation-dose shock is safer than waiting."),
  ],
  mimic=[
    ("Compensatory sinus tachycardia vs primary tachyarrhythmia", "Rate under 150 with obvious sepsis, bleeding or fever: treat the cause; shocking a sinus tachycardia does nothing."),
  ],
  traps=[
    ("“Mandatory intubation or an arterial line before cardioversion”", "AHA 2025 asks for sedation whenever feasible; intubation and lines only delay the shock."),
    ("“Unstable new AF of 5 minutes after surgery: amiodarone or metoprolol first”", "Hypotension with a rate of 167 is instability; synchronised cardioversion (87%)."),
    ("“Anticoagulate 2 or 3 weeks after cardioversion”", "At least 4 weeks after; 3 weeks is the time before."),
  ],
  decode=[
    ("Post-thoracotomy, new AF 167/min, BP 73/34 [DocT GT]", "Synchronised cardioversion."),
    ("Unstable flutter being prepared for cardioversion — what step is specifically recommended? [DocT GT]", "Sedation whenever feasible."),
    ("After cardioversion of AF, anticoagulate for how long? [DocT GT]", "4 weeks (78%)."),
    ("Narrow irregular 140/min, BP 80/50 [NEET 2025]", "Synchronised cardioversion; diltiazem, metoprolol and digoxin are for stable patients."),
  ],
  punch="Shock at once when the rate is over about 150 and it is causing instability; sedate when you can, resynchronise every time, and anticoagulate for at least 4 weeks after cardioverting AF.",
)

L['ACLS-28'] = dict(
  sub="ACLS → Tachycardia algorithm → Stable or unstable",
  step=3,
  intro="Step 3 opens with the only question that matters first in any tachycardia: is it causing the patient harm? Six questions test this, and the lowest score (30%) is a stable patient whom many chose to shock.",
  parts=[
    ('a', "**Unstable: hypotension, acutely altered mental status, signs of shock, ischaemic chest discomfort, acute heart failure.** Each means the rate is cutting cardiac output or coronary flow: diastole shortens, the ventricle fills less and the myocardium is starved. The tachycardia must also be the cause of the instability, which is why the rate is usually 150 or more."),
    ('b', "**Unstable → synchronised cardioversion; adenosine may be considered only if the rhythm is regular and narrow.** Electricity works in seconds and does not depress the heart. A regular narrow rhythm is likely nodal re-entry, which adenosine ends almost instantly, so it may be tried while the defibrillator is readied."),
    ('c', "**Stable → 12-lead ECG and IV access, then assess the QRS.** With time to spare, the 12-lead defines the rhythm before any drug is chosen."),
    ('d', "**Narrow: QRS under 0.12 s; wide: QRS 0.12 s or more.** A narrow QRS means the ventricles are activated through the His–Purkinje system, so the origin is above the ventricles; a wide QRS is VT until proved otherwise."),
  ],
  mimic=[
    ("Symptomatic but stable vs unstable", "Palpitations, light-headedness with a normal BP and mentation is stable; hypotension, confusion, chest pain or pulmonary oedema is unstable."),
  ],
  traps=[
    ("“Recurrent palpitations, no chest pain or breathlessness, AF on ECG: sedate and cardiovert at 100 J”", "He is stable; stable AF gets rate control (diltiazem or a β-blocker). Only 30% chose diltiazem."),
    ("“Unstable WCT: intubate first” (Marrow key)", "Unstable tachycardia gets synchronised cardioversion; intubation delays it. Marrow keyed the airway only because cardioversion was not offered: pick cardioversion if it is there."),
    ("“Child with SVT that recurs after adenosine and becomes unstable: give diltiazem or amiodarone”", "Synchronised cardioversion (0.5–1 J/kg, then 2 J/kg); verapamil and diltiazem cause collapse in infants."),
  ],
  decode=[
    ("BP 75/40, HR 180, regular broad QRS [DocT QBank]", "Synchronised cardioversion (81%)."),
    ("Adolescent SVT recurs 30 s after adenosine, now unstable [DocT QBank]", "Synchronised cardioversion (90%)."),
    ("Stable regular narrow 180/min, vagal failed [DocT GT ×2]", "IV adenosine (76% and 100%)."),
    ("Stable intermittent palpitations, AF [DocT QBank]", "Diltiazem — rate control (30%)."),
  ],
  punch="Instability caused by the tachycardia means a synchronised shock, with adenosine allowed only for a regular narrow rhythm; stability buys time for a 12-lead and a decision by QRS width.",
)

L['ACLS-29'] = dict(
  sub="ACLS → Tachycardia algorithm → Stable narrow-complex",
  step=3,
  intro="Step 3, narrow branch. A stable regular narrow tachycardia is almost always a re-entry circuit using the AV node, so the treatment is a sequence of ever-stronger nodal blocks. Nine questions test this, and half the cohort skipped the vagal manoeuvre.",
  parts=[
    ('a', "**Regular: vagal manoeuvres first.** A vagal surge slows AV-nodal conduction and can break a circuit that runs through the node (AVNRT, AVRT). The modified Valsalva (strain, then lie flat with legs raised) converts about 43% versus 17% for the standard one (REVERT). Carotid sinus massage is supine, on ECG, one side for 5–10 s, and contraindicated with a carotid bruit or prior TIA or stroke."),
    ('b', "**If ineffective: adenosine, then β-blockers or calcium channel blockers.** Adenosine (ACLS-31) blocks the node for seconds and ends most nodal re-entry; if the rhythm persists or returns, a longer-acting nodal blocker (diltiazem, verapamil or a β-blocker) is used."),
    ('c', "**Irregular: β-blockers or calcium channel blockers.** An irregular narrow tachycardia is AF, flutter with variable block, atrial tachycardia with variable block or multifocal atrial tachycardia; the node is not part of the circuit, so adenosine cannot end it, and the goal is rate control (ACLS-33)."),
    ('d', "**2025: synchronised cardioversion for unstable narrow-complex tachycardia, and for a stable one that persists despite vagal manoeuvres and drugs, or when they are contraindicated.** Electricity is the end of the sequence, not the start, in a stable patient."),
  ],
  mimic=[
    ("AVNRT vs AVRT vs flutter 2:1", "AVNRT: young woman, P hidden in the QRS or pseudo-r′ in V1; orthodromic AVRT: P after the QRS with RP over 70 ms; flutter 2:1: rate about 150, saw-tooth waves seen when adenosine slows the ventricles."),
  ],
  traps=[
    ("“Stable SVT 180/min: adenosine first”", "Vagal manoeuvres first (only 50% chose Valsalva); adenosine comes when they fail."),
    ("“Stable regular narrow 180/min after failed vagal: cardiovert or amiodarone”", "Adenosine is next (76%)."),
    ("“AVRT is a cause of irregular narrow tachycardia”", "AVNRT and AVRT are always regular; irregular means AF, flutter or atrial tachycardia with variable block, or MAT."),
  ],
  decode=[
    ("Stable, HR 180, narrow [DocT QBank]", "Valsalva manoeuvre (50%)."),
    ("Stable regular narrow, vagal failed [DocT GT ×2, Marrow]", "Adenosine 6 mg, then 12 mg."),
    ("Young woman, no structural disease, stable narrow 170/min — diagnosis? [DocT GT]", "AVNRT (67%)."),
    ("Contraindication to carotid sinus massage [DocT GT]", "Carotid bruit."),
  ],
  punch="Stable regular narrow tachycardia is broken at the AV node: vagal manoeuvre, then adenosine, then a β-blocker or calcium channel blocker, and a shock only if all fail. Irregular narrow tachycardia needs rate control, not adenosine.",
)

L['ACLS-30'] = dict(
  sub="ACLS → Tachycardia algorithm → Stable wide-complex",
  step=3,
  intro="Step 3, wide branch. A regular wide tachycardia in a patient with heart disease is VT about 80% of the time (over 90% after MI), so every choice here is made as if it were VT. Six questions test this.",
  parts=[
    ('a', "**Adenosine only if the rhythm is regular and monomorphic, for treatment or diagnosis.** If it is SVT with aberrancy, adenosine ends it or reveals the atrial rhythm; VT is usually unaffected, and a regular monomorphic VT rarely deteriorates from a brief nodal block (2b)."),
    ('b', "**Procainamide, amiodarone or sotalol.** All three act on the ventricle as well as the atria (2b). With decompensated heart failure, amiodarone is the usual choice: procainamide and sotalol are negatively inotropic and hypotensive, and the algorithm says to avoid procainamide in CHF. PROCAMIO (2017, 74 patients, stable regular WCT) found procainamide ended more tachycardias than amiodarone within 40 minutes (67% vs 38%) with fewer major cardiac adverse events (9% vs 41%), and the advantage held in structural heart disease; it was small and open-label and excluded patients with poor haemodynamic tolerance."),
    ('c', "**Do not give verapamil or diltiazem.** If the rhythm is VT, these depress the myocardium and dilate vessels without touching the ventricular circuit, and collapse follows (3: Harm)."),
    ('d', "**Do not give adenosine for unstable, irregularly irregular or polymorphic WCT.** Unstable WCT needs a shock; an irregular wide rhythm may be pre-excited AF, where nodal block sends all conduction down the accessory pathway; polymorphic VT can degenerate (3: Harm)."),
    ('e', "**2025: synchronised cardioversion for unstable WCT, and for stable WCT when drugs are ineffective or contraindicated.**"),
  ],
  mimic=[
    ("VT vs SVT with aberrancy", "AV dissociation, fusion and capture beats, QRS over 160 ms, a northwest axis and precordial concordance favour VT."),
    ("Irregular wide tachycardia vs VT", "Irregularly irregular, varying QRS shapes, very fast (up to 300): pre-excited AF (ACLS-33)."),
  ],
  traps=[
    ("“Stable monomorphic VT in a heart failure patient on metoprolol: adenosine or verapamil”", "Amiodarone (76–78%); verapamil is harm, adenosine does not treat VT, and cardioversion is for instability."),
    ("“Stable regular WCT: immediate defibrillation or cardioversion”", "Antiarrhythmic infusion first; electricity when it fails or the patient becomes unstable."),
  ],
  decode=[
    ("IHD, chest pain, wide QRS, absent P, 150/min — diagnosis? [DocT QBank, DocT GT]", "VT (82–88%)."),
    ("Stable regular WCT, 2025 algorithm next step [DocT GT]", "Antiarrhythmic infusion."),
    ("Decompensated HF, stable monomorphic VT 160/min [DocT GT ×2]", "IV amiodarone."),
  ],
  punch="Treat any wide tachycardia as VT: no verapamil or diltiazem, adenosine only when regular and monomorphic, amiodarone when the heart is weak, and a shock when drugs fail or the patient is unstable.",
)

L['ACLS-31'] = dict(
  sub="ACLS → Tachycardia drugs → Adenosine",
  step=3,
  intro="Step 3 relies on adenosine for both treatment and diagnosis. It works for seconds because it is cleared almost at once, which explains how it must be given and why it fails in some patients.",
  parts=[
    ('a', "**First dose 6 mg rapid IV push, followed by a saline flush.** Adenosine’s half-life is under 10 seconds (uptake into red cells and endothelium), so it must reach the heart as a bolus: a large proximal vein, a fast push and a 20 mL flush."),
    ('b', "**Second dose 12 mg if required.** Used when 6 mg fails. Start at 3 mg via a central line, after heart transplant (denervated, supersensitive) or with dipyridamole or carbamazepine, which potentiate it; theophylline and caffeine antagonise it."),
    ('c', "**Converts AVNRT, AVRT and many atrial tachycardias.** It acts on A1 receptors in the AV node, opening potassium channels and blocking conduction for a few seconds; any circuit that uses the node is broken."),
    ('d', "**Diagnostic: blocks the AV node, unmasking atrial flutter or fibrillation.** When the node is not part of the circuit, the atrial rhythm continues while ventricular beats pause, showing flutter waves (often about 300/min) or fibrillation."),
    ('e', "**Can cause severe bronchospasm in asthma.** Adenosine receptors in the airway (mainly A2B and A3 on mast cells, which release bronchoconstrictor mediators, plus A1 on smooth muscle) narrow an already hyper-reactive airway; most patients also feel a brief flush, chest tightness and a sense of doom."),
  ],
  mimic=[
    ("Flutter 2:1 vs AVNRT after adenosine", "Flutter: rate slows and saw-tooth waves appear, then the tachycardia returns; AVNRT: the rhythm terminates."),
  ],
  traps=[
    ("“Adenosine terminates the SVT, it recurs and the child is unstable: give more adenosine or diltiazem”", "Repeating adenosine buys another 30 s; synchronised cardioversion (90%)."),
    ("“Central line: still 6 mg”", "3 mg via a central line; it reaches the heart undiluted."),
  ],
  decode=[
    ("Adenosine 6 mg via central line reveals saw-tooth waves at 300/min [DocT GT]", "Atrial flutter with 2:1 conduction."),
    ("Stable SVT, adenosine 6 mg failed [Marrow]", "Adenosine 12 mg."),
    ("Only access is an IJ line — adenosine dose? [Marrow]", "3 mg."),
  ],
  punch="Adenosine lasts seconds, so give it fast with a flush, 6 then 12 mg (3 mg centrally); it ends nodal re-entry, unmasks flutter and AF, and is avoided in asthma.",
)

L['ACLS-32'] = dict(
  sub="ACLS → Tachycardia drugs → Procainamide, amiodarone, sotalol",
  step=3,
  intro="Step 3 needs a dose for each of the three wide-complex antiarrhythmics. Each endpoint or bar comes from the drug’s own toxicity, and the one real question tests why sotalol is barred by a long QT.",
  parts=[
    ('a', "**Procainamide 20–50 mg/min until the arrhythmia is suppressed, hypotension ensues, the QRS widens by over 50% or 17 mg/kg is given; maintenance 1–4 mg/min; avoid with prolonged QT or CHF.** It is a class Ia sodium-channel blocker: QRS widening means toxic conduction slowing, hypotension comes from its ganglion-blocking and negative inotropic effect, and its metabolite NAPA prolongs the QT."),
    ('b', "**Amiodarone 150 mg over 10 minutes, repeat if VT recurs; maintenance 1 mg/min for the first 6 hours.** It blocks potassium, sodium and calcium channels and β-receptors, with little negative inotropy at these doses, which is why it is the choice in poor LV function (then 0.5 mg/min for the next 18 hours)."),
    ('c', "**Sotalol 100 mg (1.5 mg/kg) over 5 minutes; avoid with prolonged QT.** Sotalol is a β-blocker with class III potassium-channel (IKr) block, so it lengthens repolarisation and the QT; a prolonged QT is the substrate for torsades. Its β-block also makes it negatively inotropic. Note that sotalol remains in the AHA 2025 guideline text (2b) but has been dropped from the 2025 tachyarrhythmia algorithm, which lists only adenosine, procainamide and amiodarone doses."),
  ],
  mimic=[
    ("Procainamide vs amiodarone choice", "Preserved LV function: procainamide works faster; poor LV function or heart failure: amiodarone."),
  ],
  traps=[
    ("“Sotalol’s main adverse effect is bradycardia or hypotension”", "These occur, but the serious one is QT prolongation and torsades from potassium-channel block."),
  ],
  decode=[
    ("Adverse effect of sotalol is due to? [NEET 2024]", "QT prolongation from potassium-channel (class III) block."),
    ("Procainamide infusion: when do you stop? [pattern]", "Arrhythmia suppressed, hypotension, QRS +50% or 17 mg/kg given."),
  ],
  punch="Procainamide is stopped by QRS widening, hypotension or 17 mg/kg; amiodarone is 150 mg then 1 mg/min; sotalol and procainamide are barred by a long QT because both prolong repolarisation.",
)

L['ACLS-33'] = dict(
  sub="ACLS → Tachycardia algorithm → AF/flutter with RVR",
  step=3,
  intro="Step 3’s most-asked card (13 questions). In AF the problem is too many atrial impulses reaching the ventricle, so the treatment is AV-nodal block, unless the ventricle is failing (decompensated heart failure, hypotension) or the node is bypassed (pre-excitation). Several keys here are disputed.",
  parts=[
    ('a', "**IV β-blocker or non-dihydropyridine CCB for acute rate control without pre-excitation.** Both slow AV-nodal conduction (Class 1); diltiazem is 0.25 mg/kg over 2 min. In the ICU with labile BP, esmolol suits best: onset 2–3 min, half-life about 9 min (red-cell esterases), so it can be switched off. Never give IV verapamil or diltiazem soon after a β-blocker: additive nodal block and negative inotropy can cause asystole. Carvedilol has no IV form."),
    ('b', "**IV amiodarone is useful for rate control in critically ill patients without pre-excitation.** It slows the node with little drop in BP or contractility (2a), so it fits septic shock on vasopressors or a failing ventricle; it may also convert to sinus rhythm."),
    ('c', "**Pre-excited AF/flutter: avoid digoxin, β-blockers, non-DHP CCBs and IV amiodarone.** The accessory pathway has no decremental conduction; blocking the node leaves the pathway to carry atrial impulses at up to 300/min, which can become VF (3: Harm). It looks like an irregular, very fast wide tachycardia with varying QRS shapes. Treat with cardioversion if unstable, procainamide or ibutilide if stable."),
    ('d', "**LV systolic dysfunction with decompensated HF: avoid non-DHP CCBs and IV β-blockers.** Both are negative inotropes; in a ventricle already failing they can precipitate cardiogenic shock (3: Harm). Use amiodarone or digoxin for rate and treat the congestion."),
    ('e', "**Conversion of AF/flutter of over 48 hours in non-anticoagulated patients risks thromboembolism.** Clot forms in the stagnant left atrial appendage; restoring contraction can dislodge it (ACLS-27). For AF under 48 h when rhythm control is wanted, ibutilide 1 mg over 10 min (repeat once; torsades risk), flecainide only without structural disease, amiodarone with it."),
  ],
  table=dict(title="Rate control in AF with RVR: the setting decides",
    head=["Setting", "Use", "Avoid"],
    rows=[["Stable, normal LV", "IV β-blocker or diltiazem", "—"],
          ["Labile BP, post-op or septic", "Esmolol, or IV amiodarone", "Diltiazem (vasodilates)"],
          ["Decompensated HFrEF", "Amiodarone or digoxin", "IV β-blocker, non-DHP CCB"],
          ["Pre-excited (WPW)", "Procainamide or ibutilide; shock if unstable", "All nodal blockers incl. IV amiodarone"]]),
  mimic=[
    ("Pre-excited AF vs polymorphic VT", "Both are irregular and wide; pre-excited AF has a known WPW pattern, rates up to 300 and QRS shapes that vary beat to beat without the twisting of torsades."),
  ],
  traps=[
    ("“HFrEF, AF 130/min, worsening dyspnoea: IV β-blocker” (DocT key, 39%)", "Disputed key: worsening dyspnoea means decompensated HF, where IV β-blockers are 3: Harm. Use amiodarone or digoxin and IV diuretics; the card is right."),
    ("“WPW with AF: only verapamil is contraindicated” (DocT key, 54%)", "Every nodal blocker is contraindicated, including adenosine, esmolol and IV amiodarone, so the item has no single right option; verapamil is the classic answer."),
    ("“Septic shock, new AF 140, BP 102/65: diltiazem or oral amiodarone”", "An IV β-blocker (keyed, 42–56%); IV amiodarone is equally defensible. Diltiazem worsens vasopressor-dependent hypotension; oral amiodarone is too slow."),
    ("“Stable symptomatic AF: IV ibutilide” (Marrow key)", "The AHA stable irregular pathway is rate control. Pick rate control if offered; pick ibutilide only if the stem asks to restore sinus rhythm in AF under 48 h."),
  ],
  decode=[
    ("Septic shock, severe LV dysfunction, AF 170 — least suitable? [DocT GT]", "Verapamil."),
    ("Post-op AF with labile BP, fastest-onset titratable drug? [DocT GT]", "Esmolol."),
    ("Irregular wide 280/min, varying QRS [DocT GT]", "AF with WPW."),
    ("Diltiazem contraindicated with? [Marrow]", "Low EF, after a β-blocker, pre-excited AF — all."),
  ],
  extra=[
    dict(q="Which IV β-blockers are used for atrial tachyarrhythmias?", a="Esmolol, metoprolol, atenolol and propranolol; carvedilol has no IV form."),
  ],
  punch="Slow the node with a β-blocker or diltiazem, unless the ventricle is failing (amiodarone or digoxin), BP is labile (esmolol or amiodarone) or a pathway bypasses the node (no nodal blocker at all: procainamide, ibutilide or a shock).",
)

L['ACLS-34'] = dict(
  sub="ACLS → Post-cardiac arrest → 2025 targets",
  step=4,
  intro="Step 4 is the hours after ROSC, when the brain is exposed to secondary injury from low pressure, abnormal gases and fever. The questions test whether the old 32–34 °C answer still stands.",
  parts=[
    ('a', "**MAP ≥65 mmHg; avoid hypotension.** The brain after arrest has impaired autoregulation, so flow follows pressure; AHA 2025 dropped the old SBP target because the trials used MAP (1). Higher MAP targets (BOX, NEUROPROTECT) did not improve outcome."),
    ('b', "**SpO₂ 90–98% (PaO₂ 60–105 mmHg); 100% FiO₂ until SpO₂ can be measured reliably.** Hypoxia worsens brain injury, and hyperoxia adds free-radical injury on reperfusion, so FiO₂ is titrated down once the saturation reads reliably."),
    ('c', "**PaCO₂ 35–45 mmHg.** Low CO₂ constricts cerebral vessels and lowers flow to an ischaemic brain; high CO₂ raises ICP. Hyperventilation is to be avoided."),
    ('d', "**Temperature control for at least 36 hours in patients unresponsive to verbal commands; goal 32–37.5 °C.** TTM (33 vs 36 °C) and TTM2 (33 vs normothermia with fever prevention, ≤37.5 °C) showed no difference in survival or neurological outcome, so AHA 2025 accepts any deliberate target in this range. The essential element is preventing fever, which worsens injury. ERC–ESICM 2025 recommend actively preventing fever (target 37.5 °C or less) for 36–72 hours in patients who remain comatose (the 2021 version said 37.7 °C or less for at least 72 hours)."),
    ('e', "**Coronary angiography before discharge in survivors with suspected cardiac cause, especially an initial shockable rhythm, unexplained LV dysfunction or severe ischaemia.** Emergent angiography is for persistent ST elevation; without it, immediate angiography did not help (COACT, TOMAHAWK)."),
  ],
  mimic=[
    ("Temperature control vs therapeutic hypothermia", "Hypothermia is one strategy (32–34 °C); temperature control includes normothermia with active fever prevention."),
  ],
  traps=[
    ("“Target temperature after VF arrest is 32–34 °C” (DocT key, 57%)", "That is the 2002–2010 answer. AHA 2025: 32–37.5 °C for at least 36 h, any rhythm. If only one range fits the question, pick it, but know 32–34 is historical."),
  ],
  decode=[
    ("Post-arrest TTM — what should be avoided? [DocT GT]", "Fever, hypoxia and hyperventilation — all (100%)."),
    ("VF arrest, ROSC, comatose, stable — modality? [Marrow]", "Targeted temperature management (temperature control)."),
  ],
  punch="After ROSC keep MAP 65 or more, SpO₂ 90–98%, PaCO₂ 35–45, and control temperature at 32–37.5 °C for at least 36 hours; preventing fever is what matters, not how cold.",
)

L['ACLS-35'] = dict(
  sub="ACLS → Bradycardia → Sinus and junctional",
  step=5,
  intro="Step 5 begins with the slow rhythm where the problem is the pacemaker itself: the sinus node fires slowly or the junction takes over. The P wave tells you which.",
  parts=[
    ('a', "**Sinus bradycardia: normal PR interval; physiological, drug-induced or pathological (hypoxia, MI, raised ICP, hypothyroidism).** Every P is sinus and conducts normally; the node is just slow. Vagal tone (athletes, sleep), β-blockers and CCBs, hypoxia, inferior MI (vagal and nodal artery), Cushing’s reflex in raised ICP and hypothyroidism all slow it. Treat only if it causes symptoms."),
    ('b', "**Junctional bradycardia: P waves inverted, absent or after the QRS; narrow QRS; from hyperkalaemia, SA exit block or severe sinus bradycardia.** When the sinus node fails, the AV junction escapes at 40–60/min. The atria are activated backwards, so the P is inverted in II, III and aVF and may be hidden in or follow the QRS. The ventricles are activated normally, so the QRS is narrow."),
  ],
  mimic=[
    ("SA exit block type II vs sinus pause", "Exit block type II: constant PP with a pause that is an exact multiple (usually twice) of the PP; a sinus pause bears no fixed relation to the PP."),
    ("SA exit block type I vs type II", "Type I: PP intervals shorten progressively, then a pause shorter than two PP; type II: constant PP then a sudden double-length pause."),
  ],
  traps=[
    ("“Constant PP with a pause equal to two PP intervals is a sinus arrest”", "An exact multiple means the impulse fired but failed to exit the node: SA exit block type II (75%)."),
  ],
  decode=[
    ("Elderly, syncope, regular 40/min with normal P and QRS [DocT QBank]", "Sinus bradycardia (92%)."),
    ("Constant PP with a pause equal to two PP [DocT GT]", "SA exit block Mobitz II."),
  ],
  punch="A normal P before each QRS means sinus bradycardia; an inverted, absent or late P with a narrow QRS means the junction has taken over because the sinus node failed.",
)

L['ACLS-36'] = dict(
  sub="ACLS → Bradycardia → AV blocks",
  step=5,
  intro="Step 5’s core: where along the conduction system is the impulse being blocked? Seven questions test this; two keys are disputed and the lowest score is 22%. The answer always comes from the level of block: AV node (vagal, benign, atropine-responsive) or below it (His–Purkinje, unstable, needs pacing).",
  parts=[
    ('a', "**First degree: PR over 200 ms, 1:1 conduction; can be normal, drugs, inferior MI, myocarditis; usually no treatment.** Every beat conducts, just slowly through the node; it is not a true block and an asymptomatic patient is discharged."),
    ('b', "**Mobitz I (Wenckebach): progressive PR lengthening then a dropped QRS; atropine if symptomatic; can progress to complete block.** The AV node tires with each beat (decremental conduction) until one fails. The block is nodal, so the QRS is usually narrow; atropine and exercise speed conduction and improve it, carotid massage worsens it. Seen in inferior MI and with high vagal tone."),
    ('c', "**Mobitz II: fixed PR, random dropped QRS; necessitates treatment — cardiologist and transvenous pacing.** The block is below the node (His–Purkinje): all-or-none failure, often a wide QRS and a sudden risk of complete block. Atropine speeds the sinus rate without helping His–Purkinje conduction, so it can make the ratio worse; carotid massage may paradoxically improve it."),
    ('d', "**Complete heart block: no P–QRS relationship, constant independent P–P and R–R; asymptomatic: pads, monitor, admit; symptomatic: pace.** A narrow escape (40–60) means a junctional pacemaker below a nodal block; a wide, slow escape (20–40) is ventricular and unreliable."),
    ('e', "**Some blocks cannot be differentiated, e.g. 2:1 block: you cannot tell whether the PR lengthens.** With every other beat dropped, there is no run of conducted beats to compare. Use the clues: a narrow QRS, a vagal setting (sleeping athlete) or improvement with atropine favours nodal block; a wide QRS or anterior MI favours infranodal block."),
  ],
  table=dict(title="Nodal vs infranodal block",
    head=["Feature", "Nodal (Mobitz I)", "Infranodal (Mobitz II)"],
    rows=[["QRS", "Usually narrow", "Often wide"],
          ["Atropine, exercise", "Improve", "Worsen or no effect"],
          ["Carotid massage", "Worsens", "May improve"],
          ["MI territory", "Inferior (RCA)", "Anterior (LAD)"],
          ["Course", "Benign, observed", "Progresses; pace"]]),
  mimic=[
    ("Mobitz II vs blocked PACs", "Blocked PACs come early and deform the T wave; in Mobitz II the non-conducted P is on time."),
  ],
  traps=[
    ("“Anterior MI with second-degree block: Mobitz I, benign, give atropine” (DocT key)", "Key is wrong: block after anterior MI is infranodal (LAD supplies the His–Purkinje system), does not respond to atropine and needs immediate transvenous pacing. On exam day pick the option that places the block in the His bundle or Purkinje fibres and paces."),
    ("“Sleeping athlete with 2:1 block: His bundle or bundle branch”", "Vagal setting with a narrow QRS: AV node (only 42% chose it)."),
    ("“Asymptomatic first-degree block: admit or observe”", "Discharge (only 39% chose it)."),
    ("“Septic, HR 34, CHB, BP 80/50: permanent pacemaker”", "Atropine is keyed first (22%); prepare TCP at once because infranodal CHB often fails atropine. A permanent pacemaker comes after stabilisation."),
  ],
  decode=[
    ("Progressive PR lengthening then a dropped beat [NEET 2025]", "Mobitz I (Wenckebach)."),
    ("Type I (nodal) block — feature NOT seen? [Marrow]", "Worsening with atropine."),
    ("HF patient, ECG with long PR, all conducted [DocT QBank]", "First-degree AV block (71%)."),
  ],
  punch="The level of block decides everything: nodal block (narrow QRS, vagal, inferior MI) is benign and helped by atropine; infranodal block (wide QRS, anterior MI, Mobitz II) progresses and needs pacing.",
)

L['ACLS-37'] = dict(
  sub="ACLS → Bradycardia algorithm",
  step=6,
  intro="Step 6 turns reading into treatment. The algorithm runs atropine, then pacing or an adrenergic infusion, then transvenous pacing. Eight questions test it, with low scores (22–43%) where atropine meets an infranodal block, and old doses in two keys.",
  parts=[
    ('a', "**Symptomatic: hypotension, acutely altered mental status, signs of shock, ischaemic chest discomfort, acute heart failure.** The same five features as the tachycardia algorithm: the slow rate is no longer maintaining output. AHA 2025 defines the bradyarrhythmia as typically under 50/min."),
    ('b', "**If absent, monitor and observe.** An asymptomatic slow rate is watched, the cause sought."),
    ('c', "**Atropine 1 mg bolus, repeat every 3–5 min, maximum 3 mg.** Atropine blocks vagal (muscarinic) input to the sinus and AV nodes, so it works in sinus bradycardia and nodal block; it does little for infranodal block or a transplanted heart, and in those it must not delay pacing. 3 mg is full vagal blockade; more adds nothing. AHA moved from 0.5 mg to 1 mg in 2020; ERC 2025 still gives 500 micrograms, repeated every 3–5 minutes to 3 mg."),
    ('d', "**If atropine is ineffective: transcutaneous pacing, or dopamine infusion, or adrenaline infusion.** These are listed as equals. Pacing bypasses the conduction problem; dopamine and adrenaline raise the rate and contractility through β₁ receptors (ACLS-38). In unstable Mobitz II or wide-complex CHB, pacing is the reliable bridge."),
    ('e', "**If still ineffective: transvenous pacing and expert consultation; 2025: temporary transvenous pacing is reasonable in refractory unstable bradycardia.** It is more reliable than transcutaneous capture, and comes with more complications (2a)."),
  ],
  mimic=[
    ("Bradycardia with a pulse vs asystole", "Pacing helps bradycardia with a pulse; routine pacing in established arrest is not recommended (ACLS-39)."),
  ],
  traps=[
    ("“Unstable Mobitz II (septic, BP 75/40): atropine first” (43% chose TCP)", "Atropine rarely helps infranodal block and must not delay pacing; DocT keys transcutaneous pacing."),
    ("“Post-CABG pericarditis, HR 33, 3 mg atropine given, waiting for pacing: norepinephrine or isoproterenol”", "Dopamine (35%); the algorithm names dopamine or adrenaline. More atropine is pointless after 3 mg."),
    ("“Atropine dose 0.5 mg” (Marrow key)", "0.5 mg is the pre-2020 AHA dose and is still the ERC dose, so it is not wrong, but AHA 2020 and 2025 give 1 mg every 3–5 min, max 3 mg. Pick 1 mg if offered."),
    ("“Pacing fails: dopamine or adrenaline?” (NEET 2025 keys dopamine)", "AHA lists them as equals, and ERC 2025 uses isoprenaline (5 mcg/min) or adrenaline (2–10 mcg/min) as its second-line drugs; pick dopamine for this recall, adrenaline if dopamine is not offered."),
  ],
  decode=[
    ("HR 28, BP 80/50, confused, wide-QRS Mobitz II, atropine 1 mg failed [DocT GT]", "Transcutaneous pacing."),
    ("Post-ACS/stent, HR 42 — first drug? [NEET 2025]", "Atropine."),
    ("Mobitz I, BP 80/60, HR 45 [Marrow]", "IV atropine 1 mg."),
    ("Unstable sinus bradycardia with pauses [Marrow]", "Atropine and arrange temporary pacing."),
  ],
  punch="Symptomatic bradycardia: atropine 1 mg to a total of 3 mg, then pacing or dopamine or adrenaline, then transvenous pacing. With an infranodal block, go to pacing without waiting for atropine to fail.",
)

L['ACLS-38'] = dict(
  sub="ACLS → Bradycardia algorithm → Infusions",
  step=6,
  intro="Step 6 needs two infusion doses. The units differ, and that difference is the trap.",
  parts=[
    ('a', "**Dopamine 5–20 mcg/kg/min, titrate to response, taper slowly.** At these doses dopamine stimulates β₁ receptors (rate, contractility) and, higher up, α₁ receptors (vasoconstriction); stopping suddenly can drop the BP."),
    ('b', "**Adrenaline 2–10 mcg/min, titrate to response.** A fixed adult rate in mcg/min, not mcg/kg/min: 2–10 mcg/min in 70 kg is about 0.03–0.14 mcg/kg/min, β-predominant, raising rate and output."),
  ],
  mimic=[
    ("Bradycardia adrenaline vs post-ROSC adrenaline", "Bradycardia: 2–10 mcg/min as a fixed adult rate; post-ROSC vasopressor: 0.1–0.5 mcg/kg/min, which is 7–35 mcg/min in a 70 kg adult."),
  ],
  traps=[
    ("“Adrenaline 2–10 mcg/kg/min”", "That is about 70 times the dose in a 70 kg adult; the bradycardia dose is per minute, not per kg."),
  ],
  decode=[
    ("Dopamine dose in the bradycardia algorithm [pattern]", "5–20 mcg/kg/min."),
    ("Adrenaline infusion for bradycardia [pattern]", "2–10 mcg/min."),
  ],
  punch="Dopamine is per kilogram (5–20 mcg/kg/min); adrenaline is per minute (2–10 mcg/min). Mixing the units is a seventy-fold error.",
)

L['ACLS-39'] = dict(
  sub="ACLS → Bradycardia → Transcutaneous pacing",
  step=6,
  intro="Step 6’s bridge: pacing through the chest wall until a transvenous wire or the cause is fixed. The card layer adds that pacing has no place in an established arrest.",
  parts=[
    ('a', "**Used in haemodynamically unstable bradycardias.** It is a bridge (2b) to transvenous pacing or to correction of the cause, and the immediate choice in unstable high-degree block when IV access is not yet available."),
    ('b', "**Narcotics and benzodiazepines for sedation and analgesia; obtain consent.** The current stimulates chest-wall muscles and is painful in a conscious patient."),
    ('c', "**Set the pacer to 60–80 bpm.** Enough to restore output without excess demand on an ischaemic heart."),
    ('d', "**Current output over 2 mA above the level at which capture is observed.** Electrical capture is a wide QRS and broad T after each spike; mechanical capture must be confirmed by a femoral pulse or arterial trace (the carotid can be confused with muscle twitch). Threshold drifts, so a margin above it prevents loss of capture."),
  ],
  mimic=[
    ("Pacing in bradycardia vs in arrest", "Pacing with a pulse can save the patient; routine pacing in established asystole or PEA does not improve ROSC or survival (3: No Benefit)."),
  ],
  traps=[
    ("“Electrical capture confirms effective pacing”", "Only a palpable femoral pulse or arterial waveform confirms mechanical capture."),
  ],
  decode=[
    ("Transcutaneous pacing rate and output [pattern]", "60–80/min; just above the capture threshold (by about 2 mA)."),
    ("Routine pacing in asystolic arrest? [pattern]", "Not recommended."),
  ],
  punch="Pace unstable bradycardia at 60–80/min, a little above capture, with sedation, and confirm with a pulse; do not pace an established arrest.",
)

L['ACLS-40'] = dict(
  sub="ACLS → Bradycardia → Causes",
  step=6,
  intro="Step 6 ends with what to treat alongside the drugs. Each cause is reversible, and one question tests which drug combination adds up to bradycardia.",
  parts=[
    ('a', "**Myocardial ischaemia or infarction.** Inferior MI (the RCA supplies the sinus and AV nodes in most people) causes vagal and nodal bradycardia; anterior MI causes infranodal block (ACLS-36)."),
    ('b', "**Drugs and toxins: calcium channel blockers, β-blockers, digoxin.** All slow nodal conduction, and their effects add; digoxin raises vagal tone and slows the node directly. Each has a specific treatment: calcium and high-dose insulin for calcium channel blockers, glucagon and high-dose insulin for β-blockers, digoxin-specific Fab fragments for digoxin."),
    ('c', "**Hypoxia.** A late, ominous cause, especially in children; correcting oxygenation is the treatment."),
    ('d', "**Electrolyte abnormality, e.g. hyperkalaemia.** High potassium depolarises cells and slows conduction at every level; calcium stabilises the membrane while potassium is lowered."),
  ],
  mimic=[
    ("Drug-induced vs structural (sick sinus) bradycardia", "Drug-induced resolves when the drug is stopped or reversed; degenerative sinus node disease does not (Top-up)."),
  ],
  traps=[
    ("“The β-blocker alone explains bradycardia in a patient on metoprolol and digoxin”", "Digoxin is the synergistic culprit; both slow the AV node."),
  ],
  decode=[
    ("Metoprolol for AF, now symptomatic bradycardia — synergistic culprit? [Marrow]", "Digoxin."),
  ],
  punch="Ischaemia, nodal-blocking drugs, hypoxia and hyperkalaemia are all reversible, so they are sought and treated at the same time as atropine, not after it fails.",
)

FLAGS = {
  'ACLS-22': "c: AHA 2025 PALS gives 4 J/kg for subsequent shocks but adds that higher levels may be considered, up to 10 J/kg or the adult maximum; the watch line ‘2 → 4 → 4, not 2 → 4 → 6’ is the default sequence, not a ban on higher doses. Also the first dose may be 2–4 J/kg (2 J/kg for ease of teaching).",
  'ACLS-30': "Card layer line (not the card): ‘procainamide is first choice only when LV function is preserved (PROCAMIO)’ misattributes the trial. PROCAMIO (2017, n 74) found procainamide better than amiodarone in stable regular WCT, including patients with structural heart disease (mean EF about 40%); it did not test or define a preserved-EF restriction. The ‘avoid in CHF’ rule comes from the AHA algorithm, not PROCAMIO. The explanation says so.",
  'ACLS-32': "c: sotalol 100 mg (1.5 mg/kg) over 5 min is the 2020 algorithm dose; the AHA 2025 tachyarrhythmia algorithm no longer mentions sotalol at all (only adenosine, procainamide and amiodarone), although the 2025 guideline text still lists IV sotalol as an option (2b). The figure is still the standard one.",
  'ACLS-35': "Last line ‘Bradycardia = heart rate <60/min’: that is the ECG definition. The AHA 2025 bradycardia algorithm and guideline use a threshold of typically under 50/min for symptomatic bradyarrhythmia. The explanation says so.",
}
