# RESP06B — Explain v3 ("Learn" depth): pulmonary embolism, part 2 — PESI and sPESI, ESC risk classes, prognostic markers, the failing RV, parenteral anticoagulation, the four NOACs, oral anticoagulation rules, systemic thrombolysis and its contraindications, embolectomy and catheter therapy, IVC filters, PE in pregnancy, true/false sweep. No mnemonics or hooks.
# Driven by the real questions in qpack/RESP06B.md (31 questions; PE-25 pregnancy asked 7 times, PE-22 contraindications 4, PE-18/20/21/24/26 3 each). Fields as TOX01, plus SPINE, PRIMER and step.
# Continues RESP06A, whose last step hands over to risk stratification. Cards with no linked question (PE-15, PE-16, PE-17) get short explanations with [pattern] decode items.
# Checked online on 11 Nov 2026: PEITHO (Meyer, NEJM 2014: 1,005 patients; death or decompensation 2.6% vs 5.6%; death at 7 days 1.2% vs 1.8%; extracranial major bleeding 6.3% vs 1.2%; stroke 2.4% vs 0.2%, 10 of 12 haemorrhagic; 30-day death 2.4% vs 3.2%);
# PEITHO-3 (alteplase 0.6 mg/kg, max 50 mg, over 15 min vs placebo in intermediate-high risk; active, not recruiting, no results, completion expected 2027); HI-PEITHO (NEJM 2026, ACC.26: 544 patients, ultrasound-facilitated catheter lysis vs anticoagulation alone, 7-day composite 61% lower, decompensation 3.7% vs 10.3%, no intracranial bleeding, no mortality difference);
# 2026 AHA/ACC multisociety PE guideline (categories A–E; LMWH preferred over UFH, Class 1, in categories C–E1; lysis and catheter therapy Class 2a in E, 2b in D and C3; DOAC preferred over VKA except APS and advanced liver disease; literature closed April 2025);
# sPESI items (Jiménez 2010, via secondary sources), PESI points (MDCalc), HOME-PE (Hestia vs sPESI, 1,974 patients, 30-day composite at home 1.3% vs 1.1%), ESC 2019 ECMO wording (IIb C), EINSTEIN-PE (major bleeding 1.1–1.2% vs 2.2%, composite 10.3% vs 11.4%),
# PREPIC 8-year (PE 6.2% vs 15.1%, DVT 35.7% vs 27.5%), PREPIC2 (399 patients, recurrent PE at 3 months 3% vs 1.5% (reported as 6 vs 3 events), no benefit), TRAPS (stroke 7% and MI 5% vs 0% on warfarin; composite 19–22% vs 3%), Artemis (van der Pol NEJM 2019: 498 women, 3-month VTE 0.21%, CTPA avoided 39%, 65% first and 32% third trimester), fetal dose CTPA and perfusion scan well below 1 mGy.
# Second check 11 Nov 2026 (see resp06b_review.md): ESC 2019 Tables 9–10 and pregnancy section read in full text; AMPLIFY, Hokusai-VTE, RE-COVER, EINSTEIN-PE, PEITHO, PREPIC, PREPIC2, TRAPS, Artemis, HOME-PE, ICOPER, HI-PEITHO and the 2026 AHA/ACC guideline confirmed from published summaries.

SPINE = [
  ("Grading the risk", "Once PE is confirmed, shock or arrest makes it high risk, and in stable patients PESI or sPESI, RV imaging and troponin sort the rest into intermediate-high, intermediate-low and low risk, which decides where and how they are treated."),
  ("Holding up the failing RV", "In high-risk PE the RV is supported with oxygen while avoiding intubation where possible, little or no fluid, noradrenaline to restore its coronary perfusion, and VA-ECMO as a bridge to clot removal when it collapses."),
  ("Anticoagulation for every patient", "Every PE is anticoagulated: LMWH or fondaparinux for most, UFH when reperfusion may follow or the kidneys fail, then a NOAC in preference to warfarin for at least 3 months, longer when the risk persists."),
  ("Thrombolysis for the unstable", "Systemic thrombolysis is for high-risk PE and for rescue when a patient deteriorates on anticoagulation, not for stable intermediate-risk patients, and recent stroke, surgery, trauma or bleeding bars it."),
  ("When lysis fails or is barred", "Surgical embolectomy or catheter-directed treatment replaces lysis when it fails or is contraindicated, and an IVC filter is kept for the patient who cannot be anticoagulated, because it trades fewer PEs for more DVT."),
  ("Pregnancy and the sweep", "In pregnancy the same pathway runs with low-dose imaging and LMWH throughout, warfarin only after delivery and NOACs never, and the true/false sweep tests the beliefs most often wrong across both PE decks."),
]

PRIMER = "RESP06A ended with the diagnosis made; this deck decides how dangerous the PE is and what to do about it. Troponin is released by an ischaemic right ventricle and BNP by a stretched one, so both are markers of RV strain rather than of the clot itself. Anticoagulants do not dissolve clot: they stop it growing while the body’s own fibrinolysis clears it over weeks, whereas thrombolytics (alteplase, tenecteplase) activate plasminogen to dissolve it within hours at the price of bleeding. Heparins work through antithrombin, while NOACs (DOACs) inhibit factor Xa or thrombin directly and are cleared partly by the kidneys."

L = {}

L['PE-14'] = dict(
  sub="Respiratory → Pulmonary embolism → PESI and simplified PESI",
  step=1,
  intro="Step 1 starts once the diagnosis is made: in a stable patient, how likely is death in the next 30 days? PESI and its short form sPESI answer that from bedside items, and they are the first column of the ESC risk table (PE-15). The one real question is arithmetic on the original PESI, and its key is wrong.",
  parts=[
    ('a', "**sPESI: age >80; cancer; chronic heart failure or chronic lung disease; pulse ≥110; systolic BP <100; saturation <90% — one point each.** Heart failure and lung disease count together as one item (chronic cardiopulmonary disease), which is how six items carry seven conditions. Each item marks either a patient with little reserve or a circulation already under strain."),
    ('b', "**sPESI 0: 30-day mortality 1.0%; ≥1 point: 10.9%.** Those are the derivation figures (Jiménez 2010). sPESI 0 identifies a low-risk patient who can be considered for early discharge if RV imaging and troponin, when checked, are normal (PE-15)."),
    ('c', "**Original PESI: altered mental status +60, the heaviest item; Class I ≤65, II 66–85, III 86–105, IV 106–125, V >125.** Start from the age in years, then add male sex +10, cancer +30, heart failure +10, chronic lung disease +10, pulse ≥110 +20, systolic BP <100 +30, respiratory rate ≥30 +20, temperature <36°C +20 and saturation <90% +20. Classes I–II are low risk; III–V count as ‘PESI positive’ in the ESC table, the same as sPESI ≥1."),
  ],
  table=dict(title="Working the real stem (70-year-old man)", head=["Item", "Points"], rows=[["Age 70", "70"], ["Male sex", "+10"], ["Chronic lung disease", "+10"], ["Pulse 118 (≥110)", "+20"], ["SpO₂ 88% (<90%)", "+20"], ["SBP 110, RR 26, temp 36.5°C, normal mentation, no cancer", "0"], ["**Total**", "**130: Class V (>125)**"]]),
  mimic=[
    ("PESI vs sPESI", "PESI weights eleven items and adds age in years, giving five classes; sPESI scores six items one point each and asks only 0 or ≥1. Both answer the same question and either can be used in the ESC table."),
  ],
  traps=[
    ("“This patient is PESI Class IV” [DocT GT key]", "With +10 for male sex the total is 130, which is Class V, and Class V was not offered. The key reaches Class IV (106–125) only by leaving out the male item. If forced, choose the highest class offered, knowing the real answer is V."),
    ("“sPESI counts heart failure and lung disease as two points”", "They are one combined item; a patient with both still scores one."),
  ],
  decode=[
    ("70-year-old man, HR 118, SBP 110, RR 26, temp 36.5°C, SpO₂ 88%, chronic lung disease, no cancer, normal mentation — PESI class? [DocT GT]", "Keyed Class IV; the correct total is 130, Class V."),
    ("[pattern] Which single PESI item scores most?", "Altered mental status, +60."),
  ],
  punch="sPESI scores six items one point each (0 means 1.0% 30-day mortality, ≥1 means 10.9%); the original PESI adds age in years plus weighted items, with altered mentation heaviest (+60) and Class V above 125.",
)

