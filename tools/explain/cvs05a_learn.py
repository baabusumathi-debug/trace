# CVS05A — Explain v3 ("Learn" depth): echocardiography in the ICU, part 1 — why bedside echo, the TTE probe and frequency, B-mode and M-mode, the Doppler effect and the angle
# of insonation, pulse wave, continuous wave, colour flow and tissue Doppler, the no-signal zone, PWD vs CWD, and setting up the machine.
# No mnemonics or hooks. Driven by qpack/CVS05A.md (5 question links: ECHO-02 probe choice asked twice in the DocT QBank (59%, 60%); ECHO-07 and ECHO-12 share one DocT QBank
# question (PWD for femoral flow, 57%); ECHO-05 one DocT GT question on acoustic impedance). ECHO-01, 03, 04, 06, 08, 09, 10, 11 and 13 have no linked question and get short
# explanations with [pattern] decode items. One Top-up card (probe manoeuvres) in cvs_topups.json: written in cvs05a_topups_learn.py.
# cvs_cardlayer.json `lines` read and used (ECHO-02 probe-to-window line; ECHO-05 acoustic impedance line). No `fix` entries for CVS05A in trace/test/data/qbank.json (checked 19 Nov 2026).
# Checked online on 19 Nov 2026:
#  - The 59% / 43% figures: Spencer KT et al., JACC 2001;37:2013–18 (scholars.uthscsa.edu abstract): 36 patients; four cardiologists’ physical examination missed 59% of overall and 43% of
#    major cardiovascular findings; the same physicians with a miniaturised echo missed 29% and 21%; full echo as the gold standard. Not an ICU study.
#  - PW Doppler (123sonography e-book 1.8.1.1): one element emits and receives; timing of the returning echo fixes the depth (sample volume, site specific); Nyquist limit = half the pulse
#    repetition frequency; velocities above it alias; PW cannot depict velocities above about 1.5–1.7 m/s; maximum PRF and so the Nyquist limit fall with depth.
#  - Physics (NYSORA POCUS physics page): acoustic impedance Z = ρc, the difficulty for sound to travel through a medium; soft-tissue speed 1540 m/s (1400–1640); attenuation coefficient rises
#    with frequency, so depth of imaging falls as frequency rises; strong reflectors hyperechoic (white), weak reflectors hypoechoic.
#  - ASE/EACVI 2015 chamber quantification (ASE summary document, asecho.org): biplane method of disks is the preferred 2D method for EF; volumes from linear measurements should not be used
#    for EF; FS from M-mode or linear 2D; S′ and TAPSE are angle dependent and reflect longitudinal (basal) RV function. Cut-offs TAPSE <17 mm, S′ <9.5 cm/s as checked for CVS05B the same day.
#  - ASE 2025 diastolic update (via the CVS05B check, 19 Nov 2026): reduced e′ septal ≤6, lateral ≤7 cm/s (ASE/EACVI 2016 had <7 and <10).
#  - Review check 19 Nov 2026: ASE Doppler quantification recommendations (Quiñones 2002, asecho.org PDF): beam as parallel as possible; deviations <20° give <10% velocity error; angle correction not recommended;
#    Nyquist limit = PRF/2; PRF set by sample-volume depth. Melamed 2009 (Chest, hand-held LV function by intensivists): 92% normal, 80% abnormal correct, kappa 0.72. ASE/EACVI 2015 summary: FS use discouraged.
# From standard references without a fresh check (confident unless said): Doppler equation Δf = 2·f₀·v·cosθ / c; error = 1 − cosθ (10° 1.5%, 20° 6%, 30° 13%, 45° 29%, 60° 50%); CW measures velocities of several m/s
# (AS, MR, TR) without aliasing; colour Doppler is multigated PW with its own Nyquist limit shown on the colour bar; tissue Doppler filters for low-velocity, high-amplitude signals;
# probe ranges (phased 1–5, curvilinear 2–5, linear 5–15 MHz).
# Could not verify: the source of the 77–93% intensivist–cardiologist agreement range (several small studies report agreement in this band; no single paper found).

