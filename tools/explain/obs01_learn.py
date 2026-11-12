# OBS01 — Explain v3 ("Learn" depth): obstetrics in critical care, part 1 — burden and causes, the physiology of pregnancy (circulation, lungs, blood gas,
# aortocaval compression, blood, kidney, gut), recognition (MEOWS, obstetrically modified qSOFA), the pregnant airway and failed intubation, ventilation, circulation,
# the decision to deliver, and radiation. No mnemonics or hooks.
# Driven by the real questions in qpack/OBS01.md (20 questions: OBS-03 asked 7 times, OBS-12 four, OBS-06 three, OBS-07, OBS-08 and OBS-11 twice each) and the verified
# corrections in trace/test/data/qbank.json (OBS-03, 07, 11, 12, 13). Fields as TOX01, plus SPINE, PRIMER and step. Cards with no linked question get short explanations with [pattern] decode items.
# Checked online on 12 Nov 2026:
#  - MEOWS chart (Singh 2012 / CEMACH 2007, as reproduced in Friedman 2018, PMC5910060): RR red <10 or >30, yellow 21–30; SpO2 red <95; temperature red <35 or >38, yellow 35–36;
#    systolic BP red <90 or >160, yellow 90–100 or 150–160; diastolic red >100, yellow 90–100; heart rate red <40 or >120, yellow 40–50 or 100–120; neuro yellow ‘voice’, red ‘pain/unresponsive’;
#    trigger = one red or two yellow. The card’s ‘150–180’ and ‘over 180’ for systolic BP differ from this (FLAG).
#  - Normal blood gas in pregnancy (Deranged Physiology chapter citing Hegewald & Crapo 2011, Oh’s Manual): pH 7.40–7.47, PaCO2 about 30 mmHg, PaO2 up to about 105 mmHg, bicarbonate about 20 mmol/L.
#    The page gives no base-excess figure; OBS-05 therefore says only ‘mildly negative, a base deficit of a few mmol/L’ (reviewer: the writer’s −2 to −4 mmol/L could not be sourced and was softened; FLAG).
#  - Asthma top-up source questions read in map/doct_gt_distinct_all.jsonl (GrandT1 Q47, AIM1 Q73, CGT1 Q44, GT3 Q149 / GT4 Q29, GT3 Q47, GT3 Q73, CGT6 Q88–89).
# From standard references, not re-checked online (stated only where I am sure): Clark 1989 haemodynamics at term (cardiac output 6.2 vs 4.3 L/min, SVR 1210 vs 1530 dyn·s/cm5, CVP and wedge
# unchanged); cardiac output in labour and immediately post partum (+60–80%); OAA/DAS 2015 obstetric difficult-airway algorithms (2 intubation attempts + 1 by an experienced colleague, 2 SGA attempts,
# mask pressure ≤20 cmH2O); Kinsella 2015 failed obstetric intubation about 1 in 390; AHA 2015/2020 maternal arrest (manual left uterine displacement, access above the diaphragm, usual drugs and
# shock energies, perimortem delivery from 4–5 minutes when the uterus is at or above the umbilicus); SOMANZ 2017 omqSOFA; ACOG Committee Opinion 723 (2017) fetal dose table and the 50 mGy threshold;
# antenatal steroids (betamethasone 12 mg IM × 2, 24 h apart; dexamethasone 6 mg IM 12-hourly × 4); 2018 international consensus on phenylephrine for spinal hypotension.

SPINE = [
  ("Who gets sick, and why", "Pregnant and postpartum women are a small share of ICU admissions, the causes are either diseases of pregnancy itself or ordinary diseases made worse by it, and most of the deaths are preventable."),
  ("The pregnant body’s new normal", "By term cardiac output and blood volume are up by nearly half, resistance and diastolic pressure are down, she hyperventilates to a PaCO₂ of 30 with a bicarbonate of 20, and creatinine and haemoglobin are low, so ‘normal’ adult values can mean disease."),
  ("Recognising deterioration with shifted thresholds", "Because her baseline has moved, the obstetric early warning chart and the obstetric qSOFA use their own cut-offs: systolic 90 or less, respiratory rate 25 or more, anything other than alert."),
  ("Small reserve, difficult airway", "A swollen, friable airway, a small oxygen store, a high oxygen use and a full stomach make intubation harder and desaturation faster, so the plan limits attempts and puts oxygenation ahead of the tube."),
  ("Supporting the mother, protecting the fetus", "Organ support is the same as in any adult with a few fetal adjustments: uterus off the vena cava, saturation 95% or more, no permissive hypercapnia, lines above the diaphragm, steroids for the fetal lung, and no necessary scan withheld."),
]

PRIMER = "The fetus has no oxygen supply of its own: what reaches it is maternal arterial oxygen content multiplied by uterine blood flow, and the uterine vessels are already fully dilated and cannot autoregulate, so any fall in maternal blood pressure, cardiac output or saturation is passed straight on. Fetal carbon dioxide leaves by diffusing down a gradient into maternal blood, which is why the mother normally runs a low PaCO₂. From about 20 weeks the uterus is large enough to press on the inferior vena cava and aorta when she lies flat. Treating the mother well is the treatment of the fetus; almost nothing in this deck asks you to trade one against the other."

L = {}

L['OBS-01'] = dict(
  sub="Obstetrics → Burden → Obstetric patients in the ICU",
  step=1,
  intro="Step 1 sets the scale before any physiology. Obstetric patients are few in any ICU, young and usually previously well, which is exactly why a death is so often judged avoidable. No linked question tests these figures, so this is the short version.",
  parts=[
    ('a', "**1–4.5% of ICU admissions (0.9% in the UK and US).** The share is higher where antenatal care and high-dependency obstetric beds are scarce, because women arrive later and sicker; in high-income countries under 1% of ICU admissions are obstetric."),
    ('b', "**Mortality 5–20%.** The range reflects the setting more than the disease: the same eclampsia or haemorrhage has a low mortality when treated early and a high one after a long transfer."),
    ('c', "**70% of maternal deaths are preventable.** The usual failures are late recognition (vital signs read against non-pregnant norms, OBS-09 and OBS-10) and late escalation, not lack of a treatment."),
    ('d', "**Physiological changes of pregnancy; pregnancy-specific diseases; the fetus; clinicians’ unfamiliarity.** The physiology changes what counts as normal (OBS-03 to OBS-07), the diseases are ones an adult ICU rarely sees (OBS-02), the fetus is a second patient who depends entirely on maternal oxygen delivery, and most intensivists manage only a handful of such patients a year."),
    ('e', "**Hypotension, hypoxia, anaemia.** These are the three terms of oxygen delivery to the uterus: flow, saturation and haemoglobin. The uterine bed cannot autoregulate, so a fall in any one reduces fetal oxygen supply directly; correcting all three is the first job in any sick pregnant woman."),
  ],
  mimic=[
    ("This ‘lethal triad’ vs the trauma lethal triad", "Obstetric (this card): hypotension, hypoxia, anaemia, the determinants of oxygen delivery. Trauma: hypothermia, acidosis, coagulopathy. A stem set in pregnancy wants the first."),
  ],
  traps=[
    ("“Haemorrhage is the commonest reason for obstetric ICU admission”", "On this card’s chart hypertensive disease (pre-eclampsia and eclampsia) is far ahead at 75%, with medical disease 14% and haemorrhage 11%. The proportions vary by series; in many high-income series haemorrhage and hypertension are closer together."),
  ],
  decode=[
    ("[pattern] Commonest indication for ICU admission in pregnancy", "Hypertensive disorders (pre-eclampsia, eclampsia), then haemorrhage and medical disease."),
    ("[pattern] Which is NOT part of the lethal triad in the critically ill parturient?", "Hypotension, hypoxia and anaemia are; hypothermia, acidosis and coagulopathy belong to trauma."),
  ],
  punch="Obstetric patients are 1–4.5% of ICU admissions with a mortality of 5–20%, most of the deaths are preventable, and the three things to correct first are hypotension, hypoxia and anaemia because together they set oxygen delivery to the uterus.",
)

