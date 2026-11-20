# GI01C — Explain v3 ("Learn" depth): acute liver failure, part 3 — liver transplantation (types, contraindications, what predicts outcome), King’s College criteria,
# other prognostic criteria (Clichy, lactate, phosphate, MELD, factor VIII/V), the AIIMS ALFED score and the older AIIMS indicators, liver assist devices (biological vs non-biological,
# cell sources, MARS vs SPAD, the device trials), plasma exchange, take-home list and true/false sweep.
# No mnemonics or hooks. Driven by qpack/GI01C.md (11 question links: ALF-33 King’s College criteria 9 — DocT QBank 1, DocT GTs 7, the MELD question shared with ALF-34;
# ALF-32 one Marrow question (Budd–Chiari); ALF-34 one DocT QBank question). ALF-35 to ALF-43 have no linked question and get short explanations with [pattern] decode items.
# gi_cardlayer.json read for GI01C|ALF-32 (Marrow line and Crossfire on the Budd–Chiari key), ALF-33 (chips only), ALF-34 (Crossfire on the MELD key); explanations agree with them.
# No `fix` entries beyond the same card layer in trace/test/data/qbank.json (checked 20 Nov 2026). No Top-up cards for GI01C in gi_topups.json.
# Checked online on 20 Nov 2026:
#  - EASL 2017 ALF CPG (J Hepatol 2017, full text PDF): transplant to be considered when Clichy or King’s criteria are met (II-2, 1); Clichy = grade 3–4 HE with factor V <20% if age <30,
#    <30% if age >30; paracetamol lactate >3.5 mmol/L on admission or >3.0 after fluid resuscitation (sens 81%, spec 95%); phosphate >1.2 mmol/L on day 2–3 (sens 89%, spec 100%);
#    MELD >33 at onset of HE (paracetamol), >32 (non-paracetamol); factor V <10% (paracetamol); new markers not validated and not for routine use; irreversible brain injury contraindicates
#    transplant (II-3, 1); contraindications should not stop transfer to a transplant centre; acute Budd–Chiari suspected when ALF presents with gross ascites; malignant infiltration and
#    acute ischaemic injury are not indications for transplant; liver support systems (biological or adsorbent) only within RCTs (II-1, 1); plasma exchange improves transplant-free survival
#    (I, 1), more so if early (I, 2); invasive ICP monitoring to be considered in grade 3–4 with high-risk features; mannitol or hypertonic saline for ICP surges, short-term hyperventilation;
#    prophylactic antiepileptics not warranted.
#  - ACG 2023 ALF guideline (Shingina, Am J Gastroenterol 2023; Healio summary and ACG grand-round slides): KCC or MELD recommended for prognostication; meeting KCC or MELD >25 = high risk;
#    no conclusive evidence for routine ICP monitoring. Its wording on plasma exchange could NOT be retrieved (the card’s ‘evidence still insufficient’ left as printed).
#  - SCCM 2023 liver failure guideline, part II (Nanchal, Crit Care Med 2023; SCCM page): suggest plasma exchange, when available, in critically ill ALF with hyperammonaemia (>150 µmol/L)
#    (conditional, low); either extracorporeal liver support or standard therapy (conditional, very low); suggest NOT using invasive ICP monitoring (conditional, very low); suggest hypertonic
#    saline when at risk of intracranial hypertension (ammonia >150, high-grade HE, multi-organ failure); no recommendation on lactulose, rifaximin, LOLA and other ammonia-lowering agents.
#  - Larsen, J Hepatol 2016 (n 182, open RCT): HVP 15% of ideal body weight daily for 3 days; hospital survival 58.7% vs 47.8%, HR 0.56 (stratified for transplant); no benefit in those
#    bridged to transplant; SIRS and SOFA fell; attenuated innate immune activation.
#  - Maiwall, Clin Gastroenterol Hepatol 2022 (n 40, AIIMS/ILBS Delhi, open RCT, ALF with cerebral oedema, 78% viral, 83% hyperacute): SVPE 1.5–2.0 plasma volumes per session,
#    mean 2.15 sessions; 21-day transplant-free survival 75% vs 45% (HR 0.30); day-5 SIRS resolution 84% vs 26%, better lactate clearance, lower ammonia and SOFA.
#  - FULMAR (Saliba, Ann Intern Med 2013, n 102): 6-month survival MARS 84.9% vs 75.5% (P 0.28); paracetamol 85.0% vs 68.4% (P 0.46); 66 of 102 transplanted, median 16.2 h from randomisation.
#  - HepatAssist (Demetriou, Ann Surg 2004): 171 randomised (11 US + 9 European sites); 30-day survival 71% vs 62% (P 0.26); 147 after excluding primary non-function 73% vs 59% (P 0.12);
#    adjusted fulminant/subfulminant subgroup risk ratio 0.56 (P 0.048).
#  - ALFED (Kumar, Gut 2012): derivation 244, validation 136; ammonia, bilirubin, INR, HE >grade 2 scored on persistence or rise over 3 days; range 0–6; AUROC 0.91/0.92; ≥4: PPV 85%, NPV 87%;
#    better than KCC and MELD (including serial KCC and MELD).
#  - Acharya, Hepatology 1996 (AIIMS, n 423): independent predictors age ≥40, cerebral oedema, bilirubin ≥15 mg/dL, PT prolonged ≥25 s; ≥3 present → 93% died (sens 93%, spec 80%);
#    about 75% of deaths within 72 h of admission; cause and speed of onset did not affect outcome; hepatitis E in 62% of the tested non-A non-B group.
#  - MARS vs SPAD crossover (Sponholz, Crit Care 2016, n 32): MARS 20% albumin closed circuit with adsorbers; SPAD 4% albumin single pass on a standard machine; bilirubin removal similar;
#    bile acids and creatinine fell more with MARS (higher dialysate flow); platelets fell with MARS only; SPAD about €1500 cheaper per cycle; cites Sauer 2004 in vitro ‘equivalent detoxification’.
#  - ICP monitoring (Karvellas, Crit Care Med 2014, ALFSG n 629): 21-day mortality 33% vs 38% (NS), no effect in paracetamol ALF, higher mortality in non-paracetamol; haemorrhage 7%.
#  - Phenytoin (Bhatia, J Hepatol 2004, n 42): no difference in seizures, cerebral oedema or survival. LOLA (Acharya, Gastroenterology 2009, n 201): ammonia not lowered vs placebo, mortality 42.4% vs 33.3% (NS).
# From standard references without a fresh check (confident unless said): KCC unit conversions (creatinine 300 µmol/L = 3.4 mg/dL, bilirubin 300 µmol/L = 17.5 mg/dL); Vaquero 2005 ICP monitor
# complications 10.3%; Ede 1986 prophylactic hyperventilation (delayed herniation, no fewer oedema cases, no survival gain); Bernal 2002 modified KCC with lactate; Pereira 1992 factor VIII/V >30;
# Schmidt 2002 phosphate; Mitchell APACHE II >15; Clemmesen 1999 / Bernal 2007 ammonia thresholds; ELAD (Ellis 1996, 24 patients); ALFSG spontaneous-survival ranking by aetiology;
# ATT-induced ALF mortality about two-thirds in the AIIMS series (Kumar 2010; less sure of the exact figure). ALFED risk-group mortalities on ALF-36 are the card’s figures, not re-checked.
# Independent review 20 Nov 2026 (second checker) confirmed online: Vaquero, Liver Transpl 2005 (332 patients, 92 monitored; haemorrhage 10.3% of 58 surveyed, half incidental);
#  Kumar, Hepatology 2010 ATT-ALF (70 of 1223, mortality 67.1%; predictors bilirubin ≥10.8, PT prolongation ≥26 s, grade 3–4 HE); Pereira, Gut 1992 (factor VIII/V >30 in 10 of 11 deaths,
#  factor V ≤10%); Mitchell, Crit Care Med 1998 (APACHE II >15, 102 paracetamol patients, sensitivity 82%, specificity 98%); ALFED risk groups 0–1/2–3/4–6 with mortality about 2.6%/33%/88.5%
#  (quoted from Kumar 2012 in a later Indian cohort, PMC6970204); Acharya 1996 (66% died; about 75% of deaths within 72 h); SCCM 2023 wording. Ede 1986 abstract not retrievable:
#  only ‘no effect on the development of cerebral oedema’ confirmed, so the ‘delayed herniation’ claim was removed. ACG 2023 plasma exchange wording still not retrievable.

