import json
B = 'https://cdn.jsdelivr.net/gh/KKHLAND/edu-hub@333579c/blog-assets/v2_0324g3/'
def img(n, lab=None):
    lab = lab or f'{n}번'
    return (f'<img src="{B}q{n}.png" alt="2026년 3월 고3 영어 {lab} 발문 지문 선택지 해석 어휘">\n'
            '<p class="cap">발문·지문·선택지·해석·어휘</p>\n')
S = {}
S['21'] = '<h2>21번 · 함축 의미 추론 [3점]</h2>\n' + img(21) + '''<h3>① 지문 구조</h3>
<p><b>도입</b> 뛰어난 음악가는 '발명가'가 아니어도 '혁신가'일 수 있다 → <b>비판</b> 그런데 현대의 '경매'는 새로움을 열망하며 음악을 하나의 '사물', 즉 기술(technique)로만 본다 → <b>비유</b> 자동차·가전 전시회처럼 해마다 '새롭고 개선된' 것을 내놓는 끝없는 진보, 더 멀리·더 빠르게·더 강하게라는 '군비 경쟁' → <b>밑줄</b> '과학적 연구'의 모방작이 넘쳐 나는 시대에 음악가도 다른 모든 사람처럼 '연구자'가 되어야 한다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">In this arms race, each new music, <b>breaking its predecessor’s records</b>, offers itself as the last thing in modernity; and each musician … <b>claims the patent on the invention</b>.</span><br>→ '연구자'가 된다는 것은 기록 경신, 특허, 신제품처럼 <b>측정·입증 가능한 기술적 새로움과 진보</b>를 내세우는 경쟁에 뛰어든다는 뜻입니다. 따옴표("researchers")와 pastiches(모방작)라는 말에서 필자의 <b>비꼬는 어조</b>가 드러납니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 거장 작곡가의 대표 스타일을 충실히 재현한다 <span class="x">— 정반대입니다. 글은 전임자를 '구식'으로 몰아내는 새로움 경쟁을 말합니다.</span></li>
<li>② 예술 작품의 질이 시간적 요인에 좌우되지 않음을 인정한다 <span class="x">— 오히려 '작년보다 새로운 것'이라는 시간적 진보에 매달린다는 내용입니다.</span></li>
<li class="ans">③ 기술적으로 입증 가능한 새로움과 형식적 진보에 집중하는 지배적 흐름을 받아들인다 <span class="o">— 정답.</span> technique alone, new and improved, never-ending progress와 정확히 대응합니다.</li>
<li>④ 음악이 미적 기준과 문화 정체성 유지에 미치는 영향을 의심한다 <span class="x">— 미적 기준·문화 정체성은 언급되지 않았습니다.</span></li>
<li>⑤ 음악가가 자신의 창작에 갖는 근본적 독립성을 구별한다 <span class="x">— '모두와 마찬가지로(just like everyone else)' 흐름에 휩쓸린다는 내용이므로 독립성과 반대입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">… the eager need for novelty … involves the idea that a musical act is a thing, <b>in which case</b>, music is no more than technique, technique alone.</span><br>in which case는 '그런 경우에는'이라는 뜻으로 앞 절 전체를 받습니다. no more than = 단지 ~에 불과한. → "음악 행위가 하나의 사물이라는 생각을 수반하며, 그 경우 음악은 기술, 오직 기술에 불과하다."</div>
<div class="tip"><b>함축 의미 공략법</b> ① 밑줄에 따옴표가 있으면 필자가 그 말을 <b>비꼬거나 거리를 두는</b> 경우가 많습니다. ② 밑줄 바로 앞의 비유(군비 경쟁, 특허, 기록 경신)를 한 단어로 요약해 보세요 → '측정 가능한 새로움 경쟁'. ③ 그 요약과 같은 말을 쓴 선택지가 정답입니다.</div>'''

