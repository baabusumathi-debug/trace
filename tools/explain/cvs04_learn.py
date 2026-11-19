# CVS04 — Explain v3 ("Learn" depth): cardiogenic shock, part 2 — mechanical circulatory support: bridge strategies, the three haemodynamic goals, percutaneous devices,
# pressure–volume loops on IABP, pLVAD and VA ECMO, the IABP (mechanism, effects, practicalities, timing errors, contraindications), IABP-SHOCK II and its score, Impella, TandemHeart,
# VA ECMO, the five-device comparison tables, the ECMO unloading paradox, transplant indications, durable LVADs and the hub-and-spoke management ladder.
# No mnemonics or hooks. Driven by qpack/CVS04.md (8 question links; CS-42 IABP mechanism asked 3 times, CS-46 Impella effects 2, CS-44 IABP-SHOCK II, CS-47 TandemHeart and
# CS-49 insertion once each). CS-37–41, 43, 45, 48, 50–55 have no linked question and get short explanations with [pattern] decode items.
# No `fix` entries exist for CVS04 in trace/test/data/qbank.json (checked 19 Nov 2026; chips only). The card layer (cvs_cardlayer.json lines for CS-42, CS-44, CS-47; chips for CS-46)
# was read and the explanations agree with it. No Top-up cards for this deck.
# Checked online on 19 Nov 2026:
#  - 2025 ACC/AHA/ACEP/NAEMSP/SCAI ACS guideline (ACC ‘Cardiogenic Shock and MCS: Year in Review 2025’; WikiDoc summary): microaxial intravascular flow pump 2a (B-R) to reduce death in selected
#    STEMI with severe or refractory CS; routine IABP or VA-ECMO in AMI-CS class 3 no benefit (B-R); short-term MCS as a bridge to surgery for mechanical complications 2a (B-NR).
#  - ESC 2023 ACS (MDPI Cardiogenetics/JCDD 2026 review summary): short-term MCS may be considered in ACS with severe/refractory CS (IIb, C); IABP for haemodynamic instability from mechanical
#    complications (IIa, C); routine IABP without mechanical complications not recommended (III; as in the CVS03 check). No preferred device named.
#  - IABP-SHOCK II (Thiele, NEJM 2012; Wiki Journal Club, The Bottom Line): n 600, 37 German centres, AMI-CS with planned early revascularisation; 30-day mortality 39.7 vs 41.3% (RR 0.96, p 0.69);
#    86.6% of balloons placed after PCI; 45% resuscitated before randomisation; ~10% crossover to IABP in controls; excluded CPR >30 min, fixed dilated pupils, no intrinsic heart activity,
#    mechanical complications, severe AR, severe PAD, shock >12 h. 6-year mortality 66.3 vs 67.0% (RR 0.99; Healio, Circulation 2019).
#  - IABP-SHOCK II risk score (Pöss, JACC 2017 abstract): age >73, prior stroke, glucose >191 mg/dL (10.6 mmol/L), creatinine >1.5 mg/dL (132.6 µmol/L), TIMI <3 after PCI, lactate >5 mmol/L;
#    0–9 points; low 0–2 (30-day mortality 23.8%), intermediate 3–4 (49.2%), high 5–9 (76.6%).
#  - ECLS-SHOCK (Thiele, NEJM 2023; MDPI review): n 420, 78% resuscitated; 30-day mortality 47.8 vs 49.0%; no 1-year difference; more bleeding and vascular complications (CVS03 check).
#  - DanGer Shock (Møller, NEJM 2024; ACC and MDPI summaries): STEMI-CS, Impella CP; 180-day mortality 45.8 vs 58.5% (HR 0.74); more bleeding, limb ischaemia and RRT; 10-year 52.5 vs 68.8%.
#  - ISAR-SHOCK (Seyfarth, JACC 2008; ACC trial page): n 26, Impella LP2.5 vs IABP; cardiac index change at 30 min +0.49 vs +0.11 L/min/m² (p 0.02); 30-day mortality 46% in both.
#    IMPRESS (2017, n 48, Impella CP vs IABP, 92% post-arrest): no mortality difference at 30 days or 6 months.
#  - Impella labelling (FDA fact sheet 2020; manufacturer 5.5 page): CS indication within 48 h of AMI or cardiac surgery, or cardiomyopathy/myocarditis with isolated LV failure; CP up to 4 days,
#    5.5 up to 14 days (axillary surgical insertion). Contraindications: LV mural thrombus; mechanical aortic valve or heart constrictive device; aortic stenosis/calcification with orifice
#    ≤0.6 cm²; moderate–severe AR (≥2+); severe arterial disease; ASD or VSD (including post-infarct VSD); significant RV failure, LV rupture, tamponade (CS indication). Adverse events include
#    haemolysis, limb ischaemia, bleeding, stroke, aortic valve injury, thrombocytopenia, renal failure.
#  - Device sizes and flows (WikiDoc device table; MDPI review): Impella 2.5 (12 Fr, 2.5 L/min), CP (14 Fr pump, ~4.3 L/min), 5.5 (21 Fr, 5.5 L/min), RP (22 Fr, 4.0); TandemHeart 21 Fr
#    transseptal inflow, 15–19 Fr arterial outflow, centrifugal, 4–5 L/min; VA-ECMO 4–6 L/min, inflow 18–21 Fr, outflow 15–22 Fr.
#  - MOMENTUM 3 5-year (Mehra, JAMA 2022; ACC page): HeartMate 3 survival 58.4% vs 43.7% (HeartMate II), n 1,028; stroke 0.05 vs 0.14 events per patient-year.
#  - SCAI SHOCK stages 2022 (as in the CVS03 check, 19 Nov 2026): C classic (lactate ≥2), D deteriorating, E extremis.
# Second check (19 Nov 2026; web search budget exhausted, so settled from standard references and the CVS03/MI sibling checks): IABP-SHOCK II 12-month 52 vs 51% (Thiele,
#  Lancet 2013, RR 1.01); Impella 2.5/CP inlet ~3.5 cm below the annulus (Abiomed IFU); ISHLT median post-transplant survival ~12.5 years; TandemHeart 21 Fr inflow, 15–19 Fr outflow, 4–5 L/min,
#  IJ route = ProtekDuo RA→PA RVAD configuration; VA-ECMO 4–6 L/min; ESC 2023 short-term MCS IIb C, IABP mechanical complications IIa C, routine IABP III B; MOMENTUM 3 58.4 vs 43.7%.
#  DanGer Shock long-term (10-year) figures above were not re-verified and are not used in the text.
# From standard references without a fresh check (confident unless said): IABP practicalities (7–8 Fr sheath, 30–50 mL helium balloon sized to height, tip about 2 cm below the top of the arch,
# above the renal arteries, ECG R-wave or pressure trigger, inflation at the dicrotic notch), Burkhoff’s PV-loop descriptions of IABP, Impella, TandemHeart and VA ECMO, ESC 2021 HF MCS
# terminology (bridge to decision, candidacy, transplant, recovery; destination therapy), the AHA 2017 cardiogenic shock statement (van Diepen) as the source of the hub-and-spoke ladder,
# IABP-SHOCK II 12-month mortality 52 vs 51%, ISHLT median post-transplant survival about 12 years, the Impella inlet about 3.5 cm below the aortic valve for the CP.

