# GI01B — Explain v3 ("Learn" depth): acute liver failure II — cerebral oedema (numbers, mechanism, grading, clinical signs, ICP monitoring, non-invasive markers), lowering ICP
# (general measures, osmotherapy, hypothermia and hyperventilation, ammonia, seizures and rescue), infection and organ support (frequency, West vs India, circulation/kidney/bleeding/glucose, NAC),
# and anti-tubercular drug liver injury (AIIMS series, stop and restart rules). No mnemonics or hooks. No Top-up cards for this deck.
# Driven by the real questions in qpack/GI01B.md (11 questions, all DocT GT: ALF-31 ATT hepatotoxicity 3, ALF-21 general ICP measures 2; ALF-16, -20, -26, -27, -28, -29 one each;
# ALF-15, -17, -18, -19, -22, -23, -24, -25, -30 none). Fields as TOX01, plus SPINE, PRIMER and step. Table cards take parts a, b, c… in the order of the card’s rows or columns.
# Card layer (gi_cardlayer.json) lines for ALF-26, -28 and -31 and the GT6 Crossfire note are covered in the text; the ALF-28 fix (vasopressin allowed) is already in the card.
# Figures checked online on 20 Nov 2026:
#  - EASL CPG on acute (fulminant) liver failure 2017 (full text, easl.eu): invasive ICP monitoring only in a highly selected subgroup (grade 3–4, ventilated, high risk: young hyperacute/acute,
#    ammonia ~150–200 not falling, renal impairment, vasopressor >0.1 µg/kg/min); ICP does not appear to change outcome; persistent ammonia >200 µmol/L = high risk; ICP <20–25, CPP >50 mmHg;
#    hypertonic saline bolus 200 mL 2.7% or 20 mL 30%; mannitol 150 mL 20% over 20 min; osmolality <320; sodium 140–150 (avoid >150 in the fluid section), correction ≤10 mmol/L/24 h;
#    PaCO2 4.5–5.5 kPa routinely, hyperventilation to 25–30 mmHg only briefly in resistant cases, with jugular saturation monitoring; mild hypothermia may be considered for uncontrolled ICH;
#    indomethacin 0.5 mg/kg only with hyperaemia; steroids not recommended; prophylactic antiepileptics not warranted, levetiracetam preferred over phenytoin when needed;
#    jugular bulb >80% hyperaemia, <55% ischaemia; TCD useful; infection 60–80% (pneumonia 50%, UTI 22%, line 12%, bacteraemia 16%), fungal about one third; prophylactic antibiotics/antifungals
#    no survival benefit; surveillance cultures; noradrenaline first, vasopressin 1–2 U/h if NA >0.2–0.3 µg/kg/min (caution: cerebral effects); hydrocortisone lowers vasopressor dose, not mortality;
#    continuous RRT preferred; no routine FFP; hypoglycaemia common; no evidence for lactulose or rifaximin; high-volume plasma exchange improves transplant-free survival (evidence I).
#  - SCCM ALF/ACLF ICU guideline Part II (Crit Care Med 2023): suggests against invasive ICP monitoring; suggests hypertonic saline when at risk (ammonia >150, high-grade HE, multiorgan failure);
#    against routine hypothermia <34 °C; plasma exchange for ammonia >150; no recommendation on lactulose, rifaximin, LOLA, carnitine, probiotics.
#  - ACG 2023 ALF guideline (Shingina, Am J Gastroenterol; Healio summary): noradrenaline first, add vasopressin if no response; no routine prophylactic antimicrobials (no fall in bacteraemia
#    or 21-day mortality); no routine correction of coagulopathy without bleeding or a high-risk procedure; IV NAC suggested in non-paracetamol ALF; CRRT for grade ≥2 HE.
#  - Canalese, Gut 1982: 44 patients, mannitol 1 g/kg for ICP >30; survival with cerebral oedema 47.1% (8/17) vs 5.9% (1/17); dexamethasone no effect; mannitol weaker in renal failure.
#  - Murphy, Hepatology 2004: 30 patients grade III–IV, 30% saline to sodium 145–155; ICP fell and intracranial hypertension was less frequent.
#  - Bhatia, Gut 2006: 80 patients; arterial ammonia ≥124 µmol/L sensitivity 78.6%, specificity 76.3% for death; median 105 vs 175 in survivors vs non-survivors.
#  - Kumar, Clin Gastroenterol Hepatol 2012: 295 patients; persistent ammonia ≥122 for 3 days: survival 23% vs 72%, cerebral oedema 71% vs 37%, infection 67% vs 28%, seizures 41% vs 7.7%.
#  - Acharya, Gastroenterology 2009: 201 patients, LOLA 30 g/day x 3 days; ammonia fell equally in both arms; mortality 42.4% vs 33.3% (NS).
#  - Bhatia, J Hepatol 2004: 42 patients, prophylactic phenytoin; no difference in cerebral oedema, seizures, ventilation or survival.
#  - Lee, Gastroenterology 2009: 173 non-paracetamol ALF; transplant-free survival 40% vs 27% overall, 52% vs 30% in coma grade I–II, 9% vs 22% in III–IV; 72-hour infusion.
#  - Kumar, Hepatology 2010 (AIIMS): 1,223 ALF, ATT-ALF 70 (5.7%), mortality 67.1%, 70% women, median icterus–encephalopathy 4.5 days, 62.8% empirical ATT, 15 (1.2%) with concurrent viral hepatitis.
#  - Sharma, Clin Infect Dis 2010: about 175 analysed, three reintroduction schedules; recurrence 13.8%, 10.2%, 8.6% (19 in all, p=0.69); simultaneous full-dose reintroduction supported.
# Reviewer check (20 Nov 2026): Vaquero, Liver Transpl 2005 (ALFSG, 332 patients, 92 monitored; complication survey of 58: intracranial haemorrhage 10.3%, about half incidental, contributed to 2 deaths);
#  Karvellas, Crit Care Med 2014 (ALFSG, 140 monitored vs 489 not: no effect on 21-day mortality in paracetamol ALF, higher mortality in non-paracetamol ALF, OR about 3; haemorrhage 4 of 56, 7%);
#  EASL 2017 full text: “at present, the most frequent causes of death in patients with ALF are MOF and severe sepsis”; platelets before line insertion if under 30,000, for active bleeding
#  platelets above 60,000 and fibrinogen 1.5–2 g/L; MAP about 60 adequate in the young; levetiracetam or lacosamide now used more than phenytoin; Acharya, J Gastroenterol Hepatol 2000 (AIIMS):
#  cerebral oedema at admission 245/423 (58%), deaths 82% with vs 44% without, two-thirds of deaths within 72 h, sepsis 65/125 (52%, positive culture or clinical sepsis), Gram-negative 43% of
#  culture-positive, Aspergillus 6/24 (25%) of blood-culture positive, UK series more than two-thirds Gram-positive; AASLD 2011: hypertonic saline to sodium 145–155 when ammonia >150, grade 3–4,
#  renal failure or vasopressors, CPP 60–80; ATS 2006 (Saukkonen): stop at ALT >5× ULN, or >3× with jaundice and/or symptoms; restart when ALT <2×; rifampicin ± ethambutol, isoniazid after 3–7 days;
#  ACG 2023 slides (Shingina): no conclusive evidence for routine ICP monitoring or hypothermia; Acharya 2009 LOLA (mortality 42.4% vs 33.3%, p=0.20); Sharma 2010 (19/175 recurrences, p=0.69).
# Not traced: the 25% bedside detection (ALF-18), mannitol paradoxical rise 20% (ALF-22), ACG 2023 sodium wording (145–150, ceiling 160; full text not reachable), the ALF-27 outcome rows,
#  hypoglycaemia 40% (ALF-28), 80% mortality with viral superinfection and 10% pregnant (ALF-30).

