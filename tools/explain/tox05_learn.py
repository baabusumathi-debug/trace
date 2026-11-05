# TOX05 — Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Management of Snake Bite (SNAKE-01 to SNAKE-16). Same fields as TOX01.
# Audited 6 Nov against qpack/TOX05.md (60 real questions): see tox05_audit.md.
L = {}

L['SNAKE-01'] = dict(
  sub="Toxicology → Snakes & Venom → The size of the problem",
  intro="Snakebite in India is a rural, night-time, farm-work injury. Most bites turn out harmless, because the snake was not venomous or injected nothing — so every bite is observed rather than treated blindly. Those that do envenom kill mostly because the patient reaches antivenom too late.",
  parts=[
    ('a', "**35,000–50,000 deaths per year (WHO), the highest in the world.** A dense barefoot farming population sleeping on the floor lives among the big four. Many deaths happen at home and are never registered, so every count is an underestimate (the Million Death Study estimates about 58,000)."),
    ('b', "**70% of bites are non-venomous, and 50% of venomous bites are dry.** A dry bite is a bite by a venomous snake that injects no venom — the snake controls the injection, and a defensive strike often delivers none. So the bite alone is never an indication for antivenom (SNAKE-12)."),
    ('c', "**About 34% of proven bites develop systemic envenoming.** The rest have no or only local signs, which is why every bite is watched for 24 hours (SNAKE-09) before it is called harmless."),
    ('d', "**Most deaths occur before reaching hospital.** Neurotoxic bites can stop breathing within hours, and distance, night-time bites, traditional healers and poor access to antivenom add the delay. Once in hospital with antivenom and a ventilator, most survive."),
  ],
  mimic=[],
  traps=[
    ("“Every snakebite needs antivenom”", "Most bites are non-venomous or dry; antivenom is given only for signs of envenoming."),
    ("“No symptoms at 1 hour, so it was a dry bite”", "Krait paralysis and viper coagulopathy can appear hours later; observe for at least 24 hours."),
  ],
  decode=[
    ("Key finding of an Indian snakebite registry [DocT]", "Most deaths come from late hospital arrival and poor access to ASV."),
    ("Which statement about dry bites is correct? [DocT]", "A venomous snake bites but injects no venom."),
  ],
  punch="Most bites never inject venom, so the bite is watched, not treated — but those that do envenom kill mostly on the way to hospital, so speed of transport and antivenom near the patient save lives.",
)

L['SNAKE-02'] = dict(
  sub="Toxicology → Snakes & Venom → Families and the big four",
  intro="Venomous snakes fall into families whose venoms do broadly different things: elapids mainly paralyse, vipers mainly disturb clotting and damage tissue. But venom is not uniform — its toxin content varies between species and even between regions of one species, and the amount injected and absorbed varies with each bite — which is why presentations differ. In India four species cause most deaths, and the national antivenom is raised against exactly those four.",
  parts=[
    ('a', "**Elapidae — cobras, kraits (also king cobra, coral snakes): neurotoxic.** Short fixed front fangs and small neurotoxins that block the neuromuscular junction: the danger is descending paralysis and respiratory failure (SNAKE-04, 07)."),
    ('b', "**Viperidae — true vipers (Russell’s, saw-scaled) and pit vipers (hump-nosed, Malayan): haemotoxic.** Long hinged fangs and enzyme-rich venoms that consume clotting factors and damage vessel walls: local swelling, bleeding, shock and kidney injury."),
    ('c', "**Hydrophidae — sea snakes: myotoxic.** Their venom breaks down skeletal muscle (pain, myoglobinuria, kidney injury) and is also neurotoxic; the bite is usually painless."),
    ('d', "**Common cobra (Naja naja), common krait (Bungarus caeruleus), Russell’s viper (Daboia russelii), saw-scaled viper (Echis carinatus).** Indian polyvalent antivenom is made by immunising horses with these four venoms. Its antibodies recognise these and not others, which is why a hump-nosed pit viper or king cobra bite does not respond."),
  ],
  table=dict(title="Family to main effect", head=["Family", "Indian examples", "Main effect"], rows=[["Elapidae", "cobra, krait, king cobra", "**neurotoxic**"], ["Viperidae", "Russell’s, saw-scaled, hump-nosed", "**haemotoxic**, local damage"], ["Sea snakes", "—", "**myotoxic** (and neurotoxic)"]]),
  mimic=[
    ("Russell’s viper vs hump-nosed pit viper", "Both give local swelling, coagulopathy and kidney injury; only Russell’s viper is covered by Indian antivenom."),
  ],
  traps=[
    ("“Venom composition is uniform, or quantity alone sets severity”", "Toxin content varies by species and geography, and absorption varies by bite; together they explain the variety."),
    ("“Polyvalent antivenom covers all Indian venomous snakes”", "Only the big four; hump-nosed pit viper and king cobra are not covered."),
  ],
  decode=[
    ("What best explains the variability of snakebite presentations? [DocT]", "Variation in venom toxin content and absorption."),
    ("Viper bite with coagulopathy not responding to antivenom [pattern]", "Hump-nosed pit viper."),
  ],
  punch="Elapids paralyse and vipers make the blood unclottable; Indian antivenom is raised against only the big four, so a snake outside that list may envenom a patient the antivenom cannot help.",
)