L['OBS-02'] = dict(
  sub="Obstetrics → Burden → Causes of critical illness in pregnancy",
  step=1,
  intro="Step 1 continues with the causes, sorted the way a stem should be sorted: is this a disease that exists only because she is pregnant, or an ordinary disease that pregnancy has made more likely or more severe? The answer decides whether delivery is part of the treatment.",
  parts=[
    ('a', "**Obstetric: severe pre-eclampsia, eclampsia, HELLP; obstetric haemorrhage (abruption, rupture, adherent placenta, inversion); amniotic fluid embolism; peripartum cardiomyopathy; acute fatty liver of pregnancy; sepsis (chorioamnionitis, septic abortion, endometritis); magnesium toxicity, tocolytic pulmonary oedema, ovarian hyperstimulation.** The placenta drives the first group (pre-eclampsia, HELLP, acute fatty liver), so delivery is the definitive treatment. Haemorrhage and amniotic fluid embolism cluster around delivery. The last line is iatrogenic: magnesium given for eclampsia, β-agonist tocolytics causing pulmonary oedema, and fertility treatment causing ovarian hyperstimulation."),
    ('b', "**Non-obstetric or worsened by pregnancy: ARDS, aspiration, pulmonary embolism; urosepsis, AKI; valvular and congenital heart disease, pulmonary hypertension; hepatitis E, varicella pneumonia, falciparum malaria, H1N1; DIC, HUS/TTP, DVT; diabetic ketoacidosis; intracranial bleed, cerebral venous sinus thrombosis, Sheehan’s.** Each follows from a change in step 2. A lax sphincter gives aspiration; a hypercoagulable state gives embolism and venous sinus thrombosis; dilated ureters give pyelonephritis; a 40–50% rise in cardiac output unmasks stenotic valves and pulmonary hypertension; altered cell-mediated immunity makes hepatitis E, varicella, influenza and falciparum malaria more severe than in other adults. Ketoacidosis develops faster and at lower glucose levels because placental hormones cause insulin resistance, the fetus and placenta take up glucose continuously so fasting ketosis starts early, and the bicarbonate buffer is already low (OBS-05)."),
  ],
  mimic=[
    ("HELLP vs acute fatty liver of pregnancy vs TTP/HUS", "HELLP: hypertension, haemolysis, platelets down, transaminases up, glucose normal. Acute fatty liver: liver failure picture with hypoglycaemia, raised ammonia, prolonged PT, low fibrinogen. TTP/HUS: haemolysis and low platelets with normal clotting, and it does not remit after delivery."),
    ("Amniotic fluid embolism vs pulmonary embolism", "Both give sudden collapse and hypoxia around delivery. Amniotic fluid embolism adds early DIC and bleeding, which may be the presenting feature; pulmonary embolism does not cause a consumptive coagulopathy."),
  ],
  traps=[
    ("“Viral hepatitis behaves in pregnancy as in other adults”", "Hepatitis E is the exception: it causes fulminant hepatic failure with a high maternal mortality, mainly in the third trimester."),
    ("“Peripartum cardiomyopathy is a pre-existing heart disease”", "It is listed with the obstetric causes: new left ventricular systolic failure towards the end of pregnancy or in the months after delivery with no other cause. Valvular, congenital and pulmonary hypertensive disease are the pre-existing group."),
  ],
  decode=[
    ("[pattern] Which is a pregnancy-specific cause of ICU admission?", "Pre-eclampsia/HELLP, acute fatty liver, amniotic fluid embolism, peripartum cardiomyopathy; not hepatitis E, malaria or embolism, which pregnancy only worsens."),
    ("[pattern] Marfan syndrome planning pregnancy — which finding makes it high risk?", "An aortic root over 4 cm (the card’s watch line): risk of dissection."),
  ],
  punch="Sort the sick pregnant woman into diseases of pregnancy (pre-eclampsia and HELLP, haemorrhage, amniotic fluid embolism, peripartum cardiomyopathy, fatty liver, genital-tract sepsis), where delivery is often the cure, and ordinary diseases that pregnancy makes commoner or worse.",
)

L['OBS-03'] = dict(
  sub="Obstetrics → Physiology → Cardiovascular changes",
  step=2,
  intro="Step 2 begins with the circulation, the most examined card in the deck (seven Grand Test questions). The whole table follows from two events: resistance falls early, and volume expands to fill the larger circuit. Flow rises, pressure does not. The questions test the direction of each number, the reason for the diastolic dip, the figures on a pulmonary artery catheter, the further rise in labour, and what is normal on auscultation.",
  parts=[
    ('a', "**Cardiac output up 40–50%; stroke volume up 30%; heart rate up 15–25%.** Output starts rising in the first trimester and is near its plateau by about 28–32 weeks. Stroke volume does the early work as volume expands and afterload falls; heart rate goes on climbing to term (about 10–20 beats/min above baseline), as the watch line says. These are antenatal figures at rest. In labour each contraction squeezes 300–500 mL from the uterus into the circulation and pain adds sympathetic drive, so output rises further, and immediately after delivery it peaks at 60–80% above the pre-pregnancy value as the emptied uterus returns its blood and the vena cava is released. That is when a woman with mitral stenosis or pulmonary hypertension goes into pulmonary oedema."),
    ('b', "**Intravascular volume up 45%.** Oestrogen and the fall in resistance activate the renin–angiotensin–aldosterone system and retain sodium and water. Plasma expands more than red cells (OBS-07). The extra volume fills a dilated circuit, which is why filling pressures do not rise, and it is a reserve against blood loss at delivery: she can lose well over a litre before the pulse and pressure change."),
    ('c', "**Systemic vascular resistance down 20%; systolic BP minimal change; diastolic BP down 20% at mid-pregnancy, back to baseline at term.** Progesterone relaxes vascular smooth muscle and blunts the response to angiotensin II, relaxin and endothelial nitric oxide add to it, and the placenta is a low-resistance circuit in parallel. Diastolic pressure is the pressure most dependent on resistance, so it falls most, with its lowest point in the second trimester; the pulse pressure widens. A pressure of 120/80 at 24 weeks is therefore relatively high. On a pulmonary artery catheter at term, expect an output of about 6–6.5 L/min and an SVR of roughly 900–1200 dyn·s/cm⁵ (Clark 1989: 6.2 L/min and 1210, against 4.3 and 1530 post partum)."),
    ('d', "**CVP unchanged.** The larger volume sits in a more compliant venous bed and a dilated heart, so central venous and wedge pressures stay in the non-pregnant range, and pulmonary vascular resistance falls along with systemic. A CVP of 15 mmHg or a raised pulmonary resistance is disease, not pregnancy."),
    ('e', "**Oxygen consumption up 30–40%.** The fetus, placenta, uterus and the extra cardiac and respiratory work all add to it; published figures at term range from about 20% to 40%, and it rises again in labour. Together with the fall in FRC (OBS-04) this explains rapid desaturation at intubation (OBS-08)."),
  ],
  table=dict(title="What a normal term circulation looks like", head=["Measure", "Change", "Use in a stem"], rows=[["Cardiac output", "**up 40–50%** (about 6–6.5 L/min); **60–80%** in labour and just after delivery", "an output of 4 L/min at 34 weeks is low"], ["Stroke volume / heart rate", "**up 30% / up 15–25%**", "resting pulse 85–95 is normal"], ["SVR", "**down 20%**", "progesterone, relaxin, nitric oxide, placental bed"], ["Blood pressure", "systolic little change; **diastolic lowest mid-pregnancy**", "the only listed parameter that falls"], ["CVP, wedge", "**unchanged**", "high values are pathological"], ["Heart sounds", "loud split S1, **S3**, soft ejection systolic murmur", "diastolic murmur or fixed split S2 needs an echo"]]),
  mimic=[
    ("Normal pregnancy vs early sepsis on the monitor", "Both have a high output, low resistance, a fast pulse and warm peripheries. Sepsis adds fever, a respiratory rate of 25 or more, systolic 90 or less, raised lactate or altered mentation (OBS-10)."),
    ("Physiological S3 and flow murmur vs heart disease", "Normal: S3, loud split S1, a soft (grade 1–2) ejection systolic murmur, mild ankle oedema. Disease: any diastolic murmur, a fixed split S2, a loud systolic murmur, a fourth sound, or symptoms at rest."),
  ],
  traps=[
    ("“Cardiac output in labour rises 30–50%”", "That is the antenatal figure on the card. DocT keys 60–80% for labour (only 41% right); most chose the antenatal range. Standard texts put about +50% in the second stage and the 60–80% peak immediately after delivery, so when a stem says labour or just delivered, pick the highest range offered."),
    ("“Loud S1” as the heart sound of pregnancy", "A loud, widely split S1 does occur, but the keyed answer is the third heart sound, from rapid filling of a volume-loaded ventricle (50% right). The two options that are never normal are a diastolic murmur and a fixed split S2."),
    ("“The diastolic dip is due to increased cardiac output or heart rate”", "A higher output would raise pressure. Pressure falls because resistance falls more than flow rises (92% right)."),
    ("“Blood pressure rises in pregnancy because volume rises 45%”", "The volume fills a dilated circuit; pressure falls in mid-pregnancy and only returns to baseline at term. Of cardiac output, stroke volume, heart rate and blood pressure, only blood pressure decreases (84%)."),
    ("“Only progesterone lowers vascular resistance”", "Progesterone, relaxin and nitric oxide all contribute; ‘all of the above’ is keyed (82%)."),
    ("“A CVP of 15 or a high pulmonary vascular resistance is expected at 34 weeks”", "Filling pressures are unchanged and pulmonary resistance falls."),
  ],
  decode=[
    ("34 weeks, trauma, PA catheter: which set of numbers is the physiological normal? [DocT GT]", "Low SVR with high output: SVR about 850 dyn·s/cm⁵ and cardiac output 6.5 L/min. The other options have a low output, a high MAP with low stroke volume, or a high CVP and pulmonary resistance."),
    ("Why does diastolic BP fall in the second trimester? / Which parameter decreases in (mid-)pregnancy? [DocT GT ×3]", "Decreased systemic vascular resistance; blood pressure is the parameter that falls."),
    ("Expected rise in cardiac output in active labour? [DocT GT]", "60–80% (41% right): autotransfusion with each contraction plus pain."),
    ("Which heart sound is common in pregnancy? [DocT GT]", "Third heart sound (50% right)."),
  ],
  extra=[dict(q="Peripheral resistance in pregnancy is reduced by which mediators?", a="Progesterone (smooth-muscle relaxation, blunted angiotensin II response), relaxin and endothelial nitric oxide, plus the low-resistance placental bed; this is why pressure stays normal despite an activated renin–angiotensin system and 45% more volume.")],
  punch="Resistance falls 20% and volume rises 45%, so output climbs 40–50% (60–80% in labour and just after delivery) while pressure does not rise: diastolic dips in mid-pregnancy, filling pressures are unchanged, and a third heart sound is normal.",
)

