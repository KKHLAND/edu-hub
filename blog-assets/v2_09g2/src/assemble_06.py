import json, sys
S = json.load(open('secs_09g2.json')); css = open('css.html').read()
REF = sys.argv[1]; LINKS = json.loads(sys.argv[2])  # {"P1":url,"P2":url,"P3":url}
CAT = 'https://kkhland.tistory.com/category/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%ED%95%B4%EC%84%A4'
P = {
 'P1': dict(name='함축 의미·어휘·어법', items=['21','29','30','42'],
   title='2026년 9월 고2 영어 모의고사 고난도 해설 ① 함축 의미·어휘·어법 (21·29·30·42번)',
   intro='함축 의미, 문맥상 낱말의 쓰임(어휘), 어법은 <b>문장 하나하나를 정확히 읽는 힘</b>을 묻는 유형입니다. 2026년 9월 2일 시행 고2 전국연합학력평가에서 이 세 유형의 4문항(21·29·30·42번)을 골라 선택지 다섯 개를 모두 분석했습니다. 21·29·30번이 3점이고, 42번과 한 지문인 41번(제목)도 함께 정리했습니다.',
   rows=[('21','함축 의미','②','3점','상록수 같은 회의 = 바뀌는 초점에 적응하며 가지를 뻗는 유동적인 과정'),('29','어법','⑤','3점','places 뒤 완전한 수동태 절 → which가 아니라 where'),('30','어휘','③','3점','빨리 쉽게 죄책감을 벗고 싶어서 → reluctant가 아니라 inclined'),('42','장문 어휘','④','2점','다양한 관점 찾기 · 예측에 반하는 선택과 나란히 → following이 아니라 challenging')],
   rules=[('비유는 글이 직접 풀어 준다','줄기 = 의제, 가지 = 새 방향, 사전적 이미지에 속지 않기','21'),('which/where는 뒤 절의 완전성으로','수동태도 완전한 절','29'),('because 이유와 나열 항목의 방향을 맞춘다','이유와 행동이 어긋나는 단어가 정답','30, 42')]),
 'P2': dict(name='빈칸 추론', items=['31','32','33','34'],
   title='2026년 9월 고2 영어 모의고사 고난도 해설 ② 빈칸 추론 (31~34번)',
   intro='빈칸 추론은 해마다 <b>1등급을 가르는 유형</b>입니다. 2026년 9월 2일 시행 고2 전국연합학력평가 31~34번 네 문항(32·33·34번 3점)을 빈칸 문장의 역할, 정답 근거, 다섯 개 선택지의 함정까지 모두 풀었습니다.',
   rows=[('31','빈칸(단어)','②','2점','on the move, in flux → 영구적으로 정착하기 어렵다'),('32','빈칸(구)','①','3점','shared social understanding → 다른 사람들과 공유되는 의미'),('33','빈칸(구)','①','3점','sadness + desire to repair → 슬프게 하면서 행동하게 한다'),('34','빈칸(절)','③','3점','전자레인지의 장기적 영향 → 시간이 흐르며 축적되지만 당장은 보이지 않는 변화')],
   rules=[('빈칸 옆 부사가 동사를 정한다','permanently anywhere ↔ settle','31'),('의외의 예시는 In fact·because 뒤가 진짜 이유','예시의 표면(편안함)을 담은 선택지 주의','32'),('양면성·대비쌍의 뒤쪽 항목이 빈칸','슬픔+행동, obvious ↔ long-term','33, 34')]),
 'P3': dict(name='글의 순서·문장 삽입·요약', items=['36','37','38','39','40'],
   title='2026년 9월 고2 영어 모의고사 고난도 해설 ③ 글의 순서·문장 삽입·요약 (36~40번)',
   intro='글의 순서, 문장 삽입, 요약문은 <b>글의 논리 흐름</b>을 묻는 유형입니다. 2026년 9월 2일 시행 고2 전국연합학력평가 36~40번 다섯 문항(38번 3점)을 지시어·연결어 단서표와 위치별 점검으로 정리했습니다.',
   rows=[('36','글의 순서','④','2점','환경 선택 능력 → (C) 미래의 필요 예측 → (A) For example 솔새 → (B) Later, though 새끼의 먹이'),('37','글의 순서','⑤','2점','상호작용 양식 → (C) They 직접적 양식 → (B) By contrast 모호한 어휘·I 대문자 → (A) This phenomenon'),('38','문장 삽입','③','3점','혼잡은 기분을 강화한다 → So 콘서트를 기대하면 → But if they are dreading'),('39','문장 삽입','③','2점','적응하면 배제가 줄어든다 → However 적응 못 하면 더 많은 배제 → excluded individuals'),('40','요약문','①','2점','기부 거의 두 배 → evident, concerned about appearances → conscious')],
   rules=[('시간 표현이 있으면 그 순서대로','early in the summer → Later','36'),('This phenomenon·By contrast가 받는 대상을 구체적으로','단락 끝 문장 ↔ 다음 단락 지시어','37'),('However·So 문장은 앞뒤 짝을 동시에 확인','adapt ↔ cannot adapt, So → But if they','38, 39')]),
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
