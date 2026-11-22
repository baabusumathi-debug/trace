# HY5 — Explain v3 ("Learn" depth): high yield haematology and transfusion (ROTEM/TEG, thresholds, damage-control resuscitation, transfusion reactions, haematology one-liners),
# endocrine emergencies (adrenal crisis, thyroid storm, adult DKA, glucose targets), obstetric critical care (physiology, eclampsia, magnesium toxicity, HELLP and fatty liver,
# antepartum and postpartum haemorrhage, amniotic fluid embolism, early-pregnancy decisions, one-liners) and a true/false sweep. No mnemonics or hooks.
# Driven by qpack/HY5.md (118 question links; HEO-02 thresholds asked 21 times, HEO-01 ROTEM/TEG 11, HEO-13 HELLP/AFLP 10, HEO-03 damage control, HEO-04 TRALI/TACO and HEO-15 PPH 9 each).
# Every card has at least one linked question; HEO-06, -09, -10, -17, -18 and -19 have one or two and get shorter explanations.
# Card layer (endo_cardlayer.json "HY5|<code>") lines and Crossfire lines read and agreed with (HEO-02 GT7 6 g/dL key, HEO-04 GrandT1 type II key and AIM2 fat-embolism stem,
# HEO-08 Marrow transition option, HEO-14 previa key). No `fix` entries for HY5 in trace/test/data/qbank.json (checked 22 Nov 2026). No Top-up cards for HY5.
# Checked online on 22 Nov 2026:
#  - ADA/EASD/JBDS/AACE/DTS hyperglycaemic crises consensus 2024 (Umpierrez, Diabetes Care 2024; CCJM 2025 summary): insulin postponed until potassium is above 3.5 mmol/L (10 mmol/h
#    K if below 3.5); fixed-rate 0.1 U/kg/h (HHS 0.05); add 5–10% dextrose once glucose is below 250 mg/dL and keep glucose around 200; bicarbonate only for pH below 7.0; basal SC insulin
#    1–2 h before stopping the infusion; DKA = glucose ≥200 (or known diabetes), β-hydroxybutyrate ≥3.0, pH <7.3 and/or bicarbonate <18; HHS glucose drop not to exceed 90–120 mg/dL/h.
#  - ISBT 2018 TACO surveillance definition (SHOT TACO chapter, checked 22 Nov 2026 in review): onset during or up to 12 h after transfusion (SHOT still accepts up to 24 h); A acute or
#    worsening respiratory compromise and/or B pulmonary oedema, and a total of ≥3 of A–E (C cardiovascular change: tachycardia, hypertension, JVD, enlarged heart, peripheral oedema;
#    D fluid overload: positive balance or response to diuretic; E BNP/NT-proBNP >1.5× pre-transfusion); pyrexia does not exclude TACO.
#  - AABB/ICTMG platelet transfusion guideline 2025 (AABB news release, 29 May 2025): <10 × 10³/µL for hypoproliferative thrombocytopenia from chemotherapy/allogeneic SCT (strong);
#    no routine prophylaxis in stable chronic hypoproliferative states (autologous SCT, aplastic anaemia; conditional); LP <20; CVC at compressible sites <10; IR <20 low-risk, <50 high-risk;
#    major non-neuraxial surgery <50; no prophylactic platelets for cardiac surgery without thrombocytopenia or for non-operative ICH with platelets >100. No neurosurgery figure given.
#  - ACOG 2024 Clinical Practice Update (PubMed 39255498; ebmedicine, UMEM, ASRM summaries): may forgo Rh testing and RhIg for abortion or pregnancy loss before 12+0 weeks; none of
#    these sources mentions ectopic pregnancy. NICE NG126 (current online text, checked in review): do not offer anti-D for ectopic pregnancy or miscarriage up to 11+6 weeks; offer
#    ≥250 IU (50 µg) at 12+0–12+6 weeks with medical or surgical management.
#  - Review, 22 Nov 2026: JTA 2016 full text (Endocr J 63:1025): either MMI or PTU; inorganic iodide simultaneously with the antithyroid drug; hydrocortisone 300 mg/day or dexamethasone
#    8 mg/day; β1-selective blockers (landiolol, esmolol, bisoprolol) first, propranolol not recommended for the tachycardia; paracetamol, no aspirin. ATA 2016 Table 7: PTU 500–1000 mg
#    then 250 mg 4-hourly (preferred in storm), methimazole 60–80 mg/day, propranolol 60–80 mg 4-hourly, SSKI 5 drops 6-hourly not until 1 h after the antithyroid drug, hydrocortisone
#    300 mg then 100 mg 8-hourly; BWPS ≥45 storm, 25–44 impending. ADA/EASD 2024 consensus (Diabetologia full text): insulin delayed until K >3.5; dextrose at <250 mg/dL with insulin
#    reduced to 0.05 U/kg/h and glucose kept about 200; resolution ketones <0.6 with pH ≥7.3 or bicarbonate ≥18, anion gap not to be used. CRASH-2 abstract: 20,211, death 14.5 vs 16.0%
#    (RR 0.91), bleeding death 4.9 vs 5.7%, enrolled within 8 h of injury. PROPPR abstract: 680, 24-h 12.7 vs 17.0% (P=.12), 30-day 22.4 vs 26.1% (P=.26), exsanguination 9.2 vs 14.6%
#    (P=.03). MINT (ACC summary): 3,504, primary 16.9 vs 14.5%, RR 1.15 (0.99–1.34), P=.07. ACOG CO 831 (2021): praevia 36+0–37+6, accreta 34+0–35+6, no separate bleeding rule;
#    RCOG GTG 27a (2018, via NHS summary): praevia with bleeding 34+0–36+6, uncomplicated 36+0–37+0. AABB/ICTMG 2025 news release: figures below confirmed.
# Carried from earlier decks’ online checks (OBS02A header, 12 Nov 2026): ACOG PB 222 magnesium 4–6 g over 20–30 min then 1–2 g/h to 24 h postpartum, recurrent seizure 2–4 g over 5 min,
#    severe BP ≥160/110 persisting 15 min treated within 30–60 min, toxicity at about 7 / 10 / 25 mEq/L, calcium gluconate 1 g IV; Tennessee HELLP LDH ≥600, AST ≥70, platelets ≤100,000.
# From standard references without a fresh check (confident unless said): CRASH-2 (Lancet 2010/2011: 20,211 patients, death 14.5 vs 16.0%, bleeding death worse if TXA given after 3 h);
# PROPPR (JAMA 2015: 1:1:1 vs 1:1:2, no 24-h or 30-day mortality difference, fewer exsanguination deaths at 24 h); European trauma bleeding guideline 2023 (SBP 80–90 / MAP 50–60 without TBI,
# MAP ≥80 with severe TBI, fibrinogen ≤1.5 g/L trigger); ISBT 2019 TRALI type I/II (Vlaar 2019); TRICC, TRISS, Villanueva 2013, TRIGGER, MINT 2023 (trend to harm with restrictive
# transfusion in acute MI, RR 1.15, not significant); AABB 2023 red cell guideline (7; 7.5 cardiac surgery; 8 orthopaedic surgery or pre-existing cardiovascular disease);
# Endocrine Society 2016 adrenal insufficiency; SSC 2021 (hydrocortisone 200 mg/day for noradrenaline ≥0.25 µg/kg/min for ≥4 h); ATA 2016 and JTA 2016 thyroid storm; NICE-SUGAR 2009
# (90-day mortality 27.5 vs 24.9%); ADA Standards perioperative 100–180 mg/dL; ACR contrast manual (metformin); AHA maternal arrest (hysterotomy by 4–5 min); WOMAN trial (2017);
# RCOG GTG 52 and WHO PPH doses; SMFM 2016 AFE guideline and Clark 2016 research criteria; ATS 2011 PE in pregnancy (normal CXR → V/Q); ESC 2019 (pregnancy-adapted D-dimer
# algorithms); IDSA 2019 bacteriuria (4–7 days); ACOG CO 712 intra-amniotic infection; neulasta label (not within 14 days before
# to 24 h after chemotherapy); NHLBI 2014 sickle cell (acute chest syndrome).

SPINE = [
  ("Reading the bleeding patient", "A viscoelastic test shows which part of clotting has failed, starting time for factors, firmness for fibrinogen and platelets, lysis for fibrinolysis, so each channel points to one product."),
  ("Giving blood without harm", "Transfuse to the lowest safe threshold, resuscitate bleeding trauma with low pressure and balanced products plus early TXA, and recognise when the transfusion itself is the injury."),
  ("Haematology diagnoses that change treatment", "Acute chest syndrome, G6PD haemolysis, HIT and TTP each have one treatment that saves the patient and one reflex, usually platelets or the wrong antidote, that harms them."),
  ("Hormone emergencies: replace or block", "Adrenal crisis needs cortisol at once, thyroid storm needs synthesis blocked before iodine closes release, and DKA needs insulin until the ketones clear, not until the glucose falls."),
  ("Pregnancy changes the baseline", "Normal pregnancy lowers PaCO2, raises fibrinogen and shrinks the oxygen reserve, so numbers that look normal can mean danger, and eclampsia, magnesium and the liver crises follow from a sick placenta."),
  ("Obstetric bleeding and collapse", "Abruption and amniotic fluid embolism consume fibrinogen, atony is treated with a ladder of uterotonics chosen by contraindication, and delivery or emptying the uterus ends most of these crises."),
]

PRIMER = "Clotting has three phases that the tests in this deck separate: starting (clotting factors, measured as a time), building a firm clot (fibrinogen plus platelets, measured as a strength or amplitude) and breaking it down (fibrinolysis, measured as lysis). Bleeding patients lose all three at once through consumption, dilution by crystalloid, hypothermia and acidosis, so modern resuscitation replaces like with like and early. Pregnancy shifts the baseline: fibrinogen rises to about 4–6 g/L, PaCO2 falls to about 30 mmHg and functional residual capacity falls, so obstetric thresholds are set higher and desaturation comes faster. The endocrine emergencies here are diseases of one missing or excessive hormone, and each treatment works by replacing it or blocking its effect in the right order."

L = {}

