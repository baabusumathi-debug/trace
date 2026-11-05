# TOX01 top-up cards — Explain v2 ("Learn" depth), same fields and voice as tox01_learn.py.
# Fields: sub, intro, parts [(letter, text)], optional table, mimic, traps, decode, punch.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
T = {}

T['TX1-QT'] = dict(
  sub="Toxicology → Cardiac toxicity → Drug-induced long QT",
  intro="Many common ICU drugs block the cardiac potassium channel (hERG) that ends the action potential. Repolarisation is delayed, the QT lengthens, and an early afterdepolarisation can set off torsades de pointes. The risk is cumulative: each extra drug, a low potassium or magnesium, bradycardia or a raised drug level adds to it.",
  parts=[
    ('a', "**Citalopram and escitalopram.** Among the SSRIs these two prolong the QT in a dose-dependent way, which is why their maximum doses were lowered, especially in the elderly. Sertraline is the usual choice when cardiac risk is a concern."),
    ('b', "**Thioridazine and ziprasidone; IV haloperidol is dangerous at high doses.** Thioridazine has the strongest hERG block of the antipsychotics. Haloperidol by mouth carries modest risk, but large intravenous doses for agitated delirium have caused torsades, so the ECG is monitored when it is given that way."),
    ('c', "**The one that also blocks CYP3A4 (erythromycin, fluconazole) — it raises the others’ levels.** Such a drug prolongs the QT itself and also slows the clearance of other QT drugs metabolised by CYP3A4, so their levels and effect climb. Removing it removes two sources of risk at once."),
    ('d', "**Potassium and magnesium.** Low potassium reduces the repolarising current and enhances hERG block; low magnesium makes afterdepolarisations more likely. Correcting both raises the threshold for torsades, and intravenous magnesium is also the first treatment once torsades occurs."),
  ],
  mimic=[
    ("Torsades vs polymorphic VT from ischaemia", "Torsades arises from a long QT, often pause-dependent; ischaemic polymorphic VT occurs with a normal QT and is treated as ischaemia."),
  ],
  traps=[
    ("“All SSRIs carry the same QT risk”", "Citalopram and escitalopram stand out; sertraline is preferred in cardiac patients."),
    ("“Oral and IV haloperidol are equally risky”", "The danger is mainly with high intravenous doses."),
    ("“Correcting potassium is enough”", "Magnesium must be corrected too; it stabilises the membrane against afterdepolarisations."),
  ],
  decode=[
    ("Patient on a QT drug starts erythromycin or fluconazole, then torsades", "The CYP3A4 inhibitor raised the other drug’s level — stop it first."),
    ("Delirious patient, large IV haloperidol doses, then polymorphic VT", "Drug-induced torsades: stop haloperidol, give magnesium."),
    ("Which SSRI prolongs QT?", "Citalopram (escitalopram)."),
  ],
  punch="QT risk adds up, so remove the drug that multiplies the others first, then correct potassium and magnesium.",
)

T['TX1-SAT'] = dict(
  sub="Toxicology → Gases and haemoglobin → Carbon monoxide vs methaemoglobin",
  intro="A pulse oximeter estimates saturation from the ratio of light absorbed at two wavelengths, 660 and 940 nm, and assumes only oxyhaemoglobin and deoxyhaemoglobin are present. Carbon monoxide and methaemoglobin both add a third haemoglobin that carries no oxygen. The oximeter misreads them in opposite directions, and that difference is what the exam tests.",
  parts=[
    ('a', "**Falsely normal — COHb looks like oxyhaemoglobin; PaO₂ normal.** Carboxyhaemoglobin absorbs red light much as oxyhaemoglobin does, so it is counted as saturated. PaO₂ measures dissolved oxygen, which is normal. Only co-oximetry measures COHb."),
    ('b', "**Drifts toward ~85% as MetHb rises — it absorbs equally at 660 and 940 nm.** An equal absorption ratio corresponds to a reading of about 85%, so the SpO₂ settles there however high the MetHb climbs. A low SpO₂ with a normal PaO₂ that does not respond to oxygen is the ‘saturation gap’."),
    ('c', "**Benzocaine/prilocaine before endoscopy, dapsone, nitrites/nitrates, primaquine, rasburicase.** These oxidise haem iron from the ferrous to the ferric state, which cannot bind oxygen. Topical anaesthetic sprays are the classic ICU cause."),
    ('d', "**Methylene blue 1–2 mg/kg if symptomatic or MetHb >20–30%; never in G6PD deficiency.** Methylene blue is reduced to leucomethylene blue by NADPH-dependent reductase, and this reduces methaemoglobin back to haemoglobin. The NADPH comes from G6PD; without it the drug does not work and can cause haemolysis."),
    ('e', "**COHb >25% (>15% in pregnancy), loss of consciousness, ischaemia or neurological signs.** Hyperbaric oxygen shortens the COHb half-life and is given to reduce delayed neurological sequelae. Fetal haemoglobin binds CO more tightly, hence the lower threshold in pregnancy."),
  ],
  mimic=[
    ("CO vs cyanide", "Both give a normal SpO₂ with tissue hypoxia; cyanide gives a very high lactate and high venous oxygen."),
    ("Methaemoglobinaemia vs sulfhaemoglobinaemia", "Both cause cyanosis; sulfhaemoglobin does not respond to methylene blue."),
  ],
  traps=[
    ("“A normal SpO₂ excludes CO poisoning”", "COHb reads as oxyhaemoglobin; send a co-oximetry sample."),
    ("“A normal PaO₂ excludes hypoxia”", "PaO₂ measures dissolved oxygen, not how much haemoglobin can carry."),
    ("“Methylene blue works in everyone”", "It needs NADPH from G6PD; in deficiency it fails and haemolyses."),
  ],
  decode=[
    ("Cyanosis after endoscopy spray, SpO₂ 85% unchanged on oxygen, PaO₂ normal", "Methaemoglobinaemia → methylene blue."),
    ("Headache in a family sharing a heater, SpO₂ 99%", "Carbon monoxide → co-oximetry, 100% oxygen."),
    ("Methylene blue given, cyanosis worse, haemolysis", "G6PD deficiency."),
  ],
  punch="The oximeter cannot see what it was not built for: carbon monoxide reads as normal, methaemoglobin as about 85%, and only co-oximetry tells the truth.",
)

