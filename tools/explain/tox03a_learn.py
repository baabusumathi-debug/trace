# TOX03A — Explain v2 ("Learn" depth). Organophosphates & carbamates. No mnemonics or hooks.
# Fields per card: sub, intro, parts, table (optional), mimic, traps, decode, punch, extra (optional)
# Audited 6 Nov against qpack/TOX03A.md (real stems): decode from real stems, traps from low-% distractors, cuts.
L = {}

L['PEST-01'] = dict(
  sub="Toxicology → Pesticides → Scale and WHO hazard classes",
  intro="Organophosphates are the single biggest cause of fatal poisoning in the developing world, because they are cheap, sold without control and kept in the homes of farming families. Most deaths are deliberate self-poisoning. The WHO grades the compounds by how little of them kills a rat, which is the only practical way of saying in advance how dangerous a bottle is.",
  parts=[
    ('a', "**About 3 million people exposed and up to 300,000 deaths a year; the commonest poisoning in developing countries.** In India poisoning is predominantly rural and agricultural, and organophosphates are among its commonest causes. Case fatality — of the order of 10–20% in South Asian series — is far higher than in Western data, because the dose swallowed is large, the hospital is far and ventilation is scarce."),
    ('b', "**Class Ia extremely hazardous, oral LD50 <5 mg/kg; Ib highly hazardous 5–50; II moderately hazardous 50–2000; III slightly hazardous >2000; U unlikely to be hazardous ≥5000.** The LD50 is the single oral dose that kills half of a group of rats, so the lower the LD50, the higher the hazard."),
  ],
  mimic=[
    ("WHO hazard class vs clinical severity", "Class reflects intrinsic toxicity. Severity in the patient is set by the amount, formulation and delay, and is graded by RBC cholinesterase activity (PEST-09)."),
  ],
  traps=[
    ("“Poisoning, and pesticide poisoning, are mainly urban; mortality matches Western data”", "In India both are mainly rural, and mortality is much higher than in the West."),
    ("“A high WHO class number means a more dangerous pesticide”", "It is the reverse: Ia is the most hazardous and III the least."),
  ],
  decode=[
    ("Epidemiology of poisoning in India: most accurate statement [DocT]", "Organophosphates are a common cause — not urban predominance, not Western-level mortality."),
    ("“Oral LD50 <5 mg/kg” — WHO class? [pattern]", "Class Ia, extremely hazardous."),
  ],
  punch="The WHO class is only the compound’s intrinsic toxicity read backwards from its LD50 — the reason organophosphates kill so many in rural India is availability and dose, not subtlety.",
)

L['PEST-02'] = dict(
  sub="Toxicology → Pesticides → Classifying the compounds",
  intro="All organophosphates do the same thing to acetylcholinesterase, so the class matters for two other reasons: the alkyl side groups decide how quickly the enzyme–poison bond becomes permanent, and fat solubility decides how long the illness lasts. Carbamates give the same clinical picture with different chemistry. Nerve agents are the military members of the organophosphate family — and are treated the same way.",
  parts=[
    ('a', "**Dimethyl: dichlorvos, fenthion, malathion, methamidophos.** The bound enzyme loses a methyl group fast, so ageing takes only about 3 hours (PEST-03) and the window for an oxime is short."),
    ('b', "**Diethyl: chlorpyrifos, diazinon, parathion, quinalphos.** Ethyl groups are lost slowly, so ageing takes about 33 hours and oximes still work the next day. Parathion poisoning is the classic organophosphate crisis treated with atropine plus pralidoxime. Several (chlorpyrifos, parathion) are thions needing hepatic activation, so onset can be delayed and prolonged."),
    ('c', "**Atypical: profenofos.** Its side chains fit neither pattern and the enzyme it inhibits is poorly reactivatable, so oximes do little for it."),
    ('d', "**Nerve agents: sarin, tabun, soman, VX.** Chemical-warfare organophosphates, far more potent and absorbed through skin and lungs. The toxidrome is the same muscarinic flood — miosis, bradycardia, tears, salivation, diarrhoea, urination — and so are the antidotes: atropine plus pralidoxime, given early because soman ages within minutes."),
    ('e', "**Carbamates: carbaryl, aldicarb, methomyl, propoxur.** They carbamylate the same site but the bond hydrolyses spontaneously, so there is no ageing and the illness is shorter (PEST-03)."),
  ],
  table=dict(title="What the subclass changes", head=["Subclass", "Ageing", "Oxime value"], rows=[["Dimethyl", "**~3 h**", "narrow window"], ["Diethyl", "**~33 h**", "best"], ["Profenofos (atypical)", "fastest", "least"], ["Nerve agents", "minutes (soman)", "give at once"], ["Carbamate", "**none**", "not recommended (PEST-11)"]]),
  mimic=[
    ("Lipophilic vs water-soluble organophosphate", "Fenthion and malathion are stored in fat and leach back out, so cholinergic features relapse; water-soluble agents give one defined illness."),
    ("Nerve agent vs anticholinergic plant vs cyanide", "Sarin: wet, miotic, bradycardic — atropine + pralidoxime. Atropa belladonna: dry, dilated, hot — physostigmine. Cyanide: hydroxocobalamin."),
  ],
  traps=[
    ("“Ethanol for isopropyl alcohol, glucagon for cocaine, D5 for methaemoglobinaemia”", "None is a recognised antidote: isopropanol makes acetone, so ADH blockade is pointless; glucagon is for β-blocker and calcium-channel-blocker poisoning; methaemoglobinaemia needs methylene blue. Pralidoxime in sarin is the recognised one — only 43% chose it in one sitting."),
    ("“Sarin needs atropine alone” or “a different antidote”", "Severe nerve-agent poisoning gets atropine and pralidoxime, as for any organophosphate."),
    ("“Aldicarb is an organophosphate”", "Aldicarb is a carbamate (and WHO class Ia); parathion is the diethyl organophosphate."),
  ],
  decode=[
    ("Recognised treatment option in poisoning (vs ethanol–isopropanol, glucagon–cocaine, D5–methaemoglobin) [DocT]", "Pralidoxime in sarin poisoning."),
    ("Subway release of sarin, most severe patients: best management [DocT GT]", "Atropine and pralidoxime."),
    ("Villagers: diarrhoea, urination, tears, bradycardia, miosis, salivation [DocT GT]", "Sarin; atropine and pralidoxime."),
    ("Cholinergic crisis treated with atropine + pralidoxime: agent [Marrow]", "Parathion (diethyl OP), not aldicarb (carbamate)."),
  ],
  punch="The subclass tells you nothing new about the toxidrome and everything about the clock: dimethyl ages in hours, diethyl in a day and a half, soman in minutes, carbamates never — and every organophosphate, nerve agents included, gets atropine plus an oxime.",
)

