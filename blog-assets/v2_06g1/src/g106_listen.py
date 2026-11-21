# 2026 6월 고1 듣기 1~17 — 발문·선택지·해석·어휘 (교사 작성 해석)
import re
Q = {
1: ('다음을 듣고, 남자가 하는 말의 목적으로 가장 적절한 것을 고르시오.', ['우정 사진 공모전 참가 방법을 안내하려고', '교내 사진 전시회 일정 변경을 알리려고', '우정 사진 공모전 수상자를 공지하려고', '교내 사진 전시회 관람을 권유하려고', '교내 행사에 재능 기부를 요청하려고']),
2: ('대화를 듣고, 여자의 의견으로 가장 적절한 것을 고르시오.', ['일의 결과보다는 과정에 의미를 두어야 한다.', '힘들더라도 계획된 일을 미루지 않아야 한다.', '충분한 휴식을 통해 스트레스를 해소해야 한다.', '과제를 수행할 때 친구와 협력하는 것이 중요하다.', '미리 계획을 세우는 것이 시간 관리에 도움이 된다.']),
3: ('다음을 듣고, 남자가 하는 말의 요지로 가장 적절한 것을 고르시오.', ['정원 가꾸기를 통해 문제 해결 능력을 향상시킬 수 있다.', '정원 가꾸기는 스트레스 해소와 정서 안정에 효과적이다.', '식물을 건강하게 키우려면 책임감과 인내심이 필요하다.', '각 식물의 특성을 아는 것은 정원 관리에 도움이 된다.', '병충해를 예방하려면 정확한 원인 파악이 중요하다.']),
4: ('대화를 듣고, 그림에서 대화의 내용과 일치하지 않는 것을 고르시오.', None),
5: ('대화를 듣고, 여자가 할 일로 가장 적절한 것을 고르시오.', ['스크린 설치하기', '의자 추가로 가져오기', '마이크 점검하기', '문자 메시지 보내기', '공지 사항 게시하기']),
6: ('대화를 듣고, 남자가 지불할 금액을 고르시오. [3점]', ['$100', '$104', '$110', '$114', '$120']),
7: ('대화를 듣고, 여자가 역사 현장 학습에 갈 수 없는 이유를 고르시오.', ['지역 축제를 위한 자원봉사를 해야 해서', 'K-pop 댄스 수업에 참여해야 해서', '등록 기간 내에 신청하지 못해서', '할머니 생신 파티에 가야 해서', '과학 수업 과제를 끝내야 해서']),
8: ('대화를 듣고, Premier Art Class에 관해 언급되지 않은 것을 고르시오.', ['수업 내용', '수업 기간', '수업료', '준비물', '모집 제한 인원']),
9: ('Silverwood Farmers’ Day에 관한 다음 내용을 듣고, 일치하지 않는 것을 고르시오.', ['시청 앞 광장에서 열린다.', '오전 9시부터 오후 5시까지 운영된다.', '판매 품목에 고기와 채소가 포함된다.', '인근 공영 주차장을 이용할 수 있다.', '할인 쿠폰은 현장에서만 받을 수 있다.']),
10: ('다음 표를 보면서 대화를 듣고, 두 사람이 참가할 하프 마라톤을 고르시오.', None),
11: ('대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오.', ['I ordered a medium but got a large.', 'Well, this jacket is missing a button.', 'Sorry, but this item is not refundable.', 'I’d like to exchange it to a black one.', 'I want to pay for it with my credit card.']),
12: ('대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]', ['Oh, that is a problem for me.', 'Peanut cookies are my favorite.', 'I want to join the cooking class, too.', 'Instead, I made cookies with different shapes.', 'Why don’t you add some peanut butter next time?']),
13: ('대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오.', ['Then, we’ll offer a free meal during the flight.', 'Oh, I’m glad to have a seat next to them.', 'Sorry, but those seats are already taken.', 'Well, the airport is too far from here.', 'Okay, those seats are fine with me.']),
14: ('대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]', ['That’s why I feel AI videos are fun to watch.', 'Your video will get a lot of likes from others.', 'I will organize the background music alone.', 'It is easy for me to make AI videos.', 'I think the waves look a bit strange.']),
15: ('다음 상황 설명을 듣고, Mina가 Lucy에게 할 말로 가장 적절한 것을 고르시오.', ['How about going to the beach some other day?', 'Let’s go back home before it starts to rain.', 'We can hike in the mountains on that day.', 'Did you cancel everything and stay home?', 'I already packed my things last night.']),
}
Q16 = ('여자가 하는 말의 주제로 가장 적절한 것은?', ['tips for getting better sleep', 'foods to energize the brain', 'helpful foods to lose weight', 'easy recipes with video guides', 'traditional dishes in many countries'])
Q17 = ('언급된 음식이 아닌 것은?', ['avocado', 'broccoli', 'almonds', 'eggs', 'blueberries'])
TABLE10 = '| | Half Marathon | Month | Entry Fee (per person) | Shuttle Service | Gift |\n| :-: | :-: | :-: | :-: | :-: | :-: |\n| ① | A | August | $40 | × | socks |\n| ② | B | September | $40 | × | T-shirt |\n| ③ | C | September | $60 | ○ | T-shirt |\n| ④ | D | October | $60 | ○ | socks |\n| ⑤ | E | October | $80 | ○ | T-shirt |'
ANSLINE = {
11: "M: I’d like to exchange it to a black one.",
12: "W: Oh, that is a problem for me.",
13: "M: Okay, those seats are fine with me.",
14: "W: I think the waves look a bit strange.",
15: "Mina: How about going to the beach some other day?",
}
FIX = [('problemsolving', 'problem-solving'), ('Fortytwo', 'Forty-two'), ('AllYear', 'All-Year'), ('Kpop', 'K-pop'),
       ('oneonone', 'one-on-one'), ('oneday', 'one-day'), ('Tshirt', 'T-shirt'), ('eyecatching', 'eye-catching'),
       ('AIgenerated', 'AI-generated'), ('brainhealthy', 'brain-healthy'), ('highquality', 'high-quality')]

