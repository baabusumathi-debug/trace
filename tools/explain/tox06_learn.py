# TOX06 — Novel Cancer Therapies: Toxicity in ICU. Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Same fields as TOX01: sub, intro, parts, table (optional), mimic, traps, decode, punch, extra (optional).
L = {}
FLAGS = {}

L['ONC-01'] = dict(
  sub="Toxicology → The Agents → Class, example and target",
  intro="The newer cancer drugs do not poison every dividing cell, as classical chemotherapy does. Each is aimed at one molecule — a surface marker, a growth signal, an enzyme inside the cell, or a brake on the immune system. Knowing the target tells you what the drug does to the tumour and, just as important for the ICU, what it does to the rest of the body.",
  parts=[
    ('a', "**Monoclonal antibodies: rituximab → CD20; bevacizumab → VEGF; cetuximab → EGFR.** CD20 sits on mature B cells, so rituximab depletes normal B cells along with lymphoma cells — hence infusion reactions with the first dose, hypogammaglobulinaemia and hepatitis B reactivation. Bevacizumab binds the VEGF ligand itself; VEGF keeps capillary endothelium healthy, so blocking it gives hypertension, proteinuria, thrombosis and poor wound healing. EGFR is also present in skin and in the renal tubule, so cetuximab causes an acneiform rash and magnesium wasting."),
    ('b', "**Bispecific antibody: blinatumomab → CD3 and CD19.** One arm grips CD3 on a T cell, the other CD19 on a B cell, so the T cell is forced up against the leukaemic B cell and kills it without needing to recognise it. Mass T-cell activation is exactly what produces cytokine release syndrome (ONC-04). It has a short half-life and runs as a continuous infusion, so stopping the infusion is itself a treatment."),
    ('c', "**Checkpoint inhibitors: ipilimumab → CTLA-4; nivolumab, pembrolizumab → PD-1.** These antibodies do not touch the tumour at all; they block the brakes on T cells (ONC-02). The price is that T cells released against the tumour can also attack normal tissue."),
    ('d', "**Tyrosine kinase inhibitors: imatinib, dasatinib → the tyrosine kinase (BCR-ABL).** These are small molecules taken by mouth that block the ATP site of the kinase that drives the tumour — BCR-ABL in chronic myeloid leukaemia. Because many kinases look alike, each TKI also hits ‘off-target’ kinases, which explains its side-effects (ONC-03)."),
    ('e', "**Immune effector cells: CAR-T cells → a tumour antigen (CD19).** The drug is the patient’s own T cells, re-engineered to recognise CD19 on B-cell leukaemia and lymphoma (BCMA is the target in myeloma). Living cells multiply after infusion, so their effect — and their toxicity — builds over days."),
  ],
  table=dict(title="Target decides toxicity", head=["Agent", "Target", "Off-tumour consequence"], rows=[["Rituximab", "CD20 (B cells)", "infusion reaction, HBV reactivation, low IgG"], ["Bevacizumab", "VEGF", "hypertension, proteinuria, thrombosis, TMA"], ["Cetuximab", "EGFR", "rash, hypomagnesaemia"], ["Blinatumomab, CAR-T", "CD19 (with CD3)", "CRS, ICANS, B-cell aplasia"], ["Ipilimumab, nivolumab", "CTLA-4, PD-1", "immune-related adverse events"]]),
  mimic=[
    ("Bevacizumab vs cetuximab", "Both are antibodies against a growth pathway, but bevacizumab binds the VEGF ligand (vascular toxicity) and cetuximab blocks the EGF receptor (skin and magnesium)."),
    ("Blinatumomab vs CAR-T", "Both direct T cells to CD19; blinatumomab is an off-the-shelf antibody that stops when the infusion stops, CAR-T cells are living cells that persist and expand."),
  ],
  traps=[
    ("“Blinatumomab targets CD20”", "That is rituximab; blinatumomab links CD3 on T cells to CD19 on B cells (ONC-13)."),
    ("“Checkpoint inhibitors kill tumour cells directly”", "They only remove a brake on T cells; the T cells do the killing — and can attack normal organs."),
    ("“Bevacizumab blocks the VEGF receptor”", "It binds the VEGF ligand; the receptor-level blockers are the small-molecule TKIs such as sunitinib."),
  ],
  decode=[
    ("Anti-CD20 antibody in lymphoma", "Rituximab."),
    ("Bispecific T-cell engager in B-ALL", "Blinatumomab (CD3/CD19)."),
    ("First checkpoint inhibitor approved", "Ipilimumab (anti-CTLA-4)."),
  ],
  punch="Each novel agent is aimed at one molecule, and its ICU toxicity follows from where else that molecule works — VEGF in vessels, EGFR in skin and tubule, and T-cell brakes everywhere.",
  extra=[dict(q="Cetuximab or panitumumab: the electrolyte to watch?", a="**Hypomagnesaemia** — EGFR drives magnesium reabsorption in the distal tubule; blocking it wastes magnesium (and secondarily calcium and potassium).")],
)

