# ENDO02A — Explain v3 ("Learn" depth): glucose control in critical care — the numbers, stress hyperglycaemia (drivers, cytokine routes, sources and sinks),
# harm and HbA1c, the protocol and the trials (Leuven, VISEP, GLUCONTROL, NICE-SUGAR), monitoring (point-of-care meters, CGM, closed loop) and hypoglycaemia.
# No mnemonics or hooks. Driven by the real questions in qpack/ENDO02A.md (GLY-21 treating hypoglycaemia asked 4 times, with a disputed DocT GT key;
# GLY-05 and GLY-08 3 each, mostly the same DocT stems; GLY-22 twice; GLY-01, 06, 07, 11, 15, 17, 19 once). 11 cards were never asked and get short entries.
# Fields as TOX01, plus SPINE, PRIMER and step. The table card (GLY-07) takes parts a, b, c in the order of its columns; GLY-13 takes a–d in the order of its rows.
# Figures checked online on 22 Nov 2026:
#  - SCCM 2024 glycaemic control guideline (Crit Care Med 2024;52:e161–e181), SCCM guideline page: good practice — start a protocol for persistent glucose ≥180 mg/dL;
#    conditional (moderate) — against titrating to 80–139 vs 140–200 mg/dL; continuous IV rather than intermittent SC insulin (very low); monitoring ≤1-hourly or
#    continuous during instability on IV insulin (low); protocol with explicit decision support (moderate); trials of HbA1c-individualised targets recommended;
#    no statement on point-of-care devices; CGM left to research.
#  - ADA hospital chapter, Section 16 of the Standards of Care 2024 (Diabetes Care 2024;47 Suppl 1:S295–S306, read on PMC; the 2025/2026 PMC pages were behind a bot check):
#    HbA1c for all with diabetes or hyperglycaemia (>140 mg/dL) if none in the past 3 months; insulin for persistent hyperglycaemia from ≥180; ICU goal 140–180 for most;
#    non-ICU goal 100–180; 110–140 for selected patients without significant hypoglycaemia; bedside checks every 30 min to 2 h on IV insulin; SGLT2 inhibitors stopped
#    3–4 days before surgery; level 1 54–69, level 2 <54, level 3 altered state needing assistance. Hypoglycaemia levels (<70, <54, level 3 = altered status needing help) are the ADA/IHSG grading, Section 6 of the Standards.
#  - NICE-SUGAR (NEJM 2009; ACC trial summary): 6104 patients, 81–108 vs ≤180 mg/dL; 90-day mortality 27.5% vs 24.9% (P = 0.02; NNH 38); 28-day 22.3% vs 20.8% (NS);
#    severe hypoglycaemia (≤40) 6.8% vs 0.5%; deaths from cardiovascular causes higher with intensive control.
#  - NICE-SUGAR hypoglycaemia follow-up (NEJM 2012; ACC journal scan): 6026 patients; moderate 41–70 mg/dL in 45.0% (74.2% of the intensive arm), severe ≤40 in 3.7%
#    (6.9% of the intensive arm); death 23.5% without, 28.5% moderate, 35.4% severe; adjusted HR 1.41 and 2.10; stronger with moderate hypoglycaemia on more than one day
#    and for death from distributive shock; severe hypoglycaemia without insulin HR 3.84; an association.
#  - Trial table (Crit Care 2014;18:cc13998): Leuven I 1548; Leuven II 1200 long-stay medical; VISEP 537, stopped early, severe hypoglycaemia 17.0% vs 4.1%, 90-day mortality
#    39.7% vs 35.4% (NS); GLUCONTROL 1101, ICU mortality 15.3% vs 17.2% (NS), hypoglycaemia 8.7% vs 2.7%.
#  - GLUCONTROL abstract (Intensive Care Med 2009): 7.8–10.0 vs 4.4–6.1 mmol/L, stopped early for ‘a high rate of unintended protocol violations’, underpowered.
#  - TGC-fast (NEJM 2023): 9230 patients without early parenteral nutrition; tight 80–110 with LOGIC-Insulin vs liberal (insulin only >215); morning glucose 107 vs 140;
#    severe hypoglycaemia 1.0% vs 0.7%; ICU stay HR 1.00; 90-day mortality 10.5% vs 10.1%.
#  - LUCID (Am J Respir Crit Care Med 2022): 419 with type 2 diabetes; liberal 180–252 (insulin >252) vs 108–180; hypoglycaemia <72 5% vs 18% (IRR 0.21);
#    90-day mortality 29.5% vs 24.9% (P = 0.29); no patient-centred benefit.
#  - Second check (22 Nov 2026): Leuven II abstract (NEJM 2006; in-hospital mortality 40.0% vs 37.3%, ≥3 days 52.5% → 43.0%, <3 days higher with intensive therapy);
#    VISEP (wikijournalclub, Relias summary): AKI 34.9% vs 22.8%, RRT 31.0% vs 18.8% with 10% HES vs Ringer’s lactate; insulin arm stopped by the DSMB for hypoglycaemia,
#    HES arm at the interim analysis; CONTROLING (Intensive Care Med 2021; The Bottom Line): 2075 randomised in 12 French ICUs, target = HbA1c-estimated glucose + 15 mg/dL,
#    stopped at 49% of planned size for low likelihood of benefit and possible harm, 90-day survival 67.2% vs 69.6% (NS), severe hypoglycaemia 3.9% vs 2.5%;
#    Krinsley and Grover (Crit Care Med 2007): severe hypoglycaemia <40, adjusted OR for death 2.28, ‘even a single episode’ independently associated; SCCM 2024 page re-read.
# From standard teaching and memory (worded softly or restated as the card gives them, not re-verified): Leuven I/II subgroup figures beyond those on the cards
# (Leuven II severe hypoglycaemia 18.7% vs 3.1% is the published figure), the incidence figures on GLY-03 and GLY-19, the meter-agreement and hypotension accuracy figures on GLY-17, the AACE/ACE 2016 CGM statement on GLY-18,
# the ISO 15197:2013 meter standard (95% of readings within ±15 mg/dL below 100 and ±15% at 100 or more),
# the stress hyperglycaemia ratio and the ADAG estimated-average-glucose equation, Vriesendorp’s hypoglycaemia risk factors, Cryer’s glycaemic thresholds.

SPINE = [
  ("The numbers that define control", "Insulin starts when glucose stays at 180 mg/dL or more, the target is 140–180, hypoglycaemia begins below 70 and becomes clinically important below 54, and the quality of control is judged by variability and time in range."),
  ("Stress makes the liver pour glucose", "Cytokines switch on the HPA axis and the sympathetic system, so the liver makes glucose by gluconeogenesis while insulin resistance stops muscle and fat taking it up, and our own drugs and feeds add to the load."),
  ("High glucose harms, diabetes shifts it", "Hyperglycaemia damages neutrophils, endothelium, kidney and heart, mortality follows a J-curve that is flattened in established diabetes, and HbA1c tells stress hyperglycaemia from diabetes."),
  ("Trials moved the target up", "Leuven suggested 80–110 saved lives, but VISEP, GLUCONTROL and above all NICE-SUGAR showed that chasing it causes hypoglycaemia and, in NICE-SUGAR, more deaths, so a protocolised IV insulin target of 140–180 replaced it."),
  ("Measure glucose you can trust", "Capillary meters are least accurate when glucose is low and when the patient is shocked, oedematous or on pressors, so arterial or laboratory samples confirm doubtful values, and CGM and closed loop are still unproven in the ICU."),
  ("Hypoglycaemia is the bigger danger", "Hypoglycaemia is common, masked by sedation and linked to death in a dose-dependent way, so it is anticipated from its risk factors and treated at once by the route the patient’s consciousness and access allow."),
]

PRIMER = "Blood glucose is set by two flows: glucose entering the blood from the gut and from the liver (glycogenolysis and gluconeogenesis), and glucose leaving it into tissues, much of it into muscle and fat through the insulin-dependent transporter GLUT4. Insulin lowers glucose by switching off hepatic output and opening GLUT4; glucagon, adrenaline, cortisol and growth hormone push the other way. The brain cannot make or store much glucose and takes it up without insulin, which is why a low value injures it within minutes. In this deck glucose is in mg/dL (divide by 18 for mmol/L: 180 mg/dL is 10 mmol/L, 70 is 3.9, 54 is 3.0, 40 is 2.2)."

