# CVS05B — Explain v3 ("Learn" depth): echocardiography in the ICU, part 2 — TTE planes and windows, marker directions, the subcostal window and the IVC (technique, RAP bands,
# fluid responsiveness), the pleural view, PLAX, PSAX and breadloafing (papillary, mitral and aortic levels), the apical views (A4C, A5C, A2C, A3C, foreshortening, rotations compared),
# which view measures what, FATE (basic and extended views, goals), normal LV and chamber dimensions, systolic function grading, normal Doppler values.
# No mnemonics or hooks. Driven by qpack/CVS05B.md (36 question links; ECHO-19 IVC and RAP asked 9 times, ECHO-40 Doppler values 5, ECHO-22 PLAX and ECHO-36 FATE goals 4 each,
# ECHO-20 and ECHO-27 three each). ECHO-14, 15, 16, 24, 26, 28, 29, 30, 31, 32, 33, 34, 35, 37 and 38 have no linked question and get short explanations with [pattern] decode items.
# Three Top-up cards in cvs_topups.json (RUSH, TEE vs TTE, valve numbers): written in cvs05b_topups_learn.py. No `fix` entries for CVS05B in trace/test/data/qbank.json (checked 19 Nov 2026).
# cvs_cardlayer.json `lines` read and used (ECHO-19, 21, 22, 36, 40).
# Checked online on 19 Nov 2026:
#  - FATE card (Jensen et al., Eur J Anaesthesiol 2004;21:700; csarim.cz copy of the card): positions 1–4 (subcostal 4C, apical 4C, PLAX + PSAX, pleural scanning); extended views = subcostal
#    IVC and liver, PSAX at MITRAL AND AORTIC levels, A5C, A2C, apical long axis; goals 1–6 (obvious pathology, wall thickness and dimensions, biventricular function, pleura both sides, relate
#    to clinical context, add other ultrasound); grading table EF ≥55 / 45–54 / 30–44 / <30, FS ≥25 / 20–24 / 15–19 / <15, MSS <10 / 7–12 / 13–24 / >24 (overlap is on the card itself),
#    MAPSE ≥11 / 9–10 / 6–8 / <6, TAPSE 16–20 / 11–15 / 6–10 / <6 (the deck card uses the ASE ≥17 normal, per its watch line); EF ≈ 2 × FS; Doppler: 4V², AO <2, PA <1, TI <2.5 m/s, DT 140–240 ms,
#    E <1.2 m/s, E/A >1 (age dependent), TVI (tissue velocity imaging) E/e′ <8–10, IVC <20 mm with about 50% inspiratory collapse.
#  - ASE/EACVI 2015 chamber quantification (Lang et al.; values read from two reference summaries, mycardio/cardi pages, because asecho.org PDFs redirected): LVEF normal 52–72% (men), 54–74%
#    (women); mildly abnormal 41–51 / 41–53; moderately 30–40; severely <30. IVS and posterior wall 0.6–1.0 cm (men), 0.6–0.9 cm (women). LA volume index ≤34 mL/m² (mild 35–41, moderate
#    42–48, severe >48). RV basal diameter >41 mm and mid >35 mm = dilated (RV-focused A4C). TAPSE <17 mm, S′ <9.5 cm/s, FAC <35% = RV systolic dysfunction; TAPSE mean 24 mm.
#  - IVC (Ciozda et al., Cardiovasc Ultrasound 2016;14:33, summarising ASE): subcostal long axis, supine, measured immediately caudal to the hepatic vein junction, about 1–2 cm from the RA;
#    normal 0–5, intermediate 5–10, high 10–20 mmHg; IVC estimates of RAP in ventilated patients are unreliable and ASE 2015 advises against routine use; dilated IVC without raised RAP in
#    athletes; unreliable with severe TR.
#  - ESC/ERS 2022 PH guideline (via a ReachMD CME summary): peak TR velocity ≤2.8 m/s low, 2.9–3.4 intermediate, >3.4 high echo probability; TAPSE/sPAP <0.55 mm/mmHg supports PH.
#  - ASE 2025 diastolic function update (Nagueh et al., JASE July 2025, ASE press release 7 Jul 2025; cut-offs from the Klein 2025 lecture slides): replaces ASE/EACVI 2016; average E/e′ >14,
#    TR ≥2.8 m/s (or PASP ≥35 mmHg), LAVI >34 mL/m², LA reservoir strain ≤18%; reduced e′ septal ≤6, lateral ≤7 cm/s; E/A ≤0.8 or ≥2.
#  - Apical rotations (123sonography e-book, LITFL echo basics): A2C ≈ 60° COUNTER-clockwise from A4C; A3C a further ~60° counter-clockwise (≈120° from A4C), marker to the right shoulder;
#    A5C by tilting (angulating) anteriorly from A4C.
# From standard references without a fresh check (confident unless said): ASE 2010 right heart guideline (Rudski) RAP table 3/8/15 with 2.1 cm and 50% sniff collapse, secondary indices
# (restrictive tricuspid filling, tricuspid E/e′ >6, hepatic vein diastolic predominance), downgrade/upgrade rule in the intermediate band; ASE 2015 LVIDd 4.2–5.8 cm (men), 3.8–5.2 cm (women),
# aortic sinus about 3.4 ± 0.3 cm (men), 3.0 ± 0.3 cm (women), RVOT proximal (PLAX) >3.0 cm; ASE/EACVI 2016 e′ septal <7, lateral <10 cm/s; ESC 2019 PE echo signs (RV/LV >1.0, TAPSE <16 mm,
# McConnell, 60/60, flattened septum, right heart thrombus); distensibility index >18% (Barbier 2004) and ΔIVC >12% (Feissel 2004) in passively ventilated patients; PLR with VTI rise ≥10–15%
# (Monnet); Yang 1992 (transudates anechoic, but anechoic effusions can be exudates); EPSS >7 mm abnormal; ACC/AHA 2020 severe AS Vmax ≥4 m/s, mean ≥40 mmHg; severe MS MVA ≤1.5 cm².
# Could not open: asecho.org guideline PDFs (redirected to the home page) and PMC full texts (captcha).
# Second check (reviewer, 19 Nov 2026): ASE 2025 right heart guideline (Mukherjee et al., JASE 2025, asecho.org PDF; replaces Rudski 2010): RAP 3 / 8 / 15 mmHg with 2.1 cm and ≥50% collapse,
#   20 mmHg if IVC >2.5 cm with no variation; secondary indices RA enlargement, interatrial septum bulging into the LA, restrictive RV filling, tricuspid E/e′ >6, hepatic vein systolic filling
#   fraction <55% (S/D <1); indeterminate band downgraded to 3 or upgraded to 15; IVC measured 0.5–3.0 cm from the RA ostium, distal to the hepatic vein; ventilated: collapse unreliable, IVC ≤2.1 cm
#   identifies RAP <10 mmHg; RV basal <4.1, mid <3.5 cm; TAPSE normal >17 mm, mild 13–17, moderate 10–13, severe ≤10. Lang 2015 LVIDd 42.0–58.4 (men) / 37.8–52.2 mm (women) (studfile copy of
#   Table 2). ASE 2025 diastolic (Klein slides): e′ septal ≤6, lateral ≤7, average ≤6.5 cm/s; E/e′ average >14 (septal >15, lateral >13); TR ≥2.8 m/s or PASP ≥35; LAVI >34; LARS ≤18%.
#   ESC 2019 PE (ACC summary): RV/LV ≥1.0 and TAPSE <16 mm. Apical rotations (123sonography): A2C ≈60° counter-clockwise from A4C, A3C a further ≈60° counter-clockwise.

SPINE = [
  ("Planes, windows and the marker", "The heart is imaged in three orthogonal planes from five windows, and the marker dot fixes which way the plane is cut, so every standard view is a window plus a plane plus a marker direction."),
  ("Subcostal window and the IVC", "The subcostal window works supine when the chest windows fail, and the IVC’s size and its change with breathing estimate right atrial pressure well and fluid responsiveness only modestly."),
  ("Parasternal views: long and short", "PLAX shows the LV, LVOT, aortic root and the relation of fluid to the descending aorta; rotating 90° clockwise gives PSAX slices, where all three coronary territories are seen together."),
  ("Apical views line the beam up", "Apical views put the beam parallel to blood flow, so Doppler of mitral and tricuspid inflow, the LVOT and the TR jet comes from them, while diameters come from views where the beam is perpendicular."),
  ("FATE: sequence, goals, pleura", "FATE strings the basic views and a bilateral pleural scan into one protocol that excludes obvious pathology, sizes the chambers and grades function by eye."),
  ("Numbers: size, function, Doppler", "Normal dimensions and systolic grading bands turn pictures into numbers, and the Bernoulli equation turns a velocity into a pressure: RVSP = 4V² + RAP."),
]

PRIMER = "Ultrasound images only what the beam can reach through soft tissue or fluid; air (lung) and bone block it, so the heart is seen through a few ‘windows’ where it touches the chest wall or can be reached from the abdomen. Two-dimensional images show structure best when the beam hits it at right angles, whereas Doppler measures velocity best when the beam runs parallel to the blood (the error grows with the cosine of the angle). The inferior vena cava is a compliant, valveless vein draining straight into the right atrium, so its size and its change with breathing follow right atrial pressure. CVS05A covered the physics and the basic principles; this deck is the views, the IVC, the FATE protocol and the normal numbers."

