# 사용: python3 crop_sheet.py 해설지.pdf "18,19,20,...,41-42" outdir
import sys, glob, subprocess, os, numpy as np
from PIL import Image, ImageOps
pdf, nums, out = sys.argv[1], sys.argv[2].split(','), sys.argv[3]
os.makedirs(out, exist_ok=True); subprocess.run(['pdftoppm', '-r', '200', '-png', pdf, '/tmp/rr'], check=True)
for f, n in zip(sorted(glob.glob('/tmp/rr-*.png')), nums):
    im = Image.open(f).convert('RGB'); a = np.asarray(im).astype(int)
    blue = (a[:, :, 2] > 200) & (a[:, :, 0] < 60) & (a[:, :, 1] > 90) & (a[:, :, 1] < 160)
    rows = np.where(blue.sum(1) > a.shape[1] * 0.5)[0]
    top = rows[rows < a.shape[0] // 2].max() + 6; bot = rows[rows > a.shape[0] // 2].min() - 4
    cols = np.where(blue[rows[0]])[0]; x0, x1 = cols.min() - 24, cols.max() + 24
    sub = a[top:bot, x0:x1 + 1]; last = np.where((sub.min(2) < 200).sum(1) > 0)[0].max()
    c = ImageOps.expand(im.crop((x0, top, x1 + 1, top + last + 24)), border=(0, 16, 0, 0), fill='white')
    c = c.resize((1200, round(c.size[1] * 1200 / c.size[0])), Image.LANCZOS)
    c.convert('P', palette=Image.ADAPTIVE, colors=16).save(f'{out}/q{n}.png', optimize=True)