L = {}

L['GLY-01'] = dict(
  sub="Endocrine → ICU glucose control → The numbers",
  step=1,
  intro="Step 1 sets the numbers every later card uses. Four figures matter: when to start insulin, what range to aim for, where hypoglycaemia begins and which targets are now known to harm. The one linked question asks the target range for a non-diabetic ICU patient whose glucose stays above 200, and 86% got it right; the point to be clear about is why the floor is 140.",
  parts=[
    ('a', "**CBG above 180–200 mg/dL.** This is the level at which persistent hyperglycaemia is treated: SCCM 2024 and ADA both start an insulin protocol when glucose stays at 180 or more. ADA’s definition of hospital hyperglycaemia is lower, any value above 140, and that lower figure is the trigger for checking HbA1c (GLY-11), not for insulin."),
    ('b', "**Below 70 mg/dL (level 1); below 54 mg/dL clinically significant (level 2).** Level 1 is an alert value: the regimen is reviewed and the patient treated. Below 54 neuroglycopenia begins and the episode counts as clinically important; level 3 is any episode with altered mental or physical state needing another person’s help, whatever the number. Trials used their own cut-offs (NICE-SUGAR: moderate 41–70, severe 40 or less), which is why figures differ between cards."),
    ('c', "**140–180 mg/dL.** This is the conventional arm of NICE-SUGAR made into policy: it avoids the deaths and hypoglycaemia of the intensive arm (GLY-15) while keeping glucose below the level at which osmotic diuresis and neutrophil dysfunction appear (GLY-09, GLY-10). ADA allows 110–140 in selected patients, typically cardiac surgical, only where it can be reached without significant hypoglycaemia."),
    ('d', "**Anything below 110 mg/dL: the intensive targets of the trials.** SCCM 2024 goes further than the card: it suggests against titrating insulin to 80–139 at all, compared with 140–200. So in a stem the lower edge of an acceptable target is 140, not 110."),
  ],
  mimic=[
    ("Definition of hyperglycaemia vs threshold to treat", "Above 140 is hospital hyperglycaemia (check HbA1c); 180 or more, persistent, starts insulin."),
    ("Level 1 vs level 2 hypoglycaemia", "Level 1 below 70 is an alert value; level 2 below 54 is clinically significant."),
    ("ICU target vs ward target", "ADA: 140–180 for most ICU patients; since 2024, 100–180 for most non-critically ill ward patients."),
  ],
  traps=[
    ("“110–140 mg/dL” for a non-diabetic ICU patient", "That is close to the old intensive range; SCCM 2024 suggests against anything that reaches into 80–139. The general ICU target is 140–180."),
    ("“The target is 180 because that is the renal threshold”", "DocT’s explanation gives this reason. The renal threshold explains the upper edge, but the target exists because NICE-SUGAR showed harm when the lower edge was pushed down."),
  ],
  decode=[
    ("Non-diabetic ICU patient, glucose persistently above 200 — best target range [DocT QBank]", "140–180 mg/dL (86%). 80–120 and 110–140 are intensive targets."),
    ("[pattern] Glucose at which hypoglycaemia becomes clinically significant", "Below 54 mg/dL (level 2)."),
  ],
  punch="Start insulin when glucose stays at 180 or more, aim for 140–180, treat below 70, and treat anything below 54 as clinically significant; a target reaching below 140 is the intensive control that NICE-SUGAR showed to harm.",
)

L['GLY-02'] = dict(
  sub="Endocrine → ICU glucose control → Variability and time in range",
  step=1,
  intro="Step 1 also needs measures of quality, because a mean glucose of 160 can hide swings from 60 to 300. Variability and time in range are the two metrics used; this card has not been asked.",
  parts=[
    ('a', "**Swings beyond the expected physiological response, quantified by the coefficient of variation; CoV above 20% is high.** The coefficient of variation is the standard deviation divided by the mean, so it does not rise simply because the mean is high. In ICU cohorts high variability is linked to death independently of the mean, but only in patients without diabetes (Krinsley 2013); in diabetics the link is lost."),
    ('b', "**Time in target range: the percentage of time spent in normoglycaemia.** It is calculated from frequent or continuous readings within a chosen band (often 70–180 or 140–180); a higher share in range goes with better outcomes in observational data."),
  ],
  mimic=[
    ("ICU CoV above 20% vs outpatient CGM CoV 36%", "The outpatient CGM goal of 36% or less is a different setting; the ICU card uses 20%."),
  ],
  traps=[
    ("“A normal mean glucose means good control”", "The mean can be normal with hypoglycaemia and hyperglycaemia on the same day; variability and time in range show it."),
  ],
  decode=[
    ("[pattern] Metric that quantifies glycaemic variability", "Coefficient of variation (SD/mean), high above 20%."),
  ],
  punch="Quality of control is judged by how much glucose swings, the coefficient of variation with 20% as the upper limit, and by the share of time spent in range, not by the mean alone.",
)

L['GLY-03'] = dict(
  sub="Endocrine → Stress hyperglycaemia → How common, and how it is viewed",
  step=2,
  intro="Step 2 begins with how often the liver’s stress response shows up as a high glucose. Most ICU patients are hyperglycaemic on admission, which is why the old view treated it as normal; this card has not been asked.",
  parts=[
    ('a', "**75% have glucose above 110 mg/dL; 12% above 200 mg/dL.** These come from the admission data of the Leuven surgical ICU trial (NEJM 2001); series vary with the population and the cut-off, but in every series hyperglycaemia on admission is the rule, not the exception."),
    ('b', "**As an adaptive stress response, so it was not routinely corrected.** Extra glucose supplies insulin-independent tissues, brain, blood cells and immune cells, when perfusion is poor (GLY-05). Until 2001 only values above about 200–215 were treated."),
    ('c', "**As a marker of severe illness: dysglycaemia is linked to higher mortality.** The higher the glucose, the sicker the patient and the higher the death rate (GLY-04); hypoglycaemia and variability are linked even more strongly. A marker is not necessarily a cause, which is why lowering glucose hard did not save lives (GLY-15)."),
  ],
  mimic=[
    ("Stress hyperglycaemia vs undiagnosed diabetes", "Both raise glucose on admission; HbA1c separates them (GLY-11)."),
  ],
  traps=[
    ("“Admission hyperglycaemia means the patient is diabetic”", "Most of it is stress hyperglycaemia; HbA1c shows whether diabetes was there before."),
  ],
  decode=[
    ("[pattern] Current view of hyperglycaemia on ICU admission", "A marker of illness severity linked to mortality, treated when persistent at 180 or more."),
  ],
  punch="Hyperglycaemia on admission is the rule in critical illness; once seen as harmless adaptation, it is now read as a marker of severity that is treated when it persists at 180 or more.",
)

L['GLY-04'] = dict(
  sub="Endocrine → ICU glucose control → The glucose-mortality curve",
  step=3,
  intro="Step 3 is about harm, and the J-curve shows it in one picture: mortality rises on both sides of normal glucose, faster on the low side, and less steeply in people who have lived with high glucose for years. This card has not been asked, but it explains the targets of step 4.",
  parts=[
    ('a', "**J-shaped; lowest risk at normoglycaemia (about 90–140 mg/dL).** In large observational cohorts mortality is lowest when mean glucose is in the normal to slightly raised range and climbs above and below it."),
    ('b', "**Without diabetes, the hyperglycaemic limb rises almost linearly; the hypoglycaemic limb is even steeper.** A fall of a few tens of mg/dL below normal carries more excess risk than a similar rise above it, because the brain depends on glucose minute by minute. The steep low limb is why intensive targets failed: aiming at 80–110 pushed many patients onto it."),
    ('c', "**In established diabetes the curve is flattened out: chronic hyperglycaemia is better tolerated.** Cells adapted to high glucose reduce their transporters, so the same value does less intracellular harm, and a ‘normal’ value can be relative hypoglycaemia for that patient. This is the reason for trials of liberal targets in diabetes; LUCID (2022) reduced hypoglycaemia but did not improve outcomes (GLY-11)."),
  ],
  mimic=[
    ("Non-diabetic vs diabetic J-curve", "Non-diabetic: steep on both sides, nadir near normal. Diabetic: flatter, with the nadir shifted higher."),
  ],
  traps=[
    ("“Mortality rises steadily with glucose, so lower is always better”", "The curve turns up sharply below normal; driving glucose low trades a small hyperglycaemic risk for a larger hypoglycaemic one."),
  ],
  decode=[
    ("[pattern] Why intensive insulin therapy failed in mixed ICU patients", "The hypoglycaemic limb of the J-curve is steeper than the hyperglycaemic limb."),
  ],
  punch="Mortality follows a J-curve with its lowest point near normal glucose and a steeper low limb than high limb, and the curve is flatter in established diabetes; that asymmetry is why targets stop at 140, not 80.",
)

