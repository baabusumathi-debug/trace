# TOX01 — Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Fields per card:
#   sub    breadcrumb: System → topic → subtopic
#   intro  "What's going on": 2–4 plain sentences that set the scene before any fact
#   parts  [(letter, text)] mirroring the card's own letters; text = **restated answer** + the why (1–4 sentences)
#   table  optional dict(title, head, rows) — only for decisions, steps or comparisons
#   mimic  [(pair, discriminator)] close look-alikes
#   traps  [(wrong belief, correction with its why)]
#   decode [(how the stem is worded, what it points to)]
#   punch  the punchline — last, one or two sentences, only after the build-up
#   extra  optional exam add-ons [dict(q, a)] shown from the second sight (kept from the pilot)
#   before optional bridge text for Any-hit flows when the previous card was skipped (full sentences)
L = {}

L['TOX-01'] = dict(
  sub="Toxicology → First steps → Coma of unknown cause",
  intro="A patient arrives unconscious and nobody knows why. A few causes of coma injure the brain within minutes yet are reversed by a cheap drug: low glucose, opioid respiratory depression, and thiamine deficiency in the malnourished or alcohol-dependent. The coma cocktail treats these first, before the cause is known — so every drug in it must be harmless if the guess turns out to be wrong.",
  parts=[
    ('a', "**Empirical treatment for coma of unknown cause.** Empirical means given on suspicion, before a diagnosis. It is justified only when the condition is common, dangerous and quickly reversible, and when the drug does no harm to the patients who turn out not to have it."),
    ('b', "**Dextrose 50 mL of 50%, thiamine 100 mg IV, naloxone up to 2 mg.** The brain runs almost entirely on glucose and has no store of it, so hypoglycaemia injures neurons within minutes — check a capillary glucose and treat. Thiamine is a cofactor of glucose metabolism; alcohol-dependent and malnourished patients may lack it, and 100 mg is cheap protection against Wernicke’s encephalopathy. Naloxone displaces opioids from the μ receptor and restores breathing within minutes; in a patient who is still breathing and may be opioid-dependent it is given in small steps (from 0.04 mg) to avoid violent withdrawal."),
    ('c', "**Yes — glucose goes first if it is needed.** The old teaching was that a glucose load in a thiamine-deficient patient uses up the last thiamine and precipitates Wernicke’s. There is no good evidence that a single dose does this, whereas untreated neuroglycopenia causes certain brain injury. So glucose is never delayed for thiamine; thiamine is given alongside, as soon as possible."),
    ('d', "**Flumazenil.** It is a benzodiazepine antagonist, so it looks like a ‘benzodiazepine naloxone’, but it fails the safe-if-wrong test. In a patient dependent on benzodiazepines it precipitates withdrawal seizures. In a mixed overdose with a drug that causes seizures — a tricyclic is the classic — the benzodiazepine was what held the seizures back. Seizures that follow are hard to treat, because the usual first drug, a benzodiazepine, is now blocked."),
  ],
  mimic=[
    ("Naloxone vs flumazenil", "Both are competitive antagonists. Opioid apnoea kills and naloxone reverses it safely; benzodiazepines alone rarely stop breathing, so flumazenil adds seizure risk for little gain."),
    ("Prophylactic vs treatment thiamine", "100 mg in the cocktail is prophylaxis. Suspected Wernicke’s encephalopathy needs treatment doses (500 mg IV 8-hourly)."),
  ],
  traps=[
    ("“Thiamine must always be given before glucose”", "Glucose is never delayed; there is no good evidence a single glucose dose precipitates Wernicke’s."),
    ("“Flumazenil belongs in the coma cocktail”", "It is not given empirically — seizures in benzodiazepine dependence or tricyclic co-ingestion."),
    ("“100 mL of 50% dextrose”", "The usual dose is 50 mL of 50% (25 g); one page of your notes prints 100 mL."),
  ],
  decode=[
    ("Coma of unknown cause — first drugs?", "Dextrose, thiamine, naloxone."),
    ("Which antidote is NOT given empirically?", "Flumazenil."),
    ("Hypoglycaemic alcohol-dependent patient — thiamine or glucose first?", "Glucose without delay, thiamine alongside."),
  ],
  punch="An empirical antidote must be safe even when the guess is wrong: dextrose, thiamine and naloxone pass that test; flumazenil fails it.",
  extra=[dict(q="Wernicke encephalopathy suspected: thiamine dose?", a="**500 mg IV 8-hourly for 3 days** (then 250 mg daily if responding); the 100 mg of the coma cocktail is only prophylaxis.")],
)

L['TOX-02'] = dict(
  sub="Toxicology → First steps → Initial work-up",
  intro="In an overdose the history is the least reliable part of the assessment: the patient may be confused, unconscious or unwilling to say, and mixed ingestions are common. So, after the airway, breathing and circulation are secured, the examination and a few bedside tests become the history. Two poisons are checked in everyone, because they look harmless early and are treatable only if found in time.",
  parts=[
    ('a', "**Mental status, pupils, skin temperature and moisture, SpO₂, ECG, capillary glucose; expose the patient.** Pupils and skin sort the patient into a toxidrome (TOX-03, 04). The ECG picks up drugs that block cardiac channels — a wide QRS or a long QT changes treatment at once. A capillary glucose excludes the commonest reversible cause of coma. Exposing the patient finds patches, needle marks, pill packets and injuries."),
    ('b', "**Opioids, benzodiazepines, cannabinoids, amphetamines, phencyclidine, cocaine.** A urine immunoassay looks for a fixed panel of drug classes or their metabolites. It answers ‘was a drug from this panel taken recently?’, not ‘what is making this patient ill now?’."),
    ('c', "**False negatives below the threshold, false positives with chronic use, and cross-reactivity — so always correlate clinically.** Drugs outside the panel (synthetic cathinones, synthetic cannabinoids, many prescription drugs) are simply not detected. Metabolites linger, so a chronic cannabis user tests positive for weeks. Unrelated drugs can trigger the antibody and give a false positive. The screen supports a diagnosis; it never makes or excludes one."),
    ('d', "**Paracetamol and salicylate.** Paracetamol gives almost no symptoms for the first day while liver injury develops, and N-acetylcysteine works best when started early. Salicylate shows only subtle early signs (tinnitus, fast breathing) before acidosis and collapse, and needs alkalinisation or dialysis. Both are common, both are often taken with other drugs, and both are treatable only if measured — so a level is sent in every overdose, whatever the history says."),
  ],
  mimic=[
    ("Urine drug screen vs serum drug level", "The urine screen is qualitative (present or absent, possibly days old). A serum level is quantitative and guides treatment — paracetamol, salicylate, lithium, digoxin, iron."),
  ],
  traps=[
    ("“A negative drug screen excludes drug toxicity”", "Designer drugs and many prescription drugs are not on the panel; a negative screen means only ‘nothing from the panel above the threshold’."),
    ("“The patient denies paracetamol, so no level is needed”", "The history is unreliable and early paracetamol toxicity is silent; the level is sent in every overdose."),
    ("“A positive screen explains the coma”", "It may reflect use days ago (cannabis for weeks); look for the cause in the examination."),
  ],
  decode=[
    ("Which two levels are sent in every overdose?", "Paracetamol and salicylate."),
    ("Sympathomimetic picture, urine screen negative", "A drug the immunoassay misses — synthetic cathinones or cannabinoids."),
    ("Main limitation of a urine drug screen", "False negatives and positives — correlate clinically."),
  ],
  punch="In overdose the examination is the history, the urine screen only hints, and paracetamol and salicylate are measured in everyone because they are silent early and treatable in time.",
)