S['29'] = '<h2>29번 · 어법 [3점]</h2>\n' + img(29) + '''<h3>① 지문 구조</h3>
<p><b>다윈의 통찰</b> 유전은 보수적이어서 생물은 환경과 상관없이 비슷하지만 변이가 있는 자손을 많이 낳는다 → 그래서 자원보다 많은 자손을 낳는 '과잉 번식'이 생긴다 → <b>문제</b> 필요와 기회는 완벽히 맞지 않는다. 유전은 환경과 무관하게 능력을 만든다 → <b>결론</b> 그래서 모든 생물이 어디서나 살 수는 없다.</p>
<h3>② 정답: ④ which → in which (= where)</h3>
<div class="key"><span class="en">Offspring cannot anticipate the nature of the conditions ④ <b>which</b> they find themselves, …</span><br>관계사절 they find themselves를 보면 find의 목적어(themselves)가 이미 있어 <b>문장이 완전합니다</b>. 관계대명사 which는 뒤에 불완전한 문장이 와야 하므로 틀렸습니다. '그 조건 <b>속에</b> 자신이 처해 있음을 알게 되다'이므로 <b>in which</b>(또는 where)가 맞습니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① producing <span class="x">— 앞 절(it is in the nature … to impose itself)의 결과를 덧붙이는 분사구문입니다. 생물이 자손을 '낳는' 능동이므로 현재분사가 맞습니다.</span></li>
<li>② imply <span class="x">— 주어는 these fundamental aspects(복수)입니다. of the nature of the organism은 수식어이므로 복수 동사 imply가 맞습니다.</span></li>
<li>③ them <span class="x">— 사용할 기회의 대상인 necessary resources(복수)를 가리키므로 them이 맞습니다.</span></li>
<li class="ans">④ which <span class="o">— 정답(틀림).</span> 뒤 문장이 완전하므로 in which가 와야 합니다.</li>
<li>⑤ minor <span class="x">— be동사 are의 보어 자리이므로 형용사 minor가 맞습니다. compared to(~에 비해)와 함께 '사소하다'는 뜻입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">… organisms routinely producing more offspring <b>than there are resources to support them</b>.</span><br>organisms가 의미상 주어인 독립분사구문(with + 목적어 + -ing)이고, than 뒤에 there are 구문이 비교 대상으로 왔습니다. → "자손을 부양할 자원보다 더 많은 자손을 생물이 통상적으로 낳으며"</div>
<div class="tip"><b>어법 공략법</b> 관계사 밑줄은 <b>뒤 문장이 완전한지</b>부터 보세요. 완전하면 관계부사(where) 또는 전치사+관계대명사(in which), 불완전하면 관계대명사(which, that)입니다. find oneself + 장소(~에 처해 있다)처럼 전치사가 필요한 표현을 떠올리면 확신이 생깁니다.</div>'''

S['30'] = '<h2>30번 · 문맥상 낱말의 쓰임 [2점]</h2>\n' + img(30) + '''<h3>① 지문 구조</h3>
<p><b>주장</b> 고유 명사가 아닌 이름을 붙일 때마다 우리는 대상의 세부적 차이를 버린다(abstract away) → <b>예시</b> '꽃', '잔디'라는 말은 데이지와 클로버, 여러 풀의 차이를 묶어 버린다 → <b>확대해 보면</b> 어디에나 개별성이 있다 → <b>목적에 따라</b> 대부분은 차이를 무시해도 되지만, 경기장 관리인에게는 중요하다.</p>
<h3>② 정답 근거: ② acknowledges → neglects</h3>
<div class="key"><span class="en">“Lawn” ② <b>acknowledges</b> the varieties of grass and all the nongrassy plants that are there.</span><br>바로 앞 문장에서 '꽃'이라는 말은 여러 종류를 <b>하나로 묶어 버린다</b>(co-categorizes)고 했습니다. '잔디'도 같은 예시이므로, 그 안의 다양한 풀과 풀이 아닌 식물을 '인정하는' 것이 아니라 <b>무시하는(neglects, ignores)</b> 것이어야 합니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① differences <span class="x">— 네 개의 보통 명사는 그것들의 '차이'를 생략한다. abstract away from its particularities와 같은 뜻입니다.</span></li>
<li class="ans">② acknowledges <span class="o">— 정답(부적절).</span> 차이를 버리는 예시이므로 neglects가 와야 합니다.</li>
<li>③ alike <span class="x">— 확대해 보면 어떤 데이지 두 송이도 정확히 '같지' 않다. individuality and uniqueness와 이어집니다.</span></li>
<li>④ ignored <span class="x">— 실용적인 목적에서는 그 차이를 '무시해도' 된다. 뒤의 Not so, however(경기장 관리인은 다르다)와 대조됩니다.</span></li>
<li>⑤ co-categorized <span class="x">— 무한한 정신에게는 각 풀잎이 동료들과 '한 범주로 묶일' 필요가 없다. 마지막 문장(각자 이름을 가질 수 있다)과 맞습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">And to an infinite mind, with infinite memory, each blade of grass, <b>with its own distinct life history</b>, need not be co-categorized with all its fellows.</span><br>주어 each blade of grass와 동사 need not be 사이에 with 부사구가 끼어 있습니다. 조동사 need not(~할 필요가 없다) 뒤에 수동 원형 be co-categorized.</div>
<div class="tip"><b>어휘 공략법</b> ① 예시가 여러 개 나열되면 <b>모두 같은 방향</b>이어야 합니다('꽃'이 차이를 묶는다면 '잔디'도 차이를 버린다). ② 반대 방향이 시작되는 곳에는 however, Not so 같은 표지가 있습니다. 표지 없이 방향이 바뀌는 낱말이 정답입니다.</div>'''

