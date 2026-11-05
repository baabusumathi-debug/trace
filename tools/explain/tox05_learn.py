# TOX05 — Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Management of Snake Bite (SNAKE-01 to SNAKE-16). Same fields as TOX01.
L = {}

L['SNAKE-01'] = dict(
  sub="Toxicology → Snakes & Venom → The size of the problem",
  intro="Snakebite in India is a rural, night-time, farm-work injury, and most victims never reach a doctor in time. Most bites turn out harmless, either because the snake was not venomous or because a venomous snake injected nothing. The numbers matter clinically: they explain why every bite is observed rather than treated blindly, and why antivenom must reach the primary health centre rather than wait in the city.",
  parts=[
    ('a', "**35,000–50,000 deaths per year (WHO), the highest in the world.** India has a dense rural population working barefoot in fields, sleeping on the floor, and living among the four commonest dangerous species. Because many deaths happen at home and are never registered, every count is an underestimate: the Indian Standard Treatment Guidelines (2017) estimate about 45,900 deaths a year, and the household-survey Million Death Study about 58,000."),
    ('b', "**70% of bites are non-venomous, and 50% of venomous bites are dry.** A snake controls whether it injects venom, and a defensive strike often delivers none. This is why the bite alone is never an indication for antivenom (SNAKE-12): treatment waits for evidence of envenoming."),
    ('c', "**About 34% of proven bites develop systemic envenoming.** Even when the snake is venomous, only a minority inject enough venom to reach the circulation and cause bleeding, paralysis, shock or kidney injury. The rest have no signs or local signs only, which is why every bite is watched for 24 hours (SNAKE-09) before it is called harmless."),
    ('d', "**Most deaths occur before reaching hospital.** Neurotoxic bites can stop breathing within hours, and delay is lengthened by distance, night-time bites, and time lost with traditional healers and harmful first aid. Once a patient is in hospital with antivenom and a ventilator, most survive."),
  ],
  mimic=[
    ("Dry bite vs delayed envenoming", "A dry bite stays normal for 24 hours. Krait envenoming can look like nothing for several hours before ptosis appears — hence the full observation period."),
  ],
  traps=[
    ("“Every snakebite needs antivenom”", "Most bites are non-venomous or dry; antivenom is given only for signs of envenoming."),
    ("“No symptoms at 1 hour, so it was a dry bite”", "Krait paralysis and viper coagulopathy can appear hours later; observe for at least 24 hours."),
    ("“Most deaths occur in hospital from antivenom reactions”", "Most die before reaching hospital, from untreated envenoming."),
  ],
  decode=[
    ("Snakebite deaths in India per year", "35,000–50,000 (WHO); highest in the world."),
    ("Proportion of venomous bites that are dry", "About 50%."),
    ("Where do most snakebite deaths occur?", "Before reaching hospital."),
  ],
  punch="Most bites never inject venom, so the bite is watched, not treated — but those that do envenom kill mostly on the way to hospital, so speed of transport and antivenom near the patient save lives.",
)

L['SNAKE-02'] = dict(
  sub="Toxicology → Snakes & Venom → Families and the big four",
  intro="Venomous snakes fall into families whose venoms do broadly different things: elapids mainly paralyse, vipers mainly disturb clotting and damage tissue. In India four species cause most deaths, and the national antivenom is raised against exactly those four. A snake outside that list may envenom a patient whom the antivenom cannot help.",
  parts=[
    ('a', "**Elapidae — cobras, kraits (also king cobra, coral snakes): neurotoxic.** Elapids have short fixed front fangs and venoms rich in small neurotoxins that block the neuromuscular junction, so the danger is descending paralysis and respiratory failure (SNAKE-04, 07)."),
    ('b', "**Viperidae — true vipers (Russell’s, saw-scaled) and pit vipers (hump-nosed, Malayan): haemotoxic.** Vipers have long, hinged fangs and venoms full of enzymes that consume clotting factors and damage vessel walls, so they cause local swelling, bleeding, shock and kidney injury. Pit vipers carry a heat-sensing pit between eye and nostril."),
    ('c', "**Hydrophidae — sea snakes: myotoxic.** Their venom breaks down skeletal muscle, giving muscle pain, myoglobinuria and kidney injury; sea snake venom is also neurotoxic. The bite itself is usually painless, with little local reaction."),
    ('d', "**Common cobra (Naja naja), common krait (Bungarus caeruleus), Russell’s viper (Daboia russelii), saw-scaled viper (Echis carinatus).** These four are widespread, live close to people and cause most bites and deaths, so Indian polyvalent antivenom is made by immunising horses with their venoms. Its antibodies recognise these venoms and not others, which is why a hump-nosed pit viper bite does not respond."),
  ],
  table=dict(title="Family to main effect", head=["Family", "Indian examples", "Main effect"], rows=[["Elapidae", "cobra, krait, king cobra", "**neurotoxic**"], ["Viperidae", "Russell’s, saw-scaled, hump-nosed", "**haemotoxic**, local damage"], ["Sea snakes", "—", "**myotoxic** (and neurotoxic)"]]),
  mimic=[
    ("Russell’s viper vs hump-nosed pit viper", "Both give local swelling, coagulopathy and kidney injury; only Russell’s viper is covered by Indian antivenom."),
    ("Cobra vs king cobra", "Both elapids with local necrosis and paralysis; the king cobra is not one of the big four and is not covered by the polyvalent antivenom."),
  ],
  traps=[
    ("“Polyvalent antivenom covers all Indian venomous snakes”", "It covers only the big four; hump-nosed pit viper and king cobra are not covered."),
    ("“The krait is a viper because it bites at night”", "The krait is an elapid: neurotoxic, with almost no local signs."),
  ],
  decode=[
    ("Which snake is NOT one of the big four?", "Hump-nosed pit viper or king cobra."),
    ("Viper bite with coagulopathy not responding to antivenom", "Hump-nosed pit viper."),
    ("Sea snake bite, muscle pain, dark urine", "Myotoxicity — rhabdomyolysis and myoglobinuria."),
  ],
  punch="Elapids paralyse and vipers make the blood unclottable; Indian antivenom is raised against only the big four, so a snake outside that list may envenom a patient the antivenom cannot help.",
)