L['OBS-04'] = dict(
  sub="Obstetrics → Physiology → Respiratory changes",
  step=2,
  intro="Step 2 moves to the lungs. Two forces act in opposite directions: progesterone makes her breathe more deeply, and the rising uterus pushes the diaphragm up and takes away resting lung volume. The first sets up the blood gas in OBS-05; the second, with the higher oxygen use in OBS-03, sets up the airway problem in OBS-08.",
  parts=[
    ('a', "**Tidal volume 7 → 10 mL/kg (up 40%).** Progesterone stimulates the respiratory centre and increases its sensitivity to carbon dioxide. Minute ventilation rises mainly through deeper breaths; respiratory rate changes little, so a rate above the low 20s at rest is not explained by pregnancy (OBS-09, OBS-10)."),
    ('b', "**Functional residual capacity 30 → 24 mL/kg (down 20%).** The diaphragm is lifted about 4 cm, reducing expiratory reserve and residual volume. FRC is the oxygen store during apnoea, and it falls further when she lies supine, so the store is smallest exactly when she is being intubated."),
    ('c', "**Total lung capacity down 5%; vital capacity unchanged.** The rib cage flares outward and the subcostal angle widens, which offsets the raised diaphragm; the diaphragm still moves fully. Inspiratory capacity rises as expiratory reserve falls, so vital capacity is preserved. Spirometry (FEV₁, FEV₁/FVC, peak flow) is unchanged, so a low value in a pregnant asthmatic is real."),
    ('d', "**Driver: progesterone; tidal volume, rate and CO₂ washout all rise; alveolar ventilation rises about 70%, mostly through tidal volume.** The rise in rate is small (a breath or two a minute); depth does most of the work. Alveolar ventilation rises more than oxygen consumption and carbon dioxide production do, so PaCO₂ falls to about 30 mmHg and PaO₂ rises slightly. Deeper breaths with a smaller FRC also mean each breath replaces more of the alveolar gas: pre-oxygenation and inhalational induction are both faster, and so is desaturation."),
  ],
  mimic=[
    ("Physiological breathlessness of pregnancy vs disease", "Physiological: an awareness of breathing from early pregnancy, at rest or on talking, with a normal rate, saturation and chest. Disease: rate 25 or more, saturation under 95%, sudden onset, orthopnoea, or a PaCO₂ that has risen to 40."),
  ],
  traps=[
    ("“Vital capacity falls in pregnancy”", "Unchanged: the wider rib cage compensates for the raised diaphragm. What falls is FRC (expiratory reserve and residual volume)."),
    ("“Rapid desaturation is due to reduced oxygen consumption” or “to increased FRC”", "The reverse on both counts: oxygen consumption is increased and FRC is decreased (the pairing the card’s watch line cites from a Grand Test)."),
    ("“She breathes faster, not deeper”", "The rise in ventilation is mostly tidal volume; a clearly raised rate is a warning sign."),
  ],
  decode=[
    ("Why does a pregnant woman desaturate rapidly at intubation? [GT, cited on the card]", "Increased oxygen consumption with decreased functional residual capacity."),
    ("[pattern] Which lung volume is unchanged in pregnancy?", "Vital capacity (and FEV₁); FRC, expiratory reserve and residual volume fall."),
  ],
  punch="Progesterone raises tidal volume by 40% and alveolar ventilation by about 70%, while the raised diaphragm cuts FRC by 20% with vital capacity unchanged: more ventilation into a smaller store.",
)

L['OBS-05'] = dict(
  sub="Obstetrics → Physiology → Normal blood gas in pregnancy",
  step=2,
  intro="Step 2’s hyperventilation shows up here as a number set that must be known cold, because every blood gas in a pregnant woman is read against it. The pattern is a chronic respiratory alkalosis that the kidney has fully compensated.",
  parts=[
    ('a', "**pH 7.40–7.47 (non-pregnant 7.35–7.45).** Slightly alkaline: compensation for a respiratory alkalosis is nearly, but not quite, complete."),
    ('b', "**PaCO₂ about 30 mmHg (non-pregnant 35–40).** The low maternal PaCO₂ keeps a gradient for fetal carbon dioxide to diffuse across the placenta. A PaCO₂ of 40 in a breathless pregnant woman is a rise of 10 from her baseline and means she is tiring; in acute asthma it is a reason to prepare for intubation."),
    ('c', "**PaO₂ 100–104 mmHg (non-pregnant 90–100).** The alveolar gas equation: a lower alveolar PCO₂ leaves room for a higher alveolar PO₂. The gain is partly lost at term when she lies supine, because the reduced FRC allows airway closure."),
    ('d', "**Bicarbonate 18–22 mmol/L (non-pregnant 20–28).** The kidney excretes bicarbonate to bring the pH back towards normal. She therefore has less buffer: the same acid load (ketoacids, lactate) lowers pH further and faster than in a non-pregnant woman, and a bicarbonate of 24 is relatively high."),
    ('e', "**Base excess: no change (non-pregnant −2 to +2); a compensated respiratory alkalosis.** The card gives no separate figure for pregnancy. With a bicarbonate of about 20 at a pH of 7.44 the calculated base excess is mildly negative (a base deficit of a few mmol/L), and that small deficit is the expected signature of the renal compensation, not a metabolic acidosis (see FLAGS)."),
  ],
  mimic=[
    ("Normal pregnancy gas vs a mixed disorder", "Normal: pH 7.44, PaCO₂ 30, bicarbonate 20. If PaCO₂ is 30 with a pH of 7.30 and bicarbonate 14, there is an added metabolic acidosis. If PaCO₂ is 40 with a pH of 7.36, there is relative hypoventilation."),
  ],
  traps=[
    ("“PaCO₂ 40 mmHg is a normal gas in a pregnant asthmatic”", "Normal for her is about 30; 40 means ventilatory failure is starting."),
    ("“Bicarbonate 19 with a base deficit of 3 means metabolic acidosis in pregnancy”", "That is the normal renal compensation for chronic hyperventilation; look at pH and the anion gap before calling acidosis."),
    ("“Pregnancy causes an uncompensated respiratory alkalosis”", "It is compensated: pH is only slightly raised because bicarbonate has fallen."),
  ],
  decode=[
    ("[pattern] Third trimester, pH 7.44, PaCO₂ 30, bicarbonate 20 — interpretation?", "Normal for pregnancy: compensated respiratory alkalosis."),
    ("[pattern] Pregnant woman with severe asthma, PaCO₂ 40–42, exhausted — next step?", "Treat as impending respiratory failure; intubate if drowsy or hypoxaemic (DocT GT keys intubation for PaO₂ 58, PaCO₂ 42 with altered sensorium)."),
  ],
  punch="The normal pregnant gas is pH 7.40–7.47, PaCO₂ about 30, bicarbonate 18–22: a compensated respiratory alkalosis, so a PaCO₂ of 40 is failure and the thinner buffer lets acidosis develop fast.",
)