S['42'] = '<h2>42번 · 장문 어휘 [3점] (41번 제목 포함)</h2>\n' + img('41-42', '41~42번') + '''<h3>① 지문 구조</h3>
<p><b>출발</b> Macherey는 Tolstoy의 작품이 1905년 러시아 혁명을 비추는 거울이라는 Lenin의 주장에 동의한다 → <b>단서</b> 하지만 그 거울은 결코 세상의 '직접적인' 반영이 아니다. 결함과 사각지대가 있다 → <b>핵심</b> 문학은 비추는 것만큼 비추지 '않는' 것(배제·왜곡·부재) 때문에 중요하다 → <b>보강</b> 거울 속 모습은 조각나 있을 수도 있다(George Eliot의 인용) → <b>마무리</b> 거울의 관점 자체는 보이지 않아서 우리는 그것을 의심 없이 받아들이기 쉽다.</p>
<p>41번 제목은 '문학이라는 거울이 보여 주지 못하는 것의 의미'인 <b>① The Significance of What Literary Mirrors Fail to Show</b>입니다. ④번(현실을 있는 그대로 비추는 힘)은 글이 반박하는 생각입니다.</p>
<h3>② 정답 근거: (d) praising → reproaching</h3>
<div class="key"><span class="en">‘The mirror is doubtless <b>defective</b>; the outlines will sometimes be disturbed …’, remarks George Eliot …, (d) <b>praising</b> the kind of naive realism which holds that art (or mirrors) always tell it like it is.</span><br>Eliot은 거울이 '불완전하다(defective)'고 말합니다. 그렇다면 예술이 '언제나 있는 그대로를 말해 준다'고 믿는 소박실재론을 <b>칭찬</b>하는 것이 아니라 <b>비판(reproaching, criticizing)</b>하는 것입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>(a) direct <span class="x">— 거울 비추기는 복잡한 일이며 결코 세상의 '직접적인' 반영이 아니다. by no means와 함께 적절합니다.</span></li>
<li>(b) figure <span class="x">— 거울 속에 '나타나지' 않는 것들이 있다. figure in은 '~에 나타나다'라는 뜻입니다.</span></li>
<li>(c) absences <span class="x">— 거울은 이러한 '부재'를 깨닫게 해 준다. 바로 뒤 see more clearly what isn't there와 맞습니다.</span></li>
<li class="ans">(d) praising <span class="o">— 정답(부적절).</span> 불완전하다는 말과 '늘 있는 그대로 보여 준다'는 믿음은 반대이므로 비판해야 합니다.</li>
<li>(e) invisible <span class="x">— 거울 자체에서는 포착할 수 없는 관점이므로 우리에게 '보이지 않는다'. 앞의 cannot be captured와 같은 말입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">In fact, they are <b>as significant for what they don’t reflect</b> — for their exclusions and distortions — <b>as for what they do</b>.</span><br>as ~ as 비교 구문에서 비교 대상은 for what they don't reflect와 for what they do(= reflect)입니다. → "문학 작품은 비추는 것만큼이나 비추지 않는 것 때문에 중요하다."</div>
<div class="tip"><b>장문 어휘 공략법</b> ① 인용문 바로 뒤의 분사(praising, criticizing)는 <b>인용문의 내용과 같은 방향</b>이어야 합니다. 인용문이 '결함'을 말하면 '있는 그대로'를 믿는 쪽을 비판하는 것입니다. ② 41번 제목을 먼저 풀어 글의 결론(보이지 않는 것이 중요하다)을 잡으면 42번의 방향이 쉽게 보입니다.</div>'''

