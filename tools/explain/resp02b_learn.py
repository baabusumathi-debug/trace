# RESP02B — Explain v3 ("Learn" depth): COPD and asthma continued — Invasive Ventilation, Auto-PEEP, Drugs, Support, Weaning & Outcome. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP02B.md (33 questions; COPD-22 and COPD-28 asked 7 times each). Fields as TOX01, plus SPINE, PRIMER and step.
# Continues the story of RESP02A (COPD-01 to COPD-14), which ended with intubation when NIV fails (COPD-12).

SPINE = [
  ("Ventilating the obstructed lung", "Once intubated, the obstructed lung is ventilated for expiratory time — small breaths, a slow rate, fast inspiration — accepting a high PaCO₂ while the pH stays above about 7.2."),
  ("Seeing and measuring trapped air", "Expiratory flow that does not reach zero shows that air is trapped; an end-expiratory hold measures intrinsic PEEP, and the trapped volume (Vei) is the validated marker of danger."),
  ("Undoing auto-PEEP", "Lowering minute ventilation is what empties the lung; external PEEP below intrinsic PEEP does not empty it but makes triggering easier for a patient who breathes for himself."),
  ("Drugs for the attack", "Inhaled salbutamol with ipratropium and a systemic steroid treat both diseases; IV magnesium is the add-on for severe asthma that has not responded, and antibiotics belong to COPD with purulent sputum."),
  ("Supporting the ventilated patient", "Hypercapnic acidosis dilates cerebral vessels and constricts pulmonary ones, and over-correcting it, overfeeding or overloading with fluid makes weaning harder."),
  ("Weaning, extubation and outcome", "A COPD patient who passes a spontaneous breathing trial is extubated to NIV; prognosis after ventilation for COPD is poor, worse than for asthma."),
]

PRIMER = "On a volume-controlled breath the peak airway pressure is the pressure needed to push flow through the airways plus the pressure needed to stretch the lung, while the plateau pressure, read during a short end-inspiratory hold when flow is zero, reflects the stretch alone; so a peak that rises with an unchanged plateau means more resistance, and both rising means a stiffer or fuller chest. An end-expiratory hold closes the valves at the end of expiration so that the pressure in the alveoli shows on the airway gauge; any pressure above the set PEEP is intrinsic PEEP (COPD-03). Minute ventilation is tidal volume times rate, and in an obstructed lung it decides how much air is trapped (COPD-02). Permissive hypercapnia means deliberately accepting a high PaCO₂ to avoid the trapping and barotrauma that normal ventilation would cause."

L = {}

L['COPD-15'] = dict(
  sub="Respiratory → Invasive ventilation → Settings in obstructive disease",
  step=1,
  intro="When NIV fails (COPD-12), the tube goes in and the ventilator must be set for the problem that put him there: a lung that cannot empty. Every setting on this card buys expiratory time. The one real question tests what happens to the pressures once those settings are in place.",
  parts=[
    ('a', "**Tidal volume <8 mL/kg; rate 10–14/min; minute ventilation <115 mL/kg/min (about 8 L/min at 70 kg).** Trapping depends mainly on minute ventilation (COPD-20): the more volume delivered per minute, the less time each breath has to leave. A small, slow minute ventilation leaves the PaCO₂ high, and that is accepted (COPD-16)."),
    ('b', "**80–100 L/min, square waveform: shortens inspiration, lengthens expiration.** A constant (square) high flow delivers the breath in the shortest time, so more of each cycle is left for expiration. The price is a higher peak pressure, which is mostly spent on airway resistance and does not reach the alveoli."),
    ('c', "**1:3 to 1:5.** At a rate of 12 each cycle lasts 5 seconds; I:E 1:4 gives 1 second in and 4 seconds out."),
    ('d', "**<30 cmH₂O.** Plateau pressure is the alveolar pressure at end-inspiration, so it reflects how far the lung is inflated, including the trapped air. It, not the peak, is the pressure that predicts barotrauma and hypotension."),
  ],
  table=dict(title="Reading peak and plateau in a ventilated obstructed patient", head=["Peak", "Plateau", "Meaning", "Action"], rows=[["**↑**", "**unchanged**", "**more airway resistance: plug, kink, biting, bronchospasm**", "**suction, check the tube, bronchodilator**"], ["↑", "↑", "lung fuller or stiffer: more trapping, pneumothorax, atelectasis, compliance loss", "disconnect briefly, examine and image, lower minute ventilation"], ["high, steady", "<30", "the expected cost of high inspiratory flow", "accept"]]),
  mimic=[
    ("Rising resistance vs rising trapping", "Resistance raises only the peak; trapping or a pneumothorax raise the plateau as well."),
  ],
  traps=[
    ("“A peak pressure of 58 means the patient is being harmed: lower the flow”", "Peak pressure largely reflects the tubes and airways. With a plateau of 26 the alveoli are safe; the widened peak–plateau gap points to a plug or a kinked tube, and lowering the flow would only lengthen inspiration and worsen trapping."),
  ],
  decode=[
    ("Ventilated COPD, peak 58, plateau 26, good air entry — cause and step? [Marrow]", "Raised airway resistance (mucus plug, kink): suction and check the airway."),
  ],
  punch="Ventilate the obstructed lung for expiratory time — VT <8 mL/kg, rate 10–14, flow 80–100 L/min, I:E 1:3–1:5 — and judge safety by the plateau (<30), not the peak.",
)

