# TOX06 — Novel Cancer Therapies: Toxicity in ICU. Explain v2 ("Learn" depth), HT's November style. No mnemonics or hooks.
# Same fields as TOX01: sub, intro, parts, table (optional), mimic, traps, decode, punch, extra (optional).
# Audited 6 Nov against qpack/TOX06.md (real stems): decode from real stems, traps from low-% distractors, cuts.
L = {}
FLAGS = {}

L['ONC-01'] = dict(
  sub="Toxicology → The Agents → Class, example and target",
  intro="The newer cancer drugs do not poison every dividing cell, as classical chemotherapy does. Each is aimed at one molecule — a surface marker, a growth signal, an enzyme, or a brake on the immune system. The target tells you what the drug does to the tumour and what it does to the rest of the body.",
  parts=[
    ('a', "**Monoclonal antibodies: rituximab → CD20; bevacizumab → VEGF; cetuximab → EGFR.** Rituximab depletes normal B cells too — infusion reactions, low IgG, hepatitis B reactivation. Bevacizumab binds the VEGF ligand, which keeps endothelium healthy — hypertension, proteinuria, thrombosis. EGFR is in skin and renal tubule — acneiform rash and magnesium wasting."),
    ('b', "**Bispecific antibody: blinatumomab → CD3 and CD19.** One arm grips CD3 on a T cell, the other CD19 on a B cell, forcing the T cell to kill; mass T-cell activation produces cytokine release syndrome (ONC-04)."),
    ('c', "**Checkpoint inhibitors: ipilimumab → CTLA-4; nivolumab, pembrolizumab → PD-1.** They block the brakes on T cells (ONC-02), so T cells can also attack normal tissue."),
    ('d', "**Tyrosine kinase inhibitors: imatinib, dasatinib → the tyrosine kinase (BCR-ABL).** Oral small molecules blocking the kinase that drives the tumour; ‘off-target’ kinases explain their side-effects (ONC-03)."),
    ('e', "**Immune effector cells: CAR-T cells → a tumour antigen (CD19).** The patient’s own T cells re-engineered to recognise CD19; living cells multiply after infusion, so effect and toxicity build over days."),
  ],
  table=dict(title="Target decides toxicity", head=["Agent", "Target", "Off-tumour consequence"], rows=[["Rituximab", "CD20 (B cells)", "infusion reaction, HBV reactivation, low IgG"], ["Bevacizumab", "VEGF", "hypertension, proteinuria, thrombosis, TMA"], ["Cetuximab", "EGFR", "rash, hypomagnesaemia"], ["Blinatumomab, CAR-T", "CD19 (with CD3)", "CRS, ICANS, B-cell aplasia"], ["Ipilimumab, nivolumab", "CTLA-4, PD-1", "immune-related adverse events"]]),
  mimic=[],
  traps=[
    ("“Blinatumomab targets CD20”", "That is rituximab; blinatumomab links CD3 to CD19 (ONC-13)."),
  ],
  decode=[
    ("Bispecific T-cell engager in B-ALL [pattern]", "Blinatumomab (CD3/CD19)."),
  ],
  punch="Each novel agent is aimed at one molecule, and its ICU toxicity follows from where else that molecule works — VEGF in vessels, EGFR in skin and tubule, and T-cell brakes everywhere.",
)

L['ONC-02'] = dict(
  sub="Toxicology → The Agents → How checkpoint inhibitors and CAR-T work",
  intro="T cells carry built-in brakes — checkpoints — that stop them attacking the body’s own tissue, and tumours exploit these brakes to hide. Checkpoint inhibitors release the brakes; CAR-T builds a T cell that cannot miss its target. Both strengthen the immune system, so their toxicities are inflammation and autoimmunity.",
  parts=[
    ('a', "**PD-1 on T cells binds PD-L1 on the cancer cell, switching the T cell off.** A late brake in the tissues; tumours over-express PD-L1 to protect themselves."),
    ('b', "**Anti-PD-1 drugs block that binding, so the T cell kills the tumour.** The same brake protects normal organs, so they can become inflamed too."),
    ('c', "**CTLA-4 competes with CD28 for CD80/86 on antigen-presenting cells and inhibits T-cell activation; blocking it restores activation.** CTLA-4 binds CD80/86 more tightly than CD28 and removes co-stimulation at priming in the lymph node. Blocking this early brake unleashes many new T-cell clones — why anti-CTLA-4 causes more frequent and severe immune-related adverse events."),
    ('d', "**The patient’s T cells are collected, given a chimeric antigen receptor gene by a viral vector, expanded and re-infused.** The receptor joins an anti-CD19 fragment to T-cell signalling and co-stimulatory domains; lymphodepleting chemotherapy precedes re-infusion."),
  ],
  table=dict(title="Two brakes, two places", head=["", "CTLA-4", "PD-1"], rows=[["Where it acts", "lymph node, at priming", "tissue and tumour, late"], ["Partner", "CD80/86 (outcompetes CD28)", "PD-L1, PD-L2"], ["Drug", "ipilimumab", "nivolumab, pembrolizumab"], ["Toxicity", "more frequent, more severe", "less frequent"]]),
  mimic=[
    ("Checkpoint inhibitor vs CAR-T toxicity", "Checkpoint toxicity is organ-specific autoimmunity weeks to months later; CAR-T toxicity is a cytokine storm and neurotoxicity in the first days to weeks."),
  ],
  traps=[
    ("“CTLA-4 is a co-stimulatory receptor like CD28”", "It competes with CD28 for CD80/86 and switches activation off."),
    ("“PD-1 is on the tumour cell”", "PD-1 is on the T cell; PD-L1 is on the tumour."),
  ],
  decode=[
    ("Which molecule competes with CD28 for B7 (CD80/86)? [pattern]", "CTLA-4."),
  ],
  punch="Checkpoint inhibitors take the brakes off T cells and CAR-T builds T cells that cannot miss; either way the toxicity is the immune system itself — inflammatory and autoimmune, not toxic in the classical sense.",
)

