# ENDO02B top-up cards — Explain v3 ("Learn" depth), same fields and voice as endo02b_learn.py.
# Fields: sub, step (index into endo02b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source question: DocT Grand Test CGT6 (the top-up’s own src). Figures from standard physiology (Henderson–Hasselbalch, Winter’s formula), worked here by arithmetic; checked 22 Nov 2026.
# Second review 22 Nov 2026: arithmetic re-checked (1.5 × 5 + 8 ≈ 15; pH 7.15 at PaCO2 15, 6.72 at 40); apnoea sentence made precise.
T = {}

T['T_6f96ae33'] = dict(
  sub="Endocrine → Hyperglycaemic crises → Intubating severe DKA",
  step=6,
  intro="Step 6 deals with complications, and intubating a severe DKA patient is one of the most dangerous moments of the whole episode. The patient is staying alive by breathing off huge amounts of CO2; the risk is that the ventilator, or the apnoea of induction, takes that compensation away.",
  parts=[
    ('a', "**The indication is impending respiratory-muscle fatigue: the huge compensatory minute ventilation is what keeps the pH survivable.** Expected PaCO2 in metabolic acidosis is about 1.5 × bicarbonate + 8 (Winter’s formula), so a bicarbonate of 5 needs a PaCO2 near 15 mmHg. That takes a minute ventilation several times normal, which tiring muscles cannot keep up; drowsiness, a rising PaCO2 or a PaCO2 above the expected value means compensation is failing."),
    ('b', "**Ventilation does not correct the metabolic acidosis itself.** It only takes over the compensation. The acid is removed by fluid and insulin stopping ketogenesis (DKA-14), so intubation buys time and does not treat the cause."),
    ('c', "**Trap: a ‘normal’ ventilator rate lets PaCO2 rise and the pH crash; set a high minute ventilation (RR 25–30 or more) matching the pre-intubation PaCO2.** With bicarbonate 5, a PaCO2 of 15 gives a pH of about 7.15; if a routine rate lets PaCO2 drift up to 40, the pH falls to about 6.7, with arrhythmia and arrest. Note the PaCO2 before induction, set the rate to match it, and check a blood gas within minutes."),
    ('d', "**Keep apnoea at induction as short as possible; even a minute can drop the pH sharply and precipitate arrest.** During apnoea CO2 accumulates at several mmHg a minute, and with bicarbonate near 5 there is almost no buffer to absorb it, so each mmHg moves the pH much further than in a normal patient. Preoxygenate, use a rapid-sequence technique with a haemodynamically stable induction agent, and start high-rate ventilation immediately after the tube is placed."),
  ],
  mimic=[
    ("Respiratory fatigue in DKA vs falling respiratory rate from recovery", "Recovery: pH and bicarbonate rising, so the drive falls naturally. Fatigue: pH static or falling with PaCO2 rising above the expected value."),
  ],
  traps=[
    ("“Intubate and ventilate to correct the acidosis”", "Ventilation only replaces the patient’s own compensation; fluid and insulin correct the acidosis."),
    ("“Standard settings, rate 12–14” after intubation", "This lets PaCO2 rise towards 40 and the pH fall towards 6.7; the rate must match the pre-intubation compensation."),
  ],
  decode=[
    ("Severe DKA, pH 7.08, tiring despite maximal breathing: why intubate, and the ventilator trap [DocT GT]", "Impending muscle fatigue; match the pre-intubation PaCO2 with a high minute ventilation and keep apnoea short."),
    ("[pattern] DKA intubated, ventilator rate 14, pH falls from 7.10 to 6.85 within 30 minutes", "PaCO2 has risen; increase the rate to restore the pre-intubation PaCO2."),
  ],
  punch="In severe DKA the patient’s own breathing is the buffer, so intubate only for fatigue, keep apnoea to seconds, and set a high ventilator rate that matches the pre-intubation PaCO2, or the pH will crash.",
)

FLAGS = {}
