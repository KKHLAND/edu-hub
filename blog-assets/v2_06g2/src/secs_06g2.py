import json, sys
REF = sys.argv[1] if len(sys.argv) > 1 else 'REF'
B = f'https://raw.githubusercontent.com/KKHLAND/edu-hub/{REF}/blog-assets/v2_06g2/'
def img(n, lab=None):
    lab = lab or f'{n}번'
    return (f'<img src="{B}q{n}.png" alt="2026년 6월 고2 영어 {lab} 발문 지문 선택지 해석 어휘">\n'
            '<p class="cap">발문·지문·선택지·해석·어휘</p>\n')
S = {}
S['21'] = '<h2>21번 · 함축 의미 추론 [3점]</h2>\n' + img(21) + '''<h3>① 지문 구조</h3>
<p><b>이상</b> 진리와 지식의 고전적 이상 = '아이디어의 시장'(경쟁하는 아이디어를 평가해 가장 알맞은 사실로 믿음을 형성, 과학자의 방식) → <b>현실</b> 대부분 우리는 '정당화의 시장'에 있다 → 밑줄: 단어를 쇼핑한다 → <b>풀이</b> 무엇을 믿을지 알려 줄 사실을 찾는 게 아니라, 이미 가진 믿음을 정당화할 진술을 찾는다(변호사의 방식).</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">Usually we already know what we believe. <b>What we seek are statements to justify those beliefs</b> ― the lawyer’s way.</span><br>→ '단어를 쇼핑한다' = 이미 믿는 것을 <b>뒷받침할(back up)</b> 말을 모은다. 그래서 <b>⑤ 우리의 믿음을 뒷받침할 단어들을 모으다</b>가 정답입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 효과적인 의사소통을 위해 명확한 단어를 고르다 <span class="x">— '명확성'이나 '소통'은 글의 관심사가 아닙니다.</span></li>
<li>② 설득력 있는 말로 다른 사람의 생각을 바꾸다 <span class="x">— 남을 설득하는 것이 아니라 '자기' 믿음을 정당화하는 것입니다.</span></li>
<li>③ 사실적 증거를 검토해 생각을 세우다 <span class="x">— 이것은 '아이디어의 시장', 즉 과학자의 방식으로 밑줄과 반대입니다.</span></li>
<li>④ 열린 마음으로 모든 생각을 평가하다 <span class="x">— 역시 이상적인 과학자의 방식입니다. 반대 방향의 함정.</span></li>
<li class="ans">⑤ 우리의 믿음을 뒷받침할 단어들을 모으다 <span class="o">— 정답.</span> justify those beliefs ↔ back up our beliefs</li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">We shop for words <b>not because</b> they contain ideas, <b>but because</b> they contain stories about ideas.</span><br>not because A but because B: 'A 때문이 아니라 B 때문에'. 필자의 진짜 이유는 but because 뒤에 있습니다.</div>
<div class="tip"><b>함축 의미 공략법</b> 글이 <b>A(이상) vs B(현실)</b>로 대조되면 밑줄이 어느 쪽에 속하는지부터 정하세요. 밑줄은 현실(정당화의 시장) 쪽이므로, 이상 쪽 설명을 옮겨 놓은 ③·④를 먼저 지울 수 있습니다.</div>'''

