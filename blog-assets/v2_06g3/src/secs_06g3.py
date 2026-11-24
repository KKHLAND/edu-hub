import json, sys
REF = sys.argv[1] if len(sys.argv) > 1 else 'REF'
B = f'https://raw.githubusercontent.com/KKHLAND/edu-hub/{REF}/blog-assets/v2_06g3/'
def img(n, lab=None):
    lab = lab or f'{n}번'
    return (f'<img src="{B}q{n}.png" alt="2026년 6월 고3 영어 모의고사(모평) {lab} 발문 지문 선택지 해석 어휘">\n'
            '<p class="cap">발문·지문·선택지·해석·어휘</p>\n')
S = {}
S['21'] = '<h2>21번 · 함축 의미 추론 [3점]</h2>\n' + img(21) + '''<h3>① 지문 구조</h3>
<p><b>도입</b> 과학자들이 동물에게 의식을 인정한 것은 인터넷보다도 최근 일이다 → <b>인물</b> 동물학자 Griffin(1976): 동물의 인지를 진지하게 다뤄야 한다 → <b>근거</b> 박쥐의 유연한 행동, 즉석 의사 결정, 인간과 같은 문제 해결 능력 → <b>결론</b> 신경과학이 발전했어도 '의식'을 담당하는 인간 고유의 뇌 부위는 아무도 찾지 못했다 → 밑줄: 이제 the ghost를 버릴 때가 아닌가?</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">no one had yet found any part of the brain <b>unique to humans</b> that might be responsible for this <b>hallowed “consciousness.”</b> Wasn’t it time to give up the ghost?</span><br>'신성시되는(hallowed)' 의식이 인간에게만 있다는 생각을 뒷받침할 증거가 없으니 버리자는 말입니다. the ghost = <b>② 의식은 인간만이 가진 특성이라는 믿음</b>.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 동물의 의식을 연구해야 한다는 주장 <span class="x">— Griffin이 내세운 주장 그 자체입니다. 버릴 대상이 아니라 지지하는 대상이라 정반대입니다.</span></li>
<li class="ans">② 의식이 인간에게만 있는 특성이라는 믿음 <span class="o">— 정답.</span> unique to humans + hallowed consciousness</li>
<li>③ 동물에게 정말로 의식 있는 내면세계가 있다는 착각 <span class="x">— Griffin은 동물에게 내면세계가 있다고 '확신'했습니다. 착각이라고 보지 않습니다.</span></li>
<li>④ 인간의 인지가 동물보다 우월하다는 생각 <span class="x">— 그럴듯하지만 글의 초점은 '우월함'이 아니라 '의식이 인간에게만 있느냐'입니다.</span></li>
<li>⑤ 인간과 동물이 본질적으로 비슷하다는 개념 <span class="x">— 필자 쪽 결론에 가까운 생각이라, 버려야 할 ghost가 될 수 없습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">scientists attributing consciousness to any animal is <b>so</b> recent <b>that</b> the internet is older.</span><br>동명사구(scientists attributing …)가 주어이고 attributing의 의미상 주어가 scientists입니다. attribute A to B: A를 B의 것으로 보다. so ~ that …: '너무 ~해서 …하다'.</div>
<div class="tip"><b>함축 의미 공략법</b> give up(버리다), get rid of 같은 동사 뒤의 밑줄은 <b>필자가 반대하는 생각</b>입니다. 필자(또는 인용된 학자)의 주장을 정리한 다음, 그 반대편 생각을 고르세요. ①처럼 필자 주장을 그대로 옮긴 선택지부터 지우면 됩니다.</div>'''

