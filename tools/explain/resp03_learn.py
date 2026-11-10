# RESP03 — Explain v3 ("Learn" depth): respiratory failure in special situations — sepsis, the post-operative lung, intra-abdominal hypertension and obesity. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP03.md (11 questions; RSC-12 obesity physiology asked 5 times). Fields as TOX01, plus SPINE, PRIMER and step.
# Most cards have no linked question and get short explanations with [pattern] decode items.

SPINE = [
  ("Sepsis: oxygen and ARDS ventilation", "In sepsis-induced hypoxaemia high-flow nasal oxygen is preferred over NIV, and once ARDS develops the ARDS rules apply — 6 mL/kg PBW and plateau <30 — while lungs without ARDS gain nothing from going lower than 8–10 mL/kg (PReVENT)."),
  ("What goes wrong after surgery", "Atelectasis is the commonest post-operative pulmonary complication, and the Melbourne Group Score calls a complication when 4 or more of 8 items occur in the same 24 hours."),
  ("Protecting the lung in theatre", "Low tidal volume protects the lung during surgery, routinely high PEEP does not, and the pressure that tracks complications is driving pressure; NIV is suggested when failure follows surgery."),
  ("The stiff chest wall", "Raised abdominal pressure stiffens the chest wall, not the lung, so plateau pressure overstates lung stress and the targets are adjusted for abdominal pressure or read as transpulmonary pressure."),
  ("Obesity: lungs, drive and airway", "Obesity lowers FRC towards closing capacity, so dependent airways close and the lung collapses; some patients also lose ventilatory drive (obesity hypoventilation), and the airway is harder to secure."),
  ("Ventilating and weaning the obese", "Set tidal volume on predicted, not actual, weight, use enough PEEP to keep FRC above closing pressure, prone if needed with care for the abdomen, and extubate to NIV or CPAP."),
]

PRIMER = "Predicted body weight comes from height and sex, not from what the patient weighs, because lung size follows height; tidal volumes are set in mL/kg of it. The respiratory system is the lung and the chest wall (rib cage, diaphragm and abdomen) in series, so its compliance falls if either one stiffens, and the plateau pressure (end-inspiratory pressure at zero flow) reflects both. Driving pressure is plateau minus PEEP, the pressure that stretches each breath; transpulmonary pressure is alveolar minus pleural pressure (estimated from an oesophageal balloon), the pressure that stretches the lung itself. Functional residual capacity (FRC) is the volume left at the end of a quiet breath; when it falls below closing capacity, small dependent airways shut during normal breathing and the alveoli behind them collapse."

L = {}

L['RSC-01'] = dict(
  sub="Respiratory → Sepsis → Oxygen and non-invasive support",
  step=1,
  intro="The deck opens with the septic patient whose lungs fail before any tube goes in. The guidance answers two practical questions — how much oxygen to aim for, and how to give it without intubating.",
  parts=[
    ('a', "**2021: insufficient evidence to recommend conservative over usual targets. 2026: titrate to a conservative or a liberal target by patient; SpO₂ 90–96% is taught (SEP-50).** Trials of conservative oxygen in the ICU have not shown a clear benefit overall, so the 2026 guideline makes only a conditional, low-certainty suggestion to titrate to either target by patient factors; most trials compared a lower target of about 90–93% with a higher one of 96% or more, and the panel reported aiming for 90–96%. The band avoids both hypoxaemia and sustained hyperoxia."),
    ('b', "**High-flow nasal oxygen over NIV (weak recommendation).** In hypoxaemic (non-hypercapnic) failure NIV by face mask is poorly tolerated and can let the patient take large, injurious breaths. High flow delivers a reliable FiO₂ (21–100%) at up to 60 L/min, washes out dead space and gives a little PEEP, and in FLORALI (which excluded patients with PaCO₂ >45 mmHg) it lowered 90-day mortality (12% vs 23% standard oxygen vs 28% NIV) without a significant difference in the intubation rate overall (38% vs 47% vs 50%). The 2026 update keeps a conditional suggestion for high flow as the initial therapy over NIV."),
    ('c', "**Post hoc: point estimates suggested possible harm with conservative oxygen in sepsis; liberal oxygen may be preferred.** In the 251 patients with sepsis in ICU-ROX, 90-day mortality was 36.2% with conservative oxygen vs 29.2% with usual oxygen, a difference that was not statistically significant (P = 0.24) in a post hoc, underpowered analysis. It is a signal to avoid driving septic patients to low saturations, not proof of harm."),
  ],
  mimic=[
    ("Hypoxaemic vs hypercapnic failure", "Hypoxaemic, non-hypercapnic failure (sepsis, pneumonia): high flow first. Hypercapnic failure (COPD, obesity hypoventilation): NIV first (RSC-13)."),
  ],
  traps=[
    ("“Surviving Sepsis suggests NIV over high flow in septic hypoxaemia” (RSC-16a)", "It is the other way round: high flow over NIV."),
    ("“FLORALI showed fewer intubations with high flow”", "The overall intubation rate did not differ significantly (P = 0.18); fewer intubations were seen only in the subgroup with P/F ≤200, and 90-day mortality was lower."),
  ],
  decode=[
    ("[pattern] Septic patient, SpO₂ 86% on face mask, not hypercapnic — preferred support?", "High-flow nasal oxygen over NIV."),
  ],
  punch="In sepsis-induced hypoxaemia give high-flow nasal oxygen rather than NIV, and do not chase a low saturation: the ICU-ROX sepsis signal leaned against conservative oxygen.",
)

