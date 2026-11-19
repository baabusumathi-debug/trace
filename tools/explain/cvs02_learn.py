# CVS02 — Explain v3 ("Learn" depth): myocarditis — WHO 1995 definition, immunohistochemical criteria, viral/autoimmune subtypes, epidemiology, infectious and non-infectious causes,
# the changing viral spectrum, the three phases of pathogenesis, the ACS-like, heart-failure and life-threatening presentations, laboratory tests, ECG, echo, CMR, endomyocardial biopsy,
# ESC clinically suspected myocarditis, the management route, treatment of unstable disease, immunosuppression and IVIG.
# No mnemonics or hooks. Driven by qpack/CVS02.md (13 question links; CVS-32 infectious causes asked 3 times, CVS-43 EMB and CVS-46 unstable myocarditis twice each, CVS-34, 37, 38, 40,
# 42 and 45 once each). CVS-28–31, 33, 35, 36, 39, 41, 44, 47 and 48 have no linked question and get short explanations with [pattern] decode items. No Top-up cards for this deck.
# No `fix` entries exist for CVS02 in trace/test/data/qbank.json (checked 19 Nov 2026). The card layer (cvs_cardlayer.json: lines for CVS-32, 40, 42, 43; Crossfire notes for CVS-42 and
# CVS-43; chips for CVS-37 and 46) was read and the explanations agree with it; the disputed DocT key (CVS-42) and the AHA-vs-ESC biopsy split (CVS-43) are stated in the traps.
# Checked online on 19 Nov 2026:
#  - ESC 2025 myocarditis and pericarditis guideline (Schulz-Menger, Eur Heart J 2025;46:3952–4041), via the Rev Esp Cardiol ‘Insights’ editorial, the esanum journal-club summary and a
#    Serbian review (TMG 2026): umbrella term inflammatory myopericardial syndrome (IMPS); inflammatory cardiomyopathy = chronic myocarditis with dysfunction and remodelling; acute ≤4 weeks;
#    complicated myocarditis = LVEF <50%, acute HF, ventricular arrhythmia or advanced AV block; fulminant = cardiogenic shock; ‘definite’ myocarditis = compatible presentation plus CMR or EMB
#    confirmation (categories now unlikely/possible/definite rather than suspected/confirmed); CMR is the non-invasive cornerstone, using the 2018 Lake Louise criteria; routine viral serology
#    not recommended (HCV, HIV and a few bacterial serologies informative); PCR on EMB tissue mandatory before immunosuppression; EMB strongly advised in acute HF or cardiogenic shock, and in
#    malignant arrhythmia, conduction disease, LVEF <40%, extensive acute LGE, suspected giant-cell myocarditis or sarcoid, or failure to respond; immunosuppression not as initial therapy,
#    IIa C in fulminant non-infectious disease, IIb C in refractory dysfunction, strong recommendations for giant-cell and eosinophilic myocarditis; antivirals not as initial therapy in
#    uncomplicated viral myocarditis; fulminant disease: early shock team, IABP as a possible first bridge, VA-ECMO most used (SCAI D–E, biventricular failure), refractory cases durable MCS or
#    transplant; biventricular dysfunction the strongest adverse predictor, extensive LGE worse prognosis; beta-blocker ≥6 months (IIa C); exercise restriction about 1 month then individualised.
#    IVIG is not mentioned in any of the three summaries.
#  - Lake Louise criteria (CMR review, Cardiovasc Diagn Ther): 2009 — T2 oedema, early gadolinium enhancement (hyperaemia/capillary leak), LGE (necrosis/fibrosis), 2 of 3 positive;
#    accuracy 78%, sensitivity 67%, specificity 91%. 2018 — one T2-based (T2 signal or mapping) AND one T1-based (native T1, ECV or non-ischaemic LGE) criterion; EGE dropped; supportive
#    pericardial effusion/signal and wall-motion abnormality; validation sensitivity 87.5%, specificity 96.2%. LGE typically patchy subepicardial or mid-wall, lateral or septal.
#  - AHA 2020 scientific statement on fulminant myocarditis (Kociol, Circulation 2020; ACC ‘ten points’): ECG low voltage, ST elevation, conduction disease; echo thick walls with normal LV
#    diastolic size, RV dysfunction a poor sign; EMB for new unexplained HF <2 weeks with haemodynamic compromise; shock team, temporary MCS, early transfer to a transplant centre; giant-cell
#    myocarditis rarely recovers and may need biventricular support; no empirical immunomodulation before diagnosis; avoid competitive sport 3–6 months.
#  - ESC 2013 position statement (Caforio; text via PMC6439898): Dallas = infiltrate with degeneration/necrosis of adjacent myocytes, non-ischaemic; immunohistochemical abnormal infiltrate
#    ≥14 leucocytes/mm² including up to 4 monocytes/mm² with CD3+ T lymphocytes ≥7 cells/mm²; clinically suspected myocarditis ≥1 presentation and ≥1 criterion from different categories, or
#    ≥2 criteria if asymptomatic, without angiographic CAD (≥50% stenosis) or pre-existing cardiovascular/extracardiac cause.
#  - Epidemiology (Alomedika, from GBD): about 22 per 100,000 a year globally; 56% mortality at 4.3 years in the Myocarditis Treatment Trial cohort.
# From standard references without a fresh check (confident unless said): WHO/ISFC 1995 (Richardson) definitions; Myocarditis Treatment Trial (Mason, NEJM 1995: 111 patients, LVEF <45%,
# prednisone with cyclosporine or azathioprine for 24 weeks, no LVEF or survival benefit, mortality 20% at 1 year); TIMIC (Frustaci 2009, virus-negative inflammatory cardiomyopathy, prednisone
# + azathioprine improved LVEF); IMAC (McNamara 2001, IVIG 2 g/kg in recent-onset DCM, no added LVEF gain); Drucker 1994 (paediatric IVIG); AHA/ACC/ESC 2007 EMB scenarios (Cooper); CAR and
# DAF as coxsackie-adenovirus receptors; Ukena 2011 (QRS ≥120 ms predicts death/transplant); Fabre & Sheppard 2006 (8.6% of young sudden deaths); Matsumori (HCV in Japanese myocarditis);
# giant-cell myocarditis (Cooper 1997; cyclosporine-based regimens). NOT re-verified: the card’s athlete SCD (1–5%), idiopathic-cardiomyopathy share (10–40%), transplant-free survival
# (79%/56%), the Kandolf series (n 3219, 46%), the year-by-year virus sequence and the ‘4 weeks to transplant’ rule.
# Second review (19 Nov 2026), checked online: Magnani 2006 (Am Heart J; 112 biopsy-proven, 79%/56% transplant-free at 1/5 years); ESC 2013 text (KSW copy and Eur Heart J Suppl 2019 summary):
#    ≥1 presentation + ≥1 criterion or ≥2 if asymptomatic; SCD in young 2–42% at autopsy; biopsy-proven myocarditis 9–16% of adult unexplained DCM, 46% of children with an identified cause; IVIG
#    ‘ineffective in IMAC … we do not give recommendations’; transplant deferred in the acute phase, considered when support cannot be weaned; Schultz 2009 Mayo Clin Proc (8.6% of SCD; viral shift;
#    fulminant 93% vs 45% at 11 years, McCarthy); athlete SCD reviews (Compagnucci 2021: about 5–20%; ACC 2018: 5–22% in the young) and UK registry (Bhatia 2023: 1.1% of community SCD);
#    AHA/ACC/ESC 2007 EMB table (failure to respond to usual care in 1–2 weeks = Class I/IIa); Rev Esp Cardiol ESC 2025 insights (immunosuppression not initial; IIa C fulminant non-infectious,
#    IIb C refractory; exercise restriction initially 1 month; paracetamol/aspirin/NSAID, colchicine IIa if pericarditic; IABP first bridge, VA-ECMO most used); Matsumori 1998 (HCV antibody
#    10.6% HCM, 6.3% DCM, 2.4% donors). Still NOT verified: the Kandolf series (n 3219, 46%), the 4.4% Japanese myocarditis figure, the card’s 1–5% athlete and 10–40% DCM ranges, and any ESC 2025 text on IVIG.
# Blocked during this session: the ESC 2025 full text (edoc.mdc-berlin.de, Tübingen repository: proxy 403) and the ESC 2025 Essential Messages PDF (robots).

