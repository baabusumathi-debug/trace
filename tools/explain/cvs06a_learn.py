# CVS06A — Explain v3 ("Learn" depth): right ventricular failure and pulmonary hypertension, part 1 — epidemiology and registry figures, RV anatomy and physiology, coronary
# perfusion, RV vs LV structure and numbers, the pressure–volume loop, preload tolerance, ventricular interdependence, afterload and impedance, contractility, PVR, the pressure-overload
# spiral, acute and chronic causes, ARDS and cardiac surgery, the PH clinical classification (groups 1–5) and congenital heart disease. CVS06B is the second half.
# No mnemonics or hooks. Driven by qpack/CVS06A.md (20 question links; RVF-20 PH definition and group 1 asked 7 times, RVF-21 groups 3–5/CTEPH 4, RVF-10 and RVF-17 two each,
# RVF-01, RVF-12, RVF-18, RVF-19, RVF-22 one each). RVF-02 to RVF-09, RVF-11, RVF-13 to RVF-16 have no linked question and get short explanations with [pattern] decode items.
# Card layer (cvs_cardlayer.json) lines for RVF-01, RVF-10, RVF-17, RVF-20, RVF-21, RVF-22 read and covered; the RVF-20 `fix` (mPAP >20, PAWP ≤15, PVR >2 WU) and its `cross` note
# (DocT GT keys mPAP >25) are taught and FLAGGED. The trace qbank.json `fix` for RVF-20 is the same entry (checked 19 Nov 2026).
# Checked online on 19 Nov 2026:
#  - ESC/ERS 2022 PH guideline (Humbert, EHJ 2022;43:3618, academic.oup.com full text; Rev Esp Cardiol commentary): PH = mPAP >20 mmHg; pre-capillary = mPAP >20, PAWP ≤15, PVR >2 WU;
#    IpcPH = PAWP >15, PVR ≤2; CpcPH = PAWP >15, PVR >2; exercise PH = mPAP/CO slope >3 mmHg/L/min. Table 6 classification: group 1 idiopathic (non-responders, acute responders),
#    heritable, drug/toxin (methamphetamine, dasatinib definite), associated with CTD, HIV, portal hypertension, CHD, schistosomiasis; PAH with features of venous/capillary involvement
#    (PVOD/PCH); PPHN. Group 2 HF (preserved, reduced or mildly reduced EF), valvular disease, congenital/acquired post-capillary conditions. Group 3 obstructive, restrictive, mixed lung
#    disease, hypoventilation syndromes (renamed from sleep-disordered breathing), hypoxia without lung disease (high altitude), developmental lung disorders. Group 4 ‘PH associated with
#    pulmonary artery obstructions’: CTEPH and other PA obstructions. Group 5 haematological (chronic haemolytic anaemias, myeloproliferative), systemic (sarcoidosis, PLCH, NF1), metabolic
#    (glycogen storage, Gaucher), chronic renal failure ± dialysis, pulmonary tumour thrombotic microangiopathy, fibrosing mediastinitis. CTEPH after acute PE: 3.2% of survivors (meta-analysis),
#    FOCUS 2.3% at 2 years; risk factors include splenectomy, permanent intravascular devices, IBD, myeloproliferative disease, APS (VKA, not DOAC), high-dose thyroxine, malignancy.
#    CTEPH: lifelong anticoagulation; PEA if operable; BPA (I, B) if inoperable or residual PH; riociguat (I, B) for inoperable or persistent/recurrent PH; evaluate persistent dyspnoea at
#    3–6 months after PE. Eisenmenger: bosentan recommended for symptomatic patients; combination if no response.
#  - ASE 2015 chamber quantification (as tabulated, mycardio echo notes citing Lang 2015): TAPSE <17 mm, S′ <9.5 cm/s, FAC <35%, 3D RVEF <45%, basal diameter >41 mm abnormal.
#  - Mekontso Dessap (ICM 2016, n 752 moderate–severe ARDS on protective ventilation, TOE): acute cor pulmonale 22%; risk factors pneumonia, driving pressure ≥18 cmH₂O, P/F <150,
#    PaCO₂ ≥48 mmHg; overall mortality not different, severe ACP 57% vs 42%.
#  - AHA/ACC 2026 acute PE guideline exists (EVToday summary); ESC 2019 PE remains the ESC document. Neither changes anything on these cards.
# Reviewer check 19 Nov 2026: ESC/ERS 2022 full text (cardio.by ehac237.pdf): severe PH in lung disease = PVR >5 WU; bosentan in symptomatic Eisenmenger I/B; CHD sits in group 1 (1.4.4) and
#  group 2 (2.3), not group 5; CTEPH 3.2% of PE survivors. Epidemiology (AJEM review; Lung 2025 review): 3–9% of AHF admissions from OFICA, ESC-HF pilot, RO-AHFS, EHFS II; 2.2% in
#  CHARITEM; in-hospital mortality 5–17% (EHFS II). The AHEAD-specific figure could not be confirmed. Mekontso Dessap 2016 abstract (QxMD) confirmed. Naxos = JUP, Carvajal = DSP, LV
#  (MedlinePlus). Durant: left lateral, head down, postulated to hold air in the right heart away from the pulmonary outflow (FPnotebook).
# From standard references without a fresh check (confident unless said): Harjola 2016 ESC-HFA RV failure statement (definition of acute RV failure);
# RV wall thickness >5 mm = RVH (Rudski ASE 2010); RV stroke work about one quarter to one sixth of LV; PVR × 80 = dyn·s·cm⁻⁵ (2 WU = 160); Wood units = mmHg·min/L; BREATHE-5 (bosentan
# in Eisenmenger, 2006); Durant manoeuvre; ARVC genetics (PKP2 commonest; Naxos = plakoglobin JUP, recessive; Carvajal = desmoplakin, LV-dominant); systemic RV after atrial switch for
# d-TGA or in congenitally corrected TGA is a pressure-loaded RV (less sure of the card source’s intent); late pulmonary regurgitation after TOF repair.

SPINE = [
  ("How big the problem is", "Acute RV failure is a few per cent of acute heart failure admissions but carries a high mortality, and true failure means a dysfunctional RV that can fill only at a high venous pressure."),
  ("A thin pump for a low-pressure circuit", "The RV is a thin, crescent-shaped, peristaltic pump perfused through the whole cardiac cycle, built to move volume into a compliant, low-resistance pulmonary bed."),
  ("Tolerates volume, not pressure", "The same low muscle mass that lets the RV dilate to take extra volume leaves it unable to generate pressure, so afterload, measured imperfectly by PVR, is the main determinant of its output."),
  ("Interdependence and the spiral", "A pressure-loaded RV dilates inside a fixed pericardium, pushes the septum into the LV, cuts LV filling and coronary perfusion, and so feeds its own ischaemia in a vicious circle."),
  ("What pushes the RV over", "Acute failure comes from lost contractility (RV infarct, sepsis, surgery), volume (transfusion) or pressure (PE, ARDS, positive-pressure ventilation, hypoxia, acidosis); chronic failure from congenital, valvular, myocardial and pulmonary vascular disease."),
  ("Pulmonary hypertension: five groups", "PH is now mPAP over 20 mmHg, and the wedge pressure and PVR sort it into pre-capillary arterial disease (group 1, 3, 4) or post-capillary left heart disease (group 2), with group 5 the miscellaneous rest."),
]

PRIMER = "The right ventricle pumps the same cardiac output as the left but into a circuit with about a tenth of the resistance, so it works at a mean pulmonary pressure of about 15 mmHg against the LV’s 90. Afterload for the RV is set by pulmonary vascular resistance (mean PA pressure minus wedge pressure, divided by cardiac output) together with the stiffness of the large pulmonary arteries. The two ventricles share a septum and sit inside a pericardium that hardly stretches acutely, so whatever enlarges one ventricle squeezes the other. Pulmonary hypertension is diagnosed on right heart catheterisation; echo only estimates its probability."

L = {}

