# TOX04 — Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Deck: Recreational Drugs & Hyperthermic Toxidromes (REC-01 to REC-15). Same fields as tox01_learn.py.
L = {}

L['REC-01'] = dict(
  sub="Toxicology → Cannabis & Opioids → Substance use in India",
  intro="The figures come from the national survey on the magnitude of substance use in India (Ministry of Social Justice with NDDTC, AIIMS, 2019), which counted current users aged 10–75. They matter in the ICU because they predict what walks in: alcohol withdrawal and its complications far outnumber everything else, and opioids — mostly heroin — are used in India at a rate well above the world average. Children have a pattern of their own.",
  parts=[
    ('a', "**Alcohol, 14.6%.** About one in seven Indians aged 10–75 is a current drinker, and a sizeable share of them are dependent. That is why alcohol withdrawal, Wernicke’s encephalopathy and alcohol-related liver and pancreatic disease are the commonest substance problems on the ward."),
    ('b', "**Cannabis 2.8%, then opioids 2.1%.** Cannabis is cheap, culturally familiar (bhang) and widely available, so it comes second. Opioids come third overall, but the striking point is the comparison: at 2.1%, Indian opioid use is about three times the global figure (0.7%), and heroin has overtaken traditional opium as the commonest opioid."),
    ('c', "**Inhalants.** Glue, whitener, petrol and solvent sprays are cheap, legal and easy to hide, so they are the substance of street and school-age children. The survey’s headline was that inhalants are the one class used more by children and adolescents than by adults."),
  ],
  mimic=[
    ("Commonest substance overall vs in children", "Overall it is alcohol; the class that is characteristic of children (used more by them than by adults) is inhalants."),
    ("Indian vs world opioid use", "India about 2.1%, the world about 0.7% — roughly three times higher."),
  ],
  traps=[
    ("“Cannabis is the commonest substance used in India”", "Alcohol is far ahead at 14.6%; cannabis is second at 2.8%."),
    ("“Opioid use in India is below the world average”", "It is about three times the global figure — 2.1% vs 0.7%."),
  ],
  decode=[
    ("Commonest substance of abuse in India (national survey)", "Alcohol."),
    ("Substance more prevalent in children than adults", "Inhalants."),
    ("Second and third commonest substances", "Cannabis, then opioids."),
  ],
  punch="Alcohol dominates Indian substance use, cannabis and opioids follow — with opioid use three times the world rate — and inhalants are the drug of children.",
)

L['REC-02'] = dict(
  sub="Toxicology → Cannabis & Opioids → Cannabis",
  intro="Cannabis acts on the body’s own endocannabinoid system, a set of receptors that normally fine-tune neurotransmitter release. Where those receptors sit explains what the drug does: mainly brain effects — euphoria, slowed time, poor coordination, appetite — with little effect on breathing. That is why plain cannabis rarely kills and its treatment is supportive.",
  parts=[
    ('a', "**Delta-9-tetrahydrocannabinol.** THC is the main psychoactive cannabinoid of the plant. It is highly lipid-soluble, so it is stored in fat and released slowly, which is why a chronic user stays urine-positive for weeks (TOX-02)."),
    ('b', "**CB1: CNS (basal ganglia, cerebellum, hypothalamus). CB2: periphery (spleen, immune cells).** CB1 receptors sit on presynaptic nerve terminals and dampen neurotransmitter release; their distribution matches the effects — basal ganglia and cerebellum (incoordination), hypothalamus (appetite and temperature), hippocampus (memory). CB2 receptors are on immune cells and modulate inflammation. CB1 is scarce in the brainstem respiratory centres, which is why cannabis alone does not stop breathing."),
    ('c', "**Bhang (crushed leaves), ganja and charas (smoked), hashish (resin of flowering tops).** Bhang is made from leaves and is drunk or eaten, so its effect starts slowly and lasts longer. Ganja is the dried flowering tops; charas and hashish are concentrated resin, so they carry more THC per gram."),
    ('d', "**Supportive; a short-acting benzodiazepine for agitation; exclude other drugs.** There is no antidote; the dangerous features are panic, psychosis and tachycardia, which settle with calm and a benzodiazepine. Because cannabis seldom explains coma or seizures, those features point to a co-ingestant, a synthetic cannabinoid or another cause."),
  ],
  mimic=[
    ("Cannabis vs synthetic cannabinoids (spice, K2)", "Synthetic cannabinoids are full CB1 agonists: seizures, agitated delirium, hyperthermia and AKI — and they are missed by the urine drug screen."),
    ("Cannabis vs anticholinergic", "Both give tachycardia and confusion, but cannabis gives red conjunctivae with normal sweating and bowel; the anticholinergic patient is dry with urinary retention."),
  ],
  traps=[
    ("“CB1 receptors are mainly peripheral”", "CB1 is the central receptor; CB2 is on immune cells (REC-14a)."),
    ("“Cannabis causes coma and respiratory depression”", "Brainstem CB1 density is low, so breathing is spared; coma means look for something else."),
    ("“A negative urine screen excludes cannabinoid toxicity”", "Synthetic cannabinoids are not detected by the standard immunoassay."),
  ],
  decode=[
    ("Active principle of cannabis", "Delta-9-THC."),
    ("Receptor on immune cells / spleen", "CB2."),
    ("Seizures, delirium, AKI after ‘herbal smoke’, urine screen negative", "Synthetic cannabinoid."),
  ],
  punch="THC acts on central CB1 receptors that are scarce in the brainstem, so cannabis disturbs the mind but spares breathing — care is supportive, and anything worse means another drug.",
  extra=[dict(q="Synthetic cannabinoids: how do they differ from cannabis?", a="Full CB1 agonists: **seizures, agitated delirium, hyperthermia, AKI**; **not detected** on urine screening; treat with **benzodiazepines** and supportive care."),
         dict(q="Cyclical vomiting in a chronic cannabis user, relieved by hot showers?", a="**Cannabinoid hyperemesis syndrome** — the cure is stopping cannabis; haloperidol or topical capsaicin help acutely.")],
)