SPINE = [
  ("What counts as myocarditis", "Myocarditis is inflammation of the heart muscle proven by tissue: an infiltrate with non-ischaemic myocyte injury, counted by immunohistochemistry, and split by viral PCR into viral, autoimmune or both."),
  ("Causes and the three phases", "Viruses (now parvovirus B19 and HHV-6 more than coxsackie) cause most cases; the virus injures myocytes in days, the immune response that clears it injures them for weeks, and months later the heart either recovers or dilates."),
  ("Three ways it presents", "It looks like an ACS with clean coronaries, like new heart failure after a viral illness, or like sudden arrhythmia and shock."),
  ("Building the diagnosis", "ECG and troponin raise the suspicion, echo and angiography exclude other causes, CMR shows oedema and non-ischaemic scar, and endomyocardial biopsy proves it and names the type."),
  ("Route by haemodynamics", "Stable patients go to CMR and heart-failure therapy; unstable ones go to biopsy, inotropes and, when shock is refractory, mechanical support as a bridge to recovery or transplant."),
  ("Immune therapy only when virus-negative", "Immunosuppression helps only proven virus-negative immune forms (giant-cell, eosinophilic, sarcoid, autoimmune), so a negative PCR on biopsy comes first; IVIG has no adult role."),
]

PRIMER = "Troponin rises whenever myocytes die, whatever the cause, so a raised troponin with normal coronary arteries points away from plaque rupture and towards myocarditis, takotsubo or other non-ischaemic injury. Cardiac MRI (CMR) reads tissue: T2-weighted images show water (oedema), T1 mapping and extracellular volume show expanded interstitium, and late gadolinium enhancement (LGE) shows contrast trapped in dead or scarred muscle. Ischaemic scar starts at the subendocardium and follows a coronary territory; inflammatory scar is patchy, subepicardial or mid-wall. Endomyocardial biopsy takes small pieces of right-ventricular septum through a vein for histology, immunohistochemistry and viral PCR."

L = {}

L['CVS-28'] = dict(
  sub="Myocarditis → Definitions → WHO 1995",
  step=1,
  intro="Step 1 starts with what the word means. Myocarditis is a tissue diagnosis, and the WHO definition says which tissue tests count.",
  parts=[
    ('a', "**Inflammatory disease of the myocardium, diagnosed by established histological, immunological and immunohistochemical criteria.** The definition is pathological on purpose: chest pain, troponin and ECG changes are shared with many diseases, so only tissue proves inflammation. ESC 2025 still keeps biopsy as the reference standard but now also accepts a compatible presentation with confirmatory CMR as ‘definite’ myocarditis (CVS-42)."),
    ('b', "**Inflammatory infiltrates with myocyte degeneration and necrosis of non-ischaemic origin.** This is the Dallas histological criterion: the inflammatory cells must sit next to damaged myocytes, and the damage must not look like infarction (which is zonal and follows a territory)."),
    ('c', "**Inflammatory cardiomyopathy: myocarditis in association with cardiac dysfunction.** Inflammation plus a failing ventricle; ESC 2025 uses the term for chronic myocarditis with dysfunction and remodelling, the bridge to dilated cardiomyopathy (CVS-35)."),
  ],
  mimic=[
    ("Myocarditis vs inflammatory cardiomyopathy", "Myocarditis is the inflammation; inflammatory cardiomyopathy is the same inflammation with ventricular dysfunction."),
  ],
  traps=[
    ("“Myocarditis is diagnosed when troponin rises after a viral illness with normal coronaries”", "That is clinically suspected myocarditis (CVS-44); the definition needs tissue (or, since ESC 2025, confirmatory CMR)."),
  ],
  decode=[
    ("[pattern] Myocarditis with LV dysfunction — WHO term?", "Inflammatory cardiomyopathy."),
  ],
  punch="Myocarditis is a tissue diagnosis: inflammation next to non-ischaemic myocyte injury. Add ventricular dysfunction and it becomes inflammatory cardiomyopathy.",
)

L['CVS-29'] = dict(
  sub="Myocarditis → Definitions → Immunohistochemical criteria",
  step=1,
  intro="Step 1 continues with counting. Ordinary histology (Dallas) misses patchy or low-grade inflammation, so immunohistochemistry stains and counts the immune cells per area.",
  parts=[
    ('a', "**At least 14 leukocytes/mm² in the myocardium.** Staining for CD45 makes scattered leukocytes visible that light microscopy misses; a count, unlike a pattern, can be compared between pathologists."),
    ('b', "**Including up to 4 monocytes/mm².** Macrophages normally live in the myocardium, so resident cells alone could reach a count; capping the monocyte/macrophage share at 4 makes sure most of the infiltrate is lymphocytic, the cell type of immune injury."),
    ('c', "**7 or more CD3-positive T lymphocytes (per mm²).** T cells are the effectors of the adaptive phase (CVS-35); requiring them makes the count specific for active inflammation. These are the ESC 2013 immunohistochemical criteria; the Dallas criteria (1986) are the histological ones on CVS-28."),
  ],
  mimic=[
    ("Dallas vs immunohistochemical criteria", "Dallas: infiltrate plus non-ischaemic myocyte necrosis on H&E, insensitive because of sampling error. Immunohistochemical: ≥14 leukocytes/mm² with ≤4 monocytes and ≥7 CD3+ T cells/mm²."),
  ],
  traps=[
    ("“The Dallas criteria are the immunohistochemical counts”", "Dallas is histological (infiltrate plus necrosis); the 14/4/7 counts are the ESC 2013 immunohistochemical criteria."),
  ],
  decode=[
    ("[pattern] Immunohistochemical threshold for myocarditis on EMB?", "≥14 leukocytes/mm², up to 4 monocytes/mm², with ≥7 CD3+ T cells/mm²."),
  ],
  punch="Fourteen leukocytes per mm², no more than four of them monocytes, and at least seven CD3+ T cells: these are the immunohistochemical criteria, not Dallas, which is the older histological definition.",
)

L['CVS-30'] = dict(
  sub="Myocarditis → Classification → Viral, autoimmune, viral-and-immune",
  step=1,
  intro="Step 1 ends with the split that decides treatment. The same biopsy that proves inflammation is tested for viral genome by PCR.",
  parts=[
    ('a', "**Viral: histological myocarditis with positive viral PCR.** The virus is still in the myocardium, so suppressing immunity would let it replicate; antiviral or supportive treatment is the route (CVS-45)."),
    ('b', "**Autoimmune: negative viral PCR, with or without serum cardiac autoantibodies.** The inflammation continues without a virus, so it is driven by the immune system itself, the group in which immunosuppression is considered (CVS-47)."),
    ('c', "**Viral and immune: both positive.** Virus present and autoantibodies present; this mixed group is not a candidate for immunosuppression until the virus is dealt with."),
  ],
  mimic=[
    ("Autoimmune myocarditis vs viral myocarditis with autoantibodies", "The PCR decides: autoantibodies with a positive PCR is viral-and-immune, not autoimmune."),
  ],
  traps=[
    ("“Positive autoantibodies alone justify steroids”", "Only if the viral PCR on biopsy is negative (CVS-43c)."),
  ],
  decode=[
    ("[pattern] Biopsy-proven lymphocytic myocarditis, PCR negative — subtype and therapy considered?", "Autoimmune; immunosuppression may be considered."),
  ],
  punch="The PCR on the biopsy decides: positive means viral and no immunosuppression; negative means autoimmune, the only group where it is considered.",
)