L['RSC-02'] = dict(
  sub="Respiratory → Sepsis → PReVENT: low tidal volume without ARDS",
  step=1,
  intro="Many septic patients are ventilated without having ARDS. PReVENT asked whether the ARDS tidal volume should be used in them too.",
  parts=[
    ('a', "**Ventilated ICU patients without ARDS.** Patients expected not to be extubated within 24 hours, with ARDS (Berlin) an exclusion (Simonis, JAMA 2018; 961 patients)."),
    ('b', "**Low tidal volume (4–6 mL/kg PBW) vs intermediate (8–10 mL/kg).** The low arm started at 6 and came down by 1 mL/kg each hour towards 4 mL/kg; the intermediate arm started at 10. PaCO₂ on day 1 was higher in the low arm, but the use and duration of sedatives and neuromuscular blockers did not differ."),
    ('c', "**No difference in ventilator-free days.** Ventilator-free days at day 28 were the same in both arms (median 21), as were mortality, ICU and hospital stay, and complications such as ARDS, pneumonia, severe atelectasis and pneumothorax. Surviving Sepsis 2026 accordingly suggests 6–8 mL/kg rather than 4 to <6 mL/kg in sepsis-associated hypoxaemic failure without ARDS."),
  ],
  mimic=[
    ("PReVENT vs ARMA", "ARMA (ARDS): 6 vs 12 mL/kg, mortality fell from about 40% to 31%. PReVENT (no ARDS): 4–6 vs 8–10 mL/kg, no difference. The proof of low tidal volume is in ARDS."),
  ],
  traps=[
    ("“PReVENT showed benefit of low tidal volume without ARDS” (RSC-16b)", "It showed no difference; an intermediate 8–10 mL/kg PBW was as good."),
  ],
  decode=[
    ("[pattern] Ventilated patient without ARDS — does a tidal volume of 4–6 rather than 8–10 mL/kg improve outcome?", "No: PReVENT found no difference in ventilator-free days."),
  ],
  punch="Without ARDS, going down to 4–6 mL/kg PBW gained nothing over 8–10 mL/kg in PReVENT; the 6 mL/kg rule belongs to ARDS.",
)

L['RSC-03'] = dict(
  sub="Respiratory → Sepsis → Ventilating sepsis-induced ARDS",
  step=1,
  intro="When sepsis does cause ARDS, the ventilator becomes part of the treatment and can itself injure the lung. The one real question checks the core of lung protection, and it is the same set of rules as any ARDS.",
  parts=[
    ('a', "**Tidal volume 6 mL/kg PBW** (strong recommendation). A smaller breath limits the stretch of the small aerated part of the ARDS lung; the ARDSNet protocol targets 6 mL/kg within a range of 4–8. The resulting rise in PaCO₂ is accepted."),
    ('b', "**Plateau pressure <30 cmH₂O.** Plateau pressure is the end-inspiratory alveolar pressure; above 30 the risk of over-distension and barotrauma rises, so the tidal volume is lowered further if needed."),
    ('c', "**Avoid incremental-PEEP recruitment manoeuvres (barotrauma).** In the ART trial a staircase of rising PEEP (25, 35, 45 cmH₂O) followed by decremental titration increased 28-day mortality (55.3% vs 49.3%) and barotrauma (5.6% vs 1.6%), so it is recommended against (strong). Surviving Sepsis 2021 still suggested traditional, sustained-inflation recruitment in moderate–severe ARDS."),
    ('d', "**Prone ventilation as needed.** Prone for more than 12 hours a day is advised in moderate–severe ARDS; PROSEVA enrolled P/F <150 on FiO₂ ≥0.6 and PEEP ≥5 after a stabilisation period and roughly halved 28-day mortality (16% vs 33%), because turning makes ventilation and lung stress more even."),
    ('e', "**Intermittent neuromuscular blocker boluses rather than infusion.** After ROSE found no benefit from routine early infusion, the guideline suggests boluses, keeping an infusion for persistent dyssynchrony or the need for deep sedation."),
    ('f', "**VV-ECMO in refractory cases.** For severe ARDS when conventional ventilation fails, in a centre that can provide it."),
  ],
  mimic=[
    ("Traditional recruitment vs incremental-PEEP strategy", "Sustained inflation was suggested (weak) in 2021; the incremental PEEP staircase of ART is recommended against (strong)."),
  ],
  traps=[
    ("“Permissive hypercapnia with tidal volumes targeting a normal PaCO₂”", "These contradict each other: permissive hypercapnia means accepting a high PaCO₂ so that the tidal volume can stay low."),
    ("“High tidal volume with high PEEP protects the other organs”", "Large breaths cause ventilator-induced lung injury, whose mediators spread to other organs; low tidal volume protects them too."),
  ],
  decode=[
    ("CAP, ARDS with P/F 120 and AKI (MODS) — lung-protective strategy by the ARDSNet protocol? [DocT QBank, 97% right]", "Low tidal volume (4–8 mL/kg PBW) with plateau pressure <30 cmH₂O."),
  ],
  punch="Septic ARDS is ventilated as any ARDS: 6 mL/kg PBW, plateau <30, prone when severe, NMB boluses not infusions, no incremental-PEEP staircase, and ECMO when all else fails.",
)

