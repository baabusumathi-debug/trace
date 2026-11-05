# TOX01 — Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Audited 6 Nov against qpack/TOX01.md (124 linked questions): decode items rewritten from the real stems, traps from real distractors.
# Fields per card:
#   sub    breadcrumb: System → topic → subtopic
#   intro  "What's going on": 2–4 plain sentences that set the scene before any fact
#   parts  [(letter, text)] mirroring the card's own letters; text = **restated answer** + the why (1–4 sentences)
#   table  optional dict(title, head, rows) — only for decisions, steps or comparisons
#   mimic  [(pair, discriminator)] close look-alikes
#   traps  [(wrong belief, correction with its why)]
#   decode [(how the stem is worded [source], what it points to)]
#   punch  the punchline — last, one or two sentences, only after the build-up
#   extra  optional exam add-ons [dict(q, a)] shown from the second sight (kept from the pilot)
#   before optional bridge text for Any-hit flows when the previous card was skipped (full sentences)
L = {}

L['TOX-01'] = dict(
  sub="Toxicology → First steps → Coma of unknown cause",
  intro="A patient arrives unconscious and nobody knows why. A few causes of coma are dangerous yet reversed by a cheap drug: low glucose and opioid respiratory depression injure the brain within minutes, and thiamine deficiency in the malnourished or alcohol-dependent causes Wernicke’s encephalopathy. The coma cocktail treats these first, before the cause is known — so every drug in it must be harmless if the guess turns out to be wrong.",
  parts=[
    ('a', "**Empirical treatment for coma of unknown cause.** Empirical means given on suspicion, before a diagnosis. It is justified only when the condition is common, dangerous and quickly reversible, and when the drug does no harm to the patients who turn out not to have it."),
    ('b', "**Dextrose 50 mL of 50%, thiamine 100 mg IV, naloxone up to 2 mg.** The brain has no glucose store, so hypoglycaemia injures neurons within minutes — check a capillary glucose and treat. Thiamine is cheap protection against Wernicke’s in the alcohol-dependent or malnourished. Naloxone displaces opioids from the μ receptor and restores breathing within minutes; pinpoint pupils with slow breathing in a patient on opioids make it the immediate step, given in small steps (from 0.04 mg) if he may be dependent, to avoid violent withdrawal."),
    ('c', "**Yes — glucose goes first if it is needed.** There is no good evidence that a single glucose dose precipitates Wernicke’s, whereas untreated neuroglycopenia causes certain brain injury. So glucose is never delayed for thiamine; thiamine is given alongside."),
    ('d', "**Flumazenil.** It is a benzodiazepine antagonist but fails the safe-if-wrong test. In benzodiazepine dependence it precipitates withdrawal seizures; in a patient with epilepsy it removes the drug that was controlling seizures; and in a mixed overdose with a pro-convulsant — a tricyclic is the classic — the benzodiazepine was holding the seizures back. Those seizures are then hard to treat, because the first-line drug is now blocked. So a suspected tricyclic co-ingestion, a seizure disorder or dependence is enough to withhold it, whatever the ECG shows. Its only safe use is reversing iatrogenic over-sedation in a benzodiazepine-naïve patient; its short half-life (about 1 hour) means re-sedation, which is a nuisance rather than the danger."),
  ],
  mimic=[
    ("Naloxone vs flumazenil", "Both are competitive antagonists. Opioid apnoea kills and naloxone reverses it safely; benzodiazepines alone rarely stop breathing, so flumazenil adds seizure risk for little gain."),
  ],
  traps=[
    ("“Thiamine must always be given before glucose”", "Glucose is never delayed; there is no good evidence a single dose precipitates Wernicke’s."),
    ("“Benzodiazepine plus amitriptyline: give flumazenil once the ECG is normal, or with naloxone”", "Withhold it: the tricyclic co-ingestion (and any seizure disorder) is the contraindication; removing the benzodiazepine unmasks seizures. Only 46% chose this on DocT GT."),
    ("“Rebound sedation is the main worry before flumazenil”", "Re-sedation is a nuisance; the danger that should most concern you is a tricyclic co-ingestion and seizures."),
    ("“100 mL of 50% dextrose”", "The usual dose is 50 mL of 50% (25 g); one page of your notes prints 100 mL."),
  ],
  decode=[
    ("Elderly man on increasing opioid doses, pinpoint pupils, drowsy — immediate step? [DocT]", "Naloxone."),
    ("Known seizure disorder, suspected benzodiazepine and amitriptyline overdose — next step? [DocT GT]", "Withhold flumazenil because of seizure risk."),
    ("Naloxone failed, flumazenil considered — what should most concern you? [DocT GT]", "A tricyclic co-ingestion — not rebound sedation, ICP or EEG access."),
    ("Benzodiazepine overdose: which drug reverses respiratory depression? (the ‘trial’ named does not exist) [DocT]", "Flumazenil — but not given routinely in overdose."),
  ],
  punch="An empirical antidote must be safe even when the guess is wrong: dextrose, thiamine and naloxone pass that test; flumazenil fails it, because it unmasks seizures.",
)

L['TOX-02'] = dict(
  sub="Toxicology → First steps → Initial work-up",
  intro="In an overdose the history is the least reliable part of the assessment: patients misreport the drug, the dose and the time, and adults commonly take several substances at once (often alcohol with a benzodiazepine or paracetamol). So, after the airway, breathing and circulation are secured, the examination and a few bedside tests become the history. Two poisons are checked in everyone, because they look harmless early and are treatable only if found in time.",
  parts=[
    ('a', "**Mental status, pupils, skin temperature and moisture, SpO₂, ECG, capillary glucose; expose the patient.** Pupils and skin sort the patient into a toxidrome (TOX-03, 04). The ECG picks up drugs that block cardiac channels — a wide QRS or a long QT changes treatment at once. A capillary glucose excludes the commonest reversible cause of coma. Exposing the patient finds patches, needle marks and pill packets."),
    ('b', "**Opioids, benzodiazepines, cannabinoids, amphetamines, phencyclidine, cocaine.** A urine immunoassay looks for a fixed panel of drug classes, mostly as metabolites. It is qualitative — present or absent — so it answers ‘was a drug from this panel taken recently?’, not ‘what is making this patient ill now?’, and it cannot be repeated to follow a drug level."),
    ('c', "**False negatives below the threshold, false positives with chronic use, and cross-reactivity — so always correlate clinically.** Drugs outside the panel (synthetic cathinones, synthetic cannabinoids, many prescription drugs) are not detected. Metabolites linger, so a chronic cannabis user tests positive for weeks. Unrelated drugs can trigger the antibody. Reading the result therefore needs knowing which drugs that panel covers, and a positive may need confirmation by a specific method (gas chromatography–mass spectrometry)."),
    ('d', "**Paracetamol and salicylate.** Paracetamol gives almost no symptoms for the first day while liver injury develops, and N-acetylcysteine works best when started early. Salicylate shows only subtle early signs (tinnitus, fast breathing) before acidosis and collapse. Both are common, often co-ingested and treatable only if measured — so a level is sent in every overdose, whatever the history says."),
  ],
  mimic=[
    ("Urine drug screen vs serum drug level", "The urine screen is qualitative (present or absent, possibly days old). A serum level is quantitative and guides treatment — paracetamol, salicylate, lithium, digoxin, iron."),
  ],
  traps=[
    ("“The reported drug and time of ingestion can be trusted”", "Agent, dose and time are often wrong; treat the time as unknown when in doubt and assume more than one substance."),
    ("“A positive screen confirms the toxicity and guides treatment”", "It may reflect use days ago and may be a cross-reaction; it needs clinical correlation and sometimes confirmatory testing."),
    ("“A negative drug screen excludes drug toxicity”", "Designer drugs and many prescription drugs are not on the panel; a negative screen means only ‘nothing from the panel above the threshold’."),
    ("“The patient denies paracetamol, so no level is needed”", "Early paracetamol toxicity is silent; the level is sent in every overdose."),
  ],
  decode=[
    ("Most accurate statement about the history in overdose [DocT]", "Multiple substances are commonly involved in adult overdoses."),
    ("Most accurate statement about urine toxicology screens [NEET 2025]", "Interpretation needs knowledge of the toxins screened and may need confirmatory testing."),
  ],
  punch="In overdose the examination is the history, the urine screen only hints, and paracetamol and salicylate are measured in everyone because they are silent early and treatable in time.",
)

