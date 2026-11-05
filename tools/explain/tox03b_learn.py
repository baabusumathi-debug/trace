# TOX03B — Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Deck: Rodenticides (PEST-14 to PEST-18) and Paraquat (PEST-19 to PEST-23).
# Same fields as tox01_learn.py. Card answers are restated in bold at the start of each part;
# disagreements with a card go in FLAGS, not in the text.
# Audited 6 Nov: no linked real questions — tightened to essentials, decode [pattern].
L = {}

L['PEST-14'] = dict(
  sub="Toxicology → Rodenticides → Classification by toxicity",
  intro="A rodenticide has to kill a rat that eats only a little bait, so many are poisons of the cell’s basic machinery. Human toxicity depends on how potent the chemical is and how much is in the bait. In India three groups dominate — yellow phosphorus paste, metal phosphide tablets and the long-acting anticoagulants — and they sit in very different places on this scale.",
  parts=[
    ('a', "**Highly toxic: yellow phosphorus, metal phosphides, strychnine, arsenic, sodium monofluoroacetate.** Each attacks something every cell needs: yellow phosphorus causes fatty degeneration of the liver (PEST-15); phosphine blocks cytochrome c oxidase (PEST-18); monofluoroacetate becomes fluorocitrate and blocks aconitase in the citric acid cycle; strychnine blocks inhibitory glycine receptors; arsenic binds enzyme thiol groups. Small amounts kill, and most have no antidote."),
    ('b', "**Moderately toxic: alpha-naphthyl thiourea (ANTU), cholecalciferol.** ANTU raises pulmonary capillary permeability, causing pulmonary oedema and effusion. Cholecalciferol causes hypercalcaemia over days."),
    ('c', "**Less toxic: superwarfarins, red squill, bromethalin.** Superwarfarin baits contain very little drug, so an accidental mouthful rarely matters — a deliberate large ingestion still causes weeks of coagulopathy (PEST-17). Red squill is a cardiac glycoside but a strong emetic, and humans, unlike rats, vomit it up."),
  ],
  table=dict(title="India’s three main rodenticides", head=["Agent", "Form", "Main danger"], rows=[["Yellow phosphorus", "paste (Ratol)", "liver failure on day 3"], ["Metal phosphides", "tablets, powder", "shock within hours"], ["Superwarfarins", "baits, cakes", "delayed bleeding, for weeks"]]),
  mimic=[
    ("Strychnine vs tetanus", "Both give spasms with a clear sensorium; strychnine starts within an hour and muscles relax fully between spasms, tetanus starts days after a wound with persisting rigidity."),
  ],
  traps=[
    ("“Superwarfarins are less toxic, so a large ingestion can be sent home”", "‘Less toxic’ refers to the dilute bait; many packets cause coagulopathy for weeks to months."),
  ],
  decode=[
    ("Ratol paste vs Celphos tablet vs rat-poison cake [pattern]", "Yellow phosphorus (liver, day 3); aluminium phosphide (shock, hours); superwarfarin (bleeding, days)."),
  ],
  punch="The most toxic rodenticides poison what every cell needs — the mitochondria, the citric acid cycle, inhibitory synapses — while the least toxic are either dilute in the bait or make the patient vomit.",
)

