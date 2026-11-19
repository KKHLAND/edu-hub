# 새 포맷: 모의고사 1회분 = 3편 (듣기 1~17 / 독해 18~30 / 독해 31~45), 쌤의 이슈노트 '모의고사 해설' 카테고리용
import sys, base64, html, os, json
sys.path.insert(0, '/home/claude/sw')
import sn_data as M
TYPE = {1:"목적",2:"의견",3:"요지",4:"그림 불일치",5:"할 일",6:"금액",7:"이유",8:"언급되지 않은 것",9:"내용 불일치",
10:"도표",11:"짧은 응답",12:"짧은 응답",13:"긴 응답",14:"긴 응답",15:"상황 응답",16:"주제",17:"언급되지 않은 것",
18:"목적",19:"심경 변화",20:"주장",21:"함축 의미",22:"요지",23:"주제",24:"제목",25:"도표",26:"내용 불일치",
27:"안내문 불일치",28:"안내문 일치",29:"어법",30:"어휘",31:"빈칸",32:"빈칸",33:"빈칸",34:"빈칸",35:"무관한 문장",
36:"순서",37:"순서",38:"삽입",39:"삽입",40:"요약",41:"제목",42:"어휘",43:"순서",44:"지칭",45:"내용 불일치"}

N = '①②③④⑤'
e = html.escape
BLOG = 'https://kkhland.tistory.com/entry/'
PARTS = [
    dict(key='P1', rng=(1, 17), name='듣기 1~17번',
         title='2027학년도 수능 영어 듣기 1~17번 해설 (대본·해석·어휘)',
         slug='2027-수능-영어-듣기-해설',
         items=[(f'L{n:02d}', [n]) for n in range(1, 16)] + [('L16', [16, 17])],
         trend=0),
    dict(key='P2', rng=(18, 30), name='독해 18~30번',
         title='2027학년도 수능 영어 독해 18~30번 해설 (지문·해석·어휘)',
         slug='2027-수능-영어-독해-18-30-해설',
         items=[(f'q{n}', [n]) for n in range(18, 31)], trend=1),
    dict(key='P3', rng=(31, 45), name='독해 31~45번',
         title='2027학년도 수능 영어 독해 31~45번 해설 (빈칸·순서·삽입·요약·장문)',
         slug='2027-수능-영어-독해-31-45-해설',
         items=[(f'q{n}', [n]) for n in range(31, 41)] + [('q41-42', [41, 42]), ('q43-45', [43, 44, 45])],
         trend=2),
]
TAGS = {
    'P1': ['2027 수능', '수능 영어 듣기', '수능 영어 듣기 대본', '수능 듣기 해석', '수능 영어 해설', '2027 수능 영어'],
    'P2': ['2027 수능', '수능 영어 해설', '수능 영어 지문 해석', '수능 영어 어휘', '수능 영어 18~30번', '2027 수능 영어'],
    'P3': ['2027 수능', '수능 영어 빈칸', '수능 순서 삽입 요약', '수능 영어 장문', '수능 영어 31~45번', '2027 수능 영어'],
}
TREND_PART = M.TREND

CSS = """<style>
.mx{font-family:'Noto Sans KR',sans-serif;max-width:760px;margin:0 auto;line-height:1.8;color:#222}
.mx h2{border-left:6px solid #1a73e8;padding-left:10px;margin:36px 0 14px;font-size:1.3em}
.mx .info{border:2px solid #1a73e8;border-radius:10px;padding:14px 18px;background:#f5f9ff;margin:16px 0}
.mx .info a{color:#1a73e8;font-weight:700}
.mx .how{background:#fff7e6;border-left:4px solid #f0a020;padding:12px 16px;margin:16px 0}
.mx table.qa{border-collapse:collapse;width:100%;margin:10px 0;font-size:.95em}
.mx table.qa th,.mx table.qa td{border:1px solid #ccd;padding:6px 4px;text-align:center}
.mx table.qa th{background:#eef3f9}
.mx .p3{color:#c0392b;font-weight:700}
.mx .item{margin:30px 0 40px}
.mx .item h3{font-size:1.15em;margin:0 0 8px;color:#1a73e8}
.mx .item h3 .ty{display:inline-block;font-size:.8em;color:#1a73e8;border:1px solid #1a73e8;border-radius:20px;padding:0 9px;margin-left:6px;font-weight:500}
.mx .item h3 .pt{color:#c0392b;font-size:.85em;margin-left:4px}
.mx .item img{width:100%;height:auto;border:1px solid #e3e6ea;border-radius:6px}
.mx .tip{background:#f6f8fb;border-radius:8px;padding:12px 16px;margin-top:10px;font-size:.97em}
.mx .tip b{color:#1a73e8}
.mx .nav{border:2px solid #1a73e8;border-radius:10px;padding:14px 18px;margin:30px 0}
.mx .nav li{margin:4px 0}
.mx .small{color:#666;font-size:.9em}
</style>"""


