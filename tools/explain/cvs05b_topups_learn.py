# CVS05B top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs05b_learn.py.
# Fields: sub, step (index into cvs05b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from each top-up's own src (DocT QBank, DocT Grand Tests, Marrow QBank); the stems are not in qpack/CVS05B.md, so decode items are labelled [pattern].
# Checked online on 19 Nov 2026: ESC/ERS 2022 TR velocity bands (≤2.8 / 2.9–3.4 / >3.4 m/s) via ReachMD summary; IVC measurement and limits (Ciozda 2016).
# From standard references without a fresh check: RUSH protocol (Perera et al., Emerg Med Clin N Am 2010: pump, tank, pipes; small IVC <1.5 cm in hypovolaemia; AAA >3 cm); ESC 2019 PE
# echo signs (RV/LV >1.0, McConnell, 60/60, D-shaped septum); PLR with VTI rise ≥10–15% (Monnet); ASE 2017 native valvular regurgitation (AR vena contracta <0.3 / 0.3–0.6 / >0.6 cm;
# regurgitant volume <30 / 30–59 / ≥60 mL; regurgitant fraction <30 / 30–49 / ≥50%; EROA <0.10 / 0.10–0.29 / ≥0.30 cm²; PHT >500 / 200–500 / <200 ms); ASE 2009 prosthetic valves
# (aortic peak <3 m/s, mean <20 mmHg, acceleration time <80 ms; mitral peak E <1.9 m/s, mean ≤5 mmHg, VTI ratio <2.2, PHT <130 ms); reviewer check 19 Nov 2026 of the ASE 2024 update (ASE journal-club notes):
# peak E >1.9 m/s and mean >5 mmHg still flag a mitral prosthesis, VTI ratio now >2.5, aortic peak >3 m/s with AT <80 ms = high flow rather than obstruction; RUSH IVC <1.5 cm collapsing = low CVP, >2.5 cm
# non-collapsing = high, aorta >5 cm in shock = rupture until proved otherwise (WikEM RUSH page);
# ASE/SCA 2013 TEE comprehensive exam (transgastric mid-papillary SAX); TEE contraindications (oesophageal stricture, varices, recent oesophageal surgery).
T = {}

