# OBS02B — Explain v3 ("Learn" depth): obstetrics in critical care, part 2 — antepartum haemorrhage, postpartum haemorrhage (four Ts, uterotonics, the ladder), why obstetric bleeding is
# under-estimated, amniotic fluid embolism (facts, mechanism, treatment) and pregnancy-specific sepsis, peripartum cardiomyopathy, maternal cardiac arrest, ovarian hyperstimulation, stem cues, true/false.
# No mnemonics or hooks. Driven by the real questions in qpack/OBS02B.md (48 question links; OBS-33 the ladder asked 10 times, OBS-32 uterotonics 8, OBS-31 and OBS-35 six each, OBS-39 five).
# Fields as TOX01, plus SPINE, PRIMER and step. OBS-38, OBS-40, OBS-41 and OBS-43 have no linked question and get short explanations with [pattern] decode items.
# No `fix` entries exist for OBS02B in trace/test/data/qbank.json (checked 12 Nov 2026).
# Checked online on 12 Nov 2026:
#  - WHO/FIGO/ICM consolidated PPH guideline (launched 5 Oct 2025, FIGO congress, Cape Town): act at 300 mL of measured loss when any vital sign is abnormal as well as at the traditional 500 mL;
#    calibrated drape; MOTIVE bundle (Massage, Oxytocics, Tranexamic acid, IV fluids, Examination of the genital tract, Escalation); oxytocin or heat-stable carbetocin for prevention (FIGO and
#    Health Policy Watch reports of the guideline; the guideline text itself was not opened).
#  - AHA 2025 cardiac arrest in pregnancy algorithm: continuous left lateral uterine displacement when the fundus is at or above the umbilicus, IV above the diaphragm, most experienced operator for
#    the airway, if on IV magnesium stop it and give calcium, detach fetal monitors, prepare for resuscitative delivery at once and aim to deliver by about 5 minutes without ROSC, causes A to H,
#    massive transfusion protocol if amniotic fluid embolism is suspected.
#  - ESC 2025 pregnancy guideline (De Backer, Eur Heart J 2025), from summaries only: mWHO 2.0 classification, Pregnancy Heart Team from class II–III upwards, class IV handled by counselling on the
#    very high risk with shared decision-making including termination (class I), left uterine displacement at ≥20 weeks and IV access above the diaphragm (class I), caesarean considered if no ROSC
#    after 4 minutes, ACE inhibitors/ARBs/ARNI/renin inhibitors/SGLT2 inhibitors contraindicated, heart failure drugs for at least 12 months after recovery of PPCM, bromocriptine listed as an evidence gap.
#    The class IV list with its numbers (EF <30%, Marfan aorta >45 mm) is quoted from ESC 2018; I could not open the 2025 table.
#  - Obstetric shock index (Nathan/El Ayadi, PLoS One 2016, 958 women with hypovolaemic shock): ≥0.9 flags need for referral, ≥1.4 urgent intervention, ≥1.7 high chance of adverse outcome.
#  - Admission haemorrhage risk tables: ACOG Safe Motherhood version retrieved (medium: prior caesarean/uterine surgery, multiple gestation, >4 births, prior PPH, large fibroids, EFW >4000 g, BMI >40,
#    haematocrit <30% with other risks; high: praevia/low-lying, accreta, coagulopathy, active bleeding, platelets <70,000, two or more medium factors; type and screen vs type and cross).
# Second check (12 Nov 2026, independent reviewer): see obs02b_review.md. Corrected: praevia timing attribution (ACOG/SMFM vs RCOG GTG 27a), obstetric qSOFA systolic cut-off (<90),
# pyelonephritis course (14 days, ACOG 2023), ATLS responder bands, internal iliac ligation success softened; OBS-43 now has parts a–j.
# From standard references without a fresh check (confident): WOMAN trial (Lancet 2017; 20,060 women; death from bleeding 1.5% vs 1.9%, 1.2% vs 1.7% when given within 3 h; no benefit after 3 h; no
# fall in hysterectomy); carboprost 250 µg IM every 15–90 min to 8 doses (2 mg); methylergonovine 0.2 mg IM every 2–4 h; misoprostol 600–1000 µg (ACOG), 800 µg sublingual (WHO/FIGO);
# ACOG 2017 PPH definition (≥1000 mL or bleeding with signs of hypovolaemia); RCOG GTG 52 (minor 500–1000 mL, major >1000 mL; secondary PPH 24 h to 12 weeks); Charbit 2007 (fibrinogen <2 g/L);
# SMFM/Clark 2016 AFE criteria; ACOG/SMFM praevia delivery at 36+0 to 37+6 weeks; RCOG GTG 5 (2016) OHSS grading; ESC 2018 bromocriptine regimens; Elkayam 2001 (subsequent pregnancy after PPCM);
# ESC EORP PPCM registry (6% mortality at 6 months); magnesium toxicity levels; SOMANZ obstetric qSOFA.

SPINE = [
  ("Bleeding before delivery", "Painful bleeding with a tender, hard uterus is abruption even when the ultrasound is normal and little blood is seen; painless bright bleeding is praevia; pain followed by loss of contractions in a scarred uterus is rupture."),
  ("Bleeding after delivery: four causes", "Postpartum haemorrhage is tone, trauma, tissue or thrombin, atony is by far the commonest, and treatment climbs a fixed ladder from massage and oxytocin through a second uterotonic and tranexamic acid to tamponade, sutures, embolisation and hysterectomy."),
  ("Why the loss is under-estimated", "A term mother has about 45% more blood and a fibrinogen of 4–6 g/L, so her pressure holds until 1–1.5 L has gone and a fibrinogen under 2 g/L is already a warning."),
  ("Sudden collapse: embolism and sepsis", "Collapse with hypoxia in labour followed by bleeding from every puncture site is amniotic fluid embolism, an inflammatory reaction to fetal material that is treated by support, delivery and blood products."),
  ("The failing heart and arrest", "Peripartum cardiomyopathy is new heart failure with an ejection fraction under 45% around delivery, and a pregnant arrest is run as standard ACLS plus uterine displacement, access above the diaphragm and delivery by 5 minutes."),
  ("Hyperstimulation and reading the stem", "Ovarian hyperstimulation is a capillary leak graded by ascites and haematocrit, and in obstetric stems one planted phrase such as ‘no asthma’ or ‘ultrasound negative’ usually decides the answer."),
]

PRIMER = "By term the mother’s blood volume has risen by about 45% and her cardiac output by 30–50%, and the uterus receives roughly 700 mL of blood a minute, so obstetric bleeding is fast but her pulse and pressure hide it for a long time. Pregnancy is also a clotting state: fibrinogen doubles to 4–6 g/L, so a ‘normal’ adult value is low for her. Lying flat after 20 weeks, the uterus presses on the vena cava and aorta and cuts venous return, which matters in every collapse. OBS02A covered the physiology and hypertensive disease; this deck covers the emergencies in which she bleeds, collapses or arrests."

L = {}

L['OBS-30'] = dict(
  sub="Obstetrics → Haemorrhage → Antepartum haemorrhage",
  step=1,
  intro="Step 1 is bleeding before the baby is born. Three diagnoses matter, and they are separated at the bedside by pain and by the feel of the uterus, not by the amount of blood seen or by the scan. The real questions test exactly the point this card’s watch line makes: a negative ultrasound and little or no vaginal bleeding do not exclude abruption.",
  parts=[
    ('a', "**Pain: abruption severe and constant; praevia painless; rupture sudden, then the contractions stop.** In abruption blood dissects between the placenta and the uterine wall and irritates the muscle, which goes into sustained contraction, so the pain does not come and go as labour pain does. In praevia the placenta lies over the cervix and bleeds as the lower segment stretches, with no blood in the muscle and so no pain. A ruptured uterus can no longer contract as a unit, so strong labour pains are followed by sudden pain and then by quiet."),
    ('b', "**Bleeding: abruption dark and possibly concealed; praevia bright red and visible; rupture variable.** In abruption the blood may stay trapped behind the placenta, so the amount seen says nothing about the amount lost; the mother can be shocked with ‘minimal’ or no vaginal bleeding. In praevia the blood escapes straight through the cervix. In rupture most of the blood is in the abdomen."),
    ('c', "**Uterus: abruption tender and firm (woody); praevia soft; rupture with fetal parts easily palpable.** The hard, tender uterus is the single most useful sign of abruption. A soft, non-tender uterus with a high or abnormal presenting part fits praevia. In rupture the fetus may lie partly outside the uterus, so its parts are felt just under the abdominal wall and the presenting part recedes."),
    ('d', "**Clue: abruption with hypertension or trauma and a low fibrinogen; praevia with a previous caesarean section; rupture with a previous scar, in labour.** Abruption releases tissue factor from the placental bed and consumes clotting factors, so it is the antepartum bleed that causes DIC early; a fibrinogen of 130 mg/dL (1.3 g/L) in a pregnant woman is very low because her normal is 4–6 g/L (OBS-34). After blunt trauma in pregnancy, abruption is the diagnosis to exclude even when the FAST scan is negative, because FAST looks for free abdominal fluid and the blood of an abruption is inside the uterus."),
    ('e', "**Ultrasound: often normal in abruption; diagnostic in praevia.** Fresh clot has the same echo texture as placenta, so ultrasound misses at least half of abruptions; its job in a bleeding woman is to locate the placenta and so confirm or exclude praevia. Abruption is diagnosed clinically and on the fetal heart trace, and treated by resuscitation and delivery without waiting for imaging."),
  ],
  mimic=[
    ("Abruption vs placenta praevia", "Abruption: pain, hard tender uterus, fetal distress, shock out of proportion to visible loss, low fibrinogen, scan often normal. Praevia: painless, soft uterus, loss matches what is seen, scan shows the placenta over the os."),
    ("Abruption vs uterine rupture after trauma or in labour", "Rupture: previous uterine scar, contractions stop, fetal parts palpable, free fluid in the abdomen (FAST positive). Abruption: uterus hard and still contracting, FAST negative."),
    ("Praevia vs vasa praevia", "Vasa praevia: bleeding starts when the membranes rupture, the blood is fetal, so the fetus becomes bradycardic while the mother stays stable."),
  ],
  traps=[
    ("“Rule out abruption because the ultrasound is negative”", "Offered as option A in the DocT GT stem. Ultrasound misses most abruptions; hypotension, a tender uterus and fetal distress make the diagnosis and the answer is immediate obstetric help and preparation for delivery."),
    ("“Perform a digital vaginal examination”", "Never in antepartum bleeding until praevia has been excluded by scan: a finger through the os can tear a low placenta and cause torrential bleeding."),
    ("“Order MRI to confirm before intervening”", "A shocked mother with fetal distress is resuscitated and delivered; imaging that delays this is wrong."),
    ("“Emergency caesarean” vs “hospitalisation and pelvic rest” for a stable praevia bleed at 36 weeks (21% right)", "DocT keys admission and pelvic rest (the older expectant rule: stable mother and fetus, cross-match, steroids if under 34 weeks, deliver at 37 weeks). ACOG/SMFM now plan caesarean for an uncomplicated praevia at 36+0 to 37+6 weeks, and RCOG advises 34+0 to 36+6 weeks when there has been bleeding, so at 36 weeks with a repeat bleed she is already inside the delivery window and caesarean is the current-guideline answer. Know both: expectant care is right for a small bleed in a stable woman earlier in the third trimester; the key is disputed at 36 weeks."),
    ("“Uterine rupture” after a road accident with a negative FAST", "Rupture is rare without a scar and puts blood in the abdomen; tenderness, contractions and mild bleeding after trauma are abruption (72% right)."),
  ],
  decode=[
    ("30 weeks, road accident, uterine tenderness, regular contractions, mild bleeding, FAST negative — cause of bleeding? [DocT]", "Abruption (72%). Trauma plus a tender contracting uterus; FAST cannot see blood behind the placenta."),
    ("31 weeks, sudden severe pain, minimal bleeding, hypotension, tender uterus, fetal distress, ultrasound shows no placental abnormality — next step? [DocT GT]", "Immediate obstetric consultation and prepare for delivery. A normal scan does not exclude abruption."),
    ("36 weeks, known praevia, second painless bleed, stable — immediate management? [DocT]", "DocT key: hospitalisation and pelvic rest (21%). Current ACOG/SMFM and RCOG timing makes caesarean defensible at 36 weeks; no vaginal examination either way."),
  ],
  punch="Pain and a hard, tender uterus mean abruption whatever the scan and the pad show; a low fibrinogen confirms it. Ultrasound is for finding a praevia, and no finger goes into the cervix until it has.",
)

