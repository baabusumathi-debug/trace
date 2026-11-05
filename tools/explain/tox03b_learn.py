# TOX03B — Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Deck: Rodenticides (PEST-14 to PEST-18) and Paraquat (PEST-19 to PEST-23).
# Same fields as tox01_learn.py. Card answers are restated in bold at the start of each part;
# disagreements with a card go in FLAGS, not in the text.
L = {}

L['PEST-14'] = dict(
  sub="Toxicology → Rodenticides → Classification by toxicity",
  intro="A rodenticide has to kill a rat that eats only a small amount of bait, so many of them are poisons of the most basic machinery of the cell. Toxicity in humans depends on two things: how potent the chemical is and how much is in the bait. In India three groups account for most poisonings — yellow phosphorus paste, metal phosphide tablets and the long-acting anticoagulants — and they sit in very different places on this scale.",
  parts=[
    ('a', "**Highly toxic: yellow phosphorus, metal phosphides, strychnine, arsenic, sodium monofluoroacetate.** Each attacks something every cell needs. Yellow phosphorus is a protoplasmic poison that causes fatty degeneration of the liver (PEST-15). Phosphides release phosphine, which blocks cytochrome c oxidase and stops oxidative phosphorylation (PEST-18). Monofluoroacetate is converted in the body to fluorocitrate, which blocks aconitase and halts the citric acid cycle. Strychnine blocks inhibitory glycine receptors in the spinal cord, and arsenic binds the thiol groups of many enzymes. Small amounts are lethal, and there is no specific antidote for most of them."),
    ('b', "**Moderately toxic: alpha-naphthyl thiourea (ANTU), cholecalciferol.** ANTU increases pulmonary capillary permeability, causing pulmonary oedema and pleural effusion; rats are far more sensitive to it than humans. Cholecalciferol (vitamin D₃) acts slowly, by raising calcium absorption and bone resorption, so the danger is hypercalcaemia over days, treated as any other hypercalcaemia."),
    ('c', "**Less toxic: superwarfarins, red squill, bromethalin.** Superwarfarin baits contain very little drug (typically 0.005%), so a single accidental mouthful rarely matters — although a deliberate large ingestion causes weeks of coagulopathy (PEST-17). Red squill contains a cardiac glycoside but is also a strong emetic; rats cannot vomit, humans can, so most of the dose comes back up. Bromethalin uncouples oxidative phosphorylation in nerve cells and causes cerebral oedema, but human poisoning is rare."),
  ],
  table=dict(title="India’s three main rodenticides", head=["Agent", "Form", "Main danger"], rows=[["Yellow phosphorus", "paste (Ratol)", "liver failure on day 3"], ["Metal phosphides", "tablets, powder", "shock within hours"], ["Superwarfarins", "baits, cakes", "delayed bleeding, for weeks"]]),
  mimic=[
    ("Strychnine vs tetanus", "Both give spasms with a clear sensorium. Strychnine starts within minutes to an hour and the muscles relax completely between spasms; tetanus starts days after a wound with rigidity persisting between spasms."),
    ("Yellow phosphorus vs metal phosphide", "Both smell of garlic; phosphorus kills the liver over days, phosphide kills the circulation within hours (PEST-15)."),
  ],
  traps=[
    ("“Superwarfarins are less toxic, so a large ingestion can be sent home”", "‘Less toxic’ refers to the small dose in a bait. A deliberate ingestion of many packets causes coagulopathy that lasts weeks to months."),
    ("“Red squill is dangerous because it is a cardiac glycoside”", "It is, but it makes humans vomit, which limits the dose absorbed; rats cannot vomit, which is why it works on them."),
    ("“Cholecalciferol rodenticide acts within hours”", "Vitamin D acts through calcium absorption and bone resorption, so hypercalcaemia develops over days."),
  ],
  decode=[
    ("Ratol paste ingestion", "Yellow phosphorus — watch the liver on day 3."),
    ("Celphos tablet, shock within hours", "Aluminium phosphide."),
    ("Rat poison cake, bleeding gums a few days later", "Long-acting anticoagulant (superwarfarin)."),
  ],
  punch="The most toxic rodenticides poison what every cell needs — the mitochondria, the citric acid cycle, inhibitory synapses — while the least toxic are either dilute in the bait or make the patient vomit.",
  extra=[dict(q="Strychnine poisoning: the airway trap?", a="Strychnine blocks glycine receptors, giving painful spasms with a clear sensorium. Treat with **benzodiazepines** in a quiet room, then paralysis and ventilation if needed — but **avoid suxamethonium**: rhabdomyolysis brings hyperkalaemia; use a non-depolarising agent.")],
)

