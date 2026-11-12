# SPECIAL05B — Explain v3 ("Learn" depth): polytrauma, part 2 — the lethal triad (and calcium), trauma-induced coagulopathy, lactate and base deficit, damage control
# (indications, resuscitation, surgery, REBOA, pelvic bleeding), fluid trials, massive transfusion (definitions, emergency blood, ratios, prediction, endpoints), tranexamic acid,
# fibrinogen replacement, other drugs, the European guideline, true/false sweep.
# No mnemonics or hooks. Driven by qpack/SPECIAL05B.md (47 question links; POLY-18 massive transfusion asked 11 times, POLY-16 damage control surgery/REBOA/pelvis 8, POLY-12 and POLY-15
# five each). POLY-17 has no linked question and gets a short explanation with [pattern] decode items.
# No `fix` entries exist for SPECIAL05B in trace/test/data/qbank.json (checked 13 Nov 2026); its `lines` and `cross` notes were read and used.
# Checked online on 13 Nov 2026:
#  - European guideline, 6th edition (Rossaint, Crit Care 2023; Europe PMC full text): restricted volume to SBP 80–90 mmHg until bleeding stops, no TBI (1B); MAP ≥80 in severe TBI GCS ≤8 (1C);
#    noradrenaline with fluids if the target is not reached (1C), dobutamine for myocardial dysfunction; 0.9% NaCl or balanced crystalloid (1B), avoid hypotonic solutions (Ringer’s lactate) in
#    severe head injury; Hb 70–90 g/L; damage control surgery in haemorrhagic shock (1B), also for hypothermia, acidosis, inaccessible injury, long procedures; pelvic binder pre-hospital,
#    ring closure, extraperitoneal packing; REBOA ‘suggest consider’ (2C); topical haemostats (1B); initial FFP:RBC at least 1:2 or fibrinogen concentrate/cryo + RBC (1C), high platelet:RBC (2B);
#    goal-directed (viscoelastic) strategy (1B); TXA 1 g over 10 min then 1 g over 8 h, as soon as possible, en route, within 3 h (1A), not awaiting viscoelastic results (1B); fibrinogen if
#    major bleeding with viscoelastic functional deficit or Clauss ≤1.5 g/L (1C), initial 3–4 g = 15–20 single-donor cryo units (2C); platelets >50 with ongoing bleeding, >100 ×10⁹/L in TBI (2C);
#    ionised calcium in the normal range 1.1–1.3 mmol/L, calcium chloride to correct (1C), <0.9 = transfusion hypocalcaemia, <0.8 arrhythmias; rFVIIa not first line (1B), off-label only if
#    bleeding and coagulopathy persist (2C); fibrinolytic shutdown TEG LY30 <0.9%. No recommendation for or against prehospital blood products.
#  - CRASH-2 (n 20,207; SBP <90 and/or HR >110 within 8 h): bleeding deaths 4.9% vs 5.7%; by time: ≤1 h RR 0.68, 1–3 h RR 0.79, >3 h RR 1.44 (harm).
#  - CRASH-3 (n 12,737; within 3 h; GCS ≤12 or CT bleed; no major extracranial bleeding): head-injury death 18.5% vs 19.8% (RR 0.94, NS) overall; benefit in mild–moderate (GCS 9–15), none in
#    GCS 3 or bilateral unreactive pupils; earlier is better; no excess vascular occlusive events.
#  - PATCH-Trauma (Gruen, NEJM 2023; prehospital TXA within 3 h, COAST-selected): favourable GOS-E at 6 months 53.7% vs 53.5% (NS); deaths 24 h 9.7 vs 14.1%, 28 d 17.3 vs 21.8%, 6 months 19.0 vs 22.9% (NS).
#  - PROPPR (JAMA 2015, n 680): 24-h mortality 12.7 vs 17.0%, 30-day 22.4 vs 26.1% (both NS); exsanguination deaths at 24 h 9.2 vs 14.6% (p 0.03); haemostasis 86.1 vs 78.1%.
#  - PROMMTT (JAMA Surg 2013, n 905 observational): higher plasma and platelet ratios linked to lower mortality in the first 6 h (ratios <1:2 had 3–4 times the odds of death); no association after 24 h.
#  - PAMPer (NEJM 2018, n 501): prehospital thawed plasma during air transport, 30-day mortality 23.2 vs 33.0%.
#  - CRYOSTAT-2 (JAMA 2023, n 1,604): early empirical cryo (3 pools, ~6 g) on top of the major haemorrhage protocol: 28-day mortality 25.3 vs 26.1% (NS); penetrating subgroup higher with cryo.
#  - UK-REBOA (JAMA 2023, n 90, 97% blunt): 90-day mortality 54 vs 42%, 87% posterior probability of harm, stopped for harm.
#  - TOWAR (NEJM May 2026, n 1,020 air-transported, cluster-randomised): prehospital low-titre O whole blood vs components, 30-day mortality 25.9 vs 20.5% (NS after adjustment).
#  - Bickell (NEJM 1994, penetrating torso, SBP ≤90): delayed fluids, survival to discharge 70 vs 62%.
#  - REBOA zones (WikEM): 1 left subclavian to coeliac (abdominal bleeding), 2 coeliac to lowest renal (not used), 3 lowest renal to bifurcation (pelvic/junctional).
#  - Fibrinolysis phenotypes (Moore): hyperfibrinolysis LY30 >3% (mortality ~44%), physiological ~0.9–2.9% (~3%), shutdown ≤0.8–0.9% (~17%).
#  - ABC score: ≥2 → activate; derivation sensitivity 75%, specificity 86%. AO Spine/Praxis 2024 SCI: MAP floor 75–80, ceiling 90–95 mmHg for 3–7 days. ATLS 10th base deficit bands
#    (calculator page: I ≤2, II >2–6, III >6–10, IV >10). More than half of trauma patients are hypocalcaemic on arrival before any blood (GWU review).
# From standard references without a fresh check (confident unless said): Cosgriff 1997 odds ratios (pH <7.1 OR 12.3, temp <34 °C OR 8.7, ISS >25 OR 7.7, SBP <70 OR 5.8, all four ≈98%) — reviewer: the outcome was life-threatening coagulopathy (PT and PTT >2× normal), not death;
# Jurkovich 1987 (core <32 °C ≈100% mortality); Wolberg 2004 (hypothermia hits platelet adhesion first, enzymes mainly below 33 °C); Brohi 2003/2007 (ACoTS ~25% on arrival, activated protein C);
# Rizoli 2011 (factor V most depleted); SAFE 2004, SAFE-TBI 2007 (24-month mortality 33.2 vs 20.4%), CHEST 2012 (RRT 7.0 vs 5.8%), CRYSTAL 2013, FIRST 2011; ITACTIC 2021 (viscoelastic vs
# conventional tests: no outcome difference); RiaSTAP dosing formula and 70 mg/kg; NASCIS II/III; AANS/CNS 2013; AO Spine 2017 (24-h methylprednisolone within 8 h as an option);
# ATLS uncrossmatched O Rh-positive for men and older women; Morrison 2011 interim (MAP 50 vs 65 intra-operatively, n 90: early post-operative deaths 1/44 vs 8/46) and Carrick 2016 final (n 168: no difference in 24-h or 30-day mortality) — checked by the reviewer; RePHILL 2022
# (prehospital red cells + plasma vs saline: no benefit; less sure); lactate sensitivity/specificity figures on POLY-13 (card figures, not re-checked).