SPINE = [
  ("Why support the pump", "Mechanical support buys time for a defined destination — recovery, a decision, a transplant or a durable pump — by keeping organs perfused, unloading the ventricle and feeding the coronaries."),
  ("How each device moves blood", "The IABP is a pneumatic counterpulsation balloon, Impella an axial pump across the aortic valve, TandemHeart a centrifugal pump draining the left atrium, and VA ECMO a centrifugal circuit with an oxygenator."),
  ("What the loop shows", "On the pressure–volume loop the IABP lowers pressure and modestly raises stroke volume, a pLVAD shrinks the loop and the work, and peripheral VA ECMO pushes it up and to the right."),
  ("The balloon pump", "The IABP inflates in diastole and deflates just before systole, gives under 1 L/min, and IABP-SHOCK II showed no survival benefit, so routine use is now class III."),
  ("Matching the device to the patient", "Flow, which ventricle is supported, afterload, gas exchange and the complication profile decide the device, and every device has anatomical contraindications."),
  ("Beyond temporary support", "When the heart does not recover, the ladder ends in transplant or a destination LVAD, with palliation available at every rung."),
]

PRIMER = "Mechanical circulatory support (MCS) means devices that take over part of the heart’s pumping when drugs are not enough. Short-term devices (IABP, Impella, TandemHeart, VA ECMO) are inserted percutaneously or peripherally for days to weeks; durable LVADs are implanted surgically for months to years. On a pressure–volume loop, the width is stroke volume, the enclosed area is stroke work, and the total pressure–volume area (loop plus the triangle under the end-systolic line) tracks myocardial oxygen consumption. Arterial elastance (Ea) is the slope from end-diastolic volume to the end-systolic point and stands for afterload."

L = {}

L['CS-37'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → Bridge strategies",
  step=1,
  intro="Step 1 is why support is started at all: every device is a bridge, and the strategy names where the bridge leads. Not asked directly; it frames stems that describe a patient and ask what the support is for.",
  parts=[
    ('a', "**Bridge to decision: uncertain suitability for transplant or long-term MCS; first goal haemodynamic stability so reversibility of organ failure and contraindications can be assessed.** The typical VA ECMO situation after a crash: neurology after arrest, kidneys and liver are unknown, so support first and decide later."),
    ('b', "**Bridge to bridge: a provisional plan to move to long-term MCS once stabilised.** Typically ECMO or Impella now, a durable LVAD once organ function has recovered enough for surgery."),
    ('c', "**Bridge to transplant: listed or known candidates, supported to prevent organ dysfunction until a donor heart is available.** Keeping the kidneys and liver intact keeps the patient transplantable."),
    ('d', "**Bridge to recovery: potentially reversible myocardial dysfunction (e.g. myocarditis), supported until function allows weaning.** Fulminant myocarditis, stunning after reperfusion, takotsubo and post-cardiotomy failure are the classic settings."),
  ],
  mimic=[("Bridge to transplant vs destination therapy", "Bridge to transplant expects a donor heart; destination therapy is a durable LVAD in a patient who will never be transplanted (CS-54, CS-55).")],
  traps=[("“Bridge strategies are always short-term devices”", "The card’s watch line says so, but in ESC terminology bridge to transplant is often a durable LVAD; the strategy is a destination, not a device class.")],
  decode=[("Young man, fulminant myocarditis, VA ECMO placed: the strategy? [pattern]", "Bridge to recovery — reversible myocardium."),
          ("Post-arrest, unknown neurology, on ECMO: the strategy? [pattern]", "Bridge to decision.")],
  punch="The bridge is named by its far end: decision when the future is unknown, recovery when the heart may heal, transplant when a donor is awaited, bridge when a durable pump is next.",
)

L['CS-38'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → Haemodynamic goals",
  step=1,
  intro="Step 1, the goals. Every device is judged against the same three, and the devices differ mainly in the second one. Not asked directly.",
  parts=[
    ('a', "**Maintenance of end-organ perfusion.** Flow and pressure to brain, kidney and gut; this is what stops the lactate rising and the patient sliding from SCAI C to D."),
    ('b', "**Ventricular unloading — less ventricular volume, wall stress, myocardial work and oxygen consumption.** Wall stress rises with pressure and radius (Laplace), so emptying the ventricle cuts oxygen demand in an ischaemic, failing heart and may limit infarct size."),
    ('c', "**Enhanced myocardial perfusion.** Coronary flow depends on aortic diastolic pressure minus LV end-diastolic pressure; raising the first (IABP) or lowering the second (unloading) both help."),
  ],
  mimic=[("Perfusion vs unloading", "VA ECMO gives the most perfusion but raises afterload and can fail to unload (CS-52); Impella both perfuses and unloads.")],
  traps=[("“More flow means a better-supported heart”", "Flow serves the organs; the heart is helped only if the device also unloads it.")],
  decode=[("Which haemodynamic goal does peripheral VA ECMO fail? [pattern]", "Ventricular unloading.")],
  punch="Support has to do three things — perfuse the organs, unload the ventricle and feed the coronaries — and devices that do the first need not do the second.",
)