L['ONC-02'] = dict(
  sub="Toxicology → The Agents → How checkpoint inhibitors and CAR-T work",
  intro="T cells need a ‘go’ signal to attack, and they carry built-in brakes — checkpoints — that stop them attacking the body’s own tissue. Tumours exploit these brakes to hide. Checkpoint inhibitors release the brakes; CAR-T therapy goes further and builds a T cell that cannot miss its target. Both make the immune system stronger, which is why their toxicities look like infection, inflammation and autoimmunity rather than poisoning.",
  parts=[
    ('a', "**PD-1 on T cells binds PD-L1 on the cancer cell, switching the T cell off.** PD-1 is a brake that works late, in the tissues: when an activated T cell meets PD-L1, it becomes exhausted. Normal tissues use PD-L1 to protect themselves during inflammation; many tumours over-express it to do the same."),
    ('b', "**Anti-PD-1 drugs block that binding, so the T cell kills the tumour.** With PD-1 occupied by the antibody, PD-L1 on the tumour has nothing to bind, and the T cell already sitting in the tumour stays active. Because the same brake protects normal organs, those organs can become inflamed too."),
    ('c', "**CTLA-4 competes with CD28 for CD80/86 on antigen-presenting cells and inhibits T-cell activation; blocking it restores activation.** A naive T cell needs two signals: antigen, and co-stimulation when CD28 binds CD80/86. CTLA-4 binds CD80/86 more tightly than CD28 and takes the co-stimulation away. This brake works early, in the lymph node, at priming — so blocking it unleashes a broad range of new T-cell clones, which is why anti-CTLA-4 drugs cause more frequent and more severe immune-related adverse events than anti-PD-1 drugs."),
    ('d', "**The patient’s T cells are collected, given a chimeric antigen receptor gene by a viral vector, expanded and re-infused.** The chimeric receptor joins an antibody fragment that recognises CD19 to the T cell’s own signalling machinery and a co-stimulatory domain, so the cell is activated by contact with the antigen alone. Before re-infusion the patient receives lymphodepleting chemotherapy (usually fludarabine and cyclophosphamide) to make room for the cells to expand."),
  ],
  table=dict(title="Two brakes, two places", head=["", "CTLA-4", "PD-1"], rows=[["Where it acts", "lymph node, at priming", "tissue and tumour, late"], ["Partner", "CD80/86 (outcompetes CD28)", "PD-L1, PD-L2"], ["Drug", "ipilimumab", "nivolumab, pembrolizumab"], ["Toxicity", "more frequent, more severe", "less frequent"]]),
  mimic=[
    ("Checkpoint inhibitor vs CAR-T toxicity", "Checkpoint toxicity is organ-specific autoimmunity that can appear weeks to months later; CAR-T toxicity is a systemic cytokine storm and neurotoxicity in the first days to weeks."),
  ],
  traps=[
    ("“CTLA-4 is a co-stimulatory receptor like CD28”", "It is the opposite: it competes with CD28 for CD80/86 and switches activation off."),
    ("“PD-1 is on the tumour cell”", "PD-1 is on the T cell; PD-L1 is on the tumour (and normal tissues)."),
    ("“CAR-T cells are donor cells”", "The licensed products are autologous — the patient’s own T cells, genetically modified."),
  ],
  decode=[
    ("Which molecule competes with CD28 for B7 (CD80/86)?", "CTLA-4."),
    ("PD-L1 expression on tumour predicts response to", "Anti-PD-1/PD-L1 therapy."),
    ("Autologous T cells modified by a viral vector to recognise CD19", "CAR-T therapy."),
  ],
  punch="Checkpoint inhibitors take the brakes off T cells and CAR-T builds T cells that cannot miss; either way the toxicity is the immune system itself — inflammatory and autoimmune, not toxic in the classical sense.",
)

L['ONC-03'] = dict(
  sub="Toxicology → The Agents → Signature toxicity by class",
  intro="Each class of novel agent fails in its own way, and the way follows from its mechanism. Drugs that free the immune system cause autoimmunity; drugs that activate huge numbers of T cells cause a cytokine storm; antibodies, being foreign proteins, cause infusion and allergic reactions; small-molecule kinase inhibitors hit kinases they were not designed for.",
  parts=[
    ('a', "**Checkpoint inhibitors: immune-related adverse events — pneumonitis, colitis, hepatitis, myocarditis, endocrinopathy.** Released T cells lose tolerance to normal tissue, so any organ can be inflamed; the gut, skin, liver, lungs and endocrine glands are the usual ones. Myocarditis is uncommon but the most often fatal."),
    ('b', "**CAR-T cells: cytokine release syndrome; ICANS.** Activated CAR-T cells release cytokines that recruit macrophages, which pour out IL-6 and IL-1 — the systemic storm (ONC-04). The same activation affects the brain’s endothelium and the blood–brain barrier, giving neurotoxicity (ONC-07)."),
    ('c', "**Monoclonal antibodies: infusion reactions, cytokine release, Kounis syndrome, PRES.** An infused foreign protein can trigger mast-cell release or complement activation; when mast-cell mediators reach the coronary arteries the result is an allergic acute coronary syndrome — Kounis syndrome (ONC-11). Anti-VEGF antibodies raise blood pressure and injure endothelium, the setting for posterior reversible encephalopathy syndrome."),
    ('d', "**Tyrosine kinase inhibitors: QT prolongation, pleural effusion (dasatinib), thrombosis, PRES, tumour lysis.** Several TKIs block the cardiac hERG potassium channel and lengthen the QT. Dasatinib causes an exudative, lymphocyte-rich pleural effusion, thought to reflect off-target inhibition of PDGFR and Src kinases; it can also cause pulmonary arterial hypertension. Rapid killing of a sensitive leukaemia releases intracellular contents — tumour lysis."),
  ],
  table=dict(title="Mechanism to toxicity", head=["Class", "Mechanism of harm", "Signature"], rows=[["Checkpoint inhibitor", "loss of self-tolerance", "irAEs (colitis, pneumonitis, hepatitis…)"], ["CAR-T, bispecifics", "mass T-cell activation", "CRS, ICANS"], ["Monoclonal antibody", "foreign protein, mast cells", "infusion reaction, Kounis"], ["TKI", "off-target kinases, hERG", "QT, effusion (dasatinib)"], ["Bevacizumab", "VEGF loss in endothelium", "hypertension, TMA, PRES, thrombosis"]]),
  mimic=[
    ("Checkpoint pneumonitis vs dasatinib effusion", "The first is inflammation of the lung itself (ground-glass, organising pneumonia on CT); the second is fluid in the pleural space with relatively normal lung."),
  ],
  traps=[
    ("“Cytokine release syndrome is a checkpoint-inhibitor toxicity”", "It is the signature of CAR-T cells and bispecific antibodies; checkpoint inhibitors cause organ-specific irAEs."),
    ("“Bevacizumab’s main risk is bleeding only”", "It also causes arterial and venous thrombosis, thrombotic microangiopathy, hypertension and PRES."),
  ],
  decode=[
    ("Pleural effusion in a CML patient on a TKI", "Dasatinib."),
    ("Colitis, hepatitis or hypophysitis in a melanoma patient", "Checkpoint inhibitor irAE."),
    ("Hypertension, proteinuria and seizures with occipital oedema on an anti-VEGF drug", "Bevacizumab-related PRES."),
  ],
  punch="Read the toxicity from the mechanism: freed T cells cause autoimmunity, mass T-cell activation causes a cytokine storm, foreign antibodies cause allergy, and kinase inhibitors hit the wrong kinases.",
  extra=[dict(q="Adrenal insufficiency on a checkpoint inhibitor: usual cause and first step?", a="Usually **hypophysitis** (classically ipilimumab): low ACTH, often with low TSH and gonadotrophins. **Hydrocortisone first, before thyroxine**; replacement is usually lifelong.")],
)

