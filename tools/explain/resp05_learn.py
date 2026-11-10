# RESP05 — Explain v3 ("Learn" depth): the pulmonary artery catheter — construction, measurements, insertion and trace, West zones and wedge, derived values, oxygen transport, thermodilution, complications and the trials. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP05.md (12 questions; SWAN-08 West zones asked 4 times, SWAN-12 complications 3 times, SWAN-06 trace twice). Fields as TOX01, plus SPINE, PRIMER and step.
# Cards with no linked question get short explanations with [pattern] decode items.
# Checked online on 11 Nov 2026: Connors 1996 (JAMA abstract), Sandham 2003 (NEJM abstract), Richard 2003 (JAMA abstract), PAC-Man 2005 (n, 65 ICUs, mortality 68 vs 66%, 46 complications),
# ESCAPE 2005 (433, days alive out of hospital, 180-day mortality, adverse events 21.9 vs 11.5%), FACTT catheter arm 2006 (1000, 60-day mortality 27.4 vs 26.3%, about twice the catheter complications, mostly arrhythmias),
# Cochrane (Rajaram 2013: 13 RCTs, 5,686 patients, RR 1.02 general ICU, 0.98 high-risk surgery), Schwann 2011 (5,065 CABG, mortality 3.5 vs 1.7%), Chiang 2015 (2,063,337, mortality 4.6 vs 3.1%),
# CSWG cardiogenic shock registry (Garan, JACC HF 2020: 1,414 patients, no PAC vs complete profiling adjusted OR 1.57), zone 3 criteria (LITFL, Deranged Physiology), insertion distances and balloon ≤1.5 mL (LITFL),
# PA rupture incidence and mortality (several sources, ranges differ), ScvO2–SvO2 relationship (LITFL), 2022 ESC/ERS haemodynamic definition of pulmonary hypertension.
# Second review 11 Nov 2026 re-checked online: thermodilution error sources (LITFL, Deranged Physiology), normal DO2I/VO2I/SVI/pressures (Edwards normal values card), contraindications (UCSF Hospital Handbook, Deranged Physiology), RV vs PA contour (LHSC), complication rates (Deranged Physiology; TTUHSC chapter), rupture management (Deranged Physiology), PACCS registry entry, all trial figures.

SPINE = [
  ("The catheter and what it reads", "A balloon-tipped catheter floats with the blood through the right heart into the pulmonary artery, where it measures pressures, cardiac output and mixed venous saturation directly, and everything else is calculated from those."),
  ("When to float one, and when not", "It is a diagnostic tool kept today for pulmonary hypertension, transplant work-up, cardiogenic shock and right ventricular failure, and avoided where the catheter cannot safely cross the right heart."),
  ("Floating it to the wedge", "With the balloon inflated in the right atrium the catheter is carried through the right ventricle into the pulmonary artery and wedges, and each chamber is recognised by its own waveform and pressure."),
  ("When the wedge means left atrium", "An occluded branch reads left atrial pressure only in West zone 3, where blood stays continuous from the tip to the left atrium, so the tip must lie there and the value is read at end-expiration."),
  ("Numbers built from the measurements", "Resistances follow from pressure drop divided by flow, oxygen delivery and uptake from flow times oxygen content, and cardiac output itself from the thermodilution curve, inversely to its area."),
  ("Harm, the trials and the verdict", "The catheter causes arrhythmias, infarction and rare but often fatal pulmonary artery rupture, and no randomised trial has shown that it improves survival."),
]

PRIMER = "A fluid-filled catheter measures pressure only after it is zeroed to atmosphere at the level of the right atrium (the phlebostatic axis, fourth intercostal space in the mid-axillary line). Preload is a volume, the end-diastolic volume, but bedside monitors measure pressures and use them as stand-ins, which works only as long as ventricular compliance is normal. Flow, pressure and resistance follow the same rule as an electric circuit: resistance is the pressure drop across a vascular bed divided by the flow through it. Oxygen content is about 1.34 mL per gram of haemoglobin times the saturation, so delivery is flow times content and uptake is flow times the arterial–venous content difference."

L = {}

L['SWAN-01'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Construction",
  step=1,
  intro="Step 1 starts with the device. The pulmonary artery (Swan–Ganz) catheter is a long, balloon-tipped tube that the blood itself carries through the right heart; each lumen opens at a set distance from the tip, so each reads a different chamber once the tip is in the pulmonary artery.",
  parts=[
    ('a', "**110 cm long, 4–8 Fr, passed through an introducer sheath.** The adult catheter is usually 7–7.5 Fr, marked every 10 cm so the operator knows how far it has gone. The sheath is a larger cannula left in the vein, so the catheter can be advanced, withdrawn or changed without new venepuncture."),
    ('b', "**1.5 mL of air.** That is the maximum for the adult (7 Fr) balloon; the smaller 5 Fr balloon takes 0.75–1 mL, which is why your notes show both. Air, not liquid, is used, so the balloon deflates at once and so a rupture releases only a small bubble. Over-inflation, or inflating with the tip already in a small distal branch, is the main route to pulmonary artery rupture (SWAN-12)."),
    ('c', "**Distal (yellow): PA pressure, wedge and mixed venous blood; proximal (blue): opens in the RA, for CVP, drugs, fluids and the cold injectate; thermistor: blood temperature near the tip; balloon (red): inflation.** The proximal port lies about 30 cm from the tip, so it sits in the right atrium when the tip is in the pulmonary artery; the thermistor lies about 4 cm from the tip. When the balloon is inflated, the distal lumen looks forward past a blocked branch and reads the pressure downstream — the wedge or pulmonary artery occlusion pressure. Nothing caustic or hyperosmolar goes down the distal lumen, because it opens into a small pulmonary artery."),
  ],
  mimic=[
    ("Distal port vs proximal port", "Distal (tip) reads the pulmonary artery and, with the balloon up, the wedge; proximal (about 30 cm back) reads the right atrium and is where the injectate goes."),
  ],
  traps=[
    ("“The balloon is inflated to measure central venous pressure”", "CVP comes from the proximal port with the balloon down; the balloon is inflated to measure the occlusion (wedge) pressure, which reflects left atrial pressure. 25% of the DocT GT cohort missed this."),
    ("“Continuous cardiac output or RV ejection fraction is the balloon’s job”", "Those come from special catheters with a heating filament or a fast-response thermistor; the balloon’s only jobs are flotation and occlusion."),
  ],
  decode=[
    ("Septic shock patient with a PAC; the balloon at the tip is inflated to occlude a small PA branch — purpose of this feature? [DocT GT]", "Measuring pulmonary artery occlusion (wedge) pressure, a stand-in for left atrial pressure."),
    ("[pattern] Maximum balloon volume in an adult PAC?", "1.5 mL of air."),
  ],
  punch="Four lumens, each opening at a fixed point: the tip reads the pulmonary artery and, with the 1.5 mL balloon up, the wedge; the proximal port reads the right atrium and takes the injectate; the thermistor times the cold.",
)

