import json, sys
REF = sys.argv[1] if len(sys.argv) > 1 else 'REF'
B = f'https://cdn.jsdelivr.net/gh/KKHLAND/edu-hub@{REF}/blog-assets/v2_05g3/'
def img(n, lab=None):
    lab = lab or f'{n}번'
    return (f'<img src="{B}q{n}.png" alt="2026년 5월 고3 영어 {lab} 발문 지문 선택지 해석 어휘">\n'
            '<p class="cap">발문·지문·선택지·해석·어휘</p>\n')
S = {}
S['21'] = '<h2>21번 · 함축 의미 추론 [2점]</h2>\n' + img(21) + '''<h3>① 지문 구조</h3>
<p><b>가설</b> 가리비의 시각은 우리와 아주 다르게 작동할 것이다(Speiser) → <b>비교</b> 우리 뇌는 두 눈의 정보를 하나의 장면으로 합치지만, 원시적인 가리비 뇌는 100개의 눈으로 그렇게 하기 어렵다 → <b>비유</b> 보안 요원이 100개의 모니터를 보지만 화면은 전송되지 않고 '무언가 감지됨' 경고등만 본다 → <b>결론</b> 눈마다 해상도는 좋아도 공간 시각은 없을 수 있다 → 밑줄: 장면 없이 본다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">It knows when eyes in a certain region of its body have detected something, <b>but it has no visual image of that object</b>. It doesn’t experience a movie in its head the same way we do.</span><br>→ 밑줄 바로 앞 두 문장이 답입니다. '본다(sees)' = 눈으로 감지한다, '장면 없이(without scenes)' = 시각적 이미지가 없다. 그래서 <b>③ 시각적 이미지는 없이 눈으로 대상을 감지한다</b>가 정답입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 발달한 뇌로 시각 이미지를 단순화한다 <span class="x">— 가리비의 뇌는 primitive(원시적)라고 했습니다. 이미지 자체가 없습니다.</span></li>
<li>② 다른 감각에 따라 시각 자극을 해석한다 <span class="x">— 다른 감각은 언급되지 않았습니다.</span></li>
<li class="ans">③ 시각적 이미지가 없는 상태로 눈으로 대상을 감지한다 <span class="o">— 정답.</span> detected something ↔ senses an object, no visual image ↔ lacking a visual image</li>
<li>④ 움직임이 나타나기 전에 위험을 예측한다 <span class="x">— 움직임을 '감지'할 뿐 예측한다는 내용은 없습니다.</span></li>
<li>⑤ 움직임을 포착하지 않고 시각 이미지를 지각한다 <span class="x">— 정반대입니다. 움직임은 감지하고, 이미지는 없습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">Think of the scallop’s brain as a security guard watching a bank of a hundred monitors, <b>each connected to</b> a motion-sensing camera.</span><br>think of A as B(A를 B라고 생각하다) + each connected to …는 독립분사구문(each (being) connected)으로 '각각 ~에 연결된'이라는 뜻입니다.</div>
<div class="tip"><b>함축 의미 공략법</b> 밑줄 바로 앞의 <b>비유를 일반 문장으로 바꾼 부분</b>(여기서는 It knows … but it has no visual image)을 찾으세요. 정답 선택지는 그 문장을 다른 단어로 바꿔 쓴 것입니다. ⑤처럼 두 요소의 방향을 뒤집은 선택지가 가장 흔한 함정입니다.</div>'''

