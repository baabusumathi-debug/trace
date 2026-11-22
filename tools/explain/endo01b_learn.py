# ENDO01B — Explain v3 ("Learn" depth): adrenal insufficiency (primary vs secondary, crisis, diagnosis, treatment, CIRCI), pituitary apoplexy and Sheehan’s syndrome,
# diabetes insipidus (types and causes, diagnosis in ICU, treatment), true/false sweep. No mnemonics or hooks.
# Driven by qpack/ENDO01B.md (57 question links; ENDO-20 DI causes asked 12 times, ENDO-21 DI diagnosis 10, ENDO-14 primary vs secondary 7, ENDO-16 and ENDO-18 six each).
# ENDO-23 (sweep) has no linked question and gets a short explanation with a [pattern] decode item.
# Card layer (endo_cardlayer.json, ENDO01B|…) lines, cross notes and fix entries (ENDO-20 sarcoid, ENDO-22 lithium/amiloride; same in trace/test/data/qbank.json) were read and used.
# Checked online on 22 Nov 2026:
#  - Endocrine Society PAI guideline 2016 (Bornstein, JCEM; endocrine.org full guideline page): cosyntropin 250 µg IV, cortisol at 30 or 60 min, peak <500 nmol/L (18 µg/dL) = adrenal
#    insufficiency (assay dependent); 1 µg test only if 250 µg is short; morning cortisol <140 nmol/L (5 µg/dL) with ACTH as a preliminary test if stimulation is not feasible; ACTH >2× upper limit
#    in confirmed cortisol deficiency = primary; crisis: hydrocortisone 100 mg IV/IM at once, fluid resuscitation, then 200 mg/24 h by infusion or 6-hourly; treat before results;
#    prednisolone is the alternative, dexamethasone least preferred; fludrocortisone 50–100 µg.
#  - SCCM/ESICM CIRCI guideline 2017 (Annane, Intensive Care Med; Springer full text): no single reliable test; delta cortisol <9 µg/dL at 60 min after 250 µg cosyntropin, or random cortisol
#    <10 µg/dL, ‘may be used’; no recommendation between them; suggest against free cortisol; 250 µg over 1 µg; septic shock not responsive to fluid and moderate–high vasopressor
#    (>0.1 µg/kg/min noradrenaline): IV hydrocortisone <400 mg/day for ≥3 days at full dose; early moderate–severe ARDS methylprednisolone 1 mg/kg/day.
#  - SCCM 2024 focused update (sccm.org page): septic shock — suggest corticosteroids (conditional, low certainty); recommend against high-dose/short course (>400 mg/day for <3 days;
#    strong, moderate); ARDS — suggest (conditional, moderate); severe bacterial CAP — recommend (strong, moderate).
#  - Surviving Sepsis 2026 (sccm.org page): adults with septic shock — suggest IV corticosteroids (conditional, low); dose not stated on the page.
#  - Society for Endocrinology UK pituitary apoplexy guideline 2011 (Rajasekaran, endocrinology.org PDF) and SfE emergency guidance 2016 (White Rose PDF): urgent MRI confirms in >90%,
#    CT conclusive in 21–28%; acute secondary adrenal insufficiency in about two-thirds, ~80% deficient in ≥1 pituitary hormone; hydrocortisone 100–200 mg IV bolus then 2–4 mg/h infusion,
#    or 100 mg IM then 50–100 mg IM 6-hourly; empirical steroid if haemodynamically unstable, altered consciousness, reduced acuity or severe field defect; surgery for severely reduced acuity,
#    severe persistent field defect or deteriorating consciousness, better visual outcome within 8 days; precipitants: hypertension, major surgery (especially CABG), dynamic pituitary testing,
#    anticoagulation, coagulopathy, pregnancy, head trauma.
#  - AVP deficiency/resistance review (Rev Endocr Metab Disord 2023, Springer): renaming of central and nephrogenic DI to AVP-D and AVP-R (2022 working group); baseline copeptin ≥21.4 pmol/L
#    = AVP-R without stimulation; hypertonic saline to Na ≥149–150 with copeptin cut-off 4.9 pmol/L, 97% accuracy; arginine 0.5 g/kg, 3.8 pmol/L at 60 min, 93%; water deprivation test 70–77%;
#    hyponatraemia on desmopressin 17% with a planned ‘escape’ vs 26–32% without.
# Second-reviewer checks on 22 Nov 2026: SSC 2026 exists (Crit Care Med, published 23 Mar 2026; sccm.org guideline page + Guideline Central/UMEM summaries): ‘suggest IV corticosteroids’ in septic shock,
#    conditional, certainty downgraded from moderate to low; no dose, threshold or fludrocortisone on any summary page. SSC 2021 rationale (secondary summary): hydrocortisone 200 mg/day once
#    noradrenaline/adrenaline ≥0.25 µg/kg/min for ≥4 h. ADRENAL (NEJM 2018 full text): 90-day mortality 27.9 vs 28.8%, OR 0.95; shock reversal 3 vs 4 days; first ventilation 6 vs 7 days;
#    transfusion 37.0 vs 41.7%. APROCCHSS (NEJM Journal Watch): 43 vs 49%. Endocrine Society PAI 2016 (Würzburg full-text PDF): 1000 mL isotonic saline within the first hour; hydrocortisone 100 mg IV
#    then 200 mg/24 h, reduced to 100 mg/day the next day; autoimmunity up to 90% in Western countries; no mineralocorticoid needed above 50 mg/24 h; maintenance 15–25 mg/day.
#    Association of Anaesthetists 2020 (Woodcock, Anaesthesia; Oxford ORA full text, Table 2): cover if prednisolone-equivalent ≥5 mg for ≥4 weeks; major AND body-surface/intermediate surgery:
#    100 mg IV at induction then 200 mg/24 h (or dexamethasone 6–8 mg IV for 24 h); major: double oral dose for 48 h if uncomplicated, up to a week otherwise; bowel preparation: usual dose; single-dose
#    etomidate: ‘clinical judgement’. Vinclair 2008 (Intensive Care Med): adrenal insufficiency after one etomidate dose in 80% at 12 h, 9% at 48 h, 7% at 72 h — reversible by 48 h.
# Blocked or unreadable on 22 Nov 2026: PMC4880116 (Endocrine Society guideline full text) and PubMed (reCAPTCHA); Endotext NBK279073 (DI) fetch was refused.
# From standard references without a fresh check by the writer (confident unless said; trials, SSC 2021, AoA 2020, etomidate, saline and autoimmune share since checked — see above): autoimmune adrenalitis 80–90% of primary AI in high-income countries; APROCCHSS (NEJM 2018: 90-day mortality 43.0 vs
# 49.1%); ADRENAL (NEJM 2018: 27.9 vs 28.8%, NS, faster shock reversal); SSC 2021 hydrocortisone 200 mg/day when noradrenaline/adrenaline ≥0.25 µg/kg/min for ≥4 h; Association of Anaesthetists
# 2020 peri-operative steroid cover (100 mg at induction, 200 mg/24 h while nil by mouth, prednisolone ≥5 mg for >4 weeks); etomidate 11β-hydroxylase block (duration quoted 6–48 h to 24–72 h;
# studies show recovery by about 72 h — less sure of the exact window); fludrocortisone unnecessary while hydrocortisone >50 mg/day; ~1 L saline in the first hour of crisis;
# water deprivation reading bands (from the card-layer lines); lithium ENaC/GSK-3β/AQP2 mechanism; vasopressinase spares desmopressin; hypernatraemia correction ≤10–12 mmol/L per day if chronic.