L['ONC-03'] = dict(
  sub="Toxicology → The Agents → Signature toxicity by class",
  intro="Each class of novel agent fails in its own way, following its mechanism. Drugs that free the immune system cause autoimmunity; drugs that activate huge numbers of T cells cause a cytokine storm; antibodies, being foreign proteins, cause infusion and allergic reactions; kinase inhibitors hit kinases they were not designed for.",
  parts=[
    ('a', "**Checkpoint inhibitors: immune-related adverse events — pneumonitis, colitis, hepatitis, myocarditis, endocrinopathy.** Released T cells lose tolerance to normal tissue. Myocarditis is uncommon but most often fatal. When a patient on a checkpoint inhibitor develops adrenal insufficiency — fatigue, hypotension, nausea — the usual mechanism is drug-induced hypophysitis (classically ipilimumab) with low ACTH: secondary adrenal insufficiency, not destruction of the adrenal gland itself (ONC-12)."),
    ('b', "**CAR-T cells: cytokine release syndrome; ICANS.** Activated CAR-T cells recruit macrophages that pour out IL-6 and IL-1 (ONC-04); the same activation opens the blood–brain barrier (ONC-07)."),
    ('c', "**Monoclonal antibodies: infusion reactions, cytokine release, Kounis syndrome, PRES.** A foreign protein can trigger mast-cell release — in the coronaries this is Kounis syndrome (ONC-11). Anti-VEGF antibodies raise blood pressure and injure endothelium, the setting for PRES."),
    ('d', "**Tyrosine kinase inhibitors: QT prolongation, pleural effusion (dasatinib), thrombosis, PRES, tumour lysis.** Several TKIs block the hERG channel; dasatinib causes an exudative, lymphocytic pleural effusion from off-target kinase inhibition; rapid killing of a sensitive leukaemia causes tumour lysis."),
  ],
  table=dict(title="Mechanism to toxicity", head=["Class", "Mechanism of harm", "Signature"], rows=[["Checkpoint inhibitor", "loss of self-tolerance", "irAEs (colitis, pneumonitis, hypophysitis…)"], ["CAR-T, bispecifics", "mass T-cell activation", "CRS, ICANS"], ["Monoclonal antibody", "foreign protein, mast cells", "infusion reaction, Kounis"], ["TKI", "off-target kinases, hERG", "QT, effusion (dasatinib)"]]),
  mimic=[
    ("Secondary vs primary adrenal insufficiency on a checkpoint inhibitor", "Hypophysitis: low ACTH, often low TSH and gonadotrophins, headache, no hyperkalaemia. Primary adrenalitis (rare): high ACTH and hyperkalaemia."),
  ],
  traps=[
    ("“Checkpoint adrenal insufficiency is direct T-cell destruction of the adrenal cortex” (or ACTH-receptor antibodies, aldosterone synthase inhibition)", "The commonest mechanism is hypophysitis causing secondary adrenal insufficiency; primary adrenalitis is rare. Only 57–65% chose it. Give hydrocortisone first, before thyroxine."),
    ("“Cytokine release syndrome is a checkpoint-inhibitor toxicity”", "It is the signature of CAR-T cells and bispecifics; checkpoint inhibitors cause organ-specific irAEs."),
  ],
  decode=[
    ("Melanoma on checkpoint inhibitor: fatigue, hypotension, nausea — mechanism of adrenal insufficiency [DocT GT ×2]", "Drug-induced hypophysitis causing secondary AI."),
    ("Pleural effusion in a CML patient on a TKI [pattern]", "Dasatinib."),
  ],
  punch="Read the toxicity from the mechanism: freed T cells cause autoimmunity — at the pituitary, giving secondary adrenal failure — mass T-cell activation causes a cytokine storm, foreign antibodies cause allergy, and kinase inhibitors hit the wrong kinases.",
)

