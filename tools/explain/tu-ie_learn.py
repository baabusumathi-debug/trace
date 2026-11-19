# TU-IE — Explain v3 ("Learn" depth): infective endocarditis — organism by setting, recognition and work-up, Duke-ISCVID 2023 (criteria and a worked case), embolic and immune
# complications, perivalvular abscess and heart block, acute AR bridge, ESC 2023 surgical indications and timing, neurological events, empirical and organism-specific antibiotics
# (streptococci, S. aureus, enterococci, Gram-negatives, fungi and culture-negative IE).
# No mnemonics or hooks. qpack/TU-IE.md links no question to any card (it is a Top-up deck), so every card gets the short treatment. The deck was built from bank questions listed in
# out/tudecks/TU-IE_input.json (note: the file is at /home/claude/map/out/tudecks/, not /home/claude/out/tudecks/); their stems, keys and cohort % were read from
# map/doct_gt_distinct_all.jsonl, map/doct_qbank_all.jsonl and map/QMap_full_932.csv (Marrow, short stems only) and used as tagged decode items and traps where they map.
# DocT GT CGT6 Q119 is not in the GT file; its key (vancomycin) is taken from the card’s watch line and the round-2 key note.
# No `fix` entries in trace/test/data/qbank.json, no card-layer lines in cvs_cardlayer.json and no Top-ups in cvs_topups.json for TU-IE (checked 19 Nov 2026), so no topups file.
# Checked online on 19 Nov 2026:
#  - Duke-ISCVID 2023 (Fowler, Clin Infect Dis 2023; MSD Manual table; JournalFeed summary): typical organisms (S. aureus, S. lugdunensis, E. faecalis, streptococci except pneumoniae/pyogenes,
#    Granulicatella, Abiotrophia, Gemella, HACEK; with intracardiac prosthetic material also CoNS, Corynebacterium striatum/jeikeium, Serratia, P. aeruginosa, Cutibacterium, M. chimaera, Candida)
#    in ≥2 sets, non-typical in ≥3; Coxiella phase I IgG >1:800 or one positive culture; Bartonella IFA IgG ≥1:800; PCR for Coxiella, Bartonella, Tropheryma; echo and/or cardiac CT lesions; new
#    significant regurgitation (worsening of pre-existing is not enough); new partial dehiscence; PET-CT major ≥3 months after implantation, minor within 3 months; surgical criterion. Minor:
#    predisposition (prior IE, prosthesis, prior repair, congenital, more than mild regurgitation or stenosis of any cause, CIED, HOCM, injection drug use), fever ≥38.0 °C, vascular, immunological,
#    microbiology short of major. Definite 2M, 1M+3m, 5m (or pathological); possible 1M+1m or 3m; rejected: firm alternative diagnosis, resolution or no IE at surgery/autopsy with <4 days of antibiotics.
#  - ESC 2023 endocarditis guideline (Delgado, Eur Heart J 2023; ACC key points; Rev Esp Cardiol commentary; Udine review): ≥3 blood-culture sets, 10 mL, peripheral vein, 30-min intervals, before
#    antibiotics; TTE first, TEE if TTE negative, prosthetic valve, before oral switch; repeat TTE/TEE in 5–7 days; cardiac CTA and PET-CT for possible PVE. Surgery: emergency <24 h (refractory oedema or
#    shock), urgent 3–5 days (HF; locally uncontrolled infection incl. new AV block; vegetation ≥10 mm after ≥1 embolic episode, or ≥10 mm with another indication — Class I); isolated vegetation ≥10 mm,
#    low risk, IIb; no separate 30 mm threshold found in 2023; persistent positive cultures >1 week despite therapy and source control ‘should be considered’ (IIa); fungal/multiresistant urgent or non-urgent.
#    Right-sided surgery: acute severe TR with RV dysfunction, recurrent pulmonary emboli needing ventilation, residual vegetation >20 mm, left-sided involvement. Neurology: surgery without delay after
#    TIA or non-haemorrhagic stroke (Class I B); significant ICH: delay ≥4 weeks (>1 month), earlier if unstable and meaningful neurological recovery likely (IIa); endovascular therapy for infective
#    aneurysm when treatment indicated. Empirical: community NVE/late PVE ampicillin + ceftriaxone or (flu)cloxacillin + gentamicin (IIa C); penicillin allergy cefazolin or vancomycin + gentamicin
#    (IIb C); early PVE/healthcare-associated vancomycin or daptomycin + gentamicin + rifampicin (IIb C); doses ampicillin 12 g/day, ceftriaxone 4 g/day in 2 doses, cloxacillin 12 g/day, cefazolin 6 g/day,
#    vancomycin 30 mg/kg/day, daptomycin 10 mg/kg/day. No aminoglycoside in staphylococcal NVE; rifampicin only with foreign material, after 3–5 days; PVE ≥6 weeks; 2-week right-sided MSSA course only if
#    prompt response, vegetation ≤20 mm, no metastatic, left-sided or prosthetic involvement, no glycopeptide.
#  - POET (Iversen, NEJM 2019; ACC trial summary): n 400 stable left-sided IE (streptococci, E. faecalis, S. aureus, CoNS) after ≥10 days IV; composite at 6 months 9.0% oral vs 12.1% IV (non-inferior);
#    median 3.5 years 26.4% vs 38.2%, all-cause mortality 16.4% vs 27.1%.
#  - AHA (MedLink review of AHA stroke guidance): no IV alteplase in suspected IE; thrombectomy reasonable for large-vessel occlusion case by case.
# Second-check review 19 Nov 2026 (see tu-ie_review.md): ESC 2023 surgery and antithrombotic rows confirmed from a lecture reproduction of the guideline tables and the J Cardiothorac Surg 2024 and
# Rev Esp Cardiol commentaries; web search budget ran out before the 2023 antibiotic tables could be re-read, so those rest on the writer’s check and the reviewer’s knowledge.
# From standard references without a fresh check (confident unless said): AHA 2015 IE statement (Baddour) — viridans MIC bands ≤0.12, >0.12 to <0.5, ≥0.5 (treat as enterococcal), ceftriaxone alone
# acceptable for relatively resistant ceftriaxone-susceptible strains when gentamicin is unsafe; culture-negative early PVE vancomycin + rifampicin + gentamicin + cefepime; Pseudomonas combination with
# high-dose tobramycin (8 mg/kg/day), ≥6 weeks; HACEK ceftriaxone 4 weeks; enterococcal 4 vs 6 weeks by symptom duration >3 months. ESC 2015/2023 Coxiella (doxycycline + hydroxychloroquine ≥18 months),
# Bartonella (doxycycline 4 weeks + gentamicin 2 weeks), Candida (liposomal amphotericin ± flucytosine or high-dose echinocandin, surgery, fluconazole suppression), UFH for 1–2 weeks after ischaemic
# stroke on a mechanical valve (weak recommendation; less sure of the 2023 class). Organism frequencies from the GT2o Q124 explanation (S. aureus 31%, viridans 17%, non-HACEK Gram-negatives 2%).