L['SNAKE-03'] = dict(
  sub="Toxicology → Snakes & Venom → What the venom contains",
  intro="Venom is modified saliva, more than 90% protein — enzymes and non-enzymatic polypeptide toxins, each with its own target, in proportions that differ between species. The clinical picture of a bite is the sum of what each component does: why vipers bleed, why cobras necrose and why kraits paralyse without a mark on the skin.",
  parts=[
    ('a', "**Metalloproteinases damage the endothelial basement membrane: capillary leak, bleeding, shock.** These zinc-dependent haemorrhagins digest the matrix of capillary walls, so red cells and plasma escape: swelling, haemorrhagic blisters, bleeding and hypovolaemic shock. With hyaluronidase they produce the painful, spreading local swelling."),
    ('b', "**Procoagulant enzymes activate clotting: consumption coagulopathy (DIC-like).** Russell’s venom activates factors X and V; saw-scaled venom activates prothrombin. Factors and fibrinogen are used up and fibrinolysis follows, so the blood becomes unclottable — and the gum bleeding and haematuria come from that, not from direct glomerular damage. It is DIC-like because it is consumption by venom, not sepsis or tissue factor."),
    ('c', "**Phospholipase A₂: myotoxicity, presynaptic neurotoxicity, mitochondrial damage.** It breaks down membrane phospholipids: in muscle, rhabdomyolysis; at the motor nerve terminal it destroys the terminal (β-bungarotoxin of the krait is a phospholipase A₂). Among metalloproteinases, haemorrhagins, procoagulants and PLA₂, it is the only one that paralyses."),
    ('d', "**Hyaluronidase: the spreading factor, with tissue destruction.** It breaks down hyaluronic acid in connective tissue, opening a path for the other toxins; the necrosis itself comes mainly from the enzymes and cytotoxins it lets through."),
    ('e', "**Polypeptide neurotoxins block the neuromuscular junction.** The α-neurotoxins of cobras bind the postsynaptic nicotinic receptor. The terminal is intact, so more acetylcholine — neostigmine — can compete them off."),
  ],
  mimic=[
    ("Venom coagulopathy (VICC) vs TTP", "VICC is factor consumption by venom prothrombin activators, treated with antivenom; TTP is ADAMTS13 deficiency, treated with plasma exchange. Some snakebites also cause a thrombotic microangiopathy with schistocytes."),
    ("Presynaptic vs postsynaptic neurotoxin", "Presynaptic (PLA₂, krait) destroys the terminal; postsynaptic (α-neurotoxin, cobra) blocks the receptor and can be overcome."),
  ],
  traps=[
    ("“Descending paralysis — metalloproteinases or haemorrhagins”", "Those cause bleeding and swelling; the neurotoxic enzyme offered is phospholipase A₂ (presynaptic). Pure α-neurotoxin, the cobra’s, is a non-enzymatic polypeptide and is often not among the options."),
    ("“Give FFP to correct the venom coagulopathy”", "Free venom consumes the new factors too; antivenom first (SNAKE-16)."),
  ],
  decode=[
    ("Ptosis and diplopia progressing to limbs — venom component [DocT]", "Phospholipase A₂."),
    ("Bleeding gums, haematuria, falling platelets — mechanism of the haematuria [DocT]", "Consumption of clotting factors and fibrinolysis."),
    ("Swelling, haemorrhagic bullae and pain — components [DocT]", "Hyaluronidase and metalloproteinases."),
    ("VICC vs TTP; pit-viper venom composition [DocT]", "Prothrombin activators consume factors (no ADAMTS13 role); enzymes plus non-enzymatic polypeptides."),
  ],
  punch="Each venom protein has one target — the vessel wall, the clotting cascade, the cell membrane, the connective tissue or the acetylcholine receptor — and the bite’s picture is their sum.",
)

L['SNAKE-04'] = dict(
  sub="Toxicology → Snakes & Venom → Cobra vs krait neurotoxicity",
  intro="Cobras and kraits both paralyse from the eyelids downwards, but from opposite sides of the neuromuscular junction. The cobra blocks the receptor on the muscle; the krait destroys the nerve terminal. That one difference explains the local signs, the response to neostigmine and the length of ventilation — and the local signs, not the timing, are what tell them apart in a stem.",
  parts=[
    ('a', "**Toxin site: cobra postsynaptic (α-neurotoxin); krait presynaptic (β-bungarotoxin).** The α-neurotoxin sits on the nicotinic receptor like a competitive blocker. β-bungarotoxin is a phospholipase A₂ that enters the terminal, causes a burst of release, then exhausts and destroys it — which is why recovery depends on nerve regeneration."),
    ('b', "**Local reaction: cobra swelling and necrosis; krait virtually painless, none.** Cobra cytotoxins kill tissue at the bite; krait venom has almost no local toxins and the fangs are small, so there may be no visible bite mark at all."),
    ('c', "**Onset: cobra early, within 30 minutes; krait delayed, with prolonged paralysis.** A receptor block acts as soon as toxin arrives; presynaptic damage usually takes hours, and neurotoxin can be absorbed late, so paralysis may first appear 12 hours after the bite. Krait paralysis can still begin within an hour, and cobra paralysis may only show at a few hours — so ptosis with no swelling or bleeding is krait whatever the clock says."),
    ('d', "**Neostigmine: cobra responds; krait does not.** Neostigmine raises cleft acetylcholine, which competes α-neurotoxin off the receptor; a destroyed terminal has nothing to amplify (SNAKE-10)."),
    ('e', "**Typical story: cobra — painful swollen bite; krait — bitten asleep on the floor at night, with abdominal pain.** Kraits hunt at night and enter houses, so the victim wakes with abdominal pain and has ptosis by morning, with no mark to explain it."),
  ],
  table=dict(title="Opposite sides of one junction", head=["", "Cobra", "Krait"], rows=[["Target", "postsynaptic receptor", "presynaptic terminal"], ["Local signs", "swelling, necrosis", "none"], ["Onset", "early", "delayed"], ["Neostigmine", "**responds**", "**no response**"], ["Ventilation", "shorter", "days to weeks"]]),
  mimic=[
    ("Krait bite vs Guillain–Barré, botulism or stroke", "Sudden descending paralysis after a night on a farm or floor, with no bite mark, is krait until proved otherwise; late paralysis after a known bite is delayed venom absorption, not GBS."),
  ],
  traps=[
    ("“Ptosis 45 minutes after the bite — too early for a krait, so cobra”", "Timing overlaps; no local swelling or bleeding decides it — krait (Bungarus caeruleus)."),
    ("“Krait with PaCO₂ 60 — oxygen, high-flow, or neostigmine first”", "That is ventilatory failure: intubate and ventilate. Oxygen hides the CO₂, and neostigmine does not work presynaptically."),
    ("“Antivenom best reverses presynaptic toxins, or can be withheld if no signs by 6 hours”", "It neutralises only circulating venom, so it is given early to stop progression; it cannot undo destroyed terminals, and signs can appear after 6 hours."),
  ],
  decode=[
    ("Ptosis, dysphonia, shallow breathing 45 minutes after a bite; no swelling or bleeding [DocT]", "Common krait."),
    ("Descending paralysis after a night at a farm, no bite mark [DocT]", "Krait bite (not GBS or botulism)."),
    ("Krait, respiratory fatigue, PaCO₂ 60 [DocT]", "Intubate and ventilate."),
    ("Ptosis, ophthalmoplegia, decremental response — mechanism and management [DocT]", "Presynaptic toxin: antivenom, plus possibly prolonged ventilation while nerves regenerate."),
  ],
  punch="The cobra blocks the receptor, so more acetylcholine wins and recovery is quick; the krait destroys the terminal, so neostigmine has nothing to work with and the patient needs the ventilator until the nerve regrows.",
  extra=[dict(q="Krait bite: when to intubate?", a="**Early** — bulbar palsy with pooled secretions, neck-flexor weakness, paradoxical breathing, a falling single-breath count, or a **rising PaCO₂**.")],
)

