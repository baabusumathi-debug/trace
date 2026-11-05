# TOX02 — Paracetamol toxicity. Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Same fields as tox01_learn.py (sub, intro, parts, table, mimic, traps, decode, punch, extra).
# Audited 6 Nov against qpack/TOX02.md (real stems): decode from real stems, traps from low-% distractors, cuts.
L = {}

L['APAP-01'] = dict(
  sub="Toxicology → Dose & Mechanism → Dose thresholds",
  intro="Paracetamol is safe at therapeutic doses because the liver has more than enough capacity to make it harmless. Toxicity is a matter of dose per kilogram: once the ingested amount outruns that capacity, a toxic metabolite accumulates. The thresholds mark where risk begins, where it becomes near-certain, and how severe injury is defined.",
  parts=[
    ('a', "**Maximum therapeutic dose 4 g/day in adults; 75 mg/kg/day in children.** At these doses conjugation handles almost all of the drug, and the small oxidised fraction is mopped up by glutathione without depleting it."),
    ('b', "**Toxic single dose: >150 mg/kg, or 7.5–10 g in an adult.** Above this the conjugation pathways saturate, more of the dose is oxidised, and NAPQI uses up glutathione faster than the liver can make it (APAP-02)."),
    ('c', "**Liver failure almost certain above 350 mg/kg (untreated).** Glutathione is exhausted early and NAPQI binds hepatocyte proteins in large amounts; without N-acetylcysteine severe hepatotoxicity is the rule."),
    ('d', "**Severe hepatotoxicity: peak AST or ALT >1000 U/L.** A peak above 1000 marks substantial necrosis; it is a laboratory definition, and most such patients recover."),
    ('e', "**Peak level at 1.5–2 h normally; within 4 hours in overdose — later with opioids, anticholinergics or food.** Anything that slows gastric emptying delays the peak, which is why a 4-hour level is the earliest valid one (APAP-06)."),
  ],
  table=dict(title="Dose and what it means", head=["Dose", "Meaning"], rows=[["≤4 g/day (adult), 75 mg/kg/day (child)", "therapeutic"], ["**>150 mg/kg** or 7.5–10 g", "potentially toxic — assess and level"], ["**>350 mg/kg**", "severe hepatotoxicity near-certain untreated"], ["Peak AST/ALT **>1000 U/L**", "definition of severe hepatotoxicity"]]),
  mimic=[],
  traps=[
    ("“Toxicity is set by the number of tablets”", "It is set by mg/kg — 10 g is far more dangerous in a 45 kg woman than in a 90 kg man."),
    ("“ALT 600 meets severe hepatotoxicity”", "The definition is a peak above 1000 U/L."),
  ],
  decode=[
    ("Minimum potentially toxic acute dose [pattern]", ">150 mg/kg (7.5–10 g in an adult)."),
    ("How is severe hepatotoxicity defined? [pattern]", "Peak AST or ALT above 1000 U/L."),
  ],
  punch="Paracetamol is dosed by the liver’s capacity: above 150 mg/kg the safe pathways saturate and the toxic metabolite starts to win, and above 350 mg/kg it almost always wins unless N-acetylcysteine is given.",
)

L['APAP-02'] = dict(
  sub="Toxicology → Dose & Mechanism → Metabolism and injury",
  intro="Paracetamol itself does not damage the liver; one of its metabolites does. Normally that metabolite is made in small amounts and neutralised at once by glutathione. Injury happens when the dose is large enough to use up glutathione, and it happens where the metabolite is made — around the central vein.",
  parts=[
    ('a', "**90% glucuronidation and sulfation (non-toxic); 1–2% unchanged in urine; 5–9% oxidised (your notes’ text says 5–7%).** Of the conjugation routes, glucuronidation takes the larger share in adults, so it is the main reaction under normal conditions; sulfation is second. Conjugation attaches a water-soluble group so the drug can be excreted; the products are inert. Only the oxidised fraction is dangerous, and in overdose it grows because conjugation saturates."),
    ('b', "**NAPQI (N-acetyl-p-benzoquinone imine), made by CYP2E1.** NAPQI is a reactive electrophile that attacks the sulphydryl groups of cell proteins. CYP2E1 is the main enzyme, with contributions from CYP3A4 and CYP1A2."),
    ('c', "**Conjugation with glutathione to cysteine and mercapturic acid conjugates.** Glutathione donates its sulphydryl group to NAPQI, making a harmless conjugate excreted in urine. This handles only the small oxidised fraction — it is a rescue step, not a main route of metabolism."),
    ('d', "**Injury begins when glutathione stores fall by 70–80%: NAPQI binds cell proteins (adducts), mitochondria fail, and the cell necroses.** While glutathione lasts, NAPQI is captured before it reaches proteins. Below about a quarter of normal, NAPQI binds mitochondrial proteins, ATP fails and the cell dies — so the mechanism of paracetamol liver failure is accumulation of NAPQI."),
    ('e', "**Centrilobular (zone 3), where CYP450 is concentrated.** NAPQI is made where CYP2E1 is most abundant, around the central vein, so the necrosis is centrilobular and periportal (zone 1) cells are relatively spared."),
  ],
  table=dict(title="Where the dose goes", head=["Route", "Share", "Product"], rows=[["Glucuronidation (main) + sulfation", "**~90%**", "inert conjugates"], ["Unchanged in urine", "1–2%", "—"], ["CYP2E1 oxidation", "**5–9%**", "**NAPQI** → glutathione conjugate"]]),
  mimic=[],
  traps=[
    ("“The main pathway is CYP450 oxidation” or “conjugation to glutathione”", "Under normal conditions the main reaction is glucuronidation; CYP oxidation is a 5–9% minor route and glutathione only detoxifies its product. 42% of the DocT cohort got this right."),
    ("“The toxic metabolite is made by glucuronidation”", "Glucuronidation makes inert conjugates; NAPQI comes from CYP2E1 oxidation."),
    ("“Paracetamol injury is periportal”", "It is centrilobular, zone 3 — where CYP2E1 is concentrated."),
  ],
  decode=[
    ("Main reaction in paracetamol metabolism under normal conditions [DocT]", "Conjugation to glucuronic acid — not CYP oxidation, not glutathione."),
    ("Analgesic overdose with liver failure: mechanism [Marrow]", "Accumulation of NAPQI once glutathione is depleted."),
    ("Zone of necrosis [pattern]", "Zone 3, centrilobular."),
  ],
  punch="Most paracetamol is glucuronidated harmlessly; only the small CYP2E1 fraction makes NAPQI, which glutathione neutralises until about three-quarters of the store is gone — and because CYP2E1 sits around the central vein, that is where the liver dies.",
)

