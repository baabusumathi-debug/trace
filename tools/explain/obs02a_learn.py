# OBS02A — Explain v3 ("Learn" depth): hypertension in pregnancy — definitions and classes, pathophysiology, acute antihypertensives, fluids and principles, when to deliver,
# eclampsia, the magnesium regimen, magnesium toxicity, how magnesium works and Magpie, other causes of a seizure in pregnancy (PRES), HELLP, acute fatty liver, HELLP vs fatty liver.
# No mnemonics or hooks. Driven by the real questions in qpack/OBS02A.md (HELLP criteria OBS-27 asked 9 times; OBS-16 classes and OBS-18 antihypertensives 5 each; OBS-19 and OBS-26 4 each).
# Fields as TOX01, plus SPINE, PRIMER and step. Table cards (no lettered parts) take parts a, b, c… in the order of the card’s rows or lines.
# Figures checked online on 12 Nov 2026:
#  - ACOG Practice Bulletin 222 (2020), read in full: BP ≥140/90 twice ≥4 h apart after 20 weeks; proteinuria ≥300 mg/24 h, PCR ≥0.3 or dipstick 2+; severe features (≥160/110, platelets <100,000,
#    transaminases ≥2× normal or severe persistent RUQ/epigastric pain, creatinine >1.1 mg/dL or doubled, pulmonary oedema, headache unresponsive to medication, visual disturbance);
#    up to 50% of gestational hypertension progresses (more if onset <32 weeks); delivery at ≥37+0 without and ≥34+0 with severe features; Box 4 conditions precluding expectant care (includes HELLP);
#    labetalol 10–20 mg IV then 20–80 mg q10–30 min, max 300 mg, or 1–2 mg/min, onset 1–2 min; hydralazine 5 mg IV/IM then 5–10 mg q20–40 min, max 20 mg, or 0.5–10 mg/h, onset 10–20 min;
#    nifedipine IR 10–20 mg, repeat in 20 min, then q2–6 h, max 180 mg/day, onset 5–10 min; treat severe BP persisting 15 min, within 30–60 min; magnesium 4–6 g over 20–30 min then 1–2 g/h
#    until 24 h postpartum; IM 10 g then 5 g q4h; toxicity at about 9 / 12 / 30 mg/dL (7 / 10 / 25 mEq/L); creatinine 1.0–1.5 or oliguria → 1 g/h; recurrent seizure 2–4 g over 5 min;
#    no consensus on magnesium without severe features; 20–38% of eclampsia without classic warning signs; HELLP = LDH ≥600, AST/ALT >2× normal, platelets <100,000, up to 15% without
#    hypertension or proteinuria, steroids not shown to help the mother; aspirin 81 mg from 12–28 weeks (ideally before 16); vitamins C and E do not prevent pre-eclampsia; aggressive fluid is dangerous.
#  - Calcium gluconate 10% 10 mL (1 g) IV over 3 minutes; therapeutic magnesium 5–9 mg/dL (4–7 mEq/L) (ObG Project summary of ACOG 222).
#  - Magpie (Lancet 2002): 10,141 women, 33 countries; eclampsia 0.8% vs 1.9%, 58% lower risk (95% CI 40–71), RR 0.42, NNT 91; maternal death RR 0.55 (0.26–1.14, not significant);
#    abruption 2.0% vs 3.2%; side effects 24% vs 5%.
#  - HELLP review (Haram, BMC Pregnancy Childbirth 2009): 0.5–0.9% of pregnancies, 10–20% of severe pre-eclampsia; Tennessee: platelets ≤100, AST ≥70, LDH ≥600 (bilirubin ≥1.2 mg/dL supports
#    haemolysis); Mississippi class 1 ≤50, class 2 >50–100, class 3 >100–150; about 30% postpartum; hypertension and proteinuria absent in 10–20%; subcapsular haematoma about 1–2%.
#  - CMQCC/Sibai algorithm for severe pre-eclampsia <34 weeks (source of the card OBS-20/21 tables): steroids and a 24–48 h delay for stable HELLP from viability to 33+6 weeks.
# Second check, 12 Nov 2026 (reviewer), confirmed online: NICE NG133 ‘limit maintenance fluids to 80 ml/hour unless there are other ongoing fluid losses (for example, haemorrhage)’ in severe
#    pre-eclampsia, no volume expansion except up to 500 mL crystalloid with antenatal hydralazine, magnesium 4 g over 5–15 min then 1 g/h for 24 h, recurrent seizure 2–4 g over 5–15 min;
#    SMFM Consult Series 52 (2020): deliver at 33–34 weeks for absent and 30–32 weeks for reversed umbilical end-diastolic flow; ASFA 2023: plasma exchange category III (grade 2C) for severe
#    pregnancy-associated thrombotic microangiopathy/HELLP, category I (grade 1A) for TTP; Swansea criteria: six or more of 14 features with no other explanation.
# Still from standard teaching and memory (worded softly in the text): the post-treatment pressure range of about 140–150/90–100 (ACOG Committee Opinion 767; earlier ACOG text said 140–160/90–100),
# Collaborative Eclampsia Trial 1995 (52% fewer recurrent seizures than diazepam, 67% fewer than phenytoin), PRES in most imaged eclampsia, the timing percentages on card OBS-22 and the
# mortality figures on card OBS-21 (not restated in the explanation).

SPINE = [
  ("Naming the hypertensive disorder", "The 20-week line separates chronic from pregnancy-induced hypertension, and proteinuria or any organ dysfunction turns gestational hypertension into pre-eclampsia, with 160/110 or organ injury marking severe disease."),
  ("A sick placenta injures endothelium", "Shallow placentation leaves an ischaemic placenta that releases anti-angiogenic factors, and the resulting endothelial dysfunction explains the hypertension, the proteinuria, the leak and the low platelets."),
  ("Lower pressure, restrict fluid, deliver", "Delivery is the only cure, so until then severe pressure is lowered to prevent stroke, fluid is held to 80 mL/hour, and the timing of delivery is set by gestation and by which organ is failing."),
  ("Eclampsia and magnesium", "A seizure in pregnancy is eclampsia until proven otherwise and is treated and prevented with magnesium, whose toxicity is tracked at the bedside by the knee jerk, the respiratory rate and the urine output."),
  ("When the seizure is something else", "Most eclamptic brains show the posterior vasogenic oedema of PRES, and a seizure that does not fit needs imaging for venous thrombosis, haemorrhage or infection."),
  ("The liver: HELLP and fatty liver", "HELLP is haemolysis, raised enzymes and low platelets with a working liver, acute fatty liver is true liver failure with hypoglycaemia and a high INR and ammonia, and both are treated by delivery."),
]

PRIMER = "Normal pregnancy lowers blood pressure in the first half, because systemic vascular resistance falls, and raises plasma volume by almost half, so a pressure of 140/90 in the second half is abnormal for a pregnant woman even though it looks mild. The spiral arteries that feed the placenta are normally remodelled into wide, low-resistance channels by about 20 weeks, which is why 20 weeks is the dividing line in every definition in this deck. The placenta has no autoregulation, so its flow follows maternal pressure; this is why blood pressure is lowered in a controlled way and never to normal. Doses and cut-offs here follow ACOG’s 2020 bulletin, which the examiners’ keys use, with ISSHP and NICE where they differ."

L = {}

L['OBS-15'] = dict(
  sub="Obstetrics → Hypertensive disorders → Definition of pre-eclampsia",
  step=1,
  intro="Step 1 is about naming the disorder correctly, and it starts with the definition every later card relies on. Pre-eclampsia is new hypertension after 20 weeks plus evidence that an organ is affected; proteinuria is the usual evidence but it is no longer the only one. The two linked questions test the timing rule and the line between severe pre-eclampsia and eclampsia.",
  parts=[
    ('a', "**Systolic 140 or more or diastolic 90 or more, on two occasions 4 hours apart.** Two readings are needed because a single high reading is often anxiety or measurement error. The exception is the severe range, 160/110 or more: that can be confirmed within minutes so that treatment is not delayed (OBS-18)."),
    ('b', "**After 20 weeks, in a previously normotensive woman.** Placental disease cannot show before the placenta is fully formed, so hypertension found before 20 weeks was there before pregnancy and is chronic (OBS-16). In the DocT stem the phrase ‘normal blood pressure before 20 weeks’ is what excludes chronic hypertension."),
    ('c', "**300 mg or more in 24 hours.** ACOG accepts a protein/creatinine ratio of 0.3 or more, or dipstick 2+ if nothing quantitative is available. The injured glomerular endothelium leaks protein (OBS-17)."),
    ('d', "**New hypertension with any one of: platelets under 100,000; creatinine over 1.1 or doubled; transaminases doubled; pulmonary oedema; cerebral or visual symptoms.** Since 2013 any one of these makes the diagnosis without proteinuria, because some women develop organ injury before the kidney leaks. The cerebral symptom ACOG means is a new headache that does not respond to medication. The same list, with a pressure of 160/110 or more, defines severe features."),
    ('e', "**Pre-eclampsia plus seizures.** A generalised seizure with no other cause moves the label from pre-eclampsia to eclampsia, whatever the pressure (OBS-22). Headache, visual disturbance and hyperreflexia without a seizure are still severe pre-eclampsia."),
  ],
  mimic=[
    ("Pre-eclampsia vs gestational hypertension", "Both are new hypertension after 20 weeks. Gestational hypertension has no proteinuria and no organ dysfunction; either one makes it pre-eclampsia."),
    ("Severe pre-eclampsia vs eclampsia", "Severe pre-eclampsia: 160/110 or organ injury, including headache and visual symptoms. Eclampsia: a seizure has occurred."),
  ],
  traps=[
    ("“Eclampsia” for headache, hyperreflexia and visual disturbance", "These are warning symptoms; without a seizure the answer is severe pre-eclampsia (DocT GT)."),
    ("“Proteinuria of 6 g/day makes it severe”", "The amount of proteinuria was dropped from the severity criteria in 2013. In the DocT stem the severity comes from BP 170/115, creatinine 1.9, headache, visual symptoms and right upper quadrant pain."),
    ("“Mild” or “moderate” pre-eclampsia as an answer", "Current classification has only two grades: with and without severe features."),
    ("“No proteinuria, so it cannot be pre-eclampsia”", "Proteinuria is no longer required if any listed organ feature is present."),
  ],
  decode=[
    ("Primigravida at 32 weeks, new BP 170/110, 3+ proteinuria, normal BP before 20 weeks [DocT GT]", "Pre-eclampsia: new after 20 weeks plus proteinuria. Chronic hypertension needs onset before 20 weeks; gestational hypertension has no proteinuria."),
    ("35 weeks, BP 170/115, headache, hyperreflexia, visual disturbance, creatinine 1.9, RUQ pain — classify [DocT GT]", "Severe pre-eclampsia; no seizure, so not eclampsia."),
    ("[pattern] New hypertension at 30 weeks, no proteinuria, platelets 80,000", "Pre-eclampsia (with severe features): organ dysfunction replaces proteinuria."),
  ],
  punch="Pre-eclampsia is new hypertension of 140/90 after 20 weeks with either proteinuria of 300 mg/day or any one organ feature; 160/110 or organ injury makes it severe, and only a seizure makes it eclampsia.",
)

