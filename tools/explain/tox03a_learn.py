# TOX03A — Explain v2 ("Learn" depth). Organophosphates & carbamates. No mnemonics or hooks.
# Fields per card: sub, intro, parts, table (optional), mimic, traps, decode, punch, extra (optional)
L = {}

L['PEST-01'] = dict(
  sub="Toxicology → Pesticides → Scale and WHO hazard classes",
  intro="Organophosphates are the single biggest cause of fatal poisoning in the developing world, because they are cheap, sold without control and kept in the house where farming families live. Most deaths are deliberate self-poisoning, and most happen before or soon after the patient reaches hospital. The WHO grades the compounds by how little of them kills a rat, which is the only practical way of saying in advance how dangerous a bottle on a shelf is.",
  parts=[
    ('a', "**About 3 million people exposed and up to 300,000 deaths a year; the commonest poisoning in developing countries.** The case fatality is high — of the order of 10–20% in South Asian series — not because the drug is exotic but because the dose swallowed is large, the hospital is far and ventilation is scarce. In Indian ICU practice organophosphates compete only with aluminium phosphide (PEST-18) for the top place."),
    ('b', "**Class Ia extremely hazardous, oral LD50 <5 mg/kg; Ib highly hazardous 5–50; II moderately hazardous 50–2000; III slightly hazardous >2000; U unlikely to be hazardous ≥5000.** The LD50 is the single oral dose that kills half of a group of rats, so a smaller number means a more toxic compound. The classes therefore run the opposite way to the numbers: the lower the LD50, the higher the hazard class. The grading is of the technical compound, not of the diluted product in the bottle, so the formulation strength and the solvent still matter at the bedside."),
  ],
  mimic=[
    ("LD50 vs lethal dose in a patient", "LD50 is a population statistic in rats; it ranks compounds but does not predict what a given swallow will do to one person."),
    ("WHO hazard class vs clinical severity", "Class reflects intrinsic toxicity. Severity in the patient is set by the amount, the formulation and the delay to treatment, and is graded by RBC cholinesterase activity (PEST-09)."),
  ],
  traps=[
    ("“A high WHO class number means a more dangerous pesticide”", "It is the reverse: Ia is the most hazardous and III the least, because the class is defined by a low LD50."),
    ("“Organophosphate poisoning is mainly occupational”", "In South Asia the great majority is deliberate ingestion of a concentrated formulation; occupational exposure is usually mild and dermal."),
    ("“Deaths are falling because antidotes have improved”", "The fall where it has happened followed bans on the most hazardous compounds — supply, not antidote, drives mortality."),
  ],
  decode=[
    ("Commonest cause of fatal poisoning in a developing country", "Organophosphate pesticide."),
    ("“Oral LD50 <5 mg/kg” — WHO class?", "Class Ia, extremely hazardous."),
    ("Approximate annual global deaths from organophosphates", "Up to 300,000."),
  ],
  punch="The WHO class is only the compound’s intrinsic toxicity read backwards from its LD50 — the reason organophosphates kill 300,000 people a year is availability and dose, not subtlety.",
)

L['PEST-02'] = dict(
  sub="Toxicology → Pesticides → Classifying the compounds",
  intro="All organophosphates do the same thing to acetylcholinesterase, so the class matters for two other reasons: what the two alkyl side groups are, which decides how quickly the enzyme–poison bond becomes permanent, and how fat-soluble the compound is, which decides how long the illness lasts. Carbamates sit alongside them with the same clinical picture but a different chemistry. Nerve agents are the military members of the same family.",
  parts=[
    ('a', "**Dimethyl: dichlorvos, fenthion, malathion, methamidophos.** Two methyl groups are attached to the phosphorus. The bound enzyme loses one of them fast, so ageing takes only about 3 hours (PEST-03) and the window for an oxime is short."),
    ('b', "**Diethyl: chlorpyrifos, diazinon, parathion, quinalphos.** The bulkier ethyl groups are lost far more slowly, so ageing takes about 33 hours and oximes still work the next day. Several of these (chlorpyrifos, parathion, diazinon) are thions, which must be converted in the liver to their active oxon, so the onset of the cholinergic crisis may be delayed by hours and then prolonged — a feature of the thion chemistry rather than of the ethyl group itself."),
    ('c', "**Atypical: profenofos.** Its side chains do not fit the dimethyl or diethyl pattern, and the enzyme it inhibits is poorly reactivatable — the rescuable window is effectively absent, which is why oximes do little for it."),
    ('d', "**Nerve agents: sarin, tabun, soman, VX.** Chemical-warfare organophosphates, far more potent per milligram and absorbed through intact skin. Soman ages within minutes, which is why pretreatment with pyridostigmine and immediate antidote autoinjectors are used in that setting rather than oximes alone."),
    ('e', "**Carbamates: carbaryl, aldicarb, methomyl, propoxur.** They carbamylate the same esteratic site but the bond hydrolyses spontaneously, so there is no ageing, the illness is shorter and central features are fewer (PEST-03)."),
  ],
  table=dict(title="What the subclass changes", head=["Subclass", "Ageing", "Oxime value"], rows=[["Dimethyl", "**~3 h**", "narrow window"], ["Diethyl", "**~33 h**", "best"], ["Profenofos (atypical)", "fastest", "least"], ["Carbamate", "**none**", "not recommended (PEST-11)"]]),
  mimic=[
    ("Dimethyl vs diethyl compound", "Chemistry you must read off the bottle; it changes only one decision — how much an oxime can still achieve."),
    ("Lipophilic vs water-soluble organophosphate", "Fenthion, dichlofenthion and malathion are stored in fat and leach back out, so cholinergic features relapse for weeks; water-soluble agents give one defined illness."),
  ],
  traps=[
    ("“Malathion is harmless because it is used domestically”", "It is of low mammalian toxicity per milligram but highly lipophilic, so a large ingestion gives prolonged and relapsing illness."),
    ("“Nerve agents need different antidotes”", "The antidotes are the same — atropine and an oxime — but ageing is so fast with soman that the oxime must be given within minutes."),
    ("“Carbamates are mild”", "Aldicarb and methomyl are WHO class Ia and can kill quickly; what differs is the duration, not the severity."),
  ],
  decode=[
    ("Chlorpyrifos ingestion, pralidoxime at 20 hours — any point?", "Yes: diethyl, ageing half-life about 33 h."),
    ("Recurrent cholinergic crises over three weeks", "A lipophilic agent such as fenthion leaching from fat."),
    ("Which compound ages fastest?", "Profenofos (then dimethyl compounds; soman among nerve agents)."),
  ],
  punch="The subclass tells you nothing new about the toxidrome and everything about the clock: dimethyl ages in hours, diethyl in a day and a half, carbamates never — and the fat-soluble agents simply refuse to end.",
)

