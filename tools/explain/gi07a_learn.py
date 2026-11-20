# GI07A — Explain v3 ("Learn" depth): cirrhosis, part 1 — portal circulation (anatomy, hepatic arterial buffer response, HVPG, why pressure rises, complications), staging and
# scores (D’Amico stages, Child-Pugh, MELD), GI bleeding (sources, acute variceal bleeding, Sengstaken–Blakemore tube, drugs), ascites and hydrothorax (SAAG, sodium and treatment,
# hepatic hydrothorax), true/false sweep.
# No mnemonics or hooks. Driven by qpack/GI07A.md (39 question links; CLD-10 acute variceal bleeding asked 15 times, CLD-07 Child-Pugh 5, CLD-12 drugs 4, CLD-05, CLD-11 and CLD-14 three each).
# CLD-01, 02, 03, 15 and 16 have no linked question and get short explanations with [pattern] decode items. No Top-up cards for GI07A (gi_topups.json checked 20 Nov 2026).
# qbank.json `fix`: one entry, CLD-14 d (no serum-albumin target; ATTIRE) — used and FLAGGED. gi_cardlayer.json `lines` and `cross` notes read and used (CLD-05 to CLD-14).
# Checked online on 20 Nov 2026:
#  - Baveno VII (de Franchis, J Hepatol 2022; pre-proof full text): CSPH = HVPG ≥10 mmHg (1.10); NSBB to prevent decompensation in CSPH (5.14), carvedilol preferred in compensated cirrhosis (5.15);
#    AVB: conservative red cell transfusion, target Hb 7–8 g/dL (6.2); intubation before endoscopy if altered consciousness (6.3); vasoactive drug as soon as possible, 2–5 days (6.5);
#    ceftriaxone 1 g/24 h in advanced cirrhosis (6.9); endoscopy within 12 h once resuscitated (6.17); erythromycin before endoscopy if no long QT (6.19); pre-emptive PTFE-covered TIPS within
#    72 h, ideally <24 h (6.27); balloon tamponade or self-expanding metal stent as bridge, SEMS as effective and safer (6.29); salvage TIPS (6.30); FFP not recommended (6.36); no evidence that
#    platelet count or fibrinogen predict failure (6.37); rFVIIa and tranexamic acid not recommended (6.38); secondary prophylaxis NSBB or carvedilol + EVL (7.8).
#    Pre-emptive TIPS high-risk criteria (Child C <14, or Child B >7 with active bleeding at endoscopy; Baveno VI/VII, confirmed in a WJG 2021 review); HVPG >20 linked to treatment failure.
#  - HALT-IT (Lancet 2020, n 12,009; TXA 1 g then 3 g over 24 h): death from bleeding within 5 days 4% vs 4% (RR 0.99); venous thromboembolism 0.8% vs 0.4% (RR 1.85).
#  - ATTIRE (NEJM 2021, n 777 analysed; hospitalised decompensated cirrhosis, albumin <30 g/L): targeted 20% albumin to serum albumin ≥30 g/L; composite of infection, renal dysfunction or death
#    29.7% vs 30.2% (NS); more serious pulmonary oedema/fluid overload (23 vs 8 events). (The qpack DocT line says target 3.5 g/dL; the trial target was 3.0 g/dL.)
#  - BSG 2020 ascites guideline (Gut): SAAG cut-off 11 g/L; spironolactone 100→400 mg, furosemide 40→160 mg; weight loss ≤0.5 kg/day (no oedema) or ≤1 kg/day (oedema); albumin 8 g per litre
#    after >5 L paracentesis; SBP albumin 1.5 g/kg then 1 g/kg day 3; fluid restriction 1–1.5 L/day only if hypervolaemic and Na <125; hypertonic saline only for severe symptoms; satavaptan no better
#    than placebo for ascites; TIPS for refractory ascites (strong), midodrine weak, alfapump only in special circumstances; terlipressin discussed for HRS-AKI only; ANSWER 18-month survival 77%
#    vs 66% (HR 0.62), not recommended for routine use in the UK.
#  - MELD: dialysis at least twice (or CVVHD ≥24 h) in the past week → creatinine set to 4.0 mg/dL (Radiopaedia, MDCalc); 3-month mortality bands from Wiesner 2003 (≤9 1.9%, 10–19 6.0%,
#    20–29 19.6%, 30–39 52.6%, ≥40 71.3%).
# Second check (independent review, 20 Nov 2026), verified online: D’Amico 2006 stages 1-year mortality 1/3/20/57% (Zipprich, Liver Int 2012, citing D’Amico J Hepatol 2006);
#  Villanueva NEJM 2013 (threshold 7 vs 9 g/dL; 6-week survival 95% vs 91%, HR 0.55; rebleeding 10% vs 16%; cirrhosis benefit Child A/B only; HVPG rose only in the liberal arm);
#  Lau NEJM 2007 (omeprazole 80 mg + 8 mg/h; endotherapy 19.1% vs 28.4%; no difference in rebleeding, surgery or 30-day death); MELD 3.0 (Kim, Gastroenterology 2021: female 1.33,
#  albumin bounded 1.5–3.5, Na 125–137, creatinine cap 3.0, C-statistic 0.869 vs 0.862; OPTN allocation from 13 July 2023; dialysis ≥2 in a week or CRRT → creatinine 3.0 in MELD 3.0,
#  4.0 in MELD/MELD-Na); 2020 cirrhotic cardiomyopathy criteria (LVEF ≤50% or GLS <18%; ≥3 of 4 diastolic criteria; ECG/QT only a research area); POPH ESC/ERS 2022 haemodynamics and
#  Krowka transplant mortality bands; Sengstaken–Blakemore (StatPearls, LITFL: gastric 250–300 mL, oesophageal 30–45 mmHg, ~90% initial control, ~50% rebleed on deflation);
#  hepatic hydrothorax (Annals of Hepatology review: >500 mL, 85% right/13% left/2% bilateral, SBEM PMN >250 culture-positive or >500 culture-negative); Baveno VII text (6.2, 6.11, 6.19,
#  6.27 incl. HVPG >20, 6.29, 6.36–6.38, 9.11). From standard references, not re-checked: Child-Turcotte 1964, Pugh 1973, Mansour 1997, Merion 2005, Runyon 1992, FDA 2013 tolvaptan,
#  HPS criteria (ERS/ILTS), EASL 2018 salt 80–120 mmol/day. Not verifiable: the CLD-09 source table (single series in the notes).

SPINE = [
  ("Portal blood and its pressure", "The portal vein brings three-quarters of the liver’s blood at low pressure, the hepatic artery adjusts to it through adenosine, and the wedged-minus-free hepatic venous gradient measures the sinusoidal pressure between them."),
  ("Resistance and flow raise pressure", "Cirrhosis raises intrahepatic resistance first, splanchnic vasodilatation then raises inflow, and every complication of portal hypertension follows from collaterals, a high sinusoidal pressure or the vasodilated circulation."),
  ("Staging and scoring severity", "Decompensation (ascites, bleeding, encephalopathy, jaundice) is the turning point for survival, and Child-Pugh and MELD grade how close the liver is to failure using bilirubin, INR and either clinical signs or creatinine."),
  ("Variceal bleeding, step by step", "A cirrhotic who bleeds is treated as variceal: protect the airway, transfuse sparingly, start a vasoactive drug and ceftriaxone, band within 12 hours, bridge with tamponade, rescue with TIPS, and prevent the next bleed with a beta-blocker plus banding."),
  ("Ascites, sodium and the pleura", "A SAAG of 1.1 g/dL or more says the fluid is from portal hypertension; the kidney then holds sodium and more water, so treatment is sodium restriction, spironolactone-led diuretics, paracentesis with albumin and TIPS, and the same fluid in the right chest is drained by needle, not by tube."),
  ("The true/false sweep", "The common errors are reversed formulas, a Child-Pugh minimum of 0, the wrong balloon first, beta-blockers in the acute bleed and chest drains for hydrothorax."),
]

PRIMER = "Portal hypertension is a rise in pressure in the portal vein, which drains the gut and spleen into the liver. Pressure in any vessel equals flow times resistance, so it can rise because the liver resists flow (cirrhosis) or because more blood arrives (splanchnic vasodilatation), and in cirrhosis both happen. Once the portal–caval gradient passes about 10 mmHg, collaterals open (varices), fluid leaks from the sinusoids (ascites) and the circulation becomes hyperdynamic with a low effective arterial volume, which drives the kidneys to retain salt and water. This deck covers the circulation, how cirrhosis is staged and scored, variceal bleeding and ascites; GI07B covers the other complications."

L = {}