L['HEO-01'] = dict(
  sub="Haematology → Bleeding → ROTEM and TEG channels",
  step=1,
  intro="Step 1 is reading the bleeding patient before choosing a product, and this card is the key to the whole deck. ROTEM and TEG put a drop of whole blood in a rotating cup and draw how fast a clot starts, how strong it gets and whether it dissolves. Eleven linked questions, most of them in TEG language (R, K, α, MA, LY30), test whether you can translate each abnormality into one product; the one most missed (47%) was a low MA with everything else normal.",
  parts=[
    ('a', "**EXTEM CT long (extrinsic) → low clotting factors → FFP or 4F-PCC.** EXTEM is started by tissue factor, so its clotting time measures the extrinsic and common pathway factors, the ones warfarin and dilution deplete. In TEG the equivalent is a long R time, which DocT keys as ‘delayed clot formation’ (94% and 81% right); a short R means hypercoagulability."),
    ('b', "**INTEM CT long, HEPTEM normal → heparin effect → protamine.** INTEM is contact-activated and so sensitive to heparin; HEPTEM is the same test with heparinase added. If adding heparinase corrects the time, heparin caused it. After cardiac bypass this is the residual-heparin pattern. Conversely, a normal R with normal PT and aPTT (GT1o) rules heparin out, so protamine is wrong there."),
    ('c', "**INTEM CT long and HEPTEM also long → low intrinsic factors → FFP.** Heparinase does not fix a factor deficiency, so both channels stay long. The card’s watch line is this point: with no heparin in the picture, a long INTEM CT means factors, and the answer is FFP (70% right; lost)."),
    ('d', "**FIBTEM A5/A10 low → low fibrinogen → cryoprecipitate or fibrinogen concentrate.** FIBTEM adds cytochalasin D, which paralyses platelets, so any firmness left comes from fibrin alone. In TEG the fibrinogen signal is a long K time and a low α angle (the speed at which the clot builds). The CGT5 trauma stem (normal R after FFP, long K, low α, preserved MA) and the CGT4 stem (FIBTEM MCF 4 mm) both key cryo or concentrate; the Marrow PPH stem with long R and long K keys plasma plus cryo."),
    ('e', "**EXTEM A5 low with FIBTEM normal → low platelet contribution → platelets.** Total firmness (EXTEM, TEG MA) is fibrin plus platelets; if the fibrin-only channel is normal, the missing strength is platelets. This is the GT1o post-valve stem (MA 37 mm with normal R, K and angle, 47% right) and the NEET 2025 recall (cirrhotic trauma, low MA): give platelets. A low MA reflects platelet function as well as number, which is why it is the test for dysfunction after bypass (HEO-19)."),
    ('f', "**Maximum lysis above 15% → hyperfibrinolysis → tranexamic acid.** The clot forms and then falls apart. The TEG equivalent is LY30: DocT lines use above 7.5% (the classic TEG cut-off) or above 3% (the lower trauma cut-off); either way a high lysis value means TXA (GT3, 73%). Most trauma patients, though, arrive in fibrinolytic shutdown rather than hyperfibrinolysis."),
  ],
  table=dict(title="ROTEM and TEG say the same thing", head=["What failed", "ROTEM", "TEG", "Give"], rows=[["Clotting factors", "EXTEM/INTEM CT long", "R long", "**FFP / PCC**"], ["Heparin", "INTEM CT long, HEPTEM normal", "R long, corrected with heparinase cup", "**protamine**"], ["Fibrinogen", "FIBTEM A5/MCF low", "K long, α low", "**cryo / fibrinogen concentrate**"], ["Platelets", "EXTEM A5/MCF low, FIBTEM normal", "MA low, R/K/α normal", "**platelets**"], ["Fibrinolysis", "ML >15%", "LY30 >7.5% (trauma >3%)", "**tranexamic acid**"]]),
  mimic=[
    ("Low MA from platelets vs low MA from fibrinogen", "MA (or EXTEM MCF) is the sum of both. A normal K and α angle (TEG) or a normal FIBTEM (ROTEM) leaves platelets as the cause; a low FIBTEM means fibrinogen first."),
    ("Heparin vs factor deficiency", "Both lengthen INTEM CT or TEG R. Heparinase correction (HEPTEM normal) means heparin; no correction means factors."),
    ("Viscoelastic test vs PT/INR", "PT and INR take 30–60 minutes, measure plasma only and miss fibrinogen, platelets and lysis; TEG/ROTEM give results in minutes on whole blood (GT3, 100%)."),
  ],
  traps=[
    ("“Protamine” for a low MA after bypass", "Heparin lengthens R, not MA. With protamine already given and normal R, PT and aPTT, the low MA is platelets (GT1o, 47% right)."),
    ("“Fibrinogen” for a low MA with a normal α angle", "A normal K and α say fibrin builds normally; the weak clot is platelets. Cryo is for a long K or low α."),
    ("“Increased fibrinolysis is most linked to death in trauma coagulopathy”", "Low clot strength (MA, MCF, A5) is the VHA variable most consistently linked to death and massive transfusion; most patients are in shutdown, and INR is not a viscoelastic variable (GT2, 38% right)."),
    ("“Additional FFP” when bleeding continues after FFP with a long K", "FFP has already corrected R; the remaining defect is fibrinogen, and FFP carries too little of it. Give cryo (CGT5)."),
    ("Low MCF in PPH read as hyperfibrinolysis", "A normal CT and CFT with a low MCF is a firmness problem; lysis shows as a falling trace after the maximum. DocT keys platelet dysfunction (CGT5); in a real PPH check FIBTEM, because fibrinogen falls first."),
  ],
  decode=[
    ("Persistent drain output after AVR; PT, aPTT, R, K, α normal, MA 37 mm — treat with? [DocT GT]", "Platelets: isolated low MA."),
    ("Trauma, ROTEM FIBTEM MCF 4 mm, EXTEM CT long and MCF low, oozing — targeted therapy? [DocT GT]", "Fibrinogen concentrate or cryo first; the fibrin channel explains the low EXTEM firmness."),
    ("Chronic liver disease, abdominal trauma, hypotension, TEG shows decreased MA [NEET 2025]", "Platelet transfusion."),
    ("Trauma, prolonged PT/PTT, TEG hyperfibrinolysis, weak clot, normal platelets [DocT GT]", "Tranexamic acid."),
  ],
  punch="Time is factors (FFP or PCC, protamine if heparinase corrects it), the fibrin-only channel or the K and α angle is fibrinogen (cryo), low firmness with normal fibrin is platelets, and lysis is TXA.",
)

L['HEO-02'] = dict(
  sub="Haematology → Transfusion → Red cell, platelet and fibrinogen thresholds",
  step=2,
  intro="Step 2 is giving blood without causing harm, and the first rule is to transfuse only below a proven threshold. This is the most-asked card in the deck (21 linked questions): the red cell trigger in sepsis, GI bleeding and stable ICU patients, platelet counts for procedures, and fibrinogen in DIC and abruption. The two traps that cost marks were letting lactate, vasopressors or coronary disease push the Hb trigger up, and giving platelets when fibrinogen was the missing part.",
  parts=[
    ('a', "**Hb 7 g/dL (restrictive); higher (~8) in active cardiac ischaemia.** TRICC (general ICU), TRISS (septic shock) and Villanueva (upper GI bleeding) all found 7 at least as safe as 9–10, and in variceal bleeding the liberal arm did worse because extra volume raises portal pressure. Vasopressors, a lactate of 3 and stable coronary disease do not change the trigger (several DocT keys, 80–100% right). AABB 2023 uses 7.5 for cardiac surgery and 8 for orthopaedic surgery or pre-existing cardiovascular disease; TRIGGER tested 8 vs 10 in upper GI bleeding, and the DocT TRIGGER stem keys 8. In acute myocardial infarction MINT (2023) showed a non-significant trend favouring a liberal target, which is why active ischaemia is the exception."),
    ('b', "**Below 10 prophylactic; below 50 for surgery or active bleeding; below 100 for neurosurgery or intracranial bleeding.** Spontaneous bleeding is rare above 10, so 10 is the prophylactic line in marrow failure from chemotherapy (GT8: platelets 6,000, transfuse, 69% right). Surgery and active bleeding need 50 (laparotomy stem 45% right; haematemesis with 38,000 → transfuse to above 50; caesarean in HELLP below 50, 69% right). The closed skull tolerates no bleed, hence 100 for neurosurgery (BSH; AABB 2025 gives no neurosurgery figure and advises against platelets in non-operative ICH with counts above 100). AABB 2025 adds LP below 20 and CVC below 10."),
    ('c', "**Below 1.5 g/L (below 2 g/L in obstetric haemorrhage) → cryo or fibrinogen concentrate.** Fibrinogen is the first factor to fall to critical levels in bleeding. FFP contains fibrinogen at about plasma concentration, so it cannot raise a low level quickly without large volumes; cryo and concentrate are concentrated. Pregnancy raises fibrinogen to 4–6 g/L, so a ‘normal’ 2 g/L in PPH already means heavy consumption. Fibrinogen 70 mg/dL in DIC (77–82%), 90 mg/dL in abruption after FFP (‘10 units of cryo or 4 g concentrate’) and neonatal afibrinogenaemia all key cryo."),
    ('d', "**Cryoprecipitate — platelets 65 are already above 50.** The bleeding patient’s platelets meet the surgical threshold; the fibrinogen of 1.2 does not. Replace the deficient component, not the one that looks low (GT4, lost)."),
  ],
  mimic=[
    ("Restrictive threshold vs ‘almost always transfuse’", "7 g/dL is the trial-based trigger; 6 g/dL is the old ASA wording for when transfusion is almost always indicated."),
    ("Low fibrinogen vs low platelets in DIC", "Both fall; the product follows the one below its threshold (fibrinogen <1.5, platelets <50 if bleeding)."),
  ],
  traps=[
    ("“Hb below 6 is where transfusion benefits” (GT7 key; 3% chose it)", "That is the old ASA statement. The restrictive trigger is 7 g/dL (TRICC, TRISS, AABB 2023). Pick 7 if offered; pick 6 only if the stem echoes ‘almost always indicated’ and 7 is absent."),
    ("“Hb 9 because of CAD and a GI bleed” (GT1o, 40% right)", "Variceal or ulcer bleeding with stable CAD: 7 is keyed; 8 is acceptable with active ischaemia; 9 raises portal pressure and rebleeding."),
    ("“Higher trigger because lactate is 3.2 and on noradrenaline”", "TRISS: 7 even in septic shock; lactate and vasopressors do not raise it (DocT QBank 80%)."),
    ("“Platelet target 100 before laparotomy” (45% right)", "Major non-neuraxial surgery needs 50; 100 is for neurosurgery."),
    ("“PFA-100 to assess platelet function after cardiac surgery” (45% right)", "PFA-100 is unreliable with haematocrit below 30% or platelets below 100 and does not guide transfusion; use TEG/ROTEM (HEO-19)."),
    ("“FFP 15 mL/kg” for fibrinogen 70", "FFP is the wrong concentrate; cryo 10 units (CGT2)."),
  ],
  decode=[
    ("Septic shock on noradrenaline, lactate 3.2, Hb 7.1 — trigger? [DocT QBank, GT6]", "Hb below 7."),
    ("Cirrhotic with prior CABG, haematemesis, Hb 7.8, platelets 76 [DocT GT]", "Transfuse for Hb below 7; platelets 76 need nothing."),
    ("Haemodynamically stable UGIB, IHD, Hb 8.1, per TRIGGER [DocT GT]", "Hb below 8: no transfusion now."),
    ("DIC with fibrinogen 70 mg/dL and bleeding [DocT GT]", "Cryoprecipitate."),
  ],
  punch="Red cells below 7 (8 with active ischaemia), platelets below 10 prophylactic, 50 for surgery or bleeding and 100 for the brain, and fibrinogen below 1.5 g/L (2 in obstetrics) means cryo, whatever else looks low.",
)

