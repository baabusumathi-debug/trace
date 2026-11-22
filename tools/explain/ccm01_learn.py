# CCM01 — Explain v3 ("Learn" depth): glucose control in critical care, the original 38-card deck — definitions (hyper-, hypoglycaemia, variability, TITR), admission
# epidemiology, the old and current view of stress hyperglycaemia, the J-curve, the biology of stress hyperglycaemia (HPA and sympathoadrenal axes, cytokines, hepatic output,
# counter-regulatory hormones, ICU and patient causes), the organ harms of hyperglycaemia, HbA1c, insulin delivery and protocols, and the Leuven Surgical, Leuven Medical and VISEP trials.
# No mnemonics or hooks. Driven by qpack/CCM01.md (only 5 question links: GLU-02 two, GLU-14, GLU-16 and GLU-27 one each). All other cards have no linked question and get a short
# explanation with [pattern] decode items.
# No `fix` entries exist for CCM01 in trace/test/data/qbank.json (checked 22 Nov 2026). endo_cardlayer.json lines/cross for GLU-02 and chips for GLU-16 were read and used; the
# DocT explanation line in the qpack for GLU-14 (IL-6 acts directly on the adrenal cortex) is taught. No Top-up cards for CCM01 in endo_topups.json.
# Checked online on 22 Nov 2026:
#  - SCCM 2024 glycaemic control guideline (Honarmand, Crit Care Med 2024; SCCM guideline page and HealthManagement summary): good practice statement to start a glycaemic management
#    protocol for persistent BG ≥180 mg/dL (10 mmol/L); suggests against an intensive target 80–139 mg/dL vs conventional 140–200 mg/dL (conditional, moderate certainty); suggests IV
#    infusion over intermittent SC insulin for acute hyperglycaemia (conditional, very low); suggests explicit decision-support tools for IV insulin titration (conditional, moderate);
#    individualised (HbA1c-based) targets left as a research question; 2012 guideline had started at ≥150 mg/dL. SCCM page summary also: glucose checks at least hourly during instability.
#  - ADA Standards of Care, hospital chapter (MDCalc summary): hospital hyperglycaemia >140 mg/dL; HbA1c if none in the prior 3 months; insulin for persistent BG ≥180 mg/dL; target 140–180
#    for most critically ill and non-critically ill patients; basal or basal-plus-correction (poor intake), basal-bolus-correction (good intake) in non-critically ill.
#  - Leuven Surgical (Van den Berghe, NEJM 2001; abstract via QxMD): 1,548 ventilated surgical ICU adults; 80–110 vs insulin only above 215, kept 180–200; ICU mortality 8.0% vs 4.6%
#    (P<0.04 adjusted for sequential analyses); ICU stay >5 days 20.2% vs 10.6%; in-hospital mortality −34%, bloodstream infections −46%, ARF needing dialysis/haemofiltration −41%,
#    red-cell transfusions −50%, critical illness polyneuropathy −44%.
#  - Leuven Medical (Van den Berghe, NEJM 2006; abstract via BVS): 1,200 medical ICU adults; same targets; ITT in-hospital mortality 40.0% vs 37.3% (P=0.33) but morbidity reduced in
#    ALL patients (new kidney injury, earlier weaning, earlier ICU and hospital discharge); stay <3 days (n 433) more deaths with IIT; stay ≥3 days (n 767) 52.5% vs 43.0% (P=0.009).
#  - VISEP (Brunkhorst, NEJM 2008; full text, Leipzig PDF): 18 German ICUs, 537 severe sepsis/septic shock, 2×2 factorial; co-primary 28-day mortality and mean SOFA; insulin arm stopped
#    after the first safety analysis (488 patients) for hypoglycaemia; hypoglycaemia ≤40 mg/dL 17.0% vs 4.1%, serious adverse events 10.9% vs 5.2%; 28-day mortality 24.7% vs 26.0% (NS);
#    10% HES 200/0.5 vs modified Ringer’s lactate: ARF 34.9% vs 22.8%, RRT 31.0% vs 18.8%, 90-day mortality 41.0% vs 33.9% (P=0.09); whole study suspended at the planned interim analysis.
#  - CONTROLING (Bohé, Intensive Care Med 2021; Bottom Line summary): n 2,075; individualised target (HbA1c-derived average glucose) vs <180; 90-day survival 67.2% vs 69.6% (P=0.23);
#    any hypoglycaemia <72 mg/dL 31.2% vs 15.8%; stopped at 49% of planned sample (benefit unlikely, possible harm).
# Second-check review (22 Nov 2026), verified online: Leuven Surgical full text (NEJM 2001; Cornell-hosted PDF): hypoglycaemia ≤40 mg/dL in 39/765 vs 6/783 (5.1% vs 0.8%);
#    admission glucose >110 mg/dL in 75% and >200 mg/dL in 12% (the source of GLU-05); IV glucose 200–300 g/24 h from admission, then parenteral, mixed or enteral feeding;
#    cardiac surgery 63%. Leuven Medical (Healio report of NEJM 2006): patients able to take oral nutrition were excluded (GLU-34 is right). Krinsley and Preiser (Crit Care
#    2015;19:179): single centre, 3,297 adults; non-diabetics with time in range 70–140 above the median (~80%) had mortality 8.5% vs 15.7%, independent after adjustment; no
#    association in diabetics. Krinsley 2013 (Crit Care 17:R37; 44,964 patients, 23 ICUs): CV >20% independently linked to death only in non-diabetics. ADA hospital chapter
#    (2018 text, dc18-S014): glucose checks every 30 min to 2 h on IV insulin; alert value ≤70, clinically significant <54, severe = cognitive impairment. Endotext (Oct 2024):
#    ADA level 1 54–70, level 2 <54, level 3 needs third-party help. NICE-SUGAR (ACC summary): 6,104; 81–108 vs <180; 90-day 27.5% vs 24.9% (P=0.02); severe hypoglycaemia
#    6.8% vs 0.5%. LUCID (Am J Respir Crit Care Med 2022; Flinders abstract): 419 type 2 diabetics, liberal 180–252 (insulin >252) vs 108–180; hypoglycaemia <72 in 5% vs 18%
#    (IRR 0.21); 90-day mortality 29.5% vs 24.9% (P=0.29).
# From standard references without a fresh check (confident unless said): ADA hypoglycaemia levels (level 1 <70 and ≥54, level 2 <54, level 3 severe event with altered mental or physical
# status needing help); ADA outpatient CGM coefficient of variation target ≤36%; ADA advice to check glucose every 30 min to 2 h on IV insulin (less sure of the exact wording);
# NICE-SUGAR 2009 (n 6,104; 81–108 vs ≤180; 90-day mortality 27.5% vs 24.9%, OR 1.14, P=0.02; severe hypoglycaemia 6.8% vs 0.5%) and its 2012 hypoglycaemia analysis (moderate and severe
# hypoglycaemia linked to death); TGC-fast 2023 (tight 80–110 vs liberal without early parenteral nutrition: no difference in ICU stay or mortality); Leuven Medical hypoglycaemia 18.7% vs 3.1%
# (card figure); Leuven Surgical hypoglycaemia ≈5.1% vs 0.8%; Krinsley’s time-in-range (70–140 mg/dL >80% of time) survival association in non-diabetics; Egi 2008 and Krinsley 2013 (the
# glucose–mortality association is weaker in diabetes); Lanspa/Krinsley glucose CV and mortality; Marik and Bellomo 2013 (stress hyperglycaemia as a survival response: GLUT1/GLUT3,
# macrophage fuel, anti-apoptosis, angiogenesis); IL-6 stimulates adrenal cortisol directly; stress hyperglycaemia ratio = admission glucose ÷ (28.7 × HbA1c − 46.7). The GLU-05
# figures, the Leuven Medical oral-nutrition exclusion and LUCID were settled in the second check (above). Still from memory: Leuven Medical control-arm hypoglycaemia 3.1%; NICE-SUGAR
# conventional-arm insulin rule (start above 180, reduce and stop below 144).

SPINE = [
  ("Defining dysglycaemia and its measures", "Hyperglycaemia, hypoglycaemia, glycaemic variability and time in range are the four ways an ICU describes glucose control, and each is independently linked to death."),
  ("Glucose and mortality: the J-curve", "Mortality is lowest at normal glucose, rises steeply with hypoglycaemia and more gently with hyperglycaemia, and the hyperglycaemic limb is flattened in people with diabetes."),
  ("Why stress raises glucose", "Cytokines, the HPA axis and the sympathoadrenal system raise counter-regulatory hormones, which drive hepatic glucose output and insulin resistance to feed immune cells and the brain."),
  ("How high glucose harms", "Above about 180–200 mg/dL glucose impairs neutrophils, clotting, endothelium, muscle protein, the kidney and the heart, which is why it is treated."),
  ("Targets, HbA1c and insulin delivery", "Start IV insulin at persistent glucose ≥180 mg/dL, aim for 140–180, use a protocol, check hourly until stable and use HbA1c to tell stress hyperglycaemia from diabetes."),
  ("Trials that set the target", "Leuven showed benefit from 80–110 mg/dL in one surgical centre; Leuven Medical, VISEP and then NICE-SUGAR showed hypoglycaemia and no benefit, or harm, so the target moved to 140–180."),
]

