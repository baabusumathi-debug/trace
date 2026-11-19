# CVS09 — Explain v3 ("Learn" depth): aortic dissection and acute aortic syndromes — epidemiology, risk factors, histology, mechanism, malperfusion, propagation (dP/dt), true vs false
# lumen, IRAD time classes, DeBakey, Stanford, TEM, management by type, complicated dissection, clinical signs, the ACS trap, bedside tests, imaging, stabilisation targets, drug sequence and
# doses, type A repair, DHCA, cerebral perfusion, tamponade, post-operative care, type B (medical vs TEVAR), spinal cord protection, complications.
# No mnemonics or hooks. Driven by qpack/CVS09.md (28 question links across 13 cards): AD-21 (second-line doses, nitroprusside cyanide and nitroglycerin) asked 7 times, AD-19 (drug sequence) 5,
# AD-17 (imaging) 4, AD-09 (DeBakey) 2; AD-02, 06, 07, 10, 12, 14, 16, 18, 20, 23 once each. AD-01, 03, 04, 05, 08, 11, 13, 15, 22, 24–29 have no linked question and get short explanations
# with [pattern] decode items.
# No `fix` entries exist for CVS09 in trace/test/data/qbank.json (checked 19 Nov 2026). The card layer (cvs_cardlayer.json: lines and cross notes for AD-02, 07, 09, 16, 17, 21, 23) was read and
# the explanations agree with it.
# Checked online on 19 Nov 2026:
#  - 2024 ESC peripheral arterial and aortic diseases (Mazzolai, Eur Heart J 2024;45:3538, full text via ORBi): classic AAD 80–90% of AAS, incidence 2.6–3.5/100 000 person-years, ~65% male,
#    mean ~63 years, morning peak 8–9 am, winter (January) peak; time classes hyperacute <24 h, acute 1–14 days, subacute 15–90 days, chronic >90 days; non-A non-B = arch-limited or retrograde
#    from the descending aorta; TEM (type, entry, malperfusion M0–M3); ~6.4% painless; D-dimer <500 ng/mL makes AAD unlikely; CXR and ECG to exclude other causes, must not delay imaging;
#    ECG-gated contrast CT neck to pelvis first line (I, C; sensitivity 100%, specificity 98%); TOE to guide peri-operative management (I, C) and in unstable patients; anti-impulse therapy
#    SBP <120 mmHg and HR ≤60 b.p.m. (I, B); adequate pain control (I, C); non-DHP CCB if beta-blockers contraindicated (IIa, B); switch to oral beta-blocker after 24 h; type A medical mortality
#    ~50% in 48 h (1–2%/h), perioperative 17–25%; malperfusion in ~30%, mesenteric malperfusion mortality 65–95%; aortic valve resuspension over replacement when leaflets are normal; root
#    replacement for root destruction, root aneurysm or genetic disorder (I, B); open distal anastomosis (I, B); immediate surgery for TAAD with malperfusion (I, B); complicated TBAD (rupture,
#    malperfusion, rapid expansion …) → TEVAR first line (I, B); uncomplicated TBAD with high-risk features → TEVAR in the subacute phase, 14–90 days (IIa, B); higher MAP for spinal ischaemia.
#  - 2022 ACC/AHA aortic disease guideline (via PMC12208080 summary): SBP <120 mmHg or the lowest BP that keeps end-organ perfusion; HR 60–80 b.p.m.
#  - IRAD (Hagan, JAMA 2000, n 464; full text): mean age 63.1, 65.3% male; abrupt onset 84.8%, ‘tearing or ripping’ only 50.6% (sharp commoner), back pain 53.2%, syncope 9.4%; CXR normal 12.4%,
#    widened mediastinum 61.6%, abnormal aortic contour 49.6%; ECG normal 31.3%, nonspecific ST-T 41.4%, ischaemia 15.1%, new Q/ST 3.2%; pulse deficit 15.1%; AR murmur 31.6%; in-hospital
#    mortality type A surgical 26% vs medical 58%, type B medical 10.7% vs surgical 31.4%.
#  - ASRA 2018 (OpenAnesthesia summary): dabigatran 72 h (CrCl ≥80), 96 h (50–79), 120 h (30–49), avoid <30; rivaroxaban, apixaban 72 h; clopidogrel 5–7 days; aspirin continued.
#  - CSF drainage (Endovascular Today 2020 protocol review): CSF pressure usually 8–12 mmHg, drain no more than 15–20 mL/h, MAP >80 after deployment, >100 if deficit, Hb >10 g/dL.
# Second review, 19 Nov 2026: ACC/AHA 2022 AAS table (PMC9860464 T88): SBP <120 or lowest BP that keeps end-organ perfusion and HR 60–80 (1, C-LD); IV beta-blocker first (1, B-NR);
#    IV non-DHP CCB if beta-blockers contraindicated (2a, B-NR); pain control (1, C-EO). ESC 2024 text (OUP full text): labetalol usual first choice, esmolol an option; complicated TBAD list
#    includes refractory pain and uncontrolled hypertension; emergency pericardial puncture only as a temporary life-saving measure. Booher 2013 IRAD time classes confirmed (abstract).
#    Left renal artery usually from the false lumen (Radiopaedia). ESC recommendation-table classes not visible online; kept as the first writer read them.
# From standard references without a fresh check (confident unless said): Booher 2013 IRAD time classes (hyperacute <24 h, acute 2–7 d, subacute 8–30 d, chronic >30 d); Sievers 2020 TEM details
# (E0–E3 by entry zone, M1 coronary, M2 supra-aortic, M3 spinal/visceral/renal/limb, +/− for clinical signs); Yan 2013 international consensus on hypothermia grades for circulatory arrest;
# drug-label doses for esmolol, labetalol, metoprolol, diltiazem, nicardipine, nitroprusside and nitroglycerin; nitroprusside chemistry (five cyanide groups per molecule, rhodanese and thiosulfate);
# DeBakey IIIa/IIIb; echo criteria for true and false lumens; the calcium sign (>5 mm, the card layer’s figure); left renal artery from the false lumen (commonly cited, not re-checked).

SPINE = [
  ("A weak media meets pressure", "Dissection happens when a medial layer weakened by age, hypertension or a connective-tissue disorder gives way under years of high pressure, most often in older hypertensive men."),
  ("The false lumen does the damage", "Blood entering through an intimal tear splits the outer media, and the pressurised false lumen squeezes the true lumen and its branches, so every complication is either rupture outward or malperfusion inward, driven by dP/dt."),
  ("Naming it by site and time", "Whether the ascending aorta is involved (Stanford A or B, DeBakey I–III, TEM) and how long since onset decide the risk and the treatment, more than anything else."),
  ("Recognising it, then imaging", "Sudden severe pain with a pulse or pressure difference, a new AR murmur or a widened mediastinum points to it, ACS is the commonest misdiagnosis, and an ECG-gated CT of the whole aorta confirms it when the patient is stable."),
  ("Anti-impulse therapy first", "Before any vasodilator, an IV beta-blocker brings the heart rate to about 60 and the systolic pressure below 120, because slowing the heart is what lowers dP/dt and stops the tear propagating."),
  ("Repair by type, protect the organs", "Type A goes to open surgery, uncomplicated type B stays medical and complicated type B gets TEVAR, and the brain, spinal cord, gut and kidneys are protected around the repair."),
]

PRIMER = "The aortic wall has three layers: the intima facing the blood, the thick elastic media that gives the aorta its strength and recoil, and the adventitia outside. The aorta is divided at the left subclavian artery into a proximal part (ascending aorta and arch) and a distal part (descending thoracic and abdominal aorta), and almost every classification of dissection turns on which side of that line the tear lies. The force that splits the wall is not the mean pressure alone but how steeply pressure rises with each beat (dP/dt), which depends on contractility and heart rate. Acute aortic syndrome covers classic dissection, intramural haematoma and penetrating ulcer; this deck is mostly about classic dissection."

L = {}

L['AD-01'] = dict(
  sub="Cardiology → Aortic dissection → Epidemiology",
  step=1,
  intro="Step 1 is who tears. The typical patient is an older hypertensive man, and the timing follows the body’s own pressure peaks. There is no linked question; the card is the profile behind every vignette in this deck.",
  parts=[
    ('a', "**Males, 5th to 7th decades.** In IRAD about 65% are men and the mean age is about 63; younger patients (under 40) point to Marfan syndrome, a bicuspid valve, pregnancy or cocaine."),
    ('b', "**Higher during the daytime, peak 8 to 10 am.** Blood pressure, heart rate and catecholamines surge after waking, which raises wall stress at the time a weak media is most likely to give way (ESC 2024 puts the peak at 8–9 am)."),
    ('c', "**Most common in winter.** Cold raises sympathetic tone and blood pressure; ESC 2024 notes a January peak in the Northern Hemisphere."),
    ('d', "**Ascending aorta involvement.** Untreated type A dissection kills about 1–2% per hour in the first 48 hours through rupture into the pericardium, coronary occlusion and acute aortic regurgitation (AD-12)."),
  ],
  mimic=[
    ("Dissection vs ACS in a hypertensive man in the morning", "Both peak in the morning in the same patient; pain that is maximal at onset and moves to the back, with a pulse deficit, points to dissection (AD-15)."),
  ],
  traps=[
    ("“Dissection is a disease of young men with Marfan syndrome”", "Most patients are hypertensive men in their 60s; Marfan explains the minority who are young."),
  ],
  decode=[
    ("Which segment carries the highest mortality? [pattern]", "Ascending aorta (type A)."),
    ("Circadian or seasonal peak of dissection [pattern]", "Morning (about 8–10 am) and winter."),
  ],
  punch="Dissection strikes older hypertensive men, in the morning and in winter, when pressure surges; involvement of the ascending aorta is what kills fastest.",
)