SPINE = [
  ("Where the adrenal axis fails", "Primary failure loses cortisol and aldosterone with a high ACTH, secondary failure loses only cortisol because aldosterone runs on renin and potassium, and CIRCI is a normal axis that cannot meet the stress."),
  ("Recognising and treating crisis", "Shock that ignores fluids and pressors, with low sodium and glucose in someone whose axis may be down, gets hydrocortisone 100 mg IV at once and 200 mg a day, before any test result."),
  ("Testing, and the critically ill", "The short Synacthen test measures adrenal reserve; in septic shock a rise under 9 µg/dL or a random cortisol under 10 µg/dL suggests CIRCI, but the decision to give steroids is clinical."),
  ("Pituitary apoplexy and Sheehan’s", "Bleeding or infarction in the pituitary gives thunderclap headache, eye signs and sudden ACTH deficiency; steroids go in before the MRI result, and Sheehan’s is the same loss in a normal postpartum gland."),
  ("Diabetes insipidus: cause and proof", "Polyuria of dilute urine with a high serum sodium is DI; desmopressin raising urine osmolality makes it central (AVP deficiency), no change makes it nephrogenic (AVP resistance)."),
  ("Treating DI safely", "Central DI is treated with desmopressin and free water while watching for hyponatraemia; nephrogenic DI with thiazide, amiloride (first for lithium) or an NSAID, and the cause removed."),
]

PRIMER = "Cortisol is made in the zona fasciculata under ACTH; aldosterone is made in the zona glomerulosa under angiotensin II and potassium, so it survives when ACTH is lost. ACTH is cut from the larger POMC precursor, which also yields melanocyte-stimulating peptides, so a high ACTH darkens the skin. Cortisol is needed to keep vascular tone (it permits catecholamines to act) and to excrete free water, which is why its lack causes refractory hypotension and hyponatraemia. Vasopressin (ADH) is made in the hypothalamus, stored in the posterior pituitary and acts on V2 receptors in the collecting duct to insert aquaporin-2 channels; without it, or without a response to it, the urine stays dilute whatever the plasma osmolality."

L = {}

L['ENDO-14'] = dict(
  sub="Endocrine → Adrenal insufficiency → Primary vs secondary",
  step=1,
  intro="The deck starts by asking where the axis has broken, because the level of failure decides the sodium and potassium, the skin, and what has to be replaced. Seven questions test the same idea: which hormones fall at each level, and which one stays normal.",
  parts=[
    ('a', "**ACTH: high in primary, low in secondary.** In primary disease the gland cannot make cortisol, so the loss of negative feedback drives ACTH up (the Endocrine Society treats an ACTH over twice the upper limit, with low cortisol, as primary). In secondary disease the pituitary (or hypothalamus) is the lesion, so ACTH is low or inappropriately normal."),
    ('b', "**Cortisol: low in both.** That is why the shared features — hypotension, hypoglycaemia, eosinophilia, hyponatraemia, fatigue, vomiting — cannot tell the two apart."),
    ('c', "**Aldosterone: low in primary (high K, low Na); spared in secondary (Na, K normal).** Primary disease destroys the whole cortex, the zona glomerulosa included, so sodium is lost and potassium and hydrogen ions are retained, and renin rises. In secondary disease the zona glomerulosa still answers to angiotensin II and potassium, so aldosterone, renin and potassium stay normal. Sodium can still fall in secondary disease: without cortisol, ADH is not suppressed and free water is retained (FLAG)."),
    ('d', "**Skin: hyperpigmented in primary (ACTH); not pigmented in secondary.** The high ACTH and its POMC fragments stimulate melanocortin-1 receptors on melanocytes; look in the palmar creases, buccal mucosa, gums and scars. Secondary disease, with a low ACTH, often shows pallor instead."),
    ('e', "**Replace cortisol plus mineralocorticoid in primary; cortisol only in secondary.** Primary disease needs fludrocortisone (50–100 µg a day) as well as hydrocortisone; in secondary disease the zona glomerulosa still works."),
  ],
  table=dict(title="What the stem gives away", head=["Finding", "Primary", "Secondary"], rows=[["High K, hyperchloraemic acidosis", "**yes**", "no (K normal)"], ["Pigmentation", "**yes**", "no"], ["Low Na, low glucose, eosinophilia", "yes", "yes"], ["Other pituitary hormones low (TSH, LH/FSH, prolactin)", "no", "**yes**"], ["Autoimmune thyroid or type 1 diabetes alongside", "**yes** (polyglandular type 2)", "no"]]),
  mimic=[
    ("Primary vs secondary in a hyponatraemic patient", "Potassium and skin decide: hyperkalaemia and pigmentation mean primary; normal potassium, pallor and other pituitary losses mean secondary."),
    ("Secondary vs tertiary (steroid withdrawal)", "Long-term glucocorticoids suppress CRH and ACTH; the picture is that of secondary disease, with aldosterone spared and potassium normal."),
  ],
  traps=[
    ("“Chronic corticosteroid use is the commonest cause of primary adrenal insufficiency” (53% right)", "It is the commonest cause of adrenal insufficiency overall, but it is secondary (HPA suppression); the commonest cause of primary disease is autoimmune adrenalitis, 80–90% in high-income countries, with tuberculosis still important in India."),
    ("“In secondary adrenal insufficiency cortisol or ACTH is normal” (46% right)", "Both are low; aldosterone is the hormone that stays normal. Renin (option D) is also normal in secondary disease, because it rises only when aldosterone fails, but the intended answer is aldosterone."),
    ("Sheehan’s stem with K 5.8 — “aldosterone must be low” (46% right)", "The TRH test shows a pituitary lesion, so aldosterone is normal; the potassium comes from the AKI and volume depletion (creatinine 1.6). Cortisol and FSH are low; GnRH is a hypothalamic hormone that is not measured and would, if anything, rise."),
    ("“Hyponatraemia, hypoglycaemia or a low cortisol confirms primary disease” (59% right)", "All three occur in both; pigmentation (or hyperkalaemia) separates primary from central."),
  ],
  decode=[
    ("Hypotension, Na 128, K 5.8, failed lactation and cold intolerance after a severe PPH — which hormone is normal? [DocT GT]", "Aldosterone: Sheehan’s is pituitary failure, and the zona glomerulosa runs on renin."),
    ("Vomiting, hypotension, hyponatraemia, hyperkalaemia, eosinophilia — what confirms primary rather than central? [DocT GT]", "Skin hyperpigmentation."),
    ("Most common cause of primary adrenal insufficiency? [DocT QBank]", "Autoimmune adrenalitis."),
    ("Pigmented, postural drop, Na 120, K 6, worse after starting thyroxine [Marrow]", "Addison’s disease in crisis: thyroxine speeds cortisol clearance, so steroid must come before thyroxine."),
  ],
  punch="Potassium and skin locate the lesion: hyperkalaemia and pigmentation mean the adrenal itself has failed and needs fludrocortisone too, while a normal potassium means the pituitary has failed and aldosterone, run by renin, is spared.",
)