L['CLD-01'] = dict(
  sub="Cirrhosis I → Portal circulation → Anatomy, flow and pressure",
  step=1,
  intro="Step 1 starts with the vessel itself. The portal vein carries venous blood from the whole gut and spleen into a low-resistance sinusoidal bed, which is why its pressure is normally only a few mmHg above the cava. No real question has been linked; the anatomy matters because it explains where collaterals form.",
  parts=[
    ('a', "**Splenic vein + superior mesenteric vein.** They join behind the neck of the pancreas. Because the splenic vein runs along the back of the pancreas, pancreatitis or a pancreatic tumour can thrombose it and cause ‘left-sided’ portal hypertension."),
    ('b', "**Into the splenic vein (as do the short gastric veins).** The inferior mesenteric vein most often joins the splenic vein, sometimes the superior mesenteric vein or their confluence. The short gastric veins draining into the splenic vein is why splenic vein thrombosis produces isolated gastric fundal varices with a normal liver; splenectomy treats them."),
    ('c', "**About 1 L/min at 5–7 mmHg.** Total hepatic blood flow is about 1.5 L/min, three-quarters portal. The pressure is low because the sinusoids offer little resistance; a gradient above 5 mmHg across the liver is already abnormal (CLD-03)."),
    ('d', "**Small and large bowel, spleen, pancreas.** It also drains the stomach and gallbladder. Everything absorbed from the gut, including ammonia and bacterial products, passes the liver first, which is why portosystemic shunting causes encephalopathy (CLD-05)."),
    ('e', "**Sinusoids, hepatic veins, inferior vena cava.** Block at any level raises portal pressure: before the sinusoid (portal vein thrombosis), at it (cirrhosis), or after it (Budd–Chiari, right heart failure)."),
  ],
  mimic=[
    ("Splenic vein thrombosis vs cirrhotic portal hypertension", "The first gives isolated gastric varices with normal liver tests and a normal HVPG; the second gives oesophageal varices, ascites and a raised HVPG."),
  ],
  traps=[
    ("“The portal vein supplies 70% of the liver’s oxygen”", "It supplies about 75% of the flow but only about half the oxygen, because portal blood is already partly desaturated."),
  ],
  decode=[
    ("Isolated gastric varices after pancreatitis, normal liver — cause? [pattern]", "Splenic vein thrombosis (short gastric veins drain into the splenic vein)."),
  ],
  punch="The portal vein is the splenic plus the superior mesenteric vein, carrying about 1 L/min at a few mmHg; it gives three-quarters of the flow but only half the oxygen.",
)

L['CLD-02'] = dict(
  sub="Cirrhosis I → Portal circulation → Hepatic arterial buffer response",
  step=1,
  intro="Step 1 continues with how the liver protects its blood supply. Two inflows must add up to a stable total, and the artery is the one that adjusts. No real question has been linked; it explains why the liver tolerates a fall in portal flow better than a fall in arterial flow.",
  parts=[
    ('a', "**A fall in portal flow dilates the hepatic artery, raising arterial flow (reciprocal).** It can make up a large part, though not all, of the lost flow."),
    ('b', "**Adenosine: less portal flow washes out less adenosine, which accumulates and dilates the artery.** Adenosine is produced at a constant rate in the space of Mall around the arterioles and portal venules. Portal flow carries it away; when portal flow falls, it builds up and relaxes arteriolar smooth muscle. No nerve or systemic hormone is needed, so the response works in a transplanted, denervated liver."),
    ('c', "**Keeps hepatic oxygen delivery constant.** This matters after TIPS or with portal vein thrombosis, when portal inflow drops and arterial flow takes over."),
    ('d', "**In sepsis.** Endotoxaemia blunts the response, so in septic shock a fall in portal flow from splanchnic vasoconstriction is not compensated and the liver becomes ischaemic, one route to hypoxic hepatitis."),
  ],
  mimic=[
    ("Buffer response vs autoregulation", "The buffer response is the artery responding to portal flow; the portal vein has no autoregulation and cannot respond to a fall in arterial flow."),
  ],
  traps=[
    ("“The portal vein dilates when the hepatic artery is occluded”", "The response is one-way. This is why hepatic artery thrombosis after transplant is so damaging: the bile ducts depend on the artery alone."),
  ],
  decode=[
    ("Mediator of the hepatic arterial buffer response? [pattern]", "Adenosine washout."),
    ("Condition in which the buffer response is lost? [pattern]", "Sepsis or endotoxaemia."),
  ],
  punch="When portal flow falls, adenosine is no longer washed out and dilates the hepatic artery; it works one way only and fails in sepsis.",
)

L['CLD-03'] = dict(
  sub="Cirrhosis I → Portal circulation → Hepatic venous pressure gradient",
  step=1,
  intro="Step 1 ends with how portal pressure is measured. The portal vein cannot be cannulated safely, so the pressure in the sinusoids is measured from the hepatic vein side. No real question has been linked, but the formula and thresholds come up in the true/false card (CLD-16) and throughout Baveno VII.",
  parts=[
    ('a', "**Wedged minus free hepatic venous pressure.** Subtracting the free (caval) pressure removes the effect of intra-abdominal and right atrial pressure, leaving only the gradient across the liver."),
    ('b', "**Balloon inflated in the right hepatic vein: a static column to the sinusoid = sinusoidal pressure.** With flow stopped, the pressure equalises back through the sinusoids, which in cirrhosis are connected to the portal vein, so the wedged pressure equals portal pressure."),
    ('c', "**Balloon deflated: caval pressure.** With blood flowing freely past the catheter tip, it reads the hepatic vein and inferior vena cava, which carry right atrial and intra-abdominal pressure; that is the part subtracted."),
    ('d', "**Pre-sinusoidal portal hypertension (it under-estimates portal pressure).** In portal vein thrombosis, schistosomiasis or non-cirrhotic portal fibrosis the block is upstream of the sinusoid; the wedged pressure reads the normal sinusoid, so HVPG is normal although the patient has varices."),
    ('e', "**Normal 1–5; clinically significant 10 or more; variceal bleeding 12 or more; poor outcome in bleeding 20 or more mmHg (standard teaching, not in your notes).** Baveno VII defines clinically significant portal hypertension as HVPG 10 or more: varices, ascites and decompensation become possible above it. Above 12, varices can bleed. Above 20 at the time of a bleed predicts failure to control bleeding and early death, which is one criterion for pre-emptive TIPS (CLD-10). On beta-blockers, a fall of 20% or more, or to 12 or less, protects against bleeding."),
  ],
  mimic=[
    ("Pre-sinusoidal vs post-hepatic (cardiac) portal hypertension", "Pre-sinusoidal: wedged pressure normal, HVPG normal. Right heart failure: wedged and free pressures both high, so the gradient is also near normal. Only sinusoidal disease (cirrhosis) gives a high wedged pressure with a normal free pressure."),
  ],
  traps=[
    ("“HVPG is free minus wedged”", "Wedged minus free; free minus wedged would be negative."),
    ("“HVPG under-reads in post-sinusoidal disease”", "It under-reads in pre-sinusoidal disease (CLD-16 b): the wedged catheter sees only the sinusoid, so a block upstream of it (portal vein, portal venules) is invisible. In post-sinusoidal (cardiac) disease both pressures rise together."),
  ],
  decode=[
    ("HVPG threshold for clinically significant portal hypertension / for variceal bleeding? [pattern]", "10 mmHg / 12 mmHg."),
    ("Varices with a normal HVPG — level of the block? [pattern]", "Pre-sinusoidal (portal vein thrombosis, schistosomiasis, non-cirrhotic portal fibrosis)."),
  ],
  punch="HVPG is wedged minus free hepatic venous pressure, a measure of sinusoidal pressure: 10 mmHg means clinically significant portal hypertension, 12 bleeding risk and 20 poor outcome, and it reads normal when the block is pre-sinusoidal.",
)

