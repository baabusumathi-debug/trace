# CVS07B — Explain v3 ("Learn" depth): post-cardiac-arrest temperature control — why cooling protects the brain, the trials (early cooling, TTM 2013, TTM2, Zeiner fever data)
# and how practice moved from hypothermia to fever prevention, the practical conduct and rewarming, cooling devices, the basic package and the three-tier shivering ladder, and the complications
# of cooling (cardiovascular, coagulation, infection, electrolytes, endocrine) and of shivering.
# No mnemonics or hooks. Driven by qpack/CVS07B.md (22 question links; PCA-35 and PCA-36 asked 4 times each, PCA-28 and PCA-34 three each). PCA-23, 24, 25, 26, 30, 37, 38, 39 and 40
# have no linked question and get short explanations with [pattern] decode items. No Top-up cards for this deck (cvs_topups.json has no CVS07B key).
# No `fix` entries exist for CVS07B in trace/test/data/qbank.json (checked 19 Nov 2026); cvs_cardlayer.json `lines` and `cross` notes for PCA-21, 28, 29, 31, 35 and 36 were read and used.
# Checked online on 19 Nov 2026:
#  - AHA 2025 Part 11 Post-Cardiac Arrest Care (cpr.heart.org): deliberate, protocolised temperature control for all adults not following commands after ROSC, any location or rhythm (COR 1, B-R);
#    maintain 32–37.5 °C (COR 1, B-R); at least 36 h (COR 2a, B-R); avoid rewarming faster than 0.5 °C/h (COR 2b); unclear whether hypothermia vs normothermia helps in sicker subgroups (2b);
#    routine rapid infusion of cold IV fluids for prehospital cooling: COR 3 No Benefit; text: 36 h total is the shortest recommended duration, TTM trials used 72 h, fever prevention may follow
#    a hypothermic period, fever strongly associated with poor outcome; MAP ≥65; neuroprognostication ≥72 h after normothermia.
#  - ERC–ESICM 2025 post-resuscitation care (via the ERC/ESICM text reproduced by resus.org.uk): actively prevent fever by targeting ≤37.5 °C in patients who remain comatose; for 36–72 h;
#    do not actively rewarm comatose patients with mild hypothermia (32–36 °C) after ROSC; recommend against routine prehospital cooling with large volumes of cold IV fluid.
#  - ERC–ESICM 2021 post-resuscitation guideline (Nolan, Resuscitation/Intensive Care Med 2021; esanum summary): TTM for adults unresponsive after ROSC, any rhythm; constant target 32–36 °C for at least 24 h;
#    avoid fever (>37.7 °C) for at least 72 h. ERC–ESICM 2022 temperature-control update after TTM2 (Sandroni, Intensive Care Med 2022, PubMed 35089409): prevent fever (>37.7 °C) for at least 72 h;
#    insufficient evidence for or against 32–36 °C.
#  - ERC–ESICM 2025 exact wording (resus.org.uk 2025 page): ‘actively prevent fever by targeting a temperature ≤37.5 °C’; ‘prevent active fever for 36 to 72 h’.
#  - Reviewer check 19 Nov 2026: RINSE (Bernard, Circulation 2016, PubMed 27562972): 1,198 OHCA, up to 2 L cold saline DURING CPR; ROSC in shockable rhythms 41.2 vs 50.6% (P = .03); discharge survival 10.2 vs 11.4% (NS).
#    Columbia protocol table (Badjatia/Choi; PMC5882245): baseline paracetamol 650–1000 mg q4–6h, buspirone 30 mg q8h, magnesium to 3–4 mg/dL, counter-warming ≤43 °C; step 1 dexmedetomidine or opioid;
#    step 2 dexmedetomidine + opioid; step 3 propofol; step 4 NMB. BSAS 0 none, 1 neck/thorax, 2 intermittent upper limbs and thorax, 3 generalised or sustained limb shivering.
#    Measured ICU cooling rates (Hoedemaekers, Crit Care 2007, via J Intensive Care 2016 table 2): devices about 1.0–1.5 °C/h, cold fluid plus ice ~0.3 °C/h; card’s rate table is from a different source.
#  - TTM (Nielsen, NEJM 2013; expanded abstract Crit Care 2015): 939 patients; death at end of trial 235/473 (50%) vs 225/466 (48%), HR 1.06 (0.89–1.28), p 0.51; death or poor CPC at 180 d 54 vs 52%,
#    RISK ratio 1.02 (0.88–1.16), p 0.78; death or poor mRS 52 vs 52%, RR 1.01 (0.89–1.14), p 0.87. Commentary: slow to target (~10 h), fast rewarming, ~1 patient per centre per month.
#  - TTM2 (Dankiewicz, NEJM 2021; Critical Care Reviews summary): 1900 randomised, 1861 ITT, 925 vs 925 for death; 33 °C for 28 h then rewarming at ~1/3 °C/h (to 40 h); normothermia: aim ≤37.5 °C,
#    device if ≥37.8 °C; 36.5–37.7 °C to 72 h if still comatose; death 6 mo 465/925 (50%) vs 446/925 (48%), RR 1.04 (0.94–1.14), p 0.37; mRS 4–6 55 vs 55%, RR 1.00; arrhythmia with
#    haemodynamic compromise 24 vs 17%, RR 1.45 (1.21–1.75), p <0.001; blinded outcome assessors.
#  - HYPERION (Lascarrou, NEJM 2019; WikiJournalClub): 581 non-shockable, 33 °C for 24 h vs 36.5–37.5 °C; CPC 1–2 at 90 d 10.2 vs 5.7% (difference 4.5 points, 95% CI 0.1–8.9); mortality 81.3 vs 83.2% (NS).
#  - CAPITAL CHILL (Le May, JAMA 2021; ACC summary): 389 OHCA, 31 vs 34 °C; death or poor neurological outcome at 180 d 48.4 vs 45.4% (p 0.56); longer CICU stay at 31 °C (10 vs 7 d).
#  - Zeiner (Arch Intern Med 2001, JAMA Network abstract): 151 of 698 patients; lowest temperature within 4 h 35.8 vs 35.2 °C (P = .002; table gives 36.0 °C, P = .001); highest in 48 h 37.7 vs 38.3 °C
#    (P <.001); OR 2.26 (1.24–4.12) per °C above 37 °C; observational.
# From standard references (reviewer agrees; worded softly where less sure): HACA 2002 (275 VF patients, 32–34 °C for 24 h; favourable outcome 55 vs 39%, death 41 vs 55%) and Bernard 2002
# (77 patients, 33 °C for 12 h; good outcome 49 vs 26%); Kim, JAMA 2014 (1,359 patients, prehospital 2 L cold saline: no survival or neurological benefit, more re-arrest and pulmonary oedema);
# PRINCESS (JAMA 2019, 677 patients, intra-arrest transnasal cooling, good outcome 16.6 vs 13.5%, NS); TTM-48 (Kirkegaard 2017: 48 vs 24 h at 33 °C, no difference); cerebral metabolism falls about 6–10% per °C (Polderman);
# CYP450 clearance falls about 7–22% per °C below 37 (Tortorici 2007); Bedside Shivering Assessment Scale 0–3 (Badjatia 2008); Columbia anti-shivering protocol (Choi 2011: baseline paracetamol,
# buspirone 30 mg q8h, magnesium to 3–4 mg/dL, skin counter-warming, then dexmedetomidine/opioid, then propofol, then paralysis); IBCC temperature packages (the card’s source for PCA-33–36);
# magnesium 1 mg/dL ≈ 0.41 mmol/L; Polderman 2009 review of the physiology and complications of hypothermia; Kurz 1996 (perioperative hypothermia and wound infection).
# Could not trace: the source of the early-trial percentages on PCA-23 (they are not the HACA or Bernard figures).

