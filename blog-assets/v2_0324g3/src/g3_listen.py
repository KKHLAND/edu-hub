# 2026 3월 고3 듣기 1~17 — 발문·선택지·해석·어휘 (교사 작성 해석)
import re
Q = {
1: ('다음을 듣고, 남자가 하는 말의 목적으로 가장 적절한 것을 고르시오.', ['체육관 이용 지침 준수를 당부하려고','체육관 운영 시간 변경을 공지하려고','새로운 운동 기구 사용법을 설명하려고','운동 목적에 맞는 의류 착용을 권장하려고','체육관 불편 사항 접수 방법을 안내하려고']),
2: ('대화를 듣고, 여자의 의견으로 가장 적절한 것을 고르시오.', ['교과서의 세부 내용까지 꼼꼼히 공부해야 한다.','복습을 빨리할수록 내용이 기억에 오래 남는다.','수업 중 이해가 되지 않으면 적극적으로 질문해야 한다.','과목별로 다른 공책을 사용하는 것이 효과적이다.','핵심 내용만 선택적으로 필기하는 것이 더 좋다.']),
3: ('다음을 듣고, 남자가 하는 말의 요지로 가장 적절한 것을 고르시오.', ['공상은 창의적이고 혁신적인 사고로 이어질 수 있다.','과학 지식이 뒷받침되어야 창의적인 발명이 가능하다.','집중력을 높이려면 주의를 분산시키는 요소를 줄여야 한다.','공상이 습관이 되면 그것을 스스로 멈추기가 어려워진다.','공상과 현실의 차이가 클수록 실망감이 커진다.']),
4: ('대화를 듣고, 그림에서 대화의 내용과 일치하지 않는 것을 고르시오.', None),
5: ('대화를 듣고, 여자가 할 일로 가장 적절한 것을 고르시오.', ['추가 배터리 준비하기','현수막 설치하기','비디오카메라 가져오기','방문객 좌석 준비하기','퀴즈 우승자 상품 주문하기']),
6: ('대화를 듣고, 남자가 지불할 금액을 고르시오. [3점]', ['$210','$220','$270','$290','$300']),
7: ('대화를 듣고, 여자가 보드게임을 하러 갈 수 없는 이유를 고르시오.', ['아르바이트를 해야 해서','보고서를 마무리해야 해서','건강 검진이 예약되어 있어서','다른 친구의 집들이에 가야 해서','수리 기사의 방문이 예정되어 있어서']),
8: ('대화를 듣고, Night Sea Concert에 관해 언급되지 않은 것을 고르시오.', ['장소','연주자','일시','주차 정보','티켓 가격']),
9: ('2026 Public Speaking Workshop에 관한 다음 내용을 듣고, 일치하지 않는 것을 고르시오.', ['5월부터 6월까지 주말마다 진행된다.','발표 기술에 관한 특강을 포함한다.','참가비는 무료이다.','모든 참가자는 일대일 피드백을 받는다.','마지막 날에 각 참가자는 무대에서 짧은 연설을 한다.']),
10: ('다음 표를 보면서 대화를 듣고, 여자가 구입할 여행용 목베개를 고르시오.', None),
11: ('대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]', ["Hmm. You’re not allowed to charge any electronic device.","Of course. Those seats are on the third floor.","Don’t worry. I’m almost done with my report.","Okay. In that case, let’s find somewhere quiet.","You’re right. I should bring my charger wherever I go."]),
12: ('대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오.', ["Alright. I’ll just use the professional-grade camera I have.","I didn’t know that. Then I’ll definitely give it a go.","Not at all. I don’t have time to take photos.","I’m sorry. The contest is for professionals only.","Hurry. You should submit your photos by tomorrow."]),
13: ('대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오.', ["No problem. I downloaded the same app as you.","Wow. I’m glad that they’ll begin a delivery service.","My goodness! You missed the notification from the app.","Thanks. I truly enjoyed the authentic Mexican dishes.","Exactly. Let’s join the waitlist through the app."]),
14: ('대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오.', ["I agree. Buying a new bag is much cheaper.","Oops! I threw away my old jeans yesterday.","Yes, please. I hope my bag comes out great.","No thanks. I don’t need any more jeans right now.","Guess what? I’ve made this upcycled bag all by myself."]),
15: ('다음 상황 설명을 듣고, Sophia가 James에게 할 말로 가장 적절한 것을 고르시오. [3점]', ["I’d rather stick to our current marketing plan.","Why don’t we collaborate with a famous character?","We should strengthen teamwork within the company.","I doubt character-branded products would be appealing.","How about creating a new flavor for the global market?"]),
}
Q16 = ('여자가 하는 말의 주제로 가장 적절한 것은?', ['reasons artificial materials are losing popularity','new technologies that help create artificial materials','the various artificial alternatives to natural materials','the preference for natural materials to artificial ones','the environmental problems caused by artificial materials'])
Q17 = ('언급된 재료가 아닌 것은?', ['silk','leather','diamond','wood','rubber'])
TABLE10 = '| Model | Price | Cover Material | Customer Ratings | Color |\n| :- | :- | :- | :- | :- |\n| ① A | $31 | Cotton | ★★★★☆ | Gray |\n| ② B | $35 | Cotton | ★★★★★ | White |\n| ③ C | $47 | Silk | ★★★☆☆ | Black |\n| ④ D | $49 | Linen | ★★★☆☆ | Navy |\n| ⑤ E | $56 | Linen | ★★★★☆ | Pink |'