L['PE-15'] = dict(
  sub="Respiratory → Pulmonary embolism → ESC risk classes for early mortality",
  step=1,
  intro="Step 1 puts the pieces together. ESC 2019 sorts every confirmed PE into four classes in a fixed order: the circulation first (PE-05), then the clinical score (PE-14), then the two markers of RV strain (PE-16). The class decides between reperfusion, monitored anticoagulation and home treatment.",
  parts=[
    ('a', "**High risk: haemodynamic instability (shock, arrest or persistent hypotension) — primary reperfusion.** Once the circulation has failed, PESI, imaging and troponin add nothing to the decision; they are marked (+) because they are usually positive but are not needed."),
    ('b', "**Intermediate-high: no shock, PESI III–V or sPESI ≥1, and BOTH RV dysfunction (echo or CT) and a raised troponin — anticoagulate, monitor, rescue reperfusion if the patient deteriorates.** These patients are stable but their RV is both dilated and injured; PEITHO showed that about one in twenty decompensates within a week on heparin alone (PE-21), which is why they are watched closely rather than lysed up front."),
    ('c', "**Intermediate-low: no shock, PESI III–V or sPESI ≥1, with one or neither of RV dysfunction and troponin — anticoagulate and admit.** The score says the patient is not low risk, but the RV is not under combined strain."),
    ('d', "**Low: no shock, PESI I–II or sPESI 0, RV normal — early discharge and home treatment.** Troponin is optional; if it is measured it must be normal. Hestia criteria (eleven yes/no questions, such as oxygen needed, bleeding risk, CrCl <30, pregnancy, social reasons) can be used instead of sPESI to select home treatment; HOME-PE found the two equally safe."),
  ],
  table=dict(title="ESC 2019 risk classes", head=["Class", "Shock", "PESI III–V / sPESI ≥1", "RV on imaging", "Troponin", "Plan"], rows=[["**High**", "yes", "(+)", "+", "(+)", "primary reperfusion"], ["**Intermediate-high**", "no", "+", "**+**", "**+**", "anticoagulate, monitor, rescue lysis"], ["**Intermediate-low**", "no", "+", "one or none", "", "anticoagulate, admit"], ["**Low**", "no", "–", "–", "optional (–)", "early discharge"]]),
  mimic=[
    ("Intermediate-high vs intermediate-low", "Both are stable with a positive score; only intermediate-high has both RV dysfunction and a raised troponin."),
  ],
  traps=[
    ("“PESI I–II or sPESI 0 is always low risk”", "If RV dysfunction or a raised troponin is found anyway, the patient is classed intermediate-low, as the card’s watch line says."),
    ("“Intermediate-high risk means thrombolyse now”", "It means anticoagulate and monitor; lysis is kept for deterioration (PE-21d)."),
  ],
  decode=[
    ("[pattern] Normotensive PE, sPESI 2, RV/LV ratio 1.2 on CT, troponin raised — risk class and plan?", "Intermediate-high: anticoagulate, monitor, rescue reperfusion if he deteriorates."),
    ("[pattern] Normotensive, sPESI 0, raised troponin — risk class?", "Intermediate-low, not low."),
  ],
  punch="Shock makes PE high risk and earns reperfusion; in the stable patient a positive score with both RV dysfunction and troponin is intermediate-high (monitor, rescue lysis), one or neither is intermediate-low, and a negative score with a normal RV is low risk for home treatment.",
)

L['PE-16'] = dict(
  sub="Respiratory → Pulmonary embolism → Prognostic markers",
  step=1,
  intro="Step 1 needs a way to see RV strain in a stable patient. Imaging shows the dilated RV, and blood tests show its injury (troponin) and stretch (natriuretic peptides). Their strength is in reassurance: a normal value makes early death unlikely.",
  parts=[
    ('a', "**On CT, an RV/LV diameter ratio ≥1.0 (0.9 in some studies).** Measured on the four-chamber or axial view; it is the CT counterpart of the dilated RV on echo (PE-12) and counts as RV dysfunction in the ESC table."),
    ('b', "**Troponin I or T (high-sensitivity T 14 pg/mL); BNP or NT-proBNP (600 pg/mL); H-FABP ≥6 ng/mL — high negative but low positive predictive value.** A raised troponin means RV ischaemia, a raised peptide means RV wall stretch. Most patients with a raised marker survive, so a positive result alone does not justify lysis; a normal result makes early death very unlikely. A lactate above 2 mmol/L marks hypoperfusion and also predicts early decompensation."),
    ('c', "**Clinical predictors of early death: age >70, systolic BP <90, RR >20, cancer, COPD, chronic heart failure, immobilisation for neurological disease, concomitant DVT.** ICOPER identified age >70, cancer, heart failure, COPD, systolic BP <90, RR >20 and RV hypokinesis on echo; the others (neurological immobilisation, concomitant DVT) come from later cohorts such as RIETE. They overlap with the PESI items, which is why PESI rather than this list is what guidelines use."),
  ],
  mimic=[],
  traps=[
    ("“A raised troponin in PE means lysis”", "Its positive predictive value is low; it moves a stable patient into an intermediate class, not into reperfusion."),
  ],
  decode=[
    ("[pattern] CT sign of RV dysfunction in PE?", "RV/LV diameter ratio ≥1.0."),
  ],
  punch="RV/LV ratio ≥1.0 on CT, troponin, NT-proBNP (600 pg/mL) and H-FABP (≥6 ng/mL) mark RV strain; they are best at reassuring when normal and do not by themselves justify lysis.",
)

