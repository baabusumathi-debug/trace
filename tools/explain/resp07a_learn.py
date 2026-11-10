# RESP07A — Explain v3 ("Learn" depth): the pleura, part 1 — pleural anatomy and fluid, pneumothorax (types, tension, open, ICU), imaging (CXR/CT, lung ultrasound, BLUE), BTS management and the chest drain. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP07A.md (38 questions; PLEU-08 lung ultrasound asked 10 times, PLEU-04 tension and PLEU-09 BLUE 7 each, PLEU-07 CXR/CT 4). Fields as TOX01, plus SPINE, PRIMER and step.
# Cards with no linked question get short explanations with [pattern] decode items. RESP07B (effusion, haemothorax; PLEU-14 to PLEU-27) follows.
# Figures checked online on 11 Nov 2026: BLUE protocol (Lichtenstein, Chest 2008: 260 patients, 90.5%, per-diagnosis sensitivity/specificity incl. pneumothorax 88%/100% = 8/9, abstract misprints 81%);
# lung point (Lichtenstein, Intensive Care Med 2000: sensitivity 66%, 75% if radio-occult, specificity 100%); absent sliding specificity 91% in the critically ill;
# CXR sensitivity by view (lateral decubitus 88%, erect 59%, supine 37%); Tocino (anteromedial 38%, subpulmonic 26%, 30% missed, half of those to tension);
# ICU misdiagnosis series (32% missed; tension 33% of missed vs 5% of recognised); ATLS 10th ed. needle site (4th/5th ICS just anterior to the mid-axillary line, 5–8 cm needle);
# 5 cm needle predicted failure (Laan, Injury 2016: 2nd ICS MCL 38%, 4/5 ICS MAL 31%, AAL 13%); Brown NEJM 2020 (316 patients, 94.4% vs 98.5%, 15.4% of conservative arm needed intervention);
# RAMPP (Hallifax, Lancet 2020: 236 patients, median stay 0 vs 4 days, more adverse events, fewer re-interventions 21% vs 35%); BTS 2023 conservative PSP regardless of size;
# Walker 2021 SSP ambulatory (41 patients; early failure 46% with 8 Fr pleural vent vs 15% standard, NS); OPTICC (Am J Surg 2021: 142 patients, distress 38% vs 25% NS, ~25% of observed needed a tube, ~40% if ventilated >=5 days);
# BTS 2010 aspiration 16–18 G, stop at 2.5 L; cardiac herniation (most within 24 h, mortality ~50% recognised, near 100% unrecognised).
# Second review (11 Nov 2026) verified online: ACURASYS pneumothorax 4.0% vs 11.7%; BTS 2010 2 cm at the hilum, 3–5-day surgical opinion, PSP incidence 18–28 (men) and 1.2–6 (women) per 100,000;
# Gupta 2000 (24.0 and 9.8 = consultation rates, PSP+SSP combined); recurrence 32% (Walker ERJ 2018); ATLS 10th adult 4th/5th ICS, 2nd ICS MCL still for children;
# BTS 2023 high-risk features incl. age >50 with smoking; normal pleural fluid pH ~7.6 from higher bicarbonate; lung sliding specificity 91.1% (Lichtenstein 1995); Tocino 1985.
# Standard teaching, not individually sourced: safe-triangle borders, removal in expiration or Valsalva, no clamping of a bubbling drain (Royal Marsden manual, citing Havelock 2010).

SPINE = [
  ("The pleura and its fluid", "The parietal pleura carries the pain fibres, makes the pleural fluid from systemic capillaries and drains it through lymphatic stomata, and normal fluid is a small, alkaline, macrophage-rich film."),
  ("Where the air comes from", "Pneumothorax is classified by its cause — primary with no lung disease, secondary on diseased lung with less reserve, traumatic and iatrogenic — and the class decides how ill the patient is and how it is treated."),
  ("Air under pressure", "When air enters and cannot leave, rising pleural pressure kills by hypoxia and by stopping venous return, fastest under positive-pressure ventilation, so tension is treated on clinical signs before any film."),
  ("Finding the air", "Air rises anteriorly in a supine patient, so the supine film misses most pneumothoraces, CT is the reference, and ultrasound excludes one wherever sliding, B-lines or a lung pulse are seen and confirms one only with a lung point."),
  ("Treat the patient, not the rim", "BTS management is driven by symptoms and by whether the lung was healthy: primary pneumothorax can be observed or aspirated, secondary needs admission and usually a drain, and the 2023 guideline allows conservative care of a minimally symptomatic primary pneumothorax whatever its size."),
  ("Draining the pleural space", "A drain goes in through the safe triangle just above a rib, small-bore by Seldinger for air, and comes out once the lung is up and the leak has stopped, while a space emptied by pneumonectomy is never put on suction."),
]

PRIMER = "The pleural space is a film of fluid a few millilitres thick between the visceral pleura on the lung and the parietal pleura lining the chest wall, diaphragm and mediastinum. At rest its pressure is about −5 cmH₂O, held negative because the lung recoils inward while the chest wall springs outward; once air enters, that coupling is lost and the lung shrinks towards its own resting volume. In a spontaneously breathing patient air is drawn in by the patient’s effort, but under positive-pressure ventilation the ventilator pushes air through any leak with every breath. On lung ultrasound the probe sees only the pleural line and the artefacts it makes: horizontal A-lines (reverberation), vertical B-lines (fluid-thickened septa) and sliding, the shimmer of visceral pleura moving on parietal pleura."

L = {}