SPINE = [
  ("Why cooling protects the brain", "After ROSC the brain is injured a second time by reperfusion, excitotoxicity, calcium overload, inflammation and fever, and lowering temperature slows every one of these processes, not just oxygen use."),
  ("The trials walked hypothermia back", "Early trials doubled good outcomes with cooling, then TTM found 33 °C no better than 36 °C and TTM2 found it no better than fever prevention, so the one firm conclusion left is that fever harms."),
  ("Running temperature control", "Every comatose survivor gets a core probe and a controlled temperature, now 32–37.5 °C (AHA) or ≤37.5 °C (ERC–ESICM) for at least 36 hours, with slow, controlled rewarming and no fever afterwards."),
  ("Choosing a cooling method", "Fast, free methods such as cold fluid and ice can bring temperature down but cannot hold it, so a feedback-controlled surface or endovascular device is what maintains the target."),
  ("The shivering ladder", "Shivering raises oxygen use, ICP and lactate in the brain being protected, so it is treated in tiers from paracetamol, buspirone, magnesium and counter-warming, through sedation, to paralysis last."),
  ("Complications of cooling", "Cooling shifts potassium, magnesium and phosphate into cells, impairs clotting and immunity, disturbs insulin and glucose, and strains the heart, and most of these reverse at rewarming."),
]

PRIMER = "After cardiac arrest, return of circulation is not the end of brain injury: the hours that follow bring reperfusion injury, calcium-driven cell death and, often, fever, and these decide whether a comatose survivor wakes up. Body temperature is one of the few things that alters all of these processes at once, which is why it became the first neuroprotective treatment after arrest. ‘Comatose’ in the guidelines means not following verbal commands after ROSC; it is the entry criterion for every card here. Core temperature is measured centrally (bladder, oesophagus or pulmonary artery), not at the skin."

L = {}

L['PCA-21'] = dict(
  sub="Post-arrest care → Temperature control → Why cooling protects (mechanisms 1)",
  step=1,
  intro="Step 1 explains why anyone tried cooling the brain after arrest. The damage done after ROSC (the post-cardiac-arrest brain injury) runs on temperature-dependent chemistry, so cooling slows it down. The DocT question that only half the cohort got right tests whether you see this as many mechanisms together or as one.",
  parts=[
    ('a', "**Purpose: to limit neurological injury after resuscitation from cardiac arrest.** The heart is restarted, but the brain keeps being damaged for hours to days by secondary injury. Temperature control is aimed only at that secondary injury, which is why it is offered to patients who are not following commands (they are the ones with a brain at risk)."),
    ('b', "**Reduces brain metabolism, oxygen use and ATP consumption.** Cerebral metabolic rate falls by roughly 6–10% for each degree Celsius of cooling, so the brain needs less oxygen and burns less ATP while its blood flow is still unreliable. This is the Marrow answer to ‘rationale after VF arrest’: reduced cerebral oxygen consumption. It is real but modest; mild cooling protects more than the metabolic fall alone would explain, which is why part c and d matter."),
    ('c', "**Inhibits the release of glutamate and dopamine.** Ischaemia floods the synapse with excitatory amino acids, glutamate opens NMDA channels and calcium pours into neurones (excitotoxicity). Cooling reduces this release, so fewer neurones are pushed into the calcium overload of part d."),
    ('d', "**Inhibits apoptosis, by reducing calcium overload and glutamate release.** Calcium overload activates the enzymes and mitochondrial pathways that trigger programmed cell death in the days after arrest. Less glutamate means less calcium entry, and less calcium means fewer neurones enter that pathway."),
  ],
  mimic=[
    ("Single mechanism vs combination", "Every single-mechanism option (‘primarily metabolic’, ‘primarily vasoconstriction’, ‘selectively apoptosis’) is wrong; the correct option always names several pathways (reperfusion, excitotoxins, blood-brain barrier)."),
  ],
  traps=[
    ("“Hypothermia primarily reduces metabolism linearly and uniformly across the brain”", "Metabolism does fall, but neither linearly nor uniformly, and it is not the whole story; this was the most chosen wrong option when only 50% were right."),
    ("“The primary benefit is cerebral vasoconstriction that lowers ICP”", "Cerebral blood flow falls because metabolism falls (coupling), not as the protective mechanism; raised ICP is not the main problem after arrest."),
    ("“Hypothermia selectively inhibits apoptosis with little effect on inflammation or free radicals”", "It suppresses inflammation and oxidative injury too (PCA-22); ‘selectively’ is the wrong word."),
  ],
  decode=[
    ("Which statement best describes the rationale for hypothermia’s neuroprotective effect? [DocT]", "The option listing several pathways together: reperfusion injury, excitatory neurotransmitters, blood-brain barrier (50% right)."),
    ("Rationale for therapeutic hypothermia after VF arrest? [Marrow]", "Reduced cerebral oxygen consumption."),
  ],
  punch="Cooling protects the post-arrest brain by slowing many processes at once: metabolism and oxygen use, glutamate release, calcium overload and apoptosis; any option that credits one mechanism alone is wrong.",
)

L['PCA-22'] = dict(
  sub="Post-arrest care → Temperature control → Why cooling protects (mechanisms 2)",
  step=1,
  intro="Step 1 continues with the rest of the secondary injury. Beyond metabolism and excitotoxicity (PCA-21), reperfusion brings oxygen radicals, inflammation and a leaky blood-brain barrier, and cooling damps each of them. The same DocT question links here: the correct option names reperfusion injury and the blood-brain barrier.",
  parts=[
    ('a', "**Suppresses post-ischaemic inflammation, reduces reperfusion injury and reoxygenation injury (lipid peroxidation, oxidative stress).** When oxygen returns to ischaemic tissue, mitochondria and enzymes produce free radicals that peroxidise membrane lipids, and activated microglia and leucocytes release cytokines. These reactions are temperature-dependent, so they run slower in a cooler brain."),
    ('b', "**Reduces brain CMRO₂, cerebral oedema, seizure activity and apoptosis.** Less oxygen demand, less fluid leaking into the tissue, a higher seizure threshold and fewer cells entering programmed death all follow from the slower chemistry."),
    ('c', "**Preserves the blood-brain barrier.** The barrier fails after ischaemia as endothelial tight junctions are broken down by proteases; keeping it intact limits vasogenic oedema and the entry of inflammatory cells."),
    ('d', "**Limits vasodilatation, capillary leak and multiorgan dysfunction.** The whole-body ischaemia-reperfusion response after arrest resembles sepsis; cooling damps the systemic inflammation that drives vasoplegia and leak."),
  ],
  mimic=[
    ("Post-arrest syndrome vs sepsis", "Both have vasodilatation, capillary leak and organ failure from systemic inflammation; after arrest the trigger is whole-body ischaemia-reperfusion, not infection."),
  ],
  traps=[
    ("“Hypothermia has minimal effect on neuroinflammation and free radical production”", "These are two of its main targets; this option (D) was a common wrong choice."),
  ],
  decode=[
    ("Which statement best describes hypothermia’s neuroprotective rationale? [DocT]", "Attenuating reperfusion injury, decreasing excitatory neurotransmitters and stabilising the blood-brain barrier (50% right)."),
  ],
  punch="Cooling also blunts reperfusion and reoxygenation injury, inflammation, oedema and seizures, and keeps the blood-brain barrier intact; protection comes from the sum of these, not from any one.",
)

