# CVS08C — Explain v3 ("Learn" depth): BLS & ACLS III — drugs and special situations. Airway ladder, ventilation and oxygen during CPR, capnography, coronary perfusion
# targets, epinephrine, antiarrhythmics, drugs of uncertain benefit, atropine, the resuscitation team, arrest in pregnancy (principles, interventions, resuscitative delivery),
# the LVAD algorithm, asthma/hypothermia/hyperthermia, the 2025 post-arrest algorithm, the ACS algorithm and the stroke time goals.
# No mnemonics or hooks. Driven by qpack/CVS08C.md (49 question links; ACLS-55 environmental emergencies asked 11 times, ACLS-45 epinephrine and ACLS-52 maternal interventions 6 each,
# ACLS-41 and ACLS-53 four each). ACLS-49, -50, -54, -56 and -58 have no linked question and get short explanations with [pattern] decode items.
# cvs_cardlayer.json lines, cross notes and the ACLS-42 fix were read and used (the fix — no intra-arrest saturation target — is already in the card).
# Checked online on 19 Nov 2026:
#  - AHA 2025 Part 9, Adult ALS (cpr.heart.org): maximal feasible FiO2 during CPR (2b); use arterial pressure or ETCO2 to monitor CPR quality when feasible (2b), supportive text ‘at least 10 mm Hg,
#    ideally 20 mm Hg or greater’, and ‘inadequate adult data to suggest any specific [diastolic] pressure’; ETCO2 >10 mm Hg not reached after 20 min of ALS in the intubated patient may be one
#    factor in stopping (2b), never in the non-intubated (3: Harm); SGA acceptable where ETI success is low (2a), either SGA or ETT (2a), bag-mask or advanced airway (2b); 1 breath every 6 s with an
#    advanced airway (2b); epinephrine recommended (1), 1 mg every 3–5 min (2a), non-shockable as soon as feasible (2a), shockable after initial defibrillation attempts fail (2a), high dose no benefit;
#    vasopressin alone or with epinephrine no advantage (3: No Benefit); amiodarone or lidocaine may be considered (2b); β-blockers, bretylium, procainamide, sotalol uncertain benefit (2b); routine
#    magnesium, calcium and bicarbonate not recommended (3: No Benefit); POCUS to find reversible causes (2b).
#  - AHA 2025 Adult BLS: head and neck trauma — jaw thrust without head extension (1), head tilt–chin lift if jaw thrust plus adjunct fail (1); OPA preferred over NPA with basal skull fracture or
#    severe coagulopathy (2a); depth at least 5 cm, avoid over 6 cm (1); rate 100–120 (2a); visible chest rise (2a), each breath over 1 s (2b); 30:2 before an advanced airway (2a).
#  - AHA 2025 adult post-cardiac arrest care algorithm (text description, cpr.heart.org): FiO2 100% until SpO2 reliable, then SpO2 about 90–98%; PCO2 35–45; MAP ≥65; 12-lead ECG, consider CT and/or
#    ultrasound; assess off sedation and neuromuscular blockade; follows commands? No/unsure → temperature control 32–37.5 °C, EEG, coronary angiography when appropriate, multimodal prognostication
#    generally ≥72 h after ROSC or normothermia; emergency cardiac intervention for persistent ST elevation, cardiogenic shock, recurrent/refractory VA, severe ischaemia.
#  - ERC–ESICM 2025 post-resuscitation care (resus.org.uk): SpO2 94–98%; MAP >60–65 mmHg, SBP >100.
#  - AHA 2025 Part 10, Special circumstances (cpr.heart.org): pregnancy — resuscitative delivery when fundal height at or above the umbilicus and no ROSC (1), preparation from recognition with the goal
#    of delivery by 5 min (1), manual left lateral uterine displacement (1), upper-limb IV/IO (2a), calcium if arrest on IV magnesium (2a); ELSO 2020: 55% survival among 42 ECLS patients; 87% 30-day
#    survival in 57 cannulated; amniotic fluid embolism: balanced massive transfusion (1), tranexamic acid (1), VA-ECMO (2a), inhaled pulmonary vasodilators (2a), no atropine without bradycardia.
#    LVAD — compressions when perfusion impaired (1); adequate perfusion = MAP >50 or PETCO2 >20 plus normal skin or capillary refill; most have no palpable pulse. Asthma — ECLS reasonable (2a),
#    volatile anaesthetics may be considered (2b), ECLS survival 83.5–100% in observational studies. Hypothermia — full resuscitation with concurrent rewarming (1), ECLS rewarming (2a), scores to
#    guide ECLS (2a; HOPE <10% predicts death, ICE >12 survival; HOPE better than K ≥12 alone), ECLS for core <28 °C without arrest (2b), defibrillate once then defer to ≥30 °C (2b), defer epinephrine
#    to ≥30 °C (2b), ECLS rewarming 1.5–5 °C/h, ETCO2 not for prognosis (3). Hyperthermia — active cooling with resuscitation (1), ice water 1–5 °C (2a), tepid 8–17 °C if none, at least 0.15 °C/min (2a),
#    stop at 38.6 °C (2a), dantrolene no benefit outside MH (3). Hyperkalaemia — IV calcium in arrest not well established (2b). Anaphylaxis — standard IM dose uncertain in arrest (2b), isotonic fluids
#    (2a), ECPR (2a). Drowning — CPR with breaths and compressions (1).
#  - AHA/ASA 2026 acute ischaemic stroke guideline (Stroke, 26 Jan 2026; emDocs and AHA news summaries): tenecteplase 0.25 mg/kg (max 25 mg) or alteplase 0.9 mg/kg within 4.5 h (1); brain imaging within
#    25 min of arrival; treat as quickly as possible.
# Second check (reviewer, 19 Nov 2026): AHA 2025 Part 11 (cpr.heart.org) — SpO2 90–98% with PaO2 60–105 mmHg (2a), temperature control 32–37.5 °C for ≥36 h, prognosis ≥72 h after normothermia;
#  RCUK/ERC 2025 ALS — diastolic ≥30 mmHg and ETCO2 ≥25 mmHg (physiology-guided CPR), adrenaline after the 3rd shock, amiodarone 300/150, lidocaine 100/50 mg; RCUK/ERC 2025 special circumstances —
#  hypothermic VF: delay further shocks after three until >30 °C, adrenaline withheld <30 °C, interval 6–10 min at 30–35 °C; RCUK/ERC–ESICM 2025 — PaO2 75–100 mmHg; AHA 2025 Part 10 — heat stroke stop
#  at 38.6 °C (2a), ELSO 55% = ECLS in 42 obstetric arrests (ECPR 29%); ACC summary of ALPS (24.4/23.7/21.0%; bystander-witnessed 27.7/27.8/22.7%); AHA news release on the 2026 AHA/ASA stroke
#  guideline (initial brain scan within 25 min of arrival; tenecteplase or alteplase within 4.5 h).
# From standard references without a fresh check (confident unless said): coronary perfusion pressure ≥15 mmHg for ROSC (Paradis 1990); ACLS bradycardia atropine 1 mg every 3–5 min, max 3 mg; PALS
# amiodarone 5 mg/kg up to 3 doses, epinephrine 0.01 mg/kg; Katz 1986/2005, Einav 2012; obstetric haemorrhage the commonest cause of maternal arrest; ESC 2023 NSTE-ACS hs-cTn 0/1 h or 0/2 h;
# NINDS 10/25/45/60 min targets; tryptase 20% + 2 rule.

SPINE = [
  ("Airway, breaths and quality feedback", "Open the airway with the least neck movement, ventilate just enough to see the chest rise, and use ETCO2 and diastolic pressure to tell you whether your compressions are making flow."),
  ("Drugs that help, and drugs that do not", "Epinephrine is the only vasopressor, timed by rhythm, amiodarone or lidocaine follow failed shocks, and almost everything else (vasopressin, magnesium, calcium, atropine) has no routine place in arrest."),
  ("The team runs the code", "Six defined roles around a leader keep compressions going, rotate the tiring compressor every 2 minutes and record every drug and pause."),
  ("Arrest in special circumstances", "Pregnancy, an LVAD, asthma and extremes of temperature change the algorithm because the cause, the circulation or the heart’s response to drugs is different."),
  ("After ROSC: stabilise, then branch", "Oxygenate to 90–98%, keep MAP 65 or more, find the cause, then ask whether the patient follows commands off sedation; that answer decides temperature control, EEG and prognostication."),
  ("Peri-arrest pathways: ACS and stroke", "Chest pain and stroke run on clocks: an ECG in 10 minutes decides reperfusion, and a scan read by 45 minutes decides lysis by 60."),
]