def load_sc(path='/home/claude/g1/lp_join.txt'):
    t = open(path).read()
    for a, b in FIX: t = t.replace(a, b)
    SC = {}
    parts = re.split(r'\n(?=\d{1,2}\. |\[16~17\])', '\n' + t)
    for p in parts:
        p = p.strip()
        if not p: continue
        if p.startswith('[16~17]'):
            SC[16] = '\n'.join(l for l in p.split('\n')[1:] if l.startswith('W:'))
            continue
        m = re.match(r'(\d{1,2})\. ', p)
        n = int(m.group(1))
        if n > 15: continue
        lines = [l for l in p.split('\n')[1:] if l.strip() and not re.match(r'^(M|W):\s*$', l.strip())]
        if n in ANSLINE: lines.append(ANSLINE[n])
        SC[n] = '\n'.join(lines)
    return SC

KO = {
1: """남: 여러분, 좋은 아침입니다! 저는 학생회장 Kevin Davis입니다. 오늘부터 우리 학교에서 우정을 주제로 한 멋진 사진 전시회가 열립니다. 사진들에는 재능 있는 많은 학생들의 창의성이 담겨 있습니다. 작품은 2층 교무실 옆 복도에 전시되어 있습니다. 오셔서 사진 하나하나에 담긴 따뜻한 이야기를 감상해 주세요. 전시회는 이번 주 금요일까지만 열리니, 이번 주에 놓치지 마세요!""",
2: """여: 얘, Tommy, 너 아주 피곤해 보이는구나. 괜찮니?
남: 엄마, 다음 주 화요일까지 과제를 세 개나 끝내야 해서 너무 스트레스 받아요.
여: 힘들겠구나.
남: 네, 짧은 시간에 많은 일을 하는 게 어려워요.
여: 미리 계획을 세워 보는 게 어떠니? 시간 관리에 도움이 될 거야.
남: 정말 효과가 있을까요?
여: 물론이지. 미리 계획을 세우면 제때 일을 끝낼 수 있단다.
남: 그런데 저는 계획 세우는 게 귀찮아요.
여: 그 마음 알아. 하지만 그렇게 하면 상황을 더 낫게 만들 수 있을 거야.
남: 알겠어요. 이번엔 한번 해 볼게요.
여: 미리 계획을 세우는 게 분명 네 시간 관리에 도움이 될 거야!
남: 고마워요, 엄마. 엄마가 최고예요!""",
3: """남: 청취자 여러분, 안녕하세요! 진행자 Justin Reed입니다. '정원 가꾸기의 세계'에 오신 것을 환영합니다. 정원 가꾸기가 그저 식물을 기르는 일이라고 생각하시나요? 사실은 그렇지 않습니다. 정원 가꾸기의 흥미로운 점은 문제 해결 능력을 기르는 데 도움이 된다는 것입니다. 식물을 기르다 보면 벌레, 잡초, 식물 질병 같은 다양한 어려움을 마주하게 됩니다. 이런 문제를 해결하려면 먼저 원인을 찾아야 합니다. 그런 다음 알맞은 해결책을 적용하지요. 결국 여러분은 식물을 살려 낼 수 있습니다. 바로 이렇게 정원 가꾸기를 통해 문제 해결 능력을 키울 수 있습니다. 그러니 한번 해 보는 게 어떨까요? 손에 흙을 묻히며 그 여정을 즐겨 보세요!""",
4: """여: 얘, Harry. 서랍에서 옛날 사진을 찾았어.
남: 어디 보자. 음…. 모래밭에 있는 어린 여자아이는 누구야?
여: 나야. 모래성을 만들고 있었어.
남: 예쁘다. 비눗방울을 부는 남자아이도 보이네. 누구야?
여: 내 남동생이야.
남: 재미있어 보인다. 아, 나무 근처에 자전거가 두 대 있네.
여: 응, 타고 돌아다닌 다음에 거기 세워 뒀었어.
남: 그리고 근처에 개도 있네.
여: 우리 개야. 공을 가지고 놀고 있었어.
남: 귀엽다. 그런데 하트 무늬 모자를 쓴 저 여자분은 누구야?
여: 우리 엄마야.
남: 다 같이 즐거운 시간을 보냈던 것 같네!""",
5: """남: 이 선생님, 학생들을 위한 '멘토와의 만남' 행사 준비가 거의 끝났어요.
여: 네. 이제 모든 걸 한 번 더 점검해 봐요. 멘토분께 확인 문자 메시지 보내셨어요?
남: 네. 꼭 오시겠다고 답장하셨어요.
여: 좋아요. 강당에 스크린은 설치하셨어요?
남: 네, 어제 해 두었어요.
여: 완벽해요. 마이크는 확인하셨어요?
남: 테스트해 봤는데 잘 작동해요.
여: 좋네요. 또 무엇을 확인해야 하죠?
남: 온라인에 공지 사항 올리셨어요?
여: 네, 벌써 했어요. 그런데 학생이 몇 명이나 신청했어요?
남: 42명이요. 그래서 의자가 더 필요할 거예요.
여: 그럼 제가 지금 바로 몇 개 더 가져올게요.""",
6: """여: All-Year Surf Zone에 오신 것을 환영합니다. 무엇을 도와드릴까요?
남: 안녕하세요. 아들과 함께 실내 서핑을 해 보고 싶어서요.
여: 서핑해 보신 적 있으세요?
남: 아니요, 이번이 처음이에요.
여: 괜찮습니다. 초급자 강습을 들으시면 돼요. 서프보드를 포함해서 1인당 50달러입니다.
남: 좋네요. 그런데 서핑복도 빌릴 수 있나요?
여: 물론이죠. 어른은 10달러이고 8세 미만 어린이는 무료입니다.
남: 잘됐네요. 아들이 일곱 살이에요. 한 벌씩 빌릴게요.
여: 알겠습니다. 1인당 4달러에 간식도 제공하는데, 드릴까요?
남: 아니요, 괜찮습니다.
여: 네. 그럼 초급자 강습 두 명, 어른 서핑복 한 벌, 무료 어린이 서핑복 한 벌, 맞으시죠?
남: 맞아요. 여기 제 신용카드요.""",
7: """남: Stacy, 역사 현장 학습에 같이 가는 게 어때?
여: 이번 주 토요일에 하는 거?
남: 맞아. 등록이 곧 끝나니까 서둘러야 해.
여: 가고 싶은데, 못 가.
남: 아, 이번 주 토요일에 할머니 생신 파티에 간다고 했던 거 기억난다.
여: 아니. 그건 사실 다음 주 토요일이야.
남: 그럼 과학 수업 과제를 끝내야 하는 거야?
여: 아, 그건 어제 벌써 다 했어!
남: 그럼 뭐 때문에 못 가는 거야?
여: 사실 그날 주민 센터에 있을 거야.
남: 거기서 하는 K-pop 댄스 수업에 참여하는 거야?
여: 아니. 그날 우리 지역 축제를 위한 자원봉사를 해야 해.
남: 아, 좋은 경험이 되겠다.
여: 응. 이번에 같이 못 가서 미안해.""",
8: """남: Emily, Premier Art Class 포스터 봤어?
여: 아니, 못 봤어. 어떤 수업이야?
남: 음, 전문적인 스케치 기법에 초점을 맞춘 수업이야.
여: 재미있겠다! 너 그 수업 들을 거야?
남: 응, 방금 신청했어.
여: 정말? 그럼 수업은 언제 열려?
남: 7월 20일부터 7월 24일까지 문화 센터에서 열려.
여: 수업료는 얼마야?
남: 100달러야.
여: 와, 꽤 비싸네.
남: 맞아, 그런데 강사님이 모두에게 일대일로 도움을 주셔. 그래서 수강생이 딱 5명으로 제한돼 있어.
여: 바로 내게 필요한 거야. 그럼 나도 신청할래.
남: 좋아. 수업에서 보자!""",
9: """여: 안녕하세요, 여러분. 저는 Silverwood 시청의 Sarah Brown입니다. 신선한 식품을 찾고 계신가요? 그렇다면 Silverwood Farmers’ Day가 딱 맞는 선택입니다. 이 하루 행사는 6월 27일 시청 앞 광장에서 열립니다. 운영 시간은 오전 9시부터 오후 5시까지입니다. 판매 품목에는 고기, 채소 등이 있습니다. 인근 공영 주차장을 이용하실 수 있습니다. 자세한 내용은 시청 웹사이트를 방문해 주세요. 웹사이트에서 할인 쿠폰도 내려받으실 수 있습니다. 이 특별한 행사를 놓치지 마세요!""",
10: """여: 여보, 우리가 나갈 하프 마라톤 찾아봤어요?
남: 응, 방금 여기 목록을 찾았어요. 와서 봐요.
여: 어디 봐요…. [잠시 후] 8월은 달리기에는 너무 더워요.
남: 맞아요. 참가비는요?
여: 1인당 80달러 미만으로 하고 싶어요.
남: 동의해요. 그럼 이건 빼야겠네요.
여: 셔틀 서비스는요? 있으면 더 좋을 것 같아요.
남: 그래요, 그게 있어야 장소까지 가기 더 편하겠죠. 그럼 두 개가 남네요.
여: 그럼 참가 기념품으로 양말과 티셔츠 중 어떤 게 좋아요?
남: 나는 양말이 좋아요.
여: 그럼 이게 우리한테 딱이네요!""",
11: """여: Trendy Store에 오신 것을 환영합니다. 무엇을 도와드릴까요?
남: 안녕하세요, 어제 아들에게 주려고 재킷을 샀는데 아들이 이 색깔을 마음에 들어 하지 않네요. 여기 영수증이요.
여: 알겠습니다. 다른 색깔로 바꾸시겠어요, 아니면 환불받으시겠어요?
남: 검은색으로 교환하고 싶어요.""",
12: """남: Amy, 요리 수업에서 이 쿠키를 구웠어. 하나 먹어 볼래?
여: 맛있어 보이는데, 나 땅콩 알레르기가 있어. 내가 먹어도 괜찮은 거야?
남: 사실, 땅콩버터를 좀 넣었어.
여: 아, 그럼 나한테는 문제가 되겠네.""",
13: """[전화벨이 울린다.]
여: 안녕하세요, Good Travel 항공입니다. 무엇을 도와드릴까요?
남: 항공편을 예약했는데, 변경할 수 있을까요?
여: 물론입니다. 성함과 예약 번호를 알려 주시겠어요?
남: 제 이름은 Mark Rogers이고, 예약 번호는 GA702입니다.
여: 감사합니다. 예약을 확인해 보겠습니다. 잠시만 기다려 주세요. [타자 치는 소리] 7월 21일 오후 3시 뉴욕행 항공편이 맞으신가요?
남: 네, 맞아요.
여: 네. 그럼 어떻게 변경하고 싶으세요?
남: 좌석을 두 개 더 예약하고 싶어요.
여: 물론이죠. 아직 몇 자리 남아 있습니다.
남: 제 옆자리 중에 남은 좌석이 있나요?
여: 죄송합니다. 고객님 좌석 바로 뒷자리만 남아 있습니다.
남: 좋아요, 그 자리도 괜찮아요.""",
14: """남: 얘, 너 정말 집중하고 있네. 뭐 보고 있어?
여: 아주 흥미로운 영상을 보고 있어. 남자랑 돌고래가 바다에서 같이 헤엄치는 영상이야.
남: 정말 눈길을 끄는데.
여: 그렇긴 한데, 이게 진짜인지 AI로 만든 건지 모르겠어.
남: 진짜 같은데. 하지만 AI 영상을 더 자세히 보면 뭔가 부자연스러워 보이거나 어색하게 움직일 수 있어.
여: 정말? 몰랐어.
남: 그럼 그 영상에서 부자연스러워 보이는 걸 찾아보는 게 어때?
여: 좋아, 해 볼게. [잠시 후] 아, 여기 하나 찾았어! 와서 봐.
남: 뭔데?
여: 파도가 좀 이상해 보이는 것 같아.""",
15: """남: Mina와 Lucy는 여름 방학 동안 바닷가 여행을 계획해 왔습니다. 두 사람은 시원한 물을 즐기며 함께 쉴 생각에 들떠 있습니다. 여행 이틀 전, Mina는 일기 예보를 확인하다가 두 사람이 가기로 한 바로 그날 폭우가 예상된다는 것을 알게 됩니다. 그런 날씨에 여행하는 것은 위험할 수 있어서 Mina는 걱정이 됩니다. 어떤 위험도 피하고 싶어서, Mina는 계획을 다른 날로 바꾸자고 제안하기로 합니다. 이 상황에서 Mina가 Lucy에게 할 말로 가장 적절한 것은 무엇일까요?
Mina: 다른 날 바닷가에 가는 게 어때?""",
16: """여: 안녕하세요, 여러분. 저는 Core Health Institute의 영양사 Eve Miller입니다. 여러분의 뇌는 스트레스와 과로 때문에 쉽게 지칠 수 있습니다. 그래서 뇌에 활력을 주는 음식 몇 가지를 소개하겠습니다. 먼저, 아보카도에는 뇌에 좋은 건강한 지방이 들어 있습니다. 아보카도를 먹으면 하루 종일 더 집중할 수 있습니다. 다음으로, 브로콜리에는 비타민 K 같은 뇌 건강에 좋은 영양소가 들어 있습니다. 매일 먹으면 뇌세포 사이의 소통이 좋아집니다. 달걀도 질 좋은 단백질의 훌륭한 공급원으로, 집중력을 높이는 에너지를 줍니다. 마지막으로, 뇌에 도움이 되는 음식이 하나 더 있습니다. 블루베리는 기억력에 정말 좋습니다. 블루베리를 꾸준히 먹으면 중요한 것을 잊어버리지 않도록 도와줍니다. 이제 이 음식들로 만드는 간단하고 쉬운 요리법 영상을 보여 드리겠습니다!""",
}