L['HEO-03'] = dict(
  sub="Haematology → Trauma → Damage-control resuscitation",
  step=2,
  intro="Step 2 continues with the bleeding trauma patient, where giving the wrong fluid at the wrong pressure kills. Damage-control resuscitation accepts a low pressure until the bleeding is controlled, replaces lost blood with blood in a ratio close to whole blood, and adds tranexamic acid early. Nine linked questions test the strategy, the ratio, TXA timing and what a positive FAST means; the worst-scored (18% and 36%) were a misprinted ratio question and TXA as an adjunct.",
  parts=[
    ('a', "**Permissive hypotension (SBP 80–90 / MAP 50–60) until bleeding is controlled; minimal crystalloid.** Raising pressure before the vessel is controlled dislodges fresh clot, and crystalloid dilutes factors, cools the patient and worsens acidosis, the lethal triad with coagulopathy. The 2023 European trauma guideline uses the same target. Crystalloid is only a small bridge until blood arrives (GT6 assertion–reason, 88%); aggressive vasopressors and immediate normotension are wrong (CGT6)."),
    ('b', "**1 : 1 : 1 (plasma : platelets : red cells); give calcium.** A balanced ratio approximates whole blood (NEET 2025). PROPPR compared 1:1:1 with 1:1:2: mortality at 24 h and 30 days did not differ significantly, but fewer patients died of exsanguination at 24 h. Citrate in stored blood binds calcium, and low ionised calcium impairs clotting and contractility, so calcium is given with the products. A 4:1:1 ratio is wrong; cryo is not part of the ratio and is given for fibrinogen below 1.5 g/L."),
    ('c', "**1 g over 10 min, then 1 g over 8 h, within 3 h of injury (CRASH-2: ↓ mortality).** TXA blocks plasminogen binding to fibrin and so stops the clot being dissolved. In CRASH-2 (20,211 patients, enrolled up to 8 hours after injury) all-cause death fell from 16.0% to 14.5% and bleeding death from 5.7% to 4.9%. The later timing analysis found the effect on bleeding death was greatest within 1 hour, still present at 1–3 hours, and reversed after 3 hours, when TXA increased bleeding deaths; the likely reason is that late trauma has moved from fibrinolysis to fibrinolytic shutdown. So 8 hours was the trial’s entry window and is the length of the second infusion, but 3 hours is the treatment window. It is given for any suspected significant haemorrhage, blunt or penetrating."),
    ('d', "**Traumatic brain injury — keep MAP ≥ 80 for cerebral perfusion.** The injured brain loses autoregulation, so cerebral blood flow follows MAP; a single hypotensive episode worsens outcome. Permissive hypotension is therefore contraindicated in severe TBI."),
  ],
  mimic=[
    ("Positive FAST stable vs unstable", "Unstable plus free fluid → straight to laparotomy; stable → contrast CT. FAST needs about 200 mL (100–250 mL) to show, so ‘at least 50 mL’ is wrong and a negative scan does not exclude injury (GT2o, 59%)."),
    ("Trauma MTP vs obstetric MTP", "Same ratio, calcium and TXA within 3 h; only the fibrinogen trigger differs (2 g/L in obstetrics) because term fibrinogen is normally 4–6 g/L. The placenta accreta stem keys 1:1:1 (98%)."),
  ],
  traps=[
    ("“TXA within 8 hours” or “within 12 hours”", "CRASH-2 enrolled up to 8 h, but the benefit was confined to the first 3 h and later TXA increased bleeding deaths. NEET 2025 asks which statement is incorrect: the 12-hour option."),
    ("TXA not chosen as an adjunct to surgical control of liver bleeding (36% right)", "TXA is the adjunct; PCC, vitamin K and ratio-matched cryo are not."),
    ("The GT1o ratio question (18% right)", "Options B and C are printed identically (‘RBC, plasma and cryo in equal numbers’). The intended answer is 1:1:1 red cells : plasma : platelets; 4:1:1 is wrong and cryo is not part of the ratio."),
    ("“Delay products until surgical haemostasis” or “rFVIIa first line”", "Products start immediately in a balanced ratio; rFVIIa is not first line (NEET 2025)."),
  ],
  decode=[
    ("Penetrating abdomen, SBP 82, before haemorrhage control — strategy? [DocT GT]", "Permissive hypotension."),
    ("Polytrauma, which TXA statement is incorrect? [NEET 2025]", "‘Within 12 hours, only in blunt or penetrating trauma’; correct is 1 g over 10 min then 1 g over 8 h, within 3 h."),
    ("Multiple trauma, Hb 6.8, INR 2, platelets 65, going to laparotomy — MTP principle? [NEET 2025]", "Balanced ratio approximating whole blood."),
  ],
  punch="Until the bleeding is controlled: SBP 80–90 (MAP ≥80 if the brain is injured), blood 1:1:1 with calcium instead of crystalloid, and TXA 1 g then 1 g over 8 h started within 3 hours, never later.",
)

L['HEO-04'] = dict(
  sub="Haematology → Transfusion → TRALI, TACO and other reactions",
  step=2,
  intro="Step 2 ends with the transfusion itself as the injury. When a patient becomes breathless within hours of blood, the two diagnoses are a leak (TRALI, antibody-activated neutrophils in the lung) and an overload (TACO, too much volume for the heart). Nine linked questions turn on one discriminator in the stem: the blood pressure, the CVP or BNP, the diuretic response, and since 2019 whether an ARDS risk factor was present.",
  parts=[
    ('a', "**Timing: TRALI within 6 h; TACO within 6–12 h.** TRALI is defined as onset within 6 hours: new hypoxaemia (P/F ≤300 or SpO2 <90% on air) with bilateral infiltrates and no left-atrial hypertension. The 2019 definition splits it: type I has no ARDS risk factor; type II has a risk factor or mild ARDS that was stable for 12 hours before the transfusion. Worsening driven by the risk factor itself is ARDS. ISBT (2018) defines TACO as onset during or up to 12 hours after transfusion, with respiratory compromise or pulmonary oedema and at least three criteria in total from respiratory distress, pulmonary oedema, cardiovascular change, fluid overload and a raised BNP."),
    ('b', "**BP: TRALI hypotension, TACO hypertension; JVP/BNP normal in TRALI, raised in TACO.** TRALI is a capillary leak with normal filling pressures, so CVP and wedge are normal and fluid leaves the circulation. TACO is hydrostatic oedema: raised CVP (the QBank stem gives 18), hypertension and a BNP or NT-proBNP above 1.5 times the pre-transfusion value. The patient with heart failure who becomes hypertensive after two units is TACO (94% and 80%)."),
    ('c', "**Fever often in TRALI, not in TACO; TRALI does not respond to diuretics (harmful), TACO improves.** Neutrophil activation causes fever in TRALI, but fever does not exclude TACO, so the card’s ‘No’ is a tendency, not a rule. The diuretic is the treatment test: it helps overload and worsens hypotension in a leak. TRALI is treated with oxygen and lung-protective ventilation; most recover in 48–96 hours."),
    ('d', "**Prevention: TRALI — male-only donor plasma; TACO — slow rate, diuretic.** Most TRALI is caused by donor anti-HLA or anti-HNA antibodies, which form in women sensitised by pregnancy, so plasma from male donors cut cases sharply. TACO is prevented by identifying at-risk patients (heart failure, renal failure, elderly, positive balance), transfusing one unit at a time slowly and giving a diuretic."),
    ('e', "**Acute haemolytic (ABO): fever, loin pain, haemoglobinuria, DIC → stop. Anaphylaxis: IgA-deficient recipient. Febrile non-haemolytic: fever only.** ABO incompatibility is a type II reaction: preformed IgM fixes complement on transfused cells, causing intravascular haemolysis, hypotension, DIC and AKI. The first move in any suspected reaction is to stop the transfusion, then notify the blood bank and send the unit with samples. Anaphylaxis in IgA deficiency comes from anti-IgA antibodies; febrile non-haemolytic reactions come from cytokines in stored products."),
  ],
  mimic=[
    ("TRALI vs TACO", "Both within hours with bilateral infiltrates. Hypotension, normal CVP/BNP and no diuretic response = TRALI; hypertension, raised CVP/BNP and diuretic response = TACO."),
    ("TRALI type I vs type II", "Read the risk-factor sentence first: none = type I; sepsis, aspiration, trauma with ARDS risk or stable mild ARDS = type II."),
    ("TRALI vs fat embolism", "Fat embolism gives the same refractory hypoxaemia and fluffy opacities 24–72 h after a long-bone fracture, with petechiae and confusion, and needs no transfusion."),
  ],
  traps=[
    ("GrandT1 keys TRALI type II for a trauma patient with NO ARDS risk factors", "No risk factor defines type I; DocT’s own explanation describes type I, and the repeats (GT2, GT8; 75–77% right) key type I."),
    ("AIM2 keys TRALI for post-trauma refractory hypoxaemia with no transfusion stated (29% right)", "TRALI needs a transfusion within 6 h. If a transfusion is stated or implied pick TRALI; if a long-bone fracture with petechiae is given, pick fat embolism."),
    ("“Give furosemide” for TRALI", "The patient is hypotensive with normal filling; diuretics worsen shock."),
  ],
  decode=[
    ("Trauma, no ARDS risk factors, plasma, 3 h later P/F 250, bilateral oedema, normal LA pressure [DocT GT]", "TRALI type I."),
    ("CHF patient, dyspnoea, hypertension and pulmonary oedema within 3 h of two units [DocT GT]", "TACO."),
    ("Dyspnoea and hypoxaemia within 6 h of transfusion, CVP normal [DocT QBank]", "TRALI."),
    ("Massive transfusion (10:10:10), CXR white-out 3 h into it [DocT GT]", "TRALI."),
  ],
  punch="Within 6 hours of blood, hypotension with normal filling and no diuretic response is TRALI (type I if no ARDS risk factor), while hypertension, a high CVP or BNP and a good diuretic response is TACO.",
)