SPINE = [
  ("The setting names the organism", "Who the patient is and how fast the illness moves predict the bug before cultures return: days and destruction mean S. aureus, weeks on a damaged valve mean streptococci, the first year after valve surgery means hospital organisms."),
  ("Proving it: cultures, echo, Duke", "Three sets of cultures before antibiotics and an echo feed the Duke-ISCVID count, where a typical organism needs two sets, a rare one three, and definite means two major, one major plus three minor, or five minor."),
  ("What the vegetation destroys", "A vegetation throws emboli to brain, spleen and lung, drives immune complexes, burrows into the annulus to cause abscess and heart block, and can wreck a valve in days."),
  ("When the surgeon must come", "Surgery treats what antibiotics cannot (a failed valve, walled-off infection, a vegetation that keeps embolising), timed as emergency, urgent or non-urgent, and only a bleed in the brain usually makes it wait."),
  ("Killing the organism", "Treatment is long, bactericidal and chosen by organism and valve: beta-lactams first, gentamicin only where it adds synergy, rifampicin only on prosthetic material, combinations where one drug selects resistance."),
]

PRIMER = "Infective endocarditis is infection of the endocardium, usually a valve, where platelets, fibrin and organisms build a vegetation on endothelium that has been damaged (by a jet, a prosthesis, a catheter or injected particles) or, for S. aureus, sometimes on a normal valve. The vegetation sits in fast-moving blood but has no blood supply of its own, so organisms inside it reach huge densities and are killed slowly; that is why treatment is long, bactericidal and often combined. Native-valve (NVE) and prosthetic-valve IE (PVE: early under 12 months after surgery, late after that), and right- vs left-sided IE, behave differently throughout this deck. Management follows the ESC 2023 guideline; diagnosis follows the 2023 Duke-ISCVID criteria."

L = {}

L['IE-01'] = dict(
  sub="Infective endocarditis → Recognition → Organism by setting",
  step=1,
  intro="Step 1 starts with the organism, because the setting predicts it before cultures return and the organism then sets the tempo, the complications and the regimen. The bank question behind this card gives a rheumatic valve with five days of fever and shock, and only a fifth of the cohort chose S. aureus.",
  parts=[
    ('a', "**Acute (days, sepsis, new severe regurgitation, Janeway lesions) → S. aureus: commonest overall (~30%), also on rheumatic or damaged valves.** S. aureus binds both normal and damaged endothelium through surface adhesins and destroys a leaflet within days. The tempo outweighs the substrate: a rheumatic valve does not make it streptococcal when the course is five days and the patient needs pressors."),
    ('b', "**IVDU, right-sided (tricuspid) → S. aureus; less often Pseudomonas, Candida.** Skin flora is injected straight into the venous return to the tricuspid valve; contaminated water and diluents bring Pseudomonas and Candida."),
    ('c', "**Subacute on a damaged native valve after dental work → viridans streptococci.** They need a ready-made fibrin–platelet nidus on an abnormal valve and are not destructive, so they cause weeks of low-grade fever, not shock."),
    ('d', "**Elderly after a GU or GI procedure → enterococci (E. faecalis); S. gallolyticus (bovis) → colonoscopy.** S. gallolyticus bacteraemia is linked to colonic neoplasia, so the colon is examined even without bowel symptoms."),
    ('e', "**Early prosthetic valve (<12 months) → CoNS, S. aureus, Gram-negatives, Candida.** These are acquired around the operation or in hospital and live in biofilm on the sewing ring. After 12 months the spectrum returns to that of native-valve IE."),
    ('f', "**Blood culture-negative → prior antibiotics (commonest); HACEK, Coxiella, Bartonella, Brucella, Tropheryma.** These are fastidious or intracellular organisms that grow slowly or not at all in routine bottles, so they are found by serology, PCR or valve tissue (IE-15)."),
  ],
  mimic=[
    ("S. aureus vs viridans streptococci", "Days, shock and a newly destroyed valve vs weeks of low-grade fever on an already abnormal valve."),
    ("Early vs late PVE", "Under 12 months: hospital organisms (CoNS, S. aureus, Gram-negatives, Candida); later: the native-valve spectrum."),
  ],
  traps=[
    ("“Rheumatic valve, so viridans streptococcus” (DocT GT2o Q124: only 20% chose S. aureus)", "The predisposition tells you where IE settles, not which organism. Five days of fever, Janeway lesions, a newly severe MR and rising pressors are the S. aureus tempo."),
    ("“CoNS in the blood after valve surgery is a contaminant”", "On a prosthetic valve within a year it is a leading cause, and Duke-ISCVID counts CoNS as a typical organism when intracardiac prosthetic material is present."),
  ],
  decode=[
    ("Rheumatic MS, 5 days of fever, plantar lesions, newly severe MR, rising pressors: most likely organism? [DocT GT2o Q124, 20%]", "S. aureus: an acute, destructive course whatever the substrate."),
    ("Fever and positive cultures 3 weeks after valve replacement: likely organism? [pattern]", "CoNS or S. aureus (early PVE)."),
  ],
  punch="The tempo names the organism: days and destruction mean S. aureus, weeks on a damaged valve mean viridans streptococci, and the first year after valve surgery means hospital organisms.",
)

L['IE-02'] = dict(
  sub="Infective endocarditis → Recognition → Right-sided IE and the work-up",
  step=1,
  intro="Step 1 continues with recognition: the drug user with fever, a murmur and lung shadows. The DocT question behind this card was answered well (85%); the teaching point is why its ‘four sets’ is still the only sensible option, and what the work-up order is.",
  parts=[
    ('a', "**Right-sided (tricuspid) IE; infiltrates = septic pulmonary emboli; new AV block = suspect perivalvular extension.** Tricuspid vegetations shed into the pulmonary arteries and give multiple peripheral nodules that often cavitate, so the lung picture is the valve’s embolic shadow, not a primary pneumonia. New AV block means infection may have spread into the annulus near the conduction tissue, or that the aortic valve is involved as well (IE-06); TEE answers both."),
    ('b', "**3 sets of blood cultures before antibiotics; TTE first, TEE if TTE negative, prosthetic valve or device, or complication suspected; repeat TTE/TEE in 5–7 days if still suspected; PET-CT or cardiac CT for an equivocal prosthetic valve; then empirical IV antibiotics.** ESC 2023 asks for at least three sets, 10 mL each, from a peripheral vein at 30-minute intervals: the bacteraemia is continuous, so separate sets prove persistence and three catch nearly all cases. TEE is advised even after a positive TTE because TTE misses abscess and perforation, except for good-quality TTE of isolated right-sided native IE. A stable patient can wait for cultures; a septic one is treated as soon as they are drawn."),
  ],
  mimic=[
    ("Septic emboli vs pneumonia", "Multiple peripheral, often cavitating nodules in a drug user with a murmur vs a single lobar consolidation."),
  ],
  traps=[
    ("“Four sets of blood cultures” (DocT Specific Cardiac Diseases Q9 key)", "ESC 2023 says at least three sets; the keyed option is still right because it is the only one that pairs cultures, echo and antibiotics."),
    ("“Start antibiotics first, culture later”", "Prior antibiotics are the commonest cause of culture-negative IE; in a stable patient cultures always come first."),
  ],
  decode=[
    ("IVDU, fever 3 days, murmur, bilateral infiltrates, first-degree block: next step? [DocT Specific Cardiac Diseases Q9, 85%]", "Blood cultures, TTE, antibiotics; the monospot, NSAID-for-pericarditis and isoniazid options ignore the murmur."),
    ("Suspected IE, TTE negative, suspicion still high: next? [pattern]", "TEE; if negative, repeat TTE/TEE in 5–7 days."),
  ],
  punch="In a febrile drug user with a murmur, lung infiltrates are tricuspid emboli and new AV block is spread into the annulus; culture three times before antibiotics, then image TTE first and TEE next.",
)