L['OBS-06'] = dict(
  sub="Obstetrics → Physiology → Supine hypotension (aortocaval compression)",
  step=2,
  intro="Step 2 adds the one change that is mechanical and instantly reversible. From mid-pregnancy the uterus lies on the great vessels when she is flat, and three real questions (DocT, Marrow, NEET 2025) all have the same answer: move the uterus to the left before doing anything else.",
  parts=[
    ('a', "**The gravid uterus compresses the inferior vena cava (less venous return) and the aorta (more afterload).** Lying supine at term the vena cava can be almost completely occluded; blood returns through the azygos and paravertebral veins. Most women compensate by vasoconstriction and a faster pulse, which is why only a minority feel faint, but the compensation is lost under anaesthesia, with hypovolaemia or sepsis, and in cardiac arrest."),
    ('b', "**Blood pressure and cardiac output fall; uteroplacental perfusion is compromised.** Preload falls, so output can drop by a quarter or more. Uterine flow suffers twice: lower maternal output, and aortic compression lowering pressure in the uterine arteries, so the fetal heart trace can deteriorate even when the pressure measured in her arm looks acceptable."),
    ('c', "**Left uterine displacement: a wedge under the right hip, or manual displacement of the uterus to the left.** The vena cava lies to the right of the spine, so the uterus is moved to the left: a 15° left lateral tilt, a wedge under the right hip, or a hand pushing or pulling the uterus leftwards. In cardiac arrest the method is manual displacement with the woman flat on a firm surface, because a tilted chest makes compressions less effective; this is the job of the second rescuer."),
    ('d', "**From about 20 weeks (uterus at the umbilicus).** If gestation is unknown, a uterus palpable at or above the umbilicus is the trigger. The same landmark defines who is considered for perimortem caesarean delivery: if circulation has not returned by about 4 minutes of correct resuscitation, the uterus is emptied (aiming for delivery by 5 minutes) to relieve the compression and help the mother’s resuscitation."),
  ],
  mimic=[
    ("Supine hypotension vs haemorrhage in a pregnant trauma patient", "Both give hypotension and tachycardia on the table. Displacement of the uterus restores pressure within a minute in aortocaval compression; if it does not, look for bleeding. Displace first, then investigate."),
  ],
  traps=[
    ("“Tilt the whole patient during CPR”", "Tilt reduces compression force and makes airway work and defibrillation awkward; keep her supine and displace the uterus by hand."),
    ("“Half-dose adrenaline”, “delay intubation until ROSC” or “magnesium immediately” in maternal arrest", "Drugs, doses and shock energies are unchanged; the airway is secured early because of aspiration risk; magnesium is for eclampsia, not an arrest drug (calcium is given if she was on magnesium). The critical modification is manual left uterine displacement (97% right)."),
    ("“The second rescuer is there for the perimortem caesarean”", "The NEET 2025 key is uterine displacement, needed from the first compression; perimortem delivery follows at 4–5 minutes if there is no return of circulation."),
    ("“Give a fluid bolus or vasopressor first for hypotension when supine at 35 weeks”", "Reposition first; it is immediate and treats the cause."),
  ],
  decode=[
    ("28 weeks, cardiac arrest in ICU: the most critical modification to ACLS? [DocT]", "Manual left uterine displacement during CPR (97%)."),
    ("Pregnant woman in cardiac arrest, two rescuers: why is the second essential? [NEET 2025]", "Uterine displacement."),
    ("35-week trauma patient hypotensive supine in theatre: next step? [Marrow]", "Reposition: left uterine displacement."),
  ],
  extra=[dict(q="Where should venous access be placed in maternal cardiac arrest, and when is perimortem caesarean delivery started?", a="Access above the diaphragm, so drugs are not held up by the compressed vena cava (OBS-13a). With a uterus at or above the umbilicus and no return of circulation by about 4 minutes, start perimortem delivery at the site of arrest, aiming to deliver by 5 minutes.")],
  punch="From 20 weeks the supine uterus squeezes the vena cava and aorta, dropping output and placental flow; the fix is left uterine displacement, done by hand by a second rescuer during CPR.",
)

L['OBS-07'] = dict(
  sub="Obstetrics → Physiology → Blood, kidney and gut",
  step=2,
  intro="Step 2 ends with three systems whose normal laboratory values shift, so that an unremarkable-looking result can be abnormal. Two Grand Test questions come from part a and the watch line: why haemoglobin is low, and which way fibrinogen moves.",
  parts=[
    ('a', "**Plasma volume rises more than red cell mass: dilutional anaemia.** Plasma expands by about 45–50% and red cell mass by only 20–30%, so haemoglobin concentration falls although the total amount of haemoglobin has gone up. A haemoglobin of 10.5–11 g/dL with normal iron studies is physiological. Clotting moves the other way: fibrinogen rises (to about 4–6 g/L) with factors VII, VIII, X and von Willebrand factor, and protein S falls. Pregnancy is hypercoagulable, which protects against bleeding at delivery and raises the risk of thrombosis, and it means a fibrinogen of 2 g/L during postpartum haemorrhage is already low and predicts severe bleeding."),
    ('b', "**GFR and renal plasma flow rise by about half; creatinine falls (to about 0.4–0.8 mg/dL).** Renal vasodilatation and the higher cardiac output increase filtration, so creatinine and urea fall. A creatinine of 1.0 mg/dL, normal on the laboratory report, can represent the loss of a large fraction of her GFR. Renally cleared drugs are eliminated faster. The ureters and renal pelves dilate, more on the right, which predisposes to pyelonephritis (OBS-02)."),
    ('c', "**Lower oesophageal sphincter relaxes (progesterone); slow transit; constipation.** Progesterone relaxes smooth muscle throughout the gut, and the uterus displaces the stomach and raises intragastric pressure, so the barrier pressure across the sphincter falls. Gastric emptying itself is close to normal until labour, when pain and opioids slow it markedly."),
    ('d', "**Aspiration: full abdomen, lax sphincter, slow transit.** She is treated as having a full stomach from mid-pregnancy: rapid sequence induction with a cuffed tube, antacid prophylaxis before anaesthesia, and caution with non-invasive ventilation when consciousness is reduced (OBS-08, OBS-12)."),
    ('e', "**A high-calorie state; needs rise in labour and are highest in lactation.** Energy needs rise by roughly 300 kcal/day in later pregnancy and about 500 kcal/day in lactation. Fasting leads to ketosis sooner than in a non-pregnant woman, so prolonged starvation in a critically ill pregnant woman is avoided."),
  ],
  mimic=[
    ("Dilutional anaemia vs iron deficiency in pregnancy", "Dilutional: haemoglobin about 10.5–11 g/dL, normal MCV and ferritin. Iron deficiency: lower haemoglobin, low MCV and ferritin."),
    ("Normal pregnancy coagulation vs early DIC", "Normal: fibrinogen 4–6 g/L, platelets normal or slightly low. Early DIC (abruption, amniotic fluid embolism, haemorrhage): fibrinogen falling to 2 g/L or less, which a non-pregnant reference range would still call normal."),
  ],
  traps=[
    ("“Fibrinogen decreases in pregnancy”", "It rises; ‘decreased fibrinogen’ is the option that is NOT a physiological change. Reduced FRC, increased cardiac output and increased GFR are all true."),
    ("“Anaemia of pregnancy is due to increased red cell mass, increased oxygen consumption or low resistance”", "Red cell mass does increase, which would raise haemoglobin; the concentration falls because plasma volume expands more."),
    ("“A creatinine of 1.0 mg/dL is normal in pregnancy”", "Above about 0.8 mg/dL is abnormal and should prompt a search for pre-eclampsia, sepsis or obstruction."),
  ],
  decode=[
    ("38 weeks, Hb 10.8 g/dL, normal iron studies, no bleeding: which adaptation explains it? [DocT GT]", "Plasma volume expansion."),
    ("Which is NOT a physiological change of pregnancy? [DocT GT]", "Decreased fibrinogen (it rises)."),
    ("[pattern] Pregnant woman with creatinine 1.1 mg/dL — interpretation?", "Renal impairment; the pregnant range is about 0.4–0.8."),
  ],
  punch="Plasma expands more than red cells, so haemoglobin falls while fibrinogen and clotting factors rise; GFR rises by half, so creatinine above 0.8 mg/dL is abnormal; and a lax sphincter makes every pregnant woman an aspiration risk.",
)