L = {}

L['ECHO-14'] = dict(
  sub="Cardiology → Echo in ICU → TTE planes",
  step=1,
  intro="Step 1 starts with geometry: before any window or view, the heart is described in three planes at right angles to each other. Every named view lies in one of them, which is why the planes come first.",
  parts=[
    ('a', "**Long axis: aortic root to LV apex.** The plane runs along the length of the LV, through the aortic valve and the apex. PLAX and the apical 3-chamber (apical long axis) view both lie in it, which is why both show the mitral and aortic valves together."),
    ('b', "**Short axis: left mid-clavicle to the RIGHT hip.** The heart lies obliquely, its long axis running roughly from the right shoulder towards the left hip, so a plane at right angles to it runs from the left shoulder region down to the right hip. PSAX lies in it and cuts the LV as a circle."),
    ('c', "**Four-chamber axis: apex to the base, perpendicular to the other two.** This plane cuts through both atria and both ventricles at once; the apical and subcostal four-chamber views lie in it."),
  ],
  mimic=[
    ("Long axis vs short axis", "Long axis shows the LV as an elongated chamber with the aortic root; short axis shows it as a ring."),
  ],
  traps=[
    ("“The short axis runs from the left mid-clavicle to the left hip”", "It crosses the body diagonally, to the RIGHT hip, because it is perpendicular to a long axis that points to the left hip."),
  ],
  decode=[
    ("Which TTE plane runs from the aortic root to the LV apex? [pattern]", "The long axis."),
  ],
  punch="Three planes at right angles: long (root to apex), short (left shoulder to right hip, across it) and four-chamber (apex to base through all four chambers). Each view sits in one of them.",
)

L['ECHO-15'] = dict(
  sub="Cardiology → Echo in ICU → Probe positions",
  step=1,
  intro="Still step 1: the windows are the places where the heart can be reached without lung or bone in the way. Each has a fixed landmark.",
  parts=[
    ('a', "**Parasternal: 2nd to 4th intercostal space, LEFT sternal border.** Here the RV outflow and the heart touch the anterior chest wall beside the sternum, with no lung in between in most patients (more so in the left lateral position)."),
    ('b', "**Apical: 4th to 5th intercostal space, lateral.** The probe goes on the apex beat, usually around the 5th space near the mid-clavicular to anterior axillary line; turning the patient to the left brings the apex against the chest wall."),
    ('c', "**Subcostal: below the xiphoid.** The beam passes through the liver, which is an acoustic window, so it works when lungs or chest wall block the parasternal and apical windows (ECHO-17)."),
    ('d', "**Right parasternal: 2nd to 4th intercostal space, RIGHT sternal border.** Used mainly to line the beam up with an aortic stenosis jet when the ascending aorta runs to the right."),
    ('e', "**Suprasternal: suprasternal notch.** Shows the aortic arch and descending aorta (coarctation, dissection extending into the arch)."),
  ],
  mimic=[
    ("Parasternal vs right parasternal", "Same 2nd–4th spaces, opposite side of the sternum."),
  ],
  traps=[
    ("“The apical window is in the 2nd–4th space”", "Apical is the only window defined by the 4th–5th space, laterally, at the apex beat."),
  ],
  decode=[
    ("Probe at the left sternal border, 3rd intercostal space — which window? [pattern]", "Parasternal."),
  ],
  punch="Parasternal and right parasternal share the 2nd–4th spaces and differ by side; apical is the apex beat at the 4th–5th space; subcostal is under the xiphoid through the liver; suprasternal is the notch.",
)

L['ECHO-16'] = dict(
  sub="Cardiology → Echo in ICU → Marker dot directions",
  step=1,
  intro="The last part of step 1: the marker dot on the probe matches a mark on the screen, so it decides which way the plane is cut and which side of the image is which. Get it wrong and the anatomy is mirrored or the wrong plane appears.",
  parts=[
    ('a', "**Subcostal: LEFT shoulder.** The probe lies flat under the xiphoid with the plane in the four-chamber orientation, the marker towards the patient’s left."),
    ('b', "**PLAX: RIGHT shoulder.** The LV long axis runs from right shoulder to left hip, so the marker points to the right shoulder to cut along it."),
    ('c', "**PSAX: LEFT shoulder.** Turning the probe 90° clockwise from PLAX moves the marker from the right to the left shoulder and cuts across the LV (ECHO-23)."),
    ('d', "**Apical 4-chamber: LEFT shoulder.** With the marker to the patient’s left (cardiology convention), the left heart is displayed on the right of the screen."),
    ('e', "**Apical 2-chamber: LEFT side of the NECK.** Rotating from A4C swings the marker up towards the neck, cutting a plane that misses the RV (ECHO-30)."),
  ],
  mimic=[
    ("Cardiology vs emergency-medicine convention", "Emergency-medicine machines often put the screen marker on the other side, so the apical and subcostal marker points to the patient’s right; the image looks the same, only the probe is held differently."),
  ],
  traps=[
    ("“PSAX marker points to the right shoulder”", "Only PLAX does; PSAX is rotated 90° clockwise to the left shoulder."),
  ],
  decode=[
    ("Probe marker towards the right shoulder at the left sternal edge — which view? [pattern]", "PLAX."),
  ],
  punch="Two exceptions to learn: PLAX is the only right-shoulder view and A2C the only neck view; subcostal, PSAX and A4C all point to the left shoulder.",
)

L['ECHO-17'] = dict(
  sub="Cardiology → Echo in ICU → Subcostal view",
  step=2,
  intro="Step 2 begins with the window that still works in a ventilated, emphysematous or obese patient. One real question asks which view assesses IVC collapse and RA filling in suspected tamponade; about one in four missed it.",
  parts=[
    ('a', "**SUPINE, with a relaxed abdomen.** Flexing the knees relaxes the rectus muscles so the probe can be pressed under the costal margin; no turning is needed, which suits a ventilated or unstable patient and the pulse check in cardiac arrest."),
    ('b', "**Probe under the xiphisternum.** The liver is the acoustic window, so the beam reaches the heart without passing through lung."),
    ('c', "**Marker dot towards the LEFT shoulder.** This gives the subcostal four-chamber view; rotating towards a cranio-caudal (north–south) orientation then brings in the IVC (ECHO-18)."),
    ('d', "**Useful in obesity, emphysema and chest wall deformity.** Hyperinflated lung (emphysema, high PEEP) gets between the heart and the chest wall and kills the parasternal and apical windows; the subcostal approach comes from below the lung."),
    ('e', "**Assesses IVC variability, pericardial effusions and RV enlargement.** The RV free wall lies closest to the probe here, so a pericardial effusion and RA or RV diastolic collapse in tamponade are seen well, and the IVC is in the same window, which is why it is the view for tamponade physiology."),
  ],
  mimic=[
    ("Subcostal vs apical 4-chamber in tamponade", "Both show RA and RV collapse, but only the subcostal window also shows the IVC; A4C is the view for Doppler of mitral inflow variation."),
  ],
  traps=[
    ("“Apical four-chamber best assesses IVC collapse and RA filling”", "The IVC cannot be seen from the apex; the subcostal long axis is the answer (72% right)."),
  ],
  decode=[
    ("ICU patient, suspected tamponade — view for IVC collapse and RA filling? [DocT QBank]", "Subcostal long axis."),
    ("Ventilated patient with COPD, no parasternal window — which view? [pattern]", "Subcostal: supine, through the liver, below the lung."),
  ],
  punch="Subcostal is the supine view through the liver, so it works when lung blocks the chest windows, and it shows the effusion, the RV and the IVC in one place.",
)