L['IE-03'] = dict(
  sub="Infective endocarditis → Diagnosis → Duke-ISCVID 2023 criteria",
  step=2,
  intro="Step 2 is proof. The 2023 Duke-ISCVID criteria turn the bedside picture into ‘definite’, ‘possible’ or ‘rejected’; the bank questions test the thresholds (how many sets, which organism, how to count), not the list.",
  parts=[
    ('a', "**Major: typical organism in ≥2 sets, non-typical (e.g. E. coli) in ≥3; Coxiella phase I IgG >1:800; Bartonella IgG ≥1:800; positive PCR; imaging (vegetation, abscess, perforation, pseudoaneurysm, fistula, new dehiscence on echo or cardiac CT; PET-CT uptake >3 months after surgery; new regurgitation on echo); IE seen at operation.** The typical organisms are so specific for IE that two sets are enough; anything else needs three to exclude contamination or another source. With intracardiac prosthetic material, ISCVID also counts CoNS, Corynebacterium striatum/jeikeium, Serratia, Pseudomonas aeruginosa, Cutibacterium, M. chimaera and Candida as typical. PET-CT within 3 months of surgery is only minor, because healing tissue around the sewing ring takes up FDG too."),
    ('b', "**Minor: predisposition (prosthesis, prior IE, RHD, IVDU, CIED, HCM, congenital), fever >38 °C, vascular, immunological, microbiology not meeting major.** ISCVID words the valve predisposition as ‘more than mild regurgitation or stenosis of any cause’, which is why rheumatic MS/MR counts. A culture that fails the major threshold is not discarded; it becomes a minor criterion (IE-04)."),
    ('c', "**Definite = 2 major, 1 major + 3 minor, or 5 minor; possible = 1 major + 1 minor, or 3 minor.** Definite can also be pathological (organisms or active IE in a vegetation, valve or embolus). ‘Rejected’ needs a firm alternative diagnosis, resolution (or no IE at surgery or autopsy) after under 4 days of antibiotics, or failure to reach ‘possible’."),
  ],
  mimic=[
    ("Duke-ISCVID 2023 vs modified Duke (2000)", "2023 adds cardiac CT and PET-CT as major imaging, the surgical criterion, PCR, and CIED/HCM/IVDU predispositions; the arithmetic for definite and possible is unchanged."),
    ("PET-CT major vs minor", "More than 3 months after implantation: major; within 3 months: minor."),
  ],
  traps=[
    ("“Worsening of a known murmur is a major criterion”", "Only new regurgitation on echo is major; worsening of existing regurgitation does not count, and a new murmur on auscultation is minor and only when echo is unavailable."),
    ("“Any organism in two sets is major”", "Two sets only for typical organisms; E. coli and other rare causes need three."),
  ],
  decode=[
    ("Count majors and minors and classify (definite, possible, rejected) [DocT GT6 Q3; worked in IE-04]", "2 major, 1 major + 3 minor, or 5 minor = definite."),
    ("Which imaging became a major criterion in 2023? [pattern]", "Cardiac CT, and [18F]FDG PET-CT more than 3 months after surgery."),
  ],
  punch="Two sets for a typical organism, three for a rare one; a culture that fails as major still counts as minor; definite is two major, one major plus three minor, or five minor.",
)

L['IE-04'] = dict(
  sub="Infective endocarditis → Diagnosis → Worked Duke-ISCVID case",
  step=2,
  intro="Step 2 applied to the bank’s own case, where about half the cohort (54%) followed a key that miscounts. The parts follow the table’s rows.",
  parts=[
    ('a', "**Major (imaging): 10 mm vegetation on TEE.** A mobile vegetation on echo is a major criterion on its own."),
    ('b', "**Micro major? No: E. coli is non-typical → needs ≥3 sets.** Two of three is not enough because non-HACEK Gram-negatives rarely cause IE, and the stem’s pyuria offers a urinary source that can seed the blood transiently."),
    ('c', "**Minor 1, 2, 3: rheumatic MS/MR (predisposition), fever >38 °C, and a positive culture not meeting major.** The failed microbiology criterion drops to minor instead of disappearing; that is the step the key misses."),
    ('d', "**Total: 1 major + 3 minor = DEFINITE IE.** ‘Rejected’ would need an alternative diagnosis that explains everything; a urinary infection does not explain a 10 mm mobile vegetation."),
  ],
  mimic=[
    ("E. coli in 2 sets vs viridans streptococci in 2 sets", "E. coli: minor only; viridans streptococci: major (typical), making this 2 major."),
  ],
  traps=[
    ("“Possible endocarditis” (DocT GT6 Q3 key; 54% chose it)", "By Duke-ISCVID this is definite (1 major + 3 minor). The key looks wrong; answer ‘definite’ unless that option is absent."),
    ("“E. coli is never a cause of endocarditis”", "Non-HACEK Gram-negatives cause about 2% of IE; being rare is why E. coli needs three sets, not a reason to exclude it."),
  ],
  decode=[
    ("RHD, AF, fever on and off for 2 months, dental extractions, E. coli in 2 of 3 sets, 10 mm mobile vegetation on TEE: what is true? [DocT GT6 Q3, 54%]", "Definite IE (1 major + 3 minor), despite the key."),
    ("Same case with viridans streptococci in 2 sets [pattern]", "2 major = definite."),
  ],
  punch="The vegetation is one major; RHD, fever and the E. coli cultures that fail as major are three minors; one major plus three minor is definite.",
)