L['AD-02'] = dict(
  sub="Cardiology → Aortic dissection → Risk factors",
  step=1,
  intro="Step 1 continues with what weakens the wall. Two kinds of factor combine: things that raise the stress on the media (hypertension above all) and things that make the media weaker (connective-tissue disease, age). The one real question asks what Marfan patients die of.",
  parts=[
    ('a', "**Hypertension: the most common predisposing factor.** Present in about three quarters of patients. Years of high pressure raise wall tension (Laplace) and damage the medial vasa vasorum, so the media degenerates."),
    ('b', "**Marfan syndrome, Ehlers-Danlos syndrome.** Marfan (fibrillin-1) and vascular Ehlers-Danlos (type III collagen) build a structurally weak media; dissection or rupture of the aorta is the leading cause of death in Marfan syndrome. Mitral valve prolapse is commoner in Marfan but rarely fatal."),
    ('c', "**Atherosclerosis (changes vessel-wall structure), hyperlipidaemia, gene mutation, infectious disease, smoking.** Atherosclerosis causes penetrating ulcers more than classic dissection; genetic aortopathies (Loeys-Dietz, familial thoracic aortic disease) and aortitis weaken the wall directly."),
    ('d', "**Elderly men: males, 5th to 7th decades.** Age itself thins and fragments the elastic media (AD-03)."),
  ],
  mimic=[
    ("Marfan: dissection vs mitral valve prolapse", "MVP is the commonest cardiac finding; aortic dissection or rupture is the commonest cause of death."),
  ],
  traps=[
    ("“Mitral valve prolapse or heart failure is the commonest cause of death in Marfan”", "MVP is commoner but far less lethal; aortic dissection or rupture kills most Marfan patients, which is why their aortic root is replaced early."),
  ],
  decode=[
    ("Most common cause of death in Marfan syndrome [Marrow]", "Rupture of aortic dissection."),
    ("Most common predisposing factor for dissection [pattern]", "Hypertension."),
  ],
  punch="Hypertension is the commonest cause because it loads the media for years; connective-tissue disorders make the media weak from birth, and in Marfan the aorta, not the mitral valve, is what kills.",
)

L['AD-03'] = dict(
  sub="Cardiology → Aortic dissection → Histology",
  step=1,
  intro="Step 1 ends at the microscope: the common pathway of every risk factor is a media that has lost its elastic structure. Not asked; a short card.",
  parts=[
    ('a', "**Cystic medial necrosis.** Pools of mucoid (proteoglycan) material replace smooth muscle cells; despite the name there are no true cysts and no necrosis of the classic kind. It is the classic lesion of Marfan syndrome but also appears with age and hypertension."),
    ('b', "**Elastin fragmentation.** Broken elastic lamellae mean the media can no longer spread the stress of each beat, so it splits along a plane."),
    ('c', "**Fibrosis.** Scar replaces elastic tissue, making the wall stiff rather than strong."),
    ('d', "**Medionecrosis.** Loss of smooth muscle cells in the media, often from vasa vasorum ischaemia in long-standing hypertension."),
  ],
  mimic=[
    ("Medial degeneration vs atherosclerosis", "Dissection starts in a degenerate media; atherosclerosis is an intimal disease that causes penetrating ulcers and aneurysms."),
  ],
  traps=[
    ("“Cystic medial necrosis means cysts in the aortic wall”", "It is mucoid degeneration with loss of elastic fibres and smooth muscle; there are no true cysts."),
  ],
  decode=[
    ("Characteristic histology of the aortic wall in Marfan/dissection [pattern]", "Cystic medial necrosis with elastin fragmentation."),
  ],
  punch="Every risk factor ends in the same media: fragmented elastin and lost smooth muscle (cystic medial necrosis), which splits instead of stretching.",
)

L['AD-04'] = dict(
  sub="Cardiology → Aortic dissection → Mechanism",
  step=2,
  intro="Step 2 begins with the tear itself. Once blood enters the wall, the false lumen it creates is what causes every later complication. Not asked directly, but each complication card builds on this sequence.",
  parts=[
    ('a', "**Tear in the intima.** Usually in the right lateral wall of the ascending aorta a few centimetres above the valve, or just beyond the left subclavian, where the wall stress is highest."),
    ('b', "**Blood dissects through the media, creating a false lumen.** Pulsatile flow drives a column of blood along the weak plane, antegrade and sometimes retrograde."),
    ('c', "**Outer one-third of the media, where the vasa vasorum run.** The plane lies in the outer media, so the outer wall of the false lumen is thin; that is why the false lumen can rupture outward into the pericardium, pleura or mediastinum. A bleed from the vasa vasorum without an intimal tear is an intramural haematoma."),
    ('d', "**Double-barrelled aorta: a true lumen and a false lumen.** The intimal flap that separates them is what CT and echo look for (AD-17)."),
    ('e', "**False lumen compresses the true lumen → impaired flow → malperfusion syndrome.** The false lumen often carries higher pressure, so it bulges into the true lumen (dynamic obstruction) or extends into a branch and occludes it (static obstruction) (AD-05)."),
  ],
  mimic=[
    ("Classic dissection vs intramural haematoma", "Dissection has an intimal tear and a flap with flow in two lumens; IMH is crescentic wall thickening with no flap and no flow."),
  ],
  traps=[
    ("“The false lumen lies between intima and media”", "The plane is within the media, in its outer third."),
  ],
  decode=[
    ("Layer in which the cleavage plane forms [pattern]", "The media (outer third)."),
  ],
  punch="An intimal tear lets blood split the outer media; the false lumen then either ruptures outward through its thin wall or squeezes the true lumen and its branches, and that is the whole disease.",
)

L['AD-05'] = dict(
  sub="Cardiology → Aortic dissection → Malperfusion",
  step=2,
  intro="Step 2: when the false lumen compresses or extends into a branch, the organ supplied by that branch fails, and the presentation follows the branch. Not asked directly, but malperfusion turns a dissection into a ‘complicated’ one (AD-13) and drives the GT pairing question on AD-09.",
  parts=[
    ('a', "**Coronary: MI or acute coronary syndrome.** When a coronary is involved it is usually the right ostium, giving an inferior ST-elevation pattern (AD-15). Only type A can do this."),
    ('b', "**Cerebral: stroke or stroke-like symptoms.** Extension into the innominate or left carotid; again a type A (or arch) feature."),
    ('c', "**Spinal cord: paraplegia or paraparesis.** Intercostal arteries arising from the false lumen lose flow; the artery of Adamkiewicz (T8–T12) is the critical one (AD-28)."),
    ('d', "**Renal: oliguria and acute kidney injury.** The left renal artery often arises from the false lumen (AD-07)."),
    ('e', "**Visceral: gut ischaemia, with abdominal pain and lactic acidosis.** Coeliac or superior mesenteric involvement; ESC 2024 gives mesenteric malperfusion a mortality of 65–95%."),
    ('f', "**Limb: numbness, weakness or pain.** Iliac or subclavian compression gives a pulse deficit and an inter-arm or arm-leg pressure difference."),
  ],
  mimic=[
    ("Coronary or cerebral vs visceral or renal malperfusion", "Coronary and cerebral need the ascending aorta or arch (type A); visceral, renal and leg need the descending or abdominal aorta (DeBakey I or III)."),
  ],
  traps=[
    ("“Mesenteric malperfusion causes early abdominal tenderness”", "Pain out of proportion to a soft abdomen with rising lactate is the early picture; peritonism is late."),
  ],
  decode=[
    ("New paraplegia in a descending dissection — which artery? [pattern]", "Artery of Adamkiewicz (intercostals T8–T12)."),
    ("Dissection with rising lactate and abdominal pain [pattern]", "Mesenteric malperfusion: the coeliac or SMA is compromised."),
  ],
  punch="Each branch the false lumen squeezes gives its own syndrome, and which syndromes are possible depends on which part of the aorta is dissected.",
)

L['AD-06'] = dict(
  sub="Cardiology → Aortic dissection → Propagation and dP/dt",
  step=2,
  intro="Step 2 asks what makes the tear spread. The answer, the steepness of each pressure upstroke, is why the drug order in AD-19 matters. The one real question is a type A dissection with a heart rate of 112, and a third of the cohort chose something other than a beta-blocker.",
  parts=[
    ('a', "**Shear stress, a function of pressure over time, dP/dt.** Each systole drives a pressure wave into the flap; the faster pressure rises, the harder the column of blood pushes into the plane of the dissection and the further it travels. Mean pressure alone does not capture this."),
    ('b', "**Influenced more by heart rate than by mean arterial pressure.** A faster heart means more upstrokes per minute and a steeper upstroke (more contractility, shorter ejection time). Halving the rate halves the number of pushes into the tear."),
    ('c', "**Lowering the heart rate is critical to reduce propagation.** Hence a beta-blocker first, to HR about 60, before any vasodilator. A vasodilator alone lowers pressure but triggers baroreflex tachycardia and a stronger contraction, which raises dP/dt."),
  ],
  mimic=[
    ("Dissection vs other hypertensive emergencies", "In most hypertensive emergencies the target is the pressure; in dissection it is dP/dt, so the heart rate is controlled first and the pressure is lowered much further and faster (SBP <120 within the first hour)."),
  ],
  traps=[
    ("“Start nitroprusside: the BP of 182/93 is the problem” (38% of the cohort chose something other than esmolol)", "Nitroprusside alone causes reflex tachycardia and raises dP/dt; it is added only after the beta-blocker."),
    ("“Get a TEE or consult cardiology first”", "CT has already made the diagnosis; more imaging or a consult only delays anti-impulse therapy and surgery."),
  ],
  decode=[
    ("Type A on CT, HR 112, BP 182/93, AR murmur — next best step? [DocT GT]", "Start an esmolol infusion (62%), then arrange surgery."),
    ("Which variable most influences propagation? [pattern]", "Heart rate (dP/dt), more than MAP."),
  ],
  punch="A dissection spreads with every steep upstroke, so the heart rate is lowered first; a vasodilator given alone makes the heart beat faster and harder, and the tear spreads.",
)