L['PEST-15'] = dict(
  sub="Toxicology → Rodenticides → Yellow phosphorus vs metal phosphide",
  intro="Both poisons contain phosphorus and both smell of garlic, but they kill in completely different ways and on different clocks. Yellow phosphorus is absorbed and poisons the liver cell itself, so the patient may look well for a day before liver failure sets in. A metal phosphide releases a gas, phosphine, that switches off cellular respiration everywhere at once, so the heart and circulation fail within hours.",
  parts=[
    ('a', "**Form: yellow phosphorus as a paste (Ratol); metal phosphide as tablets (Celphos) or zinc phosphide powder.** Ratol is a paste spread on bait. A Celphos tablet weighs 3 g and releases about 1 g of phosphine on contact with moisture — far more than a lethal dose."),
    ('b', "**Mechanism: yellow phosphorus is a protoplasmic toxin causing fatty degeneration of liver, kidney and brain; phosphide releases phosphine with acid or water, which blocks mitochondrial oxidative phosphorylation.** Phosphorus disrupts protein synthesis and the export of fat from the hepatocyte, so fat accumulates and the cell dies. Phosphide reacts with water and stomach acid to form phosphine, which inhibits cytochrome c oxidase; without the last step of the respiratory chain cells cannot make ATP, and those with the highest demand — myocardium and vascular smooth muscle — fail first."),
    ('c', "**Course: yellow phosphorus mild on day 1, transaminitis on day 2, liver failure on day 3; phosphide shock and multi-organ failure within 30 minutes.** The delay with phosphorus is the time it takes for liver cells to accumulate fat and die, which is why an early ‘well’ patient must still be admitted. Phosphine acts as soon as it is formed, so collapse is early."),
    ('d', "**Clue: luminescent faeces and garlic odour with yellow phosphorus; garlic odour with phosphide.** Elemental phosphorus glows in the dark as it oxidises in air, so vomit or stool may glow or smoke. The garlic smell comes from phosphorus compounds in both."),
    ('e', "**Death: yellow phosphorus by liver failure; phosphide by circulatory failure.** Phosphine causes myocardial depression, arrhythmias and vasodilatation together, so the shock does not respond well to fluids or vasopressors (PEST-18)."),
    ('f', "**Antidote: none for either.** Treatment is decontamination and support; for yellow phosphorus, liver support up to transplantation (PEST-16)."),
  ],
  table=dict(title="Two clocks", head=["", "Yellow phosphorus", "Metal phosphide"], rows=[["Target", "hepatocyte", "mitochondria everywhere"], ["Time to danger", "**days (day 3)**", "**minutes to hours**"], ["Death from", "liver failure", "circulatory failure"], ["Special clue", "luminescent faeces", "garlic odour only"]]),
  mimic=[
    ("Yellow phosphorus vs paracetamol", "Both look mild at first and cause liver failure around day 3; paracetamol has NAC as an antidote and a treatment nomogram, phosphorus has neither."),
    ("Phosphide shock vs septic shock", "Phosphide shock comes within hours of a tablet, with severe acidosis and myocardial dysfunction, in a patient who was well that morning."),
  ],
  traps=[
    ("“The Ratol patient is well on day 1, so discharge”", "The liver injury is still developing; transaminases rise on day 2 and failure comes on day 3."),
    ("“Luminescent faeces suggest phosphide”", "It is yellow phosphorus — the elemental form glows as it oxidises."),
    ("“Phosphide shock responds to fluids”", "It is largely myocardial and mitochondrial, so it is often refractory."),
  ],
  decode=[
    ("Garlic odour, glowing stool, jaundice on day 3", "Yellow phosphorus."),
    ("Garlic odour, BP 70/40 two hours after a tablet", "Aluminium phosphide."),
    ("Lethal dose of yellow phosphorus", "About 1 mg/kg."),
  ],
  punch="Same element, two clocks: yellow phosphorus slowly poisons the liver cell and kills on day 3, while phosphine shuts down mitochondria everywhere and kills the circulation within hours.",
)