L['OBS-08'] = dict(
  sub="Obstetrics → Airway → Why the pregnant airway is difficult",
  step=4,
  intro="Step 4 takes the physiology to the laryngoscope. Three things from step 2 arrive together at induction: swollen upper-airway mucosa, a small oxygen store with a high rate of use, and a stomach that can empty into the pharynx. The real questions ask the consequence: when she needs an airway, it is a cuffed tracheal tube, placed early.",
  parts=[
    ('a', "**Oedema, mucosal engorgement, capillary friability: bleeding and a narrow view.** Oestrogen and the expanded blood volume engorge the mucosa of the nose, pharynx and larynx. The glottic opening is smaller, the tissues bleed on contact, and each failed attempt makes the next view worse. The swelling is greater in pre-eclampsia, after prolonged pushing and with fluid loading. Nasal tubes and airways are avoided because of bleeding."),
    ('b', "**2.5 to 3 times more difficult than in the non-pregnant patient.** This is the multiplier in the notes. The audit figure usually quoted for failed intubation at obstetric general anaesthesia is about 1 in 390 (Kinsella 2015), against roughly 1 in 2000 in general surgical practice, so many texts give a larger ratio; either way the direction is what is tested."),
    ('c', "**Low functional residual capacity (small reservoir) plus high oxygen consumption (fast drain).** FRC is down 20% (more when supine) and oxygen use is up 30–40% (OBS-03, OBS-04). After full pre-oxygenation an apnoeic term woman falls below a saturation of 90% in about 5 minutes on physiological modelling, against about 7½ minutes for a non-pregnant woman, and once below 90% she falls faster; the time is shorter still in labour, obesity or sepsis, or if pre-oxygenation was incomplete."),
    ('d', "**Aspiration risk; large breasts; weight gain.** The lax sphincter and raised gastric pressure (OBS-07) make regurgitation likely at induction. Enlarged breasts obstruct the laryngoscope handle, and weight gain adds soft tissue around the airway."),
    ('e', "**Smaller tube (6.5–7.0), short-handled laryngoscope, ramped position, full pre-oxygenation.** The smaller tube passes the swollen glottis with less trauma; the short handle clears the breasts; ramping (ear level with the sternal notch) with head-up tilt improves the view and adds FRC; pre-oxygenation with a tight mask to an end-tidal oxygen of 90% or more, plus nasal oxygen during apnoea, buys time. Left uterine displacement continues throughout (OBS-06)."),
  ],
  mimic=[
    ("Difficulty from the airway vs difficulty from time", "The view is harder (oedema, breasts, bleeding) and the time available is shorter (low FRC, high oxygen use). The first is answered by equipment and position; the second by pre-oxygenation and a limit on attempts (OBS-11)."),
  ],
  traps=[
    ("“A laryngeal mask is the preferred airway device in a pregnant arrest”", "The tracheal tube is preferred because it protects against aspiration (92% right); a supraglottic airway is the rescue device when intubation fails (OBS-11)."),
    ("“Trial of CPAP or NIV for a drowsy pregnant woman with ARDS”", "Reduced consciousness plus a full stomach makes NIV unsafe; the key is intubation (86–90%). NIV is for the alert, cooperative patient with a prompt response."),
    ("“The main reason intubation is harder is the large breasts or weight gain”", "They contribute; the keyed main reason on the card is airway oedema, engorgement and friability."),
    ("“Use a standard 7.5–8.0 tube”", "Go down to 6.5–7.0 for the swollen glottis."),
  ],
  decode=[
    ("Preferred airway management device during ACLS in a pregnant patient? [DocT]", "Endotracheal tube (92%)."),
    ("30 weeks, P/F 170, bilateral infiltrates, drowsy despite oxygen: next step? [DocT GT ×2]", "Endotracheal intubation (86–90%); not CPAP with tocolysis, steroids or 100% oxygen indefinitely."),
    ("Why is intubation more difficult in pregnancy? [GT, cited on the card]", "Airway oedema and mucosal friability."),
  ],
  punch="The pregnant airway is swollen and bleeds easily, the oxygen store is small and used fast, and the stomach is never empty, so use a smaller tube in a ramped position after full pre-oxygenation, and intubate early when she is failing.",
)

L['OBS-09'] = dict(
  sub="Obstetrics → Recognition → Modified early obstetric warning score (MEOWS)",
  step=3,
  intro="Step 3 turns the shifted baseline of step 2 into a bedside chart. Young pregnant women compensate until late, so the chart is built to catch small departures early: each observation falls in a white, yellow or red band, and the bands, not a summed score, trigger the call.",
  parts=[
    ('a', "**Respiratory rate: normal 10–20; yellow 21–30; red under 10 or over 30.** Pregnancy deepens breathing without much change in rate (OBS-04), so the normal band is the same as in any adult and a raised rate is the earliest and most sensitive sign of sepsis, embolism, pulmonary oedema or bleeding."),
    ('b', "**Temperature: normal 36–37.4 °C; yellow 35–36 or 37.5–38; red under 35 or over 38.** Both ends count: hypothermia is as much a sign of sepsis as fever. The published chart has no upper yellow band: 35–36 °C is yellow and anything over 38 °C goes straight to red (see FLAGS)."),
    ('c', "**Systolic BP: normal 100–139; yellow 150–180 or 90–100; red over 180 or under 90.** These are the card’s figures. The published chart (CEMACH 2007; validated by Singh 2012) is tighter at the top: yellow 150–160 and red above 160, because a systolic of 160 or more is already severe hypertension that needs treatment within minutes to prevent intracranial haemorrhage (see FLAGS). The lower limit of 90 matches the obstetric qSOFA (OBS-10)."),
    ('d', "**Diastolic BP: normal 50–89; yellow 90–100; red over 100.** A diastolic of 90 defines hypertension in pregnancy, and the published chart’s red band is over 100, agreeing with the card’s uncertain scan. Diastolic normally dips in mid-pregnancy (OBS-03), so 90 at 24 weeks is a larger rise than it looks."),
    ('e', "**Heart rate: normal 50–99; yellow 100–120 or 40–50; red over 120 or under 40.** Resting pulse rises by only 10–20 beats/min, so a rate persistently above 100 is not put down to pregnancy; tachycardia is the first sign of concealed bleeding, well before pressure falls."),
    ('f', "**Neurological: normal alert; yellow responds to voice; red responds to pain only or unresponsive.** The AVPU scale. Oxygen saturation is also charted, normal 96–100%, with under 95% a red trigger on the published chart."),
  ],
  mimic=[
    ("MEOWS vs an aggregate score such as NEWS", "MEOWS is a colour-band trigger system: one red or two yellow observations prompt an urgent review, with no adding up. NEWS sums weighted points and uses non-pregnant ranges."),
  ],
  traps=[
    ("“A pulse of 115 or a respiratory rate of 24 is normal for pregnancy”", "Both are yellow, and together they trigger a review."),
    ("“Only a red observation triggers escalation”", "Two yellow observations trigger as well."),
    ("“Systolic pressure is acted on only above 180”", "On the published chart anything over 160 is red, and 160/110 is the treatment threshold for severe hypertension in pregnancy."),
  ],
  decode=[
    ("[pattern] Which combination triggers an urgent review on MEOWS?", "One red or two yellow observations."),
    ("[pattern] Postnatal woman: pulse 125, respiratory rate 22, temperature 37.8 °C — action?", "One red (pulse over 120) is enough on its own, and the respiratory rate is yellow as well: urgent medical review; look for sepsis or bleeding."),
  ],
  punch="MEOWS bands each observation white, yellow or red against pregnancy-adjusted ranges, and one red or two yellow observations trigger an urgent review; respiratory rate over 30, pulse over 120 and systolic under 90 are red.",
)