L['OBS-31'] = dict(
  sub="Obstetrics → Haemorrhage → Postpartum haemorrhage: definition and causes",
  step=2,
  intro="Step 2 moves to bleeding after delivery, the commonest cause of maternal death worldwide. The four Ts are a way to search: feel the uterus (tone), inspect the genital tract (trauma), check the placenta is complete (tissue), and look at whether the blood clots (thrombin). The six real questions give a bedside picture and ask which T it is, with uterine inversion asked three times.",
  parts=[
    ('a', "**Blood loss over 500 mL; massive over 1,000–1,500 mL.** This is the traditional WHO definition for the first 24 hours (primary PPH); bleeding from 24 hours onwards is secondary PPH. Other bodies draw the line elsewhere: ACOG (2017) uses 1,000 mL or more, or any loss with signs of hypovolaemia, whatever the route of delivery; RCOG calls 500–1,000 mL minor and over 1,000 mL major. The 2025 WHO/FIGO/ICM guideline keeps 500 mL but tells staff to act at 300 mL of measured loss if any vital sign is abnormal, because waiting for 500 mL misses women who are already compensating (OBS-34)."),
    ('b', "**Tone: soft, boggy uterus; treat with massage and uterotonics.** After the placenta separates, the spiral arteries are closed by the uterine muscle contracting around them, so a uterus that does not contract bleeds from an open placental bed. Atony causes about 70–80% of PPH. Its setting is an over-stretched or exhausted uterus: twins, a large baby, polyhydramnios, long labour, prolonged oxytocin (the receptors become desensitised), high parity, chorioamnionitis, and drugs that relax the uterus such as magnesium or volatile anaesthetics. Drugs are in OBS-32."),
    ('c', "**Trauma: tear, haematoma or inversion; suture, drain a haematoma over 3 cm, replace the uterus.** Suspect trauma when the uterus is firm and well contracted but bright bleeding continues, typically after an instrumental or rapid delivery. A haematoma gives pain and shock with little visible blood. Uterine inversion is the fundus turning inside out through the cervix: collapse straight after delivery, a mass in the vagina, and no fundus felt abdominally. The shock is out of proportion to the blood seen because traction on the ligaments triggers a vagal response as well as bleeding. Management is in order: stop uterotonics, resuscitate, push the uterus back at once with the placenta still attached (removing it first worsens bleeding), and only when it is back give oxytocin. If the first attempt fails because the cervical ring has tightened, relax the uterus with a tocolytic (terbutaline, glyceryl trinitrate or magnesium) or general anaesthesia and try again; hydrostatic reduction and surgery follow."),
    ('d', "**Tissue: retained placenta; manual removal, curettage.** Retained tissue stops the uterus contracting down fully. It is the usual cause of secondary PPH: heavy bleeding a day or more after delivery with a bulky, tender uterus and an open os, and an echogenic mass in the cavity with Doppler flow on ultrasound. Treat with a uterotonic, antibiotics and evacuation. A placenta that will not separate at all raises the question of accreta (OBS-33)."),
    ('e', "**Thrombin: blood not clotting; plasma, platelets, factors; recombinant factor VIIa.** Coagulopathy may be the cause (abruption, amniotic fluid embolism, HELLP, fatty liver, inherited disorders) or the result of massive bleeding and dilution. Replace fibrinogen early (OBS-34). Recombinant factor VIIa is an off-label rescue drug for life-threatening bleeding after surgery, transfusion and correction of fibrinogen, platelets, calcium, pH and temperature; it needs fibrinogen and platelets to work on and carries a risk of arterial thrombosis, so it is never first-line and never given ‘early before surgery’."),
  ],
  table=dict(title="Which T, from the bedside", head=["Finding", "T", "First action"], rows=[
    ["Soft, boggy, enlarged uterus", "**Tone**", "massage, oxytocin, then a second uterotonic"],
    ["Firm uterus, bright bleeding, instrumental delivery", "**Trauma** (tear)", "examine under good light, suture"],
    ["Collapse, mass in vagina, fundus not palpable", "**Trauma** (inversion)", "stop uterotonics, replace the uterus with placenta attached"],
    ["Day 2 or later, bulky tender uterus, open os", "**Tissue**", "uterotonic, antibiotics, evacuation"],
    ["Oozing from puncture sites, blood not clotting", "**Thrombin**", "fibrinogen, plasma, platelets"],
  ]),
  mimic=[
    ("Uterine inversion vs atony", "Both follow delivery with shock. Atony: a large soft fundus is felt above the umbilicus. Inversion: no fundus is felt abdominally and a mass fills the vagina."),
    ("Retained products vs subinvolution of the placental site", "Both give late bleeding with a bulky uterus. Retained products: echogenic mass in the cavity with colour-Doppler flow. Subinvolution: no mass."),
    ("Atony vs genital tract tear", "Atony: soft uterus. Tear: firm uterus, steady bright bleeding."),
  ],
  traps=[
    ("“Retained placenta” or “cervical laceration” for twins, prolonged oxytocin, magnesium and a boggy uterus", "Every item in that stem is a cause of atony and the uterus is described as boggy; tone is the answer."),
    ("“Remove the placenta first, then replace the inverted uterus”", "Removing it before reduction increases bleeding; replace the uterus with the placenta in place."),
    ("“Give oxytocin” when the first attempt at repositioning fails", "A contracted cervical ring is the obstacle; the next step is a tocolytic to relax it (Marrow), and oxytocin only after the uterus is back."),
    ("“rFVIIa is first-line” or “should be used early before surgery”", "It is an off-label last resort after surgical and transfusion measures (91% right)."),
    ("“Secondary PPH ends at 6 weeks” as a fixed fact", "Primary PPH is the first 24 hours and secondary PPH is everything after that. The card’s watch line ends it at 6 weeks, the end of the puerperium; RCOG and ACOG count it up to 12 weeks."),
  ],
  decode=[
    ("Collapse after delivery, severe bleeding, mass protruding through the vagina, uterus not palpable abdominally — diagnosis? [DocT; DocT GT]", "Uterine inversion (97–100%). The absent fundus decides it."),
    ("Inversion, placenta attached, first repositioning failed — next step? [Marrow]", "Tocolytics, then try again; oxytocin after reduction."),
    ("Twins, prolonged oxytocin, magnesium, profuse bleeding 15 minutes after delivery, enlarged boggy uterus — cause? [DocT GT]", "Uterine atony."),
    ("Postpartum day 2, heavy bleeding, bulky tender uterus, bleeding through the os, ultrasound image — diagnosis? [DocT]", "Retained products of conception (86%)."),
  ],
  punch="Feel the uterus first: soft means atony, firm means look for a tear, absent with a vaginal mass means inversion. Replace an inverted uterus before removing the placenta or giving oxytocin, and keep factor VIIa for the very end.",
  extra=[
    dict(q="Uterine inversion — order of management?", a="Stop uterotonics and resuscitate; manual replacement with the placenta attached; if it fails, tocolytic (terbutaline, glyceryl trinitrate, magnesium) or general anaesthesia and repeat; then hydrostatic or surgical reduction; oxytocin once reduced."),
  ],
)