L['HEO-05'] = dict(
  sub="Haematology → Emergencies → Five haematology pictures",
  step=3,
  intro="Step 3 is the haematology diagnoses in which one treatment saves the patient and a reflex harms. Six linked questions test TTP (plasma exchange without waiting), methaemoglobinaemia in G6PD deficiency, and the anticoagulant for HIT when an organ is failing.",
  parts=[
    ('a', "**Acute chest syndrome → O2, analgesia, antibiotics (cephalosporin + macrolide), incentive spirometry, transfusion (exchange if severe).** Sickled cells occlude the pulmonary microcirculation, often triggered by infection or fat embolism from infarcted marrow, and hypoxia makes more cells sickle. Antibiotics cover pneumococcus and atypicals; simple transfusion raises oxygen delivery, and exchange transfusion lowers the HbS fraction without raising viscosity when hypoxia progresses (GT2, lost)."),
    ('b', "**G6PD deficiency → stop the drug, supportive. (Methylene blue contraindicated.)** Without G6PD the red cell cannot make NADPH, so oxidant drugs (sulphonamides, dapsone, primaquine) denature haemoglobin into Heinz bodies, which the spleen bites out. Methylene blue works only through NADPH-dependent reduction, so in G6PD deficiency it fails and itself causes haemolysis; for methaemoglobinaemia use ascorbic acid, exchange transfusion or hyperbaric oxygen (DocT QBank, 43%)."),
    ('c', "**HIT → stop ALL heparin, start argatroban or fondaparinux; no platelet transfusion.** IgG against PF4–heparin complexes activates platelets, so HIT causes thrombosis, not bleeding, typically 5–10 days after exposure. Platelets add fuel. The choice of agent follows the failing organ: argatroban is cleared by the liver, so in liver failure bivalirudin (proteolytic, partly renal) is safer (CGT4). Fondaparinux barely binds PF4 and does not cause HIT, but it is renally cleared (avoid with CrCl below 30) and protamine does not reverse it."),
    ('d', "**TTP → urgent plasma exchange (± caplacizumab, steroids); avoid platelets.** Antibodies against ADAMTS13 leave ultra-large von Willebrand multimers that build platelet microthrombi in brain and kidney. Plasma exchange removes the antibody and replaces the enzyme. Send ADAMTS13 and start exchange immediately; never wait for the result (Marrow; DocT QBank 60%). Pregnancy at 10 weeks with MAHA, low platelets and AKI is TTP until proven otherwise, because HELLP almost never occurs before 20 weeks."),
    ('e', "**24 h after chemotherapy — never in the 14 days before or within 24 h after a cycle.** Pegfilgrastim is cleared mainly by neutrophils, so it keeps acting until the count recovers; given within the 14 days before chemotherapy it drives myeloid precursors into division just as the cytotoxic drug arrives, which can worsen neutropenia. The label therefore says from 24 hours after the cycle, not in the 14 days before (GT3, lost)."),
  ],
  mimic=[
    ("TTP vs HUS vs DIC", "TTP: neurology, severe ADAMTS13 deficiency, normal clotting. HUS: kidney-led, often after diarrhoea. DIC: prolonged PT and aPTT, low fibrinogen."),
    ("Argatroban vs bivalirudin in HIT", "Liver failure → bivalirudin; renal failure → argatroban."),
  ],
  traps=[
    ("“Methylene blue can be used in G6PD deficiency”", "It needs NADPH; it fails and causes haemolysis. Ascorbic acid is the alternative. In methaemoglobinaemia the dissociation curve shifts left, not right, and the dye itself distorts oximetry."),
    ("Platelet transfusion for TTP or HIT", "Adds substrate for thrombosis; give only for life-threatening bleeding."),
    ("Waiting for ADAMTS13 before plasma exchange", "Untreated TTP mortality is about 90%; start exchange on suspicion."),
  ],
  decode=[
    ("Confusion, AKI, thrombocytopenia, high LDH, low haptoglobin, schistocytes — first-line? [DocT QBank]", "Plasma exchange."),
    ("HIT with bilirubin 6.5, normal renal function — safest DTI? [DocT GT]", "Bivalirudin."),
    ("Chemical worker, cyanosis — which statement is true? [DocT QBank]", "Ascorbic acid is used in G6PD deficiency."),
  ],
  punch="Acute chest syndrome needs antibiotics and transfusion, G6PD haemolysis needs the drug stopped and no methylene blue, HIT and TTP need the cause treated (non-heparin anticoagulant, plasma exchange now) and never platelets.",
)

L['HEO-06'] = dict(
  sub="Endocrine → Adrenal → Adrenal crisis and septic shock steroids",
  step=4,
  intro="Step 4 is the hormone emergencies, and adrenal crisis is the purest one: shock from missing cortisol, cured by replacing it. The two linked questions ask for the drug and for when to give it in refractory shock with a low cortisol.",
  parts=[
    ('a', "**Hydrocortisone 100 mg IV bolus, then 200 mg/24 h (50 mg 6-hourly or infusion).** Cortisol is needed for vascular responsiveness to catecholamines, so the shock does not correct with pressors alone. Hydrocortisone is chosen because it is cortisol itself, with both glucocorticoid and mineralocorticoid action."),
    ('b', "**0.9% saline ± dextrose (hypoglycaemia).** Aldosterone and cortisol loss cause salt and water depletion; about 1 litre in the first hour is usual. Cortisol deficiency also removes gluconeogenic support, so check glucose."),
    ('c', "**No — take a sample, treat immediately.** Draw cortisol and ACTH, then give hydrocortisone; the result changes nothing in the next hour. If a stimulation test is planned later, dexamethasone does not cross-react with the cortisol assay, but it has no mineralocorticoid effect."),
    ('d', "**Hydrocortisone 200 mg/day once noradrenaline ≥ 0.25 µg/kg/min for ≥ 4 h.** This is the SSC 2021 criterion. In the pancreatitis stem the low cortisol with refractory shock makes it clearer still (95% right)."),
  ],
  mimic=[
    ("Hydrocortisone vs fludrocortisone", "At 200 mg/day hydrocortisone gives full mineralocorticoid effect, so fludrocortisone is not needed acutely; it is the maintenance add-on in primary adrenal insufficiency once the dose falls below about 50 mg/day."),
  ],
  traps=[
    ("“Fludrocortisone” or “dexamethasone” as the initial treatment (79% right)", "Neither replaces cortisol fully; hydrocortisone is the answer."),
  ],
  decode=[
    ("Initial treatment for acute adrenal insufficiency [DocT QBank]", "Hydrocortisone."),
    ("Alcoholic with pancreatitis, refractory shock, low cortisol — next step [DocT QBank]", "Start hydrocortisone."),
  ],
  punch="In adrenal crisis hydrocortisone is the pressor: 100 mg IV now, then 200 mg/day, with saline and glucose, and never wait for the cortisol result.",
)

L['HEO-07'] = dict(
  sub="Endocrine → Thyroid → Thyroid storm drug sequence",
  step=4,
  intro="Step 4 continues with thyroid storm, where the order of drugs is the point: block the effects, stop new synthesis, then shut off release, then block conversion. Seven linked questions test the timing of iodine (85% right), the role of steroids (only 49–63% right) and the first drug in an undifferentiated storm.",
  parts=[
    ('a', "**1 Propranolol — controls adrenergic symptoms; blocks T4 → T3 at high dose.** Tachycardia, tremor and fever are driven by β-adrenergic sensitisation; propranolol treats them within minutes, so it is the best initial drug (the colitis stem with HR 160, 85%). ATA 2016 uses propranolol 60–80 mg 4-hourly, with esmolol as the alternative. JTA 2016 differs: it recommends a β1-selective drug (landiolol, esmolol or bisoprolol) first and does not recommend propranolol for the tachycardia, because of heart failure and asthma risk. In heart failure from storm use a short-acting agent with care. For the exam, propranolol is the keyed answer."),
    ('b', "**2 PTU (or methimazole) — stops new hormone synthesis; PTU also blocks T4 → T3.** Thionamides block thyroid peroxidase. PTU’s extra peripheral action is why ATA 2016 prefers it in storm (500–1000 mg load, then 250 mg 4-hourly), including in pregnancy at any trimester (CGT4); methimazole 60–80 mg/day is the alternative. JTA 2016 accepts either and finds methimazole no worse. Give one thionamide, not both."),
    ('c', "**3 Iodine (Lugol’s or SSKI) at least 1 h after the thionamide — blocks hormone release.** High-dose iodide blocks release of stored hormone and its organification. Given first, it is substrate for new hormone synthesis and can worsen the storm; given after synthesis is blocked, it only closes the release. ATA 2016 says do not start it until 1 hour after the antithyroid drug (SSKI 5 drops 6-hourly). JTA 2016 gives it at the same time as the thionamide, so the 1-hour gap is the ATA rule that the card and the questions follow. So the drug ‘not indicated for immediate treatment’ after surgery (GT2o) is iodine."),
    ('d', "**4 Hydrocortisone — blocks conversion, covers relative adrenal insufficiency.** The keyed ‘main role’ of steroids is to inhibit T4 → T3 conversion (49% and 63% right). Storm also accelerates cortisol clearance, so there may be relative adrenal insufficiency, but that is the secondary reason. ATA dose: hydrocortisone 300 mg IV, then 100 mg 8-hourly (JTA: 300 mg/day or dexamethasone 8 mg/day)."),
    ('e', "**5 Supportive: cooling (paracetamol, not aspirin), fluids; cholestyramine; treat the trigger.** Aspirin displaces T4 from binding proteins and raises free hormone. Cholestyramine interrupts enterohepatic recycling of thyroid hormone. Infection, surgery and labour are common triggers. Burch–Wartofsky ≥45 is highly suggestive of storm, 25–44 is impending storm."),
  ],
  mimic=[
    ("Thyroid storm vs sepsis or malignant hyperthermia", "Storm gives a suppressed TSH, high-output features and no rigidity; the post-appendectomy stem says ‘no rigidity’ to exclude MH."),
  ],
  traps=[
    ("“Steroids prevent adrenal crisis and suppress immunity” as the main role", "True but secondary; the keyed role is blocking T4 → T3 conversion (49%)."),
    ("“Iodine first-line, before thionamides” in pregnancy", "Never before the thionamide; PTU is preferred in storm in all trimesters (CGT4)."),
    ("“Propranolol must be avoided in pregnancy”", "β-blockade is used in storm in pregnancy; brief use does not cause permanent growth restriction."),
  ],
  decode=[
    ("Started on PTU — which adjunct must wait ≥1 h? [DocT QBank, AIM2]", "Lugol’s iodine."),
    ("Graves’, post-appendectomy, T 39.3, HR 130, BP 184/106 — which drug is NOT indicated immediately? [DocT GT]", "Iodine (until a thionamide is on board)."),
    ("Main role of steroids in the storm regimen [DocT QBank, GT5]", "Inhibit T4 → T3 conversion."),
  ],
  punch="β-blocker for the effects, thionamide (PTU) to stop synthesis, iodine only an hour later to stop release, steroid to block conversion, and treat the trigger.",
)

