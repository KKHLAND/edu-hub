import json
B = 'https://cdn.jsdelivr.net/gh/KKHLAND/edu-hub@b342bb7/blog-assets/v2_0324g2/'
def img(n, lab=None):
    lab = lab or f'{n}번'
    return (f'<img src="{B}q{n}.png" alt="2026년 3월 고2 영어 {lab} 발문 지문 선택지 해석 어휘">\n'
            '<p class="cap">발문·지문·선택지·해석·어휘</p>\n')
S = {}
S['21'] = '<h2>21번 · 함축 의미 추론 [3점]</h2>\n' + img(21) + '''<h3>① 지문 구조</h3>
<p><b>주장</b> 존중하는 학습 공동체의 첫걸음은 오류가 있더라도 모든 생각과 답을 받아들이는 것 → <b>이유</b> 오답은 오개념에서 나오고, 그것이 드러나야 학생이 자기 생각을 마주할 수 있다 → <b>방법(밑줄)</b> 교사는 어떤 답에도 동의·비동의를 나타내는 말이나 몸짓 없이 모든 답을 기록한다 = '무표정(blank face)' → <b>목표</b> 정답의 출처를 교사에서 학생으로 옮긴다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">…recording all answers to be considered <b>without giving any verbal or physical expressions that indicate agreement or disagreement</b> with any answer.</span><br>→ 밑줄 바로 앞 문장이 'blank face'의 정의입니다. 동의·비동의 = <b>평가</b>, 말이나 몸짓을 하지 않음 = <b>억누름</b>.</div>
<p>교사가 고개를 끄덕이거나 표정이 굳으면 학생들은 곧바로 '정답인가 보다', '틀렸구나'를 알아챕니다. 그러면 학생이 스스로 생각을 방어할 기회가 사라지죠. 그래서 교사는 <b>답에 대한 평가 반응을 드러내지 않는 연습</b>을 해야 한다는 뜻입니다.</p>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 학생들의 감정적 갈등을 해결하려는 충동을 피하기 <span class="x">— 본문은 '감정 갈등'이 아니라 '답에 대한 반응'을 다룹니다.</span></li>
<li class="ans">② 학생들의 답에 대한 평가적 반응을 억누르기 <span class="o">— 정답.</span> agreement or disagreement → evaluative responses, without giving → suppressing으로 대응합니다.</li>
<li>③ 학습을 촉진하기 위해 모든 답을 정답으로 취급하기 <span class="x">— <b>가장 매력적인 함정</b>입니다. '모든 답을 받아들인다(accept)'는 '고려 대상으로 기록한다'는 뜻이지 '정답으로 인정한다'는 뜻이 아닙니다. 오답은 오개념으로 다뤄야 한다고 했습니다.</span></li>
<li>④ 수학 토론에서 오개념을 지적하기 <span class="x">— 지적(indicate)은 평가 반응 그 자체입니다. 무표정과 정반대입니다.</span></li>
<li>⑤ 엄격한 권위를 유지하려고 표정을 통제하기 <span class="x">— '표정 통제'는 맞지만 목적이 틀렸습니다. 목적은 권위가 아니라 안전한 학습 공동체입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">…unless these ideas <b>are allowed to be brought</b> to the forefront, we cannot help students confront their thinking.</span><br>unless = if not. allow A to do의 수동태(A is allowed to do)에 bring의 수동(be brought)이 이어진 형태입니다. help + 목적어 + 동사원형(confront)도 확인하세요. → "이런 생각들이 겉으로 드러나도록 허용되지 않으면, 우리는 학생들이 자기 생각을 마주하도록 도울 수 없다."</div>
<div class="tip"><b>함축 의미 공략법</b> ① 밑줄 바로 앞뒤 문장에서 '정의 문장'을 찾으세요(여기서는 without giving any … expressions). ② 선택지가 밑줄의 <b>행동</b>과 <b>목적</b>을 모두 맞혔는지 따로 확인하세요. ⑤처럼 행동만 맞고 목적이 틀린 선택지가 자주 나옵니다. ③ '모든 답을 받아들임'처럼 본문 단어를 과장한 선택지(③)는 지나친 일반화입니다.</div>'''