L['ENDO-15'] = dict(
  sub="Endocrine → Adrenal insufficiency → Acute adrenal crisis",
  step=2,
  intro="Step 2 is the emergency: the patient whose axis cannot meet a sudden demand. The questions test the profile that points to crisis and the patient who is still taking steroids but not enough for the illness.",
  parts=[
    ('a', "**Refractory hypotension (shock not responding to fluids or pressors), abdominal cramps, vomiting, diarrhoea, anorexia, confusion.** Cortisol is needed for vascular smooth muscle to respond to catecholamines (it maintains adrenergic receptors and vascular tone), so without it pressors work poorly; aldosterone loss in primary disease adds salt and water depletion. The abdominal pain can mimic an acute abdomen."),
    ('b', "**Hyponatraemia, hyperkalaemia, hypoglycaemia, metabolic acidosis.** Sodium falls from aldosterone loss (primary) and ADH excess (both); potassium and acid are retained without aldosterone; glucose falls without cortisol’s gluconeogenic drive. Prerenal uraemia, eosinophilia and mild hypercalcaemia may also appear."),
    ('c', "**Secondary (steroid withdrawal): potassium is usually normal.** Aldosterone is intact, so a crisis after stopping long-term steroids shows low sodium and glucose with a normal potassium. A patient still taking chronic steroids (prednisolone ≥5 mg a day) who develops sepsis or needs surgery is in the same position: the suppressed axis cannot add the extra cortisol the illness demands, so stress-dose hydrocortisone is needed even without withdrawal (FLAG)."),
  ],
  mimic=[
    ("Adrenal crisis vs septic shock", "Both are vasodilated shock; crisis is suggested by a history of steroid use or autoimmune disease, hyponatraemia with hyperkalaemia, hypoglycaemia, and a poor response to pressors. They often coexist: sepsis is the commonest trigger."),
    ("Adrenal crisis vs acute abdomen", "Crisis gives pain and vomiting with a soft abdomen, low sodium and low glucose."),
  ],
  traps=[
    ("“Hypotension that responds to fluid resuscitation” (77% right)", "Crisis is defined by hypotension that does not respond to fluids; hyponatraemia with hyperkalaemia is the profile."),
    ("Chronic prednisone, urosepsis, CVP 20 — more fluid or a pressor alone [Marrow]", "The CVP shows the patient is already filled; the missing piece is stress-dose hydrocortisone."),
  ],
  decode=[
    ("Young woman with type 1 diabetes and thyroid disease, lethargic and hypotensive — which profile fits adrenal insufficiency? [DocT GT]", "Refractory hyponatraemia and hyperkalaemia: polyglandular syndrome type 2 with primary failure."),
    ("Rheumatoid patient on chronic prednisone, urosepsis, hypotensive despite a CVP of 20 [Marrow]", "IV hydrocortisone."),
  ],
  punch="Shock that ignores fluids and pressors, with low sodium and low glucose, in someone with autoimmune disease or on steroids is adrenal crisis; potassium is high only when the adrenal itself has failed.",
)

L['ENDO-16'] = dict(
  sub="Endocrine → Adrenal insufficiency → Diagnosis",
  step=3,
  intro="Step 3 is proving it, and the problem is that the critically ill patient breaks the usual rules. Six questions test what the Synacthen test measures, the CIRCI cut-offs, and the rule that treatment never waits for the result — and two of the keys are disputed.",
  parts=[
    ('a', "**A random cortisol over 20 µg/dL excludes it (your notes).** Outside critical illness this is safe: a cortisol at that level in a stressed patient shows the gland can respond. The Endocrine Society uses a morning cortisol under 5 µg/dL (140 nmol/L), with ACTH, as a preliminary pointer when stimulation cannot be done. In septic shock a ‘normal’ level does not exclude CIRCI, because tissue resistance and low binding protein mean a level that looks adequate may be too little for the illness (FLAG)."),
    ('b', "**Short Synacthen test: 250 µg ACTH IV; cortisol at 0, 30 and 60 min.** Synthetic ACTH (cosyntropin, tetracosactide) tests whether the adrenal cortex can respond, that is, its reserve; it does not measure ACTH. For primary disease the Endocrine Society calls a peak under 18 µg/dL (500 nmol/L) at 30 or 60 min diagnostic (assay dependent). In recent secondary disease the test can be falsely normal, because the adrenal has not yet atrophied."),
    ('c', "**CIRCI likely if the rise is under 9 µg/dL or a random cortisol is under 10 µg/dL (SCCM/ESICM 2017).** The task force could not agree on one reliable test and made no recommendation between the two; it advised against free cortisol and for the 250 µg rather than the 1 µg test. The criterion is the increment: any rise under 9 µg/dL qualifies, whatever the baseline. Since then the SCCM 2024 update and Surviving Sepsis 2021 (ongoing vasopressor need) and 2026 (a conditional suggestion for IV corticosteroids in septic shock, low certainty) decide on steroids by the clinical picture of shock, not by a cortisol level."),
    ('d', "**Never delay treatment for testing.** If there is time, draw a cortisol and ACTH before the first dose; hydrocortisone then goes in at once, because it is measured in the cortisol assay and would spoil a later test, and the Synacthen test can be done after recovery."),
  ],
  mimic=[
    ("Absolute (structural) insufficiency vs CIRCI", "Absolute: autoimmune destruction, haemorrhage, pituitary tumour — the gland or pituitary is damaged. CIRCI: functional — a dysregulated axis, altered cortisol metabolism and tissue resistance, with no structural lesion."),
    ("Flat Synacthen in a long-term steroid user: CIRCI vs secondary", "The test cannot tell them apart; atrophy after HPA suppression gives the same flat rise. The treatment is the same (hydrocortisone 200 mg/day)."),
  ],
  traps=[
    ("“Relative adrenal insufficiency is autoimmune destruction of the adrenal cortex” (GrandT1 keys this; 9% right)", "The key is wrong; the GT2 repeat keys correctly. CIRCI is cortisol inadequate for the stress demand, with no structural cause. Exam answer: inadequate cortisol for stress demands."),
    ("“Only a high baseline with a low rise is CIRCI; a normal baseline with no rise is not” (28% right)", "Any rise under 9 µg/dL meets the 2017 criterion, so B is as correct as the keyed C; C is chosen because it is Annane’s classic non-responder (baseline >34 µg/dL, rise ≤9, highest mortality). If asked which response is CIRCI, any delta under 9 qualifies."),
    ("Long-term steroid user, rise of 5 µg/dL — “secondary adrenal insufficiency” (45% right; keyed relative AI)", "In this patient secondary insufficiency is at least as likely; the key wants the critical-illness label. Treatment is identical."),
    ("“The cosyntropin test assesses ACTH levels” (58% right)", "It tests the adrenal gland’s response to ACTH."),
    ("Septic shock, which cortisol supports hydrocortisone — “20 µg/dL” (57% right)", "The 2017 random cut-off is under 10 µg/dL, so 10 is the answer; current sepsis guidance no longer uses a level to decide."),
  ],
  decode=[
    ("Septic shock unresponsive to fluids and pressors with a normal cortisol — what is relative adrenal insufficiency? [DocT GT]", "Cortisol inadequate for the stress demand (no structural lesion)."),
    ("Which Synacthen pattern supports CIRCI? [DocT QBank]", "A rise under 9 µg/dL; the key picks high baseline with low rise."),
    ("Woman with APS-1 (candidiasis, pigmentation) in crisis — next step? [Marrow]", "Stress-dose hydrocortisone now; test later."),
  ],
  punch="The Synacthen test measures adrenal reserve and a rise under 9 µg/dL suggests CIRCI whatever the baseline, but in a patient in shock the cortisol is drawn, the hydrocortisone is given, and the test comes later.",
)