L['RVF-01'] = dict(
  sub="RV failure → Introduction → Epidemiology, mortality and ICU settings",
  step=1,
  intro="Step 1 sets the size of the problem and what ‘failure’ means. The RV is uncommon as the primary cause of an acute heart failure admission but common as a complication in the ICU, and the one real question asked how true RV failure differs from mere RV dysfunction or a high CVP.",
  parts=[
    ('a', "**2–9% of acute heart failure admissions to hospital.** Most acute heart failure is left-sided; isolated acute RV failure is a minority. The figure varies with how strictly RV failure is defined (RVF-02 gives 3–9%, which the card attributes to AHEAD)."),
    ('b', "**In-hospital mortality 5–17%.** This is higher than for many acute LV presentations because RV failure is usually driven by something else serious (massive PE, ARDS, RV infarct) and because a failing RV cannot be supported easily: fluid, vasodilators and positive pressure can each make it worse."),
    ('c', "**ARDS, MI, pulmonary embolism, decompensated chronic lung disease, after cardiac surgery; worsening RV function directly affects ICU mortality.** Each of these either raises RV afterload suddenly (PE, ARDS, hypoxic and hypercapnic lung disease) or removes RV contractility (RV infarct, bypass stunning). The definition that decides questions: RV failure is RV dysfunction with limited RV filling, so the RV can only fill and deliver an adequate stroke volume to the LV at the cost of a high CVP and venous congestion."),
  ],
  mimic=[
    ("RV failure vs RV dysfunction", "Dysfunction is an abnormal RV on imaging with normal filling pressures; failure is dysfunction plus a high CVP and inadequate forward flow."),
    ("RV failure vs hypervolaemia", "A high CVP with a normally contracting RV is volume, not failure; it falls with diuresis without improving output problems."),
  ],
  traps=[
    ("“True RV failure is an elevated CVP with normal RV function”", "That is volume loading. Failure needs the RV itself to be dysfunctional and unable to fill without a high CVP (69% chose correctly on DocT GT)."),
    ("“Increased RV filling without decreased output defines failure”", "If output is maintained, the RV is coping; failure is the point where more filling no longer buys more stroke volume."),
  ],
  decode=[
    ("Septic shock, CVP 16, low CO, dilated poorly contracting RV — which best defines true RV failure? [DocT GT]", "RV dysfunction with limited RV filling (69%)."),
    ("Proportion of acute heart failure admissions due to acute RV failure / its in-hospital mortality [pattern]", "2–9% (card’s AHEAD figure 3–9%); 5–17%."),
  ],
  punch="RV failure is not a high CVP and not a weak RV on echo alone: it is a dysfunctional RV that can fill only at a high venous pressure and still cannot deliver enough to the LV, and it carries an in-hospital mortality up to about one in six.",
)

L['RVF-02'] = dict(
  sub="RV failure → Introduction → AHEAD registry and HFpEF",
  step=1,
  intro="Step 1 again, with the registry figures that support the introduction. Never asked directly; the numbers matter only to recognise them in an option.",
  parts=[
    ('a', "**AHEAD registry: 3–9% of acute heart failure admissions; in-hospital mortality of acute RV failure 5–17%.** These are the figures the card gives for AHEAD. In the literature the 3–9% range comes from several European registries (OFICA, ESC-HF pilot, RO-AHFS, EuroHeart Failure Survey II), the 2.2% lower end of the introduction’s range from the CHARITEM registry, and the 5–17% mortality from EuroHeart Failure Survey II. The spread reflects definition: some registries count only isolated right heart failure, others any acute RV failure."),
    ('b', "**RV dysfunction in HFpEF: 14–40% across cohorts.** In HFpEF a stiff LV raises left atrial pressure, which is transmitted back to the pulmonary circulation (post-capillary PH, group 2, RVF-20). The RV then faces a raised afterload and fails in a sizeable minority, and when it does, prognosis worsens sharply."),
  ],
  mimic=[
    ("2–9% vs 3–9%", "Lower end from CHARITEM (2.2%) vs pooled European registries (3–9%); same mortality, 5–17%."),
  ],
  traps=[
    ("“RV dysfunction is rare when LV function is normal”", "Up to 40% of HFpEF patients have it, driven by post-capillary pulmonary hypertension."),
  ],
  decode=[
    ("Prevalence of RV dysfunction in HFpEF [pattern]", "14–40%."),
  ],
  punch="Acute RV failure is single-digit per cent of heart failure admissions with up to 17% in-hospital mortality, and a normal LV ejection fraction does not protect the RV: up to 40% of HFpEF patients have RV dysfunction.",
)

L['RVF-03'] = dict(
  sub="RV failure → Anatomy → Free wall, cavity, crista, fibres",
  step=2,
  intro="Step 2 starts with the shape of the pump, because almost every later behaviour of the RV follows from its thin wall. Not asked directly; the anatomy explains why TAPSE works and why the RV fails under pressure.",
  parts=[
    ('a', "**Thin (2–3 mm), compliant free wall forming a hemi-ellipsoid that adheres to the LV.** A thin wall is cheap to perfuse and stretches easily, which suits a low-pressure circuit. By Laplace, wall stress rises with radius and pressure and falls with thickness, so a thin wall develops high stress as soon as pressure rises. On echo a free wall over 5 mm in diastole means hypertrophy, which implies chronic pressure load."),
    ('b', "**Crescent-shaped cavity.** The RV wraps around the convex septum, so in cross-section it is a crescent. This shape gives a large surface for a small volume change, efficient for moving volume at low pressure, and makes RV volume hard to measure by 2D echo (no simple geometric formula fits)."),
    ('c', "**Crista supraventricularis: muscular ridge connecting the inflow and outflow tracts.** It separates the trabeculated inflow from the smooth infundibulum and contributes to the peristaltic sequence of contraction (RVF-04)."),
    ('d', "**Superficial circular fibres and deeper longitudinal fibres.** The LV has a third, middle circumferential layer; the RV does not, so RV ejection depends heavily on longitudinal shortening that pulls the tricuspid annulus towards the apex. That is why TAPSE, a single longitudinal measure, tracks RV function reasonably well."),
  ],
  mimic=[
    ("RV vs LV wall layers", "RV two layers, mainly longitudinal shortening; LV three layers with a dominant middle circumferential layer and radial thickening."),
  ],
  traps=[
    ("“A thick RV free wall is normal in an adult”", "Normal is 2–3 mm; over 5 mm on echo is RV hypertrophy and points to chronic pressure overload."),
  ],
  decode=[
    ("Why is TAPSE a valid surrogate of RV systolic function? [pattern]", "RV ejection is dominated by longitudinal fibre shortening."),
  ],
  punch="The RV is a 2–3 mm crescent that ejects mainly by longitudinal shortening, which makes it efficient at moving volume, easy to assess by TAPSE and defenceless against a sudden rise in pressure.",
)

L['RVF-04'] = dict(
  sub="RV failure → Physiology → Stroke work, circuit, peristalsis",
  step=2,
  intro="Step 2 continued: how the thin pump works against its low-pressure circuit. Not asked directly.",
  parts=[
    ('a', "**RV stroke work is one quarter of the LV.** Both ventricles eject the same stroke volume, but the RV does it against a mean pressure of about 15 mmHg instead of about 90, so it does a fraction of the work with a fraction of the muscle."),
    ('b', "**Highly compliant, low-resistance pulmonary circulation.** PVR is about a tenth of SVR, and the pulmonary bed can recruit and distend vessels, so flow can double with little rise in pressure in a healthy lung."),
    ('c', "**Peristaltic contraction: free-wall area falls and longitudinal fibres shorten, starting at the inflow tract and moving towards the outflow tract.** Contraction sweeps from the inlet to the infundibulum with a delay of a few tens of milliseconds, squeezing blood forward like a peristaltic wave rather than a radial squeeze."),
    ('d', "**Lower peak systolic pressure than the LV; exists at a higher steady-state volume.** RV systolic pressure is about 25 mmHg, and RV end-diastolic volume is normally a little larger than the LV’s, so the RV works on a flatter, high-volume portion of its pressure–volume relationship."),
  ],
  mimic=[
    ("RV vs LV contraction", "RV peristaltic, inflow to outflow, longitudinal; LV radial thickening with twisting."),
  ],
  traps=[
    ("“The RV does about the same stroke work as the LV because it ejects the same stroke volume”", "Stroke work is stroke volume × the pressure developed; with the same volume but a far lower ejection pressure, RV stroke work is about a quarter of the LV’s (some sources give a quarter to a sixth)."),
  ],
  decode=[
    ("RV stroke work relative to LV [pattern]", "About one quarter."),
  ],
  punch="The RV moves the same volume as the LV against a sixth of the pressure, with a peristaltic inflow-to-outflow contraction, which is why it is a volume pump and not a pressure pump.",
)

