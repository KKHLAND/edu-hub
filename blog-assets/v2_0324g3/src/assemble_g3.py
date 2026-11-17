import json, sys
S = json.load(open('secs_g3.json')); css = open('css.html').read()
REF = sys.argv[1]; LINKS = json.loads(sys.argv[2])  # {"P1":url,"P2":url,"P3":url}
CAT = 'https://kkhland.tistory.com/category/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%ED%95%B4%EC%84%A4'
P = {
 'P1': dict(name='함축 의미·어휘·어법', items=['21','29','30','42'],
   title='2026년 3월 고3 영어 모의고사 고난도 해설 ① 함축 의미·어휘·어법 (21·29·30·42번)',
   intro='함축 의미, 문맥상 낱말의 쓰임(어휘), 어법은 <b>문장 하나하나를 정확히 읽는 힘</b>을 묻는 유형입니다. 2026년 3월 고3 학평에서 이 세 유형의 4문항(21·29·30·42번)을 골라 선택지 다섯 개를 모두 분석했습니다. 이 중 세 문항이 3점입니다.',
   rows=[('21','함축 의미','③','3점','따옴표 속 \'연구자\'의 비꼬는 어조를 읽어야 함'),('29','어법','④','3점','뒤 문장이 완전하므로 in which'),('30','어휘','②','2점','예시가 모두 \'차이를 버린다\'는 같은 방향'),('42','장문 어휘','④','3점','인용문(불완전한 거울)과 분사의 방향')],
   rules=[('따옴표·비유를 한 단어로 요약하라','밑줄의 따옴표는 필자의 거리 두기, 비유는 핵심 개념으로 바꾸기','21'),('관계사는 뒤 문장의 완전성','완전하면 in which·where, 불완전하면 which·that','29'),('예시와 인용은 같은 방향','나열된 예시, 인용문 뒤 분사는 앞 내용과 방향이 같아야 함','30, 42')]),
 'P2': dict(name='빈칸 추론', items=['31','32','33','34'],
   title='2026년 3월 고3 영어 모의고사 고난도 해설 ② 빈칸 추론 (31~34번)',
   intro='빈칸 추론은 해마다 <b>1등급을 가르는 유형</b>입니다. 2026년 3월 고3 학평 31~34번 네 문항(33·34번 3점)을 빈칸 문장의 역할, 정답 근거, 다섯 개 선택지의 함정까지 모두 풀었습니다.',
   rows=[('31','빈칸(단어)','⑤','2점','본문 단어 romantic을 쓴 ③이 함정'),('32','빈칸(구)','②','2점','disciplinary(학문의 vs 징계의) 다의어 함정'),('33','빈칸(구)','③','3점','설계자의 취향(④)이 아니라 사용자의 행동'),('34','빈칸(구)','③','3점','in short = 바로 앞 문장(나의 위치)의 재진술')],
   rules=[('결론·요약 표지 뒤는 재진술','then, in short, This is why 빈칸은 바로 앞 문장의 핵심어를 바꿔 쓴 것','31, 32, 34'),('글 마지막 빈칸은 전체 요약','예시들을 한 줄로 일반화','33'),('본문 단어 그대로 쓴 선택지 의심','romantic, disciplinary처럼 맥락이 반대이거나 뜻이 다른 경우','31, 32')]),
 'P3': dict(name='글의 순서·문장 삽입·요약', items=['36','37','38','39','40'],
   title='2026년 3월 고3 영어 모의고사 고난도 해설 ③ 글의 순서·문장 삽입·요약 (36~40번)',
   intro='글의 순서, 문장 삽입, 요약문은 <b>글의 논리 흐름</b>을 묻는 유형입니다. 2026년 3월 고3 학평 36~40번 다섯 문항(37·39번 3점)을 지시어·연결어 단서표와 위치별 점검표로 정리했습니다.',
   rows=[('36','글의 순서','④','2점','장점 → The problem is → This → in this manner'),('37','글의 순서','②','3점','This structure가 처음 나오는 단락(A)이 먼저'),('38','문장 삽입','③','2점','Instead, it의 it이 가리킬 gesture가 없음'),('39','문장 삽입','⑤','3점','개방성 → Nonetheless 이해 불가 → 다른 전략'),('40','요약문','②','2점','alignment → coordinate, positive → favorable')],
   rules=[('질문 뒤엔 답, 장점 뒤엔 문제점','주어진 글의 마지막 문장이 다음 단락의 종류를 알려 줌','36, 37'),('지시어+명사는 첫 등장 단락 뒤','This structure, such choices가 받을 명사를 찾기','37, 38'),('논리의 빈틈을 찾아라','앞뒤를 바로 이었을 때 이유가 빠지는 곳이 삽입 자리','39')]),
}
ORDER = ['P1', 'P2', 'P3']
def build(k):
    p = P[k]
    h = [css, '<div class="hd">',
         f'<img src="https://cdn.jsdelivr.net/gh/KKHLAND/edu-hub@{REF}/blog-assets/v2_0324g3/hard_thumb_{k}.png" alt="{p["title"]}">',
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
    nav = '<div class="nav"><b>📚 2026년 3월 고3 영어 고난도 해설 시리즈</b><ol>'
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