S['29'] = '<h2>29번 · 어법 [3점]</h2>\n' + img(29) + '''<h3>① 지문 구조</h3>
<p><b>현상</b> 원격 근무하는 젊은 직원들은 업무량 관리에 더 어려움을 겪는다 → <b>원인</b> 팬데믹 중 원격으로 경력을 시작해 대인 관계와 조직 문화에 스며들 기회가 없었다, 집에 적절한 작업 공간이 없다 → <b>제안</b> 하이브리드 모델이 맞을 수 있다 → 정해진 요일이 아니라 근무 장소를 스스로 고르는 유연한 선택지.</p>
<h3>② 정답: ⑤ chooses → to choose</h3>
<div class="key"><span class="en">… a fluid option that allows them, if possible, depending on the job role, ⑤ <b>chooses</b> their day-to-day work location.</span><br>allow는 <b>allow + 목적어 + to부정사</b> 구조를 취합니다. 목적어 them 뒤에 삽입구(if possible, depending on the job role)가 끼어 있어 헷갈리지만, 삽입구를 지우면 allows them chooses가 되어 틀린 것이 보입니다. → <b>to choose</b></div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① reported <span class="x">— 관계사절 who were working remotely 뒤 문장의 본동사입니다. 주어 young people에 맞는 과거 동사로 적절합니다.</span></li>
<li>② themselves <span class="x">— embed의 목적어가 주어 those(older generations)와 같으므로 재귀대명사가 맞습니다.</span></li>
<li>③ it <span class="x">— find it difficult to work …에서 진목적어 to work를 대신하는 가목적어 it입니다.</span></li>
<li>④ where <span class="x">— a hybrid model을 선행사로 하고 뒤에 완전한 문장(they can work from home …)이 오므로 관계부사 where가 맞습니다.</span></li>
<li class="ans">⑤ chooses <span class="o">— 정답(틀림).</span> allow + 목적어 + to choose</li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">But it may not be that they need a formal hybrid structure … <b>but instead</b> a fluid option …</span><br>it is not that A but (instead) B: 'A라는 것이 아니라 B라는 것이다'. 필자가 말하고 싶은 것은 but 뒤(유연한 선택지)입니다.</div>
<div class="tip"><b>어법 공략법</b> 밑줄 앞에 <b>allow, enable, encourage, force</b> 같은 5형식 동사가 있으면 목적어 뒤에 to부정사가 오는지 확인하세요. 목적어와 밑줄 사이의 쉼표 삽입구는 괄호로 묶어 지우고 읽으면 구조가 바로 보입니다.</div>'''

S['30'] = '<h2>30번 · 문맥상 낱말의 쓰임 [2점]</h2>\n' + img(30) + '''<h3>① 지문 구조</h3>
<p><b>비교 1</b> 아기의 면역계가 덜 활발해 다양한 박테리아가 장에 자리 잡듯, 어린 식물도 방어 물질을 덜 내보내 다양한 미생물이 뿌리 주변에 자리 잡게 한다 → <b>비교 2</b> 모유의 당은 아기가 소화하지 못하지만 장 박테리아를 먹이기 위한 것이고, 어린 식물도 당을 흙에 내보내 미생물을 키운다 → <b>비교 3</b> 장 박테리아가 병원체를 물리치듯, 뿌리 주변 미생물도 방어막을 만든다.</p>
<h3>② 정답: ⑤ accumulate → repel(물리치다)</h3>
<div class="key"><span class="en">Plants feed beneficial bacteria species, so that they ⑤ <b>accumulate</b> pathogenic microbes.</span><br>바로 앞 문장은 미생물이 뿌리 주변에 <b>방어막(defensive ring)</b>을 만든다는 것입니다. 이로운 박테리아를 먹이는 목적은 병원성 미생물을 '쌓는(accumulate)' 것이 아니라 <b>몰아내는(repel / outcompete)</b> 것이어야 합니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① fewer <span class="x">— 아기의 면역계가 '덜' 활발하다는 앞 문장과 Similarly로 이어지므로 '더 적은' 방어 물질이 맞습니다.</span></li>
<li>② struggled <span class="x">— 아기가 소화하지 못하는 당을 왜 만드는지 과학자들이 처음에 '이해하기 어려웠다'는 흐름입니다.</span></li>
<li>③ cultivate <span class="x">— 모유의 당이 특정 박테리아 종을 선택적으로 '기른다'는 뜻으로 적절합니다.</span></li>
<li>④ defensive <span class="x">— 장 박테리아가 병원체를 공격하듯 미생물이 '방어' 고리를 만든다는 뜻입니다.</span></li>
<li class="ans">⑤ accumulate <span class="o">— 정답(부적절).</span> 방어의 목적과 정반대</li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en"><b>Just as</b> the bacteria that live in our guts outcompete and attack invading pathogens, the microbes in the rhizosphere create a defensive ring around the root.</span><br>Just as A, B: 'A와 마찬가지로 B'. 이 글은 처음부터 끝까지 '사람의 장 ↔ 식물의 뿌리'를 짝지어 비교하므로, 짝이 되는 문장의 방향이 같아야 합니다.</div>
<div class="tip"><b>어휘 공략법</b> Similarly, Just as처럼 <b>비교 구조</b>가 반복되는 글은 짝이 되는 문장끼리 방향이 같은지 확인하세요. 마지막 so that(목적) 문장은 앞 내용의 '목적'과 맞는지 보면 바로 걸러집니다.</div>'''