L['IE-05'] = dict(
  sub="Infective endocarditis → Complications → Emboli and immune phenomena",
  step=3,
  intro="Step 3: what the vegetation does once it is there. It throws fragments into the circulation and keeps releasing antigen into the blood; the bank questions give the embolic or immune picture and ask for the one diagnosis behind it.",
  parts=[
    ('a', "**Brain (~20–40%): stroke, multiple ring-enhancing abscesses at the grey–white junction, mycotic aneurysm → ICH/SAH; spleen: infarct or abscess; lung: septic emboli from right-sided IE; also limbs, kidney, mesentery, coronary.** Left-sided fragments go wherever arterial flow takes them, and the brain is the commonest symptomatic target; emboli lodge where arteries narrow, at the grey–white junction. An infected embolus in a distal artery weakens its wall and forms a mycotic aneurysm, which can bleed."),
    ('b', "**Embolic risk: vegetation >10 mm (>30 mm very high), mobile, mitral (anterior leaflet), S. aureus, Candida, prior embolism; highest before and in the first 2 weeks of antibiotics.** Effective therapy sterilises and organises the vegetation, so risk falls steeply after two weeks; that is why surgery to prevent embolism is decided early (IE-08)."),
    ('c', "**Immune complications: immune-complex GN (red-cell casts, low complement), Osler nodes, Roth spots, arthritis, positive RF.** Continuous antigen release forms circulating immune complexes that deposit in glomeruli (consuming complement), skin and retina."),
  ],
  mimic=[
    ("Osler nodes vs Janeway lesions", "Painful pulp nodules (immunological minor) vs painless palmar or plantar macules (vascular minor)."),
    ("IE vs systemic vasculitis", "Fever, a murmur, positive cultures and emboli point to IE; vasculitis does not make vegetations."),
  ],
  traps=[
    ("“Vasculitis” for IVDU + apical murmur + stroke + red-cell casts (Marrow QB25-Q28)", "Septic emboli and immune-complex GN from left-sided (mitral) IE explain every finding."),
    ("“Tuberculoma or glioma” for multiple ring-enhancing lesions in a febrile heroin user (DocT Substance-Related (Part 1) Q18, 87%)", "Multiple lesions with acute fever and hemiparesis are septic embolic abscesses; tuberculoma is subacute and usually single or few."),
  ],
  decode=[
    ("IVDU, fever, apical murmur, stroke, red-cell casts: cause? [Marrow QB25-Q28]", "Septic emboli from IE."),
    ("RHD, fever, arthralgia, confusion: suspect? [Marrow QB23-Q12]", "Acute infective endocarditis."),
    ("IV heroin, fever, altered sensorium, hemiparesis, multiple ring-enhancing lesions [DocT Substance-Related (Part 1) Q18, 87%]", "Brain abscesses from septic emboli of IE."),
  ],
  punch="A fever with emboli in several beds plus nephritis is one disease: the vegetation throws fragments and immune complexes, most dangerously in the first two weeks.",
)

L['IE-06'] = dict(
  sub="Infective endocarditis → Complications → New heart block = root abscess",
  step=3,
  intro="Step 3 also covers spread beyond the leaflet. Two bank questions give new heart block in endocarditis and offer ‘continue antibiotics’ or ‘wait 6 weeks’. The parts follow the card’s bullets.",
  parts=[
    ('a', "**New AV block = perivalvular (aortic-root) abscess eroding the conduction system near the AV node/His bundle.** The His bundle runs under the membranous septum, beneath the commissure between the non-coronary and right coronary cusps, so infection spreading from the aortic annulus there blocks conduction. New block in aortic IE is a specific marker of abscess, though many abscesses never cause it."),
    ('b', "**TEE to define abscess, fistula, pseudoaneurysm.** TTE misses about half of root abscesses; ESC 2023 asks for repeat imaging (TEE, or cardiac CT) whenever a new complication is suspected."),
    ('c', "**Urgent surgery (within 3–5 days): locally uncontrolled infection; antibiotics cannot sterilise an abscess.** A pus cavity has no blood supply, so drugs do not reach it and fever persists. ESC 2023 makes this a Class I urgent indication, native or prosthetic."),
    ('d', "**Temporary pacing as needed; daily ECG in aortic IE to catch it early.** Mobitz II and complete block are infranodal and unstable. ESC 2023 also advises epicardial pacing at surgery when complete block is present with a predictor that it will persist."),
  ],
  mimic=[
    ("Root abscess vs drug-induced AV block", "Abscess: aortic IE, still febrile, progressive block; drugs (beta-blocker, digoxin, calcium-channel blocker): no fever, no new echo lesion."),
  ],
  traps=[
    ("“Continue antibiotics alone” or “delay surgery 6 weeks” (DocT CGT6 Q118; Marrow QB25-Q10)", "Heart block with an abscess and persistent fever is uncontrolled infection: urgent surgery, Class I."),
  ],
  decode=[
    ("Aortic IE, day 3 of correct antibiotics, new Mobitz II: next step? [Marrow QB25-Q10]", "Surgical referral (root abscess)."),
    ("PVE, complete heart block, periannular abscess on TEE, still febrile: management? [DocT CGT6 Q118]", "Urgent valve surgery."),
  ],
  punch="In aortic endocarditis, new AV block means the infection has burrowed into the root beside the His bundle; image it with TEE and send for urgent surgery, because no antibiotic reaches an abscess.",
)

L['IE-07'] = dict(
  sub="Infective endocarditis → Complications → Acute severe AR: the bridge",
  step=3,
  intro="Step 3’s haemodynamic face: a valve destroyed in days. Only a fifth of the cohort chose the right drug in the bank question. The parts follow the card’s bullets.",
  parts=[
    ('a', "**Afterload reduction: nitroprusside (± dobutamine if hypotensive) to raise forward flow.** How much blood leaks back depends on the pressure behind the valve in diastole; lowering SVR lets more stroke volume go forward and lowers LV end-diastolic pressure and pulmonary pressure. A BP of 120/70 allows it, and nitroprusside can be titrated minute to minute."),
    ('b', "**Keep HR relatively fast (shorter diastole = less regurgitant time).** Bradycardia lengthens diastole and the time for backflow."),
    ('c', "**Avoid IABP (contraindicated in AR), beta-blockers, pure vasoconstrictors (norepinephrine raises regurgitation).** The balloon inflates in diastole and pushes more blood back through the open valve; beta-blockers remove the compensating tachycardia; vasoconstrictors raise the pressure driving the leak."),
    ('d', "**HF from acute valve destruction with shock or oedema = emergency surgery (<24 h).** ESC 2023 times this regardless of how long antibiotics have run; drugs only buy hours."),
  ],
  mimic=[
    ("Acute vs chronic AR", "Acute: normal-sized stiff LV, high LVEDP, early mitral closure, tachycardia, little widening of pulse pressure; chronic: dilated compliant LV, wide pulse pressure, tolerated for years."),
  ],
  traps=[
    ("“Norepinephrine or epinephrine” because the patient is sick (DocT GT2o Q60: only 20% chose nitroprusside)", "Raising afterload pushes more blood back into the LV; the blood pressure here does not need support."),
    ("“Furosemide”", "It eases congestion but does not increase forward flow; the leak is the problem."),
  ],
  decode=[
    ("IVDU, aortic vegetation, severe AR, pulmonary oedema, SpO2 85%, BP 120/70, awaiting surgery: next step? [DocT GT2o Q60, 20%]", "Nitroprusside."),
    ("Acute severe AR in shock: IABP as a bridge? [pattern]", "No, contraindicated; emergency surgery."),
  ],
  punch="In acute severe AR, unload the aorta (nitroprusside), keep the heart rate up, never use a balloon pump or a vasoconstrictor, and get the valve replaced within 24 hours.",
)

