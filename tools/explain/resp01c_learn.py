# RESP01C — Explain v3 ("Learn" depth): ARDS III — Rescue therapies, drugs, fluids and outcome. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP01C.md. Fields as TOX01, plus SPINE, PRIMER and step.

SPINE = [
  ("Prone: the proven rescue", "Prone positioning for at least 16 h a day, started early when P/F is below 150, roughly halved mortality in PROSEVA because it spreads strain evenly through the lung, not because it raises the PaO₂."),
  ("Forcing the lung open failed", "Recruitment manoeuvres and high-frequency oscillation both open the lung with high pressure, and in ART and OSCILLATE that pressure cost lives, while OSCAR showed no gain."),
  ("ECMO and inhaled vasodilators", "When protective ventilation and prone have failed, VV-ECMO is the rescue for set EOLIA thresholds, while inhaled vasodilators improve oxygenation for a day or two without improving survival."),
  ("Drugs, fluids and feeding", "Paralysis, conservative fluids after shock and early steroids shorten ventilation more reliably than they save lives, late steroids harm, and almost every other drug tested has failed."),
  ("How patients die and recover", "Most patients die of sepsis and multi-organ failure rather than hypoxaemia, and survivors’ lasting disability is in muscle and mind, not in the lung."),
  ("Trials at a glance", "Each landmark trial is asked as a one-line verdict: which arm, which outcome, and whether it was significant."),
]

PRIMER = "This deck assumes the basic lung-protective strategy is already running: tidal volume 6 mL/kg predicted body weight, plateau pressure ≤30 cmH₂O and adequate PEEP (ARDSNet, ARMA). Ventilator-induced lung injury (VILI) is damage done by the ventilator itself — over-stretching open alveoli (volutrauma), and repeated opening and closing of unstable ones (atelectrauma) — and most rescue therapies are judged by whether they reduce it. A therapy can improve PaO₂ without improving survival, so the questions always ask which outcome a trial changed: mortality, ventilator-free days, or only oxygenation. Ventilator-free days count the days alive and off the ventilator in the first 28, so they rise if patients either survive or come off the ventilator sooner."

L = {}

L['ARDS-30'] = dict(
  sub="Respiratory → ARDS → Prone positioning (PROSEVA)",
  step=1,
  intro="Once lung-protective ventilation is running and the P/F ratio is still below 150, the next step with a proven survival benefit is prone positioning. PROSEVA is the trial behind every number examiners ask: the P/F threshold, the hours per day and the size of the benefit.",
  parts=[
    ('a', "**P/F <150 on FiO₂ ≥0.6, PEEP ≥5 and tidal volume about 6 mL/kg, confirmed after 12–24 h of stabilisation.** The stabilisation period matters: many patients improve once ventilation is optimised, so only those still below 150 after 12–24 h were enrolled — moderate-to-severe ARDS, not mild. That is why <150 is the keyed threshold, not <200 or <100."),
    ('b', "**Within 36 h of intubation; sessions of at least 16 h a day (your notes: 12–18 h).** PROSEVA proned early and for long sessions (average about 17 h); patients stayed prone daily until oxygenation held in the supine position. Short sessions let the dorsal lung collapse again each time the patient is turned back."),
    ('c', "**28-day mortality 16.0% vs 32.8%.** A halving of mortality, and the benefit persisted at 90 days. Current guidance recommends prolonged prone sessions — ESICM 2023 more than 16 h a day in moderate-to-severe ARDS, ATS more than 12 h a day in severe ARDS; it comes before ECMO, not after it (ARDS-35)."),
  ],
  mimic=[
    ("PROSEVA vs the earlier prone trials", "Earlier trials proned later, for shorter sessions (some about 7 h a day) and included milder ARDS; they improved oxygenation but not survival. PROSEVA changed all three."),
    ("Prone vs ECMO for refractory hypoxaemia", "Prone has a proven mortality benefit and is tried first; ECMO is for hypoxaemia that persists despite prone (ARDS-35)."),
  ],
  traps=[
    ("“Prone for at least 6 h a day is enough”", "PROSEVA used ≥16 h; 6 h is a distractor. One DocT GT paper prints the keyed option as ‘≤16 hours/day’ — a misprint; pick the prone option whatever sign is printed."),
    ("“P/F 105 on FiO₂ 1.0, PEEP 8, paralysed — start ECMO, inhaled NO or oesophageal-pressure PEEP” (only 59% chose prone)", "P/F 105 is below 150 and prone has not been tried, so prone is next. ECMO is not yet indicated (P/F not <80 and prone not tried), inhaled NO improves only oxygenation, and oesophageal-pressure-guided PEEP had no outcome benefit (EPVent-2)."),
    ("“Avoid prone in severe ARDS”", "The reverse: prone is recommended in moderate-to-severe ARDS, and severe ARDS is where it matters most. This was the NEET 2025 ‘should NOT be done’ answer."),
    ("“Proning improves oxygenation but does not affect mortality”", "PROSEVA halved 28-day mortality."),
    ("“Methylprednisolone 2 mg/kg/day gives the most mortality benefit” (DocT GT distractor)", "Prone ≥16 h has the largest and most consistent mortality benefit, so it is the answer. Early corticosteroids are now conditionally recommended (DEXA-ARDS; ATS 2024, SCCM 2024; ARDS-40), but that is weaker evidence than PROSEVA, and 2 mg/kg/day is not the regimen behind the current recommendation."),
  ],
  decode=[
    ("At what P/F ratio is prone positioning recommended? [NEET 2024, DocT GT]", "<150."),
    ("Moderate ARDS, P/F 140 on PEEP 10 — which intervention gives the most mortality benefit? [DocT GT]", "Prone ≥16 h a day."),
    ("Intubated pneumonia, P/F 105 on FiO₂ 1.0, PEEP 8, paralysed — next step? [DocT GT]", "Prone the patient."),
    ("Moderate–severe ARDS: which should NOT be done about prone ventilation? [NEET 2025]", "Avoiding prone in severe ARDS."),
  ],
  punch="PROSEVA: P/F <150 on FiO₂ ≥0.6 after 12–24 h, proned within 36 h for ≥16 h a day, cut 28-day mortality from 32.8% to 16.0% — so prone comes before ECMO, nitric oxide or HFOV.",
)