FIX = {'foursession':'four-session','eightsession':'eight-session','oneday':'one-day','eyecatching':'eye-catching','flowerpatterned':'flower-patterned',
       'doublecheck':'double-check','parttime':'part-time','eyecontact':'eye contact','oneonone':'one-on-one','professionalgrade':'professional-grade',
       'stepbystep':'step-by-step','ecofriendly':'eco-friendly','wellknown':'well-known','characterthemed':'character-themed'}
def load_sc(path='listen.md'):
    t = open(path).read()
    for a, b in FIX.items(): t = t.replace(a, b)
    pages = re.split(r'<!-- Page \d+ -->', t)[2:]
    SC = {}
    for pg in pages:
        lines = [l.replace('## ', '').strip() for l in pg.split('\n')]
        lines = [l for l in lines if l and not l.startswith('2026학년도') and not re.match(r'^\d+$', l) and l != '---']
        head = ' '.join(lines[:3])
        m = re.match(r'^(\d+)\.', lines[0]) if lines else None
        if lines and lines[0].startswith('16번부터'): n = 16
        elif m: n = int(m.group(1))
        else: continue
        if n == 17: continue
        body = []
        for l in lines:
            if re.match(r'^(\d+\.|16번부터|\[16|을 고르시오|고르시오|르시오)', l) or '고르시오' in l and not re.match(r'^[MW]:', l): continue
            if re.match(r'^(M|W|Sophia):', l) or not body: body.append(l)
            else: body[-1] += ' ' + l
        SC[n] = '\n'.join(b for b in body if not b.startswith('16. '))
    return SC