SPINE = [
  ("The swelling brain kills first", "In acute liver failure ammonia is turned into glutamine inside astrocytes, which swell, and lost autoregulation then floods the brain with blood, so cerebral oedema is the leading cause of death in the first days."),
  ("Grading coma and spotting raised ICP", "Encephalopathy is graded 1 to 4, raised ICP is suspected from posturing or Cushing-type signs and arterial ammonia, and invasive monitoring is now kept for a few selected patients because it bleeds and has not improved survival."),
  ("Lowering ICP in steps", "Head up and neck straight, normal sodium, glucose and CO2, then hypertonic saline or mannitol, then brief hyperventilation or cooling as a bridge, while ammonia is lowered mainly by early continuous RRT."),
  ("Infection, the second killer", "Up to 80% become infected, often without fever, so surveillance cultures and immediate broad empirical cover when the patient worsens matter more than prophylaxis."),
  ("Support the other organs, give NAC", "The circulation is vasodilated, so noradrenaline then vasopressin or hydrocortisone, continuous RRT, no prophylactic plasma for the INR, dextrose for hypoglycaemia, and NAC for every patient in early coma."),
  ("Anti-TB drugs as the cause", "In India anti-tubercular drugs cause about 6% of acute liver failure with two-thirds mortality, so drugs are stopped at the ALT thresholds and reintroduced one at a time once ALT falls below twice normal."),
]

PRIMER = "Acute liver failure is jaundice, coagulopathy (INR 1.5 or more) and encephalopathy in a patient without known liver disease; the shorter the interval from jaundice to encephalopathy, the more the brain swells. The skull is a fixed box, so once the swelling brain uses up its spare volume a small further rise in volume causes a steep rise in intracranial pressure. Cerebral perfusion pressure is mean arterial pressure minus ICP, so a low blood pressure and a high ICP both starve the brain. The liver normally clears ammonia, makes clotting factors and glucose, and filters gut bacteria, which is why this deck moves from brain to infection to bleeding and glucose."

L = {}

L['ALF-15'] = dict(
  sub="GI → Acute liver failure → Intracranial hypertension: the numbers",
  step=1,
  intro="Step 1 starts with why the brain matters most in acute liver failure. This card gives the size of the problem: raised ICP kills more patients than anything else, and it kills early. No real question is linked, so this is short.",
  parts=[
    ('a', "**The commonest cause of death.** Brain herniation from cerebral oedema leads the causes of death, with infection and multiorgan failure close behind (watch line). These figures come from the AIIMS series (Acharya 2000), where oedema was present at admission in 58% and sepsis caused 24–49% of deaths. In Western units better ICU care has made oedema much less frequent, and EASL 2017 now states that the most frequent causes of death are multiorgan failure and severe sepsis; for an Indian exam stem, oedema remains the expected answer."),
    ('b', "**82% with overt cerebral oedema vs 44% without.** Overt oedema nearly doubles mortality, which is why grade 3–4 coma triggers the ICP measures in ALF-21 to ALF-25."),
    ('c', "**58%.** In the AIIMS series 245 of 423 patients already had overt oedema when they arrived, because many present late and hyperacute."),
    ('d', "**Two-thirds of deaths occur in the first 72 hours.** That is the window for transplant listing and for brain protection; patients who survive it more often die later of sepsis."),
  ],
  mimic=[
    ("Early vs late death in ALF", "Early (first 3 days): cerebral oedema and herniation. Later: sepsis and multiorgan failure."),
  ],
  traps=[
    ("“Bleeding is the commonest cause of death”", "The INR is high but haemostasis is rebalanced (ALF-28); serious bleeding is uncommon. Cerebral oedema and infection are the killers."),
  ],
  decode=[
    ("[pattern] Commonest cause of death in acute liver failure", "Cerebral oedema with intracranial hypertension; infection is the second."),
    ("[pattern] When do most ALF deaths occur?", "Within the first 72 hours."),
  ],
  punch="Cerebral oedema is the commonest killer in acute liver failure, nearly doubles mortality (82% vs 44%) and acts early, with two-thirds of deaths in the first 72 hours.",
)

L['ALF-16'] = dict(
  sub="GI → Acute liver failure → Why the brain swells",
  step=1,
  intro="Step 1 continues with the mechanism. The swelling has two parts: astrocytes swell because they turn ammonia into glutamine, and inflammation removes autoregulation so blood floods the brain. The one linked question tests the cytotoxic versus vasogenic distinction using a different disease, a brain abscess.",
  parts=[
    ('a', "**Cytotoxic: ammonia enters astrocytes, is converted to glutamine (osmotically active), and the astrocyte swells.** The liver normally clears ammonia through the urea cycle. When it fails, the brain detoxifies ammonia by joining it to glutamate to make glutamine, and only astrocytes carry glutamine synthetase (watch line). Glutamine builds up inside the cell, draws water in and damages mitochondria. The blood–brain barrier stays largely intact, which is why steroids do not help (dexamethasone failed in the Canalese trial)."),
    ('b', "**Vasogenic: systemic nitric oxide, endotoxin, TNF, IL-1 and IL-6 cause loss of cerebral autoregulation and hyperaemia.** Normally cerebral vessels hold flow steady across a range of pressures. In ALF this is lost, so cerebral blood flow follows arterial pressure and rises; the extra blood volume in a stiff, swollen brain raises ICP. This is the reason hypertension, hypercapnia and fever all push ICP up."),
    ('c', "**Other toxins: aromatic amino acids, mercaptans, glutamate, GABA, benzodiazepine-like substances, fatty acids.** These add to encephalopathy and may explain why flumazenil helps briefly in some patients, but ammonia is the one that tracks oedema (ALF-24)."),
    ('d', "**Aggravators: hypoglycaemia, hyponatraemia, hypercarbia, hyper- or hypotension, sedatives.** Low sodium moves water into cells; high CO2 dilates cerebral vessels; low glucose injures neurons; swings in pressure act on a brain that cannot autoregulate. Correcting these is the first step of treatment (ALF-21)."),
  ],
  mimic=[
    ("Cytotoxic vs vasogenic oedema", "Cytotoxic: cell swelling, barrier intact, grey and white matter, no steroid response (ischaemic stroke, ALF astrocytes). Vasogenic: barrier breaks, protein-rich fluid in white matter, responds to steroids (tumour, abscess)."),
    ("ALF oedema vs cirrhotic encephalopathy", "Both have high ammonia, but in cirrhosis astrocytes adapt slowly (they shed osmolytes), so overt oedema and raised ICP are rare."),
  ],
  traps=[
    ("“The oedema around a brain abscess is cytotoxic”", "It is vasogenic: the barrier around the abscess breaks down and fluid leaks into white matter. That is why it responds to dexamethasone [DocT GT]."),
    ("“Steroids reduce cerebral oedema in ALF”", "ALF oedema is mainly cytotoxic; dexamethasone had no effect on ICP or survival (Canalese 1982), and EASL does not recommend steroids for it."),
  ],
  decode=[
    ("The oedema surrounding a brain abscess is predominantly — cytotoxic, vasogenic, interstitial, osmotic? [DocT GT]", "Vasogenic. Interstitial oedema is hydrocephalus (CSF crossing the ventricular wall); cytotoxic is ischaemia and ALF."),
    ("[pattern] Which brain cell swells in ALF, and why?", "The astrocyte, because it alone has glutamine synthetase and so accumulates glutamine."),
  ],
  punch="ALF brain swelling is mainly cytotoxic: ammonia becomes glutamine inside astrocytes, which swell, while lost autoregulation adds hyperaemia; an abscess or tumour gives vasogenic oedema instead.",
)