SPINE = [
  ("Shock feeds the lethal triad", "Hypoperfusion makes the patient cold and acidotic, cold and acid stop clots forming, and the bleeding that follows deepens the shock, so lactate and base deficit measure how far down that spiral he already is."),
  ("Coagulopathy begins before any fluid", "A quarter of the badly injured arrive coagulopathic because shock activates protein C and fibrinolysis and consumes fibrinogen; dilution, cold and acid add the late, iatrogenic layer."),
  ("Damage control resuscitation", "When physiology is exhausted, keep the pressure low but adequate, give blood products instead of crystalloid in about a 1:1:1 ratio, and choose the patient for a short operation, not a complete one."),
  ("Stopping the bleeding mechanically", "Bleeding stops only with pressure, a binder, a tourniquet, packing, embolisation or an abbreviated operation; REBOA is a temporary bridge with doubtful benefit."),
  ("Blood in ratio, to targets", "Massive transfusion starts on a bedside score with group O cells and AB plasma, runs in a fixed ratio, then switches to laboratory and viscoelastic targets, with fibrinogen the first factor to replace."),
  ("Drugs, guideline and the sweep", "Tranexamic acid within 3 hours, calcium kept normal and rFVIIa only as a last resort complete the bundle that the European guideline sets out."),
]

PRIMER = "Haemorrhage is the commonest preventable cause of death after injury, and most of those deaths happen in the first few hours. A clot needs enough fibrinogen, platelets, ionised calcium, working enzymes (which need a normal temperature and pH) and an endothelium that is not being broken down. Shock alone disturbs all of these, which is why the bleeding trauma patient is treated as a coagulopathy from the start, not just as a volume problem. SPECIAL05A covered definitions, scores, the primary survey and the ATLS shock classes; this deck covers what happens to blood and physiology and how they are rescued."

L = {}

L['POLY-11'] = dict(
  sub="Polytrauma → Lethal triad → Hypothermia, acidosis, coagulopathy",
  step=1,
  intro="Step 1 is the spiral that kills the bleeding patient. Each part of the triad makes the other two worse: cold and acid slow clotting, poor clotting means more bleeding, and more bleeding means worse perfusion, more acid and less heat production. The one real question tests how cold impairs clotting even when the laboratory numbers look normal.",
  parts=[
    ('a', "**Hypothermia (under 34 °C), acidosis (pH under 7.2), coagulopathy: each worsens the others, and all three together carry a very high mortality.** The thresholds are where the effect on clotting becomes clinically important. Many now add hypocalcaemia as a fourth corner (the ‘lethal diamond’): over half of patients are hypocalcaemic on arrival before any blood is given, and citrate in transfused products lowers it further (POLY-22)."),
    ('b', "**pH under 7.1 (odds ratio 12.3), temperature under 34 °C (8.7), ISS over 25 (7.7), SBP under 70; all four together ≈ 98% mortality.** These figures come from Cosgriff (1997), a study of 58 massively transfused trauma patients, and what they predicted was life-threatening coagulopathy (PT and PTT more than twice normal), not death: with all four risk factors, 98% developed it. Coagulopathy of that degree carries a very high mortality, which is why the card reads them as predictors of death. Acidosis carries the highest odds because clotting enzymes fail in acid, which is why the pH or base deficit is the number most often used to choose damage control (POLY-14)."),
    ('c', "**Lost thermoregulation and shivering, low metabolism, cold fluids and exposure; a core temperature under 32 °C in trauma ≈ 100% mortality.** Heat comes from metabolism, and a hypoperfused patient makes little; cold fluids and an exposed body on a trolley remove the rest. Cold hits platelets first: adhesion and activation fall at about 33 °C, while enzyme slowing becomes important mainly below that. PT and aPTT are run at 37 °C in the laboratory, so they can be normal in a patient who is oozing, and the fix is rewarming, not more products. Trauma hypothermia is far more lethal than accidental hypothermia at the same temperature, because it marks shock."),
    ('d', "**Poor perfusion and saline resuscitation cause it; it makes factor VIIa, the Xa/Va complex and platelets fail, and depresses the myocardium.** Lactic acid from anaerobic metabolism and the hyperchloraemia of large volumes of 0.9% saline both lower the pH. Clotting enzymes are proteases that work poorly in acid: as the pH falls towards 7.0, factor VIIa and the Xa/Va complex lose most of their activity. Correcting pH with bicarbonate alone does not restore clotting; restoring perfusion does."),
  ],
  mimic=[
    ("Trauma hypothermia vs accidental hypothermia", "In trauma, 32 °C is close to unsurvivable because the cold reflects shock; in accidental hypothermia a patient may survive far lower temperatures with rewarming."),
  ],
  traps=[
    ("“Normal PT, aPTT and platelet count mean the bleeding is surgical”", "The tests are warmed to 37 °C; at 33 °C platelet adhesion is reduced in the patient while the numbers stay normal."),
    ("“Hypothermia’s main effect on clotting is enhanced fibrinolysis or excess tissue factor”", "Its main effect is reduced platelet adhesion and activation."),
  ],
  decode=[
    ("Core 33 °C, normal platelet count and factor levels, diffuse microvascular bleeding — which defect? [DocT GT]", "Reduced platelet adhesion."),
    ("Which factor most strongly predicted life-threatening coagulopathy in massively transfused trauma patients? [pattern]", "Acidosis, pH under 7.1 (odds ratio about 12; Cosgriff)."),
  ],
  punch="Cold, acid and poor clotting feed each other. Cold impairs platelets before the laboratory can see it, acid cripples the clotting enzymes, and the treatment of both is restoring perfusion and warmth, not correcting a number.",
)

L['POLY-12'] = dict(
  sub="Polytrauma → Lethal triad → Trauma-induced coagulopathy",
  step=2,
  intro="Step 2 explains why the bleeding patient is coagulopathic on arrival, before any fluid has been given. Five real questions test the mechanism, and the one that only 11% got right asked exactly that: coagulopathy despite minimal crystalloid is caused by shock-driven activation of protein C, not dilution.",
  parts=[
    ('a', "**Early (endogenous, acute traumatic coagulopathy): tissue injury exposes endothelium; shock activates protein C (anticoagulation) and hyperfibrinolysis; fibrinogen falls first.** Hypoperfused endothelium releases thrombomodulin, which binds thrombin; the thrombin–thrombomodulin complex activates protein C. Activated protein C cleaves factors Va and VIIIa (factor V is the factor most consistently depleted in shock) and inhibits PAI-1, which releases fibrinolysis. Tissue plasminogen activator from damaged endothelium adds to the clot breakdown. Fibrinogen is both consumed and broken down, so it reaches a critical level first. This is present in about a quarter of severely injured patients on arrival and needs both tissue injury and shock; neither alone produces it."),
    ('b', "**Late (iatrogenic): consumption, dilution with clot-free fluids, hypothermia, acidosis.** Crystalloid and red cells contain no clotting factors, so each litre dilutes what is left. Cold and acid then slow the enzymes that remain (POLY-11). This layer is avoidable, which is why damage control resuscitation restricts crystalloid and gives plasma early."),
    ('c', "**Six drivers: tissue damage, shock, inflammation, hypothermia, acidosis, haemodilution.** The first three are endogenous and start at the scene; the last three are added in hospital. The endothelium is also part of the injury: shock and catecholamines shed its glycocalyx, which raises permeability, releases heparin-like material and promotes fibrinolysis."),
  ],
  table=dict(title="Fibrinolysis on TEG in trauma (LY30 = % lysis 30 min after maximum amplitude)",
    head=["Phenotype", "LY30", "Meaning"],
    rows=[["Hyperfibrinolysis", "Over 3%", "Highest mortality (about 40%); give TXA"],
          ["Physiological", "About 0.9–3%", "Lowest mortality"],
          ["Shutdown", "Under 0.9%", "Commonest; mortality raised, thrombosis risk"]]),
  mimic=[
    ("Acute traumatic coagulopathy vs dilutional coagulopathy", "The first is present on arrival, needs shock and is driven by activated protein C and fibrinolysis; the second follows large volumes of factor-free fluid."),
    ("Trauma-induced coagulopathy vs DIC", "Early trauma coagulopathy is anticoagulant and fibrinolytic, with fibrinogen loss; classical DIC with widespread microthrombi is a later, inflammatory picture."),
  ],
  traps=[
    ("“Coagulopathy on arrival in a patient given little fluid is dilutional or consumptive”", "It is systemic protein C activation by shock. Only 11% chose this on DocT GT; most picked dilution or local consumption."),
    ("“PT/INR or the platelet count is the earliest marker”", "Fibrinogen is the first factor to fall to a critical level."),
    ("“An LY30 of 5% is normal fibrinolysis”", "Over 3% defines hyperfibrinolysis in trauma, with about a tenfold rise in mortality; give tranexamic acid."),
    ("“Factor IX, XI or XIII deficiency is typical of shock”", "Factor V is the one most consistently depleted, because activated protein C cleaves Va."),
  ],
  decode=[
    ("Polytrauma, minimal crystalloid, coagulopathic on admission — mechanism? [DocT GT]", "Systemic protein C activation in shock (11% right)."),
    ("Profound shock, oozing from venepuncture sites despite transfusion — primary mechanism of the acute coagulopathy? [DocT GT]", "Thrombin–thrombomodulin–protein C activation."),
    ("Which clotting factor deficiency is most consistent in haemorrhagic shock? [DocT GT]", "Factor V."),
    ("TEG LY30 5% in trauma — interpretation? / early marker of coagulopathy? [DocT GT, PYQ]", "Hyperfibrinolysis with about a tenfold mortality rise; fibrinogen is the early marker."),
  ],
  extra=[
    dict(q="What is the endotheliopathy of trauma, and why does it favour plasma over crystalloid?", a="Shock and the catecholamine surge shed the endothelial glycocalyx (syndecan-1 rises and predicts death), causing capillary leak, autoheparinisation and fibrinolysis, and later ARDS and multi-organ failure. Plasma helps restore the glycocalyx; crystalloid worsens the shedding."),
  ],
  punch="The bleeding patient arrives anticoagulated by his own shock: thrombomodulin turns thrombin into a protein C activator, factor V and fibrinogen fall, and fibrinolysis runs. Dilution, cold and acid come later and are the part we cause.",
)