L['PCA-23'] = dict(
  sub="Post-arrest care → Evidence → Early induced-hypothermia data",
  step=2,
  intro="Step 2 starts where the enthusiasm started. Early data seemed to show cooling roughly doubled good neurological outcome after arrest, in both shockable and non-shockable rhythms. No question is linked to these figures; the exam asks the direction, and the landmark 2002 trials, more than these exact numbers.",
  parts=[
    ('a', "**VF/VT: favourable neurological outcome 39% with normothermia vs 77% with hypothermia.** The shockable group did best, as in every arrest series, because VF arrests are usually witnessed, cardiac and short."),
    ('b', "**PEA/asystole: 7% vs 25%.** Non-shockable arrests start from a much lower baseline (longer no-flow, non-cardiac causes). Randomised evidence in this group came later: HYPERION (2019, 581 patients) found 33 °C gave 10.2% vs 5.7% good outcome at 90 days, a fragile result with no mortality difference."),
    ('c', "**GCS 15 at ICU discharge: 20% control vs 41% hypothermia.**"),
    ('d', "**Mortality at 6 months: 78% control vs 56% hypothermia.** These are the card’s figures; they are not from the two 2002 randomised trials. Those are the ones usually asked: HACA (275 VF patients, 32–34 °C for 24 h) raised favourable outcome from 39% to 55% and lowered 6-month death from 55% to 41%; Bernard (77 patients, 33 °C for 12 h) raised good outcome from 26% to 49%."),
  ],
  mimic=[
    ("Early trials vs TTM/TTM2", "The early trials compared cooling with no temperature control, so the control groups often became febrile. TTM and TTM2 compared cooling with a controlled, fever-free temperature, and the difference disappeared."),
  ],
  traps=[
    ("“Hypothermia was shown to help only VF arrests”", "Early data showed gains in both rhythms; current guidelines apply temperature control to any rhythm."),
  ],
  decode=[
    ("[pattern] Landmark 2002 trials that established hypothermia after VF arrest", "HACA and Bernard: 32–34 °C for 12–24 h, about one extra good outcome for every 4–6 treated."),
  ],
  punch="The early trials showed cooling roughly doubled good outcome in both rhythms, but their controls were left to become febrile, which is why later trials with controlled normothermia did not reproduce the effect.",
)

L['PCA-24'] = dict(
  sub="Post-arrest care → Evidence → TTM trial (2013), primary outcome",
  step=2,
  intro="Step 2’s first turn. TTM asked whether the depth of cooling mattered, and found that 36 °C was as good as 33 °C. No question is linked, but this trial is why ‘36 °C’ appears in so many keys.",
  parts=[
    ('a', "**Targeted temperature management at 33 °C vs 36 °C after cardiac arrest.** 939 comatose OHCA survivors of presumed cardiac cause, any rhythm; both arms were held at target for 28 hours and fever was prevented to 72 hours. The control arm was not ‘no treatment’: 36 °C is actively controlled normothermia."),
    ('b', "**In comatose OHCA survivors, TTM at 36 °C is as good as 33 °C.** The trial could not show that cooling helps; it showed that deeper cooling does not add anything once temperature is controlled."),
    ('c', "**Death at end of trial: 235/473 (50%) at 33 °C vs 225/466 (48%) at 36 °C; HR 1.06 (0.89–1.28), p 0.51.** A hazard ratio this close to 1 with a confidence interval spanning it is a clearly neutral result."),
    ('d', "**Limitations: non-blinded, too many exclusions, sedation details not available.** Other criticisms often quoted: target was reached slowly (several hours after ROSC), rewarming was fast, and enrolment was slow (about one patient per centre per month), raising concern about selection."),
  ],
  mimic=[
    ("TTM vs TTM2", "TTM: 33 vs 36 °C (depth of cooling). TTM2: 33 °C vs normothermia ≤37.5 °C with fever prevention (cooling vs no cooling)."),
  ],
  traps=[
    ("“TTM showed 36 °C is better than 33 °C”", "It showed no difference; ‘as good as’, not ‘better’."),
  ],
  decode=[
    ("[pattern] Trial comparing 33 °C with 36 °C after OHCA, and its result", "TTM (Nielsen 2013): no difference in death or neurological outcome."),
  ],
  punch="TTM showed that once temperature is controlled, 33 °C is no better than 36 °C: the depth of cooling does not matter.",
)

L['PCA-25'] = dict(
  sub="Post-arrest care → Evidence → TTM trial (2013), secondary outcomes",
  step=2,
  intro="Step 2, TTM’s secondary outcomes. They matter only because they close the door on a subgroup or secondary benefit: every one is neutral. No question is linked.",
  parts=[
    ('a', "**CPC 3–5: 251/469 (54%) vs 242/464 (52%); 1.02 (0.88–1.16), p 0.78.** CPC 3–5 means severe disability, vegetative state or death, so this outcome includes the deaths. The paper reports this as a risk ratio, not a hazard ratio (FLAG)."),
    ('b', "**mRS 4–6: 245/469 (52%) vs 239/464 (52%); 1.01 (0.89–1.14), p 0.87.** mRS 4–6 is moderately severe disability, severe disability or death; again a risk ratio."),
    ('c', "**Deaths at 180 days: 226/473 (48%) vs 220/466 (47%); 1.01 (0.87–1.15), p 0.92.**"),
  ],
  mimic=[
    ("CPC 3–5 vs mRS 4–6", "Both are ‘poor outcome including death’ on different scales: CPC is 1–5, mRS is 0–6."),
  ],
  traps=[
    ("“TTM was negative on the primary but favoured 33 °C on neurological outcome”", "Every endpoint had a ratio of about 1.0 and a large p value; the trial is uniformly neutral."),
  ],
  decode=[
    ("[pattern] TTM 2013 neurological outcome at 6 months", "No difference: about half in each arm had died or had a poor outcome."),
  ],
  punch="TTM’s secondary outcomes were as neutral as its primary: about half of each arm died or had a poor neurological outcome, with every ratio close to 1.",
)

L['PCA-26'] = dict(
  sub="Post-arrest care → Evidence → TTM2 trial (2021)",
  step=2,
  intro="Step 2’s second turn, and the trial behind the change in current guidelines. TTM2 compared 33 °C with normothermia plus fever prevention and found no benefit from cooling, with more arrhythmia. No question is linked; the card’s watch line notes the source dates it wrongly (it is 2021).",
  parts=[
    ('a', "**Open-label with blinded outcome assessment; comatose adults after OHCA; n = 1850.** 1900 were randomised, 1861 analysed; 1850 had the primary outcome (925 per arm). Clinicians cannot be blinded to temperature, so blinding the people who scored the 6-month outcome is what protects the result."),
    ('b', "**Hypothermia: 33 °C, then controlled rewarming. Normothermia: ≤37.5 °C, fever treated early, device cooling at ≥37.8 °C.** The hypothermia arm was held at 33 °C for 28 hours from randomisation, then rewarmed at about one-third of a degree per hour. The normothermia arm used antipyretics and only started a device if the temperature reached 37.8 °C; both arms had fever prevention to 72 hours."),
    ('c', "**Death from any cause at 6 months: 50% vs 48%.** RR 1.04 (0.94–1.14), p 0.37."),
    ('d', "**mRS 4 or more at 6 months: 55% vs 55%.** Functional outcome was identical."),
    ('e', "**Arrhythmia with haemodynamic compromise: 24% vs 17%.** RR 1.45, p <0.001: cooling to 33 °C slows conduction, causes bradycardia and prolongs repolarisation, and these turned into a measurable harm."),
    ('f', "**Hypothermia did not lead to a lower 6-month incidence of death than normothermia.**"),
  ],
  mimic=[
    ("TTM2 vs HYPERION", "TTM2 (mostly shockable, 1850 patients): no benefit from 33 °C. HYPERION (non-shockable only, 581 patients): small gain in good outcome with 33 °C, no mortality difference. Guidelines weigh TTM2 more heavily."),
  ],
  traps=[
    ("“TTM2 compared 33 °C with no temperature control”", "The control arm actively prevented fever (≤37.5 °C); that is why it counts as temperature control."),
  ],
  decode=[
    ("[pattern] Trial showing no benefit of 33 °C over normothermia after OHCA", "TTM2 (Dankiewicz, NEJM 2021); more arrhythmia with hypothermia."),
  ],
  punch="TTM2 showed that cooling to 33 °C gave no survival or functional benefit over strict fever prevention and caused more haemodynamically significant arrhythmia.",
)

