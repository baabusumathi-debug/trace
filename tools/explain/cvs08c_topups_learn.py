# CVS08C top-up cards — Explain v3 ("Learn" depth), same fields and voice as cvs08c_learn.py.
# Fields: sub, step (index into cvs08c_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from each top-up's own src (DocT QBank and Grand Tests); the stems themselves are not in qpack/CVS08C.md, so decode items are labelled [pattern].
# Checked online on 19 Nov 2026: AHA 2025 Part 9 (POCUS to find reversible causes, 2b); AHA 2025 Part 10 (drowning: CPR with breaths and compressions, class 1; anaphylaxis in arrest: standard IM
# dose effectiveness uncertain, 2b; isotonic fluids, 2a; ECPR, 2a; hypothermic arrest: full resuscitation with concurrent rewarming, ECLS).
# From standard references without a fresh check: ERC drowning (5 initial rescue breaths); Resuscitation Council UK 2021 anaphylaxis (IM 0.5 mg anterolateral thigh, repeat after 5 min, low-dose
# IV infusion if no improvement after two IM doses; tryptase timing); Simons 2001 (thigh IM faster, higher peak than deltoid or SC); the 20% + 2 ng/mL tryptase rule (Valent 2012);
# NAP6 (perioperative anaphylaxis, skin testing at about 4–6 weeks). Reviewer check 19 Nov 2026: RCUK/ERC 2025 special circumstances (drowning: 5 ventilations with 100% O2, then standard CPR; anaphylaxis IM 500 µg, repeat at 5 min);
# AHA 2025 Part 10 gives no submersion-time threshold; the ‘<60 min’ card figure does not match the Tipton & Golden 2011 guide (30 min >6 °C water, 90 min ≤6 °C) — FLAGGED.
T = {}

T['T_db9d2577'] = dict(
  sub="Cardiology → ACLS → Echo at the CPR pulse check",
  step=1,
  intro="Step 1 is about feedback during CPR, and a few seconds of echo at the pulse check is the most direct feedback there is: it shows whether the heart is moving and whether a reversible cause is visible. Four Grand Test questions ask what each picture means and how true PEA differs from pseudo-PEA.",
  parts=[
    ('a', "**Effusion with RV diastolic collapse = tamponade → pericardiocentesis during CPR.** The RV is the thinnest, lowest-pressure chamber, so it collapses first when pericardial pressure rises; it cannot fill, so nothing reaches the LV. Draining even a small volume restores filling, which is why it is done without stopping CPR."),
    ('b', "**Dilated RV with a D-shaped LV = massive PE → lysis; small hyperdynamic ‘kissing’ ventricles = hypovolaemia → volume or blood.** In PE the pressure-loaded RV dilates and pushes the septum into the LV, flattening it into a D. In hypovolaemia the chambers are underfilled and the walls touch in systole. Note that the RV also dilates in any arrest of a few minutes, as blood pools on the venous side, so RV dilatation alone is not proof of PE."),
    ('c', "**No cardiac motion = true PEA (CPR + adrenaline; poor prognosis); coordinated motion without a pulse = pseudo-PEA, profound shock where fluids or vasopressor may restore a pulse, better survival.** In pseudo-PEA the heart is ejecting, but too little to feel; it behaves like severe shock, so treating its cause (volume, vasopressor, tamponade, PE) can restore a pulse. True cardiac standstill carries a very low chance of ROSC."),
    ('d', "**AHA 2025: POCUS may be used by experienced operators to find a reversible cause only if it does not lengthen pauses (subxiphoid or TEE views, under 10 s); not routine, not a replacement for pulse checks and not a sole reason to stop. CTPA, MRI or CXR mean leaving the resuscitation.** Studies found that echo lengthened pauses, often beyond 10 seconds, and that what is seen as ‘standstill’ varies between observers; hence the weak 2b. TEE avoids interrupting compressions altogether."),
  ],
  mimic=[
    ("True PEA vs pseudo-PEA", "No motion: standard ALS, poor prognosis. Motion without pulse: treat as profound shock."),
    ("PE vs prolonged arrest on echo", "Both dilate the RV; a clot in transit, a D-shaped LV before arrest or a DVT supports PE."),
  ],
  traps=[
    ("“Send the patient for CTPA during CPR to confirm PE”", "Imaging outside the room means leaving the resuscitation; decide on the bedside echo and the clinical picture."),
    ("“No cardiac motion on echo — stop resuscitation”", "Echo is not a sole reason to stop."),
  ],
  decode=[
    ("PEA, effusion with RV diastolic collapse on subxiphoid view [pattern]", "Tamponade: pericardiocentesis during CPR."),
    ("PEA, coordinated cardiac motion, no palpable pulse [pattern]", "Pseudo-PEA: treat as profound shock; better prognosis."),
  ],
  punch="Echo at the pulse check asks two questions in under 10 seconds: is the heart moving, and is there a fixable cause (fluid, a dilated RV, empty ventricles)? It informs, but never alone ends, the resuscitation.",
)

