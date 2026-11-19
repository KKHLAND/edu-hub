import json, re
L = open('/home/claude/sn/hs.txt', encoding='utf8').read().split('\n')
IMG = 'https://cdn.jsdelivr.net/gh/KKHLAND/edu-hub@{REF}/blog-assets/suneung2027/'

def block(n):
    s = L.index(n); e = len(L)
    for i in range(s + 1, len(L)):
        if re.fullmatch(r'\d\d(~\d\d)?', L[i]): e = i; break
    return L[s:e]

def hv(n):
    b = block(n)
    ko, vo, mode = [], [], None
    for x in b:
        if x == '해석': mode = 'k'; continue
        if x.startswith('어휘'): mode = 'v'; continue
        if '정답' in x and len(x) < 14: mode = None; continue
        if mode == 'k': ko.append(x)
        elif mode == 'v' and x.startswith('□'): vo.append(x[1:].strip())
    return ' '.join(ko), vo

D = {
'21': dict(t='함축 의미 추론', pt='3점', a='②',
 st='<b>과거</b> 데이터 = 밀봉된 상자(가치·통제력·경쟁 우위) → <b>전환</b> 지능 시대에는 그 논리가 장애물 → <b>핵심</b> 가치는 정보를 \'보유\'하는 데서가 아니라 \'연결\'하는 데서 → <b>밑줄</b> 상자를 붙들고 있는 것 = 닻을 끌고 가는 것 → <b>결론</b> 앞서가는 기업은 필요한 만큼만, 목적을 갖고 연다.',
 key=('But in the Intelligence Age, that logic is becoming an obstacle. … Holding on to the sealed box today is less like safeguarding an asset and more like dragging an anchor.',
      '밑줄은 <b>less like A and more like B</b>의 B 자리입니다. A(자산을 지키는 것)라고 생각했던 \'데이터 움켜쥐기\'가 실제로는 B(배의 속도를 떨어뜨리는 닻)라는 뜻이죠. 바로 앞 문장의 <b>obstacle(장애물)</b>이 같은 말입니다.'),
 ch=[('① 경쟁 우위를 위해 정보 수집에 애쓰는 것', '문제는 \'수집\'이 아니라 \'움켜쥐고 공개하지 않는 것\'입니다. 본문의 competitive advantage를 그대로 가져온 함정입니다.'),
     ('② 데이터를 비공개로 유지함으로써 회사의 발전을 제한하는 것', 'holding on to the sealed box = keeping its data private, anchor = limiting progress. EBS 분석처럼 <b>정답 선지만 본문에 없는 단어(limiting, progress)로 바꿔 썼습니다.</b>'),
     ('③ 회사 내부에서 보호된 정보를 공유하려는 시도', '공유(연결)는 필자가 권하는 방향입니다. 닻은 공유가 아니라 \'보유\'의 결과입니다.'),
     ('④ 데이터 공개로 인해 회사의 이익이 줄어드는 것', '공개가 손해라는 것은 필자의 관점과 정반대입니다.'),
     ('⑤ 회사가 귀중한 데이터를 부적절하게 다루는 것을 막는 것', 'safeguarding an asset 쪽의 의미입니다. 필자가 <b>less like</b>로 밀어낸 쪽을 고르면 틀립니다.')],
 syn=[('Value no longer comes primarily from keeping information <u>but from</u> connecting it', 'no longer A but B: 더 이상 A가 아니라 B — 글의 대조축(보유 ↔ 연결)'),
      ('is <u>less like</u> safeguarding an asset and <u>more like</u> dragging an anchor', 'A라기보다는 B에 가깝다 — 밑줄은 B'),
      ('opening it <u>just enough to</u> allow data to move', '~할 만큼만 (정도) — 무조건 개방이 아님')],
 tip='비유 밑줄은 <b>글의 대조축</b>(보유 vs 연결) 중 어느 쪽인지부터 정하세요. 그다음 선지 중 <b>본문 단어를 많이 빌린 것을 의심</b>하고, 같은 뜻을 다른 말로 바꾼 선지를 찾으면 됩니다.'),
'29': dict(t='어법', pt='2점', a='③',
 st='<b>현상</b> 사람은 객관적 증거 없이 자기 신념과 맞는 생각을 믿는다 → <b>대응</b> 신중한 사고자는 기존 신념을 시험·재검토한다 → <b>효과</b> 성찰적 사고는 증거에 따라 신념을 조정하게 하고, 유혹적인 새 생각에 덜 넘어가게 한다.',
 key=('Therefore, ③ think reflectively about the existing beliefs helps people adjust them …',
      '이 문장의 본동사는 <b>helps</b>입니다. 접속사 없이 동사가 하나 더 있을 수 없으므로 문장의 주어 자리에는 동사원형 think가 아니라 <b>동명사 thinking</b>이 와야 합니다.'),
 ch=[('① largely rely', 'if절의 주어 the assumptions(복수, underlying them은 수식어) → 복수 동사 rely, 부사 largely는 동사 수식. <span class="x">적절</span>'),
     ('② it', 'reexamine의 목적어로 앞의 단수 명사 the idea를 가리킵니다. <span class="x">적절</span>'),
     ('③ think → thinking', '주어 자리 + 본동사 helps 존재 → 동명사 주어가 필요. <b class="o">정답</b>'),
     ('④ what', 'consistent with의 목적어이면서 believed의 목적어가 빠진 불완전한 절을 이끄는 관계대명사. <span class="x">적절</span>'),
     ('⑤ do', 'objectify and test their own beliefs를 대신하는 대동사, 주어 those who는 복수. <span class="x">적절</span>')],
 syn=[('<u>thinking</u> reflectively about the existing beliefs <u>helps</u> people adjust them', '동명사 주어 + 단수 동사, help + 목적어 + 동사원형'),
      ('enables people to become <u>less likely to</u> accept new ideas', 'be less likely to ~: ~할 가능성이 더 낮다'),
      ('those who objectify … think more critically than those who <u>do</u> not', '대동사 do (일반동사구 반복 회피)')],
 tip='어법 문제는 먼저 <b>문장마다 본동사 개수</b>를 세어 보세요. 접속사·관계사 없이 동사 두 개가 보이면 하나는 준동사(to부정사·동명사·분사)여야 합니다.'),
'30': dict(t='문맥상 낱말(어휘)', pt='3점', a='③',
 st='<b>통념</b> 집단이 개인보다 더 지적일 수 있다(개미·벌) → <b>양보</b> 집단에게 물으면 좋은 답을 쉽게 얻을 수 있는 건 사실 → <b>반박</b> 하지만 진짜 전문가가 그 안에 있을 때만 → <b>이유</b> 인간 지능은 더해지지 않는 개인 능력 → <b>정리</b> 집단은 성당 건설·세대 간 협력은 하지만 시·발견·수학은 개인이나 아주 작은 집단이 한다.',
 key=('But this works in a reliable fashion only where some genuine expert happens to be in the crowd. This is because human intelligence is an individual capability that is ③ additive.',
      'This is because 뒤는 바로 앞 문장의 이유입니다. 지능이 \'더해지는(additive)\' 것이라면 사람이 많을수록 똑똑해져 전문가가 없어도 될 것입니다. 전문가가 꼭 있어야 한다는 말과 맞으려면 <b>non-additive(더해지지 않는)</b>가 되어야 합니다.'),
 ch=[('① easily', 'It is certainly true that ~ 양보: 문헌 조사나 철학자에게 묻는 것보다 더 쉽게. <span class="x">적절</span>'),
     ('② reliable', 'only where 전문가가 있을 때만 \'신뢰할 수 있게\' 작동. <span class="x">적절</span>'),
     ('③ additive → non-additive', '앞뒤 논리(전문가 필요, 개인·소집단이 창조)와 반대. <b class="o">정답</b>'),
     ('④ collaboration', '과학 분야를 만들고 유지하는 세대 간 \'협력\' — 집단이 할 수 있는 일의 예. <span class="x">적절</span>'),
     ('⑤ individuals', '결론: 시·발견·수학은 주로 개인이나 아주 작은 집단이 한다. <span class="x">적절</span>')],
 syn=[('<u>It is certainly true that</u> …. <u>But</u> this works …', '양보(물론 ~이다) → 반박(그러나) 구조, 필자의 주장은 But 뒤'),
      ('works in a reliable fashion <u>only where</u> some genuine expert happens to be', 'only where: ~하는 경우에만'),
      ('This is done <u>predominantly by</u> individuals', 'predominantly: 주로')],
 tip='어휘 문제에서 <b>This is because, so, therefore</b>가 붙은 낱말은 앞 문장과의 인과가 맞는지 반드시 확인하세요. 반의어(additive ↔ non-additive)로 바꾼 자리가 정답일 확률이 높습니다.'),
'31': dict(t='빈칸(단어)', pt='2점', a='①',
 st='<b>주제</b> 제어 장치가 실수로 작동되는 것을 줄이는 방법 → <b>나열</b> 멀리 두기, 저항 높이기, 오목하게·장벽 뒤에, 덮개·잠금 → <b>공통점</b> 조작이 어려워지고 여러 단계의 행동이 생긴다 → <b>심화</b> 단계마다 \'결정\'도 거쳐야 한다 → <b>빈칸</b> 각 지점이 선택을 ___할 기회가 된다.',
 key=('the operator must go through a sequence not only of actions, but also of decisions to make each action. Each point in the activation process then provides an opportunity for the operator to ______ his or her choice',
      '단계마다 \'결정\'을 다시 해야 한다 → 작동하려던 선택을 <b>다시 생각해 볼(reconsider)</b> 기회. 글 전체 목적인 \'우발적 작동 방지\'와도 딱 맞습니다.'),
 ch=[('① reconsider (재고하다)', '각 단계의 결정 = 다시 생각할 기회. <b class="o">정답</b>'),
     ('② accelerate (가속하다)', '모든 방법이 작동을 <b>느리고 어렵게</b> 만드는 것이므로 정반대.'),
     ('③ generalize (일반화하다)', '선택을 일반화한다는 내용은 없습니다.'),
     ('④ verbalize (말로 표현하다)', '\'안전 확인 구호\' 같은 배경지식을 자극하는 함정. 본문 근거 없음.'),
     ('⑤ document (기록하다)', '작동 기록에 관한 언급 없음.')],
 syn=[('<u>not only</u> make the control harder to operate, <u>but</u> they create a sequence', 'not only A but (also) B'),
      ('a sequence not only of actions, but also of decisions <u>to make each action</u>', 'to부정사의 형용사적 용법'),
      ('Each point … <u>then</u> provides an opportunity', 'then: 그렇다면, 그 결과 — 앞 문장의 결과를 말하는 빈칸')],
 tip='빈칸 문장에 <b>then, thus</b>가 있으면 바로 앞 문장의 핵심어(여기서는 decisions)를 바꿔 말한 표현을 찾으세요.'),
'32': dict(t='빈칸(구)', pt='2점', a='①',
 st='<b>정의</b> VR은 시청자를 3차원 환경에 몰입시킨다 → <b>공통점</b> 영화처럼 기획 가능, 볼 만한 것을 제공 → <b>차이(빈칸)</b> But VR은 ___할 수 없다 → <b>예시</b> 영화는 특정 순간, 정밀한 방식으로 클로즈업을 보여 주지만, VR 시청자는 멀리 있거나 다른 곳을 볼 수도 있다.',
 key=('a movie can choose to show us a close-up detail … at a particular moment and in a precise way … A viewer … could even be looking the other way … at the moment that particular detail emerged.',
      '예시에서 영화만 할 수 있는 것은 <b>\'특정 순간(when)\'</b>에 <b>\'정밀한 방식(how)\'</b>으로 보여 주는 것입니다. 그래서 VR이 못 하는 것은 <b>언제, 어떻게 보는지를 정확히 통제하는 것</b>입니다.'),
 ch=[('① 우리가 그것들을 언제, 어떻게 보는지 정확히 통제하다', 'at a particular moment ↔ when, in a precise way ↔ how. <b class="o">정답</b>'),
     ('② 우리가 경험하는 전체적인 분위기를 전달하다', '360도로 둘러싸는 VR은 오히려 분위기 전달에 강합니다.'),
     ('③ 자연 경관의 수정된 세부를 제공하다', '자연 경관 이야기는 없습니다.'),
     ('④ 시청자가 감정을 경험하는 방식을 반영하다', '본문의 emotional response를 빌린 함정. 핵심은 \'보여 주는 통제\'입니다.'),
     ('⑤ 다감각 효과에서 영화를 능가하다', '비교 방향도 내용도 무관합니다.')],
 syn=[('makes it appear <u>as if</u> she is surrounded by', 'make it appear as if ~: 마치 ~인 것처럼 보이게 하다'),
      ('<u>Like a movie</u>, a VR experience can be curated …. <u>But</u> virtual reality cannot ___', '공통점 → But → 차이점: 빈칸은 차이점'),
      ('would <u>not necessarily</u> be close enough to see the detail', '부분 부정: 반드시 ~한 것은 아니다')],
 tip='\'A도 B처럼 ~할 수 있다. 하지만 A는 ___ 못 한다\'는 구조라면, 뒤에 나오는 <b>예시 속 B만의 장점</b>이 빈칸입니다.'),
'33': dict(t='빈칸(구)', pt='3점', a='⑤',
 st='<b>원리</b> 무엇을 배워야 하는지는 문화마다 다르다(문화의 함수) → <b>숨은 귀결(빈칸)</b> 눈에 띄는 문화 차이가 존재하려면 각 사회 안에는 ___이 있어야 한다 → <b>함의</b> 그러니 \'무엇을 배울지는 개인 혼자 결정할 문제\'라고 말할 수 없다 → <b>근거</b> 어떤 사회도 개인에게 아무거나 배울 권리를 주지 않으며, 공동체가 학교를 세워 알아야 할 것을 배우게 한다.',
 key=('And this prevents us from going on to assert that what a man should learn is a matter for him alone to decide. There is, in fact, no human society … which grants to any individual the right to learn anything he chooses.',
      '사회와 사회 사이에 차이가 뚜렷하려면, 한 사회 <b>안</b>은 비슷해야 합니다. 빈칸 뒤 this가 \'개인 마음대로 결정할 수 없다\'로 이어지므로 빈칸은 <b>규범에 대한 상당한 정도의 순응(conformity to norm)</b>입니다.'),
 ch=[('① 외부 문화의 영향에 저항하는 역동적 과정', '\'사회 내부의 동질성\'이 아니라 외부와의 관계를 말하는 함정입니다.'),
     ('② 무엇을 배울지 선택할 개인의 권리에 대한 믿음', '본문(no society grants the right)과 정반대입니다.'),
     ('③ 다문화적 관점의 광범위한 수용', '사회 내부 동질성과 반대 방향입니다.'),
     ('④ 개인의 다양성에 대한 관용 강조', '개인 자유를 막는다는 흐름과 정반대입니다.'),
     ('⑤ 규범에 대한 상당한 정도의 순응', '사회 간 차이 ↔ 사회 내 동질성, 개인 선택 불가. <b class="o">정답</b>')],
 syn=[('<u>concealed behind this principle lies</u> a corollary', '도치: 장소 부사구 + 동사 + 주어 (a corollary lies concealed behind …)'),
      ('<u>in order that</u> noticeable cultural differences <u>shall</u> exist at all', 'in order that ~ shall: ~하기 위해서(목적), at all: 도대체, 조금이라도'),
      ('<u>it is</u> the school which is established by the community <u>…</u> <u>to ensure</u>', 'It is ~ which 강조 구문 + 삽입구 not, be it noted, by the family')],
 tip='EBS가 꼽은 <b>변별력 문항</b>입니다. 빈칸 바로 뒤의 <b>this</b>가 빈칸 내용을 받는다는 점을 놓치지 마세요. \'this가 무엇을 막는가\'를 보면 빈칸의 방향(개인 자유 ↔ 집단 순응)이 정해집니다.'),
'34': dict(t='빈칸(구)', pt='3점', a='③',
 st='<b>도입</b> 화가가 음악 개념 \'리듬\'을 빌리는 것은 회화가 한계를 넘으려는 신호 → <b>개념 1</b> 공간 예술의 기본 개념은 구도(부분의 크기·모양·색·밝기의 비례 배열) → <b>개념 2</b> 리듬 = 구도 + 소리의 지속 시간 속 규칙적 반복 패턴 → <b>결론(빈칸)</b> 공간 속 구도가 ___의 형태를 띠면 구도는 리듬이 된다.',
 key=('rhythm implies composition, but it adds to it a regularly reoccurring pattern in the duration of sounds. This is to say that, as soon as pictorial composition in space assumes the form of ______, composition becomes for us a rhythm.',
      '구도가 리듬이 되려면 리듬만의 추가 요소, 즉 <b>\'시간 속에서 반복되는 패턴\'</b>이 더해져야 합니다. 그래서 <b>시간 속에서 연속적으로 지각되는 선과 색의 패턴</b>이 정답입니다.'),
 ch=[('① 그림의 다양한 요소를 나타내는 섬세한 기호', '\'시간\' 요소가 없습니다.'),
     ('② 화가의 캔버스 위 다양한 모양과 색의 분포', '<b>가장 매력적인 오답</b>입니다. 이것은 그냥 \'구도\'의 정의일 뿐, 리듬이 더하는 시간 요소가 빠져 있습니다.'),
     ('③ 시간 속에서 연속적으로 지각되는 선과 색의 패턴', 'duration ↔ in time, reoccurring pattern ↔ patterns successively perceived. <b class="o">정답</b>'),
     ('④ 빛과 그림자의 능숙하고 조화로운 배열', '구도 정의(밝기 luminosity)를 재활용한 함정.'),
     ('⑤ 공간 예술과 시간 예술의 반복적 아이디어 짝짓기', 'spatial·temporal을 섞어 그럴듯하게 만든 함정. \'아이디어의 짝\'은 본문에 없습니다.')],
 syn=[('<u>Nor are painters themselves unaware</u> of the fact.', 'Nor + 도치: 화가들도 그 사실을 모르지 않는다(=안다)'),
      ('To compose is to arrange … <u>in such a way that</u> the proportions … are pleasing to perceive', 'in such a way that: ~하는 방식으로'),
      ('<u>as soon as</u> pictorial composition … <u>assumes the form of</u>', '~하자마자 / ~의 형태를 띠다')],
 tip='EBS가 꼽은 <b>변별력 문항</b>입니다. A(구도)와 B(리듬)를 비교하는 글에서는 <b>\'B = A + 추가 요소\'</b>를 찾으세요. A만 말하는 선지(②④)는 소거됩니다.'),
'36': dict(t='글의 순서', pt='2점', a='②', tbl=True,
 st='<b>주어진 글</b> 곤충이 먹이 사슬에서 사라지면 야생 동물에게만 재앙인 것이 아니다 → <b>(B)</b> 인간의 식량에도 직접 영향, 유럽·북미인은 곤충 먹기를 혐오 → <b>(A)</b> 하지만 세계적으로는 곤충 섭취가 일반적(80%) → <b>(C)</b> 약 2,000종, 모파니 애벌레 예시.',
 key=('The loss of insect life … would not just be disastrous for wildlife. → (B) It would also have direct consequences for the human food supply.',
      '<b>not just ~ → also</b>가 가장 강한 연결 고리입니다. (B)의 Europeans and North Americans are disgusted ↔ (A)의 Globally, however, … the norm이 대조로 이어지고, (A)의 일반 진술(80%) 뒤에 (C)의 구체적 종·사례가 옵니다.'),
 clues=[('(B) It would also','주어진 글 not just와 짝, It = The loss of insect life','주어진 글 바로 뒤'),
        ('(A) Globally, however','(B)의 유럽·북미의 혐오와 대조','(B) 뒤'),
        ('(C) 2,000 species / To give an example','(A)의 일반 진술을 구체화','(A) 뒤')],
 ch=[('① (A)-(C)-(B)', '(A)의 however가 대조할 대상(유럽·북미의 혐오)이 아직 없습니다.'),
     ('② (B)-(A)-(C)', 'not just → also → however → 예시. <b class="o">정답</b>'),
     ('③ (B)-(C)-(A)', '구체적 예시(C)가 일반 진술(A)보다 먼저 와서 흐름이 거꾸로입니다.'),
     ('④ (C)-(A)-(B)', '야생 동물 이야기 직후 2,000종 섭취가 나올 연결 고리가 없습니다.'),
     ('⑤ (C)-(B)-(A)', '④와 같은 이유로 (C)로 시작할 수 없습니다.')],
 syn=[('would <u>not just</u> be disastrous …. It would <u>also</u> have …', 'not just A … also B'),
      ('<u>which is odd, since</u> they consume prawns', '계속적 용법 which(앞 절 전체) + 이유 since'),
      ('with the practice very common in South America', 'with + 명사 + 형용사: 부대상황')],
 tip='순서 문제는 <b>주어진 글의 마지막 표현과 짝을 이루는 연결어</b>(not just ↔ also)부터 찾고, <b>일반 → 구체(예시)</b> 원칙으로 나머지를 정리하세요.'),
'37': dict(t='글의 순서', pt='3점', a='④', tbl=True,
 st='<b>주어진 글</b> 박물관의 기원은 부유층·특권층의 수집품 → <b>(C)</b> 역사적으로 수집품은 수집가의 부와 인지적 힘을 보여 줌, 르네상스: 우주의 비밀(보이는 것과 보이지 않는 것의 매개) → <b>(A)</b> 수집품은 소유자가 이 숨겨진 의미의 영역에 접근함을 보여 줌, 외부인은 열등한 위치 → <b>(B)</b> 근대 초기 박물관으로 진화해도 지식·소유와 정체성·권력·지위의 관계를 표현한다는 본질은 그대로.',
 key=('(C) … the collector’s access to the secrets of the universe contained in those objects, which mediated between the visible and the invisible … → (A) The collection indexed its proprietor’s access to this domain of hidden meaning',
      '(A)의 <b>this domain of hidden meaning</b>은 (C)의 <b>secrets of the universe / the invisible</b>을 받습니다. 그리고 (B)는 Renaissance → early modern period → remain으로 시간이 이어지는 <b>결론</b>입니다.'),
 clues=[('(C) Historically, they','they = 주어진 글의 collections','주어진 글 바로 뒤'),
        ('(A) this domain of hidden meaning','(C)의 secrets / the invisible을 받음','(C) 뒤'),
        ('(B) Although … early modern period … remain','르네상스 이후로 시간 이동 + 본질 유지(결론)','맨 마지막')],
 ch=[('① (A)-(C)-(B)', '(A)의 this domain이 가리킬 대상이 없습니다.'),
     ('② (B)-(A)-(C)', '결론인 (B)가 먼저 오면 Historically로 시간이 되돌아갑니다.'),
     ('③ (B)-(C)-(A)', '②와 같은 이유입니다.'),
     ('④ (C)-(A)-(B)', '지시어 연결 + 시간 흐름 모두 자연스럽습니다. <b class="o">정답</b>'),
     ('⑤ (C)-(B)-(A)', '(B)에서 근대로 넘어간 뒤 (A)에서 다시 과거 수집가 이야기로 돌아가 흐름이 끊깁니다.')],
 syn=[('displayed the wealth of the collector, <u>but also</u> his cognitive power', '(not only) A but also B'),
      ('those objects, <u>which mediated between</u> the visible and the invisible', 'mediate between A and B: A와 B 사이를 매개하다'),
      ('<u>Paying their respects</u> to the collection, they acknowledged', '분사구문: ~하면서, ~함으로써')],
 tip='<b>this + 추상 명사</b>(this domain)는 앞 단락의 구체적 내용을 요약해 받습니다. 그리고 Although로 시작하며 \'그럼에도 본질은 그대로\'라고 말하는 단락은 대개 <b>마지막</b>입니다.'),
'38': dict(t='문장 삽입', pt='2점', a='③', tbl=True,
 st='<b>도입</b> 수면은 더 시급한 다른 욕구를 방해한다 → <b>인용</b> 필수 기능이 없다면 진화의 가장 큰 실수 → <b>미스터리</b> 그 기능은 아직 모른다 → <b>[주어진 문장]</b> 그냥 몸이 쉬는 시간이라고 하면 좋겠지만 그것도 맞지 않다 → <b>근거</b> 해먹에서 종일 쉬어도 20시간 후엔 잠을 자야 한다 → <b>보충</b> 깨어 있는 2시간당 1시간 수면, 수면 부채.',
 key=('That function is still a mystery. ( ③ ) You can relax in a hammock on a beach all day long if you want to, but after about twenty hours you will be in pretty bad shape',
      '③ 뒤의 해먹 이야기는 <b>\'쉬는 것만으로는 수면을 대신할 수 없다\'</b>는 근거입니다. 그런데 ③ 앞에는 \'휴식\'이라는 말이 없죠. 주어진 문장(수면 = 휴식이라고 하면 좋겠지만 그것도 아니다)이 들어가야 앞(기능은 미스터리)과 뒤(휴식 ≠ 수면)가 이어집니다.'),
 clues=[('주어진 문장 either','앞에 \'답을 모른다\'는 부정적 진술 필요 → That function is still a mystery','② 뒤'),
        ('주어진 문장 a body rests','③ 뒤 hammock(휴식) 사례의 도입','③ 앞'),
        ('② That function','앞의 a vital function을 바로 받으므로 끊으면 안 됨','①②는 불가')],
 ch=[('①', '수면이 다른 욕구를 방해한다 → 그래서 생물학자의 인용. 자연스럽습니다.'),
     ('②', 'That function이 앞 문장의 vital function을 받으므로 사이에 넣을 수 없습니다.'),
     ('③', '미스터리 → (휴식이라 하면 좋겠지만 아니다) → 해먹 사례. <b class="o">정답</b>'),
     ('④', '해먹 사례 → 2시간당 1시간 비율. 자연스럽습니다.'),
     ('⑤', '비율이 깨지면 안다 → 수면 부채로 보충. 자연스럽습니다.')],
 syn=[('It would be nice to say that …, but that wouldn’t be quite right <u>either</u>', '부정문 + either: ~도 역시 아니다'),
      ('<u>so</u> important, <u>yet so</u> poorly understood, <u>that</u> it led one biologist to say', 'so ~ that 구문'),
      ('<u>Each hour of</u> missed sleep one night <u>will result in</u> deeper sleep the next', 'result in: ~을 초래하다')],
 tip='삽입 문제는 <b>앞뒤를 바로 붙였을 때 논리가 비는 곳</b>을 찾으세요. 사례(해먹)가 나오는데 그 사례가 설명할 주장(휴식 ≠ 수면)이 없다면, 그 앞이 삽입 자리입니다.'),
'39': dict(t='문장 삽입', pt='3점', a='④', tbl=True,
 st='<b>배경</b> 경쟁 심화 → 공격적인 혁신 전략 → <b>혁신의 효과</b> 차별화와 일시적 독점으로 이윤 → <b>다른 수단</b> 시장 경제에서 살아남는 다른 방법들 → 지리적 거리·운송비, 소비자의 비교 능력 한계, 규제 → <b>[주어진 문장]</b> 이 모든 기제가 경쟁을 줄이고, 최고 제품·최저가가 아니어도 살아남게 한다 → <b>반전</b> However, 세계화·규제 완화·반독점 정책이 이 수단들을 약화 → <b>결론</b> 혁신만이 유일한 생존 방법.',
 key=('These conventional means rely mainly on geographical distances …, the limited capacity of consumers …, and the existence of regulated activities. ( ④ ) However, globalization, deregulation, and some antitrust policies … weaken the effectiveness of those conventional means.',
      '주어진 문장의 <b>All these mechanisms</b>는 세 가지가 \'나열된 뒤\'에야 쓸 수 있습니다. 또 \'경쟁을 줄여 살아남게 해 준다\'는 긍정적 효과가 먼저 나와야 <b>However, … weaken</b>(그러나 이것들이 약해진다)으로 반전할 수 있습니다.'),
 clues=[('All these mechanisms','③ 뒤 문장의 세 가지 수단(거리·소비자 한계·규제) 나열을 받음','③ 뒤 문장 다음'),
        ('reduce competition / survive','\'생존 수단\'의 긍정적 효과','However 앞'),
        ('④ 뒤 However … weaken','긍정 효과 → 약화로 반전','④가 경계')],
 ch=[('①', '혁신 설명 중간입니다. mechanisms로 받을 나열이 없습니다.'),
     ('②', '혁신(독점·이윤) 설명 직후라 \'최고 제품이 아니어도 살아남는다\'는 말과 충돌합니다.'),
     ('③', 'other means만 언급됐을 뿐 구체적 나열 전이라 All these mechanisms가 받을 대상이 없습니다.'),
     ('④', '나열 → 이 모든 기제의 효과 → However 약화. <b class="o">정답</b>'),
     ('⑤', '이미 However로 약화를 말한 뒤 다시 \'살아남게 해 준다\'는 긍정이 오면 역행합니다.')],
 syn=[('one way of getting out of the competition, <u>which is to say</u> situations in which …', 'which is to say: 다시 말해'),
      ('to set oneself apart and temporarily to assume a monopoly position', 'set oneself apart: 차별화하다, assume: (지위를) 차지하다'),
      ('allow companies to survive <u>even if</u> they do not have the best product', 'allow + 목적어 + to부정사, even if 양보')],
 tip='EBS가 꼽은 <b>변별력 문항</b>입니다. 주어진 문장에 <b>All these + 명사</b>가 있으면 \'나열이 끝난 지점\'을 찾고, 그 뒤에 <b>However</b> 같은 반전이 이어지는지 확인하세요.'),
'40': dict(t='요약문 완성', pt='2점', a='②',
 st='<b>통념 부정</b> 광고의 역할은 매출을 직접 늘리는 것이 아니다 → <b>질문</b> 그럼 목적은? → <b>답</b> 브랜드에 대한 소비자의 태도를 개선해 장기 매출로 → <b>작동 방식</b> 기대를 만들어 탐색적 구매(시험 구매) 가능성을 높이고, 경쟁 제품 대비 느낌에 영향.',
 key=('its value lies in improving the consumer’s attitude towards brands, thus leading to long-term sales … it does increase the likelihood of a consumer making an exploratory purchase of the brand',
      '(A) improving the attitude → <b>cultivate</b>(기르다, 함양하다), (B) exploratory purchase(시험 삼아 사 보기) → <b>trials</b>(시도, 시험 사용). expectations는 요약문에 이미 있으므로 짝이 되는 trials를 고르면 됩니다.'),
 ch=[('① criticise / understandings', '광고가 태도를 \'비판\'한다는 것은 반대입니다.'),
     ('② cultivate / trials', 'improving ↔ cultivate, exploratory purchase ↔ trials. <b class="o">정답</b>'),
     ('③ reflect / valuations', '광고는 태도를 \'반영\'하는 수동적 역할이 아니라 개선하는 역할입니다.'),
     ('④ manipulate / imitations', '조작·모방은 본문에 없는 부정적 의미입니다.'),
     ('⑤ display / campaigns', '본문의 campaign을 빌린 함정. 태도를 \'보여 준다\'는 말도 맞지 않습니다.')],
 syn=[('What then is the purpose of advertising, <u>if not</u> to directly increase sales?', 'if not ~: ~이 아니라면'),
      ('the real effect of advertising is <u>not</u> at the point of sale <u>but</u> at the point of consumption', 'not A but B'),
      ('increase the likelihood of <u>a consumer making</u> an exploratory purchase', '동명사의 의미상 주어(a consumer)')],
 tip='요약문은 본문의 <b>질문 → 답</b> 구조에서 \'답\' 문장을 찾아 (A), (B)를 각각 바꿔 쓴 말로 연결하세요.'),
'42': dict(t='장문 어휘', pt='3점', a='②', set='41~42',
 st='<b>1단락</b> 지구에 생명이 있으니 지구와 닮은 행성에서 찾는다(지구 중심 탐색) → 이 논리가 \'물을 따라가라\'를 부추기고, 액체 물·대기가 있는 행성 탐색의 기초가 되며, \'항성 거주 가능 영역\' 개념을 (b) ___, 우리와 닮은 생명 찾기와 들어맞는다 → <b>2단락</b> 대안 논리: 지구 생명이 다른 곳의 대표는 아니다 → 우리 눈에 보이는 생명은 지구 생물량의 전형도 아니며, 보이지 않는 미생물이 법칙이고 큰 생물은 예외.',
 key=('It (b) contradicts the concept of the “stellar habitable zone,” which assumes that life is restricted to those planets at just the right distance … It fits perfectly with the search for life in our own image.',
      '1단락의 It(지구 중심 논리)은 fuels(부추기다) → forms the basis(기초가 되다) → fits perfectly(완벽히 들어맞다)처럼 모두 \'지지·연결\'의 방향입니다. \'지구 같은 조건만 생명 가능\'이라는 거주 가능 영역 개념은 지구 중심 논리 그 자체이므로 contradicts가 아니라 <b>supports</b>여야 합니다.'),
 ch=[('① (a) fuels', '지구 중심 논리가 \'물을 따라가라\'를 부추긴다. <span class="x">적절</span>'),
     ('② (b) contradicts → supports', '같은 방향의 나열 속에 혼자 반대 의미. <b class="o">정답</b>'),
     ('③ (c) different', '대안 논리는 \'다른\' 가정에서 출발. <span class="x">적절</span>'),
     ('④ (d) typical', '우리가 보는 생명은 전형조차 아니다(not even typical) → 미생물이 법칙. <span class="x">적절</span>'),
     ('⑤ (e) exceptions', '큰 생물은 눈길을 끄는 \'예외\'일 뿐. <span class="x">적절</span>')],
 syn=[('It fuels … It forms … It supports … It fits', '같은 주어 It의 병렬 — 방향이 같아야 함'),
      ('the conditions … <u>need not be viewed as</u> limitations', 'need not + 동사원형: ~할 필요가 없다'),
      ('the larger organisms that catch our eye simply <u>being</u> the exceptions', 'with + 명사 + 분사: 부대상황'),],
 tip='장문 어휘는 <b>같은 주어가 반복되는 병렬 문장</b>을 묶어 보세요. 방향이 하나만 다르면 그곳이 정답입니다. 41번(제목) 정답은 ① Within or Beyond Earth’s Rules입니다.'),
}