L['ONC-04'] = dict(
  sub="Toxicology → Cytokine Release Syndrome → Causes, picture and labs",
  intro="When CAR-T cells or a bispecific antibody meet their target, thousands of T cells are activated at once. They release interferon-γ and other cytokines that switch on monocytes and macrophages, and these produce most of the IL-6. IL-6 and its partners activate the endothelium everywhere, so capillaries leak — and the patient looks exactly like someone in septic shock, usually within the first days after infusion.",
  parts=[
    ('a', "**CAR-T cells, bispecific antibodies (blinatumomab), muromonab (OKT3).** All three activate T cells en masse: CAR-T through the engineered receptor, blinatumomab by linking CD3 to CD19, and muromonab — an older anti-CD3 antibody used against transplant rejection — by binding CD3 directly."),
    ('b', "**80–85% after CAR-T; about 20% need vasopressors.** Most patients have at least fever, because the same T-cell expansion that kills the tumour drives the cytokines. Severity rises with tumour burden and the dose of cells, and the rates differ between products — CRS of any grade ranges from roughly 60% to over 90% in the pivotal trials, highest with CD28-based products such as axicabtagene ciloleucel."),
    ('c', "**IL-6, IL-8, IL-10; von Willebrand factor and angiopoietin-2 (endothelial activation).** IL-6 is the central mediator. Endothelial cells lack the membrane IL-6 receptor, but IL-6 bound to the soluble receptor can still signal through their gp130 (trans-signalling); activated endothelium releases angiopoietin-2 and von Willebrand factor from its storage granules. That is the capillary leak and the coagulopathy."),
    ('d', "**Fever first; then hypotension, hypoxaemia (non-cardiogenic oedema), arrhythmia, oliguria, confusion.** Fever is the earliest sign because cytokines reset the hypothalamus. Leaky capillaries then cause vasodilatory hypotension and fluid in the alveoli, poor renal perfusion gives oliguria, and cytokines and leak cause arrhythmia and cardiac dysfunction."),
    ('e', "**Raised CRP and procalcitonin; hypokalaemia, raised urea; altered counts and coagulation. Ferritin also rises.** CRP and ferritin are made in response to IL-6, so they track the storm. Cytopenias reflect the lymphodepleting chemotherapy as well as the inflammation, and endothelial activation consumes clotting factors (low fibrinogen, DIC). Procalcitonin can rise in CRS too, so it does not reliably separate CRS from sepsis."),
  ],
  mimic=[
    ("CRS vs sepsis", "Identical bedside picture in a patient who is neutropenic after lymphodepletion; timing after infusion suggests CRS, but cultures and empirical antibiotics are always started."),
    ("CRS vs HLH-like syndrome", "Both have fever and very high ferritin; a ferritin that keeps climbing with cytopenias, liver failure and low fibrinogen after CRS settles suggests the haemophagocytic picture."),
  ],
  traps=[
    ("“A raised procalcitonin proves infection rather than CRS”", "Procalcitonin can rise in CRS; neither it nor CRP separates them — treat both."),
    ("“The hypoxaemia of CRS is cardiogenic pulmonary oedema”", "It is mainly capillary leak — non-cardiogenic."),
    ("“CRS is a checkpoint-inhibitor toxicity”", "It follows therapies that activate T cells en masse: CAR-T, bispecifics, OKT3."),
  ],
  decode=[
    ("Fever and hypotension 3 days after CAR-T infusion", "CRS — but culture and give antibiotics."),
    ("Key cytokine in CRS", "IL-6."),
    ("Markers of endothelial activation in CRS", "Angiopoietin-2, von Willebrand factor."),
  ],
  punch="Mass T-cell activation drives macrophage IL-6, IL-6 opens the capillaries, and the patient looks septic — so CRS is graded and treated, but infection is always covered too.",
)

L['ONC-05'] = dict(
  sub="Toxicology → Cytokine Release Syndrome → ASTCT grading",
  intro="The current consensus (ASTCT) grading of cytokine release syndrome rests on three things a bedside clinician can see: fever, blood pressure and oxygen. Fever establishes that it is CRS; the grade is then set by how much support the circulation and the lungs need. Grading by treatment intensity, rather than by numbers, makes it easy to apply across centres.",
  parts=[
    ('a', "**Grade 1: fever, no hypotension, no hypoxia.** The cytokines have reset the thermostat but the capillaries are not yet leaking enough to drop pressure or oxygen."),
    ('b', "**Grade 2: hypotension not needing a vasopressor; hypoxia needing low-flow nasal oxygen.** The leak has begun: pressure responds to fluid, and a little oxygen by nasal cannula (up to about 6 L/min) corrects saturation."),
    ('c', "**Grade 3: one vasopressor (with or without vasopressin); high-flow oxygen, face mask or non-rebreather.** Vasodilatation now needs a pressor, and alveolar flooding needs more than 6 L/min — high-flow nasal oxygen, a face mask, a non-rebreather or a Venturi mask. The ASTCT consensus deliberately does not count vasopressin as a second agent, so noradrenaline plus vasopressin is still grade 3."),
    ('d', "**Grade 4: multiple vasopressors (not counting vasopressin); positive pressure (CPAP, BiPAP, ventilation).** Shock needs two or more catecholamines, or the lungs need pressure to stay open. Positive pressure, not the oxygen flow, is what defines grade 4 on the hypoxia side."),
  ],
  table=dict(title="Fever plus the worse of two columns", head=["Grade", "Circulation", "Oxygen"], rows=[["1", "normal", "none"], ["2", "fluid-responsive, no pressor", "low-flow nasal"], ["3", "**one** pressor ± vasopressin", "**high-flow**, mask, non-rebreather"], ["4", "**multiple** pressors", "**positive pressure**"]]),
  mimic=[
    ("Grade 3 vs grade 4 hypoxia", "High-flow nasal oxygen or a non-rebreather is grade 3; CPAP, BiPAP or intubation is grade 4."),
  ],
  traps=[
    ("“CRS can be graded without fever”", "Fever of 38 °C or more is required to diagnose it. Once antipyretics, tocilizumab or steroids have suppressed the fever, the grade is then followed by blood pressure and oxygen alone."),
    ("“Noradrenaline plus vasopressin is grade 4”", "Vasopressin is not counted: one catecholamine with or without vasopressin is grade 3."),
    ("“Grade 3 CRS needs positive-pressure ventilation”", "Positive pressure defines grade 4 (ONC-13)."),
  ],
  decode=[
    ("Fever, BP held on noradrenaline alone, on a non-rebreather", "Grade 3 CRS."),
    ("Fever, no pressor, 2 L/min nasal oxygen", "Grade 2 CRS."),
    ("Fever, on BiPAP", "Grade 4 CRS."),
  ],
  punch="Fever makes it CRS, and the grade is the support the patient needs — no pressor or low-flow oxygen is 2, one pressor or high-flow is 3, several pressors or positive pressure is 4, whichever column is worse.",
)