SPINE = [
  ("Why echo at the bedside", "Physical examination misses much of what echo shows, and intensivists with focused training agree well with cardiologists, so echo is part of the ICU examination."),
  ("Probe, frequency and depth", "Lower frequency penetrates deeper but resolves less, so the deep heart, seen between the ribs, needs a low-frequency phased array probe and superficial structures a high-frequency linear one."),
  ("Grey-scale pictures: B and M", "B-mode turns echo strength into shades of grey to draw structure, and M-mode plots one line of it against time to time and measure fast movement."),
  ("Doppler shift and the angle", "Moving red cells change the returning frequency in proportion to velocity times the cosine of the beam angle, so the beam must run parallel to flow and flow at 90° shows nothing."),
  ("Choosing the Doppler mode", "Pulse wave Doppler tells where but not how fast, continuous wave tells how fast but not where, colour is pulse wave painted on the picture, and tissue Doppler reads the slow wall."),
  ("Getting a usable image", "Position, gain, depth, baseline and scale decide whether the picture and the trace can be read at all."),
]

PRIMER = "Ultrasound is sound above human hearing, sent into the body by a probe in pulses; the probe listens for the echoes, and the time each takes to return gives its depth, because sound travels at about 1540 m/s in soft tissue. Echoes arise wherever two tissues differ in acoustic impedance (density × speed of sound); air and bone reflect almost everything, which is why gel is needed and lung blocks the view. Higher frequency means a shorter wavelength and sharper detail but more energy lost per centimetre, so less depth. Doppler is a separate use of the same echoes: it reads the change in frequency caused by moving blood, not the strength of the echo."

L = {}

L['ECHO-01'] = dict(
  sub="Cardiology → Echo in ICU → Why bedside echo",
  step=1,
  intro="Step 1 is the case for echo at all. The numbers on this card come from a study in which cardiologists examined patients and then scanned them, and they show how much the stethoscope misses.",
  parts=[
    ('a', "**Cardiac examination failed to detect 59% of overall cardiovascular findings.** In Spencer and colleagues’ study (JACC 2001; 36 patients, full echo as the gold standard), cardiologists’ physical examination missed 59% of findings; the same physicians with a small portable echo missed 29%. Murmurs, effusions and wall-motion defects are often silent at the bedside, more so in a ventilated, oedematous ICU patient."),
    ('b', "**43% of MAJOR cardiovascular findings were missed.** The major-finding miss rate is lower than the overall rate because big abnormalities are more likely to make a sign; portable echo halved it to 21%."),
    ('c', "**Intensivists achieve 77–93% agreement with cardiologists.** This is the source’s range; no single paper reporting it could be traced. Small studies of intensivists after focused training report agreement of this order for simple questions (in Melamed and colleagues’ 2009 hand-held study, 92% of normal and 80% of abnormal LV function correctly called against formal echo), which is why a yes-or-no answer on gross LV function or effusion can be acted on without waiting for a formal study."),
  ],
  mimic=[
    ("Overall vs major miss rate", "Overall 59%, major 43%: the larger figure belongs to the broader category."),
  ],
  traps=[
    ("“59% of major findings were missed”", "59% is the overall figure; major findings were missed 43% of the time."),
  ],
  decode=[
    ("[pattern] What proportion of cardiovascular findings does clinical examination miss compared with echo?", "59% overall, 43% of major findings."),
  ],
  punch="Examination missed 59% of all findings and 43% of the major ones; trained intensivists agree with cardiologists 77–93% of the time, so focused echo belongs in the ICU examination.",
)

