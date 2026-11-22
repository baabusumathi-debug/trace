# ENDO02A top-up cards — Explain v3 ("Learn" depth), same fields and voice as endo02a_learn.py.
# Fields: sub, step (index into endo02a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions read from doct_gt_distinct_all.jsonl (the top-ups' src: GT2 Q77, GT4 Q41, AIM1 Q65, GT6 Q44, GT7 Q114, GT1o Q30), with cohort %.
# Second check 22 Nov 2026: Endocrine Society 2009 hypoglycaemia guideline read online (JCEM 2009;94:709; glucose <55, insulin ≥3 µU/mL, C-peptide ≥0.6 ng/mL,
# proinsulin ≥5 pmol/L, β-hydroxybutyrate ≤2.7 mmol/L, glucose rise ≥25 mg/dL after 1 mg IV glucagon; NICTH from pro-IGF-II with insulin suppressed);
# ADA Standards 2024 Section 16 read online (SGLT2 inhibitors stopped 3–4 days before surgery, citing FDA: 3 days, ertugliflozin 4). From memory: FDA 2016 metformin labelling by eGFR; ACR contrast manual;
# FDA 2020 SGLT2 inhibitor peri-operative labelling (3 days, ertugliflozin 4); UKPDS and its 10-year follow-up; SCCM 2024 for IV insulin in the ICU (read online).
T = {}

T['T_d6d166b0'] = dict(
  sub="Endocrine → Hypoglycaemia → Insulin, C-peptide and the sulfonylurea screen",
  step=6,
  intro="Step 6 is about hypoglycaemia, and when it happens in someone without diabetes the question becomes why. Insulin and C-peptide are made together from proinsulin, so measuring both during the low tells endogenous insulin from injected insulin; a sulfonylurea screen and the IGF profile settle the rest. Five DocT Grand Test questions draw on this table; the exogenous-insulin stem appears three times and is answered well, while the non-islet tumour ‘all except’ item (53%) is where marks are lost.",
  parts=[
    ('a', "**Exogenous insulin: insulin high, C-peptide low or undetectable, sulfonylurea screen negative.** Commercial insulin carries no C-peptide, and the high insulin suppresses the patient’s own beta cells, so C-peptide falls. This is the pattern of factitious or malicious insulin administration."),
    ('b', "**Sulfonylurea: insulin high, C-peptide high, screen positive.** The drug closes beta-cell potassium channels and releases endogenous insulin, so both rise together, exactly as in an insulinoma; only the drug screen separates them. Octreotide treats it (GLY-21)."),
    ('c', "**Insulinoma: insulin high, C-peptide high, screen negative.** Autonomous secretion continues despite the low glucose. Proinsulin is typically high as well, because the tumour releases incompletely processed hormone."),
    ('d', "**Non-islet cell tumour hypoglycaemia: large mesenchymal tumours secrete big pro-IGF2, so insulin, C-peptide, proinsulin and β-hydroxybutyrate are all suppressed, with an IGF2:IGF1 ratio above 10.** IGF2 acts on the insulin receptor, so it lowers glucose and suppresses ketogenesis while the patient’s own insulin is switched off. Low ketones with low insulin is the clue that an insulin-like factor other than insulin is acting."),
    ('e', "**Draw the critical sample during the low (glucose below 55): insulin, C-peptide, proinsulin, β-hydroxybutyrate and a sulfonylurea screen, then treat. It works because C-peptide is cleaved 1:1 from endogenous proinsulin, while injected insulin carries none.** After dextrose the evidence is gone, so the sample is taken first and dextrose given immediately after. The Endocrine Society 2009 criteria for endogenous hyperinsulinism at a glucose below 55 are insulin 3 µU/mL or more, C-peptide 0.6 ng/mL or more and proinsulin 5 pmol/L or more, with β-hydroxybutyrate 2.7 mmol/L or less. In all three insulin-driven causes β-hydroxybutyrate is low, because insulin suppresses ketogenesis; a high β-hydroxybutyrate points away from insulin to starvation, alcohol or adrenal failure."),
  ],
  table=dict(title="Reading the critical sample", head=["Cause", "Insulin", "C-peptide", "Sulfonylurea screen", "β-hydroxybutyrate"], rows=[["**Exogenous insulin**", "high", "**low**", "negative", "low"], ["**Sulfonylurea**", "high", "high", "**positive**", "low"], ["**Insulinoma**", "high", "high", "negative", "low"], ["**Non-islet tumour (IGF2)**", "**low**", "**low**", "negative", "low"], ["Starvation, alcohol, adrenal failure", "low", "low", "negative", "**high**"]]),
  mimic=[
    ("Sulfonylurea vs insulinoma", "Identical insulin and C-peptide; only the sulfonylurea screen separates them."),
    ("Exogenous insulin vs non-islet tumour", "Both have low C-peptide; insulin is high with injection and low with IGF2."),
  ],
  traps=[
    ("“High insulin and high C-peptide prove an insulinoma”", "A sulfonylurea gives the same picture; the screen must be negative."),
    ("“Low C-peptide means no hyperinsulinism”", "Low C-peptide with high insulin means the insulin came from a syringe."),
    ("“Check the bloods after correcting the glucose”", "The diagnostic window is during the low; afterwards insulin and C-peptide are uninterpretable."),
    ("“Non-islet tumour hypoglycaemia raises serum insulin”", "The exception in the GT7 item (53% right): IGF2 lowers glucose, so the patient’s own insulin is appropriately suppressed."),
  ],
  decode=[
    ("Not diabetic, glucose 42, insulin high, C-peptide undetectable, sulfonylurea screen negative [DocT GT ×3: GT2, GT4, AIM1]", "Exogenous insulin (81%, 80%, 64%)."),
    ("Conscious, tremor, sweating, palpitations, GRBS 52 — next step of investigation [DocT GT6]", "Insulin and C-peptide levels (67%), drawn during the low, with glucose given straight after."),
    ("Biochemical changes in non-islet cell tumour hypoglycaemia, all EXCEPT [DocT GT7]", "Increased serum insulin during hypoglycaemia (53%): insulin is suppressed; free IGF2 and the IGF2:IGF1 ratio rise and GH is suppressed."),
  ],
  punch="Insulin with C-peptide means the patient’s own beta cells, sulfonylurea or insulinoma, told apart by the drug screen; insulin without C-peptide means injected insulin; and low insulin, low C-peptide and low ketones mean IGF2 from a large tumour.",
)