L['TOX-03'] = dict(
  sub="Toxicology → Toxidromes → Sympathomimetic vs anticholinergic",
  intro="Both of these patients arrive hot, fast and agitated with big pupils, so the obvious signs cannot separate them. The difference lies in one odd piece of physiology: sweat glands are supplied by sympathetic nerves, but those nerves release acetylcholine onto muscarinic receptors. That single fact decides the skin — and the skin decides the toxidrome.",
  parts=[
    ('a', "**Skin: sympathomimetic wet; anticholinergic dry and flushed.** A sympathomimetic drives the sympathetic system, including its cholinergic sweat fibres, so the patient sweats. An anticholinergic blocks the muscarinic receptor on the sweat gland, so the skin is dry — and the flushing comes from skin vessels dilating to lose the heat the patient can no longer sweat away."),
    ('b', "**Pupils: dilated in both.** Sympathetic stimulation contracts the dilator muscle; muscarinic block paralyses the constrictor. Two different routes lead to the same big pupil, which is why the pupils cannot separate them."),
    ('c', "**Bowel and bladder: normal in sympathomimetic; reduced bowel sounds and urinary retention in anticholinergic.** Gut movement and bladder emptying run on muscarinic receptors, so muscarinic block silences the bowel and retains urine. Feel for a full bladder and listen to the abdomen."),
    ('d', "**Delirium: sympathomimetic agitated and possibly violent; anticholinergic picking at the air with mumbling speech.** The sympathomimetic patient is wired and aggressive. The anticholinergic patient is confused, hallucinating, plucking at invisible objects and speaking unintelligibly."),
    ('e', "**Agents: sympathomimetic — amphetamines, cocaine, cathinones, pseudoephedrine; anticholinergic — atropine, antihistamines, tricyclics, datura, phenothiazines.** Datura (thorn apple) seeds contain atropine-like alkaloids. Tricyclics are anticholinergic as well as sodium-channel blockers, so a dry, dilated patient with a wide QRS points to a tricyclic (TOX-07)."),
  ],
  table=dict(title="Telling them apart at the bedside", head=["", "Sympathomimetic", "Anticholinergic"], rows=[["Temperature, HR, pupils", "↑ ↑ dilated", "↑ ↑ dilated"], ["Skin", "**wet**", "**dry, flushed**"], ["Bowel sounds, bladder", "normal", "reduced, retention"], ["Delirium", "agitated, violent", "picking at air, mumbling"]]),
  mimic=[
    ("Serotonin syndrome", "Also wet with dilated pupils — but adds tremor, hyperreflexia and clonus (TOX-05)."),
    ("Heat stroke", "Hot, tachycardic and confused with dry skin, but without anticholinergic pupils, retention or a drug history."),
  ],
  traps=[
    ("“Dilated pupils mean anticholinergic”", "Both toxidromes dilate the pupils; only skin, bowel and bladder separate them."),
    ("“Fever, tachycardia, mydriasis — anticholinergic”", "That triad is shared; look at the skin before answering."),
    ("“Cool the anticholinergic patient with an antipyretic”", "The heat comes from muscle activity and lost sweating, not a raised set point; cool physically and sedate with a benzodiazepine."),
  ],
  decode=[
    ("Agitated, hot, mydriatic and diaphoretic", "Sympathomimetic (cocaine, amphetamine)."),
    ("Hot, dry, flushed, urinary retention, picking at the air", "Anticholinergic (antihistamine, datura, tricyclic)."),
    ("Which single sign separates the two?", "The skin — wet or dry."),
  ],
  punch="Both run hot, fast and dilated; only the sympathomimetic can still sweat, because sweat glands work through muscarinic receptors — so the skin decides.",
)

L['TOX-04'] = dict(
  sub="Toxicology → Toxidromes → Opioid, sedative-hypnotic, cholinergic",
  intro="Three toxidromes give a sleepy or comatose patient, and two of them share small pupils. The first decision is the pupil; the second is the breathing and the secretions. Getting it right matters because each has a different antidote — naloxone for the opioid, atropine and pralidoxime for the organophosphate, and none for most sedatives.",
  parts=[
    ('a', "**Pupils: opioid pinpoint; sedative variable; cholinergic constricted.** Opioids remove inhibition of the parasympathetic (Edinger–Westphal) nucleus, so the pupil constricts to a pinpoint. Cholinergic poisons stimulate the muscarinic constrictor directly. Sedative-hypnotics have no consistent effect on the pupil."),
    ('b', "**Breathing: opioid slow, with apnoea; sedative slow or normal; cholinergic slow or fast.** Opioids depress the brainstem respiratory centre, so the rate falls first — the hallmark. Sedatives alone usually preserve breathing unless combined with alcohol or opioids. In cholinergic poisoning breathing fails from the airway (bronchorrhoea, bronchospasm) and the muscles (nicotinic weakness), so the rate can be either."),
    ('c', "**Skin: opioid variable; sedative variable; cholinergic wet.** Muscarinic stimulation turns on every secretion — sweat, saliva, tears and bronchial fluid — so the organophosphate patient is wet everywhere."),
    ('d', "**Extras: opioid — needle marks, pulmonary oedema; sedative — nystagmus; cholinergic — salivation, bronchorrhoea, fasciculation, diarrhoea.** Fasciculation is the nicotinic effect at the neuromuscular junction and is followed by weakness. Nystagmus is typical of the sedative group (and of phenytoin, ketamine and phencyclidine)."),
  ],
  table=dict(title="Coma with small pupils", head=["Finding", "Points to", "Treat with"], rows=[["Pinpoint + wet, bronchorrhoea, fasciculation", "**Organophosphate**", "atropine + pralidoxime"], ["Pinpoint + dry + very slow breathing", "**Opioid**", "naloxone"], ["Pinpoint, slow, no response to naloxone, bradycardia", "Clonidine", "supportive"]]),
  mimic=[
    ("Opioid vs clonidine", "Clonidine (a central α₂ agonist) copies opioid coma with miosis, bradycardia and hypotension, but naloxone reverses it inconsistently."),
    ("Opioid vs pontine haemorrhage", "Pinpoint pupils and coma with no response to naloxone — think of a structural cause."),
  ],
  traps=[
    ("“Pinpoint pupils and coma — give naloxone and it is settled”", "If there is no response, think clonidine, a mixed ingestion or a pontine bleed."),
    ("“Benzodiazepine overdose gives pinpoint pupils and apnoea”", "Pupils are variable and breathing is usually preserved, unless alcohol or opioids are added."),
    ("“Atropine is titrated to the pupils or the heart rate”", "In organophosphate poisoning it is titrated to drying of bronchial secretions."),
  ],
  decode=[
    ("Pinpoint pupils, wet, bronchorrhoea, fasciculations", "Organophosphate."),
    ("Pinpoint pupils, RR 6, needle marks", "Opioid."),
    ("Comatose, normal breathing, nystagmus", "Sedative-hypnotic."),
  ],
  punch="Pinpoint pupils narrow it to opioid or cholinergic, and the secretions decide: the opioid patient is dry with slow breathing, the organophosphate patient drowns in his own secretions.",
)

