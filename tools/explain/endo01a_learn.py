# ENDO01A — Explain v3 ("Learn" depth): thyroid physiology (synthesis, T3 vs T4, test patterns and causes of thyrotoxicosis), thyroid storm (epidemiology, triggers,
# mechanism, features, Burch–Wartofsky and Japanese criteria, drugs and their order), myxoedema coma (definition, causes, investigations, treatment), true/false sweep.
# No mnemonics or hooks. Driven by qpack/ENDO01A.md (36 question links; ENDO-08 storm drugs asked 8 times, ENDO-12 myxoedema treatment 7, ENDO-09 order of storm treatment 6,
# ENDO-05 storm features 4). ENDO-01, -02, -06, -07 and -13 have no linked question and get short explanations with [pattern] decode items.
# The card layer (endo_cardlayer.json, ENDO01A|…) lines and the ENDO-08 crossfire note were read and are agreed with. No `fix` entries for ENDO01A in trace/test/data/qbank.json (checked 22 Nov 2026).
# Fields as TOX01, plus SPINE, PRIMER and step. Table cards (no lettered parts) take parts a, b, c… in the order of the card’s rows or lines.
# Checked online on 22 Nov 2026:
#  - Akamizu et al., Thyroid 2012 (PubMed 22690898, abstract): JTA criteria TS1/TS2 with thyrotoxicosis a prerequisite; bilirubin >3 mg/dL the only added item; 356 patients; incidence 0.20 per
#    100,000 per year among hospitalised patients in Japan; mortality TS1 11.0%, TS2 9.5%; multiple organ failure the commonest cause of death, then heart failure; free T4 and T3 similar in storm
#    and in thyrotoxicosis without storm.
#  - JTA/JES 2016 guideline (Satoh, Endocr J 2016;63:1025; PubMed 27746415 abstract): mortality about 11%; multimodal antithyroid drug, inorganic iodide, corticosteroid and β-blocker.
#    The full text could not be opened (PDF blocked); JTA drug-specific points (landiolol/esmolol at Killip ≥III) are taken from the card-layer note and worded as such.
#  - JTA criteria table (Thyroid Res 2024, table 2): CNS (restlessness, delirium, psychosis, somnolence, coma, GCS ≤14), fever ≥38 °C, HR ≥130 (including in AF), heart failure = pulmonary oedema,
#    moist rales over more than half the lung field, cardiogenic shock, NYHA IV or Killip ≥III; GI-hepatic = nausea, vomiting, diarrhoea or bilirubin ≥3.0 mg/dL; TS1 = CNS + ≥1 other, or ≥3 others;
#    TS2 = 2 others, or TS1 features without hormone results; features clearly due to another illness do not count.
#  - Endotext ‘Thyroid storm’ (ATA 2016-based doses): propranolol 60–80 mg orally 4-hourly or 1–3 mg IV; esmolol 250–500 µg/kg then 50–100 µg/kg/min; PTU 500–1000 mg load then 250 mg 4-hourly;
#    methimazole 60–80 mg/day; iodide 250 mg 6-hourly given 1 h after the first thionamide dose; hydrocortisone 300 mg IV load then 100 mg 8-hourly; cholestyramine; lithium if iodine cannot be used;
#    plasma exchange second line; US incidence 0.57–0.76 per 100,000 per year; mortality about 10–25%; start β-blockers low (vascular collapse reported); PTU preferred initially, then methimazole.
#  - WikEM ‘Thyroid storm’: Burch–Wartofsky bands (temperature 99–99.9 °F 5 to ≥104 °F 30; heart rate 99–109 5 to ≥140 25; CNS 10/20/30; GI 10/20; heart failure 5/10/15; precipitant 0/10;
#    ≥45 storm, 25–44 impending, <25 unlikely); SSKI 5 drops (250 mg) 6-hourly or Lugol’s 8 drops 6-hourly 1 h after the thionamide; lithium 300 mg 8-hourly; paracetamol, not aspirin
#    (displaces hormone from TBG). WikEM folds AF into the severe heart failure row; the original 1993 scale scores AF as a separate +10, as the card does.
#  - Vanderbilt VIMbook: Lugol’s 8 drops 6-hourly at least 1 h after the thionamide; avoid propranolol in acute heart failure or shock.
#  - Endotext ‘Myxedema and coma’: mortality 20–50% (29.5% in-hospital in a 2010–13 Japanese series); precipitants cold, infection, stroke, sedatives, analgesics, diuretics; high vasopressin;
#    passive rewarming only (peripheral warming causes vasodilatation and shock); hydrocortisone stress doses because thyroid hormone speeds cortisol clearance; series suggest more deaths with
#    initial T4 above 500 µg or T3 above 75 µg a day.
#  - UCSF Hospitalist Handbook: IV T4 200–400 µg load, lower if elderly or cardiac; draw cortisol and give hydrocortisone until adrenal insufficiency excluded; mortality over 30%.
# Second check, 22 Nov 2026 (reviewer), confirmed online:
#  - JTA/JES 2016 guideline full text (Satoh, Endocr J 2016; NII repository PDF): β₁-selective landiolol or esmolol IV or bisoprolol 2.5–5 mg/day orally first choice, propranolol not recommended for the
#    tachycardia, rate target ≤130; landiolol/esmolol for HR ≥150 in Killip ≤III and considered in Killip IV; digitalis with AF; methimazole 60 mg/day or PTU 600 mg/day (methimazole ‘not
#    disadvantageous’; IV methimazole 30 mg/day); inorganic iodide ~200 mg/day given simultaneously with the thionamide (ATA’s ≥1 h noted); hydrocortisone 300 mg/day (100 mg 8-hourly) or
#    dexamethasone 8 mg/day; acetaminophen first, NSAIDs and aspirin not recommended; plasma exchange if no improvement in 24–48 h; mortality 38/356 = 10.7%.
#  - Akamizu 2012 abstract (PubMed 22690898): the only change from the first to the final criteria concerned the bilirubin >3 mg/dL threshold.
#  - Endotext ‘Thyroid storm’: propranolol 60–80 mg 4-hourly or 1–3 mg IV, PTU 500–1000 mg then 250 mg 4-hourly, methimazole 60–80 mg/day, KI 250 mg 6-hourly 1 h after the thionamide,
#    hydrocortisone 300 mg then 100 mg 8-hourly, dexamethasone 2 mg 6-hourly; US incidence 0.57–0.76/100,000/year; mortality 10–25%.
#  - Seo et al., Am Surg 2024 (US National Inpatient Sample 2016–2020): storm 2.5% of thyrotoxicosis admissions, ~1/100,000 population a year, in-hospital mortality 2.9–5.3%, ~72% women.
#  - Burch–Wartofsky reproductions: MDCalc prints heart rate 90–109 for 5 points; a 2017 reproduction citing the 1993 paper prints 99–109. Other bands, AF +10 and precipitant +10 agree.
#  - ATA 2014 myxoedema doses as cited by EMCrit IBCC (Jonklaas 2014): T4 200–400 µg IV load, T3 5–20 µg load then 2.5–10 µg 8-hourly, maintenance ~1.2 µg/kg/day IV (= 1.6 × 0.75).
#  - Myxoedema coma: incidence 0.22 per million/year (Western), 1.08 per million/year (Japan), hypothermia usually <35.5 °C (patient.info); hypothermia <35 °C and mortality 30–50% (2024 review).
# Still from standard teaching (restated, not expanded): free hormone fractions, half-lives, the card’s 0.01% myxoedema prevalence (not traceable; flagged).