L['ONC-06'] = dict(
  sub="Toxicology → Cytokine Release Syndrome → Treatment by grade",
  intro="The treatment of CRS escalates with the grade. Mild disease is supported while infection is excluded. Once the circulation or lungs are involved, IL-6 — the central mediator — is blocked; if that is not enough, broad immunosuppression with steroids is added. The tension is that steroids may also blunt the CAR-T cells that are fighting the cancer, so they are reserved for the more severe grades.",
  parts=[
    ('a', "**Grade 1: supportive — antipyretics, fluids, cultures, empirical antibiotics.** The patient is often neutropenic after lymphodepletion, so a fever is treated as possible sepsis until proven otherwise."),
    ('b', "**Grade 2: tocilizumab (maximum 3 doses); consider ICU.** Tocilizumab (8 mg/kg IV, no more than 800 mg a dose) blocks the IL-6 receptor and usually breaks the fever and hypotension within hours. It can be repeated after 8 hours if there is no response; guidelines cap it at 3 doses in 24 hours and 4 in total. If hypotension persists after fluids and one or two doses, dexamethasone 10 mg IV every 12–24 hours is added."),
    ('c', "**Grade 3: ICU; tocilizumab or siltuximab plus dexamethasone 10–20 mg 6-hourly.** A patient on a vasopressor or high-flow oxygen needs ICU care. Siltuximab is the alternative (off-label) IL-6 blocker. Most protocols use dexamethasone 10 mg every 6 hours and escalate the dose if there is no response. Dexamethasone suppresses cytokine production across the board and, being lipophilic, also crosses into the brain — useful because ICANS often accompanies severe CRS."),
    ('d', "**Grade 4: anti-IL-6 plus methylprednisolone 1 g pulse; anakinra if refractory.** At this point survival outweighs any worry about the anti-tumour effect, so the steroid dose is maximal: methylprednisolone 1 g daily, usually for 3 days, then a rapid taper (many protocols start with dexamethasone 10 mg 6-hourly and switch to methylprednisolone if that fails). Anakinra blocks the IL-1 receptor, a separate macrophage pathway that IL-6 blockade does not reach."),
  ],
  table=dict(title="Which drug blocks what", head=["Drug", "Binds", "Result"], rows=[["Tocilizumab", "**IL-6 receptor** (membrane and soluble)", "blocks signalling; serum IL-6 rises"], ["Siltuximab", "**IL-6** itself", "neutralises the cytokine"], ["Anakinra", "IL-1 receptor", "blocks the IL-1 pathway"], ["Steroids", "—", "broad suppression; may blunt CAR-T"]]),
  mimic=[
    ("Tocilizumab vs siltuximab", "Tocilizumab blocks the receptor (so IL-6 accumulates in the blood); siltuximab binds and removes the cytokine itself."),
  ],
  traps=[
    ("“Tocilizumab binds IL-6”", "It binds the IL-6 receptor; siltuximab binds IL-6."),
    ("“Give steroids first for any CRS”", "Steroids are kept for grade 2 refractory to tocilizumab and for grades 3–4, because they may blunt the CAR-T effect."),
    ("“Fever settled after tocilizumab, so the CRS is over”", "Tocilizumab removes fever quickly; follow blood pressure and oxygen, and watch for ICANS."),
  ],
  decode=[
    ("Grade 2 CRS — first drug?", "Tocilizumab."),
    ("Grade 4 CRS on tocilizumab — add?", "Methylprednisolone 1 g/day."),
    ("CRS refractory to IL-6 blockade and steroids", "Anakinra (IL-1 receptor antagonist)."),
  ],
  punch="CRS treatment climbs with the grade: support for 1, IL-6 blockade for 2, add dexamethasone for 3, pulse methylprednisolone and IL-1 blockade for 4 — tocilizumab blocks the receptor, siltuximab the cytokine.",
  extra=[dict(q="Why does serum IL-6 rise after tocilizumab?", a="Tocilizumab blocks the **IL-6 receptor** (membrane and soluble), so IL-6 is no longer taken up and cleared through it — the level in the blood **rises** even as signalling stops.")],
)
FLAGS['ONC-06'] = "Tocilizumab ‘maximum 3 doses’: current guidance (NCCN, ASCO, product labels) is a maximum of 3 doses in 24 hours and 4 doses in total. The WATCH’s ‘older NCI triggers’ (LVEF <40%, creatinine >2.5 × baseline, noradrenaline >2 µg/min for 48 h) are correctly quoted from the NCI criteria (Kroschinsky 2017, Crit Care, Table 3) but are pre-ASTCT and no longer used to decide tocilizumab."

