import re, html, sys, asyncio, base64, io
sys.path.insert(0, '.')
import m0324g3 as M
from g3_listen import Q, Q16, Q17, TABLE10, KO, VOC, load_sc
import rc_lib as RC
import qcrop
from playwright.async_api import async_playwright
SC = load_sc()
N = '①②③④⑤'
md, card, ko_html, CSS = RC.md, RC.card, RC.ko_html, RC.CSS
def b64(im):
    bio = io.BytesIO(); im.save(bio, 'PNG'); return base64.b64encode(bio.getvalue()).decode()
def imgtag(im, w='100%'):
    return f'<img src="data:image/png;base64,{b64(im)}" style="width:{w};display:block;margin:4px 0 10px">'
def script_html(s):
    out = []
    for ln in s.split('\n'):
        ln = ln.strip()
        if not ln: continue
        e = html.escape(ln)
        e = re.sub(r'^(M|W|Sophia):', r'<b>\1:</b>', e)
        out.append(f'<p class="sc">{e}</p>')
    return '\n'.join(out)
def chs(lst): return [f'{N[i]} {c}' for i, c in enumerate(lst)]
cards = {}
for n in range(1, 16):
    stem, ch = Q[n]
    if n == 4:
        pic = qcrop.crop('4'); pic = pic.crop((0, int(pic.height * 0.08), pic.width, pic.height))
        body = []; extra = imgtag(pic, '88%')
    elif n == 10: body = TABLE10.split('\n'); extra = ''
    else: body = chs(ch); extra = ''
    left = f'<div class="stem">{html.escape(stem)}</div>{extra}{md(body)}<span class="lab">듣기 대본</span>{script_html(SC[n])}'
    cards[f'L{n:02d}'] = card(n, left, ko_html(KO[n]), [f'정답: {N[M.ANS[n]-1]}'], VOC[n])
left = (f'<div class="stem">16. {html.escape(Q16[0])}</div>{md(chs(Q16[1]))}'
        f'<div class="stem" style="margin-top:14px">17. {html.escape(Q17[0])}</div>{md(chs(Q17[1]))}'
        f'<span class="lab">듣기 대본</span>{script_html(SC[16])}')
cards['L16'] = card('16~17', left, ko_html(KO[16]), [f'16번 정답: {N[M.ANS[16]-1]}', f'17번 정답: {N[M.ANS[17]-1]}'], VOC[16])
for n in (25, 27, 28):
    ko, voc = M.CARD[n]
    cards[f'q{n}'] = card(n, imgtag(qcrop.crop(str(n))), ko_html(ko), [f'정답: {N[M.ANS[n]-1]}'], voc)
ko, voc = M.CARD['43-45']
cards['q43-45'] = card('43~45', imgtag(qcrop.crop4345()), ko_html(ko),
    [f'43번 정답: {N[M.ANS[43]-1]}', f'44번 정답: {N[M.ANS[44]-1]}', f'45번 정답: {N[M.ANS[45]-1]}'], voc)
async def main():
    async with async_playwright() as p:
        br = await p.chromium.launch()
        pg = await br.new_page(viewport={'width': 1200, 'height': 800}, device_scale_factor=1)
        for k, c in cards.items():
            await pg.set_content(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{c}</body></html>')
            await pg.wait_for_timeout(200)
            await pg.locator('.card').screenshot(path=f'crops/{k}.png')
            print(k, end=' ')
        await br.close()
asyncio.run(main())