PRIMER = "Normal fasting glucose is about 70–100 mg/dL (to convert mg/dL to mmol/L, divide by 18; 180 mg/dL is 10 mmol/L). Insulin is the only hormone that lowers glucose; glucagon, catecholamines, cortisol and growth hormone all raise it, and all of them rise in critical illness. In the ICU glucose is measured at the bedside, and capillary samples are least reliable in shock, so arterial or venous samples on a blood gas analyser are preferred. The present target (140–180 mg/dL) comes from NICE-SUGAR (2009), which found that tighter control increased deaths; this deck builds up to that answer."

L = {}

# ---------- Step 1: definitions and epidemiology ----------

L['GLU-01'] = dict(
  sub="Glucose control → Definitions → Hyperglycaemia",
  step=1,
  intro="Step 1 starts with the threshold that triggers treatment. In the ICU the definition that matters is the level at which insulin is started, which is higher than the ward definition.",
  parts=[
    ('a', "**CBG over 180–200 mg/dL.** This is the action threshold: SCCM 2024 and the ADA start insulin for persistent glucose ≥180 mg/dL (10 mmol/L). It is also about where glucose spills into the urine and where neutrophil function starts to fail (GLU-20, GLU-23). The ADA defines hospital hyperglycaemia more loosely as any glucose over 140 mg/dL; that number marks who needs watching, not who needs insulin."),
  ],
  mimic=[
    ("Hospital hyperglycaemia (>140) vs ICU treatment threshold (≥180)", "Over 140 mg/dL defines hyperglycaemia in hospital (ADA); persistent ≥180 mg/dL is when insulin is started."),
  ],
  traps=[
    ("“Start insulin above 140 mg/dL in the ICU”", "140 is the ADA definition of hospital hyperglycaemia and the bottom of the target range; insulin starts at persistent ≥180."),
  ],
  decode=[
    ("At what glucose should an insulin infusion be started in a critically ill adult? [pattern]", "Persistent ≥180 mg/dL (10 mmol/L), SCCM 2024 and ADA."),
  ],
  punch="In the ICU, hyperglycaemia that needs treatment starts at about 180 mg/dL; 140 is the ward definition and the floor of the target, not the trigger.",
)

L['GLU-02'] = dict(
  sub="Glucose control → Definitions → Hypoglycaemia",
  step=1,
  intro="Step 1 also defines the other end of the J-curve, which carries the steeper risk. Two real questions test it: one asks what to do when glucose falls to 65 mg/dL on an insulin drip, the other what ‘insulin shock’ means.",
  parts=[
    ('a', "**CBG under 70 mg/dL is level 1.** This is the ADA alert value: the point at which glucose is low enough to act on, even if the patient feels nothing. On an insulin infusion it means the infusion has overshot, so it is stopped, not just slowed. Some ICU texts still quote under 60 mg/dL; when the ADA levels appear in the options, 70 is the answer."),
    ('b', "**Under 54 mg/dL is clinically significant (level 2).** Below about 54 mg/dL neuroglycopenia begins and the counter-regulatory response becomes blunted with repeated episodes. In the sedated ventilated patient no symptoms warn of this, so the number is the only signal. NICE-SUGAR’s follow-up analysis linked both moderate (41–70) and severe (≤40 mg/dL) hypoglycaemia to death."),
    ('c', "**Level 3 is a severe event needing help, with no number attached.** It is defined by the patient’s state (altered mental or physical status that needs another person to treat it), not by a glucose level. ‘Insulin shock’ is the old name for this: severe hypoglycaemia from too much insulin, with sweating, confusion, seizures or coma."),
  ],
  mimic=[
    ("Insulin shock vs diabetic coma", "Insulin shock is hypoglycaemia from insulin excess; diabetic coma is hyperglycaemia (DKA or HHS) from insulin lack."),
  ],
  traps=[
    ("“Glucose 65 on an insulin drip: halve the rate and recheck in an hour”", "Below 70 the infusion is stopped and IV dextrose given (D50 25 g, or D10), with a recheck every 15 minutes and the carrier line flushed, because it can still hold insulin."),
    ("“Hypoglycaemia in the ICU starts below 54”", "Below 54 is level 2 (clinically significant); level 1, the alert value, starts below 70."),
  ],
  decode=[
    ("Intra-operative insulin infusion, glucose falls 180 → 65 mg/dL: next step? [Marrow]", "Stop the insulin infusion and give D50; recheck every 15 minutes."),
    ("What is insulin shock? [NEET 2024]", "Severe hypoglycaemia caused by insulin excess."),
    ("ADA level 2 hypoglycaemia is glucose below? [pattern]", "54 mg/dL (3.0 mmol/L)."),
  ],
  punch="Level 1 is under 70, level 2 under 54, level 3 is defined by the patient needing help. On an insulin drip, any value under 70 means stop the infusion and give dextrose.",
)

L['GLU-03'] = dict(
  sub="Glucose control → Definitions → Glycaemic variability",
  step=1,
  intro="Step 1’s third measure is how much glucose swings, which predicts death even when the average is good. It is never asked directly; it is asked as the index that measures it.",
  parts=[
    ('a', "**Coefficient of variation (CoV).** CoV is the standard deviation divided by the mean, so it measures swing independent of the average level: a patient averaging 150 with wide swings and one averaging 150 who is steady have different risks. Fluctuating glucose causes oxidative stress and endothelial damage more than steady hyperglycaemia does."),
    ('b', "**CoV over 20%.** In Krinsley’s 2013 multicentre cohort (about 45,000 patients, 23 ICUs), a CoV above 20% was independently linked to higher mortality, but only in patients without diabetes; in diabetics variability carried no independent risk, the same pattern as the flattened J-curve (GLU-07). The outpatient CGM target (ADA) is different: CV ≤36%."),
  ],
  mimic=[
    ("ICU CoV >20% vs outpatient CGM CV ≤36%", "The ICU number is a mortality-risk cut-off; 36% is the outpatient CGM stability target."),
  ],
  traps=[
    ("“Variability is measured by HbA1c”", "HbA1c reflects the average over about three months and says nothing about hour-to-hour swings."),
  ],
  decode=[
    ("Which index quantifies glycaemic variability in the ICU, and what value is high? [pattern]", "Coefficient of variation; above 20%."),
  ],
  punch="Glycaemic variability is the CoV (SD ÷ mean); above 20% predicts death in non-diabetic ICU patients whatever the average glucose.",
)

L['GLU-04'] = dict(
  sub="Glucose control → Definitions → TITR",
  step=1,
  intro="Step 1 ends with the measure that joins the other three: how long the patient actually spends in range. It is a [pattern] card, never asked directly.",
  parts=[
    ('a', "**Time In Target Range.** It is the proportion of measured time that glucose sits inside the chosen band. A single high or low reading tells little; TITR captures the whole course."),
    ('b', "**Percentage of time spent in normoglycaemia.** In Krinsley and Preiser’s single-centre cohort (2015, 3,297 patients), non-diabetics with more than about 80% of time at 70–140 mg/dL had a mortality of 8.5% against 15.7% for those below it, independent of severity and length of stay; in diabetics time in range showed no such link. It is an association, not a tested target, and it is also the main quality measure of an insulin protocol (GLU-29)."),
  ],
  mimic=[],
  traps=[
    ("“A good mean glucose means good control”", "A good mean can hide hypoglycaemia and wide swings; time in range and variability show them."),
  ],
  decode=[
    ("TITR stands for? [pattern]", "Time In Target Range, the percentage of time spent in the target (normoglycaemic) band."),
  ],
  punch="TITR is the percentage of time glucose stays in range; more than 80% of the time at 70–140 mg/dL is linked to survival in non-diabetic ICU patients, not in diabetics.",
)