T['T_8cd6b5dd'] = dict(
  sub="Cardiology → Echo in ICU → Shock on POCUS (RUSH)",
  step=5,
  intro="Step 5 puts the views to work. FATE grades the heart; RUSH (pump, tank, pipes) is the shock protocol that adds the IVC, lungs, abdomen, aorta and leg veins to sort shock into its four types. Three Grand Test questions ask which type a set of findings fits.",
  parts=[
    ('a', "**Pump: poor LV contraction with dilated chambers → cardiogenic; hyperdynamic LV → hypovolaemic or distributive.** A dilated, poorly contracting LV cannot generate output; a hyperdynamic one is either underfilled (hypovolaemia) or emptying against a low afterload (sepsis), and the tank decides which (ECHO-36)."),
    ('b', "**Tank: small IVC (<1.5 cm) collapsing >50% with ‘kissing’ papillary muscles → hypovolaemic; a VTI rise >10–15% on PLR confirms responsiveness.** A small collapsing IVC means low RAP (ECHO-19), and end-systolic cavity obliteration means an underfilled LV; the PLR test shows that stroke volume actually rises with preload (ECHO-20)."),
    ('c', "**Plethoric IVC plus a cause → obstructive: effusion with RA/RV diastolic collapse (tamponade), RV larger than LV with a D-shaped septum (PE), absent lung sliding (tension pneumothorax).** In all three the venous return is blocked before the LV, so the IVC is full and the LV small. The effusion compresses the low-pressure right chambers; in PE the pressure-loaded RV dilates (RV/LV >1.0) and flattens the septum; in tension pneumothorax the lung never touches the chest wall, so sliding disappears."),
    ('d', "**Plethoric IVC + poor LV + bilateral B-lines → cardiogenic; normal or small IVC + hyperdynamic LV → early sepsis.** Raised left filling pressure pushes fluid into the interstitium (B-lines) and backs up to the IVC; in early sepsis venodilation keeps the IVC normal or small while the LV empties against low SVR."),
    ('e', "**Pipes: aortic aneurysm or dissection flap, and leg-vein compression, complete the scan.** An abdominal aorta >3 cm is aneurysmal, and in a shocked patient one >5 cm is treated as rupture (haemorrhagic shock) until proved otherwise; a flap means dissection, which can bleed or cause tamponade. A non-compressible femoral or popliteal vein supports PE."),
  ],
  table=dict(title="RUSH by shock type", head=["Type", "Pump", "Tank (IVC)", "Pipes / other"], rows=[["Hypovolaemic", "hyperdynamic, small", "small, collapsing", "AAA, free fluid"], ["Distributive", "hyperdynamic (early)", "normal or small", "—"], ["Cardiogenic", "poor, dilated", "plethoric", "B-lines"], ["Obstructive", "effusion / dilated RV", "plethoric", "DVT; absent sliding"]]),
  mimic=[
    ("Hypovolaemic vs early distributive", "Both hyperdynamic; hypovolaemia has a small collapsing IVC and small end-diastolic LV, early sepsis a normal LV size."),
    ("Obstructive vs cardiogenic with a plethoric IVC", "Obstructive: small LV with a visible cause (effusion, dilated RV, no sliding). Cardiogenic: dilated poor LV with B-lines."),
  ],
  traps=[
    ("“A plethoric IVC means cardiogenic shock”", "It means a high RAP from any cause: tamponade, PE and tension pneumothorax also give it, so look for the cause before calling it the pump."),
    ("“A hyperdynamic LV means hypovolaemia”", "Only with a small IVC and small end-diastolic LV; with a normal size it is low SVR."),
  ],
  decode=[
    ("Shock, plethoric IVC, RV larger than LV with a D-shaped septum [pattern]", "Obstructive shock from PE."),
    ("Shock, small IVC collapsing >50%, kissing papillary muscles [pattern]", "Hypovolaemic shock."),
  ],
  punch="Pump, tank, pipes: a dilated poor LV with a full IVC and B-lines is cardiogenic, a full IVC with a small LV and a cause is obstructive, and a hyperdynamic LV is hypovolaemic only if the tank is empty.",
)

T['T_11e87634'] = dict(
  sub="Cardiology → Echo in ICU → TEE vs TTE",
  step=1,
  intro="Step 1 is about windows, and TEE is the window from behind: the oesophagus lies right against the left atrium with no lung or rib in the way. Two questions ask when that advantage matters and when it does not.",
  parts=[
    ('a', "**TEE: prosthetic and native valve detail, LA/LAA thrombus before cardioversion, aortic dissection, endocarditis (vegetation, abscess), guiding valvuloplasty, LAA occlusion and ASD/PFO closure, intra-operative monitoring.** Posterior structures (LA, appendage, mitral valve, thoracic aorta) are closest to the probe, so a higher-frequency, higher-resolution image is possible; the LAA is barely seen on TTE, and prosthetic valves cast shadows that hide the atrial side from the front."),
    ('b', "**Pericardiocentesis is guided by TTE (subcostal or apical); TEE sees the anterior pericardial space poorly.** The needle enters from the front or below, where the fluid is closest to the skin; TTE shows that path, while the TEE probe looks from behind."),
    ('c', "**TEE is semi-invasive (sedation, oesophageal injury); TTE comes first in most ICU questions.** It needs sedation or a protected airway and risks oesophageal and pharyngeal injury; oesophageal perforation, stricture, tumour and recent oesophageal surgery are contraindications, and varices a relative one."),
    ('d', "**In shock, the transgastric mid-papillary short-axis view gives LV size, systolic function and wall motion in all three coronary territories in one look; mid-oesophageal views give valves and chambers, upper-oesophageal views the great vessels.** It is the TEE counterpart of the PSAX papillary level (ECHO-25), which is why it is the monitoring view in theatre and in the ICU."),
  ],
  mimic=[
    ("TEE vs TTE for tamponade", "TTE (subcostal) diagnoses it and guides the needle; TEE is needed only for loculated posterior collections, as after cardiac surgery."),
  ],
  traps=[
    ("“TEE guides pericardiocentesis”", "TTE does; TEE sees the anterior space poorly."),
    ("“TTE excludes LA appendage thrombus before cardioversion”", "Only TEE shows the appendage reliably."),
  ],
  decode=[
    ("TEE view for LV function and wall motion in all coronary territories in shock? [pattern]", "Transgastric mid-papillary short axis."),
    ("Imaging to guide pericardiocentesis? [pattern]", "TTE, subcostal or apical."),
  ],
  punch="TEE wins for posterior structures (LA appendage, prosthetic and mitral valves, thoracic aorta, endocarditis) because it looks from behind; for the front of the heart and the pericardial needle TTE is better and comes first.",
)