L['REC-03'] = dict(
  sub="Toxicology → Cannabis & Opioids → Opioid overdose and naloxone",
  intro="Opioids stimulate μ receptors in the brainstem, which blunts the response to carbon dioxide; breathing slows, then stops, and hypoxia is what kills. Naloxone is a competitive μ antagonist that displaces the opioid and restores breathing within minutes. The difficulty is that naloxone leaves the receptor sooner than most opioids do, so a patient who wakes can stop breathing again.",
  parts=[
    ('a', "**Coma, pinpoint pupils, respiratory depression.** μ stimulation depresses the reticular activating system (coma) and the respiratory centre (slow, shallow breathing), and releases the Edinger–Westphal nucleus from inhibition, so the pupils constrict (TOX-04). A respiratory rate below 12 in a drowsy patient with small pupils is the working definition."),
    ('b', "**3,6-diacetylmorphine; 2–3 times as potent as morphine.** The two acetyl groups make heroin far more lipid-soluble, so it crosses the blood–brain barrier quickly; in blood and brain it is rapidly deacetylated to 6-monoacetylmorphine and morphine, which act on the receptor. Faster entry gives the ‘rush’ and the greater potency."),
    ('c', "**0.2–0.4 mg IV or IM, repeated to a maximum of 2 mg (0.04 mg steps in the dependent).** The aim is breathing, not full wakefulness. In an opioid-dependent patient a large dose strips every receptor at once and causes abrupt withdrawal, so small steps are used and titrated to a respiratory rate of about 12 or more."),
    ('d', "**40–80 minutes (your notes also print 30–120): shorter than most opioids, so toxicity recurs.** Heroin itself is short-acting, but morphine, methadone and sustained-release preparations outlast a naloxone bolus. When the naloxone wears off the opioid still occupies the receptors, so the patient must be watched for re-sedation, not discharged on waking."),
    ('e', "**Two-thirds of the effective reversal dose per hour.** The dose that woke the patient is known to work; giving two-thirds of it every hour as an infusion keeps receptor occupancy roughly steady and avoids repeated boluses. It is adjusted to breathing and to signs of withdrawal."),
  ],
  mimic=[
    ("Opioid vs clonidine coma", "Both give miosis, coma and bradycardia, but clonidine responds poorly to naloxone (TOX-04)."),
    ("Naloxone pulmonary oedema vs heroin lung injury", "After abrupt reversal, a catecholamine surge and gasping against a closed glottis cause non-cardiogenic oedema — one reason naloxone is titrated."),
  ],
  traps=[
    ("“Naloxone outlasts the opioid, so one dose is enough”", "It lasts 40–80 minutes, less than most opioids; re-sedation is the rule with long-acting drugs (REC-14b)."),
    ("“Give 2 mg at once to any opioid overdose”", "In the dependent patient that precipitates violent withdrawal, even seizures; titrate from 0.04 mg."),
    ("“Still drowsy after naloxone — give more until fully awake”", "Naloxone restores breathing, not consciousness; once RR ≥12, look for a second cause (sedative, hypoglycaemia, head injury)."),
  ],
  decode=[
    ("Coma, pinpoint pupils, RR 6", "Opioid — naloxone."),
    ("Woke after naloxone, re-sedated an hour later", "Naloxone wore off before the opioid — infusion."),
    ("Naloxone infusion rate", "Two-thirds of the reversal dose per hour."),
  ],
  punch="Naloxone pushes the opioid off the μ receptor, but it leaves first — so it is titrated to breathing rather than wakefulness, and followed by an infusion or observation when the opioid will outlast it.",
  extra=[dict(q="Breathing restored by naloxone but patient still drowsy?", a="A **second cause** — co-ingested sedative (benzodiazepine, alcohol, gabapentinoid), **hypoglycaemia**, head injury or hypoxic brain injury."),
         dict(q="Pulmonary oedema after naloxone: mechanism?", a="**Non-cardiogenic**: catecholamine surge with negative-pressure breathing against a closed glottis; uncommon, but commoner after large, rapid doses.")],
)

L['REC-04'] = dict(
  sub="Toxicology → Cannabis & Opioids → Body packers",
  intro="A body packer swallows many tightly wrapped packets of heroin or cocaine to smuggle them across a border. Each packet holds many times a lethal dose. The packer is well while the wrapping holds; if one leaks, the gut absorbs a massive dose at once — and which drug is inside decides whether there is an antidote.",
  parts=[
    ('a', "**Massive toxicity from rupture of swallowed drug packets (heroin or cocaine).** The packets are made to survive transit, but gastric acid, bowel movement and time can split them. Because the gut wall absorbs freely, a single ruptured packet gives an overdose far larger than any street use. A packet that does not rupture can still obstruct the bowel."),
    ('b', "**Packets may be radio-opaque.** Densely wrapped packets with air or a wax rim often show as regular oval shapes on a plain abdominal film (TOX-08). The X-ray misses some, so CT is more sensitive and is used to confirm that all packets have passed."),
    ('c', "**Whole bowel irrigation for intact packets (standard teaching, not in your notes); laparotomy for a ruptured cocaine packet; naloxone infusion for heroin.** Polyethylene glycol flushes intact packets through before they break (TOX-09). Heroin leakage has a reliable antidote, so a naloxone infusion holds the patient while packets pass. Cocaine has none: continuing absorption brings seizures, hyperthermia and arrhythmia that benzodiazepines cannot outrun, so the packets must be removed surgically. Obstruction is the other indication for surgery."),
  ],
  table=dict(title="What to do with a body packer", head=["Situation", "Management"], rows=[["Asymptomatic, packets intact", "whole bowel irrigation, observe, CT to confirm clearance"], ["Heroin leak", "naloxone infusion, continue irrigation"], ["Cocaine leak (toxicity)", "**laparotomy** + benzodiazepines"], ["Bowel obstruction", "surgery"]]),
  mimic=[
    ("Body packer vs body stuffer", "A packer swallows well-made packets planned for smuggling (large dose, sealed); a stuffer hastily swallows loosely wrapped drug to evade arrest (smaller dose, leaks early)."),
  ],
  traps=[
    ("“Endoscopic removal of the packets”", "Endoscopy risks tearing a packet; it is generally avoided."),
    ("“A normal abdominal X-ray excludes packets”", "Plain films miss some; CT is more sensitive."),
    ("“Cocaine packer with seizures — benzodiazepines and wait for the packets to pass”", "There is no antidote for continuing absorption; the packets come out at laparotomy."),
  ],
  decode=[
    ("Traveller from an airport, asymptomatic, packets on X-ray", "Whole bowel irrigation."),
    ("Body packer with seizures, hyperthermia, tachycardia", "Ruptured cocaine packet — surgery."),
    ("Body packer with pinpoint pupils and apnoea", "Heroin leak — naloxone infusion."),
  ],
  punch="A body packer is safe only while every packet holds: flush the intact ones through, cover a heroin leak with naloxone, and take a leaking cocaine packet out surgically because nothing else can stop the absorption.",
)