T['T_cbaf1745'] = dict(
  sub="Cardiology → ACLS → Drowning",
  step=4,
  intro="Step 4 includes the arrest caused by water. In drowning the heart stops because of hypoxia, not a primary arrhythmia, so the order of resuscitation changes: oxygen comes first. Two questions test this and why a patient who looks well must be watched.",
  parts=[
    ('a', "**The insult is hypoxia: 5 rescue breaths, then CPR (ERC); no Heimlich; fresh vs salt water does not change management.** The heart arrests after the oxygen runs out, so breaths treat the cause; AHA 2025 also requires CPR with breaths, not compression-only, from trained rescuers (class 1). Abdominal thrusts delay ventilation and cause vomiting; little water is aspirated. The old idea that fresh water causes haemolysis and salt water pulmonary oedema did not hold in humans at the volumes aspirated."),
    ('b', "**Post-hypoxic cerebral oedema builds over hours and peaks at 24–72 h, so an alert patient can deteriorate later.**"),
    ('c', "**Observe at least 6–8 h; ARDS can also appear late.** Aspirated water washes out surfactant and inflames the alveoli, so hypoxaemia can emerge hours after rescue."),
    ('d', "**Pulseless after long submersion: start CPR if submerged under 60 min (cold water protects the brain); hypothermic → continue CPR with active rewarming (ECLS if available).** Rapid cooling lowers cerebral oxygen demand before the brain becomes hypoxic, which is why children recovered from icy water have survived intact after long submersion. The 60-minute figure is the card’s; the published decision guide (Tipton and Golden 2011, used by UK rescue services) depends on water temperature: in water above 6 °C resuscitate if submerged under 30 minutes, in water at 6 °C or below under 90 minutes; beyond that survival is unlikely. In outcome studies short submersion (minutes) does well and submersion beyond about 25 minutes does poorly. The rewarming rules of hypothermia then apply (ACLS-55)."),
  ],
  mimic=[
    ("Drowning arrest vs cardiac arrest on land", "Drowning is hypoxic: breaths first. Sudden cardiac arrest on land is usually arrhythmic: compressions and shock first."),
  ],
  traps=[
    ("“Abdominal thrusts to clear water from the lungs”", "They delay ventilation and risk aspiration; start rescue breaths."),
    ("“Alert after rescue — discharge”", "Observe for 6–8 hours; lung injury and cerebral oedema can appear late."),
  ],
  decode=[
    ("Child pulled from a pool, not breathing — first step? [pattern]", "Five rescue breaths, then CPR."),
    ("Alert after near-drowning — disposition? [pattern]", "Observe at least 6–8 h for delayed lung injury."),
  ],
  punch="Drowning stops the heart through hypoxia, so give breaths first, ignore the type of water, watch the ‘well’ patient for hours, and do not stop a cold patient’s CPR until he is warm.",
)

