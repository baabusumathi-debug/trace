# TOX01 top-up cards — Explain v2 ("Learn" depth), same fields and voice as tox01_learn.py.
# Fields: sub, intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Audited 6 Nov: no TU codes appear in qpack/TOX01.md, so each top-up is linked to the questions under its parent cards that test its content.
T = {}

T['TX1-QT'] = dict(
  sub="Toxicology → Cardiac toxicity → Drug-induced long QT",
  intro="Many common ICU drugs block the cardiac potassium channel (hERG) that ends the action potential. Repolarisation is delayed, the QT lengthens, and an early afterdepolarisation can set off torsades de pointes. The risk is cumulative: each extra drug — quinolone, macrolide, azole, antipsychotic, tricyclic — a low potassium or magnesium, or a raised drug level adds to it.",
  parts=[
    ('a', "**Citalopram and escitalopram.** Among the SSRIs these two prolong the QT in a dose-dependent way, so torsades on an SSRI means citalopram. Sertraline is the usual choice when cardiac risk is a concern."),
    ('b', "**Thioridazine and ziprasidone; IV haloperidol is dangerous at high doses.** Thioridazine (a typical) and ziprasidone (an atypical) prolong QTc the most, so the class is not what matters: the pooled arrhythmia risk of typical and atypical antipsychotics is similar, while QTc prolongation varies drug by drug. Oral haloperidol carries modest risk, but large intravenous doses have caused torsades."),
    ('c', "**The one that also blocks CYP3A4 (erythromycin, fluconazole) — it raises the others’ levels.** Such a drug prolongs the QT itself and slows the clearance of other QT drugs, so removing it removes two sources of risk at once. When no drug on the list inhibits CYP3A4, stop the strongest hERG blocker: a tricyclic before aripiprazole (minimal QT effect), carvedilol (none) or omeprazole (only through low magnesium)."),
    ('d', "**Potassium and magnesium.** Low potassium enhances hERG block and low magnesium makes afterdepolarisations more likely. Correcting both raises the threshold for torsades, and intravenous magnesium is the first treatment once torsades occurs."),
  ],
  mimic=[
    ("Long QT vs wide QRS", "A long QT is potassium-channel block (stop the drug, give magnesium); a wide QRS is sodium-channel block (bicarbonate). Osborn waves mean hypothermia, a long PR the AV node."),
  ],
  traps=[
    ("“Typical antipsychotics carry more arrhythmia risk than atypicals”", "The risk is similar; thioridazine and ziprasidone, one from each class, prolong QTc most (only 3% chose this on DocT GT)."),
    ("“With a long QT, stop the antipsychotic first”", "Aripiprazole barely affects the QT; stop the strongest hERG blocker — here amitriptyline (67% on DocT GT)."),
    ("“Correcting potassium is enough”", "Magnesium must be corrected too."),
  ],
  decode=[
    ("Pneumonia on ciprofloxacin; carvedilol, omeprazole, aripiprazole, amitriptyline; long QT — stop first? [DocT GT]", "Amitriptyline."),
    ("ICU patient on moxifloxacin, fluconazole, then erythromycin — likely ECG finding? [DocT GT]", "Widened QT."),
    ("Arrhythmia risk: typical vs atypical antipsychotics [DocT GT]", "No difference."),
    ("Torsades on an SSRI: which? [Marrow]", "Citalopram."),
  ],
  punch="QT risk adds up, so remove the drug that multiplies the others — or the strongest hERG blocker — first, then correct potassium and magnesium.",
)