L['CLD-04'] = dict(
  sub="Cirrhosis I → Portal circulation → Why portal pressure rises",
  step=2,
  intro="Step 2 explains the rise in pressure. Pressure equals resistance times flow, and cirrhosis raises both, resistance first. The one real question (Marrow) asks the mechanism in alcoholic hepatitis and keys increased splanchnic flow, because it was the only true option offered.",
  parts=[
    ('a', "**Raised resistance (intrahepatic) — structural: fibrosis, regenerative nodules, vascular occlusion.** This is the starting point and the larger, fixed part of the resistance. Fibrous septa and nodules compress and distort the sinusoids and hepatic venules. In alcoholic hepatitis swollen hepatocytes and perivenular fibrosis add to it."),
    ('b', "**Dynamic: sinusoidal contraction (more vasoconstrictors, less nitric oxide).** A smaller part, often quoted as about a quarter, of intrahepatic resistance is reversible tone. The sick sinusoidal endothelium makes less nitric oxide and more endothelin and thromboxane, so the sinusoids are contracted. Because resistance varies with the fourth power of radius, a small narrowing raises it steeply. Carvedilol (alpha-1 blockade) and nitrates act here."),
    ('c', "**Cells: capillarised endothelium, activated stellate cells.** Sinusoidal endothelium loses its fenestrae and gains a basement membrane, and activated stellate cells become contractile myofibroblasts that wrap the sinusoid and lay down collagen. Capillarisation also stops protein leaking from the sinusoid, which is why cirrhotic ascites is low in protein (CLD-13)."),
    ('d', "**Raised flow (splanchnic) — splanchnic arteriolar vasodilatation, angiogenesis and collaterals, hyperdynamic circulation.** The splanchnic arterioles make more nitric oxide (shear stress, bacterial products from the gut), glucagon is high and VEGF drives new vessels. More blood enters the portal system, which keeps the pressure high even after collaterals open. Beta-blockers act on this side: beta-1 blockade lowers cardiac output and beta-2 blockade leaves alpha-mediated splanchnic vasoconstriction unopposed. Terlipressin, somatostatin and octreotide also reduce inflow (CLD-12)."),
  ],
  mimic=[
    ("Raised resistance vs raised flow", "Resistance starts portal hypertension and is the target of carvedilol, nitrates and TIPS; flow sustains it and is the target of beta-blockers and splanchnic vasoconstrictors."),
  ],
  traps=[
    ("“Increased splanchnic flow is the primary cause of portal hypertension”", "Raised intrahepatic resistance is primary; flow rises later and maintains it. Pick flow only if, as in the Marrow question, it is the only true option."),
    ("“Collaterals decompress portal hypertension”", "They divert blood but the high splanchnic inflow keeps the pressure up."),
  ],
  decode=[
    ("Alcoholic hepatitis, SAAG 1.3 — mechanism of the ascites from the options given [Marrow]", "Increased splanchnic blood flow (the only true option; resistance is primary)."),
    ("Where do beta-blockers act / where does carvedilol add? [pattern]", "On flow (cardiac output, splanchnic vasoconstriction); carvedilol also lowers intrahepatic resistance."),
  ],
  punch="Portal pressure rises because the cirrhotic liver resists flow (fixed fibrosis plus contracted sinusoids short of nitric oxide) and then stays high because the splanchnic bed dilates and sends more blood in.",
)

L['CLD-05'] = dict(
  sub="Cirrhosis I → Portal circulation → Complications and mechanisms",
  step=2,
  intro="Step 2 continues with what the pressure does. Every complication comes from one of three things: blood diverted through collaterals, a high pressure in the sinusoids, or the vasodilated, hyperdynamic circulation. Three real questions test this: the haemodynamics of hepatorenal syndrome, recognising decompensated cirrhosis, and telling GAVE from portal hypertensive gastropathy.",
  parts=[
    ('a', "**Varices, portal gastropathy — portosystemic collaterals.** Collaterals open at the gastro-oesophageal junction, rectum, umbilicus and retroperitoneum once HVPG passes 10 mmHg. Portal hypertensive gastropathy is congestion of the gastric mucosa: a mosaic ‘snakeskin’ pattern in the fundus and body that responds to beta-blockers and TIPS. GAVE (‘watermelon stomach’, red stripes radiating from the pylorus in the antrum) also occurs in cirrhosis but is not caused by portal pressure, so it does not respond to beta-blockers or TIPS; it is treated with argon plasma coagulation or band ligation."),
    ('b', "**Ascites, splenomegaly — raised sinusoidal and portal pressure.** Sinusoidal pressure forces fluid into the space of Disse and lymph; when lymph flow is overwhelmed, it weeps into the peritoneum. Splenic congestion causes hypersplenism and the low platelet count."),
    ('c', "**Hepatorenal syndrome — splanchnic vasodilatation, low effective volume, renal vasoconstriction.** The splanchnic bed holds much of the blood volume, the arterial pressure falls, and renin–angiotensin, the sympathetic system and ADH are switched on. The kidney is structurally normal but intensely vasoconstricted, which is why treatment is a vasoconstrictor (terlipressin) plus albumin, not more fluid alone."),
    ('d', "**Cirrhotic cardiomyopathy — hyperdynamic circulation; diastolic dysfunction, long QT.** The resting cardiac output is high, which hides a blunted response to stress. The failure is unmasked by TIPS, sepsis or transplant. 2020 Cirrhotic Cardiomyopathy Consortium criteria: systolic dysfunction is LVEF 50% or less or absolute global longitudinal strain under 18%; advanced diastolic dysfunction is three or more of septal e′ under 7 cm/s, E/e′ 15 or more, left atrial volume index over 34 mL/m² and tricuspid regurgitation velocity over 2.8 m/s. The long QT on the card is a real feature (and a reason to check the QT before terlipressin or erythromycin), but the 2020 criteria list ECG changes only as a research area, not a diagnostic criterion."),
    ('e', "**Hepatopulmonary syndrome — intrapulmonary vasodilatation.** Dilated pulmonary capillaries let blood pass too fast for oxygen to diffuse to the centre of the stream. Hypoxaemia is worse upright (platypnoea, orthodeoxia), because the dilated vessels are at the lung bases. Defined by PaO₂ under 80 mmHg or an A–a gradient of 15 or more (20 or more over 64) with bubbles in the left heart three or more beats after they appear in the right on contrast echo. Transplant reverses it."),
    ('f', "**Portopulmonary hypertension — pulmonary vasoconstriction.** The opposite lesion to e: vasoactive mediators that the liver should have cleared reach the lung and cause vasoconstriction and remodelling. It is pre-capillary pulmonary hypertension in a patient with portal hypertension: current ESC/ERS 2022 haemodynamics are mean PAP over 20 mmHg, PVR over 2 Wood units and wedge 15 or less (older definitions, including ILTS 2016, used mean PAP 25 or more and PVR 3 Wood units or more). Severity decides transplant: in Krowka’s series no patient with mean PAP 25–35 died after transplant, half with 35–50 died and all above 50 died, so a mean PAP of 35 or more that does not fall with treatment makes transplant high risk, and about 45–50 or more rules it out."),
    ('g', "**Encephalopathy — shunting; astrocyte swelling.** Ammonia from the gut bypasses the liver; astrocytes turn it into glutamine, which is osmotically active, and they swell."),
  ],
  mimic=[
    ("GAVE vs portal hypertensive gastropathy", "GAVE: red stripes in the antrum, not portal-pressure related, treated by argon plasma coagulation or banding. Gastropathy: mosaic pattern in the fundus and body, treated by lowering portal pressure."),
    ("Hepatopulmonary syndrome vs portopulmonary hypertension", "HPS: dilated pulmonary vessels, hypoxaemia, positive bubble study, cured by transplant. POPH: constricted vessels, raised PVR, may make transplant unsafe."),
  ],
  traps=[
    ("“GAVE is a form of portal hypertensive gastropathy, so give a beta-blocker”", "GAVE is a separate vascular lesion; lowering portal pressure does nothing. 20% chose another option on DocT, mostly gastropathy."),
    ("“Hepatorenal syndrome is renal hypoperfusion from dehydration”", "The kidney is vasoconstricted in a patient whose total body water is high; the problem is arterial underfilling from splanchnic vasodilatation."),
  ],
  decode=[
    ("Central haemodynamic change in hepatorenal syndrome? [DocT]", "Splanchnic arterial vasodilatation with renal vasoconstriction (100% right)."),
    ("Cirrhotic with chronic anaemia, stripes in the antrum — diagnosis? [DocT]", "GAVE (80% right); treat with argon plasma coagulation."),
    ("Alcohol use, ascites, jaundice, confusion, long PT, low albumin — cause? [DocT]", "Decompensated cirrhosis (84% right); low albumin and ascites mark chronic synthetic failure, not acute hepatitis."),
  ],
  punch="Collaterals give varices and encephalopathy, high sinusoidal pressure gives ascites, and the vasodilated circulation gives hepatorenal syndrome and cardiomyopathy; GAVE is the antral lesion that portal-pressure drugs do not touch.",
)