L['PLEU-01'] = dict(
  sub="Respiratory → Pleura → Parietal vs visceral pleura",
  step=1,
  intro="Step 1 starts with the two layers, because their differences explain where pleural pain comes from and where pleural fluid is made and cleared. The parietal layer, on the chest wall, does almost all the work; the visceral layer is wrapped on the lung.",
  parts=[
    ('a', "**Parietal: systemic arteries (intercostal, pericardiophrenic, musculophrenic). Visceral: mainly bronchial arteries.** The parietal capillaries are systemic and lie close to the pleural surface, so they are the main source of pleural fluid. The visceral pleura in humans is thick and supplied by bronchial arteries, draining largely to the pulmonary veins."),
    ('b', "**Parietal: intercostal nerves for the costal and peripheral diaphragmatic pleura, phrenic for the central diaphragmatic pleura. Visceral: no pain fibres.** So pleuritic pain means the parietal pleura is involved. Irritation of the central diaphragm is felt at the shoulder tip (phrenic, C3–5); the peripheral diaphragm and costal pleura refer to the chest wall and upper abdomen. The visceral pleura has only autonomic supply, which is why a pneumonia or tumour inside the lung is painless until it reaches the parietal pleura."),
    ('c', "**Parietal pleura forms the fluid (capillaries) and removes it (lymphatic stomata); the visceral pleura absorbs little.** Fluid filters from parietal capillaries into the space and leaves through stomata in the parietal pleura, mostly over the diaphragm and lower mediastinum, into lymphatics that can raise their flow many times before fluid builds up. An effusion (RESP07B) therefore needs either more filtration than the lymphatics can clear, or blocked lymphatics."),
  ],
  mimic=[
    ("Parietal vs visceral pleura", "Parietal: systemic supply, somatic nerves, pain, makes and clears fluid. Visceral: bronchial supply, no pain fibres, little role in fluid turnover."),
  ],
  traps=[
    ("“Chest pain in lung disease comes from the visceral pleura or the parenchyma”", "Neither has pain fibres; the pain comes from the parietal pleura. Only half the cohort chose this on DocT GT (PLEU-13)."),
    ("“The parietal pleura is supplied by bronchial arteries”", "That is the visceral pleura; the parietal pleura is systemic (PLEU-13a)."),
  ],
  decode=[
    ("Chest pain caused by respiratory disease usually originates from involvement of? [DocT GT]", "Parietal pleura (50% right)."),
    ("[pattern] Shoulder-tip pain with a basal pleural process — which nerve?", "Phrenic (central diaphragmatic pleura)."),
  ],
  punch="The parietal pleura is the working layer: systemic blood, the pain fibres, and both the making and the draining of pleural fluid; the visceral pleura feels nothing.",
)

L['PLEU-02'] = dict(
  sub="Respiratory → Pleura → Normal pleural fluid",
  step=1,
  intro="Step 1 continues with the fluid itself. Its normal values are the baseline against which every effusion in RESP07B is judged, and the one that surprises people is the pH.",
  parts=[
    ('a', "**About 0.2 mL/kg.** A few millilitres in each hemithorax: enough to let the layers glide, far too little to see on a film or ultrasound. Anything visible is abnormal."),
    ('b', "**1500–1800 cells/mm³: macrophages 75%, lymphocytes about 25%, others about 2%.** Neutrophils, eosinophils and mesothelial cells are scanty, so a neutrophil-rich fluid points to an acute process such as a parapneumonic effusion, and a lymphocyte-rich one beyond the normal share points to tuberculosis or malignancy."),
    ('c', "**1–1.5 g/dL protein.** The fluid is a low-protein filtrate, so its ratio to serum protein is well below the 0.5 that Light’s criteria use to call an exudate."),
    ('d', "**pH 7.62, above plasma.** The pleural fluid holds more bicarbonate than plasma, so it is alkaline. A fall to below 7.2 therefore means a large acid load (bacteria and neutrophils metabolising glucose), which is why a pH under 7.2 in a parapneumonic effusion is the classic indication to drain (RESP07B)."),
  ],
  mimic=[
    ("Normal pleural fluid vs a transudate", "Both are low in protein, but a transudate is a visible volume; normal fluid is too small to image."),
  ],
  traps=[
    ("“Normal pleural fluid pH is about 7.4”", "It is about 7.6, above plasma (PLEU-13b)."),
  ],
  decode=[
    ("[pattern] Predominant cell in normal pleural fluid?", "Macrophages."),
    ("[pattern] Normal pleural fluid pH compared with blood?", "Higher (about 7.6)."),
  ],
  punch="Normal pleural fluid is a tiny, low-protein, macrophage-rich and alkaline film; a pH below 7.2 is a long way from normal.",
)

L['PLEU-03'] = dict(
  sub="Respiratory → Pleura → Classification of pneumothorax",
  step=2,
  intro="Step 2 sorts pneumothorax by where the air came from. The class matters because it tells you how much lung reserve is left: a primary pneumothorax in a healthy young man is often tolerated, while the same size in a man with COPD can cause type 2 failure.",
  parts=[
    ('a', "**Primary spontaneous: no known lung disease, rupture of a subpleural bleb, tall thin young men, upper lobe; smoking (cannabis more than tobacco) raises the risk. Incidence 24 per lakh a year in men, 9.8 in women.** Those two figures are the English general-practice consultation rates for all pneumothorax, primary and secondary together (Gupta, Thorax 2000); BTS 2010 gives primary spontaneous pneumothorax alone as 18–28 per lakh a year in men and 1.2–6 in women. Apical blebs sit where the distending pressure on the lung is greatest in a tall chest, which is why the apex and the tall build go together. Smoking raises the risk in a dose-related way. Recurrence after a first episode is about one in three (pooled 32%, 29% within the first year, in a 2018 meta-analysis). A woman of reproductive age with recurrent right-sided pneumothorax around her periods has catamenial pneumothorax, from thoracic endometriosis (diaphragmatic defects and implants); it recurs often and needs VATS repair of the diaphragm with pleurodesis and hormonal suppression."),
    ('b', "**Secondary spontaneous: emphysema, asthma, cystic fibrosis, tuberculosis, Pneumocystis, fibrosis, histiocytosis X, lymphangioleiomyomatosis, Marfan and Ehlers–Danlos, lung cancer.** COPD is by far the commonest. The diseased lung has little reserve, so even a small pneumothorax can cause marked hypoxaemia and hypercapnia; the card’s watch line holds — more symptoms, higher mortality, always admit (PLEU-11). In a COPD patient who suddenly worsens, think pneumothorax before ‘another exacerbation’: hyperresonance and quiet breath sounds are already present in the emphysematous chest, so the examination does not separate them, the film does."),
    ('c', "**Traumatic: penetrating or blunt chest injury; the second commonest finding after rib fractures.** Blunt trauma ruptures alveoli or lets a rib fragment pierce the lung; many are occult on the supine trauma film and seen only on CT (PLEU-06)."),
    ('d', "**Iatrogenic: subclavian or jugular cannulation, thoracentesis, transthoracic or transbronchial biopsy, positive-pressure ventilation.** The subclavian route carries a higher pneumothorax risk than the internal jugular because the needle passes over the lung apex. Desaturation or aspiration of air during attempts means stop, get a chest X-ray, and do not try the other side before it, since a bilateral pneumothorax is far more dangerous."),
  ],
  mimic=[
    ("Secondary pneumothorax vs COPD exacerbation", "Both bring sudden breathlessness and hypercapnia in a COPD patient; the signs overlap, so the film (or ultrasound) decides. Sudden onset and unilateral reduction in breath sounds favour pneumothorax."),
    ("Catamenial vs ordinary primary pneumothorax", "Catamenial: woman, right side, recurring within about 72 hours of menses, from endometriosis."),
  ],
  traps=[
    ("“Sudden breathlessness in COPD is an exacerbation”", "A third of the cohort chose COPD exacerbation or asthma; sudden deterioration in COPD is a secondary pneumothorax until imaging says otherwise. The stem’s ‘after a fall’ and bilateral hyperresonance are loose wording, and DocT’s key is still spontaneous pneumothorax."),
    ("“Try the other subclavian after a failed, desaturating attempt”", "Stop and take a film first; a pneumothorax on one side plus a second on the other is the disaster to avoid."),
  ],
  decode=[
    ("Long-standing COPD, sudden breathlessness, PaCO₂ 72, pH 7.32 — diagnosis? [DocT]", "Secondary spontaneous pneumothorax (68% right)."),
    ("Recurrent right-sided chest pain and dyspnoea with menstruation, small pneumothorax — cause? [DocT GT]", "Thoracic endometriosis (catamenial pneumothorax; 84%)."),
    ("Desaturation after failed subclavian attempts — next step? [Marrow]", "Abort, chest X-ray, drain if pneumothorax."),
  ],
  punch="Primary pneumothorax is a burst bleb in healthy lung; secondary is the same leak in diseased lung with no reserve, so the class, not the size, sets the danger.",
)