L['RSC-04'] = dict(
  sub="Respiratory → Post-operative lung → Pulmonary complications",
  step=2,
  intro="The second part of the deck moves to the lung after surgery. Anaesthesia and an abdominal or thoracic wound reduce FRC, weaken coughing and stiffen breathing for days, so the complications on this card follow.",
  parts=[
    ('a', "**Atelectasis.** General anaesthesia causes collapse of dependent lung within minutes of induction, from high FiO₂ (absorption), loss of muscle tone and the diaphragm pushed up by the abdomen; after surgery, pain and opioids limit deep breaths, so it persists."),
    ('b', "**Bronchospasm, pneumonia, exacerbation of chronic lung disease, upper airway obstruction, sleep-apnoea complications, pleural effusion, tracheal injury, abdominal compartment syndrome.** Most follow from collapse, retained secretions or residual drugs; the last links to RSC-10."),
    ('c', "**Older age, emergency surgery, hypoalbuminaemia, heart failure, COPD or smoking, lower respiratory tract infection.** Patient factors add to the procedure’s own risk, which is highest for thoracic, upper abdominal, aortic and neurosurgical operations and long or emergency surgery. A serum albumin below 35 g/L is the most useful laboratory marker of risk (ACP 2006), reflecting frailty, poor nutrition and weak respiratory muscles."),
  ],
  mimic=[
    ("Atelectasis vs pneumonia after surgery", "Atelectasis appears early (first days), with volume loss on the X-ray; pneumonia brings purulent sputum, a rising white count and consolidation (RSC-05)."),
  ],
  traps=[
    ("“Pneumonia is the commonest post-operative pulmonary complication”", "Atelectasis is (RSC-16g); it is also the soil in which pneumonia grows."),
  ],
  decode=[
    ("[pattern] Commonest post-operative pulmonary complication?", "Atelectasis."),
    ("[pattern] Which pre-operative laboratory value predicts pulmonary complications?", "A low serum albumin."),
  ],
  punch="Atelectasis is the commonest post-operative pulmonary complication; age, emergency surgery, low albumin, heart failure, COPD or smoking and recent chest infection raise the risk.",
)

L['RSC-05'] = dict(
  sub="Respiratory → Post-operative lung → Melbourne Group Score",
  step=2,
  intro="Trials of lung protection need an agreed way to say that a complication has happened. The Melbourne Group Score turns a bedside judgment into a count of eight items.",
  parts=[
    ('a', "**A post-operative pulmonary complication: 4 or more of 8 items in the same 24-hour period.** No single item is specific; requiring four together in one day makes the diagnosis reliable enough to compare groups."),
    ('b', "**New abnormal breath sounds; yellow or green sputum; temperature >38°C and SpO₂ <90% on room air, each on more than one consecutive day.** The sputum must differ from the patient’s usual sputum before surgery."),
    ('c', "**Chest X-ray collapse or consolidation; unexplained white cell count >11 × 10⁹/L; positive sputum culture; physician’s diagnosis of chest infection or antibiotic prescribed for it.** Published versions give the white count as >11.2 × 10⁹/L, and the later version (MGS-2) replaces breath sounds with readmission to, or a prolonged stay in, ICU or HDU for a respiratory problem."),
  ],
  mimic=[],
  traps=[
    ("“Any one item, such as fever with a raised white count, makes a pulmonary complication”", "Four of the eight are needed, within one 24-hour period (RSC-16c)."),
  ],
  decode=[
    ("[pattern] Melbourne Group Score — how many items define a post-operative pulmonary complication?", "4 or more of 8, in the same 24 hours."),
  ],
  punch="The Melbourne Group Score diagnoses a post-operative pulmonary complication when 4 or more of its 8 clinical, radiological and laboratory items occur within one 24-hour period.",
)

L['RSC-06'] = dict(
  sub="Respiratory → Post-operative lung → Prevention, ICOUGH and ERAS",
  step=3,
  intro="Since atelectasis is the root of most complications (RSC-04), prevention is mostly about keeping FRC up and secretions moving. The one real question asks for the least invasive way to raise FRC in an obese patient after surgery.",
  parts=[
    ('a', "**Lung-protective ventilation, good analgesia, restrictive fluids, low-dose relaxant with full reversal, early mobilisation, physiotherapy, upright position, CPAP/NIV.** Pain-free deep breathing and coughing reopen collapsed lung; residual neuromuscular block weakens the upper airway and cough; sitting up lets the abdomen fall away from the diaphragm. Going from supine to upright raises FRC substantially, which is why position comes before pressure."),
    ('b', "**Incentive spirometry (10 times an hour), Coughing and deep breathing, Oral care (twice daily), Understanding (education), Getting out of bed (3 times a day), Head of bed up 30–45°.** A nursing bundle from Boston University Medical Center; in its before-and-after evaluation pneumonia fell from 2.6% to 1.6% and unplanned intubation from 2.0% to 1.2%, by keeping the lungs expanded and secretions cleared."),
    ('c', "**Enhanced Recovery After Surgery: pre-, intra- and post-operative bundle (carbohydrate loading, no prolonged fasting, opioid-sparing and regional analgesia, early feeding and mobilisation).** Each element shortens the time the patient spends weak, sedated and in bed."),
  ],
  mimic=[
    ("Raising FRC by posture vs by PEEP", "Sitting up is the first, non-invasive step; PEEP or CPAP raises FRC further but is the escalation and can lower venous return."),
  ],
  traps=[
    ("“Obese patient supine with falling SpO₂ after surgery: first apply PEEP 10”", "PEEP would raise FRC, but the question asks for the least invasive step: sitting him up 45° comes first. Only 73% chose it on DocT GT."),
    ("“ERAS is Early Rehabilitation After Surgery”", "The standard expansion is Enhanced Recovery After Surgery."),
  ],
  decode=[
    ("Obese post-operative patient, supine, hypoxaemic — least invasive way to improve FRC? [DocT GT, 73% right]", "Elevate the head of the bed to a 45° semi-recumbent position."),
  ],
  punch="Prevention keeps FRC up and secretions moving: sit the patient up first, then add pressure if needed, with good analgesia, full reversal, the ICOUGH bundle and ERAS.",
)