L['POLY-13'] = dict(
  sub="Polytrauma → Lethal triad → Lactate and base deficit",
  step=1,
  intro="Step 1 also needs a measure of how deep the shock is. Pressure and pulse lag behind blood loss, so lactate and base deficit are used to grade hypoperfusion and to judge whether resuscitation is working. Both NEET 2025 recall questions are here: one on what a lactate of 3 means for the next step, one on the base deficit of each ATLS shock class.",
  parts=[
    ('a', "**Initial lactate and its clearance over 6 hours independently predict death; over 3 mmol/L had a sensitivity of 0.81 and specificity of 0.73 for 24-hour mortality.** The exact figures vary between cohorts (one large trauma cohort, Dezman 2015, reported 0.86 and 0.73 for 3 mmol/L or more); the point is that a lactate of 3 or more picks up most early deaths. Lactate rises when tissue oxygen delivery is inadequate, so it detects ‘occult’ shock in a patient whose pressure is still normal. The trend matters more than a single value: falling lactate means resuscitation is reaching the tissues, so the response to a raised value is to resuscitate and repeat it."),
    ('b', "**Alcohol raises it.** Ethanol metabolism increases the NADH/NAD⁺ ratio, which pushes pyruvate to lactate. The rise is usually modest, so a high lactate in an intoxicated trauma patient should still be treated as shock until proven otherwise."),
    ('c', "**Base excess is the better biochemical predictor: mild −2 to −5, moderate −6 to −9, severe −10 or worse.** Base deficit measures the total metabolic acid load, not only lactate, and is less affected by alcohol. These mild/moderate/severe bands are an older grading. Questions on the ATLS shock classes use the ATLS 10th edition bands instead: class I 0 to −2, class II −2 to −6, class III −6 to −10, class IV −10 or worse (mEq/L)."),
  ],
  mimic=[
    ("Card’s base excess severity bands vs ATLS class bands", "Card: −2 to −5, −6 to −9, −10 or worse. ATLS: I 0 to −2, II −2 to −6, III −6 to −10, IV −10 or worse. Answer a ‘shock class’ question with the ATLS bands."),
  ],
  traps=[
    ("“SBP 90 and lactate 3 after a crash: go for damage control surgery”", "That is early shock, not extremis; continue resuscitation and repeat the lactate. Damage control is for the patient with the triad (POLY-14)."),
    ("“Base deficit in class III shock is −10 or more”", "Class III is −6 to −10; −10 or worse is class IV."),
  ],
  decode=[
    ("Road crash, BP 90/60, lactate 3 mmol/L — next step? [NEET 2025]", "Further resuscitation and repeat the lactate."),
    ("Base deficit in class III shock? [NEET 2025]", "−6 to −10 mEq/L (ATLS 10th edition)."),
  ],
  punch="Lactate and base deficit see shock before the blood pressure does, and their clearance shows that resuscitation is working. For a class question use the ATLS bands: class III is −6 to −10.",
)

L['POLY-14'] = dict(
  sub="Polytrauma → Damage control → Indications",
  step=3,
  intro="Step 3 begins with choosing who gets damage control rather than complete repair. The choice is driven by physiology: a patient who is cold, acidotic and coagulopathic will die on the table during a long operation, whatever the anatomy. The one linked question (NEET 2025) tests the other side: a patient in early shock who does not yet need it.",
  parts=[
    ('a', "**Anatomical: ISS over 36; penetrating abdomen or chest; open pelvic fracture; long-bone fracture with head injury or lung contusion; truncal haemorrhage, amputation.** These are injuries that predict massive bleeding or a long operation, or in which a second hit (long-bone fixation in a patient with head or lung injury) would be dangerous."),
    ('b', "**Physiological: weak or absent radial pulse; core under 35 °C; SBP under 100, HR over 100; P/F under 250; urine under 50 mL/h.** These show that compensation is failing. The temperature threshold here is higher than the triad’s 34 °C, because the aim is to stop before the patient reaches it."),
    ('c', "**Laboratory: lactate over 2.5 mmol/L; platelets under 90,000; fibrinogen under 1 g/L; PT over 16 s, INR over 1.5; Hb under 11; pH under 7.2.** These measure the depth of shock and the coagulopathy already present. Low fibrinogen is the trigger (your notes print it the other way). The European guideline recommends damage control surgery for any severely injured patient in haemorrhagic shock, and also for hypothermia, acidosis, inaccessible major injury or a long procedure."),
  ],
  mimic=[
    ("Damage control vs early total care", "Damage control for the physiologically exhausted (triad, ongoing bleeding); early total care for the stable patient whose lactate has normalised (under about 2.5)."),
  ],
  traps=[
    ("“Any hypotension after trauma means damage control surgery”", "BP 90/60 with lactate 3 is early shock: resuscitate and reassess first."),
    ("“Fibrinogen over 1 g/dL triggers damage control”", "It is LOW fibrinogen, under 1 g/L, that does."),
  ],
  decode=[
    ("Road crash, BP 90/60, lactate 3: early total care, damage control surgery, more tests, or resuscitate and repeat lactate? [NEET 2025]", "Resuscitate and repeat the lactate."),
  ],
  punch="Damage control is chosen by physiology: the cold, acidotic, coagulopathic or persistently shocked patient gets a short operation; the patient in early shock is resuscitated first and reassessed.",
)