L['TOX-05'] = dict(
  sub="Toxicology → Toxidromes → Serotonin syndrome and hallucinogens",
  intro="Serotonin syndrome is a drug interaction more often than an overdose: a patient on one serotonergic drug is given a second, and within hours becomes agitated, sweaty and tremulous. It is diagnosed at the bedside, and the examination finding that defines it is in the reflexes. Hallucinogens, by contrast, change perception more than the body.",
  parts=[
    ('a', "**Tremor, hyperreflexia, clonus (worse in the legs), ocular clonus, diarrhoea, wet flushed skin, dilated pupils.** Excess serotonin over-stimulates 5-HT₂A receptors in the brainstem and spinal cord, producing neuromuscular excitation — tremor, then brisk reflexes, then inducible or spontaneous clonus, more in the legs than the arms. The same serotonin excess drives the autonomic signs: sweating, diarrhoea, tachycardia and mydriasis. Rising muscle activity generates heat; a temperature above 41 °C is life-threatening."),
    ('b', "**MAOIs, SSRIs and SNRIs, tricyclics, dextromethorphan, meperidine (pethidine), tramadol, linezolid.** These raise synaptic serotonin by different routes: less breakdown (MAOIs; linezolid is a weak MAOI), less reuptake (SSRIs, SNRIs, tricyclics, tramadol, pethidine, dextromethorphan). The dangerous combinations pair an MAOI with any of the reuptake blockers."),
    ('c', "**Hallucinogenic toxidrome: perceptual distortion, synaesthesia, depersonalisation; nystagmus with phencyclidine and ketamine. Agents: LSD, psilocybin, mescaline, MDMA.** These drugs alter perception (seeing sounds, feeling outside the body) with only mild sympathetic signs. Phencyclidine and ketamine are dissociative NMDA antagonists, which is why they add nystagmus."),
  ],
  mimic=[
    ("Serotonin syndrome vs neuroleptic malignant syndrome", "Serotonin: hours after the drug, clonus and brisk reflexes. NMS: days to develop, lead-pipe rigidity, slow reflexes, after a dopamine antagonist."),
    ("Serotonin syndrome vs anticholinergic", "Both are hot with dilated pupils, but the anticholinergic patient is dry with no clonus."),
  ],
  traps=[
    ("“Datura (belladonna) is serotonergic”", "It is anticholinergic: dry skin and no clonus."),
    ("“Paracetamol will bring the temperature down”", "The heat is muscular, not a reset thermostat; treat with benzodiazepines, cooling, cyproheptadine, and paralysis if severe."),
    ("“Rigidity with slow reflexes after an SSRI is serotonin syndrome”", "Slow reflexes and lead-pipe rigidity point to NMS; serotonin syndrome means clonus."),
  ],
  decode=[
    ("On an SSRI, given tramadol or linezolid; agitated, sweating, inducible clonus", "Serotonin syndrome."),
    ("Ocular clonus or lower-limb clonus", "Serotonin syndrome (Hunter criteria)."),
    ("Synaesthesia, depersonalisation, nystagmus after ketamine", "Hallucinogenic (dissociative) toxidrome."),
  ],
  punch="Serotonin excess shows in the reflexes — tremor, hyperreflexia and clonus, legs more than arms, on a wet, hot, dilated patient — and no clonus means think again.",
  extra=[dict(q="Serotonergic agents beyond the card’s list?", a="**Trazodone, cocaine, amphetamines, MDMA**, and opioids — **pethidine, tramadol, fentanyl**."),
         dict(q="SSRI overdose: the usual course, and the exception?", a="Usually benign (tachycardia, drowsiness, tremor). **Citalopram and escitalopram** prolong QTc and cause seizures.")],
)

L['TOX-06'] = dict(
  sub="Toxicology → Bedside clues → Odours",
  intro="Some poisons can be smelled on the breath, the skin or the vomit before any test is back. An odour is only a clue — many people cannot smell cyanide at all — but in an exam it is often the one word in the stem that names the poison.",
  parts=[
    ('a', "**Bitter almonds — cyanide.** Hydrogen cyanide has this smell; a genetic trait means a sizeable minority cannot detect it, so its absence excludes nothing."),
    ('b', "**Garlic — organophosphates, arsenic, phosphorus, thallium, selenium.** Sulphur- and phosphorus-containing compounds and some metals give a garlic smell. An organophosphate patient who is also wet with pinpoint pupils is the classic picture."),
    ('c', "**Rotten eggs — hydrogen sulphide.** Typical of sewers, manure pits and industrial accidents. At high concentrations it paralyses the sense of smell, so the odour can vanish as the danger rises."),
    ('d', "**Freshly mown hay — phosgene.** A choking gas that injures the alveoli, with pulmonary oedema that may be delayed by hours."),
    ('e', "**Mothballs — naphthalene; wintergreen — methyl salicylate; fruity or acetone — ethanol, isopropanol, salicylates; kerosene — organophosphates (the solvent).** Isopropanol is metabolised to acetone, which gives the fruity breath without acidosis. Oil of wintergreen is concentrated salicylate. Many organophosphate preparations are dissolved in a hydrocarbon solvent, hence the kerosene smell."),
  ],
  mimic=[
    ("Fruity breath: DKA vs isopropanol", "Both smell of acetone. DKA has a high anion gap acidosis; isopropanol gives ketosis with no acidosis and a raised osmolal gap."),
  ],
  traps=[
    ("“No almond smell, so not cyanide”", "Many people cannot smell it; rely on the lactate and the clinical picture."),
    ("“The rotten-egg smell has gone, so the exposure is over”", "Hydrogen sulphide paralyses smell at high concentration."),
  ],
  decode=[
    ("Bitter almonds", "Cyanide."),
    ("Garlic odour, wet, pinpoint pupils", "Organophosphate."),
    ("Rotten eggs in a sewer worker", "Hydrogen sulphide."),
  ],
  punch="An odour is a clue rather than a test — but in the stem it usually names the poison: almonds for cyanide, garlic for organophosphates and arsenic, rotten eggs for hydrogen sulphide.",
)