L['REC-05'] = dict(
  sub="Toxicology → Stimulants → Cocaine",
  intro="Cocaine does two things at once. It blocks reuptake of noradrenaline, dopamine and serotonin, so the synapses fill with catecholamine and the patient becomes hot, hypertensive and agitated; and it blocks cardiac sodium channels, as a local anaesthetic does. Most of its harm comes from intense vasoconstriction and that sympathetic storm — which is why calming the brain comes before treating the blood pressure.",
  parts=[
    ('a', "**Tropane alkaloid; CNS stimulant.** Cocaine comes from the coca leaf and shares the tropane ring with atropine and scopolamine. It is an ester local anaesthetic as well as a stimulant, and that sodium-channel block explains its wide-QRS arrhythmias."),
    ('b', "**Hyperthermia, seizures, myocardial infarction, aortic dissection, stroke, rhabdomyolysis and AKI.** Coronary vasospasm, increased platelet aggregation and a higher oxygen demand cause infarction even in young patients with normal arteries. Sudden surges in blood pressure tear the aorta and rupture cerebral vessels. Agitation and muscle activity generate heat, break down muscle and release myoglobin, which injures the kidney."),
    ('c', "**Benzodiazepines; cooling; aggressive fluids for rhabdomyolysis.** Benzodiazepines reduce central sympathetic outflow, so the heart rate, blood pressure, agitation and heat production all fall together — they treat the cause. Cooling is active because the set point is normal (TOX-12). Fluids keep urine flowing to clear myoglobin."),
    ('d', "**Avoid pure beta-blockers: unopposed alpha stimulation. Use nitrates, calcium-channel blockers or phentolamine.** Cocaine stimulates both α- and β-receptors; β₂ stimulation partly offsets the α-mediated vasoconstriction. Block β alone and α-vasoconstriction is left unopposed, worsening coronary spasm and blood pressure. Nitrates and calcium-channel blockers relax coronary spasm, and phentolamine blocks α-receptors directly."),
    ('e', "**Sodium bicarbonate; lidocaine; lipid emulsion.** The wide QRS is sodium-channel block, so bicarbonate overcomes it as in a tricyclic overdose (TOX-07). Lidocaine is class Ib: it binds and leaves the channel quickly, so it is thought to compete with cocaine for the channel without deepening the block, unlike class Ia and Ic drugs; it is used if bicarbonate fails, accepting a small risk of lowering the seizure threshold. Lipid emulsion is a last-resort rescue in refractory arrest because cocaine is lipophilic."),
  ],
  mimic=[
    ("Cocaine vs amphetamine", "Both are sympathomimetic, but cocaine is short-acting and also blocks sodium channels (wide QRS); amphetamine lasts many hours."),
    ("Cocaine chest pain vs ordinary ACS", "Same work-up, but benzodiazepines come first, then aspirin and nitrates — and no pure beta-blocker."),
  ],
  traps=[
    ("“Beta-blocker for cocaine tachycardia or hypertension”", "Unopposed α stimulation worsens spasm and hypertension; the exam answer is avoid (REC-14c)."),
    ("“Class Ia or Ic anti-arrhythmic for cocaine VT”", "They deepen sodium-channel block; bicarbonate first, lidocaine is the acceptable anti-arrhythmic."),
    ("“Labetalol is safe in cocaine toxicity because it also blocks α”", "Given IV, labetalol is mainly a β-blocker (α:β roughly 1:7), so α-vasoconstriction is still left largely unopposed; nitrates, calcium-channel blockers or phentolamine are preferred."),
    ("“Paracetamol for cocaine hyperthermia”", "The heat is muscular and the set point normal; cool actively and sedate."),
  ],
  decode=[
    ("Young man, chest pain, ST elevation after cocaine — first drug", "Benzodiazepine (then aspirin, nitrates; PCI)."),
    ("Cocaine with wide QRS tachycardia", "Sodium bicarbonate."),
    ("Haemoptysis and diffuse infiltrates within 48 h of smoking crack", "Diffuse alveolar haemorrhage (crack lung)."),
  ],
  punch="Cocaine is a catecholamine storm plus a sodium-channel blocker: calm the brain with benzodiazepines, open the vessels without blocking β alone, and treat the wide QRS with bicarbonate.",
  extra=[dict(q="Cocaine STEMI: reperfusion strategy?", a="**Primary PCI** (spasm, dissection and thrombus are common); fibrinolysis is the fallback, with added dissection and bleeding risk."),
         dict(q="Cocaine withdrawal: what does it look like?", a="A **crash** — depression, hypersomnia and craving, not an autonomic storm.")],
)

L['REC-06'] = dict(
  sub="Toxicology → Stimulants → Amphetamines and MDMA",
  intro="Amphetamines push monoamines out of nerve terminals rather than only blocking their reuptake, so their effect is longer and stronger than cocaine’s. MDMA is the amphetamine with the biggest serotonin effect. In a crowded, hot dance venue that serotonin surge combines with exertion to drive temperature up, and with ADH release and heavy drinking to drive sodium down — those two are what kill.",
  parts=[
    ('a', "**Ecstasy (tablet), Molly (crystal).** Molly is sold as the ‘pure’ crystal or powder form, though street samples are often adulterated with cathinones or other drugs."),
    ('b', "**Releases and blocks reuptake of dopamine and serotonin; 5-HT2A agonist.** MDMA enters the nerve terminal through the transporter and reverses it, so serotonin (and dopamine and noradrenaline) pour out into the synapse; it also blocks reuptake. The serotonin release is far greater than with other amphetamines, which explains the empathy and closeness users seek and the serotonergic toxicity."),
    ('c', "**Serotonin syndrome; also hyperthermia and hyponatraemia (standard teaching, not in your notes).** Excess serotonin gives clonus, hyperreflexia and heat (REC-11, REC-13). Hyperthermia, worsened by dancing in a hot room, drives rhabdomyolysis, DIC and multi-organ failure. Serotonin also releases ADH, and users drink large volumes of water, so a dilutional, SIADH-type hyponatraemia develops and can cause cerebral oedema and seizures — especially in young women."),
    ('d', "**Parenteral benzodiazepines; nitroglycerine or nicardipine; no beta-blockers; external cooling.** Benzodiazepines lower central sympathetic drive and therefore the heat, the heart rate and the pressure together. If hypertension persists, a vasodilator is added; a beta-blocker is avoided for the same unopposed-α reason as with cocaine (REC-05). Cooling comes first if the temperature is high, because temperature predicts death."),
  ],
  mimic=[
    ("MDMA vs cocaine", "Bruxism and jaw clenching, hyponatraemia and long duration point to MDMA; cocaine is short-acting with a wide QRS."),
    ("MDMA hyponatraemia vs exercise-associated hyponatraemia", "Both are dilutional; MDMA adds drug-driven ADH release (urine inappropriately concentrated)."),
  ],
  traps=[
    ("“Treat MDMA hypertension with a beta-blocker”", "Unopposed α stimulation; benzodiazepine first, then a vasodilator."),
    ("“Fit at a rave — give phenytoin and normal saline”", "Check sodium: seizures with severe hyponatraemia need 3% saline boluses."),
    ("“Dantrolene for MDMA hyperthermia”", "Evidence is limited to case reports and it is not standard care; the heat comes from central drive and muscle activity, not a ryanodine-receptor leak — cool, sedate, paralyse above 41 °C."),
  ],
  decode=[
    ("Rave, seizures, sodium 118", "MDMA hyponatraemia — 3% saline."),
    ("Rave, temperature 41.5 °C, clonus", "MDMA serotonin toxicity — cooling, benzodiazepines, paralysis."),
    ("Jaw clenching and bruxism", "MDMA."),
  ],
  punch="MDMA is the serotonin amphetamine: the serotonin surge brings heat, clonus and ADH release, so temperature and sodium decide survival — cool first, sedate with benzodiazepines, and never use a beta-blocker.",
  extra=[dict(q="MDMA hyponatraemia with seizures: treatment?", a="**3% saline, 100–150 mL boluses**; mild cases fluid restriction. It is SIADH-type (urine osmolality >100, urine Na >30) plus water loading.")],
)

