# GI06 top-up cards — Explain v3 ("Learn" depth), same fields and voice as gi06_learn.py.
# Fields: sub, step (index into gi06_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions: the top-ups’ own src (DocT, DocT GT, Marrow QBank QB39); the stems were not in qpack/GI06.md, so decode items paraphrase the top-up question.
# Figures from standard teaching, checked against EASL 2023 ACLF CPG (alcohol-related hepatitis and Lille model, 20 Nov 2026): Maddrey DF ≥32, MELD >20–21, prednisolone 40 mg/day for 28 days,
# Lille >0.45 at day 7 = non-response; PREDICT/EASL clinical states of decompensated cirrhosis (acute vs non-acute decompensation separated by hospital admission).
# Second review (20 Nov 2026): Maddrey formula and DF ≥32, prednisolone 40 mg × 28 days, Lille >0.45 at day 7 rechecked, correct; Zieve jaundice wording changed to mixed, not purely unconjugated.
T = {}

T['T_cc325a06'] = dict(
  sub="GI → ACLF → Severe alcoholic hepatitis vs Zieve syndrome",
  step=1,
  intro="Step 1 names alcohol-related hepatitis as one of the two commonest hepatic triggers of ACLF. A jaundiced drinker is not always alcoholic hepatitis, though: Zieve syndrome looks similar, is a haemolytic picture and needs no steroids. Two bank questions (DocT and Marrow) test the distinction and the steroid rules.",
  parts=[
    ('a', "**Severe alcoholic hepatitis: Maddrey DF 32 or more (or MELD above 20): admit, prednisolone 40 mg/day for 28 days if there is no infection or GI bleed.** The discriminant function is 4.6 × (prothrombin time minus control) plus bilirubin in mg/dL; 32 or more marks a 1-month mortality of about a third without treatment. Steroids damp the inflammatory injury but raise infection risk, so infection and bleeding must be excluded or controlled first (GI06 ACLF-10, ACLF-11)."),
    ('b', "**Lille score above 0.45 at day 7 means non-response: stop steroids; 30-day mortality 30–50%; not for outpatient care.** Lille uses the fall in bilirubin over the first week with age, albumin, creatinine and prothrombin time. If bilirubin has not fallen, continuing steroids adds infection without benefit."),
    ('c', "**Zieve syndrome: after a binge on fatty liver or alcoholic hepatitis; Coombs-negative haemolysis (spherocytes, high LDH) plus jaundice plus marked hypertriglyceridaemia.** Haemolysis adds an unconjugated component to the jaundice of the underlying alcohol-related liver disease, with a high LDH and reticulocyte count; the triglycerides are often grossly raised. The red-cell membrane is thought to be damaged by the abnormal plasma lipids, which is why the haemolysis is Coombs-negative."),
    ('d', "**Zieve treatment is supportive (abstinence, transfusion); it settles in 4–6 weeks; no steroids.** Steroids add no benefit to a self-limiting haemolysis and would expose the patient to infection."),
  ],
  mimic=[
    ("Alcoholic hepatitis vs Zieve syndrome", "Alcoholic hepatitis: conjugated jaundice, high INR, neutrophilia, AST about twice ALT; Zieve: haemolysis (high LDH, reticulocytes, spherocytes, Coombs-negative) and very high triglycerides."),
  ],
  traps=[
    ("“Give prednisolone to every jaundiced alcoholic”", "Only for severe alcoholic hepatitis (DF 32 or more) without infection or bleeding; never for Zieve syndrome."),
    ("“Continue steroids for 28 days whatever the response”", "Stop at day 7 if Lille is above 0.45."),
  ],
  decode=[
    ("Jaundiced alcoholic, DF 40, no infection: treatment and when to stop [DocT, Marrow; paraphrased]", "Prednisolone 40 mg/day; stop at day 7 if Lille above 0.45."),
    ("Jaundice after a binge with Coombs-negative haemolysis and very high triglycerides [DocT, Marrow; paraphrased]", "Zieve syndrome: supportive care, no steroids."),
  ],
  punch="Severe alcoholic hepatitis (DF 32 or more) gets prednisolone after infection is excluded and stops at day 7 if Lille is above 0.45; Zieve syndrome is haemolysis with high triglycerides and settles without steroids.",
)