L['PE-17'] = dict(
  sub="Respiratory → Pulmonary embolism → Supporting the failing RV",
  step=2,
  intro="Step 2 is the hour before and during reperfusion. The RV is failing from pressure overload, and every supportive measure is judged by whether it lowers RV afterload, restores RV coronary perfusion or makes things worse (PE-04). Several reflex ICU actions make them worse.",
  parts=[
    ('a', "**Oxygen if saturation <90%, high-flow nasal oxygen preferred; avoid intubation where possible, because induction causes severe hypotension and positive pressure worsens RV function.** Induction agents remove sympathetic tone the patient is relying on, and positive pressure raises intrathoracic pressure, cutting venous return and raising pulmonary vascular resistance, so arrest can follow induction. If intubation is unavoidable, choose drugs that keep the pressure up, have a vasopressor running, and keep tidal volume (about 6 mL/kg) and PEEP low."),
    ('b', "**Cautious fluid: ≤500 mL over 15–30 min, only if CVP is low or normal; more over-distends the RV and lowers output.** A dilated RV pushes the septum into the LV; extra volume worsens that interdependence and raises RV wall tension and oxygen demand."),
    ('c', "**Noradrenaline 0.2–1.0 µg/kg/min restores coronary perfusion; dobutamine 2–20 µg/kg/min for low output with normal BP, which alone may worsen hypotension.** Raising aortic pressure restores the gradient that perfuses the RV wall and breaks the ischaemic loop. Dobutamine improves contractility but vasodilates, so it is added to, not substituted for, a vasopressor in a hypotensive patient."),
    ('d', "**VA-ECMO, with surgical embolectomy or catheter treatment, for refractory collapse or arrest.** ECMO bypasses the obstructed pulmonary circulation and unloads the RV while the clot is removed or lyses; ESC 2019 grades it IIb and pairs it with a reperfusion strategy, since ECMO with anticoagulation alone is less well supported."),
  ],
  mimic=[
    ("RV failure in PE vs LV cardiogenic shock", "Both have low output, but in PE fluid and positive pressure harm and a vasopressor is first; in LV failure diuresis and positive pressure help."),
  ],
  traps=[
    ("“Give a fluid bolus for hypotension in massive PE”", "Large volumes worsen the RV; at most 500 mL, and only if CVP is not high."),
    ("“Intubate early to secure oxygenation”", "Induction and positive pressure can precipitate arrest; use high-flow oxygen if it is enough."),
  ],
  decode=[
    ("[pattern] Massive PE, hypotensive, CVP 18 — first vasoactive drug?", "Noradrenaline; no more fluid."),
    ("[pattern] Refractory arrest from PE — mechanical support?", "VA-ECMO with surgical or catheter clot removal."),
  ],
  extra=[
    dict(q="Why can hypoxaemia worsen suddenly in high-risk PE?", a="When RA pressure exceeds LA pressure a patent foramen ovale opens and shunts right to left, which also risks paradoxical embolism."),
  ],
  punch="Support the failing RV with high-flow oxygen rather than intubation if possible, no more than 500 mL of fluid, noradrenaline to restore its coronary perfusion, and VA-ECMO with clot removal for collapse.",
)

L['PE-18'] = dict(
  sub="Respiratory → Pulmonary embolism → Parenteral anticoagulation",
  step=3,
  intro="Step 3 begins with the drug every PE patient gets. The choice between LMWH, fondaparinux and unfractionated heparin turns on three things: will reperfusion follow, how are the kidneys, and does the drug need monitoring. The real questions test UFH monitoring, heparin resistance and fondaparinux’s properties.",
  parts=[
    ('a', "**LMWH or fondaparinux over UFH for most; UFH for high-risk PE (possible reperfusion), severe renal impairment or severe obesity.** LMWH and fondaparinux are given by weight without monitoring and cause less major bleeding and HIT. UFH is kept for when its short action matters: a patient who may go to lysis, surgery or a catheter within hours, or kidneys that cannot clear LMWH or fondaparinux (CrCl <30). This is the ESC 2019 position; the 2026 AHA/ACC guideline recommends LMWH over UFH (Class 1) for almost all patients, including the more severe categories, but the exam teaching is ESC."),
    ('b', "**UFH 80 U/kg bolus, then 18 U/kg/h; aPTT 1.5–2.5 times control.** The aPTT measures the intrinsic pathway that heparin–antithrombin inhibits; anti-Xa (0.3–0.7 IU/mL for treatment) is used when the aPTT is unreliable. INR monitors warfarin, and daily platelets watch for HIT but do not adjust the dose."),
    ('c', "**Enoxaparin 1 mg/kg every 12 h or 1.5 mg/kg once daily; fondaparinux once daily 5 mg (<50 kg), 7.5 mg (50–100 kg), 10 mg (>100 kg).** Fondaparinux is a synthetic pentasaccharide that binds antithrombin and inhibits only factor Xa. It hardly binds platelet factor 4, so it does not cause HIT (and is used off-label to treat it); it is cleared by the kidneys alone (half-life about 17–21 h), is contraindicated below CrCl 30, and protamine does not reverse it."),
    ('d', "**UFH: short half-life and reversible with protamine; but needs aPTT monitoring and risks HIT.** The half-life is about 1–1.5 h (4–6 h is LMWH, as the watch line notes), so stopping the infusion clears it within hours. When the aPTT stays flat despite large doses (more than about 35,000 U/day), suspect heparin resistance: often antithrombin deficiency, from urinary loss in nephrotic syndrome or consumption in sepsis, DIC or ECMO. Check antithrombin or anti-Xa, then give antithrombin concentrate or switch to a direct thrombin inhibitor (argatroban, bivalirudin)."),
  ],
  mimic=[
    ("Heparin resistance vs pseudo-resistance", "True resistance (low antithrombin) leaves both aPTT and anti-Xa low. A high factor VIII or fibrinogen shortens the aPTT while anti-Xa is adequate, so the dose is right and should be guided by anti-Xa."),
  ],
  traps=[
    ("“Monitor UFH with anti-Xa 1.0–1.5 or INR”", "Treatment UFH is titrated by aPTT 1.5–2.5 times control (73% right); anti-Xa 0.3–0.7 is the alternative, and INR is for warfarin."),
    ("“aPTT flat on 25 U/kg/h in nephrotic sepsis: HIT, factor VIII, or fast renal clearance”", "Antithrombin deficiency: heparin needs antithrombin to work, and nephrotic syndrome loses it in the urine. Heparin is not cleared by the kidneys, and HIT causes low platelets, not a flat aPTT."),
    ("“Fondaparinux is a porcine heparinoid, safe at eGFR 15 and reversed by protamine”", "It is synthetic, contraindicated below CrCl 30 and not reversed by protamine; its distinguishing property is that it does not bind PF4, so it does not cause HIT."),
  ],
  decode=[
    ("ICU patient with acute PE on UFH — monitoring parameter for dose adjustment? [DocT GT, 73% right]", "aPTT 1.5–2.5 times normal."),
    ("Septic shock with nephrotic syndrome, UFH 25 U/kg/h, aPTT stuck at baseline 30 s — cause and next step? [DocT GT]", "Antithrombin deficiency: measure antithrombin or switch to a direct thrombin inhibitor."),
    ("Correct statement about fondaparinux? [DocT GT]", "It does not bind PF4, so it does not cause HIT."),
  ],
  punch="LMWH or fondaparinux for most PE; UFH (80 U/kg then 18 U/kg/h, aPTT 1.5–2.5 times) when reperfusion may follow or the kidneys fail. A flat aPTT on big heparin doses means antithrombin deficiency, and fondaparinux does not cause HIT.",
)

