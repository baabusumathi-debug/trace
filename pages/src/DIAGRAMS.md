# Diagrams: how they are checked before they go on a page

Two kinds of mistake reached the Shock I page on 24 Nov. Both had the same cause: each SVG
was written as coordinates in Python and **never looked at as a picture before it shipped**.
The old `check.py` measured page overflow and counted the reveals; it never opened a
drawing. Labels were placed by guessing coordinates, so some landed on lines, under pins or
past the edge. Sides were never read against the body, so the parasternal window went on the
patient's right and the subcostal view put the LV as near the probe as the RV.

## The two gates (both must pass)

1. **Measured — `diagcheck.py`.** Run it on the built page (`check.py` runs it for you).
   For every drawing on every screen, at phone and tablet widths, it measures in the browser:
   text on text, text running outside the drawing, text with a line running through it or
   lying across outlines (the drawing is re-rendered without its words and the edges under
   each label are counted), and page text laid over a drawing. On every screen it also checks
   page text on page text, for the pages whose visuals are built from HTML boxes. It writes a
   crop of each flagged drawing and exits non-zero. **Zero issues, or the page does not ship.**
   The checker was tested against a planted overlap, and it found every case found by eye on
   25 Nov.

2. **Read — this checklist, against a picture of every drawing.** The checker cannot know
   anatomy. Put every drawing on one sheet (`/home/claude/qa/allsvg.py` was the script) and
   read each one against the list below. Open the picture: reading the code is not enough.

## Anatomy checklist

**Any body drawing faces the viewer:** the patient's LEFT is on the viewer's RIGHT. Label the
two sides on chest drawings ("patient's RIGHT / LEFT").
- Heart sits mostly to the patient's left of the sternum.
- **Parasternal window:** LEFT sternal edge, 3rd–4th space.
- **Apical:** the apex beat, 5th space, mid-clavicular line, lower and lateral.
- **Subcostal:** under the xiphisternum.

**Echo views (as displayed on the screen):**
- **PLAX** (marker to the right shoulder): RV at the top (nearest), LV below it with the apex to the
  screen LEFT, aortic root and LA to the screen RIGHT, descending aorta behind the LA.
  Pericardial fluid tracks IN FRONT of the DAo, pleural fluid BEHIND it.
- **PSAX:** LV a circle in the middle, RV a crescent to the screen left/front. Pressure overload makes a D.
- **A4C** (probe at the apex, marker to the patient's left): apex at the top, RV screen LEFT,
  LV screen RIGHT, atria at the bottom (RA left, LA right).
- **Subcostal 4C:** liver at the top; the RIGHT heart (RA, RV) lies against the liver;
  the LEFT heart (LA, LV) is deeper. Atria to the screen left, apex to the screen right.
- **IVC (subcostal long axis, marker to the head):** liver above, IVC entering the RA on the
  screen right; measured 1–2 cm from the RA junction.

**Curves and traces:** a point said to be "on" a curve is computed from the curve, never typed
in. Axis names on the right axes. Labels sit beside the line they name, never on it.

**Lung and film:** Kerley B are short, horizontal and basal, running in from the pleura;
Kerley A are long, deep, and run toward the hila.

## Writing a new drawing

- Leave room for the words first: a label goes in clear space, or in a margin with a leader line.
- Numbered pins never sit on a word. Put the pin on the structure and the word beside it.
- Captions longer than about 60 characters go on two lines.
- Then run `check.py`, read the crops, read the sheet against this list, and only then build the page.
