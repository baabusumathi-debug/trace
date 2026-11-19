# CVS07A — Explain v3 ("Learn" depth): post-cardiac-arrest care, part 1 — how CPR duration predicts outcome, the post-cardiac-arrest syndrome (definition, cascade), the chain of survival,
# the components, goals and phases of post-arrest care, the immediate post-ROSC algorithm and its doses, the reversible causes, the ERC–ESICM 2021 immediate targets, diagnostic pathway and
# ICU bundle, the diagnostic work-up, respiratory and haemodynamic targets, arrhythmias and coronary angiography, seizures and myoclonus, and general ICU care.
# No mnemonics or hooks. Driven by qpack/CVS07A.md (8 question links; PCA-16, PCA-18 and PCA-19 asked twice each, PCA-09 and PCA-17 once). PCA-01 to 08, 10 to 15 and 20 have no linked
# question and get short explanations with [pattern] decode items. One Top-up card (T_db59d55f, Pittsburgh Cardiac Arrest Category) is in cvs07a_topups_learn.py.
# No `fix` entries exist for CVS07A in trace/test/data/qbank.json (checked 19 Nov 2026); cvs_cardlayer.json has chips only, plus one `cross` line for PCA-17 (DocT MAP >80 key), which was used.
# Checked online on 19 Nov 2026:
#  - AHA 2025 Part 11 Post-Cardiac Arrest Care (cpr.heart.org): 100% O₂ until SpO₂/PaO₂ reliable (1, B-R); avoid hypoxaemia (1); then titrate to SpO₂ 90–98% (PaO₂ 60–105 mmHg) (2a, B-R);
#    PaCO₂ 35–45 mmHg (1, B-R); avoid hypotension, MAP at least 65 mmHg (1, B-R); no specific vasopressor recommended (2b); emergent angiography for persistent ST elevation regardless of coma
#    (1, B-NR); reasonable without STE for cardiogenic shock, recurrent ventricular arrhythmias or significant ongoing ischaemia (2a); comatose without STE/shock/instability/ischaemia: emergent
#    angiography no better than delayed (3: No Benefit, B-R); temporary MCS not routine (3), may be considered in selected refractory shock (2b); temperature control for all adults not following
#    commands (1), 32–37.5 °C (1), at least 36 h (2a); EEG promptly in those not following commands (1); treat clinical seizures (1); no routine seizure prophylaxis (3: No Benefit, B-R); EEG for
#    myoclonus (1); treating myoclonus without EEG correlate not recommended (3: No Benefit, C-LD); glucose: avoid <70 and >180 mg/dL (2b); routine prophylactic antibiotics and steroids of
#    uncertain benefit (2b); multimodal prognostication at least 72 h after normothermia and sedation stopped (2a).
#  - AHA 2025 adult post-cardiac arrest care algorithm (cpr.heart.org PDF, 250527): SpO₂ 90–98%, PaCO₂ 35–45, MAP ≥65; 12-lead ECG, consider CT head/chest/abdomen/pelvis and POCUS;
#    emergency cardiac intervention for persistent STE, cardiogenic shock, recurrent VT/VF or severe ischaemia; temperature control 32–37.5 °C if not following commands; EEG; glucose 70–180 mg/dL.
#    No dose panel (the 2015/2020 algorithm’s 1–2 L bolus and infusion doses are gone).
#  - ERC–ESICM 2025 post-resuscitation care (Resuscitation 2025;215 Suppl 1:110809; text via resus.org.uk, 27 Oct 2025): SpO₂ 94–98%, PaO₂ 10–13 kPa (75–100 mmHg); PaCO₂ 4.7–6.0 kPa
#    (35–45 mmHg); ‘aim for SBP >100 mmHg or MAP >60–65 mmHg’; ‘maintain perfusion with fluids, noradrenaline and/or dobutamine’ by need (no ranked first-line agent stated); IABP, LVAD or
#    VA-ECMO considered in refractory shock; no routine steroids; emergent cath lab for persistent STE, otherwise delay unless high likelihood of acute coronary occlusion; dual-phase whole-body CT
#    including CTPA suggested at admission; actively prevent fever ≤37.5 °C for 36–72 h, do not actively rewarm mild hypothermia; no seizure prophylaxis; levetiracetam or sodium valproate first line;
#    wake-up trial when myoclonus has a benign EEG background; status myoclonus ≤72 h a poor-outcome predictor; ‘standard glucose management protocols’ (no number); no routine prophylactic
#    antibiotics; stress ulcer prophylaxis especially with coagulopathy; trophic gastric feeding; short-acting sedatives; no systematic NMB; prognosticate at ≥72 h if GCS motor <6.
#  - ILCOR 2008 PCAS consensus statement (Neumar, Circulation/Resuscitation 2008; ilcor.org PDF): four components — post-arrest brain injury, myocardial dysfunction, systemic ischaemia/reperfusion
#    response, persistent precipitating pathology; severity varies with the ischaemic insult, the cause of arrest and pre-arrest health; mechanisms include free radicals, protease cascades and
#    disrupted calcium homeostasis; phases: immediate first 20 min, early 20 min–6–12 h, intermediate 6–12 h–72 h, recovery beyond 3 days; seizures/myoclonus in 5–15% of all ROSC and 10–40% of
#    those who stay comatose.
#  - Goto, Funada, Goto, JAHA 2016;5:e002819 (abstract and full text, scienceopen PDF): 17,238 adult OHCA with PREHOSPITAL ROSC, Japan 2011–12; CPR duration = EMS CPR start to prehospital ROSC;
#    overall 1-month survival 36.8%, CPC 1–2 21.8%; dynamic probability after 20 min 4.6% survival and 1.9% CPC 1–2; after 30 min 0.8% and 0.4%; no survivor beyond 53 min; >99% of CPC 1–2
#    survivors had ROSC within 35 min (42 min for asystole).
#  - AHA 2025 chain of survival (secondary sources: EMS1, InPulse CPR): one chain for all ages and settings replacing the separate IHCA/OHCA/paediatric chains; six links (recognition and activation,
#    high-quality CPR, defibrillation, advanced resuscitation, post-cardiac arrest care, recovery). Primary AHA Part 3 text not opened.
#  - Pittsburgh Cardiac Arrest Category (UPMC Post-Cardiac Arrest Service page; Coppler, Resuscitation 2015 abstract, 607 patients): see topups file.
# From standard references (confident, not freshly checked): BOX (Kjaergaard, NEJM 2022, 789 comatose OHCA): MAP 63 vs 77 mmHg, death or severe disability no different; oxygen arm PaO₂ 68–75 vs
# 98–105 mmHg, no difference; COACT (Lemkes, NEJM 2019, 552 shockable without STE): 90-day survival 64.5 vs 67.2% immediate vs delayed angiography (NS); TOMAHAWK (Desch, NEJM 2021, 554):
# 30-day death 54.0 vs 46.0% (NS); TELSTAR (Ruijter, NEJM 2022, 172): suppressing rhythmic/periodic EEG patterns did not change poor outcome (90 vs 92%); Kilgannon (JAMA 2010): PaO₂ ≥300 mmHg linked
# to higher mortality (observational); NICE-SUGAR glucose range 7.8–10 mmol/L; Lance–Adams syndrome; AHA 2010/2015 post-ROSC algorithm doses (bolus 1–2 L, adrenaline 0.1–0.5, dopamine 5–10,
# noradrenaline 0.1–0.5 mcg/kg/min; PETCO₂ 35–40); fibrinolysis after prolonged or traumatic CPR is a relative contraindication.
# Could not verify: the exact AHA Part 3 wording of the 2025 chain links. Second review (19 Nov 2026, standard reference): the card’s ‘33% seizures / 20–25% myoclonus’ pair is the ERC 2015/2021 text (one-third of comatose survivors seize; myoclonus the commonest type, 18–25%).
# Second review 19 Nov 2026: Goto 2016 full text re-read (20 min 4.6%/1.9%; 30 min 0.8%/0.4%; none beyond 53 min) and confirmed.