L['ECHO-02'] = dict(
  sub="Cardiology → Echo in ICU → The TTE probe and frequency",
  step=2,
  intro="Step 2 is the trade-off behind every probe choice: frequency against depth. The two DocT QBank questions are not about the heart at all; they test whether the rule can be applied to the pleura and the abdomen, and only about 60% got them right.",
  parts=[
    ('a', "**Phased array probe.** Its small footprint fits between the ribs, and the beam is steered electronically from one point to fan out into a sector, so a wide image is made through a narrow window. The price is a narrow near field: structures just under the skin are poorly seen."),
    ('b', "**Typical frequency range 1–5 MHz.** Cardiac views need an imaging depth of about 15–20 cm (the apical view reaches the atria), and only low frequencies reach that depth with enough echo left to image."),
    ('c', "**A smaller frequency allows better delineation of DEEPER structures.** Attenuation, the energy lost as the beam travels, rises with frequency; a low-frequency beam loses less per centimetre and so returns usable echoes from depth. The cost is resolution, because a longer wavelength cannot separate two points close together."),
    ('d', "**The orientation marker delineates the left or right side of the image.** The ridge or dot on the probe matches a marker on the screen, so the operator knows which side of the picture corresponds to which side of the probe; every standard view is defined by where the marker points (CVS05B)."),
  ],
  table=dict(
    head=["Probe", "Frequency", "Use"],
    rows=[
      ["Phased array", "1–5 MHz", "Heart between the ribs, transcranial Doppler"],
      ["Curvilinear", "2–5 MHz", "Pleural effusion and consolidation, abdomen, FAST (deep, wide field)"],
      ["Linear", "5–15 MHz", "Pleural line and sliding, vessels and access, ONSD, cricothyroid membrane (sharp, ≤6 cm)"],
    ],
  ),
  mimic=[
    ("Phased array vs curvilinear", "Both are low frequency; the curvilinear has a wide footprint and near field (pleura, abdomen), the phased array a small footprint for rib spaces (heart)."),
    ("Curvilinear vs linear for the pleura", "Fluid and consolidation are deep: curvilinear. The pleural line and lung sliding are superficial: linear."),
  ],
  traps=[
    ("“Phased array (2 MHz) is best for a pleural effusion” — the main wrong choice when 59% were right", "It reaches the depth but has a narrow near field and sector; the curvilinear 4–5 MHz probe gives the wide, deep view of the costophrenic angle. The phased array is the second choice, used when the rib spaces are tight."),
    ("“Linear 10 MHz for the pleural cavity”", "Excellent for the pleural line but it cannot see more than about 6 cm, so a moderate effusion and the lung beneath it are out of reach."),
    ("“5–10 MHz for a deep abdominal abscess” (60% right)", "Higher frequency loses too much energy with depth; deep abdominal work needs 2–5 MHz."),
  ],
  decode=[
    ("Ventilated patient, pleural effusion on POCUS — best probe? [DocT QBank]", "Curvilinear 4–5 MHz (59% right)."),
    ("Deep abdominal abscess — which frequency range gives optimal penetration? [DocT QBank]", "2–5 MHz (60% right)."),
    ("[pattern] Why does the cardiac probe use 1–5 MHz?", "The heart is deep; low frequency attenuates less, at the cost of resolution."),
  ],
  punch="Frequency buys resolution and costs depth: deep targets get low-frequency probes (phased array between ribs, curvilinear for pleura and abdomen), shallow ones the high-frequency linear.",
)

L['ECHO-03'] = dict(
  sub="Cardiology → Echo in ICU → 2D (B-mode)",
  step=3,
  intro="Step 3 turns echoes into a picture. B stands for brightness: each echo is drawn as a dot whose brightness follows its strength, placed at the depth its return time gives.",
  parts=[
    ('a', "**A 2-dimensional cross-sectional view.** Many scan lines side by side build a slice through the heart, refreshed many times a second so that it moves."),
    ('b', "**High reflectivity appears white.** A large impedance mismatch (pericardium, valve rings, calcium, bone) reflects most of the beam: hyperechoic."),
    ('c', "**Low reflectivity (muscle) appears grey.** Myocardium scatters a moderate amount of sound: hypoechoic relative to the pericardium."),
    ('d', "**No reflection (fluid) appears black.** Blood and effusion transmit sound with almost no echo: anechoic. This is why a pericardial or pleural effusion shows as a black stripe."),
  ],
  mimic=[
    ("Anechoic fluid vs very dark muscle", "Fluid is black and has no internal texture; poorly imaged muscle at too low gain is dark but speckled, and turning the gain up separates them (ECHO-13)."),
  ],
  traps=[
    ("“Muscle is hyperechoic”", "Myocardium is grey; bright white is reserved for strong reflectors such as pericardium and calcium."),
  ],
  decode=[
    ("[pattern] On 2D echo, how does a pericardial effusion appear?", "Black (anechoic): fluid does not reflect."),
  ],
  punch="B-mode draws echo strength as brightness: strong reflectors white, muscle grey, fluid black.",
)