L['CS-39'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → Percutaneous devices",
  step=2,
  intro="Step 2 opens with the common ground: percutaneous devices can go in fast in the cath lab, and they share one list of complications that comes from large-bore arterial access, anticoagulation and blood passing through a pump. Not asked directly.",
  parts=[
    ('a', "**Inserted percutaneously or surgically; the purely percutaneous route allows rapid deployment without specific surgical training.** An interventional cardiologist can place an IABP, Impella CP or peripheral ECMO in minutes, which matters when the shock is in the cath lab."),
    ('b', "**Each device carries a profile of complications that may limit its success.** The choice is a trade between support and harm: in DanGer Shock the Impella saved lives but roughly quadrupled the composite of device-related adverse events (24.0% vs 6.2%)."),
    ('c', "**Limb ischaemia, bleeding, embolic phenomena (stroke), infection, haemolysis.** Limb ischaemia and bleeding scale with sheath size (7–8 Fr IABP vs 14 Fr Impella CP vs 15–25 Fr ECMO cannulae); stroke comes from clot on the device or in a stagnant aortic root; haemolysis from shear in rotary pumps, worst with Impella (CS-46)."),
  ],
  mimic=[("Generic vs device-specific complication", "Limb ischaemia, bleeding and pseudoaneurysm come with any femoral sheath; haemolysis is the one tied to the pump itself.")],
  traps=[("“Percutaneous means low-risk”", "Large-bore arterial access is the main source of harm; ECLS-SHOCK and DanGer Shock both had more bleeding and limb ischaemia with the device.")],
  decode=[("Common complications of percutaneous MCS: all except? [pattern]", "The five are limb ischaemia, bleeding, stroke, infection and haemolysis; anything else (e.g. neuropathy) is the odd one out.")],
  punch="Percutaneous devices go in quickly without a surgeon, but large sheaths, anticoagulation and pumps bring limb ischaemia, bleeding, stroke, infection and haemolysis.",
)

L['CS-40'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → PV loops with devices",
  step=3,
  intro="Step 3 is the pressure–volume loop. The card is a sketch; the words below are what the sketch should show, so each device can be drawn from its mechanism. Not asked directly, but CS-41 and CS-52 test the conclusions.",
  parts=[
    ('a', "**IABP: the blue loop sits slightly lower and slightly wider than the green baseline, with a flatter Ea line.** Systolic deflation lowers the pressure the LV ejects against, so peak pressure falls, Ea falls and stroke volume rises a little; end-diastolic volume falls slightly. The change is small, matching the ‘modest’ effects on CS-43."),
    ('b', "**pLVAD (Impella / TandemHeart): the loop moves left and shrinks.** End-diastolic volume and pressure fall because the device drains the ventricle (Impella) or the atrium (TandemHeart). With Impella the ventricle empties continuously, so the isovolumic phases disappear and the loop turns triangular; at high flow aortic pressure is held up by the pump while the LV’s own stroke volume falls."),
    ('c', "**Peripheral VA ECMO: the loop moves right and up and narrows, with a steeper Ea.** Retrograde arterial flow raises aortic pressure, so the weak LV ejects less, end-systolic and end-diastolic volumes rise, and LVEDP climbs. In a very weak LV the aortic valve may stop opening and the loop collapses into a tall, narrow shape — the distended, unvented ventricle."),
  ],
  mimic=[("IABP vs pLVAD loop", "IABP keeps the loop’s shape and nudges it down and wider; pLVAD shrinks it and shifts it left.")],
  traps=[("“VA ECMO unloads the left ventricle because it bypasses the heart”", "It unloads the right heart; for the LV it adds afterload, so the loop moves up and right.")],
  decode=[("PV loop shifted rightward and upward with a steeper Ea after device insertion — which device? [pattern]", "Peripheral VA ECMO.")],
  punch="Draw the IABP loop slightly lower and wider, the pLVAD loop smaller and shifted left, and the peripheral ECMO loop narrower, higher and shifted right.",
)

L['CS-41'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → PV loop interpretation",
  step=3,
  intro="Step 3, reading the loops: what each device does to stroke work and myocardial oxygen consumption, the two numbers that decide whether the heart itself is helped. Not asked directly.",
  parts=[
    ('a', "**IABP: wider PV loop area, increased stroke volume.** ‘Wider’ is the stroke volume; because peak pressure also falls, the enclosed area (stroke work) and the pressure–volume area change little or fall modestly, which is why CS-43 lists a modest fall in stroke work and oxygen consumption."),
    ('b', "**Impella / TandemHeart: smaller loop area, a significant fall in LV stroke work and myocardial oxygen consumption.** The pump does the work the ventricle used to do; lower volume and pressure shrink both the loop and the pressure–volume area. This is the mechanical basis for unloading."),
    ('c', "**Peripheral ECMO: loop not unloaded; increased arterial elastance and stroke work, MVO2 unchanged or rising.** A higher afterload with a larger end-systolic volume enlarges the pressure–volume area, so oxygen demand stays the same or climbs while the organs are well perfused."),
  ],
  mimic=[("Loop width vs loop area", "Width is stroke volume; area is stroke work. The IABP widens the loop but lowers its height.")],
  traps=[("“A bigger loop on the IABP means more work for the heart”", "The wider loop reflects a larger stroke volume at a lower pressure; oxygen consumption falls slightly, not rises.")],
  decode=[("Device with greatest reduction in myocardial oxygen consumption? [pattern]", "pLVAD (Impella or TandemHeart) — smallest loop and pressure–volume area.")],
  punch="The pLVAD shrinks the loop and the oxygen bill, the IABP widens it at a lower pressure for a modest gain, and peripheral ECMO leaves the LV working as hard or harder.",
)