L['OBS-16'] = dict(
  sub="Obstetrics → Hypertensive disorders → The five classes",
  step=1,
  intro="Step 1 continues with the whole classification. Two questions sort every hypertensive pregnant woman: was the pressure high before 20 weeks, and is there proteinuria or organ dysfunction? Five linked questions test this table, and the one most often missed (49% right) asks what makes chronic hypertension ‘essential’.",
  parts=[
    ('a', "**Chronic hypertension: present before pregnancy or before 20 weeks, or persisting more than 12 weeks after delivery.** The figure the card was unsure of is 12 weeks; it is the Marrow key. Pregnancy-induced hypertension has gone by 12 weeks postpartum, so anything still present was chronic all along. Chronic hypertension is then called essential when there are risk factors for primary hypertension (family history, obesity, diabetes, older age) and no clue to a secondary cause such as renal disease, phaeochromocytoma or coarctation."),
    ('b', "**Gestational hypertension: after 20 weeks, no proteinuria or organ dysfunction.** It is a provisional label. ACOG states that up to half of these women later develop proteinuria or organ dysfunction and so become pre-eclamptic, more often when the hypertension starts before 32 weeks; DocT’s option says ‘up to 40%’. It resolves by 12 weeks postpartum. If the pressure reaches 160/110 it is managed exactly as severe pre-eclampsia, including magnesium."),
    ('c', "**Pre-eclampsia: after 20 weeks, with proteinuria or organ dysfunction.** See OBS-15 for the numbers."),
    ('d', "**Superimposed pre-eclampsia: chronic hypertension that acquires proteinuria or severe features.** In a woman who already has proteinuria from renal disease, the clues are a sudden rise in pressure or proteinuria, or new low platelets or raised transaminases."),
    ('e', "**Eclampsia: seizures.** New generalised seizures in a woman with a hypertensive disorder of pregnancy, with no other cause (OBS-22)."),
  ],
  table=dict(title="Sorting a stem", head=["Onset", "Proteinuria or organ dysfunction", "Label"], rows=[["Before 20 weeks", "no", "**chronic hypertension**"], ["Before 20 weeks", "new, or sudden worsening", "**superimposed pre-eclampsia**"], ["After 20 weeks", "no", "**gestational hypertension**"], ["After 20 weeks", "yes", "**pre-eclampsia**"], ["Any", "seizure", "**eclampsia**"]]),
  mimic=[
    ("Chronic vs gestational hypertension", "Chronic: found before 20 weeks or still present 12 weeks after delivery. Gestational: appears after 20 weeks and has gone by 12 weeks postpartum."),
    ("Essential vs secondary chronic hypertension", "Essential: family history, obesity, no other findings. Secondary: young with very high pressure, renal disease, hypokalaemia, paroxysms, radio-femoral delay."),
  ],
  traps=[
    ("“Absence of proteinuria supports essential hypertension”", "Absent proteinuria only says it is not pre-eclampsia and not overt renal disease. The DocT key (49% right) is family history and obesity, the risk factors for primary hypertension. A diastolic of 95 does not separate the types either."),
    ("“Gestational hypertension arises before 20 weeks”", "It arises after 20 weeks; this was the false statement in the DocT GT question (83%)."),
    ("“Systolic 140 is a severe feature”", "140/90 is the diagnostic threshold; severe is 160 systolic or 110 diastolic (Marrow)."),
    ("Early gestation as a severe feature", "The Marrow key counts early onset among the markers of severe disease, because disease starting before 34 weeks behaves worse. It is not on ACOG’s list of severe features, so use it only when the options force it."),
  ],
  decode=[
    ("Hypertension at 16 weeks, no proteinuria — which feature supports essential chronic hypertension? [DocT GT]", "Family history of hypertension and obesity."),
    ("Which statement about gestational hypertension is NOT true? [DocT GT]", "‘Arises before 20 weeks’ is false. No proteinuria or organ dysfunction, a substantial risk of later pre-eclampsia and resolution by 12 weeks postpartum are true."),
    ("Definition of chronic hypertension in pregnancy [Marrow]", "Pre-existing or before 20 weeks, or persisting beyond 12 weeks postpartum."),
    ("Features of severe disease — pick the set [Marrow]", "Diastolic 110, raised creatinine, platelets 50,000 (and early gestation in that key); not systolic 140."),
  ],
  punch="Before 20 weeks or beyond 12 weeks postpartum is chronic; after 20 weeks it is gestational hypertension until proteinuria or organ dysfunction makes it pre-eclampsia, and 160/110 or organ injury makes any of them severe.",
)

L['OBS-17'] = dict(
  sub="Obstetrics → Hypertensive disorders → Pathophysiology of pre-eclampsia",
  step=2,
  intro="Step 2 explains why one disease can raise the pressure, leak protein, drop the platelets and swell the brain. The fault starts in the placenta in the first half of pregnancy and reaches the mother through her endothelium in the second half. Both linked questions have the same key, endothelial dysfunction, and the distractors are the normal adaptations of pregnancy stated the wrong way round.",
  parts=[
    ('a', "**Impaired trophoblast invasion: the spiral arteries stay narrow.** Normally trophoblast replaces the muscular wall of the spiral arteries, turning them into wide passive channels. In pre-eclampsia the invasion stops at the decidua, so the vessels stay narrow and reactive."),
    ('b', "**Placental ischaemia.** The under-perfused placenta is hypoxic and under oxidative stress. This is also why the fetus is growth-restricted and the umbilical artery Doppler loses its diastolic flow (OBS-20)."),
    ('c', "**The placenta releases sFlt-1 and soluble endoglin: anti-angiogenic.** sFlt-1 is a soluble receptor that binds VEGF and placental growth factor, so they never reach the endothelium; soluble endoglin blocks TGF-β signalling in the same way. Endothelium deprived of these signals makes less nitric oxide and prostacyclin and becomes leaky."),
    ('d', "**Systemic endothelial dysfunction.** This is the step both questions key. Less prostacyclin and nitric oxide with more thromboxane and endothelin give vasoconstriction, platelet activation and capillary leak. The normal resistance of pregnancy to angiotensin II is lost, so sensitivity to it is increased."),
    ('e', "**Kidney: glomerular endotheliosis (proteinuria). Liver: microcirculatory failure. Brain: oedema, headache, stroke. Vessels: vasoconstriction, high SVR.** Each organ shows the same endothelial lesion. Swollen glomerular endothelial cells leak protein and lower the GFR; fibrin in the hepatic sinusoids gives the liver injury of HELLP (OBS-27); failed cerebral autoregulation gives PRES and eclampsia (OBS-26). Because of the leak and the vasoconstriction, plasma volume is lower than in normal pregnancy although the woman is oedematous (OBS-19)."),
  ],
  mimic=[
    ("Pre-eclampsia vs normal pregnancy physiology", "Normal: low SVR, plasma volume up, resistant to angiotensin II, high renal blood flow and GFR. Pre-eclampsia: high SVR, plasma volume contracted, sensitive to angiotensin II, reduced GFR."),
  ],
  traps=[
    ("“Decreased sensitivity to angiotensin II”", "That is normal pregnancy. Pre-eclampsia has increased sensitivity."),
    ("“Excess prostacyclin activity” or “increased renal prostaglandin synthesis”", "Prostacyclin is reduced and thromboxane dominates; this imbalance is why low-dose aspirin is used for prevention."),
    ("“Elevated plasma volume” or “enhanced renal perfusion”", "Plasma volume is contracted and renal perfusion falls."),
    ("Vitamins C and E for prevention (the card’s watch line)", "Randomised trials showed no benefit and ACOG says they do not reduce pre-eclampsia. What works is low-dose aspirin started before 16 weeks in women at risk, and calcium where dietary intake is low."),
  ],
  decode=[
    ("Which mechanism is implicated in the pathogenesis of pre-eclampsia? [DocT GT]", "Endothelial dysfunction from placental ischaemia (100%)."),
    ("24 weeks, MAP 96, at risk of later pre-eclampsia — the linked abnormality? [DocT GT]", "Endothelial dysfunction."),
    ("[pattern] Renal biopsy lesion of pre-eclampsia", "Glomerular endotheliosis."),
    ("[pattern] Which anti-angiogenic factor is raised?", "sFlt-1 (with soluble endoglin); free VEGF and placental growth factor are low."),
  ],
  punch="Shallow placentation leaves an ischaemic placenta that sheds sFlt-1 and soluble endoglin, and the endothelial dysfunction they cause explains the high SVR, the proteinuria, the contracted plasma volume and the injury to liver and brain.",
)