S['29'] = '<h2>29번 · 어법 [3점]</h2>\n' + img(29) + '''<h3>① 지문 구조</h3>
<p><b>주장</b> 문학은 인간 창의성과 표현의 지속적인 힘에 대한 증거다 → <b>근거</b> 새로운 기술과 미디어 속에서도 시대를 초월한 예술로 남았다 → <b>이유</b> 인간 경험의 복잡성을 포착하고 전달하는 능력 → <b>효과</b> 우리 자신을 비추어 보고, 다른 인물에게 공감하고, 인간 조건을 더 깊이 이해하게 한다.</p>
<h3>② 정답: ④ having → have</h3>
<div class="key"><span class="en">Through the written word, authors ④ <b>having</b> the unique ability to explore …</span><br>Through the written word는 전치사구(부사)이고, 주어는 <b>authors</b>입니다. 그런데 문장 끝까지 동사가 없습니다. 분사 having으로는 문장이 완성되지 않으므로 복수 주어에 맞는 동사 <b>have</b>가 와야 합니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① connecting <span class="x">— It transcends time and space 뒤에서 '그리고 ~을 연결한다'는 뜻의 분사구문입니다. 주어 It(문학)이 연결하는 주체라 능동이 맞습니다.</span></li>
<li>② Despite <span class="x">— 뒤에 명사구(the rise of new technologies …)가 오므로 전치사 Despite가 맞습니다(접속사 Although는 절이 와야 함).</span></li>
<li>③ convey <span class="x">— ability to capture and convey: and로 to부정사의 동사원형 capture와 병렬입니다.</span></li>
<li class="ans">④ having <span class="o">— 정답(틀림).</span> 문장의 본동사 have가 필요</li>
<li>⑤ reflected <span class="x">— see ourselves reflected: 우리 자신이 '비춰지는' 것이므로 목적격 보어로 과거분사가 맞습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">Literature allows us <b>to see</b> ourselves reflected …, <b>to empathize</b> with characters …, and <b>to gain</b> a deeper understanding …</span><br>allow + 목적어 + to부정사 세 개가 병렬로 이어집니다. 긴 문장은 to부정사 단위로 끊어 읽으세요.</div>
<div class="tip"><b>어법 공략법</b> 밑줄이 <b>-ing</b>일 때는 '이 문장에 본동사가 있는가?'를 먼저 확인하세요. 문두의 전치사구(Through …)를 괄호로 묶으면 주어(authors) 뒤에 동사가 비어 있는 것이 바로 보입니다.</div>'''

S['30'] = '<h2>30번 · 문맥상 낱말의 쓰임 [2점]</h2>\n' + img(30) + '''<h3>① 지문 구조</h3>
<p><b>정의</b> 뷰파인더 = 가운데 구멍을 뚫은 카드, 그림·물체의 일부를 분리한다 → <b>기능</b> 전체에 산만해지지 않고 한 부분에 집중하게 한다 → <b>아이들에게 주는 도움</b> 주저하는 아이에게 경계를 주고, 어디를 보는지 놓치는 아이를 같은 영역으로 되돌린다 → <b>만들 때</b> 카드 크기를 고려하라.</p>
<h3>② 정답: ③ confuse → help(support)</h3>
<div class="key"><span class="en">It can support hesitant children … and it can ③ <b>confuse</b> children who find it hard to keep track of where and what they are looking at, by bringing them back to the same area each time they look and look back.</span><br>보고 있는 곳을 놓치는 아이를 '같은 영역으로 되돌려 주는' 것은 아이를 <b>돕는</b> 일입니다. 앞의 can support와 and로 나란히 이어지므로 같은 방향(help)이어야 합니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① whole <span class="x">— 보이는 것 '전체'에 산만해지지 않고 한 부분에 집중한다는 뜻으로 적절합니다.</span></li>
<li>② focus <span class="x">— 관찰과 그리기에 '집중하도록' 돕는 유용한 도구입니다.</span></li>
<li class="ans">③ confuse <span class="o">— 정답(부적절).</span> by bringing them back(되돌려 줌으로써)과 반대</li>
<li>④ size <span class="x">— 바로 뒤 문장이 카드가 너무 크면 안 된다는 '크기' 이야기입니다.</span></li>
<li>⑤ block out <span class="x">— 구멍 주변 카드가 나머지 시각 정보를 '가려야' 집중할 수 있습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">It allows us to concentrate on one small part or area <b>without being distracted</b> by the whole of what can be seen.</span><br>without being p.p.: '~되지 않고'. 수동 동명사(being distracted)로, 뷰파인더의 목적(산만함 차단)을 보여 줍니다.</div>
<div class="tip"><b>어휘 공략법</b> <b>and로 연결된 두 절</b>은 같은 방향이어야 합니다. can support … and it can ③ — 앞이 긍정적이면 뒤도 긍정적이어야 하고, 뒤의 by -ing(방법)가 그 근거를 줍니다.</div>'''