L['COPD-16'] = dict(
  sub="Respiratory → Invasive ventilation → Goals: oxygen, pH and PaCO₂",
  step=1,
  intro="The settings in COPD-15 leave the PaCO₂ high, so this card sets the goals that make that acceptable. The four questions all test the same idea from different sides: the target is a safe pH and the patient’s own baseline PaCO₂, never a normal PaCO₂.",
  parts=[
    ('a', "**PaO₂ >60 mmHg (8 kPa).** That puts the patient near the shoulder of the oxygen dissociation curve, with saturation about 90%. More oxygen gains little content and, in COPD, can worsen V/Q matching (COPD-11b)."),
    ('b', "**Life-threatening respiratory acidaemia, pH <7.2.** Above about 7.2 the acidosis is well tolerated, and chasing it with more ventilation only adds trapping. Below 7.15–7.2 the risks — arrhythmia, depressed contractility, vasodilatation, raised ICP — start to matter, so the acidaemia is what is corrected, not the PaCO₂. If the PaCO₂ rises, let it rise slowly: intracellular and renal buffering then keep the pH up."),
    ('c', "**Target pH, not PaCO₂: accept a high PaCO₂ while pH is acceptable (permissive hypercapnia); never ventilate down to a normal PaCO₂.** A chronic retainer’s kidneys have raised his bicarbonate to match a high PaCO₂. Ventilating him to 40 mmHg leaves that bicarbonate unopposed, causing alkalosis, and over days the kidneys excrete it; when he breathes on his own again he cannot sustain the minute ventilation needed for a normal PaCO₂, and weaning fails. So the definitive goal is his own baseline PaCO₂, which gives his usual pH — not normocapnia, and not a textbook pH of 7.35–7.45 forced by over-ventilation."),
    ('d', "**Large-diameter tube (less resistance); titrated sedation; avoid paralysis (myopathy, worse with steroids). Switch to assisted modes early.** Resistance in a tube rises steeply as its radius falls, and a wide tube also allows bronchoscopy and suction. Neuromuscular blockers combined with high-dose steroids, as in acute asthma, cause an acute myopathy that prolongs ventilation. Assisted modes keep the diaphragm working, but only once the patient is ready: a stable circulation, an adequate drive, and no major acidaemia. At pH 7.15 he stays on a controlled mode, because a patient breathing for himself would raise his minute ventilation and his trapping."),
  ],
  mimic=[
    ("Permissive hypercapnia vs over-ventilation", "Permissive: high PaCO₂, pH ≥7.2, little trapping. Over-ventilation: normal PaCO₂, alkalosis, more trapping, and bicarbonate lost before weaning."),
  ],
  traps=[
    ("“Intubated asthmatic, pH 7.24, PaCO₂ 72 on RR 7: raise the rate to 20 or aim for PaCO₂ <35”", "A pH of 7.24 is acceptable. A faster rate or a shorter expiratory time worsens trapping; accept the hypercapnia."),
    ("“The chronic retainer’s goal is a normal pH of 7.35–7.45 or a normal PaCO₂”", "The goal is his baseline PaCO₂; normocapnia washes out his bicarbonate and makes him fail weaning."),
    ("“Permissive hypercapnia: let the PaCO₂ jump, or accept SaO₂ 75% to limit oxygen toxicity”", "The rise should be gradual, so buffering keeps up; and hypoxaemia is never permitted — SpO₂ stays about 88–95%. Raised ICP is the main contraindication to permissive hypercapnia."),
  ],
  decode=[
    ("Lung-protective ventilation, PaCO₂ 76 in the first hour — next step? [DocT GT]", "Keep the settings and let the PaCO₂ continue to rise gradually."),
    ("Intubated life-threatening asthma, VT 7 mL/kg, RR 7, flow 90, pH 7.24, PaCO₂ 72 — strategy? [DocT GT]", "Accept the current hypercapnia."),
    ("Ventilated asthmatic — which finding bars a switch to pressure support? [Marrow]", "pH 7.15: significant acidaemia keeps him on a controlled mode."),
    ("Intubated chronic retainer — definitive ventilation goal? [Marrow]", "Return to his baseline PaCO₂."),
  ],
  punch="Ventilate for a safe pH (above about 7.2) and the patient’s own baseline PaCO₂, with PaO₂ above 60; ventilating a chronic retainer to a normal PaCO₂ dumps his bicarbonate and makes weaning fail.",
)

L['COPD-17'] = dict(
  sub="Respiratory → Auto-PEEP → The flow–time curve",
  step=2,
  intro="Trapped air cannot be seen, but its effect on the flow trace can. In expiration the flow trace falls back towards zero as the lung empties; if the next breath arrives before it gets there, air is left behind. The three questions show this trace and ask what it means.",
  parts=[
    ('a', "**B: expiratory flow has not returned to zero before the next breath.** Zero expiratory flow means the alveoli have reached the circuit pressure and stopped emptying. Flow that is still going when inspiration starts means alveolar pressure is still above the set PEEP."),
    ('b', "**Alveoli have not emptied; gas is trapped (auto-PEEP is present).** At that point the expiratory flow is cut off by the next breath, so the alveoli begin the new breath at a higher volume and pressure. On a pressure-targeted mode this lowers the tidal volume: the ventilator delivers a fixed pressure above PEEP, and intrinsic PEEP takes part of that driving pressure, so a falling tidal volume at the same settings is a clue to trapping."),
    ('c', "**Its amount: that needs an end-expiratory hold.** The trace shows only that air is trapped. How much intrinsic PEEP there is is measured by a hold in a passive patient (COPD-18)."),
  ],
  mimic=[
    ("Trapping vs a circuit leak", "Trapping: expiratory flow does not reach zero. A leak: the expired volume is smaller than the inspired volume, and the volume trace does not return to baseline."),
  ],
  traps=[
    ("“Tidal volume falls on pressure control because compliance has fallen” (88% right)", "With expiratory flow not reaching zero, intrinsic PEEP is eating into the set driving pressure; compliance need not have changed."),
    ("“Hypotension with a raised PAOP is left-ventricular failure”", "Trapped air raises intrathoracic pressure, cutting venous return and reading falsely high on the catheter (COPD-02, COPD-04)."),
  ],
  decode=[
    ("Severe COPD, flow persisting at end-expiration, occlusion shows 8 cmH₂O — explanation? [DocT QBank, 91% right]", "Intrinsic PEEP from dynamic hyperinflation."),
    ("Pressure-targeted COPD, expiratory flow not reaching baseline, tidal volume falling — explanation? [DocT GT]", "Development of intrinsic PEEP."),
    ("Ventilated COPD, hypotension, raised PAOP, flow persisting into the next breath — mechanism? [DocT GT]", "Dynamic hyperinflation."),
  ],
  punch="Expiratory flow that has not reached zero when the next breath starts means trapped air; the curve shows that it is there, and an end-expiratory hold shows how much.",
)

