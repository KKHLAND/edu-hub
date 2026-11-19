import asyncio
from playwright.async_api import async_playwright
T = [('P1','듣기 1~17번','대본 · 해석 · 어휘 한 번에'),('P2','독해 18~30번','지문 · 해석 · 어휘 한 번에'),('P3','독해 31~45번','빈칸 · 순서 · 삽입 · 요약 · 장문')]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width':1200,'height':675})
        for k, part, sub in T:
            await pg.set_content(f"""<html><body style="margin:0"><div style="width:1200px;height:675px;box-sizing:border-box;background:#fbfaf6;font-family:'Noto Sans CJK KR';padding:66px 80px;position:relative;border-top:18px solid #0f1f3d">
<div style="display:inline-block;background:#0f1f3d;color:#d4a73a;font-size:28px;font-weight:900;padding:4px 20px;border-radius:40px">2026. 11. 19. 시행 · 대학수학능력시험</div>
<div style="font-size:92px;font-weight:900;margin-top:26px;color:#111;line-height:1.1">2027 수능 영어</div>
<div style="font-size:110px;font-weight:900;color:#b8860b;margin-top:10px;line-height:1.1">{part} 해설</div>
<div style="font-size:42px;margin-top:32px;color:#333;font-weight:700">{sub}</div>
<div style="position:absolute;right:80px;bottom:56px;font-size:30px;color:#777;font-weight:700">쌤의 이슈노트 · 모의고사 해설</div></div></body></html>""")
            await pg.screenshot(path=f'mx/thumb_{k}.png')
        await b.close()
asyncio.run(main())
