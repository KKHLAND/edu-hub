import re, html, sys, asyncio, base64
sys.path.insert(0, '/home/claude/mock3/exams'); sys.path.insert(0, '.')
import m0324g2 as M
from g2_listen import Q, Q16, Q17, TABLE10, KO, VOC
from parse_sc import SC
import rc_lib as RC
from playwright.async_api import async_playwright
SC[15] = SC[15].replace('16번부터 17번까지는 두 번 들려줍니다.', '').strip()
N = '①②③④⑤'
md, card, ko_html, CSS = RC.md, RC.card, RC.ko_html, RC.CSS
def script_html(s):
    out = []
    for ln in s.split('\n'):
        ln = ln.strip()
        if not ln: continue
        e = html.escape(ln)
        e = re.sub(r'^(M|W|Hailey):', r'<b>\1:</b>', e)
        out.append(f'<p class="sc">{e}</p>')
    return '\n'.join(out)
def chs(lst): return [f'{N[i]} {c}' for i, c in enumerate(lst)]
cards = {}
for n in range(1, 16):
    stem, ch = Q[n]
    if n == 4: body = []; extra = '<p class="sm">※ 그림(호텔 객실: 침대 세 개, 램프, 바다가 보이는 창문, 둥근 탁자, 전기 주전자)은 EBSi 문제지 4번에서 확인하세요.</p>'
    elif n == 10: body = TABLE10.split('\n'); extra = ''
    else: body = chs(ch); extra = ''
    left = f'<div class="stem">{html.escape(stem)}</div>{extra}{md(body)}<span class="lab">듣기 대본</span>{script_html(SC[n])}'
    cards[f'L{n:02d}'] = card(n, left, ko_html(KO[n]), [f'정답: {N[M.ANS[n]-1]}'], VOC[n])
left = (f'<div class="stem">16. {html.escape(Q16[0])}</div>{md(chs(Q16[1]))}'
        f'<div class="stem" style="margin-top:14px">17. {html.escape(Q17[0])}</div>{md(chs(Q17[1]))}'
        f'<span class="lab">듣기 대본</span>{script_html(SC[16])}')
cards['L16'] = card('16~17', left, ko_html(KO[16]), [f'16번 정답: {N[M.ANS[16]-1]}', f'17번 정답: {N[M.ANS[17]-1]}'], VOC[16])

b = open('b.txt').read()
def blk(start, end):
    s = b.index(start); return b[s:b.index(end, s)]
def joinbr(t):  # undo hwp line splits for emphasized words
    return re.sub(r'\n(않는|않은|다른|맞지)\n', r' \1 ', t)
def vlines(t):
    return [tuple(re.match(r'^(.*?[a-zA-Z.)’]) ([가-힣~(].*)$', l).groups()) for l in t.split('\n') if re.match(r'^[a-zA-Z][a-zA-Z \-’\']* [가-힣~(]', l)]
def rcard(n, stem, qbody, ko, voc):
    left = f'<div class="stem">{html.escape(stem)}</div>{qbody}'
    cards[f'q{n}'] = card(n, left, ko_html(ko), [f'정답: {N[M.ANS[n]-1]}'], voc)