L['COPD-18'] = dict(
  sub="Respiratory → Auto-PEEP → Measuring PEEPi and trapped volume",
  step=2,
  intro="The flow trace in COPD-17 shows that air is trapped; this card measures it. Intrinsic PEEP is the pressure the trapped air exerts, and Vei is the volume of air above FRC. The question that only 13% answered right asks which of the two is the validated measure.",
  parts=[
    ('a', "**Total PEEP – applied PEEP.** Total PEEP is the pressure in the alveoli at the end of expiration; subtracting the set PEEP leaves the part produced by trapping. A hold showing 15 with PEEP 5 means intrinsic PEEP 10."),
    ('b', "**End-expiratory hold in a passive patient: alveolar and airway pressures equilibrate.** Closing both valves at end-expiration stops flow, so the pressure in the alveoli spreads back to the airway gauge. The patient must be passive, because any effort or active expiration changes the reading."),
    ('c', "**End-inspiratory volume above FRC: the gas exhaled during a prolonged apnoea from end-inspiration until the lungs reach FRC.** Ventilation is stopped at end-inspiration and the patient (sedated and paralysed) is allowed to breathe out during an apnoea of 20–60 seconds; the total volume collected is Vei. It is the tidal volume plus the trapped volume, so it measures hyperinflation directly."),
    ('d', "**>20 mL/kg.** In Tuxen’s series of ventilated severe asthmatics (1992), complications, chiefly hypotension and barotrauma, occurred in about two-thirds of patients with a Vei of 1.4 L or more (about 20 mL/kg at 70 kg) and in none below it. Plateau pressure and intrinsic PEEP are easier surrogates, but they can underestimate trapping: units that are closed off at end-expiration do not communicate with the airway during a hold."),
  ],
  mimic=[
    ("End-expiratory vs end-inspiratory hold", "End-expiratory hold: intrinsic PEEP. End-inspiratory hold: plateau pressure."),
  ],
  traps=[
    ("“The most reliable validated method is plateau pressure or auto-PEEP on a hold” (only 13% right)", "Those are surrogates; Vei, the volume exhaled during a long apnoea, is the measure validated against complications. The keyed option calls it ‘from TLC to FRC’; strictly it is from end-inspiration to FRC."),
    ("“A rise to 8 cmH₂O on occlusion means the applied PEEP is too high or there is a cuff leak”", "With expiratory flow still running at end-expiration, the extra pressure is intrinsic PEEP from trapping."),
  ],
  decode=[
    ("Severe COPD, expiratory flow persisting, end-expiratory occlusion rises to 8 cmH₂O — explanation? [DocT QBank, 91% right]", "Intrinsic PEEP from dynamic hyperinflation."),
    ("Suspected dynamic hyperinflation — most reliable validated method to assess lung inflation? [DocT GT]", "Measuring the volume exhaled during apnoea down to FRC (Vei)."),
  ],
  punch="Intrinsic PEEP is total minus set PEEP on an end-expiratory hold; Vei, the volume exhaled in a long apnoea, is the validated measure, and above 20 mL/kg complications rise.",
)

L['COPD-19'] = dict(
  sub="Respiratory → Auto-PEEP → Static versus dynamic",
  step=2,
  intro="The hold in COPD-18 needs a passive patient; a patient who breathes for himself needs a different measurement. Because the lung’s units empty at different speeds, the two methods give different numbers.",
  parts=[
    ('a', "**Static: end-expiratory hold in a passive patient. Dynamic: the fall in oesophageal pressure from the start of effort until inspiratory flow begins, in a spontaneously breathing patient.** The oesophageal pressure tracks pleural pressure, so its fall before flow starts is the effort spent overcoming trapped pressure."),
    ('b', "**Dynamic is lower: flow begins as soon as the units with the shortest time constants (lowest auto-PEEP) are overcome.** The static hold lets all units equalise and reads their average; dynamic measurement stops at the first flow, which comes from the fastest-emptying units."),
    ('c', "**Fall in Poes = trigger pressure + intrinsic PEEP, so PEEPi = fall in Poes – trigger pressure.** The effort must first cancel the intrinsic PEEP and then reach the ventilator’s trigger before flow is delivered."),
  ],
  mimic=[
    ("Static vs dynamic PEEPi", "Static: passive, average of all units, higher. Dynamic: active, fastest units, lower."),
  ],
  traps=[
    ("“Dynamic auto-PEEP is higher than static” (COPD-29b)", "It is lower, because it reflects only the units that empty fastest."),
  ],
  decode=[
    ("[pattern] Spontaneously breathing COPD patient: how is auto-PEEP measured, and why is it lower than on a hold?", "Oesophageal pressure fall before inspiratory flow; it reflects the fastest-emptying units."),
  ],
  punch="Static intrinsic PEEP comes from a hold in a passive patient and averages every unit; dynamic comes from oesophageal pressure in a breathing patient and is lower, because flow starts as soon as the fastest units are overcome.",
)

L['COPD-20'] = dict(
  sub="Respiratory → Auto-PEEP → Reducing it",
  step=3,
  intro="Once trapping is seen (COPD-17) and measured (COPD-18), it has to be reduced. All the measures aim at the same thing: more time to empty and less volume to empty. The two questions test the first move when the blood pressure falls and the cause of failed triggering.",
  parts=[
    ('a', "**Longest possible expiratory phase: lower rate, lower tidal volume, higher inspiratory flow, I:E 1:3 to 1:5.** A lower rate lengthens every expiration; a smaller tidal volume leaves less to empty; a faster inspiratory flow shortens inspiration. When trapping has already dropped the blood pressure, the quickest test and treatment is to disconnect the ventilator for 30–60 seconds and let the chest empty (COPD-04)."),
    ('b', "**Reduce ventilatory demand (sedation, treat fever and pain); bronchodilators and steroids to lower resistance.** Fever, pain, agitation and acidosis drive the minute ventilation up; bronchodilators shorten the time constant by lowering resistance."),
    ('c', "**Lowering minute ventilation, mainly the rate (standard teaching, not in your notes).** Trapped volume rises with minute ventilation. At the same minute ventilation, raising the flow helps a little; lowering the minute ventilation, usually by the rate, helps most. A large tidal volume is also part of the minute ventilation: 700 mL is about 10 mL/kg of predicted body weight or more in most adults, and cutting it is the first change."),
  ],
  mimic=[
    ("Trapping vs tension pneumothorax with hypotension", "Disconnection restores the pressure in trapping; a pneumothorax needs decompression and is seen on the film. A clear chest X-ray points to trapping."),
  ],
  traps=[
    ("“Intrinsic PEEP 10, sudden hypotension, no pneumothorax on film: needle decompression or bronchoscopy” (64% right)", "Briefly disconnect the ventilator: the chest empties and the pressure recovers if trapping is the cause. Decompressing a chest without a pneumothorax causes one."),
    ("“Missed triggers from auto-PEEP: make the trigger more sensitive” (only 38% right)", "The patient must overcome the trapped pressure before any trigger can sense effort, so sensitivity gains almost nothing; reduce the auto-PEEP by lowering the tidal volume or rate."),
    ("“Lower the inspiratory flow”", "A slower flow lengthens inspiration and shortens expiration, worsening trapping."),
  ],
  decode=[
    ("Ventilated asthmatic, end-expiratory hold 15 on PEEP 5, then BP 75/55, film unchanged — next step? [DocT GT]", "Briefly disconnect the ventilator."),
    ("COPD on pressure control, VT 700, RR 14, ineffective efforts on the waveforms — next step? [DocT GT]", "Lower the tidal volume."),
  ],
  punch="Auto-PEEP is reduced by giving the lung less to empty and more time to do it, and lowering minute ventilation does most; if it has already dropped the pressure, disconnect first.",
)