L['CVS-31'] = dict(
  sub="Myocarditis → Epidemiology → Incidence, sudden death, outcome",
  step=1,
  intro="Step 1 sizes the problem. Most cases are mild and never biopsied, which is why every figure here is uncertain, as the card itself says.",
  parts=[
    ('a', "**22 per 100,000 annually in western countries.** This is the Global Burden of Disease estimate; subclinical cases are missed, so the true figure is higher."),
    ('b', "**1–5% of sudden cardiac death in athletes.** Exercise during active inflammation raises arrhythmia risk, the reason for exercise restriction after myocarditis (ESC 2025: initially 1 month, then individualised; AHA 2020: 3–6 months for competitive sport). Published figures vary widely with the population and the autopsy method: reviews of athlete series quote roughly 5–20%, while a recent UK community registry found myocarditis in only about 1% of all sudden cardiac deaths, so the card’s figure sits at the low end."),
    ('c', "**8.6% of sudden cardiac death in young adults.** This is an autopsy figure (quoted in the Mayo Clinic review of viral myocarditis, 2009); autopsy series select the fatal end of the spectrum, and the ESC 2013 position statement gives a range of 2–42% across autopsy studies of young sudden death."),
    ('d', "**10–40% of idiopathic cardiomyopathy.** Many ‘idiopathic’ dilated cardiomyopathies are the late phase of myocarditis (CVS-35, phase 3). The share depends on how inflammation is counted: ESC 2013 puts biopsy-proven myocarditis at 9–16% of adults with unexplained non-ischaemic DCM (and 46% of children with an identified cause); higher figures come from immunohistochemical inflammation or viral genome detection."),
    ('e', "**79% transplant-free at 1 year; 56% at 5 years.** These come from 112 consecutive patients with biopsy-proven myocarditis (Magnani, Am Heart J 2006): once myocarditis is severe enough to be biopsied, outcome is poor. The Myocarditis Treatment Trial cohort (CVS-47) was similar, with mortality 20% at 1 year and 56% at 4.3 years. Biventricular dysfunction is the strongest adverse predictor."),
  ],
  mimic=[],
  traps=[
    ("“Myocarditis is benign because most patients recover”", "Mild cases do; biopsy-proven myocarditis with dysfunction has roughly half survival free of transplant at 5 years."),
  ],
  decode=[
    ("[pattern] Proportion of sudden cardiac death in young adults due to myocarditis?", "About 8.6% (autopsy series)."),
  ],
  punch="About 22 per 100,000 a year, around one in twelve young sudden deaths, and a large share of ‘idiopathic’ DCM; once it causes dysfunction, only about half are alive without transplant at 5 years.",
)

L['CVS-32'] = dict(
  sub="Myocarditis → Aetiology → Infectious causes",
  step=2,
  intro="Step 2 opens with the causes. Viruses dominate, but bacteria, fungi, parasites and protozoa all inflame the myocardium, and the three real questions test the breadth of this list rather than the detail.",
  parts=[
    ('a', "**Viral: adenoviruses, enteroviruses (coxsackievirus), herpes viruses (HHV-6, EBV), HCV, HIV, influenza A, parvovirus B19.** Coxsackie B and adenovirus enter myocytes through the coxsackie-adenovirus receptor and lyse them directly; parvovirus B19 infects the endothelium of small vessels, so it injures the muscle indirectly. Influenza (and SARS-CoV-2) myocarditis can present with shock and a low ejection fraction in a patient whose lungs are clear (CVS-38)."),
    ('b', "**Bacterial: Borrelia, Mycobacterium, Mycoplasma pneumoniae, streptococcal species, Treponema pallidum.** Borrelia (Lyme carditis) typically causes AV block. Diphtheria and Coxiella burnetii (Q fever) belong here too: diphtheria toxin causes myocarditis with conduction block and is the leading cause of death in diphtheria."),
    ('c', "**Fungal: Aspergillus, Candida, Coccidioides, Cryptococcus, Histoplasma.** Mostly in the immunocompromised, as part of disseminated infection."),
    ('d', "**Parasitic: larva migrans, schistosomiasis.** Helminths provoke an eosinophilic infiltrate."),
    ('e', "**Protozoal: Trypanosoma cruzi (Chagas disease).** Chronic Chagas cardiomyopathy causes conduction disease (right bundle branch block, AV block), apical aneurysm and ventricular arrhythmia; Toxoplasma is another protozoal cause in the immunocompromised."),
  ],
  mimic=[
    ("Influenza myocarditis vs ACS", "Influenza myocarditis: febrile illness, troponin rise, global dysfunction, clean lungs and, if done, normal coronaries; ACS: risk factors, territorial ECG changes and wall-motion defect."),
    ("Viral myocarditis vs bacterial endocarditis", "Endocarditis is a valve infection: persistent bacteraemia, a vegetation and a new regurgitant murmur; myocarditis has none of these."),
  ],
  traps=[
    ("“Influenza with hypotension and a low EF — ACS” (31% missed the key)", "With no infiltrates and a confirmed influenza infection, the troponin and global dysfunction are influenza myocarditis; ACS needs an ischaemic story and territorial changes."),
    ("“Diphtheria or Q fever do not cause myocarditis”", "Both do; diphtheria toxin myocarditis with heart block is the commonest cause of death in diphtheria, so ‘all of the above’ was right."),
    ("“EBV is the most likely virus after a flu-like illness”", "EBV is a recognised cause, but the classic textbook answer for the commonest viral cause is coxsackie B (CVS-34)."),
  ],
  decode=[
    ("Confirmed influenza, hypotension, raised troponin, low EF, no infiltrates — diagnosis? [DocT GT, 69% right]", "Influenza myocarditis: clean lungs exclude influenza pneumonia as the cause of shock; the heart is the failing organ."),
    ("Young man, flu-like illness, diffuse ST changes, raised troponin — most likely virus? [DocT GT, 85% right]", "Coxsackie B."),
    ("Coxsackie, diphtheria, Q fever — which cause inflammatory myocarditis? [DocT GT, 89% right]", "All of them."),
  ],
  punch="Almost any infection can inflame the heart: coxsackie B is the classic virus, influenza causes shock with clear lungs, diphtheria and Lyme cause heart block, and Chagas is the protozoal cause.",
)

L['CVS-33'] = dict(
  sub="Myocarditis → Aetiology → Non-infectious causes",
  step=2,
  intro="Step 2 continues with the non-infectious causes. They matter because some are treated by stopping a drug and others by immunosuppression.",
  parts=[
    ('a', "**Toxins: anthracyclines, cocaine, interleukin-2.** Direct myocyte toxicity or, for cocaine, catecholamine injury and vasospasm. Immune checkpoint inhibitors are now an important addition: their myocarditis is often fulminant and is treated with high-dose steroids."),
    ('b', "**Hypersensitivity: cephalosporins, digoxin, diuretics, dobutamine, sulfonamides, tricyclic antidepressants.** A drug allergy with an eosinophilic infiltrate (CVS-43d); suspect it with rash, fever and blood eosinophilia, stop the drug, and give steroids. Dobutamine infused for days can itself cause it, a trap in the ICU patient whose heart worsens on inotropes."),
    ('c', "**Immunological: Churg–Strauss, diabetes mellitus, inflammatory bowel disease, giant cell myocarditis, granulomatosis with polyangiitis, sarcoidosis, SLE, Takayasu arteritis, thyrotoxicosis.** Most are systemic immune-mediated diseases that inflame the myocardium without a virus; giant-cell myocarditis, sarcoid and the vasculitis or connective-tissue forms are the group where immunosuppression has a role (CVS-47). Thyrotoxicosis and diabetes sit on the list as associations, not as indications for immune therapy."),
  ],
  mimic=[
    ("Hypersensitivity vs giant-cell myocarditis", "Hypersensitivity: drug exposure, rash, eosinophils, responds to stopping the drug. Giant-cell: young adult, rapidly progressive failure, VT and heart block, needs combined immunosuppression."),
  ],
  traps=[
    ("“Worsening heart failure on dobutamine is always disease progression”", "Prolonged dobutamine can cause eosinophilic hypersensitivity myocarditis."),
  ],
  decode=[
    ("[pattern] Which drug used in the ICU can cause hypersensitivity myocarditis?", "Dobutamine (also cephalosporins, sulfonamides, diuretics)."),
  ],
  punch="Toxins injure directly, drugs cause an eosinophilic allergy that stops when the drug stops, and systemic immune diseases cause the virus-negative forms that immunosuppression can treat.",
)