L['GLY-05'] = dict(
  sub="Endocrine → Stress hyperglycaemia → Definition, purpose and mechanism",
  step=2,
  intro="Step 2 is where the glucose comes from, and this card is the core: stress hyperglycaemia is the liver making more glucose while the tissues resist insulin. Three DocT stems test it, and the one about a diabetic stroke patient on an insulin infusion was answered correctly by only half the cohort, because ‘lack of insulin’ and ‘protective, don’t treat’ both look reasonable.",
  parts=[
    ('a', "**A relative rise in glucose during acute illness.** ‘Relative’ matters: the rise is measured against the patient’s own baseline, so a diabetic with an HbA1c of 9% can have stress hyperglycaemia at a glucose that would be ordinary for him. The stress hyperglycaemia ratio, admission glucose divided by the average glucose estimated from HbA1c, puts a number on it."),
    ('b', "**It promotes survival: glucose fuels macrophages, and acute hyperglycaemia is anti-apoptotic and angiogenic.** Immune cells, brain and injured tissue take up glucose without insulin through GLUT1 and GLUT3, so a higher concentration drives more glucose into them by diffusion when the microcirculation is poor. Short, moderate rises are therefore useful; the harm comes when the rise is marked or sustained (GLY-09)."),
    ('c', "**The HPA axis and the sympathoadrenal system, with IL-1, IL-6 and TNF-α.** The cytokines start the hormonal response (GLY-06), and the cytokines and hormones together block insulin signalling in muscle and fat."),
    ('d', "**Increased hepatic glucose output (gluconeogenesis and glycogenolysis), plus insulin resistance.** Glycogen is gone within about a day, so sustained output is gluconeogenesis, from lactate, amino acids released from muscle and glycerol from fat. Insulin resistance stops the liver switching off and stops GLUT4 uptake in muscle and fat. Insulin secretion is normal or high; the pancreas is not the problem."),
  ],
  mimic=[
    ("Stress hyperglycaemia vs type 1 diabetes", "Stress: high hepatic output with insulin resistance, insulin levels normal or high. Type 1: absolute insulin deficiency."),
    ("Stress hyperglycaemia vs steroid-induced hyperglycaemia", "Both involve insulin resistance; steroids are one of the drug causes that add to stress (GLY-07)."),
  ],
  traps=[
    ("“Hyperglycaemia is primarily due to lack of insulin secretion”", "Chosen by many of the 50% who missed the stroke stem. Insulin secretion is preserved or increased; the problem is hepatic overproduction and resistance to insulin’s action."),
    ("“Stress hyperglycaemia is protective and should not be treated aggressively”", "DocT’s planted half-truth. It is adaptive in origin, but persistent glucose at 180 or more is treated; ‘not aggressively’ is right only in the sense of not chasing 80–110."),
    ("“Easily managed with oral hypoglycaemic agents”", "In the ICU oral agents are stopped and an IV insulin protocol is used (GLY-12)."),
  ],
  decode=[
    ("Well-controlled type 2 diabetic after a severe stroke, persistent hyperglycaemia on an insulin infusion — best describes the pathophysiology [DocT QBank]", "Increased hepatic gluconeogenesis and insulin resistance (50%)."),
    ("Most accurate statement about the source of increased glucose production in critical illness [DocT QBank]", "The liver, through gluconeogenesis (67%)."),
    ("Non-diabetic road traffic victim, glucose 160–200 — key characteristic of stress hyperglycaemia [DocT QBank]", "Both increased hepatic glucose output and insulin resistance (77%)."),
  ],
  punch="Stress hyperglycaemia is the liver making more glucose, mainly by gluconeogenesis, while cytokines and counter-regulatory hormones make muscle and fat resistant to insulin; insulin secretion is not the problem, and the rise is adaptive but still treated once it persists at 180 or more.",
)

L['GLY-06'] = dict(
  sub="Endocrine → Stress hyperglycaemia → Cytokines, the HPA axis and catecholamines",
  step=2,
  intro="Step 2 continues with the wiring: which cytokine acts where, and how the signal reaches the liver. The one DocT question asks which cytokine stimulates the adrenal cortex directly; 67% chose IL-6. The card sends IL-6 only to the pituitary, so the direct adrenal action is the addition here.",
  parts=[
    ('a', "**IL-1 and TNF act on the hypothalamus (paraventricular nucleus) → CRH.** They reach the hypothalamus through the circumventricular organs and vagal afferents and release corticotrophin-releasing hormone. TNF-α also blunts the adrenal response to ACTH, so it is the wrong answer for direct adrenal stimulation."),
    ('b', "**IL-6 acts on the anterior pituitary → ACTH → adrenal cortex → cortisol.** IL-6 also stimulates the adrenal cortex directly, releasing cortisol without ACTH; this is part of the explanation for the high cortisol with low ACTH seen in prolonged critical illness, alongside the slower breakdown of cortisol in the liver and kidney."),
    ('c', "**Cortisol feeds back on the PVN, the pituitary and immune cells (negative feedback).** The feedback on immune cells is the anti-inflammatory arm: cortisol damps cytokine release and so limits its own stimulus."),
    ('d', "**Locus coeruleus → adrenal medulla (adrenaline) and sympathetic nerves (noradrenaline); both drive hepatic gluconeogenesis and glycogenolysis.** Adrenaline also suppresses insulin release through α2 receptors on the beta cell and makes muscle resistant to insulin, which is why an adrenaline infusion raises glucose and lactate."),
  ],
  mimic=[
    ("IL-6 vs IL-1 / TNF-α", "IL-6: pituitary and directly adrenal. IL-1 and TNF-α: hypothalamus; TNF-α blunts the adrenal response to ACTH."),
  ],
  traps=[
    ("“TNF-α directly induces cortisol release from the adrenal cortex”", "TNF-α acts centrally and actually blunts adrenal responsiveness to ACTH; the direct adrenal stimulant is IL-6."),
    ("“IL-1 is the cytokine acting on the adrenal”", "IL-1 acts mainly on the hypothalamus to release CRH."),
  ],
  decode=[
    ("Cytokine that directly induces cortisol release from the adrenal cortex [DocT QBank]", "IL-6 (67%)."),
    ("[pattern] High cortisol with low ACTH in prolonged critical illness", "ACTH-independent drive (IL-6 on the adrenal) and reduced cortisol breakdown."),
  ],
  punch="IL-1 and TNF-α start the cascade at the hypothalamus, IL-6 acts on the pituitary and directly on the adrenal cortex, cortisol feeds back on all three levels, and adrenaline and noradrenaline drive the liver alongside it.",
)