L['ECHO-18'] = dict(
  sub="Cardiology → Echo in ICU → IVC technique",
  step=2,
  intro="Step 2 continues with how to measure the IVC so the number means something. The one linked question (tamponade, which view) is answered by part a; the rest is technique that decides whether the RAP estimate in ECHO-19 is right.",
  parts=[
    ('a', "**Subcostal approach, longitudinal view.** The IVC is followed in its long axis as it passes through the liver into the right atrium."),
    ('b', "**North–south probe orientation.** From the subcostal four-chamber view the probe is rotated so the marker points to the head, cutting the IVC lengthways."),
    ('c', "**The IVC lies slightly to the RIGHT of midline.** The aorta lies to the left; telling them apart matters, because a pulsatile, thick-walled aorta that does not change with breathing can be mistaken for a plethoric IVC. The IVC enters the RA and receives the hepatic veins; the aorta gives off the coeliac axis and SMA."),
    ('d', "**Transducer below the xiphisternum, 1–2 cm to the right of midline.**"),
    ('e', "**M-mode line through the IVC 1 cm CAUDAL to its junction with the hepatic vein.** ASE (2015, and the 2025 right heart guideline) places the measurement just distal to the hepatic vein junction, about 0.5–3.0 cm from the RA ostium. The IVC’s diameter varies along its length and the vessel moves with the diaphragm, so only a fixed site gives numbers that can be compared with the reference bands and from one scan to the next."),
    ('f', "**Measure the maximum and minimum diameter.** These give the collapsibility index, (max − min) ÷ max, used with the maximum diameter for RAP (ECHO-19). The line must cut the vessel at right angles through its centre: an off-centre cut underestimates the diameter, and the IVC moving with breathing can slide out of the M-mode line, so check on 2D."),
  ],
  mimic=[
    ("IVC vs aorta", "IVC: right of midline, thin wall, enters the RA, hepatic veins drain into it, changes with breathing. Aorta: left, thick wall, pulsatile, branches anteriorly."),
  ],
  traps=[
    ("“Measure at the junction with the RA or at the diaphragm”", "Measure about 1 cm caudal to the hepatic vein junction; elsewhere the diameter, and therefore the RAP estimate, changes."),
  ],
  decode=[
    ("Which view assesses IVC collapse and RA filling? [DocT QBank]", "Subcostal long axis."),
    ("Where is the IVC diameter measured? [pattern]", "About 1 cm caudal to the hepatic vein junction, on M-mode or 2D, maximum and minimum."),
  ],
  punch="Find the IVC to the right of midline in a north–south subcostal view, confirm it is not the aorta, and measure maximum and minimum about 1 cm below the hepatic vein junction.",
)

L['ECHO-19'] = dict(
  sub="Cardiology → Echo in ICU → IVC and right atrial pressure",
  step=2,
  intro="Step 2’s central card, and the most-asked in the deck (nine questions). The IVC is a floppy tube connected straight to the right atrium, so its size and whether it collapses on a sniff tell you the atrial pressure. Two questions were answered right by about half: one where the stem is set in a ventilated patient, and one RVSP calculation where most forgot to add the RAP.",
  parts=[
    ('a', "**Normal RAP 0–5 (3) mmHg: IVC ≤2.1 cm with >50% collapse on sniff.** When RAP is low the IVC sits on the steep part of its compliance curve: it is small, and the fall in intrathoracic pressure on spontaneous inspiration (exaggerated by a sniff) empties it by more than half."),
    ('b', "**Intermediate RAP 5–10 (8) mmHg: either ≤2.1 cm with <50% collapse, or >2.1 cm with >50% collapse.** Each pattern has one ‘normal’ and one ‘high’ feature, so the two cancel to a middle value. ASE’s rule (2010, kept in the 2025 right heart guideline): in this band look at the secondary indices; if none is present the estimate is moved down to 3, if they are present up to 15, and if doubt remains it stays at 8."),
    ('c', "**High RAP 10–20 (15) mmHg: IVC >2.1 cm with <50% collapse; secondary indices RA enlargement, RV hypertrophy, hepatic vein S/D <1, tricuspid E/e′ >6.** A full IVC at high pressure is on the flat part of its compliance curve and cannot collapse. Hepatic vein flow turns diastolic-predominant because the stiff, high-pressure RA blunts systolic forward flow, and a high tricuspid E/e′ reflects raised RA pressure, as mitral E/e′ does for the LA (ECHO-40). In the ASE 2025 right heart guideline the secondary indices are RA enlargement, an interatrial septum bulging into the LA, restrictive right-sided filling, tricuspid E/e′ >6 and a hepatic vein systolic filling fraction <55% (S/D <1); RV hypertrophy is not among them, and they are used mainly to settle the intermediate band. ASE 2025 also adds a fifth band: IVC >2.5 cm with no respiratory variation means about 20 mmHg."),
  ],
  table=dict(title="IVC and RAP (spontaneous breathing, ASE)", head=["IVC max", "Sniff collapse", "RAP (mmHg)"], rows=[["≤2.1 cm", ">50%", "**0–5 (3)**"], ["≤2.1 cm", "<50%", "5–10 (8)"], [">2.1 cm", ">50%", "5–10 (8)"], [">2.1 cm", "<50%", "**10–20 (15)**"]]),
  mimic=[
    ("Plethoric IVC from tamponade vs from RV failure or volume overload", "All three are dilated and non-collapsing; tamponade adds an effusion with RA/RV diastolic collapse and a small LV (GT2), RV failure adds a dilated RV."),
    ("Spontaneous breathing vs passive ventilation", "Spontaneous inspiration lowers intrathoracic pressure and the IVC collapses; positive-pressure inspiration raises it and the IVC distends. Sniff-collapse bands apply only to spontaneous breathing."),
    ("Large IVC with normal RAP", "Trained athletes and some young patients have a large IVC with normal pressure; severe TR dilates it regardless; raised intra-abdominal pressure can make a small IVC look ‘empty’."),
  ],
  traps=[
    ("“Ventilated patient, IVC 17 mm, >20% variation — tamponade or RV failure”", "Only half got this right (49%, 54%). Both tamponade and RV failure give a dilated, fixed IVC. A 17 mm IVC is below 2.1 cm and it changes with each breath, so the RAP is low (key A). The stem’s ‘collapsibility’ is spontaneous-breathing language: in a passively ventilated patient the IVC DISTENDS on inspiration, and a distensibility index >18% predicts fluid responsiveness. ASE also warns that IVC collapse cannot estimate RAP reliably under positive pressure; the useful finding there is size, and the ASE 2025 right heart guideline states that an IVC ≤2.1 cm in an intubated patient accurately identifies RAP <10 mmHg, which fits this 17 mm IVC."),
    ("“RVSP = 4 × 3.5² = 49 mmHg”", "Only 33% got this: 49 is the RV–RA gradient. RVSP = 4V² + RAP = 49 + 10 = 59 ≈ 60 mmHg (key B)."),
    ("“Dilated IVC with minimal collapse means fluid responsiveness”", "It means a high RAP (84% right); a full, fixed IVC is the least likely to respond to fluid (ECHO-20)."),
  ],
  decode=[
    ("Ventilated, IVC 17 mm with >20% ‘collapsibility’ — what does it suggest? [DocT QBank, DocT GT]", "Low right atrial pressure."),
    ("TR peak 3.5 m/s, RAP 10 mmHg — RVSP? [DocT QBank]", "4 × 12.25 = 49, + 10 = 59 ≈ 60 mmHg."),
    ("Effusion, RA diastolic collapse, dilated non-collapsing IVC — haemodynamic profile? [DocT GT]", "↓ LVEDA, ↑ IVC diameter, narrow pulse pressure, ↑ CVP."),
    ("Small IVC with >50% collapse after surgery; dilated IVC with minimal collapse in shock? [DocT GT, Marrow, NEET 2024]", "Hypovolaemia (normal or low RAP); elevated RAP. Normal IVC = <2.1 cm with >50% collapse."),
  ],
  punch="Small and collapsing is low RAP, large and fixed is high RAP, and one of each is the middle band. The sniff rule is for spontaneous breathing only: under positive pressure the IVC distends instead.",
  extra=[
    dict(q="How is RVSP estimated, and when does the TR velocity suggest pulmonary hypertension?", a="RVSP = 4 × (peak TR velocity)² + RAP, and it equals PA systolic pressure if there is no pulmonary stenosis or RVOT obstruction. ESC/ERS 2022: peak TR velocity ≤2.8 m/s is low echo probability of PH, 2.9–3.4 m/s intermediate, >3.4 m/s high (combined with other RV, PA and RA/IVC signs)."),
  ],
)

