# CVS03 — Explain v3 ("Learn" depth): cardiogenic shock, part 1 — epidemiology, the three definitions (SHOCK, IABP-SHOCK II, ESC), SCAI stages, aetiology, PV loops and the
# neurohormonal spiral, Forrester profiles and bedside signs, monitoring and investigations, level of care, physiological targets, the ESC bedside-profile algorithm, supportive care,
# offloading drugs, inotropes and the inotrope algorithm, vasoactive choice by subtype (shock states, valves, mechanical/electrical), revascularisation, SHOCK and CULPRIT-SHOCK.
# No mnemonics or hooks. Driven by qpack/CVS03.md (76 question links; CS-29 inotropes asked 15 times, CS-30 inotrope algorithm 10, CS-26 ESC profiles 9, CS-27 supportive care,
# CS-28 offloading and CS-32 valvular subtypes 5 each). CS-01, 04, 07–10, 14–16, 20, 21, 23–25, 31, 35 and 36 have no linked question and get short explanations with [pattern] decode items.
# No `fix` entries exist for CVS03 in trace/test/data/qbank.json (checked 19 Nov 2026). The card layer (cvs_cardlayer.json: lines and Crossfire notes for CS-06, 11, 12, 13, 19, 22, 26,
# 28, 29, 30, 32) was read and the explanations agree with it; where a DocT key is wrong the trap says so (CS-26, CS-29, CS-30).
# Checked online on 19 Nov 2026:
#  - SHOCK (Hochman, NEJM 1999; Wiki Journal Club): n 302, MI within 36 h, shock randomised within 12 h; SBP <90 for ≥30 min or support to keep SBP ≥90, end-organ hypoperfusion, CI ≤2.2,
#    PCWP ≥15. 30-day mortality 46.7 vs 56.0% (RR 0.83, p 0.11); 6-month 50.3 vs 63.1% (p 0.027); age <75 30-day 41.4 vs 56.8%. Persistent benefit at 1 and 6 years.
#  - SHOCK PCI analysis (Webb 2003, abstract): mortality 38% with TIMI 3 flow, 55% with TIMI 2, 100% with TIMI 0–1; 39% if PCI successful vs 85% if unsuccessful.
#  - IABP-SHOCK II (Thiele, NEJM 2012): n 600; SBP <90 >30 min or catecholamines to keep >90, pulmonary congestion, impaired perfusion (altered mental status, cold clammy skin, UO <30 mL/h,
#    lactate >2.0); 30-day mortality 39.7 vs 41.3% (p 0.69).
#  - CULPRIT-SHOCK (Thiele, NEJM 2017): n 706, AMI-CS with multivessel disease and an identifiable culprit; death or RRT at 30 days 45.9 vs 55.4%, ARR 9.5% (NNT 11); at 1 year death and RRT
#    no longer significantly different, more repeat revascularisation and HF rehospitalisation with culprit-only.
#  - ECLS-SHOCK (Thiele, NEJM 2023): n 420 (417 analysed), AMI-CS with lactate >3, ~78% resuscitated; 30-day death 47.8 vs 49.0% (RR 0.98); BARC 3–5 bleeding 23.4 vs 9.6%; peripheral
#    vascular complications 11.0 vs 3.8%.
#  - DanGer Shock (Møller, NEJM 2024): n 360 STEMI-CS, SBP <100, lactate >2.5, LVEF <45%, comatose OHCA excluded; 180-day death 45.8 vs 58.5% (HR 0.74, NNT 8); composite device adverse
#    events 24 vs 6%; RRT 42 vs 27%. 10-year follow-up (ESC 2025): 52.5 vs 68.8% (HR 0.7).
#  - DOREMI (Mathew, NEJM 2021): n 192, SCAI B–E; milrinone vs dobutamine composite 49 vs 54% (RR 0.90, NS); in-hospital death 37 vs 43% (NS).
#  - SOAP II (De Backer, NEJM 2010): n 1,679; 28-day mortality dopamine 52.5 vs norepinephrine 48.5% (NS); arrhythmias 24.1 vs 12.4%; cardiogenic-shock subgroup n 280, higher mortality with
#    dopamine (log-rank p 0.03; interaction p 0.87, so not robust).
#  - SCAI SHOCK stages 2022 update (Naidu, JSCAI 2022; guideline summary): B relative hypotension or tachycardia without hypoperfusion, normal lactate; C hypoperfusion needing one intervention beyond
#    volume, lactate ≥2, CI typically <2.2; D failing initial strategy, lactate rising, escalating support; E actual or impending collapse, lactate ≥8, pH <7.2; arrest modifier now specified as
#    arrest with coma (unresponsive to voice). Three-axis model (stage, phenotype/aetiology, risk modifiers).
#  - 2025 ACC/AHA ACS guideline (ACC summary; manufacturer summary): microaxial flow pump class 2a in STEMI with severe or refractory CS; routine IABP and routine VA-ECMO class 3 (no benefit).
#  - ESC 2023 ACS (summaries): routine IABP not recommended without mechanical complications (III), IABP for mechanical complications IIa, short-term MCS may be considered (IIb); staged
#    non-culprit PCI IIa. ESC 2021 HF: norepinephrine preferred vasopressor (IIb), inotropes may be considered (IIb), short-term MCS in refractory CS (IIa).
#  - ESC 2023 HF focused update: SGLT2 inhibitors class I-A in HFmrEF and HFpEF; rapid up-titration after an admission I-B (STRONG-HF).
#  - Epidemiology: SHARC-definition CCCTN registry 2024 (n 5,869): AMI-CS 27%, HF-CS 59% (72% acute-on-chronic, 28% de novo); in-hospital death AMI-CS 41%, HF-CS 25–31%.
#    AMI-CS readmission at 30 days 18.6% (2013–14 Nationwide Readmissions Database; HF the commonest cardiac cause). MDPI 2025 review: AMI ~60–80% of CS in older series; CS in 6–8% of AMI.
#  - Older definitions page (Deranged Physiology): ESC 2016 wording ‘SBP <90 with appropriate fluid resuscitation with clinical and laboratory evidence of end-organ damage’.
# From standard references without a fresh check (confident unless said): ESC 2021 HF definition of CS by hypoperfusion without mandatory hypotension (and the 2020 HFA position statement);
# AHA 2017 cardiogenic shock statement (van Diepen) as the source of the monitoring tables, subtype tables
# and the hub-and-spoke model; OptimaCC (Levy 2018: adrenaline vs norepinephrine, refractory shock 37 vs 7%); levosimendan pharmacology
# (active metabolite, days of effect); PROMISE (oral milrinone raised mortality), OPTIME-CHF; DIG; PARADIGM-HF; EMPEROR-Preserved, DELIVER; GALACTIC-HF; RELAX-AHF-2; PRAMI, CvLPRIT,
# DANAMI-3-PRIMULTI, COMPLETE; EAST blunt cardiac injury guidance. Second check (19 Nov 2026): ESC 2021 HF definition (hypoperfusion signs, hypotension not required) confirmed from review summaries; ESC 2016 summary card flowchart
# gives congestion present 95% / absent 5% of AHF (ESC-HF-LT registry at admission: wet about 90%); SHOCK registry (Wong, JACC 2000): left main 15.5%, three-vessel 53.4%, culprit mortality
# LM 78.6, SVG 69.7, Cx 42.4, LAD 42.3, RCA 37.4%; Shaefi 2015 (JAHA) volume quartiles (lowest ≤27/yr, adjusted mortality 42.0 vs 37.0%; the >100 cut-off itself not traced);
# Webb 2003 SHOCK PCI analysis is one-year mortality; SHOCK arm 60% PCI / 40% CABG (Wiki Journal Club); CULPRIT-SHOCK 1-year death 50.0 vs 56.9%; ESC 2023 staged non-IRA PCI in CS IIa;
# SCAI 2022 descriptors and arrest-with-coma modifier; ACC/AHA 2025 microaxial pump 2a, routine IABP 3.

SPINE = [
  ("Defining the shock", "Cardiogenic shock is a primary cardiac problem with hypoperfusion proven clinically and biochemically, and SHOCK, IABP-SHOCK II, ESC and SCAI each draw that line slightly differently."),
  ("Who gets it and why", "Acute MI with large muscle loss or a mechanical complication is the classic cause, but heart failure, valves, rhythm, obstruction and toxins fill the other branches."),
  ("The spiral of the failing pump", "A weaker ventricle moves its pressure–volume loop to the right, and the sympathetic and renin systems that defend the pressure raise afterload and preload until they injure the heart further."),
  ("Profiling at the bedside", "Cold or warm (perfusion) and wet or dry (congestion), confirmed by echo, lactate, wedge pressure and serial monitoring, sort the patient and choose the treatment."),
  ("Support the circulation", "Unload congestion with nitrates, diuretics and positive pressure, add an inotrope for low output and norepinephrine for low pressure, and pick the drug by phenotype."),
  ("Fix the lesion behind it", "Valve and mechanical lesions need their own haemodynamic rules and a definitive repair, and in AMI shock early culprit-vessel revascularisation is the only treatment proven to save lives."),
]

PRIMER = "Shock means the tissues get less oxygen than they need; in cardiogenic shock the reason is the heart itself, not the volume in the vessels or their tone. Cardiac output is heart rate times stroke volume, and stroke volume depends on preload (filling), afterload (the load the ventricle ejects against) and contractility. Blood pressure is cardiac output times systemic vascular resistance, so a failing heart can hold a normal pressure for a while by clamping down the vessels, which is why hypoperfusion, not hypotension, is the heart of every modern definition. The wedge pressure (PCWP) stands in for left-sided filling pressure, and the cardiac index is cardiac output divided by body surface area."

L = {}

L['CS-01'] = dict(
  sub="Cardiogenic shock → Introduction → Aetiology, sex, associations",
  step=2,
  intro="Step 2 is who gets cardiogenic shock. This card gives the broad picture: the three big sources of a failing pump and the comorbidities that tip a weak heart into shock. It has not been asked directly; the numbers on CS-14 carry the exam weight.",
  parts=[
    ('a', "**Acute coronary syndrome and its complications, acute-on-chronic heart failure, and de novo heart failure (one third of cases).** ACS is the classic cause because it kills muscle suddenly. Modern cardiac ICU registries now see more heart-failure-related shock than infarct shock (about 59% vs 27% in the 2024 SHARC-definition registry), and in those the de novo share was about 28% of heart-failure shock, close to the card’s one third."),
    ('b', "**Men (younger) more than women.** Men have infarcts earlier, so they reach shock younger; women who develop it are older and have more comorbidity."),
    ('c', "**Anaemia, renal dysfunction, metabolic syndromes, COPD.** Each lowers oxygen delivery or reserve: anaemia cuts oxygen content, renal failure adds fluid and acidosis, COPD adds hypoxaemia and right-sided load. They are also the triggers that decompensate chronic heart failure (CS-24)."),
  ],
  mimic=[("De novo vs acute-on-chronic heart failure shock", "De novo has no prior cardiomyopathy (often a first infarct or myocarditis); acute-on-chronic is a known weak heart pushed over by infection, anaemia, arrhythmia or renal failure.")],
  traps=[("“AMI is still the cause in most cardiogenic shock”", "True in older series and still the exam’s default (CS-14), but contemporary cardiac ICU data show heart-failure-related shock is now the larger group.")],
  decode=[("Commonest cause of cardiogenic shock [pattern]", "Acute MI with LV failure — the exam answer, even though modern registries show heart-failure shock overtaking it.")],
  punch="Most cardiogenic shock still begins with a coronary event, but a known failing heart decompensated by infection, anaemia or renal failure is now just as common.",
)

