import asyncio
from playwright.async_api import async_playwright
T=[('P1','① 함축 의미·어휘·어법','21 · 29 · 30 · 42번'),('P2','② 빈칸 추론','31 · 32 · 33 · 34번'),('P3','③ 순서·삽입·요약','36 · 37 · 38 · 39 · 40번')]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1200,'height':675})
        for k,a,c in T:
            await pg.set_content(f"""<html><body style="margin:0"><div style="width:1200px;height:675px;box-sizing:border-box;background:#fbf8f5;font-family:'Noto Sans CJK KR';padding:80px 80px;position:relative;border-top:18px solid #c0392b">
<div style="font-size:32px;color:#555">2026년 5월 7일 시행 · 고3 전국연합학력평가</div>
<div style="font-size:80px;font-weight:900;margin-top:24px;color:#111;line-height:1.2">고3 영어 고난도 해설</div>
<div style="font-size:80px;font-weight:900;color:#c0392b;line-height:1.3">{a}</div>
<div style="font-size:40px;font-weight:700;color:#333;margin-top:30px">{c}</div>
<div style="position:absolute;right:80px;bottom:56px;font-size:30px;color:#777;font-weight:700">쌤의 영어 해설노트</div></div></body></html>""")
            await pg.screenshot(path=f'crops/hard_thumb_{k}.png')
        await b.close()
asyncio.run(main())