L['SNAKE-03'] = dict(
  sub="Toxicology → Snakes & Venom → What the venom contains",
  intro="Venom is modified saliva, and more than 90% of its dry weight is protein — enzymes and small toxins, each with its own target. The clinical picture of a bite is simply the sum of what each component does. Knowing the components explains why vipers bleed, why cobras necrose and why kraits paralyse without a mark on the skin.",
  parts=[
    ('a', "**Metalloproteinases damage the endothelial basement membrane: capillary leak, bleeding, shock.** These zinc-dependent enzymes digest the collagen and matrix that hold capillary walls together. Red cells and plasma escape through the damaged wall, giving local swelling and blistering, bleeding from gums and wounds, and hypovolaemic shock."),
    ('b', "**Procoagulant enzymes activate clotting: consumption coagulopathy (DIC-like).** Russell’s viper venom activates factors X and V, and saw-scaled viper venom activates prothrombin. Clotting is triggered throughout the blood until fibrinogen and factors are used up, and the blood becomes unclottable — the basis of the 20-minute clotting test (SNAKE-09). It is called DIC-like because it is consumption by venom, not sepsis or tissue factor."),
    ('c', "**Phospholipase A₂: myotoxicity, presynaptic neurotoxicity, mitochondrial damage.** This enzyme breaks down membrane phospholipids. In muscle it causes rhabdomyolysis; at the motor nerve terminal it destroys the terminal itself (β-bungarotoxin of the krait is a phospholipase A₂), which is why krait paralysis lasts and does not respond to neostigmine (SNAKE-04)."),
    ('d', "**Hyaluronidase: the spreading factor, with tissue destruction.** It breaks down hyaluronic acid in the connective tissue, opening a path for the other toxins to spread from the bite. The necrosis itself comes mainly from the enzymes and cytotoxins that hyaluronidase lets through."),
    ('e', "**Polypeptide neurotoxins block the neuromuscular junction.** These small toxins (the α-neurotoxins of cobras) bind the postsynaptic nicotinic acetylcholine receptor and stop acetylcholine from acting. The nerve terminal is intact, so more acetylcholine — neostigmine — can compete them off."),
  ],
  mimic=[
    ("Presynaptic vs postsynaptic neurotoxin", "Presynaptic (phospholipase A₂, krait) destroys the nerve terminal; postsynaptic (α-neurotoxin, cobra) blocks the receptor and can be overcome by more acetylcholine."),
    ("Venom coagulopathy vs septic DIC", "Venom consumes factors directly and is reversed by antivenom; septic DIC follows tissue factor release and is treated by treating the infection."),
  ],
  traps=[
    ("“Give FFP to correct the venom coagulopathy”", "Free venom consumes the new factors too; antivenom first, FFP only afterwards (SNAKE-16)."),
    ("“Venom is mainly lipid”", "More than 90% of it is protein, which is why horse antibodies can neutralise it."),
  ],
  decode=[
    ("Venom enzyme causing consumption coagulopathy", "Procoagulant enzymes (factor X, V and prothrombin activators)."),
    ("Spreading factor of venom", "Hyaluronidase."),
    ("Toxin behind krait paralysis", "Presynaptic phospholipase A₂ (β-bungarotoxin)."),
  ],
  punch="Each venom protein has one target — the vessel wall, the clotting cascade, the cell membrane, the connective tissue or the acetylcholine receptor — and the bite’s picture is their sum.",
)

L['SNAKE-04'] = dict(
  sub="Toxicology → Snakes & Venom → Cobra vs krait neurotoxicity",
  intro="Cobras and kraits both paralyse, from the eyelids downwards, but they attack the neuromuscular junction from opposite sides. The cobra blocks the receptor on the muscle; the krait destroys the nerve terminal that releases acetylcholine. That one difference explains the local signs, the timing, the response to neostigmine and the length of ventilation.",
  parts=[
    ('a', "**Toxin site: cobra postsynaptic (α-neurotoxin); krait presynaptic (β-bungarotoxin).** The α-neurotoxin sits on the nicotinic receptor like a competitive blocker. β-bungarotoxin is a phospholipase A₂ that enters the nerve terminal, first causing a burst of release and then exhausting and destroying it."),
    ('b', "**Local reaction: cobra swelling and necrosis; krait virtually painless, none.** Cobra venom contains cytotoxins that kill tissue at the bite, so the limb is painful and swollen and may necrose. Krait venom has almost no local toxins and the fangs are small, so the bite may not even be noticed."),
    ('c', "**Onset: cobra early, within 30 minutes; krait delayed, with prolonged paralysis.** A receptor block acts as soon as toxin reaches the junction. Presynaptic damage takes hours to show, and recovery needs a new nerve terminal to grow, so paralysis can last days to weeks."),
    ('d', "**Neostigmine: cobra responds; krait does not.** Neostigmine raises acetylcholine in the cleft, which competes the α-neurotoxin off the receptor. With a destroyed terminal there is no acetylcholine to increase (SNAKE-10)."),
    ('e', "**Typical story: cobra — painful swollen bite; krait — bitten asleep on the floor at night, with abdominal pain.** Kraits hunt at night and enter houses, so the victim is bitten while sleeping and wakes with abdominal pain, then ptosis by morning, with no mark to explain it."),
  ],
  table=dict(title="Opposite sides of one junction", head=["", "Cobra", "Krait"], rows=[["Target", "postsynaptic receptor", "presynaptic terminal"], ["Local signs", "swelling, necrosis", "none"], ["Onset", "early", "delayed"], ["Neostigmine", "**responds**", "**no response**"], ["Ventilation", "shorter", "days to weeks"]]),
  mimic=[
    ("Krait bite vs Guillain–Barré or stroke", "Sudden ptosis and bulbar palsy at dawn in a rural patient who slept on the floor, with no bite mark, is krait until proven otherwise."),
  ],
  traps=[
    ("“No bite mark and no swelling, so not envenomed”", "Krait bites are painless and leave little trace; watch for ptosis."),
    ("“Neostigmine failed, so antivenom is useless”", "Antivenom is still given in krait bites to neutralise venom still circulating, though it cannot repair terminals already damaged."),
    ("“SpO₂ is normal on oxygen, so the paralysed patient is safe”", "Oxygen hides a rising CO₂; ventilatory failure needs intubation, not more oxygen."),
  ],
  decode=[
    ("Woke at night with abdominal pain, ptosis by morning, no local swelling", "Common krait."),
    ("Painful swollen bite, then ptosis within an hour, improves with neostigmine", "Cobra."),
    ("Toxin of krait", "β-bungarotoxin — presynaptic."),
  ],
  punch="The cobra blocks the receptor, so more acetylcholine wins and recovery is quick; the krait destroys the terminal, so neostigmine has nothing to work with and the patient needs the ventilator until the nerve regrows.",
  extra=[dict(q="Krait bite: when to intubate?", a="**Early** — for bulbar palsy with pooled secretions, neck-flexor weakness, paradoxical breathing, a falling single-breath count, or a **rising PaCO₂**. Oxygen alone masks hypoventilation.")],
)