L['PEST-03'] = dict(
  sub="Toxicology → Pesticides → Mechanism and ageing",
  intro="Acetylcholinesterase sits in the synapse and splits acetylcholine the instant it is released. An organophosphate attacks its catalytic (esteratic) site and leaves a phosphate group stuck there, so transmitter accumulates everywhere acetylcholine is used — muscarinic, nicotinic and central synapses. At first that phosphate can still be pulled off; after a chemical rearrangement it cannot. That rearrangement, ageing, is the whole reason oxime treatment is a race.",
  parts=[
    ('a', "**Phosphorylates the esteratic site of acetylcholinesterase, so acetylcholine accumulates at muscarinic, nicotinic and CNS synapses.** The enzyme is normally the only route of acetylcholine removal, and it is fast enough to clear a synapse between impulses. With it inhibited the transmitter lingers, and every cholinergic receptor is stimulated continuously — which is why the picture is a sum of three receptor groups rather than one organ (PEST-04)."),
    ('b', "**Loss of an alkyl group from the bound enzyme: the bond becomes irreversible and oximes no longer work.** The phosphorylated enzyme can spontaneously shed one of its alkyl side chains, leaving a stable, negatively charged mono-alkyl phosphate on the active site. An oxime cannot attack that; recovery then depends on synthesis of new enzyme, which takes weeks."),
    ('c', "**Dimethyl about 3 hours; diethyl about 33 hours.** These are half-lives of ageing: time for half the inhibited enzyme to pass the point of rescue. The smaller methyl group leaves far more readily than the ethyl group, hence the tenfold difference."),
    ('d', "**A dimethyl patient arriving at 3 hours already has half the enzyme aged, so oximes work far better in diethyl poisoning; profenofos ages faster still.** This is why pralidoxime trials have been largely negative in populations dominated by dimethyl agents, and why an oxime is still worth giving a day later after chlorpyrifos. The oxime also slows further ageing, so it is started while the compound is unknown."),
    ('e', "**Carbamylation is reversible, with no ageing; shorter illness; little CNS penetration.** A carbamate forms a carbamyl–enzyme bond that hydrolyses by itself within hours, so the enzyme recovers without any antidote. Carbamates are also less lipophilic and more ionised, so they cross the blood–brain barrier poorly and cause fewer convulsions and less coma."),
  ],
  mimic=[
    ("Ageing vs enzyme regeneration", "Ageing is loss of rescuability within hours. Regeneration of aged enzyme is synthesis of new protein — RBC cholinesterase recovers at roughly 1% a day, so weeks."),
    ("Organophosphate vs carbamate at the bedside", "Identical cholinergic syndrome; carbamate illness resolves in a day or two, rarely shows the intermediate syndrome, and needs atropine but not an oxime."),
  ],
  traps=[
    ("“Ageing is faster with diethyl compounds”", "The opposite: dimethyl ~3 h, diethyl ~33 h — the smaller alkyl group is lost more easily."),
    ("“Pralidoxime can be given at any time”", "Once the enzyme has aged an oxime does nothing; its value falls with every hour and is near zero for profenofos."),
    ("“Carbamates need no treatment”", "They need atropine and often ventilation; what they do not need is an oxime, because there is nothing to rescue."),
  ],
  decode=[
    ("“Oximes would be least useful in poisoning with…”", "A dimethyl compound or profenofos."),
    ("Normal enzyme activity only after 4–6 weeks", "Aged enzyme — recovery depends on new synthesis."),
    ("Cholinergic crisis that resolves fully in 24 hours", "Carbamate: spontaneous decarbamylation."),
  ],
  punch="Inhibition is reversible for a few hours and then permanent, so everything in treatment is timed against ageing — fast in dimethyl and profenofos, slow in diethyl, and never in carbamates.",
  extra=[dict(q="Why does RBC cholinesterase take weeks to normalise after severe poisoning?", a="Aged enzyme cannot be reactivated; the red cell cannot make new enzyme, so activity returns only as new erythrocytes appear — about **1% a day**.")],
)

L['PEST-04'] = dict(
  sub="Toxicology → Pesticides → Receptor to symptom",
  intro="Everything in cholinergic poisoning follows from where acetylcholine receptors sit. Muscarinic receptors are on glands, smooth muscle and the heart’s pacemaker; nicotinic receptors are at the neuromuscular junction and in autonomic ganglia, including the sympathetic ones; and both types are in the brain. So the patient shows glandular flooding and bradycardia from one group, weakness and sometimes tachycardia and hypertension from another, and confusion, fits and loss of respiratory drive from the third. Death is respiratory, from all three at once.",
  parts=[
    ('a', "**Muscarinic — salivation, lacrimation, urination, diarrhoea, GI cramps, emesis; bradycardia, bronchorrhoea, bronchospasm; miosis.** Muscarinic stimulation turns on every exocrine gland and contracts smooth muscle, so secretions pour out at both ends and the airway narrows and fills. The vagus slows the sinus node, and the pupil constrictor contracts to a pinpoint. These are the effects atropine blocks, which is why atropine is titrated to a dry chest (PEST-10)."),
    ('b', "**Nicotinic — fasciculation, weakness, paralysis; tachycardia, hypertension, mydriasis from ganglionic stimulation.** At the neuromuscular junction persistent acetylcholine first makes muscle twitch and then depolarises the end-plate into a block, so fasciculation gives way to flaccid weakness, including the diaphragm. In autonomic ganglia the same receptor sits on the sympathetic pathway, so the patient may be tachycardic, hypertensive and even dilated in the pupils. Atropine does nothing here; only an oxime addresses it (PEST-11)."),
    ('c', "**CNS — confusion, coma, convulsions; central respiratory depression.** Lipophilic organophosphates cross into the brain, where cholinergic excess causes agitation, seizures and finally depression of the brainstem respiratory centre. Carbamates do this much less (PEST-03)."),
  ],
  table=dict(title="Three receptor groups, three sets of signs", head=["Receptor", "Signs", "Antidote"], rows=[["Muscarinic", "secretions, bronchospasm, bradycardia, miosis", "**atropine**"], ["Nicotinic", "fasciculation → weakness; tachycardia, hypertension", "**oxime**"], ["CNS", "coma, convulsions, apnoea", "atropine (central) + ventilation"]]),
  mimic=[
    ("Organophosphate vs opioid coma", "Both give small pupils and a failing respiratory effort; the organophosphate patient is wet, wheezy and fasciculating, the opioid patient dry (TOX-04)."),
    ("Nicotinic weakness vs the intermediate syndrome", "Early weakness accompanies the cholinergic crisis and improves with it; weakness appearing at 24–96 hours after the crisis has settled is the intermediate syndrome (PEST-06)."),
    ("Bilateral infiltrates: bronchorrhoea vs ARDS", "Both are non-cardiogenic with a normal CVP. Secretion flooding clears with suction and atropine; if the picture fits the Berlin timing and P/F it is ARDS and needs lung-protective ventilation."),
  ],
  traps=[
    ("“Tachycardia excludes organophosphate poisoning”", "Ganglionic nicotinic stimulation, hypoxia, pain and bronchospasm all raise the rate; a substantial minority of patients are tachycardic rather than bradycardic on arrival."),
    ("“Dilated pupils rule it out”", "Ganglionic sympathetic stimulation can dilate the pupil, and atropine already given will too."),
    ("“Atropine will stop the fasciculations and the weakness”", "Those are nicotinic; atropine has no action at the neuromuscular junction."),
  ],
  decode=[
    ("Pinpoint pupils, wet patient, wheeze, fasciculations", "Organophosphate — muscarinic plus nicotinic."),
    ("Organophosphate poisoning with heart rate 120", "Still organophosphate; nicotinic ganglionic effect — do not withhold atropine."),
    ("Bilateral infiltrates, normal CVP, after organophosphate ingestion", "Non-cardiogenic pulmonary oedema from bronchorrhoea, permeability and aspiration; call it ARDS when the stem gives Berlin criteria."),
  ],
  punch="Read the patient receptor by receptor: glands and airway are muscarinic and answer to atropine, muscle and ganglia are nicotinic and answer only to an oxime, and the brain adds coma and apnoea — which is why these patients die of their airway, not their heart.",
  extra=[dict(q="Why does the ECG sometimes show a long QTc?", a="Organophosphates prolong repolarisation and are associated with **QTc prolongation and torsade**; a long QTc marks more severe poisoning and worse outcome."),
         dict(q="What is the actual mode of death?", a="**Respiratory** — bronchorrhoea and bronchospasm, nicotinic failure of the diaphragm, and central apnoea together; hence airway, suction and ventilation rank with atropine.")],
)

