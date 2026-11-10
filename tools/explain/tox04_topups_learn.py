# TOX04 top-up cards — Explain v2 ("Learn" depth), same fields and voice as tox04_learn.py.
# Fields: sub, intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# No `step`: tox04_learn.py has no SPINE (like TOX01, the toxicology decks were written before v3).
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from map/out/all_rows.json, the DocT QBank and GT files (the top-up's own src).
T = {}

T['T_dbdbadf0'] = dict(
  sub="Toxicology → Alcohol → Withdrawal in the ICU: timeline and drug ladder",
  intro="Chronic alcohol enhances GABA-A inhibition and blocks NMDA excitation, and the brain adapts by turning GABA down and NMDA up. Stopping drinking leaves that adapted brain unopposed: an excitable, sympathetic state that runs on a predictable clock. The treatment replaces the missing GABA effect, which is why only some drugs work.",
  parts=[
    ('a', "**Timeline: tremor 6–24 h, withdrawal seizures 6–48 h (peak about 24 h; brief generalised clusters — status epilepticus is uncommon and should prompt a search for epilepsy or head injury), delirium tremens 48–96 h; score with CIWA-Ar.** Withdrawal seizures are brief, generalised and usually over before delirium starts. Status epilepticus or a focal seizure suggests another cause. CIWA-Ar scores the severity and triggers each dose."),
    ('b', "**Thiamine 200–500 mg IV 8-hourly, given before or with glucose.** Glucose metabolism uses thiamine, so glucose given to a depleted patient can precipitate Wernicke encephalopathy; high IV doses are needed because absorption and stores are poor."),
    ('c', "**Symptom-triggered benzodiazepine is first line (diazepam or lorazepam; lorazepam or oxazepam in liver failure).** Benzodiazepines act at the same GABA-A receptor as alcohol, so they replace it and prevent both seizures and delirium. Lorazepam and oxazepam are glucuronidated without active metabolites, so they do not accumulate in liver failure."),
    ('d', "**Benzodiazepine-refractory: phenobarbital 10 mg/kg IV (Rosenson 2013: ICU admission 25% to 8%) or propofol with intubation.** Phenobarbital acts on the GABA-A receptor at a different site and also blocks glutamate, so it works when benzodiazepines no longer do. Rosenson’s randomised trial was not in refractory patients: 102 emergency-department patients with withdrawal received a single 10 mg/kg IV dose or placebo on top of a symptom-guided lorazepam protocol, and ICU admission fell from 25% to 8% without more adverse events; mortality was not an outcome. In the ICU the same drug is used as rescue when large benzodiazepine doses fail."),
    ('e', "**Phenytoin, carbamazepine and levetiracetam do not work (GABA loss and NMDA rebound, not an epileptic focus); dexmedetomidine and clonidine only blunt autonomic signs; haloperidol never alone.** Phenytoin and levetiracetam do not prevent or stop withdrawal seizures, because the problem is a global GABA deficit with NMDA excess rather than an epileptic focus. Carbamazepine is the partial exception: it reduces symptoms in mild-to-moderate withdrawal and is used in outpatient detoxification, but it has no place in severe withdrawal, delirium tremens or the treatment of a seizure. α₂ agonists lower heart rate and blood pressure but do not prevent seizures or delirium, so they are only adjuncts; haloperidol lowers the seizure threshold and is only an add-on for hallucinations."),
  ],
  mimic=[
    ("Withdrawal seizure vs epilepsy or head injury", "Withdrawal: brief generalised seizures 6–48 h after the last drink. Focal seizures or status epilepticus: look for a structural cause (CT)."),
  ],
  traps=[
    ("“Status epilepticus is the commonest seizure complication of withdrawal”", "It is uncommon; brief generalised clusters are typical (79% knew this on DocT GT)."),
    ("“Carbamazepine, levetiracetam or valproate for withdrawal seizures”", "They do not treat the GABA deficit or stop a withdrawal seizure; diazepam with thiamine is the answer (89%)."),
    ("“Phenobarbital reduced DT mortality in the MATCH trial / VA Cooperative Study”", "Both trial names in the DocT keys are wrong (MATCH was a psychotherapy trial), and no trial shows a mortality benefit; the evidence is fewer ICU admissions (Rosenson 2013). Phenobarbital is still the right choice of the options (16% and 73%)."),
    ("“Dexmedetomidine as sole therapy”", "It only blunts autonomic signs; it does not prevent seizures or delirium."),
  ],
  decode=[
    ("Chronic drinker, seizures after 24 h abstinence, confused — best treatment? [DocT]", "Diazepam and thiamine."),
    ("Delirium tremens — next best step? [Marrow]", "IV benzodiazepine."),
    ("Benzodiazepine-refractory withdrawal or DT in ICU — which drug has evidence? [DocT ×2]", "Phenobarbital."),
    ("Alcohol and epilepsy — all true except? [DocT GT]", "Status epilepticus is the commonest seizure complication."),
  ],
  punch="Withdrawal is a brain short of GABA: give thiamine, replace GABA with a benzodiazepine, step up to phenobarbital or propofol when that fails, and do not expect antiepileptics or α₂ agonists to prevent seizures.",
)

T['T_db6f11ba'] = dict(
  sub="Toxicology → Alcohol → Alcoholic cardiomyopathy vs wet beriberi",
  intro="A chronic drinker in shock has two alcohol-related causes of heart failure, and they behave in opposite ways. One is a high-output state from thiamine deficiency that thiamine cures within hours; the other is a dilated, weak heart that thiamine cannot help. The stem gives thiamine first, so the response to it is the clue.",
  parts=[
    ('a', "**Alcoholic dilated cardiomyopathy: LOW-output cardiogenic shock; echo shows a dilated, poorly contracting LV, and thiamine does not reverse it.** Years of alcohol damage the myocytes directly, so the ventricle dilates and the ejection fraction falls; peripheries are cold and filling pressures high. It improves only slowly, over months of abstinence."),
    ('b', "**Wet beriberi (Shoshin): HIGH-output failure with warm peripheries and lactic acidosis that reverses within hours of IV thiamine.** Without thiamine, pyruvate cannot enter the citric acid cycle, so lactate accumulates and vessels dilate; the heart pumps hard into a low-resistance circulation until it fails. Replacing thiamine restores aerobic metabolism quickly."),
    ('c', "**So shock that persists after thiamine points away from beriberi and towards the cardiomyopathy.** The response to the treatment is the diagnostic test."),
    ('d', "**Wernicke encephalopathy itself does not cause neurogenic shock.** Neurogenic shock comes from spinal cord injury above about T6, which cuts sympathetic outflow; confusion, ataxia and ophthalmoplegia do not."),
  ],
  mimic=[
    ("Cardiomyopathy vs beriberi", "Cold, dilated, low output, no thiamine response = cardiomyopathy. Warm, high output, lactic acidosis, prompt thiamine response = beriberi."),
  ],
  traps=[
    ("“Neurogenic shock from Wernicke’s”", "Neurogenic shock is a spinal cord injury; Wernicke’s does not cause it."),
    ("“Septic shock from aspiration”", "Possible in a drinker, but the stem gives no fever or infection; the answer is the heart."),
    ("“Hypovolaemia from vomiting”", "Not described; it would also respond to fluid rather than need vasopressors."),
  ],
  decode=[
    ("Drinker with confusion, ataxia, ophthalmoplegia; thiamine given; now vasopressor-dependent — cause? [DocT GT]", "Alcoholic cardiomyopathy causing cardiogenic shock."),
  ],
  punch="Beriberi is a warm, high-output heart that thiamine fixes in hours; shock that outlasts the thiamine is the cold, dilated alcoholic cardiomyopathy.",
)

FLAGS = {
  'T_dbdbadf0': "Card e says carbamazepine ‘does not work’: true for seizures, severe withdrawal and DT, but carbamazepine is an evidence-based alternative to benzodiazepines in mild–moderate outpatient withdrawal (Australian alcohol guidelines, grade A). Card d frames Rosenson 2013 under ‘benzodiazepine-refractory’; the trial was a single up-front ED dose added to lorazepam, not refractory patients. Explanation corrects both.",
}