L['CVS-34'] = dict(
  sub="Myocarditis → Aetiology → Changing viral spectrum",
  step=2,
  intro="Step 2 then shows that the viruses found in biopsies have changed with time and place, which is why exam answers and current biopsy series can disagree.",
  parts=[
    ('a', "**1948 coxsackie B/A → 1950s enterovirus → 1990s adenovirus → 2000 parvovirus B19/HHV-6 → 2007 HCV/EBV; enterovirus myocarditis declining, non-enterovirus rising.** Part of the shift is real, and part reflects better PCR detection of genomes that persist in tissue."),
    ('b', "**Japan: hepatitis C commoner, 4.4%.** In the Japanese multicentre survey (Matsumori 1998) HCV antibody was commoner in patients with heart muscle disease than in blood donors (2.4%), reaching 10.6% in HCM and 6.3% in DCM. HCV genome has also been found in the myocardium, so it is a real cardiotropic virus in Japan, not a chance finding."),
    ('c', "**Europe: parvovirus B19 most common.** Parvovirus B19 is found in many biopsies, including those of people without heart disease, so its presence alone does not prove it caused the myocarditis."),
    ('d', "**India: hepatitis E case reports; adenovirus loads significantly higher than in the normal population in DCM.** The Indian evidence is small series and case reports; a higher viral load in DCM hearts than in controls suggests a causal role but does not prove it, since low-level genomes are also found in normal hearts."),
    ('e', "**Kandolf series (n 3219): 46% virus positive, 54% negative.** About half of biopsies carry no virus, the group in which autoimmune disease is considered (CVS-30). Even a positive PCR needs interpretation: low copy numbers of parvovirus B19 are common in hearts without myocarditis."),
  ],
  mimic=[
    ("Classic textbook virus vs current biopsy virus", "Exam questions on the ‘most likely viral cause’ expect coxsackie B; questions on current European biopsy data expect parvovirus B19 (and HHV-6)."),
  ],
  traps=[
    ("“Parvovirus B19 is the answer to ‘most likely viral cause’ in a young man after a flu-like illness”", "The DocT key is coxsackie B (85% right); parvovirus B19 is the commonest genome in European biopsy series, a different question."),
  ],
  decode=[
    ("Young man, flu-like illness, diffuse ST changes, raised troponin — most likely virus? [DocT GT, 85% right]", "Coxsackie B, the classic enterovirus cause."),
    ("[pattern] Commonest virus in European endomyocardial biopsy series?", "Parvovirus B19."),
  ],
  punch="Coxsackie B is the classic answer, but modern European biopsies most often show parvovirus B19 and HHV-6, and about half are virus-negative.",
)

L['CVS-35'] = dict(
  sub="Myocarditis → Pathogenesis → Three phases",
  step=2,
  intro="Step 2 ends with the time course, which explains both the presentations and why treatment depends on timing.",
  parts=[
    ('a', "**Phase 1, minutes–hours to 1–7 days: viral entry through CAR and DAF, innate immune activation, active replication and myocyte lysis.** The coxsackie-adenovirus receptor (CAR) with its co-receptor decay-accelerating factor (DAF) lets the virus in; damage now is direct viral lysis, so this is when antivirals would make sense and immunosuppression would be dangerous."),
    ('b', "**Phase 2, 1–4 weeks: adaptive immune response with cytokines, chemokines and T-cell-mediated clearance and myocardial injury.** T cells kill infected myocytes, and cross-reactive autoimmunity can injure uninfected ones; this is when the patient presents, 1–4 weeks after the viral illness (CVS-36)."),
    ('c', "**Phase 3, months to years: resolution (viral clearance, normal LV function) or dilated cardiomyopathy (chronic inflammation, fibrosis, remodelling).** Persistent virus or persistent autoimmunity keeps the injury going and the ventricle dilates; this is why some ‘idiopathic’ DCM is old myocarditis (CVS-31)."),
  ],
  mimic=[
    ("Phase 1 vs phase 2 injury", "Phase 1: the virus lyses myocytes. Phase 2: the immune response does, which is what immune therapy targets once the virus is gone."),
  ],
  traps=[
    ("“Steroids early in viral myocarditis limit the damage”", "In phase 1 the virus is replicating; suppressing immunity can increase viral injury. Immunosuppression needs a virus-negative biopsy (CVS-43c)."),
  ],
  decode=[
    ("[pattern] Receptor used by coxsackie B virus to enter cardiomyocytes?", "The coxsackie-adenovirus receptor (CAR), with DAF as co-receptor."),
  ],
  punch="Days of viral lysis, weeks of immune injury, then recovery or dilated cardiomyopathy; the phase decides whether the target is the virus or the immune response.",
)

L['CVS-36'] = dict(
  sub="Myocarditis → Presentation → ACS-like",
  step=3,
  intro="Step 3 describes the commonest picture in a young adult: chest pain, ST changes and troponin, as if this were an infarct.",
  parts=[
    ('a', "**Acute chest pain mimicking ACS, 1–4 weeks after a respiratory or gastrointestinal infection.** The delay matches phase 2 (CVS-35), when the immune response injures the myocardium; pain may be pleuritic when the pericardium is also inflamed."),
    ('b', "**No angiographic evidence of CAD.** Clean coronaries (or CT coronary angiography) turn ‘ACS’ into MINOCA, whose commonest cause in the young is myocarditis; CMR then separates it from takotsubo and small infarcts."),
    ('c', "**ST/T wave changes.** Often diffuse, without reciprocal depression (CVS-40), but they can mimic STEMI."),
    ('d', "**With or without normal or regional/global LV and/or RV dysfunction on echo or CMR.** Wall-motion abnormalities do not follow coronary territories."),
    ('e', "**With or without raised TnT/TnI.** Troponin reflects ongoing myocyte necrosis and is raised in most ACS-like cases; its height does not separate myocarditis from infarction, which is why the coronaries and CMR decide."),
  ],
  mimic=[
    ("Myocarditis vs STEMI", "Myocarditis: viral prodrome, young, diffuse ST change without reciprocity, normal coronaries, non-ischaemic LGE. STEMI: territorial change, reciprocal depression, an occluded artery."),
  ],
  traps=[
    ("“Normal coronaries and raised troponin exclude a cardiac cause”", "They point to myocarditis (or another MINOCA cause); CMR is the next test."),
  ],
  decode=[
    ("[pattern] Young man, chest pain 2 weeks after diarrhoea, ST elevation, troponin up, normal angiogram — diagnosis?", "Acute myocarditis (ACS-like presentation)."),
  ],
  punch="A coronary-looking presentation one to four weeks after a viral illness, with clean coronaries: that is ACS-like myocarditis, and CMR is the next step.",
)

