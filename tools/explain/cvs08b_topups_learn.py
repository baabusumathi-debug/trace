# CVS08B top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs08b_learn.py.
# Fields: sub, step (index into cvs08b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions: each top-up's own src (DocT Arrhythmia Q6; DocT GT GT4 Q133; DocT GT GT6 Q1). Standard references (ESC 2021 pacing; AHA 2025 bradycardia algorithm, checked 19 Nov 2026).
T = {}

T['T_cfb2066c'] = dict(
  sub="ACLS → Tachyarrhythmia → Premature ventricular beats",
  step=3,
  intro="Step 3 sorts rhythms by QRS width, and the single early wide beat is the smallest version of that question. In the ICU the beat matters less than what is irritating the ventricle.",
  parts=[
    ('a', "**Ventricular premature beats: premature wide QRS, T wave opposite the QRS, full compensatory pause.** The beat starts in ventricular muscle and spreads cell to cell, not through the Purkinje system, so the QRS is wide and repolarisation runs the opposite way. It does not reset the sinus node, so the next sinus beat comes on time: the pause makes up the lost interval exactly."),
    ('b', "**PACs differ: premature abnormal P wave, narrow QRS, incomplete pause.** An atrial beat conducts normally through the ventricles (narrow QRS) and resets the sinus node, so the pause is shorter than compensatory."),
    ('c', "**ICU causes: low K/Mg, ischaemia, hypoxia, catheter or wire irritation, inotropes — treat the cause, not the beats; couplets or R-on-T in ischaemia warn of VT/VF.** Suppressing ectopy with antiarrhythmics does not improve outcome (CAST showed harm after MI); correcting potassium and magnesium, withdrawing a wire from the ventricle and reducing catecholamines does."),
  ],
  mimic=[
    ("VPB vs PAC with aberrant conduction", "An aberrant PAC has a premature P before it and usually an RBBB shape with an incomplete pause."),
  ],
  traps=[
    ("“Frequent VPBs in the ICU: start amiodarone or lidocaine”", "Look for the cause first: electrolytes, ischaemia, a central line or PA catheter tip in the RV, inotropes."),
  ],
  decode=[
    ("Irregular pulse, early wide bizarre QRS without a preceding P [DocT]", "Ventricular premature beats."),
  ],
  punch="An early wide beat without a P, followed by a full compensatory pause, is a VPB; in the ICU fix the potassium, magnesium, oxygen, wire or inotrope that is causing it.",
)

T['T_991ff9a2'] = dict(
  sub="ACLS → Bradycardia → Sick sinus syndrome",
  step=5,
  intro="Step 5 reads where the slow rhythm starts. In an elderly patient on no drugs, sinus slowing with pauses usually means the node itself is failing.",
  parts=[
    ('a', "**Sick sinus syndrome: idiopathic degenerative fibrosis of the SA node is the commonest cause in the elderly; may coexist with AV-nodal disease and AF (tachy–brady).** Fibrosis replaces pacemaker cells, so the node fires slowly, pauses or fails to exit; the same atrial disease predisposes to AF, and pauses often follow its termination."),
    ('b', "**Exclude reversible causes first: β-blocker, CCB, digoxin, hypothyroidism, hyperkalaemia, hypothermia, raised ICP.** Each slows the node and mimics intrinsic disease (ACLS-40); a pacemaker is not indicated until they are excluded."),
    ('c', "**Symptomatic → permanent pacemaker; atropine or transcutaneous pacing only as a bridge if unstable.** Pacing treats the brady side and allows rate-controlling drugs for the tachy side."),
  ],
  mimic=[
    ("Sick sinus vs drug-induced sinus bradycardia", "Drug-induced resolves when the drug is stopped; fibrosis does not."),
  ],
  traps=[
    ("“Tachy–brady syndrome: give a β-blocker for the AF without pacing”", "The β-blocker deepens the pauses; pace first, then control the rate."),
  ],
  decode=[
    ("Elderly, on no drugs, sinus bradycardia with pauses — cause and fix? [DocT GT]", "Degenerative SA node fibrosis; exclude reversible causes, then permanent pacemaker if symptomatic."),
  ],
  punch="Sick sinus syndrome is a fibrosed SA node, often with AF; exclude drugs, thyroid and potassium, then pace if symptomatic.",
)

T['T_47f36503'] = dict(
  sub="ACLS → Pacing → Unipolar vs bipolar leads",
  step=6,
  intro="Step 6 ends with pacing, and the lead configuration explains the ECG spike size and why some pacemakers oversense.",
  parts=[
    ('a', "**Unipolar: the tip is the cathode and the can is the anode, so the circuit spans the chest wall → large spike, more myopotential and EMI oversensing, pocket muscle stimulation.** A wide circuit acts as a large antenna: it picks up pectoral muscle activity and electromagnetic interference (diathermy), which can inhibit pacing."),
    ('b', "**Bipolar: tip plus a ring electrode about 10 mm proximal → small local circuit, less oversensing; the standard today, so ‘unipolar is better’ is false.** The small spike can be hard to see on the ECG, but sensing is more reliable."),
    ('c', "**One lead per paced chamber; the RA lead usually sits in or near the appendage.** A dual-chamber device has an atrial and a ventricular lead; CRT adds a coronary sinus lead for the LV."),
  ],
  mimic=[
    ("Large vs small pacing spike", "A large spike suggests a unipolar configuration; a tiny or invisible one, bipolar."),
  ],
  traps=[
    ("“Unipolar leads are better”", "Bipolar leads sense more reliably and are the standard."),
  ],
  decode=[
    ("Pacemaker leads — which statement is true? [DocT GT]", "Bipolar has a small local circuit and less oversensing; unipolar is not better."),
  ],
  punch="Unipolar pacing uses the can as the anode, so it gives a large spike and oversenses muscle and diathermy; bipolar keeps the circuit at the tip and is the standard.",
)