S['29'] = '<h2>29번 · 어법 [2점]</h2>\n' + img(29) + '''<h3>① 지문 구조</h3>
<p><b>주제</b> 산업 혁명은 새로운 제조 과정, 즉 현대 공장을 만들어 냈다 → <b>이전</b> 1850년 무렵까지 피아노 공방은 장인이 견습생을 가르치는 도제 방식, 한 번에 한 대씩 제작 → <b>이후</b> 미국에서 Chickering, Steinway가 진정한 피아노 공장을 세워 효율과 품질이 모두 향상.</p>
<h3>② 정답: ④ occurring → occurred</h3>
<div class="key"><span class="en">The development of a true piano factory ④ <b>occurring</b> first in the United States, led by Jonas Chickering…</span><br>주어 The development of a true piano factory 뒤에 <b>본동사가 없습니다</b>. led by …는 분사구문(과거분사)이므로 동사가 될 수 없습니다. 따라서 occurring을 과거 시제 동사 <b>occurred</b>로 바꿔야 문장이 완성됩니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① in which <span class="x">— 뒤에 a master builder taught younger workers the skills(완전한 4형식 문장)가 옵니다. 전치사+관계대명사 뒤에는 완전한 문장이 와야 하므로 적절합니다.</span></li>
<li>② did have <span class="x">— 동사를 강조하는 조동사 do. 주어가 복수(The larger piano shops)이고 과거이므로 did + 동사원형이 맞습니다.</span></li>
<li>③ made <span class="x">— 피아노는 '만들어지는' 대상이므로 were made(수동태)가 맞습니다.</span></li>
<li class="ans">④ occurring <span class="o">— 정답(틀림).</span> 문장에 본동사가 없으므로 occurred로 고쳐야 합니다.</li>
<li>⑤ its <span class="x">— one of the factories(단수, '공장 중 하나')를 가리키므로 단수 소유격 its가 맞습니다. one of + 복수명사는 '하나'가 주어라는 점을 기억하세요.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">…one of the factories of the time had its own iron casting facility <b>where it made its metal plates, which were thought to be the best available</b>.</span><br>관계부사 where(시설에서) 뒤에 계속적 용법의 which(그 금속판들은)가 이어집니다. which의 선행사는 metal plates(복수)이므로 were가 쓰였습니다.</div>
<div class="tip"><b>어법 공략법</b> ① 긴 주어가 나오면 <b>본동사부터 찾으세요</b>. 수식어(of a true piano factory, in the United States)를 괄호로 묶으면 동사가 비어 있는 게 보입니다. ② -ing·p.p.가 밑줄이면 '이 자리가 동사 자리인가?'를 먼저 물으세요. ③ one of + 복수명사는 단수 취급입니다.</div>'''

S['30'] = '<h2>30번 · 문맥상 낱말의 쓰임 [2점]</h2>\n' + img(30) + '''<h3>① 지문 구조</h3>
<p><b>문제</b> 논문 기반 박사 과정은 한 주제를 깊이 파고들어 철저한 탐구가 가능하지만, 초점을 좁힌다 → <b>결과</b> 지식과 기술의 폭이 제한되어 다양한 진로에 적응하는 능력을 <b>떨어뜨릴</b> 수 있다 → <b>해결</b> 유럽 일부 대학은 수업·세미나·인턴십을 결합한 구조화된 과정을 도입해 더 넓은 기술을 갖추게 한다.</p>
<h3>② 정답 근거: ③ facilitating → hindering</h3>
<div class="key"><span class="en">Consequently, this singular focus may <b>limit</b> the breadth of knowledge and skills…, potentially ③ <b>facilitating</b> students’ ability to adapt to diverse career paths…</span><br>앞 절의 동사가 limit(제한하다)입니다. 분사구문은 앞 절의 결과를 덧붙이므로 같은 부정적 방향이어야 합니다. 지식의 폭이 좁아지면 다양한 진로에 적응하는 능력이 '촉진되는(facilitating)' 것이 아니라 <b>방해받는(hindering, limiting)</b> 것입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① thorough <span class="x">— 깊이 파고드는 것(deep dive)은 '철저한' 탐구를 가능하게 한다. 적절합니다.</span></li>
<li>② less <span class="x">— 연구에 몰두하면 관련 분야를 탐색하는 시간이 '더 적어진다'. narrowing the focus와 같은 방향입니다.</span></li>
<li class="ans">③ facilitating <span class="o">— 정답(부적절).</span> limit의 결과이므로 hindering이 와야 합니다.</li>
<li>④ recognised <span class="x">— 한계를 '인식하고' 구조화된 접근을 시작했다. 해결책의 전제로 적절합니다.</span></li>
<li>⑤ transferable <span class="x">— 다양한 진로를 준비하게 하는 '전이 가능한(여러 분야에 쓸 수 있는)' 기술. broader skill set과 같은 방향입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en"><b>While</b> this deep dive into a particular area allows for thorough exploration and understanding, <b>it can also result in</b> narrowing the focus.</span><br>While은 여기서 '~이지만(양보)'입니다. 앞은 장점, 뒤는 단점. result in(~을 초래하다) 뒤에 동명사 narrowing이 왔습니다. 글 전체가 '장점 → 단점 → 해결'로 움직인다는 신호입니다.</div>
<div class="tip"><b>어휘 공략법</b> ① 밑줄 낱말이 <b>앞 절과 같은 방향</b>인지 보세요(Consequently, potentially -ing는 결과·부연). ② 글의 흐름(장점→단점→해결)을 먼저 잡으면, 단점 구간에 놓인 긍정어(facilitating)가 바로 눈에 띕니다. ③ 정답 후보를 반의어로 바꿔 넣어 문맥이 더 자연스러운지 확인하세요.</div>'''