L['ONC-07'] = dict(
  sub="Toxicology → Neurotoxicity (ICANS) → Definition, picture and treatment",
  intro="A few days after CAR-T infusion, often as the cytokine storm peaks or just after it, some patients develop a brain disorder of their own. Cytokines and activated endothelium make the blood–brain barrier leak, and inflammatory mediators reach the cerebrospinal fluid. Language and handwriting fail first, which is why the bedside screen tests them so carefully (ONC-08).",
  parts=[
    ('a', "**Immune effector cell-associated neurotoxicity syndrome.** The name is deliberately broad: it is the neurotoxicity of any therapy that works by activating immune effector cells, not only CAR-T."),
    ('b', "**CAR-T cells and bispecific antibodies.** Both activate large numbers of T cells and produce the same cytokine and endothelial injury that underlies CRS."),
    ('c', "**Tremor, dysgraphia, aphasia, cerebellar signs, encephalopathy, seizures.** Expressive language and writing are the most sensitive early functions — a change in handwriting may be the first sign — progressing to confusion and drowsiness as the encephalopathy deepens."),
    ('d', "**Status epilepticus, coma, paresis, cerebral oedema.** Severe barrier breakdown lets fluid into the brain; diffuse cerebral oedema can be fulminant and fatal, so falling consciousness or papilloedema needs urgent imaging and ICU care."),
    ('e', "**Corticosteroids.** Dexamethasone crosses the blood–brain barrier and suppresses the inflammation inside the brain. Tocilizumab does not cross the barrier, so it does not treat isolated ICANS; by blocking the receptor it raises serum IL-6, which may reach the CSF and make ICANS worse."),
  ],
  mimic=[
    ("ICANS vs CRS", "CRS is systemic (fever, hypotension, hypoxia) and responds to tocilizumab; ICANS is neurological and responds to steroids. They often overlap, but ICANS can occur without CRS."),
    ("ICANS vs CNS infection or bleeding", "The patient is immunosuppressed and often thrombocytopenic; imaging, and lumbar puncture when safe, exclude infection and haemorrhage."),
  ],
  traps=[
    ("“Give tocilizumab for ICANS”", "It does not cross the blood–brain barrier and may worsen isolated ICANS; use steroids."),
    ("“ICANS occurs only with CRS”", "It can occur on its own, and may appear after CRS has settled."),
  ],
  decode=[
    ("Change in handwriting and word-finding difficulty after CAR-T", "Early ICANS."),
    ("ICANS without CRS — drug of choice?", "Dexamethasone."),
    ("ICANS — full form", "Immune effector cell-associated neurotoxicity syndrome."),
  ],
  punch="ICANS is the cytokine storm reaching the brain through a leaky barrier: writing and language fail first, and because tocilizumab cannot follow it across the barrier, steroids are the treatment.",
)

L['ONC-08'] = dict(
  sub="Toxicology → Neurotoxicity (ICANS) → The ICE score",
  intro="Because writing and language fail early in ICANS, a quick ten-point bedside screen — the immune effector cell-associated encephalopathy (ICE) score — tests exactly those functions. It is repeated several times a day while the patient is at risk, and a falling score is often the first warning. It forms one domain of the ICANS grade; the others are consciousness, seizures, motor weakness and cerebral oedema (ONC-09).",
  parts=[
    ('a', "**Orientation 4 (year, month, city, hospital); naming three objects 3; following a simple command 1; writing a standard sentence 1; counting back from 100 by tens 1.** Orientation tests global encephalopathy; naming detects expressive aphasia, one of the most characteristic early signs; the writing task picks up early dysgraphia; counting backwards tests attention. The total is 10, and 10 is normal."),
    ('b', "**Grade 1: 7–9; grade 2: 3–6; grade 3: 0–2; grade 4: 0, unarousable.** The lower the score, the worse the encephalopathy. A score of 0 can mean grade 3 or grade 4: it is grade 4 when the patient cannot be roused to attempt the test, so consciousness rather than the score decides."),
  ],
  table=dict(title="ICE score to ICANS grade", head=["ICE score", "Grade"], rows=[["10", "no ICANS"], ["7–9", "1"], ["3–6", "2"], ["0–2", "3"], ["0, unarousable", "4"]]),
  mimic=[
    ("ICE score vs Glasgow Coma Scale", "Both are scored so that lower is worse, but the ICE score tests cognition and language in an awake patient; it cannot be done in the unarousable patient, who is graded on consciousness."),    ("ICE score vs CAPD", "The ICE score is for adults and older children; under 12 years the ASTCT grading uses the Cornell Assessment of Pediatric Delirium instead."),
  ],
  traps=[
    ("“A higher ICE score means worse neurotoxicity”", "Lower is worse; 10 is normal (ONC-13)."),
    ("“The ICE score alone gives the ICANS grade”", "The grade is the worst of five domains — ICE, consciousness, seizure, motor findings, raised ICP/oedema."),
  ],
  decode=[
    ("ICE score 5 after CAR-T", "Grade 2 ICANS (if no worse domain)."),
    ("Which ICE domain carries 4 points?", "Orientation."),
    ("ICE score 8", "Grade 1."),
  ],
  punch="The ICE score is a ten-point test of the functions ICANS breaks first — orientation, naming, writing and attention — so a lower score means worse neurotoxicity: 7–9 is grade 1, 3–6 grade 2, 0–2 grade 3.",
)

L['ONC-09'] = dict(
  sub="Toxicology → Neurotoxicity (ICANS) → Grades and treatment",
  intro="The ICE score covers only cognition. A patient can score poorly because he is drowsy, or score zero because he is seizing or comatose. So the ASTCT grade also takes level of consciousness, seizures, motor weakness and signs of raised intracranial pressure, and the overall grade is set by the worst of these. Treatment escalates with it: observation, then steroids, then ICU care for seizures and oedema.",
  parts=[
    ('a', "**Grade 1: wakes spontaneously — monitor; imaging, EEG.** The patient is awake but mildly encephalopathic (ICE 7–9). Imaging excludes haemorrhage and other causes, and EEG looks for non-convulsive seizures; many centres also give levetiracetam prophylaxis."),
    ('b', "**Grade 2: wakes to voice — consider steroids; lumbar puncture.** A single dose of dexamethasone 10 mg IV is usual, repeated 6–12-hourly if there is no improvement. Lumbar puncture, when platelets and coagulation allow, excludes infection in an immunosuppressed patient."),
    ('c', "**Grade 3: wakes to touch only; any seizure that resolves; focal oedema on imaging — ICU; dexamethasone 10 mg 6-hourly; antiepileptics.** Needing a touch to wake means the airway is at risk, and any seizure — even one that stops — signals cortical irritation, so ICU care and full-dose steroids follow."),
    ('d', "**Grade 4: unarousable; prolonged seizure (>5 min); hemiparesis; diffuse oedema, papilloedema — as for grade 3, plus anakinra or cyclophosphamide (experimental); treat raised ICP.** Status epilepticus and diffuse cerebral oedema can be fatal within hours. Raised ICP is treated with the usual measures — head up, hyperosmolar therapy, controlled ventilation — and the steroid is escalated: ASCO and NCCN advise methylprednisolone 1 g IV daily for 3 days rather than continuing dexamethasone."),
  ],
  table=dict(title="Worst domain sets the grade", head=["Domain", "Grade 3", "Grade 4"], rows=[["Consciousness", "wakes to touch", "unarousable"], ["Seizure", "any clinical seizure that resolves, or EEG seizure settling with treatment", "prolonged >5 min, or repeated without recovery"], ["Motor", "—", "hemiparesis, paraparesis"], ["Imaging / ICP", "focal oedema", "diffuse oedema, papilloedema"]]),
  mimic=[
    ("ICANS grade 3 vs 4 seizure", "A seizure that stops is grade 3; one lasting over 5 minutes, or repeated without recovery in between, is grade 4."),
  ],
  traps=[
    ("“A single brief seizure is grade 2”", "Any clinical seizure that resolves is grade 3."),
    ("“Focal oedema on imaging is grade 4”", "Focal oedema is grade 3; diffuse oedema is grade 4."),
  ],
  decode=[
    ("ICANS, rousable only to touch", "Grade 3 — ICU, dexamethasone."),
    ("ICANS with papilloedema and diffuse oedema", "Grade 4."),
    ("ICANS grade 3 steroid", "Dexamethasone 10 mg IV 6-hourly."),
  ],
  punch="ICANS is graded by its worst sign — voice is 2, touch or any seizure or focal oedema is 3, coma, status, hemiparesis or diffuse oedema is 4 — and steroids, ICU care and ICP control escalate in step.",
)
FLAGS['ONC-09'] = "Grade 4 treatment ‘as 3’ implies dexamethasone; standard guidance (ASCO/NCCN) for grade 4 ICANS is high-dose methylprednisolone 1 g/day (usually 3 days) — card omits it."

