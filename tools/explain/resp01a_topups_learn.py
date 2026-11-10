# RESP01A top-up cards — Explain v3 ("Learn" depth), same fields and voice as resp01a_learn.py.
# Fields: sub, step (index into resp01a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from map/out/all_rows.json (the top-up's own src) plus related questions under the parent cards in qpack/RESP01A.md.
T = {}

T['T_d0febbed'] = dict(
  sub="Respiratory → ARDS → Goals of support in hypoxaemic failure",
  step=3,
  intro="Step 3 explains why the hypoxaemia of ARDS comes from shunt and why the aerated lung is small. Support therefore has a cost at every point: more PEEP, more volume and more fluid each help one number and harm something else. The goals on this card (from Principles of Critical Care) are all written as the least that is enough.",
  parts=[
    ('a', "**Least PEEP that gives SpO₂ ≥90% on FiO₂ <0.6.** SpO₂ 90% sits near PaO₂ 60 mmHg, the shoulder of the dissociation curve, so higher targets add little oxygen content. FiO₂ is kept below 0.6 to limit oxygen toxicity and absorption collapse, and PEEP is the tool that lets FiO₂ come down; beyond what is needed it overdistends the open lung and cuts venous return."),
    ('b', "**Least VT/plateau pressure compatible with pH >7.2 (accept hypercapnia).** The baby lung (ARDS-10) is overstretched by normal tidal volumes, so CO₂ is allowed to rise; a pH above about 7.2 is well tolerated by most patients. This is the logic behind ARMA’s 6 mL/kg and plateau ≤30 (RESP01B)."),
    ('c', "**Least circulating volume/PAWP that keeps adequate O₂ delivery and urine output.** A leaky capillary floods with oedema in proportion to hydrostatic pressure, so the lowest filling that keeps cardiac output, oxygen delivery and kidneys perfused is the target; once shock has resolved, a conservative fluid strategy shortens ventilation (FACTT)."),
  ],
  mimic=[],
  traps=[
    ("“The goal is a normal PaCO₂ and pH”", "Hypercapnia is accepted to protect the lung; the floor is pH about 7.2, not 7.35."),
    ("“Push PEEP until SpO₂ is 100%”", "The aim is the least PEEP for SpO₂ about 90% on a non-toxic FiO₂; more risks overdistension and hypotension."),
  ],
  decode=[
    ("Therapeutic goals in acute hypoxaemic respiratory failure — which is NOT one? [Marrow]", "None: least PEEP, least VT and least volume are all goals."),
    ("Which target is acceptable in a ventilated ARDS patient: PaCO₂ 60 with pH 7.25? [pattern]", "Yes — permissive hypercapnia within pH >7.2."),
  ],
  punch="Every lever in hypoxaemic failure is set to the least that works: enough PEEP for SpO₂ about 90% on FiO₂ under 0.6, enough volume for pH above 7.2, enough fluid for perfusion.",
)

FLAGS = {}