S['42'] = '<h2>42번 · 장문 어휘 [3점] (41번 제목 포함)</h2>\n' + img('41-42', '41~42번') + '''<h3>① 지문 구조</h3>
<p><b>상황</b> 5만 년 전 세렝게티, 영양을 잡는 데 2,000칼로리를 썼다 → <b>문제</b> 쓴 만큼만 먹으면 다음 사냥이 보장되지 않아 오래 못 산다 → <b>해결</b> 보상을 담당하는 쾌락 뇌가 작동해 더 먹게 한다, 배가 불러도 당과 지방이 많은(고열량) 음식을 원한다 = 디저트 → <b>결론</b> 디저트 배는 진화의 잔재로, 굶주림이 반복되던 시절엔 생존을 도왔지만 늘 풍족한 오늘날엔 해롭다.</p>
<h3>② 정답: ⑤ (e) restrict → maximize</h3>
<div class="key"><span class="en">… you were still desiring the right types of foods to ensure you were able to (e) <b>restrict</b> your caloric intake at every meal, because there was never a guarantee of when the next meal would arrive.</span><br>다음 식사가 언제 올지 모르니 매 끼니 칼로리 섭취를 '제한'하는 것이 아니라 <b>최대한 늘려야(maximize)</b> 합니다. because 뒤의 이유와 restrict가 정면으로 어긋납니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① (a) expenditure <span class="x">— 사냥에 쓴 2,000칼로리의 '소모'를 회복한다는 뜻으로 적절합니다.</span></li>
<li>② (b) survive <span class="x">— 쓴 만큼만 먹으면 오래 '살아남지' 못한다는 흐름입니다.</span></li>
<li>③ (c) more <span class="x">— 쾌락 뇌가 '더' 먹게 만든다는 핵심 내용입니다.</span></li>
<li>④ (d) dense <span class="x">— 배가 가득 찼으니 열량이 '밀집된' 음식을 원한다는 뜻입니다.</span></li>
<li class="ans">⑤ (e) restrict <span class="o">— 정답(부적절).</span></li>
</ul>
<p><b>41번 제목</b> 정답 ③ The Evolutionary Roots of the Human Dessert Stomach — 디저트 배가 세렝게티 시절의 생존 전략에서 왔다는 글 전체를 요약합니다. ④는 쾌락 추구가 생존에 '반했다'는 정반대 방향입니다.</p>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">so if you ONLY ate to your metabolic need, you <b>wouldn’t survive</b> very long.</span><br>가정법 과거(if + 과거, would + 동사원형)로 '만약 ~한다면 ~하지 못할 것이다'. 필자가 대문자로 강조한 ONLY가 글의 논리(필요한 만큼만 먹으면 안 된다)를 보여 줍니다.</div>
<div class="tip"><b>장문 어휘 공략법</b> 밑줄 낱말이 들어간 문장에 <b>because, so, to ensure</b> 같은 이유·목적 표현이 있으면 그 이유와 방향이 맞는지 확인하세요. 글의 결론(다음 식사가 보장되지 않는다)과 반대 방향인 낱말이 정답입니다.</div>'''