L['PEST-16'] = dict(
  sub="Toxicology → Rodenticides → Yellow phosphorus treatment",
  intro="There is no antidote to yellow phosphorus, so treatment follows the course of the poisoning: limit absorption early, support the failing liver and its clotting factors, and, if the liver does not recover, replace it. Because the patient may look well for a day, the window for decontamination is easily missed.",
  parts=[
    ('a', "**Lavage with potassium permanganate, which oxidises phosphorus; avoid oily or fatty food, which increases absorption.** Permanganate is an oxidising agent that converts elemental phosphorus into less toxic, less absorbable phosphates. Phosphorus dissolves in fat, so a fatty meal or oil carries it across the gut wall."),
    ('b', "**Vitamin K, FFP or prothrombin complex for bleeding, electrolytes, N-acetylcysteine.** The damaged liver cannot make clotting factors, so the INR rises; vitamin K helps only as far as the liver can still use it, and FFP or prothrombin complex replaces the factors directly when the patient bleeds. N-acetylcysteine is used as in other non-paracetamol acute liver failure, to support glutathione and reduce oxidative injury; it is not a specific antidote here."),
    ('c', "**Plasma exchange in liver failure lowered INR and transaminases significantly; bilirubin was unchanged.** Exchange removes toxin and inflammatory mediators and replaces the missing clotting factors with donor plasma, so the INR falls. Bilirubin behaves differently: the failing liver still cannot conjugate and excrete it, and much of it sits in the tissues, so an exchange lowers the plasma level only briefly — a likely reason it did not change. It buys time for the liver to regenerate or for a transplant."),
    ('d', "**Liver transplant as the last resort.** When the liver fails and does not recover — worsening encephalopathy, coagulopathy and acidosis, judged by criteria such as King’s College — transplantation is the only definitive treatment."),
  ],
  mimic=[
    ("Plasma exchange vs liver transplant", "Exchange corrects the INR and buys time; only a transplant replaces the failed liver."),
  ],
  traps=[
    ("“Give vegetable oil to bind the phosphorus”", "Phosphorus dissolves in fat, so oils and fatty food increase absorption."),
    ("“A normal INR after plasma exchange means the liver has recovered”", "Exchange replaces clotting factors temporarily; follow encephalopathy, acidosis and the trend once exchange stops."),
    ("“N-acetylcysteine is the antidote, as in paracetamol”", "There is no antidote; NAC is supportive here."),
  ],
  decode=[
    ("Lavage fluid for yellow phosphorus", "Potassium permanganate."),
    ("Ratol poisoning with rising INR on day 3, bridge to recovery", "Plasma exchange."),
    ("Ratol poisoning with grade III encephalopathy", "Liver transplant."),
  ],
  punch="Without an antidote, yellow phosphorus is treated by its timeline: oxidise and avoid fat early, replace clotting factors as the liver fails, exchange plasma to buy time, and transplant if the liver does not come back.",
)