L['OBS-10'] = dict(
  sub="Obstetrics → Recognition → Obstetrically modified qSOFA",
  step=3,
  intro="Step 3 applies the same idea to sepsis screening. Ordinary qSOFA would flag many healthy pregnant women, because a systolic of 100 and a respiratory rate of 22 are within reach of normal pregnancy, so the obstetric version (SOMANZ 2017) moves two of the three cut-offs.",
  parts=[
    ('a', "**Systolic BP: 90 or less in pregnancy (100 or less in the non-pregnant).** Resistance is 20% lower and pressure dips in mid-pregnancy (OBS-03), so 95–100 systolic is common in health; 90 or less is not."),
    ('b', "**Respiratory rate: 25 or more in pregnancy (22 or more in the non-pregnant).** Progesterone raises ventilation, mostly by depth with a small effect on rate, so the threshold is moved up to keep the screen specific."),
    ('c', "**Mentation: anything other than alert in pregnancy (GCS under 15 in the non-pregnant).** The same idea in simpler bedside terms (AVPU). As with qSOFA, two or more of the three criteria in a woman with suspected infection mark a high risk of organ dysfunction and call for a full assessment, lactate, cultures and antibiotics."),
  ],
  mimic=[
    ("omqSOFA vs qSOFA", "Pregnant: systolic ≤90, rate ≥25, not alert. Non-pregnant: systolic ≤100, rate ≥22, GCS <15. The blood pressure threshold moves down and the respiratory threshold moves up."),
    ("omqSOFA vs MEOWS", "omqSOFA is a three-item screen for sepsis-related organ dysfunction in suspected infection. MEOWS is a general observation chart for any deterioration."),
  ],
  traps=[
    ("“Both thresholds are lowered in pregnancy”", "They move in opposite directions: pressure down to 90, respiratory rate up to 25."),
    ("“A negative screen excludes sepsis”", "qSOFA-type screens are specific, not sensitive; a pregnant woman with suspected infection and one criterion still needs lactate and review."),
  ],
  decode=[
    ("[pattern] Which is a criterion of the obstetrically modified qSOFA?", "Systolic BP 90 mmHg or less; respiratory rate 25/min or more; any mentation other than alert."),
    ("[pattern] 30 weeks, pyelonephritis, BP 98/60, respiratory rate 23, alert — omqSOFA?", "Zero: neither threshold is met, though both would score on ordinary qSOFA."),
  ],
  punch="The obstetric qSOFA uses systolic 90 or less, respiratory rate 25 or more and any mentation other than alert, because normal pregnancy already has a lower pressure and more ventilation.",
)

L['OBS-11'] = dict(
  sub="Obstetrics → Airway → Obstetric failed intubation (OAA/DAS 2015)",
  step=4,
  intro="Step 4 ends with the plan for when the tube will not pass. The OAA/DAS 2015 guideline is three linked algorithms (safe general anaesthesia, failed intubation, can’t intubate can’t oxygenate), and the card compresses them into five lines. Two NEET 2025 recalls sit on the last step, and one of them has a disputed key.",
  parts=[
    ('a', "**Rapid sequence induction; face-mask ventilation allowed, pressure under 20 cmH₂O.** Gentle mask ventilation during the apnoeic period is permitted because she desaturates fast (OBS-08); keeping the inflation pressure at or below 20 cmH₂O avoids opening the lower oesophageal sphincter and inflating the stomach."),
    ('b', "**At most 2 intubation attempts; a third only by an experienced colleague.** Every attempt worsens oedema and bleeding in a friable airway, so the limit is strict and each attempt should change something: position, blade, videolaryngoscope, bougie, release of cricoid pressure."),
    ('c', "**Declare failed intubation; call for help; oxygenate with a supraglottic airway (at most 2 attempts) or face mask.** Saying it aloud stops further attempts at the tube and turns the team to oxygenation. A second-generation supraglottic airway is preferred because it has a gastric drain and a better seal; cricoid pressure is released for insertion."),
    ('d', "**If oxygenation succeeds: decide whether it is essential and safe to proceed with surgery, or wake.** This decision is specific to obstetrics. Waking is the default in most failed intubations, but if the mother’s life depends on delivery (haemorrhage, cardiac arrest) or the fetus is in immediate danger, surgery can proceed on the supraglottic airway. The guideline asks the team to settle this before induction."),
    ('e', "**If it fails: declare can’t intubate, can’t oxygenate; 100% oxygen; ensure neuromuscular block; front-of-neck access.** Full paralysis excludes laryngospasm and gives the best chance for one last attempt at mask or supraglottic oxygenation and the best conditions for the neck. Front-of-neck access is a scalpel cricothyroidotomy: transverse stab through the cricothyroid membrane, bougie, then a 6.0 cuffed tube. If the mother arrests, perimortem delivery follows (OBS-06)."),
  ],
  mimic=[
    ("Failed intubation vs can’t intubate, can’t oxygenate", "Failed intubation: the tube will not pass but oxygen can still be delivered by mask or supraglottic airway; go to a supraglottic airway. CICO: neither works and saturation is falling; go to the neck."),
    ("Obstetric (OAA/DAS 2015) vs general adult (DAS 2015) limits", "Obstetric: 2 intubation attempts plus 1 by an experienced colleague, and 2 supraglottic attempts. General adult: 3 plus 1, and 3 supraglottic attempts."),
    ("Cricothyroidotomy vs tracheostomy on an image", "Cricothyroidotomy: incision through the cricothyroid membrane, between the thyroid and cricoid cartilages, the emergency route. Tracheostomy: lower, between tracheal rings, elective."),
  ],
  traps=[
    ("“Cricothyrotomy after two failed attempts when mask ventilation is difficult” (the NEET 2025 key)", "The recall keys emergency cricothyrotomy. By DAS and OAA/DAS, mask ventilation that is difficult but possible means the next step is a supraglottic airway; the neck is opened only when supraglottic airway and mask have both failed. If the stem says ventilation is impossible, cricothyrotomy is right; if it is only difficult and a supraglottic airway is offered, that is the guideline answer, though the recalled key is cricothyrotomy."),
    ("“Repeat intubation with a bougie” or “fibreoptic intubation” after the attempts are used up", "More instrumentation of a failing airway loses time and oxygen; move to oxygenation."),
    ("“After a failed obstetric intubation, always wake the patient”", "If oxygenation is secure and delivery is essential for the mother or fetus, surgery may proceed on the supraglottic airway."),
  ],
  decode=[
    ("Cormack–Lehane grade 4, two failed attempts, bag-mask ventilation also difficult: next step? [NEET 2025]", "Keyed emergency cricothyrotomy; guideline-correct only if oxygenation is failing (CICO). If ventilation is merely difficult, a supraglottic airway comes first."),
    ("Which procedure is being performed here (image)? [NEET 2025]", "Cricothyroidotomy: scalpel through the cricothyroid membrane."),
    ("[pattern] Failed intubation at emergency caesarean, supraglottic airway ventilating well, massive haemorrhage — proceed or wake?", "Proceed with surgery: maternal life depends on it and oxygenation is secured."),
  ],
  punch="Two attempts at the tube (a third only by an expert), then declare failure and oxygenate with a supraglottic airway or mask; if that works decide whether to proceed or wake, and if it fails paralyse fully and open the cricothyroid membrane. Oxygenation, not intubation, is the goal.",
)