L['PEST-15'] = dict(
  sub="Toxicology → Rodenticides → Yellow phosphorus vs metal phosphide",
  intro="Both poisons contain phosphorus and both smell of garlic, but they kill on different clocks. Yellow phosphorus poisons the liver cell itself, so the patient may look well for a day before liver failure. A metal phosphide releases phosphine, which switches off cellular respiration everywhere, so the circulation fails within hours.",
  parts=[
    ('a', "**Form: yellow phosphorus as a paste (Ratol); metal phosphide as tablets (Celphos) or zinc phosphide powder.** A 3 g Celphos tablet releases about 1 g of phosphine on contact with moisture — far more than a lethal dose."),
    ('b', "**Mechanism: yellow phosphorus is a protoplasmic toxin causing fatty degeneration of liver, kidney and brain; phosphide releases phosphine with acid or water, which blocks mitochondrial oxidative phosphorylation.** Phosphorus stops the hepatocyte exporting fat, so it accumulates and the cell dies. Phosphine inhibits cytochrome c oxidase, so cells with the highest demand — myocardium and vascular smooth muscle — fail first."),
    ('c', "**Course: yellow phosphorus mild on day 1, transaminitis on day 2, liver failure on day 3; phosphide shock and multi-organ failure within 30 minutes.** The phosphorus delay is the time liver cells take to die, so an early ‘well’ patient must be admitted; phosphine acts as soon as it forms."),
    ('d', "**Clue: luminescent faeces and garlic odour with yellow phosphorus; garlic odour with phosphide.** Elemental phosphorus glows as it oxidises in air."),
    ('e', "**Death: yellow phosphorus by liver failure; phosphide by circulatory failure.** Phosphine causes myocardial depression, arrhythmias and vasodilatation together, so the shock is refractory (PEST-18)."),
    ('f', "**Antidote: none for either.** Decontamination and support; for yellow phosphorus, liver support up to transplantation (PEST-16)."),
  ],
  table=dict(title="Two clocks", head=["", "Yellow phosphorus", "Metal phosphide"], rows=[["Target", "hepatocyte", "mitochondria everywhere"], ["Time to danger", "**days (day 3)**", "**minutes to hours**"], ["Death from", "liver failure", "circulatory failure"], ["Special clue", "luminescent faeces", "garlic odour only"]]),
  mimic=[
    ("Yellow phosphorus vs paracetamol", "Both look mild at first and fail the liver around day 3; paracetamol has NAC and a nomogram, phosphorus has neither."),
  ],
  traps=[
    ("“The Ratol patient is well on day 1, so discharge”", "Transaminases rise on day 2 and failure comes on day 3."),
    ("“Luminescent faeces suggest phosphide”", "It is yellow phosphorus — the elemental form glows."),
  ],
  decode=[
    ("Garlic odour, glowing stool, jaundice on day 3 [pattern]", "Yellow phosphorus."),
    ("Garlic odour, BP 70/40 two hours after a tablet [pattern]", "Aluminium phosphide."),
  ],
  punch="Same element, two clocks: yellow phosphorus slowly poisons the liver cell and kills on day 3, while phosphine shuts down mitochondria everywhere and kills the circulation within hours.",
)

L['PEST-16'] = dict(
  sub="Toxicology → Rodenticides → Yellow phosphorus treatment",
  intro="There is no antidote to yellow phosphorus, so treatment follows the course: limit absorption early, support the failing liver and its clotting factors, and replace the liver if it does not recover.",
  parts=[
    ('a', "**Lavage with potassium permanganate, which oxidises phosphorus; avoid oily or fatty food, which increases absorption.** Permanganate converts elemental phosphorus to less absorbable phosphates; phosphorus dissolves in fat, so oil carries it across the gut wall."),
    ('b', "**Vitamin K, FFP or prothrombin complex for bleeding, electrolytes, N-acetylcysteine.** The damaged liver cannot make clotting factors, so they are replaced when the patient bleeds. NAC is supportive, as in other non-paracetamol liver failure — not an antidote."),
    ('c', "**Plasma exchange in liver failure lowered INR and transaminases significantly; bilirubin was unchanged.** Exchange removes toxin and replaces clotting factors with donor plasma, so the INR falls; much bilirubin sits in the tissues, so it barely moves. It buys time for regeneration or transplant."),
    ('d', "**Liver transplant as the last resort.** When the liver fails and does not recover, transplant is the only definitive treatment."),
  ],
  mimic=[],
  traps=[
    ("“Give vegetable oil to bind the phosphorus”", "Phosphorus dissolves in fat, so oils and fatty food increase absorption."),
  ],
  decode=[
    ("Lavage fluid for yellow phosphorus [pattern]", "Potassium permanganate."),
    ("Ratol poisoning, rising INR on day 3: bridge to recovery [pattern]", "Plasma exchange."),
  ],
  punch="Without an antidote, yellow phosphorus is treated by its timeline: oxidise and avoid fat early, replace clotting factors as the liver fails, exchange plasma to buy time, and transplant if the liver does not come back.",
)