L['APAP-03'] = dict(
  sub="Toxicology → Dose & Mechanism → Risk factors",
  intro="Two things decide how much harm a given dose does: how fast NAPQI is made, and how much glutathione is there to meet it. Anything that speeds CYP oxidation or lowers glutathione raises the risk; anything that slows oxidation or boosts conjugation lowers it.",
  parts=[
    ('a', "**Raises: chronic alcohol.** Long-term drinking induces CYP2E1, so more NAPQI is made from the same dose, and the poor nutrition that goes with it lowers glutathione. Both levers move against the patient — which is why injury can occur even at doses near or below the usual maximum."),
    ('b', "**Raises: CYP inducers — anticonvulsants, antitubercular drugs — and tobacco.** Enzyme inducers increase oxidative metabolism. Isoniazid acts on CYP2E1; phenytoin, carbamazepine, phenobarbital and rifampicin induce other CYP isoforms that can also make NAPQI."),
    ('c', "**Raises: fasting and malnutrition.** Glutathione is built from amino acids, chiefly cysteine; a malnourished patient has smaller stores and less capacity for conjugation, so NAPQI overwhelms the defence sooner."),
    ('d', "**Raises: age over 40, Gilbert syndrome, repeated supratherapeutic dosing.** Older patients have less hepatic reserve. Gilbert syndrome reduces UGT1A1 activity, so less drug is glucuronidated (weak clinical evidence). Repeated dosing wears glutathione down over days (APAP-04)."),
    ('e', "**Lowers: childhood — more glutathione, more conjugation.** Children under about 10 clear paracetamol mainly by sulfation, whereas adults mainly glucuronidate; they sulfate efficiently and make glutathione readily, so less becomes NAPQI. The nomogram and NAC rules still apply to them."),
    ('f', "**Lowers: acute alcohol co-ingestion — it competes for CYP2E1.** Ethanol drunk at the same time occupies CYP2E1, so less paracetamol is oxidised while the alcohol is present. The same enzyme, once induced by chronic drinking, has the opposite effect."),
  ],
  table=dict(title="The two levers", head=["Factor", "Lever", "Effect"], rows=[["Chronic alcohol, inducers", "more NAPQI made", "↑ risk"], ["Fasting, malnutrition, chronic alcohol", "less glutathione", "↑ risk"], ["Acute alcohol", "CYP2E1 occupied", "↓ risk"], ["Childhood", "sulfation dominant, more glutathione", "↓ risk"]]),
  mimic=[
    ("Acute vs chronic alcohol", "Acute alcohol competes for CYP2E1 and protects; chronic alcohol induces CYP2E1 and depletes glutathione, and harms."),
  ],
  traps=[
    ("“Young children metabolise paracetamol mainly by glucuronidation, like adults”", "Under about 10 years sulfation is the predominant pathway; glucuronidation dominates only in adults. Only 31% of the DocT GT cohort got this right."),
    ("“Children are at higher risk because they are smaller”", "Dosed per kg, children are at lower risk: more sulfation and glutathione."),
    ("“Alcohol always increases paracetamol toxicity”", "Acute co-ingestion is protective; only chronic use increases risk."),
    ("“Risk factors mean a lower nomogram line in the UK”", "The UK abolished its separate high-risk line in 2012; everyone is treated above the single 100 line (APAP-06)."),
  ],
  decode=[
    ("3-year-old, 220 mg/kg: predominant pathway under 10 years [DocT GT]", "Sulfation."),
    ("Chronic alcoholic, repeated supratherapeutic use: why higher risk? [DocT GT]", "Increased CYP2E1 activity and low glutathione."),
    ("Chronic alcohol use disorder and overdose: most accurate statement [DocT]", "Risk increased, even at doses below the usual safe limit."),
  ],
  punch="Every risk factor either makes more NAPQI or leaves less glutathione to meet it — which is why chronic alcohol harms, acute alcohol protects, and small children, who sulfate rather than glucuronidate, tolerate accidental doses best.",
)

