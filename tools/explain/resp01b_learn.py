# RESP01B — Explain v3 ("Learn" depth): ARDS II — Non-invasive Support, VILI, Landmark Trials, Setting the Ventilator, Pressures & Power. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP01B.md. Fields as TOX01, plus SPINE, PRIMER and step.

SPINE = [
  ("Supporting the patient before intubation", "High-flow nasal oxygen is the first-line non-invasive support in hypoxaemic failure, NIV is kept for mild cases, and ROX and HACOR tell you early when each is failing."),
  ("How breathing and ventilators injure", "The lung is injured by the stretch it actually feels — from the patient’s own vigorous effort (P-SILI) or from the ventilator (volutrauma, atelectrauma, biotrauma) — so stress and strain, not airway pressure alone, are what matter."),
  ("Trials behind lung-protective ventilation", "ARMA showed that 6 mL/kg predicted body weight saves lives; higher PEEP did not change mortality in three trials, but may help when P/F is ≤200."),
  ("Setting the ARDSNet ventilator", "Calculate predicted body weight from height and sex, step tidal volume down to 6 mL/kg, keep plateau ≤30, accept hypercapnia within the pH rules, and pair FiO₂ with PEEP from the table to a modest oxygen target."),
  ("Reading the pressures on screen", "A hold at end-inspiration separates peak (resistance plus elastance) from plateau (alveolar pressure), and an oesophageal balloon separates the lung from the chest wall."),
  ("Driving pressure, power and review", "Driving pressure scales the breath to the open lung and is the variable most strongly associated with survival; mechanical power adds rate and flow to measure the total energy the lung receives."),
]

PRIMER = "Respiratory-system compliance is tidal volume divided by the pressure needed to hold it (plateau minus PEEP); in ARDS it is low because the aerated ‘baby lung’ is small, not because that lung is stiff (ARDS-10). Plateau pressure is the airway pressure during a short pause at the end of inspiration with no flow, so it equals alveolar pressure; peak pressure also includes the pressure spent pushing flow through the tube and airways. What actually stretches the lung is transpulmonary pressure — alveolar minus pleural pressure — so a strongly breathing patient can over-stretch his lung even when the airway pressure looks low. HFNC delivers heated, humidified gas at up to 60 L/min through nasal prongs; NIV delivers set pressures (inspiratory support plus PEEP, or CPAP) through a sealed mask."

L = {}

L['ARDS-14'] = dict(
  sub="Respiratory → ARDS → Non-invasive support (FLORALI, HFNC)",
  step=1,
  intro="The story starts before the tube. A patient with acute hypoxaemic failure, often early ARDS, can be given standard oxygen, high-flow nasal oxygen or NIV, and FLORALI is the trial that compared all three. The exam asks it two ways: what the trial showed, and what HFNC actually does to the patient’s breathing.",
  parts=[
    ('a', "**HFNC vs standard oxygen (face mask) vs NIV, in acute hypoxaemic respiratory failure.** Frat and colleagues (NEJM 2015) randomised 310 non-hypercapnic patients with P/F ≤300, most with pneumonia; the NIV arm received HFNC between NIV sessions."),
    ('b', "**Intubation at 28 days: no significant difference overall.** The rates were 38% with HFNC, 47% with standard oxygen and 50% with NIV — a trend, not a significant result, so ‘HFNC reduces intubation’ is not what the primary outcome showed."),
    ('c', "**Lower 90-day mortality with HFNC; fewer intubations in the subgroup with P/F ≤200.** Neither is the primary outcome: 90-day mortality was a secondary outcome, and the P/F ≤200 intubation result came from a post hoc analysis, so both generate hypotheses rather than prove benefit. The hazard of death at 90 days was about twice as high with standard oxygen (HR 2.01) and two and a half times as high with NIV (HR 2.50), compared with HFNC. NIV did worst; its patients took large tidal volumes, which links this card to P-SILI (ARDS-17). Current ERS (2022) and ESICM (2023) guidance favour HFNC over conventional oxygen in acute hypoxaemic respiratory failure."),
    ('d', "**FiO₂ 21–100%; washes out anatomical dead space; lowers work of breathing; gives a few cmH₂O of PEEP.** A flow of up to 60 L/min matches or exceeds the patient’s own peak inspiratory flow, so room air is not entrained and the set FiO₂ is the FiO₂ delivered — something no face mask achieves. The flow flushes CO₂ from the nasopharynx, so each breath carries less dead space; the respiratory rate and work of breathing fall, while tidal volume stays the same or rises. Heated, humidified gas is comfortable and keeps secretions moving. The PEEP is small — about 1 cmH₂O per 10 L/min with the mouth closed, less with it open — and it is neither set nor measured. Even so, among the common oxygen devices it is the only one that generates any end-expiratory pressure."),
  ],
  table=dict(title="Which device does what", head=["Device", "Reliable FiO₂", "PEEP", "Dead-space washout"], rows=[["Hudson / simple face mask", "no", "no", "no"], ["Venturi mask", "yes, up to about 0.6", "no", "no"], ["Non-rebreather", "no (high but variable)", "no", "no"], ["**HFNC**", "**yes, up to 1.0**", "**small, flow-dependent**", "**yes**"], ["NIV / CPAP mask", "yes", "set (≥5)", "no"]]),
  mimic=[
    ("HFNC vs CPAP/NIV", "CPAP and NIV set and hold a known pressure through a sealed mask; HFNC gives only a small, variable pressure through open prongs, but is far better tolerated."),
    ("‘High-frequency nasal insufflation’ vs HFNC", "There is no distinct standard therapy by that name; the keyed answer simply describes HFNC — high flow, CO₂ washout, mild positive pressure."),
  ],
  traps=[
    ("“HFNC reduces tidal volume”", "It lowers the respiratory rate and work of breathing, but tidal volume is unchanged or larger; this is the false option in ‘all except’ questions."),
    ("“HFNC delivers higher pressures than CPAP” or “is CPAP”", "Its PEEP is a few cmH₂O at most and falls with an open mouth. The DocT key ‘positive pressure to maintain airway patency’ (only 60% got it right) overstates this; it is still the best of its options, but the leading mechanisms are a reliable FiO₂ and dead-space washout."),
    ("“The elderly patient pulling off her mask needs a non-rebreather, mask CPAP or intubation” (only 43% got this right)", "She is hypoxaemic but with a normal pH and PaCO₂, and she will not tolerate a mask: HFNC is tolerated through the nose and gives a reliable FiO₂. A non-rebreather is still a mask with an unreliable FiO₂; mask CPAP needs a cooperative patient."),
    ("“In FLORALI, HFNC lowered intubation”", "Overall it did not (primary outcome negative); only the P/F ≤200 subgroup, in a post hoc analysis, showed fewer intubations."),
  ],
  decode=[
    ("Which oxygen device can generate PEEP? [NEET 2025]", "HFNO — not a non-rebreather, Venturi or Hudson mask."),
    ("Benefits of HFNC include all EXCEPT [DocT GT]", "Reduce tidal volume."),
    ("Primary benefit of HFNO in ARDS [DocT QBank, three versions]", "High flow with mild positive pressure, better oxygenation and less work of breathing — the option that does not claim CPAP-level pressure or a fixed tidal volume. Some stems put HFNO on an already ventilated patient; ignore that and answer the mechanism."),
    ("Elderly, confused, rib fractures, SpO₂ 89% on 8 L face mask, pulling it off — next step? [DocT GT]", "Heated, humidified HFNC."),
  ],
  punch="FLORALI’s primary outcome was negative, but HFNC was associated with lower 90-day mortality and fewer intubations when P/F was ≤200; it works mainly through a reliable FiO₂, dead-space washout and comfort, with only a little PEEP.",
)

