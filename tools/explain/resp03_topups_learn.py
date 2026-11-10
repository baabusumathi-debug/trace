# RESP03 top-up cards — Explain v3 ("Learn" depth), same fields and voice as resp03_learn.py.
# Fields: sub, step (index into resp03_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from the DocT Grand Test files (the top-up's own src) plus qpack/RESP03.md.
T = {}

T['T_938aa87a'] = dict(
  sub="Respiratory → Respiratory failure → Types I–IV",
  step=2,
  intro="Step 2 asks what goes wrong with the lung after surgery, and the four-type classification (Principles of Critical Care) gives post-operative failure its own place. The types are sorted by mechanism, not by the blood gas alone, and the exam tests exactly that: a stem whose gas fits one type but whose setting fits another.",
  parts=[
    ('a', "**Type I (hypoxaemic): V/Q mismatch/shunt; PaO₂ <60 with normal or low PaCO₂ (pneumonia, ARDS, oedema).** Alveoli that are perfused but flooded or collapsed cannot oxygenate the blood through them; the patient breathes harder, so CO₂ is normal or low."),
    ('b', "**Type II (hypercapnic): alveolar hypoventilation; PaCO₂ >45–50 with acidosis (COPD, opioids, neuromuscular).** The pump — drive, nerves, muscles or the load on them — cannot move enough air, so CO₂ rises and pH falls; PaO₂ falls with it."),
    ('c', "**Type III (perioperative): atelectasis from low FRC, pain and splinting after upper abdominal surgery; mainly hypoxaemia, CO₂ may rise.** Anaesthesia, a painful wound and opioids shrink FRC below closing capacity, so dependent lung collapses (RSC-04). It is a type I lesion with a type II component, given its own label because the setting and the treatment — re-expansion — are specific."),
    ('d', "**Type IV (shock): normal lungs and pump, but respiratory-muscle hypoperfusion and high ventilatory demand (sepsis, cardiogenic shock) → fatigue; ventilate to unload the muscles until shock is reversed.** In shock the respiratory muscles take a large share of a cardiac output that is already too small, while acidosis and sepsis drive ventilation up; they fatigue and CO₂ rises. Ventilating them frees that blood flow for other organs."),
  ],
  mimic=[
    ("Type III vs type II after surgery", "Both can show a high CO₂; type III is atelectasis in the post-operative setting, type II is a primary failure of the pump."),
    ("Type IV vs type I in sepsis", "Type IV has clear lungs and fatigue; type I has infiltrates (pneumonia, ARDS)."),
  ],
  traps=[
    ("“Day 1 after upper abdominal surgery on opioids, pH 7.30, PaCO₂ 58 — type II”", "DocT keys type III from the setting (56% and 72% chose it); the gas is hypercapnic, so type II is defensible — in the exam, a post-operative stem goes to type III."),
    ("“Sepsis, clear lungs, rising CO₂ from fatigue — type II”", "The pump is normal; the failure is demand outstripping supply, which is type IV."),
  ],
  decode=[
    ("Post-op day 1, upper abdominal surgery, opioids, drowsy, PaCO₂ 58 [DocT GT ×2]", "Type III — perioperative."),
    ("Sepsis with normal lungs and a normal respiratory pump [DocT GT]", "Type IV (88%)."),
    ("Post-op sepsis, clear lung fields, progressive hypercapnia, intubated for fatigue [DocT GT]", "Type IV — increased ventilatory demand."),
    ("Smoker, PaO₂ 55, PaCO₂ 70, hyperinflation [DocT GT]", "Type II from COPD (94%)."),
  ],
  punch="Type I is a lung that cannot oxygenate, type II a pump that cannot ventilate, type III the collapsed post-operative lung and type IV normal lungs failing because shock starves the muscles.",
)

