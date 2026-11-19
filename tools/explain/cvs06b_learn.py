# CVS06B — Explain v3 ("Learn" depth): right ventricular failure II — clinical signs, biomarkers, CXR and BNP, ECG, CVP waveform, PAC criteria, echo signs of RV overload,
# McConnell’s sign, RV dimensions and function cut-offs (and their conflicts), chronic RV failure, the five pillars of acute management, the six-step comprehensive care pathway,
# preload and volume loading, diuretics, vasoactive drugs, inhaled vasodilators, mechanical circulatory support (ECMO, micro-axial pumps, RVADs, Impella RP, VA ECMO, indications).
# No mnemonics or hooks. Driven by qpack/CVS06B.md (24 question links; RVF-30 McConnell asked 4 times, RVF-42 inhaled vasodilators 4, RVF-36 acute pillars 3; RVF-28, RVF-29, RVF-39 twice).
# RVF-24, 27, 31, 32, 33, 34, 37, 38, 40, 41, 43, 44 and 45 have no linked question and get short explanations with [pattern] decode items.
# No Top-up cards for CVS06B in cvs_topups.json. No `fix` entries for CVS06B in trace/test/data/qbank.json (checked 19 Nov 2026). cvs_cardlayer.json `lines` and `cross` read and used
# (RVF-25, 26, 28, 29, 36, 42, 46).
# Checked online on 19 Nov 2026:
#  - ESC/ERS 2022 PH guideline (Humbert et al., Eur Heart J 2022), via the ACC “ten points” summary, Rev Esp Cardiol comments and CCJM 2025 review: PH = mPAP >20 mmHg at rest; pre-capillary
#    adds PAWP ≤15 mmHg and PVR >2 WU; RHC confirms; echo probability rests on peak TRV >2.8 m/s plus other signs (I C); anticoagulation in PAH individualised (no general recommendation; may be harmful in SSc-PAH);
#    lifelong anticoagulation recommended in CTEPH.
#  - ESC 2019 acute PE (Konstantinides et al.), via Rev Esp Cardiol comments: echo RV dysfunction TAPSE <16 mm; CT RV/LV ratio ≥1.0. No newer ESC PE guideline found (search 19 Nov 2026).
#  - ASE/EACVI 2015 chamber quantification (Lang et al.), via a Wien Klin Wochenschr 2018 review quoting it: RV basal diameter >41 mm, mid >35 mm, proximal RVOT (PLAX) >30 mm, distal RVOT >27 mm,
#    free wall >5 mm; TAPSE <17 mm; S′ <9.5 cm/s; FAC <35%; free-wall longitudinal strain less negative than −20%.
#  - ASE 2025 right heart guideline (Mukherjee et al., JASE 2025), via cardioserv.net summaries: replaces single cut-offs with normal/mild/moderate/severe grading for TAPSE, S′, FAC, strain;
#    exact bands not readable (image).
#  - Mechanical support review (Frontiers Cardiovasc Med 2022;9:856870): Impella RP inflow in the IVC, outflow in the PA, femoral vein, up to 4.6 L/min, raises LV preload; haemolysis 5–10% in
#    the first 24 h on Impella; RV failure defined post-LVAD with CVP/PCWP >0.63.
# Could not open: the full texts of ESC/ERS 2022, ESC 2019 PE, ASE 2015 and 2025 (PMC and journal sites blocked) or the HFA/ESC 2016 acute RV failure statement (Harjola et al., Eur J Heart Fail
# 2016;18:226), which is the source of RVF-23, 36–41 and 43–46. From standard references without a fresh check (confident unless said): ASE 2015 RIMP >0.43 (pulsed) and >0.54 (tissue), 3D RVEF
# <45%, RV length >83 mm; ASE 2010 (Rudski) TAPSE <16 mm, S′ <10 cm/s, RIMP >0.40 / >0.55, 3D RVEF <44%; ASE 2005 (Lang) RV ranges, which match RVF-31; 60/60 sign (PA acceleration time <60 ms
# with TR gradient <60 mmHg); McConnell’s sign also in RV infarction (Casazza 2005); PAPi <0.9 in inferior MI (Korabathina 2012) and <1.85 after LVAD (Kang 2016); ESC 2021 HF diuretic dosing
# (furosemide 20–40 mg IV if naive, 1–2 × the oral dose if on diuretics); CT main PA ≥29–30 mm.
# Review 19 Nov 2026 (second check): ESC/ERS 2022 full text (genesis-foundation.net PDF) read for Table 10 (echo PA >25 mm), §5.1.7 CT (PA ≥30 mm in a three-sign combination; PA:aorta >0.9),
#  anticoagulation in PAH (no general recommendation; individualise; may be harmful in SSc-PAH). ESC/ERS 2022 BNP/NT-proBNP strata via SEC risk document: three-strata BNP <50 / 50–800 / >800 ng/L,
#  NT-proBNP <300 / 300–1100 / >1100 ng/L; four-strata BNP <50 / 50–199 / 200–800 / >800, NT-proBNP <300 / 300–649 / 650–1100 / >1100 (the 300 and 1400 figures were 2015). ASE 2015 RV
#  function thresholds confirmed via a teaching summary of Table 10 (TAPSE <17 mm, S′ <9.5 cm/s, FAC <35%, RIMP >0.43 pulsed / >0.54 tissue, 3D RVEF <45%). Impella RP (Abiomed/J&J product page):
#  inlet IVC, outlet PA, percutaneous venous access, flow >4.0 L/min, up to 14 days.

SPINE = [
  ("Why the right ventricle fails", "The thin-walled RV tolerates volume but not a sudden rise in pressure; acutely it dilates, chronically it hypertrophies and then decompensates, and in both it starves the LV by pushing the septum across."),
  ("Bedside signs and blood markers", "RV failure shows as systemic congestion with clear lungs, a low-output state and hypoxaemia, and the blood shows it as raised lactate, natriuretic peptides, troponin and congested liver and kidneys."),
  ("ECG, venous waveform, catheter numbers", "The ECG separates RV infarction from RV strain, the CVP waveform tells TR from pulmonary hypertension, and the catheter shows CVP above PCWP with a low cardiac index."),
  ("Echo: size, function, PE pattern", "Echo measures a dilated, poorly contracting RV against fixed cut-offs (TAPSE <17 mm, FAC <35%, S′ <9.5 cm/s), dates the process by wall thickness, and points to PE by McConnell’s sign and the 60/60 sign."),
  ("Medical rescue of acute failure", "Treat the trigger, keep rate and rhythm, fill only if under-filled and decongest if over-filled, restore arterial pressure with noradrenaline before adding an inotrope, and offload the RV with inhaled pulmonary vasodilators and gentle ventilation."),
  ("Mechanical support when drugs fail", "When drugs fail, VA ECMO bypasses the RV and lungs for days, the Impella RP pumps into the pulmonary artery without oxygenating, and surgical RVADs bridge weeks to months."),
]

PRIMER = "The right ventricle is a thin-walled, crescent-shaped chamber built to push a large volume into a low-resistance, highly compliant pulmonary circuit; it copes with extra volume but fails quickly when afterload rises suddenly. Its coronary flow runs in systole and diastole and depends on the gap between aortic pressure and RV pressure, so systemic hypotension and RV distension together make it ischaemic. The two ventricles share the septum and the pericardium (ventricular interdependence): a distended RV pushes the septum left and lowers LV filling, which is how RV failure becomes a low-output state. CVS06A (RVF-01 to RVF-22) covered causes and the pathophysiology spiral; this deck is recognition, measurement and treatment."

L = {}

