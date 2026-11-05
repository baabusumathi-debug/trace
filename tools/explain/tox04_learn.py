# TOX04 — Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Deck: Recreational Drugs & Hyperthermic Toxidromes (REC-01 to REC-15). Same fields as tox01_learn.py.
# Audited 6 Nov against qpack/TOX04.md (66 real questions): see tox04_audit.md.
L = {}

L['REC-01'] = dict(
  sub="Toxicology → Cannabis & Opioids → Substance use in India",
  intro="The figures come from the 2019 national survey of substance use in India (NDDTC, AIIMS), which counted current users aged 10–75. Alcohol far outnumbers everything else, opioid use is well above the world rate, and children have a pattern of their own.",
  parts=[
    ('a', "**Alcohol, 14.6%.** About one in seven Indians aged 10–75 is a current drinker — which is why alcohol withdrawal and alcohol-related liver disease are the commonest substance problems on the ward."),
    ('b', "**Cannabis 2.8%, then opioids 2.1%.** Cannabis is cheap and culturally familiar (bhang), so it comes second. Opioids come third, but at 2.1% Indian use is about three times the global figure (0.7%), and heroin has overtaken opium as the commonest opioid."),
    ('c', "**Inhalants.** Glue, whitener and solvent sprays are cheap, legal and easy to hide. The survey’s point is that inhalants are the one class used more by children and adolescents than by adults — not that they are children’s commonest substance overall."),
  ],
  mimic=[],
  traps=[
    ("“Cannabis is the commonest substance used in India”", "Alcohol is far ahead at 14.6%; cannabis is second at 2.8%."),
    ("“Opioid use in India is below the world average”", "It is about three times the global figure — 2.1% vs 0.7%."),
  ],
  decode=[
    ("Commonest substance of abuse in India (national survey) [pattern]", "Alcohol."),
    ("Substance used more by children than by adults [pattern]", "Inhalants."),
  ],
  punch="Alcohol dominates Indian substance use, cannabis and opioids follow — with opioid use three times the world rate — and inhalants are the drug of children.",
)

L['REC-02'] = dict(
  sub="Toxicology → Cannabis & Opioids → Cannabis",
  intro="Cannabis acts on the body’s own endocannabinoid receptors, which fine-tune neurotransmitter release. They sit mainly in the brain and hardly at all in the brainstem respiratory centres, so plain cannabis disturbs the mind but spares breathing, and its treatment is supportive. A seizing, hyperthermic ‘cannabis’ user has usually taken a synthetic cannabinoid.",
  parts=[
    ('a', "**Delta-9-tetrahydrocannabinol.** THC is the main psychoactive cannabinoid. It is highly lipid-soluble, stored in fat and released slowly, which is why a chronic user stays urine-positive for weeks (TOX-02)."),
    ('b', "**CB1: CNS (basal ganglia, cerebellum, hypothalamus). CB2: periphery (spleen, immune cells).** CB1 receptors on presynaptic terminals dampen transmitter release, and their distribution matches the effects — incoordination (basal ganglia, cerebellum), appetite (hypothalamus), memory (hippocampus). CB1 is scarce in the brainstem, so cannabis alone does not stop breathing. CB2 modulates inflammation."),
    ('c', "**Bhang (crushed leaves), ganja and charas (smoked), hashish (resin of flowering tops).** Bhang is drunk or eaten, so it acts slowly and for longer; resins are concentrated and carry more THC per gram."),
    ('d', "**Supportive; a short-acting benzodiazepine for agitation; exclude other drugs.** There is no antidote. Panic, psychosis and tachycardia settle with calm and a benzodiazepine. Coma or seizures point to a co-ingestant or a synthetic cannabinoid — which is also treated first with benzodiazepines, because they lower the central drive that produces the agitation, heat and seizures."),
  ],
  mimic=[
    ("Cannabis vs synthetic cannabinoids (spice, K2)", "Synthetic cannabinoids are full CB1 agonists: a sympathomimetic picture with seizures, agitated delirium, hyperthermia and AKI — and the urine drug screen is negative."),
  ],
  traps=[
    ("“CB1 receptors are mainly peripheral”", "CB1 is the central receptor; CB2 is on immune cells (REC-14a)."),
    ("“A negative urine screen excludes cannabinoid toxicity”", "Synthetic cannabinoids are not detected by the standard immunoassay."),
    ("“Haloperidol, a beta-blocker or phentolamine first for synthetic-cannabinoid agitation and hyperthermia”", "Benzodiazepines first: haloperidol lowers the seizure threshold and impairs heat loss, and the beta-blocker or vasodilator treats a number, not the drive."),
  ],
  decode=[
    ("Synthetic cannabinoid overdose with severe agitation and hyperthermia — best initial treatment [DocT]", "Benzodiazepines."),
    ("Seizure, sympathomimetic picture, negative urine screen, says he smoked ‘cannabis’ [Marrow]", "Synthetic cannabinoid."),
  ],
  punch="THC acts on central CB1 receptors that are scarce in the brainstem, so cannabis disturbs the mind but spares breathing — care is supportive, and seizures with a negative screen mean a synthetic cannabinoid, treated first with benzodiazepines.",
)