S['31'] = '<h2>31번 · 빈칸 추론(단어) [2점]</h2>\n' + img(31) + '''<h3>① 빈칸 문장의 역할</h3>
<div class="key"><span class="en">Professional art, <b>then</b>, is inherently ________.</span><br>then(그렇다면)으로 시작하는 결론 문장입니다. 바로 앞 문장이 근거입니다.</div>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">In Western culture, it is almost impossible to <b>separate professional from commercial</b>, and so the artist is legitimized by their <b>ability to earn money</b>.</span><br>전문성 = 상업성, 예술가의 정당성 = 돈 버는 능력. 그러므로 전문 예술은 본질적으로 <b>⑤ capitalist(자본주의적)</b>입니다. 첫 문장 'Art without commerce is a hobby'와 for money, for that is the only marker of success도 같은 방향입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① universal(보편적인) <span class="x">— 글은 '서양 문화에서'라는 특정 조건을 말합니다.</span></li>
<li>② individualist(개인주의적인) <span class="x">— 개인의 창작 충동이 아니라 시장의 평가가 기준이라는 내용입니다.</span></li>
<li>③ romantic(낭만적인) <span class="x">— <b>함정</b>. 예술을 위한 창작은 '절망적으로 낭만적'이라고 '평가절하'된다고 했으니, 전문 예술의 성격과 반대입니다.</span></li>
<li>④ collective(집단적인) <span class="x">— 집단 창작은 언급되지 않았습니다.</span></li>
<li class="ans">⑤ capitalist(자본주의적인) <span class="o">— 정답.</span> commerce, money, earn money가 모두 가리키는 말입니다.</li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">Of course one can engage in art, but <b>it better be</b> for money, <b>for</b> that is the only marker of success.</span><br>it better be = it had better be(~이어야 한다)의 구어 표현. 뒤의 for는 접속사로 '왜냐하면'입니다.</div>
<div class="tip"><b>빈칸(단어) 공략법</b> then, thus, therefore로 시작하는 결론 빈칸은 <b>바로 앞 문장의 핵심어를 추상화</b>한 단어가 정답입니다(commercial, earn money → capitalist). 글 속에 나온 단어(romantic)를 그대로 쓴 선택지는 반대 맥락인지 꼭 확인하세요.</div>'''

S['32'] = '<h2>32번 · 빈칸 추론(구) [2점]</h2>\n' + img(32) + '''<h3>① 빈칸 문장의 역할</h3>
<div class="key"><span class="en">This is why all educated citizens need ________. <b>For</b> we need to understand why history takes the form that it does in scholarly accounts.</span><br>This is why(이것이 ~한 이유이다)로 앞 내용의 결론을 내리고, 바로 뒤 For(왜냐하면)가 빈칸의 이유를 설명합니다.</div>
<h3>② 정답 근거</h3>
<p>앞: 이야기는 선택적·주관적이며 생략으로 늘 왜곡한다 → 그래서 사실만으로는 부족하다. 뒤: 학술적 서술에서 역사가 왜 그런 형태를 취하는지 이해해야 하며, 학문적 역사 논증은 비공식적인 이야기 듣기와 다르다(disciplinary knowledge). 두 쪽을 합치면 <b>② not just facts about the past but history as a discipline</b>(과거에 대한 사실뿐 아니라 학문으로서의 역사)입니다.</p>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 자기 목적을 위해 역사를 전유하는 능력 <span class="x">— 왜곡을 경계하는 글의 방향과 반대입니다.</span></li>
<li class="ans">② 과거에 대한 사실뿐만 아니라 학문으로서의 역사 <span class="o">— 정답.</span> scholarly accounts, disciplined historical argument와 대응합니다.</li>
<li>③ 간과된 역사적 순간을 기록하는 비공식적 방법 <span class="x">— 글은 '비공식적으로는 얻을 수 없다'고 했습니다.</span></li>
<li>④ 문화적 특수성을 유지하기 위한 징계 조치 <span class="x">— disciplinary를 '징계'로 비튼 함정입니다. 여기서는 '학문의'라는 뜻입니다.</span></li>
<li>⑤ 과거를 성찰할 때의 확고한 도덕 감각 <span class="x">— 숨은 도덕적 판단은 이야기의 문제점으로 언급되었을 뿐입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">Stories influence subtly, invest power, make hidden moral judgement and always <b>distort by omission</b>, whether intentionally or not.</span><br>동사 네 개가 주어 Stories에 이어지고, whether A or not(A이든 아니든)이 양보의 부사절로 붙었습니다.</div>
<div class="tip"><b>빈칸(구) 공략법</b> 빈칸 뒤에 For, Because가 오면 그 이유가 곧 빈칸의 내용입니다. 또 disciplinary처럼 <b>다의어</b>가 선택지에 나오면 글 속 의미(학문의)와 선택지 의미(징계의)가 같은지 확인하세요.</div>'''