L['SNAKE-05'] = dict(
  sub="Toxicology → Clinical Syndromes → WHO syndromic approach",
  intro="Most patients never see the snake, or bring a description that cannot be trusted. The WHO approach turns the question round: instead of identifying the snake to predict the illness, it reads the illness to name the snake. Three questions do most of the work — is there local swelling, is the blood clotting, and is there paralysis?",
  parts=[
    ('a', "**Syndrome 1 — local envenoming with bleeding: Viperidae.** Swelling plus incoagulable blood means a viper, because procoagulant and haemorrhagic enzymes are the vipers’ hallmark (SNAKE-03)."),
    ('b', "**Syndrome 2 — as syndrome 1 plus shock or AKI, conjunctival oedema, pituitary failure; or plus ptosis and dark urine: Russell’s viper.** Russell’s venom adds vasodilating and nephrotoxic effects; in Myanmar it also causes chemosis and infarction of the anterior pituitary. In South India and Sri Lanka it carries a presynaptic phospholipase A₂, giving ptosis, and haemolysis or rhabdomyolysis turns the urine dark."),
    ('c', "**Syndrome 3 — local envenoming with paralysis: cobra.** Only cobras combine cytotoxic necrosis at the bite with neurotoxic paralysis; WHO lists cobra or king cobra here, and the king cobra is not one of the big four."),
    ('d', "**Syndrome 4 — paralysis with minimal local signs: krait (on land, asleep) or sea snake (in water).** Both venoms are neurotoxic with almost no local toxins; the place of the bite separates them."),
    ('e', "**Syndrome 5 — paralysis with dark urine and AKI: Russell’s viper; sea snake.** Paralysis and kidney injury together mean a venom that is both neurotoxic and myotoxic or haemolytic, so muscle or red cells break down and the pigment injures the tubules. The clotting test separates the two: a land bite with incoagulable blood is Russell’s viper (South India, Sri Lanka), a sea bite with normal clotting is a sea snake. WHO also lists kraits of Bangladesh and Thailand here, but not the Indian common krait."),
  ],
  table=dict(title="Three questions name the snake", head=["Local swelling", "Bleeding", "Paralysis", "Snake"], rows=[["yes", "yes", "no", "viper"], ["yes", "yes", "± ptosis, dark urine, AKI, shock", "Russell’s viper"], ["yes", "no", "yes", "cobra"], ["no", "no", "yes", "krait (land) / sea snake"]]),
  mimic=[
    ("Syndrome 3 vs 4", "Both paralyse; local swelling and necrosis mean cobra, a clean bite site means krait."),
  ],
  traps=[
    ("“Wait for the snake to be identified before giving antivenom”", "The syndrome is enough; polyvalent antivenom covers all four, so the species need not be known."),
    ("“Ptosis rules out a viper”", "Russell’s viper in South India and Sri Lanka can cause ptosis, with coagulopathy and dark urine."),
  ],
  decode=[
    ("Swelling, bleeding gums, oliguria", "Russell’s viper (syndrome 2)."),
    ("Ptosis, no swelling, bitten asleep on the floor", "Krait (syndrome 4)."),
    ("Necrosing bite with paralysis", "Cobra (syndrome 3)."),
  ],
  punch="Read the patient, not the snake: swelling with bleeding is a viper, swelling with paralysis a cobra, paralysis on a clean bite a krait — and Russell’s viper adds shock, kidney injury and sometimes ptosis.",
)

L['SNAKE-06'] = dict(
  sub="Toxicology → Clinical Syndromes → Features by species",
  intro="This table is the syndromic approach laid out snake by snake. Each column is the venom’s chemistry seen at the bedside: cytotoxins give local damage, neurotoxins give paralysis, procoagulants give coagulopathy, and the nephrotoxic Russell’s venom gives kidney failure. Only one box separates cobra from krait in the treatment column — neostigmine.",
  parts=[
    ('a', "**Local damage: cobra yes, krait no, Russell’s yes, saw-scaled yes.** Cobra cytotoxins and viper metalloproteinases destroy tissue at the bite. The krait’s venom has almost none, so a clean bite site with paralysis points to a krait."),
    ('b', "**Ptosis and paralysis: cobra yes, krait yes, Russell’s sometimes, saw-scaled no.** The elapids paralyse; Russell’s viper does so only in some regions (presynaptic phospholipase A₂). The saw-scaled viper is purely haemotoxic."),
    ('c', "**Coagulopathy: cobra no, krait no (may occur), Russell’s yes, saw-scaled yes.** Viper procoagulants consume clotting factors (SNAKE-03), so a positive 20WBCT points to a viper and away from the elapids."),
    ('d', "**Renal failure: only Russell’s viper.** Russell’s venom injures the kidney directly and through haemolysis, rhabdomyolysis, shock and DIC, producing acute tubular necrosis (SNAKE-07). The saw-scaled viper bleeds but seldom damages the kidney."),
    ('e', "**Neostigmine: only the cobra.** Its postsynaptic block can be overcome by more acetylcholine; the krait and Russell’s viper act presynaptically (SNAKE-10)."),
    ('f', "**Antivenom: all four.** Polyvalent antivenom is raised against each of the big four, so all respond — unlike the hump-nosed pit viper, which looks like a Russell’s bite but is not covered."),
  ],
  mimic=[
    ("Russell’s vs saw-scaled viper", "Both cause swelling and coagulopathy; kidney failure (and ptosis in some regions) points to Russell’s."),
    ("Russell’s vs hump-nosed pit viper", "Same picture of local damage, coagulopathy and AKI; hump-nosed does not respond to Indian antivenom."),
  ],
  traps=[
    ("“Coagulopathy can be a cobra bite”", "Indian cobra venom does not cause coagulopathy; a positive 20WBCT means a viper."),
    ("“Saw-scaled viper causes paralysis”", "It is purely haemotoxic."),
    ("“Neostigmine helps any neurotoxic bite”", "Only postsynaptic (cobra) paralysis responds."),
  ],
  decode=[
    ("Coagulopathy plus AKI", "Russell’s viper."),
    ("Neostigmine-responsive paralysis", "Cobra."),
    ("Viper picture, no response to adequate antivenom", "Hump-nosed pit viper."),
  ],
  punch="Every box follows from the venom: cytotoxins give local damage, procoagulants give bleeding, neurotoxins give paralysis — and only the cobra’s postsynaptic block lets neostigmine work.",
)