L['REC-03'] = dict(
  sub="Toxicology → Cannabis & Opioids → Opioid overdose and naloxone",
  intro="Opioids stimulate μ receptors in the brainstem, which blunts the response to carbon dioxide; breathing slows, then stops, and hypoxia is what kills. Naloxone is a competitive μ antagonist that displaces the opioid within minutes — it, not flumazenil, charcoal or a urine screen, is the first step. But naloxone leaves the receptor sooner than most opioids, so a patient who wakes can stop breathing again.",
  parts=[
    ('a', "**Coma, pinpoint pupils, respiratory depression.** μ stimulation depresses the reticular activating system (coma) and the respiratory centre, and releases the Edinger–Westphal nucleus, so the pupils constrict (TOX-04); heart rate and blood pressure often fall too. Small pupils with a respiratory rate below about 10 point to an opioid — including codeine derivatives such as dihydrocodeine — rather than a benzodiazepine, which leaves breathing near normal (REC-09)."),
    ('b', "**3,6-diacetylmorphine; 2–3 times as potent as morphine.** The two acetyl groups make heroin far more lipid-soluble, so it enters the brain fast before being deacetylated to 6-monoacetylmorphine and morphine, which act on the receptor."),
    ('c', "**0.2–0.4 mg IV or IM, repeated to a maximum of 2 mg (0.04 mg steps in the dependent).** The aim is breathing (RR about 12 or more), not full wakefulness. In an opioid-dependent patient a large dose strips every receptor at once and causes abrupt withdrawal — agitation, vomiting and even seizures — so small steps are used."),
    ('d', "**40–80 minutes (your notes also print 30–120): shorter than most opioids, so toxicity recurs.** In round numbers, about an hour. Morphine, methadone and sustained-release preparations outlast a naloxone bolus, so a patient who responds still needs continued monitoring — prolonged with long-acting or sustained-release drugs — not discharge on waking."),
    ('e', "**Two-thirds of the effective reversal dose per hour.** The dose that woke the patient is known to work; two-thirds of it each hour as an infusion keeps receptor occupancy roughly steady. It is adjusted to breathing and to signs of withdrawal."),
  ],
  mimic=[
    ("Opioid vs clonidine coma", "Both give miosis, coma and bradycardia, but clonidine responds poorly to naloxone (TOX-04) — pinpoint pupils alone do not confirm an opioid."),
    ("Pulmonary oedema after naloxone vs heroin lung injury", "Abrupt reversal causes a sympathetic (catecholamine) surge, and the waking patient gasps against a closed glottis: neurogenic, non-cardiogenic oedema — not heroin alveolar toxicity or myocardial depression. One more reason to titrate."),
  ],
  traps=[
    ("“Naloxone lasts 6–12 hours, so one dose is enough”", "It lasts about an hour (40–80 minutes), less than most opioids; re-sedation is the rule with long-acting drugs (REC-14b)."),
    ("“Seizures after naloxone in a heroin user are hypoxic”", "They are precipitated withdrawal — the dose stripped the receptors too fast; titrate from 0.04 mg in the dependent."),
    ("“Still drowsy after naloxone though breathing is restored — tolerance or delayed opioid toxicity”", "Naloxone restores breathing, not necessarily consciousness; a co-ingested sedative (benzodiazepine, alcohol, gabapentinoid) is the usual answer, then hypoglycaemia, head injury or hypoxic brain injury."),
    ("“Coma, small pupils, RR 8, hypotension, low tone — diazepam”", "Benzodiazepines rarely depress breathing this much on their own; small pupils with a slow rate mean an opioid (dihydrocodeine)."),
  ],
  decode=[
    ("Unconscious, pinpoint pupils, RR 6 — next step (flumazenil, intubation and CT offered) [DocT; NEET 2025]", "Naloxone."),
    ("RR improves after naloxone but remains drowsy [DocT]", "Co-ingested sedative-hypnotic."),
    ("Heroin user develops pulmonary oedema or seizures after the antidote [DocT]", "Sympathetic surge (neurogenic oedema); precipitated withdrawal."),
    ("How long does naloxone act? [DocT]", "About 60 minutes — keep monitoring, especially with sustained-release opioids."),
  ],
  punch="Naloxone pushes the opioid off the μ receptor, but it leaves first — so it is titrated to breathing rather than wakefulness, and followed by an infusion or observation when the opioid will outlast it.",
)

L['REC-04'] = dict(
  sub="Toxicology → Cannabis & Opioids → Body packers",
  intro="A body packer swallows many tightly wrapped packets of heroin or cocaine to smuggle them. Each packet holds many times a lethal dose. The packer is well while the wrapping holds; if one leaks, the gut absorbs a massive dose at once — and which drug is inside decides whether there is an antidote.",
  parts=[
    ('a', "**Massive toxicity from rupture of swallowed drug packets (heroin or cocaine).** Acid, peristalsis and time can split a packet, and the gut absorbs freely, so one rupture gives an overdose far larger than street use. A packer who suddenly develops hypotension, VT or confusion has a ruptured packet until proved otherwise. An intact packet can still obstruct the bowel."),
    ('b', "**Packets may be radio-opaque.** They often show as regular oval shapes on a plain film (TOX-08), but X-ray misses some; CT is more sensitive and confirms that all have passed."),
    ('c', "**Whole bowel irrigation for intact packets (standard teaching, not in your notes); laparotomy for a ruptured cocaine packet; naloxone infusion for heroin.** In an asymptomatic packer with a normal ECG, polyethylene glycol flushes intact packets through before they break (TOX-09) — even for cocaine; surgery is not needed while the packets hold. Heroin leakage has an antidote, so a naloxone infusion holds the patient while packets pass. Cocaine has none: continuing absorption brings seizures, hyperthermia and arrhythmia that benzodiazepines cannot outrun, so a leaking cocaine packet comes out surgically. Obstruction is the other indication for surgery."),
  ],
  table=dict(title="What to do with a body packer", head=["Situation", "Management"], rows=[["Asymptomatic, packets intact", "whole bowel irrigation, observe, CT to confirm clearance"], ["Heroin leak", "naloxone infusion, continue irrigation"], ["Cocaine leak (toxicity)", "**laparotomy** + benzodiazepines"], ["Bowel obstruction", "surgery"]]),
  mimic=[
    ("Body packer vs body stuffer", "A packer swallows well-made packets for smuggling (large dose, sealed); a stuffer hastily swallows loosely wrapped drug to evade arrest (smaller dose, leaks early)."),
  ],
  traps=[
    ("“Asymptomatic cocaine packer — surgical removal”", "Surgery is for rupture with toxicity or obstruction; intact packets in a well patient get whole bowel irrigation."),
    ("“Asymptomatic with a normal ECG — discharge”", "Every packet is a potential lethal dose; irrigate and observe until CT shows clearance."),
    ("“Endoscopic removal of the packets”", "Endoscopy risks tearing a packet; it is generally avoided."),
  ],
  decode=[
    ("Airport smuggler, no symptoms, radio-opaque packets, normal ECG — management [DocT]", "Whole bowel irrigation."),
    ("Swallowed cocaine packets, then sudden hypotension, VT and confusion [DocT GT]", "Acute packet rupture — benzodiazepines and laparotomy."),
  ],
  punch="A body packer is safe only while every packet holds: flush the intact ones through, cover a heroin leak with naloxone, and take a leaking cocaine packet out surgically because nothing else can stop the absorption.",
)