T['TX1-ALC'] = dict(
  sub="Toxicology → Toxic alcohols → Block or dialyse",
  intro="Methanol and ethylene glycol are not very toxic themselves. Alcohol dehydrogenase converts them to formic acid and glycolic and oxalic acids, which cause the acidosis, blindness and renal failure. Treatment therefore has two parts: stop the enzyme before acid forms, and remove the alcohol and acid once harm has started.",
  parts=[
    ('a', "**Empirically when a toxic alcohol is suspected and the level is delayed.** Fomepizole blocks alcohol dehydrogenase, so no new acid forms while waiting. Toxic alcohol levels are rarely available quickly, and every hour of delay lets more acid form."),
    ('b', "**No — in a late presenter the alcohol is already metabolised to acid.** The osmolal gap reflects the unmetabolised alcohol; as it is converted, the osmolal gap falls and the anion gap rises. A normal osmolal gap with high anion gap acidosis is consistent with late poisoning. The normal range is also wide, so a small toxic amount can hide inside it."),
    ('c', "**Ethanol ≥100 mg/dL saturates alcohol dehydrogenase (10–20× higher affinity).** The enzyme prefers ethanol, so while ethanol is at this level the toxic alcohol is hardly metabolised. Fomepizole becomes necessary as the ethanol level falls."),
    ('d', "**Visual signs, AKI or severe acidosis.** These show that acid has already formed and is causing organ damage. Haemodialysis removes both the parent alcohol and the toxic acids, which fomepizole cannot do."),
  ],
  mimic=[
    ("Toxic alcohol vs alcoholic ketoacidosis", "Both give high anion gap acidosis in a drinker; ketoacidosis has ketones, often low glucose, and a small osmolal gap."),
    ("Isopropanol", "Raises the osmolal gap but makes acetone, a ketone, not an acid — no acidosis."),
  ],
  traps=[
    ("“Normal osmolal gap, so not a toxic alcohol”", "A late presenter has converted the alcohol to acid."),
    ("“Wait for the level before fomepizole”", "Give it on suspicion; delay lets acid form."),
    ("“Fomepizole is enough once the patient is blind”", "Established acid and organ damage need dialysis."),
  ],
  decode=[
    ("Drinker, blurred vision, high anion gap acidosis, normal osmolal gap", "Late methanol → fomepizole and dialysis."),
    ("Suspected ethylene glycol, level awaited", "Fomepizole now."),
    ("Co-ingested ethanol, level 150 mg/dL", "Alcohol dehydrogenase is occupied; fomepizole can follow as ethanol falls."),
  ],
  punch="Block the enzyme early, while there is still alcohol to block; dialyse once the acid or the damage is already there.",
)