PRIMER = "During CPR the heart is perfused only in the release phase of each compression, by the gap between aortic diastolic and right-atrial pressure (coronary perfusion pressure); anything that raises intrathoracic pressure or interrupts compressions shrinks that gap. End-tidal CO2 during arrest is set by pulmonary blood flow, so it reads out cardiac output, not ventilation. Drugs only matter if they raise that perfusion pressure (epinephrine) or stop a recurring arrhythmia; most others were tested and dropped. CVS08A and CVS08B covered the BLS sequence and the core algorithms; this deck adds the drugs, the team, the special situations and what follows ROSC."

L = {}

L['ACLS-41'] = dict(
  sub="Cardiology → ACLS → Airway management in arrest",
  step=1,
  intro="Step 1 starts with getting air in. The airway is opened by the simplest manoeuvre that works and escalated only when needed, because every more complex device costs compression time. Four real questions test the ladder, its order with a cervical spine at risk, the weakness of bag-mask ventilation and when a supraglottic airway beats a tube.",
  parts=[
    ('a', "**Head tilt–chin lift; adjuncts OPA / NPA.** In the unconscious patient the tongue and epiglottis fall back against the posterior pharynx; lifting the mandible pulls the tongue forward. An oropharyngeal airway suits the patient with no gag (it provokes vomiting otherwise); a nasopharyngeal airway is tolerated by a semi-conscious patient. AHA 2025 prefers the OPA when a basal skull fracture or severe coagulopathy is suspected, because a nasal tube can enter the cranium or cause brisk bleeding."),
    ('b', "**Definitive airway: ETT / supraglottic airway / i-gel / Combitube.** These are the advanced airways of ACLS. Strictly, a definitive airway (the ATLS term) is a cuffed tube in the trachea; a supraglottic device sits above the cords and does not fully protect against aspiration (FLAG). For arrest outcomes the choice matters little: AHA 2025 accepts either a supraglottic airway or a tube, and prefers the supraglottic airway where intubation success is low, because it goes in faster with fewer pauses in compressions."),
    ('c', "**Ladder: compression-only CPR → mouth-to-mouth → bag-mask (basic) | supraglottic airway → tracheal intubation (advanced).** The border lies after the bag-mask: every step beyond it is a device inserted into the pharynx (supraglottic airway) or the trachea (tube). Bag-mask ventilation is the step most often done badly; its main limitation is gastric inflation, because pharyngeal pressures above about 20 cmH2O open the oesophageal sphincter, the stomach fills, the diaphragm is splinted and regurgitation follows. Slow breaths over 1 second, just enough to see the chest rise, and a two-person grip reduce it."),
    ('d', "**2025: in head and neck trauma, if the airway cannot be opened with a jaw thrust and an adjunct, a trained rescuer should open it with head tilt–chin lift.** The jaw thrust without head extension stays the first choice (class 1) because it moves the cervical spine least. But a hypoxic arrest kills in minutes, while worsening a cord injury by some neck extension is uncommon, so patency wins. The full trauma sequence the NEET recall asked is: suction first, then jaw thrust (or chin lift), then OPA/NPA, then a cuffed tube with manual in-line stabilisation, then a surgical airway if intubation fails."),
  ],
  mimic=[
    ("Advanced airway vs definitive airway", "ACLS calls any SGA or tube ‘advanced’; ATLS reserves ‘definitive’ for a cuffed tube below the cords."),
    ("Jaw thrust vs head tilt–chin lift", "Jaw thrust first in suspected spinal injury; head tilt–chin lift only when the thrust and an adjunct fail."),
  ],
  traps=[
    ("“The key limitation of bag-mask ventilation is tracheal injury or that it needs two rescuers”", "It is gastric inflation; two rescuers make it better but are not required."),
    ("“In OHCA intubation is always the preferred advanced airway”", "Where the system’s intubation success is low, a supraglottic airway is preferred; outcomes are similar."),
    ("“Advanced airway first, then suction and basic manoeuvres”", "The ladder runs from simple to complex: clear the airway, open it, add an adjunct, then a device."),
  ],
  decode=[
    ("EMS system with low intubation success — preferred advanced airway in OHCA? [DocT GT]", "Supraglottic airway."),
    ("Key limitation of bag-valve-mask ventilation? [DocT GT]", "Gastric inflation (100%)."),
    ("Correct airway sequence with cervical spine control [NEET 2025]", "Suction → jaw thrust/chin lift → OPA/NPA → cuffed ETT ± RSI or surgical airway."),
    ("Chin lift, Guedel, supraglottic device — which is not used to maintain the airway? [NEET 2025]", "None: all are used."),
  ],
  punch="Go up the ladder only as far as you need: the jaw thrust protects the neck, but a closed airway is the more urgent threat, and an SGA placed quickly beats a tube placed slowly.",
)

L['ACLS-42'] = dict(
  sub="Cardiology → ACLS → Breathing during CPR",
  step=1,
  intro="Step 1 continues with how much to breathe for the patient. The aim is enough oxygen with as little rise in intrathoracic pressure as possible, because each over-sized breath cuts the venous return that compressions depend on. Only 31% chose the right answer to the question on what protects cerebral perfusion.",
  parts=[
    ('a', "**100% FiO2 initially.** During CPR the cardiac output is a fraction of normal, so oxygen delivery is limited by flow, and the only lever left on oxygen content is a high inspired fraction. AHA 2025 says the maximal feasible FiO2 is reasonable."),
    ('b', "**Waveform capnography to confirm and monitor ET tube placement.** A sustained waveform over several breaths means CO2 is coming from the lungs; an oesophageal tube gives a few falling breaths then nothing. Seeing the tube pass the cords, chest movement and breath sounds all mislead. A chest X-ray shows depth (tip 2–5 cm above the carina) but cannot exclude oesophageal placement."),
    ('c', "**Keep the maximal feasible FiO2 throughout CPR; titrate only after ROSC (SpO2 90–98%).** There is no saturation target during arrest: pulse oximetry is unreliable without a pulse, and hypoxia is the greater danger. Hyperoxia becomes a concern only once flow returns. AHA 2025 then titrates to SpO2 90–98% with PaO2 60–105 mmHg (2020 used 92–98%); ERC–ESICM 2025 uses SpO2 94–98% with PaO2 75–100 mmHg."),
    ('d', "**EtCO2 goal: at least 10 mmHg, ideally 20 or more.** These are the values AHA 2025 quotes for adjusting compressions; ACLS-43 covers what to do when it is low."),
    ('e', "**Advanced airway in place: 1 breath every 6 seconds (10 breaths/min) with continuous chest compressions.** Before an advanced airway the ratio is 30:2, with each breath over 1 second and just enough volume to see the chest rise (about 500–600 mL). Hyperventilation raises intrathoracic pressure, which reduces venous return and so coronary and cerebral perfusion; it also lowers PaCO2, constricting cerebral vessels."),
  ],
  mimic=[
    ("Intra-arrest oxygen vs post-ROSC oxygen", "During CPR: maximal FiO2, no target. After ROSC: titrate to SpO2 90–98%."),
    ("Tube in the trachea vs tube at the right depth", "Waveform capnography confirms the first; the chest X-ray confirms the second."),
  ],
  traps=[
    ("“Deliver 10 breaths per minute” with a bag-mask (chosen often; only 31% right)", "10/min applies once an advanced airway is in; with a bag-mask it is 30:2. The answer that protects perfusion is avoiding hyperinflation."),
    ("“Increase the tidal volume to 900 mL”", "Too large: it raises intrathoracic pressure and inflates the stomach; visible chest rise is enough."),
    ("“Chest X-ray is the best way to verify the tube” (NEET 2025 key)", "The X-ray checks depth only; waveform capnography confirms tracheal placement. If capnography is offered, choose it; if the stem has already shown CO2 and asks for ‘proper position’, the keyed X-ray stands."),
    ("“Titrate oxygen to 92–98% during CPR”", "There is no intra-arrest saturation target; titration begins after ROSC."),
  ],
  decode=[
    ("Bag-mask CPR — which action best preserves cerebral perfusion? [DocT GT]", "Avoid hyperexpansion during breaths (31%)."),
    ("Intubated during CPR — ventilation rate? [DocT GT]", "1 breath every 5–6 seconds (AHA: every 6 s)."),
    ("Cords seen, colorimetric CO2 positive, breath sounds equal — best verification of proper position? [NEET 2025]", "Chest radiograph (depth); waveform capnography if offered."),
  ],
  punch="Give all the oxygen you can, but in small slow breaths: in arrest the danger is not too little ventilation but too much pressure in the chest, and capnography, not the stethoscope, tells you the tube is in the trachea.",
)