L['RVF-23'] = dict(
  sub="Cardiology → RV failure → Clinical signs",
  step=2,
  intro="Step 2 begins at the bedside: RV failure shows itself first in the systemic veins, not in the lungs. The one real question puts a dilated RV with a distended abdomen in front of you and asks you to decide between chronic RV failure and massive PE.",
  parts=[
    ('a', "**Hypoxaemia.** It comes from ventilation–perfusion mismatch (PE, lung disease), low mixed venous saturation from a low output, and right-to-left shunting through a patent foramen ovale when RA pressure exceeds LA pressure. There is no pulmonary oedema unless the left heart is also failing."),
    ('b', "**Jugular venous distension, hepatojugular reflux, peripheral oedema, pericardial effusion, congestive hepato/splenomegaly, ascites, anasarca (particularly in acute decompensation of chronic RV failure).** A high RA pressure is transmitted back into every systemic vein: neck, liver, gut, legs and pericardium. Oedema, ascites and anasarca need days to weeks of salt and water retention to build up, so their presence tells you the process is chronic or acute-on-chronic, not a fresh PE."),
    ('c', "**Third heart sound, systolic murmur of tricuspid regurgitation, hepatic pulse, signs of concomitant LV dysfunction, paradoxical pulse.** The right-sided S3 (louder on inspiration) is rapid filling of a stiff, dilated RV. A dilated annulus causes functional TR; the regurgitant systolic wave reaches the liver as a pulsatile liver (hepatic pulse). Pulsus paradoxus appears because a distended RV in a closed pericardium steals space from the LV on inspiration (interdependence)."),
    ('d', "**Hypotension, tachycardia, cool extremities, CNS abnormalities, oliguria.** A failing RV delivers less blood to the LV, and the shifted septum lowers LV filling further, so the picture is that of cardiogenic shock with a high CVP and clear lungs."),
  ],
  mimic=[
    ("Chronic RV failure from PH vs massive PE", "Both: dilated RV, high CVP, hypotension. Ascites, anasarca, hepatomegaly and RV wall >5 mm mean months of disease (PH); a sudden onset with McConnell’s or the 60/60 sign and a thin-walled RV means PE (RVF-29, RVF-30)."),
    ("RV failure vs tamponade", "Both: raised JVP, hypotension, pulsus paradoxus. In RV failure the right chambers are large; in tamponade they are small and collapse in diastole."),
  ],
  traps=[
    ("“Acute dyspnoea + hypotension + dilated RV = massive PE” (one in three chose it; 67% right)", "The distended abdomen (ascites) and CVP 20 point to a chronically congested patient, so the key is RV failure from pulmonary hypertension. The key is defensible but the stem is ambiguous; the abdominal sign is what decides it."),
    ("“A hepatic pulse is a congestion sign”", "On this card it sits under RV dysfunction: it is the TR wave transmitted to the liver."),
  ],
  decode=[
    ("Dilated RV, CVP 20, hypotension, swollen abdomen — diagnosis? [DocT QBank]", "RV failure due to pulmonary hypertension (chronic congestion), not massive PE or tamponade."),
    ("[pattern] Which sign of RV failure suggests acute-on-chronic rather than acute disease?", "Anasarca (and ascites)."),
  ],
  punch="RV failure congests the systemic veins and leaves the lungs clear; ascites and anasarca take time to form, so they mark chronic or acute-on-chronic disease, not a fresh PE.",
)

L['RVF-24'] = dict(
  sub="Cardiology → RV failure → Biochemical markers",
  step=2,
  intro="Still in step 2: the blood tests show the same three problems as the bedside signs, namely low output, a stretched and ischaemic RV, and congested organs.",
  parts=[
    ('a', "**Increased lactate.** It reflects tissue hypoperfusion from the low-output state."),
    ('b', "**Elevated natriuretic peptides (BNP or NT-proBNP).** They are released by stretched myocardium, here the dilated RV, and are used for prognosis (RVF-25)."),
    ('c', "**Elevated cardiac troponin I or T.** They mark RV ischaemia: high wall tension with a low coronary perfusion pressure. In PE, RV dysfunction plus a positive troponin defines intermediate-high risk (ESC 2019)."),
    ('d', "**Abnormal liver biochemistry: transaminases, bilirubin, prolonged prothrombin time.** Venous congestion raises bilirubin and cholestatic enzymes; low output causes ischaemic hepatitis with very high transaminases; poor synthesis prolongs the PT."),
    ('e', "**Abnormal renal function: urea, creatinine.** A high venous pressure lowers renal perfusion pressure (cardiorenal syndrome, RVF-35)."),
    ('f', "**D-dimer, used in the diagnostic work-up of suspected PE.** It rules PE out when negative at low or intermediate clinical probability; it does not measure RV failure."),
  ],
  mimic=[
    ("Congestive vs ischaemic liver injury", "Congestion: mostly bilirubin and cholestatic enzymes. Low-output ischaemic hepatitis: transaminases in the thousands."),
  ],
  traps=[
    ("“D-dimer measures RV strain”", "It is only a PE rule-out test; BNP and troponin are the RV markers."),
  ],
  decode=[
    ("[pattern] Which two blood markers, with echo, stratify a normotensive PE as intermediate-high risk?", "Troponin (with RV dysfunction on echo or CT); BNP/NT-proBNP supports it."),
  ],
  punch="Lactate shows low output, BNP and troponin show RV stretch and ischaemia, liver and kidney tests show congestion; D-dimer is only for ruling out PE.",
)

L['RVF-25'] = dict(
  sub="Cardiology → RV failure → CXR and prognosis",
  step=2,
  intro="Step 2 continues with the chest film and with BNP as a guide to how hard to treat. The one real question asks for the pulmonary artery diameter that suggests pulmonary hypertension, and only 55% got it.",
  parts=[
    ('a', "**CXR: enlarged main PA and regional oligaemia → pulmonary oedema; clear lung fields.** Raised pulmonary pressure enlarges the main and central pulmonary arteries, while pruned peripheral vessels or a regional oligaemia (Westermark sign in PE) show reduced flow beyond. Pulmonary oedema appears only when the left heart is the cause (group 2 PH); in isolated RV failure the lung fields are clear. On CT, a main PA diameter of about 29–30 mm or more (measured before the bifurcation), or a PA wider than the ascending aorta, suggests pulmonary hypertension; ESC/ERS 2022 quotes a PA:aorta ratio >0.9 and lists PA ≥30 mm (with RVOT wall ≥6 mm and septal deviation) as highly predictive, while a ratio >1 is the figure most often quoted. On echo the threshold is a PA diameter >25 mm."),
    ('b', "**Prognosis → tailoring of therapy → BNP → assess the appropriate grade of treatment.** BNP or NT-proBNP rises with RV stretch and falls when the RV is offloaded, so it carries prognosis and tells you whether treatment is enough. In PAH, ESC/ERS 2022 uses it in risk stratification: BNP <50 ng/L or NT-proBNP <300 ng/L is low risk, BNP >800 or NT-proBNP >1100 ng/L is high risk (the older 2015 cut-offs were 300 and 1400); therapy is escalated until the patient reaches low risk."),
  ],
  mimic=[
    ("Big PA with clear lungs vs big PA with oedema", "Clear lungs: pre-capillary PH or isolated RV failure. Oedema and upper-lobe diversion: left heart disease is driving the PH."),
  ],
  traps=[
    ("“A PA above 2 cm (or 4–5 cm) is abnormal” (45% chose a wrong figure)", "The CT threshold is about 3 cm (≥29 mm); 2 cm is normal and 4–5 cm is aneurysmal territory."),
  ],
  decode=[
    ("Central PA calibre proximal to the bifurcation above ___ cm suggests raised pulmonary pressure. [DocT GT]", "3 cm."),
    ("[pattern] What does BNP add in RV failure?", "Prognosis and a target for escalating therapy."),
  ],
  punch="RV failure on the film is a big pulmonary artery with clear lungs; a main PA of about 3 cm on CT, or bigger than the aorta, suggests pulmonary hypertension, and BNP tells you whether treatment is enough.",
)