L['CS-02'] = dict(
  sub="Cardiogenic shock → Definitions → Shock, cardiogenic shock, clinical definition",
  step=1,
  intro="Step 1 is drawing the line around cardiogenic shock. Shock is a mismatch of oxygen supply and demand at the tissue level; cardiogenic shock is that mismatch caused by the heart; and the clinical definition demands proof on both the bedside and the laboratory side. The one real question tests the opposite end: recognising when there is no shock at all.",
  parts=[
    ('a', "**Shock: inadequate organ perfusion to meet the tissues’ oxygen demand.** It is defined by the tissues, not by the blood pressure: a normal pressure with a rising lactate is shock, and a low pressure with normal perfusion may not be."),
    ('b', "**Cardiogenic shock: critical end-organ hypoperfusion and hypoxia due to a primary cardiac disorder.** The word ‘primary’ separates it from septic myocardial depression, where the heart is a casualty of another process (CS-12)."),
    ('c', "**Clinical definition: a cardiac disorder producing BOTH clinical AND biochemical evidence of tissue hypoperfusion.** Cold, clammy skin or confusion alone can be anxiety or cold; a lactate alone can be adrenaline or liver failure. Requiring both raises specificity, which is why modern definitions (ESC 2021, SCAI) pair signs with lactate."),
  ],
  mimic=[("Cardiogenic shock vs decompensated heart failure", "Both have a low output and high filling pressures; only shock has hypoperfusion (lactate, oliguria, confusion) — the point tested on CS-05.")],
  traps=[("“Wheezing, tachycardia 100 and breathless — must be some form of shock”", "BP 130/80 and CVP 6 with no sign of hypoperfusion is no shock at all; 90% got this right.")],
  decode=[("Asthmatic, wheeze, BP 130/80, HR 100, CVP 6: haemodynamic status? [DocT QBank]", "Acute asthma without shock — normal pressure, normal CVP, no hypoperfusion (90%).")],
  punch="Shock is a tissue diagnosis; cardiogenic shock is that tissue failure caused by the heart and proven by both signs and biochemistry.",
)

L['CS-03'] = dict(
  sub="Cardiogenic shock → Definitions → SHOCK trial criteria",
  step=1,
  intro="Step 1 continues with the trial definitions. The SHOCK trial (1999) set the classic research definition, and it is the only one of the three that demands measured haemodynamics, so it is the one quoted when a stem gives a wedge pressure and a cardiac index.",
  parts=[
    ('a', "**SBP <90 mmHg for ≥30 min.** Thirty minutes excludes the transient dip of a vagal reaction or a drug bolus."),
    ('b', "**Or support needed to keep SBP ≥90 mmHg.** A patient already on norepinephrine with a ‘normal’ pressure still qualifies, because the drug is hiding the shock."),
    ('c', "**Plus end-organ hypoperfusion: urine output <30 mL/h or cool extremities.** These are the bedside proofs that the low pressure is starving organs."),
    ('d', "**Haemodynamic: CI ≤2.2 L/min/m² AND PCWP ≥15 mmHg.** The low index proves the pump is failing; the raised wedge proves the ventricle is full, so the problem is not hypovolaemia. Many textbooks quote a split threshold (CI <1.8 without support, <2.2 on support), but the trial itself used ≤2.2 and ≥15."),
  ],
  mimic=[("Cardiogenic vs hypovolaemic shock on a PA catheter", "Both have a low CI and high SVR; the wedge is high in cardiogenic and low in hypovolaemic shock.")],
  traps=[("“A low cardiac index alone defines cardiogenic shock”", "Hypovolaemic and obstructive shock also have a low index; it is the combination with a high wedge that points to the left ventricle.")],
  decode=[("Shock with elevated PCWP — which type? [Marrow]", "Cardiogenic: PCWP ≥15 with CI ≤2.2 (SHOCK criteria)."),
          ("Which definition carries haemodynamic criteria? [pattern]", "Only the SHOCK trial; IABP-SHOCK II and ESC are clinical (CS-07).")],
  punch="SHOCK is the definition with numbers from the catheter: CI ≤2.2 with a wedge ≥15, on top of 30 minutes of hypotension and hypoperfusion.",
)

L['CS-04'] = dict(
  sub="Cardiogenic shock → Definitions → IABP-SHOCK II criteria",
  step=1,
  intro="Step 1, the second trial definition. IABP-SHOCK II (2012, n 600) used a purely clinical definition that could be applied at the cath-lab door without a PA catheter, and it added two things SHOCK did not: pulmonary congestion and a lactate threshold.",
  parts=[
    ('a', "**SBP <90 mmHg for ≥30 min.** The same pressure and duration as SHOCK."),
    ('b', "**Or catecholamines needed to keep SBP >90 mmHg.** ‘Catecholamines’ rather than ‘support’: the drug, not a device, defines the alternative."),
    ('c', "**Plus pulmonary congestion.** This replaces the wedge pressure: crackles or oedema on the film stand in for PCWP ≥15 and exclude the dry, hypovolaemic patient."),
    ('d', "**Plus impaired end-organ perfusion: altered mental status, cold/clammy skin and extremities, urine output <30 mL/h, lactate >2.0 mmol/L.** Any one of the four suffices. The lactate threshold is the definition’s distinctive feature (CS-07)."),
  ],
  mimic=[("IABP-SHOCK II vs SHOCK definition", "IABP-SHOCK II asks for congestion and allows lactate >2; SHOCK asks for CI ≤2.2 and PCWP ≥15.")],
  traps=[("“IABP-SHOCK II showed the balloon pump saves lives”", "It did not: 30-day mortality 39.7% vs 41.3%, which is why routine IABP is now class III in ESC 2023 and the 2025 ACC/AHA guideline.")],
  decode=[("Which definition includes lactate >2 mmol/L? [pattern]", "IABP-SHOCK II only.")],
  punch="IABP-SHOCK II defines shock clinically — hypotension, congestion and one of four perfusion markers including lactate above 2 — and the trial itself found the balloon pump useless.",
)

L['CS-05'] = dict(
  sub="Cardiogenic shock → Definitions → ESC heart failure definition",
  step=1,
  intro="Step 1, the guideline definition. The ESC heart failure guideline defines shock by hypoperfusion and lists its clinical and laboratory signs; the one real question asks what separates shock from simple heart failure, and fewer than half got it.",
  parts=[
    ('a', "**SBP <90 mmHg with adequate volume, plus clinical or laboratory signs of hypoperfusion.** This is the ESC 2016 wording: volume must be adequate so that hypovolaemia is excluded first. ESC 2021 (following the 2020 HFA position statement) defines cardiogenic shock by hypoperfusion from primary cardiac dysfunction and no longer requires hypotension, because compensatory vasoconstriction or drugs can keep the pressure up while the tissues starve — normotensive cardiogenic shock (CS-31)."),
    ('b', "**Clinical hypoperfusion: cold extremities, oliguria, mental confusion, dizziness, narrow pulse pressure.** These are the signs ESC 2021 lists, and the laboratory three in part c are its list too; only the hypotension requirement has gone. Each is the body diverting flow away from skin, kidney and brain; a narrow pulse pressure reflects a small stroke volume."),
    ('c', "**Laboratory hypoperfusion: metabolic acidosis, raised lactate, raised creatinine.** Lactate is the most direct marker of anaerobic metabolism and is the one used to stage shock (SCAI C: ≥2 mmol/L)."),
  ],
  mimic=[("Cardiogenic shock vs acute decompensated heart failure", "Both have a low CI and a high PCWP; only shock has hypoperfusion, so the lactate separates them.")],
  traps=[("“A cardiac index under 2.2 or a wedge over 18 separates shock from heart failure”", "Decompensated heart failure has the same numbers; 46% picked lactate. Hypoperfusion defines shock; the catheter numbers only say the pump is the cause."),
         ("“ESC still requires SBP <90”", "That is the 2016 wording on the card; ESC 2021 accepts hypoperfusion without hypotension.")],
  decode=[("Post-MI, CI 1.9, PCWP 19, oliguria, raised lactate: which finding separates shock from isolated HF? [DocT GT]", "Elevated lactate — hypoperfusion (46%).")],
  punch="What turns heart failure into cardiogenic shock is hypoperfusion — a raised lactate, oliguria, confusion — not a lower cardiac index.",
)

L['CS-06'] = dict(
  sub="Cardiogenic shock → Diagnosis → Three clinical criteria",
  step=1,
  intro="Step 1 at the bedside: in practice the diagnosis rests on three things — persistent hypotension, no response to fluid and proven hypoperfusion. The one real question flips the CS-05 logic: here the shock is already established, and it asks what proves the heart is the cause.",
  parts=[
    ('a', "**Persistent hypotension: SBP <90 mmHg.** Persistent means sustained (the trials used 30 minutes), not a single reading."),
    ('b', "**No adequate response to volume resuscitation.** Fluid unresponsiveness separates the empty circulation (which recovers with fluid) from the failing pump (which does not, and may get worse)."),
    ('c', "**End-organ hypoperfusion, clinical AND biochemical.** As on CS-02, both are needed."),
  ],
  mimic=[("“Is this shock?” vs “Is this shock cardiogenic?”", "The first is answered by hypoperfusion (lactate, CS-05); the second by a raised filling pressure (PCWP >15) with a low output.")],
  traps=[("“Cold extremities or a narrow pulse pressure confirm cardiogenic shock”", "They show hypoperfusion and a small stroke volume, which any low-output shock has; the raised wedge is what pins it on the left ventricle."),
         ("“Lactate 2 mmol/L confirms it”", "A lactate of exactly 2 is borderline, and lactate does not tell you the cause.")],
  decode=[("Anterior MI, SBP 86 for 40 min on norepinephrine, CI 1.8, PCWP 20, UO 20 mL/h: which finding confirms cardiogenic shock? [DocT GT]", "PCWP >15 — the full ventricle proves a pump problem.")],
  punch="Hypoperfusion tells you it is shock; a high wedge with a low cardiac index tells you the heart caused it.",
)

L['CS-07'] = dict(
  sub="Cardiogenic shock → Definitions → The three compared",
  step=1,
  intro="Step 1 side by side. Each definition adds one distinctive element, and examiners ask which one carries it. Not asked directly, but CS-03 to CS-06 questions turn on these differences.",
  parts=[
    ('a', "**SHOCK trial: CI ≤2.2 and PCWP ≥15.** The only definition that needs a catheter."),
    ('b', "**IABP-SHOCK II: pulmonary congestion required.** Congestion is its bedside substitute for a raised wedge."),
    ('c', "**ESC HF: adequate volume first.** The ESC wording builds fluid adequacy into the definition (2016); ESC 2021 dropped the hypotension requirement (CS-05)."),
    ('d', "**Urine output <30 mL/h in SHOCK and IABP-SHOCK II; lactate >2.0 only in IABP-SHOCK II.** The two trials share the oliguria cut-off; only IABP-SHOCK II names a lactate."),
  ],
  mimic=[("SHOCK vs IABP-SHOCK II support clause", "SHOCK: any support to keep SBP ≥90; IABP-SHOCK II: catecholamines to keep SBP >90.")],
  traps=[("“Lactate >2 is part of the SHOCK definition”", "It is not; SHOCK used urine output or cool extremities.")],
  decode=[("Which definition requires pulmonary congestion? [pattern]", "IABP-SHOCK II."),
          ("Which builds adequate volume into the wording? [pattern]", "ESC HF guideline.")],
  punch="SHOCK has the catheter numbers, IABP-SHOCK II has congestion and lactate, and ESC has adequate volume.",
)

L['CS-08'] = dict(
  sub="Cardiogenic shock → Staging → SCAI stages A–E",
  step=1,
  intro="Step 1 ends with severity. The SCAI classification (2019, updated 2022) grades shock from at-risk to extremis so that teams speak the same language and escalate on time; mortality climbs steeply with each stage. Not asked directly here, but the B–C boundary underlies CS-05.",
  parts=[
    ('a', "**A — At risk: risk factors, no signs or symptoms (large AMI, prior infarct, acute or acute-on-chronic HF).** Normal exam and normal lactate."),
    ('b', "**B — Beginning: relative hypotension or tachycardia WITHOUT hypoperfusion.** Lactate is normal; the patient is compensating."),
    ('c', "**C — Classic: hypoperfusion needing an intervention beyond volume (inotrope, pressor, MCS or ECMO), typically with relative hypotension.** The 2022 update puts lactate at ≥2 mmol/L and the CI typically <2.2 here."),
    ('d', "**D — Deteriorating: fails to respond to initial interventions; like C and getting worse.** Lactate stays high or rises and support escalates."),
    ('e', "**E — Extremis: on multiple interventions, may be in cardiac arrest with ongoing CPR and/or ECMO.** The 2022 table adds lactate ≥8 and pH <7.2."),
    ('f', "**Arrest (A) modifier: CPR, including defibrillation.** The 2022 update narrows it to arrest with coma (unresponsive to voice), because a brief arrest with prompt awakening does not carry the same risk; the update also adds a three-axis model (stage, phenotype and aetiology, risk modifiers such as age)."),
  ],
  mimic=[("SCAI B vs C", "B has hypotension or tachycardia with normal perfusion; C has hypoperfusion that needs more than fluid.")],
  traps=[("“Hypotension defines stage C”", "Hypoperfusion defines C; a hypotensive but well-perfused patient is B, and a normotensive hypoperfused one can be C.")],
  decode=[("Post-MI, BP 88/60, HR 110, warm, lactate 1.4, good urine output: SCAI stage? [pattern]", "B — hypotension without hypoperfusion."),
          ("Already on two pressors and a device, lactate rising: stage? [pattern]", "D — failing initial support.")],
  punch="SCAI staging turns on hypoperfusion: B is low pressure without it, C is hypoperfusion needing more than fluid, D is failing that, E is collapse.",
)