L['ALF-17'] = dict(
  sub="GI → Acute liver failure → Grading encephalopathy",
  step=2,
  intro="Step 2 begins with grading, because the grade decides intubation, ICP measures and the transplant criteria. No real question is linked, so this is short.",
  parts=[
    ('a', "**Grade 1: lost sleep rhythm, drowsy, confused, flapping tremor; GCS 15.** Subtle and easily missed; asterixis is the clue."),
    ('b', "**Grade 2: grade 1 plus loss of sphincter control; GCS 11–14.** In West Haven wording grade 2 is lethargy, disorientation to time and inappropriate behaviour, with asterixis; the card’s Riegler and Lake column adds incontinence."),
    ('c', "**Grade 3: unconscious, no response to voice, responds to pain; GCS 8–10.** The airway is now at risk and ICP rises; this is the grade at which to intubate (watch line)."),
    ('d', "**Grade 4: deep coma, no response to pain; GCS under 8.** Highest risk of intracranial hypertension. Grades 3–4 are the encephalopathy grades in the King’s College and Clichy criteria."),
  ],
  mimic=[
    ("Grade 2 vs grade 3", "Grade 2 still responds to voice; grade 3 responds only to pain and needs a secured airway."),
  ],
  traps=[
    ("“Grade 2 is the point to intubate”", "Intubation is for grade 3–4, when the airway and CO2 can no longer be trusted."),
  ],
  decode=[
    ("[pattern] ALF patient responds only to pain — grade and next step", "Grade 3: intubate, start ICP measures, contact a transplant centre."),
  ],
  punch="Grades 1–2 still talk; grade 3 responds only to pain and grade 4 to nothing, and grades 3–4 mean intubation and are the grades in the King’s and Clichy criteria.",
)

L['ALF-18'] = dict(
  sub="GI → Acute liver failure → Clinical diagnosis of raised ICP",
  step=2,
  intro="Step 2 continues with how raised ICP shows at the bedside when there is no monitor. No real question is linked, so this is short.",
  parts=[
    ('a', "**Decerebrate posturing, spontaneous or inducible.** Extensor posturing means the brainstem is being compressed; it alone is enough for the diagnosis."),
    ('b', "**Or any two of: hypertension above 150/90 mmHg, bradycardia, pupillary changes, neurogenic hyperventilation.** Hypertension and bradycardia are the Cushing response: the brainstem raises arterial pressure to keep perfusion against a rising ICP, and the baroreflex slows the heart. Pupillary change means uncal herniation is near. These are late signs; the watch line notes that bedside examination catches only a minority of the surges a monitor shows (the 25% figure is unclear in the source and could not be traced)."),
  ],
  mimic=[
    ("Cushing response vs sepsis", "Raised ICP: hypertension with bradycardia. Sepsis: hypotension with tachycardia. ALF patients usually run a low pressure, so new hypertension is a warning."),
  ],
  traps=[
    ("“A normal examination excludes raised ICP”", "The signs appear late and miss most surges, which is why ammonia, Doppler and optic nerve sheath are used (ALF-20)."),
  ],
  decode=[
    ("[pattern] Grade 4 ALF with BP 170/100, HR 50 and a sluggish pupil", "Clinical intracranial hypertension: treat now with hypertonic saline or mannitol (ALF-22)."),
  ],
  punch="Raised ICP is diagnosed clinically by decerebrate posturing or any two of hypertension over 150/90, bradycardia, pupil change and neurogenic hyperventilation, but these signs are late and miss most surges.",
)

L['ALF-19'] = dict(
  sub="GI → Acute liver failure → Invasive ICP monitoring",
  step=2,
  intro="Step 2 then asks whether to put a bolt in. The answer has moved from routine use to a small selected group, because monitoring bleeds and has not improved survival. No real question is linked, so this is short.",
  parts=[
    ('a', "**The case against: survival in grade III–IV is not improved; no long-term neurological data; intracranial bleeding in 10.3%.** The bleeding figure is from the US ALFSG survey (Vaquero 2005): 10.3% of 58 monitored patients bled, about half of them incidental findings on a scan, and bleeding contributed to 2 deaths; a later ALFSG cohort (Karvellas 2014) found 7%. The INR is high and the platelet count low, and a bleed into a swollen brain can be fatal. In that later cohort monitoring did not change 21-day mortality in paracetamol ALF and was linked to higher mortality in non-paracetamol ALF, and EASL notes that it does not appear to change outcome."),
    ('b', "**When to consider it: pressor-dependent with renal failure; rapidly evolving encephalopathy; arterial ammonia above 150 µmol/L; pupillary abnormalities; jugular bulb saturation outside 55–80%.** These are the patients most likely to have intracranial hypertension. EASL 2017 keeps monitoring for a highly selected group: grade 3–4, ventilated, and more than one of young age with hyperacute or acute disease, ammonia about 150–200 that does not fall with treatment, renal impairment, or noradrenaline above 0.1 µg/kg/min. SCCM 2023 suggests against invasive monitoring, and ACG 2023 finds no conclusive evidence for routine monitor placement (watch line)."),
  ],
  mimic=[
    ("Invasive monitoring vs non-invasive markers", "Bolt: direct pressure, bleeding risk. Ammonia, TCD, ONSD, jugular bulb: no bleeding, used to pick out who might need the bolt (ALF-20)."),
  ],
  traps=[
    ("“All grade 4 ALF patients should have an ICP monitor”", "No: routine monitoring is not recommended (SCCM 2023 against; EASL only in selected patients)."),
  ],
  decode=[
    ("[pattern] Main complication of ICP monitoring in ALF", "Intracranial haemorrhage (about 7–10%)."),
    ("[pattern] Grade 4, ammonia 220 not falling, on noradrenaline, creatinine rising — consider a bolt?", "Yes, this is the selected high-risk group, if the centre has expertise."),
  ],
  punch="Invasive ICP monitoring bleeds in up to one in ten and has not improved survival, so it is kept for selected high-risk patients: grade 3–4 with ammonia over 150 that is not falling, renal failure or pressor dependence.",
)

L['ALF-20'] = dict(
  sub="GI → Acute liver failure → Non-invasive markers of raised ICP",
  step=2,
  intro="Step 2 ends with the middle path between examination and a bolt: tests that estimate ICP or cerebral flow without a hole in the skull. The linked question asks which measurement cannot estimate ICP.",
  parts=[
    ('a', "**Arterial ammonia: above 124 µmol/L (Bhatia, Gut 2006); above 150 µmol/L (Clemmesen, Hepatology 1999).** Arterial ammonia tracks the glutamine load in astrocytes (ALF-16). Above 150 the risk of herniation rises, and EASL calls ammonia persistently above 200 after initial treatment high risk. Venous samples are less reliable; take arterial blood on ice and run it quickly."),
    ('b', "**Jugular bulb oxygen saturation.** Blood from the jugular bulb is the brain’s venous outflow. Above 80% means flow exceeds need (hyperaemia, which hyperventilation or indomethacin can treat); below 55% means relative ischaemia (lower ICP, raise CPP, stop hyperventilating)."),
    ('c', "**Cerebral arteriovenous oxygen difference.** The same idea from the other side: a narrow difference means hyperaemia, a wide one ischaemia."),
    ('d', "**Transcranial Doppler.** A rising ICP lowers diastolic flow in the middle cerebral artery and raises the pulsatility index; EASL rates TCD a useful non-invasive tool, and a rise in flow often comes before a rise in ICP."),
    ('e', "**Optic nerve sheath diameter.** The sheath is continuous with the subarachnoid space, so raised CSF pressure distends it; around 5–6 mm in adults is the usual alarm range on ultrasound."),
  ],
  mimic=[
    ("ICP estimates vs central venous pressure", "ONSD, TCD and the jugular bulb reflect the brain; CVP reflects right atrial pressure and tells nothing about ICP."),
  ],
  traps=[
    ("“CVP can be used to estimate ICP”", "It cannot; CVP is a right-heart pressure. A very high CVP can impede cerebral venous outflow, but it does not measure ICP [DocT GT]."),
    ("“Ventriculostomy cannot assess ICP”", "It is the gold standard: an external ventricular drain measures ICP directly and lets CSF out."),
  ],
  decode=[
    ("Which of the following cannot be used to assess or estimate ICP — CVP, ONSD, TCD, ventriculostomy? [DocT GT]", "CVP."),
    ("[pattern] Arterial ammonia threshold for cerebral oedema risk in ALF", "Above 150 µmol/L (Clemmesen); 124 in the Indian series (Bhatia)."),
  ],
  punch="Arterial ammonia, jugular bulb saturation, transcranial Doppler and optic nerve sheath diameter estimate ICP without a bolt; CVP does not.",
)