L['TOX-03'] = dict(
  sub="Toxicology → Toxidromes → Sympathomimetic vs anticholinergic",
  intro="Both of these patients arrive hot, fast and agitated with big pupils, so the obvious signs cannot separate them. The difference lies in one odd piece of physiology: sweat glands are supplied by sympathetic nerves, but those nerves release acetylcholine onto muscarinic receptors. That single fact decides the skin — and the skin decides the toxidrome.",
  parts=[
    ('a', "**Skin: sympathomimetic wet; anticholinergic dry and flushed.** A sympathomimetic raises central sympathetic outflow, and that outflow includes the cholinergic sweat fibres, so the patient sweats. An anticholinergic blocks the muscarinic receptor on the sweat gland, so the skin is dry — and the flushing comes from skin vessels dilating to lose the heat he can no longer sweat away. Serotonin syndrome and neuroleptic malignant syndrome also sweat, so dry skin is the one finding that marks the anticholinergic patient out from all three; fever, delirium and mydriasis are shared."),
    ('b', "**Pupils: dilated in both.** Sympathetic stimulation contracts the dilator muscle; muscarinic block paralyses the constrictor. Two routes lead to the same big pupil, which is why the pupils cannot separate them."),
    ('c', "**Bowel and bladder: normal in sympathomimetic; reduced bowel sounds and urinary retention in anticholinergic.** Gut movement and bladder emptying run on muscarinic receptors, so muscarinic block silences the bowel and retains urine — a suprapubic mass in a stem is a full bladder."),
    ('d', "**Delirium: sympathomimetic agitated and possibly violent; anticholinergic picking at the air with mumbling speech.** The sympathomimetic patient is wired and aggressive. The anticholinergic patient is confused, hallucinating and plucking at invisible objects."),
    ('e', "**Agents: sympathomimetic — amphetamines, cocaine, cathinones, pseudoephedrine; anticholinergic — atropine, antihistamines (diphenhydramine), tricyclics, datura, phenothiazines.** Amphetamines act indirectly: they reverse the transporter and release dopamine and noradrenaline from nerve terminals, rather than stimulating the receptors themselves; cocaine blocks reuptake. Synthetic cathinones escape the routine urine screen (TX1-S1). Tricyclics are anticholinergic as well as sodium-channel blockers, so a dry, dilated, hypotensive patient with a wide QRS points to a tricyclic (TOX-07)."),
  ],
  table=dict(title="Telling them apart at the bedside", head=["", "Sympathomimetic", "Anticholinergic"], rows=[["Temperature, HR, pupils", "↑ ↑ dilated", "↑ ↑ dilated"], ["Skin", "**wet**", "**dry, flushed**"], ["Bowel sounds, bladder", "normal", "reduced, retention"], ["Delirium", "agitated, violent", "picking at air, mumbling"]]),
  mimic=[
    ("Serotonin syndrome", "Also wet with dilated pupils — but adds tremor, hyperreflexia and clonus (TOX-05)."),
    ("Withdrawal (alcohol, sedatives, opioids)", "Also wet, fast and dilated; the history separates it. Opioids themselves give the opposite picture — small pupils and sedation — so they are the agent least likely to cause a sympathomimetic picture."),
  ],
  traps=[
    ("“Fever, delirium or mydriasis marks the anticholinergic patient”", "All are shared with sympathomimetic, serotonin and NMS pictures; only dry skin separates it (51% on DocT)."),
    ("“Sweating, agitation and big pupils — anticholinergic, from cocaine”", "Sweating makes it sympathomimetic; cocaine is a sympathomimetic, and an opioid is the agent least likely (49% on DocT)."),
    ("“Florid sympathomimetic picture, screen negative — ecstasy or amphetamine”", "The standard screen detects amphetamines; a negative screen with this picture points to synthetic cathinones (16% on DocT GT)."),
    ("“Amphetamines stimulate α-receptors directly”", "They are indirect: they release stored dopamine and noradrenaline (0% on DocT GT)."),
  ],
  decode=[
    ("Which antimuscarinic finding distinguishes it from sympathomimetic, serotonin and NMS? [DocT]", "Dry skin."),
    ("Tachycardia, fever, mydriasis, dry skin, ileus, hypotension, wide QRS and long QT [DocT]", "Amitriptyline (not diphenhydramine, dextroamphetamine or fluoxetine)."),
    ("Student, floridly hallucinating, BP 190/110, HR 129, standard screen negative [DocT GT]", "Synthetic cathinone."),
    ("‘Party drug’, sympathomimetic toxidrome — mechanism? [DocT GT]", "Increased synaptic dopamine release."),
  ],
  punch="Both run hot, fast and dilated; only the sympathomimetic can still sweat, because sweat glands work through muscarinic receptors — so the skin decides.",
)

L['TOX-04'] = dict(
  sub="Toxicology → Toxidromes → Opioid, sedative-hypnotic, cholinergic",
  intro="Three toxidromes give a sleepy or comatose patient, and two of them share small pupils. The first decision is the pupil; the second is the breathing and the secretions. Getting it right matters because each has a different antidote — naloxone for the opioid, atropine and pralidoxime for the organophosphate, and none for most sedatives.",
  parts=[
    ('a', "**Pupils: opioid pinpoint; sedative variable; cholinergic constricted.** Opioids remove inhibition of the parasympathetic (Edinger–Westphal) nucleus, so the pupil constricts — small but still reactive. Cholinergic poisons stimulate the muscarinic constrictor directly. Sedative-hypnotics have no consistent effect on the pupil."),
    ('b', "**Breathing: opioid slow, with apnoea; sedative slow or normal; cholinergic slow or fast.** Opioids depress the brainstem respiratory centre, so the rate falls first — a rate of 6–8 with small pupils, bradycardia and low blood pressure is an opioid (codeine derivatives such as dihydrocodeine included). Respiratory depression is still the main sign of sedative-hypnotic overdose, but benzodiazepines alone rarely cause apnoea; barbiturates and combinations with alcohol or opioids do. In cholinergic poisoning breathing fails from the airway (bronchorrhoea, bronchospasm) and the muscles (nicotinic weakness)."),
    ('c', "**Skin: opioid variable; sedative variable; cholinergic wet.** Muscarinic stimulation turns on every secretion — sweat, saliva, tears and bronchial fluid — so the organophosphate patient is wet everywhere. Because he sweats freely he is not hyperthermic; fever is the feature least expected in a cholinergic crisis."),
    ('d', "**Extras: opioid — needle marks, pulmonary oedema; sedative — nystagmus; cholinergic — salivation, bronchorrhoea, fasciculation, diarrhoea.** Fasciculation is the nicotinic effect at the neuromuscular junction and is followed by weakness. An elderly patient found in the garden with small pupils, bradycardia and froth at the mouth is organophosphate poisoning."),
  ],
  table=dict(title="Coma with small pupils", head=["Finding", "Points to", "Treat with"], rows=[["Pinpoint + wet, bronchorrhoea, fasciculation", "**Organophosphate**", "atropine + pralidoxime"], ["Pinpoint + dry + very slow breathing", "**Opioid**", "naloxone"], ["Pinpoint, slow, no response to naloxone, bradycardia", "Clonidine", "supportive"]]),
  mimic=[
    ("Opioid vs clonidine", "Clonidine (a central α₂ agonist) copies opioid coma with miosis, bradycardia and hypotension, but naloxone reverses it inconsistently (TX1-S2)."),
    ("Opioid vs pontine haemorrhage", "Pinpoint pupils and coma with no response to naloxone — think of a structural cause."),
  ],
  traps=[
    ("“Coma, small pupils, RR 8, low tone — diazepam”", "Benzodiazepines do not give small pupils with that degree of hypoventilation; it is an opioid such as dihydrocodeine (50% on DocT)."),
    ("“Organophosphate poisoning causes hyperthermia”", "The patient sweats; bronchorrhoea, fasciculation and diarrhoea are expected, fever is not (58% on DocT)."),
    ("“Sedative-hypnotic overdose does not depress breathing”", "Respiratory depression is its common sign; apnoea needs a barbiturate or a combination."),
    ("“Pinpoint pupils, no response to naloxone — benzodiazepine”", "Benzodiazepines do not give pinpoint pupils; think clonidine, a mixed ingestion or a pontine bleed."),
  ],
  decode=[
    ("GCS 6, RR 8, HR 52, BP 84/62, small reactive pupils, flexor plantars [DocT]", "Dihydrocodeine (opioid), not diazepam."),
    ("Pesticide worker, fasciculation, pinpoint pupils, wet — least expected feature? [DocT]", "Hyperthermia."),
    ("Coma, pinpoint pupils, hypoventilation, no response to naloxone [DocT GT]", "Clonidine toxicity."),
    ("Common sign of sedative-hypnotic overdose [NEET 2025]", "Respiratory depression."),
  ],
  punch="Pinpoint pupils narrow it to opioid or cholinergic, and the secretions decide: the opioid patient is dry with slow breathing, the organophosphate patient drowns in his own secretions.",
)