T['TX1-SAT'] = dict(
  sub="Toxicology → Gases and haemoglobin → Carbon monoxide vs methaemoglobin",
  intro="A pulse oximeter estimates saturation from the ratio of light absorbed at two wavelengths, 660 and 940 nm, and assumes only oxyhaemoglobin and deoxyhaemoglobin are present. Carbon monoxide and methaemoglobin both add a third haemoglobin that carries no oxygen. The oximeter misreads them in opposite directions, and that difference is what the exam tests.",
  parts=[
    ('a', "**Falsely normal — COHb looks like oxyhaemoglobin; PaO₂ normal.** Carboxyhaemoglobin absorbs red light much as oxyhaemoglobin does, so it is counted as saturated; PaO₂ measures dissolved oxygen, which is normal. Only co-oximetry (or, classically, the Hoppe-Seyler alkali test) shows COHb."),
    ('b', "**Drifts toward ~85% as MetHb rises — it absorbs equally at 660 and 940 nm.** An equal absorption ratio corresponds to a reading of about 85%, so SpO₂ settles there however high the MetHb climbs, with a normal PaO₂ and chocolate-brown blood."),
    ('c', "**Benzocaine/prilocaine before endoscopy, dapsone, nitrites/nitrates, primaquine, rasburicase.** These oxidise haem iron from ferrous to ferric, which cannot bind oxygen. Topical anaesthetic sprays are the classic cause; paracetamol, atropine and digoxin are not causes."),
    ('d', "**Methylene blue 1–2 mg/kg if symptomatic or MetHb >20–30%; never in G6PD deficiency.** Methylene blue is reduced to leucomethylene blue by an NADPH-dependent reductase, and this reduces methaemoglobin. The NADPH comes from G6PD; without it the drug fails and can haemolyse — ascorbic acid is the alternative. It is also an MAO inhibitor, so it can precipitate serotonin syndrome in a patient on an SSRI."),
    ('e', "**COHb >25% (>15% in pregnancy), loss of consciousness, ischaemia or neurological signs.** Hyperbaric oxygen shortens the COHb half-life and is given to reduce delayed neurological sequelae; without these features, normobaric 100% oxygen for about 6 hours is enough. The only absolute contraindication is an untreated pneumothorax; COPD and prior bleomycin are relative."),
  ],
  mimic=[
    ("CO vs cyanide", "Both give a normal SpO₂ with tissue hypoxia; cyanide gives a very high lactate and high venous oxygen."),
  ],
  traps=[
    ("“A normal SpO₂ excludes CO poisoning”", "COHb reads as oxyhaemoglobin; send a co-oximetry sample."),
    ("“Methaemoglobinaemia gives a low PaO₂”", "PaO₂ is normal; the SpO₂ sits near 85%."),
    ("“Methylene blue works in everyone”", "It needs NADPH from G6PD; in deficiency it fails and haemolyses — use ascorbic acid (43% on DocT)."),
    ("“COHb 12% — hyperbaric oxygen”", "Without high-risk features, 100% oxygen by mask for about 6 hours."),
  ],
  decode=[
    ("A patient with methaemoglobinaemia will show [DocT GT]", "Pulse oximetry around 85%."),
    ("Which drug causes methaemoglobinaemia: paracetamol, benzocaine, atropine, digoxin? [DocT GT]", "Benzocaine."),
    ("Chemical-factory worker with cyanosis — true statement [DocT]", "Ascorbic acid is used in G6PD deficiency."),
    ("Painter, CO exposure, COHb 12%, no high-risk features [Marrow]", "High-flow oxygen for 6 hours."),
  ],
  punch="The oximeter cannot see what it was not built for: carbon monoxide reads as normal, methaemoglobin as about 85%, and only co-oximetry tells the truth.",
)

T['TX1-ALC'] = dict(
  sub="Toxicology → Toxic alcohols → Block or dialyse",
  intro="Methanol and ethylene glycol are not very toxic themselves. Alcohol dehydrogenase converts them to formic acid and glycolic and oxalic acids, which cause the acidosis, blindness and renal failure. Treatment therefore has two parts: stop the enzyme before acid forms, and remove the alcohol and acid once harm has started.",
  parts=[
    ('a', "**Empirically when a toxic alcohol is suspected and the level is delayed.** Fomepizole blocks alcohol dehydrogenase, so no new acid forms while waiting; levels are rarely available quickly, and every hour of delay lets more acid form. A high anion gap acidosis with a large osmolal gap, no ethanol and no ketones means a fomepizole load now."),
    ('b', "**No — in a late presenter the alcohol is already metabolised to acid.** As the alcohol is converted, the osmolal gap falls and the anion gap rises, and the normal range is wide, so a small toxic amount can hide inside it."),
    ('c', "**Ethanol ≥100 mg/dL saturates alcohol dehydrogenase (10–20× higher affinity).** While ethanol is at this level the toxic alcohol is hardly metabolised, so fomepizole can be deferred and started as the ethanol falls."),
    ('d', "**Visual signs, AKI or severe acidosis.** These show that acid has formed and is damaging organs. Haemodialysis removes both the parent alcohol and the acids, which fomepizole cannot do; fomepizole continues alongside (dosed more often during dialysis). A pH of 7.10 with a raised creatinine means dialysis even if the level is under 50 mg/dL."),
  ],
  mimic=[
    ("Toxic alcohol vs alcoholic ketoacidosis", "Both give high anion gap acidosis in a drinker; ketoacidosis has ketones and a small osmolal gap."),
    ("Isopropanol", "Raises the osmolal gap but makes acetone, a ketone, not an acid — no acidosis, so a patient who stays comatose with a normal pH has isopropanol, and needs no fomepizole."),
  ],
  traps=[
    ("“Wait for the level before fomepizole”", "Give it on suspicion; delay lets acid form."),
    ("“Moonshine with ethanol 453 mg/dL — fomepizole now”", "Ethanol already blocks the enzyme; fomepizole can be deferred (37% on DocT GT)."),
    ("“Severe anion gap acidosis — dialysis is the immediate therapy”", "A fomepizole load starts immediately (33% on DocT GT); dialysis is added for the acidosis or organ damage."),
    ("“Fomepizole is enough once acidosis or blindness is established”", "Established acid and organ damage need dialysis."),
  ],
  decode=[
    ("Windshield-fluid ingestion, asymptomatic, methanol level 24 h away [Marrow]", "Give fomepizole."),
    ("Confused, severe anion gap acidosis, osmolal gap 32, ethanol zero, no ketones — start immediately? [DocT GT]", "Fomepizole loading dose."),
    ("Oxycodone, liquor and moonshine, ethanol 453 — why defer fomepizole? [DocT GT]", "Ethanol."),
    ("Antifreeze, pH 7.10, creatinine 3.5, ethylene glycol 45 mg/dL [DocT GT]", "Haemodialysis (with fomepizole)."),
  ],
  punch="Block the enzyme early, while there is still alcohol to block; dialyse once the acid or the damage is already there.",
)