L['ONC-10'] = dict(
  sub="Toxicology → Organ Toxicities → General management of immune-related adverse events",
  intro="An immune-related adverse event is the immune system attacking a normal organ after its brakes have been removed. The logic of treatment is therefore the logic of autoimmune disease: stop feeding the attack, exclude the alternatives, suppress the immune response, and come off suppression slowly. The added question in oncology is whether the cancer drug can ever be restarted.",
  parts=[
    ('a', "**Hold the drug; exclude infection and pre-existing autoimmune disease.** The antibody keeps working for weeks, so holding it does not end the attack but stops adding to it. Infection must be excluded first because the treatment is immunosuppression, and a flare of known autoimmune disease is managed differently."),
    ('b', "**Prednisolone 1–2 mg/kg/day or equivalent.** High-dose steroids suppress the activated T cells. This dose is for grade 3–4 events; grade 2 events usually get 0.5–1 mg/kg. Steroids at this point do not appear to undermine the anti-tumour effect enough to withhold them."),
    ('c', "**If no response in 5–7 days, add another immunosuppressant: infliximab for colitis; mycophenolate for hepatitis.** Current ASCO and ESMO guidance does not wait that long: for most organs an event is steroid-refractory after about 48–72 hours of IV steroids without improvement, because a fulminant colitis or pneumonitis can perforate or kill within days. Infliximab blocks TNF-α, which drives checkpoint colitis (vedolizumab is the gut-selective alternative). It is avoided in hepatitis because it is itself hepatotoxic, so mycophenolate is used there instead."),
    ('d', "**Taper slowly, over 4 weeks.** The activated T cells persist, so a fast taper is followed by a flare; tapering usually takes 4–6 weeks, and prolonged steroids need Pneumocystis prophylaxis."),
    ('e', "**After a grade 3 or 4 event, stop the checkpoint inhibitor permanently.** A life-threatening attack is likely to recur on re-exposure, so grade 4 events, and myocarditis of any grade, mean permanent discontinuation. After some grade 3 events (for example anti-PD-1 colitis) guidelines allow cautious rechallenge once the event has settled to grade 1. The exception is endocrine disease, where the damaged gland is simply replaced with hormone and the drug can usually be resumed once the patient is stable."),
  ],
  mimic=[
    ("Checkpoint colitis vs infective diarrhoea", "Both cause diarrhoea; stool tests for C. difficile and pathogens come first, and colitis that persists with negative tests on a checkpoint inhibitor gets steroids."),
  ],
  traps=[
    ("“Infliximab for steroid-refractory checkpoint hepatitis”", "Infliximab is hepatotoxic; mycophenolate is used for hepatitis."),
    ("“Endocrine irAEs need high-dose steroids and permanent discontinuation”", "Hormone replacement treats them, and the drug can usually be resumed."),
    ("“Stop steroids once the symptoms settle”", "Taper over at least 4 weeks or the irAE flares."),
  ],
  decode=[
    ("Grade 3 colitis on ipilimumab, no response to IV steroids", "Infliximab."),
    ("Steroid-refractory immune hepatitis", "Mycophenolate."),
    ("Grade 4 pneumonitis on pembrolizumab — after recovery?", "Do not rechallenge."),
  ],
  punch="Treat an irAE like an autoimmune disease you caused: hold the drug, rule out infection, give high-dose steroids, add infliximab or mycophenolate if they fail, taper slowly — and do not rechallenge after a severe event unless the gland can just be replaced.",
)
FLAGS['ONC-10'] = "c: ‘no response in 5–7 days’ — current ASCO/ESMO guidance defines steroid-refractory as no improvement after about 48–72 h of high-dose steroids. e: permanent discontinuation is the rule for grade 4 (and for any-grade myocarditis); after some grade 3 events (e.g. anti-PD-1 colitis) rechallenge can be considered after recovery to grade 1 or less."

