# Builds the readable "Study desk" files (one per deck + 00 INDEX) from the same data the app uses.
import json, re, os, glob, sys
OUT = 'studydesk'
L = json.load(open('library.json'))['decks']
Q = json.load(open('/home/claude/trace/test/data/qbank.json'))
X = json.load(open('/home/claude/trace/test/data/explain.json'))['decks']
meta = {d['deck']: d for d in L}
def clean(t): return re.sub(r'\n{2,}', '\n', (t or '').replace('\r', '')).strip()
def xblock(x):
    o = []
    if x.get('intro'): o.append("**What's going on:** " + x['intro'])
    for l, t in x.get('why', []): o.append(f"- **{l}** {t}")
    if x.get('table'):
        tb = x['table']; o += ['', f"*{tb.get('title','')}*", '', '| ' + ' | '.join(tb['head']) + ' |', '|' + '---|' * len(tb['head'])] + ['| ' + ' | '.join(r) + ' |' for r in tb['rows']]
    if x.get('mimic'): o += ['', '**Close mimics:**'] + [f"- {a} — {b}" for a, b in x['mimic']]
    if x.get('traps'): o += ['', '**Exam traps:**'] + [f"- {a} is wrong. {b}" for a, b in x['traps']]
    if x.get('decode'): o += ['', '**How it is asked:**'] + [f"- {a} → {b}" for a, b in x['decode']]
    if x.get('punch'): o += ['', f"**Punchline:** {x['punch']}"]
    if x.get('parts'): o += ['', '**Exam add-ons:**'] + [f"- {p['q']} — {p['a']}" for p in x['parts']]
    return '\n'.join(o)
os.makedirs(OUT, exist_ok=True)
index = []
for f in sorted(glob.glob('cards/*.jsonl')):
    deck = os.path.basename(f)[:-6]; m = meta.get(deck, {}); sysname = m.get('system', ''); title = m.get('title', deck)
    cards = []
    for l in open(f):
        try: cards.append(json.loads(l))
        except Exception: pass
    xd = X.get(deck, {}); xc = xd.get('cards', {}); explained = bool(xc)
    o = [f"# {deck} — {title}", f"System: {sysname} · {len(cards)} cards · Explanations: {'written (Learn version)' if explained else 'not yet written — explain from the card and the extra exam lines'}", '']
    extra = []
    for c in cards:
        code = c.get('code', ''); sec = c.get('section', '')
        o.append(f"## {code} · {deck} · {sysname.split(' ',1)[-1] if sysname else ''} › {sec}")
        o.append("**Question:**\n" + clean(c.get('q')))
        o.append("\n**Card answer:**\n" + clean(c.get('a')))
        if c.get('watch'): o.append('\n' + clean(c['watch']).replace('**WATCH**', '**WATCH:**'))
        qb = Q['cards'].get(deck + '|' + code) or {}
        if qb.get('chips'): o.append('\nAsked in: ' + ', '.join(f"{ch['t']}{' ×'+str(ch['n']) if ch.get('n',1)>1 else ''}" for ch in qb['chips']))
        if qb.get('fix'): o.append('\n**Checked correction:** ' + ' '.join(fx.get('t', '') for fx in qb['fix']))
        if code in xc: o.append('\n### Explanation\n' + xblock(xc[code]))
        elif qb.get('lines') or qb.get('cross'):
            o.append('\n**Extra exam lines (not yet cards):**'); o += [f"- {ln}" for ln in (qb.get('lines') or []) + (qb.get('cross') or [])]
        o.append('')
    tus = xd.get('topups') if explained and xd.get('topups') else None
    if tus:
        o.append(f"# {deck} Top-up cards (from DocT, GTs, Marrow)\n")
        for i, t in enumerate(tus):
            o.append(f"## TU-{i+1:02d} · {deck} › {t['topic']}"); o.append("**Question:**\n" + clean(t['q'])); o.append("\n**Card answer:**\n" + '\n'.join(t['a']))
            if t.get('x'): o.append('\n### Explanation\n' + xblock(t['x']))
            o.append('')
    else:
        tq = Q['topups'].get(deck) or []
        if tq:
            o.append(f"# {deck} Top-up questions (from DocT, GTs, Marrow — not yet rebuilt)\n")
            for t in tq:
                o.append(f"## {deck} Top-up › {t.get('topic','')}"); o.append("**Question:** " + clean(t.get('q'))); o.append('**Answer:**\n' + '\n'.join('- ' + a for a in t.get('a', []))); o.append('')
    name = f"{deck} — {title}".replace('/', '-')
    open(os.path.join(OUT, name + '.md'), 'w').write('\n'.join(o))
    first, last = (cards[0].get('code', ''), cards[-1].get('code', '')) if cards else ('', '')
    index.append((sysname, deck, title, len(cards), first, last, explained, name))
ix = ["# 00 INDEX — Trace Study desk", "One file per deck, named '<DECK> — <title>'. Every card starts with a heading '## <CARD-ID> · <DECK> · <system> › <section>'.",
      "To answer about a card: find its CARD-ID here (the code prefix and range tell you the deck), open that deck's file, read the card, then search other decks for related cards and cite their CARD-IDs.", "",
      "| System | Deck | Title | Cards | Card IDs | Explanations | File |", "|---|---|---|---|---|---|---|"]
for r in sorted(index): ix.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} – {r[5]} | {'✓' if r[6] else 'pending'} | {r[7]} |")
open(os.path.join(OUT, '00 INDEX.md'), 'w').write('\n'.join(ix))
tot = sum(os.path.getsize(p) for p in glob.glob(OUT + '/*.md'))
print(len(index), 'decks', round(tot / 1e6, 2), 'MB')
