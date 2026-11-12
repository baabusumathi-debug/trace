# SPECIAL02 — Explain v3 ("Learn" depth): end-of-life care in the ICU — the terms (withholding, withdrawal, DNAR, palliative and end-of-life care), the ways of ending life compared,
# the four principles, double effect, recognising futility, the ISCCM steps, communication, symptom control, a good death and its barriers in India, the case law, the 2023 board process, true/false.
# No mnemonics or hooks. Driven by the real questions in qpack/SPECIAL02.md (4 question links: EOL-03 two DocT GT stems, EOL-06 two DocT GT stems; every other card has none).
# EOL-03 and EOL-06 get the fuller treatment; the other ten cards get short explanations with [pattern] decode items.
# No `fix` entries exist for SPECIAL02 in trace/test/data/qbank.json; the `lines` there (EOL-03 autonomy, EOL-06 stop tube feeds at withdrawal) are used (checked 13 Nov 2026).
# Checked online on 13 Nov 2026:
#  - Aruna Shanbaug v Union of India, 7 March 2011, two-judge bench (Katju, Gyan Sudha Misra): active euthanasia illegal; withdrawal of life support (passive euthanasia) permissible with
#    High Court approval under Article 226, the court appointing a committee of three doctors; can be initiated by parents, spouse, close relatives or a ‘next friend’.
#  - Common Cause v Union of India, 9 March 2018, five-judge Constitution Bench (Dipak Misra CJI): right to die with dignity is part of Article 21; a capable person may refuse life-sustaining
#    treatment; advance medical directives recognised; treatment may be withheld or withdrawn from those without capacity even without a directive; palliative care continues.
#  - Supreme Court order of 24 January 2023 (Common Cause, 2023 SCC OnLine SC 99, five-judge bench, K.M. Joseph J; on an application by ISCCM): directive signed before two witnesses and
#    attested by a notary or gazetted officer (no longer countersigned by the JMFC); Primary Board = treating physician + at least two subject experts with ≥5 years, opinion preferably within
#    48 h; Secondary Board constituted by the hospital = one registered practitioner nominated by the district CMO + at least two experts with ≥5 years, none from the primary board, preferably
#    within 48 h; hospital informs the JMFC (the magistrate’s visit and authorisation deleted); refusal → writ to the High Court under Article 226, Division Bench, may appoint three doctors
#    (20 years’ standing). 2018 version: head of department + 3 experts of 20 years; Collector-constituted board chaired by the CDMO; JMFC visit and authorisation.
#  - MoHFW ‘Guidelines for Withdrawal of Life Support in Terminally Ill Patients’ (draft, released 30 Sept 2024): conditions listed are brainstem death under THOA, advanced disease unlikely to
#    benefit from aggressive treatment, documented informed refusal by patient or surrogate, and compliance with the Supreme Court procedure (the text does not make clear whether all must apply);
#    terminal illness includes severe traumatic brain injury with no recovery after ≥72 h; PMB members may be from the treating team; CMO nominee may be from the same hospital; the JMFC form is
#    notification only, not approval; hospitals to have clinical ethics committees.
#  - ISCCM guidelines 2005, revised 2012; joint ISCCM–IAPC ‘End-of-life care policy: an integrated care plan for the dying’ (Myatra et al., IJCCM 2014;18:615–35); updated joint ISCCM–IAPC
#    position statement (Mani et al., IJCCM 2024;28(3):200–250).
#  - ICMR 2018 definitions (withholding, withdrawal, DNR, physician-assisted suicide, palliative sedation ‘at the minimal dosages necessary’, double effect); ICMR consensus guidelines on DNAR
#    (IJMR 2020;151:303–310): form signed, timed and dated by patient/surrogate and physician; DNAR does not mean withholding other treatment; if in doubt, CPR is the default.
#  - EAPC revised framework on palliative sedation (Palliative Medicine, Jan 2024): proportionality in the definition; refractory = untreatable and intolerable; no fixed life expectancy.
#  - Bharatiya Nyaya Sanhita: no general offence of attempted suicide (only an attempt made to compel or restrain a public servant); Mental Healthcare Act 2017 s115 presumes severe stress.
# Re-checked online in the independent review (13 Nov 2026): Rathinam (26 April 1994, two judges, Hansaria and Sahai) and Gian Kaur (21 March 1996, five judges, Verma J;
# Rathinam held not correct); Aruna Shanbaug (KEM staff held to be her next friend and wished her to live; died 18 May 2015, pneumonia); Law Commission 196th (2006), 210th (2008),
# 241st (2012); BNS in force 1 July 2024 (s226 keeps only an attempt to compel or restrain a public servant); MHA 2017 s115; MoHFW draft text (‘the following conditions must apply’;
# ethics committee ‘may’ be constituted; CMO nominee ‘may be from the same hospital’; not finalised as far as found); Harish Rana v Union of India, 11 March 2026 (two judges; CANH is
# medical treatment; best interests; DAMA misuse disapproved; district CMO panels); Mani et al. IJCCM 2024;28(3):200–250; ICMR DNAR IJMR 2020;151(4):303–310; SSC 2021 (goals of care
# early, within 72 h, weak; against routine formal palliative consultation, conditional); Lautrette 2007 NEJM (22 French ICUs, 126 relatives); Carson 2016 JAMA; Maltoni 2012 JCO
# systematic review; EAPC 2024 framework (midazolam first line; opioids and haloperidol not for sedation; CDS when lighter sedation fails); WHO ladder 1986, three steps; four conditions
# of double effect. Standard teaching, not re-opened: Beauchamp and Childress; Egan’s SOLER; glycopyrrolate vs hyoscine pharmacology; stopping neuromuscular blockers before withdrawal.

