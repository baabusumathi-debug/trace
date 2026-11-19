# CVS08E — Explain v3 ("Learn" depth): BLS & ACLS V — the lay-rescuer sequence, AED use and the pauses around a shock, compression quality, AED special situations,
# newborn resuscitation (initial steps, heart-rate thresholds, ventilation corrective steps, compressions, adrenaline), VA vs VV ECMO, ECPR, VV-to-VA reconfiguration,
# peripheral VA-ECMO complications and the IABP / Impella / VA-ECMO ladder.
# No mnemonics or hooks. Driven by qpack/CVS08E.md (9 question links, all DocT GT; ACLS-84 VA-ECMO complications asked 3 times, ACLS-81 VA vs VV twice, ACLS-71, -73, -82 and -85 once each).
# ACLS-72, -74, -75, -76, -77, -78, -79, -80 and -83 have no linked question and get short explanations with [pattern] decode items.
# No Top-up cards for CVS08E in cvs_topups.json. cvs_cardlayer.json lines (ACLS-71 drowning, ACLS-81 arrest on VV ECMO, ACLS-82 Surugadai criteria) and the ACLS-85 cross note
# (Impella keyed, but TandemHeart and VA-ECMO are equally rhythm-independent) were read and used. No `fix` entries for CVS08E in trace/test/data/qbank.json (checked 19 Nov 2026).
# Checked online on 19 Nov 2026:
#  - AHA 2025 Part 7, Adult BLS (cpr.heart.org): lay rescuer assumes arrest in an unresponsive person not breathing normally, no pulse check (1); HCP pulse check no more than 10 s (1);
#    agonal breathing ‘present in up to 40% to 60% of OHCA’; lone responder activates EMS first then begins CPR (1), with a mobile phone activate and begin CPR at once (1), speakerphone;
#    compression-only appropriate for untrained or unwilling lay rescuers, breaths reasonable for trained rescuers (2a); rate 100–120 (2a); depth at least 5 cm (1), over 6 cm linked to lower
#    survival; full recoil (2a), leaning lowers coronary perfusion; compression fraction at least 60% (2b); pre- and post-shock pauses as short as possible (1); resume compressions immediately
#    after the shock rather than a post-shock rhythm check (2a); 30:2 before an advanced airway (2a); pads anterolateral or anteroposterior (2a).
#  - AHA 2025 Part 9, Adult ALS: single shock preferred to stacked shocks (2a, shorter CPR interruptions); DSD and vector change not established (2b).
#  - AHA 2025 ECPR (as quoted in SOCCA review, Dec 2025): reasonable ‘in select patients when provided within an appropriately trained and equipped system of care’ (2a, B-R); no specific
#    inclusion/exclusion criteria set; commonly used criteria shockable rhythm, arrest-to-CPR under 5 min, arrest-to-flow under 60 min, age under 70, no severe comorbidity.
#  - AHA 2025 Part 6, Paediatric BLS: single rescuer 30:2, two rescuers 15:2; children under 8 — paediatric attenuator recommended, an AED without one may be considered if nothing else;
#    conventional CPR with breaths preferred in children, compression-only if the rescuer cannot or will not give breaths.
#  - AHA 2025 Part 5, Neonatal resuscitation (cpr.heart.org): ventilation within 60 s of birth if gasping or apnoeic (1); PPV if heart rate below 100 despite initial steps (1); compressions if
#    heart rate below 60 despite 30 s of ventilation (1); 3:1 (2b); two-thumb encircling (2b); 100% oxygen during compressions (2b); ECG for heart rate during compressions (1); adrenaline if
#    heart rate not above 60 after optimised ventilation and compressions (1), intravascular 0.01–0.03 mg/kg (1), tracheal 0.05–0.1 mg/kg while access is obtained (2a), repeat every 3–5 min (2b);
#    volume if blood loss known or suspected and no response to adrenaline; routine oral, nasal or tracheal suctioning not recommended (3: No Benefit), intubation and suction if the trachea is
#    obstructed (2a); deferred cord clamping at least 60 s.
#  - Prague OHCA (Belohlavek, JAMA 2022; Bottom Line summary): 264 randomised (124 vs 132 analysed), age 18–65, witnessed presumed cardiac OHCA, no ROSC after 5 min of ALS; CPC 1–2 at 180 days
#    31.5% vs 22.0% (p 0.09, NS); 30-day CPC 1–2 30.6 vs 18.2% (secondary); median time to ECLS about 61 min; stopped for futility.
#  - INCEPTION (Suverein, NEJM 2023; JournalFeed): age 18–70, bystander CPR, initial ventricular arrhythmia, no ROSC by 15 min; 30-day survival with favourable neurology 20% vs 16% (NS);
#    randomised during transport, control survival double the estimate, underpowered.
#  - ACC Year in Review 2025 (Aug 2026): 2025 ACC/AHA ACS guideline — microaxial flow pump upgraded to 2a in selected AMI-CS; routine IABP 3: No Benefit; VA-ECMO downgraded after ECLS-SHOCK;
#    DanGer Shock long-term mortality 52.5 vs 68.8% (HR 0.7).
# From standard references without a fresh check (confident unless said): ARREST (Yannopoulos, Lancet 2020; n 30, refractory VF; survival to discharge 43% vs 7%, stopped early for benefit);
# INCEPTION n 134, 10 centres; ELSO 2021 interim ECPR guideline (Richardson) selection criteria and exclusions (unwitnessed, prolonged low-flow, terminal illness, severe aortic regurgitation,
# aortic dissection, contraindication to anticoagulation); Surugadai criteria as given in the DocT line; DanGer Shock (Møller, NEJM 2024; n 360, 180-day death 45.8 vs 58.5%, HR 0.74; more
# bleeding, limb ischaemia and RRT); ECLS-SHOCK (Thiele, NEJM 2023; n 420, 30-day death 47.8 vs 49.0%, more bleeding and vascular complications); IABP-SHOCK II (39.7 vs 41.3% at 30 days);
# device flows (IABP about 0.5–1 L/min; Impella 2.5, CP about 3.5–4, 5.0/5.5 up to 5–6 L/min); ERC 2021/2025 pad at least 8 cm from an implanted device, 5 initial rescue breaths in drowning,
# pre-shock pause under 5 s; Cheskes 2011 (pre-shock pause over 20 s and perishock pause over 40 s linked to lower survival; less sure of the exact cut-offs); repeated shocks lower transthoracic
# impedance by about 8% or less; NRP heart-rate reassessment after 60 s of compressions; MR SOPA.
# Second check (independent reviewer, 19 Nov 2026): ARREST 30 randomised (15 vs 15), discharge survival 43% vs 7%, stopped early for benefit (ACC trial summary); INCEPTION 160 randomised,
# 134 in the analysis (70 vs 64), 10 centres, CPC 1–2 at 30 days 14/70 (20%) vs 10/62 (16%), OR 1.4, p 0.52 (The Bottom Line); Cheskes, Circulation 2011 (815 shockable OHCA, ROC Epistry):
# pre-shock pause ≥20 s vs <10 s OR 0.47, perishock ≥40 s vs <20 s OR 0.54, each 5 s of pre-shock pause about 18% lower survival, post-shock pause not independently associated (PubMed abstract);
# ELSO 2021 interim ECPR criteria as cited in a 2025 JECT review: age under 70, witnessed, shockable rhythm, no-flow under 5 min, low-flow under 60 min, consensus-based. Not re-verified
# online (search limit reached): the Surugadai protocol itself (taken from the DocT line), AHA 2025 agonal-breathing share and paediatric call-first wording (taken from the writer’s check),
# ERC 2025 8 cm pad distance (ERC 2021 wording), device flows (standard figures).