L['ARDS-15'] = dict(
  sub="Respiratory → ARDS → ROX index",
  step=1,
  intro="Once a patient is on HFNC, the danger is staying on it too long while failing. The ROX index puts oxygenation and breathing effort into one bedside number, so failure is seen in hours rather than at the point of collapse.",
  parts=[
    ('a', "**(SpO₂ ÷ FiO₂) ÷ respiratory rate.** SpO₂ in %, FiO₂ as a fraction. Better oxygenation raises the top line, faster breathing lowers the whole, so the rate must be the divisor — SpO₂ 92% on FiO₂ 0.5 at 30/min gives 184 ÷ 30 = 6.1. It uses SpO₂, not PaO₂, because it is meant to need no blood gas."),
    ('b', "**≥4.88 at 2, 6 or 12 h: low risk of intubation.** Roca and colleagues derived it in pneumonia patients on HFNC and validated it in 2019."),
    ('c', "**Failure if below 2.85 at 2 h, 3.47 at 6 h, 3.85 at 12 h.** The failure cut-off rises with time, because a patient still struggling after 12 hours has less excuse. Values between the failure cut-off and 4.88 are indeterminate, so the score is repeated."),
  ],
  mimic=[
    ("ROX vs HACOR", "ROX is for HFNC and a lower value is worse; HACOR is for NIV and a higher value is worse (ARDS-16)."),
  ],
  traps=[
    ("“ROX = PaO₂/FiO₂ × RR” or “SpO₂ × RR / FiO₂” (69–83% got the formula right)", "ROX uses SpO₂, not PaO₂, and the respiratory rate divides: a faster rate must lower the score."),
    ("“A higher ROX predicts failure”", "A lower ROX is worse."),
  ],
  decode=[
    ("Pneumonia on HFNC — correct formula for the ROX index? [DocT GT, three tests]", "SpO₂/FiO₂ ÷ RR."),
    ("[pattern] ROX 3.2 at 6 h on HFNC — what next?", "Below 3.47: high risk of failure, so prepare to intubate rather than wait."),
  ],
  punch="ROX is SpO₂/FiO₂ divided by the respiratory rate; ≥4.88 predicts HFNC success, and values below 2.85, 3.47 and 3.85 at 2, 6 and 12 h predict failure.",
)

L['ARDS-16'] = dict(
  sub="Respiratory → ARDS → HACOR score",
  step=1,
  intro="HACOR does for NIV what ROX does for HFNC. NIV failure in hypoxaemic patients is common, and the harm lies in the delay, so the score is taken after the first hour.",
  parts=[
    ('a', "**NIV failure in hypoxaemic respiratory failure.** Duan and colleagues (2017) built it from bedside variables to predict who will need intubation."),
    ('b', "**Heart rate, acidosis (pH), consciousness (GCS), oxygenation (P/F), respiratory rate; consciousness carries the most points.** A falling GCS weighs most because a drowsy patient cannot protect his airway or cooperate with a mask: of a maximum 25 points, GCS ≤10 scores 10 on its own, more than the worst P/F (6), pH (4) or rate (4)."),
    ('c', "**>5 at 1 hour of NIV: failure rate above 80%; intubate early.** In the derivation study, among patients with a score above 5 at 1 h who failed NIV, those intubated within 12 hours had lower hospital mortality than those intubated later (66% vs 79%) — an association, but it is the reason the score is used."),
  ],
  mimic=[
    ("HACOR vs ROX", "HACOR: NIV, needs a blood gas, higher is worse. ROX: HFNC, no blood gas, lower is worse."),
  ],
  traps=[
    ("“NIV suits moderate ARDS with distress, severe ARDS or shock”", "NIV is reasonable only in mild ARDS without contraindications (ARDS-04c). The keyed option calls P/F 200 ‘mild’; by Berlin it is moderate — the option is still the best of the four."),
  ],
  decode=[
    ("Most appropriate scenario for NIPPV in ARDS [DocT QBank]", "Mild ARDS with no contraindications to NIPPV (83% got this right)."),
    ("[pattern] HACOR 7 after 1 h of NIV — next step?", "Intubate early: >5 at 1 h predicts failure."),
  ],
  punch="HACOR (heart rate, acidosis, consciousness, oxygenation, rate) above 5 after 1 hour of NIV predicts failure in over 80%, so intubate early; for NIV a higher score is worse.",
)