L['PE-19'] = dict(
  sub="Respiratory → Pulmonary embolism → The four NOACs",
  step=3,
  intro="Step 3 continues to the oral drug. Two NOACs can be started on day one with a higher loading dose; the other two were tested only after a few days of heparin, and the trials’ design is why the rules differ. The real questions test where NOACs must not be used: antiphospholipid syndrome and pregnancy.",
  parts=[
    ('a', "**Dabigatran and edoxaban need a parenteral lead-in (LMWH first).** In RE-COVER and Hokusai-VTE every patient had at least 5 days of heparin before the oral drug, so that is how they are licensed. Edoxaban is 60 mg once daily, 30 mg if CrCl 30–50, weight ≤60 kg or a strong P-gp inhibitor; dabigatran 150 mg twice daily."),
    ('b', "**Rivaroxaban 15 mg twice daily for 3 weeks, then 20 mg once daily; apixaban 10 mg twice daily for 7 days, then 5 mg twice daily.** The loading phase gives the extra anticoagulation that heparin gives in the first weeks, when recurrence risk is highest, so these two are started alone from day one. After 6 months, reduced extended doses (apixaban 2.5 mg twice daily, rivaroxaban 10 mg daily) can be used."),
    ('c', "**Trials: RE-COVER (dabigatran), Hokusai-VTE (edoxaban), EINSTEIN-PE (rivaroxaban), AMPLIFY (apixaban).** All were non-inferior to LMWH followed by warfarin for recurrence. Bleeding: AMPLIFY major bleeding 0.6% vs 1.8%; EINSTEIN-PE major bleeding 1.1% vs 2.2% (major plus clinically relevant bleeding was similar, which is the sense in which the watch line calls it ‘similar’); Hokusai-VTE lowered major plus clinically relevant bleeding (8.5% vs 10.3%) but not major bleeding alone (1.4% vs 1.6%); RE-COVER had similar major bleeding (1.6% vs 1.9%) but less bleeding overall."),
    ('d', "**Not recommended in severe renal impairment, pregnancy and lactation, and antiphospholipid syndrome.** All are partly renally cleared (dabigatran most, about 80%); they cross the placenta and enter milk with no safety data; and in APS they failed. In TRAPS (triple-positive APS, rivaroxaban vs warfarin) the trial stopped early: arterial events (stroke 7%, MI 5%) occurred only on rivaroxaban, and the composite was 19–22% vs 3%. So thrombotic APS is treated with warfarin, INR 2–3, indefinitely; LMWH is used in pregnancy."),
  ],
  table=dict(title="Starting the four NOACs", head=["Drug", "Start", "Trial"], rows=[["Dabigatran", "after ≥5 days LMWH; 150 mg twice daily", "RE-COVER"], ["Edoxaban", "after ≥5 days LMWH; 60 mg daily (30 mg if CrCl 30–50 or ≤60 kg)", "Hokusai-VTE"], ["Rivaroxaban", "**15 mg twice daily × 3 weeks**, then 20 mg daily", "EINSTEIN-PE"], ["Apixaban", "**10 mg twice daily × 7 days**, then 5 mg twice daily", "AMPLIFY"]]),
  mimic=[
    ("Xa inhibitors vs dabigatran", "Rivaroxaban, apixaban and edoxaban inhibit factor Xa (andexanet reverses apixaban and rivaroxaban); dabigatran inhibits thrombin directly (reversed by idarucizumab) and depends most on the kidneys."),
  ],
  traps=[
    ("“APS with bilateral PE: a DOAC is preferred long-term”", "Warfarin to INR 2–3 is preferred; DOACs caused more arterial events in TRAPS. Only 47% chose warfarin. Indefinite LMWH is the fallback for warfarin failure or pregnancy."),
    ("“PE at 9 weeks’ pregnancy: IV or subcutaneous UFH, or aspirin, through pregnancy”", "Subcutaneous LMWH throughout (68% right); NOACs and warfarin are avoided in pregnancy (PE-25)."),
  ],
  decode=[
    ("35-year-old with known APS, bilateral PE — preferred long-term therapy? [DocT, 47% right]", "Warfarin, INR 2–3."),
    ("PE at 9 weeks’ gestation — treatment throughout pregnancy? [DocT, 68% right]", "Subcutaneous LMWH."),
  ],
  punch="Rivaroxaban (15 mg twice daily for 3 weeks) and apixaban (10 mg twice daily for 7 days) start alone; dabigatran and edoxaban follow at least 5 days of heparin. Avoid all four in severe renal failure, pregnancy and APS, where warfarin wins.",
)

L['PE-20'] = dict(
  sub="Respiratory → Pulmonary embolism → Oral anticoagulation: general rules",
  step=3,
  intro="Step 3 ends with the long tail of treatment: which oral drug, how to start warfarin, and for how long. The duration depends on why the clot formed, not on how big it was, and that is exactly what the NEET question tests.",
  parts=[
    ('a', "**A NOAC is preferred in eligible patients.** NOACs are at least as effective as warfarin, cause less major and intracranial bleeding, and need no INR monitoring; they have fewer food and drug interactions, though some remain (rifampicin, below). The exceptions are those in PE-19d."),
    ('b', "**Overlap with parenteral anticoagulation for at least 5 days and until INR is 2.0–3.0 (target 2.5).** Warfarin lowers protein C (short half-life) before it lowers factors II and X, so it is briefly prothrombotic; and the INR rises before the patient is truly anticoagulated, because factor VII falls first and prothrombin takes days. ESC asks for the INR in range on two consecutive days before stopping heparin."),
    ('c', "**3 months for every patient; that is sufficient for a provoked PE; longer for unprovoked or recurrent events.** ESC 2019 words it by risk factor: 3 months when the first PE followed a major transient or reversible factor (surgery, trauma); extended, open-ended treatment for recurrence not linked to a major transient factor and for APS; and extended treatment should be considered when no factor is found, a persistent factor remains or only a minor transient factor was present. Femur fracture surgery is a major transient factor, so 3 months."),
  ],
  mimic=[
    ("Major transient vs persistent risk factor", "Surgery, trauma or a fracture with immobilisation is over once the patient recovers: 3 months. Active cancer or APS persists: treatment continues while it does."),
  ],
  traps=[
    ("“DOACs bleed more than warfarin, especially intracranially” or “VKAs are preferred long-term”", "The reverse: DOACs cause less intracranial haemorrhage and are preferred for long-term PE treatment."),
    ("“DVT after femur fracture surgery: 6 months or lifelong”", "A first event after a major transient factor needs 3 months."),
    ("“TB patient on rifampicin, warfarin started, dies of PE: the warfarin dose was too high”", "Rifampicin induces CYP2C9 and CYP3A4 and clears warfarin fast, so the INR stays low and the clot grows; it also lowers DOAC levels."),
  ],
  decode=[
    ("Correct statement on DOACs: more bleeding, VKAs preferred, or DOACs preferred long-term? [DocT GT]", "DOACs are preferred over VKAs for long-term management of PE."),
    ("DVT after femur fracture surgery, stable, no prior thrombosis — duration? [NEET 2025 recall]", "3 months."),
    ("TB on rifampicin, then warfarin, dies of PE — trigger? [Marrow]", "Rifampicin induction lowering warfarin levels."),
  ],
  punch="Prefer a NOAC; if warfarin is used, overlap heparin for at least 5 days and until the INR is 2–3. Three months suffices after a major transient factor such as surgery; recurrence, APS or a persistent factor needs extended treatment.",
)