SPINE = [
  ("Recognise, call, compress", "An unresponsive adult who is not breathing normally is in arrest until proved otherwise, so call, send for the AED and start hard, fast compressions with as few pauses as possible."),
  ("Shock early, pause little", "The AED goes on while compressions continue; the only pauses allowed are analysis and one shock, because coronary perfusion pressure collapses within seconds and the next shock depends on it."),
  ("The newborn needs ventilation first", "Neonatal arrest is asphyxial, so warming, opening the airway and effective positive-pressure ventilation fix most babies; compressions and adrenaline follow only when proven ventilation fails."),
  ("Lung or heart: VV or VA", "VV ECMO only oxygenates and needs the patient’s own heart to deliver the blood; VA ECMO also replaces the pump, so shock or arrest decides VA."),
  ("ECPR buys time for a fix", "VA ECMO during refractory arrest works only in a selected patient, cannulated within about an hour, with a reversible cause that can be treated straight away."),
  ("Retrograde flow and the device ladder", "Peripheral VA ECMO pumps blood backwards up the aorta, which explains Harlequin hypoxaemia, LV distension and leg ischaemia, and why an LV-unloading Impella is sometimes added."),
]

PRIMER = "During CPR the heart is perfused only between compressions, by the gap between aortic diastolic and right-atrial pressure; it takes many compressions to build that gap and seconds to lose it. A defibrillator works best on a heart that has just been perfused. A newborn, unlike an adult, rarely arrests from a rhythm problem: the lungs have to open at birth, and failure to breathe causes the bradycardia. ECMO drains venous blood, oxygenates it and returns it either to a vein (VV, lung support only) or to an artery (VA, lung and circulation)."

L = {}

L['ACLS-71'] = dict(
  sub="Cardiology → BLS → Lay-rescuer sequence in adult collapse",
  step=1,
  intro="Step 1 is the opening minute of an out-of-hospital arrest, where survival is decided by how fast compressions start. The card gives the adult sequence; the one real question tests the exception, a drowned child, where the arrest is hypoxic and breaths come first.",
  parts=[
    ('a', "**Check scene safety, then responsiveness: tap the shoulders and shout.** A rescuer who becomes a second casualty helps no one; the shake and shout separate the sleeping or intoxicated from the unresponsive."),
    ('b', "**If unresponsive: shout for help, call EMS on speakerphone, send someone for an AED.** AHA 2025 (class 1) tells a lone rescuer with a mobile phone to call and start CPR at once; on speaker the dispatcher can coach compressions while they are given. In an adult, a witnessed sudden collapse is usually VF, and survival falls with every minute without a shock, so the AED is fetched early."),
    ('c', "**Check breathing and pulse simultaneously, for no more than 10 seconds; a lay rescuer need not check a pulse at all.** The pulse check is for health care professionals (class 1, ≤10 s); even they miss or imagine pulses, so a long search wastes perfusion time. AHA 2025 tells the lay rescuer to assume arrest in anyone unresponsive and not breathing normally."),
    ('d', "**No normal breathing and no definite pulse within 10 seconds: begin compressions. Agonal gasping is not breathing.** Gasps come from the brainstem in the first minutes of arrest and fade with time; AHA 2025 quotes them in up to 40–60% of out-of-hospital arrests (the card’s ‘up to 40%’ is the lower figure). They are the commonest reason bystanders wait, which is why dispatchers are trained to treat ‘breathing strangely’ as arrest."),
  ],
  mimic=[
    ("Call first (adult, witnessed collapse) vs care first (child, drowning, asphyxia)", "The adult is probably in VF and needs the defibrillator; the hypoxic arrest needs oxygen, so a lone rescuer without a phone gives about 2 minutes of CPR with breaths before leaving to call (AHA; ERC says 1 minute). With a phone, call on speaker and start at once. A child’s witnessed sudden collapse is the exception: it is likely arrhythmic, so call and fetch the AED first."),
  ],
  traps=[
    ("“Abdominal thrusts to drain water from the drowned child’s lungs”", "Little water is aspirated, and thrusts delay ventilation and cause regurgitation. Start CPR with rescue breaths (ERC: 5 initial breaths, then 30:2)."),
    ("“High-flow oxygen and watch for spontaneous breathing”", "An unresponsive child with no breathing is in arrest; oxygen by mask moves no air into apnoeic lungs. Ventilate and compress."),
    ("“Gasping means the patient is breathing, so wait”", "Agonal gasps are a sign of arrest, not of adequate breathing."),
  ],
  decode=[
    ("A 5-year-old pulled from a pool, unresponsive, not breathing — best initial management? [DocT GT]", "CPR with a focus on rescue breathing (91% right): drowning is a hypoxic arrest."),
    ("Bystander sees an adult collapse — first action after confirming unresponsiveness? [pattern]", "Call for help and EMS (speakerphone) and send for an AED, then check breathing and start compressions."),
  ],
  punch="An unresponsive adult who is not breathing normally gets a call, an AED and compressions, with no pulse hunt by a lay rescuer; a drowned or asphyxiated patient, or a child, needs breaths early because oxygen, not a shock, is what is missing.",
)