SPINE = [
  ("Making and reading thyroid hormone", "The gland makes mostly T4, the tissues turn it into the active T3, and TSH is the most sensitive test because it amplifies small changes in free hormone."),
  ("Storm: a trigger tips thyrotoxicosis", "Thyroid storm is thyrotoxicosis that has decompensated into organ failure, usually after an infection, surgery or stopping antithyroid drugs, with hormone levels no higher than in ordinary thyrotoxicosis."),
  ("Scoring storm at the bedside", "Because no test separates storm from thyrotoxicosis, the diagnosis is clinical and is standardised by the Burch–Wartofsky score (45 or more) or the Japanese criteria."),
  ("Block, then stop, then protect", "Treatment blocks the adrenergic effects first, then stops synthesis with a thionamide, then stops release with iodine an hour later, and adds hydrocortisone to cut conversion and cover the adrenals."),
  ("Myxoedema coma: the opposite failure", "Myxoedema coma is severe hypothyroidism with depressed consciousness, recognised by hypothermia, hypoventilation, hyponatraemia and bradycardia in a patient with a trigger."),
  ("Steroid first, then gentle thyroxine", "In myxoedema coma, hydrocortisone goes in before thyroxine, thyroxine is loaded carefully to spare the heart, and the airway, sodium and temperature are supported."),
]

PRIMER = "Almost all circulating thyroid hormone is bound to proteins (TBG, transthyretin, albumin); only the tiny free fraction acts, so anything that changes binding changes the effect without changing the gland. T4 is a prohormone made only by the thyroid, and deiodinases in liver, kidney and other tissues remove one iodine to make T3, the hormone that binds the nuclear receptor; several storm drugs work here as well as in the gland. Thyroid hormone sets the number of β-adrenergic receptors and the metabolic rate, which is why excess looks like a catecholamine surge and deficiency looks like everything slowing down. Doses and criteria follow the ATA 2016 hyperthyroidism and ATA 2014 hypothyroidism guidelines, with the Japan Thyroid Association 2016 guideline where it differs."

L = {}

L['ENDO-01'] = dict(
  sub="Endocrine → Thyroid → Hormone synthesis",
  step=1,
  intro="Step 1 begins with how the gland makes hormone, because each storm drug acts on one of these steps. Iodide is trapped, attached to tyrosine on thyroglobulin, coupled, stored in colloid, and released by proteolysis.",
  parts=[
    ('a', "**Uptake: the sodium–iodide symporter on the basal side; pendrin moves iodide into the colloid.** The symporter uses the sodium gradient to concentrate iodide against its gradient; perchlorate competitively blocks it, and radioiodine (and pertechnetate for scans) enters the gland through it."),
    ('b', "**Organification, the critical step: thyroid peroxidase oxidises iodide and iodinates tyrosines on thyroglobulin, giving MIT and DIT.** This is where PTU and methimazole act (ENDO-08). A large iodide load also switches organification off for a time (Wolff–Chaikoff)."),
    ('c', "**Coupling: DIT + DIT = T4; DIT + MIT = T3.** Thyroid peroxidase also catalyses coupling, so thionamides block this too. Most of the output is T4 (ENDO-02)."),
    ('d', "**Release: colloid is taken up, fuses with lysosomes, and proteolysis frees T4 and T3.** High-dose iodine and lithium block release. That is why they lower hormone within days, whereas a thionamide only stops new synthesis and the stored colloid keeps leaking for weeks."),
    ('e', "**Feedback: hypothalamic TRH (a tripeptide) drives pituitary TSH; T4 and T3 inhibit both.** This loop is why TSH is the first test in primary disease (ENDO-03)."),
  ],
  mimic=[
    ("Thionamide vs iodine", "A thionamide stops new synthesis but not the release of stored hormone; iodine stops release fast but, given first, adds substrate for new hormone (ENDO-09)."),
  ],
  traps=[
    ("“A thionamide lowers T4 within hours”", "It blocks thyroid peroxidase, but weeks of stored hormone are still released; iodine is added in storm to stop release."),
  ],
  decode=[
    ("Which step is the critical (rate-limiting) step of synthesis? [pattern]", "Organification by thyroid peroxidase."),
    ("Match the drug to the step it blocks: thionamide, iodine excess, lithium [pattern]", "TPO (organification and coupling); organification and release; release."),
  ],
  punch="The gland traps, organifies, couples and releases; thionamides stop the organification step, iodine and lithium stop release, and the difference is why storm needs both.",
)

L['ENDO-02'] = dict(
  sub="Endocrine → Thyroid → T3 vs T4",
  step=1,
  intro="Still in step 1: the gland secretes mostly T4, but T3 is the hormone that acts. Where T3 comes from explains why blocking peripheral conversion is a treatment target in storm.",
  parts=[
    ('a', "**T3: 20–25% from the gland, 75–80% from peripheral conversion (liver, kidney); T4: only from the gland.** Because most T3 is made outside the thyroid, drugs that block conversion (PTU, propranolol, steroids) lower the active hormone even though they do not touch the gland."),
    ('b', "**Half-life: T3 about 1 day, T4 about 7 days.** T4’s long half-life is why a change in thyroxine dose takes weeks to reach steady state, and why a T4 load is used in myxoedema coma (ENDO-12)."),
    ('c', "**T3 is 3–4 times as potent as T4.** T3 binds the nuclear receptor with higher affinity; this is also why IV T3 carries the higher cardiac risk (ENDO-12)."),
    ('d', "**Free fraction: 0.2% (T3) and 0.02% (T4) in the notes.** Standard teaching gives about 0.3% and 0.03%. Either way, almost all hormone is bound, and only the free part acts."),
    ('e', "**Bound to TBG, albumin and transthyretin: less binding protein, more free hormone.** Drugs that displace hormone from TBG, such as aspirin, raise the free level; this is why paracetamol is the antipyretic in storm (ENDO-09)."),
  ],
  mimic=[
    ("Total vs free hormone", "Total T4 moves with TBG (high in pregnancy and on oestrogen); free T4 reflects thyroid status."),
  ],
  traps=[
    ("“Most circulating T3 is secreted by the thyroid”", "Only 20–25%; the rest comes from deiodination of T4 in the tissues."),
  ],
  decode=[
    ("Which hormone is more potent and which has the longer half-life? [pattern]", "T3 is 3–4 times more potent; T4 lasts about 7 days."),
  ],
  punch="T4 is the long-lived prohormone from the gland, T3 the potent hormone made mostly in the tissues, and only the free fraction of either acts.",
)