def img_tag(key, nums, embed):
    lab = f"{nums[0]}번" if len(nums) == 1 else f"{nums[0]}~{nums[-1]}번"
    alt = f"2027학년도 수능 영어 {lab} 발문·{'대본' if nums[0] <= 17 else '지문'}·선택지·해석·어휘"
    if embed:
        b = base64.b64encode(open(f'mx/{key}.png', 'rb').read()).decode()
        return f'<img src="data:image/png;base64,{b}" alt="{e(alt)}">'
    return f'<!--IMG:{key}.png|{alt}-->'


def tip(nums):
    out = []
    for n in nums:
        pre = f'<b>{n}번</b> ' if len(nums) > 1 else ''
        if n <= 17:
            if n in M.L:
                s, t = M.L[n]
                out.append(f'<p>{pre}<b>핵심</b> {e(s)}<br><b>함정</b> {e(t)}</p>')
        elif n in M.R:
            out.append(f'<p>{pre}<b>쌤의 해설</b> {M.R[n]}</p>')
    return ''.join(out)


def answer_table(a, b):
    rows = []
    nums = list(range(a, b + 1))
    for i in range(0, len(nums), 10):
        ch = nums[i:i + 10]
        rows.append('<tr><th>번호</th>' + ''.join(f'<th>{n}</th>' for n in ch) + '</tr>')
        rows.append('<tr><th>정답</th>' + ''.join(
            f'<td class="{"p3" if n in M.PT3 else ""}">{N[M.ANS[n]-1]}</td>' for n in ch) + '</tr>')
    return '<table class="qa">' + ''.join(rows) + '</table><p class="small">빨간 정답은 3점 문항입니다.</p>'