L['ONC-04'] = dict(
  sub="Toxicology → Cytokine Release Syndrome → Causes, picture and labs",
  intro="When CAR-T cells or a bispecific antibody meet their target, thousands of T cells are activated at once. They release interferon-γ and other cytokines that switch on monocytes and macrophages, and these produce most of the IL-6. IL-6 activates the endothelium everywhere, so capillaries leak — and within days of infusion the patient looks exactly like septic shock.",
  parts=[
    ('a', "**CAR-T cells, bispecific antibodies (blinatumomab), muromonab (OKT3).** All activate T cells en masse — through the engineered receptor, by linking CD3 to CD19, or by binding CD3 directly."),
    ('b', "**80–85% after CAR-T; about 20% need vasopressors.** Severity rises with tumour burden and cell dose."),
    ('c', "**IL-6, IL-8, IL-10; von Willebrand factor and angiopoietin-2 (endothelial activation).** IL-6 is the cytokine most strongly tied to the symptoms and the target of treatment; IFN-γ starts the cascade and IL-1 and TNF-α take part, but IL-6 is the answer. IL-6 bound to its soluble receptor signals in endothelium through gp130 (trans-signalling), releasing angiopoietin-2 and von Willebrand factor — the capillary leak and coagulopathy."),
    ('d', "**Fever first; then hypotension, hypoxaemia (non-cardiogenic oedema), arrhythmia, oliguria, confusion.** Cytokines reset the hypothalamus first; leaky capillaries then cause vasodilatory hypotension and alveolar fluid."),
    ('e', "**Raised CRP and procalcitonin; hypokalaemia, raised urea; altered counts and coagulation. Ferritin also rises.** CRP and ferritin are made in response to IL-6, so they track the storm; procalcitonin rises too, so it does not separate CRS from sepsis."),
  ],
  mimic=[
    ("CRS vs sepsis", "Identical bedside picture in a neutropenic patient; timing after infusion and negative cultures point to CRS, but cultures and empirical antibiotics are always started."),
  ],
  traps=[
    ("“Culture-negative shock after CD19 CAR-T: give rituximab, eculizumab or blinatumomab”", "The cytokine-targeted treatment is tocilizumab (anti-IL-6 receptor). Rituximab is anti-CD20, eculizumab anti-complement C5, blinatumomab itself causes CRS."),
    ("“A raised procalcitonin proves infection rather than CRS”", "Procalcitonin can rise in CRS; treat both."),
  ],
  decode=[
    ("Cytokine most strongly associated with CRS after CAR-T [DocT GT]", "IL-6."),
    ("Day 3 after CD19 CAR-T: fever, norepinephrine, hypoxaemia, cultures negative — cytokine-targeted therapy [DocT GT]", "Tocilizumab."),
  ],
  punch="Mass T-cell activation drives macrophage IL-6, IL-6 opens the capillaries, and the patient looks septic — so CRS is treated with IL-6 blockade, but infection is always covered too.",
)

L['ONC-05'] = dict(
  sub="Toxicology → Cytokine Release Syndrome → ASTCT grading",
  intro="ASTCT grading of cytokine release syndrome rests on three bedside things: fever, blood pressure and oxygen. Fever establishes that it is CRS; the grade is set by how much support the circulation and lungs need, whichever is worse.",
  parts=[
    ('a', "**Grade 1: fever, no hypotension, no hypoxia.** The thermostat is reset but the capillaries are not yet leaking enough to matter."),
    ('b', "**Grade 2: hypotension not needing a vasopressor; hypoxia needing low-flow nasal oxygen.** Pressure responds to fluid; up to about 6 L/min by nasal cannula corrects saturation."),
    ('c', "**Grade 3: one vasopressor (with or without vasopressin); high-flow oxygen, face mask or non-rebreather.** Vasopressin is not counted as a second agent, so noradrenaline plus vasopressin is still grade 3."),
    ('d', "**Grade 4: multiple vasopressors (not counting vasopressin); positive pressure (CPAP, BiPAP, ventilation).** Positive pressure, not oxygen flow, defines grade 4 on the hypoxia side."),
  ],
  table=dict(title="Fever plus the worse of two columns", head=["Grade", "Circulation", "Oxygen"], rows=[["1", "normal", "none"], ["2", "fluid-responsive, no pressor", "low-flow nasal"], ["3", "**one** pressor ± vasopressin", "**high-flow**, mask, non-rebreather"], ["4", "**multiple** pressors", "**positive pressure**"]]),
  mimic=[],
  traps=[
    ("“CRS can be graded without fever”", "Fever ≥38 °C is required to diagnose it; once antipyretics or tocilizumab mask it, the grade follows pressure and oxygen."),
    ("“Noradrenaline plus vasopressin is grade 4”", "One catecholamine with or without vasopressin is grade 3."),
  ],
  decode=[
    ("Fever, hypotension after 2 L saline, no pressor, SpO₂ 95% on air [pattern]", "Grade 2 CRS."),
    ("Fever, on BiPAP [pattern]", "Grade 4 CRS."),
  ],
  punch="Fever makes it CRS, and the grade is the support the patient needs — no pressor or low-flow oxygen is 2, one pressor or high-flow is 3, several pressors or positive pressure is 4, whichever column is worse.",
)