L['SWAN-02'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Measured and derived values",
  step=1,
  intro="Step 1 continues: what the catheter actually measures, and what is only calculated. Examiners test the line between the two.",
  parts=[
    ('a', "**Directly measured: CVP or RA pressure, RV and PA pressures, wedge pressure, cardiac output, mixed venous saturation.** Pressures come from the transducer, cardiac output from thermodilution (SWAN-11), and mixed venous saturation from blood drawn from the distal port or read by a fibreoptic catheter. Systemic blood pressure and heart rate come from the arterial line and ECG, not the catheter."),
    ('b', "**Derived: SVR and PVR, cardiac index, stroke volume index, LV and RV stroke work index, oxygen delivery and uptake.** Each is arithmetic on measured values (SWAN-09, 10), so any error in the measurement — a wedge read outside zone 3, a bad thermodilution curve — is carried into every derived number."),
  ],
  mimic=[
    ("Wedge pressure vs LV preload", "Wedge ≈ left atrial pressure ≈ LV end-diastolic pressure only when there is no mitral disease, no zone 1–2 lung and normal LV compliance; preload itself is a volume."),
  ],
  traps=[
    ("“Stroke volume and SVR are measured by the catheter”", "Both are calculated: stroke volume is CO ÷ HR, SVR is the pressure drop ÷ CO."),
  ],
  decode=[
    ("[pattern] Which of these is derived rather than measured by a PAC?", "SVR, PVR, cardiac index, stroke volume index, stroke work, DO₂ and VO₂."),
  ],
  punch="The catheter measures pressures, cardiac output and mixed venous saturation; resistances, indices and oxygen transport are arithmetic on those, and carry their errors.",
)

L['SWAN-03'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Indications today",
  step=2,
  intro="Step 2 asks when the catheter is still worth floating. After the trials (SWAN-13) it moved from routine ICU monitoring to a few situations where the right-heart pressures themselves are the diagnosis or decide the treatment.",
  parts=[
    ('a', "**Pulmonary hypertension: diagnosis and evaluation.** Right-heart catheterisation is the reference test: the 2022 ESC/ERS definition is a mean PA pressure above 20 mmHg, and a wedge ≤15 mmHg with PVR above 2 Wood units makes it pre-capillary, while a wedge above 15 mmHg makes it post-capillary. Echo can only estimate these."),
    ('b', "**Heart, lung and liver transplant candidacy.** Fixed pulmonary hypertension or a high PVR can rule out heart transplant (the donor right ventricle fails against it) or liver transplant (portopulmonary hypertension), so it is measured directly."),
    ('c', "**Cardiogenic shock and right ventricular failure.** Here the catheter separates LV from RV failure and guides inotropes and mechanical support. The best data are observational: in the Cardiogenic Shock Working Group registry (Garan, JACC Heart Failure 2020; 1,414 patients) no PAC assessment carried higher in-hospital mortality than complete haemodynamic profiling (adjusted OR 1.57, 95% CI 1.06–2.33), which shows association, not cause. The randomised test is the Pulmonary Artery Catheter in Cardiogenic Shock Trial (PACCS, NCT05485376; early PAC versus delayed or no PAC, primary outcome in-hospital mortality), still listed as recruiting at its last registry update."),
    ('d', "**Mixed shock, or volume status unclear in shock.** When echo and bedside signs disagree, the catheter separates hypovolaemic, distributive and cardiogenic components, and cardiogenic from non-cardiogenic pulmonary oedema (wedge above or below about 18 mmHg)."),
    ('e', "**High-risk cardiac surgery.** It is still common in cardiac theatres, though observational studies have not shown benefit (SWAN-14)."),
  ],
  mimic=[
    ("Diagnostic use vs therapeutic use", "The catheter is a diagnostic tool: it shows tamponade (equalised diastolic pressures), a left-to-right shunt (an oxygen step-up), or cardiogenic oedema; it treats nothing by itself."),
  ],
  traps=[
    ("“PAC-guided therapy improves survival in septic shock”", "No randomised trial showed benefit (SWAN-13); in a general ICU there are few if any absolute indications."),
  ],
  decode=[
    ("[pattern] Strongest current indication for a PAC?", "Diagnosis of pulmonary hypertension (and transplant work-up); in the ICU, cardiogenic shock and RV failure."),
  ],
  punch="The catheter now earns its place where the right-heart numbers are the answer: pulmonary hypertension, transplant work-up, cardiogenic shock and RV failure.",
)