T['TX1-S1'] = dict(
  sub="Toxicology → Toxidromes → Sympathomimetic with a negative screen",
  intro="A patient is agitated, hallucinating, hypertensive, tachycardic and sweating — a sympathomimetic toxidrome. The urine screen is negative for amphetamines and cocaine. That does not exclude a drug; it shows the limits of the test.",
  parts=[
    ('a', "**Synthetic cathinones (bath salts, mephedrone) or synthetic cannabinoids — routine immunoassays miss them.** A urine immunoassay detects only the molecules its antibodies were made against. The standard panel picks up amphetamines (and usually MDMA), so a negative screen argues against them; cathinones are different enough to escape it. Severe hypertension and tachycardia make it a toxidrome, not a new psychosis."),
    ('b', "**Benzodiazepines, cooling, fluids; watch hyperthermia, rhabdomyolysis, hyponatraemia.** Benzodiazepines reduce central sympathetic drive, lowering heart rate, blood pressure and heat production. Hyperthermia and rhabdomyolysis are the main causes of death; hyponatraemia, as with MDMA, can cause seizures."),
  ],
  mimic=[
    ("Sympathomimetic vs anticholinergic", "Both are hot, agitated and tachycardic; the sympathomimetic patient sweats, the anticholinergic patient has dry skin and urinary retention."),
  ],
  traps=[
    ("“Negative screen, florid picture — ecstasy or amphetamine”", "The standard screen detects those; synthetic cathinone is the answer (only 16% on DocT GT)."),
    ("“Negative screen and hallucinations — new-onset schizophrenia”", "BP 190/110 and HR 129 are a toxidrome."),
    ("“A β-blocker for the tachycardia”", "Sedation with benzodiazepines comes first; it treats the cause."),
  ],
  decode=[
    ("College student, floridly hallucinating, BP 190/110, HR 129, standard urine panel negative [DocT GT]", "Synthetic cathinone intoxication."),
    ("Same stem — why not ecstasy, amphetamine or schizophrenia? [DocT GT]", "The panel detects amphetamines and MDMA; the vital signs make it a toxidrome."),
  ],
  punch="A urine screen finds only what it was built to find; a sympathomimetic picture with a negative screen is still a sympathomimetic, and it is treated with sedation and cooling.",
)

T['TX1-S2'] = dict(
  sub="Toxicology → Toxidromes → Opioid look-alike",
  intro="Coma, pinpoint pupils and slow breathing look like opioid poisoning, so naloxone is given. When it fails, the question becomes which drug produces the same picture through a different receptor.",
  parts=[
    ('a', "**Clonidine (central α₂ agonist).** Clonidine stimulates brainstem α₂ receptors and reduces sympathetic outflow: miosis, sedation, respiratory depression, bradycardia and hypotension. Children are often poisoned by a single tablet or by imidazoline eye or nasal drops. Early transient hypertension can occur from peripheral α stimulation."),
    ('b', "**Supportive care; atropine for bradycardia. Naloxone response is inconsistent.** Most patients recover within 24–48 hours with airway and circulatory support; atropine treats symptomatic bradycardia."),
  ],
  mimic=[
    ("Clonidine vs benzodiazepine or organophosphate", "Benzodiazepines do not give pinpoint pupils; organophosphates add wet secretions and fasciculation."),
    ("Clonidine vs pontine haemorrhage", "Pontine haemorrhage also gives coma with pinpoint pupils; CT separates them."),
  ],
  traps=[
    ("“Pinpoint pupils, no naloxone response — benzodiazepine”", "Benzodiazepines do not cause pinpoint pupils; think clonidine."),
    ("“If naloxone fails, give more until it works”", "Clonidine response is inconsistent; supportive care is the treatment."),
  ],
  decode=[
    ("Comatose, pinpoint pupils, hypoventilation, no response to naloxone — next likely diagnosis? [DocT GT]", "Clonidine toxicity."),
    ("Same stem — why not benzodiazepine, organophosphate or CO? [DocT GT]", "No pinpoint pupils with benzodiazepines or CO; organophosphates are wet."),
  ],
  punch="Clonidine copies the opioid picture through a different receptor, so the opioid antidote is unreliable and care is supportive.",
)