S['42'] = '<h2>42번 · 장문 어휘 [3점] (41번 제목 포함)</h2>\n' + img('41-42', '41~42번') + '''<h3>① 지문 구조</h3>
<p><b>대조</b> 상업적 기업은 예측 가능성과 확실성을 추구한다 ↔ 스포츠는 그렇지 않다 → <b>장점</b> 관중은 예측 불가능할 때 경기를 더 즐기고, 결과를 예측할 수 없을 때 관중과 수익이 늘어난다 → <b>단점</b> 그러나 예측 가능성의 결여는 경기 질의 큰 변동성(날씨·부상·장소·상대 등)으로 이어진다 → <b>대응</b> 마케터는 스타 선수·프리미엄 좌석 등으로 상품을 '개선'하려 한다.</p>
<h3>② 정답: ③ (c) presence → absence(lack)</h3>
<div class="key"><span class="en">However, the (c) <b>presence</b> of predictability also leads to significant variability in the quality of sporting performances.</span><br>글 전체가 스포츠의 '예측 불가능성'을 다룹니다. 경기 질의 변동성을 낳는 것은 예측 가능성의 '존재'가 아니라 <b>결여(absence)</b>입니다. also가 '앞의 장점에 더해 이런 결과도'라는 뜻이므로 앞 문장들과 같은 대상(예측 불가능)을 말해야 합니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① (a) valued <span class="x">— 예측 가능성이 스포츠계에서 항상 '가치 있게 여겨지지는' 않는다는 대조로 적절합니다.</span></li>
<li>② (b) attract <span class="x">— 예측 불가능성이 사람들을 경기로 '끌어들인다'는 뜻입니다.</span></li>
<li class="ans">③ (c) presence <span class="o">— 정답(부적절).</span></li>
<li>④ (d) overcome <span class="x">— 품질의 변동성을 상품 개선으로 '극복하려' 한다는 뜻입니다.</span></li>
<li>⑤ (e) financial <span class="x">— 관중·수익과 연결되므로 '재정적' 성공이 맞습니다.</span></li>
</ul>
<p><b>41번 제목</b> 정답 ③ Unpredictability in Sports: A Blessing and a Challenge — 예측 불가능성이 관중과 수익을 늘리는 '축복'이면서, 품질 변동이라는 '도전'이기도 하다는 글의 두 측면을 모두 담았습니다.</p>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">attendances at sporting contests are likely to be higher, <b>as are</b> the profits of leagues.</span><br>as + be동사 + 주어: '~도 마찬가지로 그렇다'(도치). 리그의 수익도 더 높아질 가능성이 있다는 뜻입니다.</div>
<div class="tip"><b>장문 어휘 공략법</b> 밑줄이 <b>presence/absence, increase/decrease</b>처럼 반의어 짝이 있는 단어라면 1순위로 의심하세요. 글의 핵심어(unpredictability)와 같은 방향인지 확인하면 바로 걸러집니다.</div>'''