L['POLY-15'] = dict(
  sub="Polytrauma → Damage control → Resuscitation",
  step=3,
  intro="Step 3 continues with how the patient is resuscitated until the bleeding is controlled. Three ideas run together: accept a lower pressure so clots are not blown off, avoid fluids that dilute clotting factors, and give blood products early in a ratio close to whole blood. Five real questions test these, including a NEET 2025 stem on the cornerstone of the massive transfusion protocol.",
  parts=[
    ('a', "**Permissive hypotension: SBP 70–90 (or MAP 50), normal mentation, palpable pulses, until bleeding is controlled; follow lactate and ScvO₂.** A higher pressure raises flow through the injured vessel and can dislodge a fresh clot, and the fluid needed to reach it dilutes factors. The pressure is only ‘low enough’ if the brain and tissues are still perfused, hence mentation, a radial pulse and lactate clearance. The European guideline (6th edition, 2023) sets SBP 80–90 mmHg, which it equates to MAP 50–60 (POLY-23); noradrenaline can be added if fluids alone fail to reach it."),
    ('b', "**Not in TBI or spinal cord injury: keep MAP 80 or more if GCS 8 or less.** An injured brain or cord has lost autoregulation, so cerebral and cord perfusion follow the arterial pressure; a single episode of hypotension worsens outcome after head injury."),
    ('c', "**Restrict crystalloid: big volumes worsen bleeding (dilution, clot disruption), oedema and hepatocellular injury.** Crystalloid carries no oxygen and no clotting factors and leaks out of the circulation. Its only early role is small amounts to keep a pressure while blood is fetched. A patient still hypotensive after the first litre or so needs blood, not more crystalloid."),
    ('d', "**Haemostatic resuscitation: blood products first, RBC:FFP:platelets about 1:1:1.** Giving plasma and platelets with the red cells from the start replaces what is being lost, in the proportions of whole blood. Cryoprecipitate is not part of the ratio; it is given for fibrinogen under 1.5 g/L (POLY-21)."),
    ('e', "**Penetrating torso: a restrictive policy (SBP 60–70) lowers bleeding and 28-day mortality.** The classic trial is Bickell (1994): penetrating torso injury with SBP 90 or less, fluids delayed until the operating room, survival to discharge 70% vs 62%, with fewer complications. A later trial targeting MAP 50 vs 65 mmHg during surgery reported fewer early post-operative deaths at its interim analysis (Morrison 2011), but the final report (Carrick 2016, 168 patients) found no difference in 24-hour or 30-day mortality, only less blood and fluid use. The figures on the card are not those of either trial; the principle of tolerating a low pressure until surgical control is the same."),
  ],
  mimic=[
    ("Permissive hypotension vs no resuscitation", "The aim is the lowest pressure that still perfuses the brain and tissues, not ignoring shock; mentation, a pulse and lactate are the checks."),
    ("Blood products in ratio vs whole blood", "Components in 1:1:1 approximate whole blood. Prehospital low-titre O whole blood was not better than components in TOWAR (NEJM 2026); either is acceptable."),
  ],
  traps=[
    ("“Restore normotension with crystalloid before haemorrhage control”", "That disrupts clots and dilutes factors; permissive hypotension is the answer."),
    ("“Permissive hypotension is fine with a head injury”", "Contraindicated: keep MAP 80 or more."),
    ("“Give red cells only until Hb is over 10, then plasma”", "Products are given together in a balanced ratio from the start."),
    ("“Add 6 units of cryo with 6 units of red cells”", "The ratio is plasma and platelets; cryo is for low fibrinogen."),
  ],
  decode=[
    ("Penetrating abdomen, SBP 82, active bleeding, before haemorrhage control — strategy? [DocT GT]", "Permissive hypotension."),
    ("Polytrauma, still hypotensive after 2 L, Hb 6.8, INR 2.0 — cornerstone of the MTP? [NEET 2025]", "Products in a balanced ratio approximating whole blood."),
    ("6 units of red cells given — what else improves success? [DocT GT]", "FFP and platelets, both (94% right)."),
    ("Which parameters guide adequacy of resuscitation? [DocT GT]", "All: lactate clearance, urine output, SBP 90 or more."),
  ],
  extra=[
    dict(q="Why is blood the only colloid used in trauma?", a="Starches increase kidney injury and mortality (CHEST, 6S) and impair clotting; gelatins cause anaphylaxis; albumin raised mortality in TBI (SAFE-TBI). Hypertonic saline is used only for raised ICP."),
  ],
  punch="Until bleeding stops: accept SBP 80–90 (MAP 80 or more if the brain is injured), keep crystalloid to a minimum, and give red cells, plasma and platelets together in about 1:1:1.",
)

L['POLY-16'] = dict(
  sub="Polytrauma → Damage control → Surgery, rewarming, haemorrhage control, REBOA",
  step=4,
  intro="Step 4 is stopping the bleeding itself, because no amount of resuscitation replaces it. Eight real questions are linked here, most of them about the pelvis (binder, packing, embolisation), the stages of damage control surgery and REBOA. The common thread is that the first operation is short and aims only at bleeding and contamination.",
  parts=[
    ('a', "**Temporary sacrifice of anatomy to save physiology: (1) abbreviated laparotomy to control bleeding and contamination, (2) ICU resuscitation, (3) planned re-operation for definitive repair.** The first operation packs the liver, ligates or shunts vessels, staples bowel and closes the abdomen temporarily, in about an hour. The ICU then rewarms and corrects coagulopathy and acidosis; the patient returns at about 24–48 hours for repair. Five-stage versions add stage 0 (‘ground zero’: recognising the need in the emergency department) and a final stage of definitive abdominal-wall closure."),
    ('b', "**Rewarming: passive external (blankets, warm room); active external (forced air); active internal (warm IV fluids, warm peritoneal lavage).** Prevention is easier than rewarming: all fluids and products go through a warmer and the patient is covered after exposure. In the profoundly cold, active internal methods or extracorporeal rewarming are used."),
    ('c', "**Pelvic binder, compressive dressings, tourniquets; surgery is the gold standard; interventional radiology; pelvic packing or embolisation if unstable despite a binder.** A binder centred on the greater trochanters closes an open-book pelvis, reduces its volume and holds clot; it stays on until a fracture is excluded on imaging or the pelvis is fixed or embolised. A pelvic bleed with a negative FAST is retroperitoneal: laparotomy does not reach it, so after the binder the next steps are angiography with embolisation (arterial bleeding) or preperitoneal packing (venous plexus bleeding, the commoner source), not fixation or saline to a target MAP."),
    ('d', "**REBOA: balloon in the aorta via the femoral artery; zone 3 (infrarenal to the bifurcation; notes: IMA to bifurcation) for pelvic bleeding; zone 1 (descending thoracic) for abdominal bleeding.** Zone 1 runs from the left subclavian to the coeliac trunk, zone 2 from the coeliac to the lowest renal artery (not used), zone 3 from the lowest renal artery to the bifurcation. The balloon stops flow below it and supports cerebral and coronary perfusion, buying minutes for surgery or embolisation; it is useless for bleeding above it (thoracic aorta, subclavian, intracranial). Its benefit is doubtful: UK-REBOA (JAMA 2023, mostly blunt trauma) was stopped for harm, 90-day mortality 54% vs 42%. The European guideline only suggests ‘considering’ it for non-compressible life-threatening bleeding."),
  ],
  table=dict(title="Pelvic bleeding with haemodynamic instability",
    head=["Situation", "Next step"],
    rows=[["Suspected pelvic fracture, hypotensive", "Binder now, with resuscitation"],
          ["Binder on, FAST negative, still unstable", "Angioembolisation or preperitoneal packing"],
          ["Binder on, FAST positive, unstable", "Laparotomy (with packing of the pelvis)"],
          ["Haematuria, unstable, intraperitoneal bladder rupture", "Open repair after binding the pelvis"]]),
  mimic=[
    ("REBOA vs resuscitative thoracotomy", "Both occlude the aorta. REBOA is endovascular from the groin for bleeding below the diaphragm; thoracotomy opens the chest and is needed for tamponade or chest bleeding."),
    ("Angioembolisation vs preperitoneal packing", "Embolisation treats arterial bleeding (a blush on CT); packing treats venous and bony bleeding and is faster where angiography is not available."),
  ],
  traps=[
    ("“Remove the binder once the patient is stable, FAST is negative or the pelvis does not spring”", "Only after a fracture is excluded on imaging (or after fixation/embolisation); springing dislodges clot and FAST misses retroperitoneal blood. 75% right on DocT GT."),
    ("“Binder on and still hypotensive: fix the pelvis internally or get a CT angiogram first”", "Packing or angioembolisation is the damage control step; CT is for the stable patient."),
    ("“REBOA helps a thoracic aortic or subclavian bleed”", "It controls bleeding only below the balloon: pelvic (internal iliac) and abdominal."),
    ("“REBOA has proven benefit”", "UK-REBOA showed probable harm; it is a bridge used in selected centres."),
  ],
  decode=[
    ("Hypotensive, FAST negative, open-book pelvis on X-ray — next step? [DocT GT]", "Pelvic binder and interventional radiology for angiography (78% right)."),
    ("Open-book pelvis, binder on, MAP 55 after 2 units, FAST negative — damage control step? [DocT GT]", "Preperitoneal packing or angioembolisation."),
    ("Femoral access and an aortic balloon / temporising control of non-compressible torso bleeding — which? REBOA most useful for which site? [DocT GT]", "REBOA; internal iliac (pelvic) bleeding."),
    ("When can the pelvic binder be removed? / match the stages of damage control surgery [DocT GT]", "After radiological exclusion of fracture; ground zero → abbreviated surgery → ICU → planned re-look → closure."),
  ],
  punch="Damage control surgery stops bleeding and contamination quickly and leaves the repair for later. For the pelvis: binder first, and if still unstable with a negative FAST, packing or embolisation; REBOA is a temporary bridge with doubtful benefit.",
)