L['PCA-27'] = dict(
  sub="Post-arrest care → Evidence → Fever after arrest (Zeiner 2001)",
  step=2,
  intro="Step 2’s constant. While trials argued about how far to cool, observational data such as Zeiner’s kept showing that fever after arrest is bad. The one linked GT question tests what must be avoided during temperature control, and everyone got it.",
  parts=[
    ('a', "**Objective: the impact of body temperature on neurological outcome after successful CPR.** It was observational: 151 of 698 resuscitated patients, temperature recorded for 48 hours, outcome at 6 months."),
    ('b', "**Lowest temperature within 4 hours: favourable 35.8 °C vs unfavourable 35.2 °C.** The worse brains were colder early, because a severe brain injury impairs thermoregulation and these patients drift down on their own. This is why spontaneous hypothermia after ROSC is not a good sign, and why ERC–ESICM 2025 says not to actively rewarm it. The abstract gives P = .002, not 0.02 as on the card (FLAG)."),
    ('c', "**Highest temperature in the first 48 hours: favourable 37.7 °C vs unfavourable 38.3 °C (p <0.001).** Fever after arrest comes from the inflammatory post-arrest syndrome, aspiration pneumonia and a damaged hypothalamus, and it raises the brain’s metabolic demand when supply is weakest."),
    ('d', "**For each degree above 37 °C, the odds of unfavourable recovery rise with an OR of 2.26 (95% CI 1.24–4.12).** The watch line is right that the reference is 37 °C, not 97 °F."),
    ('e', "**Conclusion: hyperthermia is a potential factor for unfavourable neurological recovery after successful CPR.** Being observational, it shows association, not cause; but TTM2 later made fever prevention the active comparator, and the guidelines now make it the core of temperature control."),
  ],
  mimic=[
    ("Early spontaneous hypothermia vs later fever", "Both mark a worse outcome: early low temperature reflects severe injury; later fever adds injury. Neither is a reason to rewarm actively or to accept the fever."),
  ],
  traps=[
    ("Picking only ‘fever’ when ‘all of the above’ includes hypoxia and hyperventilation", "During temperature control fever, hypoxia and hypocapnia (cerebral vasoconstriction) are all avoided; the key is ‘all of the above’ (100% right)."),
  ],
  decode=[
    ("Patient undergoing TTM after arrest — what should be avoided? [DocT GT]", "All of the above: fever, hypoxia and hyperventilation."),
  ],
  punch="Fever after arrest is consistently linked to worse neurological outcome, about doubling the odds of a poor recovery for each degree above 37 °C, and preventing it is the part of temperature control every guideline keeps.",
)

L['PCA-28'] = dict(
  sub="Post-arrest care → Evidence → How practice changed: hypothermia to fever prevention",
  step=2,
  intro="Step 2 summed up. The evidence moved from ‘cool to 32–34 °C’ to ‘control temperature and never let it rise’, and the bank keys lag behind. Three linked questions: two DocT keys are historical or disputed, so the exam-day answer depends on which era the options come from.",
  parts=[
    ('a', "**Early trials: hypothermia better than normothermia; favourable outcome roughly doubled.** HACA and Bernard (PCA-23) produced the 2002–2010 recommendation of 32–34 °C for 12–24 hours after VF arrest. That is the DocT QBank key (32–34 °C), right for its era and only 57% chose it."),
    ('b', "**TTM 2013: 36 °C is as good as 33 °C; the depth of cooling does not matter.** Guidelines widened to a constant 32–36 °C."),
    ('c', "**TTM2: hypothermia is no better than normothermia, and causes more arrhythmia.** This was the decisive trial; CAPITAL CHILL (31 vs 34 °C, 2021) also found that deeper cooling did not help and lengthened ICU stay."),
    ('d', "**ERC/ESICM 2021: TTM at 36 °C; constant 32–36 °C for ≥24 h; prevent fever for at least 72 h.** The 2021 guideline (published before TTM2) did say: keep a constant 32–36 °C for at least 24 hours and avoid fever above 37.7 °C for at least 72 hours; it did not single out 36 °C. After TTM2, the 2022 ERC–ESICM update dropped the 32–36 °C target and kept only fever prevention (>37.7 °C) for at least 72 hours. ERC–ESICM 2025 now says: actively prevent fever at ≤37.5 °C for 36–72 hours, and do not actively rewarm mild spontaneous hypothermia (32–36 °C)."),
    ('e', "**What survives: fever is harmful (PCA-27); the debate was only about how far below normal to go.** AHA 2025 calls it temperature control: a deliberate protocol for any adult not following commands after ROSC, any rhythm and any location, at 32–37.5 °C (COR 1) for at least 36 hours (COR 2a). Routine prehospital cooling with rapid cold IV fluid is COR 3, no benefit."),
  ],
  table=dict(title="How the recommended target changed", head=["Era", "Target", "Duration"], rows=[["AHA 2002–2010", "32–34 °C", "12–24 h"], ["After TTM (ERC–ESICM 2015, AHA 2015/2020)", "constant 32–36 °C", "≥24 h"], ["ERC–ESICM 2021", "constant 32–36 °C, then no fever >37.7 °C", "≥24 h; fever ≥72 h"], ["ERC–ESICM 2022 (after TTM2)", "prevent fever (>37.7 °C)", "≥72 h"], ["ERC–ESICM 2025", "**prevent fever, ≤37.5 °C**", "36–72 h"], ["AHA 2025", "**32–37.5 °C**", "≥36 h"]]),
  mimic=[
    ("Hypothermic vs normothermic temperature control", "Both are ‘temperature control’ in AHA 2025: 32–34 °C or 36–37.5 °C; what is not allowed is fever."),
  ],
  traps=[
    ("“Target for VF OHCA is 32–34 °C” as the only correct range", "That is the 2002–2010 answer (DocT key). If a 32–37.5 °C or fever-prevention option is offered, choose it; if the options are only historical ranges, 32–34 °C is the keyed one."),
    ("“Delaying initiation of TH increases mortality” (DocT key, 47–50% right)", "No RCT shows that faster cooling helps; prehospital cold saline after ROSC (Kim, JAMA 2014, 1,359 patients) gave no benefit and more re-arrest and pulmonary oedema, and cold saline during CPR (RINSE, 2016) lowered ROSC in shockable rhythms. The key rests on old observational data, but it is the least wrong option: the others are clearly false (not all arrests; 24 not 48 h; shivering is harmful)."),
    ("“34 °C is wrong” after a VF OHCA (Marrow key 34 °C)", "34 °C sits inside AHA’s 32–37.5 °C range, so it is acceptable when the question follows AHA; if it follows ERC, pick normothermia with fever prevention."),
  ],
  decode=[
    ("Recommended target temperature after out-of-hospital VF arrest? [DocT]", "Keyed 32–34 °C (historical); current AHA 32–37.5 °C (57% right)."),
    ("Which statement about therapeutic hypothermia is correct? [DocT]", "Keyed ‘delaying initiation increases mortality’; the others are plainly wrong (47% right)."),
    ("Comatose after VF OHCA, absent brainstem reflexes — next step? [Marrow]", "Temperature control (keyed 34 °C); brain death cannot be declared this early after arrest."),
  ],
  punch="Practice moved from cooling to 32–34 °C to simply controlling temperature (AHA 32–37.5 °C for at least 36 hours, ERC–ESICM ≤37.5 °C): the only conclusion that has survived every trial is that fever harms.",
)

