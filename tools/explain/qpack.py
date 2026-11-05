# Usage: python3 qpack.py DECK  → explain/qpack/<DECK>.md : every real question linked to each card of the deck
import csv, glob, json, re, sys, collections
deck = sys.argv[1]; M = '/home/claude/map/'
cards = [json.loads(l) for l in open(M + f'cards/{deck}.jsonl')]
codes = [c['code'] for c in cards]
full = {}
for f in ['doct_qbank_all.jsonl', 'doct_gt_distinct_all.jsonl']:
    for l in open(M + f):
        try: o = json.loads(l)
        except Exception: continue
        full.setdefault(o['mcq_id'], o)
for o in json.load(open(M + 'pilot_doct_ards.json')): full.setdefault(o['mcq_id'], o)
hits = collections.defaultdict(list); seen = set()
def take(src, r):
    cs = re.findall(r'[A-Z][A-Z0-9]*-\d+', r.get('card') or '')
    for code in cs:
        if code in codes and (code, r.get('mcq_id'), src) not in seen:
            seen.add((code, r.get('mcq_id'), src)); hits[code].append((src, r))
for f in sorted(glob.glob(M + 'out/doct_map_*_v2.csv')) + [M + 'out/pilot_ARDS_doct_map.csv']:
    for r in csv.DictReader(open(f)): take('DocT QBank', r)
for f in sorted(glob.glob(M + 'out/gt_map_*.csv')) + sorted(glob.glob(M + 'out/gt2_map_*.csv')):
    for r in csv.DictReader(open(f)): take('NEET 2025 recall' if 'Recall25' in f else 'DocT GT · ' + r.get('module', ''), r)
for r in csv.DictReader(open(M + 'QMap_full_932.csv')): take('Marrow QBank', r)
for r in csv.DictReader(open(M + 'explain/neet2024_resp.csv')): r['stem'] = r['question']; r['mcq_id'] = r['rid']; take('NEET 2024 recall', r)
out = [f'# {deck}: real questions linked to each card', '']
for c in cards:
    hs = hits.get(c['code'], [])
    out.append(f"## {c['code']} · {c['q'].splitlines()[0].strip('* ')} — {len(hs)} questions"); out.append('')
    for src, r in hs:
        o = full.get(r.get('mcq_id'), {})
        stem = (o.get('stem') or r.get('stem') or r.get('stem_short') or '').replace('\n', ' ')
        pct = r.get('cohort_pct') or o.get('cohort_pct')
        out.append(f"- **[{src}]** {stem}")
        if o.get('options'): out.append(f"  - Options: {o['options']}")
        out.append(f"  - Answer: {r.get('answer') or o.get('answer')}" + (f" · cohort right {pct}%" if pct not in (None, '', '0', 0) else ''))
        for k in ('line', 'key_note', 'pattern', 'note', 'topic'):
            if r.get(k): out.append(f"  - {k}: {r[k][:400]}")
    out.append('')
open(M + f'explain/qpack/{deck}.md', 'w').write('\n'.join(out))
print(deck, {k: len(v) for k, v in hits.items()}, 'total', sum(len(v) for v in hits.values()))