S['31'] = '<h2>31번 · 빈칸 추론(단어) [2점]</h2>\n' + img(31) + '''<h3>① 빈칸 문장의 역할</h3>
<p>빈칸 문장(The beauty of vibrational signaling lies in its ___.)은 앞에서 설명한 진동 신호의 <b>장점을 한 단어로 요약</b>하고, 바로 뒤 문장(It avoids costly physical clashes …)이 그 요약을 풀어 설명합니다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">It avoids <b>costly</b> physical clashes, allowing spiders to resolve territorial disputes with <b>minimal risk</b> of injury.</span><br>비용이 큰 몸싸움을 피하고 최소한의 위험으로 분쟁을 해결한다 → 적은 비용으로 같은 결과를 얻는 것 = <b>② efficiency(효율성)</b></div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① secrecy(은밀함) <span class="x">— 진동 신호는 상대에게 강하게 '알리는' 것이라 정반대입니다.</span></li>
<li class="ans">② efficiency(효율성) <span class="o">— 정답.</span> costly·minimal risk와 정확히 맞습니다.</li>
<li>③ dishonesty(부정직) <span class="x">— 신호의 강도가 거미의 크기·힘과 '연관된다(correlate)'고 했으므로 정직한 신호입니다.</span></li>
<li>④ randomness(무작위성) <span class="x">— 신호는 일정한 의미(도전, 싸울 준비)를 가집니다.</span></li>
<li>⑤ subjectivity(주관성) <span class="x">— 침입자가 위험을 '객관적으로' 평가하게 해 줍니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">… allowing the invader to assess the risk of engaging in a direct confrontation.</span><br>allow + 목적어 + to부정사(29번과 같은 구조). 결과를 나타내는 분사구문으로 '그래서 침입자가 ~을 평가할 수 있게 한다'.</div>
<div class="tip"><b>빈칸(단어) 공략법</b> '~의 아름다움/핵심/장점은 ___에 있다' 문장은 <b>바로 뒤 문장의 핵심어</b>(costly, minimal risk)를 한 단어로 묶은 것입니다. 빈칸 뒤 It이 무엇을 설명하는지 먼저 읽으세요.</div>'''

S['32'] = '<h2>32번 · 빈칸 추론(구) [3점]</h2>\n' + img(32) + '''<h3>① 빈칸 문장의 역할</h3>
<p>Therefore, according to Robbins, ___ — 글 전체의 <b>결론</b>입니다. 앞에서 반복된 Robbins의 주장(경제학은 어떤 목적이 좋은지 판단하지 않는다)을 한 문장으로 요약해야 합니다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">Whether the ends chosen by man are good or bad, noble or ignoble, economics should study them, because the task of economist is <b>not to praise or criticise but only to analyse and explain</b>.</span><br>목적이 좋든 나쁘든 판단하지 않고 분석만 한다 → <b>② 경제학은 목적들 사이에서 중립적이다</b></div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 경제 위기는 반복된다 <span class="x">— 경제 위기는 나오지 않습니다.</span></li>
<li class="ans">② 경제학은 목적들 사이에서 중립적이다 <span class="o">— 정답.</span> does not make a choice, not to praise or criticise와 대응</li>
<li>③ 경제학은 윤리학 안에서 연구되어야 한다 <span class="x">— 바람직함의 판단은 경제학의 범위 밖(beyond the scope)이라고 했으므로 반대입니다.</span></li>
<li>④ 모든 경제학자는 자신의 욕구를 대변한다 <span class="x">— 경제학자는 판단 없이 분석만 한다는 내용과 반대입니다.</span></li>
<li>⑤ 경제학은 사회 체계에서 벗어날 수 없다 <span class="x">— 사회 체계는 언급되지 않았습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">economics does not deal with the question <b>as to</b> what ends should be achieved, <b>that is</b>, what wants should be satisfied and what not</span><br>as to(~에 관한) + 의문사절, that is(즉) 뒤에 같은 내용을 다시 풀어 씀. 바꿔 말하기가 많은 글일수록 결론 빈칸은 쉽게 정리됩니다.</div>
<div class="tip"><b>빈칸(구) 공략법</b> Therefore로 시작하는 마지막 빈칸은 <b>글에서 세 번 이상 반복된 말</b>을 찾으세요. 여기서는 '선택하지 않는다 / 판단하지 않는다 / 범위 밖이다'가 반복되어 neutral로 모입니다.</div>'''