L['ENDO-03'] = dict(
  sub="Endocrine → Thyroid → Test patterns and causes of thyrotoxicosis",
  step=1,
  intro="Step 1 ends with reading the tests. TSH changes far more than free T4 for the same change in thyroid status, so TSH places the problem first and free T4 confirms it. The three linked questions test how low TSH goes, which drug causes thyroiditis, and what pregnancy does to TSH.",
  parts=[
    ('a', "**Primary hyperthyroid: TSH low, T3 and T4 high.** In overt disease TSH is not just low but undetectable (under 0.01–0.05 mIU/L on modern assays); a low but measurable TSH of 0.1–0.4 suggests subclinical disease, non-thyroidal illness, or dopamine or steroids. The exception is a TSH-secreting adenoma, where TSH is normal or high with high hormone."),
    ('b', "**Primary hypothyroid: TSH high, T3 and T4 low.** The failing gland loses feedback, so the pituitary drives TSH up."),
    ('c', "**Secondary (pituitary) hypothyroid: TSH low, T3 and T4 low.** TSH may also be ‘normal’, which is inappropriate for a low T4 (ENDO-13 h). This is why a normal TSH cannot exclude hypothyroidism in pituitary disease or myxoedema coma from pituitary failure (ENDO-11)."),
    ('d', "**Subclinical hyper- or hypothyroid: TSH low or high, hormone normal.** The pituitary detects a change before free T4 leaves its reference range."),
    ('e', "**Overproduction: Graves’, toxic multinodular goitre, TSH-secreting adenoma.** These glands make new hormone, so thionamides work."),
    ('f', "**Leak from destruction: subacute, lymphocytic or Riedel thyroiditis, radiation.** Stored hormone leaks from damaged follicles, so thionamides do not help and β-blockers carry the patient; the thyrotoxic phase is usually followed by hypothyroidism. Riedel thyroiditis is a fibrosing disease and does not usually cause thyrotoxicosis (FLAG). Lithium causes painless thyroiditis in the same way, as do checkpoint inhibitors and interferon-α."),
    ('g', "**Drugs: thyroxine, amiodarone, iodinated contrast; metastatic thyroid cancer.** Amiodarone causes two types: iodine-induced overproduction (type 1) and destructive thyroiditis (type 2). Lithium mostly causes hypothyroidism and goitre by blocking release, but also silent thyroiditis."),
  ],
  table=dict(title="TSH in the stems", head=["Setting", "TSH", "Why"], rows=[["Overt primary hyperthyroidism", "**undetectable**", "full feedback suppression"], ["Subclinical, illness, dopamine, steroids", "low but detectable (0.1–0.4)", "partial suppression"], ["First trimester", "**falls, often under 0.1**", "hCG stimulates the TSH receptor"], ["TSH-secreting adenoma", "normal or high", "the source is the pituitary"]]),
  mimic=[
    ("Graves’ vs painless thyroiditis", "Graves’: new synthesis, high uptake, eye signs, responds to thionamides. Thyroiditis: leak, low uptake, self-limiting, thionamides useless."),
    ("Gestational fall in TSH vs hyperthyroidism", "First trimester: TSH low, free T4 near normal, no goitre or eye signs, peaks at 10–12 weeks. Graves’: high free T4, goitre, antibodies."),
  ],
  traps=[
    ("“TSH is low in true hyperthyroidism”", "Only 18% picked ‘undetectable’; most chose ‘low’. Both are true, but when both are offered the exam wants the more precise ‘undetectable’, which is the finding in overt disease."),
    ("“Prolactin or cortisol falls in early pregnancy”", "Both rise through pregnancy (46% right). TSH is the hormone that falls in the first trimester, because hCG shares the α-subunit and weakly stimulates the TSH receptor; vasopressin is unchanged despite placental vasopressinase."),
    ("“An SSRI or bupropion caused her thyroiditis”", "Lithium is the drug (68% right). The DocT stem calls it a medicine ‘for depression’ and adds joint pain and a rash that fit no option; lithium is still the best answer."),
  ],
  decode=[
    ("Characteristic TSH in true (overt) hyperthyroidism [DocT QBank]", "Undetectable, over ‘low’."),
    ("Thyroiditis after a new psychiatric drug [DocT QBank]", "Lithium: painless thyroiditis as well as blocked release."),
    ("Which hormone decreases in early pregnancy? [DocT GT]", "TSH, because of hCG."),
  ],
  punch="TSH is the amplified signal: undetectable in overt primary hyperthyroidism, high in primary hypothyroidism, and low or inappropriately normal when the pituitary itself fails.",
)

L['ENDO-04'] = dict(
  sub="Endocrine → Thyroid storm → Epidemiology, triggers, mechanism",
  step=2,
  intro="Step 2 is how ordinary thyrotoxicosis becomes storm. The same hormone levels that a patient was tolerating become lethal when a trigger adds stress, catecholamines or a sudden rise in free hormone. The linked questions test the commonest trigger and why the heart is so vulnerable.",
  parts=[
    ('a', "**About 1% of hospitalised hyperthyroid patients; women 3:1; mortality about 10% (multi-organ failure).** Recent data are close to the card: in the US National Inpatient Sample (2016–2020) storm was 2.5% of thyrotoxicosis admissions and about 72% of patients were women (roughly 2.5:1). The Japanese national survey (Akamizu 2012) found mortality of about 11%, with multiple organ failure the commonest cause of death and heart failure next; reviews quote 10–25%, while recent US in-hospital mortality is lower, about 3–5%. Population incidence is only about 0.6–1 per 100,000 a year, so most residents meet it as an infection or post-operative case."),
    ('b', "**Triggers: stopping antithyroid drugs, surgery (especially thyroidectomy), neck trauma, infection, pregnancy and delivery, DKA, stress, stroke, PE, intense exercise, tyrosine kinase inhibitors, even dental extraction.** In a known, treated patient, stopping the thionamide is the leading cause. In a patient whose disease was never diagnosed, infection is the commonest trigger, which is why fever in storm must be treated as possible sepsis too."),
    ('c', "**Mechanism: more free hormone (increased release, reduced TBG binding), more adrenergic receptors, more peripheral conversion.** Free T4 and T3 are no higher in storm than in uncomplicated thyrotoxicosis in the Japanese series, so the switch is not just more hormone. It is the tissue response: thyroid hormone up-regulates β₁-receptors, so the catecholamine surge of infection or surgery acts on a primed heart, and acute illness lowers binding proteins and frees more hormone."),
  ],
  mimic=[
    ("Storm vs sepsis with thyrotoxicosis", "Both have fever, tachycardia and confusion; a known or obvious thyrotoxic patient with organ dysfunction out of proportion is storm, and the infection is its trigger, not an alternative diagnosis."),
  ],
  traps=[
    ("“Lack of response to β-blockers” or “antibiotic interaction” is the concern with pneumonia", "Only 56% chose increased sensitivity to catecholamines. Storm has up-regulated β₁-receptors, so sepsis, β-agonist nebulisers or high-dose pressors trigger AF, ischaemia or high-output failure. Give propranolol early; switch to short-acting esmolol if the ejection fraction is low (ENDO-08)."),
    ("“Sepsis with secondary thyrotoxicosis”", "Sepsis does not cause thyrotoxicosis; it lowers T3 (non-thyroidal illness). An untreated hyperthyroid patient with fever, delirium and vomiting after pneumonia is storm precipitated by infection (88% right)."),
  ],
  decode=[
    ("Commonest precipitant in undiagnosed hyperthyroidism [DocT QBank]", "Infection (92% right); in treated patients, stopping antithyroid drugs."),
    ("Storm with pneumonia: what to be cautious of [DocT QBank]", "Increased sensitivity to catecholamines."),
    ("Untreated hyperthyroid, fever, confusion, vomiting after pneumonia, TSH undetectable [DocT GT]", "Thyroid storm precipitated by infection."),
  ],
  punch="Storm is a trigger acting on a primed heart, not a higher hormone level: infection leads in the undiagnosed, stopping the thionamide in the treated, and mortality is still about one in ten.",
)