L['HEO-08'] = dict(
  sub="Endocrine → Diabetes → Adult DKA",
  step=4,
  intro="Step 4 includes DKA, where insulin is given to clear ketones, and the glucose is only a guide to how much dextrose to add. Six linked questions test the potassium rule, why insulin before fluid is dangerous, what to correct, and the transition to subcutaneous insulin.",
  parts=[
    ('a', "**K below 3.3 → hold insulin, replace K first.** Insulin drives potassium into cells within minutes; starting it with a low serum K risks arrhythmia and respiratory muscle weakness. The 2024 ADA/EASD/JBDS consensus has moved the threshold to 3.5 mmol/L. Even a high starting K (5.5) hides a total-body deficit from osmotic diuresis, so replacement is almost always needed once insulin starts (82% right). The same rule applies to HHS (potassium 3.0 → hold insulin, give K; 71%)."),
    ('b', "**Fixed-rate IV 0.1 U/kg/h after the first litre of saline.** Fluid first restores perfusion; insulin given into a dehydrated circulation shifts glucose, water and potassium into cells, causing hypotension and arrhythmia (GT5, 83%). No bolus is needed with a 0.1 U/kg/h infusion. A glucose fall of about 50–75 mg/dL per hour is the classic target (NEET 2024)."),
    ('c', "**Continue insulin, add 5–10% dextrose — insulin is treating the ketosis, not the glucose.** The 2024 consensus adds dextrose once glucose is below 250 mg/dL, reduces the infusion to 0.05 U/kg/h and keeps glucose around 200 until the ketoacidosis has resolved. The abnormality to correct is the metabolic acidosis (Marrow)."),
    ('d', "**Only if pH below 6.9–7.0.** The 2024 consensus says consider it only below 7.0. Bicarbonate does not speed recovery, worsens hypokalaemia and may increase intracellular acidosis; insulin regenerates bicarbonate as ketones are metabolised."),
    ('e', "**pH above 7.3, HCO3 ≥ 15–18, anion gap normal (ketones below 0.6).** The 2024 consensus uses ketones below 0.6 mmol/L with pH ≥7.3 or bicarbonate ≥18, and says the anion gap should no longer be used, because chloride-rich fluids keep it misleading; JBDS uses bicarbonate above 15. When resolved and eating, give basal SC insulin 1–2 hours before stopping the infusion, because IV insulin acts for only minutes and ketosis can rebound."),
  ],
  mimic=[
    ("DKA vs HHS", "DKA: β-hydroxybutyrate ≥3, pH <7.3 or bicarbonate <18. HHS: glucose ≥600, effective osmolality >300, little ketosis, insulin 0.05 U/kg/h and a slower glucose fall (no more than 90–120 mg/dL/h)."),
  ],
  traps=[
    ("“Stop insulin when glucose reaches 250” (sweep g)", "Ketogenesis restarts; add dextrose and continue."),
    ("“Initial hyperkalaemia contraindicates insulin” or “replace K only below 2”", "High serum K hides a deficit; insulin will drop it."),
    ("Marrow transition option without basal overlap", "Pick the option with SC basal insulin 1–2 h before stopping; if none includes it, pick the one that continues the infusion."),
  ],
  decode=[
    ("DKA, initial K 5.5 — true statement about potassium [DocT QBank]", "Replacement is usually needed despite the high start."),
    ("HHS on insulin, glucose 580 → 300, K 3.0 — next [DocT GT]", "Hold insulin, give potassium."),
    ("Insulin given before fluids; 30 min later hypotension and arrhythmia [DocT GT]", "Rapid fall in serum potassium."),
  ],
  punch="Fluid first, potassium above 3.3 (3.5 in the 2024 consensus) before insulin, 0.1 U/kg/h until the ketones clear with dextrose added once glucose falls below 250, and basal SC insulin overlapping 1–2 hours before stopping.",
)

L['HEO-09'] = dict(
  sub="Endocrine → Glucose → ICU and perioperative targets",
  step=4,
  intro="Step 4 closes with glucose control outside DKA. The one linked question asks the ICU target for stress hyperglycaemia; the card’s watch line shows the perioperative target was the weakest (11%).",
  parts=[
    ('a', "**140–180 mg/dL; tight control (81–108) ↑ mortality.** NICE-SUGAR (6,104 patients) found higher 90-day mortality with 81–108 than with a target of 180 or less (27.5% vs 24.9%), largely through hypoglycaemia. The reason for 140–180 is this harm, not the renal threshold of 180 (DocT QBank, 86%)."),
    ('b', "**100–180 mg/dL around surgery.** ADA uses this range in the perioperative period. The lower limit is 100 rather than 140 because the window is short and glucose is checked often (every 1–2 hours), so a low is caught before it harms; the upper limit of 180 is the same as in the ICU because higher values raise wound infection."),
    ('c', "**↓ hepatic gluconeogenesis + ↑ glucose uptake by inflamed tissues and macrophages.** Early sepsis raises glucose; late sepsis exhausts hepatic glycogen and gluconeogenesis while activated immune cells keep consuming glucose."),
    ('d', "**Withhold at the time of contrast if eGFR below 30 or AKI; restart after 48 h when renal function is stable.** The risk is lactic acidosis if contrast nephropathy leaves metformin accumulating; with normal kidneys it is not stopped."),
  ],
  mimic=[
    ("ICU vs perioperative target", "ICU 140–180; perioperative 100–180."),
  ],
  traps=[
    ("“80–110” or “110–140” for an ICU patient", "Intensive targets raise mortality and hypoglycaemia (NICE-SUGAR)."),
  ],
  decode=[
    ("Non-diabetic ICU patient, glucose repeatedly above 200 — target? [DocT QBank]", "140–180 mg/dL."),
  ],
  punch="ICU 140–180 mg/dL because tighter control killed in NICE-SUGAR, 100–180 around surgery, and stop metformin for contrast only with eGFR below 30 or AKI.",
)

L['HEO-10'] = dict(
  sub="Obstetrics → Physiology → Blood gas, oxygen reserve and maternal arrest",
  step=5,
  intro="Step 5 starts with how pregnancy changes the baseline, which explains why obstetric thresholds differ. The linked question asks which change does not happen in pregnancy; the answer, a fall in fibrinogen, is the opposite of the truth.",
  parts=[
    ('a', "**Compensated respiratory alkalosis: PaCO2 28–32, HCO3 18–21, pH ~7.44.** Progesterone stimulates the respiratory centre and raises minute ventilation by about 40%; the kidney compensates by excreting bicarbonate. A PaCO2 of 40 in a breathless pregnant woman (in asthma, for example) means she is tiring."),
    ('b', "**↑ VO2 + ↓ FRC (~20%) → desaturates fast on apnoea.** The uterus pushes the diaphragm up, shrinking the oxygen store, while the fetus and placenta raise consumption. Preoxygenate fully before intubation."),
    ('c', "**Manual left uterine displacement; resuscitative hysterotomy if no ROSC by ~4 min (deliver by 5) when the fundus is at or above the umbilicus (≥ 20 weeks).** The gravid uterus compresses the IVC and aorta when supine, so chest compressions generate little output; emptying the uterus restores venous return and improves maternal survival, and fetal survival is a secondary benefit."),
  ],
  mimic=[
    ("Pregnancy fibrinogen vs normal", "Fibrinogen rises to 4–6 g/L with factors VII, VIII, X and vWF; protein S falls. Cardiac output and GFR rise by about 40–50%."),
  ],
  traps=[
    ("“Decreased fibrinogen is a normal change”", "Pregnancy is hypercoagulable; fibrinogen rises (CGT2). This is why 2 g/L in PPH is already low."),
  ],
  decode=[
    ("Which is NOT a physiological change in pregnancy: reduced FRC, increased CO, decreased fibrinogen, increased GFR? [DocT GT]", "Decreased fibrinogen."),
  ],
  punch="Pregnancy lowers PaCO2 to about 30, raises fibrinogen and oxygen use and shrinks FRC, and in arrest after 20 weeks displace the uterus and deliver within 5 minutes.",
)