L['TOX-07'] = dict(
  sub="Toxicology → Bedside clues → ECG in poisoning",
  intro="The ECG is the quickest way to see whether a poison has reached the heart’s ion channels. The width of the QRS reflects how fast the sodium channels conduct the impulse through the ventricles; the length of the QT reflects how fast potassium channels repolarise them. Drugs that block those channels change the ECG long before the patient arrests.",
  parts=[
    ('a', "**QRS under 0.12 s (120 ms); QTc under 440 ms.** Ventricular depolarisation (phase 0) depends on fast sodium channels, and their speed is the QRS width. Repolarisation depends on potassium channels (hERG); block them and the QT lengthens. In a tricyclic overdose a QRS above 100 ms already counts as dangerous."),
    ('b', "**Tricyclic antidepressants, cocaine, carbamazepine — sodium-channel block — with ventricular tachycardia as the danger.** Blocking sodium channels slows conduction, so the QRS widens; slow, uneven conduction sets up re-entry circuits, which become ventricular tachycardia. A tricyclic adds a tall terminal R wave in aVR."),
    ('c', "**IV sodium bicarbonate, 1–2 mEq/kg.** Bicarbonate works in two ways: the sodium load helps push current through the partly blocked channels, and the alkalosis reduces how tightly the drug binds to them. The bolus is repeated until the QRS narrows, aiming for a blood pH of about 7.45–7.55."),
    ('d', "**Class Ia and Ic anti-arrhythmics are avoided.** Procainamide, flecainide and their relatives are sodium-channel blockers themselves; adding them deepens the same block and can turn a wide QRS into asystole or VT."),
    ('e', "**Bradycardia or AV block: beta-blockers, calcium-channel blockers, digoxin, cholinergics, opioids, lithium, magnesium, sedative-hypnotics.** These act on the sinus and AV nodes rather than the ventricles: beta- and calcium-channel block directly, digoxin and cholinergics through vagal tone, the rest by central depression or membrane effects."),
  ],
  table=dict(title="What the ECG change points to", head=["Change", "Channel", "Think of"], rows=[["Wide QRS, R in aVR", "Na⁺ block", "tricyclic, cocaine, carbamazepine"], ["Long QT", "K⁺ (hERG) block", "antipsychotics, antihistamines, sotalol, ondansetron, organophosphates"], ["Bradycardia, AV block", "nodes", "β-blocker, CCB, digoxin"], ["SVT", "catecholamine excess", "sympathomimetic, anticholinergic, thyroid, withdrawal"]]),
  mimic=[
    ("Wide QRS vs long QT", "A wide QRS is sodium-channel block and is treated with bicarbonate; a long QT is potassium-channel block, treated by stopping the drug and giving magnesium and potassium."),
  ],
  traps=[
    ("“Wide-complex tachycardia after a tricyclic — give procainamide or flecainide”", "They are sodium-channel blockers too; give sodium bicarbonate."),
    ("“QRS 110 ms is normal, so the tricyclic overdose is safe”", "Above 100 ms predicts seizures in a tricyclic overdose; QRS width, not the dose, grades the risk."),
    ("“Calcium or glucagon will fix the wide QRS”", "They do not reverse sodium-channel block; bicarbonate does."),
  ],
  decode=[
    ("TCA overdose with QRS 140 ms and hypotension", "IV sodium bicarbonate 1–2 mEq/kg."),
    ("Which anti-arrhythmics are avoided?", "Class Ia and Ic."),
    ("Overdose with bradycardia and AV block", "Nodal agents — β-blocker, calcium-channel blocker, digoxin."),
  ],
  punch="Sodium channels set the QRS width: block them and it widens toward VT. Bicarbonate pushes through the block, and class Ia and Ic drugs add to it — wide means sodium, slow means the nodes.",
  extra=[dict(q="TCA overdose: what grades the risk?", a="**QRS width** — ≥100 ms seizures, ≥160 ms ventricular arrhythmia — not the dose or the level."),
         dict(q="Which β-blocker overdose behaves like a TCA?", a="**Propranolol** (sodium-channel block): wide QRS and seizures → **sodium bicarbonate**.")],
  before="You skipped TOX-06, the odours card. In brief: bitter almonds mean cyanide, garlic means organophosphates or arsenic, rotten eggs mean hydrogen sulphide, and wintergreen means methyl salicylate.",
)

L['TOX-08'] = dict(
  sub="Toxicology → Bedside clues → Osmolal and saturation gaps",
  intro="A ‘gap’ is a mismatch between what is measured and what is expected. When the lab measures more particles in the blood than a formula predicts, or the oximeter shows a saturation that does not fit the blood gas, something unusual is present. Both gaps point to a short list of poisons, and the radio-opaque list tells you which tablets an X-ray can see.",
  parts=[
    ('a', "**Calculated osmolality = 2 × Na + glucose/18 + BUN/2.8; the gap is measured minus calculated, normally under 10.** The formula counts only the main particles: sodium with its anions (hence ×2), glucose and urea (divided to convert mg/dL to mmol/L). Anything else dissolved in the blood is measured by the lab but missed by the formula, and shows up as the gap."),
    ('b', "**Methanol, ethylene glycol, ethanol, isopropanol, acetone, propylene glycol, mannitol, glycerol, sorbitol.** These are small, uncharged molecules present in large amounts, so they raise measured osmolality. Ethanol is the commonest cause; the toxic alcohols are the dangerous ones."),
    ('c', "**Saturation gap over 5%: carbon monoxide, methaemoglobin, cyanide, hydrogen sulphide, sulphaemoglobin.** A pulse oximeter uses only two wavelengths and assumes only oxyhaemoglobin and deoxyhaemoglobin exist. Carboxyhaemoglobin looks like oxyhaemoglobin, so SpO₂ reads falsely normal; methaemoglobin drags the reading toward about 85%. Cyanide and hydrogen sulphide block the cells’ use of oxygen, so venous blood stays bright and oxygen-rich. A co-oximeter measures the abnormal haemoglobins directly."),
    ('d', "**Radio-opaque: chloral hydrate, calcium, heavy metals, iron, iodides, psychotropics, packets, potassium, enteric-coated and sustained-release preparations, salicylates.** These contain dense atoms (metals, iodine, potassium, chlorine) or are compact tablets and packets that hold together. Iron tablets and drug packets in body packers are the practical uses of an abdominal X-ray."),
  ],
  table=dict(title="A normal SpO₂ that is wrong", head=["Poison", "SpO₂", "PaO₂", "Clue"], rows=[["Carbon monoxide", "falsely normal", "normal", "COHb on co-oximetry"], ["Methaemoglobin", "drifts toward ~85%", "normal", "chocolate blood, cyanosis despite O₂"], ["Cyanide", "normal", "normal", "high venous O₂, high lactate"]]),
  mimic=[
    ("Osmolal gap vs anion gap", "The osmolal gap is high early, while the alcohol itself is in the blood; as it is metabolised to acids the osmolal gap falls and the anion gap rises. A late presenter can have a normal osmolal gap."),
  ],
  traps=[
    ("“Normal SpO₂ and PaO₂ exclude carbon monoxide poisoning”", "Both miss carboxyhaemoglobin; only co-oximetry measures it."),
    ("“A normal osmolal gap excludes methanol”", "Not in a late presenter: the alcohol has already become acid (high anion gap)."),
    ("“Cyanide lowers the SpO₂”", "SpO₂ and PaO₂ stay normal; the high lactate and high venous oxygen give it away."),
  ],
  decode=[
    ("Raised osmolal gap and high anion gap acidosis", "Methanol or ethylene glycol."),
    ("SpO₂ 85% that does not rise with oxygen, normal PaO₂", "Methaemoglobinaemia."),
    ("Fire victim, SpO₂ 99%, confused", "Carbon monoxide (co-oximetry)."),
  ],
  punch="A gap means the lab sees something the formula or the oximeter cannot — an extra osmole in the blood, or a haemoglobin that is not carrying oxygen.",
  extra=[dict(q="Raised osmolal gap: how does the anion gap split it?", a="**Normal anion gap** → isopropanol (acetone), mannitol. **High anion gap** → methanol, ethylene glycol.")],
)