L['OBS-32'] = dict(
  sub="Obstetrics → Haemorrhage → Uterotonic drugs",
  step=2,
  intro="Still in step 2: the drugs for the commonest T. Four drugs contract the uterus, each through a different receptor, and each has one patient in whom it is dangerous. Eight real questions come from this one table, nearly all asking which second drug to give or to avoid, and the stem decides it by mentioning asthma or blood pressure.",
  parts=[
    ('a', "**Oxytocin first: 20 IU per litre of saline, up to 500 mL over 10 minutes; a rapid bolus causes hypotension.** Oxytocin acts on its own receptor on uterine muscle within a minute and has a half-life of only a few minutes, so it is given as an infusion. It relaxes vascular smooth muscle, so an undiluted rapid bolus drops the blood pressure and causes tachycardia, which a bleeding woman tolerates badly. Receptors that have been exposed to oxytocin for hours in labour respond less, which is why atony after an augmented labour so often needs a second drug rather than more oxytocin."),
    ('b', "**Methylergonovine 0.2 mg IM; avoid in hypertension and pre-eclampsia.** Ergot alkaloids act on α-adrenergic and serotonin receptors and produce a sustained contraction of the uterus, but they constrict arteries by the same action. In a hypertensive or pre-eclamptic woman this can cause a hypertensive crisis, stroke or coronary spasm. The dose can be repeated every 2–4 hours. It is not a bronchoconstrictor in ordinary use and is the usual second drug for a normotensive asthmatic."),
    ('c', "**Carboprost (15-methyl PGF2α) 0.25 mg IM; avoid in asthma.** PGF2α contracts smooth muscle in the uterus and also in the bronchi, so it can cause severe bronchospasm, and it raises pulmonary vascular resistance and can cause desaturation. The dose is 250 micrograms intramuscularly (or into the myometrium), repeated every 15–90 minutes to a maximum of 8 doses, which is 2 mg in total. Diarrhoea, vomiting and fever are common."),
    ('d', "**Misoprostol (PGE1) 1,000 micrograms rectally; few contraindications, but slower.** PGE1 contracts the uterus without constricting the bronchi or the arteries, so it is safe in asthma and in hypertension; it is also cheap and stable at room temperature. It is slower and weaker than the injectable drugs and causes shivering and fever. Doses quoted are 600–1,000 micrograms; question stems usually write 800 micrograms."),
  ],
  table=dict(title="Second uterotonic after oxytocin: what the stem tells you", head=["Stem says", "Give", "Do not give"], rows=[
    ["No asthma, normal or low pressure", "**carboprost** or methylergonovine", ""],
    ["Asthma, normotensive", "**methylergonovine** (or misoprostol)", "carboprost"],
    ["Hypertension or pre-eclampsia", "**carboprost** (or misoprostol)", "methylergonovine"],
    ["Asthma and hypertension", "**misoprostol**", "carboprost, methylergonovine"],
    ["Carboprost already given, still bleeding", "repeat every 15–90 min to **8 doses (2 mg)**", ""],
  ]),
  mimic=[
    ("Carboprost (PGF2α) vs misoprostol (PGE1) vs dinoprostone (PGE2)", "Only the F-series prostaglandin constricts the bronchi. PGE1 is neutral and PGE2 is a bronchodilator, so both E-series drugs are safe in asthma."),
    ("Methylergonovine vs carboprost: the patient to avoid", "Ergot: hypertension, pre-eclampsia, coronary disease. Carboprost: asthma."),
  ],
  traps=[
    ("Not recognising “15-methyl PGF2α” as carboprost (53% right)", "The GT lists the chemical name. The drug to avoid in an asthmatic is 15-methyl PGF2α; PGE2 in the same list is a bronchodilator."),
    ("“Methylergonovine” keyed as the drug to avoid in asthma (DocT GT)", "In that question carboprost is not among the options, and DocT keys the ergot as the best available answer because ergots can occasionally provoke bronchospasm. If carboprost or 15-methyl PGF2α is offered, that is the answer."),
    ("“Misoprostol 800 micrograms rectally” keyed for the asthmatic with atony (DocT GT)", "Carboprost is correctly excluded. But methylergonovine is safe in asthma and is the usual second drug if she is not hypertensive; the stem gives no blood pressure, so the key is debatable. Choose misoprostol when the stem also gives hypertension, or when the keyed logic is ‘the prostaglandin that is safe in asthma’."),
    ("“Ergometrine IM” rejected for atony with BP 90/60 and no mention of asthma (62% right)", "DocT keys carboprost, but ergometrine is an equally valid second drug in a hypotensive woman with no hypertension (RCOG lists it before carboprost). Carboprost is acceptable only because the stem does not mention asthma."),
    ("“Repeat the oxytocin bolus”", "A rapid bolus causes hypotension in a woman at 90/60, and receptors already saturated in labour will not respond better."),
    ("“Maximum carboprost 1 mg or 1.5 mg”", "Eight doses of 250 micrograms is 2 mg (64–70% right)."),
  ],
  decode=[
    ("Atony after oxytocin and massage, BP 90/60, no asthma mentioned — next drug? [DocT]", "Carboprost IM (62%); ergometrine is equally acceptable by guideline."),
    ("Atony after oxytocin; ‘the patient is asthmatic’ — next agent? [DocT GT]", "Not carboprost. DocT keys misoprostol; methylergonovine is the usual choice if normotensive."),
    ("Uterotonic contraindicated in hypertension? [DocT] / to avoid in asthma? [DocT GT]", "Ergometrine (91%); 15-methyl PGF2α (53%)."),
    ("250 micrograms of carboprost given, still bleeding after 30 minutes — maximum total dose? [DocT GT ×2]", "2 mg (8 doses)."),
  ],
  punch="After oxytocin, the stem picks the drug: asthma rules out carboprost, hypertension rules out the ergot, and misoprostol is the one that is safe in both. Carboprost is 250 micrograms up to eight times, 2 mg in all.",
  extra=[
    dict(q="A uterotonic is given at caesarean for placenta praevia and the patient develops bronchospasm — which drug?", a="Carboprost (PGF2α) [Marrow]."),
  ],
)

L['OBS-33'] = dict(
  sub="Obstetrics → Haemorrhage → Postpartum haemorrhage: the ladder",
  step=2,
  intro="Step 2 ends with the order of treatment, the most-asked card in the deck (10 questions). The principle is to move from the least invasive measure upward without lingering on a rung that has failed, while resuscitating in parallel. Questions give the rungs already climbed and ask for the next one; whether she is stable decides between embolisation and surgery.",
  parts=[
    ('a', "**1. Prevent: active management of the third stage (oxytocin at delivery, controlled cord traction, uterine massage).** A uterotonic given as the baby is born (oxytocin 10 IU is the standard) makes the uterus contract as the placenta separates, and it carries almost all of the benefit. Controlled cord traction is done by a skilled attendant. Early cord clamping is no longer part of the package: the cord is clamped after 1–3 minutes."),
    ('b', "**2. Resuscitate: two large cannulae, oxygen, monitoring, bloods and cross-match.** Resuscitation runs alongside every later rung. Read the response to the first fluid bolus as in trauma: a woman whose pressure rises and then falls again within minutes with a rising pulse is a transient responder, which means ongoing bleeding of roughly 15–40% of her blood volume; she needs blood and control of the source, not observation and not vasopressors alone."),
    ('c', "**3. Bimanual massage and oxytocin; find which T.** Compressing the uterus between a hand on the abdomen and a fist in the vagina squeezes the placental bed while the drug works. At the same time examine for tears, check the placenta and look at whether the blood is clotting (OBS-31)."),
    ('d', "**4. Second uterotonic: carboprost, methylergonovine or misoprostol.** Chosen by asthma and blood pressure (OBS-32). Tranexamic acid belongs here too (the card’s watch line): 1 g IV as soon as PPH is diagnosed and within 3 hours of birth, repeated once if bleeding continues after 30 minutes. In the WOMAN trial (20,060 women) it cut death from bleeding from 1.9% to 1.5%, and from 1.7% to 1.2% when given within 3 hours; after 3 hours there was no benefit, and it did not reduce hysterectomy. Bleeding activates fibrinolysis early, so an antifibrinolytic works early or not at all."),
    ('e', "**5. Massive: transfuse red cells, platelets and factors; vasopressors.** Activate the massive transfusion protocol with balanced products and early fibrinogen (OBS-34). Vasopressors only bridge while volume is restored; they do not replace blood."),
    ('f', "**6. Tamponade or packing; compression (B-Lynch) sutures; vessel ligation or embolisation.** An intrauterine balloon presses on the placental bed from inside and is the first mechanical step for atony that has not responded to drugs; it controls bleeding in about 85% of reported cases. It does not work for a ruptured uterus or a lacerated artery. If the abdomen is open, a compression suture folds and squeezes the atonic uterus; stepwise devascularisation follows (uterine arteries, then utero-ovarian vessels, then the internal iliac arteries, which is technically difficult and less reliable: about 40–60% in the older series of internal iliac ligation alone, against about 85% when all ligation and devascularisation procedures are pooled). Embolisation by interventional radiology suits the woman who is still bleeding but haemodynamically stable enough to be moved; it succeeds in about 90% of reported cases and preserves the uterus."),
    ('g', "**7. Hysterectomy.** The definitive step when the others fail or when she is too unstable to try them. It is done sooner, without climbing the uterus-sparing rungs, in placenta accreta spectrum: the placenta has invaded the uterine wall and peeling it off tears the bed open, so the planned operation is caesarean hysterectomy with the placenta left in place."),
  ],
  table=dict(title="Uterotonics have failed: what next?", head=["Situation", "Next step", "Why"], rows=[
    ["Atony, vaginal delivery, any stability", "**balloon tamponade**", "least invasive mechanical step"],
    ["Atony, stable, balloon not offered or failed", "**uterine artery embolisation**", "uterus-sparing, about 90% success"],
    ["Angiogram shows a contrast blush", "**embolise** at the same sitting", "arterial bleeding; a balloon cannot stop it"],
    ["Abdomen open, atony", "**compression suture**, then vessel ligation", "quick, treats the atony"],
    ["Unstable, measures failed", "**hysterectomy**", "definitive"],
    ["Known accreta, massive bleeding", "**hysterectomy**, placenta in situ", "invaded bed cannot contract or be sutured"],
  ]),
  mimic=[
    ("Embolisation vs laparotomy", "Same bleeding, different patient: stable enough to go to radiology means embolisation; unstable means theatre."),
    ("Atony vs accreta at caesarean", "Both bleed from the placental bed and the uterus looks atonic. Atony gets the uterus-sparing ladder; accreta goes to hysterectomy."),
    ("Transient responder vs rapid responder", "Rapid: pressure stays up after the bolus, loss small (under about 15–20%). Transient: improves then falls again, ongoing bleeding, needs blood and source control."),
  ],
  traps=[
    ("“Within 1 hour” for tranexamic acid (43–47% right)", "The WOMAN trial’s result is benefit when given within 3 hours of birth. Earlier is better within that window, but the trial finding that is asked is 3 hours; after that there is none."),
    ("“Early cord clamping” as a component of active management (59% right)", "Not a component: clamping is delayed 1–3 minutes. The DocT question accepts uterotonic, controlled cord traction and uterine massage as components."),
    ("“Uterine artery embolisation” or “internal iliac ligation” as definitive surgery in accreta (68% right)", "These spare the uterus and treat atony; an invaded placental bed needs hysterectomy."),
    ("“Ligate the internal iliac arteries” after uterine artery ligation fails for atony (48% right)", "Two DocT tests carry this stem with different keys: one keys internal iliac ligation, the repeat keys compression sutures. Compression sutures are the better answer: quicker, treat the atony, and come before further ligation in the card and in RCOG/FIGO."),
    ("“High-dose misoprostol” after three uterotonics have failed", "More of a failed class adds nothing; move to a mechanical or radiological step (59–71% right)."),
    ("“Balloon tamponade” for suspected rupture, praevia bleeding or DIC", "The balloon’s indication is atony unresponsive to drugs (86% right)."),
    ("“Begin vasopressors only” for a transient responder", "She is still bleeding: continue fluid, give blood, control the source (93% right)."),
  ],
  decode=[
    ("Atonic PPH, uterotonics running — per the WOMAN trial, when should tranexamic acid be given? [DocT; DocT GT]", "Within 3 hours (43–47%)."),
    ("Oxytocin, methylergometrine and misoprostol given, still bleeding, atonic, haemodynamically stable — next? [DocT; DocT GT]", "Uterine artery embolisation (59–71%). ‘Stable’ decides it; a balloon would come first if it were offered."),
    ("Known accreta, caesarean, loss over 2,000 mL, uncontrolled — definitive surgical management? [DocT]", "Emergency hysterectomy (68%)."),
    ("Which is NOT a component of active management of the third stage? [DocT]", "Early cord clamping (59%)."),
  ],
  punch="Climb in order: massage and oxytocin, a second uterotonic with tranexamic acid inside 3 hours, balloon, compression suture and ligation or embolisation, hysterectomy. Stable goes to radiology, unstable goes to theatre, and accreta goes straight to hysterectomy.",
  extra=[
    dict(q="1 L bolus for postpartum bleeding: pressure improves, falls again within 15 minutes, pulse rising — what is this and what next?", a="A transient responder (ongoing loss of about 15–40%): continue fluids, transfuse, control the source [DocT GT, 93%]."),
    dict(q="Persistent PPH after caesarean; pelvic angiogram shows extravasation — treatment?", a="Uterine artery embolisation at the same sitting [DocT, 87%]."),
  ],
)