L['GLY-07'] = dict(
  sub="Endocrine → Stress hyperglycaemia → What adds to it",
  step=2,
  intro="Step 2 ends with what pushes glucose up on top of the illness itself: the counter-regulatory hormones, the things we do to the patient, and what the patient brings. The one linked question asks which hormone contributes to DKA and HHS, and fewer than half chose cortisol.",
  parts=[
    ('a', "**Counter-regulatory hormones: glucagon, glucocorticoids, growth hormone, catecholamines.** All four oppose insulin. Glucagon and adrenaline raise hepatic output within minutes; cortisol and growth hormone act over hours by increasing gluconeogenesis and insulin resistance. The same four, with relative or absolute insulin deficiency, drive DKA and HHS."),
    ('b', "**Interventions: enteral or parenteral nutrition, dextrose solutions, steroids, vasopressors, dialysis, bed rest.** Feeds and dextrose add substrate; steroids and catecholamine pressors add counter-regulation; dextrose-containing dialysate or replacement fluid adds glucose; bed rest causes muscle insulin resistance within days. These are the causes the ICU team can change, and they are checked first when glucose rises."),
    ('c', "**Pre-existing: diabetes, obesity, cirrhosis.** Each reduces insulin sensitivity or secretion before the illness starts; cirrhosis also reduces hepatic insulin clearance and glycogen storage."),
  ],
  mimic=[
    ("Cortisol vs insulin in DKA/HHS", "Cortisol is a contributing counter-regulatory hormone; insulin deficiency is the defect, not a contributing hormone."),
  ],
  traps=[
    ("“Insulin contributes to DKA and HHS”", "Half the GT8 cohort missed this item (49% right). It is the lack of insulin that causes them; the hormones that contribute are the counter-regulatory ones, cortisol among them."),
    ("“TSH” or “oestrogen”", "Neither is a counter-regulatory hormone; thyrotoxicosis can precipitate a crisis, but TSH itself does not raise glucose."),
  ],
  decode=[
    ("Hormone that contributes to DKA and HHS [DocT GT]", "Cortisol (49%): one of the four counter-regulatory hormones."),
    ("[pattern] Glucose rising on day 3 in a stable patient", "Look for the interventions: new feed, dextrose, hydrocortisone, noradrenaline, dialysis fluid."),
  ],
  punch="Glucagon, cortisol, growth hormone and catecholamines oppose insulin, and nutrition, dextrose, steroids, pressors, dialysis and bed rest add to the illness; insulin deficiency is the defect in DKA and HHS, cortisol a contributor.",
)

L['GLY-08'] = dict(
  sub="Endocrine → Stress hyperglycaemia → Sources and sinks of glucose",
  step=2,
  intro="Step 2 is about sources, and this card names the organs. Three DocT stems ask where the extra glucose comes from and what adipose tissue does with it; the adipose question (62%) and the stroke stem (50%) are where people lose marks, because ‘insulin-dependent’ and ‘insulin-independent’ uptake are easily swapped.",
  parts=[
    ('a', "**The liver, by gluconeogenesis.** The liver has the enzymes to release free glucose, and in critical illness gluconeogenesis is driven by glucagon, cortisol and catecholamines and fed by lactate, alanine and glycerol. Insulin normally switches this off; in critical illness it fails to, which is hepatic insulin resistance. The kidney adds a smaller share."),
    ('b', "**Muscle lacks glucose-6-phosphatase, so its glycogen serves only itself.** Glycogen breaks down to glucose-6-phosphate, which cannot leave the cell without this enzyme. Muscle contributes to blood glucose only indirectly, by releasing lactate and alanine that the liver turns into glucose."),
    ('c', "**Adipose tissue shifts to insulin-independent uptake via GLUT1; GLUT4 is the insulin-dependent transporter.** Insulin resistance closes GLUT4 in fat and muscle, while cytokines increase GLUT1, so uptake that continues does so without insulin. Fat does not become a glucose store in critical illness; it releases fatty acids and glycerol."),
  ],
  table=dict(title="Who makes, who takes", head=["Tissue", "Role in stress", "Transporter / enzyme"], rows=[["Liver", "**main source**: gluconeogenesis, early glycogenolysis", "has glucose-6-phosphatase"], ["Skeletal muscle", "indirect source (lactate, alanine), uptake falls", "no glucose-6-phosphatase; GLUT4 resistant"], ["Adipose", "uptake shifts to insulin-independent", "**GLUT1** up, GLUT4 resistant"], ["Brain, blood and immune cells", "insulin-independent users", "GLUT1, GLUT3"]]),
  mimic=[
    ("GLUT1 vs GLUT4", "GLUT1 (and GLUT3): insulin-independent, increased in stress. GLUT4: insulin-dependent, in muscle and fat, resistant in stress."),
  ],
  traps=[
    ("“Skeletal muscle is the primary source of excess glucose via glycogenolysis”", "Muscle has no glucose-6-phosphatase; its glycogen cannot reach the blood."),
    ("“Adipose tissue increases insulin-dependent glucose uptake” or “becomes the primary site of insulin-dependent uptake”", "The opposite: insulin-dependent uptake through GLUT4 falls; what rises is insulin-independent uptake."),
    ("“Adipose tissue mainly stores glucose in critical illness”", "Fat is in net breakdown, releasing fatty acids and glycerol."),
  ],
  decode=[
    ("Role of adipose tissue in glucose metabolism during critical illness [DocT QBank]", "Increased non-insulin-dependent glucose uptake (62%)."),
    ("Source of increased glucose production in critical illness [DocT QBank]", "Liver gluconeogenesis (67%)."),
    ("Diabetic stroke patient on insulin infusion, mechanism of hyperglycaemia [DocT QBank]", "Hepatic gluconeogenesis plus insulin resistance (50%); the adipose option is worded the wrong way round."),
  ],
  punch="The extra glucose comes from the liver by gluconeogenesis, muscle cannot release its glycogen because it lacks glucose-6-phosphatase, and fat and muscle lose insulin-dependent GLUT4 uptake while insulin-independent GLUT1 uptake rises.",
)

L['GLY-09'] = dict(
  sub="Endocrine → Harm of hyperglycaemia → Host defence, vessels, muscle",
  step=3,
  intro="Step 3 explains why stress hyperglycaemia is treated at all. Sustained high glucose damages the defence it was meant to fuel, the blood vessels and the muscles; this card has not been asked.",
  parts=[
    ('a', "**Host defence: neutrophil dysfunction, with less bactericidal activity and opsonisation; mitochondrial dysfunction blunts the inflammatory cascade.** Glucose glycates complement and immunoglobulin, and overloads the neutrophil’s mitochondria, so chemotaxis, phagocytosis and the oxidative burst weaken. This is why the original Leuven trial saw fewer bloodstream infections with tighter control."),
    ('b', "**Blood and vessels: impaired fibrinolysis and platelet function, hypercoagulability and thrombosis; endothelial dysfunction with poor microcirculation.** Cells that cannot limit glucose entry, endothelium among them, make excess reactive oxygen species; nitric oxide falls and PAI-1 rises."),
    ('c', "**Muscle and protein: protein lysis and more skeletal-muscle catabolism.** Insulin resistance removes insulin’s anabolic effect, so muscle protein is broken down for gluconeogenesis."),
  ],
  mimic=[
    ("Acute benefit vs sustained harm", "Short, moderate rises fuel immune cells (GLY-05); marked or sustained rises impair them."),
  ],
  traps=[
    ("“Hyperglycaemia improves immunity because macrophages need glucose”", "Only a modest rise; above about 200 neutrophil function is impaired."),
  ],
  decode=[
    ("[pattern] Mechanism linking hyperglycaemia to infection in ICU", "Neutrophil dysfunction: reduced chemotaxis, phagocytosis and bactericidal activity."),
  ],
  punch="Sustained hyperglycaemia weakens neutrophils, makes blood prothrombotic, damages endothelium and speeds muscle breakdown, which is why it is treated once persistent even though the rise began as adaptation.",
)

L['GLY-10'] = dict(
  sub="Endocrine → Harm of hyperglycaemia → Kidney and heart",
  step=3,
  intro="Step 3 continues with two organ chains a resident can follow at the bedside: the urine and the ECG. This card has not been asked.",
  parts=[
    ('a', "**Kidney: glycosuria → osmotic diuresis → hypovolaemia and electrolyte loss.** Once filtered glucose exceeds tubular reabsorption, about 180 mg/dL in blood, glucose stays in the tubule and carries water, sodium, potassium, magnesium and phosphate with it. The patient can be hypovolaemic with a good urine output."),
    ('b', "**Heart: more free fatty acids → more myocardial oxygen demand → ischaemia → less contractility → arrhythmias.** Insulin resistance increases lipolysis, and the heart burns fatty acids, which yield less ATP per oxygen than glucose; the result is relative ischaemia, and the fatty acids themselves are arrhythmogenic."),
  ],
  mimic=[
    ("Osmotic diuresis vs recovery polyuria", "Osmotic diuresis comes with glycosuria and a high glucose; recovery polyuria from AKI does not."),
  ],
  traps=[
    ("“Good urine output means adequate volume”", "In marked hyperglycaemia the output is osmotic and the patient may be dry."),
  ],
  decode=[
    ("[pattern] Hyperglycaemic patient with high urine output, falling BP and low potassium", "Osmotic diuresis from glycosuria."),
  ],
  punch="High glucose causes an osmotic diuresis that drains volume and electrolytes, and floods the heart with fatty acids that raise oxygen demand and provoke ischaemia and arrhythmias.",
)