L['PCA-29'] = dict(
  sub="Post-arrest care → Conduct → Phases, duration and rewarming",
  step=3,
  intro="Step 3 turns the evidence into a protocol. The phases are induction, maintenance, controlled rewarming and then fever prevention, and the two linked questions test why rewarming must be slow and which statements about cooling are true.",
  parts=[
    ('a', "**AHA 2025: deliberate temperature control at 32–37.5 °C (COR 1) for at least 36 h (COR 2a). ERC–ESICM 2025: prevent fever (≤37.5 °C) for 36–72 h; do not actively rewarm mild hypothermia (32–36 °C). There is no fixed 24 h + 24 h schedule.** The older teaching of 24 hours at target then 24 hours of rewarming has gone; the trials actually ran 72 hours of temperature management in all, and AHA calls 36 hours the minimum."),
    ('b', "**Rewarming is controlled, no faster than 0.5 °C/h (AHA COR 2b).** Rapid rewarming raises cerebral metabolic demand abruptly in a brain whose oxygen delivery is still fragile, causes vasodilatation and hypotension, and lets potassium move back out of cells (rebound hyperkalaemia; PCA-38). TTM2 rewarmed at about 0.33 °C/h, HYPERION at 0.25–0.5 °C/h."),
    ('c', "**TTM involves: an invasive core temperature probe, a safe target, and coordinated multimodal shivering control.** Bladder or oesophageal probes (PCA-33) feed the device’s feedback loop; shivering control is the tier system (PCA-34–36)."),
    ('d', "**It is always preferable to prevent fever and shivering, if possible.** Preventing is easier than reversing: once a fever or shivering has started, more drugs and deeper sedation are needed, and those cloud neuroprognostication."),
  ],
  mimic=[
    ("Controlled rewarming after TTM vs rewarming in accidental hypothermia", "Afterdrop (core temperature falling further as cold peripheral blood returns) is an accidental-hypothermia phenomenon during field rewarming; it is not the reason for slow rewarming after TTM."),
  ],
  traps=[
    ("“Slow rewarming prevents a rapid fall in potassium”", "The direction is wrong: rewarming moves potassium out of cells, so the risk is hyperkalaemia (option C)."),
    ("“Rapid rewarming causes a paradoxical fall in core temperature”", "That describes afterdrop in accidental hypothermia (option D); the answer is the cerebral demand-supply mismatch (only 45% right)."),
    ("“Temperature goal is 32–36 °C for 48 hours” or “TH is for all cardiac arrests”", "Temperature control is for comatose survivors only; the hypothermic phase in the trials was 24–28 h, not 48 h, and AHA now gives 32–37.5 °C for at least 36 h."),
    ("“Earlier initiation is linked to better outcome” (in the DocT GT line)", "Only observational data say so; prehospital cooling RCTs were negative. It is still the keyed answer when the other options are clearly wrong."),
  ],
  decode=[
    ("Physiological principle behind slow, controlled rewarming? [DocT]", "Rapid rewarming abruptly increases cerebral metabolic demand beyond oxygen delivery (45% right)."),
    ("Which statement about therapeutic hypothermia is correct? [DocT GT]", "Keyed ‘delaying initiation increases mortality’ (50% right); the others are wrong on indication, duration and shivering."),
  ],
  punch="Temperature control runs for at least 36 hours at 32–37.5 °C (or ≤37.5 °C in Europe) and ends with rewarming no faster than 0.5 °C/h, because fast rewarming raises brain oxygen demand, drops the pressure and releases potassium.",
)

L['PCA-30'] = dict(
  sub="Post-arrest care → Cooling methods → Rate and cost",
  step=4,
  intro="Step 4 compares the tools. Speed and cost go together except for cold IV fluid, which is fast and free but cannot hold a temperature (PCA-32). No question is linked; the exam asks the ranking and the exception.",
  parts=[
    ('a', "**Endovascular: 2–4 °C/h, extremely high cost.** A cooling catheter in a central vein exchanges heat directly with blood, so it is fastest and holds the target most tightly; the cost is the catheter and console."),
    ('b', "**Infused crystalloids: 2.5–3.5 °C/h, negligible cost.** Cold (4 °C) fluid cools quickly by mixing with blood, but only while it runs; the volume needed also limits it (pulmonary oedema)."),
    ('c', "**Hydrogel-coated pads: 1.5–2 °C/h, very high cost.** Adhesive pads with servo-controlled water (for example Arctic Sun) give good contact and feedback control."),
    ('d', "**Water-circulating pads: 1–1.5 °C/h, somewhat high cost.** Blankets with less skin contact cool more slowly."),
    ('e', "**Ice packs: about 1 °C/h, negligible cost.** No feedback, slow and labour-dependent. Published rates vary a lot with the study: in a head-to-head ICU comparison (Hoedemaekers 2007) devices cooled at about 1–1.5 °C/h, so learn the card’s ranking rather than the decimals."),
  ],
  mimic=[
    ("Induction vs maintenance", "Speed matters for induction, feedback for maintenance; current practice values tight maintenance far more, since no trial shows faster cooling helps."),
  ],
  traps=[
    ("“The fastest cheap method is ideal on its own”", "Cold fluid induces but cannot maintain (PCA-32), and prehospital cold fluid is not recommended."),
  ],
  decode=[
    ("[pattern] Which cooling method is both rapid and inexpensive?", "Infused cold crystalloid (2.5–3.5 °C/h), for induction only."),
  ],
  punch="Endovascular cooling is fastest and costliest; cold crystalloid is nearly as fast and free, but it can only start cooling, not maintain it.",
)

L['PCA-31'] = dict(
  sub="Post-arrest care → Cooling methods → Advantages",
  step=4,
  intro="Step 4, what each method is good for. The one linked GT question adds a method the card does not list: transnasal evaporative cooling, the only brain-selective one (79% right).",
  parts=[
    ('a', "**Endovascular: fastest cooling possible.** It also gives the tightest maintenance and controlled rewarming through feedback."),
    ('b', "**Infused crystalloids: very fast, easily accessible, works with other methods.** Any ward has cold saline, so it is the bridge until a device is attached; it does not replace one."),
    ('c', "**Hydrogel-coated pads: very easy to use; rapid cooling and rewarming.** Non-invasive, with servo control, so they suit units without endovascular catheters."),
    ('d', "**Water-circulating pads: targeted neck (cerebral) cooling possible; cheaper than invasive methods.**"),
    ('e', "**Ice packs: very inexpensive.**"),
  ],
  mimic=[
    ("Transnasal evaporative cooling vs water-circulating neck cooling", "Transnasal (RhinoChill) cools the brain through the nasopharynx, works prehospital and has few side effects, but induction is slow and it has no feedback, so it cannot hold a target; PRINCESS found no outcome benefit."),
  ],
  traps=[
    ("“Intravascular cooling is the brain-specific method”", "Intravascular cools the whole body; the brain-specific method with slow induction and no feedback is transnasal evaporative cooling."),
  ],
  decode=[
    ("Cooling method specific to the brain, few side effects, slow induction, no feedback control? [DocT GT]", "Transnasal evaporative cooling (79% right)."),
  ],
  punch="Endovascular is fastest, cold fluid is the accessible bridge, gel pads are easiest, and only transnasal evaporative cooling targets the brain, at the cost of slow induction and no feedback.",
)