L['PEST-03'] = dict(
  sub="Toxicology → Pesticides → Mechanism and ageing",
  intro="Acetylcholinesterase splits acetylcholine the instant it is released. An organophosphate leaves a phosphate group stuck on its catalytic (esteratic) site, so transmitter accumulates at muscarinic, nicotinic and central synapses. At first that phosphate can still be pulled off; after a chemical rearrangement — ageing — it cannot.",
  parts=[
    ('a', "**Phosphorylates the esteratic site of acetylcholinesterase, so acetylcholine accumulates at muscarinic, nicotinic and CNS synapses.** This is conventionally called irreversible inhibition: the phosphorylated enzyme does not recover on its own in any useful time, unlike a carbamylated one. Strictly, it is slowly reversible by an oxime until it ages, and only then truly permanent."),
    ('b', "**Loss of an alkyl group from the bound enzyme: the bond becomes irreversible and oximes no longer work.** The aged enzyme carries a stable, negatively charged phosphate an oxime cannot attack; recovery then depends on new enzyme, over weeks."),
    ('c', "**Dimethyl about 3 hours; diethyl about 33 hours.** Half-lives of ageing. The smaller methyl group leaves far more readily, hence the tenfold difference."),
    ('d', "**A dimethyl patient arriving at 3 hours already has half the enzyme aged, so oximes work far better in diethyl poisoning; profenofos ages faster still.** An oxime is still worth giving a day later after chlorpyrifos, and it is started while the compound is unknown."),
    ('e', "**Carbamylation is reversible, with no ageing; shorter illness; little CNS penetration.** The carbamyl–enzyme bond hydrolyses within hours, so the enzyme recovers without an antidote; carbamates cross the blood–brain barrier poorly."),
  ],
  mimic=[
    ("Organophosphate vs carbamate at the bedside", "Identical cholinergic syndrome; carbamate illness resolves in a day or two, rarely shows the intermediate syndrome, and needs atropine but not an oxime."),
  ],
  traps=[
    ("“Organophosphates cause reversible inhibition of AChE” / “block ACh receptors” / “release ACh”", "The keyed answer is irreversible inhibition of acetylcholinesterase; reversible inhibition is the carbamate. Only 58% got it right."),
    ("“Ageing is faster with diethyl compounds”", "The opposite: dimethyl ~3 h, diethyl ~33 h."),
    ("“Carbamates need no treatment”", "They need atropine and often ventilation; what they do not need is an oxime."),
  ],
  decode=[
    ("Primary biochemical effect of organophosphates [DocT]", "Irreversible inhibition of acetylcholinesterase."),
    ("“Oximes would be least useful in poisoning with…” [pattern]", "A dimethyl compound or profenofos."),
  ],
  punch="Organophosphate inhibition is called irreversible because it becomes so once the enzyme ages — fast in dimethyl and profenofos, slow in diethyl — while carbamate inhibition is reversible and never ages.",
)

