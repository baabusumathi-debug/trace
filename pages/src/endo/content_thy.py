# Thyroid group content for the endocrine concept page (22 Nov 2026).
# Card text = Drive cards.jsonl + cardfix.json + Endo_Card_Flags_22Nov_DECISIONS.md.

GROUP = dict(id='THY', title='Thyroid', deck='ENDO01A')

# ---------- hit-card text (q, a, watch) with fixes applied ----------
CARDS = {
('ENDO01A', 'ENDO-03'): ("**Thyroid patterns and causes of thyrotoxicosis:**",
"**STATE** | **TSH** | **T3, T4**\n**Primary hyperthyroid** | **Low** | High\n**Primary hypothyroid** | **High** | Low\n**Secondary (pituitary) hypothyroid** | **Low or inappropriately normal** | Low\n**Subclinical hyperthyroid / hypothyroid** | Low / High | **Normal**\n"
"- **Overproduction**: Graves', toxic multinodular goitre, TSH-secreting adenoma.\n- **Leak from destruction**: subacute or lymphocytic thyroiditis, radiation (Riedel's is fibrosing and does not cause thyrotoxicosis).\n- **Drugs**: thyroxine, **amiodarone**, iodinated contrast; metastatic thyroid cancer.", ""),
('ENDO01A', 'ENDO-04'): ("**Thyroid storm:**\na Frequency, sex, mortality\nb Triggers\nc Mechanism",
"a **1%** of hospitalised hyperthyroid patients; **women 3:1**; mortality about **10%** (multi-organ failure).\nb **Stopping antithyroid drugs**, **surgery** (especially thyroidectomy), neck trauma, infection, pregnancy and delivery, **DKA**, stress, stroke, PE, intense exercise, tyrosine kinase inhibitors, even dental extraction.\nc More **free hormone**: increased release, reduced TBG binding, more adrenergic receptors and peripheral conversion.", ""),
('ENDO01A', 'ENDO-05'): ("**Thyroid storm: clinical features.**",
"- **Fever**, hyperthermia; profuse sweating, flushed skin.\n- **CNS**: anxiety, agitation, delirium, up to coma.\n- **CVS**: tachycardia, especially **atrial fibrillation**; **high systolic-to-diastolic ratio** (wide pulse pressure); heart failure up to cardiogenic shock; **Lerman-Means scratch** (pleuro-pericardial sound).\n- **GI-hepatic**: diarrhoea, nausea, vomiting, jaundice.\n- Tachypnoea, tremor.\n- Labs: high free T4/T3, **TSH undetectable (under 0.1 mIU/L)**.",
"Diagnosis is clinical: hormone levels do not separate storm from uncomplicated thyrotoxicosis. That is why a score exists."),
('ENDO01A', 'ENDO-08'): ("**Drugs in thyroid storm:**",
"**DRUG** | **DOSE** | **WHY**\n**Propranolol** | IV 1–2 mg; oral 60–80 mg 4-hourly (ATA 2016) | Blocks adrenergic effects; **reduces T4→T3**\n**PTU** (preferred) | 500–1000 mg load, then 200–250 mg | Blocks synthesis **and** **peripheral conversion**\n**Methimazole / carbimazole** | **60–80 mg/day** (20 mg every 4–6 h); IV not in India | Blocks synthesis\n**Lugol's iodine** / SSKI | **At least 1 h after** the thionamide | Wolff-Chaikoff: stops release and synthesis\n**Hydrocortisone** | Steroid of choice | Reduces conversion; covers relative adrenal insufficiency\n**Lithium carbonate** | 300 mg every 6–8 h (rarely used) | Inhibits colloid proteolysis (release)\n**L-carnitine** | Adjuvant | Blocks hormone entry to nuclei",
"Iodine first would feed new hormone synthesis: the thionamide must block TPO before the iodine load arrives."),
('ENDO01A', 'ENDO-09'): ("**Thyroid storm: the order of treatment.**",
"- **First line**: **β-blocker** (propranolol) → **thionamide** (PTU best) → **iodine** (at least 1 h after the thionamide) → **hydrocortisone**.\n- **Refractory**: lithium (when iodine cannot be used), cholestyramine, L-carnitine, plasma exchange, emergency thyroidectomy.\n- **Support**: fluids and electrolytes, **paracetamol** (not aspirin: it displaces hormone from TBG), phenobarbital, furosemide and ACE inhibitor for heart failure, sedation.\n- **Selected**: ventilation for hypoxaemia; cooling mattresses and cold packs if over 40 °C.\n- Treat the trigger.",
"The usual exam sequence is β-blocker → thionamide → iodine (an hour later) → glucocorticoid. Plasma exchange or emergency thyroidectomy if all fail."),
('HY5', 'HEO-07'): ("**Thyroid storm: the drug sequence and why the order matters.**",
"**β-blocker → thionamide → iodine (≥ 1 h later) → steroid**\n1 **Propranolol**: controls adrenergic symptoms; blocks T4 → T3 at high dose.\n2 **PTU** (or methimazole): stops new hormone synthesis; PTU also blocks T4 → T3.\n3 **Iodine** (Lugol's/SSKI) **at least 1 h after the thionamide**: blocks hormone release.\n4 **Hydrocortisone**: blocks conversion, covers relative adrenal insufficiency.\n5 Supportive: cooling (paracetamol, not aspirin), fluids; cholestyramine; treat the trigger.",
"Sequence correct in GT4; Burch–Wartofsky ≥ 45 = storm (GT2 correct)."),
('ENDO01A', 'ENDO-10'): ("**Myxoedema (hypothyroid) coma:**\na Definition and numbers\nb Underlying causes\nc Precipitants\nd Features",
"a Decompensated severe hypothyroidism with altered mentation; **rare** (about 0.2–1 per million a year); mortality **20–50% even with treatment**; TSH usually **over 100 mIU/L**.\nb Hashimoto's, thyroidectomy, radioiodine or radiotherapy, antithyroid drugs, **tyrosine kinase inhibitors**; pituitary disease.\nc **Infection, cold exposure, stroke**, drugs (**sedatives, analgesics, amiodarone, lithium**).\nd Coma, **hypothermia** (below 35 °C, often much lower), bradycardia, non-pitting oedema, dry yellow skin, hyporeflexia, muffled heart sounds (effusion), constipation; rarely seizures.", ""),
('ENDO01A', 'ENDO-11'): ("**Myxoedema coma: investigations.**",
"**TEST** | **FINDING**\n**Thyroid** | Free T4, T3 low; **TSH over 100** (low or normal if pituitary)\n**ABG** | **Hypoxaemia, hypercapnia**, respiratory acidosis\n**Blood** | **Hyponatraemia** (low free-water clearance from a low GFR, plus raised ADH), **hypoglycaemia**, anaemia, high CK and LDH, high transaminases, creatinine, cholesterol\n**ECG** | **Sinus bradycardia, low voltage**, long QT, **T-wave flattening or inversion**\n**Echo** | **Pericardial effusion**, concentric LVH, reduced EF", ""),
('ENDO01A', 'ENDO-12'): ("**Treating myxoedema coma:**",
"- **Hydrocortisone IV first**: concurrent adrenal insufficiency (**Schmidt's syndrome**) or panhypopituitarism.\n- **IV levothyroxine**: **200–400 µg load** (lower if old or cardiac), then 1.6 µg/kg/day (75% while IV); ± **IV liothyronine (T3) 5–20 µg**, then 2.5–10 µg 8-hourly.\n- **Sodium**: water restriction; 0.9% saline if Na under 120; 3% saline if severe; vaptans if not severe; sodium 8-hourly.\n- Ventilate for respiratory acidosis; furosemide for pulmonary oedema; passive rewarming if under 35 °C; treat infection.\n- **Complications**: respiratory or cardiac failure, **MI from too much T4**, pulmonary oedema, shock, bleeding (**acquired von Willebrand**; factors V, VII, VIII, IX, X low).",
"Old 500 µg T4 loads were dropped: they caused myocardial ischaemia. Thyroxine before steroid can precipitate adrenal crisis by speeding cortisol clearance."),
}