L['ECHO-04'] = dict(
  sub="Cardiology → Echo in ICU → M-mode",
  step=3,
  intro="Still step 3: M-mode (motion mode) takes a single scan line from the 2D image and plots it against time. Because one line is sampled thousands of times a second, it times and measures fast movement better than the 2D picture.",
  parts=[
    ('a', "**Detects and records RAPID MOVEMENTS.** The very high sampling rate along one line resolves the motion of valve leaflets and walls that 2D, at 30–60 frames a second, blurs."),
    ('b', "**ECG or respiratory pressure waveforms are traced alongside.** The ECG marks end-diastole and end-systole for measurements; a respiratory trace lets the IVC or septal shift be timed against breathing."),
    ('c', "**Calculates chamber dimensions, fractional shortening and ejection fraction.** LV diameters at end-diastole and end-systole give FS = (LVIDd − LVIDs)/LVIDd (normal above 25%; ASE/EACVI 2015 discourages its use). EF can be derived from these diameters (Teichholz), but ASE/EACVI 2015 advises against EF from linear measurements, because they assume a regular shape the ICU ventricle with regional defects does not have; the biplane method of disks (Simpson) on 2D is preferred."),
  ],
  mimic=[
    ("M-mode vs 2D", "M-mode: one line, superb time resolution, for timing and linear distances (TAPSE, MAPSE, IVC). 2D: the whole slice, for shape, regional motion and volumes."),
  ],
  traps=[
    ("“M-mode EF is the recommended method”", "It is possible but not recommended; current guidance prefers biplane Simpson’s from 2D."),
  ],
  decode=[
    ("[pattern] Which echo mode measures TAPSE?", "M-mode through the lateral tricuspid annulus in the apical 4-chamber view."),
  ],
  punch="M-mode is one scan line plotted against time: unmatched for timing and linear distances, but the ejection fraction is better taken from 2D volumes.",
)

L['ECHO-05'] = dict(
  sub="Cardiology → Echo in ICU → The Doppler principle",
  step=4,
  intro="Step 4 changes what is being read. 2D uses the strength and timing of the echo; Doppler uses its frequency. The one Grand Test question sits one step earlier, on what makes an echo at all, and the card layer adds it.",
  parts=[
    ('a', "**The observed frequency of a wave depends on the relative speed of the source and the observer.** A source moving towards the listener squeezes the waves together (higher pitch); moving away stretches them (lower pitch), as with a passing siren."),
    ('b', "**Piezoelectric crystals convert electrical power to mechanical oscillations (sound waves).** A voltage makes the crystal vibrate and emit sound; the same crystal works in reverse when listening, turning returning sound into a voltage."),
    ('c', "**Doppler echo uses reflection of ultrasound by MOVING RED BLOOD CELLS.** Red cells are the moving scatterers in blood; their echo is weak, but its frequency carries their speed."),
    ('d', "**Doppler shift is the change in frequency between the emitted and the returning waveform.** Δf = 2 f₀ v cosθ / c, where f₀ is the transmitted frequency, v the velocity of the cells, θ the angle between beam and flow and c the speed of sound. The factor 2 is there because the cells first receive and then re-emit the sound while moving."),
    ('e', "**The shift is determined by the velocity AND direction of blood flow, which gives haemodynamic information.** A positive shift means flow towards the probe, a negative shift flow away; the size gives velocity, and velocity gives pressure gradients (4V²) and stroke volume (VTI × LVOT area)."),
  ],
  mimic=[
    ("Acoustic impedance vs attenuation", "Impedance (Z = density × speed of sound) is a medium’s resistance to sound and decides how much reflects at an interface. Attenuation is energy lost along the path with depth, and it rises with frequency."),
    ("Doppler shift vs echo amplitude", "Doppler reads frequency (movement); 2D reads amplitude (structure)."),
  ],
  traps=[
    ("“Attenuation is the resistance to propagation of sound”", "That is acoustic impedance. Attenuation is loss of energy with distance (absorption, scatter, reflection), which is why high frequencies do not reach deep."),
    ("“The piezoelectric effect is the resistance to sound”", "It is the conversion between electrical and mechanical energy in the crystal."),
  ],
  decode=[
    ("Which of the following is the resistance to propagation of sound? [DocT GT]", "Acoustic impedance (Z = ρc); the size of the impedance mismatch decides reflection, hence gel and the blocking effect of lung and bowel gas."),
    ("[pattern] What does the Doppler shift depend on?", "The velocity and direction of the red cells relative to the beam (and the transmitted frequency)."),
  ],
  punch="2D reads how strong an echo is; Doppler reads how its frequency has changed, and that change gives the speed and direction of the red cells.",
)