L['SWAN-04'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Contraindications and high-risk states",
  step=2,
  intro="Step 2 continues with the other side: when the catheter should not cross the right heart, or crosses it at real risk. Each item follows from where the catheter goes and what it touches.",
  parts=[
    ('a', "**Absolute: infection at the site, RV assist device, RA or RV thrombus or mass, no consent.** A clot or tumour in the right heart can be dislodged into the lungs; an RV assist device has cannulae in the right heart that the catheter can tangle with or be drawn into, and the device itself carries the flow the catheter is meant to measure. Many texts (for example the UCSF Hospital Handbook) also list right-sided endocarditis and a mechanical tricuspid or pulmonary valve as absolute, because the catheter can dislodge vegetations into the lung or be trapped by, and damage, a mechanical valve (see FLAGS)."),
    ('b', "**Relative: coagulopathy, platelets <50,000, electrolyte disturbance that favours arrhythmia, severe acid–base disturbance.** The catheter touches the RV wall and outflow tract, so low potassium or magnesium and acidosis make ectopics turn into sustained VT; bleeding risk applies to the puncture and to any rupture."),
    ('c', "**High risk: severe pulmonary hypertension or Eisenmenger, LBBB, pacemaker or ICD, tricuspid or pulmonary stenosis or prosthesis, persistent left SVC.** In pulmonary hypertension the stiff vessels rupture more easily (SWAN-12). In LBBB, the catheter brushing the right bundle can add RBBB, and both bundles blocked means complete heart block, so external pacing must be ready. Transient catheter-induced RBBB is uncommon (about 0.05–5% of insertions), and in one series of 82 patients with LBBB none developed complete block during insertion, so the risk is real but small; the precaution is cheap. Pacing leads can be dislodged or entangled; a left SVC drains into the coronary sinus, so a left-sided catheter will not follow the usual path."),
  ],
  mimic=[
    ("LBBB vs RBBB before insertion", "Pre-existing RBBB adds little risk; pre-existing LBBB is the one that can become complete heart block."),
  ],
  traps=[
    ("“LBBB is no concern because the catheter stays on the right”", "The catheter can cause RBBB as it passes the RV outflow tract; on top of LBBB that is complete heart block."),
  ],
  decode=[
    ("[pattern] Which conduction disturbance makes PAC insertion high risk, and why?", "LBBB: catheter-induced RBBB gives complete heart block."),
  ],
  punch="Avoid floating through a heart that holds clot or a device, and in LBBB have pacing ready, because the catheter can block the right bundle as well.",
)

L['SWAN-05'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Insertion",
  step=3,
  intro="Step 3 floats the catheter. The site decides how easily the catheter follows the natural curve into the pulmonary artery, and the 10-cm markings tell the operator which chamber to expect next, so a missing waveform at the expected depth means coiling.",
  parts=[
    ('a', "**Right IJV > left subclavian > right subclavian > left IJV.** The right internal jugular gives the straightest route to the tricuspid valve, and the left subclavian’s curve matches the catheter’s curve into the outflow tract; the left IJ has the most bends."),
    ('b', "**RA at 15–20 cm; about 10 cm more to each of RV, PA and wedge.** From the right IJ that gives roughly RV 25–30 cm, PA 35–40 cm and wedge 40–50 cm. If the RV trace has not appeared by about 30 cm, or the PA trace by about 50 cm, the catheter is coiling in the atrium or ventricle: deflate, withdraw to the RA and try again, because coils knot."),
    ('c', "**Inflate in the right atrium, before crossing the tricuspid valve; always deflate before withdrawing.** Inflated, the balloon is carried by the flow like a sail and cushions the tip, so it is less likely to irritate the RV wall or perforate it; your notes’ ‘inflate once the RV trace appears’ is not standard practice. Withdrawing with the balloon up can tear the tricuspid or pulmonary valve, and leaving it up after wedging occludes the branch, causing infarction or rupture (SWAN-12)."),
    ('d', "**Depth to wedge: subclavian 35–50 cm, internal jugular 40–55 cm, femoral 60 cm.** From the femoral vein the catheter has the IVC and a sharp turn to make, so it is longer and often needs fluoroscopy."),
  ],
  mimic=[
    ("Balloon left up vs catheter knotting", "A balloon left inflated causes infarction and rupture; knotting comes from advancing too far without the expected waveform change."),
  ],
  traps=[
    ("“Balloon left inflated after placement: the worst risk is knotting in the atrium”", "Knotting comes from over-advancing a coiling catheter; the balloon left up occludes the branch, and the most serious result is pulmonary artery rupture (66% right in DocT QBank)."),
    ("“Inflate the balloon once the RV trace appears”", "Inflate in the RA so the tip is cushioned as it crosses the RV."),
  ],
  decode=[
    ("Balloon accidentally left inflated after placement — most serious complication? [DocT]", "Pulmonary artery rupture (not knotting, pacing wire displacement or thrombus)."),
    ("[pattern] From the right IJ, at what depth should the RV trace appear?", "About 25–30 cm; no RV by 30 cm suggests coiling."),
  ],
  punch="Inflate in the right atrium, expect a new chamber every 10 cm, deflate before every withdrawal, and never leave the balloon up.",
)