L['ARDS-31'] = dict(
  sub="Respiratory → ARDS → Prone positioning: mechanism",
  step=1,
  intro="Why should turning a patient over halve mortality? In the supine ARDS lung, the weight of the oedematous lung, the heart and the abdomen squeeze the dorsal regions shut, so a small ventral lung takes every breath. Turning the patient prone changes where that weight falls.",
  parts=[
    ('a', "**The pleural-pressure gradient becomes more uniform and the dorsal lung is recruited (more lung mass lies dorsally).** Supine, pleural pressure is much less negative over the dependent dorsal lung, so it collapses. Prone, the dorsal lung becomes non-dependent and re-opens, and because more of the lung’s tissue lies dorsally, more lung is gained there than is lost ventrally. The shape of the lung also fits the chest wall better prone, so ventilation spreads more evenly."),
    ('b', "**Perfusion stays mainly dorsal, so V/Q matching improves and shunt falls.** Pulmonary blood flow goes mostly to the dorsal lung whichever way the patient lies. Supine, that well-perfused lung was the collapsed part — shunt; prone, it is re-aerated, so ventilation and perfusion now meet in the same regions."),
    ('c', "**The heart and abdomen no longer compress the lung; the right ventricle is unloaded; secretions drain.** Prone, the heart rests on the sternum rather than on the lower lobes. Recruitment and a lower PaCO₂ reduce pulmonary vascular resistance, which offloads a strained right ventricle (acute cor pulmonale, ARDS-43). Gravity drains secretions from the dorsal airways."),
    ('d', "**More homogeneous strain → less VILI.** When ventilation is spread over more open lung, each alveolus is stretched less, and fewer units open and close with every breath. This, not the higher PaO₂, is thought to be why survival improves."),
  ],
  mimic=[
    ("Oxygenation response vs survival benefit", "In PROSEVA, the gain in PaO₂ after proning did not predict who survived; patients whose PaO₂ does not rise still benefit, so a non-responder is not a reason to stop."),
    ("Prone vs raising mean airway pressure", "Inverse-ratio ventilation, HFOV and recruitment manoeuvres open lung with pressure; prone opens it by redistributing weight, without raising pressure."),
  ],
  traps=[
    ("“Proning works by raising mean airway pressure”, “by reducing dead space through airway patency” or “by improving chest-wall compliance”", "Its main effect is redistribution of ventilation to the dorsal lung, where perfusion already is. The keyed options say ‘V/Q matching by redistributing ventilation to dorsal regions’ or ‘to more compliant regions’."),
    ("“The main goal of proning is to prevent pressure sores or remove lung fluid”", "Pressure sores are a complication of proning (ARDS-32); the goal is recruitment and oxygenation."),
    ("“Severe ARDS, FiO₂ 0.8, Pplat 30, pH 7.22 — increase VT, reduce PEEP or target PaCO₂ <40” (DocT keys inverse-ratio ventilation)", "With prone not offered, IRV is the least harmful option because it raises mean airway pressure without raising tidal volume or plateau pressure. It has no outcome evidence and is in no ARDS guideline; pH 7.22 is acceptable permissive hypercapnia, so do not chase PaCO₂ <40. If prone is offered, choose prone."),
  ],
  decode=[
    ("Primary mechanism by which proning improves oxygenation? [DocT]", "Better V/Q matching by redistributing ventilation to the dorsal lung."),
    ("Image of a prone patient — primary goal of this position? [DocT]", "Alveolar recruitment and oxygenation."),
    ("Which statement about proning is true? (≥6 h, ‘no mortality effect’ as distractors) [DocT]", "It improves oxygenation by redistributing ventilation and perfusion."),
    ("Severe ARDS, Pplat 30, pH 7.22, no prone option — best strategy to improve oxygenation without VILI? [DocT, DocT GT]", "Inverse-ratio ventilation (best of the options; prone if offered)."),
  ],
  punch="Prone re-opens the heavy dorsal lung where the blood already flows, so V/Q improves; its survival benefit comes from spreading strain evenly and reducing VILI, not from the rise in PaO₂.",
)

L['ARDS-32'] = dict(
  sub="Respiratory → ARDS → Prone positioning: contraindications and complications",
  step=1,
  intro="Prone is the step that saves lives, so the questions test when you cannot do it — and then what comes instead — and what goes wrong when you do.",
  parts=[
    ('a', "**Contraindications: unstable spine (absolute); raised intracranial pressure; open chest or abdomen; recent sternotomy or tracheal surgery; facial or pelvic fractures; massive haemoptysis; severe haemodynamic instability; life-threatening arrhythmia; late pregnancy (relative).** Each is either something turning could injure (an unstable spine, fresh wounds, fractures that bear weight face-down), something prone worsens (prone with the head turned can raise ICP and impede venous drainage), or a patient who cannot be resuscitated face-down. When prone is contraindicated and the patient meets EOLIA criteria, VV-ECMO is the next step (ARDS-35)."),
    ('b', "**Complications: tube obstruction or displacement; loss of lines and drains; pressure sores (face, chest, knees); facial and eye oedema; brachial plexus injury; feed intolerance and vomiting; transient desaturation.** The dangerous ones happen during the turn — the tube and lines. Pressure sores are the commonest, on the face, chest and knees, which bear the weight. Facial and eye oedema, and eye injury from pressure, are why the face is padded and moved regularly."),
  ],
  mimic=[
    ("Raised ICP as contraindication vs complication", "Raised ICP is a reason not to prone; facial and ocular injury is the keyed ‘major complication’ of proning itself."),
  ],
  traps=[
    ("“Increased intracranial pressure is the major complication of proning” (only 67% chose facial and ocular injury)", "Raised ICP belongs to the contraindications. The keyed complication is facial and ocular injury, which follows from lying face-down for 16 h."),
    ("“Polytrauma with uncleared C-spine and chest lacerations, P/F <150 — prone the patient” (only 52% chose ECMO)", "Prone is contraindicated (unstable spine, open chest-wall wounds). With PaO₂ 67 on FiO₂ 1.0 — P/F 67 — for 6 h despite optimal ventilation and paralysis, he meets the EOLIA oxygenation criterion (<80 for >6 h), so VV-ECMO is next."),
    ("Two correct options in one DocT GT question", "‘Proning improves oxygenation by redistributing ventilation and perfusion’ is keyed, but ‘proning is contraindicated in spinal fractures’ is also true (unstable spine is absolute). Pick the keyed mechanism statement."),
  ],
  decode=[
    ("Major complication of prone positioning? [DocT]", "Facial and ocular injuries."),
    ("Uncleared C-spine, ventral chest lacerations, P/F 67 for 6 h, paralysed — next step? [DocT GT]", "VV-ECMO (prone contraindicated)."),
    ("Proned, ventilated TBI patient desaturates acutely — what to assess first? [Marrow]", "Tube dislodgement or obstruction."),
  ],
  punch="Do not prone an unstable spine, raised ICP, an open chest or abdomen or a peri-arrest patient; when you do prone, watch the tube and lines at every turn and the face and eyes for pressure injury.",
  extra=[dict(q="A proned, ventilated patient suddenly desaturates: first step?", a="**Check the tube first: displacement or obstruction** (Marrow), before blaming the lung — the turn is when tubes move.")],
)