L['PLEU-04'] = dict(
  sub="Respiratory → Pleura → Tension pneumothorax",
  step=3,
  intro="Step 3 is what happens when the leak acts as a valve. Each breath adds air that cannot leave, pleural pressure climbs above atmospheric, and the patient dies of hypoxia and of a heart that cannot fill. Seven questions test it, and they ask three things: recognise it from the bedside (often in a ventilated or trauma patient), act without imaging, and know that the needle is only a bridge to a drain.",
  parts=[
    ('a', "**A one-way valve: air enters in inspiration and cannot leave, so pleural pressure rises with each breath; the lung collapses and the mediastinum shifts.** The flap of torn lung or chest wall opens when pleural pressure is lower than airway pressure and closes when it rises. Under positive-pressure ventilation the ventilator drives air in on every breath, so pressure builds within minutes; in a spontaneously breathing patient it builds more slowly. The signs follow the pressure: absent breath sounds and hyperresonance on that side, rising peak and plateau pressures on the ventilator (stiff chest, collapsed lung), surgical emphysema tracking into the neck, and late tracheal deviation away from the affected side."),
    ('b', "**Venous return falls (raised pressure, caval distortion) and cardiac chamber pressures equalise → shock and arrest.** Raised intrathoracic pressure compresses and kinks the venae cavae, the right heart fills poorly, and stroke volume falls; the neck veins distend unless the patient is hypovolaemic. In the awake, spontaneously breathing patient the body defends blood pressure for a long time and hypoxia and distress dominate, so hypotension is a late, pre-arrest sign. In the ventilated or hypovolaemic patient hypotension comes early. Blood pressure goes down, never up: hypertension is not a sign of tension."),
    ('c', "**Immediate needle decompression without waiting for imaging: 14–16 G cannula, 4th–5th intercostal space, mid- or anterior axillary line.** ATLS 10th edition places it in adults at the 4th or 5th space just anterior to the mid-axillary line, because the chest wall is thinner there than at the old site, the 2nd space in the mid-clavicular line. In a meta-analysis of chest-wall thickness (Laan, Injury 2016) a 5 cm cannula was predicted to fail in about 38% at the 2nd space mid-clavicular, 31% at the 4th–5th space mid-axillary and 13% at the 4th–5th space anterior axillary line, and failure rises with body mass; many authors therefore advise a longer (7–8 cm) catheter in adults. The 2nd space mid-clavicular site is still accepted in children, whose chest wall is thin. The needle only converts tension into an open, simple pneumothorax and kinks or blocks easily, so it is temporising: the definitive treatment is a chest drain, 5th space just anterior to the mid-axillary line, above the rib (PLEU-12). In a ventilated trauma patient a finger thoracostomy at the same site is an alternative to the needle."),
  ],
  table=dict(title="Tension or simple pneumothorax: what decides the first step", head=["", "Simple pneumothorax", "Tension pneumothorax"], rows=[["Circulation", "stable", "**hypotension**, tachycardia, distended neck veins"], ["Breathing", "breathless, hypoxaemia modest", "severe distress, falling SpO₂, rising airway pressures"], ["First step", "**chest X-ray (or ultrasound), then drain** if needed", "**decompress now**, no imaging"], ["Definitive", "drain or aspiration by BTS (PLEU-10, 11)", "**chest drain** after the needle"]]),
  mimic=[
    ("Tension pneumothorax vs cardiac tamponade", "Both cause hypotension and distended neck veins. Tension: absent breath sounds, hyperresonance, high airway pressure, tracheal shift. Tamponade: breath sounds normal, quiet heart sounds, effusion on echo."),
    ("Tension pneumothorax vs haemothorax", "Haemothorax: dull percussion and flat neck veins from blood loss; treated with a large-bore tube."),
    ("Tension pneumothorax vs mainstem intubation", "Both give one silent side and high airway pressure after intubation; ultrasound with a lung pulse and no lung point, and tube depth, decide (PLEU-08)."),
  ],
  traps=[
    ("“Respiratory distress with hypertension is a sign of tension”", "It is the odd one out: tension lowers blood pressure; tracheal deviation, quiet breath sounds and distended neck veins are all signs."),
    ("“Pneumothorax suspected in trauma: chest radiograph first”", "Not when the bedside signs are of tension (poor compliance, silent chest, shock): decompress first. The film is for the stable patient."),
    ("“Needle decompression is the definitive treatment”", "It is a bridge; the definitive treatment is a chest drain (Marrow keys tube thoracostomy for the ventilated COPD patient and for trauma with surgical emphysema and hypotension)."),
    ("“Pneumothorax during a subclavian line with stable vitals: needle decompression first”", "Marrow keys this, but stable vitals mean a simple pneumothorax: image, then drain. Decompression without imaging is only for tension. For Marrow pick its key; in practice and elsewhere, image first."),
  ],
  decode=[
    ("Which is NOT a sign of tension pneumothorax? [DocT GT]", "Respiratory distress with hypertension."),
    ("Ventilated trauma patient: hypotension, rising peak pressure, one silent side, cervical crepitus [DocT GT]", "Pneumothorax (tension) — decompress and drain."),
    ("Trauma, decreased breath sounds, poor compliance — condition and immediate step? [NEET 2025]", "Tension pneumothorax; needle decompression."),
    ("Ventilated COPD on PEEP 10, sudden desaturation and hypotension — definitive treatment? [Marrow]", "Tube thoracostomy (needle is temporising)."),
  ],
  punch="Tension is a clinical diagnosis — shock, a silent side, rising airway pressure — and is decompressed at the 4th–5th space just anterior to the mid-axillary line before any film, then drained; stable vitals mean image first.",
)