L['TOX-05'] = dict(
  sub="Toxicology → Toxidromes → Serotonin syndrome and hallucinogens",
  intro="Serotonin syndrome is a drug interaction more often than an overdose: a patient on one serotonergic drug is given a second — a cough medicine, an opioid, linezolid — and within hours becomes agitated, sweaty and tremulous. It is diagnosed at the bedside, and the finding that defines it is in the reflexes. Hallucinogens, by contrast, change perception more than the body.",
  parts=[
    ('a', "**Tremor, hyperreflexia, clonus (worse in the legs), ocular clonus, diarrhoea, wet flushed skin, dilated pupils.** Excess serotonin over-stimulates 5-HT₁A and especially 5-HT₂A receptors in the brainstem and cord, producing neuromuscular excitation — tremor, then brisk reflexes, then inducible or spontaneous clonus and myoclonus. The same excess drives sweating, diarrhoea, tachycardia and mydriasis, and rising muscle activity generates heat. Fever with myoclonus or hyperreflexia separates it from opioid withdrawal (no fever, normal reflexes) and from NMS (rigid, slow reflexes, after a dopamine antagonist)."),
    ('b', "**MAOIs, SSRIs and SNRIs, tricyclics, dextromethorphan, meperidine (pethidine), tramadol, linezolid.** These raise synaptic serotonin by less breakdown (MAOIs; linezolid is a weak MAOI) or less reuptake (the rest). An antidepressant plus an over-the-counter cold remedy (dextromethorphan) is a classic stem, as is a tricyclic such as amoxapine plus tramadol. An SSRI overdose on its own is usually benign: sinus tachycardia around 110, drowsiness, tremor and big pupils, with no wide QRS."),
    ('c', "**Hallucinogenic toxidrome: perceptual distortion, synaesthesia, depersonalisation; nystagmus with phencyclidine and ketamine. Agents: LSD, psilocybin, mescaline, MDMA.** These drugs alter perception with only mild sympathetic signs; phencyclidine and ketamine are dissociative NMDA antagonists, hence the nystagmus."),
  ],
  mimic=[
    ("Serotonin syndrome vs neuroleptic malignant syndrome", "Serotonin: hours after the drug, clonus and brisk reflexes. NMS: days to develop, lead-pipe rigidity, slow reflexes, after a dopamine antagonist."),
    ("Serotonin syndrome vs anticholinergic", "Both are hot with dilated pupils, but the anticholinergic patient is dry with no clonus."),
  ],
  traps=[
    ("“Fluoxetine overdose: pinpoint pupils, RR 6 or QRS 140 ms”", "SSRI overdose gives sinus tachycardia (~110); pinpoint pupils and RR 6 are an opioid, QRS 140 a tricyclic (or venlafaxine, bupropion). Only 33% on DocT. Citalopram and escitalopram are the exception — long QTc and seizures."),
    ("“On antidepressants with fever, tremor, myoclonus and sweating — NMS or anticholinergic”", "Sweating and myoclonus without a neuroleptic make it serotonin syndrome; the cold remedy was the second drug (57% on DocT)."),
    ("“IV drug user, febrile, sweaty, hyperreflexic — opioid withdrawal”", "Withdrawal has no fever, hyperreflexia or myoclonus; this is serotonin syndrome (57% on DocT)."),
    ("“Datura (belladonna) is serotonergic”", "It is anticholinergic: dry skin and no clonus."),
  ],
  decode=[
    ("Takes antidepressants, recent URTI, T 39.2 °C, HR 135, tremor, myoclonus, diaphoresis [DocT]", "Serotonin syndrome."),
    ("IV drug user, febrile, diaphoretic, mydriatic, hyperreflexia and myoclonus [DocT]", "Serotonin syndrome, not opioid withdrawal."),
    ("Which is a feature of fluoxetine overdose? [DocT]", "Heart rate 110."),
    ("Serotonin syndrome is NOT associated with [Marrow]", "Belladonna alkaloids."),
  ],
  punch="Serotonin excess shows in the reflexes — tremor, hyperreflexia and clonus, legs more than arms, on a wet, hot, dilated patient — and no clonus means think again.",
  extra=[dict(q="Serotonergic agents beyond the card’s list?", a="**Trazodone, cocaine, amphetamines, MDMA**, and opioids — **pethidine, tramadol, fentanyl**.")],
)

L['TOX-06'] = dict(
  sub="Toxicology → Bedside clues → Odours",
  intro="Some poisons can be smelled on the breath, the skin or the vomit before any test is back. An odour is only a clue — many people cannot smell cyanide at all — but in an exam it is often the one word in the stem that names the poison.",
  parts=[
    ('a', "**Bitter almonds — cyanide.** Hydrogen cyanide has this smell; many people cannot detect it, so its absence excludes nothing. The source can be iatrogenic: sodium nitroprusside releases cyanide, so confusion, tachycardia, lactic acidosis and almond breath during a high-dose or prolonged nitroprusside infusion mean cyanide toxicity — stop the infusion and give hydroxocobalamin."),
    ('b', "**Garlic — organophosphates, arsenic, phosphorus, thallium, selenium.** Sulphur- and phosphorus-containing compounds and some metals give a garlic smell. An organophosphate patient who is also wet with pinpoint pupils is the classic picture."),
    ('c', "**Rotten eggs — hydrogen sulphide.** Sewers, manure pits and industrial accidents. At high concentrations it paralyses the sense of smell, so the odour can vanish as the danger rises."),
    ('d', "**Freshly mown hay — phosgene.** A choking gas that injures the alveoli, with pulmonary oedema that may be delayed by hours."),
    ('e', "**Mothballs — naphthalene; wintergreen — methyl salicylate; fruity or acetone — ethanol, isopropanol, salicylates; kerosene — organophosphates (the solvent).** Isopropanol is metabolised to acetone, which gives fruity breath without acidosis (TOX-08). Oil of wintergreen is concentrated salicylate."),
  ],
  mimic=[
    ("Fruity breath: DKA vs isopropanol", "Both smell of acetone. DKA has a high anion gap acidosis; isopropanol gives ketosis with no acidosis and a raised osmolal gap."),
  ],
  traps=[
    ("“Almond breath after a high-dose IV antihypertensive — nitroglycerin”", "Nitroglycerin causes headache and methaemoglobin, not cyanide; nitroprusside releases cyanide. The DocT GrandT1 key (nitroglycerin) is wrong — its own GT3 repeat and explanation give nitroprusside (16% chose it)."),
    ("“No almond smell, so not cyanide”", "Many people cannot smell it; rely on the lactate and the clinical picture."),
  ],
  decode=[
    ("Heart failure, high-dose IV antihypertensive for 20 min, confused, tachycardic, almond breath [DocT GT]", "Sodium nitroprusside → cyanide."),
    ("Hair loss, loss of the lateral eyebrows, behaviour change, nail lines [Marrow]", "Thallium."),
  ],
  punch="An odour is a clue rather than a test — but in the stem it usually names the poison: almonds for cyanide (including from nitroprusside), garlic for organophosphates and arsenic, rotten eggs for hydrogen sulphide.",
  extra=[dict(q="Thallium: how does it present?", a="**Alopecia** (including the lateral eyebrows), a **painful ascending neuropathy**, behaviour change and **Mees lines** on the nails, after gastrointestinal upset.")],
)