L['GLU-05'] = dict(
  sub="Glucose control → Epidemiology → Admission glucose",
  step=1,
  intro="Step 1 needs a sense of scale: abnormal glucose is the rule at ICU admission, not the exception. The figures come from the admission data of the Leuven Surgical trial (2001, 1,548 ventilated surgical patients). Never asked; a [pattern] figure.",
  parts=[
    ('a', "**Over 110 mg/dL in 75% (three-quarters).** 110 mg/dL is the upper limit of normal fasting glucose, so three in four ventilated patients arrived above it, mostly from stress (step 3), not from known diabetes."),
    ('b', "**Over 200 mg/dL in 12% (about one in eight).** 200 mg/dL is the non-fasting diabetic range, where glucose is high enough to cause harm (step 4). These are one surgical cohort’s numbers; medical and septic populations differ, but in every series admission hyperglycaemia is the rule."),
  ],
  mimic=[],
  traps=[
    ("“Most ICU hyperglycaemia is undiagnosed or known diabetes”", "Most is stress hyperglycaemia; HbA1c separates the two (GLU-25)."),
  ],
  decode=[
    ("What proportion of ICU patients have admission glucose above 110 mg/dL? [pattern]", "About three-quarters (75%); above 200 mg/dL about 12%."),
  ],
  punch="Three-quarters of ICU admissions are above 110 mg/dL and about one in eight above 200, so every patient needs glucose checked.",
)

# ---------- Step 2: concepts and the J-curve ----------

L['GLU-06'] = dict(
  sub="Glucose control → Concepts → Old vs current view",
  step=2,
  intro="Step 2 begins with how the view of a high glucose changed. Never asked; a [pattern] concept card that frames everything after it.",
  parts=[
    ('a', "**Old view: an adaptive response, not routinely corrected.** A high glucose was taken as the body’s way of fuelling vital tissues in stress, and it was left alone unless very high. The reasoning was sound (GLU-09, GLU-10), which is why the card says it ‘had a rationality’."),
    ('b', "**Current view: a marker of severe illness; dysglycaemia means higher mortality.** Hyperglycaemia, hypoglycaemia and variability are each linked to death. The trials (step 6) then showed that pushing glucose to normal is not the answer either: the aim is moderate control, 140–180 mg/dL."),
  ],
  mimic=[],
  traps=[
    ("“The current view is that all stress hyperglycaemia should be normalised”", "Normalising (80–110) increased deaths in NICE-SUGAR; the current aim is to prevent harmful highs and any lows."),
  ],
  decode=[
    ("Stress hyperglycaemia is now regarded as? [pattern]", "A marker of illness severity linked to mortality, treated when persistently ≥180 mg/dL."),
  ],
  punch="Stress hyperglycaemia was once left alone as adaptive; it is now treated as a marker of severity, but only to moderate targets.",
)

L['GLU-07'] = dict(
  sub="Glucose control → J-curve → Shape and who it spares",
  step=2,
  intro="Step 2’s core picture is the J-curve, and the point most often tested is who it differs for. Never asked directly; a [pattern] card.",
  parts=[
    ('a', "**J-shaped association.** Plotting mortality against mean glucose gives a short steep left limb (hypoglycaemia), a trough near normal and a longer, gentler right limb (hyperglycaemia)."),
    ('b', "**Significantly flattened in established diabetes.** People with long-standing hyperglycaemia have adapted: their cells have down-regulated glucose transporters and their tissues are used to high levels, so the same glucose does them less harm (Egi 2008, Krinsley 2013). They also gained no benefit from tight control in the Leuven trials."),
    ('c', "**Almost linear relationship in patients without diabetes.** In a non-diabetic, every step up in glucose carries more risk, because the tissues have no adaptation. This is why stress hyperglycaemia without diabetes is the more ominous finding."),
  ],
  mimic=[
    ("Same glucose in a diabetic vs non-diabetic", "220 mg/dL in a diabetic is often the patient’s usual level; in a non-diabetic it marks severe stress and higher mortality."),
  ],
  traps=[
    ("“Diabetics are at the highest risk from ICU hyperglycaemia”", "The hyperglycaemia–mortality link is weaker in diabetes; the steepest rise is in patients without diabetes."),
  ],
  decode=[
    ("In which patients is the glucose–mortality relationship flattened? [pattern]", "Established diabetes mellitus."),
  ],
  punch="The glucose–mortality curve is a J: almost linear in non-diabetics, flattened in established diabetes, whose tissues are used to high glucose.",
)

L['GLU-08'] = dict(
  sub="Glucose control → J-curve → Steeper limb",
  step=2,
  intro="Step 2 finishes with which end of the J is worse, and this is the reason the targets were relaxed. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Hypoglycaemia gives an even steeper rise in mortality.** The brain has almost no glucose reserve, and in a sedated patient hypoglycaemia goes unnoticed until harm is done. A single severe episode is independently linked to death. Every tight-control trial (Leuven Medical, VISEP, NICE-SUGAR) raised hypoglycaemia several-fold."),
    ('b', "**Normoglycaemia carries the lowest risk of dying.** The trough of the curve is near normal glucose, but that is an association: patients who are normoglycaemic on their own do best, whereas forcing glucose to normal with insulin did not reproduce that benefit."),
  ],
  mimic=[
    ("Spontaneous vs insulin-induced normoglycaemia", "Normal glucose without insulin marks a less sick patient; insulin-driven normoglycaemia brings hypoglycaemia and no survival gain."),
  ],
  traps=[
    ("“Because normoglycaemia has the lowest risk, target 80–110”", "That was tested; NICE-SUGAR found more deaths (27.5% vs 24.9%) with 81–108 mg/dL."),
  ],
  decode=[
    ("Which limb of the J-curve is steeper? [pattern]", "The hypoglycaemic limb."),
  ],
  punch="Hypoglycaemia is the steeper limb; normal glucose is lowest-risk only when the patient gets there alone, which is why the target is 140–180 and not normal.",
)

# ---------- Step 3: stress hyperglycaemia ----------

L['GLU-09'] = dict(
  sub="Glucose control → Stress hyperglycaemia → Definition and purpose",
  step=3,
  intro="Step 3 explains why stress raises glucose at all. Never asked; a [pattern] definition.",
  parts=[
    ('a', "**A relative increase in blood glucose during acute illness.** ‘Relative’ is the key word: it is a rise above the patient’s own baseline. That baseline is estimated from HbA1c, and the stress hyperglycaemia ratio (admission glucose ÷ HbA1c-derived average glucose) measures it (GLU-25)."),
    ('b', "**An evolutionary response to promote survival.** In stress, the tissues that matter most for survival (brain, blood cells, immune cells, wound) take up glucose through insulin-independent transporters (GLUT1, GLUT3), which depend on the concentration gradient. A higher blood glucose pushes more fuel into them while insulin-dependent muscle and fat are held back."),
  ],
  mimic=[],
  traps=[
    ("“Stress hyperglycaemia means glucose above a fixed number in a non-diabetic”", "It is a rise relative to the patient’s baseline, so it can occur in a diabetic too."),
  ],
  decode=[
    ("What is the purpose of stress hyperglycaemia? [pattern]", "An adaptive (evolutionary) response that supplies glucose to insulin-independent vital tissues."),
  ],
  punch="Stress hyperglycaemia is a rise above the patient’s own baseline that drives glucose into insulin-independent tissues such as brain and immune cells.",
)

L['GLU-10'] = dict(
  sub="Glucose control → Stress hyperglycaemia → Protective effects",
  step=3,
  intro="Step 3 continues with what acute hyperglycaemia actually achieves, from Marik and Bellomo’s argument that it is a survival response. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Glucose is the main fuel of the macrophage.** Activated macrophages and neutrophils run on glycolysis, taking up glucose through GLUT1 without insulin, so more glucose supports the immune response."),
    ('b', "**Acute hyperglycaemia is anti-apoptotic.** In ischaemic tissue, raised glucose limits cell death; in experimental ischaemia, myocardium survives better with more glucose available."),
    ('c', "**Acute hyperglycaemia promotes angiogenesis.** Higher glucose supports new vessel growth in hypoxic, healing tissue. All three benefits are of moderate, short-lived hyperglycaemia; sustained high glucose turns harmful (step 4)."),
  ],
  mimic=[],
  traps=[
    ("“Hyperglycaemia is protective at any level”", "The benefit is of moderate acute rises; above about 180–200 mg/dL, immune and endothelial function deteriorate (GLU-19)."),
  ],
  decode=[
    ("Which cell uses glucose as its primary metabolic substrate in stress? [pattern]", "The macrophage."),
  ],
  punch="Moderate acute hyperglycaemia fuels macrophages, limits apoptosis and supports angiogenesis; it is the sustained, higher level that harms.",
)