L['RVF-05'] = dict(
  sub="RV failure → Physiology → Coronary perfusion",
  step=2,
  intro="Step 2’s last piece of normal physiology: the RV is perfused throughout the cardiac cycle, and losing that advantage is what turns pressure overload into ischaemia (RVF-15). Not asked directly.",
  parts=[
    ('a', "**80% of the population: RV supplied by the right coronary artery; remaining 20%: the left coronary artery.** The 80/20 split follows coronary dominance: in most people the RCA gives the acute marginal branches to the free wall. The anterior RV wall and the moderator band also receive branches from the LAD in most people, which is one reason RV infarction is less complete and recovers better than LV infarction."),
    ('b', "**Unlike the LV, RV perfusion occurs during both systole and diastole, giving oxygen delivery throughout the cardiac cycle.** Coronary flow depends on aortic pressure minus the pressure in the surrounding myocardium. LV systolic pressure equals aortic pressure, so the LV is perfused only in diastole. RV systolic pressure (about 25 mmHg) is far below aortic pressure, so flow continues in systole."),
    ('c', "**Disrupted by pulmonary arterial hypertension.** When RV systolic pressure rises towards systemic, the systolic gradient disappears and the RV becomes diastole-dependent like the LV, while its wall stress and oxygen demand rise. Systemic hypotension narrows the gradient further, which is why keeping aortic pressure up (noradrenaline) protects a pressure-loaded RV."),
  ],
  mimic=[
    ("RV vs LV coronary flow timing", "RV: systole and diastole; LV: diastole only, because LV systolic pressure equals aortic pressure."),
  ],
  traps=[
    ("“Like the LV, the RV is perfused only in diastole”", "Only when RV pressure approaches systemic, as in severe PH; normally flow is continuous."),
  ],
  decode=[
    ("Why is the RV at risk of ischaemia in severe PH with hypotension? [pattern]", "Loss of systolic coronary flow plus a lower aortic driving pressure and higher wall stress."),
  ],
  punch="RV coronary flow runs through systole as long as RV pressure stays well below aortic pressure; pulmonary hypertension and hypotension remove that margin, and the RV becomes ischaemic.",
)

L['RVF-06'] = dict(
  sub="RV failure → RV vs LV → Structure",
  step=2,
  intro="Step 2 set side by side with the LV: each structural row is a consequence of one ventricle being built for volume and the other for pressure. Not asked directly.",
  parts=[
    ('a', "**Morphology: RV complex and crescentic; LV bullet-shaped, ellipsoid.** A sphere-like LV generates pressure efficiently; a wrap-around crescent moves volume efficiently."),
    ('b', "**Cross-section: RV semicircular, serpentine; LV circular.** In short axis the RV is a crescent hugging the septum; when it is pressure-loaded the septum flattens and the LV becomes D-shaped (RVF-10)."),
    ('c', "**Myocardium: RV thin and heavily trabeculated; LV thick, smooth-walled with fine trabeculations.** Coarse trabeculation and the moderator band are how the RV is identified on echo or in congenital disease, whatever its position."),
    ('d', "**Pump: RV peristaltic-like from inflow to outflow, with bellows-like free-wall motion towards the septum; LV radial thickening and contraction.** The RV ejects by longitudinal shortening and by pulling the free wall in towards the septum; LV contraction also pulls the septum, so part of RV output comes from LV contraction."),
    ('e', "**Flow: RV has no or minimal isovolumetric periods; LV has well-defined isovolumetric periods.** The PA opens almost as soon as the RV starts to contract, and flow coasts on after RV pressure falls (RVF-08)."),
  ],
  mimic=[
    ("Identifying the morphological RV", "Coarse trabeculation, moderator band and a more apical tricuspid valve, not its position or wall thickness."),
  ],
  traps=[
    ("“The RV has distinct isovolumetric contraction and relaxation like the LV”", "Both phases are short or absent because the pulmonary circuit is low-pressure."),
  ],
  decode=[
    ("Which feature distinguishes RV from LV flow? [pattern]", "Minimal isovolumetric periods."),
  ],
  punch="The LV is a thick, smooth ellipsoid that squeezes radially with clear isovolumetric phases; the RV is a thin, trabeculated crescent that ejects peristaltically with almost none, because one faces 120 mmHg and the other 25.",
)

L['RVF-07'] = dict(
  sub="RV failure → RV vs LV → The numbers",
  step=2,
  intro="Step 2 in numbers. Not asked directly, but the ejection fraction row is the one most likely to appear: a normal RV ejection fraction starts lower than a normal LV one.",
  parts=[
    ('a', "**End-diastolic thickness ≤3 mm vs ≤11 mm; volume 49–101 vs 44–89 (mL/m²); EF 40–68% vs 57–74%.** These are cardiac MRI-type normal ranges. The RV is slightly larger and ejects a smaller fraction of its volume because its crescent shape gives a big volume for a small inward movement. On echo the cut-offs differ: ASE 2015 calls a 3D RVEF under 45% abnormal and an RV wall over 5 mm hypertrophied, so ‘RVEF 45% is normal’ sits at the lower limit."),
    ('b', "**Systolic pressure 25 vs 120 mmHg; coronary perfusion continuous vs diastolic.** The pressure difference explains the perfusion difference (RVF-05)."),
    ('c', "**RV tolerates volume overload better (compliance rises); LV tolerates pressure overload better.** Thin compliant muscle dilates; thick muscle generates pressure (RVF-12)."),
    ('d', "**P–V loop: RV trapezoidal; LV rectangular, with rapid rise and fall in pressure.** RVF-08 explains the shape."),
  ],
  mimic=[
    ("RVEF 45% vs LVEF 45%", "Low-normal for the RV; reduced for the LV."),
  ],
  traps=[
    ("“An RVEF of 45% means RV systolic dysfunction”", "The RV’s normal range starts at about 40–45%; the LV’s at about 55%."),
  ],
  decode=[
    ("Normal RV systolic pressure and timing of RV coronary flow [pattern]", "About 25 mmHg; continuous through the cycle."),
  ],
  punch="The RV is thinner (≤3 mm), slightly larger, works at 25 mmHg, is perfused continuously and has a lower normal ejection fraction than the LV, so one cut-off cannot be applied to both ventricles.",
)

L['RVF-08'] = dict(
  sub="RV failure → Physiology → The pressure–volume loop",
  step=2,
  intro="Step 2 ends with the loop that summarises the pump. Every difference in shape follows from the low-pressure circuit downstream, not from the muscle itself. Not asked directly.",
  parts=[
    ('a', "**LV loop rectangular with parallel sides from well-defined isovolumetric contraction and relaxation, and sharp corners where systole and diastole begin and end.** The aortic valve opens only once LV pressure reaches about 80 mmHg, so the LV must spend a measurable time building pressure at constant volume, and the same in reverse at the end of systole."),
    ('b', "**RV isovolumetric contraction is shorter: the pulmonary valve opens as soon as RV pressure exceeds the low PA pressure.** PA diastolic pressure is about 10 mmHg, so very little pressure needs to be built before ejection starts."),
    ('c', "**End-systole is less well defined, so the RV loop looks almost triangular.** RV pressure peaks early and then falls while ejection continues, rounding off the upper left corner."),
    ('d', "**Ejection continues despite falling RV pressure because of the momentum of blood in the low-pressure system, so isovolumetric relaxation is shortened or absent.** In a compliant, low-impedance bed, blood keeps moving forward after the RV has started to relax (the ‘hangout’ period). When PVR rises, momentum is lost early, the loop becomes rectangular like the LV’s, and an isovolumetric phase reappears: a sign of pressure overload."),
  ],
  mimic=[
    ("Short isovolumetric contraction vs absent isovolumetric relaxation", "The first because the PA opens early; the second because flow coasts on momentum."),
  ],
  traps=[
    ("“The RV loop is triangular because RV muscle contracts differently”", "It is the low-pressure, compliant circuit downstream that shapes it; raise PVR and it becomes rectangular."),
  ],
  decode=[
    ("Why is RV isovolumetric relaxation absent? [pattern]", "Ejection continues on blood momentum into a low-pressure bed."),
  ],
  punch="The RV loop is nearly triangular because the pulmonary valve opens early and blood keeps flowing after RV pressure falls; a rising PVR squares the loop off, which is what pressure overload looks like.",
)