L['OBS-18'] = dict(
  sub="Obstetrics → Hypertensive disorders → Acute severe hypertension: the three drugs",
  step=3,
  intro="Step 3 is treatment, and it begins with the pressure. A reading of 160/110 or more that persists for 15 minutes is an emergency because the danger is maternal intracerebral haemorrhage; it should be treated within 30–60 minutes. Five questions test this table: three turn on asthma, one on which drug is not for acute use and one on the drug class that is forbidden.",
  parts=[
    ('a', "**Labetalol: 10–20 mg IV, then 20–80 mg every 10–30 min (maximum 300 mg); or 1–2 mg/min infusion. Onset 1–2 min. Caution: asthma, bradycardia, heart failure.** It blocks α and β receptors, so pressure falls without reflex tachycardia and placental flow is preserved, which is why it is the usual first choice and the key in two Grand Tests. The β-blockade is non-selective: it causes bronchospasm in asthma and worsens bradycardia, heart block and decompensated heart failure. A stem that says ‘no asthma, no bradycardia’ is permitting labetalol; a stem that gives asthma is forbidding it."),
    ('b', "**Hydralazine: 5 mg IV or IM, then 5–10 mg every 20–40 min (maximum 20 mg); or 0.5–10 mg/h. Onset 10–20 min. Caution: maternal hypotension, headache, abnormal fetal heart tracing.** It is a direct arteriolar dilator. Its slow onset tempts early repeat doses, which then stack and overshoot; the hypotension drops placental flow and the fetal heart tracing deteriorates. Its headache and tachycardia also imitate worsening pre-eclampsia."),
    ('c', "**Nifedipine: 10–20 mg orally, repeat in 20 min; then every 2–6 h (maximum 180 mg/day). Onset 5–10 min. Caution: reflex tachycardia, headache.** Immediate-release oral nifedipine is as effective as the IV drugs and needs no IV access, so it is the answer when labetalol is contraindicated or when it is the only first-line drug offered. It is swallowed, not given sublingually. It can be given with magnesium; the old fear of profound hypotension or neuromuscular block from the combination has not been borne out."),
  ],
  table=dict(title="Which drug the stem wants", head=["Stem detail", "Answer", "Why"], rows=[["No asthma, no bradycardia", "**IV labetalol**", "fast, no reflex tachycardia"], ["Asthma", "**oral nifedipine** (or IV hydralazine)", "labetalol is a non-selective β-blocker"], ["No IV access", "**oral nifedipine**", "works in 5–10 min"], ["Pulmonary oedema", "**nitroglycerin infusion**, with furosemide", "venodilates and unloads the lung"], ["Maintenance, not acute", "methyldopa, oral labetalol, long-acting nifedipine", "methyldopa takes hours to act"], ["Never", "**ACE inhibitors, ARBs**", "fetal renal failure, oligohydramnios"]]),
  mimic=[
    ("Acute drugs vs maintenance drugs", "Acute (minutes): IV labetalol, IV hydralazine, oral immediate-release nifedipine. Maintenance (hours to days): methyldopa, oral labetalol, long-acting nifedipine."),
    ("Antihypertensive vs magnesium", "The antihypertensive prevents stroke; magnesium prevents seizures and does not lower the pressure usefully. A woman with severe pre-eclampsia needs both (OBS-19)."),
  ],
  traps=[
    ("“Labetalol” in a woman with asthma", "Contraindicated; both asthma stems key against it. In CGT2 the answer is oral nifedipine, in CGT6 labetalol is the IV drug to avoid."),
    ("“Methyldopa” for acute severe hypertension", "It is safe in pregnancy but slow, so it is the one option that is not first-line for an acute crisis (73% right)."),
    ("“Oral nifedipine and magnesium cannot be given together”", "They can; this was a wrong option in CGT2."),
    ("“ACE inhibitor” because it is ideal for renal artery stenosis", "ACE inhibitors and ARBs cause fetal renal dysgenesis, oligohydramnios and skull defects in the second and third trimesters; contraindicated (87%)."),
    ("“Nitroprusside” or “enalapril” as first line", "Nitroprusside is a last resort because of fetal cyanide exposure; with nifedipine among the options, nifedipine is the answer (89%)."),
    ("Lowering the pressure to normal", "The aim is to bring the pressure out of the severe range, to roughly 140–150/90–100, not to normal. The placenta does not autoregulate, so a large or rapid fall reduces its flow and causes fetal distress."),
  ],
  decode=[
    ("Which is NOT a first-line drug for acute severe hypertension in pregnancy? [DocT GT]", "Methyldopa; the three first-line drugs are IV labetalol, IV hydralazine and oral nifedipine."),
    ("37 weeks, BP 170/100, headache, asthma with a hospital admission last year [DocT GT]", "Oral nifedipine; asthma rules out labetalol."),
    ("Severe pre-eclampsia, BP 182/116, asthma on inhaled steroids — which IV drug to avoid? [DocT GT]", "Labetalol."),
    ("34 weeks, BP 175/110; options enalapril, nifedipine, nitroprusside, spironolactone [DocT GT]", "Nifedipine, the only first-line drug listed."),
  ],
  punch="Severe hypertension of 160/110 is lowered within the hour to prevent stroke, using IV labetalol unless there is asthma, bradycardia or heart failure, otherwise oral nifedipine or IV hydralazine; methyldopa is too slow and ACE inhibitors are forbidden.",
  extra=[dict(q="Why is an ACE inhibitor contraindicated in pregnancy?", a="Fetal kidneys need angiotensin II to maintain filtration; blockade causes renal dysgenesis, oligohydramnios, lung hypoplasia and skull defects.")],
)

L['OBS-19'] = dict(
  sub="Obstetrics → Hypertensive disorders → Principles: delivery, fluids, diuretics, magnesium",
  step=3,
  intro="Step 3 continues with the rules that run alongside the antihypertensive. The woman with pre-eclampsia is oedematous yet her circulation is under-filled, so both a diuretic and a generous fluid bolus can harm her. Four questions are linked, and two of the keys are disputed, so the reasoning matters more than the letter.",
  parts=[
    ('a', "**Delivery.** Removing the placenta removes the source of sFlt-1 (OBS-17), and the disease resolves over days. Everything else on this card only buys safety until the placenta is out; timing is in OBS-20."),
    ('b', "**Volume-depleted despite oedema: avoid diuretics; but aggressive fluid causes pulmonary oedema.** Leaky capillaries and a low albumin move water into the tissues, so the plasma volume is contracted. A diuretic shrinks it further and reduces placental and renal perfusion. Yet the same leak, with a stiff left ventricle working against a high SVR, means a fluid load ends up in the lungs. The single indication for a diuretic is pulmonary oedema, treated with IV furosemide."),
    ('c', "**Isotonic fluid to replace urine output and insensible loss; no more than 80 mL/hour.** The figure is from NICE: in severe pre-eclampsia maintenance fluid is limited to 80 mL/hour unless there are other ongoing losses such as haemorrhage, and volume expansion is not used. The reason is the leak described in b: extra fluid leaves the circulation for the lungs, so it is not given to chase the urine output."),
    ('d', "**Strict input–output charting: prone to renal dysfunction.** Glomerular endotheliosis lowers the GFR, so a low urine output is common. Urine output also governs magnesium safety, because magnesium is cleared only by the kidney (OBS-24)."),
    ('e', "**Not needed unless severe features develop.** In Magpie the number needed to treat to prevent one seizure was about 100 in women without severe disease, so ACOG leaves magnesium without severe features to local policy. With severe features, or with gestational hypertension in the severe range, it is given."),
  ],
  mimic=[
    ("Oliguria in pre-eclampsia vs hypovolaemic oliguria", "Pre-eclampsia: expected, tolerated, and watched without a fluid challenge unless there is bleeding. Haemorrhage or sepsis: needs volume."),
    ("Pulmonary oedema in pre-eclampsia vs peripartum cardiomyopathy", "Pre-eclampsia: severe hypertension, preserved systolic function, clears with furosemide, a vasodilator and delivery. Cardiomyopathy: reduced ejection fraction, pressure often normal or low."),
  ],
  traps=[
    ("“Magnesium first” as the only initial step when BP is 180/110 with pulmonary oedema", "DocT keys magnesium (60% and 73% right) and by exam convention it is the answer. In practice magnesium, an antihypertensive and furosemide are started together: magnesium does nothing for the pressure or the oedema, and the immediate threats are stroke and hypoxia. Choose magnesium when the question asks for the single first drug in severe pre-eclampsia, and know why it is disputed."),
    ("“IV furosemide” for the same stem", "Furosemide is correct treatment for the pulmonary oedema, and it is the key when the question asks for the indication for a diuretic (81%); it is not DocT’s key for ‘initial management’."),
    ("“Diuretic for severe pedal oedema” or “for persistent hypertension”", "Neither is an indication. Only pulmonary oedema is."),
    ("“Controlled plasma volume expansion” as first-line management", "This is the Marrow key, taken from an older handbook. Current practice is the opposite: restrict fluid to about 80 mL/hour. Recognise the dated answer if those are the options."),
    ("Aggressive crystalloid to correct ‘intravascular depletion’", "A wrong option in the HELLP Grand Test question; it causes pulmonary oedema."),
  ],
  decode=[
    ("36 weeks, headache, visual symptoms, BP 180/110, SpO₂ 92%, bilateral crepitations, proteinuria 3+ — initial management? [DocT QBank, DocT GT]", "Keyed IV magnesium sulphate; in practice with labetalol or nitroglycerin and furosemide at the same time."),
    ("Indication for diuretics in a primigravida with pre-eclampsia? [DocT GT]", "Pulmonary oedema."),
    ("First-line management in pre-eclampsia [Marrow]", "Keyed ‘controlled plasma volume expansion’ (dated); current answer is fluid restriction."),
    ("[pattern] Pre-eclampsia without severe features at 35 weeks — magnesium?", "Not required; start it if severe features appear."),
  ],
  punch="Delivery cures; until then treat pressure to prevent stroke and give magnesium to prevent seizures as two separate jobs, hold fluid to 80 mL/hour, and use a diuretic only for pulmonary oedema.",
  extra=[dict(q="Antihypertensive of choice when pre-eclampsia presents with pulmonary oedema?", a="Nitroglycerin infusion, with IV furosemide, oxygen or non-invasive ventilation, fluid restriction and delivery.")],
)

