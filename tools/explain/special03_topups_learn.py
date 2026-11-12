# SPECIAL03 top-up cards — Explain v3 ("Learn" depth), same fields and voice as special03_learn.py.
# Fields: sub, step (index into special03_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source question: DocT GT4 Q28 (Wernicke encephalopathy), via qbank.json topups["SPECIAL03"].
# Review 13 Nov 2026: Harper 1986 (131 cases, triad 16%, no signs 19%), Caine criteria and EFNS ≥200 mg tds re-checked online. Otherwise from standard references (confident): classic triad 10–20%; MRI pattern (symmetric T2/FLAIR
# signal in medial thalami, mammillary bodies, periaqueductal grey, tectal plate; DWI may show restriction; contrast enhancement of mammillary bodies typical of the alcohol-related form);
# high-dose regimen 500 mg IV three times daily for 3 days then 250 mg daily (RCP/Thomson; EFNS 2010 gives 200 mg three times daily IV); Caine criteria (2 of 4: dietary deficiency,
# eye signs, cerebellar dysfunction, altered mental state or memory impairment); thiamine is a cofactor for pyruvate dehydrogenase, α-ketoglutarate dehydrogenase and transketolase.
T = {}

T['T_3d23a130'] = dict(
  sub="Nutrition → When feeding harms → Wernicke encephalopathy",
  step=5,
  intro="Step 5 covered harm from feeding a starved patient, and Wernicke encephalopathy is its neurological form. Thiamine is a cofactor for the enzymes that move glucose through the Krebs cycle, and body stores last only a few weeks, so a malnourished patient given carbohydrate uses up what is left and the most metabolically active parts of the brain fail first. The one GT question asks for the picture, the scan and the treatment together.",
  parts=[
    ('a', "**Triad (complete in only about 10%): confusion, ataxia, ophthalmoplegia or nystagmus; causes are alcohol, hyperemesis, bariatric surgery and refeeding.** Because the full triad is uncommon (16% in Harper’s autopsy series of 131 cases, and 19% had no recorded signs), waiting for all three misses most cases; the Caine criteria, derived in alcohol-dependent patients, need only two of dietary deficiency, eye signs, cerebellar signs and altered mental state or memory. In the ICU the patient is often sedated, so the eye signs and an unexplained confusion in a malnourished or alcohol-dependent patient are enough. Hyperemesis, bariatric surgery, prolonged vomiting, cancer and refeeding (NUT-12) are the non-alcohol causes that stems use."),
    ('b', "**MRI: symmetric T2/FLAIR signal in the medial thalami, mammillary bodies, periaqueductal grey and tectum.** These regions surround the third ventricle and aqueduct and have the highest thiamine-dependent glucose turnover, so they swell first. MRI is specific but not sensitive (it is normal in many patients), so a normal scan does not exclude the diagnosis and never delays treatment."),
    ('c', "**Treat on suspicion: thiamine 500 mg IV 8-hourly for 3 days, then 250 mg daily.** Oral thiamine is poorly absorbed, especially in alcohol use, so high-dose IV is given; regimens differ (EFNS: at least 200 mg three times daily IV; some UK hospital protocols use two pairs of Pabrinex three times daily for 5–7 days). Eye signs improve within hours to days, ataxia and confusion more slowly; untreated, it progresses to Korsakoff’s amnesia, coma and death. Magnesium is replaced too, because the thiamine-dependent enzymes need it."),
    ('d', "**Never delay glucose to give thiamine first (TOX-01).** A hypoglycaemic brain is injured within minutes, while a single glucose dose does not precipitate Wernicke’s; give glucose at once and thiamine alongside. The ‘thiamine first’ rule applies to a planned refeed, not to an emergency."),
  ],
  mimic=[
    ("Wernicke vs Korsakoff", "Wernicke: acute, confusion, ataxia, eye signs, reversible with thiamine. Korsakoff: chronic, anterograde amnesia with confabulation, largely irreversible."),
    ("Wernicke vs hepatic encephalopathy in an alcoholic", "Both confuse; eye signs and ataxia point to Wernicke, asterixis and high ammonia to hepatic encephalopathy. Treat Wernicke anyway when in doubt."),
  ],
  traps=[
    ("“All three features are needed before thiamine”", "The triad is complete in only about a tenth; treat on suspicion."),
    ("“A normal MRI excludes Wernicke’s”", "MRI is specific, not sensitive."),
    ("“Thiamine 100 mg orally is enough”", "Suspected Wernicke’s needs high-dose IV thiamine."),
    ("“Hold glucose until thiamine is given”", "Glucose is never delayed in hypoglycaemia (TOX-01)."),
  ],
  decode=[
    ("Wernicke encephalopathy — clinical picture, MRI findings and treatment? [DocT GT]", "Confusion, ataxia, eye signs (triad often incomplete); symmetric medial thalamic, mammillary and periaqueductal T2/FLAIR signal; high-dose IV thiamine on suspicion."),
    ("Malnourished patient started on feed, becomes confused with nystagmus on day 3 [pattern]", "Refeeding-induced Wernicke’s: IV thiamine, check phosphate and magnesium."),
  ],
  punch="Treat Wernicke’s on suspicion with high-dose IV thiamine, because the triad is usually incomplete and MRI often normal; and never delay glucose for a hypoglycaemic patient while waiting for it.",
)

FLAGS = {
  'T_3d23a130': "Card is sound. ‘Complete in only ~10%’: Harper’s autopsy series (131 cases) found 16%; 10–20% is the usual range. The 500 mg IV 8-hourly × 3 days then 250 mg daily schedule is the commonly quoted high-dose regimen (Thomson/RCP 2002; Sechi and Serra 2007), which has no trial basis; the original documents were not opened. EFNS 2010: at least 200 mg three times daily IV (confirmed via a 2014 CMAJ review). UK trust protocols vary (e.g. two pairs of Pabrinex three times daily for 5–7 days).",
}
