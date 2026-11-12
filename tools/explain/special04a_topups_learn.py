# SPECIAL04A top-up cards — Explain v3 ("Learn" depth), same fields and voice as special04a_learn.py.
# Fields: sub, step (index into special04a_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part (one part per answer line, in order); disagreements with a card go in FLAGS, not in the text.
# Source questions: map/out/all_rows.json — DocT GT2 Q120 (why monoclonal antibodies have a small central Vd: ‘Limited membrane diffusion’, 50% right) and DocT GT3 Q75 (falling mAb
# levels in autoimmune disease: ‘Increased immune clearance’, 64% right). Only the stems’ short forms and keys were available; the other options were not.
# From standard references without a fresh check (confident): IgG ~150 kDa; Vd roughly plasma plus part of the interstitium (central ~3 L, total ~5–8 L, under 0.1–0.15 L/kg); elimination by
# intracellular (lysosomal) proteolysis after pinocytosis, and by target-mediated drug disposition (TMDD), which saturates at higher doses; no glomerular filtration of intact IgG; FcRn salvage
# gives IgG1 a half-life of about 3 weeks; anti-drug antibodies (immunogenicity) speed clearance and are reduced by co-prescribed methotrexate or azathioprine.
T = {}

T['T_8c9e16fa'] = dict(
  sub="Special topics → Pharmacokinetics → Monoclonal antibodies",
  step=2,
  intro="Step 2 explained that where a drug goes depends on whether it can cross membranes. Monoclonal antibodies take that to an extreme: they are proteins several hundred times the size of a typical antibiotic, so they stay almost entirely in the plasma and interstitial fluid, and they are removed by being broken down, not by the kidney or the liver. The two bank questions ask why their Vd is small and why their levels fall over months of treatment.",
  parts=[
    ('a', "**~150 kDa → cannot cross membranes → small Vd (plasma + interstitium, ~3–8 L).** A small-molecule drug diffuses across cell membranes; an IgG antibody is far too big and too polar to do so. It leaves the blood only slowly, by convection through gaps in the capillary wall, and reaches the interstitium but not the inside of cells. So its central Vd is close to plasma volume (about 3 L) and its total Vd only a few litres more."),
    ('b', "**Not renally cleared; proteolysis and target-mediated disposal (non-linear at low doses).** At about 150 kDa an IgG is far above the glomerular filtration cut-off, and the liver’s CYP enzymes do not act on it, so renal and hepatic failure barely change its dose. It is taken up into cells by pinocytosis and digested in lysosomes. It is also removed when it binds its target and the complex is internalised. That route saturates once the target is occupied, so clearance is faster at low doses and the kinetics are non-linear."),
    ('c', "**FcRn recycling protects IgG → long half-life (~3 weeks).** Inside the endosome the neonatal Fc receptor binds the antibody’s Fc portion at acid pH and carries it back to the cell surface, where it is released into the blood instead of being digested. This salvage gives IgG1 a half-life of about 21 days and allows dosing every 2–8 weeks."),
    ('d', "**Anti-drug antibodies increase immune clearance → falling troughs, loss of response.** The patient’s immune system may make antibodies against the therapeutic antibody, especially against chimeric or humanised regions. The immune complexes are cleared quickly, so trough levels fall and the disease returns despite unchanged dosing. Measuring the trough level and anti-drug antibodies separates this from true failure of the drug’s target; co-prescribed methotrexate or azathioprine reduces it."),
  ],
  mimic=[
    ("Monoclonal antibody vs small-molecule drug", "Antibody: small Vd, no renal or CYP clearance, half-life of weeks, cleared by proteolysis and its target. Small molecule: crosses membranes, filtered or metabolised, half-life of hours."),
    ("Anti-drug antibodies vs target-mediated clearance", "Anti-drug antibodies appear over weeks to months of treatment and cause a new fall in levels. Target-mediated clearance is there from the first dose and is greatest when the target burden is high or the dose is low."),
  ],
  traps=[
    ("“Their small Vd is due to high protein binding or rapid renal clearance”", "Antibodies are themselves proteins and are not filtered; the cause is that they cannot diffuse across membranes (50% right on DocT GT)."),
    ("“Falling levels on a mAb mean the drug is cleared faster by the kidney or liver”", "Neither organ clears intact IgG; the usual cause is anti-drug antibodies increasing immune clearance (64% right on DocT GT)."),
    ("“Reduce the dose in renal failure”", "Renal function does not change IgG clearance."),
  ],
  decode=[
    ("Why do monoclonal antibodies have small central volumes of distribution? [DocT GT]", "Limited membrane diffusion."),
    ("Autoimmune disease on a mAb, drug levels falling, response lost — mechanism? [DocT GT]", "Increased immune clearance (anti-drug antibodies)."),
  ],
  punch="An antibody is too big to cross membranes or be filtered, so it stays in plasma and interstitium and is removed by proteolysis and by its target. FcRn salvage gives it a half-life of weeks, and anti-drug antibodies are what make its levels fall.",
)

FLAGS = {}