L['CLD-06'] = dict(
  sub="Cirrhosis I → Staging and scores → The four clinical stages",
  step=3,
  intro="Step 3 turns to how far along the patient is. The D’Amico stages divide cirrhosis by the events that mark it, and the jump in mortality from stage 2 to stage 3 is the first episode of decompensation. One real question asks you to recognise decompensated cirrhosis from ascites, jaundice and confusion.",
  parts=[
    ('a', "**Stage 1: no varices, no ascites, 1-year death 1%. Stage 2: varices, no ascites, no bleeding, 3%.** Both are compensated. Patients die mostly of other causes; the risk is progression to stage 3 or 4."),
    ('b', "**Stage 3: ascites ± varices, no bleeding, 20%. Stage 4: bleeding ± ascites, 57%.** Decompensation is ascites, variceal bleeding, encephalopathy or jaundice. Ascites is the commonest first decompensating event (about half of compensated patients within 10 years), and cirrhosis causes about 80–85% of all ascites. Once ascites appears, about 15–20% die within a year and about 44% within 5 years."),
    ('c', "**Stages 1–2 are compensated (survival 12–15 years if controlled); stages 3–4 decompensated (2–5 years).** The prognosis changes at decompensation, not at the diagnosis of cirrhosis, which is why Baveno VII aims beta-blockers at preventing decompensation in compensated patients with clinically significant portal hypertension. Removing the cause (abstinence, viral cure) can bring a decompensated patient back to a stable state (‘recompensation’)."),
  ],
  mimic=[
    ("Decompensated cirrhosis vs acute hepatitis", "Ascites and low albumin take weeks to develop; acute hepatitis has very high transaminases and usually no ascites."),
  ],
  traps=[
    ("“Varices alone make cirrhosis decompensated”", "Varices that have not bled are stage 2, still compensated; it is bleeding, ascites, encephalopathy or jaundice that decompensate."),
  ],
  decode=[
    ("Alcohol use with ascites, jaundice, confusion, long PT and low albumin — most likely cause? [DocT]", "Cirrhosis (decompensated; 84% right)."),
    ("Commonest first decompensating event, and its 1-year mortality? [DocT GT]", "Ascites; about 15–20%."),
  ],
  punch="Mortality is 1% and 3% a year while cirrhosis is compensated and jumps to 20% with ascites and 57% with bleeding; decompensation, usually ascites first, is the turning point.",
)

L['CLD-07'] = dict(
  sub="Cirrhosis I → Staging and scores → Child-Turcotte-Pugh score",
  step=3,
  intro="Step 3 continues with the bedside score. Child-Pugh adds three laboratory values to two clinical signs and grades hepatic reserve. Five real questions test it: two calculations, what it predicts, the best single marker of severity, and which test appears in both Child-Pugh and MELD.",
  parts=[
    ('a', "**Encephalopathy: none 1, grade 1–2 2, grade 3–4 3.** Grade 1 (West Haven) is subtle: altered sleep, short attention, mild confusion; a stem’s ‘sleep disturbance’ means grade 1, so 2 points. Grade 3 is somnolent but rousable; grade 4 coma."),
    ('b', "**Ascites: none 1, mild–moderate (diuretic-responsive) 2, severe (refractory) 3.** Ascites and encephalopathy are judged, not measured, which is one reason MELD was developed."),
    ('c', "**Bilirubin under 2 = 1, 2–3 = 2, over 3 mg/dL = 3.** In cholestatic disease (PBC, PSC) the bands are higher (1–4, 4–10, over 10), because bilirubin rises early without matching loss of function."),
    ('d', "**Albumin over 3.5 = 1, 2.8–3.5 = 2, under 2.8 g/dL = 3.** Albumin has a half-life of about three weeks, so it reflects chronic synthetic function, not today’s."),
    ('e', "**INR under 1.7 = 1, 1.7–2.3 = 2, over 2.3 = 3. Class A: 5–6. Class B: 7–9. Class C: 10–15.** Older versions score prolongation of PT over control: 1–3 s, 4–6 s, over 6 s. INR is the best single marker of severity in chronic liver disease because factor VII has a half-life of about 6 hours and falls first; it is in both Child-Pugh and MELD. Transaminases measure ongoing injury, not reserve, and may be normal in end-stage cirrhosis. The score predicts overall survival, variceal bleeding and operative risk: 1-year survival about 100% (A), 80% (B) and 45% (C), and abdominal operative mortality about 10%, 30% and 80%."),
  ],
  table=dict(title="The two linked calculations",
    head=["Item", "DocT GT (CGT2)", "Marrow"],
    rows=[["Bilirubin", "3.5 → 3", "4 → 3"],
          ["Albumin", "2.8 → 2", "3.2 → 2"],
          ["INR / PT", "INR 2.1 → 2", "PT +5 s → 2"],
          ["Ascites", "Moderate → 2", "Mild → 2"],
          ["Encephalopathy", "Grade II → 2", "Sleep disturbance (grade 1) → 2"],
          ["Total", "11 → Class C", "11 → Class C"]]),
  mimic=[
    ("Child-Pugh vs MELD", "Child-Pugh: bilirubin, albumin, INR, ascites, encephalopathy, minimum 5, no creatinine. MELD: bilirubin, INR, creatinine (± sodium, albumin), all laboratory values, no ceiling."),
  ],
  traps=[
    ("“The lowest Child-Pugh score is 0”", "Each of five items scores at least 1, so the minimum is 5 (CLD-16 c)."),
    ("“Creatinine is part of Child-Pugh”", "It is in MELD only; renal failure is a major predictor of death that Child-Pugh misses."),
    ("“SGOT/SGPT or bilirubin is the best marker of severity”", "Transaminases measure injury, not function; bilirubin is prognostic, but PT/INR is the best single synthetic marker."),
    ("“Albumin 2.8 scores 3”", "On this card 2.8–3.5 scores 2; under 2.8 scores 3. Read the band edge carefully."),
  ],
  decode=[
    ("Bilirubin 3.5, albumin 2.8, INR 2.1, moderate ascites, grade II HE — class? [DocT GT, CGT2]", "11 points, Class C."),
    ("Bilirubin 4, albumin 3.2, PT +5 s, mild ascites, sleep disturbance — class? [Marrow]", "11 points, Class C."),
    ("Best marker of severity in chronic liver disease? / marker in both Child-Pugh and MELD? [DocT GT PYQ, NEET 2024]", "PT/INR."),
    ("True statement about Child-Pugh? [Marrow]", "It predicts overall mortality (and bleeding and operative risk)."),
  ],
  punch="Child-Pugh scores bilirubin, albumin, INR, ascites and encephalopathy from 1 to 3 each, so it runs from 5 to 15 (A 5–6, B 7–9, C 10–15); INR, in both Child-Pugh and MELD, is the best single marker of severity.",
)

L['CLD-08'] = dict(
  sub="Cirrhosis I → Staging and scores → MELD",
  step=3,
  intro="Step 3 ends with the score built from laboratory values alone. MELD predicts 3-month survival and decides who gets a liver first. Two real questions: which variable tracks hepatorenal syndrome, and what a MELD of 25 means.",
  parts=[
    ('a', "**Bilirubin, INR, creatinine.** Excretory function, synthetic function and the kidney, which reflects the circulatory failure of advanced cirrhosis. Creatinine is the MELD variable that follows hepatorenal syndrome, because HRS is defined by a rise in creatinine."),
    ('b', "**3.78 × ln(bilirubin) + 11.2 × ln(INR) + 9.57 × ln(creatinine) + 6.43.** Values under 1 are set to 1 so the logarithm is not negative, and creatinine is capped at 4 mg/dL. INR has the largest coefficient."),
    ('c', "**3-month survival: the higher the score, the lower the survival.** Approximate 3-month mortality: 9 or less about 2%, 10–19 about 6%, 20–29 about 20%, 30–39 about 53%, 40 or more about 71%. Transplant gives more benefit than risk from about MELD 15, which is when patients should be referred; so MELD 25 is high risk and transplant should be considered."),
    ('d', "**Adds sodium; used for organ allocation.** Hyponatraemia reflects the severity of the circulatory disturbance and adds risk independent of MELD, especially at low scores. MELD-Na was used for US allocation from 2016; since 13 July 2023 the US uses MELD 3.0 (Kim, Gastroenterology 2021), which adds female sex (1.33 points) and albumin (bounded 1.5–3.5 g/dL), adds sodium–bilirubin and albumin–creatinine interaction terms, keeps sodium bounded at 125–137 mmol/L and lowers the creatinine cap from 4.0 to 3.0 mg/dL. Its 90-day C-statistic was only slightly better than MELD-Na (0.869 vs 0.862), but it re-ranked women and patients with low albumin upward."),
    ('e', "**Adds sodium and albumin.** The five-variable MELD (Myers and colleagues, Canada) slightly improved prediction, because low albumin adds prognostic information that bilirubin, INR and creatinine miss; MELD 3.0 follows the same idea and adds sex, because women have a lower creatinine for the same kidney function."),
    ('f', "**Creatinine is unreliable in the critically ill; in dialysed patients use the pre-dialysis creatinine.** Creatinine is low in sarcopenic patients and in women, and bilirubin interferes with some assays, so MELD under-estimates their risk. The allocation rule is different from the card: if the patient has had dialysis twice in the past week (or 24 hours of CRRT), creatinine is set to 4.0 mg/dL (3.0 in MELD 3.0), not taken from a pre-dialysis sample."),
  ],
  mimic=[
    ("MELD vs Child-Pugh", "MELD is objective, continuous and includes the kidney; Child-Pugh includes the subjective signs and albumin but no creatinine and has a ceiling at 15."),
  ],
  traps=[
    ("“Sodium is the MELD variable most linked to HRS”", "Low sodium accompanies HRS, but creatinine defines it and tracks its onset. 25% chose another variable on DocT."),
    ("“MELD 25 is moderate risk, transplant not needed”", "About 20% 3-month mortality; transplant benefit begins near MELD 15."),
    ("“A dialysed patient’s MELD uses the pre-dialysis creatinine”", "For allocation creatinine is set to 4.0 (3.0 in MELD 3.0) after two dialysis sessions in a week."),
  ],
  decode=[
    ("Which MELD parameter most closely correlates with the onset of HRS? [DocT]", "Creatinine (75% right)."),
    ("MELD 25 — prognosis? [DocT]", "High risk; consider liver transplantation (80% right)."),
  ],
  punch="MELD combines bilirubin, INR and creatinine (INR weighted most) to predict 3-month mortality, about 20% at 20–29; refer for transplant from about 15, and creatinine is the variable that tracks HRS.",
)