S['33'] = '<h2>33번 · 빈칸 추론(구) [3점]</h2>\n' + img(33) + '''<h3>① 빈칸 문장의 역할</h3>
<p>마지막 문장 '각자 방식대로 살게 하는 것은 가치 중립적이지 않다; 그것은 문화적 자율성을 ___보다 중시하는 선택이다'에서, 빈칸은 <b>문화적 자율성과 저울에 올려진 다른 가치</b>입니다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">Should the British simply have lived and let live, or <b>lived and let die</b> as the case may be?</span><br>백신을 도입하지 않고 그 문화를 그대로 두는 것 = 천연두로 죽게 내버려 두는 것(let die). 그러니 문화적 자율성과 맞서는 가치는 <b>② 그렇지 않았다면 구할 수 있었던 사람들의 생명</b>입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 사회 내 커진 지위 격차 <span class="x">— 지위 격차는 언급되지 않았습니다.</span></li>
<li class="ans">② 그렇지 않았다면 구해졌을 사람들의 생명 <span class="o">— 정답.</span> let die와 짝을 이룹니다.</li>
<li>③ 집단이 스스로 회복할 고유한 잠재력 <span class="x">— 스스로 회복한다는 내용은 없습니다.</span></li>
<li>④ 대대로 존중받아 온 지역 관습 <span class="x">— 그것은 문화적 자율성 '쪽'의 가치입니다. 저울의 같은 편을 고른 함정입니다.</span></li>
<li>⑤ 공동체가 지키려 한 종교적 권위 <span class="x">— Sitala 숭배(종교) 역시 문화적 자율성 쪽에 속합니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">What is beyond dispute is that <b>no matter how</b> you answer that question, you are making a value judgment.</span><br>What is beyond dispute(논란의 여지가 없는 것은) + no matter how(어떻게 ~하든). 어느 쪽을 택해도 가치 판단이라는 것이 글의 결론입니다.</div>
<div class="tip"><b>빈칸(구) 공략법</b> 'A over B(B보다 A를 중시)' 빈칸에서는 <b>A와 반대편 가치</b>를 찾아야 합니다. ④⑤처럼 A와 같은 편(전통·종교)을 고르는 실수가 가장 많습니다.</div>'''

S['34'] = '<h2>34번 · 빈칸 추론(구) [3점]</h2>\n' + img(34) + '''<h3>① 빈칸 문장의 역할</h3>
<p>In other words, for Bourdieu, from the beginning of life, ___ — <b>In other words</b>이므로 바로 앞 문장(아이의 쾌·불쾌는 이미 계급에 따라 정해져 있다, 가장 '순수한' 쾌락도 사회적으로 조건 지어진 경험에 뿌리를 둔다)을 다시 말한 것입니다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">the pleasure and the aversion they experience are class-specific … the ‘purest’ pleasures … are rooted in these <b>socially conditioned</b> experiences.</span><br>socially conditioned ↔ <b>④ 모든 경험은 이미 외부 세계에 의해 조건 지어져 있다</b>. 빈칸 뒤 and this influence(이 영향)도 '외부 세계의 영향'을 받습니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 인간은 비슷한 행동 양식을 갖도록 타고났다 <span class="x">— 계급에 따라 '다르다'는 내용이고, '타고났다'는 사회적 조건과 반대입니다.</span></li>
<li>② 타고난 능력은 계급 차이와 상관없이 드러난다 <span class="x">— 정반대입니다.</span></li>
<li>③ 각 개인이 사회 계급 형성에 기여한다 <span class="x">— 방향이 거꾸로입니다. 계급이 개인의 경험을 형성합니다.</span></li>
<li class="ans">④ 모든 경험은 이미 외부 세계에 의해 조건 지어져 있다 <span class="o">— 정답.</span></li>
<li>⑤ 작가는 다른 사람보다 아름다움에 더 민감하다 <span class="x">— 작가의 민감성 비교는 나오지 않습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">the pleasure and the aversion they experience are class-specific, <b>according to the volume of capital they can access</b>, <b>so that</b> the ‘purest’ pleasures … are rooted in …</span><br>according to(~에 따라) + so that(그래서 결과적으로). 결과의 so that 뒤가 빈칸의 직접 근거입니다.</div>
<div class="tip"><b>빈칸(구) 공략법</b> In other words, That is 빈칸은 <b>바로 앞 문장의 재진술</b>입니다. 앞 문장의 핵심어(socially conditioned)를 다른 말로 바꾼 선택지를 고르고, 방향이 거꾸로 된 ③을 조심하세요.</div>'''