L['PEST-04'] = dict(
  sub="Toxicology → Pesticides → Receptor to symptom",
  intro="Everything in cholinergic poisoning follows from where acetylcholine receptors sit. Muscarinic receptors are on glands, smooth muscle and the heart’s pacemaker; nicotinic receptors are at the neuromuscular junction and in autonomic ganglia; both are in the brain. So the patient shows glandular flooding and bradycardia, weakness and sometimes tachycardia, and coma and loss of respiratory drive.",
  parts=[
    ('a', "**Muscarinic — salivation, lacrimation, urination, diarrhoea, GI cramps, emesis; bradycardia, bronchorrhoea, bronchospasm; miosis.** Every exocrine gland is turned on — including sweat glands, so the skin is wet — and smooth muscle contracts. The patient is wet, miotic and bradycardic, often frothing at the mouth; a hot, dry patient is anticholinergic (or over-atropinised), not cholinergic. Bronchorrhoea flooding the alveoli, raised capillary permeability and aspiration give bilateral infiltrates with a normal heart and CVP — non-cardiogenic pulmonary oedema. Atropine blocks these effects (PEST-10)."),
    ('b', "**Nicotinic — fasciculation, weakness, paralysis; tachycardia, hypertension, mydriasis from ganglionic stimulation.** Persistent acetylcholine first makes muscle twitch, then depolarises the end-plate into a block, so fasciculation gives way to flaccid weakness, including the diaphragm. Atropine does nothing here; fasciculation or weakness persisting after atropine is the sign that an oxime is needed (PEST-11)."),
    ('c', "**CNS — confusion, coma, convulsions; central respiratory depression.** Lipophilic organophosphates cross into the brain and finally depress the brainstem respiratory centre. The commonest cause of death is respiratory failure — bronchorrhoea and bronchospasm, nicotinic diaphragm failure and central apnoea together — not cardiotoxicity."),
  ],
  table=dict(title="Three receptor groups, three sets of signs", head=["Receptor", "Signs", "Antidote"], rows=[["Muscarinic", "secretions, bronchospasm, bradycardia, miosis, wet skin", "**atropine**"], ["Nicotinic", "fasciculation → weakness; tachycardia, hypertension", "**oxime**"], ["CNS", "coma, convulsions, apnoea", "atropine (central) + ventilation"]]),
  mimic=[
    ("Organophosphate vs other garden poisons", "Small pupils, bradycardia and frothing are cholinergic; paraquat gives caustic mouth and later lung fibrosis, glyphosate GI injury and shock, creosote phenol burns — none is miotic and wet."),
    ("Bilateral infiltrates: non-cardiogenic oedema vs ARDS", "Both have a normal CVP. DocT keys ‘non-cardiogenic pulmonary oedema’ as the umbrella term; if the stem gives Berlin criteria it is ARDS and gets lung-protective ventilation."),
  ],
  traps=[
    ("“Hyperthermia is expected in cholinergic crisis”", "It is the least expected feature: the patient sweats and is wet. Hyperthermia points to an anticholinergic state or atropine toxicity. Only 58% chose it."),
    ("“Bilateral infiltrates with normal heart size and CVP — ARDS” (or aspiration)", "DocT keys non-cardiogenic pulmonary oedema (50% right); ARDS is defensible by Berlin, aspiration is one contributor."),
    ("“Persisting bronchorrhoea or miosis after atropine means pralidoxime is needed”", "Those are muscarinic — give more atropine. Fasciculation is the nicotinic sign that calls for the oxime."),
    ("“Tachycardia excludes organophosphate poisoning”", "Ganglionic stimulation, hypoxia and bronchospasm all raise the rate."),
  ],
  decode=[
    ("Agricultural worker, wet, miotic, bradycardic: least expected feature [DocT]", "Hyperthermia."),
    ("Intubated OP patient, bilateral infiltrates, normal heart and CVP [DocT]", "Non-cardiogenic pulmonary oedema (ARDS defensible)."),
    ("After atropine, which finding indicates pralidoxime? [NEET 2025]", "Muscle fasciculations."),
    ("75-year-old found in garden: unconscious, small pupils, HR 50, frothing [DocT]", "Organophosphorus poisoning."),
  ],
  punch="Read the patient receptor by receptor: glands and airway are muscarinic and answer to atropine, muscle and ganglia are nicotinic and answer only to an oxime, and the brain adds coma and apnoea — which is why these patients die of their airway, not their heart.",
  extra=[dict(q="Commonest cause of death and its treatment? [Marrow]", a="**Respiratory failure** — bronchorrhoea plus respiratory muscle fatigue — treated with **atropine + pralidoxime**, airway and ventilation.")],
)

L['PEST-05'] = dict(
  sub="Toxicology → Pesticides → The three paralyses",
  intro="Weakness in organophosphate poisoning comes in three waves with different mechanisms: day one, day three, and weeks later. Only the first responds to atropine, the second needs a ventilator and nothing else, and the third is a neuropathy that no antidote touches. The clock after exposure is the main discriminator.",
  parts=[
    ('a', "**Type I — acute cholinergic crisis: minutes to hours, generalised weakness with fasciculation, responds to atropine.** The cholinergic flood itself (PEST-04); atropine reverses the muscarinic half, which saves the airway."),
    ('b', "**Type II — intermediate syndrome: 24–96 hours, neck flexors, proximal limb, cranial nerve and respiratory muscles, no response to atropine.** It appears after the crisis has settled, in a conscious, afebrile patient who looked to be recovering — a post-synaptic nicotinic problem (PEST-06)."),
    ('c', "**Type III — delayed neuropathy (OPIDN): 1–3 weeks, distal muscles, legs first, ascending, no response to atropine.** A dying-back axonopathy from inhibition of neuropathy target esterase, not acetylcholinesterase (PEST-07) — so neither persistent AChE inhibition nor antibodies explain it."),
  ],
  table=dict(title="Telling the three apart", head=["", "Type I", "Type II", "Type III"], rows=[["Onset", "minutes–hours", "**24–96 h**", "**1–3 weeks**"], ["Pattern", "generalised, fasciculation", "**neck flexors, proximal, cranial, respiratory**", "**distal, legs first, ascending**"], ["Enzyme", "AChE", "AChE (nicotinic receptor)", "**neuropathy target esterase**"], ["Atropine", "responds", "no", "no"], ["Treatment", "atropine, oxime, airway", "ventilation", "physiotherapy, time"]]),
  mimic=[
    ("Intermediate syndrome vs myasthenic crisis vs Guillain–Barré", "All give respiratory weakness; the intermediate syndrome follows a documented cholinergic crisis by 1–4 days, with neck-flexor weakness, intact sensation and no antibodies."),
    ("OPIDN vs intermediate syndrome", "Distal and sensory at 1–3 weeks versus proximal, neck-flexor and respiratory at 24–96 hours."),
  ],
  traps=[
    ("“Weakness and areflexia 7 days after OP: persistent AChE inhibition or myositis”", "DocT keys OPIDP (neuropathy target esterase) for this delayed complication. Note the stem’s ‘proximal’ weakness fits poorly — the textbook OPIDN is distal and ascending."),
    ("“Intermediate syndrome affects distal muscles first”", "It is neck flexors and proximal muscles; distal weakness is the delayed neuropathy."),
    ("“Recovery from the crisis means the patient can be extubated and discharged”", "The intermediate syndrome begins exactly then — keep ventilation available for 4 days."),
  ],
  decode=[
    ("48 h after atropine + pralidoxime: neck flexor weakness, respiratory distress, afebrile, conscious [DocT]", "Intermediate syndrome — not myasthenic crisis, GBS or neuropathy."),
    ("72 h later: neck flexor weakness, shallow breathing [DocT GT]", "Intermediate syndrome."),
    ("7 days later: weakness, areflexia, prolonged ventilation — mechanism [DocT]", "OPIDP (neuropathy target esterase)."),
  ],
  punch="Three waves, three mechanisms: the cholinergic flood answers to atropine, the intermediate syndrome answers only to a ventilator, and the delayed neuropathy belongs to a different enzyme altogether.",
)

