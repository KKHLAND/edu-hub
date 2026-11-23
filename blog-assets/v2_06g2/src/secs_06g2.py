import json, sys
REF = sys.argv[1] if len(sys.argv) > 1 else 'REF'
B = f'https://raw.githubusercontent.com/KKHLAND/edu-hub/{REF}/blog-assets/v2_06g2/'
def img(n, lab=None):
    lab = lab or f'{n}번'
    return (f'<img src="{B}q{n}.png" alt="2026년 6월 고2 영어 {lab} 발문 지문 선택지 해석 어휘">\n'
            '<p class="cap">발문·지문·선택지·해석·어휘</p>\n')
S = {}
S['21'] = '<h2>21번 · 함축 의미 추론 [3점]</h2>\n' + img(21) + '''<h3>① 지문 구조</h3>
<p><b>사실</b> 인간은 시각적 심상에 뛰어나다(머릿속 모델로 행동을 미리 연습) → <b>근거</b> 뇌는 상상할 때도 실제로 볼 때와 같은 영역을 쓴다 → <b>단서</b> 그러나 진화는 상상이 <b>결코 진짜만큼 생생하지 않게</b> 해 두었다 → 밑줄: 유전자 쪽의 현명한 자제 → <b>이유</b> 상상이 완벽한 대체물이면 상상 속 잔치로 만족해 진짜 음식을 찾지 않고 굶어 죽을 것이다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">But evolution has seen to it that such internally generated representations are <b>never as authentic as the real thing</b>. This is a wise bit of self-restraint on your genes’ part.</span><br>→ This가 가리키는 것은 바로 앞 문장, 즉 '상상이 진짜만큼 사실적이지 않게 한 것'입니다. 그래서 <b>① 상상이 얼마나 사실적일 수 있는지를 진화가 영리하게 제한한 것</b>이 정답입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li class="ans">① evolution’s clever limiting of how realistic your imagination is <span class="o">— 정답.</span> never as authentic ↔ limiting how realistic, wise ↔ clever</li>
<li>② 인간이 논리적 존재로 진화하지 못했다는 눈에 보이는 증거 <span class="x">— 실패가 아니라 '현명한' 장치라고 했으므로 반대 평가입니다.</span></li>
<li>③ 상상할 수 있는 것에 대한 불필요한 제약 <span class="x">— 제약이긴 하지만 '불필요하다'가 아니라 생존에 꼭 필요한(wise) 것입니다.</span></li>
<li>④ 진짜 배고픔을 무시하도록 돕는 영리한 유전 전략 <span class="x">— 정반대입니다. 상상으로 배고픔을 무시하지 '못하게' 해서 진짜 음식을 찾게 합니다.</span></li>
<li>⑤ 뇌가 심상을 분류하는 기발한 방법 <span class="x">— 심상의 '분류'는 글에 나오지 않습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en"><b>If</b> your internal model of the world <b>were</b> a perfect substitute, then anytime you felt hungry you <b>could</b> simply imagine yourself at a banquet.</span><br>가정법 과거(If + 과거동사 were, 주어 + could + 동사원형): '만약 ~라면 …할 수 있을 텐데'. 현실은 그렇지 않다는 뜻이므로, 상상은 완벽한 대체물이 '아니다'라는 필자의 요점을 거꾸로 보여 줍니다.</div>
<div class="tip"><b>함축 의미 공략법</b> 밑줄에 <b>This</b>가 있으면 바로 앞 문장이 밑줄의 내용입니다. wise·self-restraint처럼 '평가'가 담긴 말은 선택지에서 긍정/부정 방향까지 맞아야 하므로 ②·③처럼 부정적으로 평가한 선택지를 먼저 지우세요.</div>'''

