import json, sys
S = json.load(open('secs_09g1.json')); css = open('css.html').read()
REF = sys.argv[1]; LINKS = json.loads(sys.argv[2])  # {"P1":url,"P2":url,"P3":url}
CAT = 'https://kkhland.tistory.com/category/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%ED%95%B4%EC%84%A4'
P = {
 'P1': dict(name='함축 의미·어휘·어법', items=['21','29','30','42'],
   title='2026년 9월 고1 영어 모의고사 고난도 해설 ① 함축 의미·어휘·어법 (21·29·30·42번)',
   intro='함축 의미, 문맥상 낱말의 쓰임(어휘), 어법은 <b>문장 하나하나를 정확히 읽는 힘</b>을 묻는 유형입니다. 2026년 9월 2일 시행 고1 전국연합학력평가에서 이 세 유형의 4문항(21·29·30·42번)을 골라 선택지 다섯 개를 모두 분석했습니다. 네 문항 모두 2점이지만 오답률이 높은 문항이고, 42번과 한 지문인 41번(제목, 3점)도 함께 정리했습니다.',
   rows=[('21','함축 의미','⑤','2점','오렌지는 먹고 껍질은 버려라 = 재능 감탄과 모든 말의 수용을 구분'),('29','어법','⑤','2점','단수 the impact를 받는 대명사 → those가 아니라 that'),('30','어휘','③','2점','but 앞뒤 흐름 → much가 아니라 little'),('42','장문 어휘','⑤','2점','monopoly minting fees → legalize가 아니라 outlaw')],
   rules=[('비유적 밑줄은 바로 앞 문장의 대조쌍','대조 두 개를 모두 담은 선택지','21'),('that/those 밑줄은 받는 명사의 수부터','비교 구문(the opposite to)에서 자주 출제','29'),('정도 표현·반의어 짝이 있는 단어를 의심','역접어(but, though)와 바로 뒤 답변 문장으로 확인','30, 42')]),
 'P2': dict(name='빈칸 추론', items=['31','32','33','34'],
   title='2026년 9월 고1 영어 모의고사 고난도 해설 ② 빈칸 추론 (31~34번)',
   intro='빈칸 추론은 해마다 <b>1등급을 가르는 유형</b>입니다. 2026년 9월 2일 시행 고1 전국연합학력평가 31~34번 네 문항(32·33·34번 3점)을 빈칸 문장의 역할, 정답 근거, 다섯 개 선택지의 함정까지 모두 풀었습니다.',
   rows=[('31','빈칸(단어)','③','2점','long run vs next election, spread out over time → time'),('32','빈칸(구)','②','3점','conceptual building, architectural art → 건물이 아니라 아이디어 속에서 살았다'),('33','빈칸(구)','④','3점','Hence causality flowed in both directions → 기대는 남의 행동의 산물'),('34','빈칸(절)','④','3점','unable to agree on who would win → 경쟁자가 대등해 보일 때')],
   rules=[('첫 문장 빈칸은 예시의 공통 개념','반복되는 시간 표현을 한 단어로','31'),('It was as though 빈칸은 앞 내용의 비유적 요약','핵심어(idea, conceptual)를 담은 선택지','32'),('Hence·Only when 문장이 빈칸의 방향을 정한다','양방향 = 역방향 찾기, Only when = 예외 조건','33, 34')]),
 'P3': dict(name='글의 순서·문장 삽입·요약', items=['36','37','38','39','40'],
   title='2026년 9월 고1 영어 모의고사 고난도 해설 ③ 글의 순서·문장 삽입·요약 (36~40번)',
   intro='글의 순서, 문장 삽입, 요약문은 <b>글의 논리 흐름</b>을 묻는 유형입니다. 2026년 9월 2일 시행 고1 전국연합학력평가 36~40번 다섯 문항(37·39번 3점)을 지시어·연결어 단서표와 위치별 점검으로 정리했습니다.',
   rows=[('36','글의 순서','⑤','2점','size matters → (C) 표면적 대 부피 비율 → (B) 배설 습관 → (A) Their plumbing'),('37','글의 순서','②','3점','severity → (B) technologies → (A) these tools, remote sensing → (C) Satellites'),('38','문장 삽입','②','2점','아이가 줄어 생기는 이점 → But 최악의 방법 → 아이는 미래의 일꾼'),('39','문장 삽입','④','3점','원주민의 문화적 기억 → such … memory banks → this blinds us'),('40','요약문','②','2점','truly involved → engagement, immediately → instantly')],
   rules=[('단락 첫 대명사는 앞 단락의 마지막 주인공','Their = large animals','36'),('일반 → 범주 → 구체적 예로 내려가는 흐름','technologies → remote sensing → satellites','37'),('But·such·this가 앞뒤로 동시에 맞는 자리','원래 있던 But과 겹치지 않는지도 확인','38, 39')]),
}
ORDER = ['P1', 'P2', 'P3']
def build(k):
    p = P[k]
    h = [css, '<div class="hd">',
         f'<img src="https://raw.githubusercontent.com/KKHLAND/edu-hub/{REF}/blog-assets/v2_09g1/hard_thumb_{k}.png" alt="{p["title"]}">',
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
    nav = '<div class="nav"><b>📚 2026년 9월 고1 영어 모의고사 고난도 해설 시리즈</b><ol>'
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