L['AD-07'] = dict(
  sub="Cardiology → Aortic dissection → True vs false lumen",
  step=2,
  intro="Step 2: telling the lumens apart matters because TEVAR has to land in the true lumen and because the branches arising from the false lumen are the ones at risk. The real question asks how echo separates them; nearly half of the cohort picked a feature of the false lumen.",
  parts=[
    ('a', "**True lumen is anteromedial.** In the descending aorta the false lumen usually spirals along the outer (left posterolateral) curve. Position helps on CT but is not reliable; flow and behaviour through the cardiac cycle are better."),
    ('b', "**Coeliac, superior mesenteric and right renal arteries.** These usually stay with the true lumen."),
    ('c', "**Left renal artery, often from the false lumen.** That is why left kidney malperfusion and AKI are common in type B and DeBakey I dissections."),
  ],
  table=dict(title="Echo: true vs false lumen",
    head=["Feature", "True lumen", "False lumen"],
    rows=[["Systole", "Expands", "Compressed"],
          ["Colour flow", "Systolic, forward, in phase with the cardiac cycle", "Slow, delayed or reversed; spontaneous contrast or thrombus"],
          ["Size", "Usually smaller", "Usually larger"],
          ["Cobwebs (residual media strands)", "Absent", "Present"]]),
  mimic=[
    ("Which lumen is larger?", "The false lumen usually is; a small lumen is not proof it is false."),
  ],
  traps=[
    ("“The false lumen is usually smaller” or “expands in systole” (56% right)", "Both describe the true lumen in reverse: the false lumen is usually larger and is compressed in systole."),
    ("“Cobwebs are seen in the true lumen”", "Cobwebs (strands of residual media) are a feature of the false lumen."),
  ],
  decode=[
    ("Descending dissection — most helpful echo feature for the true lumen? [DocT GT]", "Colour Doppler flow in phase with the cardiac cycle, systolic expansion (56%)."),
    ("Which renal artery usually arises from the false lumen? [pattern]", "Left."),
  ],
  punch="The true lumen expands and fills forward in systole; the false lumen is larger, slower, has cobwebs, and often feeds the left renal artery.",
)

L['AD-08'] = dict(
  sub="Cardiology → Aortic dissection → IRAD time classification",
  step=3,
  intro="Step 3 begins with time, because risk of death and rupture falls steeply after the first days. Not asked directly; the trap is that IRAD and ESC use different time bands.",
  parts=[
    ('a', "**Hyperacute: onset to 24 hours.** The highest mortality: untreated type A dies at about 1–2% per hour in the first 48 hours."),
    ('b', "**Acute: 2 to 7 days.** Risk is still high; most early deaths happen in the first week."),
    ('c', "**Subacute: 8 to 30 days.** The flap is still mobile, so TEVAR can still reshape the aorta."),
    ('d', "**Chronic: beyond 30 days.** The flap stiffens and the false lumen thickens, so remodelling after TEVAR is less likely."),
    ('e', "**Consider acute and unstable up to 14 days from onset.** This matches the ESC 2024 bands: hyperacute <24 h, acute 1–14 days, subacute 15–90 days, chronic >90 days. The ESC ‘subacute’ window (14–90 days) is the one in which TEVAR for uncomplicated type B is considered (AD-27)."),
  ],
  table=dict(title="Two time systems",
    head=["Phase", "IRAD (card)", "ESC 2024"],
    rows=[["Hyperacute", "<24 h", "<24 h"],
          ["Acute", "2–7 days", "1–14 days"],
          ["Subacute", "8–30 days", "15–90 days"],
          ["Chronic", ">30 days", ">90 days"]]),
  mimic=[
    ("IRAD subacute vs ESC subacute", "8–30 days in IRAD; 15–90 days in ESC 2024, the window used for elective TEVAR."),
  ],
  traps=[
    ("“Acute means the first 7 days, so a 10-day dissection is stable”", "It is still treated as acute and unstable up to 14 days."),
  ],
  decode=[
    ("Dissection 3 weeks old — which IRAD phase? [pattern]", "Subacute (8–30 days)."),
  ],
  punch="IRAD splits time at 24 hours, 7 days and 30 days, ESC at 24 hours, 14 days and 90 days; either way, treat the first two weeks as unstable.",
)

L['AD-09'] = dict(
  sub="Cardiology → Aortic dissection → DeBakey classification",
  step=3,
  intro="Step 3: DeBakey classifies by where the dissection starts and how far it extends. Both real questions were answered badly (12% and 38%), because each needs you to work out which branches and complications are anatomically possible.",
  parts=[
    ('a', "**Type I: ascending AND descending aorta.** Starts in the ascending aorta and runs at least to the arch, usually beyond. Every complication is possible: coronary, cerebral, AR, tamponade, visceral, renal, spinal and limb."),
    ('b', "**Type II: ascending aorta ONLY.** Confined proximal to the innominate artery. It can cause AR, tamponade and coronary occlusion, but it cannot reach the mesenteric or renal arteries."),
    ('c', "**Type III: descending aorta ONLY.** Starts beyond the left subclavian. IIIa stops above the diaphragm (descending thoracic only); IIIb extends below it into the abdominal aorta. Both are Stanford B. It cannot cause AR, tamponade or coronary occlusion (unless it extends backwards into the arch)."),
  ],
  mimic=[
    ("DeBakey IIIa vs IIIb", "IIIa is limited to the thoracic descending aorta; IIIb extends below the diaphragm."),
    ("DeBakey II vs Stanford A", "All DeBakey II is Stanford A, but Stanford A also includes DeBakey I."),
  ],
  traps=[
    ("“A dissection of the descending thoracic aorta is DeBakey III” (bare III, or IIIb; 38% right)", "With the subdivision offered, thoracic-only is IIIa; IIIb goes below the diaphragm."),
    ("“Which pairing is NOT correct?” — only one option looks wrong (12% right)", "Two are wrong: DeBakey II (ascending only) cannot cause high lactate, high INR and AKI from visceral malperfusion, and DeBakey III (descending only) cannot cause a new AR murmur. DocT keys A (the DeBakey II pairing); pick A."),
  ],
  decode=[
    ("Dissection of the descending thoracic aorta — DeBakey type? [DocT GT]", "IIIa (38%)."),
    ("Which complication–classification pairing is wrong? [DocT GT]", "Visceral malperfusion with DeBakey II (12%); AR with DeBakey III is also wrong."),
  ],
  punch="DeBakey I is everywhere, II is ascending only, III is descending only (IIIa thoracic, IIIb below the diaphragm), and each type can cause only the complications its segment supplies.",
)

L['AD-10'] = dict(
  sub="Cardiology → Aortic dissection → Stanford classification",
  step=3,
  intro="Step 3: Stanford simplifies DeBakey to the one question that decides treatment: is the ascending aorta involved? The one real question is the GT pairing question shared with AD-09.",
  parts=[
    ('a', "**Type A: involves the aorta proximal to the left subclavian origin.** Strictly, type A is any involvement of the ascending aorta, wherever the tear starts; an arch-only dissection is non-A non-B (AD-11)."),
    ('b', "**Type B: involves the aorta distal to the left subclavian origin.** Without ascending involvement."),
    ('c', "**DeBakey I and II = Stanford A; DeBakey III = Stanford B.** DeBakey adds extent; Stanford keeps only what changes management."),
    ('d', "**Deciding feature: is the ascending aorta involved?** If yes, the risks are tamponade, coronary occlusion and AR, which only surgery fixes, so type A is a surgical emergency (AD-12)."),
  ],
  mimic=[
    ("Stanford A from a descending tear", "A tear in the descending aorta that extends backwards into the ascending aorta is still type A."),
  ],
  traps=[
    ("“Elevated troponin cannot occur in Stanford A”", "It can: the flap can occlude a coronary ostium. Troponin with Stanford A is a correct pairing."),
  ],
  decode=[
    ("Pairing of complications with Stanford and DeBakey types [DocT GT]", "Troponin rise with Stanford A and hemiplegia with DeBakey I are correct pairings."),
  ],
  punch="Stanford asks only whether the ascending aorta is involved, because that is what decides between the operating theatre and the ICU.",
)