L['APAP-04'] = dict(
  sub="Toxicology → Dose & Mechanism → Repeated supratherapeutic ingestion",
  intro="Not every paracetamol poisoning is a single deliberate overdose. A patient in pain — a toothache, a fever — may take a little more than the maximum dose, several times a day, for several days. Each dose is small, but glutathione never recovers, and the patient comes in only once the liver is injured.",
  parts=[
    ('a', "**More dangerous: presents late with established injury, so severe hepatotoxicity and death are more frequent.** There is no dramatic event to bring the patient in, so the treatment window passes unnoticed; such patients often have risk factors that lowered glutathione already (APAP-03). A young patient dosing every 4 hours for pain who turns up with ALT in the thousands is the typical picture — paracetamol is the drug to screen for."),
    ('b', "**The nomogram does not apply: levels do not correlate with toxicity.** With many doses there is no single time zero, and much of the drug has already been metabolised, so a low level can coexist with severe injury."),
    ('c', "**NAC if more than 7.5 g in 24 h (4 g with risk factors), symptoms, a level above 20 µg/mL, or raised transaminases (>50) whatever the level.** A level above 20 µg/mL means drug is still circulating to make NAPQI; a raised ALT means injury has begun. Dose thresholds differ between guidelines (Australia–NZ: 10 g or 200 mg/kg in 24 h, or 6 g or 150 mg/kg a day for 48 h or more), but the level and ALT triggers are shared."),
  ],
  mimic=[
    ("Repeated ingestion vs staggered overdose", "Both lack a single time zero, so neither can be plotted. A staggered overdose is several large doses over hours; repeated supratherapeutic ingestion is over-dosing for pain over days."),
  ],
  traps=[
    ("“Plot the level and treat only if it is above the line”", "The nomogram is invalid for repeated ingestion; treat on dose, level >20 or raised ALT."),
    ("“A low level means low risk”", "The drug has already been metabolised; ALT tells you about injury."),
  ],
  decode=[
    ("Teen taking an analgesic 4-hourly, ALT >2000: drug screen positive for [Marrow]", "Paracetamol — repeated supratherapeutic ingestion."),
    ("Repeated ingestion, level 25 µg/mL, ALT normal [pattern]", "Treat — a level above 20 is an indication."),
  ],
  punch="With repeated dosing there is no time zero to plot, the level understates the danger, and the patient comes late — so treatment is triggered by the dose, any meaningful level, or a rising ALT.",
)

L['APAP-05'] = dict(
  sub="Toxicology → Stages & Nomogram → Clinical stages",
  intro="Paracetamol poisoning unfolds over days, and the time course follows the mechanism. In the first day NAPQI is depleting glutathione but cells have not yet died, so the patient looks almost well. Necrosis declares itself on days 2 to 4, and those who survive the peak regenerate their liver.",
  parts=[
    ('a', "**Stage I, 0.5–24 h: nausea, vomiting, pallor, sweating; laboratory tests usually normal.** Injury is under way inside the hepatocyte, but transaminases have not yet leaked — which is why a level is sent in every overdose (TOX-02)."),
    ('b', "**Stage II, 24–72 h: symptoms settle; right upper quadrant pain; transaminases rise; oliguria.** Hepatocytes are dying, so ALT and AST rise and the swollen liver is tender. Oliguria is the first sign of the renal tubular injury paracetamol can cause independently of the liver."),
    ('c', "**Stage III, 72–96 h: peak injury — AST/ALT above 10,000, coagulopathy, hypoglycaemia, encephalopathy, lactic acidosis, AKI.** The failing liver cannot make clotting factors (INR rises), release glucose (hypoglycaemia is common and must be checked often), clear ammonia (encephalopathy) or clear lactate (lactic acidosis). Death is from cerebral oedema, dysrhythmias with multi-organ failure, haemorrhage or sepsis. The stage is set by the picture, not the clock: in severe poisoning jaundice, INR 3 and AKI at 36 h already mean fulminant failure, with these same killers."),
    ('d', "**Stage IV, beyond 5 days: recovery, usually complete by day 7.** The liver regenerates from surviving cells and survivors usually recover without chronic liver disease, though histological recovery can take up to 3 months."),
  ],
  table=dict(title="The four stages", head=["Stage", "Time", "What is happening", "Labs"], rows=[["I", "0.5–24 h", "glutathione depletion, no necrosis yet", "normal"], ["II", "24–72 h", "necrosis begins; patient feels better", "ALT/AST rising"], ["III", "72–96 h", "peak necrosis, liver failure", "ALT >10,000, INR ↑, glucose ↓, lactate ↑"], ["IV", ">5 days", "regeneration", "normalising"]]),
  mimic=[
    ("Stage I vs stage II vs fulminant failure", "Nausea and sweating with normal enzymes is stage I; right upper quadrant tenderness with rising enzymes is stage II; jaundice, high INR and AKI is liver failure, whatever the hour."),
  ],
  traps=[
    ("“At 36 hours with jaundice and INR 3, expect right upper quadrant tenderness (stage II)”", "That is already fulminant failure; the associated complication is cerebral oedema and dysrhythmias. Only 31% of the DocT GT cohort got this right."),
    ("“Hypoglycaemia is rare in paracetamol liver failure” / “older or alcoholic patients do better”", "Hypoglycaemia is common; age over 40 and chronic alcohol worsen prognosis. Lactic acidosis is the recognised complication."),
    ("“She feels better on day 2, so she can go home”", "Stage II is the deceptive one: symptoms settle while the liver worsens. Decide on ALT and INR."),
  ],
  decode=[
    ("36 h after overdose: jaundice, INR 3.0, creatinine 2.5 — associated complication [DocT GT]", "Cerebral oedema and dysrhythmias."),
    ("Paracetamol liver failure: which is true? [DocT]", "Lactic acidosis is a recognised complication."),
    ("RUQ pain, rising enzymes at 48 h [pattern]", "Stage II."),
  ],
  punch="The stages track the mechanism: silent glutathione depletion on day 1, necrosis the patient does not feel on day 2, liver failure by days 3–4 — or earlier if severe — and regeneration in survivors; so a well patient on day 2 is not a safe patient.",
)