L['RVF-26'] = dict(
  sub="Cardiology → RV failure → ECG",
  step=3,
  intro="Step 3 starts with the ECG, which must tell two different RV problems apart: infarction of the RV muscle and strain from a sudden pressure load. The one real question is an inferior STEMI with shock and clear lungs.",
  parts=[
    ('a', "**General: right axis deviation, RBBB, P pulmonale.** A larger RV shifts the mean QRS vector to the right; a stretched RV and its conduction tissue give a right bundle branch block; a dilated, high-pressure RA gives tall P waves (≥2.5 mm in II)."),
    ('b', "**RV MI: ST elevation in V3R, V4R; Q wave in V1–V3.** RV infarction comes from proximal RCA occlusion, so it rides on an inferior STEMI. ST elevation ≥1 mm in V4R is the key sign and is transient (it has gone within about 12 hours in roughly half of patients), so record right-sided leads early. ST elevation in III greater than in II, and ST elevation in V1, also point to RV involvement, because lead III and V1 face the right side. Q waves in V1–V3 are non-specific; they can also come from an anterior infarct."),
    ('c', "**RV strain: T inversion in V1–V4; S1Q3T3.** Acute pressure load (PE) causes subendocardial RV ischaemia seen in the right precordial leads (T inversion V1–V4 is the commonest abnormality apart from sinus tachycardia). S1Q3T3 is specific but insensitive and is not needed for the diagnosis."),
  ],
  mimic=[
    ("RV infarction vs RV strain", "Infarction: ST elevation in V4R with an inferior STEMI, III > II. Strain: T inversion V1–V4, S1Q3T3, sinus tachycardia, often new RBBB."),
  ],
  traps=[
    ("“ST elevation in II greater than III means RV involvement”", "It is the opposite: III > II points to the RCA and the RV; II > III points to the circumflex."),
    ("“S1Q3T3 is the RV infarct pattern”", "It is the strain (PE) pattern."),
  ],
  decode=[
    ("Inferior STEMI, hypotension, raised JVP, clear lungs — which ECG finding points to RV involvement? [Marrow]", "ST elevation in III > II (also ST elevation in V1 and ≥1 mm in V3R/V4R)."),
    ("[pattern] Which ECG pattern is RV strain in acute PE?", "T inversion V1–V4, S1Q3T3, RBBB, sinus tachycardia."),
  ],
  punch="Right-sided ST elevation (V4R, III > II, V1) on an inferior STEMI means RV infarction; anterior T inversion with S1Q3T3 means RV strain.",
)

L['RVF-27'] = dict(
  sub="Cardiology → RV failure → CVP and its waveform",
  step=3,
  intro="Still step 3: the CVP is the RV’s filling pressure, and its waveform shows what is loading the RA.",
  parts=[
    ('a', "**A raised JVP reflects raised atrial pressure.** With the tricuspid valve open in diastole, RA pressure equals RV end-diastolic pressure."),
    ('b', "**Kussmaul’s sign: an increase in JVP on inspiration; it can indicate the cause of RV failure.** Normally inspiration lowers intrathoracic pressure and draws blood into the right heart, so the JVP falls. When the RV cannot accept the extra return (constrictive pericarditis, restrictive cardiomyopathy, RV infarction, severe RV failure), the pressure rises instead."),
    ('c', "**A rising CVP in RV dysfunction is an ominous sign; the CVP trend in response to fluids and inotropes is what is informative.** A single value says little; a CVP that climbs after a fluid bolus says the RV is on the flat part of its curve and more fluid will only distend it (RVF-39)."),
    ('d', "**Severe TR: dominant V wave in ventricular systole from retrograde RA filling, then a sharp Y descent from the high RA volume.** The regurgitant jet fills the RA during systole, merging the c and v waves into a large cv wave; when the tricuspid valve opens the overfilled RA empties fast."),
    ('e', "**Pulmonary hypertension: dominant A wave, the RA contracting against increased resistance.** A stiff, hypertrophied RV resists the atrial kick, so the a wave grows (also in tricuspid stenosis). Cannon a waves are different: the RA contracting against a closed tricuspid valve in AV dissociation."),
  ],
  mimic=[
    ("Large v wave vs large a wave", "Large v (cv) wave: TR, systolic. Large a wave: PH or tricuspid stenosis, end-diastolic."),
  ],
  traps=[
    ("“A high CVP in RV failure means more fluid is needed”", "A rising CVP is ominous; it means the RV is overfilled."),
  ],
  decode=[
    ("[pattern] Giant v waves with a steep y descent on the CVP trace — lesion?", "Severe tricuspid regurgitation."),
  ],
  punch="A rising CVP in RV failure is a warning, not a fluid target; a giant v wave means TR and a giant a wave means a stiff, pressure-loaded RV.",
)

L['RVF-28'] = dict(
  sub="Cardiology → RV failure → Pulmonary artery catheter",
  step=3,
  intro="Step 3 ends with the catheter, which turns the bedside impression into numbers. Two real questions ask the index that predicts death in RV infarction and the test that confirms pulmonary hypertension.",
  parts=[
    ('a', "**Diagnosis of RV failure and guiding management.** Right heart catheterisation is the gold standard to confirm pulmonary hypertension: ESC/ERS 2022 defines PH as mPAP >20 mmHg, and pre-capillary PH adds PAWP ≤15 mmHg and PVR >2 WU. Echo only estimates the probability (RVF-29), so RHC comes before the aetiological work-up."),
    ('b', "**Accurate measurement of CO, which allows calculation of PVR as a surrogate marker for afterload.** PVR = (mPAP − PAWP) / CO, in Wood units. It tells you whether the RV faces a high afterload (PH, PE) or a normal one (RV infarction), which decides whether to give fluid or to offload."),
    ('c', "**Acute RV dysfunction: CVP > PCWP, low cardiac index, low stroke volume index, SvO₂ <55%.** Normally left filling pressure exceeds right; when CVP rises above PCWP the right side is failing first (before LVAD implantation, a CVP/PCWP ratio >0.63 predicts RV failure afterwards). The PA pulsatility index, PAPi = (PA systolic − PA diastolic) / RA pressure, combines how much pulse pressure the RV generates with how much it is congested: PAPi <0.9 in acute inferior MI predicts RV failure and in-hospital death; <1.85 predicts RV failure after LVAD implantation."),
  ],
  mimic=[
    ("Isolated RV failure vs biventricular failure", "Isolated: CVP > PCWP, clear lungs. Biventricular: both high, PCWP usually higher."),
  ],
  traps=[
    ("“The lowest cardiac index best predicts death in RV infarct shock”", "PAPi (here 0.4) is the index that predicts mortality; it captures RV pulse generation against congestion."),
    ("“Echo confirms PH”", "Echo gives a probability; RHC confirms (mPAP >20 mmHg)."),
  ],
  decode=[
    ("RV infarct, persistent shock, RHC — which value carries the greatest mortality? [Marrow]", "PAPi 0.4 (<0.9 is high risk)."),
    ("Young woman with PH features on echo and CXR — next step? [Marrow]", "Right heart catheterisation."),
  ],
  punch="The catheter confirms PH (mPAP >20, PAWP ≤15, PVR >2 WU) and shows RV failure as CVP above PCWP; a PAPi below 0.9 in RV infarction predicts death.",
)

L['RVF-29'] = dict(
  sub="Cardiology → RV failure → Echo signs of RV overload",
  step=4,
  intro="Step 4 brings in echo, which measures the RV against fixed cut-offs. Two real questions use these signs to tell chronic pulmonary hypertension from acute PE.",
  parts=[
    ('a', "**RV wall thickness increased: a chronic overload state.** Free wall >5 mm (subcostal view) means the RV has had weeks to months to hypertrophy; an acutely loaded RV dilates with a thin wall. This is the sign that dates the process."),
    ('b', "**Distended IVC with <50% collapse.** An IVC >21 mm that collapses less than 50% on sniff estimates RA pressure at about 15 mmHg."),
    ('c', "**TR V >2.8 m/s.** Peak TR velocity gives the RV–RA gradient (4V²); above 2.8 m/s (gradient about 31 mmHg) is the ESC/ERS 2022 threshold for echo probability of PH. A thin acute RV in PE often cannot generate a high velocity (60/60 sign, RVF-30)."),
    ('d', "**TAPSE <17 mm.** Longitudinal shortening is the main RV contraction (ASE 2015; ESC 2019 PE uses <16 mm prognostically)."),
    ('e', "**RV cavity size ≥ size of LV.** An RV/LV ratio ≥1 in the apical four-chamber view (or on CT) is dilatation; with septal flattening it gives a D-shaped LV in short axis."),
    ('f', "**FAC <35%.** Fractional area change = (end-diastolic − end-systolic area) / end-diastolic area, in the RV-focused view."),
    ('g', "**Longitudinal strain of RV free wall <20%.** That is, less negative than −20%; normal is about −29%."),
  ],
  mimic=[
    ("Chronic PH vs acute PE on echo", "PH: thick RV wall (>5 mm), high TR velocity, often pericardial effusion. PE: thin dilated RV, modest TR velocity, McConnell’s sign, 60/60 sign, sometimes thrombus in transit."),
  ],
  traps=[
    ("“Massive PE” for a dilated RV with CVP 20 and ascites (one in three chose it)", "Ascites and a thick RV need time; this is chronic RV failure from PH (cardlayer line)."),
  ],
  decode=[
    ("Dilated RV, CVP 20, distended abdomen — chronic PH or massive PE? [DocT QBank]", "Chronic RV failure from PH; a free wall >5 mm would confirm chronicity."),
    ("Echo finding in PE? [NEET 2024]", "RV dilatation; McConnell’s sign."),
  ],
  punch="Every sign on this list says the RV is overloaded, but only wall thickness says for how long: a thick wall means chronic PH, a thin dilated one means an acute load.",
)