L['ARDS-17'] = dict(
  sub="Respiratory → ARDS → Patient self-inflicted lung injury",
  step=2,
  intro="Why does NIV do badly in hypoxaemic failure, and why does delay matter? Because the patient’s own breathing can injure the lung. A high respiratory drive generates large swings in pleural pressure, and the lung feels transpulmonary pressure, not the modest airway pressure on the screen.",
  parts=[
    ('a', "**Lung injury caused by the patient’s own vigorous spontaneous effort, on NIV, HFNC or assisted modes.** Hypoxaemia, acidosis and inflammation drive breathing hard; in an injured, small lung, those big breaths over-stretch it in the same way that a large ventilator breath would (ARDS-18)."),
    ('b', "**Large negative pleural swings → high transpulmonary pressure and tidal volume; pendelluft (gas moving from non-dependent to dependent lung); raised transmural vascular pressure → oedema; patient–ventilator dyssynchrony.** On NIV, the ventilator’s pressure support and the patient’s muscle pressure add together, so large tidal volumes are easy to reach: in Carteaux’s cohort, patients who failed NIV averaged about 10.6 mL/kg PBW, against 8.5 in those who succeeded. In an injured lung, a forceful diaphragm contraction sucks gas from non-dependent into dependent alveoli before air enters from the mouth (pendelluft), stretching the dependent lung in a way the airway pressure does not show. Very negative pleural pressure also lowers the pressure around the capillaries, raising the transmural pressure across them and adding oedema. Dyssynchrony, such as double triggering, stacks breaths."),
    ('c', "**Do not delay intubation in a patient with high drive; then sedation, higher PEEP, or neuromuscular blockade.** On NIV for hypoxaemic failure, an expired tidal volume persistently above about 9.5 mL/kg PBW (Carteaux 2016) predicts NIV failure, mainly when P/F is ≤200, even in a patient who looks comfortable — and NIV failure with late intubation carries a high mortality. After intubation, sedation lowers the drive, higher PEEP makes the injured lung behave more uniformly and reduces pendelluft, and paralysis abolishes the effort entirely in severe cases."),
  ],
  mimic=[
    ("P-SILI vs VILI", "Same physics, different source of pressure: the patient’s muscles in P-SILI, the ventilator in VILI."),
  ],
  traps=[
    ("“She is comfortable, so tidal volumes of >9.5 mL/kg on NIV do not matter”", "Read the volume, not the face: it marks high drive and P-SILI risk, and predicts NIV failure (81–94% got this right)."),
    ("“High tidal volume on NPPV causes auto-PEEP or prevents recruitment”", "The concern is P-SILI. The keyed wording ‘a marker of low lung compliance’ is loose: a large tidal volume marks high drive, which is dangerous because the lung receiving it is small."),
    ("“Airway pressure on NIV is low, so the lung is safe”", "Transpulmonary pressure can be dangerously high while airway pressure looks safe."),
  ],
  decode=[
    ("Hypoxaemic failure on NIV, comfortable, tidal volumes consistently >9.5 mL/kg — main concern? [DocT GT, two tests]", "Patient self-inflicted lung injury."),
    ("NPPV in de novo hypoxaemic failure — concern about high tidal volumes? [DocT GT]", "P-SILI."),
    ("Causes of NIV failure in ARDS [NEET 2024]", "P-SILI, delayed intubation, mask intolerance, secretions, shock."),
  ],
  punch="A patient with high drive can injure his own lung through large pleural swings and pendelluft, unseen on the airway pressure; a tidal volume above about 9.5 mL/kg on NIV is the warning, and early intubation is the remedy.",
)

