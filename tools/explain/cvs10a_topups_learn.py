# CVS10A top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs10a_learn.py.
# Fields: sub, step (index into cvs10a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source: cvs_topups.json → "CVS10A": T_3a5116ba (chest pain relieved by nitrate; DocT GT AIM1 Q140). The source stem was not opened; decode items follow the top-up question.
# From standard references without a fresh check: nitroglycerin relief does not predict ACS in ED cohorts (Henrikson, Ann Intern Med 2003: relief in about 35% with and 41% without
# active CAD); ESC 2023 / AHA/ACC 2025: a single normal ECG does not exclude ACS, serial hs-cTn (0 h/1 h or 0 h/2 h, 3 h if inconclusive); HEART score for risk; oesophageal spasm
# diagnosed by high-resolution manometry (Chicago classification, premature contractions).

T = {}

T['T_3a5116ba'] = dict(
  sub="ACS → Presentation → Chest pain relieved by nitrate",
  step=5,
  intro="Step 5 is the patient with chest pain, and this top-up tests a common bedside reflex: ‘it went with GTN, so it was cardiac’. Nitrates act on smooth muscle wherever it is, so the response cannot separate the heart from the oesophagus.",
  parts=[
    ('a', "**Nothing diagnostic: nitrates relax smooth muscle, so they relieve both myocardial ischaemia and oesophageal spasm (NTG response does not predict ACS in ED studies).** In ischaemia nitrates lower preload and wall tension and dilate epicardial arteries; in oesophageal spasm they relax the oesophageal muscle. In emergency department cohorts relief after nitroglycerin was as common in patients without ACS as in those with it, and pain relief after a ‘GI cocktail’ is equally uninformative."),
    ('b', "**One normal ECG + one negative troponin excludes MI, not unstable angina → repeat hs-troponin at 1–3 h and risk-stratify (HEART score).** A first troponin taken soon after symptom onset may not yet have risen, and unstable angina never raises it; ESC 2023 accepts a single hs-cTn as rule-out only when it is very low and the pain began more than 3 h earlier; ESC 2023 uses 0 h/1 h or 0 h/2 h hs-cTn, with a 3 h sample if inconclusive, and a non-diagnostic first ECG does not exclude ACS (AHA/ACC 2025). The HEART score then decides who can go home."),
    ('c', "**Oesophageal spasm clues: dysphagia, relation to swallowing or hot/cold liquids; confirm by manometry.** Spasm is triggered by swallowing and may be accompanied by dysphagia; high-resolution manometry shows premature (spastic) contractions. It is diagnosed only after a cardiac cause has been excluded."),
  ],
  mimic=[
    ("Oesophageal spasm vs angina", "Both squeeze, both radiate, both respond to nitrate; spasm is linked to swallowing and dysphagia, angina to exertion."),
  ],
  traps=[
    ("“Pain relieved by GTN confirms angina”", "It does not; the response is the same in oesophageal spasm and does not predict ACS."),
    ("“Normal ECG and negative troponin: discharge”", "That excludes MI at that moment, not unstable angina; repeat troponin and risk-stratify first."),
  ],
  decode=[
    ("Chest pain relieved by nitroglycerin, normal ECG, negative troponin: what does the nitrate response tell you? [DocT GT AIM1]", "Nothing diagnostic; repeat hs-troponin and risk-stratify."),
  ],
  punch="A nitrate response proves only that smooth muscle relaxed; the diagnosis comes from serial ECG and troponin and the risk score.",
)

FLAGS = {
  'T_3a5116ba': "b: ‘one negative troponin excludes MI’ is too strong as written; a single hs-cTn rules out MI only when it is very low (below the assay’s rule-out cut-off) and the pain began more than 3 h earlier (ESC 2023 0 h/1 h algorithm); otherwise a repeat at 1–2 h (3 h if inconclusive) is needed before MI is excluded. The explanation states this.",
}
