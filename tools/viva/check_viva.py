"""Checks a viva package file before it ships (spec: claude/Trace_Viva_File_Spec_7Nov.md, section 9).
Usage: python3 tools/viva/check_viva.py data/viva/P4.json data/viva/img/P4/ <cards dir with DECK.jsonl> [data/cardfix.json]
Exit code 1 when anything fails; warnings do not fail."""
import json,os,re,sys
P=json.load(open(sys.argv[1])); imgdir=sys.argv[2].rstrip('/')+'/'; CARDS=sys.argv[3]; FIX=sys.argv[4] if len(sys.argv)>4 else None
cards={}
for f in [x for x in os.listdir(CARDS) if x.endswith('.jsonl')]:
    for l in open(os.path.join(CARDS,f)):
        if not l.strip(): continue
        c=json.loads(l); cards[c['deck']+'|'+c['code']]=c
fix=json.load(open(FIX))['cards'] if FIX else {}
for k,v in fix.items():
    for fl,t in v['fields'].items(): cards[k]=dict(cards[k],**{fl:t})
decks={k.split('|')[0] for k in cards}
err=[];warn=[]
for k,c in P['cards'].items():
    if not re.fullmatch(r'V'+P['package'][1:]+r'-\d{3}',k): err.append(f'bad code {k}')
    if c['deck'] not in decks: err.append(f'{k} deck {c["deck"]}')
    if not 3<=len(c['a'])<=8: err.append(f'{k} a len {len(c["a"])}')
    for l in c['a']:
        if len(l)>300: err.append(f'{k} line {len(l)}')
    if len(c['topic'])>70: err.append(f'{k} topic len')
    if c['tier'] not in 'SAB': err.append(f'{k} tier')
    if c.get('pic') and not os.path.exists(imgdir+c['pic']): err.append(f'{k} pic')
    for t in c['a']+[c['q']]:
        if 'TODO' in t or 'Card error' in t or 'correction box' in t: warn.append(f'{k}: {t[:90]}')
for k in P['lines']:
    if k not in cards: err.append(f'line card {k}')
qs=set()
for q in P['questions']:
    if q['q'] in qs: err.append('dup q '+q['q'])
    qs.add(q['q'])
    if not 1<=len(q['steps'])<=8: err.append(f'{q["q"]} steps {len(q["steps"])}')
    if not 4<=len(q['spine'])<=6: err.append(f'{q["q"]} spine {len(q["spine"])}')
    if q['steps'][-1]['bridge'] is not None: warn.append(f'{q["q"]} last bridge not null')
    for s in q['steps']:
        if s['card'] not in cards and s['card'] not in P['cards']: err.append(f'{q["q"]} card {s["card"]}')
        b=s['bridge']
        if b and len(b)>160: warn.append(f'{q["q"]} {s["card"]} bridge {len(b)}')
    for l in q['spine']:
        if len(l)>200: warn.append(f'{q["q"]} spine line {len(l)}')
for k,e in P['explain'].items():
    if k not in cards and k not in P['cards']: err.append('explain key '+k)
    if len(e['intro'])>600: warn.append(f'explain {k} intro {len(e["intro"])}')
    if e.get('pic'):
        if not os.path.exists(imgdir+e['pic']): err.append(f'explain {k} pic {e["pic"]}')
        if not e.get('cap'): err.append(f'explain {k} no cap')
    for lab,t in e['why']:
        if re.search(r'card error|Card error|correction',t): warn.append(f'explain {k}: {t[:100]}')
for f in P['fixes']:
    c=cards.get(f['card'])
    if not c: err.append('fix card '+f['card']); continue
    n=c.get(f['field'],'').count(f['old'])
    if n!=1: err.append(f'fix {f["card"]} {f["field"]} old count {n}: {f["old"][:60]}')
print('ERRORS',len(err)); print('\n'.join(err)); print('WARN',len(warn)); print('\n'.join(warn))
sys.exit(1 if err else 0)
