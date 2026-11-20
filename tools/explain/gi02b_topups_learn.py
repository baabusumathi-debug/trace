# GI02B top-up cards — Explain v3 ("Learn" depth), same fields and voice as gi02b_learn.py.
# Fields: sub, step (index into gi02b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source question: the top-up's own src (DocT:22). Checked online 20 Nov 2026 (and confirmed by the second reviewer: Intern Emerg Med 2023 systematic review, 148 papers, 68 cohorts): pooled incidence 11% of all AP, mortality 43%;
# the card's ~10–20% refers to severe AP, where published series vary widely, so it is restated, not sharpened.
T = {}

T['T_305a0e05'] = dict(
  sub="Acute pancreatitis → Organ failure → Pancreatic encephalopathy",
  step=4,
  intro="Step 4 is about organs failing outside the pancreas, and the brain is the one most often missed. A patient with severe necrotising pancreatitis who becomes confused in the first fortnight has several possible causes, and some of them can be reversed within hours, so the question is less about naming the syndrome than about what to exclude first.",
  parts=[
    ('a', "**Pancreatic encephalopathy: about 10–20% of severe acute pancreatitis, usually in the first 2 weeks.** It comes with the early SIRS phase: fluctuating confusion, agitation, hallucinations, disorientation and sometimes myoclonus or seizures. A 2023 meta-analysis of 68 cohorts found it in 11% of all pancreatitis, with a pooled mortality of 43%, mostly because it marks severe disease."),
    ('b', "**Mechanism: circulating phospholipase A2 and lipase demyelinate, plus cytokines and microcirculatory injury.** The same phospholipase A2 that digests surfactant (PANC-20) attacks the phospholipids of myelin once cytokines open the blood–brain barrier; MRI may show white-matter change."),
    ('c', "**Exclude Wernicke’s (usually later, over 2 weeks; alcohol, vomiting, TPN), withdrawal, low calcium, glucose or sodium, sepsis and drugs.** Pancreatic encephalopathy is a diagnosis of exclusion. Wernicke’s comes later, after weeks of vomiting, poor intake or glucose-containing fluids without thiamine; alcohol withdrawal peaks at 2–3 days after the last drink; hypocalcaemia, hypoglycaemia and hyponatraemia are measured and corrected; sepsis and sedatives are looked for."),
    ('d', "**Treat the pancreatitis and give empirical thiamine.** There is no specific treatment; it improves as the pancreatitis settles. Thiamine is safe and cheap and Wernicke’s cannot be excluded at the bedside, so it is given before glucose."),
  ],
  mimic=[
    ("Pancreatic encephalopathy vs Wernicke’s", "PE is early (first 2 weeks) with SIRS; Wernicke’s is later, after malnutrition, and responds to thiamine."),
    ("Pancreatic encephalopathy vs alcohol withdrawal", "Withdrawal starts 6–24 hours and peaks 2–3 days after the last drink, with tremor and autonomic overactivity."),
  ],
  traps=[
    ("“Confusion on day 5 of severe pancreatitis is Wernicke’s”", "Wernicke’s usually appears after 2 weeks; at day 5 pancreatic encephalopathy is likelier, but thiamine is still given."),
  ],
  decode=[
    ("Day 5 of severe necrotising AP, fluctuating confusion, agitation, myoclonus [DocT GT]", "Pancreatic encephalopathy; exclude Wernicke’s, withdrawal, metabolic causes and sepsis, give thiamine."),
  ],
  punch="Early confusion in severe pancreatitis is usually pancreatic encephalopathy from phospholipase A2 and cytokines, but it is diagnosed only after Wernicke’s, withdrawal, metabolic causes and sepsis are excluded, and thiamine is given anyway.",
)