SPINE = [
  ("Naming the decisions", "Withholding means not starting or not escalating a treatment, withdrawal means stopping it, and in both the disease, not the doctor, causes the death; only euthanasia and assisted suicide use a drug to end life."),
  ("The ethics that justify them", "Autonomy (or a surrogate’s substituted judgment) decides what is accepted, doctors are not obliged to give futile treatment, and double effect allows symptom relief that may hasten death as long as death is not the intention."),
  ("Recognising futility", "The process starts when the team judges, from age, function and response to treatment, that further intensive care will not return the patient to a life worth having, and this is the hardest step."),
  ("Consensus, disclosure, shared decision", "The team agrees among itself first, then tells the family honestly and early, decides with them, documents, and continues treatment while consensus is not yet reached."),
  ("Comfort and a good death", "Once the goal is comfort, pain, breathlessness, secretions and agitation are treated by the clock with opioids, glycopyrrolate and sedatives titrated to symptoms, and the family is cared for before and after the death."),
  ("The law in India", "Active euthanasia is illegal; withdrawal and withholding are lawful since Aruna Shanbaug (2011) and Common Cause (2018), and since January 2023 they need two hospital medical boards of 5-year experts and an intimation to the magistrate, not a court."),
]

PRIMER = "Life-sustaining treatment is anything that keeps a patient alive without curing the illness: ventilation, vasopressors, dialysis, artificial nutrition, CPR. In the ICU most deaths now follow a decision to limit such treatment, so the questions are who decides, on what ethical grounds, by what steps, and with what legal protection. A patient with capacity decides for himself; for one without, a surrogate speaks for him, ideally guided by an advance directive. In India the courts used the term ‘passive euthanasia’ for withdrawal or withholding, and ISCCM prefers to call it limitation of life support."

L = {}

L['EOL-01'] = dict(
  sub="End-of-life care → Definitions → The five terms",
  step=1,
  intro="Step 1 is naming the decisions, because every later card uses these words. The intensivist can decide not to add a treatment, to take one away, or not to attempt CPR, and the care that follows is palliative or end-of-life care. No bank question is linked to this card.",
  parts=[
    ('a', "**Withholding: a decision not to start or escalate a life-sustaining treatment (e.g. DNR, non-escalation).** Not starting dialysis, not adding a second vasopressor, not reintubating after a planned extubation. The patient keeps what he already has."),
    ('b', "**Withdrawal: a decision to stop or remove one.** Stopping vasopressors, dialysis or ventilation. It feels more active than withholding, but ethically the two are equivalent: if a treatment is no longer benefiting the patient, there is no reason to continue it merely because it was started, and the disease is the cause of death in both."),
    ('c', "**DNAR: no CPR, given terminal illness and the patient’s or surrogate’s wishes.** It concerns CPR only. ICMR’s 2020 DNAR guidance is explicit that it does not mean withholding other treatment: antibiotics, fluids, vasopressors and pain relief continue unless separately limited. The form is signed, timed and dated by the patient or surrogate and the physician; when the physician is unsure, CPR is the default."),
    ('d', "**Palliative care: from diagnosis of a life-threatening illness; quality of life alongside treatment.** It is not reserved for the dying and does not replace active treatment; it runs with it."),
    ('e', "**End-of-life care: at the end stage — comfort, dignity, quality of dying, closure; includes the family.** It is the last part of palliative care, when the goal has changed from survival to a good death."),
  ],
  mimic=[
    ("Withholding vs withdrawal", "Not starting or not escalating vs stopping something already running; ethically and legally the same decision."),
    ("DNAR vs ‘no treatment’", "DNAR removes CPR only; everything else continues unless a separate decision limits it."),
  ],
  traps=[
    ("Believing withdrawal is morally worse than withholding", "It only feels worse; ethically they are equivalent, and treating them differently makes teams reluctant to start a trial of treatment for fear they could never stop it."),
    ("Reading DNAR as an order to stop all treatment", "ICMR states that DNAR does not mean withdrawal or withholding of other life-supporting treatment."),
  ],
  decode=[
    ("A patient on noradrenaline is not started on vasopressin and not offered dialysis — what is this? [pattern]", "Withholding (non-escalation)."),
    ("Palliative care is appropriate from which point? [pattern]", "From the diagnosis of a life-threatening illness, alongside curative treatment, not only at the end."),
  ],
  punch="Withholding is not starting, withdrawal is stopping, and the two are ethically the same; DNAR removes CPR and nothing else; palliative care begins at diagnosis and end-of-life care is its last stage.",
)