SPINE = [
  ("Duration decides the damage", "The longer the circulation is absent and CPR runs before ROSC, the deeper the whole-body ischaemia, and both survival and good neurological recovery fall steeply after about 20 minutes."),
  ("ROSC starts a second disease", "Post-cardiac arrest syndrome is the ischaemia of the arrest plus the reperfusion injury of resuscitation, hitting brain, heart and every other organ, so its severity tracks how long and how deep the insult was."),
  ("A chain, goals and phases", "Post-arrest care is a link in the chain of survival with fixed goals (keep the patient alive, find the cause, protect the brain, treat reperfusion injury) and a clock running from the first 20 minutes to 72 hours and beyond."),
  ("The first minutes after ROSC", "Immediately after ROSC the team secures oxygenation without hyperoxia, ventilation without hyperventilation and a MAP of at least 65, then sends ST elevation to the cath lab and the patient who does not follow commands to temperature control."),
  ("Finding the cause", "A cardiac cause with persistent ST elevation goes for emergent angiography whatever the conscious level; without it, angiography is deferred unless there is shock, recurrent arrhythmia or ongoing ischaemia, and CT looks for the non-cardiac causes."),
  ("Supporting the organs in ICU", "In ICU the targets are normoxia, normocapnia, a perfusing pressure, fever prevention, normoglycaemia and treatment of seizures, with prognosis deferred for at least 72 hours."),
]

PRIMER = "ROSC means return of spontaneous circulation: a palpable pulse and measurable pressure after CPR. The guidelines’ word ‘comatose’ means not following verbal commands after ROSC, and it is the entry criterion for temperature control and for most of the brain-protective care in this deck. Two guideline families are quoted throughout: the American Heart Association (AHA 2025, Circulation, October 2025) and the European ERC–ESICM post-resuscitation guideline (2021, updated October 2025); where they give different numbers, the card usually quotes one of them, so the source matters. MAP is mean arterial pressure; PCI is percutaneous coronary intervention; TTM is targeted temperature management, now called temperature control."

L = {}

L['PCA-01'] = dict(
  sub="Post-arrest care → CPR duration → Survival and neurological outcome by minutes of CPR",
  step=1,
  intro="Step 1 starts before ROSC: how long CPR ran before the heart restarted is the strongest early marker of how severe the coming post-arrest syndrome will be. The figures come from one large Japanese registry, and the point is the shape of the curve rather than the decimals.",
  parts=[
    ('a', "**At 1 minute: survival 36.8%, favourable neurological outcome 21.8%.** These are the starting point of the curve in Goto 2016 (17,238 out-of-hospital arrests that achieved ROSC before hospital). In the paper they are the cohort’s overall 1-month rates, which the ‘dynamic probability’ curve begins from."),
    ('b', "**At 20 minutes: survival 4.6%, favourable neurological outcome 0.8%.** Survival 4.6% matches the paper. The paper gives favourable neurological outcome after 20 minutes as 1.9%, not 0.8% (see FLAGS). Either way the drop is about eightfold in 20 minutes: each minute without circulation deepens brain ischaemia, and the brain is the organ that decides a good outcome."),
    ('c', "**At 30 minutes: survival 0.4%, favourable neurological outcome 0%.** The paper gives 0.8% survival and 0.4% favourable outcome after 30 minutes, so good neurological recovery is rare but not zero at 30 minutes (FLAGS). The same study found that more than 99% of good-outcome survivors had ROSC within 35 minutes (42 minutes for asystole)."),
    ('d', "**At 53 minutes: survival 0%, favourable neurological outcome 0%.** No patient whose CPR lasted more than 53 minutes survived to one month. CPR duration here means EMS CPR start to prehospital ROSC; bystander CPR time is not counted, and the study included only patients who did get ROSC."),
  ],
  mimic=[
    ("Duration of CPR vs no-flow time", "No-flow is collapse to first compression, with no circulation at all; CPR duration is low-flow time. Both predict outcome, and a long no-flow time makes even short CPR less hopeful."),
  ],
  traps=[
    ("“Favourable neurological outcome reaches zero at 30 minutes”", "The source gives 0.4% at 30 minutes; the 35-minute figure (over 99% of good outcomes by then) is the one used to argue for continuing CPR to at least 35 minutes."),
    ("“No ROSC by 20 minutes means stop”", "Duration alone is never a termination rule in the guidelines; shockable rhythm, witnessed arrest, bystander CPR and reversible causes (and ECPR) change the picture."),
  ],
  decode=[
    ("[pattern] Beyond about how many minutes of CPR do good neurological outcomes almost disappear?", "About 35 minutes (over 99% of good outcomes had ROSC by then); survival falls to zero beyond 53 minutes."),
    ("[pattern] Survival and good outcome at 20 minutes of CPR", "Survival about 5%, good neurological outcome about 1–2%: a roughly eightfold fall from the start."),
  ],
  punch="Outcome falls steeply with every minute of CPR: by 20 minutes survival is under 5%, by 30 minutes good recovery is well under 1%, almost every good outcome has ROSC within 35 minutes, and no one survived beyond 53.",
)

L['PCA-02'] = dict(
  sub="Post-arrest care → Post-cardiac arrest syndrome → Definition, processes and severity",
  step=2,
  intro="Step 2 names the disease that ROSC starts. The 2008 ILCOR statement called it post-cardiac arrest syndrome (PCAS) and defined it as two insults in sequence, which is why the patient can deteriorate hours after a ‘successful’ resuscitation.",
  parts=[
    ('a', "**The complex pathophysiological processes following whole-body ischaemia during cardiac arrest and the subsequent reperfusion response during CPR and after successful resuscitation.** The first insult is ischaemia: no flow, no oxygen, ATP runs out. The second is reperfusion: when oxygen returns, the injured cells make free radicals and inflammatory signals. ILCOR divides the result into four components: post-arrest brain injury, myocardial dysfunction, the systemic ischaemia/reperfusion response, and the persistent pathology that caused the arrest."),
    ('b', "**Disruption of homeostasis; free radical formation; protease activation.** Ischaemia stops the ATP-driven pumps, so calcium floods into cells (the homeostasis that fails); oxygen arriving at damaged mitochondria produces reactive oxygen species; calcium switches on proteases (calpains, caspases) that digest the cell from inside. These run for hours to days, which is the window that post-arrest care tries to use."),
    ('c', "**Severity depends on various factors.** ILCOR names them: how severe and how long the ischaemic insult was (no-flow and low-flow time, PCA-01), the cause of the arrest, and the patient’s health before it. A short witnessed VF arrest from a coronary occlusion produces a mild syndrome; a long asystolic arrest from hypoxia produces a severe one."),
  ],
  mimic=[
    ("PCAS vs sepsis", "The systemic ischaemia/reperfusion response looks like sepsis (vasodilatation, high cytokines, capillary leak) but starts at ROSC without infection; true infection can follow later from aspiration or gut translocation (PCA-03)."),
  ],
  traps=[
    ("“ROSC ends the injury”", "Reperfusion is the second insult; much of the brain injury develops after circulation returns."),
  ],
  decode=[
    ("[pattern] PCAS definition: which two insults?", "Whole-body ischaemia during arrest plus reperfusion during CPR and after ROSC."),
    ("[pattern] Four components of PCAS", "Brain injury, myocardial dysfunction, systemic ischaemia/reperfusion response, persistent precipitating pathology."),
  ],
  punch="Post-cardiac arrest syndrome is two insults, ischaemia and then reperfusion, driven by calcium overload, free radicals and proteases, and its severity follows how long and how deep the arrest was, its cause and the patient before it.",
)