S['29'] = '<h2>29번 · 어법 [2점]</h2>\n' + img(29) + '''<h3>① 지문 구조</h3>
<p><b>주제</b> 패션은 언제나 깊이 문화적이다(유럽 의복의 진화) → 중세 초: 단순한 옷 → 직물 기술 발전: 정교하고 몸에 맞는 스타일 → 르네상스·엘리자베스 시대: 더 화려해짐 → 의복과 신분의 연결이 강해 사치품 착용을 제한하는 법까지 생김 → 상류층 스타일은 의식(儀式)에 통합되어 신분을 드러냄.</p>
<h3>② 정답: ② what → that(또는 which)</h3>
<div class="key"><span class="en">fashion began moving toward <b>styles</b> ② <b>what</b> were more elaborate and form-fitting.</span><br>앞에 선행사 styles가 있고, 뒤는 주어가 빠진 불완전한 절(were more elaborate …)입니다. 선행사를 받는 주격 관계대명사 <b>that/which</b>가 와야 합니다. what은 '선행사를 포함한' 관계대명사라 선행사 바로 뒤에 올 수 없습니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① frequently <span class="x">— 과거분사 made를 꾸미므로 부사가 맞습니다(was frequently made of).</span></li>
<li class="ans">② what <span class="o">— 정답(틀린 것).</span> 선행사 styles + 불완전한 절 → that/which</li>
<li>③ to limit <span class="x">— laws were enacted <b>to limit</b> …: '제한하기 위해' 법이 제정되었다. 목적을 나타내는 to부정사가 맞습니다.</span></li>
<li>④ Allowed <span class="x">— 의미상 주어 luxurious styles and decorations가 '허용되는' 대상이므로 수동의 과거분사 분사구문이 맞습니다.</span></li>
<li>⑤ their <span class="x">— 가리키는 것이 복수 upperclass styles이므로 their가 맞습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">The connection between clothing and social status was <b>so</b> pronounced <b>that</b> laws were enacted to limit …</span><br>so + 형용사 + that 결과절: '너무 뚜렷해서 ~하는 법이 제정되었다'. 주어가 The connection(단수)이므로 동사도 was입니다(between ~ status는 수식어).</div>
<div class="tip"><b>어법 공략법</b> what이 밑줄이면 <b>바로 앞에 명사(선행사)가 있는지</b> 먼저 보세요. 선행사가 있으면 what은 틀리고 that/which가 맞습니다. 반대로 선행사가 없고 뒤가 불완전하면 what이 맞습니다.</div>'''

S['30'] = '<h2>30번 · 문맥상 낱말의 쓰임 [3점]</h2>\n' + img(30) + '''<h3>① 지문 구조</h3>
<p><b>도입</b> 셰익스피어 같은 고전 희곡이나 뮤지컬 가사는 비관습적 표현을 써서 이해하려면 기술과 인내가 필요하다 → <b>방법</b> 시적 형식을 방해물로 보지 말고 의미를 드러내는 기법으로 보라, 여러 번 읽어라 → <b>뮤지컬</b> 대사보다 노래·춤의 비중이 커서 읽으며 떠올리기 특히 어렵다 → 음악과 가사를 빼면 남는 대사(book, libretto)는 매우 ___하다 → 춤·동작은 무대에서는 시간이 오래 걸리지만 대본에선 공간을 거의 차지하지 않는다.</p>
<h3>② 정답: ④ thick → thin</h3>
<div class="key"><span class="en">what is left is the dialogue, known as the book or libretto, and it can be very ④ <b>thick</b>. There is an emphasis on dance … that can be time-consuming when actually performed on stage, but can take <b>very little space</b> when typed into a play script.</span><br>뮤지컬은 <b>대사에 대한 강조가 줄어든(diminished emphasis on dialogue)</b> 장르이고, 춤·동작은 대본에서 공간을 거의 차지하지 않습니다. 그러니 음악과 가사를 뺀 대본은 '두꺼운' 것이 아니라 '얇은(thin)' 것이 맞습니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① revealing <span class="x">— 형식을 방해물이 아니라 '많은 것을 드러내는' 문체 기법으로 보라. but instead와 맞는 긍정적 표현이라 적절합니다.</span></li>
<li>② clear <span class="x">— 여러 번 더 읽어야 뉘앙스가 '명확해진다'. 적절합니다.</span></li>
<li>③ significant <span class="x">— 대사 강조는 줄고(diminished), 노래와 춤 강조는 '상당하다'. 대조가 맞습니다.</span></li>
<li class="ans">④ thick <span class="o">— 정답(부적절).</span> diminished emphasis on dialogue, very little space → thin</li>
<li>⑤ time-consuming <span class="x">— 무대에서는 '시간이 걸리지만', 대본에서는 공간을 거의 차지하지 않는다. but 앞뒤 대조가 맞습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">The reader must be mindful <b>not to let</b> the poetic form or archaic word usage <b>get in the way of</b> getting meaningful information …</span><br>let + 목적어 + 동사원형(get), 부정은 not to let. get in the way of -ing: '~하는 데 방해가 되다'.</div>
<div class="tip"><b>어휘 공략법</b> thick/thin, increase/decrease처럼 반의어 짝이 분명한 단어는 바로 뒤 문장과 맞춰 보세요. 여기서는 <b>very little space</b>가 결정적 단서입니다. 앞 문장의 diminished emphasis on dialogue도 같은 방향을 가리킵니다.</div>'''