L['EOL-02'] = dict(
  sub="End-of-life care → Definitions → Ways of ending life compared",
  step=1,
  intro="Still step 1. The card separates five acts by two questions: what causes the death, and what the doctor intends. The first three are lawful end-of-life care; the last two are not permitted in India. No bank question is linked to this card.",
  parts=[
    ('a', "**Withhold treatment: the underlying disease causes death; the intent is to avoid a burdensome intervention.** The patient dies of what he was dying of, without an extra burden."),
    ('b', "**Withdraw treatment: the underlying disease causes death; the intent is to remove a burdensome intervention.** Stopping the ventilator lets the lung disease take its course; it does not introduce a new cause of death."),
    ('c', "**Palliative sedation and analgesia: the underlying disease causes death; the intent is to relieve symptoms.** Sedatives and opioids are titrated to the minimum dose that controls a refractory symptom (ICMR: ‘at the minimal dosages necessary’). Titrated this way they have not been shown to shorten survival, and if they did, double effect covers it (EOL-04)."),
    ('d', "**Physician-assisted suicide: a drug used by the patient; the intent is to end life.** The doctor provides the means and the patient takes it. Not permitted in India."),
    ('e', "**Euthanasia: a drug given by the doctor; the intent is to end life.** Active euthanasia, such as a lethal injection, was held illegal in Aruna Shanbaug (2011) and remains so; only Parliament could change that."),
  ],
  mimic=[
    ("Palliative sedation vs euthanasia", "Intent to relieve a symptom, dose titrated to the symptom, death from the disease vs intent to end life, dose chosen to kill, death from the drug."),
    ("Assisted suicide vs euthanasia", "Who gives the final drug: the patient vs the doctor."),
  ],
  traps=[
    ("Calling withdrawal of ventilation ‘active euthanasia’ because the doctor acts", "The act is removing a treatment; death comes from the disease, and the courts call it passive euthanasia, which is lawful."),
    ("Treating ‘passive euthanasia’ as a third illegal category", "In Indian law passive euthanasia is simply withdrawal or withholding, and it is lawful under the Common Cause procedure."),
  ],
  decode=[
    ("Which of the following is permitted in India: physician-assisted suicide, active euthanasia, withdrawal of life support, lethal injection on request? [pattern]", "Withdrawal of life support."),
  ],
  punch="Ask two things: what causes the death and what the doctor intends; when the disease causes it and the intent is to remove a burden or relieve a symptom, it is lawful end-of-life care.",
)

L['EOL-03'] = dict(
  sub="End-of-life care → Ethics → The four principles",
  step=2,
  intro="Step 2 is the ethics that justify the decisions of step 1. The four principles of Beauchamp and Childress are applied to the dying patient. Both linked DocT questions test autonomy: what respecting it does and does not allow, and which principle advance directives and surrogates serve. Only 20% chose the right answer to the first, so the common belief that autonomy means ‘do whatever the patient wants’ is the live trap.",
  parts=[
    ('a', "**Autonomy: informed consent or refusal; needs capacity and full information. No capacity: surrogate (substituted judgment); wishes unknown: best interests.** A choice is autonomous only when the patient understands, can weigh the information and is free of pressure. Respecting it allows the doctor to persuade with honest argument and evidence; it forbids coercion (a threat) and manipulation (distorted or selective information). It gives the patient a right to refuse, not a right to demand: there is no duty to provide treatment that will not help. When capacity is lost, autonomy is carried forward by an advance directive or by a surrogate who says what the patient would have chosen (substituted judgment); only when his wishes cannot be known does the surrogate fall back on best interests. That is why advance directives and surrogates belong to autonomy, not to beneficence. A refusal protects the doctor only if it was properly informed: risks that were never explained still carry liability."),
    ('b', "**Beneficence: act in the patient’s best interest; includes protecting the family from financial ruin. Insisting on futile care violates it.** Futile care brings burden without benefit, so it is not in the patient’s interest. The family’s finances are part of the Indian position (ISCCM) because most ICU care is paid out of pocket and ruin follows the patient’s family after his death."),
    ('c', "**Non-maleficence: first, do no harm — pain, distress, and harm to the family.** Prolonging dying with painful procedures is a harm, even when each procedure is done well."),
    ('d', "**Justice: fair use of resources; futile therapy violates it.** An ICU bed given to a patient who cannot benefit is denied to one who can. Policy-level budget decisions are macro-allocation; deciding who gets the last bed or ventilator is micro-allocation."),
  ],
  table=dict(title="What respecting autonomy allows", head=["Act", "Allowed?", "Why"], rows=[
    ["Persuading with honest argument and evidence", "Yes", "Leaves the choice with the patient"],
    ["Coercion by a credible threat", "No", "Removes free choice"],
    ["Manipulation by selective or false information", "No", "Corrupts the information the choice depends on"],
    ["Giving any treatment the patient demands", "No", "No duty to give non-beneficial treatment"],
    ["Accepting an uninformed refusal as protection", "No", "Liability remains for risks not explained"],
  ]),
  mimic=[
    ("Substituted judgment vs best interests", "What this patient would have chosen (his values, his directive) vs what a reasonable person would judge best for him when his wishes are unknown; Indian courts (Aruna Shanbaug 2011, Harish Rana 2026) apply a best-interests test to incapacitated patients without a directive, with his known wishes as one factor in it."),
    ("Autonomy vs justice", "The family demands futile care (autonomy) while the bed is needed elsewhere (justice): resolved by repeated communication and negotiation, not by giving in or by unilateral withdrawal."),
  ],
  traps=[
    ("‘Physicians are obligated to do whatever the patient wants’ [DocT GT]", "Autonomy is a right to refuse and to choose among appropriate options; it does not create a duty to give inappropriate treatment."),
    ("‘If a patient refuses, the physician cannot be liable’ [DocT GT]", "Only an informed refusal protects; if the risks were not explained, liability remains."),
    ("‘Coercion with a credible threat is acceptable to save life’ [DocT GT]", "A threat removes free choice; persuasion with legitimate argument is the limit."),
    ("Linking advance directives to beneficence because they are ‘for the patient’s good’", "They express the patient’s own choice in advance, which is autonomy."),
  ],
  decode=[
    ("Which is true regarding respect for autonomy: coercion by credible threat, persuasion by legitimate argument, doing whatever the patient wants, no liability after refusal? [DocT GT, 20% right]", "Persuasion by legitimate argument."),
    ("Which principle primarily supports advance directives and surrogate decision-making in the ICU? [DocT GT]", "Autonomy."),
    ("The family insists on continuing dialysis in a patient with no prospect of recovery while beds are short — which principles conflict? [pattern]", "Autonomy (the surrogate’s demand) and justice (fair use of resources); also beneficence, since futile care does not serve him."),
  ],
  punch="Autonomy is the right to an informed choice and to refuse, kept alive after capacity is lost by directives and surrogates; it allows persuasion, never coercion, and never obliges a doctor to give futile treatment.",
)