L['ARDS-33'] = dict(
  sub="Respiratory → ARDS → Recruitment manoeuvres (ART)",
  step=2,
  intro="If collapsed lung can be re-opened with pressure, why not do it deliberately? A recruitment manoeuvre is a brief, high pressure to open collapsed alveoli, followed by enough PEEP to keep them open. The idea is sound physiology; the ART trial is why it is no longer routine.",
  parts=[
    ('a', "**Sustained inflation: CPAP 40 cmH₂O for 30–40 s.** The pressure must exceed the opening pressure of collapsed units. The other method is stepwise (staircase) recruitment: PEEP is raised in steps, then lowered in a decremental trial while static compliance is tracked — the step at which compliance suddenly falls is the derecruitment point, and PEEP is set about 2 cmH₂O above it after re-recruiting. Whatever the method, the gain is lost unless PEEP holds the lung open afterwards."),
    ('b', "**Hypotension (fall in venous return), barotrauma, desaturation.** High intrathoracic pressure squeezes the great veins and loads the right ventricle, so cardiac output falls during the manoeuvre. Over-stretching already-open alveoli can rupture them (pneumothorax). Oxygenation can fall transiently as blood is pushed towards unrecruited lung and output drops."),
    ('c', "**Stepwise recruitment plus PEEP titrated to best compliance vs low PEEP: higher mortality and more barotrauma with recruitment.** ART (Cavalcanti, JAMA 2017; about 1000 patients with moderate-to-severe ARDS) found 28-day mortality 55.3% vs 49.3%, with more pneumothorax needing drainage. ESICM 2023 and the 2024 ATS update both make a strong recommendation against prolonged high-pressure recruitment manoeuvres, and ESICM also suggests (weakly) against brief high-pressure manoeuvres."),
  ],
  mimic=[
    ("Derecruitment vs pneumothorax as a cause of sudden desaturation", "After open suctioning or a disconnection, the lung derecruits and compliance falls; a pneumothorax adds unilateral absent breath sounds and haemodynamic collapse — exclude it before any recruitment manoeuvre."),
  ],
  traps=[
    ("“Recruitment manoeuvres every 4 h maintain alveolar stability”", "Routine, repeated manoeuvres are not recommended; ART showed harm."),
    ("“PEEP after a recruitment manoeuvre is to prevent over-distension or improve cardiac output”", "It is there to keep open what the manoeuvre opened (DocT GT, 100% right)."),
    ("“Recruitment manoeuvres are a grade B recommendation”", "In the Harrison table Marrow uses, recruitment manoeuvres are grade C; low tidal volume is A, and conservative fluids, higher PEEP, prone and ECMO are B."),
  ],
  decode=[
    ("Recommended sustained-inflation technique? [DocT GT]", "CPAP 30–40 cmH₂O."),
    ("Purpose of PEEP after a recruitment manoeuvre? [DocT GT]", "To maintain the recruitment achieved."),
    ("Decremental PEEP trial: static compliance suddenly falls before oxygenation worsens — what happened? [DocT GT]", "Alveolar derecruitment."),
    ("Desaturation after open suctioning in ventilated pneumonia — next step? [Marrow]", "Recruitment manoeuvre (after excluding pneumothorax)."),
  ],
  punch="A recruitment manoeuvre (CPAP 40 for 30–40 s) opens lung only if PEEP then holds it open, costs blood pressure and risks barotrauma — and in ART, recruitment with compliance-titrated PEEP increased mortality.",
  extra=[dict(q="Desaturation after open suctioning in ARDS: why, and what then?", a="**Disconnection loses PEEP and the lung derecruits.** Exclude pneumothorax, then recruit; pre-oxygenate with FiO₂ 1.0 and use a closed in-line system when PEEP or FiO₂ is high (Marrow).")],
)

L['ARDS-34'] = dict(
  sub="Respiratory → ARDS → High-frequency oscillation (OSCAR, OSCILLATE)",
  step=2,
  intro="HFOV takes the open-lung idea to its limit: hold the lung open with a constant high mean airway pressure and move gas with tiny oscillations, so there is no cyclic stretch at all. In theory it is the ideal lung-protective mode; two large trials in 2013 showed it is not.",
  parts=[
    ('a', "**OSCAR: no difference in mortality. OSCILLATE: higher mortality (stopped early).** OSCAR (UK, about 800 patients) found 30-day mortality almost identical in the two arms. OSCILLATE (Canada and elsewhere, about 550 patients) was stopped early because in-hospital mortality was higher with HFOV (about 47% vs 35%)."),
    ('b', "**High mean airway pressure → haemodynamic compromise, more vasopressors, sedation and paralysis.** HFOV holds a constant high mean airway pressure for oxygenation, which reduces venous return and raises right-ventricular afterload. In OSCILLATE, the HFOV arm needed more vasoactive drugs, midazolam and neuromuscular blockade."),
    ('c', "**Not recommended for routine use in adult ARDS.** The ATS/ESICM/SCCM 2017 guideline makes a strong recommendation against routine HFOV in moderate-to-severe ARDS; the 2023 ESICM guideline did not revisit it."),
  ],
  table=dict(title="How HFOV works — the details the stems test", head=["Feature", "HFOV"], rows=[["Oxygenation", "set by **mean airway pressure** (high, CPAP-like) and FiO₂"], ["Tidal volume", "1–3 mL/kg, **below dead space**"], ["Frequency", "3–15 Hz (180–900/min)"], ["Expiration", "**active** (the piston pulls gas back)"], ["CO₂ clearance", "rises with **amplitude (ΔP)** and with **lower** frequency"], ["Gas transport", "Taylor dispersion, pendelluft, asymmetric velocity profiles, molecular diffusion, plus bulk flow to proximal units"]]),
  mimic=[
    ("HFOV vs high-frequency jet ventilation", "HFJV pulses small jets at about 100–200/min with passive expiration; its niche is airway surgery and a large bronchopleural fistula, not ARDS. Neither improves adult ARDS survival."),
    ("OSCAR vs OSCILLATE", "OSCAR: no difference. OSCILLATE: harm. NEET 2024 asked OSCAR: ‘HFO in adult ARDS — no benefit’."),
  ],
  traps=[
    ("“HFOV provides low inspiratory pressures”", "It runs a high mean airway pressure; its theoretical advantage is tiny tidal volumes at high rates, not low pressure."),
    ("“In HFOV expiration is passive” or “raising the frequency clears more CO₂”", "Expiration is active; lowering the frequency lengthens each cycle, enlarges the tidal volume and clears more CO₂."),
    ("“HFOV is the preferred rescue over prone positioning”", "Prone has the survival benefit; HFOV harmed or did nothing."),
    ("“The keyed ‘advantage’ means HFOV is recommended”", "DocT keys the theoretical mechanism (small volumes, high rates, less VILI); the trials failed, so it is not recommended routinely."),
  ],
  decode=[
    ("Primary advantage of HFOV in ARDS? [DocT, DocT GT]", "Very small tidal volumes at very high rates, minimising VILI (in theory)."),
    ("How is gas transported during HFOV? [DocT GT]", "Taylor dispersion and pendelluft, with tidal volumes smaller than dead space."),
    ("Primary advantage of HFJV in ARDS? [DocT, DocT GT]", "Very small tidal volumes at high rates (theory only; no outcome benefit)."),
    ("OSCAR trial was about? [NEET 2024]", "HFOV in adult ARDS: no benefit."),
  ],
  punch="HFOV oxygenates with a high mean airway pressure and moves gas below the dead space, but OSCAR showed no benefit and OSCILLATE showed harm, so it is not used routinely in adult ARDS.",
)