L['IE-08'] = dict(
  sub="Infective endocarditis → Surgery → ESC 2023 indications by timing",
  step=4,
  intro="Step 4: when antibiotics are not enough. ESC 2023 groups indications by reason (heart failure, uncontrolled infection, embolism) and timing (emergency <24 h, urgent 3–5 days, non-urgent during the same admission). The parts follow the table’s rows.",
  parts=[
    ('a', "**Emergency (<24 h): HF with cardiogenic shock or pulmonary oedema from severe acute regurgitation, obstruction or fistula.** This is a mechanical failure that no drug can fix, so the length of antibiotic treatment does not matter (IE-07)."),
    ('b', "**Urgent (3–5 days): HF without shock; locally uncontrolled infection (abscess, pseudoaneurysm, fistula, enlarging vegetation, new AV block).** ESC 2023 defines ‘urgent’ as 3–5 days (2015 said only ‘within a few days’). Walled-off infection is not reached by antibiotics (IE-06)."),
    ('c', "**Urgent: fungal or multiresistant organism; persistent bacteraemia despite correct antibiotics and source control.** Fungal and multiresistant IE are surgical because medical cure is rare (IE-15). ESC 2023 grades persistent positive cultures for more than a week, after metastatic foci are controlled, as ‘should be considered’ (IIa)."),
    ('d', "**Urgent: vegetation ≥10 mm + ≥1 embolic event on antibiotics (Class I).** Also Class I: a vegetation ≥10 mm with any other surgical indication. Embolic risk is highest early (IE-05), so the decision cannot wait for the course to finish."),
    ('e', "**Urgent (IIa): vegetation ≥10 mm + severe valve disease and low risk; vegetation ≥30 mm; S. aureus or non-HACEK Gram-negative PVE.** Only the last is still IIa in ESC 2023 (‘should be considered’, IIa C): these organisms rarely clear from prosthetic material. The vegetation rows are 2015 wording. In 2023 a vegetation ≥10 mm with any other surgical indication, which takes in severe valve disease, was upgraded to Class I; the separate 30 mm cut-off was dropped; and an isolated vegetation ≥10 mm without embolism or severe dysfunction, in a low-risk patient, ‘may be considered’ (IIb B; 2015 set this at >15 mm, IIb C)."),
  ],
  mimic=[
    ("Left- vs right-sided IE surgery", "Tricuspid IE is usually medical; ESC 2023 operates for RV failure from acute severe TR, recurrent pulmonary emboli needing ventilation, residual vegetation >20 mm, or left-sided involvement."),
  ],
  traps=[
    ("“Add a second antibiotic” for MRSA aortic IE with a splenic embolus on day 2 (Marrow QB25-Q24)", "Embolism with a vegetation is a surgical question: cardiothoracic opinion now."),
    ("“Finish 6 weeks of antibiotics before operating”", "Emergency and urgent timings run from the indication, not the course; operating on active infection is accepted."),
  ],
  decode=[
    ("MRSA aortic IE, splenic lesion on day 2: next step? [Marrow QB25-Q24]", "Cardiothoracic surgery consult for septic embolus."),
    ("Mechanical mitral valve, candidaemia, EF 35%: next step? [Marrow QB25-Q35]", "Antifungal plus early surgery (IE-15)."),
    ("Which IE indication needs surgery within 24 h? [pattern]", "Refractory pulmonary oedema or cardiogenic shock from valve failure."),
  ],
  punch="Operate within 24 hours for shock or oedema from a failed valve, within 3–5 days for heart failure, uncontrolled infection or a ≥10 mm vegetation that has embolised; antibiotics do not change those clocks.",
)

L['IE-09'] = dict(
  sub="Infective endocarditis → Surgery → Neurological events",
  step=4,
  intro="Step 4’s hardest call: the brain has been hit, and the operation needs full heparin and bypass. The answer depends on whether there is blood in the brain. The parts follow the card’s numbered points.",
  parts=[
    ('a', "**Any neuro symptom → CT/MRI brain ± CT/MR angiography (mycotic aneurysm, haemorrhage).** ESC 2023 recommends brain imaging in every symptomatic patient, because ischaemia and haemorrhage lead to opposite surgical timing."),
    ('b', "**No thrombolysis; thrombectomy may be considered for large-vessel occlusion.** Septic emboli inflame and weaken the arterial wall, so a lytic converts infarcts into bleeds; thrombectomy removes the clot without a systemic lytic."),
    ('c', "**Ischaemic stroke/TIA, no haemorrhage, not comatose + a surgical indication → operate without delay.** ESC 2023 Class I: bypass rarely turns a bland infarct into a bleed, while recurrent emboli and heart failure kill if surgery waits."),
    ('d', "**Intracranial haemorrhage → usually postpone surgery ≥4 weeks; earlier only if HF or uncontrolled infection forces it, weighing neuro prognosis.** Full heparinisation during bypass readily enlarges an existing bleed."),
    ('e', "**Coma or severe neurological damage → defer.** Surgery adds risk without a meaningful neurological outcome to gain."),
    ('f', "**ICH → stop all anticoagulation; ischaemic stroke on a mechanical valve → switch warfarin to UFH for 1–2 weeks; do not start aspirin or anticoagulants to prevent emboli.** Antithrombotics do not reduce IE emboli but do raise bleeding; UFH is short-acting and reversible if a bleed appears. ESC 2023 stops antiplatelets and anticoagulants in major bleeding (I C), but with a mechanical valve it restarts UFH as soon as possible after a haemorrhage, after team discussion (IIa C), because valve thrombosis is the other risk. The fixed ‘1–2 weeks’ of UFH after ischaemic stroke comes from ESC 2015; 2023 frames it as replacing the oral anticoagulant with closely monitored UFH."),
    ('g', "**Large or ruptured mycotic aneurysm → endovascular or neurosurgical repair, ideally before valve surgery.** Securing it first stops bypass heparin from making it bleed."),
  ],
  mimic=[
    ("Ischaemic vs haemorrhagic stroke in IE", "Ischaemic without coma: operate if indicated, without delay; haemorrhage: usually wait ≥4 weeks."),
  ],
  traps=[
    ("“Wait 2–4 weeks after any stroke”", "ESC 2023: a non-haemorrhagic stroke without coma does not delay indicated surgery (Class I)."),
    ("“Thrombolyse an IE stroke inside the window”", "Contraindicated: septic arteritis bleeds."),
  ],
  decode=[
    ("IE with acute ischaemic stroke, no haemorrhage on CT, an indication for surgery: timing? [pattern]", "Without delay."),
    ("IE with intracerebral haemorrhage, haemodynamically stable: timing? [pattern]", "Postpone surgery for about 4 weeks."),
    ("CT shows intraparenchymal bleed layering in the ventricles: most expected complication? [DocT Stroke (Part 2) Q16, 67%]", "Hydrocephalus; mycotic aneurysm is a cause to look for in IE, not the expected complication."),
  ],
  punch="Image the brain first: an ischaemic stroke without coma does not delay surgery, a haemorrhage usually delays it about four weeks, and IE strokes are never thrombolysed.",
)