T['TX1-S1'] = dict(
  sub="Toxicology → Toxidromes → Sympathomimetic with a negative screen",
  intro="A patient is agitated, hallucinating, hypertensive, tachycardic and sweating — a sympathomimetic toxidrome. The urine screen is negative for amphetamines and cocaine. That does not exclude a drug; it shows the limits of the test.",
  parts=[
    ('a', "**Synthetic cathinones (bath salts, mephedrone) or synthetic cannabinoids — routine immunoassays miss them.** A urine immunoassay detects only the molecules its antibodies were made against. These new psychoactive substances are structurally different enough to escape the amphetamine and cannabinoid assays, and their structures keep changing. The diagnosis is clinical."),
    ('b', "**Benzodiazepines, cooling, fluids; watch hyperthermia, rhabdomyolysis, hyponatraemia.** Benzodiazepines reduce central sympathetic drive, which lowers heart rate, blood pressure and heat production. Agitation and muscle activity cause hyperthermia and rhabdomyolysis, which are the main causes of death. Hyponatraemia is reported with mephedrone, as with MDMA, and can cause seizures."),
  ],
  mimic=[
    ("Sympathomimetic vs anticholinergic", "Both are hot, agitated and tachycardic; the sympathomimetic patient sweats, the anticholinergic patient has dry skin and urinary retention."),
    ("Serotonin syndrome", "Also hot and agitated, but with clonus and hyperreflexia, worse in the legs, after a serotonergic drug."),
  ],
  traps=[
    ("“Negative screen, so not drug-induced”", "Immunoassays miss most new psychoactive substances; treat the toxidrome."),
    ("“A β-blocker for the tachycardia”", "Sedation with benzodiazepines comes first; it treats the cause of the tachycardia and hypertension."),
  ],
  decode=[
    ("Festival-goer, agitation, hypertension, sweating, screen negative", "Synthetic cathinone → benzodiazepines, cooling."),
    ("Same picture with dark urine and high CK", "Rhabdomyolysis — fluids."),
    ("Same picture with a seizure and sodium 122", "Drug-associated hyponatraemia."),
  ],
  punch="A urine screen finds only what it was built to find; a sympathomimetic picture with a negative screen is still a sympathomimetic, and it is treated with sedation and cooling.",
)

T['TX1-S2'] = dict(
  sub="Toxicology → Toxidromes → Opioid look-alike",
  intro="Coma, pinpoint pupils and slow breathing look like opioid poisoning, so naloxone is given. When it fails, the question becomes which drug produces the same picture through a different receptor.",
  parts=[
    ('a', "**Clonidine (central α₂ agonist).** Clonidine stimulates α₂ receptors in the brainstem, which reduces sympathetic outflow: miosis, sedation, respiratory depression, bradycardia and hypotension. Children are often poisoned by a single tablet or by imidazoline eye or nasal drops, which act the same way. Early transient hypertension can occur from peripheral α stimulation."),
    ('b', "**Supportive care; atropine for bradycardia. Naloxone response is inconsistent.** Most patients recover within 24–48 hours with airway and circulatory support. Atropine treats symptomatic bradycardia, and fluids or vasopressors treat hypotension. Naloxone helps some patients, possibly through an indirect opioid link, but its effect cannot be relied upon."),
  ],
  mimic=[
    ("Clonidine vs opioid", "Same picture; clonidine adds marked bradycardia and hypotension, and naloxone often fails."),
    ("Clonidine vs pontine haemorrhage", "Pontine haemorrhage also gives coma with pinpoint pupils; CT separates them."),
  ],
  traps=[
    ("“Pinpoint pupils and apnoea mean opioid”", "Clonidine, imidazolines and pontine haemorrhage give the same picture."),
    ("“If naloxone fails, give more until it works”", "Clonidine response is inconsistent; supportive care is the treatment."),
    ("“Early hypertension excludes clonidine”", "A brief hypertensive phase can precede hypotension."),
  ],
  decode=[
    ("Toddler, coma, miosis, HR 50, naloxone no response", "Clonidine (or imidazoline drops)."),
    ("Father’s antihypertensive tablets at home, child drowsy and bradycardic", "Clonidine → supportive care, atropine."),
  ],
  punch="Clonidine copies the opioid picture through a different receptor, so the opioid antidote is unreliable and care is supportive.",
)

T['TX1-S3'] = dict(
  sub="Toxicology → Smoke inhalation → Cyanide and carbon monoxide",
  intro="Burning wool, silk, plastics and foam release hydrogen cyanide as well as carbon monoxide. A house-fire victim can therefore have two poisons that both stop oxygen use, and neither lowers the pulse oximeter reading. The blood lactate is the clue.",
  parts=[
    ('a', "**Cyanide plus carbon monoxide.** COHb reads as oxyhaemoglobin, so SpO₂ is normal. Cyanide blocks cytochrome oxidase, so cells cannot use oxygen and switch to anaerobic metabolism; venous blood stays oxygenated and lactate rises. In smoke inhalation a lactate of about 8–10 mmol/L or more strongly suggests cyanide."),
    ('b', "**Hydroxocobalamin 5 g with 100% O₂ (intubate if GCS ≤8); avoid nitrites — their methaemoglobin worsens oxygen carriage.** Hydroxocobalamin binds cyanide to form cyanocobalamin, which is excreted in urine; it is given intravenously over 15 minutes and can be repeated. Nitrites work by creating methaemoglobin, which binds cyanide, but with CO already blocking haemoglobin this further reduces oxygen delivery. 100% oxygen speeds removal of CO."),
  ],
  mimic=[
    ("Smoke victim vs simple CO poisoning", "CO alone rarely gives a very high lactate; a lactate of 12 with shock points to cyanide."),
  ],
  traps=[
    ("“SpO₂ 99%, so oxygenation is fine”", "COHb reads as oxyhaemoglobin and cyanide stops oxygen use, not delivery."),
    ("“Use the standard cyanide kit with nitrites”", "Nitrite-induced methaemoglobin adds to the CO deficit in carriage; hydroxocobalamin is safe."),
    ("“Wait for the cyanide level”", "The level takes hours; treat on the clinical picture and lactate."),
  ],
  decode=[
    ("Fire victim, coma, high lactate, normal SpO₂", "Cyanide with CO → hydroxocobalamin and 100% oxygen."),
    ("Which cyanide antidote to avoid in smoke inhalation?", "Nitrites."),
    ("Red urine after treatment", "Hydroxocobalamin colouring, expected."),
  ],
  punch="In a fire victim with a normal SpO₂, the lactate gives cyanide away: give hydroxocobalamin and oxygen, never nitrites.",
)