def sec(n, ref):
    d = D[n]; base = IMG.replace('{REF}', ref)
    imgf = 'q41-42.png' if n == '42' else f'q{n}.png'
    ko, vo = hv(d.get('set', n))
    h = [f'<h2>{n}번 · {d["t"]} [{d["pt"]}]</h2>',
         f'<img src="{base}{imgf}" alt="2027학년도 수능 영어 {n}번 {d["t"]} 문제">',
         '<p class="cap">2027학년도 수능 영어 홀수형 문제지 (출처: 한국교육과정평가원)</p>',
         '<h3>① 지문 구조</h3>', f'<p>{d["st"]}</p>',
         '<h3>② 정답 근거</h3>', f'<div class="key"><span class="en">{d["key"][0]}</span><br>→ {d["key"][1]}</div>']
    if d.get('tbl'):
        h.append('<table><tr><th>단서</th><th>연결</th><th>위치</th></tr>' + ''.join(f'<tr><td class="l"><b>{a}</b></td><td class="l">{b}</td><td>{c}</td></tr>' for a, b, c in d['clues']) + '</table>')
    h.append('<h3>③ 선택지 전부 분석</h3><ul class="ch">' + ''.join(
        f'<li{" class=\"ans\"" if c.startswith(d["a"]) or c.startswith(d["a"] + " ") else ""}><b>{c}</b><br>{e}</li>' for c, e in d['ch']) + '</ul>')
    h.append('<h3>④ 핵심 구문</h3><ul>' + ''.join(f'<li><span class="en">{a}</span><br>→ {b}</li>' for a, b in d['syn']) + '</ul>')
    h.append(f'<h3>⑤ 이 유형 공략법</h3><div class="tip">{d["tip"]}</div>')
    if ko:
        h.append(f'<details><summary><b>📖 전체 해석 보기</b></summary><p>{ko}</p></details>')
    if vo:
        h.append('<p class="sm"><b>어휘</b> · ' + ' · '.join(vo) + '</p>')
    return '\n'.join(h)

if __name__ == '__main__':
    import sys
    ref = sys.argv[1] if len(sys.argv) > 1 else 'REF'
    S = {n: sec(n, ref) for n in D}
    json.dump(S, open('secs_sn.json', 'w'), ensure_ascii=False, indent=0)
    for n in D: print(n, len(S[n]), len(hv(D[n].get('set', n))[0]), len(hv(D[n].get('set', n))[1]))
