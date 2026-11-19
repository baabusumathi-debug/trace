# CVS06A top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs06a_learn.py.
# Fields: sub, step (index into cvs06a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source: cvs_topups.json → "CVS06A": T_a1c52257 (myocardial O₂ demand and Laplace; DocT GT GT2 Q123, 75% right, key ‘increased heart rate’; DocT GT GT6 Q37, 75% right, key
# ‘haemoglobin’ as NOT a determinant of demand; Marrow QB20-Q04, key ‘ventricular wall thickness’ for what wall stress is inversely proportional to). Stems read in out/gt_map_GT2_GT3.csv,
# out/gt2_map_GT6.csv and QMap_full_932.csv (options other than the key not available).
# From standard physiology without a fresh check (confident): Laplace for a thin-walled sphere, wall stress = P × r / 2h; determinants of MVO₂ are heart rate, contractility and wall
# tension (preload and afterload); coronary flow occurs mainly in diastole, so tachycardia also cuts supply.
T = {}

T['T_a1c52257'] = dict(
  sub="RV failure → Pathophysiology → Myocardial oxygen demand and Laplace",
  step=4,
  intro="Step 4’s spiral starts with wall tension raising oxygen demand, and this top-up asks the general rule behind it. Three bank questions test it: what dobutamine does to an ischaemic heart, which variable is not a determinant of demand, and what wall stress is inversely proportional to.",
  parts=[
    ('a', "**Heart rate (most important: more beats AND a shorter diastole for coronary filling), contractility and wall tension.** Each beat costs oxygen, so demand rises with rate; and because the LV is perfused mainly in diastole, which shortens most as rate rises, tachycardia cuts supply at the same moment. Contractility raises the energy cost per beat. Wall tension is the force the muscle must hold during systole, set by preload (radius) and afterload (pressure)."),
    ('b', "**Laplace: wall stress = P × r / 2h; it rises with pressure and radius and falls with wall thickness (the logic of compensatory hypertrophy).** A dilated ventricle needs more tension to make the same pressure, so it costs more oxygen. Hypertrophy spreads the load over more muscle and brings wall stress back to normal; this is why a chronically loaded RV thickens, and why a thin, acutely loaded RV develops high stress and becomes ischaemic (RVF-15)."),
    ('c', "**Dobutamine raises heart rate and contractility, so demand outruns a fixed supply and ST depression follows.** With a fixed coronary stenosis supply cannot rise, and the shorter diastole lowers it; ischaemia appears as subendocardial ST depression. The fix is to slow the rate or reduce the dose, not to add fluid."),
    ('d', "**Reducing preload or radius lowers demand; anaemia lowers supply, not demand.** Nitrates and diuretics shrink the ventricle and reduce wall tension. Haemoglobin sets oxygen content of coronary blood, which is supply; anaemia worsens ischaemia by that route and may raise heart rate, but haemoglobin itself is not a determinant of demand."),
  ],
  mimic=[
    ("Determinants of demand vs supply", "Demand: heart rate, contractility, wall tension; supply: coronary flow (perfusion pressure, diastolic time, stenosis) and oxygen content (haemoglobin, saturation)."),
  ],
  traps=[
    ("“Dobutamine causes ischaemia mainly by raising wall tension or afterload”", "Its main effects are on heart rate and contractility; rate is the most important determinant and also shortens diastolic filling (DocT GT keys increased heart rate, 75%)."),
    ("“Haemoglobin is a determinant of myocardial oxygen demand”", "It determines supply (oxygen content); 75% got this on DocT GT."),
    ("“Wall stress is inversely proportional to radius or pressure”", "It is directly proportional to both and inversely proportional to wall thickness (Marrow)."),
  ],
  decode=[
    ("Ischaemic cardiomyopathy on dobutamine develops chest pain and ST depression — main mechanism? [DocT GT]", "Increased heart rate (75%)."),
    ("Which is NOT a determinant of myocardial oxygen demand? [DocT GT]", "Haemoglobin (75%)."),
    ("Myocardial wall stress is inversely proportional to? [Marrow]", "Ventricular wall thickness."),
  ],
  punch="Myocardial oxygen demand is set by heart rate, contractility and wall tension, and wall tension by Laplace (pressure × radius over twice the thickness); haemoglobin is supply, and dobutamine causes ischaemia mainly through heart rate.",
)