L['REC-05'] = dict(
  sub="Toxicology → Stimulants → Cocaine",
  intro="Cocaine does two things at once. It blocks reuptake of noradrenaline, dopamine and serotonin, so the patient becomes hot, hypertensive and agitated; and it blocks cardiac sodium channels, as a local anaesthetic does. Most of its harm comes from intense vasoconstriction and that sympathetic storm — which is why calming the brain comes before treating the blood pressure.",
  parts=[
    ('a', "**Tropane alkaloid; CNS stimulant.** Cocaine is an ester local anaesthetic as well as a stimulant, and that sodium-channel block explains its wide-QRS arrhythmias."),
    ('b', "**Hyperthermia, seizures, myocardial infarction, aortic dissection, stroke, rhabdomyolysis and AKI.** Coronary vasospasm, platelet aggregation and higher oxygen demand cause infarction even with normal arteries. Sudden pressure surges tear the aorta and rupture cerebral vessels — intracranial haemorrhage is the complication to fear, not bradycardia, respiratory depression or hypothermia. Agitation and muscle activity break down muscle; heroin causes rhabdomyolysis too, by a different route (immobility and compression after a long down-time), whereas synthetic cannabinoids injure the kidney mostly directly and are the least likely of these to cause it. Smoked or snorted cocaine can also cause diffuse alveolar haemorrhage within 48 hours."),
    ('c', "**Benzodiazepines; cooling; aggressive fluids for rhabdomyolysis.** Benzodiazepines reduce central sympathetic outflow, so heart rate, blood pressure, agitation and heat production fall together — they treat the cause. Cooling is active because the set point is normal (TOX-12). Fluids keep urine flowing to clear myoglobin."),
    ('d', "**Avoid pure beta-blockers: unopposed alpha stimulation. Use nitrates, calcium-channel blockers or phentolamine.** Cocaine stimulates α- and β-receptors; β₂ vasodilation partly offsets α vasoconstriction. Block β alone (metoprolol, propranolol) and the α effect is left unopposed, worsening coronary spasm and pressure. Nitroglycerin, nitroprusside and calcium-channel blockers (diltiazem, verapamil, nicardipine) dilate vessels without that problem, and phentolamine blocks α directly; aspirin is given as in any ACS."),
    ('e', "**Sodium bicarbonate; lidocaine; lipid emulsion.** The wide QRS is sodium-channel block, so bicarbonate overcomes it as in a tricyclic overdose (TOX-07). Lidocaine (class Ib) leaves the channel quickly and is the acceptable anti-arrhythmic if bicarbonate fails; lipid emulsion is a last resort in refractory arrest."),
  ],
  mimic=[
    ("Cocaine vs amphetamine", "Same sympathomimetic picture and same blood-pressure rules; cocaine is short-acting and also widens the QRS, amphetamine lasts many hours (REC-06)."),
    ("Diffuse alveolar haemorrhage vs pneumothorax after cocaine", "Haemoptysis, hypoxaemia and diffuse bilateral infiltrates = alveolar haemorrhage (‘crack lung’); deep inhalation with Valsalva can cause pneumothorax, but that gives no diffuse infiltrates."),
  ],
  traps=[
    ("“Metoprolol for cocaine chest pain with hypertension and tachycardia”", "Contraindicated — unopposed α. Diltiazem, aspirin and lorazepam are all appropriate (REC-14c)."),
    ("“Labetalol is safe in cocaine toxicity because it also blocks α”", "Given IV it is mainly a β-blocker (α:β about 1:7). AHA guidance (2008 statement, 2012 update) calls it ‘may be reasonable’ in hypertensive cocaine ACS only after a vasodilator, and the 2014 guideline advises against β-blockers during acute intoxication; against lorazepam, phentolamine and nitroglycerin it is the exam’s ‘least appropriate’ answer."),
    ("“Heroin does not cause rhabdomyolysis”", "It does, through immobilisation and compression; among cocaine, methamphetamine, heroin and synthetic cannabinoids, the last is least likely."),
  ],
  decode=[
    ("Cocaine chest pain with ST elevation (or hypertension and tachycardia) — contraindicated drug [DocT]", "Beta-blocker (metoprolol)."),
    ("Cocaine, BP 223/150, diaphoretic, ST depression — least appropriate: lorazepam, phentolamine, nitroglycerin, labetalol [DocT GT]", "Labetalol."),
    ("Haemoptysis and diffuse bilateral infiltrates after snorting cocaine [DocT]", "Diffuse alveolar haemorrhage."),
    ("Complication of cocaine abuse to worry about most [NEET 2025]", "Intracranial haemorrhage."),
  ],
  punch="Cocaine is a catecholamine storm plus a sodium-channel blocker: calm the brain with benzodiazepines, open the vessels without blocking β alone, and treat the wide QRS with bicarbonate.",
  extra=[dict(q="Cocaine STEMI: reperfusion strategy?", a="**Primary PCI** when available (spasm, dissection and thrombus are common), plus benzodiazepines, nitrates and aspirin; fibrinolysis is second-line because of dissection and haemorrhage risk."),
         dict(q="Depression, hypersomnia and craving after stopping a stimulant?", a="**Cocaine withdrawal** — a ‘crash’, not an autonomic storm.")],
)

L['REC-06'] = dict(
  sub="Toxicology → Stimulants → Amphetamines and MDMA",
  intro="Amphetamines are indirect sympathomimetics: they push monoamines out of nerve terminals rather than stimulating receptors themselves, so their effect is longer and stronger than cocaine’s. MDMA is the amphetamine with the biggest serotonin effect. At a hot, crowded rave that surge drives temperature up and, through ADH release and heavy drinking, sodium down — and hyperthermia is what kills.",
  parts=[
    ('a', "**Ecstasy (tablet), Molly (crystal).** Molly is sold as the ‘pure’ powder, though street samples are often adulterated."),
    ('b', "**Releases and blocks reuptake of dopamine and serotonin; 5-HT2A agonist.** MDMA enters the terminal through the transporter and reverses it, so serotonin, dopamine and noradrenaline pour into the synapse — increased synaptic release, not direct α- or dopamine-receptor agonism. The serotonin release is far greater than with other amphetamines, which explains the empathy users seek, the jaw clenching and bruxism, and the serotonergic toxicity."),
    ('c', "**Serotonin syndrome; also hyperthermia and hyponatraemia (standard teaching, not in your notes).** Excess serotonin gives clonus, hyperreflexia and heat (REC-11, REC-13). The heat is produced, not set: serotonergic and dopaminergic drive, agitation and muscle activity, plus mitochondrial uncoupling in muscle, while vasoconstriction and a hot room stop its loss — the set point is normal and the patient sweats. It drives rhabdomyolysis, DIC and multi-organ failure. Serotonin also releases ADH, and users drink large volumes of water, so a euvolaemic SIADH-type hyponatraemia (urine osmolality >100, urine sodium >30) develops, with cerebral oedema and seizures — especially in young women."),
    ('d', "**Parenteral benzodiazepines; nitroglycerine or nicardipine; no beta-blockers; external cooling.** Benzodiazepines lower central drive and so the heat, heart rate and pressure together. If hypertension persists a vasodilator or phentolamine is added; a beta-blocker (propranolol, even labetalol) is avoided for the unopposed-α reason (REC-05). Cooling comes first when the temperature is high, because peak temperature predicts death. Hyponatraemia is treated by severity: mild symptoms, fluid restriction; seizures or coma, 3% saline in 100–150 mL boluses."),
  ],
  mimic=[
    ("MDMA vs cocaine or methamphetamine", "Bruxism and jaw clenching, hyponatraemia and long duration point to MDMA; LSD gives hallucinations with little sympathetic storm."),
  ],
  traps=[
    ("“Methamphetamine with severe hypertension — labetalol or propranolol”", "Beta-blockade leaves α unopposed. DocT keys phentolamine as the first antihypertensive; nicardipine is equally defensible (both listed as alternatives), and benzodiazepines — the true first step — are not offered. The key is disputed."),
    ("“Seizures, rhabdomyolysis or intracranial haemorrhage is the most immediate threat after ‘molly’”", "Hyperthermia is the killer; the others are downstream of it or rarer. Cool first."),
    ("“MDMA hyperthermia is a reset hypothalamic set point or impaired sweating”", "It is heat production (muscle activity, mitochondrial uncoupling) with poor heat loss; users sweat and the set point is normal."),
    ("“Any MDMA hyponatraemia needs hypertonic saline”", "Sodium 128 with only dizziness and a normal neurological examination: fluid restriction. 3% saline is for seizures or coma; demeclocycline is too slow."),
    ("“Amphetamines stimulate α-receptors directly”", "They are indirect: transporter reversal increases synaptic dopamine and noradrenaline release."),
  ],
  decode=[
    ("Rave, agitation, hyperthermia, mydriasis, sweating, bruxism [DocT]", "MDMA."),
    ("‘Molly’ at a festival — most immediate life-threatening complication [DocT]", "Hyperthermia leading to multi-organ failure."),
    ("Ecstasy, sodium 128, euvolaemic, urine Na 105, only dizzy [DocT GT]", "SIADH-type — fluid restriction."),
    ("Methamphetamine with severe hypertension and seizures — best antihypertensive [DocT; DocT GT]", "Phentolamine (keyed; nicardipine also defensible) — never a beta-blocker."),
  ],
  punch="MDMA is the serotonin amphetamine: the serotonin surge brings heat, clonus and ADH release, so temperature and sodium decide survival — cool first, sedate with benzodiazepines, and never use a beta-blocker.",
)

