# TOX02 — Paracetamol toxicity. Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Same fields as tox01_learn.py (sub, intro, parts, table, mimic, traps, decode, punch, extra).
L = {}

L['APAP-01'] = dict(
  sub="Toxicology → Dose & Mechanism → Dose thresholds",
  intro="Paracetamol is safe at therapeutic doses because the liver has more than enough capacity to make it harmless. Toxicity is a matter of dose per kilogram: once the ingested amount outruns that capacity, a toxic metabolite starts to accumulate. The thresholds below mark where the risk begins, where it becomes near-certain, and how severe injury is defined.",
  parts=[
    ('a', "**Maximum therapeutic dose 4 g/day in adults; 75 mg/kg/day in children.** At these doses glucuronidation and sulfation handle almost all of the drug, and the small oxidised fraction is mopped up by glutathione without depleting it."),
    ('b', "**Toxic single dose: >150 mg/kg, or 7.5–10 g in an adult.** Above this the conjugation pathways saturate, so a larger share of the dose is diverted to oxidation, and the resulting NAPQI begins to use up glutathione faster than the liver can make it (APAP-02)."),
    ('c', "**Liver failure almost certain above 350 mg/kg (untreated).** At this dose glutathione is exhausted early and NAPQI binds hepatocyte proteins in large amounts; without N-acetylcysteine severe hepatotoxicity is the rule rather than the exception."),
    ('d', "**Severe hepatotoxicity: peak AST or ALT >1000 U/L.** Transaminases leak from necrotic hepatocytes, so a peak above 1000 marks substantial necrosis. It is the standard end-point used in the studies behind the nomogram and NAC timing."),
    ('e', "**Peak level at 1.5–2 h normally; within 4 hours in overdose — later with opioids, anticholinergics or food.** Paracetamol is absorbed quickly from the small intestine, so a level taken 4 hours after ingestion has usually captured the peak. Anything that slows gastric emptying (opioid or anticholinergic co-ingestion, food, large tablet masses) delays the peak, which is why a 4-hour level is the earliest valid one (APAP-06)."),
  ],
  table=dict(title="Dose and what it means", head=["Dose", "Meaning"], rows=[["≤4 g/day (adult), 75 mg/kg/day (child)", "therapeutic"], ["**>150 mg/kg** or 7.5–10 g", "potentially toxic — assess and level"], ["**>350 mg/kg**", "severe hepatotoxicity near-certain untreated"], ["Peak AST/ALT **>1000 U/L**", "definition of severe hepatotoxicity"]]),
  mimic=[
    ("Hepatotoxicity vs hepatic failure", "Hepatotoxicity is a laboratory definition (AST/ALT >1000); hepatic failure adds coagulopathy and encephalopathy. Most patients with hepatotoxicity recover."),
  ],
  traps=[
    ("“A 2-hour level can show the peak”", "Absorption may not be complete before 4 hours, and later still with opioids or anticholinergics."),
    ("“Toxicity is set by the number of tablets”", "It is set by mg/kg — 10 g is far more dangerous in a 45 kg woman than in a 90 kg man."),
    ("“ALT 600 meets severe hepatotoxicity”", "The definition is a peak above 1000 U/L."),
  ],
  decode=[
    ("Minimum potentially toxic acute dose", ">150 mg/kg (7.5–10 g in an adult)."),
    ("Ingestion of 400 mg/kg, untreated", "Severe hepatotoxicity is almost certain."),
    ("How is severe hepatotoxicity defined?", "Peak AST or ALT above 1000 U/L."),
  ],
  punch="Paracetamol is dosed by the liver’s capacity: above 150 mg/kg the safe pathways saturate and the toxic metabolite starts to win, and above 350 mg/kg it almost always wins unless N-acetylcysteine is given.",
)