L['GLU-11'] = dict(
  sub="Glucose control → Stress hyperglycaemia → Mediating systems",
  step=3,
  intro="Step 3’s machinery has two arms, one slow and one fast. Never asked; a [pattern] card.",
  parts=[
    ('a', "**HPA axis.** CRH, ACTH and cortisol (GLU-15). Cortisol raises glucose over hours by driving gluconeogenesis and causing insulin resistance."),
    ('b', "**Sympathoadrenal system.** Adrenaline and noradrenaline act within minutes: they stimulate glycogenolysis and gluconeogenesis, release glucagon and, through α2 receptors on β-cells, suppress insulin secretion. That suppression is the ‘relative insulin deficiency’ of GLU-18."),
  ],
  mimic=[],
  traps=[
    ("“Stress hyperglycaemia is driven mainly by excess glucagon”", "Glucagon contributes, but the two driving systems are the HPA axis and the sympathoadrenal system, triggered by cytokines."),
  ],
  decode=[
    ("Stress hyperglycaemia is mediated by which two systems? [pattern]", "The HPA axis and the sympathoadrenal system."),
  ],
  punch="Stress hyperglycaemia runs on two systems: the fast sympathoadrenal one (catecholamines, which also suppress insulin) and the slower HPA axis (cortisol).",
)

L['GLU-12'] = dict(
  sub="Glucose control → Stress hyperglycaemia → Cytokines",
  step=3,
  intro="Step 3 starts at the inflammation that switches both systems on. Never asked; a [pattern] card.",
  parts=[
    ('a', "**IL-6 and TNF-α, with IL-1 also taking part.** They do two things. They activate the HPA axis (GLU-14). And they cause insulin resistance directly: TNF-α makes the cell phosphorylate insulin receptor substrate-1 (IRS-1) at serine sites, which blocks insulin signalling in muscle and liver. So inflammation raises glucose both through hormones and at the insulin receptor itself."),
  ],
  mimic=[],
  traps=[
    ("“Anti-inflammatory cytokines (IL-10) drive stress hyperglycaemia”", "The drivers are the pro-inflammatory IL-1, IL-6 and TNF-α."),
  ],
  decode=[
    ("Which pro-inflammatory cytokines drive stress hyperglycaemia? [pattern]", "IL-6 and TNF-α (with IL-1)."),
  ],
  punch="IL-1, IL-6 and TNF-α drive stress hyperglycaemia both by switching on the HPA axis and by blocking insulin signalling directly.",
)

L['GLU-13'] = dict(
  sub="Glucose control → Stress hyperglycaemia → Primary metabolic response",
  step=3,
  intro="Step 3 converges on one organ: the liver is where the extra glucose comes from. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Increased hepatic glucose output is the primary response.** In health, insulin switches hepatic glucose output off after a meal or a glucose load. In stress it does not: the liver keeps releasing glucose even while the patient is being fed dextrose or nutrition, because counter-regulatory hormones override insulin."),
    ('b', "**Also increased gluconeogenesis, increased glycogenolysis and increased insulin resistance.** Glycogenolysis supplies glucose in the first hours, but liver glycogen runs out within a day or so; after that, gluconeogenesis from lactate, alanine (from muscle breakdown, GLU-22) and glycerol is the main source. Peripheral insulin resistance then stops muscle and fat taking the glucose up."),
  ],
  mimic=[],
  traps=[
    ("“The primary problem is reduced peripheral glucose uptake”", "Peripheral resistance contributes, but the primary response is increased hepatic output, mostly gluconeogenesis."),
  ],
  decode=[
    ("What is the primary metabolic response in stress hyperglycaemia? [pattern]", "Increased hepatic glucose output."),
  ],
  punch="The extra glucose of stress comes mainly from the liver, which keeps making it by gluconeogenesis even when insulin and feeding should stop it.",
)

L['GLU-14'] = dict(
  sub="Glucose control → Stress hyperglycaemia → Cytokine targets",
  step=3,
  intro="Step 3 places each cytokine on a level of the HPA axis. One real question tests the level the card leaves out: IL-6 also acts directly on the adrenal cortex, and a third of the cohort missed it.",
  parts=[
    ('a', "**IL-1 and TNF act on the hypothalamus (paraventricular nucleus).** They stimulate CRH release, which starts the cascade (GLU-15)."),
    ('b', "**IL-6 acts on the anterior pituitary.** It stimulates ACTH. It also acts beyond the pituitary: the adrenal cortex has IL-6 receptors, and IL-6 releases cortisol directly, without ACTH. This helps explain why in prolonged critical illness cortisol stays high while ACTH is low. TNF-α, by contrast, blunts the adrenal response to ACTH."),
    ('c', "**Cortisol feeds back negatively on both the hypothalamus and the pituitary.** The feedback keeps working in critical illness, which is why ACTH falls after the first days; cortisol stays high anyway because the cytokines drive the adrenal directly and because cortisol breakdown in the liver and kidney slows."),
  ],
  mimic=[
    ("IL-6 vs IL-1/TNF-α", "IL-6 acts on the pituitary and directly on the adrenal cortex; IL-1 and TNF-α act mainly on the hypothalamus, and TNF-α blunts the adrenal response."),
  ],
  traps=[
    ("“IL-1 directly releases cortisol from the adrenal”", "IL-1 acts mainly on the hypothalamus; the cytokine that acts directly on the adrenal cortex is IL-6."),
    ("“TNF-α drives adrenal cortisol release”", "TNF-α actually blunts the adrenal response to ACTH."),
  ],
  decode=[
    ("Which cytokine directly induces cortisol release from the adrenal cortex? [DocT QBank, 67% right]", "IL-6."),
    ("Which cytokines act on the hypothalamic paraventricular nucleus? [pattern]", "IL-1 and TNF-α."),
  ],
  punch="IL-1 and TNF-α act on the hypothalamus, IL-6 on the pituitary and directly on the adrenal cortex, which is how cortisol stays high while ACTH is low.",
)

L['GLU-15'] = dict(
  sub="Glucose control → Stress hyperglycaemia → HPA cascade",
  step=3,
  intro="Step 3’s slower arm, traced from top to bottom. Never asked as a whole; a [pattern] card.",
  parts=[
    ('a', "**Top: paraventricular nucleus → CRH.** Stimulated by IL-1, TNF-α and pain."),
    ('b', "**Middle: anterior pituitary → ACTH.** CRH, with vasopressin, releases ACTH; IL-6 adds to it (GLU-14)."),
    ('c', "**Bottom: adrenal cortex → cortisol.** Zona fasciculata releases cortisol."),
    ('d', "**Cortisol → liver → raised glucose.** Cortisol switches on the genes for gluconeogenic enzymes (such as PEPCK), supplies substrate by breaking down muscle protein, and causes insulin resistance in muscle and fat. This is why corticosteroids given in the ICU raise glucose (GLU-17)."),
  ],
  mimic=[],
  traps=[
    ("“Cortisol raises glucose mainly by glycogenolysis”", "Cortisol’s main effect is gluconeogenesis and insulin resistance; glycogenolysis is the catecholamine and glucagon effect."),
  ],
  decode=[
    ("Trace the HPA axis from hypothalamus to glucose. [pattern]", "PVN → CRH → anterior pituitary → ACTH → adrenal cortex → cortisol → hepatic gluconeogenesis."),
  ],
  punch="CRH from the PVN, ACTH from the pituitary, cortisol from the adrenal cortex: cortisol raises glucose by gluconeogenesis and insulin resistance.",
)

L['GLU-16'] = dict(
  sub="Glucose control → Stress hyperglycaemia → Counter-regulatory hormones",
  step=3,
  intro="Step 3 names the hormones that oppose insulin. One real Grand Test asked which of them contributes to DKA and HHS, and half the cohort missed it.",
  parts=[
    ('a', "**Glucagon.** The first-line defence: it raises glucose within minutes by glycogenolysis and gluconeogenesis, and in DKA it drives ketone production when insulin is lacking."),
    ('b', "**Glucocorticoids (cortisol).** They act over hours: gluconeogenesis, protein breakdown, insulin resistance."),
    ('c', "**Catecholamines.** Adrenaline acts within minutes and also suppresses insulin release (α2 on β-cells) and increases lipolysis."),
    ('d', "**Growth hormone.** It acts over hours, causing insulin resistance and lipolysis. DKA and HHS need both insulin deficiency (absolute or severe in DKA, relative in HHS, where enough insulin remains to block ketogenesis) and a rise in these four hormones, usually triggered by infection."),
  ],
  mimic=[
    ("Insulin deficiency vs counter-regulatory excess in DKA", "Both are needed: the lack of insulin and the excess of glucagon, cortisol, catecholamines and GH together drive hyperglycaemia and ketosis."),
  ],
  traps=[
    ("“Insulin contributes to DKA and HHS”", "It is the lack of insulin, not insulin, that contributes; the hormone among the options that drives them is cortisol, a counter-regulatory hormone."),
    ("“Oestrogen or TSH is a counter-regulatory hormone”", "The four are glucagon, glucocorticoids, catecholamines and growth hormone."),
  ],
  decode=[
    ("Which hormone contributes to DKA and HHS: insulin, oestrogen, cortisol or TSH? [DocT GT, 49% right]", "Cortisol."),
    ("Name the counter-regulatory hormones. [pattern]", "Glucagon, glucocorticoids, catecholamines, growth hormone."),
  ],
  punch="Glucagon and adrenaline act in minutes, cortisol and growth hormone over hours; together with insulin lack they produce DKA and HHS, so cortisol is the answer when asked which hormone contributes.",
)