L['ARDS-35'] = dict(
  sub="Respiratory → ARDS → VV-ECMO: indications",
  step=3,
  intro="When the lung cannot exchange gas even with protective ventilation, paralysis and prone, VV-ECMO takes over that job outside the body, so the ventilator can be turned down to rest the lung. The questions test the thresholds and, above all, the order: prone first, ECMO after.",
  parts=[
    ('a', "**P/F <80 on FiO₂ ≥0.9 despite optimal ventilation and prone (EOLIA: <50 for 3 h or <80 for 6 h).** ECMO is a rescue for persistent, severe hypoxaemia after optimal care including prone. DocT keys ‘P/F <100 despite optimal ventilation’: that is the older ELSO threshold (P/F <100 on FiO₂ >0.9 for 6 h or more despite optimal care, marking a mortality risk of 80% or more; P/F <150 marked about 50%, when ECMO should be considered), and it is still the best option when <80 is not offered."),
    ('b', "**PaCO₂ >80 mmHg or inability to keep plateau ≤30 (EOLIA: pH <7.25 with PaCO₂ ≥60 for 6 h).** Here the problem is ventilation: the CO₂ cannot be cleared without injurious pressures. ECMO removes CO₂ very efficiently, so the ventilator can stay protective."),
    ('c', "**Severe air-leak syndromes.** A large bronchopleural fistula leaks with every positive-pressure breath; ECMO lets the ventilator be turned right down so the leak can close."),
    ('d', "**Ventilated >7 days at high pressures; contraindication to anticoagulation; irreversible disease; severe brain injury (standard teaching, not in your notes).** ECMO is a bridge to recovery, so it is pointless when the lung or the patient cannot recover: irreversible multi-organ failure is the keyed contraindication. Age alone is not one — it only lowers the predicted survival (RESP score)."),
  ],
  table=dict(title="EOLIA entry: any one, despite optimal ventilation", head=["Criterion", "Threshold"], rows=[["Severe hypoxaemia", "P/F **<50 for >3 h**"], ["Persistent hypoxaemia", "P/F **<80 for >6 h**"], ["Hypercapnic acidosis", "**pH <7.25 with PaCO₂ ≥60** for >6 h"]]),
  mimic=[
    ("VV vs VA ECMO", "VV supports the lung only and needs a working heart; VA also supports the circulation. Severe ARDS with a normal echo → VV."),
    ("Prone vs ECMO", "Prone has the proven mortality benefit and goes first; ECMO is for failure of prone or when prone is contraindicated (ARDS-32)."),
  ],
  traps=[
    ("“Refractory ARDS: ECMO” when prone positioning is also offered (DocT keys ECMO; 75% agreed)", "Guidelines put prone ≥16 h a day before ECMO, and ECMO thresholds are read as ‘despite optimal ventilation’, which includes prone. If prone has not been tried, the evidence-based answer is prone; pick ECMO once prone has failed or is contraindicated."),
    ("“Persistent hypercapnia with pH <7.25” as the ECMO criterion (only 63% chose P/F <100)", "Incomplete: EOLIA needs pH <7.25 with PaCO₂ ≥60 for >6 h; ‘FiO₂ >90%’ alone is also incomplete. The P/F threshold despite optimal ventilation is the cleanest answer."),
    ("“Age >60 is a contraindication”", "Not in itself; irreversible multi-organ failure is."),
    ("“Recruitment manoeuvres, HFOV or a larger tidal volume” for P/F 55 after prone and paralysis", "ART and OSCILLATE showed harm; with P/F 55 after optimal care, VV-ECMO is next."),
    ("Polytrauma vignette: “pH 7.25 with PaCO₂ 68 for 6 h meets EOLIA”", "Strictly, EOLIA needs pH below 7.25; the stronger reason is P/F 67 on FiO₂ 1.0 for 6 h, which meets the <80 for >6 h criterion. Either way VV-ECMO is right, because prone is contraindicated."),
  ],
  decode=[
    ("Most appropriate criterion to start ECMO in ARDS? [DocT]", "P/F <100 (or <80) despite optimal ventilation, including prone."),
    ("Key contraindication to ECMO in ARDS? [DocT]", "Severe, irreversible multi-organ failure."),
    ("Severe ARDS, hypoxaemic despite protective ventilation, paralysis and prone, normal echo — which configuration? [DocT GT]", "Venovenous ECMO."),
    ("P/F 55 despite prone and NMB — next step? [DocT GT]", "Initiate VV-ECMO."),
  ],
  punch="VV-ECMO is for P/F <80 for 6 h, <50 for 3 h, or pH <7.25 with PaCO₂ ≥60 for 6 h despite optimal ventilation — after prone, or when prone is contraindicated — and not for irreversible disease.",
)

