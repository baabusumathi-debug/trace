# GI02A top-up cards — Explain v3 ("Learn" depth), same fields and voice as gi02a_learn.py.
# Fields: sub, step (index into gi02a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Parts follow the lines of the top-up's answer in order (a, b, c…); each starts with the line restated in bold. Disagreements with a card go in FLAGS, not in the text.
# Source: gi_topups.json["GI02A"]: T_9299d85e (cutaneous signs of haemorrhagic pancreatitis, 3 links: Marrow QB38-Q02, Q07, Q09). The source stems were not opened; decode items follow the top-up question.
# Checked online 20 Nov 2026: Dickson & Imrie (Surg Gynecol Obstet 1984, abstract): 770 patients, body wall ecchymosis in 3% of acute pancreatitis, mortality 37% in that group.
# Reviewer check 20 Nov 2026 (LITFL, non-traumatic abdominal ecchymosis): Grey Turner flank (anterior pararenal space, lumbar triangle), Cullen periumbilical, Fox upper outer thigh below the
# inguinal ligament (along psoas and iliacus fascia), Bryant scrotum (inguinal canal and spermatic cord; classically ruptured AAA); signs usually appear 3–5 days after onset.
# From standard references (confident): Cullen via the falciform ligament; also in ruptured ectopic pregnancy and other haemoperitoneum.
T = {}

T['T_9299d85e'] = dict(
  sub="Acute pancreatitis → Severity → Cutaneous signs of retroperitoneal haemorrhage",
  step=5,
  intro="Step 5 is about spotting the patient who will do badly, and these bruising signs are the oldest bedside clue. They mean blood from a necrotising, haemorrhagic pancreas has tracked through tissue planes to the skin, usually a day or more after onset. Marrow asks them three times: the names and sites, what they mean, and how much weight to give them.",
  parts=[
    ('a', "**Grey Turner: flank; Cullen: periumbilical; Fox: upper thigh below the inguinal ligament; Bryant: scrotum.** Each site is where a retroperitoneal plane reaches the skin: the flank from the anterior pararenal space through the lumbar triangle, the umbilicus along the falciform ligament, the thigh by tracking beneath the inguinal ligament along the psoas and iliacus fascia, and the scrotum through the inguinal canal along the spermatic cord. Fox and Bryant signs are not specific to pancreatitis: both are also seen with a leaking abdominal aortic aneurysm."),
    ('b', "**Retroperitoneal blood tracking from haemorrhagic necrotising pancreatitis.** Elastase digests vessel walls in necrotic tissue (PANC-02), and the blood spreads slowly through the retroperitoneum before it shows in the skin, usually several days (typically 3–5) after the pain began, so the signs are late and cannot guide early triage."),
    ('c', "**Seen in under 5% of severe AP: very low sensitivity and NPV, so their absence excludes nothing; their presence signals high mortality.** In Dickson and Imrie’s series body wall bruising occurred in about 3% of all acute pancreatitis, with a mortality of 37% in those patients. A sign present in so few cannot be used to rule severe disease out; severity is still judged by organ failure (PANC-05)."),
    ('d', "**Cullen also occurs in ruptured ectopic pregnancy and other haemoperitoneum.** Any intra-abdominal or retroperitoneal bleed can track to the umbilicus, so the sign means blood, not pancreatitis specifically."),
  ],
  mimic=[
    ("Grey Turner vs Cullen", "Grey Turner is flank bruising (retroperitoneal route); Cullen is periumbilical bruising (along the falciform ligament). Both mean retroperitoneal or intra-abdominal blood."),
    ("Cullen in pancreatitis vs ruptured ectopic", "Pancreatitis: epigastric pain to the back, lipase above three times normal. Ectopic: a woman of reproductive age, positive pregnancy test, pelvic fluid on ultrasound."),
  ],
  traps=[
    ("“No Grey Turner or Cullen sign, so it is not severe”", "The signs are seen in only about 3%; their absence excludes nothing."),
    ("“Cullen’s sign is specific for pancreatitis”", "It occurs with any haemoperitoneum, classically a ruptured ectopic pregnancy."),
  ],
  decode=[
    ("Bruising of the flank or around the umbilicus in pancreatitis: name and meaning [Marrow]", "Grey Turner (flank), Cullen (periumbilical): retroperitoneal haemorrhage from necrotising pancreatitis."),
    ("Prognostic value of body wall ecchymosis [Marrow]", "Rare and insensitive, but when present it marks a high mortality."),
  ],
  punch="Grey Turner, Cullen, Fox and Bryant signs are retroperitoneal blood from haemorrhagic necrosis reaching the skin; they are rare, so their absence means nothing, but their presence marks a high risk of death.",
)

FLAGS = {
  'T_9299d85e': "c: ‘under 5% of severe AP’ — Dickson & Imrie (1984) give about 3% of all acute pancreatitis (mortality 37%), not of severe disease only. The explanation restates the card and gives the source figure.",
}