L['GLU-17'] = dict(
  sub="Glucose control → Stress hyperglycaemia → Treatment-related causes",
  step=3,
  intro="Step 3 is not only the patient’s biology: ICU care itself adds glucose. Never asked; a [pattern] card, often the answer to ‘what to look for when glucose suddenly rises’.",
  parts=[
    ('a', "**Enteral or parenteral nutrition.** Parenteral nutrition gives a large glucose load straight into the vein, bypassing the gut hormones that help insulin work."),
    ('b', "**Dextrose solutions.** Including dextrose used as drug diluent and maintenance fluid."),
    ('c', "**Drugs: corticosteroids, vasopressors.** Steroids act through gluconeogenesis and insulin resistance; adrenaline raises glucose (and lactate) more than noradrenaline."),
    ('d', "**Dialysis.** Dextrose in peritoneal dialysate and some CRRT fluids is absorbed."),
    ('e', "**Bed rest.** Immobile muscle quickly becomes resistant to insulin, and muscle is where most glucose normally goes."),
  ],
  mimic=[],
  traps=[
    ("“A sudden rise in glucose in a stable patient means new sepsis”", "First check the drug chart and fluids: new steroids, adrenaline, dextrose or a feed increase are commoner causes."),
  ],
  decode=[
    ("Name treatment-related causes of hyperglycaemia in the ICU. [pattern]", "Nutrition, dextrose, steroids and vasopressors, dialysis, bed rest."),
  ],
  punch="Nutrition, dextrose, steroids, catecholamines, dialysis fluids and bed rest all raise glucose, so review the treatment before blaming the illness.",
)

L['GLU-18'] = dict(
  sub="Glucose control → Stress hyperglycaemia → Predisposing conditions",
  step=3,
  intro="Step 3 closes with who is primed for it and the two defects that produce it. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Pre-existing diabetes, obesity, cirrhosis.** All three already have insulin resistance; cirrhosis adds hepatic and muscle insulin resistance and small glycogen stores (high insulin levels in cirrhosis come from reduced hepatic clearance and do not overcome the resistance). Stress pushes them over the threshold more easily."),
    ('b', "**Increased insulin resistance plus relative insulin deficiency.** Resistance comes from cytokines, cortisol, growth hormone and immobility. The deficiency is relative because insulin levels may be normal or high but are too low for the resistance; catecholamines also suppress insulin release. Both are needed: resistance alone is usually compensated by more insulin."),
  ],
  mimic=[],
  traps=[
    ("“Stress hyperglycaemia is from absolute insulin deficiency”", "Insulin may be normal or high; it is relatively inadequate for the resistance. Absolute deficiency is type 1 diabetes and DKA."),
  ],
  decode=[
    ("Which two insulin abnormalities generate stress hyperglycaemia? [pattern]", "Increased insulin resistance and relative insulin deficiency."),
  ],
  punch="Diabetes, obesity and cirrhosis predispose; stress hyperglycaemia itself needs both insulin resistance and an insulin supply too small to overcome it.",
)

# ---------- Step 4: adverse effects ----------

L['GLU-19'] = dict(
  sub="Glucose control → Adverse effects → By organ system",
  step=4,
  intro="Step 4 is why the high limb of the J is treated. This master card lists the five systems; the cards that follow give the mechanism for each. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Immune dysfunction.** Neutrophils and complement fail (GLU-20), which is why infections rise."),
    ('b', "**Blood: coagulation and fibrinolysis.** Clots form more readily and break down less (GLU-21)."),
    ('c', "**Microcirculation and endothelium.** Glucose impairs nitric oxide-mediated vasodilatation (GLU-21)."),
    ('d', "**Kidneys: osmotic diuresis.** Fluid and electrolytes are lost (GLU-23)."),
    ('e', "**Heart: free fatty acids, ischaemia, arrhythmia.** (GLU-24.) Protein breakdown in muscle (GLU-22) completes the picture. The outcomes cut in Leuven Surgical (infection, kidney failure, transfusion, neuropathy; GLU-33) map onto these systems."),
  ],
  mimic=[],
  traps=[
    ("“Hyperglycaemia’s harm in the ICU is mainly osmotic”", "Osmotic diuresis is one effect; infection through neutrophil failure is the best documented."),
  ],
  decode=[
    ("List the adverse effects of hyperglycaemia by system. [pattern]", "Immune, coagulation, endothelium/microcirculation, renal (osmotic diuresis), cardiac."),
  ],
  punch="High glucose harms immunity, clotting, endothelium, kidney and heart, and these match the outcomes intensive insulin improved in Leuven Surgical.",
)

L['GLU-20'] = dict(
  sub="Glucose control → Adverse effects → Immune",
  step=4,
  intro="Step 4’s best-supported harm is infection. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Neutrophil dysfunction.** Above about 200 mg/dL, neutrophil chemotaxis, phagocytosis and the oxidative burst all fall. Glucose diverted into the polyol pathway uses up NADPH, which the burst needs."),
    ('b', "**Decreased bactericidal activity and opsonisation.** Glucose glycates complement and immunoglobulins, so bacteria are less well coated for phagocytosis."),
    ('c', "**Mitochondrial dysfunction, impairing the inflammatory cascade.** Cells that take up glucose without insulin (GLUT1, GLUT3) are flooded, which generates reactive oxygen species and damages mitochondria; liver biopsies from conventional-arm Leuven patients showed this damage."),
  ],
  mimic=[],
  traps=[
    ("“Hyperglycaemia impairs mainly T-lymphocyte function”", "The documented defects are in neutrophils, complement and opsonisation, plus mitochondrial damage."),
  ],
  decode=[
    ("Which immune cell is chiefly impaired by hyperglycaemia? [pattern]", "The neutrophil (chemotaxis, phagocytosis, oxidative burst)."),
  ],
  punch="High glucose cripples neutrophils, weakens opsonisation and damages mitochondria, which is why bloodstream infections fell with insulin in Leuven Surgical.",
)

L['GLU-21'] = dict(
  sub="Glucose control → Adverse effects → Coagulation and endothelium",
  step=4,
  intro="Step 4’s second and third systems act together in the microcirculation. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Impaired fibrinolysis and platelet function.** Hyperglycaemia raises plasminogen activator inhibitor-1 (PAI-1), so clots are broken down less; platelets become more reactive."),
    ('b', "**Hypercoagulability and thrombotic events.** The result of the above, with raised tissue factor."),
    ('c', "**Endothelial dysfunction, compromising the microcirculation.** Glucose lowers nitric oxide availability and generates oxidative stress, so small vessels vasodilate poorly. It is the same microcirculation that makes SC insulin unreliable in shock (GLU-27)."),
  ],
  mimic=[],
  traps=[
    ("“Hyperglycaemia increases fibrinolysis and bleeding”", "It does the opposite: PAI-1 rises, fibrinolysis falls and the patient becomes prothrombotic."),
  ],
  decode=[
    ("Effect of hyperglycaemia on fibrinolysis? [pattern]", "Impaired (PAI-1 rises), giving hypercoagulability."),
  ],
  punch="High glucose raises PAI-1 and platelet reactivity and lowers nitric oxide, so the patient clots more and the microcirculation fails.",
)

L['GLU-22'] = dict(
  sub="Glucose control → Adverse effects → Protein and muscle",
  step=4,
  intro="Step 4’s quieter harm is to muscle, which feeds the ICU-acquired weakness. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Facilitates protein breakdown.** Insulin normally restrains proteolysis; with insulin resistance, and with cortisol active, muscle protein is broken down to supply amino acids for gluconeogenesis (GLU-13)."),
    ('b', "**Worsens catabolism in skeletal muscle.** This adds to ICU-acquired weakness; Leuven Surgical reduced critical illness polyneuropathy by 44% with intensive insulin."),
  ],
  mimic=[],
  traps=[
    ("“Hyperglycaemia is anabolic because glucose is fuel”", "In insulin resistance glucose cannot get into muscle, and protein is broken down instead."),
  ],
  decode=[
    ("Effect of hyperglycaemia on skeletal muscle in critical illness? [pattern]", "Increased proteolysis and catabolism."),
  ],
  punch="With insulin resistance, muscle protein is broken down to make more glucose, worsening catabolism and ICU-acquired weakness.",
)