L['TOX-09'] = dict(
  sub="Toxicology → Decontamination and elimination → Gut decontamination",
  intro="Decontamination tries to stop absorption of a poison that is still in the gut. It only helps while the drug is there, only if the method can bind or move it, and never at the cost of aspiration. So each method has a time window, a list of drugs it works for, and a protected airway as its precondition.",
  parts=[
    ('a', "**Activated charcoal within 1 hour, in an awake patient with a protected airway.** Charcoal has a huge surface that binds most organic drug molecules in the gut lumen. After about an hour most drugs have been absorbed, so the benefit falls away. Aspirating charcoal causes severe pneumonitis, hence the airway condition."),
    ('b', "**Multi-dose charcoal: carbamazepine, theophylline, dapsone, quinine, phenobarbital.** Repeated doses keep the gut lumen empty of free drug, so drug already in the blood diffuses back across the gut wall and is bound — often called gut dialysis. It also breaks the cycle for drugs that undergo enterohepatic recirculation."),
    ('c', "**Whole bowel irrigation: polyethylene glycol at 1500–2000 mL/h until the rectal effluent is clear; for iron, lithium, sustained-release or enteric-coated drugs, and body packers.** The large volume of an isotonic, non-absorbed solution flushes tablets through the gut before they dissolve. It is used for what charcoal cannot bind (iron and lithium, which are ions) and for slow-release tablets that keep releasing drug for hours."),
    ('d', "**Induced emesis is not recommended — it is ineffective and risks aspiration.** Ipecac removes little drug, delays charcoal and is dangerous if consciousness falls."),
  ],
  table=dict(title="Which method for which poison", head=["Problem", "Method"], rows=[["Most organic drugs, <1 h", "single-dose charcoal"], ["Carbamazepine, theophylline, dapsone, quinine, phenobarbital", "multi-dose charcoal"], ["Iron, lithium, slow-release, packets", "whole bowel irrigation"], ["Corrosives, hydrocarbons, unprotected airway", "no gut decontamination"]]),
  mimic=[
    ("Multi-dose charcoal vs urine alkalinisation", "Multi-dose charcoal pulls drug back into the gut (carbamazepine, theophylline); alkalinisation traps weak acids in the urine (salicylate, phenobarbital)."),
  ],
  traps=[
    ("“Charcoal for lithium or iron”", "Ions are not bound by charcoal; use whole bowel irrigation."),
    ("“Altered sensorium is an absolute contraindication to decontamination”", "Not once the airway is protected; corrosives, hydrocarbons and an unprotected airway are."),
    ("“Charcoal is useful at 6 hours for any drug”", "The window is about 1 hour; paracetamol within 2 hours (up to 4 h only for massive or modified-release ingestions)."),
  ],
  decode=[
    ("Sustained-release or iron overdose — decontamination?", "Whole bowel irrigation."),
    ("Carbamazepine or theophylline toxicity, rising level", "Multi-dose activated charcoal."),
    ("Ipecac or induced vomiting?", "Not recommended."),
  ],
  punch="Decontaminate only what is still in the gut and can be bound or flushed out — charcoal binds organic molecules, metals and ions slip through, and the airway always comes first.",
  extra=[dict(q="Gastric lavage: when, if ever?", a="Not routine. Only within **~1 h** of a potentially lethal ingestion that charcoal does not bind or has no antidote — with a **protected airway**.")],
)

L['TOX-10'] = dict(
  sub="Toxicology → Decontamination and elimination → Urine alkalinisation",
  intro="The kidney filters many drugs, but most are then reabsorbed back into the blood as they pass down the tubule. Only the un-ionised (uncharged) form of a drug can cross the tubular wall. Change the urine pH so the drug becomes ionised, and it is trapped in the urine and excreted — this is ion trapping.",
  parts=[
    ('a', "**Urine pH ≥7.5, using IV sodium bicarbonate.** Bicarbonate is excreted by the kidney and raises urine pH. For a weak acid, each unit of pH above its pKa makes it about ten times more ionised, so a small rise in pH greatly increases excretion."),
    ('b', "**Weak acids that are renally eliminated and poorly protein-bound.** Only a weak acid is ionised by alkaline urine. The drug must be cleared mainly by the kidney for this route to matter, and must be free in plasma to be filtered at all."),
    ('c', "**Salicylates, methotrexate, phenobarbital, 2,4-D (a herbicide), chlorpropamide.** Salicylate is the main indication. Alkalinising the blood has a second benefit: it keeps salicylate ionised in the plasma, so less enters the brain."),
    ('d', "**Monitor urine pH and electrolytes, especially potassium.** Bicarbonate drives potassium into cells and increases its loss in urine. When potassium is low the kidney holds on to it by secreting hydrogen ions instead, so the urine stays acid however much bicarbonate is given."),
    ('e', "**Renal failure is the contraindication.** A failing kidney cannot filter the drug or handle the sodium load, so alkalinisation achieves nothing and risks fluid overload. Severe salicylate poisoning with renal failure goes to haemodialysis (TOX-11)."),
  ],
  mimic=[
    ("Alkalinisation for salicylate vs bicarbonate for tricyclics", "In salicylate poisoning bicarbonate traps the drug in urine; in tricyclic poisoning it overcomes sodium-channel block in the heart. Same drug, different reason."),
  ],
  traps=[
    ("“Bicarbonate alone will alkalinise the urine”", "Not if potassium is low — correct K⁺ first."),
    ("“Alkalinisation works for weak bases such as amphetamines”", "Alkaline urine traps acids; it does not help bases."),
    ("“Intubate the salicylate patient and ventilate normally”", "Losing the patient’s hyperventilation lets the blood become acid and drives salicylate into the brain; match the high minute ventilation."),
  ],
  decode=[
    ("Salicylate poisoning, urine pH 6 despite bicarbonate", "Correct hypokalaemia."),
    ("Which toxins qualify for alkalinisation?", "Weak acids, renally cleared, low protein binding — salicylate, phenobarbital, methotrexate."),
    ("Target urine pH", "≥7.5."),
  ],
  punch="An acid is trapped in base: alkaline urine ionises the weak acid so it cannot be reabsorbed — and without enough potassium the kidney will not let the urine turn alkaline.",
)