L['ALF-21'] = dict(
  sub="GI → Acute liver failure → General measures for raised ICP",
  step=3,
  intro="Step 3 is lowering ICP, and it starts with measures that cost nothing: help venous blood leave the head and remove anything that adds blood, water or metabolic demand to the brain. Two linked questions test neck position and ventilation during transfer.",
  parts=[
    ('a', "**Head up 20–30 degrees, neck neutral.** Raising the head lowers jugular venous pressure and helps CSF drain into the spinal space. A neutral neck keeps the jugular veins open; flexion or rotation kinks them, venous blood backs up and ICP rises. Tight tube ties do the same."),
    ('b', "**Avoid tactile stimulation, head turning, hypercapnia, hypo- or hyperglycaemia, hyponatraemia, fever, shivering.** Each raises cerebral blood volume or water: CO2 dilates cerebral vessels (and in ALF autoregulation is already lost), low sodium moves water into cells, fever and shivering raise metabolic demand and so flow. Suctioning and turning cause surges, so sedate before them. The routine target is normocapnia, PaCO2 about 34–41 mmHg (EASL); hypoventilation during transfers or procedures is a common, avoidable cause of a surge."),
    ('c', "**Treatable causes of agitation: distended bladder, bed sores.** Pain and a full bladder raise blood pressure and ICP in a patient who cannot say so; check them before adding sedation."),
  ],
  mimic=[
    ("Neck flexion vs head elevation", "Head-up 30° lowers ICP; neck flexion raises it by blocking jugular outflow."),
    ("Normocapnia vs hyperventilation", "Normocapnia is the routine target; hyperventilation is a brief rescue for a surge (ALF-23)."),
  ],
  traps=[
    ("“Mild hypothermia or head elevation raises ICP the most”", "Both lower ICP. Hyperventilation lowers it too. Neck flexion raises it [DocT GT]."),
    ("“Permissive hypercapnia, or PaCO2 above 50”", "Lung-protective permissive hypercapnia is wrong here: CO2 dilates cerebral vessels and raises ICP. Keep CO2 normal and avoid hypoventilation, especially during transfers [DocT GT]."),
    ("“Induce prolonged hyperventilation”", "Prolonged hypocapnia causes cerebral vasoconstriction and ischaemia and has no prophylactic benefit (ALF-23)."),
  ],
  decode=[
    ("Which increases ICP the most — hyperventilation, neck flexion, head-up 30°, mild hypothermia? [DocT GT]", "Neck flexion: it obstructs jugular venous outflow."),
    ("ALF, grade III, intubated — key ventilation strategy? [DocT GT]", "Avoid hypoventilation during transfers: keep PaCO2 normal."),
  ],
  punch="Head up 20–30°, neck straight, and normal CO2, sodium, glucose and temperature; neck flexion and hypoventilation are the classic ways to push ICP up.",
)

L['ALF-22'] = dict(
  sub="GI → Acute liver failure → Mannitol vs hypertonic saline",
  step=3,
  intro="Step 3 continues with osmotherapy. Both drugs draw water out of the brain across an intact blood–brain barrier, which works because ALF oedema is mainly cytotoxic. No real question is linked, so this is short.",
  parts=[
    ('a', "**Dose: mannitol bolus 0.5–1 g/kg; hypertonic saline 23.4% 30 mL or 7.5% 2 mL/kg, repeat every 2–3 h, or 3% infusion at 5–20 mL/h.** EASL gives mannitol as 150 mL of 20% over 20 minutes and hypertonic saline as 200 mL of 2.7% or 20 mL of 30%. Concentrated saline needs a central line."),
    ('b', "**Response: 15–60 min after a mannitol bolus.** Mannitol stays in the vessels, raises plasma osmolality and pulls water from brain tissue; it also lowers blood viscosity, so vessels constrict and blood volume falls."),
    ('c', "**Target: osmolality under 320 for mannitol; sodium 145–155 mmol/L for hypertonic saline.** Above 320 mannitol injures the kidney. The 145–155 target is from the Murphy 2004 trial (30% saline in grade III–IV: ICP fell and intracranial hypertension was less frequent, without a survival difference), and AASLD 2011 adopted it for patients at highest risk (ammonia over 150, grade 3–4 coma, renal failure or vasopressors). SCCM 2023 suggests hypertonic saline for patients at risk of intracranial hypertension. EASL’s own range is lower (140–150, correcting by no more than 10 mmol/L a day); the watch line gives ACG 2023 as 145–150 in common practice with a ceiling of 160."),
    ('d', "**Limits: mannitol has a paradoxical ICP rise in 20% and is best in mild to moderate rises; sodium should rise no more than 12 mmol/L in 24 h (18 in 48 h).** Mannitol can leak into damaged brain and carry water back with it, and it is a diuretic that needs working kidneys or RRT to clear it; the Canalese trial found it less effective in renal failure. The sodium limit protects against osmotic injury, a risk if sodium was low at the start."),
    ('e', "**Evidence: mannitol survival 47.1% vs 5.9%.** In Canalese 1982 (44 patients), mannitol 1 g/kg for ICP over 30 mmHg reversed most episodes and, among patients with cerebral oedema, 8 of 17 survived with mannitol against 1 of 17 without."),
  ],
  mimic=[
    ("Mannitol vs hypertonic saline", "Mannitol: bolus for a surge, needs urine output, watch osmolality. Hypertonic saline: bolus or infusion, also prophylactic, expands volume, watch sodium; preferred in renal failure and hypotension."),
  ],
  traps=[
    ("“Mannitol is the agent of choice in oliguric ALF”", "Mannitol needs renal clearance; in renal failure it accumulates and can raise osmolality without benefit. Use hypertonic saline, or remove the fluid with CRRT."),
  ],
  decode=[
    ("[pattern] Sodium target for prophylactic hypertonic saline in ALF", "145–155 mmol/L (Murphy 2004); keep under 160."),
    ("[pattern] Osmolality limit with mannitol", "Under 320 mOsm/kg."),
  ],
  punch="Mannitol (0.5–1 g/kg, osmolality under 320) reverses surges and improved survival in Canalese (47% vs 6%); hypertonic saline to sodium 145–155 prevents them and suits renal failure better.",
)