L['COPD-21'] = dict(
  sub="Respiratory → Auto-PEEP → External PEEP",
  step=3,
  intro="Lowering minute ventilation (COPD-20) is the treatment in a passive patient. A patient who is triggering his own breaths has another problem: he must overcome intrinsic PEEP before every breath (COPD-03). External PEEP set below intrinsic PEEP reduces that load without adding air, and the three questions test why.",
  parts=[
    ('a', "**It lowers the negative pressure the patient must generate to trigger.** The trigger senses a fall below the circuit pressure. Raising the circuit pressure towards the alveolar pressure narrows the gap the patient must pull through before the ventilator responds."),
    ('b', "**With flow limitation, downstream pressure (external PEEP) does not affect upstream flow until it exceeds the critical closing pressure.** In COPD the small airways collapse during expiration, and flow is set at that narrowed point, as water over a weir is unaffected by the level downstream. Pursed-lip breathing works the same way: it raises the downstream pressure and splints the airways. So external PEEP below the closing pressure leaves the lung’s emptying unchanged."),
    ('c', "**80% of intrinsic PEEP: large relief of trigger load without adding hyperinflation.** The closing pressure is not known exactly, so a margin is kept below the measured intrinsic PEEP. Above it, external PEEP adds directly to lung volume."),
    ('d', "**Effort needed falls from more than 8 to more than 2 cmH₂O (your notes’ figure; 80% of 8 is strictly 6.4).** With PEEPi 8 and external PEEP 6, the circuit sits at 6, so the patient pulls alveolar pressure down only 2 cmH₂O before the trigger can sense him."),
  ],
  mimic=[
    ("External PEEP in a spontaneously breathing vs a passive patient", "Breathing patient: it lowers trigger load. Passive patient: it does not help triggering, and if it exceeds the closing pressure it adds to trapping."),
  ],
  traps=[
    ("“Switching from pressure to flow triggering fixes ineffective efforts” (DocT key; 68% chose it)", "Flow triggering saves only about 1 cmH₂O; the barrier is intrinsic PEEP. The key is debatable: reducing intrinsic PEEP (higher inspiratory flow, option D) or offsetting it with external PEEP treats the cause. Setting PEEP to 0 makes triggering worse."),
    ("“External PEEP lengthens expiratory time or increases the alveolar–circuit gradient”", "It does neither: it narrows the gradient, lowering the threshold load."),
    ("“External PEEP increases elastic recoil or removes airway resistance”", "It changes neither; it splints flow-limited airways, as pursed-lip breathing does."),
  ],
  decode=[
    ("COPD with ineffective efforts, abrupt expiratory flow changes — what improves synchrony? [DocT QBank]", "Keyed: switch to flow triggering; better on physiology: reduce or offset intrinsic PEEP."),
    ("AECOPD on BiPAP failing to trigger — how does external PEEP reduce work of breathing? [DocT GT]", "It reduces the threshold load from PEEPi."),
    ("Ventilated COPD with auto-PEEP given PEEP 5 — principal rationale? [DocT GT]", "It mimics pursed-lip breathing (the waterfall effect)."),
  ],
  punch="In flow-limited COPD, external PEEP set at about 80% of intrinsic PEEP does not change emptying but cuts the pressure the patient must pull before each breath; above intrinsic PEEP it adds trapping.",
)