L['ECHO-20'] = dict(
  sub="Cardiology → Echo in ICU → IVC and fluid responsiveness",
  step=2,
  intro="Step 2 then asks a different question of the same vessel: not ‘what is the pressure?’ but ‘will the stroke volume rise with fluid?’. Three questions test it, and the cut-offs differ from the RAP table on purpose.",
  parts=[
    ('a', "**Check the absolute number AND the variability (collapsibility) of the IVC with inspiration.** A diameter alone describes the pressure; variation with breathing shows that the vessel, and so the right heart’s filling, is on the steep part of its curve."),
    ('b', "**LESS likely fluid responsive: >2 cm, <50% collapse.** A large, fixed IVC means a high RAP; the right heart is already on the flat part of the Frank–Starling curve, so more volume mostly raises venous pressure."),
    ('c', "**MORE likely fluid responsive: <1 cm, >50% collapse. This only suggests: the IVC alone predicts modestly, worse in spontaneous breathing; confirm with PLR or VTI change.** Fluid responsiveness needs both ventricles to be preload-dependent, and the IVC reports only the right side. In spontaneous breathing the collapse depends on how hard the patient breathes (a vigorous inspiration collapses any IVC), and raised intra-abdominal pressure compresses it. In passively ventilated patients (tidal volume about 8 mL/kg or more, no breathing effort) the distensibility index, (max − min) ÷ min, >18% (Barbier 2004), or the respiratory variation (max − min) ÷ mean >12% (Feissel 2004), performs better; unlike pulse pressure variation, it does not need sinus rhythm. The test that settles it is a passive leg raise with a rise in LVOT VTI (or stroke volume) of about 10–15%."),
  ],
  mimic=[
    ("RAP thresholds vs fluid-responsiveness thresholds", "RAP uses 2.1 cm and 50%; fluid responsiveness uses <1 cm and >2 cm, leaving 1–2 cm unclassified."),
    ("Collapsibility vs distensibility", "Collapsibility (÷ max) for spontaneous breathing; distensibility (÷ min, >18%) for passive ventilation."),
  ],
  traps=[
    ("“Septic shock, 1 L given, IVC varies >50% — start noradrenaline (or do a PLR first)”", "The key is another 500–1,000 mL bolus (76% right): the IVC already shows preload dependence and only 1 L of the initial 30 mL/kg has gone in. Noradrenaline may be started alongside if hypotension persists, but stopping fluid here is wrong; corticosteroids are for shock that persists on vasopressors."),
    ("“Dilated IVC with minimal collapse means fluid responsiveness”", "It means a high RAP, the opposite (84% right)."),
    ("“A 1.5 cm IVC predicts fluid responsiveness”", "1–2 cm is the grey zone; neither threshold applies, so use PLR or VTI."),
  ],
  decode=[
    ("Septic shock after 1 L, IVC >50% variation — next step? [DocT GT]", "Another 500–1,000 mL crystalloid bolus."),
    ("Shock, dilated IVC with minimal collapse — indicates? [DocT GT]", "Elevated right atrial pressure (not fluid responsiveness)."),
    ("Ventilated patient, IVC 17 mm, >20% respiratory variation? [DocT GT]", "Low RAP; in a ventilated patient read it as distensibility (>18% suggests responsiveness)."),
  ],
  punch="A tiny IVC that collapses suggests fluid will help and a large fixed one suggests it will not, but the IVC only hints; a PLR with a VTI rise of 10–15% decides.",
)

L['ECHO-21'] = dict(
  sub="Cardiology → Echo in ICU → Pleural view",
  step=5,
  intro="Step 5 includes the pleura, because FATE is a heart-and-lung protocol by design (position 4). One real question asks what the sinusoid sign means, and the card layer adds the mirror-image and spine signs.",
  parts=[
    ('a', "**Pleura appreciated in the MID-AXILLARY LINES BILATERALLY.** The probe sits above the diaphragm in the mid-axillary line, with liver or spleen as the landmark; fluid collects posteriorly and at the bases in a supine patient, so this low lateral position finds it."),
    ('b', "**A transudative effusion is ANECHOIC.** Transudates have little protein or cells, so they return no echoes. The reverse does not hold: an anechoic effusion can still be an exudate, whereas complex, septated or diffusely echogenic effusions are exudates."),
    ('c', "**Plankton sign: swirling, punctiform echoes in an effusion; may indicate infection or haemothorax.** The floating echoes are cells, protein and fibrin strands moving with breathing and the heartbeat, so the fluid is cellular (empyema, parapneumonic exudate, blood)."),
  ],
  mimic=[
    ("Effusion vs consolidation", "Effusion: anechoic space with a sinusoid sign and the spine visible above the diaphragm. Consolidation: tissue-like (hepatised) lung, which does not move like fluid."),
    ("Effusion vs pneumothorax on M-mode", "Effusion: sinusoid sign. Pneumothorax: barcode (stratosphere) sign and a lung point."),
  ],
  traps=[
    ("“Sinusoid sign = pneumothorax or consolidation”", "It is pleural effusion: on M-mode the lung line swings towards the pleural line on inspiration, tracing a sine wave; with the quad sign it confirms free fluid."),
    ("“Liver mirrored above the diaphragm means fluid”", "The mirror image needs air-filled lung, so it means NO effusion at that spot; with an effusion the mirror image disappears and the spine becomes visible above the diaphragm (spine sign)."),
  ],
  decode=[
    ("‘Sinusoid sign’ on ultrasound is characteristic of? [DocT GT PYQ]", "Pleural effusion."),
    ("Swirling echoes within a pleural collection suggest? [pattern]", "An exudate: infection (empyema) or haemothorax."),
  ],
  punch="Scan the pleura in both mid-axillary lines: anechoic fluid with a sinusoid sign is free fluid, swirling echoes mean cells or blood, and an anechoic effusion is not proof of a transudate.",
)

L['ECHO-22'] = dict(
  sub="Cardiology → Echo in ICU → Parasternal long axis",
  step=3,
  intro="Step 3 starts with the first chest-wall view. PLAX lies in the long-axis plane, so it shows the LV, mitral valve, LVOT, aortic valve and root in one picture, with the descending aorta behind the LA. Four questions test what it shows, how it separates pericardial from pleural fluid and its role in dissection.",
  parts=[
    ('a', "**Transducer at the LEFT sternal edge, 2nd to 4th ICS.**"),
    ('b', "**Marker dot towards the RIGHT SHOULDER.** This lines the plane up with the LV long axis (ECHO-14, ECHO-16)."),
    ('c', "**Useful for assessing contractility, calculating EF, detecting RWMA and measuring LVOT diameter.** The beam crosses the septum and posterior wall at right angles, so M-mode measures wall thickness, cavity size, fractional shortening and EPSS here (ECHO-39); the anteroseptal and inferolateral walls show regional motion. The LVOT is measured in mid-systole, inner edge to inner edge, just below the aortic valve; because stroke volume = 0.785 × D² × VTI, a 1 mm error in the diameter becomes a large error in stroke volume. The same view shows the aortic root and proximal ascending aorta (dilatation, an intimal flap, AR)."),
  ],
  mimic=[
    ("Pericardial vs pleural effusion on PLAX", "Pericardial fluid lies ANTERIOR to the descending aorta, between the aorta and the LA; pleural fluid lies posterior and lateral to it, because the pericardial reflection stops at the aorta."),
    ("PLAX vs PSAX at aortic valve level", "PLAX shows the LVOT, aortic valve and root lengthways; PSAX AV level shows the valve in cross-section (Mercedes-Benz sign) and the pulmonary artery."),
  ],
  traps=[
    ("“Best TTE view for aortic dissection is PSAX at the aortic valve”", "PLAX is (75% right): it shows the root and proximal ascending aorta lengthways. TTE can still miss a dissection, so CT aortography or TEE confirms."),
    ("“Left 4th space, marker to the right shoulder shows the PA bifurcation or the IVC”", "That is PLAX, which shows the LVOT and aortic valve (75% and 88% right); the PA bifurcation is PSAX at the aortic level, the IVC is subcostal."),
    ("“Fluid anterior to the descending aorta on PLAX is pleural”", "It is pericardial."),
  ],
  decode=[
    ("Left 4th ICS, marker to the right shoulder — which structure is best seen? [DocT QBank, DocT GT]", "LV outflow tract and aortic valve."),
    ("Anechoic fluid anterior to the descending aorta on PLAX? [DocT GT]", "Pericardial effusion."),
    ("Best echo view for aortic dissection and aneurysm? [DocT GT]", "Parasternal long axis."),
  ],
  punch="PLAX lies along the LV and aortic root: it measures the LVOT diameter, shows the root for dissection, and separates fluid by the descending aorta (in front pericardial, behind pleural).",
)

L['ECHO-23'] = dict(
  sub="Cardiology → Echo in ICU → Parasternal short axis",
  step=3,
  intro="Step 3 continues: turn the probe from PLAX and the LV becomes a ring. Two questions ask what this view is best for, and about one in three chose a Doppler measurement instead of wall motion.",
  parts=[
    ('a', "**Rotate the probe CLOCKWISE 90° from PLAX.** The plane turns from along the LV to across it."),
    ('b', "**Transducer at the LEFT sternal edge, 2nd to 4th ICS.** The same spot as PLAX; only the rotation changes."),
    ('c', "**Marker dot towards the LEFT SHOULDER.**"),
    ('d', "**Short-axis views from the aortic valve down to the LV apex.** Tilting the beam from base to apex gives successive slices (breadloafing, ECHO-24). At the mid-papillary level all three coronary territories are seen together: anterior and anteroseptal walls (LAD), inferior and inferoseptal (RCA), inferolateral (circumflex) and anterolateral (circumflex, often shared with the LAD), which is why this view is best for regional wall motion. The ring shape of the LV also shows septal flattening (a D-shaped LV) when the RV is overloaded."),
  ],
  mimic=[
    ("Septal flattening in systole vs in diastole", "Systolic flattening means RV pressure overload (PE, PH); diastolic flattening means RV volume overload."),
  ],
  traps=[
    ("“PSAX is for LVOT gradient, stroke volume or RVSP”", "Those need Doppler with the beam parallel to flow, from apical views (LVOT, TR); PSAX is for regional wall motion (61%, 67% right)."),
  ],
  decode=[
    ("Probe rotated 90° clockwise from PLAX, circular LV — primary advantage? [DocT QBank, DocT GT]", "Evaluating LV regional wall motion."),
    ("D-shaped LV on PSAX in systole — what does it mean? [pattern]", "RV pressure overload (PE, pulmonary hypertension)."),
  ],
  punch="PSAX is PLAX turned 90° clockwise from the same spot, marker to the left shoulder; it shows the LV as a ring, so all coronary territories and the septum’s shape are seen at once.",
)