T['T_ee74dd4a'] = dict(
  sub="Cardiology → Echo in ICU → Valve echo numbers",
  step=6,
  intro="Step 6’s numbers extended to the valves: Marrow asks the aortic regurgitation severity cut-offs and what normal Doppler looks like across a prosthetic valve.",
  parts=[
    ('a', "**AR vena contracta: <0.3 cm mild, 0.3–0.6 moderate, >0.6 cm severe.** The vena contracta is the narrowest part of the jet just below the valve, which reflects the size of the regurgitant orifice and is little affected by loading or by the jet’s spread."),
    ('b', "**AR regurgitant volume <30 / 30–59 / ≥60 mL; pressure half-time >500 / 200–500 / <200 ms.** The more severe the leak, the faster aortic and LV diastolic pressures equalise, so the CW slope steepens and the half-time shortens. Half-time also shortens when LV diastolic pressure is high for other reasons, so it supports rather than decides severity."),
    ('c', "**Normal prosthetic aortic valve: peak velocity ≤3 m/s, mean gradient ≤20 mmHg.** Every prosthesis is mildly stenotic compared with a native valve, so its normal gradient is higher; above these values, consider obstruction (thrombus, pannus) or patient–prosthesis mismatch, or high flow."),
    ('d', "**Normal prosthetic mitral valve: peak velocity <1.9 m/s, mean gradient ≤5 mmHg.** Both figures rise with heart rate and flow, so they are read with the heart rate and with the VTI ratio across the valve."),
  ],
  table=dict(title="AR severity (ASE 2017)", head=["Measure", "Mild", "Moderate", "Severe"], rows=[["Vena contracta (cm)", "<0.3", "0.3–0.6", ">0.6"], ["Regurgitant volume (mL)", "<30", "30–59", "≥60"], ["Pressure half-time (ms)", ">500", "200–500", "<200"]]),
  mimic=[
    ("Pressure half-time in AR vs in mitral stenosis", "In AR a SHORT half-time means severe disease; in MS a LONG half-time means a tight valve (MVA ≈ 220 ÷ PHT)."),
  ],
  traps=[
    ("“A longer AR half-time means more severe AR”", "The reverse: <200 ms is severe."),
    ("“Any mean gradient above 10 mmHg across a prosthetic aortic valve is obstruction”", "Up to 20 mmHg is normal for a prosthesis."),
  ],
  decode=[
    ("AR vena contracta 0.7 cm — severity? [pattern]", "Severe (>0.6 cm)."),
    ("Normal mean gradient across a prosthetic mitral valve? [pattern]", "≤5 mmHg (peak velocity <1.9 m/s)."),
  ],
  punch="Severe AR: vena contracta >0.6 cm, regurgitant volume ≥60 mL, half-time <200 ms. A normal prosthesis is mildly stenotic: aortic peak ≤3 m/s and mean ≤20 mmHg, mitral peak <1.9 m/s and mean ≤5.",
)