S['29'] = '<h2>29번 · 어법 [3점]</h2>\n' + img(29) + '''<h3>① 지문 구조</h3>
<p><b>인용</b> 문명은 생각하지 않고 할 수 있는 일의 수를 늘리며 발전한다(Whitehead) → <b>예</b> 할인 쿠폰: 쿠폰을 내면 값이 싸진다고 기계적으로 가정 → <b>실험</b> 인쇄 오류로 할인이 전혀 없는 쿠폰도 정상 쿠폰만큼 반응을 얻음 → <b>결론</b> 쿠폰은 돈뿐 아니라 '생각하는 시간과 정신적 에너지'도 아껴 준다.</p>
<h3>② 정답: ② producing → produced</h3>
<div class="key"><span class="en">Mailed-out coupons [that ― because of a printing error ― offered no savings to recipients] ② <b>producing</b> just as much customer response as did error-free coupons …</span><br>주어는 <b>Mailed-out coupons</b>이고, that ~ recipients는 주어를 꾸미는 관계절입니다. 관계절을 괄호로 묶으면 문장의 본동사가 없습니다. 분사 producing으로는 문장이 완성되지 않으므로 과거시제 동사 <b>produced</b>가 와야 합니다. 뒤의 as <b>did</b> error-free coupons도 produced를 받는 대동사입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① offered <span class="x">— the "advance" (which was) offered to civilization: 발전이 문명에 '제공된' 것이므로 과거분사(수동)가 맞습니다.</span></li>
<li class="ans">② producing <span class="o">— 정답(틀린 것).</span> 본동사 자리 → produced</li>
<li>③ that <span class="x">— The point is that + 완전한 절(we expect … double duty): 보어 역할을 하는 명사절 접속사 that이 맞습니다.</span></li>
<li>④ do <span class="x">— Not only가 문장 앞에 나와 도치: Not only <b>do we expect</b> them …. 주어 we, 일반동사 expect이므로 do가 맞습니다.</span></li>
<li>⑤ potentially <span class="x">— 형용사 important를 꾸미므로 부사가 맞습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en"><b>Not only do we expect</b> them to save us money, we also expect them to save us the time and mental energy …</span><br>부정어(Not only)가 문두에 오면 '조동사 + 주어 + 동사' 어순으로 도치됩니다. expect + 목적어 + to부정사(…가 ~하기를 기대하다) 구조도 함께 익혀 두세요.</div>
<div class="tip"><b>어법 공략법</b> 밑줄이 <b>-ing</b>이면 그 문장에 본동사가 따로 있는지 먼저 확인하세요. 주어 뒤에 관계절·삽입구(― … ―)가 길게 붙으면 괄호로 묶고 '주어 + 동사'만 남겨 보는 것이 가장 빠릅니다.</div>'''

S['30'] = '<h2>30번 · 문맥상 낱말의 쓰임 [2점]</h2>\n' + img(30) + '''<h3>① 지문 구조</h3>
<p><b>주제</b> 혁신적 첨단 제품은 가격 탄력성이 낮다(가격이 변해도 수요가 크게 변하지 않음) → <b>이유 1</b> 대체품이 적어 바꾸는 비용이 높다 → <b>이유 2</b> 초기 구매자는 돈이 많아 가격에 민감하지 않다(예: 자산 250만 달러 이상의 백만장자 가구) → <b>결과</b> 경쟁자도 가격을 내리지 않고, 높은 가격은 품질의 신호가 된다.</p>
<h3>② 정답: ③ more → less</h3>
<div class="key"><span class="en">buyers — either innovators or forerunners — are ③ <b>more</b> sensitive to price than to additional performance; they often have deep pockets or are ready to spend a lot …</span><br>세미콜론 뒤는 앞 내용의 이유입니다. 주머니가 두둑하고 돈을 많이 쓸 준비가 된 사람들은 가격보다 추가 성능에 '덜' 민감해야 합니다. 뒤의 <b>customers, not sensitive to price</b>와도 맞추려면 <b>less</b>가 적절합니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① demand <span class="x">— 가격 탄력성이 낮다 = 가격이 변해도 '수요'가 크게 변하지 않는다. 적절합니다.</span></li>
<li>② high <span class="x">— 대체품이 적으니 다른 제품으로 바꾸는 비용이 '높다'. 적절합니다.</span></li>
<li class="ans">③ more <span class="o">— 정답(부적절).</span> deep pockets, not sensitive to price와 충돌 → less</li>
<li>④ lowering <span class="x">— 고객이 가격에 둔감하므로 경쟁자도 가격을 '내릴' 생각이 없다. 적절합니다.</span></li>
<li>⑤ reinforces <span class="x">— 높은 가격이 품질의 신호로 여겨져 회사에 대한 신뢰를 '강화한다'. and 앞뒤가 같은 방향이라 적절합니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">These high-tech products have few substitutes, <b>meaning that</b> the costs to switch to another product are high.</span><br>, meaning that ~: 앞 문장 전체의 의미(결과)를 풀어 주는 분사구문입니다. '이는 ~라는 뜻이다'로 읽으면 흐름이 자연스럽습니다.</div>
<div class="tip"><b>어휘 공략법</b> more/less, high/low처럼 <b>반의어 짝이 있는 단어</b>가 밑줄이면 먼저 의심하세요. 세미콜론(;) 뒤의 이유와, 글 뒤쪽에서 같은 대상을 다시 설명하는 말(not sensitive to price)이 결정적 단서입니다.</div>'''