L['SNAKE-05'] = dict(
  sub="Toxicology → Clinical Syndromes → WHO syndromic approach",
  intro="Most patients never see the snake, or bring a description that cannot be trusted. The WHO approach reads the illness to name the snake. Three questions do most of the work — is there local swelling, is the blood clotting, and is there paralysis?",
  parts=[
    ('a', "**Syndrome 1 — local envenoming with bleeding: Viperidae.** Swelling plus incoagulable blood or gum bleeding means a viper — bleeding is the haemotoxic sign (SNAKE-03)."),
    ('b', "**Syndrome 2 — as syndrome 1 plus shock or AKI, conjunctival oedema, pituitary failure; or plus ptosis and dark urine: Russell’s viper.** Russell’s venom adds vasodilating and nephrotoxic effects, and in South India and Sri Lanka a presynaptic phospholipase A₂ that gives ptosis. A necrotic, bleeding bite in an Indian stem is Russell’s viper unless the stem says the antivenom failed."),
    ('c', "**Syndrome 3 — local envenoming with paralysis: cobra.** Only cobras combine necrosis at the bite with paralysis; WHO lists cobra or king cobra here."),
    ('d', "**Syndrome 4 — paralysis with minimal local signs: krait (on land, asleep) or sea snake (in water).** Both venoms are neurotoxic with almost no local toxins; the place separates them."),
    ('e', "**Syndrome 5 — paralysis with dark urine and AKI: Russell’s viper; sea snake.** Neurotoxic plus myotoxic or haemolytic venom. A land bite with incoagulable blood is Russell’s viper; a sea bite with normal clotting is a sea snake."),
  ],
  table=dict(title="Three questions name the snake", head=["Local swelling", "Bleeding", "Paralysis", "Snake"], rows=[["yes", "yes", "no", "viper"], ["yes", "yes", "± ptosis, dark urine, AKI, shock", "Russell’s viper"], ["yes", "no", "yes", "cobra"], ["no", "no", "yes", "krait (land) / sea snake"]]),
  mimic=[
    ("Syndrome 3 vs 4", "Both paralyse; local swelling and necrosis mean cobra, a clean bite site means krait."),
  ],
  traps=[
    ("“Necrosis with bleeding at the bite — hump-nosed pit viper”", "It can do this, but the big-four answer is Russell’s viper; choose hump-nosed only when the stem gives antivenom failure or a Kerala/Western Ghats pit viper."),
    ("“Wait for the snake to be identified before giving antivenom”", "The syndrome is enough; polyvalent antivenom covers all four."),
  ],
  decode=[
    ("Image of a necrotic, bleeding bite site — species (krait, Russell’s, coral, hump-nosed) [DocT]", "Russell’s viper."),
    ("Image of gum bleeding — what it indicates [DocT]", "Haemotoxicity."),
    ("Descending paralysis 3 hours after a bite, no bleeding [DocT]", "Common krait."),
    ("Ptosis, dysphonia, dysphagia 4 hours after a bite — which snake (saw-scaled, Russell’s, cobra, sea snake) [DocT]", "Cobra."),
  ],
  punch="Read the patient, not the snake: swelling with bleeding is a viper, swelling with paralysis a cobra, paralysis on a clean bite a krait — and Russell’s viper adds shock, kidney injury and sometimes ptosis.",
)

L['SNAKE-06'] = dict(
  sub="Toxicology → Clinical Syndromes → Features by species",
  intro="This table is the syndromic approach laid out snake by snake. Cytotoxins give local damage, neurotoxins give paralysis, procoagulants give coagulopathy, and the nephrotoxic Russell’s venom gives kidney failure. Only one box separates cobra from krait in treatment — neostigmine.",
  parts=[
    ('a', "**Local damage: cobra yes, krait no, Russell’s yes, saw-scaled yes.** Cobra cytotoxins and viper metalloproteinases destroy tissue, so painful progressive swelling occurs with all three; among cobra, krait, hump-nosed and coral snake, tissue necrosis is classically the cobra. A clean bite site with paralysis points to a krait."),
    ('b', "**Ptosis and paralysis: cobra yes, krait yes, Russell’s sometimes, saw-scaled no.** Russell’s viper paralyses only in some regions; the saw-scaled viper is purely haemotoxic."),
    ('c', "**Coagulopathy: cobra no, krait no (may occur), Russell’s yes, saw-scaled yes.** A positive 20WBCT points to a viper and away from the elapids."),
    ('d', "**Renal failure: only Russell’s viper.** Directly and through haemolysis, rhabdomyolysis, shock and DIC, producing acute tubular necrosis (SNAKE-07)."),
    ('e', "**Neostigmine: only the cobra.** Its postsynaptic block can be overcome; the krait and Russell’s viper act presynaptically (SNAKE-10)."),
    ('f', "**Antivenom: all four.** Polyvalent antivenom is raised against each of the big four. A pit viper outside them — the hump-nosed pit viper of Kerala — has antigenically different venom, so the antivenom does not bind it and swelling and coagulopathy persist after repeated doses."),
  ],
  mimic=[
    ("Russell’s vs saw-scaled viper", "Both cause swelling and coagulopathy; kidney failure (and ptosis in some regions) points to Russell’s."),
  ],
  traps=[
    ("“Ptosis and shallow breathing early after a bite, no swelling — cobra or Russell’s”", "No local swelling or bleeding means krait (SNAKE-04)."),
    ("“Pit viper in Kerala not responding to two doses of ASV — bad batch or broken cold chain”", "Antigenic variability: the venom is not one the antivenom was raised against."),
    ("“Coagulopathy can be a cobra bite”", "Indian cobra venom does not cause coagulopathy; a positive 20WBCT means a viper."),
  ],
  decode=[
    ("Ptosis, dysphonia, shallow breathing; no swelling or bleeding (or an image of ptosis alone) [DocT]", "Krait — the absent local signs decide."),
    ("Painful progressive swelling — saw-scaled, Russell’s, cobra? [DocT]", "All of them."),
    ("Tissue necrosis after a bite — cobra, krait, hump-nosed, coral [NEET 2025]", "Cobra."),
    ("Kerala pit viper, no response to 2 doses of ASV [NEET 2025]", "Antigenic variability among species."),
  ],
  punch="Every box follows from the venom: cytotoxins give local damage, procoagulants give bleeding, neurotoxins give paralysis — and only the cobra’s postsynaptic block lets neostigmine work.",
)