L['CS-09'] = dict(
  sub="Cardiogenic shock → Aetiology → Six branches",
  step=2,
  intro="Step 2 needs a framework for causes. Six branches cover every way the heart can fail as a pump; the detail sits on CS-10 to CS-13. Not asked directly.",
  parts=[
    ('a', "**Myocardial.** The muscle itself: infarction, cardiomyopathy, myocarditis, stunning (CS-10 to CS-12)."),
    ('b', "**Mechanical complication.** Papillary muscle, septal or free-wall rupture after infarction."),
    ('c', "**Valvular, native or prosthetic.** Stenosis blocks forward flow; acute regurgitation volume-loads a ventricle that has not had time to dilate."),
    ('d', "**Electrical.** Too fast (no filling time), too slow (too few beats) or uncoordinated."),
    ('e', "**Extra-cardiac / obstructive.** Tamponade, constriction, massive PE: the heart is normal but cannot fill or eject."),
    ('f', "**Other.** Toxins and hypothermia depressing the myocardium."),
  ],
  mimic=[("Obstructive vs cardiogenic", "Many classifications keep obstructive shock separate; this framework folds it in because the final common path is a low cardiac output.")],
  traps=[("“Tamponade is cardiogenic”", "In the four-category physiological classification it is obstructive; this card files it under an extra-cardiac branch of cardiogenic shock (CS-13).")],
  decode=[("Classify this cause of low-output shock [pattern]", "Pick the branch by where the pump fails: muscle, structure, valve, rhythm, obstruction, other.")],
  punch="Every cardiogenic shock is muscle, mechanics, valve, rhythm, obstruction or toxin; asking which one points straight at the fix.",
)

L['CS-10'] = dict(
  sub="Cardiogenic shock → Aetiology → AMI: muscle loss and complications",
  step=2,
  intro="Step 2’s commonest cause: myocardial infarction. How much muscle is lost decides whether shock follows. Not asked directly, but the mechanical complications return on CS-32 and CS-33.",
  parts=[
    ('a', "**More than 40% loss of LV mass causes shock on its own.** Autopsy studies of fatal infarct shock found at least 40% of the LV destroyed, old and new together, which is why a second infarct in a scarred heart is so dangerous."),
    ('b', "**Less than 40% loss causes shock only with an added arrhythmia or vasodilation.** A smaller infarct is tipped over by AF, VT or bradycardia (lost filling or rate) or by a systemic inflammatory response that drops SVR."),
    ('c', "**Right ventricular infarction.** Usually with an inferior infarct; the RV cannot fill the LV, so the patient is hypotensive with clear lungs and a high JVP and needs preload, not diuretics (CS-31)."),
    ('d', "**Mechanical complications: papillary muscle rupture, ventricular septal rupture, free-wall rupture.** Usually within the first week (classically days 3–5, but in the reperfusion era often within the first 24 hours), typically after a first, late-presenting or unreperfused infarct; a new murmur or sudden collapse is the clue."),
  ],
  mimic=[("Papillary muscle rupture vs post-infarct VSD", "Both give a new systolic murmur after MI; papillary rupture gives flash pulmonary oedema (often inferior MI), VSD gives a left-to-right shunt with an O₂ step-up in the RV.")],
  traps=[("“Under 40% loss rules out cardiogenic shock”", "Not if an arrhythmia or vasodilation is added: 30% loss plus fast AF is still cardiogenic shock.")],
  decode=[("Inferior MI, hypotension, clear lungs, raised JVP [pattern]", "RV infarction — give fluid, avoid nitrates and diuretics.")],
  punch="Lose 40% of the left ventricle and shock follows; lose less and it takes an arrhythmia, vasodilation, RV infarction or a rupture to get there.",
)

L['CS-11'] = dict(
  sub="Cardiogenic shock → Aetiology → Heart failure, cardiomyopathies, pregnancy, endocrine",
  step=2,
  intro="Step 2, the non-infarct muscle causes. These are the stems where coronary angiography is normal or the history points elsewhere — drink, a stressor, pregnancy, a thyroid. Four real questions, and the alcohol one was missed by two thirds.",
  parts=[
    ('a', "**Acute decompensated HF: chronic HF of known cause that decompensates, or acute HF as the first presentation.** These are the two heart-failure-related shock groups (CS-01)."),
    ('b', "**Chronic ischaemia, dilated cardiomyopathy, myocarditis, stress-induced (Takotsubo) cardiomyopathy.** Alcoholic cardiomyopathy is a dilated cardiomyopathy: heavy drinking for years (often quoted as >80 g a day for >5 years) gives a large, poorly contracting ventricle, cold low-output failure that needs inotropes, partly reversible with abstinence. Takotsubo follows an emotional or physical stressor, usually in a post-menopausal woman: ST elevation or deep T inversion, a modest troponin rise, unobstructed coronaries and apical ballooning with a hyperkinetic base; it recovers over weeks. Its danger is dynamic LVOT obstruction, where inotropes make it worse (CS-33)."),
    ('c', "**Pregnancy-associated: peripartum cardiomyopathy, coronary artery dissection.** PPCM is LV systolic failure (EF <45%) late in pregnancy or the months after delivery. A better outlook is predicted at diagnosis by a less dilated ventricle (LVEDD under about 5.5–6 cm), EF above 30–35% (fractional shortening >20%), no troponin rise and no LV thrombus. Spontaneous coronary dissection is the commonest cause of MI in pregnancy."),
    ('d', "**Endocrine: hypo- or hyperthyroidism, phaeochromocytoma.** Thyroid storm gives high-output failure and fast AF; profound hypothyroidism a weak, slow heart; phaeochromocytoma a catecholamine cardiomyopathy that can look exactly like Takotsubo."),
  ],
  mimic=[("Alcoholic cardiomyopathy vs wet beriberi", "Both in drinkers; beriberi is warm, high-output failure with low SVR that reverses within hours of thiamine, cardiomyopathy is cold, low-output and persists after thiamine."),
         ("Takotsubo vs anterior STEMI", "Same ECG and chest pain; angiography shows open coronaries and a wall-motion abnormality beyond one coronary territory.")],
  traps=[("“Alcoholic with Wernicke’s, hypotension after thiamine — neurogenic shock”", "Wernicke’s has no cord lesion to cut sympathetic outflow; shock persisting after thiamine is alcoholic dilated cardiomyopathy (only 34% right). Sepsis from aspiration is the other popular wrong pick, but nothing in the stem suggests it."),
         ("“Takotsubo with hypotension — start dobutamine”", "If the base is hyperkinetic and the outflow obstructed, inotropes increase the gradient; use fluid, phenylephrine and a beta-blocker.")],
  decode=[("Chronic drinker, confusion, ataxia, ophthalmoplegia; hypotension persists after thiamine [DocT QBank]", "Alcoholic cardiomyopathy causing cardiogenic shock (34%)."),
          ("Woman, chest pain and ST elevation after sudden bereavement, clean coronaries [DocT GT PYQ; NEET 2024]", "Takotsubo cardiomyopathy."),
          ("Peripartum cardiomyopathy: favourable prognostic factors [Marrow]", "All of the above — small LVEDD, EF >30–35%, no troponin rise, no thrombus.")],
  punch="When the coronaries are clean, think muscle: alcohol (persists after thiamine), stress (Takotsubo, beware the outflow tract), pregnancy and the endocrine glands.",
)

L['CS-12'] = dict(
  sub="Cardiogenic shock → Aetiology → Post-cardiotomy, LVOT, post-arrest, septic, contusion",
  step=2,
  intro="Step 2, the remaining muscle causes — mostly hearts stunned by something else: bypass, arrest, sepsis or a blow. Two real questions: post-CABG low output and blunt cardiac injury.",
  parts=[
    ('a', "**Post-cardiotomy shock: prolonged cardiopulmonary bypass, insufficient cardioprotection.** Ischaemia during cross-clamp and reperfusion injury stun the myocardium; output is lowest at about 6–12 hours after bypass. Cold, clammy, confused and oliguric in that window is low cardiac output syndrome. Treat by optimising preload and afterload, correcting potassium, magnesium and calcium, fixing rate and rhythm (epicardial pacing), then inotropes (dobutamine or milrinone), IABP or MCS if refractory, and always exclude tamponade and graft failure."),
    ('b', "**Dynamic outflow tract obstruction.** A small, hyperdynamic ventricle (hypertrophy, Takotsubo, hypovolaemia, inotropes) pulls the mitral leaflet into the outflow tract (CS-33)."),
    ('c', "**Post-cardiac-arrest stunning.** Global ischaemia–reperfusion depresses the heart for 24–72 hours and usually recovers."),
    ('d', "**Myocardial depression in septic shock or SIRS.** Cytokines and nitric oxide depress contractility; it is reversible and secondary, which is why it is not primary cardiogenic shock (CS-02)."),
    ('e', "**Myocardial contusion.** Blunt chest trauma bruises the muscle (usually the anterior RV). Screen with ECG and troponin: if either is abnormal, monitor for 24–48 hours for arrhythmia, and echo if unstable; normal ECG with normal troponin effectively excludes significant injury."),
  ],
  mimic=[("Low cardiac output syndrome vs tamponade after cardiac surgery", "Both are cold and oliguric; tamponade has rising, equalising filling pressures, falling drain output and a clot on echo, and needs re-opening, not inotropes.")],
  traps=[("“Post-CABG low output — start high-dose vasoconstrictors”", "Raising SVR in a stunned ventricle lowers output further; optimise loading, rhythm and electrolytes, then inotropes (97% got this right).")],
  decode=[("8 h after on-pump CABG: confused, cold, clammy, oliguric — next? [DocT GT]", "Optimise preload and afterload, correct electrolytes, inotrope if needed (97%)."),
          ("Stable blunt chest trauma with PVCs on ECG — next? [Marrow]", "Admit for 24–48 h cardiac monitoring.")],
  punch="Bypass, arrest, sepsis and trauma all stun the heart; treat the stunned ventricle by loading, rhythm and inotropes, and never miss tamponade after surgery.",
)

L['CS-13'] = dict(
  sub="Cardiogenic shock → Aetiology → Valvular, electrical, obstructive, other",
  step=2,
  intro="Step 2’s last branches. Two Marrow questions test the edges of the classification: what counts as obstructive shock, and which lesions block forward flow.",
  parts=[
    ('a', "**Native valve: stenosis, acute regurgitation, valvular obstruction.** Acute regurgitation is the deadly one: a normal-sized ventricle suddenly takes a large regurgitant volume, so filling pressures soar (CS-32)."),
    ('b', "**Prosthetic valve: obstruction (thrombus, pannus), leaflet failure or restriction, mechanical failure, dehiscence.** A new murmur or muffled clicks with shock in a patient with a prosthetic valve is valve thrombosis until shown otherwise."),
    ('c', "**Electrical: atrial arrhythmia with rapid ventricular rate, VT, bradycardia.** A fast rate cuts filling time; a slow one cuts beats per minute."),
    ('d', "**Extra-cardiac / obstructive: cardiac tamponade, constriction, pulmonary embolism.** The wider physiological list of obstructive shock also includes tension pneumothorax and aortic dissection, and ‘obstruction to forward flow’ includes critical AS, dynamic LVOT obstruction (HCM), mitral stenosis and LA myxoma."),
    ('e', "**Other: toxidromes, hypothermic myocardial depression.** Beta-blockers, calcium-channel blockers and other cardiotoxins; cold depresses contractility and rate."),
  ],
  mimic=[("Obstructive vs distributive (adrenal crisis)", "Adrenal crisis is distributive (endocrine) shock with low SVR; obstructive shock has a high SVR and a low output from blocked filling or ejection.")],
  traps=[("“Myocardial contusion obstructs forward flow”", "Contusion reduces contractility; it belongs with the myocardial causes, not with AS, HCM, MS and tamponade.")],
  decode=[("Which is NOT obstructive shock? [Marrow]", "Adrenal crisis — distributive."),
          ("Cardiogenic shock from mechanical obstruction to forward flow [Marrow]", "AS, HCM (dynamic LVOT), MS, tamponade — not contusion.")],
  punch="Valves, rhythm and obstruction are the non-muscle causes; obstruction means blocked filling or ejection, never a weak muscle and never adrenal crisis.",
)