L['PEST-05'] = dict(
  sub="Toxicology → Pesticides → The three paralyses",
  intro="Weakness in organophosphate poisoning comes in three separate waves with different mechanisms, so the same patient can be weak on day one, recover, become weak again on day three, and develop a quite different weakness three weeks later. Keeping them apart matters because only the first responds to atropine, the second needs a ventilator and nothing else, and the third is a neuropathy that no antidote touches.",
  parts=[
    ('a', "**Type I — acute cholinergic crisis: minutes to hours, generalised weakness with fasciculation, responds to atropine.** This is the cholinergic flood itself (PEST-04): muscarinic secretions and bronchospasm alongside nicotinic fasciculation and depolarising block. Atropine reverses the muscarinic half, which is what saves the airway."),
    ('b', "**Type II — intermediate syndrome: 24–96 hours, neck flexors, proximal limb, cranial nerve and respiratory muscles, no response to atropine.** It appears after the cholinergic crisis has settled, in a patient who looked to be recovering, and is a post-synaptic nicotinic problem — persistent stimulation with receptor down-regulation (PEST-06). Atropine cannot help because no muscarinic receptor is involved."),
    ('c', "**Type III — delayed neuropathy (OPIDN): 1–3 weeks, distal muscles, legs first, ascending, no response to atropine.** This is a dying-back axonopathy from inhibition of a different enzyme, neuropathy target esterase, not acetylcholinesterase at all (PEST-07) — hence the different timing, the distal pattern and the uselessness of cholinergic antidotes."),
  ],
  table=dict(title="Telling the three apart", head=["", "Type I", "Type II", "Type III"], rows=[["Onset", "minutes–hours", "**24–96 h**", "**1–3 weeks**"], ["Pattern", "generalised, fasciculation", "**neck flexors, proximal, cranial, respiratory**", "**distal, legs first, ascending**"], ["Enzyme", "AChE", "AChE (nicotinic receptor)", "**neuropathy target esterase**"], ["Atropine", "responds", "no", "no"], ["Treatment", "atropine, oxime, airway", "ventilation", "physiotherapy, time"]]),
  mimic=[
    ("Intermediate syndrome vs Guillain–Barré", "Both give ascending or proximal weakness with respiratory failure; the intermediate syndrome follows a documented cholinergic crisis by 1–4 days, spares sensation and has normal CSF."),
    ("OPIDN vs intermediate syndrome", "Distal and sensory at 1–3 weeks versus proximal, neck-flexor and respiratory at 24–96 hours."),
    ("Type II weakness vs prolonged suxamethonium block", "Suxamethonium given to such a patient is metabolised by the inhibited plasma enzyme and paralyses for hours (PEST-12); the history separates them."),
  ],
  traps=[
    ("“Intermediate syndrome affects distal muscles first”", "It is neck flexors and proximal muscles; distal, ascending weakness is the delayed neuropathy."),
    ("“More atropine will fix the weakness on day three”", "Type II is nicotinic; extra atropine only adds delirium and tachycardia."),
    ("“Recovery from the cholinergic crisis means the patient can be extubated and discharged”", "The intermediate syndrome begins exactly then — keep the patient where ventilation is available for 4 days."),
  ],
  decode=[
    ("Day 3, cannot lift head off the pillow, atropine not helping", "Intermediate syndrome — ventilate."),
    ("Three weeks later, distal leg weakness with absent ankle jerks", "OPIDN."),
    ("Fasciculations with secretions on arrival", "Type I acute cholinergic crisis."),
  ],
  punch="Three waves, three mechanisms: the cholinergic flood answers to atropine, the intermediate syndrome answers only to a ventilator, and the delayed neuropathy belongs to a different enzyme altogether.",
)