L['PLEU-05'] = dict(
  sub="Respiratory → Pleura → Open pneumothorax",
  step=3,
  intro="Step 3 has a second way to lose pleural pressure: a hole in the chest wall rather than in the lung. The pleural space then follows atmospheric pressure, and the mediastinum swings with each breath.",
  parts=[
    ('a', "**Penetrating trauma: a sucking chest wound; negative pleural pressure is lost.** When the wound is wide (ATLS: about two-thirds of the tracheal diameter or more), air takes the easier path through the wound rather than the trachea, so the lung on that side is not ventilated."),
    ('b', "**Mediastinal flutter: the mediastinum shifts away from the wound in inspiration and back towards it in expiration.** In inspiration the intact side’s pleural pressure falls while the open side stays atmospheric, so the mediastinum is pulled to the intact side; in expiration it swings back. The intact lung also loses volume with each swing."),
    ('c', "**It distorts the venae cavae (IVC torsion), so venous return falls further.** The swinging mediastinum kinks the great veins, adding a circulatory insult to the ventilatory one. Treatment: a three-sided occlusive dressing or vented chest seal (a fully sealed dressing can create tension), then a chest drain away from the wound, and surgical closure."),
  ],
  mimic=[
    ("Open vs tension pneumothorax", "Open: pleural pressure is atmospheric through a chest-wall hole and the mediastinum swings. Tension: pleural pressure is above atmospheric and the mediastinum is pushed steadily away."),
  ],
  traps=[
    ("“Seal the wound on all four sides”", "A full seal turns an open pneumothorax into tension if the lung is also leaking; tape three sides or use a vented seal."),
  ],
  decode=[
    ("[pattern] Sucking chest wound — first-aid dressing?", "Three-sided occlusive dressing (or vented seal), then a chest drain away from the wound."),
  ],
  punch="An open pneumothorax makes pleural pressure atmospheric, so the mediastinum swings to and fro and kinks the cavae; seal on three sides and drain elsewhere.",
)

L['PLEU-06'] = dict(
  sub="Respiratory → Pleura → Pneumothorax in the ICU",
  step=3,
  intro="Step 3 in the setting that matters most to you: the ventilated patient. Positive pressure drives air through any leak, the patient cannot complain, and the supine film hides the air, so the diagnosis rests on the ventilator and the monitor. The questions test the bedside signs, and what to do with a pneumothorax seen only on CT.",
  parts=[
    ('a', "**4–15% of ventilated patients; higher in ARDS (reduced by 48 h of paralysis); up to 50% of chest trauma victims.** Barotrauma follows high transpulmonary pressure in a lung with stiff and normal regions side by side. In ACURASYS, 48 hours of cisatracurium in early severe ARDS lowered pneumothorax (about 4% vs 12%), probably by removing asynchrony and large patient-generated swings. Pneumomediastinum and pneumopericardium from barotrauma are usually managed without a drain: keep plateau pressure under 30 cmH₂O and paralyse if the patient is fighting the ventilator."),
    ('b', "**Sudden unexplained deterioration, rising oxygen need, haemodynamic instability, a sudden rise in peak and plateau pressures.** Add surgical emphysema, which tracks from the mediastinum into the chest wall and neck. In a ventilated patient with these signs and a suspected pneumothorax, drain without waiting for a film. A rise in both peak and plateau points to the lung or chest (stiffness); a rise in peak with an unchanged plateau points to the airway or tube."),
    ('c', "**Occult pneumothorax: seen on CT but not on the chest X-ray; up to 15% in trauma, 64% in multitrauma; ultrasound detects 92–100%.** The air lies anteriorly in the supine patient, where the AP film does not show it (PLEU-07). Ultrasound of the anterior chest finds most of these."),
    ('d', "**Controversial: a randomised trial in ventilated trauma patients found no difference in respiratory distress between observation and a prophylactic drain.** This is OPTICC (Am J Surg 2021; 142 ventilated trauma patients): respiratory distress occurred in 38% of observed and 25% of drained patients, a difference that was not significant in an underpowered trial, and mortality was the same. About a quarter of observed patients went on to need a drain, rising to about 40% of those ventilated for 5 days or more. So a stable occult pneumothorax may be observed on positive pressure, with a low threshold to drain if it grows, the patient deteriorates or ventilation is prolonged."),
  ],
  mimic=[
    ("Pneumothorax vs blocked tube or bronchospasm on the ventilator", "Pneumothorax raises both peak and plateau pressure with one silent side; a blocked tube or bronchospasm raises peak with plateau unchanged."),
  ],
  traps=[
    ("“An occult pneumothorax is an indication for a chest tube”", "No; a stable occult pneumothorax may be observed even on positive pressure (OPTICC)."),
    ("“Any pneumothorax needing positive-pressure ventilation needs a chest tube”", "Also false; observation is acceptable for the stable occult one. Together these two distractors drew most of the 35% who missed the DocT GT question."),
    ("“All traumatic haemothoraces need VATS”", "Only a retained haemothorax after tube drainage (more than about 300 mL) does."),
  ],
  decode=[
    ("Trauma, haemopneumothorax drained — which is true? [DocT GT]", "Persistent air leak or recurrent pneumothorax despite a working tube → look for a tracheobronchial injury (bronchoscopy) (65%)."),
    ("Ventilated polytrauma on high PEEP, surgical emphysema and rising peak pressure — next? [Marrow]", "Chest tubes, without waiting for a film."),
    ("ARDS, asynchrony despite deep sedation, pneumopericardium — next? [Marrow]", "Neuromuscular blocker infusion."),
  ],
  extra=[dict(q="Persistent large air leak after chest trauma despite a working drain — what is it until proven otherwise?", a="A tracheobronchial injury; bronchoscopy.")],
  punch="On the ventilator, a pneumothorax shows as a sudden rise in peak and plateau with shock or desaturation, and is drained on those signs; one seen only on CT can be watched if the patient is stable.",
)