L['ECHO-06'] = dict(
  sub="Cardiology → Echo in ICU → Doppler angle",
  step=4,
  intro="Still step 4: the Doppler equation contains cosθ, so the machine only sees the part of the velocity that runs along the beam. This card is that one term turned into numbers.",
  parts=[
    ('a', "**The USG beam must be PARALLEL to the direction of blood flow.** Only the component of flow along the beam changes the returning frequency. Cardiac Doppler is aligned, not angle-corrected (ASE: angle correction is not recommended): the angle is kept below about 20°, which is why gradients are taken from apical views where the beam runs with the blood (CVS05B)."),
    ('b', "**Cosine: 0° = 1, 30° = 0.87, 45° = 0.7, 60° = 0.5, 90° = 0.** The cosine is the fraction of true velocity that is measured; it falls slowly at first and then steeply."),
    ('c', "**Measured velocity for a true 5 m/s: 5, 4.35, 3.5, 2.5 and 0 m/s.** Measured = true × cosθ, so 60° reads exactly half and 90° reads nothing. Because a gradient is 4V², the 30° reading (4.35 m/s) gives 76 mmHg instead of 100 mmHg: a severe aortic stenosis can be graded moderate."),
    ('d', "**Error: 0° → 0%, 10° → 2%, 20° → 6%, 30° → 13%, 45° → 29%, 90° → 100%.** The error is 1 − cosθ; it stays under about 6% up to 20°, which is the working tolerance."),
  ],
  mimic=[
    ("Doppler vs 2D angle", "Doppler wants the beam parallel to flow; 2D wants it perpendicular to the structure for the sharpest edges."),
  ],
  traps=[
    ("“Off-angle Doppler overestimates velocity”", "Angle error always underestimates, because cosθ is never above 1."),
  ],
  decode=[
    ("[pattern] True velocity 5 m/s, beam at 60° to flow — measured velocity?", "2.5 m/s (cos 60° = 0.5)."),
  ],
  punch="The machine sees true velocity × cosθ: under 20° the error is small, at 60° it is half and at 90° there is no signal, so a misaligned beam always underestimates.",
)

L['ECHO-07'] = dict(
  sub="Cardiology → Echo in ICU → Pulse wave Doppler",
  step=5,
  intro="Step 5 is the choice between Doppler modes, and pulse wave Doppler is the one that can say where the velocity comes from. The one linked DocT QBank question (57% right) turns on exactly that.",
  parts=[
    ('a', "**The Doppler signal is analysed to depict velocity and direction of flow.** It is shown as a spectral trace: time on the x-axis, velocity on the y-axis, flow towards the probe above the baseline and away below."),
    ('b', "**A SINGLE crystal transmits the ultrasound and receives it after a preset time delay.** The crystal sends a short pulse and then listens only at one moment; sound returning at that moment can only have come from one depth."),
    ('c', "**The preset delay is a.k.a. the NYQUIST LIMIT.** That is the card’s wording, and it is wrong (FLAG): the delay sets the depth of the sample volume (range gating). The Nyquist limit is half the pulse repetition frequency, the highest velocity PW can show before aliasing (wrapping round to the other side of the baseline), usually about 1.5–1.7 m/s. The two are linked: a deeper sample needs a longer delay, so fewer pulses per second and a lower Nyquist limit."),
    ('d', "**A ‘sample volume’ is placed over the 2-D image at the region of interest.** The small gate on the image (in the LVOT for VTI, at the mitral leaflet tips for E and A) is the only place the trace comes from."),
    ('e', "**Used when flow disturbance must be LOCALISED, or blood velocity from a small region measured.** LVOT VTI for stroke volume, mitral inflow for diastolic function, a single point in a peripheral artery."),
  ],
  mimic=[
    ("PWD vs CWD", "PW: one site, low velocities, aliases above the Nyquist limit. CW: every depth along the beam at once, high velocities, no aliasing (ECHO-12)."),
  ],
  traps=[
    ("“Continuous wave Doppler for velocity and direction at a single site in the femoral artery” — the wrong choice when 57% were right", "CW gives direction and velocity but cannot say from which depth; only PW localises to one site, and femoral velocities are low enough not to alias."),
    ("“The preset delay is the Nyquist limit” (the card’s own wording)", "The delay sets depth; the Nyquist limit is PRF/2. In the exam, Nyquist limit means the maximum velocity before aliasing."),
  ],
  decode=[
    ("Femoral artery: which Doppler mode best determines both flow direction and velocity at a single site? [DocT QBank]", "Pulse wave Doppler (57% right)."),
    ("[pattern] What is the Nyquist limit?", "Half the pulse repetition frequency; above it PW aliases."),
  ],
  punch="Pulse wave Doppler listens at one moment after each pulse, so it knows where the signal comes from; the price is a velocity ceiling, the Nyquist limit (PRF/2), which falls as the sample goes deeper.",
)