L['ONC-06'] = dict(
  sub="Toxicology → Cytokine Release Syndrome → Treatment by grade",
  intro="CRS treatment escalates with the grade. Mild disease is supported while infection is excluded. Once the circulation or lungs are involved, IL-6 — the central mediator — is blocked; if that is not enough, steroids are added. Steroids may blunt the CAR-T cells fighting the cancer, so they wait for the more severe or refractory grades.",
  parts=[
    ('a', "**Grade 1: supportive — antipyretics, fluids, cultures, empirical antibiotics.** The patient is often neutropenic, so fever is treated as possible sepsis."),
    ('b', "**Grade 2: tocilizumab (maximum 3 doses); consider ICU.** Hypotension persisting after fluid boluses, without a pressor and with normal oxygen, is grade 2 — the next step is tocilizumab, not steroids, ventilation or adrenaline for ‘anaphylaxis’. Tocilizumab 8 mg/kg IV (maximum 800 mg) usually breaks fever and hypotension within hours; repeat after 8 hours if needed, up to 3 doses in 24 hours. Dexamethasone 10 mg is added if hypotension persists after one or two doses."),
    ('c', "**Grade 3: ICU; tocilizumab or siltuximab plus dexamethasone 10–20 mg 6-hourly.** A patient on a vasopressor or high-flow oxygen still gets tocilizumab as the initial cytokine-targeted drug, with dexamethasone alongside; dexamethasone also crosses into the brain, useful because ICANS often accompanies severe CRS."),
    ('d', "**Grade 4: anti-IL-6 plus methylprednisolone 1 g pulse; anakinra if refractory.** Survival now outweighs any concern for the anti-tumour effect. Anakinra blocks the IL-1 receptor, a pathway IL-6 blockade does not reach."),
  ],
  table=dict(title="Which drug blocks what", head=["Drug", "Binds", "Result"], rows=[["Tocilizumab", "**IL-6 receptor** (membrane and soluble)", "blocks signalling; serum IL-6 rises"], ["Siltuximab", "**IL-6** itself", "neutralises the cytokine"], ["Anakinra", "IL-1 receptor", "blocks the IL-1 pathway"], ["Steroids", "—", "broad suppression; may blunt CAR-T"]]),
  mimic=[
    ("Tocilizumab vs siltuximab", "Tocilizumab blocks the receptor (so IL-6 accumulates in the blood); siltuximab binds and removes the cytokine itself."),
  ],
  traps=[
    ("“Tocilizumab neutralises circulating IL-6” or “inhibits gp130 directly”", "It is a humanised antibody to the IL-6 receptor (membrane and soluble); siltuximab binds IL-6, gp130 is downstream and untouched, anakinra blocks IL-1. Only 59% chose ‘blocks IL-6 receptor’."),
    ("“Hypotension after immune effector cells despite fluids: high-dose methylprednisolone or adrenaline for anaphylaxis”", "This is grade 2 CRS — tocilizumab first; steroids are for refractory or higher grades."),
    ("“Fever settled after tocilizumab, so the CRS is over”", "Tocilizumab removes fever quickly; follow pressure, oxygen and watch for ICANS."),
  ],
  decode=[
    ("12 h after immune effector cells: fever, BP 88/50 after 2 L saline, SpO₂ 95% on air — next step [DocT GT]", "Tocilizumab."),
    ("CD19 CAR-T, day 3, on norepinephrine, hypoxaemic, cultures negative — initial cytokine therapy [DocT GT]", "Tocilizumab."),
    ("Mechanism of tocilizumab in CRS [DocT GT]", "Blocks the IL-6 receptor."),
  ],
  punch="CRS treatment climbs with the grade: support for 1, IL-6 blockade for 2, add dexamethasone for 3, pulse methylprednisolone and IL-1 blockade for 4 — tocilizumab blocks the receptor, siltuximab the cytokine.",
  extra=[dict(q="Why does serum IL-6 rise after tocilizumab?", a="With the **IL-6 receptor** blocked, IL-6 is no longer taken up and cleared through it, so the blood level **rises** even as signalling stops — the basis of tocilizumab’s failure in ICANS (ONC-07).")],
)
FLAGS['ONC-06'] = "Tocilizumab ‘maximum 3 doses’: current guidance (NCCN, ASCO, product labels) is a maximum of 3 doses in 24 hours and 4 doses in total. The WATCH’s ‘older NCI triggers’ (LVEF <40%, creatinine >2.5 × baseline, noradrenaline >2 µg/min for 48 h) are correctly quoted from the NCI criteria (Kroschinsky 2017, Crit Care, Table 3) but are pre-ASTCT and no longer used to decide tocilizumab."

