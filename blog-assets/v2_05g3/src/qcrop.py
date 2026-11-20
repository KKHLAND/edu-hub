import fitz, re, sys
from PIL import Image
d = fitz.open('qp.pdf')
POS = {}
for pi, p in enumerate(d):
    W = p.rect.width
    for b in p.get_text('blocks'):
        s = b[4].strip()
        m = re.match(r'^(\[\d+\s*[∼~]\s*\d+\]|\d{1,2})\.?\s', s)
        if m and (s.startswith('[') or re.match(r'^\d{1,2}\. ', s)):
            k = re.sub(r'\s', '', m.group(1)).replace('∼', '~')
            if k not in POS: POS[k] = (pi, 0 if b[0] < W/2 else 1, b[1])
COLX = [(70, 422), (420, 775)]
def seg(pi, col, y0, y1):
    p = d[pi]; r = fitz.Rect(COLX[col][0], y0, COLX[col][1], y1)
    pix = p.get_pixmap(dpi=220, clip=r)
    return Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
def nxt(pi, col, y):
    ys = [v[2] for v in POS.values() if v[0] == pi and v[1] == col and v[2] > y + 2]
    return min(ys) - 6 if ys else 1110
def trim(im):
    import numpy as np
    a = np.asarray(im.convert('L')); rows = np.where((a < 200).sum(1) > 0)[0]
    return im.crop((0, max(0, rows[0]-10), im.width, min(im.height, rows[-1]+14))) if len(rows) else im
def crop(key, until=None):
    pi, col, y = POS[key]
    parts = [seg(pi, col, y - 6, until or nxt(pi, col, y))]
    return trim(stack(parts))
def stack(ims):
    w = max(i.width for i in ims); h = sum(i.height for i in ims)
    c = Image.new('RGB', (w, h), 'white'); y = 0
    for i in ims: c.paste(i, (0, y)); y += i.height
    return c
def crop4345():
    pi, col, y = POS['[43~45]']
    a = trim(seg(pi, 0, y - 6, 1080)); b = trim(seg(pi, 1, 160, 990))
    return stack([a, b])
if __name__ == '__main__':
    print(POS.keys())
    for k in ['4', '10', '25', '27', '28']:
        crop(k).save(f'/tmp/qc_{k}.png')
    crop4345().save('/tmp/qc_43.png')