L['SWAN-06'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Flotation trace",
  step=3,
  intro="Step 3 continues with the trace on the monitor as the catheter advances: right atrium, right ventricle, pulmonary artery, wedge. Each transition is recognised by one change in the waveform, and both real questions test whether you can name the chamber from its shape, not from the number alone.",
  parts=[
    ('a', "**1 = right atrium; 2 = right ventricle; 3 = pulmonary artery; 4 = wedge.** The atrial trace is a low venous waveform (mean about 2–6 mmHg) with a, c and v waves; the wedge looks like it again, because it is a left atrial waveform seen through the lung."),
    ('b', "**RA → RV: systolic pressure jumps; diastolic stays near zero.** The ventricle generates 20–30 mmHg in systole but relaxes to near the atrial pressure in diastole, so the trace becomes tall and wide-swinging. Its diastolic part slopes upward as the ventricle fills. This is when ectopics and VT appear, so the catheter is advanced through the ventricle without pausing."),
    ('c', "**RV → PA: diastolic pressure rises (the diastolic step-up) and a dicrotic notch appears; systolic is unchanged.** Systolic is the same because the open pulmonary valve joins the RV and PA in systole. In diastole the pulmonary valve closes and holds the arterial pressure at 8–15 mmHg instead of letting it fall to near zero; the notch is that valve closing. The diastolic part now slopes downward as blood runs off into the lung, the opposite of the ventricle’s upward filling slope; this contour is a useful extra sign, but the diastolic step-up and the notch are the main ones."),
    ('d', "**PA → wedge: the pulsatile trace is lost, replaced by an atrial-type trace at or below PA diastolic pressure.** The inflated balloon stops flow in that branch, so the tip sees the still column of blood leading to the left atrium. A wedge reading above PA diastolic pressure is wrong (over-wedging, or a zone 1–2 tip reading alveolar pressure, SWAN-08) unless there are large v waves from mitral regurgitation."),
  ],
  table=dict(title="What changes at each step", head=["Position", "Systolic", "Diastolic", "Shape"], rows=[["Right atrium", "low (mean 2–6)", "—", "a, c and v waves"], ["Right ventricle", "**jumps to 20–30**", "near zero, rising through diastole", "tall, no notch"], ["Pulmonary artery", "unchanged (20–30)", "**steps up to 8–15**, falling through diastole", "**dicrotic notch**"], ["Wedge", "pulsation lost", "mean ≤ PA diastolic", "a and v waves"]]),
  mimic=[
    ("RV vs PA trace", "Same systolic. PA has a raised diastolic, a dicrotic notch and a downward diastolic slope; RV has diastolic near zero sloping upward."),
    ("Wedge vs RA trace", "Both are atrial waveforms; the wedge is reached only after the PA trace, and its mean normally sits a few mmHg below PA diastolic."),
  ],
  traps=[
    ("“A low pressure of 10 mmHg must be the wedge”", "A dicrotic notch means the pulmonary valve is behind the tip, so the trace is pulmonary artery; a wedge trace has no notch and no arterial pulsation. The number alone does not name the chamber."),
    ("“RV to PA is recognised by a rise in systolic pressure”", "Systolic is shared; the rise is in diastolic (SWAN-15d)."),
  ],
  decode=[
    ("Septic shock patient with a Swan–Ganz; low-amplitude waveform with a clear dicrotic notch, pressure 10 mmHg — which pressure? [DocT GT · PYQ]", "Pulmonary artery pressure: the dicrotic notch decides it, not the value."),
    ("PA catheter waveforms as the catheter advances [NEET 2024]", "RA → RV (systolic jumps) → PA (diastolic steps up, dicrotic notch) → wedge (pulsation lost, atrial-type trace)."),
  ],
  punch="Systolic jumps when the catheter enters the ventricle; diastolic steps up and a dicrotic notch appears when it enters the pulmonary artery; pulsation vanishes when it wedges — the shape names the chamber, not the number.",
)

L['SWAN-07'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Normal right-heart pressures",
  step=3,
  intro="Step 3 ends with the numbers each chamber should read. The relationships matter more than the exact ranges, which vary between texts.",
  parts=[
    ('a', "**Right atrium 0–3 mmHg; RV 20–30/0–8; PA 20–30/8–15; wedge 8–12.** References differ: a widely used set (Edwards) gives RA 2–6, RV 15–25/0–8, PA 15–25/8–15 and wedge 6–12, and others give PA diastolic as low as 4; normal mean PA pressure is about 10–20 (see FLAGS). The fixed relationships are: RV and PA systolic are equal (open valve in systole), PA diastolic is above RV diastolic (closed valve), and wedge is a few mmHg below PA diastolic. A mean PA pressure above 20 mmHg is pulmonary hypertension (SWAN-03a)."),
  ],
  mimic=[
    ("PA diastolic vs wedge", "Normally wedge is 1–5 mmHg below PA diastolic; a widening gap means raised PVR (pre-capillary disease), since PA diastolic then exceeds left atrial pressure."),
  ],
  traps=[
    ("“PA systolic is higher than RV systolic”", "They are the same in the absence of pulmonary stenosis."),
  ],
  decode=[
    ("[pattern] Normal PA pressure and wedge?", "PA about 25/10 (mean under 20) mmHg; wedge 6–12 mmHg."),
  ],
  punch="RV and PA share the systolic, the pulmonary valve lifts PA diastolic above RV diastolic, and the wedge sits just below PA diastolic.",
)