L['ONC-07'] = dict(
  sub="Toxicology → Neurotoxicity (ICANS) → Definition, picture and treatment",
  intro="A few days after CAR-T infusion, often as the cytokine storm peaks or just after it, some patients develop a brain disorder of their own. Cytokines and activated endothelium make the blood–brain barrier leak, and inflammatory mediators reach the cerebrospinal fluid. Language and handwriting fail first.",
  parts=[
    ('a', "**Immune effector cell-associated neurotoxicity syndrome.** The neurotoxicity of any therapy that works by activating immune effector cells."),
    ('b', "**CAR-T cells and bispecific antibodies.** Both produce the cytokine and endothelial injury behind CRS."),
    ('c', "**Tremor, dysgraphia, aphasia, cerebellar signs, encephalopathy, seizures.** A change in handwriting or word-finding may be the first sign (ONC-08)."),
    ('d', "**Status epilepticus, coma, paresis, cerebral oedema.** Diffuse cerebral oedema can be fulminant and fatal."),
    ('e', "**Corticosteroids.** Dexamethasone crosses the blood–brain barrier and suppresses the inflammation inside it. Tocilizumab does not cross: it blocks peripheral IL-6 receptors, so serum IL-6 rises, more IL-6 reaches the CNS, and there the receptors are unblocked — so neurotoxicity can worsen after tocilizumab."),
  ],
  mimic=[
    ("ICANS vs CRS", "CRS is systemic (fever, hypotension, hypoxia) and responds to tocilizumab; ICANS is neurological and responds to steroids. ICANS can occur without CRS."),
  ],
  traps=[
    ("“Tocilizumab crosses the blood–brain barrier” / “blocks IL-6 centrally” / “IL-6 is trapped peripherally”", "The paradox is the reverse: IL-6 rises and increases in the CNS, where tocilizumab cannot follow. 68% got it."),
    ("“Give tocilizumab for isolated ICANS”", "Use dexamethasone; tocilizumab may worsen it."),
  ],
  decode=[
    ("48 h after CAR-T: fever, hypotension, confusion; tocilizumab given, neurotoxicity worsens — mechanism [DocT GT]", "IL-6 increased in the CNS."),
    ("ICANS without CRS — drug of choice? [pattern]", "Dexamethasone."),
  ],
  punch="ICANS is the cytokine storm reaching the brain through a leaky barrier: writing and language fail first, and because tocilizumab cannot follow IL-6 across the barrier — and raises it — steroids are the treatment.",
)

L['ONC-08'] = dict(
  sub="Toxicology → Neurotoxicity (ICANS) → The ICE score",
  intro="Because writing and language fail early in ICANS, a ten-point bedside screen — the ICE score — tests exactly those functions, several times a day while the patient is at risk. It is one domain of the ICANS grade; the others are consciousness, seizures, motor weakness and cerebral oedema (ONC-09).",
  parts=[
    ('a', "**Orientation 4 (year, month, city, hospital); naming three objects 3; following a simple command 1; writing a standard sentence 1; counting back from 100 by tens 1.** Orientation tests global encephalopathy, naming expressive aphasia, writing dysgraphia, counting attention. 10 is normal."),
    ('b', "**Grade 1: 7–9; grade 2: 3–6; grade 3: 0–2; grade 4: 0, unarousable.** Lower is worse. A score of 0 is grade 4 only when the patient cannot be roused to try."),
  ],
  table=dict(title="ICE score to ICANS grade", head=["ICE score", "Grade"], rows=[["10", "no ICANS"], ["7–9", "1"], ["3–6", "2"], ["0–2", "3"], ["0, unarousable", "4"]]),
  mimic=[],
  traps=[
    ("“A higher ICE score means worse neurotoxicity”", "Lower is worse; 10 is normal (ONC-13)."),
    ("“The ICE score alone gives the ICANS grade”", "The grade is the worst of five domains."),
  ],
  decode=[
    ("ICE score 5 after CAR-T [pattern]", "Grade 2 ICANS (if no worse domain)."),
  ],
  punch="The ICE score is a ten-point test of the functions ICANS breaks first — orientation, naming, writing and attention — so a lower score means worse neurotoxicity: 7–9 is grade 1, 3–6 grade 2, 0–2 grade 3.",
)