L['CVS-37'] = dict(
  sub="Myocarditis → Presentation → New-onset heart failure",
  step=3,
  intro="Step 3 continues with the second picture: heart failure arriving over weeks after an infection. The one real question gave a teenager with a flu-like illness, raised troponin and pulmonary oedema.",
  parts=[
    ('a', "**New or progressive heart failure over 2 weeks to 3 months (DCM).** The window is the adaptive phase running into early remodelling; the ventricle may already be dilated."),
    ('b', "**Impaired LV and/or RV systolic function, with or without increased wall thickness, with or without dilated LV/RV.** Thick walls with a normal-sized LV mean oedema in acute or fulminant disease; a dilated, thin ventricle means longer-standing disease."),
    ('c', "**Symptoms after a respiratory or gastrointestinal infection.** The prodrome is the clue that separates it from other new cardiomyopathy."),
    ('d', "**Non-specific ECG signs, bundle branch block, AV block (D/D diphtheria, Chagas) and/or ventricular arrhythmias (D/D giant cell, lymphocytic myocarditis).** AV block in myocarditis points to diphtheria, Chagas, Lyme or sarcoid; new VT with failure points to giant-cell myocarditis, and both are reasons to biopsy (CVS-43)."),
  ],
  mimic=[
    ("Myocarditis vs peripartum or tachycardia-induced cardiomyopathy", "Myocarditis: viral prodrome, troponin rise, non-ischaemic LGE with oedema on CMR. The others lack the inflammatory signal."),
  ],
  traps=[
    ("“Pulmonary oedema with troponin in a teenager means MI”", "After a flu-like illness, with no risk factors, it is acute myocarditis presenting as heart failure."),
  ],
  decode=[
    ("Teenager, flu-like illness, raised troponin, pulmonary oedema — diagnosis? [Marrow]", "Acute myocarditis: heart failure after a respiratory or GI infection."),
    ("[pattern] Heart failure over 6 weeks with new VT and heart block in a young adult — suspect?", "Giant-cell myocarditis (or cardiac sarcoid); biopsy."),
  ],
  punch="New heart failure over weeks after a viral illness is myocarditis until proven otherwise; heart block or VT in that setting points to giant-cell myocarditis, sarcoid or Chagas and calls for biopsy.",
)

L['CVS-38'] = dict(
  sub="Myocarditis → Presentation → Life-threatening and asymptomatic",
  step=3,
  intro="Step 3 ends at the two extremes: the patient who arrives in shock or arrest, and the one found by chance. The real question was the shock end, triggered by influenza.",
  parts=[
    ('a', "**Life-threatening arrhythmia and aborted sudden death; cardiogenic shock; severely impaired LV function.** This is fulminant myocarditis (ESC 2025: myocarditis with cardiogenic shock). Diffuse oedema stiffens and stuns the whole ventricle at once, so output falls within hours; the walls look thick and the LV is not dilated. An older series (McCarthy, NEJM 2000) found excellent long-term survival after fulminant lymphocytic myocarditis; newer cohorts (Ammirati, Circulation 2017 and 2019) show that fulminant disease carries more death and transplant than non-fulminant, but ventricular function often recovers in those who are supported through the acute phase, which is why mechanical support as a bridge is worth it (CVS-46)."),
    ('b', "**Asymptomatic: troponin I raised, coronary angiogram normal, echo showing varying LV function.** Found during screening or after a viral illness; still needs CMR and follow-up because some progress."),
  ],
  mimic=[
    ("Fulminant myocarditis vs septic cardiomyopathy", "Septic cardiomyopathy: an infective source with vasodilatory shock and a dilated, recovering LV. Fulminant myocarditis: a viral prodrome, very high troponin, thick oedematous walls, low output and cold peripheries."),
    ("Fulminant myocarditis vs pulmonary embolism", "PE: a dilated RV with a small LV, hypoxaemia and normal LV function. Myocarditis: global LV failure."),
  ],
  traps=[
    ("“Influenza with hypotension and a low EF — ACS” (31% missed the key)", "Influenza can cause fulminant myocarditis; global dysfunction after a viral illness with clean lungs is myocarditis, not plaque rupture."),
  ],
  decode=[
    ("Confirmed influenza, hypotension, raised troponin, reduced EF, no pulmonary infiltrates — diagnosis? [DocT GT, 69% right]", "Influenza myocarditis (life-threatening presentation)."),
  ],
  punch="Fulminant myocarditis is cardiogenic shock from a thick, oedematous, stunned ventricle; it is more dangerous than non-fulminant disease but can recover, so support it. Influenza is a classic trigger.",
)

L['CVS-39'] = dict(
  sub="Myocarditis → Investigations → Laboratory tests",
  step=4,
  intro="Step 4 starts with the blood tests. None proves myocarditis; each answers a narrower question.",
  parts=[
    ('a', "**Inflammation: ESR, CRP, WBC, TNF-α, IL-1β, IL-10.** They show that inflammation is present somewhere, not that it is in the heart; a normal CRP does not exclude myocarditis."),
    ('b', "**Cardiac biomarkers: troponin / CK-MB.** Troponin shows myocyte injury, is raised in most cases and supports the diagnosis, but is not specific; a normal troponin makes acute myocarditis less likely."),
    ('c', "**Viral serology: limited diagnostic value (HIV, hepatitis C).** Antibodies to common cardiotropic viruses are frequent in the population and do not show that the virus is in the heart, so ESC 2025 advises against routine serology; HIV and hepatitis C are the exceptions because they change management."),
    ('d', "**Cardiac autoantibodies: no viral genome on EMB with positive autoantibodies = autoimmune myocarditis, which identifies the patient for immunosuppression.** The autoantibodies support an immune mechanism, but the negative viral PCR on tissue is the condition that makes immunosuppression safe (CVS-43c)."),
  ],
  mimic=[],
  traps=[
    ("“A positive coxsackie antibody titre confirms viral myocarditis”", "Serology does not localise the virus to the heart; PCR on biopsy tissue does."),
  ],
  decode=[
    ("[pattern] Role of viral serology in suspected myocarditis?", "Limited; not routinely recommended except HIV and hepatitis C."),
  ],
  punch="Troponin shows injury, CRP shows inflammation, serology shows little; only a biopsy with negative viral PCR and positive autoantibodies identifies the patient for immunosuppression.",
)

L['CVS-40'] = dict(
  sub="Myocarditis → Investigations → ECG",
  step=4,
  intro="Step 4 continues with the ECG: cheap and almost always abnormal in some way, but not specific and not sensitive enough to rule myocarditis out. The one real question tested exactly that.",
  parts=[
    ('a', "**Role: a screening tool.** It is done in everyone, but its changes are non-specific and a normal ECG does not exclude myocarditis; it raises suspicion, it does not decide."),
    ('b', "**Sinus tachycardia is the most common finding.** It reflects fever, pain and a falling stroke volume, and is the least specific finding of all."),
    ('c', "**ST-T changes without reciprocation; LV strain; QRS and QT prolongation; AV conduction block and ventricular arrhythmias.** Inflammation is patchy and epicardial, so ST changes are diffuse without a reciprocal territory, as in pericarditis (CVS-08); fulminant disease may show low voltage from oedema. Block and VT suggest giant-cell myocarditis, sarcoid or Lyme (CVS-37)."),
    ('d', "**Bad prognosis: QTc >440 ms, ventricular arrhythmia, QRS >120 ms.** A wide QRS means inflammation and fibrosis in the conducting tissue and was an independent predictor of death or transplant in biopsy-proven myocarditis."),
  ],
  mimic=[
    ("Myocarditis vs STEMI on the ECG", "Myocarditis: diffuse ST change without reciprocity and often sinus tachycardia. STEMI: territorial elevation with reciprocal depression (CVS-08)."),
  ],
  traps=[
    ("“The ECG is sensitive for myocarditis”", "False: it is often abnormal but non-specifically, and a normal ECG does not exclude it. Troponin is also more specific than sensitive, so CMR or biopsy confirms."),
  ],
  decode=[
    ("Myocarditis statements — which is false? [Marrow]", "‘The ECG is sensitive’: it is non-specific and insensitive, a screening test only."),
    ("[pattern] ECG features of poor prognosis in myocarditis?", "QRS >120 ms, QTc >440 ms, ventricular arrhythmia."),
  ],
  punch="The ECG in myocarditis is usually abnormal but non-specific: sinus tachycardia and diffuse ST-T changes without reciprocity. It screens, it cannot exclude, and a wide QRS predicts a bad outcome.",
)

