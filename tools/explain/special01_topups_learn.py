# SPECIAL01 top-up cards — Explain v3 ("Learn" depth), same fields and voice as special01_learn.py.
# Fields: sub, step (index into special01_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source question: trace/test/data/qbank.json → topups["SPECIAL01"] — T_59eb957d, DocT GT7 Q23 (cardiac arrest in a brain-dead patient = Maastricht IV). No cohort % given.
# From standard references without a fresh check: Maastricht classification (Kootstra 1995: I–IV); category V (unexpected arrest in a hospital in-patient) added in 2000 (checked online 13 Nov 2026; the Madrid 2011 classification has I–IV only);
# modified Maastricht (Paris 2013, Thuong et al. Transpl Int 2016) splits I and II into subgroups and mentions euthanasia (Belgian category V, Detry 2012) only in a footnote.
T = {}

T['T_59eb957d'] = dict(
  sub="Special situations → Organ donation → Maastricht DCD categories",
  step=1,
  intro="Step 1 covered who can become a donor. Besides the brain-dead donor whose heart is still beating, organs can be taken after the heart stops: donation after circulatory death (DCD). The Maastricht classification groups these donors by how the arrest happened, and the main line it draws is between uncontrolled arrests, where nobody knows how long the organs were without blood, and controlled arrests, where the team is ready. The one bank question asks where a brain-dead patient who arrests belongs.",
  parts=[
    ('a', "**IV. I found dead outside hospital and II witnessed arrest with failed resuscitation (both uncontrolled).** In both, warm ischaemia starts before any team is present and its length is uncertain, so these organs (mainly kidneys) carry the highest risk of non-function. They need rapid cannulation or normothermic regional perfusion and are used mainly in Spain and France."),
    ('b', "**III awaiting arrest after planned withdrawal of life support (controlled, the commonest DCD).** Treatment is withdrawn in the ICU or theatre with the retrieval team waiting; after a fixed no-touch period (usually 5 minutes) following circulatory arrest, death is declared and the organs are cooled straight away, so warm ischaemia is short and measured. This is the usual DCD in the UK, the USA and Australia."),
    ('c', "**IV arrest during or after brain-death testing; V (some versions) unexpected in-hospital arrest.** A brain-dead donor whose heart stops before retrieval moves from heart-beating donation to DCD; it can be controlled (retrieval team ready) or uncontrolled. Category V means different things in different versions: unexpected arrest of a hospital in-patient in the addition made in 2000; medically assisted circulatory death (euthanasia) in the Belgian modification (2012), which the Paris 2013 classification mentions only in a footnote, folding in-hospital arrests into IB and IIB."),
  ],
  table=dict(title="Maastricht categories", head=["Category", "Situation", "Controlled?"], rows=[
    ["I", "dead on arrival", "uncontrolled"],
    ["II", "failed resuscitation", "uncontrolled"],
    ["III", "awaiting arrest after withdrawal", "**controlled** (commonest)"],
    ["IV", "**arrest in a brain-dead donor**", "either"],
    ["V", "unexpected in-hospital arrest, or assisted death (by version)", "varies"],
  ]),
  mimic=[
    ("Maastricht IV vs DBD", "DBD retrieves organs from a brain-dead donor with a beating heart; if that heart stops first, the donor becomes Maastricht IV."),
    ("Maastricht II vs III", "II is a failed resuscitation (uncontrolled); III is a planned withdrawal with the team waiting (controlled)."),
  ],
  traps=[
    ("“A brain-dead patient who arrests is category III”", "III needs a planned withdrawal of life support in a patient who is not brain-dead; arrest after brain death is category IV."),
    ("“DCD organs are mostly uncontrolled”", "Category III, controlled, is the commonest DCD worldwide."),
  ],
  decode=[
    ("Cardiac arrest in a brain-dead patient — Maastricht category? [DocT GT]", "IV."),
    ("Commonest type of donation after circulatory death [pattern]", "Maastricht III, controlled withdrawal."),
  ],
  punch="Maastricht I and II are uncontrolled arrests (dead on arrival, failed resuscitation), III is the controlled withdrawal and the commonest DCD, and IV is the brain-dead donor whose heart stops before retrieval.",
)

FLAGS = {
  'T_59eb957d': "Card correct. Category V differs by version (unexpected in-hospital arrest in the 2000 addition; euthanasia in the Belgian 2012 modification, noted only in a footnote of the Paris 2013 classification, which puts in-hospital arrests in IB/IIB); the card’s ‘(some versions)’ covers this. Category IV is uncontrolled or controlled in the Paris 2013 classification (Thuong et al., Transpl Int 2016).",
}