L['ENDO-05'] = dict(
  sub="Endocrine → Thyroid storm → Clinical features",
  step=2,
  intro="Step 2 continues with what storm looks like. Every system shows the effect of too much hormone acting on primed tissue; the features that separate storm from plain thyrotoxicosis are fever, altered mentation, heart failure and liver dysfunction. The linked questions test the cardinal symptom and the mimics.",
  parts=[
    ('a', "**Fever, hyperthermia; profuse sweating, flushed skin.** Hyperpyrexia is the defining feature (98% right): heat production rises with metabolic rate faster than sweating can lose it. The score gives it up to 30 points (ENDO-06)."),
    ('b', "**CNS: anxiety, agitation, delirium, up to coma.** Altered mentation is what makes the Japanese criteria definite (ENDO-07) and scores up to 30 on Burch–Wartofsky (ENDO-06), because it marks storm rather than compensated thyrotoxicosis."),
    ('c', "**CVS: tachycardia, especially AF; wide pulse pressure; heart failure up to cardiogenic shock; Lerman–Means scratch.** High output with low systemic resistance widens the pulse pressure. Prolonged tachycardia and AF can cause a tachycardia cardiomyopathy with a low ejection fraction, which changes the choice of β-blocker (ENDO-08)."),
    ('d', "**GI-hepatic: diarrhoea, nausea, vomiting, jaundice.** Hepatic congestion from heart failure and direct hepatotoxicity raise bilirubin; unexplained jaundice scores 20 and is a poor sign."),
    ('e', "**Tachypnoea, tremor.** High CO₂ production and oxygen demand drive ventilation."),
    ('f', "**Labs: high free T4/T3, TSH undetectable (under 0.1 mIU/L).** Hormone levels do not separate storm from uncomplicated thyrotoxicosis, so the diagnosis rests on the clinical picture and a score."),
  ],
  mimic=[
    ("Storm vs sepsis", "Both: fever, tachycardia, delirium, shock. Send TSH and free T4 with cultures; a suppressed TSH with high free T4 points to storm, and both can coexist."),
    ("Storm vs adrenal crisis", "Adrenal crisis: shock, vomiting, confusion, hyponatraemia, hyperkalaemia. Hydrocortisone treats both, which is why it is given early in storm."),
    ("Storm vs NMS, serotonin syndrome, phaeochromocytoma, sympathomimetic toxicity", "NMS: rigidity, high CK, antipsychotic; serotonin syndrome: clonus; phaeochromocytoma: paroxysms, hypertension, high metanephrines; sympathomimetics: the history. TSH is normal in all."),
  ],
  traps=[
    ("“Sepsis” alone as the mimic of storm", "The keyed answer is both sepsis and adrenal insufficiency (65% right). Storm has no confirmatory test, so check a cortisol and give hydrocortisone, which covers both."),
    ("“Palpitations and arrhythmia are part of the Diamond triad”", "The Diamond triad of Graves’ disease is exophthalmos, pretibial myxoedema and thyroid acropachy (Marrow)."),
  ],
  decode=[
    ("Which condition mimics storm and makes diagnosis hard? [DocT QBank]", "Both sepsis and adrenal insufficiency."),
    ("Primary symptom that characterises storm [DocT QBank]", "Hyperpyrexia."),
    ("Untreated hyperthyroid, fever, tachycardia, confusion, vomiting after pneumonia [DocT GT]", "Storm precipitated by infection."),
    ("Diamond triad of thyrotoxicosis includes all except [Marrow]", "Palpitations and arrhythmias."),
  ],
  punch="Storm is thyrotoxicosis plus fever, a changed mind, a failing heart or a yellow liver; hormone levels do not decide it, so think of sepsis and adrenal crisis alongside it.",
  extra=[dict(q="What is the Diamond triad?", a="Exophthalmos, pretibial myxoedema and thyroid acropachy (clubbing with periosteal new bone): the extrathyroidal signs of Graves’ disease.")],
)

L['ENDO-06'] = dict(
  sub="Endocrine → Thyroid storm → Burch–Wartofsky point scale",
  step=3,
  intro="Step 3 turns the clinical picture into a number. The Burch–Wartofsky scale (1993) gives points for each organ system so that two clinicians call the same patient the same way.",
  parts=[
    ('a', "**Temperature (°F): 99–99.9 scores 5, then +5 per degree up to 104 or more: 30.** 99 °F is about 37.2 °C and 104 °F is 40 °C."),
    ('b', "**Heart rate: 99–109 scores 5, then +5 per 10 up to 140 or more: 25; AF: +10.** Reproductions of the 1993 table differ: some print the first band as 99–109, others (MDCalc among them) as 90–109; the bands above 110 and the scoring are the same in both. The original scale scores AF as its own item; some reproductions fold it into heart failure."),
    ('c', "**Heart failure: pedal oedema 5, bibasal rales 10, pulmonary oedema 15.**"),
    ('d', "**CNS: agitation 10; delirium, psychosis or lethargy 20; seizure or coma 30.**"),
    ('e', "**GI-hepatic: diarrhoea, vomiting or pain 10; unexplained jaundice 20.**"),
    ('f', "**Precipitant: present 10; absent 0.** The card corrects the notes, which printed it the other way round."),
    ('g', "**Under 25: unlikely; 25–44: impending storm; 45 or more: thyroid storm.** The scale is sensitive but over-calls; the Japanese criteria are more specific (ENDO-07). A score of 25–44 still deserves treatment if the patient is sick."),
  ],
  mimic=[
    ("Burch–Wartofsky vs Japanese criteria", "Burch–Wartofsky adds points and does not require proven thyrotoxicosis; the Japanese criteria require it and use combinations of features (ENDO-07)."),
  ],
  traps=[
    ("“A score of 30 is thyroid storm”", "25–44 is impending storm; storm needs 45 or more (ENDO-13 d)."),
  ],
  decode=[
    ("A score of 38: what does it mean? [pattern]", "Impending storm (25–44)."),
    ("Which single findings score 30? [pattern]", "Temperature 104 °F or more, and seizure or coma."),
  ],
  punch="Burch–Wartofsky scores temperature, pulse, heart failure, brain, gut and trigger: under 25 unlikely, 25–44 impending, 45 or more storm.",
)