S['42'] = '<h2>42번 · 장문 어휘 [3점] (41번 제목 포함)</h2>\n' + img('41-42', '41~42번') + '''<h3>① 지문 구조</h3>
<p><b>현상</b> 유리 구조는 분자 수준에서 무작위 원자 볼풀처럼 엉망이다 → 무정형 고체? 과냉각 액체? → 실제로는 고체처럼 행동하며 실온에서 결코 액체처럼 움직이지 않는다 → <b>오해 바로잡기</b> 아래가 두꺼운 옛 스테인드글라스는 흘러내려서가 아니라 처음부터 그렇게 만들어졌다 → <b>역설</b> 가장 오래된 인공 물질인데 과학자들은 아직 유리를 이해하지 못한다 → 유리는 분자 법칙을 (e)___하는 것 같다 → 유리는 물질이 아니라 상태다.</p>
<h3>② 정답: ⑤ (e) obey → defy</h3>
<div class="key"><span class="en">The paradox is that … scientists still struggle to comprehend why glass behaves the way it does. Glass seems to (e) <b>obey</b> most molecular laws.</span><br>과학자들이 이해하지 못하는 '역설'의 이유이므로, 유리가 분자 법칙을 '따른다'면 이해가 쉬웠을 것입니다. 법칙을 '거스른다(defy)'가 맞습니다. 마지막 문장 glass is not a material; it’s a state도 '보통 물질의 규칙에 맞지 않는다'는 방향입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>(a) liquid <span class="x">— 실제로는 고체(the latter)이므로, 실온에서 결코 '액체'처럼 행동하지 않는다. 적절합니다.</span></li>
<li>(b) misshapen <span class="x">— 위보다 아래가 두꺼운 '모양이 일그러진' 유리판. 적절합니다.</span></li>
<li>(c) solidified <span class="x">— 애초에 그렇게 불어서 '굳혀졌기' 때문에 고르지 않다. 적절합니다.</span></li>
<li>(d) paradox <span class="x">— 가장 오래된 인공 물질인데도 아직 이해하지 못한다는 것은 '역설'. 적절합니다.</span></li>
<li class="ans">(e) obey <span class="o">— 정답(부적절).</span> struggle to comprehend의 이유 → defy</li>
</ul>
<h3>④ 41번 제목도 함께</h3>
<div class="key">유리는 고체인지 액체인지 애매하고, 과학자들도 아직 그 작동 방식을 이해하지 못한다 → <b>① Unsolved Mystery Behind the Nature of Glass</b>. ④(왜 고체인데 잘 깨지나)는 글에 없는 '깨짐'을 끌어온 오답이고, ③(스테인드글라스의 문제)은 예시 하나에만 초점을 맞춘 오답입니다.</div>
<div class="tip"><b>장문 어휘 공략법</b> obey/defy, accept/reject처럼 정반대 짝이 있는 동사가 마지막 밑줄로 오면 <b>앞 문장의 핵심어(paradox, struggle to comprehend)</b>와 방향이 맞는지 확인하세요.</div>'''

S['31'] = '<h2>31번 · 빈칸 추론(단어) [2점]</h2>\n' + img(31) + '''<h3>① 빈칸 문장의 역할</h3>
<p>보존(preservation)과 보전(conservation)은 거의 동의어였다 → 보전론자는 <b>복원(restorative)</b>을 강조한다(악기·그림·공룡·생태계 복원) → <b>빈칸 문장</b>: 보전론자는 변화를 인정하지만 그것을 관리해 ______ 상태를 연장하려 한다 → 반면 보존론자는 '발견된 그대로' 두려고 한다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">Conservationists … emphasize conservation’s <b>restorative</b> aspects ― restoring a historical musical instrument … They sometimes criticize conservationists for setting an additional priority on <b>yield or harvest or use</b></span><br>보전론자는 복원하고, 수확·사용 같은 목적까지 고려합니다. 즉 자신들이 '원하는' 상태로 만들어 그 상태를 유지하려는 것이므로 <b>① desired</b>(바람직한)가 정답입니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li class="ans">① desired <span class="o">— 정답.</span> 복원·사용 목적에 맞는 '바람직한' 상태</li>
<li>② unstable <span class="x">— 불안정한 상태를 연장하려는 사람은 없습니다.</span></li>
<li>③ isolated <span class="x">— 고립은 글과 관계없습니다.</span></li>
<li>④ natural <span class="x">— '원래 그대로'를 지키려는 것은 보존론자 쪽입니다. 보전론자는 손을 대서 복원합니다.</span></li>
<li>⑤ delicate <span class="x">— 훼손된(deteriorated) 상태를 떠올리게 하는 함정. 보존론자가 그대로 두려는 상태에 가깝습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">Preservationists would … prefer to keep a historical musical instrument “as found” in a deteriorated state, for study, <b>rather than</b> to restore or repair it for display or use.</span><br>prefer to A rather than (to) B: B하기보다 A하기를 선호하다. 보존론자의 선택(그대로 둠)이 보전론자의 선택(복원)과 대조됩니다.</div>
<div class="tip"><b>빈칸 공략법</b> 두 집단을 비교하는 글에서는 빈칸이 <b>어느 집단의 설명인지</b> 먼저 확인하세요. 빈칸 문장의 주어는 Conservationists(복원파)이므로, 보존론자 쪽 특징인 natural·delicate는 지워집니다.</div>'''

