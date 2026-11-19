import asyncio, re, json
from playwright.async_api import async_playwright
md = open('/home/claude/sn/ans.md').read()
def table(seg):
    A = {}
    for row in seg.split('\n'):
        c = [x.strip() for x in row.strip('|').split('|')]
        if len(c) >= 12 and c[0].isdigit():
            for i in range(0, 12, 3):
                if c[i].isdigit(): A[int(c[i])] = (c[i+1], c[i+2])
    return A
odd_s, even_s = md.split('짝수')[0], md.split('짝수')[1]
ODD, EVEN = table(odd_s), table(even_s)
json.dump({'odd': ODD, 'even': EVEN}, open('answers.json', 'w'), ensure_ascii=False)
assert len(ODD) == 45 and len(EVEN) == 45
NAVY, GOLD = '#0f1f3d', '#d4a73a'
FONT = "font-family:'Noto Sans CJK KR',sans-serif"
EBS_HARD = {21, 33, 34, 39}
def grid(A, label, col):
    cells = ''
    for n in range(1, 46):
        a, p = A[n]
        three = p == '3'
        bg = '#eef4ff' if n <= 17 else '#fff'
        cells += f'''<div style="border:2px solid {'#c0392b' if three else '#d7dce6'};border-radius:12px;background:{bg};height:92px;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative">
<div style="font-size:22px;color:#667;font-weight:700">{n}</div><div style="font-size:40px;font-weight:900;color:{'#c0392b' if three else '#111'};line-height:1.1">{a}</div>
{'<div style="position:absolute;top:4px;right:6px;font-size:15px;color:#fff;background:#c0392b;border-radius:6px;padding:0 5px">3점</div>' if three else ''}</div>'''
    return f'''<div style="width:1200px;box-sizing:border-box;padding:50px 56px;background:#fff;{FONT}">
<div style="display:flex;align-items:flex-end;justify-content:space-between;border-bottom:6px solid {col};padding-bottom:14px">
<div><div style="font-size:26px;color:#555">2027학년도 대학수학능력시험 3교시</div><div style="font-size:56px;font-weight:900;color:{NAVY}">영어 영역 정답 <span style="color:{col}">{label}</span></div></div>
<div style="font-size:22px;color:#777;text-align:right">출처: 한국교육과정평가원<br>2026. 11. 19. 공개(가답안)</div></div>
<div style="display:grid;grid-template-columns:repeat(9,1fr);gap:12px;margin-top:28px">{cells}</div>
<div style="margin-top:22px;font-size:22px;color:#555">■ 파란 칸: 듣기(1~17번) &nbsp; ■ <span style="color:#c0392b;font-weight:700">빨간 테두리: 3점 문항</span> &nbsp; · 최종 정답은 12월 1일 오후 5시 확정</div></div>'''
THUMB = f'''<div style="width:1200px;height:675px;box-sizing:border-box;background:radial-gradient(circle at 85% 20%,#1d3a6e 0,{NAVY} 60%);{FONT};padding:64px 80px;position:relative;color:#fff;overflow:hidden">
<div style="position:absolute;right:-40px;top:-60px;font-size:420px;font-weight:900;color:rgba(212,167,58,.10)">27</div>
<div style="display:inline-block;border:3px solid {GOLD};color:{GOLD};font-size:30px;font-weight:900;padding:6px 22px;border-radius:40px;letter-spacing:2px">SPECIAL EDITION</div>
<div style="font-size:40px;margin-top:30px;color:#c9d3e6">2027학년도 대학수학능력시험 · 2026.11.19</div>
<div style="font-size:104px;font-weight:900;line-height:1.1;margin-top:12px">수능 영어</div>
<div style="font-size:92px;font-weight:900;line-height:1.15;color:{GOLD}">빠른 정답 &amp; 총평</div>
<div style="font-size:36px;margin-top:26px;color:#e7ecf5;font-weight:700">1~45번 홀수형·짝수형 · 난이도 · EBS 연계 · 킬러 문항</div>
<div style="position:absolute;right:80px;bottom:50px;font-size:28px;color:#aab6cc;font-weight:700">쌤의 이슈노트 · 현직 영어 교사 분석</div></div>'''
def bars():
    data = [('2026학년도<br>수능', 3.11, '#c0392b'), ('2027학년도<br>6월 모평', 4.13, '#e67e22'), ('2027학년도<br>9월 모평', 15.5, '#1a73e8')]
    mx = 17; H = 360; out = ''
    for lab, v, c in data:
        h = int(H * v / mx)
        out += f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end"><div style="font-size:40px;font-weight:900;color:{c}">{v}%</div><div style="width:150px;height:{h}px;background:{c};border-radius:12px 12px 0 0"></div><div style="font-size:24px;color:#333;margin-top:12px;text-align:center;font-weight:700;line-height:1.3">{lab}</div></div>'
    out += f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end"><div style="font-size:40px;font-weight:900;color:{NAVY}">?</div><div style="width:150px;height:200px;border:4px dashed {NAVY};border-bottom:none;border-radius:12px 12px 0 0;display:flex;align-items:center;justify-content:center;font-size:22px;color:{NAVY};text-align:center;font-weight:700">12월 11일<br>성적 발표</div><div style="font-size:24px;color:{NAVY};margin-top:12px;text-align:center;font-weight:900;line-height:1.3">2027학년도<br>수능(이번)</div></div>'
    return f'''<div style="width:1200px;box-sizing:border-box;padding:50px 60px;background:#fff;{FONT}">
<div style="font-size:52px;font-weight:900;color:{NAVY}">영어 1등급(90점 이상) 비율 흐름</div>
<div style="font-size:26px;color:#555;margin-top:6px">절대평가 · 응시자 중 1등급 비율 (평가원 채점 결과 기준)</div>
<div style="display:flex;gap:20px;height:500px;align-items:flex-end;border-bottom:3px solid #333;margin-top:30px">{out}</div>
<div style="margin-top:34px;background:#f4f6fb;border-radius:16px;padding:22px 28px;font-size:28px;color:#222;line-height:1.6">
<b style="color:{NAVY}">EBS 분석</b> · 이번 수능은 <b style="color:#c0392b">작년 수능보다 쉽고</b>, <b style="color:#1a73e8">올해 9월 모평보다는 어렵게</b> 출제<br>
<span style="font-size:24px;color:#666">→ 체감 난도: 9월 모평 → <b style="color:{NAVY}">2027 수능</b> → 2026 수능 순으로 어려움 · 1등급 비율 예측치는 공식 자료가 아니라 싣지 않았습니다</span></div></div>'''
def mapimg():
    TY = {1:'목적',2:'의견',3:'요지',4:'그림',5:'할 일',6:'금액',7:'이유',8:'언급X',9:'내용X',10:'도표',11:'응답',12:'응답',13:'응답',14:'응답',15:'상황',16:'주제',17:'언급X',
          18:'목적',19:'심경',20:'주장',21:'함축',22:'요지',23:'주제',24:'제목',25:'도표',26:'인물',27:'안내문',28:'안내문',29:'어법',30:'어휘',
          31:'빈칸',32:'빈칸',33:'빈칸',34:'빈칸',35:'무관',36:'순서',37:'순서',38:'삽입',39:'삽입',40:'요약',41:'제목',42:'어휘',43:'순서',44:'지칭',45:'내용X'}
    cells = ''
    for n in range(1, 46):
        p = ODD[n][1]; hard = n in EBS_HARD
        bg = GOLD if hard else ('#eef4ff' if n <= 17 else ('#fdecea' if p == '3' else '#f6f7f9'))
        cells += f'<div style="border-radius:12px;background:{bg};height:96px;display:flex;flex-direction:column;align-items:center;justify-content:center;{"border:3px solid #c0392b;" if p=="3" else "border:3px solid transparent;"}"><div style="font-size:26px;font-weight:900;color:{NAVY}">{n}{" ★" if hard else ""}</div><div style="font-size:21px;color:#333">{TY[n]}</div></div>'
    return f'''<div style="width:1200px;box-sizing:border-box;padding:50px 56px;background:#fff;{FONT}">
<div style="font-size:52px;font-weight:900;color:{NAVY}">45문항 유형·배점 지도</div>
<div style="font-size:25px;color:#555;margin-top:6px">듣기 17문항 + 읽기 28문항 · 신유형 없음 · 3점 10문항(빨간 테두리)</div>
<div style="display:grid;grid-template-columns:repeat(9,1fr);gap:10px;margin-top:26px">{cells}</div>
<div style="display:flex;gap:26px;margin-top:26px;font-size:24px;color:#333;align-items:center">
<span><span style="display:inline-block;width:22px;height:22px;background:#eef4ff;border-radius:5px;vertical-align:middle"></span> 듣기</span>
<span><span style="display:inline-block;width:22px;height:22px;background:{GOLD};border-radius:5px;vertical-align:middle"></span> ★ EBS가 꼽은 변별력 문항(21·33·34·39)</span>
<span><span style="display:inline-block;width:22px;height:22px;border:3px solid #c0392b;border-radius:5px;vertical-align:middle"></span> 3점</span></div>
<div style="display:flex;gap:20px;margin-top:28px">
<div style="flex:1;background:{NAVY};color:#fff;border-radius:16px;padding:22px 26px"><div style="font-size:24px;color:#c9d3e6">EBS 연계율</div><div style="font-size:62px;font-weight:900;color:{GOLD}">55.6%</div><div style="font-size:24px">45문항 중 25문항 (간접 연계)</div></div>
<div style="flex:1;background:#f4f6fb;border-radius:16px;padding:22px 26px"><div style="font-size:24px;color:#555">듣기·간접 말하기</div><div style="font-size:62px;font-weight:900;color:#1a73e8">15<span style="font-size:30px">문항</span></div><div style="font-size:24px;color:#333">17문항 중 연계</div></div>
<div style="flex:1;background:#f4f6fb;border-radius:16px;padding:22px 26px"><div style="font-size:24px;color:#555">읽기·간접 쓰기</div><div style="font-size:62px;font-weight:900;color:#c0392b">10<span style="font-size:30px">문항</span></div><div style="font-size:24px;color:#333">28문항 중 연계</div></div></div></div>'''
def timeline():
    ev = [('11. 19.(목)', '시험 · 문제/정답 공개', '평가원 홈페이지에 문제지·정답·듣기 음원·대본', '#1a73e8'),
          ('~ 11. 23.(월) 18시', '이의 신청', '평가원 홈페이지 이의신청 게시판', '#e67e22'),
          ('12. 1.(화) 17시', '최종 정답 발표', '이의 심사 결과 반영', '#c0392b'),
          ('12. 11.(금)', '성적 통지', '영어 등급·1등급 비율 확인', NAVY)]
    items = ''.join(f'<div style="flex:1;text-align:center"><div style="width:44px;height:44px;border-radius:50%;background:{c};margin:0 auto;border:6px solid #fff;box-shadow:0 0 0 3px {c}"></div><div style="font-size:30px;font-weight:900;color:{c};margin-top:18px">{d}</div><div style="font-size:30px;font-weight:900;color:#111;margin-top:6px">{t}</div><div style="font-size:22px;color:#555;margin-top:8px;line-height:1.4;padding:0 10px">{s}</div></div>' for d, t, s, c in ev)
    return f'''<div style="width:1200px;box-sizing:border-box;padding:50px 50px 60px;background:#fff;{FONT}">
<div style="font-size:52px;font-weight:900;color:{NAVY};margin-bottom:40px">수능 이후 꼭 챙길 일정</div>
<div style="position:relative"><div style="position:absolute;left:12%;right:12%;top:22px;height:6px;background:#d7dce6"></div><div style="display:flex;position:relative">{items}</div></div></div>'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1200, 'height': 675})
        async def shot(html, path, full=True):
            await pg.set_content(f'<html><body style="margin:0;background:#fff">{html}</body></html>')
            el = await pg.query_selector('body > div')
            await el.screenshot(path=path)
        await shot(THUMB, 'img/thumb_S.png')
        await shot(grid(ODD, '홀수형', '#c0392b'), 'img/ans_odd.png')
        await shot(grid(EVEN, '짝수형', '#1a73e8'), 'img/ans_even.png')
        await shot(bars(), 'img/grade1.png')
        await shot(mapimg(), 'img/map.png')
        await shot(timeline(), 'img/timeline.png')
        await b.close()
asyncio.run(main())