L['SNAKE-07'] = dict(
  sub="Toxicology → Clinical Syndromes → What kills, and the brain-death trap",
  intro="Systemic envenoming kills in two different ways. Vipers make the blood unclottable and the vessels leaky, so the patient bleeds where it does most harm and the kidneys fail. Elapids paralyse from the head down until the breathing muscles stop. A fully paralysed patient can look dead while wide awake — the most dangerous misjudgement in the snakebite ward.",
  parts=[
    ('a', "**Viper bite deaths: intracranial bleeding, anterior pituitary haemorrhage, multi-organ failure.** Incoagulable blood plus vessel damage lets a small bleed in the brain expand. Russell’s venom can cause haemorrhagic infarction of the anterior pituitary: acutely shock and hypoglycaemia from adrenal insufficiency, and months to years later chronic hypopituitarism (loss of body hair, amenorrhoea or testicular atrophy, hypothyroidism). Shock, AKI and DIC together give multi-organ failure."),
    ('b', "**Neurotoxic paralysis is descending: ptosis, ophthalmoplegia, bulbar weakness, then respiratory muscles.** The small, fast-firing motor units of the eye and face have the least safety margin at the neuromuscular junction, so they fail first. Bulbar weakness then threatens the airway, and the diaphragm fails last."),
    ('c', "**Locked-in state mimics brain death: fixed dilated pupils and no movement, yet conscious. Never diagnose brain death.** Venom blocks the neuromuscular junction, including the eye muscles and the iris, but not the brain. The patient can hear everything, so is sedated and spoken to, and brainstem death testing is invalid until the toxin has gone."),
    ('d', "**Acute tubular necrosis is the commonest renal lesion.** Shock, haemoglobin and myoglobin pigments, microthrombi from consumption coagulopathy and direct venom toxicity all injure the tubular cells. Cortical necrosis is less common and carries a worse outlook."),
  ],
  mimic=[
    ("Locked-in envenoming vs brain death", "Both: fixed pupils, no movement, apnoea. Envenoming is a junction block in a conscious brain — the EEG is active and recovery is expected."),
  ],
  traps=[
    ("“Fixed dilated pupils in a krait bite mean brain death”", "Paralysis of the iris and every muscle mimics it; never certify brain death in neurotoxic envenoming."),
    ("“Russell’s viper AKI will settle with fluids”", "Pigment, DIC and direct toxicity rarely reverse on fluid alone; repeat antivenom if still incoagulable and start renal replacement early."),
    ("“Steroids help venom AKI”", "They have no role."),
  ],
  decode=[
    ("Viper bite, sudden headache and coma", "Intracranial haemorrhage."),
    ("Recovered from Russell’s bite, later amenorrhoea and hypotension", "Anterior pituitary haemorrhage — hypopituitarism."),
    ("Ventilated krait patient, fixed pupils, no movement", "Locked-in state, not brain death."),
  ],
  punch="Vipers kill by bleeding and kidney failure, elapids by descending paralysis — and a paralysed patient can look brain-dead while fully aware, so brain death is never diagnosed in envenoming.",
  extra=[dict(q="Russell’s viper, oliguric AKI, blood still incoagulable: management?", a="**Repeat antivenom** (venom still active) **and early renal replacement therapy**; FFP only after antivenom; no steroids.")],
)

L['SNAKE-08'] = dict(
  sub="Toxicology → First Aid & Tests → First aid",
  intro="First aid for a snakebite has two aims: slow the spread of venom through the lymphatics, and get the patient to antivenom quickly. Venom travels mainly through lymph, which moves when the muscles of the limb contract. Most traditional measures do neither and add harm, especially in viper bites where the tissue is already being destroyed.",
  parts=[
    ('a', "**Do: reassure, immobilise the limb like a fracture, carry the patient (no walking), get to hospital.** Fear raises heart rate and makes the patient run; immobility stops the muscle pump that drives lymph and venom towards the circulation. Walking does the opposite. The definitive treatment is antivenom, so transport is the most important step."),
    ('b', "**Do not: tourniquet, cutting or sucking, ice, electric shock.** A tight tourniquet traps venom in an ischaemic limb, worsening necrosis and gangrene, and releases it in a bolus when removed. Cutting causes bleeding in a coagulopathic patient and infection; suction removes no useful venom; ice and electric shock damage tissue and achieve nothing."),
    ('c', "**Pressure immobilisation is controversial; only for purely neurotoxic bites, and not so tight as to stop perfusion.** A firm crepe bandage compresses the lymphatics and slows spread, which matters most for elapid venom that kills by paralysis and does little local damage. The worry in viper bites, which are most Indian bites, is that holding a tissue-destroying venom in the limb may worsen local necrosis. WHO 2016 favours pressure-pad immobilisation for suspected elapid bites, and the Indian Standard Treatment Guidelines (2017) allow a crepe bandage only when applied by trained staff and the hospital is 30 minutes to 3 hours away."),
  ],
  mimic=[
    ("Pressure immobilisation vs tourniquet", "The bandage compresses lymphatics but keeps the arterial supply; a tourniquet stops blood flow and causes ischaemia."),
  ],
  traps=[
    ("“Apply a pressure-immobilisation bandage to every snakebite”", "It comes from Australian elapid practice; in India most bites are vipers, so the default is splinting without a tight bandage, and a crepe bandage is left to trained staff."),
    ("“Remove the tourniquet at once”", "Sudden release can flood the circulation with venom; remove it only once antivenom has started and resuscitation is ready — check the distal pulse, apply a proximal cuff, remove the tourniquet, then deflate slowly."),
    ("“Incise and suck the wound”", "It removes nothing useful and causes bleeding and infection."),
  ],
  decode=[
    ("First aid in an Indian snakebite", "Reassure, immobilise, carry to hospital — no tourniquet."),
    ("Patient arrives with a tight tourniquet", "Check pulse, proximal cuff, remove tourniquet, slow deflation, antivenom ready."),
  ],
  punch="Keep the limb still so the lymph — and the venom — stops moving, and move the patient to antivenom instead; everything that cuts, ties or freezes the limb only adds injury.",
)