L['ARDS-18'] = dict(
  sub="Respiratory → ARDS → Ventilator-induced lung injury",
  step=2,
  intro="The ventilator can do to the lung what the patient’s effort does in P-SILI. Each type of VILI names a different way the breath harms the lung, and each is matched by a setting that prevents it — which is how the questions are framed.",
  parts=[
    ('a', "**Volutrauma: over-distension from high tidal volume (high strain).** Animal work (Dreyfuss) showed that it is the volume, not the airway pressure itself, that injures: high pressure with the chest strapped, limiting volume, caused little oedema, whereas high volume at low pressure caused severe injury. Low tidal volume prevents it."),
    ('b', "**Barotrauma: high transpulmonary pressure → air leak (pneumothorax, pneumomediastinum).** Over-stretched alveoli rupture, and air tracks along the bronchovascular sheaths into the mediastinum and under the skin, where on a chest X-ray it can outline the fibres of pectoralis major (the ‘ginkgo leaf’ sign)."),
    ('c', "**Atelectrauma: cyclic opening and closing of unstable units; shear (low PEEP).** Units that collapse at end-expiration and are forced open with each breath tear at the junction between open and closed lung. Enough PEEP keeps them open, which is why PEEP is started early, not just to raise the PaO₂."),
    ('d', "**Biotrauma: mediator release from injured lung → distant organ failure.** Injurious ventilation releases cytokines into the blood; lower tidal volumes reduce them, which is one explanation of why ARMA lowered organ failure as well as mortality (ARDS-19)."),
    ('e', "**Ergotrauma: injury from total energy delivered (mechanical power) (standard teaching, not in your notes).** It brings rate and flow into the picture, not only volume and pressure (ARDS-27)."),
    ('f', "**Strain = tidal volume ÷ end-expiratory lung volume; stress = transpulmonary pressure.** Strain is how much the open lung is stretched relative to its resting size; stress is the pressure across it. They are linked by the specific elastance of the lung (stress = specific elastance × strain), so the same tidal volume is more harmful in a smaller baby lung."),
  ],
  table=dict(title="Each injury and the setting that prevents it", head=["Injury", "Cause", "Prevented by"], rows=[["Volutrauma", "large tidal volume", "**6 mL/kg PBW**"], ["Barotrauma", "high transpulmonary pressure", "plateau ≤30"], ["Atelectrauma", "cyclic collapse", "**PEEP**"], ["Biotrauma", "mediator release", "all of the above"], ["Ergotrauma", "total energy", "limit power, including rate"]]),
  mimic=[
    ("Volutrauma vs barotrauma", "Volutrauma is diffuse oedema from over-stretch; barotrauma is air outside the alveoli."),
  ],
  traps=[
    ("“High PEEP is mainly to improve cardiac output or prevent hypercapnia”", "PEEP raises intrathoracic pressure and can lower cardiac output; its purposes are recruitment, a larger end-expiratory lung volume (FRC) and prevention of atelectrauma (98% got this right)."),
    ("“Barotrauma is caused by high airway pressure per se”", "The injury follows high transpulmonary pressure and volume; airway pressure is only a proxy."),
  ],
  decode=[
    ("FiO₂ 0.7, plateau 32 — strongest reason to start PEEP early? [DocT GT]", "Prevent ventilator-induced lung injury (atelectrauma)."),
    ("Primary rationale for high PEEP in ARDS [DocT QBank]", "Recruits collapsed alveoli and increases FRC."),
    ("Post-ROSC, difficult bag-mask ventilation — expected chest X-ray finding? [Marrow]", "Ginkgo leaf sign: subcutaneous emphysema outlining pectoralis major, from air leak."),
  ],
  punch="Volume over-stretches, cyclic collapse shears, the injured lung releases mediators and the total energy adds up; low tidal volume and enough PEEP are the two settings that prevent most of it.",
)

L['ARDS-19'] = dict(
  sub="Respiratory → ARDS → ARMA trial",
  step=3,
  intro="ARMA is the trial that turned the baby-lung idea (ARDS-10) into practice. It is the only ventilator setting in ARDS with a large mortality benefit in a randomised trial, so it is the answer to most ‘which strategy improves survival’ questions.",
  parts=[
    ('a', "**Tidal volume 6 vs 12 mL/kg predicted body weight (861 patients).** The ARDS Network trial (NEJM 2000) compared a low tidal volume with what was then standard practice."),
    ('b', "**Plateau ≤30 vs ≤50 cmH₂O.** The tidal volume in the low arm was reduced further, down to 4 mL/kg, if the plateau stayed above 30 (ARDS-22)."),
    ('c', "**31.0% vs 39.8% mortality (about 9% absolute reduction); stopped early for benefit.** About one death prevented for every 11 patients treated."),
    ('d', "**More ventilator-free and organ-failure-free days.** Oxygenation was initially worse in the low-volume arm, yet survival was better: the benefit came from less lung injury, not from better gas exchange — so a better PaO₂ is not the goal of ventilation."),
  ],
  mimic=[
    ("Therapies that improve oxygenation vs therapies that improve survival", "Inhaled vasodilators and recruitment manoeuvres raise PaO₂ without proven survival benefit; low tidal volume (and proning in severe ARDS) improves survival."),
  ],
  traps=[
    ("“Plateau pressure <35 cmH₂O” as the goal", "The ARDSNet limit is ≤30."),
    ("“Intubated with P/F 86 on FiO₂ 1.0 — start VV-ECMO” (only 66% chose low tidal volume)", "First ventilate protectively: 4–6 mL/kg with PEEP >5, then prone. ECMO comes after optimised ventilation fails (EOLIA criteria: P/F <50 for >3 h, <80 for >6 h, or pH <7.25 with PaCO₂ ≥60 for >6 h)."),
    ("“Use actual body weight”", "Predicted body weight, from height and sex (ARDS-21). Stems that say ‘ideal body weight’ mean the same thing."),
  ],
  decode=[
    ("Primary goal of lung-protective ventilation in ARDS [DocT QBank]", "Tidal volume 6–8 mL/kg predicted body weight (79% got this right)."),
    ("Strategy most likely to reduce ventilator-associated lung injury [DocT QBank]", "Low tidal volume (6 mL/kg ideal body weight) with appropriate PEEP."),
    ("Influenza, intubated, P/F 86 on FiO₂ 1.0 — next best step? [DocT GT]", "Tidal volume 4–6 mL/kg with PEEP >5, not ECMO or CT."),
  ],
  punch="ARMA: 6 mL/kg predicted body weight with plateau ≤30 cut mortality from 39.8% to 31.0% despite worse early oxygenation — protecting the lung, not the PaO₂, is what saves lives.",
)