S['42'] = '<h2>42번 · 장문 어휘 [3점] (41번 제목 포함)</h2>\n' + img('41-42', '41~42번') + '''<h3>① 지문 구조</h3>
<p><b>배경</b> 19세기 사회 과학과 대규모 데이터 → 정보를 시각화하는 새로운 방식(표·도표·그래프)에 대한 수요 → <b>전개</b> 역사학은 설계자가 아닌 절제된 소비자였고, 통계 분석이 정교해질수록 시각화가 논증의 중심이 됨 → <b>사례</b> John Snow의 콜레라 지도: 시각화가 서사와 분석을 동시에 수행 → <b>결과</b> 작가들이 시각적 단서로 복잡한 이야기를 전달하며 작은 공간에 더 많은 정보를 담게 됨.</p>
<p>41번 제목은 데이터가 시각화를 통해 해석(통찰)으로 이어진다는 흐름을 담은 <b>③ From Data to Insight: The Power of Visualization</b>입니다.</p>
<h3>② 정답 근거: (e) intensifying → overcoming</h3>
<div class="key"><span class="en">…<b>increasing the amount of information</b> that could be conveyed in a small space and <b>thereby</b> (e) <b>intensifying</b> the limitations of two dimensions in print.</span><br>thereby(그 결과)는 앞 내용의 결과를 말합니다. 작은 공간에 담을 수 있는 정보량이 <b>늘어났다면</b>, 인쇄물의 이차원이라는 한계는 '심화된(intensifying)' 것이 아니라 <b>극복된(overcoming)</b> 것입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>(a) forefront <span class="x">— 통계를 쓰는 학문들이 도표·그래프 발전의 '선두'에 있었다. 뒤 문장의 '역사학은 소비자였다'와 대조됩니다. (적절)</span></li>
<li>(b) ordinary <span class="x">— 단순한 도표는 해석하기 어렵지 않아 '평범한' 독자도 따라올 수 있었다. (적절)</span></li>
<li>(c) sophisticated <span class="x">— 통계 분석이 '정교해지면서' 시각화가 논증의 중심이 되었다. (적절)</span></li>
<li>(d) demonstrated <span class="x">— 성공 사례들이 통계 분석과 시각화의 가치를 '입증했다'. 바로 뒤 John Snow 사례가 증거입니다. (적절)</span></li>
<li class="ans">(e) intensifying <span class="o">— 정답(부적절).</span> 정보량 증가의 결과는 한계 '극복'입니다.</li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">History was a consumer, not a designer, of most of these new visualizations — and mostly a sparing consumer <b>at that</b>…</span><br>at that은 '그것도'라는 뜻으로 앞말에 정보를 덧붙입니다. "역사학은 소비자였고, 그것도 대체로 절제된 소비자였다."</div>
<div class="tip"><b>장문 어휘 공략법</b> ① thereby, thus, consequently 뒤의 밑줄은 <b>원인과 결과의 방향</b>을 맞춰 보세요. ② 마지막 문장의 밑줄은 글 전체 논지(시각화의 힘)와 같은 방향이어야 합니다. ③ 41번 제목을 먼저 풀면 42번의 방향 판단이 쉬워집니다.</div>'''