L['SNAKE-09'] = dict(
  sub="Toxicology → First Aid & Tests → 20-minute whole blood clotting test",
  intro="Viper venom consumes fibrinogen and clotting factors until the blood cannot clot. The 20-minute whole blood clotting test checks this at the bedside with only a glass tube and a clock, so a peripheral health centre can decide on antivenom without a laboratory. It relies on glass activating the contact pathway of coagulation.",
  parts=[
    ('a', "**A few mL of venous blood in a new, clean, dry glass tube, left undisturbed for 20 minutes, then tilted.** The glass surface activates factor XII and starts the intrinsic pathway; normal blood forms a firm clot well within 20 minutes. Disturbing the tube early breaks a forming clot and gives a false result."),
    ('b', "**Still liquid = coagulopathy = viper bite, and an indication for antivenom.** If fibrinogen has been consumed, no clot can form however long you wait. Indian cobras and kraits do not cause coagulopathy, so an unclotted tube points to a viper."),
    ('c', "**Plastic tubes, or glass washed with detergent, give false results.** Plastic does not activate the contact pathway, so normal blood stays liquid — a false positive. Detergent coats the glass and has the same effect."),
    ('d', "**Every 30 minutes for 3 hours, then hourly; and 6 hours after antivenom. Observe every bite for at least 24 hours.** Coagulopathy can appear hours after the bite, so a single normal test excludes nothing. After antivenom the liver needs about 6 hours to make new clotting factors, so testing sooner would mislead (SNAKE-13)."),
  ],
  mimic=[
    ("20WBCT vs PT/INR", "Both detect venom coagulopathy; 20WBCT needs no laboratory, and PT or INR (INR >1.2) is used where available (SNAKE-12)."),
  ],
  traps=[
    ("“Use any clean tube — plastic is fine”", "Plastic does not activate clotting; only new, clean, dry glass."),
    ("“Repeat the test 1 hour after antivenom”", "The liver needs about 6 hours to restore clotting factors."),
    ("“Normal test on arrival — discharge”", "Repeat for 3 hours, then hourly; observe 24 hours."),
  ],
  decode=[
    ("Blood still liquid at 20 minutes", "Viper coagulopathy — give antivenom."),
    ("When to repeat 20WBCT after antivenom?", "At 6 hours."),
    ("False positive 20WBCT", "Plastic or detergent-washed tube."),
  ],
  punch="Glass starts clotting, so normal blood clots within 20 minutes; liquid blood means the venom has used up the factors — and because the liver needs 6 hours to replace them, that is when the test is repeated.",
)

L['SNAKE-10'] = dict(
  sub="Toxicology → First Aid & Tests → Neostigmine test",
  intro="A neurotoxic bite paralyses by stopping acetylcholine from acting on muscle. If the block is on the receptor, raising acetylcholine with an anticholinesterase can overcome it. The neostigmine test is a trial of exactly that — and its result tells you whether the drug can be continued as treatment.",
  parts=[
    ('a', "**In any neurotoxic envenoming.** The snake is often unknown, and some patients respond who would not be predicted to, so every patient with ptosis or paralysis is tested."),
    ('b', "**Atropine 0.6 mg IV first, then neostigmine 0.5–2 mg IM (children 50 µg/kg and 0.04 mg/kg).** Neostigmine raises acetylcholine at every synapse, including muscarinic ones, causing bradycardia, bronchorrhoea and salivation. Atropine first blocks those muscarinic effects while leaving the nicotinic junction free to benefit. The response is judged at one hour: the Indian guideline calls the test positive if ptosis recovers by 50% or more, with eye movements and the single-breath count as further measures."),
    ('c', "**If it works, repeat every half hour for 3 hours, then hourly.** A response proves the block is postsynaptic and can be overcome. Neostigmine lasts only a few hours, so it is repeated, with atropine, to hold the improvement while antivenom works."),
    ('d', "**It fails in krait (and Russell’s viper) bites: presynaptic toxins.** Their phospholipase A₂ destroys the nerve terminal, so there is no acetylcholine release for neostigmine to amplify."),
  ],
  mimic=[
    ("Neostigmine here vs in organophosphate poisoning", "Here we raise acetylcholine to beat a receptor block; in organophosphate poisoning acetylcholine is already in excess and atropine is the treatment."),
  ],
  traps=[
    ("“Neostigmine replaces antivenom in cobra bites”", "It only buys time; antivenom is still given."),
    ("“Give neostigmine without atropine”", "Muscarinic effects — bradycardia and secretions — follow; atropine first."),
    ("“A negative test means no envenoming”", "It means a presynaptic toxin, as in krait; the patient may still need ventilation."),
  ],
  decode=[
    ("Ptosis improves 1 hour after neostigmine", "Postsynaptic (cobra) — continue neostigmine with atropine."),
    ("Neostigmine test negative, bitten asleep", "Krait — presynaptic."),
    ("Drug given before neostigmine", "Atropine 0.6 mg IV."),
    ("What counts as a positive test?", "50% or more recovery of ptosis at 1 hour."),
  ],
  punch="Neostigmine can only add acetylcholine, so it helps only where the nerve terminal is intact and the receptor is blocked — the cobra — and atropine goes first to stop the muscarinic side effects.",
)

L['SNAKE-11'] = dict(
  sub="Toxicology → Antivenom & Complications → Indian antivenom",
  intro="Antivenom is made by immunising horses with venom and purifying their antibodies. Because it is a foreign protein, a minority of patients react to it, and the rules on test doses and premedication come from trials of how to predict and prevent those reactions. Its storage rules matter because it must be kept at rural centres without a cold chain.",
  parts=[
    ('a', "**Polyvalent equine immunoglobulin against the big four.** Horses are immunised with the venoms of cobra, krait, Russell’s viper and saw-scaled viper, so one product covers all four and the snake need not be identified. Each vial is standardised by how much of each venom it neutralises."),
    ('b', "**Liquid: 2 years at 2–8 °C. Lyophilised: 5 years below 25 °C.** Liquid protein degrades unless refrigerated. Freeze-dried powder is stable at room temperature, which makes it the practical form for rural centres; it is reconstituted before use."),
    ('c', "**No test dose: it does not predict reactions.** Most early reactions are not IgE-mediated but complement activation by the foreign protein, so a small skin or IV test dose neither predicts nor prevents them, and it delays treatment."),
    ('d', "**Subcutaneous adrenaline 0.25–0.3 mg is the only premedication with evidence; antihistamines, steroids and slower infusion have no role.** In a large Sri Lankan trial (de Silva, PLoS Med 2011) low-dose SC adrenaline reduced severe early reactions, while promethazine and hydrocortisone did not. Low-dose adrenaline narrows the leaky vessels and stabilises mast cells before the protein arrives. WHO 2016 recommends it routinely unless the antivenom is known to cause few reactions, and the Indian guideline (2017) advises it before ASV except in known hypertensives; drugs for anaphylaxis are still drawn up for every infusion (SNAKE-15)."),
  ],
  mimic=[
    ("Test dose for antivenom vs antibiotics", "Neither is recommended; for antivenom it fails because most reactions are not IgE-mediated."),
  ],
  traps=[
    ("“Give a test dose first”", "It does not predict reactions and wastes time."),
    ("“Premedicate everyone with hydrocortisone and chlorphenamine”", "No evidence; only low-dose SC adrenaline has shown benefit, and it is now advised routinely."),
    ("“A past horse-serum reaction is a contraindication”", "No absolute contraindication; give it with resuscitation drugs ready."),
  ],
  decode=[
    ("Shelf life of lyophilised Indian ASV", "5 years below 25 °C."),
    ("Is a sensitivity test dose required?", "No."),
    ("Premedication with evidence", "SC adrenaline 0.25 mg."),
  ],
  punch="Antivenom is horse antibody against the big four; because its reactions are mostly not allergic, a test dose predicts nothing, and only low-dose adrenaline has been shown to prevent them.",
  extra=[dict(q="How much venom does one vial neutralise, and why start with 10?", a="Each mL neutralises **0.6 mg** of cobra and Russell’s venom (0.45 mg krait and saw-scaled), so a 10 mL vial ≈ **6 mg**. A Russell’s viper injects about **63 mg** on average — hence **10 vials** (~60 mg), and the same dose in children.")],
)