L['PLEU-07'] = dict(
  sub="Respiratory → Pleura → Chest X-ray and CT in pneumothorax",
  step=4,
  intro="Step 4 is about finding the air, and the chest X-ray fails in the patient who needs it most. In the supine patient air rises to the front of the chest and spreads over the lung instead of collecting at the apex, so there is no apical pleural line to see. The questions test the sign that replaces it.",
  parts=[
    ('a', "**Sensitivity: lateral decubitus 88%, erect 59%, supine 37%.** These are against CT. The supine AP film misses most pneumothoraces; in one ICU series about 30% were missed at first and half of those progressed to tension, and missed cases went on to tension far more often than recognised ones. The lateral decubitus film, affected side up, lets air rise to the lateral chest wall, where it is easy to see."),
    ('b', "**On a supine film air collects anteromedially and subpulmonically: the deep sulcus sign, a lucent upper quadrant, an unusually sharp hemidiaphragm.** In supine patients the anteromedial recess holds about 38% of pneumothoraces and the subpulmonic recess about 26%. Air in the lateral costophrenic sulcus makes it abnormally deep and lucent (the deep sulcus sign); air under the lung outlines the diaphragm unusually sharply, sometimes as two diaphragm lines (the double diaphragm sign, also a supine pneumothorax sign); air in front of the heart sharpens the cardiac border."),
    ('c', "**Mimic: a skin fold.** A skin fold is an edge — a band of density that ends abruptly, with lung markings continuing beyond it, and it often runs beyond the chest wall. A pneumothorax shows a thin white visceral pleural line with no lung markings beyond it."),
    ('d', "**CT is the gold standard: sizing, separating a bulla from a pneumothorax (avoids draining a bulla and creating a fistula), checking tube position.** A drain pushed into a large bulla in emphysema makes a bronchopleural fistula; CT shows which is which. After previous thoracic surgery adhesions loculate the air, so drains go in under CT or ultrasound guidance. Ultrasound beats the supine film but does not beat CT."),
  ],
  mimic=[
    ("Pneumothorax vs bulla", "Pneumothorax: pleural line parallel to the chest wall, no markings beyond. Bulla: wall concave towards the chest wall, thin strands may cross it; CT settles it."),
    ("Deep sulcus sign vs normal supine film", "A unilateral, unusually deep and lucent costophrenic angle in a supine patient is pneumothorax until proven otherwise."),
  ],
  traps=[
    ("“Visible lung point sign” on the X-ray", "The lung point is an ultrasound sign (PLEU-08); the supine X-ray sign is the deep sulcus."),
    ("“A radiolucent costophrenic angle after a jugular line is a skin fold or a normal supine variant”", "It is a supine pneumothorax (the deep sulcus sign)."),
    ("“Double diaphragm sign” as the wrong answer", "It too can appear in supine pneumothorax, so the image decides; DocT keys deep sulcus for its picture."),
    ("“Ultrasound is superior to both chest X-ray and CT”", "False (Marrow): ultrasound beats the supine film, but CT is still the reference standard."),
  ],
  decode=[
    ("Ventilated ICU patient, suspected pneumothorax — most suggestive supine X-ray finding? [DocT GT]", "Deep sulcus sign (87%)."),
    ("Supine portable film after a jugular line, lucent costophrenic angle — diagnosis? [DocT GT]", "Pneumothorax in a supine patient."),
    ("Ventilated trauma patient, acute hypoxia, image shown — the sign? [DocT GT]", "Deep sulcus sign."),
    ("False statement on ultrasound for pneumothorax? [Marrow]", "‘Ultrasound is superior to CXR and CT.’"),
  ],
  punch="Supine, the air goes to the front and the base, so look for a deep, lucent costophrenic angle rather than an apical line; the supine film misses most, and CT is the reference.",
)

L['PLEU-08'] = dict(
  sub="Respiratory → Pleura → Lung ultrasound for pneumothorax",
  step=4,
  intro="Step 4 moves to the bedside test that has replaced the supine film. Every sign rests on one fact: the visceral pleura can be seen only where it touches the parietal pleura. Air between them hides it, so anything generated by the visceral pleura — sliding, B-lines, the lung pulse — proves the layers are apposed at that point, and only the lung point proves air. This card was asked ten times, and the commonest error was treating absent sliding as a diagnosis.",
  parts=[
    ('a', "**Lung sliding present = no pneumothorax at that spot.** Sliding is the visceral pleura moving on the parietal pleura with breathing, seen at the pleural line about half a centimetre below the rib line (the ‘bat sign’ of two ribs and the line between them). Because air rises, scan the least dependent part — the anterior chest in a supine patient. Absent sliding is sensitive for pneumothorax but not specific: about 91% specificity in the critically ill, less in ARDS or after pleurodesis, because anything that stops the lung moving or glues the layers abolishes it (part e)."),
    ('b', "**B-lines present = rules out pneumothorax there (negative predictive value 100%).** B-lines are vertical, hyperechoic, laser-like artefacts that start at the pleural line, reach the edge of the screen without fading, erase A-lines and move with sliding. They arise from the visceral pleura and fluid-thickened septa beneath it, so they cannot form where air separates the layers. The lung pulse — the heartbeat transmitted to a still pleural line — rules out pneumothorax in the same way: no sliding, but the visceral pleura is there and touching. A-lines, horizontal reverberations of the pleural line, are seen both in normal lung and in pneumothorax, so they decide nothing alone."),
    ('c', "**Lung point: where sliding meets no sliding — 100% specific for pneumothorax.** It is the edge of the pneumothorax, where the collapsed lung touches the chest wall intermittently with breathing; on M-mode, seashore and barcode patterns alternate. In Lichtenstein’s study (Intensive Care Med 2000) it was never seen without a pneumothorax, but it was found in only 66% of pneumothoraces (75% of radio-occult ones): a totally collapsed lung never reaches the chest wall, so a large pneumothorax may have no lung point. The more lateral or posterior the lung point, the larger the pneumothorax."),
    ('d', "**Barcode (stratosphere) sign: the M-mode pattern of absent sliding. Normal is the seashore sign.** In M-mode the still chest wall gives horizontal lines above the pleural line; normally the moving lung below gives a granular ‘sand’ pattern (seashore). Without sliding, horizontal lines continue below the pleural line too, like a barcode. The barcode shows only that sliding is absent; it does not prove air. The sinusoid sign is something else — the lung line moving towards the pleural line in an effusion."),
    ('e', "**Other causes of absent sliding: mainstem intubation (the other lung), pleural adhesions, endobronchial obstruction, diaphragm paralysis.** Add atelectasis from a mucus plug, ARDS, pleurodesis and apnoea. Right after intubation, absent sliding on the left with a lung pulse is a right mainstem tube: the left lung is touching but not ventilated. Pull the tube back, do not drain the chest."),
  ],
  table=dict(title="Each sign, and what it decides at that spot", head=["Finding", "Means", "Pneumothorax?"], rows=[["Lung sliding", "pleurae apposed and moving", "**excluded** there"], ["B-lines", "visceral pleura apposed", "**excluded** there"], ["Lung pulse", "pleurae apposed, lung not ventilated", "**excluded**; think mainstem intubation"], ["Absent sliding + A-lines (barcode)", "pleurae not moving", "possible; needs a lung point"], ["Lung point", "edge of the air", "**confirmed** (specificity 100%)"]]),
  mimic=[
    ("Pneumothorax vs right mainstem intubation", "Both abolish sliding on the left. Lung pulse, no lung point and a tube too deep point to the tube; a lung point means pneumothorax."),
    ("Barcode vs seashore vs sinusoid", "Barcode: no sliding. Seashore: normal sliding. Sinusoid: effusion."),
  ],
  traps=[
    ("“Absent sliding, A-lines, lung pulse after intubation: drain the left chest”", "The lung pulse excludes pneumothorax; this is a mainstem intubation — adjust the tube. Only 22% got this DocT GT question right."),
    ("“B-lines or a lung pulse confirm the pneumothorax”", "Both exclude it; only the lung point confirms. A third of the cohort missed this (67%)."),
    ("“B-lines are horizontal hyperechoic lines”", "Those are A-lines; B-lines are vertical."),
    ("“Ultrasound is superior to both chest X-ray and CT”", "It beats the supine film; CT remains the reference standard."),
    ("“No lung point, so no pneumothorax”", "Sensitivity is only 66%; a completely collapsed lung has no lung point."),
  ],
  decode=[
    ("Absent sliding and barcode on M-mode — which finding confirms pneumothorax? [DocT; DocT GT]", "Lung point (67%)."),
    ("COPD intubated, SpO₂ falls, peak 45, no sliding on left with A-lines and lung pulse — next step? [DocT GT]", "Adjust the endotracheal tube (22%)."),
    ("Absent sliding; M-mode shows parallel horizontal lines above and below the pleural line — which sign is absent? [DocT GT]", "Seashore sign."),
    ("Tall young man, sudden dyspnoea, M-mode image — which sign? [Marrow]", "Barcode sign."),
  ],
  extra=[dict(q="Absent sliding with a lung pulse after intubation — diagnosis?", a="Mainstem intubation of the other side; pull the tube back.")],
  punch="Sliding, B-lines or a lung pulse at a spot exclude pneumothorax there; absent sliding and a barcode only raise the question, and the lung point alone answers it (specific, not sensitive).",
)