S['31'] = '<h2>31번 · 빈칸 추론(단어) [2점]</h2>\n' + img(31) + '''<h3>① 빈칸 문장의 역할</h3>
<div class="key"><span class="en"><b>However</b>, ________ can sometimes disrupt this understanding, or at least its expression.</span><br>However로 시작하므로 앞 내용(세 살이면 상상한 것이 현실이 되지 않는다는 것을 안다)을 <b>방해하는 요인</b>이 빈칸입니다. 바로 뒤 That is(즉)가 빈칸을 풀어 줍니다.</div>
<h3>② 정답 근거</h3>
<p>That is 이후 문장: 괴물이 진짜가 아님을 알면서도 침대 밑 괴물 생각만으로 방에 들어가길 거부한다. Indeed 문장: <span class="en">scary things</span>를 상상하라고 할 때 이해를 드러내기 더 어렵다. 실험: 빈 상자인 걸 알면서도 <span class="en">fear and avoidance</span>를 보였다. 세 문장의 공통점은 <b>무서움(감정)</b>입니다. 따라서 정답은 <b>① emotion</b>.</p>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li class="ans">① emotion(감정) <span class="o">— 정답.</span> monster, scary, fear가 모두 감정 반응입니다.</li>
<li>② curiosity(호기심) <span class="x">— 상자를 '피했다(avoidance)'고 했으니 호기심과 반대입니다.</span></li>
<li>③ familiarity(친숙함) <span class="x">— 연필 같은 '일상적인' 사물은 오히려 이해가 분명하다고 했습니다.</span></li>
<li>④ memory(기억) <span class="x">— 기억에 관한 내용은 없습니다.</span></li>
<li>⑤ ignorance(무지) <span class="x">— 아이들은 상자가 비었다는 것을 '알고' 있었습니다(All children agreed). 모르는 게 아닙니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">…the thought of a monster under a bed <b>might be enough to make</b> a child <b>refuse</b> to go into his room at night.</span><br>be enough to do(~하기에 충분하다) + 사역동사 make + 목적어 + 동사원형(refuse). → "침대 밑 괴물 생각만으로도 아이가 밤에 방에 들어가기를 거부하게 만들기에 충분할 수 있다."</div>
<div class="tip"><b>빈칸(단어) 공략법</b> However 빈칸은 '앞 내용을 뒤집는 것'이고, That is·Indeed·In one study는 그 빈칸의 <b>재진술과 증거</b>입니다. 뒤에 나오는 사례들의 공통 단어(scary, fear)를 한 단어로 묶으면 정답입니다.</div>'''

S['32'] = '<h2>32번 · 빈칸 추론(구) [2점]</h2>\n' + img(32) + '''<h3>① 빈칸 문장의 역할</h3>
<div class="key"><span class="en">In that book Dewey ________ by <b>basing aesthetic experience on the biological and cultural conditions of human life</b>.</span><br>by 이하가 빈칸의 '방법'입니다. 미적 경험을 <b>인간 삶의 조건</b>에 두었다 → 예술과 삶을 연결했다.</div>
<h3>② 정답 근거</h3>
<p>글 전체 주제는 <b>일상의 미학(aesthetics of everyday life)</b>, 즉 평범한 사물과 사건에서도 미적 만족을 얻을 수 있다는 것입니다. Dewey는 미적인 것을 '자아와 대상·사건 세계의 완전한 상호 침투'에, 그리고 '모든 정상적인 경험에 속하는 특성의 발전'에 두었습니다. 예술을 특별한 영역에 가두지 않고 삶 속으로 가져온 것이므로 정답은 <b>⑤ argued against the separation of art from life</b>(예술을 삶과 분리하는 것에 반대했다).</p>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 미적 감상을 문학적 관습과 동일시했다 <span class="x">— 시인·소설가 언급은 '일상 미학을 인정한 사람들'의 예일 뿐입니다.</span></li>
<li>② 사물의 실용적 가치보다 예술적 가치를 선호했다 <span class="x">— 둘을 대립시키는 내용은 없습니다. Dewey는 오히려 둘을 연결합니다.</span></li>
<li>③ 미적 경험을 감각적 즐거움에 한정했다 <span class="x">— <b>반대</b>입니다. 'not in an internalized awareness of sensation and feeling'이라고 분명히 부정했습니다.</span></li>
<li>④ 예술 기법의 개혁을 옹호했다 <span class="x">— 기법 이야기는 없습니다.</span></li>
<li class="ans">⑤ 예술을 삶과 분리하는 것에 반대했다 <span class="o">— 정답.</span> human life, every normally complete experience와 정확히 대응합니다.</li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">He located the aesthetic, <b>not</b> in an internalized awareness of sensation and feeling <b>but</b> in “a complete interpenetration of self and the world…”</span><br>not A but B 구조. 정답은 늘 B 쪽입니다. A(감각·감정의 내적 인식)를 그대로 쓴 ③은 함정입니다.</div>
<div class="tip"><b>빈칸(구) 공략법</b> ① 빈칸 뒤 by -ing가 있으면 그것이 정답의 '방법'입니다. ② not A but B가 나오면 A를 쓴 선택지를 먼저 지우세요. ③ 글의 첫 문장(주제)과 빈칸 정답이 같은 방향인지 마지막으로 확인합니다.</div>'''