L['RSC-07'] = dict(
  sub="Respiratory → Post-operative lung → IMPROVE vs PROVHILO",
  step=3,
  intro="Two trials split lung protection in theatre into its parts. IMPROVE tested the whole package against old-style large breaths; PROVHILO kept the tidal volume low in both arms and tested PEEP alone.",
  parts=[
    ('a', "**IMPROVE (Futier): VT 6–8 + PEEP 6–8 + recruitment vs VT 10–12, no PEEP, no recruitment (400 patients). PROVHILO: PEEP 12 + recruitment vs PEEP ≤2 without recruitment, same low VT.** IMPROVE studied major abdominal surgery in patients at intermediate to high risk; PROVHILO studied 900 at-risk patients having open abdominal surgery, with 8 mL/kg in both arms."),
    ('b', "**IMPROVE: complications 10.5% vs 27.5%; less atelectasis and pneumonia; hospital stay 2 days shorter. PROVHILO: no difference in pulmonary complications; more hypotension and vasoactive drugs with high PEEP.** IMPROVE’s 10.5% vs 27.5% is a composite of major pulmonary and extrapulmonary complications within 7 days; fewer patients needed NIV or intubation (5% vs 17%). PROVHILO’s complication rates were 40% vs 39%. Since only PEEP differed in PROVHILO, the benefit in IMPROVE probably came mostly from leaving large tidal volumes behind."),
  ],
  mimic=[
    ("PROVHILO vs PROBESE", "Both found no benefit from high PEEP with recruitment and more hypotension; PROBESE did it in obese patients (RSC-14)."),
  ],
  traps=[
    ("“PROVHILO showed fewer complications with high PEEP” (RSC-16d)", "No difference; more hypotension."),
  ],
  decode=[
    ("[pattern] Open abdominal surgery, low VT in both arms, PEEP 12 + recruitment vs PEEP ≤2 — result?", "No fewer pulmonary complications, more hypotension (PROVHILO)."),
  ],
  punch="Low tidal volume protects the lung in theatre (IMPROVE); routinely high PEEP adds hypotension without fewer complications (PROVHILO).",
)

L['RSC-08'] = dict(
  sub="Respiratory → Post-operative lung → Driving pressure and FiO₂",
  step=3,
  intro="If PEEP alone does not help (RSC-07), which number does? Pooling the surgical trials pointed to driving pressure; the card ends with the other setting that touches atelectasis, FiO₂.",
  parts=[
    ('a', "**17 trials, 2250 patients: driving pressure was the variable linked to post-operative pulmonary complications (odds ratio 1.16 per cmH₂O).** Driving pressure is tidal volume divided by compliance, so it scales the breath to the lung actually open; tidal volume was not associated (OR 1.05), and PEEP alone had too small an effect to enter the model (Neto, Lancet Respir Med 2016)."),
    ('b', "**More complications. PEEP helps only if it lowers driving pressure.** If PEEP recruits, compliance rises and driving pressure falls; if it only over-distends, driving pressure rises and so do complications (odds ratio about 3 when a PEEP increase raised driving pressure)."),
    ('c', "**No effect on short-term mortality; high FiO₂ may increase atelectasis.** Pure oxygen in poorly ventilated alveoli is absorbed and not replaced by nitrogen, so the alveoli collapse."),
  ],
  mimic=[],
  traps=[
    ("“More PEEP is always more protective”", "Only when it lowers driving pressure; PEEP that raises it is linked to more complications."),
  ],
  decode=[
    ("[pattern] Which intra-operative ventilator variable is associated with post-operative pulmonary complications?", "Driving pressure."),
  ],
  punch="In theatre driving pressure, not tidal volume or PEEP alone, tracks pulmonary complications; PEEP helps only if it lowers it, and high FiO₂ adds atelectasis.",
)

L['RSC-09'] = dict(
  sub="Respiratory → Post-operative lung → NIV for post-operative failure",
  step=3,
  intro="When prevention fails and the patient becomes hypoxaemic after surgery, the cause is usually atelectasis, which positive pressure reverses. That is why NIV works here better than in most hypoxaemic failure.",
  parts=[
    ('a', "**Suggested (conditional recommendation, moderate certainty).** The ERS/ATS NIV guideline (2017) suggests NIV for acute respiratory failure after surgery; by contrast it makes no recommendation for de novo hypoxaemic failure."),
    ('b', "**Mortality relative risk 0.28; intubation relative risk 0.27. It improves aeration and oxygenation and reduces atelectasis.** These are the guideline’s pooled estimates (mortality moderate certainty, intubation low certainty, wide confidence intervals). Positive pressure reopens the collapsed bases and lowers the work of breathing."),
    ('c', "**Gastric insufflation, regurgitation, anastomotic leak.** Mask pressure can push air into the stomach; after upper gastrointestinal surgery that distends a fresh anastomosis, so the pressures are kept modest and a gastric tube is considered."),
  ],
  mimic=[
    ("Post-operative failure vs de novo hypoxaemic failure", "After surgery (atelectasis) NIV is suggested; in de novo hypoxaemic failure (sepsis, pneumonia) high flow is preferred (RSC-01b)."),
  ],
  traps=[
    ("“NIV is contraindicated after abdominal surgery”", "It is suggested; the anastomosis is a reason for care with pressures, not a ban."),
  ],
  decode=[
    ("[pattern] Hypoxaemia on day 1 after abdominal surgery — role of NIV?", "Suggested: it reduces intubation and mortality."),
  ],
  punch="NIV is suggested for respiratory failure after surgery, cutting intubation and mortality by reopening atelectasis; watch for gastric distension and the anastomosis.",
)