L['OBS-20'] = dict(
  sub="Obstetrics → Hypertensive disorders → Severe pre-eclampsia: timing of delivery",
  step=3,
  intro="Step 3 now sets the date of the cure. Delivery always benefits the mother, so the only reason to wait is fetal lung maturity, and waiting is allowed only while mother and fetus are stable. The table sorts women into deliver now, deliver after a 48-hour course of steroids, or wait until 34 weeks. Three questions are linked; two are HELLP stems at 33 and 29 weeks.",
  parts=[
    ('a', "**34 weeks or more: deliver.** From 34 weeks the neonatal gain from waiting is small and the maternal risk of stroke, abruption and eclampsia continues, so ACOG recommends delivery once the mother is stabilised, without delaying for steroids. Without severe features the same reasoning gives delivery at 37 weeks."),
    ('b', "**Under 24 weeks: deliver (not viable).** Before viability, expectant care exposes the mother to serious risk with almost no chance of a surviving baby."),
    ('c', "**Eclampsia, pulmonary oedema, DIC, renal failure, abruption, non-reassuring fetal testing: deliver immediately, at any gestation.** These mean an organ has already failed or the fetus is in danger. ‘Immediately’ means after stabilising the mother with magnesium and blood pressure control; it does not by itself mean caesarean section."),
    ('d', "**33+0 to 33+6 weeks; HELLP; growth restriction under 5th centile; reversed end-diastolic flow; persistent symptoms; preterm labour or rupture of membranes: steroids; deliver after 48 hours.** These women are too unstable for prolonged waiting but can usually be held for the 48 hours that antenatal corticosteroids need to mature the fetal lung. The steroid course is for the baby, not a treatment for the mother. If mother or fetus worsens during the 48 hours, delivery goes ahead."),
    ('e', "**24 to 32+6 weeks, none of the above: steroids; expectant; deliver at 33+6 weeks.** Each extra week before 34 weeks lowers the baby’s risk from prematurity, and that is the only gain. Expectant care means admission to a centre with neonatal intensive care, magnesium while she is assessed and the steroids are given, controlled pressure, daily maternal and fetal assessment, and delivery as soon as any feature in rows c or d appears (OBS-21)."),
  ],
  mimic=[
    ("Absent vs reversed end-diastolic flow", "Both mean high placental resistance with growth restriction. Absent flow: steroids and delivery at about 33–34 weeks. Reversed flow is worse: delivery at about 30–32 weeks (SMFM 2020), and persistent reversed flow is one of ACOG’s reasons not to continue expectant care."),
    ("Steroids for the fetus vs steroids for HELLP", "Betamethasone or dexamethasone for lung maturity is standard before 34 weeks. High-dose dexamethasone to treat the mother’s HELLP raises the platelet count but has not improved outcomes."),
  ],
  traps=[
    ("“Immediate caesarean section” for stable HELLP at 33 weeks", "Mother and fetus are stable, so the key is delivery within 48 hours after corticosteroids (61% right). Caesarean is for obstetric indications."),
    ("“Delay until 37 weeks” or “wait till platelets normalise” in HELLP", "HELLP does not recover until the placenta is delivered; platelets go on falling."),
    ("“Dexamethasone to cure the thrombocytopenia and wait until 34 weeks”", "A wrong option in the 29-week stem. That woman also has severe epigastric pain and BP 175/115, so the key is magnesium followed by prompt delivery. ACOG lists HELLP among the conditions that preclude expectant care; a 24–48 hour steroid window is acceptable only while she is stable."),
    ("“Absent end-diastolic flow means cord thrombosis”", "It means placental resistance is so high that forward flow stops in diastole: uteroplacental insufficiency with growth restriction (91%)."),
  ],
  decode=[
    ("33 weeks, HELLP (platelets 70,000, AST 300, LDH 800), BP 150/100, fetus stable — when to deliver? [DocT QBank]", "Within 48 hours after corticosteroids."),
    ("29 weeks, HELLP, BP 175/115, severe epigastric pain — definitive management? [DocT GT]", "Magnesium for seizure prophylaxis and prompt delivery regardless of gestation."),
    ("35 weeks, pre-eclampsia, umbilical artery Doppler with absent end-diastolic flow — implication? [DocT QBank]", "Fetal growth restriction from uteroplacental insufficiency."),
    ("[pattern] Severe pre-eclampsia at 35 weeks, stable", "Deliver; do not wait for steroids."),
  ],
  punch="Severe pre-eclampsia is delivered at 34 weeks, at once at any gestation if an organ or the fetus is failing, and after a 48-hour steroid course for stable HELLP, growth restriction or 33 weeks; only the stable woman at 24–33 weeks waits.",
)

L['OBS-21'] = dict(
  sub="Obstetrics → Hypertensive disorders → Severe pre-eclampsia: deliver or wait",
  step=3,
  intro="Step 3 ends with the daily decision in a woman being managed expectantly before 34 weeks. Each row asks the same thing of a different organ: is the abnormality fixed and progressing, in which case deliver, or mild and reversible, in which case wait. The linked question takes the liver row to its worst outcome, a subcapsular haematoma.",
  parts=[
    ('a', "**Blood pressure — deliver: uncontrolled severe hypertension; eclampsia. Expectant: controlled.** Pressure that stays at 160/110 despite maximum doses of the drugs in OBS-18 leaves the mother exposed to cerebral haemorrhage, so waiting is no longer justified."),
    ('b', "**Liver — deliver: AST or ALT over twice normal with epigastric or right upper quadrant pain. Expectant: over twice normal without pain.** The pain means the liver capsule is being stretched by swelling or by bleeding beneath it, which precedes subcapsular haematoma and rupture. Raised enzymes alone, without pain, can be watched."),
    ('c', "**Kidney — deliver: compromised renal function. Expectant: oliguria (under 0.5 mL/kg/h) that resolves with fluid.** A rising creatinine is established injury; transient oliguria that responds to a modest fluid intake is not."),
    ('d', "**Other — deliver: platelets under 100,000; pulmonary oedema; abruption; persistent headache or visual change. Expectant: proteinuria of any amount.** Proteinuria rises during expectant care, but the amount does not predict outcome and never decides delivery; ACOG says it need not be re-measured once the diagnosis is made."),
    ('e', "**Fetus — deliver: repeated late or severe variable decelerations; biophysical profile 4 or less twice; weight under 5th centile; reversed diastolic flow. Expectant: reassuring heart rate; profile 6 or more; weight above 5th centile.** These are signs that the placenta can no longer support the fetus, which is then safer delivered than left in the uterus."),
  ],
  mimic=[
    ("Subcapsular haematoma vs acute fatty liver", "Both have right upper quadrant pain and raised enzymes near term. Haematoma: HELLP picture (haemolysis, platelets 60,000, AST in the hundreds), shoulder-tip pain, then sudden shock; needs imaging now. Fatty liver: hypoglycaemia, raised INR and ammonia, jaundice (OBS-29)."),
  ],
  traps=[
    ("“Acute fatty liver” for HELLP with severe RUQ pain and AST 520", "Haemolysis on the smear with platelets of 60,000, and no hypoglycaemia, coagulopathy or encephalopathy in the stem, is HELLP; the complication needing immediate imaging is a hepatic subcapsular haematoma (53% right)."),
    ("“Heavy proteinuria is an indication to deliver”", "The amount of proteinuria never decides delivery."),
    ("“Raised transaminases always mean delivery”", "Only with pain, or with the other features of HELLP."),
  ],
  decode=[
    ("34 weeks, malaise, RUQ pain, platelets 60,000, AST 520, LDH 900, haemolysis, BP 160/100 — which complication needs immediate imaging? [DocT QBank]", "Hepatic subcapsular haematoma: ultrasound or CT. If unruptured, deliver, transfuse and avoid pressure on the abdomen; if ruptured, laparotomy with packing or embolisation."),
    ("[pattern] 30 weeks, severe pre-eclampsia, proteinuria risen from 2 g to 7 g/day, otherwise stable", "Continue expectant care; proteinuria does not decide."),
    ("[pattern] 31 weeks, BP 170/112 despite maximal labetalol and nifedipine", "Deliver."),
  ],
  punch="Deliver within 72 hours for uncontrolled pressure, liver pain with raised enzymes, a rising creatinine, platelets under 100,000, pulmonary oedema, abruption, persistent cerebral symptoms or a failing fetus; the amount of proteinuria never decides.",
  extra=[dict(q="HELLP with sudden severe RUQ and shoulder-tip pain, then hypotension?", a="Ruptured subcapsular liver haematoma: massive transfusion, laparotomy with packing or hepatic artery embolisation.")],
)

