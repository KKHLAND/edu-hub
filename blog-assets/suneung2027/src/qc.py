import fitz, re, sys
from PIL import Image
import numpy as np
d = fitz.open('/home/claude/sn/qp.pdf')
POS = {}
for pi in range(8):
    p = d[pi]; W = p.rect.width
    for b in p.get_text('blocks'):
        s = b[4].strip()
        m = re.match(r'^(\[\d+\s*[∼～~]\s*\d+\]|\d{1,2})\.?\s', s)
        if m and (s.startswith('[') or re.match(r'^\d{1,2}\. ', s)):
            k = re.sub(r'\s', '', m.group(1)).replace('∼', '~').replace('～','~')
            if k not in POS: POS[k] = (pi, 0 if b[0] < W/2 else 1, b[1])
COLX = [(78, 420), (427, 771)]
def seg(pi, col, y0, y1):
    pix = d[pi].get_pixmap(dpi=200, clip=fitz.Rect(COLX[col][0], y0, COLX[col][1], y1))
    return Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
def nxt(pi, col, y):
    ys = [v[2] for v in POS.values() if v[0] == pi and v[1] == col and v[2] > y + 2]
    return min(ys) - 6 if ys else 1092
def trim(im):
    a = np.asarray(im.convert('L')); rows = np.where((a < 200).sum(1) > 0)[0]
    return im.crop((0, max(0, rows[0]-10), im.width, min(im.height, rows[-1]+14))) if len(rows) else im
def stack(ims):
    w = max(i.width for i in ims); h = sum(i.height for i in ims)
    c = Image.new('RGB', (w, h), 'white'); y = 0
    for i in ims: c.paste(i, (0, y)); y += i.height
    return c
def crop(key):
    pi, col, y = POS[key]
    return trim(seg(pi, col, y - 6, nxt(pi, col, y)))
if __name__ == '__main__':
    print(POS)
POS.update({'36':(5,1,595.0),'37':(6,0,160.0),'38':(6,0,714.0),'39':(6,1,160.0)})
def run():
    import os; os.makedirs('img',exist_ok=True)
    for k in ['21','29','30','31','32','33','34','36','37','38','39','40']:
        crop(k).save(f'img/q{k}.png')
    pi,col,y=POS['[41~42]']; trim(seg(pi,col,y-6,POS['[43~45]'][2]-6)).save('img/q41-42.png')
