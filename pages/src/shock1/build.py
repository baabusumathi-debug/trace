# -*- coding: utf-8 -*-
"""Shock I page: the writing is in content.py, the drawings in draw.py; the engine is ../packet.py."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
import vis as V
from content import SECTIONS, TITLE, SUB, TRAPS
from packet import build

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, '..', '..', 'shock1.html')
CLOSE = V.three({'filling': ('read', 'the IVC, the leg raise, the CVP'),
                 'pump': ('read', 'the wedge with a low index, the echo'),
                 'squeeze': ('read', 'warm or cold, the SVR')},
                'You can now read which number failed',
                note='The definitions told you when a failing pump counts as shock. The bedside told you the same story with your hands. The catheter wrote it in four columns, the probe showed it in pictures, and the last four cards asked whether filling was still worth giving.')
build('shock1', TITLE, SUB, SECTIONS, TRAPS, json.load(open(os.path.join(HERE, 'S1.json'))), OUT, CLOSE,
      'Shock II: you can read which number has failed. What do you push with?',
      'The six traps NEET has actually set — hear the wrong answer first')