# top-up answers with the 22 Nov decisions applied
TOPUP_A = {
'T_2b8a9a37': ["Cytokines, cortisol and fasting cut **type 1 deiodinase** (less T4 to T3) and raise **type 3** (more reverse T3), so **T3 falls first**; type 2 changes are inconsistent.",
  "Hypothalamic TRH falls, so **TSH is normal or low**: an acquired, transient **central** hypothyroidism (dopamine and steroids suppress TSH further).",
  "Low T3 alone = mild illness; **low T4 with low TSH = severe** (total T4 < 4 µg/dL carries about 50% mortality).",
  "In recovery TSH may rise transiently, **usually below 20**: this is not primary hypothyroidism.",
  "**Do not screen TFTs or give thyroxine**: treat the illness, feed the patient, recheck 4–6 weeks after recovery; treat only clear primary disease (TSH > 20 with low free T4)."],
'T_38ffd8d5': ["Steroid-responsive encephalopathy with autoimmune thyroiditis: **high anti-TPO**; thyroid status varies (most reported cases are subclinically or overtly hypothyroid), and the brain does not track it.",
  "Subacute confusion, **seizures, myoclonus, stroke-like episodes**, headache or visual change.",
  "CSF protein high, EEG diffusely slow, MRI often non-specific; a **diagnosis of exclusion**.",
  "**High-dose steroids** (methylprednisolone 1 g/day for 3–7 days, then taper): the response is the confirmation.",
  "IVIG or plasma exchange if refractory."],
}