L['ACLS-72'] = dict(
  sub="Cardiology → BLS → AED arrival sequence",
  step=2,
  intro="Step 2 starts when the AED reaches the patient. Every action is arranged so that compressions stop only for analysis and the shock.",
  parts=[
    ('a', "**Switch on, attach the pads while compressions continue, stop only for analysis, deliver one shock if advised, resume compressions at once, reanalyse after 2 minutes.** Even when a shock ends VF, the stunned myocardium usually produces little or no output for the first minute or so (often a brief PEA or asystole), so a pulse check finds nothing and only costs perfusion. Two minutes of compressions both perfuses the myocardium and lets the rhythm declare itself. AHA 2025 prefers a single shock to stacked shocks (2a) because three shocks in a row lengthen the interruption, and today’s biphasic shock succeeds first time often enough that a second immediate shock adds little."),
  ],
  mimic=[
    ("AED single shock vs old three stacked shocks", "Single shock then 2 minutes of CPR is current; up to three stacked shocks survive only in the monitored, witnessed VF in the cath lab or after cardiac surgery, where the defibrillator is already attached (ERC)."),
  ],
  traps=[
    ("“Check the pulse straight after the shock to see if it worked”", "Resume compressions immediately; the check comes at the next 2-minute analysis."),
  ],
  decode=[
    ("What follows a delivered AED shock? [pattern]", "Immediate compressions for 2 minutes, no rhythm or pulse check."),
  ],
  punch="The AED pauses the chest twice only, to analyse and to shock; everything else, from pad placement to the post-shock period, happens with compressions running.",
)

L['ACLS-73'] = dict(
  sub="Cardiology → BLS → Pause and compression-fraction targets",
  step=2,
  intro="Step 2 puts numbers on the pauses. The real question asked which statement about shocks was false, and only 36% chose correctly: survival falls as the perishock pause lengthens, it does not rise.",
  parts=[
    ('a', "**Pre-shock pause as short as possible (AHA 2025, class 1); ERC 2025 says under 5 seconds; charge while compressions continue.** Charging takes several seconds; if done during compressions, the hands come off only for the final ‘clear’ and the shock. In 815 shockable out-of-hospital arrests (Cheskes 2011), a pre-shock pause of 20 seconds or more, against under 10, roughly halved the odds of survival to discharge (OR 0.47), and each extra 5 seconds cost about 18%; a perishock pause of 40 seconds or more, against under 20, did the same (OR 0.54)."),
    ('b', "**Post-shock pause as short as possible: resume compressions immediately, no rhythm or pulse check (AHA 2025, class 2a).** See ACLS-72: the post-shock heart is stunned and needs perfusion, not inspection. In the Cheskes data the post-shock pause alone was not independently linked to survival; the recommendation rests on the total perishock interruption and on physiology."),
    ('c', "**Compression fraction at least 60% (AHA 2025, class 2b, a minimum); good teams exceed 80%, which is not a guideline target.** Compression fraction is the share of the resuscitation during which compressions are being given. It is a measure of how few and how short the pauses are."),
    ('d', "**Rhythm checks every 2 minutes, timed with the compressor change.** AHA does not fix the interval in a recommendation, but 2 minutes matches the cycle of the algorithm and the point at which a compressor’s depth begins to fall, so one pause does two jobs."),
  ],
  mimic=[
    ("Pre-shock pause vs perishock pause", "Pre-shock is last compression to shock; perishock is pre-shock plus post-shock, from the last compression before to the first after."),
  ],
  traps=[
    ("“The perishock pause is directly proportional to survival”", "It is inversely related: the longer the pause, the lower the survival (a perishock pause of 40 seconds or more, against under 20, OR 0.54). This was the false statement (36% right)."),
    ("“Repeated shocks hardly change impedance, so this must be the false one”", "True as written: successive shocks lower transthoracic impedance only slightly, about 8% or less, which is one reason stacked shocks add little."),
    ("“Rescue shocks are not effective early in VF”", "They are most effective when VF has lasted only 1–2 minutes, before the myocardium is depleted; true statement, so not the answer."),
  ],
  decode=[
    ("Which is false about defibrillation: brief VF responds well; lowest effective energy; repeated shocks lower impedance ≤8%; perishock pause directly proportional to survival? [DocT GT]", "The last: the perishock pause is inversely related to survival."),
    ("Minimum chest compression fraction in adult CPR? [pattern]", "At least 60% (2b)."),
  ],
  punch="Coronary perfusion pressure falls within seconds of stopping and takes many compressions to rebuild, so every second of pause before or after a shock lowers the chance that the shock works; that is why the target is ‘as short as possible’.",
)