L['ALF-23'] = dict(
  sub="GI → Acute liver failure → Hypothermia and hyperventilation",
  step=3,
  intro="Step 3 moves to rescue measures for ICP that osmotherapy has not controlled. Both work by reducing cerebral blood flow, and both are bridges, not treatments. No real question is linked, so this is short.",
  parts=[
    ('a', "**Target temperature 32–35 °C, by external cooling blankets.** EASL says mild hypothermia may be considered; SCCM 2023 suggests against routine moderate hypothermia below 34 °C."),
    ('b', "**Reserved for uncontrolled intracranial hypertension (a bridge to transplant).** A trial of prophylactic cooling to 34 °C (Bernal 2016) found no fall in intracranial hypertension, and ACG 2023 finds no conclusive evidence for routine cooling, so it is not used routinely."),
    ('c', "**Normalises cerebral blood flow; lowers brain ammonia uptake, anaerobic glycolysis and extracellular glutamate.** Cooling lowers cerebral metabolism, and flow falls with it; less ammonia enters the brain and less glutamine is made."),
    ('d', "**Risks: shivering (needs paralysis), infection, low platelets, pancreatitis, arrhythmia.** Cold also worsens coagulopathy, which matters in a patient who may need a line or a bolt."),
    ('e', "**Hyperventilation: prophylactic, no benefit; PaCO2 25–30 mmHg lowers ICP once oedema develops; excess causes vasoconstriction.** Low CO2 constricts cerebral vessels and cuts blood volume within minutes, but the effect fades as CSF bicarbonate adjusts, and too much vasoconstriction causes ischaemia. EASL uses it only briefly in resistant cases, with jugular bulb saturation monitored to catch ischaemia (below 55%, ALF-20)."),
  ],
  mimic=[
    ("Hyperventilation vs osmotherapy", "Hyperventilation lowers blood volume quickly and briefly; osmotherapy removes brain water and lasts longer."),
  ],
  traps=[
    ("“Prophylactic hyperventilation prevents cerebral oedema”", "It does not, and prolonged hypocapnia risks ischaemia; keep CO2 normal (ALF-21)."),
  ],
  decode=[
    ("[pattern] Role of hypothermia in ALF", "32–35 °C only for ICP not controlled by osmotherapy, as a bridge to transplant; not prophylactic."),
    ("[pattern] PaCO2 target for rescue hyperventilation", "25–30 mmHg, briefly, with jugular bulb monitoring."),
  ],
  punch="Cooling to 32–35 °C and brief hyperventilation to PaCO2 25–30 lower ICP by cutting cerebral blood flow, but both are rescue bridges for uncontrolled ICP, not prophylaxis.",
)

L['ALF-24'] = dict(
  sub="GI → Acute liver failure → Ammonia",
  step=3,
  intro="Step 3 continues with the cause behind the swelling. Ammonia predicts who will swell and who will die, and its fall over three days predicts survival, but the drugs that lower it in cirrhosis do little here. No real question is linked, so this is short.",
  parts=[
    ('a', "**Arterial ammonia above 124 µmol/L: sensitivity 78.6%, specificity 76.3% for death.** From 80 Indian patients (Bhatia, Gut 2006); non-survivors had a median of about 175 against 105 in survivors."),
    ('b', "**A high admission level predicts more cerebral oedema, grade 3–4 encephalopathy, seizures, infection, renal failure and ventilation.** Ammonia is both a marker of how little liver is working and a direct brain toxin (ALF-16)."),
    ('c', "**Kinetics: under 85 lowest risk; 85–121 low, or intermediate if still 85 or more at 3 days; 122 or more persisting for 3 days is high risk (transplant).** In 295 patients (Kumar 2012), ammonia of 122 or more for three days meant survival of 23% against 72% when it fell, with more oedema (71% vs 37%), infection (67% vs 28%) and seizures (41% vs 8%). Infection and renal failure kept ammonia high, which is another reason to treat both early."),
    ('d', "**Anti-ammonia measures: lactulose, rifaximin, L-ornithine L-aspartate, L-ornithine phenylacetate, levocarnitine, probiotics.** None has outcome evidence in ALF; EASL finds no evidence for lactulose or rifaximin, and SCCM 2023 makes no recommendation for any of them. Lactulose also distends the bowel, which matters if transplant surgery follows. What lowers ammonia is early continuous RRT and, per SCCM 2023, plasma exchange for ammonia above 150 (watch line)."),
    ('e', "**LOLA works in cirrhosis; in ALF it neither lowers ammonia nor improves survival.** In the AIIMS trial (201 patients, 30 g/day for 3 days) ammonia fell equally in both arms and mortality was 42% with LOLA against 33% with placebo (not significant). The ornithine needs working liver to drive ammonia into urea and glutamine."),
  ],
  mimic=[
    ("Ammonia in ALF vs cirrhosis", "ALF: the level predicts oedema and death, and RRT or plasma exchange lowers it. Cirrhosis: the level correlates poorly with encephalopathy, and lactulose, rifaximin and LOLA help."),
  ],
  traps=[
    ("“Lactulose is standard therapy for ALF encephalopathy”", "It is not supported by evidence in ALF and can distend the bowel; it is the cirrhosis treatment."),
  ],
  decode=[
    ("[pattern] Best way to lower ammonia in ALF", "Early continuous RRT (or plasma exchange), not lactulose or LOLA."),
    ("[pattern] Ammonia 140 at admission and still 130 on day 3", "Persistent hyperammonaemia: high risk, list for transplant."),
  ],
  punch="Arterial ammonia above about 124–150 predicts oedema and death, and a level of 122 or more that persists for 3 days means transplant; it is lowered by CRRT or plasma exchange, not by lactulose or LOLA.",
)

L['ALF-25'] = dict(
  sub="GI → Acute liver failure → Seizures and rescue measures",
  step=3,
  intro="Step 3 closes with seizures and last-line options. Seizures in a comatose ALF patient are usually silent, and each one raises cerebral metabolism and ICP. No real question is linked, so this is short.",
  parts=[
    ('a', "**Subclinical seizures worsen cerebral oedema.** A seizure raises cerebral oxygen use and blood flow, so ICP climbs; in a paralysed, sedated patient only EEG shows it. EASL advises EEG when seizures are suspected."),
    ('b', "**Prophylactic phenytoin: a randomised trial of 42 patients showed no benefit.** In the AIIMS trial (Bhatia 2004) phenytoin did not reduce cerebral oedema, seizures, ventilation or death. EASL now says prophylactic antiepileptics are not warranted; phenytoin was the traditional choice for proven seizures, but levetiracetam or lacosamide are now used more, as they carry little hepatotoxic risk. The watch line notes that the notes also print the opposite advice; the trial is the exam answer."),
    ('c', "**Other measures for refractory ICP: hypertonic saline, ultrafiltration, plasmapheresis, barbiturates.** Ultrafiltration removes water and ammonia; high-volume plasma exchange (Larsen 2016) improved transplant-free survival and lowers ammonia; thiopental lowers cerebral metabolism but drops blood pressure and so CPP. EASL adds indomethacin 0.5 mg/kg only when flow is hyperaemic."),
  ],
  mimic=[
    ("Prophylaxis vs treatment of seizures", "Prophylaxis: no benefit. Proven or EEG seizures: treat (levetiracetam preferred), and use propofol for sedation, which is also anticonvulsant."),
  ],
  traps=[
    ("“All deep-coma ALF patients need prophylactic phenytoin”", "The 42-patient trial was negative and EASL does not recommend prophylaxis."),
  ],
  decode=[
    ("[pattern] Role of prophylactic phenytoin in ALF", "None: no effect on oedema, seizures or survival."),
  ],
  punch="Silent seizures raise ICP and should be sought on EEG and treated, but prophylactic phenytoin failed in its trial; refractory ICP is managed with osmotherapy, CRRT, plasma exchange and barbiturates.",
)