L['CS-42'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → IABP mechanism",
  step=4,
  intro="Step 4 is the balloon pump, the most-asked card in this deck. Counterpulsation means the balloon does the opposite of the heart: it fills in diastole and empties in systole. Three Grand Test questions came from it — practicalities, timing errors and contraindications — and fewer than half got the practicalities right.",
  parts=[
    ('a', "**Diastole: the balloon inflates, displacing blood volume, augmenting native stroke volume and enhancing coronary blood flow.** A 30–50 mL helium balloon in the descending aorta (tip about 2 cm below the top of the arch, beyond the left subclavian, ending above the renal arteries) inflates at aortic valve closure. The displaced blood raises aortic diastolic pressure (diastolic augmentation), and since the LV is perfused mainly in diastole, coronary pressure rises. Helium is used because its low density lets the balloon fill and empty within one beat."),
    ('b', "**Systole: rapid deflation reduces LV afterload and increases LV stroke volume.** Collapsing the balloon just before the aortic valve opens leaves a space the LV ejects into, so end-diastolic aortic pressure (the pressure the LV must exceed) falls and the ventricle empties further for less work."),
    ('c', "**Synchronised with the ECG.** The R wave triggers deflation and inflation follows at the T wave; the arterial pressure waveform (dicrotic notch) or a pacing spike can trigger instead. A regular rhythm is needed: in fast or irregular rhythms timing slips, so ‘requires an unstable rhythm’ is the reverse of the truth."),
  ],
  table=dict(title="Timing errors on the arterial trace", head=["Error", "What happens", "Effect"], rows=[
    ["Early inflation (before the dicrotic notch)", "Balloon inflates while the LV is still ejecting", "Afterload and LV work rise; aortic valve may close early"],
    ["Late inflation", "Inflates well after valve closure", "Diastolic augmentation and coronary benefit lost"],
    ["Early deflation", "Deflates mid-diastole", "Augmentation lost; possible retrograde coronary flow"],
    ["Late deflation", "Balloon still up as the LV starts to eject", "Most harmful: LV ejects against the inflated balloon"],
  ]),
  mimic=[("IABP vs Impella insertion", "IABP: 7–8 Fr femoral sheath, femoral artery ≥4 mm. Impella CP: 14 Fr sheath, needs a larger vessel.")],
  traps=[("“Usual sheath size is 13–14 Fr” (chosen by many; 46% got the question)", "That is Impella CP and ECMO territory; the IABP goes through a 7–8 Fr femoral sheath, and the femoral artery must be over about 4 mm to avoid limb ischaemia."),
         ("“Implant beyond 2 weeks is safe”", "Usual support is days; beyond 1–2 weeks limb ischaemia, infection and thrombocytopenia rise."),
         ("“Severe LV dysfunction or CAD contraindicates the IABP”", "Those are its indications. The absolute contraindications are moderate–severe aortic regurgitation (diastolic inflation drives more blood back into the LV), aortic dissection and severe aorto-iliac disease (79% got this).")],
  decode=[("IABP in cardiogenic shock: which is true — >2 weeks safe, femoral artery >4 mm, 13–14 Fr sheath, needs unstable rhythm? [DocT GT]", "Femoral artery >4 mm (46%)."),
          ("Inflation occurs before aortic valve closure: consequence? [DocT GT]", "Increased LV workload — inflation against ejection raises afterload."),
          ("Contraindication to IABP after MI? [DocT GT]", "Aortic regurgitation (79%).")],
  extra=[dict(q="Blood appears in the IABP gas line. What next?", a="Balloon rupture: stop pumping, clamp the line and remove the balloon at once (helium embolism; clot inside can trap it); never reinsert the same balloon. A stationary balloon is thrombogenic, so never leave it switched off in situ.")],
  punch="The balloon inflates at the dicrotic notch to push blood into the coronaries and deflates just before systole to lower afterload; it needs a 7–8 Fr sheath, a regular rhythm and a competent aortic valve.",
)

L['CS-43'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → IABP effects",
  step=4,
  intro="Step 4, what the balloon actually achieves. Every effect is modest, which is why it helps a borderline patient and fails a crashing one. Not asked directly; the comparison tables (CS-50, CS-51) carry these numbers into questions.",
  parts=[
    ('a', "**Modest rise in SV and cardiac output.** The balloon moves only its own volume (30–50 mL) per beat and depends on the LV still ejecting; it adds no flow of its own."),
    ('b', "**Modest fall in LVEDP, LV wall stress, stroke work and myocardial oxygen consumption.** Lower afterload lets the ventricle empty further, so end-diastolic pressure and wall tension fall slightly."),
    ('c', "**Rise in diastolic BP with more coronary perfusion.** Coronary perfusion pressure is aortic diastolic pressure minus LVEDP, and the balloon raises the first and lowers the second."),
    ('d', "**Up to 1 L/min more cardiac output, depending on balloon size and patient interaction.** ‘Interaction’ means heart rate, rhythm, aortic compliance and residual LV function; a stiff aorta, tachycardia or a nearly silent LV all shrink the gain."),
    ('e', "**Decreases afterload; easily available and cost-effective.** It is the only device in the comparison table that lowers afterload (CS-51), and it is cheap, small-bore and familiar."),
  ],
  mimic=[("IABP vs Impella output", "IABP adds 0.5–1 L/min and needs a beating LV; Impella CP adds up to about 3.5–4.3 L/min independent of LV ejection.")],
  traps=[("“The IABP can support a heart in VF or asystole”", "It augments only what the ventricle ejects; without ejection there is nothing to augment, unlike Impella or ECMO.")],
  decode=[("Maximum increase in cardiac output with IABP? [pattern]", "About 0.5–1 L/min (up to 1 L/min)."),
          ("Which MCS device decreases afterload? [pattern]", "IABP.")],
  punch="The IABP raises diastolic pressure and lowers afterload, but adds at most about 1 L/min and only to a heart that is still ejecting.",
)