T['T_23f59da7'] = dict(
  sub="Respiratory → Airway → Anterior mediastinal mass at induction",
  step=5,
  intro="Step 5 turns to the airway that is harder to secure. A large anterior mediastinal mass is the extreme case: an airway that stays open while the patient breathes and may close the moment anaesthesia is induced. The exam asks which bedside finding predicts that collapse.",
  parts=[
    ('a', "**Symptoms when supine (orthopnoea, cough, stridor) predict compression; normal PFTs or auscultation do not reassure.** If lying flat already narrows the airway, the patient is relying on posture and muscle tone to keep it open. Normal tests done upright and awake say nothing about the anaesthetised, supine state; an echo looks for cardiac or vascular compression, not the airway."),
    ('b', "**Induction, paralysis and positive pressure remove the muscle tone and negative intrathoracic pressure that hold the airway open, so the mass compresses trachea, bronchi or pulmonary artery.** Awake, the negative pleural pressure of inspiration pulls the airways open and smooth-muscle tone stiffens them. Anaesthesia lowers lung volume, abolishes that tone and replaces negative with positive pressure, so the mass meets less resistance; a tube may pass the narrowing yet the bronchi beyond it can still collapse."),
    ('c', "**Plan: CT first, keep spontaneous breathing (awake fibreoptic intubation, sitting up), rigid bronchoscope ready, ECMO standby if high risk; steroids or radiotherapy can shrink the mass first.** CT shows where and how badly the airway is narrowed. Keeping the patient breathing preserves the forces that hold the airway open; a rigid bronchoscope can be passed beyond a compression, and ECMO (or bypass) supports a patient whose airway cannot be rescued. Treating lymphoma first can shrink the mass but may compromise the histology, so where possible tissue is taken first, often from a peripheral node or under local anaesthesia; when the airway cannot wait, a short steroid course is given after discussion with the oncologists, who also watch for tumour lysis."),
  ],
  mimic=[],
  traps=[
    ("“Normal recent pulmonary function tests make induction safe”", "They are done awake and upright; supine symptoms are the predictor (65% chose correctly)."),
    ("“An echocardiogram best predicts airway collapse”", "Echo shows cardiac and vessel compression or effusion, not the airway."),
    ("“Standard rapid sequence induction with paralysis”", "Paralysis removes the tone that keeps the airway open; keep spontaneous breathing."),
  ],
  decode=[
    ("New lymphoma, widened superior mediastinum, needs intubation — best test of airway-collapse risk? [DocT GT]", "Ability to lie supine without orthopnoea or cough."),
  ],
  punch="An anterior mediastinal mass is held off the airway by the patient’s own breathing, so the best predictor is whether lying flat already causes symptoms, and the plan is to keep the patient breathing.",
)

T['T_3e6c3480'] = dict(
  sub="Respiratory → Post-operative lung → Lobar collapse on the ventilator",
  step=2,
  intro="Step 2 makes atelectasis the commonest pulmonary complication; lobar collapse is its sudden form. A ventilated patient with secretions desaturates, and the usual fixes — more oxygen, more PEEP, checking the tube — do nothing, because no gas reaches a lobe sealed off by a plug.",
  parts=[
    ('a', "**Left lower lobe collapse (‘sail sign’), usually from a mucus plug.** The collapsed lobe lies behind the heart as a triangular opacity; it removes the outline of the medial left hemidiaphragm and the descending aorta, and gives a double cardiac contour. It is easily missed because the heart hides it."),
    ('b', "**Next: therapeutic bronchoscopy to clear the plug (plus suction, humidification, physiotherapy).** Removing the plug reopens the lobe, so the shunt closes. Physiotherapy and suction often work as well: in Marini’s 1979 randomised trial of acute lobar atelectasis (31 patients), bronchoscopy added nothing to vigorous respiratory therapy, and an air bronchogram (patent proximal airways) predicted slow resolution with either. So in a stable patient chest physiotherapy comes first; bronchoscopy is chosen, as here, when hypoxaemia is severe and has not responded, when physiotherapy cannot be done or has failed, or when the absence of air bronchograms suggests a central plug."),
    ('c', "**Not needle decompression (tension pneumothorax is hyperlucent with shift away); not advancing the tube (right mainstem intubation collapses the whole left lung).** Collapse is white with volume loss, and the mediastinum moves toward it; tension pneumothorax is black and pushes everything away. A tube already checked is in place; pushing it 3 cm further enters the right main bronchus. Prone positioning is for ARDS, not a plugged lobe."),
  ],
  mimic=[
    ("Lobar collapse vs tension pneumothorax", "Collapse: white, volume loss, shift toward it. Tension: black, no lung markings, shift away, hypotension."),
    ("Lobar collapse vs ARDS", "Collapse is one lobe with volume loss; ARDS is bilateral opacities without volume loss."),
  ],
  traps=[
    ("“Advance the tube by 3 cm”", "The tube was already repositioned; advancing it causes right mainstem intubation."),
    ("“Needle decompression”", "Nothing on the film is hyperlucent; this is collapse, not tension."),
    ("“Prone him”", "Proning treats diffuse ARDS; a plugged lobe needs the plug removed (only 28% chose bronchoscopy)."),
    ("“Bronchoscopy is always better than physiotherapy for lobar collapse”", "Marini 1979 found no difference overall; bronchoscopy is for severe or refractory hypoxaemia, as in this stem."),
  ],
  decode=[
    ("Ventilated, productive cough, hypoxaemia not fixed by FiO₂, PEEP or tube repositioning; CXR retrocardiac triangle [DocT GT]", "Bronchoscopy."),
  ],
  punch="Hypoxaemia that ignores oxygen, PEEP and the tube, with a triangle behind the heart, is a plugged left lower lobe, and the treatment is to remove the plug.",
)

FLAGS = {
  'T_938aa87a': "Not a card error: DocT GT (GT2 Q9, GT5 Q56) keys type III for a post-op opioid patient with pH 7.30 and PaCO₂ 58, although the gas and the opioid mechanism fit type II; the classification overlaps. Card is consistent with the key; explanation names the dispute.",
}