S['33'] = '<h2>33번 · 빈칸 추론(구) [3점]</h2>\n' + img(33) + '''<h3>① 빈칸 문장의 역할</h3>
<div class="key"><span class="en">Both entities, <b>therefore</b>, must ________.</span><br>therefore로 시작하는 결론 문장입니다. 바로 앞 문장(도덕적 우월성 판단의 조건)을 요약하면 정답입니다.</div>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">One entity is correctly judged morally superior to another if it is the case that, <b>when valid moral standards are applied to both entities</b>, the first fulfills them to a greater degree than the second.</span><br>도덕적 우월성을 판단하려면 <b>두 존재 모두에게 도덕적 기준을 적용</b>할 수 있어야 합니다. 그래서 두 존재는 모두 <b>⑤ 도덕적 기준의 적용 범위 안에 들어가야 한다(fall within the range of application of moral standards)</b>.</div>
<p>마지막 문장도 확인해 줍니다. 동식물은 도덕 행위자가 아니므로 이 조건을 충족하지 못하고, 그래서 '인간이 동식물보다 도덕적으로 우월하다'는 판단은 성립하지 않습니다.</p>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 도덕적 탁월함의 가장 높은 수준에 서야 한다 <span class="x">— 비교는 '더 많이 충족하는가'의 문제이지, 둘 다 최고일 필요는 없습니다.</span></li>
<li>② 서로의 도덕적 결함에 공감해야 한다 <span class="x">— 공감은 논증과 무관합니다.</span></li>
<li>③ 일련의 도덕적 가치에 합의해야 한다 <span class="x">— 기준은 '타당한 기준(valid moral standards)'이 적용되는 것이지, 두 존재가 합의하는 것이 아닙니다.</span></li>
<li>④ 도덕적 우월성 판단에서 제외되어야 한다 <span class="x">— 정반대입니다. 판단의 대상이 되어야 비교가 가능합니다.</span></li>
<li class="ans">⑤ 도덕적 기준의 적용 범위 안에 들어가야 한다 <span class="o">— 정답.</span> applied to both entities의 재진술입니다.</li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">One cannot validly argue that humans are morally superior beings on the ground that they possess, <b>while others lack</b>, the capacities of a moral agent.</span><br>possess와 lack이 목적어 the capacities of a moral agent를 함께 받습니다. 삽입된 while others lack을 괄호로 묶어 읽으세요. on the ground that = ~라는 이유로.</div>
<div class="tip"><b>추상 논증 빈칸 공략법</b> 이 지문처럼 철학 논증이 나오면 문장마다 '<b>조건 → 결론</b>'을 화살표로 적어 보세요. therefore 빈칸은 바로 앞의 조건(applied to both entities)을 다른 말로 바꾼 선택지가 정답입니다. 추상어가 많은 선택지는 각각 우리말로 번역한 뒤 본문 문장과 대응시키세요.</div>'''

S['34'] = '<h2>34번 · 빈칸 추론(구) [3점]</h2>\n' + img(34) + '''<h3>① 빈칸 문장의 역할</h3>
<div class="key"><span class="en">In this context at least, the AI may be starting to ________. <b>Yet</b> the AI’s confusion when presented with substantial silences … indicate the AI’s continuing preferences for sound over silence, for presence over absence.</span><br>빈칸 바로 뒤가 Yet(그러나)입니다. Yet 뒤가 'AI는 여전히 침묵보다 소리, 부재보다 존재를 선호한다'이므로, 빈칸은 그 반대 = <b>AI가 침묵을 의미 있는 것으로 인식하기 시작했다</b>입니다.</div>
<h3>② 정답 근거</h3>
<p>앞부분: AI는 짧은 침묵을 '생각하는 멈춤'처럼 활용해 인간처럼 보이게 하고, 대화 상황에 따라 침묵을 관련 있는 소리로 채울 수 있다고 추론합니다. 즉 침묵을 <b>그냥 비어 있는 것이 아니라 정보로</b> 다루기 시작한 것이죠. 따라서 정답은 <b>④ recognise silence not as an absence but as meaningful data</b>입니다. Yet 뒤의 for presence over absence와 정확히 대조됩니다.</p>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 맥락 정보를 무관한 데이터로 오인하다 <span class="x">— 본문은 AI가 침묵을 '관련 있는(relevant)' 소리로 채운다고 했습니다.</span></li>
<li>② 침묵을 대화의 종료로 분석하다 <span class="x">— 짧은 침묵을 '생각하는 멈춤'으로 해석한다고 했습니다. 종료가 아닙니다.</span></li>
<li>③ 더 빠른 말 속도와 함께 인간다움을 얻다 <span class="x">— 인간다움은 맞지만 '빠른 말 속도'는 본문에 없습니다. 오히려 멈춤을 넣는 이야기입니다.</span></li>
<li class="ans">④ 침묵을 부재가 아니라 의미 있는 데이터로 인식하다 <span class="o">— 정답.</span> Yet 뒤의 presence over absence와 대조를 이룹니다.</li>
<li>⑤ 멈춤 채우기가 대화 흐름을 현저히 방해한다고 여기다 <span class="x">— 반대입니다. pause filler는 더 자연스러운 억양을 만든다고 했습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">…the technical issues flagged in AI’s poor handling of higher duration and frequency silences, <b>no less than</b> the machine inference that silence can be filled…, <b>are both</b> significant.</span><br>no less than은 여기서 '~와 마찬가지로'라는 뜻입니다. 주어는 the technical issues와 the machine inference 두 개이고, 그래서 동사가 are both입니다.</div>
<div class="tip"><b>빈칸 뒤 Yet 공략법</b> 빈칸 바로 뒤에 Yet·But·However가 오면 <b>뒷문장을 뒤집은 것</b>이 빈칸입니다. 뒷문장의 핵심 대립어(presence ↔ absence, sound ↔ silence)를 찾아, 그 반대편을 긍정하는 선택지를 고르세요.</div>'''