L['ARDS-20'] = dict(
  sub="Respiratory → ARDS → Higher vs lower PEEP",
  step=3,
  intro="After tidal volume, the next question was how much PEEP. Three trials compared higher and lower PEEP on top of low tidal volume, and the answer lies in who was studied.",
  parts=[
    ('a', "**ALVEOLI, LOVS, ExPress.** ALVEOLI (ARDSNet, 2004) used a higher PEEP/FiO₂ table; LOVS (2008) added recruitment manoeuvres and pressure control; ExPress (2008) raised PEEP as far as a plateau of 28–30 cmH₂O allowed."),
    ('b', "**No mortality difference; better oxygenation and less rescue therapy with higher PEEP.** Higher PEEP recruits lung and lowers FiO₂ needs, but in patients with little recruitable lung it only over-distends what is already open, so the net effect on survival was neutral."),
    ('c', "**Moderate to severe ARDS (P/F ≤200) benefits from higher PEEP; mild ARDS may be harmed.** The individual-patient meta-analysis of the three trials (Briel, JAMA 2010) found lower mortality with higher PEEP when P/F was ≤200, and a non-significant trend to harm above 200. ATS guidance (2024 update) suggests higher PEEP, without prolonged recruitment manoeuvres, in moderate–severe ARDS; a later trial of recruitment plus PEEP titration (ART, 2017) increased mortality."),
  ],
  mimic=[
    ("Higher PEEP vs recruitment manoeuvres", "Higher PEEP is suggested in moderate–severe ARDS; prolonged high-pressure recruitment manoeuvres are not."),
  ],
  traps=[
    ("“Higher PEEP reduced mortality in ALVEOLI”", "No trial showed it alone; the benefit appears only in pooled data for P/F ≤200 (ARDS-29e)."),
  ],
  decode=[
    ("Septic shock, bilateral infiltrates, P/F 100 — ideal ventilator settings? [Marrow]", "Low tidal volume with high PEEP."),
    ("[pattern] Which ARDS patients benefit from higher PEEP?", "Moderate to severe (P/F ≤200)."),
  ],
  punch="ALVEOLI, LOVS and ExPress each found no mortality difference with higher PEEP, but pooled data favour it when P/F is ≤200.",
)

L['ARDS-21'] = dict(
  sub="Respiratory → ARDS → Predicted body weight",
  step=4,
  intro="Every tidal volume in the ARDSNet protocol is per kilogram of predicted body weight, so this calculation comes before the first setting.",
  parts=[
    ('a', "**Men: 50 + 0.91 × (height in cm – 152.4).** A 170 cm man: 50 + 0.91 × 17.6 = 66 kg, so 6 mL/kg is about 400 mL."),
    ('b', "**Women: 45.5 + 0.91 × (height in cm – 152.4).** At the same height a woman’s PBW is 4.5 kg less: a 160 cm woman is about 52 kg, so 6 mL/kg is about 315 mL."),
    ('c', "**Lung size follows height and sex, not actual weight.** Fat does not add alveoli, so dosing by actual weight gives an obese patient a dangerously large breath."),
  ],
  mimic=[
    ("Predicted vs ideal body weight", "Questions use the terms interchangeably; both mean the height-and-sex formula."),
  ],
  traps=[
    ("“Tidal volume by actual body weight”", "Never: by predicted body weight (ARDS-29a)."),
  ],
  decode=[
    ("[pattern] 170 cm man weighing 110 kg — tidal volume at 6 mL/kg?", "About 400 mL, from PBW 66 kg, not 660 mL."),
  ],
  punch="Predicted body weight is 50 (men) or 45.5 (women) + 0.91 × (height in cm – 152.4), because lung size follows height and sex, not weight.",
)

L['ARDS-22'] = dict(
  sub="Respiratory → ARDS → ARDSNet protocol",
  step=4,
  intro="This is ARMA turned into steps at the bedside. The questions test three things: the tidal volume and plateau rules, what to do when the CO₂ rises, and when hypercapnia is itself dangerous.",
  parts=[
    ('a', "**Start 8 mL/kg PBW; reduce by 1 mL/kg every ≤2 h to 6 mL/kg.** The mode is volume assist-control. Stepping down lets the CO₂ and pH adjust gradually instead of in one jump."),
    ('b', "**Rate up to 35/min.** The initial rate is set to match the patient’s previous minute ventilation; raising the rate is the first lever for the CO₂ that rises when tidal volume falls."),
    ('c', "**Plateau ≤30 cmH₂O; if higher, reduce tidal volume in 1 mL/kg steps to a minimum of 4 mL/kg.** Plateau is checked with a 0.5 s inspiratory pause. Six mL/kg is a starting point: if the plateau is still high, the baby lung is smaller than average and the breath must shrink further."),
    ('d', "**pH 7.30–7.45. If pH falls, raise rate to 35; if pH <7.15 at rate 35, tidal volume may be raised and bicarbonate considered (permissive hypercapnia).** The CO₂ is allowed to rise because protecting the lung matters more than a normal PaCO₂, and it should rise gradually, so that cells buffer it and the pH falls less. Hypercapnia is not harmless: it raises intracranial pressure by dilating cerebral vessels, constricts pulmonary vessels (raising right-ventricular afterload), depresses myocardial contractility, stimulates a sympathetic surge and shifts the oxyhaemoglobin curve to the right. So it is avoided in raised ICP and used with care in right-ventricular failure."),
  ],
  table=dict(title="ARDSNet acid–base rules", head=["pH", "Action"], rows=[["7.30–7.45", "**goal: no change**"], ["7.15–7.30", "raise rate until pH >7.30 or PaCO₂ <25 (max 35)"], ["<7.15", "rate 35; if still <7.15, raise tidal volume by 1 mL/kg (plateau may exceed 30); bicarbonate may be given"], [">7.45", "lower the rate if possible"]]),
  mimic=[
    ("Permissive hypercapnia vs chasing a normal PaCO₂", "Raising tidal volume to normalise CO₂ undoes the lung protection; ARDSNet raises the rate first and the volume only below pH 7.15."),
  ],
  traps=[
    ("“PaCO₂ 76 in the first hour — raise it faster, or accept SaO₂ 75%”", "Let it rise gradually on the current settings; the oxygen target stays at SpO₂ 88–95% (ARDS-23) (100% got this right)."),
    ("“Hypercapnia lowers ICP”", "It raises ICP through cerebral vasodilation — the ‘NOT deleterious’ answer is decreased ICP."),
    ("“pH 7.27 on 6 mL/kg — continue current settings” (Marrow key)", "Permissive hypercapnia is right in principle, and the tidal volume should not be raised. But by ARDSNet, pH 7.15–7.30 means raise the rate towards 35 if it is lower; choose ‘continue’ only if the options are between that and raising tidal volume. Conversely, Marrow keys ‘increase rate’ at pH 7.32 — the lever is right, but 7.32 is already within the goal."),
    ("“Your notes: pH goal above 7.2”", "Many texts accept ≥7.20 in permissive hypercapnia; the ARDSNet protocol goal is 7.30–7.45."),
  ],
  decode=[
    ("Pneumonia ARDS, P/F 120, AKI, MODS — ARDSNet strategy? [DocT QBank]", "Low tidal volume (4–8 mL/kg PBW) with plateau <30 cmH₂O."),
    ("Influenza ARDS, normal echo, VT 500 — which therapy is best shown to improve survival? [DocT GT]", "6 mL/kg ideal body weight — not diuresis, inhaled vasodilators or recruitment-guided PEEP titration (none has a proven survival benefit, and recruitment with PEEP titration increased mortality in ART)."),
    ("Permissive hypercapnia, PaCO₂ 76 in the first hour — next step? [DocT GT]", "Maintain settings and let it rise gradually."),
    ("On 6 mL/kg: pH 7.32/PaCO₂ 48, or pH 7.27/PaCO₂ 60 — next ventilator step? [Marrow]", "The lever is the respiratory rate (to 35), not the tidal volume; Marrow keys ‘increase rate’ at 7.32 and ‘continue’ at 7.27."),
  ],
  punch="Start at 8 mL/kg PBW, step to 6 (down to 4 if plateau >30), raise the rate to 35 for acidosis, and raise tidal volume only when pH is <7.15 at rate 35 — hypercapnia is tolerated, except where ICP is raised.",
  extra=[dict(q="Harmful effects of hypercapnia?", a="**Raised ICP** (cerebral vasodilation), **pulmonary vasoconstriction** with right-ventricular strain, **reduced myocardial contractility**, sympathetic surge and arrhythmias, **right shift of the oxyhaemoglobin curve**. Decreased ICP is not one of them.")],
)