SPINE = [
  ("Who needs a new liver", "Aetiology decides whether the native liver can recover, so the first job is to identify early, and transfer, the patients who will not survive without a transplant."),
  ("King’s College criteria", "King’s uses two separate lists: for paracetamol, acidosis alone or the triad of INR, creatinine and coma; for everything else, an INR above 6.5 alone or any three of five history and laboratory items."),
  ("Other and dynamic scores", "Clichy, lactate, phosphate, MELD and the AIIMS ALFED score add sensitivity, and ALFED does it by scoring the trend over three days rather than the admission value."),
  ("Liver support devices", "Biological devices use hepatocytes and non-biological ones remove albumin-bound toxins, and no device has shown a survival benefit in a randomised trial."),
  ("Plasma exchange works", "Plasma exchange replaces toxin- and cytokine-laden plasma with fresh plasma, and is the only extracorporeal therapy with randomised evidence of better transplant-free survival."),
  ("The sweep", "Cerebral oedema and infection kill, most prophylactic brain measures have failed in trials, and the criteria are easy to mix up between paracetamol and other causes."),
]

PRIMER = "Acute liver failure is coagulopathy (INR 1.5 or more) and encephalopathy in a patient without known liver disease, within weeks of the onset of jaundice (GI01A covers the definitions and causes; GI01B the ICU management of the brain, circulation and kidneys). The liver can regenerate, so some patients recover fully with supportive care alone, while others die within days of cerebral oedema, infection or multi-organ failure. Emergency transplantation rescues the second group, but a graft is scarce and the window is short, so prognostic criteria exist to pick out, early and with high specificity, the patients who will not survive without one. A score with high specificity rarely lists someone who would have recovered; the price is low sensitivity, so some who will die are not flagged."

L = {}