L['APAP-02'] = dict(
  sub="Toxicology → Dose & Mechanism → Metabolism and injury",
  intro="Paracetamol itself does not damage the liver; one of its metabolites does. Normally that metabolite is made in small amounts and neutralised at once by glutathione. Injury happens when the dose is large enough to use up glutathione, and it happens where the metabolite is made — in the hepatocytes around the central vein.",
  parts=[
    ('a', "**90% glucuronidation and sulfation (non-toxic); 1–2% unchanged in urine; 5–9% oxidised (your notes’ text says 5–7%).** Conjugation attaches a water-soluble group so the drug can be excreted; the products are inert. Only the oxidised fraction is dangerous, and in overdose this fraction grows because the conjugating pathways saturate."),
    ('b', "**NAPQI (N-acetyl-p-benzoquinone imine), made by CYP2E1.** NAPQI is a highly reactive electrophile: it attacks the sulphydryl groups of cell proteins. CYP2E1 is the main enzyme, with contributions from CYP3A4 and CYP1A2."),
    ('c', "**Conjugation with glutathione to cysteine and mercapturic acid conjugates.** Glutathione donates its sulphydryl group to NAPQI, making a harmless conjugate that is processed and excreted in urine. Each molecule of NAPQI uses up glutathione, so the store falls as the dose rises."),
    ('d', "**Injury begins when glutathione stores fall by 70–80%: NAPQI binds cell proteins (adducts), mitochondria fail, and the cell necroses.** While glutathione is available, NAPQI is captured before it reaches proteins. Once stores are below about a quarter of normal, NAPQI binds mitochondrial proteins, causing oxidative stress, loss of ATP and necrosis. The protein–paracetamol adducts that leak out are the basis of the adduct test (APAP-07)."),
    ('e', "**Centrilobular (zone 3), where CYP450 is concentrated.** NAPQI is made where CYP2E1 is most abundant, around the central vein; zone 3 also receives the least oxygenated blood. So the necrosis is centrilobular, and periportal (zone 1) cells are relatively spared."),
  ],
  table=dict(title="Where the dose goes", head=["Route", "Share", "Product"], rows=[["Glucuronidation + sulfation", "**~90%**", "inert conjugates"], ["Unchanged in urine", "1–2%", "—"], ["CYP2E1 oxidation", "**5–9%**", "**NAPQI** → glutathione conjugate"]]),
  mimic=[
    ("Paracetamol vs ischaemic hepatitis", "Ischaemic hepatitis is also centrilobular (zone 3, least oxygen). Paracetamol injury follows an ingestion with a timed rise in transaminases; ischaemic injury follows shock."),
  ],
  traps=[
    ("“The toxic metabolite is made by glucuronidation”", "Glucuronidation makes inert conjugates; NAPQI comes from CYP2E1 oxidation."),
    ("“Paracetamol injury is periportal”", "It is centrilobular, zone 3 — where CYP2E1 is concentrated."),
    ("“NAPQI injures the liver from the first tablet”", "It is harmless while glutathione lasts; injury starts after a 70–80% fall."),
  ],
  decode=[
    ("Enzyme forming the toxic metabolite", "CYP2E1 → NAPQI."),
    ("Zone of necrosis in paracetamol poisoning", "Zone 3, centrilobular."),
    ("What detoxifies NAPQI?", "Glutathione."),
  ],
  punch="Paracetamol is poisonous only through NAPQI, which glutathione neutralises until about three-quarters of the store is gone — and because CYP2E1 sits around the central vein, that is where the liver dies.",
)

L['APAP-03'] = dict(
  sub="Toxicology → Dose & Mechanism → Risk factors",
  intro="Two things decide how much harm a given dose does: how fast NAPQI is made, and how much glutathione is there to meet it. Anything that speeds CYP oxidation or lowers glutathione raises the risk; anything that slows oxidation or boosts conjugation lowers it. Every item on this list fits one of those two levers.",
  parts=[
    ('a', "**Raises: chronic alcohol.** Long-term drinking induces CYP2E1, so more NAPQI is made from the same dose, and the poor nutrition that goes with it lowers glutathione. Both levers move against the patient."),
    ('b', "**Raises: CYP inducers — anticonvulsants, antitubercular drugs — and tobacco.** Enzyme inducers increase oxidative metabolism. Isoniazid acts on CYP2E1; phenytoin, carbamazepine, phenobarbital and rifampicin induce other CYP isoforms that can also make NAPQI. Smoking induces CYP1A2 and has been linked to worse outcomes after overdose."),
    ('c', "**Raises: fasting and malnutrition.** Glutathione is built from amino acids, chiefly cysteine; a starved or malnourished patient has smaller stores and less capacity for glucuronidation, so NAPQI overwhelms the defence sooner."),
    ('d', "**Raises: age over 40, Gilbert syndrome, repeated supratherapeutic dosing.** Older patients have less hepatic reserve and worse outcomes. Gilbert syndrome reduces UGT1A1 activity, so in theory less drug is glucuronidated and more is left for oxidation; the clinical evidence for this is weak. Repeated dosing wears glutathione down over days (APAP-04)."),
    ('e', "**Lowers: childhood — more glutathione, more conjugation.** Young children clear paracetamol mainly by sulfation, which they do efficiently, and they make glutathione readily, so a smaller fraction becomes NAPQI and it is neutralised faster."),
    ('f', "**Lowers: acute alcohol co-ingestion — it competes for CYP2E1.** Ethanol drunk at the same time occupies CYP2E1, so less paracetamol is oxidised to NAPQI while the alcohol is present. The same enzyme, once induced by chronic drinking, has the opposite effect."),
  ],
  table=dict(title="The two levers", head=["Factor", "Lever", "Effect"], rows=[["Chronic alcohol, inducers, tobacco", "more NAPQI made", "↑ risk"], ["Fasting, malnutrition, chronic alcohol", "less glutathione", "↑ risk"], ["Gilbert syndrome", "less glucuronidation", "↑ risk"], ["Acute alcohol", "CYP2E1 occupied", "↓ risk"], ["Childhood", "more sulfation, more glutathione", "↓ risk"]]),
  mimic=[
    ("Acute vs chronic alcohol", "Acute alcohol competes for CYP2E1 and protects; chronic alcohol induces CYP2E1 and depletes glutathione, and harms."),
  ],
  traps=[
    ("“Alcohol always increases paracetamol toxicity”", "Acute co-ingestion is protective; only chronic use increases risk."),
    ("“Children are at higher risk because they are smaller”", "Dosed per kg, children are at lower risk: more sulfation and glutathione."),
    ("“Risk factors mean a lower nomogram line in the UK”", "The UK abolished its separate high-risk line in 2012; everyone is treated above the single 100 line (APAP-06)."),
  ],
  decode=[
    ("Chronic alcoholic, fasting, takes 6 g over a day", "High risk: induced CYP2E1 and low glutathione."),
    ("Paracetamol taken with a bottle of whisky at a party", "Acute alcohol — protective while it lasts."),
    ("Why do toddlers tolerate accidental ingestions better?", "More sulfation and glutathione, less NAPQI."),
  ],
  punch="Every risk factor either makes more NAPQI or leaves less glutathione to meet it — which is why chronic alcohol harms and acute alcohol, competing for the same enzyme, protects.",
  extra=[dict(q="Children under ~10: main clearance route?", a="**Sulfation** (adults mainly glucuronidation), with more glutathione — so less NAPQI. The nomogram and NAC rules still apply.")],
)