L['PEST-17'] = dict(
  sub="Toxicology → Rodenticides → Superwarfarins",
  intro="The second-generation ‘superwarfarins’ were made after rats became resistant to warfarin: they bind the same enzyme far more tightly and stay in the liver for weeks. In a human that means a coagulopathy that starts late and lasts long.",
  parts=[
    ('a', "**Brodifacoum, bromadiolone, difenacoum, chlorophacinone.** All are fat-soluble and concentrate in the liver, giving half-lives of weeks."),
    ('b', "**Inhibit vitamin K epoxide reductase, so no active factors II, VII, IX and X are made.** Vitamin K must be recycled by this reductase after each use; blocked, the liver releases factors that cannot work."),
    ('c', "**Bleeding begins at 24–48 hours, once the existing factors fall below 30%.** The drug stops new factors being made but leaves circulating ones, so nothing happens until they run out; factor VII goes first, so the INR rises first."),
    ('d', "**Confirmation by 4-hydroxycoumarin level on mass spectrometry.** The level confirms the agent and, repeated, shows when it has cleared."),
    ('e', "**Vitamin K1 in high doses for weeks to months; FFP or prothrombin complex for active bleeding.** High-dose vitamin K1 uses an alternative pathway the poison does not block; the drug lasts weeks, so treatment does too, guided by the INR. Vitamin K takes hours, so a bleeding patient also needs factors replaced."),
  ],
  mimic=[
    ("Superwarfarin vs warfarin overdose vs liver failure", "Warfarin wears off in days, a superwarfarin lasts weeks to months; liver failure also lowers factor V and fibrinogen, which vitamin K antagonism spares."),
  ],
  traps=[
    ("“Normal INR on the day of ingestion — safe to discharge”", "The existing factors have not yet run out; repeat the INR at 48 hours."),
    ("“A single dose of vitamin K reverses it”", "High doses are needed for weeks to months."),
  ],
  decode=[
    ("Unexplained high INR with bleeding, no warfarin, normal liver; INR recurs when vitamin K stops [pattern]", "Superwarfarin ingestion — high-dose vitamin K1 for weeks."),
  ],
  punch="Superwarfarins stop new clotting factors being made but leave the old ones, so the INR is normal until they run out at 24–48 hours — and because the drug stays in the liver for weeks, so must the vitamin K.",
)

L['PEST-18'] = dict(
  sub="Toxicology → Rodenticides → Aluminium phosphide",
  intro="Aluminium phosphide is a cheap grain fumigant, freely available in rural North India and one of the commonest suicidal poisons there. Each tablet releases phosphine in the moist, acid stomach. Phosphine stops the last step of energy production, so the heart and vessels fail first.",
  parts=[
    ('a', "**26% of pesticide poisonings in a North Indian series (PGI Chandigarh).** Common where grain is stored, with high mortality."),
    ('b', "**Phosphine, which inhibits cytochrome c oxidase.** Complex IV, the last enzyme of the respiratory chain: ATP production collapses, free radicals form and lactate rises."),
    ('c', "**Vomiting, refractory shock, myocarditis and arrhythmias, severe metabolic acidosis, within minutes to hours.** The shock combines a failing myocardium with vasodilatation, so fluids and vasopressors work poorly; the acidosis is lactic."),
    ('d', "**Supportive only; magnesium sulphate is used but unproven.** No antidote: early ventilation, careful fluids, vasopressors and inotropes; VA-ECMO can carry the heart through the first 24–48 hours. Magnesium trials conflict."),
  ],
  mimic=[
    ("Aluminium phosphide vs organophosphate", "Both are garlic-smelling pesticides; the organophosphate patient has a cholinergic toxidrome, the phosphide patient shock and acidosis without one."),
  ],
  traps=[
    ("“Shock is hypovolaemic, so give large volumes of fluid”", "The heart is failing; large volumes worsen pulmonary oedema. Guide fluids by echo and use inotropes."),
  ],
  decode=[
    ("Grain-storage tablet, refractory shock, severe acidosis: agent, toxin, target [pattern]", "Aluminium phosphide; phosphine; cytochrome c oxidase — supportive care."),
  ],
  punch="Phosphine blocks the last step of the respiratory chain, so the heart and vessels fail first and the shock resists treatment — and with no antidote, survival depends on supporting the circulation through the first day.",
)