L['COPD-22'] = dict(
  sub="Respiratory → Drugs → Acute asthma doses",
  step=4,
  intro="The ventilator buys time; drugs open the airways. This card is asked seven times, and the questions are about order: what goes first, what is added in the first hour, and what is given only when that fails. The answers follow the speed of action of each drug.",
  parts=[
    ('a', "**Salbutamol 2.5 mg (continuous for an hour, then reassess); ipratropium 0.5 mg every 4–6 h in the same nebuliser.** Salbutamol acts within minutes and is the treatment every option must contain. Doses vary by source: 2.5–5 mg nebulised every 20 min in the first hour (GINA/NAEPP); BTS/SIGN uses 5 mg oxygen-driven, repeated every 15–30 min, or continuous nebulisation at 5–10 mg per hour when the response is poor. Ipratropium added to salbutamol in the first hour, usually with each of the first three doses, reduces admissions in severe attacks; after that it is given 4–6-hourly. High-dose salbutamol drives potassium into cells (β2 stimulation of the Na⁺/K⁺-ATPase), causing hypokalaemia with weakness, flat T waves, U waves and a long QT; check and replace potassium."),
    ('b', "**Methylprednisolone 40 mg IV, hydrocortisone 200 mg IV, or prednisolone 40 mg oral.** The acute steroid is systemic: prednisolone 40–50 mg daily for 5–7 days (GINA; BTS/SIGN at least 5 days) is as effective as IV when the patient can swallow. BTS/SIGN gives hydrocortisone as 100 mg IV 6-hourly when oral is not possible; the 200 mg figure is a single-dose variant used in some texts. It is given within the first hour, but it takes 4–6 hours to act, so it treats the inflammation and prevents relapse rather than relieving the first hour. Inhaled steroid is not the acute steroid."),
    ('c', "**Single IV infusion of 2 g over 20 min: reduces hospital admission.** Magnesium relaxes airway smooth muscle by blocking calcium entry into the cell, and it reduces acetylcholine release. It is for a severe attack that has not responded to initial bronchodilators (GINA; BTS 1.2–2 g), not for every exacerbation."),
    ('d', "**Adrenaline 0.3–0.4 mL of 1:1000 SC every 20 min for 3 doses. Terbutaline 0.25 mg SC every 20 min for 3 doses (preferred in pregnancy).** These are for a patient who cannot take nebulised drugs or has anaphylaxis; they are not the evidence-based add-on to nebulised salbutamol."),
    ('e', "**Not first line: poor response, serious adverse effects.** Aminophylline adds little to inhaled β-agonists and has a narrow therapeutic range, with arrhythmias, seizures and vomiting; GINA advises against it. IV montelukast (the watch) has weak evidence and no guideline place."),
  ],
  table=dict(title="Order of treatment in severe acute asthma", head=["When", "Give", "Why then"], rows=[["At once", "**salbutamol** nebulised, repeated or continuous; oxygen to SpO₂ 93–95%", "acts in minutes"], ["First hour", "**+ ipratropium 0.5 mg** with the first doses; **systemic steroid**", "ipratropium adds bronchodilation; steroid takes 4–6 h"], ["Not responding to the above", "**IV magnesium 2 g over 20 min**", "fewer admissions in severe attacks"], ["Cannot nebulise, or anaphylaxis", "adrenaline or terbutaline SC", "terbutaline in pregnancy"], ["Not routinely", "aminophylline, heliox, IV montelukast", "little benefit, real harm"]]),
  mimic=[
    ("Ipratropium vs magnesium as the add-on", "Ipratropium is added in the first hour to every severe attack. Magnesium is given when the attack is still severe after the first bronchodilators."),
  ],
  traps=[
    ("“Still distressed after inhaled bronchodilators, PaCO₂ 32: give a second salbutamol nebule or oral steroid, or intubate” (only 38% right)", "Failure of initial bronchodilators is the indication for IV magnesium. A low PaCO₂ with a normal pH does not call for intubation, and a steroid, although it should be given, will not act for hours."),
    ("“Magnesium 2 g IV upfront, or IV methylprednisolone, as the first-hour add-on” (53% right)", "Ipratropium with salbutamol has the best evidence in the first hour; magnesium is for non-responders and steroids are slow."),
    ("“Systemic steroid alone” (86% right) or “oxygen 6 L/min” (63% right)", "Neither opens the airways; the right option is the one that contains the inhaled β-agonist. The keyed ‘high-dose inhaled corticosteroid’ is the weak half of that option: the acute steroid is systemic."),
    ("“Magnesium is an M3 antagonist, an anti-inflammatory or a first-line agent”", "It blocks calcium influx into smooth muscle and is a second-line single dose."),
  ],
  decode=[
    ("Asthmatic, severe wheeze, cannot speak, PaO₂ 60, PaCO₂ 42 — best next step? [DocT QBank]", "High-dose inhaled β-agonist (with steroid), not oxygen alone, NIV or magnesium first. The PaCO₂ of 42 marks impending failure (COPD-08), so escalate fast."),
    ("Still distressed after inhaled bronchodilators — next step? [DocT QBank]", "IV magnesium sulphate."),
    ("Not improving on salbutamol, ipratropium and steroids — supported IV adjunct? [DocT GT]", "Magnesium sulphate 2 g IV, not aminophylline, montelukast or clonidine."),
    ("Status asthmaticus on salbutamol, weakness, long QT, flat T — cause? [Marrow]", "Hypokalaemia."),
  ],
  punch="In severe asthma give nebulised salbutamol at once, add ipratropium and a systemic steroid in the first hour, and give IV magnesium 2 g over 20 min only if the attack has not responded; aminophylline is not first line.",
)

L['COPD-23'] = dict(
  sub="Respiratory → Drugs → Asthma vs COPD: which therapy matters",
  step=4,
  intro="The same drugs treat both attacks, but not equally. This table grades them, and the one question — answered right by only 25% — asks which treatment helps most in a COPD exacerbation with type 2 failure.",
  parts=[
    ('a', "**Inhaled β-agonists: ++ in both.** Short-acting inhaled bronchodilators are the first treatment in either attack; oral bronchodilators are not used."),
    ('b', "**Inhaled anticholinergics: + asthma, ++ COPD.** In COPD, cholinergic tone is the main reversible part of the narrowing, so salbutamol with ipratropium is standard; in asthma ipratropium helps in the first hours of a severe attack (COPD-22)."),
    ('c', "**Systemic steroids: ++ asthma, + COPD.** In COPD they reduce treatment failure and shorten stay: prednisolone 40 mg for 5 days (REDUCE: as good as 14 days), and oral works as well as IV. Higher doses add hyperglycaemia without benefit."),
    ('d', "**Antibiotics: – asthma, + COPD.** Asthma attacks are mostly viral or allergic. In COPD they are given when sputum is purulent or the patient is ventilated (COPD-24)."),
    ('e', "**Oxygen: ++ asthma, + (cautious) COPD.** Asthma: to SpO₂ 93–95%. COPD: to 88–92%, because more raises PaCO₂ (COPD-11b)."),
    ('f', "**NIV: + asthma, ++ COPD.** Strong evidence in hypercapnic COPD (COPD-10), weak in asthma (COPD-13). CPAP is not NIV for this purpose: it does not add ventilation, so it does not lower PaCO₂."),
    ('g', "**Theophylline, mucokinetics: – in both.** Side effects outweigh a small gain, and mucolytics and chest physiotherapy do not shorten an exacerbation."),
  ],
  mimic=[
    ("Steroid course in asthma vs COPD", "Asthma: prednisolone 40–50 mg for 5–7 days. COPD: 40 mg for 5 days. IV is no better than oral in either."),
  ],
  traps=[
    ("“AECOPD with PaCO₂ 65: high-dose IV corticosteroids is the most beneficial treatment” (DocT key; 25% right)", "The key is the least wrong of four poor options. The first treatment is inhaled bronchodilator, which no option offers (oral bronchodilators are not used); the steroid is oral prednisolone 40 mg for 5 days, not high-dose IV. Antibiotics need purulent sputum or ventilatory support, and the stem states neither (a productive cough is not purulence), although they become indicated once he needs NIV; CPAP does not treat hypercapnia."),
  ],
  decode=[
    ("COPD, more dyspnoea and productive cough, PaO₂ 58, PaCO₂ 65 — most beneficial treatment? [DocT QBank]", "Keyed: high-dose IV corticosteroids; in practice inhaled SABA ± SAMA, oral prednisolone 40 mg × 5 days, controlled oxygen, NIV if pH <7.35."),
  ],
  punch="β-agonists help both attacks equally; anticholinergics, antibiotics and NIV matter more in COPD, steroids and oxygen more in asthma, and theophylline in neither.",
)