L['ENDO-17'] = dict(
  sub="Endocrine → Adrenal insufficiency → Treating adrenal crisis",
  step=2,
  intro="Back to the emergency in step 2: what to give, how much, and when. The same doses cover surgery in a patient whose axis is suppressed, and etomidate creates a short crisis of its own; five questions test those three settings.",
  parts=[
    ('a', "**Hydrocortisone IV now: 100 mg bolus, then 200 mg/day (infusion or 50 mg 6-hourly).** These are the Endocrine Society doses. Hydrocortisone is cortisol itself, so it acts on both glucocorticoid and mineralocorticoid receptors; dexamethasone has no mineralocorticoid action and is the least preferred choice, used only if nothing else is available (prednisolone is the alternative)."),
    ('b', "**Fluid resuscitation: saline, with dextrose for hypoglycaemia.** The Endocrine Society gives 1000 mL of isotonic saline within the first hour, then more by response; saline replaces the salt lost without aldosterone and corrects the hyponatraemia, and dextrose treats the low glucose."),
    ('c', "**Mineralocorticoid (fludrocortisone) for primary disease.** It is started once the hydrocortisone dose falls, because at 200 mg a day hydrocortisone saturates the mineralocorticoid receptor; below about 50 mg a day primary disease needs fludrocortisone 50–100 µg."),
    ('d', "**Treat the trigger; taper to maintenance.** Infection is the commonest trigger. The Endocrine Society reduces the dose to 100 mg the next day, then tapers to the oral maintenance dose (hydrocortisone 15–25 mg a day in two or three doses) once the patient is eating and stable; the precipitant, not the hormone, usually decides how long that takes."),
  ],
  table=dict(title="Same drug, different settings", head=["Setting", "Hydrocortisone"], rows=[["Adrenal crisis", "**100 mg IV now**, then 200 mg/24 h"], ["Major surgery, Addison’s or prednisolone ≥5 mg for >4 weeks", "**100 mg IV at induction**, 200 mg/24 h while nil by mouth, then double the oral dose for 48 h (Association of Anaesthetists 2020)"], ["Body-surface or intermediate surgery", "the same **100 mg IV at induction** and 200 mg/24 h (or dexamethasone 6–8 mg IV), then double the oral dose for 48 h (2020); the older ‘single 25–50 mg’ is pre-2020 teaching"], ["Bowel preparation", "usual dose (IV equivalent if nil by mouth for long)"], ["Pressor-refractory shock after etomidate", "**100 mg IV**"]]),
  mimic=[
    ("Induction bolus vs daily total", "100 mg is the bolus at induction or in crisis; 200 mg is the 24-hour total."),
  ],
  traps=[
    ("“Fludrocortisone or dexamethasone first” (79% right)", "Hydrocortisone first: it gives both actions at stress doses; fludrocortisone alone gives no glucocorticoid, dexamethasone no mineralocorticoid."),
    ("Prednisone 10 mg for a year, major surgery — “200 mg hydrocortisone at the start” (69% right)", "200 mg is the daily total; the induction dose is 100 mg IV. Continuing only the usual prednisone risks intra-operative crisis."),
    ("Pressor-refractory shock after an etomidate RSI — “more noradrenaline” [Marrow]", "A single dose of etomidate blocks 11β-hydroxylase, the last step from 11-deoxycortisol to cortisol, most strongly in the first 12–24 hours and largely reversed by 48 hours (80% insufficient at 12 h, 9% at 48 h in one ICU study); in that window catecholamines work poorly, so give hydrocortisone 100 mg IV."),
  ],
  decode=[
    ("Initial treatment of acute adrenal insufficiency? [DocT QBank]", "Hydrocortisone."),
    ("Addison’s patient for major surgery? [DocT QBank, 94% right]", "Stress-dose hydrocortisone."),
    ("Post-etomidate urosepsis, pressor-resistant hypotension — cause and treatment? [Marrow ×2]", "Transient adrenal suppression by etomidate; hydrocortisone 100 mg IV."),
  ],
  punch="Crisis gets hydrocortisone 100 mg IV at once and 200 mg a day with saline and dextrose; the same 100 mg covers induction in a steroid-dependent patient and the shock that follows an etomidate intubation.",
)