L['RSC-10'] = dict(
  sub="Respiratory → Abdominal hypertension → Respiratory effects",
  step=4,
  intro="The abdomen is part of the chest wall, so a tense abdomen pushes the diaphragm up and stiffens the whole respiratory system. The key point for the next card is which compliance falls.",
  parts=[
    ('a', "**Sustained IAP ≥12 mmHg; compartment syndrome is >20 mmHg with new organ failure.** These are the WSACS 2013 definitions, with IAP measured through the bladder, supine, at end-expiration and zeroed at the mid-axillary line. Normal IAP in the critically ill is about 5–7 mmHg; IAH is graded I 12–15, II 16–20, III 21–25 and IV >25 mmHg."),
    ('b', "**20–80% (about half).** Reviews put the average near 50%, but the fraction varies with the patient and the chest wall, so pleural pressure cannot be calculated from IAP; it is measured with an oesophageal balloon when it matters (RSC-11d)."),
    ('c', "**Chest-wall (and so respiratory-system) compliance falls; lung compliance is unchanged.** With healthy lungs the lung tissue itself is not stiffer; the container around it is (if the lung is already injured, its compliance may fall as well). Plateau pressure rises because part of it is spent pushing the diaphragm and abdomen out."),
    ('d', "**FRC and lung volumes fall, compression atelectasis; pleural, peak, mean and plateau pressures rise; PVR rises; shunt, dead space and PaCO₂ rise; difficult weaning.** Collapsed bases cause shunt, and raised intrathoracic pressure lowers venous return and raises pulmonary vascular resistance."),
  ],
  mimic=[
    ("Stiff chest wall vs stiff lung", "Stiff chest wall (IAH, obesity): high plateau with high pleural pressure, transpulmonary pressure may be normal. Stiff lung (ARDS, fibrosis): high plateau with high transpulmonary pressure."),
  ],
  traps=[
    ("“Lung compliance falls in intra-abdominal hypertension” (RSC-16e)", "Chest-wall compliance falls; the lung is unchanged."),
    ("“IAH starts at 12 cmH₂O”", "The consensus unit is mmHg: IAP ≥12 mmHg."),
  ],
  decode=[
    ("[pattern] Intra-abdominal hypertension raises plateau pressure — which compliance has fallen?", "Chest-wall (and respiratory-system); lung compliance is unchanged."),
  ],
  punch="Intra-abdominal hypertension (≥12 mmHg; compartment syndrome >20 mmHg with new organ failure) stiffens the chest wall, not the lung, so plateau pressure rises while lung stress may not.",
)

L['RSC-11'] = dict(
  sub="Respiratory → Abdominal hypertension → Ventilating abdominal compartment syndrome",
  step=4,
  intro="Because the high plateau in RSC-10 comes partly from the chest wall, the usual targets would force needlessly small breaths. This card adjusts them, and the one real question tests the reason: lung injury follows transpulmonary pressure, not airway pressure.",
  parts=[
    ('a', "**6–8 mL/kg; driving pressure <15.** Lung protection still starts with a small breath on predicted body weight."),
    ('b', "**Usual plateau target + (IAP – 13) ÷ 2, IAP in cmH₂O.** Roughly half the abdominal pressure reaches the thorax (RSC-10b), so the plateau limit is raised by that share. Example: IAP 25 mmHg is 34 cmH₂O, so the limit becomes 30 + (34 – 13) ÷ 2, about 40 cmH₂O. In mmHg the same formula reads target – 7 + 0.7 × IAP. It is a physiological correction proposed in reviews, not a target tested in trials."),
    ('c', "**PEEP by best respiratory-system compliance; higher pressures are needed for recruitment.** The stiff chest wall absorbs part of each pressure, so more is needed to reach the alveoli; PEEP is titrated to the compliance it produces, not to a fixed number."),
    ('d', "**Oesophageal balloon: end-inspiratory <25 (over-distension); end-expiratory kept positive (your notes: 3; EPVent 0–10) to prevent collapse. Transpulmonary = alveolar – pleural (oesophageal) pressure.** EPVent set PEEP to keep end-expiratory transpulmonary pressure at 0–10 and limited end-inspiratory to below 25 cmH₂O. This measures what the lung actually feels: with a plateau of 38 and a pleural pressure of 20, the lung is stretched by only 18."),
  ],
  mimic=[
    ("Airway (plateau) pressure vs transpulmonary pressure", "Plateau is lung plus chest wall; transpulmonary pressure is the lung alone. When the chest wall is stiff, plateau overestimates lung stress."),
  ],
  traps=[
    ("“Plateau 38 cmH₂O with markedly raised pleural pressure means alveolar rupture, volutrauma or high transpulmonary pressure”", "With a high pleural pressure the transpulmonary pressure may be well below 20–25, so it can be a safe distending pressure. ‘Safe’ is an inference; an oesophageal balloon confirms it."),
  ],
  decode=[
    ("Morbidly obese, plateau 38 cmH₂O, pleural pressure markedly raised by abdominal and chest-wall compression — interpretation? [DocT GT]", "Safe distending pressure: injury follows transpulmonary pressure."),
  ],
  punch="With a stiff abdomen, plateau overstates lung stress: raise the plateau limit by (IAP – 13) ÷ 2 in cmH₂O, or measure transpulmonary pressure and keep it below 25 at end-inspiration and positive at end-expiration.",
)