S['33'] = '<h2>33번 · 빈칸 추론(구) [3점]</h2>\n' + img(33) + '''<h3>① 빈칸 문장의 역할</h3>
<div class="key"><span class="en">A profound building is ________.</span><br>마지막 문장, 즉 글 전체의 결론입니다. 글 전체에서 '좋은 건축'을 정의한 부분을 모으면 됩니다.</div>
<h3>② 정답 근거</h3>
<ul class="ch">
<li>건축은 행동을 이끄는 공간적 '연출'이며 감정과 지각까지 유도한다.</li>
<li>설계자는 인간의 <b>행동과 욕구</b>를 직관하고, 거주자의 <b>본능적 필요와 의도</b>에 공명한다.</li>
<li>설계자는 상상 속에서 미래 거주자를 대신해 그 집을 '살고, 쓰고, 느낀다'.</li>
<li>창문은 거주자가 '보고 싶은 곳'에, 계단은 '가고 싶은 곳'에 놓인다 → 설명서가 필요 없다.</li>
</ul>
<p>건물이 사람의 몸의 움직임과 마음의 욕구를 그대로 이어받아 구현한다는 것이므로 <b>③ an extension of human bodily and mental actions and capabilities</b>(인간의 신체적·정신적 행동과 능력의 연장)가 정답입니다.</p>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 당대의 문화적 사고방식을 전하는 도구 <span class="x">— 문화 전달은 언급되지 않았습니다.</span></li>
<li>② 비전문가의 의견과 무관한 공간 논리 <span class="x">— 오히려 사용자(비전문가)의 욕구에 공명해야 한다고 했습니다.</span></li>
<li class="ans">③ 인간의 신체적·정신적 행동과 능력의 연장 <span class="o">— 정답.</span> behavior and desire, natural and instinctual needs와 대응합니다.</li>
<li>④ 설계자의 미적 취향의 건축적 표현 <span class="x">— <b>함정</b>. 설계자가 주인공처럼 보이지만, 설계자는 '거주자를 대신해서' 느낄 뿐 자기 취향을 드러내지 않습니다.</span></li>
<li>⑤ 외관이 기능을 가리는 구조물 <span class="x">— 정반대입니다. 구조와 용도를 말없이 '드러낸다(reveals)'고 했습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">Successful architecture does not need manuals or signage for its use, <b>as</b> it reveals its very structure and use in a wordless manner.</span><br>as는 이유의 접속사(~이므로)입니다. very는 명사 앞에서 '바로 그'라는 강조의 형용사입니다.</div>
<div class="tip"><b>결론 빈칸 공략법</b> 글 마지막의 빈칸은 <b>글 전체의 요약</b>입니다. 예시(창문, 계단)를 한 줄로 일반화하세요: '사람이 원하는 곳에 건물이 응답한다' → 인간 행동과 능력의 연장. 주어(설계자)에 끌려 ④번을 고르지 않도록, '누구의 욕구에 맞추는가'를 확인하세요.</div>'''

S['34'] = '<h2>34번 · 빈칸 추론(구) [3점]</h2>\n' + img(34) + '''<h3>① 빈칸 문장의 역할</h3>
<div class="key"><span class="en">It would, <b>in short</b>, ________.</span><br>in short(요컨대)로 시작하므로 바로 앞 문장을 짧게 바꿔 말한 것이 정답입니다.</div>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">It might take the form of some vector of information that summarizes your situation and value across many features — something that compactly represents <b>your position in the multidimensional space of classification situations</b>.</span><br>여러 특징에 걸친 나의 상황과 가치를 요약하는 벡터 = 분류 공간에서의 <b>나의 위치</b>. 이를 줄이면 <b>③ characterize your social location</b>(당신의 사회적 위치를 특징짓다)입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 당신의 디지털 흔적을 숨긴다 <span class="x">— 흔적을 모아 압축하는 것이지 숨기는 것이 아닙니다.</span></li>
<li>② 사람의 오해를 바로잡는다 <span class="x">— 오해는 나오지 않습니다.</span></li>
<li class="ans">③ 당신의 사회적 위치를 특징짓는다 <span class="o">— 정답.</span> your position, your situation and value와 대응합니다.</li>
<li>④ 교환 가치가 있는 것을 정의한다 <span class="x">— resource, value라는 단어에 끌린 함정입니다. 글은 '무엇이 가치 있는가'가 아니라 '나'를 요약합니다.</span></li>
<li>⑤ 널리 퍼진 사회적 경향을 나타낸다 <span class="x">— 사회 전체의 경향이 아니라 한 개인(your)에 관한 내용입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">It is diverse and multidimensional and, of course, it is <b>not all</b> gathered into a single place or condensed down to a single quantity. But in principle it <b>might be</b>.</span><br>not all은 부분 부정(모두 ~인 것은 아니다). might be 뒤에는 gathered … quantity가 생략되었습니다. → "하지만 원칙적으로는 그렇게 될 수도 있다."</div>
<div class="tip"><b>in short 빈칸 공략법</b> in short, in other words, that is 뒤의 빈칸은 <b>바로 앞 문장의 재진술</b>입니다. 앞 문장의 소유격(your position)과 핵심 명사(position → location)가 선택지에 어떻게 바뀌어 들어갔는지 찾으세요.</div>'''