L['ARDS-36'] = dict(
  sub="Respiratory → ARDS → ECMO trials (CESAR, EOLIA)",
  step=3,
  intro="Two trials sit behind ECMO in ARDS, and neither alone proved it saves lives. The question is always what each actually tested and whether the result was significant.",
  parts=[
    ('a', "**CESAR: 180 patients, transfer to an ECMO centre vs conventional care. EOLIA: 249 patients, early ECMO vs conventional ventilation with rescue ECMO.** CESAR tested a referral strategy, not ECMO itself; EOLIA tested ECMO itself, started early."),
    ('b', "**CESAR: survival without severe disability at 6 months 63% vs 47% (RR 0.69, P = 0.03). EOLIA: 60-day mortality 35% vs 46%, P = 0.09, not significant.** EOLIA’s secondary outcome, treatment failure (death, or crossover to ECMO in the control arm), was clearly reduced — the NEET 2025 answer."),
    ('c', "**CESAR: only 75% of the ECMO arm received ECMO; control care was not protocolised. EOLIA: 28% of controls crossed over to ECMO; stopped early.** CESAR’s benefit may reflect expert-centre care rather than ECMO. EOLIA’s crossovers diluted the difference, and it stopped for futility before reaching its planned size; later Bayesian and pooled analyses suggested a probable benefit, and the 2024 ATS update suggests VV-ECMO for selected patients with severe ARDS."),
  ],
  mimic=[
    ("EOLIA’s two P values", "0.09 for the primary outcome (60-day mortality, RR 0.76) and 0.07 for the time-to-death analysis to day 60 (hazard ratio 0.70; your notes’ ‘survival curve’); neither is significant."),
  ],
  traps=[
    ("“EOLIA showed a significant mortality benefit”", "35% vs 46%, P = 0.09: not significant (ARDS-46c)."),
    ("“EOLIA showed ECMO had no effect” or “increased mortality”", "The point estimate favoured ECMO and treatment failure fell; ‘no significant mortality benefit but less treatment failure’ is the keyed answer."),
  ],
  decode=[
    ("Key findings of EOLIA? [NEET 2025]", "No statistically significant mortality benefit, but reduced treatment failure."),
    ("[pattern] What did CESAR actually test?", "Referral to an ECMO centre, not ECMO itself."),
  ],
  punch="CESAR showed that referral to an ECMO centre improved survival without severe disability (63% vs 47%); EOLIA’s 35% vs 46% fell short of significance (P = 0.09) but reduced treatment failure.",
)

L['ARDS-37'] = dict(
  sub="Respiratory → ARDS → Inhaled nitric oxide and prostacyclin",
  step=3,
  intro="Inhaled vasodilators are the other rescue for refractory hypoxaemia. They are a clear example of a therapy that improves the blood gas without improving survival.",
  parts=[
    ('a', "**Selective vasodilation of ventilated units only → better V/Q matching; lowers pulmonary artery pressure without systemic hypotension.** An inhaled gas reaches only open alveoli, so only their vessels dilate and blood is drawn away from shunt units. Nitric oxide is inactivated by haemoglobin as soon as it reaches the blood, so it has no systemic effect."),
    ('b', "**Oxygenation improves for 24–72 h; no mortality benefit.** The gain fades within a few days and no trial has shown fewer deaths; it is a bridge, for example to ECMO, not a treatment."),
    ('c', "**Methaemoglobinaemia, nitrogen dioxide, rebound pulmonary hypertension on withdrawal, renal dysfunction.** NO oxidises haemoglobin to methaemoglobin and reacts with oxygen to form toxic NO₂, so both are monitored. Meta-analyses found more acute kidney injury with iNO. Abrupt withdrawal can cause rebound pulmonary hypertension, so it is weaned."),
  ],
  mimic=[
    ("Inhaled vs intravenous vasodilators", "Intravenous vasodilators dilate the vessels of unventilated units too, abolish hypoxic vasoconstriction and worsen shunt."),
  ],
  traps=[
    ("“Inhaled nitric oxide improves survival”", "It improves oxygenation only, and transiently (ARDS-46e)."),
  ],
  decode=[
    ("[pattern] iNO in severe ARDS — which statement is true?", "Improves oxygenation transiently; no mortality benefit; renal dysfunction."),
  ],
  punch="Inhaled vasodilators dilate only ventilated units, so V/Q improves for a day or two — but survival does not, and nitric oxide adds methaemoglobin, NO₂, rebound and kidney injury.",
)

L['ARDS-38'] = dict(
  sub="Respiratory → ARDS → Neuromuscular blockade (ACURASYS, ROSE)",
  step=4,
  intro="Paralysis was meant to protect the lung by stopping the patient fighting the ventilator: dyssynchrony, double-triggered breaths and big swings in transpulmonary pressure stretch the lung beyond what the settings allow. Two trials gave opposite answers, and the reason is in the control arms.",
  parts=[
    ('a', "**Cisatracurium infusion for 48 h, early ARDS with P/F <150.** Both trials enrolled within 48 h of ARDS onset. Cisatracurium was chosen because its elimination does not depend on the liver or kidney."),
    ('b', "**ACURASYS: better adjusted 90-day survival, less barotrauma, no excess weakness. ROSE: no difference in 90-day mortality.** ACURASYS (340 patients) found the benefit only after adjustment for baseline severity (crude 90-day mortality 31.6% vs 40.7%, P = 0.08); ROSE (about 1000 patients) found 90-day mortality almost identical (about 43% in each arm) and was stopped for futility."),
    ('c', "**ROSE controls had light sedation (ACURASYS controls were deeply sedated), and ROSE used higher PEEP; less proning in ROSE.** In ACURASYS, the comparison was paralysis vs deep sedation alone; in ROSE, it was paralysis with deep sedation vs light sedation, with a higher-PEEP strategy in both arms, which may itself reduce injurious effort."),
  ],
  mimic=[
    ("Routine vs selective paralysis", "Routine early paralysis is not supported after ROSE (ESICM 2023 recommends against routine continuous infusion); short paralysis is used for severe dyssynchrony despite deep sedation, during proning, or when plateau pressure cannot be controlled. The 2024 ATS update suggests it in early severe ARDS."),
  ],
  traps=[
    ("“Early neuromuscular blockade helps every ARDS patient” (77% of the cohort got this right)", "Against low tidal volume, higher PEEP and prone, early routine NMB is the one with no consistent benefit after ROSE."),
    ("“Use NMB indefinitely” or “no role of NMB” for persistent dyssynchrony despite deep sedation", "Use it for a short period, about 24–48 h (NEET 2025)."),
  ],
  decode=[
    ("Atypical pneumonia → ARDS: which intervention is least likely to help? [DocT GT]", "Early neuromuscular blockade."),
    ("Persistent dyssynchrony despite deep sedation — NMB, and for how long? [NEET 2025]", "Yes, short duration (about 24–48 h)."),
  ],
  punch="ACURASYS (paralysis vs deep sedation) suggested benefit, ROSE (vs light sedation, higher PEEP) found none, so paralysis is now for 24–48 h in selected patients — dyssynchrony, proning, uncontrolled plateau pressure.",
)