T['T_a674f960'] = dict(
  sub="Endocrine → ICU glucose control → Oral diabetes drugs in the ICU",
  step=4,
  intro="Step 4 ends with a protocolised IV insulin infusion, and this top-up explains why the patient’s own tablets are stopped first. Each class has an ICU-specific harm: lactic acidosis, euglycaemic DKA, prolonged hypoglycaemia or delayed gastric emptying. The one linked GT question asks for the false statement, and only 29% spotted the outdated metformin cut-off.",
  parts=[
    ('a', "**Metformin: full dose at eGFR 45 or above, reduce at 30–44, stop below 30 (the old eGFR below 60 cut-off is outdated). Hold it in shock, hypoxia or sepsis because of lactic acidosis, and around contrast if eGFR is below 30 or there is AKI.** Metformin inhibits hepatic gluconeogenesis from lactate and is cleared unchanged by the kidney, so poor perfusion, hypoxia and falling GFR combine to raise lactate. The 2016 FDA change moved the limit from creatinine to eGFR."),
    ('b', "**SGLT2 inhibitors: volume depletion, AKI and euglycaemic DKA; stop about 3 days before surgery.** They lower glucose by glycosuria, so a patient who stops eating, with less insulin, makes ketones while glucose stays near normal; the DKA is missed because the glucose looks reassuring. The FDA labelling says 3 days for canagliflozin, dapagliflozin and empagliflozin and 4 for ertugliflozin, which is why ADA writes 3–4 days."),
    ('c', "**Sulfonylureas: prolonged, recurrent hypoglycaemia; octreotide treats the overdose. They cut microvascular complications, with weak macrovascular benefit (a late UKPDS legacy effect).** They release insulin whatever the glucose, their effect outlasts their half-life in kidney failure, and dextrose alone provokes more insulin release (GLY-21)."),
    ('d', "**GLP-1 agonists and DPP-4 inhibitors: reported pancreatitis; GLP-1 agonists also delay gastric emptying, which matters for aspiration risk.** Retained gastric contents are found even after a normal fast, which is why anaesthetic guidance addresses them before elective procedures."),
    ('e', "**In the ICU all are stopped and replaced by an IV insulin protocol.** Unpredictable absorption, changing renal and hepatic function, interrupted feeding and the class harms above make oral agents unsafe; SCCM 2024 suggests continuous IV insulin in critically ill adults (GLY-12)."),
  ],
  mimic=[
    ("Euglycaemic DKA vs starvation ketosis", "Both have ketones with near-normal glucose; euglycaemic DKA has a high anion gap acidosis and follows an SGLT2 inhibitor."),
    ("Metformin lactic acidosis vs septic hyperlactataemia", "Metformin: very high lactate with kidney failure and a history of the drug, often with modest shock. Sepsis: lactate follows the shock."),
  ],
  traps=[
    ("“Stop metformin if eGFR is below 60”", "Outdated since the 2016 FDA change; stop below 30, reduce at 30–44. This is the false statement in GT1o, which only 29% found."),
    ("“Sulfonylureas reduce only microvascular complications” (picking option C as the false one)", "DocT treats ‘reduce both microvascular and macrovascular complications’ as true, on the long-term UKPDS follow-up; the macrovascular effect is late and modest, but the statement is not the false one."),
    ("“Normal glucose excludes DKA”", "Not on an SGLT2 inhibitor; check ketones and the anion gap."),
  ],
  decode=[
    ("Statements about drugs for type 2 diabetes — which is FALSE [DocT GT1o]", "‘Metformin is contraindicated below eGFR 60’ (29% right); the limit is 30."),
    ("[pattern] Post-operative patient on empagliflozin, glucose 160, pH 7.15, ketones high", "Euglycaemic DKA."),
  ],
  punch="Metformin risks lactic acidosis below eGFR 30 and in shock, SGLT2 inhibitors cause euglycaemic DKA, sulfonylureas cause prolonged hypoglycaemia that needs octreotide, GLP-1 agonists slow the stomach, and in the ICU all are replaced by an IV insulin protocol.",
)

FLAGS = {}
FLAGS['T_a674f960'] = "Line a ‘hold around contrast if eGFR <30 or AKI’ matches the ACR manual; FDA labelling also advises stopping at the time of contrast for eGFR 30–60, liver disease, alcoholism, heart failure or intra-arterial contrast. Line c ‘weak macrovascular benefit (late UKPDS legacy effect)’ is fair: the 10-year follow-up showed fewer MIs and deaths."