S['42'] = '<h2>42번 · 장문 어휘 [2점] (41번 제목 포함)</h2>\n' + img('41-42', '41~42번') + '''<h3>① 지문 구조</h3>
<p><b>현상</b> 석유의 주 소비처는 운송인데, 유가가 비싸 엔진 효율이 크게 높아졌다 → <b>전망</b> 유가가 더 오르면 연료전지 기술이 더 탄력을 받는다(자동차 회사들이 이미 시제품 개발) → <b>가정</b> 연료전지 기술이 돌파구를 찾으면 유가 폭락 → 석유 회사·OPEC는 큰 수입 손실 → <b>대응</b> 그래서 다른 수입원을 찾는다(석유 메이저는 에너지 회사로 다각화).</p>
<h3>② 정답: ⑤ (e) exclude → develop</h3>
<div class="key"><span class="en">The ‘oil majors’ have diversified and are now more energy companies than oil companies these days and the OPEC countries are urgently attempting to (e) <b>exclude</b> other industries.</span><br>위협이 현실이라 생산자들이 <b>alternative sources of income</b>(다른 수입원)을 찾는다고 했고, 석유 메이저도 '다각화'했습니다. OPEC 국가들도 같은 방향이어야 하므로 다른 산업을 '배제하는(exclude)' 것이 아니라 '개발하려고(develop)' 애쓴다가 맞습니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>(a) efficient <span class="x">— 석유가 비싸서 엔진이 연료 소비에 훨씬 '효율적'이 되었다. 적절합니다.</span></li>
<li>(b) receive <span class="x">— 유가가 더 오르면 연료전지 기술이 또 다른 추진력을 '얻는다'. 적절합니다.</span></li>
<li>(c) lose <span class="x">— 유가가 폭락하면 석유 회사와 OPEC는 많은 수입을 '잃게' 된다. 적절합니다.</span></li>
<li>(d) alternative <span class="x">— 위협 때문에 '대안적' 수입원을 찾는다. 적절합니다.</span></li>
<li class="ans">(e) exclude <span class="o">— 정답(부적절).</span> diversified와 같은 방향 → develop</li>
</ul>
<h3>④ 41번 제목도 함께</h3>
<div class="key">연료 효율 향상과 연료전지 기술이 석유를 위협하고, 석유 산업은 다각화로 대응한다 → <b>① Oil Under Threat: Innovation Reshapes the Energy Landscape</b>. ⑤(유가 등락의 순환)는 유가가 '오르고 내리는 주기'가 아니라 기술 혁신으로 인한 구조 변화라는 점에서 어긋납니다.</div>
<div class="tip"><b>장문 어휘 공략법</b> 마지막 밑줄은 글의 결론과 직결되는 경우가 많습니다. 같은 문장 안의 <b>and</b> 앞(oil majors have diversified)과 뒤(OPEC countries …)가 같은 방향인지 확인하세요.</div>'''