L['SNAKE-07'] = dict(
  sub="Toxicology → Clinical Syndromes → What kills, and the brain-death trap",
  intro="Systemic envenoming kills in different ways — haemorrhage, renal failure and respiratory failure are all complications. Vipers make the blood unclottable and the vessels leaky, so the patient bleeds where it does most harm and the kidneys fail. Elapids paralyse from the head down until breathing stops. A fully paralysed patient can look dead while wide awake.",
  parts=[
    ('a', "**Viper bite deaths: intracranial bleeding, anterior pituitary haemorrhage, multi-organ failure.** Incoagulable blood plus vessel damage lets a small brain bleed expand. Russell’s venom can infarct the anterior pituitary: acutely shock and hypoglycaemia, later chronic hypopituitarism. Shock, AKI and DIC together give multi-organ failure."),
    ('b', "**Neurotoxic paralysis is descending: ptosis, ophthalmoplegia, bulbar weakness, then respiratory muscles.** The fast-firing eye and face motor units have the least safety margin, so they fail first; bulbar weakness threatens the airway, and the diaphragm fails last."),
    ('c', "**Locked-in state mimics brain death: fixed dilated pupils and no movement, yet conscious. Never diagnose brain death.** Venom blocks every neuromuscular junction, including the iris, but not the brain: the EEG stays active and MRI shows no anoxic injury. The patient is sedated, spoken to and kept ventilated; an apnoea test or brainstem testing is invalid until the toxin has gone."),
    ('d', "**Acute tubular necrosis is the commonest renal lesion.** Shock, haemoglobin and myoglobin pigments, microthrombi and direct venom toxicity all injure the tubular cells — the same pigment-and-shock ATN as in exertional heat stroke with myoglobinuria. Cortical necrosis is less common and worse."),
  ],
  mimic=[
    ("Locked-in envenoming vs brain death", "Both: fixed pupils, no movement, apnoea. Envenoming is a junction block in a conscious brain — the EEG is active and recovery is expected."),
  ],
  traps=[
    ("“Fixed dilated pupils 48 hours after a krait bite — declare brain death or do an apnoea test”", "Continue ventilation and supportive care; never certify brain death in neurotoxic envenoming."),
    ("“Russell’s viper AKI — fluids, steroids or FFP and observe”", "Oliguria, K 5.8 and still-incoagulable blood need repeat ASV and early renal replacement; steroids have no role, FFP only after ASV."),
  ],
  decode=[
    ("Krait bite 48 h ago, deep coma, fixed pupils, apnoeic, EEG active [DocT]", "Continue ventilation and supportive care."),
    ("Russell’s viper, oliguric, creatinine 3.1, K 5.8, prolonged WBCT20 [DocT]", "Renal replacement therapy and ASV."),
    ("Heat collapse with myoglobinuria and rising creatinine — renal lesion [DocT]", "Acute tubular necrosis."),
  ],
  punch="Vipers kill by bleeding and kidney failure, elapids by descending paralysis — and a paralysed patient can look brain-dead while fully aware, so brain death is never diagnosed in envenoming.",
)

L['SNAKE-08'] = dict(
  sub="Toxicology → First Aid & Tests → First aid",
  intro="First aid has two aims: slow the spread of venom through the lymphatics, and get the patient to antivenom quickly. Lymph moves when the limb’s muscles contract. Most traditional measures do neither and add harm, especially in viper bites where tissue is already being destroyed.",
  parts=[
    ('a', "**Do: reassure, immobilise the limb like a fracture, carry the patient (no walking), get to hospital.** Immobility stops the muscle pump that drives lymph and venom onward. Antivenom is the definitive treatment, so transport is the most important step."),
    ('b', "**Do not: tourniquet, cutting or sucking, ice, electric shock.** A tight arterial tourniquet traps venom in an ischaemic limb, worsens necrosis and releases a bolus when removed. Cutting bleeds and infects; suction removes nothing useful; ice and shock only damage tissue. Steroids for local swelling have no role."),
    ('c', "**Pressure immobilisation is controversial; only for purely neurotoxic bites, and not so tight as to stop perfusion.** A firm crepe bandage slows lymphatic spread, which matters for elapid venom. In viper bites, most Indian bites, holding a tissue-destroying venom in the limb may worsen necrosis. WHO 2016 favours it for suspected elapid bites; the Indian guideline (2017) allows it only by trained staff when hospital is 30 minutes to 3 hours away."),
  ],
  mimic=[
    ("Pressure immobilisation vs tourniquet", "The bandage compresses lymphatics but keeps the arterial supply; a tourniquet stops blood flow."),
  ],
  traps=[
    ("“Immobilise and apply a pressure-immobilisation bandage to every snakebite”", "DocT keys this (it is the least wrong of its four options, against tourniquet, incision and steroids), but it is Australian elapid practice; Indian and WHO guidance immobilise without a tight bandage by default."),
    ("“Remove the tourniquet at once”", "Remove it only once antivenom has started and resuscitation is ready — check the distal pulse, apply a proximal cuff, remove, then deflate slowly."),
  ],
  decode=[
    ("Initial management of a suspected snakebite — tourniquet, incision, PIB, IM steroids [DocT]", "Immobilise the limb (pressure bandage as keyed)."),
    ("Snakebite first aid does NOT include [Marrow]", "A tight arterial tourniquet."),
  ],
  punch="Keep the limb still so the lymph — and the venom — stops moving, and move the patient to antivenom instead; everything that cuts, ties or freezes the limb only adds injury.",
)