L['CS-14'] = dict(
  sub="Cardiogenic shock → Epidemiology → AMI share, incidence, mortality",
  step=2,
  intro="Step 2’s numbers. These are the classic figures quoted in older reviews; not asked directly, but the STEMI–NSTEMI swap is a standard trap.",
  parts=[
    ('a', "**AMI accounts for 80% of cardiogenic shock.** This is the older, infarct-era figure (reviews quote 60–80%). In contemporary cardiac ICUs AMI shock is about 27% and heart-failure shock about 59% (2024 registry), so expect the classic figure in the exam but know it is changing."),
    ('b', "**Cardiogenic shock complicates 5–10% of acute MI.** Most series give 5–8%."),
    ('c', "**It is the leading cause of death after MI.** In-hospital death of infarct shock remains around 40–50% despite revascularisation."),
    ('d', "**STEMI causes about twice as many cases as NSTEMI, but NSTEMI shock has the higher mortality.** NSTEMI patients are older, with more multivessel disease and comorbidity, and shock develops later, often after the window for early revascularisation."),
    ('e', "**6- and 12-month mortality about 50%.** Most of the deaths happen in the first month; survivors have a reasonable long-term outlook."),
    ('f', "**18.6% 30-day readmission (MI and CHF).** From the US Nationwide Readmissions Database; heart failure was the commonest cardiac reason, infection the commonest non-cardiac one."),
  ],
  mimic=[("Frequency vs mortality", "STEMI more often causes shock; NSTEMI kills more of the shocks it causes.")],
  traps=[("“NSTEMI causes more cardiogenic shock”", "It is STEMI that causes more; NSTEMI only wins on mortality.")],
  decode=[("Incidence of cardiogenic shock in AMI [pattern]", "5–10%."),
          ("Commonest cause of death in hospitalised AMI [pattern]", "Cardiogenic shock.")],
  punch="Shock complicates 5–10% of infarcts and kills about half; STEMI causes more of it, NSTEMI shock kills a larger share.",
)

L['CS-15'] = dict(
  sub="Cardiogenic shock → Pathophysiology → Pressure–volume loops",
  step=3,
  intro="Step 3 begins with the pressure–volume loop, the picture of one heartbeat. Its width is stroke volume, its top-left corner sits on the end-systolic pressure–volume line (Emax, the slope that measures contractility), and its bottom edge is the diastolic filling curve. Not asked directly.",
  parts=[
    ('a', "**Steady state: the green baseline loop on a steep Emax line.** A normal ventricle fills to about 120 mL, ejects about 70 mL and generates a systolic pressure of about 120 mmHg."),
    ('b', "**Acute MI: Emax flattens (lost contractility) while the loop is drawn little changed.** Early on, compensation (sympathetic drive, a modest rise in filling) keeps stroke volume and pressure near baseline despite the weaker muscle."),
    ('c', "**Cardiogenic shock: the loop shifts right on a flat Emax line.** End-systolic and end-diastolic volumes rise, the loop narrows (smaller stroke volume), its top falls (lower systolic pressure) and the end-diastolic point climbs the stiffer filling curve (high LVEDP, pulmonary congestion)."),
  ],
  mimic=[("Lost contractility vs raised afterload on a PV loop", "Lost contractility flattens the Emax slope; raised afterload makes the loop taller and narrower on the same slope.")],
  traps=[("“A flatter Emax alone means shock”", "Both MI and shock flatten Emax; the rightward shift and narrow loop mark shock (CS-16).")],
  decode=[("Which PV loop shows cardiogenic shock? [pattern]", "Shifted right, narrow, low, with a high end-diastolic pressure on a flat Emax.")],
  punch="In cardiogenic shock the loop slides right, narrows and sinks on a flattened Emax line: big, weak, high-pressure ventricle ejecting little.",
)

L['CS-16'] = dict(
  sub="Cardiogenic shock → Pathophysiology → Reading the PV loops",
  step=3,
  intro="Step 3, the loops read in words. Contractility falls in both MI and shock; what changes once shock supervenes is the position of the loop. Not asked directly.",
  parts=[
    ('a', "**Acute MI: contractility decreased; pressure and volume remain the same; loop position unchanged.** The weaker muscle is still compensated: heart rate, catecholamines and a little more filling hold stroke volume."),
    ('b', "**Cardiogenic shock: contractility decreased; pressure and volume shifted right; loop shifted to the RIGHT.** Volumes rise as the ventricle dilates to use Frank–Starling, but the flat Emax means each beat ejects less and the systolic pressure falls, while filling pressure rises."),
  ],
  mimic=[("Cardiogenic shock vs hypovolaemia on a PV loop", "Hypovolaemia shifts the loop LEFT (small volumes) with normal Emax; cardiogenic shock shifts it right with a flat Emax.")],
  traps=[("“Lower contractility separates shock from MI”", "Both have it; the rightward shift is the discriminator.")],
  decode=[("PV loop with reduced Emax and rightward shift [pattern]", "Cardiogenic shock (not uncomplicated MI).")],
  punch="Contractility falls in both; only shock drags the loop to the right.",
)

L['CS-17'] = dict(
  sub="Cardiogenic shock → Pathophysiology → The neurohormonal spiral",
  step=3,
  intro="Step 3’s engine. A falling output is sensed by baroreceptors and kidneys, and the reflexes meant to defend blood pressure end up overloading the injured heart. The one real question asks which part of this response does the most damage.",
  parts=[
    ('a', "**Myocardial injury → reduced cardiac output.** The starting point of the spiral."),
    ('b', "**→ less carotid baroreceptor stimulation and less renal perfusion.** The baroreceptors sense lower pressure and stop restraining sympathetic outflow; the juxtaglomerular cells sense less flow and release renin."),
    ('c', "**→ activation of the SNS and RAAS.**"),
    ('d', "**SNS: more heart rate and inotropy, and myocardial toxicity; inhibited by beta-blockers.** Tachycardia and inotropy raise oxygen demand in a heart already short of supply, and chronic catecholamine exposure injures myocytes."),
    ('e', "**RAAS: angiotensin II vasoconstriction (more afterload) and aldosterone salt retention (more preload); inhibited by ACE inhibitors, ARBs, aldosterone antagonists and ADH antagonists.** Higher afterload raises wall stress and myocardial oxygen demand and lowers stroke volume; more preload raises LVEDP, pulmonary congestion and subendocardial ischaemia."),
    ('f', "**Common end point: negative remodelling and worse LV function → heart failure; BNP and ANP oppose the vasoconstriction and fluid retention.** Natriuretic peptides are the counter-regulatory brake, which is why BNP rises with stretch (CS-22). In about a fifth of infarct shock a systemic inflammatory response adds vasodilation, so SVR is not always high."),
  ],
  mimic=[("Afterload vs preload harm in the spiral", "Afterload (angiotensin II, catecholamines) raises wall stress and cuts stroke volume; preload (aldosterone, ADH) raises filling pressure and congestion.")],
  traps=[("“Reduced oxygen extraction or capillary recruitment worsens the injury”", "These are distractors; the direct harm of a persistently high SVR is a higher afterload, which raises myocardial wall stress and oxygen demand.")],
  decode=[("Large anterior MI, shock, SVR stays high after reperfusion: what worsens myocardial injury? [DocT GT]", "Increased cardiac afterload.")],
  punch="The reflexes that defend blood pressure raise afterload and preload on an injured heart, and that extra load is what drives the spiral.",
)

L['CS-18'] = dict(
  sub="Cardiogenic shock → Haemodynamic profiles → Forrester quadrants",
  step=4,
  intro="Step 4 sorts the patient by perfusion and congestion. Forrester (1976) did this with a PA catheter after MI; the same quadrants (cold or warm, wet or dry) are now read at the bedside. Four real questions, mostly the ‘high CVP plus low BP’ pattern.",
  parts=[
    ('a', "**Cold and wet: classic cardiogenic shock — CI down, SVRI up, PCWP up.** Low output, compensatory vasoconstriction and a congested left heart; about two thirds of infarct shock."),
    ('b', "**Cold and dry: euvolaemic cardiogenic shock — CI down, SVRI up, PCWP normal.** Low output without congestion; these patients may tolerate small fluid boluses (CS-31)."),
    ('c', "**Warm and wet: vasodilatory cardiogenic or mixed shock — CI down, SVRI down or normal, PCWP up.** A failing heart plus inflammation or sepsis that drops vascular tone; needs norepinephrine."),
    ('d', "**Warm and dry: vasodilatory shock, NOT cardiogenic — CI up, SVRI down, PCWP down.** The only quadrant with a high output; this is the profile of sepsis and other distributive states."),
  ],
  mimic=[("High-CVP shock: cardiogenic vs obstructive vs RV failure", "All have a high CVP; a high wedge with a low CI and poor LV is cardiogenic, a low wedge with a high CVP is RV failure, PE or tamponade.")],
  traps=[("“Thyrotoxicosis or AV shunts are the commonest cause of high-output hypotension”", "They cause high output, but sepsis is by far the commonest (63% right).")],
  decode=[("Prior MI, BP 80/50, HR 110, CVP 15 [DocT QBank]", "Cardiogenic shock from LV dysfunction (88%)."),
          ("Chronic HF, BP 90/50, CVP 18, low EF [DocT QBank]", "Cardiogenic shock (93%)."),
          ("Older patient, cold shock, high CVP, PCWP and SVR [Marrow]", "Acute MI — classic wet and cold."),
          ("Commonest cause of high-output hypotension [DocT QBank]", "Sepsis (63%).")],
  punch="Three Forrester quadrants have a low cardiac index and are cardiogenic; warm and dry has a high one and is not cardiogenic shock at all.",
)

L['CS-19'] = dict(
  sub="Cardiogenic shock → Haemodynamic profiles → Bedside correlates",
  step=4,
  intro="Step 4 without a catheter. Congestion is heard, seen on the film and counted on lung ultrasound; perfusion is felt in the hands. Four real questions test recognising pulmonary oedema and acute heart failure from bedside clues.",
  parts=[
    ('a', "**Wet: pulmonary congestion — dyspnoea and orthopnoea; CXR pulmonary oedema; lung ultrasound B lines.** B lines are vertical artefacts from thickened, fluid-filled interlobular septa; three or more per intercostal space in several zones on both sides with preserved sliding is interstitial oedema. An S3 with bibasal crackles adds weight: it is rapid early filling into a stiff, overfull ventricle with a high LVEDP — specific (about 90%) but insensitive."),
    ('b', "**Dry: does NOT show signs of pulmonary congestion.** Clear lungs, A lines on ultrasound, no orthopnoea."),
    ('c', "**Warm type: can present as hypertensive heart failure.** Perfusion is maintained and the pressure is high; the problem is afterload and redistribution of fluid into the lungs, treated with nitrates (CS-28)."),
  ],
  mimic=[("Hypertensive acute heart failure vs aortic dissection", "Both give chest pain with severe hypertension; pulmonary oedema with no pulse or BP differential and no widened mediastinum points to acute heart failure."),
         ("B lines vs pneumothorax", "Pneumothorax abolishes sliding and B lines; oedema has many B lines with preserved sliding.")],
  traps=[("“BP 200/120, chest pain, confusion and oedema — aortic dissection or AMI”", "A normal ECG and pulmonary oedema make it acute (hypertensive) heart failure; 68% right."),
         ("“Oedema with CVP 18 is CKD fluid overload”", "Possible, but in a hypertensive diabetic with breathlessness the expected answer is acute pulmonary oedema from LV failure (83%).")],
  decode=[("HTN, diabetes, breathless, oedema, BP 100/60, CVP 18 [DocT QBank]", "Acute pulmonary oedema due to left heart failure (83%)."),
          ("BP 200/120, chest pain, disoriented, normal ECG, pulmonary oedema on CXR [DocT QBank]", "Acute heart failure (68%)."),
          ("CAD, crackles, S3, sinus tachycardia, no ST change [DocT QBank]", "Congestive heart failure (89%)."),
          ("Lung ultrasound >3 B lines per field, sliding preserved [DocT QBank]", "Pulmonary oedema (86%).")],
  punch="Wet is crackles, oedema on the film and B lines on ultrasound; warm and wet with a high pressure is hypertensive heart failure.",
)