L['HEO-11'] = dict(
  sub="Obstetrics → Hypertensive disorders → Eclampsia",
  step=5,
  intro="Step 5 continues with eclampsia, the seizure of a placental disease. Magnesium treats and prevents the seizure, while blood pressure is lowered in parallel to prevent stroke. Six linked questions test the drug of choice (93–94%), magnesium as the ‘initial’ step even with pulmonary oedema (60%), and the imaging behind the seizure (PRES, 60%).",
  parts=[
    ('a', "**4–6 g IV over 15–20 min, then 1–2 g/h (extra 2 g for a recurrent seizure). Continue 24 h after delivery.** ACOG gives the load over 20–30 minutes and 2–4 g over 5 minutes for a recurrent seizure. Magnesium works as a cerebral vasodilator and NMDA antagonist; it is better than diazepam or phenytoin for preventing further seizures, so benzodiazepines, levetiracetam and phenytoin are wrong first-line answers. About a third of eclampsia occurs postpartum, hence the 24 hours."),
    ('b', "**If SBP ≥ 160 or DBP ≥ 110 (persisting 15 min; treat within 30–60 min) → IV labetalol, hydralazine or oral nifedipine; aim ~140–150/90–100.** The threshold is set by stroke risk, which tracks systolic pressure. Treating to normal reduces placental flow, which has no autoregulation."),
    ('c', "**CT head — exclude haemorrhage or venous thrombosis.** Most eclamptic brains show PRES: posterior subcortical vasogenic oedema from failed autoregulation (GT2o). Seizures despite magnesium, focal signs or an atypical course mean imaging for haemorrhage, venous sinus thrombosis or another cause."),
    ('d', "**Diuretics — intravascularly depleted; reduce uterine perfusion. Delivery is definitive.** Pre-eclampsia leaks fluid into tissues while the plasma volume is contracted. The one exception is pulmonary oedema, where furosemide is indicated."),
  ],
  mimic=[
    ("Eclampsia vs epilepsy or a high block after delivery", "A seizure soon after delivery in a hypertensive woman with RUQ pain is eclampsia with PRES."),
  ],
  traps=[
    ("“Treat BP when diastolic is above 90” (only 28% picked it as the incorrect statement)", "That is the diagnostic threshold, not the treatment threshold; treat at ≥160 or ≥110."),
    ("“IV furosemide first” for BP 180/110 with pulmonary oedema", "DocT keys magnesium as the single initial step; in practice magnesium, an IV antihypertensive and furosemide all start promptly. Magnesium is the least-wrong single answer."),
    ("Diazepam or levetiracetam for the eclamptic seizure", "Magnesium is the drug of choice."),
  ],
  decode=[
    ("32 weeks, tonic-clonic seizure, hypertension, 3+ proteinuria — first-line? [DocT QBank]", "Magnesium sulphate."),
    ("36 weeks, BP 180/110, headache, crackles, CXR infiltrates — initial management? [DocT QBank, GT6]", "IV magnesium (keyed), with prompt BP control and furosemide."),
    ("Seizure 15 minutes after delivery, hypertensive, RUQ pain — most likely associated with? [DocT GT]", "Subcortical vasogenic cerebral oedema (PRES)."),
  ],
  punch="Magnesium 4–6 g then 1–2 g/h until 24 hours after delivery, lower BP only at 160/110 to about 140–150/90–100, image if seizures persist, no diuretics unless the lungs are wet, and deliver.",
)

L['HEO-12'] = dict(
  sub="Obstetrics → Magnesium → Toxicity, monitoring and antidote",
  step=5,
  intro="Step 5 includes the bedside safety check on magnesium. Because the kidney clears it, toxicity follows oliguria, and the clinical signs appear in a fixed order. Four linked questions describe toxicity (absent reflexes, slow breathing, prolonged PR, oliguria or a high creatinine) and ask for the response (82–89% right).",
  parts=[
    ('a', "**4–7 mEq/L therapeutic.** This is about 5–9 mg/dL; multiply mEq/L by about 1.2 for mg/dL."),
    ('b', "**~7–10: loss of patellar reflex.** Magnesium blocks calcium-dependent acetylcholine release at the neuromuscular junction; the reflex goes before breathing, so it is the hourly early warning."),
    ('c', "**~10–13: respiratory depression; above 25: cardiac arrest.** Further neuromuscular block weakens the respiratory muscles; at higher levels conduction slows (prolonged PR and QRS, CGT2) and the heart arrests."),
    ('d', "**Monitor every hour: patellar reflex, RR above 12, urine above 30 mL/h (US); WHO: RR ≥16, urine ≥25–30 mL/h or 100 mL in 4 h.** Oliguria (15 mL/h in CGT4) or a creatinine of 3.0 means magnesium is accumulating; reduce the maintenance dose and check levels before signs appear."),
    ('e', "**Toxic → stop infusion, calcium gluconate 1 g IV.** Calcium antagonises magnesium at the membrane in minutes (10 mL of 10% over about 3 minutes). Ventilate if needed; dialysis or furosemide is not the first step."),
  ],
  mimic=[
    ("Magnesium toxicity vs worsening eclampsia", "Somnolence with absent reflexes, slow breathing and oliguria is toxicity; eclampsia gives hyperreflexia and seizures."),
  ],
  traps=[
    ("“Increase magnesium because somnolence signals a seizure”", "Absent reflexes and RR 8 are toxicity (CGT4)."),
    ("“Labetalol bolus” for a prolonged PR and RR 6", "Magnesium toxicity (CGT2)."),
    ("“Start dialysis” or “give furosemide” first", "Stop the infusion and give calcium first."),
  ],
  decode=[
    ("Eclampsia on magnesium, respiratory depression, creatinine 3.0 — next? [DocT QBank, GT6]", "Stop magnesium and give IV calcium gluconate."),
  ],
  punch="The knee jerk goes at about 7 mEq/L, breathing at 10 and the heart at 25, so check reflexes, breathing and urine every hour and give calcium gluconate 1 g for toxicity.",
)

L['HEO-13'] = dict(
  sub="Obstetrics → Liver → HELLP and acute fatty liver of pregnancy",
  step=5,
  intro="Step 5 ends with the two third-trimester liver crises. HELLP is a microangiopathy of pre-eclampsia in which the liver works; acute fatty liver is liver failure. Ten linked questions test the Tennessee criteria, management, the bleeding risk, and the NEET 2025 recall of a subcapsular haematoma and a fatty liver with hypoglycaemia.",
  parts=[
    ('a', "**Haemolysis (LDH above 600), AST/ALT above 70, platelets below 100,000 → MgSO4 + control BP + delivery.** Endothelial injury lays fibrin in small vessels, which shears red cells, consumes platelets and causes periportal necrosis. Delivery ends it; magnesium prevents seizures. At 29 weeks DocT keys magnesium and prompt delivery; ACOG still allows a 48-hour steroid delay in stable HELLP before 34 weeks. Steroids do not cure the thrombocytopenia. Up to 15% have no hypertension or proteinuria."),
    ('b', "**Hypoglycaemia, low fibrinogen/coagulopathy, AKI, encephalopathy, mildly raised ammonia — liver FAILURE, not just enzymes.** A fetal defect of fatty-acid oxidation (LCHAD) loads the maternal liver with fat, so it stops making glucose and clotting factors (AIM1, 85%). The Swansea criteria need six of 14 features. Treatment is prompt delivery after stabilisation (NEET 2025)."),
    ('c', "**Imaging is often normal → liver biopsy (rarely needed).** Ultrasound may show a bright liver but has low sensitivity; diagnosis is clinical and biopsy is rarely needed because the coagulopathy makes it risky."),
    ('d', "**Haemorrhage from coagulopathy.** In HELLP the PPH risk comes from platelet consumption, not atony (DocT QBank, 89%); in AFLP from failed synthesis. HELLP with hypotension and a falling Hb means a subcapsular liver haematoma; if it has ruptured (free fluid, shock), resuscitate and do an emergency caesarean with laparotomy for the liver."),
  ],
  mimic=[
    ("HELLP vs AFLP", "Glucose, INR and ammonia decide: normal in HELLP, abnormal in AFLP."),
    ("HELLP vs catastrophic APS vs TTP in an APS pregnancy", "CAPS adds multi-organ thrombosis and rising antibody titres; TTP has severe ADAMTS13 deficiency; HELLP resolves after delivery."),
  ],
  traps=[
    ("“Platelets <150k, LDH >400” or “AST >50”", "Tennessee is platelets ≤100,000, AST ≥70, LDH ≥600 (76%)."),
    ("“High-dose dexamethasone to cure the thrombocytopenia and allow expectant care to 34 weeks”", "Steroids do not treat HELLP."),
    ("“Steroids and wait” or “transplant” for a ruptured subcapsular haematoma", "Emergency caesarean with surgical control of the liver (NEET 2025)."),
  ],
  decode=[
    ("Tennessee HELLP criteria [DocT QBank]", "Platelets <100k, AST >70, LDH >600."),
    ("35 weeks, jaundice, INR 2.3, glucose 42, ammonia 80, creatinine 2.1, fatty liver on US — immediate management? [NEET 2025]", "Emergency delivery."),
    ("HELLP, BP 170/110, platelets 38,000, subcapsular haematoma with free fluid, shock [NEET 2025]", "Emergency caesarean with surgical management of the liver."),
    ("HELLP with hypotension, falling Hb, crescentic subcapsular collection on CT [NEET 2025]", "Subcapsular liver haematoma."),
  ],
  punch="HELLP is LDH ≥600, AST ≥70 and platelets ≤100,000 with a working liver, treated with magnesium and delivery; AFLP is hypoglycaemia, coagulopathy and encephalopathy, treated with delivery; both bleed from coagulopathy.",
)

L['HEO-14'] = dict(
  sub="Obstetrics → Haemorrhage → Abruption and placenta praevia",
  step=6,
  intro="Step 6 is obstetric bleeding and collapse, and abruption is the clearest example of fibrinogen consumption. Six linked questions test the diagnosis after trauma, the DIC mechanism, fibrinogen replacement and the timing of delivery in praevia, where the bank’s key is out of date.",
  parts=[
    ('a', "**Cryoprecipitate + FFP + emergency delivery (resuscitate and correct clotting alongside).** Placental separation releases tissue factor (thromboplastin), which drives systemic thrombin generation; fibrin microthrombi then consume platelets and fibrinogen and shear red cells (CGT1: microvascular fibrin deposition). Fibrinogen 85 mg/dL is critical against a term normal of 400–450, so cryo is the first product (NEET 2025: fibrinogen 0.5 g/L → cryo). Ultrasound misses many abruptions, so a normal scan does not exclude it; prepare for delivery (CGT2)."),
    ('b', "**Placenta praevia; empty the bladder before ultrasound (a full bladder mimics previa).** Painless bright red bleeding from a soft, non-tender uterus is praevia; pain, tenderness and contractions mean abruption (trauma at 30 weeks, FAST negative, 72%). A full bladder compresses the lower segment and makes the placenta look low. Transvaginal ultrasound is safe and more accurate."),
    ('c', "**Digital vaginal examination.** A finger through the cervix can tear the placenta and cause massive bleeding; examine with a speculum only after ultrasound."),
  ],
  mimic=[
    ("Abruption vs praevia", "Abruption: pain, a hard tender uterus, fetal distress, DIC. Praevia: painless bleeding, soft uterus, malpresentation."),
    ("Abruption vs uterine rupture after trauma", "Rupture gives loss of fetal station and palpable fetal parts; abruption gives a tender, contracting uterus."),
  ],
  traps=[
    ("DocT keys ‘hospitalise and pelvic rest’ for praevia at 36 weeks with a second bleed (21% right)", "That is the older expectant rule. ACOG/SMFM 2021 plan caesarean for praevia at 36+0 to 37+6 weeks (34+0 to 35+6 is their timing for accreta, not for bleeding praevia); RCOG 2018 advises delivery at 34+0 to 36+6 weeks when there has been bleeding. At 36 weeks with a second bleed both put her in the delivery window, so caesarean is the current answer. Pick expectant care only before 34 weeks with a single stable bleed."),
    ("“Rule out abruption because ultrasound is negative”", "Ultrasound misses many abruptions; the diagnosis is clinical."),
    ("Platelets or heparin for abruption DIC with fibrinogen 0.5", "Replace fibrinogen; heparin and antithrombin have no place."),
  ],
  decode=[
    ("Abruption after 6 PRBC and 4 FFP, fibrinogen 90 — priority? [DocT GT]", "10 units of cryo or 4 g fibrinogen concentrate."),
    ("35 weeks, shock, no FHS, platelets 66, fibrinogen 0.5 g/L — next? [NEET 2025]", "Fibrinogen replacement (cryoprecipitate)."),
    ("Seatbelted MVA at 30 weeks, tenderness, contractions, FAST negative — cause of bleeding? [DocT QBank]", "Abruptio placentae."),
  ],
  punch="Abruption releases tissue factor and burns fibrinogen first, so replace it with cryo and deliver; praevia is painless, is never examined digitally, and is delivered at 36–37 weeks (from 34 weeks if she has bled).",
)