L['TOX-07'] = dict(
  sub="Toxicology → Bedside clues → ECG in poisoning",
  intro="The ECG is the quickest way to see whether a poison has reached the heart’s ion channels. The width of the QRS reflects how fast the sodium channels conduct the impulse through the ventricles; the length of the QT reflects how fast potassium channels repolarise them. Drugs that block those channels change the ECG long before the patient arrests.",
  parts=[
    ('a', "**QRS under 0.12 s (120 ms); QTc under 440 ms.** Ventricular depolarisation depends on fast sodium channels, and their speed is the QRS width. Repolarisation depends on potassium channels (hERG); block them and the QT lengthens. In a tricyclic overdose the QRS width, not the dose taken or the drug level, grades the risk: ≥100 ms predicts seizures, ≥160 ms ventricular arrhythmia. That is why the ECG is the first test in a drowsy tricyclic overdose."),
    ('b', "**Tricyclic antidepressants, cocaine, carbamazepine — sodium-channel block — with ventricular tachycardia as the danger.** Slow, uneven conduction widens the QRS and sets up re-entry, which becomes VT. A tricyclic adds right axis deviation and a tall terminal R wave in aVR, usually with sinus tachycardia and anticholinergic signs. Massive propranolol overdose does the same (membrane-stabilising effect). Tricyclics are therefore avoided in patients with bundle branch block."),
    ('c', "**IV sodium bicarbonate, 1–2 mEq/kg.** The sodium load helps push current through the partly blocked channels, and the alkalosis reduces how tightly the drug binds to them. Boluses are repeated until the QRS narrows, aiming for a blood pH of about 7.45–7.55; airway, fluids and benzodiazepines for seizures go alongside."),
    ('d', "**Class Ia and Ic anti-arrhythmics are avoided.** Procainamide, flecainide and their relatives are sodium-channel blockers themselves and deepen the block. Lidocaine (class Ib) is only a second-line option after bicarbonate."),
    ('e', "**Bradycardia or AV block: beta-blockers, calcium-channel blockers, digoxin, cholinergics, opioids, lithium, magnesium, sedative-hypnotics.** These act on the sinus and AV nodes rather than on ventricular conduction."),
  ],
  table=dict(title="What the ECG change points to", head=["Change", "Channel", "Think of"], rows=[["Wide QRS, R in aVR", "Na⁺ block", "tricyclic, cocaine, carbamazepine, propranolol"], ["Long QT", "K⁺ (hERG) block", "antipsychotics, citalopram, quinolones, macrolides, azoles, sotalol, ondansetron"], ["Bradycardia, AV block", "nodes", "β-blocker, CCB, digoxin"]]),
  mimic=[
    ("Wide QRS vs long QT", "A wide QRS is sodium-channel block and is treated with bicarbonate; a long QT is potassium-channel block, treated by stopping the drug and giving magnesium and potassium (TX1-QT)."),
  ],
  traps=[
    ("“Tricyclic overdose, GCS 8 — charcoal or a CT head first”", "An unprotected airway rules out charcoal; the ECG (QRS width) grades the risk. Only 47% on DocT — in reality airway and oxygen come first."),
    ("“Tricyclic with QRS 175, seizures and a full bladder — physostigmine for the anticholinergic signs”", "Physostigmine can cause asystole in tricyclic poisoning; give bicarbonate (43% on DocT GT)."),
    ("“Wide-complex tachycardia after a tricyclic — procainamide or flecainide”", "They are sodium-channel blockers too; bicarbonate first, lidocaine only second-line."),
    ("“The dose or serum level best predicts a tricyclic’s danger”", "Both correlate poorly; the QRS duration does."),
    ("“Calcium, glucagon or insulin will fix a propranolol wide QRS”", "They do not reverse sodium-channel block; bicarbonate does."),
    ("“Typical antipsychotics carry more arrhythmia risk than atypicals”", "The pooled risk is similar (only 3% chose this on DocT GT); the size of QTc prolongation varies by drug — thioridazine and ziprasidone most (TX1-QT)."),
  ],
  decode=[
    ("Amitriptyline and diazepam, GCS 8, HR 140, dilated pupils — initial action among charcoal, CT, ECG, atenolol? [DocT]", "ECG."),
    ("Seizures, pulseless wide-complex tachycardia, QRS 175, terminal R in aVR, suprapubic mass [DocT GT]", "Sodium bicarbonate — not physostigmine, lidocaine or ammonium chloride."),
    ("Amitriptyline overdose 7 h ago — what best stratifies cardiac or neurological risk? [DocT GT]", "QRS duration."),
    ("Massive propranolol, refractory despite glucagon, QRS 180 ms [DocT GT]", "IV sodium bicarbonate."),
  ],
  punch="Sodium channels set the QRS width: block them and it widens toward VT. Bicarbonate pushes through the block, and class Ia and Ic drugs add to it — wide means sodium, slow means the nodes.",
  extra=[dict(q="Tricyclic: dose at which cardiovascular and neurological toxicity begins?", a="About **10 mg/kg**; but the **QRS width**, not the dose, grades the risk."),
         dict(q="Which beta-blocker gives long QT and torsades?", a="**Sotalol** (it also blocks potassium channels).")],
  before="You skipped TOX-06, the odours card. In brief: bitter almonds mean cyanide, garlic means organophosphates or arsenic, rotten eggs mean hydrogen sulphide, and wintergreen means methyl salicylate.",
)

L['TOX-08'] = dict(
  sub="Toxicology → Bedside clues → Osmolal and saturation gaps",
  intro="A ‘gap’ is a mismatch between what is measured and what is expected. When the lab measures more particles in the blood than a formula predicts, or the oximeter shows a saturation that does not fit the blood gas, something unusual is present. Both gaps point to a short list of poisons, so in a comatose patient with a low bicarbonate and a normal CT the next step is to calculate the osmolal and anion gaps.",
  parts=[
    ('a', "**Calculated osmolality = 2 × Na + glucose/18 + BUN/2.8; the gap is measured minus calculated, normally under 10.** The formula counts only sodium with its anions (hence ×2), glucose and urea (divided to convert mg/dL to mmol/L). Anything else dissolved is measured by the lab but missed by the formula. Ethanol is itself an osmole (about ethanol in mg/dL ÷ 3.7–4.6), so subtract its share: a gap still above about 25 after that points to a toxic alcohol."),
    ('b', "**Methanol, ethylene glycol, ethanol, isopropanol, acetone, propylene glycol, mannitol, glycerol, sorbitol.** Small, uncharged molecules present in large amounts. Their metabolites tell them apart: methanol → formic acid, which poisons the retina and optic nerve (visual loss); ethylene glycol → glycolic acid (the acidosis) → oxalic acid, which binds calcium as calcium oxalate crystals in the urine, causing hypocalcaemia and renal failure — the findings specific to ethylene glycol. Isopropanol → acetone: ketosis without acidosis, and two to four times more sedating than ethanol, so coma persists with a normal pH."),
    ('c', "**Saturation gap over 5%: carbon monoxide, methaemoglobin, cyanide, hydrogen sulphide, sulphaemoglobin.** A pulse oximeter uses two wavelengths and assumes only oxy- and deoxyhaemoglobin exist. Carboxyhaemoglobin looks like oxyhaemoglobin, so SpO₂ reads falsely normal; methaemoglobin absorbs equally at both wavelengths and drags the reading toward about 85%, with a normal PaO₂ and chocolate-brown blood. A co-oximeter measures the abnormal haemoglobins directly. Cyanide and H₂S create no arterial gap; the clue is a high venous oxygen and a high lactate."),
    ('d', "**Radio-opaque: chloral hydrate, calcium, heavy metals, iron, iodides, psychotropics, packets, potassium, enteric-coated and sustained-release preparations, salicylates.** Dense atoms or compact tablets and packets; iron tablets and body-packer packets are the practical uses of an abdominal X-ray."),
  ],
  table=dict(title="A normal SpO₂ that is wrong", head=["Poison", "SpO₂", "PaO₂", "Clue"], rows=[["Carbon monoxide", "falsely normal", "normal", "COHb on co-oximetry"], ["Methaemoglobin", "drifts toward ~85%", "normal", "chocolate blood, cyanosis despite O₂"], ["Cyanide", "normal", "normal", "high venous O₂, high lactate"]]),
  mimic=[
    ("Osmolal gap vs anion gap", "The osmolal gap is high early, while the alcohol itself is in the blood; as it is metabolised to acids the osmolal gap falls and the anion gap rises. Early after ingestion the anion gap can still be normal."),
    ("Methanol vs ethylene glycol", "Both raise both gaps. Visual loss means methanol; oxalate crystals, hypocalcaemia and renal failure mean ethylene glycol."),
  ],
  traps=[
    ("“Alcoholic on fomepizole, pH 7.38, still not waking — methanol or ethylene glycol”", "A normal pH with a raised osmolal gap and persistent coma is isopropanol (14% on DocT GT); fomepizole is not needed for it."),
    ("“A raised osmolal gap is the finding specific to ethylene glycol”", "It is raised by any toxic alcohol; calcium oxalate crystals (and renal failure) are specific."),
    ("“Normal SpO₂ and PaO₂ exclude carbon monoxide poisoning”", "Both miss carboxyhaemoglobin; only co-oximetry measures it."),
    ("“A normal osmolal gap excludes methanol”", "Not in a late presenter: the alcohol has already become acid (high anion gap)."),
  ],
  decode=[
    ("Na 140, BUN 10, glucose 100, ethanol 100 mg/dL, measured osmolality 340 — which value supports a toxic alcohol? [DocT GT]", "Osmolal gap >25."),
    ("Severe alcohol use, ethanol 250, fomepizole started, next day pH 7.38 but not waking [DocT GT]", "Isopropyl alcohol."),
    ("Antifreeze, high anion gap acidosis — most specific finding? [NEET 2025]", "Calcium oxalate crystals in urine (renal failure in a second recall)."),
    ("Methaemoglobinaemia will show [DocT GT]", "Pulse oximetry around 85%."),
  ],
  punch="A gap means the lab sees something the formula or the oximeter cannot — an extra osmole in the blood, or a haemoglobin that is not carrying oxygen.",
  extra=[dict(q="Raised osmolal gap: how does the anion gap split it?", a="**Normal anion gap** → isopropanol, acetone, mannitol, diethyl ether. **High anion gap** → methanol, ethylene glycol, formaldehyde, paraldehyde."),
         dict(q="Carbon monoxide: bedside blood test, and the brain lesion?", a="**Hoppe-Seyler test** (blood with alkali stays pink when COHb is present); **globus pallidus** necrosis.")],
)