L['POLY-17'] = dict(
  sub="Polytrauma → Damage control → Fluid trials",
  step=3,
  intro="Step 3 also rests on the trials that removed colloids from trauma resuscitation. No real question is linked to this card; the trials are asked as the reason behind ‘no albumin in TBI’ and ‘no starch’.",
  parts=[
    ('a', "**SAFE 2004 (ICU): saline vs 4% albumin, 28-day mortality similar.** Albumin was safe in general ICU patients but not better, so there was no reason to pay for it."),
    ('b', "**SAFE-TBI 2007: albumin had higher mortality at 24 months.** In the TBI subgroup, deaths were about a third vs a fifth, mainly in severe TBI. Hypotonic 4% albumin is thought to raise intracranial pressure."),
    ('c', "**FIRST 2011 (trauma): saline vs HES 130/0.4, HES needed less volume and gave lower lactate in penetrating injury; mortality similar.** It was small, and its kidney finding (less injury with starch in penetrating trauma) was not repeated in larger trials."),
    ('d', "**CHEST 2012: saline vs 6% HES, mortality similar, more renal replacement therapy with HES.** With 6S (more deaths with starch in sepsis), this ended routine starch use."),
    ('e', "**CRYSTAL 2013 (shock): crystalloid vs colloid, 28-day mortality similar.** The 90-day mortality was lower with colloid, but that was a secondary outcome and is not taken as proof."),
  ],
  mimic=[
    ("SAFE vs SAFE-TBI", "Same trial: neutral overall, harmful in the head-injured subgroup."),
  ],
  traps=[
    ("“HES protects the kidneys in trauma (FIRST)”", "The larger trials (CHEST, 6S) showed more kidney injury with starch."),
  ],
  decode=[
    ("Preferred fluid in TBI; which fluid raised mortality in TBI? [pattern]", "Isotonic crystalloid; albumin (SAFE-TBI)."),
    ("Which trial showed more RRT with starch? [pattern]", "CHEST (6% HES 130/0.4)."),
  ],
  punch="Albumin is neutral in general ICU patients but harmful in TBI, and starch damages the kidney; in trauma the only colloid is blood.",
)

L['POLY-18'] = dict(
  sub="Polytrauma → Massive transfusion → Definitions, emergency blood, ratios, prediction",
  step=5,
  intro="Step 5 is where blood replaces fluid. This is the most-asked card in the deck (11 questions): when to activate the protocol, which group to give before the patient’s group is known, which ratio, and which score predicts the need. The lowest scores (13% and 18%) were on plasma compatibility and on a GT stem printed with two identical options.",
  parts=[
    ('a', "**10 or more red cell units in 24 h; or more than 4 units in 1 h with ongoing need; or more than 50% of blood volume in 3 h.** The 24-hour definition is retrospective and biased by survival (those who die early never reach 10 units), so the rate-based definitions are more useful clinically. In practice, the protocol is activated on clinical grounds or a score (part d), not after 10 units."),
    ('b', "**Group O red cells and group AB plasma until the group is known.** Red cell compatibility is about antigens on the donor cells: group O cells carry neither A nor B. Plasma compatibility is the reverse, about antibodies in the donor plasma: AB plasma has neither anti-A nor anti-B, so it is universal, and its RhD group does not matter because plasma contains no red cells. O RhD-positive cells are given to men and older women; O RhD-negative is kept for girls and women of child-bearing age to avoid anti-D sensitisation. Platelets carry a few red cells, so an RhD-negative woman of child-bearing age should get RhD-negative platelets, or anti-D. After several units of group O, keep giving group O even when the group comes back A, B or AB, because transfused anti-A and anti-B could haemolyse type-specific cells; switch only when the laboratory says it is safe."),
    ('c', "**PROPPR: 1:1:1 vs 1:1:2, no difference in 24-hour or 30-day mortality, but fewer exsanguination deaths and more haemostasis. PROMMTT: higher plasma and platelet ratios linked to lower early mortality.** PROPPR (JAMA 2015, 680 patients): 24-hour mortality 12.7% vs 17.0% and 30-day 22.4% vs 26.1%, neither significant; deaths from exsanguination at 24 hours 9.2% vs 14.6%, and haemostasis 86% vs 78%, with no more complications. PROMMTT (observational) found that high ratios mattered in the first 6 hours, when haemorrhagic deaths happen, and not after 24 hours. Prehospital plasma helped in PAMPer (air transport, 30-day mortality 23% vs 33%)."),
    ('d', "**TASH (7 variables: SBP, HR, free abdominal fluid, pelvic or long-bone fracture, sex, Hb, base excess; 0–28). ABC score: SBP under 90, HR over 120, penetrating mechanism, positive FAST; 2 or more → activate.** The ABC score needs no laboratory test, so it is the fastest bedside tool; at 2 or more it has a sensitivity of about 75% and specificity of about 86%. TASH needs Hb and base excess; a score of 16 or more corresponds to roughly a 50% probability of massive transfusion and is the usual activation threshold. TEG and ROTEM guide which products, not whether to start."),
  ],
  table=dict(title="Emergency products before the group is known",
    head=["Product", "Universal donor", "Why"],
    rows=[["Red cells", "Group O (Rh-positive for men and older women)", "No A or B antigen on the cells"],
          ["Plasma", "Group AB (Rh irrelevant)", "No anti-A or anti-B in the plasma"],
          ["Platelets", "Rh-negative for girls and women of child-bearing age", "Contain a few red cells"]]),
  mimic=[
    ("Red cell vs plasma compatibility", "Cells: O is universal (no antigens). Plasma: AB is universal (no antibodies)."),
    ("ABC score vs TASH vs shock index", "ABC: four bedside items, no labs, fastest. TASH: needs Hb and base excess. Shock index (HR ÷ SBP over 1) flags shock but is not a massive transfusion score."),
  ],
  traps=[
    ("“O RhD-negative FFP for an O RhD-negative woman”", "Group O plasma has anti-A and anti-B; AB plasma is universal and the RhD of FFP does not matter. Only 13% chose AB RhD-positive FFP on DocT GT."),
    ("“Red cells, plasma and cryo in equal numbers”", "The ratio is red cells : plasma : platelets. The DocT GT stem printed options B and C identically (18% right); choose the platelets option."),
    ("“Switch to the patient’s own group AB as soon as it is known after 6 units of O”", "Continue group O until the laboratory confirms no significant anti-A/B; 63% right."),
    ("“Wait for cross-matched blood, or give a fourth litre of crystalloid first”", "Give uncrossmatched group O (Rh-positive in a man) now."),
    ("“4:1:1 or 1:1:2 is the ideal ratio”", "1:1:1."),
  ],
  decode=[
    ("Stab wound, SBP 85, HR 125, FAST positive — next step? [DocT GT]", "Activate the massive transfusion protocol (64% right)."),
    ("Which bedside score predicts massive transfusion fastest, without laboratory tests? [DocT GT]", "ABC score (66% right)."),
    ("Woman O RhD-negative bleeding at caesarean — most suitable product? / 6 units O-negative given, group returns AB+ [DocT GT]", "FFP group AB RhD-positive; continue group O."),
    ("Hypotensive after 3 L of crystalloid — which statement is right? [NEET 2025]", "Transfuse type O Rh-positive blood (not wait for cross-match, not more crystalloid)."),
  ],
  punch="Activate on the bedside picture or an ABC score of 2, start with group O cells and AB plasma, and run red cells, plasma and platelets at 1:1:1: in PROPPR this did not change 30-day mortality but cut deaths from exsanguination.",
)