L['HEO-15'] = dict(
  sub="Obstetrics → Haemorrhage → PPH drug ladder and contraindications",
  step=6,
  intro="Step 6 continues with postpartum haemorrhage, most of which is atony. The drugs are climbed in order, and the choice at each rung depends on the patient’s contraindications. Nine linked questions test carboprost dosing (64–70%), its contraindication in asthma (53%), TXA timing in WOMAN (43–76%) and which drug follows oxytocin.",
  parts=[
    ('a', "**Oxytocin 5 IU slow IV, then infusion.** It acts on myometrial oxytocin receptors within minutes; a rapid bolus causes hypotension, so give it slowly."),
    ('b', "**Ergometrine 0.2–0.5 mg IM; avoid in hypertension and pre-eclampsia.** It causes sustained uterine and vascular smooth-muscle contraction through α-adrenergic and serotonin receptors, so it can cause a hypertensive crisis or stroke. It is safe in asthma (91% right on hypertension)."),
    ('c', "**Carboprost (PGF2α) 250 µg IM every 15 min, max 8 doses; avoid in asthma.** Eight doses is 2 mg total. PGF2α constricts bronchial smooth muscle and can cause severe bronchospasm."),
    ('d', "**Misoprostol 800 µg sublingual or rectal.** A PGE1 analogue that does not cause bronchospasm; slower and weaker than the injectables. DocT keys it for an asthmatic after oxytocin; methylergonovine is equally safe in asthma when the BP is normal."),
    ('e', "**Tranexamic acid 1 g IV within 3 h (repeat once).** WOMAN (20,060 women) reduced death from bleeding, with the benefit only when given within 3 hours of birth; a second 1 g is given if bleeding continues after 30 minutes or restarts within 24 hours."),
    ('f', "**Then: balloon tamponade → B-Lynch / embolisation → hysterectomy. Keep fibrinogen ≥ 2 g/L.** Mechanical and surgical steps follow failed drugs; fibrinogen below 2 g/L predicts severe PPH (HEO-02)."),
  ],
  mimic=[
    ("Asthma vs hypertension", "Asthma: avoid carboprost, use ergometrine or misoprostol. Hypertension or pre-eclampsia: avoid ergometrine, use carboprost or misoprostol."),
  ],
  traps=[
    ("“Carboprost” as the only correct second agent (62% right)", "With normal BP and no pre-eclampsia, ergometrine is an equally valid second uterotonic (RCOG, WHO). Carboprost is keyed only because the stem doesn’t mention asthma."),
    ("“Within 1 hour” for TXA in WOMAN", "The trial threshold is 3 hours; earlier is better, but the keyed window is 3."),
    ("“TXA causes uterine contraction”", "It is antifibrinolytic, not a uterotonic."),
  ],
  decode=[
    ("Initial carboprost 250 µg; maximum total dose? [DocT GT]", "2 mg (8 × 250 µg)."),
    ("Atony after oxytocin in an asthmatic — next agent? [DocT GT]", "Misoprostol (keyed); methylergonovine if normotensive."),
    ("WOMAN trial — when should TXA be given? [DocT QBank, GT6, GT7]", "Within 3 hours."),
  ],
  punch="Oxytocin, then ergometrine unless hypertensive, carboprost unless asthmatic (max 2 mg), misoprostol, and TXA 1 g within 3 hours, with fibrinogen kept at 2 g/L or above.",
)

L['HEO-16'] = dict(
  sub="Obstetrics → Collapse → Amniotic fluid embolism",
  step=6,
  intro="Step 6 includes the obstetric collapse with DIC. Amniotic fluid embolism is an inflammatory reaction to fetal material, not a clot, so it is treated supportively and not lysed. Six linked questions test recognition, the two phases, the bedside investigation and why heparin or thrombolysis is wrong (40% right).",
  parts=[
    ('a', "**Labour or just after: sudden hypoxia, hypotension or arrest, and DIC (± seizure).** It occurs during labour, caesarean or within 30 minutes of delivery. Seizures and bleeding from IV sites and the vagina after ROSC complete the picture (CGT4)."),
    ('b', "**Anaphylactoid / systemic inflammatory response to fetal antigens — not mechanical obstruction.** Fetal material activates mast cells, complement and tissue factor. Pulmonary vasospasm causes acute RV failure first, then LV failure follows with consumptive DIC. Finding fetal squames in pulmonary blood is not diagnostic; they are found in healthy women too."),
    ('c', "**Supportive: CPR with left uterine displacement, early delivery, massive transfusion with early fibrinogen, RV support; VA-ECMO if refractory.** Use TEE or TTE at the table to show a dilated RV with an under-filled LV; this steers to inotropes and pulmonary vasodilators rather than fluid. A-OK (atropine, ondansetron, ketorolac) is unproven."),
  ],
  mimic=[
    ("AFE vs massive PE", "Both dilate the RV. DIC, seizures and onset within 30 minutes of delivery point to AFE; only PE is lysed."),
    ("AFE vs peripartum cardiomyopathy", "Cardiomyopathy is a failing LV over days, without DIC."),
  ],
  traps=[
    ("“Mechanical obstruction by amniotic fluid; thrombolyse” (lost in GT4)", "The mechanism is anaphylactoid; thrombolysis onto DIC after delivery is dangerous."),
    ("“Immediate heparin” for an APS patient with a dilated RV after delivery (40% right)", "AFE until proven otherwise: supportive care, not anticoagulation."),
    ("“CTPA” as the immediate investigation", "Transporting an unstable, bleeding patient is unsafe; TEE (68% right)."),
  ],
  decode=[
    ("38 weeks, labour, hypoxia, hypotension, low platelets, long PT, high D-dimer, RV failure [DocT QBank]", "Amniotic fluid embolism."),
    ("Collapse during caesarean with coagulopathy — immediate investigation? [DocT QBank]", "Transoesophageal echocardiography."),
  ],
  punch="AFE is sudden hypoxia, collapse and DIC around delivery from an anaphylactoid reaction, causing RV then LV failure; treat with support, delivery, fibrinogen-rich transfusion and ECMO, never thrombolysis.",
)

L['HEO-17'] = dict(
  sub="Obstetrics → Early pregnancy → PE imaging, PUL, anti-D and bacteriuria",
  step=5,
  intro="Step 5 includes decisions where pregnancy changes the usual test or drug. The two linked questions are on PE imaging; the card’s watch line shows V/Q (11%) and bacteriuria (19%) were the weakest.",
  parts=[
    ('a', "**V/Q (lung scintigraphy). Abnormal CXR → CTPA. D-dimer unreliable.** With a normal chest film the perfusion scan is likely to be diagnostic, gives less breast radiation than CTPA, and both give fetal doses far below the harm threshold (CGT4). D-dimer rises through pregnancy, so it is unreliable alone; ESC 2019 accepts pregnancy-adapted algorithms (YEARS) that use it. If the legs are symptomatic, compression ultrasound comes first."),
    ('b', "**Pregnancy of unknown location → repeat hCG + transvaginal US in 48 h — don’t treat on one value.** An hCG of 2,800 is below the level at which an intrauterine pregnancy must be visible (up to about 3,500); the trend separates a viable, failing or ectopic pregnancy."),
    ('c', "**Anti-D 50 µg (fetal Rh antigen present from ~6 weeks).** 50 µg (250 IU) covers the small fetal bleed in the first trimester; this is the traditional ACOG (Practice Bulletin 181) answer and the one the card keys. Practice is moving away from it. ACOG 2024 says anti-D may be forgone after abortion or pregnancy loss before 12 weeks, and its published summaries do not mention ectopic pregnancy. NICE NG126 now says do not offer anti-D for ectopic pregnancy or miscarriage up to 11+6 weeks, and offer 250 IU only at 12+0 weeks or later. On exam day, give anti-D 50 µg."),
    ('d', "**Amoxicillin or cephalexin 3–7 days (nitrofurantoin avoided in 1st trimester; no fluoroquinolones).** Untreated bacteriuria in pregnancy leads to pyelonephritis and preterm birth. IDSA 2019 suggests 4–7 days. ACOG allows nitrofurantoin and sulphonamides in the first trimester when no alternative exists."),
  ],
  mimic=[
    ("V/Q vs CTPA in pregnancy", "Normal CXR → V/Q; abnormal CXR → CTPA."),
  ],
  traps=[
    ("“A negative D-dimer is highly reliable in the third trimester”", "D-dimer rises normally; alone it is unreliable (CGT4)."),
    ("“Thrombolysis is strictly contraindicated in pregnancy”", "Pregnancy is a relative contraindication; massive PE with instability is still lysed."),
    ("“Warfarin is safest in the third trimester”", "LMWH is the anticoagulant of pregnancy."),
  ],
  decode=[
    ("Second-trimester suspected PE, normal CXR and Doppler — initial imaging? [Marrow]", "V/Q scan."),
    ("32 weeks, suspected PE — which statement is correct? [DocT GT]", "V/Q or CTPA can be safely performed."),
  ],
  punch="In pregnancy, normal CXR means V/Q, one hCG of 2,800 means repeat it in 48 h, Rh-negative ectopic gets anti-D 50 µg in the exam (NICE no longer gives it before 12 weeks), and bacteriuria is treated with amoxicillin or cephalexin.",
)