L['ACLS-43'] = dict(
  sub="Cardiology → ACLS → Capnography during CPR",
  step=1,
  intro="Step 1 ends with feedback. During arrest the CO2 reaching the alveoli depends on how much blood is pushed through the lungs, so the capnograph becomes a flow meter for compressions. Both real questions show a low or falling value and ask what to do.",
  parts=[
    ('a', "**Low or flat trace (around 5–10 mmHg) → improve chest compressions; EtCO2 reflects pulmonary blood flow and therefore compression quality.** With ventilation fixed, ETCO2 falls only when less blood reaches the lungs: a tired compressor, shallow or slow compressions, or leaning. A gradual fall from 18 to 7 with no rhythm change is the classic tiring compressor; rotate and push harder. Hyperventilation lowers ETCO2 too, which is why a constant ventilation rate is needed before reading the number."),
    ('b', "**Abrupt sustained rise (typically ≥40 mmHg) → ROSC.** When the heart restarts, output jumps and the CO2 that has built up in the tissues is washed to the lungs at once, so the value rises suddenly, often above normal. A rhythm and pulse check confirms it. A bolus of sodium bicarbonate also raises ETCO2 briefly, a known false signal."),
    ('c', "**Compression depth: good 2–2.4 inches (5–6 cm); bad <2 inches (<5 cm).** Depth sets stroke volume during CPR. Too deep (over 6 cm) adds injury without benefit. AHA 2025 keeps the rate at 100–120/min with full recoil."),
  ],
  mimic=[
    ("Falling ETCO2 in CPR vs falling ETCO2 under anaesthesia", "In arrest it means less flow (fix compressions); under anaesthesia with a pulse it can also mean hyperventilation, PE or a leak."),
  ],
  traps=[
    ("“ETCO2 8 mmHg — give bicarbonate or increase the ventilation rate”", "Bicarbonate is not routine and more breaths lower ETCO2 further; improve compressions."),
    ("“ETCO2 8 mmHg — terminate resuscitation”", "A low value alone is never a reason to stop; AHA 2025 allows ETCO2 under 10 after 20 minutes of ALS in an intubated patient only as one factor among several, and never in a non-intubated patient (ACLS-20)."),
  ],
  decode=[
    ("Intubated PEA, persistent ETCO2 8 mmHg despite correct ventilation [DocT GT]", "Reassess and improve CPR quality."),
    ("ETCO2 falling from 18 to 7 over minutes, rhythm unchanged [DocT GT]", "Reassess CPR quality (the compressor is tiring)."),
  ],
  punch="During arrest the capnograph measures flow, not breathing: a low or falling number means push better, and a sudden jump means the heart has started.",
)

L['ACLS-44'] = dict(
  sub="Cardiology → ACLS → Circulation targets during CPR",
  step=1,
  intro="Step 1 also asks how you know compressions are perfusing the heart. Both real questions ask which parameter best predicts ROSC, and only 53–58% chose coronary perfusion pressure; the rest picked numbers that are easy to see but do not reach the myocardium.",
  parts=[
    ('a', "**Monitor CPR quality via EtCO2.** ETCO2 reports flow through the lungs, and with an arterial line the diastolic pressure reports what is left for the coronaries; AHA 2025 suggests using either when feasible. Both are surrogates for coronary perfusion pressure."),
    ('b', "**EtCO2 goal >10 mmHg.** AHA 2025 text puts it as at least 10, ideally 20 or more (ACLS-42)."),
    ('c', "**Arterial diastolic BP: no adult target in AHA 2025; ERC 2025 suggests ≥30 mmHg.** The heart is perfused in the release phase, so coronary perfusion pressure is aortic diastolic minus right-atrial diastolic pressure; animal and human studies found that ROSC is rare below about 15 mmHg. The arterial diastolic pressure is its bedside proxy. AHA 2020 used ‘under 20 mmHg, improve CPR’; AHA 2025 says adult data are inadequate to set any number. ERC 2025, as a pragmatic physiology-guided approach, aims for a diastolic pressure of ≥30 mmHg with an arterial line and an ETCO2 of ≥25 mmHg."),
    ('d', "**Attach monitor / defibrillator • obtain IV/IO access • use drugs appropriately.** The shock decides shockable rhythms, so the defibrillator comes first; access follows without stopping compressions."),
  ],
  mimic=[
    ("Coronary perfusion pressure vs systolic pressure during compressions", "Systolic peaks show the push; diastolic pressure minus right-atrial pressure shows what reaches the myocardium."),
  ],
  traps=[
    ("“Systolic or peak arterial pressure during compressions best predicts ROSC”", "The coronaries fill in diastole; systolic peaks can be high while the heart is not perfused."),
    ("“A palpable femoral pulse means compressions are effective”", "The femoral vein lies next to the artery and transmits pressure waves; a felt pulse may be venous and says nothing about coronary flow."),
  ],
  decode=[
    ("Pulseless, high-quality CPR — which parameter best correlates with ROSC? [DocT GT ×2]", "Coronary perfusion pressure (58% and 53%)."),
  ],
  punch="The heart in arrest is fed only between compressions, by the gap between aortic diastolic and right-atrial pressure; ETCO2 and the arterial diastolic pressure are the two windows on that gap.",
)

L['ACLS-45'] = dict(
  sub="Cardiology → ACLS → Epinephrine in arrest",
  step=2,
  intro="Step 2 begins with the one vasopressor left in the algorithm. Epinephrine’s α effect constricts the periphery and raises aortic diastolic pressure, which lifts coronary perfusion pressure (ACLS-44). Six questions test its timing, dose, preparation, its use in pregnancy and the end of vasopressin; the dilution question was answered right by only 34%.",
  parts=[
    ('a', "**Non-shockable: administer epinephrine as soon as possible.** In asystole or PEA there is no shock to deliver, and the chance of ROSC falls with every minute before the first dose, so the drug goes in as soon as access exists (AHA 2025, 2a)."),
    ('b', "**Shockable: reasonable to administer after initial defibrillation attempts have failed.** Here the treatment that works is the shock; epinephrine raises myocardial oxygen demand and can make VF harder to terminate. AHA gives it after the second shock; ERC after the third."),
    ('c', "**Adult: 1 mg IV/IO every 3–5 minutes.** It is the same in pregnancy: no dose change and no other first-line vasopressor. The 1 mg is 10 mL of 1:10,000 (0.1 mg/mL). In India it is often prepared by drawing 1 mL of the 1:1000 ampoule (1 mg/mL) and diluting to 10 mL. 1:1000 undiluted is the IM anaphylaxis strength (0.5 mL = 0.5 mg); 10 mL of it would be a tenfold overdose. High-dose epinephrine has no benefit."),
    ('d', "**Paediatric: 0.01 mg/kg (0.1 mL/kg of the 0.1 mg/mL concentration), max 1 mg, every 3–5 min.** The weight-based dose reaches the adult dose at 100 kg."),
    ('e', "**2025: vasopressin alone, or with epinephrine, offers no advantage as a substitute for epinephrine.** Vasopressin acts on V1 receptors rather than α receptors, which seemed attractive in an acidotic circulation, but trials of vasopressin alone or added to epinephrine showed no better survival, so the algorithm was simplified to one drug (AHA 2020 and 2025, 3: No Benefit). Adding vasopressin with methylprednisolone in in-hospital arrest raised ROSC in trials but not survival."),
  ],
  mimic=[
    ("1:10,000 vs 1:1000", "0.1 mg/mL (IV in arrest, 10 mL for 1 mg) vs 1 mg/mL (IM in anaphylaxis, 0.5 mL)."),
    ("Epinephrine timing in VF vs asystole", "VF: after failed shocks. Asystole/PEA: as soon as feasible."),
  ],
  traps=[
    ("“10 mL of 1:1000” or “1 mL of 1:1000” as the IV arrest preparation (34% right)", "The arrest dose is 1 mg as 10 mL of 1:10,000; 10 mL of 1:1000 is 10 mg."),
    ("“Phenylephrine, noradrenaline or dopamine as first-line in maternal arrest” (54% right)", "Pregnancy changes the position and the access route, not the drugs: epinephrine 1 mg every 3–5 min."),
    ("“Wait for the second rhythm check, or for an advanced airway, before epinephrine in asystole”", "Give it as soon as feasible; neither the airway nor ETCO2 gates it."),
    ("“Vasopressin is first line for shockable rhythms or superior after long down-times”", "It offers no advantage over epinephrine."),
  ],
  decode=[
    ("Asystole — when is epinephrine given? [DocT GT]", "As soon as feasible."),
    ("1 mg every 3 minutes — correct volume and concentration? [DocT GT]", "10 mL of 1:10,000 (34%)."),
    ("Maternal arrest — first-line vasopressor and dose? [DocT QBank ×2]", "Epinephrine 1 mg IV every 3–5 min (54%, 95%)."),
    ("Vasopressin in the 2025 guideline? [DocT GT] [Marrow]", "No advantage over epinephrine; not in the algorithm."),
  ],
  punch="Epinephrine is the only arrest vasopressor: 1 mg of 1:10,000 every 3–5 minutes, straight away when there is no shock to give, after the shocks when there is.",
)