L['PE-21'] = dict(
  sub="Respiratory → Pulmonary embolism → Systemic thrombolysis",
  step=4,
  intro="Step 4 is reperfusion. Thrombolysis dissolves clot in hours rather than weeks, which saves an RV that is failing now, but it costs bleeding, including intracranial bleeding. So it is given where the RV is failing (high risk) and held back where it is only strained (intermediate risk). The questions test exactly that split and the standard regimen.",
  parts=[
    ('a', "**High-risk PE; and rescue for haemodynamic deterioration on anticoagulation.** In shock the benefit of fast clot removal outweighs the bleeding risk. An intermediate-risk patient who deteriorates on heparin has become high risk, so rescue lysis is the same logic applied later."),
    ('b', "**Greatest benefit within 48 hours; some benefit up to 2 weeks.** Fresh clot is rich in fibrin that plasmin can reach; older clot organises. About nine in ten patients improve clinically and on echo within 36 hours."),
    ('c', "**rtPA 100 mg over 2 h, or 0.6 mg/kg over 15 min (maximum 50 mg); streptokinase 250,000 IU over 30 min then 100,000 IU/h for 12–24 h (accelerated 1.5 million IU over 2 h); urokinase 4400 IU/kg over 10 min then 4400 IU/kg/h for 12–24 h.** Alteplase 100 mg over 2 hours is the standard answer for massive PE with shock. The accelerated 0.6 mg/kg regimen is used in arrest; in cardiac arrest lysis is given and CPR continued for 60–90 minutes. Reduced-dose alteplase in stable patients is still being tested (PEITHO-3, below)."),
    ('d', "**Routine primary thrombolysis is not recommended in intermediate-risk PE.** PEITHO (Meyer, NEJM 2014; 1,005 intermediate-high-risk patients, tenecteplase plus heparin vs heparin) cut death or decompensation at 7 days from 5.6% to 2.6%, almost all by preventing decompensation; death at 7 days (1.2% vs 1.8%) and at 30 days (2.4% vs 3.2%) did not differ. The price was extracranial major bleeding 6.3% vs 1.2% and stroke 2.4% vs 0.2%, mostly haemorrhagic (intracranial haemorrhage 2.0% vs 0.2%). So these patients get anticoagulation and monitoring, with rescue lysis on deterioration. Two newer trials target the same group: PEITHO-3 (alteplase 0.6 mg/kg, maximum 50 mg, vs placebo) is no longer recruiting and has not yet reported; HI-PEITHO (NEJM 2026; 544 patients) found ultrasound-facilitated catheter lysis cut the 7-day composite from 10.3% to 4.0%, almost all by preventing decompensation (3.7% vs 10.3%), with no intracranial bleeding and no mortality difference (PE-23)."),
    ('e', "**Tenecteplase is more fibrin-selective, resistant to plasminogen activator inhibitor, and given as a single bolus over 5 seconds (weight-based 30–50 mg).** The PEITHO doses rise by 5 mg per 10 kg: 30 mg under 60 kg up to 50 mg at 90 kg or more. A single bolus suits arrest and transfer, but tenecteplase is not in the ESC 2019 regimen table for PE and is used off-label."),
  ],
  table=dict(title="Who gets what", head=["Risk class", "Reperfusion"], rows=[["High (shock, arrest)", "**systemic lysis — alteplase 100 mg over 2 h**; embolectomy or catheter if lysis is barred or fails"], ["Intermediate-high", "anticoagulate and monitor; **rescue** lysis if he deteriorates"], ["Intermediate-low, low", "anticoagulation only"]]),
  mimic=[
    ("Intermediate-high PE vs high-risk PE", "Both may have a dilated RV and raised troponin; only shock, arrest or persistent hypotension makes lysis first-line."),
  ],
  traps=[
    ("“Intermediate-risk PE with RV dysfunction: immediate thrombolysis”", "Anticoagulate with enoxaparin and monitor; PEITHO prevented decompensation but did not save lives and caused intracranial bleeding."),
    ("“Shock after spine surgery: IV heparin is the treatment of choice”", "That is the least likely true statement (42% right): shock is high-risk PE needing reperfusion, and with lysis barred by surgery that means surgical or catheter embolectomy (PE-22, PE-23)."),
    ("“Massive PE with shock: oral apixaban, oxygen and observation, or a leg ultrasound first”", "Shock needs reperfusion now: alteplase 100 mg over 2 hours."),
  ],
  decode=[
    ("50-year-old with massive PE and shock — immediate treatment? [DocT GT]", "Alteplase 100 mg over 2 hours."),
    ("Intermediate-risk PE, RV dysfunction, stable BP — initial management? [DocT GT]", "Anticoagulation with enoxaparin."),
    ("After spinal surgery: SpO₂ 86%, HR 124, BP 85/41, EtCO₂ 15 — statement LEAST likely true? [DocT GT, 42% right]", "‘IV heparin is the treatment of choice’."),
  ],
  punch="Lysis is for shock (alteplase 100 mg over 2 h) and for rescue on deterioration; in intermediate-high risk PEITHO cut decompensation (5.6% to 2.6%) but not death, at 2% intracranial haemorrhage, so those patients are anticoagulated and watched.",
)