L['CS-20'] = dict(
  sub="Cardiogenic shock → Monitoring → Frequency and rationale",
  step=4,
  intro="Step 4 continues once the patient is profiled: how closely to watch. These frequencies come from the AHA 2017 cardiogenic shock statement; not asked directly, but the CVP point recurs across shock questions.",
  parts=[
    ('a', "**Telemetry, pulse oximetry, respiratory rate: continuous — arrhythmias, ventilatory failure and pulmonary oedema are common.**"),
    ('b', "**Critical care unit monitoring: 1:1 nurse-to-patient ratio — haemodynamic deterioration and multi-organ failure are common.**"),
    ('c', "**Arterial BP: continuous, until vasoactive drugs have been off for 12–24 h.** Cuff pressures are unreliable in vasoconstricted, low-output patients."),
    ('d', "**CVP: continuous; a single value is unreliable, trends inform fluid status.** One CVP number depends on compliance, intrathoracic pressure and the RV, so it predicts fluid response poorly; the direction of change is more useful."),
    ('e', "**Central venous oxygen saturation: every 4 h — trends track cardiac output.** With constant oxygen consumption and haemoglobin, a falling ScvO₂ means more extraction because delivery (output) has fallen."),
    ('f', "**Urine output: hourly — renal perfusion and AKI.**"),
    ('g', "**PAC or non-invasive cardiac output monitor: selected use — early if not responding to initial therapy or the diagnosis is uncertain.** Routine PA catheters did not improve outcomes in unselected patients, but in refractory shock they separate LV, RV and mixed failure and guide devices."),
  ],
  mimic=[("ScvO₂ vs lactate", "ScvO₂ falls when delivery falls relative to demand; lactate rises when tissues have already turned anaerobic.")],
  traps=[("“A CVP of 8 means the patient is adequately filled”", "A single CVP is unreliable; follow the trend and the response to a challenge.")],
  decode=[("Which monitored variable is unreliable as a single value? [pattern]", "CVP."),
          ("When is a PA catheter indicated in cardiogenic shock? [pattern]", "Failure to respond to initial therapy or diagnostic uncertainty.")],
  punch="Watch continuously, trend the CVP and ScvO₂ rather than trusting single values, and bring in a PA catheter when the patient fails to respond.",
)

L['CS-21'] = dict(
  sub="Cardiogenic shock → Monitoring → Laboratory frequency",
  step=4,
  intro="Step 4’s laboratory rhythm, also from AHA 2017. Lactate is the test that drives decisions. Not asked directly.",
  parts=[
    ('a', "**Complete blood count: every 12–24 h, more often if bleeding.** Devices, anticoagulants and antiplatelets make bleeding common."),
    ('b', "**Electrolytes: every 6–12 h.** Diuretics and renal failure shift potassium and magnesium, and low levels provoke arrhythmias."),
    ('c', "**Creatinine: every 12–24 h — renal perfusion and AKI.**"),
    ('d', "**Liver function: daily — congestive hepatopathy and hypoperfusion.** A sharp transaminase rise (‘shock liver’) signals hypoperfusion; cholestasis signals congestion."),
    ('e', "**Lactate: every 1–4 h; clearance marks resolving hypoperfusion, failure to clear predicts death.** Lactate trajectory moves the SCAI stage from C to D (CS-08)."),
    ('f', "**Coagulation: every 4–6 h on anticoagulants until stable, otherwise daily.** Hepatic congestion alters drug handling and devices need anticoagulation."),
  ],
  mimic=[("Ischaemic hepatitis vs congestive hepatopathy", "Ischaemic: transaminases in the thousands after a low-output episode, falling within days; congestive: raised bilirubin and ALP with a high CVP.")],
  traps=[("“Lactate once a day is enough”", "It is checked every 1–4 h because clearance (or its absence) is the earliest sign that treatment is working or failing.")],
  decode=[("Which lab trend best predicts mortality in cardiogenic shock? [pattern]", "Lack of lactate clearance.")],
  punch="Repeat lactate every few hours: its clearance is the clearest sign that perfusion is coming back.",
)

L['CS-22'] = dict(
  sub="Cardiogenic shock → Investigations → Echo, ECG, CXR, BNP, lactate",
  step=4,
  intro="Step 4’s first tests. Echo tells you which part of the heart has failed, the ECG whether it is ischaemic, the film whether the patient is wet. Three real questions, and the Kerley-line item was missed by four in five.",
  parts=[
    ('a', "**Echocardiography: LV and RV dysfunction, valvular abnormalities, chamber dimensions, response to therapy.** It also finds the causes that need a different treatment: tamponade, a ruptured papillary muscle or septum, LVOT obstruction."),
    ('b', "**12-lead ECG: exclude arrhythmias and new ischaemia or infarction.** ST elevation or its equivalent sends the patient straight to the cath lab (CS-23)."),
    ('c', "**Chest X-ray: upper-lobe diversion, Kerley B lines, pleural effusion, cardiomegaly.** Kerley lines are thickened, oedematous interlobular septa — not swollen lymphatics, as first thought. B lines are short (about 1 cm) horizontal lines at the peripheral bases, perpendicular to the pleura; A lines are longer (2–6 cm) lines deep in the lung running towards the hila. Cardiogenic oedema also shows perihilar ‘bat-wing’ shadowing, peribronchial cuffing and a widened vascular pedicle (>70 mm); ARDS gives patchy peripheral opacities with a normal heart and pedicle and few effusions or septal lines."),
    ('d', "**Pro-BNP elevated in cardiogenic shock; troponin I.** BNP rises with myocardial stretch or poor clearance, so it is also high in PE (RV strain), AF, renal failure, sepsis, ACS and old age. Obesity lowers it. Sacubitril raises BNP but not NT-proBNP, so NT-proBNP is the marker on an ARNI."),
    ('e', "**Lactate: higher levels mean higher mortality.**"),
  ],
  mimic=[("Cardiogenic oedema vs ARDS on CXR", "Cardiogenic: big heart, upper-lobe diversion, Kerley B lines, effusions; ARDS: normal heart, peripheral patchy opacities, air bronchograms."),
         ("LV failure vs RV failure vs tamponade on echo", "Poor LV with a dilated LV; dilated RV with septal flattening; effusion with diastolic RV collapse.")],
  traps=[("“Kerley lines are swollen pulmonary lymphatics” (marked as true)", "That is the false statement: they are oedematous septa. Only 19% chose it — most thought the A-line description was wrong, but A lines really are the deep lines running to the hila."),
         ("“All of these raise BNP — including hypothyroidism”", "Hypothyroidism has no stretch mechanism and is the usual odd one out; obesity lowers BNP.")],
  decode=[("All true about Kerley lines EXCEPT [DocT GT]", "‘Represent swollen lymphatics’ — they are oedematous interlobular septa (19%)."),
          ("CXR: cardiomegaly, bat-wing opacities, Kerley B lines [DocT GT]", "Cardiogenic pulmonary oedema."),
          ("HF patient, hypotensive, echo shows poor LVEF: cause of shock? [DocT QBank]", "Cardiogenic shock from acute left-sided failure (56%).")],
  punch="Echo finds the failing chamber and the surgical lesions; the film shows wetness, and Kerley lines are oedematous septa, not lymphatics.",
)

L['CS-23'] = dict(
  sub="Cardiogenic shock → Investigations → Cardiac catheterisation",
  step=4,
  intro="Step 4’s invasive test. Angiography both diagnoses and treats when the cause may be ischaemic. Not asked directly, but CS-34 questions turn on it.",
  parts=[
    ('a', "**Indication: acute RV or LV failure of suspected ischaemic aetiology.** ESC 2023 gives immediate angiography with PCI of the culprit a class I recommendation in ACS with shock, whatever the time since symptom onset."),
    ('b', "**Assesses the coronaries, pressures, valves and structural lesions.** Right and left heart pressures, LVEDP and shunt runs are measured in the same sitting."),
    ('c', "**Identifies contributors to the shock.** A septal rupture, severe MR or an unsuspected valve lesion changes the plan to surgery or a device."),
  ],
  mimic=[("Angiography first vs echo first", "Echo at the bedside comes first to exclude tamponade and mechanical lesions; angiography follows immediately if ischaemia is suspected.")],
  traps=[("“Stabilise for 24 h before angiography”", "In infarct shock, delay costs lives; angiography is immediate (SHOCK, CS-35).")],
  decode=[("Cardiogenic shock, suspected ischaemic cause: next step? [pattern]", "Immediate coronary angiography with intent to revascularise.")],
  punch="Suspect ischaemia in cardiogenic shock and you go straight to the cath lab, which both finds and fixes the cause.",
)

L['CS-24'] = dict(
  sub="Cardiogenic shock → Management → Level of care, triggers, shock centres",
  step=5,
  intro="Step 5 starts with where the patient is treated. Shock outcomes depend on volume and on having a team that can offer revascularisation and devices around the clock. Not asked directly.",
  parts=[
    ('a', "**ICU admission for pulmonary oedema, cardiogenic shock, de novo acute heart failure.**"),
    ('b', "**Acute-on-chronic HF decompensates from intercurrent infection, anaemia or renal dysfunction.** Each raises demand or lowers delivery in a heart with no reserve; arrhythmia, ischaemia and stopping medication are the other triggers."),
    ('c', "**ESC: a cardiac ICU is better than a general ICU; AHA does not advocate either.** The AHA 2017 statement prefers organisation (a shock team and hub) over the label on the unit."),
    ('d', "**Regionalised care: centre volume over about 100 cases a year lowers in-hospital mortality; field diagnosis → bypass the nearest non-shock site → direct transfer to a hub shock centre, with the team mobilised after a doctor-to-doctor call.** The volume data come from a US national inpatient sample (Shaefi 2015): the highest-volume quartile of hospitals had lower adjusted in-hospital mortality than those treating 27 or fewer shock cases a year (about 37% vs 42%). Experience with devices, round-the-clock PCI and surgery, and a practised team are the likely reasons."),
  ],
  mimic=[("Hub vs spoke", "The hub offers 24/7 PCI, MCS, cardiac surgery and a shock team; the spoke stabilises and transfers.")],
  traps=[("“Which guideline recommends the CICU over the ICU — AHA”", "It is ESC; AHA takes no position.")],
  decode=[("Commonest triggers of acute-on-chronic decompensation [pattern]", "Infection, anaemia, renal dysfunction (plus arrhythmia, ischaemia, non-adherence).")],
  punch="Shock is treated best in high-volume hub centres with a shock team; ESC prefers the cardiac ICU, AHA does not take sides.",
)