S['36'] = '<h2>36번 · 글의 순서 [2점]</h2>\n' + img(36) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">표현의 자유에서 개인의 자율성은 <b>개인적(individual)</b>일 수도, <b>관계적(relational)</b>일 수도 있다</td><td class="l">→ 두 측면을 차례로 설명할 차례</td></tr>
<tr><td>(B)</td><td class="l">개인의 발언은 인격 발달을 위해 보호되어야 한다</td><td class="l">첫 번째 '개인적' 측면 → 주어진 글 바로 뒤</td></tr>
<tr><td>(C)</td><td class="l"><b>Relational autonomy, however,</b> 청중의 이익도 고려</td><td class="l">두 번째 '관계적' 측면, however로 (B)와 대조 → (B) 뒤</td></tr>
<tr><td>(A)</td><td class="l">European legal systems <b>also</b> take <b>the latter aspect</b> into account</td><td class="l">the latter(후자) = 관계적 측면 → (C) 뒤</td></tr>
</table>
<h3>② 정답: ③ (B)-(C)-(A)</h3>
<div class="key">두 측면 소개 → (B) 개인적 측면 → (C) however, 관계적 측면(명예 훼손·혐오 발언처럼 타인의 자율성 제한) → (A) 유럽 법체계도 후자(관계적 측면)를 고려해 표현의 자유를 제한한다.</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— the latter aspect가 무엇의 '후자'인지 아직 설명되지 않았습니다.</span></li>
<li>(B)-(A)-(C)(②) <span class="x">— (A)의 관계적 측면 언급이 (C)의 정의보다 먼저 나와 순서가 거꾸로입니다.</span></li>
<li>(C)로 시작(④, ⑤) <span class="x">— however로 대조할 '개인적 측면'이 앞에 없습니다.</span></li>
</ul>
<div class="tip"><b>순서 공략법</b> 주어진 글이 'A와 B 두 가지'를 소개하면 대개 <b>A 설명 → B 설명 → B의 사례/적용</b> 순서입니다. the latter, the former 같은 말은 두 개념이 모두 설명된 뒤에 나옵니다.</div>'''

S['37'] = '<h2>37번 · 글의 순서 [2점]</h2>\n' + img(37) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">시력이 안전 운전에 중요하다는 믿음 때문에 대부분 나라의 운전면허 시험에 시력 측정이 들어 있다</td><td class="l">→ 그 '요건'에 대한 반론이 이어질 차례</td></tr>
<tr><td>(B)</td><td class="l"><b>Despite these requirements</b>, 시력과 사고 기록의 연관은 거의 찾지 못했다</td><td class="l">these requirements = 면허 시험의 시력 측정 → 주어진 글 바로 뒤</td></tr>
<tr><td>(A)</td><td class="l"><b>The fact is</b> 운전은 시각·인지가 함께 필요한 복잡한 일, 짧은 시간에 앞일을 해석해야 한다</td><td class="l">(B)의 '측정한 시력이 너무 단순할 수 있다'의 이유 → (B) 뒤</td></tr>
<tr><td>(C)</td><td class="l"><b>To do this</b>, 운전자는 다른 운전자 행동에 대한 기대를 발전시켰다</td><td class="l">this = (A)의 '앞일을 해석하기' → (A) 뒤</td></tr>
</table>
<h3>② 정답: ② (B)-(A)-(C)</h3>
<div class="key">면허 시험의 시력 측정 → (B) 그런데 시력과 사고의 연관은 없었다, 측정하는 시력이 너무 단순할 수 있다 → (A) 사실 운전은 시각과 인지가 함께하는 복잡한 일 → (C) 그것(앞일 해석)을 위해 운전자는 기대를 발전시키고, 시각 체계가 늘 잘 맞지는 않는 판단을 한다.</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— The fact is(사실은)는 앞의 통념을 반박할 때 쓰는데, 주어진 글 다음 바로 반박하기엔 (B)의 '연관 없음' 결과가 먼저 필요합니다.</span></li>
<li>(B)-(C)-(A)(③) <span class="x">— (C)의 To do this가 가리킬 '앞일 해석'이 (A)에 있으므로 (C)가 (A)보다 앞설 수 없습니다.</span></li>
<li>(C)로 시작(④, ⑤) <span class="x">— To do this의 this가 주어진 글의 '시험'을 가리키면 뜻이 통하지 않습니다.</span></li>
</ul>
<div class="tip"><b>순서 공략법</b> <b>Despite these + 명사</b>는 앞 단락의 내용을 바로 받고, <b>To do this</b>는 앞 단락의 '해야 할 일'을 받습니다. 지시어가 가리키는 대상을 한 단어로 적어 두면 순서가 저절로 정해집니다.</div>'''