L['SWAN-08'] = dict(
  sub="Respiratory → Pulmonary artery catheter → West zones and the wedge pressure",
  step=4,
  intro="Step 4 is the card asked most often in this deck. The wedge is meant to read left atrial pressure through a still column of blood, but the pulmonary capillaries run through the alveolar walls; wherever alveolar pressure is higher than the vascular pressure, it squeezes the capillaries shut and the catheter reads the alveolus instead. West’s zones describe where that happens, and the questions test the zone order, the zone for the wedge, the effect of PEEP and the V/Q gradient that comes from the same physics.",
  parts=[
    ('a', "**Zone 1: PA > Pa > Pv. Zone 2: Pa > PA > Pv. Zone 3: Pa > Pv > PA (PA = alveolar).** Upright, gravity adds about 1 cmH₂O of vascular pressure per centimetre below the top of the lung, while alveolar pressure is the same everywhere. At the apex alveolar pressure can exceed arterial pressure, so capillaries collapse and there is no flow (zone 1, alveolar dead space); normally zone 1 hardly exists, but it appears with low pulmonary pressure or high airway pressure. In the middle, flow depends on arterial minus alveolar pressure (zone 2, the ‘waterfall’). At the base both arterial and venous pressure exceed alveolar pressure, the vessels stay open and flow depends on arterial minus venous pressure (zone 3)."),
    ('b', "**Zone 3: only there is there a continuous column of blood from the tip to the left atrium; elsewhere the wedge reads alveolar pressure.** With the balloon up, flow stops and the tip is connected to the left atrium by a still column of blood, but only if no capillary along that path is compressed. In zones 1 and 2 alveolar pressure exceeds pulmonary venous pressure, the capillaries collapse, and the transducer reads airway pressure. Because a flow-directed catheter follows the most flow, it usually goes to dependent, zone 3 lung on its own, which in a supine patient is posterior."),
    ('c', "**Tip at or below the left atrium on a lateral film; respiratory swing in the wedge <50% of the swing in alveolar pressure (plateau – PEEP); wedge changes by <50% of a change in PEEP.** Each check asks the same thing: does the wedge follow the left atrium or the airway? If it rises and falls with each breath by as much as the airway pressure, or moves almost one-for-one with PEEP, it is reading the alveolus. Other signs of zone 3: wedge below PA diastolic, and clear a and v waves (a smooth trace suggests zones 1–2)."),
    ('d', "**End-expiration.** That is when pleural and alveolar pressures are closest to atmospheric, so the intravascular reading is nearest the true transmural pressure. On a ventilator end-expiration is the low point just before the inspiratory rise; breathing spontaneously it is the high point just before the inspiratory dip. PEEP still adds to the reading at end-expiration, so high PEEP overestimates the true filling pressure."),
  ],
  table=dict(title="The three zones", head=["Zone", "Pressure order", "Flow depends on", "Wedge reads"], rows=[["1 (apex)", "PA > Pa > Pv", "no flow (dead space)", "alveolar pressure"], ["2 (middle)", "Pa > PA > Pv", "Pa − PA", "alveolar pressure"], ["3 (base, dependent)", "**Pa > Pv > PA**", "Pa − Pv", "**left atrial pressure**"]]),
  mimic=[
    ("Zone 2 vs zone 3", "In both arterial pressure exceeds alveolar; in zone 3 venous pressure also exceeds alveolar, so the whole path stays open when flow stops."),
    ("Wedge high from fluid vs high from PEEP", "Fluid raises a wedge with clear a and v waves and little respiratory swing; PEEP-driven readings swing with each breath and move almost one-for-one with PEEP changes."),
  ],
  traps=[
    ("“Excess PEEP converts zone 2 to zone 3 and improves V/Q”", "The reverse: excess PEEP raises alveolar pressure above vascular pressure, converting zones 2 and 3 to zone 1, which adds alveolar dead space and makes the wedge read airway pressure."),
    ("“Excess PEEP lowers PVR as volume approaches TLC”", "PVR is lowest near FRC; at high lung volumes alveolar vessels are stretched and compressed and PVR rises."),
    ("“Upright, V/Q is greater at the bases” (or “ventilation is greater at the apex”)", "Both ventilation and perfusion are greater at the bases, but perfusion rises more steeply, so V/Q is highest at the apex (about 3) and lowest at the base (about 0.6). Only 35% of the DocT GT cohort chose this as the false statement; supine, the same gradient runs from posterior (low V/Q) to anterior (high V/Q)."),
    ("“Hypovolaemia makes the wedge more reliable”", "Low vascular pressures let alveolar pressure win, converting zone 3 to zone 2 or 1, so the wedge reads high and misleads."),
  ],
  decode=[
    ("Pressures Pa > Pv > PA (alveolar) — which West zone? [NEET 2025]", "Zone 3."),
    ("PAC in a ventilated patient — in which West zone is the wedge most accurate? [DocT GT]", "Zone 3: continuous blood column to the left atrium."),
    ("Most likely consequence of excessive PEEP in ARDS, by West zones? [DocT GT]", "Increase in alveolar dead space by converting zone 2 or 3 into zone 1."),
    ("All true except: ventilation greater at bases / perfusion greater at bases / V/Q greater at bases / V/Q greater anteriorly when supine [DocT GT]", "V/Q greater at the bases is false: V/Q is highest at the apex."),
  ],
  extra=[
    dict(q="Why is V/Q highest at the apex if ventilation is lowest there?", a="Gravity affects blood far more than gas: perfusion falls steeply from base to apex while ventilation falls only gently, so the ratio rises towards the apex (about 3) and falls towards the base (about 0.6)."),
  ],
  punch="The wedge reads the left atrium only through open zone 3 vessels, so the tip must sit below the left atrium and the reading taken at end-expiration; high PEEP or hypovolaemia turn zone 3 into zones 2 and 1, adding dead space and making the wedge read the airway.",
)

L['SWAN-09'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Derived haemodynamic formulae",
  step=5,
  intro="Step 5 turns measurements into derived numbers. Each resistance is the pressure drop across a bed divided by the flow through it; the only real question here (Marrow) tests a perfusion pressure built the same way.",
  parts=[
    ('a', "**SVR = 80 × (MAP − CVP) ÷ CO.** The systemic bed runs from the aorta (MAP) to the right atrium (CVP). The 80 converts Wood units (mmHg·min/L) to dyn·s·cm⁻⁵; normal SVR is 800–1200 dyn·s·cm⁻⁵."),
    ('b', "**PVR = 80 × (mean PAP − wedge) ÷ CO.** The pulmonary bed runs from the pulmonary artery to the left atrium, which the wedge stands in for. Normal is below about 250 dyn·s·cm⁻⁵ (about 3 Wood units); the 2022 pulmonary hypertension definition uses above 2 Wood units for pre-capillary disease."),
    ('c', "**Cardiac index = CO ÷ body surface area.** Normal 2.5–4 L/min/m²; below 2.2 with a high wedge is the classic cardiogenic shock profile."),
    ('d', "**Stroke volume index = cardiac index ÷ heart rate.** Normal about 33–47 mL/m² per beat. A low cardiac index with a normal SVI means the problem is rate, not pump."),
  ],
  mimic=[
    ("SVR vs PVR", "SVR uses MAP minus CVP; PVR uses mean PAP minus wedge. Mixing up the downstream pressure is the common slip."),
  ],
  traps=[
    ("“LV coronary perfusion pressure = MAP − CVP”", "The LV is perfused in diastole against its own end-diastolic pressure: LV CPP = diastolic BP − wedge (LVEDP). With DBP 72 and PAOP 10 that is 62 mmHg."),
  ],
  decode=[
    ("LV coronary perfusion pressure from SBP 133, DBP 72, PAOP 10? [Marrow]", "62 mmHg: diastolic BP − PAOP."),
    ("[pattern] Formula for PVR?", "80 × (mean PAP − wedge) ÷ CO."),
  ],
  extra=[
    dict(q="Coronary perfusion pressure of each ventricle", a="LV: diastolic BP − PAOP (LVEDP), because the thick LV wall squeezes its own vessels shut in systole and it fills only in diastole. RV: MAP − mean RV pressure, because the thin RV is perfused through the whole cycle; a rising RV pressure in pulmonary hypertension starves the RV of flow."),
  ],
  punch="Every resistance is pressure drop ÷ flow × 80: MAP − CVP for the body, mean PAP − wedge for the lung; LV coronary perfusion is diastolic pressure minus wedge.",
)