L['ECHO-24'] = dict(
  sub="Cardiology → Echo in ICU → Breadloafing",
  step=3,
  intro="Still step 3: from the PSAX position the beam is tilted, not moved, to cut the heart in slices from base to apex.",
  parts=[
    ('a', "**Change the angulation on the chest wall.** The probe stays at the same spot and is tilted from pointing at the right shoulder (base) towards the left hip (apex)."),
    ('b', "**Any number of short-axis views can be obtained.** Each degree of tilt gives a new slice."),
    ('c', "**The standard four: aortic valve, mitral valve, LV papillary muscles, LV apex.** AV level shows the three cusps, RVOT and PA (ECHO-26); MV level the ‘fish-mouth’ mitral orifice; papillary level the mid-LV (ECHO-25); the apex the apical segments."),
    ('d', "**Like cutting a loaf of bread into slices.**"),
  ],
  mimic=[
    ("Breadloafing (angulation) vs PSAX from PLAX (rotation)", "Rotation turns the plane from long to short axis; angulation then moves the short-axis slice up and down the heart."),
  ],
  traps=[
    ("“Only four short-axis views exist”", "Any number can be obtained; four are standard."),
  ],
  decode=[
    ("The four standard PSAX levels? [pattern]", "Aortic valve, mitral valve, papillary muscles, apex."),
  ],
  punch="Tilting the probe at the PSAX position slices the heart from aortic valve to apex; four slices are standard, but any number is possible.",
)

L['ECHO-25'] = dict(
  sub="Cardiology → Echo in ICU → PSAX papillary level",
  step=3,
  intro="Step 3’s workhorse slice, the one in the basic FATE set. One question asks its main advantage; the hypovolaemia questions in ECHO-36 are also read here (‘kissing’ papillary muscles).",
  parts=[
    ('a', "**LV end-diastolic area.** A small end-diastolic area with end-systolic cavity obliteration means an underfilled LV (hypovolaemia), though a small, hyperdynamic cavity is also seen with low afterload and with a hypertrophied LV."),
    ('b', "**Contractility.** Wall thickening and inward motion around the whole ring give a global impression of LV function."),
    ('c', "**Detecting RWMA.** All three coronary territories are in one slice (ECHO-23)."),
    ('d', "**Detecting RV enlargement.** The normal RV is a crescent wrapped around the LV; when it dilates it becomes as large as or larger than the LV, and the septum flattens."),
    ('e', "**IVS motion abnormalities.** Paradoxical septal motion follows cardiac surgery and LBBB; septal flattening reflects RV pressure (systolic) or volume (diastolic) overload."),
  ],
  mimic=[
    ("‘Kissing’ papillary muscles from hypovolaemia vs from low SVR", "Both obliterate the cavity in systole; hypovolaemia has a small end-diastolic area and a small IVC, low SVR has a normal end-diastolic size (ECHO-36)."),
  ],
  traps=[
    ("“The main advantage of the circular LV view is measuring the LVOT gradient”", "It is regional wall motion (67% right); gradients need apical Doppler."),
  ],
  decode=[
    ("Circular LV after rotating 90° clockwise from PLAX — primary advantage? [DocT GT]", "Evaluating LV regional wall motion."),
    ("Small LV with end-systolic cavity obliteration at the papillary level? [pattern]", "Hypovolaemia (check the IVC), or low SVR if diastolic size is normal."),
  ],
  punch="The mid-papillary slice gives LV filling, global and regional contraction, RV size and septal shape in one look, which is why it is the PSAX level in basic FATE.",
)

L['ECHO-26'] = dict(
  sub="Cardiology → Echo in ICU → PSAX mitral and aortic levels",
  step=3,
  intro="The basal slices of step 3: at the mitral and aortic levels the valves are seen in cross-section.",
  parts=[
    ('a', "**Mitral valve level: measure the mitral valve AREA, assess regurgitant flow and look for vegetations.** Cut across the leaflet tips, the orifice is seen face-on as a ‘fish mouth’, so its area can be traced directly (planimetry), the reference method in mitral stenosis (severe at ≤1.5 cm²). Colour shows where along the coaptation line a regurgitant jet arises."),
    ('b', "**Aortic valve level: structural abnormalities; the MERCEDES-BENZ sign is seen.** The three closed cusps form a ‘Y’ in diastole; a bicuspid valve shows a single closure line and an oval (‘fish-mouth’) opening in systole. The same slice shows the tricuspid and pulmonary valves, the RVOT, the pulmonary artery and the interatrial septum."),
  ],
  mimic=[
    ("Tricuspid (Mercedes-Benz) vs bicuspid aortic valve", "Three cusps and a Y-shaped closure line vs two cusps and a single closure line."),
  ],
  traps=[
    ("“Mitral valve area is measured in A4C”", "A4C gives inflow Doppler; the area is traced in PSAX at the mitral level (ECHO-33)."),
  ],
  decode=[
    ("View for planimetry of the mitral valve area? [pattern]", "PSAX at the mitral valve level."),
  ],
  punch="At the mitral level the orifice is traced for its area; at the aortic level the Mercedes-Benz sign shows three normal cusps.",
)

L['ECHO-27'] = dict(
  sub="Cardiology → Echo in ICU → Apical 4-chamber",
  step=4,
  intro="Step 4: from the apex the beam runs along the long axis of the heart, parallel to blood moving through the atrioventricular valves. Three versions of one question ask which view grades TR and estimates RVSP; only about half got it in two of them.",
  parts=[
    ('a', "**Transducer at the APEX of the heart.**"),
    ('b', "**Marker dot towards the LEFT shoulder.**"),
    ('c', "**Uses: chamber enlargement; detecting and quantifying regurgitant and stenotic lesions; RV and LV contractility; mitral and tricuspid INFLOW pattern.** All four chambers are side by side, so their relative size is judged directly (the RV is normally under two-thirds of the LV; RV/LV >1.0 is an ESC 2019 sign of RV dysfunction in PE). Mitral and tricuspid flow, including regurgitant jets, runs along the beam, so colour and CW Doppler measure them with little angle error; the TR peak velocity gives RVSP = 4V² + RAP. TAPSE and MAPSE are measured here on M-mode, and LV EF by the biplane method (with A2C). PW Doppler at the mitral leaflet tips gives E, A and deceleration time (ECHO-40)."),
  ],
  mimic=[
    ("A4C vs subcostal IVC for RVSP", "A4C gives the TR velocity (the 4V² part); the subcostal IVC gives the RAP that is added to it."),
  ],
  traps=[
    ("“Subcostal IVC view assesses TR severity and RVSP”", "It gives only the RAP; the TR jet is measured in A4C (58%, 51%, 89% right)."),
    ("“PLAX or A2C for TR”", "In PLAX the TR jet runs across the beam; A2C contains no RV or tricuspid valve."),
  ],
  decode=[
    ("Best view for TR severity and RVSP by Doppler? [DocT QBank, DocT GT ×2]", "Apical four-chamber."),
    ("Where is TAPSE measured? [pattern]", "A4C, M-mode through the lateral tricuspid annulus."),
  ],
  punch="A4C lines the beam up with flow across both AV valves, so it is the view for inflow Doppler, regurgitant jets and the TR velocity behind RVSP, and the view where the four chambers are compared.",
)

L['ECHO-28'] = dict(
  sub="Cardiology → Echo in ICU → Foreshortening",
  step=4,
  intro="Step 4’s commonest error: an apical view that misses the true apex makes the LV look short and gives wrong volumes.",
  parts=[
    ('a', "**The beam does NOT cut through the true apex but transects ABOVE and ANTERIOR to it.** The usual cause is a probe placed one rib space too high or too medial."),
    ('b', "**Geometric DISTORTION of the LV image.** The LV appears shorter, so volumes are underestimated and EF misreported, and apical problems (apical wall motion abnormality, aneurysm, thrombus, Takotsubo) can be missed."),
    ('c', "**Apex looks ‘ROUNDED’ instead of the normal ‘BULLET’ shape.** The fix is to move down and laterally until the LV is longest and the apex tapers."),
  ],
  mimic=[
    ("Rounded apex from foreshortening vs from a real apical aneurysm", "Foreshortening disappears when the probe is moved to the true apex; an aneurysm persists and bulges in systole."),
  ],
  traps=[
    ("“A rounded apex is normal”", "The normal apex is bullet-shaped; rounded means foreshortened."),
  ],
  decode=[
    ("Apical view with a rounded LV apex — what is wrong? [pattern]", "Foreshortening: the beam is above and anterior to the true apex."),
  ],
  punch="If the apex looks round, the beam has missed it: move down and out until the LV is longest and bullet-shaped, or volumes and apical motion will be wrong.",
)