L['APAP-04'] = dict(
  sub="Toxicology → Dose & Mechanism → Repeated supratherapeutic ingestion",
  intro="Not every paracetamol poisoning is a single deliberate overdose. A patient in pain — a toothache, a fever, a hangover — may take a little more than the maximum dose, several times a day, for several days. Each dose is small, but glutathione is never allowed to recover, and the patient does not see a doctor until the liver is already injured.",
  parts=[
    ('a', "**More dangerous: presents late with established injury, so severe hepatotoxicity and death are more frequent.** There is no dramatic event to bring the patient in, so the treatment window passes unnoticed. These patients are also often the ones with risk factors — fasting through illness, chronic alcohol — so glutathione is low before the excess even begins (APAP-03)."),
    ('b', "**The nomogram does not apply: levels do not correlate with toxicity.** The nomogram reads a level against the time since one ingestion. With many doses there is no single time zero, and much of the drug has already been metabolised, so a low level can coexist with severe injury."),
    ('c', "**NAC if more than 7.5 g in 24 h (4 g with risk factors), symptoms, a level above 20 µg/mL, or raised transaminases (>50) whatever the level.** Because the level cannot be plotted, the decision rests on the amount taken and on two simple markers: a level above 20 µg/mL means enough drug is still circulating to keep making NAPQI, and a raised ALT means injury has already begun. The exact dose thresholds differ between guidelines (Australia–NZ, for example, uses 10 g or 200 mg/kg in 24 h, 6 g or 150 mg/kg a day for 48 h or more, and 4 g or 100 mg/kg in 24 h with risk factors), but the level and ALT triggers are shared. Either one is a reason to start NAC (APAP-14 watch: 12 hours of IV NAC, then repeat the tests)."),
  ],
  mimic=[
    ("Repeated ingestion vs staggered overdose", "Both lack a single time zero, so neither can be plotted. A staggered overdose is several large doses over hours; repeated supratherapeutic ingestion is over-dosing for pain over days."),
  ],
  traps=[
    ("“Plot the level and treat only if it is above the line”", "The nomogram is invalid for repeated ingestion; treat on dose, level >20 or raised ALT."),
    ("“A low level means low risk”", "The drug has already been metabolised; ALT tells you about injury."),
  ],
  decode=[
    ("Toothache, 6–8 g/day for 3 days, ALT 400", "Repeated supratherapeutic ingestion — start NAC; the nomogram does not apply."),
    ("Repeated ingestion, level 25 µg/mL, ALT normal", "Treat — a level above 20 is an indication."),
  ],
  punch="With repeated dosing there is no time zero to plot, the level understates the danger, and the patient comes late — so treatment is triggered by the dose, any meaningful level, or a rising ALT.",
)

L['APAP-05'] = dict(
  sub="Toxicology → Stages & Nomogram → Clinical stages",
  intro="Paracetamol poisoning unfolds over days, and the time course follows the mechanism. In the first day NAPQI is depleting glutathione and binding proteins, but cells have not yet died, so the patient looks almost well. Necrosis declares itself on days 2 to 4, and those who survive the peak regenerate their liver.",
  parts=[
    ('a', "**Stage I, 0.5–24 h: nausea, vomiting, pallor, sweating; laboratory tests usually normal.** The symptoms are non-specific gastrointestinal upset. Injury is under way inside the hepatocyte, but transaminases have not yet leaked — which is exactly why a level is sent in every overdose (TOX-02)."),
    ('b', "**Stage II, 24–72 h: symptoms settle; right upper quadrant pain; transaminases rise; oliguria.** Hepatocytes are now dying, so ALT and AST rise and the swollen liver causes right upper quadrant pain. Oliguria is the first sign of the renal tubular injury that paracetamol can cause independently of the liver."),
    ('c', "**Stage III, 72–96 h: peak injury — AST/ALT above 10,000, coagulopathy, hypoglycaemia, encephalopathy, lactic acidosis, AKI.** The failing liver cannot make clotting factors (INR rises), cannot release glucose (hypoglycaemia), cannot clear ammonia (encephalopathy) or lactate (lactic acidosis). Death in this stage is from cerebral oedema, multi-organ failure, haemorrhage or sepsis."),
    ('d', "**Stage IV, beyond 5 days: recovery, usually complete by day 7.** The liver regenerates from surviving cells and survivors usually recover without chronic liver disease. Biochemical recovery is often under way by the end of the first week, but Goldfrank’s places stage IV from about day 4 to 2 weeks, and histological recovery can take up to 3 months; the AKI recovers over 1–4 weeks."),
  ],
  table=dict(title="The four stages", head=["Stage", "Time", "What is happening", "Labs"], rows=[["I", "0.5–24 h", "glutathione depletion, no necrosis yet", "normal"], ["II", "24–72 h", "necrosis begins; patient feels better", "ALT/AST rising"], ["III", "72–96 h", "peak necrosis, liver failure", "ALT >10,000, INR ↑, glucose ↓, lactate ↑"], ["IV", ">5 days", "regeneration", "normalising"]]),
  mimic=[
    ("Stage I vs stage II", "Nausea and sweating with normal enzymes is stage I; right upper quadrant pain with rising enzymes is stage II."),
  ],
  traps=[
    ("“She feels better on day 2, so she can go home”", "Stage II is the deceptive one: symptoms settle while the liver worsens. Decide on ALT and INR."),
    ("“Normal LFTs at 12 hours exclude poisoning”", "Stage I labs are normal; the level, not the LFTs, decides treatment."),
    ("“Survivors of paracetamol liver failure develop cirrhosis”", "Survivors usually regenerate fully; chronic liver disease is not the expected outcome."),
  ],
  decode=[
    ("RUQ pain, rising enzymes at 48 h", "Stage II."),
    ("Jaundice, INR 3 and AKI at 36 h", "Severe poisoning reaching stage III early — fulminant hepatic failure."),
    ("Leading causes of death in fulminant paracetamol failure", "Cerebral oedema and multi-organ failure."),
  ],
  punch="The stages track the mechanism: silent glutathione depletion on day 1, necrosis that the patient does not feel on day 2, liver failure by days 3–4, and regeneration in those who survive — so a well patient on day 2 is not a safe patient.",
  extra=[dict(q="Severe poisoning: can stage III come early?", a="**Yes** — jaundice, INR 3 and AKI at 36 h already mean fulminant hepatic failure; the killers are **cerebral oedema** and dysrhythmias with **multi-organ failure**.")],
)