L['ENDO-18'] = dict(
  sub="Endocrine → Adrenal insufficiency → CIRCI",
  step=3,
  intro="Step 3 continues with the ICU version of adrenal failure: glands that are intact but not enough for the illness. Six questions ask what it is, which drugs cause it, and what the current guidance says to give.",
  parts=[
    ('a', "**Relative adrenal insufficiency: normal glands that cannot raise cortisol enough for the stress.** SCCM/ESICM define CIRCI as corticosteroid activity inadequate for the severity of illness, from three mechanisms: a dysregulated HPA axis, altered cortisol metabolism, and tissue resistance to glucocorticoid (with low binding globulin). There is no structural lesion, so the cortisol may look normal (ENDO-16)."),
    ('b', "**Sepsis; presents as vasopressor-dependent hypotension.** Also in severe CAP, ARDS, trauma, burns and after cardiac surgery. Drugs precipitate it: etomidate (blocks 11β-hydroxylase; after one dose, largely reversed by 48 hours), azoles such as ketoconazole (block steroid synthesis), and enzyme inducers — phenytoin, rifampicin, phenobarbital — that speed cortisol breakdown."),
    ('c', "**Hydrocortisone (200 mg/day in septic shock needing pressors).** SCCM/ESICM 2017: less than 400 mg a day for at least 3 days at full dose when shock does not respond to fluid and moderate–high vasopressor (over 0.1 µg/kg/min noradrenaline). Surviving Sepsis 2021: 200 mg a day (50 mg 6-hourly or by infusion) once noradrenaline or adrenaline is at least 0.25 µg/kg/min for at least 4 hours. The SCCM 2024 update suggests steroids in septic shock (conditional, low certainty) and recommends against high-dose short courses (over 400 mg a day for under 3 days); Surviving Sepsis 2026 again suggests IV corticosteroids in septic shock (conditional), with the certainty downgraded from moderate to low; its published summary gives no new dose or threshold, so the 2021 regimen stands."),
    ('d', "**Adding fludrocortisone may or may not help.** APROCCHSS (hydrocortisone 50 mg 6-hourly plus fludrocortisone 50 µg daily for 7 days) lowered 90-day mortality (43.0% vs 49.1%); ADRENAL (hydrocortisone 200 mg a day by infusion alone, 3800 patients) did not (27.9% vs 28.8%) but reversed shock sooner (3 vs 4 days), shortened the first episode of ventilation and reduced transfusion. Whether the fludrocortisone or the sicker population made the difference is not known."),
  ],
  mimic=[
    ("CIRCI vs secondary insufficiency from chronic steroids", "Both give a flat Synacthen response in a steroid user; the test cannot separate them, and both get hydrocortisone 200 mg/day."),
    ("Hydrocortisone in septic shock vs in ARDS or CAP", "Septic shock: hydrocortisone 200 mg/day. Early ARDS: methylprednisolone 1 mg/kg/day (2017). Severe bacterial CAP: steroids recommended (strong, 2024), typically hydrocortisone as in CAPE COD."),
  ],
  traps=[
    ("Etomidate, ketoconazole and phenytoin — “only etomidate” (44% right)", "All three contribute: one blocks synthesis briefly, one blocks it continuously, one speeds breakdown."),
    ("Long-term steroid user, rise of 5 µg/dL — “secondary insufficiency” (45%; keyed relative AI)", "Disputed: secondary is at least as likely in that patient. Pick the critical-illness label when the stem is about septic shock; the treatment is the same."),
    ("“Withhold steroids unless cortisol is low or adrenal disease is known”", "Current guidance decides on the vasopressor need, not on a cortisol level."),
    ("“High-dose dexamethasone” or “fludrocortisone alone”", "Hydrocortisone 200 mg/day; high-dose short courses are recommended against, and fludrocortisone alone gives no glucocorticoid."),
  ],
  decode=[
    ("Septic shock on noradrenaline 0.3 µg/kg/min for 6 hours, rising doses — steroid recommendation? [DocT GT]", "IV hydrocortisone 200 mg/day, by infusion or 50 mg 6-hourly."),
    ("Alcoholic pancreatitis, refractory shock, low cortisol despite pressors [DocT QBank 95%; DocT GT]", "Start hydrocortisone."),
    ("Which finding indicates relative adrenal insufficiency? [DocT QBank]", "Normal cortisol with a poor response to stress."),
    ("Intubated with etomidate, on ketoconazole and phenytoin, shocked at 36 h, responds to hydrocortisone [DocT GT]", "All three drugs contributed."),
  ],
  punch="CIRCI is a normal gland that cannot match the illness, with no lesion to find; septic shock that keeps needing pressors gets hydrocortisone 200 mg a day on clinical grounds, and fludrocortisone is optional.",
)

L['ENDO-19'] = dict(
  sub="Endocrine → Pituitary → Apoplexy and Sheehan’s syndrome",
  step=4,
  intro="Step 4 moves up the axis to the pituitary, where a sudden bleed removes ACTH in hours. Four questions test the precipitants, Sheehan’s syndrome and what to give first.",
  parts=[
    ('a', "**Haemorrhage or infarction of a pituitary adenoma (or a normal gland).** Usually a non-functioning macroadenoma, often not known before; the tumour outgrows its blood supply, so it bleeds or infarcts, and the swelling inside the fixed sella compresses the gland, the optic chiasm and the cavernous sinuses."),
    ('b', "**Surgery, postpartum haemorrhage, hypertension, anticoagulants, oestrogens.** The UK guidance adds major surgery (especially CABG), dynamic pituitary testing, coagulopathy, pregnancy and head trauma; diabetes mellitus and sickle cell disease also predispose through microvascular ischaemia, as do dopamine agonists. Hyperthyroidism does not."),
    ('c', "**Sheehan’s syndrome: necrosis of a normal pituitary after peripartum haemorrhage or shock.** In pregnancy the gland enlarges (lactotroph hyperplasia) without more blood supply, so hypotension infarcts it. It is an anterior pituitary loss: failure to lactate is often the first sign, then amenorrhoea, central hypothyroidism and ACTH deficiency, which become chronic. DI is rare because the posterior pituitary has a separate arterial supply."),
    ('d', "**Sudden headache, vomiting, falling consciousness (raised ICP); visual field defects, reduced acuity, ophthalmoplegia (cavernous sinus nerves); hypopituitarism.** The headache is sudden and severe, like subarachnoid haemorrhage, which it can mimic; consciousness falls from pressure, blood in the subarachnoid space and acute cortisol lack. The chiasm gives a bitemporal defect; the third nerve is the one most often hit. About two-thirds have acute secondary adrenal insufficiency and about 80% lack at least one pituitary hormone (UK 2011)."),
    ('e', "**MRI (diagnostic in over 90%); CT insensitive. Bloods: cortisol, ACTH, prolactin, FSH, LH, sex hormones, free T4, IGF-1.** CT confirms the diagnosis in only 21–28%, but a CT is still used to exclude subarachnoid haemorrhage. The bloods are drawn for later analysis; they do not delay treatment."),
    ('f', "**Supportive ICU care, hormone (steroid) replacement, surgical decompression if needed.** Hydrocortisone 100–200 mg IV, then 2–4 mg/h by infusion (or 50–100 mg IM 6-hourly), is given empirically if the patient is unstable, drowsy or has a reduced acuity or a severe field defect. Surgery is for severely reduced acuity, a severe persistent field defect or falling consciousness, ideally within 8 days; otherwise conservative care is reasonable."),
  ],
  mimic=[
    ("Pituitary apoplexy vs subarachnoid haemorrhage", "Both give a thunderclap headache and meningism; apoplexy adds a field defect, ophthalmoplegia and hypopituitarism, and MRI shows a pituitary mass."),
    ("Sheehan’s vs apoplexy with stalk involvement", "Sheehan’s: anterior loss in a normal gland after obstetric bleeding, DI rare. Apoplexy of a large tumour can reach the stalk and cause DI."),
  ],
  traps=[
    ("“Hypertension, diabetes or sickle cell disease is not associated” (39% right)", "All three predispose; hyperthyroidism is the exception."),
    ("Sheehan’s — “diabetes insipidus becomes chronic” [Marrow]", "Central hypothyroidism (and ACTH and gonadotrophin loss) becomes chronic; the posterior pituitary is usually spared."),
    ("Sheehan’s with K 5.8 — “aldosterone is low” (46% right)", "Aldosterone is normal (ENDO-14); the potassium is from AKI."),
  ],
  decode=[
    ("All are associated with pituitary apoplexy except — hyperthyroidism, DM, sickle cell, hypertension [DocT GT]", "Hyperthyroidism."),
    ("PPH, then headache, shock and hypoglycaemia — the drug that reverses it? [Marrow]", "Steroids (hydrocortisone) first."),
    ("Sheehan’s syndrome — which disorder becomes chronic? [Marrow]", "Central hypothyroidism."),
  ],
  punch="Pituitary apoplexy is a thunderclap headache with eye signs and sudden ACTH loss: hydrocortisone goes in before the MRI result, and Sheehan’s is the same anterior loss in a normal gland after obstetric bleeding, without DI.",
)