L['REC-07'] = dict(
  sub="Toxicology → Stimulants → Sympathomimetic toxidrome",
  intro="Every feature of the sympathomimetic toxidrome is the fight-or-flight response turned up and left on. Cocaine, amphetamines, MDMA and cathinones flood the synapses with noradrenaline and dopamine, so each organ shows its sympathetic action — and the opposite drug class, an opioid, is the one that cannot produce it.",
  parts=[
    ('a', "**CNS: euphoria, agitation, psychosis, seizures.** Dopamine excess gives euphoria, then paranoia and psychosis; at high levels the cortex seizes, and agitation adds heat and acidosis."),
    ('b', "**Neuromuscular: hyperreflexia, tremor.** Central drive and β₂ stimulation of muscle make reflexes brisk and produce tremor — but without the inducible clonus that marks serotonin toxicity (REC-12)."),
    ('c', "**Autonomic: hyperthermia, sweating, mydriasis.** Heat comes from muscle activity and vasoconstriction that stops skin heat loss. Sweating continues because sympathetic sweat fibres use acetylcholine and are driven, not blocked — the key difference from the anticholinergic patient (TOX-03). The pupils dilate through α₁ action."),
    ('d', "**Cardiovascular: tachycardia, hypertension, arrhythmia.** β₁ stimulation speeds the heart and α₁ vasoconstriction raises the pressure, raising oxygen demand while narrowing coronary supply."),
    ('e', "**GI: nausea, vomiting, diarrhoea.** Non-specific, but bowel sounds are present, unlike the silent bowel of anticholinergic poisoning."),
  ],
  mimic=[
    ("Sympathomimetic vs anticholinergic", "Both hot, fast and dilated; the sympathomimetic patient sweats and has bowel sounds, the anticholinergic is dry with retention."),
    ("Sympathomimetic vs serotonin syndrome", "Both sweat with brisk reflexes; clonus belongs to serotonin toxicity."),
  ],
  traps=[
    ("“Agitation, tachycardia, mydriasis and diaphoresis — anticholinergic”", "Diaphoresis excludes it: anticholinergic skin is dry. This is sympathomimetic, and cocaine or amphetamine causes it; the least likely agent is an opioid (miosis, sedation, bradycardia)."),
    ("“Hyperreflexia means serotonin syndrome”", "Sympathomimetics give brisk reflexes too; clonus is the serotonin sign."),
  ],
  decode=[
    ("Agitation, tachycardia, dilated pupils, diaphoresis — toxidrome, and the agent least likely to cause it [DocT]", "Sympathomimetic; opioid."),
    ("Same stem, option ‘anticholinergic; cocaine’ [DocT]", "Wrong twice — sweating excludes anticholinergic, and cocaine does cause this picture."),
  ],
  punch="The sympathomimetic toxidrome is adrenaline on every organ — hot, fast, hypertensive and dilated — and, unlike the anticholinergic, still sweating with bowel sounds present.",
)

L['REC-08'] = dict(
  sub="Toxicology → Hallucinogens & Sedatives → Hallucinogens",
  intro="Classic hallucinogens are 5-HT2A agonists in the cortex: they scramble sensory filtering and give visions and synaesthesia. A second group — phencyclidine, ketamine and dextromethorphan — block the NMDA receptor and dissociate mind from body. None has an antidote; the danger is behaviour, panic and occasionally heat, and agitation is treated with benzodiazepines.",
  parts=[
    ('a', "**LSD: ergot-derived; synaesthesia, panic, hyperthermia.** Made from lysergic acid of the ergot fungus and active in micrograms; strong 5-HT2A agonism mixes the senses and can cause ‘bad trips’, with mild sympathetic stimulation and heat at large doses."),
    ('b', "**Psilocybin: magic mushrooms; active form psilocin.** Psilocybin is a prodrug, dephosphorylated to psilocin, which acts at 5-HT2A."),
    ('c', "**Mescaline: phenylethylamine (peyote).** It shares the amphetamine backbone, which is why it carries some sympathetic effects with its visions."),
    ('d', "**Phencyclidine: angel dust; nystagmus, violence.** NMDA block gives dissociation with analgesia, so patients become violent and injure themselves without noticing. Horizontal, vertical or rotatory nystagmus is its bedside signature (TOX-05)."),
    ('e', "**Ketamine: NMDA antagonist; dissociation.** The shorter-acting relative of PCP: dissociation, nystagmus, raised heart rate and pressure, with airway reflexes and breathing usually preserved."),
    ('f', "**Salvia: salvinorin A.** A κ-opioid agonist rather than a serotonin or NMDA drug; intense, very brief dissociation."),
  ],
  mimic=[
    ("Classic hallucinogen vs dissociative", "LSD and psilocybin (5-HT2A) alter perception; PCP, ketamine and dextromethorphan (NMDA) dissociate and add nystagmus."),
    ("PCP vs sympathomimetic", "Both agitated, hypertensive and violent; nystagmus points to PCP."),
  ],
  traps=[
    ("“Ketamine is a GABA agonist”", "It is an NMDA antagonist (REC-14d)."),
    ("“Psilocybin is the active molecule”", "It is a prodrug; psilocin acts."),
    ("“Haloperidol to sedate dextromethorphan or PCP agitation”", "Benzodiazepines (lorazepam) are the chemical sedation of choice; dextromethorphan is often co-formulated with paracetamol, so check a paracetamol level."),
  ],
  decode=[
    ("Dextromethorphan agitation — chemical sedation [Marrow]", "Lorazepam."),
    ("Violent, analgesic, vertical nystagmus [pattern]", "Phencyclidine."),
  ],
  punch="Hallucinogens split into 5-HT2A agonists that distort perception (LSD, psilocybin, mescaline) and NMDA antagonists that dissociate with nystagmus (PCP, ketamine) — neither has an antidote, so quiet and benzodiazepines are the treatment.",
)