L['ARDS-23'] = dict(
  sub="Respiratory → ARDS → ARDSNet oxygenation targets",
  step=4,
  intro="The last part of the protocol sets how much oxygen is enough, and how FiO₂ and PEEP climb together to reach it.",
  parts=[
    ('a', "**PaO₂ 55–80 mmHg; SpO₂ 88–95%.** Above this range extra oxygen adds little to delivery, while the FiO₂ and PEEP needed to reach it add their own harm. Going lower is not free either: a trial of a more conservative target in ARDS (LOCO2, PaO₂ 55–70) was stopped early with a signal of harm: higher 90-day mortality and cases of mesenteric ischaemia in the conservative arm."),
    ('b', "**Lower PEEP/FiO₂ table: 0.3/5, 0.4/5–8, 0.5/8–10, 0.6/10, 0.7/10–14, 0.8/14, 0.9/14–18, 1.0/18–24.** If the target is not met, move to the next pair; if it is exceeded, step back. PEEP of 10 belongs with FiO₂ of about 0.5–0.7. This is the table ARMA used; the higher table, from ALVEOLI, pairs each FiO₂ with more PEEP (ARDS-20)."),
  ],
  mimic=[],
  traps=[
    ("“Aim for SpO₂ 100% or PaO₂ >100”", "The target is deliberately modest; hyperoxia is not the aim."),
  ],
  decode=[
    ("Which settings are most consistent with lung-protective ventilation? [DocT QBank]", "Tidal volume 6 mL/kg with PEEP 10 (86% got this right)."),
    ("[pattern] ARDSNet SpO₂ target", "88–95% (PaO₂ 55–80)."),
  ],
  punch="ARDSNet aims for PaO₂ 55–80 and SpO₂ 88–95%, climbing the PEEP/FiO₂ table in pairs until the target is reached.",
)

L['ARDS-24'] = dict(
  sub="Respiratory → ARDS → Pressure–time curve",
  step=5,
  intro="The plateau rule in ARDS-22 depends on reading the airway pressure curve. In volume control with constant flow, a pause at end-inspiration splits the peak into its two parts.",
  parts=[
    ('a', "**1 = peak pressure; 2 = plateau pressure; 3 = PEEP.**"),
    ('b', "**Resistive pressure (airways, tube): flow × resistance.** When flow stops, this part disappears, so the pressure falls from peak to plateau."),
    ('c', "**Driving pressure: the elastic load of the tidal volume.** It is the pressure needed to hold the breath in the lung against its elastic recoil (ARDS-26)."),
    ('d', "**End-inspiratory hold of 0.5–2 s (zero flow), in a passive patient.** With no flow, airway pressure equals alveolar pressure; an active patient’s effort distorts the reading. Total PEEP needs a separate end-expiratory hold, to include any auto-PEEP."),
  ],
  table=dict(title="Reading a pressure rise", head=["Pattern", "Meaning", "Causes"], rows=[["Peak ↑, plateau normal (wide gap)", "**resistance**", "bronchospasm, secretions, kinked or bitten tube"], ["Peak and plateau both ↑ (normal gap)", "**compliance**", "ARDS, pneumothorax, abdominal distension"]]),
  mimic=[],
  traps=[
    ("“Peak pressure reflects lung stretch”", "Peak includes the resistive pressure; plateau reflects the stretch."),
  ],
  decode=[
    ("[pattern] Peak pressure rises from 30 to 45, plateau unchanged at 22 — cause?", "A resistance problem: bronchospasm, secretions or a kinked tube."),
  ],
  punch="Peak minus plateau is resistance, plateau minus PEEP is the elastic load; the plateau needs a no-flow hold in a passive patient.",
)