S['32'] = '<h2>32번 · 빈칸 추론(구) [2점]</h2>\n' + img(32) + '''<h3>① 빈칸 문장의 역할</h3>
<p>화자는 중요한 것을 다 말로 하지 않는다 → 목소리·눈 맞춤·표정·몸짓 같은 비언어로 의미를 알 수 있다 → 효과적인 청자는 비언어 해석을 말로 확인한다 → 의미의 절반 이상이 비언어로 전달된다 → 프로이트: 입이 침묵해도 손끝으로 떠들고, 모든 모공에서 누설이 스며 나온다 → <b>빈칸 문장(결론)</b>: 그러니 대면 토론에서 대부분의 사람이 ______하기 어려운 것도 당연하다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">no mortal can <b>keep a secret</b>. If his lips are silent, he chatters with his fingertips; <b>betrayal oozes out</b> of him at every pore.</span><br>비밀을 지킬 수 없다 = 자신이 뜻하고 느끼는 바를 <b>② 숨기기(conceal)</b> 어렵다. No wonder가 바로 앞 인용문의 결론을 이끕니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① pretend to pay attention to others <span class="x">— 남에게 주의를 기울이는 '척'은 글의 초점이 아닙니다.</span></li>
<li class="ans">② conceal what they mean and feel <span class="o">— 정답.</span> keep a secret, betrayal oozes out</li>
<li>③ interpret one’s nonverbal behavior <span class="x">— 글 앞부분 소재(해석)를 이용한 함정. 비언어를 해석하기 '어렵다'가 아니라 감정이 새어 나와 '숨기기' 어렵다는 결론입니다.</span></li>
<li>④ maintain the nonverbal communication <span class="x">— 비언어 소통을 '유지'하는 것은 어려운 일이 아닙니다. 오히려 저절로 일어납니다.</span></li>
<li>⑤ encounter a chance to understand others <span class="x">— 대면 토론은 오히려 남을 이해할 기회가 많은 상황입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en"><b>If</b>, as nonverbal research indicates, more than half of a speaker’s meaning <b>is conveyed</b> nonverbally, we <b>are missing</b> a lot of important information <b>if</b> we fail to “listen” to nonverbal behavior.</span><br>조건절 안에 as 삽입절(연구가 보여 주듯)이 들어갔습니다. 삽입을 괄호로 묶으면 If 주어 + is conveyed 구조가 드러납니다.</div>
<div class="tip"><b>빈칸 공략법</b> <b>No wonder</b>(~하는 것도 당연하다)로 시작하는 빈칸 문장은 바로 앞 문장(인용문)의 결론입니다. 인용문의 핵심어 keep a secret을 다른 말로 바꾼 선택지(conceal)를 찾으세요.</div>'''

