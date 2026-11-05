# Builds trace/test/data/explain.json — Explain v2 (T-070): TOX01 only, Learn/Revise, no deck map/close, no hooks.
import json, sys, hashlib, io, contextlib
ns = {}
old_argv = sys.argv; sys.argv = ['x', '/dev/null']
with contextlib.redirect_stdout(io.StringIO()):
    exec(open('build_explain.py').read(), ns)          # pilot data: TOPUPS (card text of the rebuilt Top-ups), PATTERNS
sys.argv = old_argv
exec(open('tox01_learn.py').read(), ns)               # L: main cards
exec(open('tox01_topups_learn.py').read(), ns)        # T: Top-ups
L, T = ns['L'], ns['T']

def v2(e, topup=False):
    x = {'v': 2, 'sub': e.get('sub', ''), 'intro': e['intro'], 'why': [list(p) for p in e['parts']],
         'mimic': [list(p) for p in e.get('mimic', [])], 'traps': [list(p) for p in e.get('traps', [])],
         'decode': [list(p) for p in e.get('decode', [])], 'punch': e['punch']}
    if e.get('table'): x['table'] = e['table']
    if e.get('extra'): x['parts'] = e['extra']
    if e.get('before'): x['before'] = e['before']
    if topup: x['topup'] = True
    return x

cards = {k: v2(e) for k, e in L.items()}
topups = []
for t in ns['TOPUPS']['TOX01']:
    t = dict(t); t['x'] = v2(T[t['id']])
    topups.append(t)
out = {'v': 2, 'decks': {'TOX01': {'cards': cards, 'topups': topups}}, 'patterns': ns['PATTERNS']}
s = json.dumps(out, ensure_ascii=False, sort_keys=True)
out['version'] = hashlib.sha1(s.encode()).hexdigest()[:10]
dest = sys.argv[1] if len(sys.argv) > 1 else 'explain.json'
json.dump(out, open(dest, 'w'), ensure_ascii=False, indent=1)
print('written', dest, out['version'], 'cards', len(cards), 'topups', len(topups))