L['CLD-09'] = dict(
  sub="Cirrhosis I → GI bleeding → Source: cirrhotic vs non-cirrhotic",
  step=4,
  intro="Step 4 opens with the bleeding patient. In a cirrhotic, the source changes the first hour of treatment, and since about half of bleeds are variceal, every cirrhotic who bleeds is managed as variceal until the endoscopy says otherwise. The one real question (60% right) hid varices behind NSAID use and a history of GAVE.",
  parts=[
    ('a', "**Oesophageal varices: cirrhosis 50%, no cirrhosis 0%.** The card’s figures come from one series; most guidance quotes a higher share of variceal bleeding in cirrhosis, up to about 70%. Either way it is the commonest source and the most lethal."),
    ('b', "**Gastric ulcer: 24.2% vs 54.2%.** Even in cirrhosis about a quarter of bleeds are ulcers, which is why the PPI infusion runs until the source is known (CLD-10 f)."),
    ('c', "**Duodenal ulcer: 7.6% vs 12.7%.** Peptic ulcer is still the second source in cirrhosis; portal hypertensive gastropathy and impaired mucosal defence add to the risk, and an ulcer can coexist with varices, so the endoscopist looks for both."),
    ('d', "**Gastric varices: 4.5% vs 0%.** Less common but bleed more heavily; fundal varices are treated with cyanoacrylate glue rather than bands."),
    ('e', "**Mallory–Weiss: 0% vs 12.7%.** A mucosal tear at the gastro-oesophageal junction from retching, classically after binge drinking; it usually stops on its own. The 0% in cirrhosis reflects this one series, not immunity."),
    ('f', "**Cancer: 0% vs 10.8%.** Rule out haemoptysis, haemobilia (after ERCP, liver biopsy or TIPS) and nasal bleeding before calling it upper GI."),
  ],
  mimic=[
    ("Variceal vs ulcer bleeding in a cirrhotic", "You cannot tell at the bedside; vasoactive drug, ceftriaxone and a PPI are started together, and the PPI is stopped once varices are confirmed."),
  ],
  traps=[
    ("“NSAID use and known GAVE make this a gastric ulcer or GAVE bleed”", "In a cirrhotic with portal hypertension and massive haematemesis, varices come first; GAVE causes slow chronic loss, not torrential haematemesis. 40% were misled on DocT."),
  ],
  decode=[
    ("Alcoholic cirrhosis with ascites, sudden massive haematemesis, shock, NSAIDs and mild GAVE — likely source? [DocT]", "Oesophageal varices (60% right)."),
  ],
  punch="In cirrhosis about half of upper GI bleeds, or more, are variceal and a quarter are ulcers, so treat every cirrhotic bleed as variceal until the endoscope says otherwise.",
)

L['CLD-10'] = dict(
  sub="Cirrhosis I → GI bleeding → Acute variceal bleeding: management",
  step=4,
  intro="Step 4 is the heart of the deck and its most asked card (15 real questions). The bleed is driven by portal pressure, so everything either protects the patient while you lower that pressure (airway, sparing transfusion, vasoactive drug, antibiotics) or closes the bleeding vessel (bands, tamponade, TIPS). The questions test the order of steps, the transfusion target, airway protection and what to do when banding fails.",
  parts=[
    ('a', "**Airway, two wide cannulas, blood products; correct fibrinogen by TEG; nasogastric tube to decompress and localise.** Two large-bore cannulas come first in a shocked bleeder, before endoscopy, a nasogastric tube or a PPI. Intubate before endoscopy when consciousness is reduced (encephalopathy), haematemesis is massive or the airway is unprotected (Baveno VII): aspiration of blood is a leading cause of death, NIV is contraindicated (vomiting, low GCS) and nasal oxygen protects nothing. Transfuse restrictively: start at haemoglobin 7 g/dL and aim for 7–8 (Baveno VII). Villanueva (NEJM 2013, all upper GI bleeders, cirrhotics included) compared a threshold of 7 g/dL with 9 g/dL: the restrictive arm had better 6-week survival (95% vs 91%, HR 0.55) and less rebleeding (10% vs 16%). In the cirrhotic subgroup the survival gain was in Child A and B, not Child C, and the HVPG rose in the first 5 days only in the liberal arm, which is the mechanism: over-transfusion raises portal pressure and restarts the bleed. Fresh frozen plasma is not recommended: the INR does not measure bleeding risk in cirrhosis (both pro- and anticoagulant proteins fall) and the volume raises portal pressure. Baveno VII found no evidence that platelet count or fibrinogen predict failure and makes no recommendation on correcting them, so ‘correct fibrinogen by TEG’ is local practice, not guideline. Baveno VII advises caution with nasogastric tubes (airway manipulation) and recommends erythromycin 250 mg IV 30–120 minutes before endoscopy (if no long QT) to empty the stomach of blood."),
    ('b', "**Terlipressin (or somatostatin, octreotide), started before endoscopy.** Start as soon as variceal bleeding is suspected and continue for 2–5 days. These drugs constrict the splanchnic arterioles, cutting portal inflow and pressure (CLD-12). Terlipressin 2 mg 4-hourly, reduced to 1 mg once bleeding is controlled; octreotide 50 µg bolus then 50 µg/h. The vasoactive drug is the right ‘next step after resuscitation’ and the best first drug once varices are seen, not a PPI or a beta-blocker."),
    ('c', "**IV ceftriaxone.** 1 g every 24 hours for up to 7 days. About a fifth of cirrhotic bleeders are infected on admission or soon after; infection worsens portal pressure and haemostasis, and prophylaxis reduces infection, rebleeding and death. It is part of the pre-endoscopy bundle with the vasoactive drug."),
    ('d', "**Endoscopic band ligation; sclerotherapy, clips or thrombin as alternatives.** Endoscopy within 12 hours, once resuscitated. Band ligation is first line because it controls bleeding as well as sclerotherapy with fewer ulcers, strictures and perforations. Gastric fundal varices are injected with cyanoacrylate glue. Argon plasma coagulation is for GAVE, not varices."),
    ('e', "**Balloon tamponade, then TIPS; CT angiography and embolisation if the source is unclear.** When drugs and banding fail, a Sengstaken–Blakemore tube (CLD-11, no more than about 24 hours) or a self-expanding oesophageal metal stent (which can stay longer) bridges to definitive treatment; Baveno VII finds the stent as effective as tamponade and safer. Salvage covered TIPS then lowers the portal pressure directly. Pre-emptive covered TIPS within 72 hours (ideally 24) is offered to high-risk patients who stopped bleeding: Child C under 14 points, or Child B over 7 with active bleeding at endoscopy, or HVPG over 20; it reduces rebleeding and death."),
    ('f', "**A pantoprazole infusion only while the source is unknown.** Acid does not cause variceal bleeding, so the PPI is stopped once varices are confirmed (a short course after banding can shrink the banding ulcer). In non-variceal bleeding, high-dose PPI keeps gastric pH above 6, where pepsin is inactive and the clot is stable, which H2 blockers cannot do. Given before endoscopy (80 mg bolus ± 8 mg/h), it downstages ulcers (Lau, NEJM 2007) but does not reduce rebleeding, surgery or death, so it must never delay the endoscope. There is no ‘REDUCE’ PPI trial: REDUCE is a COPD steroid trial."),
  ],
  table=dict(title="The first 12 hours",
    head=["Order", "Step", "Why"],
    rows=[["1", "Large-bore access; intubate if GCS low or massive haematemesis", "Shock and aspiration kill first"],
          ["2", "Vasoactive drug + IV ceftriaxone", "Lower portal pressure; prevent infection-driven rebleeding"],
          ["3", "Red cells to Hb 7–8 g/dL; no FFP", "Over-transfusion raises portal pressure"],
          ["4", "Endoscopy within 12 h: band ligation", "Closes the varix"],
          ["5", "Fails: tamponade or stent, then salvage TIPS", "Bridge, then decompress"],
          ["6", "High risk: pre-emptive TIPS within 72 h", "Prevents early rebleeding and death"]]),
  mimic=[
    ("Variceal vs non-variceal bleeding", "Variceal: vasoactive drug, ceftriaxone, banding; PPI only until the source is known. Non-variceal: high-dose PPI, endoscopic haemostasis; no vasoactive drug."),
  ],
  traps=[
    ("“After resuscitation, go straight to endoscopy (or give a PPI bolus)”", "The vasoactive drug comes first and endoscopy follows within 12 hours. Only 59% picked octreotide on DocT."),
    ("“Marrow: emergent endoscopy is the next step in a cirrhotic in shock”", "Marrow keys endoscopy, but vasoactive drug and IV ceftriaxone are both guideline steps before it, and Marrow’s own explanation stresses antibiotics. Exam day: if the drug is already running and ceftriaxone is offered, pick it; if both are given, pick endoscopy."),
    ("“Transfuse to haemoglobin above 9–10”", "Over-transfusion raises portal pressure and rebleeding; threshold 7, target 7–8."),
    ("“Sclerotherapy or APC is the endoscopic treatment of choice”", "Band ligation; 39% missed it on the image question. APC is for GAVE."),
    ("“NIV or nasal oxygen for the confused bleeder”", "Intubate before endoscopy; NIV is contraindicated."),
    ("“Tranexamic acid helps variceal bleeding”", "Not recommended: HALT-IT showed no fewer bleeding deaths (4% vs 4%) and more venous thrombosis (0.8% vs 0.4%)."),
    ("“The pre-endoscopy PPI strategy comes from the REDUCE trial”", "The evidence is Lau 2007; REDUCE is a COPD steroid trial. The answer (80 mg bolus + 8 mg/h) is still right."),
  ],
  decode=[
    ("Child C, haematemesis, shock — after initial resuscitation, next step? [DocT]", "IV octreotide (vasoactive drug) (59% right); antibiotics alongside."),
    ("Varices seen at endoscopy — best initial pharmacological therapy? [DocT]", "Octreotide infusion (84% right)."),
    ("Haemoglobin 7.5, stable — transfusion strategy? / why avoid over-transfusion? [DocT, DocT GT GT6, AIM1, AIM2]", "Restrictive (transfuse below 7, 91–94% right); it raises portal pressure and rebleeding (95–100% right)."),
    ("Variceal bleed with confusion — airway? / massive haematemesis, SBP 80 — first priority? [DocT GT GT8, AIM1, AIM2]", "Prophylactic intubation (94–95% right); large-bore IV access (94% right)."),
    ("First-line endoscopic therapy / procedure in the image? [DocT GT CGT2, DocT]", "Band ligation (61% right on the image)."),
    ("Bleeding uncontrolled by banding and drugs — next step? [DocT GT GT2, GT4]", "Sengstaken–Blakemore tube (100% right), as a bridge to TIPS."),
  ],
  extra=[
    dict(q="Melaena, endoscopy in 4 hours — PPI strategy? [DocT, 93% right]", a="IV 80 mg bolus + 8 mg/h. It downstages ulcers before the endoscopy (Lau 2007) without reducing death; ACG 2021 makes no recommendation for or against it."),
  ],
  punch="Secure the airway and access, transfuse to only 7–8 g/dL, start a vasoactive drug and ceftriaxone before the endoscope, band within 12 hours, bridge failure with tamponade or a stent to TIPS, and give pre-emptive TIPS to the high-risk patient.",
)