S['33'] = '<h2>33번 · 빈칸 추론(구) [3점]</h2>\n' + img(33) + '''<h3>① 빈칸 문장의 역할</h3>
<p>지각이 대상을 분별하지 못할 때(감정·질병·수면) 상상력이 작동한다 → 감정은 세상을 왜곡해서 보게 한다(겁쟁이는 두려움, 연인은 욕망) → 지각한 대상과 기대하는 것의 <b>작은 유사성</b>만으로도 대상을 그것으로 오인한다 → 겁쟁이는 적을, 연인은 욕망의 대상을 어디서나 본다 → <b>빈칸 문장</b>: 더 많이 영향받을수록 ______ → 감정적 몰입이 클수록 지각은 더 편향된다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">a <b>small similarity</b> between a perceived object and the thing one expects to see can lead to the misidentification … <b>The greater the emotional investment, the more biased one’s perception.</b></span><br>감정이 강할수록 '아주 작은 유사성'만 있어도 그 대상이 보입니다. 즉 그것이 나타나는 데 필요한 유사성이 <b>② 더 적어진다</b>. 빈칸 문장과 마지막 문장이 같은 the 비교급 구조로 짝을 이룹니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① 차이를 찾을 기회가 더 많아진다 <span class="x">— 정반대입니다. 감정은 차이를 무시하고 유사성에 끌리게 만듭니다.</span></li>
<li class="ans">② 그것이 나타나는 데 필요한 유사성이 더 적어진다 <span class="o">— 정답.</span> small similarity → misidentification</li>
<li>③ 지각된 유사성이 더 빨리 사라진다 <span class="x">— 유사성이 사라지는 것이 아니라 더 쉽게 느껴집니다.</span></li>
<li>④ 세상을 있는 그대로 더 쉽게 감지한다 <span class="x">— distorted, biased와 정반대입니다.</span></li>
<li>⑤ 다른 감정들이 덜 느리게 방출된다 <span class="x">— 감정의 방출 속도는 글과 관계없습니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en"><b>The more</b> affected one is, <b>the less</b> similarity is required for the thing to appear.</span><br>the 비교급 + 주어 + 동사, the 비교급 + 주어 + 동사: '~할수록 더 …하다'. for the thing은 to appear의 의미상 주어입니다.</div>
<div class="tip"><b>빈칸 공략법</b> 빈칸이 <b>the 비교급, the 비교급</b> 구조의 뒷부분이면 앞부분(more affected)과 같은 방향의 결과를 찾으세요. 바로 뒤 문장(The greater …, the more biased …)이 같은 구조로 정답 방향을 확인해 줍니다.</div>'''

S['34'] = '<h2>34번 · 빈칸 추론(절) [3점]</h2>\n' + img(34) + '''<h3>① 빈칸 문장의 역할</h3>
<p>예술적 가치는 의존적이고 변한다는 사실이 오늘날 수집가의 머릿속에서 가장 중요하다 → 작품을 산다 = 미술사의 한 조각을 사는 것, 아니면 아무것도 아님 → 수표에 서명하며 그 작품이 <b>미래에도 의미 있게 남을 것</b>이라는 믿음을 단언한다 → 그러나 역사는 열려 있고, 현재의 합의는 거의 확실히 대체된다 → <b>빈칸 문장(결론)</b>: 그림에 자신을 거는 것은 수집가의 행위이며, 그는 미적 판단뿐 아니라 ______라는 확신을 용기 있게 단언한다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">In signing his check the collector asserts his belief in the <b>future presence</b> of the work as a significant point attained by art as a whole. … This consensus is all but certain to be displaced</span><br>합의는 바뀔 것이 거의 확실한데도 '이 작품이 미래 미술사에 남는다'고 거는 것 = 예술이 어디로 갈지 <b>① 예측할 수 있다</b>는 확신. courageously(용기 있게)라는 말도 불확실한 미래에 거는 행동임을 보여 줍니다.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li class="ans">① he can predict where art is going <span class="o">— 정답.</span> future presence, 대체될 합의에 대한 도전</li>
<li>② the artist behind the work is reliable <span class="x">— 작가의 신뢰성은 나오지 않습니다.</span></li>
<li>③ the art work tells the story of his time <span class="x">— '현재(그의 시대)'가 아니라 '미래'에 남을 가치가 핵심입니다.</span></li>
<li>④ his choice will lead to immediate profits <span class="x">— 시장 가치 언급을 이용한 함정. '즉각적 이익'은 글의 초점(미래의 미술사적 가치)과 다릅니다.</span></li>
<li>⑤ the originality of the work is unshakable <span class="x">— 작품 가치는 의존적이고 변한다(shifting)고 했으므로 '흔들리지 않는다'는 반대입니다.</span></li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">he courageously affirms <b>not only</b> his aesthetic judgment, from whatever source it <b>be</b> derived, <b>but</b> the conviction that …</span><br>not only A but (also) B 구조에 양보절(from whatever source it be derived: 그것이 어디서 비롯되었든)이 끼어 있습니다. be는 가정법 현재(격식체)입니다.</div>
<div class="tip"><b>빈칸 공략법</b> 빈칸이 the conviction that ~(~라는 확신)이면 글 앞에서 수집가가 '믿는다(belief)'고 한 내용을 찾아 같은 말로 바꾸세요. belief in the future presence ↔ predict where art is going.</div>'''