L['APAP-06'] = dict(
  sub="Toxicology → Stages & Nomogram → Rumack–Matthew nomogram",
  intro="After a single overdose the paracetamol level falls steadily once absorption is complete. If the level at a known time is high, more drug is reaching CYP2E1 and the risk of injury is higher. The nomogram turns that into a line: plot one level against the hours since ingestion, and treat if the point lies above the line.",
  parts=[
    ('a', "**It plots serum paracetamol against time since a single acute ingestion.** It is the risk tool for paracetamol (acetaminophen) only, and works only when there is one known time zero."),
    ('b', "**Earliest valid level: 4 hours after ingestion.** Before 4 hours absorption may be incomplete, so the level is still rising and a low value can be falsely reassuring (APAP-01). A patient seen at 3 hours, even after a large dose, has the level taken at 4 hours: the result is back well inside the 8-hour window, so NAC can wait for it."),
    ('c', "**Original line: 200 µg/mL at 4 h. Treatment line, 25% lower: 150 at 4 h.** The 200 line was drawn from patients who developed hepatotoxicity; US practice lowered it by 25% to allow for errors in timing and assay. Under this line, a valid 4-hour level decides — not the dose: 130 is below and not treated, 170 is above and treated."),
    ('d', "**Revised UK line (2012): a single line from 100 at 4 h to 15 at 15 h, with no risk stratification.** The MHRA moved everyone to the 100 line because risk factors could not be judged reliably at the bedside (APAP-03); many more patients receive NAC."),
    ('e', "**Not usable: staggered or repeated ingestion, unknown time; with sustained-release, take 4- and 8-hour levels and treat if either is above the line.** Without a single time zero the point cannot be placed; sustained-release tablets may give a late or second peak."),
  ],
  table=dict(title="Three numbers at 4 hours", head=["Line", "Level at 4 h", "Used for"], rows=[["Original Rumack–Matthew", "**200 µg/mL**", "probable hepatotoxicity"], ["US treatment line", "**150 µg/mL**", "NAC above it (US, Canada, Australia–NZ)"], ["UK (MHRA 2012)", "**100 mg/L**", "NAC above it for everyone"]]),
  mimic=[
    ("µg/mL vs mg/L vs mg/dL", "µg/mL and mg/L are the same number (150 µg/mL = 150 mg/L); mg/dL would be 100 times larger, so a stem printing “130 mg/dL” means 130 µg/mL. In µmol/L multiply by about 6.6 (150 line ≈ 990 µmol/L)."),
  ],
  traps=[
    ("“100 tablets 3 hours ago: give NAC now” or “give charcoal 50 g”", "Measure the 4-hour level in an hour — it will be back before 8 hours. Charcoal at 3 hours is outside the usual 1-hour window (UK; up to 2 h for large doses). DocT key; only 32% got it. Note the card conflict: APAP-08 allows charcoal to 4 hours, and Australia–NZ would give it for >30 g."),
    ("“Both took 15 g, so both get NAC”", "DocT keys the US 150 line: 4-hour levels 130 (no NAC) and 170 (NAC). The stem’s “mg/dL” should read µg/mL; under the UK 100 line both would be treated, and many centres would treat 15 g on dose alone. Only 42% chose the key."),
    ("“The treatment line is 200 at 4 hours”", "200 is the original line; the US treatment line is 150 and the UK line 100."),
  ],
  decode=[
    ("Two patients, 15 g each, 4-hour levels 130 and 170: treatment [DocT]", "Treat only the one above 150 (US line) — key; UK line would treat both."),
    ("17-year-old, 100 tablets 3 hours ago: next step [DocT]", "Measure the paracetamol level in one hour (at 4 h)."),
    ("Rumack–Matthew nomogram is used for which drug? [DocT GT]", "Acetaminophen (paracetamol)."),
  ],
  punch="The nomogram reads one level against one time, so it needs a single ingestion at a known time and a level at 4 hours or later — then the only question is which line the question names: 200, 150 or 100.",
)

L['APAP-07'] = dict(
  sub="Toxicology → Stages & Nomogram → Paracetamol–protein adducts",
  intro="Some patients arrive in liver failure days after an overdose they do not mention. By then the paracetamol has been cleared, so the level is undetectable. But when NAPQI binds liver proteins and the cells die, the bound fragments leak into the blood and persist for days.",
  parts=[
    ('a', "**They establish paracetamol as the cause of liver injury when the level is already undetectable.** Adducts form only when NAPQI binds protein cysteine groups (APAP-02), so they are specific, and they outlast the parent drug in blood."),
    ('b', "**Above 1 nmol/mL (with ALT above 1000), measured by HPLC.** A high adduct level with severe hepatotoxicity indicates paracetamol caused the injury; therapeutic dosing gives only low levels."),
    ('c', "**AcetaSTAT: a competitive immunoassay giving a positive or negative result only.** A rapid bedside strip test where HPLC is not available; it does not give a number."),
  ],
  mimic=[
    ("Paracetamol level vs adducts", "The level measures drug still in the blood and guides NAC early; adducts measure injury already done and identify the cause late."),
  ],
  traps=[
    ("“An undetectable level excludes paracetamol as the cause of liver failure”", "The drug is cleared within a day; adducts persist and can prove the cause."),
  ],
  decode=[
    ("Acute liver failure, denies overdose, paracetamol undetectable: confirmatory test [pattern]", "Paracetamol–protein adducts."),
  ],
  punch="When the drug has gone but the liver has failed, adducts are the fingerprint NAPQI left on the dead cells — proof of cause, not a guide to NAC dosing.",
)