T['TX1-ME'] = dict(
  sub="Toxicology → Heavy metals → Arsenic, lead, mercury",
  intro="Heavy metals poison enzymes by binding their sulfhydryl groups. In the ICU they appear as an unexplained gastroenteritis with arrhythmia, a neuropathy that looks like Guillain–Barré syndrome, or an encephalopathy. Chelators treat them by offering the metal a partner it binds more tightly, which is then excreted.",
  parts=[
    ('a', "**Binds sulfhydryl groups (blocks pyruvate dehydrogenase); garlic odour, rice-water diarrhoea, QT prolongation.** Blocking pyruvate dehydrogenase stops aerobic energy production in cells. Damage to capillaries in the gut causes profuse watery diarrhoea and fluid loss, and potassium-channel effects prolong the QT, leading to torsades."),
    ('b', "**At 1–3 weeks an ascending axonal neuropathy that mimics GBS; Mees lines.** The neuropathy is sensorimotor, often painful, and can progress to weakness and respiratory failure. Mees lines are white transverse bands across the nails; they appear weeks later as the nail grows out."),
    ('c', "**24-h urine arsenic (blood clears in days); chelate with dimercaprol, then DMSA or DMPS.** Arsenic leaves the blood quickly, so a blood level taken at the neuropathy stage is often normal while urine still shows it. Dimercaprol is given intramuscularly in the acute, unwell patient; oral DMSA or DMPS follows when the gut works."),
    ('d', "**Dimercaprol first, then CaNa₂EDTA 4 h later; avoid LP and routine hyperventilation.** EDTA given alone mobilises lead from tissues and can move it into the brain, worsening encephalopathy; dimercaprol first prevents this. Lead encephalopathy causes cerebral oedema, so lumbar puncture risks herniation."),
    ('e', "**Swallowed elemental (thermometer): harmless. Inhaled vapour: pneumonitis, ARDS, neurotoxicity.** Elemental mercury is almost not absorbed from the gut. Heated or vaporised, it is absorbed well through the lungs and damages lung and brain."),
  ],
  mimic=[
    ("Arsenic neuropathy vs GBS", "Both ascend; arsenic follows a gastrointestinal illness with QT prolongation and later Mees lines — check urine arsenic before treating as GBS."),
  ],
  traps=[
    ("“Normal blood arsenic excludes poisoning”", "Blood clears in days; 24-hour urine is the test."),
    ("“EDTA alone for lead encephalopathy”", "It can move lead into the brain; dimercaprol goes first."),
    ("“A swallowed thermometer needs chelation”", "Elemental mercury is not absorbed from the gut."),
  ],
  decode=[
    ("Vomiting and diarrhoea, then 2 weeks later ascending weakness", "Arsenic → 24-hour urine arsenic, dimercaprol."),
    ("Child with pica, seizures, raised ICP", "Lead encephalopathy → dimercaprol, then EDTA."),
    ("Heated mercury in a closed room, then ARDS", "Inhaled mercury vapour."),
  ],
  punch="Metals poison by binding sulfhydryl groups and chelators offer them a better partner — but the route and the order of chelation decide whether that helps or harms.",
)