L['RVF-09'] = dict(
  sub="RV failure → Mechanics → Preload tolerance and its limit",
  step=3,
  intro="Step 3 is the central asymmetry: the RV takes volume well and pressure badly. This card is the volume side and its limit. Not asked directly, but it is the reason a fluid bolus can harm a failing RV.",
  parts=[
    ('a', "**The RV is tolerant of preload.** A compliant chamber accepts extra volume with little rise in pressure, as in an ASD or tricuspid regurgitation, which can be tolerated for decades."),
    ('b', "**Low muscle mass lets the compliant RV dilate (up to a point) in the face of excess volume.** Thin muscle offers little resistance to stretch, so the chamber enlarges rather than its pressure rising."),
    ('c', "**With ongoing distension, decompensation occurs and failure ensues.** Past a point, stretch increases wall stress (Laplace) and oxygen demand without more output, and the chamber meets the limit of the pericardium."),
    ('d', "**Excess RV dilatation → tricuspid annulus dilates → TR → RA pressure rises → LV filling and function impaired.** The tricuspid annulus has little fibrous support, so it stretches with the RV; regurgitation adds more volume to the RV and raises venous pressure. Meanwhile the dilated RV pushes the septum into the LV (RVF-10), so LV preload and output fall. This is why fluid given to a dilated, failing RV can lower cardiac output."),
  ],
  mimic=[
    ("Preload-responsive RV vs over-distended RV", "The first increases output with fluid (e.g. early RV infarct); the second dilates, develops TR and compresses the LV, so output falls."),
  ],
  traps=[
    ("“The RV tolerates preload, so keep giving fluid in RV failure”", "Only up to a point; beyond it, TR and septal shift lower LV filling. Volume is given cautiously and stopped when CVP rises without output."),
  ],
  decode=[
    ("Why can a fluid bolus worsen hypotension in RV failure? [pattern]", "Annular dilatation and TR, plus septal shift reducing LV filling."),
  ],
  punch="The RV takes extra volume by dilating, but only up to a point: once the annulus stretches and the septum bows, more fluid raises venous pressure and lowers LV filling and output.",
)

L['RVF-10'] = dict(
  sub="RV failure → Mechanics → Ventricular interdependence",
  step=4,
  intro="Step 4 is where RV trouble becomes LV trouble. The two ventricles share a septum inside a pericardium that cannot stretch acutely, so a distended RV steals space from the LV. Both linked questions test this: pulsus paradoxus in tamponade, and a high left atrial pressure with a small LV.",
  parts=[
    ('a', "**Pathological rises in RV filling pressure are transmitted to the interventricular septum.** The septum is a shared wall; its position is set by the pressure difference across it at each moment of the cycle."),
    ('b', "**The RV is constrained by the pericardium, so the septum shifts leftwards and the LV becomes D-shaped.** With a fixed outer envelope, the only way the RV can enlarge is inwards, against the LV. A D-shaped LV in diastole means RV volume overload; persisting into systole means pressure overload."),
    ('c', "**Cardiac output falls through lower LV distensibility, lower preload and lower ventricular elastance, impairing LV diastolic filling.** The LV now has less room and a stiffer apparent compliance, so its end-diastolic volume is low even though its diastolic pressure (and the left atrial and wedge pressures) is high. This is the trap: a raised wedge pressure here does not mean the LV is full."),
    ('d', "**The same shift impairs RV contraction by distorting normal ventricular geometry.** The septum normally contributes to RV ejection (LV contraction pulls it); once it is flattened or bowed leftward, that contribution is lost."),
  ],
  mimic=[
    ("Septal shift vs LV diastolic failure", "Both give a high LA pressure; septal shift gives a small LV (low LVEDV), primary LV disease or aortic regurgitation a normal or large one."),
    ("Pulsus paradoxus in tamponade vs constriction", "Tamponade: inspiration fills the RV, the septum bows left, LV output falls; constriction shows discordant RV/LV pressures but pulsus paradoxus is less common."),
  ],
  traps=[
    ("“Inspiratory fall in BP in tamponade is from blood pooling in the lungs”", "Pooling contributes little; the key is inspiratory RV filling pushing the septum into the LV inside a fixed pericardium."),
    ("“Aortic regurgitation causes a high LA pressure with a low LVEDV”", "AR raises LVEDV. High LAP with a small LV comes from pulmonary hypertension, high PEEP or severe hypoxaemic respiratory failure through septal shift (Marrow ‘NOT a cause’ key)."),
  ],
  decode=[
    ("Large effusion, SBP falls 15 mmHg on inspiration — mechanism? [DocT GT]", "Inspiration raises RV filling, the septum shifts left, LV filling falls."),
    ("High LAP + low LVEDV ‘diastolic dysfunction’ — which is NOT a cause: PH, high PEEP, severe AHRF, AR? [Marrow]", "Aortic regurgitation."),
  ],
  punch="A fixed pericardium turns RV distension into LV compression: the septum shifts left, the LV becomes small but high-pressure, and output falls, which is why the wedge pressure misleads in RV failure and why inspiration drops the pulse in tamponade.",
)

L['RVF-11'] = dict(
  sub="RV failure → Mechanics → Afterload and impedance",
  step=3,
  intro="Step 3, the pressure side. RV afterload is more than PVR, and the RV handles any acute rise in it poorly. Not asked directly.",
  parts=[
    ('a', "**RV afterload is the load the RV has to overcome during ejection.** In practice it is the pulmonary arterial input impedance plus wall stress."),
    ('b', "**Influenced by PVR, PA distensibility and pulse wave reflections in the pulmonary bed; together called RV impedance.** PVR is the steady part; the pulsatile part depends on how stiff the proximal PAs are and how early reflected waves return. In PH, stiff arteries and early reflections can add a large load not visible in PVR (RVF-14)."),
    ('c', "**Less able to handle acute afterload changes because of its smaller muscle mass.** A thin wall cannot develop a high pressure quickly; a previously normal RV fails acutely at a mean PA pressure of around 40 mmHg. That is why a massive PE rarely produces a very high PA pressure: the RV fails first."),
    ('d', "**So the RV is described as intolerant of afterload.** Chronic loading lets it hypertrophy and reach systemic pressures over years (as in idiopathic PAH or Eisenmenger); acute loading does not allow that time."),
  ],
  mimic=[
    ("Acute vs chronic RV pressure load", "Acute: thin RV, failure at mPAP around 40, little hypertrophy; chronic: hypertrophied RV can reach systemic pressures."),
  ],
  traps=[
    ("“RV afterload equals PVR”", "PVR is only the steady component; impedance adds PA stiffness and wave reflection."),
  ],
  decode=[
    ("Massive PE in a previously well patient — why is the measured PA pressure only moderately raised? [pattern]", "A non-hypertrophied RV cannot generate more than about 40 mmHg mean before failing."),
  ],
  punch="RV afterload is impedance, not just PVR, and a thin RV that has had no time to hypertrophy fails at pressures a chronically loaded RV would cope with.",
)

L['RVF-12'] = dict(
  sub="RV failure → Mechanics → Preload tolerant, afterload intolerant",
  step=3,
  intro="Step 3 in one table: the same anatomical fact, low muscle mass, gives opposite responses to the two kinds of load. The one linked question applies this to the definition of RV failure in septic shock.",
  parts=[
    ('a', "**RV is preload tolerant: low muscle mass → compliant → dilates to accommodate volume.** Extra volume is absorbed by stretch with little pressure rise, up to the limit described in RVF-09."),
    ('b', "**RV is afterload intolerant: low muscle mass → cannot generate pressure against a rising load.** Its contractile reserve is small, so stroke volume falls as soon as impedance rises (RVF-11)."),
    ('c', "**RV tolerates volume overload better; LV tolerates pressure overload better.** The LV’s thick wall keeps wall stress down at high pressure (Laplace: stress falls with thickness), so aortic stenosis or hypertension is tolerated for years; the thin RV has no such protection, but its compliance lets it absorb volume."),
    ('d', "**On the curves, RV stroke volume falls steeply as mean PA pressure rises from 0 to 30 mmHg, while LV stroke volume declines only gently across 100–140 mmHg.** A modest PA rise, as in ARDS, high PEEP or a moderate PE, can halve RV output; the LV can absorb a 40 mmHg rise in aortic pressure with little loss. This is why lowering RV afterload (oxygen, correcting CO₂ and pH, lower plateau pressure, pulmonary vasodilators) improves output more than pushing preload."),
  ],
  mimic=[
    ("RV failure vs a full but functioning RV", "Failure: stroke volume does not rise with filling, CVP climbs; a functioning RV converts extra filling into output."),
  ],
  traps=[
    ("“RV failure is increased RV filling without decreased output”", "That is adaptation; failure is when filling rises (high CVP) and output does not (DocT GT, 69%)."),
    ("“The RV is afterload tolerant because it already works against a low resistance”", "Working at low resistance is exactly why it has little reserve when resistance rises."),
  ],
  decode=[
    ("Septic shock, CVP 16, low CO, dilated hypokinetic RV — true RV failure? [DocT GT]", "RV dysfunction with limited RV filling."),
    ("Stroke volume vs afterload curves: which ventricle falls steeply? [pattern]", "The RV, over a mean PA pressure of 0–30 mmHg."),
  ],
  punch="Low muscle mass makes the RV stretch easily and push weakly: it absorbs volume but its stroke volume collapses with even a modest rise in PA pressure, so treating RV failure is mostly treating its afterload.",
)