L['ARDS-25'] = dict(
  sub="Respiratory → ARDS → Pressure differences",
  step=5,
  intro="Each named pressure on a ventilator is a difference between two points along the path from the ventilator to the pleura. Knowing which two points each spans answers both the calculation questions and the subtler question of when the airway pressure can be trusted.",
  parts=[
    ('a', "**Pplat – PEEP = driving pressure, which reflects tidal volume ÷ compliance.** Use the total PEEP (set plus auto-PEEP)."),
    ('b', "**Ppeak – Pplat = resistive pressure, which reflects airway resistance.** This only works in volume control with constant flow; in pressure control the peak is the set pressure, and flow decays, so this gap does not measure resistance."),
    ('c', "**Palv – Ppl = transpulmonary pressure: stress on the lung itself.** This is what over-stretches alveoli (ARDS-28)."),
    ('d', "**Palv – Patm = trans-respiratory pressure: lung plus chest wall.** In a passive patient at zero flow, this is the plateau; it treats the lung and chest wall as one."),
    ('e', "**Ppl – Patm = chest-wall pressure: the chest wall alone.** A stiff chest wall (obesity, abdominal hypertension) takes a larger share of the plateau, so the plateau overstates lung stress."),
  ],
  mimic=[
    ("Respiratory-system vs lung compliance", "Volume ÷ (plateau – PEEP) gives respiratory-system compliance; lung compliance needs pleural (oesophageal) pressure."),
  ],
  traps=[
    ("“Alveolar pressure during the hold is 32 (peak), 18 (plateau – PEEP) or 26” (62–81% chose 24)", "At zero flow, airway pressure equals alveolar pressure: the plateau, 24. 18 is the driving pressure; 32 still includes the resistive part."),
    ("“Pressure control, paralysed asthmatic: compliance is reliable from Pinsp and volume, or resistance from peak – pause” (only 12% got this right)", "Both statements hold only in other circumstances. In pressure control, peak is the set pressure, so peak – pause cannot give resistance; and with flow not reaching zero, or auto-PEEP in an asthmatic, Pinsp – PEEP is not the true elastic pressure. The keyed answer: once paralysis wears off, the patient’s own muscle pressure adds to the ventilator’s, so pleural (oesophageal) pressure is needed to calculate lung compliance."),
  ],
  decode=[
    ("Volume control, end-inspiratory hold: peak 32, plateau 24, PEEP 6 — alveolar pressure? [DocT QBank, DocT GT, three tests]", "24 cmH₂O (the plateau)."),
    ("Asthmatic on pressure control, paralysed, VT 200 mL on Pinsp 25/PEEP 5 — most accurate statement? [DocT GT]", "When paralysis wears off, pleural pressure is needed to calculate pulmonary compliance reliably."),
  ],
  punch="Plateau is alveolar pressure; plateau minus PEEP is driving pressure, peak minus plateau is resistance (in volume control only), and only pleural pressure separates the lung from the chest wall.",
)

L['ARDS-26'] = dict(
  sub="Respiratory → ARDS → Driving pressure",
  step=6,
  intro="Driving pressure brings the deck back to the baby lung. Six mL/kg PBW assumes an average lung; driving pressure measures the breath against the lung that is actually open.",
  parts=[
    ('a', "**Pplat – PEEP = tidal volume ÷ respiratory-system compliance.** 400 mL into a compliance of 25 mL/cmH₂O needs 16 cmH₂O."),
    ('b', "**<15 cmH₂O.** Commonly quoted as ≤14–15."),
    ('c', "**Amato, 2015: of all ventilator variables it was the one most strongly linked to survival; changes in tidal volume or PEEP helped only if they lowered it.** A re-analysis of 3562 patients from nine trials: each rise of one standard deviation (about 7 cmH₂O) carried about 1.4 times the risk of death (relative risk 1.41). This is an association from secondary analysis, not a randomised test of a driving-pressure target."),
    ('d', "**It scales tidal volume to the size of the baby lung (compliance) rather than to predicted body weight.** Two patients with the same height get the same 6 mL/kg, but in the one with less open lung that breath is a larger strain; driving pressure shows it. PEEP that recruits lung raises compliance and lowers driving pressure; PEEP that only over-distends raises it."),
  ],
  mimic=[
    ("Driving pressure vs peak pressure", "Driving pressure uses plateau, not peak, and total PEEP."),
  ],
  traps=[
    ("“High PEEP or a high peak pressure predicts a better outcome”", "Low driving pressure does."),
  ],
  decode=[
    ("Predictor of a better outcome in ARDS [DocT GT PYQ; NEET 2024]", "Low driving pressure (<14–15)."),
  ],
  punch="Driving pressure (plateau – PEEP = VT/compliance) sizes the breath to the open lung; below 15 is the target, and in Amato’s analysis it was the ventilator variable most strongly associated with survival.",
)

L['ARDS-27'] = dict(
  sub="Respiratory → ARDS → Mechanical power",
  step=6,
  intro="Driving pressure looks at one breath. Mechanical power asks how much energy the lung receives every minute, which also counts how often the breath is given and how fast it is pushed in.",
  parts=[
    ('a', "**Energy delivered to the respiratory system per minute (J/min).** Energy per breath (pressure × volume) multiplied by the respiratory rate."),
    ('b', "**0.098 × RR × VT × (Ppeak – ½ driving pressure), VT in litres; bedside surrogate (4 × driving pressure) + RR.** The 0.098 converts L·cmH₂O to joules. RR 20, VT 0.4 L, peak 30, driving pressure 14: 0.098 × 20 × 0.4 × 23 ≈ 18 J/min."),
    ('c', "**Tidal volume, driving pressure, flow, PEEP and respiratory rate.** Flow enters through the resistive part of the peak pressure, PEEP through the static part."),
    ('d', "**Above about 17 J/min (12 J/min in ARDS in some studies) (standard teaching, not in your notes).** The 17 J/min figure is an association with mortality in large observational ICU data (Serpa Neto 2018); the 12 J/min figure comes mainly from experimental work. No randomised trial has tested a power target."),
  ],
  mimic=[
    ("Mechanical power vs driving pressure", "Driving pressure ignores rate; power counts it, so a very high rate used to compensate for a low tidal volume is not harmless."),
  ],
  traps=[
    ("“Mechanical power is airway pressure × time, or pressure × compliance, or excludes PEEP” (only 34% got this right)", "Energy is pressure × volume, not pressure × time; pressure × compliance gives a volume. Power is energy per breath × rate, and PEEP is one of its components."),
  ],
  decode=[
    ("Best description of mechanical power [DocT GT]", "The product of energy per breath and respiratory rate."),
  ],
  punch="Mechanical power is energy per breath times rate (J/min), counting volume, pressure, flow, PEEP and rate; values above about 17 J/min are associated with higher mortality.",
)