L['PEST-06'] = dict(
  sub="Toxicology → Pesticides → Intermediate syndrome",
  intro="In a substantial minority the cholinergic crisis settles, atropine is weaned, and then over a few hours the patient cannot hold the head up, cannot cough and stops breathing adequately. Nothing prevents it and nothing shortens it; what matters is that a ventilator is ready.",
  parts=[
    ('a', "**10–40% of patients; 24–96 hours after exposure, after the cholinergic crisis has resolved.** The timing is the point: it begins when the muscarinic features have gone and the patient appears to be improving."),
    ('b', "**Neck flexion weakness (cannot lift the head off the pillow), proximal limb weakness, cranial nerve palsies, reduced reflexes, respiratory failure.** Neck flexors, girdle muscles, facial and bulbar muscles and the diaphragm fail; distal strength and sensation are preserved (PEST-07), and there are no recurrent muscarinic signs."),
    ('c', "**Highly fat-soluble agents; possibly inadequate oxime dosing.** Lipophilic compounds such as fenthion keep releasing poison from fat (PEST-02); whether too little oxime contributes is debated."),
    ('d', "**Persistent nicotinic over-stimulation with receptor down-regulation and muscle necrosis.** Continuous acetylcholine at the end-plate desensitises and down-regulates post-synaptic receptors and damages muscle fibres. Because the problem is post-synaptic and structural, neither atropine nor an oxime alters it."),
    ('e', "**Supportive ventilation; no treatment prevents it.** Recovery takes days to weeks. Watch head lift, single-breath count and vital capacity, and intubate before the patient tires."),
  ],
  mimic=[
    ("Intermediate syndrome vs recurrent cholinergic crisis", "Returning secretions, wheeze and miosis is cholinergic and needs atropine; pure weakness with a dry chest is the intermediate syndrome."),
    ("Intermediate syndrome vs myasthenic crisis", "Same proximal, bulbar and respiratory pattern; the poisoning history and preceding cholinergic phase decide it."),
  ],
  traps=[
    ("“It is a rebound cholinergic crisis, so give more atropine”", "Without muscarinic signs it is nicotinic and post-synaptic; atropine does not treat it."),
    ("“Atropine toxicity explains the weakness” / “it was a carbamate”", "Atropine excess gives a hot, dry, delirious patient, not paralysis; carbamates rarely cause the intermediate syndrome."),
    ("“The patient is well at 24 hours, so discharge”", "This is the window in which the syndrome begins; observe for at least 4 days."),
  ],
  decode=[
    ("Improved with atropine, then progressive weakness and respiratory failure [DocT / DocT GT]", "Intermediate syndrome — not rebound crisis, atropine toxicity or carbamate."),
    ("Day 3: cannot lift head, proximal and facial weakness, no muscarinic signs [DocT GT]", "Intermediate syndrome."),
    ("48–72 h, neck flexor weakness and shallow breathing [DocT / DocT GT]", "Intermediate syndrome."),
  ],
  punch="The intermediate syndrome is the trap of the second and third day: the cholinergic storm is over, the antidote is being weaned, and the only treatment for the weakness that follows is a ventilator you decided on early.",
)