L['ECHO-29'] = dict(
  sub="Cardiology → Echo in ICU → Apical 5-chamber",
  step=4,
  intro="Step 4 again: a small tilt from A4C brings the LVOT and aortic valve into the beam, parallel to systolic flow.",
  parts=[
    ('a', "**Slight ANTERIOR angulation of the transducer, towards the chest wall.** Tilting, not rotating: the plane moves forward onto the LVOT."),
    ('b', "**The fifth ‘chamber’ is the aortic valve and ascending aorta.** It is the outflow tract and root, not a cavity."),
    ('c', "**Assesses LVOT velocities; detects and quantifies aortic regurgitation and stenosis.** PW Doppler just below the valve gives the LVOT VTI, which with the PLAX diameter gives stroke volume (ECHO-33) and, before and after a PLR, fluid responsiveness. CW through the valve gives the aortic stenosis peak velocity and gradient (severe at ≥4 m/s); the AR jet runs back along the beam."),
  ],
  mimic=[
    ("A5C (angulation) vs A2C and A3C (rotation)", "A5C is the only apical view made by tilting."),
  ],
  traps=[
    ("“The fifth chamber is the coronary sinus or LA appendage”", "It is the aortic valve and ascending aorta."),
  ],
  decode=[
    ("View for LVOT VTI and aortic stenosis gradient? [pattern]", "Apical five-chamber (or A3C)."),
  ],
  punch="Tilt forward from A4C and the aortic root appears as a ‘fifth chamber’: this is the view for LVOT velocity, VTI and aortic valve Doppler.",
)

L['ECHO-30'] = dict(
  sub="Cardiology → Echo in ICU → Apical 2-chamber",
  step=4,
  intro="Step 4: rotate at the apex and the RV leaves the picture, leaving the LV and LA alone.",
  parts=[
    ('a', "**Transducer at the APEX of the heart.**"),
    ('b', "**Marker dot towards the LEFT SIDE OF THE NECK.**"),
    ('c', "**Rotate the probe 90° from the apical 4-chamber.** Most texts describe about 60–90° counter-clockwise. Rotating on the apex gives the apical long-axis and two-chamber views, which show different LV segments."),
    ('d', "**Focus on the LV WITHOUT ANY RV IMAGE.** A2C shows the anterior and inferior LV walls, which A4C does not, so A4C plus A2C give the biplane (Simpson’s) EF and full regional assessment."),
  ],
  mimic=[
    ("A4C vs A2C", "A4C: septum and lateral wall, with the RV. A2C: anterior and inferior walls, no RV."),
  ],
  traps=[
    ("“A2C can assess the RV or TR”", "There is no RV in the image."),
  ],
  decode=[
    ("Apical view that shows the LV and LA without the RV? [pattern]", "Apical two-chamber."),
  ],
  punch="A2C is A4C rotated so the marker points at the neck: the RV disappears, and the anterior and inferior walls appear for biplane EF.",
)

L['ECHO-31'] = dict(
  sub="Cardiology → Echo in ICU → Apical 3-chamber",
  step=4,
  intro="Step 4: the apical long axis is the PLAX plane seen from the apex, so the LVOT now runs along the beam.",
  parts=[
    ('a', "**Transducer at the APEX of the heart.**"),
    ('b', "**Transducer turned CLOCKWISE by 60° from the A2C view.** This is the card’s wording. Standard texts rotate a further ~60° COUNTER-clockwise from A2C (about 120° from A4C), bringing the marker towards the right shoulder, the same plane as PLAX (see FLAGS)."),
    ('c', "**Mitral AND aortic valves in the SAME PLANE.** Because it lies in the long-axis plane (ECHO-14), the LVOT, aortic valve and mitral valve appear together, with the anteroseptal and inferolateral walls."),
    ('d', "**Measure LVOT velocities.** The outflow tract runs along the beam, so PW and CW Doppler measure LVOT VTI, aortic stenosis velocity and dynamic LVOT obstruction (systolic anterior motion) with little angle error."),
  ],
  mimic=[
    ("A3C vs PLAX", "Same plane; PLAX measures the LVOT DIAMETER (beam perpendicular), A3C its VELOCITY (beam parallel)."),
  ],
  traps=[
    ("“A3C is obtained by tilting from A4C”", "Tilting gives A5C; A3C is reached by rotation, taken from A2C on the card."),
  ],
  decode=[
    ("Apical view with mitral and aortic valves in the same plane? [pattern]", "Apical 3-chamber (apical long axis)."),
  ],
  punch="A3C is the long-axis plane seen from the apex: both left-sided valves in one picture and the LVOT lined up for Doppler.",
)

L['ECHO-32'] = dict(
  sub="Cardiology → Echo in ICU → Rotations compared",
  step=4,
  intro="Step 4 summarised: each derived view comes from a reference view by a rotation or a tilt.",
  parts=[
    ('a', "**PSAX: rotate clockwise, from PLAX, 90°.** Marker from right to left shoulder."),
    ('b', "**A5C: angulate anteriorly, from A4C, no angle.** The only tilt."),
    ('c', "**A2C: rotate, from A4C, 90°.** Usually counter-clockwise, about 60–90°."),
    ('d', "**A3C: rotate clockwise, from A2C, 60°.** Card wording; standard texts rotate further counter-clockwise from A2C (see FLAGS on ECHO-31)."),
  ],
  table=dict(title="As usually taught", head=["View", "From", "Manoeuvre"], rows=[["PSAX", "PLAX", "rotate 90° clockwise"], ["A5C", "A4C", "tilt anteriorly"], ["A2C", "A4C", "rotate ~60–90° counter-clockwise"], ["A3C", "A2C", "rotate a further ~60° counter-clockwise (marker to right shoulder)"]]),
  mimic=[
    ("Rotation vs angulation", "Rotation turns the plane around the beam axis; angulation tilts the beam to a different part of the heart in the same orientation."),
  ],
  traps=[
    ("“A5C is a rotation from A4C”", "It is the only angulation."),
  ],
  decode=[
    ("Manoeuvre to go from PLAX to PSAX? [pattern]", "Rotate 90° clockwise."),
  ],
  punch="Three rotations and one tilt: PLAX → PSAX 90° clockwise, A4C → A5C tilt forward, A4C → A2C and then A2C → A3C by rotation.",
)

L['ECHO-33'] = dict(
  sub="Cardiology → Echo in ICU → Which view measures what",
  step=4,
  intro="Step 4’s rule in one table: diameters come from views where the beam is perpendicular to the structure, velocities from views where it is parallel to the flow.",
  parts=[
    ('a', "**LVOT diameter: PLAX.** Axial resolution is best when the beam strikes the walls at right angles."),
    ('b', "**LVOT velocities: A5C and A3C.** Doppler underestimates velocity by the cosine of the angle; under 20° the error is small. Stroke volume = 0.785 × D² (PLAX) × LVOT VTI (apical)."),
    ('c', "**Mitral valve area: PSAX, mitral valve level.** The orifice is seen face-on for planimetry."),
    ('d', "**Mitral and tricuspid inflow pattern: A4C.** Inflow runs along the beam."),
  ],
  mimic=[
    ("Diameter vs velocity", "Perpendicular beam (PLAX) vs parallel beam (apical)."),
  ],
  traps=[
    ("“LVOT velocity is measured in PLAX”", "In PLAX the flow runs across the beam; Doppler there reads near zero."),
  ],
  decode=[
    ("Views needed to calculate stroke volume by echo? [pattern]", "PLAX for LVOT diameter, A5C or A3C for LVOT VTI."),
  ],
  punch="Measure size where the beam is perpendicular and velocity where it is parallel; that is why stroke volume needs two views.",
)

L['ECHO-34'] = dict(
  sub="Cardiology → Echo in ICU → Basic FATE views",
  step=5,
  intro="Step 5: FATE (focus-assessed transthoracic echo, Jensen 2004) is a short protocol for the anaesthetist and intensivist, built from the views most likely to be obtainable.",
  parts=[
    ('a', "**1 Subcostal 4-chamber, 2 Apical 4-chamber, 3 PLAX, 4 PSAX at papillary level, 5 Pleural scanning.** On the FATE card these are positions 1 to 4, with PLAX and PSAX together as position 3 and pleural scanning as position 4; the card says to scan in the most favourable sequence. Subcostal comes first because it works supine; pleural scanning is in the basic set because effusions are a common cause of breathlessness and low output."),
  ],
  mimic=[
    ("FATE vs RUSH", "FATE is a structured cardiac and pleural exam; RUSH adds the IVC, abdomen, aorta and leg veins to find the type of shock."),
  ],
  traps=[
    ("“Pleural scanning is an extended view”", "It is basic."),
  ],
  decode=[
    ("Which PSAX level is in the basic FATE set? [pattern]", "Papillary muscle level."),
  ],
  punch="Basic FATE is subcostal, apical, parasternal long and short (papillary) and the pleura: a heart-and-lung exam from the start.",
)