img = base64.b64encode(open('hx/BinData/image3.jpg', 'rb').read()).decode()
# 25
q = joinbr(blk('25. 다음', '25. [출제의도]'))
pas = q[q.index('The graph'):].strip()
ko = joinbr(blk('25. [출제의도]', '26. Dennis')).split('\n', 1)[1]
kop = re.split(r'\nconsumer ', ko)[0].replace('\n', '').replace('.이메일', '. 이메일').strip()
qb = f'<img src="data:image/jpeg;base64,{img}" style="width:86%;display:block;margin:4px auto 14px">' + md([pas])
voc25 = [('percentage','비율'),('consumer','소비자'),('respond','응답하다'),('review request','후기 요청'),('method','방식'),('in person','대면하여'),('except for','~을 제외하고'),('gap','차이'),('increase','증가하다')]
rcard(25, '다음 도표의 내용과 일치하지 않는 것은?', qb, kop, voc25)
# 27, 28
for n, nxt, title in ((27, '28. Library', '2026 Student Smart Farming Program에 관한 다음 안내문의 내용과 일치하지 않는 것은?'),
                      (28, '29. 다음', 'Library of Things에 관한 다음 안내문의 내용과 일치하는 것은?')):
    q = joinbr(blk(f'{n}. ', f'{n}. [출제의도]'))
    ql = [l for l in q.split('\n')[1:] if l.strip() and '그림입니다' not in l and not l.startswith('원본 그림') and l.strip() not in ('않는', ' 것은?', '것은?')]
    if ql and ql[0].startswith('않는'): ql = ql[1:]
    qh = ''.join(f'<p class="ch">{html.escape(l)}</p>' if re.match(r'^[①②③④⑤]', l) else (f'<p style="text-align:center;font-weight:700">{html.escape(l)}</p>' if l == ql[0] else f'<p style="margin-bottom:2px">{html.escape(l.strip())}</p>') for l in ql)
    ko = blk(f'{n}. [출제의도]', nxt).split('\n')[1:]
    kol = [l for l in ko if not re.match(r'^[a-zA-Z]', l)]
    ko_t = re.sub(r' \n(?=[가-힣])', ' ', '\n'.join(kol)).strip()
    v = vlines('\n'.join(ko))
    extra = {27: [('temperature control','온도 조절'),('watering drone','관수 드론'),('track','추적하다'),('crop','작물'),('mentoring session','멘토링 세션'),('submit','제출하다'),('institute','기관')],
             28: [('community center','주민 센터'),('check out','확인하다'),('pick up','수령하다'),('in good condition','양호한 상태로')]}[n]
    rcard(n, title, qh, ko_t, v + extra)
# 43~45
seg = b[b.index('[43~45]'):]
pas = seg[seg.index('(A)'):seg.index('[43 ~45]')]
pas = re.sub(r'\((\w)\) \n(\w+)\n ', lambda m: f'({m.group(1)}) <span class="u">{m.group(2)}</span> ', pas)
def para(l):
    l = l.strip()
    if not l: return ''
    if re.match(r'^\([A-D]\)$', l): return f'<p style="text-align:center;font-weight:700;margin-top:6px">{l}</p>'
    if l.startswith('*'): return f'<p class="fn">{l}</p>'
    return f'<p>{l}</p>'
left = ''.join(para(l) for l in pas.split('\n'))
qs = joinbr(seg[seg.index('43. '):])
qs = qs[:qs.index('그림입니다')] if '그림입니다' in qs else qs
qh = ''
for l in [l for l in qs.split('\n') if l.strip()]:
    if re.match(r'^4[345]\.', l): qh += f'<div class="stem" style="margin:14px 0 6px">{html.escape(l)}</div>'
    else: qh += '<p class="ch">' + re.sub(r'\s+(?=[②③④⑤])', '&nbsp;&nbsp;&nbsp;&nbsp;', html.escape(l.strip())) + '</p>'
kos = seg[seg.index('[43 ~45]'):seg.index('43. ')].split('\n')[1:]
kol = [l for l in kos if not re.match(r'^[a-zA-Z]', l)]
ko_t = re.sub(r' ?\n(그|그의)\n', r' \1', '\n'.join(kol))
ko_t = re.sub(r'\n(?=[는의] )', '', ko_t).strip()
v43 = vlines('\n'.join(kos))
cards['q43-45'] = card('43~45', left + '<hr>' + qh, ko_html(ko_t),
    [f'43번 정답: {N[M.ANS[43]-1]}', f'44번 정답: {N[M.ANS[44]-1]}', f'45번 정답: {N[M.ANS[45]-1]}'], v43)

async def main():
    async with async_playwright() as p:
        br = await p.chromium.launch()
        pg = await br.new_page(viewport={'width': 1200, 'height': 800}, device_scale_factor=1)
        for k, c in cards.items():
            await pg.set_content(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{c}</body></html>')
            await pg.wait_for_timeout(200)
            await pg.locator('.card').screenshot(path=f'crops/{k}.png')
            print(k)
        await br.close()
asyncio.run(main())
