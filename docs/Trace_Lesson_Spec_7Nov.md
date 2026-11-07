# Trace narrated lessons: file spec (7 Nov 2026)

How narrated lessons sit in a viva package file (`claude/viva/P4.json` and later packages). The writing rules are in `Viva_Lesson_Standard_7Nov.md`. The voice is Iapetus (Gemini), American English.

## 1. Where the keys sit

```json
{
  "package": "P4",
  "version": "P4.20261108.1",
  "questions": [
    {
      "q": "P4-005",
      "text": "What is driving pressure and why does it matter?",
      "open":  { "v": 1, "text": "Let me start with a puzzle.\n\nTwo patients with ARDS. ..." },
      "steps": [
        { "card": "RESP01B|ARDS-24", "bridge": "…",
          "lesson": { "v": 1, "text": "So let's begin with the screen.\n\n...\n\n[[What's left is only the stretch. That number is the plateau pressure.]]\n\n{{pic}}\n\n...", "pic": "P4_G1_three_layers.svg", "cap": "Peak, plateau, PEEP" } },
        { "card": "RESP01B|ARDS-26", "bridge": "…",
          "lesson": { "v": 2, "text": "...\n\n{{**Driving pressure = Pplat − PEEP = Vt ÷ Crs**}}\n\n[[Driving pressure is the plateau minus the PEEP.]] ..." } },
        { "card": "RESP01B|ARDS-25", "bridge": "…", "lesson": { "same": "P4-003" } }
      ],
      "close": { "v": 1, "text": "So let's bring it all together, slowly. ..." },
      "spine": ["…"]
    }
  ]
}
```

- `questions[i].open`: the opening lesson. Optional.
- `questions[i].steps[j].lesson`: the micro-lesson for that card in that question. Optional; if there is none, the card shows the Viva explanation as now.
- `questions[i].close`: the closing lesson. Optional.
- Nothing else in the file changes. `explain`, `bridge` and `spine` stay as they are.

## 2. A lesson object

| key | type | required | meaning |
|---|---|---|---|
| `v` | integer | yes | Lesson version. Start at 1 and add 1 on every edit. |
| `text` | string | yes | The script. Paragraphs are separated by a blank line (`\n\n`). |
| `pic` | string | no | File name in `data/viva/img/<pkg>/` (svg, png or webp). |
| `cap` | string | no | Picture caption, on screen only. |
| `same` | string | no | Instead of `text`: reuse the lesson of this card from another question (the question ID, e.g. `"P4-003"`). |

## 3. Markers inside `text`

- **`[[ … ]]` marks a takeaway.** Put it around one or two whole sentences. It may sit inside a paragraph. Never nest it.
- **`{{ … }}` marks on-screen-only text.** It must be a paragraph of its own. It is shown as a box when the voice reaches it and is never spoken. Bold (`**…**`) and simple `|` tables are allowed inside.
- **`{{pic}}` places the picture.** It is a paragraph of its own and shows the picture when the voice reaches it. Without `{{pic}}`, the picture sits at the top of the lesson.
- Everything else is spoken. Follow the written-for-the-ear rules: no symbols, arrows or card codes outside `{{ }}`. Pronunciation (PEEP, ARDS, SpO2, units) is handled by Trace's word list.

## 4. How takeaways reach the voice

Trace cuts each paragraph into runs at the `[[ ]]` marks, and each run becomes its own clip.

- A **plain run** is sent with the lesson style instruction:
  > Speak as a calm, composed senior consultant teaching one aspirant. Neutral American English accent. Unhurried, measured pace. Enunciate every word and medical term clearly; say numbers and units in full. Pause briefly after each sentence.
- A **takeaway run** is sent with the brackets stripped, and this line added to the same instruction:
  > This line is a key takeaway. Say it a little slower, with a clear, natural stress on the important words, and a short pause after it. Do not exaggerate or sound dramatic.

The marker itself is never sent. A separate request is used because Gemini's style instruction applies to the whole request. It is also safer, because instruction text placed inside the spoken text has been read out before (7 Nov).

On screen, takeaways show in bold, and the clips play back to back.

## 5. Caps (the checker enforces these)

| item | limit |
|---|---|
| `text` of any lesson | 150 to 4,000 characters, counting spoken text only. The checker warns above 3,000. A 30-second fact card is about 400 characters; a 3-minute lesson about 2,500–3,000. |
| One paragraph | 1,200 characters at most. |
| One takeaway | 300 characters at most. Takeaways may make up at most a quarter of a lesson's spoken text. |
| One `{{ }}` block | 400 characters at most. |
| Picture | 300 KB at most. |

The 600-character cap stays on `explain` intros only. It does not apply to lessons.

## 6. A card under several questions

Each question gets its own micro-lesson. Lessons carry the question's thread: bridges ("Now, the next question…"), running patients and teasers.

- If the card's lesson would be the same, write `"lesson": { "same": "P4-003" }`. Trace plays that lesson's clips; nothing new is made.
- Otherwise, write a short new lesson for the new question. It can open with "You met this card in driving pressure. Here's what matters for this question."

## 7. Playing

- In a viva walk, the order is: `open`, then each card's lesson (on that card), then `close`, then the next question's `open`.
- A **Lesson** tab sits beside **NEET | Viva** in the explanation. It is the default when a lesson exists, and the Viva explanation stays one tap away.
- When a step has a lesson, the written `bridge` stays on screen but is not spoken.
- **Autoplay / Tap to play** is a toggle on the Viva page, set per session. It starts on Tap to play.
  - In Autoplay, a lesson starts when its card opens, and Trace moves on 1.5 seconds after it ends.
  - In Tap to play, Trace waits for ▶.
- The speed setting (0.8× to 2×) is shared with card voice and remembered on the device.

## 8. Regenerating without losing history

- **Clip key:** `L-<q>-<slot>-<hash>`, where slot is `open`, `close` or `s<j>`, and hash is a short hash of the run text plus the voice and its style instruction. Clips are stored in Drive under `Trace › voice › VIVA-<pkg>`.
- **On an edit:** bump `v`. Only runs whose text changed get new hashes, so only they are made again. Unchanged runs keep their clips and cost nothing.
- **Old clips are never deleted or overwritten**, because a new hash means a new file name. They stay in Drive and in the index. Trace plays only the clips that match the current text.
- **Text history** is kept in the package file's git history, one commit per package version. The writer chat may also keep drafts in `claude/viva/lessons/`.
- **A voice change** gives new hashes for everything. The old voice's clips remain, so switching back is free.
- **Audio is made only when Naven says so**, from the deck page's Make voice button for the package. Trace shows how many minutes each package will make before it starts.