L['PCA-03'] = dict(
  sub="Post-arrest care → Post-cardiac arrest syndrome → The organ cascade",
  step=2,
  intro="Step 2 continues by following the injury into each organ. The card’s cascade shows why the post-arrest patient often has several shocks and several failures at once, and how lung injury feeds back into more hypoxia.",
  parts=[
    ('a', "**CPR and defibrillation → hypoxic brain injury, impaired cerebral autoregulation, myocardial stunning (decreased systolic function).** Low-flow CPR delivers only a fraction of normal brain flow; afterwards the brain loses autoregulation, so its flow follows blood pressure passively, which is why hypotension after ROSC is so damaging. The heart, ischaemic and shocked, is stunned: systolic function is depressed for 24–72 hours and usually recovers."),
    ('b', "**Global hypoxic injury → systemic inflammatory response, aspiration pneumonitis, loss of intestinal barrier function, immune dysfunction, acute renal failure, ischaemic hepatitis.** Every organ was ischaemic. The gut and kidney are the most sensitive after the brain; aspiration happens during the collapse and the CPR."),
    ('c', "**Hypoxic brain injury → cerebral oedema; myocardial stunning → cardiogenic shock.** Cytotoxic oedema follows neuronal energy failure; on CT it shows as loss of grey–white differentiation and predicts a poor outcome. The stunned ventricle produces low-output cardiogenic shock."),
    ('d', "**Systemic inflammatory response → distributive shock.** Cytokines and endothelial injury cause vasodilatation and capillary leak, the ‘sepsis-like’ part of PCAS. Its overlap with cardiogenic shock is why post-arrest shock is usually mixed and needs echo to separate the two."),
    ('e', "**Loss of intestinal barrier plus immune dysfunction → sepsis from bacterial translocation from the ischaemic gut; aspiration pneumonitis and barrier loss → ARDS.** Ischaemic mucosa lets bacteria and endotoxin through while immune function is depressed; aspiration injures the lung directly."),
    ('f', "**Shock states and ARDS → pulmonary oedema → further global hypoxic injury (the loop closes).** Low output and leaky capillaries flood the lung, oxygenation falls and the hypoxic injury restarts. Breaking that loop (oxygenation, perfusion) is the logic of the ICU bundle (PCA-14)."),
  ],
  mimic=[
    ("Cardiogenic vs distributive post-arrest shock", "Cardiogenic: poor LV function on echo, low output, cold periphery; distributive: good or hyperdynamic LV, low SVR, warm. Often both, so noradrenaline plus dobutamine is common."),
  ],
  traps=[
    ("“Post-arrest shock is one type”", "It is usually mixed: stunned myocardium plus inflammatory vasodilatation (the card’s watch line)."),
  ],
  decode=[
    ("[pattern] Which shock follows myocardial stunning, and which the systemic inflammatory response?", "Cardiogenic and distributive respectively."),
    ("[pattern] Mechanism of sepsis after cardiac arrest", "Bacterial translocation through the ischaemic gut, with immune dysfunction."),
  ],
  punch="The arrest injures every organ at once: the stunned heart gives cardiogenic shock, inflammation gives distributive shock, gut and lung injury give sepsis and ARDS, and the resulting pulmonary oedema restarts the hypoxia.",
)

L['PCA-04'] = dict(
  sub="Post-arrest care → Systems of care → Chain of survival",
  step=3,
  intro="Step 3 places post-arrest care in the wider system. The chain of survival is the sequence of links that a patient needs; post-arrest care is the fifth, and it is the first link delivered in hospital.",
  parts=[
    ('a', "**1 Activation of emergency system → 2 CPR → 3 defibrillation → 4 advanced EMS care → 5 post-arrest care → 6 recovery.** This is the AHA 2020 adult out-of-hospital chain; ‘recovery’ was added as a sixth link in 2020 to cover rehabilitation and survivorship. AHA 2025 replaced the separate in-hospital, out-of-hospital and paediatric chains with one chain for all ages and settings, with essentially the same six links (recognition and activation, high-quality CPR, defibrillation, advanced resuscitation, post-arrest care, recovery)."),
    ('b', "**Prehospital phase: links 1–4 (activation, CPR, defibrillation, advanced EMS care).** These decide whether ROSC happens at all, and how long the no-flow and low-flow times are (PCA-01)."),
    ('c', "**Post-acute phase: links 5–6 (post-arrest care, recovery).** These decide what kind of survivor results."),
  ],
  mimic=[
    ("Out-of-hospital vs in-hospital chain (2020)", "The 2020 in-hospital chain began with early recognition and prevention rather than activation of EMS; 2025 merged them."),
  ],
  traps=[
    ("“Recovery is not a link”", "It has been the sixth link since 2020."),
  ],
  decode=[
    ("[pattern] Which link was added in 2020, and which links are prehospital?", "Recovery; links 1–4."),
  ],
  punch="The chain runs activation, CPR, defibrillation, advanced care, post-arrest care and recovery; the first four decide whether the heart restarts, the last two what kind of survivor results.",
)

L['PCA-05'] = dict(
  sub="Post-arrest care → Components of post cardiac arrest care (PCAC)",
  step=3,
  intro="Step 3 lists what post-arrest care looks after. The five components map onto the organs that PCAS injures (PCA-03), and each is expanded later in the deck.",
  parts=[
    ('a', "**Ventilation.** Oxygenation without hyperoxia and normocapnia without hyperventilation (PCA-16)."),
    ('b', "**Haemodynamics.** A perfusing pressure for a brain that has lost autoregulation (PCA-17)."),
    ('c', "**Cardiovascular.** The cause of the arrest, usually coronary: ECG, echo, angiography and arrhythmia control (PCA-18)."),
    ('d', "**Neurological.** Temperature control, seizure detection and treatment, and delayed prognostication (PCA-19, CVS07B)."),
    ('e', "**Metabolic.** Glucose, electrolytes (especially potassium and magnesium) and acid–base (PCA-20)."),
  ],
  mimic=[
    ("PCAC as care vs PCAC as Pittsburgh category", "Here PCAC means post cardiac arrest care; the Pittsburgh Cardiac Arrest Category (top-up card) is a four-level severity score with the same initials."),
  ],
  traps=[
    ("“PCAC = the Pittsburgh score”", "Read the stem: ‘components’ means the care domains; ‘category I–IV’ means the severity score."),
  ],
  decode=[
    ("[pattern] Five components of post cardiac arrest care", "Ventilation, haemodynamics, cardiovascular, neurological, metabolic."),
  ],
  punch="Post-arrest care has five domains, ventilation, haemodynamics, the heart, the brain and metabolism, which match the organs the syndrome injures.",
)

L['PCA-06'] = dict(
  sub="Post-arrest care → Goals of post cardiac arrest care",
  step=3,
  intro="Step 3 continues with what post-arrest care is for. The four goals are the four components of PCAS turned into tasks.",
  parts=[
    ('a', "**Maintain vitals.** Keep the patient alive through the early instability: re-arrest, hypotension and hypoxaemia are common in the first hours."),
    ('b', "**Determine and treat the cause of arrest.** This is ILCOR’s ‘persistent precipitating pathology’: a coronary occlusion, PE or hypoxia not treated will cause another arrest (PCA-11, PCA-13)."),
    ('c', "**Minimise brain injury.** Brain injury causes most deaths after admission with ROSC, often through withdrawal of treatment, so temperature control, perfusion, normoxia and normocapnia are all aimed at the brain."),
    ('d', "**Manage problems from global ischaemia and reperfusion injury.** The myocardial dysfunction and the systemic, sepsis-like response (PCA-03)."),
  ],
  mimic=[
    ("Goals vs components", "Goals are what care tries to achieve (PCA-06); components are the organ domains it works through (PCA-05)."),
  ],
  traps=[
    ("“The main goal after ROSC is the heart”", "The heart usually recovers; the brain decides the outcome."),
  ],
  decode=[
    ("[pattern] Goals of post-arrest care", "Maintain vitals, treat the cause, minimise brain injury, manage ischaemia/reperfusion injury."),
  ],
  punch="Post-arrest care aims to keep the patient alive, remove the cause, protect the brain and treat the reperfusion injury: the four parts of the syndrome turned into tasks.",
)