# patch bold leads in the explanation layer that restate the old card text
WHY_FIX = {
('ENDO01A', 'ENDO-03', 'f'): ('subacute, lymphocytic or Riedel thyroiditis, radiation', 'subacute or lymphocytic thyroiditis, radiation'),
('ENDO01A', 'ENDO-07', 'd'): ('from 90 vs 130', 'from 99 vs 130'),
('ENDO01A', 'ENDO-08', 'c'): ('10–50 mg (scan unclear), 6-hourly; IV not in India', '60–80 mg/day (20 mg every 4–6 h); IV not in India'),
('ENDO01A', 'ENDO-09', 'b'): ('Second line: iodine (Lugol’s, potassium or sodium iodide) → lithium → L-carnitine.', 'Iodine belongs to the first line, an hour after the thionamide; lithium only when iodine cannot be used.'),
('ENDO01A', 'ENDO-10', 'a'): ('prevalence 0.01%', 'rare'),
('ENDO01A', 'ENDO-10', 'd'): ('hypothermia (under 33 °C in the notes)', 'hypothermia (below 35 °C)'),
('ENDO01A', 'ENDO-11', 'c'): ('hyponatraemia (high ADH)', 'hyponatraemia (low GFR plus ADH)'),
('ENDO01A', 'ENDO-11', 'd'): ('ECG: sinus bradycardia, low voltage, long QT.', 'ECG: sinus bradycardia, low voltage, long QT, T-wave flattening or inversion.'),
}


WHY_FIX_MORE = {
('ENDO01A', 'ENDO-08', 'c'): (', so the card’s range is unclear and probably low (FLAG)', ''),
('ENDO01A', 'ENDO-08', 'f'): ('Lithium carbonate: 300 mg 6-hourly', 'Lithium carbonate: 300 mg every 6–8 h'),
('ENDO01A', 'ENDO-10', 'a2'): (' (the card’s 0.01% could not be traced; FLAG)', ''),
('ENDO01A', 'ENDO-10', 'd2'): (' 33 °C is the notes’ figure, not a standard cut-off (FLAG).', ''),
('ENDO01A', 'ENDO-11', 'd2'): (' (not printed on the card)', ''),
}