L['OBS-34'] = dict(
  sub="Obstetrics → Haemorrhage → Why obstetric bleeding is under-estimated",
  step=3,
  intro="Step 3 explains why the ladder of step 2 is so often started late. The mother’s own physiology hides the loss, staff cannot see or measure much of it, and the laboratory value that warns earliest is read against the wrong normal range. The two real questions test the consequence: balanced transfusion without waiting for results, and recognising DIC.",
  parts=[
    ('a', "**Blood volume is up 45%, so shock appears late: 1–1.5 L can be lost before the pressure falls.** The extra volume is a reserve built for delivery, and a young woman vasoconstricts strongly. Pulse and pressure stay near normal until a quarter or more of her blood volume has gone, and then she deteriorates quickly. A rising heart rate, a narrowing pulse pressure and a rising shock index (heart rate divided by systolic pressure; see the top-up card) change before the systolic pressure does."),
    ('b', "**Visual estimation of loss is unreliable; bleeding may be concealed.** Blood is mixed with amniotic fluid, soaked into drapes or on the floor, and staff under-estimate large losses by a third to a half. Blood may also be hidden behind the placenta (abruption, OBS-30), in the uterus, in a haematoma or in the abdomen. Weighing swabs and using a calibrated drape is more accurate, and the woman’s condition counts for more than the number."),
    ('c', "**Fibrinogen is normally high (4–6 g/L): a value under 2 g/L is already dangerous.** Fibrinogen is the first clotting factor to fall in obstetric bleeding, because the placental bed consumes it and transfusion dilutes it. A level reported as ‘low-normal’ for a non-pregnant adult has already halved for her. In Charbit’s study a fibrinogen under 2 g/L at the start of PPH predicted progression to severe haemorrhage in every case. Elsewhere in massive bleeding the replacement trigger is 1.5 g/L; in obstetrics it is 2 g/L."),
    ('d', "**Early fibrinogen replacement; massive transfusion protocol.** Give red cells, plasma and platelets in a balanced ratio (1:1:1) from the start, with cryoprecipitate or fibrinogen concentrate to keep fibrinogen above 2 g/L, calcium, warming and tranexamic acid (OBS-33). Waiting for the INR and platelet count before giving plasma means treating a coagulopathy after it is established. When the consumption runs ahead of replacement the picture is DIC: oozing from puncture sites, long PT and aPTT, low platelets and a very low fibrinogen."),
  ],
  mimic=[
    ("DIC vs HELLP", "Both lower the platelets. DIC: prolonged PT and aPTT and low fibrinogen. HELLP: clotting times and fibrinogen normal until late, with haemolysis and raised liver enzymes."),
    ("DIC vs acute fatty liver", "Fatty liver also prolongs the PT and lowers fibrinogen, but by failed synthesis: hypoglycaemia, high ammonia and jaundice precede any bleeding (OBS-42)."),
  ],
  traps=[
    ("“Continue red cells until the haemoglobin is normal”", "Red cells alone dilute clotting factors and platelets; after 3 units with ongoing bleeding the answer is balanced products."),
    ("“Wait for INR and platelet count”", "Results lag the bleeding; the protocol is started on clinical grounds (98% right)."),
    ("Reading a fibrinogen of 130–200 mg/dL as acceptable", "For a term mother that is less than half her normal and predicts severe haemorrhage; it was the planted clue in the abruption stem (OBS-30)."),
    ("“HELLP” for PT 22 s, aPTT 45 s, platelets 40,000, fibrinogen 80 mg/dL after massive PPH", "Prolonged clotting times with a very low fibrinogen and oozing from IV sites are DIC (89% right)."),
  ],
  decode=[
    ("Accreta at caesarean, loss over 2,000 mL, 3 units of red cells given, still bleeding — next step in transfusion? [DocT]", "FFP and platelets with red cells in a 1:1:1 ratio (98%)."),
    ("Massive PPH, oozing from IV sites, PT 22 s, aPTT 45 s, platelets 40,000, fibrinogen 80 mg/dL — diagnosis? [DocT]", "DIC (89%)."),
    ("Bleeding parturient with normal blood pressure and fibrinogen 1.8 g/L — interpretation? [pattern]", "Significant loss with early coagulopathy; replace fibrinogen and escalate."),
  ],
  punch="A normal blood pressure after delivery does not mean a small bleed: she can lose over a litre first. Read fibrinogen against 4–6 g/L, treat under 2 g/L as dangerous, and transfuse in balance without waiting for the laboratory.",
)

L['OBS-35'] = dict(
  sub="Obstetrics → Amniotic fluid embolism → Clinical facts and diagnosis",
  step=4,
  intro="Step 4 turns from bleeding to sudden collapse. Amniotic fluid embolism is rare, but it is the collapse that examiners write: a woman in labour or just delivered becomes hypoxic and hypotensive within minutes, may fit or arrest, and then bleeds from everywhere. Six real questions ask you to recognise it, choose the bedside investigation, and know that no laboratory test makes the diagnosis.",
  parts=[
    ('a', "**Rare: about 3.3 per 100,000 deliveries.** Published figures run from about 2 to 6 per 100,000 depending on how cases are defined. It is rare enough that no unit sees it often, yet it remains one of the leading direct causes of maternal death in high-income countries."),
    ('b', "**Mortality 15–85%; half die in the first hour.** The wide range reflects the era and the case definition: early registries that counted only the catastrophic cases reported 60–85%, and recent population studies using clinical criteria report about 20%. Deaths are early, from the first cardiopulmonary collapse; women who survive the first hour then face haemorrhage from DIC."),
    ('c', "**Sudden hypoxia (respiratory failure), hypotension or arrest, seizures, then DIC.** The order matters. Hypoxia and hypotension come first, from pulmonary vasospasm and acute right heart failure (OBS-36); seizures or loss of consciousness occur in a substantial minority; and coagulopathy follows within minutes to hours, sometimes as the only late sign in a woman who was resuscitated. Bilateral infiltrates on the chest film are common."),
    ('d', "**During labour, delivery or within 30 minutes after.** The timing is part of the diagnosis: fetal material can enter the maternal circulation only while the uterine veins are open, at rupture of membranes, in labour, at caesarean or as the placenta separates. Collapse days after delivery is something else (pulmonary embolism, cardiomyopathy, sepsis)."),
    ('e', "**Clinical, by exclusion.** The research criteria (SMFM and the AFE Foundation, 2016) require all four of: sudden cardiorespiratory arrest, or hypotension with respiratory compromise; overt DIC; onset in labour or within 30 minutes of delivery of the placenta; and no fever in labour. No test confirms it. Fetal squamous cells in maternal pulmonary blood were once called diagnostic but are found in pregnant women without the syndrome. Serum markers of fetal material (zinc coproporphyrin, a meconium pigment, and sialyl-Tn antigen) and low complement are research tests that support the diagnosis when asked. The most useful immediate investigation is echocardiography at the bedside or table: a dilated, failing right ventricle with an under-filled left ventricle supports the diagnosis and steers treatment."),
  ],
  mimic=[
    ("Amniotic fluid embolism vs pulmonary thromboembolism", "Both give sudden hypoxia, hypotension and a dilated right ventricle. Embolism of amniotic fluid: in labour or within 30 minutes of delivery, with seizures and early DIC and bleeding. Thromboembolism: usually days postpartum or antenatal, no DIC, leg signs or risk factors."),
    ("Amniotic fluid embolism vs anaphylaxis", "Anaphylaxis: a drug just given, rash, wheeze, angioedema, no early coagulopathy."),
    ("Amniotic fluid embolism vs eclampsia", "Eclampsia: seizure first, with hypertension and proteinuria; hypoxia and DIC are not the opening picture."),
    ("Amniotic fluid embolism vs peripartum cardiomyopathy", "Cardiomyopathy: breathlessness over days, left ventricular failure, no DIC (OBS-38)."),
  ],
  traps=[
    ("“D-dimer” or “troponin” as the supportive biomarker (34% right)", "Both rise in normal labour and in every differential, so neither helps. The marker the question wants is zinc coproporphyrin, a component of meconium in maternal serum; it is a research test and the diagnosis stays clinical."),
    ("“Fetal squames in the pulmonary circulation are the gold standard”", "They are found without the syndrome and are not diagnostic."),
    ("“CT pulmonary angiography” as the immediate investigation in collapse with coagulopathy at caesarean", "It means moving an unstable, bleeding patient. Transoesophageal (or transthoracic) echocardiography is done where she lies and shows the right ventricle (68% right)."),
    ("“Pulmonary thromboembolism” for hypoxia, hypotension, RV failure and thrombocytopenia with long PT in labour", "The coagulopathy and the timing in labour make it amniotic fluid embolism (75% right)."),
    ("“Thrombolysis for an amniotic clot in the pulmonary artery”", "There is no obstructing clot (OBS-36) and she is about to bleed from DIC."),
  ],
  decode=[
    ("38 weeks, in labour: sudden hypoxia, hypotension, low platelets, long PT, high D-dimer, echo with acute RV failure, bilateral infiltrates — diagnosis? [DocT]", "Amniotic fluid embolism (75%). Coagulopathy plus timing separate it from thromboembolism."),
    ("Suspected AFE — which biomarker best supports the diagnosis? [DocT]", "Zinc coproporphyrin (34%)."),
    ("Sudden cardiovascular collapse with coagulopathy during caesarean — most appropriate immediate investigation? [DocT]", "Transoesophageal echocardiography (68%)."),
    ("Rupture of membranes, then hypotension, cyanosis, seizure, arrest; after ROSC bleeds from IV sites — hallmark and priority? [DocT GT]", "RV failure, then LV failure and consumptive coagulopathy; management is supportive."),
  ],
  punch="Hypoxia and hypotension in labour or within half an hour of delivery, followed by DIC, is amniotic fluid embolism on clinical grounds alone. Echo at the bedside is the test to ask for; squames, D-dimer and troponin prove nothing.",
  extra=[
    dict(q="Collapse after caesarean and death; autopsy shows fibrin thrombi in the pulmonary vessels — cause?", a="DIC from amniotic fluid embolism: the triad is hypoxia, hypotension and coagulopathy [Marrow]."),
  ],
)