T['TX1-FE'] = dict(
  sub="Toxicology → Metals → Iron poisoning",
  intro="Iron tablets are common in homes, and in children they are a classic cause of death from overdose. Iron first damages the gut directly, then enters the circulation and cells, where free iron damages mitochondria. The stages follow that path, and the quiet middle stage is where patients are wrongly sent home.",
  parts=[
    ('a', "**Corrosive GI: vomiting, haematemesis, shock.** Iron is directly corrosive to the gut lining. Vomiting and diarrhoea, sometimes bloody, with fluid loss can cause early hypovolaemic shock. A patient with no gastrointestinal symptoms by 6 hours is unlikely to develop serious toxicity."),
    ('b', "**Latent — apparent recovery while iron enters cells: the dangerous reassurance.** Gut symptoms settle, but iron is moving into tissues. In severe poisoning this stage may be short or absent, and a persistent acidosis or tachycardia shows that toxicity is still progressing."),
    ('c', "**Shock, high anion gap acidosis, hepatic necrosis, coagulopathy.** Free iron disrupts mitochondrial oxidative phosphorylation, so cells make lactate; iron also causes vasodilatation and capillary leak. The liver receives the iron first through the portal circulation."),
    ('d', "**Hepatic failure; gastric outlet stricture at 2–6 weeks.** Survivors of the early stages may develop liver failure. The early corrosive injury heals with scarring, which can obstruct the pylorus weeks later."),
    ('e', "**Not bound by charcoal (an ion) → whole bowel irrigation; tablets are radio-opaque; deferoxamine up to 15 mg/kg/h (vin-rosé urine), usually stopped by ~24 h (ARDS).** Charcoal does not bind charged metals, so tablets seen on X-ray are flushed through with polyethylene glycol. Deferoxamine binds free iron to form ferrioxamine, which colours urine red-orange. Infusions beyond about 24 hours are associated with ARDS."),
  ],
  mimic=[
    ("Iron vs lithium", "Both are not bound by charcoal and are treated with whole bowel irrigation; iron tablets are radio-opaque and give a corrosive gastroenteritis."),
  ],
  traps=[
    ("“Symptoms have settled at 12 hours, so discharge”", "That may be the latent stage; check acidosis and serum iron."),
    ("“Give activated charcoal”", "Iron is an ion and is not bound."),
    ("“Continue deferoxamine until the urine clears”", "Long infusions cause ARDS; usually stopped by about 24 hours."),
  ],
  decode=[
    ("Child, mother’s tablets, vomiting, then well, then shock at 30 h", "Iron poisoning, stage 3."),
    ("Radio-opaque tablets on abdominal X-ray", "Iron → whole bowel irrigation."),
    ("Urine turns vin-rosé on treatment", "Deferoxamine binding iron."),
  ],
  punch="Iron burns the gut, then hides in cells: a quiet middle stage is not recovery, so judge by the acidosis, not by how the patient looks.",
)

T['TX1-CA'] = dict(
  sub="Toxicology → Corrosives → Caustic ingestion",
  intro="A patient has swallowed a strong acid or alkali. The burn to the pharynx and larynx swells over the following hours, so a patient who is talking now can obstruct later. Hoarseness, stridor and drooling show that the larynx is already involved.",
  parts=[
    ('a', "**Secure the airway early (fibreoptic or awake): laryngeal oedema worsens over hours.** Intubation becomes harder as the oedema grows, so it is done while it is still possible. A blind or rapid technique can traumatise burned tissue, so the airway is secured under direct vision."),
    ('b', "**Endoscopy within 12–24 h for Zargar grading.** Grading the depth of the burn predicts stricture and perforation and guides feeding and steroid decisions. Beyond about 48 hours the healing wall softens, and it is weakest from roughly day 5 to day 15, when endoscopy carries the highest risk of perforation."),
    ('c', "**No emesis, no charcoal, no neutralisation, no blind NG tube.** Vomiting re-exposes the oesophagus and airway to the caustic. Charcoal does not bind caustics and obscures endoscopy. Neutralisation produces heat and adds thermal injury, and a blind tube can perforate a burned oesophagus."),
    ('d', "**No overall benefit; only a deep circumferential grade IIb burn may benefit — never grade III (masks perforation).** Trials have not shown that steroids reduce strictures overall. In grade IIb burns, some data suggest a reduction; in grade III necrosis, steroids add infection risk and hide the signs of perforation."),
  ],
  table=dict(title="Zargar grading", head=["Grade", "Finding"],
    rows=[["I", "Oedema and redness"], ["IIa", "Superficial ulcers, erosions"], ["IIb", "Deep or circumferential ulcers"], ["IIIa", "Scattered necrosis"], ["IIIb", "Extensive necrosis"]]),
  mimic=[
    ("Alkali vs acid", "Alkali causes liquefactive necrosis, penetrating deeply, mainly in the oesophagus; acid causes coagulative necrosis, often worse in the stomach."),
  ],
  traps=[
    ("“No mouth burns, so no oesophageal injury”", "The oesophagus can be burned without visible oral injury; symptoms guide endoscopy."),
    ("“Neutralise the alkali with a weak acid”", "The reaction produces heat and worsens the burn."),
    ("“Steroids prevent strictures”", "No overall benefit, and harmful in grade III."),
  ],
  decode=[
    ("Drooling, hoarseness after drinking drain cleaner", "Secure the airway first."),
    ("Next step after stabilisation", "Endoscopy within 12–24 hours."),
    ("Grade III on endoscopy — steroids?", "No."),
  ],
  punch="A caustic burn of the larynx swells while the patient still looks well, so the airway is secured first and the endoscopy grades everything else.",
)

