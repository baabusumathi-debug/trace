# RESP07A top-up cards — Explain v3 ("Learn" depth), same fields and voice as resp07a_learn.py.
# Fields: sub, step (index into resp07a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from map/out/all_rows.json and the DocT GT/QBank files (the top-up's own src) plus qpack/RESP07A.md.
# Checked online 11 Nov 2026: most herniations occur within 24 h (many in theatre or on turning), mortality about 50% when recognised and near 100% when not,
# right-sided herniation kinks the cavae (obstructive shock), left-sided strangulates the ventricle (ischaemia, arrhythmia), repair with a patch rather than direct suture.
# Second review 11 Nov 2026: positioning non-operated side down (= operated side up) and air injection into the operated hemithorax as temporising steps (PMC7049486);
# suction on the drain listed as a precipitant (J Cardiothorac Surg 2021, doi 10.1186/s13019-021-01439-5); 75% intraoperative, 50%/100% mortality, patch repair confirmed in the same paper.
T = {}

T['T_bb56c02c'] = dict(
  sub="Respiratory → Pleura → Cardiac herniation after pneumonectomy",
  step=6,
  intro="Step 6 ends with a pleural space that has been emptied on purpose. After a pneumonectomy, especially an intrapericardial one, the pericardium may be left with a defect, and the heart can swing through it into the empty hemithorax. Anything that pulls the heart towards that side — suction on the drain, coughing, turning the patient onto the operated side, or a large pressure difference between the two hemithoraces — can trigger it.",
  parts=[
    ('a', "**Cardiac herniation through a pericardial defect, usually within 24 h (often on coughing, turning onto the operated side, or suction on the drain); it may cause SVC obstruction or arrhythmia.** Most cases occur in theatre (about three-quarters in one review) or in the first hours, often at the moment of turning; late cases are reported. On the right the heart rotates into the empty chest and kinks the superior and inferior venae cavae: obstructive shock with a high central venous pressure, a congested face and neck, and tachycardia. On the left the ventricle is strangled by the edge of the defect: ischaemia, arrhythmia and ventricular fibrillation."),
    ('b', "**Chest X-ray, echo or CT show the heart displaced into the empty hemithorax.** The cardiac silhouette lies in the operated side, rotated or with an abnormal contour; echo shows the displacement and the kinked cavae. Imaging must not delay action in a patient who is crashing."),
    ('c', "**Turn the operated side up, stop suction, and re-operate at once to repair the pericardium; mortality is high if delayed.** Putting the operated side up lets gravity draw the heart back towards the midline, and removing suction ends the pull into the empty space (some reports also inject air into the operated hemithorax to push the heart back); keep tidal volumes and airway pressures modest. These buy time only: the definitive treatment is immediate re-thoracotomy, reduction of the heart and closure of the defect with a patch (direct suture can tear again). Mortality is about half when it is recognised and treated, and close to all when it is not."),
  ],
  mimic=[
    ("Cardiac herniation vs post-operative bleeding or tamponade", "All cause hypotension and tachycardia after pneumonectomy. Bleeding shows on the drain and the haemoglobin; tamponade shows a pericardial effusion; herniation shows the heart in the wrong hemithorax and often follows a position change or suction."),
    ("Cardiac herniation vs mediastinal shift from the post-pneumonectomy space", "Gradual shift towards the operated side is normal as the space fills; herniation is sudden, with shock."),
  ],
  traps=[
    ("“Turn him onto the operated side to help the remaining lung”", "That swings the heart into the empty hemithorax; the operated side goes up."),
    ("“Put the pneumonectomy drain on suction to evacuate the space”", "Suction on a pneumonectomy drain pulls the mediastinum and heart across; the drain is kept off suction (clamped with periodic release, or a balanced drainage system, by local practice)."),
  ],
  decode=[
    ("Sudden hypotension and tachycardia hours after pneumonectomy — diagnosis and action? [Marrow]", "Cardiac herniation: operated side up, stop suction, immediate re-operation."),
  ],
  punch="Sudden shock in the first day after pneumonectomy, often on turning, coughing or suction, is cardiac herniation until shown otherwise: operated side up, suction off, back to theatre.",
)

FLAGS = {}