L['PEST-06'] = dict(
  sub="Toxicology → Pesticides → Intermediate syndrome",
  intro="The dangerous moment in organophosphate poisoning is not always the first day. In a substantial minority the cholinergic crisis settles, atropine is weaned, and then over a few hours the patient cannot hold the head up, cannot cough and stops breathing adequately. Nothing prevents it, nothing shortens it, and the only thing that matters is that a ventilator is ready when it happens.",
  parts=[
    ('a', "**10–40% of patients; 24–96 hours after exposure, after the cholinergic crisis has resolved.** The wide range reflects how it is defined and which agents dominate a given series. The timing is the point: it begins when the muscarinic features have gone and the patient appears to be improving."),
    ('b', "**Neck flexion weakness (cannot lift the head off the pillow), proximal limb weakness, cranial nerve palsies, reduced reflexes, respiratory failure.** The muscles affected are those with the least reserve against a failing neuromuscular junction — neck flexors, shoulder and hip girdle, the bulbar muscles and the diaphragm. Distal strength and sensation are preserved, which separates it from the delayed neuropathy (PEST-07)."),
    ('c', "**Highly fat-soluble agents; possibly inadequate oxime dosing.** Lipophilic compounds such as fenthion and dichlofenthion keep releasing poison from fat, so the junction never gets a clean interval (PEST-02). Whether too little oxime contributes is debated, which is one argument for a sustained infusion rather than boluses (PEST-11)."),
    ('d', "**Persistent nicotinic over-stimulation with receptor down-regulation and muscle necrosis.** Continuous acetylcholine at the end-plate causes post-synaptic receptor down-regulation and desensitisation, and calcium entry damages the muscle fibre itself — a myopathy with a raised creatine kinase. The mechanism is still not settled, but all the proposed ones are post-synaptic and structural, which is why neither atropine nor an oxime alters the course."),
    ('e', "**Supportive ventilation; no treatment prevents it.** Recovery takes days to two or three weeks as receptors are restored and muscle repairs. The clinical task is anticipation: watch head lift, single-breath count and vital capacity, and intubate before the patient tires rather than after."),
  ],
  mimic=[
    ("Intermediate syndrome vs recurrent cholinergic crisis", "A relapse of secretions, wheeze and miosis is cholinergic and needs atropine again; pure weakness with a dry chest is the intermediate syndrome."),
    ("Intermediate syndrome vs myasthenic crisis", "Same pattern of proximal, bulbar and respiratory weakness; the poisoning history and the preceding cholinergic phase decide it."),
  ],
  traps=[
    ("“It is a late cholinergic relapse, so give more atropine”", "It is nicotinic and post-synaptic; atropine does not treat it."),
    ("“The patient is well at 24 hours, so discharge”", "This is precisely the window in which the syndrome begins; observe for at least 4 days after a significant ingestion."),
    ("“It means the poisoning was mild if the pupils are normal”", "Pupils and secretions are irrelevant by then — the sign to follow is whether the head can be lifted off the pillow."),
  ],
  decode=[
    ("Weakness of neck flexion 48 hours after chlorpyrifos", "Intermediate syndrome."),
    ("Which syndrome needs only ventilation?", "Intermediate syndrome — nothing prevents or shortens it."),
    ("Risk factor for intermediate syndrome", "A highly fat-soluble agent such as fenthion."),
  ],
  punch="The intermediate syndrome is the trap of the second and third day: the cholinergic storm is over, the antidote is being weaned, and the only treatment for the weakness that follows is a ventilator you decided on early.",
)

L['PEST-07'] = dict(
  sub="Toxicology → Pesticides → Delayed neuropathy (OPIDN)",
  intro="Weeks after the poisoning is over, some patients return with numb feet and a slapping gait. This has nothing to do with acetylcholinesterase: certain organophosphates inhibit another esterase in the axon, and the long nerves degenerate from their tips backwards. Because the mechanism is separate, so is everything else — the timing, the pattern and the fact that the severity of the acute illness predicts nothing.",
  parts=[
    ('a', "**Inhibition of neuropathy target esterase, not acetylcholinesterase.** The compound phosphorylates this axonal enzyme and then undergoes its own ageing reaction; the modified enzyme, rather than simple loss of its function, triggers a dying-back degeneration of the longest axons. Cholinergic antidotes are therefore irrelevant."),
    ('b', "**Stocking-and-glove paraesthesia, then distal flaccid weakness of the legs ascending to the arms; absent ankle jerks.** The longest fibres fail first, so symptoms begin in the feet and hands, sensory before motor, with wasting and loss of the ankle jerk. It is a peripheral axonopathy, so there is no sphincter or cranial involvement, and some patients are left with spasticity from an associated central component."),
    ('c', "**Chlorpyrifos is the typical agent.** Among the compounds in common agricultural use it is the one most often reported; the classic historical examples were triorthocresyl phosphate (contaminated cooking oil and ‘ginger jake’ paralysis) and mipafox."),
    ('d', "**Independent of the severity of the acute poisoning: it can follow a mild acute illness.** The two enzymes are different proteins with different sensitivities, so a compound can inhibit neuropathy target esterase appreciably while causing only modest cholinergic symptoms. A patient who never needed much atropine may still develop the neuropathy at three weeks."),
    ('e', "**Carbamates only rarely cause it.** Carbamates inhibit neuropathy target esterase weakly and their bond does not age in the way required to trigger degeneration, so the syndrome is exceptional with them."),
  ],
  mimic=[
    ("OPIDN vs Guillain–Barré syndrome", "Both ascend; OPIDN starts 1–3 weeks after a known exposure, progresses over days to weeks rather than hours, and has normal CSF protein."),
    ("OPIDN vs critical illness polyneuropathy", "Indistinguishable electrically at times; the exposure history and onset after recovery rather than during sepsis separate them."),
  ],
  traps=[
    ("“Delayed neuropathy follows only severe poisoning”", "It is independent of acute severity, because a different enzyme is involved."),
    ("“Pralidoxime given early prevents it”", "Oximes act on acetylcholinesterase; they do not protect neuropathy target esterase."),
    ("“Weakness at 10 days is the intermediate syndrome”", "That window has passed: at 1–3 weeks with distal sensory loss this is OPIDN (PEST-05)."),
  ],
  decode=[
    ("Enzyme inhibited in delayed neuropathy", "Neuropathy target esterase."),
    ("Three weeks after chlorpyrifos: numb feet, foot drop, absent ankle jerks", "OPIDN."),
    ("Does a mild acute illness exclude it?", "No — severity is unrelated."),
  ],
  punch="OPIDN is organophosphate poisoning in a different enzyme: a dying-back axonopathy of the longest nerves that arrives weeks later, ignores how ill the patient was, and has no antidote.",
)

