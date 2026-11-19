# CVS05A top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs05a_learn.py.
# Fields: sub, step (index into cvs05a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions: the top-up's own src (DocT Procedures, Techniques & POCUS Q19; DocT GT GT5 Q99); the stems are not in qpack/CVS05A.md, so decode items are labelled [pattern].
# Checked online on 19 Nov 2026: frequency against attenuation and depth (NYSORA POCUS physics page). Review check 19 Nov 2026: probe manoeuvre terms (POCUS101 probe-movements page:
# rock = toward/away from the indicator along the long axis, in-plane; tilt/fan = side to side along the short axis; rotate about the central axis; compress). From standard references: PLAX to PSAX by a 90° clockwise rotation; probe ranges linear 5–15, curvilinear 2–5, phased array 1–5 MHz.
T = {}

T['T_4d72df8c'] = dict(
  sub="Cardiology → Echo in ICU → Probe manoeuvres and probe choice",
  step=2,
  intro="Step 2 is about the probe, and this card adds how it is moved. Each manoeuvre changes one thing while the others stay fixed, which is what lets an operator find a view and then refine it without losing it; the last line repeats the frequency–depth rule that both Grand Test and QBank questions use.",
  parts=[
    ('a', "**Slide: move across the skin; sweep: slide a long distance (track a vessel).** The whole probe changes position, so the window changes; a sweep follows a vein or artery along its course, for example a femoral vein before cannulation."),
    ('b', "**ROCK (heel–toe): tilt along the long axis with the contact point fixed.** The beam swings within its own plane, towards or away from the marker, bringing a structure at the edge of the image towards the centre."),
    ('c', "**Fan/tilt: angle across the short axis, contact point fixed.** The beam swings out of its plane, cutting successive slices; fanning through PSAX moves from the aortic to the mitral and papillary levels."),
    ('d', "**Rotate: turn on the spot (PLAX → PSAX); compress: press (vein compressibility).** Rotation changes the plane at the same window, 90° clockwise from PLAX to PSAX; compression that flattens a vein fully excludes thrombus at that point."),
    ('e', "**Probe choice: linear 5–15 MHz for superficial work (pleura, vascular access, ONSD, airway); curvilinear 2–5 MHz for abdomen, FAST and lung bases; phased array 1–5 MHz between ribs (heart, TCD). Higher frequency = better resolution, less depth.** Attenuation rises with frequency, so depth decides the frequency and the window decides the footprint (ECHO-02)."),
  ],
  mimic=[
    ("Rock vs fan", "Rock moves the beam within its plane (in-plane); fan moves it across planes (out-of-plane). Both keep the contact point still."),
    ("Rotate vs fan", "Rotation changes the plane’s orientation around the beam’s axis; fanning tilts the plane through the tissue."),
  ],
  traps=[
    ("“Rotating the probe moves it to a new window”", "Rotation keeps the window and changes the plane; sliding changes the window."),
    ("“Linear probe for a pleural effusion or the lung bases”", "The linear probe is for the pleural line; deep fluid needs the curvilinear 2–5 MHz probe."),
  ],
  decode=[
    ("[pattern] Which manoeuvre converts PLAX to PSAX?", "Rotation, 90° clockwise, at the same window."),
    ("[pattern] Which probe for optic nerve sheath diameter or the cricothyroid membrane?", "Linear, high frequency."),
  ],
  punch="Slide and sweep move the window, rock and fan swing the beam with the contact point fixed, rotate changes the plane, compress tests a vein; and depth decides the frequency.",
)

FLAGS = {}
