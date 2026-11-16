import json, sys
S = json.load(open('secs_g2.json')); css = open('css.html').read()
REF = sys.argv[1]; LINKS = json.loads(sys.argv[2])  # {"P1":url,"P2":url,"P3":url}
CAT = 'https://kkhland.tistory.com/category/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%ED%95%B4%EC%84%A4'
P = {
 'P1': dict(name='함축 의미·어휘·어법', items=['21','29','30','42'],
   title='2026년 3월 고2 영어 모의고사 고난도 해설 ① 함축 의미·어휘·어법 (21·29·30·42번)',
   intro='함축 의미, 문맥상 낱말의 쓰임(어휘), 어법은 <b>문장 하나하나를 정확히 읽는 힘</b>을 묻는 유형입니다. 2026년 3월 고2 학평에서 이 세 유형의 4문항(21·29·30·42번)을 골라 선택지 다섯 개를 모두 분석했습니다.',
   rows=[('21','함축 의미','②','3점','\'모든 답을 정답 취급\'하는 ③이 매력적'),('29','어법','④','2점','긴 주어 뒤에 본동사가 빠짐'),('30','어휘','③','2점','limit의 결과를 나타내는 분사구문'),('42','장문 어휘','⑤','3점','thereby 뒤 결과의 방향(극복 vs 심화)')],
   rules=[('정의 문장을 찾아라','밑줄 바로 앞뒤에 그 말을 풀어 쓴 문장이 있다','21, 42'),('본동사부터 찾아라','수식어를 괄호로 묶으면 빠진 동사가 보인다','29'),('결과 표지 뒤는 같은 방향','Consequently, thereby, -ing 분사구문은 앞 절의 결과','30, 42')]),
 'P2': dict(name='빈칸 추론', items=['31','32','33','34'],
   title='2026년 3월 고2 영어 모의고사 고난도 해설 ② 빈칸 추론 (31~34번)',
   intro='빈칸 추론은 해마다 <b>1등급을 가르는 유형</b>입니다. 2026년 3월 고2 학평 31~34번 네 문항을 빈칸 문장의 역할, 정답 근거, 다섯 개 선택지의 함정까지 모두 풀었습니다.',
   rows=[('31','빈칸(단어)','①','2점','However 빈칸 = 뒤 사례들의 공통점(fear)'),('32','빈칸(구)','⑤','2점','not A but B에서 A를 쓴 ③이 함정'),('33','빈칸(구)','⑤','3점','철학 논증, therefore 앞 조건의 재진술'),('34','빈칸(구)','④','3점','빈칸 뒤 Yet 문장을 뒤집어야 함')],
   rules=[('빈칸 문장의 역할부터 정하라','However·therefore·by -ing가 무엇을 찾을지 알려 준다','31, 32, 33'),('재진술과 사례를 묶어라','That is, Indeed, In one study 뒤가 빈칸의 쉬운 버전','31, 33'),('빈칸 뒤 Yet은 뒤집어라','뒷문장 대립어의 반대편이 정답','34')]),
 'P3': dict(name='글의 순서·문장 삽입·요약', items=['36','37','38','39','40'],
   title='2026년 3월 고2 영어 모의고사 고난도 해설 ③ 글의 순서·문장 삽입·요약 (36~40번)',
   intro='글의 순서, 문장 삽입, 요약문은 <b>글의 논리 흐름</b>을 묻는 유형입니다. 2026년 3월 고2 학평 36~40번 다섯 문항을 지시어·연결어 단서표와 위치별 점검표로 정리했습니다.',
   rows=[('36','글의 순서','⑤','2점','시간 흐름과 also의 짝'),('37','글의 순서','②','3점','용어를 정의하는 단락이 먼저'),('38','문장 삽입','④','2점','sufficient ↔ insufficient, At these times'),('39','문장 삽입','③','3점','우리 경험 → 행성 전체로 장면 전환'),('40','요약문','①','2점','followed by = 자기 실험이 먼저')],
   rules=[('짝을 요구하는 말을 찾아라','also, this need, these times가 가리키는 말이 앞에 온다','36, 38'),('정의 → 사용 순서','용어를 처음 정의하는 단락이 그 용어를 쓰는 단락보다 먼저','37'),('소재가 바뀌는 첫 지점','But·대조어로 장면이 전환되는 틈에 삽입','39, 40')]),
}
ORDER = ['P1', 'P2', 'P3']
def build(k):
    p = P[k]
    h = [css, '<div class="hd">',
         f'<img src="https://cdn.jsdelivr.net/gh/KKHLAND/edu-hub@{REF}/blog-assets/v2_0324g2/hard_thumb_{k}.png" alt="{p["title"]}">',
         f'<p>{p["intro"]}</p>',
         '<div class="lead"><b>이 글의 구성</b> — 문항마다 ① 발문·지문·선택지·해석·어휘 한 장 → ② 지문 구조 → ③ 정답 근거 문장 → ④ 다섯 개 선택지 전부 분석 → ⑤ 핵심 구문 → ⑥ 이 유형 공략법 순서로 정리했습니다.<br>'
         f'<span class="sm">1~45번 전체 해설은 쌤의 이슈노트의 <a href="{CAT}" target="_blank" rel="noopener">모의고사 해설 카테고리</a>에서 볼 수 있습니다. 문제지와 듣기 음원은 <a href="https://www.ebsi.co.kr/ebs/xip/xipc/previousPaperList.ebs" target="_blank" rel="noopener">EBSi 기출문제</a>에서 무료로 받을 수 있습니다.</span></div>',
         f'<h2>{p["name"]} 문항 한눈에 보기</h2><table><tr><th>번호</th><th>유형</th><th>정답</th><th>배점</th><th>어려운 이유</th></tr>' +
         ''.join(f'<tr><td>{a}</td><td>{b}</td><td class="o">{c}</td><td>{d}</td><td class="l">{e}</td></tr>' for a, b, c, d, e in p['rows']) + '</table>']
    for it in p['items']:
        h.append(S[it])
    h.append(f'<h2>{p["name"]} 공략 3원칙</h2><table><tr><th>원칙</th><th>적용 문항</th></tr>' +
             ''.join(f'<tr><td class="l"><b>{i+1}. {a}</b> — {b}</td><td>{c}</td></tr>' for i, (a, b, c) in enumerate(p['rules'])) + '</table>')
    h.append('<div class="tip"><b>복습 체크리스트</b><br>□ 각 문항의 정답 근거 문장을 영어로 다시 찾아 밑줄 그어 보기<br>□ 내가 고른 오답이 왜 틀렸는지 한 줄로 써 보기<br>□ 이미지 속 어휘 체크박스에서 모르는 단어만 골라 지문 문장과 함께 외우기<br>□ 이틀 뒤 해석 없이 지문만 다시 읽기</div>')
    nav = '<div class="nav"><b>📚 2026년 3월 고2 영어 고난도 해설 시리즈</b><ol>'
    for kk in ORDER:
        cur = ' <b>(지금 보는 글)</b>' if kk == k else ''
        url = LINKS.get(kk)
        lab = P[kk]['name'] + ' — ' + ', '.join(P[kk]['items']) + '번'
        nav += f'<li><a href="{url}">{lab}</a>{cur}</li>' if url else f'<li>{lab}{cur}</li>'
    nav += f'</ol>· 1~45번 전 문항 해설: <a href="{CAT}" target="_blank" rel="noopener">쌤의 이슈노트 · 모의고사 해설</a></div>'
    h.append(nav)
    h.append('<p class="sm">해설은 현직 영어 교사가 직접 작성했습니다. 문항 원문의 저작권은 출제 기관(서울특별시교육청 등)에 있으며, 학습 목적으로만 활용해 주세요.</p></div>')
    return '\n'.join(h)
for k in ORDER:
    open(f'hard_{k}.html', 'w').write(build(k))
json.dump({k: P[k]['title'] for k in ORDER}, open('titles.json', 'w'), ensure_ascii=False)
print('ok')