L['PLEU-09'] = dict(
  sub="Respiratory → Pleura → BLUE protocol",
  step=4,
  intro="Step 4 widens from one diagnosis to the breathless patient. The BLUE protocol (Lichtenstein, Chest 2008) is a decision tree: check sliding, then the anterior artefact (A or B), then the leg veins, then the posterolateral bases. Each combination is a ‘profile’ that points to one diagnosis. The questions give you the findings and ask for the diagnosis, and the hard one is separating ARDS from cardiogenic oedema.",
  parts=[
    ('a', "**Pulmonary oedema: B profile (sliding + bilateral anterior B-lines).** Three or more B-lines in an intercostal space (lung rockets) on both sides anteriorly, with sliding preserved: fluid in the septa of a lung that still moves. In the 2008 study: sensitivity 97%, specificity 95%. Cardiogenic oedema gives homogeneous B-lines from the bases up with a smooth pleural line and often effusions; ARDS gives patchy B-lines with spared areas, an irregular thickened pleural line, small subpleural consolidations and reduced sliding."),
    ('b', "**Pneumothorax: A′ profile (no sliding, A-lines) + lung point.** The prime means sliding is abolished. In the 2008 study there were 9 pneumothoraces and A′ with a lung point found 8 of them: sensitivity 88%, specificity 100%, as on the card and in Lichtenstein’s own later review. The 2008 abstract prints 81%, which cannot be a fraction of 9 and is a misprint. A′ without a lung point is not a diagnosis: it needs another test (CT or film), because the lung point may be absent in a complete collapse (PLEU-08)."),
    ('c', "**Pulmonary embolism: A profile + venous thrombosis.** The anterior lung looks normal (sliding with A-lines) because embolism does not wet the lung; a thrombus on venous compression of the legs supplies the diagnosis. Sensitivity 81%, specificity 99%."),
    ('d', "**COPD or asthma: A profile, veins free, no PLAPS.** A normal-looking lung, no thrombus and nothing at the bases: the cause is in the airways, which ultrasound cannot see. Sensitivity 89%, specificity 97%."),
    ('e', "**Pneumonia: A + PLAPS; B′; A/B; C.** PLAPS is the posterolateral alveolar or pleural syndrome (consolidation or effusion at the bases); B′ is B-lines with abolished sliding (inflammatory adhesion); A/B is B-lines on one side only; C is anterior consolidation. Combined, sensitivity 89%, specificity 94%. Overall, the profiles gave the right diagnosis in 90.5% of 260 patients, a figure drawn from experienced operators after excluding patients with unclear or multiple diagnoses, so it is likely to be lower in ordinary hands."),
  ],
  table=dict(title="BLUE profiles (Lichtenstein, Chest 2008)", head=["Profile", "Findings", "Diagnosis (sens/spec)"], rows=[["B", "sliding + bilateral anterior B-lines", "**pulmonary oedema** (97/95)"], ["A′ + lung point", "no sliding, A-lines, lung point", "**pneumothorax** (88/100)"], ["A + DVT", "normal anterior lung, venous thrombus", "**pulmonary embolism** (81/99)"], ["A, no DVT, no PLAPS", "normal anterior lung, nothing else", "**COPD or asthma** (89/97)"], ["A + PLAPS, B′, A/B, C", "basal consolidation, asymmetry, adhesion or anterior consolidation", "**pneumonia** (89/94)"]]),
  mimic=[
    ("Cardiogenic oedema vs ARDS", "Both are B-line lungs. Oedema: homogeneous, smooth pleural line, sliding kept, effusions. ARDS: patchy with spared areas, irregular pleural line, subpleural consolidations, reduced sliding."),
    ("Pulmonary embolism vs COPD", "Both give the A profile; the leg veins separate them."),
  ],
  traps=[
    ("“Irregular pleural line with subpleural consolidations and B-lines = cardiogenic oedema”", "That pattern is ARDS; cardiogenic oedema has a smooth pleural line and uniform B-lines. Only 44% got this right."),
    ("“Diffuse bilateral B-lines with sliding could be pneumothorax or massive effusion”", "B-lines exclude pneumothorax, and an effusion is an anechoic space at the bases, not a B-line field."),
    ("“A′ profile alone diagnoses pneumothorax”", "Not without a lung point."),
  ],
  decode=[
    ("Acute dyspnoea, more than 3 B-lines per field with preserved sliding — diagnosis? [DocT]", "Pulmonary oedema (86%)."),
    ("Multiple bilateral B-lines in all zones in a ventilated patient — diagnosis? [DocT GT]", "Alveolar (interstitial) oedema (87–93%)."),
    ("Irregular pleural line, subpleural consolidation, B-lines in the same space, bilateral infiltrates — diagnosis? [DocT GT]", "ARDS (44%)."),
    ("Right: no sliding, no B-lines, lung point, barcode — diagnosis? [DocT GT]", "Pneumothorax (94%)."),
  ],
  punch="BLUE reads sliding, then A or B anteriorly, then the leg veins, then the bases: B profile is oedema, A′ with a lung point is pneumothorax, A with a clot is embolism, A with nothing is COPD or asthma, and the rest is pneumonia.",
)