L['GLU-23'] = dict(
  sub="Glucose control → Adverse effects → Renal",
  step=4,
  intro="Step 4’s renal effect follows from simple tubular physiology. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Promotes osmotic diuresis.** Above the renal threshold of about 180 mg/dL, the proximal tubule’s glucose transporters (SGLT2) are saturated and glucose stays in the tubule, holding water with it."),
    ('b', "**Hypovolaemia.** Urine output can look reassuringly high while the patient is losing volume, so urine output stops being a reliable sign of perfusion."),
    ('c', "**Electrolyte abnormalities.** Potassium, phosphate and magnesium are lost in the urine; water lost in excess of sodium raises plasma sodium once the glucose is corrected."),
  ],
  mimic=[],
  traps=[
    ("“Good urine output means adequate perfusion in a hyperglycaemic patient”", "Osmotic diuresis keeps urine flowing even when the patient is volume depleted."),
  ],
  decode=[
    ("Renal consequence of hyperglycaemia and its results? [pattern]", "Osmotic diuresis, giving hypovolaemia and electrolyte losses."),
  ],
  punch="Above about 180 mg/dL glucose spills into the urine and drags water and electrolytes with it, so urine output becomes a false reassurance.",
)

L['GLU-24'] = dict(
  sub="Glucose control → Adverse effects → Cardiac chain",
  step=4,
  intro="Step 4’s last system: the heart, harmed through fat rather than glucose itself. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Raised free fatty acids increase myocardial oxygen demand.** With insulin resistance and catecholamines, lipolysis rises and the heart shifts from glucose to fatty acids. Burning fat uses more oxygen for each unit of ATP than burning glucose."),
    ('b', "**This leads to ischaemia.** In a heart with limited oxygen supply, the higher demand tips into ischaemia."),
    ('c', "**Then reduced myocardial contractility.** The ischaemic, fatty-acid-loaded myocyte contracts less well."),
    ('d', "**And cardiac arrhythmias.** Fatty acids and ischaemia destabilise the membrane, and the potassium and magnesium losses of osmotic diuresis add to the risk."),
  ],
  mimic=[],
  traps=[
    ("“Hyperglycaemia harms the heart because glucose is toxic to myocytes”", "The chain starts with free fatty acids raising oxygen demand."),
  ],
  decode=[
    ("Trace the cardiac harm of hyperglycaemia. [pattern]", "Raised FFA → higher myocardial O₂ demand → ischaemia → reduced contractility → arrhythmias."),
  ],
  punch="In insulin resistance the heart burns fatty acids, which need more oxygen, so ischaemia, weaker contraction and arrhythmia follow.",
)

# ---------- Step 5: HbA1c, targets, insulin delivery ----------

L['GLU-25'] = dict(
  sub="Glucose control → HbA1c → Uses in critical illness",
  step=5,
  intro="Step 5 begins with the one test that shows the patient’s glucose before he got ill. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Differentiates stress hyperglycaemia from diabetes.** HbA1c reflects the average glucose over about three months, so acute stress does not raise it. An HbA1c of 6.5% or more means pre-existing diabetes, which needs follow-up and a discharge plan. The ADA advises checking it in any hyperglycaemic inpatient without a result in the previous three months."),
    ('b', "**Prognostic significance.** Combined with admission glucose it gives the stress hyperglycaemia ratio: admission glucose ÷ (28.7 × HbA1c − 46.7). A high ratio (a big rise above the patient’s own average) predicts worse outcome better than glucose alone."),
    ('c', "**Used to formulate glycaemic control protocols.** HbA1c-based targets have been tested (GLU-26), but no benefit has been shown, so no guideline uses them yet. HbA1c is falsely low after transfusion, haemorrhage or haemolysis, which are common in the ICU."),
  ],
  mimic=[
    ("Stress hyperglycaemia vs undiagnosed diabetes", "Normal HbA1c with high glucose is stress hyperglycaemia; HbA1c ≥6.5% means diabetes was already there."),
  ],
  traps=[
    ("“HbA1c is unreliable in the ICU, so it should not be sent”", "It is reliable except after recent transfusion, bleeding or haemolysis, and it is the only way to tell new from pre-existing diabetes."),
  ],
  decode=[
    ("What separates stress hyperglycaemia from pre-existing diabetes on admission? [pattern]", "HbA1c (≥6.5% means diabetes)."),
  ],
  punch="HbA1c tells stress hyperglycaemia from diabetes, gives the stress hyperglycaemia ratio for prognosis, and is misleading after transfusion or bleeding.",
)

L['GLU-26'] = dict(
  sub="Glucose control → HbA1c → HbA1c-tiered targets",
  step=5,
  intro="Step 5 tests whether the target should depend on the patient’s usual glucose. The card gives the old teaching and its own correction; the exam answer follows the guideline. Never asked; a [pattern] card.",
  parts=[
    ('a', "**HbA1c under 7%: 140–180 mg/dL.** This is the standard target for everyone."),
    ('b', "**HbA1c over 7%, surgical: 140–180 mg/dL.** The same target."),
    ('c', "**HbA1c over 7%, medical: 180–220 mg/dL in the old notes only; no guideline uses HbA1c tiers: start insulin at ≥180 and target 140–180 for all.** The idea was that a poorly controlled diabetic’s tissues are used to high glucose (the flattened J-curve, GLU-07), so lowering it to 140–180 risks relative hypoglycaemia without benefit. The idea is reasonable but unproven: LUCID (2022, 419 type 2 diabetics) compared a liberal 180–252 mg/dL with 108–180 and cut hypoglycaemia (5% vs 18%) without improving outcomes (90-day mortality 29.5% vs 24.9%, not significant)."),
    ('d', "**Caution: the tiers are expert opinion. SCCM 2024: start insulin at persistent BG ≥180 mg/dL, keep a conventional target (SCCM compared 140–200; ADA uses 140–180) and avoid 80–139. CONTROLING (2021, n 2,075): an HbA1c-individualised target gave no benefit (90-day mortality about 32.8% vs 30.4%) and was stopped early.** CONTROLING lowered the target for patients with a normal HbA1c (to their own estimated average glucose), and roughly doubled the rate of any hypoglycaemia under 72 mg/dL (31% vs 16%). SCCM 2024 lists HbA1c-based targets as a research question, not a recommendation."),
  ],
  mimic=[],
  traps=[
    ("“A medical ICU diabetic with HbA1c over 7% should be kept at 180–220”", "No guideline says so; the target is 140–180 for all, with insulin started at ≥180."),
    ("“Individualising targets by HbA1c improves survival”", "CONTROLING found no benefit, more hypoglycaemia and was stopped early."),
  ],
  decode=[
    ("Glucose target for a critically ill diabetic with HbA1c 9%? [pattern]", "140–180 mg/dL, as for everyone (ADA; SCCM 2024)."),
  ],
  punch="HbA1c-tiered targets are opinion; the guideline answer is start insulin at ≥180 and aim for 140–180 whatever the HbA1c.",
)

L['GLU-27'] = dict(
  sub="Glucose control → Insulin protocol → IV over SC",
  step=5,
  intro="Step 5’s delivery question. The linked Marrow question is about a ward patient, not an ICU one, and its key (sliding scale) is outdated.",
  parts=[
    ('a', "**Compromised microcirculation.** In shock, oedema or on vasopressors, skin blood flow falls, so absorption from a subcutaneous depot is slow, then may surge when perfusion returns."),
    ('b', "**SC injection therefore has unpredictable effects.** IV insulin has a half-life of only a few minutes, so an infusion can be titrated hour by hour and stopped at once if glucose falls. SCCM 2024 suggests continuous IV infusion over intermittent SC insulin for acute hyperglycaemia in the critically ill. For stable ward patients the opposite applies: scheduled SC basal (plus prandial and correction) insulin is standard (ADA)."),
  ],
  mimic=[
    ("ICU patient vs ward/peri-operative patient", "Critically ill: IV infusion by protocol. Stable ward patient: basal or basal-bolus SC insulin with correction doses, not sliding scale alone."),
  ],
  traps=[
    ("“Sliding-scale SC insulin is the inpatient plan for a T2DM patient after laparoscopic cholecystectomy”", "The Marrow key is outdated: the ADA discourages sliding scale alone; give basal insulin with correction doses (basal-bolus once eating), and hold metformin and the oral agents in hospital."),
  ],
  decode=[
    ("T2DM on glipizide, sitagliptin and metformin, admitted after lap chole: inpatient glucose plan? [Marrow]", "Keyed ‘sliding-scale SC insulin’; current ADA answer is basal (or basal-bolus) SC insulin plus correction doses. Choose sliding scale only if no basal option is offered."),
    ("Why is IV insulin preferred in the ICU? [pattern]", "Poor microcirculation makes SC absorption unpredictable; IV acts and stops within minutes."),
  ],
  punch="In the critically ill, poor skin perfusion makes SC insulin unpredictable, so use an IV infusion; on the ward, scheduled basal insulin, not sliding scale alone.",
)