L['ONC-11'] = dict(
  sub="Toxicology → Organ Toxicities → Neurological and cardiac toxicities",
  intro="Neurological and cardiac complications of novel agents are rare but among the most dangerous. Some are autoimmune (checkpoint inhibitors attacking nerve, muscle, meninges or myocardium); some are vascular (anti-VEGF drugs and TKIs raising blood pressure and damaging endothelium); and some are allergic (antibodies releasing mast-cell mediators into the coronaries). The mechanism dictates the treatment.",
  parts=[
    ('a', "**Guillain–Barré, myasthenia: anti-PD-1/PD-L1, sunitinib — IVIG, plasma exchange, steroids.** The sunitinib link rests on case reports; the checkpoint inhibitors are the main cause. Checkpoint blockade releases T cells and antibodies against nerve and neuromuscular junction. Unlike classical Guillain–Barré, the checkpoint form is treated with steroids as well as IVIG or plasma exchange, because the attack is T-cell driven. Myasthenia can overlap with myositis and myocarditis, so check the troponin and CK."),
    ('b', "**PRES: monoclonals, TKIs — stop the drug, control BP.** Anti-VEGF agents raise blood pressure and injure endothelium; when pressure exceeds the brain’s autoregulation, fluid leaks into the posterior white matter. Removing the cause and lowering the pressure usually reverses it."),
    ('c', "**Aseptic meningitis: monoclonals, checkpoint inhibitors — steroids, IVIG, rituximab.** Immune inflammation of the meninges gives headache, neck stiffness and a lymphocytic CSF; infection must be excluded before steroids, with rituximab for refractory immune encephalitis."),
    ('d', "**Myocarditis: checkpoint inhibitors — high-dose steroids, IVIG.** T cells infiltrate the myocardium, usually within the first weeks of treatment, causing conduction block, arrhythmia and heart failure; it is the most often fatal irAE. Pulse methylprednisolone (500–1000 mg IV daily for 3–5 days) is given early, before biopsy if need be, and the drug is stopped permanently; refractory cases get further agents such as mycophenolate or abatacept."),
    ('e', "**Kounis syndrome: monoclonal antibodies — treat as ACS plus anaphylaxis; morphine with caution.** Mast-cell histamine, leukotrienes and proteases cause coronary spasm or plaque rupture during an allergic reaction. Morphine itself releases histamine from mast cells, so it can deepen the reaction."),
    ('f', "**Acute coronary syndrome: bevacizumab, trastuzumab — treat as ACS.** Anti-VEGF therapy damages endothelium and promotes arterial thrombosis, so bevacizumab raises the risk of myocardial infarction and stroke (and also causes hypertension and heart failure). Trastuzumab is a weaker fit: HER2 signalling keeps stressed cardiomyocytes alive, so blocking it causes left ventricular systolic dysfunction that usually recovers when the drug is stopped — heart failure, not coronary occlusion, and worse after anthracyclines. The other classic drug cause of ACS is 5-fluorouracil (and capecitabine), which causes coronary vasospasm, typically chest pain during or soon after the infusion; it is treated by stopping the infusion and giving nitrates or a calcium-channel blocker."),
  ],
  table=dict(title="Mechanism to treatment", head=["Syndrome", "Mechanism", "Key treatment"], rows=[["GBS, myasthenia (ICI)", "autoimmune, T-cell", "IVIG/PLEX **plus steroids**"], ["PRES", "hypertension, endothelial injury", "stop drug, lower BP"], ["Myocarditis (ICI)", "T-cell infiltration", "pulse steroids, stop for good"], ["Kounis", "mast-cell mediators in coronaries", "ACS + anaphylaxis care"], ["Bevacizumab", "arterial thrombosis, endothelial injury", "as ACS; stop drug"], ["5-FU, capecitabine", "coronary vasospasm", "stop infusion; nitrate, calcium-channel blocker"], ["Trastuzumab", "HER2 loss in cardiomyocytes", "LV dysfunction: stop, heart-failure therapy"]]),
  mimic=[
    ("Checkpoint myocarditis vs ACS", "Both raise troponin; myocarditis comes weeks after starting a checkpoint inhibitor, often with conduction block and myositis, and the coronaries are normal."),
    ("Kounis syndrome vs simple anaphylaxis", "Kounis adds ischaemic chest pain and ST change during the allergic reaction."),
  ],
  traps=[
    ("“Steroids are not used in Guillain–Barré”", "True for classical GBS, but checkpoint-related GBS is treated with steroids as well as IVIG or plasma exchange."),
    ("“Morphine is safe analgesia in Kounis syndrome”", "It releases histamine and may worsen the reaction; use it with caution."),
    ("“Checkpoint myocarditis is mild and self-limiting”", "It is the most often fatal irAE; give pulse steroids early and stop the drug permanently."),
    ("“Trastuzumab’s cardiotoxicity is myocardial infarction”", "Its signature is reversible LV systolic dysfunction; the drugs that cause ACS are bevacizumab (thrombosis) and 5-FU or capecitabine (vasospasm)."),
  ],
  decode=[
    ("Ptosis, myalgia and raised troponin 3 weeks after nivolumab", "Myasthenia with myositis and myocarditis overlap — high-dose steroids."),
    ("Chest pain with urticaria during a rituximab infusion", "Kounis syndrome."),
    ("Chest pain and ST elevation during a 5-FU infusion, normal coronaries", "5-FU coronary vasospasm — stop the infusion, give nitrate."),
    ("Falling LVEF on adjuvant trastuzumab after anthracyclines", "Trastuzumab cardiomyopathy — usually reversible on stopping."),
    ("Headache, seizures, cortical blindness, posterior oedema, high BP on bevacizumab", "PRES."),
  ],
  punch="Read each syndrome by its mechanism: autoimmune ones need steroids even when classical teaching says otherwise, vascular ones need the drug stopped and the pressure lowered, and allergic coronary events need ACS and anaphylaxis care together.",
  extra=[dict(q="Classic transplant cause of PRES, and its management?", a="**Calcineurin inhibitors (ciclosporin, tacrolimus)**: seizures, hypertension, cortical blindness, parieto-occipital vasogenic oedema. **Withdraw or switch the CNI and control BP** — usually reversible.")],
)
FLAGS['ONC-11'] = "ACS row lists trastuzumab: trastuzumab’s signature cardiotoxicity is (usually reversible) LV systolic dysfunction / heart failure, not ACS; the classic ACS-causing cancer drugs are bevacizumab (arterial thrombosis) and fluoropyrimidines (5-FU, capecitabine — vasospasm). GBS/myasthenia row lists sunitinib: supported only by case reports. Myocarditis row omits the key step — permanent discontinuation of the checkpoint inhibitor at any grade, with methylprednisolone 500–1000 mg/day."