L['OBS-36'] = dict(
  sub="Obstetrics → Amniotic fluid embolism → Mechanism",
  step=4,
  intro="Still in step 4: why the collapse happens. The name suggests a plug of amniotic debris blocking the pulmonary arteries, and that is the old view. The answer examiners key is that fetal material in the maternal blood sets off a systemic inflammatory reaction, which explains what a mechanical plug cannot: the left heart failure, the DIC and the fact that most women with fetal cells in their blood are unharmed.",
  parts=[
    ('a', "**Trigger. Old view: amniotic debris (lanugo, vernix) through a torn uterine vein. Current view: fetal material entering the maternal circulation.** The entry route is the same: a breach between the amniotic sac and maternal veins at the cervix, the placental site or a uterine incision. What changed is the meaning of the material. Fetal cells reach the maternal circulation in many normal deliveries, so their presence is not the disease; the disease is an abnormal response to them in a few women."),
    ('b', "**Mechanism. Old view: mechanical obstruction of the pulmonary vessels. Current view: a maternal systemic inflammatory (anaphylactoid) response.** Fetal antigens and the vasoactive and procoagulant substances in amniotic fluid activate complement, mast cells and the clotting system and release mediators such as endothelin and leukotrienes. The picture resembles anaphylaxis and septic shock, which is why it has been called the anaphylactoid syndrome of pregnancy. It is not IgE-mediated: there is no prior sensitisation, and complement is consumed. Tissue factor in amniotic fluid explains the DIC but not the cardiopulmonary collapse."),
    ('c', "**Phase 1: pulmonary vasospasm, acute right heart failure, hypoxia.** The mediators constrict the pulmonary arteries intensely for minutes. The right ventricle dilates and fails, the septum bows into the left ventricle, left-sided filling and output fall, and the patient is hypoxic, hypotensive and may arrest. This is the phase seen on an early echo."),
    ('d', "**Phase 2: left ventricular failure, then DIC and haemorrhage.** In survivors the pulmonary pressure falls and the left ventricle fails, from ischaemia during phase 1 and from direct depression by mediators, giving pulmonary oedema. Capillary leak from the inflammatory response adds a non-cardiogenic component, so the oedema is mixed. Consumptive coagulopathy then produces bleeding, most obviously from the uterus, which also becomes atonic."),
  ],
  mimic=[
    ("Amniotic fluid embolism vs anaphylaxis (mechanism)", "Both release mast-cell and complement mediators. Anaphylaxis is IgE-mediated with prior sensitisation and no DIC; amniotic fluid embolism is not IgE-mediated and DIC is the rule."),
    ("Amniotic fluid embolism vs thromboembolism (mechanism)", "Thromboembolism is true mechanical obstruction and is treated by anticoagulation or lysis; amniotic fluid embolism is vasospasm and inflammation and is treated by support."),
  ],
  traps=[
    ("“Mechanical embolisation of amniotic debris”", "The old view and the commonest wrong choice; the keyed answer is systemic inflammatory activation by fetal material."),
    ("“IgE-mediated anaphylaxis”", "Anaphylactoid means it resembles anaphylaxis without IgE."),
    ("“Tissue factor activation of coagulation” as the primary mechanism", "It explains only the DIC, not the pulmonary vasospasm and heart failure."),
    ("“Cardiogenic pulmonary oedema from AFE” vs non-cardiogenic", "DocT’s keyed option says cardiogenic while its own explanation says non-cardiogenic. The oedema is mixed (left ventricular failure plus capillary leak); pick the option that names AFE oedema over pneumonia, embolism without infarction or atelectasis (89% right)."),
  ],
  decode=[
    ("Mechanism of amniotic fluid embolism? [DocT GT, card watch line]", "Maternal systemic inflammatory (anaphylactoid) response to fetal material; not mechanical, not IgE."),
    ("Collapse at caesarean, saturation 70%, then DIC; chest image with bilateral infiltrates — what does it represent? [DocT]", "Pulmonary oedema from AFE (89%); keyed as cardiogenic."),
    ("Sequence of haemodynamic failure in AFE? [DocT GT]", "Right ventricular failure first, then left ventricular failure and consumptive coagulopathy."),
  ],
  punch="Amniotic fluid embolism is an inflammatory reaction to fetal material, not a plug: first the right heart fails from pulmonary vasospasm, then the left heart fails and DIC begins.",
)

L['OBS-37'] = dict(
  sub="Obstetrics → Amniotic fluid embolism → Treatment; pregnancy-specific sepsis",
  step=4,
  intro="Step 4 closes with what to do. Because amniotic fluid embolism is an inflammatory collapse with no removable cause, treatment is support of each failing organ plus delivery; nothing specific reverses it. The card then lists the infections that pregnancy itself creates. The two real questions are a collapse after delivery where 60% chose the wrong first treatment, and the management of pyelonephritis.",
  parts=[
    ('a', "**Aggressive multi-organ support; correct coagulopathy; massive transfusion protocol.** Secure the airway and oxygenate; if she arrests, run the maternal algorithm (OBS-39). For the circulation, treat the phase you are in (OBS-36): the failing right ventricle wants noradrenaline to keep coronary perfusion, an inotrope such as dobutamine or milrinone, and a pulmonary vasodilator such as inhaled nitric oxide, not large volumes of fluid, which over-distend it. Activate the massive transfusion protocol as soon as the diagnosis is suspected, before the bleeding starts, with early fibrinogen (OBS-34). Atropine, ondansetron and ketorolac have been proposed as an adjunct and are unproven."),
    ('b', "**Emergency delivery; caesarean with ligation of uterine or internal iliac arteries, even hysterectomy.** If she is undelivered, delivering the baby relieves aortocaval compression and improves resuscitation, and the fetus is at risk from maternal hypoxia. The uterus then bleeds from atony and DIC together, so the PPH ladder (OBS-33) is climbed quickly, up to hysterectomy."),
    ('c', "**VA-ECMO has reduced mortality.** Veno-arterial ECMO supports both the failing heart and the lungs through a phase that often reverses within hours to days, and it is recommended for refractory collapse where available. The evidence is case series, not trials, and anticoagulating a woman in DIC is the practical difficulty."),
    ('d', "**Chorioamnionitis (altered vaginal pH, amniocentesis); pyelonephritis (ureteric tone lost to progesterone; Gram-negative colonisation); endometritis (instrumentation); pneumonia.** These are the sources to look for in a septic pregnant or postpartum woman. Chorioamnionitis is ascending infection of the membranes, usually after prolonged rupture; treatment is antibiotics and delivery. Pyelonephritis follows from progesterone relaxing the ureters and the uterus compressing them, so urine stagnates and bladder bacteria ascend; it is treated in hospital with an IV cephalosporin such as ceftriaxone and fluids to keep a good urine output, switched to oral treatment once afebrile for 24–48 hours, to complete 14 days in total (ACOG), and it can be complicated by ARDS. A week of treatment is not enough because the infection is in the renal parenchyma and relapse is common in pregnancy, which is also why suppressive treatment is often continued until delivery. Endometritis follows caesarean or instrumentation. Pregnant women also do worse with pneumonia, influenza in particular."),
  ],
  mimic=[
    ("Amniotic fluid embolism vs massive pulmonary embolism right after delivery", "Both show a dilated right ventricle on echo. DIC, seizures and onset within 30 minutes of delivery point to amniotic fluid embolism, and only confirmed pulmonary embolism is anticoagulated or lysed."),
    ("Chorioamnionitis vs endometritis", "Chorioamnionitis: before delivery, maternal fever with fetal tachycardia and uterine tenderness. Endometritis: after delivery, fever with a tender uterus and foul lochia."),
  ],
  traps=[
    ("“Immediate anticoagulation with heparin” for collapse with a dilated RV just after delivery in a woman with antiphospholipid syndrome (40% right)", "The antiphospholipid syndrome is there to pull you toward thromboembolism. Collapse with acute right heart failure immediately after delivery is amniotic fluid embolism until proved otherwise, and DIC is about to appear in a uterus that has just delivered; the first step is supportive care with oxygen, vasopressors and careful fluids."),
    ("“Emergency thrombolysis”", "Only for confirmed massive pulmonary embolism or arrest from it; in amniotic fluid embolism it adds bleeding and removes nothing."),
    ("“Corticosteroids and IVIG”", "Unproven for either diagnosis in this setting."),
    ("“Discharge after 72 hours afebrile with 5 days of antibiotics” for pyelonephritis in pregnancy", "The incorrect statement in the Marrow question: she can go home once afebrile for 24–48 hours, without waiting 72, and the course is 14 days by ACOG (Marrow’s note says 7–10), not 5."),
  ],
  decode=[
    ("Known APS, sudden breathlessness and hypotension immediately after vaginal delivery, echo: dilated RV, raised PA pressure — initial management? [DocT]", "Supportive care with fluids, vasopressors and oxygen (40%)."),
    ("Pyelonephritis in pregnancy — incorrect management statement? [Marrow]", "Discharge after 72 hours afebrile with 5 days of antibiotics."),
    ("AFE with refractory cardiogenic shock despite inotropes — rescue? [pattern]", "VA-ECMO."),
  ],
  punch="Treat amniotic fluid embolism by supporting the right heart, delivering the baby and transfusing early; do not anticoagulate or thrombolyse on suspicion. VA-ECMO is the rescue.",
  extra=[
    dict(q="Pyelonephritis in pregnancy — outline of management?", a="Admit; IV ceftriaxone; fluids to keep urine output up; oral antibiotics once afebrile 24–48 h; 14 days in total (ACOG; 7–10 in Marrow’s note); then consider suppression for the rest of pregnancy. Watch for ARDS."),
  ],
)