L['AD-11'] = dict(
  sub="Cardiology → Aortic dissection → TEM classification",
  step=3,
  intro="Step 3 ends with the classification the 2024 ESC guideline adopted. It keeps Stanford’s logic but adds where the entry tear is and whether organs are ischaemic, because both change the operation. Not asked yet.",
  parts=[
    ('a', "**T = Type of dissection; E = Entry tear location; M = Malperfusion (carries prognostic and therapeutic weight).** E0 means no entry seen; E1 entry in the ascending aorta (zone 0), E2 in the arch, E3 in the descending aorta. M0 none, M1 coronary, M2 supra-aortic, M3 spinal, visceral, renal or limb, each marked + if clinically symptomatic."),
    ('b', "**Type A, Type B, non-A non-B.** ESC 2024 defines non-A non-B as dissections limited to the arch, or retrograde from the descending aorta into the arch, without involving the ascending aorta."),
    ('c', "**Arch involvement WITHOUT ascending involvement: unclassifiable in Stanford, now non-A non-B.** These behave between A and B: they rarely need emergency sternotomy but often need arch or hybrid repair."),
  ],
  mimic=[
    ("Non-A non-B vs type B", "Type B stays distal to the left subclavian; non-A non-B involves the arch without the ascending aorta."),
  ],
  traps=[
    ("“TEM replaced the need to assess malperfusion clinically”", "M is graded with a + sign for clinical signs, so the bedside picture is part of the class."),
  ],
  decode=[
    ("Classification used by ESC 2024 with a non-A non-B category [pattern]", "TEM (type, entry, malperfusion)."),
  ],
  punch="TEM keeps Stanford’s A and B, adds non-A non-B for arch-only dissection, and records the entry tear and malperfusion because they decide the operation.",
)

L['AD-12'] = dict(
  sub="Cardiology → Aortic dissection → Management and mortality by type",
  step=6,
  intro="Step 6 starts with the decision between theatre and ICU. The numbers invert between types: surgery saves type A and harms uncomplicated type B. The real question is the same type A vignette as AD-06, testing what comes before the surgeon arrives.",
  parts=[
    ('a', "**Preferred: SURGERY for type A, MEDICAL for type B.** Type A kills by tamponade, coronary occlusion and AR, which no drug fixes. Uncomplicated type B rarely ruptures early, and an operation on the descending aorta carries the risks of paraplegia, renal failure and a thoracotomy."),
    ('b', "**Medical mortality: ~50% for type A, ~15% for type B.** ESC 2024 gives about 50% within 48 hours for untreated type A (1–2% per hour); IRAD 2000 gave 58% for medically treated type A and 10.7% for type B."),
    ('c', "**Surgical mortality: 15–20% for type A, ~30% for type B.** ESC 2024 quotes 17–25% perioperative mortality for type A; IRAD 2000 gave 26% for type A and 31.4% for surgically treated type B. Surgery in type B is usually reserved for complicated cases, which partly explains the high figure; TEVAR has largely replaced it (AD-27)."),
  ],
  mimic=[
    ("Type A: drug first or surgery first?", "Both: start anti-impulse therapy at once and go to surgery; drugs are a bridge, not the treatment."),
  ],
  traps=[
    ("“Type A on CT — order a TEE” or “consult cardiology” before treatment (62% right)", "The diagnosis is made; esmolol starts now and the surgeon is called."),
    ("“Surgery improves survival in all dissections”", "Open surgery roughly doubles mortality in uncomplicated type B; medical therapy (then TEVAR if complicated or high risk) is preferred."),
  ],
  decode=[
    ("Type A on CT, tachycardic, hypertensive — next best step? [DocT GT]", "Start esmolol (62%), with urgent surgery."),
    ("Mortality of medically treated type A in the first 48 h [pattern]", "About 50%, 1–2% per hour."),
  ],
  punch="Type A goes to theatre because its killers are mechanical and mortality without surgery is about 50%; uncomplicated type B stays on drugs because surgery there roughly doubles mortality.",
)

L['AD-13'] = dict(
  sub="Cardiology → Aortic dissection → Complicated dissection",
  step=3,
  intro="Step 3: ‘complicated’ is the label that moves a type B dissection from medical treatment to TEVAR (AD-27). Not asked directly.",
  parts=[
    ('a', "**Rupture or impending rupture.** Blood outside the aorta (haemothorax, mediastinal or periaortic haematoma) or rapid expansion."),
    ('b', "**Intractable pain.** Pain that persists or recurs despite full analgesia and anti-impulse therapy means the dissection is still extending."),
    ('c', "**Malperfusion syndrome.** Organ or limb ischaemia from the false lumen (AD-05)."),
    ('d', "**Cardiac tamponade.** Rupture into the pericardium, a type A feature (AD-25)."),
    ('e', "**Severe aortic valve insufficiency.** Also type A. ESC 2024 also counts rapid aortic expansion, paraplegia, periaortic haematoma and uncontrolled hypertension; ‘high-risk’ uncomplicated type B (commonly cited features: aorta >40 mm, false lumen >20 mm, entry tear >10 mm) is a separate group that may get TEVAR in the subacute phase."),
  ],
  mimic=[
    ("Complicated vs high-risk uncomplicated type B", "Complicated (rupture, malperfusion, intractable pain) → TEVAR now (I, B); high-risk uncomplicated (large aorta or false lumen, large entry tear) → consider TEVAR at 14–90 days (IIa, B)."),
  ],
  traps=[
    ("“Hypertension alone makes a dissection complicated”", "Only refractory hypertension despite full therapy is counted, and it signals ongoing extension."),
  ],
  decode=[
    ("Type B with leg ischaemia or rising lactate — management? [pattern]", "Complicated → TEVAR."),
  ],
  punch="Rupture, intractable pain, malperfusion, tamponade or severe AR makes a dissection complicated, and in type B that means TEVAR rather than drugs alone.",
)

L['AD-14'] = dict(
  sub="Cardiology → Aortic dissection → Clinical signs",
  step=4,
  intro="Step 4 is recognition at the bedside. The signs follow the anatomy: pain from the tearing wall, pressure differences from compressed branches, a diastolic murmur from a disrupted valve, and shock from tamponade or rupture. The linked real question shows a classic picture and asks for the imaging test, where DocT’s key is outdated (AD-17).",
  parts=[
    ('a', "**Sudden-onset severe ‘ripping’ or ‘tearing’ chest pain, back pain radiating to the chest.** The key feature is that the pain is maximal at onset (85% abrupt in IRAD); only about half call it tearing, and sharp is the commonest word. Anterior chest pain suggests type A, back or abdominal pain type B; about 6% have no pain."),
    ('b', "**HIGH blood pressure.** Typical of type B; type A patients are more often normotensive or hypotensive because of tamponade, AR or rupture."),
    ('c', "**Difference between arms >20 mmHg (also radial pulse deficit).** The flap compresses the subclavian or innominate; a pulse deficit is seen in only about 15%, so its absence does not exclude dissection. Measure the pressure in both arms before giving thrombolysis."),
    ('d', "**Diastolic murmur: aortic insufficiency.** Heard in about a third. The flap dilates the root, tears the commissures or prolapses through the valve. A murmur at the right sternal border points to root dilatation, as in the vignette."),
    ('e', "**Low BP, muffled heart sounds.** Rupture into the pericardium; with raised JVP this is Beck’s triad."),
    ('f', "**LATE sign (also collapse or syncope; focal neuro deficit → limb weakness, paraesthesia).** Hypotension means tamponade, rupture, severe AR or coronary occlusion, and it carries the worst prognosis. Syncope (about 9%) often means tamponade or carotid involvement."),
  ],
  mimic=[
    ("Dissection vs ACS pain", "Dissection: maximal at onset, tearing or sharp, moving to the back, pulse or pressure asymmetry. ACS: builds over minutes, pressing, with no asymmetry."),
  ],
  traps=[
    ("“TEE is the preferred test” for a stable patient with BP 205/110 (DocT key; 40% chose it)", "The key is outdated: ESC 2024 makes ECG-gated CT neck to pelvis first line (I, C). For a stable patient choose CT; TEE is for the unstable or for the theatre."),
    ("“No pulse deficit, so no dissection”", "Pulse deficits are present in only about 15%."),
  ],
  decode=[
    ("Tearing pain to the jaw, BP 205/110, diastolic murmur, widened mediastinum — preferred test? [DocT QBank]", "CT angiography (DocT keys TEE, 40%)."),
    ("Hypotension in dissection: early or late? [pattern]", "Late, and ominous (tamponade, rupture, AR)."),
  ],
  punch="Pain maximal at onset with a pressure difference or a new diastolic murmur means dissection; high BP is usual, and hypotension means the aorta has ruptured into the pericardium or the valve has failed.",
)

