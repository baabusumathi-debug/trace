# RESP06A top-up cards — Explain v3 ("Learn" depth), same fields and voice as resp06a_learn.py.
# Fields: sub, step (index into resp06a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source question comes from the DocT GT Recall25 file (the top-up's own src, Recall25:Q70 = TS411658) plus qpack/RESP06A.md.
# Checked online 11 Nov 2026: ACCP (Geerts 2008) surgical risk levels and DVT rates without prophylaxis. Second review: Caprini tiers of ACCP 2012 (Gould) confirmed (very low 0, low 1–2, moderate 3–4, high ≥5).
T = {}

T['T_9885f6ac'] = dict(
  sub="Respiratory → Pulmonary embolism → Surgical VTE risk by operation",
  step=1,
  intro="Step 1 says surgery is one of the strongest triggers of VTE (PE-02). How strong depends on the operation: its length, how much tissue and bone it injures, how near it is to the pelvic and leg veins, and how long the patient stays immobile afterwards. The NEET 2025 recall asks which operation is not medium risk.",
  parts=[
    ('a', "**Low: minor day-case surgery under 30 minutes with early ambulation (for example inguinal hernia repair).** Little tissue injury and an early return to walking keep the calf pump working. In the ACCP tiers (Geerts 2008) low risk means a DVT rate below 10% without prophylaxis, and early ambulation alone is enough."),
    ('b', "**Moderate: major general, gynaecological or maxillofacial surgery, or splenectomy, without extra risk factors.** Longer operations under general anaesthesia with more tissue injury and days of reduced mobility; DVT rate 10–40% without prophylaxis, so pharmacological prophylaxis (LMWH or low-dose heparin) is given, or mechanical if bleeding risk is high. Age, cancer, prior VTE or obesity move the patient up a tier."),
    ('c', "**High: hip or knee arthroplasty, hip fracture, major trauma, spinal cord injury, cancer surgery — so total hip replacement is not ‘medium’.** Hip surgery injures the femoral vein directly (twisting during the operation), leg surgery and paralysis abolish the calf pump, and trauma and cancer activate coagulation; DVT rates without prophylaxis reach 40–80%, which is why prophylaxis is extended for weeks after arthroplasty. ACCP 2012 grades general and abdominal-pelvic surgery by the Caprini score instead (very low 0, low 1–2, moderate 3–4, high ≥5), and abdominal or pelvic cancer surgery usually reaches the high group because cancer and major surgery each add 2 points and age adds more."),
  ],
  table=dict(title="Surgical risk tiers (ACCP 2008, with the card’s examples)", head=["Tier", "Examples", "DVT without prophylaxis"], rows=[["Low", "minor surgery, mobile patient (inguinal hernia)", "<10%"], ["Moderate", "most general, open gynaecological or urological surgery; maxillofacial; splenectomy", "10–40%"], ["High", "**hip or knee arthroplasty, hip fracture, major trauma, spinal cord injury**", "40–80%"]]),
  mimic=[
    ("Total hip replacement vs other ‘major’ surgery", "Both are long operations under anaesthesia, but hip and knee arthroplasty add direct venous injury and post-operative leg immobility, so they sit in the high tier however fit the patient."),
  ],
  traps=[
    ("“Inguinal hernia repair is medium risk”", "By the same tiers it is low risk, so strictly two options (A and C) are not medium; the question works only by its intent — find the high-risk operation — and the key is total hip replacement."),
  ],
  decode=[
    ("All of the following surgeries carry a medium risk of DVT EXCEPT: inguinal hernia repair, maxillofacial surgery, total hip replacement, splenectomy for ITP [NEET 2025 recall]", "Total hip replacement (high risk)."),
  ],
  punch="Minor day-case surgery is low risk, most major general, gynaecological and maxillofacial surgery moderate, and hip or knee arthroplasty, hip fracture, major trauma, spinal cord injury and cancer surgery high — so total hip replacement is never ‘medium’.",
)

FLAGS = {}
FLAGS['T_9885f6ac'] = "Recall25:Q70 is flawed: by DocT’s own explanation inguinal hernia repair (A) is low risk, so two options are not ‘medium’; key C (THR, high) is the intended answer. Card line c adds ‘cancer surgery’ to the high tier — usually true under ACCP 2012/Caprini scoring, not in the ACCP 2008 example list; maxillofacial surgery and splenectomy (line b) are not ACCP 2008 examples either (which names arthroplasty, hip fracture, major trauma, spinal cord injury)."