L['RVF-30'] = dict(
  sub="Cardiology → RV failure → McConnell’s sign",
  step=4,
  intro="Still step 4: a regional pattern of RV wall motion that points to PE. It was asked four times, including NEET 2025, and the Grand Test twist is that it is not the most specific sign.",
  parts=[
    ('a', "**Seen in pulmonary embolism.** A sudden rise in PA pressure overstretches and makes ischaemic the free wall of a thin RV; the apex is tethered to a contracting LV and keeps moving."),
    ('b', "**Lateral wall hypokinesia + apex sparing.** The RV free wall from base to mid is hypokinetic while the apex contracts normally. Its original specificity for PE (about 94%) has not held up: the same pattern occurs in RV infarction, because the RV apex is partly supplied by the LAD and is tethered to the LV. The sign that best separates PE from RV infarction is the 60/60 sign: PA acceleration time <60 ms (a stiff, high-resistance pulmonary bed) with a TR gradient <60 mmHg (a thin RV that cannot generate high pressure). RV infarction has a normal PVR, so the acceleration time stays normal."),
  ],
  mimic=[
    ("McConnell’s sign vs Takotsubo", "McConnell: RV free wall hypokinetic, RV apex spared. Takotsubo: LV apex ballooned, base hyperkinetic, the reverse distribution in the other ventricle."),
    ("McConnell vs 60/60", "McConnell: regional wall motion, also in RV infarction. 60/60: Doppler signs of acute pressure load, more specific for PE."),
  ],
  traps=[
    ("“McConnell’s sign is the most specific sign of PE versus RV infarction”", "It also occurs in RV infarction; the 60/60 sign is more specific."),
    ("“A D-shaped LV or TAPSE <15 mm points to PE”", "Both mean RV pressure overload or dysfunction from any cause."),
    ("“Pericardial effusion with RV collapse suggests PE”", "That is tamponade; in PE the RA and RV are dilated."),
  ],
  decode=[
    ("Post-stenting patient, acute dyspnoea, RV hypokinesia with preserved apical contractility — diagnosis? [NEET 2025]", "Pulmonary embolism."),
    ("Dilated RV after a long flight — which finding is most specific for PE rather than RV infarction? [DocT GT]", "The 60/60 sign."),
    ("Which echo finding most suggests acute PE? [DocT GT; NEET 2024]", "RA/RV dilatation (McConnell’s sign as the classic named sign)."),
  ],
  punch="McConnell’s sign is a hypokinetic RV free wall with a moving apex and points to PE, but RV infarction can copy it; the 60/60 sign is the more specific test.",
)

L['RVF-31'] = dict(
  sub="Cardiology → RV failure → Normal RV dimensions",
  step=4,
  intro="Step 4 needs reference sizes before you can call an RV dilated. The card’s ranges are the 2005 ASE values; the current ones are larger because they are measured in the RV-focused view.",
  parts=[
    ('a', "**RV length, base-to-apex: 7.1–7.9 cm.** ASE 2015 gives a normal longitudinal dimension up to 8.3 cm."),
    ('b', "**Basal RV: 2.0–2.8 cm.** ASE 2015: normal 2.5–4.1 cm, dilated above 4.1 cm, in the RV-focused apical four-chamber view."),
    ('c', "**Mid RV: 2.7–3.3 cm.** ASE 2015: normal 1.9–3.5 cm, dilated above 3.5 cm."),
    ('d', "**RV outflow tract: 2.5–2.9 cm.** ASE 2015: RVOT up to 3.0 cm in parasternal long axis, proximal RVOT (short axis) up to 3.5 cm, distal RVOT (just below the pulmonary valve) up to 2.7 cm."),
    ('e', "**Pulmonary artery: 1.5–2.1 cm.** On echo, a PA diameter >2.5 cm is one of the ‘other signs’ of PH (RVF-25)."),
  ],
  mimic=[
    ("Basal vs mid RV diameter (ASE 2015)", "Basal is the widest (upper limit 4.1 cm); mid is narrower (3.5 cm)."),
  ],
  traps=[
    ("“Mid RV is wider than basal RV” (card watch line)", "True only of the 2005 ranges; in the current RV-focused view the basal diameter is the largest."),
  ],
  decode=[
    ("[pattern] Basal RV diameter above what value means dilatation?", "4.1 cm (ASE 2015)."),
  ],
  punch="Quote 2015 values when asked: basal RV >4.1 cm and mid RV >3.5 cm are dilated; the card’s smaller ranges are the 2005 ones.",
)

L['RVF-32'] = dict(
  sub="Cardiology → RV failure → Measures of RV function",
  step=4,
  intro="Step 4 continues with the numbers that call RV systolic function abnormal. The card mixes 2010 and 2015 thresholds; the current answer is the ASE 2015 set.",
  parts=[
    ('a', "**RVEF on 2D: <44%.** 2D volumes depend on geometric assumptions that a crescent-shaped RV does not obey, so ASE does not recommend 2D RVEF (RVF-33)."),
    ('b', "**FAC: <35%.** The same in every edition."),
    ('c', "**TAPSE: <1.7 cm.** ASE 2015 (it was <1.6 cm in 2010). ASE 2025 keeps TAPSE but grades severity as mild, moderate or severe."),
    ('d', "**RIMP: pulsed >0.44; tissue >0.55.** RIMP (Tei index) = (isovolumic contraction + relaxation time) / ejection time. ASE 2015 gives >0.43 by pulsed Doppler and >0.54 by tissue Doppler (2010: >0.40 and >0.55)."),
    ('e', "**IVA: not defined.** Isovolumic acceleration is load-dependent and varies with age and heart rate, so no screening cut-off is used."),
    ('f', "**S′ (pulsed): <10 cm/s.** ASE 2015 gives <9.5 cm/s; <10 cm/s is the 2010 value."),
    ('g', "**RVEF on 3D: <44%.** ASE 2015 gives <45% (2010: <44%)."),
  ],
  table=dict(title="RV function: card vs ASE 2015", head=["Measure", "Card", "ASE 2015 (exam answer)"], rows=[["TAPSE", "<1.7 cm", "**<17 mm**"], ["FAC", "<35%", "**<35%**"], ["S′", "<10 cm/s", "**<9.5 cm/s**"], ["RIMP", ">0.44 / >0.55", "**>0.43 pulsed / >0.54 tissue**"], ["3D RVEF", "<44%", "**<45%**"], ["Free-wall strain", "—", "**less negative than −20%**"]]),
  mimic=[
    ("TAPSE <17 mm (ASE) vs <16 mm (ESC PE)", "Same idea; ASE uses 17 mm for dysfunction, ESC 2019 uses 16 mm for prognosis in PE."),
  ],
  traps=[
    ("“S′ <10 cm/s and RIMP >0.40 are current”", "They are 2010 values; ASE 2015 is S′ <9.5 cm/s, RIMP >0.43 / >0.54."),
  ],
  decode=[
    ("[pattern] Which RV measure has the same abnormal cut-off in every guideline?", "FAC <35%."),
  ],
  punch="Use ASE 2015: TAPSE <17 mm, FAC <35%, S′ <9.5 cm/s, RIMP >0.43 or >0.54, 3D RVEF <45%, free-wall strain less negative than −20%.",
)