L['AD-15'] = dict(
  sub="Cardiology → Aortic dissection → Dissection mimicking ACS",
  step=4,
  intro="Step 4: the commonest misdiagnosis, and the one with the worst consequence, because the treatment for ACS can kill a dissection patient. Not asked directly here, but the GT question on AD-17 is built on this overlap.",
  parts=[
    ('a', "**Misdiagnosed as ACUTE CORONARY SYNDROME; consider dissection once ACS is ruled out.** Both happen in older hypertensive men with severe chest pain, and most dissection ECGs are abnormal."),
    ('b', "**Non-specific ST-T changes and T-wave inversion, especially when the dissection involves the coronary artery origins.** In IRAD, 41% had non-specific ST-T changes and 15% ischaemic changes, but only about 3% a new infarct pattern. When it happens, it is usually the right coronary ostium, so an inferior STEMI."),
    ('c', "**Coronary origin involvement → true myocardial injury, mimicking MI.** Troponin also rises from hypotension, tachycardia and LVH strain, so a positive troponin does not exclude dissection."),
    ('d', "**THROMBOLYSIS given for a presumed MI can be catastrophic.** Lysis or heparin turns the false lumen into a bleeding cavity and can cause tamponade. Aortic dissection is an absolute contraindication to fibrinolysis (MI-53), and the pressure in both arms is checked before lysis."),
  ],
  mimic=[
    ("Inferior STEMI from RCA occlusion vs from type A dissection", "Look for a pressure or pulse difference, AR murmur, widened mediastinum or effusion on bedside echo; image the aorta before lysis or the catheter lab."),
  ],
  traps=[
    ("“Normal troponin excludes dissection” or “raised troponin confirms ACS”", "Troponin is often normal in dissection and can be raised by it; it does not separate the two."),
  ],
  decode=[
    ("Inferior STEMI with BP difference between arms — next step? [pattern]", "Image the aorta (CT) before thrombolysis or anticoagulation."),
  ],
  punch="Dissection imitates ACS, usually through the right coronary, and the treatment for ACS can kill it, so check both arms and look at the aorta before lysis.",
)

L['AD-16'] = dict(
  sub="Cardiology → Aortic dissection → Bedside tests",
  step=4,
  intro="Step 4: the bedside tests raise or lower suspicion but never settle it. The one real question asks which chest X-ray sign is seen.",
  parts=[
    ('a', "**Widened mediastinum: 50%.** IRAD found a widened mediastinum in about 62% and an abnormal aortic contour in about 50%. Other signs: a double or irregular aortic contour, displacement of intimal calcification more than 5 mm inside the outer aortic wall (calcium sign; some texts use 1 cm), and a left pleural effusion."),
    ('b', "**Falsely reassuring → missed diagnosis.** About 12% of chest X-rays are completely normal (IRAD). ESC 2024: an X-ray and ECG are done to exclude other causes, and normal findings must not delay CT."),
    ('c', "**Leukocytosis or thrombocytopenia (platelet consumption).** The false lumen is a large thrombogenic surface; platelets and fibrinogen are consumed and D-dimer rises. A D-dimer under 500 ng/mL makes acute dissection unlikely (ESC 2024)."),
    ('d', "**Gut ischaemia: compromised coeliac or superior mesenteric arteries.** Lactate rises with mesenteric malperfusion, or with shock; a rising lactate after repair calls for repeat CT (AD-26)."),
  ],
  mimic=[
    ("Widened mediastinum: dissection vs traumatic aortic injury", "Trauma: deceleration injury at the isthmus; dissection: spontaneous pain in a hypertensive patient. Both go to CT."),
  ],
  traps=[
    ("“A normal chest X-ray excludes dissection”", "About one in eight are normal."),
  ],
  decode=[
    ("Feature of dissection on chest X-ray [Marrow]", "Abnormal aortic contour (also a widened mediastinum, calcium sign)."),
    ("Low-risk patient with D-dimer <500 ng/mL [pattern]", "Dissection unlikely."),
  ],
  punch="The X-ray shows a widened mediastinum or abnormal contour in about half to two thirds, is normal in one in eight, and can never rule dissection out; only CT does that.",
)

L['AD-17'] = dict(
  sub="Cardiology → Aortic dissection → Imaging",
  step=4,
  intro="Step 4 ends with the test that decides. Four real questions ask which test to choose and what it shows, and the choice depends on one thing: whether the patient can safely go to the scanner. DocT’s QBank key is outdated, and its GT question shows how an effusion leads people into a lethal step.",
  parts=[
    ('a', "**TTE: shows severe AR if the root or valve is involved; may miss the dissection.** It sees the root, valve, pericardium and LV well but only parts of the aorta. Its role is the first bedside look: an effusion, AR or a dilated root in a patient with chest pain means type A until proved otherwise."),
    ('b', "**TEE: superior to TTE, sees nearly all the aorta (blind spot: distal ascending aorta and proximal arch, behind the trachea); useful if CT is contraindicated or the patient cannot be transported.** It shows an undulating flap separating the lumens, colour flow in both lumens, entry and exit tears, false-lumen stasis or thrombus, and intramural haematoma (crescentic wall thickening without a flap). ESC 2024 recommends it to guide peri-operative management (I, C): in theatre it confirms the entry tear, valve mechanism and coronary involvement."),
    ('c', "**CT aortogram: the DEFINITIVE test, whole aorta; preferred over routine contrast CT chest or CT pulmonary angiography.** ESC 2024 first-line test: ECG-gated contrast CT from neck to pelvis (I, C), sensitivity 100% and specificity 98%. ECG gating removes motion artefact at the root that can mimic a flap; neck to pelvis shows the extent, the branches and malperfusion."),
    ('d', "**MR angiography: detailed but slow, unsuitable for unstable patients.** It is used for follow-up and when contrast or radiation must be avoided."),
  ],
  mimic=[
    ("Stable vs unstable suspected dissection", "Stable → CT; too unstable to move → TEE in the ED or theatre (with bedside TTE first). The same split applies to PE: stable → CTPA, unstable → bedside echo."),
    ("CT aortogram vs CTPA", "A CTPA times contrast for the pulmonary arteries and can miss the aorta; a suspected dissection needs an aortic (ECG-gated) protocol."),
  ],
  traps=[
    ("“TEE is the preferred investigation” for a stable patient with BP 205/110 (DocT key; 40% chose it)", "The key is outdated. ESC 2024 makes CT first line; TEE is for the unstable, CT contraindication, or in theatre. If the patient is stable and CT is offered, pick CT."),
    ("“Pericardiocentesis” or “coronary angiography” for chest pain, BP 200/89, negative troponin and an effusion (24% right)", "The effusion with a normal troponin and hypertension points to type A dissection; pericardiocentesis can restore pressure and speed rupture, and coronary angiography delays surgery. Image the aorta with CT, then go to theatre."),
    ("“TEE sees the whole aorta”", "The trachea hides the distal ascending aorta and proximal arch."),
  ],
  decode=[
    ("Stable, tearing pain, BP 205/110, AR murmur, wide mediastinum — preferred test? [DocT QBank]", "CT angiography (DocT keys TEE; 40%)."),
    ("Chest pain, BP 200/89, troponin negative, moderate effusion on POCUS — next step? [DocT GT]", "Contrast CT of the chest (24%), not pericardiocentesis."),
    ("CT angiogram with an intimal flap and two lumens [DocT QBank]", "Aortic dissection (68%)."),
    ("TEE findings of dissection [Marrow]", "All: flap, flow in both lumens, entry and exit tears, false-lumen thrombus, IMH."),
  ],
  punch="If the patient can go to the scanner, ECG-gated CT from neck to pelvis is the test; TEE is for the patient who cannot be moved and for the theatre; and an effusion with chest pain and hypertension is dissection until CT says otherwise.",
)

L['AD-18'] = dict(
  sub="Cardiology → Aortic dissection → Stabilisation and targets",
  step=5,
  intro="Step 5 begins anti-impulse therapy: pain, heart rate and pressure, in that order, because each drives dP/dt. The one real question tests the drug sequence, which is covered in AD-19.",
  parts=[
    ('a', "**Opioid (morphine): cuts sympathetic drive → prevents tachycardia and further shear stress (dP/dt).** Pain releases catecholamines that raise heart rate and contractility; analgesia is part of reaching the targets (ESC 2024: adequate pain control, I, C). Persistent pain despite analgesia means the dissection is still extending (AD-13)."),
    ('b', "**HR <60 bpm.** ESC 2024: HR ≤60 b.p.m. (I, B). The 2022 ACC/AHA guideline gives 60–80 b.p.m. (class 1, C-LD). In the exam, ‘about 60’ fits both."),
    ('c', "**SBP <120 mmHg.** Both guidelines; ACC/AHA adds ‘or the lowest BP that maintains end-organ perfusion’ (class 1, C-LD), and most protocols aim to reach it within about the first hour. ESC 2024 accepts a higher pressure when an organ is malperfused. Heart rate first, then pressure."),
    ('d', "**Arterial and central lines: avoid rapid BP fluctuations.** An arterial line, ideally in the arm with the higher pressure (the other arm may be reading a compressed subclavian), allows titration of short-acting infusions beat to beat; a central line is for vasoactive drugs."),
  ],
  mimic=[
    ("ESC vs ACC/AHA heart-rate target", "ESC 2024: ≤60; ACC/AHA 2022: 60–80. Same SBP target, below 120."),
  ],
  traps=[
    ("“Labetalol alone is wrong because it is not esmolol”", "Labetalol is an acceptable first-line agent (it blocks β and α1); the key prefers esmolol then nicardipine because it follows the beta-blocker-before-vasodilator rule."),
    ("“Put the arterial line in the arm with the lower pressure”", "Use the arm with the higher reading; the lower one may reflect a compressed branch and underestimate the true pressure."),
  ],
  decode=[
    ("Type B, BP 210/115, HR 102 — initial drugs? [DocT GT]", "Esmolol followed by nicardipine (59%)."),
    ("HR and SBP targets in acute dissection [pattern]", "HR about 60 (ESC ≤60; ACC/AHA 60–80), SBP <120 mmHg."),
  ],
  punch="Treat the pain, slow the heart to about 60, then bring the systolic below 120, watching an arterial line in the arm with the higher pressure.",
)