L['OBS-38'] = dict(
  sub="Obstetrics → Heart → Peripartum cardiomyopathy",
  step=5,
  intro="Step 5 is the heart. Peripartum cardiomyopathy is heart failure from a weak left ventricle that appears around delivery in a woman with no previous heart disease. It is easy to miss because breathlessness, oedema and tiredness are normal in late pregnancy. No bank question is linked to this card, so the explanation is kept to the definition and the drug rules.",
  parts=[
    ('a', "**Cardiomyopathy arising in the last month of pregnancy or the first 5 months postpartum, with no other cause.** This is the classic time window; most cases present in the first weeks after delivery. The European definition is looser (‘towards the end of pregnancy or in the months following delivery’). It is a diagnosis of exclusion: pre-existing dilated cardiomyopathy, valve disease, pre-eclampsia with pulmonary oedema, myocardial infarction and pulmonary embolism must be ruled out."),
    ('b', "**Ejection fraction under 45%.** Left ventricular systolic dysfunction on echo is required; the ventricle may or may not be dilated. An ejection fraction under 30% at presentation predicts a poor recovery, but it is not the diagnostic cut-off (OBS-43j)."),
    ('c', "**About 1 in 3,500; mortality 20–50%.** Incidence varies widely with ancestry and region, from about 1 in 1,000–4,000 in the United States to about 1 in 100–300 in Nigeria and Haiti. The mortality figure on the card comes from older series; with modern heart-failure treatment it is about 5–10% (6% at 6 months in the European registry). Risk factors are older age, multiple pregnancy, pre-eclampsia and African ancestry."),
    ('d', "**ACE inhibitors and ARBs (allowed postpartum).** In the second and third trimesters they cause fetal renal failure, oligohydramnios and skull defects. Sacubitril–valsartan, spironolactone, ivabradine and SGLT2 inhibitors are also avoided in pregnancy. After delivery standard heart-failure drugs are started; enalapril and captopril are compatible with breastfeeding."),
    ('e', "**Beta-blockers, diuretics, hydralazine and nitrates, digoxin.** Hydralazine with a nitrate replaces the ACE inhibitor as the vasodilator before delivery. A β1-selective blocker such as metoprolol is used; diuretics are given for congestion but cautiously, because they can reduce placental blood flow."),
    ('f', "**Persistent LV dysfunction = poor prognosis; it can recur: contraception counselling.** About half or more recover an ejection fraction above 50%, mostly within 6 months. If the ventricle has not recovered, another pregnancy carries a high risk of deterioration and death (about a fifth in older series) and is advised against; even after recovery about a fifth relapse."),
  ],
  mimic=[
    ("Peripartum cardiomyopathy vs pre-eclampsia with pulmonary oedema", "Pre-eclampsia: hypertension, proteinuria, preserved ejection fraction. Cardiomyopathy: ejection fraction under 45%."),
    ("Peripartum cardiomyopathy vs pulmonary embolism postpartum", "Embolism: sudden onset, right ventricular strain, clear lung fields. Cardiomyopathy: orthopnoea over days, crackles, a poorly contracting left ventricle."),
  ],
  traps=[
    ("“Ejection fraction under 30% is required”", "The criterion is under 45%."),
    ("“ACE inhibitors are contraindicated throughout”", "Only until delivery; they are started postpartum."),
    ("“She has recovered, so another pregnancy is safe”", "Recurrence occurs even after recovery, and persistent dysfunction makes a further pregnancy very high risk."),
  ],
  decode=[
    ("Two weeks postpartum, orthopnoea, no previous heart disease, echo EF 35% — diagnosis and the drug class now allowed? [pattern]", "Peripartum cardiomyopathy; ACE inhibitors can be started because she has delivered."),
    ("36 weeks pregnant with new LV failure — which vasodilator? [pattern]", "Hydralazine with a nitrate; not an ACE inhibitor or ARB."),
  ],
  punch="New heart failure in the last month of pregnancy or the five months after, with an ejection fraction under 45% and no other cause. Hydralazine and nitrates before delivery, ACE inhibitors after it, and counsel against another pregnancy if the ventricle has not recovered.",
  extra=[
    dict(q="Two additions from the card’s watch line — when?", a="Bromocriptine (suppresses prolactin, whose cleaved fragment is thought to injure the myocardium) may be added to standard treatment, always with at least prophylactic anticoagulation; anticoagulate when the ejection fraction is very low (about ≤35%) because of ventricular thrombus."),
  ],
)

L['OBS-39'] = dict(
  sub="Obstetrics → Arrest → Cardiac arrest in pregnancy",
  step=5,
  intro="Step 5 ends with arrest. The algorithm is ordinary ACLS; pregnancy changes only what the uterus changes: venous return, the airway, where the cannula goes, and the option of emptying the uterus. Five real questions each test one modification, and two of them (adrenaline 54%, hypermagnesaemia 61%) show that people expect more to be different than is.",
  parts=[
    ('a', "**Continuous manual left uterine displacement.** From about 20 weeks, when the fundus is at or above the umbilicus, the supine uterus compresses the vena cava and aorta and cuts venous return, so chest compressions generate little output. One rescuer pushes or pulls the uterus to the mother’s left with the hands throughout. Manual displacement keeps her flat on a firm surface; tilting the whole patient makes compressions less effective."),
    ('b', "**IV access above the diaphragm.** Drugs and fluid given into a leg or femoral vein must pass the compressed vena cava and may not reach the heart. Use an arm, neck or humeral intraosseous site."),
    ('c', "**Expect a difficult airway: most experienced operator; 100% oxygen; waveform capnography; then 1 breath every 6 seconds with continuous compressions.** Airway oedema, large breasts and a full stomach make intubation harder, and a low FRC with high oxygen consumption makes her desaturate fast, so the airway is managed early by the best operator with a smaller tube. Once the airway is in, ventilation is 10 a minute without pausing compressions, as in any arrest."),
    ('d', "**If on magnesium: stop it and give calcium.** A woman on magnesium for pre-eclampsia who becomes bradycardic and arrests has magnesium toxicity until proved otherwise, particularly with oliguria, since magnesium is cleared by the kidney. Toxicity runs in order: loss of the patellar reflex, respiratory depression, conduction block, arrest. Calcium antagonises it at the membrane: calcium chloride 10% 10 mL or calcium gluconate 10% 30 mL IV."),
    ('e', "**Perimortem caesarean: if no return of circulation, aim to deliver by 5 minutes.** Prepare from the moment the arrest is recognised, and if circulation has not returned after about 4 minutes of resuscitation, deliver so that the uterus is empty by 5 minutes. Its purpose is maternal: emptying the uterus removes aortocaval compression and returns blood to her circulation, and survival of both mother and baby falls with each minute of delay. It is done where she lies, without moving to theatre, without checking for a fetal heart, and whether or not the fetus is viable, in any woman whose fundus is at or above the umbilicus. The current name is resuscitative hysterotomy."),
    ('f', "**Detach fetal monitors; call the neonatal team.** Fetal monitoring does not alter maternal resuscitation and gets in the way of defibrillation and delivery. The fetus is treated by resuscitating the mother."),
    ('g', "**Compressions, defibrillation energy and drug doses are unchanged.** Hand position, rate and depth are standard. Shocks are given at the usual energies: the fetus receives negligible current and maternal circulation is its only chance. Adrenaline 1 mg every 3–5 minutes is the vasopressor, as in any arrest, and no drug is withheld for fear of harming the fetus."),
  ],
  mimic=[
    ("Magnesium toxicity vs eclampsia as the cause of collapse on a magnesium infusion", "Toxicity: absent reflexes, slow breathing, bradycardia, often oliguria. Eclampsia: seizure with brisk reflexes and hypertension."),
    ("Vasopressor during arrest vs for spinal hypotension", "Arrest: adrenaline. Spinal hypotension at caesarean: phenylephrine. The DocT question on the first-line vasopressor in arrest offers phenylephrine as the distractor."),
  ],
  traps=[
    ("“Phenylephrine” or “noradrenaline” as first-line vasopressor in maternal arrest (54% right)", "Phenylephrine is the obstetric anaesthetist’s drug for spinal hypotension, which is why it attracts. In cardiac arrest the drug is adrenaline at the standard dose."),
    ("“Hypokalaemia” as the first electrolyte to suspect in bradycardia progressing to arrest (61% right)", "A pregnant woman in the ICU is likely to be on magnesium; bradycardia then arrest is hypermagnesaemia. Stop the infusion and give calcium."),
    ("“Halve the defibrillation energy” or “defibrillation is contraindicated”", "Standard energies, no modification (81% right)."),
    ("“Perimortem caesarean after 20 minutes of CPR” or “only after fetal demise is confirmed”", "By 5 minutes, for the mother’s benefit, without assessing the fetus (92% right)."),
    ("“Half-dose adrenaline because of pregnancy” or “give magnesium during the arrest”", "Doses are unchanged; magnesium is stopped, not started."),
  ],
  decode=[
    ("28 weeks, arrest in the ICU — the most critical modification of ACLS? [DocT]", "Manual left uterine displacement (97%)."),
    ("34 weeks, arrest — timing of perimortem caesarean? [DocT]", "Within 5 minutes of arrest if no ROSC (92%)."),
    ("First-line vasopressor in maternal cardiac arrest? [DocT]", "Adrenaline (54%)."),
    ("Third trimester, ventricular fibrillation — true statement on defibrillation? [DocT]", "Standard energy doses without modification (81%)."),
    ("Pregnant ICU patient, bradycardia progressing to arrest — electrolyte to suspect first? [DocT]", "Hypermagnesaemia (61%)."),
  ],
  punch="Maternal arrest is standard ACLS with the uterus pushed left, the cannula above the diaphragm, magnesium stopped and calcium given, and the uterus emptied by 5 minutes. Adrenaline, shocks and compressions do not change.",
)