L['SNAKE-09'] = dict(
  sub="Toxicology → First Aid & Tests → 20-minute whole blood clotting test",
  intro="Viper venom consumes fibrinogen and clotting factors until the blood cannot clot. The 20-minute whole blood clotting test checks this at the bedside with only a glass tube and a clock, so a peripheral centre can decide on antivenom without a laboratory. It relies on glass activating the contact pathway.",
  parts=[
    ('a', "**A few mL of venous blood in a new, clean, dry glass tube, left undisturbed for 20 minutes, then tilted.** Glass activates factor XII; normal blood forms a firm clot well within 20 minutes. Disturbing the tube early breaks a forming clot."),
    ('b', "**Still liquid = coagulopathy = viper bite, and an indication for antivenom.** If fibrinogen has been consumed, no clot can form however long you wait. Indian cobras and kraits do not cause coagulopathy, so an unclotted tube means haemotoxic envenoming."),
    ('c', "**Plastic tubes, or glass washed with detergent, give false results.** Plastic does not activate the contact pathway, so normal blood stays liquid — a false positive."),
    ('d', "**Every 30 minutes for 3 hours, then hourly; and 6 hours after antivenom. Observe every bite for at least 24 hours.** Venom can be absorbed late: coagulopathy can appear hours after the bite, and neurotoxicity as late as 12–13 hours, so a single normal test or an asymptomatic patient at 4 hours excludes nothing. After antivenom the liver needs about 6 hours to make new factors; still liquid at 6 hours means repeat the dose (SNAKE-13)."),
  ],
  mimic=[
    ("20WBCT vs PT/INR", "Both detect venom coagulopathy; 20WBCT needs no laboratory, and INR >1.2 is used where available (SNAKE-12)."),
  ],
  traps=[
    ("“Unclotted blood at 20 minutes — DIC or lab error”", "In a snakebite it is haemotoxic envenomation — give antivenom (use only clean glass)."),
    ("“Asymptomatic 4 hours after a neurotoxic bite — discharge”", "Admit and observe for 24 hours; neurotoxicity can be delayed by up to about 13 hours."),
    ("“Still abnormal at 6 hours — wait 24 hours or give FFP only”", "Repeat ASV; FFP alone is consumed by the free venom."),
  ],
  decode=[
    ("Image: blood still liquid at 20 minutes [NEET 2025]", "Haemotoxic envenomation."),
    ("Viper bite, 10 vials given 6 h ago, WBCT20 still abnormal [DocT]", "Repeat ASV, 10 vials."),
    ("New ptosis and weak breathing 12 h after a bite [DocT]", "Delayed systemic absorption of neurotoxin."),
    ("Asymptomatic coral snake bite 4 h ago wants to leave [Marrow]", "Admit — neurotoxicity can be delayed up to 13 h."),
  ],
  punch="Glass starts clotting, so normal blood clots within 20 minutes; liquid blood means the venom has used up the factors — and because the liver needs 6 hours to replace them, that is when the test is repeated.",
)

L['SNAKE-10'] = dict(
  sub="Toxicology → First Aid & Tests → Neostigmine test",
  intro="A neurotoxic bite paralyses by stopping acetylcholine from acting on muscle. If the block is on the receptor, raising acetylcholine with an anticholinesterase can overcome it. The neostigmine test is a trial of exactly that — and its result tells you whether to continue the drug.",
  parts=[
    ('a', "**In any neurotoxic envenoming.** The snake is often unknown, so every patient with ptosis or paralysis is tested."),
    ('b', "**Atropine 0.6 mg IV first, then neostigmine 0.5–2 mg IM (children 50 µg/kg and 0.04 mg/kg).** Neostigmine raises acetylcholine at muscarinic synapses too — bradycardia, bronchorrhoea, salivation — so atropine goes first. The test is positive if ptosis recovers by 50% or more at one hour."),
    ('c', "**If it works, repeat every half hour for 3 hours, then hourly.** A response proves a postsynaptic block; neostigmine is short-acting, so it is repeated with atropine while antivenom works."),
    ('d', "**It fails in krait (and Russell’s viper) bites: presynaptic toxins.** Their phospholipase A₂ destroys the terminal, so there is no release for neostigmine to amplify — and toxicity with AKI or DIC is not a neostigmine problem at all."),
  ],
  mimic=[
    ("Neostigmine here vs in organophosphate poisoning", "Here acetylcholine is raised to beat a receptor block; in organophosphate poisoning it is already in excess and atropine is the treatment."),
  ],
  traps=[
    ("“Neostigmine replaces antivenom in cobra bites”", "It only buys time; antivenom is still given."),
    ("“A negative test means no envenoming”", "It means a presynaptic toxin, as in krait; the patient may still need ventilation."),
  ],
  decode=[
    ("Which neurotoxic bite is most likely to respond to neostigmine? [DocT]", "Cobra — postsynaptic block."),
    ("Drug given before neostigmine [pattern]", "Atropine 0.6 mg IV."),
  ],
  punch="Neostigmine can only add acetylcholine, so it helps only where the nerve terminal is intact and the receptor is blocked — the cobra — and atropine goes first to stop the muscarinic side effects.",
)