L['RVF-13'] = dict(
  sub="RV failure → Mechanics → Contractility and afterload",
  step=3,
  intro="Step 3 continued: even in a normal RV, afterload rather than intrinsic contractility sets ejection fraction. Not asked directly.",
  parts=[
    ('a', "**Afterload is the primary determinant of normal RV function.** RVEF is highly load-dependent, so a low RVEF often reflects a high PA pressure rather than weak muscle; contractility measured by end-systolic elastance is often preserved or raised early in PH."),
    ('b', "**RVEF is inversely proportional to pulmonary artery pressure.** As PA pressure rises, RVEF falls almost linearly; this is why RV–PA coupling (TAPSE relative to PA systolic pressure) is a better index than TAPSE alone in PH."),
    ('c', "**Antegrade flow from the pulmonary valve meets retrograde waves generated at the many bifurcations of the pulmonary tree.** Each branch point reflects part of the pressure wave back towards the RV."),
    ('d', "**This reduces antegrade flow and raises peak PA systolic pressure.** In a compliant bed the reflections return late, in diastole; in stiff PH vessels they return early, during ejection, adding to the load the RV must overcome."),
  ],
  mimic=[
    ("Low RVEF from afterload vs from myocardial disease", "Afterload: RVEF improves when PA pressure falls (e.g. after thrombolysis, iNO); myocardial: it does not."),
  ],
  traps=[
    ("“A low RVEF in PH means the RV muscle is failing”", "RVEF falls with PA pressure even with preserved contractility; the coupling of the two matters."),
  ],
  decode=[
    ("Main determinant of normal RV ejection [pattern]", "Afterload; RVEF falls as PA pressure rises."),
  ],
  punch="For the RV, ejection fraction is a measure of load as much as of muscle: it falls as PA pressure rises and wave reflections return earlier, so judge the RV against the pressure it faces.",
)

L['RVF-14'] = dict(
  sub="RV failure → Measurement → PVR",
  step=3,
  intro="Step 3’s measurement: PVR is the number used to grade RV afterload and to define pre-capillary PH (RVF-20), with one known blind spot. Not asked directly here, but the threshold appears in every PH definition question.",
  parts=[
    ('a', "**PVR = (mPAP − PCWP) × 80 / CO.** The transpulmonary gradient (mPAP minus wedge) is the pressure drop across the lung vessels; dividing by flow gives resistance. Without the ×80 the result is in Wood units (mmHg·min/L); with it, dyn·s·cm⁻⁵. ESC/ERS 2022 defines a raised PVR as over 2 WU (160 dyn·s·cm⁻⁵); older teaching used 3 WU."),
    ('b', "**Limitation: the impedance offered by the large pulmonary arteries is not reflected.** PVR is a steady-flow resistance; it ignores PA stiffness and wave reflection (RVF-11, 13). It also depends on an accurate wedge: if PCWP is overestimated, PVR is underestimated."),
  ],
  mimic=[
    ("Wood units vs dyn·s·cm⁻⁵", "Multiply Wood units by 80; 2 WU = 160, 3 WU = 240."),
  ],
  traps=[
    ("“PVR = mPAP / CO”", "Wedge pressure must be subtracted; otherwise a high left atrial pressure looks like pulmonary vascular disease."),
  ],
  decode=[
    ("mPAP 35, PCWP 10, CO 5 — PVR? [pattern]", "(35 − 10)/5 = 5 WU = 400 dyn·s·cm⁻⁵."),
  ],
  punch="PVR is the transpulmonary gradient divided by cardiac output, over 2 WU is raised by ESC 2022, and it misses the pulsatile load from stiff proximal pulmonary arteries.",
)

L['RVF-15'] = dict(
  sub="RV failure → Pathophysiology → The pressure-overload spiral",
  step=4,
  intro="Step 4 joins the pieces: wall stress, ischaemia, interdependence and shock form a loop that closes through coronary perfusion. Not asked directly, but every management step for acute RV failure aims at a link in this chain.",
  parts=[
    ('a', "**RV pressure overload → raised RV wall tension and RV dilatation.** Higher pressure and a larger radius both raise wall stress (Laplace)."),
    ('b', "**Raised wall tension → raised oxygen demand; meanwhile coronary perfusion falls → arrhythmia, RV ischaemia, injury, inflammation → lower contractility.** Demand rises as supply falls: high intramural pressure removes systolic coronary flow (RVF-05) and systemic hypotension lowers the driving pressure. Troponin rises in PE for this reason."),
    ('c', "**Lower contractility / RV dysfunction → lower RV output and altered systolic and diastolic interdependence.** The RV delivers less to the lungs and its dilatation pushes the septum into the LV (RVF-10)."),
    ('d', "**Both → lower LV preload → low cardiac output, hypotension, shock → further fall in coronary perfusion (the vicious circle); separately, TR/PR → RV volume overload → raised RA pressure and CVP → systemic congestion.** Forward failure and backward congestion run together: the gut, liver and kidneys get low flow and high venous pressure at once."),
    ('e', "**Both limbs converge on organ dysfunction or failure.** Breaking the loop means raising aortic pressure (noradrenaline) to restore the coronary gradient, lowering RV afterload, avoiding over-filling, and supporting contractility."),
  ],
  mimic=[
    ("Forward limb vs backward limb", "Forward: low LV preload, low output, hypotension; backward: TR, high CVP, venous congestion of liver, kidney and gut."),
  ],
  traps=[
    ("“In RV failure with hypotension, fluids first and vasopressors later”", "Hypotension removes RV coronary perfusion; restoring aortic pressure early is part of breaking the spiral, and fluid can worsen dilatation."),
  ],
  decode=[
    ("Why does systemic hypotension accelerate RV failure in massive PE? [pattern]", "It lowers RV coronary perfusion while wall stress and oxygen demand are high."),
  ],
  punch="A pressure-loaded RV dilates, needs more oxygen, gets less, weakens, shrinks the LV and lowers aortic pressure, which starves it further; the loop is broken by restoring coronary perfusion pressure and lowering afterload.",
)

L['RVF-16'] = dict(
  sub="RV failure → Causes → Acute, by mechanism",
  step=5,
  intro="Step 5 lists what pushes the RV over. Sorting causes by mechanism tells you what to fix: contractility, volume or afterload. Not asked directly.",
  parts=[
    ('a', "**Sepsis and LVAD support act by both reduced contractility and volume overload.** Sepsis depresses myocardium through cytokines and adds resuscitation fluid; it also raises PVR through hypoxia, acidosis and ARDS. An LVAD unloads the LV, which pulls the septum leftwards (lost septal contribution to RV contraction) while increasing venous return to the RV."),
    ('b', "**RV infarction, myocarditis and perioperative injury or ischaemia (post-cardiotomy) act by reduced contractility.** RV infarction comes with a proximal RCA occlusion and typically presents with hypotension, raised JVP and clear lungs."),
    ('c', "**Excess transfusion acts by volume overload.** Large volumes dilate the RV beyond its compliant range (RVF-09)."),
    ('d', "**Acidosis, hypoxia, PE, ARDS and positive-pressure ventilation act by pressure overload.** Hypoxia and acidosis cause pulmonary vasoconstriction; PE obstructs; ARDS adds vasoconstriction, microthrombi and remodelling; positive pressure compresses alveolar vessels when lung volume or PEEP is high, raising PVR. These are the causes the ICU can reverse."),
  ],
  mimic=[
    ("RV infarct vs massive PE", "Both give hypotension, high JVP and clear lungs; RV infarct shows inferior ST elevation and a normal PA pressure, PE shows a high PA pressure, RV/LV over 1 and McConnell’s sign."),
  ],
  traps=[
    ("“Positive-pressure ventilation affects RV preload only”", "It also raises RV afterload by compressing alveolar vessels; high PEEP and plateau pressures are a cause of acute RV failure."),
  ],
  decode=[
    ("Which acute causes act by pressure overload? [pattern]", "PE, ARDS, positive-pressure ventilation, hypoxia, acidosis."),
  ],
  punch="Acute RV failure is lost contractility (RV infarct, myocarditis, post-cardiotomy), extra volume (transfusion), both (sepsis, LVAD) or, most often in the ICU, raised afterload from PE, ARDS, the ventilator, hypoxia and acidosis.",
)