L['CS-44'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → IABP-SHOCK II trial",
  step=4,
  intro="Step 4 ends with the evidence. IABP-SHOCK II (2012) is the trial that took the balloon pump off the routine list, and its derived risk score is what Marrow asked. CS-04 used its entry criteria as a definition; this card is its result.",
  parts=[
    ('a', "**No difference in 30-day mortality, IABP vs no IABP.** 39.7% vs 41.3% (RR 0.96, p 0.69). The null result held at 12 months (52% vs 51%, RR 1.01) and 6 years (66.3% vs 67.0%), so it is not a short-follow-up artefact."),
    ('b', "**AMI-related cardiogenic shock.** 600 patients at 37 German centres, all with planned early revascularisation (PCI in nearly all); most balloons (86.6%) went in after PCI."),
    ('c', "**IABP is not routinely recommended in cardiogenic shock.** ESC 2023 ACS: routine IABP without mechanical complications class III; IABP for shock from a mechanical complication (VSD, papillary rupture) IIa. ACC/AHA 2025: routine IABP class 3 (no benefit)."),
    ('d', "**Major limitation: only mild to moderate cardiogenic shock was included.** The trial excluded the sickest (CPR >30 min, fixed dilated pupils, no intrinsic cardiac activity), and its 40% mortality was lower than registry figures, though 45% had been resuscitated, so ‘mild’ is the textbook shorthand. Other criticisms: open label, about 10% crossover, and IABP timing and escalation to LVADs left to the operator."),
  ],
  table=dict(title="IABP-SHOCK II risk score (30-day mortality)", head=["Variable", "Cut-off"], rows=[
    ["Age", ">73 years"], ["Prior stroke", "Yes"], ["Admission glucose", ">191 mg/dL (10.6 mmol/L)"], ["Admission creatinine", ">1.5 mg/dL (132.6 µmol/L)"],
    ["TIMI flow after PCI", "<3"], ["Arterial lactate", ">5 mmol/L"],
    ["Score 0–2 / 3–4 / 5–9", "Mortality 23.8% / 49.2% / 76.6%"],
  ]),
  mimic=[("IABP-SHOCK II vs CULPRIT-SHOCK", "IABP-SHOCK II tested the balloon (null); CULPRIT-SHOCK tested culprit-only PCI vs multivessel PCI (culprit-only won).")],
  traps=[("“Prior MI is part of the IABP-SHOCK II score”", "It is not; prior stroke is. The six are age, prior stroke, glucose, creatinine, post-PCI TIMI flow and lactate."),
         ("“IABP-SHOCK II proved the balloon is useless in all shock”", "It showed no benefit from routine use in AMI shock; the most severe shock was not tested, and IABP keeps a IIa role for mechanical complications.")],
  decode=[("IABP-SHOCK II score components: all except? [Marrow]", "Prior MI."),
          ("IABP vs medical therapy in AMI cardiogenic shock — 30-day mortality? [pattern]", "No difference (39.7 vs 41.3%).")],
  punch="IABP-SHOCK II found no survival benefit from the balloon in AMI shock at 30 days, 1 year or 6 years, so routine IABP is class III — with the caveat that the sickest patients were never tested.",
)

L['CS-45'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → Impella mechanism",
  step=2,
  intro="Step 2, the microaxial pump. Impella is a catheter-mounted motor that sits across the aortic valve and lifts blood out of the LV, which is why it unloads the ventricle directly. Not asked directly.",
  parts=[
    ('a', "**Transvalvular axial flow pump placed across the aortic valve.** A small impeller spins at very high speed inside the catheter, like a ship’s propeller in a tube."),
    ('b', "**Displaces blood directly from the LV into the ascending aorta.** Flow is antegrade and in series with the LV, so it lowers LV volume and pressure without raising afterload."),
    ('c', "**Tip in the left ventricle.** The inlet sits in the LV cavity (about 3.5 cm below the aortic valve annulus for the 2.5 and CP) and the outlet in the aortic root; position is checked by echo, because a migrated inlet causes suction and haemolysis."),
    ('d', "**Catheter diameter 9 Fr; peak flow up to 4.3 L/min.** These are Impella CP figures: 9 Fr catheter, 14 Fr pump head (so a 14 Fr sheath). The 2.5 gives 2.5 L/min; the 5.5 gives up to 5.5 L/min via axillary cutdown and is labelled for 14 days (CP for 4 days)."),
  ],
  mimic=[("Impella vs TandemHeart", "Impella drains the LV across the aortic valve; TandemHeart drains the left atrium through the septum.")],
  traps=[("“The 9 Fr catheter means a 9 Fr sheath”", "The pump head is 14 Fr for the CP; the sheath must fit the pump, not the catheter.")],
  decode=[("Axial flow pump placed across the aortic valve? [pattern]", "Impella.")],
  punch="Impella is an axial pump across the aortic valve that draws blood from the LV and delivers it to the ascending aorta — 2.5 to 5.5 L/min depending on the model.",
)

L['CS-46'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → Impella effects",
  step=5,
  intro="Step 5 is matching device to patient, and Impella’s contraindications and signature complication follow from its position across the valve and its spinning rotor. Two Grand Test questions: the contraindication (92% right) and the unique complication (39% right).",
  parts=[
    ('a', "**Significant increase in cardiac output.** Up to 2.5–5.5 L/min by model, delivered whether or not the LV ejects. In DanGer Shock (STEMI shock, Impella CP) 180-day mortality fell from 58.5% to 45.8% (HR 0.74); ACC/AHA 2025 made a microaxial pump class 2a in selected STEMI with severe or refractory shock. ISAR-SHOCK (n 26) had shown better haemodynamics than IABP (cardiac index +0.49 vs +0.11) but the same mortality."),
    ('b', "**Decrease in LVEDP, LV wall stress and myocardial oxygen consumption.** It empties the ventricle in series, so volume, pressure and oxygen demand all fall (CS-41)."),
    ('c', "**Contraindication: mechanical aortic valve.** The catheter must sit across the valve: it can jam a mechanical leaflet or be damaged by it. The label also lists LV mural thrombus (sucked into the pump and embolised), aortic stenosis with an orifice ≤0.6 cm², moderate–severe AR (the pump recirculates the regurgitant blood), severe peripheral arterial disease, ASD or VSD, significant RV failure, LV rupture and tamponade."),
    ('d', "**Risk of haemolysis.** Shear from the rotor, made worse by suction when the LV is underfilled or the inlet is against the wall. Watch plasma free haemoglobin, urine colour and LDH; reposition under echo, give volume or lower the performance level."),
  ],
  mimic=[("Device-specific vs access complication", "Haemolysis comes from the pump; pseudoaneurysm, bleeding and limb ischaemia come from any large femoral sheath.")],
  traps=[("“Pseudoaneurysm or septicaemia is the unique Impella complication” (only 39% chose haemolysis)", "Both happen with any femoral device; haemolysis is the one tied to the Impella rotor."),
         ("“Post-cardiotomy failure or acute myocarditis contraindicates Impella”", "Those are labelled indications; severe aortic stenosis and a mechanical aortic valve are the bars (92% right).")],
  decode=[("Cardiogenic shock with severe AS and prior mechanical AVR: contraindication to Impella? [DocT GT]", "Severe aortic stenosis (92%) — and the mechanical valve itself."),
          ("Unique complication of Impella? [DocT GT]", "Haemolysis (39%).")],
  punch="Impella raises output and unloads the LV, but it cannot cross a mechanical or tightly stenosed aortic valve, and its rotor shears red cells — haemolysis is its signature complication.",
)

