#!/usr/bin/env python3
"""
trace_validate.py — checks a staged Trace visual-deck version before it goes live.

Usage:
    python3 trace_validate.py <visual folder> <cards.jsonl> [--version N]

<visual folder> is a local copy of  My Drive › Trace › decks › <DECK> › visual
(current.json, images/, versions/v1/, v2/ …). Without --version the newest version folder is checked.
<cards.jsonl> is the deck's card file (My Drive › Trace › decks › <DECK> › cards.jsonl).

Writes versions/v<N>/validation.json with "result": "pass" or "fail" and the exact problems,
and prints the same. Only switch current.json when the result is "pass".

The phrase rules here are the same ones the Trace app uses on every device:
  * the card text is re-flowed exactly as the screen shows it;
  * ** and * marks are ignored, any run of white space counts as one space, capitals must match;
  * parts:  heading = the first line(s) of q before the first sub-part, without a final ":";
            a, b, c … = the lettered sub-part lines;  li1, li2 … = the nth "- " list line in that field;
            whole = the whole field (for q: everything after the heading).
"""
import csv, io, json, os, re, sys

SOFT = '\u2028'
SUB_B = re.compile(r'^\s*\*\*([a-h])[.)]?\*\*\s+(.*)$')
SUB_P = re.compile(r'^\s*([a-h])[.)]?\s+(?=[A-Z0-9*(“"\'≥≤<>])(.*)$')
CONT_START = re.compile(r'^[a-z0-9(\[→←↑↓–\-/,;:%+×=<>≥≤~&·]')
CAPS_WORD = re.compile(r'^[A-Z]{2,}[A-Z0-9\'\-]*\b')
OPEN_END = re.compile(r'([,(\-–/+&→←]|\b(the|a|an|and|or|of|to|with|for|in|on|by|at|from|than|as|is|are|be|if|vs|via|per|not|no|THE|OF|AND|OR|TO|WITH|FOR|IN|ON|BY|AT|AS|IS|NOT|NO))$')


def sub_match(l):
    return SUB_B.match(l) or SUB_P.match(l)


def plain(s):
    s = (s or '').replace('**', '')
    return re.sub(r'(^|[^*])\*([^*]+)\*', r'\1\2', s)


def is_row(l):
    return ' | ' in l or re.search(r'\s\|$', l) is not None


def reflow(md):
    out = []
    for raw in (md or '').split('\n'):
        l = raw.rstrip()
        if re.search(r'\s\|$', l):
            l += ' '
        if not l.strip():
            out.append('')
            continue
        bare = plain(l).strip()
        prev = out[-1] if out else None
        starts_cont = bool(CONT_START.match(bare))
        marker = sub_match(l) or re.match(r'^\s*[-•]\s+', l) or (is_row(l) and not starts_cont)
        if prev is not None and not marker and prev.strip():
            pb = plain(prev.split(SOFT)[-1]).strip()
            prev_open = not re.search(r'[.:!?]$', pb)
            if starts_cont or (prev_open and (CAPS_WORD.match(bare) or OPEN_END.search(pb))):
                out[-1] = prev.rstrip() + ' ' + l.strip()
                continue
            if prev_open and not is_row(prev):
                out[-1] = prev + SOFT + l.strip()
                continue
        out.append(l)
    return '\n'.join(out)


def split_q(q):
    head, rest, in_rest = [], [], False
    for l in (q or '').split('\n'):
        if not in_rest and (sub_match(l) or re.search(r' \| ', l) or re.match(r'^\s*[-•]\s', l)):
            in_rest = True
        (rest if in_rest else head).append(l)
    return re.sub(r'\s+', ' ', ' '.join(head)).strip(), reflow('\n'.join(rest))


def norm(s):
    return re.sub(r'\s+', ' ', (s or '').replace('*', '').replace(SOFT, ' ')).strip()