L['OBS-22'] = dict(
  sub="Obstetrics → Eclampsia → The facts",
  step=4,
  intro="Step 4 is the seizure. Eclampsia is a generalised seizure in a woman with a hypertensive disorder of pregnancy and no other cause, and it does not wait for labour or for a warning. The one linked question asks only for the first-line drug, which 94% get right; the facts on this card are what a harder stem would use to disguise the diagnosis.",
  parts=[
    ('a', "**Antepartum 53%; intrapartum 19%; postpartum 28%.** More than a quarter occur after delivery, most within 48 hours but some up to several weeks later, when the woman may already be at home. Delivery starts the cure but does not end the risk, which is why magnesium continues for 24 hours postpartum (OBS-23)."),
    ('b', "**20%.** About one in five has no preceding diagnosis of pre-eclampsia; ACOG gives 20–38% without the classic signs before the seizure. A normal pressure record or absent proteinuria therefore does not exclude eclampsia."),
    ('c', "**Generalised tonic-clonic, lasting 60–90 seconds; then confusion or agitation.** The seizure is brief and stops by itself. A focal seizure, one that lasts many minutes, or a persistent focal deficit or coma afterwards suggests another diagnosis and needs imaging (OBS-26)."),
    ('d', "**Bradycardia from hypoxia; it usually recovers.** During the seizure the mother is apnoeic and the uterus contracts, so the fetal heart rate falls for some minutes and recovers once she is oxygenated. This is treated by resuscitating the mother, not by an immediate caesarean section; bradycardia that persists raises the question of abruption."),
    ('e', "**A seizure in pregnancy is eclampsia until proven otherwise.** Give magnesium first and investigate afterwards. The rule applies from 20 weeks to about six weeks postpartum."),
  ],
  mimic=[
    ("Eclampsia vs epilepsy in pregnancy", "Eclampsia: no seizure history, hypertension or proteinuria, headache or visual symptoms beforehand, after 20 weeks. Epilepsy: known disorder or missed drugs, normal pressure and urine. When in doubt, treat as eclampsia."),
    ("Postpartum eclampsia vs cerebral venous thrombosis", "Both present in the puerperium with headache and seizures. Venous thrombosis: focal signs, haemorrhagic venous infarct, clot on venography (OBS-26)."),
  ],
  traps=[
    ("“Diazepam”, “phenytoin” or “levetiracetam” for the eclamptic seizure", "Magnesium sulphate is first line (94%); it prevents recurrence better than either older drug (OBS-25)."),
    ("“She has delivered, so it cannot be eclampsia”", "28% of cases are postpartum."),
    ("“Emergency caesarean for the fetal bradycardia during the seizure”", "Stabilise the mother first; the fetal heart rate usually recovers. Delivery follows once she is stable."),
  ],
  decode=[
    ("32 weeks, tonic-clonic seizures, hypertension, pedal oedema, proteinuria 3+ — first-line treatment? [DocT QBank]", "Magnesium sulphate."),
    ("[pattern] Seizure three days after a normal delivery, BP 150/95, headache", "Postpartum eclampsia until proven otherwise: magnesium, then imaging if atypical."),
    ("[pattern] Fetal bradycardia for three minutes during an eclamptic seizure", "Maternal oxygenation and left lateral position; it usually recovers."),
  ],
  punch="Eclampsia is a brief generalised seizure that comes before labour in half, after delivery in over a quarter and without known pre-eclampsia in a fifth, so every seizure in pregnancy gets magnesium first.",
)

L['OBS-23'] = dict(
  sub="Obstetrics → Eclampsia → Magnesium sulphate regimen",
  step=4,
  intro="Step 4 continues with how the drug is given. The regimen is a loading dose to reach an effective level quickly and an infusion to hold it, monitored at the bedside. The linked question asks only which drug; the numbers here are what a dose or toxicity stem will use.",
  parts=[
    ('a', "**4–6 g IV over 15–20 minutes (not above 8 g).** A loading dose is needed because an infusion alone would take hours to reach a protective level. It is given slowly because a fast bolus causes flushing, hypotension and respiratory depression. ACOG words the time as 20–30 minutes; NICE uses the Collaborative Eclampsia Trial regimen of 4 g over 5–15 minutes, then 1 g/hour."),
    ('b', "**1–2 g/hour.** The infusion replaces what the kidney clears. With a creatinine of 1.0–1.5 mg/dL or oliguria, ACOG gives the full loading dose but only 1 g/hour and checks levels, because the loading dose fills the body’s volume of distribution while the maintenance dose depends on renal clearance."),
    ('c', "**From the onset of labour until 24 hours postpartum (or after the last seizure).** The seizure risk extends into the puerperium (OBS-22), so the infusion covers labour, delivery and the first postpartum day, or 24 hours from the last seizure if that is later."),
    ('d', "**2–3.5 mmol/L (4.8–8.4 mg/dL).** This is the range above which toxicity begins (OBS-24). The target is derived from observation, not from a trial, which is why levels are not routine."),
    ('e', "**Clinically: patellar reflex, respiratory rate, urine output. Levels only if indicated.** The knee jerk is lost before breathing is affected, so a present reflex means the level is safe. A falling respiratory rate is the next sign. Urine output matters because magnesium is excreted only by the kidney: oliguria predicts accumulation. Levels are measured in renal impairment, oliguria or suspected toxicity."),
  ],
  table=dict(title="Regimens and adjustments", head=["Situation", "Dose"], rows=[["IV (Zuspan-type, ACOG)", "**4–6 g load, then 1–2 g/h**"], ["IM when IV access or pumps are lacking (Pritchard)", "4 g IV plus 10 g IM (5 g in each buttock), then 5 g IM every 4 h"], ["Seizure recurs on magnesium", "**a further 2 g IV** (ACOG: 2–4 g over 5 min)"], ["Creatinine 1.0–1.5 mg/dL or oliguria", "full load, **1 g/h**, check levels"], ["Absent knee jerk, slow breathing", "**stop the infusion**, check a level (OBS-24)"]]),
  mimic=[
    ("Loading dose vs maintenance dose in renal impairment", "The loading dose is unchanged; only the maintenance rate is reduced."),
  ],
  traps=[
    ("“A benzodiazepine for a second seizure on magnesium”", "Give a further magnesium bolus first; benzodiazepines, phenytoin or thiopental are for seizures that continue despite it."),
    ("“Check serum magnesium every few hours in everyone”", "Monitoring is clinical; levels are for renal impairment, oliguria or signs of toxicity."),
    ("“Stop magnesium at delivery”", "Continue for 24 hours postpartum."),
    ("“Omit the loading dose in renal failure”", "The load is still needed; the infusion is what is cut."),
  ],
  decode=[
    ("32 weeks, tonic-clonic seizures, hypertension, proteinuria 3+ — first-line treatment? [DocT QBank]", "Magnesium sulphate: 4–6 g IV load, then 1–2 g/hour."),
    ("[pattern] Eclamptic woman on 1 g/hour seizes again", "A further 2 g IV bolus of magnesium."),
    ("[pattern] What is monitored during magnesium infusion?", "Patellar reflex, respiratory rate and urine output."),
  ],
  punch="Magnesium is loaded with 4–6 g IV over 15–20 minutes and run at 1–2 g/hour until 24 hours after delivery or the last seizure, watched by knee jerk, respiratory rate and urine output, with the infusion reduced in renal impairment.",
)

L['OBS-24'] = dict(
  sub="Obstetrics → Eclampsia → Magnesium toxicity by level",
  step=4,
  intro="Step 4 now covers what goes wrong with the drug. Magnesium blocks calcium-dependent transmitter release at the neuromuscular junction, so toxicity is a progressive paralysis in a fixed order: reflexes, then breathing, then the heart. Three questions test the order and the treatment.",
  parts=[
    ('a', "**5–9 mg/dL: therapeutic.** At this level the anticonvulsant effect is present and the reflexes are intact. The card’s other range, 4.8–8.4 mg/dL, is the same band converted from 2–3.5 mmol/L."),
    ('b', "**Over 9 mg/dL: patellar reflex lost.** Loss of the knee jerk is the first sign of toxicity and the commonest ‘side effect’ asked. It is the reason the reflex is tested before each dose and hourly on an infusion: while it is present, breathing is safe."),
    ('c', "**Over 12 mg/dL: respiratory paralysis.** The respiratory muscles weaken next. A slowing respiratory rate or falling saturation on magnesium is toxicity until proven otherwise."),
    ('d', "**Over 30 mg/dL: cardiac arrest.** At very high levels conduction fails and the heart stops."),
    ('e', "**Antidote: calcium gluconate. ECG: long PR, wide QRS, long QT, then heart block.** Calcium gluconate 10%, 10 mL (1 g) IV over about 3 minutes, competes with magnesium at the junction and the heart and reverses the effect within minutes, but it does not remove magnesium. The infusion is stopped, breathing is supported, and the magnesium must be excreted: by the kidney, helped by furosemide, or by dialysis if the kidney has failed."),
  ],
  table=dict(title="Level and effect in three units", head=["Effect", "mg/dL", "mEq/L (about)", "mmol/L (about)"], rows=[["Therapeutic", "**5–9**", "4–7", "2–3.5"], ["Knee jerk lost", "**>9**", ">7", ">3.5"], ["Respiratory paralysis", "**>12**", ">10", ">5"], ["Cardiac arrest", "**>30**", ">25", ">12.5"]]),
  mimic=[
    ("Magnesium toxicity vs post-ictal state or eclamptic coma", "Toxicity: absent reflexes, flaccid, slow shallow breathing, often oliguria. Eclampsia: brisk reflexes and clonus."),
    ("Magnesium toxicity vs high spinal block or opioid", "All slow the breathing after delivery. Magnesium: areflexia with a known infusion and a low urine output; responds to calcium."),
  ],
  traps=[
    ("“Reduce the magnesium dose” for respiratory depression", "Respiratory depression is established toxicity: stop the infusion and give calcium gluconate (89% right)."),
    ("“Start dialysis” as the next step with creatinine 3.0", "Dialysis is how the magnesium is finally removed when the kidney has failed, but the next step is still to stop the drug and give calcium, which works in minutes."),
    ("“Give furosemide” as the next step", "It speeds excretion only if the kidney is working and does nothing for the immediate paralysis."),
    ("Mixing units", "The obstetric table is in mg/dL; the electrolyte chapter (MGP-07) uses mEq/L with lower cut-offs. 1 mEq/L is about 1.2 mg/dL. In every version the knee jerk goes first."),
  ],
  decode=[
    ("Eclampsia on magnesium, respiratory depression, creatinine 3.0 — best next step? [DocT QBank]", "Stop magnesium and give IV calcium gluconate."),
    ("Severe pre-eclampsia given IV seizure prophylaxis — likely side effect? [Marrow, twice]", "Loss of deep tendon reflexes."),
    ("[pattern] Why is urine output charted on magnesium?", "Magnesium is cleared only by the kidney, so oliguria leads to toxicity."),
  ],
  punch="Magnesium toxicity runs in order: knee jerk lost above 9 mg/dL, breathing above 12, cardiac arrest above 30; at the first sign stop the infusion and give 1 g of calcium gluconate IV.",
)