L['ONC-12'] = dict(
  sub="Toxicology → Organ Toxicities → Lung, kidney, endocrine and liver",
  intro="Any organ can be injured by these drugs, and the ICU question is always the same: is this the drug, the cancer, or an infection in an immunosuppressed patient? The answer decides whether to give steroids — which help immune toxicity but harm infection. Each organ also has a typical culprit, which narrows the list.",
  parts=[
    ('a', "**Pneumonitis: separate infection (Pneumocystis, CMV) from drug (anti-PD-1, rituximab, dasatinib) by CT and bronchoalveolar lavage; then steroids.** Both give ground-glass change and hypoxaemia. Rituximab and steroids predispose to Pneumocystis and CMV, which steroids would worsen, so lavage for organisms comes before treating drug pneumonitis."),
    ('b', "**Renal: checkpoint inhibitors — tubulointerstitial nephritis, median onset 3 months; anti-VEGF — thrombotic microangiopathy; rituximab, TKIs — tumour lysis.** Released T cells infiltrate the renal interstitium; a proton-pump inhibitor or NSAID taken at the same time is a common co-trigger, which is why these are stopped. VEGF maintains the glomerular endothelium, so blocking it causes proteinuria and renal-limited TMA. Rapid tumour killing releases uric acid, phosphate and potassium."),
    ('c', "**Hypophysitis: anti-CTLA-4 (ipilimumab) — headache, visual disturbance, pituitary failure; MRI and hormone levels; replace hormones.** An inflamed, swollen pituitary causes headache and, rarely, compresses the chiasm. ACTH deficiency is the dangerous loss: give hydrocortisone before thyroxine, because thyroxine speeds cortisol metabolism and can precipitate adrenal crisis. Aldosterone is preserved (the renin–angiotensin system is intact), so hyperkalaemia is absent."),
    ('d', "**Thyroid: hypo- or hyperthyroidism in 1–10%.** Thyroiditis often starts with a transient thyrotoxic phase as stored hormone leaks out, followed by permanent hypothyroidism. Primary thyroid disease is more typical of anti-PD-1 drugs, hypophysitis of anti-CTLA-4."),
    ('e', "**Hepatitis: 5–10%; from transaminitis to fulminant failure; steroids.** It is usually asymptomatic and found on routine tests, commoner with combined anti-CTLA-4 and anti-PD-1 therapy. Viral hepatitis, other drugs and liver metastases are excluded first; refractory cases get mycophenolate, not infliximab (ONC-10)."),
  ],
  mimic=[
    ("Hypophysitis vs primary adrenalitis", "Hypophysitis: low ACTH, other pituitary hormones low, no hyperkalaemia. Primary adrenal failure (rare with checkpoint inhibitors): high ACTH, hyperkalaemia from aldosterone loss."),
    ("Checkpoint nephritis vs anti-VEGF kidney injury", "Nephritis gives sterile pyuria and white-cell casts; anti-VEGF TMA gives proteinuria, hypertension and sometimes schistocytes."),
  ],
  traps=[
    ("“Start steroids for pneumonitis straight away”", "Exclude Pneumocystis and CMV with BAL first — steroids worsen them."),
    ("“In hypophysitis replace thyroxine first”", "Hydrocortisone first, or thyroxine may precipitate adrenal crisis."),
    ("“Hypophysitis is typical of anti-PD-1 drugs”", "It is typical of anti-CTLA-4 (ipilimumab); anti-PD-1 drugs more often cause primary thyroiditis."),
  ],
  decode=[
    ("Headache, fatigue, low sodium, low ACTH and TSH on ipilimumab", "Hypophysitis — hydrocortisone first, then MRI."),
    ("Rising creatinine with sterile pyuria 3 months into pembrolizumab", "Tubulointerstitial nephritis."),
    ("Ground-glass opacities on rituximab", "BAL for Pneumocystis and CMV before steroids."),
  ],
  punch="In every organ the first step is to separate drug from infection and cancer, and the treatment follows the mechanism: steroids for immune injury, hormone replacement for a destroyed gland — cortisol before thyroxine — and stopping the drug for vascular injury.",
  extra=[dict(q="New hyperglycaemia or DKA on anti-PD-1 therapy?", a="**Checkpoint-induced type 1 diabetes** (β-cell destruction): treat with **insulin**; steroids do not reverse it.")],
)

L['ONC-13'] = dict(
  sub="Toxicology → Organ Toxicities → True or false",
  intro="This card checks the deck’s key distinctions. Each statement turns on one detail met earlier; the reason for each answer is the mechanism behind it.",
  parts=[
    ('a', "**False — blinatumomab targets CD3 and CD19.** It is a bispecific T-cell engager joining a T cell to a B cell; CD20 is rituximab’s target (ONC-01)."),
    ('b', "**True — ipilimumab blocks CTLA-4,** the early brake that competes with CD28 for CD80/86 (ONC-02)."),
    ('c', "**False — fever is required.** Fever of 38 °C or more is what makes it CRS; the grade then comes from blood pressure and oxygen, which are followed alone once antipyretics or tocilizumab have masked the fever (ONC-05)."),
    ('d', "**False — positive-pressure ventilation is grade 4.** Grade 3 is high-flow oxygen, face mask or non-rebreather (ONC-05)."),
    ('e', "**True — tocilizumab blocks the IL-6 receptor;** siltuximab binds IL-6 itself (ONC-06)."),
    ('f', "**False — a lower ICE score is worse.** The score counts tasks done correctly out of 10 (ONC-08)."),
    ('g', "**True — hypophysitis is typical of anti-CTLA-4 therapy.** Pituitary cells themselves express CTLA-4, so the antibody binds the gland and fixes complement there, on top of the broad early T-cell activation ipilimumab causes (ONC-12)."),
    ('h', "**True — dasatinib is linked to pleural effusion,** an exudative, lymphocytic effusion from off-target kinase inhibition (ONC-03)."),
  ],
  mimic=[],
  traps=[
    ("“Tocilizumab and siltuximab both bind IL-6”", "Only siltuximab binds IL-6; tocilizumab blocks its receptor."),
    ("“Grade is set by the better of the two columns”", "The worse of hypotension and hypoxia sets the CRS grade."),
  ],
  decode=[
    ("Statements about CRS grading", "Check fever, the number of pressors, and whether the oxygen is positive pressure."),
    ("Statements about targets", "Match the antibody to its molecule: CD20 rituximab, CD3/CD19 blinatumomab, CTLA-4 ipilimumab, PD-1 nivolumab."),
  ],
  punch="Every statement turns on one detail from the deck — the target of each antibody, fever and positive pressure in CRS grading, receptor versus cytokine for IL-6 blockade, and lower-is-worse for the ICE score.",
)