T['T_60914e52'] = dict(
  sub="Cardiology → ACLS → Confirming anaphylaxis with tryptase",
  step=4,
  intro="Step 4 includes anaphylaxis, and after the event comes the question of proof. Tryptase is stored in mast cell granules and released when they degranulate, so a rise above the patient’s own baseline confirms that mast cells fired. One Grand Test question asks how and when to measure it.",
  parts=[
    ('a', "**Serum mast-cell tryptase 15 min–3 h after onset (peak 1–2 h), plus a baseline more than 24 h later.** Tryptase peaks at about 1–2 hours and has a half-life of about 2 hours, so a late sample misses the rise. The baseline later is the patient’s own reference, because some people (mastocytosis) run high values."),
    ('b', "**A rise above 1.2 × baseline + 2 ng/mL confirms mast-cell activation; a normal value does not exclude anaphylaxis (asthma does not raise it).** Basophil-driven or some food reactions release little tryptase. Acute asthma does not degranulate mast cells systemically, which is why tryptase separates anaphylactic bronchospasm from an asthma attack."),
    ('c', "**Refer for skin testing at 4–6 weeks (NMBAs, cefazolin, chlorhexidine, latex).** Mast cells need weeks to restock after degranulation, so earlier testing gives false negatives. In the UK audit (NAP6) antibiotics were the commonest perioperative cause, followed by neuromuscular blockers, chlorhexidine and patent blue dye."),
  ],
  mimic=[
    ("Tryptase vs histamine", "Histamine peaks and clears within minutes, so it is impractical; tryptase stays up for hours."),
  ],
  traps=[
    ("“A normal tryptase rules out anaphylaxis”", "It confirms when raised but does not exclude when normal."),
    ("“Skin test the next day”", "Wait 4–6 weeks for mast cells to recover."),
  ],
  decode=[
    ("Hypotension and bronchospasm after induction — investigation to confirm anaphylaxis? [pattern]", "Serum tryptase at 1–2 h, with a baseline after 24 h."),
  ],
  punch="Tryptase proves that mast cells fired: take it at 1–2 hours, compare it with the patient’s own baseline (1.2 × baseline + 2), and refer for skin tests after 4–6 weeks.",
)

T['T_238aeb8c'] = dict(
  sub="Cardiology → ACLS → Anaphylaxis: first-line adrenaline",
  step=4,
  intro="Step 4 ends with the first drug for anaphylaxis. Adrenaline treats every limb of the reaction: α vasoconstriction reverses vasodilatation and leak, β1 supports the heart, and β2 opens the bronchi and stabilises mast cells. The question asks the dose, route and site; it also shares a number with the arrest dose (ACLS-45).",
  parts=[
    ('a', "**IM adrenaline 0.5 mg (0.5 mL of 1 mg/mL; child 0.01 mg/kg) into the anterolateral thigh (vastus lateralis): faster, higher peak than deltoid or SC; repeat every 5 min.** Thigh muscle is well perfused, so absorption is quick; subcutaneous fat is poorly perfused and adrenaline constricts its own vessels there. The IM route is safe without monitoring; IV boluses are for anaesthetists and intensivists with monitoring, in 50 µg steps, because a 1 mg IV bolus in a patient with a pulse can cause VT or a hypertensive crisis."),
    ('b', "**Refractory after 2 IM doses → IV adrenaline infusion; on β-blockers add glucagon.** Two failed IM doses mark refractory anaphylaxis, which needs a titrated infusion and fluids for the leak. β-blockade blunts adrenaline’s cardiac and bronchial effects; glucagon raises cyclic AMP through its own receptor, bypassing the β receptor. If the patient arrests, standard ALS with 1 mg IV every 3–5 min replaces the IM dose (AHA 2025)."),
    ('c', "**Antihistamine and steroid are adjuncts that never replace adrenaline; confirm with tryptase at 1–2 h.** Antihistamines treat skin features only; steroids work over hours and have not been shown to prevent a biphasic reaction."),
  ],
  mimic=[
    ("0.5 mg IM of 1:1000 vs 1 mg IV of 1:10,000", "Anaphylaxis with a pulse vs cardiac arrest."),
  ],
  traps=[
    ("“Subcutaneous or deltoid adrenaline”", "The anterolateral thigh gives the fastest, highest peak."),
    ("“Hydrocortisone and chlorphenamine first, adrenaline if they fail”", "Adrenaline is first; the others are adjuncts."),
  ],
  decode=[
    ("Anaphylaxis — first drug, dose and site? [pattern]", "IM adrenaline 0.5 mg (1:1000) into the anterolateral thigh."),
  ],
  punch="Anaphylaxis gets 0.5 mg of 1:1000 adrenaline into the thigh muscle, repeated at 5 minutes; after two doses start an infusion, and only in arrest switch to the 1 mg IV arrest dose.",
)

FLAGS = {
  'T_cbaf1745': "d: ‘start CPR if submerged <60 min’ is not a guideline figure. The submersion decision guide (Tipton & Golden 2011) uses water temperature: resuscitate if under 30 min in water >6 °C, under 90 min in water ≤6 °C; AHA 2025 and ERC 2025 give no single cut-off. The explanation gives the real thresholds.",
}