L['ECHO-08'] = dict(
  sub="Cardiology → Echo in ICU → Continuous wave Doppler",
  step=5,
  intro="Still step 5: continuous wave Doppler gives up knowing where in exchange for measuring any speed.",
  parts=[
    ('a', "**Good resolution of HIGH VELOCITIES.** Sending and receiving never stop, so there is no pulse repetition frequency and no Nyquist limit; jets of 4–6 m/s are recorded without aliasing."),
    ('b', "**Localisation is LIMITED: the signal can originate at any point along the length or width of the beam.** With no timing gate, every moving scatterer along the line contributes; the trace shows the highest velocity anywhere on it, and the operator infers its origin from the anatomy."),
    ('c', "**Measures velocities of regurgitation and systolic flow through the aortic valve.** TR peak velocity estimates PA systolic pressure (4V² + RAP); the AS jet gives peak and mean gradients; MR and AR jets are also traced by CW."),
    ('d', "**2 crystals: one transmitting continuously, one receiving continuously.** One crystal cannot do both at once, so the jobs are split."),
  ],
  mimic=[
    ("CW vs PW for aortic stenosis", "The AS jet (above 4 m/s if severe) aliases on PW; CW records it whole. PW is used below the valve, in the LVOT."),
  ],
  traps=[
    ("“CW tells you where along the beam a jet arises”", "It cannot; that is the PW sample volume’s job."),
  ],
  decode=[
    ("[pattern] Which Doppler mode measures the peak TR velocity?", "Continuous wave."),
  ],
  punch="Continuous wave Doppler never stops listening, so it has no velocity ceiling but cannot say where along the beam the fastest flow lies.",
)

L['ECHO-09'] = dict(
  sub="Cardiology → Echo in ICU → Colour flow imaging",
  step=5,
  intro="Still step 5: colour flow imaging is pulse wave Doppler done at many sample points at once, each coded as a colour and laid over the 2D picture.",
  parts=[
    ('a', "**Velocity and direction of blood flow as a colour map superimposed on the 2-D image.** Within a colour box, each pixel shows the mean velocity at that point."),
    ('b', "**PULSE WAVE Doppler signals derive the image.** It is multigated PW, so it localises, and it has a Nyquist limit, shown at the ends of the colour bar; jets faster than that alias into a mosaic, which is itself a marker of turbulent high-velocity flow."),
    ('c', "**Used to visualise and semi-quantitatively assess regurgitant jets and abnormal flows.** Jet area, vena contracta width and PISA come from colour; they grade severity in bands, not exact volumes."),
    ('d', "**Higher velocities are shown in progressively LIGHTER shades of colour.** Dark red or blue is slow flow; pale, near yellow or cyan, is fast flow near the limit."),
    ('e', "**BLUE = AWAY from the probe, RED = TOWARDS the probe; the source’s BART (Blue Away, Red Towards).** Colour shows direction relative to the beam, not to the heart."),
  ],
  mimic=[
    ("Mosaic vs true flow reversal", "A mosaic of colours in a jet is aliasing and turbulence; a clean change from red to blue across a straight vessel is the beam angle (ECHO-11)."),
  ],
  traps=[
    ("“Red means arterial, blue means venous”", "Colour is direction relative to the probe; an artery flowing away is blue."),
  ],
  decode=[
    ("[pattern] On colour Doppler, what does blue indicate?", "Flow away from the probe."),
  ],
  punch="Colour flow is pulse wave Doppler painted over the picture, so it localises but aliases; red is towards, blue away, and lighter shades are faster.",
)