L['SWAN-10'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Oxygen transport",
  step=5,
  intro="Step 5 continues with oxygen. Because the catheter samples truly mixed venous blood from the pulmonary artery, it measures the arterial–venous difference directly, and with the cardiac index that gives delivery and uptake.",
  parts=[
    ('a', "**DO₂I = CI × 13.4 × Hb × SaO₂.** Flow times arterial oxygen content (dissolved oxygen ignored). The 13.4 is 1.34 mL O₂ per gram × 10, converting Hb in g/dL to per litre. Normal is about 500–600 mL/min/m²."),
    ('b', "**VO₂I = CI × 13.4 × Hb × (SaO₂ − SvO₂).** The reverse Fick: uptake is flow times the content taken out. Normal is about 120–160 mL/min/m², an extraction of about 22–30%."),
    ('c', "**Mixed venous saturation 60–80%.** About 65–75% in most texts. A low SvO₂ means delivery is short of demand (low output, anaemia, hypoxaemia, high demand); a high SvO₂ in shock means the tissues are not extracting (sepsis, shunting, cytotoxic hypoxia), not that all is well. Central venous ScvO₂ from the SVC is normally 2–3% lower than SvO₂, but in shock the order reverses and ScvO₂ runs about 5% higher, because splanchnic blood in the IVC is extracted more."),
    ('d', "**Fick cardiac output = VO₂ ÷ (10 × arteriovenous content difference); content difference = 1.34 × Hb × (SaO₂ − SvO₂).** The ×10 again turns mL/dL into mL/L. In practice VO₂ is often assumed (about 125 mL/min/m²), which makes the Fick output an estimate."),
  ],
  mimic=[
    ("SvO₂ vs ScvO₂", "SvO₂ (pulmonary artery) mixes SVC, IVC and coronary sinus blood; ScvO₂ (SVC) misses the lower body and heart. They move together but are not interchangeable."),
  ],
  traps=[
    ("“A high SvO₂ in septic shock excludes tissue hypoxia”", "It may mean the tissues cannot extract oxygen; lactate and the CO₂ gap help."),
  ],
  decode=[
    ("[pattern] Normal mixed venous saturation, and what a low value means?", "About 65–75% (card 60–80%); low means delivery is not meeting demand."),
  ],
  punch="Delivery is flow times content, uptake is flow times the content removed, and SvO₂ is the balance between them.",
)

L['SWAN-11'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Thermodilution cardiac output",
  step=5,
  intro="Step 5 ends with how the catheter measures flow. A known amount of cold is added upstream and its dilution is timed downstream; the more blood flows past, the faster and smaller the temperature dip.",
  parts=[
    ('a', "**Cold dextrose or saline is injected through the proximal (RA) port; the thermistor near the tip records the fall in blood temperature.** About 10 mL is usual in adults; 5 mL (your notes) also works, but the smaller temperature dip makes rewarming and technique errors weigh more. It is injected rapidly, three to five times at the same phase of respiration (usually end-expiration, since output varies by up to about 10% with breathing), and the readings averaged."),
    ('b', "**Output is inversely proportional to the area under the curve (Stewart–Hamilton).** CO = V × (Tb − Ti) × K ÷ ∫ΔTb dt: the injectate volume and the temperature gap are known, so a large area under the temperature–time curve means the cold lingered, which means slow flow."),
    ('c', "**High output: small, quick curve. Low output: large, prolonged curve.** Errors follow from the formula: anything that shrinks the area overestimates output, so too little or too warm injectate overestimates it, and too much underestimates it. Tricuspid regurgitation usually underestimates output, because cold blood washes back and forth and the curve is drawn out; intracardiac shunts make the reading unreliable, as the catheter measures right-sided flow, which then differs from left-sided output."),
  ],
  mimic=[
    ("Area under the curve vs output", "Inverse: a big area means low output (SWAN-15g)."),
  ],
  traps=[
    ("“Output is proportional to the area under the curve”", "It is inversely proportional."),
  ],
  decode=[
    ("[pattern] Large, prolonged thermodilution curve indicates?", "Low cardiac output."),
  ],
  punch="Fast flow washes the cold past quickly, so a small curve is high output and a large curve low output.",
)

