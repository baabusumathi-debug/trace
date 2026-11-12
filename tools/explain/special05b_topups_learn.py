# SPECIAL05B top-up cards — Explain v3 ("Learn" depth), same fields and voice as special05b_learn.py.
# Fields: sub, step (index into special05b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source: trace/test/data/qbank.json → topups["SPECIAL05B"]: T_356f55ec (compartment syndrome, 5 links: DocT GT ×4, Marrow QB61-Q08), T_9f6a04d7 (post-splenectomy vaccination, DocT GT:130),
# T_c9721678 (VTE prophylaxis in major trauma, DocT GT:53). The source stems were not opened; decode items follow the top-up questions.
# Checked online 13 Nov 2026: PREVENT CLOT (NEJM 2023, 12,211 fracture patients): aspirin 81 mg twice daily non-inferior to enoxaparin 30 mg twice daily for 90-day death (0.78% vs 0.73%),
# DVT 2.51% vs 1.71%, PE 1.49% each, bleeding similar.
# Reviewer checked online 13 Nov 2026: McQueen 1996 (delta-P = diastolic − compartment, decompress under 30 mmHg); Shatz 1998 (better functional antibody at 14 days, IgG similar); Geerts 1996
# (NEJM: both 12-hourly, DVT 44% vs 31%, proximal 15% vs 6%); ACIP 2024 (PCV21 or PCV20 alone, or PCV15 then PPSV23 ≥8 weeks in immunocompromise incl. asplenia); European 6th edition Rec 37.
# From standard references without a fresh check (confident): McQueen 1996 delta-P (diastolic − compartment pressure) <30 mmHg; fasciotomy within about 6 h; Shatz 1998 (vaccination at 14 days
# gives better functional antibody); ACIP 2022 adult pneumococcal schedule (PCV20 alone, or PCV15 then PPSV23 at ≥8 weeks for asplenia); OPSI mortality up to about 50%; Geerts 1996
# (enoxaparin 30 mg 12-hourly vs UFH 5000 U 12-hourly: DVT 31% vs 44%, proximal 6% vs 15%); EAST guidance on LMWH within 24–48 h once bleeding is controlled.

T = {}