L['POLY-19'] = dict(
  sub="Polytrauma → Massive transfusion → Ending the protocol",
  step=5,
  intro="Step 5 ends with stopping the fixed ratio. Once surgical control is achieved, products are given to laboratory or viscoelastic targets instead of by formula. The two linked questions are about viscoelastic tests, and the one most people got wrong (38%) asked which viscoelastic finding predicts death.",
  parts=[
    ('a', "**Red cells: stop at Hb about 10 g/dL (notes).** The European guideline target during bleeding is Hb 7–9 g/dL (POLY-23); the higher figure in your notes is a stop point for the protocol, not a transfusion trigger."),
    ('b', "**FFP: stop when PT is under 18 s and PTT under 35 s.** Plasma replaces all the soluble factors; once PT and PTT approach normal, more plasma adds volume without benefit."),
    ('c', "**Platelets: stop when the count is above target (notes print 150,000).** The guideline targets are over 50 × 10⁹/L with ongoing bleeding and over 100 in TBI; 150,000 is a generous stop point."),
    ('d', "**Cryoprecipitate: stop at fibrinogen over 100 mg/dL (1 g/L).** Current European practice uses a higher trigger, Clauss fibrinogen 1.5 g/L or less, or a low FIBTEM A5 on ROTEM, because fibrinogen falls first and furthest (POLY-21)."),
  ],
  mimic=[
    ("Viscoelastic tests vs PT/INR", "TEG/ROTEM are whole-blood, run at body temperature, give results in 10–15 minutes and show clot strength and fibrinolysis; PT/INR is plasma-based, slow and misses both. In the ITACTIC trial (trauma, 2021), guiding treatment by viscoelastic tests did not improve survival free of massive transfusion at 24 hours or mortality over conventional tests. Cochrane reviews, mostly of cardiac surgery, suggest lower mortality, but on very low-certainty evidence."),
  ],
  traps=[
    ("“Increased fibrinolysis is the viscoelastic finding most associated with death”", "Low clot strength (TEG MA, ROTEM MCF or A5) is; most patients have fibrinolytic shutdown, not hyperfibrinolysis. Only 38% got this on DocT GT."),
    ("“INR over 1.2 is a viscoelastic variable”", "INR is a conventional plasma test."),
  ],
  decode=[
    ("Which VHA finding is most strongly associated with mortality in trauma coagulopathy? [DocT GT]", "Decreased clot strength (38% right)."),
    ("Which test rapidly assesses clot dynamics in trauma? [DocT GT]", "TEG (100% right)."),
  ],
  punch="After surgical control, stop the formula and treat to targets; on viscoelastic testing the number that predicts death is low clot strength, not fibrinolysis.",
)

L['POLY-20'] = dict(
  sub="Polytrauma → Drugs → Tranexamic acid",
  step=6,
  intro="Step 6 opens with the drug that every bleeding trauma patient should get. Tranexamic acid blocks the binding of plasminogen to fibrin and so stops clots being broken down, the hyperfibrinolysis of step 2. Three questions are linked; the one only 36% answered correctly hid it among options for a diffusely bleeding liver, and the NEET 2025 stem tested the time window.",
  parts=[
    ('a', "**CRASH-2: 1 g over 10 minutes, then 1 g over 8 hours; fewer bleeding deaths (about 15%).** CRASH-2 (20,207 bleeding adults, SBP under 90 or HR over 110, within 8 hours of injury) reduced death from bleeding from 5.7% to 4.9% and all-cause death a little, with no rise in vascular occlusive events. It works in blunt and penetrating trauma alike."),
    ('b', "**Within 3 hours of injury; after 3 hours it increased bleeding deaths.** The benefit was greatest when given within 1 hour (bleeding deaths RR 0.68), still present at 1–3 hours (RR 0.79), and reversed after 3 hours (RR 1.44), probably because fibrinolysis gives way to shutdown and a prothrombotic state. The 8 hours on the card is the length of the second infusion, not the window."),
    ('c', "**CRASH-3: benefit in mild-to-moderate TBI (given early), none in severe TBI.** CRASH-3 (12,737 patients with TBI, within 3 hours) did not reduce head-injury deaths overall (18.5% vs 19.8%, not significant), but did in GCS 9–15 and when given early; in GCS 3 or with bilateral unreactive pupils there was no effect. There was no excess of thrombotic events."),
    ('d', "**Give as early as possible to anyone bleeding or at risk; prehospital first dose.** The European guideline (Grade 1A) gives TXA as soon as possible, en route if feasible, within 3 hours, and not waiting for viscoelastic results. PATCH-Trauma (NEJM 2023, prehospital TXA) did not improve functional outcome at 6 months; deaths at 24 hours and 28 days were lower with TXA as secondary outcomes, and 6-month mortality did not differ significantly."),
  ],
  mimic=[
    ("CRASH-2 vs CRASH-3 vs WOMAN", "CRASH-2: bleeding trauma, within 3 h. CRASH-3: TBI, helps mild-moderate. WOMAN: postpartum haemorrhage, same dose, same 3-hour window."),
  ],
  traps=[
    ("“TXA works if given within 8 (or 12) hours”", "Within 3 hours; after 3 hours it increased bleeding deaths. The NEET 2025 stem asked which statement is incorrect: ‘within 12 hours, only in blunt or penetrating trauma’."),
    ("“Diffuse liver bleeding at laparotomy: cryo in equal numbers, PCC or vitamin K”", "Tranexamic acid is the useful adjunct; only 36% chose it."),
    ("“TEG shows hyperfibrinolysis and weak clot: give FFP or platelets”", "Hyperfibrinolysis is treated with TXA (73% right)."),
  ],
  decode=[
    ("Multiple liver lacerations with diffuse bleeding — useful adjunct along with volume? [DocT GT]", "Tranexamic acid (36% right)."),
    ("TEG hyperfibrinolysis, weak clot, normal platelets — targeted intervention? [DocT GT]", "Tranexamic acid."),
    ("Which is incorrect about TXA in trauma? [NEET 2025]", "‘Within 12 hours and only in blunt or penetrating trauma’; 1 g over 10 min, 1 g over 8 h, for all with suspected significant bleeding are correct."),
  ],
  punch="Tranexamic acid: 1 g over 10 minutes then 1 g over 8 hours, as early as possible and never after 3 hours, because late doses increased bleeding deaths in CRASH-2.",
)