L['PCA-07'] = dict(
  sub="Post-arrest care → Phases of post-cardiac arrest syndrome",
  step=3,
  intro="Step 3 puts a clock on the syndrome. ILCOR 2008 divided the time after ROSC into phases because the dangers, and so the priorities, change with time.",
  parts=[
    ('a', "**Immediate: ROSC to 20 minutes.** Re-arrest risk is highest and the cause is still active."),
    ('b', "**Early: 20 minutes to 6–12 hours.** The period when early interventions (reperfusion, temperature control, haemodynamic optimisation) are thought most likely to help."),
    ('c', "**Intermediate: 6–12 hours to 72 hours.** Injury pathways are still active; organ support, temperature control and fever prevention continue."),
    ('d', "**Recovery: 72 hours to disposition.** Prognosis becomes more reliable after this point, which is why prognostication waits until at least 72 hours (PCA-14)."),
    ('e', "**Rehabilitation: after disposition.** Physical and cognitive recovery, the sixth link of the chain (PCA-04). Across the phases run the overlays the card lists: prevent recurrence, limit ongoing injury and support organs, prognosticate, rehabilitate."),
  ],
  mimic=[
    ("Early vs intermediate phase", "The boundary is 6–12 hours; early is when interventions are most likely to change injury, intermediate is when the injury is still running but the window is closing."),
  ],
  traps=[
    ("“Prognosticate during the intermediate phase”", "The intermediate phase ends at 72 hours, and prognostication waits until at least then."),
  ],
  decode=[
    ("[pattern] Time boundaries of the phases of PCAS", "20 minutes, 6–12 hours, 72 hours, then disposition."),
  ],
  punch="The syndrome runs on a clock, 20 minutes, 6–12 hours and 72 hours, and the 72-hour boundary into recovery is the same 72 hours before which prognosis must not be decided.",
)

L['PCA-08'] = dict(
  sub="Post-arrest care → Management priority by phase",
  step=3,
  intro="Step 3 ends by matching each phase of PCA-07 to its main task. The order follows the threats: stability, then the cause, then the brain, then the outlook.",
  parts=[
    ('a', "**Immediate: ABCD.** Airway, breathing, circulation and disability: secure oxygenation, ventilation and pressure before anything else."),
    ('b', "**Early: identify and treat the cause.** ECG, echo, angiography or CT (PCA-13, PCA-15)."),
    ('c', "**Intermediate: TH/TTM.** Therapeutic hypothermia, now temperature control at 32–37.5 °C for at least 36 hours (AHA 2025) or fever prevention ≤37.5 °C for 36–72 hours (ERC–ESICM 2025); see CVS07B."),
    ('d', "**Recovery: decooling, prognostication, supportive care.** Controlled rewarming, then multimodal prognosis from 72 hours."),
    ('e', "**Rehabilitation: physical and cognitive.** Survivors often have memory, attention and mood problems even with a good neurological score."),
  ],
  mimic=[
    ("Phase vs task", "Temperature control starts as soon as possible after ROSC in practice; the card files it under ‘intermediate’ because that is where most of it runs."),
  ],
  traps=[
    ("“Temperature control waits until the intermediate phase”", "It is started as soon as the patient is not following commands and runs through the intermediate phase."),
  ],
  decode=[
    ("[pattern] Main task of the early phase", "Identify and treat the cause of the arrest."),
  ],
  punch="Each phase has one task: stabilise, find the cause, protect the brain with temperature control, then rewarm and prognosticate, then rehabilitate.",
)

L['PCA-09'] = dict(
  sub="Post-arrest care → Immediate post-ROSC algorithm",
  step=4,
  intro="Step 4 is the first minutes after ROSC. The card follows the AHA adult post-arrest algorithm, with two parallel branches: the ECG decides on the cath lab, the conscious level decides on temperature control. The one bank question tests the second branch.",
  parts=[
    ('a', "**Step 2: optimise ventilation and oxygenation — SpO₂ 90–98% (PaO₂ 60–105 mmHg; avoid hypoxaemia and hyperoxia), consider an advanced airway, waveform capnography, do not hyperventilate.** Hypoxaemia extends the ischaemic injury; very high PaO₂ feeds free-radical injury. Capnography confirms tube position and guards against hyperventilation, which constricts cerebral vessels and raises intrathoracic pressure."),
    ('b', "**Step 3: treat hypotension (SBP <90 mmHg) with an IV/IO bolus, a vasopressor infusion and a search for treatable causes.** The brain after arrest has lost autoregulation, so its flow follows pressure. AHA 2025 frames the target as MAP at least 65 mmHg rather than an SBP threshold (PCA-17)."),
    ('c', "**Step 4: 12-lead ECG — STEMI or high suspicion of AMI → yes: step 5, coronary reperfusion.** ST elevation after ROSC means an occluded artery until proved otherwise, and angiography is emergent whether or not the patient is awake (PCA-18)."),
    ('d', "**Step 6: follows commands? No → step 7, targeted temperature management.** Not following commands is the marker of brain injury, and it is the only entry criterion: rhythm and cause do not matter (AHA 2025, COR 1). Temperature is now held at 32–37.5 °C for at least 36 hours."),
    ('e', "**Yes at step 6 → step 8, advanced critical care.** A patient who follows commands has no brain injury to protect with temperature control but still needs the cause treated and the organs supported."),
  ],
  mimic=[
    ("Coronary branch vs temperature branch", "They run in parallel: a comatose STEMI patient gets both, an awake STEMI patient gets the cath lab only, a comatose patient without STEMI gets temperature control only."),
  ],
  traps=[
    ("“Haemodynamically stable and VF, so no further intervention”", "Comatose after ROSC means temperature control regardless of rhythm or stability."),
    ("“Temperature control only after VF”", "AHA 2025 applies it to all comatose adults, any rhythm, any location."),
  ],
  decode=[
    ("VF arrest, ROSC, comatose, haemodynamically stable: modality to consider? [Marrow]", "Targeted temperature management: not following commands is the trigger."),
    ("[pattern] Post-ROSC STEMI, awake and following commands", "Emergent angiography; no temperature control needed."),
  ],
  punch="After ROSC two questions run side by side: ST elevation sends the patient to the cath lab, and not following commands sends him to temperature control, whatever the rhythm or the cause.",
)