L['REC-07'] = dict(
  sub="Toxicology → Stimulants → Sympathomimetic toxidrome",
  intro="Every feature of the sympathomimetic toxidrome is the fight-or-flight response turned up and left on. Cocaine, amphetamines, MDMA and cathinones flood the synapses with noradrenaline and dopamine, so each organ shows its sympathetic action. Going system by system is just going round the body and asking what adrenaline does there.",
  parts=[
    ('a', "**CNS: euphoria, agitation, psychosis, seizures.** Dopamine excess in reward pathways gives euphoria; more of it gives paranoia and psychosis that looks like schizophrenia. At high levels the cortex becomes hyperexcitable and seizes, and agitation itself adds heat and acidosis."),
    ('b', "**Neuromuscular: hyperreflexia, tremor.** Raised central drive and β₂ stimulation of muscle make reflexes brisk and produce tremor — but without the inducible clonus that marks serotonin toxicity (REC-12)."),
    ('c', "**Autonomic: hyperthermia, sweating, mydriasis.** Heat comes from muscle activity and vasoconstriction that stops the skin losing it. Sweating continues because sympathetic sweat fibres use acetylcholine and are driven, not blocked — the key difference from the anticholinergic patient (TOX-03). The pupils dilate through α₁ action on the dilator muscle."),
    ('d', "**Cardiovascular: tachycardia, hypertension, arrhythmia.** β₁ stimulation speeds and strengthens the heart; α₁ vasoconstriction raises the pressure. The combination raises myocardial oxygen demand while narrowing coronary supply, so ischaemia and arrhythmia follow."),
    ('e', "**GI: nausea, vomiting, diarrhoea.** These are common but non-specific; importantly, bowel sounds are present, unlike the silent bowel of anticholinergic poisoning."),
  ],
  mimic=[
    ("Sympathomimetic vs anticholinergic", "Both hot, fast and dilated; the sympathomimetic patient sweats and has bowel sounds, the anticholinergic is dry with retention."),
    ("Sympathomimetic vs serotonin syndrome", "Both sweat with brisk reflexes; clonus (inducible or ocular) belongs to serotonin toxicity."),
    ("Sympathomimetic vs alcohol or benzodiazepine withdrawal", "Look alike at the bedside and both settle with benzodiazepines; only the history (recent stopping of alcohol or sedatives) separates them."),
  ],
  traps=[
    ("“Dilated pupils and fever — anticholinergic”", "Shared with sympathomimetics; check the skin (TOX-03)."),
    ("“Hyperreflexia means serotonin syndrome”", "Sympathomimetics give brisk reflexes too; clonus is the serotonin sign."),
  ],
  decode=[
    ("Agitated, sweating, mydriatic, BP 210/120", "Sympathomimetic."),
    ("Paranoid psychosis after several days of a stimulant binge", "Amphetamine (methamphetamine) psychosis."),
  ],
  punch="The sympathomimetic toxidrome is adrenaline on every organ — hot, fast, hypertensive and dilated — and, unlike the anticholinergic, still sweating with bowel sounds present.",
)

L['REC-08'] = dict(
  sub="Toxicology → Hallucinogens & Sedatives → Hallucinogens",
  intro="Most classic hallucinogens act as agonists at the 5-HT2A receptor in the cortex, which scrambles the way sensory input is filtered and gives visions, synaesthesia and a distorted sense of self. A second group — phencyclidine and ketamine — block the NMDA glutamate receptor instead and cut the mind off from the body (dissociation). The physical danger is usually small; the danger is behaviour, panic and, occasionally, heat.",
  parts=[
    ('a', "**LSD: ergot-derived; synaesthesia, panic, hyperthermia.** Lysergic acid diethylamide is made from lysergic acid, found in the ergot fungus, and is active in microgram doses. Strong 5-HT2A agonism mixes the senses (seeing sounds) and can cause terrifying ‘bad trips’; with large doses mild sympathetic stimulation and hyperthermia occur."),
    ('b', "**Psilocybin: magic mushrooms; active form psilocin.** Psilocybin is a prodrug: it is dephosphorylated to psilocin, the molecule that acts at 5-HT2A. The main real-world risk is eating a toxic mushroom by mistake."),
    ('c', "**Mescaline: phenylethylamine (peyote).** Mescaline comes from the peyote cactus and is chemically a phenylethylamine — the same backbone as amphetamine and MDMA — which is why it carries some sympathetic effects with its visions."),
    ('d', "**Phencyclidine: angel dust; nystagmus, violence.** PCP blocks NMDA receptors; that dissociation with anaesthesia to pain lets patients become violent and injure themselves without noticing. Nystagmus — horizontal, vertical or rotatory — is its bedside signature (TOX-05)."),
    ('e', "**Ketamine: NMDA antagonist; dissociation.** Ketamine is the shorter-acting relative of PCP: dissociation, nystagmus, raised heart rate and blood pressure, with airway reflexes and breathing usually preserved — which is why it is used as an anaesthetic."),
    ('f', "**Salvia: salvinorin A.** Salvinorin A, from Salvia divinorum, is unusual in being a κ-opioid agonist rather than a serotonin or NMDA drug; it gives intense, very brief dissociation."),
  ],
  mimic=[
    ("Classic hallucinogen vs dissociative", "LSD and psilocybin (5-HT2A) alter perception with insight largely kept; PCP and ketamine (NMDA) dissociate and add nystagmus."),
    ("PCP vs sympathomimetic", "Both agitated, hypertensive and violent; nystagmus points to PCP."),
  ],
  traps=[
    ("“Activated charcoal and an antidote for hallucinogens”", "There is no antidote and charcoal does not help; a quiet room and benzodiazepines are the treatment."),
    ("“Ketamine is a GABA agonist”", "It is an NMDA antagonist (REC-14d)."),
    ("“Psilocybin is the active molecule”", "It is a prodrug; psilocin acts."),
  ],
  decode=[
    ("Violent, analgesic, vertical nystagmus", "Phencyclidine."),
    ("Synaesthesia after a blotter tab", "LSD."),
    ("Magic mushrooms — active compound", "Psilocin."),
  ],
  punch="Hallucinogens split into 5-HT2A agonists that distort perception (LSD, psilocybin, mescaline) and NMDA antagonists that dissociate with nystagmus (PCP, ketamine) — neither has an antidote, so quiet and benzodiazepines are the treatment.",
  extra=[dict(q="An over-the-counter dissociative often combined with paracetamol?", a="**Dextromethorphan** (NMDA antagonist) — check a **paracetamol level**; agitation gets benzodiazepines.")],
)