L['CLD-11'] = dict(
  sub="Cirrhosis I → GI bleeding → Sengstaken–Blakemore tube",
  step=4,
  intro="Step 4 continues with the bridge when banding and drugs fail. The tube compresses the varices mechanically while TIPS is arranged. Three real questions: two ask when to use it, and the NEET 2025 recall asks its most dangerous complication.",
  parts=[
    ('a', "**Two balloons (gastric, oesophageal) and one gastric aspiration port.** Three lumens in all."),
    ('b', "**Insert through the mouth; inflate the gastric balloon first; apply traction; inflate the oesophageal balloon only if still bleeding (your notes list it before traction).** Intubate first. Inflate the gastric balloon with a small volume (about 50 mL) and confirm on X-ray that it lies below the diaphragm before filling it fully (about 250–300 mL of air; the larger Minnesota balloon takes about 450–500 mL). Traction pulls it against the cardia, compressing the feeding vessels of the oesophageal varices, which alone often stops the bleeding. The oesophageal balloon (to about 30–45 mmHg) is added only if bleeding continues, because it can cause necrosis and rupture. If the gastric balloon is inflated in the oesophagus or trachea, or migrates upward with traction, it obstructs the airway: sudden distress, hypoxaemia and high airway pressures mean cut and deflate the balloons at once, so scissors stay at the bedside."),
    ('c', "**Linton–Nachlas: a single large gastric balloon.** With no oesophageal balloon, it relies on a large gastric balloon pulled up against the cardia and fundus, so it suits bleeding gastric fundal varices."),
    ('d', "**Minnesota: adds an oesophageal aspiration port (four lumens) (standard teaching, not in your notes).** It drains saliva above the oesophageal balloon and lowers aspiration risk."),
    ('e', "**A bridge for no more than 24 hours; intubate first (standard teaching, not in your notes).** It controls about 90% of refractory bleeds at first, but about half rebleed when it is deflated, so it is only a bridge to TIPS. Longer use causes pressure necrosis. Baveno VII considers a self-expanding oesophageal metal stent as effective and safer."),
  ],
  mimic=[
    ("Gastric balloon in the airway vs aspiration", "Balloon in the airway: abrupt hypoxaemia and high airway pressures right after inflation. Aspiration: develops over hours, with new infiltrates."),
  ],
  traps=[
    ("“Respiratory distress after inflation is oesophageal perforation or aspiration”", "Immediate distress with high airway pressures is the gastric balloon in the trachea: deflate and cut."),
    ("“Inflate the oesophageal balloon first”", "Gastric first; the oesophageal balloon first risks displacement, airway obstruction and rupture (CLD-16 f)."),
  ],
  decode=[
    ("Variceal bleeding uncontrolled by banding and drugs — next step? [DocT GT GT2, GT4]", "Sengstaken–Blakemore tube (100% right)."),
    ("Acute respiratory distress, hypoxaemia, high airway pressures just after balloon inflation — cause? [NEET 2025 recall]", "Gastric balloon placed in the trachea."),
  ],
  punch="Intubate, confirm the gastric balloon below the diaphragm, inflate it first and apply traction, add the oesophageal balloon only if bleeding continues, and use it for under 24 hours as a bridge to TIPS.",
)

L['CLD-12'] = dict(
  sub="Cirrhosis I → GI bleeding → Drugs in portal hypertensive bleeding",
  step=4,
  intro="Step 4 ends with the drugs. Each class either cuts portal inflow or lowers resistance, and the timing matters: vasoconstrictors in the acute bleed, beta-blockers for prevention. Four real questions test secondary prophylaxis (where the DocT key is wrong), primary prophylaxis, and antifibrinolytic mechanism.",
  parts=[
    ('a', "**Splanchnic vasoconstrictors — reduce portal venous inflow — vasopressin, terlipressin, somatostatin, vapreotide.** Vasopressin acts on V1 receptors but also constricts coronary and peripheral vessels, so it is now rarely used. Terlipressin is a longer-acting prodrug with fewer side effects. Somatostatin and its analogues block glucagon and other splanchnic vasodilators and reduce post-meal hyperaemia. Used for 2–5 days in the acute bleed (CLD-10)."),
    ('b', "**Non-selective beta-blockers — lower the hepatic venous pressure gradient — propranolol.** Beta-1 blockade lowers cardiac output; beta-2 blockade leaves alpha-mediated splanchnic vasoconstriction unopposed, so inflow falls. Carvedilol adds alpha-1 blockade, which lowers intrahepatic resistance, and is preferred in compensated cirrhosis (Baveno VII). Primary prophylaxis of large varices: a beta-blocker (carvedilol preferred), or banding if beta-blockers are not tolerated. Secondary prophylaxis after a bleed: banding every 2–4 weeks until varices are gone PLUS a beta-blocker; the combination beats either alone. TIPS is for failure of this combination or pre-emptive in high-risk patients. In portal vein thrombosis with large varices, variceal prophylaxis (beta-blocker or banding) is put in place and anticoagulation follows without long delay; Baveno VII prefers to start with LMWH (then LMWH, a vitamin K antagonist or a DOAC), partly because the raised baseline INR makes warfarin hard to monitor."),
    ('c', "**Venodilators — lower intrahepatic and collateral resistance — isosorbide mononitrate.** Nitrates also lower blood pressure, which reflexly reduces the benefit, and they are not used alone."),
    ('d', "**Antifibrinolytics — slow plasminogen to plasmin — tranexamic acid: not recommended (HALT-IT: no fewer bleeding deaths, more venous thrombosis).** Tranexamic acid and aminocaproic acid are lysine analogues that block plasminogen binding to fibrin, so it is not converted to plasmin. HALT-IT (12,009 patients with GI bleeding) found death from bleeding 4% in both arms and venous thrombosis 0.8% vs 0.4%; Baveno VII does not recommend it."),
  ],
  mimic=[
    ("Acute vs chronic phase", "Acute bleed: vasoconstrictor for 2–5 days, beta-blocker held (it lowers blood pressure in a shocked patient). After the bleed: beta-blocker plus banding."),
  ],
  traps=[
    ("“TIPS is first-line to prevent recurrent variceal bleeding (DocT key C)”", "The key is wrong and contradicts DocT’s own explanation: banding plus beta-blocker is first line (Baveno VII, AASLD). Only 45% matched the key; the exam-day answer for a stable patient after a first bleed is EVL + NSBB."),
    ("“Propranolol is started during the acute bleed”", "It is for the chronic phase (CLD-16 g)."),
    ("“Large varices with portal vein thrombosis: anticoagulate first”", "Prevent bleeding first with a beta-blocker (or banding); the Marrow key is propranolol."),
  ],
  decode=[
    ("Which reduces recurrent variceal bleeding in the long term? [DocT]", "EVL + NSBB (DocT keys TIPS, which is wrong)."),
    ("After band ligation, drug to prevent rebleeding? [Marrow]", "Propranolol."),
    ("Cirrhosis with portal vein thrombosis and large non-bleeding varices — next step? [Marrow]", "Propranolol."),
    ("Mechanism of aminocaproic acid? [Marrow]", "Blocks conversion of plasminogen to plasmin."),
  ],
  punch="Vasoconstrictors cut portal inflow during the bleed; beta-blockers, with banding, prevent the next one, and TIPS is for when that fails. Tranexamic acid has no place.",
)

