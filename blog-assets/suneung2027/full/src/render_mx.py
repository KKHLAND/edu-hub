import re, html, sys, asyncio, base64, io
sys.path.insert(0, '/home/claude/sw')
import sn_data as M, rc_lib as RC, qc
from secs_sn import block, hv
from PIL import Image
from playwright.async_api import async_playwright
qc.POS.update({'36':(5,1,595.0),'37':(6,0,160.0),'38':(6,0,714.0),'39':(6,1,160.0)})
N = '①②③④⑤'
SC = M.load_sc()
def b64(im):
    bio = io.BytesIO(); im.save(bio, 'PNG'); return base64.b64encode(bio.getvalue()).decode()
def imgtag(im, w='100%'): return f'<img src="data:image/png;base64,{b64(im)}" style="width:{w};display:block;margin:4px 0 10px">'
def script_html(s):
    out = []
    for ln in s.split('\n'):
        e = html.escape(ln.strip())
        if not e: continue
        e = re.sub(r'^(M|W):', r'<b>\1:</b>', e); out.append(f'<p class="sc">{e}</p>')
    return '\n'.join(out)
def chs(l): return [f'{N[i]} {c}' for i, c in enumerate(l)]
def voc(lst): return [tuple(x.split(' - ', 1)) if ' - ' in x else (x, '') for x in lst]
cards = {}
for n in range(1, 16):
    stem, ch = M.Q[n]
    if n == 4:
        pic = qc.crop('4'); pic = pic.crop((0, int(pic.height * 0.1), pic.width, pic.height)); body = []; extra = imgtag(pic, '80%')
    elif n == 10: body = M.TABLE10.split('\n'); extra = ''
    else: body = chs(ch); extra = ''
    left = f'<div class="stem">{html.escape(stem)}</div>{extra}{RC.md(body)}<span class="lab">듣기 대본</span>{script_html(SC[n])}'
    cards[f'L{n:02d}'] = RC.card(n, left, RC.ko_html(M.KO[n]), [f'정답: {N[M.ANS[n]-1]}'], M.VOC[n])
left = (f'<div class="stem">16. {html.escape(M.Q16[0])}</div>{RC.md(chs(M.Q16[1]))}'
        f'<div class="stem" style="margin-top:14px">17. {html.escape(M.Q17[0])}</div>{RC.md(chs(M.Q17[1]))}'
        f'<span class="lab">듣기 대본</span>{script_html(SC[16])}')
cards['L16'] = RC.card('16~17', left, RC.ko_html(M.KO[16]), [f'16번 정답: {N[M.ANS[16]-1]}', f'17번 정답: {N[M.ANS[17]-1]}'], M.VOC[16])
CROP = {21, 25, 27, 28, 29, 30, 40}
def text_left(n):
    b = block(str(n))[1:]
    stem = b[0]; rest = []
    for x in b[1:]:
        if x == '해석': break
        rest.append(x)
    return f'<div class="stem">{html.escape(stem)}</div>' + RC.md(rest)
def fix_lines(n):
    k = str(n) if n != 42 else '41~42'
    if n in M.CARD: return []
    b = block(k)
    return [x for x in b if '→' in x and len(x) < 40]
for n in range(18, 41):
    if n in CARD_SKIP if False else False: pass
    if n in M.CARD:
        ko, vc = M.CARD[n]
    else:
        ko, v = hv(str(n)); vc = voc(v)
    left = imgtag(qc.crop(str(n))) if n in CROP else text_left(n)
    ans = fix_lines(n) + [f'정답: {N[M.ANS[n]-1]}']
    cards[f'q{n}'] = RC.card(n, left, RC.ko_html(ko), ans, vc)
ko, v = hv('41~42')
cards['q41-42'] = RC.card('41~42', imgtag(Image.open('img/q41-42.png')), RC.ko_html(ko), fix_lines(42) + [f'41번 정답: {N[M.ANS[41]-1]}', f'42번 정답: {N[M.ANS[42]-1]}'], voc(v))
pi, col, y = qc.POS['[43~45]']
c4345 = qc.stack([qc.trim(qc.seg(7, 0, y - 6, 1070)), qc.trim(qc.seg(7, 1, 150, 995))])
ko, vc = M.CARD['43-45']
cards['q43-45'] = RC.card('43~45', imgtag(c4345), RC.ko_html(ko), [f'{k}번 정답: {N[M.ANS[k]-1]}' for k in (43, 44, 45)], vc)
async def main():
    async with async_playwright() as p:
        br = await p.chromium.launch(); pg = await br.new_page(viewport={'width': 1200, 'height': 800})
        for k, c in cards.items():
            await pg.set_content(f'<html><head><meta charset="utf-8"><style>{RC.CSS}</style></head><body>{c}</body></html>')
            await pg.wait_for_timeout(150)
            await pg.locator('.card').screenshot(path=f'mx/{k}.png')
        await br.close()
import os; os.makedirs('mx', exist_ok=True)
asyncio.run(main()); print(len(cards))
