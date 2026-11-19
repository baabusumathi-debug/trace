# CVS07A top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs07a_learn.py.
# Fields: sub, step (index into cvs07a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source: cvs_topups.json → "CVS07A": T_db59d55f (Pittsburgh Cardiac Arrest Category, DocT Brain Death Q10). The source stem was not opened; decode items follow the top-up question.
# Checked online 19 Nov 2026: UPMC Post-Cardiac Arrest Service PCAC page (I awake, follows commands, survival 80%; II coma, mild cardiopulmonary failure, noradrenaline ≤0.1 mcg/kg/min, 60%;
# III coma, severe cardiopulmonary failure, high ventilator support and vasopressor >0.1, 40%; IV coma with absent pupil and/or corneal reflexes and no motor response, 10%, about 5% good recovery);
# Coppler, Resuscitation 2015 (validation in 607 patients at two sites; survival odds about one-third per category step). Rittenberger 2011 derivation (>450 patients, UPMC 2005–09): the SOFA
# cardiovascular + respiratory ≥4 split between II and III is from the derivation paper (standard reference, not reopened).
T = {}

T['T_db59d55f'] = dict(
  sub="Post-arrest care → Severity at ICU entry → Pittsburgh Cardiac Arrest Category (PCAC)",
  step=2,
  intro="Step 2 says that the severity of the post-arrest syndrome depends on the brain injury and the cardiopulmonary failure. The Pittsburgh Cardiac Arrest Category turns exactly those two things into four levels in the first hours after ROSC, and survival falls with each level.",
  parts=[
    ('a', "**I: awake, follows commands.** No significant brain injury; survival about 80%. These patients do not need temperature control (PCA-09)."),
    ('b', "**II: comatose, mild cardiopulmonary dysfunction.** Coma with modest support (SOFA cardiovascular plus respiratory below 4; low-dose vasopressor); survival about 60%. The brain, not the circulation, decides the outcome."),
    ('c', "**III: comatose with moderate–severe cardiopulmonary failure (SOFA cardiovascular + respiratory ≥4).** High ventilator support and higher-dose vasopressors; survival about 40%. Death comes from both shock and brain injury, so these patients are the ones in whom haemodynamic support matters most."),
    ('d', "**IV: comatose with loss of brainstem reflexes.** Absent pupillary and/or corneal reflexes and no motor response, whatever the cardiopulmonary state; survival under 10%, with only about 5% recovering well. Early on this can still reflect sedation, cooling or a primary brain cause, so it is not a basis for withdrawal before 72 hours."),
    ('e', "**Survival falls step-wise (about 80% → 60% → 40% → <10%), so it stratifies outcome at ICU entry.** The score is used to compare patients and to enrol them in trials; it is assigned early and is not a neuroprognostication tool."),
  ],
  mimic=[
    ("Pittsburgh category vs post cardiac arrest care (both ‘PCAC’)", "The category is a four-level severity score; post cardiac arrest care is the five-domain care package (PCA-05)."),
    ("PCAC IV vs brain death", "PCAC IV is lost brainstem reflexes early after ROSC, often confounded; brain death needs the confounders excluded and a formal test."),
  ],
  traps=[
    ("“PCAC IV means brain dead”", "It is a severity category assigned in the first hours, and about 5% still recover well."),
    ("“Category depends on rhythm or arrest duration”", "It uses only coma, brainstem reflexes and cardiopulmonary SOFA."),
  ],
  decode=[
    ("Pittsburgh Cardiac Arrest Category after ROSC: the four levels [DocT]", "I awake; II coma, mild cardiopulmonary failure; III coma, SOFA cardiovascular + respiratory ≥4; IV coma with lost brainstem reflexes."),
    ("[pattern] Approximate survival by PCAC category", "About 80, 60, 40 and under 10%."),
  ],
  punch="The Pittsburgh category grades the arrest by the two things that kill: coma and cardiopulmonary failure; survival falls from about 80% (awake) through 60% and 40% to under 10% when brainstem reflexes are lost.",
)

FLAGS = {}