L['TOX-09'] = dict(
  sub="Toxicology → Decontamination and elimination → Gut decontamination",
  intro="Decontamination tries to stop absorption of a poison that is still in the gut. It only helps while the drug is there, only if the method can bind or move it, and never at the cost of aspiration. So each method has a time window, a list of drugs it works for, and a protected airway as its precondition.",
  parts=[
    ('a', "**Activated charcoal within 1 hour, in an awake patient with a protected airway.** Charcoal has a huge surface that adsorbs most organic drug molecules in the gut lumen — it binds rather than neutralises. Its effect is greatest within an hour, while most drug is still unabsorbed. Aspirating charcoal causes severe pneumonitis, hence the airway condition."),
    ('b', "**Multi-dose charcoal: carbamazepine, theophylline, dapsone, quinine, phenobarbital.** Repeated doses keep the gut lumen empty of free drug, so drug already in the blood diffuses back across the gut wall and is bound — enhanced elimination, not decontamination. It also breaks enterohepatic recirculation."),
    ('c', "**Whole bowel irrigation: polyethylene glycol at 1500–2000 mL/h until the rectal effluent is clear; for iron, lithium, sustained-release or enteric-coated drugs, and body packers.** A large volume of isotonic, non-absorbed solution flushes tablets and packets through before they dissolve. It is for what charcoal cannot bind (iron and lithium are ions), for slow-release tablets such as sustained-release verapamil, and for the asymptomatic body packer — packets are not removed endoscopically (they may rupture); surgery is for obstruction or a leaking packet with toxicity."),
    ('d', "**Induced emesis is not recommended — it is ineffective and risks aspiration.** Ipecac removes little drug and delays charcoal. Gastric lavage is not routine either: consider it only for a potentially life-threatening ingestion within about an hour, with a protected airway; altered consciousness is not itself a contraindication once the patient is intubated."),
  ],
  table=dict(title="Which method for which poison", head=["Problem", "Method"], rows=[["Most organic drugs, <1 h", "single-dose charcoal"], ["Carbamazepine, theophylline, dapsone, quinine, phenobarbital", "multi-dose charcoal"], ["Iron, lithium, slow-release, packets", "whole bowel irrigation"], ["Corrosives, hydrocarbons, unprotected airway", "no gut decontamination"]]),
  mimic=[
    ("Multi-dose charcoal vs urine alkalinisation", "Multi-dose charcoal pulls drug back into the gut (carbamazepine, theophylline); alkalinisation traps weak acids in the urine (salicylate, phenobarbital)."),
  ],
  traps=[
    ("“Asymptomatic body packer — remove the packets endoscopically, or discharge”", "Whole bowel irrigation; endoscopy risks rupture and surgery is for obstruction or leakage (38% on DocT)."),
    ("“Gastric lavage is contraindicated in altered mental status” or “first-line within 1 hour”", "Neither: only for a recent, potentially lethal ingestion, with the airway protected (33% on DocT)."),
    ("“Charcoal is contraindicated with a sustained-release drug” or “dialyse verapamil”", "Charcoal can still be given; verapamil is protein-bound, so whole bowel irrigation is the answer (45% on DocT)."),
    ("“Multi-dose charcoal is the decontamination for any sustained-release drug”", "Whole bowel irrigation is; multi-dose charcoal enhances elimination of its own short list — DocT keys it only because irrigation was not offered (58%)."),
    ("“Charcoal for lithium or iron”", "Ions are not bound by charcoal; use whole bowel irrigation."),
  ],
  decode=[
    ("Body packer, no symptoms, normal ECG, packets on X-ray [DocT]", "Whole bowel irrigation."),
    ("Large sustained-release verapamil ingestion — most accurate statement [DocT]", "Whole bowel irrigation may be beneficial."),
    ("Gastric lavage in an obtunded overdose — most accurate statement [DocT]", "May be considered if potentially life-threatening and very recent."),
    ("Activated charcoal — most accurate statement [NEET 2025]", "Most effective within 1 hour of ingestion."),
  ],
  punch="Decontaminate only what is still in the gut and can be bound or flushed out — charcoal binds organic molecules, metals and ions slip through, and the airway always comes first.",
  extra=[dict(q="Whole bowel irrigation is NOT indicated for?", a="**Quinine** — it is a multi-dose charcoal drug.")],
)

L['TOX-10'] = dict(
  sub="Toxicology → Decontamination and elimination → Urine alkalinisation",
  intro="The kidney filters many drugs, but most are then reabsorbed as they pass down the tubule. Only the un-ionised (uncharged) form can cross the tubular wall. Change the urine pH so the drug becomes ionised, and it is trapped in the urine and excreted — ion trapping.",
  parts=[
    ('a', "**Urine pH ≥7.5, using IV sodium bicarbonate.** For a weak acid, each unit of pH above its pKa makes it about ten times more ionised, so a small rise in urine pH greatly increases excretion."),
    ('b', "**Weak acids that are renally eliminated and poorly protein-bound.** Only a weak acid is ionised by alkaline urine; a weak base such as phencyclidine or amphetamine becomes less ionised and is reabsorbed more, so alkalinisation cannot be used for them."),
    ('c', "**Salicylates, methotrexate, phenobarbital, 2,4-D (a herbicide), chlorpropamide.** Salicylate is the main indication. Alkalinising the blood also keeps salicylate ionised in plasma, so less enters the brain — which is why an alkalaemic pH from the early respiratory alkalosis is not a contraindication. A rising salicylate level with symptoms means continued absorption (enteric-coated tablets or a bezoar): start bicarbonate then, rather than waiting for another level."),
    ('d', "**Monitor urine pH and electrolytes, especially potassium.** When potassium is low the kidney holds on to it by secreting hydrogen ions, so the urine stays acid however much bicarbonate is given — correct potassium first."),
    ('e', "**Renal failure is the contraindication.** A failing kidney cannot clear the drug or handle the sodium load; severe salicylate poisoning with renal failure goes to haemodialysis (TOX-11)."),
  ],
  mimic=[
    ("Alkalinisation for salicylate vs bicarbonate for tricyclics", "In salicylate poisoning bicarbonate traps the drug in urine; in tricyclic poisoning it overcomes sodium-channel block in the heart."),
  ],
  traps=[
    ("“Alkalinisation works for phencyclidine or amphetamines”", "They are weak bases; alkaline urine traps acids. Chlorpropamide, by contrast, is a weak acid on the list (31% on DocT)."),
    ("“pH 7.54, so bicarbonate is contraindicated in salicylate poisoning”", "The early respiratory alkalosis is not a contraindication; salicylic acid is a weak acid trapped in alkaline urine."),
    ("“Salicylate level rising from 20 to 35 with tachypnoea — repeat the level in 2 hours”", "Rising level plus symptoms means start IV bicarbonate now (45% on DocT GT)."),
    ("“Intubate the salicylate patient and ventilate normally”", "Losing his hyperventilation makes the blood acid and drives salicylate into the brain; avoid intubation if possible, and if needed match the high minute ventilation."),
    ("“Bicarbonate alone will alkalinise the urine”", "Not if potassium is low — correct K⁺ first."),
  ],
  decode=[
    ("Urinary alkalinisation cannot be used in: salicylate, chlorpropamide, phenobarbitone, phencyclidine [DocT]", "Phencyclidine."),
    ("Salicylate, pH 7.54, PaCO₂ 22, bicarbonate given — which property supports it? [DocT GT]", "Salicylic acid is a weak acid; alkaline urine enhances its excretion."),
    ("‘Handfuls’ of analgesics, salicylate 20 then 35 mg/dL, nauseated, tachypnoeic, pH 7.50 [DocT GT]", "IV sodium bicarbonate now."),
  ],
  punch="An acid is trapped in base: alkaline urine ionises the weak acid so it cannot be reabsorbed — and without enough potassium the kidney will not let the urine turn alkaline.",
)