L['CLD-13'] = dict(
  sub="Cirrhosis I → Ascites and hydrothorax → Diagnosis: SAAG",
  step=5,
  intro="Step 5 begins with telling portal hypertensive ascites from the rest. The serum–ascites albumin gradient measures the oncotic difference that balances the hydrostatic push from the sinusoids, so a wide gradient means high sinusoidal pressure. The one real question was answered correctly by only 30%: pancreatic ascites is the low-SAAG option.",
  parts=[
    ('a', "**Serum albumin minus ascitic albumin.** Measured on the same day. A SAAG of 1.1 g/dL or more identifies portal hypertension with about 97% accuracy. It is a gradient, not a ratio, and it does not use total protein."),
    ('b', "**Portal hypertension: cirrhosis, heart failure, Budd–Chiari.** Raised sinusoidal pressure pushes out water with little albumin, so the gradient is wide. Ascitic total protein then separates them: under 2.5 g/dL in cirrhosis (capillarised sinusoids hold protein back, CLD-04), 2.5 or more in heart failure and early Budd–Chiari (normal, leaky sinusoids let protein through)."),
    ('c', "**Tuberculosis, carcinomatosis, pancreatitis, peritonitis, nephrotic syndrome.** The fluid comes from the peritoneum or a leak, not from the sinusoids, so its albumin is close to serum and the gradient is narrow. Pancreatic ascites has a high amylase; tuberculous ascites is lymphocytic with a raised ADA. Nephrotic syndrome is low SAAG because serum albumin is very low. ‘Peritonitis’ here means secondary or tuberculous peritonitis; spontaneous bacterial peritonitis is infected cirrhotic ascites and stays high SAAG."),
    ('d', "**Budd–Chiari syndrome or trauma.** Sudden hepatic venous outflow block distends the liver capsule, causing pain, hepatomegaly and rapidly accumulating ascites."),
  ],
  mimic=[
    ("Cirrhotic vs cardiac ascites", "Both are high SAAG; cirrhosis has ascitic protein under 2.5 g/dL, cardiac ascites 2.5 or more."),
  ],
  traps=[
    ("“Budd–Chiari or heart failure gives low-SAAG ascites”", "Both are post-sinusoidal portal hypertension and high SAAG; their high protein is what misleads. Only 30% chose pancreatic ascites on DocT."),
    ("“Tuberculous ascites has a high SAAG”", "Low; the fluid is exudative (CLD-16 h)."),
  ],
  decode=[
    ("Which condition gives low-SAAG (under 1.1) ascites — Budd–Chiari, cardiac failure, cirrhosis, pancreatic? [DocT]", "Pancreatic ascites (30% right)."),
  ],
  punch="SAAG of 1.1 or more means portal hypertension (cirrhosis, heart failure, Budd–Chiari), with protein separating cirrhosis (low) from cardiac and Budd–Chiari (high); pancreatic, tuberculous, malignant and nephrotic ascites are low SAAG.",
)

L['CLD-14'] = dict(
  sub="Cirrhosis I → Ascites and hydrothorax → Hyponatraemia and treatment of ascites",
  step=5,
  intro="Step 5 continues with why the kidney makes things worse and how ascites is treated. The vasodilated circulation makes the kidney hold sodium and even more water, so the patient is sodium-overloaded and hyponatraemic at once. Three real questions: the first step for hypervolaemic hyponatraemia (only 30% right), the next step in refractory ascites (56%), and long-term albumin.",
  parts=[
    ('a', "**Splanchnic vasodilatation lowers effective volume and renal cortical flow, activating RAAS and ADH: sodium AND water are retained, water more than sodium.** ADH is released by low arterial filling (non-osmotic release), overriding the low plasma osmolality, so free water is kept. Total body sodium is high, serum sodium is low: dilutional, hypervolaemic hyponatraemia. Urine sodium is low because the kidney is avid for sodium."),
    ('b', "**Sodium restriction; free-water restriction if hyponatraemic.** Sodium about 80–120 mmol (4.6–6.9 g salt) a day (EASL 2018); stricter restriction reduces intake and worsens malnutrition. Fluid restriction to 1–1.5 L/day only when the patient is hypervolaemic and sodium is under 125 mmol/L; diuretics are stopped at that level. Hypertonic saline only for severe symptoms (seizures, coma) or just before transplant, because the patient is already sodium-overloaded. Correct by no more than 8 mmol/L in 24 hours: malnutrition, low potassium and alcohol make cirrhotics very prone to osmotic demyelination."),
    ('c', "**Spironolactone with furosemide, ratio 100:40 mg (standard teaching, not in your notes).** Spironolactone leads because secondary hyperaldosteronism drives sodium reabsorption in the collecting duct; a loop diuretic alone loses its effect when that sodium is reabsorbed downstream. Increase in steps to 400:160 mg; the ratio keeps potassium normal. A first episode of moderate ascites can be treated with spironolactone alone. Weight loss no more than 0.5 kg/day without oedema, 1 kg/day with it."),
    ('d', "**Replace when under 3 g/dL; target above 3 g/dL.** Current evidence says otherwise: there is no serum-albumin target. ATTIRE (NEJM 2021) raised albumin to 3 g/dL or more in hospitalised patients and found no fewer infections, kidney failures or deaths but more pulmonary oedema. Albumin is given for specific indications: large-volume paracentesis over 5 L (6–8 g per litre removed), SBP (1.5 g/kg on day 1, 1 g/kg on day 3) and HRS-AKI. Long-term weekly albumin in uncomplicated ascites on diuretics (ANSWER 2018: 40 g twice weekly for 2 weeks, then 40 g weekly) improved 18-month survival (77% vs 66%) and reduced SBP, encephalopathy, renal dysfunction and paracenteses, through non-oncotic effects; MACHT in wait-listed patients was negative, and UK guidance does not yet recommend it routinely."),
    ('e', "**V2-receptor antagonists at the collecting duct: aquaresis; also reduce ascites.** They block ADH and excrete free water, raising sodium. But they are little used in cirrhosis: tolvaptan carries an FDA warning against use in liver disease (hepatotoxicity), and satavaptan was no better than placebo for controlling ascites (with higher mortality in one trial), so they do not have a role in treating ascites."),
    ('f', "**Midodrine, terlipressin; large-volume paracentesis with albumin; TIPS.** Refractory ascites does not respond to sodium restriction and maximum diuretics, recurs early after paracentesis, or the diuretics cannot be tolerated (renal failure, hyperkalaemia, hyponatraemia). Serial large-volume paracentesis with albumin is the first step; covered TIPS is offered when paracentesis is needed often and the patient is suitable (it can improve survival); midodrine may help selected patients; an alfapump is for special circumstances; transplant is the cure. Terlipressin is a treatment of HRS-AKI, not of refractory ascites. Synthetic plasma expanders are inferior to albumin after paracentesis."),
  ],
  mimic=[
    ("Hypervolaemic (dilutional) vs hypovolaemic hyponatraemia in cirrhosis", "Dilutional: oedema and ascites, no diuretic overuse; restrict fluid. Hypovolaemic: diuretic overuse or diarrhoea; stop diuretics and give saline."),
  ],
  traps=[
    ("“Sodium 120 with confusion in a cirrhotic: hypertonic saline, a vaptan or a loop diuretic”", "The confusion with asterixis and high ammonia is encephalopathy; the hyponatraemia is dilutional, so restrict fluid. Only 30% chose this on DocT."),
    ("“Diuretic-intolerant ascites: push furosemide to 160 mg, or use synthetic expanders, or an alfapump”", "Large-volume paracentesis with albumin, then TIPS. 44% missed it on DocT GT."),
    ("“Albumin works only by oncotic pressure”", "Long-term albumin (ANSWER) improves survival through antioxidant, endotoxin-binding and immune effects too."),
    ("“ATTIRE tested a target of 3.5 g/dL”", "The target was 3.0 g/dL (30 g/L); it showed no benefit and more fluid overload."),
  ],
  decode=[
    ("Cirrhosis, Na 120, low osmolality, low urine sodium, no diuretics, encephalopathy — management? [DocT]", "Fluid restriction (30% right)."),
    ("On maximum tolerated diuretics, renal function worsening, paracentesis twice monthly — next step? [DocT GT GT2]", "Large-volume paracentesis with albumin (56% right); TIPS if it keeps recurring."),
    ("Long-term albumin in decompensated cirrhosis — true statement? [DocT GT GT3]", "Improves survival in responsive ascites (ANSWER; 86% right)."),
  ],
  extra=[
    dict(q="Why is the urine sodium low in this hyponatraemia?", a="The kidney is retaining sodium under aldosterone because effective arterial volume is low; total body sodium is high. A low urine sodium with ascites points to dilutional hyponatraemia, not salt loss."),
  ],
  punch="The underfilled circulation makes the kidney keep sodium and more water, so the cirrhotic is sodium-overloaded yet hyponatraemic: restrict fluid, not salt replacement; treat ascites with sodium restriction, spironolactone-led diuretics, paracentesis with albumin and TIPS.",
)