def card_parts(c, field):
    out = {}
    if field == 'q':
        head, body = split_q(c.get('q', ''))
        out['heading'] = norm(re.sub(r':$', '', plain(head)))
    else:
        body = reflow(c.get(field) or '')
    li, whole, segs = 0, [], []
    lines = body.split('\n')
    def is_tbl(i):
        return 0 <= i < len(lines) and ' | ' in lines[i] and not re.match(r'^\s*[-•]\s+', lines[i])
    # same order as the app's renderer: bullets, then table rows (2+ in a run), then sub-parts / plain lines
    for i, l in enumerate(lines):
        if not l.strip():
            continue
        if is_tbl(i) and (is_tbl(i - 1) or is_tbl(i + 1)):
            whole.append(' '.join(l.split(' | '))); segs.extend(norm(x) for x in l.split(' | ') if norm(x)); continue
        if re.match(r'^\s*[-•]\s+', l):
            li += 1
            out['li%d' % li] = norm(re.sub(r'^\s*[-•]\s+', '', l)); whole.append(out['li%d' % li]); segs.append(out['li%d' % li]); continue
        m = sub_match(l)
        if m and m.group(2):
            out[m.group(1)] = norm(m.group(2)); whole.append(m.group(2)); segs.append(out[m.group(1)]); continue
        whole.append(' '.join(l.split(' | ')))
        segs.extend(norm(x) for x in l.split(' | ') if norm(x))
    out['whole'] = norm(' '.join(whole))
    return out, segs


def count_in(hay, needle):
    n, i = 0, 0
    while True:
        i = hay.find(needle, i)
        if i < 0:
            return n
        n += 1; i += len(needle)


def read_csv(path, required=True):
    if not os.path.exists(path):
        if required:
            raise FileNotFoundError(os.path.basename(path))
        return []
    with open(path, encoding='utf-8-sig', newline='') as f:
        return [{k.strip(): (v or '').strip() for k, v in r.items() if k} for r in csv.DictReader(f) if any((v or '').strip() for v in r.values())]