L['SWAN-12'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Complications",
  step=6,
  intro="Step 6 opens with harm, the second most-asked card. Complications fall into three groups by when they happen — getting into the vein, passing through the heart, and leaving the catheter in — and all three questions test the most dangerous of them: pulmonary artery rupture after balloon inflation.",
  parts=[
    ('a', "**Venous access: bleeding, arterial puncture, pneumothorax, air embolism, neuropathy.** These are the same as for any central line; in PAC-Man they made up most of the 10% complication rate (haematoma 4%, arterial puncture 3%, a few pneumothoraces), alongside arrhythmias needing treatment in 3%."),
    ('b', "**Passage: atrial and ventricular ectopics, VT or VF, RBBB, knotting.** The tip touching the RV outflow tract triggers ectopics, which are common and usually stop once the catheter moves on; sustained VT is unusual and VF rare (in two large series only about 1.3–1.5% needed drugs, a thump or cardioversion). Transient RBBB occurs in about 0.05–5% and matters in LBBB (SWAN-04). Knotting (about 1% in one review) comes from advancing too far without the expected trace change (SWAN-05b)."),
    ('c', "**Residence: thromboembolism, pulmonary infarction, infection and endocarditis, valve and endocardial damage, minor tricuspid regurgitation.** Infarction follows a tip that migrates distally into a permanent wedge, or a balloon left up: the branch is occluded for hours, and a wedge-shaped opacity appears (0–1.4% in one large series, often only a new shadow on the film). Infection rises with the days the catheter stays in."),
    ('d', "**Pulmonary artery rupture: 0.03–0.2%, mortality 41–70%.** Published figures vary: a 17-year series of 32,442 catheterised patients found 0.031% with 7 of 10 dying (70%), other large series 0.06–0.2%, and one review quotes 0.2% with 30% mortality; the card’s range sits within these. The message is the same: rare and often fatal. It happens when the balloon is inflated in a distal or stiff branch, or over-inflated: pulmonary hypertension, age over 60, female sex, anticoagulation, hypothermia (a stiffer catheter) and mitral disease raise the risk. It presents at once with haemoptysis, hypoxaemia and often collapse, usually right-sided. Management: do not pull the catheter out (some advise withdrawing it slightly and re-inflating the balloon to occlude the bleeding branch); secure the airway and isolate the lung (double-lumen tube, bronchial blocker or main-bronchus intubation of the good side); until the lung is isolated, put the bleeding side down so blood does not flood the good lung, and add PEEP; reverse anticoagulation; definitive control is angiographic embolisation or surgery. A pseudoaneurysm can form and rebleed days later."),
  ],
  table=dict(title="Rupture vs infarction", head=["", "Pulmonary artery rupture", "Pulmonary infarction"], rows=[["Cause", "balloon inflated in a distal or stiff branch", "tip migrated distally, or balloon left up for hours"], ["Timing", "**sudden, at inflation**", "hours to days"], ["Picture", "**brisk haemoptysis, hypoxaemia, collapse**", "pleuritic pain, wedge-shaped opacity, minor haemoptysis"], ["Outcome", "mortality roughly 30–70%", "usually self-limiting"]]),
  mimic=[
    ("Rupture vs air embolism", "Air embolism comes from an open line or a burst balloon and causes collapse without haemoptysis; rupture brings blood up the airway."),
    ("Rupture vs knotting", "Knotting causes failure to advance or withdraw and arrhythmias, not haemoptysis."),
  ],
  traps=[
    ("“Balloon left inflated: knotting is the most serious risk”", "Knotting is a passage problem from over-advancing; the inflated balloon leads to infarction and, most seriously, rupture. DocT QBank 66% right (93% on the GT repeat)."),
    ("“Sudden haemoptysis just after wedging is pulmonary infarction”", "Infarction develops over hours with minor haemoptysis; sudden haemoptysis with collapse right after inflation is rupture."),
    ("“The balloon may be inflated with saline to make it safer”", "Always air, at most 1.5 mL, inflated slowly while watching the trace; stop as soon as it wedges."),
  ],
  decode=[
    ("Balloon accidentally left inflated after placement — most serious potential complication? [DocT, DocT GT]", "Pulmonary artery rupture."),
    ("Septic shock, PAC; shortly after balloon inflation for wedge — sudden haemoptysis, hypoxaemia, collapse [DocT GT]", "Pulmonary artery rupture (not infarction, air embolism or knotting)."),
    ("[pattern] Incidence and mortality of PA rupture?", "About 0.03–0.2%; mortality roughly 30–70% (card 41–70%)."),
  ],
  punch="The balloon causes the worst harm: left up it infarcts the lung, inflated in a distal or stiff branch it ruptures the artery — sudden haemoptysis and collapse at inflation is rupture until proved otherwise.",
)

L['SWAN-13'] = dict(
  sub="Respiratory → Pulmonary artery catheter → The trials",
  step=6,
  intro="Step 6 continues with the evidence. An observational study suggested harm, and six randomised trials in different populations then tested whether catheter-guided care improves outcome; none showed benefit.",
  parts=[
    ('a', "**Connors 1996 (SUPPORT): 5,735 patients, observational, 5 US teaching hospitals — higher 30-day mortality (OR 1.24), cost and stay.** Propensity matching gave OR 1.24 (95% CI 1.03–1.49); mean hospital cost was $49,300 vs $35,700. Being observational, it could not exclude that sicker patients got catheters, but it triggered the randomised trials."),
    ('b', "**Sandham 2003 (NEJM): 1,994 high-risk surgical patients — no difference; more pulmonary embolism (8 vs 0).** Patients were 60 or older, ASA III–IV; hospital mortality was 7.8% vs 7.7%, and median stay 10 days in both groups."),
    ('c', "**Richard 2003 (JAMA): 676 patients with shock or ARDS, 36 French ICUs — no difference.** Day-28 mortality was 59.4% vs 61.0%, with no difference in organ failure."),
    ('d', "**PAC-Man 2005 (Lancet): 1,041 patients, 65 UK ICUs — no difference; 46 non-fatal complications.** Hospital mortality was 68% vs 66%; complications (10% of insertions) were mostly from cannulation, none fatal."),
    ('e', "**ESCAPE 2005 (JAMA): 433 patients with decompensated heart failure — no difference; more adverse events.** Days alive out of hospital over 6 months were the same (about 133 vs 135), as was 6-month mortality (20% vs 17%); in-hospital adverse events were 21.9% vs 11.5%."),
    ('f', "**FACTT catheter arm 2006 (NEJM): 1,000 patients with ARDS, PAC vs central venous catheter — no difference; more arrhythmias.** 60-day mortality was 27.4% vs 26.3%; the PAC group had about twice as many catheter-related complications, mostly arrhythmias."),
  ],
  mimic=[
    ("Connors vs the randomised trials", "Connors was observational and suggested harm; the randomised trials found neither harm in mortality nor benefit."),
  ],
  traps=[
    ("“PAC-Man showed lower mortality with the catheter”", "No difference (SWAN-15f)."),
    ("“FACTT compared PAC with no catheter”", "It compared PAC with a central venous catheter, in a factorial design alongside the fluid strategy trial."),
  ],
  decode=[
    ("[pattern] Which trial compared PAC with CVP-guided care in ARDS?", "FACTT (ARDS Network, 2006)."),
    ("[pattern] Observational study linking PAC with higher mortality?", "Connors 1996 (SUPPORT), OR 1.24."),
  ],
  punch="One observational study suggested harm and six randomised trials — surgery, shock and ARDS, the UK ICU, heart failure, ARDS again — found no benefit.",
)