L['ALF-26'] = dict(
  sub="GI → Acute liver failure → Infection",
  step=4,
  intro="Step 4 is the second killer. The failed liver can no longer clear bacteria from portal blood and makes too little complement, so infection is very common, often silent, and it worsens the brain. One linked question tests what to do when a patient on day 5 shows signs of pneumonia.",
  parts=[
    ('a', "**Up to 80%.** EASL gives bacterial infection in 60–80% and fungal infection in about a third of those needing prolonged critical care, mostly Candida. The reasons are in the watch line: low complement and fibronectin, poor neutrophil chemotaxis and opsonisation, failed reticulo-endothelial (Kupffer cell) clearance, plus tubes and lines."),
    ('b', "**Pneumonia is the commonest site.** About half of infections (EASL), then urinary tract, spontaneous bacteraemia and line infections. Coma, aspiration and ventilation explain the lungs."),
    ('c', "**The diagnostic problem: fever and leucocytosis may be absent, so daily surveillance cultures.** The usual inflammatory response is blunted, so infection may show only as worsening encephalopathy, rising pressor need or SIRS. EASL recommends regular surveillance cultures and early anti-infective treatment when coma deepens, infection signs appear or SIRS develops."),
    ('d', "**Criteria in the notes: temperature above 101 °F or below 98 °F, count above 15,000 with over 80% polymorphs, plus a positive blood or urine culture or pneumonitis on X-ray.** These are old research criteria; at the bedside a lower threshold to treat applies because the signs are blunted."),
    ('e', "**Prophylactic antibiotics: fewer infections, no survival benefit.** EASL and ACG 2023 do not recommend routine prophylaxis (ACG: no fall in bacteraemia or 21-day mortality). Empirical cover is advised for patients listed for transplant, when encephalopathy worsens, or with SIRS. Once infection is suspected, start an extended-spectrum beta-lactam (piperacillin-tazobactam or a carbapenem, by local Gram-negative ecology) after cultures, without waiting for results; add antifungals only for deterioration despite antibiotics or a long ICU course (card layer)."),
  ],
  mimic=[
    ("Prophylaxis vs empirical treatment", "Prophylaxis in a stable patient: no survival benefit. Empirical broad cover when the patient worsens or shows SIRS: recommended and urgent."),
  ],
  traps=[
    ("“Hold antibiotics until cultures return”", "Never: these patients die of delay. Take cultures and start an extended-spectrum beta-lactam at once [DocT GT]."),
    ("“Narrow-spectrum penicillin”", "It misses the Gram-negatives (and Staph. aureus) that cause most ALF infections; the cover must be broad."),
    ("“High-dose amphotericin first”", "Fungal infection comes later, after long antibiotic courses; antifungals are added for deterioration despite antibiotics, not as first-line."),
  ],
  decode=[
    ("ALF day 5 with fever, rising WBC and new infiltrates — best empirical step? [DocT GT]", "Extended-spectrum beta-lactam (piperacillin-tazobactam or a carbapenem)."),
    ("[pattern] Commonest site of infection in ALF", "Pneumonia."),
  ],
  punch="Up to 80% of ALF patients are infected, usually in the chest and often without fever; prophylaxis does not save lives, but surveillance cultures and immediate broad cover with an extended-spectrum beta-lactam when they worsen does.",
)

L['ALF-27'] = dict(
  sub="GI → Acute liver failure → Infection: West vs India, and outcome",
  step=4,
  intro="Step 4 continues with why the antibiotic choice in India differs from Western teaching, and how much infection worsens outcome. The linked question is the same day-5 pneumonia stem as ALF-26; the organism mix in this table is why the answer is a broad Gram-negative beta-lactam.",
  parts=[
    ('a', "**Culture positive: 80% in the West vs 52% in India.** The Western 80% is the King’s surveillance-culture series. The Indian 52% is the AIIMS series (Acharya 2000): 65 of 125 patients had a positive culture or clinical evidence of sepsis, and many lacked overt signs, which is why repeated cultures are needed."),
    ('b', "**Organisms: Gram-positive (Staph. aureus) in the West vs Gram-negative (57%) in India: Acinetobacter, Klebsiella.** The AIIMS review contrasts its Gram-negative and fungal sepsis with a UK series in which more than two-thirds were Gram-positive (in its own count Gram-negatives were 43% of culture-positive patients, so the card’s 57% may be a different series). In Indian ICUs the Gram-negatives are often multidrug-resistant, which is why piperacillin-tazobactam or a carbapenem by local ecology is the empirical choice, with vancomycin added for lines or MRSA risk."),
    ('c', "**Fungal: 32% in the West vs Aspergillus in 23% in India (scan unclear).** The Western 32% is the classic King’s figure, mostly Candida. The Indian figure is marked unclear on the card; the AIIMS series found Aspergillus in 6 of 24 patients with a positive blood culture (25%), so invasive fungal infection appears early there."),
    ('d', "**Outcome without vs with infection: encephalopathy worse or static 9.1% vs 60.3%; seizures 2.3% vs 22.1%; renal failure 4.5% vs 33.8%; mortality 11.4% vs 52.9%.** Infection and its cytokines raise ICP and keep ammonia high (ALF-24), so infection worsens the brain as well as the kidneys; mortality rises about five-fold."),
  ],
  mimic=[
    ("Western vs Indian ALF infection", "West: Gram-positive, Staph. aureus, Candida. India: Gram-negative, Acinetobacter and Klebsiella."),
  ],
  traps=[
    ("“Gram-positive cover alone is enough”", "In Indian ICUs most isolates are Gram-negative, so cover must be broad Gram-negative first [DocT GT]."),
  ],
  decode=[
    ("ALF day 5 with fever, rising WBC and new infiltrates — best empirical step? [DocT GT]", "Extended-spectrum beta-lactam, guided by local Gram-negative ecology."),
    ("[pattern] Predominant organisms in Indian ALF infections", "Gram-negative: Acinetobacter, Klebsiella."),
  ],
  punch="In India ALF infections are mainly Gram-negative (Acinetobacter, Klebsiella), unlike the Staph. aureus of Western series, and infection worsens the brain and raises mortality about five-fold (53% vs 11%).",
)