L['APAP-06'] = dict(
  sub="Toxicology → Stages & Nomogram → Rumack–Matthew nomogram",
  intro="After a single overdose the paracetamol level falls steadily once absorption is complete. If the level at a known time is high, more drug is reaching CYP2E1 and the risk of injury is higher. The nomogram turns that into a line: plot one level against the hours since ingestion, and treat if the point lies above the line.",
  parts=[
    ('a', "**It plots serum paracetamol against time since a single acute ingestion.** The line is drawn on a log scale and falls by half every 4 hours — a deliberately long half-life (the drug’s own is 2–3 hours, longer in overdose), so the line stays conservative. It only works when there is one known time zero."),
    ('b', "**Earliest valid level: 4 hours after ingestion.** Before 4 hours absorption may not be complete, so the level is still rising and a low value can be falsely reassuring (APAP-01)."),
    ('c', "**Original line: 200 µg/mL at 4 h. Treatment line, 25% lower: 150 at 4 h.** Rumack and Matthew drew the 200 line from patients who developed hepatotoxicity. US practice lowered it by 25% to 150 to allow for errors in the timing and the assay — a deliberate safety margin."),
    ('d', "**Revised UK line (2012): a single line from 100 at 4 h to 15 at 15 h, with no risk stratification.** After a Commission on Human Medicines review in 2012, the UK regulator (MHRA) moved everyone to the 100 line and dropped the separate high-risk line, because risk factors could not be judged reliably at the bedside (APAP-03). The price is that many more patients receive NAC."),
    ('e', "**Not usable: staggered or repeated ingestion, unknown time; with sustained-release, take 4- and 8-hour levels and treat if either is above the line.** Without a single time zero the point cannot be placed. Sustained-release tablets may produce a late or second peak, so one level can understate the exposure."),
  ],
  table=dict(title="Three numbers at 4 hours", head=["Line", "Level at 4 h", "Used for"], rows=[["Original Rumack–Matthew", "**200 µg/mL**", "probable hepatotoxicity"], ["US treatment line", "**150 µg/mL**", "NAC above it (US, Canada, Australia–NZ)"], ["UK (MHRA 2012)", "**100 mg/L**", "NAC above it for everyone"]]),
  mimic=[
    ("µg/mL vs mg/L vs µmol/L", "µg/mL and mg/L are the same number (150 µg/mL = 150 mg/L). Laboratories reporting in µmol/L multiply by about 6.6, so the 150 line is about 990 µmol/L and the UK 100 line about 660 µmol/L."),
  ],
  traps=[
    ("“A 2-hour level above the line can be plotted”", "The nomogram starts at 4 hours."),
    ("“Plot a level after a staggered overdose”", "There is no single time zero; treat instead."),
    ("“The treatment line is 200 at 4 hours”", "200 is the original line; the US treatment line is 150 and the UK line 100."),
  ],
  decode=[
    ("“Treatment line” with no country named", "150 µg/mL at 4 h."),
    ("UK or MHRA named", "100 mg/L at 4 h, one line for all."),
    ("Level 120 at 4 h", "Below the 150 line, above the UK 100 line — the answer depends on which line the question names."),
  ],
  punch="The nomogram reads one level against one time, so it needs a single ingestion at a known time and a level at 4 hours or later — then the only question is which line the question names: 200, 150 or 100.",
  extra=[dict(q="More than 150 mg/kg taken, level will not be back before 8 hours: wait?", a="**No** — start NAC on the dose and stop it if the level returns below the line (APAP-14).")],
)