L['PEST-17'] = dict(
  sub="Toxicology → Rodenticides → Superwarfarins",
  intro="Rats learn to avoid a bait that makes them ill at once, so anticoagulant rodenticides were designed to work slowly. The second-generation ‘superwarfarins’ were made after rats became resistant to warfarin: they bind the same enzyme far more tightly and stay in the liver for weeks. In a human that means a coagulopathy that starts late and lasts long.",
  parts=[
    ('a', "**Brodifacoum, bromadiolone, difenacoum, chlorophacinone.** The first three are 4-hydroxycoumarins like warfarin; chlorophacinone is an indandione, a different chemical class with the same action. All are fat-soluble and concentrate in the liver, which gives them half-lives of weeks."),
    ('b', "**Inhibit vitamin K epoxide reductase, so no active factors II, VII, IX and X are made.** These factors need vitamin K to become functional; once used, vitamin K is turned into its epoxide and must be recycled by this reductase. Block the reductase and the liver keeps releasing factors that cannot work. Proteins C and S are also vitamin K dependent."),
    ('c', "**Bleeding begins at 24–48 hours, once the existing factors fall below 30%.** The drug stops new factors being made but does not destroy those already circulating, so nothing happens until they are used up. Factor VII has the shortest half-life (about 6 hours), so the INR rises first, and bleeding follows once levels fall far enough."),
    ('d', "**Confirmation by 4-hydroxycoumarin level on mass spectrometry.** A long INR with low II, VII, IX and X and a normal fibrinogen fits, but the level confirms the agent and, repeated, shows when it has cleared."),
    ('e', "**Vitamin K1 in high doses for weeks to months; FFP or prothrombin complex for active bleeding.** Large doses of vitamin K1 (phytomenadione) drive an alternative reductase that is not blocked, so some active factor is made despite the poison. The drug lasts weeks, so treatment does too, guided by the INR. Vitamin K takes hours to act, so a bleeding patient also needs the factors replaced directly."),
  ],
  mimic=[
    ("Superwarfarin vs warfarin overdose", "Same mechanism, but warfarin wears off in days; a superwarfarin coagulopathy lasts weeks to months."),
    ("Superwarfarin vs liver failure", "Both raise the INR, but in liver failure fibrinogen and factor V also fall; superwarfarin spares them."),
  ],
  traps=[
    ("“Normal INR on the day of ingestion — safe to discharge”", "The existing factors have not yet run out; repeat the INR at 48 hours."),
    ("“A single dose of vitamin K reverses it”", "The drug outlasts the vitamin K; high doses are needed for weeks to months."),
    ("“Bleeding starts within 6 hours”", "Stored factors must be used up first — 24–48 hours."),
  ],
  decode=[
    ("Unexplained high INR with bleeding, no warfarin prescribed, normal liver", "Superwarfarin ingestion (check the history of rat poison)."),
    ("INR recurs after vitamin K is stopped", "Long-acting anticoagulant still in the liver — restart high-dose vitamin K1."),
    ("Factors II, VII, IX, X low, V and fibrinogen normal", "Vitamin K antagonism."),
  ],
  punch="Superwarfarins stop new clotting factors being made but leave the old ones, so the INR is normal until they run out at 24–48 hours — and because the drug stays in the liver for weeks, so must the vitamin K.",
)