L['IE-10'] = dict(
  sub="Infective endocarditis → Antibiotics → Empirical regimens",
  step=5,
  intro="Step 5 begins before the organism is known: the regimen follows the setting, the same split as IE-01. The parts follow the table’s rows.",
  parts=[
    ('a', "**Community NVE or late PVE (≥12 months): ampicillin + ceftriaxone, or ampicillin + (flu)cloxacillin + gentamicin.** This covers streptococci, enterococci (ampicillin + ceftriaxone act together, IE-13), HACEK (ceftriaxone) and, with cloxacillin, MSSA. ESC 2023 grades it IIa."),
    ('b', "**Penicillin allergy: vancomycin + ceftriaxone.** The ESC 2023 table lists cefazolin or vancomycin with gentamicin (IIb) for this group; see FLAGS."),
    ('c', "**Early PVE (<12 months) or healthcare-associated: vancomycin (or daptomycin) + gentamicin + rifampicin (rifampicin only for PVE).** Vancomycin covers MRSA and CoNS; rifampicin penetrates biofilm on prosthetic material but, given alone into a high inoculum, selects resistance, so ESC 2023 adds it after 3–5 days of effective therapy."),
    ('d', "**Culture-negative early PVE (AHA): vancomycin + gentamicin + cefepime + rifampicin.** Cefepime adds the hospital Gram-negatives that the ESC early-PVE regimen leaves to gentamicin."),
    ('e', "**Narrow to organism-specific therapy once cultures return.** In stable patients a later step-down to oral therapy is allowed: in POET (left-sided IE with streptococci, E. faecalis, S. aureus or CoNS, after ≥10 days IV) oral was non-inferior (composite 9.0% vs 12.1% at 6 months) and better at a median of 3.5 years. ESC 2023 asks for a TEE showing no progression before the switch."),
  ],
  mimic=[
    ("Early vs late PVE regimen", "Early: vancomycin-based with rifampicin and Gram-negative cover; late: the community native-valve regimen."),
  ],
  traps=[
    ("“Vancomycin + ceftriaxone” 4 weeks after mechanical AVR with negative cultures (DocT CGT5 Q56)", "Ceftriaxone misses Pseudomonas and many hospital Gram-negatives, and the pair has neither gentamicin nor rifampicin; early PVE needs MRSA, CoNS, biofilm and resistant Gram-negative cover: vancomycin, cefepime, gentamicin, rifampicin (AHA 2015)."),
    ("“Rifampicin from day 1”", "Added after 3–5 days, once the bacteraemia is controlled, or resistance emerges."),
  ],
  decode=[
    ("Fever and heart failure 4 weeks after mechanical AVR, cultures negative after antibiotics: broadest recommended empirical cover? [DocT CGT5 Q56]", "Vancomycin, cefepime, gentamicin, rifampicin."),
    ("Which IE patients may step down to oral antibiotics? [pattern]", "Stable left-sided IE after ≥10 days IV with no complication on TEE (POET)."),
  ],
  punch="Empirical cover follows the setting: ampicillin plus ceftriaxone for community and late prosthetic IE, vancomycin-based with gentamicin and later rifampicin for early prosthetic IE.",
)

L['IE-11'] = dict(
  sub="Infective endocarditis → Antibiotics → Viridans streptococci and S. gallolyticus",
  step=5,
  intro="Step 5 by organism, starting with oral streptococci. The questions turn on the penicillin MIC and the kidneys; two near-identical bank questions give different keys.",
  parts=[
    ('a', "**Penicillin-susceptible (MIC ≤0.125 mg/L): penicillin G, amoxicillin or ceftriaxone 2 g once daily, 4 weeks NVE, 6 weeks PVE (2-week beta-lactam + gentamicin only for uncomplicated NVE with normal kidneys).** A beta-lactam alone kills these strains reliably; the 2-week option trades two weeks of drug for aminoglycoside risk."),
    ('b', "**Relatively or fully resistant (MIC >0.125–2 mg/L): same beta-lactam 4 weeks + gentamicin for the first 2 weeks (PVE 6 weeks).** The beta-lactam damages the cell wall so the aminoglycoside gets in, which restores killing of less-susceptible strains. AHA 2015 uses three bands: ≤0.12, >0.12 to <0.5 (relatively resistant) and ≥0.5 (treat as enterococcal IE)."),
    ('c', "**Renal risk or elderly: ceftriaxone monotherapy 4 weeks (AHA: acceptable for MIC >0.12 to <0.5); avoids gentamicin.** This needs a ceftriaxone-susceptible isolate; killing stays good with once-daily dosing and no kidney toxicity."),
    ('d', "**Beta-lactam allergy: vancomycin 4 weeks (6 weeks PVE).** Vancomycin kills more slowly and is nephrotoxic, so it is kept for patients who cannot take a beta-lactam."),
  ],
  mimic=[
    ("Ceftriaxone alone vs vancomycin in CKD", "Ceftriaxone for the non-allergic patient; vancomycin only when beta-lactams cannot be given."),
  ],
  traps=[
    ("“Vancomycin” for S. mitis MIC 0.3 with CKD 4 (DocT CGT6 Q119 key)", "Wrong for a non-allergic patient; its twin CGT5 Q55 correctly keys ceftriaxone monotherapy. Vancomycin is only the answer if ceftriaxone is not offered."),
    ("“Penicillin + gentamicin” for MIC 0.3 with CKD 4", "Standard for the MIC, but gentamicin is unsafe in CKD 4."),
  ],
  decode=[
    ("71-year-old, native aortic IE, S. mitis penicillin MIC 0.3, CKD 4: preferred strategy? [DocT CGT5 Q55]", "Ceftriaxone monotherapy."),
    ("S. gallolyticus IE: what else must be done? [pattern]", "Colonoscopy."),
  ],
  punch="For oral streptococci, the MIC decides whether gentamicin is added and the kidneys decide whether it can be; ceftriaxone alone is the gentamicin-free choice, and vancomycin is for allergy only.",
)