L['PEST-08'] = dict(
  sub="Toxicology → Pesticides → Delayed manifestations by time",
  intro="Organophosphate poisoning is not one illness but a sequence spread over three weeks, and most of the sequence appears after the patient has been declared out of danger. The order follows the mechanisms: continuing absorption first, then the neuromuscular junction, then the brain, and last the peripheral axon. Knowing when each is due is what sets the length of observation.",
  parts=[
    ('a', "**Delayed-onset cholinergic phase at 40–48 hours.** Seen with lipophilic compounds and with thion compounds needing hepatic conversion to their active oxon (chlorpyrifos, parathion, fenthion, malathion), so poison keeps arriving at the synapse and secretions and miosis return after an apparent recovery. This phase does respond to atropine."),
    ('b', "**Intermediate syndrome at 24–96 hours.** Post-synaptic nicotinic failure of neck flexors, proximal, bulbar and respiratory muscles, needing ventilation and nothing else (PEST-06)."),
    ('c', "**Late-onset intermediate syndrome at about 114 hours.** The same syndrome appearing beyond the usual four days, again typically with fat-soluble agents whose release from adipose tissue is still going on."),
    ('d', "**Delayed encephalopathy or coma at 4–6 days.** A central cholinergic and possibly hypoxic-metabolic effect appearing after the acute phase, with confusion, drowsiness or coma and no new muscarinic signs."),
    ('e', "**Cerebellar ataxia at about 8 days.** Transient cerebellar dysfunction with gait and limb ataxia, usually self-limiting over weeks."),
    ('f', "**Extrapyramidal syndrome at 5–15 days.** Dystonia, rigidity and tremor, attributed to striatal cholinergic–dopaminergic imbalance; generally reversible."),
    ('g', "**Delayed neuropathy at 1–3 weeks.** The neuropathy target esterase axonopathy — distal, sensory then motor, ascending (PEST-07)."),
  ],
  table=dict(title="The timeline", head=["Time", "Manifestation"], rows=[["24–96 h", "**intermediate syndrome**"], ["40–48 h", "delayed cholinergic phase"], ["~114 h", "late-onset intermediate syndrome"], ["4–6 days", "delayed encephalopathy or coma"], ["8 days", "cerebellar ataxia"], ["5–15 days", "extrapyramidal syndrome"], ["1–3 weeks", "**delayed neuropathy**"]]),
  mimic=[
    ("Delayed cholinergic phase vs intermediate syndrome", "Secretions, wheeze and miosis returning means cholinergic and needs atropine; pure weakness with a dry chest does not."),
    ("Delayed encephalopathy vs hypoxic brain injury", "Overlapping; a patient who was never hypoxic and has normal imaging points to the toxic encephalopathy."),
  ],
  traps=[
    ("“Everything happens in the first 24 hours”", "Most of the syndromes begin after 24 hours, which is why observation runs for at least four days and follow-up for weeks."),
    ("“Movement disorder after organophosphate means permanent brain injury”", "The extrapyramidal and cerebellar syndromes are usually transient."),
    ("“A patient asymptomatic at 12 hours after a fat-soluble agent can go home”", "Fenthion and relatives can declare themselves at 40–48 hours or later."),
  ],
  decode=[
    ("Ataxia at one week after poisoning", "Delayed cerebellar syndrome."),
    ("Dystonia 10 days later", "Extrapyramidal syndrome."),
    ("Reappearance of secretions at 44 hours", "Delayed-onset cholinergic phase — atropine again."),
  ],
  punch="The poisoning unfolds for three weeks, and the order is mechanistic: continuing absorption, then the junction, then the brain, then the axon — so observation is measured in days and follow-up in weeks.",
)

L['PEST-09'] = dict(
  sub="Toxicology → Pesticides → Diagnosis: cholinesterases and the atropine challenge",
  intro="The diagnosis is clinical, but two blood enzymes are often measured and they answer different questions. One is the same enzyme as in the synapse and tracks how poisoned the patient is; the other is a liver protein that merely proves exposure. Where neither assay is available, a small dose of atropine can be used as a test: a patient with real cholinergic excess barely responds to it.",
  parts=[
    ('a', "**RBC cholinesterase is true (acetyl) cholinesterase: it mirrors the synaptic enzyme and correlates with severity.** It is the identical enzyme on the red cell membrane, so its inhibition reflects inhibition at the junction. Severity grades with activity: roughly 20–50% of normal is mild, 10–20% moderate and under 10% severe, with coma, flaccid paralysis, bronchorrhoea or pulmonary oedema at the severe end. Because red cells cannot resynthesise it, recovery is slow — about 1% a day."),
    ('b', "**Plasma cholinesterase is pseudo (butyryl) cholinesterase, made in the liver: a simple marker of exposure with no correlation with severity.** It is inhibited earlier and more readily, so it is a sensitive screen, but its baseline varies widely and falls in liver disease, pregnancy, malnutrition and genetic variants. It also recovers within days as the liver makes more, which can mislead. Its one practical use is a warning that suxamethonium will be prolonged (PEST-12)."),
    ('c', "**Atropine challenge: a rise in heart rate of more than 20–25/min with flushing after a small dose means no significant cholinergic poisoning.** A test dose of around 1–2 mg is given. In a genuinely poisoned patient the muscarinic receptors are swamped with acetylcholine, so a small competitive antagonist dose produces little change; an unpoisoned patient shows the expected tachycardia, dry mouth and flush. It is a bedside substitute where assays are unavailable, not a substitute for clinical judgement."),
  ],
  table=dict(title="The two enzymes", head=["", "RBC (true) AChE", "Plasma (pseudo) BChE"], rows=[["Same enzyme as synapse", "**yes**", "no"], ["Tracks severity", "**yes**", "no"], ["Sensitivity to exposure", "lower", "higher"], ["Recovery", "~1%/day, weeks", "days"], ["Use", "**severity, prognosis**", "exposure; suxamethonium warning"]]),
  mimic=[
    ("Low plasma cholinesterase from poisoning vs other causes", "Liver disease, pregnancy, malnutrition and genetic variants all lower it; only the clinical picture and the RBC enzyme confirm poisoning."),
    ("Atropine challenge vs atropine loading", "The challenge is one small diagnostic dose; loading is 2–5 mg doubled every 5 minutes to an end-point (PEST-10)."),
  ],
  traps=[
    ("“Plasma cholinesterase correlates with severity”", "It does not — the RBC enzyme does; plasma activity only shows exposure."),
    ("“A normal cholinesterase excludes poisoning”", "Baselines vary several-fold between people, so an individual’s ‘normal’ value may already represent a large fall; treat the patient."),
    ("“Wait for the assay before giving atropine”", "Treatment is clinical and immediate; the assay is confirmatory and often retrospective."),
  ],
  decode=[
    ("Which enzyme grades severity?", "RBC (true) acetylcholinesterase — severe under 10% of normal."),
    ("Marker of mere exposure", "Plasma (butyryl) cholinesterase."),
    ("Heart rate rises 30/min after 1 mg atropine", "No significant cholinergic poisoning."),
  ],
  punch="The red cell enzyme is the synapse in a tube and grades severity; plasma cholinesterase only says the patient met the poison — and if neither is available, a patient who shrugs off a test dose of atropine is the one who needs it.",
  extra=[dict(q="Severity bands by RBC acetylcholinesterase activity?", a="**Mild 20–50%**, moderate 10–20%, **severe <10%** of normal; severe poisoning shows coma, flaccid paralysis, bronchorrhoea or pulmonary oedema and pinpoint pupils.")],
)