L['ALF-32'] = dict(
  sub="Acute liver failure → Transplant → Types, contraindications, predictor of outcome",
  step=1,
  intro="Step 1 asks who needs a new liver and what kind. Transplant is the only treatment that reliably changes survival in the patient who is not going to recover, and because most deaths come within the first few days of admission, the decision must be made early. The one real question (Marrow) tests the indication for transplant evaluation in Budd–Chiari presenting as acute liver failure, and its key collides with the contraindications on this card.",
  parts=[
    ('a', "**Orthotopic: the native liver is removed and replaced; lifelong immunosuppression.** This is the standard operation, usually a whole deceased-donor graft (living-donor grafts are used where deceased organs are not readily available, as in much of India). The native liver is gone, so the patient is committed to immunosuppression for life whatever the cause of the failure."),
    ('b', "**Auxiliary: a reduced-size graft supports the patient while the native liver recovers; immunosuppression is then tapered.** A partial graft is placed alongside part of the native liver. The idea follows from biology: in hyperacute failure (paracetamol, hepatitis A, young patients) the native liver often regenerates if the patient survives the first weeks. Once it has, the graft is allowed to atrophy and immunosuppression is withdrawn. It is technically harder and is reserved for selected young, haemodynamically stable patients."),
    ('c', "**Irreversible brain damage, or oedema with sustained ICP above 50 and CPP below 40 mmHg; active extrahepatic infection; multi-organ failure; extrahepatic malignancy.** Each of these means the new liver would not save the patient: a dead or irreversibly injured brain, sepsis that immunosuppression would make lethal, failure of too many other organs, or a cancer that would recur. EASL 2017 states irreversible brain injury as the firm contraindication and adds two points: malignant infiltration of the liver is not an indication at all, and contraindications should not stop transfer to a transplant centre, because they are often judged better there."),
    ('d', "**Aetiology.** Cause matters most because it decides whether the liver can regenerate. Paracetamol, hepatitis A, ischaemic injury and pregnancy-related failure have the best spontaneous survival (about half or more recover without transplant); idiosyncratic drug injury, hepatitis B, indeterminate cases and Wilson’s disease presenting as liver failure have the worst. This is also why King’s College uses separate criteria for paracetamol and non-paracetamol failure (ALF-33)."),
  ],
  mimic=[
    ("Fulminant Budd–Chiari vs other causes of ALF", "Budd–Chiari presents with gross ascites, tender hepatomegaly and an occluded hepatic venous outflow on Doppler or MRI; it needs anticoagulation and decompression (angioplasty, stent or TIPS) before or alongside transplant listing."),
  ],
  traps=[
    ("“Budd–Chiari presenting as ALF in a patient with colon cancer 2 months ago → evaluate for transplant” (Marrow key)", "The key is disputed. Fulminant Budd–Chiari is a transplant indication, but a recent or active extrahepatic malignancy is a contraindication (c). Exam-day rule: with active or recent cancer in the stem, pick anticoagulation with TIPS or stenting; without it, pick transplant evaluation. Ursodiol and open shunt surgery have no role either way."),
    ("“Grade 4 coma or a high ICP alone contraindicates transplant”", "Only irreversible brain injury, or sustained ICP above 50 with CPP below 40 mmHg, does; many grade 4 patients transplanted in time recover neurologically."),
  ],
  decode=[
    ("Recent colon cancer, ALF from Budd–Chiari on CT: additional step? [Marrow]", "Keyed transplant evaluation; the cancer argues for decompression (TIPS) and anticoagulation instead — see the trap."),
    ("Which factor best predicts whether a patient with ALF survives without transplant? [pattern]", "Aetiology."),
  ],
  punch="Cause decides whether the native liver can recover; transplant is for the one that will not, and is ruled out only by an irreversibly damaged brain, uncontrolled infection, multi-organ failure or cancer. In the AIIMS series about three-quarters of deaths came within 72 hours of admission, so list early.",
)