L['AD-19'] = dict(
  sub="Cardiology → Aortic dissection → Drug sequence",
  step=5,
  intro="Step 5’s core: five real questions all test one rule, beta-blocker before vasodilator. Each distractor is a drug that lowers pressure without slowing the heart, or a slow route of giving the right drug.",
  parts=[
    ('a', "**IV BETA-BLOCKERS: labetalol (α1 + β1 + β2), esmolol (short-acting β1, infusion), metoprolol (small boluses).** Beta-blockade lowers heart rate and contractility, so dP/dt falls before pressure does. Esmolol is preferred when the patient may not tolerate beta-blockade (asthma, borderline pressure, AR) because it wears off in about 10–20 minutes. Labetalol alone can reach both targets, since it also vasodilates; ESC 2024 calls IV labetalol the usual first choice, with esmolol an option."),
    ('b', "**Non-dihydropyridine CCB (diltiazem); ACE inhibitor also considered.** ESC 2024 (IIa, B) and ACC/AHA 2022 (2a, B-NR): an IV non-DHP calcium blocker for rate control if beta-blockers are contraindicated or not tolerated. Diltiazem and verapamil slow the sinus and AV nodes; dihydropyridines do not."),
    ('c', "**Nitroglycerin or sodium nitroprusside.** Nicardipine (a dihydropyridine) is the other common choice and the one used in the DocT keys."),
    ('d', "**ONLY after or with a beta-blocker, to block reflex tachycardia.** Once the rate is controlled, the vasodilator takes the systolic below 120."),
    ('e', "**Reflex tachycardia ↑ dP/dt → propagation.** Vasodilation drops the pressure, the baroreflex speeds the heart and strengthens contraction, and the shear on the flap rises even though the cuff reading has fallen."),
  ],
  mimic=[
    ("Diltiazem vs nicardipine", "Diltiazem (non-DHP) slows the heart and replaces a beta-blocker; nicardipine (DHP) only vasodilates and must follow one."),
  ],
  traps=[
    ("“IV nitroprusside alone” or “nicardipine infusion alone” (76–83% right)", "Monotherapy with a vasodilator causes reflex tachycardia; it is used only after a beta-blocker."),
    ("“Oral metoprolol”", "Right class, wrong route: the targets must be reached within the hour, so IV."),
    ("“Sublingual nitroglycerin then an ACE inhibitor”", "Uncontrolled, with no rate control; neither is first line."),
    ("“Labetalol alone is wrong” (GT4/GT5; 59–83% right)", "Labetalol alone is acceptable; DocT keys esmolol then nicardipine, so pick that when both are offered."),
  ],
  decode=[
    ("First-line drug to limit propagation [DocT GT]", "IV esmolol (76%)."),
    ("Type A, BP 180/100 — first-line agent? [DocT GT]", "Esmolol infusion (73%)."),
    ("Type B, BP 210/115, HR 102 — initial pharmacological management? [DocT GT ×2]", "Esmolol followed by nicardipine (59%, 83%)."),
    ("Dissection with arm BP difference on CTA — next step? [Marrow]", "Esmolol."),
  ],
  punch="Every dissection drug question has the same answer: an IV beta-blocker first (or diltiazem if one cannot be given), and a vasodilator only once the heart rate is controlled.",
)

L['AD-20'] = dict(
  sub="Cardiology → Aortic dissection → Beta-blocker doses",
  step=5,
  intro="Step 5: the doses of the drugs that come first. The one real question asks only which drug to start, but the doses show why esmolol is the safest titratable choice.",
  parts=[
    ('a', "**Esmolol (β1): bolus 500 mcg/kg over 1 min, then 50 mcg/kg/min, titrated up to 300 mcg/kg/min.** Red-cell esterases clear it with a half-life of about 9 minutes, so its effect stops within about 20 minutes, which makes it the safest choice if AR, asthma or low pressure might make beta-blockade risky."),
    ('b', "**Labetalol bolus: 20 mg over 2 min, then 20–80 mg every 10 min.** The label gives repeat doses of 40–80 mg every 10 minutes, to a cumulative maximum of 300 mg. Its β:α ratio is about 7:1 IV, so it slows the heart and dilates the arteries."),
    ('c', "**Labetalol infusion: load 20 mg, then 1–2 mg/min.** Its half-life is 5–8 hours, so it is harder to reverse than esmolol."),
    ('d', "**Metoprolol: 5 mg over 2 min, repeated every 5 min, up to 3 doses.** Bolus-only control is less smooth, which is why it ranks behind the infusions."),
  ],
  mimic=[
    ("Esmolol vs labetalol", "Esmolol: pure β1, minutes-long, infusion; labetalol: β plus α1, hours-long, boluses or infusion."),
  ],
  traps=[
    ("“Oral metoprolol to limit propagation”", "Too slow; the IV route is needed to reach targets within the hour."),
  ],
  decode=[
    ("First-line IV agent to limit propagation [DocT GT]", "IV esmolol (76%)."),
    ("Esmolol loading dose [pattern]", "500 mcg/kg over 1 minute, then 50 mcg/kg/min."),
  ],
  punch="Esmolol is the easiest beta-blocker to titrate because a 500 mcg/kg load and a 50–300 mcg/kg/min infusion wear off within minutes; labetalol (ESC 2024’s usual first choice) and IV metoprolol work equally well but last much longer.",
)

L['AD-21'] = dict(
  sub="Cardiology → Aortic dissection → Second-line doses and vasodilator toxicity",
  step=5,
  intro="Step 5 ends with the vasodilators and the most-asked card in the deck: seven questions, six of them on what each drug does to the body with prolonged use. The key fact is the chemistry: nitroprusside carries cyanide, nitroglycerin carries nitrite.",
  parts=[
    ('a', "**Diltiazem (non-DHP): 0.25 mg/kg over 2 min, then 5–10 mg/h, up to 15 mg/h.** It is the rate-controlling alternative when a beta-blocker is contraindicated."),
    ('b', "**Nicardipine (DHP): 5 mg/h, increased by 2.5 mg/h every 5–15 min, max 15 mg/h.** A pure arterial dilator with no effect on the heart rate, so it follows the beta-blocker."),
    ('c', "**Nitroprusside: 0.3 mcg/kg/min, max 10 mcg/kg/min (no more than 10 min at max); cyanide toxicity, unsuitable for prolonged use.** Each molecule releases five cyanide ions. Rhodanese uses thiosulfate to turn cyanide into thiocyanate, which the kidney excretes. Two toxicities follow. Cyanide comes early, at high doses (above about 2 mcg/kg/min) or when thiosulfate runs out: cells cannot use oxygen, so there is lactic acidosis, a high venous oxygen saturation, confusion and tachycardia. Thiocyanate builds up later, after 48–72 hours or in renal failure (toxic above about 60 mg/L on a serum level), causing confusion, psychosis and seizures. Stop the infusion and give hydroxocobalamin or sodium thiosulfate."),
    ('d', "**Nitroglycerin: 5 mcg/min, increased by 5 mcg/min every 3–5 min (ceiling commonly quoted as 200 mcg/min).** Mostly a venodilator at low doses. Prolonged use causes headache, reflex tachycardia, tachyphylaxis within 24 hours, methaemoglobinaemia (its nitrite oxidises haemoglobin) and inhibition of platelet aggregation, but never cyanide toxicity."),
  ],
  table=dict(title="Nitroprusside vs nitroglycerin: the toxicity questions",
    head=["", "Nitroprusside", "Nitroglycerin"],
    rows=[["Toxic product", "Cyanide (early), thiocyanate (late, renal failure)", "Nitrite → methaemoglobin"],
          ["Clues", "Lactic acidosis, high venous O₂, confusion, almond breath", "Headache, tachycardia, tachyphylaxis, cyanosis with normal PaO₂"],
          ["Test", "Lactate, venous O₂; serum thiocyanate (cyanide: whole-blood level)", "Methaemoglobin level"],
          ["Treatment", "Stop; hydroxocobalamin or sodium thiosulfate", "Stop; methylene blue"]]),
  mimic=[
    ("Cyanide vs thiocyanate toxicity from nitroprusside", "Cyanide: early, high dose, lactic acidosis and high venous saturation. Thiocyanate: late (48–72 h) or renal failure, neurotoxic, no lactic acidosis."),
    ("Hydroxocobalamin vs cyanocobalamin", "Hydroxocobalamin binds cyanide to become cyanocobalamin, which is the harmless end product, not the antidote."),
  ],
  traps=[
    ("GrandT1 keys “nitroglycerin” for confusion, tachycardia, acidosis and almond breath after a high-dose infusion (16% right)", "The key is wrong: that is cyanide from nitroprusside, as the GT3 and AIM2 repeats and DocT’s own explanation say. Pick nitroprusside."),
    ("“Cyanide toxicity is a side effect of prolonged nitroglycerin” (41–43% right)", "Nitroglycerin causes methaemoglobinaemia, headache, tachycardia and inhibited platelet aggregation; cyanide belongs to nitroprusside."),
    ("“Give thiocyanate” or “cyanocobalamin” for nitroprusside toxicity (39% right)", "Thiocyanate is the toxic product, cyanocobalamin is what hydroxocobalamin becomes; the antidotes are sodium thiosulfate and hydroxocobalamin. Methylene blue treats methaemoglobinaemia."),
    ("“Urinary thiocyanate confirms it” (58% right)", "Serum thiocyanate is the proper test, but among the four options it is still the best answer; an ABG shows acidosis but does not confirm the cause."),
  ],
  decode=[
    ("72 h of high-dose nitroprusside, altered sensorium, lactic acidosis — confirmatory test? [DocT QBank]", "Thiocyanate level (58%)."),
    ("Nitroprusside for 32 h in renal failure, confusion, acidosis — prevention/treatment? [DocT GT]", "Sodium thiosulfate (39%)."),
    ("Nitroglycerin drip for a day — least likely side effect? [DocT GT ×2]", "Cyanide toxicity (41%, 43%)."),
    ("High-dose infusion, confused, tachycardic, almond breath — drug? [DocT GT]", "Nitroprusside (DocT keys nitroglycerin, 16%)."),
    ("Most critical thing to monitor with prolonged nitroprusside [DocT GT]", "Cyanide toxicity (95%)."),
    ("Nitroglycerin infusion dose in hypertensive emergency [NEET 2024]", "Start 5 mcg/min, titrate by 5 mcg/min every 3–5 min."),
  ],
  punch="Nitroprusside carries five cyanides per molecule, so high doses or long infusions (especially in renal failure) cause lactic acidosis and confusion treated with thiosulfate or hydroxocobalamin; nitroglycerin carries nitrite, so it causes methaemoglobinaemia, never cyanide.",
)