L['CS-25'] = dict(
  sub="Cardiogenic shock → Management → Physiological targets",
  step=5,
  intro="Step 5’s map of treatment: every intervention targets one of the determinants of output — rate, rhythm, preload, afterload, contractility. Not asked directly, but CS-26 to CS-31 are this list applied.",
  parts=[
    ('a', "**Rate: maintain normal sinus rhythm.** Too fast shortens filling, too slow cuts output; aim for a rate the ventricle can fill at."),
    ('b', "**Rhythm: restore sinus rhythm.** The atrial kick supplies a large share of filling in a stiff ventricle; cardiovert unstable AF or VT."),
    ('c', "**Preload: diuretics to lower it; renal replacement if diuretic-resistant.** In the wet patient, lowering LVEDP relieves congestion without much loss of output because the failing ventricle sits on the flat part of its Starling curve."),
    ('d', "**Afterload: vasodilators such as NTG.** A failing ventricle is very sensitive to afterload, so small falls in SVR give large rises in stroke volume — if the pressure allows."),
    ('e', "**Contraction: inotropes — sympathomimetics, inodilators, calcium sensitisers; MAP may fall with inotropes, so norepinephrine is used alongside.** Dobutamine, milrinone and levosimendan all vasodilate (CS-29)."),
  ],
  mimic=[("Afterload reduction vs inotropy", "Both raise stroke volume; vasodilators do it without raising oxygen demand, inotropes at the cost of more demand and arrhythmia.")],
  traps=[("“Diuretics drop output in the wet failing heart”", "On the flat part of the Starling curve, lowering preload relieves congestion with little loss of stroke volume — unless the patient is dry (CS-26 f).")],
  decode=[("Inotrope started, MAP falls: next? [pattern]", "Add norepinephrine (inodilators lower SVR).")],
  punch="Treat cardiogenic shock by its determinants: fix rate and rhythm, lower preload and afterload where the pressure allows, and add an inotrope with norepinephrine behind it.",
)

L['CS-26'] = dict(
  sub="Cardiogenic shock → Management → ESC bedside profile algorithm",
  step=5,
  intro="Step 5 at the bedside: the ESC warm/cold, wet/dry algorithm (ESC 2016) matches treatment to the profile from CS-18 and CS-19. Nine real questions, the most-asked management card, and three of DocT’s keys need care.",
  parts=[
    ('a', "**Wet and warm, vascular type (hypertension predominates): vasodilator + diuretic.** The fluid has been redistributed into the lungs by a sudden afterload rise rather than gained; nitrates unload the ventricle fastest (CS-28)."),
    ('b', "**Wet and warm, cardiac type (congestion predominates): diuretic + vasodilator; ultrafiltration if diuretic-resistant.** Here the patient has gained fluid over days, so IV loop diuretic is the first-line treatment."),
    ('c', "**Wet and cold, SBP <90: inotrope; vasopressor if refractory; diuretic once perfusion is corrected; MCS if no response to drugs.** Diuresing a hypoperfused patient lowers output further, so perfusion comes first. The AHA/SCAI and ACC/AHA 2025 teaching starts norepinephrine first in hypotensive shock and then adds dobutamine; ESC (2021) also prefers norepinephrine when a vasopressor is needed."),
    ('d', "**Wet and cold, SBP ≥90: vasodilators + diuretics; inotrope only if refractory.** With an adequate pressure, unloading improves output without the costs of an inotrope."),
    ('e', "**Dry and warm: compensated — adjust oral therapy.**"),
    ('f', "**Dry and cold: hypoperfused and hypovolaemic — fluid challenge; inotrope if still hypoperfused.** Wet is 95% of acute heart failure presentations, dry 5%. ESC 2021 now organises acute HF by four presentations (decompensated HF, acute pulmonary oedema, isolated RV failure, cardiogenic shock), but the profile logic is unchanged."),
  ],
  table=dict(title="Which drug the stem wants", head=["Stem", "Exam answer"], rows=[
    ["Wet, BP ≥90 (even 95/60)", "IV loop diuretic"],
    ["Wet, hypertensive (SBP 180+)", "Nitroglycerin ± furosemide, NIV"],
    ["Asks for an inotrope, SBP 85, low output", "Dobutamine"],
    ["Shock, MAP <65 or SBP clearly <90, offered norepinephrine", "Norepinephrine first, then dobutamine"],
    ["Hypotension appearing after diuresis", "Stop the diuretic, reassess volume; norepinephrine if a drug is needed"],
  ]),
  mimic=[("Wet-cold SBP <90 vs ≥90", "Below 90: perfusion first (inotrope/pressor), diuretic later; at or above 90: vasodilator and diuretic.")],
  traps=[("“SBP 95/60 with congestion — start norepinephrine”", "95 is above 90 and perfusion is not described as failing; this is wet-warm and needs IV furosemide (73%)."),
         ("“HFrEF, BP 85/50, HR 120: norepinephrine”", "DocT keys dobutamine (58%), following the ESC algorithm; AHA/SCAI would start norepinephrine at this pressure. If the stem says low output and asks for the next drug, choose dobutamine; if it says shock with MAP <65 and offers norepinephrine, choose norepinephrine."),
         ("“Hypotension after diuresis — dopamine” (DocT key)", "Outdated: SOAP II found more arrhythmias and, in the cardiogenic subgroup, higher mortality with dopamine. The patient was 120/80 before diuresis, so this is over-diuresis: hold the diuretic and reassess volume; if a drug is needed, norepinephrine (42% chose the keyed dopamine)."),
         ("“Hypertensive pulmonary oedema — nitroprusside or morphine to lower preload”", "Nitroglycerin is the first-line preload reducer (59%); nitroprusside is a potent balanced arterial and venous dilator that needs arterial-line titration and carries cyanide and thiocyanate risk, so it is kept for refractory hypertension or acute valve regurgitation, and morphine is no longer routine.")],
  decode=[("IHD, orthopnoea, crackles, oedema, BP 130/85 [DocT QBank ×3]", "IV furosemide (86%, 94%, 73% with LVEF 30%)."),
          ("DCM, BP 85/60, HR 110, starting inotropic support [DocT QBank]", "Dobutamine (75%)."),
          ("HFrEF, BP 85/50, HR 120, next step [DocT QBank]", "Dobutamine per DocT (58%); norepinephrine per AHA/SCAI if shock is explicit."),
          ("CHF at a picnic, SpO₂ 85%, BP 185/90: first-line preload reducer [DocT QBank]", "Nitroglycerin (59%).")],
  punch="Read the profile: wet with a pressure gets diuretic and vasodilator, wet and cold gets perfusion first, dry and cold gets fluid — and dopamine is never the modern answer.",
)

L['CS-27'] = dict(
  sub="Cardiogenic shock → Supportive care → Ventilation, induction, renal support",
  step=5,
  intro="Step 5’s supportive measures. Positive pressure is a treatment for the failing left ventricle, not just for the lungs, and examiners test exactly why. Five real questions.",
  parts=[
    ('a', "**CPAP/NIV: more alveolar recruitment, less extravascular lung water, less work of breathing.** Recruiting flooded alveoli improves oxygenation; the pressure gradient pushes fluid back; unloading the respiratory muscles frees cardiac output for other organs."),
    ('b', "**Etomidate preferred at induction because of the risk of haemodynamic collapse.** It has the least effect on SVR and contractility. Its cost is adrenal suppression: one dose blocks 11β-hydroxylase for 24–72 hours, and with azoles (ketoconazole) or enzyme inducers (phenytoin, rifampicin) it can produce critical-illness corticosteroid insufficiency."),
    ('c', "**Positive pressure ventilation has a POSITIVE effect on LV function.** Raised intrathoracic pressure surrounds the LV and lowers its transmural pressure during systole, which is a fall in afterload; it also cuts venous return (preload), which helps the congested ventricle. On the right side it lowers RV preload and raises RV afterload. Removing it at a spontaneous breathing trial does the reverse and can cause weaning-induced pulmonary oedema."),
    ('d', "**Lung-protective ventilation: 6 mL/kg predicted body weight.**"),
    ('e', "**About 20% of cardiogenic shock need CRRT; consider it from KDIGO stage 2 or for life-threatening indications.** Continuous rather than intermittent therapy, because it removes fluid without the swings in pressure that a failing heart cannot tolerate."),
  ],
  mimic=[("PPV in cardiogenic vs hypovolaemic shock", "In cardiogenic shock lowering preload and afterload helps; in hypovolaemic shock the loss of venous return drops output.")],
  traps=[("“CPAP mainly reduces preload” (true?)", "False: it reduces LV afterload as well as preload (Marrow keyed this as the false statement)."),
         ("“NIV lowers afterload by lowering alveolar pressure or blocking RAAS”", "It works by raising intrathoracic pressure and lowering LV transmural pressure."),
         ("“Hypertensive pulmonary oedema — loop diuretic and wait, or intubate now”", "Nitrates plus NIV first (65%); diuretics are slow and the patient is redistributed, not overloaded; intubate if NIV fails or consciousness falls."),
         ("“Only etomidate caused the adrenal crisis”", "Etomidate, ketoconazole and phenytoin all contribute — ‘all of the above’ (44%).")],
  decode=[("ACPE: how does NPPV reduce LV afterload? [DocT GT]", "Raises intrathoracic pressure, reducing LV transmural pressure in systole."),
          ("SBP 180, pink frothy sputum, SpO₂ 88%, alert [DocT GT]", "Nitrates + NIPPV (65%)."),
          ("Haemodynamic effects of PEEP [NEET 2024]", "RV preload down, RV afterload up, LV afterload down."),
          ("Phenytoin, ketoconazole, etomidate; refractory shock responding to hydrocortisone [DocT GT]", "All of the above (44%).")],
  punch="Positive pressure lowers LV afterload and preload, so in the failing left heart it is a treatment, not just a ventilation mode.",
)

L['CS-28'] = dict(
  sub="Cardiogenic shock → Drugs → Offloading therapies",
  step=5,
  intro="Step 5’s unloading drugs. In the warm, wet, hypertensive patient the fastest relief comes from reducing load, not from removing fluid. Five real questions, all on hypertensive acute pulmonary oedema (SCAPE).",
  parts=[
    ('a', "**Loop diuretics: less circulating volume, mild venodilation, lower LVEDP and RVEDP.** The venodilation comes within minutes (before the diuresis); the volume effect takes hours."),
    ('b', "**NIV: better oxygenation, less work of breathing, less LV wall stress.** Less wall stress is the afterload effect of CS-27."),
    ('c', "**Vasodilators (nitroglycerin): veno-arterial dilatation, lower preload and LVEDP, lower afterload.** Venodilation dominates at low doses; high doses (as used in SCAPE) add arterial dilation. In sympathetic crashing acute pulmonary oedema (SBP often 180+), high-dose IV nitrates with NIV are first line, IV furosemide second; avoid nitrates if hypotensive, after phosphodiesterase-5 inhibitors and in RV infarction or severe AS. Morphine is no longer routine (more ventilation and deaths in registry data)."),
    ('d', "**Haemodialysis / haemodiafiltration / haemofiltration: lower volume and LVEDP/RVEDP, correction of electrolytes.**"),
  ],
  mimic=[("SCAPE vs volume-overloaded ADHF", "SCAPE: sudden, hypertensive, fluid redistributed — nitrates first; ADHF: days of weight gain, normal BP — diuretic first.")],
  traps=[("“Hypertensive pulmonary oedema — furosemide alone”", "Too slow and does not treat the afterload surge; nitroglycerin plus furosemide (NEET 2025)."),
         ("“Morphine for the distressed patient in pulmonary oedema”", "No longer routine; it is linked to more ventilation and mortality."),
         ("“Esmolol-triggered pulmonary oedema needs more beta-blockade”", "After esmolol for amphetamine SVT, pulmonary oedema needs nitrates and diuretics.")],
  decode=[("Acute HF with pulmonary oedema, BP 180/100 [NEET 2025]", "NTG + furosemide."),
          ("SCAPE after CABG: drug of choice [NEET 2024]", "Nitroglycerin."),
          ("Amphetamine, hypertensive SVT → esmolol → pulmonary oedema: next? [Marrow]", "Nitrates and diuretics."),
          ("Wet-warm, BP 130/85: first line [DocT QBank]", "IV furosemide (86%).")],
  punch="When the pressure is high and the lungs are wet, nitroglycerin and NIV unload the ventricle in minutes; the diuretic follows.",
)