L['ALF-33'] = dict(
  sub="Acute liver failure → Transplant criteria → King’s College criteria",
  step=2,
  intro="Step 2 is the criteria everyone uses to decide who gets listed. King’s College (O’Grady, 1989) split the patients by cause, because paracetamol failure behaves differently: it is hyperacute, and acidosis predicts death in it better than anything else. Nine real questions hit this card; almost all are a paracetamol stem with several abnormal values, asking which one alone qualifies, and the one at 57% shows people pulling items across from the non-paracetamol list or from Clichy.",
  parts=[
    ('a', "**Paracetamol: arterial pH under 7.3, OR all three of INR above 6.5 (PT over 100 s), creatinine above 3.4 mg/dL, grade 3–4 encephalopathy.** The pH criterion stands alone and is measured after adequate fluid resuscitation; early acidosis in paracetamol poisoning reflects massive hepatocyte necrosis with failure to clear lactate, and it predicts death regardless of the coma grade. The other limb needs all three together; any one alone does not qualify. The creatinine figure is 300 µmol/L converted, and paracetamol is directly nephrotoxic, which is why the kidney appears only on this side. A later modification added lactate (above 3.5 mmol/L on admission or above 3.0 after fluids; ALF-34), which raises sensitivity. Meeting the criteria means emergency transplant evaluation now, not more NAC alone or observation."),
    ('b', "**Non-paracetamol: INR above 6.5 (PT over 100 s) alone, OR any three of: cause non-A non-B, drug or halothane; jaundice to encephalopathy over 7 days; age under 10 or over 40; INR above 3.5 (PT over 50 s); bilirubin above 17.5 mg/dL.** These failures are slower and regenerate less, so the criteria lean on the history: an unfavourable cause, a slow (subacute) course and age. Bilirubin (300 µmol/L) counts here because a long jaundiced phase marks failure of regeneration. Encephalopathy is part of the definition of ALF but is not one of the criteria; neither pH nor creatinine appears."),
    ('c', "**Performance: specific, not sensitive.** The criteria rarely list a patient who would have recovered, but they miss a substantial share of those who die, which is why serial reassessment and the add-on markers matter. ACG 2023 recommends King’s or MELD for prognosis and treats meeting King’s, or MELD above 25, as high risk; EASL 2017 says to consider transplant when King’s or Clichy is met."),
  ],
  table=dict(title="Sorting a King’s stem", head=["", "Paracetamol", "Non-paracetamol"], rows=[["Single sufficient item", "**pH under 7.3**", "**INR above 6.5**"], ["Combination", "All three: INR above 6.5, creatinine above 3.4 mg/dL, grade 3–4 HE", "Any three of five: cause, jaundice to HE over 7 days, age under 10 or over 40, INR above 3.5, bilirubin above 17.5 mg/dL"], ["Never on this side", "bilirubin, age, cause, timing", "pH, creatinine, coma grade"]]),
  mimic=[
    ("King’s College vs Clichy", "Clichy uses factor V with grade 3–4 encephalopathy and was derived in viral (hepatitis B) failure; King’s uses pH, INR, creatinine and coma for paracetamol and history items for other causes (ALF-34)."),
  ],
  traps=[
    ("“Bilirubin above 17.4 mg/dL or factor V under 30% fulfils King’s in a paracetamol overdose” (AIM1, 57% right)", "Bilirubin is a non-paracetamol item and factor V is Clichy. In paracetamol the single sufficient item is pH under 7.3."),
    ("“Bilirubin above 10 mg/dL is a transplant criterion” (CGT2 EXCEPT question)", "The non-paracetamol cut-off is about 17.5 mg/dL (300 µmol/L); 10 is the wrong number. Halothane hepatitis does count, as an unfavourable cause."),
    ("“MELD is the most appropriate score for a paracetamol overdose” (DocT QBank key, 45% right)", "King’s is the standard. The options were APACHE II, MELD, SOFA and Child-Pugh; MELD is the least wrong (ACG 2023 accepts King’s or MELD, and MELD above 33 is a paracetamol marker), Child-Pugh is for cirrhosis, SOFA and APACHE II are general ICU scores. If King’s is offered, pick King’s."),
    ("“Patient meets the criteria: repeat enzymes, observe, or continue NAC only”", "Meeting King’s means emergency transplant evaluation; NAC continues alongside, but is not the step being asked."),
  ],
  decode=[
    ("Paracetamol, pH 7.25, creatinine 3.8, INR 7.2, grade 3 HE: which finding ALONE predicts poor prognosis? [DocT GT, 93%]", "Arterial pH under 7.3; the other limb needs all three together."),
    ("Paracetamol, pH 7.25, INR 7.0, creatinine 3.8, grade 4 HE: next step? [DocT GT ×3, 79–88%]", "Emergency liver transplant evaluation."),
    ("Paracetamol, INR 4, grade 3 HE: which poor prognostic indicator requires referral? [DocT GT]", "INR above 6.5 (as part of the triad); AST, platelets and modest bilirubin are not criteria."),
    ("All are transplant criteria EXCEPT: pH under 7.3, bilirubin over 10, creatinine over 3.4, halothane hepatitis [DocT GT]", "Bilirubin over 10 mg/dL."),
  ],
  punch="Sort the stem by cause first. In paracetamol, pH under 7.3 is enough on its own, otherwise INR, creatinine and coma must all be present; in every other cause, INR above 6.5 is enough on its own, otherwise any three of cause, slow onset, age, INR above 3.5 and bilirubin.",
)

L['ALF-34'] = dict(
  sub="Acute liver failure → Transplant criteria → Clichy and other prognostic markers",
  step=3,
  intro="Step 3 adds the markers that patch King’s weak point, its low sensitivity. Each was derived in one kind of liver failure, and the card’s ‘used in’ column is the part examiners test. The one real question (DocT QBank, 45% right) asked which score suits a paracetamol overdose and keyed MELD.",
  parts=[
    ('a', "**Clichy (factor V), viral: factor V under 20% if under 30 years, or under 30% if 30 or older, with grade 3–4 encephalopathy.** Factor V is made only by hepatocytes, has a short half-life (roughly 12–36 hours), and does not depend on vitamin K, so it falls quickly when synthesis stops and is not corrected by vitamin K or distorted by its deficiency. The Paris (Beaujon–Paul Brousse) group derived it in hepatitis B failure. EASL 2017 prints the age split as under 30 / over 30; the card’s note that your notes print ‘any age’ is about the source, not an error in the card."),
    ('b', "**Arterial phosphate above 1.2 mmol/L, paracetamol.** Measured on day 2–3 after the overdose. A regenerating liver takes up phosphate to make ATP and nucleic acids, so the level falls; a high phosphate means no regeneration (and often renal failure). EASL quotes sensitivity 89%, specificity 100% from the original series."),
    ('c', "**Arterial lactate above 3.5 mmol/L, paracetamol.** EASL 2017: above 3.5 on admission or above 3.0 after fluid resuscitation (sensitivity 81%, specificity 95%). A necrotic liver cannot clear lactate and may produce it; adding lactate to King’s (the modified criteria) identifies deaths earlier."),
    ('d', "**Arterial ammonia above 150–200 µmol/L, mixed causes.** It predicts cerebral oedema and herniation rather than liver recovery as such: above 200 is strongly linked to herniation, and above 150 is the level SCCM 2023 uses to call for hypertonic saline and plasma exchange (ALF-41)."),
    ('e', "**APACHE II above 15 and MELD above 33, paracetamol.** Both are general severity scores tested in paracetamol failure. MELD (bilirubin, INR, creatinine) above 33 at the onset of encephalopathy is the EASL figure (above 32 in non-paracetamol); ACG 2023 accepts King’s or MELD and treats MELD above 25 as high risk."),
    ('f', "**Liver biopsy necrosis above 70%, mixed; factor VIII/V ratio above 30, paracetamol.** Extensive necrosis on a transjugular biopsy means too little liver is left to regenerate, but sampling error limits it; its practical use is to exclude malignant infiltration. Factor VIII is made outside the hepatocyte (endothelium) and rises as an acute-phase protein, while factor V falls, so a high ratio marks severe hepatocyte failure."),
  ],
  mimic=[
    ("Ammonia vs King’s criteria", "Ammonia predicts the brain (oedema, herniation) and drives ICU treatment; King’s predicts death without transplant and drives listing."),
  ],
  traps=[
    ("“APACHE II, SOFA or Child-Pugh for a paracetamol overdose” (DocT QBank, MELD keyed, 45% right)", "King’s College is the standard; among the offered options MELD is the least wrong, because it is liver-specific and ACG 2023 endorses it as an alternative. Child-Pugh is for cirrhosis; APACHE II and SOFA are general ICU scores."),
    ("“Factor V under 30% is a King’s criterion”", "It is Clichy, and it applies to patients aged 30 or older; under 30 years the cut-off is 20%."),
  ],
  decode=[
    ("Paracetamol overdose, GCS 13: most appropriate score for the risk of liver failure? Options APACHE II, MELD, SOFA, Child-Pugh [DocT QBank, 45%]", "MELD (King’s if offered)."),
    ("Factor V under 20% in a 25-year-old with grade 3 HE and hepatitis B: which criteria? [pattern]", "Clichy."),
  ],
  punch="Each marker belongs to a cause: factor V and Clichy to viral failure; phosphate, lactate, APACHE II, MELD above 33 and the factor VIII/V ratio to paracetamol; ammonia predicts the brain rather than the liver. When King’s is not among the options, MELD is the liver-specific answer.",
)