L['OBS-25'] = dict(
  sub="Obstetrics → Eclampsia → How magnesium works; the Magpie trial",
  step=4,
  intro="Step 4 finishes with why magnesium is the anticonvulsant of choice and the trial that established it for prevention. Three questions are linked: the Magpie result, the drug of choice for the eclamptic seizure (77% right, the rest choosing a benzodiazepine) and the one patient in whom magnesium must not be used.",
  parts=[
    ('a', "**Cerebral vasodilatation: relieves vasospasm.** Magnesium is a calcium antagonist in vascular smooth muscle. It also protects the blood–brain barrier and so limits the vasogenic oedema that underlies the seizure (OBS-26). The effect on systemic blood pressure is small and brief, which is why it is not an antihypertensive."),
    ('b', "**Reduces acetylcholine release at the motor end-plate.** Calcium entry into the nerve terminal triggers acetylcholine release, and magnesium competes with calcium. This explains the loss of reflexes and the respiratory weakness in toxicity (OBS-24), the potentiation of non-depolarising neuromuscular blockers, and the danger in myasthenia gravis, where transmission is already failing."),
    ('c', "**Antagonises intracellular calcium; blocks NMDA receptors.** Blocking the NMDA glutamate receptor raises the seizure threshold."),
    ('d', "**About 10,000 women in 33 countries; magnesium vs placebo in pre-eclampsia.** Magpie (Lancet 2002) randomised 10,141 women with pre-eclampsia, before delivery or within 24 hours after it, to magnesium or placebo."),
    ('e', "**A 58% lower risk of eclampsia (relative risk about 0.41).** Eclampsia occurred in 0.8% on magnesium and 1.9% on placebo; the published relative risk is 0.42. About 91 women had to be treated to prevent one seizure. Maternal deaths were fewer but not significantly so, placental abruption was reduced, and there was no harm to the baby. Side effects, mostly flushing, occurred in a quarter, with no excess of serious ones."),
  ],
  mimic=[
    ("Magpie vs the Collaborative Eclampsia Trial", "Magpie (2002): prevention, magnesium vs placebo in pre-eclampsia. Collaborative Eclampsia Trial (1995): treatment of women who had already seized, magnesium vs diazepam and vs phenytoin; magnesium roughly halved recurrent seizures against diazepam and cut them by two-thirds against phenytoin."),
    ("Magnesium vs a benzodiazepine in eclampsia", "Magnesium prevents recurrence without sedating mother or baby. A benzodiazepine sedates, depresses breathing and was inferior in the trial; it is kept for seizures that continue despite magnesium."),
  ],
  traps=[
    ("“Lorazepam” or “diazepam” for acute seizure control in eclampsia", "The usual status epilepticus rule does not apply; magnesium is the drug of choice even for the seizure in progress (77% right)."),
    ("“Magnesium lowers the blood pressure”", "It is not an antihypertensive; give a separate drug (OBS-18)."),
    ("“Magpie showed lower maternal mortality”", "The reduction was not statistically significant. The proven result is fewer seizures without serious side effects."),
    ("“Magnesium for a woman with myasthenia gravis”", "Contraindicated; it can precipitate a myasthenic crisis. The Marrow key is levetiracetam."),
    ("Normal dose of non-depolarising relaxant at caesarean under general anaesthesia", "Magnesium prolongs the block; reduce the dose and monitor with a nerve stimulator."),
  ],
  decode=[
    ("Primary finding of the Magpie trial (2002)? [DocT QBank]", "Magnesium reduces the risk of eclampsia without major side effects."),
    ("Drug of choice for acute seizure control in eclampsia? [DocT QBank]", "Magnesium sulphate."),
    ("Eclampsia prophylaxis in a woman with myasthenia gravis? [Marrow]", "Levetiracetam; magnesium is contraindicated."),
    ("[pattern] Why does a woman on magnesium stay paralysed after vecuronium?", "Less acetylcholine release potentiates the non-depolarising block."),
  ],
  punch="Magnesium dilates cerebral vessels, blocks NMDA receptors and reduces acetylcholine release; Magpie showed it more than halves eclampsia in pre-eclampsia, and the same end-plate action is why it is avoided in myasthenia and prolongs muscle relaxants.",
)

L['OBS-26'] = dict(
  sub="Obstetrics → Eclampsia → Other causes of a seizure in pregnancy; PRES",
  step=5,
  intro="Step 5 asks what else the seizure could be. The rule is to treat as eclampsia first, then look for another cause when the seizure is focal or prolonged, when consciousness does not return, or when it occurs before 20 weeks or late after delivery. Four questions are linked and all four are answered by PRES, the first item on the card.",
  parts=[
    ('a', "**PRES (posterior reversible encephalopathy).** When pressure rises faster than cerebral autoregulation can follow, and the endothelium is already damaged, fluid leaks into the white matter. The posterior circulation has the least sympathetic innervation, so the oedema is mainly parieto-occipital, bilateral and subcortical; hence headache, visual loss and seizures. On MRI it is bright on T2/FLAIR without restricted diffusion, because it is vasogenic, not cytotoxic. PRES is found in most women with eclampsia who are imaged, so it is the imaging face of eclampsia more than a rival diagnosis. Treatment is to control the pressure, give magnesium and remove the trigger, which here is the placenta."),
    ('b', "**Cerebral venous sinus thrombosis.** Pregnancy and especially the puerperium are prothrombotic. It presents with progressive headache, seizures and focal signs; imaging shows haemorrhagic venous infarcts that do not respect arterial territories, and venography shows the clot. Treatment is anticoagulation with heparin, even when the infarct is haemorrhagic."),
    ('c', "**Intracranial haemorrhage.** This is how severe hypertension kills in pre-eclampsia. Suspect it with sudden severe headache, a focal deficit or coma that persists after the seizure; CT shows it."),
    ('d', "**Meningitis, encephalitis; septic encephalopathy.** Fever, neck stiffness or a source of sepsis point here; lumbar puncture after imaging."),
    ('e', "**Brain tumour; gestational trophoblastic disease.** Choriocarcinoma metastasises to the brain and bleeds. A molar pregnancy is also the classic cause of pre-eclampsia before 20 weeks."),
    ('f', "**Drug intoxication or withdrawal.** Local anaesthetic toxicity during an epidural, alcohol or benzodiazepine withdrawal, hypoglycaemia and hyponatraemia are checked at the bedside."),
  ],
  table=dict(title="Seizing pregnant woman: reading the imaging", head=["Finding", "Diagnosis", "Treatment"], rows=[["Bilateral parieto-occipital FLAIR hyperintensity, **no diffusion restriction**", "**PRES**", "BP control, magnesium, delivery"], ["Restricted diffusion in an arterial territory", "arterial infarct", "stroke pathway"], ["Haemorrhagic infarct crossing territories, clot on venography", "**venous sinus thrombosis**", "heparin"], ["Blood on CT", "intracerebral or subarachnoid haemorrhage", "BP control, neurosurgery"]]),
  mimic=[
    ("PRES vs acute infarct", "PRES: bilateral, symmetrical, subcortical, no restricted diffusion, reverses in days to weeks. Infarct: restricted diffusion in one arterial territory."),
    ("PRES vs cerebral venous thrombosis", "Both give headache and seizures after delivery. Venous thrombosis: asymmetrical haemorrhagic infarcts, empty-delta sign, clot on venography."),
    ("PRES vs ‘hypertensive encephalopathy’", "Hypertensive encephalopathy names the clinical syndrome; PRES is the imaging diagnosis and the answer when an MRI is shown."),
  ],
  traps=[
    ("“Hypertensive encephalopathy” when an MRI is shown", "The examiners want PRES (88% right)."),
    ("“Cerebral venous thrombosis” or “acute ischaemic stroke” for bilateral parieto-occipital hyperintensity", "Symmetrical posterior vasogenic oedema is PRES (86%)."),
    ("“A complication of delivery before blood pressure was normalised”, “new epilepsy” or “high epidural block”", "For a seizure 15 minutes after delivery in a hypertensive woman with right upper quadrant pain, the key is the option that describes PRES: subcortical vasogenic oedema on imaging (60% right). It is eclampsia, and a high block causes hypotension and apnoea, not a seizure."),
    ("“Neurosurgical decompression” or “aciclovir” for PRES on ciclosporin", "Remove the trigger: reduce or withdraw the calcineurin inhibitor and control the pressure."),
  ],
  decode=[
    ("Eclampsia, seizures, MRI with bilateral parieto-occipital hyperintensities [DocT QBank]", "PRES."),
    ("Postpartum, history of eclampsia, altered mental status, FLAIR image [DocT QBank]", "PRES, not ‘hypertensive encephalopathy’."),
    ("Hypertensive in labour with RUQ pain, generalised seizure 15 minutes after delivery [DocT GT]", "Eclampsia: associated with subcortical vasogenic cerebral oedema on imaging."),
    ("Stem-cell transplant recipient on ciclosporin: seizures, hypertension, cortical blindness, posterior white-matter oedema [DocT GT]", "PRES from the calcineurin inhibitor: withdraw or reduce it and control the pressure."),
  ],
  punch="The eclamptic brain shows PRES, bilateral posterior vasogenic oedema without restricted diffusion, treated by pressure control, magnesium and removing the trigger; a focal, prolonged or late seizure needs imaging for venous thrombosis, haemorrhage or infection.",
)