L['COPD-24'] = dict(
  sub="Respiratory → Drugs → Antibiotics in a COPD exacerbation",
  step=4,
  intro="Bacteria are found in about half of COPD exacerbations (COPD-06), so antibiotics are given by rule, not to everyone. The one question asks whether a patient with more dyspnoea and a productive cough needs them first.",
  parts=[
    ('a', "**At least 2 of the 3 cardinal symptoms (GOLD: all 3, or 2 if one is purulence), or any patient on ventilation (cover Gram-negatives).** The three are more dyspnoea, more sputum and purulent sputum. Purulence is the sign that best predicts a bacterial cause, which is why GOLD requires it when only two are present. Any patient needing NIV or invasive ventilation gets antibiotics, because untreated infection there carries a high mortality."),
    ('b', "**Any one of: age >65, FEV₁ <50%, 3 or more exacerbations a year, cardiac disease.** These patients more often have resistant or Gram-negative organisms and fail narrow-spectrum treatment, so they get broader cover."),
    ('c', "**4 or more antibiotic courses in the past year; Pseudomonas isolated in a previous admission; severe COPD (FEV₁ <50%).** The cut-off differs by source: the older GOLD table set it at very severe disease, FEV₁ <30%, while several current lists use <50%. The lists also add a recent admission (2 days or more in the past 90 days) and recent systemic steroids (GOLD: more than 10 mg prednisolone a day in the last 2 weeks). Each marks a lung damaged or repeatedly treated enough for Pseudomonas to colonise it."),
    ('d', "**Risk: levofloxacin 750 mg, cefepime, ceftazidime or piperacillin-tazobactam, after sputum culture. No risk: levofloxacin, moxifloxacin, ceftriaxone or cefotaxime. Re-evaluate at 72 h.** Sputum is sent before anti-pseudomonal treatment so it can be narrowed later. GOLD recommends 5–7 days; failure to improve by 72 hours prompts a review of the organism and the diagnosis."),
  ],
  mimic=[
    ("Productive cough vs purulent sputum", "More sputum is one cardinal symptom; purulence is the one that predicts bacteria and is needed when only two are present."),
  ],
  traps=[
    ("“More dyspnoea and a productive cough: antibiotics are the most beneficial treatment”", "Without stated purulence or ventilation, GOLD does not require them; bronchodilators, steroid and controlled oxygen come first (COPD-23)."),
  ],
  decode=[
    ("COPD exacerbation, more dyspnoea and productive cough, PaCO₂ 65 — most beneficial treatment? [DocT QBank]", "Keyed: systemic steroids. Antibiotics only if sputum is purulent or the patient needs ventilation."),
  ],
  punch="Give antibiotics in a COPD exacerbation when all three cardinal symptoms are present, or two including purulence, or when the patient is ventilated; cover Pseudomonas if there are risk factors, and review at 72 hours.",
)

L['COPD-25'] = dict(
  sub="Respiratory → Drugs → Heliox",
  step=4,
  intro="Heliox replaces nitrogen with helium, a much lighter gas, to ease flow through narrowed airways. It works only if enough helium is in the mix, and the one question turns on that.",
  parts=[
    ('a', "**Helium:oxygen 80:20 or 70:30.** Helium is always the larger fraction."),
    ('b', "**Low density → low Reynolds number → turbulent flow becomes laminar.** The Reynolds number is density × velocity × diameter ÷ viscosity; above a threshold flow turns turbulent. Turbulent resistance depends on density, so a gas about one-third as dense as air lowers it; and with a low Reynolds number more of the flow becomes laminar, where resistance is lower for the same flow."),
    ('c', "**Lower airflow resistance and work of breathing; better bronchodilator delivery.** Laminar flow carries aerosol deeper. It buys time for drugs to work; it does not treat the asthma, and GINA does not recommend it routinely."),
    ('d', "**Helium must be at least 60–70% to work, so FiO₂ cannot exceed 0.3–0.4 (standard teaching, not in your notes).** Diluting helium below that loses the density advantage. A hypoxaemic patient who needs more than 40% oxygen cannot use it."),
  ],
  mimic=[
    ("Density vs viscosity", "Helium’s viscosity is similar to, slightly above, that of air; the benefit comes entirely from its low density."),
  ],
  traps=[
    ("“Heliox 40:60 (He:O₂) in status asthmaticus is useful”", "Only 40% helium has almost no effect; it must be 60–80%. The Marrow explanation prints the ratio backwards; the answer stands."),
    ("“Heliox works because of its low viscosity” (COPD-29f)", "Low density."),
  ],
  decode=[
    ("Status asthmaticus — least useful therapy? [Marrow]", "Heliox 40:60 He:O₂, because the helium fraction is too low."),
  ],
  punch="Heliox works by low density, turning turbulent flow laminar, so it needs at least 60–70% helium and cannot be used when the patient needs more than 30–40% oxygen.",
)

L['COPD-26'] = dict(
  sub="Respiratory → Support → Supportive care while ventilated",
  step=5,
  intro="The ventilated COPD patient lives with a high PaCO₂ (COPD-16), a strained right heart and drugs that stimulate the heart. This card covers what that does to the body and the care around it. The one question tests which way CO₂ moves the cerebral and pulmonary vessels.",
  parts=[
    ('a', "**Judicious: prone to overload (heart failure, pulmonary hypertension); BNP helps.** Many have cor pulmonale or left-ventricular disease, and extra fluid worsens oxygenation and weaning. Fluid is still needed after intubation when trapping and sedation drop the blood pressure (COPD-04)."),
    ('b', "**Acidosis: raised cerebral blood flow and ICP, cardiac output, pulmonary artery pressure and catecholamines; lower SVR. Alkalosis from aggressive hyperventilation is symptomatic above pH 7.55: seizures, coma, arrhythmias, arrest.** CO₂ dilates cerebral vessels, so ICP rises; in the lung, acidosis and hypoxia constrict vessels, so pulmonary pressure rises and the right ventricle strains. Acidosis also shifts the oxygen dissociation curve to the right and stimulates the sympathetic system. Over-ventilating a retainer whose bicarbonate is high causes post-hypercapnic metabolic alkalosis (COPD-16c)."),
    ('c', "**Early enteral feeding; avoid overfeeding (excess CO₂); no benefit from pulmonary formulas.** Excess calories, especially carbohydrate, are converted to fat; that conversion (lipogenesis) produces more CO₂ than the oxygen it uses (respiratory quotient above 1), which adds to the ventilatory load. What matters is not overfeeding; high-fat ‘pulmonary’ feeds add nothing."),
    ('d', "**Hypoxia, high work of breathing, beta-agonists and aminophylline, pulmonary hypertension. Optimise ventilation and sedation, reduce or stop the offending drug, exclude myocardial ischaemia.** Multifocal atrial tachycardia is the classic COPD rhythm; it settles when the cause is treated and potassium and magnesium are corrected (β-agonists and steroids lower potassium)."),
  ],
  mimic=[
    ("CO₂ on cerebral vs pulmonary vessels", "Cerebral: dilatation, more flow, higher ICP. Pulmonary: constriction (with acidosis and hypoxia), higher PA pressure."),
  ],
  traps=[
    ("“Hypercapnia causes cerebral vasoconstriction and reduced cerebral blood flow” (62% right)", "It causes vasodilatation and raised ICP; that is why permissive hypercapnia is avoided in raised ICP. Pulmonary vasoconstriction, a right-shifted curve and sympathetic stimulation are all true effects."),
  ],
  decode=[
    ("Smoker, drowsy, pH 7.28, PaCO₂ 75, HCO₃ 34, intubated — which effect is NOT expected? [DocT QBank]", "Cerebral vasoconstriction with reduced cerebral blood flow."),
  ],
  punch="Hypercapnic acidosis dilates cerebral vessels and constricts pulmonary ones; keep fluids lean, do not overfeed, and do not over-correct the CO₂ into alkalosis.",
)