L['ARDS-39'] = dict(
  sub="Respiratory → ARDS → Fluid strategy (FACTT)",
  step=4,
  intro="A leaky lung floods more when filling pressures are high, so less fluid should mean less oedema. FACTT tested that, but only once the patient was out of shock — the condition the question stem always hides in the wording.",
  parts=[
    ('a', "**Conservative (CVP <4 or PAOP <8) vs liberal (CVP 10–14 or PAOP 14–18) fluid strategy over 7 days (1000 patients).** The conservative arm used diuretics and fluid restriction guided by filling pressures, urine output and perfusion — and only in patients who were no longer in shock."),
    ('b', "**–136 mL vs +6992 mL.** The cumulative 7-day balance: roughly even with the conservative strategy, about 7 L positive with the liberal one."),
    ('c', "**60-day mortality 25.5% vs 28.4%: not significant.**"),
    ('d', "**Ventilator-free days 14.6 vs 12.1, more ICU-free days, no increase in shock or dialysis.** Less lung water meant better oxygenation and earlier extubation, without harming the kidneys."),
    ('e', "**Pulmonary artery catheter vs central venous catheter: no difference (27.4% vs 26.3%), more catheter complications with the PA catheter.** The paired catheter comparison showed a PA catheter added nothing but complications, mainly arrhythmias."),
  ],
  mimic=[
    ("Resuscitation vs de-resuscitation", "Fluids for shock come first; FACTT’s conservative strategy applies after shock has resolved."),
  ],
  traps=[
    ("“Conservative fluids reduced mortality”", "Not significant (25.5% vs 28.4%); the gain was ventilator-free days."),
    ("“Routine pulmonary artery catheter-guided resuscitation”", "FACTT’s catheter comparison found no benefit and more complications."),
  ],
  decode=[
    ("Haemodynamically stable ARDS — which fluid strategy improves oxygenation and ventilator-free days without more organ failure? [DocT GT]", "Conservative fluid strategy after shock resolves."),
    ("[pattern] FACTT outcome", "More ventilator-free days; no mortality difference."),
  ],
  punch="FACTT: once shock has resolved, a conservative fluid strategy (balance about zero vs +7 L) gives more ventilator-free days without more renal failure, but no significant fall in mortality; the PA catheter adds only complications.",
)

L['ARDS-40'] = dict(
  sub="Respiratory → ARDS → Corticosteroids",
  step=4,
  intro="Steroids aim at the inflammation and the fibroproliferation that follows. The trials say that timing decides everything: started early they may help, started late they harm.",
  parts=[
    ('a', "**Early low-dose methylprednisolone: ICU mortality 21% vs 43%.** Meduri’s trial (2007) gave methylprednisolone 1 mg/kg/day within 72 h of onset; it was small (91 patients), so it was suggestive, not decisive."),
    ('b', "**180 patients, persistent ARDS (day 7–28), methylprednisolone: no difference in 60- or 180-day mortality; more neuromyopathy.** LaSRS (ARDS Network) did improve oxygenation, compliance and blood pressure, and gave more ventilator-free and shock-free days at day 28 — but some patients needed re-intubation, and survival did not improve."),
    ('c', "**Dexamethasone 20 mg for 5 days then 10 mg for 5 days: 60-day mortality 15.3% lower, more ventilator-free days.** DEXA-ARDS (2020) enrolled moderate-to-severe ARDS (P/F ≤200 on PEEP ≥10); mortality was about 21% vs 36%. It was stopped early for slow recruitment and was not blinded."),
    ('d', "**Dexamethasone 6 mg in COVID-19 needing oxygen: lower mortality.** RECOVERY: the largest benefit was in ventilated patients, and none in patients not on oxygen (RESP01A, ARDS-12)."),
    ('e', "**Do not start 14 or more days after onset: LaSRS 60-day mortality 35% vs 8%; 180-day 44% vs 12%.** In the LaSRS subgroup started on day 14 or later, mortality was higher with steroids. The 2024 ATS update and the 2024 SCCM guideline now conditionally recommend corticosteroids in ARDS, on the evidence of trials that started them early."),
  ],
  table=dict(title="Steroid trials by timing", head=["Trial", "When", "Result"], rows=[["Meduri 2007", "≤72 h", "ICU mortality 21% vs 43%"], ["DEXA-ARDS", "early, P/F ≤200", "mortality about 15% lower, more VFDs"], ["RECOVERY", "COVID on oxygen", "mortality lower"], ["LaSRS", "day 7–28", "no survival gain; **harm if started ≥14 days**"]]),
  mimic=[
    ("Better physiology vs better survival", "LaSRS improved oxygenation, compliance and shock-free days without saving lives — the questions test which outcome changed."),
  ],
  traps=[
    ("“Late steroids (more than 2 weeks after onset) are beneficial”", "They increased mortality in LaSRS."),
    ("“LaSRS: increased long-term survival”, “reduced weakness” or “no change in oxygenation” (only 59% chose more ventilator- and shock-free days)", "LaSRS improved oxygenation and gave more ventilator- and shock-free days, with no survival benefit and more neuromuscular weakness."),
    ("“Corticosteroids should be started immediately” or “are contraindicated in all ARDS” (69% chose the keyed answer)", "The keyed truth is that they improve oxygenation and respiratory compliance in early ARDS."),
    ("“Hypoglycaemia” or “hyperkalaemia” as the steroid side effect to watch (only 60% chose myopathy)", "Steroids cause hyperglycaemia and hypokalaemia, and lower the lymphocyte count; myopathy is the keyed side effect, and LaSRS showed more neuromyopathy."),
  ],
  decode=[
    ("Persistent ARDS for 8 days, methylprednisolone — outcome consistent with the ARDS Network trial? [DocT GT]", "More ventilator- and shock-free days."),
    ("Which statement about steroids in ARDS is true? [DocT]", "They improve oxygenation and respiratory compliance in early ARDS."),
    ("ICU patient on hydrocortisone — side effect to monitor? [DocT]", "Myopathy."),
  ],
  punch="Steroids help early — Meduri, DEXA-ARDS, RECOVERY — and harm late: started 14 or more days after onset, LaSRS mortality was 35% vs 8% at 60 days.",
)