L['RSC-12'] = dict(
  sub="Respiratory → Obesity → Respiratory changes and obesity hypoventilation",
  step=5,
  intro="Obesity is the everyday version of the stiff chest wall in RSC-10: the weight of the chest and abdomen lowers FRC, and some patients also stop driving their breathing enough. Five real questions test this card, mostly on obesity hypoventilation, which the card mentions in a single line.",
  parts=[
    ('a', "**FRC and ERV fall; airway closure, atelectasis, intrinsic PEEP, V/Q mismatch.** Abdominal contents push the diaphragm up, so FRC falls, mostly by losing expiratory reserve volume; TLC and residual volume change little. When FRC falls below closing capacity, small dependent airways close during quiet breathing: the alveoli behind them are perfused but not ventilated (V/Q mismatch, hypoxaemia), gas is trapped behind closed airways (intrinsic PEEP), and they collapse (atelectasis). All of this worsens supine and under anaesthesia, which is why sitting him up raises FRC (RSC-06)."),
    ('b', "**Chest-wall and total compliance fall; abdominal pressure rises.** The patient breathes on a stiffer system at a lower volume, so the work of breathing and oxygen consumption rise, and plateau pressures read higher on the ventilator without the lung itself being stretched more (RSC-11)."),
    ('c', "**Difficult airway, obstructive sleep apnoea; low drive in obesity hypoventilation syndrome.** Obesity hypoventilation is defined as BMI ≥30 with awake daytime hypercapnia (PaCO₂ ≥45 mmHg) after other causes of hypoventilation are excluded; hypoxaemia is not part of the definition. Its cause is not the load alone: a blunted central response to CO₂ (with leptin resistance) is central, sleep-disordered breathing adds nocturnal CO₂ loading, and the kidneys retain bicarbonate, which further blunts the drive. About 90% have OSA, but the OSA can be mild — so a BMI of 40 with a PaCO₂ of 50 and only mild OSA is explained by diminished drive."),
    ('d', "**Poor chest X-ray and ultrasound windows; difficult transport for CT. Always rule out pulmonary embolism.** Obesity is a major thrombotic risk and a hypoxaemic obese patient may be untestable by the usual routes, so embolism must be actively sought rather than assumed absent."),
  ],
  table=dict(title="Obstructive sleep apnoea vs obesity hypoventilation", head=["", "OSA alone", "Obesity hypoventilation"], rows=[["Awake PaCO₂", "normal", "**≥45 mmHg**"], ["Serum HCO₃⁻", "normal", "raised (≥27)"], ["Main problem", "upper airway collapse in sleep", "**low drive** + load + sleep breathing"], ["Long-term support", "CPAP", "CPAP if severe OSA; **NIV (bilevel)** if OSA mild or absent"]]),
  mimic=[
    ("OSA vs obesity hypoventilation", "OSA is obstruction during sleep with a normal daytime PaCO₂; obesity hypoventilation adds daytime hypercapnia from low drive."),
    ("Raised HCO₃⁻ in obesity: metabolic alkalosis vs compensation", "In an obese patient a raised bicarbonate is usually renal compensation for chronic hypercapnia — the ABG shows it."),
  ],
  traps=[
    ("“Hypoxaemia on room air is required for obesity hypoventilation”", "The definition is BMI ≥30 plus awake PaCO₂ ≥45 mmHg with other causes excluded; hypoxaemia is common but not required."),
    ("“Obese patient with HCO₃⁻ 35 and a chest infection: start antibiotics or a sleep study first”", "The raised bicarbonate signals chronic hypercapnia: an arterial blood gas comes first."),
    ("“Obesity hypoventilation is just severe sleep apnoea”", "Hypercapnia with only mild OSA points to diminished ventilatory drive."),
    ("“Supine obese patient desaturating: start PEEP first” (73% right)", "Sit him up first; it is the least invasive way to raise FRC."),
  ],
  decode=[
    ("Obese post-operative patient, supine, hypoxaemic — least invasive way to improve FRC? [DocT GT, 73% right]", "Head of bed up to 45°."),
    ("Obesity hypoventilation syndrome — most accurate statement? [Marrow]", "Awake daytime PaCO₂ >45 mmHg."),
    ("Obese patient, HCO₃⁻ 35, respiratory infection — next step? [Marrow]", "Arterial blood gas."),
    ("BMI 40, awake PaCO₂ 50, mild OSA — best explanation? [Marrow]", "Diminished ventilatory drive from obesity."),
  ],
  extra=[
    dict(q="Obese OSA patient, hypercapnic after surgery on morphine — CPAP improves which volume? [Marrow]", a="Functional residual capacity: CPAP lifts FRC above closing capacity; residual volume and TLC are unchanged. If tidal volume needs support, use bilevel NIV."),
    dict(q="When is a bicarbonate used to screen for obesity hypoventilation?", a="ATS 2019: in an obese patient with sleep-disordered breathing and low suspicion, a serum HCO₃⁻ <27 mmol/L makes it unlikely; a raised value or high suspicion needs an ABG."),
  ],
  punch="Obesity lowers FRC below closing capacity, causing airway closure, atelectasis and V/Q mismatch; obesity hypoventilation is BMI ≥30 with awake PaCO₂ ≥45 mmHg from low drive, flagged by a raised bicarbonate and confirmed by ABG.",
)