L['COPD-27'] = dict(
  sub="Respiratory → Weaning → Why COPD patients fail weaning",
  step=6,
  intro="Weaning fails when the load on the respiratory muscles outweighs their capacity. This table sorts the causes so each can be looked for and corrected before the next trial.",
  parts=[
    ('a', "**Gas exchange: V/Q mismatch; shunt (atelectasis, embolism).** Hypoxaemia and a high dead space raise the ventilation needed."),
    ('b', "**Muscle: fatigue, atrophy, hyperinflation, high resistive load.** Hyperinflation flattens the diaphragm (COPD-03), and days of controlled ventilation waste it."),
    ('c', "**Ventilator: resistance of tube, circuit, humidifier, demand valves.** A narrow tube adds work (COPD-16d)."),
    ('d', "**Metabolic: overfeeding; malnutrition; low phosphate or magnesium.** Overfeeding adds CO₂ (COPD-26c); low phosphate and magnesium weaken the muscles."),
    ('e', "**Cardiovascular: LV failure with oedema; pulmonary hypertension with RV failure.** Moving from positive pressure to spontaneous breathing raises venous return and left-ventricular afterload, so a weak heart develops pulmonary oedema during the trial."),
    ('f', "**Neurological: sedation; critical-illness polyneuromyopathy; delirium.** Steroids and neuromuscular blockers add myopathy (COPD-16d)."),
  ],
  mimic=[
    ("Weaning-induced pulmonary oedema vs respiratory muscle failure", "Both fail the trial; oedema brings a rise in BNP and a fall in oxygenation, and responds to diuretics and nitrates."),
  ],
  traps=[
    ("“Clinical judgment predicts weaning outcome well” (COPD-29h)", "Sensitivity 35%, specificity 79%: daily screening and a protocolled trial are better."),
  ],
  decode=[
    ("[pattern] COPD repeatedly fails SBT — list correctable causes by category", "Load (resistance, hyperinflation, overfeeding), capacity (muscles, phosphate, sedation) and the heart."),
  ],
  punch="COPD patients fail weaning when load exceeds capacity: look for hyperinflation, a narrow tube, overfeeding, low phosphate, sedation and a failing heart, and decide by protocol, not judgment.",
)

L['COPD-28'] = dict(
  sub="Respiratory → Weaning → Extubation and outcome",
  step=6,
  intro="The last step is getting the tube out and knowing what follows. Seven questions test the order — readiness, then a spontaneous breathing trial, then extubation to NIV — and the mortality figures after ventilation.",
  parts=[
    ('a', "**Extubate to NIV.** A normal pH and the patient’s baseline PaCO₂ make him ready to be tested, not to be extubated: he first passes a spontaneous breathing trial (pressure support 5–8, CPAP or T-piece, 30–120 minutes), is extubated, and goes straight onto NIV. ERS/ATS (2017) make two conditional recommendations that apply here: NIV to facilitate weaning in hypercapnic patients (extubating them to NIV, even before they are fully ready to breathe unsupported, in experienced units), and NIV to prevent post-extubation failure in high-risk patients, among whom hypercapnic COPD is the clearest group; they advise against it in patients who are not at high risk. A trial is a team process: the nurse, therapist and doctor are present at its start and watch the first minutes."),
    ('b', "**Prevents post-extubation respiratory failure; lowers re-intubation and ICU mortality.** NIV takes over part of the work while the muscles recover, and holds PEEP against intrinsic PEEP. When a COPD patient develops hypercapnia and distress after extubation, NIV is the next step; in other patients, NIV for established post-extubation failure is advised against, because it delays needed re-intubation."),
    ('c', "**Asthma has the better prognosis; ventilation does not worsen it.** Asthma’s obstruction resolves; COPD’s is fixed, and the patient has used up his reserve."),
    ('d', "**6-month survival 40–70%.** The questions test mortality instead. GOLD puts in-hospital mortality for a hypercapnic exacerbation with acidosis at about 10%, and mortality at 1 year after discharge at about 40% in those who needed ventilatory support; in ICU series of ventilated patients, hospital mortality is about 25–30% (Seneff 1995: 24% overall, 30% at 65 or over, with 59% of those aged 65 or over dead at 1 year). Marrow’s keyed ranges (10–30% in hospital, 40–60% at 1 year) span these figures. The deaths come from the underlying lung and heart disease, not from the ventilator."),
    ('e', "**Functional and nutritional status, exacerbation frequency, comorbidities. Poor: dyspnoea at rest; cor pulmonale; obstruction irreversible with beta-agonists; cachexia; frequent exacerbations; cardiomyopathy or nephropathy.** Older age, low BMI and albumin, chronic steroids and chronic hypercapnia are other markers. The acute gas matters less than how the patient lived before."),
  ],
  table=dict(title="From ventilator to NIV in COPD", head=["Stage", "Test", "Next"], rows=[["Improving: pH normal, PaCO₂ at baseline", "ready to test", "**spontaneous breathing trial**, not extubation yet"], ["Passes SBT", "hypercapnic or high risk", "**extubate to NIV**"], ["Post-extubation hypercapnia and distress", "COPD", "**NIV**; re-intubate if it fails"], ["Fails SBT", "look for a cause (COPD-27)", "rest, correct, retest next day"]]),
  mimic=[
    ("NIV to prevent failure vs NIV to rescue it", "Prevention after extubation in high-risk or hypercapnic patients is recommended; rescue of established failure is advised against in general, though those trials largely excluded hypercapnic COPD, where a short NIV trial is standard."),
  ],
  traps=[
    ("“Improving on day 2, pH 7.35, PaCO₂ 50: extubate to NIV, or continue full ventilation” (52% right)", "First run a spontaneous breathing trial; extubation to NIV follows only a pass."),
    ("“After a passed SBT with risk factors, delay extubation or do a tracheostomy”", "Extubate and add NIV (94% right)."),
    ("“Post-extubation hypercapnia in COPD: re-intubate at once or give high-flow oxygen”", "Start NIV (93% right); re-intubate if it fails."),
  ],
  decode=[
    ("Ventilated AECOPD, day 2, pH 7.35, PaCO₂ 50 — next step? [DocT QBank]", "Spontaneous breathing trial."),
    ("Hypercapnic COPD passes SBT on day 3 — next step? [Marrow, DocT GT]", "Extubate to BiPAP."),
    ("COPD weaned off, now moderate hypercapnia and distress — next step? [DocT GT]", "Non-invasive ventilation."),
    ("GOLD figures: in-hospital and 12-month mortality after ventilation for AECOPD [Marrow, two questions]", "10–30% in hospital; 40–60% at one year."),
  ],
  extra=[
    dict(q="Protocolised SBT — which step best ensures safety? [Marrow]", a="Nurse, respiratory therapist and physician present at the start, watching the first 5–10 minutes."),
  ],
  punch="A COPD patient ready to wean first passes a spontaneous breathing trial and is then extubated straight to NIV; after ventilation, roughly 40–60% die within a year.",
)