L['REC-09'] = dict(
  sub="Toxicology → Hallucinogens & Sedatives → Sedative street drugs",
  intro="Flunitrazepam and GHB are both used to sedate a victim without their knowledge (‘date-rape drugs’) because they are tasteless in a drink, act fast and erase memory of the events. Both enhance GABA inhibition, so the picture is sedation and amnesia — and, as with all sedative-hypnotics, the vital signs stay surprisingly normal until coma is deep.",
  parts=[
    ('a', "**Rohypnol: a benzodiazepine 10 times as potent as diazepam; acts in 10–20 minutes for 4–6 hours; detected as a benzodiazepine on screening.** Flunitrazepam binds the GABA-A benzodiazepine site with high affinity, so a 1–2 mg tablet sedates strongly. Its rapid onset and anterograde amnesia are what make it a drug of assault — and sedation and amnesia often last well beyond 4–6 hours (8–12 hours or more is described); alcohol greatly deepens the sedation and respiratory depression."),
    ('b', "**Gamma-hydroxybutyrate: liquid, mixed with alcohol; euphoria, amnesia, hypotonia, then sudden coma; supportive care.** GHB acts mainly on GABA-B receptors. It has a steep dose–response curve, so a little more than the euphoric dose gives coma within minutes — often with bradycardia and myoclonus — and, characteristically, the patient wakes abruptly a few hours later. Airway support is all that is needed; there is no antidote."),
    ('c', "**CNS depression with near-normal vital signs and reflexes.** Sedative-hypnotics depress the cortex and reticular activating system long before they affect the brainstem centres that control breathing and circulation. So the patient is deeply asleep with a nearly normal pulse, blood pressure and breathing — unless alcohol or an opioid is added (TOX-04)."),
  ],
  mimic=[
    ("GHB vs opioid coma", "GHB coma comes on suddenly and ends abruptly, often with bradycardia and myoclonus, and does not respond to naloxone."),
    ("Sedative-hypnotic vs opioid", "Opioid: pinpoint pupils and a very slow respiratory rate. Sedative: variable pupils, near-normal breathing, often nystagmus."),
  ],
  traps=[
    ("“Flumazenil to reverse a suspected Rohypnol drink”", "Rarely given — seizure risk in dependence or mixed ingestion; support the airway (TOX-01)."),
    ("“Profound coma means respiratory failure in a sedative overdose”", "Vital signs stay near normal unless alcohol or opioids are added."),
    ("“A negative screen excludes a drink spiked with GHB”", "GHB is not on the standard urine immunoassay."),
  ],
  decode=[
    ("Sudden coma at a party, wakes abruptly after 3 hours", "GHB."),
    ("Amnesia after a spiked drink, benzodiazepine-like", "Flunitrazepam."),
    ("Deep coma with normal vital signs", "Sedative-hypnotic toxidrome."),
  ],
  punch="Flunitrazepam and GHB both deepen GABA inhibition — sedation and amnesia with near-normal vital signs — and GHB adds a sudden coma that ends as suddenly, needing only airway support.",
)

L['REC-10'] = dict(
  sub="Toxicology → Hallucinogens & Sedatives → Volatile solvents",
  intro="Volatile solvents — toluene, butane, propane and other hydrocarbons — are inhaled from a bag or rag (‘huffing’, ‘bagging’). They behave like inhaled anaesthetics: fat-soluble, taken up and cleared through the lungs within minutes. The acute danger is not the intoxication but the heart; the chronic danger is to every lipid-rich tissue, especially the brain.",
  parts=[
    ('a', "**Glue, lighter refills, spray deodorants; street children.** These products are cheap, legal and sold everywhere, so they are the drug of the poorest and youngest users (REC-01). Toluene is the usual solvent in glue; butane and propane fill lighters and aerosol propellants."),
    ('b', "**Sudden sniffing death syndrome: arrhythmia (myocardium sensitised to catecholamines).** Halogenated and hydrocarbon solvents make the myocardium excitable, so a surge of adrenaline — a fright, being chased or startled, sudden exertion — triggers ventricular fibrillation. Hypoxia from rebreathing in a bag adds to it. This is why the user should be approached calmly, and adrenaline is used with great care."),
    ('c', "**Neurological, lung, liver and kidney damage.** Solvents dissolve into myelin: chronic toluene use gives white-matter loss (leukoencephalopathy), cerebellar ataxia and dementia. Toluene also causes distal renal tubular acidosis with hypokalaemia. Other solvents have their own targets — n-hexane causes peripheral neuropathy, and chlorinated solvents injure the liver."),
  ],
  mimic=[
    ("Solvent coma vs heroin coma", "Solvent coma clears within minutes of removal from the vapour; heroin coma lasts hours and responds to naloxone."),
    ("Toluene vs other causes of hypokalaemic acidosis", "Toluene gives a normal anion gap acidosis from distal RTA, with very low potassium and weakness."),
  ],
  traps=[
    ("“Sudden death in huffing is from asphyxia alone”", "The main mechanism is catecholamine-sensitised VF, often triggered by fright or exertion."),
    ("“Give adrenaline freely to a solvent abuser in arrest”", "The myocardium is sensitised to catecholamines; adrenaline may perpetuate VF — β-blockade has been used for refractory arrhythmia."),
  ],
  decode=[
    ("Teenager collapses while running from police after sniffing glue", "Sudden sniffing death — VF."),
    ("Chronic glue sniffer with weakness, hypokalaemia, normal anion gap acidosis", "Toluene — distal RTA."),
    ("Solvent abuser, GCS 3 recovering to 15 within minutes", "Volatile solvent cleared through the lungs."),
  ],
  punch="Solvents are cheap anaesthetic vapours: they wear off in minutes, but they sensitise the heart to adrenaline — so fright can cause fatal VF — and with chronic use they dissolve the brain’s myelin.",
)