L['CVS-41'] = dict(
  sub="Myocarditis → Investigations → Echocardiography",
  step=4,
  intro="Step 4 adds echo, which cannot see inflammation but excludes other causes and finds the dangerous signs.",
  parts=[
    ('a', "**Its primary role is to rule out other causes of heart failure.** Valve disease, hypertrophic or restrictive cardiomyopathy, tamponade and territorial wall-motion defects of infarction are all seen at the bedside."),
    ('b', "**Regional or global LV and/or RV dysfunction.** In fulminant disease the walls are thick from oedema and the LV is not dilated; in subacute disease the LV is dilated."),
    ('c', "**Done before EMB to exclude pericardial effusion and intracavitary thrombi.** Perforation is the main biopsy complication and a pre-existing effusion would hide or worsen it; a thrombus in the ventricle could embolise when the bioptome passes."),
    ('d', "**RV dysfunction: poor prognosis.** Biventricular failure means more extensive disease and is the strongest predictor of death or transplant (ESC 2025, AHA 2020)."),
    ('e', "**Coronary angiography must be done to rule out ACS.** Echo cannot tell an infarct from myocarditis when dysfunction is regional; an angiogram (or CT coronary angiography in low-risk patients) excludes coronary disease, a condition of the diagnosis (CVS-44d)."),
  ],
  mimic=[],
  traps=[
    ("“Echo can confirm myocarditis”", "It cannot characterise tissue; CMR or biopsy does (CVS-42, 43)."),
  ],
  decode=[
    ("[pattern] Echo finding of worst prognosis in myocarditis?", "RV dysfunction (biventricular failure)."),
  ],
  punch="Echo excludes other causes and an effusion before biopsy, and finds RV dysfunction, the worst prognostic sign; coronary angiography must still exclude ACS.",
)

L['CVS-42'] = dict(
  sub="Myocarditis → Investigations → Cardiac MRI",
  step=4,
  intro="Step 4 reaches the test that sees the tissue without a biopsy. The real question asked when CMR works best and what it can and cannot tell, and half the cohort got it wrong.",
  parts=[
    ('a', "**Performed in symptomatic patients with clinical suspicion of myocarditis.** ESC 2025 makes CMR the non-invasive cornerstone and accepts a compatible presentation with positive CMR as definite myocarditis. Yield is highest when it is done after about the first week (ideally within 2–3 weeks), when oedema, hyperaemia and LGE are all present; very early or late scans miss oedema."),
    ('b', "**Three markers of tissue injury: intracellular and interstitial oedema, hyperaemia and capillary leakage, necrosis and fibrosis.** These are the 2009 Lake Louise markers (T2 oedema, early gadolinium enhancement, LGE), two of three positive; sensitivity 67%, specificity 91%. The 2018 update needs one T2-based criterion (oedema) and one T1-based criterion (native T1, extracellular volume or non-ischaemic LGE), drops early enhancement, and is more accurate (sensitivity about 88%, specificity about 96%)."),
    ('c', "**Late gadolinium enhancement of myocardial pattern.** The pattern is non-ischaemic: patchy, subepicardial or mid-wall, typically inferolateral or septal, sparing the subendocardium. An infarct starts at the subendocardium and follows a territory, so the location separates the two; it does not name the virus or the type of myocarditis."),
  ],
  mimic=[
    ("Myocarditis LGE vs infarct LGE", "Myocarditis: subepicardial or mid-wall, patchy, inferolateral or septal. Infarct: subendocardial or transmural, in a coronary territory."),
  ],
  traps=[
    ("“The location of LGE confirms a viral aetiology”", "CMR cannot tell viral from non-viral or name the histology; that needs biopsy with PCR."),
    ("“CMR replaces endomyocardial biopsy”", "Not when giant-cell, eosinophilic or fulminant myocarditis is suspected, or before immunosuppression; histology and PCR decide treatment."),
    ("“LGE extent does not predict events; LVEF does” (DocT’s explanation for rejecting option C)", "DocT’s key is ‘sensitivity highest after 7 days’ and its explanation names LVEF, not LGE, as the prognostic marker. That is dated: LGE presence and extent, especially mid-wall septal LGE, independently predict events (ITAMY; ESC 2025). In a DocT paper pick ‘after 7 days’; in a newer paper LGE extent is also correct."),
  ],
  decode=[
    ("Suspected myocarditis, subepicardial inferolateral LGE — which statement on CMR is correct? [DocT GT, 50% right]", "Key: sensitivity highest after about 7 days from onset. LGE extent predicting events is also true by current evidence; LGE location does not identify the virus, and CMR does not replace biopsy."),
    ("[pattern] 2018 Lake Louise criteria for myocarditis?", "One T2-based (oedema) plus one T1-based (T1 mapping, ECV or non-ischaemic LGE) criterion."),
  ],
  punch="CMR shows oedema and patchy subepicardial or mid-wall LGE; the 2018 Lake Louise criteria need one T2 and one T1 marker, yield is best after the first week, and the extent of LGE carries prognosis, but it cannot name the cause.",
)

L['CVS-43'] = dict(
  sub="Myocarditis → Investigations → Endomyocardial biopsy",
  step=4,
  intro="Step 4 ends with the gold standard. Biopsy is invasive and samples only a few millimetres, so the questions are when to do it and what each pattern means.",
  parts=[
    ('a', "**Gold standard for the diagnosis of myocarditis.** It is the only test that names the histological type and detects viral genome; its weakness is sampling error, because inflammation is patchy. Taking several samples from both ventricles, or guided by CMR or mapping, improves yield."),
    ('b', "**It identifies the specific aetiology, so treatment can be tailored, and it is the basis for starting immunosuppression.** Giant-cell, eosinophilic and sarcoid myocarditis are treated with immunosuppression; lymphocytic viral myocarditis is not. ESC 2025 advises biopsy in acute heart failure or cardiogenic shock, malignant arrhythmia or conduction disease, LVEF <40%, extensive acute LGE, suspected giant-cell myocarditis or sarcoid, and failure to respond to treatment. The AHA (Cooper 2007) list is new unexplained heart failure under 2 weeks with haemodynamic compromise; 2 weeks to 3 months with a dilated LV and new ventricular arrhythmia, Mobitz II or complete block, or no response in 1–2 weeks; and heart failure with rash, fever or eosinophilia, connective-tissue disease, suspected infiltrative disease or suspected giant-cell myocarditis."),
    ('c', "**Immunosuppression only after active infection has been ruled out by PCR on the biopsy.** Suppressing immunity while the virus replicates removes the defence that limits myocyte lysis (CVS-35)."),
    ('d', "**Lymphocytic: viral or autoimmune; neutrophilic: bacterial, fungal or early viral; eosinophilic: hypersensitivity or hypereosinophilic syndrome; granulomatous: sarcoidosis; giant cells: giant-cell myocarditis.** Giant cells with extensive myocyte necrosis and no well-formed granulomas mean giant-cell myocarditis; non-caseating granulomas with less necrosis mean sarcoid."),
  ],
  table=dict(title="EMB pattern and what it changes", head=["Pattern", "Usual cause", "Treatment it points to"],
    rows=[["Lymphocytic, PCR+", "Viral", "Supportive care; no immunosuppression"],
          ["Lymphocytic, PCR−", "Autoimmune", "Immunosuppression may be considered (CVS-47)"],
          ["Eosinophilic", "Hypersensitivity, HES, EGPA", "Stop the drug; steroids"],
          ["Granulomatous", "Sarcoidosis", "Steroids ± steroid-sparing agent"],
          ["Giant cells", "Giant-cell myocarditis", "Combined immunosuppression; early MCS or transplant"]]),
  mimic=[
    ("Giant-cell myocarditis vs cardiac sarcoid", "Both cause VT and heart block. Giant-cell: younger, faster, diffuse necrosis with giant cells and no granulomas, worse survival. Sarcoid: non-caseating granulomas, extracardiac disease, slower course."),
  ],
  traps=[
    ("“Giant-cell myocarditis gets supportive care, as viral myocarditis does”", "It is the one myocarditis where combined immunosuppression (steroid plus cyclosporine, with or without azathioprine) is life-saving; refractory VT and shock are typical, so plan early mechanical support or transplant."),
    ("“Failure of EF to improve after optimal heart failure therapy is not an indication for EMB” (Marrow’s key)", "The key is disputed. Marrow’s source table lists worsening EF despite therapy but not failure to improve. The AHA/ACC/ESC 2007 statement itself makes failure to respond to usual care within 1–2 weeks a Class I indication (heart failure of 2 weeks to 3 months with a dilated LV), ESC (CVS-45) sends LV dysfunction persisting after 3 months of therapy to biopsy, and ESC 2025 lists failure to respond. In Marrow’s question pick its key; in any guideline-based question it is an indication."),
  ],
  decode=[
    ("Cardiogenic shock with refractory VT; biopsy shows multinucleated giant cells and extensive necrosis — management priority? [DocT GT]", "High-dose combined immunosuppression and early consideration of mechanical support or transplant."),
    ("Indications for endomyocardial biopsy — which is incorrect? [Marrow]", "Marrow keys ‘no EF improvement after optimal HF therapy’; refractory HF, new block or VT, eosinophilia, CTD, infiltrative disease and suspected giant-cell are the classic indications. By AHA 2007 and ESC, failure to respond is also an indication, so the key is disputed."),
  ],
  punch="Biopsy names the type and the virus, and only a virus-negative biopsy licenses immunosuppression; giant cells with necrosis mean giant-cell myocarditis, the form that needs immediate combined immunosuppression and early mechanical support.",
)