L['CS-29'] = dict(
  sub="Cardiogenic shock → Drugs → Inotropes: receptors and net effect",
  step=5,
  intro="Step 5’s inotropes, the most-asked card in the deck (15 questions). Every inotrope raises contractility by raising calcium availability or sensitivity, and every one in this table also vasodilates — which is why blood pressure falls and norepinephrine is so often added.",
  parts=[
    ('a', "**Dobutamine: β1 (more contractility and heart rate) and β2 (arteriolar dilation); net effect ‘inodilation’.** β1 → Gs → adenylate cyclase → cAMP → protein kinase A, which phosphorylates L-type calcium channels and ryanodine receptors (more systolic calcium: inotropy), phospholamban (releases SERCA2a: faster reuptake, lusitropy) and troponin I. Tachycardia is a dose-related direct β1 effect, not a reflex. Because β2 vasodilates, dobutamine can lower the pressure: a patient still hypotensive on it needs norepinephrine, not less dobutamine."),
    ('b', "**Adrenaline: β1 (contractility and rate), α1 at higher doses (vasoconstriction), more lactate production.** The lactate is β2-driven aerobic glycolysis, not hypoperfusion, so it can mislead. In infarct shock adrenaline caused more refractory shock than norepinephrine (OptimaCC, 2018)."),
    ('c', "**PDE-3 inhibitors (milrinone): more myocardial cAMP and contractility, more vascular cAMP → vasodilation, especially pulmonary.** Acting below the receptor, milrinone works in a beta-blocked patient. It vasodilates more than dobutamine, so hypotension is its main effect, and it is renally excreted, so it accumulates in AKI or ESRD (reduce the rate, skip the load). DOREMI (2021) found no outcome difference from dobutamine."),
    ('d', "**Levosimendan (calcium sensitiser): more contractility, reduced calcium flux, vascular K⁺-channel activation → vasodilation and lower afterload.** It binds troponin C and increases its calcium sensitivity without raising intracellular calcium, so oxygen cost and arrhythmia are lower; opening ATP-sensitive potassium channels dilates vessels. An active metabolite keeps it working for days."),
  ],
  mimic=[("Milrinone vs levosimendan", "Milrinone: PDE-3 inhibition, more cAMP and calcium; levosimendan: troponin C sensitisation, no rise in calcium, K-ATP vasodilation."),
         ("Isoprenaline vs dobutamine", "Isoprenaline is a pure β1+β2 agonist: big rate rise and diastolic fall, so myocardial ischaemia limits it; it is a bridge to pacing in bradycardia.")],
  traps=[("“On dobutamine, HR 130 and still hypotensive — decrease dobutamine” (DocT key)", "Disputed: cutting dobutamine slows the heart but does not raise the pressure; add norepinephrine (33% chose the key). If the stem stresses the tachyarrhythmia with an adequate BP, reduce the dose (77% did, correctly)."),
         ("“Tachycardia on dobutamine is a reflex”", "It is dose-related direct β1 chronotropy, the ‘toxic effect’ (66%)."),
         ("“Serelaxin is an inotrope”", "It is a relaxin-2 vasodilator; omecamtiv mecarbil is the myosin activator that raises stroke volume without raising cAMP, calcium or oxygen use."),
         ("“Milrinone hypotension is toxicity or bradycardia”", "It is milrinone-induced vasodilation (88%).")],
  decode=[("Inotrope after failed dobutamine: cAMP up, venodilation, faster relaxation — mechanism? [DocT GT]", "PDE-3 inhibition (50%)."),
          ("On high-dose norepinephrine, still low output — which inotrope? [DocT GT ×2]", "Dobutamine (100%, 95%)."),
          ("Dobutamine: intracellular mechanism of better contraction and relaxation [DocT GT]", "Ryanodine receptor phosphorylation (via cAMP–PKA)."),
          ("Which comorbidity prolongs milrinone? [Marrow] / milrinone false statement [NEET 2024]", "End-stage renal disease; milrinone is a PDE-3 inhibitor that works downstream of the β receptor.")],
  punch="Every inotrope here also dilates vessels, so pressure falls: the answer to hypotension on an inotrope is norepinephrine, not a smaller dose.",
)

L['CS-30'] = dict(
  sub="Cardiogenic shock → Drugs → Inotrope algorithm",
  step=5,
  intro="Step 5’s decision tree. Low output with a low pressure starts an inotrope; the first branch is whether the right ventricle or the pulmonary circulation is the problem. Ten real questions, and two DocT keys are out of date.",
  parts=[
    ('a', "**Entry: MAP <65 mmHg AND LVEF <40% or CI <1.8 L/min/m².** A low pressure with proof of a weak pump."),
    ('b', "**Branch: RV dysfunction and/or raised pulmonary resistance?**"),
    ('c', "**No: begin dobutamine; if MAP stays <65 add norepinephrine, then vasopressin.** Dobutamine is the standard β-agonist inotrope for LV failure; norepinephrine restores the pressure that its β2 effect lowers."),
    ('d', "**Yes: begin milrinone or levosimendan WITH norepinephrine; if MAP stays <65 add vasopressin.** Both lower pulmonary vascular resistance, which unloads the RV, but both dilate systemic vessels too, so norepinephrine starts with them. Vasopressin raises SVR without raising PVR (CS-31)."),
    ('e', "**If vasopressin fails: consider a mechanical support device.** Both arms converge there; SCAI D is the stage where MCS is considered."),
  ],
  mimic=[("Dobutamine vs milrinone first", "Dobutamine for LV failure; milrinone or levosimendan when the RV or PVR is the problem, or the patient is on a beta-blocker.")],
  traps=[("“BP 80/50 after fluids, which inotrope? — dopamine” (DocT key)", "Outdated: SOAP II showed more arrhythmias and higher mortality in the cardiogenic subgroup. Norepinephrine for the pressure, dobutamine or milrinone for output (38% chose the keyed dopamine). Pick dopamine only if it is the sole vasoactive option."),
         ("“Still hypotensive on dobutamine — decrease dobutamine” (DocT key)", "Add norepinephrine (MAP <65 → norepinephrine, as this card says); 33% chose the key."),
         ("“Hypotension on dobutamine — switch to milrinone”", "Milrinone vasodilates more; the fix for pressure is norepinephrine (62% and 90%).")],
  decode=[("HFrEF, BP 85/55 on dobutamine, BP falling [DocT QBank]", "Add norepinephrine (90%)."),
          ("End-stage HF on low-dose dobutamine, BP 80/50 after fluids [DocT QBank]", "Add norepinephrine (62%)."),
          ("BP 80/50 despite fluids, which drug to improve output? [DocT QBank]", "DocT keys dopamine (38%); exam-day answer norepinephrine if offered."),
          ("Diltiazem overdose, low CI, normal SVR [Marrow]", "Dobutamine — choose by phenotype after calcium and high-dose insulin.")],
  punch="Dobutamine for the failing left ventricle, milrinone or levosimendan with norepinephrine when the right side is failing, norepinephrine whenever MAP stays under 65, and a device when drugs fail.",
)

L['CS-31'] = dict(
  sub="Cardiogenic shock → Subtypes → Shock states",
  step=5,
  intro="Step 5 by phenotype, from the AHA 2017 statement. Each Forrester profile (CS-18) gets its own vasoactive choice. Not asked directly, but CS-26 and CS-30 questions draw on it.",
  parts=[
    ('a', "**Classic wet and cold: norepinephrine first, then an inotrope once stable and after revascularisation; low CI, high SVR.** In SOAP II’s cardiogenic subgroup dopamine gave more arrhythmias and higher mortality, so it is not an equal choice."),
    ('b', "**Euvolaemic cold and dry: as above, plus small fluid boluses; LVEDP may be low.**"),
    ('c', "**Vasodilatory warm and wet or mixed: norepinephrine, haemodynamics-guided; this subtype has a LOW SVR.** Often post-arrest or infarct shock with a systemic inflammatory response; look for sepsis."),
    ('d', "**RV shock: fluid boluses; norepinephrine, dopamine or vasopressin; inotropes; inhaled pulmonary vasodilators — keep preload, lower PVR, treat bradycardia, keep AV synchrony; vasopressin raises SVR with neutral PVR.** The RV needs filling and a low afterload, and its coronary perfusion depends on systemic pressure, so a pressor that does not constrict the pulmonary bed is ideal."),
    ('e', "**Normotensive shock: inotrope or vasopressor; SBP >90 with a relatively high SVR, so initial inotropy may be appropriate.** This is ESC 2021’s hypoperfusion-without-hypotension (CS-05)."),
  ],
  mimic=[("RV shock vs LV shock", "RV: clear lungs, high CVP, needs fluid and a low PVR; LV: congestion, needs diuresis and afterload reduction.")],
  traps=[("“Diuretics and nitrates for RV infarction with hypotension”", "They drop preload in a preload-dependent ventricle; give fluid, then norepinephrine or vasopressin.")],
  decode=[("RV shock: which pressor does not raise PVR? [pattern]", "Vasopressin."),
          ("Hypoperfused but SBP 100 with high SVR [pattern]", "Normotensive cardiogenic shock — an inotrope may be first.")],
  punch="Match the drug to the phenotype: norepinephrine for the cold and hypotensive, an inotrope for the normotensive, fluid and a PVR-sparing pressor for the right ventricle.",
)

L['CS-32'] = dict(
  sub="Cardiogenic shock → Subtypes → Valvular lesions",
  step=6,
  intro="Step 6 starts with valves, where each lesion has its own haemodynamic rules and a definitive fix. Five real questions: low-flow aortic stenosis three times, acute AR and acute MR once each — and the AR question was answered correctly by only one in five.",
  parts=[
    ('a', "**Aortic stenosis: phenylephrine or vasopressin; if LVEF low, echo- or PAC-guided dobutamine; afterload-dependent; inotropy may not help if LVEF is preserved; definitive SAVR, balloon valvuloplasty, TAVR.** The fixed valve sets the outflow, so dilating vessels drops pressure without raising flow, and the hypertrophied ventricle depends on diastolic pressure for coronary perfusion. Symptomatic severe AS — including low-flow, low-gradient AS (valve area <1 cm² with a low gradient because the stroke volume is low) — needs urgent valve replacement, TAVI often preferred in the acutely ill elderly; balloon valvuloplasty is only a bridge (restenosis within months)."),
    ('b', "**Aortic regurgitation: dopamine, temporary pacing; a faster heart rate shortens diastole and lowers LVEDP; definitive SAVR.** Less diastolic time means less time to regurgitate. That is for the hypotensive patient. With pulmonary oedema and a normal pressure, nitroprusside is the bridge to surgery: it lowers afterload and the regurgitant volume. IABP is contraindicated (it augments diastolic pressure and the regurgitant jet), and β-blockers lengthen diastole."),
    ('c', "**Mitral stenosis: phenylephrine or vasopressin, esmolol or amiodarone; preload-dependent; avoid chronotropes, slow the rate to lengthen filling, keep AV synchrony; definitive MVR or balloon valvuloplasty.** Flow across a narrow mitral valve needs time; fast AF can cause sudden oedema and shock."),
    ('d', "**Mitral regurgitation: norepinephrine or dopamine, an inotrope, temporary MCS including IABP; afterload reduction lowers LVEDP; IABP reduces regurgitant fraction by lowering afterload and raising CI; definitive repair, replacement or edge-to-edge.** In an inferior STEMI, a new systolic murmur with flash pulmonary oedema and shock is posteromedial papillary muscle rupture (that muscle has a single blood supply); IABP is the bridge to surgery."),
  ],
  mimic=[("Acute AR vs acute MR", "Both need afterload reduction; IABP helps MR and is contraindicated in AR."),
         ("AR vs MS heart rate", "Raise it in AR to shorten diastole; slow it in MS to lengthen filling.")],
  traps=[("“Acute AR with pulmonary oedema, BP 120/70 — norepinephrine, adrenaline or furosemide”", "Raising afterload increases regurgitation; nitroprusside is the bridge (only 20% right)."),
         ("“Inferior STEMI, new systolic murmur, oedema, BP 90/50 — norepinephrine or milrinone”", "Norepinephrine raises afterload and the regurgitant fraction; milrinone drops the pressure; IABP unloads and perfuses (38% right)."),
         ("“Low-flow AS — balloon valvuloplasty, diuresis or fluids”", "Valvuloplasty is a bridge, diuresis or fluids leave the obstruction: urgent valve replacement (59–71%).")],
  decode=[("78-year-old, oedema, weak carotid upstroke, AVA 0.7 cm², low gradient [DocT GT ×3]", "Urgent aortic valve replacement (71%, 59%, 61%)."),
          ("IVDU, aortic vegetation, severe AR, pulmonary oedema, BP 120/70 [DocT GT]", "Nitroprusside (20%)."),
          ("Inferior STEMI, systolic murmur, pulmonary oedema, cold, BP 90/50 [DocT GT]", "Intra-aortic balloon pump (38%).")],
  punch="Stenoses need pressure and time (pressors, slow rates), regurgitation needs unloading (vasodilators, IABP in MR but never in AR), and every valve shock needs the valve fixed.",
)