L['RVF-17'] = dict(
  sub="RV failure → Causes → Chronic, by mechanism",
  step=5,
  intro="Step 5, the chronic list. The two linked Marrow questions take two rows further: ARVC and its syndromes, and a patient with chronic RV strain who needs anticoagulation.",
  parts=[
    ('a', "**RV cardiomyopathy and ARVC act by reduced contractility.** ARVC is a desmosomal disease (plakophilin-2 is the commonest gene) with fibrofatty replacement of the RV free wall, presenting in young people with ventricular arrhythmia of LBBB morphology, syncope or sudden death. Naxos disease is ARVC with woolly hair and palmoplantar keratoderma (recessive, plakoglobin); Carvajal syndrome has the same skin and hair with a dilated, LV-dominant cardiomyopathy (desmoplakin)."),
    ('b', "**Ebstein anomaly spans reduced contractility and volume overload.** The tricuspid leaflets are displaced apically, so part of the RV is ‘atrialised’ (less functional muscle) and the valve regurgitates (volume)."),
    ('c', "**Left heart disease and single ventricle span volume and pressure overload.** Left heart disease raises pulmonary venous pressure (post-capillary PH, pressure load) and is often accompanied by functional TR (volume); it is the commonest cause of chronic RV failure."),
    ('d', "**PR, TGA and TR act by volume overload.** Regurgitant valves return blood to the RV each beat. In d-TGA after an atrial switch, and in congenitally corrected TGA, the RV is the systemic ventricle and its load is mainly pressure."),
    ('e', "**Pericardial disease, PAH, CTEPH, pulmonary stenosis, left-sided valve disease and restrictive cardiomyopathy act by pressure overload.** PAH and CTEPH raise PVR; PS obstructs outflow; left valve disease and restrictive cardiomyopathy raise left atrial pressure, which the RV must pump against. CTEPH is suspected when dyspnoea persists over 3 months after PE; the V/Q scan is the screening test."),
  ],
  mimic=[
    ("Naxos vs Carvajal", "Both woolly hair and palmoplantar keratoderma; Naxos is RV-dominant ARVC, Carvajal LV-dominant dilated cardiomyopathy."),
    ("ARVC vs RVOT tachycardia", "Both LBBB-morphology VT; ARVC has a structurally abnormal RV, epsilon waves and T inversion V1–V3; RVOT VT has a normal heart and a benign course."),
  ],
  traps=[
    ("“The ARVC syndrome with woolly hair and keratoderma is Carvajal”", "Carvajal (desmoplakin) gives the same hair and skin signs with a dilated, LV-dominant cardiomyopathy; the RV-dominant ARVC syndrome is Naxos (plakoglobin), Marrow’s key."),
    ("“Syncope, RV hypertrophy, TR murmur, raised troponin and CKD — wait for imaging”", "Marrow keys a heparin infusion: treat suspected thromboembolism while the work-up (V/Q rather than contrast CT in CKD) proceeds."),
  ],
  decode=[
    ("ARVC with sustained VT in a teenager: associated syndrome? [Marrow]", "Naxos syndrome."),
    ("Syncope, RVH, TR murmur, raised troponin, CKD: next step? [Marrow]", "Heparin infusion."),
  ],
  punch="Chronic RV failure is mostly pressure: left heart disease first, then PAH, CTEPH, stenoses and restrictive disease; the contractility causes are ARVC and RV cardiomyopathy, and the volume causes are regurgitant valves and shunts.",
)

L['RVF-18'] = dict(
  sub="RV failure → ICU settings → ARDS and RV-protective ventilation",
  step=5,
  intro="Step 5 in the commonest ICU setting. ARDS raises PVR, and the ventilator can add to it; the one linked question shows PEEP dropping the blood pressure because the RV could not cope.",
  parts=[
    ('a', "**RV dysfunction occurs in 22–55% of ARDS.** The lower figure is acute cor pulmonale (dilated RV with septal dyskinesia) on TOE under protective ventilation (Mekontso Dessap 2016: 22%); wider definitions of RV dysfunction give higher figures."),
    ('b', "**Survival is much higher in ARDS without RV dysfunction.** In the largest TOE cohort the excess mortality was concentrated in severe acute cor pulmonale (57% vs 42%); milder RV dysfunction carried less clear risk. RV dysfunction is a marker of a bad trajectory and a target, not only a bystander."),
    ('c', "**Predisposing: hypoxia, hypercarbia, respiratory acidosis, high PEEP, positive-pressure ventilation raising PVR.** Hypoxia and acidosis constrict pulmonary vessels; high PEEP and plateau pressure over-distend alveoli and compress the capillaries around them. The validated risk score uses pneumonia as the cause, driving pressure ≥18 cmH₂O, P/F under 150 and PaCO₂ ≥48 mmHg."),
    ('d', "**RV-protective ventilation: minimise plateau and driving pressures; lower PVR by improving PaO₂ and PaCO₂; prone positioning to unload the RV.** Prone positioning recruits dorsal lung at lower pressures, improves oxygenation and CO₂ clearance and reduces RV size; in severe ARDS with acute cor pulmonale it is used for the RV as much as for oxygenation. PEEP is titrated to recruit without over-distending: on echo, a rising RV/LV ratio or falling output after a PEEP increase means too much."),
  ],
  mimic=[
    ("PEEP-induced hypotension from RV afterload vs from low preload", "Afterload: RV dilates, septum flattens, CVP rises; preload: small, underfilled ventricles, falls with fluid."),
  ],
  traps=[
    ("“Raising PEEP is least likely to help in severe ARDS or obesity”", "Those are the patients who usually recruit, and in LV dysfunction PEEP lowers LV afterload and preload and may help; with RV dysfunction the extra PEEP raises PVR and drops output (DocT GT keys RV dysfunction)."),
    ("“Prone positioning is only an oxygenation manoeuvre”", "It also unloads the RV by lowering PVR and plateau pressure."),
  ],
  decode=[
    ("Severe ARDS, P/F 85, PEEP 5→10, MAP falls 65→45 — setting where more PEEP is least likely to help? [DocT GT]", "Right ventricular dysfunction."),
    ("Components of RV-protective ventilation [pattern]", "Limit plateau and driving pressure, correct PaO₂ and PaCO₂, prone positioning."),
  ],
  punch="ARDS loads the RV through hypoxia, hypercapnia, acidosis and high airway pressures; RV-protective ventilation limits plateau and driving pressure, corrects the gases and uses prone positioning, and a fall in pressure after more PEEP signals an RV that cannot take it.",
)

L['RVF-19'] = dict(
  sub="RV failure → ICU settings → After cardiac surgery",
  step=5,
  intro="Step 5 after cardiac surgery, where the RV is stunned and loaded at the same time. The one linked question asks about gas embolism, the anaesthetist’s version of the same problem.",
  parts=[
    ('a', "**Cardiopulmonary bypass → myocardial stunning.** The thin, anterior RV is the hardest chamber to protect: retrograde cardioplegia reaches it poorly because much of its venous drainage bypasses the coronary sinus, and it rewarms quickly because it lies uppermost in the open chest. Stunned RV muscle then meets a raised PVR."),
    ('b', "**Air embolism.** Air entering the coronaries goes preferentially to the RCA because its ostium is anterior (uppermost in the supine patient), causing acute RV ischaemia; air in the venous circulation lodges in the RVOT and pulmonary arteries."),
    ('c', "**Raised post-operative PVR.** Bypass triggers inflammation, protamine reactions, transfusion, hypoxia and atelectasis, all of which raise PVR."),
    ('d', "**LVAD implantation.** Unloading the LV shifts the septum leftwards and increases venous return to the RV; RV failure after LVAD occurs in a sizeable minority and may need temporary RV support."),
  ],
  mimic=[
    ("Venous gas embolism vs coronary air embolism", "Venous: air lock in the RVOT, high PA pressure, falling ETCO₂; coronary: RV ischaemia with inferior ST elevation after bypass."),
  ],
  traps=[
    ("“Left lateral head-down position (Durant) helps by improving venous return”", "It is meant to hold the gas in the right atrium and RV apex, away from the RV outflow tract, relieving the air lock (a postulated mechanism with little outcome evidence); aspirate through a central line (Marrow)."),
  ],
  decode=[
    ("CO₂ embolism during laparoscopic cholecystectomy: purpose of left lateral head-down position? [Marrow]", "Traps the embolus in the RV, away from the outflow tract."),
  ],
  punch="After cardiac surgery the RV is stunned by bypass, embolised by air, loaded by a raised PVR and destabilised by an LVAD; venous gas is managed by trapping it at the RV apex and aspirating it.",
)