L['OBS-27'] = dict(
  sub="Obstetrics → HELLP and fatty liver → HELLP: criteria and consequences",
  step=6,
  intro="Step 6 turns to the liver. HELLP is the same endothelial disease seen in the liver and the blood: damaged endothelium shreds red cells and consumes platelets, and fibrin in the sinusoids kills hepatocytes. It is the most examined card in the deck, with nine linked questions: the exact criteria, recognising it in a stem, the smear, the cause of the pain, the bleeding risk and what to do when it does not recover.",
  parts=[
    ('a', "**Haemolysis: abnormal smear (schistocytes); bilirubin 1.2 mg/dL or more; low haptoglobin; LDH at least twice normal.** Red cells are sheared as they pass fibrin strands in damaged small vessels, a microangiopathic haemolysis, so the smear shows fragments. The bilirubin is unconjugated and haptoglobin is used up. The Tennessee criteria that DocT keys state the LDH as over 600 IU/L."),
    ('b', "**Elevated liver enzymes: AST over 70 U/L (twice normal).** Fibrin deposition in the sinusoids causes periportal necrosis and haemorrhage. The liver swells and stretches its capsule, which is the mechanism of the epigastric or right upper quadrant pain and, at the extreme, of subcapsular haematoma and rupture (OBS-21). AST also rises from the haemolysis itself."),
    ('c', "**Low platelets: under 100,000.** Platelets are consumed on the activated endothelium. The count is the best marker of severity and of recovery: it reaches its lowest point one to two days after delivery and then rises; a count still falling after about 72 hours is not behaving like HELLP."),
  ],
  table=dict(title="Two classifications the questions use", head=["System", "Platelets", "AST", "LDH"], rows=[["**Tennessee** (all three = complete HELLP)", "**<100,000**", "**≥70 IU/L**", "**≥600 IU/L**"], ["Mississippi class 1", "≤50,000", "≥70", "≥600"], ["Mississippi class 2", ">50,000 to 100,000", "≥70", "≥600"], ["Mississippi class 3", ">100,000 to 150,000", "≥40", "≥600"]]),
  mimic=[
    ("HELLP vs TTP", "Both: schistocytes and low platelets. HELLP: hypertension, raised transaminases, improves within 72 hours of delivery. TTP: neurological signs and fever, near-normal transaminases, ADAMTS13 under 10%, does not improve after delivery; plasma exchange."),
    ("HELLP vs atypical HUS", "Atypical HUS: usually postpartum, renal failure dominates, complement-mediated; eculizumab."),
    ("HELLP vs catastrophic antiphospholipid syndrome", "In a woman with antiphospholipid syndrome, hypertension, proteinuria, raised AST, low platelets and schistocytes is still HELLP. The catastrophic syndrome adds thromboses in three or more organs within a week."),
    ("HELLP vs acute fatty liver", "Fatty liver: hypoglycaemia, raised INR and ammonia, encephalopathy (OBS-29)."),
    ("HELLP vs DIC", "Early HELLP has a normal PT, APTT and fibrinogen; these become abnormal only when DIC supervenes, as after abruption."),
  ],
  traps=[
    ("Tennessee options with platelets <150,000, AST >50 or LDH >250", "The set is platelets <100,000, AST >70 and LDH >600 (76% right)."),
    ("“Pre-eclampsia” or “catastrophic APS” when the stem gives all three of HELLP", "Once haemolysis, raised enzymes and low platelets are present the answer is HELLP (73% right in the antiphospholipid stem)."),
    ("“HELLP needs severe hypertension and heavy proteinuria”", "BP 152/98 with 0.6 g of protein was keyed HELLP; 10–20% of cases have neither hypertension nor proteinuria."),
    ("“Uterine atony” as the main reason for postpartum haemorrhage in HELLP", "DocT keys coagulopathy from platelet consumption (89%). Atony is the commonest cause of postpartum haemorrhage in general; the question asks what HELLP adds."),
    ("“Wait and watch” or “IVIG” when platelets keep falling and haemolysis worsens despite treatment", "The key is plasma exchange (66% right). Plasma exchange is only a weak indication for HELLP itself (ASFA category III, role not established); it is keyed because a picture that keeps worsening suggests TTP, where it is first-line (category I). Send ADAMTS13 before starting."),
    ("“Dexamethasone treats HELLP”", "It raises the platelet count but has not improved maternal outcomes; steroids are given for fetal lungs. Treatment is delivery."),
    ("“Basophilic stippling”, “target cells” or “acanthocytes” on the smear", "The smear of HELLP shows schistocytes (NEET 2025)."),
  ],
  decode=[
    ("Which laboratory combination is diagnostic of HELLP by the Tennessee criteria? [DocT QBank]", "Platelets <100,000, AST >70 IU/L, LDH >600 IU/L."),
    ("33 weeks, oedema, BP 152/98, protein 0.6 g/day, raised enzymes, low platelets, mild haemolysis [DocT GT, twice]", "HELLP syndrome."),
    ("Pre-eclampsia with abdominal pain and malaise — smear finding? [NEET 2025]", "Schistocytes."),
    ("Pre-eclampsia, RUQ pain, low platelets — mechanism of the pain? [Marrow]", "Distension of the hepatic (Glisson’s) capsule."),
  ],
  punch="HELLP is microangiopathic haemolysis with LDH over 600, AST over 70 and platelets under 100,000; the pain is a stretched liver capsule, the bleeding risk is from consumed platelets, the cure is delivery, and a picture still worsening after 72 hours is TTP until excluded.",
  extra=[
    dict(q="Major cause of the postpartum haemorrhage risk in HELLP?", a="Coagulopathy from platelet consumption (DocT key)."),
    dict(q="HELLP not recovering after delivery, platelets still falling — next step?", a="Send ADAMTS13 and start plasma exchange for presumed TTP."),
  ],
)

L['OBS-28'] = dict(
  sub="Obstetrics → HELLP and fatty liver → Acute fatty liver of pregnancy",
  step=6,
  intro="Step 6 continues with the rarer and more dangerous liver disease of late pregnancy. Acute fatty liver is acute liver failure: the hepatocytes cannot oxidise fatty acids, so they fill with fat and stop making glucose, urea and clotting factors. Both linked questions give the same triad of low glucose, raised INR and raised ammonia, and NEET 2025 asked for the treatment.",
  parts=[
    ('a', "**1 in 7,000–20,000 deliveries.** It is rare, so it is diagnosed only when someone thinks of it."),
    ('b', "**Third trimester; multiple gestation; underweight women.** Fatty-acid demand is highest late in pregnancy, and more so with twins. First pregnancy and a male fetus are further associations. About half of the women also have pre-eclampsia."),
    ('c', "**Microvesicular fatty infiltration of hepatocytes.** The mechanism is failed mitochondrial β-oxidation. In the best-described form the fetus lacks the enzyme LCHAD, and its unmetabolised long-chain fatty-acid intermediates cross to the mother and poison her hepatic mitochondria. The fat is in tiny droplets with the nucleus left central, as in Reye’s syndrome; the cells are not necrotic, which is why the transaminases are only moderately raised."),
    ('d', "**Nausea, vomiting, epigastric pain, anorexia, jaundice.** A week or two of vomiting and malaise in the third trimester is followed by jaundice and then encephalopathy. Persistent vomiting in late pregnancy should prompt liver tests."),
    ('e', "**Transaminases raised (up to about 1,000); high bilirubin, ammonia and INR; hypoglycaemia.** These are failures of synthesis and clearance: no gluconeogenesis, no urea cycle, no clotting factors. A raised creatinine, uric acid and white cell count are usual, and DIC with a low fibrinogen is common. The platelet count is often only mildly reduced, which separates it from HELLP (OBS-29)."),
    ('f', "**Bright liver on ultrasound; biopsy is definitive but avoided (bleeding).** Imaging is mainly to exclude a haematoma or obstruction and is often normal. The diagnosis is clinical, using the Swansea criteria (six or more of fourteen clinical and laboratory features)."),
  ],
  mimic=[
    ("Acute fatty liver vs HELLP", "Fatty liver: hypoglycaemia, raised INR and ammonia, encephalopathy, platelets near normal. HELLP: haemolysis, platelets low early, glucose and INR normal (OBS-29)."),
    ("Acute fatty liver vs acute viral hepatitis (hepatitis E)", "Viral hepatitis: transaminases in the thousands, any trimester, positive serology; delivery does not treat it."),
    ("Acute fatty liver vs intrahepatic cholestasis of pregnancy", "Cholestasis: itching, raised bile acids, the woman is well, no liver failure."),
  ],
  traps=[
    ("“HELLP” or “severe pre-eclampsia” for the 35-week stem with glucose 42, INR 2.4 and high ammonia", "LDH 720 and platelets of 100,000 pull towards HELLP, and the BP is 140/90, but a low glucose with a raised INR and ammonia means the liver has failed: acute fatty liver (69% right)."),
    ("“Supportive management until spontaneous recovery”", "It does not recover while the pregnancy continues; the key is emergency delivery after rapid stabilisation (NEET 2025)."),
    ("“Steroids with plasma exchange” or “liver transplantation first-line”", "Delivery is first; most women recover within days to weeks. Plasma exchange and transplantation are for failure to recover."),
    ("“A normal ultrasound excludes it” or “biopsy is needed”", "Neither; the diagnosis is clinical."),
  ],
  decode=[
    ("35 weeks, nausea, vomiting, jaundice, BP 140/90, platelets 100,000, AST 280, glucose 42, INR 2.4, raised ammonia — diagnosis? [DocT QBank]", "Acute fatty liver of pregnancy."),
    ("35 weeks, vomiting then jaundice, confusion, oliguria, INR 2.3, glucose 42, bright liver on ultrasound — immediate management? [NEET 2025]", "Emergency delivery, with glucose infusion and correction of coagulopathy."),
    ("[pattern] Baby of a woman who had acute fatty liver — what to screen for?", "LCHAD deficiency, which causes hypoketotic hypoglycaemia and cardiomyopathy in the infant."),
  ],
  punch="Acute fatty liver is third-trimester liver failure from failed fatty-acid oxidation: vomiting, then jaundice, with hypoglycaemia and a raised INR and ammonia but only modest transaminases; correct the glucose and clotting and deliver.",
)