L['EOL-04'] = dict(
  sub="End-of-life care → Ethics → Double effect",
  step=2,
  intro="Still step 2. Comfort drugs at the end of life can depress breathing, and teams fear that relieving suffering is the same as killing. The doctrine of double effect separates the two by intention and by dose. No bank question is linked to this card.",
  parts=[
    ('a', "**An act with a good intention (relieving suffering) is ethical even if it has a foreseen bad effect (hastening death), provided the bad effect is not intended.** The classic conditions: the act itself is good or neutral (giving an analgesic), only the good effect is intended, the bad effect is not the means to the good one, and the good outweighs the bad. In practice, opioids and sedatives titrated to symptoms have not been shown to shorten survival, so double effect is a safeguard more often than a real trade-off."),
    ('b', "**So: titrate opioids and sedatives to symptoms, not to death.** Intention shows in the dose: small increments in response to pain, breathlessness or agitation. A sudden large dose with no symptom to treat cannot be explained as relief."),
    ('c', "**Document the indication and doses meticulously.** The record of the symptom, the dose and the response is what shows that the intent was relief."),
  ],
  mimic=[
    ("Double effect vs active euthanasia", "Dose titrated to a symptom, death foreseen but not intended vs a large dose given deliberately to end life."),
    ("Proportional palliative sedation vs continuous deep sedation", "Consciousness lowered only as far as needed to control a refractory symptom, light or intermittent first (EAPC 2024) vs deep sedation until death, considered when lighter sedation has failed and generally in the final stage of life; EAPC 2024 sets no fixed life expectancy."),
  ],
  traps=[
    ("Withholding morphine from a breathless dying patient for fear of respiratory depression", "Titrated morphine relieves breathlessness, and any hastening of death, if it occurs, is covered by double effect; leaving the symptom untreated is the harm."),
    ("Thinking a large bolus is double effect because the motive was compassion", "Given to end life, it is euthanasia; double effect needs the bad effect to be unintended and the dose proportionate."),
  ],
  decode=[
    ("A dying patient’s dyspnoea is treated with titrated morphine; respiratory rate falls. Which principle justifies it? [pattern]", "Double effect."),
  ],
  punch="Relief that may hasten death is ethical when relief is the intention, the dose is titrated to the symptom and the record shows it; a dose meant to end life is euthanasia whatever the motive.",
)

L['EOL-05'] = dict(
  sub="End-of-life care → The process → Recognising futility",
  step=3,
  intro="Step 3 is where the process starts. Before any family meeting or legal step, someone has to judge that further intensive treatment will not help. The card lists the situations in which that judgement is usually reached. No bank question is linked to this card.",
  parts=[
    ('a', "**Advanced age with poor functional state.** Physiological reserve and the pre-illness function predict whether the patient can return to an acceptable life."),
    ('b', "**Severe illness refractory to reasonable aggressive treatment.** Escalating organ failure despite appropriate treatment over a reasonable trial is the commonest ICU route to futility."),
    ('c', "**Coma from an acute catastrophic, irreversible cause.** Massive haemorrhagic stroke or devastating brain injury."),
    ('d', "**Severe chronic neurological disease (advanced dementia, vegetative state).**"),
    ('e', "**Progressive metastatic cancer after failed treatment.**"),
    ('f', "**Prolonged poor neurological state after cardiac arrest.** Judged after an adequate interval and multimodal prognostication, not on day one."),
    ('g', "**Any comparable situation with a predicted low chance of survival.** Futility is a reasonable prediction, not a certainty; the experience of the team and a mortality estimate support it."),
  ],
  mimic=[
    ("Quantitative vs qualitative futility", "Treatment very unlikely to work vs treatment that may keep the patient alive but cannot restore a life he would value."),
  ],
  traps=[
    ("Waiting for certainty before discussing futility", "Prognosis is never certain; the standard is a reasonable prediction, and delay prolongs suffering."),
    ("Declaring futility on age alone", "Age counts with poor function and refractory illness, not by itself."),
  ],
  decode=[
    ("Which is the first and most difficult step of end-of-life care in the ICU? [pattern]", "Recognising futility."),
  ],
  punch="Everything starts with a reasonable, experienced judgement that more intensive treatment will not help; age, function, refractory illness and irreversible brain injury are the usual grounds.",
)