L['ACLS-46'] = dict(
  sub="Cardiology → ACLS → Antiarrhythmics in refractory VF/pVT",
  step=2,
  intro="Step 2 continues with the drugs for VF that keeps coming back after shocks. They do not restart the heart; they make the next shock more likely to hold. Both questions test that amiodarone and lidocaine are alternatives, one in a pregnant patient where the key is disputed.",
  parts=[
    ('a', "**Amiodarone (class III), adult: first 300 mg bolus, second 150 mg.** In ALPS (2016, shock-refractory OHCA) survival to discharge was 24.4% with amiodarone, 23.7% with lidocaine and 21.0% with placebo, not significantly different; in the prespecified bystander-witnessed subgroup both drugs did better than placebo (about 28% vs 23%), which suggests the drugs help when given early. AHA 2025 gives them a weak 2b recommendation. ERC gives amiodarone 300 mg after the third shock and 150 mg after the fifth."),
    ('b', "**Paediatric: 5 mg/kg bolus, may repeat up to 3 total doses.** Weight-based, unlike the fixed adult doses."),
    ('c', "**Lidocaine, adult: first 1–1.5 mg/kg, second 0.5–0.75 mg/kg.** The maximum is 3 mg/kg. ERC uses fixed doses instead: 100 mg, then 50 mg."),
    ('d', "**Class: the card labels amiodarone class III; lidocaine, the drug just above in the question, is class Ib.** Amiodarone is class III because its main action is potassium-channel block, which prolongs repolarisation and refractoriness, although it also blocks sodium and calcium channels and β receptors. Lidocaine blocks fast sodium channels with rapid on–off kinetics, so it acts mainly on ischaemic, depolarised tissue, which is why it suits ischaemic VF."),
  ],
  mimic=[
    ("Amiodarone vs lidocaine in arrest", "Equal outcomes in ALPS; the algorithm reads ‘amiodarone or lidocaine’, never both in sequence as a rule."),
  ],
  traps=[
    ("“Lidocaine + magnesium is wrong for eclamptic maternal VF” (key: amiodarone + magnesium, 67% right)", "AHA lists amiodarone or lidocaine, so lidocaine + magnesium is equally correct; fetal thyroid risk is irrelevant in arrest. With both pairs offered, pick the keyed amiodarone pair."),
    ("“Procainamide infusion for refractory VF”", "Procainamide is an option for stable VT with a pulse; in arrest its benefit is uncertain (ACLS-47)."),
  ],
  decode=[
    ("Three shocks and two doses of epinephrine, still VF — preferred antiarrhythmic strategy? [DocT GT]", "Either amiodarone or lidocaine; equivalent survival to discharge."),
    ("Eclampsia, status epilepticus, then VF arrest at 30 weeks — drug pair? [DocT QBank]", "Amiodarone + magnesium (keyed; lidocaine + magnesium equally valid)."),
  ],
  punch="After failed shocks give amiodarone 300 then 150 mg, or lidocaine 1–1.5 then 0.5–0.75 mg/kg; they are alternatives with equal outcomes, and pregnancy does not change them.",
)

L['ACLS-47'] = dict(
  sub="Cardiology → ACLS → Drugs of uncertain or no benefit",
  step=2,
  intro="Step 2 also lists the drugs that were tested and found wanting. Each was given because it made physiological sense, and each failed to improve survival when trialled. The exam asks which ones are out and what single job magnesium keeps.",
  parts=[
    ('a', "**β-blockers, bretylium, procainamide, sotalol for defibrillation-unresponsive VF/pVT: uncertain benefit.** The evidence is a few small studies. β-blockade in electrical storm makes sense (it blunts the catecholamine drive), but has not been shown to improve survival in arrest (AHA 2025, 2b)."),
    ('b', "**Vasopressin: no advantage, alone or combined with epinephrine.** See ACLS-45."),
    ('c', "**IV calcium for arrest from suspected hyperkalaemia: effectiveness not well established; must be weighed against detracting from CPR, defibrillation and epinephrine.** Calcium stabilises the cardiac membrane against a high potassium, which is why it is used with a pulse; in arrest the trials of routine calcium showed no benefit and a signal of harm, so AHA 2025 makes routine calcium a 3: No Benefit and leaves it a weak 2b where hyperkalaemia is suspected. It does keep a clear place in arrest on a magnesium infusion (ACLS-52) and in calcium-channel-blocker toxicity."),
    ('d', "**Intra-arrest magnesium: did not improve ROSC, survival or neurological outcome regardless of rhythm, and not useful for monomorphic VT. It retains its role in torsades de pointes.** Torsades arises from early afterdepolarisations in a long QT; magnesium suppresses them by blocking the calcium current that triggers them, without needing to correct a low serum level. The dose is 2 g IV (NEET 2024)."),
  ],
  mimic=[
    ("Torsades vs monomorphic VT", "Torsades (twisting axis, long QT) responds to magnesium; monomorphic VT does not."),
    ("Calcium with a pulse vs calcium in arrest", "With a pulse, hyperkalaemic ECG changes are a clear indication; in arrest its effect is not established."),
  ],
  traps=[
    ("“Cocaine-related arrest with polymorphic VT — β-blocker”", "The keyed answer is magnesium for torsades (70% right). Cocaine more often causes a wide-QRS VT from sodium-channel block, which takes bicarbonate (TOX-07)."),
    ("“Bretylium is back on the shelf, so it is recommended again”", "It returned to the market without new evidence; its benefit is uncertain."),
  ],
  decode=[
    ("Indication for MgSO4 in cardiac arrest? [NEET 2024]", "Torsades de pointes (2 g IV)."),
    ("Polymorphic VT after cocaine, collapse — best immediate management? [DocT QBank]", "IV magnesium (torsades)."),
    ("Vasopressin as substitute or adjunct to epinephrine? [DocT GT]", "No advantage."),
  ],
  punch="Outside epinephrine and one antiarrhythmic, nothing routine survives in the arrest algorithm: magnesium is kept only for torsades, and calcium only for a specific cause.",
)