L['ENDO-07'] = dict(
  sub="Endocrine → Thyroid storm → Burch–Wartofsky vs Japanese (Akamizu) criteria",
  step=3,
  intro="Still step 3: the Japan Thyroid Association criteria (Akamizu, 2012) were built from a national survey and ask a different question: given proven thyrotoxicosis, which combination of organ failures makes it storm.",
  parts=[
    ('a', "**Thyrotoxicosis: not required (Burch–Wartofsky) vs a prerequisite (Japanese).** The Japanese criteria start from a high free T4 or T3, then look for organ failure."),
    ('b', "**Format: a points score vs criteria without a score.** Definite storm (TS1) is CNS involvement plus at least one of fever, tachycardia, heart failure or GI-hepatic signs, or three of those four without CNS signs; suspected storm (TS2) is two of the four, or a TS1 picture before hormone results are available. Features clearly caused by another illness do not count."),
    ('c', "**Fever: from 37.2 °C vs 38 °C.**"),
    ('d', "**Heart rate: from 90 vs 130.** Some reproductions of Burch–Wartofsky start the first band at 90, others at 99 as on ENDO-06; either way the Japanese threshold is far higher, because it is meant to pick out storm, not thyrotoxicosis (FLAG on the mismatch between the two cards)."),
    ('e', "**AF: included vs not included.** In the Japanese criteria AF is not a separate item, but a rate of 130 or more in AF counts as tachycardia."),
    ('f', "**Heart failure: oedema to pulmonary oedema vs NYHA IV or Killip III+.** The Japanese list also accepts pulmonary oedema, rales over more than half the lung field and cardiogenic shock."),
    ('g', "**Liver: jaundice vs bilirubin over 3 mg/dL.** The only change between the first and final Japanese criteria after the national survey concerned this item, the bilirubin threshold of over 3 mg/dL."),
  ],
  mimic=[
    ("Burch–Wartofsky ‘impending’ vs Japanese TS2", "Both mark a patient who is not yet definite but needs treatment; neither should delay therapy."),
  ],
  traps=[
    ("“Burch–Wartofsky is the European score”", "It is American (Burch and Wartofsky, 1993); the notes’ label is wrong."),
  ],
  decode=[
    ("Which criteria need thyrotoxicosis as a prerequisite? [pattern]", "The Japanese (Akamizu) criteria."),
    ("Japanese heart-rate and bilirubin thresholds [pattern]", "130 per minute; bilirubin over 3 mg/dL."),
  ],
  punch="Burch–Wartofsky adds points from 37.2 °C and a pulse of 99; the Japanese criteria require proven thyrotoxicosis and count organ failures from 38 °C, 130 per minute and bilirubin over 3.",
)

L['ENDO-08'] = dict(
  sub="Endocrine → Thyroid storm → Drugs: dose and mechanism",
  step=4,
  intro="Step 4 is treatment, and this card is the most-asked in the deck (8 links). Each drug hits a different point: β-blockade at the tissue, thionamides at synthesis, iodine at release, steroids and PTU at conversion. The questions test iodine timing, why steroids are given, PTU’s mechanism and what to do when the heart is failing.",
  parts=[
    ('a', "**Propranolol: IV 1–2 mg; oral 60–80 mg 4-hourly (ATA 2016; notes 40–80 mg 6–8-hourly); blocks adrenergic effects and reduces T4→T3.** It controls the rate, tremor and agitation within hours. High doses can tip a patient with storm cardiomyopathy into shock, so start low. The JTA 2016 guideline goes further: it prefers β₁-selective drugs (landiolol or esmolol IV, bisoprolol 2.5–5 mg a day orally), does not recommend propranolol for the tachycardia, aims for a rate of 130 or less, and adds digitalis for AF. With heart failure and a low ejection fraction use a short-acting titratable β₁-blocker (esmolol 250–500 µg/kg then 50–100 µg/kg/min) that can be stopped at once, with digoxin as an add-on (it needs higher doses in thyrotoxicosis)."),
    ('b', "**PTU (preferred): 500–1000 mg load, then 200–250 mg; blocks synthesis and peripheral conversion.** The primary action is blocking thyroid peroxidase (synthesis); blocking T4→T3 is the extra action that makes it the storm choice. ATA 2016 prefers PTU in storm (500–1000 mg, then 250 mg 4-hourly), and in pregnancy it is preferred in any trimester; outside storm, methimazole is used after the first trimester. The JTA 2016 guideline accepts either (methimazole 60 mg or PTU 600 mg a day) and finds methimazole no worse. After stabilisation switch to methimazole, because PTU carries the risk of severe liver injury."),
    ('c', "**Methimazole / carbimazole: 10–50 mg (scan unclear), 6-hourly; IV not in India; blocks synthesis.** ATA 2016 gives 60–80 mg a day and JTA 2016 60 mg a day (IV methimazole 30 mg a day in Japan), so the card’s range is unclear and probably low (FLAG). It is acceptable instead of PTU, but give one thionamide, not both."),
    ('d', "**Lugol’s iodine / SSKI: at least 1 hour after the thionamide; Wolff–Chaikoff stops release and synthesis.** Typical doses are SSKI 5 drops (250 mg) or Lugol’s 8 drops 6-hourly. Given first, iodine would be organified into new hormone and fill the gland; with thyroid peroxidase already blocked, it only shuts off release. The JTA 2016 guideline gives iodide (about 200 mg a day) at the same time as the thionamide, but the ATA 2016 rule of at least 1 hour after is the exam answer."),
    ('e', "**Hydrocortisone: steroid of choice; reduces conversion and covers relative adrenal insufficiency.** ATA 2016 gives 300 mg IV, then 100 mg 8-hourly; JTA 2016 gives 300 mg a day, or dexamethasone 8 mg a day (2 mg 6-hourly). When asked for the main role in storm, the exam key is inhibiting T4→T3."),
    ('f', "**Lithium carbonate: 300 mg 6-hourly (rarely used); inhibits colloid proteolysis (release).** It replaces iodine when iodine cannot be given (allergy, amiodarone thyrotoxicosis); levels must be watched for toxicity. Some sources give it 8-hourly."),
    ('g', "**L-carnitine: adjuvant; blocks hormone entry to nuclei.** A peripheral antagonist with little evidence; not a core drug."),
  ],
  table=dict(title="Drug, target, and the exam answer", head=["Target", "Drug", "Exam point"], rows=[["Tissue adrenergic effects", "**propranolol**; esmolol if EF low", "first drug; also cuts T4→T3"], ["Synthesis (TPO)", "**PTU** (or methimazole)", "PTU’s main action is synthesis"], ["Release", "**iodine** ≥1 h after thionamide; lithium if no iodine", "iodine first fills the gland"], ["Conversion T4→T3", "**hydrocortisone**, PTU, propranolol", "steroid’s main role in storm"], ["Enterohepatic recycling", "cholestyramine", "adjunct"]]),
  mimic=[
    ("Esmolol infusion vs digoxin plus cautious β-blocker in storm with AF and heart failure", "Both are defensible; DocT keys digoxin plus a cautious β-blocker, while the JTA 2016 guideline uses short-acting landiolol or esmolol for fast rates in heart failure, with digitalis alongside for AF. Never full-dose propranolol or diltiazem, which is negatively inotropic."),
    ("PTU vs methimazole", "PTU blocks synthesis and conversion, so ATA 2016 prefers it in storm and in the first trimester; methimazole is longer-acting and safer for the liver (everything else), and JTA 2016 accepts it in storm too."),
  ],
  traps=[
    ("“Esmolol infusion” or “IV propranolol bolus” for storm with AF and severe heart failure", "Only 33% chose the key, digoxin plus a cautious β-blocker. Esmolol is equally supported by the JTA 2016 guideline, which prefers short-acting β₁-selective drugs; if both appear, pick the DocT key. A propranolol bolus or diltiazem can cause cardiogenic collapse."),
    ("“Steroids prevent adrenal crisis and suppress immunity”", "Covering relative adrenal insufficiency is true, but the key for the main role is inhibiting T4→T3 conversion (49% and 63% right)."),
    ("“PTU’s primary mechanism is blocking T4→T3” [NEET 2025]", "Its primary mechanism is blocking synthesis at thyroid peroxidase; blocking conversion is the additional effect."),
    ("“Methimazole is the gold standard in the second and third trimesters” in a pregnant woman in storm", "Outside storm that is true, but in storm PTU is preferred in any trimester because it also blocks conversion. Propranolol is not contraindicated in pregnancy, and iodine is never given before the thionamide."),
  ],
  decode=[
    ("Storm, PTU started: which adjunct must wait at least 1 hour? [DocT QBank, DocT GT, Marrow]", "Lugol’s solution or potassium iodide (84–85% right)."),
    ("PTU, propranolol and dexamethasone: main role of the steroid [DocT QBank, DocT GT]", "Inhibit T4→T3 conversion."),
    ("Storm at 22 weeks: which statement about drugs is right? [DocT GT]", "PTU is preferred in storm in any trimester."),
    ("Storm with AF and severe heart failure: rate control [DocT GT]", "Digoxin plus a cautious β-blocker (esmolol equally supported)."),
    ("Primary mechanism of PTU [NEET 2025]", "Reduces thyroid hormone synthesis."),
  ],
  punch="Propranolol for the tissues, a thionamide for synthesis, iodine an hour later for release, hydrocortisone for conversion; with a failing ventricle, use a β-blocker you can switch off.",
)