L['ALF-28'] = dict(
  sub="GI → Acute liver failure → Circulation, kidney, bleeding and glucose",
  step=5,
  intro="Step 5 is supporting every other organ. ALF looks like septic shock: dilated vessels, high cardiac output, constricted kidneys, low glucose and a high INR that does not mean bleeding. The linked question tests what to add when noradrenaline is not enough.",
  parts=[
    ('a', "**Hyperdynamic: peripheral vasodilatation with renal vasoconstriction.** Nitric oxide and cytokines dilate systemic vessels, cardiac output rises and resistance falls, while renal vessels constrict as in hepatorenal physiology. Relative adrenal insufficiency is common and adds to the vasodilatation."),
    ('b', "**Target cerebral perfusion pressure above 60 mmHg, rather than MAP alone.** Because the brain cannot autoregulate, its flow follows CPP (MAP minus ICP). EASL sets CPP above 50 and accepts a MAP of about 60 in a young patient (higher if chronically hypertensive); AASLD 2011 gave MAP 75 or more and CPP 60–80, which is where the card’s 60 comes from. Fluids first with crystalloid, then vasopressors."),
    ('c', "**Second vasopressor: low-dose vasopressin added to noradrenaline if hypotension persists (ACG 2023, SCCM 2020).** EASL suggests vasopressin 1–2 units/h when noradrenaline exceeds about 0.2–0.3 µg/kg/min, with caution because vasopressin and terlipressin may dilate cerebral vessels. For shock still refractory, low-dose hydrocortisone (200 mg/day): it lowers the vasopressor dose without proven survival benefit (EASL; card layer). High-dose steroids and adrenaline boluses are wrong."),
    ('d', "**Continuous, not intermittent renal replacement; avoid nephrotoxins.** Intermittent dialysis drops blood pressure and shifts osmoles fast, which can raise ICP; continuous RRT is steadier and also clears ammonia (ALF-24). ACG 2023 suggests early CRRT to lower ammonia in grade 2 or higher encephalopathy, even without the usual renal indications."),
    ('e', "**Rebalanced haemostasis: correct platelets (under 50,000) or INR only for bleeding or before a procedure; give a PPI.** Pro- and anticoagulant factors fall together, so the high INR overstates bleeding risk; viscoelastic tests are often normal. Plasma given to correct the INR adds volume (and ICP), and hides the INR, which is the prognostic marker the transplant criteria use (watch line). ACG and EASL advise no routine correction without bleeding or a high-risk procedure; EASL gives platelets before line insertion if the count is under 30,000, and for active bleeding aims for platelets above 60,000 and fibrinogen 1.5–2 g/L."),
    ('f', "**Hypoglycaemia in 40%: lost glycogen and gluconeogenesis, high insulin; 10% or 50% dextrose.** The 40% is the card’s figure and could not be traced; EASL simply calls hypoglycaemia common and linked to higher mortality. The liver can no longer release glucose and does not clear insulin. Check glucose every 1–2 hours, run 10% dextrose, give 50% for a low reading, and avoid hyperglycaemia, which worsens ICP. Feeding: hypercatabolic, protein 1–1.5 g/kg/day (watch line)."),
  ],
  mimic=[
    ("ALF shock vs cardiogenic shock", "ALF: warm, high output, low resistance. Cardiogenic: cold, low output, high resistance."),
    ("High INR in ALF vs bleeding risk", "INR reflects lost synthesis and predicts outcome; actual bleeding risk is better judged by platelets, fibrinogen and viscoelastic tests."),
  ],
  traps=[
    ("“High-dose vasopressin” as the next step", "Only low-dose vasopressin (1–2 units/h) is used, as an adjunct; high doses cause ischaemia. Among the options the key is low-dose hydrocortisone [DocT GT]."),
    ("“High-dose corticosteroids” or “adrenaline bolus”", "High-dose steroids raise infection and do not help shock; adrenaline boluses are not the step for vasodilatory shock. Low-dose hydrocortisone is the correct steroid [DocT GT]."),
    ("“Give FFP to bring the INR down”", "Only for bleeding or before a procedure; otherwise it adds volume and hides the prognostic INR."),
  ],
  decode=[
    ("ALF with persistent hypotension despite noradrenaline — next step? [DocT GT]", "Low-dose hydrocortisone (200 mg/day); low-dose vasopressin is the other correct adjunct."),
    ("[pattern] RRT mode in ALF", "Continuous (CRRT), not intermittent."),
    ("[pattern] INR 4, no bleeding, no procedure planned", "Do not correct."),
  ],
  punch="ALF shock is vasodilatory: noradrenaline first, then low-dose vasopressin or low-dose hydrocortisone, with CPP above 50–60; use continuous RRT, keep the INR uncorrected unless bleeding, and give dextrose for the hypoglycaemia.",
)

L['ALF-29'] = dict(
  sub="GI → Acute liver failure → N-acetylcysteine",
  step=5,
  intro="Step 5 continues with the one drug given to nearly everyone with ALF. NAC is the antidote for paracetamol, and it also helps non-paracetamol liver failure in early coma. The linked question gives a young man with very high transaminases and falling consciousness and asks what to start empirically.",
  parts=[
    ('a', "**Oral regimen: 140 mg/kg, then 70 mg/kg every 4 hours for 17 doses.** The old 72-hour oral regimen; it is unreliable in a vomiting or comatose patient, so IV is used in ALF."),
    ('b', "**IV regimen (72-hour): 150 mg/kg over 1 hour; 12.5 mg/kg/h for 4 hours; 6.25 mg/kg/h for 67 hours.** This is the regimen of the US ALFSG trial in non-paracetamol ALF. The 21-hour, 300 mg/kg regimen for paracetamol poisoning is in APAP-09 (watch line)."),
    ('c', "**How it works: antidote under 24 hours, antioxidant after 24 hours; also anti-inflammatory, inotropic, vasodilating.** Early, NAC restores glutathione, which binds the toxic paracetamol metabolite NAPQI. Late, it scavenges free radicals and improves microcirculation and oxygen delivery, which is why it helps even when no paracetamol is left."),
    ('d', "**Non-paracetamol liver failure: IV NAC improves transplant-free survival in early coma grades (I–II); no benefit in advanced coma, which needs transplant.** In the ALFSG trial (173 patients) transplant-free survival was 40% vs 27% overall and 52% vs 30% in grade I–II, with no gain in grade III–IV (9% vs 22%) and no difference in overall survival. ACG 2023 suggests IV NAC in non-paracetamol ALF; EASL notes the benefit is confined to early grades and that the paediatric trial was negative. Give NAC whenever paracetamol is even possible, because levels can be undetectable when patients present late."),
  ],
  mimic=[
    ("NAC in paracetamol vs non-paracetamol ALF", "Paracetamol: antidote, give at any stage. Non-paracetamol: benefit only in coma grade I–II, and transplant decisions must not wait for it."),
  ],
  traps=[
    ("“Methylprednisolone” for an unexplained hyperacute ALF", "Steroids are for autoimmune hepatitis with a supporting profile, not empirical use; NAC is safe and helps [DocT GT, 83% right]."),
    ("“Hepatitis B immunoglobulin” or “heparin”", "HBIG is post-transplant or post-exposure prophylaxis; heparin is for Budd–Chiari, which would show ascites and hepatomegaly, not this picture."),
  ],
  decode=[
    ("22-year-old, AST 5,116, ALT 4,300, INR 2.1, declining mental status, no history — what to start empirically? [DocT GT]", "N-acetylcysteine: transaminases in the thousands suggest paracetamol or ischaemia, and NAC is given whenever paracetamol is possible."),
    ("[pattern] Benefit of NAC in non-paracetamol ALF", "Better transplant-free survival in coma grade I–II only."),
  ],
  punch="Give IV NAC (150 mg/kg over 1 h, then 12.5 mg/kg/h for 4 h, then 6.25 mg/kg/h for 67 h) to any ALF patient in whom paracetamol is possible; in non-paracetamol ALF it helps only in coma grade I–II.",
)

L['ALF-30'] = dict(
  sub="GI → Acute liver failure → Anti-tubercular drug liver failure (AIIMS data)",
  step=6,
  intro="Step 6 turns to a cause that matters most in India: anti-tubercular drugs. This card gives the AIIMS series that defines it. No real question is linked, so this is short.",
  parts=[
    ('a', "**6% of all acute liver failure (70 patients).** 70 of 1,223 ALF patients (5.7%) over 1986–2009 (Kumar, Hepatology 2010); viral hepatitis remains the main cause in India."),
    ('b', "**Mortality 67%; 80% with a superadded virus (1.2% of the series).** The published mortality is 67.1%. Fifteen patients (1.2%) had a hepatitis virus as well as ATT; the 80% figure for them is the card’s and could not be checked against the abstract."),
    ('c', "**Who: 70% under 35 years; 70% female (10% pregnant).** Young women dominate this series."),
    ('d', "**Tempo: hyperacute, icterus to encephalopathy about 4.5 days.** The median interval was 4.5 days, so these patients swell their brains quickly and need early transfer."),
    ('e', "**The avoidable fact: 63% were on empirical treatment.** 62.8% had started ATT with no definite proof of tuberculosis, so the harm came from treatment that might not have been needed."),
  ],
  mimic=[
    ("ATT-ALF vs viral ALF in India", "ATT-ALF: young women, hyperacute, two-thirds mortality, often on empirical ATT. Viral (hepatitis E, B): history of exposure, markers positive."),
  ],
  traps=[
    ("“ATT liver failure is slow and subacute”", "In this series it was hyperacute, with only about 4.5 days from jaundice to coma."),
  ],
  decode=[
    ("[pattern] Proportion of ALF due to anti-TB drugs in India and its mortality", "About 6%; mortality about 67%."),
  ],
  punch="In the AIIMS series anti-tubercular drugs caused about 6% of ALF, killed two-thirds, struck mostly young women within days, and nearly two-thirds were on ATT started without proof of TB.",
)