L['GLU-28'] = dict(
  sub="Glucose control → Insulin protocol → Monitoring frequency",
  step=5,
  intro="Step 5’s safety rule: a fast-acting infusion needs frequent checks. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Hourly initially.** Until glucose is stable in range, IV insulin can move it quickly, and hypoglycaemia gives no warning in a sedated patient. SCCM 2024 suggests checking at least hourly during instability."),
    ('b', "**4-hourly once stabilised.** This is longer than the guidance: the ADA hospital chapter asks for bedside checks every 30 minutes to 2 hours for as long as IV insulin runs, and most protocols check every 1–2 hours once stable. 4-hourly fits a stable patient on subcutaneous insulin with continuous feeds. Go back to hourly with any change in feed, steroids, vasopressors or after hypoglycaemia."),
  ],
  mimic=[],
  traps=[
    ("“Once stable on an infusion, 4–6-hourly checks are enough”", "Feed interruptions on an infusion cause hypoglycaemia within an hour or two; ADA keeps checks every 30 minutes to 2 hours while IV insulin runs. Write 4-hourly only if the options follow the card."),
  ],
  decode=[
    ("How often is glucose checked on an IV insulin infusion? [pattern]", "Hourly until stable, then every 1–2 hours (ADA: every 30 min to 2 h); the card’s 4-hourly is the older teaching."),
  ],
  punch="Check hourly until stable and go back to hourly with any change in feed or drugs; while IV insulin runs, ADA keeps checks every 30 minutes to 2 hours.",
)

L['GLU-29'] = dict(
  sub="Glucose control → Insulin protocol → Benefits of a protocol",
  step=5,
  intro="Step 5 ends with why the infusion should run on a written or computerised protocol. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Improved control of glucose.** A protocol adjusts the rate by both the current value and its direction, which bedside judgement does inconsistently."),
    ('b', "**Improved time in target range.** (GLU-04.)"),
    ('c', "**Reduced treatment error.** Standard concentrations and fixed steps remove calculation errors."),
    ('d', "**Avoids hypoglycaemia.** It builds in automatic dose reduction and a dextrose rule. SCCM 2024 suggests protocols with explicit decision-support tools (paper or computerised) for IV insulin, and as good practice protocols with a low hypoglycaemia risk."),
  ],
  mimic=[],
  traps=[
    ("“Protocols matter only for tight targets”", "SCCM 2024 recommends decision-support protocols at conventional targets too, mainly to prevent hypoglycaemia."),
  ],
  decode=[
    ("Benefit of a protocolised (decision-support) insulin infusion? [pattern]", "Better control and time in range, fewer errors, less hypoglycaemia (SCCM 2024)."),
  ],
  punch="A protocol, ideally computerised, gives better control and time in range with fewer errors and less hypoglycaemia, and SCCM 2024 suggests one for every infusion.",
)

# ---------- Step 6: trials ----------

L['GLU-30'] = dict(
  sub="Glucose control → Trials → Leuven Surgical: design",
  step=6,
  intro="Step 6 begins with the trial that started tight control. Who was studied explains why it did not generalise. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Single-centre RCT, Leuven, Belgium.** Single-centre trials often overestimate effect; the result was not reproduced in multicentre trials."),
    ('b', "**Van den Berghe et al. (NEJM 2001).**"),
    ('c', "**1,548 adult surgical ICU patients receiving mechanical ventilation.** About 63% had cardiac surgery, and all received IV glucose (200–300 g a day) from admission, followed by parenteral, mixed or enteral feeding from the next day, so the control arm was unusually hyperglycaemic. Later trials, with less IV glucose, found no benefit."),
  ],
  mimic=[],
  traps=[
    ("“Leuven Surgical was a multicentre trial”", "It was single-centre, which is one reason its benefit did not survive NICE-SUGAR."),
  ],
  decode=[
    ("Leuven Surgical: design and population? [pattern]", "Single-centre RCT, 1,548 ventilated surgical ICU adults (about 63% cardiac surgery)."),
  ],
  punch="Leuven Surgical was one centre, mostly cardiac surgical patients given high IV glucose loads, which is why its benefit did not generalise.",
)

L['GLU-31'] = dict(
  sub="Glucose control → Trials → Leuven targets",
  step=6,
  intro="Step 6’s two arms, shared by both Leuven trials; the later trials changed the control arm, and that changed the result. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Intensive: 80–110 mg/dL.** Normoglycaemia, by insulin infusion."),
    ('b', "**Conventional: 180–200 mg/dL.** Insulin was started only above 215 mg/dL. That is higher than today’s ‘conventional’ arm: NICE-SUGAR compared 81–108 with a target of 180 or less (insulin from 180, aiming 144–180), and then tight control increased mortality (27.5% vs 24.9%)."),
  ],
  mimic=[
    ("Leuven conventional vs NICE-SUGAR conventional", "Leuven: insulin only above 215, kept 180–200. NICE-SUGAR: target ≤180 mg/dL. Against the lower control arm, tight control did harm."),
  ],
  traps=[
    ("“NICE-SUGAR used the same targets as Leuven”", "Its intensive arm was similar (81–108), but its control arm was lower (≤180), and the result reversed."),
  ],
  decode=[
    ("Glucose targets in the Leuven trials? [pattern]", "80–110 mg/dL intensive vs 180–200 mg/dL conventional (insulin above 215)."),
  ],
  punch="Leuven compared 80–110 with 180–200; NICE-SUGAR compared 81–108 with ≤180 and found tight control killed more, which set today’s 140–180 target.",
)

L['GLU-32'] = dict(
  sub="Glucose control → Trials → Leuven Surgical: result",
  step=6,
  intro="Step 6’s headline result that made tight control standard for nearly a decade. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Primary outcome: mortality (ICU).**"),
    ('b', "**ICU mortality lower with intensive insulin: 8% → 4.6%, P < 0.04.** The P value was adjusted for repeated interim analyses. The gain was largest in patients staying more than 5 days (20.2% vs 10.6%), mostly fewer deaths from multiple organ failure with sepsis. The cost was hypoglycaemia (≤40 mg/dL) in 39 vs 6 patients (5.1% vs 0.8%)."),
  ],
  mimic=[],
  traps=[
    ("“Leuven Surgical lowered 90-day mortality”", "Its primary outcome was ICU mortality (8.0% vs 4.6%); 90-day mortality was the NICE-SUGAR outcome."),
  ],
  decode=[
    ("Leuven Surgical: primary outcome and result? [pattern]", "ICU mortality, 8.0% vs 4.6% (P<0.04)."),
  ],
  punch="Leuven Surgical cut ICU mortality from 8.0% to 4.6%, mostly in long-stay patients, but in one centre and against a high-glucose control arm.",
)

L['GLU-33'] = dict(
  sub="Glucose control → Trials → Leuven Surgical: secondary benefits",
  step=6,
  intro="Step 6’s secondary outcomes match the harms of step 4. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Sepsis.** Bloodstream infections fell by 46%, consistent with better neutrophil function (GLU-20)."),
    ('b', "**Acute renal failure.** Renal failure needing dialysis or haemofiltration fell by 41%."),
    ('c', "**Red cell transfusion.** The number of red cell transfusions fell by 50%."),
    ('d', "**In-hospital mortality.** It fell by 34%. Critical illness polyneuropathy also fell by 44%."),
  ],
  mimic=[],
  traps=[
    ("“Leuven Surgical reduced ventilator-associated pneumonia”", "The infection benefit was in bloodstream infections (septicaemia)."),
  ],
  decode=[
    ("Besides ICU mortality, what did intensive insulin reduce in Leuven Surgical? [pattern]", "Bloodstream infection, renal failure needing RRT, red cell transfusion, in-hospital mortality (and polyneuropathy)."),
  ],
  punch="Leuven Surgical cut bloodstream infection, renal failure needing RRT, transfusion, polyneuropathy and in-hospital death.",
)