T['TX1-S3'] = dict(
  sub="Toxicology → Smoke inhalation → Cyanide and carbon monoxide",
  intro="Burning wool, silk, plastics and foam release hydrogen cyanide as well as carbon monoxide. A house-fire victim can therefore have two poisons that both stop oxygen use, and neither lowers the pulse oximeter reading. The blood lactate is the clue.",
  parts=[
    ('a', "**Cyanide plus carbon monoxide.** COHb reads as oxyhaemoglobin, so SpO₂ is normal. Cyanide blocks cytochrome oxidase, so cells cannot use oxygen; venous blood stays oxygenated and lactate rises. In smoke inhalation a lactate of about 8–10 mmol/L or more strongly suggests cyanide; convulsions and coma are common."),
    ('b', "**Hydroxocobalamin 5 g with 100% O₂ (intubate if GCS ≤8); avoid nitrites — their methaemoglobin worsens oxygen carriage.** Hydroxocobalamin binds cyanide to form cyanocobalamin, excreted in urine; it is now first choice for any cyanide poisoning. Nitrites work by creating methaemoglobin, which, with CO already occupying haemoglobin, cuts oxygen delivery further; they are also vasodilators and worsen hypotension. Thiosulphate alone is safe."),
  ],
  mimic=[
    ("Smoke victim vs simple CO poisoning", "CO alone rarely gives a very high lactate; a lactate of 12 with shock points to cyanide."),
  ],
  traps=[
    ("“Cyanide, lactate 12, hypotension — nitrite plus thiosulphate”", "Hydroxocobalamin is first choice (42% on DocT)."),
    ("“Smoke victim — the standard nitrite kit is fine”", "Nitrite methaemoglobin adds to the CO deficit and lowers blood pressure; avoid it (55% on DocT GT)."),
    ("“SpO₂ 99%, so oxygenation is fine”", "COHb reads as oxyhaemoglobin and cyanide stops oxygen use, not delivery."),
  ],
  decode=[
    ("Clothing-factory fire (wool, silk), ‘bitter almond’, convulsions — cyanide treatment to AVOID? [DocT GT]", "Sodium nitrite."),
    ("Fire victim, cyanide with hypotension — avoid [Marrow]", "3% sodium nitrite."),
    ("Industrial worker, unconscious, hypotensive, lactate 12, almond odour [DocT]", "Hydroxocobalamin."),
  ],
  punch="In a fire victim with a normal SpO₂, the lactate gives cyanide away: give hydroxocobalamin and oxygen, never nitrites.",
)