# ---------- concepts ----------
CONCEPTS = [
dict(id='THY1', title='Reading thyroid labs', steps=[('ENDO01A', 1)], extra=[], tops=['T_2b8a9a37'],
summary='TSH is the amplified signal: read it first, then free T4, and in the ICU suspect the illness before the gland.',
core=[
 "The gland makes mostly **T4**, a long-lived prohormone (**half-life 7 days**); tissues turn it into **T3**, the potent hormone (**3–4×**), so **75–80% of T3 is made outside the thyroid**. Only the **free** fraction acts.",
 "TRH drives TSH, TSH drives the gland, and T4/T3 feed back on both. A small change in free T4 moves TSH a lot, so **TSH is the first test**.",
 "Primary disease moves TSH against T4: **undetectable** in overt hyperthyroidism, **high** in hypothyroidism. When the pituitary fails, TSH is **low or inappropriately normal** with a low T4, so a normal TSH cannot exclude central disease.",
 "Thyrotoxicosis has two engines. **Overproduction** (Graves’, toxic nodules) makes new hormone, so thionamides work. A **leak** from damaged follicles (thyroiditis, **lithium**, amiodarone type 2) releases stored hormone, so thionamides are useless and the β-blocker carries the patient.",
 "In the **first trimester TSH falls** (often < 0.1) because **hCG** stimulates the TSH receptor: physiological, peaking at 10–12 weeks.",
 "In the ICU the commonest abnormal result is **non-thyroidal illness**: cytokines cut **type 1** deiodinase and raise **type 3**, so **T3 falls first and reverse T3 rises**; TRH falls, so TSH stays normal or low.",
 "Severity follows the illness: low T3 alone is mild; **low T4 with a low TSH is severe** (total T4 < 4 µg/dL, about 50% mortality). It marks prognosis; it is not a thyroid problem to treat.",
 "So **don’t test routinely and don’t give thyroxine**: treat and feed the patient. In recovery TSH can overshoot (**usually < 20**); repeat **4–6 weeks** after recovery and treat only **TSH > 20 with a low free T4**.",
],
flag=[
 "**Undetectable vs low:** in overt hyperthyroidism both are true, but when both are offered the exam wants **undetectable** (only 18% chose it).",
 "**Why TSH falls in illness:** DocT keys **cytokines acting directly on the pituitary** over ‘decreased TRH’ when both appear; both happen.",
 "**Card fixed:** Riedel thyroiditis is no longer listed as a cause of thyrotoxicosis; secondary hypothyroidism reads ‘TSH low or inappropriately normal’.",
],
vis=['GRID_TSH', 'NTI_TIMELINE'],
pairs=[
 ('Graves’', 'Painless thyroiditis', ['Thyrotoxic', 'TSH suppressed', 'β-blocker for symptoms'],
  [('!Engine', 'Overproduction (new synthesis)', 'Leak of stored hormone'),
   ('Uptake scan', 'High', 'Low'),
   ('Thionamide', 'Works', 'Useless'),
   ('Clues', 'Eye signs, goitre, TRAb', 'Lithium, checkpoint inhibitor, interferon; self-limiting, then hypothyroid')]),
 ('Non-thyroidal illness', 'Central hypothyroidism', ['Low T4', 'TSH low or normal'],
  [('!Recovers with the illness', 'Yes', 'No'),
   ('Other pituitary hormones', 'Normal', 'Often deficient'),
   ('History / imaging', 'Sepsis, surgery, starvation', 'Sellar lesion, apoplexy, surgery'),
   ('Thyroxine', 'Not given', 'Replace (after cortisol)')]),
 ('Recovery-phase TSH rise', 'Primary hypothyroidism', ['TSH above normal', 'Free T4 low-normal'],
  [('!TSH level', 'Usually < 20, rising as the patient improves', '> 20 with a low free T4, or persistent'),
   ('On repeat (4–6 weeks)', 'Normal', 'Still abnormal'),
   ('Action', 'Repeat, no thyroxine', 'Levothyroxine')]),
 ('First-trimester low TSH', 'Graves’ in pregnancy', ['TSH low', 'Early pregnancy'],
  [('!Free T4', 'Near normal', 'Clearly high'),
   ('Goitre, eye signs, TRAb', 'Absent', 'Present'),
   ('Course', 'Peaks at 10–12 weeks, settles', 'Persists'),
   ('Treatment', 'None; a β-blocker only for symptoms', 'Antithyroid drug (PTU in the first trimester)')]),
],
trees=[],
gate=[
 ("Septic shock, T3 low, TSH 8. What do you do?", "Nothing thyroid-specific: non-thyroidal illness. No thyroxine and no extra tests; treat the sepsis and recheck after recovery."),
 ("Pituitary disease, low free T4, TSH 1.5. What is that TSH?", "Inappropriately normal: central hypothyroidism. TSH cannot exclude it."),
 ("Thyrotoxicosis after starting lithium, low uptake. Will a thionamide help?", "No. It is a leak (painless thyroiditis), so give a β-blocker and support."),
]),

dict(id='THY2', title='Thyroid storm', steps=[('ENDO01A', 2), ('ENDO01A', 3), ('ENDO01A', 4)], extra=[('HY5', 'HEO-07')], tops=[],
summary='Storm is a trigger acting on a primed heart. Score it clinically, then block the tissue, stop synthesis, close release an hour later and cut conversion.',
core=[
 "Storm is thyrotoxicosis that has **decompensated into organ failure**. Hormone levels are **no higher** than in ordinary thyrotoxicosis, so no test makes the diagnosis.",
 "What tips it is a **trigger** acting on tissue with **up-regulated β₁-receptors**: **infection** in the undiagnosed, **stopping the thionamide** in the treated; surgery, labour and DKA too. Mortality is still about **1 in 10**.",
 "Four features mark storm over plain thyrotoxicosis: **fever** (hyperpyrexia, the cardinal sign), a **changed mind**, a **failing heart** (AF, high-output failure) and a **yellow liver**.",
 "Score it: **Burch–Wartofsky ≥ 45 = storm, 25–44 = impending, < 25 unlikely**; ≥ 104 °F and seizure or coma score **30** each. The **Japanese criteria** need proven thyrotoxicosis and count organ failures (38 °C, pulse 130, bilirubin > 3).",
 "Treat at four points, in order. **β-blocker first** (propranolol): it acts in minutes on the primed heart and also cuts T4→T3.",
 "Then a **thionamide**: **PTU** is preferred in storm because it also blocks conversion (any trimester); methimazole 60–80 mg/day is acceptable. Give one thionamide, not both.",
 "Then **iodine at least 1 h after the thionamide** to shut off release. Given first, iodine becomes substrate for new hormone. Lithium replaces it when iodine cannot be used.",
 "**Hydrocortisone** (300 mg, then 100 mg 8-hourly): its keyed role is to **cut T4→T3**; it also covers adrenal reserve. Add **paracetamol, not aspirin**, cooling and fluids, and treat the trigger. No response in 24–48 h: plasma exchange, then thyroidectomy.",
],
flag=[
 "**Iodine timing:** ATA 2016 says **at least 1 h after** the thionamide (the exam answer); JTA 2016 gives it at the same time.",
 "**Which β-blocker:** the exam key is **propranolol**; JTA 2016 prefers β₁-selective landiolol or esmolol. Storm with AF and severe heart failure: DocT keys **digoxin plus a cautious β-blocker** (esmolol is equally supported); never full-dose propranolol or diltiazem.",
 "**Cards fixed:** iodine is part of the first-line regimen (not ‘second line’); methimazole is 60–80 mg/day.",
],
vis=['DRUG_SITES', 'BWPS_LADDER', 'STORM_ORDER'],
pairs=[
 ('Thyroid storm', 'Sepsis', ['Fever', 'Tachycardia', 'Delirium', 'Shock'],
  [('!TSH and free T4', 'TSH suppressed, free T4 high', 'Normal (or a low T3 from illness)'),
   ('What drives it', 'A trigger on a primed heart', 'Infection'),
   ('Treatment', 'β-blocker → thionamide → iodine → steroid', 'Antibiotics, source control, pressors'),
   ('Together?', 'Yes: infection is the commonest trigger', 'Treat both')]),
 ('Thyroid storm', 'Phaeochromocytoma crisis', ['Tachycardia', 'Sweating', 'Hyperthermia', 'Agitation'],
  [('!Which blocker first', 'β-blocker first', 'α-blocker before any β-blocker'),
   ('Blood pressure', 'Wide pulse pressure, high output', 'Paroxysmal severe hypertension'),
   ('Test', 'TSH suppressed, high free T4', 'High metanephrines; TSH normal'),
   ('Why the order', 'β₁ up-regulation drives the danger', 'Unopposed α-stimulation causes a hypertensive crisis')]),
 ('PTU', 'Methimazole', ['Block thyroid peroxidase (synthesis)', 'Stored hormone still leaks for weeks', 'Give only one'],
  [('!T4→T3 in the tissues', 'Also blocks it', 'No effect'),
   ('In storm', 'Preferred (ATA 2016)', 'Acceptable (JTA 2016: no worse)'),
   ('Pregnancy', 'First trimester; any trimester in storm', 'After the first trimester'),
   ('Liver', 'Severe injury risk: switch once stable', 'Safer'),
   ('Dose', '500–1000 mg load, then 250 mg 4-hourly', '60–80 mg/day')]),
 ('Burch–Wartofsky', 'Japanese (Akamizu)', ['Clinical diagnosis', 'An ‘impending’ or ‘suspected’ tier', 'Neither should delay treatment'],
  [('!Proven thyrotoxicosis', 'Not required', 'Prerequisite'),
   ('Format', 'Points: ≥ 45 storm', 'Combinations: TS1 definite, TS2 suspected'),
   ('Fever', 'From 37.2 °C', '38 °C'),
   ('Heart rate', 'From 99', '130'),
   ('Liver', 'Jaundice', 'Bilirubin > 3 mg/dL')]),
],
trees=[dict(start='Fever, tachycardia and delirium in the ICU', q='Which clue is in the stem?', b=[
 dict(a='TSH suppressed, free T4 high', dx='Thyroid storm', c='infection may be its trigger'),
 dict(a='Rigidity, high CK, antipsychotic', dx='NMS'),
 dict(a='Clonus, serotonergic drug', dx='Serotonin syndrome'),
 dict(a='Paroxysmal hypertension, high metanephrines', dx='Phaeo crisis', c='α-blocker first'),
 dict(a='Shock, Na low, K high, glucose low', dx='Adrenal crisis', c='hydrocortisone covers storm too')])],
gate=[
 ("Storm, PTU just started. Which drug must wait at least an hour?", "Iodine (Lugol’s or SSKI). Given first it feeds new hormone synthesis."),
 ("What is the main role of the steroid in the storm regimen?", "Inhibiting T4→T3 conversion; covering adrenal reserve is the second reason."),
 ("Burch–Wartofsky score of 38. What is it?", "Impending storm (25–44): treat if the patient is sick."),
]),

dict(id='THY3', title='Myxoedema coma', steps=[('ENDO01A', 5), ('ENDO01A', 6)], extra=[], tops=['T_38ffd8d5'],
summary='The opposite failure: everything slows until a trigger tips it. Steroid before thyroxine, thyroxine loaded gently, rewarming passive, sedatives never.',
core=[
 "Myxoedema coma is **severe hypothyroidism plus a changed mind**; most patients are obtunded rather than comatose. It is very rare, and mortality is **20–50%** even with treatment.",
 "The background is long-standing hypothyroidism (Hashimoto’s, **radioiodine or thyroidectomy**, TKIs, **lithium**). The tip is **infection, cold, stroke or sedatives and opioids**, which these patients clear slowly.",
 "Recognise the pattern: **hypothermia (< 35 °C), hypoventilation, hyponatraemia, hypoglycaemia and bradycardia**, often in an elderly patient in winter. Fever may be absent even with sepsis.",
 "Tests: **TSH high** (often > 100; low or normal if the pituitary failed) with a low free T4. ECG: **bradycardia, low voltage, long QT, T-wave inversion**; echo: effusion. Send a **cortisol**, then treat without waiting.",
 "The sodium falls mainly because a **low cardiac output and GFR** deliver less filtrate to the diluting segment, with ADH on top. Exclude hypothyroidism and cortisol lack before calling it SIADH.",
 "**Airway first**: hypercapnia and **aspiration pneumonitis** are the typical lung problems. Intubate if obtunded, and give empirical antibiotics.",
 "**Hydrocortisone before thyroxine**, because thyroxine speeds cortisol clearance and can precipitate adrenal crisis. Then **IV levothyroxine 200–400 µg** (less if old or cardiac), then about 1.6 µg/kg/day at 75% IV. **T3 only in small doses** (5–20 µg): it strains the heart.",
 "Support: **passive rewarming** (active external warming causes vasodilatory collapse), slow sodium correction (3% saline boluses if severe) and glucose. **No sedatives.**",
],
flag=[
 "**Cards fixed:** hypothermia is below 35 °C (not 33); the ECG row now includes **T-wave inversion** (DocT’s key); prevalence reads ‘rare’.",
 "**T4 load:** ATA 2014 gives 200–400 µg; older texts 300–500 µg. Loads above 500 µg T4 or 75 µg T3 a day are linked to more deaths.",
 "**The opposite trap:** Hashimoto encephalopathy (SREAT) has high anti-TPO and a variable thyroid state; it is treated with **steroids, not thyroxine**.",
],
vis=['FOUR_HYPOS', 'MYX_ORDER'],
pairs=[
 ('Myxoedema coma', 'Thyroid storm', ['Thyroid emergency with an altered mind', 'Often triggered by infection', 'Hydrocortisone early'],
  [('!Steroid timing', 'Before thyroxine', 'With the first-line drugs (cuts conversion)'),
   ('Temperature', 'Hypothermia', 'Hyperpyrexia'),
   ('Heart', 'Bradycardia, low voltage, effusion', 'Tachycardia, AF, high-output failure'),
   ('Breathing', 'Hypoventilation, CO₂ retention', 'Tachypnoea'),
   ('Avoid', 'Sedatives, active rewarming', 'Aspirin, iodine before the thionamide')]),
 ('Myxoedema coma', 'Uncomplicated hypothyroidism', ['Cold intolerance, weight gain, dry skin', 'High TSH, low free T4'],
  [('!Mental state', 'Obtunded or comatose', 'Alert'),
   ('Temperature', 'Below 35 °C', 'Normal'),
   ('Organ failure', 'CO₂ retention, low Na, low glucose, bradycardia', 'None'),
   ('Treatment', 'ICU: hydrocortisone, then IV T4', 'Oral levothyroxine')]),
 ('Myxoedema coma', 'Environmental hypothermia', ['Cold, slow, bradycardic', 'Confused'],
  [('!TSH', 'High (or low if pituitary)', 'Normal'),
   ('Look', 'Periorbital and non-pitting oedema, macroglossia', 'No such signs'),
   ('Sodium', 'Low', 'Usually normal'),
   ('Rewarming', 'Passive; does not rewarm normally', 'Rewarms; active core warming if in arrest')]),
 ('Hashimoto encephalopathy (SREAT)', 'Myxoedema coma', ['Autoimmune thyroid disease', 'Encephalopathy'],
  [('!Thyroid state', 'Varies, often mild; the brain does not follow it', 'Profoundly hypothyroid'),
   ('Features', 'Seizures, myoclonus, stroke-like episodes', 'Hypothermia, slowness, hypoventilation'),
   ('Treatment', 'High-dose steroids (methylprednisolone 1 g/day, 3–7 days)', 'Hydrocortisone, then IV thyroxine'),
   ('What confirms it', 'Response to steroids', 'TSH and free T4')]),
 ('Hypothyroid hyponatraemia', 'SIADH', ['Euvolaemic', 'Concentrated urine', 'Low serum osmolality'],
  [('!Rule out first', 'Check TSH and cortisol', 'Called only after both are normal'),
   ('Main mechanism', 'Low GFR: less filtrate reaches the diluting segment (plus ADH)', 'Inappropriate ADH'),
   ('Fix', 'Thyroxine, with hydrocortisone first', 'Fluid restriction; treat the cause')]),
],
trees=[],
gate=[
 ("Which drug goes in before thyroxine, and why?", "Hydrocortisone. Thyroxine speeds cortisol clearance and can precipitate adrenal crisis."),
 ("Agitated, hypercapnic hypothyroid patient. Sedate?", "No. Sedatives deepen hypoventilation and are themselves a precipitant."),
 ("Typical ECG in myxoedema coma?", "Bradycardia, low voltage, long QT and T-wave inversion (the keyed finding)."),
]),
]