L['GLU-34'] = dict(
  sub="Glucose control → Trials → Leuven Medical: population",
  step=6,
  intro="Step 6 then tested the same idea in medical patients, from the same centre. Never asked; a [pattern] card.",
  parts=[
    ('a', "**1,200 medical ICU patients.** Same centre, same targets (80–110 vs 180–200)."),
    ('b', "**All unable to take oral nutrition.** Patients able to eat were excluded, because they rarely need three or more days of intensive care; the inclusion was medical patients expected to need intensive care for at least three days. That expectation was wrong in 433, who left the ICU sooner, which matters for GLU-36."),
  ],
  mimic=[],
  traps=[
    ("“Leuven Medical was multicentre”", "It was the same single Leuven centre as the surgical trial."),
  ],
  decode=[
    ("Leuven Medical trial population? [pattern]", "1,200 medical ICU adults expected to stay at least 3 days, excluding those able to take oral nutrition."),
  ],
  punch="Leuven Medical repeated the surgical trial in 1,200 medical ICU patients who could not eat and were expected to stay at least three days, in the same single centre.",
)

L['GLU-35'] = dict(
  sub="Glucose control → Trials → Leuven Medical: result",
  step=6,
  intro="Step 6’s first warning: in medical patients tight control did not save lives and caused much hypoglycaemia. Never asked; a [pattern] card.",
  parts=[
    ('a', "**No difference in primary or secondary endpoints.** The primary outcome, in-hospital mortality, did not differ (37.3% vs 40.0%, P=0.33). The secondary outcomes did improve, though: in all patients, intensive insulin reduced new kidney injury and shortened ventilation, ICU stay and hospital stay. So ‘no mortality difference, less morbidity’ is the accurate summary."),
    ('b', "**Severe hypoglycaemia with intensive insulin: 18.7%.** Against 3.1% with conventional treatment, about six times as many. The investigators reported no immediate harm from the episodes, but later cohorts (Krinsley 2007, NICE-SUGAR 2012) linked even one severe episode with death."),
  ],
  mimic=[],
  traps=[
    ("“Leuven Medical showed no benefit of any kind”", "Mortality was unchanged but morbidity (kidney injury, ventilation time, length of stay) fell."),
  ],
  decode=[
    ("Leuven Medical: result and severe hypoglycaemia rate? [pattern]", "No difference in in-hospital mortality; severe hypoglycaemia 18.7% vs 3.1%."),
  ],
  punch="Leuven Medical did not lower mortality, reduced morbidity, and caused severe hypoglycaemia in nearly one patient in five.",
)

L['GLU-36'] = dict(
  sub="Glucose control → Trials → Leuven Medical: the subgroup",
  step=6,
  intro="Step 6’s classic trap figure: the mortality benefit everyone quotes was in a subgroup that could not be identified in advance. Never asked; a [pattern] card.",
  parts=[
    ('a', "**In-hospital mortality, intensive vs conventional.** 52.5% (conventional) vs 43.0% (intensive), P=0.009."),
    ('b', "**The catch: this was the subgroup staying 3 days or more in the ICU, not the intention-to-treat population.** Length of stay is known only afterwards and is itself affected by treatment, so the subgroup was not randomised. In those who stayed less than 3 days (433), mortality was higher with intensive insulin. The whole-trial figure was 40.0% vs 37.3%, not significant."),
    ('c', "**Secondary analyses: less AKI, shorter ventilation, shorter ICU and hospital stay.** These morbidity gains were present in all patients, not only the long-stay group."),
  ],
  mimic=[
    ("Intention-to-treat vs post-randomisation subgroup", "ITT keeps randomisation and is the answer; a subgroup defined by something that happened after randomisation (length of stay) can be biased."),
  ],
  traps=[
    ("“Leuven Medical reduced in-hospital mortality from 52.5% to 43.0%”", "Only in the ≥3-day subgroup; the ITT result was 40.0% vs 37.3% (P=0.33)."),
  ],
  decode=[
    ("Leuven Medical: what is the 43.0% vs 52.5% figure? [pattern]", "In-hospital mortality in the ≥3-day ICU stay subgroup, not the ITT population."),
  ],
  punch="The 52.5% vs 43.0% benefit was in a subgroup defined after randomisation; the intention-to-treat result showed no mortality difference.",
)

L['GLU-37'] = dict(
  sub="Glucose control → Trials → VISEP: design",
  step=6,
  intro="Step 6’s multicentre sepsis trial tested two questions at once. Never asked; a [pattern] card, often asked for its starch half.",
  parts=[
    ('a', "**Multicentre RCT, 537 patients with severe sepsis.** 18 German academic ICUs (Brunkhorst, NEJM 2008); severe sepsis or septic shock."),
    ('b', "**Intensive vs conventional insulin therapy.** Intensive 80–110 mg/dL vs conventional (insulin above 200 mg/dL, aiming 180–200)."),
    ('c', "**And 10% starch vs modified Ringer’s lactate.** A 2 × 2 factorial design: 10% HES 200/0.5 (pentastarch) vs modified Ringer’s lactate for resuscitation."),
  ],
  mimic=[],
  traps=[
    ("“VISEP compared starch with albumin”", "The comparator was modified Ringer’s lactate; albumin was SAFE."),
  ],
  decode=[
    ("VISEP: design and interventions? [pattern]", "Multicentre 2 × 2 factorial RCT in 537 severe sepsis patients: intensive vs conventional insulin, and 10% HES vs modified Ringer’s lactate."),
  ],
  punch="VISEP was a German multicentre factorial trial in severe sepsis testing intensive insulin and 10% starch together.",
)

L['GLU-38'] = dict(
  sub="Glucose control → Trials → VISEP: results",
  step=6,
  intro="Step 6’s sepsis result: tight control gave no benefit, more hypoglycaemia and early stopping. Never asked; a [pattern] card.",
  parts=[
    ('a', "**Outcomes: 28-day mortality plus mean organ failure (SOFA) score.** These were co-primary."),
    ('b', "**No significant difference in mortality.** 28-day mortality 24.7% vs 26.0%; mean SOFA 7.8 vs 7.7."),
    ('c', "**Intensive insulin: lower mean glucose, but more severe hypoglycaemia and serious adverse events.** Hypoglycaemia (≤40 mg/dL) 17.0% vs 4.1%; serious adverse events 10.9% vs 5.2%. The insulin arm was itself stopped early for safety, after the first safety analysis of 488 patients."),
    ('d', "**Starch: more AKI and RRT, and the trial was stopped early.** Acute renal failure 34.9% vs 22.8%, RRT 31.0% vs 18.8%, with a trend to higher 90-day mortality (41.0% vs 33.9%). The whole study was suspended at the planned interim analysis. So VISEP stopped early for both reasons: hypoglycaemia in the insulin arm and kidney harm in the starch arm."),
  ],
  mimic=[
    ("Why the insulin arm stopped vs why the starch arm stopped", "Insulin: hypoglycaemia (17.0% vs 4.1%). Starch: kidney injury and RRT."),
  ],
  traps=[
    ("“VISEP was stopped only because of starch”", "The insulin arm was stopped first, for hypoglycaemia; the starch arm then stopped at the interim analysis for kidney harm."),
  ],
  decode=[
    ("Why was VISEP stopped early? [pattern]", "Hypoglycaemia with intensive insulin, then more AKI and RRT with 10% HES."),
  ],
  punch="VISEP found no mortality benefit, stopped its insulin arm for hypoglycaemia and its starch arm for kidney injury; with NICE-SUGAR it ended tight control.",
)

FLAGS = {
  'GLU-02': "Card is correct (ADA levels <70, <54, level 3). The endo_cardlayer Marrow line says ‘this card uses <60 mg/dL’; the current card uses <70, so that line is out of date. Crossfire’s exam rule (70 when ADA levels are in the options) is kept.",
  'GLU-14': "Incomplete: the card routes IL-6 only to the anterior pituitary; IL-6 also stimulates the adrenal cortex directly (the DocT QBank key, 67% right). The explanation teaches it.",
  'GLU-27': "Card is correct for the ICU. The linked Marrow question is a ward/peri-operative patient keyed ‘sliding-scale SC insulin’; that key is outdated (ADA: basal or basal-bolus with correction; sliding scale alone discouraged). Said in the trap.",
  'GLU-28': "‘4th hourly once stabilised’ is longer than guidance while an IV infusion runs: ADA hospital chapter asks for checks every 30 min to 2 h; SCCM 2024 at least hourly during instability. 4-hourly fits a stable patient on SC insulin. The explanation says so.",
  'GLU-35': "‘No difference in primary or secondary endpoints’ is wrong: mortality did not differ, but in the whole trial intensive insulin reduced new kidney injury and shortened ventilation, ICU stay and hospital stay (as GLU-36 itself says).",
  'GLU-38': "Incomplete: the card attributes early stopping only to starch; the intensive insulin arm was itself stopped early for hypoglycaemia (17.0% vs 4.1%) after the first safety analysis.",
}