L['OBS-29'] = dict(
  sub="Obstetrics → HELLP and fatty liver → HELLP vs acute fatty liver",
  step=6,
  intro="Step 6 ends by separating the two. Both arrive in the third trimester with vomiting, upper abdominal pain and raised transaminases, and both are treated by delivery, so the examiner asks you to name which one it is. The question behind the table is whether the liver is still doing its job.",
  parts=[
    ('a', "**Hypertension — HELLP: usual. Fatty liver: in about half.** HELLP is a form of severe pre-eclampsia, although 10–20% lack hypertension. Fatty liver overlaps with pre-eclampsia in about half, so blood pressure does not separate them."),
    ('b', "**Platelets — HELLP: low, early. Fatty liver: normal until DIC.** Platelet consumption is part of the definition of HELLP. In fatty liver the count falls later, as DIC develops."),
    ('c', "**Glucose — HELLP: normal. Fatty liver: low.** A failing liver cannot make glucose or release glycogen. Hypoglycaemia is the most useful single discriminator."),
    ('d', "**INR, ammonia — HELLP: normal (until late). Fatty liver: raised: true liver failure.** The INR rises because clotting factors are not made and ammonia because the urea cycle fails. In HELLP the clotting screen stays normal unless DIC supervenes."),
    ('e', "**Haemolysis — HELLP: yes. Fatty liver: no.** Schistocytes, a high LDH and a low haptoglobin belong to HELLP. In fatty liver the bilirubin is high and mostly conjugated, from hepatocyte failure, so jaundice is deeper than in HELLP."),
    ('f', "**Encephalopathy — HELLP: no. Fatty liver: yes.** Confusion with a high ammonia is hepatic encephalopathy. In HELLP an altered mental state means eclampsia, PRES or intracranial bleeding."),
  ],
  mimic=[
    ("HELLP vs acute fatty liver", "Coagulopathy out of proportion to the platelet count, hypoglycaemia and a raised ammonia point to fatty liver; schistocytes with platelets low early and a normal INR point to HELLP."),
    ("Either vs TTP", "TTP: schistocytes and very low platelets with fever and neurological signs, normal clotting screen, near-normal transaminases (OBS-27)."),
  ],
  traps=[
    ("“HELLP” because LDH is 720 and platelets are 100,000", "With glucose 42, INR 2.4 and a raised ammonia the answer is acute fatty liver (69% right). A high LDH alone is not haemolysis; damaged liver releases it too."),
    ("“Normal blood pressure excludes HELLP” or “hypertension excludes fatty liver”", "Neither holds; blood pressure does not discriminate."),
    ("“Low platelets exclude fatty liver”", "They fall once DIC develops."),
  ],
  decode=[
    ("35 weeks, vomiting, jaundice, BP 140/90, platelets 100,000, AST 280, LDH 720, glucose 42, INR 2.4, ammonia raised [DocT QBank]", "Acute fatty liver of pregnancy."),
    ("[pattern] 34 weeks, RUQ pain, schistocytes, platelets 60,000, AST 300, glucose and INR normal", "HELLP."),
    ("[pattern] Which single test best separates acute fatty liver from HELLP?", "Blood glucose (with INR and ammonia)."),
  ],
  punch="HELLP is a blood and endothelial disease with a working liver; acute fatty liver is liver failure. Low glucose, a raised INR and ammonia and encephalopathy mean fatty liver, and haemolysis with early low platelets means HELLP.",
)

FLAGS = {}
FLAGS['OBS-15'] = "Card agrees with ACOG PB 222 (2020). Additions only: proteinuria is also met by a protein/creatinine ratio ≥0.3 or dipstick 2+; ‘cerebral symptoms’ in ACOG is a new headache unresponsive to medication; ISSHP also accepts uteroplacental dysfunction (growth restriction) as the organ feature. No disagreement."
FLAGS['OBS-16'] = "The digit the card marks as unclear is 12 weeks (correct; Marrow key). Watch line omits ‘headache unresponsive to medication’ and ‘RUQ/epigastric pain’ wording but is otherwise ACOG’s list. The Marrow key counts early gestational age at onset as a marker of severe disease; that is not an ACOG severe feature. DocT GT says ‘up to 40%’ of gestational hypertension progresses; ACOG says up to 50%."
FLAGS['OBS-17'] = "Watch line lists vitamins C and E under prevention: trials were negative and ACOG/WHO do not recommend them. Aspirin (ACOG 81 mg from 12–28 weeks, ideally before 16; NICE 75–150 mg) and calcium only where dietary intake is low are the evidence-based measures. Explanation says so in a trap."
FLAGS['OBS-18'] = "Table matches ACOG PB 222 exactly. The DocT CGT2 key words nifedipine as ‘10–30 mg orally’; the card and ACOG say 10–20 mg. In the same question option C (magnesium loading dose in selected cases) is also true; key B is preferred because the asthma is the point of the stem."
FLAGS['OBS-19'] = "Card b ‘avoid diuretics’ needs its exception: pulmonary oedema is the one indication (DocT GT key). The 80 mL/h limit is NICE NG133’s figure for severe pre-eclampsia (confirmed; ACOG gives no number). Two keys are disputed: DocT keys magnesium alone as ‘initial management’ of BP 180/110 with pulmonary oedema (antihypertensive and furosemide are equally immediate); Marrow keys ‘controlled plasma volume expansion’, which is dated. Card e matches ACOG (no consensus for magnesium without severe features)."
FLAGS['OBS-20'] = "The table is the 2011 Sibai / 2013 ACOG Task Force algorithm. ACOG PB 222 (2020) keeps delivery at ≥34+0 weeks but lists HELLP, persistent symptoms and persistent reversed end-diastolic flow as conditions that preclude expectant care (deliver after stabilisation; a 24–48 h steroid delay for stable HELLP before 34 weeks is still accepted), and words ‘under 24 weeks’ as ‘before viability’. The DocT GT 29-week HELLP key (prompt delivery regardless of gestation) follows the 2020 wording; the DocT QBank 33-week key (48 h after steroids) follows the card. The card puts reversed end-diastolic flow in the 48-hour row; SMFM 2020 times delivery at 30–32 weeks for reversed and 33–34 weeks for absent flow."
FLAGS['OBS-21'] = "Table agrees with the Sibai/ACOG Task Force criteria. Watch-line figures (perinatal mortality 5–11.8%, maternal death up to 1.8%) could not be traced to a source and are not restated in the explanation."
FLAGS['OBS-22'] = "Percentages are restated as on the card (not re-verified; series differ, postpartum share quoted between about a quarter and a third). Card b ‘20%’: ACOG gives 20–38% without classic signs before the seizure."
FLAGS['OBS-23'] = "Card a ‘over 15–20 minutes’ is the Sibai wording; ACOG PB 222 says 20–30 minutes. Watch line ‘another 2 g bolus’: ACOG says 2–4 g over 5 minutes. Card d 4.8–8.4 mg/dL is correct for 2–3.5 mmol/L; ACOG’s quoted therapeutic range is 4.8–9.6 mg/dL. NICE NG133 uses 4 g over 5–15 minutes then 1 g/hour. Minor wording differences only."
FLAGS['OBS-25'] = "Card e ‘relative risk about 0.41’: the published Magpie figure is RR 0.42 (58% lower risk, 95% CI 40–71%); 10,141 women, 33 countries. Marrow tests the myasthenia contraindication, which the card only implies in its watch line."
FLAGS['OBS-27'] = "Card a ‘LDH at least twice normal’: the Tennessee criteria and ACOG state LDH ≥600 IU/L (the DocT key). Watch line incidence ‘20% of pre-eclamptics, 0.1–0.2% of pregnancies’: reviews give 10–20% of SEVERE pre-eclampsia and about 0.5–0.9% of pregnancies (ranges vary by source). A DocT QBank stem calls platelets of 70,000 ‘class I’; by the Mississippi system that is class 2 (class 1 is ≤50,000). Watch line ‘plasma exchange is only a category III indication’ is right (ASFA 2023: category III, grade 2C; TTP is category I). The plasma exchange key is right only because persistent worsening suggests TTP."
FLAGS['OBS-29'] = "Table is standard teaching and holds. Nuance: platelets in fatty liver are often mildly low even before overt DIC, and the DocT stem gives 100,000; glucose, INR and ammonia decide."