T['TX1-SK'] = dict(
  sub="Toxicology → Drug reactions → SJS/TEN vs DRESS",
  intro="Two severe drug reactions can bring a patient to the ICU with a rash and fever. SJS/TEN is widespread death of the epidermis and mucosa, behaving like a burn. DRESS is a delayed systemic hypersensitivity reaction in which the internal organs, not the skin, carry the risk.",
  parts=[
    ('a', "**One spectrum by detachment: SJS <10% · overlap 10–30% · TEN >30% BSA.** Both are caused by cytotoxic T cells killing keratinocytes. The name depends only on the area of skin that detaches, and mortality rises with it."),
    ('b', "**SJS/TEN 4–28 days; DRESS 2–8 weeks.** The latency is a key clue. DRESS appears later than almost any other drug rash, so a recently started drug may not be the cause — the causative drug is often one started a month or more before."),
    ('c', "**Eosinophilia with fever, facial oedema, nodes and organ involvement (liver most).** DRESS is a systemic hypersensitivity, so blood and organs are affected. Hepatitis is the commonest organ injury; kidney, lung and heart can be involved."),
    ('d', "**SJS/TEN: involved. DRESS: usually spared.** Mucosal erosions of the mouth, eyes and genitals are part of SJS/TEN, usually from the start. In DRESS they are absent or mild."),
    ('e', "**SJS/TEN: stop the drug, burn-unit care (ciclosporin or IVIG may help). DRESS: stop the drug, steroids with a slow taper.** SJS/TEN is managed like a burn: fluids, wound care, eye care, infection control. In DRESS the immune reaction drives organ damage, so systemic steroids are used, tapered slowly because it relapses."),
  ],
  table=dict(title="Telling them apart", head=["Feature", "SJS/TEN", "DRESS"],
    rows=[["Onset after drug", "4–28 days", "2–8 weeks"], ["Skin", "Blisters, detachment", "Morbilliform, facial oedema"], ["Mucosa", "Involved", "Usually spared"], ["Blood", "—", "Eosinophilia"], ["Organs", "Skin failure", "Liver, kidney, lung"], ["Treatment", "Burn care", "Steroids, slow taper"]]),
  mimic=[
    ("TEN vs staphylococcal scalded skin syndrome", "SSSS splits more superficially, spares mucosa and affects mainly children."),
  ],
  traps=[
    ("“The rash began 5 weeks after the drug, so it is not drug-induced”", "DRESS typically appears at 2–8 weeks."),
    ("“Stop steroids once the rash fades”", "DRESS relapses; taper slowly over weeks."),
  ],
  decode=[
    ("Started carbamazepine 5 weeks ago, fever, facial oedema, eosinophilia, raised ALT", "DRESS → stop drug, steroids."),
    ("10 days after a new drug, blisters, oral erosions, 40% detachment", "TEN → burn unit."),
    ("Detachment 20%", "SJS/TEN overlap."),
  ],
  punch="Timing and blood separate them: early skin and mucosal necrosis is SJS/TEN and is treated as a burn; late fever, eosinophils and organ injury is DRESS and is treated with a slow steroid taper.",
)

T['TX1-QN'] = dict(
  sub="Toxicology → Sodium-channel blockers → Quinine",
  intro="Quinine is still used for malaria and, in some places, for cramps. In overdose it behaves like other sodium-channel blockers on the heart, but it also damages the retina and stimulates insulin release. These two features make it recognisable.",
  parts=[
    ('a', "**Cinchonism: tinnitus, deafness, nausea, headache.** These appear even at high therapeutic levels and are the first sign of toxicity. They come from toxicity to the inner ear and the central nervous system."),
    ('b', "**Blindness at 6–12 h, fixed dilated pupils.** Quinine is directly toxic to the retina. Vision may recover partly over weeks, but permanent loss can occur."),
    ('c', "**Na⁺-channel block: wide QRS, VT → bicarbonate.** Like tricyclics, quinine slows conduction through sodium channels, widening the QRS and causing ventricular arrhythmias. Sodium bicarbonate raises extracellular sodium and pH, which reduces drug binding to the channel. It also blocks potassium channels, so the QT lengthens."),
    ('d', "**Hypoglycaemia (quinine releases insulin).** Quinine stimulates insulin secretion from pancreatic β cells. Low glucose can add to coma and seizures, so it is checked repeatedly."),
    ('e', "**Multi-dose charcoal; dialysis does not help.** Repeated charcoal binds quinine in the gut and draws it from the circulation, shortening its half-life. Quinine is widely distributed in tissues and protein-bound, so little is in the blood for dialysis to remove."),
  ],
  mimic=[
    ("Quinine vs tricyclic overdose", "Both widen the QRS and respond to bicarbonate; quinine adds blindness, tinnitus and hypoglycaemia."),
    ("Quinine vs salicylate", "Both cause tinnitus; salicylate gives respiratory alkalosis with metabolic acidosis, not wide QRS and blindness."),
  ],
  traps=[
    ("“Dialyse to remove quinine”", "Its large distribution volume makes dialysis ineffective; use multi-dose charcoal."),
    ("“Coma in quinine overdose is only cardiac”", "Hypoglycaemia from insulin release can cause or worsen it."),
  ],
  decode=[
    ("Overdose with tinnitus, then sudden blindness", "Quinine."),
    ("Wide QRS in quinine overdose", "Sodium bicarbonate."),
    ("Recurrent low glucose in a malaria patient on quinine", "Quinine-induced insulin release."),
  ],
  punch="Quinine is a sodium-channel blocker with two extras: it blinds and it releases insulin, so give bicarbonate for the QRS, glucose for the sugar, and charcoal, not dialysis.",
)