L['OBS-40'] = dict(
  sub="Obstetrics → Ovarian hyperstimulation syndrome → Severity",
  step=6,
  intro="Step 6 begins with a condition of fertility treatment, not of pregnancy itself. After ovarian stimulation and an hCG trigger, the enlarged ovaries release vascular endothelial growth factor, capillaries leak, and fluid moves from the blood into the abdomen and chest. The grading (RCOG) follows that leak: where the fluid is and how concentrated the blood has become. No bank question is linked to this card.",
  parts=[
    ('a', "**Mild: bloating, mild pain; ovaries usually under 8 cm.** The ovaries are enlarged but the leak is small. Managed at home with fluids to thirst and paracetamol."),
    ('b', "**Moderate: nausea, vomiting; ascites on ultrasound; ovaries 8–12 cm.** The dividing line from mild is fluid that can be seen on a scan but not yet felt."),
    ('c', "**Severe: clinical ascites (with or without hydrothorax); oliguria (under 300 mL/day or 30 mL/h); haematocrit over 0.45; sodium under 135; osmolality under 282; albumin under 35 g/L; ovaries over 12 cm.** Ascites is now clinically obvious, and the laboratory shows what has left the vessels: water (haemoconcentration, oliguria) and albumin. Sodium is low because volume depletion drives ADH release and water retention. This grade is admitted."),
    ('d', "**Critical: tense ascites; haematocrit over 0.55; white cells over 25,000; anuria; thromboembolism; ARDS.** Organ failure or thrombosis defines it. Tense ascites raises intra-abdominal pressure and worsens renal perfusion and breathing; very thick blood clots. This grade is for intensive care."),
  ],
  mimic=[
    ("Severe vs critical", "Severe: clinical ascites, haematocrit over 0.45, oliguria. Critical: tense ascites, haematocrit over 0.55, anuria, thrombosis or ARDS."),
    ("Hyperstimulation vs ovarian torsion or ruptured cyst", "All follow stimulation with pain and large ovaries. Sudden severe one-sided pain suggests torsion; a falling haematocrit suggests bleeding, where hyperstimulation makes it rise."),
  ],
  traps=[
    ("Grading by ovarian size alone", "Size is ‘usually’ in each grade; ascites, urine output and haematocrit decide."),
    ("Reading a haematocrit of 0.47 as reassuring", "It is haemoconcentration from a leak and places her in the severe grade."),
  ],
  decode=[
    ("Day 7 after hCG trigger, distended abdomen with clinical ascites, urine 20 mL/h, haematocrit 0.48 — grade? [pattern]", "Severe."),
    ("Same patient with haematocrit 0.57, white cells 28,000 and a jugular vein thrombosis — grade? [pattern]", "Critical."),
  ],
  punch="Ascites seen only on scan is moderate, felt at the bedside is severe, and tense with a haematocrit over 0.55, anuria, clot or ARDS is critical.",
)

L['OBS-41'] = dict(
  sub="Obstetrics → Ovarian hyperstimulation syndrome → Treatment",
  step=6,
  intro="Still in step 6. The leak of OBS-40 stops by itself as hCG clears (within about two weeks, longer if she conceives), so treatment keeps her safe until then: maintain the circulating volume, relieve tense ascites and prevent clots. No bank question is linked to this card.",
  parts=[
    ('a', "**Supportive: hydration, electrolyte correction, organ support.** She is depleted inside the vessels although she looks fluid-overloaded. Let her drink to thirst; give crystalloid if she cannot, guided by urine output and haematocrit, without over-filling, because extra fluid leaks into the abdomen. Albumin is used when large volumes of ascites are drained or she stays oliguric."),
    ('b', "**Paracentesis for tense ascites.** Draining ascites under ultrasound guidance lowers intra-abdominal pressure, which improves renal blood flow, urine output and breathing. Indications are tense ascites with discomfort or breathlessness, and oliguria that persists despite adequate volume."),
    ('c', "**DVT prophylaxis: haemoconcentration makes it prothrombotic.** High oestradiol, thick blood and immobility together raise the risk of venous and arterial thrombosis, characteristically in the neck and arm veins. All admitted patients get low-molecular-weight heparin, continued through the first trimester if she is pregnant."),
    ('d', "**Avoid diuretics while haemoconcentrated.** A diuretic removes more water from an already depleted circulation, worsening renal perfusion and the tendency to clot, and does not mobilise the ascites. It has a place only after volume is restored and oliguria persists, usually after paracentesis."),
  ],
  mimic=[
    ("Oliguria of hyperstimulation vs oliguria of fluid overload", "Hyperstimulation: high haematocrit, ascites, low intravascular volume; treat with volume and paracentesis. Overload: low or normal haematocrit; treat with a diuretic."),
  ],
  traps=[
    ("“Furosemide for the ascites and oliguria”", "She is haemoconcentrated; diuretics worsen it."),
    ("“Thromboprophylaxis is not needed in a young woman”", "It is always given in admitted cases."),
  ],
  decode=[
    ("Severe hyperstimulation, tense ascites, breathless, urine output falling despite fluids — next step? [pattern]", "Ultrasound-guided paracentesis."),
    ("Haematocrit 0.50 and oliguria — which drug to avoid, which to give? [pattern]", "Avoid diuretics; give low-molecular-weight heparin prophylaxis."),
  ],
  punch="Support the circulation, drain tense ascites, give heparin prophylaxis to everyone admitted, and keep diuretics away while the haematocrit is high.",
)

L['OBS-42'] = dict(
  sub="Obstetrics → Exam technique → Planted cues in obstetric stems",
  step=6,
  intro="Step 6 continues with how the stems are written. Obstetric questions in these banks rarely turn on a rare fact; they turn on one phrase the examiner has added to make a single option correct. This card collects eight such phrases from OBS02A and this deck, and the five linked questions are the ones in which that phrase decided the key.",
  parts=[
    ('a', "**“No history of asthma”: carboprost (or labetalol) is allowed.** Both drugs constrict the bronchi, carboprost through PGF2α and labetalol through β2 blockade. Writing ‘no asthma’ removes the only objection to them. The reverse cue, ‘history of asthma’, removes them: in severe pre-eclampsia at 182/116 with asthma, the IV antihypertensive to avoid is labetalol."),
    ('b', "**“No bradycardia or conduction disease”: labetalol.** The other objections to a β-blocker are heart block, bradycardia and decompensated heart failure; a stem that excludes them is pointing at labetalol for severe hypertension."),
    ('c', "**“After magnesium, BP remains 176/114”: now treat the blood pressure with labetalol.** Magnesium prevents seizures and lowers pressure very little. A pressure of 160/110 or more is treated promptly with an antihypertensive (IV labetalol, IV hydralazine or oral nifedipine) to prevent stroke; more magnesium is the wrong answer."),
    ('d', "**“No vaginal bleeding; ultrasound negative” with a tender uterus: concealed abruption.** Both negatives are there to mislead; the tender, hard uterus decides (OBS-30)."),
    ('e', "**Collapse, then seizure, then bleeding from IV sites, in labour: amniotic fluid embolism.** The order and the timing are the diagnosis (OBS-35)."),
    ('f', "**“Despite adequate pre-oxygenation”: low FRC, high oxygen consumption.** FRC falls by about 20% at term and oxygen consumption rises by about 20%, so the oxygen store is smaller and is used faster; she desaturates within a couple of minutes of apnoea even after good pre-oxygenation."),
    ('g', "**Low fibrinogen: abruption or embolism with DIC.** Against a normal of 4–6 g/L, a low value means consumption (OBS-34)."),
    ('h', "**Hypoglycaemia with jaundice in the third trimester: fatty liver, not HELLP.** Acute fatty liver is failure of hepatic synthesis, so glucose falls, ammonia and INR rise and jaundice appears, out of proportion to the platelet count. HELLP is a microangiopathy: haemolysis, low platelets and raised enzymes with glucose and clotting preserved until late."),
  ],
  mimic=[
    ("Acute fatty liver vs HELLP", "Fatty liver: hypoglycaemia, high ammonia, INR prolonged out of proportion to platelets, jaundice, often normal or mildly raised pressure. HELLP: hypertension, haemolysis, platelets low, glucose and INR normal."),
    ("Labetalol vs hydralazine by cue", "Asthma, bradycardia or heart block in the stem: hydralazine or nifedipine. None of them: labetalol."),
  ],
  traps=[
    ("“HELLP” for platelets 100,000, AST 280, glucose 42 mg/dL, INR 2.4 and raised ammonia at 35 weeks", "Hypoglycaemia, a high INR and ammonia are failed synthesis: acute fatty liver (69% right)."),
    ("“Hydralazine” or “methyldopa” as the IV drug to avoid in an asthmatic with severe pre-eclampsia", "Labetalol is the one with β2 blockade."),
    ("Treating ‘no asthma’ as proof that carboprost is the only answer", "It makes carboprost allowed; ergometrine is equally valid in a normotensive woman (OBS-32)."),
    ("“Pulmonary thromboembolism” when the stem adds thrombocytopenia and a long PT to collapse in labour", "The coagulopathy is the planted cue for amniotic fluid embolism (75% right)."),
  ],
  decode=[
    ("Severe pre-eclampsia, BP 182/116, asthma on inhaled steroids — which IV antihypertensive to avoid? [DocT GT]", "Labetalol."),
    ("35 weeks, nausea, jaundice, platelets 100,000, AST 280, glucose 42, INR 2.4, high ammonia — diagnosis? [DocT]", "Acute fatty liver of pregnancy (69%)."),
    ("Atony after oxytocin; BP 90/60; stem silent on asthma — next drug? [DocT]", "Carboprost (62%)."),
    ("Trauma at 30 weeks, tender uterus, FAST negative — cause of bleeding? [DocT]", "Abruption (72%)."),
  ],
  punch="In an obstetric stem, look for the phrase that was not needed to tell the story: ‘no asthma’, ‘after magnesium’, ‘ultrasound negative’, ‘despite pre-oxygenation’, a glucose or a fibrinogen. That phrase is the key.",
)