L['ENDO-09'] = dict(
  sub="Endocrine → Thyroid storm → Order of treatment",
  step=4,
  intro="Still step 4: the order matters as much as the drugs. The β-blocker goes first because it acts within minutes on the heart; the thionamide follows so that iodine, given an hour later, cannot feed new hormone. The six linked questions all test this sequence.",
  parts=[
    ('a', "**First line: β-blocker (propranolol) → thionamide (PTU best) → hydrocortisone.** The β-blocker controls rate and symptoms while the slower drugs act. The thionamide must be in before iodine. Hydrocortisone can go at any point."),
    ('b', "**Second line: iodine (Lugol’s, potassium or sodium iodide) → lithium → L-carnitine.** In ATA 2016 and JTA 2016 iodine is part of the standard initial regimen (ATA: an hour after the thionamide; JTA: with it), not reserved for failure (FLAG on the label). Lithium replaces it when iodine cannot be used."),
    ('c', "**Support: fluids and electrolytes, paracetamol (not aspirin, which displaces hormone from TBG), phenobarbital, furosemide and ACE inhibitor for heart failure, sedation.** Fever, sweating and vomiting cause large fluid losses. Aspirin raises the free hormone. Phenobarbital sedates and speeds hormone metabolism."),
    ('d', "**Selected: ventilation for hypoxaemia; cooling mattresses and cold packs if over 40 °C.**"),
    ('e', "**Treat the trigger.** Infection is the commonest; cultures and antibiotics go in alongside the antithyroid drugs. If there is no improvement in 24–48 hours, JTA 2016 suggests plasma exchange; emergency thyroidectomy is the last resort."),
  ],
  mimic=[
    ("Thyroid storm vs phaeochromocytoma crisis", "Storm: β-blocker first. Phaeochromocytoma: α-blocker before any β-blocker, because unopposed α-stimulation causes a hypertensive crisis."),
    ("Thyroid storm vs levothyroxine overdose", "In overdose the gland is not the source, so blocking synthesis or release does nothing (PTU, propranolol and steroids still reduce T4→T3 conversion); propranolol is the life-saving drug, with cholestyramine to bind hormone in the gut."),
  ],
  traps=[
    ("“Iodine is indicated for immediate treatment” after propranolol in post-operative storm [DocT GT]", "The key is iodine as the drug NOT indicated immediately (64% right), because it must wait an hour after the thionamide. Some argue methimazole is the odd one out because PTU is preferred and only one thionamide is given; that is weaker, since ATA 2016 and JTA 2016 both accept methimazole. On exam day, answer iodine."),
    ("“High-dose iodine” or “hydrocortisone” as the best initial treatment", "In the ileostomy patient with a pulse of 160 and a low TSH, propranolol comes first (85% right); diltiazem only if β-blockers are contraindicated."),
    ("“Lugol’s → methimazole → propranolol”", "Iodine first fills the gland with substrate. The correct order is propranolol → methimazole (or PTU) → iodine an hour later."),
  ],
  decode=[
    ("Storm on PTU: which adjunct must be delayed 1 hour? [DocT QBank, DocT GT]", "Lugol’s solution."),
    ("Post-appendicectomy storm, propranolol given: which drug is NOT for immediate use? [DocT GT]", "Iodine."),
    ("Fever, pulse 160, sepsis work-up negative, low TSH: best initial treatment [DocT GT]", "Propranolol."),
    ("Which sequence prevents worsening thyrotoxicosis? [DocT GT]", "Propranolol → methimazole → Lugol’s iodine after 1 hour."),
    ("Accidental levothyroxine overdose: first life-saving drug [Marrow]", "Propranolol."),
  ],
  punch="β-blocker, then thionamide, then iodine an hour later, with hydrocortisone, paracetamol and a hunt for the trigger; iodine before the thionamide makes storm worse.",
)

L['ENDO-10'] = dict(
  sub="Endocrine → Myxoedema coma → Definition, causes, precipitants, features",
  step=5,
  intro="Step 5 moves to the opposite failure. Myxoedema coma is long-standing hypothyroidism that decompensates when a trigger demands more than the slowed body can give; ‘coma’ is a misnomer, since most patients are obtunded rather than comatose. The linked questions test what defines it and what to avoid.",
  parts=[
    ('a', "**Decompensated severe hypothyroidism with altered mentation; prevalence 0.01%; mortality 20–50% even with treatment; TSH usually over 100 mIU/L.** Altered mental status is what separates it from ordinary hypothyroidism. It is very rare: about 0.2 cases per million a year in Western series and about 1 per million a year in Japan (the card’s 0.01% could not be traced; FLAG); Japanese national data give in-hospital mortality of about 30%. TSH is high in primary disease, but the level does not define it, and in pituitary disease it is low or normal (ENDO-11)."),
    ('b', "**Causes: Hashimoto’s, thyroidectomy, radioiodine or radiotherapy, antithyroid drugs, tyrosine kinase inhibitors; pituitary disease.** A neck scar or a history of Graves’ treated with radioiodine is the usual clue in a stem."),
    ('c', "**Precipitants: infection, cold exposure, stroke, drugs (sedatives, analgesics, amiodarone, lithium).** Hypothyroid patients clear sedatives and opioids slowly and have a blunted ventilatory drive, so a usual dose can cause respiratory arrest. Lithium both causes hypothyroidism and appears as a precipitant (Marrow)."),
    ('d', "**Features: coma, hypothermia (under 33 °C in the notes), bradycardia, non-pitting oedema, dry yellow skin, hyporeflexia, muffled heart sounds (effusion), constipation; rarely seizures.** Low T3 cuts heat production, so most patients are hypothermic; reviews define hypothermia here as below 35–35.5 °C, and the lower the temperature, the worse the prognosis. 33 °C is the notes’ figure, not a standard cut-off (FLAG). Hypothermia, hypoventilation, hyponatraemia and bradycardia together in an elderly patient in winter should prompt thyroid tests. Infection may not produce fever, so a normal temperature in a hypothyroid patient can be a sign of sepsis."),
  ],
  mimic=[
    ("Myxoedema coma vs uncomplicated hypothyroidism", "Coma: obtundation or altered mental status, plus hypothermia and organ failure. Cold intolerance and weight gain occur in both."),
    ("Myxoedema coma vs environmental hypothermia", "Both cold and slow; myxoedema has periorbital oedema, macroglossia, hyponatraemia and a high TSH, and does not rewarm normally."),
  ],
  traps=[
    ("“Elevated T3” or “cold intolerance” distinguishes coma from hypothyroidism", "Altered mental status does (87% right); T3 is low, and cold intolerance is common to both."),
    ("“Sedatives” for an agitated hypoventilating hypothyroid patient", "Not recommended (95% right): they worsen hypoventilation and are themselves a precipitant."),
  ],
  decode=[
    ("Untreated hypothyroid with respiratory depression: which intervention is NOT recommended? [DocT QBank]", "Sedatives."),
    ("What distinguishes myxoedema coma from uncomplicated hypothyroidism? [DocT QBank]", "Obtundation and altered mental status."),
    ("Elderly on lithium, 32 °C, hypotension, hyponatraemia, slow reflexes: next step [Marrow]", "Thyroid function tests, with a cortisol."),
  ],
  punch="Myxoedema coma is severe hypothyroidism plus a changed mind, usually after infection, cold or sedatives; hypothermia, hypoventilation, hyponatraemia and bradycardia are the pattern to recognise.",
)

