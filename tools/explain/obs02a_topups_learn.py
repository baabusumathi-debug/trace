# OBS02A top-up cards — Explain v3 ("Learn" depth), same fields and voice as obs02a_learn.py.
# Fields: sub, step (index into obs02a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Parts follow the lines of the top-up's answer in order (a, b, c…); each starts with the line restated in bold. Disagreements with a card go in FLAGS, not in the text.
# Source questions: DocT QBank ‘Hypertensive Disorders in Pregnancy’ Q5 (CHIPS, 68% right) and Q15 (HYPITAT, 49% right), DocT GT7 Q145 (CHIPS, 65%), Marrow QB52-Q04 (GDM after caesarean).
# Checked online 12 Nov 2026: HYPITAT (Koopmans, Lancet 2009): 756 women, 38 Dutch centres, 36–41 weeks, poor maternal outcome 31% vs 44% (29% lower relative risk; DocT quotes RR 0.71, 95% CI 0.59–0.86);
# ACOG PB 222: delivery at 37+0 weeks for gestational hypertension or pre-eclampsia without severe features; ADA Standards of Care: 75 g OGTT at 4–12 weeks postpartum, then lifelong screening
# at least every 3 years. CHIPS figures (Magee, NEJM 2015: 987 women analysed, 14+0 to 33+6 weeks, primary outcome 31.4% vs 30.7%, severe hypertension 40.6% vs 27.5%) agree with the bank’s
# own lines and with memory; PubMed could not be opened today.
# Second check, 12 Nov 2026 (reviewer), confirmed online: CHIPS primary outcome 31.4% (less-tight) vs 30.7% (tight), adjusted OR 1.02; severe hypertension 40.6% vs 27.5%; serious maternal
# complications 3.7% vs 2.0% (not significant). HYPITAT composite = maternal death, eclampsia, HELLP, pulmonary oedema, thromboembolism, abruption, progression to severe hypertension or
# proteinuria, major postpartum haemorrhage; no eclampsia or deaths occurred. HYPITAT-II (Broekhuijsen, Lancet 2015): 703 women, 34–37 weeks, adverse maternal outcome 1.1% vs 3.1% (RR 0.36,
# not significant), neonatal respiratory distress syndrome 5.7% vs 1.7% (RR 3.3). CHAP (Tita, NEJM 2022): 2,408 women, target <140/90 vs treatment only at ≥160/105, primary outcome
# 30.2% vs 37.0% (RR 0.82), small for gestational age 11.2% vs 10.4%. From memory only (kept out of the text): HYPITAT caesarean rates (14% vs 19%), the roughly tenfold later risk of type 2 diabetes after GDM.
T = {}