L['HEO-18'] = dict(
  sub="Obstetrics → One-liners → Infection, dystocia, arrhythmia and thyroid",
  step=6,
  intro="Step 6 includes five obstetric one-liners that have each cost marks. The one linked recall question asks for the key criterion for postpartum endometritis; the watch line lists fetal tachycardia (16%), gestational thyrotoxicosis (29%) and amiodarone (47%).",
  parts=[
    ('a', "**IV clindamycin + gentamicin.** Endometritis after caesarean is polymicrobial, including anaerobes; clindamycin covers anaerobes and gentamicin covers Gram-negatives. The diagnosis is clinical, and fever is the key criterion (≥38 °C after the first 24 h, with uterine tenderness); leucocytosis is normal after delivery (NEET 2025)."),
    ('b', "**Fetal tachycardia above 160 (with maternal fever).** ACOG 2017 defines suspected intra-amniotic infection as maternal fever plus fetal tachycardia, maternal leucocytosis or purulent cervical discharge. Fetal tachycardia is the keyed ‘best sign’ because maternal leucocytosis is common in normal labour and after steroids, whereas the fetal heart rate responds directly to infection and fever around it."),
    ('c', "**McRoberts (± suprapubic pressure). Never fundal pressure.** Flexing the hips flattens the sacral promontory and rotates the pelvis; fundal pressure impacts the shoulder further."),
    ('d', "**Amiodarone (fetal thyroid, neurotoxicity).** Its iodine causes fetal hypothyroidism and goitre; use electrical cardioversion or β-blockers instead."),
    ('e', "**Gestational transient thyrotoxicosis → supportive ± β-blocker; no antithyroid drugs.** hCG peaks in the first trimester and stimulates the TSH receptor; with hyperemesis and no TRAb it resolves by about 14–18 weeks as hCG falls."),
  ],
  mimic=[
    ("Gestational thyrotoxicosis vs Graves’", "Graves’ has TRAb, goitre or eye signs and persists after the first trimester."),
  ],
  traps=[
    ("“Foul-smelling lochia” or “leucocytosis” for endometritis", "Both are non-specific; fever is the criterion."),
  ],
  decode=[
    ("Most important criterion for postpartum endometritis [NEET 2025]", "Fever."),
    ("[pattern] Hyperemesis at 10 weeks, low TSH, high FT4, TRAb negative — treat?", "Supportive care; no thionamide."),
  ],
  punch="Clindamycin with gentamicin after caesarean, fetal tachycardia for chorioamnionitis, McRoberts for dystocia, no amiodarone in pregnancy, and hCG thyrotoxicosis treated with time.",
)

L['HEO-19'] = dict(
  sub="Sweep → Nine true/false statements",
  step=6,
  intro="Step 6 closes with a sweep across the deck. Each false statement is a reflex that a linked question exploited; each true one is the guideline answer. The one linked question tests platelet function after cardiac surgery, which sits behind statement a.",
  parts=[
    ('a', "**F — normal HEPTEM = heparin → protamine.** If heparinase corrects the INTEM time, heparin was the cause; FFP is for a long time that heparinase does not correct (HEO-01). Platelet function after bypass is read from MA or EXTEM MCF against FIBTEM, not PFA-100."),
    ('b', "**T — threshold 1.5 g/L.** 2 g/L in obstetric haemorrhage (HEO-02)."),
    ('c', "**T — CRASH-2; later = harm.** TXA after 3 h increased bleeding deaths (HEO-03)."),
    ('d', "**F — TACO does; TRALI does not.** TRALI is a leak with normal filling; diuretics worsen its hypotension (HEO-04)."),
    ('e', "**T — bolus then infusion or 6-hourly.** 100 mg IV, then 200 mg/24 h (HEO-06)."),
    ('f', "**F — iodine ≥ 1 h AFTER thionamide.** Given first it becomes substrate for more hormone (HEO-07)."),
    ('g', "**F — add dextrose, continue insulin.** Insulin is treating the ketosis (HEO-08)."),
    ('h', "**F — SBP ≥ 160 or DBP ≥ 110.** Diastolic 90 is the diagnostic, not the treatment, threshold (HEO-11)."),
    ('i', "**T — bronchospasm.** PGF2α constricts bronchi; use ergometrine or misoprostol (HEO-15)."),
  ],
  mimic=[
    ("Statement a vs the card watch line on HEO-01", "Long INTEM CT with HEPTEM also long, or no heparin in the picture, means FFP; HEPTEM normal means protamine."),
  ],
  traps=[
    ("“PFA-100” for platelet function after cardiac surgery (45% right)", "Unreliable with low haematocrit or platelets; use TEG/ROTEM."),
  ],
  decode=[
    ("Bleeding after cardiac surgery, normal platelet count — test platelet function with? [DocT GT]", "Viscoelastic testing (TEG or ROTEM)."),
    ("[pattern] Statements I–IV on transfusion and obstetric emergencies — which are correct?", "Mark each true or false on its own before reading the options."),
  ],
  punch="Normal HEPTEM is protamine, fibrinogen below 1.5 is cryo, TXA only within 3 hours, diuretics help TACO not TRALI, hydrocortisone 100 then 200, iodine after the thionamide, dextrose not insulin withdrawal, BP treated at 160/110, and no carboprost in asthma.",
)

FLAGS = {
  'HEO-08': "a: ‘K below 3.3 → hold insulin’ is the ADA 2009 figure; the 2024 ADA/EASD/JBDS/AACE/DTS consensus postpones insulin until K is above 3.5 mmol/L (confirmed online). d: 2024 says bicarbonate only for pH below 7.0. e: 2024 resolution is ketones <0.6 mmol/L with pH ≥7.3 or bicarbonate ≥18 (JBDS uses >15), and the 2024 consensus says the anion gap should not be used, so ‘anion gap normal’ is outdated. Explanation keeps the card wording and states the 2024 figures.",
  'HEO-04': "Table says TACO ‘within 6–12 h’ and ‘Fever: No’. ISBT criteria define TACO as onset during or up to 12 h after transfusion, and require at least 3 criteria in total (respiratory compromise and/or pulmonary oedema, plus cardiovascular change, fluid overload, BNP); fever does not exclude TACO (SHOT/ISBT). Card layer: GrandT1 Q43 type II key is wrong (type I); AIM2 Q105 TRALI key needs an assumed transfusion (fat embolism fits).",
  'HEO-11': "a: ‘over 15–20 min’ and ‘extra 2 g’ are the Sibai wording; ACOG PB 222 gives the load over 20–30 min and 2–4 g over 5 min for a recurrent seizure. Minor. The DocT ‘initial management’ key (magnesium alone with BP 180/110 and pulmonary oedema) is the least-wrong single option; antihypertensive and furosemide are equally immediate.",
  'HEO-02': "Card agrees with AABB 2023 (red cells) and AABB/ICTMG 2025 (platelets: surgery 50). AABB 2025 gives no neurosurgery figure; ‘below 100’ is BSH/standard teaching. Disputed key: GT7 Q90 keys 6 g/dL (old ASA wording); the trial-based trigger is 7. GT8 aplastic anaemia stem keys prophylaxis at 6,000; AABB 2025 advises against routine prophylaxis in stable aplastic anaemia but for it (<10) during chemotherapy, which the stem also says.",
  'HEO-03': "Card correct. DocT GT1o explanation says TXA ‘within 8 hours’: that was CRASH-2’s enrolment window, but the benefit was confined to the first 3 h and later TXA increased bleeding deaths, so 3 h is the answer. GT1o ratio question has options B and C printed identically; the intended answer is 1:1:1 red cells : plasma : platelets.",
  'HEO-13': "Card answer folds part d into line c (‘…biopsy (rarely needed). Haemorrhage from coagulopathy.’); the explanation separates them as c and d. Tennessee cut-offs are written ‘above 600 / above 70 / below 100’; the criteria are ≥600, ≥70, ≤100. At 29 weeks DocT keys prompt delivery; ACOG still allows a 48-h steroid delay for stable HELLP before 34 weeks.",
  'HEO-14': "Card correct. Card layer: DocT QBank keys expectant care for praevia at 36 weeks with a repeat bleed (21% right); current timing makes caesarean the answer. The card-layer cross line itself is wrong in one detail: it attributes ‘34+0 to 35+6 with recurrent bleeding’ to ACOG/SMFM 2021, but ACOG CO 831 gives 36+0–37+6 for praevia and 34+0–35+6 for accreta, with no bleeding modifier; the earlier window for praevia with bleeding is RCOG GTG 27a (34+0–36+6). The verdict (caesarean at 36 weeks) is unchanged.",
  'HEO-15': "Card correct. Two keys disputed: DocT QBank keys carboprost as the next agent where ergometrine is equally valid (no hypertension stated); CGT4 keys misoprostol for the asthmatic where methylergonovine is safe and standard if normotensive.",
  'HEO-17': "a ‘D-dimer unreliable’: ESC 2019 accepts pregnancy-adapted algorithms (YEARS, Geneva) that use D-dimer; unreliable alone is right. d ‘3–7 days’: IDSA 2019 suggests 4–7 days; ‘nitrofurantoin avoided in the 1st trimester’ is ACOG’s ‘if alternatives exist’. c ‘Anti-D 50 µg’ for a 7-week ectopic is the traditional ACOG PB 181 answer and the exam answer, but is now contested: NICE NG126 (current text) says do not offer anti-D for ectopic pregnancy or miscarriage up to 11+6 weeks; ACOG 2024 lets RhIg be forgone after abortion or pregnancy loss before 12 weeks, and its abstract and summaries do not mention ectopic pregnancy (whether ectopic is covered could not be confirmed from the full text).",
  'HEO-07': "Card ‘why’ calls iodine-given-first ‘Jod-Basedow’; strictly the risk is that iodide becomes substrate for new hormone before synthesis is blocked (Jod-Basedow is iodine-induced hyperthyroidism in nodular or iodine-deficient glands). The card’s sequence is the ATA 2016 regimen (PTU preferred; iodide not until 1 h after the thionamide; propranolol). JTA 2016 differs on three points: either thionamide (methimazole no worse), inorganic iodide given simultaneously with the thionamide, and β1-selective blockers (landiolol, esmolol, bisoprolol) first with propranolol not recommended for the tachycardia. Exam answers follow ATA; no change to the answer.",
}