L['REC-11'] = dict(
  sub="Toxicology → Hyperthermic Toxidromes → Serotonin syndrome vs NMS",
  intro="Both syndromes give a hot, confused, rigid patient on psychiatric drugs, and both can kill through hyperthermia and rhabdomyolysis. But they arise from opposite neurochemistry: serotonin syndrome is too much serotonin stimulation, NMS is too little dopamine action. Too much serotonin excites — fast onset, clonus, brisk reflexes; too little dopamine freezes — slow onset, rigidity, slow reflexes.",
  parts=[
    ('a', "**Cause: serotonin syndrome — excess serotonin, usually two serotonergic drugs; NMS — dopamine blockade, or stopping a dopamine agonist.** Serotonin syndrome usually follows adding a second serotonergic drug (TOX-05). NMS follows a dopamine D₂ antagonist — antipsychotics, metoclopramide — or abrupt withdrawal of levodopa in Parkinson’s disease, which removes dopamine action in the same way."),
    ('b', "**Onset: serotonin syndrome under 12 hours; NMS 1–3 days.** Serotonin excess is a direct pharmacological effect, so it appears within hours of the dose change. NMS develops gradually as dopamine block in the hypothalamus and basal ganglia builds up, over days."),
    ('c', "**Pupils: serotonin syndrome dilated; NMS normal.** Serotonin excess drives the sympathetic system and dilates the pupil; dopamine block has no such effect."),
    ('d', "**Tone: serotonin syndrome increased, in the legs; NMS lead-pipe rigidity.** Serotonin excitation of spinal motor neurones raises tone mostly in the lower limbs. Loss of dopamine in the basal ganglia produces generalised parkinsonian ‘lead-pipe’ rigidity, uniform throughout the range of movement."),
    ('e', "**Reflexes: serotonin syndrome hyperreflexia and clonus; NMS bradyreflexia.** This is the most reliable discriminator: clonus means serotonin. In NMS the rigid muscle and slowed motor system give sluggish reflexes."),
    ('f', "**Bowel: serotonin syndrome hyperactive; NMS normal.** Most of the body’s serotonin is in the gut, where it drives motility, so serotonin excess gives diarrhoea and loud bowel sounds."),
    ('g', "**Treatment: serotonin syndrome — cyproheptadine; NMS — bromocriptine, dantrolene.** Both start with stopping the drug, benzodiazepines and cooling. Cyproheptadine blocks 5-HT2A receptors (REC-13). Bromocriptine is a dopamine agonist that replaces the missing dopamine action; dantrolene relaxes skeletal muscle by blocking calcium release, reducing heat production."),
  ],
  table=dict(title="Opposite chemistry, opposite signs", head=["", "Serotonin syndrome", "NMS"], rows=[["Problem", "too much serotonin", "too little dopamine"], ["Onset", "**<12 h**", "**1–3 days**"], ["Tone, reflexes", "legs > arms, **clonus**", "**lead-pipe**, slow reflexes"], ["Pupils, bowel", "dilated, hyperactive", "normal, normal"], ["Specific drug", "cyproheptadine", "bromocriptine, dantrolene"]]),
  mimic=[
    ("NMS vs malignant hyperthermia", "Both rigid and hot with high CK; MH happens in theatre after a volatile agent or suxamethonium, with rising ETCO₂."),
    ("Serotonin syndrome vs anticholinergic", "Both hot with dilated pupils; the anticholinergic patient is dry with a silent bowel and no clonus."),
  ],
  traps=[
    ("“NMS shows hyperreflexia and clonus”", "NMS gives slow reflexes; clonus is serotonin (REC-14e)."),
    ("“Bromocriptine for serotonin syndrome”", "A dopamine agonist can worsen serotonin toxicity; it is for NMS."),
    ("“Haloperidol to sedate the agitated patient”", "In NMS it is the cause, and in serotonin syndrome it does not treat the serotonin excess and may add dopamine-block rigidity. Use benzodiazepines."),
  ],
  decode=[
    ("Schizophrenic on haloperidol for 3 days, rigid, CK 20 000, temperature 40 °C", "NMS."),
    ("On sertraline, given tramadol, sweating, clonus within hours", "Serotonin syndrome."),
    ("Parkinson’s patient, levodopa stopped, rigid and febrile", "NMS (parkinsonism–hyperpyrexia)."),
  ],
  punch="Serotonin syndrome is excess serotonin — fast, twitchy, clonus and dilated pupils within hours; NMS is lost dopamine — slow, stiff, lead-pipe rigidity with slow reflexes over days.",
)