S['31'] = '<h2>31번 · 빈칸 추론(구) [2점]</h2>\n' + img(31) + '''<h3>① 빈칸 문장의 역할</h3>
<p>도시 광장과 쇼핑 거리는 '미래를 견뎌 내는(future-proof)' 기술이다 → 예: 마차 채찍·타자기를 팔던 같은 가게가 지금은 휴대폰 수리와 버블티를 판다 → <b>빈칸 문장</b>: 같은 기반 시설이 ______을 지탱한다(예시의 일반화) → Jane Jacobs: 도시 건축의 큰 장점은 쓰임의 변화를 지탱하는 능력.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">the great advantage of a city architecture is its ability to <b>support change in uses</b></span><br>빈칸 문장 The same infrastructure <b>supports</b> ____와 동사 support까지 같습니다. change in uses = <b>① evolving uses</b>(변화하는 쓰임).</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li class="ans">① evolving uses <span class="o">— 정답.</span> 같은 가게, 달라진 용도</li>
<li>② social connections <span class="x">— 광장이 사람을 모은다는 이야기는 없습니다. 상식으로 고르기 쉬운 오답.</span></li>
<li>③ limited functions <span class="x">— 반대입니다. 쓰임이 '한정'되지 않고 계속 바뀝니다.</span></li>
<li>④ architectural innovation <span class="x">— 건물(기반 시설)은 '같은' 것이고, 바뀌는 것은 안에서 파는 것입니다.</span></li>
<li>⑤ collaborative work <span class="x">— 협업은 글에 나오지 않습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">The city square is a fairly future-proof technology, <b>as is</b> the shopping street.</span><br>as + 동사 + 주어: '~도 그렇듯이'. as is the shopping street = the shopping street is also a future-proof technology.</div>
<div class="tip"><b>빈칸 공략법</b> For example 뒤의 예시 바로 다음에 오는 빈칸은 <b>예시를 한 단어로 일반화</b>한 말입니다. 그리고 글 뒤쪽에서 필자(또는 인용된 학자)가 같은 말을 다시 합니다(support change in uses).</div>'''

S['32'] = '<h2>32번 · 빈칸 추론(구) [2점]</h2>\n' + img(32) + '''<h3>① 빈칸 문장의 역할</h3>
<p>유전체학 혁명으로 접촉이 식물에 얼마나 영향을 주는지 볼 수 있게 됨 → <b>빈칸 문장</b>: 접촉이 호르몬과 유전자 발현에 극적인 반응을 일으켜 ______할 수 있었다(결론 먼저) → 실험: 붓으로 쓰다듬자 30분 만에 유전체 10% 변화 → 키 크는 데서 에너지를 돌림 → 여러 번 만지면 위쪽 성장률이 30%까지 감소.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">rerouting energy away from the hard work of <b>getting taller</b> … arabidopsis <b>cut its upward growth rate</b> by as much as 30 percent.</span><br>실험 결과가 곧 빈칸입니다. 성장률을 줄였다 = <b>② inhibit their growth</b>(성장을 억제하다).</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① impact their lifespan <span class="x">— 수명 이야기는 없습니다.</span></li>
<li class="ans">② inhibit their growth <span class="o">— 정답.</span> cut its upward growth rate</li>
<li>③ lift their reproduction rate <span class="x">— 번식률은 언급되지 않습니다.</span></li>
<li>④ hinder their defense capability <span class="x">— 오히려 방해(disturbance)에 대처하려고 우선순위를 바꾸는 것이라 방어를 '방해'한다는 말은 반대 방향입니다.</span></li>
<li>⑤ increase their maximum height <span class="x">— 정반대입니다. 키 크는 일에서 에너지를 빼냅니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">touch quietly triggered <b>such</b> a dramatic response in their hormones and gene expression <b>that</b> it could substantially …</span><br>such + a + 형용사 + 명사 + that ~: '너무 ~한 …라서 ~하다'. 빈칸은 극적인 반응의 '결과'입니다.</div>
<div class="tip"><b>빈칸 공략법</b> 빈칸이 글 앞쪽에 있고 뒤에 실험이 나오면 <b>실험의 결과 문장</b>(마지막 수치)을 찾으세요. 30 percent 감소 → '억제'.</div>'''