L['PCA-32'] = dict(
  sub="Post-arrest care → Cooling methods → Disadvantages",
  step=4,
  intro="Step 4, where each method fails. The pattern is that the cheap methods fail at holding the temperature and the expensive ones carry device risks. The linked GT question turns on ‘no feedback control’, the same weakness as cold fluid and ice.",
  parts=[
    ('a', "**Endovascular: needs central line access; more bleeding and infection.** A large catheter in a patient who may be anticoagulated or on antiplatelets after PCI, and more catheter-related thrombosis."),
    ('b', "**Infused crystalloids: uncontrolled rewarming; cannot maintain temperature.** Once the infusion stops, temperature drifts back; in the Kim prehospital trial the large volumes also caused more pulmonary oedema and re-arrest."),
    ('c', "**Hydrogel-coated pads: skin lesions may occur.** Prolonged contact with cold pads can injure skin, especially with poor perfusion."),
    ('d', "**Water-circulating pads: labour intensive; several pads or blankets needed.**"),
    ('e', "**Ice packs: skin lesions, unreliable maintenance and rewarming, slow onset.** No feedback loop means overshoot below target and uncontrolled rewarming, both of which current guidelines try to avoid."),
  ],
  mimic=[
    ("Methods without feedback (cold fluid, ice, transnasal) vs with feedback (gel pads, endovascular)", "Only feedback-controlled devices can hold a target and rewarm at a set rate."),
  ],
  traps=[
    ("“Surface cooling devices lack feedback control”", "Modern surface devices (gel pads) do have feedback; the stem’s ‘no feedback’ points to transnasal cooling."),
  ],
  decode=[
    ("Brain-specific, few side effects, slow induction, no feedback? [DocT GT]", "Transnasal evaporative cooling."),
  ],
  punch="Cold fluid and ice are free but cannot hold a temperature, gel pads risk skin injury, and endovascular cooling needs a central line with its bleeding and infection risk.",
)

L['PCA-33'] = dict(
  sub="Post-arrest care → Conduct → Basic temperature package",
  step=3,
  intro="Step 3 at the bedside: the basic package every comatose survivor gets before any device. It is fever prevention by monitoring and paracetamol, with a clear trigger to escalate. The linked NEET 2024 recall asks where core temperature cannot be measured.",
  parts=[
    ('a', "**Entry: a post-arrest patient unable to follow verbal commands.** That is the same entry criterion as AHA 2025 and ERC–ESICM 2025; a patient who obeys commands has no brain injury to protect and needs no package."),
    ('b', "**A continuous temperature monitor: bladder or oesophageal.** Both read core temperature continuously and can drive a device. The pulmonary artery catheter is the reference core site; nasopharynx and tympanic membrane are also core sites. Axillary and skin readings are not core. A bladder probe lags when urine output is low."),
    ('c', "**Scheduled paracetamol, usually 1 g every 6 hours.** Scheduled, not as needed: the aim is to stop fever starting, not to treat it after it appears."),
    ('d', "**650 mg every 8 hours if alcoholic, cirrhotic or under 50 kg.** These groups have less glutathione reserve, so the daily dose is lowered to avoid liver injury."),
    ('e', "**Temperature above 37.8 °C escalates to the advanced package and Tier 1; below it, close monitoring for fever.** 37.8 °C is the same threshold at which TTM2 switched on a cooling device in its normothermia arm."),
  ],
  mimic=[
    ("Core sites vs peripheral sites", "Core: pulmonary artery, distal oesophagus, nasopharynx, tympanic, bladder, rectum (the last two lag). Not core: skin, axilla, and, in the exam list, femoral artery."),
  ],
  traps=[
    ("“Core temperature cannot be measured in the oesophagus or pulmonary artery”", "Both are core sites (the PA is the reference); the NEET 2024 key is femoral artery. A femoral arterial thermistor (as on PiCCO) does read blood temperature close to core, so the key follows the classic list of probe sites rather than physiology; give femoral artery on exam day."),
  ],
  decode=[
    ("Core temperature cannot be measured at: oesophagus, PA, femoral artery? [NEET 2024]", "Femoral artery."),
  ],
  punch="Every patient not following commands after ROSC gets a continuous bladder or oesophageal probe and scheduled paracetamol, and a temperature above 37.8 °C moves him up to a cooling device and the shivering ladder.",
)

L['PCA-34'] = dict(
  sub="Post-arrest care → Shivering → Advanced package and Tier 1",
  step=5,
  intro="Step 5 begins the shivering ladder. A cooling device makes the body fight back by shivering, so Tier 1 is started with the device: drugs that blunt shivering without sedating or lowering blood pressure. Three questions are linked; the DocT version was answered correctly by only 32%.",
  parts=[
    ('a', "**External adaptive cooling device (for example Arctic Sun), target 37.5 °C.** A fever-prevention target, not a hypothermic one, in line with TTM2 and ERC–ESICM 2025."),
    ('b', "**Buspirone 30 mg per tube, every 8–12 hours, scheduled.** A 5-HT1A partial agonist that lowers the shivering threshold modestly on its own and acts synergistically with meperidine, with no sedation or hypotension worth noting."),
    ('c', "**Magnesium repleted to a normal level, above 2 mg/dL or 0.8 mmol/L.** Magnesium is a vasodilator that improves skin perfusion and lowers the shivering threshold; it is also an NMDA antagonist, and low magnesium is common during cooling (PCA-38). With skin counter-warming (PCA-35) and paracetamol it is the low-harm first step."),
  ],
  table=dict(title="The shivering ladder", head=["Tier", "Main measures", "Why at this level"], rows=[["Basic + Tier 1", "paracetamol, buspirone, magnesium to normal, device at 37.5 °C", "no sedation, no hypotension"], ["Tier 2", "counter-warming, dexmedetomidine or propofol, low-dose ketamine, magnesium 3–4 mg/dL", "some sedation and hypotension"], ["Tier 3", "fentanyl boluses, then paralysis under deep sedation", "hides the examination and seizures"]]),
  mimic=[
    ("Counter-warming plus magnesium vs dexmedetomidine", "Both reduce shivering; counter-warming and magnesium come first because they neither sedate nor lower BP, dexmedetomidine is the next tier."),
  ],
  traps=[
    ("“A cold saline bolus suppresses thermogenesis”", "Cold fluid lowers core temperature further and worsens shivering."),
    ("“Single short-acting opioid dose as the initial step”", "Opioids sedate and depress breathing; they are a later tier (Tier 3 fentanyl)."),
    ("“Neuromuscular blockade with EEG as the initial step”", "Paralysis is the last resort, because it hides seizures and the neurological examination."),
    ("“Dexmedetomidine” for least hypotension and sedation (DocT GT key, 71% right)", "The key is disputed: magnesium (option D) comes before dexmedetomidine on the Columbia ladder and causes the least hypotension and sedation. If magnesium is offered for ‘least hypotension and sedation’, choose magnesium; if the stem says magnesium has already failed, choose dexmedetomidine."),
  ],
  decode=[
    ("Shivering during TH: initial intervention that spares the neurological examination and haemodynamics? [DocT]", "Skin counter-warming plus magnesium (32% right)."),
    ("Moderate shivering despite passive rewarming; least hypotension and excess sedation? [DocT GT]", "Keyed dexmedetomidine; magnesium is equally defensible."),
    ("Same initial-intervention stem [DocT GT6]", "Counter-warming plus magnesium (47% right)."),
  ],
  punch="Shivering is treated first with drugs that neither sedate nor drop the pressure (paracetamol, buspirone, magnesium and skin counter-warming), while a feedback device holds 37.5 °C.",
)