L['PCA-10'] = dict(
  sub="Post-arrest care → Post-ROSC algorithm → Doses",
  step=4,
  intro="Step 4 continues with the numbers in the algorithm’s dose box. These come from the older AHA post-arrest algorithm (the 2010/2015 version, with PETCO₂ 35–40 and dopamine); later versions moved to PaCO₂ 35–45 mmHg, and the 2025 algorithm keeps the targets but no longer prints a dose panel.",
  parts=[
    ('a', "**Ventilation: start at 10 breaths/min and titrate to PETCO₂ 35–40 mmHg; avoid excessive ventilation.** Ten breaths a minute is a normal rate for an adult. AHA 2025 states the target as PaCO₂ 35–45 mmHg on a blood gas, because PETCO₂ underestimates PaCO₂ when dead space is high after arrest."),
    ('b', "**FiO₂: 100% until SpO₂ reads reliably, then titrate to the minimum necessary for SpO₂ 90–98% (PaO₂ 60–105 mmHg).** Start high because a falsely reassuring or absent oximeter reading may hide hypoxaemia; come down because hyperoxia is linked to worse outcome in observational data."),
    ('c', "**IV bolus: 1–2 L normal saline or lactated Ringer’s.** The old fixed bolus; current practice gives fluid only when the patient is volume-responsive (PCA-17), because the stunned heart tolerates fluid poorly."),
    ('d', "**Adrenaline 0.1–0.5 mcg/kg/min (7–35 mcg/min for 70 kg).** Inotrope and vasoconstrictor; it raises myocardial oxygen use and is associated with more arrhythmias than noradrenaline."),
    ('e', "**Dopamine 5–10 mcg/kg/min.** The only drug in the box on a different scale; little used now because of arrhythmias."),
    ('f', "**Noradrenaline 0.1–0.5 mcg/kg/min (7–35 mcg/min for 70 kg).** Same range as adrenaline; the usual first vasopressor in practice, although AHA 2025 names no preferred agent (2b)."),
  ],
  mimic=[
    ("PETCO₂ vs PaCO₂ targets", "PETCO₂ 35–40 (old dose box) vs PaCO₂ 35–45 mmHg (AHA 2025 and ERC–ESICM): use PaCO₂ when a gas is available."),
  ],
  traps=[
    ("“Dopamine shares the adrenaline/noradrenaline range”", "Dopamine is 5–10 mcg/kg/min; the other two are 0.1–0.5."),
  ],
  decode=[
    ("[pattern] Post-ROSC noradrenaline dose range", "0.1–0.5 mcg/kg/min, the same as adrenaline."),
  ],
  punch="Ventilate at 10 a minute to normocapnia, cut oxygen to the least that keeps SpO₂ 90–98%, and remember that adrenaline and noradrenaline share 0.1–0.5 mcg/kg/min while dopamine is 5–10.",
)

L['PCA-11'] = dict(
  sub="Post-arrest care → Reversible causes of arrest (H’s and T’s)",
  step=4,
  intro="Step 4 includes the search for a cause that is still active. The H’s and T’s are the reversible causes; if one is missed, the patient arrests again.",
  parts=[
    ('a', "**H’s: hypovolaemia, hypoxia, hydrogen ion (acidosis), hypo/hyperkalaemia, hypothermia.** Each stops the heart by a different route: no preload, no oxygen, depressed contractility and vasoplegia, membrane instability, or cold. Each has a direct treatment: fluid or blood, oxygen and ventilation, bicarbonate or ventilation, calcium and potassium shifting or replacement, rewarming."),
    ('b', "**T’s: tension pneumothorax, cardiac tamponade, toxins, pulmonary thrombosis, coronary thrombosis.** Tension and tamponade are obstructive: decompress or drain. PE may need thrombolysis; coronary thrombosis needs PCI (PCA-18). ERC groups the same list as four H’s and four T’s, with hyperthermia added to hypothermia."),
  ],
  mimic=[
    ("PEA from tamponade vs PE on echo", "Tamponade: effusion with RV diastolic collapse; PE: dilated RV with a small LV and no effusion."),
  ],
  traps=[
    ("“Hypoglycaemia is one of the five H’s”", "It is not in the current AHA list (the 2010 list of six H’s included it), although glucose is checked in every arrest."),
  ],
  decode=[
    ("[pattern] Which of these is not a reversible cause of arrest?", "Look for the odd one out against the five H’s and five T’s."),
  ],
  punch="The five H’s and five T’s are the causes that will restart the arrest unless they are found and treated.",
)

L['PCA-12'] = dict(
  sub="Post-arrest care → ERC–ESICM 2021 algorithm → Immediate treatment targets",
  step=4,
  intro="Step 4 seen from the European side. The ERC–ESICM 2021 post-resuscitation algorithm gives the immediate targets on this card; the 2025 update and AHA 2025 changed three of them, so the source named in a stem decides the number.",
  parts=[
    ('a', "**Airway and breathing: SpO₂ 94–98%, advanced airway, waveform capnography, ventilate to normocapnia.** ERC keeps 94–98% in 2025 (PaO₂ 75–100 mmHg); AHA 2025 accepts 90–98%. Normocapnia is PaCO₂ 35–45 mmHg in both."),
    ('b', "**Circulation: 12-lead ECG, reliable IV access, aim for SBP >100 mmHg, crystalloid to restore normovolaemia, intra-arterial BP monitoring, consider vasopressor/inotrope.** ERC–ESICM 2025 states ‘SBP >100 mmHg or MAP >60–65 mmHg’; AHA 2025 says MAP at least 65. SBP >100 is the ERC number, SBP <90 the old AHA trigger (PCA-09)."),
    ('c', "**Temperature control: constant 32–36 °C, sedation, control shivering.** This was the 2021 target. ERC–ESICM 2025 replaced it with active fever prevention (≤37.5 °C) for 36–72 hours, without actively rewarming patients who are mildly hypothermic; AHA 2025 says 32–37.5 °C for at least 36 hours. The change followed TTM2, which found no benefit of 33 °C over fever prevention (CVS07B)."),
  ],
  mimic=[
    ("ERC vs AHA oxygen target", "ERC 94–98% (PaO₂ 75–100); AHA 90–98% (PaO₂ 60–105). Both avoid hypoxaemia and hyperoxia."),
  ],
  traps=[
    ("“32–36 °C is still the ERC target”", "ERC–ESICM 2025 targets fever prevention ≤37.5 °C instead."),
  ],
  decode=[
    ("[pattern] ERC post-ROSC SBP and SpO₂ targets", "SBP >100 mmHg (or MAP >60–65 in 2025); SpO₂ 94–98%."),
  ],
  punch="ERC’s immediate targets are SpO₂ 94–98%, normocapnia and SBP over 100; the constant 32–36 °C of 2021 is now fever prevention at 37.5 °C or below.",
)

L['PCA-13'] = dict(
  sub="Post-arrest care → ERC–ESICM 2021 algorithm → Diagnostic pathway",
  step=5,
  intro="Step 5 asks why the heart stopped. The ERC pathway first asks whether the cause is likely cardiac, because that decides between the cath lab and the CT scanner.",
  parts=[
    ('a', "**First branch: likely cardiac cause?** The history (chest pain, known coronary disease), the rhythm (VF suggests cardiac) and the ECG decide."),
    ('b', "**If yes: ST elevation on the 12-lead ECG? Yes → coronary angiography ± PCI; no → consider coronary angiography ± PCI.** ST elevation predicts an acute occlusion. Without it, an occlusion is still possible, so angiography is considered rather than excluded; COACT and TOMAHAWK later showed that emergent angiography gives no advantage over a delayed one in stable patients without ST elevation (PCA-18)."),
    ('c', "**If no: consider CT brain and/or CTPA.** Subarachnoid haemorrhage and pulmonary embolism are the non-cardiac causes that change treatment immediately. ERC–ESICM 2025 now suggests a dual-phase whole-body CT including CTPA at admission when a non-cardiac cause is suspected or angiography shows no culprit."),
    ('d', "**Cause identified → admit to ICU; not identified → back to CT brain and/or CTPA; non-cardiac cause → treat it, then ICU.** The loop prevents a patient reaching ICU with no cause found when imaging has not been done."),
  ],
  mimic=[
    ("Cardiac with STE vs without", "With STE: angiography emergent. Without: considered, usually delayed unless shock, recurrent arrhythmia or ongoing ischaemia."),
  ],
  traps=[
    ("“No ST elevation excludes a coronary cause”", "It downgrades angiography from mandatory to considered; it does not exclude occlusion."),
  ],
  decode=[
    ("[pattern] Post-ROSC, likely non-cardiac cause: investigation?", "CT brain and/or CT pulmonary angiography."),
  ],
  punch="If the cause looks cardiac, ST elevation sends the patient to the cath lab and its absence makes angiography a consideration; if it does not, CT of the brain and pulmonary arteries looks for haemorrhage and embolism.",
)