T['TX1-ME'] = dict(
  sub="Toxicology → Heavy metals → Arsenic, lead, mercury",
  intro="Heavy metals poison enzymes by binding their sulfhydryl groups. In the ICU they appear as an unexplained gastroenteritis with arrhythmia, a neuropathy that looks like Guillain–Barré syndrome, or an encephalopathy. Chelators offer the metal a partner it binds more tightly, which is then excreted.",
  parts=[
    ('a', "**Binds sulfhydryl groups (blocks pyruvate dehydrogenase); garlic odour, rice-water diarrhoea, QT prolongation.** Blocking pyruvate dehydrogenase stops aerobic energy production; capillary damage in the gut causes profuse watery diarrhoea, and the long QT leads to torsades."),
    ('b', "**At 1–3 weeks an ascending axonal neuropathy that mimics GBS; Mees lines.** The neuropathy is sensorimotor and often painful; Mees lines are white transverse nail bands that appear weeks later."),
    ('c', "**24-h urine arsenic (blood clears within hours to days); chelate with dimercaprol, then DMSA or DMPS.** Arsenic leaves the blood quickly, so a blood level at the neuropathy stage is often normal while urine still shows it."),
    ('d', "**Dimercaprol first, then CaNa₂EDTA 4 h later; avoid LP and routine hyperventilation.** EDTA alone mobilises lead from tissues into the brain; dimercaprol first prevents this. Lead encephalopathy causes cerebral oedema, so lumbar puncture risks herniation."),
    ('e', "**Swallowed elemental (thermometer): harmless. Inhaled vapour: pneumonitis, ARDS, neurotoxicity.** Elemental mercury is barely absorbed from the gut but is absorbed well through the lungs."),
  ],
  mimic=[
    ("Arsenic neuropathy vs GBS", "Both ascend; arsenic follows a gastrointestinal illness with QT prolongation and later Mees lines — check urine arsenic."),
    ("Arsenic vs thallium", "Both give a painful neuropathy and Mees lines; thallium adds alopecia, including loss of the lateral eyebrows."),
  ],
  traps=[
    ("“Normal blood arsenic excludes poisoning”", "Blood clears in days; 24-hour urine is the test."),
    ("“EDTA alone for lead encephalopathy”", "It can move lead into the brain; dimercaprol goes first."),
  ],
  decode=[
    ("Hair loss, lateral eyebrow loss, behaviour change, nail lines [Marrow]", "Thallium."),
    ("Vomiting and diarrhoea, then 2 weeks later ascending weakness [pattern]", "Arsenic → 24-hour urine arsenic, dimercaprol."),
  ],
  punch="Metals poison by binding sulfhydryl groups and chelators offer them a better partner — but the route and the order of chelation decide whether that helps or harms.",
)

T['TX1-FE'] = dict(
  sub="Toxicology → Metals → Iron poisoning",
  intro="Iron tablets are common in homes, and in children they are a classic cause of death from overdose. Iron first damages the gut directly, then enters the circulation and cells, where free iron damages mitochondria. The stages follow that path, and the quiet middle stage is where patients are wrongly sent home.",
  parts=[
    ('a', "**Corrosive GI: vomiting, haematemesis, shock.** Iron is directly corrosive; fluid loss can cause early hypovolaemic shock. No gastrointestinal symptoms by 6 hours makes serious toxicity unlikely."),
    ('b', "**Latent — apparent recovery while iron enters cells: the dangerous reassurance.** Gut symptoms settle, but a persistent acidosis or tachycardia shows that toxicity is progressing."),
    ('c', "**Shock, high anion gap acidosis, hepatic necrosis, coagulopathy.** Free iron disrupts oxidative phosphorylation, so cells make lactate; the liver receives the iron first through the portal circulation."),
    ('d', "**Hepatic failure; gastric outlet stricture at 2–6 weeks.** The early corrosive injury heals with scarring that can obstruct the pylorus."),
    ('e', "**Not bound by charcoal (an ion) → whole bowel irrigation; tablets are radio-opaque; deferoxamine up to 15 mg/kg/h (vin-rosé urine), usually stopped by ~24 h (ARDS).** Deferoxamine chelates free iron into ferrioxamine, which the kidney excretes and which colours the urine. If AKI develops, haemodialysis removes the ferrioxamine complex — not the protein-bound iron — so chelation can continue."),
  ],
  mimic=[
    ("Iron vs lithium", "Neither is bound by charcoal and both get whole bowel irrigation; iron tablets are radio-opaque and give a corrosive gastroenteritis."),
  ],
  traps=[
    ("“Symptoms have settled at 12 hours, so discharge”", "That may be the latent stage; check acidosis and serum iron."),
    ("“Haemodialysis removes the iron”", "It removes ferrioxamine; the iron itself is bound and in tissues."),
    ("“Continue deferoxamine until the urine clears”", "Long infusions cause ARDS; usually stopped by about 24 hours."),
  ],
  decode=[
    ("Severe iron poisoning on deferoxamine develops AKI — role of haemodialysis? [DocT GT]", "Removes the ferrioxamine complex."),
    ("Iron reaction: mechanism of the drug needed [Marrow]", "Chelation."),
  ],
  punch="Iron burns the gut, then hides in cells: a quiet middle stage is not recovery, so judge by the acidosis, not by how the patient looks.",
)