S['36'] = '<h2>36번 · 글의 순서 [2점]</h2>\n' + img(36) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">기원전 9500년 무렵부터 작물을 재배했다</td><td class="l">→ 그 이후 '수천 년 동안'의 이야기가 이어져야 함</td></tr>
<tr><td>(C)</td><td class="l"><b>Over the millennia</b>, 혁신이 생산성을 높였다. However, 인구 증가로 더 많은 식량이 필요하다</td><td class="l">9500 BC → 수천 년 동안 → 주어진 글 바로 뒤</td></tr>
<tr><td>(B)</td><td class="l">2050년 인구 97억, 식량 생산 70% 증가 필요. <b>Despite this need</b>, 농사에 적합한 땅은 적다</td><td class="l">(C)의 '더 많은 식량 수요'를 수치로 구체화 → (C) 뒤</td></tr>
<tr><td>(A)</td><td class="l">정치·경제적 요인<b>also</b> 농지 사용에 영향을 준다. 실제로 농지가 줄고 있다</td><td class="l">also = (B)의 자연적 제약(기후·지형·토양·기술)에 더해 → (B) 뒤</td></tr>
</table>
<h3>② 정답: ⑤ (C)-(B)-(A)</h3>
<div class="key">농업의 시작 → (C) 수천 년간의 혁신, 그러나 늘어나는 인구 → (B) 2050년 식량 수요 70% 증가, 그런데 경작 가능한 땅은 적음(자연적 제약) → (A) 정치·경제적 요인<b>도</b> 영향, 실제로 농지 감소. <b>시간 흐름</b>(과거 → 현재 → 미래 수요)과 <b>also의 짝</b>이 모두 맞습니다.</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— also가 받을 '다른 요인'이 주어진 글에 없습니다.</span></li>
<li>(B)로 시작(②, ③) <span class="x">— this need가 가리킬 '수요'가 주어진 글에 없습니다. 9500 BC에서 곧바로 2050년으로 건너뛰는 것도 어색합니다.</span></li>
<li>(C)-(A)-(B)(④) <span class="x">— (A)의 also가 (C) 뒤에 오면 '무엇에 더해서'인지 알 수 없습니다. 제약 요인은 (B)에서 처음 나옵니다.</span></li>
</ul>
<div class="tip"><b>순서 공략법</b> ① 연도·시간 표현(9500 BC, millennia, 2050)이 있으면 시간 순서로 먼저 배열해 보세요. ② also·this need·these 같은 <b>짝을 요구하는 말</b>에 동그라미를 치고, 그 짝이 어느 단락에 있는지 화살표로 연결하세요.</div>'''

S['37'] = '<h2>37번 · 글의 순서 [3점]</h2>\n' + img(37) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">모든 언어에 있는 것부터 비교하라. 예: mother, father</td><td class="l">→ mother, father를 출발점으로 범주를 넓혀야 함</td></tr>
<tr><td>(B)</td><td class="l"><b>If we add other family relationships to this category</b> — son, grandmother… = 친족 용어</td><td class="l">this category = 주어진 글의 mother, father → 바로 뒤</td></tr>
<tr><td>(A)</td><td class="l"><b>And</b> 특정 친족 관계에 이름이 있을 확률은 예측 가능하다. 모든 언어에는 핵심 친족 용어(core set)가 있다</td><td class="l">And = (B)의 '일부 관계에만 이름이 있다'에 덧붙임 → (B) 뒤</td></tr>
<tr><td>(C)</td><td class="l"><b>By contrast</b>, 덜 중심적인 용어는 핵심 용어로 만들어진다(mother-in-law)</td><td class="l">By contrast = (A)의 core terms와 대조 → (A) 뒤</td></tr>
</table>
<h3>② 정답: ② (B)-(A)-(C)</h3>
<div class="key">mother·father에서 출발 → (B) 가족 관계를 더해 '친족 용어' 범주를 정의, 일부 관계에만 이름이 있다 → (A) And 그 확률은 예측 가능, 모든 언어에 <b>핵심 용어</b>가 있다 → (C) By contrast, <b>주변 용어</b>는 핵심 용어로 만든다.</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— And가 이어 줄 앞 내용(이름이 있는 관계/없는 관계)이 주어진 글에 없습니다. a specific kin relationship이라는 용어도 아직 등장하지 않았습니다.</span></li>
<li>(B)-(C)-(A)(③) <span class="x">— (C)의 By contrast가 대조할 core terms가 (A)에서야 처음 나옵니다.</span></li>
<li>(C)로 시작(④, ⑤) <span class="x">— less central category members는 '핵심(core)'이 먼저 나와야 성립합니다.</span></li>
</ul>
<div class="tip"><b>함정 주의</b> (A)에도 mother and father가 다시 나와서 주어진 글 바로 뒤에 붙이고 싶어집니다. 하지만 (A)는 <b>And</b>로 시작하고 kin relationship, kinship terms라는 '이미 정의된 용어'를 씁니다. 용어를 <b>정의하는 단락(B)</b>이 그 용어를 <b>사용하는 단락(A)</b>보다 먼저 옵니다.</div>'''

