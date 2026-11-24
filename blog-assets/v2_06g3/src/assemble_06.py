import json, sys
S = json.load(open('secs_06g3.json')); css = open('css.html').read()
REF = sys.argv[1]; LINKS = json.loads(sys.argv[2])  # {"P1":url,"P2":url,"P3":url}
CAT = 'https://kkhland.tistory.com/category/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%ED%95%B4%EC%84%A4'
P = {
 'P1': dict(name='함축 의미·어휘·어법', items=['21','29','30','42'],
   title='2026년 6월 고3 영어 모의고사(모평) 고난도 해설 ① 함축 의미·어휘·어법 (21·29·30·42번)',
   intro='함축 의미, 문맥상 낱말의 쓰임(어휘), 어법은 <b>문장 하나하나를 정확히 읽는 힘</b>을 묻는 유형입니다. 2027학년도 6월 모의평가(2026년 6월 4일 시행)에서 이 세 유형의 4문항(21·29·30·42번)을 골라 선택지 다섯 개를 모두 분석했습니다. 21·30·42번이 3점입니다.',
   rows=[('21','함축 의미','②','3점','give up the ghost = 의식은 인간만의 것이라는 믿음'),('29','어법','②','2점','선행사 styles 뒤의 what → that/which'),('30','어휘','④','3점','diminished emphasis on dialogue, very little space → thin'),('42','장문 어휘','⑤','3점','paradox·struggle to comprehend → obey가 아니라 defy')],
   rules=[('give up 뒤의 밑줄은 필자가 반대하는 생각','필자 주장을 옮긴 선택지부터 지우기','21'),('what 밑줄이면 앞에 선행사가 있는지','선행사 + 불완전한 절 → that/which','29'),('반의어 짝이 있는 단어를 의심','바로 뒤 문장의 단서와 방향 맞추기','30, 42')]),
 'P2': dict(name='빈칸 추론', items=['31','32','33','34'],
   title='2026년 6월 고3 영어 모의고사(모평) 고난도 해설 ② 빈칸 추론 (31~34번)',
   intro='빈칸 추론은 해마다 <b>1등급을 가르는 유형</b>입니다. 2027학년도 6월 모의평가 31~34번 네 문항(33·34번 3점)을 빈칸 문장의 역할, 정답 근거, 다섯 개 선택지의 함정까지 모두 풀었습니다.',
   rows=[('31','빈칸(단어)','①','2점','보전론자 = 복원·사용 → desired 상태 연장'),('32','빈칸(구)','②','2점','No wonder + 인용문 keep a secret → conceal'),('33','빈칸(구)','②','3점','the 비교급 구조, small similarity → 필요한 유사성이 더 적다'),('34','빈칸(절)','①','3점','belief in the future presence → 예술의 방향을 예측')],
   rules=[('두 집단 비교 글은 빈칸 주어부터 확인','보전론자 vs 보존론자','31'),('No wonder 빈칸은 앞 문장의 결론','인용문 핵심어를 바꿔 말한 선택지','32'),('the 비교급 구조는 같은 방향으로','바로 뒤 문장이 구조를 반복해 확인','33, 34')]),
 'P3': dict(name='글의 순서·문장 삽입·요약', items=['36','37','38','39','40'],
   title='2026년 6월 고3 영어 모의고사(모평) 고난도 해설 ③ 글의 순서·문장 삽입·요약 (36~40번)',
   intro='글의 순서, 문장 삽입, 요약문은 <b>글의 논리 흐름</b>을 묻는 유형입니다. 2027학년도 6월 모의평가 36~40번 다섯 문항(37·39번 3점)을 지시어·연결어 단서표와 위치별 점검으로 정리했습니다.',
   rows=[('36','글의 순서','⑤','2점','화학 → (C) 구조적 방어·혼자가 아니다 → (B) 이웃 신호 → (A) back-and-forth'),('37','글의 순서','④','3점','In saying that → By extension → also'),('38','문장 삽입','③','2점','문제(위험한 흔들림) → To minimize → 해결책'),('39','문장 삽입','③','3점','It was with red that → It was also … that → Here the lexicon'),('40','요약문','⑤','2점','neglected → disregard, neglected populations → underserved')],
   rules=[('단락 끝 예고 문장이 다음 단락의 주제','Nor are individual plants … on their own','36'),('덧붙이는 연결어는 첫 단락이 될 수 없다','By extension, also','37'),('To ~(하기 위해)로 시작하면 문제→해결 전환점','also가 있으면 같은 구조의 앞 문장','38, 39')]),
}
ORDER = ['P1', 'P2', 'P3']
def build(k):
    p = P[k]
    h = [css, '<div class="hd">',
         f'<img src="https://raw.githubusercontent.com/KKHLAND/edu-hub/{REF}/blog-assets/v2_06g3/hard_thumb_{k}.png" alt="{p["title"]}">',
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
    nav = '<div class="nav"><b>📚 2026년 6월 고3 영어 모의고사(모평) 고난도 해설 시리즈</b><ol>'
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