KO = {
1: """남: 안녕하세요, 소중한 회원 여러분! 저희 체육관에서 운동해 주셔서 감사합니다. 모든 직원은 모두에게 깨끗하고 안전하며 즐거운 환경을 제공하려고 노력합니다. 그런데 최근 일부 회원들이 체육관 규정을 어긴다는 불만이 접수되었습니다. 기구에 운동 원판이 그대로 남아 있었고, 장비를 사용한 뒤 닦지 않았으며, 실외화를 신은 채 체육관 안에 들어오기도 했습니다. 이런 행동은 다른 사람을 불편하게 하고 모든 회원의 안전을 위협할 수 있습니다. 모두가 안전하고 쾌적하게 운동할 수 있도록 체육관 지침을 지켜 주시기를 부탁드립니다. 감사합니다!""",
2: """남: 안녕하세요, Christine 선생님. 잠깐 시간 괜찮으세요?
여: 물론이지. 무슨 이야기를 하고 싶니?
남: 수업 시간에 필기할 시간을 좀 더 주실 수 있을까 해서요.
여: 네 필기를 한번 볼 수 있을까? 지금도 시간은 충분히 주고 있다고 생각하는데. [잠시 후] 음. 너무 많은 것을 받아 적는 것 같구나.
남: 무슨 말씀이세요?
여: 필기를 할 때는 언급된 모든 것이 아니라 수업에서 중요한 부분만 적는 게 더 좋아.
남: 선생님 말씀을 하나도 놓치면 안 된다고 생각해서 최대한 많이 적었어요.
여: 그러면 무엇이 중요한지 알아내기 어려울 수 있어.
남: 맞아요. 필기를 복습할 때 선생님이 무엇을 가장 강조하셨는지 알기 어려웠어요.
여: 바로 그거야. 핵심 내용만 골라서 필기해 보렴.
남: 그렇게 해 볼게요. 감사합니다.""",
3: """남: 안녕하세요, 열정적인 여러분! The Creativity Channel의 Alex입니다. 오늘은 공상의 힘에 대해 이야기해 봅시다. 많은 사람이 공상을 게으름이나 집중력 부족의 신호라고 생각하지만, 저는 그 생각에 이의를 제기하려고 합니다. 공상은 창의성에 불을 지피고 혁신을 불러일으키는 강력한 도구가 될 수 있습니다. 많은 연구에 따르면 공상과 창의성은 비슷한 정신 과정을 사용합니다. 창의성은 흔히 서로 먼 생각들을 연결해 새로운 것을 만드는 데서 나옵니다. 마찬가지로 우리가 공상할 때는 현재 상황과 관련 없는 우리만의 생각을 만들어 냅니다. 이는 공상 속의 무작위적인 생각이 신선하고 혁신적인 아이디어로 이어질 수 있음을 보여 줍니다. 그러니 다음에 공상에 빠지면, 그것과 싸우지 마세요!""",
4: """남: 안녕, Tina. 지난 주말에 뭐 했어?
여: 하루짜리 베이킹 수업에 갔어. 내가 찍은 이 사진 좀 봐.
남: 와. 벽에 'Baking Class'라고 쓰인 현수막이 있네.
여: 정말 눈에 띄지, 그렇지?
남: 응. 수납장 위에 베이킹 쟁반들도 보여.
여: 응. 학생마다 자기 쟁반을 써서 쿠키를 구웠어.
남: 꽃무늬 셔츠를 입은 사람은 누구야?
여: 강사님이야. 정말 많이 도와주셨어. 강사님 쟁반에 있는 쿠키 보여? 하트 모양으로 만드셨어.
남: 그렇구나. 탁자 위에 있는 상자 두 개는 뭐에 쓰는 거야?
여: 쿠키를 포장하는 상자야. 우리가 구운 쿠키를 거기에 담았어.
남: 좋다. 정말 재미있었겠다. 나도 언젠가 그 수업을 듣고 싶어.""",
5: """여: 안녕, Jake! 내일 로봇 축구 경기 준비 다 됐지?
남: 안녕, Emma! 그런 것 같은데, 혹시 모르니 다시 확인해 보자. 여분 배터리 있어?
여: 완전히 충전된 여분 배터리 두 개가 있어.
남: 좋아. 로봇 축구 미니 퀴즈는?
여: 문제는 다 준비했고, 퀴즈 우승자 상품도 주문해 뒀어.
남: 좋아. 손님 좌석은 내가 벌써 마련했어. 더 필요할 것 같아?
여: 아니, 이 정도면 충분할 것 같아.
남: 그럼 다 준비된 것 같네. 아, 잠깐. 동아리방에 비디오카메라를 두고 왔어.
여: 정말? 경기를 녹화하려면 그게 필요해. 내가 지금 바로 가져올게.
남: 고마워. 네가 그거 하는 동안 나는 입구에 현수막을 설치할게.
여: 좋아! 모든 게 순조롭게 진행되면 좋겠다.""",
6: """남: 안녕하세요, 스쿠버 다이빙 강습을 신청하고 싶어요.
여: 네. 4회 패키지와 8회 패키지가 있습니다. 어느 것으로 하시겠어요?
남: 각각 얼마예요?
여: 4회 패키지는 140달러입니다. 그런데 8회 패키지로 등록하시면 220달러밖에 안 해요.
남: 아, 그럼 8회 패키지로 할게요. 다이빙 장비도 빌려야 해요.
여: 걱정 마세요. 장비 대여는 패키지에 포함되어 있습니다.
남: 잘됐네요! 또 알아야 할 게 있나요?
여: 네, 다이빙 풀 입장료가 있어요. 1회에 10달러인데, 손님은 8회니까 8번 내셔야 해요.
남: 알겠어요. 그리고 이번 달에 신규 회원 할인이 있다고 봤는데요.
여: 맞아요! 처음 오셨으니 10달러 할인해 드릴게요.
남: 좋네요. 지금 결제할게요.""",
7: """남: 안녕, Jenny. 어제 건강 검진은 어땠어?
여: 안녕, Mark. 잘 끝났어. 의사 선생님이 걱정할 게 하나도 없대.
남: 다행이다. 그런데 보드게임 좋아해?
여: 좋아해. 왜?
남: 이번 금요일 오후에 친구들을 우리 집에 불러서 보드게임을 하려고 하거든. 너도 올래?
여: 재미있겠다, 그런데 못 갈 것 같아.
남: 아, 아르바이트 때문이야?
여: 아니, 금요일에는 일 안 해.
남: 그럼 보고서를 끝내야 해?
여: 그건 벌써 끝냈어. 사실 세탁기가 고장 나서 그날 수리 기사님이 고치러 오시기로 했어.
남: 그렇구나. 누군가 집에 있어야 들어오실 수 있겠네.
여: 바로 그거야. 집을 비울 수가 없어. 그래도 다른 친구들이랑 재미있게 놀아!""",
8: """여: 안녕, Sean. Night Sea Concert에 관한 이 안내 책자 봤어?
남: Night Sea Concert? 그게 뭐야?
여: Fintown Ocean Park에서 열리는 콘서트야. 그 공원은 경치로 유명하잖아.
남: 정말? 저녁 바다 풍경에 둘러싸여 아름다운 음악을 들으면 멋지겠다.
여: 그렇지. Henry Solace를 포함해 최고 수준의 음악가들이 공연해. 네가 제일 좋아하는 바이올리니스트잖아.
남: 멋지다! 내 아르바이트랑 겹치지 않으면 좋겠는데.
여: 4월 11일 토요일이고, 저녁 7시에 시작해.
남: 딱 좋아. 티켓 가격을 확인해 보자. [잠시 후] 아, 성인은 20달러, 학생은 10달러야.
여: 응, 적당하네. 같이 갈래?
남: 당연하지! 매진되기 전에 표를 사자.""",
9: """여: 안녕하세요, 학생 여러분. 저는 Bella 주민 센터의 Jamie입니다. 사람들 앞에서 말하는 데 관심이 있다면 2026 Public Speaking Workshop 소식이 반가울 거예요. 워크숍은 5월부터 6월까지 매주 주말에 주민 센터에서 열립니다. 이 프로그램에는 자신 있게 눈을 맞추는 방법 같은 발표 기술에 관한 특강이 포함되어 있습니다. 워크숍 전체가 완전히 무료이므로 대중 연설에 관심 있는 누구나 참여할 수 있습니다. 무엇보다도 개인 맞춤형 지도가 제공됩니다! 먼저 신청한 참가자 10명은 일대일 피드백을 받게 됩니다. 그리고 마지막 날에는 참가자 각자가 무대에서 짧은 연설을 합니다. 망설이지 말고 훌륭한 연설가가 되기 위한 한 걸음을 내디디세요!""",
10: """여: 여보, 여행 때 쓸 목베개를 사고 싶은데. 고르는 것 좀 도와줄래요?
남: 물론이죠. 어떤 것들을 보고 있어요?
여: 이 다섯 개 모델을 생각하고 있어요.
남: 어디 봐요. 예산은 정했어요?
여: 50달러 미만으로 하고 싶어요. 그 이상은 너무 비싼 것 같아요.
남: 동의해요. 그럼 이건 빼면 되겠네요. 커버 소재는 실크가 아닌 걸로 하길 추천해요.
여: 좋은 지적이에요. 실크는 약해서 특별히 관리해야 하니까요.
남: 그렇죠. 고객 평점도 확인해 보는 게 어때요? 별 네 개 이상인 걸 골라야 해요.
여: 물론이죠. 실제 사용자 후기가 중요하니까요. 그리고 흰색은 쉽게 더러워져서 싫어요.
남: 일리 있어요. 그럼 이게 당신한테 딱 맞겠네요.
여: 좋아요. 지금 주문할게요.""",
11: """남: 아, 이런! 노트북 배터리가 거의 다 됐는데 보고서를 아직 못 끝냈어.
여: 꺼지기 전에 충전하는 게 좋겠어. 이 도서관에 충전할 수 있는 자리가 몇 군데 있어.
남: 바로 그게 필요했어! 어디 있는지 알려 줄래?
여: ______________""",
12: """여: David, 나 다음 달 사진 공모전에 신청할 거야. 너도 지원해 보는 게 어때? 너 사진 찍는 거 좋아하잖아.
남: 정말 하고 싶은데, 전문가용 카메라가 없어. 스마트폰밖에 없거든.
여: 그건 문제가 안 돼. 이 공모전에는 스마트폰 사진 부문이 따로 있어.
남: ______________""",
13: """여: 여보, 오늘 저녁에 뭐 먹고 싶어요?
남: 멕시코 음식이 당겨요. 우리 집 근처 멕시코 음식점이 정말 맛있대요.
여: 네, 요즘 정말 인기 많아요. 그 식당은 늘 붐벼요.
남: 으… 그럼 오래 기다려야겠네요. 줄 서는 거 정말 싫은데.
여: 사실 밖에서 길게 줄 서지 않는 방법이 있어요.
남: 정말요? 어떻게요?
여: 이 앱으로 대기 명단에 이름을 올리면 돼요.
남: 앱으로요? 어떻게 하는 거예요?
여: 식당을 고르고 인원수를 입력하면 대기 명단에 올라가요!
남: 그럼 내 차례가 된 건 어떻게 알아요?
여: 앱이 예상 대기 시간을 보여 주고, 차례가 가까워지면 알림을 보내 줘요.
남: 편리하네요. 밖에서 오래 서 있을 필요가 없겠어요.
여: ______________""",
14: """남: 엄마, 이 청바지 어디에 버리면 돼요?
여: 잠깐. 그걸 왜 버리려고 하니? 아직 상태가 좋아 보이는데.
남: 알아요. 그런데 무릎에 구멍이 났어요.
여: 그럼 가방으로 업사이클링해 보는 건 어떠니? 새 가방 갖고 싶다고 하지 않았니?
남: 이 청바지로 가방을 만든다는 말씀이세요? 좋은 생각인데, 저는 바느질을 잘 못해요.
여: 고급 바느질 기술은 필요 없어. 온라인에 있는 쉬운 단계별 영상을 따라 하기만 하면 돼.
남: 음. 내 가방을 직접 만드는 건 재미있고 친환경적이겠네요.
여: 분명히 그럴 거야. 게다가 완성품을 보면 뿌듯할 거야.
남: 맞아요. 한번 해 봐야겠어요.
여: 내가 좋은 채널을 알아. 링크 보내 줄까?
남: ______________""",
15: """남: Sophia와 James는 한 과자 회사 마케팅 팀의 동료이다. 그들은 회사의 최신 제품인 초콜릿 바를 홍보하기 위해 함께 일하고 있다. 여러 광고 방법을 시도했지만 제품은 잘 팔리지 않았다. 새로운 마케팅 아이디어를 찾던 중, Sophia는 일부 브랜드가 잘 알려진 캐릭터와의 협업으로 인기를 높였다는 것을 알게 되었다. 그녀는 회사도 비슷한 방식으로 효과를 볼 수 있다고 생각한다. 캐릭터 테마 상품이 일반 제품보다 선호되는 경우가 많기 때문에, 제품에 인기 캐릭터를 넣으면 더 많은 관심을 끌고 판매를 늘릴 수 있을 것이다. 그래서 Sophia는 제품을 위해 캐릭터와 협업해야 한다고 제안하고 싶다. 이 상황에서 Sophia가 James에게 할 말로 가장 적절한 것은 무엇인가?
Sophia: ______________""",
16: """여: 안녕하세요, 학생 여러분. 아시다시피 우리는 일상생활에서 천연 재료와 인공 재료를 모두 사용합니다. 오늘은 천연 자원 대신 흔히 쓰이는 몇 가지 인공 재료를 살펴보겠습니다. 먼저 실크입니다. 인조 실크는 천연 실크만큼 옷에 널리 쓰이지만, 특별한 처리 없이도 세탁하고 관리하기가 더 쉽습니다. 가죽도 있습니다. 요즘 인조 가죽은 가방과 신발에 흔히 쓰입니다. 동물 가죽의 수요를 줄여서 특정 동물 종을 보호하는 데 도움이 될 수 있습니다. 다음은 다이아몬드입니다. 인공 다이아몬드는 천연 다이아몬드와 거의 똑같지만 훨씬 낮은 가격에 판매됩니다. 마지막으로 고무는 많은 생활용품에 들어가는 또 하나의 중요한 재료입니다. 합성 고무는 천연 고무보다 대개 더 오래가고 극한의 조건에서도 성능이 더 좋습니다. 이제 이러한 인공 대체재들이 시간이 지나면서 어떻게 발전해 왔는지 살펴봅시다.""",
}