L['AD-22'] = dict(
  sub="Cardiology → Aortic dissection → Type A repair",
  step=6,
  intro="Step 6: type A goes to open surgery because the problems are at the root, where stents cannot yet land safely. Not asked directly.",
  parts=[
    ('a', "**Proximity to the aortic root and involvement of the coronary origins makes endovascular repair challenging.** A stent graft needs a healthy landing zone; the ascending aorta is short, close to the valve and the coronaries, and moves with each beat."),
    ('b', "**Resect the diseased segment → replace with a synthetic graft.** At minimum, the entry tear in the ascending aorta is removed and the graft is sewn to the reconstructed root and to the arch; ESC 2024 recommends an open distal anastomosis (under circulatory arrest, AD-23) to improve survival and false-lumen thrombosis (I, B)."),
    ('c', "**Valve involved, aortic insufficiency, or dilated root >55 mm → simultaneous aortic valve replacement.** ESC 2024 and ACC/AHA 2022: when the leaflets are normal, resuspension of the valve is preferred over replacement; root replacement with a valved conduit is for root destruction, a root aneurysm or a genetic disorder such as Marfan (I, B)."),
    ('d', "**Midline sternotomy.** On cardiopulmonary bypass, often with axillary artery cannulation so that perfusion goes into the true lumen."),
  ],
  mimic=[
    ("AR in type A: resuspend vs replace", "Normal leaflets with commissural detachment → resuspend; destroyed root, aneurysm or connective-tissue disorder → root replacement."),
  ],
  traps=[
    ("“AR in type A always means valve replacement”", "Most AR in type A is from commissural detachment with normal leaflets and is fixed by resuspension."),
  ],
  decode=[
    ("Why type A is not treated with a stent graft [pattern]", "Root and coronary ostia: no safe landing zone."),
  ],
  punch="Type A is repaired openly through a sternotomy, replacing the ascending aorta with a graft and resuspending the valve unless the root itself is destroyed or diseased.",
)

L['AD-23'] = dict(
  sub="Cardiology → Aortic dissection → Hypothermic circulatory arrest",
  step=6,
  intro="Step 6: repairing the arch means stopping flow to the brain, and cold is what makes that survivable. The one real question uses a different temperature scale altogether, and nearly half of the cohort mixed the two.",
  parts=[
    ('a', "**Surgery on the aortic root or arch needs temporary arrest of the cerebral circulation.** No clamp can be placed on the arch without stopping flow to its branches, and the open distal anastomosis is sewn in a bloodless field."),
    ('b', "**↓ Cerebral metabolic rate and oxygen consumption → protects neurons.** Cerebral metabolic rate falls by about 6–7% per °C; at about 18 °C the brain tolerates roughly 30–40 minutes of arrest, longer with selective cerebral perfusion (AD-24)."),
    ('c', "**Profound ≤14 °C, deep 14.1–20 °C, moderate 20.1–28 °C, mild 28.1–34 °C.** These are the 2013 international consensus grades for circulatory arrest. With antegrade cerebral perfusion many centres now use moderate hypothermia, which reduces bleeding and bypass time."),
  ],
  table=dict(title="Two hypothermia scales",
    head=["Grade", "Surgical (DHCA consensus)", "Accidental / clinical"],
    rows=[["Mild", "28.1–34 °C", "32–35 °C"],
          ["Moderate", "20.1–28 °C", "28–32 °C"],
          ["Deep / severe", "Deep 14.1–20 °C", "Severe <28 °C"],
          ["Profound", "≤14 °C", "<24 °C (some systems)"]]),
  mimic=[
    ("30 °C: surgical vs accidental scale", "On the surgical scale 30 °C is mild; on the accidental scale it is moderate. A TTM or ED stem uses the accidental scale."),
  ],
  traps=[
    ("“30 °C during TTM is mild hypothermia” (55% right)", "Clinical and accidental scales call 28–32 °C moderate; the surgical scale (mild 28.1–34 °C) applies only to circulatory arrest in theatre."),
    ("“Below 14 °C is deep hypothermia”", "By the 2013 consensus, ≤14 °C is profound; deep is 14.1–20 °C."),
  ],
  decode=[
    ("Post-arrest TTM, core falls to 30 °C — grade? [DocT GT]", "Moderate (55%)."),
    ("Temperature range of deep hypothermic circulatory arrest [pattern]", "14.1–20 °C."),
  ],
  punch="Arch surgery stops cerebral flow, so the brain is cooled to cut its oxygen use; know which scale the question uses, because 30 °C is mild in theatre and moderate everywhere else.",
)

L['AD-24'] = dict(
  sub="Cardiology → Aortic dissection → Cerebral perfusion during arch surgery",
  step=6,
  intro="Step 6: cold alone buys limited time, so the brain is also perfused during the arrest. Not asked directly.",
  parts=[
    ('a', "**Retrograde: through the SUPERIOR VENA CAVA.** Cold oxygenated blood is pumped backwards up the SVC into the cerebral veins at low pressure (about 25 mmHg). It cools the brain evenly and flushes air and debris out of the arch vessels, but delivers limited oxygen and can cause cerebral oedema."),
    ('b', "**Antegrade: via a balloon-tipped catheter or axillary artery cannulation.** Blood flows forwards into the arch vessels, either through the right axillary artery (with the innominate clamped) or through cannulas placed directly into the vessel ostia. It gives physiological flow and allows longer, warmer arrests, which is why it is now the commoner choice."),
  ],
  mimic=[
    ("Retrograde vs antegrade cerebral perfusion", "Retrograde: SVC, venous route, mainly cooling and de-airing; antegrade: arterial route, real nutrient flow, longer safe arrest."),
  ],
  traps=[
    ("“Retrograde perfusion goes through the carotids backwards”", "It goes through the SVC and the cerebral veins."),
  ],
  decode=[
    ("Route of retrograde cerebral perfusion [pattern]", "Superior vena cava."),
  ],
  punch="Retrograde perfusion goes up the SVC and mainly cools and de-airs; antegrade perfusion goes through the axillary artery or ostial balloon catheters and actually feeds the brain.",
)

L['AD-25'] = dict(
  sub="Cardiology → Aortic dissection → Tamponade in type A",
  step=6,
  intro="Step 6: tamponade in type A is a rupture into the pericardium, and the clot in the pericardium is all that stops it bleeding. Not asked directly here, but the AD-17 GT question shows why pericardiocentesis is a trap.",
  parts=[
    ('a', "**SLOW drainage, avoiding rapid haemodynamic change that worsens the dissection.** The pericardial pressure is holding back the bleeding; drop it suddenly and the systemic pressure rises, so the false lumen ruptures freely."),
    ('b', "**Drain 30–40 mL, then wait for haemodynamic improvement.** Small volumes restore filling and cardiac output; the aim is a pressure just enough to perfuse. ESC 2024 allows an emergency pericardial puncture only as a temporary life-saving measure before transfer to theatre."),
    ('c', "**Avoid COMPLETE drainage; it destabilises the dissection.** Full drainage restores full pressure into the false lumen."),
    ('d', "**Maintain balance → expedite transfer to theatre.** The definitive treatment is surgical repair; drainage is a bridge."),
  ],
  mimic=[
    ("Tamponade from dissection vs from other causes", "Routine tamponade: drain completely (CVS-27). Type A dissection: drain small volumes only if surgery is delayed, and go to theatre."),
  ],
  traps=[
    ("“Pericardiocentesis is the next step for an effusion with chest pain”", "If dissection is possible, image the aorta; drainage of a haemopericardium from type A can cause fatal rupture."),
  ],
  decode=[
    ("Type A with tamponade, surgery delayed — how to drain? [pattern]", "Controlled drainage of small volumes (30–40 mL), not complete."),
  ],
  punch="In type A tamponade the pericardium is holding back a rupture, so drain only enough to perfuse and get the patient to theatre.",
)