L['SNAKE-12'] = dict(
  sub="Toxicology → Antivenom & Complications → Indications for antivenom",
  intro="Antivenom is scarce, costly and can cause reactions, while half of venomous bites are dry. So it is given for evidence that venom has reached the circulation or is spreading dangerously in the limb — never for the bite itself. Once that evidence is there, no reaction risk outweighs it.",
  parts=[
    ('a', "**Systemic: coagulopathy (20WBCT positive, INR >1.2 or PT 4–5 s over normal, spontaneous bleeding); neurotoxicity (ptosis, ophthalmoplegia, paralysis); shock, arrhythmia; AKI, rhabdomyolysis, haemolysis.** Each sign means circulating venom acting on a distant organ. Antivenom neutralises venom that is still free, so it stops further damage — which is why it is still given to a late presenter with systemic signs."),
    ('b', "**Local: swelling of more than half the limb; rapidly extending swelling; swelling after a bite on a digit; a tender regional lymph node.** These mark a large venom load spreading through the tissue and lymphatics. A finger has little room to swell, so even modest swelling threatens necrosis and loss of the digit."),
    ('c', "**Local swelling alone is not an indication.** Minor swelling occurs in many bites and settles without antivenom; treating it exposes the patient to reactions without benefit."),
  ],
  table=dict(title="Give antivenom when", head=["Domain", "Sign"], rows=[["Blood", "20WBCT positive, INR >1.2, bleeding"], ["Nerve", "ptosis, ophthalmoplegia, paralysis"], ["Circulation", "shock, arrhythmia"], ["Kidney, muscle, red cells", "AKI, rhabdomyolysis, haemolysis"], ["Limb", ">half the limb, rapid spread, digit, tender node"]]),
  mimic=[
    ("Minor local swelling vs local envenoming", "Swelling confined near the bite is observed; swelling beyond half the limb, rapid spread or a tender node is treated."),
  ],
  traps=[
    ("“Krait patient already ventilated at 48 hours — antivenom is too late”", "Free venom may remain; antivenom is still given if envenomed, though it cannot undo toxin already bound."),
    ("“Asthma or a previous serum reaction is a contraindication”", "There is no absolute contraindication; untreated envenoming is deadlier — have adrenaline ready."),
    ("“Egg allergy contraindicates antivenom”", "Irrelevant — antivenom is horse protein, not egg-based."),
  ],
  decode=[
    ("Bite with mild swelling at the site, 20WBCT normal", "Observe; no antivenom."),
    ("Bite on a finger with swelling", "Antivenom indicated."),
    ("Absolute contraindication to antivenom", "None."),
  ],
  punch="Antivenom treats venom, not the bite: give it for any systemic sign or dangerous local spread, withhold it for local swelling alone — and once indicated, no allergy history stops it.",
)

L['SNAKE-13'] = dict(
  sub="Toxicology → Antivenom & Complications → Antivenom dosing",
  intro="Antivenom neutralises venom molecule for molecule, so the dose is set by how much venom the snake injected, not by the size of the patient. It cannot repair damage already done: in haemotoxic bites the liver must remake the clotting factors, and in neurotoxic bites only free venom can be caught. Those two facts decide when, and whether, to repeat.",
  parts=[
    ('a', "**10 vials, by IV infusion over 1 hour (or slow IV at 2 mL/min).** Ten vials neutralise roughly the average venom load of a Russell’s viper bite (SNAKE-11); the older national protocol allows 8–10. The whole dose goes in quickly so free venom is caught early; IM injection is never used, because absorption is too slow and causes haematomas. Indian studies found that larger initial doses add cost and reactions without better outcomes, and the 2017 guideline states that low-dose infusion is as effective as high-dose bolus therapy (expert consensus)."),
    ('b', "**No reduction in children: the snake injects the same venom.** The dose matches the venom, not the body weight, and a child receives a larger dose of venom per kilogram, so the need is if anything greater."),
    ('c', "**Haemotoxic: repeat 20WBCT at 6 hours; if still incoagulable, another 5–10 vials, 6-hourly.** After venom is neutralised the liver needs about 6 hours to make new clotting factors, so a test sooner would be misleading. Blood still liquid at 6 hours means venom is still active."),
    ('d', "**Neurotoxic: if no better or worse after 1–2 hours, a second 10 vials; then stop (maximum 20) and ventilate.** Antivenom catches only circulating toxin; toxin already bound, and terminals already destroyed, are beyond it. If 20 vials have not helped, more adds reaction risk without benefit — the patient needs ventilation and time."),
    ('e', "**Late presenters: haemotoxic — antivenom if coagulopathy persists; neurotoxic — one dose of 8–10 vials, then support.** Persistent coagulopathy proves free venom is still present. In a late neurotoxic case most toxin is already bound, so one dose mops up the rest."),
  ],
  table=dict(title="When to repeat", head=["Bite", "Reassess at", "If not better"], rows=[["Haemotoxic", "**6 h** (20WBCT)", "5–10 vials, 6-hourly"], ["Neurotoxic", "**1–2 h**", "10 more vials; maximum 20"]]),
  mimic=[
    ("Haemotoxic vs neurotoxic repeat timing", "Haemotoxic waits 6 hours for the liver; neurotoxic is judged at 1–2 hours by the paralysis."),
  ],
  traps=[
    ("“Halve the dose in children”", "Same dose — the venom load is the same."),
    ("“Keep giving antivenom until the krait patient breathes”", "Stop at 20 vials; recovery needs nerve terminals to regrow, so ventilate."),
    ("“Repeat 20WBCT at 1 hour after antivenom”", "At 6 hours — the liver needs that long to restore factors."),
  ],
  decode=[
    ("Initial ASV dose in a 20 kg child with a viper bite", "10 vials — same as an adult."),
    ("Blood still incoagulable 6 hours after ASV", "Repeat ASV, 5–10 vials."),
    ("Maximum ASV in neurotoxic envenoming", "20 vials, then ventilate."),
  ],
  punch="The dose is set by the venom, not the patient, so children get the full 10 vials; repeat at 6 hours in haemotoxic bites because the liver needs that long, and stop at 20 in neurotoxic bites because bound toxin cannot be reached.",
  extra=[dict(q="Is 10 vials a universal rule?", a="No — it is the Indian polyvalent rule. **CroFab** for North American pit vipers starts at **4–6 vials**. The constant is that **children get the adult dose**.")],
)