VOC = {
1: [('valued','소중한'),('workout','운동'),('complaint','불만'),('policy','규정'),('wipe','닦다'),('compromise','위태롭게 하다'),('guideline','지침'),('pleasant','쾌적한')],
2: [('take notes','필기하다'),('as is','지금 그대로'),('figure out','알아내다'),('review','복습하다'),('emphasize','강조하다'),('selective','선택적인'),('key idea','핵심 내용')],
3: [('enthusiast','열성적인 사람'),('daydreaming','공상'),('laziness','게으름'),('challenge','이의를 제기하다'),('fuel','불을 지피다'),('inspire','불러일으키다'),('innovation','혁신'),('distant','먼'),('generate','만들어 내다')],
4: [('one-day','하루짜리'),('banner','현수막'),('eye-catching','눈길을 끄는'),('tray','쟁반'),('cabinet','수납장'),('flower-patterned','꽃무늬의'),('instructor','강사')],
5: [('all set','준비가 다 된'),('double-check','다시 확인하다'),('just in case','혹시 모르니'),('fully charged','완전히 충전된'),('set up','마련하다, 설치하다'),('record','녹화하다'),('entrance','입구')],
6: [('sign up for','~을 신청하다'),('package','패키지 상품'),('register','등록하다'),('gear','장비'),('rental','대여'),('admission fee','입장료'),('session','(1회) 수업')],
7: [('health checkup','건강 검진'),('have ~ over','~을 집에 초대하다'),('make it','(모임에) 가다'),('part-time job','아르바이트'),('break down','고장 나다'),('repairman','수리 기사'),('let ~ in','~을 들여보내다')],
8: [('brochure','안내 책자'),('scenery','경치'),('surrounded by','~에 둘러싸인'),('top class','최고 수준의'),('overlap','겹치다'),('reasonable','적당한'),('sell out','매진되다')],
9: [('community center','주민 센터'),('in public','사람들 앞에서'),('lecture','강의'),('maintain','유지하다'),('confidently','자신 있게'),('personalized','맞춤형의'),('participant','참가자'),('hesitate','망설이다')],
10: [('neck pillow','목베개'),('consider','고려하다'),('budget','예산'),('rule out','제외하다'),('material','소재'),('delicate','약한, 섬세한'),('rating','평점')],
11: [('out of battery','배터리가 다 된'),('charge','충전하다'),('shut down','꺼지다'),('electronic device','전자 기기'),('charger','충전기')],
12: [('sign up for','~에 신청하다'),('contest','공모전'),('professional-grade','전문가용의'),('category','부문'),('specifically','특별히'),('give it a go','한번 해 보다')],
13: [('in the mood for','~이 당기는'),('crowded','붐비는'),('stand in line','줄을 서다'),('waitlist','대기 명단'),('estimated','예상되는'),('notify','알리다'),('convenient','편리한')],
14: [('throw away','버리다'),('condition','상태'),('upcycle','업사이클링하다'),('sew','바느질하다'),('advanced','고급의'),('step-by-step','단계별의'),('eco-friendly','친환경적인'),('finished product','완성품')],
15: [('colleague','동료'),('promote','홍보하다'),('advertising','광고'),('collaboration','협업'),('well-known','잘 알려진'),('boost','늘리다'),('character-themed','캐릭터 테마의'),('partner up with','~와 협업하다')],
16: [('artificial','인공의'),('in place of','~ 대신에'),('maintain','관리하다'),('treatment','처리'),('demand','수요'),('species','종'),('identical','똑같은'),('extreme','극한의'),('alternative','대체재')],
}