L['GLY-11'] = dict(
  sub="Endocrine → ICU glucose control → HbA1c",
  step=3,
  intro="Step 3 ends with the test that tells stress hyperglycaemia from diabetes. HbA1c reflects the last two to three months, so it is unaffected by today’s stress; the linked question (the same DocT stem as GLY-01) checks that a non-diabetic with glucose above 200 still gets 140–180, and the card itself notes that no guideline sets tiers by HbA1c.",
  parts=[
    ('a', "**When glycaemia is above 180 mg/dL.** ADA asks for more: HbA1c in every patient with known diabetes or any glucose above 140, if none has been done in the previous three months. Recent large transfusion, haemolysis, blood loss and advanced kidney disease make the value unreliable."),
    ('b', "**To separate stress hyperglycaemia from diabetes, for prognosis, and to shape the protocol.** An HbA1c of 6.5% or more says diabetes was there before admission and needs follow-up; a normal value says the rise is stress. The stress hyperglycaemia ratio, glucose divided by the average glucose estimated from HbA1c (28.7 × HbA1c − 46.7), predicts outcome better than glucose alone, because it measures the rise against the patient’s own baseline."),
    ('c', "**HbA1c below 7%: 140–180. HbA1c above 7%: the old notes gave a medical target of 180–220, but no guideline uses HbA1c tiers; SCCM 2024 starts insulin at 180 or more, avoids 80–139 and uses 140–180 for all.** SCCM recommends trials of targets stratified by HbA1c rather than adopting them. LUCID (2022, 419 type 2 diabetics, 180–252 vs 108–180) cut hypoglycaemia from 18% to 5% but did not improve outcomes, and a French trial of HbA1c-individualised targets (CONTROLING, 2021) was stopped at about half its planned size for a low likelihood of benefit and possible harm, with no difference in 90-day survival."),
  ],
  mimic=[
    ("Stress hyperglycaemia vs undiagnosed diabetes", "Same glucose; HbA1c below 6.5% says stress, 6.5% or more says diabetes."),
  ],
  traps=[
    ("“A higher target of 180–220 is recommended when HbA1c is above 7%”", "It follows the flattened J-curve (GLY-04) but is not guideline policy; 140–180 is used for everyone, with less aggressive titration in poorly controlled diabetics."),
    ("“A non-diabetic needs a tighter target, 110–140”", "The same 140–180 applies whether or not the patient has diabetes."),
  ],
  decode=[
    ("Non-diabetic ICU patient, glucose persistently above 200 — target range [DocT QBank]", "140–180 (86%); being non-diabetic does not make the target tighter."),
    ("[pattern] New ICU hyperglycaemia, HbA1c 5.4%", "Stress hyperglycaemia: treat to 140–180, no diabetes label."),
  ],
  punch="HbA1c tells stress hyperglycaemia from diabetes and refines prognosis, but the ICU target stays 140–180 for everyone; HbA1c-tiered targets are a research question, and the liberal-target trials so far have only reduced hypoglycaemia.",
)

L['GLY-12'] = dict(
  sub="Endocrine → ICU glucose control → The insulin protocol",
  step=4,
  intro="Step 4 is how the target is reached safely, and the answer from every trial is a written IV protocol. This card has not been asked.",
  parts=[
    ('a', "**IV insulin: poor microcirculation makes subcutaneous absorption unpredictable. Use a regional protocol.** In shock, oedema and on pressors a subcutaneous dose may barely be absorbed and then be absorbed all at once when perfusion returns. IV insulin has a half-life of minutes, so it can be titrated hourly. SCCM 2024 suggests a continuous IV infusion over intermittent subcutaneous insulin in critically ill adults."),
    ('b', "**Hourly checks at first, then 4-hourly once stable.** SCCM 2024 suggests checks at least hourly, or continuous, during instability on IV insulin. ADA calls bedside checks every 30 minutes to 2 hours the required standard for as long as an IV infusion runs; 4-hourly suits a stable patient off the infusion or on subcutaneous insulin with continuous feeds."),
    ('c', "**Protocolisation gives better control, fewer treatment errors, more time in target range and less hypoglycaemia.** SCCM 2024 suggests protocols with explicit decision support (a computer or paper algorithm that sets the rate), because ad hoc titration overshoots."),
  ],
  mimic=[
    ("IV infusion vs subcutaneous basal-bolus", "IV infusion: unstable critically ill. Subcutaneous basal plus correction: stable, eating or on steady feeds, ward patients."),
  ],
  traps=[
    ("“Subcutaneous sliding scale is adequate in shock”", "Absorption is unpredictable; sliding scale alone reacts after the event."),
    ("“4-hourly checks while on an insulin infusion”", "Checks stay every 30 minutes to 2 hours while the infusion runs (ADA), and at least hourly when glucose or feeding is changing (SCCM 2024)."),
  ],
  decode=[
    ("[pattern] Route of insulin in a ventilated patient on noradrenaline", "Continuous IV infusion by protocol."),
  ],
  punch="In the ICU insulin is given as a protocolised IV infusion with frequent checks, because subcutaneous absorption is unpredictable in shock and protocols give more time in range with less hypoglycaemia.",
)

L['GLY-13'] = dict(
  sub="Endocrine → ICU glucose control → Leuven surgical and medical trials",
  step=4,
  intro="Step 4 starts with the two Leuven trials, the high point of tight control. Their design explains why they could not be repeated: one centre, mostly cardiac surgical patients, and early intravenous glucose in both arms. This card has not been asked.",
  parts=[
    ('a', "**Population: 1548 ventilated surgical ICU patients (2001) vs 1200 medical ICU patients without oral intake (2006).** The surgical trial was dominated by cardiac surgery, and both arms received early parenteral glucose and nutrition by local practice, so ‘conventional’ patients were often very hyperglycaemic."),
    ('b', "**Targets: 80–110 vs 180–200 mg/dL, the same in both trials.** Conventional patients received insulin only above 215."),
    ('c', "**Mortality: surgical ICU 8% → 4.6% (P < 0.04); medical, no overall difference, 52.5% → 43.0% only in stays of 3 days or more.** The medical benefit lay in a post-randomisation subgroup: length of stay is not known on admission, so the result cannot guide treatment. In short stays mortality was, if anything, higher with intensive therapy."),
    ('d', "**Other effects: surgical, less in-hospital death, sepsis, acute renal failure and transfusion; medical, less AKI, shorter ventilation and stay, but 18.7% severe hypoglycaemia.** Severe hypoglycaemia (40 or less) was about six times commoner with intensive therapy in the medical trial (18.7% vs 3.1%). Hypoglycaemia was linked with higher mortality in observational analyses, but this trial cannot show that it caused deaths."),
  ],
  mimic=[
    ("Leuven surgical vs Leuven medical", "Surgical: overall mortality fell. Medical: no overall difference; only a post-randomisation subgroup benefited."),
  ],
  traps=[
    ("“Leuven medical showed a mortality benefit”", "Only in patients who stayed 3 days or more, a subgroup defined after randomisation."),
  ],
  decode=[
    ("[pattern] Why Leuven I was not reproduced", "Single centre, mainly cardiac surgical, early parenteral glucose in both arms, a conventional arm at 180–200."),
  ],
  punch="Leuven surgical cut ICU mortality with 80–110, but in a single-centre, mainly cardiac surgical population fed early with IV glucose; Leuven medical found no overall benefit, a subgroup effect only, and 18.7% severe hypoglycaemia.",
)

