# Top-up explanations: independent review (10 Nov)

All 14 ids in topups_todo.json have an entry. Every bold restatement matches its card answer line, in order. All 8 files exec cleanly.

Checked and found correct (no change): RESP01A goals (SpO2 ≥90% on FiO2 <0.6, pH >7.2, FACTT); RESP01B CPAP/BiPAP and NIV contraindications; emphysema rib counts (>6 anterior / >10 posterior) and retrosternal space >2.5 cm (Radiopaedia); IPF restrictive pattern with normal/raised FEV1/FVC and early DLCO fall; Types I–IV respiratory failure (type III perioperative atelectasis, type IV shock/hypoperfusion; Principles of Critical Care via UMEM summary); EDAC diagnosis by dynamic bronchoscopy/dynamic expiratory CT (J Thorac Dis TBM review); anterior mediastinal mass predictors and plan (SPA case guide); strychnine onset 15–60 min, benzodiazepines, non-depolarising blockers (Mahidol poison-centre protocol); thiamine 200–500 mg IV 8-hourly (GPnotebook/NICE: 300–500 mg TDS for Wernicke); Rosenson 2013 ICU 25% to 8% (J Emerg Med 2013, PMID 22999778); Loxosceles systemic illness 24–72 h, up to 7 days (Missouri Poison Center); prazosin 30 µg/kg in children, 3-hourly (Indian Pediatrics 2014).

## Changes

- RESP02A T_ade9b5a5 c: "bullae are air spaces without vessels or walls" → avascular air spaces >1 cm with walls <1 mm (standard radiology definition; bullae have thin walls).
- RESP02A T_a8369bdb b: added the >50% expiratory lumen loss threshold and its low specificity (J Thorac Dis, severe adult TBM review).
- RESP02A T_a68aceb6 mimic: extrapulmonary restriction KCO "preserved" → "normal or raised" (KCO rises when lung tissue is normal but volume is small).
- RESP02B T_a6c60300 a: added that the 2023 international aerosol consensus (Ann Intensive Care 2023, s13613-023-01147-4) places the pMDI with a spacer >150 mL in the inspiratory limb before the Y-piece and withdrew distance-specific statements; the 15 cm figure is not critical.
- RESP02B T_a6c60300 b: added that the same consensus advises against changing VT, flow pattern or mode solely for aerosol delivery (keep lung-protective VT, titrate dose).
- RESP02B T_a6c60300 d: added that volume control is the exam answer but the mode is not changed just for a nebuliser (same consensus). New FLAG.
- RESP03 T_3e6c3480 b: added Marini 1979 (Am Rev Respir Dis; 31 patients, randomised): bronchoscopy added nothing to respiratory therapy, and an air bronchogram predicted slow resolution; bronchoscopy kept for severe/refractory hypoxaemia, failed physio or a suspected central plug. Added a trap on the same point.
- RESP03 T_23f59da7 c: "may spoil the biopsy" → may compromise histology; take tissue first (peripheral node / local anaesthesia) where possible, short steroid course after oncology discussion if the airway cannot wait, watch for tumour lysis (SPA case guide: a short course may not hamper diagnosis; discuss with oncology first).
- TOX04 T_dbdbadf0 d: Rosenson 2013 described correctly: 102 ED patients, single 10 mg/kg IV vs placebo added to a symptom-guided lorazepam protocol, ICU 25% → 8%, no excess adverse events, mortality not an outcome; it was not a benzodiazepine-refractory population (Medbullets/PMID 22999778 abstract).
- TOX04 T_dbdbadf0 e: "Sodium-channel drugs treat focal epilepsy" → phenytoin and levetiracetam do not prevent or stop withdrawal seizures; carbamazepine reduces symptoms in mild–moderate outpatient withdrawal but has no role in severe withdrawal, DT or seizure treatment (Australian alcohol treatment guidelines, rec 8.29 grade A for carbamazepine, 8.30 phenytoin not recommended). Trap reworded to match. New FLAG.
- TOX05 T_1467a2fc e: mechanism softened to sodium- and potassium-channel neurotoxins releasing catecholamines; added the adult prazosin dose: a fixed 0.5–1 mg orally, 1 mg in Bawaskar's 2011 randomised trial (NCT00753064: 500 µg children, 1 mg adults, 3-hourly until recovery).
- TOX05 T_dfc56d26 b: added the review's data: vipers ~80% of cases, hump-nosed (26%) and Russell's viper (23%) the commonest identified; TMA in ~10% of VICC in the Australian cohort (Noutsos 2020, PLoS NTD, PMC7748274).
- TOX05 T_dfc56d26 c: normal ADAMTS13 attributed to small case series (Isbister, brown-snake TMA, 2 patients with normal ADAMTS13; Univ. Newcastle record), not the 2020 review; plasma exchange "cannot be recommended" (Noutsos 2020).
- TOX05 T_dfc56d26 d: "antivenom neither prevents nor shortens" explained as "no evidence that antivenom changes the course" (Noutsos 2020). FLAG rewritten with these facts.

Not verified, left as is: DocT/Marrow cohort percentages in traps and decode lines (taken from the source question files; the ones spot-checked, 65% for the mediastinal mass and 75–80% for MDI timing, match doct_gt_distinct_all.jsonl).

## Final FLAGS

- T_a6c60300 (RESP02B): Card a (~15 cm from the Y-piece) and b (low flow, VT >500 mL, pause) follow older guidance (Dhand). The 2023 consensus puts the pMDI spacer (>150 mL) before the Y-piece with no fixed distance and advises against changing VT, flow or mode only for aerosol. Not wrong for the exam key.
- T_938aa87a (RESP03): unchanged. DocT keys type III for a hypercapnic post-op opioid patient; type II is defensible; the explanation names the dispute.
- T_dbdbadf0 (TOX04): Card e "carbamazepine does not work" is too absolute (effective in mild–moderate outpatient withdrawal; not for seizures, severe withdrawal or DT). Card d puts Rosenson 2013 under "benzodiazepine-refractory", but the trial gave one up-front ED dose added to lorazepam.
- T_dfc56d26 (TOX05): Card c credits "ADAMTS13 normal" to Isbister/Noutsos 2020. The review has no ADAMTS13 data; that comes from case series. The review's findings are no benefit from plasma exchange and no evidence of benefit from antivenom. Card b "mainly Russell's viper" is slightly narrow (hump-nosed 26%, Russell's 23%). DocT Animal P2 Q11 key B is wrong in substance.