T['TX1-CA'] = dict(
  sub="Toxicology → Corrosives → Caustic ingestion",
  intro="A patient has swallowed a strong acid or alkali. The burn to the pharynx and larynx swells over the following hours, so a patient who is talking now can obstruct later. Hoarseness, stridor and drooling show that the larynx is already involved.",
  parts=[
    ('a', "**Secure the airway early (fibreoptic or awake): laryngeal oedema worsens over hours.** Intubation gets harder as the oedema grows, and paralysing a patient with a distorted airway risks a can’t-intubate, can’t-oxygenate crisis, so spontaneous breathing is kept."),
    ('b', "**Endoscopy within 12–24 h for Zargar grading.** Grading predicts stricture and perforation; the healing wall is weakest from roughly day 5 to day 15, when endoscopy is most dangerous."),
    ('c', "**No emesis, no charcoal, no neutralisation, no blind NG tube.** Vomiting re-exposes the oesophagus, charcoal obscures endoscopy, neutralisation adds heat, and a blind tube can perforate."),
    ('d', "**No overall benefit; only a deep circumferential grade IIb burn may benefit — never grade III (masks perforation).** Trials show no overall fall in strictures; in grade III necrosis steroids add infection risk and hide the signs of perforation."),
  ],
  table=dict(title="Zargar grading", head=["Grade", "Finding"],
    rows=[["I", "Oedema and redness"], ["IIa", "Superficial ulcers, erosions"], ["IIb", "Deep or circumferential ulcers"], ["IIIa", "Scattered necrosis"], ["IIIb", "Extensive necrosis"]]),
  mimic=[],
  traps=[
    ("“No mouth burns, so no oesophageal injury”", "The oesophagus can be burned without visible oral injury."),
    ("“Neutralise the alkali with a weak acid”", "The reaction produces heat and worsens the burn."),
  ],
  decode=[
    ("Drooling and hoarseness after drinking drain cleaner [pattern]", "Secure the airway first."),
    ("Grade III on endoscopy — steroids? [pattern]", "No."),
  ],
  punch="A caustic burn of the larynx swells while the patient still looks well, so the airway is secured first and the endoscopy grades everything else.",
)

T['TX1-SK'] = dict(
  sub="Toxicology → Drug reactions → SJS/TEN vs DRESS",
  intro="Two severe drug reactions can bring a patient to the ICU with a rash and fever. SJS/TEN is widespread death of the epidermis and mucosa, behaving like a burn. DRESS is a delayed systemic hypersensitivity in which the internal organs carry the risk.",
  parts=[
    ('a', "**One spectrum by detachment: SJS <10% · overlap 10–30% · TEN >30% BSA.** The name depends only on the area of skin that detaches, and mortality rises with it."),
    ('b', "**SJS/TEN 4–28 days; DRESS 2–8 weeks.** DRESS appears later than almost any other drug rash, so the culprit is often a drug started a month or more before."),
    ('c', "**Eosinophilia with fever, facial oedema, nodes and organ involvement (liver most).** DRESS is a systemic hypersensitivity, so blood and organs are affected; hepatitis is the commonest organ injury."),
    ('d', "**SJS/TEN: involved. DRESS: usually spared.** Mucosal erosions of mouth, eyes and genitals are part of the epidermal necrosis of SJS/TEN."),
    ('e', "**SJS/TEN: stop the drug, burn-unit care (ciclosporin or IVIG may help). DRESS: stop the drug, steroids with a slow taper.** The immune reaction drives DRESS organ damage and relapses, hence the slow taper."),
  ],
  table=dict(title="Telling them apart", head=["Feature", "SJS/TEN", "DRESS"],
    rows=[["Onset after drug", "4–28 days", "2–8 weeks"], ["Mucosa", "Involved", "Usually spared"], ["Blood", "—", "Eosinophilia"], ["Organs", "Skin failure", "Liver, kidney, lung"], ["Treatment", "Burn care", "Steroids, slow taper"]]),
  mimic=[],
  traps=[
    ("“The rash began 5 weeks after the drug, so it is not drug-induced”", "DRESS typically appears at 2–8 weeks."),
  ],
  decode=[
    ("Carbamazepine started 5 weeks ago; fever, facial oedema, eosinophilia, raised ALT [pattern]", "DRESS → stop drug, steroids."),
    ("10 days after a new drug, oral erosions, 40% detachment [pattern]", "TEN → burn unit."),
  ],
  punch="Timing and blood separate them: early skin and mucosal necrosis is SJS/TEN and is treated as a burn; late fever, eosinophils and organ injury is DRESS and is treated with a slow steroid taper.",
)