L['REC-09'] = dict(
  sub="Toxicology → Hallucinogens & Sedatives → Sedative street drugs",
  intro="Flunitrazepam and GHB are both used to sedate a victim without their knowledge because they are tasteless in a drink, act fast and erase memory. Both enhance GABA inhibition, so the picture is sedation and amnesia with vital signs that stay surprisingly normal until coma is deep.",
  parts=[
    ('a', "**Rohypnol: a benzodiazepine 10 times as potent as diazepam; acts in 10–20 minutes for 4–6 hours; detected as a benzodiazepine on screening.** A 1–2 mg dose sedates strongly, with anterograde amnesia; in practice sedation and amnesia often last 8–12 hours or more, and the low dose means routine immunoassays often miss it. Alcohol deepens the sedation and respiratory depression."),
    ('b', "**Gamma-hydroxybutyrate: liquid, mixed with alcohol; euphoria, amnesia, hypotonia, then sudden coma; supportive care.** GHB acts mainly on GABA-B receptors with a steep dose–response curve, so coma follows within minutes — often with bradycardia and myoclonus — and the patient wakes abruptly a few hours later. Airway support is all that is needed."),
    ('c', "**CNS depression with near-normal vital signs and reflexes.** Sedative-hypnotics depress the cortex and reticular activating system long before the brainstem centres for breathing and circulation — unless alcohol or an opioid is added (TOX-04)."),
  ],
  mimic=[
    ("Sedative-hypnotic or GHB vs opioid coma", "Opioid: pinpoint pupils and a very slow respiratory rate, reversed by naloxone. Sedative: variable pupils, near-normal breathing; GHB coma also ends abruptly."),
  ],
  traps=[
    ("“Flumazenil to reverse a suspected Rohypnol drink”", "Rarely given — seizure risk in dependence or mixed ingestion; support the airway (TOX-01)."),
    ("“A negative screen excludes a spiked drink”", "GHB is not on the standard immunoassay, and flunitrazepam is often missed."),
  ],
  decode=[
    ("Sudden coma at a party, wakes abruptly after 3 hours [pattern]", "GHB."),
    ("Deep coma with near-normal vital signs [pattern]", "Sedative-hypnotic toxidrome."),
  ],
  punch="Flunitrazepam and GHB both deepen GABA inhibition — sedation and amnesia with near-normal vital signs — and GHB adds a sudden coma that ends as suddenly, needing only airway support.",
)

L['REC-10'] = dict(
  sub="Toxicology → Hallucinogens & Sedatives → Volatile solvents",
  intro="Volatile solvents — toluene, butane, propane — are inhaled from a bag or rag. They behave like inhaled anaesthetics: fat-soluble, taken up and cleared through the lungs within minutes, so even deep coma lifts quickly once the vapour is gone. The acute danger is the heart; the chronic danger is to lipid-rich tissue, especially the brain.",
  parts=[
    ('a', "**Glue, lighter refills, spray deodorants; street children.** Cheap, legal and everywhere, so they are the drug of the poorest and youngest users (REC-01)."),
    ('b', "**Sudden sniffing death syndrome: arrhythmia (myocardium sensitised to catecholamines).** Solvents make the myocardium excitable, so an adrenaline surge — fright, being chased, sudden exertion — triggers VF; rebreathing hypoxia adds to it. Approach calmly, and use adrenaline with great care."),
    ('c', "**Neurological, lung, liver and kidney damage.** Solvents dissolve into myelin: chronic toluene gives leukoencephalopathy, ataxia and dementia, and also distal renal tubular acidosis with severe hypokalaemia (normal anion gap). n-Hexane causes peripheral neuropathy; chlorinated solvents injure the liver."),
  ],
  mimic=[],
  traps=[
    ("“GCS 3 recovering to 15 within 10 minutes — smoked heroin”", "Heroin coma lasts hours unless naloxone is given; cannabis does not cause coma; only a solvent clears through the lungs that fast."),
    ("“Sudden death in huffing is from asphyxia alone”", "The main mechanism is catecholamine-sensitised VF, often triggered by fright or exertion."),
  ],
  decode=[
    ("16-year-old, GCS 3, sitting up talking with GCS 15 ten minutes later [DocT]", "Inhaled solvent (glue)."),
    ("Teenager collapses while running from police after sniffing glue [pattern]", "Sudden sniffing death — VF."),
  ],
  punch="Solvents are cheap anaesthetic vapours: they wear off in minutes, but they sensitise the heart to adrenaline — so fright can cause fatal VF — and with chronic use they dissolve the brain’s myelin.",
)