L['CS-47'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → TandemHeart",
  step=2,
  intro="Step 2, the left-atrial bypass. TandemHeart takes oxygenated blood from the left atrium and pumps it into the femoral artery, which explains both its effects and its contraindications. One Grand Test question, answered by everyone.",
  parts=[
    ('a', "**Drains oxygenated blood from the left atrium and returns it to the arterial circulation.** It bypasses the LV entirely, so the ventricle is unloaded from upstream."),
    ('b', "**A paracorporeal circuit (next to the body).** The pump sits outside the body but close to it, unlike ECMO’s bedside console."),
    ('c', "**Drainage via a femoral venous cannula passed by transseptal puncture into the LA.** A 21 Fr inflow cannula goes up the IVC and across the atrial septum; this is the only device needing a transseptal puncture, and the hardest to insert."),
    ('d', "**Pump strapped to the leg; return via a femoral arterial cannula.** A 15–19 Fr arterial cannula sends flow retrograde up the aorta, which is why its afterload effect is +++ on CS-51."),
    ('e', "**Significant rise in cardiac output; fall in LVEDP, LV wall stress, LV stroke work and myocardial oxygen consumption.** A centrifugal pump gives about 4–5 L/min. Draining the atrium lowers LV preload, so the LV does less work."),
  ],
  mimic=[("TandemHeart vs VA ECMO", "TandemHeart drains oxygenated blood from the LA and needs no oxygenator; VA ECMO drains venous blood from the RA and oxygenates it.")],
  traps=[("“TandemHeart helps isolated RV failure”", "An LA-to-artery pump needs the right heart to deliver blood to the LA; in RV failure it cannot fill."),
         ("“VSD is fine with TandemHeart”", "Dropping LA and LV pressure reverses the shunt right-to-left and causes hypoxaemia; VSD, severe PVD, LA thrombus and moderate–severe AR are contraindications.")],
  decode=[("Not a contraindication to TandemHeart: PVD, LV failure, VSD, RV failure? [DocT GT]", "LV failure — it is the indication (100%)."),
          ("Device needing transseptal puncture? [pattern]", "TandemHeart.")],
  punch="TandemHeart drains the left atrium through the septum and returns blood to the femoral artery, so it needs a working right heart, an intact septum and good femoral vessels.",
)

L['CS-48'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → Venoarterial ECMO",
  step=2,
  intro="Step 2, the full bypass. VA ECMO is the only device that adds an oxygenator, so it supports both heart and lungs, but its peripheral form pumps against the LV. Not asked directly.",
  parts=[
    ('a', "**Blood drawn from the venous system, oxygenated, and pumped into the arterial circulation.** Peripheral: femoral vein to the right atrium, through a centrifugal pump and membrane oxygenator, back into the femoral artery and retrograde up the aorta at 4–6 L/min."),
    ('b', "**Partial or complete support to the heart, and oxygenation of the blood.** It replaces right and left heart output and lung gas exchange, so it suits shock with arrest, biventricular failure or severe hypoxaemia (ECPR). ECLS-SHOCK (2023) found no 30-day mortality benefit from early routine use in AMI shock (47.8 vs 49.0%) with more bleeding, and ACC/AHA 2025 made routine VA-ECMO class 3."),
  ],
  mimic=[("VA vs VV ECMO", "VA returns blood to an artery and supports the circulation; VV returns it to a vein and supports only gas exchange.")],
  traps=[("“VA ECMO unloads the failing LV”", "Retrograde flow raises afterload; the LV may distend and need venting (CS-52).")],
  decode=[("MCS device that also provides oxygenation? [pattern]", "VA ECMO.")],
  punch="VA ECMO takes venous blood, oxygenates it and pumps it into the arteries, so it supports both ventricles and the lungs — at the cost of LV afterload.",
)

L['CS-49'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → Device mechanism and insertion",
  step=2,
  intro="Step 2 in one table: what drives each device and how it goes in. The one linked question (an IABP practicalities question, also on CS-42) turns on insertion: the femoral artery has to be big enough.",
  parts=[
    ('a', "**IABP: pneumatic; percutaneous via the femoral artery.** A console shuttles helium in and out of the balloon. Small 7–8 Fr sheath; femoral artery ≥4 mm; balloon sized to the patient’s height."),
    ('b', "**TandemHeart: centrifugal, paracorporeal; percutaneous femoral artery and vein with transseptal puncture, or IJ vein with a trans-pulmonary route.** The femoral transseptal route is the left-sided set-up: LA blood to the femoral artery. The internal jugular route is the right-sided set-up: a dual-lumen cannula (ProtekDuo) placed through the right IJ drains the right atrium and returns blood into the pulmonary artery, so the same pump supports the RV."),
    ('c', "**Impella: axial, transvalvular; percutaneous or peripheral surgical.** CP goes in percutaneously through the femoral artery; the 5.5 needs a surgical cutdown with a graft on the axillary artery."),
    ('d', "**VA ECMO: centrifugal, extracorporeal; percutaneous or peripheral surgical.** Femoral cannulae are usually placed percutaneously; open cut-down is used when vessels are small or diseased."),
    ('e', "**Surgical VAD: centrifugal, extracorporeal; central surgical access.** Cannulae go directly into the heart and great vessels through a sternotomy, so it needs a surgeon and an operating theatre."),
  ],
  mimic=[("Pneumatic vs rotary", "Only the IABP is pneumatic and moves no blood of its own; all the others spin a rotor (axial in Impella, centrifugal in the rest).")],
  traps=[("“An IABP needs a 13–14 Fr sheath”", "That is the Impella CP; the IABP uses 7–8 Fr through a femoral artery of at least 4 mm (46% got this right).")],
  decode=[("IABP: which is true — femoral artery >4 mm? [DocT GT]", "Yes — minimum femoral artery size above 4 mm (46%)."),
          ("Only axial-flow device? Only pneumatic device? [pattern]", "Impella; IABP.")],
  punch="IABP is pneumatic, Impella axial, and the rest centrifugal; all but the surgical VAD can go in percutaneously, and TandemHeart alone needs a transseptal puncture.",
)