L['PLEU-10'] = dict(
  sub="Respiratory → Pleura → BTS management of primary spontaneous pneumothorax",
  step=5,
  intro="Step 5 turns to treatment. The card is BTS 2010; the 2023 BTS pleural guideline kept its spirit (treat symptoms, not size) but went further, and an exam may test either.",
  parts=[
    ('a', "**Large = more than 2 cm from lung margin to chest wall at the level of the hilum; symptoms matter more than size.** A 2 cm rim at the hilum is roughly half the hemithorax by volume. In BTS 2023 size no longer decides whether to intervene; it mainly tells you whether a drain can safely be placed at the bedside."),
    ('b', "**Small and not breathless: consider discharge, outpatient review in 2–4 weeks.** BTS 2023 extends this: a minimally symptomatic PSP can be managed conservatively whatever its size, after Brown (NEJM 2020; 316 patients with moderate to large PSP): re-expansion at 8 weeks 94.4% with observation vs 98.5% with intervention, non-inferior, and only 15% of the observed group needed a procedure."),
    ('c', "**Large or breathless: needle aspiration, 16–18 G, up to 2.5 L; success = less than 2 cm and breathing better.** Aspiration works as well as a large-bore drain and shortens stay. BTS 2023 adds an ambulatory device as an option, by shared decision: in RAMPP (Hallifax, Lancet 2020; 236 patients) it cut median stay from 4 days to 0 and needed fewer further procedures, at the cost of more adverse events."),
    ('d', "**If aspiration fails: small-bore chest drain, 8–14 Fr, and admit; suction is not routine.** Bilateral or haemodynamically unstable pneumothorax goes straight to a drain."),
  ],
  mimic=[
    ("BTS 2010 vs BTS 2023 for PSP", "2010: size and breathlessness choose observation or aspiration. 2023: symptoms and high-risk features choose; conservative care allowed regardless of size; aspiration, ambulatory device or drain by shared decision."),
  ],
  traps=[
    ("“Primary pneumothorax is first treated with a large-bore drain”", "No; aspiration (or observation if symptoms are minimal) first (PLEU-13g)."),
  ],
  decode=[
    ("[pattern] Young man, first PSP, 3 cm rim at the hilum, mildly breathless — first step (BTS 2010)?", "Needle aspiration."),
    ("[pattern] Large PSP, minimal symptoms — acceptable under BTS 2023?", "Conservative management."),
  ],
  punch="For primary pneumothorax, breathlessness, not the rim, chooses the treatment: observe if comfortable, aspirate if breathless, drain small-bore if aspiration fails; BTS 2023 allows observation whatever the size.",
)

L['PLEU-11'] = dict(
  sub="Respiratory → Pleura → BTS management of secondary spontaneous pneumothorax",
  step=5,
  intro="Step 5 continues with the patient who has no reserve. Because a small leak can cause respiratory failure in diseased lung (PLEU-03), the thresholds are lower and every patient is admitted.",
  parts=[
    ('a', "**Treated as secondary: underlying lung disease, or age over 50 with a significant smoking history.** Over 50 with smoking, occult emphysema is likely even without a diagnosis, so the patient is managed as secondary. BTS 2023 keeps this as a high-risk feature."),
    ('b', "**More than 2 cm or breathless: chest drain 8–14 Fr at once.** Aspiration fails more often in diseased lung, and the patient cannot afford a failed attempt. Ambulatory devices have weak evidence here: in a small 2021 trial (Walker, 41 patients) length of stay was no shorter, and one device, an 8 Fr pleural vent, failed early in 6 of 13 patients against 3 of 20 with a standard drain (46% vs 15%, not significant), so an ambulatory device is not a routine choice in SSP."),
    ('c', "**1–2 cm: aspirate; if still more than 1 cm, chest drain.**"),
    ('d', "**Less than 1 cm: admit, high-flow oxygen, observe for 24 hours.** So not every secondary pneumothorax needs a tube; the small one is observed. High-flow oxygen speeds reabsorption of the air (it washes nitrogen out of the blood), but in CO₂-retaining COPD it is titrated to target saturation."),
    ('e', "**All admitted for at least 24 h; thoracic surgical referral at 3–5 days for a persistent leak or failure to re-expand (thoracotomy with pleurectomy). No air travel until resolved; no diving unless treated surgically.** Open pleurectomy has the lowest recurrence, but VATS is now the usual approach for its lower morbidity, and BTS also lists a second ipsilateral pneumothorax, and a first contralateral one as indications. For a persistent leak in someone unfit for surgery, autologous blood patch or endobronchial valves are options."),
  ],
  mimic=[
    ("Secondary vs primary pneumothorax management", "Secondary: always admit, drain if more than 2 cm or breathless, aspirate only at 1–2 cm, observe under 1 cm. Primary: observe or aspirate, often as an outpatient."),
  ],
  traps=[
    ("“Most should be treated with thoracotomy, stapling of blebs and pleural abrasion” as a true statement", "That is old textbook wording; surgery today is for persistent leak, failure to re-expand or recurrence. DocT GT keys a different statement as false (‘all patients with secondary pneumothorax don’t need tube thoracostomy’), yet that one is true by BTS: under 1 cm is observed. Statement C is the more defensible false one; for DocT pick its key. Only 53% got it."),
    ("“Severe dyspnoea, cyanosis, large pneumothorax in a smoker of 50: oxygen only”", "Large and breathless in a patient managed as secondary means a drain; DocT keys decompression then tube (98%)."),
  ],
  decode=[
    ("COPD, no air entry on the left — which is false about management? [DocT GT]", "Keyed: ‘All patients with secondary pneumothorax don’t need tube thoracostomy’ (53%; key disputed)."),
    ("50-year-old smoker, severe dyspnoea, cyanosis, large pneumothorax on CT — next step? [DocT]", "Needle decompression then chest tube (98%)."),
    ("Long-standing COPD, sudden breathlessness, hypercapnia — diagnosis? [DocT]", "Spontaneous (secondary) pneumothorax (68%)."),
  ],
  punch="Secondary pneumothorax is treated harder because the lung has no reserve: admit everyone, drain if over 2 cm or breathless, aspirate at 1–2 cm, observe under 1 cm with oxygen, and refer to surgery for a leak lasting days.",
)