L['ACLS-48'] = dict(
  sub="Cardiology → ACLS → Atropine",
  step=2,
  intro="Step 2 ends with a drug that left the arrest algorithm long ago but remains first line in another. Atropine blocks vagal (muscarinic) slowing of the sinus and AV nodes, so it works only where the block is in or above the node. Only 22% chose it for unstable complete heart block in the ICU.",
  parts=[
    ('a', "**Used only for the symptomatic bradycardia algorithm.** In asystole the problem is not vagal tone, and trials found no benefit, so it was removed in 2010."),
    ('b', "**1 mg × 3 times (maximum 3 mg), repeated every 3–5 minutes.** AHA moved from 0.5 mg to 1 mg in 2020; doses under 0.5 mg can cause paradoxical slowing. If it fails, go to transcutaneous pacing or an epinephrine or dopamine infusion. It rarely works in Mobitz II or complete block below the node (typical of anterior MI, wide QRS escape) or in a transplanted (denervated) heart; there go straight to pacing."),
  ],
  mimic=[
    ("Nodal vs infranodal block", "Narrow QRS escape, inferior MI, Mobitz I: atropine often works. Wide QRS escape, Mobitz II, anterior MI: pace."),
  ],
  traps=[
    ("“Unstable complete heart block — permanent pacemaker or cardioversion” (only 22% right)", "Atropine first while pacing is prepared; a permanent device comes after stabilisation, and cardioversion is for tachycardia."),
    ("“Bradycardia after stenting — dopamine or noradrenaline first”", "Atropine first; infusions are the second line."),
    ("“Atropine 0.5 mg” (an older dose still in some explanations)", "AHA now uses 1 mg every 3–5 min, maximum 3 mg."),
  ],
  decode=[
    ("HR 34, BP 80/50, complete heart block, good contractility — next step? [DocT GT]", "Atropine (22%), with pacing ready."),
    ("Post-ACS/stenting bradycardia, HR 42 — drug to start? [NEET 2025]", "Atropine."),
  ],
  punch="Atropine belongs to bradycardia, not arrest: 1 mg every 3–5 minutes to 3 mg, and if the block is below the node, pace.",
)

L['ACLS-49'] = dict(
  sub="Cardiology → ACLS → Resuscitation triangle roles",
  step=3,
  intro="Step 3 is who does what. The resuscitation triangle is the three people around the patient whose work keeps flow going; no real question is linked, but stems ask who rotates and how often.",
  parts=[
    ('a', "**Compressor: assesses the patient, does 5 cycles of compressions, alternates with the AED/monitor role.** Compression quality falls within about 2 minutes as the rescuer tires, often before he notices."),
    ('b', "**AED / monitor / defibrillator: brings and operates the device, alternates with the compressor, places the monitor where the team leader can see it.** Swapping these two at the rhythm check means the change happens in a pause that already exists."),
    ('c', "**Airway: opens the airway, gives bag-mask ventilation, inserts adjuncts.** Ventilation is a separate job so that breaths are given at the right rate and size while the other two keep compressions and shocks going; only the compressor and AED roles are set to swap."),
    ('d', "**Compressor and AED roles alternate every 5 cycles or 2 minutes, earlier with fatigue; no one leaves the triangle except for his or her own safety.**"),
  ],
  mimic=[
    ("Triangle roles vs leadership roles", "The triangle keeps the patient perfused; the leader, medications and recorder roles (ACLS-50) run the decisions around it."),
  ],
  traps=[
    ("“The compressor changes only when he feels tired”", "Fatigue degrades compressions before it is felt; swap every 2 minutes."),
  ],
  decode=[
    ("How often should compressors rotate? [pattern]", "Every 2 minutes (5 cycles), at the rhythm check."),
  ],
  punch="Swap the compressor every 2 minutes at the rhythm check, because quality fades before the rescuer knows it.",
)

L['ACLS-50'] = dict(
  sub="Cardiology → ACLS → Leadership roles and team composition",
  step=3,
  intro="Step 3 continues with the three roles that surround the triangle. No real question is linked; the likely ask is the leader’s duties and what the recorder tracks.",
  parts=[
    ('a', "**Team leader: every team must have a defined leader; assigns roles, makes treatment decisions, gives feedback, assumes responsibility for roles not assigned.** The leader stays hands-off where possible so he can see the whole scene and think ahead to the next rhythm check."),
    ('b', "**IV/IO / medications: an ACLS provider role; starts IV/IO access, gives medications.**"),
    ('c', "**Time / recorder: records the time of interventions and medications, announces when next due, records the frequency and duration of compression interruptions.** Pauses are the commonest hidden failure in CPR, which is why they are timed."),
    ('d', "**2025: in-hospital code teams should comprise ALS-trained members with clearly defined roles and simulation-based training; an ALS-level clinician present is beneficial in OHCA.**"),
  ],
  mimic=[
    ("Leader vs recorder", "The leader decides; the recorder keeps time and prompts the next drug or rhythm check."),
  ],
  traps=[
    ("“The leader performs the most skilled task himself, such as intubation”", "The leader directs and covers unassigned roles; doing a task narrows his view."),
  ],
  decode=[
    ("Who records the frequency and duration of interruptions in compressions? [pattern]", "The timer/recorder."),
  ],
  punch="One named leader decides, the recorder times every drug and pause, and the 2025 guideline asks for ALS-trained teams that practise by simulation.",
)

L['ACLS-51'] = dict(
  sub="Cardiology → ACLS → Arrest in pregnancy: principles",
  step=4,
  intro="Step 4 opens the special circumstances with pregnancy. From about 20 weeks the uterus compresses the inferior vena cava and aorta when the woman lies supine, so CPR on her back produces even less output than usual. Three questions test that and the airway.",
  parts=[
    ('a', "**Priorities: high-quality CPR and relief of aortocaval compression.** Compressions need venous return to fill the heart; a gravid uterus on the vena cava removes much of it."),
    ('b', "**Continuous manual left lateral uterine displacement.** Pushing the uterus up and to the left lifts it off the vena cava while the woman stays flat, so compressions stay effective. A tilted board was used before, but tilting reduces compression force; AHA 2025 makes manual displacement class 1. It needs a second rescuer, which is the answer to the NEET recall."),
    ('c', "**A difficult airway is common in pregnancy; use the most experienced provider; ETT or SGA; waveform capnography to confirm and monitor.** Airway oedema, breast tissue, a full stomach with a lax oesophageal sphincter and a lower functional residual capacity with higher oxygen demand mean she desaturates fast and aspirates easily. A cuffed tube protects the airway best, so it is the preferred device when an expert can place it."),
    ('d', "**1 breath every 6 seconds (10/min) with continuous compressions once the advanced airway is in; team planning with obstetric, neonatal, emergency, anaesthesia, intensive care and arrest services.**"),
  ],
  mimic=[
    ("Manual uterine displacement vs left lateral tilt", "Displacement keeps her flat for good compressions; tilt weakens them."),
  ],
  traps=[
    ("“Half-dose epinephrine in pregnancy” or “avoid intubation until ROSC”", "Drug doses are unchanged and the airway is secured early by the most experienced person."),
    ("“The second rescuer is needed for perimortem caesarean or defibrillation”", "The second pair of hands is for continuous uterine displacement."),
  ],
  decode=[
    ("28 weeks, arrest in ICU — most critical ACLS modification? [DocT QBank]", "Manual left uterine displacement (97%)."),
    ("Preferred airway device in maternal arrest? [DocT QBank]", "Endotracheal tube (92%)."),
    ("Why is a second rescuer essential? [NEET 2025]", "Uterine displacement."),
  ],
  punch="In maternal arrest the uterus is the obstruction: push it left by hand while compressions continue, and let the most experienced person secure an airway that is both difficult and at risk of aspiration.",
)