L['CVS-44'] = dict(
  sub="Myocarditis → Diagnosis → ESC clinically suspected myocarditis",
  step=4,
  intro="Step 4 pulls the tests together. Since most patients are never biopsied, ESC defined when myocarditis is clinically suspected, the trigger for further work-up.",
  parts=[
    ('a', "**Acute chest pain (pericarditic or pseudo-ischaemic); new or worsening heart failure; subacute or chronic heart failure; palpitations or syncope; cardiogenic shock.** The three syndromes of CVS-36 to 38, with arrhythmia added."),
    ('b', "**ECG/Holter/stress test features; raised troponin; functional and structural abnormalities on imaging; tissue characterisation by CMR.** Each criterion is a different kind of evidence: electrical, biochemical, mechanical and tissue."),
    ('c', "**Diagnosis if >1 presentation AND >1 criterion, or >2 criteria.** The ESC 2013 wording is ‘≥1’ presentation with ‘≥1’ criterion from different categories, or, in an asymptomatic patient, ‘≥2’ criteria. One clinical feature with one objective test is enough to suspect it."),
    ('d', "**In the absence of CAD or pre-existing heart disease.** Specifically no angiographic stenosis of 50% or more and no known cardiovascular or extracardiac cause that explains the picture. ESC 2025 now calls myocarditis definite when a compatible presentation is confirmed by CMR (2018 Lake Louise) or biopsy, and lower-certainty findings possible."),
  ],
  mimic=[],
  traps=[
    ("“Two clinical presentations are needed”", "One presentation with one diagnostic criterion is enough; two criteria are needed only when the patient is asymptomatic."),
  ],
  decode=[
    ("[pattern] Asymptomatic patient — how many ESC criteria for clinically suspected myocarditis?", "Two or more."),
  ],
  punch="One clinical presentation plus one objective criterion, or two criteria if asymptomatic, with coronary disease excluded: that is clinically suspected myocarditis, which CMR or biopsy then confirms.",
)

L['CVS-45'] = dict(
  sub="Myocarditis → Management → Initial route",
  step=5,
  intro="Step 5 turns the diagnosis into a route. The branch point is haemodynamics, because an unstable patient needs a tissue answer fast.",
  parts=[
    ('a', "**First, exclude coronary artery disease where appropriate.** The commonest cause of troponin with dysfunction is still an infarct; angiography or CT coronary angiography removes it."),
    ('b', "**Haemodynamically stable: cardiac MRI.** CMR confirms the diagnosis without risk, and most stable patients do well with supportive care."),
    ('c', "**Haemodynamically unstable: EMB.** Shock or malignant arrhythmia raises the chance of giant-cell, eosinophilic or fulminant necrotising forms that need specific treatment within days; CMR is often impossible in such patients anyway."),
    ('d', "**Normal LV function: supportive care.** Rest from exercise, symptom relief (ESC 2025: paracetamol, aspirin or NSAID, with colchicine if pericarditic symptoms) and follow-up."),
    ('e', "**LV dysfunction: neurohormonal antagonists.** Standard heart-failure therapy (ACE inhibitor or ARNI, beta-blocker, MRA, SGLT2 inhibitor). If dysfunction persists despite 3 months of optimal therapy, biopsy; virus-negative lymphocytic myocarditis may then get immunosuppression, virus-positive antiviral therapy."),
  ],
  mimic=[
    ("Stable vs unstable branch", "Stable: CMR then heart-failure therapy. Unstable: biopsy because the histology changes treatment now."),
  ],
  traps=[
    ("“Persistent LV dysfunction after 3 months of optimal therapy is never a biopsy indication” (Marrow’s key)", "In the ESC route it is, and the AHA/ACC/ESC 2007 statement also counts failure to respond to usual care as an indication; Marrow’s key is disputed (CVS-43). Pick it only in Marrow’s own question."),
  ],
  decode=[
    ("Indications for endomyocardial biopsy — which is incorrect? [Marrow]", "Marrow keys ‘no EF improvement after optimal HF therapy’; by this ESC route (and by AHA 2007), persistent dysfunction despite therapy is an indication, so the key is disputed."),
    ("[pattern] Suspected myocarditis, haemodynamically stable, coronaries normal — next investigation?", "Cardiac MRI."),
  ],
  punch="Exclude coronary disease, then branch: stable patients get CMR and heart-failure therapy, unstable ones get a biopsy, and dysfunction that persists 3 months on therapy goes to biopsy to decide on immune or antiviral treatment.",
)