def build(part, embed, items=None):
    a, b = part['rng']
    items = items or part['items']
    h = [CSS, '<div class="mx">']
    if not embed:
        h.append('<!--THUMB-->')
    h.append(f"<p>2026년 11월 19일에 시행된 <b>2027학년도 대학수학능력시험 영어 {part['name']}</b> 해설입니다. "
             f"문항마다 발문·{'듣기 대본' if a == 1 else '지문'}·선택지·해석·어휘를 한 장에 모았습니다. "
             "따로 단어장을 만들지 않아도 이 글 하나로 문제 풀이, 해석, 어휘 복습까지 끝낼 수 있게 구성했습니다.</p>")
    h.append('<div class="info"><b>📥 공식 자료</b><br>문제지 · 정답표 · 듣기 음원(MP3)과 대본은 한국교육과정평가원 홈페이지와 EBSi에서 무료로 받을 수 있습니다.<br>'
             '<a href="https://cdn.kice.re.kr/27dae-suneung/index.html" target="_blank" rel="noopener">한국교육과정평가원 2027 수능 문제·정답·듣기 자료 ›</a><br><a href="https://www.ebsi.co.kr/ebs/xip/xipa/retrieveSCVMainInfo.ebs?irecord=202611193&targetCd=D300&cookieGradeVal=high3" target="_blank" rel="noopener">EBSi 2027 수능 영어 문제·음원 바로가기 ›</a><br>'
                          f'<span class="small">⚡ 빠른 정답·총평·변별력 문항 분석은 <a href="{BLOG}2027-수능-영어-빠른-정답-총평">2027 수능 영어 특별판</a>에서 볼 수 있습니다.</span></div>')
    h.append('<div class="how"><b>이렇게 공부하세요</b><br>'
             + ('① 먼저 EBSi 음원으로 문제를 풀고 → ② 대본에서 정답 근거 문장을 찾은 뒤 → ③ 해석으로 확인하고 → ④ 어휘 칸에 모르는 단어를 체크하세요.'
                if a == 1 else
                '① 지문만 보고 먼저 풀고 → ② 해석으로 내용을 확인한 뒤 → ③ 쌤의 해설에서 정답 근거를 확인하고 → ④ 어휘 칸에 모르는 단어를 체크하세요. 같은 지문을 이틀 뒤 한 번 더 읽으면 어휘가 문맥과 함께 기억됩니다.')
             + '</div>')
    h.append(f"<h2>{part['name']} 빠른 정답</h2>" + answer_table(a, b))
    h.append(f"<h2>출제 경향 한눈에 보기</h2><p>{TREND_PART[part['trend']]}</p>")
    h.append(f"<h2>{part['name']} 문항별 해설</h2>")
    for key, nums in items:
        lab = f"{nums[0]}번" if len(nums) == 1 else f"{nums[0]}~{nums[-1]}번"
        ty = TYPE.get(nums[0], '') if len(nums) == 1 else ('장문' if nums[0] >= 41 else '세트 문항')
        pt = ''.join('<span class="pt">[3점]</span>' for n in nums if n in M.PT3)[:30]
        h.append(f'<div class="item"><h3>{lab}<span class="ty">{e(ty)}</span>{pt}</h3>{img_tag(key, nums, embed)}'
                 f'<div class="tip">{tip(nums)}</div>'
                 + (f'<p class="ebs-link" style="margin:8px 0 2px;font-size:.95em">🎧 <a href="https://www.ebsi.co.kr/ebs/xip/xipa/retrieveSCVMainInfo.ebs?irecord=202611193&targetCd=D300&cookieGradeVal=high3" target="_blank" rel="noopener" style="color:#1a73e8;font-weight:700">EBSi 무료 음원 바로가기</a> <span style="color:#888">({lab} 다시 듣기)</span> · <a href="https://cdn.kice.re.kr/27dae-suneung/index.html" target="_blank" rel="noopener" style="color:#1a73e8">평가원 듣기 MP3·대본</a></p>' if nums[0] <= 17 else '')
                 + '</div>')
    nav = f'<div class="nav"><b>📚 2027학년도 수능 영어 해설 시리즈</b><ol><li><a href="{BLOG}2027-수능-영어-빠른-정답-총평">빠른 정답 및 총평 (특별판)</a></li>'
    for p in PARTS:
        cur = ' (지금 보는 글)' if p is part else ''
        nav += f'<li><a href="{BLOG}{p["slug"]}">{p["name"]} 해설</a>{cur}</li>'
    nav += '</ol>· 고난도 문항 심층 해설(쌤의 영어 해설노트): <a href="https://kkhnote.blogspot.com/2026/11/suneung-2027-imp.html" target="_blank" rel="noopener">함축·어휘·어법</a> · <a href="https://kkhnote.blogspot.com/2026/11/suneung-2027-blank.html" target="_blank" rel="noopener">빈칸</a> · <a href="https://kkhnote.blogspot.com/2026/11/suneung-2027-order.html" target="_blank" rel="noopener">순서·삽입·요약</a></div>'
    h.append(nav)
    h.append('<p class="small">해설지는 현직 영어 교사가 직접 만든 자료입니다. 문항 원문의 저작권은 한국교육과정평가원에 있으며, 학습 목적으로만 활용해 주세요.</p>')
    h.append('</div>')
    return '\n'.join(h)


os.makedirs('out', exist_ok=True)
os.chdir('/home/claude/sw')
meta = {}
for p in PARTS:
    body = build(p, True)
    open(f"out/{p['key']}_미리보기.html", 'w').write(
        f"<!DOCTYPE html><html lang='ko'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
        f"<title>{e(p['title'])}</title></head><body style='margin:0;padding:20px;background:#fff'>"
        f"<h1 style=\"font-family:'Noto Sans KR',sans-serif;max-width:760px;margin:0 auto 10px;font-size:1.6em\">{e(p['title'])}</h1>{body}</body></html>")
    open(f"out/{p['key']}_티스토리.html", 'w').write(build(p, False))
    if p['key'] != 'P1':
        h = len(p['items']) // 2
        for i, its in enumerate([p['items'][:h], p['items'][h:]], 1):
            r = f"{its[0][1][0]}-{its[-1][1][-1]}"
            open(f"out/{p['key']}_미리보기_{i}({r}).html", 'w').write(
                f"<!DOCTYPE html><html lang='ko'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
                f"<title>{e(p['title'])} ({i}/2)</title></head><body style='margin:0;padding:20px;background:#fff'>"
                f"<h1 style=\"font-family:'Noto Sans KR',sans-serif;max-width:760px;margin:0 auto 10px;font-size:1.6em\">{e(p['title'])} <span style='font-size:.6em;color:#888'>미리보기 {i}/2 ({r}번)</span></h1>{build(p, True, its)}</body></html>")
    meta[p['key']] = dict(title=p['title'], slug=p['slug'], tags=TAGS[p['key']], category='모의고사 해설',
                         images=[k + '.png' for k, _ in p['items']])
json.dump(meta, open('out/meta.json', 'w'), ensure_ascii=False, indent=1)
print({k: os.path.getsize(f'out/{k}_미리보기.html') for k in meta})