S['36'] = '<h2>36번 · 글의 순서 [2점]</h2>\n' + img(36) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">식물의 방어는 다양하다. <b>Some</b> load their tissues with harsh compounds(화학적 방어)</td><td class="l">→ Some 다음 다른 종류의 방어가 이어질 차례</td></tr>
<tr><td>(C)</td><td class="l"><b>Structural defenses</b> like thick coats of wax … <b>Nor</b> are individual plants entirely on their own</td><td class="l">화학 → 구조적 방어로 확장, 끝에서 '혼자가 아니다' 예고 → 주어진 글 바로 뒤</td></tr>
<tr><td>(B)</td><td class="l">Plants can release chemical compounds that let their <b>same-species neighbors</b> know …</td><td class="l">(C) 끝의 '혼자가 아니다'를 구체화(이웃·포식자의 도움) → (C) 뒤</td></tr>
<tr><td>(A)</td><td class="l"><b>The back-and-forth</b> is not a matter of natural balance …</td><td class="l">식물 방어와 곤충의 대응 전체를 묶어 정리 → 맨 끝</td></tr>
</table>
<h3>② 정답: ⑤ (C)-(B)-(A)</h3>
<div class="key">화학적 방어 → (C) 구조적 방어, 그리고 식물은 혼자가 아니다 → (B) 같은 종 이웃에게 신호, 곤충 포식자까지 불러들인다 → (A) 이런 주고받기는 균형이 아니라 길게 이어지는 진화적 대화다.</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— The back-and-forth(주고받기)는 여러 방어 방식이 다 나온 뒤에야 묶어 말할 수 있습니다.</span></li>
<li>(B)로 시작(②, ③) <span class="x">— 이웃에게 신호를 보내는 이야기는 (C)의 Nor are individual plants entirely on their own이 먼저 나와야 자연스럽습니다.</span></li>
<li>(C)-(A)-(B)(④) <span class="x">— (A)에서 결론(진화적 대화)을 내린 뒤 다시 구체적 방어 사례(B)로 돌아가면 흐름이 끊깁니다.</span></li>
</ul>
<div class="tip"><b>순서 공략법</b> 단락 끝의 <b>예고 문장</b>(Nor are individual plants entirely on their own)이 다음 단락의 주제가 됩니다. 그리고 The back-and-forth, This process처럼 앞 내용 전체를 묶는 말은 대개 마지막 단락입니다.</div>'''

S['37'] = '<h2>37번 · 글의 순서 [3점]</h2>\n' + img(37) + '''<h3>① 단서 정리</h3>
<table>
<tr><th>단락</th><th>첫머리 단서</th><th>무엇을 받나</th></tr>
<tr><td>주어진 글</td><td class="l">스펙터클은 주로 <b>문화적 틀</b> 안에서 작동한다</td><td class="l">→ 이 말의 의미를 풀어 줄 차례</td></tr>
<tr><td>(C)</td><td class="l"><b>In saying that</b>, we stress that … 스펙터클 창조는 문학 창작처럼 규칙을 따르면서도 독창성이 필요하다</td><td class="l">that = 주어진 글의 '문화적 틀' → 주어진 글 바로 뒤</td></tr>
<tr><td>(A)</td><td class="l"><b>By extension</b>, 혁신과 기존 것을 섞어 문화의 결에 맞춘다 … but <b>imitation is not enough</b></td><td class="l">(C)의 '규칙 + 독창성'을 확장 → (C) 뒤</td></tr>
<tr><td>(B)</td><td class="l">Spectacle must <b>also</b> be spectacular … outdoing previous efforts</td><td class="l">(A) 끝 '모방만으론 부족'에 '또한 놀라워야' 추가 → 맨 끝</td></tr>
</table>
<h3>② 정답: ④ (C)-(A)-(B)</h3>
<div class="key">스펙터클은 문화적 틀 안에서 작동 → (C) 그렇다고 보편적 표현은 아니고, 문학처럼 전통에 묶이면서도 독창성이 필요한 전략 → (A) 더 나아가 기존 것과 혁신을 섞어 만든다, 모방만으론 부족 → (B) 스펙터클은 또한 장관이어야 한다(이전 것을 능가해야).</div>
<h3>③ 오답 순서가 안 되는 이유</h3>
<ul class="ch">
<li>(A)로 시작(①) <span class="x">— By extension(더 나아가)은 확장할 앞 내용이 필요합니다. 주어진 글만으로는 '혁신과 기존 것의 혼합'으로 바로 넘어갈 근거가 부족합니다.</span></li>
<li>(B)로 시작(②, ③) <span class="x">— also(또한)가 첫 단락에 오면 무엇에 더하는지 알 수 없습니다.</span></li>
<li>(C)-(B)-(A)(⑤) <span class="x">— (B)의 also는 (A) 끝 '모방만으로는 충분하지 않다'에 이어져야 자연스럽습니다.</span></li>
</ul>
<div class="tip"><b>순서 공략법</b> <b>In saying that</b>(그렇게 말할 때)은 바로 앞 문장을 받고, <b>By extension</b>(더 나아가)과 <b>also</b>(또한)는 앞 내용에 무언가를 덧붙입니다. 덧붙이는 연결어는 첫 단락이 될 수 없다는 점만 알아도 선택지가 절반으로 줄어듭니다.</div>'''

S['38'] = '<h2>38번 · 문장 삽입 [2점]</h2>\n' + img(38) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<p><b>To minimize vortex shedding</b>, skyscraper designers do everything in their powers to confuse the wind.<br>→ '와류 흘림을 줄이기 위해' 설계자들이 하는 일 = <b>해결책의 시작</b>입니다. 앞에는 와류 흘림이 왜 위험한지(문제), 뒤에는 구체적인 해결 방법이 와야 합니다.</p>
<h3>② 위치별 점검</h3>
<table>
<tr><th>위치</th><th>앞 / 뒤</th><th>판단</th></tr>
<tr><td>①</td><td class="l">바람이 건물 면에서 분리됨 / 앞뒤 압력 차가 소용돌이를 만든다</td><td class="l">× 현상 설명이 이어지는 중</td></tr>
<tr><td>②</td><td class="l">소용돌이 발생 / 소용돌이가 건물을 밀고 당긴다</td><td class="l">× 아직 문제의 심각성이 다 나오지 않음</td></tr>
<tr><td>③</td><td class="l">앞: 위험할 정도로 지속될 수 있는 빈도로 흔든다(문제) / 뒤: 건물 방향을 바람과 나란히 놓는 것이 도움(해결책)</td><td class="l">○ 문제 → 해결책으로 바뀌는 지점</td></tr>
<tr><td>④·⑤</td><td class="l">모서리 깎기, 모서리 거칠게 하기(likewise로 해결책 나열)</td><td class="l">× 이미 해결책이 진행 중</td></tr>
</table>
<h3>③ 정답: ③</h3>
<div class="key">소용돌이가 건물을 위험하게 흔든다 → <b>[주어진 문장] 와류 흘림을 줄이려고 설계자들은 바람을 혼란시키려 애쓴다</b> → 건물의 긴 면을 탁월풍과 나란히 → 모서리를 깎거나 둥글게(likewise) → 발코니나 계단식 모서리로 거칠게.</div>
<div class="tip"><b>삽입 공략법</b> 주어진 문장이 <b>To + 동사(~하기 위해)</b>로 시작하면 '문제 → 해결' 전환점을 찾으세요. ③ 뒤 문장(can help)부터 해결책이 시작되는데, 무엇을 돕는지 알려 주는 문장이 바로 앞에 빠져 있습니다.</div>'''