L['RSC-13'] = dict(
  sub="Respiratory → Obesity → Non-invasive support and the airway",
  step=5,
  intro="The low FRC and low drive of RSC-12 decide how the obese patient is supported before and around intubation. The two real questions test which non-invasive mode fits obesity hypoventilation and what prevents a disaster at intubation.",
  parts=[
    ('a', "**Hypercapnic failure, sleep apnoea or obesity hypoventilation. Settings: avoid high tidal volumes, adequate PEEP, high back-up rate. Start CPAP 2 weeks before elective surgery.** UK perioperative guidance (CPOC) aims for 4–6 weeks of CPAP before planned surgery, so 2 weeks is a minimum rather than the ideal. NIV (bilevel) adds inspiratory support, which a low-drive, hypercapnic patient needs; high flow and CPAP do not support the tidal volume. PEEP holds the airways open above closing capacity, and a high back-up rate covers the hypoventilating patient who stops breathing in sleep. So BMI 50 with mild OSA (AHI 7), nocturnal desaturation and a raised bicarbonate points to NIV: the problem is hypoventilation, not obstruction."),
    ('b', "**Respiratory complications relative risk 0.33; unplanned ICU admission 0.43. First-line for post-operative failure in obesity.** These come from a 2016 meta-analysis (11 studies, 768 patients with BMI ≥35, NIV around induction and after surgery): the fall in respiratory complications was significant (95% CI 0.16–0.66), but the 0.43 for unplanned ICU admission was not (95% CI 0.16–1.15), nor was the fall in re-intubation. After surgery the obese patient’s FRC falls further; positive pressure reverses the atelectasis (RSC-09)."),
    ('c', "**Semi-sitting; pre-oxygenate with CPAP/NIV plus apnoeic oxygenation; rapid sequence induction; videolaryngoscope recommended.** A small FRC is a small oxygen store, and oxygen consumption is high, so the obese patient desaturates within a minute or two of apnoea. Head-up positioning and positive pressure enlarge the store, and apnoeic oxygenation extends the safe time. Mask ventilation and laryngoscopy are harder, so the airway is assessed in advance (neck circumference, Mallampati, mouth opening, the 3-3-2 rule) and senior help is present before induction."),
  ],
  mimic=[
    ("NIV vs CPAP in obesity hypoventilation", "CPAP holds the airway open (severe OSA); bilevel NIV also supports ventilation, needed when OSA is mild and drive is low."),
  ],
  traps=[
    ("“The obese asthmatic’s arrest after failed RSI was due to the induction drug or the tube size”", "It was preventable by assessing the high-risk airway beforehand and planning (videolaryngoscope, senior help, pre-oxygenation)."),
    ("“Mild OSA (AHI 7) means no positive pressure is needed”", "Nocturnal desaturation with a raised bicarbonate is hypoventilation; NIV is the next step."),
  ],
  decode=[
    ("Obese asthmatic arrests after failed RSI — what would have prevented it? [Marrow]", "Assessing the high-risk airway beforehand."),
    ("BMI 50, AHI 7, nocturnal desaturation, HCO₃⁻ 30 — next step? [Marrow]", "Non-invasive positive airway pressure (NIV)."),
  ],
  punch="In obesity choose NIV for hypercapnia and hypoventilation, use it after surgery, and intubate semi-sitting after CPAP/NIV pre-oxygenation with apnoeic oxygen, a videolaryngoscope and a planned difficult airway.",
)

L['RSC-14'] = dict(
  sub="Respiratory → Obesity → Invasive ventilation settings",
  step=6,
  intro="Once the obese patient is intubated, the settings follow from two facts already met: lung size follows height, and the chest wall is stiff (RSC-12). The one real question is the same transpulmonary pressure point as RSC-11.",
  parts=[
    ('a', "**Tidal volume 6–8 mL/kg predicted body weight.** A patient 160 cm tall has the lungs of a 160 cm person whatever he weighs; 8 mL/kg of an actual 140 kg would be about 1100 mL, against about 450 mL on his predicted weight (about 57 kg for a man)."),
    ('b', "**PEEP 5–10 cmH₂O (keep alveolar pressure above closing pressure).** The weight of the chest and abdomen raises pleural pressure, so without PEEP dependent airways close at the end of every breath."),
    ('c', "**Recruitment may need CPAP up to 50; risk of hypotension, barotrauma.** The stiff chest wall takes part of the pressure, so higher pressures are needed to reach the alveoli. In PROBESE (2013 patients with BMI ≥35, 7 mL/kg PBW), PEEP 12 with recruitment vs PEEP 4 did not reduce pulmonary complications (21.3% vs 23.6%) and caused more hypotension (31.6% vs 17.2%) and bradycardia, although less intra-operative hypoxaemia."),
    ('d', "**Plateau target + (IAP – 13) ÷ 2 (IAP in cmH₂O); driving pressure <15–17 cmH₂O.** As in RSC-11, part of the plateau is spent on the chest wall, so the plateau limit is adjusted and driving pressure, or transpulmonary pressure, judges lung stress."),
  ],
  mimic=[
    ("Predicted vs actual body weight", "Predicted (from height and sex) sets the tidal volume; actual weight is used for many drug doses but never for the breath."),
  ],
  traps=[
    ("“Tidal volume in obesity is set on actual body weight” (RSC-16f)", "Predicted body weight; actual weight over-distends."),
    ("“A plateau of 38 in a morbidly obese patient means volutrauma”", "With a high pleural pressure the transpulmonary pressure may be safe (RSC-11)."),
  ],
  decode=[
    ("Morbidly obese, plateau 38 cmH₂O, markedly raised pleural pressure — interpretation? [DocT GT]", "Safe distending pressure."),
  ],
  punch="Ventilate the obese on predicted body weight (6–8 mL/kg), PEEP 5–10 to stay above closing pressure, and judge stress by driving or transpulmonary pressure, not the raw plateau.",
)