L['GLY-14'] = dict(
  sub="Endocrine → ICU glucose control → VISEP",
  step=4,
  intro="Step 4 continues with the first multicentre test of tight control in sepsis. VISEP is remembered for two failures in one trial: insulin and starch. This card has not been asked.",
  parts=[
    ('a', "**A multicentre 2 × 2 factorial RCT of 537 patients with severe sepsis: intensive vs conventional insulin, and 10% starch vs modified Ringer’s lactate.** A factorial design tests two questions in one population."),
    ('b', "**Insulin arm: lower glucose but no mortality benefit; more severe hypoglycaemia and adverse events.** Severe hypoglycaemia was 17.0% vs 4.1%, and 90-day mortality 39.7% vs 35.4% (not significant)."),
    ('c', "**Starch arm: more AKI and RRT with starch.** With 10% hydroxyethyl starch (pentastarch) acute kidney injury was 34.9% vs 22.8% and renal replacement therapy 31.0% vs 18.8% compared with Ringer’s lactate; starch is taken up into tubular cells and causes osmotic-nephrosis-like injury. VISEP was the first of the trials (with 6S and CHEST) that ended the use of hydroxyethyl starch in sepsis."),
    ('d', "**Stopped early for safety.** The insulin comparison was stopped for hypoglycaemia, and the starch comparison for a trend to harm."),
  ],
  mimic=[
    ("VISEP vs GLUCONTROL", "VISEP: sepsis, stopped for safety (hypoglycaemia, starch harm). GLUCONTROL: mixed ICU, stopped for protocol violations."),
  ],
  traps=[
    ("“VISEP stopped for benefit”", "It stopped for harm: hypoglycaemia in the insulin arm, kidney injury in the starch arm."),
  ],
  decode=[
    ("[pattern] Trial that tested intensive insulin and starch in severe sepsis", "VISEP: no benefit, more hypoglycaemia, more AKI and RRT with starch."),
  ],
  punch="VISEP found that intensive insulin in severe sepsis lowered glucose without saving lives and quadrupled severe hypoglycaemia, that starch injured the kidney, and it stopped early for safety.",
)

L['GLY-15'] = dict(
  sub="Endocrine → ICU glucose control → NICE-SUGAR",
  step=4,
  intro="Step 4 reaches the trial that settled the target. NICE-SUGAR was large, multicentre and pragmatic, and its intensive arm died more often. The linked GT question uses its 2012 follow-up and only 32% got it right, because the options separate causation, association and the cause of death.",
  parts=[
    ('a', "**More than 6000 patients (6104); primary outcome 90-day mortality.** Mixed medical and surgical ICU patients in 42 centres, randomised to 81–108 or 180 or less."),
    ('b', "**Intensive control gave higher mortality, more cardiovascular deaths and more severe hypoglycaemia.** 90-day mortality 27.5% vs 24.9% (P = 0.02; about one extra death for every 38 treated); severe hypoglycaemia (40 or less) 6.8% vs 0.5%. Unlike Leuven, most patients were fed enterally, so the comparison was of glucose targets, not of glucose-loaded patients."),
    ('c', "**No difference in length of stay, duration of ventilation or RRT.** So the extra deaths were not traded for any organ benefit."),
    ('d', "**2012 post-hoc: a dose-response link between severe hypoglycaemia and death; hypoglycaemia also lengthened stay.** Moderate (41–70) hypoglycaemia affected 45% and severe (40 or less) 3.7%; adjusted hazard ratios for death were 1.41 and 2.10. The link was stronger when moderate hypoglycaemia occurred on more than one day and was strongest for death from distributive (vasodilatory) shock. It is an association: sicker patients become hypoglycaemic more often, and the analysis cannot prove cause."),
  ],
  mimic=[
    ("NICE-SUGAR vs Leuven I", "NICE-SUGAR: multicentre, mostly enteral feeding, harm with 81–108. Leuven I: single centre, early IV glucose, benefit with 80–110."),
  ],
  traps=[
    ("“Hypoglycaemia is a cause of mortality in critically ill patients”", "Many chose this (32% got the item right). The 2012 analysis shows a strong, dose-dependent association, not proof of cause, so ‘cause’ overstates it."),
    ("“ICU length of stay is not associated with hypoglycaemia”", "False: longer stays carry more hypoglycaemia."),
    ("“Well-controlled diabetes (HbA1c under 6.5%) raises hypoglycaemia risk”", "The GT key treats this as false. The recognised risk markers are diabetes itself, insulin treatment, severity of illness, septic shock, renal failure and longer stay; good prior control is not one of them."),
  ],
  decode=[
    ("T2DM, pancreatitis, vasopressors, ventilation, RRT, repeated glucose below 80 — true statement [DocT GT]", "Hypoglycaemia carries an increased risk of death from vasodilatory shock (32%)."),
    ("[pattern] Primary outcome and result of NICE-SUGAR", "90-day mortality, higher with 81–108 than with 180 or less."),
  ],
  punch="NICE-SUGAR randomised over 6000 patients and found that a target of 81–108 raised 90-day mortality and severe hypoglycaemia; its 2012 analysis tied hypoglycaemia to death in a dose-dependent way, mostly from distributive shock, as an association, not proof of cause.",
)

L['GLY-16'] = dict(
  sub="Endocrine → ICU glucose control → How the target moved to 140–180",
  step=4,
  intro="Step 4 in one line: each trial after Leuven found less benefit and more hypoglycaemia, until NICE-SUGAR found harm. This card has not been asked, but it is the summary a viva expects.",
  parts=[
    ('a', "**Leuven surgical: 80–110 looked beneficial.** Single centre, mainly cardiac surgical, with early IV glucose (GLY-13)."),
    ('b', "**Leuven medical and VISEP: no overall benefit; hypoglycaemia rose.** (GLY-13, GLY-14)."),
    ('c', "**GLUCONTROL: about 1100 patients; hypoglycaemia 8.7% vs 2.7%; stopped for protocol violations; no outcome difference.** It compared 80–110 with 140–180 and stopped early because of a high rate of unintended protocol violations, so it was underpowered; ICU mortality was 17.2% vs 15.3%, not significant."),
    ('d', "**NICE-SUGAR: intensive control increased mortality.** (GLY-15)."),
    ('e', "**Today: 140–180 mg/dL; below 110 is not recommended.** SCCM 2024 suggests against titrating to 80–139. TGC-fast (2023), the Leuven group’s own test in 9230 patients without early parenteral nutrition, found no difference in ICU stay or 90-day mortality with 80–110, and its authors suggest that the early Leuven benefit depended on the early parenteral glucose load of that era."),
  ],
  mimic=[
    ("GLUCONTROL vs NICE-SUGAR", "GLUCONTROL stopped early for protocol violations, no difference; NICE-SUGAR completed and showed harm."),
  ],
  traps=[
    ("“GLUCONTROL stopped because intensive control increased mortality”", "It stopped for protocol violations; mortality did not differ."),
  ],
  decode=[
    ("[pattern] Trial whose intensive arm increased mortality", "NICE-SUGAR."),
    ("[pattern] Trial stopped for protocol violations", "GLUCONTROL."),
  ],
  punch="Leuven surgical showed benefit, Leuven medical and VISEP none, GLUCONTROL stopped for protocol violations and NICE-SUGAR showed harm, so the target rose to 140–180; TGC-fast later showed that without early IV glucose, tight control changes nothing.",
)

L['GLY-17'] = dict(
  sub="Endocrine → Monitoring → Point-of-care glucose",
  step=5,
  intro="Step 5 asks whether the number on the meter can be trusted. Capillary meters were designed for outpatients, and the ICU combines the conditions that make them err; the linked DocT question (58%) tests the one fact that matters most, that error is greatest at low glucose.",
  parts=[
    ('a', "**Non-agreement with the reference: capillary 1.4–27.1%, arterial 0–12.3%.** Arterial blood on the same meter agrees better because it avoids poor skin perfusion and tissue-fluid dilution. A laboratory plasma sample remains the reference; whole-blood glucose reads about 11% below plasma because red cells hold less water, and most meters convert to a plasma equivalent."),
    ('b', "**Least accurate in the hypoglycaemic range.** Meter error is roughly a fixed amount (the ISO 15197 standard allows ±15 mg/dL below 100), which is a large share of a low value: a true 50 can read 65. The error therefore matters most exactly where a decision is most urgent."),
    ('c', "**Insulin, oedema and vasopressors worsen capillary error.** Vasopressors and shock reduce skin perfusion, so capillary blood stagnates and its glucose is consumed; oedema dilutes the sample with tissue fluid; insulin infusions are where low values occur. Haematocrit also matters: anaemia reads falsely high and polycythaemia falsely low on many meters."),
    ('d', "**Accuracy in hypotension: ISO accuracy 95% normotensive vs 79% hypotensive; clinical accuracy 90% vs 79.8%.** In the shocked patient one capillary reading in five may be outside the standard."),
  ],
  mimic=[
    ("Capillary vs arterial vs laboratory", "Capillary: worst in shock and oedema. Arterial on a meter: better. Laboratory plasma: the reference."),
  ],
  traps=[
    ("“Point-of-care measurements are always more accurate than the laboratory”", "The laboratory is the reference standard; meters are faster, not more accurate."),
    ("“Arterial, venous and capillary glucose are interchangeable in all contexts”", "Venous values are a little lower than arterial, and capillary values diverge in shock and oedema."),
    ("“Blood and plasma glucose are the same”", "Plasma reads about 11% higher than whole blood."),
  ],
  decode=[
    ("Most accurate statement about measuring blood glucose [DocT QBank]", "Inaccuracies are greater at lower glucose levels (58%)."),
    ("[pattern] Capillary 62 in a patient on noradrenaline", "Confirm on an arterial or laboratory sample; treat if in doubt."),
  ],
  punch="Capillary meters are least accurate at low glucose and in shock, oedema and on pressors, so in the ICU an arterial or laboratory sample confirms any low or surprising value, and the laboratory remains the reference.",
)

