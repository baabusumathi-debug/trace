# -*- coding: utf-8 -*-
"""Home-screen icons for a study page: a coloured square with its short tag and an ECG-style trace.
python3 icons.py <slug> <TAG> <hex colour>  → ../icons/<slug>-192.png, -512.png, -mask-512.png"""
import sys, os, math
from PIL import Image, ImageDraw, ImageFont
slug, tag, col = sys.argv[1], sys.argv[2], sys.argv[3]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'icons')
def font(sz):
    for f in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf']:
        if os.path.exists(f): return ImageFont.truetype(f, sz)
    return ImageFont.load_default()
def make(n, mask):
    im = Image.new('RGB', (n, n), col) if mask else Image.new('RGBA', (n, n), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    if not mask: d.rounded_rectangle([0, 0, n - 1, n - 1], radius=int(n * 0.2), fill=col)
    pad = 0.2 if mask else 0.1
    x0, x1 = n * pad, n * (1 - pad); y = n * 0.70
    pts = []
    for i in range(201):
        t = i / 200
        v = 0.09 * math.exp(-((t - 0.25) / 0.035) ** 2) + 1.0 * math.exp(-((t - 0.45) / 0.012) ** 2) \
            - 0.28 * math.exp(-((t - 0.48) / 0.012) ** 2) + 0.22 * math.exp(-((t - 0.72) / 0.05) ** 2)
        pts.append((x0 + t * (x1 - x0), y - v * n * (0.26 if mask else 0.3)))
    d.line(pts, fill='white', width=max(2, n // 40), joint='curve')
    f = font(int(n * (0.24 if mask else 0.3)))
    w = d.textlength(tag, font=f)
    d.text(((n - w) / 2, n * (0.16 if mask else 0.08)), tag, font=f, fill='white')
    return im
make(192, False).save(os.path.join(OUT, '%s-192.png' % slug))
make(512, False).save(os.path.join(OUT, '%s-512.png' % slug))
make(512, True).save(os.path.join(OUT, '%s-mask-512.png' % slug))
print('icons for', slug)