L['RSC-15'] = dict(
  sub="Respiratory → Obesity → Prone positioning and extubation",
  step=6,
  intro="The last clinical card follows the obese patient to the two hardest moments: turning prone and coming off the ventilator. Both are shaped by the abdomen and the low FRC.",
  parts=[
    ('a', "**Yes: feasible and safe with a trained team; improves P/F; may reduce mortality.** Obese patients have more dorsal collapse, so turning them reopens a large area; a French case–control study (De Jong 2013) found oxygenation improved at least as much as in non-obese patients without more complications, though mortality benefit is not proven in this group."),
    ('b', "**Careful abdominal positioning; reverse Trendelenburg.** The abdomen must hang free or be supported so that it does not push on the diaphragm and raise IAP; tilting head-up lets the abdomen fall away and reduces facial and airway oedema."),
    ('c', "**T-piece, or pressure support 0 with PEEP 0.** With pressure support and PEEP the ventilator does work that the patient will have to do after the tube comes out; a trial without them shows the real post-extubation work of breathing in the obese."),
    ('d', "**Stop sedation; extubate to NIV/CPAP (prevents atelectasis and re-intubation); pre-operative settings may be used.** As FRC falls again after extubation, positive pressure holds it up; a patient on home CPAP or NIV goes straight back on it."),
  ],
  mimic=[
    ("Weaning trial in obese vs non-obese", "In the obese, support during the trial hides the load; a T-piece or zero support and zero PEEP is closest to life after extubation."),
  ],
  traps=[
    ("“Obesity is a contraindication to proning”", "It is feasible and safe with a trained team and careful abdominal positioning."),
  ],
  decode=[
    ("[pattern] Which weaning trial best predicts post-extubation work of breathing in the obese?", "T-piece, or pressure support 0 with PEEP 0."),
  ],
  punch="Prone the obese when needed with the abdomen free and the bed tilted head-up; wean with a T-piece or zero support and extubate to NIV or CPAP.",
)

L['RSC-16'] = dict(
  sub="Respiratory → Special situations → Revision: true or false",
  step=6,
  intro="A sweep through the deck. Each statement turns on one detail from an earlier card.",
  parts=[
    ('a', "**False — high flow over NIV** in septic hypoxaemia (RSC-01b)."),
    ('b', "**False — no difference** in ventilator-free days with 4–6 vs 8–10 mL/kg PBW (RSC-02)."),
    ('c', "**True — 4 or more of 8 items, in one 24-hour period** (RSC-05)."),
    ('d', "**False — no difference in complications; more hypotension** with high PEEP (RSC-07)."),
    ('e', "**False — chest-wall compliance falls**; lung compliance is unchanged (RSC-10c)."),
    ('f', "**False — predicted body weight**; actual weight over-distends (RSC-14a)."),
    ('g', "**True — atelectasis is the commonest post-operative pulmonary complication** (RSC-04)."),
  ],
  mimic=[],
  traps=[
    ("“Low tidal volume and high PEEP are proven for every ventilated lung”", "Low tidal volume is proven in ARDS; PReVENT (no ARDS) and PROVHILO and PROBESE (high PEEP in theatre) found no benefit."),
  ],
  decode=[
    ("[pattern] True/false on special-situation ventilation", "High flow in sepsis, PReVENT no difference, four MGS items, PROVHILO no difference, chest wall not lung, predicted weight, atelectasis."),
  ],
  punch="Most errors here come from overextending ARDS rules: low tidal volume is proven in ARDS, high PEEP is not proven in theatre, and in IAH and obesity the chest wall, not the lung, is stiff.",
)

FLAGS = {}
FLAGS['RSC-05'] = "Card c gives the white-count item as >11 × 10⁹/L; published Melbourne Group Score versions use >11.2 × 10⁹/L, and MGS-2 replaces abnormal breath sounds with ICU/HDU readmission or stay >36 h for a respiratory problem. Not wrong enough to change; explanation gives both."
FLAGS['RSC-12'] = "Card c mentions obesity hypoventilation only as ‘low drive’; three Marrow questions test its definition (BMI ≥30 + awake PaCO₂ ≥45 mmHg, other causes excluded, hypoxaemia not required) and the raised-HCO₃⁻ → ABG screen. Consider adding; explanation and extra give them."
FLAGS['RSC-13'] = "Marrow’s failed-RSI question keys pre-assessment of the high-risk airway (3-3-2 rule, senior help); card c covers technique but not assessment. Consider adding; explanation gives it. Also: card b’s unplanned-ICU RR 0.43 was not statistically significant in its meta-analysis (95% CI 0.16–1.15; only respiratory complications RR 0.33 was); and card a’s ‘CPAP 2 weeks before surgery’ is shorter than CPOC’s 4–6 weeks. Consider adding ‘NS’ and ‘ideally 4–6 weeks’."
FLAGS['RSC-10'] = "Card c says lung compliance is unchanged in IAH; true for healthy lungs, but in injured lungs IAH can lower lung compliance too (Regli/Malbrain review, Ann Intensive Care 2019). Teaching simplification; explanation notes it."
FLAGS['RSC-02'] = "Not an error: Surviving Sepsis 2026 now adds a conditional suggestion of 6–8 mL/kg IBW over 4 to <6 mL/kg in sepsis without ARDS, which matches PReVENT. Consider adding to the card; explanation gives it."