T['TX1-AS'] = dict(
  sub="Toxicology → Sodium-channel blockers → Antiseizure drug overdose",
  intro="Lamotrigine and carbamazepine control seizures by blocking neuronal sodium channels. In overdose the same block appears in the heart, and, paradoxically, the brain can start seizing. Treating these seizures means choosing drugs that do not add more sodium-channel block.",
  parts=[
    ('a', "**At toxic levels the Na⁺ block silences inhibitory interneurons → paradoxical seizures.** Inhibitory interneurons fire rapidly and depend heavily on sodium channels, so they may be suppressed first. With less inhibition, excitatory neurons are released and seizures follow."),
    ('b', "**Wide QRS — the same block in the heart.** Cardiac sodium channels conduct the impulse through the ventricles. Blocking them slows conduction and widens the QRS, with risk of ventricular arrhythmia and hypotension."),
    ('c', "**Benzodiazepines, then phenobarbital or propofol.** These work on GABA-A receptors and do not depend on sodium channels. Phenytoin is avoided because it is itself a sodium-channel blocker and adds to cardiac toxicity."),
    ('d', "**Bicarbonate; lipid if refractory.** Raising extracellular sodium and pH reduces drug binding to the channel and narrows the QRS. Intravenous lipid emulsion is a rescue therapy for lipophilic drugs when the patient does not respond."),
  ],
  mimic=[
    ("Antiseizure drug vs tricyclic overdose", "Both cause wide QRS and seizures and both respond to bicarbonate; carbamazepine is structurally similar to tricyclics and also anticholinergic."),
  ],
  traps=[
    ("“Seizures in overdose mean the antiseizure level is low”", "In toxicity the drug itself can cause seizures."),
    ("“Phenytoin for the seizures”", "It is another sodium-channel blocker and worsens cardiac toxicity."),
    ("“A wide QRS needs lidocaine or a class Ic drug”", "Class I antiarrhythmics add sodium-channel block; give bicarbonate."),
  ],
  decode=[
    ("Lamotrigine overdose, seizure, QRS 130 ms", "Benzodiazepine and sodium bicarbonate."),
    ("Carbamazepine overdose, seizures — which anticonvulsant to avoid?", "Phenytoin."),
    ("Refractory hypotension and wide QRS despite bicarbonate", "Lipid emulsion."),
  ],
  punch="Too much sodium-channel block silences the brain’s brakes and slows the heart, so treat with GABA drugs and bicarbonate, never another sodium-channel blocker.",
)

T['TX1-INH'] = dict(
  sub="Toxicology → Seizures → Isoniazid overdose",
  intro="A patient on tuberculosis treatment is seizing, and the seizures do not stop with a benzodiazepine. Isoniazid in overdose depletes the vitamin the brain needs to make its main inhibitory transmitter. Until that vitamin is replaced, the usual anticonvulsants have little to act on.",
  parts=[
    ('a', "**Isoniazid — give pyridoxine with the benzodiazepine: gram for gram, or 5 g IV if the amount is unknown.** Isoniazid depletes pyridoxal phosphate, the active form of vitamin B6, which is the cofactor for glutamic acid decarboxylase, the enzyme that makes GABA. With low GABA the brain seizes, and benzodiazepines, which enhance GABA, have too little GABA to work with. Pyridoxine restores GABA synthesis, and the two drugs together stop the seizures. The acidosis comes from lactate produced by prolonged seizures."),
    ('b', "**Phenytoin does not work.** Phenytoin acts on sodium channels and does nothing to correct the GABA deficit. The seizures are corrected only by replacing pyridoxine."),
  ],
  mimic=[
    ("Isoniazid vs other causes of refractory seizures in overdose", "Tricyclics, bupropion and tramadol also cause seizures; the clue to isoniazid is TB treatment and failure of benzodiazepines."),
    ("Isoniazid vs toxic alcohol", "Both give coma and high anion gap acidosis; isoniazid has seizures from the start and a TB history."),
  ],
  traps=[
    ("“More benzodiazepine will eventually work”", "Without pyridoxine there is too little GABA to enhance."),
    ("“Load phenytoin for refractory seizures”", "It does not act on GABA synthesis and fails."),
    ("“Pyridoxine replaces the benzodiazepine”", "They are given together; they work as a pair."),
  ],
  decode=[
    ("TB patient, refractory seizures, high anion gap acidosis", "Isoniazid → pyridoxine."),
    ("Unknown amount of isoniazid ingested — pyridoxine dose?", "5 g IV."),
    ("Known amount taken", "Gram for gram."),
  ],
  punch="Isoniazid takes away the vitamin B6 that GABA synthesis depends on, so GABA drugs fail until pyridoxine is replaced.",
)