L['RVF-33'] = dict(
  sub="Cardiology → RV failure → Limitations of RV measures",
  step=4,
  intro="Still step 4: each number has a weakness that matters in ICU patients, who are often ventilated, in AF and with a high RA pressure.",
  parts=[
    ('a', "**RVEF on 2D: unreliable.** The RV is a crescent wrapped around the LV; 2D formulae built for an ellipsoid misjudge its volume."),
    ('b', "**FAC: endocardial border needs accurate tracing.** RV trabeculation and a poor window make the border hard to trace, and FAC ignores the outflow tract."),
    ('c', "**TAPSE: load and angle dependent.** It is one M-mode line at one point of the annulus; it falls with low preload, is overestimated when the whole heart swings (large effusion), and falls after cardiac surgery without true loss of RV function."),
    ('d', "**RIMP: not reliable in raised RA pressure or irregular rhythm such as AF.** A high RA pressure shortens isovolumic relaxation and falsely lowers (normalises) the index; AF changes cycle length from beat to beat."),
    ('e', "**IVA: load and angle dependent; varies with age and heart rate.** So no single cut-off works."),
    ('f', "**S′: angle dependent; assumes all segments have similar function; limited data in the elderly.** It is measured at the basal free wall only, so regional disease (McConnell) is missed or overstated."),
    ('g', "**RVEF on 3D: not readily available.** It needs a 3D probe, offline software and a good window."),
  ],
  mimic=[
    ("Angle-dependent vs angle-independent measures", "Angle-dependent: TAPSE, S′, IVA (and Doppler RIMP). Less angle-dependent: FAC, speckle-tracking strain, 3D RVEF."),
  ],
  traps=[
    ("“A normal RIMP rules out RV dysfunction in a patient with CVP 20”", "A high RA pressure pseudo-normalises RIMP."),
  ],
  decode=[
    ("[pattern] Which RV index is unreliable in AF and high RA pressure?", "RIMP (Tei index)."),
  ],
  punch="TAPSE and S′ are quick but angle- and load-dependent, RIMP fails in AF and high RA pressure, and FAC, strain and 3D RVEF depend on image quality.",
)

L['RVF-34'] = dict(
  sub="Cardiology → RV failure → Conflicting cut-offs",
  step=4,
  intro="Step 4 ends with the source’s own contradictions. They are not random: one set is ASE 2015 and the other is ASE 2010.",
  parts=[
    ('a', "**TAPSE: <17 mm (overload list) vs <1.6 cm (function table); they reconcile loosely.** They do not quite: 17 mm is ASE 2015 and 16 mm is ASE 2010 (and ESC 2019 PE). RVF-32 prints <1.7 cm for the same function table."),
    ('b', "**S′: <9.5 cm/s (echo figure) vs <10 cm/s (function table).** 9.5 cm/s is ASE 2015; 10 cm/s is ASE 2010."),
    ('c', "**RIMP: >0.54 (echo figure) vs >0.44 pulsed and >0.55 tissue (function table).** 0.54 is the ASE 2015 tissue Doppler value (pulsed >0.43); 0.55 is the 2010 tissue value."),
    ('d', "**3D RVEF: <45% (echo figure) vs <44% (function table).** 45% is ASE 2015; 44% is ASE 2010."),
    ('e', "**FAC <35% is the figure all three agree on (strain <20% where given).** FAC has not changed between editions."),
  ],
  mimic=[
    ("Echo figure (p.321) vs function table (p.322)", "The figure carries ASE 2015 values; the table carries ASE 2010 values."),
  ],
  traps=[
    ("“Quote the function table (p.322) as the formal source” (card watch line)", "The function table is the older (2010) set; the exam answer is ASE 2015: TAPSE <17 mm, S′ <9.5 cm/s, RIMP >0.43/0.54, 3D RVEF <45%."),
  ],
  decode=[
    ("[pattern] Which S′ value defines RV systolic dysfunction?", "<9.5 cm/s (ASE 2015)."),
  ],
  punch="The conflicts are two guideline editions side by side; answer with ASE 2015 (TAPSE <17 mm, S′ <9.5 cm/s, RIMP >0.43/0.54, 3D RVEF <45%), and FAC <35% is safe either way.",
)

L['RVF-35'] = dict(
  sub="Cardiology → RV failure → Chronic RV failure",
  step=1,
  intro="Step 1 of the story: how the RV fails slowly, and why that failure starves the LV. The one real question rests on telling this chronic picture from an acute PE.",
  parts=[
    ('a', "**A gradual increase in RV afterload from pulmonary hypertension, most often from left heart failure.** Group 2 PH (left heart disease) is the commonest cause of PH; the raised LA pressure is transmitted back through the lungs to the RV."),
    ('b', "**Chronic volume overload from right-sided lesions such as TR.** Here the RV dilates to accommodate volume rather than pressure."),
    ('c', "**Initially compensatory myocyte hypertrophy and fibrosis, as in LV failure.** By Laplace, a thicker wall lowers wall stress for the same pressure, so a chronically loaded RV can generate systemic-level pressure, which is why chronic PH gives high TR velocities and a thick free wall (RVF-29)."),
    ('d', "**If the load persists: decompensation with myocyte loss and replacement fibrosis.** Hypertrophy outgrows its capillary supply, the RV becomes ischaemic, dilates and uncouples from the pulmonary circulation."),
    ('e', "**Reduced left heart filling is due more to RV dilation and ventricular interdependence than to reduced RV forward output → peripheral oedema and abdominal congestion → cardiorenal and cardiohepatic syndromes.** In a closed pericardium a big RV pushes the septum left (D-shaped LV), so the LV underfills even if RV output is maintained. The high venous pressure, not low output alone, damages kidney and liver."),
  ],
  mimic=[
    ("Chronic vs acute RV failure", "Chronic: hypertrophy, high pressures, ascites, anasarca. Acute: thin dilated RV, low generated pressure, no time for ascites."),
  ],
  traps=[
    ("“Massive PE” for the dilated RV with a distended abdomen (one in three)", "Abdominal congestion means chronic RV failure from PH."),
  ],
  decode=[
    ("Dilated RV, CVP 20, hypotension, distended abdomen in a man with CAD — diagnosis? [DocT QBank]", "RV failure due to pulmonary hypertension (from left heart disease)."),
  ],
  punch="Chronic RV failure is usually PH from left heart disease; the RV first thickens, then dilates, and the dilated RV starves the LV through the septum while venous congestion injures kidney and liver.",
)

L['RVF-36'] = dict(
  sub="Cardiology → RV failure → Five pillars of acute management",
  step=5,
  intro="Step 5 turns to treatment. Three Grand Test questions test it: a patient with IPAH on epoprostenol, and a patient with acute RV failure after mitral surgery.",
  parts=[
    ('a', "**Maintain rate and rhythm: a higher heart rate; aim for sinus rhythm; cardioversion if new onset or unstable; amiodarone ± DCCV.** A dilated RV cannot raise its stroke volume, so output depends on rate; loss of the atrial kick in AF or block drops filling of a stiff RV sharply. Bradycardia and AF are both poorly tolerated."),
    ('b', "**Optimise preload: under-filled, small boluses (50–100 mL) with close attention to CVP; over-filled, loop diuretics, CVVH if needed.** Most RV failure from raised afterload is over-filled; extra volume only dilates the RV and shifts the septum. In IPAH, decongest steadily, not by rapid aggressive diuresis that drops preload too far."),
    ('c', "**Improve contractility and perfusion: inodilators (dobutamine, milrinone); vasopressors (noradrenaline, vasopressin).** Restore arterial pressure first so the RV coronary perfusion gradient returns (RVF-38). Vasopressin raises SVR with little effect on PVR."),
    ('d', "**Reduce afterload: prevent hypoxia, hypercapnia, acidosis; reduce PEEP and airway pressures; avoid atelectasis; inhaled and IV pulmonary vasodilators.** Hypoxia, hypercapnia and acidosis all constrict pulmonary arterioles; high PEEP and plateau pressure compress alveolar vessels; atelectasis triggers hypoxic vasoconstriction. In a patient on IV epoprostenol, never interrupt the infusion: its half-life is minutes and stopping it causes a rebound PH crisis."),
    ('e', "**Mechanical support: IABP, ECMO, VAD.** For refractory cases (RVF-43 to RVF-46)."),
  ],
  mimic=[
    ("Acute RV failure after mitral surgery vs LV failure", "RV: dilated, hypokinetic RV, high CVP, preserved LV, hypoxia. LV: high PCWP, pulmonary oedema."),
  ],
  traps=[
    ("“Aggressive fluids for hypotension with a dilated RV and high CVP”", "The RV is already over-filled; fluid worsens interdependence. Start iNO (67–71% right)."),
    ("“Increase PEEP to improve oxygenation”", "Higher PEEP raises PVR and RV afterload."),
    ("“High-dose furosemide” as first step for hypotension", "It drops preload in a shocked patient; treat the afterload first."),
    ("“Lifelong anticoagulation” as the right add-on in IPAH on epoprostenol (key; 64% right)", "The key rests on older practice. ESC/ERS 2022 individualises anticoagulation in PAH (e.g. catheter-related thrombosis risk on IV epoprostenol). It is the least-wrong option here because digoxin is not routine, rapid diuresis harms and a CCB trial is only for stable outpatients; if ‘continue epoprostenol’ appears, choose that."),
  ],
  decode=[
    ("IPAH on IV epoprostenol admitted with RV failure — most appropriate additional therapy? [DocT GT]", "Keyed lifelong anticoagulation; disputed under ESC/ERS 2022."),
    ("Hypotension and hypoxia 3 h after mitral repair; dilated hypokinetic RV, preserved LV, high CVP — next step? [DocT GT, twice]", "Start inhaled nitric oxide."),
  ],
  punch="Keep the rate up and the rhythm sinus, fill only an under-filled RV and in small steps, raise arterial pressure first, and lower afterload with oxygen, CO₂ control, low PEEP and inhaled vasodilators.",
)