L['TOX-11'] = dict(
  sub="Toxicology → Decontamination and elimination → Extracorporeal removal",
  intro="Dialysis cleans the blood, so it can only remove a drug that is actually in the blood, free to cross the membrane. A drug that is bound to plasma proteins, or that has spread out into fat and tissues, is beyond its reach. Three properties of the molecule therefore decide whether dialysis is worth starting.",
  parts=[
    ('a', "**Low molecular weight, low protein binding, small volume of distribution (the drug stays in the extracellular fluid).** A small molecule crosses the dialysis membrane. An unbound molecule is free in plasma rather than carried on albumin. A small volume of distribution means most of the body’s load is in the blood, so cleaning the blood empties the body."),
    ('b', "**Haemodialysis removes salicylates, lithium, methanol, ethylene glycol and isopropanol.** All are small and poorly bound, and dialysis also corrects the acidosis and removes toxic metabolites (formate, glycolate). Lithium is the model dialysable toxin — tiny, unbound and confined to body water."),
    ('c', "**Haemoperfusion: barbiturates, carbamazepine, theophylline, valproate — over a charcoal or resin adsorbent.** These are more protein-bound, so dialysis removes little. In haemoperfusion the blood passes over an adsorbent that strips the drug off the protein. Modern high-flux dialysis has narrowed the difference, but the exam list stands."),
  ],
  table=dict(title="Why each property matters", head=["Property", "Why it matters"], rows=[["Low molecular weight", "crosses the membrane"], ["Low protein binding", "free in plasma, not carried by albumin"], ["Small volume of distribution", "most of the body load is in the blood"]]),
  mimic=[
    ("Haemodialysis vs haemoperfusion", "Dialysis needs a free, small drug; haemoperfusion can take drug off protein."),
  ],
  traps=[
    ("“Calcium-channel blockers and beta-blockers are dialysed”", "Most are protein-bound or widely distributed; only atenolol and sotalol are dialysable."),
    ("“Digoxin is removed by dialysis”", "Its volume of distribution is very large; Fab fragments are the treatment."),
    ("“Tricyclics can be dialysed”", "Highly protein-bound with a huge volume of distribution — dialysis does not help."),
  ],
  decode=[
    ("Which toxin is best removed by haemodialysis?", "Lithium, salicylate, methanol, ethylene glycol."),
    ("Properties of a dialysable toxin", "Small, unbound, small volume of distribution."),
    ("Theophylline or carbamazepine toxicity, extracorporeal method", "Haemoperfusion (or high-flux dialysis)."),
  ],
  punch="Dialysis can reach only what is small, free and in the blood; a protein-bound drug needs an adsorbent, and a drug hidden in the tissues cannot be dialysed at all.",
  extra=[dict(q="Salicylate: when to dialyse?", a="Level **>100 mg/dL**, worsening CNS signs, renal failure, acute lung injury, or severe acidosis despite treatment."),
         dict(q="Carbamazepine: severe toxicity level, and what tips a stable patient over?", a="**Above 40 µg/mL**; CYP3A4 inhibitors (diltiazem, isoniazid, macrolides); valproate raises the toxic epoxide.")],
)

L['TOX-12'] = dict(
  sub="Toxicology → Decontamination and elimination → Supportive care",
  intro="Most poisoned patients survive on good supportive care rather than an antidote. The usual emergency drugs mostly work here too — with one rule added: do not give a drug that does the same harm as the poison. That rule explains every choice on this card.",
  parts=[
    ('a', "**Hypertension: a calcium-channel blocker, phentolamine, labetalol or nitroprusside.** Toxic hypertension is usually catecholamine excess (cocaine, amphetamines). A benzodiazepine to calm the sympathetic storm comes first; then a vasodilator. Phentolamine blocks α-receptors directly. A pure beta-blocker is avoided because it leaves α-stimulation unopposed."),
    ('b', "**Seizures: benzodiazepines, then barbiturates.** Toxic seizures are treated by strengthening GABA-A inhibition. Phenytoin is avoided — it rarely works for toxic seizures and is itself a sodium-channel blocker, which is dangerous in tricyclic or other sodium-channel poisoning."),
    ('c', "**Ventricular tachycardia: sodium bicarbonate; avoid class Ia and Ic.** Toxic VT is usually sodium-channel block (TOX-07), so bicarbonate treats the cause and sodium-channel anti-arrhythmics would deepen it."),
    ('d', "**Bradyarrhythmia: atropine and pacing.** Atropine blocks vagal slowing; pacing supports the rate while the specific antidote (digoxin Fab, high-dose insulin, glucagon — TOX-14) takes effect."),
    ('e', "**Hyperthermia: active cooling.** Toxic hyperthermia comes from muscle activity and failed heat loss, with a normal hypothalamic set point, so antipyretics do not work. Cool externally, sedate, and paralyse and ventilate if the temperature keeps rising."),
  ],
  mimic=[
    ("Toxic seizure vs epileptic seizure", "Both get benzodiazepines first, but phenytoin, a standard second-line drug in epilepsy, is avoided in poisoning."),
  ],
  traps=[
    ("“Beta-blocker for cocaine-induced hypertension”", "It leaves α unopposed; benzodiazepine first, then a vasodilator. Labetalol is a later, debated option — never the first answer."),
    ("“Phenytoin for a tricyclic seizure”", "Another sodium-channel blocker, and ineffective; use benzodiazepines then barbiturates."),
    ("“Paracetamol for drug-induced hyperthermia”", "The set point is normal; cool actively."),
  ],
  decode=[
    ("Cocaine chest pain and BP 200/120 — first drug?", "Benzodiazepine."),
    ("Status epilepticus after an overdose, benzodiazepines failed", "Barbiturate (phenobarbital) or propofol — not phenytoin."),
    ("Temperature 41 °C after amphetamine", "Active cooling, sedation, paralysis if needed."),
  ],
  punch="Toxic emergencies get the usual tools minus the ones the poison already uses: benzodiazepines first, no phenytoin, no class Ia or Ic, and cooling rather than antipyretics.",
)