L['APAP-07'] = dict(
  sub="Toxicology → Stages & Nomogram → Paracetamol–protein adducts",
  intro="Some patients arrive in liver failure days after an overdose they do not mention. By then the paracetamol has been cleared, so the level is undetectable and cannot prove the cause. But the injury leaves a fingerprint: when NAPQI binds liver proteins and the cells die, the bound fragments leak into the blood and persist for days.",
  parts=[
    ('a', "**They establish paracetamol as the cause of liver injury when the level is already undetectable.** Adducts form only when NAPQI binds cysteine groups on proteins (APAP-02), so they are specific to paracetamol toxicity. Their half-life in blood is far longer than the drug’s, so they remain measurable after the parent drug is gone."),
    ('b', "**Above 1 nmol/mL (with ALT above 1000), measured by HPLC.** A high adduct level together with severe hepatotoxicity indicates that paracetamol caused the injury; therapeutic dosing produces only low adduct levels."),
    ('c', "**AcetaSTAT: a competitive immunoassay giving a positive or negative result only.** It is a rapid strip test designed for the bedside where HPLC is not available; it answers ‘has paracetamol injured this liver?’ but does not give a number."),
  ],
  mimic=[
    ("Paracetamol level vs adducts", "The level measures drug still in the blood and guides NAC early; adducts measure injury already done and identify the cause late."),
  ],
  traps=[
    ("“An undetectable level excludes paracetamol as the cause of liver failure”", "The drug is cleared within a day; adducts persist and can prove the cause."),
    ("“Adducts are raised in anyone taking therapeutic paracetamol”", "Therapeutic dosing gives only low levels; the high cut-off with ALT >1000 is what matters."),
  ],
  decode=[
    ("Acute liver failure, denies overdose, paracetamol undetectable", "Paracetamol–protein adducts."),
    ("Bedside test for adducts", "AcetaSTAT (qualitative)."),
  ],
  punch="When the drug has gone but the liver has failed, adducts are the fingerprint NAPQI left on the dead cells — proof of cause, not a guide to NAC dosing.",
)

L['APAP-08'] = dict(
  sub="Toxicology → N-acetylcysteine → Mechanism and timing",
  intro="The liver cannot take up glutathione given from outside, but it can make its own from cysteine. N-acetylcysteine delivers that cysteine, so it refills the store that NAPQI is draining. Its effect is greatest before glutathione runs out and NAPQI starts binding proteins — but it still helps after that, by other means.",
  parts=[
    ('a', "**Replenishes glutathione; enhances sulfation; antioxidant and anti-inflammatory.** NAC is deacetylated to cysteine, the rate-limiting building block of glutathione, so NAPQI is captured before it reaches proteins. Its sulphur also supports the sulfation pathway, so less drug goes to oxidation. Once injury has started, its antioxidant action and improved microcirculation limit further damage — the reason it helps even in liver failure."),
    ('b', "**Within 8 hours of ingestion: near-complete protection.** In the first 8 hours glutathione has not yet fallen to the point at which NAPQI binds proteins (APAP-02), so refilling it prevents almost all injury. After that, protein binding has begun and each hour of delay allows more necrosis."),
    ('c', "**Activated charcoal 1 g/kg (maximum 50 g) within 4 hours of a single ingestion; not with altered sensorium unless the airway is protected.** The usual window is 1 hour (TOX-09); some guidelines extend it for paracetamol because large or modified-release overdoses keep absorbing for hours — Australia–NZ, for example, uses 2 hours for an ordinary toxic dose and up to 4 hours for very large (over 30 g) or modified-release ingestions. As with all charcoal, aspiration is the danger, hence the airway condition."),
  ],
  mimic=[
    ("NAC before vs after 8 hours", "Before 8 hours it prevents injury by refilling glutathione; after 8 hours it limits injury that has already begun, so it is still given."),
  ],
  traps=[
    ("“After 8 hours NAC is useless”", "It is still given late and in established liver failure; it improves outcome."),
    ("“A patient arriving at 7 hours should wait for the level before NAC”", "If the level will not be back by 8 hours and the dose is over 150 mg/kg, start NAC now (APAP-14)."),
    ("“NAC works by binding paracetamol”", "It replenishes glutathione, which binds NAPQI."),
  ],
  decode=[
    ("Main mechanism of NAC", "Replenishes glutathione."),
    ("Window for near-complete protection", "Within 8 hours."),
    ("Presents 30 hours after overdose with ALT 4000", "Give NAC — late treatment still improves outcome."),
  ],
  punch="NAC refills the glutathione that NAPQI drains: given within 8 hours it prevents injury almost completely, and given later it still limits the damage — so it is never withheld for being late.",
)