L['ALF-31'] = dict(
  sub="GI → Acute liver failure → ATT hepatotoxicity: stop and restart rules",
  step=6,
  intro="Step 6 ends with the rules that prevent ALF-30: when to stop, how to keep TB covered, and how to restart. Three linked questions test the diagnosis of idiosyncratic DILI and the cholestatic rifampicin pattern; one, missed by 89%, tests the quinolone substitute.",
  parts=[
    ('a', "**Stop all drugs when ALT is above 5 times normal, or above 3 times with symptoms.** These are the ATS 2006 thresholds (above 3 times with jaundice and/or hepatitis symptoms). Stop also when bilirubin reaches jaundice levels (above 2 times normal), whatever the ALT (card layer). Isoniazid and pyrazinamide give a hepatocellular ALT rise; rifampicin more often a cholestatic rise of bilirubin and ALP."),
    ('b', "**ALT above 2 times normal: recheck at 1 and 2 weeks, then 2-weekly.** Mild rises are common (adaptation) and often settle on treatment; ATS asks for closer monitoring, every 2 weeks rather than monthly, when ALT is climbing towards a stop threshold."),
    ('c', "**If treatment cannot wait: a temporary non-hepatotoxic regimen of ethambutol, a fluoroquinolone and streptomycin.** ATS asks for at least three agents less likely to injure the liver, for example ethambutol, a fluoroquinolone and an injectable aminoglycoside (streptomycin) or capreomycin, for severe or smear-positive TB, so that the disease is covered while the liver recovers. A fluoroquinolone (levofloxacin or moxifloxacin) is the standard stand-in when rifampicin cannot be reintroduced."),
    ('d', "**Restart when ALT falls below 2 times normal.** Restarting too soon risks a second, more severe injury."),
    ('e', "**Order: rifampicin first (with or without ethambutol); isoniazid after 3–7 days; if ALT rises again, remove the last drug added. After prolonged or severe injury, no pyrazinamide; add ethambutol, a fluoroquinolone or cycloserine.** Rifampicin is the most important drug and the least likely cause of hepatocellular injury, so it goes first; pyrazinamide is the most hepatotoxic and is left out after severe injury. In the Sharma 2010 trial (about 175 patients), restarting all drugs at once or in two stepwise schedules gave recurrence in 8, 6 and 5 patients (13.8%, 10.2%, 8.6%), with no significant difference (watch line); sequential restart remains guideline practice because it identifies the culprit."),
  ],
  mimic=[
    ("Isoniazid/pyrazinamide vs rifampicin injury", "Isoniazid and pyrazinamide: hepatocellular, high ALT. Rifampicin: cholestatic, high bilirubin and ALP (it competes for bilirubin uptake and blocks the bile salt export pump)."),
    ("Idiosyncratic DILI vs paracetamol", "Idiosyncratic: weeks into a drug, not dose-related, subacute. Paracetamol: dose-related, hyperacute, transaminases in the thousands."),
  ],
  traps=[
    ("“A quinolone must never replace rifampicin”", "False: a fluoroquinolone is the standard substitute when rifampicin cannot be reintroduced. The GT6 option D is garbled (‘should not be substituted by Q’); read as ‘never substitute a quinolone’, it is the false statement and the key (only 11% right) [DocT GT]."),
    ("“Stop DOTS and switch to second-line drugs with ethambutol” as false", "That statement is true: with jaundice the hepatotoxic drugs are stopped and a non-hepatotoxic regimen covers the TB [DocT GT]."),
    ("“Hepatitis A, Wilson disease or paracetamol” for INR 2.5 and coma after 4 weeks of isoniazid", "No paracetamol, a 4-week course on a known idiosyncratic hepatotoxin: idiosyncratic DILI (91–100% right) [DocT GT]."),
  ],
  decode=[
    ("42-year-old on isoniazid, jaundice, INR 2.5, encephalopathy after 4 weeks, no paracetamol — aetiology? [DocT GT ×2]", "Idiosyncratic drug-induced liver injury."),
    ("On DOTS, bilirubin 18, jaundice worsened after ATT — identify the false statement [DocT GT]", "‘Rifampicin should not be substituted by a quinolone’ is false; a cholestatic rise points to rifampicin; stop rifampicin once bilirubin is above 2 times normal."),
    ("[pattern] When to restart ATT after hepatotoxicity, and in what order", "When ALT is below 2 times normal: rifampicin first, isoniazid after 3–7 days, pyrazinamide left out after severe injury."),
  ],
  punch="Stop ATT at ALT over 5 times normal, over 3 times with symptoms, or with jaundice; cover TB with ethambutol, a fluoroquinolone and streptomycin; restart when ALT is under twice normal, rifampicin first, then isoniazid, leaving out pyrazinamide after severe injury.",
)

FLAGS = {}
FLAGS['ALF-15'] = "Card a ‘commonest cause of death’ is the older Indian (AIIMS, Acharya 2000) position; EASL 2017 states that the most frequent causes of death are now multiorgan failure and severe sepsis. Figures 82% vs 44%, 58% and two-thirds within 72 h are confirmed in Acharya 2000."
FLAGS['ALF-18'] = "Watch line ‘about 25% of surges’ is marked unclear on the card and could not be traced; not restated as fact."
FLAGS['ALF-22'] = "Sodium targets differ by source: card 145–155 (Murphy 2004; AASLD 2011), EASL 2017 140–150 with correction ≤10 mmol/L per 24 h (card: 12). The watch line’s ACG 2023 wording (145–150, ceiling 160) could not be checked against the full text. Mannitol ‘paradoxical ICP rise in 20%’ not traced."
FLAGS['ALF-27'] = "India column: the matching AIIMS series (Acharya 2000) gives 52% as culture-positive or clinical sepsis, Gram-negatives 43% of culture-positive patients (Gram-positives 57%) and Aspergillus in 6 of 24 bacteraemic patients (25%); the card’s ‘Gram-negative (57%)’ may be swapped or from another series. Outcome rows (9.1% vs 60.3% etc.) not traced."
FLAGS['ALF-28'] = "Card b CPP ‘above 60’ follows AASLD 2011 (CPP 60–80); EASL 2017 says above 50, MAP about 60 adequate in the young. Hypoglycaemia ‘40%’ not traced (EASL: common). DocT GT key for refractory shock is low-dose hydrocortisone; card’s vasopressin and the hydrocortisone line are both correct. EASL gives platelets before line insertion if under 30,000 and above 60,000 for active bleeding (card: 50,000)."
FLAGS['ALF-30'] = "Card a ‘6%’ is 5.7% (70/1,223) and e ‘63%’ is 62.8% (Kumar, Hepatology 2010): rounding only. ‘80% mortality with a superadded virus’ and ‘10% pregnant’ not in the abstract; not verified."
FLAGS['ALF-31'] = "Card omits the bilirubin stop rule (jaundice, bilirubin above 2× normal) and the cholestatic rifampicin pattern that DocT GT6 tests; both are in the card layer and the explanation. ATS 2006 does not give the card’s ‘recheck at 1 and 2 weeks’ schedule and names an aminoglycoside or capreomycin rather than streptomycin specifically. GT6 option D is garbled; the trap gives the exam-day reading. Sharma 2010 favoured simultaneous reintroduction; the card’s sequential order is still ATS practice."