S['39'] = '<h2>39번 · 문장 삽입 [3점]</h2>\n' + img(39) + '''<h3>① 주어진 문장 먼저 해부하기</h3>
<p>It was <b>also</b> within the range of reds that they learned early on to diversify the palette …, as <b>the oldest known color terms</b> demonstrate.<br>→ It was ~ that 강조 구문 + also: 붉은색 범위 안에서 한 '또 다른' 일. 앞에는 붉은색으로 한 첫 번째 일이, 뒤에는 color terms(색채 용어)를 받는 말이 와야 합니다.</p>
<h3>② 위치별 점검</h3>
<table>
<tr><th>위치</th><th>앞 / 뒤</th><th>판단</th></tr>
<tr><td>①</td><td class="l">붉은색이 다른 모든 색을 능가했다 / 다른 색들이 없었던 건 아니지만</td><td class="l">× 앞뒤가 바로 이어짐</td></tr>
<tr><td>②</td><td class="l">다른 색은 인정받기까지 오래 기다림 / <b>It was with red that</b> 첫 실험·첫 성공</td><td class="l">× also가 받을 '첫 번째 It was ~ that'이 아직 없음</td></tr>
<tr><td>③</td><td class="l">앞: <b>It was with red that</b> humans did their first color experiments / 뒤: <b>Here the lexicon</b> seems in keeping with …</td><td class="l">○ 같은 강조 구문 + also, color terms ↔ the lexicon</td></tr>
<tr><td>④·⑤</td><td class="l">'붉은'이 '색칠된', '아름다운'과 같은 단어인 언어 사례</td><td class="l">× 어휘 사례가 이어지는 중</td></tr>
</table>
<h3>③ 정답: ③</h3>
<div class="key">인간이 첫 색채 실험을 한 것은 붉은색으로였다 → <b>[주어진 문장] 팔레트를 다양화하는 법을 배운 것 '역시' 붉은색 범위 안에서였다(가장 오래된 색채 용어가 보여 주듯)</b> → <b>Here</b> the lexicon(여기서 어휘 목록) = 주어진 문장의 색채 용어 → 언어 사례들.</div>
<div class="tip"><b>삽입 공략법</b> 주어진 문장에 <b>also</b>가 있으면 같은 구조의 앞 문장을 찾으세요(It was with red that → It was also within the range of reds that). 그리고 ③ 뒤 Here the lexicon의 Here가 무엇을 가리키는지 원래 글에서 찾을 수 없다는 점이 빈자리의 증거입니다.</div>'''