L['TOX-13'] = dict(
  sub="Toxicology → Antidotes → Toxin to antidote (1)",
  intro="An antidote works by undoing the poison’s one key move. Some refill what the poison uses up, some push it off its receptor, some block the enzyme that makes it toxic, and some bind it so it cannot act. If you know the poison’s move, you can work out the antidote — and the reason for its dose.",
  parts=[
    ('a', "**Paracetamol — N-acetylcysteine.** Paracetamol becomes toxic when its metabolite NAPQI exhausts the liver’s glutathione. N-acetylcysteine refills glutathione so NAPQI is detoxified."),
    ('b', "**Opioids — naloxone, 0.04–2 mg.** Naloxone competes the opioid off the μ receptor. Small doses restore breathing in the opioid-dependent without provoking severe withdrawal; larger doses for apnoea."),
    ('c', "**Organophosphate — atropine plus pralidoxime 1–2 g over 30 minutes.** Organophosphates inhibit acetylcholinesterase, so acetylcholine floods every synapse. Atropine blocks the muscarinic excess (secretions, bronchospasm, bradycardia) and is titrated to dry chest secretions. Pralidoxime reactivates the enzyme, but only before the bond ‘ages’ and becomes permanent."),
    ('d', "**Methanol, ethylene glycol — fomepizole 15 mg/kg over 30 minutes, then 10 mg/kg 12-hourly for four doses, then 15 mg/kg 12-hourly.** The alcohols are harmless; their acids (formic acid, glycolate and oxalate) kill. Fomepizole blocks alcohol dehydrogenase so the acids are not made. The dose rises after 48 hours because fomepizole induces its own metabolism."),
    ('e', "**Carbon monoxide — 100% oxygen, hyperbaric in some.** Oxygen competes CO off haemoglobin and shortens the COHb half-life from about 4 hours on air to about 1 hour on 100% oxygen, and further under hyperbaric pressure."),
    ('f', "**Cyanide — sodium nitrite 300 mg IV (hydroxocobalamin 5 g is now first choice).** Nitrite turns some haemoglobin into methaemoglobin, which pulls cyanide off cytochrome oxidase; thiosulphate then converts it to thiocyanate. Hydroxocobalamin binds cyanide directly to form cyanocobalamin, without creating methaemoglobin."),
    ('g', "**Methaemoglobinaemia — methylene blue 1–2 mg/kg.** It is reduced to leucomethylene blue, which converts methaemoglobin back to haemoglobin. The reaction needs NADPH from the G6PD pathway, so it fails — and can cause haemolysis — in G6PD deficiency."),
    ('h', "**Iron — deferoxamine, up to 15 mg/kg/h.** Deferoxamine chelates free iron into ferrioxamine, which is excreted in the urine and turns it a vin-rosé colour."),
  ],
  table=dict(title="Each antidote undoes one move", head=["Antidote", "Its move"], rows=[["N-acetylcysteine", "refills glutathione to detoxify NAPQI"], ["Naloxone", "pushes the opioid off the μ receptor"], ["Atropine + pralidoxime", "blocks muscarinic excess; reactivates AChE before ageing"], ["Fomepizole", "blocks alcohol dehydrogenase → no toxic acids"], ["100% O₂", "displaces CO, shortens COHb half-life"], ["Nitrite / hydroxocobalamin", "pulls cyanide off cytochrome oxidase / binds it"], ["Methylene blue", "reduces MetHb back to Hb"], ["Deferoxamine", "chelates free iron"]]),
  mimic=[
    ("Cyanide antidotes in a fire victim", "Nitrite makes methaemoglobin, which worsens oxygen carriage when CO is also present; hydroxocobalamin does not."),
  ],
  traps=[
    ("“Methylene blue for every methaemoglobinaemia”", "Not in G6PD deficiency — it fails and causes haemolysis."),
    ("“Atropine until the pupils dilate or the heart rate is 120”", "Titrate to drying of bronchial secretions."),
    ("“Pralidoxime can be given at any time”", "It works only before the enzyme–organophosphate bond ages."),
  ],
  decode=[
    ("Methanol with visual blurring — antidote?", "Fomepizole (and dialysis for visual signs)."),
    ("Chocolate-brown blood, SpO₂ 85% after benzocaine spray", "Methylene blue 1–2 mg/kg."),
    ("House-fire victim with high lactate", "Hydroxocobalamin 5 g."),
  ],
  punch="Each antidote undoes the toxin’s one move — refill what it uses up, push it off the receptor, block the enzyme that makes it toxic, or bind it — so name the move and the antidote follows.",
  extra=[dict(q="Methanol vs ethylene glycol: what separates them?", a="Their acid. **Methanol → formic acid** → eyes (snowstorm vision, blindness), putamen. **Ethylene glycol → oxalate** → crystals, hypocalcaemia, AKI at 24–72 h."),
         dict(q="CO: COHb half-life on air, 100% O₂, hyperbaric?", a="About **4 h · 1 h · 20–30 min**.")],
)

L['TOX-14'] = dict(
  sub="Toxicology → Antidotes → Toxin to antidote (2)",
  intro="Cardiotoxic poisons shut down the heart’s channels, receptors or fuel supply. The antidotes on this card do not usually reverse the poison itself; most go around the blocked step — feeding the heart another way, raising its second messengers through a different receptor, or pulling the drug out of the tissue.",
  parts=[
    ('a', "**Digoxin — digoxin-specific Fab: 10–20 vials in acute poisoning, 3–6 in chronic.** Fab fragments bind digoxin directly and the complex is excreted. Acute overdoses carry a large body load, hence more vials; chronic toxicity usually needs only a few."),
    ('b', "**Calcium-channel blocker — high-dose insulin 0.5–1 U/kg/h with dextrose; lipid emulsion.** A poisoned heart switches from fatty acids to glucose but cannot take glucose up, because the drug also blocks insulin release. High-dose insulin lets the myocardium use glucose and restores contractility; dextrose is run alongside to prevent hypoglycaemia. Lipid is a rescue for refractory cases."),
    ('c', "**Beta-blocker — atropine; glucagon; high-dose insulin.** Glucagon raises cAMP through its own receptor, bypassing the blocked β-receptor, and increases heart rate and contractility. Atropine treats the bradycardia; insulin supports the failing myocardium as in calcium-channel blocker poisoning."),
    ('d', "**Tricyclic antidepressant — sodium bicarbonate 1–2 mEq/kg; lipid.** Bicarbonate overcomes the sodium-channel block (TOX-07). Lipid emulsion is a rescue for refractory cardiotoxicity, because tricyclics are lipophilic."),
    ('e', "**Sulfonylurea — octreotide 50 µg SC 6-hourly with dextrose.** Sulfonylureas close the β-cell potassium channel and force insulin release. Dextrose alone triggers more insulin and rebound hypoglycaemia; octreotide stops the release."),
    ('f', "**Benzodiazepine — flumazenil, rarely, because of the seizure risk.** It is reserved for pure benzodiazepine sedation in a non-dependent patient, such as procedural over-sedation (TOX-01)."),
    ('g', "**Local anaesthetic — 20% lipid emulsion.** The lipid creates a fat phase in plasma into which the lipophilic drug partitions out of the heart (TOX-15)."),
  ],
  table=dict(title="How each antidote goes around the block", head=["Antidote", "Mechanism"], rows=[["Digoxin Fab", "binds digoxin itself"], ["High-dose insulin", "lets the poisoned heart use glucose"], ["Glucagon", "raises cAMP through its own receptor, bypassing β"], ["Bicarbonate", "Na⁺ load and alkalosis overcome Na⁺-channel block"], ["Octreotide", "stops the pancreas releasing insulin"], ["Lipid emulsion", "pulls lipophilic drug out of the heart"]]),
  mimic=[
    ("Calcium-channel blocker vs beta-blocker poisoning", "Both give bradycardia and hypotension. Calcium-channel blockers cause hyperglycaemia (insulin release blocked); beta-blockers more often give hypoglycaemia. Propranolol also widens the QRS."),
  ],
  traps=[
    ("“Sulfonylurea overdose — give dextrose and wait”", "Dextrose triggers more insulin and rebound hypoglycaemia; octreotide stops it."),
    ("“IV calcium will correct heart rate and AV block in verapamil overdose”", "Calcium reliably improves contractility and blood pressure, but is least likely to change heart rate."),
    ("“Dialyse the digoxin”", "Its volume of distribution is huge; Fab is the treatment."),
  ],
  decode=[
    ("Verapamil overdose, shock despite calcium and pressors", "High-dose insulin euglycaemia therapy."),
    ("Recurrent hypoglycaemia after glibenclamide", "Octreotide."),
    ("8 mg digoxin ingested — vials of Fab?", "8 × 0.8 ÷ 0.5 ≈ 13 vials."),
  ],
  punch="When a drug shuts down the heart’s channels or fuel, the antidote goes around the blocked step: insulin refuels the myocardium, glucagon skips the β-receptor, and octreotide stops the insulin a sulfonylurea forces out.",
  extra=[dict(q="TCA seizures: first drug, and the one to avoid?", a="**Benzodiazepines** first (then phenobarbital or propofol); **avoid phenytoin** — another sodium-channel blocker.")],
)