L['ACLS-74'] = dict(
  sub="Cardiology → BLS → Adult compression quality",
  step=1,
  intro="Step 1 also sets how the compressions are given. Each target exists because blood flow in CPR depends on how deeply the chest is squeezed and how fully it refills.",
  parts=[
    ('a', "**Rate 100 to 120 per minute.** Faster than 120 shortens each release phase, so the heart fills less and depth tends to fall (AHA 2025, 2a)."),
    ('b', "**Depth at least 5 cm, not more than 6 cm.** Deeper compressions eject more blood (class 1); beyond 6 cm, observational data show more injuries with no added survival, so the upper limit protects without costing flow."),
    ('c', "**Full recoil; do not lean on the chest.** The heart fills and the coronaries perfuse during release; residual leaning keeps intrathoracic pressure up and lowers coronary perfusion."),
    ('d', "**30:2 for one or two rescuers in an adult; with an advanced airway, continuous compressions and one breath every 6 seconds.** Once the airway is secured, breaths no longer need a pause; 10 a minute is enough because cardiac output during CPR is low."),
    ('e', "**Untrained bystander: continuous compression-only CPR.** In a witnessed adult cardiac arrest the blood is still oxygenated for the first minutes, so compressions matter more than breaths, and bystanders are more willing to start."),
  ],
  mimic=[
    ("Adult 30:2 vs child/infant 15:2 (two rescuers)", "Children arrest from hypoxia more often, so two rescuers give more breaths; a single rescuer uses 30:2 at any age beyond the newborn."),
  ],
  traps=[
    ("“Compression-only CPR is fine for a child or a drowning victim”", "In asphyxial arrest ventilation is the treatment; AHA 2025 prefers conventional CPR with breaths in children."),
  ],
  decode=[
    ("Adult compression rate and depth? [pattern]", "100–120/min, 5–6 cm, full recoil."),
  ],
  punch="Push at least 5 cm, at 100–120 a minute, and let the chest come all the way up; compressions alone suffice for a witnessed adult cardiac arrest, but not when hypoxia caused the arrest.",
)

L['ACLS-75'] = dict(
  sub="Cardiology → BLS → AED in special situations",
  step=2,
  intro="Step 2 ends with the situations that tempt a rescuer to hold the shock. In each, the problem is the contact between pad and skin or between current and device, and it is fixed in seconds.",
  parts=[
    ('a', "**Water or sweat: move the patient clear of standing water and dry the chest; rain or a wet surface alone is not a contraindication.** Water on the chest gives the current a path across the skin between the pads instead of through the heart."),
    ('b', "**Hairy chest: press the pads firmly; if they will not stick, shave or rip off a first set of pads and apply a second.** Air under the pad raises impedance and can cause burns or a ‘check pads’ message."),
    ('c', "**Pacemaker or ICD: pad at least 8 cm from the device, or anteroposterior; never withhold the shock.** Current passing through the generator can damage it or travel down the lead and burn the myocardium at its tip; moving the pad avoids that. Have the device checked afterwards."),
    ('d', "**Medication patch: remove it and wipe the skin.** The patch backing can block current and cause arcing and burns."),
    ('e', "**Child under 8 with no paediatric pads: use adult pads, anteroposterior.** AHA 2025 recommends a paediatric attenuator but allows an AED without one when nothing else is available; VF untreated is far more dangerous than an adult dose. Anteroposterior placement stops the large pads touching each other on a small chest."),
  ],
  mimic=[],
  traps=[
    ("“An implanted ICD is a reason not to use the AED”", "Shock, with the pad moved away from the device."),
  ],
  decode=[
    ("AED use in a 5-year-old with no paediatric pads? [pattern]", "Use adult pads, anteroposterior; do not delay the shock."),
  ],
  punch="Water, hair, devices, patches and small chests are interface problems: correct the contact and shock, because no one of them outweighs untreated VF.",
)

L['ACLS-76'] = dict(
  sub="Cardiology → Newborn resuscitation → Initial steps and the golden minute",
  step=3,
  intro="Step 3 changes patient: the newborn arrests because the lungs have not opened, not because of an arrhythmia, so the first minute is about warmth and air.",
  parts=[
    ('a', "**Initial steps, about 30 seconds: warmth, sniffing position, clear secretions only if obstructing, dry, stimulate; then assess breathing and heart rate.** Newborns lose heat fast through wet skin, and cold raises oxygen use and worsens acidosis, so drying and warming are resuscitation. A newborn’s large occiput flexes the neck on a flat surface and narrows the airway, so the head is brought to neutral or slight extension (sniffing). AHA 2025 makes routine oral, nasal or tracheal suctioning ‘No Benefit’; suction only a blocked airway."),
    ('b', "**Golden minute: initial steps, reassessment and, if needed, PPV all by 60 seconds of life.** AHA 2025 (class 1) says ventilation should begin within 60 seconds in an apnoeic or gasping baby. Most depressed newborns respond to ventilation alone; delay prolongs hypoxia and bradycardia."),
  ],
  mimic=[
    ("Non-vigorous baby with meconium: old tracheal suction vs current PPV", "Go straight to PPV; intubate and suction only if the trachea is obstructed (AHA 2025, 2a)."),
  ],
  traps=[
    ("“Suction the trachea of every non-vigorous meconium-stained baby before ventilating”", "Removed; it delays the ventilation that works."),
  ],
  decode=[
    ("Limp apnoeic term newborn — by when must PPV start? [pattern]", "Within 60 seconds of birth (the golden minute)."),
  ],
  punch="A newborn is resuscitated through the lungs: warm, open, dry, stimulate, and ventilate within the first minute.",
)