L['APAP-09'] = dict(
  sub="Toxicology → N-acetylcysteine → Regimens",
  intro="NAC can be given intravenously over about a day or by mouth over three days. Both regimens aim at the same thing — enough cysteine to keep glutathione ahead of NAPQI until the paracetamol has been cleared — and they differ in route, length and side effects.",
  parts=[
    ('a', "**IV 21-hour protocol: bag 1 150 mg/kg in 200 mL 5% dextrose over 60 min; bag 2 50 mg/kg in 500 mL over 4 h; bag 3 100 mg/kg in 1000 mL over 16 h — 300 mg/kg in total.** The large first dose refills glutathione quickly while NAPQI production is at its peak; the smaller later bags (12.5 then 6.25 mg/kg/h) keep it topped up while the remaining paracetamol is cleared. Bag 1 was originally run over 15 minutes; lengthening it to 60 minutes was meant to reduce reactions, though trials showed little difference."),
    ('b', "**Oral protocol: 140 mg/kg, then 70 mg/kg every 4 h for 17 doses (72 hours).** The oral route delivers NAC straight to the liver through the portal vein, but its systemic bioavailability is low (about 10%) and the sulphurous taste and vomiting make doses hard to keep down. The 72-hour length comes from the original US protocol design rather than from proof that so long a course is needed."),
    ('c', "**IV is chosen for vomiting, no oral route, pregnancy and liver failure.** In all of these the oral dose may not be absorbed or tolerated, and in liver failure and pregnancy reliable delivery matters most."),
    ('d', "**Main adverse effect of IV: an anaphylactoid reaction — rate-related, not IgE — so slow or pause, give an antihistamine, then restart.** NAC releases histamine directly, most often during the high-concentration first bag, giving flushing, rash, wheeze and sometimes hypotension. Because no antibody is involved, it is not true allergy and not a contraindication; the infusion is restarted once the reaction settles."),
  ],
  table=dict(title="a — The IV 21-hour protocol", head=["Bag", "Dose", "In", "Over", "Why"], rows=[["1", "**150 mg/kg**", "200 mL 5% dextrose", "**60 min**", "refill glutathione fast"], ["2", "**50 mg/kg**", "500 mL", "**4 h**", "maintain"], ["3", "**100 mg/kg**", "1000 mL", "**16 h**", "maintain while drug clears (6.25 mg/kg/h)"], ["Total", "**300 mg/kg**", "", "21 h", ""]]),
  mimic=[
    ("Anaphylactoid vs anaphylactic reaction", "Anaphylactoid is direct histamine release related to rate and concentration; it does not need prior exposure and allows NAC to be restarted."),
  ],
  traps=[
    ("“A rash on bag 1 means NAC must be stopped for good”", "It is anaphylactoid: pause, antihistamine, restart."),
    ("“The first IV bag is 150 mg/kg over 15 minutes”", "The original protocol used 15 minutes; your notes print 60 minutes, which is current practice in the three-bag regimen."),
    ("“The oral course lasts 21 hours”", "Oral is 72 hours (loading dose plus 17 doses); IV is 21 hours."),
  ],
  decode=[
    ("First IV NAC bag", "150 mg/kg in 200 mL over 60 min."),
    ("Total IV dose", "300 mg/kg over 21 hours."),
    ("Flushing and wheeze 30 minutes into NAC", "Anaphylactoid reaction — pause, antihistamine, restart."),
  ],
  punch="Both regimens refill glutathione — IV front-loads it over 21 hours, oral spreads it over 72 — and the IV reaction is anaphylactoid, so it means slowing down, not stopping.",
  extra=[dict(q="Newer IV regimens with fewer reactions?", a="**Two-bag** (Australia–NZ): 200 mg/kg over 4 h, then 100 mg/kg over 16 h. **SNAP** (Scottish, Bateman, Lancet 2014): 100 mg/kg over 2 h, then 200 mg/kg over 10 h — 12 hours. Both give 300 mg/kg but avoid the high-concentration first bag: in its trial SNAP cut both vomiting and anaphylactoid reactions, and the two-bag regimen mainly reduces reactions.")],
)

L['APAP-10'] = dict(
  sub="Toxicology → N-acetylcysteine → When to stop",
  intro="The 21-hour protocol is a fixed course, but the patient may not be finished when the bags are. NAC is needed for as long as paracetamol is still being turned into NAPQI or the liver is still being injured. So, at the end of the course, the decision to stop rests on three blood tests rather than the clock.",
  parts=[
    ('a', "**Stop when paracetamol is undetectable, ALT is falling, and INR is below 2.** An undetectable level means no more NAPQI is being made. A falling ALT means necrosis has stopped. An INR under 2 means synthetic function is preserved. Together they show that the poison has gone and the liver is recovering."),
    ('b', "**If not met at 21 hours, continue at 6.25 mg/kg/h — the third-bag rate — and repeat the tests 12-hourly.** The third bag gives 100 mg/kg over 16 hours, which is 6.25 mg/kg/h; continuing at that rate maintains the protection without a new loading dose."),
    ('c', "**In established liver failure, continue until transplant or resolution.** NAC still improves survival once the liver is failing (APAP-08), so it is continued for as long as the failure lasts."),
  ],
  mimic=[
    ("Falling ALT: recovery vs burnout", "A falling ALT with a falling INR means recovery; a falling ALT with a rising INR means too few hepatocytes are left — a bad sign (APAP-11)."),
  ],
  traps=[
    ("“The 21-hour course is complete, so stop NAC”", "Stop only if the level is undetectable, ALT falling and INR below 2."),
    ("“Restart with a new 150 mg/kg loading bag”", "Continue at the third-bag rate, 6.25 mg/kg/h."),
  ],
  decode=[
    ("End of 21 h: level undetectable, ALT rising, INR 2.4", "Continue NAC at 6.25 mg/kg/h, repeat tests in 12 hours."),
    ("Criteria for stopping NAC", "Undetectable level, falling ALT, INR <2."),
  ],
  punch="NAC is stopped by the blood tests, not the clock: when no drug is left, the ALT is falling and the INR is under 2 — otherwise it continues at the third-bag rate.",
)