L['APAP-08'] = dict(
  sub="Toxicology → N-acetylcysteine → Mechanism and timing",
  intro="The liver cannot take up glutathione given from outside, but it can make its own from cysteine. N-acetylcysteine delivers that cysteine, so it refills the store that NAPQI is draining. Its effect is greatest before glutathione runs out — but it still helps after that.",
  parts=[
    ('a', "**Replenishes glutathione; enhances sulfation; antioxidant and anti-inflammatory.** NAC is deacetylated to cysteine, the rate-limiting building block of glutathione, so NAPQI is captured before it reaches proteins. Once injury has started, its antioxidant action and improved microcirculation limit further damage — the reason it helps even in liver failure."),
    ('b', "**Within 8 hours of ingestion: near-complete protection.** In the first 8 hours glutathione has not yet fallen to the point at which NAPQI binds proteins (APAP-02). After that each hour of delay allows more necrosis — so a patient already beyond 8 hours after a toxic dose gets NAC at once, before the level is back."),
    ('c', "**Activated charcoal 1 g/kg (maximum 50 g) within 4 hours of a single ingestion; not with altered sensorium unless the airway is protected.** The usual window is 1 hour (TOX-09; UK up to 2 hours for large doses); Australia–NZ extends it to 4 hours only for very large (>30 g) or modified-release ingestions."),
  ],
  mimic=[
    ("NAC before vs after 8 hours", "Before 8 hours it prevents injury by refilling glutathione; after 8 hours it limits injury that has begun, so it is started immediately."),
  ],
  traps=[
    ("“Pinpoint pupils after codeine + 30 g paracetamol at 12 h: naloxone first”", "With BP held and no respiratory depression described, the time-critical treatment is NAC — already past 8 hours after a massive dose. Naloxone is for depressed breathing or consciousness (and precipitates withdrawal in an IV drug user); flumazenil has no role. Only 45% chose NAC."),
    ("“After 8 hours NAC is useless”", "It is still given late and in established liver failure; it improves outcome."),
    ("“NAC works by binding paracetamol”", "It replenishes glutathione, which binds NAPQI."),
  ],
  decode=[
    ("12 h after 480 mg codeine + 30 g paracetamol, BP 100/60, pinpoint pupils: most appropriate [DocT]", "Start N-acetylcysteine."),
    ("Main mechanism of NAC [pattern]", "Replenishes glutathione."),
  ],
  punch="NAC refills the glutathione that NAPQI drains: given within 8 hours it prevents injury almost completely, and given later it still limits the damage — so a late presenter gets it at once, ahead of the level and ahead of the distractions.",
)

L['APAP-09'] = dict(
  sub="Toxicology → N-acetylcysteine → Regimens",
  intro="NAC can be given intravenously over about a day or by mouth over three days. Both aim to keep glutathione ahead of NAPQI until the paracetamol has been cleared; they differ in route, length and side effects.",
  parts=[
    ('a', "**IV 21-hour protocol: bag 1 150 mg/kg in 200 mL 5% dextrose over 60 min; bag 2 50 mg/kg in 500 mL over 4 h; bag 3 100 mg/kg in 1000 mL over 16 h — 300 mg/kg in total.** The large first dose refills glutathione quickly while NAPQI production peaks; the later bags (12.5 then 6.25 mg/kg/h) keep it topped up while the drug clears."),
    ('b', "**Oral protocol: 140 mg/kg, then 70 mg/kg every 4 h for 17 doses (72 hours).** Oral NAC goes straight to the liver through the portal vein, but the taste and vomiting make doses hard to keep down."),
    ('c', "**IV is chosen for vomiting, no oral route, pregnancy and liver failure.** In all of these the oral dose may not be absorbed or tolerated, and reliable delivery matters most."),
    ('d', "**Main adverse effect of IV: an anaphylactoid reaction — rate-related, not IgE — so slow or pause, give an antihistamine, then restart.** NAC releases histamine directly, mostly during the concentrated first bag. No antibody is involved, so it is not a contraindication."),
  ],
  table=dict(title="a — The IV 21-hour protocol", head=["Bag", "Dose", "In", "Over"], rows=[["1", "**150 mg/kg**", "200 mL 5% dextrose", "**60 min**"], ["2", "**50 mg/kg**", "500 mL", "**4 h**"], ["3", "**100 mg/kg**", "1000 mL", "**16 h** (6.25 mg/kg/h)"], ["Total", "**300 mg/kg**", "", "21 h"]]),
  mimic=[],
  traps=[
    ("“A rash on bag 1 means NAC must be stopped for good”", "It is anaphylactoid: pause, antihistamine, restart."),
    ("“The oral course lasts 21 hours”", "Oral is 72 hours (loading dose plus 17 doses); IV is 21 hours."),
  ],
  decode=[
    ("Flushing and wheeze 30 minutes into IV NAC [pattern]", "Anaphylactoid reaction — pause, antihistamine, restart."),
    ("Total IV NAC dose and duration [pattern]", "300 mg/kg over 21 hours."),
  ],
  punch="Both regimens refill glutathione — IV front-loads it over 21 hours, oral spreads it over 72 — and the IV reaction is anaphylactoid, so it means slowing down, not stopping.",
  extra=[dict(q="Newer IV regimens with fewer reactions?", a="**SNAP**: 100 mg/kg over 2 h, then 200 mg/kg over 10 h; **two-bag**: 200 mg/kg over 4 h, then 100 mg/kg over 16 h. Both give 300 mg/kg without the concentrated first bag, so fewer reactions.")],
)