L['REC-11'] = dict(
  sub="Toxicology → Hyperthermic Toxidromes → Serotonin syndrome vs NMS",
  intro="Both syndromes give a hot, confused, rigid patient on psychiatric drugs. But they arise from opposite neurochemistry: serotonin syndrome is too much serotonin, NMS too little dopamine action. Too much serotonin excites — fast onset, clonus, brisk reflexes; too little dopamine freezes — slow onset, rigidity, slow reflexes. The drug history usually gives it away.",
  parts=[
    ('a', "**Cause: serotonin syndrome — excess serotonin, usually two serotonergic drugs; NMS — dopamine blockade, or stopping a dopamine agonist.** Serotonin syndrome follows adding a second serotonergic drug — an antidepressant plus tramadol, linezolid or a cough remedy (dextromethorphan) for a cold (TOX-05). NMS follows a D₂ antagonist — typical or atypical antipsychotics (haloperidol, olanzapine), metoclopramide — or abrupt withdrawal of levodopa, as in a Parkinson’s patient who stops getting it after admission. A psychiatric card with procyclidine (given for antipsychotic side-effects) implies an antipsychotic. Dopamine agonists themselves do not cause it."),
    ('b', "**Onset: serotonin syndrome under 12 hours; NMS 1–3 days.** Serotonin excess is direct, so it appears within hours of the change; NMS builds as dopamine block accumulates — days to a few weeks after starting or raising the drug."),
    ('c', "**Pupils: serotonin syndrome dilated; NMS normal.** Serotonin excess drives the sympathetic system; dopamine block does not."),
    ('d', "**Tone: serotonin syndrome increased, in the legs; NMS lead-pipe rigidity.** Spinal serotonin excitation raises tone mostly in the legs; loss of basal-ganglia dopamine gives generalised, uniform lead-pipe rigidity."),
    ('e', "**Reflexes: serotonin syndrome hyperreflexia and clonus; NMS bradyreflexia.** The most reliable discriminator: clonus or myoclonus means serotonin; ‘no clonus’ in a rigid febrile patient points to NMS."),
    ('f', "**Bowel: serotonin syndrome hyperactive; NMS normal.** Gut serotonin drives motility, so serotonin excess gives diarrhoea."),
    ('g', "**Treatment: serotonin syndrome — cyproheptadine; NMS — bromocriptine, dantrolene.** Both start with stopping the drug, benzodiazepines and cooling. Cyproheptadine blocks 5-HT2A (REC-13). Bromocriptine replaces the missing dopamine action and is the conventional drug of choice; dantrolene relaxes muscle by blocking calcium release and is the adjunct. Neither has trial evidence, and dantrolene has none at all in stimulant hyperthermia."),
  ],
  table=dict(title="Opposite chemistry, opposite signs", head=["", "Serotonin syndrome", "NMS"], rows=[["Problem", "too much serotonin", "too little dopamine"], ["Onset", "**<12 h**", "**1–3 days**"], ["Tone, reflexes", "legs > arms, **clonus**", "**lead-pipe**, slow reflexes"], ["Pupils, bowel", "dilated, hyperactive", "normal, normal"], ["Specific drug", "cyproheptadine", "bromocriptine, dantrolene"]]),
  mimic=[
    ("NMS vs malignant hyperthermia", "Both rigid and hot with high CK; MH happens in theatre after a volatile agent or suxamethonium, with rising ETCO₂."),
    ("Serotonin syndrome vs opioid withdrawal or anticholinergic", "All can be tachycardic with dilated pupils. Withdrawal gives yawning, lacrimation and piloerection without fever or clonus; the anticholinergic patient is dry with a silent bowel."),
  ],
  traps=[
    ("“NMS drug of choice — dantrolene”", "DocT keys bromocriptine; dantrolene is the adjunct. A Marrow item keys dantrolene for antipsychotic-related rigidity and catatonia — if both are offered, bromocriptine is the conventional answer."),
    ("“A trial (HAT, RAMP, DAHS) supports dantrolene in amphetamine hyperthermia”", "No trial does — those names are invented; stimulant heat is central drive and muscle activity, not a ryanodine-receptor leak."),
    ("“Rigid and febrile 2 weeks after starting olanzapine and clomipramine — the antidepressant”", "No clonus, rigidity, raised CK and transaminases mean NMS from the high-dose antipsychotic; atypicals cause it too. Lithium alone causes it only rarely (case reports) and is not the answer."),
    ("“Fever, tremor, myoclonus and sweating on antidepressants — NMS or anticholinergic”", "Myoclonus and sweating mean serotonin syndrome; a cold remedy was the second drug (REC-14e)."),
  ],
  decode=[
    ("Schizophrenic recently started on haloperidol, rigid, 39.5 °C, CK 12 000 — drug of choice [DocT]", "Bromocriptine."),
    ("Antipsychotic started 2 weeks ago, rigid, no clonus, diaphoretic, BP 185/90 [DocT GT]", "NMS (olanzapine)."),
    ("On antidepressants with a cold; tremor, myoclonus, diaphoresis, 39.2 °C [DocT]", "Serotonin syndrome."),
    ("Parkinson’s patient intubated in ICU, day 6: fever, rigidity [DocT GT]", "NMS (levodopa interrupted or a dopamine blocker)."),
  ],
  punch="Serotonin syndrome is excess serotonin — fast, twitchy, clonus and dilated pupils within hours; NMS is lost dopamine — slow, stiff, lead-pipe rigidity with slow reflexes over days.",
)