S['33'] = '<h2>33번 · 빈칸 추론(구) [3점]</h2>\n' + img(33) + '''<h3>① 빈칸 문장의 역할</h3>
<p>진화는 조건(빙하기 시작, 강수량, 바람)이 변할 때까지 멈춘다 → 그런데 진화의 긴 시간 속에선 이런 변화가 실제로 일어난다 → <b>빈칸 문장</b>: 그 결과 진화는 보통 멈추지 않고 ______ → 예: 기온이 수백 년간 내려가면 털이 긴 쪽으로, 다시 오르면 짧은 쪽으로 밀려간다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">If there is a steady downward drift in the average temperature … growing longer coats of hair. If … the trend reverses … pushed towards growing <b>shorter</b> coats again.</span><br>환경이 바뀔 때마다 그 방향을 따라 진화의 방향도 바뀝니다 → <b>② constantly tracks the changing environment</b>(변화하는 환경을 끊임없이 따라간다).</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① occurs regardless of local temperature trend <span class="x">— 정반대입니다. 기온 추세에 '따라' 방향이 정해집니다.</span></li>
<li class="ans">② constantly tracks the changing environment <span class="o">— 정답.</span> 긴 털 ↔ 짧은 털의 예와 일치</li>
<li>③ finds ways to bring nature into balance <span class="x">— 진화가 자연의 균형을 '만든다'는 말은 없습니다. 환경에 맞춰 갈 뿐입니다.</span></li>
<li>④ makes species compete with one another <span class="x">— 종 간 경쟁은 나오지 않습니다.</span></li>
<li>⑤ gradually threatens the survival of hairy animals <span class="x">— 털 이야기를 이용한 함정. 생존 위협이 아니라 적응 방향의 변화입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">Such changes <b>do happen</b> when we are dealing with a timescale as long as the evolutionary one.</span><br>do + 동사원형: 강조('정말로 일어난다'). 앞 문장의 '조건이 변할 때까지 멈춘다'를 받아, 실제로는 조건이 변한다는 점을 힘주어 말합니다.</div>
<div class="tip"><b>빈칸 공략법</b> <b>not A but B</b>(does not come to a halt, but ____)의 빈칸은 A의 반대이면서 뒤 예시의 일반화입니다. '멈추지 않는다' + '환경 따라 방향을 바꾼다' 둘 다 만족하는 것은 ②뿐입니다.</div>'''

S['34'] = '<h2>34번 · 빈칸 추론(구) [3점]</h2>\n' + img(34) + '''<h3>① 빈칸 문장의 역할</h3>
<p>대도시의 높은 땅값은 자원의 효율적 사용에 영향을 준다 → 예: 뉴욕의 핫도그 노점이 왜 3,000개 넘게 있나? → 자원(땅·노동·자본·기업가 능력·재료) 중 뉴욕에서 가장 비싼 것은 <b>땅</b> → 노점 크기만큼 상업 공간을 빌리면 1년에 2만 달러 → 그러나 공공 보도는 노점상에게 공짜 → <b>빈칸 문장(결론)</b>: 이익을 극대화하려는 노점상은 ______.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">it could cost as much as $20,000 a year to rent that much commercial space. Aside from the necessary public permits, however, <b>space on the public sidewalk is free</b> to vendors.</span><br>비싼 자원(상업 공간) 대신 공짜 자원(보도)을 쓴다 → <b>⑤ substitute public sidewalks for costly commercial space</b>. substitute A for B: B 대신 A를 쓰다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① depend less on public sidewalks as their business expands <span class="x">— 정반대입니다. 보도에 '더' 의존합니다.</span></li>
<li>② negotiate ingredient prices with suppliers to cut costs <span class="x">— 재료(핫도그·빵)는 비싼 자원이 아닙니다. 핵심은 땅값.</span></li>
<li>③ devise new products to out-compete other vendors <span class="x">— 신제품 경쟁은 나오지 않습니다.</span></li>
<li>④ promote their business to attract potential customers <span class="x">— 홍보 이야기는 없습니다.</span></li>
<li class="ans">⑤ substitute public sidewalks for costly commercial space <span class="o">— 정답.</span> free sidewalk ↔ $20,000 rent</li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">Which of these do you suppose is most expensive in New York City?</span><br>의문사 + do you suppose(think) + 동사: '어느 것이 가장 비싸다고 생각하는가?' do you suppose는 삽입된 말이라 뒤에 바로 동사 is가 옵니다.</div>
<div class="tip"><b>빈칸 공략법</b> 첫 문장(땅값이 자원의 효율적 사용에 영향)과 마지막 빈칸은 짝입니다. 질문(Which … most expensive?)이 나오면 그 <b>답(땅)</b>이 빈칸의 핵심어가 됩니다. substitute A for B의 A·B 순서도 꼭 확인하세요.</div>'''