VOC = {
1: [('student council', '학생회'), ('exhibition', '전시회'), ('friendship', '우정'), ('creativity', '창의성'), ('talented', '재능 있는'), ('on display', '전시된'), ('hallway', '복도'), ('teachers’ office', '교무실'), ('run', '(행사가) 계속되다')],
2: [('stressed', '스트레스를 받는'), ('project', '과제'), ('in advance', '미리'), ('manage', '관리하다'), ('in time', '제때'), ('annoying', '귀찮은'), ('give it a try', '한번 해 보다'), ('time management', '시간 관리')],
3: [('host', '진행자'), ('gardening', '정원 가꾸기'), ('problem-solving skill', '문제 해결 능력'), ('face', '마주하다'), ('weed', '잡초'), ('disease', '질병'), ('identify', '찾아내다, 확인하다'), ('cause', '원인'), ('apply', '적용하다'), ('appropriate', '알맞은')],
4: [('drawer', '서랍'), ('take a look', '한번 보다'), ('sandcastle', '모래성'), ('blow bubbles', '비눗방울을 불다'), ('nearby', '근처에'), ('pattern', '무늬')],
5: [('mentor', '멘토'), ('go over', '점검하다, 검토하다'), ('remind', '상기시키다'), ('definitely', '꼭, 반드시'), ('set up', '설치하다'), ('auditorium', '강당'), ('post', '게시하다'), ('notice', '공지 사항'), ('sign up', '신청하다')],
6: [('indoor', '실내의'), ('surf', '서핑하다'), ('beginner', '초급자'), ('per person', '1인당'), ('including', '~을 포함하여'), ('rent', '빌리다'), ('surfwear', '서핑복'), ('offer', '제공하다')],
7: [('field trip', '현장 학습'), ('registration', '등록'), ('assignment', '과제'), ('community center', '주민 센터'), ('take part in', '~에 참여하다'), ('volunteer work', '자원봉사'), ('local festival', '지역 축제')],
8: [('focus on', '~에 초점을 맞추다'), ('professional', '전문적인'), ('technique', '기법'), ('be held', '열리다'), ('class fee', '수업료'), ('instructor', '강사'), ('one-on-one', '일대일의'), ('be limited to', '~로 제한되다')],
9: [('city hall', '시청'), ('fresh', '신선한'), ('square', '광장'), ('item for sale', '판매 품목'), ('public parking lot', '공영 주차장'), ('available', '이용 가능한'), ('further details', '자세한 내용'), ('discount coupon', '할인 쿠폰')],
10: [('half marathon', '하프 마라톤'), ('search for', '~을 찾아보다'), ('entry fee', '참가비'), ('under', '~ 미만의'), ('shuttle service', '셔틀 서비스'), ('convenient', '편리한'), ('participate', '참가하다'), ('prefer', '더 좋아하다')],
11: [('receipt', '영수증'), ('refund', '환불'), ('exchange', '교환하다'), ('refundable', '환불 가능한'), ('missing', '빠진, 없는')],
12: [('bake', '굽다'), ('tasty', '맛있는'), ('be allergic to', '~에 알레르기가 있다'), ('peanut', '땅콩'), ('safe', '안전한, 괜찮은')],
13: [('flight reservation', '항공편 예약'), ('make changes', '변경하다'), ('reservation number', '예약 번호'), ('book', '예약하다'), ('available', '이용 가능한'), ('directly', '바로'), ('behind', '~ 뒤에')],
14: [('focused', '집중한'), ('video clip', '영상'), ('dolphin', '돌고래'), ('eye-catching', '눈길을 끄는'), ('AI-generated', 'AI로 만든'), ('closely', '자세히'), ('unnatural', '부자연스러운'), ('awkward', '어색한'), ('strange', '이상한')],
15: [('plan', '계획하다'), ('relax', '쉬다'), ('weather forecast', '일기 예보'), ('discover', '알게 되다'), ('heavy rain', '폭우'), ('expect', '예상하다'), ('avoid', '피하다'), ('risk', '위험'), ('suggest', '제안하다')],
16: [('nutritionist', '영양사'), ('overwork', '과로'), ('energize', '활력을 주다'), ('healthy fat', '건강한 지방'), ('nutrient', '영양소'), ('enhance', '높이다, 향상시키다'), ('high-quality protein', '질 좋은 단백질'), ('boost', '높이다'), ('concentration', '집중력'), ('regularly', '꾸준히')],
}