L['PCA-35'] = dict(
  sub="Post-arrest care → Shivering → Tier 2",
  step=5,
  intro="Step 5, the middle rung. When Tier 1 fails, counter-warming is added and sedatives with anti-shivering action come in, at the cost of some sedation and hypotension. Four questions are linked, all versions of ‘what comes first’.",
  parts=[
    ('a', "**Entry: shivering despite Tier 1.** The order matters because each step adds harm; Bedside Shivering Assessment Scale 2 (shivering of the arms or upper body) is the usual point to add sedation."),
    ('b', "**Warming the hands and feet: it tricks the body into feeling warm.** The hypothalamus sets shivering from a weighted mix of core and skin temperature, and skin contributes about a fifth; warming the skin lowers the shivering threshold without changing core temperature much. It is cheap and harmless, which is why DocT keys it with magnesium as the first step."),
    ('c', "**Dexmedetomidine and/or propofol infusions.** Dexmedetomidine (alpha-2 agonist) lowers the shivering threshold with light sedation, at the price of bradycardia and hypotension; propofol sedates more deeply and lowers BP more."),
    ('d', "**Ketamine 0.2–0.3 mg/kg/h (low, analgesic dose).** NMDA antagonism reduces shivering; at this dose it supports the blood pressure rather than lowering it."),
    ('e', "**Magnesium to a slightly raised level, about 3–4 mg/dL (1.2–1.6 mmol/L).** The Columbia protocol targets this range from the start; the card’s source reserves it for Tier 2. Either way, magnesium is given before the sedatives."),
    ('f', "**Ondansetron 4 mg IV every 8 hours may be considered.** A 5-HT3 antagonist with a modest anti-shivering effect."),
  ],
  mimic=[
    ("Counter-warming vs active rewarming", "Counter-warming heats the skin to stop shivering while the device holds the core temperature; it is not rewarming the patient."),
  ],
  traps=[
    ("“Dexmedetomidine” when magnesium is offered for ‘least hypotension and sedation’", "DocT GT keys dexmedetomidine (71–73% right), but magnesium is lower on the ladder and has less hypotension and sedation; choose magnesium if it is offered and has not been tried."),
    ("“Midazolam infusion” or “ketamine bolus” for shivering", "Midazolam sedates without much anti-shivering effect and accumulates when cold (PCA-36); ketamine is a low-dose infusion, not a bolus."),
    ("“Cold saline” or “paralysis first”", "Cold saline worsens shivering; paralysis is Tier 3."),
  ],
  decode=[
    ("Initial intervention for shivering sparing neurology and haemodynamics? [DocT]", "Skin counter-warming plus magnesium (32% right)."),
    ("Moderate shivering despite passive rewarming; least hypotension and sedation? [DocT GT3/GT4]", "Keyed dexmedetomidine; magnesium equally defensible."),
    ("Initial intervention [DocT GT6]", "Counter-warming plus magnesium (47% right)."),
  ],
  punch="Counter-warming and magnesium come before any sedative because they reduce shivering without sedation or hypotension; dexmedetomidine, propofol and low-dose ketamine are the next rung.",
)

L['PCA-36'] = dict(
  sub="Post-arrest care → Shivering → Tier 3 and paralysis",
  step=5,
  intro="Step 5’s top rung. Opioid boluses, then paralysis under deep sedation and analgesia, are kept last because they remove the examination you need for prognosis. Four questions are linked, including the drug-metabolism question on what cooling does to the sedatives.",
  parts=[
    ('a', "**Entry: shivering despite Tier 2.** On the Bedside Shivering Assessment Scale, 3 (shivering of the trunk and all limbs) is the usual trigger for neuromuscular blockade."),
    ('b', "**Fentanyl boluses as needed, safer than meperidine (pethidine).** Meperidine is the strongest anti-shivering opioid (it lowers the shivering threshold about twice as much as the vasoconstriction threshold, an effect attributed partly to kappa-opioid and alpha-2 actions), but its metabolite normeperidine lowers the seizure threshold and accumulates in renal failure, and it has serotonergic interactions; in a post-arrest brain prone to seizures that is a poor trade."),
    ('c', "**Paralysis is the last resort.** It abolishes shivering completely, but it also hides seizures and myoclonus and removes the neurological examination."),
    ('d', "**Before cisatracurium: a propofol or midazolam infusion to RASS −5 and a fentanyl infusion.** A paralysed patient cannot show distress, so deep sedation and analgesia must be running first; continuous EEG is advised because seizures become invisible. Cisatracurium is chosen because Hofmann elimination does not depend on the liver or CYP enzymes."),
  ],
  mimic=[
    ("Midazolam and fentanyl vs atracurium/cisatracurium and hydromorphone during cooling", "Cooling slows CYP450 metabolism by about 7–22% per °C below 37, so midazolam (CYP3A4) and fentanyl accumulate and prolong sedation; atracurium and cisatracurium (Hofmann elimination, ester hydrolysis) and hydromorphone (glucuronidation) do not depend on CYP, although Hofmann elimination itself slows a little in the cold."),
  ],
  traps=[
    ("“Cooling slows CYP450 metabolism of atracurium”", "Atracurium is cleared by Hofmann elimination, not CYP; the concern is midazolam (75% right)."),
    ("“Raise the target to 36 °C” or “large fluid bolus” for refractory shivering", "The next step after counter-warming and magnesium have failed is escalation up the ladder, with NMB and EEG at the top (72% right)."),
    ("“Hofmann elimination slows hydromorphone or midazolam”", "Neither drug is cleared by Hofmann elimination."),
  ],
  decode=[
    ("Persistent shivering despite counter-warming and magnesium — next step? [DocT]", "Neuromuscular blockade with continuous EEG (72% right)."),
    ("Midazolam, hydromorphone and atracurium during TH — concern? [DocT GT]", "Reduced CYP450 metabolism of midazolam, prolonged sedation (75% right)."),
    ("Shivering of the trunk and all limbs (BSAS 3) — next step? [Marrow]", "Neuromuscular blockade, under deep sedation."),
  ],
  punch="Paralysis is the last rung because it hides seizures and the examination, so it is given only on top of deep sedation, analgesia and EEG; cooling also slows CYP450, so midazolam and fentanyl linger and confuse prognosis.",
)

L['PCA-37'] = dict(
  sub="Post-arrest care → Complications → Cardiovascular, coagulation, immune",
  step=6,
  intro="Step 6 is the price of cooling. No question is linked; the exam asks which complications belong to cooling, and the classic one, bradycardia, is not on this card’s list.",
  parts=[
    ('a', "**Cardiovascular: myocardial ischaemia, hypertension, tachycardia, deep vein thrombosis.** Tachycardia and hypertension belong to the induction phase and to shivering, when catecholamines and vasoconstriction rise. Once at 33 °C the usual finding is sinus bradycardia, with a longer PR and QT and sometimes Osborn (J) waves; TTM2 showed more haemodynamically significant arrhythmia at 33 °C (PCA-26)."),
    ('b', "**Coagulation: platelet activation, coagulopathy.** Cold slows the clotting enzymes and impairs platelet function, so bleeding increases slightly, which matters after PCI or thrombolysis; standard coagulation tests are run at 37 °C and underestimate it."),
    ('c', "**Immune: more infection of surgical wounds.** That finding comes from perioperative hypothermia; after cardiac arrest the infection that rises with cooling is mainly pneumonia, because cooling impairs neutrophil function and cytokine release."),
  ],
  mimic=[
    ("Induction-phase vs maintenance-phase heart rate", "Induction and shivering: tachycardia, hypertension. Maintenance at 33 °C: bradycardia, which is usually left untreated if perfusion is adequate."),
  ],
  traps=[
    ("“Hypothermia causes tachycardia” as the maintenance finding", "Steady mild hypothermia causes bradycardia; tachycardia comes from induction and shivering."),
  ],
  decode=[
    ("[pattern] Which is a recognised complication of TTM?", "Arrhythmia (bradycardia), bleeding tendency, infection (pneumonia), electrolyte shifts."),
  ],
  punch="Cooling causes bradycardia and arrhythmia (tachycardia and hypertension during induction and shivering), a mild bleeding tendency and more infection, mainly pneumonia.",
)