S['36'] = '<h2>36번 · 글의 순서 [2점]</h2>\n' + img(36) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">Dennett: 도덕적 고려는 '대화 중단자' 역할. 우리는 늘 정당화를 요구할 수 있는 이성적 존재이고, 이것은 유용한 특성이었다</td><td class="l">→ 그 특성의 '문제점'이 이어질 차례</td></tr>
<tr><td>(C)</td><td class="l"><b>The problem is that</b> … 끝없이 "그건 무엇이 정당화하지?"라고 물으며 결정을 못 내릴 수 있다</td><td class="l">'유용한 특성'의 문제점 → 주어진 글 바로 뒤</td></tr>
<tr><td>(A)</td><td class="l"><b>This</b> is potentially as much a problem for our own private deliberations … Dennett은 숙고를 멈추는 말이 유용하다고 함</td><td class="l">This = (C)의 끝없는 질문 → (C) 뒤</td></tr>
<tr><td>(B)</td><td class="l">"That would be morally wrong!" would appear to work <b>in this manner</b></td><td class="l">in this manner = (A)의 '숙고를 멈추는 말' → (A) 뒤</td></tr>
</table>
<h3>② 정답: ④ (C)-(A)-(B)</h3>
<div class="key">이성적 존재의 장점 → (C) 그런데 끝없이 정당화를 물을 수 있다는 문제 → (A) This(그 문제)는 사적 숙고에서도 마찬가지 → 그래서 숙고를 멈추는 말이 유용 → (B) '도덕적으로 잘못이야!'가 바로 그런 방식으로 작동한다(예시).</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— This가 가리킬 '문제'가 주어진 글에 없습니다. 주어진 글은 장점(served us well)으로 끝납니다.</span></li>
<li>(B)로 시작(②, ③) <span class="x">— in this manner가 받을 '숙고를 멈추는 말'의 설명이 아직 없습니다.</span></li>
<li>(C)-(B)-(A)(⑤) <span class="x">— (B)의 in this manner가 (C)의 '끝없는 질문'을 받으면 뜻이 정반대가 됩니다. 멈추게 하는 장치는 (A)에서 처음 소개됩니다.</span></li>
</ul>
<div class="tip"><b>순서 공략법</b> 주어진 글이 '장점'으로 끝나면 다음은 대개 '문제점(The problem is)'입니다. 그다음 this, in this manner 같은 지시어가 <b>무엇을 받는지</b> 한 단어로 적어 두면 순서가 저절로 정해집니다.</div>'''

S['37'] = '<h2>37번 · 글의 순서 [3점]</h2>\n' + img(37) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">팽창이라 하면 유한한 경계가 늘어나는 우주를 떠올리고, 우주가 '어디로' 팽창하는지 궁금해진다</td><td class="l">→ 그 질문에 대한 '답'이 이어질 차례</td></tr>
<tr><td>(B)</td><td class="l"><b>Unfortunately, the only answer I can give you</b> … 우주는 어디로도 팽창하지 않고 스스로 안에서 팽창한다</td><td class="l">주어진 글의 질문에 대한 답 → 바로 뒤</td></tr>
<tr><td>(A)</td><td class="l"><b>In contrast to</b> our inflating balloon … 늘어나는 것은 시공간 '구조(structure)'다</td><td class="l">(B)의 '스스로 안에서 팽창'을 풍선과 대조해 설명 → (B) 뒤</td></tr>
<tr><td>(C)</td><td class="l"><b>This structure</b> or fabric of space and time is elastic</td><td class="l">This structure = (A)의 the structure of space and time → (A) 뒤</td></tr>
</table>
<h3>② 정답: ② (B)-(A)-(C)</h3>
<div class="key">우주는 어디로 팽창하나? → (B) 답: 어디로도 아니다, 스스로 안에서 팽창한다 → (A) 풍선이나 가스 누출과 달리, 늘어나는 것은 시공간의 구조다 → (C) 이 구조는 탄력적이라 블랙홀처럼 당기기도, 팽창하기도 한다.</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— 질문에 대한 답(B) 없이 바로 대조 설명이 나오면 무엇과 대조하는지 불분명합니다.</span></li>
<li>(B)-(C)-(A)(③) <span class="x">— <b>함정</b>. (C)의 This structure가 가리킬 '구조'라는 말이 (B)에는 없습니다. structure는 (A)에서 처음 등장합니다.</span></li>
<li>(C)로 시작(④, ⑤) <span class="x">— This structure가 받을 말이 주어진 글에 없습니다.</span></li>
</ul>
<div class="tip"><b>명사 지시어 공략법</b> This structure, these factors처럼 <b>지시어+명사</b>가 나오면, 그 명사가 <b>처음 등장한 단락</b>을 찾으세요. 그 단락이 바로 앞에 와야 합니다. 질문(Q)으로 끝나는 주어진 글 뒤에는 '답(answer)'이 먼저 옵니다.</div>'''

