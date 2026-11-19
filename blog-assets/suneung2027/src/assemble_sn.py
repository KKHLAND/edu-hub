import json, sys, subprocess
REF = sys.argv[1]; LINKS = json.loads(sys.argv[2]); TS = sys.argv[3] if len(sys.argv) > 3 else ''
subprocess.run(['python3', 'secs_sn.py', REF], check=True, capture_output=True)
S = json.load(open('secs_sn.json')); css = open('css.html').read()
CAT = 'https://kkhland.tistory.com/category/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%ED%95%B4%EC%84%A4'
BASE = f'https://cdn.jsdelivr.net/gh/KKHLAND/edu-hub@{REF}/blog-assets/suneung2027/'
P = {
 'P1': dict(name='함축 의미·어휘·어법', items=['21','29','30','42'],
   title='2027학년도 수능 영어 고난도 해설 ① 함축 의미·어휘·어법 (21·29·30·42번)',
   intro='2026년 11월 19일에 치러진 <b>2027학년도 수능 영어</b>의 고난도 문항 해설 1편입니다. 함축 의미, 문맥상 낱말(어휘), 어법은 <b>문장 하나하나를 정확히 읽는 힘</b>을 묻습니다. EBS가 변별력 문항으로 꼽은 21번을 포함해 4문항(3점 3문항)의 선택지 다섯 개를 모두 분석했습니다.',
   rows=[('21','함축 의미','②','3점','정답만 본문에 없는 말(limiting, progress)로 바꿔 씀 · EBS 변별력 문항'),('29','어법','③','2점','본동사 helps가 있으니 주어 자리는 동명사'),('30','어휘','③','3점','This is because 뒤 이유가 앞 문장과 맞는지(non-additive)'),('42','장문 어휘','②','3점','같은 주어 It의 병렬 속 혼자 반대 방향(contradicts)')],
   rules=[('비유는 글의 대조축에 올려놓기','less like A and more like B, no longer A but B로 어느 쪽인지 정하기','21'),('본동사 개수를 세라','접속사 없이 동사가 둘이면 하나는 준동사','29'),('인과·병렬은 방향이 같아야','This is because 뒤 이유, 같은 주어 병렬의 의미 방향 확인','30, 42')]),
 'P2': dict(name='빈칸 추론', items=['31','32','33','34'],
   title='2027학년도 수능 영어 고난도 해설 ② 빈칸 추론 (31~34번)',
   intro='2027학년도 수능 영어 고난도 해설 2편, <b>빈칸 추론</b>입니다. EBS는 이번 수능에서 <b>33·34번(3점)</b>을 변별력 문항으로 꼽았습니다. 31~34번 네 문항의 빈칸 문장 역할, 정답 근거, 다섯 개 선택지의 함정까지 모두 풀었습니다.',
   rows=[('31','빈칸(단어)','①','2점','단계마다 decisions → 다시 생각할 기회'),('32','빈칸(구)','①','2점','예시 속 영화만의 장점(특정 순간·정밀한 방식)'),('33','빈칸(구)','⑤','3점','사회 간 차이 ↔ 사회 내 순응 · EBS 변별력 문항'),('34','빈칸(구)','③','3점','리듬 = 구도 + 시간, 구도만 말한 ②가 함정 · EBS 변별력 문항')],
   rules=[('then·this는 바로 앞뒤 문장과 연결','빈칸 문장의 then, 빈칸 뒤 this가 받는 내용을 찾기','31, 33'),('대조 구조에서는 B만의 특징','A도 ~하지만 B는 못 한다 / B = A + 추가 요소','32, 34'),('본문 단어 재활용 선지 의심','emotional, luminosity, spatial처럼 단어만 빌린 선지 소거','32, 34')]),
 'P3': dict(name='글의 순서·문장 삽입·요약', items=['36','37','38','39','40'],
   title='2027학년도 수능 영어 고난도 해설 ③ 글의 순서·문장 삽입·요약 (36~40번)',
   intro='2027학년도 수능 영어 고난도 해설 3편, <b>글의 순서·문장 삽입·요약문</b>입니다. EBS가 변별력 문항으로 꼽은 <b>39번(3점)</b>을 포함해 36~40번 다섯 문항을 지시어·연결어 단서표와 위치별 점검으로 정리했습니다.',
   rows=[('36','글의 순서','②','2점','not just ↔ also, 일반 → 예시'),('37','글의 순서','④','3점','this domain of hidden meaning = (C)의 secrets'),('38','문장 삽입','③','2점','either + 휴식 → 해먹 사례 앞'),('39','문장 삽입','④','3점','All these mechanisms = 나열 직후, However 앞 · EBS 변별력 문항'),('40','요약문','②','2점','improving → cultivate, exploratory purchase → trials')],
   rules=[('짝을 이루는 연결어부터','not just ↔ also, however는 대조 대상이 앞에 있어야','36'),('this/All these + 명사는 앞 내용 요약','받을 대상(나열·구체 내용)이 먼저 나온 곳 뒤','37, 39'),('사례 앞에는 그 사례가 설명할 주장','주장 없이 사례가 시작되는 곳이 삽입 자리','38')]),
}
ORDER = ['P1', 'P2', 'P3']
def build(k):
    p = P[k]
    h = [css, '<div class="hd">', f'<img src="{BASE}hard_thumb_{k}.png" alt="{p["title"]}">', f'<p>{p["intro"]}</p>',
         '<div class="lead"><b>이 글의 구성</b> — 문항마다 ① 지문 구조 → ② 정답 근거 문장 → ③ 다섯 개 선택지 전부 분석 → ④ 핵심 구문 → ⑤ 이 유형 공략법 순서이며, 끝에 전체 해석과 어휘를 붙였습니다.<br>'
         f'<span class="sm">1~45번 빠른 정답과 총평은 쌤의 이슈노트 <a href="{LINKS.get("TS") or CAT}" target="_blank" rel="noopener">2027 수능 영어 특별판</a>에 있습니다. 문제지·정답·듣기 음원은 한국교육과정평가원 홈페이지와 <a href="https://www.ebsi.co.kr/ebs/xip/xipc/previousPaperList.ebs" target="_blank" rel="noopener">EBSi 기출문제</a>에서 무료로 받을 수 있습니다.</span></div>',
         f'<h2>{p["name"]} 문항 한눈에 보기</h2><table><tr><th>번호</th><th>유형</th><th>정답</th><th>배점</th><th>어려운 이유</th></tr>' +
         ''.join(f'<tr><td>{a}</td><td>{b}</td><td class="o">{c}</td><td>{d}</td><td class="l">{e}</td></tr>' for a, b, c, d, e in p['rows']) + '</table>']
    for it in p['items']: h.append(S[it])
    h.append(f'<h2>{p["name"]} 공략 3원칙</h2><table><tr><th>원칙</th><th>적용 문항</th></tr>' +
             ''.join(f'<tr><td class="l"><b>{i+1}. {a}</b> — {b}</td><td>{c}</td></tr>' for i, (a, b, c) in enumerate(p['rules'])) + '</table>')
    h.append('<div class="tip"><b>복습 체크리스트 (예비 고3)</b><br>□ 각 문항의 정답 근거 문장을 영어로 다시 찾아 밑줄 그어 보기<br>□ 내가 고른 오답이 왜 틀렸는지 한 줄로 써 보기<br>□ 어휘 목록에서 모르는 단어만 골라 지문 문장과 함께 외우기<br>□ 이틀 뒤 해석 없이 지문만 다시 읽고 구조를 말로 설명해 보기</div>')
    nav = '<div class="nav"><b>📚 2027학년도 수능 영어 고난도 해설 시리즈</b><ol>'
    for kk in ORDER:
        cur = ' <b>(지금 보는 글)</b>' if kk == k else ''
        url = LINKS.get(kk); lab = P[kk]['name'] + ' — ' + ', '.join(P[kk]['items']) + '번'
        nav += f'<li><a href="{url}">{lab}</a>{cur}</li>' if url and kk != k else f'<li>{lab}{cur}</li>'
    ts = LINKS.get('TS')
    nav += '</ol>' + (f'· 빠른 정답·총평: <a href="{ts}" target="_blank" rel="noopener">쌤의 이슈노트 · 2027 수능 영어 특별판</a><br>' if ts else '') + f'· 모의고사 전 문항 해설: <a href="{CAT}" target="_blank" rel="noopener">쌤의 이슈노트 · 모의고사 해설</a></div>'
    h.append(nav)
    h.append('<p class="sm">해설·해석은 현직 영어 교사가 직접 작성했습니다. 정답은 한국교육과정평가원 발표(11월 19일) 기준이며 최종 정답은 12월 1일에 확정됩니다. 문항 원문의 저작권은 한국교육과정평가원에 있으며, 학습 목적으로만 활용해 주세요.</p></div>')
    return '\n'.join(h)
for k in ORDER: open(f'hard_{k}.html', 'w').write(build(k))
json.dump({k: P[k]['title'] for k in ORDER}, open('titles.json', 'w'), ensure_ascii=False)
print('ok')