L['PEST-10'] = dict(
  sub="Toxicology → Pesticides → Atropine",
  intro="Atropine is a competitive muscarinic antagonist, so it must outnumber the acetylcholine piling up in the synapse — which means the dose is whatever it takes, not a number from a book. The thing it is competing for is the airway: secretions and bronchospasm are what kill these patients in the first hours. So the dose is escalated fast and judged by the chest, not by the pupils or the pulse.",
  parts=[
    ('a', "**2–5 mg IV, doubling every 5 minutes until atropinised.** Fixed small doses given slowly lose the race against a synapse flooded with transmitter, so the dose is doubled rather than repeated — 2, 4, 8, 16 mg and beyond — until the end-points are met. Published protocols open with 1.8–3 mg and then double in the same way, so the card's 2–5 mg is the same practice. Total requirements from about 10 mg up to 100 mg or more in the first day are usual, and giving too little is the commoner error."),
    ('b', "**End-points: a clear chest with no wheeze or secretions, heart rate above 80, systolic pressure above 80, dry axillae, and pupils no longer pinpoint.** The chest is the one that matters, because bronchorrhoea and bronchospasm are the lethal muscarinic effects; the others confirm that enough has been given to reach the whole muscarinic system. Pupils are the least reliable end-point — they respond late and may be affected by continuing absorption."),
    ('c', "**Maintenance by infusion of 10–20% of the total loading dose per hour.** Atropine’s effect lasts a few hours while the organophosphate persists for days, so stopping after loading lets the patient relapse. Running a fraction of the dose that worked keeps the chest dry and allows titration up or down against the same end-points."),
    ('d', "**If atropine toxicity occurs, stop, then restart at 70–80% of the previous rate.** Over-atropinisation gives agitation, delirium, hyperthermia, ileus, urinary retention and tachyarrhythmia — and because it is a hot, dry, confused patient, it mimics worsening poisoning. Brief interruption and a modest reduction keep the airway protected without the delirium."),
    ('e', "**It does not treat the nicotinic effects: weakness and paralysis.** There are no muscarinic receptors at the neuromuscular junction, so fasciculation, weakness and respiratory muscle failure are untouched; they need an oxime and often a ventilator (PEST-11, PEST-05)."),
  ],
  table=dict(title="What to titrate against", head=["End-point", "Target"], rows=[["Chest", "**clear — no wheeze, no secretions**"], ["Axillae", "**dry**"], ["Heart rate", ">80/min"], ["Systolic BP", ">80 mmHg"], ["Pupils", "no longer pinpoint (least reliable)"]]),
  mimic=[
    ("Atropine toxicity vs continuing poisoning", "Both give a confused, tachycardic patient; atropine excess has a dry chest, absent bowel sounds and a full bladder, continuing poisoning a wet, wheezy chest."),
    ("Atropine vs glycopyrrolate", "Glycopyrrolate does not cross into the brain, so it dries secretions with far less delirium but cannot treat central effects (PEST-12)."),
  ],
  traps=[
    ("“Atropinisation is judged by dilated pupils”", "The end-point is a dry chest; pupils are slow and unreliable."),
    ("“Tachycardia is a reason to withhold atropine”", "Tachycardia is usually hypoxia, bronchospasm or ganglionic stimulation; a wet chest still needs atropine."),
    ("“A fixed 0.6 mg dose repeated as needed”", "Too small and too slow — the dose is doubled every 5 minutes until the chest is clear."),
  ],
  decode=[
    ("End-point of atropinisation", "Clear chest and dry axillae."),
    ("Agitated, hot, dry patient with absent bowel sounds on day 2", "Atropine toxicity — stop, restart at 70–80%."),
    ("Which effects does atropine not treat?", "Nicotinic — weakness, fasciculation, paralysis."),
  ],
  punch="Atropine is titrated against the airway and nothing else: double the dose until the chest is clear and the axillae dry, keep an infusion going because the poison outlasts the drug, and accept that weakness is not its business.",
)