S['38'] = '<h2>38번 · 문장 삽입 [2점]</h2>\n' + img(38) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<p><b>For example</b>, in English, words like ‘eleven’ and ‘twelve’ <b>do not directly reflect</b> the values … → ① 앞에 '언어마다 수 체계가 다르다'는 일반 진술이 필요하고, ② 뒤에는 이와 <b>대조</b>되는 예(값을 그대로 드러내는 언어)가 와야 합니다.</p>
<h3>② 정답: ②</h3>
<div class="key"><span class="en">… there are distinct language and cultural differences in how counting systems are used. ( ② ) <b>However, in Chinese</b>, the number system is very logical, with words that <b>directly reflect</b> the values …</span><br>② 뒤의 However, in Chinese(그러나 중국어에서는)는 대조할 다른 언어가 앞에 있어야 합니다. 주어진 문장(영어는 값을 직접 드러내지 않는다)이 들어가야 'directly reflect'가 정확히 대조됩니다.</div>
<h3>③ 위치별 점검</h3>
<ul class="ch">
<li>① <span class="x">— 앞은 타고난 수 감각과 학습 이야기라 영어 예시가 나올 자리가 아닙니다.</span></li>
<li class="ans">② <span class="o">— 정답.</span> 일반 진술 → For example 영어 → However 중국어</li>
<li>③ <span class="x">— 중국어 설명 → For example 20 = ershí로 자연스럽게 이어집니다.</span></li>
<li>④ <span class="x">— But it is not only the linguistic representation …으로 '표현'에서 '체계'로 화제가 넘어가는 자리입니다.</span></li>
<li>⑤ <span class="x">— 다른 수 체계(마야의 20진법) 예시로 이어지는 자리입니다.</span></li>
</ul>
<div class="tip"><b>삽입 공략법</b> 주어진 문장이 For example로 시작하면 <b>일반 진술 바로 뒤</b>, 그리고 뒤 문장이 However로 시작하면 <b>대조되는 짝</b>이 있는지 확인하세요. '직접 드러내지 않는다 ↔ 직접 드러낸다'처럼 같은 표현의 반대가 결정적 단서입니다.</div>'''

S['39'] = '<h2>39번 · 문장 삽입 [3점]</h2>\n' + img(39) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<p><b>Once you plug the holes in the hose</b>, all the water goes then out the nozzle; in your brain, this is analogous to <b>the synapses relaying the correct messages being much stronger</b> … → 앞에는 '구멍 난 호스 = 처음 배우는 뇌' 비유가, 뒤에는 '뇌가 이것을 어떻게 이루는지'가 와야 합니다.</p>
<h3>② 정답: ④</h3>
<div class="key"><span class="en">… the water running out the holes is all the erroneous information your brain is sending to your fingers, lips, etc. ( ④ ) <b>The brain accomplishes this</b> through changing the structure of the synapse …</span><br>④ 뒤 The brain accomplishes this의 this(이것)는 '올바른 시냅스를 강하게 만드는 것'이어야 하는데, ④ 앞에는 '새는 물 = 잘못된 정보'뿐입니다. 주어진 문장(구멍을 막으면 올바른 시냅스가 훨씬 강해진다)이 들어가야 this가 해결됩니다.</div>
<h3>③ 위치별 점검</h3>
<ul class="ch">
<li>① <span class="x">— 호스 비유가 소개되기 전이라 the hose가 가리킬 대상이 없습니다.</span></li>
<li>② <span class="x">— 호스에 구멍이 많다는 설명 직후라, 아직 '물이 새는' 상황도 나오지 않았습니다.</span></li>
<li>③ <span class="x">— This is what your brain is like …(처음 배울 때의 뇌)로 비유를 해석하는 문장이 바로 이어져야 합니다.</span></li>
<li class="ans">④ <span class="o">— 정답.</span> 새는 호스(처음) → 구멍 막기(연습 후) → The brain accomplishes this</li>
<li>⑤ <span class="x">— this(구조 변화)를 neurons that fire together wire together로 설명하는 흐름이 자연스럽습니다.</span></li>
</ul>
<div class="tip"><b>삽입 공략법</b> 비유 지문은 <b>비유 → 해석 → 다음 단계 비유 → 해석</b>의 짝을 맞추세요. 뒤 문장의 this가 가리킬 내용이 앞에 없는 곳이 바로 삽입 자리입니다.</div>'''