L['APAP-10'] = dict(
  sub="Toxicology → N-acetylcysteine → When to stop",
  intro="The 21-hour protocol is a fixed course, but the patient may not be finished when the bags are. NAC is needed for as long as paracetamol is still being turned into NAPQI or the liver is still being injured. So the decision to stop rests on blood tests — liver function tests among them — rather than the clock.",
  parts=[
    ('a', "**Stop when paracetamol is undetectable, ALT is falling, and INR is below 2.** No drug means no more NAPQI; a falling ALT means necrosis has stopped; an INR under 2 means synthetic function is preserved. This is why LFTs and INR are taken at presentation and again before NAC ends in every paracetamol overdose."),
    ('b', "**If not met at 21 hours, continue at 6.25 mg/kg/h — the third-bag rate — and repeat the tests 12-hourly.** Continuing at that rate maintains protection without a new loading dose."),
    ('c', "**In established liver failure, continue until transplant or resolution.** NAC still improves survival once the liver is failing (APAP-08)."),
  ],
  mimic=[
    ("Falling ALT: recovery vs burnout", "A falling ALT with a falling INR means recovery; a falling ALT with a rising INR means too few hepatocytes are left (APAP-11)."),
  ],
  traps=[
    ("“NAC should routinely be given to anyone presenting within 12 hours”", "Within 8 hours NAC is guided by the 4-hour level on the nomogram (APAP-06), not given routinely; the statement that holds is that LFTs must be monitored. Only 57% chose it."),
    ("“Over the age of 6, she is unlikely to develop significant toxicity”", "Only young children are relatively protected (sulfation, APAP-03); a 19-year-old is an adult."),
    ("“The 21-hour course is complete, so stop NAC”", "Stop only if the level is undetectable, ALT falling and INR below 2."),
  ],
  decode=[
    ("19-year-old with paracetamol overdose: which statement is correct? [DocT]", "Liver function tests should be monitored."),
    ("End of 21 h: level undetectable, ALT rising, INR 2.4 [pattern]", "Continue NAC at 6.25 mg/kg/h, repeat tests in 12 hours."),
  ],
  punch="NAC is stopped by the blood tests, not the clock: when no drug is left, the ALT is falling and the INR is under 2 — otherwise it continues at the third-bag rate.",
)

L['APAP-11'] = dict(
  sub="Toxicology → Transplant & Sweep → King’s College criteria",
  intro="Most patients with paracetamol liver failure recover with NAC and intensive care, but some will die without a transplant. King’s College criteria pick out that group using markers of how much liver function is left. Transaminases are not among them: they measure how many cells died, not how many survive.",
  parts=[
    ('a', "**Arterial pH below 7.30 after fluid resuscitation; OR all three of creatinine above 3.4 mg/dL, grade 3 or 4 encephalopathy and INR above 6.5 (PT above 100 s).** Persistent acidosis means the liver cannot clear lactate and other acids; pH alone is enough. INR measures synthetic function, encephalopathy detoxification, and creatinine the renal injury. A patient who meets them needs emergency transplant evaluation, not more enzymes or observation."),
    ('b', "**Specificity 90%, sensitivity only 60%: it misses patients who will die.** When the criteria are met, death without transplant is very likely; failing to meet them is not reassurance."),
    ('c', "**Lactate modification: above 3.5 after 1 hour of fluid resuscitation, or above 3.0 after adequate fluids.** Units are mmol/L; the necrotic liver both fails to clear lactate and produces it, so lactic acidosis is a recognised complication and adding lactate identifies non-survivors earlier."),
  ],
  table=dict(title="King’s College criteria — paracetamol", head=["Route", "Criterion"], rows=[["Alone", "**pH <7.30** after fluids (or lactate >3.0 mmol/L after adequate fluids)"], ["All three", "**INR >6.5**, **creatinine >3.4 mg/dL** (300 µmol/L), **grade 3–4 encephalopathy**"]]),
  mimic=[
    ("Paracetamol vs non-paracetamol criteria", "Non-paracetamol King’s use INR >6.5 alone, or three of five (age <10 or >40, aetiology, jaundice-to-encephalopathy >7 days, INR >3.5, bilirubin >17.5 mg/dL). Factor V <20–30% with encephalopathy is the Clichy criterion. Age, bilirubin and factor V are distractors in a paracetamol question."),
  ],
  traps=[
    ("“ALT (or the paracetamol level) at 30 hours best predicts outcome”", "ALT measures injury, not outcome; among ALT, bilirubin, creatinine and level, creatinine is the King’s marker. DocT keys ALT — disputed; the card is right. 58% chose the key."),
    ("“Not meeting King’s criteria means the patient will survive”", "Sensitivity is only about 60%."),
    ("“A falling ALT means recovery”", "With a rising INR it means too little liver is left."),
  ],
  decode=[
    ("pH 7.25, creatinine 3.8, INR 7.2, grade III: which finding alone predicts poor prognosis? [DocT GT]", "Arterial pH <7.3."),
    ("pH 7.25, INR 7.0, creatinine 3.8, grade IV: next best step [DocT GT]", "Emergency liver transplant evaluation."),
    ("30 h after 25 g: test most helpful for outcome [DocT]", "Key ALT (disputed); by King’s, creatinine."),
  ],
  punch="King’s College criteria measure what the liver can no longer do — clear acid, make clotting factors, protect the brain and the kidneys — so they predict death well when met, but miss many who will still die.",
)