L['RVF-37'] = dict(
  sub="Cardiology → RV failure → Comprehensive care steps 1–3",
  step=5,
  intro="Still step 5: the HFA/ESC 2016 statement orders treatment of acute RV failure as six steps; the first three are assess, find the trigger, and set the volume.",
  parts=[
    ('a', "**Step 1, assess severity: clinical (arterial pressure, mental status, diuresis), biochemical (lactate, liver, renal, BNP, troponin), imaging (echo, CT), invasive (CVC or PAC).** These are the markers of RVF-23, RVF-24 and RVF-28 used to grade how sick the patient is."),
    ('b', "**Step 2, identify and treat triggers: sepsis, arrhythmias, drug withdrawal; PCI for RV infarction, reperfusion for high-risk PE.** Drug withdrawal includes stopping PAH therapy such as epoprostenol. A cause-specific fix (reopening the RCA, lysing the clot) unloads the RV faster than any drug."),
    ('c', "**Step 3, optimise fluid status: IV diuretics if overloaded, RRT if diuretics fail, cautious filling if CVP is low; avoid overfilling.** Volume is set before drugs because a wrongly filled RV will not respond to them."),
  ],
  mimic=[
    ("Trigger treatment in RV infarction vs PE", "RV infarction: PCI of the RCA. High-risk PE: systemic thrombolysis (or surgical or catheter therapy)."),
  ],
  traps=[
    ("“Start inotropes before addressing volume”", "Fluid status (step 3) comes before pressure and inotropy (steps 4–5)."),
  ],
  decode=[
    ("[pattern] Acute RV failure from an inferior STEMI — which cause-specific treatment comes first?", "Primary PCI of the culprit RCA."),
  ],
  punch="Assess severity, treat the trigger (PCI for RV infarction, reperfusion for high-risk PE), then set the volume, decongesting the over-filled RV and filling only a truly empty one.",
)

L['RVF-38'] = dict(
  sub="Cardiology → RV failure → Comprehensive care steps 4–6",
  step=5,
  intro="Step 5 continues: once volume is set, pressure comes before inotropy, and further afterload reduction comes last.",
  parts=[
    ('a', "**Step 4, maintain arterial pressure: norepinephrine.** RV coronary perfusion depends on aortic pressure minus RV pressure; hypotension makes a distended RV ischaemic, which lowers output and pressure further. Noradrenaline breaks this spiral and also helps the septum by supporting LV pressure."),
    ('b', "**Step 5, inotropes that reduce filling pressures: levosimendan, dobutamine, PDE III inhibitors.** All three also dilate vessels, which is why pressure must be secured first (RVF-41)."),
    ('c', "**Step 6, further afterload reduction: inhaled NO, inhaled prostacyclins.** Inhaled agents reach only ventilated lung, so they lower PVR without dropping systemic pressure (RVF-42)."),
    ('d', "**Alongside: haemodynamic monitoring and support in ICU or intermediate care, and early consideration of transfer to an ECMO/MCS-capable centre.** Transfer is planned before the patient is too unstable to move."),
  ],
  mimic=[
    ("Pressure first vs inotrope first", "In RV failure noradrenaline comes before inotropy, because an inodilator alone can drop coronary perfusion pressure further."),
  ],
  traps=[
    ("“Give dobutamine alone for a hypotensive RV failure”", "It can worsen hypotension; noradrenaline first."),
  ],
  decode=[
    ("[pattern] Hypotensive acute RV failure after fluid optimisation — first vasoactive drug?", "Noradrenaline."),
  ],
  punch="Restore arterial pressure with noradrenaline, then add an inodilator, then inhaled pulmonary vasodilators, and plan transfer for ECMO before it is too late.",
)

L['RVF-39'] = dict(
  sub="Cardiology → RV failure → Preload and volume loading",
  step=5,
  intro="Step 5 again: the fluid question, which turns on whether the RV afterload is normal. Two Marrow questions test the case where fluid is right: RV infarction.",
  parts=[
    ('a', "**Maintain adequate RV preload, carefully titrated fluid boluses (in RV MI with normal afterload), avoid overdistension.** An infarcted RV facing a normal PVR behaves as a passive conduit: forward flow depends on RA pressure, so a fluid bolus raises output."),
    ('b', "**Carefully titrated boluses in RV MI when afterload is normal.** With raised afterload (PH, PE, ARDS) the RV is already distended and fluid worsens it."),
    ('c', "**Saline or Ringer’s lactate, >200 mL over 15–30 min.** This is a single, measured challenge with reassessment; RVF-36’s 50–100 mL boluses are the cautious steps for the RV with raised afterload."),
    ('d', "**Decompensated RV failure with normal CVP and low arterial pressure.** A normal CVP in a hypotensive patient is the sign there is room to fill."),
    ('e', "**It can overdistend the ventricles, worsen interdependence and reduce cardiac output.** Once CVP rises without a rise in output, stop: the RV is on the flat part of its curve. Nitrates and diuretics are avoided in RV infarction because they drop preload."),
  ],
  mimic=[
    ("RV infarction vs pulmonary hypertension", "RV infarction: normal PVR, fluid helps (with PCI). PH or PE: high PVR, fluid usually harms; offload instead."),
  ],
  traps=[
    ("“Nitrates or diuretics for inferior STEMI with hypotension and clear lungs”", "These drop preload; give a fluid bolus."),
  ],
  decode=[
    ("Inferior STEMI, hypotension, clear lungs, normal LV — next step? [Marrow]", "Normal saline bolus."),
    ("Inferior MI, proximal RCA thrombus — first treatment of hypotension? [Marrow]", "IV fluids."),
  ],
  punch="Fluid helps the RV only when afterload and CVP are normal, as in RV infarction; give a measured bolus and stop when CVP rises without a rise in output.",
)