L['ALF-35'] = dict(
  sub="Acute liver failure → Transplant criteria → ALFED score (AIIMS)",
  step=3,
  intro="Step 3 also has an Indian, dynamic answer to King’s. The AIIMS group (Kumar, Gut 2012) argued that a single admission value cannot tell a liver that is about to recover from one that is failing, so ALFED scores the trend over the first three days.",
  parts=[
    ('a', "**Encephalopathy persisting or progressing beyond grade 2: 2 points; arterial ammonia persisting or rising to 123 µmol/L or more: 2 points; INR persisting or rising to 5 or more: 1 point; bilirubin persisting or rising to 15 mg/dL or more: 1 point.** Encephalopathy and ammonia carry double weight because they were the strongest predictors in the derivation model, which fits a population (mostly hyperacute viral failure) in which cerebral oedema is the main killer. ‘Persisting or rising’ is the whole point: a high INR that is falling by day 3 scores nothing, because the liver is recovering."),
    ('b', "**Range 0–6. A score of 4 or more: positive predictive value 85%, negative 87%.** Derived in 244 patients and validated in 136, with an AUROC of about 0.92, better than King’s and MELD even when those were also scored serially."),
  ],
  mimic=[
    ("ALFED vs King’s College", "ALFED is dynamic (change over 3 days) and uses ammonia; King’s is static (values at presentation) and uses pH or creatinine for paracetamol and history items for other causes."),
  ],
  traps=[
    ("“ALFED is scored on admission values”", "It is scored on persistence or rise over the first 3 days (ALF-43h)."),
  ],
  decode=[
    ("A dynamic AIIMS score using ammonia, bilirubin, INR and HE over 3 days, and the cut-off that predicts death? [pattern]", "ALFED; 4 or more."),
  ],
  punch="ALFED asks whether the liver is getting better or worse over three days, not how bad it looked on arrival, and a score of 4 or more out of 6 predicts death without transplant.",
)

L['ALF-36'] = dict(
  sub="Acute liver failure → Transplant criteria → ALFED risk groups and older AIIMS indicators",
  step=3,
  intro="Step 3 ends with what the ALFED score means at the bedside, and with the older AIIMS model it replaced. Both come from Indian cohorts in which viral, hyperacute failure and cerebral oedema dominate.",
  parts=[
    ('a', "**ALFED 0–1 low risk, mortality about 3%; 2–3 moderate, 29–37%; 4–6 high, 80–96%.** The ranges are the derivation and validation cohorts of Kumar 2012 (later Indian papers quote about 2.6%, 33% and 88.5%). Mortality climbs steeply with each point, which is why 4 is the cut-off for early transplant evaluation; a low score lets the team wait for recovery."),
    ('b', "**Older adverse indicators at admission: age over 40, cerebral oedema, bilirubin above 15 mg/dL, prothrombin time prolonged by more than 25 seconds.** From 423 AIIMS patients (Acharya 1996): with three or more present, 93% died. In that cohort cause and speed of onset did not change outcome, unlike Western series, which is why the AIIMS models are built on physiology, not aetiology."),
  ],
  mimic=[
    ("AIIMS 1996 indicators vs ALFED", "The 1996 indicators are admission values; ALFED scores their change over 3 days."),
  ],
  traps=[
    ("“One adverse AIIMS indicator predicts death”", "The model needs three or more of the four."),
  ],
  decode=[
    ("ALFED score 5: risk group and approximate mortality? [pattern]", "High risk, about 80–96%."),
  ],
  punch="An ALFED of 4 or more puts mortality above 80%, while 0–1 is about 3%; the older AIIMS rule needed three of age over 40, cerebral oedema, bilirubin above 15 and a PT prolonged by more than 25 seconds.",
)