L['TOX-11'] = dict(
  sub="Toxicology → Decontamination and elimination → Extracorporeal removal",
  intro="Dialysis cleans the blood, so it can only remove a drug that is actually in the blood, free to cross the membrane. A drug bound to plasma proteins, or spread out into fat and tissues, is beyond its reach. Three properties of the molecule therefore decide whether dialysis is worth starting — and the decision to start is triggered by a high level or by organ toxicity.",
  parts=[
    ('a', "**Low molecular weight, low protein binding, small volume of distribution (the drug stays in the extracellular fluid).** A small molecule crosses the membrane, an unbound molecule is free in plasma, and a small volume of distribution means most of the body’s load is in the blood, so cleaning the blood empties the body. Atenolol and sotalol are water-soluble and poorly bound, so unlike other beta-blockers they can be dialysed when glucagon and pressors fail."),
    ('b', "**Haemodialysis removes salicylates, lithium, methanol, ethylene glycol and isopropanol.** All are small and poorly bound, and dialysis also corrects the acidosis and removes toxic metabolites. Lithium is the model dialysable toxin; dialysis is indicated for a high level with impaired kidney function or for neurological toxicity (reduced consciousness, seizures) or arrhythmia at any level — forced diuresis does not help. In ethylene glycol or methanol poisoning, severe acidosis or acute kidney injury means dialysis now, with fomepizole given alongside."),
    ('c', "**Haemoperfusion: barbiturates, carbamazepine, theophylline, valproate — over a charcoal or resin adsorbent.** These moderately protein-bound drugs are stripped off protein by the adsorbent. Current EXTRIP guidance prefers high-flux haemodialysis for all four; older keys still answer ‘haemoperfusion’."),
  ],
  mimic=[
    ("Haemodialysis vs haemofiltration or peritoneal dialysis", "Intermittent haemodialysis clears fastest; haemofiltration and peritoneal dialysis are too slow for a severe salicylate or lithium poisoning."),
  ],
  traps=[
    ("“Ethylene glycol 45 mg/dL is below 50, so observe or just start fomepizole”", "pH 7.10 and creatinine 3.5 mean haemodialysis now; the level rule is secondary. Fomepizole goes in too — the key is defensible because dialysis is the step that cannot wait (46% on DocT GT)."),
    ("“Refractory atenolol overdose — lipid or insulin will save him”", "Atenolol is dialysable (hydrophilic, low protein binding); haemodialysis is the answer (50% on DocT GT). Lipid suits lipophilic drugs such as propranolol."),
    ("“Lithium toxicity — furosemide or forced alkaline diuresis”", "Diuresis worsens sodium loss and lithium retention; dialyse."),
    ("“Digoxin and tricyclics are removed by dialysis”", "Both have a huge volume of distribution (and tricyclics are highly protein-bound)."),
  ],
  decode=[
    ("Aspirin 12 h ago, salicylate 1120 mg/L, creatinine 2.38, bicarbonate 14 [DocT]", "Haemodialysis."),
    ("Lithium 5.0 mmol/L, tremor, convulsion, GCS 12 [DocT]", "Haemodialysis."),
    ("Antifreeze, pH 7.10, anion gap 28, creatinine 3.5, ethylene glycol 45 mg/dL, no fomepizole yet [DocT GT]", "Initiate haemodialysis (start fomepizole too)."),
    ("Large atenolol ingestion, refractory despite glucagon and pressors [DocT GT]", "Haemodialysis for drug removal."),
  ],
  punch="Dialysis can reach only what is small, free and in the blood; start it for a high level or organ damage, and remember that a drug hidden in the tissues cannot be dialysed at all.",
  extra=[dict(q="Salicylate: when to dialyse?", a="Level **>100 mg/dL** (>90 with impaired kidney function), or **any level** with altered mental status, new hypoxaemia or **pH ≤7.20** despite treatment. A level of 50 mg/dL alone is not an indication."),
         dict(q="Carbamazepine: severe toxicity level, and what tips a stable patient over?", a="**Above 40 µg/mL**; CYP3A4 inhibitors (**diltiazem**, isoniazid, macrolides) raise the level; valproate raises the toxic epoxide.")],
)

L['TOX-12'] = dict(
  sub="Toxicology → Decontamination and elimination → Supportive care",
  intro="Most poisoned patients survive on good supportive care rather than an antidote. The usual emergency drugs mostly work here too — with one rule added: do not give a drug that does the same harm as the poison. That rule explains every choice on this card.",
  parts=[
    ('a', "**Hypertension: a calcium-channel blocker, phentolamine, labetalol or nitroprusside.** Toxic hypertension is usually catecholamine excess (cocaine, amphetamines). A benzodiazepine to calm the sympathetic storm comes first; then an α-blocker or vasodilator — phentolamine (a pure α-blocker) is the keyed first antihypertensive, with nicardipine, nitroglycerin or nitroprusside as alternatives. Any beta-blocker, even labetalol, risks leaving α-stimulation unopposed, and vasoconstrictors such as phenylephrine or noradrenaline make it worse."),
    ('b', "**Seizures: benzodiazepines, then barbiturates.** Toxic seizures are treated by strengthening GABA-A inhibition. Phenytoin is avoided — it rarely works for toxic seizures and is itself a sodium-channel blocker. A tricyclic seizure with a wide QRS needs airway, fluids, benzodiazepines and sodium bicarbonate together."),
    ('c', "**Ventricular tachycardia: sodium bicarbonate; avoid class Ia and Ic.** Toxic VT is usually sodium-channel block (TOX-07)."),
    ('d', "**Bradyarrhythmia: atropine and pacing.** These support the rate while the specific antidote (digoxin Fab, high-dose insulin, glucagon — TOX-14) takes effect."),
    ('e', "**Hyperthermia: active cooling.** Toxic hyperthermia comes from muscle activity and failed heat loss with a normal set point, so antipyretics do not work; cool, sedate, and paralyse if it keeps rising."),
  ],
  mimic=[],
  traps=[
    ("“Methamphetamine with severe hypertension and seizures — labetalol or propranolol”", "Avoid beta-blockers; benzodiazepine first, then phentolamine (DocT key) — nicardipine is equally defensible (50% on DocT)."),
    ("“Phenytoin for a tricyclic seizure”", "Another sodium-channel blocker, and ineffective; use benzodiazepines then barbiturates."),
    ("“Paracetamol for drug-induced hyperthermia”", "The set point is normal; cool actively."),
  ],
  decode=[
    ("Acute methamphetamine toxicity, severe hypertension and seizures — best initial antihypertensive? [DocT]", "Phentolamine (nicardipine also defensible; benzodiazepines are the true first step)."),
    ("Cocaine, hypertensive emergency — safest vasodilator? [DocT]", "Nitroprusside (not phenylephrine, beta-blockers or noradrenaline)."),
    ("Seizure, dilated pupils, QRS >120 ms — management of choice [Marrow]", "Airway, fluids, benzodiazepines and IV sodium bicarbonate."),
  ],
  punch="Toxic emergencies get the usual tools minus the ones the poison already uses: benzodiazepines first, no phenytoin, no beta-blockers for stimulant hypertension, no class Ia or Ic, and cooling rather than antipyretics.",
)