L['PEST-18'] = dict(
  sub="Toxicology → Rodenticides → Aluminium phosphide",
  intro="Aluminium phosphide is sold as a grain fumigant, cheap and freely available in rural North India, and it is one of the commonest suicidal poisons there. Each tablet releases phosphine gas in the moist, acid stomach. Phosphine stops the cell’s final step of energy production, so the organs with the highest energy demand — the heart and blood vessels — fail first.",
  parts=[
    ('a', "**26% of pesticide poisonings in a North Indian series (PGI Chandigarh).** It matters because it is common where grain is stored, and mortality is high."),
    ('b', "**Phosphine, which inhibits cytochrome c oxidase.** This is complex IV, the last enzyme of the respiratory chain. With it blocked, oxygen cannot accept electrons, ATP production collapses and free radicals form. Cells switch to anaerobic metabolism, which is why lactate rises."),
    ('c', "**Vomiting, refractory shock, myocarditis and arrhythmias, severe metabolic acidosis, within minutes to hours.** The shock combines a failing myocardium with vasodilatation, so neither fluids nor vasopressors restore pressure easily. Myocardial injury shows as ST changes, conduction block and arrhythmias. The acidosis is lactic, from cells unable to use oxygen. ARDS can follow."),
    ('d', "**Supportive only; magnesium sulphate is used but unproven.** There is no antidote. Support means early ventilation, careful fluids, vasopressors and inotropes, and correction of acidosis; VA-ECMO has been used to carry the heart through the first 24–48 hours, after which survivors usually recover. Magnesium is given as a membrane stabiliser against arrhythmias, and low magnesium has been reported in some series, but small trials have given conflicting results and no survival benefit has been established."),
  ],
  mimic=[
    ("Aluminium phosphide vs organophosphate", "Both are pesticides with a garlic smell, but the organophosphate patient has cholinergic signs — miosis, bronchorrhoea, bradycardia, fasciculations (TOX-04); the phosphide patient is in shock with severe acidosis but no cholinergic toxidrome."),
    ("Phosphide cardiac shock vs acute MI", "ST changes and troponin rise in both, but phosphide comes with a tablet history, severe acidosis and vasodilatation."),
  ],
  traps=[
    ("“Phosphide has a specific antidote”", "None exists; care is supportive."),
    ("“Magnesium is proven to lower mortality”", "It is widely used, but the small trials conflict and benefit has not been established."),
    ("“Shock is hypovolaemic, so give large volumes of fluid”", "The heart is failing; large volumes worsen pulmonary oedema. Guide fluids by echo and use inotropes."),
  ],
  decode=[
    ("Grain-storage tablet, refractory shock and severe acidosis", "Aluminium phosphide."),
    ("Toxic gas in phosphide poisoning, and its target", "Phosphine; cytochrome c oxidase."),
    ("Management of aluminium phosphide", "Supportive (magnesium used, unproven)."),
  ],
  punch="Phosphine blocks the last step of the respiratory chain, so the heart and vessels fail first and the shock resists treatment — and with no antidote, survival depends on supporting the circulation through the first day.",
)

L['PEST-19'] = dict(
  sub="Toxicology → Paraquat → Basics",
  intro="Paraquat is a contact herbicide that destroys green plant tissue by generating free radicals. It is cheap, widely used and, swallowed, one of the deadliest poisons in agricultural regions of Asia. A small volume of the concentrate is enough to kill, and there is no antidote — which is why so many countries have banned it.",
  parts=[
    ('a', "**Bipyridyl herbicide.** Two linked pyridine rings form a molecule that accepts and gives away electrons easily. That chemistry is the basis of its toxicity (PEST-20). Diquat is the other member of the group."),
    ('b', "**10–20 mL of the 20% concentrate.** That is 2–4 g, or roughly 30–60 mg/kg in a 70 kg adult — inside the moderate-to-fulminant range (PEST-21). A single mouthful can therefore be fatal."),
    ('c', "**Ingestion is dangerous; inhalation and skin contact are not life-threatening.** Spray droplets are too large to reach the alveoli, and intact skin absorbs little. Swallowed paraquat is absorbed from the gut and carried to the lungs and kidneys, where it concentrates."),
    ('d', "**Case fatality up to 70%.** Death comes either quickly, from multi-organ failure after a large dose, or slowly, over weeks, from pulmonary fibrosis after a moderate one."),
  ],
  mimic=[
    ("Paraquat vs diquat", "Both bipyridyls; diquat spares the lung (no active alveolar uptake) and injures the kidney and brain instead."),
    ("Paraquat vs a corrosive", "Both burn the mouth and oesophagus; only paraquat goes on to lung fibrosis."),
  ],
  traps=[
    ("“The patient only swallowed a mouthful, so it is minor”", "10–20 mL of the concentrate is a lethal dose."),
    ("“Farmers who spray paraquat die of lung fibrosis”", "Inhaled droplets do not reach the alveoli; serious poisoning is from ingestion."),
  ],
  decode=[
    ("Weedkiller ingestion, mouth ulcers, then breathlessness at 1–2 weeks", "Paraquat."),
    ("Class of paraquat", "Bipyridyl herbicide."),
  ],
  punch="Paraquat is lethal only when swallowed, but then a single mouthful of the 20% concentrate can kill — and there is nothing to reverse it.",
)