L['ACLS-52'] = dict(
  sub="Cardiology → ACLS → Maternal arrest interventions and causes",
  step=4,
  intro="Step 4 continues with what the maternal algorithm adds. Each addition answers a feature of pregnancy: the vena cava is blocked, the patient may be on magnesium, and the causes differ. Six questions test these, and two keys are disputed.",
  parts=[
    ('a', "**Maternal: airway management • 100% O2, avoid excess ventilation • place IV above the diaphragm.** With the vena cava compressed, a drug given in a leg may not reach the heart; AHA 2025 recommends upper-limb IV or IO access."),
    ('b', "**If receiving IV magnesium, stop it and give calcium chloride or gluconate.** Magnesium toxicity causes loss of reflexes, respiratory depression, conduction block and arrest; calcium antagonises its effect on the membrane. Hypermagnesaemia is the electrolyte cause to suspect when a woman on a magnesium infusion becomes bradycardic and arrests. Seizure prophylaxis can resume after ROSC."),
    ('c', "**Obstetric: continuous lateral uterine displacement • detach fetal monitors • prepare for resuscitative delivery.** Fetal monitors are removed because they slow the move to delivery and interfere with defibrillation; the fetus is best served by restoring the mother’s circulation."),
    ('d', "**Aetiologies A–H: anaesthetic complications, bleeding, cardiovascular, drugs, embolic, fever, general non-obstetric causes (H’s and T’s), hypertension.** Haemorrhage is the commonest single cause of maternal arrest, so PEA in pregnancy is treated as hypovolaemia first (wide-bore access above the diaphragm, massive transfusion, uterotonics, obstetrician to theatre). Drugs include magnesium toxicity and local anaesthetic toxicity; embolic includes amniotic fluid and pulmonary embolism."),
  ],
  mimic=[
    ("Magnesium in eclampsia vs magnesium in arrest", "Before arrest it is the treatment; once she arrests on an infusion it is a suspected cause: stop it and give calcium."),
  ],
  traps=[
    ("“Give magnesium promptly as part of ACLS in eclampsia-related arrest” (DocT key, 68% chose it)", "The algorithm says stop magnesium and give calcium; magnesium for seizures resumes after ROSC. If she was already on magnesium, choose calcium."),
    ("“Continue the magnesium infusion to prevent seizures, or delay changes until ROSC”", "Stop it now and give calcium."),
    ("“Hypokalaemia or hypercalcaemia” for bradycardic arrest on the ICU (61% right)", "On magnesium the suspect is hypermagnesaemia."),
    ("“Attach fetal monitors”", "They are detached."),
  ],
  decode=[
    ("PEA in pregnancy — commonest reversible cause? [DocT QBank]", "Hypovolaemia from obstetric haemorrhage (81%)."),
    ("Pregnant, bradycardia then arrest in ICU — electrolyte? [DocT QBank]", "Hypermagnesaemia (61%)."),
    ("Arrest on IV magnesium for pre-eclampsia, CPR and displacement under way — next? [DocT GT]", "Stop magnesium, give IV calcium."),
    ("Maternal arrest — which is NOT indicated? [Marrow]", "Attaching fetal monitors."),
  ],
  punch="The maternal algorithm adds three things: access above the diaphragm because the vena cava is blocked, calcium because magnesium may be the cause, and delivery because the uterus is the obstruction.",
)

L['ACLS-53'] = dict(
  sub="Cardiology → ACLS → Resuscitative delivery",
  step=4,
  intro="Step 4 turns to delivery during arrest. Emptying the uterus relieves aortocaval compression, increases venous return and removes the fetus’s and placenta’s oxygen demand, so it is a manoeuvre for the mother first. Four questions test the timing, the evidence and the incision; two are poorly answered because they ask about trials.",
  parts=[
    ('a', "**2025 term: resuscitative delivery, replacing ‘perimortem caesarean delivery’.** The new name says what it is for: maternal resuscitation, not fetal salvage."),
    ('b', "**Preparation should begin at the recognition of cardiac arrest.** It is indicated when the fundus is at or above the umbilicus (about 20 weeks) and standard resuscitation has not restored circulation (class 1). The team, kit and operator are gathered from the first minute so that the clock is not lost."),
    ('c', "**Goal: complete delivery by 5 minutes.** This comes from Katz, Dotters and Droegemueller (1986), the ‘4-minute rule’: start by 4 minutes, deliver by 5. It is a goal from case series, not a trial result. It is done where she lies, through a vertical midline incision from just above the symphysis to the umbilicus, with CPR and displacement continuing."),
    ('d', "**Purpose: improve both maternal and fetal outcomes.** In case reviews (Katz 2005, Einav 2012) ROSC often followed delivery; earlier delivery was linked to better survival of both."),
    ('e', "**ECPR is reasonable in pregnant or peripartum patients not responding to standard resuscitation (55% survival in the ELSO registry, 87% of 57 patients); a massive transfusion protocol with a balanced strategy, with tranexamic acid, for suspected amniotic fluid embolism (both class 1).** AHA 2025 gives the figures precisely: the 55% is survival among 42 obstetric patients given ECLS for cardiac arrest in the ELSO registry (for ECPR itself the registry figure was 29%), and the 87% is 30-day survival among 57 patients cannulated for arrest in pregnancy or within 24 hours of delivery. Pregnant patients are young, with reversible causes, which is why extracorporeal support does well. In AFE the typical sequence is sudden collapse with right heart failure, then consumptive coagulopathy and massive bleeding; AHA 2025 also supports VA-ECMO and inhaled pulmonary vasodilators."),
  ],
  mimic=[
    ("Resuscitative delivery vs ordinary emergency caesarean", "One is done at the bedside during CPR to resuscitate the mother; the other is done in theatre for maternal or fetal indications."),
  ],
  traps=[
    ("“The HELP trial studied maternal arrest and perimortem caesarean” (DocT key; 14% right)", "No such trial exists; the evidence is Katz 1986/2005 and Einav 2012. If Katz or a case series is offered, choose it; otherwise eliminate MOMS (fetal spina bifida surgery), ALPS (late-preterm steroids) and PROWESS (drotrecogin alfa in sepsis)."),
    ("“After 20 minutes of failed CPR”, “only after fetal demise” or “after ROSC”", "Prepare at recognition and deliver by 5 minutes if there is no ROSC."),
    ("“Supra-umbilical or xiphoid incision” (45% right)", "Vertical midline from just above the symphysis to the umbilicus."),
  ],
  decode=[
    ("Timing of perimortem delivery at 34 weeks [DocT QBank]", "Within 5 minutes of arrest if no ROSC (92%)."),
    ("Origin of the ‘4-minute rule’ [DocT QBank]", "Katz et al (54%)."),
    ("Landmark for the incision [DocT QBank]", "Just above the symphysis pubis, vertical midline (45%)."),
  ],
  punch="Resuscitative delivery is a manoeuvre for the mother: start preparing when the arrest is recognised, deliver by 5 minutes, and if that fails, extracorporeal support is reasonable.",
)

L['ACLS-54'] = dict(
  sub="Cardiology → ACLS → The unresponsive LVAD patient",
  step=4,
  intro="Step 4 includes a patient whose circulation does not depend on a beating heart. A continuous-flow LVAD pumps without pulsatility, so most patients have no palpable pulse while perfusing well. No real question is linked; the likely ask is how to judge perfusion and when to compress.",
  parts=[
    ('a', "**Adequate perfusion if any of: normal skin colour and temperature, normal capillary refill, MAP >50 mmHg, PETCO2 >20 mmHg. Patients may not have a palpable pulse.** The MAP is read with a Doppler or arterial line, because a cuff may not register non-pulsatile flow. Current durable LVADs give continuous flow, so most patients have no pulse at all; its absence is not a sign of arrest."),
    ('b', "**Adequate → do not perform external chest compressions; assess and treat non-LVAD causes; monitor perfusion.** If the pump is moving blood, compressions add nothing."),
    ('c', "**Impaired → perform external chest compressions, assess LVAD function if a second rescuer is available, continue BLS/ALS, transport and contact the VAD centre.** AHA 2025 makes compressions class 1 here: the fear of dislodging the cannula is theoretical, while hypoperfusion is lethal."),
    ('d', "**Restart checks: alarms • the LVAD hum • driveline connected? • power source connected? • replace the system controller?** A disconnected driveline, a flat battery or a failed controller are faults that can be fixed at the bedside in seconds, which is why they are checked before anything else."),
    ('e', "**Non-LVAD causes: dysrhythmia, haemorrhage/hypovolaemia, hypoglycaemia, hypoxia, overdose, RV failure, sepsis, stroke.** The pump depends on RV output to fill it, so RV failure or a ventricular arrhythmia that stops the RV can starve it."),
  ],
  mimic=[
    ("No pulse with an LVAD vs no pulse in arrest", "With an LVAD it is expected; perfusion is judged by MAP, PETCO2, skin and capillary refill."),
  ],
  traps=[
    ("“Never compress the chest of an LVAD patient”", "Compress whenever perfusion is impaired; the risk of dislodgment is outweighed."),
  ],
  decode=[
    ("Unresponsive LVAD patient, no pulse, MAP 60, PETCO2 25 — compress? [pattern]", "No; perfusion is adequate, look for non-LVAD causes."),
  ],
  punch="In an LVAD patient the pulse means nothing: judge perfusion by MAP over 50 or PETCO2 over 20, and if it is impaired, compress without delay.",
)