S['38'] = '<h2>38번 · 문장 삽입 [2점]</h2>\n' + img(38) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<div class="key"><span class="en">According to McNeil and Duncan, gesture is different from language <b>in that it does not present the speaker with such choices</b>.</span><br>"McNeil과 Duncan에 따르면, 제스처는 화자에게 <b>그러한 선택</b>을 제시하지 않는다는 점에서 언어와 다르다."<br>→ 단서 1: <b>such choices</b> — 앞에 언어가 강요하는 '선택'의 구체적 설명이 있어야 합니다.<br>→ 단서 2: 뒤에는 '그 대신 제스처는 무엇을 하는가'가 이어져야 합니다.</div>
<h3>② 위치별 점검</h3>
<table>
<tr><th>위치</th><th>앞 문장</th><th>뒤 문장</th><th>판단</th></tr>
<tr><td>①</td><td class="l">언어의 범주적 요구 + 제스처의 심상적 가능성</td><td class="l">For example, 완료/진행 중 하나를 골라야 함</td><td>✕ 아직 '선택'의 예가 없음</td></tr>
<tr><td>②</td><td class="l">완료/진행을 반드시 골라야 함(예시)</td><td class="l">This kind of choice는 언어의 특징</td><td>✕ This kind of choice가 바로 앞 예시를 받음</td></tr>
<tr><td class="o">③</td><td class="l">이런 선택은 기호 체계로서 <b>언어</b>의 특징</td><td class="l"><b>Instead, it</b> offers a kind of glue</td><td class="o">○ it = 제스처, Instead = 선택 대신</td></tr>
<tr><td>④</td><td class="l">제스처는 일종의 접착제를 제공</td><td class="l">이 관점에서 말과 제스처는 중복이 아님</td><td>✕ 제스처 설명이 이어지는 중</td></tr>
<tr><td>⑤</td><td class="l">중복도 번역도 아님</td><td class="l">Rather, 최소 단위는 둘의 결합</td><td>✕ not A … Rather B로 연결</td></tr>
</table>
<h3>③ 정답 근거</h3>
<p>③ 뒤 문장의 <span class="en">it</span>은 무엇일까요? 바로 앞 문장의 주어는 This kind of choice와 language이므로 it이 '제스처'일 수 없습니다. 주어진 문장을 넣으면 it = gesture가 되고, Instead(선택을 주는 대신)가 자연스럽게 이어집니다. 정답 <b>③</b>.</p>
<div class="tip"><b>문장 삽입 공략법</b> 대명사(it)와 연결어(Instead)로 시작하는 문장의 <b>바로 앞</b>을 의심하세요. it이 가리킬 명사가 바로 앞에 없거나, Instead가 무엇을 대신하는지 불분명한 곳이 주어진 문장의 자리입니다.</div>'''

S['39'] = '<h2>39번 · 문장 삽입 [3점]</h2>\n' + img(39) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<div class="key"><span class="en"><b>Nonetheless</b>, for most outsiders <b>even completely transparent practices</b> do not lift the veil behind which such forms of knowledge are hidden — …</span><br>"그럼에도 불구하고, 대부분의 외부인에게는 <b>완전히 투명한 관행조차</b> 그러한 지식이 숨겨진 장막을 걷어 내지 못한다."<br>→ 단서 1: <b>Nonetheless</b> — 앞은 '개방·투명해졌다'는 긍정적 내용이어야 합니다.<br>→ 단서 2: <b>even transparent practices</b> — 앞에 '개방성(openness)'이 언급되어야 합니다.</div>
<h3>② 위치별 점검</h3>
<table>
<tr><th>위치</th><th>앞 문장</th><th>뒤 문장</th><th>판단</th></tr>
<tr><td>①</td><td class="l">전문 지식 습득 = 지식 공동체의 구성원이 되는 것</td><td class="l">신입은 전문가에게 배우며 사회화된다</td><td>✕ 정의 → 과정으로 자연스러움</td></tr>
<tr><td>②</td><td class="l">사회화</td><td class="l">Often 입회 절차와 시험</td><td>✕ 과정 설명이 이어짐</td></tr>
<tr><td>③</td><td class="l">입회 절차</td><td class="l">전근대에는 비밀·충성 시험</td><td>✕ 과거 사례로 이어짐</td></tr>
<tr><td>④</td><td class="l">전근대의 비밀주의</td><td class="l">오늘날에는 개방성으로 이동</td><td>✕ 과거 → 현재 대조</td></tr>
<tr><td class="o">⑤</td><td class="l">이상이 <b>개방성(openness)</b>으로 옮겨 갔다</td><td class="l"><b>Other, more active strategies</b> are needed</td><td class="o">○ 개방 → 그럼에도 이해 불가 → 그래서 더 적극적 전략</td></tr>
</table>
<h3>③ 정답 근거</h3>
<p>⑤ 앞뒤를 바로 이으면 '개방성이 이상이 되었다 → 더 적극적인 다른 전략이 필요하다'가 되어 <b>논리의 빈틈</b>이 생깁니다. 왜 개방만으로 부족한지가 빠져 있죠. 주어진 문장이 '투명해도 훈련 없이는 이해할 수 없다'는 이유를 채워 줍니다. 정답 <b>⑤</b>.</p>
<div class="tip"><b>함정 주의</b> ④ 자리도 '과거 → 현재'로 흐름이 바뀌어서 고민되지만, 주어진 문장의 transparent practices는 '개방성'이 언급된 <b>뒤</b>에만 쓸 수 있습니다. 또 마지막 문장의 Other(다른) 전략은 '투명성만으로는 안 된다'는 말이 앞에 있어야 성립합니다.</div>'''