L['ONC-09'] = dict(
  sub="Toxicology → Neurotoxicity (ICANS) → Grades and treatment",
  intro="The ICE score covers only cognition, so the ASTCT grade also takes consciousness, seizures, motor weakness and raised intracranial pressure; the worst sets the grade. Treatment escalates with it: observation, then steroids, then ICU care for seizures and oedema.",
  parts=[
    ('a', "**Grade 1: wakes spontaneously — monitor; imaging, EEG.** EEG looks for non-convulsive seizures; many centres give levetiracetam prophylaxis."),
    ('b', "**Grade 2: wakes to voice — consider steroids; lumbar puncture.** Dexamethasone 10 mg IV, repeated if no improvement; LP when safe excludes infection."),
    ('c', "**Grade 3: wakes to touch only; any seizure that resolves; focal oedema on imaging — ICU; dexamethasone 10 mg 6-hourly; antiepileptics.** Needing touch to wake puts the airway at risk, and any seizure signals cortical irritation."),
    ('d', "**Grade 4: unarousable; prolonged seizure (>5 min); hemiparesis; diffuse oedema, papilloedema — as for grade 3, plus anakinra or cyclophosphamide (experimental); treat raised ICP.** Raised ICP gets the usual measures, and ASCO/NCCN escalate to methylprednisolone 1 g IV daily for 3 days."),
  ],
  table=dict(title="Worst domain sets the grade", head=["Domain", "Grade 3", "Grade 4"], rows=[["Consciousness", "wakes to touch", "unarousable"], ["Seizure", "any clinical seizure that resolves", "prolonged >5 min, or repeated without recovery"], ["Motor", "—", "hemiparesis, paraparesis"], ["Imaging / ICP", "focal oedema", "diffuse oedema, papilloedema"]]),
  mimic=[],
  traps=[
    ("“A single brief seizure is grade 2”", "Any clinical seizure that resolves is grade 3."),
    ("“Focal oedema on imaging is grade 4”", "Focal is grade 3; diffuse is grade 4."),
  ],
  decode=[
    ("ICANS, rousable only to touch [pattern]", "Grade 3 — ICU, dexamethasone 10 mg 6-hourly."),
  ],
  punch="ICANS is graded by its worst sign — voice is 2, touch or any seizure or focal oedema is 3, coma, status, hemiparesis or diffuse oedema is 4 — and steroids, ICU care and ICP control escalate in step.",
)
FLAGS['ONC-09'] = "Grade 4 treatment ‘as 3’ implies dexamethasone; standard guidance (ASCO/NCCN) for grade 4 ICANS is high-dose methylprednisolone 1 g/day (usually 3 days) — card omits it."

L['ONC-10'] = dict(
  sub="Toxicology → Organ Toxicities → General management of immune-related adverse events",
  intro="An immune-related adverse event is the immune system attacking a normal organ after its brakes have been removed, so treatment follows the logic of autoimmune disease: stop feeding the attack, exclude alternatives, suppress, and come off slowly.",
  parts=[
    ('a', "**Hold the drug; exclude infection and pre-existing autoimmune disease.** Infection must be excluded first because the treatment is immunosuppression."),
    ('b', "**Prednisolone 1–2 mg/kg/day or equivalent.** For grade 3–4 events; grade 2 usually gets 0.5–1 mg/kg."),
    ('c', "**If no response in 5–7 days, add another immunosuppressant: infliximab for colitis; mycophenolate for hepatitis.** Current ASCO/ESMO guidance calls an event steroid-refractory after about 48–72 hours. Infliximab is avoided in hepatitis because it is itself hepatotoxic."),
    ('d', "**Taper slowly, over 4 weeks.** Activated T cells persist, so a fast taper flares; prolonged steroids need Pneumocystis prophylaxis."),
    ('e', "**After a grade 3 or 4 event, stop the checkpoint inhibitor permanently.** Grade 4 events and any-grade myocarditis mean permanent discontinuation. Endocrine disease is the exception: the gland is replaced with hormone and the drug can usually resume."),
  ],
  mimic=[],
  traps=[
    ("“Infliximab for steroid-refractory checkpoint hepatitis”", "Infliximab is hepatotoxic; mycophenolate is used."),
    ("“Endocrine irAEs need high-dose steroids and permanent discontinuation”", "Hormone replacement treats them; the drug can usually be resumed."),
  ],
  decode=[
    ("Grade 3 colitis on ipilimumab, no response to IV steroids [pattern]", "Infliximab (mycophenolate if it were hepatitis)."),
  ],
  punch="Treat an irAE like an autoimmune disease you caused: hold the drug, rule out infection, give high-dose steroids, add infliximab or mycophenolate if they fail, taper slowly — and do not rechallenge after a severe event unless the gland can just be replaced.",
)
FLAGS['ONC-10'] = "c: ‘no response in 5–7 days’ — current ASCO/ESMO guidance defines steroid-refractory as no improvement after about 48–72 h of high-dose steroids. e: permanent discontinuation is the rule for grade 4 (and for any-grade myocarditis); after some grade 3 events (e.g. anti-PD-1 colitis) rechallenge can be considered after recovery to grade 1 or less."

