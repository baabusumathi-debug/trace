# RESP02B top-up cards — Explain v3 ("Learn" depth), same fields and voice as resp02b_learn.py.
# Fields: sub, step (index into resp02b_learn.SPINE), intro, parts [(letter, text)], optional table, mimic, traps, decode, punch, optional extra.
# Card answers are restated in bold at the start of each part; disagreements with a card go in FLAGS, not in the text.
# Source questions come from the DocT Grand Test files (the top-up's own src) plus qpack/RESP02B.md.
T = {}

T['T_a6c60300'] = dict(
  sub="Respiratory → Drugs → Inhaled bronchodilators on the ventilator",
  step=4,
  intro="Step 4 gives the drugs for the attack; on the ventilator the question becomes how much of an inhaled dose actually reaches the lung. Aerosol must travel through tubing and an endotracheal tube, and most of it can stick to the circuit on the way. Every rule on this card either gives the aerosol a slower, larger, longer breath to ride or removes something that traps it.",
  parts=[
    ('a', "**Spacer in the inspiratory limb ~15 cm from the Y-piece; actuate at the START of inspiration.** The spacer lets the fast MDI plume slow down and evaporate into fine particles before the tube. Firing at the start of inspiration means the breath carries the aerosol in; fired during expiration it is lost down the expiratory limb. The exact distance matters less than the position: the 2023 international aerosol consensus (Ann Intensive Care 2023) asks for the pMDI with a spacer larger than 150 mL in the inspiratory limb before the Y-piece and gives no fixed distance."),
    ('b', "**Low inspiratory flow, VT >500 mL, longer Ti with a pause; remove the HME (or place the device between HME and patient).** Slow flow means less turbulence and less impaction in the circuit and tube; a large tidal volume and an end-inspiratory pause carry particles deep and let them settle. A heat–moisture exchanger is a filter and traps aerosol. These settings come from bench and small clinical studies; the 2023 consensus advises against changing tidal volume, flow pattern or mode solely for aerosol delivery, so in a lung-protective ARDS patient the low tidal volume is kept and the dose is titrated to response instead."),
    ('c', "**Wider ETT helps; deposition falls with high flow, small tubes and humidified gas; typical dose 4–8 puffs.** Narrow tubes and fast flow make particles impact on the tube wall; humidity makes them grow and rain out in the circuit. Because so much is lost, the usual dose is higher than in a spontaneously breathing patient."),
    ('d', "**Nebuliser with the HME left in place: the filter traps the aerosol and almost no drug arrives — remove the HME during nebulisation; volume control with a square, low inspiratory flow carries aerosol more consistently than pressure control.** A poor response with the HME still in the circuit is a delivery failure, not resistant bronchospasm. Volume control guarantees the breath size, whereas pressure control’s tidal volume falls exactly when the airways are tightest. This is the exam answer; in practice the mode is not changed just to give a nebuliser."),
    ('e', "**Vibrating-mesh nebuliser is electrically powered: no added driving gas, so VT, trigger and FiO₂ are undisturbed and it refills without breaking the circuit; a jet nebuliser adds 6–8 L/min of gas.** Extra gas from a jet nebuliser enlarges delivered volume, dilutes FiO₂ and can make triggering harder; the mesh device avoids all three and leaves less drug unused."),
  ],
  mimic=[],
  traps=[
    ("“Increase inspiratory flow to push the drug in”", "Higher flow increases impaction and reduces delivery; flow is lowered."),
    ("“Reduce tidal volume below 400 mL”", "Larger tidal volumes (>500 mL) improve delivery."),
    ("“Pressure control or a square waveform?”", "DocT keys volume control; a square low flow is the waveform volume control usually delivers, so read the options carefully when both appear."),
    ("“Minimal response to nebulised salbutamol — refractory asthma”", "Check the HME first; left in the circuit it traps the aerosol."),
  ],
  decode=[
    ("MDI with spacer near the Y-piece — which other adjustment improves delivery? [DocT GT ×2]", "Deliver during the inspiratory phase (75–80%)."),
    ("Nebulised salbutamol, minimal response, HME left in the circuit [DocT GT]", "Markedly reduced drug deposition."),
    ("Ventilator setting giving the greatest aerosol delivery [DocT GT]", "Volume-controlled ventilation."),
    ("Main advantage of a vibrating-mesh nebuliser over a jet nebuliser [DocT GT]", "Electrically powered — no added gas."),
  ],
  punch="Aerosol on a ventilator is lost to fast flow, small tubes, humidity and filters, so fire it at the start of a slow, large inspiration with the HME out of the path.",
)

FLAGS = {
  'T_a6c60300': "Card a (‘~15 cm from the Y-piece’) and b (low flow, VT >500 mL, pause) follow older guidance (Dhand). The 2023 international consensus (Ann Intensive Care 2023;13:63) places the pMDI spacer (>150 mL) in the inspiratory limb before the Y-piece with no fixed distance, and advises against changing VT, flow pattern or mode solely for aerosol delivery. Explanation states this; card not wrong for the exam key.",
}