L['ARDS-41'] = dict(
  sub="Respiratory → ARDS → Nutrition (EDEN, OMEGA)",
  step=4,
  intro="Feeding was tested in two ARDS Network trials: how much to give early, and whether anti-inflammatory supplements help. Both answers were no difference or worse.",
  parts=[
    ('a', "**Trophic vs full enteral feeding for the first 6 days: no difference in ventilator-free days or mortality; less gastrointestinal intolerance with trophic feeds.** EDEN (about 1000 patients) gave trophic feeds at a low rate; patients did as well, with less vomiting and fewer high gastric residuals."),
    ('b', "**No benefit; stopped for futility with a signal of harm.** OMEGA gave omega-3 fatty acids, γ-linolenic acid and antioxidants twice daily; it was stopped early, with fewer ventilator-free days and more diarrhoea in the supplement arm."),
  ],
  mimic=[
    ("Trophic vs full feeding", "Same outcomes; trophic is better tolerated."),
  ],
  traps=[
    ("“Omega-3 supplements improve ARDS outcomes”", "OMEGA was stopped for futility with a signal of harm."),
  ],
  decode=[
    ("[pattern] EDEN trial result", "Trophic feeding for 6 days: same ventilator-free days and mortality, less GI intolerance."),
  ],
  punch="EDEN: trophic feeding for the first 6 days does as well as full feeding with less intolerance; OMEGA: anti-inflammatory supplements failed and may harm.",
)

L['ARDS-42'] = dict(
  sub="Respiratory → ARDS → Therapies that failed",
  step=4,
  intro="Almost every drug aimed at a single step in ARDS — surfactant, inflammation, oxidants, the epithelium — has failed in trials. The list is asked as ‘which is NOT effective’ or as an evidence grade.",
  parts=[
    ('a', "**Exogenous surfactant (adults).** Surfactant works in premature infants, who lack it; in adult ARDS the problem is injury and inactivation, and replacement did not help."),
    ('b', "**Beta-2 agonists: BALTI-2 (IV salbutamol, harm), ALTA (inhaled).** They speed alveolar fluid clearance in the laboratory; IV salbutamol increased mortality in BALTI-2 and inhaled albuterol was futile in ALTA."),
    ('c', "**Statins: SAILS, HARP-2.** Rosuvastatin (SAILS) and simvastatin (HARP-2) did not improve outcomes."),
    ('d', "**Ketoconazole, lisofylline, ibuprofen, IV prostaglandin E1; N-acetylcysteine, procysteine, glutamine and other antioxidants; neutrophil elastase inhibitor, activated protein C; keratinocyte growth factor (harm).** All anti-inflammatory, antioxidant or repair strategies with no survival benefit."),
    ('e', "**Aspirin for prevention (LIPS-A); inhaled nitric oxide and HFOV (no survival benefit).** LIPS-A gave aspirin to at-risk patients and did not prevent ARDS; iNO (ARDS-37) and HFOV (ARDS-34) failed for survival."),
  ],
  mimic=[
    ("Failed drugs vs steroids", "Steroids are not on this list: early steroids are now conditionally recommended (ARDS-40)."),
  ],
  traps=[
    ("“Recruitment manoeuvres are a grade B recommendation”", "In the Harrison table Marrow uses, they are grade C. Low tidal volume is A; conservative fluids, higher PEEP, prone and ECMO are B; NMB and iNO are C; HFOV and surfactant are D. That table also grades steroids D, which is dated (ARDS-40)."),
    ("“Inhaled β-agonists speed recovery”", "ALTA (inhaled) was futile and BALTI-2 (IV) harmful."),
  ],
  decode=[
    ("ARDS therapies: which is NOT a class B recommendation? [Marrow]", "Recruitment manoeuvres (grade C)."),
    ("[pattern] Which therapy is ineffective in ARDS?", "Surfactant, β-agonists, statins, antioxidants, iNO — pick from the list."),
  ],
  punch="Surfactant, β-agonists, statins, antioxidants, aspirin, iNO and HFOV all failed; what reduces mortality is ventilation — low tidal volume and prone — with early steroids the one drug now gaining support.",
)

L['ARDS-43'] = dict(
  sub="Respiratory → ARDS → Complications and causes of death",
  step=5,
  intro="The story now moves from treatment to outcome. Patients with ARDS are ventilated for long periods, so the complications are those of prolonged critical illness, and what kills them is rarely the hypoxaemia itself.",
  parts=[
    ('a', "**About 60%.** Prolonged ventilation, an injured lung and sedation make VAP common; published series range from about 15% to 60% (most between a third and a half), so 60% is the upper end."),
    ('b', "**About 25% (hypoxic vasoconstriction, microthrombi, high airway pressures).** Each raises pulmonary vascular resistance and loads the right ventricle; echo shows a dilated RV with septal flattening. Prone and limiting plateau pressure and PaCO₂ unload it (ARDS-31c)."),
    ('c', "**Multi-organ dysfunction / sepsis, not refractory hypoxaemia.** Only a minority die of hypoxaemia; most die of the sepsis, shock and organ failure that caused or followed the ARDS."),
    ('d', "**Barotrauma, ICU-acquired weakness, delirium, DVT, stress-ulcer bleeding.** These are the complications of a long ICU stay, and weakness and delirium lead into the long-term outcome (ARDS-44)."),
  ],
  mimic=[
    ("Dying with ARDS vs of hypoxaemia", "Patients die with ARDS, of multi-organ failure, more often than of hypoxaemia."),
  ],
  traps=[
    ("“Refractory hypoxaemia is the commonest cause of death”", "Multi-organ failure and sepsis are (ARDS-46f)."),
  ],
  decode=[
    ("[pattern] Commonest cause of death in ARDS", "Multi-organ dysfunction / sepsis."),
  ],
  punch="ARDS brings VAP, acute cor pulmonale in about a quarter and the complications of a long ICU stay, and most patients die of multi-organ failure and sepsis, not of hypoxaemia.",
)