T['TX1-QN'] = dict(
  sub="Toxicology → Sodium-channel blockers → Quinine",
  intro="Quinine is still used for malaria and, in some places, for cramps. In overdose it behaves like other sodium-channel blockers on the heart, but it also damages the retina and stimulates insulin release.",
  parts=[
    ('a', "**Cinchonism: tinnitus, deafness, nausea, headache.** The first sign of toxicity, even at high therapeutic levels."),
    ('b', "**Blindness at 6–12 h, fixed dilated pupils.** Quinine is directly toxic to the retina."),
    ('c', "**Na⁺-channel block: wide QRS, VT → bicarbonate.** Like tricyclics, quinine slows ventricular conduction; bicarbonate reduces drug binding to the channel."),
    ('d', "**Hypoglycaemia (quinine releases insulin).** Low glucose can add to coma and seizures, so it is checked repeatedly."),
    ('e', "**Multi-dose charcoal; dialysis does not help.** Repeated charcoal draws quinine back into the gut and shortens its half-life; quinine is widely distributed and protein-bound, so dialysis removes little. It is not a whole bowel irrigation drug."),
  ],
  mimic=[
    ("Quinine vs tricyclic overdose", "Both widen the QRS and respond to bicarbonate; quinine adds blindness, tinnitus and hypoglycaemia."),
  ],
  traps=[
    ("“Whole bowel irrigation or dialysis for quinine”", "Multi-dose charcoal is the elimination method."),
  ],
  decode=[
    ("Whole bowel irrigation indications EXCEPT [Marrow]", "Quinine overdose (multi-dose charcoal instead)."),
    ("Overdose with tinnitus, then sudden blindness [pattern]", "Quinine."),
  ],
  punch="Quinine is a sodium-channel blocker with two extras: it blinds and it releases insulin, so give bicarbonate for the QRS, glucose for the sugar, and charcoal, not dialysis.",
)

T['TX1-AS'] = dict(
  sub="Toxicology → Sodium-channel blockers → Antiseizure drug overdose",
  intro="Lamotrigine and carbamazepine control seizures by blocking neuronal sodium channels. In overdose the same block appears in the heart, and, paradoxically, the brain can start seizing. Treating these seizures means choosing drugs that do not add more sodium-channel block.",
  parts=[
    ('a', "**At toxic levels the Na⁺ block silences inhibitory interneurons → paradoxical seizures.** The proposed explanation: fast-firing inhibitory interneurons depend most on sodium channels and are suppressed first, releasing excitatory neurons."),
    ('b', "**Wide QRS — the same block in the heart.** Cardiac sodium channels conduct the impulse through the ventricles, so blocking them widens the QRS and risks VT."),
    ('c', "**Benzodiazepines, then phenobarbital or propofol.** These act on GABA-A receptors; phenytoin is avoided because it is itself a sodium-channel blocker."),
    ('d', "**Bicarbonate; lipid if refractory.** Raising extracellular sodium and pH reduces drug binding and narrows the QRS."),
  ],
  mimic=[
    ("Antiseizure drug vs tricyclic overdose", "Both cause wide QRS and seizures and respond to bicarbonate; carbamazepine is structurally a tricyclic and also anticholinergic."),
  ],
  traps=[
    ("“Seizures in overdose mean the antiseizure level is low”", "In toxicity the drug itself causes seizures."),
    ("“Phenytoin for the seizures”", "It is another sodium-channel blocker."),
  ],
  decode=[
    ("Somnolent, carbamazepine 45 µg/mL after a new drug was added — which drug? [Marrow]", "Diltiazem (CYP3A4 inhibition)."),
    ("Lamotrigine overdose, seizure, QRS 130 ms [pattern]", "Benzodiazepine and sodium bicarbonate."),
  ],
  punch="Too much sodium-channel block silences the brain’s brakes and slows the heart, so treat with GABA drugs and bicarbonate, never another sodium-channel blocker.",
  extra=[dict(q="Carbamazepine: what tips a stable patient into toxicity?", a="**CYP3A4 inhibitors** — diltiazem, verapamil, macrolides, isoniazid; severe toxicity above **40 µg/mL**.")],
)

T['TX1-INH'] = dict(
  sub="Toxicology → Seizures → Isoniazid overdose",
  intro="A patient on tuberculosis treatment is seizing, and the seizures do not stop with a benzodiazepine. Isoniazid in overdose depletes the vitamin the brain needs to make its main inhibitory transmitter, so until it is replaced the usual anticonvulsants have little to act on.",
  parts=[
    ('a', "**Isoniazid — give pyridoxine with the benzodiazepine: gram for gram, or 5 g IV if the amount is unknown.** Isoniazid depletes pyridoxal phosphate, the cofactor of glutamic acid decarboxylase, which makes GABA. With little GABA the brain seizes and benzodiazepines have too little GABA to enhance; pyridoxine restores synthesis, and the two together stop the seizures. The acidosis is lactic, mainly from the seizures."),
    ('b', "**Phenytoin does not work.** It acts on sodium channels and does nothing for the GABA deficit."),
  ],
  mimic=[],
  traps=[
    ("“More benzodiazepine will eventually work”", "Without pyridoxine there is too little GABA to enhance."),
  ],
  decode=[
    ("TB patient, refractory seizures, high anion gap acidosis [pattern]", "Isoniazid → pyridoxine (5 g IV if amount unknown)."),
  ],
  punch="Isoniazid takes away the vitamin B6 that GABA synthesis depends on, so GABA drugs fail until pyridoxine is replaced.",
)