L['GLY-18'] = dict(
  sub="Endocrine → Monitoring → CGM and closed-loop control",
  step=5,
  intro="Step 5 ends with the technology meant to replace finger pricks. CGM reads interstitial fluid, not blood, and closed loop adds an algorithm and a pump; both are promising and both are unproven in the ICU. This card has not been asked.",
  parts=[
    ('a', "**Not truly continuous: it samples every 15 minutes; sensor drift and lag time; most devices fail accuracy standards.** Interstitial glucose lags blood glucose by about 5–15 minutes, more when glucose changes fast, and the sensor drifts until recalibrated. Current outpatient sensors report every 1–5 minutes; the 15-minute figure is from older devices, but the lag remains."),
    ('b', "**Paracetamol, dopamine and mannitol interfere; evidence is limited; AACE/ACE 2016 thought it likely useful whenever IIT is used; cost is a concern.** Interference depends on the sensor’s chemistry: drugs oxidised at the electrode read as glucose. SCCM 2024 makes no CGM recommendation and lists it as a research need."),
    ('c', "**Closed-loop components: sensor, control algorithm and IV pump.** The algorithm reads the sensor and sets the insulin rate without a nurse in the loop."),
    ('d', "**Benefits: better control without more hypoglycaemia, less variability and nursing work, more time in range; evidence limited.** Trials are small and surrogate-outcome based."),
  ],
  mimic=[
    ("CGM vs closed loop", "CGM only measures; closed loop measures and adjusts insulin automatically."),
  ],
  traps=[
    ("“CGM measures blood glucose in real time”", "It measures interstitial glucose with a lag of minutes."),
  ],
  decode=[
    ("[pattern] Limitation of CGM in the ICU", "Lag time and drift, drug interference, limited validation."),
  ],
  punch="CGM reads interstitial glucose with lag and drift and is open to drug interference, closed loop adds an algorithm and a pump to it, and both improve time in range in small studies without yet changing ICU guidance.",
)

L['GLY-19'] = dict(
  sub="Endocrine → Hypoglycaemia → Incidence, recognition and consequences",
  step=6,
  intro="Step 6 turns to the side of the J-curve that kills faster. In the ICU hypoglycaemia is common, silent in sedated patients and strongly tied to death; the linked GT question (32%) is the same NICE-SUGAR 2012 stem as GLY-15.",
  parts=[
    ('a', "**19% at below 40 and 32% at below 60 mg/dL.** These are the card’s figures; incidence depends heavily on the target: in NICE-SUGAR 6.8% of the intensive arm had severe hypoglycaemia (40 or less), against 0.5% of the conventional arm."),
    ('b', "**Easily missed: headache and confusion are not seen in sedated patients; the proof is that signs reverse with glucose.** Sedation removes symptoms, and β-blockers and neuropathy remove the adrenergic warning signs (sweating, tremor, tachycardia). The only safeguards are frequent measurement and a high index of suspicion; the definition of a hypoglycaemic event is low glucose with signs that resolve when glucose is given."),
    ('c', "**Consequences: brain damage, seizures, depression, arrhythmias; even one episode independently predicts death.** In Krinsley and Grover’s 2007 case-control study severe hypoglycaemia (below 40) carried an adjusted odds ratio for death of 2.28, and even a single episode was independently associated with mortality. Arrhythmias come from the adrenaline surge and from QT prolongation with hypokalaemia. NICE-SUGAR 2012 adds a dose-response: moderate, then severe, then repeated episodes carry rising risk, mostly of death from distributive shock (GLY-15)."),
  ],
  mimic=[
    ("Hypoglycaemia vs other causes of a reduced GCS in a sedated patient", "Only a glucose measurement separates them; a response to dextrose confirms it."),
  ],
  traps=[
    ("“Hypoglycaemia causes death in critically ill patients”", "The data show a strong association; the defensible statement is increased risk of death, especially from vasodilatory shock."),
    ("“Hypoglycaemia is unrelated to ICU length of stay”", "Longer stays carry more hypoglycaemia."),
  ],
  decode=[
    ("ICU patient with shock, RRT and repeated glucose below 80 — true statement [DocT GT]", "Increased risk of death from vasodilatory shock (32%); ‘cause of mortality’ overstates the evidence."),
    ("[pattern] Why hypoglycaemia is missed in the ICU", "Sedation masks neuroglycopenic symptoms; β-blockade masks adrenergic ones."),
  ],
  punch="ICU hypoglycaemia is common, invisible under sedation and linked to death even after a single episode, with risk rising with severity and repetition; the evidence is an association, strongest for death from distributive shock.",
)

L['GLY-20'] = dict(
  sub="Endocrine → Hypoglycaemia → Risk factors",
  step=6,
  intro="Step 6 continues with prevention: most ICU hypoglycaemia follows a change the team made without adjusting insulin. This card has not been asked.",
  parts=[
    ('a', "**Treatment-related: insulin, nutrition cut without adjusting insulin, CVVH with bicarbonate-based fluid, levofloxacin, inotropes.** The commonest story is a feed stopped for a procedure or high gastric residuals while the infusion runs on. Glucose is freely filtered and lost in the effluent; many bicarbonate-buffered replacement fluids are glucose-free and, unlike lactate-buffered fluids, give no lactate as substrate for gluconeogenesis. Fluoroquinolones stimulate insulin release from beta cells."),
    ('b', "**Patient-related: hepatic dysfunction, sepsis, diabetes, endocrine deficiency, high APACHE score.** A failing liver cannot make glucose or store glycogen; sepsis increases glucose use and impairs gluconeogenesis; adrenal or pituitary failure removes counter-regulation; kidney failure slows insulin clearance."),
  ],
  mimic=[
    ("Bicarbonate vs lactate-buffered CVVH fluid", "Bicarbonate fluid: glucose lost, no gluconeogenic substrate, more hypoglycaemia. Lactate fluid: supplies substrate."),
  ],
  traps=[
    ("“Hypoglycaemia on insulin is always an insulin dose error”", "Often the dose was right for yesterday’s feed; stopping nutrition without adjusting insulin is the leading cause."),
  ],
  decode=[
    ("[pattern] Patient on insulin infusion, feed stopped for extubation, glucose 45", "Nutrition interrupted without adjusting insulin."),
  ],
  punch="ICU hypoglycaemia usually follows insulin running on after nutrition stops, bicarbonate-based CVVH or a drug such as levofloxacin, in a patient made vulnerable by liver failure, sepsis, diabetes, endocrine deficiency or severe illness.",
)