T['TX1-RAD'] = dict(
  sub="Toxicology → Physical agents → Acute radiation syndrome",
  intro="After whole-body radiation exposure, cells that divide rapidly die first, because radiation damages DNA and the damage shows when a cell tries to divide. The dose therefore decides which tissue fails: marrow at the lowest dose, then gut lining, and at very high doses the nervous system and blood vessels. Estimating the dose early guides who needs intensive care.",
  parts=[
    ('a', "**Haematopoietic: marrow nadir at 2–4 weeks; the 48-h lymphocyte count estimates the dose.** Marrow stem cells are very sensitive, but mature blood cells already in circulation survive their normal lifespan, so counts fall over weeks. Lymphocytes are the exception: they die directly from radiation, and the fall in the absolute lymphocyte count over the first 48 hours tracks the dose."),
    ('b', "**Gastrointestinal: vomiting, diarrhoea, sepsis within days.** The crypt cells that replace the gut lining are destroyed, so the lining sloughs within days. Fluid loss, bleeding and bacterial translocation follow, made worse by the falling neutrophil count."),
    ('c', "**Neurovascular (signs from ~20 Gy, full syndrome >~50 Gy): collapse within hours; uniformly fatal.** At these doses damage to blood vessels and neurons causes oedema, confusion, hypotension and collapse within hours. Death follows within days, and care is palliative."),
    ('d', "**Vomiting within 1 hour.** The prodrome of nausea and vomiting comes earlier with higher doses. Vomiting within an hour suggests a dose of roughly 4 Gy or more, which means significant marrow failure is likely."),
  ],
  table=dict(title="Dose to syndrome", head=["Dose", "Syndrome", "Timing"],
    rows=[[">1 Gy", "Haematopoietic", "Nadir 2–4 weeks"], [">6 Gy", "Gastrointestinal", "Days"], ["≥20 Gy", "Neurovascular", "Hours"]]),
  mimic=[
    ("Radiation sickness vs gastroenteritis", "Early vomiting after a known exposure, followed by falling lymphocytes, marks radiation injury."),
  ],
  traps=[
    ("“The patient feels well after the prodrome, so the dose was low”", "A latent phase follows the prodrome; the marrow nadir comes weeks later."),
    ("“Platelets and neutrophils fall first”", "Lymphocytes fall first, within 48 hours; they estimate the dose."),
  ],
  decode=[
    ("Radiation accident, vomiting at 30 minutes", "High dose — expect marrow failure, possibly GI syndrome."),
    ("Best early lab estimate of dose", "Absolute lymphocyte count at 24–48 hours."),
    ("Collapse and confusion within hours of exposure", "Neurovascular syndrome, fatal."),
  ],
  punch="The faster a tissue divides, the lower the dose that kills it: marrow first, then gut lining, then nerves and vessels, and how soon the patient vomits shows how high the dose was.",
)

FLAGS = {
  'TX1-ALC': "Card d lists clinical dialysis triggers only. EXTRIP/standard texts also dialyse on level (e.g. methanol >50 mg/dL, or >70 mg/dL with fomepizole) and on severe acidosis thresholds (pH ≤7.15–7.25) — consider adding the level criterion, which MCQs test.",
  'TX1-SAT': "Card e lists the common HBO criteria; the evidence for HBO in CO is contested and criteria vary (some add pH <7.1 or COHb >20% in pregnancy elsewhere). Card statement kept; fine for exam use.",
  'TX1-CA': "Card b says endoscopy within 12–24 h; most texts allow up to 48 h and say avoid roughly days 5–15 (tissue weakest). Kept card window; the text mentions the risk rising after ~48 h.",
  'TX1-AS': "Card a gives the interneuron-silencing mechanism as fact; it is a proposed explanation rather than established. Also worth adding: severe carbamazepine poisoning is an EXTRIP indication for high-flux haemodialysis, and MDAC is used.",
  'TX1-FE': "Stage timings vary by source (stage 3 often given as 6–72 h; stricture at 2–8 weeks). Card values kept. Deferoxamine indications (serum iron >500 µg/dL, shock, acidosis, altered consciousness) are not on the card and are commonly tested.",
  'TX1-RAD': "Card a says haematopoietic syndrome '>1 Gy'; many sources place clinically significant H-ARS at 2–6 Gy (prodrome from ~1 Gy). Card kept. Vomiting-within-1-h dose (~4 Gy+) was added from IAEA-style time-to-emesis tables.",
}
