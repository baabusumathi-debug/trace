# -*- coding: utf-8 -*-
"""ECG II page: the writing is in content.py, the drawings in draw.py; the engine is ../packet.py.
EC2.json is P12-1201 … 1207 taken from data/viva/P12.json (the live packet)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import content as C
from packet import build
ROOT = os.path.join(HERE, '..', '..', '..')
P = json.load(open(os.path.join(ROOT, 'data', 'viva', 'P12.json')))
EC2 = [q for q in P['questions'] if q['q'].startswith('P12-12')]
json.dump(EC2, open(os.path.join(HERE, 'EC2.json'), 'w'), ensure_ascii=False, indent=1)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', 'ecg2.html')
CLOSE = C.ANCHOR
build('ecg2', C.TITLE, C.SUB, C.SECTIONS, C.TRAPS, EC2, OUT, CLOSE,
      'The cardiology packets: the same wiring, now with the diseases',
      'Six traps NEET has actually set: the tempting answer first', theme='#7a1f2b')