L['APAP-11'] = dict(
  sub="Toxicology → Transplant & Sweep → King’s College criteria",
  intro="Most patients with paracetamol liver failure recover with NAC and intensive care, but some will die without a transplant, and the liver must be found in time. King’s College criteria pick out the group most likely to die, using markers of how much liver function is left. Transaminases are not among them: they measure how many cells died, not how many survive.",
  parts=[
    ('a', "**Arterial pH below 7.30 after fluid resuscitation; OR all three of creatinine above 3.4 mg/dL, grade 3 or 4 encephalopathy and INR above 6.5 (PT above 100 s).** A persistent acidosis despite fluids means the liver can no longer clear lactate and other acids. INR measures loss of synthetic function, encephalopathy loss of detoxification, and creatinine the hepatorenal and direct renal injury. Each limb is a measure of what the liver can no longer do."),
    ('b', "**Specificity 90%, sensitivity only 60%: it misses patients who will die.** When the criteria are met, death without transplant is very likely, so listing is justified. But a large share of patients who die never meet them, so failing to meet the criteria is not reassurance."),
    ('c', "**Lactate modification: above 3.5 after 1 hour of fluid resuscitation, or above 3.0 after adequate fluids.** Lactate rises early because the necrotic liver both fails to clear it and produces it. In the original study (Bernal, Lancet 2002) the units are mmol/L, the early value was measured about 4 hours after admission and the later one at about 12 hours, after full fluid resuscitation; adding the post-resuscitation lactate raised the sensitivity of King’s criteria from 76% to 91% and identified non-survivors hours earlier."),
  ],
  table=dict(title="King’s College criteria — paracetamol", head=["Route", "Criterion"], rows=[["Alone", "**pH <7.30** after fluids (or lactate >3.0 mmol/L after adequate fluids)"], ["All three", "**INR >6.5**, **creatinine >3.4 mg/dL** (300 µmol/L), **grade 3–4 encephalopathy**"]]),
  mimic=[
    ("Paracetamol vs non-paracetamol King’s criteria", "Non-paracetamol criteria use INR >6.5 alone, or three of five (age, aetiology, jaundice-to-encephalopathy interval, INR >3.5, bilirubin); pH and creatinine are the paracetamol limbs."),
  ],
  traps=[
    ("“ALT is the prognostic marker”", "ALT measures injury, not outcome; pH, INR, creatinine, encephalopathy and lactate predict death."),
    ("“Not meeting King’s criteria means the patient will survive”", "Sensitivity is only about 60%."),
    ("“A falling ALT means recovery”", "With a rising INR it means too little liver is left."),
  ],
  decode=[
    ("pH 7.25 after fluids in paracetamol liver failure", "Meets King’s criteria — list for transplant."),
    ("Best prognostic marker among options including ALT", "Creatinine, pH, INR or lactate — not ALT."),
    ("King’s criteria: strength and weakness", "High specificity, low sensitivity."),
  ],
  punch="King’s College criteria measure what the liver can no longer do — clear acid, make clotting factors, protect the brain and the kidneys — so they predict death well when met, but miss many who will still die.",
)

L['APAP-12'] = dict(
  sub="Toxicology → Transplant & Sweep → Adjuncts in massive overdose",
  intro="In a massive overdose NAC alone may not keep up. Enormous levels can also poison mitochondria directly, giving coma and lactic acidosis within hours, before the liver injury of stage III. Adjuncts aim either to stop NAPQI being made or to remove the paracetamol itself — but each sits on top of NAC, never in place of it.",
  parts=[
    ('a', "**Fomepizole: a CYP2E1 inhibitor, an emerging adjunct to NAC (case reports).** Blocking CYP2E1 reduces NAPQI formation at its source, which is attractive when the drug load is too large for glutathione to cope with. In mice it also blocks JNK-mediated mitochondrial injury, which may explain benefit even after metabolism. The human evidence is limited to case reports, and no guideline yet sets a dose or threshold for it."),
    ('b', "**Haemodialysis clears paracetamol; it is used in massive ingestion with severe lactic acidosis, and is never a substitute for NAC.** Paracetamol is a small molecule with low protein binding and a modest volume of distribution, so dialysis removes it efficiently. The EXTRIP workgroup (2014) recommends it — intermittent haemodialysis preferred — for a level above 1000 mg/L without NAC, or for signs of mitochondrial dysfunction (altered mental status, metabolic acidosis, raised lactate) with a level above 700 mg/L without NAC or above 900 mg/L with NAC. It corrects the acidosis and lowers the drug load, but NAC must continue — at a higher rate, because dialysis also removes NAC."),
    ('c', "**Cimetidine worked in animals but gave no benefit in humans.** It is a CYP inhibitor and in theory should reduce NAPQI formation; in clinical use it did not improve outcome, so it has no role."),
  ],
  mimic=[
    ("Early vs late acidosis in paracetamol poisoning", "Early (hours), with coma and a massive level, is mitochondrial toxicity — dialysis is considered. Late (days 3–4) is from liver failure — a King’s College criterion (APAP-11)."),
  ],
  traps=[
    ("“Dialysis can replace NAC in massive overdose”", "It is always added to NAC, never instead of it."),
    ("“Cimetidine is a useful CYP inhibitor adjunct”", "It showed no benefit in humans."),
    ("“Fomepizole is only for toxic alcohols”", "It also inhibits CYP2E1 and is an emerging adjunct here."),
  ],
  decode=[
    ("Massive paracetamol ingestion, comatose, severe lactic acidosis, level 950 mg/L on NAC", "Haemodialysis (EXTRIP) plus NAC at an increased rate."),
    ("CYP2E1 inhibitor as an adjunct to NAC", "Fomepizole."),
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
    ('d', "**False — acute alcohol is protective; chronic alcohol harms.** Acute ethanol competes for CYP2E1; chronic use induces it (APAP-03)."),
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
    ("Statements about metabolism", "Ask which pathway makes NAPQI — CYP2E1, not conjugation."),
    ("Statements about the nomogram", "Check the time (≥4 h) and which line (200, 150, 100)."),
  ],
  punch="Every statement here turns on a mechanism from earlier in the deck — CYP2E1 making NAPQI in zone 3, absorption complete by 4 hours, and stopping or listing decided by what the liver can still do.",
)