L['TOX-13'] = dict(
  sub="Toxicology → Antidotes → Toxin to antidote (1)",
  intro="An antidote works by undoing the poison’s one key move. Some refill what the poison uses up, some push it off its receptor, some block the enzyme that makes it toxic, and some bind it so it cannot act. If you know the poison’s move, you can work out the antidote — and its limits.",
  parts=[
    ('a', "**Paracetamol — N-acetylcysteine.** Paracetamol becomes toxic when its metabolite NAPQI exhausts the liver’s glutathione; N-acetylcysteine refills it. It is still given once acute liver failure has developed."),
    ('b', "**Opioids — naloxone, 0.04–2 mg.** Naloxone competes the opioid off the μ receptor. Small doses restore breathing in the opioid-dependent without severe withdrawal; larger doses for apnoea."),
    ('c', "**Organophosphate — atropine plus pralidoxime 1–2 g over 30 minutes.** Organophosphates and nerve agents such as sarin inhibit acetylcholinesterase, so acetylcholine floods every synapse: miosis, bradycardia, secretions, diarrhoea, urination. Atropine blocks the muscarinic excess and is titrated to dry chest secretions; pralidoxime reactivates the enzyme before the bond ‘ages’."),
    ('d', "**Methanol, ethylene glycol — fomepizole 15 mg/kg over 30 minutes, then 10 mg/kg 12-hourly for four doses, then 15 mg/kg 12-hourly.** The parent alcohols are relatively non-toxic; their acids kill — formic acid damages the retina and optic nerve directly (‘snowstorm’ vision), oxalate forms calcium oxalate crystals and kidney injury. Fomepizole blocks alcohol dehydrogenase so the acids are not made; it is started at once on suspicion, before levels return. Ethanol at ≥100 mg/dL already occupies the enzyme, so fomepizole can wait while the ethanol is high. Established acidosis, visual signs or kidney injury add haemodialysis."),
    ('e', "**Carbon monoxide — 100% oxygen, hyperbaric in some.** Oxygen competes CO off haemoglobin and shortens the COHb half-life from about 4 hours on air to about 1 hour on 100%, and further under hyperbaric pressure. A comatose patient (GCS ≤8) is intubated and ventilated with 100% oxygen. The only absolute contraindication to hyperbaric oxygen is an untreated pneumothorax; prior bleomycin, COPD with bullae, seizures and pregnancy are relative — weigh the risk and take consent."),
    ('f', "**Cyanide — sodium nitrite 300 mg IV (hydroxocobalamin 5 g is now first choice).** Nitrite turns some haemoglobin into methaemoglobin, which pulls cyanide off cytochrome oxidase; thiosulphate then converts it to thiocyanate. Hydroxocobalamin binds cyanide directly, without creating methaemoglobin or lowering blood pressure, so it is preferred whenever there is shock or smoke (carbon monoxide) exposure."),
    ('g', "**Methaemoglobinaemia — methylene blue 1–2 mg/kg.** It is reduced to leucomethylene blue, which converts methaemoglobin back to haemoglobin. The reaction needs NADPH from the G6PD pathway, so in G6PD deficiency it fails and causes haemolysis — use ascorbic acid instead (or exchange transfusion). Methaemoglobin shifts the dissociation curve to the left, and methylene blue, a dye, itself distorts oximetry."),
    ('h', "**Iron — deferoxamine, up to 15 mg/kg/h.** Deferoxamine chelates free iron into ferrioxamine, which the kidney excretes (vin-rosé urine). If the kidneys fail, haemodialysis removes the ferrioxamine complex — not the iron itself — so chelation can continue."),
  ],
  mimic=[
    ("Cyanide antidotes in a fire victim", "Nitrite makes methaemoglobin, which worsens oxygen carriage when CO is also present; hydroxocobalamin does not."),
  ],
  traps=[
    ("“G6PD deficiency: methylene blue still works” or “the curve shifts right”", "It fails and haemolyses — give ascorbic acid; and methaemoglobin shifts the curve left (43% on DocT)."),
    ("“Bleomycin or COPD is an absolute contraindication to hyperbaric oxygen”", "Relative only; an untreated pneumothorax is the one absolute contraindication (50% on DocT)."),
    ("“Cyanide with lactate 12 and hypotension — nitrite plus thiosulphate”", "Hydroxocobalamin is first choice, and nitrite worsens hypotension (42% on DocT)."),
    ("“Smoke inhalation with cyanide — sodium nitrite is fine”", "Avoid it: its methaemoglobin adds to the CO deficit (55% on DocT GT)."),
    ("“Moonshine plus ethanol 453 mg/dL — start fomepizole at once”", "Ethanol is blocking alcohol dehydrogenase; fomepizole can be deferred and started as ethanol falls (37% on DocT GT)."),
    ("“Osmolal gap 32, severe acidosis — dialysis before anything”", "The therapy started immediately is a fomepizole load; dialysis follows for severe acidosis (33% on DocT GT). When the stem stresses established acidosis and AKI and asks for the next step, the key is dialysis (TOX-11)."),
    ("“Antifreeze crystals are uric acid or struvite”", "Calcium oxalate (51% on DocT GT)."),
  ],
  decode=[
    ("Factory worker, cyanosis — true statement? [DocT]", "Ascorbic acid is used in G6PD deficiency."),
    ("Clothing-factory fire, ‘bitter almond’, convulsions — which cyanide treatment to AVOID? [DocT GT]", "Sodium nitrite."),
    ("Oxycodone, liquor and moonshine, ethanol 453 — fomepizole deferred because of? [DocT GT]", "Ethanol."),
    ("CO poisoning in a patient with COPD and prior bleomycin — hyperbaric oxygen? [DocT]", "Relatively contraindicated: proceed after risk assessment and consent."),
  ],
  punch="Each antidote undoes the toxin’s one move — refill what it uses up, push it off the receptor, block the enzyme that makes it toxic, or bind it — so name the move and both the antidote and its limits follow.",
  extra=[dict(q="Methanol vs ethylene glycol: what separates them?", a="Their acid. **Methanol → formic acid** → retina and optic nerve (snowstorm vision, blindness), putamen; folinic acid speeds formate clearance. **Ethylene glycol → glycolic then oxalic acid** → calcium oxalate crystals, hypocalcaemia, AKI at 24–72 h."),
         dict(q="CO: COHb half-life on air, 100% O₂, hyperbaric?", a="About **4 h · 1 h · 20–30 min**."),
         dict(q="CO with COHb 12% and no high-risk features?", a="**Normobaric 100% oxygen** by mask for about **6 h**; hyperbaric oxygen for loss of consciousness, COHb >25% (>15% in pregnancy), ischaemia or neurological signs."),
         dict(q="Antidote match: sulfonylurea, CO, cyanide, metoprolol, desipramine?", a="**Octreotide · oxygen · hydroxocobalamin · glucagon · sodium bicarbonate**.")],
)

L['TOX-14'] = dict(
  sub="Toxicology → Antidotes → Toxin to antidote (2)",
  intro="Cardiotoxic poisons shut down the heart’s channels, receptors or fuel supply. The antidotes on this card mostly do not reverse the poison itself; they go around the blocked step — feeding the heart another way, raising its second messengers through a different receptor, or binding the drug.",
  parts=[
    ('a', "**Digoxin — digoxin-specific Fab: 10–20 vials in acute poisoning, 3–6 in chronic.** Fab binds digoxin and the complex is excreted by the kidney. For a known ingested amount, vials = mg × 0.8 (bioavailability) ÷ 0.5 mg bound per vial. Give it for a life-threatening dysrhythmia (VT, VF, or bradycardia or block unresponsive to atropine), potassium >5.0 in acute poisoning, a level >10 ng/mL at 6 h or more, or an adult ingestion >10 mg — not for nausea, first-degree block or a therapeutic level. In severe renal failure the complex lingers and slowly dissociates, so free digoxin and toxicity can rebound days later."),
    ('b', "**Calcium-channel blocker — high-dose insulin 0.5–1 U/kg/h with dextrose; lipid emulsion.** IV calcium, fluids and pressors come first, with charcoal or whole bowel irrigation for sustained-release tablets. The poisoned heart switches from fatty acids to glucose but cannot take it up, because the drug also blocks insulin release. High-dose insulin lets the myocardium use glucose, improving contractility without the rise in oxygen demand that catecholamines bring; dextrose prevents hypoglycaemia. Calcium raises contractility and blood pressure but does little for heart rate or AV conduction. Calcium-channel blockers keep the patient alert and raise glucose."),
    ('c', "**Beta-blocker — atropine; glucagon; high-dose insulin.** Bradycardia is the commonest feature. Glucagon raises cAMP through its own receptor, bypassing the blocked β-receptor; it is the classic drug of choice, although recent consensus ranks high-dose insulin above it. Beta-blocker poisoning more often depresses consciousness."),
    ('d', "**Tricyclic antidepressant — sodium bicarbonate 1–2 mEq/kg; lipid.** Bicarbonate overcomes the sodium-channel block (TOX-07); lipid is a rescue for refractory cardiotoxicity."),
    ('e', "**Sulfonylurea — octreotide 50 µg SC 6-hourly with dextrose.** Sulfonylureas force insulin release. Dextrose alone triggers more insulin and rebound hypoglycaemia; octreotide stops the release."),
    ('f', "**Benzodiazepine — flumazenil, rarely, because of the seizure risk.** Reserved for iatrogenic over-sedation in a non-dependent patient (TOX-01)."),
    ('g', "**Local anaesthetic — 20% lipid emulsion** (TOX-15)."),
  ],
  table=dict(title="How each antidote goes around the block", head=["Antidote", "Mechanism"], rows=[["Digoxin Fab", "binds digoxin itself"], ["High-dose insulin", "lets the poisoned heart use glucose"], ["Glucagon", "raises cAMP through its own receptor, bypassing β"], ["Bicarbonate", "Na⁺ load and alkalosis overcome Na⁺-channel block"], ["Octreotide", "stops the pancreas releasing insulin"], ["Lipid emulsion", "pulls lipophilic drug out of the heart"]]),
  mimic=[
    ("Calcium-channel blocker vs beta-blocker poisoning", "Both give bradycardia and hypotension. A normal mental state and hyperglycaemia suggest a calcium-channel blocker; beta-blockers depress consciousness and their effect on glucose varies. Propranolol also widens the QRS."),
  ],
  traps=[
    ("“8 mg digoxin — 8 vials”", "8 × 0.8 ÷ 0.5 ≈ 13 vials; DocT keys 16 (bioavailability ignored), the closest option (31%)."),
    ("“Glyburide, glucose 52 after D50 — more D50 or a glucose infusion”", "D50 plus octreotide; dextrose alone drives more insulin release (47% on DocT GT)."),
    ("“Recurrent bradyarrhythmia 4 days after Fab in CKD — Fab hypersensitivity”", "Rebound free digoxin as the complex dissociates."),
    ("“IV calcium will correct heart rate in verapamil overdose”", "It improves contractility and blood pressure; heart rate (and AV conduction — a second defensible answer) changes least."),
  ],
  decode=[
    ("8 mg digoxin, VT, no levels — vials to bind the ingestion (2/4/8/16)? [DocT]", "16 (≈13 with bioavailability)."),
    ("Glyburide, sertraline, omeprazole; glucose 33, then 52 an hour after D50 [DocT GT]", "D50 bolus and octreotide."),
    ("Massive verapamil on calcium, pacing, glucagon — why does high-dose insulin help without raising O₂ demand? [DocT GT]", "Enhanced glucose utilisation."),
    ("Severe digoxin toxicity in stage 5 CKD, Fab given, bradyarrhythmia 4 days later [DocT GT]", "Rebound free digoxin."),
  ],
  punch="When a drug shuts down the heart’s channels or fuel, the antidote goes around the blocked step: insulin refuels the myocardium, glucagon skips the β-receptor, and octreotide stops the insulin a sulfonylurea forces out.",
)