L['PCA-38'] = dict(
  sub="Post-arrest care → Complications → Electrolytes",
  step=6,
  intro="Step 6, the electrolyte shifts. Cooling drives three ions into cells and raises urine output (cold diuresis), so all three fall; at rewarming they come back out. No question is linked.",
  parts=[
    ('a', "**Hypokalaemia.** Cooling moves potassium into cells (via the Na-K ATPase and beta stimulation) and cold diuresis loses some in the urine. At rewarming it moves back out, so replacing aggressively during cooling risks rebound hyperkalaemia; most units replace only to the low-normal range."),
    ('b', "**Hypomagnesaemia.** Losses through cold diuresis and intracellular shift; low magnesium worsens arrhythmia and shivering, which is why magnesium is part of the shivering ladder (PCA-34, PCA-35)."),
    ('c', "**Hypophosphataemia.** Shift into cells and renal loss; it can weaken respiratory muscles and the myocardium."),
  ],
  mimic=[
    ("Cooling vs rewarming", "Cooling: K, Mg, PO₄ fall. Rewarming: potassium rises as it leaves cells, so rewarm slowly (PCA-29)."),
  ],
  traps=[
    ("“Hyperkalaemia during the cooling phase”", "During cooling potassium falls; hyperkalaemia belongs to rewarming and to shivering (PCA-40)."),
  ],
  decode=[
    ("[pattern] Electrolyte disturbances during TTM", "Low potassium, magnesium and phosphate; rebound hyperkalaemia at rewarming."),
  ],
  punch="Cooling pushes potassium, magnesium and phosphate into cells and out in the urine, so all three fall, and potassium returns at rewarming, which is why it is replaced cautiously and rewarming is slow.",
)

L['PCA-39'] = dict(
  sub="Post-arrest care → Complications → Endocrine and metabolic",
  step=6,
  intro="Step 6, the hormones. Cooling lowers insulin secretion and raises insulin resistance, so glucose rises, and the reverse at rewarming lets it fall. No question is linked.",
  parts=[
    ('a', "**Steroids fall.**"),
    ('b', "**Insulin secretion falls.** Pancreatic beta cells secrete less insulin in the cold."),
    ('c', "**Peripheral resistance to insulin rises.** Together with part b this drives hyperglycaemia during cooling, and insulin requirements rise."),
    ('d', "**TSH and thyroxine rise.** A thermogenic stress response to the cold."),
    ('e', "**Hyperglycaemia.** The usual problem during induction and maintenance."),
    ('f', "**Hypoglycaemia.** At rewarming, insulin sensitivity returns quickly; an infusion set for the cold phase can then drop glucose sharply, so insulin is reduced and glucose checked more often during rewarming (PCA-20)."),
  ],
  mimic=[
    ("Cooling vs rewarming glucose", "Cooling: high glucose, high insulin need. Rewarming: falling need, risk of hypoglycaemia."),
  ],
  traps=[
    ("“Hypothermia causes only hyperglycaemia”", "Hypoglycaemia occurs too, at rewarming, when insulin sensitivity recovers."),
  ],
  decode=[
    ("[pattern] Metabolic effect of TTM on glucose", "Hyperglycaemia from less insulin and more resistance; hypoglycaemia risk at rewarming."),
  ],
  punch="Cooling reduces insulin secretion and raises insulin resistance, so glucose rises, and rewarming reverses both, so the same insulin dose can then cause hypoglycaemia.",
)

L['PCA-40'] = dict(
  sub="Post-arrest care → Shivering → Consequences of shivering",
  step=5,
  intro="Step 5’s reason. Shivering is the body’s defence of its set-point, and it undoes the point of cooling by raising the very demands cooling is meant to lower. No question is linked, but this is why the ladder in PCA-34 to PCA-36 exists.",
  parts=[
    ('a', "**Lactic acidosis.** Shivering muscle can raise oxygen use beyond supply in a patient with a recovering heart, so anaerobic metabolism produces lactate."),
    ('b', "**Raised oxygen consumption.** Whole-body oxygen use can more than double, and the brain’s metabolic demand rises with arousal, opposing the reduction in PCA-21."),
    ('c', "**Raised ICP.** Muscle activity, raised intrathoracic pressure and higher cerebral metabolism with blood flow all raise ICP."),
    ('d', "**Hyperkalaemia.** Working muscle releases potassium, the opposite of the fall seen with cooling itself (PCA-38)."),
  ],
  mimic=[
    ("Shivering vs seizures or myoclonus", "Shivering is rhythmic, synchronous and settles with counter-warming or sedation; seizures need EEG to exclude, especially once paralysis is considered."),
  ],
  traps=[
    ("“Shivering is a desired effect during cooling”", "It is harmful and is actively suppressed (DocT option C in PCA-28/29)."),
  ],
  decode=[
    ("[pattern] Why must shivering be controlled during TTM?", "It raises oxygen consumption, lactate, ICP and potassium, cancelling the benefit of cooling."),
  ],
  punch="Shivering raises oxygen consumption, lactate, ICP and potassium, the opposite of what cooling is meant to do, so it is treated as a complication, not a sign that cooling is working.",
)

FLAGS = {}
FLAGS['PCA-23'] = "Source of the card’s percentages could not be traced; they are not the HACA (favourable outcome 55 vs 39%, death 41 vs 55%) or Bernard (49 vs 26%) figures, and are probably from observational cohorts. Explanation restates them and gives the RCT figures."
FLAGS['PCA-25'] = "Card heads the ratio column ‘HR’; in Nielsen 2013 the CPC and mRS ratios are risk ratios (only end-of-trial death is a hazard ratio). Figures themselves match."
FLAGS['PCA-26'] = "Card correct (watch line already notes the source’s wrong year). For precision: 1900 randomised, 1861 analysed, 1850 with primary outcome; hypothermia was 33 °C for 28 h then ~1/3 °C/h rewarming."
FLAGS['PCA-27'] = "Card b gives p = 0.02; the Zeiner abstract gives P = .002 (and the results table puts the favourable-group minimum at 36.0 °C, P = .001). Other figures match."
FLAGS['PCA-28'] = "Card row ‘ERC/ESICM 2021’ is right on constant 32–36 °C for ≥24 h and no fever for ≥72 h (Nolan 2021), but ‘TTM at 36 °C’ is not the guideline’s wording (it gave 32–36 °C); the fever-prevention-only position came in the 2022 ERC–ESICM update after TTM2. DocT QBank key 32–34 °C is the 2002–2010 answer; DocT key ‘delaying initiation increases mortality’ is not supported by RCTs (least-wrong option)."
FLAGS['PCA-29'] = "Card agrees with AHA 2025 and ERC–ESICM 2025. The DocT GT card-layer line says ‘current ERC–ESICM practice is fever prevention ≤37.5–37.7 °C for at least 72 h’ (that is 2021; 2025 says ≤37.5 °C for 36–72 h) and that ‘earlier initiation is linked to better outcome’ (observational only; RCTs of early prehospital cooling were negative)."
FLAGS['PCA-34'] = "DocT GT3/GT4 key ‘dexmedetomidine’ for least hypotension and sedation is disputed: magnesium (offered as option D) comes earlier on the Columbia ladder and causes less of both."
FLAGS['PCA-35'] = "Card puts the 3–4 mg/dL magnesium target at Tier 2 (IBCC); the Columbia protocol targets 3–4 mg/dL from the baseline tier. Not wrong, a source difference."
FLAGS['PCA-30'] = "Rates are from the card’s source table; measured ICU rates (Hoedemaekers 2007) are lower (devices about 1–1.5 °C/h, cold fluid plus ice ~0.3 °C/h). Ranking and the crystalloid exception are the examinable points."
FLAGS['PCA-37'] = "List is incomplete as a guide to the maintenance phase: steady mild hypothermia causes bradycardia (tachycardia and hypertension belong to induction and shivering), and the infection that rises after arrest is mainly pneumonia; the surgical-wound finding comes from perioperative hypothermia data."