L['RVF-20'] = dict(
  sub="RV failure → Pulmonary hypertension → Definition, group 1 and group 2",
  step=6,
  intro="Step 6 classifies the commonest chronic cause of RV pressure load. This is the most-asked card in the deck (seven questions): the haemodynamic definition, how a normal wedge pressure separates pre-capillary from post-capillary disease, and the young woman with Raynaud’s and right heart failure.",
  parts=[
    ('a', "**Pulmonary hypertension: MAP >25 mmHg (mean PA pressure).** ESC/ERS 2022 now defines PH as mPAP over 20 mmHg at rest on right heart catheterisation; 25 was the pre-2018 cut-off. The definition then splits on wedge pressure and PVR: pre-capillary PH (PAH, groups 1, 3, 4, some 5) = mPAP over 20, PAWP 15 or less, PVR over 2 WU; isolated post-capillary PH = PAWP over 15, PVR 2 WU or less; combined post- and pre-capillary PH = PAWP over 15 and PVR over 2. Exercise PH is an mPAP/cardiac output slope over 3 mmHg/L/min."),
    ('b', "**Group 1, pulmonary arterial hypertension: idiopathic; heritable (BMPR2, ALK-1, endoglin, unknown); drug and toxin induced; associated with connective tissue disease, HIV, portal hypertension, congenital heart disease, schistosomiasis, chronic haemolytic anaemia; pulmonary veno-occlusive disease / capillary haemangiomatosis; persistent PH of the newborn.** Group 1 is disease of the small pulmonary arteries themselves (intimal and medial proliferation, plexiform lesions), so the wedge is normal and PVR high. Systemic sclerosis is the classic associated disease: a young woman with Raynaud’s, exertional dyspnoea, a raised JVP, oedema and a loud P2 without orthopnoea or crackles has CTD-associated PAH. The 2022 list splits idiopathic PAH into vasoreactivity non-responders and acute responders, names methamphetamines and dasatinib as definite drug causes, renames PVOD/PCH ‘PAH with features of venous/capillary involvement’, and places chronic haemolytic anaemia in group 5. Exertional dyspnoea is the commonest symptom (the RV cannot raise output); fatigue, exertional angina and exertional syncope follow, with oedema late."),
    ('c', "**Group 2, PH due to left heart disease (post-capillary): LV systolic dysfunction, LV diastolic dysfunction, valvular disease, congenital/acquired left heart inflow or outflow obstruction, congenital cardiomyopathy.** A high left atrial pressure is transmitted backwards, so the wedge is over 15 mmHg. It is the commonest cause of PH overall. In 2022 wording: heart failure with preserved, mildly reduced or reduced EF, valvular disease, and congenital or acquired conditions causing post-capillary PH. A raised PCWP or LVEDP therefore excludes PAH."),
  ],
  table=dict(title="ESC/ERS 2022 haemodynamic definitions (right heart catheter, at rest)",
    head=["Category", "mPAP", "PAWP", "PVR"],
    rows=[["Pulmonary hypertension", "Over 20 mmHg", "—", "—"],
          ["Pre-capillary PH", "Over 20", "15 or less", "Over 2 WU"],
          ["Isolated post-capillary PH", "Over 20", "Over 15", "2 WU or less"],
          ["Combined post- and pre-capillary PH", "Over 20", "Over 15", "Over 2 WU"]]),
  mimic=[
    ("PAH (group 1) vs PH of left heart disease (group 2)", "PAWP 15 or less vs over 15; left heart disease gives orthopnoea, crackles and LA enlargement."),
    ("CTD-associated PAH vs ILD-associated PH (group 3)", "Both in systemic sclerosis; ILD gives crackles, restriction and fibrosis on CT; PAH has clear lungs and an isolated low DLCO."),
    ("PAH vs CTEPH", "CTEPH needs a thromboembolic history or risk (APS), mismatched perfusion defects on V/Q, and a normal wedge too."),
  ],
  traps=[
    ("“Young woman, Raynaud’s, JVD, oedema, loud P2 — left heart failure, ILD or CTEPH”", "Raynaud’s points to systemic sclerosis and group 1 PAH; no orthopnoea or crackles argues against left heart failure and ILD, and nothing suggests VTE (only 54% and 68% on two DocT GTs)."),
    ("“The RHC criterion for PAH is mPAP >25 mmHg” (DocT GT key)", "That is the pre-2022 threshold. ESC/ERS 2022: mPAP over 20, PAWP 15 or less, PVR over 2 WU. If over 20 is offered, choose it; if only over 25 appears alongside a PCWP over 25 or LVEDP over 15, choose over 25, because a high wedge or LVEDP means group 2."),
    ("“PVR under 3 WU fits PAH”", "PAH needs a raised PVR, now over 2 WU."),
    ("“A raised mPAP with a normal wedge means group 1 PAH”", "A normal wedge only makes it pre-capillary (groups 1, 3, 4 or 5); with antiphospholipid syndrome the likely cause is recurrent PE (CTEPH, group 4) (Marrow)."),
    ("“Syncope is the commonest symptom of PH”", "Exertional dyspnoea is; syncope is a late, high-risk sign."),
  ],
  decode=[
    ("Raynaud’s, exertional dyspnoea, JVD, oedema, loud P2 in a 42-year-old woman — diagnosis? [DocT GT ×4]", "Pulmonary arterial hypertension (54–91%)."),
    ("True statement on RHC in PAH: mPAP >25 / PCWP >25 / LVEDP >15 / PVR <3 [DocT GT]", "mPAP >25 (76%); today mPAP >20."),
    ("Most common symptom of PH [DocT GT]", "Exertional dyspnoea (76%)."),
    ("APS, JVD, oedema, mPAP 28, PCWP 11 — likely cause? [Marrow]", "Recurrent pulmonary embolism."),
  ],
  extra=[
    dict(q="How is Eisenmenger syndrome treated? [DocT GT]", a="With PAH-targeted therapy: bosentan has the trial evidence (BREATHE-5: better exercise capacity and haemodynamics without worse saturation) and ESC/ERS 2022 recommends it for symptomatic patients to improve exercise capacity (class I, level B), with combination therapy if there is no response; PDE-5 inhibitors are the alternative. Calcium-channel blockers lower SVR and increase the right-to-left shunt; beta-blockers and digoxin do not treat PAH (RVF-22)."),
  ],
  punch="PH is now mPAP over 20 mmHg; a wedge of 15 or less with a PVR over 2 WU makes it pre-capillary, and in a young woman with Raynaud’s and right heart failure that means group 1 PAH from systemic sclerosis, while a high wedge means left heart disease, group 2.",
)