S['40'] = '<h2>40번 · 요약문 완성 [2점]</h2>\n' + img(40) + '''<h3>① 요약문 구조</h3>
<div class="key"><span class="en">As goals mature over the course of one’s life, older adults become more selective and <b>(A)</b> their goals according to priorities, sustaining motivation and well-being through a(n) <b>(B)</b> self-view.</span><br>(A) = 우선순위에 따라 목표를 어떻게 하는가 / (B) = 어떤 자기관</div>
<h3>② 정답 근거</h3>
<ul class="ch">
<li><b>(A)</b> <span class="en">subject to the balance and organisation of one’s goals in relation to life priorities / goal alignment</span> → 목표를 균형 있게 <b>조정(coordinate)</b>한다</li>
<li><b>(B)</b> <span class="en">a positive self-perception / developing a well-rounded self-view</span> → <b>긍정적인(favorable)</b> 자기관</li>
</ul>
<p>정답 <b>② coordinate ······ favorable</b>.</p>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① coordinate / objective(객관적인) <span class="x">— (A)는 맞지만, 본문은 '객관적' 자기관이 아니라 '긍정적' 자기관을 말합니다.</span></li>
<li class="ans">② coordinate / favorable <span class="o">— 정답.</span></li>
<li>③ organize / inconsistent(일관성 없는) <span class="x">— (A)는 가능하지만 (B)가 정반대입니다(well-rounded).</span></li>
<li>④ disassociate(분리하다) / positive <span class="x">— (B)는 맞지만, 목표를 '분리'하는 것이 아니라 '정렬(alignment)'합니다.</span></li>
<li>⑤ disassociate / indefinite(불명확한) <span class="x">— 둘 다 반대 방향입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">… motivation may even attain its highest levels in the later stages of life, <b>subject to</b> the balance and organisation of one’s goals in relation to life priorities.</span><br>subject to + 명사는 '~에 따라, ~을 조건으로'라는 뜻입니다. → "삶의 우선순위와 관련한 목표의 균형과 조직화 여부에 따라"</div>
<div class="tip"><b>요약문 공략법</b> ① (A)·(B) 칸마다 본문에서 <b>같은 뜻의 단어</b>를 찾아 밑줄 그으세요(alignment·organisation → coordinate, positive·well-rounded → favorable). ② 한 칸만 맞는 선택지(①, ③, ④)가 매력적인 오답으로 꼭 섞여 있으니, 두 칸을 모두 확인한 뒤 고르세요.</div>'''

json.dump(S, open('secs_g3.json', 'w'), ensure_ascii=False)
print(len(S))