S['31'] = '<h2>31번 · 빈칸 추론(단어·구) [2점]</h2>\n' + img(31) + '''<h3>① 빈칸 문장의 역할</h3>
<p>Heraclitus의 말(같은 강에 두 번 들어갈 수 없다)에 제자 Cratylus가 <b>덧붙인(added)</b> 생각이 빈칸입니다. 바로 뒤 문장 When you step in a river, you change it.이 그 생각을 풀어 줍니다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">When you step in a river, <b>you change it</b>. Nothing is static.</span><br>우리는 강을 그저 바라보는 존재가 아니라 강을 바꾸는 존재다 → we are not mere <b>② passive observers</b>(단순한 수동적 관찰자가 아니다).</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① effective leaders(유능한 지도자) <span class="x">— 이끄는 능력은 글과 무관합니다.</span></li>
<li class="ans">② passive observers(수동적 관찰자) <span class="o">— 정답.</span> not mere와 결합해 '능동적으로 바꾸는 존재'</li>
<li>③ accurate predictors(정확한 예측자) <span class="x">— 미래 사건을 아직 깨닫지 못한다고 했으므로 예측과 거리가 멉니다.</span></li>
<li>④ sensitive dreamers(예민한 몽상가) <span class="x">— 근거가 없습니다.</span></li>
<li>⑤ influential philosophers(영향력 있는 철학자) <span class="x">— Heraclitus·Cratylus가 철학자라서 만든 함정입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">events are taking place outside your immediate surroundings <b>that will change your life</b> in the future</span><br>관계대명사 that절의 선행사는 바로 앞 surroundings가 아니라 멀리 있는 <b>events</b>입니다(사건이 삶을 바꾼다).</div>
<div class="tip"><b>빈칸 공략법</b> not mere ___ 빈칸은 '단순한 ~가 아니다'이므로, 뒤 문장이 말하는 모습(능동적으로 바꾼다)의 <b>반대말</b>을 고르세요.</div>'''

S['32'] = '<h2>32번 · 빈칸 추론(구) [2점]</h2>\n' + img(32) + '''<h3>① 빈칸 문장의 역할</h3>
<p>Numerous experiments have found that … 빈칸 — 여러 실험이 발견한 <b>결과</b>입니다. 바로 뒤에 그 실험 중 하나가 예시로 이어집니다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">When asked to recall as many words on the list as possible, those who had moved around <b>did far better</b>.</span><br>두 장소에서 공부한 학생들이 단어를 훨씬 더 잘 기억했다 → 학습자가 최소 두 곳에서 공부하면 <b>① 학습 자료를 기억할</b> 가능성이 높다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li class="ans">① recall the material(자료를 기억하다) <span class="o">— 정답.</span> 실험의 recall as many words와 대응</li>
<li>② worsen their learning habits(학습 습관을 나쁘게 하다) <span class="x">— 정반대입니다.</span></li>
<li>③ develop anxiety and depression(불안과 우울이 생기다) <span class="x">— 감정 이야기는 없습니다.</span></li>
<li>④ create diverse networks of people(다양한 인맥을 만들다) <span class="x">— rich association(풍부한 연상)을 '사람 관계'로 바꾼 함정입니다.</span></li>
<li>⑤ remember the features of the places(장소의 특징을 기억하다) <span class="x">— 기억하는 대상은 장소가 아니라 공부한 자료입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en"><b>When asked</b> to recall as many words on the list <b>as possible</b>, …</span><br>When (they were) asked: 접속사 뒤 '주어+be동사' 생략. as many ~ as possible은 '가능한 한 많은 ~'.</div>
<div class="tip"><b>빈칸 공략법</b> 빈칸 뒤에 <b>실험(In one of the first such trials)</b>이 오면, 실험의 결과 문장(did far better)이 빈칸의 답입니다. 결과에서 '무엇을' 더 잘했는지 확인하세요.</div>'''