L['PEST-19'] = dict(
  sub="Toxicology → Paraquat → Basics",
  intro="Paraquat is a contact herbicide that destroys plant tissue by generating free radicals. Swallowed, it is one of the deadliest poisons in agricultural Asia: a small volume of concentrate kills, and there is no antidote.",
  parts=[
    ('a', "**Bipyridyl herbicide.** Two linked pyridine rings accept and give away electrons easily — the basis of its toxicity (PEST-20). Diquat is the other member."),
    ('b', "**10–20 mL of the 20% concentrate.** That is 2–4 g, about 30–60 mg/kg in an adult (PEST-21): a single mouthful can be fatal."),
    ('c', "**Ingestion is dangerous; inhalation and skin contact are not life-threatening.** Spray droplets are too large to reach the alveoli and intact skin absorbs little."),
    ('d', "**Case fatality up to 70%.** Death is quick from multi-organ failure after a large dose, or slow from pulmonary fibrosis after a moderate one."),
  ],
  mimic=[
    ("Paraquat vs diquat", "Diquat spares the lung (no active alveolar uptake) and injures kidney and brain instead."),
  ],
  traps=[
    ("“The patient only swallowed a mouthful, so it is minor”", "10–20 mL of the concentrate is a lethal dose."),
  ],
  decode=[
    ("Weedkiller ingestion, mouth ulcers, breathlessness at 1–2 weeks [pattern]", "Paraquat."),
  ],
  punch="Paraquat is lethal only when swallowed, but then a single mouthful of the 20% concentrate can kill — and there is nothing to reverse it.",
)

L['PEST-20'] = dict(
  sub="Toxicology → Paraquat → Mechanism",
  intro="Paraquat is not consumed when it does harm: it shuttles electrons to oxygen again and again, making free radicals every time. The organs it injures most are those that take it up actively, and in the lung that uptake meets the highest oxygen tension in the body.",
  parts=[
    ('a', "**Redox cycling generates reactive oxygen species, with mitochondrial failure.** NADPH-dependent enzymes reduce paraquat to a radical, which hands its electron to oxygen as superoxide and returns ready to cycle again — damaging membranes and draining NADPH."),
    ('b', "**Active uptake by alveolar cells through the polyamine uptake system, causing alveolitis and then pulmonary fibrosis.** Paraquat resembles natural polyamines, so alveolar cells pump it in and concentrate it; with abundant oxygen the cycle runs fastest. Alveolitis comes first, fibrosis over one to three weeks."),
    ('c', "**Accumulation in proximal tubular cells, causing tubular necrosis.** The kidney is the only route of elimination; as it fails, more paraquat reaches the lung."),
    ('d', "**Oxygen is the substrate for free-radical formation.** Extra oxygen accelerates the injury, so it is withheld unless the patient is hypoxic."),
  ],
  mimic=[],
  traps=[
    ("“Give high-flow oxygen as in every poisoning”", "Oxygen feeds the redox cycle; give it only for hypoxia."),
  ],
  decode=[
    ("Why is oxygen withheld in paraquat poisoning? [pattern]", "Oxygen is the substrate for the redox cycle that forms free radicals."),
    ("Transport concentrating paraquat in the lung [pattern]", "The polyamine uptake system of alveolar cells."),
  ],
  punch="Paraquat recycles itself, handing electrons to oxygen to make free radicals; the lung pumps it in and is full of oxygen, so the lung fibroses — and giving more oxygen only feeds the cycle.",
)