L['SNAKE-11'] = dict(
  sub="Toxicology → Antivenom & Complications → Indian antivenom",
  intro="Antivenom is purified antibody from horses immunised with venom. Because it is a foreign protein, a minority of patients react to it — but untreated envenoming is deadlier, so it has no absolute contraindication. Its storage rules matter because it must be kept at rural centres without a cold chain.",
  parts=[
    ('a', "**Polyvalent equine immunoglobulin against the big four.** One product covers cobra, krait, Russell’s viper and saw-scaled viper. Each mL is standardised to neutralise 0.6 mg of cobra and Russell’s venom (0.45 mg krait and saw-scaled), so one 10 mL vial neutralises about **6 mg** of Russell’s venom. A Russell’s viper injects about 63 mg on average — hence a starting dose of 10 vials (about 60 mg)."),
    ('b', "**Liquid: 2 years at 2–8 °C. Lyophilised: 5 years below 25 °C.** Freeze-dried powder is stable at room temperature, so it is the practical form for rural centres."),
    ('c', "**No test dose: it does not predict reactions.** Most early reactions are complement activation by the foreign protein, not IgE, so a test dose neither predicts nor prevents them and delays treatment."),
    ('d', "**Subcutaneous adrenaline 0.25–0.3 mg is the only premedication with evidence; antihistamines, steroids and slower infusion have no role.** In a large Sri Lankan trial low-dose SC adrenaline reduced severe early reactions, while promethazine and hydrocortisone did not. WHO 2016 and the Indian guideline (2017, except in known hypertensives) advise it routinely; anaphylaxis drugs are drawn up for every infusion (SNAKE-15)."),
  ],
  mimic=[],
  traps=[
    ("“One vial neutralises 60 mg of Russell’s venom”", "6 mg per vial; 60 mg is what the 10-vial starting dose covers."),
    ("“Hypotension, respiratory depression or egg allergy contraindicates ASV”", "There is none: hypotension and respiratory failure are signs of envenoming (indications), and egg allergy concerns vaccines, not horse serum. A past serum reaction means resuscitation ready, not withholding."),
    ("“Give a test dose first”", "It does not predict reactions and wastes time."),
  ],
  decode=[
    ("One vial of ASV neutralises how much Russell’s viper venom? [DocT]", "6 mg."),
    ("Contraindications to ASV — hypotension, respiratory suppression, egg allergy, none [DocT]", "None."),
  ],
  punch="Antivenom is horse antibody against the big four, each vial neutralising about 6 mg of venom; because its reactions are mostly not allergic, a test dose predicts nothing, and only low-dose adrenaline has been shown to prevent them.",
)

L['SNAKE-12'] = dict(
  sub="Toxicology → Antivenom & Complications → Indications for antivenom",
  intro="Antivenom is scarce, costly and can cause reactions, while half of venomous bites are dry. So it is given for evidence that venom has reached the circulation or is spreading dangerously in the limb — never for the bite itself. Once that evidence is there, no reaction risk or delay outweighs it.",
  parts=[
    ('a', "**Systemic: coagulopathy (20WBCT positive, INR >1.2 or PT 4–5 s over normal, spontaneous bleeding); neurotoxicity (ptosis, ophthalmoplegia, paralysis); shock, arrhythmia; AKI, rhabdomyolysis, haemolysis.** Each sign means circulating venom. Antivenom neutralises venom that is still free, so it stops further damage — which is why it is still given to a late presenter, even a krait patient intubated at 48 hours."),
    ('b', "**Local: swelling of more than half the limb; rapidly extending swelling; swelling after a bite on a digit; a tender regional lymph node.** These mark a large venom load spreading through tissue and lymphatics; a finger has little room to swell, so even modest swelling threatens the digit."),
    ('c', "**Local swelling alone is not an indication.** Minor swelling — still less pain without swelling — settles without antivenom; treating it exposes the patient to reactions without benefit."),
  ],
  table=dict(title="Give antivenom when", head=["Domain", "Sign"], rows=[["Blood", "20WBCT positive, INR >1.2, bleeding"], ["Nerve", "ptosis, ophthalmoplegia, paralysis"], ["Circulation", "shock, arrhythmia"], ["Kidney, muscle, red cells", "AKI, rhabdomyolysis, haemolysis"], ["Limb", ">half the limb, rapid spread, digit, tender node"]]),
  mimic=[],
  traps=[
    ("“Krait patient intubated at 48 hours — ASV is ineffective after 24 hours”", "Give it: circulating venom may remain. It cannot undo bound toxin, and neostigmine adds nothing in a presynaptic bite."),
    ("“Asthma, egg allergy or a previous serum reaction is a contraindication”", "There is no absolute contraindication; have adrenaline ready (SNAKE-11)."),
  ],
  decode=[
    ("Not a WHO indication for ASV — systemic bleeding, progressive swelling, localised pain without swelling, neuroparalysis [DocT]", "Localised pain without swelling."),
    ("Krait neuroparalysis, presents at 48 h, intubated — give ASV? [NEET 2025]", "Yes — it neutralises circulating venom."),
    ("Contraindications to ASV [DocT]", "None."),
  ],
  punch="Antivenom treats venom, not the bite: give it for any systemic sign or dangerous local spread, withhold it for local swelling alone — and once indicated, no allergy history stops it.",
)