L['ACLS-77'] = dict(
  sub="Cardiology → Newborn resuscitation → Heart-rate thresholds",
  step=3,
  intro="Step 3’s decisions rest on the heart rate, because in a newborn bradycardia is the read-out of hypoxia and rises when the lungs are ventilated.",
  parts=[
    ('a', "**Below 100/min, or apnoea or gasping: start PPV.** AHA 2025 (class 1). A slowing newborn heart is a hypoxic heart, so ventilation is the treatment."),
    ('b', "**Below 60/min after 30 seconds of effective PPV: start compressions, secure the airway, FiO2 1.0.** AHA 2025 (class 1) says ‘despite 30 seconds of ventilation’; effective means chest rise. An advanced airway makes ventilation reliable during compressions, and 100% oxygen is given while compressing (2b)."),
    ('c', "**Above 100/min with spontaneous breathing: PPV may stop.** A rising heart rate is the best sign that ventilation is working."),
  ],
  mimic=[
    ("Under 100 vs under 60", "Under 100 starts ventilation; under 60 after effective ventilation adds compressions."),
  ],
  traps=[
    ("“Heart rate 50 at birth: start compressions first”", "Ventilate first; compressions start only if the rate stays under 60 after 30 seconds of effective PPV."),
  ],
  decode=[
    ("Newborn heart rate 80, gasping — next step? [pattern]", "PPV."),
  ],
  punch="Under 100 means ventilate; under 60 despite proven ventilation means compress; a rate rising above 100 says the ventilation has worked.",
)

L['ACLS-78'] = dict(
  sub="Cardiology → Newborn resuscitation → Ventilation corrective steps",
  step=3,
  intro="Step 3 also covers the commonest failure: PPV that does not move the chest. Until the chest rises, the baby has not been ventilated, whatever time has passed.",
  parts=[
    ('a', "**Mask reseal, reposition the head, suction mouth then nose, open the mouth, increase pressure in steps, then an alternative airway (ETT or laryngeal mask).** The order goes from the commonest and simplest cause of failure (mask leak, poor position) to the more invasive. Compressions are considered only after chest rise is achieved and 30 seconds of effective PPV have still left the heart rate below 60."),
  ],
  mimic=[],
  traps=[
    ("“No chest rise after 30 seconds of PPV and heart rate 50: start compressions”", "Correct the ventilation first; 30 seconds of PPV without chest rise does not count."),
  ],
  decode=[
    ("PPV for 30 seconds, chest not moving — first corrective step? [pattern]", "Adjust the mask to reseal it, then reposition the head."),
  ],
  punch="No chest rise means no ventilation; fix the mask, position, airway and pressure before the heart is blamed.",
)

L['ACLS-79'] = dict(
  sub="Cardiology → Newborn resuscitation → Chest compressions",
  step=3,
  intro="Step 3 reaches compressions only after effective ventilation has failed. The ratio favours breaths because the cause is still asphyxia.",
  parts=[
    ('a', "**3:1.** AHA 2025 (2b). More breaths per compression than in any other age group, because the lungs are the problem."),
    ('b', "**120 events a minute: 90 compressions and 30 breaths.** One cycle of 3 compressions and 1 breath every 2 seconds."),
    ('c', "**Two-thumb encircling technique, lower third of the sternum, one third of the AP diameter.** The two-thumb technique produces higher pressures and less fatigue than two fingers (2b)."),
    ('d', "**100% oxygen once compressions begin.** AHA 2025 (2b), then wean to saturation targets after recovery."),
    ('e', "**Reassess the heart rate every 60 seconds.** A shorter interval interrupts compressions before they can raise coronary perfusion; AHA 2025 recommends ECG monitoring for an accurate rate during compressions (class 1)."),
  ],
  mimic=[
    ("Newborn 3:1 vs child 15:2", "3:1 in the newborn (asphyxia); 15:2 for two rescuers beyond the newborn period, or in a newborn whose arrest is cardiac."),
  ],
  traps=[
    ("“Newborn compressions at 15:2 like a child”", "3:1 unless the arrest is known to be cardiac."),
  ],
  decode=[
    ("Newborn compressions: ratio and events per minute? [pattern]", "3:1, 90 compressions + 30 breaths = 120 events."),
  ],
  punch="Newborn compressions run at 3:1, 120 events a minute, two thumbs at a third of the chest depth, with 100% oxygen and a heart-rate check each minute.",
)