T['T_7bbda3e4'] = dict(
  sub="Obstetrics → Hypertensive disorders → CHIPS and HYPITAT",
  step=3,
  intro="Step 3 is about lowering the pressure and timing the delivery, and these two trials set the rules for the mild end of the disease, where the cards OBS-18 to OBS-21 deal with the severe end. CHIPS asked how tightly to control non-severe hypertension; HYPITAT asked whether to induce or wait near term. Each question gives the trial and asks for its finding, and the HYPITAT one is missed by half the cohort.",
  parts=[
    ('a', "**CHIPS (2015): non-severe hypertension, tight (DBP 85) vs less-tight (DBP 100).** About 1,000 women at 14 to 33 weeks with chronic or gestational hypertension and no proteinuria were randomised to a diastolic target of 85 or 100 mmHg. The fear being tested was that tighter control would reduce placental flow and harm the baby."),
    ('b', "**No difference in pregnancy loss or neonatal high-level care; tight control cut severe hypertension (~28% vs 41%).** The primary outcome, pregnancy loss or high-level neonatal care for more than 48 hours, occurred in about 31% of both groups, and babies were not smaller with tight control. The mothers in the less-tight group reached 160/110 more often (40.6% vs 27.5%). Serious maternal complications were few and did not differ significantly (3.7% vs 2.0%), and neither did perinatal death or preterm birth. So tight control protects the mother from severe hypertension, the range that carries the stroke risk, at no cost to the fetus."),
    ('c', "**HYPITAT (2009): gestational hypertension/mild pre-eclampsia at 36–41 weeks, induction vs expectant.** 756 women with a singleton pregnancy in the Netherlands were randomised to induction of labour or to monitoring until labour began or the disease worsened."),
    ('d', "**Induction cut poor maternal outcome 44% → 31% without more caesareans.** The composite counted progression to severe hypertension or proteinuria, HELLP, eclampsia, pulmonary oedema, thromboembolism, abruption and major postpartum haemorrhage (relative risk 0.71); nearly all of the difference was progression to severe disease, and no woman died or had eclampsia. Caesarean delivery was not more frequent with induction and neonatal outcomes were the same. Near term the placenta is the source of the disease and the baby is mature, so waiting only adds maternal risk."),
    ('e', "**Hence: treat to DBP 85; deliver mild disease at 37 weeks.** A diastolic target of 85 is what ISSHP now recommends, since CHIPS showed it is safe for the baby. The 37-week line comes from HYPITAT together with HYPITAT-II, in which immediate delivery at 34–37 weeks tripled neonatal respiratory distress syndrome (5.7% vs 1.7%) without a significant maternal gain. ACOG accordingly delivers gestational hypertension and pre-eclampsia without severe features at 37+0 weeks. With severe features the line is 34 weeks (OBS-20)."),
  ],
  table=dict(title="The two trials side by side", head=["", "CHIPS (NEJM 2015)", "HYPITAT (Lancet 2009)"], rows=[["Who", "non-severe chronic or gestational hypertension, 14–33 weeks", "gestational hypertension or mild pre-eclampsia, 36–41 weeks"], ["Compared", "diastolic target **85** vs 100", "**induction** vs expectant monitoring"], ["Mother", "severe hypertension **27.5% vs 40.6%**", "poor outcome **31% vs 44%**"], ["Baby", "no difference", "no difference"], ["Caesarean", "no difference", "not increased"]]),
  mimic=[
    ("CHIPS vs CHAP", "CHIPS: tight vs less-tight diastolic targets; fewer episodes of severe hypertension, no difference in the perinatal primary outcome. CHAP (NEJM 2022): treating mild chronic hypertension to below 140/90 vs treating only at 160/105; fewer adverse pregnancy outcomes (a composite of severe pre-eclampsia, indicated preterm birth before 35 weeks, abruption and fetal or neonatal death: 30% vs 37%), without more small babies. It is why ACOG now treats chronic hypertension in pregnancy from 140/90."),
    ("HYPITAT vs HYPITAT-II", "HYPITAT: 36–41 weeks, induce. HYPITAT-II: 34–37 weeks, wait until 37 weeks unless the disease worsens."),
  ],
  traps=[
    ("“No difference in maternal outcomes” for HYPITAT", "Induction reduced maternal morbidity (49% right). The outcomes that did not differ were neonatal outcome and the caesarean rate."),
    ("“Expectant management reduced the caesarean rate”", "It did not; induction did not increase caesareans."),
    ("“Tight control reduced stillbirths” for CHIPS", "Perinatal outcomes were the same in both groups; the proven benefit is less progression to severe hypertension (68% and 65% right)."),
    ("“Less-tight control reduced preterm births or ICU admissions”", "No such difference was found."),
  ],
  decode=[
    ("CHIPS compared tight vs less-tight control in non-severe hypertension — which finding is TRUE? [DocT QBank, DocT GT]", "Tight control prevented progression to severe hypertension."),
    ("HYPITAT: induction vs expectant management after 36 weeks — main finding? [DocT QBank]", "Induction reduced maternal morbidity."),
    ("[pattern] Gestational hypertension at 37 weeks, BP 146/94, no severe features — plan?", "Induce labour now."),
  ],
  punch="CHIPS: a diastolic target of 85 does not change the baby’s outcome but cuts severe maternal hypertension from 41% to 28%. HYPITAT: inducing mild disease from 37 weeks cuts poor maternal outcome from 44% to 31% without more caesareans.",
)