T['T_6144df58'] = dict(
  sub="GI → ACLF → Phases of decompensated cirrhosis",
  step=1,
  intro="Step 1 separates ACLF from the other clinical states of decompensated cirrhosis. The EASL/PREDICT framework draws its lines at hospital admission and at organ failure, and a Grand Test question asks where the lines fall.",
  parts=[
    ('a', "**Acute decompensation (AD): rapid ascites, HE, variceal bleed or infection needing hospital admission.** Admission is the marker because it captures a decompensation severe or fast enough to need inpatient care."),
    ('b', "**Non-acute decompensation (NAD): slowly progressive ascites or mild HE not needing admission.** Managed as an outpatient; it carries a better short-term outlook than AD."),
    ('c', "**ACLF: AD plus organ failure(s), high 28-day mortality.** Organ failure is counted by CLIF-OF (GI06 ACLF-06), and grade sets the risk (ACLF-08)."),
    ('d', "**Stable decompensated: previous decompensation, now controlled; hospitalisation is the dividing line between AD and NAD.**"),
  ],
  mimic=[
    ("AD vs NAD", "Both are new decompensation; AD needs admission, NAD does not."),
    ("AD vs ACLF", "Both are admitted; only ACLF has organ failure."),
  ],
  traps=[
    ("“New ascites managed in clinic is acute decompensation”", "Without admission it is non-acute decompensation."),
  ],
  decode=[
    ("Slowly increasing ascites managed as an outpatient: which phase? [DocT GT; paraphrased]", "Non-acute decompensation."),
  ],
  punch="Hospital admission separates acute from non-acute decompensation, and organ failure separates ACLF from acute decompensation.",
)

T['T_b7c7f544'] = dict(
  sub="GI → ACLF → Alcohol withdrawal in cirrhosis",
  step=4,
  intro="Step 4 is about supporting a failing patient without harming the liver, and sedation in alcohol withdrawal is the commonest drug choice where liver metabolism decides the answer. The Marrow question asks which benzodiazepine to choose.",
  parts=[
    ('a', "**Alcohol withdrawal: symptom-triggered benzodiazepine (CIWA-Ar).** Withdrawal is GABA-receptor downregulation unmasked when alcohol stops; benzodiazepines replace the missing GABA effect. Symptom-triggered dosing uses less drug than fixed schedules, which matters when clearance is poor."),
    ('b', "**With liver disease prefer lorazepam (or oxazepam): glucuronidation only, no active metabolites.** Glucuronidation is preserved until late in cirrhosis, while cytochrome P450 oxidation fails early."),
    ('c', "**Diazepam and chlordiazepoxide accumulate (oxidative metabolism, active metabolites) and can precipitate HE.** Their long-acting metabolites build up over days, so a patient who seemed settled becomes encephalopathic."),
    ('d', "**Thiamine before glucose; phenobarbital or dexmedetomidine as adjuncts for refractory withdrawal.** Glucose without thiamine can precipitate Wernicke encephalopathy. Dexmedetomidine controls the adrenergic symptoms but does not prevent seizures."),
  ],
  mimic=[
    ("Withdrawal vs hepatic encephalopathy", "Withdrawal: agitation, tremor, tachycardia, sweating, within 6–72 hours of the last drink; HE: drowsiness, asterixis, slowing."),
  ],
  traps=[
    ("“Chlordiazepoxide is the drug of choice in every alcoholic”", "Not in cirrhosis; its active metabolites accumulate."),
  ],
  decode=[
    ("Agitated tachycardic alcoholic with cirrhosis: benzodiazepine of choice [Marrow; paraphrased]", "Lorazepam (or oxazepam)."),
  ],
  punch="In cirrhosis treat withdrawal with symptom-triggered lorazepam or oxazepam, which are only glucuronidated, and give thiamine before glucose.",
)