L['OBS-12'] = dict(
  sub="Obstetrics → Organ support → Ventilating the pregnant patient",
  step=5,
  intro="Step 5 starts with the ventilator. Lung protection is the same as in any ARDS, and the pregnancy-specific rules exist only to protect fetal gas exchange: the fetus needs a well-saturated mother and a maternal PaCO₂ low enough for its own carbon dioxide to diffuse out. Four Grand Test questions test the oxygen target, the tidal volume (with a key that is wrong) and when to intubate.",
  parts=[
    ('a', "**Plateau pressure under 30 cmH₂O.** Standard lung protection: 6 mL/kg predicted body weight with the plateau kept under 30. Predicted weight comes from height, so pregnancy weight gain does not enlarge the breath. The gravid abdomen stiffens the chest wall, so a given plateau pressure distends the lung less than usual and a slightly higher plateau may be accepted late in pregnancy, but no guideline recommends larger tidal volumes."),
    ('b', "**Avoid permissive hypercapnia: maternal CO₂ retention causes fetal acidosis.** Fetal PCO₂ runs about 10 mmHg above maternal so that carbon dioxide can cross the placenta. Raise maternal PaCO₂ and the fetal value rises with it, producing fetal respiratory acidosis and a right shift of fetal haemoglobin that reduces its oxygen uptake. Aim near her normal (about 30–32 mmHg, the card’s watch line) and avoid values much above 45; reach it with rate, not volume. Do not over-ventilate either: marked alkalosis constricts the uterine vessels."),
    ('c', "**Prone: avoids compression by the gravid uterus and of the umbilical vessels, improving fetal blood flow.** Prone positioning is used for the same indications as in other adults and is feasible in pregnancy with supports under the chest and pelvis so that the abdomen hangs free; that unloads the vena cava and aorta as well as improving oxygenation. The fetal heart is monitored when the fetus is viable."),
    ('d', "**Refractory hypoxaemia: VV-ECMO.** Pregnancy is not a contraindication, and reported maternal and fetal survival is good; these are young patients with a single failing organ. Anticoagulation and cannula flow past the gravid uterus need planning."),
    ('e', "**Expedited delivery may improve the mother’s outcome: a multidisciplinary decision.** Emptying the uterus lowers oxygen consumption, lifts FRC and removes aortocaval compression, but the gain in oxygenation is inconsistent and surgery in a hypoxaemic woman is hazardous. Delivery is for obstetric indications or a viable fetus in jeopardy, and for a mother who cannot be oxygenated otherwise; it is decided with obstetricians and neonatologists after she has been stabilised."),
  ],
  table=dict(title="Ventilator targets in pregnancy", head=["Setting", "Target", "Reason"], rows=[["Tidal volume", "**6 mL/kg predicted body weight**", "same as any ARDS (DocT keys 8–9 mL/kg; disputed)"], ["Plateau pressure", "**under 30 cmH₂O**", "stiff chest wall may justify slightly more"], ["Oxygenation", "**SpO₂ 95% or more, PaO₂ above 70 mmHg**", "fetal oxygen delivery; fetal haemoglobin needs a well-saturated mother"], ["PaCO₂", "**about 30–32 mmHg; no permissive hypercapnia**", "keeps the gradient for fetal CO₂"], ["Position", "left uterine displacement; prone if indicated", "aortocaval compression"]]),
  mimic=[
    ("Oxygen target in pregnancy vs other ARDS", "Non-pregnant ARDS: SpO₂ 88–95%, PaO₂ 55–80 mmHg. Pregnancy: SpO₂ 95% or more, PaO₂ above 70 mmHg, because the fetus sits on the steep part of its own dissociation curve."),
    ("CO₂ strategy in pregnancy vs other ARDS", "Non-pregnant: permissive hypercapnia accepted for lung protection. Pregnancy: avoided; rate is raised to hold PaCO₂ near the pregnant normal."),
  ],
  traps=[
    ("“8–9 mL/kg is the safe tidal volume for ARDS in pregnancy” (the DocT key, 3% right)", "The key is wrong by current practice. The physiological rise in her spontaneous tidal volume is not a reason to ventilate injured lungs with larger breaths; use 6 mL/kg predicted body weight with a plateau under 30. Pick 6–7 mL/kg on principle, and know that this DocT paper keys 8–9."),
    ("“SaO₂ of 85% or more is acceptable”", "That is below even the non-pregnant ARDS range and too low for the fetus; the key is SaO₂ 95% or more."),
    ("“FiO₂ 100% continuously” or “FiO₂ 80% or more” to protect the fetus", "The target is a saturation, reached with the lowest FiO₂ and adequate PEEP; sustained high FiO₂ adds oxygen toxicity and absorption collapse."),
    ("“Start CPAP and tocolysis” in a drowsy woman with P/F 170", "Drowsiness removes airway protection in a patient at high aspiration risk; intubate. Tocolysis and delivery are decided after the mother is stabilised."),
    ("“High-dose corticosteroids” as the next step", "Not a treatment for hypoxaemic respiratory failure here; betamethasone for fetal lungs (OBS-13) is a separate, low-dose indication."),
    ("“Permissive hypercapnia is fine if pH stays above 7.2”", "The fetus becomes acidotic before the mother does."),
  ],
  decode=[
    ("Pregnant woman with ARDS, oxygenation improved after recruitment: which oxygenation target? [DocT GT]", "SaO₂ 95% or more."),
    ("Safe tidal volume in ARDS in pregnancy? [DocT GT]", "Keyed 8–9 mL/kg (3% right); the correct practice is 6 mL/kg predicted body weight."),
    ("30 weeks, bilateral infiltrates, P/F 170, drowsy despite oxygen: next step? [DocT GT ×2]", "Endotracheal intubation (86–90%)."),
    ("[pattern] Ventilated at 28 weeks, PaCO₂ 58 mmHg on lung-protective settings — what should change?", "Raise the rate to bring PaCO₂ down towards the pregnant range; permissive hypercapnia is avoided because of fetal acidosis."),
  ],
  punch="Ventilate her as any ARDS (6 mL/kg predicted weight, plateau under 30) with two fetal adjustments: saturation 95% or more, and no permissive hypercapnia. Prone and VV-ECMO remain available, and delivery is a team decision after stabilisation.",
)

L['OBS-13'] = dict(
  sub="Obstetrics → Organ support → Circulation and the decision to deliver",
  step=5,
  intro="Step 5 continues with the circulation. Resuscitation is the same as in any adult, with the uterus kept off the vena cava and lines placed where the drugs will reach the heart. The card then covers the two fetal questions that come with every admission: has she had steroids, and should she be delivered. A NEET 2025 recall on the vasopressor of choice hangs on part b.",
  parts=[
    ('a', "**Two large-bore peripheral cannulae; avoid the femoral route; left uterine displacement.** The uterus compresses the inferior vena cava, so fluid and drugs given through a femoral or leg vein may be delayed in reaching the heart; access goes above the diaphragm. The femoral site also carries a higher thrombosis risk in a hypercoagulable patient and is in the way at delivery. Displacement of the uterus is part of resuscitation, not an extra (OBS-06)."),
    ('b', "**Crystalloids, vasopressors and inotropes as in any patient.** No drug needed to save the mother is withheld for the fetus; the uterine bed does not autoregulate, so restoring maternal pressure restores placental flow. For septic shock, or haemorrhagic shock after volume, noradrenaline is first line as outside pregnancy. Phenylephrine is the agent of choice for hypotension after spinal anaesthesia at caesarean section, where it causes less fetal acidosis than ephedrine. Fluid is given with care in pre-eclampsia, where capillary leak and low oncotic pressure favour pulmonary oedema."),
    ('c', "**Two doses of betamethasone, 24 hours apart.** 12 mg intramuscularly, twice (the notes’ ‘beclomethasone’ is a misprint, as the watch line says); the alternative is dexamethasone 6 mg every 12 hours for four doses. Both cross the placenta and speed surfactant production, reducing neonatal respiratory distress, intraventricular haemorrhage and death. They are given when delivery is likely within a week between about 24 and 34 weeks, and maternal critical illness, sepsis included, is not in itself a contraindication when preterm delivery is expected; delivery that the mother needs is not delayed to complete the course."),
    ('d', "**Fetal monitoring: biophysical profile.** Ultrasound scoring of fetal breathing, movement, tone and liquor volume, with a non-stress test. Once the fetus is viable, the fetal heart trace is also a continuous monitor of uterine perfusion: late decelerations or lost variability often mean the mother is under-resuscitated."),
    ('e', "**Delivery decision: multidisciplinary; correct coagulopathy first.** Delivery is treatment when the disease is driven by the pregnancy (pre-eclampsia, HELLP, acute fatty liver, chorioamnionitis) and is otherwise for obstetric indications. The mother is stabilised first and platelets, fibrinogen and clotting are corrected, because operating on a coagulopathic patient converts one problem into haemorrhage. The exception is cardiac arrest, where delivery is part of the resuscitation."),
  ],
  mimic=[
    ("Vasopressor for spinal hypotension vs for shock in pregnancy", "Spinal hypotension at caesarean: phenylephrine. Septic or other shock in a pregnant ICU patient: noradrenaline first, as in any adult."),
    ("Betamethasone vs beclomethasone", "Betamethasone (and dexamethasone) cross the placenta in active form and mature the fetal lung. Beclomethasone is an inhaled asthma steroid; prednisolone and hydrocortisone are largely inactivated by the placenta and are used when the mother, not the fetus, is the target."),
  ],
  traps=[
    ("“Phenylephrine is the vasopressor of choice in pregnancy” applied to septic shock", "The NEET 2025 recall keys phenylephrine with no setting given, and that is the answer to the bare question. It holds for spinal hypotension; if the stem describes septic shock in a pregnant woman, noradrenaline is first line."),
    ("“Avoid vasopressors because they reduce uterine blood flow”", "Maternal hypotension reduces it more; treat the mother as any patient."),
    ("“A femoral line is the quickest safe access in a collapsed pregnant woman”", "Drugs may pool below the compressed vena cava; use the arms, neck or humeral intraosseous route."),
    ("“Deliver first, then correct the coagulopathy”", "Correct first, except in maternal arrest."),
  ],
  decode=[
    ("Vasopressor of choice in pregnancy? [NEET 2025]", "Phenylephrine as keyed (spinal hypotension); noradrenaline if the stem is septic shock."),
    ("[pattern] 30 weeks, septic shock, delivery may be needed within days — which drug for fetal lung maturity and how?", "Betamethasone 12 mg IM, two doses 24 hours apart."),
    ("[pattern] Where should venous access be sited in a shocked woman at 34 weeks?", "Above the diaphragm; avoid the femoral route."),
  ],
  extra=[dict(q="Which vasopressor for hypotension in a pregnant woman?", a="It depends on the setting: phenylephrine for hypotension after spinal anaesthesia at caesarean (less fetal acidosis than ephedrine); noradrenaline first line for septic shock or other shock in the ICU, as outside pregnancy.")],
  punch="Resuscitate her as any patient, with lines above the diaphragm and the uterus displaced; give betamethasone 12 mg twice, 24 hours apart, when preterm delivery is likely; and deliver by team decision after stabilising her and correcting coagulopathy.",
)