L['COPD-29'] = dict(
  sub="Respiratory → COPD → Revision: true or false",
  step=6,
  intro="A sweep through the deck. Each statement turns on one detail from an earlier card.",
  parts=[
    ('a', "**False — auto-PEEP is measured with an end-expiratory hold** (COPD-18)."),
    ('b', "**False — dynamic auto-PEEP is lower, reflecting the fastest units only** (COPD-19)."),
    ('c', "**True — external PEEP at 80% of intrinsic PEEP relieves trigger load safely** (COPD-21)."),
    ('d', "**False — a high flow (80–100 L/min) lengthens expiration and reduces trapping** (COPD-15)."),
    ('e', "**False — the target is pH (his normal pH), not a normal PaCO₂** (COPD-16)." + " His normal pH is the one he lives at, reached by returning to his own baseline PaCO₂; in the acute phase a pH above about 7.2 is accepted, and a textbook pH of 7.35–7.45 is not forced by over-ventilation."),
    ('f', "**False — heliox works by low density** (COPD-25)."),
    ('g', "**True — terbutaline 0.25 mg SC is preferred in pregnancy** (COPD-22)."),
    ('h', "**False — clinical judgment has a sensitivity of 35% and a specificity of 79%** (COPD-27)."),
  ],
  mimic=[],
  traps=[
    ("“A low inspiratory flow is gentler on the lung and reduces trapping”", "It lengthens inspiration and shortens expiration; trapping worsens."),
  ],
  decode=[
    ("[pattern] True/false on auto-PEEP and ventilation in obstruction", "End-expiratory hold, dynamic lower than static, PEEPe 80% of PEEPi, high flow, target pH, low density."),
  ],
  punch="Most errors here come from direction: hold at end-expiration, dynamic is lower, flow goes up not down, and the target is pH, not a normal PaCO₂.",
)

FLAGS = {}
FLAGS['COPD-16'] = "Card c says ‘target pH, not PaCO₂’; Marrow keys the chronic retainer’s goal as return to his BASELINE PaCO₂ and notes the wording can pull to ‘normal pH 7.35–7.45’. Not wrong; consider adding ‘aim for his baseline PaCO₂’. Explanation gives both."
FLAGS['COPD-21'] = "DocT QBank key (switch to flow triggering for ineffective efforts) is debatable: flow triggering saves ~1 cmH₂O; reducing PEEPi (inspiratory flow 80 L/min, option D) or offsetting it treats the cause. Card is right."
FLAGS['COPD-22'] = "Two DocT keys name ‘high-dose inhaled corticosteroids and β-agonists’; they are right only for the β-agonist — the acute steroid is systemic (card b is right). Card a’s salbutamol ‘2.5 mg (continuous for an hour)’ is at the low end and mixes two schedules: GINA/NAEPP 2.5–5 mg every 20 min in the first hour; BTS/SIGN 5 mg, repeated every 15–30 min, or continuous 5–10 mg/hour. Card b’s hydrocortisone 200 mg differs from BTS/SIGN (100 mg IV 6-hourly). Ipratropium 0.5 mg 4–6-hourly matches BTS; in the first hour it is given with each of the first three salbutamol doses (DocT GT4). Not wrong enough to change; explanation gives both."
FLAGS['COPD-23'] = "DocT QBank keys ‘high-dose IV corticosteroids’ as most beneficial in AECOPD (25% right). GOLD: inhaled SABA ± SAMA first, then oral prednisolone 40 mg × 5 days; IV/high dose adds no benefit. Key is least wrong, not right; card is right (same question under COPD-24)."
FLAGS['COPD-24'] = "Card c gives the Pseudomonas FEV₁ cut-off as <50%. The older GOLD table uses FEV₁ <30%, with recent hospitalisation and oral steroids >10 mg/day in the last 2 weeks; <50% appears in other lists (e.g. Sanford 2014). Not wrong, but a question keyed to GOLD would want <30%. Explanation gives both."
FLAGS['COPD-28'] = "Card d gives only 6-month survival (40–70%), which is not the figure the questions test. Marrow keys in-hospital mortality 10–30% and 1-year mortality 40–60% after ventilation; GOLD gives about 10% in-hospital for hypercapnic acidosis and about 40% at 1 year after ventilatory support, Seneff 1995 24% hospital and 59% 1-year (age ≥65). Consider adding the in-hospital and 1-year figures; explanation gives them."
FLAGS['COPD-29'] = "Row e’s reason ‘Normal pH’ can be read as a textbook pH of 7.35–7.45, which Marrow’s retainer question marks wrong (key: return to baseline PaCO₂). Consider ‘Target pH (his usual pH) via his baseline PaCO₂’. Explanation clarifies."