L['PEST-07'] = dict(
  sub="Toxicology → Pesticides → Delayed neuropathy (OPIDN)",
  intro="Weeks after the poisoning is over, some patients return with numb feet and a slapping gait. This has nothing to do with acetylcholinesterase: certain organophosphates inhibit another esterase in the axon, and the long nerves degenerate from their tips backwards. Because the mechanism is separate, so are the timing, the pattern and the irrelevance of the acute severity.",
  parts=[
    ('a', "**Inhibition of neuropathy target esterase, not acetylcholinesterase.** The compound phosphorylates this axonal enzyme, which then ages; the modified enzyme triggers a dying-back degeneration of the longest axons. So the mechanism of a delayed weakness is not persistent AChE inhibition, and cholinergic antidotes are irrelevant."),
    ('b', "**Stocking-and-glove paraesthesia, then distal flaccid weakness of the legs ascending to the arms; absent ankle jerks.** The longest fibres fail first, sensory before motor, with wasting and areflexia; some patients are left with spasticity."),
    ('c', "**Chlorpyrifos is the typical agent.** It is the compound in common agricultural use most often reported; triorthocresyl phosphate is the historical one."),
    ('d', "**Independent of the severity of the acute poisoning: it can follow a mild acute illness.** The two enzymes have different sensitivities, so a compound can inhibit neuropathy target esterase while causing only modest cholinergic symptoms."),
    ('e', "**Carbamates only rarely cause it.** They inhibit neuropathy target esterase weakly and the bond does not age."),
  ],
  mimic=[
    ("OPIDN vs Guillain–Barré syndrome", "Both ascend; OPIDN starts 1–3 weeks after a known exposure and progresses over days to weeks."),
  ],
  traps=[
    ("“Delayed weakness is persistent AChE inhibition at the junction” or “antibody-mediated”", "It is OPIDP — neuropathy target esterase. 71% got it right."),
    ("“Delayed neuropathy follows only severe poisoning”", "It is independent of acute severity."),
    ("“Pralidoxime given early prevents it”", "Oximes act on acetylcholinesterase, not neuropathy target esterase."),
  ],
  decode=[
    ("Weakness, areflexia and ventilator dependence ~7 days after OP: mechanism [DocT]", "Organophosphate-induced delayed polyneuropathy."),
    ("Three weeks after chlorpyrifos: numb feet, foot drop, absent ankle jerks [pattern]", "OPIDN."),
  ],
  punch="OPIDN is organophosphate poisoning in a different enzyme: a dying-back axonopathy of the longest nerves that arrives weeks later, ignores how ill the patient was, and has no antidote.",
)

L['PEST-08'] = dict(
  sub="Toxicology → Pesticides → Delayed manifestations by time",
  intro="Organophosphate poisoning is a sequence spread over three weeks, and most of it appears after the patient has been declared out of danger. The order follows the mechanisms: continuing absorption first, then the neuromuscular junction, then the brain, and last the peripheral axon.",
  parts=[
    ('a', "**Delayed-onset cholinergic phase at 40–48 hours.** With lipophilic and thion compounds poison keeps arriving at the synapse, so secretions and miosis return; it responds to atropine."),
    ('b', "**Intermediate syndrome at 24–96 hours.** Nicotinic failure of neck flexors, proximal, bulbar and respiratory muscles, needing ventilation (PEST-06)."),
    ('c', "**Late-onset intermediate syndrome at about 114 hours.** The same syndrome beyond four days, typically with fat-soluble agents."),
    ('d', "**Delayed encephalopathy or coma at 4–6 days.** Confusion or coma after the acute phase, with no new muscarinic signs."),
    ('e', "**Cerebellar ataxia at about 8 days.** Usually self-limiting."),
    ('f', "**Extrapyramidal syndrome at 5–15 days.** Dystonia, rigidity and tremor; generally reversible."),
    ('g', "**Delayed neuropathy at 1–3 weeks.** Distal, sensory then motor, ascending (PEST-07)."),
  ],
  table=dict(title="The timeline", head=["Time", "Manifestation"], rows=[["24–96 h", "**intermediate syndrome**"], ["40–48 h", "delayed cholinergic phase"], ["~114 h", "late-onset intermediate syndrome"], ["4–6 days", "delayed encephalopathy or coma"], ["8 days", "cerebellar ataxia"], ["5–15 days", "extrapyramidal syndrome"], ["1–3 weeks", "**delayed neuropathy**"]]),
  mimic=[
    ("Delayed cholinergic phase vs intermediate syndrome", "Returning secretions and miosis need atropine; pure weakness with a dry chest does not."),
  ],
  traps=[
    ("“Everything happens in the first 24 hours”", "Most syndromes begin after 24 hours — observe at least four days, follow up for weeks."),
  ],
  decode=[
    ("Reappearance of secretions at 44 hours after a fat-soluble OP [pattern]", "Delayed-onset cholinergic phase — atropine again."),
    ("Dystonia 10 days later [pattern]", "Extrapyramidal syndrome."),
  ],
  punch="The poisoning unfolds for three weeks, and the order is mechanistic: continuing absorption, then the junction, then the brain, then the axon — so observation is measured in days and follow-up in weeks.",
)

L['PEST-09'] = dict(
  sub="Toxicology → Pesticides → Diagnosis: cholinesterases and the atropine challenge",
  intro="The diagnosis is clinical, but two blood enzymes answer different questions. One is the synapse’s own enzyme and tracks how poisoned the patient is; the other is a liver protein that merely proves exposure. Where neither assay is available, a small dose of atropine can serve as a test.",
  parts=[
    ('a', "**RBC cholinesterase is true (acetyl) cholinesterase: it mirrors the synaptic enzyme and correlates with severity.** Mild 20–50% of normal, moderate 10–20%, severe under 10% — with coma, flaccid paralysis, pulmonary oedema and pinpoint pupils. Red cells cannot resynthesise it, so recovery is about 1% a day."),
    ('b', "**Plasma cholinesterase is pseudo (butyryl) cholinesterase, made in the liver: a simple marker of exposure with no correlation with severity.** It is a sensitive screen, but its baseline varies widely and falls in liver disease, pregnancy and malnutrition; its practical use is a warning that suxamethonium will be prolonged (PEST-12)."),
    ('c', "**Atropine challenge: a rise in heart rate of more than 20–25/min with flushing after a small dose means no significant cholinergic poisoning.** A poisoned patient’s receptors are swamped with acetylcholine, so a small competitive dose changes little."),
  ],
  table=dict(title="The two enzymes", head=["", "RBC (true) AChE", "Plasma (pseudo) BChE"], rows=[["Same enzyme as synapse", "**yes**", "no"], ["Tracks severity", "**yes** (severe <10%)", "no"], ["Recovery", "~1%/day, weeks", "days"], ["Use", "**severity, prognosis**", "exposure; suxamethonium warning"]]),
  mimic=[],
  traps=[
    ("“Plasma cholinesterase correlates with severity”", "It does not — the RBC enzyme does."),
    ("“Wait for the assay before giving atropine”", "Treatment is clinical and immediate; the assay confirms."),
  ],
  decode=[
    ("RBC AChE 8% of normal with coma and flaccid paralysis: severity? [pattern]", "Severe (<10%)."),
    ("Heart rate rises 30/min after 1 mg atropine [pattern]", "No significant cholinergic poisoning."),
  ],
  punch="The red cell enzyme is the synapse in a tube and grades severity; plasma cholinesterase only says the patient met the poison — and a patient who shrugs off a test dose of atropine is the one who needs it.",
)