T['T_356f55ec'] = dict(
  sub="Polytrauma → Limb → Acute compartment syndrome",
  step=4,
  intro="Step 4 was stopping the bleeding; this is the limb complication that follows a fracture, a crush or reperfusion of an ischaemic limb. Bleeding and oedema inside a closed fascial compartment raise its pressure until capillary flow stops, and muscle and nerve die within hours. Five bank questions (four DocT GT, one Marrow) test the early signs, the pressure that matters and the response.",
  parts=[
    ('a', "**Commonest after a closed tibial fracture or crush. Early signs: pain out of proportion and on passive stretch, a tense compartment, paraesthesia; pulses and pallor are LATE.** The leg’s anterior compartment is tight and the tibia is the commonest fracture behind it. Compartment pressure needed to stop capillary flow is far below arterial pressure, so the distal pulse stays present while the muscle is dying; waiting for pulselessness means waiting for necrosis."),
    ('b', "**Remove all circumferential dressings and splints at once.** A cast, bandage or splint adds external pressure to the compartment; splitting the cast down to the skin can lower pressure markedly. The limb is kept at heart level, not elevated, because elevation lowers the arterial pressure driving flow."),
    ('c', "**Unreliable examination (sedated, obtunded) → measure: delta-P = DIASTOLIC BP − compartment pressure; an absolute pressure over 30 alone ignores perfusion; measurement is an adjunct, not infallible.** Perfusion depends on the gradient, so a pressure of 30 is dangerous in a hypotensive patient and tolerable in a hypertensive one. In the ICU patient who cannot report pain, measurement (or repeated measurement) replaces the history."),
    ('d', "**Not relieved, or delta-P under 30 mmHg → emergency fasciotomy (ideally within 6 hours).** Muscle tolerates about 4–6 hours of ischaemia before irreversible necrosis. Fasciotomy opens all compartments (four in the leg), and the wounds are left open. Afterwards, watch for rhabdomyolysis and hyperkalaemia."),
    ('e', "**Never more opioids, and never delay for imaging.** Escalating analgesic need is itself a warning sign, and treating it hides the diagnosis; regional blocks can mask it too. Compartment syndrome is a clinical diagnosis: X-ray, Doppler or MRI only waste the time the muscle has."),
  ],
  mimic=[
    ("Compartment syndrome vs arterial injury", "Arterial injury: pulse lost early, cold pale limb. Compartment syndrome: pulse present until late, with pain on passive stretch."),
    ("Delta-P vs absolute compartment pressure", "Delta-P (diastolic minus compartment) under 30 mmHg is the threshold; an absolute pressure of 30 ignores the patient’s blood pressure."),
  ],
  traps=[
    ("“A palpable pulse excludes compartment syndrome”", "Pulses are lost late; pain on passive stretch is early."),
    ("“Compartment pressure over 30 is the fasciotomy threshold”", "Use delta-P: diastolic pressure minus compartment pressure under 30."),
    ("“Elevate the limb and give more analgesia”", "Remove dressings, keep the limb at heart level, and decompress; rising opioid need is a warning."),
  ],
  decode=[
    ("Tibial fracture, pain out of proportion, pain on passive stretch, pulses present — next step? [DocT GT]", "Remove dressings and decompress (fasciotomy), not more opioids or imaging."),
    ("Sedated patient, tense calf — which measurement decides? [DocT GT, Marrow]", "Delta-P = diastolic BP − compartment pressure; under 30 → fasciotomy."),
  ],
  punch="Compartment syndrome is diagnosed by pain on passive stretch while pulses are still present, measured by delta-P (diastolic minus compartment pressure) in the sedated, and treated by removing dressings and fasciotomy within about 6 hours.",
)

T['T_9f6a04d7'] = dict(
  sub="Polytrauma → After surgery → Post-splenectomy vaccination",
  step=4,
  intro="Step 4 includes splenectomy for an uncontrollable splenic bleed. Without a spleen, the patient cannot clear encapsulated bacteria well, so vaccination is part of the operation’s aftercare. One DocT GT question asks the timing after an emergency splenectomy.",
  parts=[
    ('a', "**Vaccinate 14 days or more after surgery (better response), or before discharge if follow-up is doubtful; for elective splenectomy, at least 2 weeks BEFORE.** Antibody responses are better when vaccination is delayed to about 2 weeks after the operation, probably because surgery and trauma blunt the immune response. If the patient may not return, an earlier dose is better than none."),
    ('b', "**Pneumococcal (PCV20, or PCV15 then PPSV23 at least 8 weeks later), meningococcal ACWY and B, Hib, and yearly influenza.** PCV21 alone is now also accepted (ACIP 2024). These cover the encapsulated organisms the spleen normally clears (pneumococcus above all, then meningococcus and Haemophilus). Influenza is added because it predisposes to secondary pneumococcal infection. Antibiotic prophylaxis and a standby course are usually advised as well."),
    ('c', "**Asplenia → overwhelming post-splenectomy infection (encapsulated organisms), mortality about 50%.** The spleen filters unopsonised bacteria and makes IgM against polysaccharide capsules. Without it, sepsis from pneumococcus can progress from fever to purpura fulminans and death within hours, and the risk lasts for life."),
  ],
  mimic=[
    ("Emergency vs elective splenectomy", "Emergency: vaccinate at about 14 days after surgery. Elective: at least 2 weeks before."),
  ],
  traps=[
    ("“Vaccinate on day 1 after emergency splenectomy”", "Responses are better at 14 days; vaccinate earlier only if the patient may not return."),
    ("“Pneumococcal vaccine alone is enough”", "Meningococcal, Hib and yearly influenza vaccines are also given."),
  ],
  decode=[
    ("After emergency splenectomy, vaccinate at how many days? [DocT GT]", "14 days."),
  ],
  punch="After emergency splenectomy, vaccinate at about 14 days (or before discharge if follow-up is uncertain) against pneumococcus, meningococcus, Hib and influenza, because overwhelming post-splenectomy infection kills about half of those it affects.",
)

