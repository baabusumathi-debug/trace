# HY2 top-up cards — Explain v3 ("Learn" depth), same fields and voice as hy2_learn.py.
# Fields: sub, step (index into hy2_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions: the top-up's own src list (DocT GT / Marrow) plus qpack/HY2.md. Checked 19 Nov 2026 against AHA 2017 hypertension (hypertensive emergency), AHA/ASA 2019 stroke,
# AHA 2022 ICH, ACC/AHA 2022 aortic disease.
# The fundus-grade / BP-target qa card has its own id, T_6ad11458b (coordinator fix, 19 Nov 2026).
T = {}

T['T_6ad11458'] = dict(
  sub="Cardiology → Vascular emergencies → Hypertensive emergency",
  step=4,
  intro="Step 4 deals with emergencies where the cardiovascular drugs are chosen by the organ at risk, and the hypertensive emergency (asked 15 times in the DocT tests) is the clearest case. The number alone does not make the emergency; acute organ damage does, and that also decides how fast and with what the pressure comes down.",
  parts=[
    ('a', "**BP ≥180/120 + acute organ damage (encephalopathy, ICH/stroke, ACS, pulmonary oedema, dissection, AKI/TMA, eclampsia) = emergency → ICU + IV titratable drug; no organ damage = urgency → oral drugs over 24–48 h.** What separates the two is new organ injury, because that is what the pressure is doing now; a high reading without injury carries no short-term benefit from rapid lowering and the risk of overshoot."),
    ('b', "**Lower MAP by ≤25% in the 1st hour → 160/100–110 over the next 2–6 h → normal over 24–48 h (autoregulation is reset upward; fast drops cause watershed ischaemia).** In chronic hypertension the cerebral and renal autoregulation curves shift to the right, so a ‘normal’ pressure is below the lower limit for that patient and flow falls; stroke, blindness and renal infarction follow over-rapid correction. The 2017 AHA guideline gives a fall in SBP of no more than 25% in the first hour."),
    ('c', "**Drugs by organ: encephalopathy/stroke → labetalol, nicardipine or clevidipine; acute pulmonary oedema → IV nitroglycerin + loop diuretic + NIV (avoid labetalol/β-blockers in decompensated HF); renal failure → fenoldopam, nicardipine or clevidipine (no prolonged nitroprusside: cyanide/thiocyanate); avoid nitroprusside with raised ICP; oral drugs are too slow.** The drug is chosen for what it does to the injured organ: titratable IV agents allow precise control; nitroglycerin lowers preload in pulmonary oedema; nitroprusside dilates cerebral vessels (raising ICP) and accumulates cyanide and, in renal failure, thiocyanate."),
    ('d', "**Go faster: dissection SBP <120 and HR <60 within 20 min (β-blocker first); severe pre-eclampsia SBP <160 within 1 h; phaeochromocytoma α before β. Ischaemic stroke: treat only if >185/110 (before lysis) or >220/120.** In dissection the force driving the tear (dP/dt) matters, so the heart rate is controlled first with an IV β-blocker (esmolol, labetalol) and only then a vasodilator, to avoid reflex tachycardia. In phaeochromocytoma an unopposed β-blocker leaves α-vasoconstriction unchecked. In ischaemic stroke the penumbra depends on pressure: lower only for lysis (<185/110, kept <180/105 after) or above 220/120 (by about 15% in 24 h). AHA 2022 ICH guidance targets SBP about 140, avoiding falls below 130."),
    ('e', "**Clonidine withdrawal: restart clonidine; if organ damage, phentolamine or labetalol — never an unopposed pure β-blocker.** Stopping clonidine releases a catecholamine surge, like a phaeochromocytoma; a pure β-blocker would leave α-vasoconstriction unopposed and push the pressure higher."),
    ('f', "**Why it spirals: an abrupt BP rise injures the endothelium (lost NO, fibrinoid necrosis) and activates RAAS → more vasoconstriction; malignant hypertension’s pressure natriuresis and RAAS surge cause volume depletion, hypokalaemia, polyuria and weight loss.** These patients are often volume-depleted, which is why a vasodilator can drop the pressure abruptly and why diuretics are avoided unless there is pulmonary oedema."),
  ],
  mimic=[
    ("Hypertensive emergency vs urgency", "Emergency: acute organ damage, IV drug in ICU, ≤25% in the first hour. Urgency: no damage, oral drugs over 24–48 h."),
    ("Dissection vs other emergencies", "Dissection: SBP <120 and HR <60 within about 20 minutes, β-blocker first. Others: gradual reduction."),
  ],
  traps=[
    ("“Lower the BP to normal within the first hour”", "No more than 25% in the first hour; normal over 24–48 h. Exceptions are dissection, severe pre-eclampsia and phaeochromocytoma."),
    ("“Nitroprusside for hypertensive encephalopathy with raised ICP” or for days in renal failure", "Nitroprusside raises ICP and accumulates cyanide/thiocyanate; nicardipine, clevidipine or labetalol instead."),
    ("“Labetalol for hypertensive acute pulmonary oedema”", "IV nitroglycerin, loop diuretic and NIV; β-blockers worsen decompensated HF."),
    ("“Esmolol alone” for clonidine withdrawal or phaeochromocytoma crisis", "Never an unopposed β-blocker: α-blockade first (phentolamine) or labetalol."),
  ],
  decode=[
    ("[pattern; topic asked 15× in DocT GT] BP 220/130 with headache, confusion or papilloedema — target in the first hour?", "Lower MAP by no more than 25%, then 160/100–110 over 2–6 h."),
    ("[pattern] Hypertensive emergency with acute aortic dissection — target and first drug?", "SBP <120 and HR <60 within about 20 min; IV β-blocker first."),
    ("[pattern] Hypertensive pulmonary oedema — drug?", "IV nitroglycerin with a loop diuretic and NIV."),
    ("[pattern] Ischaemic stroke, candidate for lysis — BP threshold?", "Treat if above 185/110; keep below 180/105 after lysis."),
  ],
  punch="A hypertensive emergency is high BP with acute organ damage: lower by no more than 25% in the first hour with a titratable IV drug chosen for the organ, except dissection, pre-eclampsia and phaeochromocytoma, which need faster or different control.",
)