L['RVF-40'] = dict(
  sub="Cardiology → RV failure → Diuretics",
  step=5,
  intro="Step 5 continues with the commoner situation, the over-filled RV, where removing volume lets the septum move back.",
  parts=[
    ('a', "**Not on oral diuretics: 20–40 mg IV.** The furosemide starting dose of ESC heart failure guidelines."),
    ('b', "**On chronic diuretics: initial furosemide dose at least equivalent to the oral dose.** ESC 2021 HF specifies 1–2 times the daily oral dose, because oral absorption of furosemide is about half and chronic users are diuretic-resistant."),
    ('c', "**IV loop diuretics for all patients admitted with signs or symptoms of fluid overload.** Gut oedema slows oral absorption, so the IV route is used."),
    ('d', "**Intermittent boluses or continuous infusion.** DOSE showed no clear difference between them."),
    ('e', "**For resistant oedema: add a thiazide-type diuretic or spironolactone.** Sequential nephron blockade; distal tubules hypertrophy under chronic loop diuretics."),
    ('f', "**Caveats: worsening renal function and hypokalaemia.** Hypokalaemia raises arrhythmia risk, which the RV tolerates poorly."),
  ],
  mimic=[
    ("Over-filled vs under-filled RV", "Over-filled (high CVP, distended RV, septal shift): diuretics or CVVH. Under-filled (low CVP, RV infarction): fluid."),
  ],
  traps=[
    ("“The IV dose should be lower than the home oral dose”", "It should be at least equal to it (ESC 2021: 1–2 times)."),
  ],
  decode=[
    ("[pattern] Patient on furosemide 80 mg orally, admitted with congestion — initial IV dose?", "At least 80 mg IV (up to 160 mg)."),
  ],
  punch="Give IV furosemide 20–40 mg if naive or at least the home oral dose if not, by bolus or infusion, add a thiazide or spironolactone for resistance, and watch creatinine and potassium.",
)

L['RVF-41'] = dict(
  sub="Cardiology → RV failure → Vasoactive drugs",
  step=5,
  intro="Step 5 needs the three drugs used to support pressure and contractility, each with its own downside.",
  parts=[
    ('a', "**Noradrenaline 0.2–1.0 µg/kg/min: raises RV inotropy and systemic BP, promotes positive ventricular interaction, restores the coronary perfusion gradient; excess vasoconstriction may worsen tissue perfusion.** α₁ effects raise aortic pressure more than PVR at usual doses and β₁ effects help contractility. A higher LV pressure pushes the septum back towards the RV."),
    ('b', "**Dobutamine 2–20 µg/kg/min: raises RV inotropy and lowers filling pressures, especially with left heart failure; can worsen hypotension if used alone; can trigger arrhythmias.** β₂ vasodilation lowers SVR, so pair it with a vasopressor."),
    ('c', "**Levosimendan 0.1–0.2 µg/kg/min: RV inotropy plus pulmonary vasodilation, improving RV–arterial coupling; may worsen hypotension and trigger arrhythmias. Bolus 6–12 µg/kg over 10 min is optional and not recommended if SBP <90 mmHg; infusion can go down to 0.05 or up to 0.2 µg/kg/min.** It sensitises troponin C to calcium and opens K-ATP channels in vascular muscle, which is why it lowers PVR and also SVR. No guideline names it the drug of choice; it is one option at step 5 after pressure is secured."),
  ],
  mimic=[
    ("Dobutamine vs levosimendan", "Dobutamine: β-agonist, short half-life, tachycardia. Levosimendan: calcium sensitiser with an active metabolite lasting days, more pulmonary vasodilation, more hypotension."),
  ],
  traps=[
    ("“Levosimendan bolus in a patient with SBP 85”", "Not recommended below SBP 90 mmHg."),
  ],
  decode=[
    ("[pattern] Which drug combines RV inotropy with pulmonary vasodilation?", "Levosimendan."),
  ],
  punch="Noradrenaline restores the coronary perfusion gradient, dobutamine adds contractility but needs a vasopressor beside it, and levosimendan adds pulmonary vasodilation at the cost of hypotension.",
)

L['RVF-42'] = dict(
  sub="Cardiology → RV failure → Inhaled vasodilators",
  step=5,
  intro="Step 5 ends with offloading the RV through the airway. Four real questions test inhaled NO: when to start it, what it does, and what happens if it is stopped suddenly.",
  parts=[
    ('a', "**Inhaled prostaglandins reduce PVR, hypoxic pulmonary vasoconstriction and systemic vascular resistance; iNO reduces PVR only in well-ventilated lung zones.** NO diffuses into the vessel wall, raises cGMP and is inactivated by haemoglobin within seconds, so it never reaches the systemic circulation. Prostacyclin raises cAMP and has a longer half-life, so some spills over into the systemic circulation."),
    ('b', "**iNO acts only where ventilation reaches.** Blood is redirected to ventilated alveoli, so shunt falls and oxygenation improves."),
    ('c', "**iNO improves V/Q matching and RV ejection fraction.** Lower PVR is lower RV afterload, so the RV empties better, and the improved V/Q matching raises PaO₂."),
    ('d', "**Prostaglandins: hypotension and hypoxia.** These are mainly effects of IV prostacyclin, which dilates the whole pulmonary bed (including unventilated units, releasing hypoxic vasoconstriction) and the systemic bed. Inhaled prostacyclin is much more selective and usually improves oxygenation like iNO, with mild hypotension at most. iNO has its own harms: rebound PH and hypoxaemia if stopped suddenly (endogenous NO synthase is suppressed), methaemoglobinaemia, NO₂ formation, and pulmonary oedema if LV filling pressure is high."),
    ('e', "**iNO: start at 5 ppm, overall 20–40 ppm.** Benefit plateaus around 20 ppm. To stop, wean in steps down to about 1 ppm before switching off; if rebound occurs, restart and wean more slowly."),
  ],
  mimic=[
    ("Inhaled vs IV pulmonary vasodilators", "Inhaled: selective for ventilated lung, oxygenation improves, little hypotension. IV: dilate everything, so hypotension and worse V/Q."),
  ],
  traps=[
    ("“Increase IV fluids” or “increase PEEP” for RV failure after mitral repair (one in three chose wrong)", "The RV is dilated and the CVP high; start iNO to lower PVR."),
    ("“iNO raises systemic blood pressure” or “improves surfactant”", "Its goal is to reduce PVR (95% right); any rise in BP is indirect."),
    ("“Hypoxia after stopping iNO — give 100% oxygen and wait”", "Restart iNO and wean slowly."),
  ],
  decode=[
    ("Hypotension and hypoxia 3 h after mitral repair; dilated RV, preserved LV, high CVP — next step? [DocT GT, twice]", "Inhaled nitric oxide."),
    ("Severe RV failure after PE, iNO started — primary goal? [DocT GT]", "Reduce PVR."),
    ("Rebound hypoxia and PH after stopping iNO — management? [Marrow]", "Restart iNO and wean slowly."),
  ],
  punch="iNO lowers PVR only where the lung is ventilated, so it unloads the RV and improves oxygenation without hypotension; stop it slowly, because sudden withdrawal causes rebound PH and hypoxaemia.",
)

L['RVF-43'] = dict(
  sub="Cardiology → RV failure → Mechanical support options",
  step=6,
  intro="Step 6 is mechanical support when drugs have failed. The options differ in how long they can run and whether they oxygenate.",
  parts=[
    ('a', "**ECMO/ECLS: short-term, rapid; an oxygenator is part of it; complications rise beyond 5–10 days.** It can be placed at the bedside and supports both circulation and gas exchange; bleeding, thrombosis, limb ischaemia and infection accumulate with time."),
    ('b', "**Percutaneous micro-axial pumps: limited pump capacity; ECLS preferred in severe cardiogenic shock or when high flow is needed.** They give about 4 L/min and no gas exchange."),
    ('c', "**Paracorporeal RVADs: longer-term (weeks or months); can be combined with oxygenators.** Surgically placed, usually RA or RV to PA, for bridge to recovery or transplant."),
  ],
  mimic=[
    ("ECMO vs RVAD", "ECMO: fast, oxygenates, days. RVAD: surgical, weeks to months, needs an added oxygenator for gas exchange."),
  ],
  traps=[
    ("“A micro-axial pump also oxygenates”", "Only ECMO, or an RVAD with an oxygenator, supports gas exchange."),
  ],
  decode=[
    ("[pattern] Refractory RV failure with severe hypoxaemia — which support?", "VA ECMO (or an RVAD with an oxygenator)."),
  ],
  punch="ECMO is the fast, short-term option that also oxygenates, micro-axial pumps give limited flow without gas exchange, and surgical RVADs run for weeks to months.",
)