L['ENDO-20'] = dict(
  sub="Endocrine → Diabetes insipidus → Types and causes",
  step=5,
  intro="Step 5 turns to the posterior pituitary and the kidney. This is the most-asked card in the deck (12 questions): the mechanism of each type, which drugs and electrolytes cause the nephrogenic form, the triphasic response after pituitary surgery, and two disputed keys. Since 2022 central DI is also called arginine vasopressin deficiency (AVP-D) and nephrogenic DI AVP resistance (AVP-R).",
  parts=[
    ('a', "**Central: too little ADH. Causes: tumour (primary, metastatic), meningitis, encephalitis, SLE, snake venom, genetic; head injury, surgery, brain death.** ADH is made in the supraoptic and paraventricular nuclei and carried down the stalk; permanent DI needs loss of over 80–90% of these neurons, so a lesion of the posterior lobe alone often causes only transient DI. Granulomatous disease — sarcoidosis and Langerhans cell histiocytosis — infiltrates the hypothalamus and stalk and is a classic central cause. After stalk injury (transsphenoidal surgery, TBI) sodium can run a triphasic course: DI from axonal shock (days 1–5), SIADH as dying neurons release stored ADH (days 5–10; stop desmopressin, restrict water), then permanent DI. Lesions of the osmoreceptors (hypothalamic tumours, anterior communicating aneurysm clipping) cause adipsic DI: no thirst and no osmotic ADH release, while baroreceptor-driven release persists."),
    ('b', "**Nephrogenic: kidney does not respond. Causes: lithium, demeclocycline, vaptans, aminoglycosides, amphotericin, rifampicin, polymyxin; hypokalaemia, hypercalcaemia; sickle cell, ATN, obstruction, amyloid, PKD, Bartter, sarcoid.** Lithium enters collecting-duct cells through ENaC and inhibits GSK-3β, so aquaporin-2 is down-regulated; loss of the urea transporter UT-A1 also lowers medullary tonicity. Hypercalcaemia activates the calcium-sensing receptor, which reduces aquaporin-2 and the medullary gradient; hypokalaemia also reduces aquaporin-2. Foscarnet is another drug cause. Sarcoid reaches this column only through hypercalcaemia and interstitial nephritis (FLAG). Hyperkalaemia is not a cause."),
    ('c', "**Gestational: placental vasopressinase. Third trimester; reversible.** The placenta makes an aminopeptidase that destroys ADH; it is cleared by the liver, so it is worse with pre-eclampsia, HELLP or acute fatty liver. Desmopressin resists the enzyme and is the treatment."),
  ],
  mimic=[
    ("Nephrogenic DI vs osmotic diuresis", "Both give polyuria; in DI the urine is dilute (urine Na + K far below plasma, osmolality under 300), while an osmotic diuresis (glucose, urea, mannitol) has urine osmolality near or above plasma."),
    ("Sarcoid DI: central vs nephrogenic", "Central directly (granulomas in the stalk and hypothalamus); nephrogenic only indirectly, through hypercalcaemia or interstitial nephritis."),
  ],
  traps=[
    ("“Which is NOT a cause of nephrogenic DI — sarcoidosis” (30% right; disputed)", "Sarcoid causes both; the key wants its primary mechanism, central DI. On exam day: sarcoid = central DI; demeclocycline, foscarnet and hypercalcaemia are direct nephrogenic causes."),
    ("Lithium — “increases ADH secretion” or “enhances V2/aquaporin-2 action” (42% right)", "Lithium blocks the response to ADH; the keyed answer is reduced medullary tonicity (urea transporter), though aquaporin-2 down-regulation is the main mechanism. B and D invert lithium’s action."),
    ("Adipsic DI — “normal thirst” or “hypertonic saline raises ADH” (30% right; disputed stem)", "Adipsic DI has absent thirst and no ADH response to hypertonic saline. The keyed D (hypotonic saline lowers ADH) only shows that the baroreceptor arm works; the stem’s lack of response to DDAVP actually suggests nephrogenic DI."),
    ("“Hyperkalaemia causes nephrogenic DI” (62% right)", "Hypokalaemia does; hyperkalaemia is the ‘not associated’ option."),
    ("Meningitis with new polyuria and hypernatraemia — “urine studies first” (DocT GT; the explanation mislabels the options)", "Antibiotics first; the central DI is a complication to confirm later."),
  ],
  decode=[
    ("After transsphenoidal surgery, a triphasic sodium response [DocT QBank]", "Post-transsphenoidal surgery: DI, then SIADH, then permanent DI."),
    ("Head injury with acute DI — mechanism? [DocT QBank]", "Insufficient ADH synthesis and release."),
    ("Lithium, thirst, polyuria, hypernatraemia, dilute urine with a high plasma ADH [DocT GT]", "Nephrogenic DI."),
    ("CKD with mild hypercalcaemia, dilute polyuria, urine Na + K far below plasma [DocT GT]", "Nephrogenic DI."),
  ],
  punch="Central DI is a loss of ADH from the hypothalamus or stalk (head injury, pituitary surgery, sarcoid granulomas), nephrogenic DI a kidney that ignores it (lithium, low potassium, high calcium), and gestational DI an enzyme that destroys it but spares desmopressin.",
)