L['ENDO-11'] = dict(
  sub="Endocrine → Myxoedema coma → Investigations",
  step=5,
  intro="Still step 5: the tests confirm the hypothyroidism and show which organs are failing. The two linked questions test the ECG and the mechanism of the hyponatraemia.",
  parts=[
    ('a', "**Thyroid: free T4 and T3 low; TSH over 100 (low or normal if pituitary).** Send TSH, free T4 and a random cortisol before treatment, but do not wait for them to treat."),
    ('b', "**ABG: hypoxaemia, hypercapnia, respiratory acidosis.** The central drive to CO₂ and hypoxia is blunted, the respiratory muscles are weak, and macroglossia and effusions add obstruction and restriction. Hypercapnia is a common reason for intubation."),
    ('c', "**Blood: hyponatraemia (high ADH), hypoglycaemia, anaemia, high CK and LDH, high transaminases, creatinine and cholesterol.** The main cause of hyponatraemia is a low cardiac output and GFR, so less filtrate reaches the diluting segments and free water cannot be excreted; non-osmotic ADH adds to it. Hypoglycaemia should prompt a search for adrenal insufficiency too."),
    ('d', "**ECG: sinus bradycardia, low voltage, long QT.** The T waves are often flattened or inverted, and DocT keys T-wave inversion as the typical finding (not printed on the card). Low voltage is worse with a pericardial effusion."),
    ('e', "**Echo: pericardial effusion, concentric LVH, reduced EF.** The effusion builds slowly and rarely causes tamponade."),
  ],
  mimic=[
    ("Hypothyroid vs SIADH hyponatraemia", "Both euvolaemic with concentrated urine; check TSH and cortisol before calling it SIADH, because both deficiencies must be excluded first."),
  ],
  traps=[
    ("“Hyperaldosteronism” or “hypercortisolism” causes hyponatraemia by reduced delivery to the diluting segment", "Hypothyroidism does (only 38% right). Hyperaldosteronism retains sodium with water and causes mild hypernatraemia; it is glucocorticoid deficiency, not excess, that impairs water excretion."),
    ("“ST elevation” or “AF” is the ECG of myxoedema", "T-wave inversion is the key (61% right). ST elevation points to infarction or pericarditis, AF to thyrotoxicosis, short QT to hypercalcaemia."),
  ],
  decode=[
    ("Typical ECG finding in myxoedema coma [DocT QBank]", "T-wave inversion; also bradycardia, low voltage, long QT."),
    ("Hyponatraemia from reduced filtrate delivery to the diluting segments [DocT QBank]", "Hypothyroidism."),
  ],
  punch="Myxoedema coma shows a slow, low-voltage heart with flat or inverted T waves, CO₂ retention, low sodium and low glucose; check cortisol in every case.",
)

L['ENDO-12'] = dict(
  sub="Endocrine → Myxoedema coma → Treatment",
  step=6,
  intro="Step 6 is treatment, the second most-asked card here (7 links). The order is the same idea as in storm: protect against what the first drug could unmask. Thyroxine speeds cortisol clearance, so a steroid goes in first; thyroxine then has to be enough to reverse the coma without overloading a heart that has been slow for months.",
  parts=[
    ('a', "**Hydrocortisone IV first: concurrent adrenal insufficiency (Schmidt’s syndrome) or panhypopituitarism.** Thyroid hormone raises metabolic rate and cortisol clearance, so it can precipitate adrenal crisis in a patient with low reserve. Draw a cortisol, then give stress doses (about 100 mg 8-hourly) until adrenal insufficiency is excluded."),
    ('b', "**IV levothyroxine: 200–400 µg load (lower if old or cardiac), then 1.6 µg/kg/day (75% while IV); ± IV liothyronine 5–20 µg, then 2.5–10 µg 8-hourly.** These are the ATA 2014 figures; 1.6 µg/kg a day at 75% is about 1.2 µg/kg a day IV, because IV T4 is fully absorbed. Some older texts load 300–500 µg. The load refills the empty pool of T4. T3 acts within hours and is 3–4 times as potent, so it raises myocardial oxygen demand fast; it is an add-on at the low end, or avoided in cardiac patients. Series link loads above 500 µg T4 or 75 µg T3 a day to more deaths."),
    ('c', "**Sodium: water restriction; 0.9% saline if Na under 120 (notes); 3% saline if severe; vaptans if not severe; sodium 8-hourly.** Symptomatic or severe hyponatraemia gets small boluses of 3% saline; the sodium is checked often because correction speeds up as thyroid hormone restores water excretion."),
    ('d', "**Ventilate for respiratory acidosis; furosemide for pulmonary oedema; passive rewarming if under 35 °C; treat infection.** Passive rewarming (blankets, warm room) is used because active external warming opens the constricted skin vessels and causes collapse in a volume-depleted patient. Protect the airway early: low consciousness, poor reflexes, ileus and macroglossia make aspiration pneumonitis the typical pulmonary complication. Give empirical antibiotics, since fever may be absent."),
    ('e', "**Complications: respiratory or cardiac failure, MI from too much T4, pulmonary oedema, shock, bleeding (acquired von Willebrand; factors V, VII, VIII, IX, X low).** Acquired von Willebrand syndrome reverses with thyroid hormone; desmopressin can be used for bleeding."),
  ],
  table=dict(title="Order in the stems", head=["Step", "What", "Why"], rows=[["1", "**airway, ventilation, cultures, antibiotics**", "hypercapnia, aspiration, hidden infection"], ["2", "**IV hydrocortisone**", "thyroxine can precipitate adrenal crisis"], ["3", "**IV levothyroxine** load, ± low-dose T3", "refill the T4 pool; T3 strains the heart"], ["Support", "passive rewarming, sodium, glucose", "active warming causes collapse"], ["Avoid", "**sedatives**, iodine, insulin", "worse hypoventilation; not relevant"]]),
  mimic=[
    ("Steroid first: myxoedema coma vs thyroid storm", "In myxoedema coma hydrocortisone precedes thyroxine to prevent adrenal crisis; in storm it is part of the first line to cut conversion and cover the adrenals. Both are ‘hydrocortisone early’."),
    ("Passive vs active rewarming", "Myxoedema: passive. Accidental hypothermia with arrest: active core rewarming."),
  ],
  traps=[
    ("“Active rewarming” or “insulin” after starting IV levothyroxine [DocT GT]", "Hydrocortisone is the key (62% right). Active external rewarming risks vasodilatory collapse, and insulin has no role; iodine belongs to hyperthyroidism."),
    ("“Hypoglycaemia” or “respiratory failure” is the main concern with T3", "Cardiovascular instability is (87% right): arrhythmia, angina or infarction from a sudden rise in oxygen demand."),
    ("“Sedatives” in a hypoventilating hypothyroid patient", "Never: they deepen hypoventilation (95% right)."),
    ("“Thyroxine before hydrocortisone” [Marrow]", "Steroid first; giving thyroxine first can precipitate adrenal crisis (ENDO-13 g)."),
  ],
  decode=[
    ("Myxoedema coma: immediate medical intervention [DocT QBank]", "IV hydrocortisone."),
    ("Which therapy should be started in all patients before thyroid hormone? [DocT GT]", "IV hydrocortisone."),
    ("Intubated, on IV levothyroxine and antibiotics: additional therapy [DocT GT]", "Hydrocortisone."),
    ("Most concerning complication of T3 therapy [DocT QBank]", "Cardiovascular instability."),
    ("Complication commonly associated with myxoedema coma [DocT QBank]", "Aspiration pneumonitis."),
    ("Lithium-induced myxoedema coma, hypotensive despite fluids [Marrow]", "IV hydrocortisone, then levothyroxine."),
  ],
  punch="Secure the airway, give hydrocortisone, then load IV thyroxine at 200–400 µg with T3 only in small doses; rewarm passively, correct sodium slowly, and give no sedatives.",
)

