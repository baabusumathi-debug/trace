# P12 NEET cardiology packets — writer brief (23 Nov 2026)

You are writing the middle of one **NEET packet** for Naven (Dr Harish), who is preparing for the NEET-SS DM Critical Care exam (11–12 Dec 2026), an MCQ exam. A packet is built like his viva packages in the Trace app: an opening lesson, then the cards in a deliberate order, each with a narrated micro-lesson, then a closing lesson. Its aim is NEET MCQs, not viva answers. **Claude (the orchestrator) writes the opening and closing lessons. You write everything in between**, and you collect the traps and mimics that the closing lesson will draw on.

Why this works for him: in the viva packages nothing felt like a standalone card. Everything sat on one arc and the narration carried him from card to card. Keep that feel. The facts already exist; your job is the **one continuous story**.

## Inputs (read them all)
- `/home/claude/p12/S1_pack.json` — the packet: questions (sections) in order, and for each step the card (`q`, `a` with corrections applied), its NEET explanation (`explain`: intro, why per part, mimic, traps, punch), the bank lines (`bank_lines`: how DocT, Marrow, the GTs and NEET recall asked it), how many bank questions hit it (`bank_questions`), and any earlier viva lesson for the card (`earlier_viva_lessons`, from package P1). Earlier lessons are source material: Naven may have heard them. Do not copy them. You may call back to them ("You met this in haemodynamics…").
- The writing standard is below. It is binding.

## What to write: `/home/claude/p12/S1_draft.json`
```json
{
  "questions": [
    {
      "q": "P12-101",
      "text": "…the section title, as given…",
      "steps": [
        { "card": "CVS03|CS-02",
          "bridge": "One or two sentences on screen, handing over to the next card, at most 160 characters. null on the last step of the last section.",
          "lesson": { "v": 1, "text": "…the micro-lesson…" },
          "model": { … }            // ONLY on echo steps; see the model section
        }
      ],
      "spine": ["4 to 6 short lines: the chain of this section, at most 200 characters each"]
    }
  ],
  "drill": [ { "q": "…", "a": "…" } ],          // 15–25 tap-to-reveal items for the end of the packet
  "traps": [ { "trap": "…", "truth": "…", "cards": ["DECK|CODE"], "asked": "where it was asked, e.g. GT4 Q75, DocT 60%" } ],
  "mimics": [ { "pair": "X vs Y", "tell": "the single feature that separates them", "cards": ["DECK|CODE"] } ],
  "new_cards": [],                                // only if a NEET-asked fact has no card at all (see below)
  "card_flags": [ { "card": "DECK|CODE", "issue": "…" } ]   // card text you believe is wrong; do not fix the card
}
```
Use exactly the sections and the card order of the pack. If a step truly adds nothing for NEET, you may write a short 20–40 second lesson for it, but keep it in the walk.

## The micro-lesson (each step)
- It **replaces the explanation** for that card in this packet. Reshape the NEET explanation and the card into a narration that sits on the arc. Keep every fact that NEET asks (use `bank_lines` and `bank_questions` to judge weight). Drop the explanation's own intro and punchline, because the packet carries those.
- Length: a reasoning card 1.5–3 minutes (about 1,500–3,000 spoken characters); a pure fact or number card about 30–60 seconds (400–900). The hard cap is 4,000 spoken characters.
- **Open by joining it to the card before** (the arc), then mechanism first, then the clinical layer, then the exact numbers last. Teach the why.
- **Name the trap where it forms**, in one line ("NEET's favourite wrong option here is…"). Then collect it in `traps`.
- **One discriminator per mimic**, not a table. Collect it in `mimics`.
- Mark one or two takeaways per lesson with `[[ … ]]`: whole sentences, at most 300 characters each, at most a quarter of the spoken text. These are the "write this on your palm card" lines.
- On-screen-only boxes `{{ … }}` (a paragraph of their own, at most 400 characters; bold and simple `A | B` tables allowed). Use them for a table or a set of numbers the eye needs, e.g. the PA-catheter profile table.
- End on a short hand-off or teaser into the next card. The last step of a section hands over to the next section.
- **No story worlds, no invented characters.** A simple classic mnemonic only where a standard one already exists and genuinely helps. Patients may be named Patient A, Patient B.