L['ECHO-10'] = dict(
  sub="Cardiology → Echo in ICU → Tissue Doppler",
  step=5,
  intro="Still step 5: tissue Doppler points the same pulse wave method at the heart wall instead of the blood.",
  parts=[
    ('a', "**Measures velocities of TISSUE movement.** The filters are reversed: blood Doppler discards slow, strong signals (wall clutter); tissue Doppler keeps them and discards the fast, weak blood signal."),
    ('b', "**These velocities are LOWER than blood velocities.** The annulus moves at centimetres per second (about 5–20 cm/s), blood at up to a metre or more per second."),
    ('c', "**Assesses tricuspid and mitral annulus velocities.** At the mitral annulus, e′ reflects LV relaxation (reduced if septal ≤6 or lateral ≤7 cm/s in ASE 2025), and E/e′ estimates filling pressure (average >14 raised)."),
    ('d', "**Assesses RV systolic function.** The systolic velocity of the lateral tricuspid annulus, S′, below 9.5 cm/s indicates RV systolic dysfunction (ASE 2015); like TAPSE it is angle dependent and measures longitudinal function only."),
  ],
  mimic=[
    ("S′ vs TAPSE", "Both judge RV longitudinal function at the tricuspid annulus: S′ is a velocity (tissue Doppler, <9.5 cm/s abnormal), TAPSE a distance (M-mode, <17 mm abnormal)."),
  ],
  traps=[
    ("“Tissue velocities are higher than blood velocities”", "They are much lower, but the signal is stronger."),
  ],
  decode=[
    ("[pattern] Tricuspid annular S′ 8 cm/s — interpretation?", "RV systolic dysfunction (<9.5 cm/s)."),
  ],
  punch="Tissue Doppler reads the slow, strong signal of the annulus: S′ for RV systolic function and e′ (with E/e′) for LV relaxation and filling pressure.",
)

L['ECHO-11'] = dict(
  sub="Cardiology → Echo in ICU → The no-signal zone",
  step=4,
  intro="Step 4’s cosine rule seen on the screen. A straight vessel crossing a sector image meets the diverging beam lines at different angles along its length, so one stretch of flow is coming towards the beam and another going away, though the blood never changes direction.",
  parts=[
    ('a', "**At the centre the flow is perpendicular to the beam: 90°, cosine 0, no detectable Doppler shift. Where flow angles towards the probe it is RED; where it angles away it is BLUE.** The machine only sees the part of velocity along each beam line; where the line meets the vessel at right angles that part is zero, so the pixels are black, and on either side the sign of the cosine flips."),
  ],
  mimic=[
    ("Angle colour change vs real reversal", "Angle: colour changes at the point where the vessel is perpendicular to the beam, with a black gap between. Real reversal (as in AR in the descending aorta) changes colour in time across the cardiac cycle, not along the vessel."),
  ],
  traps=[
    ("“The black centre is thrombus or no flow”", "Flow is present; the beam meets it at 90°. Tilting the probe brings colour back."),
  ],
  decode=[
    ("[pattern] Vessel across the beam shows red one end, blue the other and black in the middle — why?", "The angle: cos 90° = 0 at the centre."),
  ],
  punch="Same blood, same direction, different colours: the colour follows the beam angle, and where the angle is 90° the cosine is zero and there is no signal.",
)

