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
    if isinstance(e.get('step'), int): x['step'] = e['step']
    return x

cards = {k: v2(e) for k, e in L.items()}
topups = []
for t in ns['TOPUPS']['TOX01']:
    t = dict(t); t['x'] = v2(T[t['id']])
    topups.append(t)
decks = {'TOX01': {'cards': cards, 'topups': topups}}
# T-083: the other Toxicology decks (main cards only; their few bank Top-ups are not explained yet)
import os
for dk in ['TOX02', 'TOX03A', 'TOX03B', 'TOX04', 'TOX05', 'TOX06', 'RESP01A', 'RESP01B', 'RESP01C', 'RESP02A', 'RESP02B', 'RESP03', 'RESP04', 'RESP05', 'RESP06A', 'RESP06B', 'RESP07A', 'RESP07B']:
    f = dk.lower() + '_learn.py'
    if not os.path.exists(f): print('skip', dk); continue
    n2 = {}; exec(open(f).read(), n2)
    decks[dk] = {'cards': {k: v2(e) for k, e in n2['L'].items()}, 'topups': []}
    # T-088: the deck's story — spine steps and a primer for arriving cold
    if n2.get('SPINE'): decks[dk]['spine'] = [list(p) for p in n2['SPINE']]
    if n2.get('PRIMER'): decks[dk]['primer'] = n2['PRIMER']
# T-084: approved corrections to the card text, shown on the card and in the Explain pane
n3 = {}; exec(open('tox_corrections.py').read(), n3)
for dk, m in n3['FIX'].items():
    for code, items in m.items():
        assert code in decks[dk]['cards'], (dk, code)
        decks[dk]['cards'][code]['fix'] = [list(p) for p in items]
out = {'v': 2, 'decks': decks, 'patterns': ns['PATTERNS']}
s = json.dumps(out, ensure_ascii=False, sort_keys=True)
out['version'] = hashlib.sha1(s.encode()).hexdigest()[:10]
dest = sys.argv[1] if len(sys.argv) > 1 else 'explain.json'
json.dump(out, open(dest, 'w'), ensure_ascii=False, indent=1)
print('written', dest, out['version'], {k: len(v['cards']) for k, v in decks.items()}, 'topups', len(topups))
