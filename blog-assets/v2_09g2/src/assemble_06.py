import json, sys
S = json.load(open('secs_09g2.json')); css = open('css.html').read()
REF = sys.argv[1]; LINKS = json.loads(sys.argv[2])  # {"P1":url,"P2":url,"P3":url}
CAT = 'https://kkhland.tistory.com/category/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%ED%95%B4%EC%84%A4'
P = {
 'P1': dict(name='함축 의미·어휘·어법', items=['21','29','30','42'],
   title='2026년 9월 고2 영어 모의고사 고난도 해설 ① 함축 의미·어휘·어법 (21·29·30·42번)',
   intro='함축 의미, 문맥상 낱말의 쓰임(어휘), 어법은 <b>문장 하나하나를 정확히 읽는 힘</b>을 묻는 유형입니다. 2026년 9월 2일 시행 고2 전국연합학력평가에서 이 세 유형의 4문항(21·29·30·42번)을 골라 선택지 다섯 개를 모두 분석했습니다. 21·30·42번이 3점이고, 42번과 한 지문인 41번(제목)도 함께 정리했습니다.',
   rows=[('21','함축 의미','①','3점','우리의 설계에서 멀어진다 = 움직이도록 만들어진 몸으로 활동적인 삶을 살지 못함'),('29','어법','④','2점','주어 the first few minutes(복수) → is가 아니라 are'),('30','어휘','⑤','3점','Actually + 생각의 흐름을 끊는다 → easier가 아니라 harder'),('42','장문 어휘','⑤','3점','memes are transmitted at rapid pace → weaker가 아니라 stronger')],
   rules=[('밑줄 바로 뒤 문장이 밑줄을 풀어 준다','밑줄 속 단어를 다른 뜻으로 바꾼 선택지 주의','21'),('A of B 구조에서는 A가 주어','수식어 속 단수 명사에 속지 않기','29'),('Actually·and 뒤 결과와 방향이 맞는지 확인','기대를 뒤집는 반전, 원인과 결과의 방향','30, 42')]),
 'P2': dict(name='빈칸 추론', items=['31','32','33','34'],
   title='2026년 9월 고2 영어 모의고사 고난도 해설 ② 빈칸 추론 (31~34번)',
   intro='빈칸 추론은 해마다 <b>1등급을 가르는 유형</b>입니다. 2026년 9월 2일 시행 고2 전국연합학력평가 31~34번 네 문항(32·33·34번 3점)을 빈칸 문장의 역할, 정답 근거, 다섯 개 선택지의 함정까지 모두 풀었습니다.',
   rows=[('31','빈칸(단어)','①','2점','family and friends, person to person → 입맛은 사회적이다'),('32','빈칸(구)','②','3점','Change the judgment, and you change the emotion → 감정은 판단에서 생긴다'),('33','빈칸(구)','①','3점','However + 모방하지 않은 Pollock → 모방 예술관은 예술을 충분히 정의하지 못한다'),('34','빈칸(절)','②','3점','슈퍼컴퓨터도 못 하는 계산 → 우리 몸이 달리기를 아주 잘하기 때문')],
   rules=[('첫 문장 빈칸은 예시들의 공통 분모','반복되는 말을 한 단어로','31'),('원인·결과 빈칸은 화살표 방향부터','해석 → 감정 순서를 뒤집은 선택지 주의','32'),('However 뒤와 바로 뒤 예시가 빈칸을 증명한다','반전 이후 내용, 예시의 한 줄 요약','33, 34')]),
 'P3': dict(name='글의 순서·문장 삽입·요약', items=['36','37','38','39','40'],
   title='2026년 9월 고2 영어 모의고사 고난도 해설 ③ 글의 순서·문장 삽입·요약 (36~40번)',
   intro='글의 순서, 문장 삽입, 요약문은 <b>글의 논리 흐름</b>을 묻는 유형입니다. 2026년 9월 2일 시행 고2 전국연합학력평가 36~40번 다섯 문항(36번 3점)을 지시어·연결어 단서표와 위치별 점검으로 정리했습니다.',
   rows=[('36','글의 순서','②','3점','패턴의 학문 → (B) 스도쿠 예시 → (A) However 숫자 값은 무관 → (C) 수학이라는 생각만으로도'),('37','글의 순서','⑤','2점','망원경 이전 → (C) Copernicus 맨눈 관측 → (B) He 지동설 → (A) Using the telescope'),('38','문장 삽입','⑤','2점','한 정착지 안의 신체 단위 → these communities grew, though → 무역 분쟁의 예'),('39','문장 삽입','③','2점','don’t eat these leaves → Instead 균을 키우는 비료 → feed the fungus'),('40','요약문','①','2점','threat to social bonds → problems, fix the relationship → relationships')],
   rules=[('for example·However가 순서를 거의 정한다','일반 진술 → 예시 → 반전','36'),('역사 소재는 시간 순서 + 대명사·정관사','16세기 → 17세기, He, the telescope','37'),('주어진 문장의 첫 단어와 마지막 새 정보를 동시에','though·Instead, this system·fungus','38, 39')]),
}
ORDER = ['P1', 'P2', 'P3']
def build(k):
    p = P[k]
    h = [css, '<div class="hd">',
         f'<img src="https://raw.githubusercontent.com/KKHLAND/edu-hub/{REF}/blog-assets/v2_09g2/hard_thumb_{k}.png" alt="{p["title"]}">',
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
    nav = '<div class="nav"><b>📚 2026년 9월 고2 영어 모의고사 고난도 해설 시리즈</b><ol>'
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