L['SNAKE-14'] = dict(
  sub="Toxicology → Antivenom & Complications → Expected response to antivenom",
  intro="Antivenom works by binding free venom, so anything caused directly by circulating venom improves fast. Anything that needs the body to rebuild — clotting factors, damaged tissue — takes hours. Knowing the expected time course tells you whether the dose was enough or a repeat is needed.",
  parts=[
    ('a', "**Spontaneous bleeding stops in 15–30 minutes.** Once the haemorrhagins and procoagulants are bound, vessel damage and factor consumption stop at once, and platelets plug the small leaks, even before the factor levels recover."),
    ('b', "**Blood pressure normalises in 30–60 minutes.** Venom-induced vasodilatation and myocardial depression stop when the toxin is neutralised; fluid lost through leaky capillaries may still need replacing."),
    ('c', "**Blood becomes coagulable in 3–9 hours.** Neutralising venom stops consumption, but the liver must make new fibrinogen and factors, which takes hours — the reason the 20WBCT is repeated at 6 hours (SNAKE-09, 13)."),
    ('d', "**Haemolysis and rhabdomyolysis stop within a few hours.** The membrane-damaging enzymes are bound, so no new cells break, and the dark urine clears as the pigment is excreted."),
    ('e', "**Postsynaptic paralysis improves from 30 minutes.** Antivenom pulls α-neurotoxin off the receptor, so cobra paralysis can begin to lift early. Presynaptic krait paralysis does not improve this way, because the nerve terminal must regrow."),
  ],
  mimic=[
    ("Bleeding stops vs blood clots again", "Bleeding stops in under 30 minutes; the 20WBCT normalises only after 3–9 hours. A still-liquid test at 1 hour is expected, not a failure."),
  ],
  traps=[
    ("“20WBCT still positive at 2 hours — repeat the antivenom”", "Clotting takes 3–9 hours to return; reassess at 6 hours."),
    ("“Krait paralysis should lift within an hour of antivenom”", "Only postsynaptic paralysis responds early; presynaptic recovery takes days."),
  ],
  decode=[
    ("Bleeding gums stop how soon after ASV?", "15–30 minutes."),
    ("Time for blood to become coagulable", "3–9 hours."),
    ("Earliest improvement of cobra paralysis", "From 30 minutes."),
  ],
  punch="Whatever free venom causes stops within minutes of antivenom; whatever the body must rebuild takes hours — so bleeding stops in half an hour but clotting returns only after the liver has had about 6 hours.",
)

L['SNAKE-15'] = dict(
  sub="Toxicology → Antivenom & Complications → Reactions to antivenom",
  intro="Antivenom is foreign horse protein, and the body can react to it in three ways at three different times. Early reactions come from complement and mast-cell activation by the protein; pyrogenic reactions from bacterial endotoxin contaminating the product; serum sickness from immune complexes once the body makes antibodies against horse protein about a week later. The timing tells you which one you face.",
  parts=[
    ('a', "**Early anaphylactic, 10–180 minutes: urticaria, bronchospasm, shock — stop; chlorphenamine 10 mg + hydrocortisone 100 mg IV; IM adrenaline if severe; restart slowly after 10–15 minutes.** The infusion is stopped to remove the trigger. Adrenaline is the drug that reverses bronchospasm and vasodilatation; current WHO guidance gives IM adrenaline 0.5 mg (child 0.01 mg/kg) at the first sign, with chlorphenamine and hydrocortisone as slower adjuncts. Antivenom is then restarted slowly, because the envenoming still needs treating."),
    ('b', "**Pyrogenic, 1–2 hours: fever, rigors, hypotension (endotoxin) — antipyretic, fluids.** Endotoxin in the product triggers cytokine release, so the patient has rigors and vasodilatation. Physical cooling, an antipyretic and fluids are enough."),
    ('c', "**Serum sickness, 1–12 days: fever, arthralgia, urticaria, nephritis — oral prednisolone, antihistamine.** The patient makes antibodies to horse protein, which form immune complexes with the antivenom still circulating; these deposit in joints, skin and glomeruli. Steroids suppress the inflammation, and antihistamine relieves the itch."),
  ],
  table=dict(title="Three reactions, three mechanisms", head=["Reaction", "Timing", "Mechanism"], rows=[["Early anaphylactic", "10–180 min", "complement and mast-cell activation by foreign protein"], ["Pyrogenic", "1–2 h", "endotoxin contamination"], ["Serum sickness", "1–12 days", "immune complexes (type III)"]]),
  mimic=[
    ("Pyrogenic reaction vs anaphylaxis", "Both can drop the blood pressure; rigors and fever without urticaria or wheeze point to endotoxin."),
  ],
  traps=[
    ("“Antihistamine and hydrocortisone first, adrenaline only if severe”", "Adrenaline IM 0.5 mg comes first; the others are slow adjuncts."),
    ("“After a reaction, antivenom is abandoned”", "It is restarted slowly once the reaction settles — the envenoming is the greater danger."),
    ("“Fever and joint pain a week later is a new infection”", "Serum sickness — oral prednisolone."),
  ],
  decode=[
    ("Wheeze and hypotension 20 minutes into ASV", "Stop; IM adrenaline 0.5 mg; then chlorphenamine and hydrocortisone."),
    ("Rigors 1 hour after ASV", "Pyrogenic (endotoxin) reaction."),
    ("Arthralgia, rash and proteinuria 7 days later", "Serum sickness."),
  ],
  punch="The timing names the reaction — minutes for anaphylaxis, an hour or two for endotoxin, a week for immune complexes — and in anaphylaxis adrenaline comes first, after which the antivenom is restarted.",
)