L['PEST-10'] = dict(
  sub="Toxicology → Pesticides → Atropine",
  intro="Atropine is a competitive muscarinic antagonist, so it must outnumber the acetylcholine piling up in the synapse — the dose is whatever it takes. What it is competing for is the airway: secretions and bronchospasm kill in the first hours. So the dose is escalated fast and judged by the chest, not by the pupils or the pulse.",
  parts=[
    ('a', "**2–5 mg IV, doubling every 5 minutes until atropinised.** Fixed small doses lose the race against a flooded synapse, so the dose is doubled — 2, 4, 8, 16 mg — until the end-points are met; giving too little is the commoner error. Atropine is the life-saving first drug; with an oxime alongside in moderate to severe poisoning, it is the initial management (TOXBASE: immediate bolus then infusion)."),
    ('b', "**End-points: a clear chest with no wheeze or secretions, heart rate above 80, systolic pressure above 80, dry axillae, and pupils no longer pinpoint.** Drying of respiratory secretions is the one that matters, because bronchorrhoea is the lethal effect. The heart-rate target is only above 80 — tachycardia over 100 is not the goal; mydriasis and hypertension are not end-points, and pupils are the least reliable sign."),
    ('c', "**Maintenance by infusion of 10–20% of the total loading dose per hour.** Atropine lasts a few hours while the organophosphate persists for days, so stopping after loading lets the patient relapse."),
    ('d', "**If atropine toxicity occurs, stop, then restart at 70–80% of the previous rate.** Over-atropinisation gives agitation, delirium, hyperthermia, ileus, urinary retention and tachyarrhythmia."),
    ('e', "**It does not treat the nicotinic effects: weakness and paralysis.** There are no muscarinic receptors at the neuromuscular junction; those need an oxime and often a ventilator (PEST-11, PEST-05)."),
  ],
  table=dict(title="What to titrate against", head=["End-point", "Target"], rows=[["Chest", "**clear — no wheeze, no secretions**"], ["Axillae", "**dry**"], ["Heart rate", ">80/min (not >100)"], ["Systolic BP", ">80 mmHg"], ["Pupils", "no longer pinpoint (least reliable)"]]),
  mimic=[
    ("Atropine toxicity vs continuing poisoning", "Both give a confused, tachycardic patient; atropine excess has a dry chest, absent bowel sounds and a full bladder, continuing poisoning a wet, wheezy chest."),
  ],
  traps=[
    ("“Atropinisation means heart rate >100 or dilated pupils”", "The end-point is a dry chest and axillae with clear lungs; HR >80 is enough. Only 63% chose this."),
    ("“Gastric lavage in all cases, haemodialysis or steroids”", "None is initial management; immediate atropine bolus then infusion is."),
    ("“Tachycardia is a reason to withhold atropine”", "A wet chest still needs atropine."),
  ],
  decode=[
    ("What guides adequate atropinisation during titration? [DocT]", "Dry axilla and chest, clear lungs."),
    ("Endpoint of continuous IV atropine [DocT]", "Drying of respiratory secretions."),
    ("TOXBASE initial management of moderate OP poisoning [DocT]", "Immediate atropine bolus followed by infusion."),
    ("Farmer with SLUDGE and miosis: initial step [DocT]", "Atropine and pralidoxime together."),
  ],
  punch="Atropine is titrated against the airway and nothing else: double the dose until the chest is clear and the axillae dry, keep an infusion going because the poison outlasts the drug, and accept that weakness is not its business.",
)