S['36'] = '<h2>36번 · 글의 순서 [3점]</h2>\n' + img(36) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">대부분의 동물은 생존 투쟁에 <b>모든 시간과 에너지</b>를 쓴다</td><td class="l">→ 남는 시간이 있다면? 이어질 차례</td></tr>
<tr><td>(B)</td><td class="l"><b>If they do have any time to spare</b>, 쉬거나 잔다 … This was also true for our early ancestors</td><td class="l">they = 주어진 글의 animals, 이야기를 '초기 조상'으로 옮김 → 주어진 글 바로 뒤</td></tr>
<tr><td>(A)</td><td class="l"><b>But</b> as they slowly evolved into more efficient hunters, the situation changed</td><td class="l">they = (B)의 early ancestors, 식량 찾기에 시달리던 상황을 뒤집음 → (B) 뒤</td></tr>
<tr><td>(C)</td><td class="l">특정 지역·시기에 먹이가 풍부하고 사냥 기술이 발달 → 놀라운 번영, <b>time on their hands</b></td><td class="l">(A) 끝의 some degree of affluence를 구체화 → (A) 뒤</td></tr>
</table>
<h3>② 정답: ② (B)-(A)-(C)</h3>
<div class="key">동물은 생존에 모든 시간을 씀 → (B) 시간이 나도 쉰다, 초기 조상도 마찬가지 → (A) 하지만 효율적 사냥꾼으로 진화하며 상황이 바뀌고 어느 정도 풍요를 누림 → (C) 특정 지역·시기엔 놀라운 번영, 여유 시간이 생김.</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— (A)의 they가 '사냥꾼으로 진화한' 존재여야 하는데, 주어진 글의 animals 전체로는 맞지 않습니다. 인간 조상 이야기는 (B)에서 처음 나옵니다.</span></li>
<li>(B)-(C)-(A)(③) <span class="x">— (C)에서 이미 번영과 여유를 누렸는데 (A)에서 But … the situation changed가 오면 흐름이 거꾸로 됩니다.</span></li>
<li>(C)로 시작(④, ⑤) <span class="x">— prey, hunting techniques의 주인공(초기 인류)이 아직 등장하지 않았습니다.</span></li>
</ul>
<div class="tip"><b>순서 공략법</b> <b>대명사 they가 누구인지</b>를 단락마다 확인하세요. 동물 일반 → 초기 조상(B) → 효율적 사냥꾼(A) → 번영(C). 일반에서 구체로, 결핍에서 풍요로 흐름이 이어집니다.</div>'''

S['37'] = '<h2>37번 · 글의 순서 [2점]</h2>\n' + img(37) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">깜짝 놀랐을 때 멈추고, <b>얼어붙고, 숨을 참으며</b> 위협을 살폈는가?</td><td class="l">→ 이 반응들의 기능 설명이 이어질 차례</td></tr>
<tr><td>(C)</td><td class="l"><b>All these responses</b> maximize our ability to avoid detection … 소리는 위치를 드러낼 수 있다</td><td class="l">All these responses = 주어진 글의 멈춤·얼어붙기·숨 참기 → 주어진 글 바로 뒤</td></tr>
<tr><td>(B)</td><td class="l"><b>Because of this</b>, the freeze response results in the inhibition of language … 위협이 지나면 목소리를 되찾는다</td><td class="l">this = (C)의 '소리가 위치를 드러냄' → (C) 뒤</td></tr>
<tr><td>(A)</td><td class="l"><b>But</b> what if we can never relax?</td><td class="l">(B) 끝의 '긴장을 풀고 목소리를 되찾는다'를 뒤집음 → (B) 뒤</td></tr>
</table>
<h3>② 정답: ⑤ (C)-(B)-(A)</h3>
<div class="key">놀라면 얼어붙는다 → (C) 이 반응들은 발각을 피하게 하고, 소리는 위치를 드러낸다 → (B) 그래서 극심한 스트레스 상황에선 언어가 억제되고, 위협이 지나면 목소리를 되찾는다 → (A) 그런데 결코 긴장을 풀 수 없다면? 만성 스트레스와 정신 질환으로 이어질 수 있다.</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— never relax는 '긴장을 푸는' 장면(B 끝)이 먼저 나와야 대조가 됩니다.</span></li>
<li>(B)로 시작(②, ③) <span class="x">— Because of this의 this(소리가 위치를 드러냄)가 아직 나오지 않았습니다.</span></li>
<li>(C)-(A)-(B)(④) <span class="x">— (A) 뒤에 (B)가 오면 만성 스트레스 이야기 뒤에 다시 '언어 억제'의 원리로 돌아가 흐름이 끊깁니다.</span></li>
</ul>
<div class="tip"><b>순서 공략법</b> <b>All these responses, Because of this</b>처럼 앞 내용을 묶어 받는 지시어가 가장 강력한 단서입니다. 그리고 마지막 단락은 But what if …?처럼 문제를 제기하며 글을 확장하는 경우가 많습니다.</div>'''