L['IE-12'] = dict(
  sub="Infective endocarditis → Antibiotics → S. aureus regimens",
  step=5,
  intro="Step 5 for the commonest and most lethal organism. The DocT question behind this card offers vancomycin because it ‘covers everything’; for MSSA that is the wrong reason.",
  parts=[
    ('a', "**MSSA native valve: (flu)cloxacillin 12 g/day in 4–6 doses (oxacillin/nafcillin) or cefazolin 6 g/day in 3 doses, 4–6 weeks; no gentamicin.** Beta-lactams kill MSSA faster than vancomycin, and MSSA treated with vancomycin fails and kills more often. ESC 2023 does not recommend aminoglycosides in staphylococcal native-valve IE: no benefit, more kidney injury."),
    ('b', "**MRSA or true penicillin anaphylaxis: vancomycin 30–60 mg/kg/day (AUC 400–600) or daptomycin 10 mg/kg/day, 4–6 weeks.** ESC uses the high daptomycin dose (10 mg/kg) and advises a second agent with it (for example cloxacillin or fosfomycin) to prevent resistance. Daptomycin is inactivated by surfactant, so it fails in alveolar pneumonia; septic pulmonary emboli from right-sided IE are not a contraindication."),
    ('c', "**Prosthetic valve: anti-staphylococcal agent + rifampicin (≥6 weeks) + gentamicin 2 weeks.** Rifampicin is the drug that acts in biofilm; it starts after 3–5 days of effective therapy to avoid resistance."),
    ('d', "**Uncomplicated right-sided MSSA in IVDU: 2 weeks of (flu)cloxacillin can suffice.** ESC conditions: MSSA with a prompt clinical response, vegetation <20 mm, no metastatic infection, no left-sided or prosthetic involvement, no severe immunosuppression, and not with a glycopeptide."),
  ],
  mimic=[
    ("Cefazolin vs ceftriaxone for MSSA", "Cefazolin is an anti-staphylococcal first-choice drug; ceftriaxone is weaker against staphylococci."),
  ],
  traps=[
    ("“Vancomycin” for MSSA mitral IE with septic emboli and HF (DocT Antimicrobials Q5, 61%)", "Vancomycin kills MSSA slowly and penetrates vegetations poorly; oxacillin or nafcillin (or cefazolin) wins."),
    ("“Add gentamicin to MSSA native-valve IE”", "No benefit and more AKI; gentamicin belongs only to the prosthetic-valve regimen."),
  ],
  decode=[
    ("MSSA mitral IE, multiple septic emboli, worsening HF: most appropriate initial regimen? [DocT Antimicrobials Q5, 61%]", "Oxacillin or nafcillin."),
    ("Right-sided MSSA IE in an IVDU, prompt response, vegetation 12 mm: duration? [pattern]", "2 weeks of (flu)cloxacillin can suffice."),
  ],
  punch="MSSA is treated with an anti-staphylococcal beta-lactam, never vancomycin by choice; gentamicin and rifampicin belong only to prosthetic-valve S. aureus.",
)

L['IE-13'] = dict(
  sub="Infective endocarditis → Antibiotics → Enterococci",
  step=5,
  intro="Step 5: enterococci are slow to kill, so the question is always which partner to give with ampicillin, and for how long.",
  parts=[
    ('a', "**E. faecalis, no HLAR, normal kidneys: ampicillin/amoxicillin + gentamicin, 4 weeks NVE, 6 weeks PVE or symptoms >3 months (gentamicin may be limited to 2 weeks).** Ampicillin alone only inhibits enterococci; gentamicin, let in through the damaged wall, adds the killing."),
    ('b', "**HLAR or renal risk: ampicillin + ceftriaxone 2 g 12-hourly × 6 weeks (ESC 2023 Class I; avoids nephrotoxicity).** Ceftriaxone saturates PBP2/3 while ampicillin binds PBP4/5, so together they kill without an aminoglycoside, and ESC accepts it for non-HLAR strains too."),
    ('c', "**Beta-lactam allergy: vancomycin + gentamicin × 6 weeks.** It is the only combination left that kills, at the cost of two nephrotoxins."),
    ('d', "**VRE faecium: high-dose daptomycin (10–12 mg/kg) + ampicillin or fosfomycin; linezolid alternative.** E. faecium is usually ampicillin-resistant and intrinsically ceftriaxone-resistant; daptomycin is bactericidal, and a partner prevents daptomycin resistance."),
  ],
  mimic=[
    ("E. faecalis vs E. faecium", "Faecalis: ampicillin-susceptible, ampicillin + ceftriaxone works; faecium: often ampicillin- and vancomycin-resistant, daptomycin-based."),
  ],
  traps=[
    ("“Amoxicillin + ceftriaxone for 4 weeks” (DocT GrandT1 Q95, 41%)", "The combination is right but the course is 6 weeks; with only 4 weeks offered, ampicillin + gentamicin for 6 weeks is the best available answer."),
    ("“Ampicillin” or “tigecycline” for VRE faecium bacteraemia in shock (DocT Antimicrobials Q14, 58%)", "Faecium is usually ampicillin-resistant and tigecycline is bacteriostatic with low blood levels; daptomycin."),
  ],
  decode=[
    ("E. faecalis IE, penicillin MIC 4 mg/L, no HLAR: initial regimen? [DocT GrandT1 Q95, 41%]", "Ampicillin + gentamicin for 6 weeks."),
    ("VRE faecium bacteraemia, ventilated, on vasopressors: agent? [DocT Antimicrobials Q14, 58%]", "Daptomycin."),
  ],
  punch="Enterococci need two drugs to die: ampicillin with gentamicin, or ampicillin with ceftriaxone for 6 weeks when the kidneys or HLAR forbid gentamicin; faecium needs daptomycin.",
)