L['PEST-11'] = dict(
  sub="Toxicology → Pesticides → Oximes",
  intro="Atropine blocks the receptor; an oxime attacks the problem one step upstream by taking the phosphate off the enzyme and giving the synapse its acetylcholinesterase back. That is the only way the nicotinic effects — fasciculation, weakness, respiratory muscle failure — can be treated at all. It works only while the bond is still rescuable, which is why it is started at once and given in a way that keeps the plasma level up.",
  parts=[
    ('a', "**Pralidoxime, obidoxime, trimedoxime.** All are quaternary oximes; pralidoxime is the one available in India (as the chloride or iodide), obidoxime is used mainly in Europe and is somewhat more potent against some compounds."),
    ('b', "**They bind the anionic site and pull the phosphate off the esteratic site, reactivating cholinesterase before ageing; they also slow further ageing.** The charged oxime docks onto the enzyme’s anionic subsite, which positions its nucleophilic oxime group next to the phosphorus; it then strips the phosphate off as a phosphoryl-oxime. Reactivated enzyme clears acetylcholine again, so fasciculation and weakness improve — the effects atropine cannot reach."),
    ('c', "**Pralidoxime 1–2 g over 30 minutes, repeated in 1 hour if weakness persists, or given as an infusion.** Weight-based WHO dosing is a 30 mg/kg bolus (about 2 g) over 30 minutes followed by 8 mg/kg/h (about 500 mg/h), continued until atropine is no longer needed. The reasoning for an infusion rather than intermittent boluses is that a plasma concentration above roughly 4 mg/L has to be sustained to outpace re-inhibition from drug still being absorbed and released from fat. The clinical evidence is thin and conflicting: a small Indian trial of a sustained high-dose regimen (1 g every hour for 48 hours against 1 g every four hours) found fewer deaths and a shorter time on the ventilator, whereas a placebo-controlled trial of the WHO regimen in Sri Lanka showed no clinical benefit and a trend towards harm despite reactivating blood cholinesterase."),
    ('d', "**Not recommended in carbamate poisoning, but do not withhold it when the agent is unknown.** Carbamylated enzyme hydrolyses by itself within hours, so there is nothing to rescue, and with carbaryl there is old experimental evidence of worse outcome. In practice the bottle is often unidentified and a mixed or organophosphate exposure cannot be excluded, so the oxime is given."),
    ('e', "**Useless once the enzyme has aged; no CNS effect; rapid injection causes laryngospasm, hypertension and vomiting.** Aged enzyme offers no bond for the oxime to attack (PEST-03). Being permanently charged, pralidoxime scarcely crosses the blood–brain barrier, so it does nothing for coma or convulsions. Given as a fast push it causes laryngospasm, muscle rigidity, hypertension and vomiting — hence a 30-minute infusion."),
  ],
  mimic=[
    ("Atropine vs pralidoxime", "Atropine blocks muscarinic receptors and treats secretions; pralidoxime restores the enzyme and is the only treatment for nicotinic weakness. They are always given together."),
    ("Oxime failure from ageing vs from under-dosing", "Dimethyl or profenofos poisoning ages past rescue within hours; under-dosing shows as weakness that improves when a proper infusion is started."),
  ],
  traps=[
    ("“Oximes are recommended in carbamate poisoning”", "They are not — carbamylated enzyme recovers spontaneously; but an unknown agent is still treated."),
    ("“Pralidoxime instead of atropine if secretions are heavy”", "It has no muscarinic action; secretions need atropine."),
    ("“Give the 1 g dose as a bolus to save time”", "Rapid injection causes laryngospasm and hypertension; infuse over 30 minutes."),
    ("“Trial evidence settles the question either way”", "It does not: the Cochrane review concludes the evidence is insufficient to show oximes are beneficial or harmful, and the trials were dominated by dimethyl compounds and late presentation. An oxime is still started early, when the compound is unknown and the bond may still be rescuable, but it cannot be relied on to change the outcome."),
  ],
  decode=[
    ("Which effects do oximes treat that atropine cannot?", "Nicotinic — fasciculation, weakness, respiratory failure."),
    ("WHO pralidoxime regimen", "30 mg/kg (~2 g) over 30 min, then 8 mg/kg/h (~500 mg/h) until atropine is no longer needed."),
    ("Is the WHO regimen proven to save lives?", "No — a placebo-controlled trial of it showed no clinical benefit; the evidence overall is insufficient either way."),
    ("Hypertension and laryngospasm during the antidote", "Pralidoxime given too fast."),
  ],
  punch="An oxime is the only drug that gives the enzyme back, so it is the only treatment for nicotinic weakness — started early, infused rather than pushed, and worthless once the bond has aged.",
  extra=[dict(q="Why an infusion rather than repeated boluses?", a="A plasma level above about **4 mg/L** has to be sustained to outrun re-inhibition from drug still being absorbed and released from fat, before ageing fixes the bond.")],
)

L['PEST-12'] = dict(
  sub="Toxicology → Pesticides → Other measures",
  intro="Beyond atropine and an oxime, management is airway, decontamination and avoiding harm. Two details are specific to this poisoning: the muscle relaxant used for intubation is cleared by the very enzyme the poison has inhibited, and the poison is still on the patient’s skin and in the vomit, so it keeps being absorbed — by the patient and by the staff. A long list of plausible-sounding extras has no benefit and one is harmful.",
  parts=[
    ('a', "**Avoid succinylcholine: it is metabolised by plasma cholinesterase, so paralysis is prolonged.** With the plasma enzyme inhibited, a standard dose can paralyse for hours rather than minutes. Use a non-depolarising agent — rocuronium — recognising that higher doses may be needed since acetylcholine is competing at the junction."),
    ('b', "**Remove clothes and wash the skin; activated charcoal 1 g/kg within 1 hour; no forced emesis.** Organophosphates are absorbed through intact skin and evaporate from soaked clothing, so undressing and washing with soap and water stops further absorption — and protects the team, who need gloves, gown, eye protection and a ventilated space, since vomit and clothing release the agent. Charcoal binds any that remains in the gut if given early. Induced emesis is dangerous in a patient who may convulse or lose airway control within minutes, and gastric lavage has no proven benefit."),
    ('c', "**Glycopyrrolate does not cross the blood–brain barrier: added to atropine it caused far less confusion and hallucination (30% versus 90%) and less tachyarrhythmia, with the same outcome. Dose 7.5 mg in 200 mL, infused until the mucous membranes are dry.** Being a quaternary amine it is excluded from the brain, so it dries secretions peripherally without central antimuscarinic delirium. It cannot replace atropine entirely, because central respiratory depression and seizures need a drug that does get in."),
    ('d', "**Fresh frozen plasma is harmful; haemodialysis and bicarbonate have no role; magnesium has no scientific data, and clonidine and vitamin E rest on animal studies only.** FFP has been proposed as a source of butyrylcholinesterase to scavenge circulating poison. The one randomised pilot trial (FFP against albumin against saline, in India) did raise plasma cholinesterase but produced no improvement in deaths or ventilator days, with a numerically longer time ventilated in the FFP arm — so the honest position is no benefit rather than proven harm, and it is not recommended. Organophosphates are lipophilic with a large volume of distribution and are not meaningfully cleared by dialysis, and the acidosis in these patients is from hypoxia and shock, so bicarbonate treats nothing. Magnesium is better described as unproven than undocumented: several small trials exist and pooled together they hint at lower mortality, but they are too small and too heterogeneous to recommend, and the higher doses caused hypotension."),
  ],
  mimic=[
    ("Glycopyrrolate vs atropine", "Glycopyrrolate dries without delirium but has no central action; atropine remains the drug for central effects and the one titrated to the chest (PEST-10)."),
    ("Rocuronium vs succinylcholine here", "Succinylcholine depends on the inhibited plasma enzyme; rocuronium does not, though its dose may need to be higher."),
  ],
  traps=[
    ("“Give fresh frozen plasma to replace cholinesterase”", "It raises the plasma enzyme without improving survival or ventilator days in the one randomised trial, and carries the usual transfusion risks; it is not a treatment for organophosphate poisoning."),
    ("“Dialyse the organophosphate”", "Large volume of distribution and high lipid solubility — dialysis removes nothing useful."),
    ("“Decontamination is only for the patient”", "Staff are exposed through vomit and soaked clothing; gloves, gown, eye protection and ventilation are part of the procedure."),
    ("“Induce vomiting to get the poison out”", "Forced emesis risks aspiration and convulsion; use early charcoal instead."),
  ],
  decode=[
    ("Intubating drug to avoid in organophosphate poisoning", "Succinylcholine — prolonged block."),
    ("Atropine-induced delirium: what to add?", "Glycopyrrolate, 7.5 mg in 200 mL to dry mucous membranes."),
    ("Which listed therapy is the one to answer as harmful?", "Fresh frozen plasma (the trial evidence shows no benefit)."),
  ],
  punch="The extras are mostly about not adding harm: no succinylcholine, no forced emesis, no dialysis or bicarbonate, never FFP — while the things that do work are washing the patient, protecting the team and keeping the chest dry.",
)