L['ENDO-13'] = dict(
  sub="Endocrine → Thyroid emergencies → True/false sweep",
  step=6,
  intro="The sweep closes the deck by retesting the points the questions turn on: the critical step of synthesis, iodine timing, PTU’s second action, score thresholds, the antipyretic, myxoedema labs, steroid order and secondary hypothyroidism.",
  parts=[
    ('a', "**True: organification by TPO is the critical step.** It is where thionamides act (ENDO-01)."),
    ('b', "**False: iodine is given at least 1 hour AFTER the thionamide.** Given first it becomes substrate for new hormone (ENDO-08)."),
    ('c', "**True: PTU also blocks peripheral T4→T3 conversion.** That is why it is preferred in storm, though its primary action is on synthesis."),
    ('d', "**False: storm needs 45 or more.** 30 is impending storm (ENDO-06)."),
    ('e', "**False: paracetamol, because aspirin frees hormone from TBG.**"),
    ('f', "**True: myxoedema coma causes hyponatraemia and hypoglycaemia.** Low GFR and ADH cause the first; low gluconeogenesis and possible adrenal insufficiency the second (ENDO-11)."),
    ('g', "**False: steroid first.** Thyroxine speeds cortisol clearance and can precipitate adrenal crisis (ENDO-12)."),
    ('h', "**False: TSH is low or normal in secondary hypothyroidism.** The pituitary cannot respond to the low T4 (ENDO-03)."),
  ],
  mimic=[
    ("Storm order vs myxoedema order", "Storm: β-blocker, thionamide, iodine an hour later, steroid. Myxoedema: steroid, then thyroxine."),
  ],
  traps=[
    ("“Aspirin for fever in storm”", "It displaces T4 and T3 from TBG and raises free hormone; use paracetamol and cooling."),
  ],
  decode=[
    ("Statements on storm and myxoedema treatment order [pattern]", "Iodine after the thionamide; steroid before thyroxine."),
  ],
  punch="Iodine after the thionamide, steroid before thyroxine, paracetamol not aspirin, 45 for storm, and a low or normal TSH when the pituitary fails.",
)

FLAGS = {}
FLAGS['ENDO-03'] = "Riedel thyroiditis is listed as a cause of destructive thyrotoxicosis; it is a fibrosing thyroiditis that is usually euthyroid or hypothyroid and is not a recognised cause of thyrotoxicosis. Card table ‘secondary hypothyroid: TSH low’ is better ‘low or inappropriately normal’ (the sweep, ENDO-13 h, says so)."
FLAGS['ENDO-04'] = "‘1% of hospitalised hyperthyroid patients’ is an older figure; US National Inpatient Sample 2016–2020 gives 2.5% of thyrotoxicosis admissions, with about 72% women (close to the card’s 3:1). Mortality ‘about 10%’ matches the Japanese survey (10.7–11%); reviews quote 10–25%, recent US in-hospital mortality is about 3–5%. Not wrong for the exam."
FLAGS['ENDO-07'] = "Heart rate row ‘From 90’ for Burch–Wartofsky does not match ENDO-06 (99–109 scores 5). Both versions circulate: reproductions citing the 1993 paper print 99–109, MDCalc prints 90–109. Neither card is clearly wrong; the deck is internally inconsistent."
FLAGS['ENDO-08'] = "Methimazole ‘10–50 mg, 6-hourly’ (scan unclear): ATA 2016 gives 60–80 mg a day, JTA 2016 60 mg a day. Lithium ‘300 mg 6-hourly’: some sources give 8-hourly. ‘PTU (preferred)’ is the ATA 2016 position; JTA 2016 accepts methimazole equally. Iodine ‘at least 1 h after’ is ATA 2016; JTA 2016 gives iodide with the thionamide. JTA 2016 prefers β₁-selective blockers (landiolol, esmolol, bisoprolol) and does not recommend propranolol for the tachycardia. The GT5 key (digoxin plus cautious β-blocker for storm with AF and heart failure) stands, but an esmolol infusion is equally supported; the card-layer note’s ‘JTA: landiolol/esmolol when Killip ≥III’ is a simplification (JTA uses them for rates ≥150 in Killip ≤III and considers them in Killip IV, with digitalis for AF)."
FLAGS['ENDO-10'] = "Prevalence ‘0.01%’ could not be traced; published incidence is about 0.22 per million a year (Western series) and 1.08 per million a year (Japan). Hypothermia ‘under 33 °C’ is not a standard cut-off; reviews use below 35–35.5 °C. ‘TSH usually over 100’ is not a defining criterion (TSH is high in primary disease, low or normal in central)."
FLAGS['ENDO-09'] = "Card calls iodine ‘second line’; in ATA 2016, JTA 2016 and most guidelines iodine is part of the standard initial regimen, given at least 1 h after the thionamide. The qpack note on the GT2o ‘NOT indicated for immediate treatment’ question argues for methimazole (C); the key, iodine (A), is the better answer and is taught as such."
FLAGS['ENDO-11'] = "Card ECG row omits T-wave flattening or inversion, which DocT keys as the typical ECG finding of myxoedema coma; the card’s ‘hyponatraemia (high ADH)’ gives only the secondary mechanism (DocT keys reduced filtrate delivery from low cardiac output and GFR)."