L['PLEU-12'] = dict(
  sub="Respiratory → Pleura → Chest drain insertion and removal",
  step=6,
  intro="Step 6 is the drain itself. The safe triangle keeps the tube away from the heart, liver, spleen and the long thoracic nerve, and the rules for removal are mostly about not clamping a drain that is still doing its job.",
  parts=[
    ('a', "**Safe triangle: the lateral edge of pectoralis major, the anterior (lateral) edge of latissimus dorsi, the line of the 5th intercostal space; apex at the base of the axilla.** Below the 5th space the diaphragm, liver and spleen rise in expiration. Go just above the rib, because the intercostal vessels and nerve run under the lower border of the rib above. For air, BTS prefers a small-bore drain inserted by Seldinger technique (guidewire, dilator, drain); large-bore drains for trauma or haemothorax go in by blunt dissection, a finger sweeping the pleura before the tube, and a trocar is never used to push a drain in."),
    ('b', "**Large anterior pneumothorax: apico-anterior approach.** The 2nd intercostal space in the mid-clavicular line is an alternative for an apical pneumothorax, with the cosmetic and muscle-bulk drawbacks of the front of the chest."),
    ('c', "**Removal: lung expanded and air leak stopped; suction off; clamp for up to 12 h after the leak ceases; chest X-ray at 24 h, then remove.** BTS 2010 does not advise routine clamping for pneumothorax, and a bubbling drain must never be clamped, because the leak continues and can produce tension. The usual practice is to remove the drain once bubbling has stopped and the film shows re-expansion, pulling it out during expiration or a Valsalva manoeuvre so that air is not sucked in."),
  ],
  mimic=[
    ("Seldinger vs blunt dissection", "Seldinger: small-bore, for air or free fluid. Blunt dissection: large-bore, for blood, trauma or thick fluid. Never a trocar."),
  ],
  traps=[
    ("“Insert just below the rib”", "Just above the rib; the bundle runs under the rib above."),
    ("“Clamp a bubbling drain before removal”", "Never; clamping a drain that is still leaking can cause tension."),
  ],
  decode=[
    ("[pattern] Borders of the triangle of safety?", "Pectoralis major, latissimus dorsi, 5th intercostal space, apex below the axilla."),
    ("[pattern] Should a chest drain for pneumothorax be clamped before removal (BTS)?", "Not routinely; never if bubbling."),
  ],
  punch="Drains go through the safe triangle, just above a rib, small-bore by Seldinger for air, and come out when the lung is up and bubbling has stopped, without routine clamping.",
)

L['PLEU-13'] = dict(
  sub="Respiratory → Pleura → Review: true or false",
  step=1,
  intro="This review runs the whole story from step 1 (the pleura) to step 5 (treatment). Each statement is a belief the questions show people hold.",
  parts=[
    ('a', "**False: the parietal pleura is supplied by systemic arteries.** Bronchial arteries supply the visceral pleura (PLEU-01)."),
    ('b', "**False: normal pleural fluid pH is 7.62.** It holds more bicarbonate than plasma, so it is alkaline (PLEU-02)."),
    ('c', "**False: a supine chest film has a sensitivity of 37%.** Air lies anteriorly and the film looks through it (PLEU-07)."),
    ('d', "**True: the lung point is 100% specific.** But only about two-thirds sensitive (PLEU-08)."),
    ('e', "**False: B-lines exclude a pneumothorax.** They are made by the visceral pleura, which air would hide (PLEU-08)."),
    ('f', "**True: large is more than 2 cm at the hilum (BTS 2010).** In BTS 2023, symptoms rather than size decide treatment (PLEU-10)."),
    ('g', "**False: primary spontaneous pneumothorax is first treated with needle aspiration.** Or observed if symptoms are minimal (PLEU-10)."),
  ],
  mimic=[
    ("Lung point vs B-lines", "Lung point confirms pneumothorax; B-lines exclude it."),
  ],
  traps=[
    ("“Pleuritic pain comes from the visceral pleura”", "Only half the cohort knew it comes from the parietal pleura."),
  ],
  decode=[
    ("Chest pain caused by respiratory disease usually originates from? [DocT GT]", "Parietal pleura (50%)."),
  ],
  punch="Parietal pleura is systemic and painful, normal fluid is alkaline, the supine film misses most pneumothoraces, B-lines exclude one and a lung point confirms it, and primary pneumothorax starts with aspiration or observation.",
)

FLAGS = {}
FLAGS['PLEU-03'] = "Card a is wrong: 24 and 9.8 per lakh a year (men, women) are the English GP consultation rates for all pneumothorax, primary and secondary combined (Gupta, Thorax 2000), not the incidence of primary pneumothorax. BTS 2010 gives PSP as 18–28 per lakh a year in men and 1.2–6 in women (hospital admissions 16.7 and 5.8, PSP and SSP combined). Explanation restates the card and corrects it. Also not on the card: catamenial pneumothorax (DocT GT) and subclavian > jugular risk with ‘abort and film’ (Marrow); explanation covers both."
FLAGS['PLEU-04'] = "Card is right. Marrow keys needle decompression (5th ICS MAL) for a pneumothorax with STABLE vitals during a subclavian line; stable vitals mean simple pneumothorax: image, then drain. Explanation says pick Marrow’s key for Marrow. Consider adding to c: ‘needle is temporising; definitive = chest drain 5th ICS just anterior to MAL’ (two Marrow keys) and the ATLS 10th wording ‘4th/5th ICS just anterior to the mid-axillary line in adults; 2nd ICS MCL still for children’."
FLAGS['PLEU-06'] = "Not an error but incomplete: b should add surgical emphysema (Marrow). Trial in d is OPTICC (Am J Surg 2021, 142 patients): respiratory distress 38% observed vs 25% drained, not significant in an underpowered trial, so ‘no difference’ overstates it; ~25% of observed patients needed a drain (~40% if ventilated 5 days or more); explanation adds this."
FLAGS['PLEU-10'] = "Dated: the card is BTS 2010. BTS 2023 (Roberts, Thorax 2023) lets symptoms and high-risk features, not size, decide; allows conservative management of a minimally symptomatic PSP regardless of size (Brown NEJM 2020); and adds ambulatory devices as an option by shared decision (RAMPP, Hallifax Lancet 2020). Explanation teaches both."
FLAGS['PLEU-11'] = "DocT GT7 key (‘all patients with secondary pneumothorax don’t need tube thoracostomy’ as the false statement) is disputed: BTS and the card observe SSP <1 cm, so it is true; ‘most should have thoracotomy with stapling’ is the more defensible false statement. Card e’s ‘thoracotomy with pleurectomy’ is dated wording; VATS is now usual, and BTS surgical indications also include a second ipsilateral or first contralateral pneumothorax. Ambulatory devices are weakly supported in SSP (Walker, ERJ 2021, 41 patients: no shorter stay; early failure 46% with an 8 Fr pleural vent vs 15% with a standard drain, not significant)."
FLAGS['PLEU-12'] = "Card c (‘clamp for up to 12 h after the leak ceases; chest X-ray at 24 h, then remove’) is not BTS practice: BTS 2010 does not recommend routine clamping for pneumothorax and a bubbling drain is never clamped (the card’s watch line says so). Explanation restates the card and teaches removal once bubbling has stopped and the lung is up. Seldinger vs blunt dissection is not on the card; explanation adds it."