L['POLY-21'] = dict(
  sub="Polytrauma → Drugs → Fibrinogen concentrate vs cryoprecipitate",
  step=5,
  intro="Step 5 also covers the first factor to replace. Fibrinogen falls first and furthest in bleeding trauma (step 2), and it can be replaced from two sources. The two linked questions ask the concentrate dose when the level is unknown and which product to give for a fibrinogen of 70 mg/dL.",
  parts=[
    ('a', "**Source: concentrate is a lyophilised, pathogen-reduced powder; cryoprecipitate comes from controlled thawing of FFP.** Thawing FFP at 1–6 °C leaves a cold-insoluble precipitate rich in fibrinogen, which is collected and refrozen."),
    ('b', "**Contents: concentrate is fibrinogen only; cryoprecipitate contains fibrinogen, factor VIII, von Willebrand factor and factor XIII.** That is why cryo was historically used for haemophilia A and von Willebrand disease, and why it is the cheaper alternative where concentrate is not available."),
    ('c', "**Dose: concentrate (target − measured, mg/dL) ÷ 1.7 mg/kg, often about 70 mg/kg (notes); cryoprecipitate 1 unit per 5–10 kg.** The divisor 1.7 is the expected rise in mg/dL for each mg/kg; when the level is unknown, 70 mg/kg is the labelled starting dose. In trauma the European guideline suggests an initial 3–4 g of fibrinogen, equal to 15–20 single-donor units of cryo, when Clauss fibrinogen is 1.5 g/L or less or ROTEM shows a functional deficit."),
    ('d', "**Pros and cons: concentrate is fast and needs no matching; cryo has limited availability, is allogeneic, needs thawing and is group-matched.** Concentrate has a known, standard fibrinogen content and a lower infection risk. Neither has shown a survival benefit when given early and empirically in a randomised trial: CRYOSTAT-2 (JAMA 2023, 1,604 patients) found no difference in 28-day mortality with early high-dose cryo (25.3% vs 26.1%). The ‘lower 6-hour mortality’ with concentrate comes from a registry matched-pairs study (Wafaisade 2013), in which mortality at discharge did not differ."),
  ],
  mimic=[
    ("Cryo vs FFP for low fibrinogen", "FFP contains fibrinogen at plasma concentration (about 2 g/L), so it cannot raise a low level without large volumes; cryo or concentrate is needed."),
  ],
  traps=[
    ("“Fibrinogen 70 mg/dL with oozing: FFP, PCC or rFVIIa”", "Cryoprecipitate (or concentrate); PCC contains no fibrinogen."),
    ("“Early empirical cryo improves survival”", "CRYOSTAT-2 was neutral."),
  ],
  decode=[
    ("Congenital afibrinogenaemia, level unknown — initial RiaSTAP dose? [DocT GT]", "70 mg/kg IV."),
    ("Septic patient bleeding, fibrinogen 70 mg/dL, platelets 92,000, INR 1.4 — product? [DocT GT]", "Cryoprecipitate 10 units."),
  ],
  punch="When fibrinogen is low (1.5 g/L or less in trauma), give cryoprecipitate or concentrate, about 3–4 g in an adult; FFP and PCC cannot replace it, and early empirical cryo did not save lives in CRYOSTAT-2.",
)

L['POLY-22'] = dict(
  sub="Polytrauma → Drugs → Calcium, factor VIIa, steroids in cord injury, antioxidants",
  step=6,
  intro="Step 6 continues with the other drugs. Calcium is the fourth corner of the triad, rFVIIa is a last resort, and steroids for cord injury are the classic question. The two linked questions ask about rFVIIa as a rescue agent and, with only 43% right, what improves neurological outcome after spinal cord injury.",
  parts=[
    ('a', "**Calcium is a cofactor for clotting, cardiac contractility and vascular tone; monitor every 10 units transfused; keep ionised Ca over 0.9 mmol/L (notes).** Citrate in each unit binds calcium, and a shocked liver clears citrate slowly, so ionised calcium falls with every unit. The European guideline keeps it in the normal range (1.1–1.3 mmol/L) and recommends calcium chloride; below 0.9 mmol/L is transfusion hypocalcaemia and below 0.8 risks arrhythmias."),
    ('b', "**rFVIIa: off-label, no outcome benefit, causes thrombosis, last resort only.** It needs fibrinogen, platelets, a normal pH, temperature and calcium to work, so it fails in exactly the patients who are given it too early. The European guideline does not recommend it first-line and suggests it only when bleeding and coagulopathy persist despite everything else."),
    ('c', "**NASCIS II: high-dose methylprednisolone within 8 h improved motor recovery; NASCIS III: 48 h better than 24 h if started at 3–8 h. Now not recommended (CNS, CAEP): harms, no long-term benefit.** The NASCIS benefits were found in post-hoc subgroups, while steroids increased infections, GI bleeding and hyperglycaemia. What does help the cord is perfusion: the traditional target is MAP 85–90 mmHg for 7 days (AO Spine 2024 suggests a floor of 75–80 and ceiling of 90–95 for 3–7 days)."),
    ('d', "**Vitamins A, C and E reduce inflammation; vitamin C may protect the kidneys.** This is weak, experimental evidence and is not part of any trauma guideline."),
  ],
  mimic=[
    ("Steroids vs MAP augmentation in acute cord injury", "Steroids: not recommended. Keeping MAP 85–90: suggested by guidelines and the answer to ‘what improves neurological outcome’."),
  ],
  traps=[
    ("“Methylprednisolone improves neurological outcome after cord injury”", "Not recommended; MAP augmentation is the answer (43% right on DocT GT)."),
    ("“SBP over 120 or CVP over 20 protects the cord”", "The target is MAP, about 85 mmHg or more."),
    ("“rFVIIa is first-line, or should be given early before surgery”", "It is an off-label rescue agent after surgery and full correction; 91% right."),
  ],
  decode=[
    ("Massive PPH despite uterotonics, sutures and MTP — which statement about rFVIIa is correct? [DocT]", "Off-label rescue agent for life-threatening haemorrhage."),
    ("88-year-old with cervical cord injury — what improves neurological outcome? [DocT GT]", "Maintain MAP over 85 mmHg."),
  ],
  punch="Give calcium chloride to keep ionised calcium normal during transfusion, keep rFVIIa as an off-label last resort, and protect an injured cord with a MAP of about 85, not with steroids.",
)

L['POLY-23'] = dict(
  sub="Polytrauma → Guideline → European bleeding-in-trauma guideline",
  step=6,
  intro="Step 6 gathers the numbers into the European guideline (6th edition, 2023), the reference most of these targets come from. The one linked question tests its pelvic recommendation, which is in the card’s watch line: packing or embolisation for the patient who stays unstable despite a binder.",
  parts=[
    ('a', "**Restricted volume replacement to a target SBP of 80–90 mmHg until bleeding is controlled (no TBI).** Grade 1B. This is a little higher than the 70–90 often taught (POLY-15)."),
    ('b', "**Severe TBI (GCS 8 or less): MAP 80 mmHg or more.** Grade 1C. Cerebral perfusion follows arterial pressure once autoregulation is lost."),
    ('c', "**Vasopressors with fluids for life-threatening hypotension.** The guideline names noradrenaline, added when fluids alone do not reach the target, and dobutamine if the myocardium is failing. A vasopressor reduces the fluid needed to hold the pressure."),
    ('d', "**Isotonic crystalloid; avoid excess 0.9% saline.** The 6th edition recommends starting with 0.9% saline or a balanced crystalloid (Grade 1B); its rationale adds that if saline is used it should be limited to about 1–1.5 L, because large volumes cause hyperchloraemic acidosis. Hypotonic solutions such as Ringer’s lactate are avoided in severe head injury."),
    ('e', "**Haemoglobin 7–9 g/dL.** Grade 1C. Higher targets add risk without benefit."),
    ('f', "**Start coagulation support with plasma:RBC at least 1:2, or fibrinogen concentrate plus RBC.** Either a plasma-based or a factor-concentrate strategy is accepted (Grade 1C), with a high platelet:RBC ratio; then goal-directed treatment guided by viscoelastic or laboratory tests."),
    ('g', "**TXA 1 g over 10 minutes then 1 g over 8 hours, within 3 hours.** Grade 1A, the strongest recommendation in the guideline: as soon as possible, en route if feasible, and not waiting for viscoelastic results."),
    ('h', "**Platelets over 50; over 100 with ongoing bleeding or TBI.** In the 6th edition the higher threshold of 100 × 10⁹/L applies to TBI; over 50 is the target with ongoing bleeding."),
  ],
  mimic=[
    ("European SBP 80–90 vs SBP 70–90 / MAP 50", "Both are permissive hypotension; the guideline number is 80–90 without TBI."),
  ],
  traps=[
    ("“Pelvic binder on and still hypotensive: internal fixation, CT angiogram, or saline to MAP 80”", "Preperitoneal packing or angioembolisation (the watch line)."),
    ("“Hb target 10 g/dL during bleeding”", "7–9 g/dL."),
  ],
  decode=[
    ("Open-book pelvis, binder on, MAP 55 after 2 units, FAST negative — damage control step? [DocT GT]", "Preperitoneal packing or angioembolisation."),
    ("European guideline BP target without TBI / with severe TBI? [pattern]", "SBP 80–90; MAP 80 or more."),
  ],
  extra=[
    dict(q="What does the European guideline say about fibrinogen, calcium and REBOA?", a="Give fibrinogen concentrate or cryo if Clauss fibrinogen is 1.5 g/L or less or viscoelastic tests show a deficit (initial 3–4 g); keep ionised calcium in the normal range with calcium chloride; consider REBOA only for non-compressible life-threatening bleeding (weak, 2C)."),
  ],
  punch="The European numbers: SBP 80–90 (MAP 80 or more in severe TBI), Hb 7–9, plasma:RBC at least 1:2 or fibrinogen, fibrinogen if 1.5 g/L or less, platelets over 50 (100 in TBI), TXA within 3 hours, calcium normal.",
)