L['ACLS-80'] = dict(
  sub="Cardiology → Newborn resuscitation → Adrenaline and volume",
  step=3,
  intro="Step 3 ends with drugs, used only when ventilation and compressions together have not lifted the heart rate.",
  parts=[
    ('a', "**Heart rate still below 60 after at least 60 seconds of compressions with effective PPV and 100% oxygen.** AHA 2025 (class 1) ties adrenaline to optimised ventilation and compressions; given earlier it treats the wrong problem."),
    ('b', "**IV via umbilical venous catheter, or IO: 0.01–0.03 mg/kg (0.1–0.3 mL/kg of 1:10,000).** Confirmed in AHA 2025 (class 1). The umbilical vein is the quickest large vein at delivery; IO is acceptable if it fails (2a)."),
    ('c', "**Tracheal 0.05–0.1 mg/kg (0.5–1 mL/kg of 1:10,000).** AHA 2025 (2a), only while access is obtained; absorption from fluid-filled newborn lungs is unreliable, so the dose is higher."),
    ('d', "**Every 3 to 5 minutes while the heart rate stays below 60.** AHA 2025 (2b), preferably intravascular; give the IV dose as soon as access is obtained, whatever the interval since a tracheal dose."),
  ],
  mimic=[
    ("IV 0.01–0.03 vs tracheal 0.05–0.1 mg/kg", "The tracheal dose is about ten times higher because little is absorbed."),
  ],
  traps=[
    ("“Give the tracheal dose and delay the umbilical line”", "Tracheal adrenaline is a holding measure; access is not delayed for it."),
  ],
  decode=[
    ("Newborn heart rate 40 after 60 s of 3:1 CPR with 100% oxygen — dose of IV adrenaline? [pattern]", "0.01–0.03 mg/kg of 1:10,000 via the umbilical vein; 10 mL/kg saline or blood if there is no response and blood loss is suspected."),
  ],
  punch="Adrenaline comes last in newborn resuscitation, after proven ventilation and a minute of compressions, at 0.01–0.03 mg/kg IV; no response, think of blood loss and give volume.",
)

L['ACLS-81'] = dict(
  sub="Cardiology → ECMO → VA vs VV configuration",
  step=4,
  intro="Step 4 is the choice of circuit, decided by one question: does the heart need support or only the lung? The two real questions test the consequence of that choice: arrest on VV ECMO is treated with ordinary CPR, and the commonest VA circuit is femoro-femoral.",
  parts=[
    ('a', "**VA: gas exchange and circulation.** Blood is drained from the venous side and pumped, oxygenated, into an artery, so the circuit does the heart’s work as well as the lung’s."),
    ('b', "**VA cannulation: femoral vein to femoral artery peripherally; right atrium to aorta centrally.** Femoral cannulation is quick at the bedside or during CPR; central cannulation is used after cardiac surgery, through the open chest, and gives antegrade flow."),
    ('c', "**VA bypasses both the lungs and the heart.** That is why the native lungs and LV can be failing while the body is perfused, and why blood stagnating in the heart and lungs is a hazard (ACLS-84)."),
    ('d', "**VA indication: cardiogenic shock and cardiac arrest.**"),
    ('a', "**VV: gas exchange only.** Drained blood is oxygenated and returned to the venous side, so it reaches the right heart already oxygenated."),
    ('b', "**VV cannulation: femoro-jugular, or a dual-lumen cannula in the right internal jugular.** Drainage and return are both venous, so no artery is needed; the dual-lumen cannula drains from both venae cavae and returns towards the tricuspid valve from a single neck site, which limits recirculation and lets the patient mobilise."),
    ('c', "**VV: blood still traverses the lungs; the native heart does all the work.** Blood pressure and flow are entirely the patient’s own."),
    ('d', "**VV indication: severe isolated respiratory failure.** Hypoxaemia with an adequate cardiac output takes VV; add shock and it becomes VA."),
  ],
  mimic=[
    ("Arrest on VV vs arrest on VA ECMO", "On VV the circuit gives no flow to the body, so standard ACLS with compressions; on VA the circuit itself is the circulation."),
  ],
  traps=[
    ("“Arrest on VV ECMO: urgent conversion to VA” (the main wrong choice, 69% right)", "VV gives no circulatory support, so the immediate step is chest compressions; conversion to VA is a later decision."),
    ("“Defibrillate the asystole at 200 J”", "Shocks are for VF/pVT only; treat the cause, here hyperkalaemia."),
    ("“Epinephrine only, avoid compressions because of the cannulas”", "Compressions are needed; the cannulas are not a reason to withhold CPR on VV."),
  ],
  decode=[
    ("Patient on VV ECMO for ARDS, hyperkalaemia, VT then asystole — immediate next step? [DocT GT]", "Start chest compressions (standard ACLS); VV ECMO gives no circulatory support."),
    ("Image of cannulation — which type? [DocT GT]", "Peripheral VA femoro-femoral (83% right); a femoral vein drainage cannula with a femoral artery return cannula."),
  ],
  punch="Ask what is failing: lung alone takes VV, which still needs a beating heart; heart as well takes VA, which replaces it. Arrest on VV is therefore an ordinary arrest.",
)