def validate(visual, cards_path, version=None):
    errors, warnings, info = [], [], {}
    vers = os.path.join(visual, 'versions')
    nums = sorted(int(d[1:]) for d in os.listdir(vers) if re.fullmatch(r'v\d+', d))
    if not nums:
        return {'result': 'fail', 'errors': ['no versions/v<N> folder'], 'warnings': []}, None
    v = version or nums[-1]
    vd = os.path.join(vers, 'v%d' % v)
    cards = [json.loads(l) for l in open(cards_path, encoding='utf-8') if l.strip()]
    by_code = {c['code']: c for c in cards}
    deck = cards[0]['deck'] if cards else '?'
    try:
        manifest = json.load(open(os.path.join(vd, 'manifest.json'), encoding='utf-8'))
    except Exception as e:
        manifest = {}; errors.append('manifest.json: %s' % e)
    if manifest and manifest.get('deck') != deck:
        errors.append('manifest.json deck "%s" is not the card file deck "%s"' % (manifest.get('deck'), deck))
    if manifest and manifest.get('version') != v:
        errors.append('manifest.json version %s is not the folder v%d' % (manifest.get('version'), v))
    try:
        scenes = read_csv(os.path.join(vd, 'scenes.csv')); seqrows = read_csv(os.path.join(vd, 'sequences.csv'))
        links = read_csv(os.path.join(vd, 'links.csv')); cues = read_csv(os.path.join(vd, 'cues.csv'))
        hotspots = read_csv(os.path.join(vd, 'hotspots.csv'), False); notes = read_csv(os.path.join(vd, 'notes.csv'), False)
        stories = json.load(open(os.path.join(vd, 'stories.json'), encoding='utf-8'))
    except FileNotFoundError as e:
        return {'result': 'fail', 'errors': ['missing file %s' % e], 'warnings': []}, vd
    imgdir = os.path.join(visual, 'images')
    present = set(os.listdir(imgdir)) if os.path.isdir(imgdir) else set()

    sc = {}
    for s in scenes:
        if s['scene_id'] in sc: errors.append('scenes.csv: duplicate scene_id %s' % s['scene_id'])
        sc[s['scene_id']] = s
        if s.get('kind') not in ('overview', 'detail'): errors.append('scenes.csv: %s kind "%s" must be overview or detail' % (s['scene_id'], s.get('kind')))
        if s.get('card_code') not in by_code: errors.append('scenes.csv: %s card_code %s is not in the deck' % (s['scene_id'], s.get('card_code')))
        if not re.fullmatch(r'[a-z0-9\-]+\.(webp|png)', s.get('image', '')): errors.append('scenes.csv: %s image name "%s" must be lowercase letters, digits, hyphens + .webp/.png' % (s['scene_id'], s.get('image')))
        if s.get('image') not in present: errors.append('scenes.csv: %s image %s is missing from images/' % (s['scene_id'], s.get('image') or '(blank)'))
    seqs = {}
    for r in seqrows:
        if r['scene_id'] not in sc: errors.append('sequences.csv: %s uses unknown scene %s' % (r['sequence_id'], r['scene_id']))
        seqs.setdefault(r['sequence_id'], []).append(r)
    for sid, rows in seqs.items():
        try: o = sorted(int(r['order']) for r in rows)
        except ValueError: o = []
        if o != list(range(1, len(rows) + 1)): errors.append('sequences.csv: %s order must run 1..%d without gaps or repeats' % (sid, len(rows)))
    need_ov = set()
    for i, r in enumerate(links, start=2):
        where = 'links.csv row %d' % i
        c = by_code.get(r.get('card_code'))
        if not c: errors.append('%s: card_code %s is not in the deck' % (where, r.get('card_code'))); continue
        need_ov.add(r['card_code'])
        if r.get('sequence_id') not in seqs: errors.append('%s: unknown sequence %s' % (where, r.get('sequence_id')))
        if r.get('field') not in ('q', 'a', 'why', 'watch'): errors.append('%s: field "%s" must be q, a, why or watch' % (where, r.get('field'))); continue
        if r.get('part') == 'heading':
            errors.append('%s: the heading opens the overview by itself; link a sub-part, list line or phrase instead' % where); continue
        parts, segs = card_parts(c, r['field']); text = parts.get(r.get('part'))
        if text is None: errors.append('%s: %s %s has no part "%s" (has %s)' % (where, r['card_code'], r['field'], r.get('part'), ', '.join(parts))); continue
        if not r.get('phrase'): continue
        ph = norm(r['phrase']); occ = r.get('occurrence') or ''
        n = sum(count_in(x, ph) for x in segs) if r['part'] == 'whole' else count_in(text, ph)
        if n == 0 and r['part'] == 'whole' and count_in(text, ph):
            errors.append('%s: phrase "%s" runs across two lines or cells of %s %s; link it within one line' % (where, r['phrase'], r['card_code'], r['field'])); continue
        if n == 0: errors.append('%s: phrase "%s" not found in %s %s/%s: "%s"' % (where, r['phrase'], r['card_code'], r['field'], r['part'], text))
        elif n > 1 and not (occ.isdigit() and 1 <= int(occ) <= n): errors.append('%s: AMBIGUOUS — "%s" appears %d× in %s %s/%s; set occurrence 1..%d' % (where, r['phrase'], n, r['card_code'], r['field'], r['part'], n))
        elif n == 1 and occ and occ != '1': errors.append('%s: occurrence %s but the phrase appears once' % (where, occ))
    for i, h in enumerate(hotspots, start=2):
        where = 'hotspots.csv row %d' % i; s = sc.get(h.get('overview_id'))
        if not s or s.get('kind') != 'overview': errors.append('%s: %s is not an overview scene' % (where, h.get('overview_id')))
        else: need_ov.add(s['card_code'])
        if h.get('sequence_id') not in seqs: errors.append('%s: unknown sequence %s' % (where, h.get('sequence_id')))
        try:
            x, y, w, hh = (float(h[k]) for k in ('x', 'y', 'w', 'h'))
            if x < 0 or y < 0 or w <= 0 or hh <= 0 or x + w > 100.001 or y + hh > 100.001: raise ValueError
        except Exception: errors.append('%s: box %s,%s,%s,%s must lie inside 0–100' % (where, h.get('x'), h.get('y'), h.get('w'), h.get('h')))
    for code in sorted(need_ov):
        if not any(s.get('kind') == 'overview' and s.get('card_code') == code for s in scenes): errors.append('%s has links or hotspots but no overview scene' % code)
    for i, r in enumerate(cues, start=2):
        if r.get('scene_id') not in sc: errors.append('cues.csv row %d: unknown scene %s' % (i, r.get('scene_id')))
    for i, r in enumerate(stories, start=1):
        if r.get('scene_id') not in sc: errors.append('stories.json item %d: unknown scene %s' % (i, r.get('scene_id')))
    for i, r in enumerate(notes, start=2):
        where = 'notes.csv row %d' % i
        if r.get('card_code') not in by_code: errors.append('%s: card_code %s is not in the deck' % (where, r.get('card_code')))
        if r.get('level') not in ('card', 'scene'): errors.append('%s: level must be card or scene' % where)
        if r.get('level') == 'scene' and r.get('scene_id') not in sc: errors.append('%s: unknown scene %s' % (where, r.get('scene_id')))
        if r.get('kind') not in ('correction', 'qualification', 'update'): errors.append('%s: kind must be correction, qualification or update' % where)
    # images: every listed image opens; size recorded; >2 MB is a warning
    sizes = {}
    for name in sorted(set(manifest.get('images', [])) | {s.get('image') for s in scenes if s.get('image')}):
        p = os.path.join(imgdir, name)
        if not os.path.exists(p): errors.append('image %s listed but not in images/' % name); continue
        b = os.path.getsize(p); px = None
        try:
            from PIL import Image
            with Image.open(p) as im: im.verify()
            with Image.open(p) as im: px = '%dx%d' % im.size
        except ImportError: pass
        except Exception as e: errors.append('image %s does not open: %s' % (name, e))
        sizes[name] = {'bytes': b, 'pixels': px}
        if b > 2 * 1024 * 1024: warnings.append('image %s is %.1f MB (over 2 MB — fine if needed, mention it in manifest.json)' % (name, b / 1048576))
    # the previous live version must still have all its images
    try:
        cur = json.load(open(os.path.join(visual, 'current.json'), encoding='utf-8'))
        pv = cur.get('live_version')
        if pv and pv != v:
            pm = json.load(open(os.path.join(vers, 'v%d' % pv, 'manifest.json'), encoding='utf-8'))
            gone = [n for n in pm.get('images', []) if n not in present]
            if gone: errors.append('live version v%d images missing from images/: %s' % (pv, ', '.join(gone)))
    except FileNotFoundError: pass
    except Exception as e: warnings.append('could not check the live version: %s' % e)
    info = {'deck': deck, 'version': v, 'counts': {'overview': sum(s.get('kind') == 'overview' for s in scenes), 'detail': sum(s.get('kind') == 'detail' for s in scenes),
            'sequences': len(seqs), 'links': len(links), 'hotspots': len(hotspots), 'cues': len(cues), 'stories': len(stories), 'notes': len(notes)}, 'images': sizes}
    return {'result': 'fail' if errors else 'pass', 'errors': errors, 'warnings': warnings, **info}, vd


if __name__ == '__main__':
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    ver = None
    if '--version' in sys.argv:
        ver = int(sys.argv[sys.argv.index('--version') + 1]); args = [a for a in args if a != str(ver)]
    if len(args) != 2:
        print(__doc__); sys.exit(2)
    rep, vd = validate(args[0], args[1], ver)
    if vd:
        with open(os.path.join(vd, 'validation.json'), 'w', encoding='utf-8') as f: json.dump(rep, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: rep[k] for k in ('result', 'errors', 'warnings') if k in rep}, ensure_ascii=False, indent=1))
    sys.exit(0 if rep['result'] == 'pass' else 1)