L['SNAKE-16'] = dict(
  sub="Toxicology → Antivenom & Complications → Supportive care and revision",
  intro="Around the antivenom, supportive care follows one theme: do not add to what the venom is already doing. The venom causes bleeding, kidney injury and tissue swelling, so the analgesic, the blood products and the surgery must not worsen any of them. The last three statements revisit the deck’s key distinctions.",
  parts=[
    ('a', "**Analgesia: paracetamol or tramadol; no NSAIDs (bleeding, AKI).** NSAIDs block platelet function in a patient who already cannot clot, and reduce renal blood flow in a kidney already under attack. IM injections are also avoided in coagulopathy."),
    ('b', "**Fresh frozen plasma only after antivenom: un-neutralised venom consumes the factors.** FFP given while free venom is present simply feeds the consumption. Once antivenom has neutralised it, FFP or cryoprecipitate can top up factors in a patient who is bleeding."),
    ('c', "**Fasciotomy only for compartment pressure >40 mmHg, and only after coagulopathy is corrected.** A swollen, tense, painful limb usually reflects venom oedema in the subcutaneous tissue, not true compartment syndrome, and settles with antivenom. Operating on unclottable blood causes uncontrollable bleeding, so the pressure is measured and the blood corrected first."),
    ('d', "**False — neostigmine does not reverse krait paralysis: the toxin is presynaptic.** The nerve terminal is destroyed, so there is no acetylcholine to amplify (SNAKE-10)."),
    ('e', "**False — the antivenom dose is the same in children.** The snake injects the same venom whatever the patient’s size (SNAKE-13)."),
    ('f', "**False — the clotting test needs clean glass, not plastic.** Plastic does not activate the contact pathway and gives a false positive (SNAKE-09)."),
  ],
  mimic=[
    ("Venom oedema vs compartment syndrome", "Both give a tense swollen limb; only a measured pressure above 40 mmHg with corrected clotting justifies fasciotomy."),
  ],
  traps=[
    ("“Give FFP at once to the bleeding viper patient”", "Antivenom first; until then FFP is consumed."),
    ("“Diclofenac for the painful bite”", "No NSAIDs — bleeding and kidney injury."),
    ("“Tense swollen limb — fasciotomy now”", "Measure the pressure and correct coagulopathy first; most settle with antivenom."),
  ],
  decode=[
    ("Analgesic for a viper bite", "Paracetamol or tramadol."),
    ("When is FFP given in envenoming?", "Only after antivenom."),
    ("Fasciotomy criteria", "Compartment pressure >40 mmHg, after coagulopathy is corrected."),
  ],
  punch="Supportive care must not add to the venom’s harm: no NSAIDs on a bleeding kidney, no plasma before the venom is neutralised, and no knife until the blood clots and the pressure proves it is needed.",
  extra=[dict(q="Myoglobinuria after a sea snake or Russell’s bite: what to aim for?", a="**Alkaline diuresis** with a high urine output (the card gives **above 100 mL/h**), started within 24 hours so the pigment does not precipitate in the tubules; dialysis if AKI develops.")],
)

FLAGS = {}
FLAGS['SNAKE-01'] = "35,000–50,000 is the older WHO figure. The Indian STG 2017 estimates ~45,900 deaths a year, and the Million Death Study (Suraweera et al., eLife 2020) ~58,000 a year (1.2 million in 2000–2019). The source of ‘34% of proven bites’ could not be found; check it against the notes."
FLAGS['SNAKE-02'] = "‘Hydrophidae’ is an old family name: sea snakes are now classed within Elapidae (subfamily Hydrophiinae). Their venom is neurotoxic as well as myotoxic, not myotoxic only."
FLAGS['SNAKE-03'] = "Small point: hyaluronidase is the spreading factor; local tissue destruction comes mainly from metalloproteinases, phospholipase A₂ and cytotoxins, which hyaluronidase helps spread."
FLAGS['SNAKE-05'] = "Card matches WHO SEARO for India. Small omissions: syndrome 3 is ‘cobra or king cobra’; syndrome 5 is Russell’s viper for a land bite with coagulopathy (South India, Sri Lanka) and sea snake for a sea bite without; WHO also lists non-Indian kraits (B. niger, B. candidus, B. multicinctus) under syndrome 5."
FLAGS['SNAKE-09'] = "Repeat schedule ‘every 30 min for 3 h, then hourly’ is the older national protocol (2009). The Indian STG 2017 says hourly for 3 h, then 6-hourly up to 24 h, and 6 h after the loading dose of ASV."
FLAGS['SNAKE-10'] = "Doses/route mixed: the Indian STG 2017 gives atropine 0.6 mg then neostigmine 1.5 mg IV, then 0.5 mg with atropine every 30 min for 5 doses (child atropine 0.05 mg/kg, neostigmine 0.04 mg/kg, repeat 0.01 mg/kg); positive = ≥50% recovery of ptosis at 1 h. WHO SEARO uses IM neostigmine (adult ≈0.02 mg/kg, ~1.5 mg). ‘0.5–2 mg’ blends the test dose with the 0.5 mg repeat dose; ‘every half hour for 3 h then hourly’ does not match the STG’s 5 half-hourly doses."
FLAGS['SNAKE-11'] = "Card says SC adrenaline is the only premedication with evidence (correct), but omits that it is now advised routinely: WHO SEARO 2016 recommends it unless the antivenom’s reaction rate is known to be low, and the Indian STG 2017 before ASV except in known hypertensives. STG 2017 gives lyophilised shelf life as 3–5 years."
FLAGS['SNAKE-13'] = "Indian STG 2017 regimens differ from the card: neurotoxic 10 vials over 30 min, second 10 at 1 h if no better (max 20); haemotoxic low-dose 10 vials (Russell’s) or 6 (saw-scaled) then 2 vials 6-hourly, or high-dose 10 then 6 vials 6-hourly. The card’s ‘5–10 vials 6-hourly’ is the older protocol."
FLAGS['SNAKE-15'] = "Qbank fix (WHO SEARO 2016 / Indian STG 2017): IM adrenaline 0.5 mg (child 0.01 mg/kg) is given FIRST at the earliest sign of anaphylaxis, not only ‘if severe’; chlorphenamine and hydrocortisone follow as adjuncts."
FLAGS['SNAKE-16'] = "Myoglobinuria target ‘urine above 100 mL/h’ could not be confirmed in WHO SEARO or the Indian STG 2017 (which describes forced alkaline diuresis cycles expecting ~3 mL/min, within 24 h of the bite)."