# ---------- group extras: axis map and pattern drill ----------
AXIS = dict(
 title='Thyroid axis: where each emergency breaks it',
 levels=[
  ('Hypothalamus', 'TRH', ['Non-thyroidal illness: cytokines lower TRH'], []),
  ('Anterior pituitary', 'TSH', ['Central hypothyroidism: TSH low or inappropriately normal', 'Apoplexy, Sheehan’s'], ['Dopamine and high-dose steroids suppress TSH']),
  ('Thyroid gland', 'T4 ≫ T3 (trap → organify → couple → store → release)', ['Primary hypothyroidism → myxoedema coma (TSH high)', 'Graves’ / toxic nodules: overproduction', 'Thyroiditis: leak'], ['Thionamides block TPO', 'Iodine and lithium block release', 'Perchlorate blocks the trap']),
  ('Tissues', 'Deiodinase: T4 → T3; β₁-receptors', ['Storm: trigger acting on primed β₁-receptors', 'Non-thyroidal illness: type 1 down, type 3 up'], ['PTU, propranolol, steroids cut T4 → T3', 'Propranolol blocks the β effects']),
 ],
 feedback='T4 and T3 inhibit TRH and TSH. That loop is why TSH moves opposite to T4 in primary disease, and why it fails to rise when the pituitary is the problem.')