S['38'] = '<h2>38번 · 문장 삽입 [2점]</h2>\n' + img(38) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<div class="key"><span class="en"><b>These in-character behaviors</b> can be <b>insufficient, however</b>, to maintain the necessary amount of common ground…</span><br>"그러나 이러한 '배역 안에서의' 행동은 … 공통 기반을 유지하기에 <b>불충분할</b> 수 있다."<br>→ 단서 1: <b>These in-character behaviors</b> — 앞에 배역 안에서의 행동(예: 헐떡이며 칼을 뽑음)이 나와야 합니다.<br>→ 단서 2: <b>insufficient, however</b> — 앞은 '충분하다(sufficient)'는 내용이어야 합니다.</div>
<h3>② 위치별 점검</h3>
<table>
<tr><th>위치</th><th>앞 문장</th><th>뒤 문장</th><th>판단</th></tr>
<tr><td>①</td><td class="l">가상 놀이 참여자들이 소통하는 여러 방법</td><td class="l">Sometimes 배역 안에서 자연스럽게 전달된다</td><td>✕ 아직 in-character 행동이 없음</td></tr>
<tr><td>②</td><td class="l">배역 안에서 말하거나 행동해 전달</td><td class="l">For example, 피터 팬 놀이</td><td>✕ 주장 → 예시로 이어짐</td></tr>
<tr><td>③</td><td class="l">헐떡이며 칼을 뽑음</td><td class="l">이것으로 후크 선장이 다가옴을 전달하기에 충분</td><td>✕ This가 바로 앞 행동을 받음</td></tr>
<tr><td class="o">④</td><td class="l">…전달하기에 <b>충분할(sufficient)</b> 수 있다</td><td class="l"><b>At these times</b> 참여자들은 배역에서 일부 벗어나 정보를 준다</td><td class="o">○ sufficient ↔ insufficient, these times가 받을 말 필요</td></tr>
<tr><td>⑤</td><td class="l">배역에서 벗어나 정보를 줌</td><td class="l">For example, "아니, 네가 후크 선장이야!"</td><td>✕ 배역 밖 발화의 예시</td></tr>
</table>
<h3>③ 정답 근거</h3>
<p>④ 뒤의 <span class="en">At these times</span>(이런 때에는)는 무엇을 가리킬까요? 앞 문장은 '충분하다'는 내용이라 '이런 때'가 가리킬 상황이 없습니다. 주어진 문장을 넣으면 these times = <b>배역 안 행동만으로는 불충분할 때</b>가 되어 흐름이 완성됩니다. 정답 <b>④</b>.</p>
<div class="tip"><b>문장 삽입 공략법</b> ① 주어진 문장의 지시어(These)와 연결어(however)에 표시하세요. ② 본문에서 <b>논리가 끊기는 곳</b>을 찾으세요. 여기서는 sufficient(③ 뒤)에서 '배역에서 벗어난다'(④ 뒤)로 갑자기 바뀌는 지점입니다. ③ 넣은 뒤 다음 문장의 these times가 자연스럽게 받는지 확인하세요.</div>'''

S['39'] = '<h2>39번 · 문장 삽입 [3점]</h2>\n' + img(39) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<div class="key"><span class="en"><b>But</b> the pressure changes <b>we experience</b> are <b>trivial</b> compared to the pressure range of the overall planetary environment.</span><br>"그러나 우리가 경험하는 압력 변화는 행성 환경 전체의 압력 범위에 비하면 사소하다."<br>→ 단서 1: <b>But</b> — 앞은 '우리가 경험하는 압력 변화가 크다(큰 영향)'는 내용이어야 합니다.<br>→ 단서 2: 뒤에는 '행성 전체의 엄청난 압력 범위' 이야기가 이어져야 합니다.</div>
<h3>② 위치별 점검</h3>
<table>
<tr><th>위치</th><th>앞 문장</th><th>뒤 문장</th><th>판단</th></tr>
<tr><td>①</td><td class="l">녹는 것·끓는 것 = 온도 상승이라 직관적으로 가정</td><td class="l">This bias는 압력이 일정한 환경에서 온다</td><td>✕ This bias가 앞의 가정을 받음</td></tr>
<tr><td>②</td><td class="l">압력이 일정한 환경</td><td class="l">Even 작은 압력 변화도 신진대사에 큰 영향</td><td>✕ Even으로 이어지는 부연</td></tr>
<tr><td class="o">③</td><td class="l">작은 압력 변화도 <b>큰 영향</b>(물속, 산꼭대기)</td><td class="l">압력은 위에 놓인 물질의 무게로 결정되어 깊이에 따라 급증</td><td class="o">○ 우리 경험 → 행성 전체로 범위 전환</td></tr>
<tr><td>④</td><td class="l">압력은 깊이에 따라 급증</td><td class="l">1마일 두께 암석의 무게를 상상해 보라</td><td>✕ 설명 → 상상 예시로 이어짐</td></tr>
<tr><td>⑤</td><td class="l">암석의 무게</td><td class="l">For this reason 행성의 압력 범위는 엄청나다</td><td>✕ 원인 → 결과로 이어짐</td></tr>
</table>
<h3>③ 정답 근거</h3>
<p>② 뒤 문장까지는 '<b>우리</b>가 지구 표면에서 겪는 압력'(물속, 산꼭대기) 이야기이고, ③ 뒤 문장부터는 '<b>행성 내부</b>의 압력'(깊이, 암석의 무게) 이야기입니다. 이 <b>장면 전환</b>을 이어 주는 문장이 주어진 문장이므로 정답은 <b>③</b>입니다. very large effects(우리에겐 크다) ↔ trivial(행성 전체로 보면 사소하다)의 대조도 정확히 맞습니다.</p>
<div class="tip"><b>함정 주의</b> ⑤ 뒤에 planet's pressure ranges가 나와서 ⑤를 고르기 쉽습니다. 하지만 ⑤ 뒤 문장은 For this reason으로 시작해 앞의 '암석 무게'를 이유로 받습니다. 그 사이에 주어진 문장이 끼면 인과 관계가 끊깁니다. 삽입 문제는 <b>소재가 바뀌는 첫 지점</b>을 찾으세요.</div>'''