S['33'] = '<h2>33번 · 빈칸 추론(문장) [3점]</h2>\n' + img(33) + '''<h3>① 빈칸 문장의 역할</h3>
<p>This is how evolution has shaped our brain: We respond to odors correctly …, but ___ — 콜론(:) 뒤에서 글 전체를 정리하는 결론입니다. <b>but</b> 앞(정확히 반응한다)과 반대되는 내용이 와야 합니다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">even this most basic way of <b>talking about smells is challenging</b>. There are <b>no words</b> in the English language to describe smells …</span><br>냄새를 묘사할 단어가 없고, 흔한 냄새도 이름을 대지 못한다. 그래도 맥주와 소변은 정확히 구별한다 → 반응은 정확하지만 <b>② 그것에 대해 말할 채비가 잘 되어 있지 않다</b>.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 정확한 근원을 그럭저럭 찾아낸다 <span class="x">— 흔한 냄새도 식별하기 어렵다고 했습니다.</span></li>
<li class="ans">② 그것에 대해 말할 채비가 잘 되어 있지 않다 <span class="o">— 정답.</span> 첫 문장의 talking about smells is challenging과 수미상관</li>
<li>③ 지각이 강한 감정으로 이어지지 않는다 <span class="x">— 감정은 다루지 않습니다.</span></li>
<li>④ 시각 정보 없이는 구별하지 못한다 <span class="x">— '시각'은 근거가 없고, 실제로는 정확히 구별해 반응합니다.</span></li>
<li>⑤ 평소 맥락이 없으면 반응이 틀릴 수 있다 <span class="x">— 맥락 없이도 맥주는 마시고 소변은 마시지 않는다고 했으므로 반대입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">There are no words … to describe smells <b>in the same way in which</b> “blue” or “green” describe colors.</span><br>in the same way in which: '~하는 것과 같은 방식으로'. 전치사 + 관계대명사(in which)가 way를 꾸밉니다.</div>
<div class="tip"><b>빈칸 공략법</b> 마지막 빈칸이 <b>A, but ___</b> 구조면 A의 반대 + 글의 첫 문장(주제)을 합치세요. 이 글의 첫 문장(냄새에 대해 말하기는 어렵다)이 곧 정답입니다.</div>'''

S['34'] = '<h2>34번 · 빈칸 추론(구) [3점]</h2>\n' + img(34) + '''<h3>① 빈칸 문장의 역할</h3>
<p>첫 문장이 빈칸이고 For instance로 예시가 이어집니다. 인간이 환경에 적응하는 '특히 강력한 방식'을 <b>예시들을 일반화</b>해서 찾아야 합니다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">a child who gets praised … is likely to continue … A dancer who feels that a particular conditioning exercise is not giving any results is likely to give that exercise up</span><br>칭찬(좋은 결과) → 계속, 결과 없음 → 그만둠. 행동이 낳는 결과에 따라 행동을 바꾼다 → <b>① 결과에 비추어 행동을 바꾸는 것</b>.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li class="ans">① 결과에 비추어 행동을 바꾸는 것 <span class="o">— 정답.</span> 빈칸 뒤 that they yield(그것들이 낳는)가 consequences를 꾸밉니다.</li>
<li>② 이익을 받은 뒤에도 일을 그만두는 것 <span class="x">— 이익이 있으면 계속한다는 내용과 반대입니다.</span></li>
<li>③ 온갖 어려움에도 새로운 도전에 맞서는 것 <span class="x">— 오히려 불편함·불이익을 피한다고 했습니다.</span></li>
<li>④ 가능한 결과와 상관없이 운동하는 것 <span class="x">— '결과에 따라' 바꾼다는 핵심과 정반대입니다. exercise라는 단어를 재활용한 함정.</span></li>
<li>⑤ 금전적 이익을 기대하며 위험을 감수하는 것 <span class="x">— 금전적 이익·위험 감수는 언급되지 않습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">we tend to do things that bring us some kind of benefit <b>or</b> act in ways that help us avoid some kind of problem</span><br>tend to 뒤에 do things와 act in ways가 or로 병렬. help + 목적어 + 동사원형(avoid).</div>
<div class="tip"><b>빈칸 공략법</b> 빈칸 뒤에 <b>that + 동사</b>(that they yield)가 붙어 있으면, 그 동사의 목적어가 될 명사가 선택지 끝에 있어야 합니다. yield(낳다)의 목적어로 자연스러운 것은 consequences뿐입니다.</div>'''