S['40'] = '<h2>40번 · 요약문 완성 [2점]</h2>\n' + img(40) + '''<h3>① 요약문 구조</h3>
<p>By lowering the cost of pharmaceutical research and development, AI can help reduce the imbalance in investment that has led to the <b>(A)</b> of less profitable diseases, thereby broadening the focus of medical research to include <b>(B)</b> populations.<br>→ AI는 수익성이 덜한 질병의 (A)를 초래한 투자 불균형을 줄여, 의학 연구가 (B)한 인구 집단까지 포함하도록 넓힌다.</p>
<h3>② 정답 근거</h3>
<div class="key"><span class="en">the disease <b>has been neglected</b> compared to First World illnesses … to find cures to traditionally <b>neglected</b> health issues and among traditionally <b>neglected populations</b>.</span><br>(A) 수익성 낮은 질병은 '소홀히 다뤄졌다' = <b>disregard</b>(무시). (B) 비용을 감당할 수 없는, 전통적으로 소외된 인구 집단 = <b>underserved</b>(혜택을 충분히 받지 못하는). 정답은 <b>⑤ disregard …… underserved</b>.</div>
<h3>③ 선택지 전부 분석</h3>
<ul class="ch">
<li>① prevention …… marginalized <span class="x">— (B)는 맞지만, 불균형이 질병의 '예방'을 초래했다는 것은 반대 방향입니다.</span></li>
<li>② spread …… general <span class="x">— 질병의 '확산'도, '일반' 인구도 글의 초점(소외)과 맞지 않습니다.</span></li>
<li>③ overlook …… native <span class="x">— overlook은 뜻은 비슷하지만 동사라 the ___ of 자리에 맞지 않고, native(원주민의)는 글과 무관합니다.</span></li>
<li>④ ignorance …… wealthy <span class="x">— (B) wealthy는 정반대입니다. 제약 산업은 원래 부유층에 집중했습니다.</span></li>
<li class="ans">⑤ disregard …… underserved <span class="o">— 정답.</span> neglected ↔ disregard, neglected populations ↔ underserved</li>
</ul>
<h3>④ 핵심 구문</h3>
<div class="key"><span class="en">The definition of rare has too often been associated with poor ― that is, <b>even if</b> a disease is quite prevalent in a population that cannot afford to pay for it …, the disease has been neglected</span><br>that is(즉)로 앞 문장을 풀어 말하고, even if(비록 ~일지라도) 양보절이 이어집니다. '희귀하다'는 말이 실은 '가난한 사람들의 병'이라는 뜻으로 쓰였다는 필자의 비판이 담긴 문장입니다.</div>
<div class="tip"><b>요약문 공략법</b> 본문에서 <b>반복되는 단어(neglected ×3)</b>가 요약문에서 다른 말로 바뀝니다. 그리고 (B)처럼 사람을 꾸미는 형용사 자리에는 wealthy ↔ underserved처럼 정반대 선택지가 꼭 섞여 있으니 방향을 먼저 정하세요.</div>'''

json.dump(S, open('secs_06g3.json', 'w'), ensure_ascii=False)
print(len(S))