L['PE-22'] = dict(
  sub="Respiratory → Pulmonary embolism → Contraindications to thrombolysis",
  step=4,
  intro="Step 4 continues with who cannot be lysed. The absolute list is the set of conditions where the bleed would be in the brain or uncontrollable; the relative list raises risk but can be accepted when the patient is dying of PE. The questions test the 6-month stroke rule and what to do when the operation was yesterday.",
  parts=[
    ('a', "**Absolute: haemorrhagic stroke or stroke of unknown origin at any time; ischaemic stroke in the last 6 months; CNS neoplasm; major trauma, surgery or head injury in the last 3 weeks; bleeding diathesis; active bleeding.** Each is a site where plasmin would open a bleed that cannot be compressed or stopped. Recent surgery means a fresh wound and haemostatic plugs that lysis would dissolve, which is why PE on day 1 after hip replacement goes to embolectomy, not lysis."),
    ('b', "**Relative: TIA in the last 6 months; oral anticoagulation; pregnancy or first week post-partum; non-compressible punctures; traumatic resuscitation; refractory hypertension (systolic >180); advanced liver disease; infective endocarditis; active peptic ulcer.** These raise bleeding risk but are weighed against the risk of dying; in a pregnant woman in shock from PE, lysis is given (PE-25)."),
  ],
  table=dict(title="The stroke rule differs by guideline", head=["Setting", "Ischaemic stroke counted as absolute"], rows=[["ESC PE 2019 and ESC STEMI", "**within 6 months**"], ["AHA STEMI", "within 3 months"], ["Either way", "a stroke 2 months ago bars lysis"]]),
  mimic=[
    ("Ischaemic stroke vs TIA within 6 months", "An ischaemic stroke within 6 months is absolute; a TIA within 6 months is relative, as the watch line warns."),
  ],
  traps=[
    ("“Ischaemic stroke 2 months ago: eligible, or barred only if on anticoagulation or SBP >140”", "Absolute contraindication (71% right)."),
    ("“Unstable despite lysis: give more alteplase, or switch to oral anticoagulation”", "Move to catheter-directed treatment or surgical embolectomy (100% right; PE-23)."),
    ("“Massive PE the day after hip replacement: thrombolyse”", "Surgery within 3 weeks is absolute; surgical (or catheter) embolectomy."),
  ],
  decode=[
    ("Massive PE with shock, ischaemic stroke 2 months ago — fibrinolysis eligibility? [DocT GT, 71% right]", "Absolute contraindication."),
    ("Anterior STEMI, PCI 3 hours away, ischaemic stroke 2 months ago — strongest reason to withhold lysis? [DocT GT]", "The recent ischaemic stroke."),
    ("Massive PE still unstable after systemic lysis — next? [DocT GT, 100% right]", "Catheter-directed therapy or embolectomy."),
    ("Massive PE on day 1 after hip replacement — therapy? [Marrow]", "Surgical embolectomy."),
  ],
  punch="Haemorrhagic stroke ever, ischaemic stroke within 6 months, CNS tumour, major surgery or trauma within 3 weeks, bleeding diathesis and active bleeding are absolute; a TIA within 6 months, pregnancy and anticoagulation are only relative.",
)

L['PE-23'] = dict(
  sub="Respiratory → Pulmonary embolism → When thrombolysis fails or is contraindicated",
  step=5,
  intro="Step 5 is the patient who needs the clot out but cannot be lysed, or was lysed and is still in shock. The options remove clot mechanically, either with the chest open or through a catheter, and catheters can deliver a small dose of lytic exactly where it is needed.",
  parts=[
    ('a', "**Surgical embolectomy for high-risk and selected intermediate-high-risk patients; done on normothermic cardiopulmonary bypass, clot removed down to segmental level.** ESC 2019 recommends it for high-risk PE when lysis is contraindicated or has failed, and as an alternative to rescue lysis in the deteriorating patient. It is also favoured for a clot in transit through a patent foramen ovale. Bypass takes over the circulation so the pulmonary arteries can be opened without the heart beating against them."),
    ('b', "**Without lysis: pigtail fragmentation, rheolytic (AngioJet), suction and rotational thrombectomy; with lysis: catheter-directed, ultrasound-assisted (EKOS) and pharmacomechanical.** Catheter lysis delivers a small fraction of the systemic dose straight into the clot, so it lowers RV strain with less bleeding; ultrasound loosens the fibrin to let the drug in. ESC 2019 suggests it for high-risk PE when lysis is barred or fails, and for the deteriorating intermediate-high patient. HI-PEITHO (NEJM 2026; 544 patients) tested EKOS plus heparin against heparin alone in intermediate-high-risk PE: the 7-day primary composite (led by PE-related death and decompensation) fell from 10.3% to 4.0%, driven by decompensation (3.7% vs 10.3%); there was no intracranial bleeding, major bleeding did not differ significantly (about 4% vs 2–3%), and mortality did not differ. The commonest complication of catheter lysis is access-site and minor bleeding; intracranial haemorrhage is rare."),
  ],
  mimic=[
    ("Surgical vs catheter embolectomy", "Surgery needs bypass and a cardiac surgeon but removes clot completely and handles clot in transit; catheter methods need only a cath lab and work through a vein."),
  ],
  traps=[
    ("“The commonest complication of catheter-directed thrombolysis is haemorrhagic stroke” [Marrow key]", "Access-site and other minor bleeding is commonest; intracranial haemorrhage is rare with the small catheter doses (none in either arm of HI-PEITHO). Choose the key only if it is the sole bleeding option offered."),
  ],
  decode=[
    ("Massive PE on day 1 after hip replacement — therapy? [Marrow]", "Surgical embolectomy (lysis barred by surgery within 3 weeks)."),
    ("Commonest complication of catheter-directed thrombolysis? [Marrow]", "Keyed haemorrhagic stroke; in practice access-site bleeding."),
  ],
  punch="When lysis is barred or fails, take the clot out: surgical embolectomy on bypass or catheter treatment, with or without a small dose of local lytic, which bleeds far less than systemic lysis.",
)

L['PE-24'] = dict(
  sub="Respiratory → Pulmonary embolism → Inferior vena cava filters",
  step=5,
  intro="Step 5 ends with a device that stops clot reaching the lung but does nothing to the clot in the leg. That is its whole trade-off, and it is why the filter is for patients who cannot have the drug that does treat the clot. The questions test the indication and what to do when PE happens with a filter in place.",
  parts=[
    ('a', "**Absolute contraindication to anticoagulation; recurrent PE despite adequate anticoagulation; routine use is not recommended.** Active gastrointestinal bleeding with an acute PE is the classic case: place a retrievable filter, and start anticoagulation and remove the filter once the bleeding stops. PREPIC2 (399 patients with PE and DVT, retrievable filter plus anticoagulation vs anticoagulation alone) found no reduction in recurrent PE at 3 months (3% vs 1.5%), so a filter adds nothing when the patient can be anticoagulated."),
    ('b', "**Infrarenal IVC; retrievable or permanent.** Below the renal veins, so a filter thrombus does not threaten the kidneys; a suprarenal filter is used when clot extends above the renal veins or in pregnancy. Retrievable filters should come out once anticoagulation is possible, because complications rise with time."),
    ('c', "**Fewer recurrent PEs at the cost of more DVT.** In PREPIC at 8 years, symptomatic PE was 6.2% vs 15.1%, but DVT was 35.7% vs 27.5%, with no survival difference. The filter catches clot, and the caught clot and the device itself slow flow and make more."),
    ('d', "**Recurrent DVT, IVC occlusion, migration, tilting, caval wall penetration, fracture and fragment embolisation, device thrombosis.** A new PE with a filter in place suggests clot on or above the filter, or through collaterals; after anticoagulation, image the filter (Doppler ultrasound or CT of the IVC), and a retrievable filter with thrombus may need thrombectomy and removal."),
  ],
  mimic=[
    ("Filter vs anticoagulation", "Anticoagulation treats the clot and prevents new ones; a filter only intercepts emboli and increases DVT, so it substitutes only when anticoagulation is impossible."),
  ],
  traps=[
    ("“Acute PE with active GI bleeding: systemic lysis, catheter lysis, or a routine filter for proximal DVT”", "Bleeding bars both kinds of lysis; the answer is a retrievable IVC filter, with anticoagulation once bleeding stops (60–74% right). ‘Routine filter’ is wrong because filters are never routine."),
    ("“IVC filters reduce DVT”", "They increase DVT (PE-26h)."),
  ],
  decode=[
    ("Acute PE, cannot be anticoagulated because of active GI bleeding — next step? [DocT and DocT GT, 60% right]", "Retrievable IVC filter."),
    ("ICU patient with PE and active GI bleeding — best management? [DocT GT, 74% right]", "IVC filter."),
    ("PE in a patient with an IVC filter — next step after heparin? [Marrow]", "Ultrasound of the IVC for filter thrombus."),
  ],
  punch="An IVC filter is for the patient who cannot be anticoagulated (active bleeding) or clots through full anticoagulation; placed infrarenally and retrieved when possible, it trades fewer PEs for more DVT and is never routine.",
)