T['TX1-RAD'] = dict(
  sub="Toxicology → Physical agents → Acute radiation syndrome",
  intro="After whole-body radiation, cells that divide rapidly die first, because radiation damages DNA and the damage shows when a cell tries to divide. The dose therefore decides which tissue fails: marrow at the lowest dose, then gut lining, and at very high doses the nervous system and blood vessels.",
  parts=[
    ('a', "**Haematopoietic: marrow nadir at 2–4 weeks; the 48-h lymphocyte count estimates the dose.** Mature blood cells in circulation survive their normal lifespan, so counts fall over weeks; lymphocytes die directly from radiation, so their fall over 48 hours tracks the dose."),
    ('b', "**Gastrointestinal: vomiting, diarrhoea, sepsis within days.** The crypt cells that renew the gut lining are destroyed."),
    ('c', "**Neurovascular (signs from ~20 Gy, full syndrome >~50 Gy): collapse within hours; uniformly fatal.** Vascular and neuronal damage causes oedema, hypotension and collapse; care is palliative."),
    ('d', "**Vomiting within 1 hour.** The prodrome comes earlier with higher doses; vomiting within an hour suggests roughly 4 Gy or more."),
  ],
  table=dict(title="Dose to syndrome", head=["Dose", "Syndrome", "Timing"],
    rows=[[">1 Gy", "Haematopoietic", "Nadir 2–4 weeks"], [">6 Gy", "Gastrointestinal", "Days"], ["≥20 Gy", "Neurovascular", "Hours"]]),
  mimic=[],
  traps=[
    ("“Platelets and neutrophils fall first”", "Lymphocytes fall first, within 48 hours; they estimate the dose."),
  ],
  decode=[
    ("Best early laboratory estimate of dose [pattern]", "Absolute lymphocyte count at 24–48 hours."),
    ("Radiation accident, vomiting at 30 minutes [pattern]", "High dose — expect marrow failure."),
  ],
  punch="The faster a tissue divides, the lower the dose that kills it: marrow first, then gut lining, then nerves and vessels, and how soon the patient vomits shows how high the dose was.",
)

FLAGS = {
  'TX1-ALC': "Card d lists clinical dialysis triggers only. EXTRIP/standard texts also dialyse on level (e.g. methanol >50 mg/dL, or >70 mg/dL with fomepizole) and on severe acidosis thresholds (pH ≤7.15–7.25) — consider adding the level criterion, which MCQs test. DocT GT keys dialysis for ethylene glycol 45 mg/dL with pH 7.10 and AKI.",
  'TX1-SAT': "Card e lists the common HBO criteria; the evidence for HBO in CO is contested and criteria vary (some add pH <7.1 or COHb >20% in pregnancy elsewhere). Card statement kept; fine for exam use.",
  'TX1-CA': "Card b says endoscopy within 12–24 h; most texts allow up to 48 h and say avoid roughly days 5–15 (tissue weakest). Kept card window; the text mentions the risk rising after ~48 h.",
  'TX1-AS': "Card a gives the interneuron-silencing mechanism as fact; it is a proposed explanation rather than established. Also worth adding: severe carbamazepine poisoning is an EXTRIP indication for high-flux haemodialysis, and MDAC is used.",
  'TX1-FE': "Stage timings vary by source (stage 3 often given as 6–72 h; stricture at 2–8 weeks). Card values kept. Deferoxamine indications (serum iron >500 µg/dL, shock, acidosis, altered consciousness) are not on the card and are commonly tested.",
  'TX1-RAD': "Card a says haematopoietic syndrome '>1 Gy'; many sources place clinically significant H-ARS at 2–6 Gy (prodrome from ~1 Gy). Card kept. Vomiting-within-1-h dose (~4 Gy+) was added from IAEA-style time-to-emesis tables.",
  'TX1-QT': "Card c says stop the CYP3A4 inhibitor first; DocT GT (ciprofloxacin + amitriptyline + aripiprazole, no CYP3A4 inhibitor offered) keys stopping the strongest hERG blocker. Consider adding ‘otherwise the strongest hERG blocker’. Explanation adds it.",
}