L['AD-26'] = dict(
  sub="Cardiology → Aortic dissection → Post-operative care",
  step=6,
  intro="Step 6: after repair, the false lumen may still be perfusing parts of the aorta, so every organ that was at risk before is still at risk. Not asked directly.",
  parts=[
    ('a', "**Visceral: malperfusion, abdominal compartment syndrome; repeat CT if lactate rises.** Persistent malperfusion is not always relieved by proximal repair, and ischaemic gut and large-volume resuscitation raise intra-abdominal pressure."),
    ('b', "**Pulses: check all four limbs for deficits.** A new deficit means the false lumen is still compressing a branch."),
    ('c', "**Neurological: embolic events and stroke.** Air, debris and cerebral malperfusion during arch surgery; spinal cord ischaemia after descending repair (AD-28)."),
    ('d', "**Coagulation: coagulopathy (platelet consumption), treated with blood products.** Consumption in the false lumen, bypass, hypothermia and dilution all add up."),
    ('e', "**Renal: AKI; wine-coloured urine = haemolysis.** Red cells are damaged by bypass and by flow through stent grafts or a partly thrombosed false lumen; free haemoglobin is toxic to the tubules."),
  ],
  mimic=[
    ("Wine-coloured urine: haemolysis vs rhabdomyolysis", "Both are dipstick-positive for blood without red cells; pink plasma and high free Hb point to haemolysis, a very high CK to rhabdomyolysis (limb ischaemia)."),
  ],
  traps=[
    ("“Once the ascending aorta is replaced, malperfusion resolves”", "Distal false-lumen flow can persist; a rising lactate needs a repeat CT."),
  ],
  decode=[
    ("Rising lactate after type A repair [pattern]", "Persisting mesenteric malperfusion: repeat CT."),
  ],
  punch="After repair, keep looking for the old complications: lactate for the gut, four pulses for the limbs, neurology for the brain and cord, platelets and urine colour for consumption and haemolysis.",
)

L['AD-27'] = dict(
  sub="Cardiology → Aortic dissection → Type B: medical vs TEVAR",
  step=6,
  intro="Step 6: type B splits by whether it is complicated. Not asked directly, but the notes contradict themselves, and the population resolves it.",
  parts=[
    ('a', "**MEDICAL: anti-impulse therapy.** Beta-blocker to HR about 60, SBP below 120, analgesia, then oral beta-blockers after 24 hours if the gut works (ESC 2024)."),
    ('b', "**TEVAR (2024 ESC I/B with favourable anatomy); open surgery the alternative.** For complicated type B (rupture, malperfusion, refractory pain or hypertension, rapid expansion), TEVAR is first line (I, B)."),
    ('c', "**Favourable anatomy → TEVAR in the SUBACUTE phase (IIa/B).** ESC 2024: in selected uncomplicated patients with high-risk features (aorta >40 mm, false lumen >20 mm, entry tear >10 mm), TEVAR between 14 and 90 days (the ESC subacute phase, not IRAD’s 8–30 days, AD-08) improves aortic remodelling."),
    ('d', "**Stent graft seals the entry tear → false lumen obliterates over time.** Covering the entry stops flow into the false lumen, which thromboses and shrinks while the true lumen expands."),
    ('e', "**Only if unsuitable for endovascular repair (higher morbidity and mortality): midline sternotomy or posterolateral thoracotomy, often on CPB.** Open descending repair carries more paraplegia, renal failure and death."),
  ],
  mimic=[
    ("Uncomplicated vs complicated type B", "Uncomplicated: drugs (± TEVAR later if high risk); complicated: TEVAR now."),
  ],
  traps=[
    ("“The primary treatment of type B is TEVAR”", "Only when complicated or high-risk; uncomplicated type B is medical first."),
  ],
  decode=[
    ("Type B with malperfusion or rupture [pattern]", "TEVAR (I, B)."),
    ("Uncomplicated type B with an aorta of 45 mm [pattern]", "Medical, then consider TEVAR at 14–90 days (IIa, B)."),
  ],
  punch="Uncomplicated type B is treated with drugs, complicated type B with TEVAR at once, and high-risk uncomplicated type B with TEVAR in the subacute window; open surgery is the fallback.",
)

L['AD-28'] = dict(
  sub="Cardiology → Aortic dissection → Spinal cord protection",
  step=6,
  intro="Step 6: covering or replacing the descending aorta can cut off the intercostal supply to the cord, so cord perfusion pressure is protected from both sides. Not asked directly, but the top-up on spinal drain anticoagulant holds comes from a TEVAR stem.",
  parts=[
    ('a', "**Hypothermia, distal aortic perfusion, CSF drainage.** Hypothermia lowers cord oxygen demand; distal (left heart) bypass keeps the lower body perfused while the aorta is clamped; CSF drainage lowers the pressure opposing cord blood flow."),
    ('b', "**15 mL/h.** Protocols usually cap drainage at about 15–20 mL/h; draining faster risks intracranial hypotension and subdural haematoma."),
    ('c', "**CSF pressure <10 mmHg; <5 mmHg if signs of paraplegia.** Spinal cord perfusion pressure is MAP minus CSF pressure (or CVP if higher). Protocols typically keep it at about 10 mmHg (range 8–12) and drain further if a deficit appears, while raising the MAP (often above 80–100 mmHg; ESC 2024 recommends a higher MAP in spinal ischaemia)."),
    ('d', "**Intercostal vessels T8–T12 → artery of Adamkiewicz.** The great radicular artery feeds the anterior spinal artery, which supplies the anterior two thirds of the lower thoracic and lumbar cord; reattaching its intercostal origin preserves the anterior spinal circulation."),
    ('e', "**Hb >10 g/dL, cardiac index >2.5 L/min/m².** Oxygen delivery to a cord with marginal collateral flow depends on both."),
  ],
  mimic=[
    ("Raising MAP vs lowering CSF pressure", "Both raise cord perfusion pressure; they are used together."),
  ],
  traps=[
    ("“Drain the CSF as fast as possible when paraplegia appears”", "Drain to target but within the hourly limit; rapid drainage causes subdural haematoma."),
  ],
  decode=[
    ("New leg weakness after TEVAR — immediate steps? [pattern]", "Raise MAP, drain CSF to <10 (lower if needed), keep Hb and cardiac index up."),
  ],
  punch="Cord perfusion pressure is MAP minus CSF pressure, so protect the cord by keeping the MAP high and draining CSF to below 10 mmHg at no more than about 15 mL/h, with good Hb and cardiac output.",
)

L['AD-29'] = dict(
  sub="Cardiology → Aortic dissection → Complications",
  step=6,
  intro="Step 6 closes the deck by listing every way dissection kills; each one traces back to rupture or malperfusion (step 2). Not asked directly.",
  parts=[
    ('a', "**~120 mmHg: protects the surgical sites.** Systolic pressure is kept near 120 after type B repair to protect the anastomoses and stent seal and to limit stress on any residual false lumen, while keeping the spinal cord and kidneys perfused."),
    ('b', "**Stroke (impaired cerebral perfusion); spinal cord involvement (paraplegia or hemisensory loss); MI (coronary compromise); cardiac tamponade (aortic root involvement); severe aortic regurgitation; AKI; gut ischaemia.** The first five come from the ascending aorta and arch (type A); spinal, renal and gut ischaemia come from the descending and abdominal aorta. Rupture underlies tamponade, and every other item is malperfusion or valve failure."),
  ],
  mimic=[
    ("Type A vs type B complications", "Type A: tamponade, AR, MI, stroke. Type B: paraplegia, AKI, gut and limb ischaemia."),
  ],
  traps=[
    ("“Tamponade and AR can complicate a type B dissection”", "Only if it extends back into the ascending aorta, which makes it type A."),
  ],
  decode=[
    ("Commonest cause of death in type A [pattern]", "Rupture into the pericardium (tamponade)."),
  ],
  punch="Every complication of dissection is either rupture or malperfusion, and the segment involved decides which ones can happen.",
)

FLAGS = {
  'AD-09': "Card is correct. DocT GT2o pairing question has two wrong pairings (A: DeBakey II with visceral malperfusion, and C: DeBakey III with AR); DocT keys A. The trap says so.",
  'AD-14': "Card is correct. The linked DocT QBank question keys TEE for a stable patient (BP 205/110); ESC 2024 makes ECG-gated CT first line (I, C). Exam-day answer: CT. Same note on AD-17.",
  'AD-16': "a: ‘Widened mediastinum 50%’ is low: IRAD (Hagan 2000) gives widened mediastinum 61.6%, abnormal aortic contour 49.6%, normal X-ray 12.4%. The explanation gives the IRAD figures.",
  'AD-18': "b: HR <60 matches ESC 2024 (≤60, I, B); ACC/AHA 2022 gives 60–80 (the watch line says so). Not an error; the explanation gives both.",
  'AD-20': "b: labetalol repeat bolus ‘20–80 mg every 10 min’; the label gives 40–80 mg every 10 min (after the first 20 mg), to a total of 300 mg. Minor; the explanation gives the label figures.",
  'AD-21': "Card is correct. DocT GT GrandT1 keys nitroglycerin for cyanide toxicity (almond breath after high-dose infusion); the correct answer is nitroprusside (GT3 and AIM2 repeats agree). The QBank ‘urinary thiocyanate’ key is imprecise (serum level), but still the best option.",
  'AD-23': "Card is correct (2013 consensus grades). The linked DocT GT question uses the accidental/clinical scale (30 °C = moderate); the explanation sets the two scales side by side.",
  'AD-27': "c: ‘Subacute phase’ here is the ESC 2024 window of 14–90 days, not the IRAD subacute class on AD-08 (8–30 days). The explanation says so.",
}