L['EOL-06'] = dict(
  sub="End-of-life care → The process → The ISCCM steps",
  step=4,
  intro="Step 4 turns the judgement of step 3 into a decision. The ISCCM–IAPC policy (2014, updated 2024) sets an order that protects the family from mixed messages: the team agrees first, then speaks once, honestly. Both linked DocT questions test this card: one on how the decision is made with an emotional surrogate (78% right), one on what palliative care involvement achieves (95% right).",
  parts=[
    ('a', "**1. Recognise futility and the dying process.** EOL-05."),
    ('b', "**2. Consensus among all caregivers before meeting the family.** If the cardiologist offers hope that the intensivist has given up, the family hears disagreement and trust is lost. Disagreement inside the team is resolved first, with a second opinion if needed."),
    ('c', "**3. Honest, early disclosure of prognosis: imminent death, futility, natural death; respect hope, stay realistic.** Early disclosure gives the family time; hope is redirected to comfort and to time together, not denied."),
    ('d', "**4. Discuss modalities: DNR, withdrawal, withholding (non-escalation).** The family is told what will be continued (comfort, nursing, presence) as well as what will stop."),
    ('e', "**5. Shared decision-making; no consensus yet → continue and review.** The doctor gives a clear recommendation, the family contributes the patient’s values, and the decision is made together. Neither extreme is right: the physician deciding and merely informing, or the family deciding alone with the full burden. A surrogate who is struggling needs emotional support within the shared process, not to hand everything to an ethics team. If there is no agreement, current treatment continues and the discussion is repeated."),
    ('f', "**6. Document discussions, process and decision.** Who was present, what was said, what was decided and why; this is also the legal protection."),
    ('g', "**7. Implement: prepare staff, family, room; limitation form signed by family and team.** Plan the order of withdrawal; stop investigations and non-comfort drugs; stop tube feeds (they add aspiration and bloating, not comfort; the Supreme Court in Harish Rana, March 2026, held that clinically assisted nutrition and hydration is medical treatment that the boards may withdraw); stop neuromuscular blockers before ventilation is withdrawn so distress can be seen and treated."),
    ('h', "**8. Compassionate palliative care (symptoms, preferred place, rituals, liberal visiting). Then after-death care (certify early, dignified exit) and bereavement support (starts before death).** Comfort measures continue: opioids, anxiolytics, glycopyrrolate, oxygen if it eases breathlessness, mouth and eye care (EOL-08)."),
  ],
  mimic=[
    ("Shared decision-making vs informed consent", "The team brings a recommendation and the family brings the patient’s values, decided together vs the doctor offers options and the family carries the choice alone."),
    ("Palliative care consult for triggered cases vs for every patient", "Proactive involvement for poor-prognosis ventilated patients often shortens stay and lowers cost; the Surviving Sepsis Campaign 2021 suggests (conditional) against routine formal consultation for every septic patient, partly because trials gave mixed effects on families."),
  ],
  traps=[
    ("‘Physician decides and informs the family’ [DocT GT]", "Paternalism ignores the patient’s values carried by the surrogate; the recommended model is shared decision-making with emotional support."),
    ("‘Surrogate defers all choices to the ethics team’ [DocT GT]", "An ethics committee helps resolve conflict; it does not replace the surrogate."),
    ("Telling the family first and then reaching consensus in the team", "Consensus comes first (EOL-12e); otherwise the family hears contradictory messages."),
    ("Accepting DAMA/LAMA for financial reasons", "The patient dies at home or on the way without palliation; the right answer is limitation of treatment with comfort care in hospital. The Supreme Court (Harish Rana, 2026) also disapproved of using discharge against advice once treatment has stopped."),
    ("Believing palliative involvement increases stay or invasive procedures [DocT GT]", "It reduces non-beneficial procedures, ICU readmission and cost without raising mortality. Effects on families are mixed: one trial of palliative-care-led family meetings (Carson, JAMA 2016) did not reduce relatives’ anxiety or depression and may have increased post-traumatic stress symptoms."),
  ],
  decode=[
    ("Ventilated patient with poor prognosis; benefit most consistently associated with multidisciplinary palliative care involvement? [DocT GT, 95% right]", "Reduced ICU readmission and cost savings."),
    ("Multi-organ failure despite maximal support; the daughter-surrogate struggles emotionally with withdrawal — best approach? [DocT GT, 78% right]", "Shared decision-making with emotional support."),
    ("Family not yet ready to agree to withdrawal — next step? [pattern]", "Continue current treatment and review with repeated meetings; do not withdraw unilaterally."),
  ],
  table=dict(title="Withdrawing support: what stops, what continues", head=["Stop", "Continue"], rows=[
    ["Investigations, non-comfort drugs, vasopressors, dialysis", "Opioids and anxiolytics titrated to symptoms"],
    ["Tube feeds", "Glycopyrrolate for secretions, mouth and eye care"],
    ["Neuromuscular blockers (before ventilation is withdrawn)", "Oxygen if it eases breathlessness"],
    ["Routine observations and alarms", "Liberal visiting, rituals, family presence"],
  ]),
  punch="Agree as a team, tell the family early and honestly, decide with them while supporting them, write it down, and keep treating if agreement has not come; then make comfort the whole of the care.",
)

L['EOL-07'] = dict(
  sub="End-of-life care → The process → Communication",
  step=4,
  intro="Still step 4. The disclosure and shared decision of EOL-06 happen at a family meeting, and how it is run decides whether the family trusts the team. No bank question is linked to this card.",
  parts=[
    ('a', "**Intensivist coordinates; consensus among specialists first; meeting with all significant family.** One coordinator speaks for one agreed team. Having all decision-makers present avoids the relative who arrives later and reverses the plan."),
    ('b', "**Disease process, likely prognosis, time available, comfort options.** The family should leave knowing what is happening, how it is likely to end, roughly how long, and what will be done for comfort. Listening matters more than talking: in a French trial (Lautrette, NEJM 2007), a proactive end-of-life conference in which relatives spoke for about half the time, plus a bereavement brochure, reduced their anxiety, depression and post-traumatic stress symptoms at 90 days."),
    ('c', "**SOLER: Squarely face at eye level, Open posture, Lean toward, Eye contact (no phone), Relaxed.** These are the non-verbal signals of attention (Egan). Sitting at eye level rather than standing over a family is the single most visible one."),
  ],
  mimic=[
    ("Coordinator-led meeting vs separate specialist conversations", "One agreed message vs several partial and sometimes contradictory ones."),
  ],
  traps=[
    ("Holding the family meeting before the specialists agree", "Consensus comes first (EOL-06 step 2)."),
  ],
  decode=[
    ("Who should coordinate end-of-life discussions with the family in the ICU? [pattern]", "The intensivist, after consensus among the specialists."),
  ],
  punch="One coordinator, one agreed message, the whole family present, attention shown by posture, and the family leaves knowing the prognosis, the time and the comfort plan.",
)