L['ACLS-82'] = dict(
  sub="Cardiology → ECPR → Configuration, selection, timing, exclusions",
  step=5,
  intro="Step 5 applies VA ECMO to a heart that has stopped. The trials show it helps only when the right patient reaches the circuit quickly, with a fix waiting. The one real question tested the Surugadai criteria, and only 42% saw that a core temperature under 35 °C is not an exclusion.",
  parts=[
    ('a', "**Venoarterial, always.** With no cardiac output, blood returned to a vein would sit in a still heart; only arterial return perfuses the body."),
    ('b', "**Candidate: witnessed arrest, bystander CPR, initial shockable rhythm or another reversible cause, younger with few comorbidities, and a definitive treatment ready (PCI, thrombectomy, rewarming).** Each criterion shortens the no-flow time or predicts a heart and brain that can recover. AHA 2025 makes ECPR reasonable ‘in select patients when provided within an appropriately trained and equipped system of care’ (2a) but sets no fixed criteria; ELSO’s 2021 interim guideline uses age under 70, witnessed arrest, a shockable rhythm, no-flow under 5 minutes and low-flow under 60 minutes, and states these are consensus, not validated."),
    ('c', "**Low-flow time as short as possible; most target cannulation within 60 minutes of arrest.** Neurologically intact survival falls steeply with each minute of conventional CPR. ARREST (30 patients, refractory VF, a mobile cath-lab system) showed survival to discharge of 43% vs 7% and stopped early; Prague OHCA (264 patients) gave 31.5% vs 22.0% good neurological survival at 180 days (not significant); INCEPTION (160 randomised, 134 analysed, 10 Dutch centres) gave 20% vs 16% at 30 days (not significant). The benefit appears only in fast, experienced systems."),
    ('d', "**Exclusions: unwitnessed arrest, long no-flow time, terminal illness, severe aortic regurgitation, uncontrolled bleeding.** Aortic regurgitation lets retrograde ECMO flow fill the LV; bleeding forbids the heparin the circuit needs; aortic dissection is also an exclusion."),
  ],
  mimic=[
    ("Hypothermia 30–35 °C vs below 30 °C (Surugadai)", "Mild to moderate hypothermia is a protective, reversible state and favours ECPR; only a core temperature under 30 °C is listed as an exclusion."),
  ],
  traps=[
    ("“Core temperature under 35 °C excludes ECPR” (42% right)", "In the Surugadai criteria, as DocT quotes them, the exclusions are presumed non-cardiac cause, ROSC within 10 minutes of arrival, core temperature under 30 °C and pregnancy; 30–35 °C is not excluded."),
    ("“ROSC within 10 minutes is a reason to cannulate”", "It is an exclusion: the patient no longer has a refractory arrest."),
  ],
  decode=[
    ("Surugadai ECPR criteria — all are exclusions EXCEPT: non-cardiac cause, ROSC <10 min, core <35 °C, pregnancy? [DocT GT]", "Core temperature <35 °C (the exclusion is <30 °C)."),
    ("Which ECPR candidate does best? [pattern]", "Young, witnessed arrest, bystander CPR, refractory VF, flow within 60 minutes, PCI ready."),
  ],
  punch="ECPR is VA ECMO started in a refractory arrest so that a reversible cause can be fixed; it works only when the patient is well chosen and on the circuit within about an hour.",
)

L['ACLS-83'] = dict(
  sub="Cardiology → ECMO → Cardiogenic shock on VV ECMO",
  step=4,
  intro="Step 4 explains why a VV circuit cannot rescue a failing heart: it adds oxygen to the venous blood but nothing to the pump that delivers it.",
  parts=[
    ('a', "**Reconfigure to VA or VAV; no change in pump flow or sweep corrects falling cardiac output on VV.** Oxygen delivery is cardiac output times oxygen content; VV raises content, but if the native heart cannot pump, delivery falls and lactate rises. Pump flow and sweep act on oxygenation and CO2, which are not the failing step. VAV adds an arterial return limb to the VV circuit, so lung and heart are both supported. First exclude causes that VV itself can create or hide (tamponade, RV failure from high PEEP or acidosis, hypovolaemia) on echo."),
  ],
  mimic=[
    ("VV recirculation vs heart failure on VV", "Recirculation lowers patient saturation with a high drainage saturation; heart failure gives low pressure and rising lactate with adequate saturation."),
  ],
  traps=[
    ("“Increase ECMO flow to improve the shock on VV”", "More VV flow only adds oxygenated blood to the venous side; it does not raise cardiac output."),
  ],
  decode=[
    ("VV ECMO for ARDS, now cardiogenic shock with rising lactate despite inotropes — next? [pattern]", "Convert to VA (or VAV)."),
  ],
  punch="On VV ECMO the patient’s own heart delivers every litre; when it fails, the circuit must change to VA or VAV, because no setting on a VV circuit adds flow.",
)

L['ACLS-84'] = dict(
  sub="Cardiology → ECMO → Complications of peripheral VA ECMO",
  step=6,
  intro="Step 6 follows from the plumbing: femoral VA ECMO returns blood up the aorta, against the heart. The three real questions test the two complications that arise from it and their fixes.",
  parts=[
    ('a', "**Differential hypoxaemia (Harlequin, north-south): a recovering heart ejects blood from failing lungs into the aortic root and upper body, while ECMO flow supplies the lower body; monitor the right hand; treat by improving native oxygenation or converting to VAV.** The two streams meet at a ‘mixing zone’ in the aorta; when the LV recovers, it pushes the zone towards the abdomen, and the coronaries, brain and right arm receive the deoxygenated native output. The right subclavian comes off the brachiocephalic trunk, the first branch of the arch, so the right radial is the first site to show the native output’s low saturation; the femoral side reads high. Raising sweep FiO2 does nothing, because the ECMO blood is already fully oxygenated (left foot 99%). VAV adds a return cannula in the internal jugular, so oxygenated blood enters the right heart, passes the failing lungs and is ejected oxygenated by the LV."),
    ('b', "**LV distension: retrograde aortic flow raises afterload on a ventricle that cannot eject, so it never unloads; treat by venting (IABP, Impella, atrial septostomy).** A non-ejecting LV still fills: the venous cannula never drains all the return, so some blood crosses the lungs, and bronchial and Thebesian flow and any aortic regurgitation add to it; pressure rises, the aortic valve stops opening (flat arterial trace, loss of pulse pressure), left atrial pressure rises and pulmonary oedema follows, with a risk of thrombus in the stagnant LV. Lowering ECMO flow and adding an inotrope are the first steps; an Impella pulls blood out of the LV directly (ECPELLA, ACLS-85)."),
    ('c', "**Distal limb ischaemia: prevented by a distal perfusion cannula at cannulation.** The arterial cannula occludes most of the femoral artery, so the leg beyond it depends on collaterals. A cool, pale, pulseless foot needs an antegrade distal perfusion cannula into the superficial femoral artery at once; heparin, elevation or thrombectomy do not address a cannula blocking the vessel."),
  ],
  mimic=[
    ("Harlequin vs global hypoxaemia", "Harlequin: right hand low, foot high; global: both low, a circuit or oxygenator problem."),
    ("LV distension vs good LV recovery", "Distension: no pulse pressure, closed aortic valve, rising LA and PA pressures; recovery: rising pulse pressure with an opening valve."),
  ],
  traps=[
    ("“Harlequin: increase ECMO pump flow”", "More flow moves the mixing zone a little closer to the aortic root but raises LV afterload and does not oxygenate the native output; VAV is the definitive fix."),
    ("“Harlequin: increase sweep FiO2 to 1.0”", "The circuit blood is already saturated; the deoxygenated blood comes from the native lungs."),
    ("“Harlequin: convert to VV”", "The patient still needs circulatory support for cardiogenic shock; VV removes it."),
    ("“Cool pulseless leg: raise heparin, elevate, or thrombectomy”", "Place an antegrade distal perfusion cannula."),
  ],
  decode=[
    ("Femoral VA ECMO, right hand SpO2 84%, left foot 99%, TRALI — best intervention? [DocT GT]", "Convert to VAV with a return cannula in the internal jugular vein."),
    ("Femoral VA ECMO, right radial severe hypoxaemia, femoral gases good — modification? [DocT GT]", "Add a venous return cannula (VAV)."),
    ("Six hours after right femoral arterial cannulation, cold pale pulseless foot — next step? [DocT GT]", "Immediate antegrade distal perfusion cannula into the superficial femoral artery."),
  ],
  punch="Peripheral VA ECMO pumps blood backwards up the aorta: the upper body gets whatever the native lungs and heart send, the LV pushes against the circuit, and the cannulated leg loses its inflow. Put a sensor on the right hand, a vent on the LV and a cannula into the distal leg.",
)