S['40'] = '<h2>40번 · 요약문 완성 [2점]</h2>\n' + img(40) + '''<h3>① 요약문 구조</h3>
<p>실험에서 마사지 중 휴식을 가진 참가자들은 길고 연속적인 마사지를 받은 참가자들보다 더 <b>(A)</b>했는데, 이는 휴식이 긍정적 경험에 대한 참가자들의 적응을 <b>(B)</b>했음을 보여 준다.</p>
<h3>② 정답: ① content(만족한) … blocked(막았다)</h3>
<div class="key"><span class="en">those forced to take a 20-second break … gave a rating of 7.05 ― that’s a 17% improvement in satisfaction. … the break in pleasure <b>prevents us from becoming too familiar with</b> the positive experience</span><br>(A) 만족도가 더 높았다 → <b>content</b>, (B) 익숙해지는 것(적응, habituation)을 막는다 → <b>blocked</b></div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li class="ans">① content … blocked <span class="o">— 정답.</span></li>
<li>② bored … prompted <span class="x">— 둘 다 반대입니다. 더 즐거웠고, 적응을 막았습니다.</span></li>
<li>③ relaxed … sustained <span class="x">— relaxed는 그럴듯하지만, 적응을 '유지시켰다'는 반대입니다. 한 칸만 맞는 함정.</span></li>
<li>④ annoyed … interrupted <span class="x">— interrupted는 맞지만 짜증이 났다는 (A)가 반대입니다. 한 칸만 맞는 함정.</span></li>
<li>⑤ refreshed … reinforced <span class="x">— 적응을 '강화했다'는 반대입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">the break in pleasure <b>prevents</b> us <b>from</b> becoming too familiar with the positive experience and <b>thus</b> noticing it less</span><br>prevent A from -ing: A가 ~하지 못하게 막다. from 뒤 becoming과 noticing이 and thus로 병렬 연결됩니다.</div>
<div class="tip"><b>요약문 공략법</b> 실험 지문은 <b>결과 수치(6.05 vs 7.05)</b>로 (A)를, <b>But the theory is that</b> 뒤의 설명으로 (B)를 정합니다. 한 칸만 맞는 선택지(③, ④)를 꼭 걸러 내세요.</div>'''

json.dump(S, open('secs_05g3.json', 'w'), ensure_ascii=False)
print(len(S))
