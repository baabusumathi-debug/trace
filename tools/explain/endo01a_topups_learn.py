# ENDO01A top-up cards — Explain v3 ("Learn" depth), same fields and voice as endo01a_learn.py.
# Fields: sub, step (index into endo01a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions read from /home/claude/wd/map/doct_qbank_all.jsonl (Thyroid-Related Disorders Q14–20) and doct_gt_distinct_all.jsonl (GT1o Q36, GT2o Q102, NEET 2025 recall Q120, Q122),
# matching each top-up's src. Second check, 22 Nov 2026 (reviewer), confirmed online: Endotext ‘The non-thyroidal illness syndrome’ (D1 down in liver, D3 up, D2 inconsistent; total T4
# <4 µg/dL up to 50% mortality, <2 µg/dL very poor; TSH transiently above normal in recovery; replacement unproven); StatPearls ‘Euthyroid sick syndrome’ (T4 <4 ~50%, <2 >80% mortality; TSH >20
# makes true thyroid disease likelier; test only on suspicion; retest no earlier than 6 weeks); SREAT summary (methylprednisolone 1 g/day IV for 3–7 days or prednisone 50–150 mg/day; thyroid
# abnormal in most reported cases; no controlled trials; IVIG and plasma exchange for non-responders).
T = {}

T['T_2b8a9a37'] = dict(
  sub="Endocrine → Thyroid → Non-thyroidal illness (sick euthyroid)",
  step=1,
  intro="Step 1 is about reading thyroid tests, and in the ICU the commonest abnormal result is not thyroid disease at all. Critical illness changes how T4 is converted and how the hypothalamus drives TSH, so the tests look hypothyroid while the gland is normal. This top-up is linked to 10 questions, more than any card in the deck.",
  parts=[
    ('a', "**Cytokines, cortisol and fasting cut type 1 and 2 deiodinase (less T4 to T3) and raise type 3 (more reverse T3), so T3 falls first.** IL-1, IL-6 and TNF-α act on the deiodinases, so the mechanism the questions want is inhibition of deiodinase activity, not more binding or more TSH. The firmest changes are less type 1 activity in the liver and more type 3 in liver and muscle; type 2 changes are inconsistent, and in some tissues it rises. Low T3 with high reverse T3 is the earliest and most consistent finding, and it may save energy during illness."),
    ('b', "**Hypothalamic TRH falls, so TSH is normal or low: an acquired, transient CENTRAL hypothyroidism (dopamine and steroids suppress TSH further).** Cytokines suppress both TRH and the pituitary’s response, so either answer may be keyed. Dopamine and high-dose steroids, common in the ICU, lower TSH further."),
    ('c', "**Low T3 alone = mild illness; low T4 with low TSH = severe (total T4 <4 µg/dL carries about 50% mortality).** The degree of abnormality follows the severity of illness: total T4 under 4 µg/dL carries up to about 50% mortality and under 2 µg/dL about 80%. A low T4 marks prognosis, not a thyroid problem to treat; the association does not show that the low T4 causes the deaths."),
    ('d', "**In recovery TSH can overshoot to 10–20 mIU/L; this is not primary hypothyroidism.** As the hypothalamus recovers, TSH rises above normal for a time to bring T4 back, usually staying below 20, so a mildly raised TSH in a recovering patient needs a repeat, not thyroxine; a TSH over 20 makes true primary hypothyroidism more likely."),
    ('e', "**Do not screen TFTs or give thyroxine: treat the illness, feed the patient, recheck 4–6 weeks after recovery; treat only clear primary disease (TSH >20 with low free T4).** Trials of thyroid hormone in non-thyroidal illness have not shown benefit. Routine testing in the ICU mainly creates false diagnoses, which is why testing should follow clinical suspicion. Some sources advise waiting at least 6 weeks after discharge, because an earlier test can catch the recovery rise."),
  ],
  table=dict(title="Sorting an ICU thyroid panel", head=["T3", "T4", "TSH", "Reading"], rows=[["low", "normal", "normal", "**mild non-thyroidal illness**: no treatment"], ["low", "low", "low", "severe illness; check pituitary only if the setting fits"], ["low", "normal or low", "mildly high (under 20)", "recovery phase, or early primary disease: repeat after recovery"], ["low", "low free T4", "**over 20**", "primary hypothyroidism: treat"]]),
  mimic=[
    ("Non-thyroidal illness vs central hypothyroidism from pituitary disease", "Both have low T4 with a low or normal TSH; pituitary disease has other hormone deficiencies, a sellar lesion or a history, and does not recover with the illness."),
    ("Recovery-phase TSH vs primary hypothyroidism", "Recovery: TSH under about 20, rising as the patient improves, normal on repeat. Primary: TSH over 20 with a low free T4, or persistent."),
  ],
  traps=[
    ("“Send free T4 and reverse T3” or “start IV levothyroxine” in septic shock with T3 60 and TSH 8 [DocT GT]", "No treatment is needed (only 21% right). A low T3 with a mildly raised TSH in sepsis is non-thyroidal illness; more tests change nothing and thyroxine does not help."),
    ("“Routine testing is harmless” in the critically ill [DocT QBank]", "Routine thyroid testing is the factor that leads to misdiagnosis (only 33% right); test only when thyroid disease is suspected."),
    ("“Decreased TRH” as the reason TSH is suppressed [DocT QBank]", "DocT keys direct cytokine action on the pituitary (71% right). Both happen; when both are offered, follow the key."),
    ("“Elevated TSH in non-thyroidal illness means primary hypothyroidism” [DocT QBank]", "It may represent recovery from an acquired transient central hypothyroidism (69% right); do not start thyroxine on it."),
  ],
  decode=[
    ("Septic shock, T3 low, TSH mildly high: most appropriate intervention [DocT GT]", "No further treatment."),
    ("Post-operative, malnourished, normal TSH and T4, low T3: management [DocT GT]", "Supportive care with nutrition (76% right)."),
    ("Mechanism of low T3 in non-thyroidal illness; how cytokines act [DocT QBank, NEET 2025]", "Down-regulated 5′-deiodinase; cytokines inhibit deiodinase activity."),
    ("Altered thyroid hormone levels without thyroid disease in the critically ill [NEET 2025]", "Sick euthyroid syndrome."),
  ],
  punch="In the ICU a low T3 with a low or normal TSH is the illness, not the thyroid: do not test routinely, do not give thyroxine, treat and feed the patient, and recheck after recovery.",
)