L['ACLS-55'] = dict(
  sub="Cardiology → ACLS → Asthma, hypothermia and hyperthermia",
  step=4,
  intro="Step 4 ends with the most-asked card in the deck: eleven questions, almost all on temperature. Cold and heat both kill, but in opposite ways: cold protects the brain and makes the heart unresponsive, so rewarming comes before drugs; heat injures every minute, so cooling speed is everything.",
  parts=[
    ('a', "**Asthma: ECLS may be reasonable; volatile anaesthetics may be considered; survival 83.5–100% in observational studies.** Refractory asthma kills by gas trapping and hypercapnia, not by a damaged lung, so taking over gas exchange buys time for bronchodilators to work. Volatile agents relax bronchial smooth muscle directly."),
    ('b', "**Hypothermia: ECLS for rewarming; prognostication scores (HOPE, ICE) to guide initiation; may rewarm with ECLS if core <28 °C even without arrest.** Below 28 °C the heart is prone to VF on handling. ECLS rewarms the core at 1.5–5 °C/h while supporting the circulation. HOPE estimates survival (under 10% predicts death) and is better than a potassium threshold alone; potassium above 12 mmol/L suggests cell lysis from asphyxia or death before cooling, and is non-survivable. Grades and rewarming: mild 32–35 °C passive external (dry, insulate; shivering rewarms); moderate 28–32 °C active external (forced air, warmed IV fluid); severe under 28 °C or unstable, active internal (ECLS, or thoracic or peritoneal lavage). The cold myocardium does not respond to shocks or drugs, and drugs accumulate: AHA 2025 now says defibrillate once and defer further shocks and epinephrine until 30 °C; ERC allows up to three shocks, withholds adrenaline below 30 °C and doubles its interval at 30–35 °C."),
    ('c', "**Hyperthermia: ice water immersion (1–5 °C) preferred; cool as rapidly as possible, at least 0.15 °C/min.** Heat stroke (core over 40 °C with CNS dysfunction) damages cells in proportion to time above the critical temperature, so the outcome depends on how fast the core falls. Water conducts heat far better than air, which is why immersion beats fans, blankets and cold IV fluid. If ice water is not available, AHA 2025 accepts tepid water at 8–17 °C or tarp-assisted ice water; where immersion is not possible at all (frail elderly, ICU), evaporative cooling with ice packs is the fallback. Antipyretics do nothing because the set-point is normal, and dantrolene has no role outside malignant hyperthermia. AHA 2025 stops active cooling at 38.6 °C, because the core keeps falling after removal."),
  ],
  table=dict(title="Accidental hypothermia: grade and rewarming",
    head=["Grade", "Core", "Rewarming"],
    rows=[["Mild", "32–35 °C", "Passive external: dry, insulate, warm room"],
          ["Moderate", "28–32 °C", "Active external (forced air) + warmed IV fluid"],
          ["Severe / unstable / arrest", "Under 28 °C", "Active internal: ECLS first, lavage if unavailable"]]),
  mimic=[
    ("Hypothermic arrest vs normothermic arrest", "Cold: rewarm, limit shocks and defer drugs below 30 °C, continue CPR long. Normothermic: standard ALS."),
    ("Heat stroke vs fever", "Heat stroke has a normal set-point and needs physical cooling; fever responds to antipyretics."),
  ],
  traps=[
    ("“Cool exertional heat stroke to at least 36 °C to prevent rebound” (DocT key; 78% chose it)", "The key is wrong: stop cooling at about 38.6–39 °C (AHA 2025: 38.6 °C), because the core falls further after removal. Choose ‘stop at 39 °C’ if offered."),
    ("“Cooling blankets and fans” or “cold IV fluid alone” for heat stroke (59% right)", "Ice-water immersion is fastest."),
    ("“Passive rewarming is wrong for mild hypothermia — use active external” (47% right)", "Stable mild hypothermia needs only passive external rewarming."),
    ("“Give antiarrhythmics for VF at 29 °C” (53% right)", "Continue CPR and withhold antiarrhythmics until above 30 °C; lidocaine does not work in a cold heart. ‘Defibrillate once and proceed with active rewarming’ is not wrong either (AHA 2025 allows one shock, ERC up to three), but the keyed answer is ‘continue CPR and withhold antiarrhythmics’."),
    ("“AHA is more permissive than ERC on shocks and drugs in hypothermia”", "That was AHA 2020; AHA 2025 defers further shocks and epinephrine below 30 °C, close to ERC."),
  ],
  decode=[
    ("Hot day, core 41 °C, confused — initial step? [DocT QBank ×2]", "Ice-water immersion (59%, 88%)."),
    ("Core 29 °C, VF — next step? [DocT QBank]", "Continue CPR, withhold antiarrhythmics until above 30 °C (53%)."),
    ("Core 30 °C, Osborn waves, wide QRS — strategy? [DocT QBank]", "Active internal rewarming with gentle handling (83%)."),
    ("Pulseless in snow — which test decides continuing CPR? [Marrow]", "Serum potassium (over 12 mmol/L is non-survivable)."),
  ],
  extra=[
    dict(q="Which conduction site does hypothermia depress first? [Marrow]", a="The sinoatrial node: sinus bradycardia comes first, then atrial fibrillation, Osborn (J) waves and a long QT; VF risk is highest below 28 °C."),
  ],
  punch="Cold protects the brain and paralyses the heart, so rewarm (by ECLS when severe) and hold drugs and repeated shocks below 30 °C; heat injures every minute, so immerse in ice water at 0.15 °C/min and stop at about 38.6 °C.",
)

L['ACLS-56'] = dict(
  sub="Cardiology → ACLS → 2025 post-cardiac arrest algorithm",
  step=5,
  intro="Step 5 is what happens once the heart restarts. Most deaths after ROSC come from brain injury and recurrent shock, so the algorithm first protects oxygen delivery, then sorts patients by whether the brain is working. No real question is linked to this card.",
  parts=[
    ('a', "**Initial stabilisation: airway • oxygenation and ventilation (SpO2 90–98%, PCO2 35–45) • haemodynamics (MAP ≥65).** FiO2 stays at 100% until the saturation can be read reliably. Both hypoxia and hyperoxia, and both low and high CO2, injure the reperfused brain (low CO2 constricts cerebral vessels). ERC–ESICM 2025 targets 94–98% and MAP over 60–65."),
    ('b', "**Early diagnostics: 12-lead ECG; consider CT (head to pelvis) and/or ultrasound.** The ECG finds the coronary cause; CT finds bleeding, PE, aortic dissection or injury from CPR."),
    ('c', "**Assess the patient off sedation and neuromuscular blockade, if able → follows commands?** Sedation can make an awake brain look comatose, which would push a patient wrongly into the coma arm and later into a false poor prognosis."),
    ('d', "**No or unsure: the same, plus a deliberate temperature-control strategy, EEG and appropriately timed multimodal prognostication.** Temperature is held between 32 and 37.5 °C for at least 36 hours (AHA 2025), with fever prevented; EEG detects seizures that are often non-convulsive; prognostication is consolidated at least 72 hours after normothermia and stopping sedation (AHA 2025; ERC–ESICM counts 72 hours from ROSC), using several tests together, because sedatives and cooling slow the recovery of brain function and an early single test misleads."),
    ('e', "**Emergency cardiac intervention for persistent ST elevation, cardiogenic shock, recurrent or refractory ventricular arrhythmias, severe myocardial ischaemia.** Without these, early angiography after arrest without ST elevation did not improve survival (COACT, TOMAHAWK)."),
  ],
  mimic=[
    ("Follows commands vs does not", "Awake: critical care and angiography as needed. Not awake or unsure: add temperature control, EEG and delayed multimodal prognostication."),
  ],
  traps=[
    ("“Prognosticate at 24 hours on a single test”", "Wait at least 72 hours after normothermia and sedation are off, and use several tests."),
  ],
  decode=[
    ("Post-ROSC targets for SpO2, PaCO2 and MAP? [pattern]", "90–98%, 35–45 mmHg, MAP ≥65."),
    ("What decides entry to temperature control and EEG? [pattern]", "Not following commands off sedation."),
  ],
  punch="After ROSC, stabilise oxygen, CO2 and pressure, find the cause, then ask one question off sedation: does the patient follow commands? A ‘no’ brings temperature control, EEG and prognostication at 72 hours.",
)