L['PEST-11'] = dict(
  sub="Toxicology → Pesticides → Oximes",
  intro="Atropine blocks the receptor; an oxime takes the phosphate off the enzyme and gives the synapse its acetylcholinesterase back. That is the only way the nicotinic effects — fasciculation, weakness, respiratory muscle failure — can be treated. It works only while the bond is still rescuable, so it is started at once and given as an infusion.",
  parts=[
    ('a', "**Pralidoxime, obidoxime, trimedoxime.** All quaternary oximes; pralidoxime is the one available in India."),
    ('b', "**They bind the anionic site and pull the phosphate off the esteratic site, reactivating cholinesterase before ageing; they also slow further ageing.** The reactivated enzyme clears acetylcholine again. Pralidoxime does not block receptors, enhance renal excretion of the poison or stop it binding red cells — it reactivates the enzyme."),
    ('c', "**Pralidoxime 1–2 g over 30 minutes, repeated in 1 hour if weakness persists, or given as an infusion.** WHO dosing: 30 mg/kg (about 2 g) over 30 minutes, then 8 mg/kg/h (about 500 mg/h) until atropine is no longer needed. An infusion holds the plasma level (above about 4 mg/L) needed to outpace re-inhibition."),
    ('d', "**Not recommended in carbamate poisoning, but do not withhold it when the agent is unknown.** Carbamylated enzyme recovers on its own; an unidentified bottle may be an organophosphate."),
    ('e', "**Useless once the enzyme has aged; no CNS effect; rapid injection causes laryngospasm, hypertension and vomiting.** Being permanently charged, pralidoxime scarcely enters the brain; it is infused over 30 minutes."),
  ],
  mimic=[
    ("Atropine vs pralidoxime", "Atropine blocks muscarinic receptors and treats secretions; pralidoxime restores the enzyme and treats nicotinic weakness. Organophosphates, sarin included, get both."),
  ],
  traps=[
    ("“After atropine, persisting bronchorrhoea, miosis or bradycardia indicates pralidoxime”", "Those are muscarinic — more atropine. Fasciculation (nicotinic) is the indication [NEET 2025]."),
    ("“Pralidoxime instead of atropine if secretions are heavy”", "It has no muscarinic action."),
    ("“Trial evidence proves oximes work”", "It does not: a placebo-controlled trial of the WHO regimen showed no clinical benefit and the Cochrane review finds the evidence insufficient. They are still given early, with atropine."),
  ],
  decode=[
    ("Action of pralidoxime [DocT ×2]", "Reactivates acetylcholinesterase by removing the organophosphate."),
    ("Pralidoxime dosing in severe OP poisoning [DocT]", "2 g IV over 30 min, then 500 mg/h infusion."),
    ("After atropine, finding indicating pralidoxime [NEET 2025]", "Muscle fasciculations."),
    ("Cholinergic crisis after suicide attempt / severe sarin: effective combination [Marrow / DocT GT]", "Atropine and pralidoxime."),
  ],
  punch="An oxime is the only drug that gives the enzyme back, so it is the only treatment for nicotinic weakness — started early, infused rather than pushed, and worthless once the bond has aged.",
)

L['PEST-12'] = dict(
  sub="Toxicology → Pesticides → Other measures",
  intro="Beyond atropine and an oxime, management is airway, decontamination and avoiding harm. Two details are specific: the relaxant used for intubation is cleared by the enzyme the poison has inhibited, and the poison is still on the skin and in the vomit — absorbed by the patient and by the staff.",
  parts=[
    ('a', "**Avoid succinylcholine: it is metabolised by plasma cholinesterase, so paralysis is prolonged.** With the plasma enzyme inhibited a standard dose can paralyse for hours. Use rocuronium."),
    ('b', "**Remove clothes and wash the skin; activated charcoal 1 g/kg within 1 hour; no forced emesis.** Organophosphates are absorbed through skin and evaporate from soaked clothing and vomit, so staff need full protective gear against both dermal and inhaled exposure — gloves, gown, eye protection and a ventilated space. Induced emesis risks aspiration in a patient who may convulse."),
    ('c', "**Glycopyrrolate does not cross the blood–brain barrier: added to atropine it caused far less confusion and hallucination (30% versus 90%) and less tachyarrhythmia, with the same outcome. Dose 7.5 mg in 200 mL, infused until the mucous membranes are dry.** It dries secretions without central delirium, but cannot replace atropine for central effects."),
    ('d', "**Fresh frozen plasma is harmful; haemodialysis and bicarbonate have no role; magnesium has no scientific data, and clonidine and vitamin E rest on animal studies only.** FFP raised plasma cholinesterase in the one randomised pilot but did not improve deaths or ventilator days — no benefit rather than proven harm. Organophosphates are lipophilic with a large volume of distribution, so dialysis removes nothing useful. Magnesium is better described as unproven: small trials hint at benefit but are insufficient to recommend it."),
  ],
  mimic=[
    ("Glycopyrrolate vs atropine", "Glycopyrrolate dries without delirium but has no central action; atropine remains the drug titrated to the chest (PEST-10)."),
  ],
  traps=[
    ("“Gloves are enough” / “decontamination is only for the patient”", "Vomit and clothing release the agent; full dermal and inhalational protection is needed."),
    ("“Give fresh frozen plasma to replace cholinesterase”", "No improvement in survival; not a treatment."),
    ("“Dialyse the organophosphate”", "Large volume of distribution — dialysis removes nothing useful."),
  ],
  decode=[
    ("Cholinergic patient vomiting, chemical smell: staff precaution [Marrow]", "Full protective gear — dermal and inhalational."),
    ("Intubating drug to avoid [pattern]", "Succinylcholine — prolonged block."),
  ],
  punch="The extras are mostly about not adding harm: no succinylcholine, no forced emesis, no dialysis, never FFP — while the things that do work are washing the patient, protecting the team and keeping the chest dry.",
)