L['REC-12'] = dict(
  sub="Toxicology → Hyperthermic Toxidromes → The five hyperthermic toxidromes",
  intro="Five drug-related syndromes can push the temperature to lethal levels. In all of them the heat comes from the body producing or holding heat — muscle activity, hypermetabolism or lost sweating — not from a raised hypothalamic set point, so antipyretics do nothing and every one is cooled actively. Fever, mydriasis and confusion are shared; one bedside sign each separates them, and that sign picks the specific drug.",
  parts=[
    ('a', "**Sympathomimetic: sweaty, extreme hypertension — benzodiazepines.** Catecholamine excess raises heat production (muscle activity and, with MDMA, mitochondrial uncoupling) while sweating continues (REC-07). Benzodiazepines lower central drive and so treat heat and pressure together — as in synthetic-cannabinoid agitation."),
    ('b', "**Anticholinergic: dry, non-reactive pupils, retention, absent bowel sounds — physostigmine (severe).** Muscarinic block stops sweating, so dry skin is the one sign that separates it from the other four. Physostigmine is a reversible (carbamate) cholinesterase inhibitor that crosses into the brain, so it reverses both the delirium and the peripheral signs — the specific answer for, say, diphenhydramine or ingested atropine eye drops with a normal QRS. It is kept for severe cases and avoided when the ECG shows conduction delay."),
    ('c', "**Serotonin: clonus, hyperreflexia — cyproheptadine.** Spinal 5-HT2A stimulation gives clonus, which no other toxidrome here produces (REC-13)."),
    ('d', "**NMS: lead-pipe rigidity, slow reflexes — bromocriptine.** Dopamine block causes the rigidity and impairs central heat regulation; bromocriptine replaces dopamine action, with dantrolene as the adjunct (REC-11). A drug started newly that causes hyperthermia is a blocker (antipsychotic, metoclopramide) — never dopamine itself."),
    ('e', "**Malignant hyperthermia: rising CO₂, rigor despite relaxant; temperature often above 42 °C — dantrolene.** In susceptible patients a volatile agent or suxamethonium opens the abnormal ryanodine receptor and calcium floods the muscle, which contracts and burns energy uncontrollably: rising ETCO₂, tachycardia, mixed acidosis and high CK, then heat. After stopping the trigger, dantrolene is the most critical step — oxygen, ice and bicarbonate support but do not stop the calcium release. It is the specific cure here, where the problem is in the muscle itself, and at most an adjunct elsewhere."),
  ],
  table=dict(title="One sign each", head=["Toxidrome", "The giveaway", "Specific treatment"], rows=[["Sympathomimetic", "**wet** + very high BP", "benzodiazepines"], ["Anticholinergic", "**dry**, retention, silent bowel", "physostigmine (severe)"], ["Serotonin", "**clonus**", "cyproheptadine"], ["NMS", "**lead-pipe**, slow reflexes", "bromocriptine"], ["Malignant hyperthermia", "**rising ETCO₂** in theatre", "dantrolene"]]),
  mimic=[
    ("Malignant hyperthermia vs NMS", "MH: minutes to hours in theatre after a trigger; NMS: days after an antipsychotic."),
  ],
  traps=[
    ("“Mydriasis, fever or altered mental status distinguishes the anticholinergic syndrome”", "All are shared with sympathomimetic, serotonin and NMS; only the dry skin separates it."),
    ("“Paracetamol, or a reset set point, explains toxic hyperthermia”", "The set point is normal; MDMA heat is muscle activity and uncoupling. All five are cooled actively."),
    ("“A trial supports dantrolene in amphetamine hyperthermia”", "None does (the trial names offered are invented) and it is not standard care; cool, sedate, paralyse above 41 °C."),
    ("“Haloperidol for the agitated hyperthermic patient”", "It lowers the seizure threshold, impairs heat loss and may add NMS; benzodiazepines are first."),
  ],
  decode=[
    ("Which finding best distinguishes antimuscarinic from sympathomimetic, serotonin and NMS? [DocT]", "Dry skin."),
    ("Amphetamine hyperthermia — which trial supports dantrolene? [DocT]", "None."),
    ("Diphenhydramine, dry, retention, normal QRS — reverses central and peripheral toxicity [DocT GT; Marrow]", "Physostigmine (reversible cholinesterase inhibitor)."),
    ("Suxamethonium MH — most critical first intervention [DocT]", "Dantrolene."),
  ],
  punch="Five syndromes, one heat mechanism — muscle and lost cooling, never the thermostat — so all are cooled actively, and the giveaway sign (wet, dry, clonus, lead-pipe, rising CO₂) picks the specific drug.",
  extra=[dict(q="Malignant hyperthermia: dantrolene dose?", a="**2.5 mg/kg IV**, repeated until the crisis settles; usual upper limit about **10 mg/kg**."),
         dict(q="Physostigmine contraindications?", a="**Wide QRS or AV block (and suspected tricyclic overdose)**, ventricular arrhythmias, asthma, and mechanical bowel or bladder obstruction. **Hypertension is not one.**")],
)

L['REC-13'] = dict(
  sub="Toxicology → Hyperthermic Toxidromes → Serotonin syndrome: diagnosis and treatment",
  intro="Serotonin syndrome has no laboratory test; it is a clinical diagnosis in a patient exposed to a serotonergic drug, ranging from tremor and sweating to a temperature above 41 °C with rigidity. Hyperthermia is what kills, so treatment rests on removing the drug and stopping the heat; the antidote only helps.",
  parts=[
    ('a', "**Altered mental status, autonomic hyperactivity, neuromuscular abnormality.** Brain (agitation, confusion), autonomic system (sweating, tachycardia, mydriasis, diarrhoea, heat) and spinal cord (tremor, hyperreflexia, clonus). The neuromuscular part is the most specific."),
    ('b', "**Hunter criteria (sensitivity 84%, specificity 97%); Sternbach (75%, 96%).** Hunter requires a serotonergic drug plus one of: spontaneous clonus; inducible or ocular clonus with agitation or sweating; tremor with hyperreflexia; or hypertonia with temperature above 38 °C and ocular or inducible clonus. Built on clonus, it is more accurate than Sternbach, whose non-specific features overlap with NMS and stimulant toxicity."),
    ('c', "**Serotonin (5-HT2A) antagonist: 2 mg per dose to a maximum of 12 mg; maintenance 8 mg every 6 hours. Usual regimen: 12 mg, then 2 mg every 2 hours (standard teaching, not in your notes).** Cyproheptadine is an antihistamine that also blocks 5-HT2A receptors; 12–32 mg over 24 hours binds most of them, so the notes’ ‘maximum of 12 mg’ does not fit the standard regimen. It is oral only — crushed down a nasogastric tube."),
    ('d', "**Symptom relief only; no proven effect on outcome.** Survival depends on stopping the drug, benzodiazepines, active cooling and, above 41 °C, paralysis with a non-depolarising relaxant and ventilation, which stops the muscle heat at its source."),
  ],
  mimic=[],
  traps=[
    ("“Rhabdomyolysis, seizures or hypertensive haemorrhage is the most immediate threat in a hot, serotonergic stimulant patient”", "Hyperthermia drives multi-organ failure and death; the others follow from it. Cool and paralyse first."),
    ("“Cyproheptadine is the mainstay and improves survival”", "It relieves symptoms only; supportive care, cooling and paralysis save life."),
    ("“Paralyse the hyperthermic patient with suxamethonium”", "Use a non-depolarising agent — rhabdomyolysis raises potassium, which suxamethonium worsens."),
  ],
  decode=[
    ("‘Molly’ at a festival, hyperthermic — most immediate life-threatening complication [DocT]", "Hyperthermia leading to multi-organ dysfunction."),
    ("Best diagnostic criteria for serotonin syndrome [pattern]", "Hunter."),
  ],
  punch="Serotonin syndrome is diagnosed by clonus (Hunter criteria) and survived by removing the drug and stopping the heat — cyproheptadine eases the symptoms but has never been shown to change the outcome.",
)