L['CLD-15'] = dict(
  sub="Cirrhosis I → Ascites and hydrothorax → Hepatic hydrothorax",
  step=5,
  intro="Step 5 ends with ascites that has moved into the chest. Fluid passes through small defects in the diaphragm, drawn up by the negative pressure in the pleural space, so it can fill the chest even when there is little ascites. No real question has been linked.",
  parts=[
    ('a', "**Pleural effusion of more than 500 mL in cirrhosis, without cardiopulmonary cause.** Exclude heart failure, infection and malignancy first."),
    ('b', "**Right: defects near the bare area of the liver (right triangular ligament).** About 85% are right-sided, 13% left and 2% bilateral. The defects are gaps in the collagen bundles of the tendinous diaphragm; raised abdominal pressure from ascites stretches them into pleuroperitoneal blebs, which form more often on the right. Fluid moves one way, so the chest can fill while the abdomen looks dry."),
    ('c', "**Transudate: high SAAG-type gradient, low cell count.** Serum-to-pleural albumin gradient over 1.1 g/dL, low protein. Pleural neutrophils over 250/mm³ with a positive culture, or over 500/mm³ with a negative culture once pneumonia and a parapneumonic effusion are excluded, is spontaneous bacterial empyema: an infection of the transudate, not pus, so it is treated with antibiotics like SBP, not with a drain."),
    ('d', "**Repeated ultrasound-guided thoracentesis; exclude infection.** For breathlessness, alongside sodium restriction and diuretics, which are the basis of treatment."),
    ('e', "**A chest tube: it can convert it to empyema, with protein and fluid loss.** The pleura refills as fast as it drains, so the tube pours out litres of protein and electrolytes, causes renal failure and infection, and is hard to remove."),
    ('f', "**TIPS; liver transplant is definitive.** TIPS lowers the portal pressure that makes the fluid; an indwelling pleural catheter is an option when TIPS and transplant are not possible. Pleurodesis rarely works because fluid re-accumulates too fast."),
  ],
  mimic=[
    ("Right vs left effusion in a cirrhotic", "Right: hepatic hydrothorax until proved otherwise. Left: think pancreatitis, oesophageal rupture or another cause."),
  ],
  traps=[
    ("“A chest drain is the best treatment for hepatic hydrothorax”", "Avoid chest tubes; use needle drainage, diuretics and TIPS (CLD-16 i)."),
  ],
  decode=[
    ("Cirrhotic with a large right effusion and little ascites — mechanism and what to avoid? [pattern]", "Ascites through diaphragmatic defects; avoid a chest tube."),
  ],
  punch="Hepatic hydrothorax is ascites drawn through right diaphragmatic defects; treat it with diuretics, needle thoracentesis and TIPS, never a chest tube.",
)

L['CLD-16'] = dict(
  sub="Cirrhosis I → Sweep → True or false",
  step=6,
  intro="Step 6 checks the deck’s commonest reversals. Each false statement is a real misconception from the cards above. No real question has been linked to the sweep itself.",
  parts=[
    ('a', "**False: wedged minus free.** The free pressure is subtracted to remove caval pressure (CLD-03)."),
    ('b', "**False: pre-sinusoidal.** The wedged pressure reads the sinusoid, which is normal when the block is upstream."),
    ('c', "**False: 5.** Five items, each at least 1 point (CLD-07)."),
    ('d', "**False: not in Child-Pugh.** Creatinine is in MELD (CLD-08)."),
    ('e', "**True.** About half on the card’s series; most guidance quotes more (CLD-09)."),
    ('f', "**False: gastric first.** Then traction; oesophageal only if still bleeding (CLD-11)."),
    ('g', "**False: chronic phase.** Beta-blockers lower blood pressure in the shocked patient and are for preventing rebleeding (CLD-12)."),
    ('h', "**False: low SAAG.** The fluid comes from the peritoneum, not the sinusoids (CLD-13)."),
    ('i', "**False: avoid chest tubes.** They cause protein loss, renal failure and empyema (CLD-15)."),
  ],
  mimic=[
    ("Child-Pugh minimum vs MELD minimum", "Child-Pugh starts at 5; MELD has a floor of about 6 because values under 1 are set to 1."),
  ],
  traps=[
    ("“Oesophageal balloon first, beta-blocker now”", "Both reverse the right order: gastric balloon first; beta-blocker after the acute bleed."),
  ],
  decode=[
    ("True/false sweep of formulas and first steps [pattern]", "Wedged minus free; Child-Pugh minimum 5; gastric balloon first; NSBB chronic only; TB ascites low SAAG; no chest tube."),
  ],
  punch="Wedged minus free, pre-sinusoidal, a minimum of 5, no creatinine, half variceal, gastric first, beta-blockers later, TB low SAAG and no chest tube.",
)

FLAGS = {
  'CLD-08': "f: ‘in dialysed patients use the pre-dialysis creatinine’ is not the allocation rule: after dialysis twice in the past week (or 24 h of CRRT) creatinine is set to 4.0 mg/dL (3.0 in MELD 3.0). d: US allocation moved from MELD-Na to MELD 3.0 (adds sex and albumin) in July 2023.",
  'CLD-09': "Table percentages (50% varices, 24.2% gastric ulcer etc.) come from a single series in the notes and could not be traced; most guidance quotes up to about 70% variceal in cirrhosis. Explanation keeps the card figures and says so.",
  'CLD-10': "a: ‘correct fibrinogen by TEG’ and the nasogastric tube are not Baveno VII recommendations (6.37: no evidence that platelet count or fibrinogen predict failure; 6.11: caution with nasogastric tubes; 6.19: erythromycin 250 mg IV to clear the stomach). e: Baveno VII lists a self-expanding oesophageal stent as an equal, safer bridge. The linked Marrow key (emergent endoscopy as next step) is disputed: vasoactive drug and ceftriaxone come first.",
  'CLD-12': "Card layout error: the antifibrinolytic row prints ‘not recommended (HALT-IT: no fewer bleeding deaths, more venous thrombosis)’ twice. Linked DocT key (C, TIPS first-line secondary prophylaxis) is wrong; EVL + NSBB is correct.",
  'CLD-14': "d: ‘replace when under 3 g/dL; target above 3 g/dL’ is outdated (verified fix): ATTIRE 2021 showed no benefit and more pulmonary oedema; there is no serum-albumin target, albumin is for LVP >5 L, SBP and HRS-AKI. e: vaptans ‘also reduce ascites’ is not supported (satavaptan no better than placebo; tolvaptan FDA warning in liver disease). f: terlipressin is a treatment of HRS-AKI, not of refractory ascites. The qpack DocT line gives the ATTIRE target as 3.5 g/dL; the trial target was 3.0 g/dL (the card-layer line is correct).",
}