L['EOL-08'] = dict(
  sub="End-of-life care → Comfort → Symptom control",
  step=5,
  intro="Step 5 is comfort once the goal has changed. Four symptoms dominate dying in the ICU, and each has a first-line drug. Doses are titrated to the symptom, which is also what keeps them within double effect (EOL-04). No bank question is linked to this card.",
  parts=[
    ('a', "**Pain: mild — paracetamol, ibuprofen, ketorolac; moderate — oxycodone, morphine, fentanyl; severe — infusion or PCA; pain team.** In the ICU most dying patients cannot report pain, so behavioural scales guide dosing. Fentanyl is preferred when renal failure would let morphine’s active metabolites accumulate."),
    ('b', "**Secretions: gentle suction; glycopyrrolate; scopolamine patch.** Antimuscarinics reduce new secretions but cannot clear what is already there, so start them early. Glycopyrrolate is a quaternary amine that does not cross the blood–brain barrier, so it does not sedate or cause delirium; hyoscine hydrobromide (scopolamine) does cross and can cause both. The noise distresses the family more than the patient; positioning and explanation help."),
    ('c', "**Dyspnoea: oxygen as needed; morphine; lorazepam if anxious.** Low-dose opioids reduce the sensation of breathlessness. Oxygen helps only if the patient is hypoxaemic or feels better with it; a fan on the face also helps."),
    ('d', "**Agitation: look for pain, hypoxia, poor sleep; lorazepam; haloperidol.** Treat a cause first (pain, full bladder, hypoxia). Haloperidol for delirium; benzodiazepines for anxiety or as palliative sedation, midazolam being the first-line drug (EAPC 2024). Opioids and haloperidol are not used as sedatives: raising an opioid to sedate adds toxicity without reliable sedation."),
  ],
  mimic=[
    ("Glycopyrrolate vs hyoscine hydrobromide", "Peripheral only, no sedation vs crosses into the brain, sedates and can cause delirium."),
  ],
  traps=[
    ("Giving opioids only ‘as needed’ to a dying patient with continuous pain", "Dose by the clock (WHO ladder rule); on-demand dosing leaves gaps of pain."),
    ("Combining two drugs of the same class (two opioids, two NSAIDs)", "Adds side effects without adding analgesia."),
  ],
  decode=[
    ("Noisy upper-airway secretions in a dying patient; drug that will not add sedation? [pattern]", "Glycopyrrolate."),
    ("Drug of choice for refractory breathlessness at the end of life? [pattern]", "Morphine (low-dose opioid)."),
  ],
  punch="Morphine for pain and breathlessness, glycopyrrolate for secretions, a cause and then lorazepam or haloperidol for agitation, all given by the clock and titrated to the symptom.",
)

L['EOL-09'] = dict(
  sub="End-of-life care → Comfort → A good death and its barriers",
  step=5,
  intro="Still step 5. The card sets out what a good death looks like and why Indian ICUs often fail to provide it. No bank question is linked to this card.",
  parts=[
    ('a', "**Knowing death is near; symptoms controlled; wishes respected; dignity at a place of choice; life not prolonged artificially.** Each item is something the team can deliver once it accepts that the patient is dying."),
    ('b', "**No consensus within the medical community, unawareness of ethical issues, a culture of fighting till the end, little palliative orientation, fear of litigation, no legal backing or regulatory requirement (NABH).** Fear of prosecution was the main legal barrier; Common Cause (2018) and its 2023 simplification answered much of it, but awareness and practice lag."),
    ('c', "**Convincing colleagues.** The hardest barrier is inside the profession, not the family: specialists who see any death as failure."),
  ],
  mimic=[
    ("Barrier from families vs from doctors", "Families usually accept honest disclosure; disagreement among doctors is the larger obstacle."),
  ],
  traps=[
    ("Assuming the main barrier is the family’s refusal", "The card names convincing colleagues as the biggest challenge."),
  ],
  decode=[
    ("Biggest challenge to end-of-life care in Indian ICUs? [pattern]", "Convincing colleagues (lack of consensus in the medical community)."),
  ],
  punch="A good death means knowing it is coming, comfort, respected wishes and no artificial prolonging; in India the largest obstacle is persuading other doctors.",
)