L['RVF-21'] = dict(
  sub="RV failure → Pulmonary hypertension → Groups 3, 4 and 5",
  step=6,
  intro="Step 6 continued. Four questions hit this card, all on group 4: which kind of embolism causes chronic PH, which group a patient with old PE belongs to, and how CTEPH is treated.",
  parts=[
    ('a', "**Group 3, lung disease and/or hypoxia: COPD, ILD, obstructive and restrictive lung disease, sleep-disordered breathing, alveolar hypoventilation, chronic high-altitude exposure, developmental lung disease.** Hypoxic vasoconstriction and loss of the vascular bed raise PVR. PH is usually mild. ESC/ERS 2022 defines severe PH in lung disease by PVR over 5 WU (replacing the older pressure-based definition); it carries a worse prognosis and is referred to a PH centre. ESC 2022 groups sleep-disordered breathing with alveolar hypoventilation as ‘hypoventilation syndromes’."),
    ('b', "**Group 4, chronic thromboembolic PH: a complication of PE, large or proximal vessel disease, high pressure and clots, reduced compliance and luminal narrowing.** Emboli that fail to resolve organise into fibrotic material lining the pulmonary arteries; the unaffected vessels then remodel under high flow, so PVR rises in both. The classic source is multiple small, recurrent, often silent emboli, not one massive saddle embolus (which kills or lyses). CTEPH follows about 3% of PE survivors. ESC 2022 names group 4 ‘PH associated with pulmonary artery obstructions’: CTEPH plus other obstructions (sarcoma, other tumours, arteritis, congenital stenoses, hydatid). Diagnosis: symptoms after at least 3 months of anticoagulation, mismatched perfusion defects on V/Q (a normal V/Q excludes it), confirmed by CT/pulmonary angiography and RHC. Treatment: lifelong anticoagulation (VKA if APS); pulmonary endarterectomy if operable, the only potentially curative step; balloon pulmonary angioplasty if inoperable or residual; riociguat for inoperable or persistent PH."),
    ('c', "**Group 5, unclear and/or multifactorial: haematological (myeloproliferative disorders, splenectomy), systemic (vasculitis, sarcoidosis, PLCH, NF), metabolic (glycogen storage disease, thyroid disorders), congenital heart disease, cancer-related, renal failure on dialysis.** ESC 2022 group 5: haematological (chronic haemolytic anaemias, myeloproliferative disorders), systemic (sarcoidosis, PLCH, NF1), metabolic (glycogen storage, Gaucher), chronic renal failure with or without dialysis, pulmonary tumour thrombotic microangiopathy and fibrosing mediastinitis. Splenectomy is now a CTEPH risk factor, and vasculitis and thyroid disorders have left group 5. Congenital heart disease (‘complex CHD’ in group 5 in 2018) is no longer in group 5: ESC 2022 places it in group 1 (PAH associated with CHD, including Eisenmenger) and group 2 (congenital or acquired post-capillary conditions)."),
  ],
  mimic=[
    ("CTEPH (group 4) vs PAH (group 1)", "Both pre-capillary; CTEPH has a VTE history and mismatched V/Q defects and is treated by surgery first."),
    ("Group 3 PH vs PAH with incidental lung disease", "Group 3: usually mild PH matching the lung disease; severe PH (PVR over 5 WU) or PH out of keeping with the lung disease needs a PH centre."),
  ],
  traps=[
    ("“Massive (saddle) PE is the commonest embolic cause of chronic PH”", "It is multiple small recurrent emboli; air and fat emboli are acute events without chronic PH (51% on DocT QBank)."),
    ("“Clot ‘a long time ago’, large PA thrombus, severe PH — group 1”", "Chronic thromboembolism is group 4 (56%)."),
    ("“CTEPH, hypoxaemic, mPAP 40, anticoagulated — IV epoprostenol” (Marrow key)", "Disputed: the ESC 2022 ladder is anticoagulation → endarterectomy if operable → balloon angioplasty if not → riociguat as the first drug; epoprostenol is only for a critically ill patient. Choose endarterectomy if it is offered and the disease is operable; choose riociguat if it is inoperable."),
  ],
  decode=[
    ("Which form of PE is the commonest cause of secondary PH? [DocT QBank]", "Multiple small recurrent emboli (51%)."),
    ("Old PE treated for a few months, dilated right heart, severe TR, PA thrombus, severe PH — WHO group? [DocT GT]", "Group 4 (56%)."),
    ("CTEPH, hypoxaemic, mPAP 40, anticoagulated — next best step? [Marrow ×2]", "Keyed IV epoprostenol; guideline answer PEA if operable, otherwise BPA/riociguat."),
  ],
  punch="Group 3 is lung and hypoxia, group 4 is obstructed pulmonary arteries, mostly CTEPH from small recurrent emboli and treated by endarterectomy first, and group 5 is the miscellaneous rest; a normal V/Q scan excludes CTEPH.",
)

L['RVF-22'] = dict(
  sub="RV failure → Causes → Congenital heart disease and Eisenmenger",
  step=5,
  intro="Step 5’s congenital causes, with the sequence that ends in Eisenmenger syndrome. The linked question asks how Eisenmenger is treated.",
  parts=[
    ('a', "**Volume overload: septal defects (ASD, VSD) and left-to-right shunts.** An ASD loads the RV with volume directly; a VSD or PDA mainly loads the pulmonary circulation and LV, and then the RV with pressure as PVR rises."),
    ('b', "**RA and RV → raised PVR → pulmonary vascular remodelling → PVR exceeds SVR → the shunt becomes right-to-left → Eisenmenger syndrome.** High flow and pressure damage the pulmonary arterioles (intimal proliferation, plexiform lesions), so PVR climbs until it exceeds SVR; the shunt reverses and the patient becomes cyanosed with secondary erythrocytosis. At that point closing the defect is contraindicated, because the shunt is now the RV’s pressure vent."),
    ('c', "**Two pressure-overload causes: pulmonary stenosis and post-TOF correction.** Pulmonary stenosis loads the RV directly; the repaired outflow tract in TOF can leave residual RVOT or branch PA obstruction. The commonest late lesion after tetralogy repair, though, is pulmonary regurgitation, which is volume overload."),
  ],
  mimic=[
    ("Eisenmenger vs PH from a small defect", "Eisenmenger follows a large unrestricted shunt; PH with a small defect is coincidental PAH, managed like group 1."),
  ],
  traps=[
    ("“Eisenmenger syndrome: start a calcium-channel blocker, beta-blocker or digoxin”", "CCBs lower SVR and increase the right-to-left shunt; beta-blockers and digoxin do not treat PAH. Bosentan has the evidence (BREATHE-5) and the ESC 2022 class I recommendation for symptomatic patients (75% right on DocT GT)."),
    ("“Close the defect once Eisenmenger develops”", "Closure removes the RV’s outlet and is contraindicated once PVR exceeds SVR."),
  ],
  decode=[
    ("PAH from CHD, now Eisenmenger syndrome — most appropriate treatment? [DocT GT]", "Bosentan (75%)."),
  ],
  punch="A large left-to-right shunt remodels the pulmonary vessels until PVR exceeds SVR and the shunt reverses; Eisenmenger is then treated with bosentan, never with calcium-channel blockers or closure.",
)

FLAGS = {
  'RVF-20': "a: ‘MAP >25 mmHg’ is outdated (and should read mean PA pressure); ESC/ERS 2022 defines PH as mPAP >20, pre-capillary PH with PAWP ≤15 and PVR >2 WU (card-layer fix, confirmed). DocT GT keys mPAP >25 for PAH: right as the only true option, wrong threshold. b/c: the group 1 and 2 lists are the older (Dana Point 2008 / Nice 2013) wording: chronic haemolytic anaemia has been in group 5 since 2013; ESC 2022 adds vasoreactivity responders/non-responders, names methamphetamine and dasatinib, renames PVOD/PCH, and lists group 2 as HF by EF, valvular disease and congenital/acquired post-capillary conditions.",
  'RVF-21': "b: ESC 2022 names group 4 ‘PH associated with pulmonary artery obstructions’ (CTEPH plus sarcoma, tumours, arteritis, congenital stenoses, parasites); ‘high blood pressure, blood clots’ is not classification wording. c: splenectomy, vasculitis and thyroid disorders are no longer group 5 causes (splenectomy and high-dose thyroxine are CTEPH risk factors); 2022 group 5 is haematological (incl. chronic haemolytic anaemia), systemic, metabolic (incl. Gaucher), chronic renal failure ± dialysis, pulmonary tumour thrombotic microangiopathy and fibrosing mediastinitis. Congenital heart disease is no longer in group 5 (it sits in group 1, 1.4.4, and group 2, 2.3). Marrow’s ‘IV epoprostenol’ key for a stable anticoagulated CTEPH patient conflicts with the ESC 2022 ladder (PEA → BPA → riociguat).",
  'RVF-22': "Watch line: post-TOF correction is not purely pressure overload; the commonest late lesion after repair is pulmonary regurgitation (volume overload), with residual RVOT or branch PA obstruction as the pressure cause. The card’s grouping is kept and the explanation says both.",
  'RVF-17': "d: TGA under ‘volume overload’ is questionable; in d-TGA after an atrial switch and in congenitally corrected TGA the RV is the systemic ventricle and its load is mainly pressure. Explained, card text kept.",
  'RVF-07': "a: RVEF lower limit 40% and wall ≤3 mm are MRI-type normal ranges; ASE 2015 echo cut-offs are 3D RVEF <45% abnormal and RV wall >5 mm = hypertrophy, so the watch line’s ‘RVEF 45% is normal’ sits on the lower limit. Not wrong, but say which method.",
  'RVF-18': "b: ‘survival much higher without RV dysfunction’ is stronger than the largest TOE cohort (Mekontso Dessap 2016): overall mortality did not differ with acute cor pulmonale; it was higher only with severe ACP (57% vs 42%).",
  'RVF-02': "a: the 3–9% admission range is a pooled figure from several European registries (OFICA, ESC-HF pilot, RO-AHFS, EHFS II), with 5–17% in-hospital mortality from EHFS II; attributing it to the AHEAD registry alone could not be confirmed. Figures kept; explanation says where they come from.",
  'RVF-05': "a: the 80/20 RCA/left split reflects coronary dominance; the anterior RV wall and moderator band also receive LAD branches in most people. Card kept; added in the explanation.",
}