L['PEST-13'] = dict(
  sub="Toxicology → Pesticides → True or false",
  intro="These eight statements are the deck’s key discriminations, and each one turns on a mechanism met earlier: which alkyl group ages faster, which enzyme is the synapse’s own, which receptor each antidote reaches, and which muscles fail when.",
  parts=[
    ('a', "**False — dimethyl compounds age in about 3 hours, diethyl in about 33.** The smaller methyl group is shed far more readily from the phosphorylated enzyme, so it is the dimethyl patient whose window for an oxime has closed (PEST-03)."),
    ('b', "**False — the RBC (true) enzyme correlates with severity.** Plasma butyrylcholinesterase is a liver protein with a wide normal range; it shows exposure only (PEST-09)."),
    ('c', "**False — the intermediate syndrome affects neck flexors and proximal muscles first.** Distal, ascending weakness at 1–3 weeks is the delayed neuropathy instead (PEST-05, PEST-07)."),
    ('d', "**False — delayed neuropathy is independent of acute severity.** It follows inhibition of neuropathy target esterase, a different enzyme, so it can follow a mild cholinergic illness (PEST-07)."),
    ('e', "**False — fasciculation is nicotinic, and atropine is purely antimuscarinic.** There are no muscarinic receptors at the neuromuscular junction; only an oxime addresses it (PEST-10, PEST-11)."),
    ('f', "**False — oximes are not recommended in carbamate poisoning.** Carbamylated enzyme hydrolyses spontaneously, so there is nothing to reactivate; they are still given when the agent is unknown (PEST-11)."),
    ('g', "**True — atropinisation is judged by a dry chest.** Clear lungs and dry axillae, not dilated pupils or a particular heart rate, are the end-point, because bronchial secretions are what kill (PEST-10)."),
    ('h', "**False — tachycardia does not exclude organophosphate poisoning.** Nicotinic ganglionic stimulation, hypoxia and bronchospasm all raise the rate (PEST-04)."),
  ],
  mimic=[
    ("Dry chest vs dilated pupils as the atropine end-point", "The chest is the lethal muscarinic target; pupils respond late and unreliably."),
    ("RBC vs plasma cholinesterase", "Same words, different enzymes: one is the synaptic enzyme and grades severity, the other a liver marker of exposure."),
  ],
  traps=[
    ("“Pinpoint pupils are needed to make the diagnosis”", "Pupils may be normal or dilated from ganglionic stimulation or atropine already given."),
    ("“Atropine covers the whole syndrome”", "It covers only the muscarinic part; nicotinic weakness and central effects need an oxime and a ventilator."),
  ],
  decode=[
    ("Statements about ageing", "Check which alkyl group — dimethyl is the fast one."),
    ("Statements about antidotes", "Ask which receptor the drug reaches: atropine muscarinic, oxime the enzyme itself."),
  ],
  punch="Every statement here comes back to three questions: which alkyl group is on the phosphorus, which enzyme is being measured, and which receptor the antidote can actually reach.",
)

FLAGS = {
  'PEST-01': "Card a gives up to 300,000 deaths a year from organophosphates specifically; most sources quote ~250,000–370,000 deaths from pesticide self-poisoning as a whole, with organophosphates the largest share. Card figure kept. The WHO classification quoted is the older oral-LD50 table (the 2019 revision also uses dermal LD50 and reclassifies some compounds) — fine for exam use.",
  'PEST-02': "Card lists malathion as dimethyl (correct) and the watch note calls it lipophilic (correct), but malathion is of low mammalian toxicity because of rapid carboxylesterase detoxification; a stem pairing malathion with rapid death is usually testing formulation/solvent or massive dose. No change needed.",
  'PEST-09': "Card c gives the atropine challenge as a rise in heart rate >20–25/min with flushing after a small dose. This is traditional teaching from resource-limited settings, not a validated test, and it is absent from Goldfrank's/UpToDate; it should not delay empirical atropine. Card statement kept.",
  'PEST-10': "Card c itself notes the maintenance infusion (10–20% of the loading dose per hour) is standard teaching not in Naven's notes — confirmed correct and widely used, so it is explained as standard. Card b's heart rate >80 and systolic >80 are the published atropinisation end-points; some protocols drop the pupil criterion entirely because it is unreliable — the explanation says so.",
  'PEST-11': "Card c gives pralidoxime 1–2 g over 30 min with repeat at 1 hour. The WHO regimen is 30 mg/kg (~2 g) over 30 min then 8 mg/kg/h (~500 mg/h) until atropine is no longer needed; both are given, card first. The card implies oximes work if given in time: the Cochrane review (Buckley, Eddleston et al.) concludes the evidence is insufficient to show benefit or harm, and the placebo-controlled trial of the WHO regimen in Sri Lanka found no clinical benefit with a trend to harm, while a small Indian trial of 1 g/h for 48 h found fewer deaths and fewer ventilator days. The explanation now states this rather than asserting benefit.",
  'PEST-12': "Card b gives activated charcoal 1 g/kg within 1 hour. Single-dose charcoal in organophosphate poisoning has no proven mortality benefit (negative Sri Lankan RCT) and carries aspiration risk in a patient with vomiting and a falling GCS — reasonable but not mandatory. Card c's glycopyrrolate figures (30% vs 90% confusion, 7.5 mg in 200 mL) come from a small single-centre study; kept as the card states.",
  'PEST-12 (FFP)': "Card d calls fresh frozen plasma harmful. The evidence is a single randomised pilot (Pichamuthu et al., Clin Toxicol 2010, Vellore: FFP vs albumin vs saline) in which FFP raised plasma cholinesterase but gave no improvement in deaths (4/19 vs 2/19 saline) or ventilator days (median 10 vs 7.5) — statistically no difference. 'No benefit, do not use' is defensible; 'harmful' overstates it. The explanation says so; if the exam asks for the harmful item on this list, FFP is still the intended answer.",
  'PEST-12 (magnesium)': "Card d says magnesium has 'no scientific data'. This is outdated: there are four randomised trials and several cohorts, pooled OR for mortality 0.55 (95% CI 0.32–0.94) in the systematic review by Brvar et al., Clin Toxicol 2018, with hypotension at the highest dose and the conclusion that evidence is insufficient to recommend it. The explanation states 'unproven rather than undocumented'.",
}