L['PCA-14'] = dict(
  sub="Post-arrest care → ERC–ESICM 2021 → ICU management bundle",
  step=6,
  intro="Step 6 is the ICU. The ERC–ESICM 2021 bundle has seven points, each aimed at one part of the syndrome; two of its numbers (temperature target and duration) changed in 2025.",
  parts=[
    ('a', "**Temperature control: constant 32–36 °C for at least 24 h; prevent fever for at least 72 h.** The 2021 target. AHA 2025: 32–37.5 °C for at least 36 h; ERC–ESICM 2025: prevent fever (≤37.5 °C) for 36–72 h, no active rewarming of mild hypothermia. Fever prevention is the part all versions keep, because fever is linked to worse brain outcome."),
    ('b', "**Maintain normoxia and normocapnia; protective ventilation.** Hypocapnia constricts cerebral vessels in a brain that already has too little flow; low tidal volumes protect lungs injured by aspiration and reperfusion."),
    ('c', "**Avoid hypotension.** MAP at least 65 mmHg (AHA 2025) or >60–65 (ERC–ESICM 2025)."),
    ('d', "**Echocardiography.** To measure the myocardial stunning and separate cardiogenic from distributive shock (PCA-03)."),
    ('e', "**Maintain normoglycaemia.** Both hypo- and hyperglycaemia worsen brain injury; ERC 2025 says ‘standard glucose protocols’, AHA 2025 says avoid <70 and >180 mg/dL."),
    ('f', "**Diagnose and treat seizures: EEG, sedation, anti-epileptic drugs.** Many seizures are non-convulsive and are seen only on EEG (PCA-19)."),
    ('g', "**Delay prognostication for at least 72 h.** Sedatives, cooling and early unreliable signs can make a recoverable patient look hopeless; premature withdrawal is the main avoidable cause of death."),
  ],
  mimic=[
    ("2021 vs 2025 temperature numbers", "2021: 32–36 °C for ≥24 h then no fever to 72 h. 2025: AHA 32–37.5 °C ≥36 h; ERC fever prevention ≤37.5 °C for 36–72 h."),
  ],
  traps=[
    ("“Temperature control for 24 hours is enough”", "AHA 2025 asks for at least 36 hours."),
  ],
  decode=[
    ("[pattern] Minimum time before neuroprognostication", "At least 72 hours (after ROSC in ERC; after normothermia and stopping sedation in AHA)."),
  ],
  punch="The ICU bundle is temperature control, normoxia and normocapnia, no hypotension, echo, normoglycaemia, seizure treatment and no prognosis before 72 hours; only the temperature numbers changed in 2025.",
)

L['PCA-15'] = dict(
  sub="Post-arrest care → Finding the cause → Diagnostic work-up",
  step=5,
  intro="Step 5 continues with the full work-up. Each test answers one of the H’s and T’s (PCA-11) or measures the brain injury.",
  parts=[
    ('a', "**History, physical examination (ABC) and neurological examination; the neurological examination looks at the GCS, especially the motor score, asymmetry and brainstem reflexes, to identify the cause, the likely course and the need for neurological intervention.** The motor score is the most reliable part of the GCS in an intubated patient; asymmetry suggests a structural cause such as haemorrhage rather than global hypoxia."),
    ('b', "**Laboratory: ABG, glucose, CBC, electrolytes, toxic screen.** Potassium, acidosis and glucose are treatable causes; the toxic screen looks for overdose."),
    ('c', "**Tests: ECG, echo, chest X-ray, ultrasound, EEG.** ECG for ischaemia, echo for LV function, RV dilatation and effusion, ultrasound for pneumothorax and bleeding, EEG for non-convulsive seizures."),
    ('d', "**CT brain and CT pulmonary angiography.** For haemorrhage and PE, the non-cardiac causes that change management immediately (PCA-13)."),
  ],
  mimic=[
    ("Focal vs global neurological signs", "Focal or asymmetric signs suggest a primary brain cause (bleed, stroke); symmetrical depression suggests hypoxic-ischaemic injury."),
  ],
  traps=[
    ("“Early neurological examination predicts outcome”", "It identifies the cause and guides care; prognostic weight comes only after 72 hours."),
  ],
  decode=[
    ("[pattern] Which part of the GCS matters most after ROSC?", "The motor score."),
  ],
  punch="The work-up looks for the reversible cause with labs, ECG, echo and CT, and grades the brain with the GCS motor score and EEG.",
)

L['PCA-16'] = dict(
  sub="Post-arrest care → ICU → Respiratory targets",
  step=6,
  intro="Step 6 begins with the lungs and their effect on the brain. The two Grand Test questions on this card were answered by everyone: what to avoid during temperature control is hypoxia, hyperventilation and fever together.",
  parts=[
    ('a', "**Airway; stomach decompression (NG/OG tube).** Bag-mask ventilation during CPR fills the stomach with air; decompressing it reduces aspiration and splinting of the diaphragm."),
    ('b', "**Lung-protective ventilation.** Low tidal volume (about 6–8 mL/kg predicted body weight) because aspiration and reperfusion injure the lung and ARDS is common (PCA-03)."),
    ('c', "**PaCO₂ 35–45 mmHg.** In AHA 2025 and ERC–ESICM 2025. Hypocapnia constricts cerebral vessels and cuts flow to an ischaemic brain; hypercapnia raises ICP. CO₂ is checked on a blood gas rather than trusted to the capnograph, and it is checked often during cooling, because lower temperature cuts CO₂ production and an unchanged ventilator setting then drifts the patient into hypocapnia."),
    ('d', "**Saturation 90–98% (PaO₂ 60–105 mmHg; AHA 2025).** ERC keeps 94–98% (PaO₂ 75–100). The BOX trial’s two oxygen targets (PaO₂ 68–75 vs 98–105 mmHg) gave the same outcome, so the safe zone is broad; the danger is at the extremes."),
    ('e', "**Avoid hyperventilation and hyperoxia.** Hyperventilation: cerebral vasoconstriction plus higher intrathoracic pressure, less venous return and lower output. Hyperoxia: more free-radical injury in freshly reperfused tissue. Hypoxia is avoided too, because it repeats the original insult."),
  ],
  mimic=[
    ("Hyperventilation after ROSC vs in raised ICP", "Short-term hyperventilation may be used as a bridge in herniation, but after cardiac arrest the brain is short of flow, so it is avoided."),
  ],
  traps=[
    ("“Only fever matters during TTM”", "Hypoxia, hyperventilation and fever all worsen brain injury; the answer is ‘all of the above’ (100% right)."),
    ("“Maximise oxygen to protect the brain”", "Hyperoxia is harmful; titrate to the lowest FiO₂ that keeps saturation in range."),
  ],
  decode=[
    ("Post-arrest patient on TTM: what should be avoided — fever, hypoxia, hyperventilation? [DocT GT ×2]", "All of the above (100% right)."),
    ("[pattern] Post-ROSC PaCO₂ target", "35–45 mmHg, normocapnia."),
  ],
  punch="Ventilate to normal CO₂ and normal oxygen: hyperventilation starves the brain of flow, hyperoxia adds free-radical injury and hypoxia repeats the arrest, so all three are avoided along with fever.",
)