T['T_f2d95d0c'] = dict(
  sub="Obstetrics → Diabetes in pregnancy → Gestational diabetes after delivery",
  step=3,
  intro="This top-up sits with Step 3 because it follows the same logic as pre-eclampsia: the placenta causes the disease and delivering it is the cure. Gestational diabetes is insulin resistance produced by placental hormones, so the insulin requirement falls within hours of delivery. The Marrow question gives a normal fasting glucose the day after caesarean section and asks for the next step.",
  parts=[
    ('a', "**Stop insulin: placental anti-insulin hormones are gone.** Human placental lactogen, placental growth hormone, progesterone and the raised cortisol of pregnancy make the mother insulin-resistant, and they fall rapidly once the placenta is delivered. Insulin sensitivity returns to normal within a day, so continuing the pregnancy dose causes hypoglycaemia, the more so in a woman who is fasting after surgery. Insulin (and metformin, if used for the pregnancy) is stopped at delivery."),
    ('b', "**Check glucose; 75 g OGTT at 6–12 weeks postpartum (lifelong type 2 risk).** Glucose is checked for a day or two after delivery to find the few women whose hyperglycaemia persists, which means diabetes that was present before pregnancy. A 75 g oral glucose tolerance test, read by non-pregnant criteria, is then done once the puerperium is over; the ADA now words the window as 4–12 weeks. HbA1c is less reliable so soon after delivery. Gestational diabetes marks limited β-cell reserve, so the later risk of type 2 diabetes is several-fold raised, and screening is repeated at least every three years for life."),
  ],
  mimic=[
    ("Gestational diabetes vs pre-existing type 1 or type 2 diabetes after delivery", "Gestational: stop insulin. Type 1: never stop; reduce to about the pre-pregnancy dose or less, because requirements fall sharply. Type 2: return to the pre-pregnancy regimen."),
    ("Gestational diabetes vs overt diabetes first found in pregnancy", "Overt diabetes: diagnosed in the first trimester or with clearly diabetic values; glucose stays high after delivery and treatment continues."),
  ],
  traps=[
    ("“Continue the same insulin dose”", "The resistance has gone with the placenta; the pregnancy dose now causes hypoglycaemia."),
    ("“Halve the insulin dose” or “switch to oral agents”", "That is the plan for pre-existing diabetes. With gestational diabetes and a normal fasting glucose, insulin is stopped."),
    ("“No follow-up is needed once glucose is normal”", "A postpartum OGTT and lifelong screening are required."),
    ("“OGTT immediately after delivery”", "Glucose handling is still changing; the test is done at 4–12 weeks."),
  ],
  decode=[
    ("GDM on insulin, fasting glucose 85 mg/dL one day after caesarean section — next step? [Marrow]", "Stop insulin."),
    ("[pattern] When and how is a woman with GDM retested after delivery?", "75 g OGTT at 4–12 weeks postpartum, then at least every three years."),
    ("[pattern] Type 1 diabetic after delivery — insulin?", "Reduce the dose sharply; do not stop."),
  ],
  punch="Gestational diabetes is caused by placental hormones, so insulin is stopped at delivery; glucose is checked for a day or two, a 75 g OGTT is done at 4–12 weeks, and screening continues for life.",
)

FLAGS = {}
FLAGS['T_7bbda3e4'] = "Card is accurate (CHIPS: severe hypertension 27.5% vs 40.6%, primary outcome about 31% in both arms; HYPITAT: 31% vs 44%). CHIPS was published in NEJM 2015; the DocT explanation cites the Lancet. ‘Deliver at 37 weeks’ also rests on HYPITAT-II (confirmed: more neonatal respiratory distress with delivery at 34–37 weeks) and ACOG PB 222. ‘Treat to DBP 85’ is the ISSHP target; ACOG, after CHAP, states its threshold as 140/90."
FLAGS['T_f2d95d0c'] = "Card says OGTT at 6–12 weeks postpartum; current ADA and ACOG wording is 4–12 weeks (NICE uses a fasting glucose at 6–13 weeks). Either is acceptable in an exam; explanation restates the card and gives the current window."