T['T_c9721678'] = dict(
  sub="Polytrauma → Drugs → VTE prophylaxis in major trauma",
  step=6,
  intro="Step 6 covers drugs given during bleeding; this is the drug given after it stops. Trauma patients swing from the early coagulopathy of step 2 to a prothrombotic state within a day or two, and DVT is common without prophylaxis. One DocT GT question asks the first-line agent.",
  parts=[
    ('a', "**LMWH: enoxaparin 30 mg SC 12-hourly (or 40 mg 12-hourly or anti-Xa guided), started within 24–48 h once bleeding is controlled.** Trauma patients often have low anti-Xa levels on standard doses (oedema, high clearance), so twice-daily or weight- or anti-Xa-adjusted dosing is used. Starting is timed against bleeding risk: once haemorrhage is controlled and, in TBI or solid organ injury, once imaging is stable. The European trauma guideline (6th edition) recommends drug prophylaxis plus IPC within 24 hours of bleeding control (Grade 1B)."),
    ('b', "**It beats UFH 5000 U 8-hourly (fewer DVT and PE, less HIT).** In the trial by Geerts (1996), enoxaparin 30 mg 12-hourly reduced DVT compared with UFH 5000 U 12-hourly (31% vs 44%; proximal DVT 6% vs 15%), with no significant excess of major bleeding; the trial was not powered for PE. Heparin-induced thrombocytopenia is also less frequent with LMWH. UFH remains the choice in severe renal failure."),
    ('c', "**IPC alone only while drug prophylaxis is contraindicated; fondaparinux for HIT.** Mechanical compression is a bridge for the patient still bleeding, not an equal alternative. In fracture patients, PREVENT CLOT (NEJM 2023) found aspirin 81 mg twice daily non-inferior to enoxaparin for death at 90 days, though with slightly more DVT."),
  ],
  mimic=[
    ("LMWH vs UFH in trauma", "LMWH: fewer DVT, less HIT, first line. UFH: for renal failure or when rapid reversal may be needed."),
  ],
  traps=[
    ("“UFH 5000 U is first line in major trauma”", "LMWH is, with normal renal function."),
    ("“Compression devices alone are equivalent”", "Only while drug prophylaxis is contraindicated."),
  ],
  decode=[
    ("First-line VTE prophylaxis in major trauma with normal renal function? [DocT GT]", "LMWH (enoxaparin 30 mg twice daily)."),
  ],
  punch="Once bleeding is controlled, usually within 24–48 hours, give LMWH (enoxaparin 30 mg twice daily) rather than UFH; compression devices are only a bridge while drugs are contraindicated.",
)

FLAGS = {
  'T_356f55ec': "Line 4: ‘delta-P under 30 mmHg’ uses the McQueen diastolic gradient; some sources use MAP minus compartment pressure under 30–40. ‘Ideally within 6 h’ is standard teaching. The linked stems were not opened.",
  'T_9f6a04d7': "Line 2: ACIP since 2024 also accepts PCV21; the schedule given is the 2022 ACIP version. ‘Mortality about 50%’ is the commonly quoted figure for established OPSI (range about 40–70%).",
  'T_c9721678': "Line 2 compares with UFH 8-hourly; the Geerts trial used UFH 5000 U 12-hourly, and showed fewer DVT (total and proximal), not fewer PE (not powered for it). European 6th edition: drug prophylaxis plus IPC within 24 h of bleeding control. PREVENT CLOT (aspirin alternative in fracture patients) is added in the explanation.",
}