L['RVF-44'] = dict(
  sub="Cardiology → RV failure → Impella RP",
  step=6,
  intro="Step 6 continues with the percutaneous right-sided pump.",
  parts=[
    ('a', "**A transvalvular axial-flow pump across the pulmonary valve, moving blood from the RV to the PA.** Its inlet sits at the IVC–RA junction and its outlet in the PA, so it crosses both the tricuspid and the pulmonary valves and moves blood from the right atrium side into the PA, bypassing the RV."),
    ('b', "**Placed percutaneously via the right femoral vein; flows up to 4 L/min.** The manufacturer rates it at more than 4 L/min, for up to 14 days of support. The newer Impella RP Flex goes in through the internal jugular vein, with its inlet in the RA."),
    ('c', "**Lowers RA pressure and RV native stroke volume; raises RV and PA systolic pressure.** It offloads the RV while delivering its flow into the PA, so PA pressure rises."),
    ('d', "**More pulmonary blood flow → more LV preload and stroke volume.** This is how a right-sided pump raises systemic output."),
    ('e', "**Cannot oxygenate; low-level anticoagulation, ACT 160–180 s; haemolysis at high pump speed.** Shear stress across the small, fast rotor damages red cells, so haemolysis is the typical device complication; it is watched with plasma free haemoglobin and managed by lowering the pump speed or repositioning. It cannot help a patient who is also hypoxaemic."),
  ],
  mimic=[
    ("Impella RP vs Impella CP", "RP: femoral vein, inflow IVC/RA, outflow PA. CP: femoral artery, inflow LV, outflow aorta. Neither oxygenates."),
  ],
  traps=[
    ("“Impella RP works whatever the PVR”", "It pumps into the PA, so a very high PVR limits it; VA ECMO bypasses the lungs."),
  ],
  decode=[
    ("[pattern] Isolated RV failure, adequate oxygenation — which percutaneous device pumps blood into the PA?", "Impella RP."),
  ],
  punch="Impella RP goes in through the femoral vein and pumps from the right atrium side into the pulmonary artery at about 4 L/min; it raises LV preload but cannot oxygenate and can cause haemolysis.",
)

L['RVF-45'] = dict(
  sub="Cardiology → RV failure → VA ECMO",
  step=6,
  intro="Step 6 again: the device that bypasses both the RV and the lungs.",
  parts=[
    ('a', "**Centrifugal pump: deoxygenated blood from the RA, through an oxygenator and extracorporeal circuit, back to the arterial system.** Drainage is usually from the femoral vein into the RA; return is to the femoral artery or aorta."),
    ('b', "**It bypasses the RV and the pulmonary circulation.** So it works whatever the PVR, which is why it is the device for massive PE with arrest or shock and for RV failure with hypoxaemia. The cost is a higher LV afterload, which can distend a weak LV."),
    ('c', "**Central (sternotomy) or peripheral (peripheral vessels).** Central is used after cardiac surgery; peripheral femoral cannulation is quicker at the bedside."),
  ],
  mimic=[
    ("VA vs VV ECMO", "VA: support for heart and lungs, bypasses the RV. VV: gas exchange only, the RV still has to pump."),
  ],
  traps=[
    ("“VV ECMO supports a failing RV”", "Only indirectly (by correcting hypoxia and hypercapnia); VA ECMO bypasses it."),
  ],
  decode=[
    ("[pattern] Massive PE with cardiac arrest or refractory shock — which ECMO?", "VA ECMO."),
  ],
  punch="VA ECMO drains the RA and returns oxygenated blood to the arteries, bypassing both the RV and the lungs, so it works regardless of PVR.",
)

L['RVF-46'] = dict(
  sub="Cardiology → RV failure → Indications for mechanical support",
  step=6,
  intro="The deck ends with who should get mechanical support. The one real question, a shocked patient hours after heart transplant, was got right by only 23%.",
  parts=[
    ('a', "**Indications: primary graft failure after heart transplant, RV failure after LVAD, inferior MI, post-cardiotomy shock, pulmonary embolus.** All are acute RV failures that may recover. After transplant the new RV, not used to pulmonary hypertension and injured by ischaemia–reperfusion, meets the recipient’s raised PVR. After an LVAD, increased venous return and a septum pulled leftwards overload the RV. Inferior MI comes from the RCA, which supplies the RV."),
    ('b', "**Contraindications: advanced age, multiple co-morbidities, irreversible organ injury.** Support is a bridge; without a way out (recovery, transplant or durable device) it only prolongs dying."),
  ],
  table=dict(title="Shock in the first hours after heart transplant", head=["Cause", "Timing", "Clue"], rows=[["Primary graft dysfunction", "hours", "long ischaemic time, poor biventricular function"], ["RV failure against recipient PH", "hours", "high CVP, dilated RV; needs iNO, inotropes"], ["Tamponade from mediastinal bleeding", "hours", "falling output, rising CVP, drain output"], ["Hyperacute (antibody) rejection", "minutes to hours", "rare with crossmatching"], ["**Acute cellular (T-cell) rejection**", "**days to weeks**", "**least likely in the first hours**"]]),
  mimic=[
    ("Primary graft dysfunction vs rejection", "Primary graft dysfunction: within 24 hours, ischaemia–reperfusion injury. Acute cellular rejection: T-cell mediated, after days to weeks."),
  ],
  traps=[
    ("“Acute on chronic PH” or “tamponade” as least likely early after transplant (77% chose wrong)", "Both are common early causes; T-cell rejection is the least likely because it takes days to weeks."),
  ],
  decode=[
    ("Shock hours after heart transplant, ischaemic time 4 h, CVP 18, on iNO — least likely cause? [DocT GT]", "T-lymphocyte-mediated (acute cellular) rejection."),
  ],
  punch="Mechanical support is for reversible acute RV failure: graft failure, RV failure after LVAD, RV infarction, post-cardiotomy shock and PE; in the first hours after transplant, think graft dysfunction, PH and tamponade, not T-cell rejection.",
)

FLAGS = {
  'RVF-31': "Ranges are the ASE 2005 values (Lang 2005). ASE 2015: basal RV >4.1 cm, mid >3.5 cm, length >8.3 cm, RVOT >3.0 cm (PLAX), proximal RVOT >3.5 cm (short axis), distal RVOT >2.7 cm are abnormal. The watch line ‘mid RV is wider than basal’ is wrong for the current RV-focused view, where the basal diameter is the largest. The explanation gives 2015 values.",
  'RVF-32': "Mixed editions: S′ <10 cm/s, RIMP >0.44/0.55 and 3D RVEF <44% are 2010 or near-2010 values (2010: RIMP >0.40 pulsed). ASE 2015: S′ <9.5 cm/s, RIMP >0.43 pulsed / >0.54 tissue, 3D RVEF <45%. TAPSE <1.7 cm is current. Explanation gives both.",
  'RVF-34': "Watch line advises quoting the function table (p.322), but that table is the older ASE 2010 set; the echo figure (p.321) is ASE 2015 and is the exam answer. TAPSE 17 vs 16 mm are 2015 vs 2010, not one claim ‘loosely stated’. The table’s TAPSE <1.6 cm also disagrees with RVF-32’s <1.7 cm for the same source table.",
  'RVF-25': "a: ‘regional oligaemia → pulmonary oedema’ reads as if one leads to the other; pulmonary oedema appears only when left heart disease is the cause. Wording only; explained.",
  'RVF-26': "b: ‘Q wave in V1–V3’ is non-specific for RV infarction (also anterior MI, RV overload). The Marrow-tested signs (ST elevation III > II, ST elevation in V1) are missing; consider adding. Explained.",
  'RVF-41': "Watch line calls levosimendan ‘the agent of choice’ in RV failure; no guideline says so (HFA/ESC 2016 lists it with dobutamine and PDE III inhibitors at step 5, after noradrenaline). Explained.",
  'RVF-42': "d: ‘hypotension and hypoxia’ are the caveats of IV prostacyclin; inhaled prostacyclin is largely selective and usually improves oxygenation. Card also omits the tested iNO rebound on abrupt withdrawal. Explained.",
  'RVF-44': "a: Impella RP’s inlet is at the IVC–RA junction, not the RV; it moves blood from the RA side to the PA across the tricuspid and pulmonary valves. Manufacturer’s rated flow is >4 L/min (up to 14 days). Explained. (Answer letters b–e are shifted against the question’s c–e; content is complete.)",
  'RVF-36': "Card is correct. The linked DocT GT (IPAH on epoprostenol) keys lifelong anticoagulation, which ESC/ERS 2022 no longer recommends generally (individualise); the trap says so (cardlayer cross line).",
}