L['APAP-12'] = dict(
  sub="Toxicology → Transplant & Sweep → Adjuncts in massive overdose",
  intro="In a massive overdose NAC alone may not keep up, and enormous levels can poison mitochondria directly, giving coma and lactic acidosis within hours. Adjuncts either stop NAPQI being made or remove the drug — always on top of NAC, never in place of it.",
  parts=[
    ('a', "**Fomepizole: a CYP2E1 inhibitor, an emerging adjunct to NAC (case reports).** Blocking CYP2E1 cuts NAPQI formation at its source; human evidence is limited to case reports."),
    ('b', "**Haemodialysis clears paracetamol; it is used in massive ingestion with severe lactic acidosis, and is never a substitute for NAC.** Paracetamol is small, poorly protein-bound and has a modest volume of distribution, so dialysis removes it. EXTRIP (2014) recommends it for a level >1000 mg/L without NAC, or mitochondrial dysfunction (coma, acidosis, raised lactate) with a level >700 mg/L without NAC or >900 mg/L with NAC. NAC continues at a higher rate, because dialysis removes it too."),
    ('c', "**Cimetidine worked in animals but gave no benefit in humans.** A CYP inhibitor in theory; no clinical benefit, so no role."),
  ],
  mimic=[
    ("Early vs late acidosis in paracetamol poisoning", "Early (hours), with coma and a massive level, is mitochondrial toxicity — consider dialysis. Late (days 3–4) is liver failure — a King’s criterion (APAP-11)."),
  ],
  traps=[
    ("“Dialysis can replace NAC in massive overdose”", "It is always added to NAC, never instead of it."),
  ],
  decode=[
    ("Massive ingestion, comatose, severe lactic acidosis, level 950 mg/L on NAC [pattern]", "Haemodialysis plus NAC at an increased rate."),
  ],
  punch="In a massive overdose the adjuncts attack the same problem from two ends — fomepizole stops NAPQI being made, dialysis removes the drug — but NAC stays the treatment throughout.",
)

L['APAP-13'] = dict(
  sub="Toxicology → Transplant & Sweep → True or false",
  intro="This card tests the deck’s key distinctions. Each statement either holds or turns on one detail from an earlier card; the reason is the mechanism you met there.",
  parts=[
    ('a', "**False — the toxic metabolite is formed by CYP2E1 oxidation.** Glucuronidation makes inert conjugates; NAPQI comes from the small oxidised fraction (APAP-02)."),
    ('b', "**False — injury is centrilobular.** CYP2E1 is concentrated in zone 3, so NAPQI is made, and cells die, around the central vein (APAP-02)."),
    ('c', "**False — the level must be taken at 4 hours or later.** Before 4 hours absorption may be incomplete and the level still rising (APAP-06)."),
    ('d', "**False — acute alcohol is protective; chronic alcohol harms.** Acute ethanol competes for CYP2E1; chronic use induces it and lowers glutathione (APAP-03)."),
    ('e', "**True — the US treatment line starts at 150 at 4 hours,** 25% below the original 200 line as a safety margin (APAP-06)."),
    ('f', "**True — the first IV NAC bag is 150 mg/kg,** to refill glutathione quickly (APAP-09)."),
    ('g', "**True — NAC is stopped when INR is below 2 and ALT falling, with an undetectable level.** All three are needed: no drug left, necrosis over, function preserved (APAP-10)."),
    ('h', "**True — pH below 7.30 after fluids meets King’s criteria** on its own (APAP-11)."),
  ],
  mimic=[],
  traps=[
    ("“Alcohol increases toxicity”", "Only chronic alcohol; acute co-ingestion protects."),
    ("“INR <2 and falling ALT are enough to stop NAC”", "The level must also be undetectable."),
  ],
  decode=[
    ("Chronic alcoholic, repeated supratherapeutic use: why higher risk? [DocT GT]", "Increased CYP2E1 activity and low glutathione — not renal clearance or absorption."),
    ("True/false on metabolism or the nomogram [pattern]", "Ask which pathway makes NAPQI (CYP2E1) and which time and line apply (≥4 h; 200, 150, 100)."),
  ],
  punch="Every statement here turns on a mechanism from earlier in the deck — CYP2E1 making NAPQI in zone 3, absorption complete by 4 hours, and stopping or listing decided by what the liver can still do.",
)