L['REC-12'] = dict(
  sub="Toxicology → Hyperthermic Toxidromes → The five hyperthermic toxidromes",
  intro="Five drug-related syndromes can push the temperature to lethal levels. In all of them the heat comes from the body producing or holding heat — muscle activity, hypermetabolism or lost sweating — not from a raised hypothalamic set point, so antipyretics do nothing and every one is cooled actively. What separates them is one bedside sign each, and that sign decides the specific treatment.",
  parts=[
    ('a', "**Sympathomimetic: sweaty, extreme hypertension — benzodiazepines.** Catecholamine excess raises heat production and blood pressure while sweating continues (REC-07). Benzodiazepines lower central sympathetic drive and so treat both."),
    ('b', "**Anticholinergic: dry, non-reactive pupils, retention, absent bowel sounds — physostigmine (severe).** Muscarinic block stops sweating, so heat cannot be lost; it also paralyses the pupil, the bladder and the gut (TOX-03). Physostigmine inhibits acetylcholinesterase and crosses into the brain, so it reverses both the delirium and the peripheral signs; it is kept for severe cases and avoided when the ECG shows conduction delay."),
    ('c', "**Serotonin: clonus, hyperreflexia — cyproheptadine.** Spinal 5-HT2A stimulation gives clonus, which no other toxidrome here produces (REC-13)."),
    ('d', "**NMS: lead-pipe rigidity, slow reflexes — bromocriptine.** Dopamine block causes the rigidity and impairs central heat regulation; bromocriptine replaces dopamine action (REC-11)."),
    ('e', "**Malignant hyperthermia: rising CO₂, rigor despite relaxant; temperature often above 42 °C — dantrolene.** In susceptible patients a volatile agent or suxamethonium opens the abnormal ryanodine receptor, calcium floods the muscle cytoplasm, and the muscles contract and burn energy uncontrollably. That hypermetabolism first shows as a rising end-tidal CO₂ and tachycardia; temperature rises later. Dantrolene blocks the ryanodine receptor and stops the calcium release — which is why it is the specific cure here, where the problem is in the muscle itself, and at most an adjunct in the other toxidromes."),
  ],
  table=dict(title="One sign each", head=["Toxidrome", "The giveaway", "Specific treatment"], rows=[["Sympathomimetic", "**wet** + very high BP", "benzodiazepines"], ["Anticholinergic", "**dry**, retention, silent bowel", "physostigmine (severe)"], ["Serotonin", "**clonus**", "cyproheptadine"], ["NMS", "**lead-pipe**, slow reflexes", "bromocriptine"], ["Malignant hyperthermia", "**rising ETCO₂** in theatre", "dantrolene"]]),
  mimic=[
    ("Sympathomimetic vs anticholinergic", "The skin: wet vs dry."),
    ("Serotonin vs NMS", "Clonus and hours vs rigidity and days."),
    ("Malignant hyperthermia vs NMS", "MH: minutes to hours in theatre after a trigger; NMS: days after an antipsychotic."),
  ],
  traps=[
    ("“Paracetamol for toxic hyperthermia (your notes list it under cocaine)”", "The set point is normal; all five are cooled actively."),
    ("“Dantrolene for cocaine or MDMA hyperthermia”", "Only case reports support it, and it is not standard care; the heat is central and muscular drive, not a ryanodine-receptor leak. Cool, sedate, paralyse above 41 °C."),
    ("“Physostigmine for any agitated, dry patient”", "Avoid with QRS widening or suspected tricyclic — it can cause bradyasystole; also asthma and conduction defects."),
  ],
  decode=[
    ("Which hyperthermic toxidrome is dry?", "Anticholinergic."),
    ("Rising ETCO₂, tachycardia, masseter rigidity under sevoflurane", "Malignant hyperthermia — dantrolene."),
    ("Hyperthermic toxidrome with clonus", "Serotonin syndrome."),
  ],
  punch="Five syndromes, one heat mechanism — muscle and lost cooling, never the thermostat — so all are cooled actively, and the giveaway sign (wet, dry, clonus, lead-pipe, rising CO₂) picks the specific drug.",
  extra=[dict(q="Malignant hyperthermia: dantrolene dose?", a="**2.5 mg/kg IV**, repeated every 5–10 minutes until the crisis settles; usual upper limit about **10 mg/kg**, though more is occasionally needed."),
         dict(q="Physostigmine contraindications?", a="**Wide QRS or AV block (and suspected tricyclic overdose)**, asthma or reactive airways disease, and mechanical bowel or bladder obstruction."),
         dict(q="Physostigmine: adult dose?", a="**0.5–2 mg IV slowly over at least 5 minutes** (no faster than about 1 mg/min), repeated if needed; child 0.02 mg/kg. Atropine must be at hand.")],
)

L['REC-13'] = dict(
  sub="Toxicology → Hyperthermic Toxidromes → Serotonin syndrome: diagnosis and treatment",
  intro="Serotonin syndrome has no laboratory test; it is a clinical diagnosis made at the bedside in a patient exposed to a serotonergic drug. Its severity ranges from tremor and a little sweating to a temperature above 41 °C with rigidity. Treatment rests mostly on removing the drug and controlling heat and agitation; the specific antidote is a helper rather than a cure.",
  parts=[
    ('a', "**Altered mental status, autonomic hyperactivity, neuromuscular abnormality.** Serotonin excess acts in three places: the brain (agitation, confusion), the autonomic system (sweating, tachycardia, mydriasis, diarrhoea, heat) and the spinal cord (tremor, hyperreflexia, clonus). The neuromuscular part is the most specific."),
    ('b', "**Hunter criteria (sensitivity 84%, specificity 97%); Sternbach (75%, 96%).** The Hunter criteria require a serotonergic drug plus one of: spontaneous clonus; inducible clonus with agitation or sweating; ocular clonus with agitation or sweating; tremor with hyperreflexia; or hypertonia with temperature above 38 °C and ocular or inducible clonus. Because they are built on clonus, they are more accurate than the older Sternbach criteria, which counted non-specific features that overlap with NMS and sympathomimetic toxicity."),
    ('c', "**Serotonin (5-HT2A) antagonist: 2 mg per dose to a maximum of 12 mg; maintenance 8 mg every 6 hours. Usual regimen: 12 mg, then 2 mg every 2 hours (standard teaching, not in your notes).** Cyproheptadine is a first-generation antihistamine that also blocks 5-HT2A (and 5-HT1A) receptors. The larger initial dose is chosen because 12–32 mg over 24 hours is estimated to bind 85–95% of serotonin receptors; the notes’ ‘maximum of 12 mg’ does not fit the standard regimen. It exists only as an oral preparation, so in a sedated patient it is crushed and given by nasogastric tube."),
    ('d', "**Symptom relief only; no proven effect on outcome.** There are no controlled trials; case series show it eases symptoms. Survival depends on stopping the drug, benzodiazepines, active cooling and, above 41 °C, paralysis with a non-depolarising relaxant and ventilation, which stops the muscle heat at its source."),
  ],
  mimic=[
    ("Hunter vs Sternbach", "Hunter rests on clonus and is more specific; Sternbach counts broader features and catches NMS and stimulant toxicity by mistake."),
  ],
  traps=[
    ("“Cyproheptadine is the mainstay and improves survival”", "It relieves symptoms only; supportive care, cooling and paralysis save life."),
    ("“Paralyse the hyperthermic patient with suxamethonium”", "Use a non-depolarising agent — rhabdomyolysis raises potassium, which suxamethonium worsens."),
    ("“Give IV cyproheptadine”", "It is oral only — crushed via nasogastric tube."),
  ],
  decode=[
    ("Best diagnostic criteria for serotonin syndrome", "Hunter."),
    ("Temperature 41.5 °C, rigid, on SSRI and linezolid", "Paralysis and ventilation, cooling, benzodiazepines."),
    ("Cyproheptadine loading dose", "12 mg, then 2 mg every 2 hours."),
  ],
  punch="Serotonin syndrome is diagnosed by clonus (Hunter criteria) and survived by removing the drug and stopping the heat — cyproheptadine eases the symptoms but has never been shown to change the outcome.",
)