L['APAP-14'] = dict(
  sub="Toxicology → Transplant & Sweep → Indications for NAC",
  intro="NAC is safe and the cost of missing paracetamol toxicity is a dead liver, so the indications are deliberately broad. They follow one logic: treat whenever the nomogram says the dose is toxic, whenever the nomogram cannot be used but toxicity is possible, and whenever the liver is already injured.",
  parts=[
    ('a', "**Single ingestion with a level at 4 hours or later above the treatment line.** This is the nomogram doing its job: a known time and a valid level place the patient in the risk zone (APAP-06)."),
    ('b', "**More than 150 mg/kg (7.5 g) with no level available within 8 hours.** Protection is near-complete only if NAC starts within 8 hours (APAP-08), so waiting for a delayed result throws away the window. Start on the dose and stop if the level returns below the line."),
    ('c', "**Unknown dose or time with a level above 10 µg/mL.** Without a time the level cannot be plotted, so any measurable paracetamol means drug is still present to form NAPQI."),
    ('d', "**Any ingestion with evidence of liver injury.** A raised ALT shows that NAPQI has already overwhelmed glutathione, whatever the level or the history; NAC limits further injury."),
    ('e', "**Presentation after 24 hours with liver injury.** The nomogram ends at 24 hours, but NAC still improves outcome in late presenters and in liver failure (APAP-08)."),
  ],
  table=dict(title="The logic of the indications", head=["Situation", "Why treat"], rows=[["Level above the line at ≥4 h", "nomogram says toxic"], ["Level not back by 8 h, >150 mg/kg", "protect the 8-hour window"], ["Unknown time, level >10", "nomogram unusable, drug present"], ["Liver injury, any ingestion", "injury already under way"], ["After 24 h with injury", "late NAC still helps"]]),
  mimic=[
    ("Acute single vs repeated supratherapeutic ingestion", "Acute: these five indications and the nomogram. Repeated: dose, level >20 or raised ALT (APAP-04)."),
  ],
  traps=[
    ("“No paracetamol in the history, so no level”", "Send a paracetamol level in every deliberate overdose: co-ingestion is common, histories are unreliable and stage I looks harmless."),
    ("“Wait for the level even if it will take 10 hours”", "Over 150 mg/kg with no result by 8 hours — start NAC."),
    ("“Presented at 30 hours, beyond the nomogram, so NAC is pointless”", "Late NAC still improves outcome when the liver is injured."),
  ],
  decode=[
    ("Took 12 g, level will not be available for 9 hours", "Start NAC now."),
    ("Found with empty strips, time unknown, level 18 µg/mL", "Treat — unknown time with a detectable level."),
    ("Combination analgesic overdose with vomiting, other drug named", "Suspect paracetamol: level and NAC."),
  ],
  punch="NAC is given whenever toxicity is shown, cannot be ruled out in time, or has already begun — because the drug is safe and the window is short.",
)

FLAGS = {}
FLAGS['APAP-01'] = "WATCH says pesticides ‘dominate’ — true of poisoning in India, but the commonest causes of acute liver failure in India are viral hepatitis (HEV, HBV) and anti-tubercular drug injury, not pesticides. Consider rewording."
FLAGS['APAP-03'] = "Card groups anticonvulsants under ‘CYP2E1 inducers’; only isoniazid (and alcohol) act mainly on CYP2E1 — phenytoin, carbamazepine, phenobarbital and rifampicin induce other CYP isoforms. Evidence for inducers raising risk is weak (UK dropped the high-risk line in 2012). Explanation says ‘CYP inducers’."
FLAGS['APAP-04'] = "Repeated-ingestion dose thresholds vary by guideline and the card’s 7.5 g / 4 g in 24 h matches none exactly: US out-of-hospital consensus (Dart 2006) and Australia–NZ use ≥10 g or 200 mg/kg in 24 h, or ≥6 g or 150 mg/kg per 24 h for ≥48 h; Australia–NZ adds 4 g or 100 mg/kg in 24 h with risk factors. The level >20 µg/mL and ALT >50 triggers agree (Australia–NZ). Explanation states the range."
FLAGS['APAP-05'] = "Stage IV timing: Goldfrank places recovery from about day 4–5 to 2 weeks, with histological recovery up to 3 months; ‘usually complete by day 7’ is optimistic. Explanation adds this."
FLAGS['APAP-08'] = "Charcoal ‘within 4 hours’ is broader than most guidelines: the usual window is 1 hour; Australia–NZ uses 2 hours for a toxic immediate-release dose and up to 4 hours only for >30 g or modified-release ingestions. Explanation says this."
FLAGS['APAP-11'] = "Lactate modification (Bernal, Lancet 2002): >3.5 mmol/L about 4 h after admission (early) or >3.0 mmol/L at about 12 h after full fluid resuscitation. The card’s ‘after 1 hour of fluid resuscitation’ does not match the original timing; the explanation gives the original timing."
FLAGS['APAP-14'] = "WATCH ‘IV NAC for 12 hours, then repeat the tests’ for repeated ingestion is not universal: the Australian (RCH) guideline, for example, gives the full regimen and rechecks paracetamol and ALT about 2 hours before it ends. Treat as source-specific."
