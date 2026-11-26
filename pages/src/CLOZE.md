# Blanks (cloze): how they are written and checked

The recall switch on a study page covers chosen words in the notes; a tap uncovers one.
A blank is a question, so it is written and checked with the same care as a question. The first
GI and pancreatitis pages hid every bold word automatically. That produced blanks like
"amylase" hidden on a line about amylase, with the word printed on the line above. This file
replaces that habit.

Sources: P. Wozniak, *Twenty rules of formulating knowledge* (SuperMemo, 1999), rules 4, 5,
9–11, 14, 16–17; A. Matuschak, *How to write good prompts* (2020), on what makes a retrieval
prompt focused, precise, consistent, tractable and effortful, and on cloze pattern-matching.

## Markup

In content text: `{?answer?}`, or `{?answer|label?}` to print a gap label such as
`(number)`, `(drug)` or `(test)`. Wozniak's gap labels tell the reader what kind of thing is
missing without saying what it is. With recall off, the answer reads as ordinary bold text.

## The checklist: every blank must pass all of these

1. **It tests what the exam asks.** A blank goes on the cut-off, the drug, the test, the deciding
   finding or the trial, never on filler or on the obvious. Wozniak's rule 20 is to prioritise.
2. **One small fact per blank.** At most about four words. Two blanks per line at most, and only
   if the rest of the line still asks both questions (minimum information, rule 4).
3. **The open words ask a clear question.** Reading the line with the blank covered, you know
   exactly what is wanted. If not, add a gap label or a few words of context. This is
   Matuschak's "precise" and "tractable".
4. **Only one right answer.** If two drugs or two numbers could fill it, the context must rule one
   out. Matuschak: enough context to exclude the alternatives, not so much it gives the answer.
5. **No giveaway on the same screen.** The answer must not be printed anywhere else in the notes
   or visuals the reader can see with recall on. That includes the line above and below it, the
   diagram beside it and another blank's open text. A blank shown next to its own answer is not
   a recall item (Matuschak on cues; the amylase case).
6. **The blank's shape gives nothing away.** Every blank is the same width whatever its answer.
7. **Keep the frame.** Blank the number and keep the unit and the direction:
   "lactate over {?2.5?} mmol/L", not "{?lactate over 2.5 mmol/L?}".
8. **Lists keep their order; blank one member at a time.** Never blank a whole set (rules 9–10).
9. **Put blanks where mimics split.** Interference between similar facts is the biggest cause of
   forgetting (rule 11), so the row that separates two look-alikes deserves a blank more than a
   number nobody confuses.
10. **Ask the same high-value fact a second way where possible.** For example a blank in the
    notes and a tap-to-reveal question in the Cards tab (rule 17, and Matuschak on "multiple
    angles"). This keeps recall from becoming memory of a line's shape.

## How the page enforces it

- **The build measures.** For every blank it checks: the answer is short; there are no more than
  two blanks in a line; at least four open words remain in the line; and the answer does not
  appear anywhere else in the screen's visible notes (case-insensitive, whole words; numbers
  matched as whole numbers). A failure stops the build. A real exception is waived in the
  content file with a written reason.
- **Then a person reads it.** The build writes `recall-read.txt`: every concept as HT sees it
  with recall on. Each blank is read cold and gets two questions: *would I know what is being
  asked?* and *is there only one right answer?* Fix any blank that fails either before the page
  goes live.
- **On the page:** blanks are equal-width boxes with their gap label; one tap uncovers one;
  "Reveal all" and "Cover all again" reset a concept for the next round. With recall on, the
  tabs below the notes stay closed until tapped, so the cards and traps can't give answers
  away by accident.