## Writing standard (from the viva standard, binding)
- A calm, certain senior teaching one aspirant, speaking to "you". Level: an anaesthetist who has forgotten the detail.
- Say what matters and what doesn't ("You don't need this number. You need this one.").
- Build from the ground up, cause before effect, signpost ("first… then… so…"), loop back often.
- True discovery stories only; never invent history. Analogies only if every element is true and it carries something a sentence can't.
- Vary rhythm: long building sentences, then a short one that lands.
- **Written for the ear:** no symbols, arrows, brackets, bullet points or tables in spoken text. Numbers as they are said ("two point two litres per minute per square metre", "fifteen millimetres of mercury"). Never read card codes aloud. Write abbreviations as they should appear (PAWP, SVR, IVC); the app pronounces them.
- **Accuracy:** every fact, number and trial result must be true and current (2024–2026 guidelines where they exist: ESC 2021/2023 heart failure, SCAI 2022 shock stages, ASE 2015/2025 chamber and RA pressure guidance, AHA/ESC 2025 where relevant). Prefer the card's figure when it is right; if the card is wrong or outdated, teach the right fact, say briefly what NEET keys if they key the old one, and add a `card_flags` entry. Check doubtful facts on the web (prefer WebFetch of guideline pages and PubMed abstracts; web search budget is shared and limited). An independent checker will review everything after you.

## Echo model (section P12-104 and any echo step)
Echo basics are taught here, for the first and only full time in the cardiology series. Each echo step carries a `model` object that drives a 3D model beside the lesson. Fields: `view` (PLAX, PSAX-PM, PSAX-AV, PSAX-MV, PSAX-AP, A4C, A5C, A2C, SUB4C, SUBIVC, LUNG, EFAST-RUQ, EFAST-LUQ, EFAST-PELVIS), `turn` and `tilt` (degrees, usually 0), `camera` (front, left, feet, probe), `show` (subset of chest, lungs, liver, labels), `path` (normal, effusion, tamponade, rv-dilated, lv-poor, hyperdynamic, hypovolaemia, ivc-plethoric, ivc-collapsing, pneumothorax, pleural-effusion), `phase` (play, systole, diastole), `mmode` (none, EPSS, TAPSE, MAPSE, IVC), `highlight` (list of RV, LV, RA, LA, Ao, DAo, LVOT, IVC, septum, pericardium). Start the lesson with an on-screen box that says what the model shows, e.g. `{{**Model:** parasternal long axis, probe at the left sternal edge, marker to the right shoulder.}}`. Teach only what NEET needs: views, what each shows in shock, the IVC and RA pressure numbers, the FATE goals, the normal Doppler values at the end.

## Drill (end of the packet)
15–25 tap-to-reveal items covering the highest-value facts of the whole packet: numbers and cut-offs, X-versus-Y discriminators, and the exact ways NEET asked them. Each `q` is short and answerable in your head; each `a` is one or two lines. Weight by `bank_questions`.

## New cards
Only if NEET (a bank line or a GT) asked a fact that no card in the pack answers. Shape: `{ "code": "V12-0nn", "deck": "CVS03", "topic": "…", "tier": "S", "q": "…", "a": ["3 to 8 lines"], "why": "the bank question it answers" }`. Number from V12-001. Most packets need none.

## Done means
- Valid JSON at `/home/claude/p12/S1_draft.json`, every section and step of the pack present in order, every lesson within the caps.
- Report back in under 300 words: total spoken minutes (about 14 spoken characters a second), the traps and mimics you collected (count), any card flags, anything you could not verify.