L['ENDO-21'] = dict(
  sub="Endocrine → Diabetes insipidus → Diagnosis in ICU",
  step=5,
  intro="Step 5 continues with proof. The ICU patient is usually already hypernatraemic, so the question is not whether he can concentrate when deprived but whether desmopressin works. Ten questions test reading the numbers, the formal deprivation test, and the hormone that hides DI.",
  parts=[
    ('a', "**Urine volume over 3 L/day; urine osmolality under 300; serum osmolality over 300; hypernatraemia, altered sensorium, unable to drink; no glycosuria.** Dilute urine at a high plasma osmolality is the core: in health, a serum osmolality of 300 would produce maximal ADH and concentrated urine. The ICU patient cannot drink to keep up, so sodium rises where an ambulant patient would stay near normal by thirst."),
    ('b', "**Desmopressin test: 1–2 µg IV (or 10 µg nasal). Central: urine osmolality rises. Nephrogenic: no change.** In complete central DI the urine osmolality rises by over 50% (often doubling); in nephrogenic DI it rises by less than 10%. The response comes within 1–2 hours, with a fall in urine volume."),
    ('c', "**The water deprivation test is not done in ICU.** The patient is already hyperosmolar, so further deprivation adds danger and no information; the desmopressin step alone answers the question. Outside ICU, deprivation then desmopressin reads: complete central stays under 300, then rises over 50%; partial central rises to 300–800, then another 10–50%; nephrogenic stays under 300 with under 10% rise; primary polydipsia concentrates to over 600–800 with no further rise."),
    ('d', "**Primary polydipsia (low sodium, low serum osmolality) and diabetic polyuria (glycosuria).** In primary polydipsia the drinking comes first, so sodium is low-normal; in DI the water loss comes first, so sodium is high-normal or high. Glycosuria and urine osmolality near plasma mark an osmotic diuresis."),
  ],
  table=dict(title="Reading the ICU numbers", head=["Pattern", "Diagnosis"], rows=[["High serum Na/osm, urine osm <300, large volume", "**DI**"], ["… and urine osm rises >50% with desmopressin", "**central DI**"], ["… and urine osm rises <10%", "**nephrogenic DI**"], ["Low Na, low serum osm, dilute urine", "primary polydipsia"], ["Urine osm ≥300, glucose or urea load", "osmotic diuresis"], ["Low Na, high urine Na, volume depleted", "cerebral salt wasting"]]),
  mimic=[
    ("Central DI vs cerebral salt wasting after brain injury", "Both have high urine output; DI raises sodium with dilute urine, salt wasting lowers sodium with concentrated, salty urine."),
    ("Central DI vs hypertonic-saline solute diuresis", "Solute diuresis has urine osmolality near or above plasma; a urine osmolality of 199 at a serum osmolality of 338 is a water diuresis — DI."),
  ],
  traps=[
    ("Drinks 8–10 L, Na 141, no concentration on deprivation, 650 after desmopressin — “primary polydipsia” (65–76% right)", "Primary polydipsia concentrates during deprivation; failure to concentrate until desmopressin is central DI. The normal sodium only shows that she can drink."),
    ("Submaximal rise on deprivation, significant rise after ADH — “complete central DI” or “nephrogenic” (48% right)", "Partial central DI: some ADH is left, so the urine concentrates a little and more with desmopressin."),
    ("TBI on hypertonic saline, Na 167, urine osm 199, urine Na 55 — “osmotic diuresis” or “cerebral salt wasting” (53% right)", "Urine more dilute than plasma at a sodium of 167 is central DI; salt wasting causes hyponatraemia."),
  ],
  decode=[
    ("After transsphenoidal surgery, 7.5 L/day, Na 150, serum osm 302, urine osm 80 [DocT GT ×3; DocT QBank]", "Central DI (77–94% right)."),
    ("Suspected central DI — which coexisting condition should be checked? [DocT QBank]", "Hypoadrenalism: cortisol lack masks DI, which may appear only once hydrocortisone starts."),
    ("Fluid deprivation: serum osm rises, urine osm does not, no rise after DDAVP [DocT GT]", "Nephrogenic DI."),
    ("Lithium, hypernatraemia, dilute urine, high plasma ADH [DocT GT]", "Nephrogenic DI."),
  ],
  extra=[
    dict(q="What has copeptin added to the diagnosis of DI?", a="Copeptin is released with ADH in equal amounts and is stable to measure. A baseline copeptin of 21.4 pmol/L or more means nephrogenic DI without any stimulation; after hypertonic saline to a sodium of about 150, a copeptin above 4.9 pmol/L separates primary polydipsia from central DI with 97% accuracy, and arginine stimulation (3.8 pmol/L at 60 min) gives 93%; the water deprivation test manages only 70–77%."),
  ],
  punch="In ICU, dilute urine at a high serum sodium is DI, and the test is desmopressin, not deprivation: a rise in urine osmolality means central, no rise means nephrogenic; check cortisol first, because its absence can hide the polyuria.",
)

