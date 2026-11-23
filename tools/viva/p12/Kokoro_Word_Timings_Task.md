# Task for the ChatGPT agent: word timings for the Michael (Kokoro) lesson clips

**Why.** Trace highlights each word as the lesson voice speaks it. The Iapetus clips come with word timings. The Michael (Kokoro) clips don't, so for now Trace spreads the highlight evenly across each clip. This task adds real timings.

## Where the clips are
- Google Drive › **Trace › voice-k**. One flat folder.
- **Clips:** `VIVA-P12__<key>.b64`. Each is a text file holding one MP3 as **base64**: mono, 24 kHz, 48 kb/s. Decode the base64 to get the MP3.
- **Index:** `VIVA-P12.kidx.json` is a JSON object:
  ```json
  { "<key>": { "id": "<Drive file id of the .b64>", "h": "<hash>", "sec": 13.3, "voice": "kokoro-am_michael" }, ... }
  ```
  It holds about 3,130 entries, about 16 hours of audio.

## What to make, for each index entry
1. Download the `.b64` file by its `id`, base64-decode it, and save it as an MP3.
2. Transcribe it with **word timestamps**, for example:
   - OpenAI Whisper with `word_timestamps=True`
   - faster-whisper with `word_timestamps=True`
   - whisper.cpp with `-ml 1`

   Use English. Any model is fine; `small` or larger is good.
3. Write a timing file into the **same voice-k folder**, named `VIVA-P12__<key>.t.json`, in exactly this format:
   ```json
   {"words":[["Now",0,520],["the",520,880],["card's",880,1580]],"dur":4220}
   ```
   - `words`: every heard word in order, as `[text, startMs, endMs]`. Times are integers in milliseconds from the start of the clip. Punctuation may be stripped from the word text.
   - `dur`: clip length in milliseconds (integer).
4. Add `"tid": "<Drive file id of that .t.json>"` to the entry for that key in `VIVA-P12.kidx.json`. Leave `id`, `h`, `sec` and `voice` exactly as they are.

## Rules
- **Only add `tid`.** Don't rename, move, delete or rewrite any `.b64` file, and don't remove or reorder index entries.
- **Save the index safely.** Re-read `VIVA-P12.kidx.json` from Drive just before each save, add your `tid`s to that fresh copy, then write it back. Trace may have added new clips in the meantime. Save every 100 clips and at the end.
- **Skip entries that are done:** any entry that already has a `tid`. You can stop and restart at any time.
- If a clip fails to download or transcribe, skip it and list it at the end.
- Leave any other files in the folder alone. The other packages' folders under Trace › voice are not part of this task.

## When finished
Report how many clips got timings, how many failed (with their keys), and the total audio processed. Trace picks up the timings by itself the next time the index loads. No app change is needed.