L['ECHO-35'] = dict(
  sub="Cardiology → Echo in ICU → Extended FATE views",
  step=5,
  intro="Step 5 continues: when the basic scan raises a question, the extended views answer it.",
  parts=[
    ('a', "**1 Subcostal IVC, 2 A2C, 3 A3C, 4 A5C, 5 PSAX at mitral valve level.** These add filling (IVC), the LV segments missing from A4C (A2C, A3C), outflow Doppler (A5C, A3C) and the mitral valve (PSAX). The FATE card itself lists PSAX at both the mitral AND aortic levels among the extended views (see FLAGS)."),
  ],
  mimic=[
    ("Subcostal 4-chamber vs subcostal IVC", "Same window: the 4-chamber view is basic, the IVC view is extended."),
  ],
  traps=[
    ("“The IVC view is basic because subcostal is basic”", "Subcostal 4-chamber is basic; the IVC view is extended."),
  ],
  decode=[
    ("Which PSAX level is in the extended FATE set? [pattern]", "Mitral valve level (the card also lists the aortic level)."),
  ],
  punch="Extended FATE adds the IVC, the other apical views and the basal PSAX: filling, all LV segments and Doppler.",
)

L['ECHO-36'] = dict(
  sub="Cardiology → Echo in ICU → Goals of FATE",
  step=5,
  intro="Step 5’s core: what the FATE scan is for. Four questions test how its findings are read; one of them, a hyperdynamic LV with normal volume status, was got right by only 38%.",
  parts=[
    ('a', "**Goal 1: exclude obvious pathology: pleural and pericardial effusions, valvular disease, aortic dissection, pulmonary embolism.** These are the causes of instability that change management at once. In PLAX, fluid anterior to the descending aorta is pericardial and fluid behind it is pleural (ECHO-22)."),
    ('b', "**Goal 2: assess wall thickness and chamber dimensions: hypertrophy, relative LV/RV size, chamber enlargement.** A small LV with cavity obliteration suggests hypovolaemia; a dilated, thin-walled LV is chronic cardiomyopathy; a dilated RV with septal flattening points to PE or RV failure."),
    ('c', "**Goal 3: assess contractility qualitatively: hyperdynamic, normal, mild, moderate or severe dysfunction.** Eyeballing in all views is quick and, in trained hands, agrees well with measured EF. A hyperdynamic LV means a small end-systolic volume: if the end-diastolic size is small too, the patient is hypovolaemic; if it is normal, afterload is low (sepsis, anaemia, liver failure, thyrotoxicosis)."),
    ('d', "**Goal 4: image the pleura bilaterally: a transudative effusion is ANECHOIC; the ‘plankton sign’ suggests infection or haemothorax.** A free-flowing effusion moves with a sinusoid sign on M-mode (ECHO-21)."),
  ],
  mimic=[
    ("Hyperdynamic LV: hypovolaemia vs low SVR", "Hypovolaemia: small end-diastolic LV and a small, collapsing IVC. Low SVR: normal end-diastolic size and normal IVC, with an empty-looking LV only in systole."),
    ("Hypovolaemic vs cardiogenic vs obstructive oliguria", "Small hyperdynamic LV with cavity obliteration vs dilated poorly contracting LV vs dilated RV with septal flattening."),
  ],
  traps=[
    ("“Hyperdynamic LV with normal volume status = hypovolaemic shock”", "Only 38% got this: the stem says volume status is normal, so the LV is not underfilled; it empties because the afterload is low (key A, low SVR). Raised pulmonary resistance gives a dilated RV, not a hyperdynamic LV."),
    ("“Anechoic dependent fluid with a sinusoid sign proves a transudate”", "The key (simple transudative effusion, 61% right) is the best option, but it over-reads: the sinusoid sign proves free-flowing, low-viscosity fluid, and an anechoic effusion can be an exudate. Empyema and organised haemothorax damp the swing."),
    ("“Fluid anterior to the descending aorta on PLAX is pleural”", "It is pericardial; the pericardial reflection stops at the aorta."),
  ],
  decode=[
    ("Acute dyspnoea, hyperdynamic LV, normal volume status — haemodynamic state? [DocT QBank]", "Low systemic vascular resistance."),
    ("Post-hypotension oliguria — echo finding of a prerenal, hypovolaemic cause? [DocT GT PYQ]", "Hyperdynamic LV with near-complete cavity obliteration in systole."),
    ("Dependent anechoic pleural fluid moving sinusoidally — indicates? [DocT QBank]", "Free-flowing simple effusion (keyed transudate)."),
    ("Anechoic fluid anterior to the descending aorta on PLAX? [DocT GT]", "Pericardial effusion."),
  ],
  punch="FATE asks four things in order: is there an obvious lesion, are the chambers the right size and thickness, how well do they contract, and is there pleural fluid. A hyperdynamic LV is hypovolaemia only if it is also small in diastole.",
)

L['ECHO-37'] = dict(
  sub="Cardiology → Echo in ICU → LV dimensions",
  step=6,
  intro="Step 6 begins the numbers. These are the FATE-style textbook values measured on PLAX M-mode; ASE 2015 now gives sex-specific ranges, which differ at the upper ends.",
  parts=[
    ('a', "**Internal diameter: end-systolic 2.0–4.0 cm, end-diastolic 3.5–5.6 cm.** ASE 2015 gives LVIDd 4.2–5.8 cm in men and 3.8–5.2 cm in women; LV size is now better described by indexed volumes."),
    ('b', "**Diastolic wall thickness, septum and posterior wall: 0.6–1.2 cm.** ASE 2015: 0.6–1.0 cm in men and 0.6–0.9 cm in women; mildly abnormal (LVH) is 1.1–1.3 cm in men and 1.0–1.2 cm in women. The FATE card itself gives 6–10 mm."),
    ('c', "**Systolic wall thickness, septum and posterior wall: 0.9–1.8 cm.** The wall thickens as it contracts; failure to thicken marks a regional abnormality."),
    ('d', "**Fractional shortening 30–45%; ejection fraction 50–85%.** FS = (LVIDd − LVIDs) ÷ LVIDd, and EF is roughly twice FS. ASE 2015 normal LVEF is 52–72% in men and 54–74% in women; FS is valid only when the LV contracts evenly, because it samples one line."),
  ],
  mimic=[
    ("Diastolic vs systolic wall thickness", "0.6–1.2 cm vs 0.9–1.8 cm, identical for septum and posterior wall."),
  ],
  traps=[
    ("“A septum of 1.2 cm is normal”", "It is at the card’s upper limit but mildly thickened by ASE 2015 standards."),
  ],
  decode=[
    ("Normal LV end-diastolic diameter? [pattern]", "Card 3.5–5.6 cm; ASE 2015 4.2–5.8 (men), 3.8–5.2 (women)."),
  ],
  punch="Card values: LVIDs 2–4, LVIDd 3.5–5.6, walls 0.6–1.2 in diastole and 0.9–1.8 in systole, FS 30–45%, EF 50–85%; current ASE ranges are sex-specific and tighter.",
)

L['ECHO-38'] = dict(
  sub="Cardiology → Echo in ICU → Other chamber dimensions",
  step=6,
  intro="Step 6 continues with the other linear sizes, again older M-mode values that ASE 2015 has largely replaced.",
  parts=[
    ('a', "**Left atrium: 2.0–4.0 cm.** A single antero-posterior diameter underestimates LA enlargement because the atrium grows mostly downwards and sideways; ASE 2015 uses the LA volume index (normal ≤34 mL/m²), which is also a marker of chronic raised filling pressure."),
    ('b', "**Aortic root: 2.0–4.0 cm.** ASE 2015 mean at the sinuses is about 3.4 cm in men and 3.0 cm in women, best judged against body size and age."),
    ('c', "**Right ventricle (systolic–diastolic): 0.7–2.3 cm.** This is the old M-mode RV dimension in PLAX. ASE 2015 (and the 2025 right heart guideline) measures the RV in an RV-focused A4C: basal diameter >4.1 cm or mid >3.5 cm is dilated."),
  ],
  mimic=[
    ("LA diameter vs LA volume index", "Diameter is quick but insensitive; volume index is the current standard."),
  ],
  traps=[
    ("“A normal LA diameter excludes LA enlargement”", "The LA can enlarge in other directions; check the volume."),
  ],
  decode=[
    ("Normal LA and aortic root diameters? [pattern]", "2.0–4.0 cm each (card)."),
  ],
  punch="LA, aortic root and LV end-systolic diameter all share 2.0–4.0 cm on the card, and RV 0.7–2.3 cm; current practice uses LA volume and RV-focused apical diameters.",
)