L['ALF-37'] = dict(
  sub="Acute liver failure → Liver support → Biological vs non-biological devices",
  step=4,
  intro="Step 4 is the attempt to buy time with a machine. The liver has two jobs a machine could copy: detoxification (clearing ammonia, bilirubin, bile acids and cytokines, many bound to albumin) and synthesis. Non-biological devices only detoxify; biological ones add living hepatocytes in the hope of synthesis too.",
  parts=[
    ('a', "**Principle: biological = hepatocytes in a bioreactor; non-biological = artificial detoxification.** Ordinary dialysis cannot remove albumin-bound toxins, so non-biological devices use albumin as the dialysate or adsorbent columns to strip them (ALF-39)."),
    ('b', "**Devices: biological BAL (HepatAssist), ELAD, BLSS; non-biological MARS, Prometheus, SPAD, plasmapheresis, charcoal haemoperfusion.** Plasmapheresis is grouped with the non-biological methods, but it is the one with positive trials (ALF-41)."),
    ('c', "**Risk: biological — infection, zoonosis; non-biological — infection, bio-incompatibility.** Porcine cells carry the theoretical risk of porcine endogenous retrovirus; extracorporeal circuits activate platelets and complement and need anticoagulation in a coagulopathic patient."),
  ],
  mimic=[
    ("Liver support device vs plasma exchange", "Devices remove toxins but none has improved survival; plasma exchange removes toxins and replaces deficient plasma proteins, and improves transplant-free survival."),
  ],
  traps=[
    ("“Liver assist devices are an established bridge that improves survival”", "EASL 2017: use them only within trials; SCCM 2023 leaves them as an option equal to standard care. Transplant remains the treatment."),
  ],
  decode=[
    ("Which of these is a bioartificial (cell-based) liver support device: MARS, Prometheus, ELAD, SPAD? [pattern]", "ELAD."),
  ],
  punch="Biological devices carry hepatocytes, non-biological ones only clear albumin-bound toxins, and neither kind has yet saved lives in a trial.",
)

L['ALF-38'] = dict(
  sub="Acute liver failure → Liver support → Device, cell source and adverse effects",
  step=4,
  intro="Step 4 continues with what each device is made of, because the cell source is what examiners pair with the risk.",
  parts=[
    ('a', "**MARS: no cells; coagulopathy, DIC.** The circuit and adsorber columns consume platelets (the most consistent finding is a fall in platelet count) in a patient who already bleeds easily."),
    ('b', "**Prometheus: no cells; hypotension, low albumin and white cells.** Fractionated plasma separation and adsorption: the patient’s own albumin fraction is filtered off and passed over adsorbers; the extracorporeal volume and blood–membrane contact explain the hypotension and leucopenia."),
    ('c', "**HepatAssist (BAL): porcine hepatocytes; no substantial adverse effects.** Pig hepatocytes plus a charcoal column; safe in its trial but with the theoretical zoonosis risk."),
    ('d', "**ELAD: human C3A hepatoma line; thrombocytopenia, hypotension.** C3A is a subclone of the HepG2 hepatoblastoma line; human cells avoid zoonosis."),
    ('e', "**BLSS: porcine hepatocytes; hyper- or hypotension.**"),
  ],
  mimic=[
    ("HepatAssist and BLSS vs ELAD", "HepatAssist and BLSS use pig cells (zoonosis risk); ELAD uses a human hepatoma line."),
  ],
  traps=[
    ("“ELAD uses porcine hepatocytes”", "It uses human C3A hepatoma cells (ALF-43i)."),
  ],
  decode=[
    ("Which liver support device uses a human hepatoblastoma-derived cell line? [pattern]", "ELAD."),
  ],
  punch="Pig cells mean HepatAssist or BLSS and a zoonosis risk; human hepatoma cells mean ELAD; MARS and Prometheus have no cells and cost platelets and blood pressure.",
)

L['ALF-39'] = dict(
  sub="Acute liver failure → Liver support → MARS vs SPAD",
  step=4,
  intro="Step 4 then compares the two albumin dialysis systems. Both rest on one idea: toxins bound to albumin will move across a membrane to fresh albumin on the other side, which ordinary dialysis cannot achieve.",
  parts=[
    ('a', "**MARS = Molecular Adsorbent Recirculating System; SPAD = Single-Pass Albumin Dialysis.**"),
    ('b', "**Albumin: MARS 20%, recirculated; SPAD dilute, counter-current, discarded after one pass.** MARS has to clean its albumin to reuse it; SPAD simply throws it away, using about 4% albumin."),
    ('c', "**Regeneration: MARS charcoal and anion-exchange columns, then a dialyser; SPAD none.** The columns strip bound toxins from the albumin, and the dialyser removes water-soluble ones (ammonia, urea, creatinine)."),
    ('d', "**Circuits: MARS three (blood, albumin, dialysate); SPAD a standard CRRT machine.**"),
    ('e', "**Clearance: MARS improves encephalopathy, renal function, haemodynamics; SPAD ammonia and bilirubin clearance similar or better, and cheaper.** In vitro (Sauer 2004) the two matched; in a crossover in patients (2016) bilirubin removal was similar, MARS removed more bile acids and creatinine because of its higher dialysate flow, platelets fell only with MARS, and SPAD cost about €1500 less per session."),
  ],
  mimic=[
    ("Albumin dialysis vs CRRT", "CRRT removes water-soluble molecules only; albumin dialysis also removes albumin-bound bilirubin and bile acids."),
  ],
  traps=[
    ("“SPAD needs a special three-circuit machine”", "That is MARS; SPAD runs on a standard CRRT machine with albumin added to the dialysate."),
  ],
  decode=[
    ("Albumin dialysis in which the albumin is regenerated over charcoal and anion-exchange columns? [pattern]", "MARS."),
  ],
  punch="MARS recirculates 20% albumin and cleans it; SPAD uses dilute albumin once and throws it away, on an ordinary CRRT machine, at lower cost and similar bilirubin clearance.",
)