L['ARDS-28'] = dict(
  sub="Respiratory → ARDS → Transpulmonary pressure",
  step=5,
  intro="The plateau tells you the pressure across lung and chest wall together (ARDS-25). When the chest wall is stiff, part of that pressure never reaches the lung, and an oesophageal balloon is the way to separate the two.",
  parts=[
    ('a', "**Alveolar pressure (airway pressure at zero flow) – pleural pressure; pleural pressure from an oesophageal balloon in the lower third of the oesophagus.** The oesophagus lies against the pleura, so its pressure approximates pleural pressure; position is checked by an occlusion test, in which airway and oesophageal pressure swings should match."),
    ('b', "**<25 cmH₂O (limits over-distension).**"),
    ('c', "**Positive, about 0 to +3 cmH₂O (EPVent protocol used 0–10), so alveoli stay open; this is how PEEP is titrated.** A negative end-expiratory value means pleural pressure exceeds airway pressure, so dependent alveoli are squeezed shut; PEEP is raised until it is just positive."),
    ('d', "**Stiff chest wall: obesity, raised intra-abdominal pressure, chest-wall oedema; plateau pressure overestimates lung stress here.** A morbidly obese patient may tolerate, and need, a PEEP and plateau that would be excessive in a thin one."),
  ],
  mimic=[
    ("Oesophageal pressure vs alveolar pressure", "Pes approximates pleural pressure, not alveolar, and it is affected by the weight of the chest wall and mediastinum."),
  ],
  traps=[
    ("“PL = Paw + Pes” or “keep end-inspiratory PL above 35”", "PL = Paw – Pes; end-inspiratory PL is kept below about 25."),
    ("“Oesophageal-guided PEEP is proven better”", "EPVent-2 found it no better than an empirical high-PEEP table (standard teaching, not in your notes)."),
  ],
  decode=[
    ("Obese ARDS, end-expiratory Pes 20, PEEP 15 — interpretation? [DocT GT]", "PL –5 cmH₂O: dependent alveoli likely collapsed; PEEP should be raised."),
  ],
  punch="Transpulmonary pressure is airway minus oesophageal pressure; keep it just positive at end-expiration and below about 25 at end-inspiration — most useful when a stiff chest wall makes the plateau misleading.",
)

L['ARDS-29'] = dict(
  sub="Respiratory → ARDS → Revision: true or false",
  step=6,
  intro="A sweep through the deck. Each statement turns on one detail from an earlier card.",
  parts=[
    ('a', "**False — ARMA used predicted body weight** (ARDS-19, ARDS-21)."),
    ('b', "**False — a ROX of 5 at 12 h is ≥4.88, which predicts HFNC success** (ARDS-15)."),
    ('c', "**True — HACOR above 5 at 1 h predicts NIV failure in over 80%** (ARDS-16)."),
    ('d', "**False — driving pressure is plateau – PEEP, not peak – PEEP** (ARDS-26)."),
    ('e', "**False — ALVEOLI showed no mortality difference with higher PEEP** (ARDS-20)."),
    ('f', "**True — the ARDSNet SpO₂ target is 88–95%, with PaO₂ 55–80** (ARDS-23)."),
    ('g', "**True — PEEP prevents atelectrauma by stopping cyclic collapse** (ARDS-18)."),
  ],
  mimic=[],
  traps=[
    ("“A higher ROX is worse”", "Lower ROX is worse; higher HACOR is worse."),
  ],
  decode=[
    ("ROX formula on HFNC [DocT GT]", "SpO₂/FiO₂ ÷ RR (83% got this right)."),
    ("[pattern] Statements about scores and trials", "ROX lower is worse, HACOR higher is worse; ARMA used PBW; no single PEEP trial cut mortality."),
  ],
  punch="Most errors here come from direction (low ROX, high HACOR are bad), the plateau-not-peak rule and the negative PEEP trials.",
)

FLAGS = {}
FLAGS['ARDS-14'] = "DocT HFNC-mechanism keys (‘positive pressure to maintain airway patency’, ‘mild positive pressure’) overstate HFNC’s PEEP (about 1 cmH₂O per 10 L/min, mouth closed); the main mechanisms are a reliable FiO₂, dead-space washout and lower work of breathing. Keys still the best options. Several stems put HFNO on an already ventilated patient. Card is right."
FLAGS['ARDS-17'] = "DocT CGT4 key says high VT on NPPV ‘is a marker of low lung compliance’; more precisely it marks high respiratory drive acting on a small lung. Key is the best option; card is right."
FLAGS['ARDS-22'] = "Marrow keys conflict with the ARDSNet protocol and with each other: ‘continue settings’ at pH 7.27 (protocol: raise rate towards 35 when pH 7.15–7.30), and ‘increase rate’ at pH 7.32 (within the 7.30–7.45 goal). Card is right."
FLAGS['ARDS-27'] = "Card’s ‘12 J/min in ARDS in some studies’: this threshold comes mainly from experimental (animal) data; 17 J/min is an observational association (Serpa Neto 2018). No power threshold has been tested in a randomised trial. Explanation says so."
