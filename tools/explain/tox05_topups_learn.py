# TOX05 top-up cards — Explain v2 ("Learn" depth), same fields and voice as tox05_learn.py.
# Fields: sub, intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# No `step`: tox05_learn.py has no SPINE (like TOX01, the toxicology decks were written before v3).
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from map/out/all_rows.json and the DocT QBank (the top-up's own src) plus qpack/TOX05.md (SNAKE-03).
T = {}

T['T_1467a2fc'] = dict(
  sub="Toxicology → Envenomation → Spiders and scorpions",
  intro="Spider and scorpion venoms act on a few targets: transmitter release, sodium channels, or cell membranes. Each target gives a recognisable picture, so the exam either describes the picture and asks for the creature, or names the creature and asks for the mechanism.",
  parts=[
    ('a', "**Black widow (Latrodectus): alpha-latrotoxin floods presynaptic transmitter release — local sweating, cramps, rigid abdomen, hypertension.** The toxin forms calcium-permeable pores in nerve terminals, so acetylcholine and noradrenaline pour out. The bite shows a small puncture with a blanched halo and local sweating; abdominal rigidity can mimic an acute abdomen."),
    ('b', "**Brown recluse (Loxosceles): sphingomyelinase D — painless bite, necrosis over days, with haemolysis, DIC or AKI delayed 24–72 h (up to a week).** The enzyme damages cell membranes and activates complement, so tissue necroses slowly and red cells lyse. Systemic illness is late, not within minutes, and steroids have not been shown to prevent the haemolysis."),
    ('c', "**Funnel-web: delta-atracotoxin slows sodium-channel inactivation — autonomic storm; pressure bandage plus antivenom.** Channels that stay open keep nerves firing, releasing transmitter at autonomic and motor terminals: sweating, salivation, hypertension, fasciculation, pulmonary oedema. The venom spreads by lymph, so a pressure-immobilisation bandage slows it."),
    ('d', "**Bark scorpion (Centruroides, US): sodium-channel neurotoxin — jerking limbs and roving eye movements in children.** Its toxins open sodium channels so nerves fire repeatedly; it is the only US scorpion that causes serious systemic illness."),
    ('e', "**Indian red scorpion: catecholamine storm with myocarditis and pulmonary oedema — prazosin 30 microgram/kg, repeated 3-hourly.** The venom’s neurotoxins act on sodium and potassium channels of autonomic nerves and release a surge of catecholamines; α₁-mediated vasoconstriction raises afterload and the catecholamine-injured myocardium fails. Prazosin blocks α₁ receptors and lowers afterload, which is why it is the treatment in India. The 30 microgram/kg dose is the paediatric one; adults get a fixed oral dose (0.5–1 mg; 1 mg in Bawaskar’s 2011 randomised trial of prazosin with or without antivenom), repeated 3-hourly until the extremities warm and signs settle."),
  ],
  mimic=[
    ("Black widow vs brown recluse", "Black widow: painful bite, neurotoxic within an hour (cramps, sweating, rigid abdomen). Brown recluse: painless bite, local necrosis and haemolysis days later."),
  ],
  traps=[
    ("“Loxosceles: violin marking always present” or “systemic symptoms within 15 minutes”", "The marking is not consistent and systemic effects are delayed; delayed haemolysis is the feature (only 28% chose it)."),
    ("“Child with jerking after a US scorpion sting — desert hairy or stripe-tailed scorpion”", "Only the bark scorpion causes this (21% on DocT)."),
    ("“Black widow venom blocks sodium channels”", "It releases transmitter presynaptically; sodium channels are funnel-web and scorpion targets."),
  ],
  decode=[
    ("Painful bite, puncture with blanched halo, localised sweating — which spider? [DocT]", "Black widow (72%)."),
    ("Mechanism of funnel-web venom [DocT]", "Slowed inactivation of sodium channels (76%)."),
    ("Mechanism of Latrodectus venom [DocT]", "Presynaptic transmitter release (63%)."),
    ("Characteristic of Loxosceles envenomation [DocT]", "Delayed systemic complications, including haemolysis."),
  ],
  punch="Black widow releases transmitter, funnel-web and scorpions jam sodium channels open, brown recluse dissolves membranes slowly; and the Indian red scorpion’s catecholamine storm is treated with prazosin.",
)

T['T_dfc56d26'] = dict(
  sub="Toxicology → Snakes & Venom → VICC vs snakebite TMA",
  intro="A viper bite can cause two different blood disorders. VICC is the familiar one: venom consumes clotting factors and the blood will not clot (SNAKE-03, SNAKE-09). A minority then develop a thrombotic microangiopathy, which damages red cells and kidneys and does not respond to antivenom.",
  parts=[
    ('a', "**VICC: procoagulant venom consumes fibrinogen, giving incoagulable blood (positive 20WBCT, high INR); antivenom reverses it in about 6–24 h.** Venom prothrombin and factor X activators drive clotting until fibrinogen is used up. Antivenom neutralises circulating venom and the liver then restores factors, which is why the 20WBCT is repeated at 6 hours (SNAKE-14)."),
    ('b', "**TMA: about 5–15% of VICC, mainly Russell’s viper — schistocytes, low platelets, high LDH and AKI that PERSIST after clotting has recovered.** Endothelial injury forms platelet microthrombi that shear red cells and block glomerular vessels. A normal coagulation profile with ongoing haemolysis and AKI is the marker that VICC has given way to TMA. In the 2020 systematic review (Noutsos, Currie, Wijewickrama, Isbister; PLoS NTD) about four in five cases followed viper bites, hump-nosed and Russell’s vipers being the commonest, with Australian brown snakes next; in the Australian cohort TMA followed about 10% of VICC."),
    ('c', "**ADAMTS13 is normal in snakebite TMA, and plasma exchange gives no benefit (Isbister/Noutsos 2020).** The lesion is not the ADAMTS13 deficiency of TTP, so removing an inhibitor or replacing the enzyme has nothing to correct. The normal ADAMTS13 comes from small case series (Isbister’s brown-snake patients), not from the 2020 review; the review’s contribution is that plasma exchange showed no benefit on dialysis-free survival, so it ‘cannot be recommended’."),
    ('d', "**Antivenom neither prevents nor shortens the TMA — it is given for the venom effect, not the microangiopathy.** By the time TMA is evident the venom has done its damage; the 2020 review found no evidence that antivenom changes the course of the TMA, but it is still given for active envenoming."),
    ('e', "**Treatment is supportive, with dialysis for the AKI.** Most patients with snakebite TMA develop AKI and many need dialysis; the kidney often recovers over weeks."),
  ],
  mimic=[
    ("Snakebite TMA vs DIC vs TTP vs HUS", "DIC prolongs PT and lowers fibrinogen; TTP has ADAMTS13 <10%; snakebite TMA follows a bite with normal clotting by then and AKI."),
  ],
  traps=[
    ("“The MAHA is VICC fibrin deposition and antivenom is essential to halt it”", "This is the DocT key, and it is wrong in substance: TMA is a separate process and antivenom does not prevent or shorten it. B was keyed only because the other options were more wrong."),
    ("“Plasmapheresis, as in TTP”", "ADAMTS13 is not severely deficient and plasma exchange showed no benefit."),
    ("“Normal coagulation profile excludes a venom cause”", "That is exactly the TMA picture (84% chose correctly)."),
  ],
  decode=[
    ("Haematuria, thrombocytopenia, MAHA and AKI after a snakebite; coagulation normal [DocT]", "Viper-induced thrombotic microangiopathy."),
    ("Post-snakebite MAHA with schistocytes, high LDH, AKI — pathophysiology and intervention [DocT]", "Key: VICC plus antivenom and renal support (disputed; dialysis is the treatment that matters)."),
    ("VICC vs TTP — which statement is true? [DocT]", "VICC is driven by venom prothrombin activators (91%)."),
  ],
  punch="VICC is a clotting problem that antivenom fixes; snakebite TMA is an endothelial problem that persists after clotting recovers, needs no plasma exchange, and is treated with dialysis.",
)

FLAGS = {
  'T_dfc56d26': "Card c attributes ‘ADAMTS13 normal’ to Isbister/Noutsos 2020; that systematic review (Noutsos, Currie, Wijewickrama, Isbister, PLoS NTD 2020) reports no ADAMTS13 data — normal ADAMTS13 comes from small case series (e.g. Isbister’s two brown-snake TMA patients). The review’s conclusions are no benefit from plasma exchange and no evidence of benefit from antivenom. Suggest ‘ADAMTS13 is normal (case series); plasma exchange gives no benefit (Noutsos 2020)’. Card b ‘mainly Russell’s viper’: in the review hump-nosed viper (26%) and Russell’s viper (23%) were the commonest identified, vipers 80% overall — fine for India, slightly narrow globally. Also DocT Animal P2 Q11 key B (antivenom halts MAHA) is wrong in substance.",
}