S['38'] = '<h2>38번 · 문장 삽입 [2점]</h2>\n' + img(38) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<p><b>The next step in this problematic process</b> would be having diminished emotional responses to violence … leading to <b>reduced empathy</b>.<br>→ 앞에는 '이 문제적 과정'의 앞 단계가 있어야 하고, 이 문장은 그 다음 단계(감정 반응 감소 → 공감 감소)입니다.</p>
<h3>② 위치별 점검</h3>
<table>
<tr><th>위치</th><th>앞 문장</th><th>판단</th></tr>
<tr><td>①</td><td class="l">비디오 게임은 공감과 관련해 가장 많이 연구된 기술</td><td class="l">× 아직 '과정'이 시작되지 않음</td></tr>
<tr><td>②</td><td class="l">폭력 게임에 대한 우려로 많은 연구가 진행됨</td><td class="l">× 연구 배경일 뿐</td></tr>
<tr><td>③</td><td class="l">과학자들이 게임이 공감에 영향을 주는 방식을 설명함</td><td class="l">× 설명이 이제 시작될 참</td></tr>
<tr><td>④</td><td class="l">폭력을 보면 부정적 감정·생리적 각성을 느끼는 것이 정상</td><td class="l">× 정상 반응, '문제적' 과정이 아님</td></tr>
<tr><td>⑤</td><td class="l">반복 노출로 정상 반응이 무뎌짐 = <b>desensitization</b>(둔감화)</td><td class="l">○ 문제적 과정의 1단계 → 다음 단계가 공감 감소</td></tr>
</table>
<h3>③ 정답: ⑤</h3>
<div class="key">둔감화(1단계) → <b>[주어진 문장] 다음 단계: 폭력에 대한 감정 반응 감소 → 공감 감소</b> → ⑤ 뒤: 폭력 게임과 공감 감소의 연관성을 보여 주는 많은 연구. ⑤ 뒤 문장의 reduced empathy가 주어진 문장의 reduced empathy를 그대로 이어받습니다.</div>
<div class="tip"><b>삽입 공략법</b> 주어진 문장에 <b>The next step</b>이 있으면 '첫 단계'가 어디서 끝나는지 찾으세요. 첫 단계의 이름(desensitization)이 붙는 순간이 바로 그 자리입니다.</div>'''

S['39'] = '<h2>39번 · 문장 삽입 [3점]</h2>\n' + img(39) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<p>Making a real difference with social problems is hard enough; to succeed, it has to follow from <b>an authentic, company-wide commitment to the purpose</b>.<br>→ 사회 문제를 실제로 바꾸려면 '진정한 회사 전체의 헌신'이 있어야 한다는 <b>조건</b>입니다. 이 조건을 받는 말(그렇지 않으면 …)이 뒤에 와야 합니다.</p>
<h3>② 위치별 점검</h3>
<table>
<tr><th>위치</th><th>앞 / 뒤</th><th>판단</th></tr>
<tr><td>①</td><td class="l">앞: 일부 브랜드는 실제로 좋은 일을 하기 전에 사회적 목적을 광고 / 뒤: 마케터들이 목적을 평판용으로 씀</td><td class="l">× 앞뒤가 같은 이야기로 자연스럽게 이어짐</td></tr>
<tr><td>②</td><td class="l">앞: 목적 자체를 받아들이지 않고 평판에 이용 / 뒤: <b>Otherwise</b> the mission is just window-dressing</td><td class="l">○ Otherwise(그렇지 않으면)가 받을 '조건'이 없음 → 주어진 문장이 필요</td></tr>
<tr><td>③</td><td class="l">앞: purpose-washing의 정의 / 뒤: 그 결과 엘리트의 속임수</td><td class="l">× 정의 → 결과로 연결됨</td></tr>
<tr><td>④·⑤</td><td class="l">purpose-washing 브랜드의 단기 이익과 장기 손실</td><td class="l">× 결과 설명이 이어지는 중</td></tr>
</table>
<h3>③ 정답: ②</h3>
<div class="key">브랜드가 목적을 평판용으로만 씀 → <b>[주어진 문장] 사회 문제 해결은 어렵고, 성공하려면 진정한 전사적 헌신이 있어야 한다</b> → Otherwise(그런 헌신이 없으면) 사명은 겉치레, 즉 'purpose-washing'일 뿐이다.</div>
<div class="tip"><b>삽입 공략법</b> <b>Otherwise, Instead, However</b>처럼 앞 문장과의 관계를 나타내는 연결어가 있는 문장은 바로 앞 문장과 논리가 맞는지 꼭 확인하세요. 원래 글에서 그 연결어가 받을 말이 없으면 그 앞이 빈자리입니다.</div>'''