L['GLY-21'] = dict(
  sub="Endocrine → Hypoglycaemia → Treatment",
  step=6,
  intro="Step 6 is treatment, and it is the most asked card in the deck (four questions). The rule is to choose the route by consciousness and access: oral if awake and swallowing safely, IV dextrose if not and a line is in, IM glucagon if there is no line; octreotide is added when a sulfonylurea is the cause. One DocT GT key is disputed and is explained below.",
  parts=[
    ('a', "**Marrow’s options: dextrose, steroids, diazoxide or octreotide (which cut insulin release).** Dextrose is the treatment: 15–20 g orally if the patient is awake and can swallow, or 25 g IV (50 mL of 50% or 250 mL of 10%) if not, rechecked at 15 minutes and repeated until above 70, then followed by a glucose infusion or food if the cause lasts. Steroids help only when adrenal insufficiency is the cause. Octreotide (a somatostatin analogue) and diazoxide (which opens beta-cell potassium channels) stop insulin release; octreotide is the antidote for sulfonylurea overdose, because dextrose alone stimulates more insulin release and the glucose falls again."),
    ('b', "**Unconscious with no IV access: IM glucagon 1 mg (DocT).** Glucagon releases hepatic glycogen within about 10–15 minutes. It fails when glycogen is gone: starvation, alcohol, liver failure and prolonged hypoglycaemia. It is a bridge until IV access, not a replacement for dextrose."),
    ('c', "**“Insulin shock” is the old name for insulin-induced hypoglycaemic coma.** Used historically for insulin shock therapy in psychiatry; it means coma from hypoglycaemia, not circulatory shock."),
  ],
  table=dict(title="Pick the route", head=["Stem", "Answer", "Why"], rows=[["Awake, swallow safe", "**15–20 g oral glucose**, recheck at 15 min", "fastest without a line"], ["Obtunded, IV access", "**25 g IV dextrose** (50 mL D50 or 250 mL D10)", "acts in minutes"], ["Obtunded, no IV", "**glucagon 1 mg IM/SC**", "mobilises liver glycogen"], ["Sulfonylurea, recurrent after dextrose", "**dextrose plus octreotide**", "blocks insulin release"], ["Adrenal insufficiency", "dextrose plus **hydrocortisone**", "replaces the missing counter-regulation"]]),
  mimic=[
    ("Octreotide vs repeated D50 in sulfonylurea overdose", "Repeated D50 stimulates more insulin and the glucose falls again; octreotide stops the release."),
    ("Glucagon vs dextrose", "Glucagon needs liver glycogen and is a bridge; dextrose works regardless."),
  ],
  traps=[
    ("“Oral glucose tablets (20 g)” for a confused but arousable ICU patient on insulin, glucose 48", "DocT GT keys this (15% chose it); the key is disputed. Glucose 48 is level 2, the patient is confused and in an ICU with IV access, and most ICU protocols and ADA give IV dextrose (25 g) unless the swallow is clearly safe. On exam day pick IV dextrose unless the stem states the patient can swallow safely."),
    ("“D50 bolus followed by a glucose infusion” after a glyburide overdose", "The tempting option; 53% chose something other than the key. The glucose fell back to 52 after D50 because the sulfonylurea keeps releasing insulin; octreotide is the specific treatment (key B)."),
    ("“Nasogastric glucose” or “IV saline” for an unconscious patient without IV access", "IM glucagon 1 mg is the answer (81% and 97%); a nasogastric tube in an unprotected airway is unsafe."),
  ],
  decode=[
    ("Unconscious, fingerstick 48, IV access delayed — immediate intervention [DocT QBank, DocT GT]", "1 mg IM glucagon (81%, 97%)."),
    ("Glyburide, omeprazole and sertraline overdose, glucose 33, D50 given, 52 an hour later [DocT GT]", "D50 bolus and octreotide (47%)."),
    ("ICU patient on insulin, confused but arousable, glucose 48, airway protected [DocT GT]", "Keyed oral glucose tablets (15%); IV dextrose 25 g is the safer and defensible answer."),
  ],
  punch="Choose the route by consciousness and access, oral if the patient can swallow, IV dextrose if not, IM glucagon 1 mg if there is no line, and add octreotide when a sulfonylurea keeps driving insulin release.",
)

L['GLY-22'] = dict(
  sub="Endocrine → Hypoglycaemia → Counter-regulatory physiology",
  step=6,
  intro="Step 6 ends with the body’s own defence against a falling glucose, which explains why some patients tolerate low values and others do not. Two DocT questions test it, both answered well (74% and 84%).",
  parts=[
    ('a', "**The fast counter-regulatory hormones are glucagon and adrenaline (minutes); insulin release is suppressed.** The response is ordered: insulin secretion falls first at about 80 mg/dL, glucagon and adrenaline rise at about 65–70, symptoms appear around 50–55 and cognition fails below about 50. In long-standing type 1 diabetes the glucagon response is lost and the adrenaline response blunted, so the response is not uniform across patients."),
    ('b', "**Cortisol is slow and sustained, not the acute defence.** Cortisol and growth hormone act over hours by increasing gluconeogenesis and insulin resistance; they matter in prolonged hypoglycaemia and explain hypoglycaemia in adrenal or pituitary failure."),
    ('c', "**Prolonged starvation rarely causes symptoms because after about 72 hours the brain runs on ketones; glycogen is gone within a day.** As insulin falls, the liver makes ketone bodies from fatty acids, and the brain takes up β-hydroxybutyrate in proportion to its concentration, so its glucose need falls and muscle protein is spared."),
  ],
  mimic=[
    ("Glucagon and adrenaline vs cortisol and growth hormone", "Glucagon and adrenaline: minutes. Cortisol and growth hormone: hours."),
  ],
  traps=[
    ("“Cortisol’s role is immediate, preventing acute hypoglycaemia”", "Cortisol acts over hours."),
    ("“Insulin is the primary counter-regulatory hormone”", "The first defence is a fall in insulin, which is not counter-regulation by insulin."),
    ("“The counter-regulatory response is consistent in all individuals”", "It is blunted in long-standing diabetes and after repeated hypoglycaemia (hypoglycaemia unawareness)."),
    ("“Increased hepatic glycogen stores protect in prolonged starvation”", "Glycogen is exhausted within a day; ketone use by the brain is the adaptation."),
  ],
  decode=[
    ("Most accurate statement about the counter-regulatory response to hypoglycaemia [DocT QBank]", "Glucagon and adrenaline are the key hormones (84%)."),
    ("Prolonged starvation (72 h or more), why symptomatic hypoglycaemia is uncommon [DocT QBank]", "The brain adapts to use ketone bodies (74%)."),
  ],
  punch="Falling glucose first switches off insulin and then calls on glucagon and adrenaline within minutes, with cortisol and growth hormone acting over hours; in prolonged starvation the brain switches to ketones, which is why glucose falls without symptoms.",
)

FLAGS = {}
FLAGS['GLY-01'] = "Card a gives hyperglycaemia as >180–200; ADA defines inpatient hyperglycaemia as >140 mg/dL (the HbA1c trigger), and 180 is the threshold to start insulin (ADA, SCCM 2024). Card d says <110 is not recommended; SCCM 2024 suggests against titrating to 80–139 (vs 140–200), so the floor is 140. ADA still allows 110–140 for selected patients. DocT’s ‘renal threshold’ explanation for the target is not the reason."
FLAGS['GLY-06'] = "Card routes IL-6 only to the anterior pituitary. IL-6 also stimulates the adrenal cortex directly (ACTH-independent cortisol; DocT key and card-layer line); TNF-α blunts the adrenal response to ACTH. Explanation adds this."
FLAGS['GLY-11'] = "Card a ‘check HbA1c when >180’: ADA asks for HbA1c in all patients with diabetes or glucose >140 if none in the previous 3 months. Card c is right that no guideline uses HbA1c tiers; LUCID (2022) and CONTROLING (2021, stopped early for low likelihood of benefit and possible harm) did not show benefit from liberal or individualised targets."
FLAGS['GLY-12'] = "Card b ‘then 4-hourly once stable’: while an IV insulin infusion runs, ADA calls checks every 30 min to 2 h the required standard (SCCM 2024: ≤1-hourly during instability). 4-hourly fits a stable patient on SC insulin or off the infusion."
FLAGS['GLY-18'] = "Card a ‘samples every 15 min’ reflects older devices; current sensors report every 1–5 min. The real limitation is the 5–15 min interstitial lag and drift. SCCM 2024 makes no CGM recommendation (research need); the AACE/ACE 2016 statement on the card was not re-verified."
FLAGS['GLY-21'] = "DocT GT (GrandT1) keys oral glucose tablets for a confused but arousable ICU patient on insulin with glucose 48 (15% chose it). Disputed: level 2 hypoglycaemia with altered sensorium and IV access → IV dextrose 25 g is the safer answer; pick oral only if the stem makes a safe swallow explicit (the card-layer cross line says the same). Card a ‘steroids’ applies only to adrenal insufficiency."