L['PCA-17'] = dict(
  sub="Post-arrest care → ICU → Haemodynamic targets",
  step=6,
  intro="Step 6 continues with pressure. The brain after arrest has lost autoregulation (PCA-03), so a perfusing pressure is a brain treatment. The only Grand Test question on this card was answered right by 24%, because DocT keyed a MAP higher than any guideline recommends.",
  parts=[
    ('a', "**Arterial and central lines.** Beat-to-beat pressure because vasopressors are titrated minute to minute; central access for the vasopressors and ScvO₂."),
    ('b', "**MAP >65, SBP >90, urine output 0.5–1 mL/kg/h, to optimise cerebral perfusion.** AHA 2025 confirms MAP at least 65 mmHg (COR 1); ERC–ESICM 2025 says MAP >60–65 or SBP >100. A higher target has been tested and did not help: BOX (2022) compared MAP 63 and 77 mmHg in comatose survivors and found no difference in death or severe disability."),
    ('c', "**12-lead ECG to rule out MI; echo and critical care ultrasound screening.** Echo shows whether shock is cardiogenic (poor LV), distributive (good LV, low SVR) or obstructive (tamponade, RV dilatation)."),
    ('d', "**Fluid only if volume-responsive (isotonic crystalloid in small boluses, reassessed on echo); no fixed 20–30 mL/kg load.** The stunned ventricle cannot handle large volumes, and extra fluid worsens the lung injury."),
    ('e', "**Vasopressors: noradrenaline first (ERC–ESICM 2025; AHA 2025: no specific agent proven, 2b); dobutamine if the stunned pump is the problem; mechanical support: IABP, ECMO, Impella; immunomodulation.** ERC–ESICM 2025 actually says ‘fluids, noradrenaline and/or dobutamine’ according to need without ranking a first agent (FLAGS); noradrenaline is the usual first choice in practice. AHA 2025 says temporary mechanical support should not be used routinely (3: No Benefit) but may be considered in selected refractory cardiogenic shock (2b); see CS-49 to CS-52."),
  ],
  mimic=[
    ("Post-arrest MAP target vs TBI or spinal cord targets", "Post-arrest: at least 65 mmHg. Higher MAP goals (85–90 mmHg) belong to acute spinal cord injury, and TBI is managed by cerebral perfusion pressure; neither applies to post-arrest care."),
  ],
  traps=[
    ("“Comatose, on TTM, MAP 65 despite fluids: increase MAP to >80 mmHg” (DocT key, 24% right)", "No guideline supports this: AHA 2025 and ERC–ESICM target MAP ≥65, and BOX found no benefit from a higher MAP. The DocT key is wrong; if the stem is DocT’s, pick >80, but on a guideline-framed question keep ≥65."),
    ("“Rewarm rapidly” or “stop TTM because of STEMI”", "Rapid rewarming causes rebound hypotension and fever; STEMI and temperature control run together (PCA-18)."),
    ("“Delay reperfusion until awakening”", "STEMI goes to the cath lab regardless of coma."),
  ],
  decode=[
    ("Comatose post-arrest on TTM, day 1, MAP 65 despite fluids: next step? [DocT GT, 24%]", "DocT key: increase MAP >80. Guideline answer: MAP ≥65 is already the target (FLAGS)."),
    ("[pattern] Post-ROSC MAP target", "At least 65 mmHg (AHA 2025); >60–65 (ERC–ESICM 2025)."),
  ],
  punch="After arrest the pressure target exists for the brain, and it is a MAP of at least 65: BOX found nothing gained by pushing to 77, so a key that demands over 80 is DocT’s, not the guideline’s.",
)

L['PCA-18'] = dict(
  sub="Post-arrest care → Arrhythmias and coronary angiography",
  step=5,
  intro="Step 5 returns to the commonest cause, the coronary artery. The two bank questions both turn on one rule: ST elevation after ROSC goes to the cath lab now, whatever the neurological state. Half the Grand Test cohort chose to wait.",
  parts=[
    ('a', "**Arrhythmias: anti-arrhythmics, correct electrolyte imbalance, treat coronary ischaemia, toxin management, temperature correction.** Post-arrest arrhythmias are mostly secondary, so the cause is treated: potassium and magnesium, ischaemia (reperfusion), drugs, and temperature (cooling causes bradycardia; rewarming and fever cause tachyarrhythmias)."),
    ('b', "**Emergent angiogram ± PCI (AHA 2025): persistent ST elevation, comatose or not (COR 1); reasonable without STE if cardiogenic shock, recurrent ventricular arrhythmias or ongoing ischaemia (2a); otherwise not emergent, no benefit over a delayed strategy (3; COACT, TOMAHAWK).** In COACT (552 patients with shockable arrest and no ST elevation) 90-day survival was 64.5% with immediate and 67.2% with delayed angiography; TOMAHAWK found no benefit either. ERC–ESICM 2025 agrees: emergent cath lab for persistent STE, otherwise delay unless acute occlusion is likely."),
    ('c', "**TTM can be initiated during the angiogram.** The two treatments are independent and should not delay each other."),
    ('d', "**ACS medical management should be started in appropriate patients.** Antiplatelets, anticoagulation and statin as for any ACS, adjusted for bleeding risk from CPR and for cooling."),
  ],
  mimic=[
    ("PCI vs thrombolysis after ROSC with STEMI", "Primary PCI is preferred; prolonged or traumatic CPR is a relative contraindication to fibrinolysis, which is kept for when PCI cannot be done in time."),
  ],
  traps=[
    ("“Wait for a favourable neurological prognosis, or correct the metabolic derangement first” (50% right)", "Coma is not a reason to delay: AHA 2025 recommends emergent angiography for STE regardless of coma (COR 1). Metabolic problems are corrected in the lab, not before."),
    ("“Angiography within 24–48 hours”", "That is the timing for patients without STE; with STE it is emergent."),
    ("“Thrombolysis” for post-ROSC STEMI", "Primary PCI is the answer when available; CPR raises the bleeding risk of lysis."),
    ("“No obvious cause, so emergent angiography”", "No longer an indication without STE, shock, recurrent arrhythmia or ischaemia (COACT, TOMAHAWK)."),
  ],
  decode=[
    ("VF arrest after snow shovelling, ROSC, mental status not determinable, post-ROSC ECG shown: timing of angiography? [DocT GT, 50%]", "Urgently post-ROSC (the ECG shows STEMI)."),
    ("VF arrest, ROSC, anterior ST elevation, haemodynamically unstable: next step? [NEET 2025 recall]", "Immediate coronary angiography with PCI."),
    ("[pattern] Comatose after shockable arrest, no STE, stable: emergency angiography?", "No: delayed or selective strategy is as good."),
  ],
  punch="Persistent ST elevation after ROSC means the cath lab now, comatose or not, with temperature control started on the table; without ST elevation angiography waits unless there is shock, recurrent arrhythmia or ongoing ischaemia.",
)