S['40'] = '<h2>40번 · 요약문 완성 [3점]</h2>\n' + img(40) + '''<h3>① 요약문 구조</h3>
<p>The brain models <b>(A)</b> musical patterns, which creates the possibility for emotional impact to arise when musicians <b>(B)</b> these patterns, making music engaging.<br>→ 뇌는 (A)한 음악적 패턴을 모델링하고, 음악가가 그 패턴을 (B)할 때 감정적 효과가 생긴다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">Metrical extraction, knowing what the pulse is and <b>when we expect it to occur</b>, is a crucial part of musical emotion. Music communicates to us emotionally through <b>systematic violations of expectations</b>.</span><br>(A) 뇌가 모델링하는 것은 '예상되는' 박자 = <b>anticipated</b>. (B) 감정은 기대를 '위반할' 때 생긴다 = <b>break</b>. 정답은 <b>④ anticipated …… break</b>.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① unpredictable …… repeat <span class="x">— 뇌가 모델링하는 것은 '예측 불가능한' 패턴이 아니라 일정한(constant) 박자입니다. repeat도 반대.</span></li>
<li>② unpredictable …… disobey <span class="x">— (B)는 맞는 방향이지만 (A)가 틀립니다.</span></li>
<li>③ anticipated …… maintain <span class="x">— (A)는 맞지만, 패턴을 '유지'하기만 하면 감정적으로 밋밋하고 기계적인(flat and robotic) 음악이 됩니다.</span></li>
<li class="ans">④ anticipated …… break <span class="o">— 정답.</span> expect ↔ anticipated, violations ↔ break</li>
<li>⑤ established …… embody <span class="x">— (A)는 그럴듯하지만, 패턴을 '구현'하는 것은 위반이 아닙니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">These violations can occur in any domain … but <b>occur they must</b>.</span><br>동사(occur)를 앞으로 보낸 강조 도치: '하지만 반드시 일어나야 한다'. 위반은 선택이 아니라 필수라는 필자의 강조입니다.</div>
<div class="tip"><b>요약문 공략법</b> 요약문의 단어는 본문의 단어를 다른 말로 바꿔 씁니다(expect → anticipated, violation → break). (A)와 (B)를 따로따로 판단해 두 칸 모두 맞는 짝만 남기세요.</div>'''

json.dump(S, open('secs_06g2.json', 'w'), ensure_ascii=False)
print(len(S))
