# -*- coding: utf-8 -*-
"""ECG I page: the writing is in content.py, the drawings in draw.py; the engine is ../packet.py.
EC1.json is P12-1101 … 1105 taken from data/viva/P12.json (the live packet)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import content as C
from packet import build
ROOT = os.path.join(HERE, '..', '..', '..')
P = json.load(open(os.path.join(ROOT, 'data', 'viva', 'P12.json')))
EC1 = [q for q in P['questions'] if q['q'].startswith('P12-11')]
json.dump(EC1, open(os.path.join(HERE, 'EC1.json'), 'w'), ensure_ascii=False, indent=1)
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', 'ecg1.html')
CLOSE = C.ANCHOR
build('ecg1', C.TITLE, C.SUB, C.SECTIONS, C.TRAPS, EC1, OUT, CLOSE,
      'ECG II: blocks, short circuits, drugs, and what changes the waves',
      'Six traps NEET has actually set: the tempting answer first', theme='#7a1f2b')