DRILL = [
 ("TSH undetectable, free T4 high, eye signs", "Overt primary hyperthyroidism (Graves’)", "Full feedback suppression; ‘undetectable’ beats ‘low’."),
 ("TSH 9, free T4 low", "Primary hypothyroidism", "The failing gland loses feedback, so TSH rises."),
 ("TSH 1.2, free T4 low, low cortisol and gonadotrophins", "Central (secondary) hypothyroidism", "The TSH is inappropriately normal."),
 ("Septic, day 3: T3 low, reverse T3 high, TSH and T4 normal", "Non-thyroidal illness (mild)", "No treatment; do not repeat tests in the ICU."),
 ("Ventilated, shocked: T4 low, TSH low", "Severe non-thyroidal illness", "A prognostic sign (T4 < 4 µg/dL ≈ 50% mortality), not a reason for thyroxine."),
 ("Recovering from sepsis: TSH 12, free T4 low-normal", "Recovery phase of non-thyroidal illness", "Repeat 4–6 weeks after recovery; treat only TSH > 20 with a low free T4."),
 ("10 weeks pregnant: TSH 0.05, free T4 near normal, no goitre", "Gestational (hCG-driven) TSH suppression", "Physiological; peaks at 10–12 weeks."),
 ("TSH normal or high with a high free T4", "TSH-secreting pituitary adenoma", "The source is the pituitary, so TSH is not suppressed."),
 ("Thyrotoxic on lithium, low radioiodine uptake", "Painless (silent) thyroiditis", "A leak: thionamides useless, β-blocker for symptoms."),
 ("32 °C, Na 118, glucose 50, PaCO₂ 70, TSH 90", "Myxoedema coma", "Hydrocortisone first, then IV levothyroxine."),
]

PRIMER_EXTRA = ''