T['T_74c38a9d'] = dict(
  sub="Cardiology → Arrest → First recorded rhythm",
  step=3,
  intro="Step 3 starts at the collapse, and the first rhythm recorded decides whether a shock can help. Which rhythm is ‘commonest’ depends on who has arrested and how quickly the monitor goes on.",
  parts=[
    ('a', "**Overall out-of-hospital arrest: asystole/PEA now outnumber VF (VF ~20–25% and falling).** VF degenerates into asystole within minutes if untreated, so a late first recording finds asystole; fewer arrests are also caused by acute coronary occlusion now, and more by non-cardiac causes (respiratory, overdose)."),
    ('b', "**Witnessed collapse in the young or athletes: VF/VT is classic (HCM, channelopathy, commotio cordis) — the earlier the rhythm is recorded, the likelier VF.** A sudden arrhythmic death in a structurally abnormal or electrically unstable heart starts as VT or VF; a bystander-witnessed arrest with an AED on early catches it before it decays."),
    ('c', "**Late sudden death weeks after MI: asystole ~50%, PEA ~20% as first rhythm (Tintinalli).** Late after infarction, deaths are often from pump failure, re-infarction or bradyarrhythmia rather than primary VF, which is why early ICDs after MI did not lower mortality (CAR-10)."),
  ],
  mimic=[
    ("Commonest first rhythm overall vs in the young", "Overall OHCA: non-shockable (asystole/PEA). Young, witnessed, early AED: VF."),
  ],
  traps=[
    ("“VF is the commonest first rhythm in all cardiac arrest”", "It was in older series and remains so in witnessed arrests with early monitoring; in OHCA overall, asystole and PEA now outnumber it."),
  ],
  decode=[
    ("[Marrow QB22] Commonest first recorded rhythm in sudden cardiac arrest?", "Depends on the stem: OHCA overall → asystole/PEA; witnessed collapse in a young person → VF."),
    ("[Marrow QB22] First rhythm in sudden death weeks after MI?", "Asystole (about half), then PEA."),
  ],
  punch="In out-of-hospital arrest overall the first rhythm is now usually asystole or PEA, with VF in only about a fifth; a witnessed collapse in a young person, recorded early, is classically VF.",
)

T['T_6ad11458b'] = dict(
  sub="Cardiology → Vascular emergencies → Hypertensive emergency: fundus and targets",
  step=4,
  intro="This short companion to the hypertensive-emergency card covers the two things it is asked on. The fundus shows whether the pressure has already damaged small vessels, and the targets say how fast to bring it down once there is organ damage.",
  parts=[
    ('a', "**Keith–Wagener–Barker: I narrowing; II AV nipping; III haemorrhages, exudates, cotton-wool; IV = III + papilloedema (malignant).** Grades I–II are chronic arteriolar thickening. Grade III is acute endothelial injury: haemorrhages, leaking exudates, and cotton-wool spots, which are nerve-fibre infarcts. Grade IV adds disc swelling from raised pressure and ischaemia. Papilloedema with this picture is the classic sign of malignant hypertension and counts as organ damage."),
    ('b', "**Lower MAP 10–20% (≤25%) in the first hour, then to 160/100 over 2–6 h, normal over 24–48 h.** Chronic hypertension shifts cerebral and renal autoregulation to higher pressures. A fast return to ‘normal’ pressure therefore drops below that patient’s lower limit and causes watershed ischaemia (stroke, blindness, renal infarction)."),
    ('c', "**Exceptions: aortic dissection (SBP <120 in 20 min), pre-eclampsia (<160/110, aim 140–150/90–100), ischaemic stroke and ICH have their own targets.** In dissection the shear force propagating the tear is the danger, so the heart rate is controlled first with an IV β-blocker and the SBP is brought down fast. In pre-eclampsia placental flow depends on pressure, so the aim stops at about 140–150/90–100. In ischaemic stroke, BP is lowered only above 185/110 before lysis or above 220/120 otherwise, to protect the penumbra; in ICH the SBP target is about 140, avoiding falls below 130 (AHA 2022)."),
  ],
  mimic=[
    ("Grade III vs grade IV retinopathy", "Both have haemorrhages, exudates and cotton-wool spots; only grade IV has papilloedema (malignant hypertension)."),
  ],
  traps=[
    ("“Bring the BP to normal within the first hour”", "No more than 25% in the first hour; dissection is the main exception that is lowered fast."),
    ("“Grade IV = haemorrhages and exudates”", "That is grade III; grade IV needs papilloedema."),
  ],
  decode=[
    ("[pattern; DocT and Marrow] Hypertensive emergency with papilloedema, no stroke or dissection — fundus grade and first-hour target?", "Grade IV (malignant); lower MAP by 10–20%, at most 25%, in the first hour."),
  ],
  punch="Papilloedema on top of haemorrhages and exudates is grade IV, malignant hypertension. Lower the MAP by no more than 25% in the first hour, except in dissection, pre-eclampsia, ischaemic stroke and ICH, which have their own targets.",
)

FLAGS = {}