L['ARDS-44'] = dict(
  sub="Respiratory → ARDS → Long-term outcome (Herridge)",
  step=5,
  intro="For survivors, the question is what is left after discharge. Herridge’s Toronto cohort followed them for five years and found the lungs largely recovered while the person did not.",
  parts=[
    ('a', "**109 survivors, followed for 5 years.** Relatively young adults (median age in the mid-40s), so the lasting disability is largely attributable to the critical illness itself rather than to old age."),
    ('b', "**Median 436 m, 76% of predicted.** Exercise capacity improved over the first years but never returned to normal."),
    ('c', "**Lung volumes and spirometry return to near normal (diffusing capacity mildly low). Persisting: muscle weakness and exercise limitation, cognitive and psychological problems (depression, PTSD), reduced quality of life.** The limit on walking is muscle wasting and weakness from the ICU stay, not the lung."),
  ],
  mimic=[
    ("Pulmonary vs extrapulmonary sequelae", "Lung function near normal; muscle, cognition and mood remain impaired."),
  ],
  traps=[
    ("“ARDS survivors are limited by pulmonary fibrosis”", "The lasting disability is neuromuscular and neuropsychological."),
  ],
  decode=[
    ("[pattern] Main cause of long-term disability after ARDS", "Muscle weakness and neuropsychological problems, not lung function."),
  ],
  punch="Five years after ARDS, the lungs are near normal but walking distance is 76% of predicted, because muscle weakness, cognitive and psychological problems persist.",
)

L['ARDS-45'] = dict(
  sub="Respiratory → ARDS → Trials at a glance",
  step=6,
  intro="The deck’s trials in one table. The questions give the trial name and ask what was compared, or give the intervention and ask which trial or what verdict.",
  parts=[
    ('a', "**ARMA: 6 vs 12 mL/kg — mortality ↓.** 6 mL/kg predicted body weight with plateau ≤30 vs 12 mL/kg; mortality 31% vs 40%. This is the therapy best shown to improve survival."),
    ('b', "**PROSEVA: prone ≥16 h — mortality ↓.** 16.0% vs 32.8% at 28 days (ARDS-30)."),
    ('c', "**ACURASYS: cisatracurium 48 h — benefit. ROSE: cisatracurium 48 h — no difference.** The difference lies in the control arms (ARDS-38)."),
    ('d', "**FACTT: conservative fluids — more ventilator-free days only.** No significant mortality difference (ARDS-39)."),
    ('e', "**OSCILLATE: HFOV — mortality ↑. ART: recruitment + high PEEP — mortality ↑.** Both opened the lung with high pressure (ARDS-33, 34)."),
    ('f', "**EOLIA: early VV-ECMO — not significant.** 35% vs 46%, P = 0.09 (ARDS-36)."),
  ],
  mimic=[
    ("Predicted vs actual body weight", "ARMA used predicted (ideal) body weight, calculated from height and sex — not actual weight."),
  ],
  traps=[
    ("“Diuresis, inhaled vasodilator or recruitment with PEEP titration is best shown to improve survival”", "Low tidal volume (6 mL/kg IBW) is; FACTT improved ventilator-free days only, iNO oxygenation only, and ART showed harm."),
    ("“ARMA compared 6 vs 8 mL/kg actual body weight”", "6 vs 12 mL/kg predicted body weight."),
  ],
  decode=[
    ("Influenza ARDS on VT 500 mL, FiO₂ 1.0, PEEP 5 — which therapy is best shown to improve survival? [DocT GT]", "Tidal volume 6 mL/kg ideal body weight."),
    ("ARMA compared which tidal volumes? [DocT GT]", "6 vs 12 mL/kg predicted body weight."),
  ],
  punch="Mortality fell with ARMA and PROSEVA, rose with OSCILLATE and ART, and did not change significantly with ROSE, FACTT or EOLIA; ACURASYS’s benefit was not reproduced.",
)

L['ARDS-46'] = dict(
  sub="Respiratory → ARDS → Revision: true or false",
  step=6,
  intro="A sweep through the deck. Each statement turns on one number or verdict from an earlier card.",
  parts=[
    ('a', "**False — PROSEVA enrolled P/F below 150** (ARDS-30)."),
    ('b', "**False — OSCAR showed no difference; OSCILLATE showed harm** (ARDS-34)."),
    ('c', "**False — EOLIA P = 0.09 (0.07 on the survival curve)** (ARDS-36)."),
    ('d', "**True — LaSRS: steroids started ≥14 days after onset, 60-day mortality 35% vs 8%** (ARDS-40)."),
    ('e', "**False — iNO improves oxygenation only, and transiently** (ARDS-37)."),
    ('f', "**False — multi-organ failure / sepsis is the commonest cause of death** (ARDS-43)."),
    ('g', "**False — ROSE found no difference** (ARDS-38)."),
  ],
  mimic=[],
  traps=[
    ("“P/F <200 for prone”", "<150 is the PROSEVA threshold; <200 is the moderate ARDS band."),
  ],
  decode=[
    ("[pattern] Statements about the rescue trials", "Only ARMA and PROSEVA cut mortality significantly; OSCILLATE and ART raised it."),
  ],
  punch="Most errors here come from mixing up the two HFOV trials, calling EOLIA significant, and forgetting that late steroids and routine paralysis did not help.",
)

FLAGS = {}
FLAGS['ARDS-30'] = "Card right. One DocT GT paper (AIM2 Q97) prints the keyed prone option as ‘≤16 hours/day’ — misprint for ≥16 h."
FLAGS['ARDS-32'] = "Card right. DocT GT (CGT4) has two true options: the keyed mechanism statement and ‘proning is contraindicated in spinal fractures’ (unstable spine is absolute on the card)."
FLAGS['ARDS-35'] = "Card right. DocT/DocT GT key ECMO for refractory ARDS when prone is also offered and untried — guidelines put prone first. DocT’s oxygenation trigger ‘P/F <100’ is the older ELSO threshold, not EOLIA’s <80 for 6 h. The polytrauma key note says pH 7.25 with PaCO₂ 68 meets EOLIA; strictly EOLIA needs pH <7.25 — the vignette qualifies on P/F 67 for 6 h instead."
FLAGS['ARDS-42'] = "WATCH ‘No drug has consistently reduced mortality’: defensible for non-COVID ARDS, but dexamethasone reduced mortality in COVID-19 (RECOVERY) and in DEXA-ARDS, and early corticosteroids are now conditionally recommended (ATS 2024, SCCM 2024). The Marrow/Harrison grade table rating steroids D is dated."
FLAGS['ARDS-43'] = "‘VAP about 60%’ is the upper end of published series (about 15–60%, most a third to a half: Chastre 1998 55%, Meduri 1998 43%, Markowicz 2000 36%); kept as the card’s number with that caveat."