L['ENDO-22'] = dict(
  sub="Endocrine → Diabetes insipidus → Treatment",
  step=6,
  intro="The last step is treatment, and both types carry their own risk: desmopressin can drown the patient in water, and the drug for the nephrogenic form works by an apparently paradoxical route. Five questions test the lithium patient, the desmopressin complication and a disputed key.",
  parts=[
    ('a', "**Central: desmopressin SC or IV 1 µg (notes; 1–2 µg standard), once or twice daily (also nasal, oral, sublingual); replace free water.** Desmopressin is a V2-selective analogue of ADH with no pressor action and a longer half-life. It gives a continuous antidiuresis, so any water taken in is retained: hyponatraemia is its commonest complication. Check sodium daily, restrict free water to need, and allow a daily ‘escape’ (delay a dose until a water diuresis starts), which lowers hyponatraemia rates. After pituitary surgery, give doses as needed rather than on a schedule, because the SIADH phase may follow."),
    ('b', "**Nephrogenic: thiazide + amiloride; indomethacin; high-dose desmopressin; stop the drug, correct K and Ca.** A thiazide causes mild volume contraction, so the proximal tubule reabsorbs more sodium and water and less reaches the collecting duct; a low-sodium diet adds to the effect. Amiloride blocks ENaC, the channel through which lithium enters the cell, so in lithium-induced DI it is the first drug and does not raise lithium levels as a thiazide does (FLAG). An NSAID removes prostaglandin E2, which opposes ADH. High-dose desmopressin helps only partial resistance. Stopping lithium often does not reverse established disease."),
    ('c', "**Correct hypernatraemia slowly.** In chronic hypernatraemia (over 48 hours) brain cells have made osmolytes, so fast correction causes cerebral oedema; aim for no more than about 10–12 mmol/L a day, with free water calculated and replaced, including ongoing urine losses."),
  ],
  mimic=[
    ("Desmopressin vs vasopressin", "Desmopressin acts on V2 (kidney, and vWF release); vasopressin acts on V1 too, so it constricts vessels and is the one used in septic shock."),
  ],
  traps=[
    ("Lithium nephrogenic DI, polyuria — “desmopressin” or “lithium withdrawal” (52% right; keyed thiazide)", "The receptor is resistant and withdrawal often fails; thiazide is the best option offered when amiloride is absent."),
    ("Lithium nephrogenic DI, initial treatment — “thiazide” (21% right; keyed amiloride)", "When amiloride is offered it is the answer: it blocks lithium’s entry. The two DocT keys conflict; amiloride is the better one."),
    ("Lithium DI — “stop lithium, start desmopressin” or “loop diuretic” (60% right)", "Thiazide with a low-sodium diet; desmopressin fails, and a loop diuretic destroys the medullary gradient."),
    ("Desmopressin risk — “hypernatraemia” (69% right)", "Hyponatraemia, from continuous antidiuresis with ongoing intake."),
    ("Post-op DI on desmopressin and co-trimoxazole, new purpura — keyed desmopressin [Marrow]", "Doubtful: desmopressin thrombocytopenia is rare and mainly in type 2B von Willebrand disease, while co-trimoxazole is a common cause of immune thrombocytopenia. Pick desmopressin only if the stem says the lesions appeared before, or names type 2B vWD."),
  ],
  decode=[
    ("Lithium, plasma osm 290, urine osm 200, Na 140 — initial treatment? [DocT QBank]", "Amiloride."),
    ("Lithium nephrogenic DI confirmed on testing — next step? [DocT GT]", "Hydrochlorothiazide and a low-sodium diet."),
    ("Central DI on desmopressin — main risk? [DocT QBank]", "Hyponatraemia."),
  ],
  punch="Central DI needs desmopressin and a daily sodium; nephrogenic DI needs the kidney’s salt handling changed — thiazide with a low-salt diet, an NSAID, and amiloride first when lithium is the cause.",
)

L['ENDO-23'] = dict(
  sub="Endocrine → Adrenal, pituitary and DI → Revision: true or false",
  step=6,
  intro="A sweep through the deck. Each statement turns on one detail from an earlier card.",
  parts=[
    ('a', "**False — primary.** Pigmentation needs a high ACTH (ENDO-14)."),
    ('b', "**True.** Outside critical illness; in septic shock a ‘normal’ level does not exclude CIRCI (ENDO-16a, FLAG)."),
    ('c', "**False — treat first; test later** (ENDO-16d)."),
    ('d', "**True.** Aldosterone is driven by renin and potassium (ENDO-14)."),
    ('e', "**False — a normal pituitary.** Bleeding into an adenoma is apoplexy (ENDO-19)."),
    ('f', "**True.** MRI confirms over 90%; CT 21–28% (ENDO-19e)."),
    ('g', "**False — rises in central DI.** No change is nephrogenic (ENDO-21b)."),
    ('h', "**False — thiazide + amiloride.** The kidney is resistant to desmopressin (ENDO-22)."),
  ],
  mimic=[],
  traps=[
    ("“A normal cortisol excludes adrenal insufficiency in septic shock”", "It does not exclude CIRCI; treatment in septic shock is decided by the pressor need."),
  ],
  decode=[
    ("[pattern] True/false on adrenal, pituitary and DI", "Pigment means primary, treat before testing, Sheehan’s is a normal gland, MRI for apoplexy, desmopressin works only in central DI."),
  ],
  punch="Most errors here come from mixing levels: pigment and potassium belong to the adrenal, steroids come before every test, and desmopressin answers only when the kidney can still hear ADH.",
)

FLAGS = {
  'ENDO-14': "Aldosterone row says secondary disease has ‘Na, K normal’: potassium is normal, but sodium is often low in secondary insufficiency (cortisol lack leaves ADH unsuppressed and impairs free-water excretion), as in the linked Sheehan’s stem (Na 128). Consider ‘K normal; Na may be low’.",
  'ENDO-15': "c names only steroid withdrawal; Marrow tests the patient still ON chronic prednisone (≥5 mg/day) who develops sepsis and needs stress-dose hydrocortisone. Consider adding; explanation gives it.",
  'ENDO-16': "a (and sweep ENDO-23b): ‘random cortisol over 20 µg/dL excludes it’ holds outside critical illness; in septic shock a normal cortisol does not exclude CIRCI (GrandT1 stem; SCCM/ESICM 2017 found no reliable single test), and current sepsis guidance does not use a level. Explanation says so. b: could add the Endocrine Society diagnostic cut-off (peak <18 µg/dL / 500 nmol/L at 30 or 60 min).",
  'ENDO-20': "Sarcoid is listed only under nephrogenic; it is primarily a central cause (granulomatous infiltration of hypothalamus/stalk, with LCH) and nephrogenic only via hypercalcaemia/interstitial nephritis (verified fix, ‘partly’). DocT keys sarcoid as NOT a nephrogenic cause. Explanation teaches both routes.",
  'ENDO-17': "Card text is right. Card-layer line (DocT) says minor procedures need ‘only the usual dose plus a single 25–50 mg’: that is pre-2020 teaching; Association of Anaesthetists 2020 gives body-surface and intermediate surgery under anaesthesia the same 100 mg IV at induction (then double the oral dose for 48 h), and only bowel preparation keeps the usual dose. Card-layer etomidate figure ‘6–48 h’ (Marrow line) and ‘24–72 h’ (ENDO-18 DocT GT line) conflict; Vinclair 2008 found insufficiency in 80% at 12 h, 9% at 48 h, 7% at 72 h (reversible by 48 h). Explanation uses the study.",
  'ENDO-18': "Card text is right. ‘Surviving Sepsis 2026’ (cited in the DocT CGT4 stem) is real: Crit Care Med, March 2026; it keeps a conditional suggestion for IV corticosteroids in septic shock with certainty downgraded to low, and its public summaries give no dose or noradrenaline threshold, so the 200 mg/day and ≥0.25 µg/kg/min for ≥4 h figures are SSC 2021’s.",
  'ENDO-22': "Card lists thiazide + amiloride but not that amiloride is first for lithium-induced DI (verified fix, ‘partly’); the two DocT keys conflict (thiazide vs amiloride). Explanation gives the lithium rule.",
}