S['36'] = '<h2>36번 · 글의 순서 [2점]</h2>\n' + img(36) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">빙하기는 더 추웠을 뿐 아니라 결정적으로 <b>훨씬 더 건조했다(drier)</b></td><td class="l">→ '건조'에 대한 설명이 이어질 차례</td></tr>
<tr><td>(B)</td><td class="l">아일랜드에서는 추위를 습함과 연관 짓지만, 정말 추우면 증발·구름·비가 적다 → <b>cold and dry</b></td><td class="l">왜 건조한지 설명 → 주어진 글 바로 뒤</td></tr>
<tr><td>(A)</td><td class="l"><b>In this type of climate</b>, 농사는 선택지가 아니다 … 기온이 오르며 생명이 폭발</td><td class="l">this type of climate = (B)의 춥고 건조한 기후 → (B) 뒤</td></tr>
<tr><td>(C)</td><td class="l">The world got <b>warmer and wetter</b>, 사람들이 식량을 기르는 곳에 살기 시작</td><td class="l">(A) 끝의 '기온 상승·만년설 해빙' 이후 → (A) 뒤</td></tr>
</table>
<h3>② 정답: ② (B)-(A)-(C)</h3>
<div class="key">빙하기는 춥고 건조했다 → (B) 추우면 비가 적어 식물이 자라기 어렵다 → (A) 이런 기후에서 농사는 불가능, 기온이 오르며 생명이 폭발 → (C) 따뜻하고 습해지자 사람들이 정착해 서서히 농사를 시작했다.</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— this type of climate가 무엇인지 (B)의 설명(cold and dry)이 먼저 나와야 합니다.</span></li>
<li>(B)-(C)-(A)(③) <span class="x">— (C)에서 이미 따뜻해졌는데 (A)에서 다시 '이런(건조한) 기후'를 말하면 시간 순서가 뒤집힙니다.</span></li>
<li>(C)로 시작(④, ⑤) <span class="x">— 빙하기 이야기 직후 갑자기 '더 따뜻해졌다'가 올 수 없습니다.</span></li>
</ul>
<div class="tip"><b>순서 공략법</b> 기후·역사 지문은 <b>시간 순서</b>가 곧 글의 순서입니다. 빙하기(춥고 건조) → 기온 상승 → 따뜻하고 습함 → 정착·농사, 이 흐름에 단락을 끼워 맞추세요.</div>'''

S['37'] = '<h2>37번 · 글의 순서 [3점]</h2>\n' + img(37) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">작업 기억은 명시적으로 인식하지만, 장기 기억에는 <b>직접 접근할 수 없다</b></td><td class="l">→ 그럼 어떻게 접근하는지 설명할 차례</td></tr>
<tr><td>(C)</td><td class="l"><b>We access long-term memory by</b> bringing the information into working memory. 예: 지금 모든 배우를 의식하지 않음</td><td class="l">접근 방법 + '배우' 예시 처음 등장 → 주어진 글 바로 뒤</td></tr>
<tr><td>(B)</td><td class="l"><b>However</b>, if I asked you to list all the actors …</td><td class="l">(C)의 '지금은 의식하지 않는다'와 대조 → (C) 뒤</td></tr>
<tr><td>(A)</td><td class="l"><b>But</b> remember <b>it</b> has a limit of seven items</td><td class="l">it = (B)의 working memory, 한계를 덧붙임 → (B) 뒤</td></tr>
</table>
<h3>② 정답: ⑤ (C)-(B)-(A)</h3>
<div class="key">직접 접근할 수 없다 → (C) 작업 기억으로 불러와 접근한다, 예: 배우들은 장기 기억에 있다 → (B) 하지만 나열하라고 하면 작업 기억으로 하나씩 불러온다 → (A) 그러나 작업 기억은 7개 항목이 한계라 한 번에 몇 명만 인식한다.</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— Each actor라는 말이 '배우' 예시가 소개되기 전에 나올 수 없습니다.</span></li>
<li>(B)로 시작(②, ③) <span class="x">— the actors가 무엇인지 모르고, However가 대조할 내용도 없습니다.</span></li>
<li>(C)-(A)-(B)(④) <span class="x">— (A)의 it(작업 기억)으로 배우를 불러오는 장면은 (B)에서 처음 나오므로 (A)가 먼저 올 수 없습니다.</span></li>
</ul>
<div class="tip"><b>순서 공략법</b> <b>However, But</b> 같은 역접은 바로 앞 단락의 내용을 뒤집습니다. (B) However는 '지금은 의식하지 않는다'(C)를, (A) But은 '하나씩 불러올 수 있다'(B)를 뒤집으므로 C → B → A로 자연스럽게 정해집니다.</div>'''