L['PEST-20'] = dict(
  sub="Toxicology → Paraquat → Mechanism",
  intro="Paraquat is not consumed when it does harm. It shuttles electrons from the cell’s reducing machinery to oxygen, again and again, making free radicals every time. The organs it injures most are those that take it up actively and hold it, and in the lung that uptake meets the highest oxygen tension in the body.",
  parts=[
    ('a', "**Redox cycling generates reactive oxygen species, with mitochondrial failure.** NADPH-dependent enzymes reduce the paraquat ion to a radical; the radical gives its electron to oxygen, forming superoxide, and paraquat returns to its original state ready to go again. Each cycle makes more superoxide, hydrogen peroxide and hydroxyl radicals, damaging lipid membranes, and drains the cell’s NADPH, so its antioxidant defences fail."),
    ('b', "**Active uptake by alveolar cells through the polyamine uptake system, causing alveolitis and then pulmonary fibrosis.** Paraquat resembles the natural polyamines, so type I and type II alveolar cells pump it in and concentrate it, even when plasma levels are falling. There it meets plenty of oxygen, so the redox cycle runs fastest. The acute destruction is alveolitis; the repair response that follows is fibrosis, which develops over one to three weeks."),
    ('c', "**Accumulation in proximal tubular cells, causing tubular necrosis.** Paraquat is cleared almost entirely by the kidneys and is actively secreted by the proximal tubule, so these cells concentrate it. As the kidney fails, clearance falls and more paraquat is left to reach the lung."),
    ('d', "**Oxygen is the substrate for free-radical formation.** Every turn of the cycle needs a molecule of oxygen, so extra oxygen accelerates the very injury that is destroying the lung."),
  ],
  mimic=[
    ("Paraquat lung vs oxygen toxicity", "Both are free-radical injuries; paraquat makes the alveoli far more vulnerable to oxygen, which is why supplemental oxygen is withheld."),
  ],
  traps=[
    ("“Give high-flow oxygen as in every poisoning”", "Oxygen feeds the redox cycle; give it only when the patient is hypoxic."),
    ("“The lung is injured because paraquat is inhaled”", "It is swallowed and actively taken up by alveolar cells from the blood."),
    ("“Renal failure is a side-issue”", "The kidney is the only route of elimination; when it fails, more paraquat reaches the lung."),
  ],
  decode=[
    ("Why is oxygen withheld in paraquat poisoning?", "Oxygen is the substrate for the redox cycle that forms free radicals."),
    ("Transport system concentrating paraquat in the lung", "The polyamine uptake system of alveolar cells."),
  ],
  punch="Paraquat recycles itself, handing electrons to oxygen to make free radicals; the lung pumps it in and is full of oxygen, so the lung fibroses — and giving more oxygen only feeds the cycle.",
)