L['ALF-40'] = dict(
  sub="Acute liver failure → Liver support → Device trials",
  step=4,
  intro="Step 4 closes with the evidence, which is the reason guidelines do not recommend these devices. Trials in ALF are hard to run: patients are few, and many are transplanted within hours, before a device could make a difference.",
  parts=[
    ('a', "**HepatAssist: randomised, 147 patients, 20 centres (USA, Europe); no difference in 30-day survival; safe.** The trial randomised 171; 147 is the group left after excluding primary graft non-function. Overall 30-day survival was 71% vs 62% (P 0.26). Only an adjusted subgroup analysis of fulminant and subfulminant failure reached significance (risk ratio 0.56, P 0.048), which is hypothesis-generating, not proof."),
    ('b', "**ELAD: 24 patients; no difference in 30-day survival.** Too small to show anything; later larger ELAD trials in alcoholic hepatitis were also negative."),
    ('c', "**MARS (French trial): 102 patients, 16 transplant centres; 6-month survival in paracetamol cases 85.0% vs 68.4%, P = 0.46.** FULMAR: overall 6-month survival 84.9% vs 75.5% (P 0.28). Two-thirds of patients were transplanted, at a median of 16 hours after randomisation, so many received little or no MARS; the trial could not answer its question."),
  ],
  mimic=[
    ("FULMAR (MARS) vs Larsen (plasma exchange)", "FULMAR was neutral, its effect diluted by early transplant; Larsen showed better survival with high-volume plasma exchange (ALF-41)."),
  ],
  traps=[
    ("“MARS improved survival in paracetamol ALF (85% vs 68%)”", "The difference was not significant (P 0.46), and early transplantation confounded the trial."),
  ],
  decode=[
    ("Randomised trial of MARS in ALF (FULMAR): result? [pattern]", "No significant survival difference; most patients were transplanted within a day."),
  ],
  punch="Every device trial in ALF was neutral or too small, the MARS trial largely because patients were transplanted before treatment could act; that is why devices stay inside trials.",
)

L['ALF-41'] = dict(
  sub="Acute liver failure → Liver support → Plasma exchange",
  step=5,
  intro="Step 5 is the exception. Plasma exchange does two things a device cannot: it removes toxins, cytokines and damage signals, and it replaces the clotting factors and other proteins the failing liver no longer makes, with fresh frozen plasma.",
  parts=[
    ('a', "**High-volume plasma exchange: open randomised trial; improved transplant-free survival; dampens innate immune activation and multi-organ dysfunction.** Larsen (J Hepatol 2016, 182 patients): hospital survival 58.7% vs 47.8% (hazard ratio 0.56). The benefit was in patients who were not transplanted; used only as a bridge before transplant it did not improve post-transplant survival. SIRS and SOFA scores fell, which supports the anti-inflammatory mechanism."),
    ('b', "**Standard-volume plasma exchange (2022): 40 patients, 1:1; transplant-free survival 75% vs 45% (hazard ratio 0.30); by day 5 better lactate clearance, less SIRS (84% vs 26% resolution), lower ammonia and SOFA.** Maiwall (AIIMS/ILBS Delhi, Clin Gastroenterol Hepatol 2022), at 21 days, in ALF with cerebral oedema, mostly viral and hyperacute. Smaller volumes were tested because high volumes risk fluid overload and worse brain swelling; about 2 sessions were needed."),
    ('c', "**High volume: about 15% of ideal body weight (8–12 L) a day for 3 days. Standard: 1.5–2 plasma volumes.** For a 70-kg ideal weight, 15% is about 10 L; one plasma volume is roughly 40 mL/kg, so standard volume is about 4–6 L per session (the 2022 trial confirmed 1.5–2.0 plasma volumes)."),
  ],
  mimic=[
    ("Plasma exchange vs albumin dialysis", "Plasma exchange replaces plasma proteins and has positive trials; albumin dialysis only removes bound toxins and has none."),
  ],
  traps=[
    ("“Plasma exchange improves survival after transplant when used as a bridge”", "In Larsen it improved survival in those not transplanted; it did not change post-transplant survival."),
  ],
  decode=[
    ("Which extracorporeal therapy improves transplant-free survival in ALF in a randomised trial? [pattern]", "High-volume plasma exchange (Larsen 2016); standard volume also, in a small Indian trial."),
    ("Indication for plasma exchange in ALF according to SCCM 2023? [pattern]", "Suggested, where available, in critically ill ALF with hyperammonaemia above 150 µmol/L (conditional)."),
  ],
  punch="Plasma exchange removes the inflammatory and toxic load and replaces what the liver cannot make; it is the only extracorporeal therapy with randomised survival benefit, and EASL and SCCM both support it.",
)

L['ALF-42'] = dict(
  sub="Acute liver failure → Sweep → Take-home list",
  step=6,
  intro="Step 6 sweeps the three ALF decks for an Indian exam. The list joins definition (GI01A), management (GI01B) and the transplant and device evidence of this deck.",
  parts=[
    ('a', "**The IASL definition is the clinically relevant one in India; hepatitis E is the major cause.** The IASL scheme times encephalopathy from the onset of jaundice (within 4 weeks for ALF), which fits Indian patients, who present with jaundice and are mostly viral (GI01A). Hepatitis E dominates the cases once labelled non-A non-B, and carries a particular risk in pregnancy."),
    ('b', "**Anti-tubercular drug liver failure has high mortality.** Idiosyncratic drug injury regenerates poorly; in the AIIMS series (Kumar 2010: 70 of 1223 ALF patients) 67% died, and bilirubin, prothrombin time and grade 3–4 encephalopathy at presentation predicted death, which is why ATT-induced failure needs early referral."),
    ('c', "**Manage aggressively in ICU; identify transplant candidates early; cerebral oedema and infection are the major killers; liver assist devices have not shown great results.** Each line maps to a step: listing early (step 1), the criteria (steps 2–3), brain protection and infection surveillance (GI01B), and the device trials (step 4)."),
  ],
  mimic=[
    ("India vs the West", "In India ALF is mostly viral (hepatitis E, B) and ATT-induced; in the West, paracetamol leads."),
  ],
  traps=[
    ("“Paracetamol is the commonest cause of ALF in India”", "It is the commonest in the UK and USA; in India it is hepatitis E (and other viruses), then drugs such as ATT."),
  ],
  decode=[
    ("Commonest cause of acute liver failure in India? [pattern]", "Hepatitis E."),
  ],
  punch="In India ALF is viral, mainly hepatitis E, ATT failure is especially lethal, and patients die of cerebral oedema and infection; manage them in ICU, find transplant candidates early, and expect little from devices.",
)