L['PE-25'] = dict(
  sub="Respiratory → Pulmonary embolism → PE in pregnancy",
  step=6,
  intro="Step 6 brings the whole pathway into pregnancy, the card asked most in this deck. Nothing about PE changes its danger, so the same rules apply — treat on suspicion, image to confirm, lyse in shock — but three things change: D-dimer rises naturally, imaging must count fetal radiation, and the drug must not cross the placenta. The seven questions test each of these and what happens after delivery.",
  parts=[
    ('a', "**A leading cause of maternal death in developed countries; risk highest post-partum, especially after caesarean section.** Pregnancy is hypercoagulable (more fibrinogen and factors VII, VIII and X, less protein S), the gravid uterus slows venous return from the legs, and delivery adds vessel injury; risk peaks in the 6 weeks after birth."),
    ('b', "**Start LMWH; chest X-ray, and leg ultrasound if DVT is suspected (a proximal DVT ends the work-up); normal X-ray: CTPA or perfusion scan; abnormal X-ray: CTPA.** Heparin starts while tests are done, as in any patient with high or intermediate probability (PE-13); both DocT GT questions key ‘begin IV heparin immediately’, and either heparin answers that. A proximal DVT confirms VTE without chest radiation. A normal film makes a perfusion scan readable; an abnormal one makes it non-diagnostic, so CTPA. D-dimer rises through pregnancy, so a fixed cut-off is positive in most women by the third trimester; a negative result still helps, but only within a validated pathway. In the Artemis study (van der Pol, NEJM 2019; 498 women) the pregnancy-adapted YEARS algorithm (leg ultrasound if DVT signs; no YEARS item and D-dimer <1000 ng/mL, or ≥1 item and <500, excludes PE) missed one VTE at 3 months (0.21%) and avoided CTPA in 39% — 65% in the first trimester but only 32% in the third. ESC 2019 recommends formal assessment with a validated pathway in pregnancy."),
    ('c', "**Fetal danger threshold 50 mSv (ESC 2019: 50–100); all tests fall well below it.** ESC 2019 writes the threshold in mSv; strictly, fetal absorbed dose is measured in mGy, and for X-rays the two numbers are the same. ESC lists fetal doses of 0.05–0.5 mGy for CTPA and a similar fraction of a milligray for perfusion scanning, so both are at least a hundred times below the threshold. The real difference is the mother’s breast dose, which is far higher with CTPA (3–10 mGy). So neither test is withheld for fear of the fetus."),
    ('d', "**LMWH is the drug of choice; UFH is also safe (neither crosses the placenta). Vitamin K antagonists cause embryopathy and fetal bleeding; NOACs are contraindicated.** LMWH is given in a fixed therapeutic dose based on early-pregnancy weight. Warfarin crosses the placenta: in weeks 6–12 it causes nasal hypoplasia and stippled epiphyses, and later fetal bleeding. NOACs cross the placenta and are untested. In shock, the pregnant woman is lysed or has embolectomy as any other patient would, because pregnancy is only a relative contraindication (PE-22). After delivery, anticoagulation continues for at least 6 weeks post-partum and at least 3 months in total; warfarin and LMWH are both safe in breastfeeding, so switching to warfarin after delivery is standard, while NOACs are avoided during breastfeeding."),
  ],
  table=dict(title="Through and after pregnancy", head=["Phase", "Drug"], rows=[["Suspected PE", "**heparin now**, then imaging"], ["Pregnancy (all trimesters)", "**LMWH**, weight-based; UFH if renal failure or delivery imminent"], ["Shock", "**thrombolysis** or embolectomy"], ["After delivery", "LMWH or **warfarin** (INR 2–3), ≥6 weeks post-partum and ≥3 months in total"], ["Never in pregnancy or breastfeeding", "NOACs; warfarin not during pregnancy"]]),
  mimic=[
    ("Warfarin in pregnancy vs post-partum", "Teratogenic in pregnancy because it crosses the placenta; safe after delivery and in breastfeeding because little enters milk."),
  ],
  traps=[
    ("“A negative D-dimer (<500 ng/mL) is highly reliable in the third trimester”", "D-dimer rises through pregnancy and is above 500 in most women by the third trimester; only a pregnancy-adapted pathway uses it. The keyed answer is that V/Q or CTPA can be done safely."),
    ("“Thrombolysis is strictly contraindicated in pregnancy, even in shock”", "Pregnancy is a relative contraindication; an unstable pregnant woman with PE is lysed (NEET 2024 recall)."),
    ("“Warfarin is the safest anticoagulant for the fetus in the third trimester”", "Warfarin crosses the placenta and causes fetal bleeding; LMWH is the drug in all trimesters."),
    ("“Pregnancy PE at 9 weeks: IV UFH, subcutaneous UFH or aspirin throughout”", "Subcutaneous LMWH throughout (68% right); UFH is safe but needs monitoring and causes more HIT and osteoporosis."),
    ("“After delivery, stop anticoagulation, keep IV heparin for 6 months, or switch to aspirin”", "Continue anticoagulation for at least 6 weeks post-partum and 3 months in total; warfarin is the keyed choice."),
  ],
  decode=[
    ("PE at 9 weeks’ gestation — treatment throughout pregnancy? [DocT, 68% right]", "Subcutaneous LMWH."),
    ("32 weeks, pleuritic pain, SpO₂ 91% on 4 L, PE suspected — most appropriate statement? [DocT GT]", "V/Q or CTPA can be done safely; the fetal dose is well below the teratogenic threshold."),
    ("32 weeks, sudden dyspnoea, pleuritic pain, hypoxia, PE strongly suspected — initial step? [DocT GT, twice, 81% and 100% right]", "Begin IV heparin immediately."),
    ("PE in pregnancy treated with heparin, now delivered — post-partum strategy? [DocT GT, twice]", "Switch to warfarin for at least 6–8 weeks post-partum (≥3 months in total)."),
  ],
  extra=[
    dict(q="Pregnant woman with unstable PE: thrombolysis, LMWH or UFH? [NEET 2024 recall]", a="Thrombolysis: shock is high-risk PE, and pregnancy is only a relative contraindication."),
  ],
  punch="In pregnancy, start heparin, image without fear (fetal doses are far below 50–100 mGy), treat with weight-based LMWH throughout, lyse if she is in shock, and after delivery continue LMWH or warfarin for at least 6 weeks; NOACs never.",
)