L['ONC-11'] = dict(
  sub="Toxicology → Organ Toxicities → Neurological and cardiac toxicities",
  intro="Neurological and cardiac complications of novel agents are rare but dangerous. Some are autoimmune (checkpoint inhibitors attacking nerve, muscle, meninges or myocardium); some are vascular (drugs raising blood pressure and damaging endothelium); some are allergic (antibodies releasing mast-cell mediators into the coronaries). The mechanism dictates the treatment.",
  parts=[
    ('a', "**Guillain–Barré, myasthenia: anti-PD-1/PD-L1, sunitinib — IVIG, plasma exchange, steroids.** Checkpoint inhibitors are the main cause. Because the attack is T-cell driven, the checkpoint form gets steroids as well as IVIG or plasma exchange. Myasthenia can overlap with myositis and myocarditis — check troponin and CK."),
    ('b', "**PRES: monoclonals, TKIs — stop the drug, control BP.** When pressure exceeds cerebral autoregulation and the endothelium is injured, fluid leaks into the posterior white matter: seizures, headache, cortical blindness, hypertension. The same syndrome follows calcineurin inhibitors (ciclosporin, tacrolimus) after transplant, and the management is identical — withdraw or reduce the trigger and lower the pressure; it usually reverses."),
    ('c', "**Aseptic meningitis: monoclonals, checkpoint inhibitors — steroids, IVIG, rituximab.** Lymphocytic CSF; exclude infection before steroids."),
    ('d', "**Myocarditis: checkpoint inhibitors — high-dose steroids, IVIG.** T-cell infiltration in the first weeks, with conduction block, arrhythmia and heart failure — the most often fatal irAE. Pulse methylprednisolone early, and the drug is stopped permanently."),
    ('e', "**Kounis syndrome: monoclonal antibodies — treat as ACS plus anaphylaxis; morphine with caution.** Mast-cell mediators cause coronary spasm or plaque rupture; morphine releases histamine and can deepen the reaction."),
    ('f', "**Acute coronary syndrome: bevacizumab, trastuzumab — treat as ACS.** Bevacizumab damages endothelium and promotes arterial thrombosis. Trastuzumab’s signature is reversible LV systolic dysfunction rather than coronary occlusion; 5-fluorouracil causes coronary vasospasm."),
  ],
  table=dict(title="Mechanism to treatment", head=["Syndrome", "Mechanism", "Key treatment"], rows=[["GBS, myasthenia (ICI)", "autoimmune, T-cell", "IVIG/PLEX **plus steroids**"], ["PRES (mAbs, TKIs, CNIs)", "hypertension, endothelial injury", "stop or reduce drug, lower BP"], ["Myocarditis (ICI)", "T-cell infiltration", "pulse steroids, stop for good"], ["Kounis", "mast-cell mediators in coronaries", "ACS + anaphylaxis care"], ["Bevacizumab", "arterial thrombosis", "as ACS; stop drug"]]),
  mimic=[
    ("PRES vs its lookalikes after transplant", "Posterior vasogenic oedema with hypertension on a CNI is PRES; it is not a posterior fossa tumour (no decompression), HSV encephalitis (temporal, febrile — aciclovir) or venous sinus thrombosis (anticoagulation)."),
    ("Checkpoint myocarditis vs ACS", "Both raise troponin; myocarditis comes weeks after starting a checkpoint inhibitor, often with conduction block and myositis, and the coronaries are normal."),
  ],
  traps=[
    ("“Seizures, cortical blindness and posterior oedema on ciclosporin: neurosurgery, aciclovir or anticoagulation”", "Withdraw or reduce the calcineurin inhibitor and control BP aggressively."),
    ("“Steroids are not used in Guillain–Barré”", "True for classical GBS, but checkpoint-related GBS gets steroids too."),
    ("“Checkpoint myocarditis is mild and self-limiting”", "It is the most often fatal irAE; pulse steroids early, stop the drug permanently."),
  ],
  decode=[
    ("HSCT recipient on ciclosporin: seizures, hypertension, cortical blindness, posterior white-matter oedema — immediate step [DocT GT]", "Withdraw or reduce the calcineurin inhibitor; aggressive BP control."),
    ("Ptosis, myalgia and raised troponin 3 weeks after nivolumab [pattern]", "Myasthenia–myositis–myocarditis overlap — high-dose steroids."),
    ("Chest pain with urticaria during a rituximab infusion [pattern]", "Kounis syndrome."),
  ],
  punch="Read each syndrome by its mechanism: autoimmune ones need steroids even when classical teaching says otherwise, vascular ones — PRES from any trigger — need the drug stopped and the pressure lowered, and allergic coronary events need ACS and anaphylaxis care together.",
)
FLAGS['ONC-11'] = "ACS row lists trastuzumab: trastuzumab’s signature cardiotoxicity is (usually reversible) LV systolic dysfunction / heart failure, not ACS; the classic ACS-causing cancer drugs are bevacizumab (arterial thrombosis) and fluoropyrimidines (5-FU, capecitabine — vasospasm). GBS/myasthenia row lists sunitinib: supported only by case reports. Myocarditis row omits the key step — permanent discontinuation of the checkpoint inhibitor at any grade, with methylprednisolone 500–1000 mg/day."

