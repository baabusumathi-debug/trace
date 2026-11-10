# TOX03B top-up cards — Explain v2 ("Learn" depth), same fields and voice as tox03b_learn.py.
# Fields: sub, intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# No `step`: tox03b_learn.py has no SPINE (like TOX01, the toxicology decks were written before v3).
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from map/out/all_rows.json and the DocT GT files (the top-up's own src); qpack/TOX03B.md has no linked questions.
T = {}

T['T_1dbd9a24'] = dict(
  sub="Toxicology → Rodenticides → Strychnine and the airway",
  intro="Strychnine is one of the highly toxic rodenticides in PEST-14. It removes the brake on spinal motor neurons, so every stimulus sets off a full-body spasm in a patient who is awake throughout. The exam tests three things: how to tell it from a seizure, how to tell it from tetanus, and which drug to avoid at intubation.",
  parts=[
    ('a', "**Strychnine is a glycine-receptor antagonist: awake patient with painful generalised muscle spasms, opisthotonus, trismus and risus sardonicus, triggered by noise or touch.** Glycine is the main inhibitory transmitter in the spinal cord and brainstem; blocking its receptor leaves motor neurons firing unopposed. Extensors overpower flexors, giving the arched back, and a small sensory input produces a massive reflex response."),
    ('b', "**The sensorium stays clear — it is spinal disinhibition, not a seizure — and the muscles relax COMPLETELY between spasms, within minutes to an hour of ingestion. Tetanus differs: persistent baseline rigidity and trismus between spasms, onset days after a wound, autonomic storm later.** Glycine has little role in the cortex, so the patient is alert and feels every spasm. Tetanus toxin blocks the release of glycine and GABA from the inhibitory neuron, which produces a steady rigidity rather than discrete episodes."),
    ('c', "**Benzodiazepines first for the spasms, in a dark quiet room; add paralysis and ventilation if spasms threaten ventilation or hyperthermia.** Benzodiazepines strengthen the other inhibitory system, GABA-A, which partly replaces the lost glycine inhibition. Removing stimuli prevents triggers. There is no antidote, so paralysis is the definitive control."),
    ('d', "**Avoid DEPOLARISING blockers (suxamethonium) for rapid sequence induction: rhabdomyolysis gives hyperkalaemia and hyperthermia risk — use a non-depolarising agent.** Repeated spasms break down muscle and raise potassium; suxamethonium adds a further potassium rise and its own fasciculation. Rocuronium paralyses without either."),
    ('e', "**Supportive care with active cooling; death is from respiratory failure and hyperthermia.** Spasm of the chest wall and diaphragm stops ventilation, and constant muscle work generates heat, lactic acidosis and rhabdomyolysis."),
  ],
  mimic=[
    ("Strychnine vs generalised seizure", "Strychnine leaves consciousness intact; a tonic–clonic seizure removes it and leaves post-ictal confusion."),
    ("Strychnine vs tetanus", "Strychnine: onset within an hour, full relaxation between spasms. Tetanus: onset days after a wound, rigidity and trismus persist between spasms."),
  ],
  traps=[
    ("“Hyperthermia, lactic acidosis or rhabdomyolysis favour strychnine over seizures”", "All three follow any prolonged muscle activity, including seizures; only preserved consciousness separates them."),
    ("“Persistent trismus or sympathetic overactivity favours strychnine”", "Both point to tetanus; complete relaxation between spasms is the strychnine sign."),
    ("“Suxamethonium for the RSI”", "Avoid it: rhabdomyolysis and hyperkalaemia; use a non-depolarising agent."),
  ],
  decode=[
    ("Unknown rodenticide, awake, extensor spasms triggered by noise — best feature against tonic–clonic seizures? [DocT GT]", "Preserved consciousness."),
    ("Trismus and painful spasms — feature that most reliably separates strychnine from tetanus? [DocT GT]", "Complete muscle relaxation between spasms."),
    ("Strychnine poisoning needing RSI — avoid? [Marrow]", "Depolarising neuromuscular blockers."),
  ],
  punch="Strychnine takes the glycine brake off the spinal cord, so an awake patient spasms and then relaxes completely; control it with benzodiazepines and, if needed, a non-depolarising blocker, never suxamethonium.",
)

FLAGS = {}
