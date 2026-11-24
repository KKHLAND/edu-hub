import asyncio, sys
from playwright.async_api import async_playwright
T = [('P1','듣기 1~17번','대본 · 해석 · 어휘 한 번에','#1a73e8'),
     ('P2','독해 18~30번','지문 · 해석 · 어휘 한 번에','#0f9d58'),
     ('P3','독해 31~45번','빈칸 · 순서 · 삽입 · 요약 · 장문','#c0392b')]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width':1200,'height':675})
        for k, part, sub, c in T:
            await pg.set_content(f"""<html><body style="margin:0"><div style="width:1200px;height:675px;box-sizing:border-box;
background:#fbfaf6;font-family:'Noto Sans CJK KR';padding:70px 80px;position:relative;border-top:18px solid {c}">
<div style="font-size:34px;color:#555;font-weight:500">2026년 6월 4일 시행 · 2027학년도 6월 모의평가</div>
<div style="font-size:92px;font-weight:900;margin-top:26px;color:#111;line-height:1.1">고3 영어 모의고사(모평)</div>
<div style="font-size:110px;font-weight:900;color:{c};margin-top:10px;line-height:1.1">{part} 해설</div>
<div style="font-size:42px;margin-top:34px;color:#333;font-weight:700">{sub}</div>
<div style="position:absolute;right:80px;bottom:60px;font-size:30px;color:#777;font-weight:700">쌤의 이슈노트 · 모의고사 해설</div>
</div></body></html>""")
            await pg.screenshot(path=f'crops/thumb_{k}.png')
        await b.close()
asyncio.run(main())