L['EOL-10'] = dict(
  sub="End-of-life care → Law in India → The cases",
  step=6,
  intro="Step 6 is the law, which turns the ethics into protection for the team. The cases moved from whether there is a right to die, through allowing withdrawal under court control, to a right to die with dignity with advance directives. No bank question is linked to this card.",
  parts=[
    ('a', "**1994, P. Rathinam vs Union of India: right to die read into Article 21 (later overruled).** A two-judge bench struck down IPC 309 (attempted suicide)."),
    ('b', "**1996, Gian Kaur vs State of Punjab: no right to die; upheld IPC 309.** A five-judge bench held that the right to life does not include a right to end it, overruling Rathinam."),
    ('c', "**2006/2008, Law Commission reports: euthanasia; decriminalising suicide attempt.** The 196th report (2006) dealt with withholding or withdrawing treatment from the terminally ill, protecting both patients who refuse treatment and their doctors, not with active euthanasia; the 210th report (2008) called IPC 309 inhuman and recommended removing it. A later 241st report (2012) returned to passive euthanasia after Aruna Shanbaug. Attempted suicide is now effectively decriminalised: the Mental Healthcare Act 2017 (section 115) presumes severe stress, and the Bharatiya Nyaya Sanhita, which replaced the IPC in 2024, has no general offence of attempted suicide."),
    ('d', "**2011, Aruna Shanbaug vs Union of India: passive euthanasia allowed, via the High Court.** A two-judge bench (7 March 2011) held active euthanasia illegal but allowed withdrawal of life support from a patient in a vegetative state, on application by relatives or a ‘next friend’, with the High Court’s approval under Article 226 after a committee of three doctors examined the patient. Aruna herself was not allowed it, because the KEM hospital staff caring for her wanted to continue."),
    ('e', "**2018, Common Cause vs Union of India: right to die with dignity (Article 21); advance directives (living wills).** A five-judge Constitution Bench (9 March 2018) held that a capable adult may refuse life-sustaining treatment, may make an advance directive for when capacity is lost, and that treatment may be withheld or withdrawn from those without capacity even without one, with palliative care continuing. It replaced the court route with medical boards (EOL-11)."),
  ],
  mimic=[
    ("Aruna Shanbaug vs Common Cause", "2011, two judges, withdrawal with High Court approval, no advance directives vs 2018, five judges, right to die with dignity, advance directives, medical boards."),
    ("Gian Kaur vs Rathinam", "No right to die (five judges, 1996) vs a right to die (two judges, 1994, overruled)."),
  ],
  traps=[
    ("‘Common Cause legalised active euthanasia’", "It did not; active euthanasia and assisted suicide remain illegal (EOL-12c)."),
    ("Thinking Aruna Shanbaug herself had life support withdrawn", "The petition was refused; she died in May 2015 of pneumonia. The first withdrawal reported as approved by the Supreme Court under the Common Cause framework was Harish Rana (March 2026)."),
  ],
  decode=[
    ("Which judgment first allowed passive euthanasia in India? [pattern]", "Aruna Shanbaug (2011)."),
    ("Which judgment recognised advance directives and the right to die with dignity under Article 21? [pattern]", "Common Cause (2018)."),
  ],
  extra=[
    dict(q="Indian end-of-life guidelines in order?", a="ISCCM 2005, revised 2012; joint ISCCM–IAPC policy 2014 (Myatra, IJCCM); updated joint ISCCM–IAPC statement 2024 (Mani, IJCCM); ICMR DNAR guidelines 2020; MoHFW draft guidelines on withdrawal of life support, September 2024."),
    dict(q="What did Harish Rana v Union of India (2026) add?", a="A two-judge bench (11 March 2026) allowed withdrawal of clinically assisted nutrition and hydration from a man in a vegetative state for 13 years, reported as the first withdrawal approved under the Common Cause framework. It held that such nutrition is medical treatment, set out a holistic best-interests test, said withdrawal must not mean abandonment (palliative care continues; misuse of discharge against advice disapproved), directed that each district’s Chief Medical Officer keep a panel of doctors for secondary boards, and urged Parliament to legislate."),
  ],
  punch="Rathinam gave a right to die, Gian Kaur took it away, Aruna Shanbaug (2011) allowed withdrawal through the High Court, and Common Cause (2018) made dying with dignity part of Article 21 with advance directives.",
)

L['EOL-11'] = dict(
  sub="End-of-life care → Law in India → The 2023 board process",
  step=6,
  intro="Still step 6. The 2018 procedure was so heavy (Collector, 20-year experts, a magistrate’s visit) that it was hardly workable in an ICU. On ISCCM’s application the Supreme Court simplified it on 24 January 2023, and this card is that procedure. No bank question is linked to this card.",
  parts=[
    ('a', "**Applies to: patients who have lost capacity AND are terminally ill, where further treatment would not benefit.** A patient with capacity simply refuses; no board is needed."),
    ('b', "**1. Primary Medical Board: treating physician + 2 subject experts with 5+ years → opinion.** The hospital forms it; the order says at least two experts and asks for the opinion preferably within 48 h."),
    ('c', "**2. Inform next of kin (or those named in the advance directive) and obtain their concurrence.** With a valid directive, the persons named in it give consent; without one, the next of kin, next friend or guardian. Directives are now signed before two witnesses and attested by a notary or gazetted officer, no longer countersigned by a magistrate."),
    ('d', "**3. Secondary Medical Board within 48 h: a doctor nominated by the district CMO + 2 experts (5+ years) not on the first board.** It is also formed by the hospital, not the Collector, and confirms the first board’s opinion."),
    ('e', "**4. Boards agree → hospital records and informs the Judicial Magistrate → team implements.** Intimation only; the magistrate no longer visits or authorises."),
    ('f', "**5. Boards disagree → family, team or hospital may approach the High Court.** The order gives this route whenever a board refuses to certify withdrawal: a writ under Article 226, heard by a Division Bench, which may appoint an independent committee of three doctors of at least 20 years’ standing and decides on the patient’s best interests."),
  ],
  table=dict(title="2018 vs 2023", head=["Step", "2018", "2023"], rows=[
    ["Advance directive", "Countersigned by a JMFC", "Two witnesses + notary or gazetted officer"],
    ["Primary board", "Head of department + 3 experts, 20 years", "Treating physician + ≥2 experts, 5 years, ~48 h"],
    ["Secondary board", "Formed by the Collector, chaired by the CDMO, 20-year experts", "Formed by the hospital: CMO nominee + ≥2 experts, 5 years, ~48 h"],
    ["Magistrate", "Visits and authorises", "Informed only"],
  ]),
  mimic=[
    ("Primary vs secondary board", "Treating physician + 2 experts vs CMO nominee + 2 different experts; both 5 years, both about 48 h."),
  ],
  traps=[
    ("Still teaching 20-year experts or the magistrate’s visit", "That is the 2018 procedure, replaced in January 2023."),
    ("‘Secondary board decides within 7 days’", "Preferably within 48 h (EOL-12h)."),
  ],
  decode=[
    ("Minimum experience of experts on the medical boards after the 2023 modification? [pattern]", "5 years."),
    ("After both boards agree, whom does the hospital inform? [pattern]", "The jurisdictional Judicial Magistrate First Class (intimation, not permission)."),
  ],
  extra=[
    dict(q="What did the MoHFW draft guidelines (September 2024) add?", a="They restate the 2023 boards for ICUs: PMB members may be from the treating team and the CMO nominee from the same hospital; terminal illness includes severe traumatic brain injury with no recovery after ≥72 h; the listed conditions are brainstem death, advanced disease unlikely to benefit from aggressive treatment, documented informed refusal by patient or surrogate, and compliance with the Supreme Court procedure (worded ‘must apply’, though the first two are really alternatives); the magistrate form is notification only, not approval; hospitals may set up clinical ethics committees. Released for comment in late September 2024; no final version had been published as far as could be found (November 2026)."),
  ],
  punch="Two hospital boards of 5-year experts, each in about 48 hours, the family’s or named persons’ consent, then a note to the magistrate; only disagreement goes to the High Court.",
)