L['REC-14'] = dict(
  sub="Toxicology → Revision → True or false",
  intro="Each statement turns on one mechanism from an earlier card; the reason for each answer is the physiology met there.",
  parts=[
    ('a', "**False — CB1 is central; CB2 is peripheral.** CB1 is on brain nerve terminals; CB2 on immune cells (REC-02)."),
    ('b', "**False — naloxone lasts 40–80 minutes.** Shorter than most opioids, so sedation recurs (REC-03)."),
    ('c', "**False — avoid beta-blockers; give benzodiazepines.** Blocking β alone leaves α-vasoconstriction unopposed — beta-blockers are the contraindicated drug in cocaine chest pain with ST elevation, while aspirin, nitroglycerin and benzodiazepines are given (REC-05)."),
    ('d', "**True — ketamine is an NMDA antagonist,** which gives its dissociation and nystagmus (REC-08)."),
    ('e', "**False — hyperreflexia and clonus are serotonin syndrome.** NMS gives lead-pipe rigidity with slow reflexes (REC-11)."),
    ('f', "**True — malignant hyperthermia is treated with dantrolene,** which blocks calcium release from the abnormal ryanodine receptor (REC-12)."),
    ('g', "**False — anticholinergic skin is dry.** Sweat glands work through muscarinic receptors (TOX-03)."),
    ('h', "**True — serotonin syndrome begins within 12 hours** of the drug change, unlike NMS, which takes days (REC-11)."),
  ],
  mimic=[],
  traps=[
    ("“Clonus can occur in NMS”", "Clonus is the serotonin sign; NMS is slow and stiff."),
  ],
  decode=[
    ("Cocaine overdose, chest pain, ST elevation — which drug is contraindicated? [DocT]", "Beta-blockers."),
    ("Statements about hyperthermic toxidromes [pattern]", "Clonus and hours mean serotonin; rigidity and days mean NMS."),
  ],
  punch="Every statement here turns on a mechanism from the deck — where CB1 sits, how long naloxone lasts, unopposed α, clonus versus rigidity, and the sweat gland’s muscarinic receptor.",
)

L['REC-15'] = dict(
  sub="Toxicology → Hyperthermic Toxidromes → Temperature, onset and reflexes",
  intro="Once the skin and the giveaway sign are known (REC-12), three more features sort the hyperthermic toxidromes: how hot, how fast and what the reflexes do. Drugs acting directly — sympathomimetic, anticholinergic, serotonin — act within hours; NMS needs days; malignant hyperthermia is the hottest because the muscle itself is out of control.",
  parts=[
    ('a', "**Sympathomimetic: above 38 °C, under 12 hours, brisk reflexes.** Catecholamine excess is immediate; central excitation makes reflexes brisk without clonus (REC-07)."),
    ('b', "**Anticholinergic: above 38 °C, under 12 hours, normal reflexes.** Muscarinic receptors do not run the spinal reflex arc, so reflexes stay normal."),
    ('c', "**Serotonin: above 38 °C, under 12 hours, clonus (ocular too).** Spinal motor-neurone excitation gives hyperreflexia and inducible, spontaneous or ocular clonus (REC-13)."),
    ('d', "**NMS: 39–42 °C, 1–3 days, slow reflexes.** Dopamine block builds over days; rigid muscle generates heat and blunts the reflexes (REC-11). NMS is always hot — hypothermia is not a feature."),
    ('e', "**Malignant hyperthermia: often above 42 °C, 30 minutes to 24 hours, hyporeflexia.** Uncontrolled calcium release keeps every fibre contracting, so temperature can climb by 1 °C or more every 5 minutes. It starts in theatre during or soon after the trigger; it is inherited (autosomal dominant RYR1), so a relative’s reaction under anaesthesia is a warning. Stopping the trigger and giving dantrolene come first."),
  ],
  table=dict(title="How hot, how fast, which reflexes", head=["Toxidrome", "Temp (°C)", "Onset", "Reflexes"], rows=[["Sympathomimetic", ">38", "<12 h", "brisk"], ["Anticholinergic", ">38", "<12 h", "normal"], ["Serotonin", ">38", "<12 h", "**clonus**"], ["NMS", "39–42", "**1–3 days**", "slow"], ["Malignant hyperthermia", "**often >42**", "30 min–24 h", "hyporeflexia"]]),
  mimic=[
    ("Malignant hyperthermia vs NMS", "Both rigid with high CK; MH follows a trigger within the anaesthetic, NMS takes days after an antipsychotic."),
  ],
  traps=[
    ("“Temperature is the first sign of malignant hyperthermia”", "A rising ETCO₂ and tachycardia come first; the temperature rises later."),
    ("“Propofol, midazolam, rocuronium or nitrous oxide can trigger malignant hyperthermia”", "Only volatile agents and suxamethonium trigger it; propofol, benzodiazepines, opioids, ketamine, nitrous oxide and non-depolarising relaxants are safe."),
  ],
  decode=[
    ("Relative had fever and rigidity under anaesthesia — which neuromuscular blocker is linked? [Marrow]", "Suxamethonium (succinylcholine)."),
    ("Haloperidol overdose 2 days ago — which finding is NOT expected? [Marrow]", "Hypothermia (NMS runs 39–42 °C)."),
    ("Rigidity, 41 °C and mixed acidosis after suxamethonium and a volatile — diagnosis and drug; first intervention [DocT]", "Malignant hyperthermia — dantrolene."),
  ],
  punch="Hours and brisk reflexes or clonus mean a drug acting directly (sympathomimetic, serotonin); days and slow reflexes mean NMS; the hottest of all, in theatre, is malignant hyperthermia, where the muscle itself burns.",
)

FLAGS = {}
FLAGS['REC-01'] = "Part c ‘In children: inhalants’ — the 2019 national survey’s point is that inhalants are the only class used MORE by children than adults (about 1.17% vs 0.58%); inhalants are not the commonest substance in children overall (alcohol and opioids are reported higher). Worth rewording to ‘used more by children than adults’. Check against the report."
FLAGS['REC-03'] = "Part c ‘maximum of 2 mg’ — 2 mg is not a true ceiling: if no response, doses up to about 10 mg are given before excluding opioid toxicity (more relevant with fentanyl analogues). Consistent with TOX-01, so left as is in the explanation."
FLAGS['REC-09'] = "Part a ‘detected as a benzodiazepine on screening’ — flunitrazepam is often NOT detected on routine urine benzodiazepine immunoassays (low dose, poor cross-reactivity of 7-aminoflunitrazepam); specific assays are needed. Also ‘lasts 4–6 hours’ is short: sedation and amnesia are described as lasting 8–12 hours or more (US DOJ Rohypnol fact sheet: onset 15–20 min, effects >12 h)."
FLAGS['REC-13'] = "Part c ‘2 mg per dose to a maximum of 12 mg’ — does not match the standard regimen (Boyer & Shannon, NEJM 2005): 12 mg initially, then 2 mg every 2 hours while symptoms persist, maintenance 8 mg every 6 hours, about 12–32 mg per 24 h. The card already adds the standard regimen; the notes’ line should probably go."
FLAGS['REC-15'] = "WATCH ‘temperature climbs 1 degree every 10 minutes’ — standard texts quote a rise of about 1 °C (up to 2 °C) every 5 minutes in fulminant malignant hyperthermia. ‘All inhaled agents except nitrous oxide’ is better phrased ‘all volatile agents’ (xenon also does not trigger). Onset ‘up to 24 h’ is generous; most cases start intra-operatively or within about an hour after (PACU)."