L['CS-50'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → Ventricle supported and flow",
  step=5,
  intro="Step 5 begins the comparison: which ventricle each device helps and how much flow it adds. Flow is the first filter when choosing a device for worsening shock. Not asked directly.",
  parts=[
    ('a', "**IABP LV; TandemHeart LV or RV; Impella LV or RV; VA ECMO LV and RV; surgical VAD LV and/or RV.** TandemHeart and Impella have right-sided versions (an RA-to-PA circuit; Impella RP), but each configuration supports one side; only VA ECMO supports both at once from one circuit."),
    ('b', "**Flow: IABP 0.5–1, TandemHeart 4, Impella 2.5–5, VA ECMO >5, surgical VAD >5 L/min.** The IABP only augments; the rotary pumps generate their own flow, rising with pump size from Impella 2.5 to 5.5 and up to full output with ECMO or a surgical VAD."),
  ],
  mimic=[("Biventricular support", "VA ECMO supports both ventricles together; a surgical VAD can be an LVAD, RVAD or BiVAD.")],
  traps=[("“Impella and TandemHeart give the same flow as ECMO”", "They give 2.5–5 and about 4 L/min; only ECMO and surgical VADs exceed 5 L/min.")],
  decode=[("Device providing the least flow? Device supporting both ventricles together? [pattern]", "IABP (0.5–1 L/min); VA ECMO.")],
  punch="Flow climbs from under 1 L/min on the IABP to 2.5–5 on Impella, about 4 on TandemHeart and over 5 on VA ECMO and surgical VADs, and only VA ECMO supports both ventricles at once.",
)

L['CS-51'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → Afterload, gas exchange and risk",
  step=5,
  intro="Step 5, the costs: afterload, gas exchange and complications. The table follows from where each device returns its blood. Not asked directly.",
  parts=[
    ('a', "**Afterload: IABP – (reduces); TandemHeart +++; Impella none; VA ECMO +++; surgical VAD none.** Retrograde femoral return (TandemHeart, peripheral ECMO) pushes against the LV; antegrade return into the ascending aorta (Impella, central VAD) does not; systolic deflation (IABP) lowers it."),
    ('b', "**Gas exchange: none except TandemHeart possible and VA ECMO +++.** An oxygenator can be spliced into the TandemHeart circuit; ECMO has one by design."),
    ('c', "**Limb ischaemia: IABP +, TandemHeart +++, Impella ++, VA ECMO +++, surgical VAD variable.** Risk tracks the arterial sheath size; ECMO needs a distal perfusion cannula to protect the leg."),
    ('d', "**Haemorrhage: IABP +, TandemHeart +++, Impella +++, VA ECMO +++, surgical VAD ++.** Large-bore access plus full anticoagulation; in ECLS-SHOCK moderate or severe bleeding was 23.4% vs 9.6%."),
  ],
  mimic=[("Retrograde vs antegrade return", "Retrograde (femoral artery) raises afterload; antegrade (ascending aorta) does not.")],
  traps=[("“All pumps raise afterload because they add flow to the aorta”", "Only retrograde femoral return raises it; Impella’s antegrade flow does not, and the IABP lowers it.")],
  decode=[("Which device reduces afterload? Which has the lowest bleeding and limb risk? [pattern]", "IABP for both.")],
  punch="Where the blood re-enters decides the afterload: the IABP lowers it, Impella and central VADs leave it, and femoral TandemHeart and ECMO raise it; the IABP is also the gentlest on limbs and bleeding.",
)

L['CS-52'] = dict(
  sub="Cardiogenic shock → Mechanical circulatory support → The ECMO paradox",
  step=3,
  intro="Step 3’s key contrast: VA ECMO gives the most flow yet does the least for the left ventricle. Not asked directly, but it is the reasoning behind LV venting and behind the ‘ECPELLA’ combination.",
  parts=[
    ('a', "**More flow: VA ECMO (>5 L/min) vs Impella 2.5–5 L/min.** ECMO can replace the whole cardiac output."),
    ('b', "**Impella unloads and cuts stroke work significantly; VA ECMO fails to unload and increases stroke work (MVO2 unchanged or rising).** ECMO’s retrograde flow raises aortic pressure; a weak LV then ejects less, end-diastolic pressure rises, the aortic valve may stop opening, and the LV distends with pulmonary oedema and stasis thrombus. The fixes are venting: IABP, Impella (ECPELLA) or atrial septostomy."),
    ('c', "**Arterial elastance increases on peripheral ECMO.** A steeper Ea line on the PV loop is the picture of the higher afterload (CS-40)."),
    ('d', "**Gas exchange: VA ECMO +++, the only device.** It is the only one built with an oxygenator; TandemHeart can have one added (CS-51)."),
  ],
  mimic=[("ECMO with a distending LV vs recovering LV", "Loss of pulsatility, a closed aortic valve and rising wedge pressure mean the LV needs venting; returning pulsatility means it is recovering.")],
  traps=[("“The device with the highest flow best protects the ischaemic heart”", "VA ECMO perfuses the body but raises LV afterload and oxygen demand; Impella offers less flow but unloads.")],
  decode=[("Patient on peripheral VA ECMO develops pulmonary oedema and a non-opening aortic valve — mechanism? [pattern]", "Raised afterload from retrograde flow, LV distension; vent the LV.")],
  punch="VA ECMO delivers the most flow and the only gas exchange, but its retrograde flow raises afterload so the LV works harder, while Impella delivers less flow and genuinely unloads.",
)