L['PE-26'] = dict(
  sub="Respiratory → Pulmonary embolism → True or false sweep",
  step=6,
  intro="Step 6 closes both PE decks with the beliefs that are most often wrong. Each line points back to the card that explains it, and the real questions linked here test the ECG, the D-dimer and the filter.",
  parts=[
    ('a', "**False: sinus tachycardia is the commonest ECG finding.** S1Q3T3 appears in only about one in five; tachycardia with non-specific ST–T changes is commonest (PE-07)."),
    ('b', "**False: in high clinical probability go straight to CTPA.** A normal D-dimer cannot exclude PE when it is likely, and a raised one means little in hospital or ICU patients, where sepsis, surgery and age all raise it (PE-10)."),
    ('c', "**True: a normal perfusion scan excludes PE.** No perfusion defect means no embolus large enough to matter (PE-11)."),
    ('d', "**False: high-risk PE is defined by haemodynamic instability, not by a saddle embolus.** A saddle clot in a normotensive patient is not high risk (PE-05, PE-15)."),
    ('e', "**False: rivaroxaban needs no heparin lead-in; it starts at 15 mg twice daily for 3 weeks.** Dabigatran and edoxaban are the two that need heparin first (PE-19)."),
    ('f', "**True: NOACs are avoided in antiphospholipid syndrome.** TRAPS showed more arterial events than with warfarin (PE-19d)."),
    ('g', "**False: primary thrombolysis is not recommended in intermediate-risk PE; rescue only.** PEITHO prevented decompensation but not death and caused intracranial bleeding (PE-21d)."),
    ('h', "**False: IVC filters increase DVT.** They reduce PE (PREPIC at 8 years) at the cost of more DVT (PE-24)."),
  ],
  mimic=[],
  traps=[
    ("“Commonest ECG finding after a long flight with calf pain is S1Q3T3”", "Tachycardia with non-specific ST–T changes; only 37% chose it."),
    ("“A raised D-dimer in a septic ICU patient confirms PE or calls for lysis”", "It is non-specific in critical illness; only a normal value has meaning, and only when probability is not high."),
    ("“PE with active GI bleeding: systemic or catheter lysis”", "Retrievable IVC filter (60% right)."),
  ],
  decode=[
    ("Breathless at rest 2 days after a 7-hour flight, left calf pain — commonest ECG finding? [DocT, 37% right]", "Tachycardia with non-specific ST–T changes."),
    ("Septic ICU patient with a raised D-dimer — meaning? [DocT GT]", "Non-specific; D-dimer is raised in critical illness."),
    ("Acute PE, anticoagulation impossible because of GI bleeding — next step? [DocT GT, 60% right]", "Retrievable IVC filter."),
  ],
  punch="Tachycardia, not S1Q3T3; CTPA, not D-dimer, in high probability; a normal perfusion scan excludes PE; instability, not clot size, makes PE high risk; rivaroxaban needs no lead-in; no NOACs in APS; lysis in intermediate risk only as rescue; filters increase DVT.",
)

FLAGS = {}
FLAGS['PE-14'] = "Card is right. DocT GT key ‘Class IV’ is wrong: 70 + male 10 + lung disease 10 + pulse 20 + SpO₂ 20 = 130 = Class V (not offered). Minor: watch line says ‘RR >30’; PESI uses RR ≥30."
FLAGS['PE-18'] = 'Card a (UFH for high-risk PE) follows ESC 2019; the 2026 AHA/ACC multisociety guideline recommends LMWH over UFH (Class 1) for initial parenteral anticoagulation in almost all patients, including its more severe categories. Not wrong for ESC-based teaching, but dated outside it. Consider adding fondaparinux facts the questions test: no PF4 binding (no HIT), contraindicated below CrCl 30, not reversed by protamine; and heparin resistance (antithrombin deficiency).'
FLAGS['PE-19'] = 'Watch line is inaccurate on bleeding. EINSTEIN-PE (rivaroxaban) roughly halved major bleeding (1.1% vs 2.2%); only major plus clinically relevant bleeding was similar (10.3% vs 11.4%). Hokusai-VTE (edoxaban) lowered major plus clinically relevant bleeding (8.5% vs 10.3%) but not major bleeding (1.4% vs 1.6%), so ‘clearly lower’ overstates it. RE-COVER (dabigatran) major bleeding was similar (1.6% vs 1.9%), any bleeding lower. DocT line on TRAPS (‘12% vs 3%’) mixes outcomes: thromboembolic (all arterial) events 12% vs 0%; composite with bleeding and death 19–22% vs 3%.'
FLAGS['PE-20'] = "Card c uses ‘provoked/unprovoked’; ESC 2019 frames duration by major transient/reversible, minor transient, persistent or no identifiable risk factor (3 months only for a major transient factor). Consider adding the rifampicin–warfarin/DOAC interaction (Marrow question; see top-up T_51989536)."
FLAGS['PE-21'] = 'Not an error; update: PEITHO-3 (alteplase 0.6 mg/kg, max 50 mg, vs placebo) is active, not recruiting, no results yet. HI-PEITHO (NEJM 2026, 544 patients) showed ultrasound-facilitated catheter lysis cut the 7-day composite (4.0% vs 10.3%; decompensation 3.7% vs 10.3%) in intermediate-high-risk PE, with no ICH and no mortality difference. 2026 AHA/ACC: advanced therapy may be considered in category D, role unclear in C3, systemic lysis harmful in A–C2. Card e: tenecteplase is not in the ESC 2019 regimen table (ESC: not approved for PE).'
FLAGS['PE-23'] = "Marrow key ‘haemorrhagic stroke’ as the commonest complication of catheter-directed lysis is doubtful; access-site/minor bleeding is commonest, ICH rare (none in HI-PEITHO). Consider adding catheter-lysis complications and HI-PEITHO to card b."
FLAGS['PE-24'] = "Card is right. Marrow note: consider adding to d — PE with a filter in place → image the IVC/filter (Doppler US) for filter thrombus; retrievable filter → thrombectomy and removal."
FLAGS['PE-25'] = 'Card c gives the threshold in mSv, as the ESC 2019 text itself does (‘50–100 mSv’); fetal absorbed dose is properly expressed in mGy (numerically equal for X-rays), so minor only. Card b omits the pregnancy-adapted YEARS pathway (Artemis, van der Pol NEJM 2019; ESC 2019 recommends a validated pathway in pregnancy) and post-partum duration (ESC 2019: ≥6 weeks after delivery, ≥3 months in total; LMWH or warfarin in breastfeeding, NOACs not recommended), which DocT tests twice; consider adding.'