L['ACLS-85'] = dict(
  sub="Cardiology → Mechanical support → IABP, Impella, VA ECMO",
  step=6,
  intro="Step 6 closes with the ladder of devices. Each adds more flow, but only one empties the LV, which explains why devices are combined. The real question asked which device works without cardiac synchrony, and the key is narrower than the truth.",
  parts=[
    ('a', "**Mechanism: IABP inflates in diastole and deflates in systole; Impella is a microaxial pump from LV to aorta; VA ECMO is full cardiopulmonary support.** The IABP is triggered from the ECG or arterial trace, so a fast irregular rhythm or no rhythm defeats it; the Impella and ECMO are continuous-flow pumps that run regardless of rhythm, even in VF."),
    ('b', "**Flow: IABP about 0.5 L/min; Impella 2.5–5 L/min by device; VA ECMO 4–6 L/min or more.** The IABP only augments native output and needs some (most sources give 0.5–1 L/min); the Impella’s output depends on the model (2.5 about 2.5 L/min, CP about 3.5–4, 5.0/5.5 about 5–5.5); ECMO can provide a full cardiac output and gas exchange."),
    ('c', "**LV workload: IABP modestly lowers afterload; Impella directly unloads the LV; VA ECMO increases LV afterload and may need a vent.** The Impella removes blood from the LV, lowering its volume, wall stress and oxygen use; retrograde ECMO flow does the opposite (ACLS-84). Evidence: IABP-SHOCK II showed no mortality benefit, and the 2025 ACC/AHA ACS guideline lists routine IABP as no benefit (3); ECLS-SHOCK (420 patients) found no fall in 30-day mortality with early VA ECMO in infarct-related shock (47.8 vs 49.0%) and more bleeding; DanGer Shock (360 STEMI-shock patients) found lower 180-day mortality with Impella CP (45.8 vs 58.5%) at the cost of more bleeding, limb ischaemia and RRT, and microaxial support is now 2a in selected patients."),
  ],
  mimic=[
    ("IABP vs continuous-flow devices", "Only the IABP needs a native rhythm and output; Impella, TandemHeart and VA ECMO do not."),
  ],
  traps=[
    ("“Only the Impella works despite an irregular rhythm” (keyed answer)", "Only the IABP needs synchrony; TandemHeart and VA ECMO are equally rhythm-independent, and ECMO even supports VF. On the exam pick the keyed Impella if offered, as the classic contrast to the IABP."),
    ("“VA ECMO unloads the LV because it gives the most flow”", "It raises LV afterload; most flow, least unloading."),
  ],
  decode=[
    ("Refractory shock with rapid AF — device that does not need cardiac synchrony? [DocT GT]", "Impella CP as keyed; strictly, TandemHeart and VA ECMO also qualify, only the IABP does not."),
    ("Rank IABP, Impella, VA ECMO by flow, and say which unloads the LV [pattern]", "IABP < Impella < VA ECMO; Impella unloads, ECMO loads."),
  ],
  punch="Flow rises from IABP to Impella to VA ECMO, but only the Impella empties the LV and only the IABP depends on the rhythm; ECMO’s full flow loads the ventricle, which is why it is sometimes paired with an Impella.",
)

FLAGS = {
  'ACLS-71': "Watch line (‘for a child … give 2 minutes of CPR first, then call’) holds for a lone rescuer without a phone at an unwitnessed collapse (ERC uses 1 minute); a witnessed sudden collapse in a child is likely arrhythmic and is call-and-AED first, and with a mobile phone any rescuer calls on speaker and starts CPR at once (AHA 2025). Agonal breathing: AHA 2025 quotes up to 40–60%, the card’s ‘up to 40%’ is the low end. The explanation says both.",
  'ACLS-85': "Card is correct. DocT GT keys Impella CP as the one device that works without cardiac synchrony; TandemHeart and VA-ECMO are equally rhythm-independent (only the IABP needs synchrony). The trap gives the exam-day answer.",
}