L['REC-14'] = dict(
  sub="Toxicology → Revision → True or false",
  intro="This card tests the deck’s key distinctions. Each statement turns on one mechanism from an earlier card; the reason for each answer is the physiology met there.",
  parts=[
    ('a', "**False — CB1 is central; CB2 is peripheral.** CB1 receptors sit on brain nerve terminals (basal ganglia, cerebellum, hypothalamus); CB2 is on immune cells (REC-02)."),
    ('b', "**False — naloxone lasts 40–80 minutes.** That is shorter than most opioids, so sedation recurs as it wears off (REC-03)."),
    ('c', "**False — avoid beta-blockers; give benzodiazepines.** Blocking β alone leaves α-vasoconstriction unopposed; benzodiazepines reduce the sympathetic drive itself (REC-05)."),
    ('d', "**True — ketamine is an NMDA antagonist,** which gives its dissociation and nystagmus (REC-08)."),
    ('e', "**False — hyperreflexia and clonus are serotonin syndrome.** NMS gives lead-pipe rigidity with slow reflexes (REC-11)."),
    ('f', "**True — malignant hyperthermia is treated with dantrolene,** which blocks calcium release from the abnormal ryanodine receptor (REC-12)."),
    ('g', "**False — anticholinergic skin is dry.** Sweat glands work through muscarinic receptors (TOX-03)."),
    ('h', "**True — serotonin syndrome begins within 12 hours** of the drug change, unlike NMS, which takes days (REC-11)."),
  ],
  mimic=[],
  traps=[
    ("“Naloxone wakes the patient for good”", "It wears off before most opioids."),
    ("“Clonus can occur in NMS”", "Clonus is the serotonin sign; NMS is slow and stiff."),
  ],
  decode=[
    ("Statements about hyperthermic toxidromes", "Check the reflexes and the onset: clonus and hours mean serotonin, rigidity and days mean NMS."),
    ("Statements about stimulant hypertension", "Benzodiazepines first, no pure beta-blocker."),
  ],
  punch="Every statement here turns on a mechanism from the deck — where CB1 sits, how long naloxone lasts, unopposed α, clonus versus rigidity, and the sweat gland’s muscarinic receptor.",
)

L['REC-15'] = dict(
  sub="Toxicology → Hyperthermic Toxidromes → Temperature, onset and reflexes",
  intro="Once the skin and the giveaway sign are known (REC-12), three more features sort the hyperthermic toxidromes: how hot, how fast and what the reflexes do. The drug-induced syndromes that act directly — sympathomimetic, anticholinergic, serotonin — appear within hours; NMS needs days; malignant hyperthermia is the hottest because the muscle itself is out of control.",
  parts=[
    ('a', "**Sympathomimetic: above 38 °C, under 12 hours, brisk reflexes.** Catecholamine excess is immediate, and central excitation makes reflexes brisk without clonus (REC-07)."),
    ('b', "**Anticholinergic: above 38 °C, under 12 hours, normal reflexes.** The drug blocks muscarinic receptors, which do not run the spinal reflex arc, so reflexes stay normal; the heat comes from absent sweating and agitation."),
    ('c', "**Serotonin: above 38 °C, under 12 hours, clonus (ocular too).** Serotonin acts on spinal motor neurones, giving hyperreflexia and inducible, spontaneous or ocular clonus — slow, side-to-side eye movements (REC-13)."),
    ('d', "**NMS: 39–42 °C, 1–3 days, slow reflexes.** Dopamine block builds up over days; rigid muscle generates heat and blunts the reflexes (REC-11)."),
    ('e', "**Malignant hyperthermia: often above 42 °C, 30 minutes to 24 hours, hyporeflexia.** Uncontrolled calcium release keeps every muscle fibre contracting, so heat production is enormous and temperature can climb by 1 °C or more every 5 minutes in a fulminant case. It usually starts in theatre during or soon after exposure to the trigger; in the anaesthetised, relaxant-given patient reflexes are depressed."),
  ],
  table=dict(title="How hot, how fast, which reflexes", head=["Toxidrome", "Temp (°C)", "Onset", "Reflexes"], rows=[["Sympathomimetic", ">38", "<12 h", "brisk"], ["Anticholinergic", ">38", "<12 h", "normal"], ["Serotonin", ">38", "<12 h", "**clonus**"], ["NMS", "39–42", "**1–3 days**", "slow"], ["Malignant hyperthermia", "**often >42**", "30 min–24 h", "hyporeflexia"]]),
  mimic=[
    ("Malignant hyperthermia vs NMS", "Both rigid with high CK; MH follows a trigger within the anaesthetic, NMS takes days after an antipsychotic."),
  ],
  traps=[
    ("“Temperature is the first sign of malignant hyperthermia”", "A rising ETCO₂ and tachycardia come first; the temperature rises later."),
    ("“Propofol or rocuronium can trigger malignant hyperthermia”", "Only volatile agents and suxamethonium trigger it; propofol, opioids, ketamine and non-depolarising relaxants are safe."),
    ("“Nitrous oxide is a trigger”", "It is the exception — not a trigger."),
  ],
  decode=[
    ("Hyperthermic toxidrome developing over 2 days", "NMS."),
    ("Temperature 43 °C during anaesthesia", "Malignant hyperthermia."),
    ("Ocular clonus", "Serotonin syndrome."),
  ],
  punch="Hours and brisk reflexes or clonus mean a drug acting directly (sympathomimetic, serotonin); days and slow reflexes mean NMS; the hottest of all, in theatre, is malignant hyperthermia, where the muscle itself burns.",
  extra=[dict(q="Malignant hyperthermia: genetics and triggers?", a="**Autosomal dominant RYR1** (or CACNA1S) mutation; triggered only by **volatile agents and suxamethonium**.")],
)

FLAGS = {}
FLAGS['REC-01'] = "Part c ‘In children: inhalants’ — the 2019 national survey’s point is that inhalants are the only class used MORE by children than adults (about 1.17% vs 0.58%); inhalants are not the commonest substance in children overall (alcohol and opioids are reported higher). Worth rewording to ‘used more by children than adults’. Check against the report."
FLAGS['REC-03'] = "Part c ‘maximum of 2 mg’ — 2 mg is not a true ceiling: if no response, doses up to about 10 mg are given before excluding opioid toxicity (more relevant with fentanyl analogues). Consistent with TOX-01, so left as is in the explanation."
FLAGS['REC-09'] = "Part a ‘detected as a benzodiazepine on screening’ — flunitrazepam is often NOT detected on routine urine benzodiazepine immunoassays (low dose, poor cross-reactivity of 7-aminoflunitrazepam); specific assays are needed. Also ‘lasts 4–6 hours’ is short: sedation and amnesia are described as lasting 8–12 hours or more (US DOJ Rohypnol fact sheet: onset 15–20 min, effects >12 h)."
FLAGS['REC-13'] = "Part c ‘2 mg per dose to a maximum of 12 mg’ — does not match the standard regimen (Boyer & Shannon, NEJM 2005): 12 mg initially, then 2 mg every 2 hours while symptoms persist, maintenance 8 mg every 6 hours, about 12–32 mg per 24 h. The card already adds the standard regimen; the notes’ line should probably go."
FLAGS['REC-15'] = "WATCH ‘temperature climbs 1 degree every 10 minutes’ — standard texts quote a rise of about 1 °C (up to 2 °C) every 5 minutes in fulminant malignant hyperthermia. ‘All inhaled agents except nitrous oxide’ is better phrased ‘all volatile agents’ (xenon also does not trigger). Onset ‘up to 24 h’ is generous; most cases start intra-operatively or within about an hour after (PACU)."
