import json, sys
S = json.load(open('secs_06g2.json')); css = open('css.html').read()
REF = sys.argv[1]; LINKS = json.loads(sys.argv[2])  # {"P1":url,"P2":url,"P3":url}
CAT = 'https://kkhland.tistory.com/category/%EB%AA%A8%EC%9D%98%EA%B3%A0%EC%82%AC%20%ED%95%B4%EC%84%A4'
P = {
 'P1': dict(name='함축 의미·어휘·어법', items=['21','29','30','42'],
   title='2026년 6월 고2 영어 모의고사 고난도 해설 ① 함축 의미·어휘·어법 (21·29·30·42번)',
   intro='함축 의미, 문맥상 낱말의 쓰임(어휘), 어법은 <b>문장 하나하나를 정확히 읽는 힘</b>을 묻는 유형입니다. 2026년 6월 고2 학평에서 이 세 유형의 4문항(21·29·30·42번)을 골라 선택지 다섯 개를 모두 분석했습니다. 21·29·42번이 3점입니다.',
   rows=[('21','함축 의미','⑤','3점','아이디어의 시장(이상) vs 정당화의 시장(현실) 대조'),('29','어법','④','3점','전치사구 뒤 주어 authors의 본동사(have)가 빠짐'),('30','어휘','③','2점','and로 이어진 can support와 같은 방향이어야 함'),('42','장문 어휘','③','3점','presence ↔ absence, 글의 핵심은 예측 불가능성')],
   rules=[('이상 vs 현실, 밑줄은 어느 쪽?','반대편 설명을 옮긴 선택지부터 지우기','21'),('-ing 밑줄이면 본동사 확인','문두 전치사구를 괄호로 묶고 주어·동사 찾기','29'),('반의어 짝이 있는 단어를 의심','and·also 앞뒤가 같은 방향인지 점검','30, 42')]),
 'P2': dict(name='빈칸 추론', items=['31','32','33','34'],
   title='2026년 6월 고2 영어 모의고사 고난도 해설 ② 빈칸 추론 (31~34번)',
   intro='빈칸 추론은 해마다 <b>1등급을 가르는 유형</b>입니다. 2026년 6월 고2 학평 31~34번 네 문항(33·34번 3점)을 빈칸 문장의 역할, 정답 근거, 다섯 개 선택지의 함정까지 모두 풀었습니다.',
   rows=[('31','빈칸(구)','②','2점','not mere ___ → 뒤 문장(you change it)의 반대'),('32','빈칸(구)','①','2점','빈칸 뒤 실험의 결과(recall)가 답'),('33','빈칸(문장)','②','3점','A, but ___ → 첫 문장(냄새를 말하기 어렵다)으로 수미상관'),('34','빈칸(구)','①','3점','예시 일반화 + that they yield의 목적어')],
   rules=[('빈칸 뒤 문장이 빈칸을 풀어 쓴다','When you step in a river, you change it.','31'),('실험이 오면 결과 문장을 보라','did far better → 무엇을 더 잘했나','32'),('첫 문장과 마지막 빈칸은 짝','but 뒤는 앞의 반대 + 주제','33, 34')]),
 'P3': dict(name='글의 순서·문장 삽입·요약', items=['36','37','38','39','40'],
   title='2026년 6월 고2 영어 모의고사 고난도 해설 ③ 글의 순서·문장 삽입·요약 (36~40번)',
   intro='글의 순서, 문장 삽입, 요약문은 <b>글의 논리 흐름</b>을 묻는 유형입니다. 2026년 6월 고2 학평 36~40번 다섯 문항(37·39번 3점)을 지시어·연결어 단서표와 위치별 점검으로 정리했습니다.',
   rows=[('36','글의 순서','②','2점','춥고 건조 → this type of climate → 따뜻하고 습함'),('37','글의 순서','⑤','3점','We access by → However → But it has a limit'),('38','문장 삽입','③','2점','테스트 → 결과 → the same effects 확인 실험'),('39','문장 삽입','③','3점','this process + Unfortunately → And forests gone'),('40','요약문','①','2점','unconscious·before → automatic, justify → support')],
   rules=[('시간·인과 순서가 곧 글의 순서','빙하기 → 기온 상승 → 정착','36'),('역접은 바로 앞 단락을 뒤집는다','However, But이 무엇과 대조하는지','37, 39'),('실험은 방법 → 결과 → 추가 실험','the same effects가 가리킬 결과 찾기','38')]),
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