L['PEST-21'] = dict(
  sub="Toxicology → Paraquat → Severity by dose",
  intro="Because the redox cycle runs as long as paraquat is present, outcome is set mainly by the dose swallowed — which predicts not just whether the patient dies but how.",
  parts=[
    ('a', "**Mild: below 20 mg/kg — GI symptoms only, full recovery.** Under about 7 mL of the concentrate; too little reaches the lung to start fibrosis."),
    ('b', "**Moderate to severe: 20–40 mg/kg — renal and hepatic failure, then pulmonary fibrosis; death in 2–3 weeks.** The patient may seem to improve, then becomes steadily more hypoxic as the lung fibroses."),
    ('c', "**Fulminant: above 40 mg/kg — multi-organ failure and shock; death in 1–4 days.** Heart, liver, kidneys and adrenals fail together, before fibrosis has time to develop."),
  ],
  table=dict(title="Dose decides how death comes", head=["Grade", "mg/kg", "Approx. 20% concentrate (adult)", "Outcome"], rows=[["Mild", "<20", "<7 mL", "recovery"], ["Moderate to severe", "20–40", "7–15 mL", "**fibrosis, death in 2–3 weeks**"], ["Fulminant", ">40", ">15 mL", "**shock, death in 1–4 days**"]]),
  mimic=[],
  traps=[
    ("“Early recovery from the GI phase means survival”", "In the 20–40 mg/kg group, fibrosis progresses over the following weeks."),
  ],
  decode=[
    ("Paraquat 30 mg/kg, improving on day 3 [pattern]", "Moderate–severe: expect progressive fibrosis, death in 2–3 weeks."),
  ],
  punch="Paraquat severity follows the dose: under 20 mg/kg the gut recovers, 20–40 mg/kg the lung fibroses over weeks, and above 40 mg/kg the whole body fails in days.",
)

L['PEST-22'] = dict(
  sub="Toxicology → Paraquat → Diagnosis and prognosis",
  intro="With no antidote, the useful questions are ‘was it paraquat?’ and ‘will this patient survive?’. A bedside urine test answers the first; the plasma level read against time since ingestion answers the second.",
  parts=[
    ('a', "**Sodium dithionite in alkali added to urine gives a blue colour; best within 6 hours.** Dithionite reduces paraquat to its blue radical; most is excreted early, so a late sample can be falsely negative."),
    ('b', "**Severity Index of Paraquat Poisoning (SIPP) = plasma level (mg/L) × hours since ingestion; below 10, survival is likely.** A given level means more the later it is taken, because it should be falling; multiplying by time corrects for this."),
    ('c', "**Other poor signs: lactate above 4, renal failure, ARDS.** Lactate means cellular respiration is failing; renal failure shuts the only exit; early ARDS signals a large lung dose."),
  ],
  mimic=[
    ("Paraquat vs diquat in the dithionite test", "Paraquat turns blue; diquat gives green."),
  ],
  traps=[
    ("“A plasma level alone predicts outcome”", "It must be read against the time since ingestion."),
  ],
  decode=[
    ("Urine turns blue with sodium dithionite [pattern]", "Paraquat."),
    ("Plasma level × hours since ingestion [pattern]", "SIPP; below 10, survival likely."),
  ],
  punch="Dithionite turns paraquat blue by the same reduction that makes it toxic, and prognosis comes from the plasma level read against time — because a level that should have fallen but has not means death.",
)

