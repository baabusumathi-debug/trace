# SPECIAL02 top-up cards — Explain v3 ("Learn" depth), same fields and voice as special02_learn.py.
# Fields: sub, step (index into special02_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source questions (from qbank.json topups["SPECIAL02"] src): DocT GT CGT5 Q131 and Q132 (ICU palliative care: barriers, triggers); DocT GT CGT1 Q31 (macro- vs micro-allocation).
# Independent review (13 Nov 2026): decode items rewritten from the real stems in map/doct_gt_distinct_all.jsonl (CGT5 Q131, Q132; CGT1 Q31). ‘SEP-59’ is the cross-reference to card
# SEP-59 (deck SEP01E, goals of care and palliative care), not an SSC recommendation number. SSC 2021 points re-checked (goals of care early, within 72 h, weak; conditional against
# routine formal palliative consultation; best-practice statement to integrate palliative principles).
# From standard references (writer): Surviving Sepsis Campaign 2021 — discuss goals of care and prognosis with patients and families (best practice); address goals
# of care early, within 72 h (weak); suggest against routine formal palliative care consultation for all patients in favour of clinician discretion (weak). ICU palliative-care trigger
# criteria (IPAL-ICU / CAPC lists, e.g. ICU stay over 10 days, multi-organ failure, stage IV cancer, post-arrest, family conflict, tracheostomy/PEG being considered).
# Macro- vs micro-allocation: standard health-economics and ethics teaching.
T = {}

T['T_d32ab4c4'] = dict(
  sub="End-of-life care → The process → Palliative care in the ICU",
  step=4,
  intro="Step 4 was the team reaching a decision with the family. Bringing in palliative care is how many ICUs do that well, but it happens late or not at all. Two DocT GT questions ask why it is held back and when a consult should be triggered.",
  parts=[
    ('a', "**Barriers: deficient communication training (prognosis talks are a skill), unrealistic family/team expectations, prognostic uncertainty, belief that palliation = giving up.** Each one delays the conversation. Uncertainty is a frequent reason given for waiting, but prognosis is never certain, and palliative care runs alongside full treatment (EOL-01), so starting it does not mean giving up."),
    ('b', "**Triggers: ICU stay >10 days, multi-organ failure, advanced dementia/frailty, metastatic cancer, post-arrest poor neurology, family conflict.** These are the patients with a high chance of dying or of surviving with a heavy burden, and the families most likely to need help with decisions. Using fixed triggers removes the need for one doctor to ‘give up’ first."),
    ('c', "**Also whenever tracheostomy or PEG (prolonged life support) is being considered.** That is the moment the team commits to long-term support, so goals of care should be clear before it is done."),
    ('d', "**SSC: discuss goals of care within 72 h; no routine consult for every patient (SEP-59).** SEP-59 is the matching card in the sepsis deck. The Surviving Sepsis Campaign 2021 recommends discussing goals and prognosis with patients and families and suggests doing it early (within 72 hours, weak recommendation), but suggests against a routine formal palliative consult for every septic patient (conditional), because trials showed mixed effects on families; the ICU team integrates palliative principles itself and refers by trigger or judgement."),
  ],
  mimic=[
    ("Primary vs specialist palliative care", "Symptom control and goals-of-care talks by the ICU team for every patient vs a palliative-care team consult for triggered or complex cases."),
  ],
  traps=[
    ("Waiting for prognostic certainty before involving palliative care", "Uncertainty is a barrier, not a reason; the triggers act on a high risk, not on certainty."),
    ("Thinking SSC recommends a palliative consult for every septic patient", "It advises early goals-of-care discussion for all, but against a routine formal consult for all."),
  ],
  decode=[
    ("79-year-old with advanced dementia, frailty, multi-organ failure and prolonged ventilation develops septic shock; tracheostomy and PEG are being considered. Strongest trigger for early palliative consult: vasopressors, PEG and tracheostomy consideration, broad-spectrum antibiotics, fever? [DocT GT]", "PEG and tracheostomy consideration: it marks a commitment to prolonged life support; vasopressors reflect severity but many patients recover."),
    ("Metastatic cancer, septic shock, ventilated; the intensivist thinks more treatment will not help but struggles to say so at the family meeting. Barrier illustrated: lack of diagnostic resources, poor symptom-control protocols, deficient communication training, limited reimbursement? [DocT GT]", "Deficient communication training: the prognosis is understood, the skill to convey it is missing."),
  ],
  punch="Barriers are poor communication skills, unrealistic hopes, uncertainty and the idea that palliation is surrender; consult on fixed triggers or before a tracheostomy or PEG, and discuss goals of care within 72 hours, but not with a routine consult for everyone.",
)

T['T_43e8d00d'] = dict(
  sub="End-of-life care → Ethics → Justice: allocating resources",
  step=2,
  intro="Step 2 named justice as fair use of resources (EOL-03). Allocation decisions happen at two levels, and one DocT GT question asks you to tell them apart.",
  parts=[
    ('a', "**Macroallocation: system/policy decisions by government or payers on splitting a budget (e.g. capping hospital reimbursement to fund outpatient care).** It is made away from the bedside, for populations, before any patient is known."),
    ('b', "**Microallocation: bedside decisions on which patient gets a scarce resource (last ICU bed, ventilator, organ), guided by justice and triage criteria.** It is about named patients competing for one resource; triage criteria such as likely benefit keep it fair rather than first-come or by influence."),
  ],
  mimic=[
    ("Macro- vs microallocation", "Policy and budgets for a population vs choosing between identified patients for one bed, ventilator or organ."),
  ],
  traps=[
    ("Calling a hospital’s choice of who gets the last ventilator ‘macroallocation’ because a hospital made it", "It concerns identified patients and one resource, so it is microallocation; macro is budget-level policy."),
  ],
  decode=[
    ("A health minister caps hospital reimbursement to expand outpatient coverage — macroallocation, microallocation by a physician, evidence-based restriction, or equality-based prioritisation? [DocT GT]", "Macroallocation for system-level cost control: a policy decision about budgets, made for a population."),
  ],
  punch="Macroallocation is a government or payer splitting a budget; microallocation is choosing which patient gets the last bed, ventilator or organ, guided by justice and triage criteria.",
)

FLAGS = {}