L['PCA-19'] = dict(
  sub="Post-arrest care → ICU → Seizures and myoclonus",
  step=6,
  intro="Step 6 includes the brain’s electrical response to hypoxic injury. Both Grand Test questions here are about the comatose patient with seizures or myoclonus: what it means for prognosis, and what to do when an EEG pattern persists.",
  parts=[
    ('a', "**Seizures occur in 33% of comatose patients after ROSC; myoclonus is more common, 20–25%.** The two figures come from the ERC post-resuscitation text (2015, repeated in 2021): seizures in about one-third of patients who stay comatose, and myoclonus the commonest type, in 18–25%. So 20–25% is a subset of the 33%; ‘more common’ means the commonest form, not more frequent than seizures overall. ILCOR 2008 gives 10–40% for seizures, myoclonus or both in comatose survivors. Myoclonus is the commonest visible form, while many other seizures are seen only on EEG."),
    ('b', "**Both are poor prognostic markers; cerebral oedema is a consequence of hypoxic brain injury.** Early generalised myoclonus, especially status myoclonus within 72 hours with a burst-suppression EEG, reflects severe cortical injury; ERC–ESICM 2025 lists status myoclonus ≤72 h among its poor-outcome predictors. It is never used alone (multimodal prognosis), and late action myoclonus in an awakening patient (Lance–Adams syndrome) has a good outlook."),
    ('c', "**Seizures: no sufficient evidence for prophylaxis; EEG to monitor treatment effects; levetiracetam or sodium valproate first line.** AHA 2025 and ERC–ESICM 2025 both advise against routine prophylaxis (no trial benefit); ERC–ESICM names levetiracetam or sodium valproate as first line, with sedatives such as propofol, and AHA 2025 asks for clinical seizures to be treated without naming an agent. TELSTAR (2022) found that aggressively suppressing rhythmic and periodic EEG patterns did not change the poor outcome (about 90% in both arms), so treating the EEG does not rescue the prognosis."),
    ('d', "**Myoclonus: phenytoin is inefficient; use propofol, sodium valproate, clonazepam, levetiracetam.** Post-anoxic myoclonus is cortical and subcortical, not the type phenytoin controls. AHA 2025: get an EEG, and do not treat myoclonus that has no EEG correlate (3: No Benefit); ERC–ESICM 2025 suggests a wake-up trial when the EEG background is benign."),
  ],
  table=dict(title="Two kinds of post-anoxic myoclonus",
    head=["", "Early status myoclonus", "Lance–Adams syndrome"],
    rows=[["When", "Within 24–72 h, patient comatose", "Days to weeks, patient awakening"],
          ["Type", "Generalised, often face and trunk, repetitive", "Action myoclonus on voluntary movement"],
          ["EEG", "Burst suppression or generalised discharges", "Background reactive, often near normal"],
          ["Outlook", "Poor (with other predictors)", "Good for survival; disability from the myoclonus"]]),
  mimic=[
    ("Myoclonic status vs Lance–Adams", "Comatose and early with a malignant EEG vs awake and later with action-triggered jerks."),
    ("Seizure vs shivering under TTM", "Shivering is rhythmic muscle activity without EEG change and stops with warming of the skin, magnesium or deeper sedation."),
  ],
  traps=[
    ("“EEG activity means a high chance of recovery”", "Rhythmic, malignant EEG activity with myoclonus points the other way (84% right)."),
    ("“Oxcarbazepine and topiramate are the only proven agents”", "No drug has proven benefit; first line is levetiracetam or valproate, with propofol and clonazepam."),
    ("“Lumbar puncture is essential”", "Post-anoxic myoclonus after a long arrest needs EEG and multimodal assessment, not an LP."),
    ("“Pattern persists after propofol and valproate: wait, or stop sedation” (69% right)", "Seizure activity persisting on two agents is escalated by adding another, levetiracetam; waiting or withdrawing sedation leaves it running. TELSTAR shows that suppressing the EEG pattern does not improve outcome, so escalation treats the seizure, not the prognosis."),
    ("“Phenytoin for post-anoxic myoclonus”", "Ineffective."),
  ],
  decode=[
    ("Alcohol-using woman after OHCA and 24 h hypothermia, rapid face and limb twitching after rewarming, EEG rhythmic activity: most true? [DocT GT, 84%]", "Post-anoxic myoclonic status epilepticus indicates a poor prognosis."),
    ("Comatose post-arrest, malignant epileptiform EEG persisting 90 min on propofol and valproate: next step? [DocT GT, 69%]", "Add levetiracetam."),
    ("[pattern] Seizure prophylaxis after ROSC?", "Not recommended."),
  ],
  punch="Seizures and early myoclonus are common after arrest and signal severe injury; there is no prophylaxis, levetiracetam or valproate with propofol come first, phenytoin does not work for myoclonus, and myoclonus without an EEG correlate is not treated.",
)

L['PCA-20'] = dict(
  sub="Post-arrest care → ICU → General care",
  step=6,
  intro="Step 6 ends with the routine ICU care that the post-arrest patient shares with every ventilated patient, plus the few things that are different because of cooling and the brain.",
  parts=[
    ('a', "**FASTHUGS BID principle.** The daily ICU checklist: feeding, analgesia, sedation, thromboprophylaxis, head of bed up, ulcer prophylaxis, glucose control, spontaneous breathing trial, bowel care, indwelling catheter removal, de-escalation of antibiotics."),
    ('b', "**Short-acting sedatives and opioids; avoid neuromuscular blocking drugs routinely.** Short-acting drugs clear quickly so the neurological examination at 72 hours is not confounded. ERC–ESICM 2025 does not recommend systematic paralysis, except for severe hypoxaemia in ARDS or shivering that does not respond to other steps; paralysis also hides seizures."),
    ('c', "**Stress ulcer prophylaxis routinely; DVT prophylaxis.** Stress ulcer prophylaxis especially with coagulopathy (ERC–ESICM 2025); DVT prophylaxis follows general ICU practice."),
    ('d', "**Blood glucose 7.8–10 mmol/L (140–180 mg/dL).** The NICE-SUGAR range used in ICU. AHA 2025 says avoid <70 and >180 mg/dL; ERC–ESICM 2025 says use standard ICU protocols. Hypoglycaemia is the greater danger to an injured brain, and insulin needs change with cooling and rewarming."),
    ('e', "**Enteral feeding at low rates (trophic) during TTM, increased after rewarming if indicated.** Cooling slows gastric emptying and gut motility, and the gut was ischaemic; ERC–ESICM 2025 suggests trophic gastric feeding, increased as tolerated."),
    ('f', "**No role for prophylactic antibiotics routinely.** Trials of prophylaxis reduced early pneumonia but did not improve survival; ERC–ESICM 2025 advises against routine use with a low threshold to treat suspected pneumonia, and AHA 2025 calls the benefit uncertain."),
  ],
  mimic=[
    ("Routine vs not routine", "Routine: stress ulcer and DVT prophylaxis. Not routine: paralysis, antibiotics and steroids."),
  ],
  traps=[
    ("“Tight glucose control (4.4–6.1 mmol/L) protects the brain”", "Tight control causes hypoglycaemia; moderate control (up to 10 mmol/L) is the target."),
    ("“Give prophylactic antibiotics to all post-arrest patients”", "Not recommended routinely."),
  ],
  decode=[
    ("[pattern] Post-arrest glucose target", "7.8–10 mmol/L (140–180 mg/dL), avoiding hypoglycaemia."),
  ],
  punch="General care is the standard ICU bundle with short-acting sedation, ulcer and DVT prophylaxis, glucose 7.8–10 mmol/L and trophic feeding while cooled, and no routine paralysis or prophylactic antibiotics.",
)

FLAGS = {}
FLAGS['PCA-01'] = "Card figures do not match Goto 2016 (JAHA, n 17,238): after 20 min CPC 1–2 is 1.9% (card 0.8%); after 30 min survival is 0.8% (card 0.4%) and CPC 1–2 is 0.4% (card 0%). The ‘1 minute’ row (36.8/21.8%) is the cohort’s overall rate. Watch line (‘neurological outcome reaches zero at 30 minutes’) is therefore wrong; >99% of good outcomes by 35 min."
FLAGS['PCA-04'] = "Card gives the AHA 2020 adult OHCA chain; AHA 2025 uses a single chain for all ages and settings with essentially the same six links. Not wrong for 2020."
FLAGS['PCA-10'] = "Dose box is from the older AHA algorithm (2010/2015 version; 2020 already used PaCO₂ 35–45) (PETCO₂ 35–40, fixed 1–2 L bolus, infusion doses); the AHA 2025 algorithm has no dose panel and targets PaCO₂ 35–45 and MAP ≥65. Card is dated, not wrong as a quotation."
FLAGS['PCA-17'] = "Card says ‘noradrenaline first (ERC–ESICM 2025)’; ERC–ESICM 2025 says ‘maintain perfusion with fluids, noradrenaline and/or dobutamine’ by need, without ranking a first agent. Card ‘SBP >90’ differs from ERC 2025 ‘SBP >100 or MAP >60–65’. DocT GT8 key ‘increase MAP >80’ is not guideline-supported (cross line agrees)."
FLAGS['PCA-19'] = "Card a wording: ‘myoclonus is more common: 20–25%’ reads as if myoclonus exceeds the 33% for seizures. The source (ERC 2015/2021) says seizures occur in about one-third of comatose survivors and myoclonus is the MOST common type (18–25%), i.e. a subset. Figures right, wording misleading; the card’s watch line calling it a contradiction is itself wrong."