L['ACLS-57'] = dict(
  sub="Cardiology → ACLS → ACS algorithm",
  step=6,
  intro="Step 6 leaves arrest for the patient who may arrest next. In ACS the ECG sorts patients in minutes into those who need reperfusion now and those who need a troponin pathway. The one real question, a T-wave inversion with pain, was answered right by only 44%.",
  parts=[
    ('a', "**Prehospital: support ABCs and monitor ECG • obtain and evaluate a 12-lead ECG • consider IV access, oxygen, aspirin, nitrate, morphine • transfer to an emergency PCI-capable facility.** A prehospital ECG lets the cath lab be activated before arrival. Oxygen only if SpO2 is under 90%; giving it to normoxic patients does not help (AVOID, DETO2X)."),
    ('b', "**ED concurrent assessment in <10 minutes: vitals, 12-lead ECG, targeted history, hs-cTn, electrolytes, coagulation, CXR and TTE, call cardiology.** The ECG within 10 minutes is the step that decides everything that follows."),
    ('c', "**Chew aspirin 162–325 mg; nitroglycerin spray; IV morphine if discomfort is not relieved by nitroglycerin.** Chewing gives faster absorption. Nitrates are avoided in hypotension, RV infarction and after a phosphodiesterase-5 inhibitor. Morphine delays absorption of oral P2Y12 inhibitors, so it is kept for pain that nitrates do not settle."),
    ('d', "**ST elevation or new LBBB → suspicious for STEMI → consult cardiology: do not delay reperfusion.** ACC/AHA no longer treat a new LBBB alone as diagnostic (Sgarbossa criteria help); ESC 2023 manages any bundle branch block with ongoing ischaemic symptoms as a STEMI equivalent."),
    ('e', "**Non-ST elevation → suspicious for UA/NSTEMI → hs-cTn on arrival (0 h); positive + clinical presentation: CCU or monitored bed; negative: chest pain unit, recheck hs-cTn at 1 h or 3 h, with ECG monitoring.** The rule-out depends on the assay; ESC 2023 uses 0/1 h or 0/2 h algorithms. Immediate angiography in NSTE-ACS is only for very high risk (shock, refractory pain, arrhythmia, mechanical complication)."),
  ],
  mimic=[
    ("STEMI vs NSTE-ACS first hour", "STEMI: reperfusion without delay. NSTE-ACS: monitor, aspirin, troponin, risk-stratify."),
  ],
  traps=[
    ("“T inversion with pain — call the cath lab for immediate PCI”", "That is for STEMI or very-high-risk NSTE-ACS; first monitor, oxygen if hypoxic, aspirin."),
    ("“Two sublingual nitrates and observe” or “CXR then aspirin, clopidogrel and heparin”", "The immediate step is monitor, oxygen if needed and aspirin; dual antiplatelets and anticoagulation follow assessment."),
  ],
  decode=[
    ("New chest pain, lateral T inversion — most immediate step? [DocT GT]", "Monitor, oxygen if needed, aspirin (44%)."),
  ],
  punch="In suspected ACS the 12-lead ECG within 10 minutes splits the road: ST elevation goes straight to reperfusion, the rest get aspirin, monitoring and a repeat high-sensitivity troponin.",
)

L['ACLS-58'] = dict(
  sub="Cardiology → ACLS → Stroke algorithm time goals",
  step=6,
  intro="Step 6 ends with the stroke clock. Brain tissue in an ischaemic penumbra dies by the minute, so the algorithm sets fixed targets from the door. No real question is linked; the usual ask is the door-to-needle time and what is checked first.",
  parts=[
    ('a', "**10 minutes: immediate general assessment and stabilisation — ABCs, oxygen if hypoxic, IV access and labs, check glucose, neurological screen, activate the stroke team, order emergent CT or MRI, 12-lead ECG.** Hypoglycaemia mimics stroke and is excluded by a bedside glucose first."),
    ('b', "**25 minutes: neurological assessment by the stroke team — history, time of onset or last known normal, NIH Stroke Scale.** The time last known normal sets the lysis window (within 4.5 hours, later only with imaging selection). The 2026 AHA/ASA guideline also aims for imaging within 25 minutes of arrival."),
    ('c', "**45 minutes: CT interpretation — does it show haemorrhage?** A bleed excludes lysis and goes to neurology or neurosurgery."),
    ('d', "**60 minutes: give rtPA if still a candidate; no anticoagulants or antiplatelets for 24 hours.** The 2026 AHA/ASA guideline endorses either tenecteplase 0.25 mg/kg (maximum 25 mg, single bolus) or alteplase 0.9 mg/kg within 4.5 hours. Blood pressure must be under 185/110 to lyse and is kept under 180/105 for 24 hours after."),
    ('e', "**3 hours: begin the post-rtPA stroke pathway — aggressive monitoring, BP per protocol, admit to stroke unit or ICU.**"),
    ('f', "**Not a fibrinolytic candidate → administer aspirin.** Once haemorrhage is excluded."),
  ],
  mimic=[
    ("Time of onset vs time last known normal", "For a stroke found on waking, the clock starts when the patient was last seen well, not when found."),
  ],
  traps=[
    ("“Start aspirin with lysis”", "No antiplatelets or anticoagulants for 24 hours after a lytic."),
  ],
  decode=[
    ("Door-to-needle goal for lysis? [pattern]", "60 minutes."),
    ("Door-to-CT interpretation goal? [pattern]", "45 minutes."),
  ],
  punch="Stroke runs on a door clock (10, 25, 45, 60 minutes), and the time last known normal decides whether the 60-minute needle is still possible.",
)

FLAGS = {
  'ACLS-41': "b: ETT, SGA, i-gel and Combitube are ACLS ‘advanced airways’; ‘definitive airway’ (ATLS) means a cuffed tube in the trachea, which a supraglottic device is not. The explanation says so.",
  'ACLS-42': "Card is correct (no intra-arrest saturation target; post-ROSC SpO2 90–98% with PaO2 60–105 mmHg confirmed in AHA 2025 Part 11). The NEET 2025 recall keys chest X-ray for ‘best verification’; X-ray confirms depth, not tracheal placement; waveform capnography is the standard. The trap gives the exam-day rule.",
  'ACLS-44': "Card is correct: AHA 2025 sets no adult diastolic target; ERC 2025 (RCUK text) aims for diastolic ≥30 mmHg with an arterial line and ETCO2 ≥25 mmHg. The DocT line’s ‘arterial-line target diastolic >20 mmHg’ is the AHA 2020 figure; 2025 removed it.",
  'ACLS-46': "d: the question asks ‘its drug class’ after the lidocaine row, but the card prints a class only for amiodarone (class III); lidocaine is class Ib. The explanation gives both. DocT keys amiodarone + magnesium for eclamptic maternal VF; lidocaine + magnesium is equally correct (amiodarone OR lidocaine).",
  'ACLS-52': "Card is correct. DocT keys ‘give magnesium promptly as part of ACLS’ in eclampsia-related arrest; the algorithm says stop magnesium and give calcium.",
  'ACLS-53': "e: ‘55% in the ELSO registry’ is survival among 42 obstetric patients given ECLS for arrest; AHA 2025 gives 29% for ECPR itself in that registry, and ‘87% of 57’ is 30-day survival. The explanation states this. DocT keys a ‘HELP trial’ as the evidence for resuscitative delivery; no such trial exists (Katz 1986/2005, Einav 2012).",
  'ACLS-55': "Card is correct. DocT key ‘cool to at least 36 °C’ in heat stroke is wrong (AHA 2025: stop at 38.6 °C, 2a). Card-layer line ‘AHA is more permissive’ on hypothermic arrest is out of date: AHA 2025 says defibrillate once, then defer further shocks and epinephrine until ≥30 °C; so in the 29 °C VF question ‘defibrillate once and rewarm’ is also defensible, though C is keyed.",
  'ACLS-58': "Dated wording: ‘rtPA’ — the 2026 AHA/ASA guideline endorses tenecteplase 0.25 mg/kg (max 25 mg) or alteplase 0.9 mg/kg within 4.5 h. Time goals are the classic NINDS targets; the 2026 guideline asks for the initial brain scan within 25 min of arrival. The explanation adds both.",
}