L['TOX-15'] = dict(
  sub="Toxicology → Antidotes → Lipid emulsion for local anaesthetic toxicity",
  intro="Bupivacaine and other local anaesthetics are lipophilic and bind tightly to cardiac sodium channels; an accidental intravascular dose can cause seizures and then cardiac arrest that resists standard resuscitation. A 20% lipid emulsion creates a fat phase in the blood into which the drug moves out of the heart, and also gives the myocardium fuel. The doses are by weight, with a ceiling, and resuscitation itself is modified.",
  parts=[
    ('a', "**Bolus: 20% lipid 1.5 mL/kg over 2–3 minutes (100 mL if over 70 kg).** The bolus quickly builds a lipid sink in plasma so the drug can partition out of the heart."),
    ('b', "**Infusion: 0.25 mL/kg/min (200–250 mL over 15–20 minutes if over 70 kg). If still unstable, repeat the bolus once or twice and double the rate.** The infusion keeps the lipid level up while the drug is redistributed and cleared."),
    ('c', "**Maximum dose: 12 mL/kg.** Larger lipid loads risk pancreatitis, fat overload, lung injury and interference with laboratory tests."),
    ('d', "**Changes to resuscitation: adrenaline boluses ≤1 µg/kg; avoid vasopressin, calcium-channel blockers, beta-blockers and lidocaine; benzodiazepines for seizures, avoiding large doses of propofol.** Large adrenaline doses worsen arrhythmia and blunt the lipid response. Lidocaine is another local anaesthetic. Calcium-channel blockers and beta-blockers depress a heart that is already failing, and large propofol doses do the same."),
    ('e', "**Monitoring: 4–6 hours after a cardiovascular event; 2 hours after a CNS-only event.** As the lipid is cleared, the drug can move back from fat into plasma and the heart, so toxicity can recur."),
  ],
  table=dict(title="Lipid dosing", head=["Step", "Dose"], rows=[["Bolus", "**1.5 mL/kg** over 2–3 min"], ["Infusion", "**0.25 mL/kg/min**"], ["Still unstable", "repeat bolus ×1–2, double rate"], ["Ceiling", "**12 mL/kg**"]]),
  mimic=[
    ("LAST resuscitation vs standard ACLS", "Smaller adrenaline doses, no vasopressin, and no lidocaine for the arrhythmia."),
  ],
  traps=[
    ("“Standard 1 mg adrenaline boluses”", "Use small boluses, ≤1 µg/kg."),
    ("“Lidocaine for the ventricular arrhythmia”", "It is another local anaesthetic and adds to the toxicity."),
    ("“Patient stable after lipid — discharge to the ward at once”", "Monitor 4–6 hours after a cardiovascular event: toxicity can recur."),
  ],
  decode=[
    ("Maximum lipid dose", "12 mL/kg."),
    ("Bolus for a 60 kg patient", "90 mL (1.5 mL/kg) over 2–3 min."),
    ("Which drugs are avoided in LAST resuscitation?", "Vasopressin, calcium-channel blockers, beta-blockers, lidocaine."),
  ],
  punch="Lipid soaks the fat-soluble drug out of the heart, so it is dosed by weight with a ceiling of 12 mL/kg — and resuscitation changes with it: small adrenaline doses and no extra local anaesthetic.",
  extra=[dict(q="Lipid emulsion beyond local anaesthetics?", a="Rescue for **lipophilic cardiotoxins** — propranolol, verapamil/diltiazem, TCAs — after standard antidotes fail; **VA-ECMO** is the next step.")],
)

L['TOX-16'] = dict(
  sub="Toxicology → Revision → True or false",
  intro="This card tests the deck’s key distinctions. Each statement is either true or turns on one detail from an earlier card; the reason for each answer is the mechanism you met there.",
  parts=[
    ('a', "**False — anticholinergic skin is dry.** Sweat glands work through muscarinic receptors, so blocking them stops sweating (TOX-03)."),
    ('b', "**True — bitter almonds suggest cyanide** (TOX-06), though many people cannot smell it."),
    ('c', "**False — lithium is not bound by charcoal; use whole bowel irrigation.** Charcoal binds organic molecules; ions such as lithium and iron slip through (TOX-09)."),
    ('d', "**True — urine alkalinisation is used for salicylates.** A weak acid is ionised and trapped in alkaline urine (TOX-10)."),
    ('e', "**False — a tricyclic wide QRS is treated with bicarbonate; avoid class Ia drugs such as procainamide.** Procainamide is itself a sodium-channel blocker (TOX-07)."),
    ('f', "**True — octreotide treats sulfonylurea overdose** by stopping insulin release (TOX-14)."),
    ('g', "**True — the maximum lipid emulsion dose is 12 mL/kg** (TOX-15)."),
    ('h', "**True — methanol raises the osmolal gap,** early, before it is metabolised to formic acid (TOX-08)."),
  ],
  mimic=[],
  traps=[
    ("“Charcoal binds everything”", "Not metals, ions or alcohols."),
    ("“Any anti-arrhythmic will do for a toxic wide QRS”", "Class Ia and Ic deepen sodium-channel block."),
  ],
  decode=[
    ("Statements about skin in toxidromes", "Check sweat: wet sympathomimetic, dry anticholinergic."),
    ("Statements about decontamination", "Ask whether charcoal can bind the toxin."),
  ],
  punch="Every statement here turns on a mechanism from earlier in the deck — the sweat gland’s muscarinic receptor, what charcoal can bind, ion trapping, and sodium-channel block.",
)