S['38'] = '<h2>38번 · 문장 삽입 [2점]</h2>\n' + img(38) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<p>Adults who were told to gesture … <b>remembered more</b> than adults who were told not to gesture, <b>particularly several weeks later</b>. → 첫 번째 실험의 <b>결과</b>입니다. 앞에는 실험 방법과 '몇 주 후' 테스트가, 뒤에는 다른 조건의 실험이 와야 합니다.</p>
<h3>② 정답: ③</h3>
<div class="key"><span class="en">We then tested the adults’ memories of these events immediately after the descriptions and <b>three weeks later</b>. ( ③ ) <b>To see if we’d get the same effects</b> if people gestured on their own, we did the study again …</span><br>③ 앞: 직후와 3주 후에 기억을 테스트 → 주어진 문장: 결과(특히 몇 주 후에 더 많이 기억) → ③ 뒤: '같은 효과(the same effects)'가 나오는지 다시 실험. the same effects가 가리킬 결과가 ③ 자리에 있어야 합니다.</div>
<h3>③ 위치별 점검</h3>
<ul class="ch">
<li>① <span class="x">— 아직 실험 소개 전이라 'told to gesture'한 성인이 누구인지 알 수 없습니다.</span></li>
<li>② <span class="x">— 영상 내용 설명 뒤, 테스트(We then tested)보다 결과가 먼저 나올 수 없습니다.</span></li>
<li class="ans">③ <span class="o">— 정답.</span> 테스트 → 결과 → 같은 효과 확인 실험</li>
<li>④ <span class="x">— 두 번째 실험(지시 없음)의 결과 자리입니다. 주어진 문장은 '지시받은' 성인 이야기입니다.</span></li>
<li>⑤ <span class="x">— 결론(제스처는 정보를 기억하기 쉽게 만든다) 직전이라 첫 실험 결과가 올 자리가 아닙니다.</span></li>
</ul>
<div class="tip"><b>삽입 공략법</b> 실험 지문은 <b>방법 → 결과 → 추가 실험 → 결과 → 결론</b> 순서입니다. 뒤 문장의 the same effects처럼 '앞의 결과'를 가리키는 말이 있는데 그 앞에 결과가 없다면, 그곳이 삽입 자리입니다.</div>'''

S['39'] = '<h2>39번 · 문장 삽입 [3점]</h2>\n' + img(39) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<p><b>Unfortunately</b>, deforestation is preventing <b>this process</b> from being fully accomplished. → 앞에는 좋은 '과정(this process)'이 설명되어 있어야 하고(Unfortunately로 반전), 뒤에는 삼림 벌채의 결과가 이어져야 합니다.</p>
<h3>② 정답: ③</h3>
<div class="key"><span class="en">The existence of a larger amount of trees will no doubt lead to the reduced presence of carbon dioxide … and the increased existence of oxygen. ( ③ ) <b>And with half of the Earth’s forests gone</b>, the amount of carbon dioxide is progressively rising.</span><br>this process = 나무가 많을수록 이산화탄소는 줄고 산소는 늘어나는 과정. ③ 뒤 And with half of the Earth’s forests gone은 갑자기 '숲이 사라진' 이야기를 하므로, 그 사이에 삼림 벌채를 꺼내는 주어진 문장이 필요합니다.</div>
<h3>③ 위치별 점검</h3>
<ul class="ch">
<li>① <span class="x">— 아직 나무의 역할(광합성)이 설명되기 전이라 this process가 가리킬 것이 없습니다.</span></li>
<li>② <span class="x">— 광합성 설명 뒤지만, 바로 다음 문장이 같은 과정을 더 설명하므로 흐름이 끊깁니다.</span></li>
<li class="ans">③ <span class="o">— 정답.</span> 좋은 과정 → Unfortunately 벌채가 막는다 → And 숲의 절반이 사라져 CO2 증가</li>
<li>④ <span class="x">— CO2 증가 → 복사 에너지 반사로 이어지는 인과 사슬 중간입니다.</span></li>
<li>⑤ <span class="x">— 결론(Accordingly) 직전으로, 이미 벌채의 결과가 다 나온 뒤입니다.</span></li>
</ul>
<div class="tip"><b>삽입 공략법</b> 주어진 문장이 <b>Unfortunately, However</b>로 시작하면 '좋은 내용 → 나쁜 내용'으로 바뀌는 경계를 찾으세요. 그리고 뒤 문장의 And가 주어진 문장에 '덧붙이는' 내용인지 확인하면 확실해집니다.</div>'''