L['PEST-21'] = dict(
  sub="Toxicology → Paraquat → Severity by dose",
  intro="Because the redox cycle runs as long as paraquat is present, the outcome is set mainly by how much was swallowed. Grading by dose per kilogram predicts not just whether the patient dies but how: quickly from multi-organ failure, or weeks later from the lung.",
  parts=[
    ('a', "**Mild: below 20 mg/kg — GI symptoms only, full recovery.** That is under about 7 mL of the 20% concentrate in an adult. The local caustic effect gives vomiting, diarrhoea and perhaps mouth ulcers, but too little reaches the lung to start fibrosis."),
    ('b', "**Moderate to severe: 20–40 mg/kg — renal and hepatic failure, then pulmonary fibrosis; death in 2–3 weeks.** The kidney and liver are injured in the first days. Enough paraquat reaches the lung to start progressive fibrosis, so the patient may seem to improve and then become steadily more hypoxic. Survivors are few."),
    ('c', "**Fulminant: above 40 mg/kg — multi-organ failure and shock; death in 1–4 days.** About 15 mL or more of the concentrate. The dose is so large that the heart, liver, kidneys and adrenal glands fail together, and the patient dies before fibrosis has time to develop."),
  ],
  table=dict(title="Dose decides how death comes", head=["Grade", "mg/kg", "Approx. 20% concentrate (adult)", "Outcome"], rows=[["Mild", "<20", "<7 mL", "recovery"], ["Moderate to severe", "20–40", "7–15 mL", "**fibrosis, death in 2–3 weeks**"], ["Fulminant", ">40", ">15 mL", "**shock, death in 1–4 days**"]]),
  mimic=[
    ("Moderate vs fulminant death", "Moderate dies of the lung over weeks; fulminant dies of the circulation within days."),
  ],
  traps=[
    ("“Early recovery from the GI phase means survival”", "In the 20–40 mg/kg group, fibrosis progresses over the following weeks."),
    ("“Fulminant paraquat poisoning ends in fibrosis”", "Those patients die of multi-organ failure before fibrosis develops."),
  ],
  decode=[
    ("Paraquat 30 mg/kg, improving on day 3", "Moderate–severe: expect progressive fibrosis, death in 2–3 weeks."),
    ("Paraquat >40 mg/kg", "Fulminant: multi-organ failure, death in 1–4 days."),
  ],
  punch="Paraquat severity follows the dose: under 20 mg/kg the gut recovers, 20–40 mg/kg the lung fibroses over weeks, and above 40 mg/kg the whole body fails in days.",
)

L['PEST-22'] = dict(
  sub="Toxicology → Paraquat → Diagnosis and prognosis",
  intro="With no antidote, the useful questions in paraquat poisoning are ‘was it paraquat?’ and ‘will this patient survive?’. A simple bedside test answers the first. The second is answered by how much paraquat is still in the plasma and how long after ingestion that level was taken, because the level falls quickly as the drug moves into the tissues and urine.",
  parts=[
    ('a', "**Sodium dithionite in alkali added to urine gives a blue colour; best within 6 hours.** Dithionite reduces paraquat to its blue radical — the same reduction that drives its toxicity. Most paraquat is excreted in the first hours, so a late sample can be falsely negative; the depth of colour gives a rough guide to the amount."),
    ('b', "**Severity Index of Paraquat Poisoning (SIPP) = plasma level (mg/L) × hours since ingestion; below 10, survival is likely.** A given level means more the later it is taken, because the plasma level should be falling. Multiplying by time corrects for this. Higher values predict death — first from lung fibrosis, and at very high values from circulatory failure."),
    ('c', "**Other poor signs: lactate above 4, renal failure, ARDS.** A raised lactate means cellular respiration is already failing. Renal failure shuts off the only route of elimination, and early ARDS signals a large lung dose."),
  ],
  mimic=[
    ("Paraquat vs diquat in the dithionite test", "Paraquat turns blue; diquat gives green."),
    ("SIPP vs Proudfoot curve", "Both use plasma level and time since ingestion; SIPP turns them into one number, Proudfoot plots them against a survival line."),
  ],
  traps=[
    ("“A negative urine test the next day excludes paraquat”", "Most is excreted early; test within about 6 hours."),
    ("“A plasma level alone predicts outcome”", "It must be read against the time since ingestion."),
  ],
  decode=[
    ("Urine turns blue with sodium dithionite", "Paraquat."),
    ("Plasma level × hours since ingestion", "SIPP; below 10, survival likely."),
    ("Paraquat with lactate 6 and rising creatinine", "Poor prognosis."),
  ],
  punch="Dithionite turns paraquat blue by the same reduction that makes it toxic, and prognosis comes from the plasma level read against time since ingestion — the SIPP — because a level that should have fallen but has not means death.",
  extra=[dict(q="Proudfoot curve: which levels mark 50% survival?", a="About **2.0 mg/L at 4 h, 0.6 at 6 h, 0.3 at 10 h, 0.16 at 16 h and 0.1 at 24 h**; levels above the line predict death.")],
)