L['CVS-46'] = dict(
  sub="Myocarditis → Management → Haemodynamically unstable disease",
  step=5,
  intro="Step 5 continues with the unstable patient, the ICU part of the deck. Both real questions are the same scenario: shock that keeps worsening on drugs.",
  parts=[
    ('a', "**Class IV shock with normal BP: vasodilators.** If pressure is preserved, lowering afterload (nitrates, nitroprusside) lets a weak ventricle eject more."),
    ('b', "**Cardiogenic shock with low BP: inotropes and vasopressors.** Norepinephrine to hold perfusion pressure, dobutamine or milrinone for output; they buy time but raise myocardial oxygen demand and arrhythmia risk in an inflamed heart."),
    ('c', "**Increased filling pressures: diuretics.** To relieve congestion once perfusion is secured."),
    ('d', "**Refractory shock: IABP, ECMO, VAD.** Fulminant myocarditis can recover fully if the patient survives the acute weeks, so mechanical support is a bridge to recovery. VA-ECMO is the most used (SCAI D–E, biventricular failure); an IABP may be a first bridge in less severe shock; a microaxial LV pump (Impella) unloads the LV, alone or with ECMO; durable VADs are for no recovery."),
    ('e', "**No recovery within 4 weeks: cardiac transplantation.** The guidelines give no fixed number of weeks: ESC 2013 says transplantation should be deferred in the acute phase because recovery may occur, and considered when the patient cannot be weaned from drug and mechanical support; ESC 2025 says refractory cases may need long-term MCS or transplant. The tension is the same: waiting too long on temporary support risks multiorgan failure and device complications, transplanting too early removes a heart that might have recovered. Giant-cell myocarditis rarely recovers, so it reaches transplant or durable support sooner (AHA 2020)."),
  ],
  mimic=[
    ("Fulminant myocarditis vs AMI shock on MCS", "In myocarditis the injured muscle can recover, so MCS is a bridge to recovery; in AMI shock, scar is permanent and the route to durable support or transplant is commoner."),
  ],
  traps=[
    ("“Switch dobutamine to milrinone and add vasopressin”", "Changing drugs does not fix refractory shock (CI 1.8, lactate 5 on two agents); the next step is VA-ECMO."),
    ("“Pulse methylprednisolone for biopsy-proven viral myocarditis in shock”", "Immunosuppression with virus present can worsen it; steroids are for virus-negative immune forms (CVS-47)."),
    ("“Repeat the biopsy to see if inflammation has resolved”", "A deteriorating patient needs support now, not more histology."),
  ],
  decode=[
    ("Biopsy-proven viral myocarditis, CI 1.8, lactate 5, on high-dose dobutamine and norepinephrine, worsening — next step? [DocT GT]", "VA-ECMO: mechanical support for shock refractory to drugs."),
    ("Fulminant myocarditis, ventilated, shock despite maximal inotropes — next step? [Marrow]", "Mechanical circulatory support as a bridge to recovery (Marrow keys LVAD). In practice the first device is temporary, usually VA-ECMO with or without a microaxial LV pump; a durable LVAD comes only if the heart does not recover."),
  ],
  punch="When fulminant myocarditis stays in shock on two vasoactive drugs, go to mechanical support, usually VA-ECMO, because the heart may recover; transplant or durable support is for the heart that cannot be weaned, the card’s ‘4 weeks’ being a rule of thumb rather than a guideline cut-off.",
)

L['CVS-47'] = dict(
  sub="Myocarditis → Management → Immunosuppression",
  step=6,
  intro="Step 6 asks when to treat the immune response itself. The negative trial explains the caution; the ESC list says where it is still used.",
  parts=[
    ('a', "**Myocarditis Treatment Trial (NEJM 1995): 111 patients with myocarditis and LVEF <45%, randomised to conventional therapy alone or with 24 weeks of immunosuppression.** Prednisone with cyclosporine or azathioprine did not improve LVEF or survival; it included virus-positive and virus-negative patients alike, since PCR was not used. Later virus-negative trials (TIMIC: prednisone plus azathioprine for 6 months) did improve LVEF."),
    ('b', "**Worsening heart failure despite standard treatment; giant-cell or eosinophilic myocarditis, sarcoidosis; myocarditis with autoimmune disease.** These are the virus-negative immune forms. ESC 2025 says immunosuppressants and corticosteroids should not be used as initial therapy; it reserves them for biopsy-proven or highly suspected immune forms (giant-cell, eosinophilic, sarcoid, autoimmune), fulminant non-infectious myocarditis (IIa C) and refractory ventricular dysfunction (IIb C)."),
    ('c', "**Started only after active infection has been ruled out on EMB by PCR.** Suppressing immunity while a virus replicates removes the defence that limits myocyte lysis. Patient selection is the likely reason the unselected MTT was negative while the virus-negative TIMIC was positive (CVS-30, 43)."),
  ],
  mimic=[
    ("Myocarditis Treatment Trial vs TIMIC", "MTT: unselected histological myocarditis, no benefit. TIMIC: virus-negative inflammatory cardiomyopathy, LVEF improved."),
  ],
  traps=[
    ("“The Myocarditis Treatment Trial showed immunosuppression improves LVEF”", "It did not; benefit appears only when patients are selected by a negative viral PCR."),
  ],
  decode=[
    ("[pattern] Absolute precondition before immunosuppression in myocarditis?", "Active infection excluded by PCR on endomyocardial biopsy."),
  ],
  punch="Unselected immunosuppression failed in the Myocarditis Treatment Trial; it works only in virus-negative immune forms, above all giant-cell and eosinophilic myocarditis, so a negative PCR on biopsy comes first.",
)

L['CVS-48'] = dict(
  sub="Myocarditis → Management → IVIG",
  step=6,
  intro="Step 6 ends with IVIG, the immune therapy whose evidence points in two directions by age.",
  parts=[
    ('a', "**IVIG 2 g/kg.** The same immunomodulatory dose as in Kawasaki disease, given over one to two days; it neutralises antibodies, blocks Fc receptors and dampens cytokines."),
    ('b', "**In recent-onset dilated cardiomyopathy IVIG does not augment the improvement in LVEF.** In the IMAC trial both arms improved by a similar amount, because many recent-onset cases recover on standard therapy anyway."),
    ('c', "**In small series of acute paediatric myocarditis IVIG has been effective.** Better recovery of LV function and a trend to survival, but uncontrolled and small."),
    ('d', "**ESC: no recommendation for IVIG in adult myocarditis.** The ESC 2013 position statement says IVIG was ineffective in the IMAC trial and gives no recommendation for its use; the ESC 2025 guideline summaries do not list it among the treatments of myocarditis, so adults do not receive it routinely."),
  ],
  mimic=[],
  traps=[
    ("“IVIG is standard in adult myocarditis because it works in children”", "Adult evidence (IMAC) was negative; ESC makes no recommendation."),
  ],
  decode=[
    ("[pattern] Role of IVIG in adult myocarditis per ESC?", "No recommendation; the controlled trial in recent-onset DCM showed no added LVEF benefit."),
  ],
  punch="IVIG 2 g/kg helped in small paediatric series but added nothing to LVEF recovery in the adult trial, so ESC gives no recommendation for adults.",
)

FLAGS = {
  'CVS-29': "Title: the 14/4/7 counts are the ESC 2013 immunohistochemical criteria, not the Dallas criteria (Dallas 1986 is the histological definition: infiltrate with non-ischaemic myocyte necrosis). c: the threshold is ≥7 CD3+ T cells per mm².",
  'CVS-42': "b and c follow the 2009 Lake Louise criteria (2 of 3 markers). The 2018 update, adopted by ESC 2025, needs one T2-based and one T1-based criterion and drops early enhancement; the ‘myocardial pattern’ LGE is the non-ischaemic subepicardial/mid-wall pattern.",
  'CVS-31': "b: ‘1–5% of athlete SCD’ is at the low end of the literature (athlete reviews quote about 5–20%; ESC 2013 gives 2–42% of young SCD at autopsy); source of the card’s range not traced. d: ESC 2013 gives 9–16% of adult unexplained DCM as biopsy-proven myocarditis; the card’s 10–40% is wider. e: the 79%/56% figures are Magnani 2006 (112 biopsy-proven patients), not a population figure.",
  'CVS-43': "Card layer cross-note (Marrow EMB question) says persistent dysfunction is not an AHA indication; AHA/ACC/ESC 2007 makes failure to respond to usual care within 1–2 weeks a Class I (2 weeks–3 months) or IIa (>3 months) indication, so Marrow’s key is disputed under AHA as well as ESC.",
  'CVS-44': "c: ESC 2013 reads ≥1 presentation and ≥1 criterion (from different categories), or ≥2 criteria if the patient is asymptomatic; the card’s ‘>1’ and ‘>2’ overstate the threshold and omit ‘if asymptomatic’. ESC 2025 calls myocarditis definite when a compatible presentation is confirmed by CMR or EMB.",
  'CVS-46': "e: ‘transplant if no recovery within 4 weeks’ is not a guideline cut-off; ESC 2013 defers transplant in the acute phase and considers it when drug and mechanical support cannot be weaned, ESC 2025 says refractory cases may need long-term MCS or transplant.",
}
