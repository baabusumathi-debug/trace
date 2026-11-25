# -*- coding: utf-8 -*-
"""Shock II page: the writing is in content.py, the drawings in draw.py; the engine is ../packet.py.
S2.json is P12-201 … P12-206 taken from data/viva/P12.json (the live packet)."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import importlib.util
_spec = importlib.util.spec_from_file_location('content2', os.path.join(HERE, 'content.py'))
C = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(C)
from packet import build

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', 'shock2.html')
CLOSE = C.V.three({'filling': ('read', 'take it off: diuretic, nitrate, positive pressure'),
                   'pump': ('read', 'inotrope by receptor, or a machine'),
                   'squeeze': ('read', 'norepinephrine → vasopressin → epinephrine')},
                  'You can now choose what to push with — and what it costs',
                  note='The drugs push through receptors; the ladder gives the order; the special hearts bend it; opening the artery saves lives; the machines take over when the drugs run out, each unloading or loading the heart in its own way.')
build('shock2', C.TITLE, C.SUB, C.SECTIONS, C.TRAPS, json.load(open(os.path.join(HERE, 'S2.json'))), OUT, CLOSE,
      'Next: the ECG packets, then the infarct itself — almost every patient in this packet had one.',
      'The six traps you have actually met — hear the wrong answer first',
      'And the two the closing lesson spells out', '#6b2a1f')