L['SWAN-14'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Why it failed",
  step=6,
  intro="Step 6 then asks why accurate-seeming numbers did not help. The catheter is a measuring tool; outcome depends on whether the numbers are right, read correctly, and lead to a treatment that helps.",
  parts=[
    ('a', "**The data may be inaccurate.** Wrong zeroing, zone 1–2 placement, PEEP and poor thermodilution technique all distort the readings."),
    ('b', "**Clinicians often misinterpret the data, and act on them variably.** Surveys found many clinicians could not read a wedge trace correctly, and the trials had no fixed protocol for what to do with the numbers."),
    ('c', "**Wedge pressure correlates poorly with stroke volume.** A pressure stands in for a volume only when compliance is normal; in the stiff or dilated ventricles of ICU patients it does not."),
    ('d', "**Wedge pressure does not predict fluid responsiveness.** Static filling pressures, wedge or CVP, do not tell whether the stroke volume will rise with fluid; dynamic tests do."),
    ('e', "**It prompts excess interventions that may harm.** More fluid, inotropes and procedures followed the numbers, without benefit."),
    ('f', "**It was studied before echocardiography was widespread.** Echo now answers many of the same questions without a catheter in the heart."),
  ],
  mimic=[],
  traps=[
    ("“A low wedge means the patient will respond to fluid”", "Static pressures do not predict fluid responsiveness."),
  ],
  decode=[
    ("[pattern] Main reason PAC use did not improve outcome?", "Its numbers are often wrong or misread, and no treatment protocol based on them has been shown to help."),
  ],
  extra=[
    dict(q="Cardiac surgery evidence", a="Schwann 2011 (5,065 CABG patients, 70 centres, observational) found higher mortality with the catheter in propensity-matched pairs (3.5% vs 1.7%, OR 2.08); Chiang 2015 (over 2 million patients) found higher operative mortality too (4.6% vs 3.1%, adjusted OR 1.34); the Cochrane review (Rajaram 2013, 13 trials, 5,686 patients) found no change in mortality (RR 1.02 general ICU, 0.98 high-risk surgery), stay or cost."),
  ],
  punch="The catheter failed because its numbers are often wrong or misread, pressure is a poor stand-in for volume, and no treatment driven by those numbers has been shown to help.",
)

L['SWAN-15'] = dict(
  sub="Respiratory → Pulmonary artery catheter → Revision: true or false",
  step=6,
  intro="A sweep through the deck. Each statement turns on one detail from an earlier card.",
  parts=[
    ('a', "**False — the proximal lumen opens in the right atrium** (SWAN-01c), about 30 cm from the tip."),
    ('b', "**True — zone 3, for a continuous blood column** to the left atrium (SWAN-08b)."),
    ('c', "**False — wedge is read at end-expiration** (SWAN-08d)."),
    ('d', "**False — RV to PA is recognised by a rise in diastolic pressure** and a dicrotic notch; systolic is shared (SWAN-06c)."),
    ('e', "**True — catheter-induced RBBB on LBBB gives complete heart block** (SWAN-04c)."),
    ('f', "**False — PAC-Man showed no difference** in mortality (SWAN-13d)."),
    ('g', "**False — output is inversely proportional to the area** under the curve (SWAN-11b)."),
  ],
  mimic=[],
  traps=[
    ("“Systolic rises from RV to PA”", "Systolic is the same; the step-up is diastolic."),
  ],
  decode=[
    ("[pattern] True/false on the PAC", "Proximal port in RA, zone 3, end-expiration, diastolic step-up, LBBB risk, PAC-Man neutral, area inverse."),
  ],
  punch="Proximal port in the atrium, tip in zone 3, read at end-expiration, diastolic step-up into the PA, LBBB means pacing ready, and no trial showed benefit.",
)

FLAGS = {}
FLAGS['SWAN-07'] = "Card ranges differ from common references in places: RA 0–3 (Edwards 2–6, LITFL 0–6), PA systolic 20–30 (Edwards 15–25), wedge 8–12 (Edwards 6–12). PA diastolic 8–15 matches Edwards (some texts give 4–12). Watch partly notes this. Explanation gives both; consider adding ‘mean PAP >20 mmHg = pulmonary hypertension (ESC/ERS 2022)’."
FLAGS['SWAN-04'] = "Checked: the UCSF Hospital Handbook lists a mechanical right-heart valve and right-sided endocarditis, thrombus or mass as absolute contraindications, and Deranged Physiology lists valve prostheses, vegetations and endocarditis among contraindications; the card puts prostheses under high-risk and omits endocarditis. Explanation mentions both."
FLAGS['SWAN-09'] = "Marrow’s question tests LV coronary perfusion pressure = diastolic BP − PAOP (and RV CPP = MAP − mean RV pressure), not on the card (qpack note ‘Add to SWAN-09’). Explanation and extra give it."
FLAGS['SWAN-14'] = "Watch says Chiang (over 2 million) found ‘no benefit’; the paper (J Cardiothorac Vasc Anesth 2015; 2,063,337 patients) found higher operative mortality with the catheter (4.6% vs 3.1%, adjusted OR 1.34). Not wrong, but understated; explanation gives the figures."
FLAGS['SWAN-03'] = "Not an error: the card gives no evidence for cardiogenic shock; the Cardiogenic Shock Working Group registry (Garan, JACC HF 2020, 1,414 patients) linked no PAC assessment with higher in-hospital mortality than complete profiling (adjusted OR 1.57), observational only; the randomised Pulmonary Artery Catheter in Cardiogenic Shock Trial (PACCS, NCT05485376, Tufts; target 400, adaptive up to 800; primary outcome in-hospital mortality) was listed as recruiting at its last registry update. Explanation gives it."
FLAGS['SWAN-12'] = "Minor: card gives rupture mortality 41–70%; sources found range wider, from 30% (Deranged Physiology, with 0.2% incidence) to 70% (Kearney and Shabot, 0.031%), and a lower bound of 41% was not found. Incidence 0.03–0.2% is supported. Explanation gives the sources’ range."
