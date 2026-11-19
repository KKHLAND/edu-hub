import asyncio
from playwright.async_api import async_playwright
T=[('P1','① 함축 의미·어휘·어법','21 · 29 · 30 · 42번'),('P2','② 빈칸 추론','31 · 32 · 33 · 34번'),('P3','③ 순서·삽입·요약','36 · 37 · 38 · 39 · 40번')]
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1200,'height':675})
        for k,a,c in T:
            await pg.set_content(f"""<html><body style="margin:0"><div style="width:1200px;height:675px;box-sizing:border-box;background:radial-gradient(circle at 85% 20%,#1d3a6e 0,#0f1f3d 60%);font-family:'Noto Sans CJK KR';padding:70px 80px;position:relative;color:#fff">
<div style="display:inline-block;border:3px solid #d4a73a;color:#d4a73a;font-size:28px;font-weight:900;padding:4px 20px;border-radius:40px">수능 특별판 · 2026.11.19 시행</div>
<div style="font-size:76px;font-weight:900;margin-top:30px;line-height:1.2">2027 수능 영어 고난도 해설</div>
<div style="font-size:80px;font-weight:900;color:#d4a73a;line-height:1.3">{a}</div>
<div style="font-size:40px;font-weight:700;color:#e7ecf5;margin-top:26px">{c}</div>
<div style="position:absolute;right:80px;bottom:52px;font-size:30px;color:#aab6cc;font-weight:700">쌤의 영어 해설노트</div></div></body></html>""")
            await pg.screenshot(path=f'img/hard_thumb_{k}.png')
        await b.close()
asyncio.run(main())