T['T_38ffd8d5'] = dict(
  sub="Endocrine → Thyroid → Hashimoto encephalopathy (SREAT)",
  step=5,
  intro="Step 5 is about the brain failing in thyroid disease, and Hashimoto encephalopathy is the case where the thyroid tests are often normal. It is an autoimmune encephalopathy associated with thyroid antibodies, recognised mainly by how well it responds to steroids. It is linked to one DocT question.",
  parts=[
    ('a', "**Steroid-responsive encephalopathy with autoimmune thyroiditis: high anti-TPO, usually EUTHYROID.** The antibodies are a marker, not the cause; their titre does not track the severity. Reported series in fact show many patients with subclinical or overt hypothyroidism, but the encephalopathy does not follow thyroid function: correcting it with levothyroxine does not treat the encephalopathy."),
    ('b', "**Subacute confusion, seizures, myoclonus, stroke-like episodes, headache or visual change.** It can relapse and remit, and is easily mistaken for viral encephalitis, prion disease or vasculitis."),
    ('c', "**CSF protein high, EEG diffusely slow, MRI often non-specific; a diagnosis of exclusion.** CSF protein is raised in many but not all cases, and the EEG is abnormal in almost all, though not specifically. Infection, other autoimmune encephalitides, prion disease and metabolic causes must be ruled out first."),
    ('d', "**High-dose steroids (methylprednisolone 1 g/day for 3–5 days, then taper); the response is the confirmation.** Reported regimens use 1 g a day IV for 3–7 days, or oral prednisolone 50–150 mg a day, then a slow taper over weeks to months; relapse on stopping is common. Because no test proves the diagnosis, a clear response to steroids is what supports it."),
    ('e', "**IVIG or plasma exchange if refractory.** There are no controlled trials, so these second-line choices rest on case series."),
  ],
  mimic=[
    ("Hashimoto encephalopathy vs myxoedema coma", "SREAT: usually euthyroid, seizures and myoclonus, responds to steroids. Myxoedema coma: profoundly hypothyroid, hypothermic, slow, responds to thyroxine and hydrocortisone."),
  ],
  traps=[
    ("“Start levothyroxine” for Hashimoto’s with new headaches, visual change and high anti-TPO", "The key is corticosteroids (63% right): the encephalopathy is autoimmune and the patient is usually euthyroid."),
  ],
  decode=[
    ("Hashimoto’s, new headaches and visual disturbance, high anti-TPO: next step [DocT QBank]", "Corticosteroids."),
  ],
  punch="Encephalopathy with high anti-TPO and normal thyroid function is SREAT: exclude other causes and give high-dose steroids, not thyroxine.",
)

FLAGS = {}
FLAGS['T_2b8a9a37'] = "Line a says critical illness cuts type 1 AND type 2 deiodinase; the firm changes are type 1 down and type 3 up, while type 2 changes are inconsistent (raised in some tissues). Line d ‘TSH can overshoot to 10–20’: sources say transiently above normal and usually below 20; no fixed range."
FLAGS['T_38ffd8d5'] = "Line a ‘usually EUTHYROID’ is overstated: in reported series most patients have subclinical or overt hypothyroidism, and about a third are euthyroid; the point is that the encephalopathy does not track thyroid function. Line d ‘3–5 days’: reported regimens run 3–7 days."