L['TOX-15'] = dict(
  sub="Toxicology → Antidotes → Lipid emulsion for local anaesthetic toxicity",
  intro="Bupivacaine and other local anaesthetics are lipophilic and bind tightly to cardiac sodium channels; an accidental intravascular dose causes seizures, then bradycardia and cardiac arrest that resists standard resuscitation. A 20% lipid emulsion creates a fat phase in the blood into which the drug moves out of the heart. The doses are by weight, with a ceiling, and resuscitation itself is modified.",
  parts=[
    ('a', "**Bolus: 20% lipid 1.5 mL/kg over 2–3 minutes (100 mL if over 70 kg).** The bolus quickly builds a lipid sink in plasma. The same 1.5 mL/kg bolus is the rescue for other lipophilic cardiotoxins — propranolol, verapamil, tricyclics — once standard antidotes have failed."),
    ('b', "**Infusion: 0.25 mL/kg/min (200–250 mL over 15–20 minutes if over 70 kg). If still unstable, repeat the bolus once or twice and double the rate.** The infusion keeps the lipid level up while the drug is redistributed and cleared."),
    ('c', "**Maximum dose: 12 mL/kg.** Larger loads risk pancreatitis, fat overload and lung injury."),
    ('d', "**Changes to resuscitation: adrenaline boluses ≤1 µg/kg; avoid vasopressin, calcium-channel blockers, beta-blockers and lidocaine; benzodiazepines for seizures, avoiding large doses of propofol.** Large adrenaline doses worsen arrhythmia; lidocaine is another local anaesthetic; the others depress a failing heart."),
    ('e', "**Monitoring: 4–6 hours after a cardiovascular event; 2 hours after a CNS-only event.** As the lipid is cleared, the drug can return from fat to the heart."),
  ],
  table=dict(title="Lipid dosing", head=["Step", "Dose"], rows=[["Bolus", "**1.5 mL/kg** over 2–3 min"], ["Infusion", "**0.25 mL/kg/min**"], ["Still unstable", "repeat bolus ×1–2, double rate"], ["Ceiling", "**12 mL/kg**"]]),
  mimic=[
    ("LAST vs anaphylaxis after an epidural", "Wheeze, flushing and hypotension point to anaphylaxis — IM adrenaline. LAST gives perioral numbness, seizures and arrhythmia — lipid."),
  ],
  traps=[
    ("“Standard 1 mg adrenaline boluses”", "Use small boluses, ≤1 µg/kg."),
    ("“Lidocaine or amiodarone is the drug of choice for the arrest”", "Lipid emulsion is; lidocaine adds to the toxicity."),
    ("“Any reaction to an epidural local anaesthetic is LAST”", "Wheeze and flushing mean anaphylaxis — adrenaline, not lipid."),
  ],
  decode=[
    ("Seizures, then bradycardia and arrest after bupivacaine for a nerve block — drug of choice? [DocT GT]", "Lipid emulsion."),
    ("Massive propranolol, refractory despite glucagon, insulin and bicarbonate — what is given as a 1.5 mL/kg bolus? [DocT GT]", "IV lipid emulsion (ECMO is the next step, not a bolus)."),
    ("Epidural bupivacaine and morphine, then wheeze, hypotension, flushing [Marrow]", "IM adrenaline — anaphylaxis, not LAST."),
  ],
  punch="Lipid soaks the fat-soluble drug out of the heart, so it is dosed by weight with a ceiling of 12 mL/kg — and resuscitation changes with it: small adrenaline doses and no extra local anaesthetic.",
)

L['TOX-16'] = dict(
  sub="Toxicology → Revision → True or false",
  intro="This card tests the deck’s key distinctions. Each statement is either true or turns on one detail from an earlier card; the reason for each answer is the mechanism you met there.",
  parts=[
    ('a', "**False — anticholinergic skin is dry.** Sweat glands work through muscarinic receptors (TOX-03)."),
    ('b', "**True — bitter almonds suggest cyanide** (TOX-06), though many people cannot smell it."),
    ('c', "**False — lithium is not bound by charcoal; use whole bowel irrigation.** Ions such as lithium and iron slip through (TOX-09)."),
    ('d', "**True — urine alkalinisation is used for salicylates.** A weak acid is trapped in alkaline urine (TOX-10)."),
    ('e', "**False — a tricyclic wide QRS is treated with bicarbonate; avoid class Ia drugs such as procainamide.** Procainamide is itself a sodium-channel blocker; physostigmine, despite the anticholinergic signs, risks asystole; lidocaine is only second-line (TOX-07)."),
    ('f', "**True — octreotide treats sulfonylurea overdose** by stopping insulin release (TOX-14)."),
    ('g', "**True — the maximum lipid emulsion dose is 12 mL/kg** (TOX-15)."),
    ('h', "**True — methanol raises the osmolal gap,** early, before it is metabolised to formic acid (TOX-08)."),
  ],
  mimic=[],
  traps=[
    ("“Tricyclic with anticholinergic signs — physostigmine”", "Contraindicated: asystole risk. Bicarbonate (43% on DocT GT)."),
    ("“Any anti-arrhythmic will do for a toxic wide QRS”", "Class Ia and Ic deepen sodium-channel block."),
  ],
  decode=[
    ("Seizures, pulseless wide-complex tachycardia, QRS 175, terminal R in aVR, dilated pupils, suprapubic mass [DocT GT]", "Sodium bicarbonate."),
    ("Same stem: why not the other options? [DocT GT]", "Physostigmine risks asystole, ammonium chloride acidifies, lidocaine is second-line."),
  ],
  punch="Every statement here turns on a mechanism from earlier in the deck — the sweat gland’s muscarinic receptor, what charcoal can bind, ion trapping, and sodium-channel block.",
)

FLAGS = {
  'TOX-12': "Card a lists labetalol for toxic hypertension; DocT (methamphetamine HTN, keyed phentolamine) says avoid beta-blockers including labetalol, and labetalol remains debated in cocaine toxicity. Consider dropping labetalol or marking it ‘debated’. Explanation restates the card and adds the caveat.",
  'TOX-11': "Card b omits atenolol, which DocT GT keys as dialysable (refractory atenolol → haemodialysis). Consider adding ‘atenolol, sotalol’. Explanation adds it in part a.",
}