S['40'] = '<h2>40번 · 요약문 완성 [2점]</h2>\n' + img(40) + '''<h3>① 요약문 구조</h3>
<div class="key"><span class="en">Since self-experiments are suited to <b>(A)</b> while conventional experiments provide <b>validation</b>, the most efficient strategy is for the former to <b>(B)</b> the latter.</span><br>(A) = 자기 실험의 강점, validation(검증)과 대조 / (B) = 자기 실험과 전통적 실험의 <b>순서</b></div>
<h3>② 정답 근거</h3>
<ul class="ch">
<li><b>(A)</b> <span class="en">Self-experiments are better for <b>discovery</b> … This <b>exploratory</b> and theory-building phase…</span> → discovery, exploratory = <b>exploration(탐구)</b></li>
<li><b>(B)</b> <span class="en">self-experiments <b>followed by</b> conventional ones … <b>Only then</b> would the researcher begin conventional experiments</span> → 자기 실험이 전통적 실험보다 <b>앞선다(precede)</b></li>
</ul>
<p>정답 <b>① exploration ······ precede</b>.</p>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li class="ans">① exploration / precede <span class="o">— 정답.</span></li>
<li>② formalization(형식화) / precede <span class="x">— 자기 실험은 형식을 갖추는 단계가 아니라 탐색 단계입니다.</span></li>
<li>③ confirmation(확인) / follow <span class="x">— 확인(검증)은 전통적 실험의 몫이고, 순서도 반대입니다.</span></li>
<li>④ investigation(조사) / follow <span class="x">— (A)는 그럴듯하지만 (B)의 순서가 반대입니다. followed by를 거꾸로 읽으면 이 함정에 걸립니다.</span></li>
<li>⑤ standardization(표준화) / accompany(동반하다) <span class="x">— 동시에 진행하는 것이 아니라 순서가 있습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en"><b>Only then would the researcher begin</b> conventional experiments…</span><br>Only then이 문두에 오면서 조동사 would와 주어 the researcher가 <b>도치</b>되었습니다. "그때가 되어서야 비로소 연구자는 전통적 실험을 시작할 것이다."</div>
<div class="tip"><b>요약문 공략법</b> ① 요약문의 대조어(while … validation)부터 보세요. (A)는 validation의 반대편입니다. ② 'A followed by B'는 <b>A가 먼저</b>입니다. 순서를 묻는 (B)는 followed by, Only then, begins with 같은 순서 표지로 확인하세요.</div>'''

json.dump(S, open('secs_g2.json', 'w'), ensure_ascii=False)
print(len(S))