L['APAP-14'] = dict(
  sub="Toxicology → Transplant & Sweep → Indications for NAC",
  intro="NAC is safe and the cost of missing paracetamol toxicity is a dead liver, so the indications are deliberately broad. They follow one logic: treat whenever the nomogram says the dose is toxic, whenever it cannot be used but toxicity is possible, and whenever the liver is already injured.",
  parts=[
    ('a', "**Single ingestion with a level at 4 hours or later above the treatment line.** A known time and a valid level place the patient in the risk zone (APAP-06)."),
    ('b', "**More than 150 mg/kg (7.5 g) with no level available within 8 hours.** Protection is near-complete only if NAC starts within 8 hours (APAP-08), so waiting for a late result throws away the window — and a patient who arrives after 8 hours with a toxic dose gets NAC immediately. Stop if the level returns below the line."),
    ('c', "**Unknown dose or time with a level above 10 µg/mL.** Without a time the level cannot be plotted, so any measurable paracetamol means drug is still present to form NAPQI."),
    ('d', "**Any ingestion with evidence of liver injury.** A raised ALT shows NAPQI has already overwhelmed glutathione, whatever the level or history."),
    ('e', "**Presentation after 24 hours with liver injury.** The nomogram ends at 24 hours, but NAC still improves outcome in late presenters (APAP-08)."),
  ],
  table=dict(title="The logic of the indications", head=["Situation", "Why treat"], rows=[["Level above the line at ≥4 h", "nomogram says toxic"], ["Level not back by 8 h, >150 mg/kg", "protect the 8-hour window"], ["Unknown time, level >10", "nomogram unusable, drug present"], ["Liver injury, any ingestion", "injury already under way"], ["After 24 h with injury", "late NAC still helps"]]),
  mimic=[
    ("Acute single vs repeated supratherapeutic ingestion", "Acute: these indications and the nomogram. Repeated: dose, level >20 or raised ALT (APAP-04)."),
  ],
  traps=[
    ("“Mixed overdose with a striking other finding (opioid pupils, long QTc after ecstasy): treat that first”", "Suspect hidden paracetamol in any analgesic overdose with vomiting; when the time and dose make it toxic, NAC is the answer the question wants."),
    ("“No paracetamol in the history, so no level”", "Send a level in every deliberate overdose: co-ingestion is common and stage I looks harmless."),
    ("“NAC routinely for everyone presenting within 12 hours”", "Within 8 hours, wait for the 4-hour level and use the nomogram; LFTs are monitored in all (APAP-10)."),
  ],
  decode=[
    ("Ecstasy, peptic ulcer, analgesic use, vomiting, QTc 503: next step [Marrow]", "N-acetylcysteine — hidden paracetamol."),
    ("12 h after codeine + 30 g paracetamol, pinpoint pupils [DocT]", "Start NAC."),
    ("19-year-old overdose: correct statement [DocT]", "LFTs should be monitored — not routine NAC within 12 h."),
  ],
  punch="NAC is given whenever toxicity is shown, cannot be ruled out in time, or has already begun — because the drug is safe and the window is short.",
)

FLAGS = {}
FLAGS['APAP-01'] = "WATCH says pesticides ‘dominate’ — true of poisoning in India, but the commonest causes of acute liver failure in India are viral hepatitis (HEV, HBV) and anti-tubercular drug injury, not pesticides. Consider rewording."
FLAGS['APAP-03'] = "Card groups anticonvulsants under ‘CYP2E1 inducers’; only isoniazid (and alcohol) act mainly on CYP2E1 — phenytoin, carbamazepine, phenobarbital and rifampicin induce other CYP isoforms. Evidence for inducers raising risk is weak (UK dropped the high-risk line in 2012). Explanation says ‘CYP inducers’."
FLAGS['APAP-04'] = "Repeated-ingestion dose thresholds vary by guideline and the card’s 7.5 g / 4 g in 24 h matches none exactly: US out-of-hospital consensus (Dart 2006) and Australia–NZ use ≥10 g or 200 mg/kg in 24 h, or ≥6 g or 150 mg/kg per 24 h for ≥48 h; Australia–NZ adds 4 g or 100 mg/kg in 24 h with risk factors. The level >20 µg/mL and ALT >50 triggers agree (Australia–NZ). Explanation states the range."
FLAGS['APAP-05'] = "Stage IV timing: Goldfrank places recovery from about day 4–5 to 2 weeks, with histological recovery up to 3 months; ‘usually complete by day 7’ is optimistic. Explanation adds this."
FLAGS['APAP-06'] = "DocT QBank ‘100 tablets 3 h ago’ keys ‘measure level in 1 h’, which assumes the UK 1-hour charcoal window; APAP-08 says charcoal within 4 h. DocT QBank ‘suicide pact’ prints levels in mg/dL (should be µg/mL) and keys the US 150 line. Both noted in traps."
FLAGS['APAP-08'] = "Charcoal ‘within 4 hours’ is broader than most guidelines: the usual window is 1 hour; Australia–NZ uses 2 hours for a toxic immediate-release dose and up to 4 hours only for >30 g or modified-release ingestions. Explanation says this. Conflicts with the DocT key on APAP-06."
FLAGS['APAP-11'] = "Lactate modification (Bernal, Lancet 2002): >3.5 mmol/L about 4 h after admission (early) or >3.0 mmol/L at about 12 h after full fluid resuscitation. The card’s ‘after 1 hour of fluid resuscitation’ does not match the original timing. DocT QBank ‘30 h after 25 g’ keys ALT as the outcome test — disputed; creatinine is the King’s marker."
FLAGS['APAP-14'] = "WATCH ‘IV NAC for 12 hours, then repeat the tests’ for repeated ingestion is not universal: the Australian (RCH) guideline, for example, gives the full regimen and rechecks paracetamol and ALT about 2 hours before it ends. Treat as source-specific."
