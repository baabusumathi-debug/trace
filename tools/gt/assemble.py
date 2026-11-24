#!/usr/bin/env python3
"""Build test/data/gt/{index,GT7,GT8}.json from papers.json + out/classify.json + checked cards (out/final/*.json)."""
import json, glob, hashlib, os, sys
ROOT = '/home/claude/gt'
DEST = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/trace/test/data/gt'
P = json.load(open(f'{ROOT}/papers.json'))
CL = json.load(open(f'{ROOT}/out/classify.json'))
cards = {}
for f in sorted(glob.glob(f'{ROOT}/out/final/*.json')):
    cards.update(json.load(open(f)))
# before links both ways
for k, c in list(cards.items()):
    for ref in c.get('before') or []:
        r = cards.get(ref)
        if r is not None:
            r.setdefault('before', [])
            if k not in r['before']: r['before'].append(k)
os.makedirs(DEST, exist_ok=True)
index = {'version': '', 'papers': []}
FIELDS = ['links', 'before', 'answer', 'why', 'watch', 'hook', 'explain', 'options', 'picks_note', 'key', 'depth']
for g in ['7', '8']:
    src = P[g]; pid = 'GT' + g
    qs = []
    for q in src['questions']:
        c = CL.get(f'{pid}-{q["n"]}', {})
        qs.append({**q, 'sys': c.get('sys', ''), 'topic': c.get('topic', '')})
    cs = {}
    for n in src['need']:
        k = f'{pid}-{n}'
        if k in cards:
            cs[str(n)] = {f: cards[k][f] for f in FIELDS if f in cards[k]}
    out = {'id': pid, 'title': src['title'], 'date': src['date'], 'sections': src['sections'], 'q': qs, 'people': src['people'], 'cards': cs}
    s = json.dumps(out, ensure_ascii=False, separators=(',', ':'))
    ver = hashlib.sha1(s.encode()).hexdigest()[:10]
    out['version'] = ver
    open(f'{DEST}/{pid}.json', 'w').write(json.dumps(out, ensure_ascii=False, separators=(',', ':')))
    index['papers'].append({'id': pid, 'file': pid + '.json', 'version': ver, 'date': src['date'], 'cards': len(cs), 'need': len(src['need'])})
    print(pid, 'cards', len(cs), 'of', len(src['need']), 'version', ver)
index['version'] = hashlib.sha1(json.dumps(index['papers']).encode()).hexdigest()[:10]
open(f'{DEST}/index.json', 'w').write(json.dumps(index, separators=(',', ':')))