L['OBS-14'] = dict(
  sub="Obstetrics → Organ support → Radiation in pregnancy",
  step=5,
  intro="Step 5 closes with imaging, where the usual error is to withhold a scan the mother needs. The fetal dose depends on whether the fetus lies in the beam, and for almost every single test it is far below the level at which harm has been shown.",
  parts=[
    ('a', "**Very low, under 0.1 mGy: chest X-ray, limb X-ray, mammography.** The fetus is outside the beam and receives only scatter. A chest film delivers about 0.0005–0.01 mGy, less than a few days of natural background radiation."),
    ('b', "**Low to moderate, 0.1–10 mGy: abdominal X-ray, lumbar spine, IVP, CT chest or CT pulmonary angiogram (0.01–0.66 mGy).** Plain films through the abdomen put the fetus in the beam but with a small dose. A CT pulmonary angiogram, although a CT, gives the fetus very little because the uterus is outside the scanned volume; its dose falls at or below the bottom of this band. A low-dose perfusion scan is similar (about 0.1–0.5 mGy)."),
    ('c', "**High, 10–50 mGy: abdominal or pelvic CT, whole-body PET/CT.** Here the fetus is in the primary beam. Even so, a single abdominopelvic CT usually stays under 50 mGy, so in trauma or suspected intra-abdominal sepsis it is done when needed."),
    ('d', "**Fetal harm is not expected below 50 mGy.** Malformation, growth restriction and miscarriage are threshold effects that have not been seen below this dose; the most sensitive period for the brain is about 8–15 weeks. The small rise in childhood cancer risk has no threshold but is very low at diagnostic doses. Ultrasound and MRI without gadolinium are preferred when they answer the question equally well; iodinated contrast can be given if needed."),
  ],
  mimic=[
    ("CT pulmonary angiogram vs V/Q scan in pregnancy", "Fetal dose is low with both and of the same order. CTPA gives more radiation to the mother’s breast; a V/Q (or perfusion-only) scan is favoured when the chest film is normal, CTPA when it is abnormal or she is unstable."),
  ],
  traps=[
    ("“CT pulmonary angiography is contraindicated in pregnancy”", "Fetal dose is 0.01–0.66 mGy, at least 75 times below the 50 mGy threshold; an undiagnosed embolism is the real danger."),
    ("“Shield the abdomen or skip the chest film”", "A chest film is in the very-low band; a necessary investigation is never withheld (ACOG 2017)."),
    ("“Any CT carries a high fetal dose”", "Only CT through the abdomen or pelvis reaches the 10–50 mGy band."),
  ],
  decode=[
    ("[pattern] Which test gives the highest fetal radiation dose?", "Abdominal or pelvic CT (or whole-body PET/CT), 10–50 mGy."),
    ("[pattern] 28 weeks, suspected pulmonary embolism, unstable — can CTPA be done?", "Yes: fetal dose under 1 mGy, below the 50 mGy threshold for harm."),
    ("[pattern] Below what fetal dose is harm not expected?", "50 mGy."),
  ],
  punch="Fetal dose is under 0.1 mGy for a chest film, under 1 mGy for a CT pulmonary angiogram and 10–50 mGy for abdominal or pelvic CT, and harm is not expected below 50 mGy, so no scan the mother needs is withheld.",
)

FLAGS = {}
FLAGS['OBS-01'] = "Watch line: the pie chart (pre-eclampsia/eclampsia 75%, medical 14%, haemorrhage 11%) was matched by position in the scan and could not be verified; proportions vary widely between series. Explanation restates the card and says so."
FLAGS['OBS-02'] = "Watch line: ‘Marfan syndrome with an aortic root over 4 cm’ is the older threshold. ESC 2018 (modified WHO) puts an aortic root of 40–45 mm in class III (significantly increased risk) and over 45 mm in class IV (pregnancy contraindicated). Explanation keeps the card’s 4 cm as the point at which risk rises."
FLAGS['OBS-03'] = "Card gives the antenatal figures only. DocT GT keys a 60–80% rise in cardiac output ‘in active labour’ (41% right); standard texts put about +50% in the second stage and the 60–80% peak immediately post partum. The card could add ‘labour / just delivered: 60–80%’ and the normal auscultation (S3, loud split S1, soft systolic flow murmur). Oxygen consumption ‘up 30–40%’ is at the upper end of published figures (20–40%)."
FLAGS['OBS-05'] = "Card prints base excess ‘no change’ in pregnancy. With bicarbonate 18–22 at pH 7.40–7.47 the base excess is mildly negative (a small base deficit of a few mmol/L from renal compensation). None of the sources checked online (Deranged Physiology, OpenAnesthesia, Brandis) prints a base-excess figure, so no exact range is given; explanation restates the card and adds the direction only."
FLAGS['OBS-08'] = "Card b (‘2.5 to 3 times more difficult’) is the notes’ multiplier; commonly quoted audit figures are about 1 in 390 failed intubations at obstetric general anaesthesia (Kinsella 2015) against about 1 in 2000 in general practice, which is a larger ratio. Not changed; explanation gives both. The GT question cited in the watch lines of OBS-04 and OBS-08 (GT-4 Q29, GT-3 Q47) could not be found under those numbers in the DocT GT file (those numbers are asthma-in-pregnancy questions there)."
FLAGS['OBS-09'] = "Systolic BP bands on the card (yellow 150–180, red over 180) differ from the published MEOWS chart (CEMACH 2007; Singh 2012, checked online): yellow 150–160 or 90–100, red over 160 or under 90. Diastolic red ‘over 100’ (unclear in scan) is correct. The published chart has no upper yellow temperature band (yellow 35–36 only; red under 35 or over 38) and makes SpO2 under 95% a red trigger. Explanation restates the card and gives the published values."
FLAGS['OBS-11'] = "Card is faithful to OAA/DAS 2015. NEET 2025 recall keys emergency cricothyrotomy after two failed attempts with DIFFICULT bag-mask ventilation; by DAS and OAA/DAS a supraglottic airway comes first unless oxygenation is impossible (CICO). Explanation follows the qbank fix: cricothyrotomy if ventilation is impossible, supraglottic airway if merely difficult."
FLAGS['OBS-12'] = "DocT GT keys 8–9 mL/kg as the safe tidal volume for ARDS in pregnancy (3% right); no guideline supports it, and 6 mL/kg predicted body weight applies (qbank fix). The card does not state a tidal volume and could add it. Watch line gives PaCO2 30–32 mmHg; the qbank fix says about 30–45 mmHg. Explanation gives 30–32 as the aim and ‘avoid much above 45’. Card c’s reason for prone (‘avoids compression … of the umbilical vessels’) is the notes’ wording; the accepted point is that prone positioning with the abdomen free is feasible and relieves aortocaval compression."
FLAGS['OBS-13'] = "Card b (‘as in any patient’) is right; NEET 2025 recall keys phenylephrine as ‘the vasopressor of choice in pregnancy’ with no setting. Phenylephrine is correct for spinal hypotension at caesarean; noradrenaline is first line for shock (qbank fix). Explanation gives both. The gestation window for steroids (about 24–34 weeks) and the dexamethasone alternative are added from standard guidance, not from the card."