L['ECHO-39'] = dict(
  sub="Cardiology → Echo in ICU → Systolic function grading",
  step=6,
  intro="Step 6’s grading table, from the FATE card, turns function into bands. The NEET 2024 recall asks where EPSS (the card’s MSS) is measured; the TR questions return to A4C, where TAPSE comes from.",
  parts=[
    ('a', "**EF: normal ≥55%, mild 45–54, moderate 30–44, severe <30.** ASE 2015 grades slightly differently: normal 52–72% (men) and 54–74% (women), mildly abnormal 41–51 (men) / 41–53 (women), moderate 30–40, severe <30."),
    ('b', "**FS: normal ≥25%, mild 20–24, moderate 15–19, severe <15.** EF is roughly twice FS."),
    ('c', "**MSS (mitral–septal separation, EPSS): normal <10 mm, mild 7–12, moderate 13–24, severe >24.** In PLAX on M-mode, the anterior mitral leaflet’s early opening (E point) normally nearly touches the septum because a large stroke volume passes through a normal-sized LV. In a dilated, poorly contracting LV the leaflet opens less and the septum is further away. EPSS >7 mm is usually taken as reduced EF. It is unreliable when the anterior leaflet cannot open fully for another reason (mitral stenosis, or an AR jet striking the leaflet), which raises it falsely, and with asymmetric septal hypertrophy or a septal wall-motion abnormality."),
    ('d', "**MAPSE: normal ≥11 mm, mild 9–10, moderate 6–8, severe <6.** Longitudinal fibres move the mitral annulus towards the apex in systole; the distance is measured on M-mode in A4C."),
    ('e', "**TAPSE: normal ≥17 mm, mild 11–16, moderate 6–10, severe <6.** The RV contracts mostly longitudinally, so tricuspid annular motion in A4C reflects RV function; ASE 2015 takes <17 mm as dysfunction (mean about 24 mm), and the ASE 2025 right heart guideline grades it as mild 13–17, moderate 10–13 and severe ≤10 mm. ESC 2019 uses TAPSE <16 mm among the echo signs of RV dysfunction in PE, and TAPSE/sPAP <0.55 mm/mmHg supports PH (ESC/ERS 2022). TAPSE is angle-dependent and load-dependent, and falls after cardiac surgery even when RV function is preserved."),
  ],
  mimic=[
    ("MSS vs the other indices", "MSS runs the other way: high is bad."),
    ("MAPSE vs TAPSE", "Same severe cut-off (<6 mm), different normals (≥11 vs ≥17)."),
  ],
  traps=[
    ("“EPSS is measured in A4C”", "It is measured on PLAX M-mode (NEET 2024)."),
    ("“TAPSE comes from PLAX”", "EF, FS and MSS come from PLAX (FATE position 3); MAPSE and TAPSE come from A4C (position 2)."),
  ],
  decode=[
    ("Best view to measure EPSS? [NEET 2024]", "Parasternal long axis; EPSS >7 mm suggests low EF."),
    ("TAPSE cut-off for RV systolic dysfunction? [pattern]", "<17 mm (ASE 2015); <16 mm in ESC 2019 PE."),
  ],
  punch="EF, FS and EPSS come from PLAX, MAPSE and TAPSE from A4C; EPSS rises as function falls, and TAPSE under 17 mm marks a failing RV.",
)

L['ECHO-40'] = dict(
  sub="Cardiology → Echo in ICU → Normal Doppler values",
  step=6,
  intro="Step 6 ends with the Doppler numbers and the one equation of the chapter. Five questions link here: three on where the TR jet is measured, one RVSP calculation (33% right) and one asking the name of the equation (48% right).",
  parts=[
    ('a', "**CW: peak pressure gradient = 4V²; normal AO <2 m/s, PA <1 m/s, TI <2.5 m/s.** The simplified Bernoulli equation: when blood accelerates through a narrow orifice, pressure energy becomes kinetic energy, and with blood’s density and unit conversions the gradient in mmHg is about 4 × V² (m/s). It ignores the velocity before the orifice, which is safe when that is under about 1 m/s. Applied to TR: RVSP = 4V² + RAP. Aortic velocity rises with stenosis (severe ≥4 m/s); ESC/ERS 2022 treats a TR velocity >2.8 m/s as raising the probability of pulmonary hypertension."),
    ('b', "**PW: mitral inflow deceleration time 140–240 ms; max E <1.2 m/s; E/A >1 (age dependent).** PW at the mitral leaflet tips in A4C. E is early passive filling, driven by the LA–LV pressure difference and LV relaxation; A is atrial contraction. With age and impaired relaxation E falls, A rises and DT lengthens (E/A <1); when LA pressure is high E rises again and DT shortens (restrictive filling, E/A ≥2). Because a normal and a high-pressure pattern can look alike (pseudonormal), E/A is read with e′ and E/e′."),
    ('c', "**TVI: E/e′ <8–10; IVC <20 mm; 50% inspiratory collapse is normal.** TVI here is tissue velocity imaging (tissue Doppler), not velocity–time integral. e′ is the speed of early diastolic mitral annular motion, a measure of relaxation that is fairly independent of load, so E/e′ tracks LA pressure. Current cut-offs: average E/e′ >14 indicates raised filling pressure (ASE/EACVI 2016, kept in the ASE 2025 update, which also uses TR ≥2.8 m/s, LA volume index >34 mL/m² and LA reservoir strain ≤18%). The IVC figure (<20 mm) is the FATE card’s; the ASE RAP table uses 2.1 cm (ECHO-19)."),
  ],
  mimic=[
    ("Bernoulli vs Laplace vs Poiseuille", "Bernoulli converts velocity to a pressure gradient; Laplace relates wall tension to pressure and radius; Poiseuille relates laminar flow to pressure, radius and viscosity."),
    ("Mitral E/e′ vs tricuspid E/e′", "Mitral <8 normal and >14 raised LA pressure; tricuspid >6 suggests raised RA pressure (ECHO-19)."),
  ],
  traps=[
    ("“RVSP = 4 × 3.5² = 49 mmHg”", "That is the RV–RA gradient; add the RAP: 49 + 10 ≈ 60 mmHg (33% right)."),
    ("“The pressure gradient between two chambers is calculated by Laplace’s law”", "It is Bernoulli’s (48% right); Laplace is wall tension, and the ‘Dubois’ formula is body surface area."),
    ("“Subcostal IVC or PLAX for TR and RVSP”", "The TR jet is measured in A4C, parallel to the beam (ECHO-27)."),
  ],
  decode=[
    ("Equation for the pressure gradient between two chambers? [DocT GT]", "Bernoulli: ΔP = 4V²."),
    ("TR 3.5 m/s, RAP 10 mmHg — RVSP? [DocT QBank]", "≈60 mmHg."),
    ("Best view for TR severity and RVSP? [DocT QBank, DocT GT ×2]", "Apical four-chamber."),
  ],
  punch="Every CW velocity becomes a pressure by 4V², and adding the RAP to the TR gradient gives RVSP. Mitral E and A describe filling, and E/e′ (tissue Doppler) says whether the LA pressure is high.",
)

FLAGS = {
  'ECHO-31': "b: ‘turned CLOCKWISE by 60° from A2C’ — standard texts (123sonography, LITFL) rotate a further ~60° COUNTER-clockwise from A2C (≈120° from A4C), marker to the right shoulder. Direction probably wrong; the explanation gives both.",
  'ECHO-32': "d: same issue as ECHO-31 (A3C ‘rotate clockwise’ from A2C). Also c: A2C is usually taught as ~60° (60–90°) counter-clockwise from A4C; the card gives 90° without direction — acceptable.",
  'ECHO-35': "The FATE card lists PSAX at both the mitral AND aortic levels among the extended views; the card gives only the mitral level (five items). Incomplete rather than wrong.",
  'ECHO-37': "Older textbook values. ASE 2015 normal LVIDd 4.2–5.8 (men) / 3.8–5.2 cm (women); IVS and posterior wall 0.6–1.0 / 0.6–0.9 cm (1.1–1.2 is mildly abnormal); LVEF 52–72 / 54–74% (card 50–85%). Fine as the source’s values; the explanation gives ASE 2015.",
  'ECHO-38': "Outdated measures. ASE 2015 uses LA volume index ≤34 mL/m² (not a 2–4 cm diameter); RV dilated if basal >4.1 cm or mid >3.5 cm (RV-focused A4C), not the old 0.7–2.3 cm M-mode dimension; aortic sinus about 3.4 (men) / 3.0 cm (women).",
  'ECHO-39': "a: FATE EF bands (≥55 / 45–54 / 30–44 / <30) differ from ASE 2015 (normal 52–72 men, 54–74 women; mildly abnormal 41–51 / 41–53; moderate 30–40; severe <30). Correct for FATE; the explanation states ASE. The FATE card’s own TAPSE row is 16–20 / 11–15; the deck card uses the ASE ≥17 normal, as its watch line says.",
  'ECHO-40': "c: ‘TVI’ here means tissue velocity imaging (tissue Doppler), not velocity–time integral; worth saying on the card, since VTI is used elsewhere in the deck. E/e′ <8–10 is the FATE normal; current raised-pressure cut-off is average E/e′ >14 (ASE/EACVI 2016, ASE 2025). The IVC <20 mm differs from the ASE 2.1 cm (ECHO-19).",
  'ECHO-19': "c: the card lists RV hypertrophy among the secondary indices of raised RAP and pins them to the high band. ASE 2010 and the 2025 right heart guideline that replaced it list RA enlargement, interatrial septum bulging into the LA, restrictive right-sided filling, tricuspid E/e′ >6 and hepatic vein systolic filling fraction <55% (S/D <1); RVH is not one, and the indices are used mainly to move the intermediate band to 3 or 15. ASE 2025 also adds IVC >2.5 cm without variation ≈ 20 mmHg.",
  'ECHO-21': "b (and ECHO-36 d): ‘transudative effusion is ANECHOIC’ is true, but the reverse is not: an anechoic effusion may be an exudate (Yang 1992). The DocT QBank key ‘simple transudative effusion’ for a sinusoid sign over-reads; the traps say so.",
}