L['SNAKE-13'] = dict(
  sub="Toxicology → Antivenom & Complications → Antivenom dosing",
  intro="Antivenom neutralises venom molecule for molecule, so the dose is set by how much venom the snake injected, not by the size of the patient. It cannot repair damage already done: in haemotoxic bites the liver must remake the clotting factors, and in neurotoxic bites only free venom can be caught. Those two facts decide when, and whether, to repeat — and why it is given early.",
  parts=[
    ('a', "**10 vials, by IV infusion over 1 hour (or slow IV at 2 mL/min).** Ten vials neutralise roughly the average Russell’s viper venom load (SNAKE-11); the older protocol allows 8–10. The whole dose goes in early so free venom is caught before it binds; IM is never used. Indian studies — the SAKTI trial, as DocT reports it, compared low- with high-dose ASV in haemotoxic bites — found larger doses add cost and reactions without better outcomes."),
    ('b', "**No reduction in children: the snake injects the same venom.** The dose matches the venom, not body weight, and a child receives more venom per kilogram."),
    ('c', "**Haemotoxic: repeat 20WBCT at 6 hours; if still incoagulable, another 5–10 vials, 6-hourly.** Antivenom stops further venom action but does not replace factors; the liver needs about 6 hours to make them. Blood still liquid at 6 hours means venom is still active — repeat the dose (and, with oliguric AKI, start renal replacement too)."),
    ('d', "**Neurotoxic: if no better or worse after 1–2 hours, a second 10 vials; then stop (maximum 20) and ventilate.** Toxin already bound, and terminals already destroyed, are beyond antivenom. If 20 vials have not helped, more adds reaction risk without benefit — the patient needs ventilation (intubate on rising PaCO₂) and time."),
    ('e', "**Late presenters: haemotoxic — antivenom if coagulopathy persists; neurotoxic — one dose of 8–10 vials, then support.** Persistent coagulopathy proves free venom remains; in a late neurotoxic case one dose mops up the rest."),
  ],
  table=dict(title="When to repeat", head=["Bite", "Reassess at", "If not better"], rows=[["Haemotoxic", "**6 h** (20WBCT)", "5–10 vials, 6-hourly"], ["Neurotoxic", "**1–2 h**", "10 more vials; maximum 20"]]),
  mimic=[],
  traps=[
    ("“Antivenom rapidly reverses coagulopathy within 1–2 hours, or replaces factors”", "It stops further venom effect; clotting returns only as the liver makes factors (3–9 hours)."),
    ("“Halve the dose in children”", "Same dose — the venom load is the same. The same rule holds for North American CroFab, which starts at 4–6 vials."),
    ("“Keep giving antivenom until the krait patient breathes”", "Stop at 20 vials; recovery needs nerve terminals to regrow, so ventilate."),
  ],
  decode=[
    ("Viper bite, WBCT20 still abnormal 6 h after 10 vials [DocT]", "Repeat ASV, 10 vials."),
    ("Role of antivenom in snakebite coagulopathy [DocT]", "Prevents further venom effect but does not immediately restore factors."),
    ("SAKTI trial studied [NEET 2025]", "Low-dose versus high-dose ASV in haemotoxic bites."),
    ("20 kg child, rattlesnake bite 45 minutes ago [Marrow]", "CroFab 4–6 vials — the adult dose."),
  ],
  punch="The dose is set by the venom, not the patient, so children get the full 10 vials; repeat at 6 hours in haemotoxic bites because the liver needs that long, and stop at 20 in neurotoxic bites because bound toxin cannot be reached.",
)

L['SNAKE-14'] = dict(
  sub="Toxicology → Antivenom & Complications → Expected response to antivenom",
  intro="Antivenom binds free venom, so anything caused directly by circulating venom improves fast; anything the body must rebuild — clotting factors, damaged tissue — takes hours. The expected time course tells you whether the dose was enough.",
  parts=[
    ('a', "**Spontaneous bleeding stops in 15–30 minutes.** Once haemorrhagins and procoagulants are bound, vessel damage and consumption stop, and platelets plug small leaks before factor levels recover."),
    ('b', "**Blood pressure normalises in 30–60 minutes.** Venom vasodilatation and myocardial depression stop when the toxin is neutralised; lost fluid may still need replacing."),
    ('c', "**Blood becomes coagulable in 3–9 hours.** Antivenom does not replace factors; the liver must make new fibrinogen and factors — hence the 20WBCT is repeated at 6 hours (SNAKE-09, 13)."),
    ('d', "**Haemolysis and rhabdomyolysis stop within a few hours.** No new cells break, and the dark urine clears as pigment is excreted."),
    ('e', "**Postsynaptic paralysis improves from 30 minutes.** Antivenom pulls α-neurotoxin off the receptor; presynaptic krait paralysis waits for the terminal to regrow."),
  ],
  mimic=[],
  traps=[
    ("“20WBCT still positive at 2 hours — antivenom has failed”", "Clotting takes 3–9 hours to return; reassess at 6 hours."),
  ],
  decode=[
    ("Best description of antivenom’s role in coagulopathy [DocT]", "Prevents further venom effects but does not immediately restore clotting factors."),
    ("Bleeding gums stop how soon after ASV? [pattern]", "15–30 minutes."),
  ],
  punch="Whatever free venom causes stops within minutes of antivenom; whatever the body must rebuild takes hours — so bleeding stops in half an hour but clotting returns only after the liver has had about 6 hours.",
)

L['SNAKE-15'] = dict(
  sub="Toxicology → Antivenom & Complications → Reactions to antivenom",
  intro="Antivenom is foreign horse protein, and the body can react in three ways at three times: early reactions from complement and mast-cell activation, pyrogenic reactions from contaminating endotoxin, and serum sickness from immune complexes about a week later. The timing tells you which one you face.",
  parts=[
    ('a', "**Early anaphylactic, 10–180 minutes: urticaria, bronchospasm, shock — stop; chlorphenamine 10 mg + hydrocortisone 100 mg IV; IM adrenaline if severe; restart slowly after 10–15 minutes.** Stop the infusion to remove the trigger. Adrenaline reverses bronchospasm and vasodilatation, so current WHO guidance gives IM adrenaline 0.5 mg (child 0.01 mg/kg) at the first sign — hypotension, wheeze or rash — with chlorphenamine and hydrocortisone as slower adjuncts. Antivenom is then restarted slowly, because the envenoming still needs treating."),
    ('b', "**Pyrogenic, 1–2 hours: fever, rigors, hypotension (endotoxin) — antipyretic, fluids.** Endotoxin triggers cytokine release: rigors and vasodilatation, treated with cooling, an antipyretic and fluids."),
    ('c', "**Serum sickness, 1–12 days: fever, arthralgia, urticaria, nephritis — oral prednisolone, antihistamine.** Antibodies to horse protein form immune complexes that deposit in joints, skin and glomeruli."),
  ],
  table=dict(title="Three reactions, three mechanisms", head=["Reaction", "Timing", "Mechanism"], rows=[["Early anaphylactic", "10–180 min", "complement and mast-cell activation by foreign protein"], ["Pyrogenic", "1–2 h", "endotoxin contamination"], ["Serum sickness", "1–12 days", "immune complexes (type III)"]]),
  mimic=[
    ("Pyrogenic reaction vs anaphylaxis", "Both can drop the blood pressure; rigors and fever without urticaria or wheeze point to endotoxin."),
  ],
  traps=[
    ("“Stop ASV and give IV hydrocortisone; or slow the rate; or continue with antihistamines”", "Stop it and give IM adrenaline 0.5 mg first; steroids and antihistamines are slow adjuncts."),
    ("“After a reaction, antivenom is abandoned”", "It is restarted slowly once the reaction settles."),
  ],
  decode=[
    ("Chills, hypotension, wheeze and rash 15 minutes into ASV [DocT]", "Stop ASV, IM adrenaline, supportive care."),
    ("Arthralgia, rash and proteinuria 7 days later [pattern]", "Serum sickness."),
  ],
  punch="The timing names the reaction — minutes for anaphylaxis, an hour or two for endotoxin, a week for immune complexes — and in anaphylaxis adrenaline comes first, after which the antivenom is restarted.",
)