L['ALF-43'] = dict(
  sub="Acute liver failure → Sweep → True or false",
  step=6,
  intro="Step 6 ends with the statements most often turned into true/false items: four brain measures that failed in trials, an ammonia drug that failed, and three criteria and device facts that are easy to swap.",
  parts=[
    ('a', "**False: ICP monitoring does not improve survival; bleeding in 10.3%.** Monitors are placed through the skull in coagulopathic patients: in the US ALFSG survey (Vaquero 2005) intracranial haemorrhage occurred in 10.3% of 58 monitored patients, half of them incidental on imaging, and it may have contributed to 2 deaths; 30-day post-transplant survival was 85% with or without a monitor (7% haemorrhage in the later ALFSG cohort). In ALFSG data (Karvellas 2014) 21-day mortality did not differ, and was higher with monitoring in non-paracetamol ALF. SCCM 2023 suggests not using invasive ICP monitoring; EASL 2017 still allows it in grade 3–4 with high-risk features."),
    ('b', "**True: mannitol can paradoxically raise ICP.** If the blood–brain barrier is disrupted, or doses are repeated with renal failure, mannitol enters the brain and reverses the osmotic gradient, pulling water back in."),
    ('c', "**False: prophylactic hyperventilation does not prevent cerebral oedema.** It lowers ICP briefly by cerebral vasoconstriction, but the effect fades as CSF bicarbonate readjusts and the vasoconstriction risks ischaemia; in the controlled trial (Ede 1986) it did not reduce cerebral oedema or improve survival. It is kept as a short rescue for surges (EASL)."),
    ('d', "**False: prophylactic phenytoin is not proven.** Bhatia (2004, 42 patients): no difference in seizures, cerebral oedema or survival; EASL says prophylactic antiepileptics are not warranted."),
    ('e', "**False: LOLA does not lower ammonia in acute liver failure.** Acharya (2009, 201 patients): ammonia fell equally with placebo, and mortality was not lower (42% vs 33%, not significant). LOLA works by feeding the urea cycle and glutamine synthesis; with massive hepatocyte loss the urea cycle cannot respond, and glutamine made in muscle is broken back down to ammonia by glutaminase in gut and kidney."),
    ('f', "**False: arterial pH is a King’s criterion only in paracetamol failure.**"),
    ('g', "**True: Clichy criteria use factor V.**"),
    ('h', "**False: ALFED is dynamic, scored over 3 days.**"),
    ('i', "**False: ELAD uses human hepatoma (C3A) cells.** Porcine cells are HepatAssist and BLSS (ALF-38)."),
  ],
  mimic=[
    ("Prophylactic vs rescue brain measures", "Hyperventilation and osmotherapy are rescues for ICP surges; as prophylaxis, hyperventilation and phenytoin failed. Hypertonic saline to sodium 145–155 is the one measure used to prevent intracranial hypertension in high-risk patients."),
  ],
  traps=[
    ("“LOLA, effective in cirrhotic encephalopathy, also lowers ammonia in ALF”", "Not in ALF: the randomised trial showed no fall in ammonia and no survival gain."),
  ],
  decode=[
    ("Which intervention has shown no benefit in ALF: prophylactic phenytoin, LOLA, prophylactic hyperventilation, ICP monitoring? [pattern]", "All four; plasma exchange and hypertonic saline are the ones with support."),
  ],
  punch="In ALF, ICP monitoring, prophylactic hyperventilation, prophylactic phenytoin and LOLA have all failed in trials; pH belongs to paracetamol King’s, factor V to Clichy, the 3-day trend to ALFED, and human hepatoma cells to ELAD.",
)

FLAGS = {
  'ALF-40': "a: HepatAssist randomised 171 patients (11 US + 9 European sites); 147 is the subgroup after excluding primary non-function. ‘No difference in 30-day survival’ is right overall (71% vs 62%, P 0.26), but an adjusted analysis in fulminant/subfulminant failure showed benefit (RR 0.56, P 0.048). The explanation states both.",
  'ALF-41': "Watch line ‘ACG 2023: evidence still insufficient’ could not be checked against the ACG text (second check on 20 Nov 2026: the full guideline is paywalled, and the ACG grand-round slides, Healio, MDedge and Guideline Central summaries do not mention plasma exchange at all); EASL 2017 (I, 1) and SCCM 2023 (conditional) both support plasma exchange. b: the 2022 trial enrolled ALF with cerebral oedema, and its outcome was 21-day transplant-free survival; the card does not say so, the explanation does.",
  'ALF-32': "Marrow key (transplant evaluation for fulminant Budd–Chiari despite colon cancer 2 months earlier) conflicts with c (extrahepatic malignancy contraindicates); the trap gives the card-layer rule. Watch line ‘two-thirds of deaths occur within 72 hours’: the AIIMS series (Acharya 1996, n 423) reports that about 75% of those who died did so within 72 hours; two-thirds (66%) was the overall mortality, the likely source of the mix-up.",
}
