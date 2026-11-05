# Usage: python3 check_learn.py DECK   — checks explain/<deck>_learn.py against cards/<DECK>.jsonl
import json, re, sys
deck = sys.argv[1]; f = f'/home/claude/map/explain/{deck.lower()}_learn.py'
ns = {}; exec(open(f).read(), ns); L = ns['L']
cards = [json.loads(l) for l in open(f'/home/claude/map/cards/{deck}.jsonl')]
let = lambda t: [m for m in re.findall(r'^(?:\*\*)?([a-h])(?:\*\*)?\s', t, re.M)]
bad = 0
def err(*a):
    global bad; bad += 1; print('ERR', *a)
for c in cards:
    e = L.get(c['code'])
    if not e: err(c['code'], 'missing'); continue
    for k in ('sub', 'intro', 'parts', 'mimic', 'traps', 'decode', 'punch'):
        if k not in e: err(c['code'], 'no field', k)
    la, lq = let(c['a']), let(c['q'])
    want = lq if len(lq) > len(la) else (la or lq)   # the question's letters win when the answer prints a part as a table
    got = [p[0] for p in e.get('parts', [])]
    if want and got != want: err(c['code'], 'letters', got, 'card has', want)
    # table cards (no letters): parts a, b, c… follow the table rows or topics in order
    for p in e.get('parts', []):
        if not p[1].startswith('**'): err(c['code'], p[0], 'part must start with the bold restated answer')
    txt = json.dumps(e, ensure_ascii=False).lower()
    for w in ('mnemonic', 'remember it as', 'hook:', 'think of it as'): 
        if w in txt: err(c['code'], 'banned phrase', w)
    if len(e.get('punch', '')) > 320: err(c['code'], 'punch too long')
    for t in e.get('traps', []) + e.get('mimic', []) + e.get('decode', []):
        if len(t) != 2: err(c['code'], 'pair not 2 items', t)
extra = set(L) - {c['code'] for c in cards}
if extra: err('entries not in deck', extra)
print(deck, len(cards), 'cards', len(L), 'entries', 'OK' if not bad else f'{bad} problems')