L['IE-14'] = dict(
  sub="Infective endocarditis → Antibiotics → Gram-negative IE",
  step=5,
  intro="Step 5: Gram-negatives cause few cases of IE, so the questions test the exceptions: combination for Pseudomonas even when it is susceptible, and the intrinsic resistance of Burkholderia.",
  parts=[
    ('a', "**Pseudomonas aeruginosa (IVDU): two active classes even if susceptible: high-dose anti-pseudomonal beta-lactam (cefepime 2 g 8-hourly, ceftazidime, extended-infusion pip-tazo) + aminoglycoside (tobramycin 8 mg/kg/day), ≥6 weeks; left-sided → early surgery, tricuspid often medical.** A vegetation holds a huge inoculum killed slowly, so one drug lets resistant mutants take over during treatment. Left-sided Pseudomonas IE rarely clears without surgery."),
    ('b', "**Burkholderia cepacia on a prosthetic valve: TMP-SMX or meropenem; intrinsically resistant to colistin and aminoglycosides.** Its modified lipopolysaccharide does not bind polymyxins, and efflux pumps with a poorly permeable outer membrane keep aminoglycosides out."),
    ('c', "**HACEK: ceftriaxone, 4 weeks NVE, 6 weeks PVE.** Some HACEK organisms make beta-lactamase, so ampicillin is unreliable; they are typical organisms under Duke-ISCVID."),
    ('d', "**Other non-HACEK Gram-negatives: early surgery + ≥6 weeks of beta-lactam + aminoglycoside (or quinolone).** Mortality is high with medical treatment alone; ESC 2023 lists non-HACEK Gram-negative PVE as an urgent-surgery indication (IIa)."),
  ],
  mimic=[
    ("Pseudomonas vs Burkholderia", "Pseudomonas: beta-lactam + aminoglycoside; Burkholderia: TMP-SMX or meropenem, never colistin or an aminoglycoside."),
  ],
  traps=[
    ("“Pip-tazo or meropenem monotherapy” because the isolate is susceptible (DocT Antimicrobials Q21, 74%)", "Endocarditis needs two active classes; cefepime + an aminoglycoside."),
    ("“Colistin” or “aminoglycoside” for Burkholderia (DocT GT6 Q141, 88%)", "It is intrinsically resistant to both."),
  ],
  decode=[
    ("IVDU, tricuspid IE, Pseudomonas susceptible to everything: initial regimen? [DocT Antimicrobials Q21, 74%]", "Cefepime + gentamicin."),
    ("Prosthetic mitral valve, on haemodialysis, Burkholderia cepacia: which antibiotic? [DocT GT6 Q141, 88%]", "Carbapenem or TMP-SMX."),
  ],
  punch="Gram-negative endocarditis is treated with two active classes and, if left-sided, early surgery; Burkholderia is the exception that ignores colistin and aminoglycosides.",
)

L['IE-15'] = dict(
  sub="Infective endocarditis → Antibiotics → Fungal and culture-negative IE",
  step=5,
  intro="Step 5 ends with what cultures miss or drugs cannot sterilise: Candida on prosthetic material, and the intracellular organisms behind culture-negative IE.",
  parts=[
    ('a', "**Candida PVE: liposomal amphotericin B 3–5 mg/kg/day ± flucytosine (or high-dose echinocandin) + urgent valve surgery, then lifelong oral fluconazole suppression if the valve cannot be removed.** Fungi build dense biofilm on prosthetic material that antifungals cannot clear, so medical treatment alone relapses; fungal IE is a Class I surgical indication."),
    ('b', "**Supporting test when cultures are negative: (1→3)-β-D-glucan (not cryptococcal antigen; galactomannan is for Aspergillus).** Glucan is in the cell wall of most fungi except Cryptococcus and the Mucorales; false positives come from haemodialysis membranes, albumin, immunoglobulin and surgical gauze."),
    ('c', "**Coxiella burnetii (Q fever): doxycycline + hydroxychloroquine ≥18 months; phase I IgG >1:800 is a major criterion.** Coxiella lives in the acidic phagolysosome where doxycycline is inactive; hydroxychloroquine raises the pH so doxycycline can kill it."),
    ('d', "**Bartonella: doxycycline 4 weeks + gentamicin 2 weeks.** B. quintana (homeless, body lice) and B. henselae (cats) are found by serology or PCR, rarely by culture."),
  ],
  mimic=[
    ("β-D-glucan vs galactomannan", "Glucan: Candida and most fungi; galactomannan: Aspergillus."),
  ],
  traps=[
    ("“Antifungal alone” or “echinocandin and wait” for Candida on a mechanical mitral valve (Marrow QB25-Q35)", "Antifungal plus early surgery; biofilm is not sterilised by drugs."),
    ("“Galactomannan” or “cryptococcal antigen” to confirm invasive candidiasis (DocT Infections (Part 3) Q6, 75%)", "These detect Aspergillus and Cryptococcus; β-D-glucan is the Candida test."),
  ],
  decode=[
    ("Mechanical mitral valve, candidaemia, EF 35%: next step? [Marrow QB25-Q35]", "Antifungal plus early surgery."),
    ("Septic shock, suspected fungal endocarditis, cultures unhelpful: best non-culture test for Candida? [DocT Infections (Part 3) Q6, 75%]", "(1→3)-β-D-glucan."),
  ],
  punch="Fungal prosthetic IE needs amphotericin and the surgeon, then lifelong fluconazole if the valve stays; culture-negative IE is diagnosed by serology and treated with long doxycycline-based courses.",
)

FLAGS = {
  'IE-08': "e: the ‘vegetation ≥10 mm + severe valve disease, low risk’ and ‘vegetation ≥30 mm’ rows (IIa) are ESC 2015 wording; ESC 2023 upgrades vegetation ≥10 mm with any other surgical indication to Class I (C), drops the 30 mm cut-off, and grades an isolated vegetation ≥10 mm without embolism or severe valve dysfunction, in a low-risk patient, IIb (B). Only S. aureus or non-HACEK Gram-negative PVE stays IIa. c: persistent bacteraemia (>1 week despite correct antibiotics and source control) is IIa in 2023 (‘should be considered’), weaker than fungal or multiresistant organisms. The explanation states both.",
  'IE-10': "Penicillin-allergy row: the ESC 2023 empirical table lists cefazolin or vancomycin with gentamicin (IIb C) for community NVE or late PVE, not vancomycin + ceftriaxone. The explanation keeps the card’s wording and gives the ESC regimen.",
  'IE-09': "Point 6: ‘switch warfarin to UFH for 1–2 weeks’ after ischaemic stroke is ESC 2015 wording; ESC 2023 replaces the oral anticoagulant with closely monitored UFH and, with a mechanical valve, restarts UFH as soon as possible after an intracranial haemorrhage (IIa C), which the card’s ‘ICH → stop all anticoagulation’ omits. The explanation states both.",
  'IE-04': "Card is correct (1 major + 3 minor = definite). The linked DocT GT6 Q3 keys ‘possible endocarditis’, which is wrong by Duke-ISCVID; the trap says so.",
  'IE-11': "Card is correct. DocT CGT6 Q119 keys vancomycin for relatively resistant viridans IE with CKD 4 in a non-allergic patient; its twin CGT5 Q55 correctly keys ceftriaxone monotherapy. The trap says so.",
  'IE-02': "Card is correct (ESC 2023: at least 3 sets). DocT Specific Cardiac Diseases Q9 keys ‘four sets’; still the only sensible option there.",
}
