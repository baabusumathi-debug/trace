import json,sys
# assemble a NEET packet draft into the Trace package P12 (all packets so far, in order)
OUT=sys.argv[1] if sys.argv[1].endswith('.json') else '/home/claude/trace/test/data/viva/P12.json'
parts=[a for a in sys.argv[1:] if not a.endswith('.json')]  # e.g. S1
P={'package':'P12','title':'NEET cardiology','kind':'neet','version':'P12.20261124.1','cards':{},'lines':{},'questions':[],'explain':{},'fixes':[]}
for g in parts:
    d=json.load(open(f'/home/claude/p12/{g}_draft.json'))
    for c in d.get('new_cards',[]):
        P['cards'][c['code']]={'deck':c['deck'],'topic':c['topic'],'type':'qa','tier':c.get('tier','S'),'q':c['q'],'a':c['a']}
    for q in d['questions']:
        q=dict(q); q.setdefault('tier','S'); q['gen']=g; q.setdefault('kind','direct')
        P['questions'].append(q)
    P['questions'][-1]['drill']=d.get('drill',[])   # the packet's check sits on its last section
    P['questions'][-1]['packet']={'S1':'Shock I: reading the failing heart','S2':'Shock II: fixing it','EC1':'ECG I: the wiring, the waves and the cameras','EC2':'ECG II: blocks, short circuits, drugs and what changes the waves','A1':'ACS I: recognising the infarct','A2':'ACS II: treating the infarct','RY':'Rhythm: fast and slow','DR':'Cardiac drugs and the poisoned heart','RH':'Pericardium, myocarditis and endocarditis','RV':'The right heart and pulmonary hypertension','AO':'Aorta: dissection','AR':'Arrest, from the first minute to prognosis'}.get(g,g)
json.dump(P,open(OUT,'w'),ensure_ascii=False,indent=1)
print('written',OUT,len(P['questions']),'questions',sum(len(q.get('drill',[])) for q in P['questions']),'drill')
