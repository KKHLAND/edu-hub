import json, sys
S = json.load(open('secs_06g2.json')); css = open('css.html').read()
REF = sys.argv[1]; LINKS = json.loads(sys.argv[2])  # {"P1":url,"P2":url,"P3":url}
CAT = 'https://kkhland.tistory.com/category/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%ED%95%B4%EC%84%A4'
P = {
 'P1': dict(name='함축 의미·어휘·어법', items=['21','29','30','42'],
   title='2026년 6월 고2 영어 모의고사 고난도 해설 ① 함축 의미·어휘·어법 (21·29·30·42번)',
   intro='함축 의미, 문맥상 낱말의 쓰임(어휘), 어법은 <b>문장 하나하나를 정확히 읽는 힘</b>을 묻는 유형입니다. 2026년 6월 고2 학평에서 이 세 유형의 4문항(21·29·30·42번)을 골라 선택지 다섯 개를 모두 분석했습니다. 21·29번이 3점입니다.',
   rows=[('21','함축 의미','①','3점','This = 상상이 진짜만큼 생생하지 않게 한 진화'),('29','어법','②','3점','관계절 뒤 주어 coupons의 본동사(produced)가 빠짐'),('30','어휘','③','2점','deep pockets·not sensitive to price → less'),('42','장문 어휘','⑤','2점','diversified와 같은 방향 → exclude가 아니라 develop')],
   rules=[('밑줄에 This가 있으면 앞 문장','평가어(wise)의 긍정·부정 방향까지 맞추기','21'),('-ing 밑줄이면 본동사 확인','관계절·삽입구를 괄호로 묶고 주어·동사 찾기','29'),('반의어 짝이 있는 단어를 의심','세미콜론 뒤 이유, and 앞뒤 방향 점검','30, 42')]),
 'P2': dict(name='빈칸 추론', items=['31','32','33','34'],
   title='2026년 6월 고2 영어 모의고사 고난도 해설 ② 빈칸 추론 (31~34번)',
   intro='빈칸 추론은 해마다 <b>1등급을 가르는 유형</b>입니다. 2026년 6월 고2 학평 31~34번 네 문항(33·34번 3점)을 빈칸 문장의 역할, 정답 근거, 다섯 개 선택지의 함정까지 모두 풀었습니다.',
   rows=[('31','빈칸(구)','①','2점','예시 일반화 → support change in uses'),('32','빈칸(구)','②','2점','실험 결과 cut its upward growth rate'),('33','빈칸(구)','②','3점','not A but ___ + 긴 털 ↔ 짧은 털 예시'),('34','빈칸(구)','⑤','3점','가장 비싼 땅 대신 공짜 보도(substitute A for B)')],
   rules=[('예시 뒤 빈칸은 일반화','뒤에서 학자가 같은 말을 반복','31'),('실험이 오면 결과 수치를 보라','30 percent 감소 → 억제','32'),('not A but B, 첫 문장과 마지막 빈칸은 짝','A의 반대 + 예시의 공통점','33, 34')]),
 'P3': dict(name='글의 순서·문장 삽입·요약', items=['36','37','38','39','40'],
   title='2026년 6월 고2 영어 모의고사 고난도 해설 ③ 글의 순서·문장 삽입·요약 (36~40번)',
   intro='글의 순서, 문장 삽입, 요약문은 <b>글의 논리 흐름</b>을 묻는 유형입니다. 2026년 6월 고2 학평 36~40번 다섯 문항(36·39·40번 3점)을 지시어·연결어 단서표와 위치별 점검으로 정리했습니다.',
   rows=[('36','글의 순서','②','3점','동물 → 초기 조상(B) → But 효율적 사냥꾼(A) → 번영(C)'),('37','글의 순서','⑤','2점','All these responses → Because of this → But what if'),('38','문장 삽입','⑤','2점','desensitization(1단계) → The next step'),('39','문장 삽입','②','3점','조건(헌신 필요) → Otherwise'),('40','요약문','④','3점','expect → anticipated, violations → break')],
   rules=[('대명사 they가 누구인지 추적','동물 → 조상 → 사냥꾼','36'),('앞 내용을 묶는 지시어가 최강 단서','All these responses, Because of this, The next step','37, 38'),('연결어가 받을 말이 없으면 그 앞이 빈자리','Otherwise 앞의 조건 찾기','39')]),
}
ORDER = ['P1', 'P2', 'P3']
def build(k):
    p = P[k]
    h = [css, '<div class="hd">',
         f'<img src="https://raw.githubusercontent.com/KKHLAND/edu-hub/{REF}/blog-assets/v2_06g2/hard_thumb_{k}.png" alt="{p["title"]}">',
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
    nav = '<div class="nav"><b>📚 2026년 6월 고2 영어 고난도 해설 시리즈</b><ol>'
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