L['PEST-23'] = dict(
  sub="Toxicology → Paraquat → Treatment and revision",
  intro="Paraquat moves from the plasma into the lung and kidney within hours, and once there no treatment pulls it out. So treatment is mostly about binding what remains in the gut, keeping the kidneys excreting, and not making things worse with oxygen. Many experimental treatments have been tried; none has clearly changed survival.",
  parts=[
    ('a', "**Avoid oxygen unless hypoxic; hydration; no forced emesis (caustic); wash skin and eyes; Fuller’s earth or activated charcoal early.** Oxygen feeds the redox cycle (PEST-20). Fluids keep urine flowing, because the kidney is the only route of elimination. Forcing emesis brings the corrosive back over the oesophagus and risks aspiration. Fuller’s earth (a clay) and charcoal bind paraquat in the gut, but only before it has been absorbed, which happens within hours."),
    ('b', "**Experimental: immunosuppression (dexamethasone, cyclophosphamide), N-acetylcysteine, vitamins C and E, edaravone — none proven.** Immunosuppression aims to damp the alveolitis that leads to fibrosis; the antioxidants and the free-radical scavenger edaravone aim to mop up the radicals. Early small trials of steroid plus cyclophosphamide looked promising, but the largest trial (299 patients in Sri Lanka, 2018) found no significant survival benefit, and the 2021 Cochrane review rates the evidence as low certainty, with at most a small in-hospital effect and no difference at three months. None of the antioxidants has trial evidence of benefit."),
    ('c', "**Haemofiltration: a meta-analysis of 3 trials showed no reduction in mortality (risk ratio 0.94).** The meta-analysis (2017: three randomised trials, 290 patients, continuous venovenous haemofiltration added to standard care) found mortality of about 58% versus 61%. Extracorporeal removal can only take paraquat out of the plasma; within hours most of it has already moved into the lung and kidney, where it is beyond reach. Haemofiltration did prolong survival, and fewer patients died of circulatory failure but more of respiratory failure — it delays death from the plasma load without stopping the lung injury already under way."),
    ('d', "**False — luminescent faeces suggest yellow phosphorus.** Elemental phosphorus glows as it oxidises (PEST-15); phosphides release a gas."),
    ('e', "**False — superwarfarin bleeding starts at 24–48 hours.** The circulating factors must be used up first (PEST-17)."),
  ],
  mimic=[
    ("Oxygen in paraquat vs in carbon monoxide", "In CO, 100% oxygen is the treatment (TOX-13); in paraquat it feeds the injury."),
  ],
  traps=[
    ("“Give high-flow oxygen to every poisoned patient”", "In paraquat, only for hypoxia."),
    ("“Haemoperfusion or haemofiltration removes paraquat from the lung”", "Only plasma paraquat is removed; tissue uptake happens within hours."),
    ("“Induce vomiting to empty the stomach”", "Paraquat is caustic; use an adsorbent instead."),
  ],
  decode=[
    ("Best early step in paraquat ingestion", "Fuller’s earth or activated charcoal, fluids, no oxygen unless hypoxic."),
    ("Proven therapy for paraquat lung", "None."),
    ("Large ingestion, high SIPP", "Outcome is clear by 24–48 hours; early palliative care is appropriate."),
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
