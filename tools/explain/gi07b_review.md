# GI07B review (independent fact-check, 20 Nov 2026)

Files checked: gi07b_learn.py (20 cards) and gi07b_topups_learn.py (T_584f592f) against cards/GI07B.jsonl, qpack/GI07B.md and gi_cardlayer.json. check_learn.py GI07B: OK (20/20, spine 6).

## Primary checks of the writer's new-guideline citations
- **Baveno VIII exists**: Baveno VIII Faculty, "Baveno VIII – Advancing Consensus in Portal Hypertension", J Hepatol 2026, doi 10.1016/j.jhep.2026.07.030 (accepted pre-proof, read via flore.unifi.it). Confirmed: 5.31 pre-emptive TIPS within 72 h (ideally <24 h) for Child C 10–13, Child B >7 with active bleeding, or HVPG ≥20; 5.33 ACLF, OHE, bilirubin, MELD, severe alcohol hepatitis not absolute contraindications; 6.16 rifaximin "should be considered" in candidates for elective TIPS; 6.19 terlipressin preferably as infusion, start 2–3 mg/24 h; 6.20 noradrenaline if terlipressin unavailable; 6.22 stop SBP prophylaxis on recompensation.
- **ACG 2026 HE guideline exists**: Bajaj JS et al., Am J Gastroenterol 2026;121(3):588–618 (PubMed 41773757; ACG EBGI summary Apr 2026). Confirmed: rifaximin from 14 days before elective TIPS and ≥6 months after (strong, moderate certainty); lactulose to 2–3 soft stools; protein 1.2–1.5 g/kg/day; BCAA if diet goals not met; ammonia should not guide treatment; rifaximin add-on for breakthrough.
- **ICA–ADQI 2024** (Nadim et al., J Hepatol 2024, PMC11193657): bolus 1–2 mg 6-hourly or infusion 2–12 mg/day, step up if creatinine not down 25%; albumin 20–40 g/day; noradrenaline 0.5–3 mg/h second line; midodrine–octreotide only if neither; stop at 14 days or no response after 48–72 h at maximum dose; response at 24 h, against 48 h albumin as a requisite. Writer's figures all match.