L['CS-53'] = dict(
  sub="Cardiogenic shock → Beyond temporary support → Indications for cardiac transplantation",
  step=6,
  intro="Step 6 is where the bridge leads when the heart does not recover. Transplant is for end-stage disease of any of three kinds. Not asked directly.",
  parts=[
    ('a', "**Advanced heart failure from ischaemic heart disease or dilated cardiomyopathy.** These two make up most adult transplants."),
    ('b', "**Diastolic dysfunction from restrictive or hypertrophic cardiomyopathy.** A stiff, small ventricle is poorly suited to an LVAD (there is little cavity to drain and the inflow cannula sucks down), so transplant is usually the only replacement."),
    ('c', "**Heart failure from congenital heart disease.** Failing single-ventricle or systemic-RV circulations reach a point where only a new heart helps."),
  ],
  mimic=[("Transplant vs LVAD candidates", "Dilated, ischaemic hearts can take either; restrictive or hypertrophic hearts with small cavities usually need transplant.")],
  traps=[("“Restrictive cardiomyopathy is an LVAD indication”", "A small, stiff cavity gives the pump nothing to drain; transplant is the option.")],
  decode=[("Indications for cardiac transplantation: all except? [pattern]", "The three are advanced ischaemic/dilated HF, restrictive/hypertrophic diastolic failure and congenital heart disease.")],
  punch="Transplant is for end-stage systolic failure (ischaemic or dilated), diastolic failure (restrictive or hypertrophic) and failed congenital hearts.",
)

L['CS-54'] = dict(
  sub="Cardiogenic shock → Beyond temporary support → Long-term MCS",
  step=6,
  intro="Step 6, the durable pump. An implantable LVAD is the alternative when there is no heart to transplant or the patient cannot have one. Not asked directly.",
  parts=[
    ('a', "**Implantable LVADs may be an alternative to heart transplantation.** As destination therapy for patients who are not candidates, or a bridge while they wait."),
    ('b', "**The little data beyond 2 years suggests they are not as good as transplantation.** That was true of older pumps; MOMENTUM 3 now gives 5-year data for the HeartMate 3: survival 58.4% (vs 43.7% for the older axial HeartMate II). Transplant still does better, with a median survival of about 12.5 years in the ISHLT registry, so the card’s conclusion stands even though the data gap has closed."),
  ],
  mimic=[("Destination therapy vs bridge to transplant", "Same pump; the difference is whether a donor heart is expected (CS-37).")],
  traps=[("“A modern LVAD matches transplant survival”", "Five-year LVAD survival is around 58%, well below transplant.")],
  decode=[("LVAD vs transplant long-term outcome? [pattern]", "LVAD inferior; transplant remains the better long-term option.")],
  punch="A durable LVAD is an alternative to transplant, not an equal: even the best pump gives about 58% survival at five years.",
)

L['CS-55'] = dict(
  sub="Cardiogenic shock → Beyond temporary support → Management algorithm",
  step=6,
  intro="Step 6 ties the deck together: the AHA (2017) hub-and-spoke ladder that runs from drugs to a durable pump, with recovery and palliation as exits. Not asked directly.",
  parts=[
    ('a', "**Spoke hospital → cardiogenic shock hub hospital.** Spokes stabilise and transfer; hubs offer 24/7 cath lab, MCS, surgery and transplant/LVAD services. Higher-volume centres have lower shock mortality."),
    ('b', "**Rung 1, resuscitation and medical therapy: inotropes/vasopressors, mechanical ventilation, aetiology-specific medical therapy.** Norepinephrine for pressure, an inotrope for low output (CVS03)."),
    ('c', "**Rung 2, reperfusion for ACS only: PCI, CABG, fibrinolysis.** Only shock caused by infarction has a culprit to open. Early revascularisation was the first treatment shown to improve survival (SHOCK, at 6 and 12 months), and CULPRIT-SHOCK showed culprit-only PCI beats immediate multivessel PCI."),
    ('d', "**Rung 3, temporary MCS: IABP, peripheral VAD, ECMO, implantable VAD.** Chosen by the flow and unloading needed (CS-50, CS-51); routine IABP and routine VA-ECMO are class 3 in ACC/AHA 2025, a microaxial pump 2a in selected STEMI shock."),
    ('e', "**Rung 4, durable VAD: transplant or destination VAD.** For the heart that does not recover."),
    ('f', "**Recovery and palliation are exits at every rung, in both directions.** A patient may wean at any rung, or the team may decide escalation no longer serves the patient."),
  ],
  mimic=[("Temporary vs durable MCS rung", "Temporary devices bridge (days to weeks); durable VADs are destinations or long bridges to transplant.")],
  traps=[("“Reperfusion is a step for every cardiogenic shock”", "Only for ACS; shock from myocarditis or cardiomyopathy skips to temporary MCS.")],
  decode=[("Which rung applies only to ACS? [pattern]", "Reperfusion (PCI, CABG, fibrinolysis).")],
  punch="The ladder runs medical therapy, reperfusion for ACS only, temporary MCS, then transplant or a destination VAD, with recovery and palliation open at every rung.",
)

FLAGS = {
  'CS-37': "Watch line: ‘ALL FOUR are short-term MCS’ is too absolute. In ESC HF terminology bridge to transplant (and sometimes bridge to recovery) is often a durable LVAD; the strategy names the destination, not the device.",
  'CS-41': "a: ‘WIDER PV loop area’ is loose. The IABP widens the loop (larger stroke volume) but lowers its peak pressure, so the area (stroke work) and oxygen consumption fall modestly, as CS-43 says. ‘Wider loop’ is accurate; ‘larger area’ is not.",
  'CS-44': "d: ‘only mild to moderate cases’ is textbook shorthand. IABP-SHOCK II excluded only the extremes (CPR >30 min, fixed dilated pupils, no intrinsic cardiac activity), 45% had been resuscitated and 30-day mortality was about 40%; ‘the most severe shock was not tested’ is the accurate form.",
  'CS-49': "TandemHeart row: ‘IJ vein + trans-pulmonary vein’ is garbled. The IJ route is the right-sided configuration (ProtekDuo dual-lumen cannula, RA → pulmonary artery); there is no standard trans-pulmonary-vein route.",
  'CS-54': "b: ‘little data beyond 2 years’ is dated. MOMENTUM 3 (JAMA 2022) reports 5-year HeartMate 3 survival of 58.4%. The conclusion (inferior to transplant) still holds.",
}