L['OBS-43'] = dict(
  sub="Obstetrics → Revision → True or false",
  step=6,
  intro="Step 6 ends by checking ten statements against OBS02A and this deck. Each false statement is a real distractor from the cards before it. Eight of the ten are false, and for each the correction matters more than the verdict.",
  parts=[
    ('a', "**False: it falls by 20%.** The uterus lifts the diaphragm, so functional residual capacity falls; with higher oxygen consumption this is why she desaturates quickly (OBS-42f)."),
    ('b', "**False: about 30; 18–22.** Progesterone drives ventilation up, so PaCO₂ is about 30 mmHg and the kidney lowers bicarbonate to 18–22 mmol/L to compensate. A PaCO₂ of 40 in a pregnant woman is already hypoventilation."),
    ('c', "**True.** The obstetric qSOFA uses a respiratory rate of 25 or more (not 22), a systolic pressure under 90 mmHg (not 100 or less), and altered mentation, because the normal pregnant woman breathes faster and has a lower pressure."),
    ('d', "**False: anticonvulsant only.** Magnesium prevents and treats eclamptic seizures and lowers blood pressure little; severe hypertension needs labetalol, hydralazine or nifedipine (OBS-42c)."),
    ('e', "**False: patellar reflex.** Loss of the knee jerk comes first (about 3.5–5 mmol/L), then respiratory depression, then conduction block and arrest at higher levels, which is why reflexes, respiratory rate and urine output are monitored. Treatment is calcium (OBS-39d)."),
    ('f', "**False: inflammatory, anaphylactoid.** It resembles anaphylaxis but is not IgE-mediated (OBS-36)."),
    ('g', "**False: carboprost is avoided in asthma; the ergot is avoided in hypertension.** Each drug contracts a second smooth muscle besides the uterus: carboprost (PGF2α) the bronchi, methylergonovine the arteries. The statement swaps the two (OBS-32)."),
    ('h', "**True.** Fresh retroplacental clot looks like placenta, so ultrasound misses at least half of abruptions; the diagnosis is clinical (OBS-30)."),
    ('i', "**False: by 5 minutes.** Preparation starts when the arrest is recognised, and if circulation has not returned by about 4 minutes the uterus is emptied so that delivery is complete by 5. The operation is for the mother: it removes aortocaval compression and returns uterine blood to her circulation, and both maternal and neonatal survival fall with each minute of delay, so waiting 15 minutes forfeits the benefit (OBS-39e)."),
    ('j', "**False: under 45%.** The diagnosis needs left ventricular systolic dysfunction with an ejection fraction under 45%, in the last month of pregnancy or the months after delivery, with no other cause. An ejection fraction under 30% at presentation predicts poor recovery and makes mWHO class IV for a future pregnancy, but it is a marker of severity and not the diagnostic cut-off (OBS-38b)."),
  ],
  table=dict(title="All ten statements", head=["", "Statement", "Verdict", "Why"], rows=[
    ["a", "FRC rises in pregnancy", "**F**", "falls by 20%"],
    ["b", "Normal PaCO₂ 40, bicarbonate 24", "**F**", "about 30; 18–22"],
    ["c", "Obstetric qSOFA uses a respiratory rate of 25", "**T**", "and systolic under 90"],
    ["d", "Magnesium is the antihypertensive of choice", "**F**", "anticonvulsant only"],
    ["e", "First sign of magnesium toxicity is respiratory arrest", "**F**", "loss of the patellar reflex"],
    ["f", "Amniotic fluid embolism is IgE-mediated", "**F**", "inflammatory, anaphylactoid"],
    ["g", "Carboprost is avoided in hypertension", "**F**", "carboprost: asthma; ergot: hypertension"],
    ["h", "Ultrasound can be normal in abruption", "**T**", ""],
    ["i", "Perimortem caesarean after 15 minutes of CPR", "**F**", "**by 5 minutes** (OBS-39e)"],
    ["j", "Peripartum cardiomyopathy needs an EF under 30%", "**F**", "**under 45%** (OBS-38b)"],
  ]),
  mimic=[
    ("Obstetric qSOFA vs standard qSOFA", "Obstetric: respiratory rate ≥25, systolic under 90. Standard: respiratory rate ≥22, systolic ≤100. Altered mentation is in both."),
  ],
  traps=[
    ("“Respiratory arrest is the first sign of magnesium toxicity”", "The reflex goes first; if it is present, the level is not yet dangerous."),
    ("“Carboprost: hypertension”", "The pairs are swapped: carboprost with asthma, ergot with hypertension."),
    ("“PaCO₂ 40 is normal”", "Normal for a non-pregnant adult; in pregnancy it means she is tiring."),
    ("“Perimortem caesarean is a last resort after prolonged CPR”", "It is part of the resuscitation, not what follows it: by 5 minutes, because emptying the uterus is what restores venous return."),
    ("“An ejection fraction under 30% is needed to diagnose peripartum cardiomyopathy”", "Under 45% makes the diagnosis; under 30% grades its severity."),
  ],
  decode=[
    ("Pregnant asthmatic in an attack with PaCO₂ 40 mmHg — interpretation? [pattern]", "Relative hypercapnia; her normal is about 30, so this is impending respiratory failure."),
    ("On magnesium: reflexes absent, respiratory rate 10 — action? [pattern]", "Stop magnesium, give calcium."),
  ],
  punch="Two statements are true: the obstetric qSOFA uses a respiratory rate of 25, and ultrasound can be normal in abruption. The other eight are each a distractor from an earlier card.",
)

FLAGS = {
  'OBS-30': "Card text is sound. A linked DocT key is disputed: stable praevia with a repeat bleed at 36 weeks is keyed ‘hospitalisation and pelvic rest’ (21% right), but ACOG/SMFM (Committee Opinion 831) plan caesarean for uncomplicated praevia at 36+0 to 37+6 weeks and RCOG GTG 27a advises 34+0 to 36+6 weeks after bleeding. Explanation gives both. (The 34+0 to 35+6 window quoted in the question note is ACOG’s window for accreta, not for praevia with recurrent bleeds.)",
  'OBS-31': "Definition (>500 mL) is the traditional WHO one; ACOG 2017 uses ≥1,000 mL or signs of hypovolaemia, RCOG minor 500–1,000 and major >1,000 mL, and the WHO/FIGO/ICM 2025 guideline adds action at 300 mL with any abnormal vital sign. Watch line ends secondary PPH at 6 weeks; RCOG and ACOG say 12 weeks. Uterine inversion management (asked three times) is not on the card beyond ‘replace the uterus’; added.",
  'OBS-32': "Card does not give carboprost’s repeat interval or maximum (250 µg every 15–90 min, 8 doses = 2 mg), asked twice. Misoprostol 1,000 µg rectally is the top of ACOG’s 600–1,000 µg range; WHO/FIGO use 800 µg sublingually and DocT stems write 800 µg. Three linked keys are debatable (carboprost over ergometrine with BP 90/60; misoprostol over methylergonovine in a normotensive asthmatic; methylergonovine as the asthma drug when carboprost is not offered).",
  'OBS-33': "Step 1 lists uterine massage as part of active management: WHO (2012 onwards) no longer recommends sustained massage for prevention when oxytocin has been given, and delays cord clamping; the DocT question still accepts massage as a component. Tranexamic acid is only in the watch line and belongs with step 3–4. One stem (uterine artery ligation failed for atony) is keyed two ways in two DocT tests; compression sutures before internal iliac ligation agrees with the card.",
  'OBS-35': "a: 3.3 per 100,000 is within the published range (about 2–6 per 100,000). b: ‘mortality 15–85%’ spans old registries (60–85%) and modern population studies (about 20%); ‘half die in the first hour’ comes from the old registry and refers to those who die. e: could name the SMFM/AFE Foundation 2016 criteria.",
  'OBS-36': "Card agrees with the current view. The linked DocT key calls the pulmonary oedema ‘cardiogenic’ while DocT’s own explanation says non-cardiogenic; it is mixed.",
  'OBS-37': "c: ‘VA-ECMO has reduced mortality’ rests on case series and registry data, not trials; it is a recommended rescue for refractory collapse. Pyelonephritis management (asked by Marrow) is not on the card; the Marrow note gives 7–10 days of antibiotics, ACOG (Clinical Consensus 4, 2023) gives 14 days in total; the explanation uses 14.",
  'OBS-38': "c: mortality 20–50% is from older series; contemporary figures are about 5–10% (ESC registry 6% at 6 months), and incidence ranges from about 1 in 1,000–4,000 (United States) to 1 in 100–300 (Nigeria, Haiti). a: the ESC definition has no fixed month limits. d: sacubitril–valsartan, spironolactone, ivabradine and SGLT2 inhibitors are also avoided in pregnancy. Watch line: bromocriptine is a weak (‘may be considered’) recommendation in ESC 2018 and is described as an evidence gap in ESC 2025; it is an option, not standard treatment.",
  'OBS-39': "Card agrees with AHA 2020/2025. e: the current term is resuscitative hysterotomy, applies when the fundus is at or above the umbilicus (about 20 weeks), and the decision is taken at about 4 minutes to deliver by 5. d could give the calcium dose (chloride 10% 10 mL or gluconate 10% 30 mL).",
  'OBS-42': "Watch line: ‘cystitis in pregnancy with penicillin allergy is treated with cephalexin’ follows a GT key; a cephalosporin is acceptable only if the penicillin allergy was not severe, and nitrofurantoin or fosfomycin are the usual alternatives. Not expanded in the explanation.",
  'OBS-43': "No error in the card. c: the obstetric qSOFA (SOMANZ 2017) is respiratory rate ≥25, systolic pressure under 90 mmHg and altered mentation. All ten statements a–j are now explained as parts.",
}