L['ECHO-12'] = dict(
  sub="Cardiology → Echo in ICU → PWD vs CWD",
  step=5,
  intro="Step 5 in one table: every difference between the two spectral Doppler modes follows from one crystal timed against two crystals running continuously. The linked DocT QBank question (57%) rests on the localisation row.",
  parts=[
    ('a', "**Crystals: PWD 1, CWD 2.** One crystal must stop transmitting to listen; two can share the work and never stop."),
    ('b', "**PWD: one crystal transmits, then receives after a preset delay (Nyquist limit); CWD: one transmits continuously, one receives continuously.** The delay is what fixes the depth of the PW sample; the Nyquist limit is a separate quantity, PRF/2, the velocity ceiling (ECHO-07, FLAG)."),
    ('c', "**Localisation: PWD YES, at the sample volume; CWD LIMITED, signal from anywhere along the beam.** Timing the return pins the depth; continuous listening cannot."),
    ('d', "**High velocities: PWD limited; CWD good resolution.** PW samples in pulses, so above the Nyquist limit it aliases; CW has no sampling limit."),
    ('e', "**Uses: PWD for localising a flow disturbance and velocity from a small region; CWD for regurgitation velocities and systolic flow through the aortic valve.** Hence LVOT VTI and mitral inflow by PW, TR and AS jets by CW."),
  ],
  mimic=[
    ("Colour vs PW", "Colour flow is multigated PW, so it shares PW’s ability to localise and its aliasing."),
  ],
  traps=[
    ("“CWD to measure velocity at a single site in the femoral artery”", "CW cannot localise; PW is the answer (57% chose it)."),
  ],
  decode=[
    ("Which Doppler mode determines both flow direction and velocity accurately at a single site? [DocT QBank]", "Pulse wave Doppler."),
    ("[pattern] Peak velocity of a 5 m/s AS jet — which mode?", "Continuous wave; PW would alias."),
  ],
  punch="Pulse wave knows where but not how fast; continuous wave knows how fast but not where. One crystal timed versus two running continuously explains every row.",
)

L['ECHO-13'] = dict(
  sub="Cardiology → Echo in ICU → Setting up",
  step=6,
  intro="Step 6 closes the deck at the bedside: the settings that decide whether the views of CVS05B can be read at all.",
  parts=[
    ('a', "**Optimal positioning: LEFT LATERAL position.** Turning the patient onto the left side brings the heart forward against the chest wall and moves lung out of the way, improving the parasternal and apical windows. The subcostal view is taken supine (CVS05B)."),
    ('b', "**Adjust the height of the patient bed and connect the ECG cables of the echo machine.** A comfortable working height steadies the probe hand; the ECG times systole and diastole for every measurement."),
    ('c', "**2-D: adjust the gain knob until the picture is neither too dark nor too bright; depth knob so the structure of interest sits in the CENTRE of the screen.** Gain amplifies all returning echoes: too high fills the cavities with noise, too low hides endocardium. Too much depth wastes the image on structures behind the heart and lowers the frame rate."),
    ('d', "**PWD and CWD: adjust baseline and scale so the entire waveform is seen.** Moving the baseline and raising the scale (for PW only up to the maximum pulse repetition frequency the depth allows) brings a clipped or wrapped trace back on screen, so peak velocity and VTI can be traced."),
  ],
  mimic=[
    ("Gain vs depth", "Gain changes brightness; depth changes how far down the image goes and how big the heart appears."),
  ],
  traps=[
    ("“Turn the gain up until the cavities look grey”", "Blood should be black; grey cavities mean too much gain."),
  ],
  decode=[
    ("[pattern] Optimal patient position for parasternal and apical views?", "Left lateral decubitus."),
  ],
  punch="Left lateral position, ECG on, gain until the blood is black and the walls are clear, depth with the target in the centre, and Doppler baseline and scale so the whole waveform fits.",
)

FLAGS = {
  'ECHO-07': "c: ‘the preset delay is a.k.a. the NYQUIST LIMIT’ is wrong. The delay sets the depth of the sample volume (range gating); the Nyquist limit is half the pulse repetition frequency, the maximum velocity before aliasing (123sonography). The explanation says so.",
  'ECHO-12': "b (table, transmit/receive row): same error as ECHO-07 — ‘preset delay (Nyquist limit)’. The delay fixes depth; the Nyquist limit is PRF/2.",
  'ECHO-04': "c and watch: EF can be computed from M-mode diameters, but ASE/EACVI 2015 says volumes from linear measurements should not be used for EF (biplane Simpson preferred). The watch line’s ‘IVC, EF … all come from an M-mode line, not from the 2D picture’ overstates it: IVC and linear dimensions may be measured on 2D, and EF is preferably from 2D volumes.",
  'ECHO-01': "a, b: the 59% / 43% figures come from Spencer et al. (JACC 2001), cardiologists’ physical examination versus a miniaturised echo in 36 patients, not an ICU study. The source of the 77–93% agreement range could not be traced (Melamed 2009, 80–92% against formal echo, sits in the band). Fine as the source’s figures.",
}