## Changes
- Header (ARiE): "Crit Care 2023" → Kulkarni et al., Am J Gastroenterol 2024; subgroup "HR 0.39 / ACLF HR 0.99" not confirmed → removed (The Bottom Line summary).
- CLD-29 g: "subgroup hazard ratio was 0.39" → "subgroup had lower mortality with rifaximin, none in ACLF (Kulkarni, AJG 2024)" (factual: unverifiable statistic, wrong journal).
- CLD-29 FLAG: Baveno VIII said to restrict rifaximin to "patients with prior HE" → statement 6.16 applies to all elective-TIPS candidates, no 14-day timing (factual; Baveno VIII pre-proof).
- Header (Baveno VIII): Afya secondary summary → primary pre-proof with statement numbers; "rifaximin … with prior HE" corrected as above.
- CLD-35 b: "Baveno VIII … adds HVPG ≥20 mmHg" → Baveno VII (2022) already had it; VII and VIII both accept it; window 72 h, ideally <24 h (factual; Baveno VIII 5.31). Same fix in CLD-35 FLAG.
- CLD-35 trap: Garcia-Pagán "within 72 hours (most within 24)" → randomised within 24 h of admission, TIPS within 72 h of randomisation; Baveno VIII ideally <24 h (factual; NEJM 2010 abstract via UB repository).
- CLD-17 d: "10% at admission … 10–30% develop it within a year" → EASL 2018 prevalence about 10% in hospitalised patients with ascites, 1.5–3.5% outpatients; card's 20% at upper end (factual: invented one-year figure).
- CLD-19 b: "about 10%" peritoneal signs: no primary source found → kept in bold (card), text now says series differ and guarding/rebound are the exception (softened).
- CLD-23 c: "secondary prophylaxis is lifelong until transplant" → long term, until transplant, death or recompensation (Baveno VIII 6.22) (minor).
- CLD-23 e: survival figures **verified**: Hung et al., Turk J Gastroenterol 2015;26:159–62, Taiwan nationwide cohort of 16,992 cirrhotics; SBP mortality 53.9%, 61.4%, 66.5% at 1, 2, 3 years; renal failure HR 2.02 for 3-year mortality. Moved from "could not verify" to verified in header. No text change.
- CLD-28 trap: "dialysis is not a treatment for HE in cirrhosis" contradicted CLD-29 f → "not initial treatment; kept for refractory HE with kidney injury or fluid overload" (minor, internal consistency).
- CLD-30 a: "the order is consistent" → exact figures not traceable to a primary study; pre-renal consistently largest, HRS a minority (softened; searched, no source for 41.7/38/20/0.3).
- CLD-33 f: "Noradrenaline works as well as terlipressin" → similar reversal in most trials; second line per ICA–ADQI 2024 and Baveno VIII 6.20 (minor).
- Header: Salerno 2013, Ginés 1990, Garcia-Pagán 2010, Bureau 2021 moved to "reviewer checked" with sources. All writer figures correct: Salerno 4 RCTs/288 pts, OR 0.21 and 0.34 (PubMed 23178229); Ginés 80 pts, 20% vs 68% (Hepatology 1990); Garcia-Pagán 63 pts, 86% vs 61%; Bureau 197 randomised, rifaximin 600 mg BD from 2 weeks pre-TIPS to day 168, overt HE 34% vs 53%, OR 0.48 (ACG EBGI).
- Topup T_584f592f b: "respond poorly to levodopa" → "inconsistent response to levodopa" (minor; response is variable in acquired hepatocerebral degeneration).

Checked and kept: Sort 1999 (6/63 vs 21/63; 14/63 vs 26/63); CONFIRM (32% vs 17%; respiratory deaths 11% vs 2%; 90-day mortality 51% vs 45%); Bass 2010; FDA Terlivaz label points; SBP Runyon criteria; cefotaxime 5 days; nosocomial regimen (EASL 2018); primary-prophylaxis criteria (Fernández 2007); West Haven/ISHEN; ammonia and lactulose mechanisms; OPTN SLK. All traps keep their truth side; bank-key disputes (CLD-25 "all of the above", CLD-25 GI bleed vs infection, CLD-33 Marrow midodrine key) agree with gi_cardlayer.json.

## Final FLAGS (gi07b_learn.py)
- CLD-32: b prints ICA 2015 / EASL 2018 criteria (48 h, albumin 1 g/kg/day, proteinuria/RBC exclusions); ICA–ADQI 2024 uses 24 h, against 48 h albumin, allows crystalloid or albumin 1–1.5 g/kg, adds urine output, lets CKD/tubular injury/proteinuria coexist. (Writer's flag, confirmed.)
- CLD-33: a bolus range 0.5 → 2–3 mg 6-hourly is older; ICA–ADQI 2024 1 mg then 2 mg 6-hourly; Baveno VIII infusion starts 2–3 mg/24 h, not 2 mg. (Writer's flag, confirmed.)
- CLD-35: c pre-existing HE is a contraindication for elective TIPS only; Baveno VIII 5.33: not an absolute contraindication to pre-emptive TIPS. HVPG ≥20 also qualifies (Baveno VII and VIII). (Corrected wording.)
- CLD-29: watch line credits Baveno VIII with "rifaximin from 14 days before elective TIPS"; only ACG 2026 says that; Baveno VIII 6.16 says "consider", no timing. (Corrected wording.)
- Topups: none.

Not verified: CLD-30 shares (41.7/38/20/0.3%); CLD-19b "about 10%" peritoneal signs; CLD-34 European/Canadian SLK thresholds (card figures kept).