L['SNAKE-16'] = dict(
  sub="Toxicology → Antivenom & Complications → Supportive care and revision",
  intro="Supportive care follows one theme: do not add to what the venom is already doing — bleeding, kidney injury and tissue swelling. The last three statements revisit the deck’s key distinctions.",
  parts=[
    ('a', "**Analgesia: paracetamol or tramadol; no NSAIDs (bleeding, AKI).** NSAIDs block platelets in a patient who cannot clot and cut renal blood flow in a kidney under attack. IM injections are also avoided."),
    ('b', "**Fresh frozen plasma only after antivenom: un-neutralised venom consumes the factors.** Once antivenom has neutralised the venom, FFP or cryoprecipitate can top up factors in a bleeding patient."),
    ('c', "**Fasciotomy only for compartment pressure >40 mmHg, and only after coagulopathy is corrected.** A tense swollen limb is usually subcutaneous venom oedema that settles with antivenom; operating on unclottable blood causes uncontrollable bleeding."),
    ('d', "**False — neostigmine does not reverse krait paralysis: the toxin is presynaptic** (SNAKE-10)."),
    ('e', "**False — the antivenom dose is the same in children.** The snake injects the same venom (SNAKE-13)."),
    ('f', "**False — the clotting test needs clean glass, not plastic.** Plastic does not activate the contact pathway (SNAKE-09)."),
  ],
  mimic=[],
  traps=[
    ("“Diclofenac for the painful bite”", "No NSAIDs — bleeding and kidney injury."),
    ("“Tense swollen limb — fasciotomy now”", "Measure the pressure and correct coagulopathy first; most settle with antivenom."),
  ],
  decode=[
    ("Analgesic for a viper bite [pattern]", "Paracetamol or tramadol."),
    ("Fasciotomy criteria [pattern]", "Compartment pressure >40 mmHg, after coagulopathy is corrected."),
  ],
  punch="Supportive care must not add to the venom’s harm: no NSAIDs on a bleeding kidney, no plasma before the venom is neutralised, and no knife until the blood clots and the pressure proves it is needed.",
)

FLAGS = {}
FLAGS['SNAKE-01'] = "35,000–50,000 is the older WHO figure. The Indian STG 2017 estimates ~45,900 deaths a year, and the Million Death Study (Suraweera et al., eLife 2020) ~58,000 a year (1.2 million in 2000–2019). The source of ‘34% of proven bites’ could not be found; check it against the notes."
FLAGS['SNAKE-02'] = "‘Hydrophidae’ is an old family name: sea snakes are now classed within Elapidae (subfamily Hydrophiinae). Their venom is neurotoxic as well as myotoxic, not myotoxic only."
FLAGS['SNAKE-03'] = "Small point: hyaluronidase is the spreading factor; local tissue destruction comes mainly from metalloproteinases, phospholipase A₂ and cytotoxins, which hyaluronidase helps spread."
FLAGS['SNAKE-04'] = "Part c ‘cobra early, within 30 minutes; krait delayed’ is a tendency, not a rule: DocT keys krait for ptosis and respiratory weakness at 45 minutes with no local signs, and cobra for bulbar palsy at 4 hours. Local signs, not onset time, discriminate."
FLAGS['SNAKE-05'] = "Card matches WHO SEARO for India. Small omissions: syndrome 3 is ‘cobra or king cobra’; syndrome 5 is Russell’s viper for a land bite with coagulopathy (South India, Sri Lanka) and sea snake for a sea bite without; WHO also lists non-Indian kraits (B. niger, B. candidus, B. multicinctus) under syndrome 5."
FLAGS['SNAKE-09'] = "Repeat schedule ‘every 30 min for 3 h, then hourly’ is the older national protocol (2009). The Indian STG 2017 says hourly for 3 h, then 6-hourly up to 24 h, and 6 h after the loading dose of ASV."
FLAGS['SNAKE-10'] = "Doses/route mixed: the Indian STG 2017 gives atropine 0.6 mg then neostigmine 1.5 mg IV, then 0.5 mg with atropine every 30 min for 5 doses (child atropine 0.05 mg/kg, neostigmine 0.04 mg/kg, repeat 0.01 mg/kg); positive = ≥50% recovery of ptosis at 1 h. WHO SEARO uses IM neostigmine (adult ≈0.02 mg/kg, ~1.5 mg). ‘0.5–2 mg’ blends the test dose with the 0.5 mg repeat dose; ‘every half hour for 3 h then hourly’ does not match the STG’s 5 half-hourly doses."
FLAGS['SNAKE-11'] = "Card says SC adrenaline is the only premedication with evidence (correct), but omits that it is now advised routinely: WHO SEARO 2016 recommends it unless the antivenom’s reaction rate is known to be low, and the Indian STG 2017 before ASV except in known hypertensives. STG 2017 gives lyophilised shelf life as 3–5 years."
FLAGS['SNAKE-13'] = "Indian STG 2017 regimens differ from the card: neurotoxic 10 vials over 30 min, second 10 at 1 h if no better (max 20); haemotoxic low-dose 10 vials (Russell’s) or 6 (saw-scaled) then 2 vials 6-hourly, or high-dose 10 then 6 vials 6-hourly. The card’s ‘5–10 vials 6-hourly’ is the older protocol. SAKTI trial details are as DocT gives them; not independently verified."
FLAGS['SNAKE-15'] = "Qbank fix (WHO SEARO 2016 / Indian STG 2017): IM adrenaline 0.5 mg (child 0.01 mg/kg) is given FIRST at the earliest sign of anaphylaxis, not only ‘if severe’; chlorphenamine and hydrocortisone follow as adjuncts."
FLAGS['SNAKE-16'] = "Myoglobinuria target ‘urine above 100 mL/h’ could not be confirmed in WHO SEARO or the Indian STG 2017 (which describes forced alkaline diuresis cycles expecting ~3 mL/min, within 24 h of the bite)."
