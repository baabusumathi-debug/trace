# GI07B top-up cards — Explain v3 ("Learn" depth), same fields and voice as gi07b_learn.py.
# Fields: sub, step (index into gi07b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Parts follow the lines of the top-up's answer in order (a, b, c…); each starts with the line restated in bold. Disagreements with a card go in FLAGS, not in the text.
# Source: gi_topups.json["GI07B"]: T_584f592f (pallidal manganese in cirrhosis, 1 link: DocT:18). The source stem was not opened; the decode item follows the top-up question.
# From standard references without a fresh check (confident): bilateral symmetric T1 pallidal hyperintensity in 70–90% of cirrhotics from manganese deposition, related to portosystemic
# shunting and biliary excretion; acquired hepatocerebral degeneration with parkinsonism; regression after transplant; Wilson disease ‘face of the giant panda’ on T2 in the midbrain,
# with T2 hyperintensity of putamen and thalami.
T = {}

T['T_584f592f'] = dict(
  sub="GI → Cirrhosis → Hepatic encephalopathy → Pallidal manganese on MRI",
  step=4,
  intro="Step 4 is about what blood that bypasses the liver does to the brain, and ammonia is not the only substance involved. Manganese is cleared by the liver into bile; in cirrhosis it reaches the basal ganglia instead, and the exam asks you to recognise the MRI picture.",
  parts=[
    ('a', "**Manganese deposition: manganese is cleared in bile, and portosystemic shunting (cirrhosis, TIPS) lets it reach the pallidum.** Manganese is paramagnetic and shortens T1, so the globus pallidus turns bright on T1 bilaterally and symmetrically. It is seen in most cirrhotics with shunting, more after TIPS, and correlates with shunting more than with ammonia."),
    ('b', "**Linked to parkinsonism (acquired hepatocerebral degeneration); regresses after transplant.** Manganese damages the dopaminergic pathway in the pallidum, giving rigidity and bradykinesia with an inconsistent response to levodopa. When the shunt and liver are corrected by transplant, the signal fades over months."),
    ('c', "**Wilson disease differs: T2-hyperintense putamen/thalami (‘face of the giant panda’).** Wilson disease is copper, seen on T2 in the putamen, thalami and midbrain (the panda face). Pallidal T1 brightness is manganese; striatal T2 brightness is copper."),
  ],
  mimic=[
    ("Manganese vs Wilson disease", "Manganese: T1-bright globus pallidus. Wilson: T2-bright putamen and thalami, ‘giant panda’ midbrain."),
    ("Manganese vs kernicterus", "Kernicterus (neonatal bilirubin) also targets the globus pallidus, but on T2 and in neonates."),
  ],
  traps=[
    ("“Copper deposition” or “Wilson disease” for T1 pallidal hyperintensity in cirrhosis", "Copper gives T2 changes in the putamen and thalami; T1 pallidal brightness in cirrhosis is manganese."),
  ],
  decode=[
    ("Cirrhotic with chronic HE; MRI shows bilateral T1-hyperintense globus pallidus — what is it? [DocT]", "Manganese deposition from portosystemic shunting."),
  ],
  punch="Bilateral T1-bright globus pallidus in a cirrhotic is manganese that shunting carried past the liver; it underlies hepatocerebral parkinsonism and fades after transplant, while Wilson disease is copper on T2.",
)

FLAGS = {}