L['PEST-13'] = dict(
  sub="Toxicology → Pesticides → True or false",
  intro="These eight statements are the deck’s key discriminations, and each turns on a mechanism met earlier: which alkyl group ages faster, which enzyme is the synapse’s own, which receptor each antidote reaches, and which muscles fail when.",
  parts=[
    ('a', "**False — dimethyl compounds age in about 3 hours, diethyl in about 33.** The smaller methyl group is shed more readily (PEST-03)."),
    ('b', "**False — the RBC (true) enzyme correlates with severity.** Under 10% of normal is severe, 10–20% moderate, 20–50% mild; plasma butyrylcholinesterase shows exposure only (PEST-09)."),
    ('c', "**False — the intermediate syndrome affects neck flexors and proximal muscles first.** Distal, ascending weakness at 1–3 weeks is the delayed neuropathy (PEST-05, PEST-07)."),
    ('d', "**False — delayed neuropathy is independent of acute severity.** It follows inhibition of neuropathy target esterase (PEST-07)."),
    ('e', "**False — fasciculation is nicotinic, and atropine is purely antimuscarinic.** Only an oxime addresses it (PEST-10, PEST-11)."),
    ('f', "**False — oximes are not recommended in carbamate poisoning.** Carbamylated enzyme hydrolyses spontaneously; they are still given when the agent is unknown (PEST-11)."),
    ('g', "**True — atropinisation is judged by a dry chest.** Clear lungs and dry axillae are the end-point (PEST-10)."),
    ('h', "**False — tachycardia does not exclude organophosphate poisoning.** Ganglionic stimulation, hypoxia and bronchospasm raise the rate (PEST-04)."),
  ],
  mimic=[
    ("Severe acute poisoning vs intermediate syndrome", "Coma, flaccid paralysis, pulmonary oedema and pinpoint pupils on arrival is severe cholinergic poisoning; the intermediate syndrome comes later, in a conscious patient after the crisis."),
  ],
  traps=[
    ("“Flaccid paralysis means intermediate syndrome”", "On presentation, with coma and RBC AChE <10%, it is severe cholinergic poisoning."),
    ("“Atropine covers the whole syndrome”", "It covers only the muscarinic part."),
  ],
  decode=[
    ("Flaccid paralysis, coma, pulmonary oedema, pinpoint pupils, RBC AChE 8%: classify [DocT GT]", "Severe cholinergic poisoning."),
    ("Statements about ageing or antidotes [pattern]", "Which alkyl group (dimethyl is fast); which receptor the drug reaches."),
  ],
  punch="Every statement here comes back to three questions: which alkyl group is on the phosphorus, which enzyme is being measured, and which receptor the antidote can actually reach.",
)

FLAGS = {
  'PEST-01': "Card a gives up to 300,000 deaths a year from organophosphates specifically; most sources quote ~250,000–370,000 deaths from pesticide self-poisoning as a whole, with organophosphates the largest share. Card figure kept. The WHO classification quoted is the older oral-LD50 table (the 2019 revision also uses dermal LD50 and reclassifies some compounds) — fine for exam use.",
  'PEST-02': "Card lists malathion as dimethyl (correct) and the watch note calls it lipophilic (correct), but malathion is of low mammalian toxicity because of rapid carboxylesterase detoxification; a stem pairing malathion with rapid death is usually testing formulation/solvent or massive dose. No change needed.",
  'PEST-03': "DocT QBank keys ‘irreversible inhibition of AChE’. Strictly, phosphorylation is slowly reversible (by oximes) until ageing; ‘irreversible’ is the conventional answer. Explanation says both.",
  'PEST-05': "DocT QBank ‘7 days later, progressive proximal weakness, areflexia, prolonged ventilation’ keys OPIDP. The card (and textbooks) describe OPIDN as distal and ascending at 1–3 weeks; a proximal, ventilator-dependent picture at day 7 overlaps the late-onset intermediate syndrome. Key kept; mismatch noted in the trap.",
  'PEST-09': "Card c gives the atropine challenge as a rise in heart rate >20–25/min with flushing after a small dose. This is traditional teaching from resource-limited settings, not a validated test, and it is absent from Goldfrank's/UpToDate; it should not delay empirical atropine. Card statement kept.",
  'PEST-10': "Card c itself notes the maintenance infusion (10–20% of the loading dose per hour) is standard teaching not in Naven's notes — confirmed correct and widely used, so it is explained as standard. Card b's heart rate >80 and systolic >80 are the published atropinisation end-points; some protocols drop the pupil criterion entirely because it is unreliable — the explanation says so.",
  'PEST-11': "Card c gives pralidoxime 1–2 g over 30 min with repeat at 1 hour. The WHO regimen is 30 mg/kg (~2 g) over 30 min then 8 mg/kg/h (~500 mg/h) until atropine is no longer needed; both are given, card first. The card implies oximes work if given in time: the Cochrane review (Buckley, Eddleston et al.) concludes the evidence is insufficient to show benefit or harm, and the placebo-controlled trial of the WHO regimen in Sri Lanka found no clinical benefit with a trend to harm, while a small Indian trial of 1 g/h for 48 h found fewer deaths and fewer ventilator days. The explanation now states this rather than asserting benefit.",
  'PEST-12': "Card b gives activated charcoal 1 g/kg within 1 hour. Single-dose charcoal in organophosphate poisoning has no proven mortality benefit (negative Sri Lankan RCT) and carries aspiration risk in a patient with vomiting and a falling GCS — reasonable but not mandatory. Card c's glycopyrrolate figures (30% vs 90% confusion, 7.5 mg in 200 mL) come from a small single-centre study; kept as the card states.",
  'PEST-12 (FFP)': "Card d calls fresh frozen plasma harmful. The evidence is a single randomised pilot (Pichamuthu et al., Clin Toxicol 2010, Vellore: FFP vs albumin vs saline) in which FFP raised plasma cholinesterase but gave no improvement in deaths (4/19 vs 2/19 saline) or ventilator days (median 10 vs 7.5) — statistically no difference. 'No benefit, do not use' is defensible; 'harmful' overstates it. The explanation says so; if the exam asks for the harmful item on this list, FFP is still the intended answer.",
  'PEST-12 (magnesium)': "Card d says magnesium has 'no scientific data'. This is outdated: there are four randomised trials and several cohorts, pooled OR for mortality 0.55 (95% CI 0.32–0.94) in the systematic review by Brvar et al., Clin Toxicol 2018, with hypotension at the highest dose and the conclusion that evidence is insufficient to recommend it. The explanation states 'unproven rather than undocumented'.",
}
