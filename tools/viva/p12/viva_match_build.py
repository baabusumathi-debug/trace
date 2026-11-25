import json, collections, sys
P12=json.load(open('/home/claude/trace/data/viva/P12.json'))
V=json.load(open('viva_hits.json'))
ORDER=['P1','P2','P3','P4','P5','P6','P7','P8','P10','P11']
p12=collections.defaultdict(list)   # card -> [(q, i, gen, open)]
for q in P12['questions']:
    for i,s in enumerate(q['steps']):
        p12[s['card']].append(dict(q=q['q'],i=i,gen=q.get('gen'),t=(s.get('lesson') or {}).get('text','')[:150],len=len((s.get('lesson') or {}).get('text',''))))
viva=collections.defaultdict(list)
for q in sorted(V,key=lambda q:(ORDER.index(q['p']),q['q'])):
    for s in q['steps']:
        viva[s['card']].append(dict(p=q['p'],q=q['q'],qtext=q['text'],i=s['i'],t=s['t'],len=s['len'],voiced=s['voiced'],first=q['first']))
shared=[c for c in p12 if c in viva]
print('P12 cards',len(p12),'shared',len(shared),'P12 steps on shared cards',sum(len(p12[c]) for c in shared))
dist=collections.Counter((len(p12[c]),len(viva[c])) for c in shared)
print('(P12 uses, viva uses) -> cards', sorted(dist.items()))
unv=[c for c in shared if any(v['voiced']==0 for v in viva[c])]
print('shared cards with an unvoiced viva lesson', len(unv), sum(1 for c in shared for v in viva[c] if v['len']==0))
bysec=collections.Counter(); tot=collections.Counter()
for q in P12['questions']:
    for s in q['steps']:
        tot[q['gen']]+=1
        if s['card'] in viva: bysec[q['gen']]+=1
print({g:f'{bysec[g]}/{tot[g]}' for g in tot})
json.dump(dict(p12=p12,viva=viva,shared=shared),open('match.json','w'),indent=1)