L['POLY-24'] = dict(
  sub="Polytrauma → Sweep → True or false",
  step=6,
  intro="Step 6 closes with a sweep across both polytrauma decks. Three linked questions all test the shock index, which is statement b: they give a heart rate and systolic pressure and ask you to divide.",
  parts=[
    ('a', "**False: BP first falls in Class III (30–40% loss).** In class II the pulse rises and pulse pressure narrows but systolic pressure is maintained by vasoconstriction (POLY-09)."),
    ('b', "**True: a shock index over 1 predicts mortality.** Shock index = heart rate ÷ systolic pressure; normal is 0.5–0.7. It rises before the systolic pressure falls, so 118/105 (1.1) or 130/92 (1.4) already signals hypovolaemia despite a ‘normal’ pressure. Over 1 is abnormal and associated with transfusion need and death."),
    ('c', "**False: permissive hypotension is contraindicated in TBI.** The injured brain needs a MAP of 80 or more (POLY-15)."),
    ('d', "**False: TXA must be given within 3 hours.** After 3 hours it increased bleeding deaths in CRASH-2 (POLY-20)."),
    ('e', "**True: fibrinogen is the first factor to fall critically.** It is consumed, broken down by fibrinolysis and diluted (POLY-12)."),
    ('f', "**False: albumin raised mortality in TBI (SAFE-TBI).** Isotonic crystalloid is preferred (POLY-17)."),
    ('g', "**True: the Berlin definition needs AIS 3 or more in 2 or more regions plus at least one physiological factor.** The factors are SBP 90 or less, GCS 8 or less, base excess −6 or worse, INR 1.4 or more or PTT 40 s or more, and age 70 or more (POLY-02)."),
    ('h', "**False: ISS takes one injury per region (taking the three worst regardless of region is NISS).** ISS squares the highest AIS in each of the three most severely injured body regions and adds them; NISS squares the three highest AIS scores regardless of region, so it counts two severe injuries in the same region (POLY-04)."),
  ],
  mimic=[
    ("ISS vs NISS", "ISS: the worst injury in each of the three worst regions. NISS: the three worst injuries anywhere."),
  ],
  traps=[
    ("“SBP 105 and lactate 1.8 rule out early hypovolaemia”", "A shock index of 1.1 already signals it."),
    ("“Shock index 120/90 is 0.75, normal”", "It is 1.33, severe shock."),
  ],
  decode=[
    ("SBP 92, HR 130, CRT 3.5 s, lactate 2.2 — which index best suggests inadequate perfusion? [DocT GT]", "Shock index 1.4 (79% right)."),
    ("Trauma, cool, HR 118, SBP 105 — which index most suggests early hypovolaemia? [DocT GT]", "Shock index 1.1."),
    ("HR 120, SBP 90 — shock index and interpretation? [NEET 2025]", "1.33, severe shock."),
  ],
  punch="Divide pulse by systolic pressure: over 1 is shock even when the pressure looks normal. And the rest: BP falls in class III, no permissive hypotension or albumin in TBI, TXA within 3 hours, fibrinogen falls first.",
)

FLAGS = {
  'POLY-11': "b: the Cosgriff (1997) odds ratios and the 98% figure predict life-threatening coagulopathy (PT and PTT more than twice normal) in massively transfused patients, not death; the card calls them ‘independent predictors of death’ and ‘≈ 98% mortality’. The explanation states the real outcome.",
  'POLY-13': "c: the card’s mild/moderate/severe base excess bands are an older scheme; the NEET 2025 recall asks the ATLS 10th edition class bands (I 0 to −2, II −2 to −6, III −6 to −10, IV −10 or worse), which the explanation teaches. a: the 0.81/0.73 figures could not be traced; the closest source found (Dezman 2015, lactate ≥3 mmol/L for 24-hour death) reports sensitivity 0.86, specificity 0.73. The explanation says figures vary between cohorts.",
  'POLY-15': "a: SBP 70–90 differs from the European 6th edition target of SBP 80–90 (Grade 1B). Last line: ‘penetrating torso, SBP 60–70 lowers bleeding and 28-day mortality’ matches no trial I could identify; the evidence is Bickell 1994 (delayed fluids, survival to discharge 70% vs 62%) and the MAP 50 vs 65 intra-operative trial (fewer early post-operative deaths at the Morrison 2011 interim; no difference in 24-hour or 30-day mortality in the final Carrick 2016 report). The explanation teaches those.",
  'POLY-16': "d: REBOA is taught without its evidence; UK-REBOA (JAMA 2023) stopped for harm (90-day mortality 54% vs 42%), and the European guideline only suggests considering it (2C). Added in the explanation.",
  'POLY-18': "Card is correct. The linked DocT GT stem prints options B and C identically (‘RBC, plasma and cryo in equal numbers’), keyed C; the intended answer is 1:1:1 red cells : plasma : platelets. Watch line ‘TASH 16+ → over 50%’: by the TASH logistic model a score of 16 is about 50% (≈47%), so ‘about 50%’ is safer.",
  'POLY-19': "Stop points (Hb 10, platelets 150,000, fibrinogen 1 g/L) are from your notes and are more generous or older than the European 6th edition targets (Hb 7–9, platelets over 50 or over 100 in TBI, fibrinogen trigger 1.5 g/L or less). Watch line: ‘a Cochrane review found no proven mortality benefit’ is out of date: the Cochrane reviews (2016; update May 2026) found lower mortality with TEG/ROTEM-guided transfusion (2026: RR 0.76) but on very low-certainty evidence, mostly cardiac surgery. In trauma, ITACTIC (2021) showed no outcome difference.",
  'POLY-20': "Card is correct. d could add PATCH-Trauma (NEJM 2023): prehospital TXA did not improve 6-month function; 24-hour and 28-day deaths were lower as secondary outcomes, 6-month mortality not significantly different.",
  'POLY-21': "Watch line: ‘concentrate lowered 6-h mortality’ is from a TraumaRegister DGU matched-pairs study (Wafaisade 2013: 10.5% vs 16.7% at 6 h, no difference at discharge), not a trial; no RCT of fibrinogen concentrate in trauma has shown a mortality benefit. CRYOSTAT-2 is now published (JAMA 2023, neutral, 28-day mortality 25.3% vs 26.1%), no longer ongoing.",
  'POLY-22': "a: ionised Ca over 0.9 mmol/L (notes) is the threshold for transfusion hypocalcaemia; the European target is the normal range 1.1–1.3 (watch line agrees). c: AO Spine (2017) still offers a 24-hour methylprednisolone infusion within 8 h as an option; CNS/AANS 2013 recommend against. The linked question (MAP over 85) is not on the card and is taught in the explanation.",
  'POLY-23': "h: in the 6th edition (2023) the platelet target is over 50 with ongoing bleeding and over 100 × 10⁹/L in TBI; ‘over 100 with ongoing bleeding’ is 5th-edition wording. d: the 6th edition recommendation is ‘0.9% saline or balanced crystalloid’ (1B); ‘avoid excess 0.9% saline’ is not in the recommendation itself but matches its rationale (limit saline to about 1–1.5 L). a: the SBP 80–90 target is in the guideline (1B); the card’s ‘not in your notes’ tag is fine.",
  'POLY-24': "h: the reason is right but incomplete; ISS adds the SQUARES of the highest AIS in the three worst regions.",
}