L['EOL-12'] = dict(
  sub="End-of-life care → Sweep → True or false",
  step=6,
  intro="The sweep tests the whole story, one statement per step. No bank question is linked to it; each statement is the form an examiner would use.",
  parts=[
    ('a', "**Withholding and withdrawing are ethically equivalent: true.** Stopping a treatment that no longer helps is the same decision as not starting it (EOL-01)."),
    ('b', "**After withdrawal, the cause of death is the withdrawal: false — the underlying disease.** Removing treatment lets the disease take its course (EOL-02)."),
    ('c', "**Active euthanasia is legal in India since 2018: false — not permitted.** Common Cause allowed withdrawal, withholding and advance directives only (EOL-10)."),
    ('d', "**Titrating morphine for dyspnoea is justified by double effect: true.** Intent is relief and the dose follows the symptom (EOL-04)."),
    ('e', "**Family is told first, then caregivers reach consensus: false — among caregivers first.** (EOL-06 step 2)."),
    ('f', "**DAMA is the preferred route for financial futility: false — discouraged.** The patient dies without palliation (EOL-06)."),
    ('g', "**Aruna Shanbaug (2011) allowed passive euthanasia: true.** With High Court approval (EOL-10)."),
    ('h', "**The secondary medical board decides within 7 days: false — within 48 h.** Preferably within 48 h under the 2023 order (EOL-11)."),
  ],
  mimic=[
    ("Withdrawal (lawful) vs active euthanasia (unlawful)", "Removing a treatment, death from the disease vs giving a drug, death from the drug."),
  ],
  traps=[
    ("Reading ‘since 2018’ as making the euthanasia statement true", "2018 legalised the right to die with dignity through withdrawal, not active euthanasia."),
  ],
  decode=[
    ("Which statement about end-of-life care in India is true? [pattern]", "Look for withholding = withdrawal, double effect for titrated opioids, Aruna Shanbaug 2011, and 48 h for the boards."),
  ],
  punch="Withholding equals withdrawal, the disease is the cause of death, titrated morphine is double effect, the team agrees before the family is told, and the boards work in 48 hours; active euthanasia and DAMA for money are wrong.",
)

FLAGS = {
  'EOL-06': "Card sound. The linked DocT explanation (palliative-care question) says family satisfaction is equal or better; SSC 2021 notes mixed effects on families, and Carson (JAMA 2016) found palliative-care-led meetings did not reduce relatives’ anxiety or depression and may have increased PTSD symptoms. Harish Rana (2026) also disapproved misuse of DAMA once treatment stops, which supports the watch line.",
  'EOL-08': "Watch line gives the WHO ladder as four steps (with ‘interventional’); the original WHO ladder (1986) has three, the fourth is a later adaptation. The card’s ‘moderate pain: oxycodone, morphine, fentanyl’ differs from the WHO ladder’s step 2 (weak opioids such as codeine or tramadol, or low-dose strong opioid). Not wrong for ICU practice; noted.",
  'EOL-10': "Card labels the 2006 Law Commission report ‘Euthanasia’: the 196th report dealt with withholding or withdrawing treatment from the terminally ill and did not support active euthanasia; the 241st report (2012, passive euthanasia) is not on the card. Watch line lists ISCCM 2005, 2012 and the joint ISCCM–IAPC statement (2014) but not the 2024 joint update (Mani et al., IJCCM 2024;28(3):200–250) or the MoHFW draft guidelines (September 2024, still a draft). ‘Upheld IPC 309’ is history: MHA 2017 s115 and the BNS (in force 1 July 2024; no general offence of attempted suicide) have since decriminalised it in effect. Harish Rana v Union of India (11 March 2026; CANH is medical treatment, first approved withdrawal) is not on the card. All added in the explanation.",
  'EOL-11': "Card is correct for the 24 Jan 2023 order. Small points: the order says ‘at least’ two experts and ‘preferably’ within 48 h, and the 48 h applies to the primary board as well; the High Court route applies when a board refuses, not only when the boards disagree. The card omits that advance directives are now attested by a notary or gazetted officer (not a JMFC), the MoHFW draft guidelines of September 2024 (not finalised as far as found), and the Harish Rana (2026) direction that district CMOs keep panels for secondary boards. Added.",
}