L['PEST-23'] = dict(
  sub="Toxicology → Paraquat → Treatment and revision",
  intro="Paraquat moves from plasma into lung and kidney within hours, and once there no treatment pulls it out. So treatment is binding what remains in the gut, keeping the kidneys excreting, and not feeding the injury with oxygen.",
  parts=[
    ('a', "**Avoid oxygen unless hypoxic; hydration; no forced emesis (caustic); wash skin and eyes; Fuller’s earth or activated charcoal early.** Oxygen feeds the redox cycle (PEST-20); fluids keep the only exit open; emesis brings the corrosive back over the oesophagus; adsorbents work only before absorption."),
    ('b', "**Experimental: immunosuppression (dexamethasone, cyclophosphamide), N-acetylcysteine, vitamins C and E, edaravone — none proven.** Immunosuppression aims at the alveolitis, the antioxidants at the radicals; the largest steroid–cyclophosphamide trial showed no significant survival benefit."),
    ('c', "**Haemofiltration: a meta-analysis of 3 trials showed no reduction in mortality (risk ratio 0.94).** It removes only plasma paraquat; within hours most has moved into the lung and kidney, beyond reach."),
    ('d', "**False — luminescent faeces suggest yellow phosphorus.** Elemental phosphorus glows as it oxidises (PEST-15)."),
    ('e', "**False — superwarfarin bleeding starts at 24–48 hours.** The circulating factors must be used up first (PEST-17)."),
  ],
  mimic=[
    ("Oxygen in paraquat vs in carbon monoxide", "In CO, 100% oxygen is the treatment (TOX-13); in paraquat it feeds the injury."),
  ],
  traps=[
    ("“Haemoperfusion or haemofiltration removes paraquat from the lung”", "Only plasma paraquat is removed; tissue uptake happens within hours."),
  ],
  decode=[
    ("Best early step in paraquat ingestion [pattern]", "Fuller’s earth or activated charcoal, fluids, no oxygen unless hypoxic."),
  ],
  punch="Paraquat leaves the plasma for the lung within hours and cannot be pulled back, so care is early binding, fluids and withholding oxygen — and when the dose is lethal, honest palliative care.",
)

FLAGS = {
  'PEST-14': "Bromethalin is placed in ‘less toxic’; groupings vary by source and some put it with the moderately or highly toxic agents (it is a potent CNS mitochondrial uncoupler). Thallium and barium carbonate are often listed as highly toxic and are absent. Card kept.",
  'PEST-15': "‘Shock and multi-organ failure within 30 minutes’ is compressed: symptoms (vomiting) start within minutes, but shock usually develops over 1–6 hours and most deaths occur within 24 hours. Yellow-phosphorus staging is also classically given as stage 1 (GI, first 24 h), latent stage (24–72 h), hepatic/renal failure after 72 h. Card kept.",
  'PEST-16': "Watch note re ‘vegetable oil lavage’: older forensic texts used liquid paraffin (a non-absorbed mineral oil) to hold phosphorus in the gut, distinct from digestible fats, which increase absorption — the notes may be a garbled version of this. Also, gastric lavage of any kind is not routine in current toxicology guidance. Card kept.",
  'PEST-17': "Chlorophacinone is an indandione, not a 4-hydroxycoumarin, so part d’s ‘4-hydroxycoumarin level’ does not strictly cover it. Also, coagulopathy (INR rise) appears at 24–48 h; clinical bleeding may appear later (days). The ‘below 30%’ threshold could not be verified against a standard reference. Card kept.",
  'PEST-18': "The 26% PGI figure could not be verified independently; kept as the card states. Part d ‘supportive only’ is correct; note that magnesium trials conflict (some small Indian trials reported benefit, others none), so ‘unproven’ is fair.",
  'PEST-19': "Skin contact is ‘not life-threatening’ for intact skin and diluted spray, but fatal systemic poisoning has been reported after prolonged contact with concentrate on damaged skin. Card kept.",
}