L['CS-33'] = dict(
  sub="Cardiogenic shock → Subtypes → Mechanical and electrical",
  step=6,
  intro="Step 6, the lesions that make standard treatment harmful. LVOT obstruction is the one place where inotropes are contraindicated. One real question, on Takotsubo with outflow obstruction.",
  parts=[
    ('a', "**Post-infarct VSD: treat as classic wet and cold; temporary MCS including IABP, which lowers the shunt fraction by lowering afterload and raising CI; surgical repair or percutaneous umbrella closure.** Lower systemic resistance means more blood goes out of the aorta rather than across the septum."),
    ('b', "**Dynamic LVOT obstruction: fluid boluses, phenylephrine or vasopressin; AVOID inotropes and vasodilators; esmolol or amiodarone; RV pacing — raise preload and afterload, reduce inotropy and ectopy, keep AV synchrony.** A bigger, slower, less forceful ventricle with a higher aortic pressure keeps the mitral leaflet out of the outflow tract; inotropes and vasodilators make the cavity smaller and the gradient larger. Takotsubo with a hyperkinetic base is the classic ICU example."),
    ('c', "**Bradycardia: chronotropes (atropine, isoprenaline, dopamine, dobutamine, adrenaline), temporary pacing; treat the cause.** Look for inferior ischaemia, drugs (beta-blockers, calcium-channel blockers, digoxin) and hyperkalaemia."),
    ('d', "**Pericardial tamponade: fluid bolus, norepinephrine; pericardiocentesis or a surgical window is the definitive treatment.** Fluid and pressor only buy time; avoid positive pressure ventilation if possible, because it further limits filling."),
  ],
  mimic=[("LVOT obstruction vs LV pump failure", "Both are cold and hypotensive; LVOTO has a small hyperdynamic LV, systolic anterior motion and a high outflow gradient, and gets worse with dobutamine.")],
  traps=[("“Takotsubo with hypotension — dobutamine or norepinephrine”", "With LVOT obstruction, phenylephrine (pure α) raises afterload without inotropy; dobutamine worsens the gradient.")],
  decode=[("Takotsubo after near-drowning, hypotension with LVOTO: best vasopressor [Marrow]", "Phenylephrine.")],
  punch="LVOT obstruction is the exception: fill it, constrict it with phenylephrine, slow it — and never give an inotrope.",
)

L['CS-34'] = dict(
  sub="Cardiogenic shock → Revascularisation → Stabilisation, anatomy, culprit vessel",
  step=6,
  intro="Step 6’s decisive treatment in infarct shock: open the culprit artery. Two real questions, both asking what changes survival, and the device distractors pulled two thirds of the cohort away.",
  parts=[
    ('a', "**Stabilisation and resuscitation: IV fluids, oxygenation and ventilation, reperfusion and revascularisation, fibrinolysis vs PCI, PCI strategy, antithrombotic drugs, CABG.** Fibrinolysis is for when primary PCI cannot happen in time; it works less well in shock because low pressure limits drug delivery to the clot."),
    ('b', "**15% have left main lesions; more than 50% have triple-vessel disease.** Shock usually means extensive coronary disease, so non-culprit vessels can no longer compensate."),
    ('c', "**Culprit-vessel mortality: left main 78.6%, saphenous vein graft 69.7%, circumflex 42.4%, LAD 42.3%, RCA 37.4%.** Left main occlusion threatens most of the LV; the RCA usually supplies less LV muscle. Circumflex and LAD are effectively equal."),
    ('d', "**Default primary PCI; rarely, depending on resources, CABG ± PCI or emergent transplantation.** ESC 2023 gives immediate angiography and culprit PCI a class I recommendation, with emergency CABG if the anatomy is not suitable. Routine IABP is class III (ESC 2023, ACC/AHA 2025); the 2025 ACC/AHA guideline gives a microaxial pump (Impella) class 2a in selected STEMI shock after DanGer Shock (180-day death 45.8% vs 58.5%, at the cost of more bleeding, limb ischaemia and RRT), and routine VA-ECMO class 3 after ECLS-SHOCK (30-day death 47.8% vs 49.0%, more bleeding)."),
  ],
  mimic=[("Revascularisation vs device support", "Revascularisation treats the cause and saves lives (SHOCK); devices support the circulation while the cause is fixed.")],
  traps=[("“Severe biventricular failure, EF 12%, VT — insert an LVAD or IABP first”", "IABP and LV devices support one ventricle and fix nothing; with a large troponin rise and a likely ischaemic cause, urgent angiography comes first (37% right)."),
         ("“High-dose dopamine, adrenaline or IABP improves survival in STEMI shock”", "Only early reperfusion has proven survival benefit.")],
  decode=[("Intubated, pressors, troponin 2.5, recurrent VT, EF 12% biventricular [DocT GT]", "Urgent coronary angiography with intent to revascularise (37%)."),
          ("Large anterior STEMI, BP 72/40, rising lactate: what most improves survival? [DocT GT]", "Early coronary reperfusion.")],
  punch="In infarct shock, opening the culprit artery is the treatment that saves lives; drugs and devices only keep the patient alive until it is done.",
)

L['CS-35'] = dict(
  sub="Cardiogenic shock → Trials → SHOCK",
  step=6,
  intro="Step 6’s founding trial. SHOCK (1999) is why infarct shock goes to the cath lab, even though its primary end point was negative. Not asked directly here, but CS-34 questions rest on it.",
  parts=[
    ('a', "**Strong evidence for early revascularisation (PCI) in cardiogenic shock.** Early revascularisation meant PCI or CABG; well over a third of those revascularised had CABG, with similar survival."),
    ('b', "**n = 302, MI complicated by cardiogenic shock, randomised.** Shock within 36 h of MI, randomised within 12 h of its onset; mostly STEMI with LV failure."),
    ('c', "**Overall 30-day mortality was SIMILAR.** 46.7% vs 56.0% (p 0.11): a 9-point difference the trial was not large enough to prove; in patients under 75 it was significant (41.4% vs 56.8%)."),
    ('d', "**Revascularisation 50.3% vs medical therapy 63.1%.** These are the 6-month figures (p 0.027); at 1 year about 53% vs 66%."),
    ('e', "**The 6-month and 1-year differences WERE significant.** The benefit persisted at 6 years: about 13 lives saved per 100 treated."),
    ('f', "**Successful vs unsuccessful PCI: 35% vs 80% mortality.** The SHOCK PCI analysis (Webb 2003) gives one-year mortality of 39% if PCI succeeded vs 85% if it failed; by final flow, 38% with TIMI 3, 55% with TIMI 2 and 100% with TIMI 0–1. Either way, an open artery is what decides survival."),
  ],
  mimic=[("SHOCK vs CULPRIT-SHOCK", "SHOCK: revascularise early (vs medical stabilisation); CULPRIT-SHOCK: revascularise the culprit only (vs all lesions).")],
  traps=[("“SHOCK was negative, so early revascularisation is unproven”", "The 30-day result missed significance, but 6-month and later survival was clearly better; it is a positive trial in practice.")],
  decode=[("SHOCK trial: primary end point result [pattern]", "No significant 30-day difference; significant benefit at 6 and 12 months.")],
  punch="SHOCK missed its 30-day end point but showed a lasting survival gain from early revascularisation, and success depends on actually opening the artery.",
)

L['CS-36'] = dict(
  sub="Cardiogenic shock → Trials → CULPRIT-SHOCK",
  step=6,
  intro="Step 6’s second question once the patient is on the table: open only the culprit or every lesion? CULPRIT-SHOCK (2017) answered it for shock. Not asked directly.",
  parts=[
    ('a', "**n = 706; STEMI or NSTEMI with shock and an identifiable culprit lesion.** All had multivessel disease."),
    ('b', "**Primary end point: death or renal failure needing dialysis at 30 days.**"),
    ('c', "**9.5% absolute risk reduction.** 45.9% culprit-only vs 55.4% immediate multivessel PCI (NNT 11), driven mainly by death. At 1 year the mortality gap (50.0% vs 56.9%) was no longer statistically significant, and the culprit-only group had more repeat revascularisation and heart-failure readmission."),
    ('d', "**It contradicted widespread practice.** Guidelines had allowed multivessel PCI in shock; ESC now recommends culprit-only PCI at the index procedure in shock, with staged PCI of other lesions considered (IIa). Extra contrast, longer procedures and more ischaemia from multiple interventions in a failing heart are the likely reasons."),
    ('e', "**Complete revascularisation benefit comes from NON-shock patients: DANAMI-3-PRIMULTI, PRAMI, CvLPRIT** (and later COMPLETE)."),
  ],
  mimic=[("Shock vs stable STEMI", "In shock, culprit only (CULPRIT-SHOCK); in haemodynamically stable STEMI, complete revascularisation (PRAMI, CvLPRIT, DANAMI-3-PRIMULTI, COMPLETE).")],
  traps=[("“Complete revascularisation at the index PCI is preferred in shock”", "Not in shock: culprit-only reduced 30-day death or dialysis by 9.5%.")],
  decode=[("AMI shock with multivessel disease: PCI strategy [pattern]", "Culprit lesion only, staged later if needed.")],
  punch="In cardiogenic shock open the culprit artery only; complete revascularisation belongs to stable patients.",
)

FLAGS = {
  'CS-01': "a/c: ‘de novo HF one third’ and the AMI-dominant ordering reflect older series. The 2024 SHARC-definition CCCTN registry found AMI-CS 27% and HF-CS 59% (de novo 28% of HF-CS). The explanation gives both.",
  'CS-05': "a: ‘SBP <90 with adequate volume’ is the ESC 2016 definition. ESC 2021 HF (and the 2020 HFA statement) defines cardiogenic shock by hypoperfusion from primary cardiac dysfunction and no longer requires hypotension (normotensive shock). Same applies to the ESC column of CS-07.",
  'CS-06': "Card correct. The linked card-layer line attributes ‘CI <2.2 on support (<1.8 without)’ to the SHOCK trial; the trial used CI ≤2.2 and PCWP ≥15, and the 1.8/2.2 split is the broader textbook definition.",
  'CS-08': "f: ‘Arrest modifier = CPR, including defibrillation’ is the 2019 wording; the 2022 SCAI update narrows the cardiac arrest modifier to arrest with coma (unresponsive to verbal stimuli) and adds the three-axis model.",
  'CS-14': "a: ‘AMI accounts for 80%’ is the older figure (reviews quote 60–80%); contemporary cardiac ICU registries show AMI-CS about 27% (2024). Kept as the likely exam answer, explained in the text.",
  'CS-26': "Card follows the ESC 2016 profile algorithm (wet-cold SBP <90 → inotrope first); ESC 2021 organises acute HF by four presentations and AHA/SCAI/ACC-AHA 2025 start norepinephrine first in hypotensive shock (Crossfire). DocT keys dopamine for post-diuresis hypotension — outdated (SOAP II). The 95%/5% split is the ESC 2016 flowchart’s congestion-present vs absent figure (verified); real-world registry data give about 90% wet at admission.",
  'CS-29': "d: ‘reduced calcium flux’ for levosimendan is loose; it sensitises troponin C without increasing intracellular calcium (no rise in calcium flux). DocT keys ‘decrease dobutamine’ for persistent hypotension on dobutamine — disputed; the card (with CS-30) is right to add norepinephrine.",
  'CS-30': "Card correct. Two DocT keys disagree: dopamine for BP 80/50 low output (outdated, SOAP II) and ‘decrease dobutamine’ for persistent hypotension on dobutamine (the card’s MAP <65 → norepinephrine is right).",
  'CS-35': "d: 50.3% vs 63.1% are the 6-month figures (30-day was 46.7% vs 56.0%). f: ‘35% vs 80%’ could not be traced; the SHOCK PCI analysis (Webb 2003) reports one-year mortality 39% vs 85% for successful vs unsuccessful PCI.",
}