L['ONC-12'] = dict(
  sub="Toxicology → Organ Toxicities → Lung, kidney, endocrine and liver",
  intro="Any organ can be injured by these drugs, and the ICU question is always: drug, cancer, or infection in an immunosuppressed patient? The answer decides whether to give steroids — which help immune toxicity but harm infection.",
  parts=[
    ('a', "**Pneumonitis: separate infection (Pneumocystis, CMV) from drug (anti-PD-1, rituximab, dasatinib) by CT and bronchoalveolar lavage; then steroids.** Both give ground-glass change; steroids would worsen the infections, so lavage comes first."),
    ('b', "**Renal: checkpoint inhibitors — tubulointerstitial nephritis, median onset 3 months; anti-VEGF — thrombotic microangiopathy; rituximab, TKIs — tumour lysis.** T cells infiltrate the interstitium (PPIs and NSAIDs are co-triggers); VEGF loss injures the glomerular endothelium; rapid killing releases uric acid, phosphate and potassium."),
    ('c', "**Hypophysitis: anti-CTLA-4 (ipilimumab) — headache, visual disturbance, pituitary failure; MRI and hormone levels; replace hormones.** ACTH deficiency causes secondary adrenal insufficiency — the commonest mechanism of adrenal failure on a checkpoint inhibitor. Give hydrocortisone before thyroxine, because thyroxine speeds cortisol metabolism and can precipitate crisis. Aldosterone is preserved, so there is no hyperkalaemia; replacement is usually lifelong."),
    ('d', "**Thyroid: hypo- or hyperthyroidism in 1–10%.** Thyroiditis often passes through a transient thyrotoxic phase to permanent hypothyroidism; more typical of anti-PD-1."),
    ('e', "**Hepatitis: 5–10%; from transaminitis to fulminant failure; steroids.** Exclude viral hepatitis and metastases; refractory cases get mycophenolate, not infliximab (ONC-10)."),
  ],
  mimic=[
    ("Hypophysitis vs primary adrenalitis", "Hypophysitis: low ACTH, other pituitary hormones low, no hyperkalaemia. Primary adrenal failure (rare with checkpoint inhibitors): high ACTH, hyperkalaemia."),
  ],
  traps=[
    ("“In hypophysitis replace thyroxine first”", "Hydrocortisone first, or thyroxine may precipitate adrenal crisis."),
    ("“Start steroids for pneumonitis straight away”", "Exclude Pneumocystis and CMV with BAL first."),
  ],
  decode=[
    ("Headache, fatigue, low sodium, low ACTH and TSH on ipilimumab [pattern]", "Hypophysitis — hydrocortisone first, then MRI."),
    ("Rising creatinine with sterile pyuria 3 months into pembrolizumab [pattern]", "Tubulointerstitial nephritis."),
  ],
  punch="In every organ the first step is to separate drug from infection and cancer, and the treatment follows the mechanism: steroids for immune injury, hormone replacement for a destroyed gland — cortisol before thyroxine — and stopping the drug for vascular injury.",
)

L['ONC-13'] = dict(
  sub="Toxicology → Organ Toxicities → True or false",
  intro="This card checks the deck’s key distinctions. Each statement turns on one detail met earlier.",
  parts=[
    ('a', "**False — blinatumomab targets CD3 and CD19.** CD20 is rituximab’s target (ONC-01)."),
    ('b', "**True — ipilimumab blocks CTLA-4,** the early brake that competes with CD28 for CD80/86 (ONC-02)."),
    ('c', "**False — fever is required.** Fever ≥38 °C makes it CRS; the grade then comes from blood pressure and oxygen (ONC-05)."),
    ('d', "**False — positive-pressure ventilation is grade 4.** Grade 3 is high-flow oxygen, face mask or non-rebreather (ONC-05)."),
    ('e', "**True — tocilizumab blocks the IL-6 receptor;** siltuximab binds IL-6 itself (ONC-06)."),
    ('f', "**False — a lower ICE score is worse.** It counts tasks done correctly out of 10 (ONC-08)."),
    ('g', "**True — hypophysitis is typical of anti-CTLA-4 therapy.** Pituitary cells express CTLA-4, so the antibody binds the gland there (ONC-12)."),
    ('h', "**True — dasatinib is linked to pleural effusion,** exudative and lymphocytic, from off-target kinase inhibition (ONC-03)."),
  ],
  mimic=[],
  traps=[
    ("“Tocilizumab and siltuximab both bind IL-6”", "Only siltuximab binds IL-6; tocilizumab blocks its receptor."),
  ],
  decode=[
    ("True/false on CRS grading or targets [pattern]", "Check fever, number of pressors, positive pressure; match antibody to molecule."),
  ],
  punch="Every statement turns on one detail from the deck — the target of each antibody, fever and positive pressure in CRS grading, receptor versus cytokine for IL-6 blockade, and lower-is-worse for the ICE score.",
)