S['40'] = '<h2>40번 · 요약문 완성 [2점]</h2>\n' + img(40) + '''<h3>① 요약문 구조</h3>
<p>우리는 의식적 사고 전에 위험에 대한 <b>(A)</b> 평가를 수행하는데, 감정에 기반한 결정을 먼저 내리고 나서 그것을 <b>(B)</b>할 이유를 만들어 낸다.</p>
<h3>② 정답: ① automatic(자동적인) … support(뒷받침하다)</h3>
<div class="key"><span class="en">an <b>unconscious</b> “danger detector” that determines whether or not something or someone is safe <b>before we can even begin to consciously make a determination</b> … most human decisions are made emotionally, and then we collect or generate the facts <b>to justify</b> these decisions.</span><br>(A) 무의식적으로, 의식보다 먼저 → <b>automatic</b>, (B) 결정을 정당화할 사실을 모은다 → <b>support</b></div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li class="ans">① automatic … support <span class="o">— 정답.</span></li>
<li>② purposeful … challenge <span class="x">— 의도적이지 않고(unconscious), 결정에 '도전'하는 게 아니라 정당화합니다.</span></li>
<li>③ analytical … confirm <span class="x">— confirm은 그럴듯하지만 '분석적' 평가는 감정 기반 결정과 반대입니다. 한 칸만 맞는 함정.</span></li>
<li>④ detailed … explain <span class="x">— '세부적인' 평가는 근거가 없습니다.</span></li>
<li>⑤ immediate … alter <span class="x">— immediate는 그럴듯하지만, 이유를 만들어 결정을 '바꾸는' 게 아닙니다. 한 칸만 맞는 함정.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">It is <b>what</b> psychologist Joseph LeDoux has suggested is an unconscious “danger detector” <b>that</b> determines …</span><br>what + (주어+동사 삽입: LeDoux has suggested) + is …: 'LeDoux가 ~라고 제안한 것'. 삽입절을 괄호로 묶으면 what is an unconscious danger detector가 보입니다.</div>
<div class="tip"><b>요약문 공략법</b> (A)는 <b>before conscious thinking</b>과, (B)는 <b>justify</b>와 짝을 찾으세요. 요약문의 단어는 본문의 단어를 반드시 다른 말로 바꿔 씁니다(justify → support).</div>'''

json.dump(S, open('secs_06g2.json', 'w'), ensure_ascii=False)
print(len(S))
