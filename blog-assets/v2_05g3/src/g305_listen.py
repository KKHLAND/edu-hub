# 2026 5월 고3 듣기 1~17 — 발문·선택지·해석·어휘 (교사 작성 해석)
import re
Q = {
1: ('다음을 듣고, 여자가 하는 말의 목적으로 가장 적절한 것을 고르시오.', ['자전거를 지정된 구역에 주차할 것을 요청하려고','공원 내 단체 조깅 시 소음을 자제할 것을 부탁하려고','자전거 이용 시 안전 장비 착용의 중요성을 강조하려고','공원에서 자전거 이용 시 제한 속도 준수를 당부하려고','공사로 인해 공원 산책로 이용이 임시 중단됨을 안내하려고']),
2: ('대화를 듣고, 남자의 의견으로 가장 적절한 것을 고르시오.', ['속독보다는 정독이 글의 내용 이해에 효과적이다.','배경지식에 의존한 독해는 글의 내용을 왜곡할 수 있다.','독서는 새로운 어휘를 자연스럽게 익히는 데 도움이 된다.','모르는 단어의 뜻을 매번 찾는 것은 글 전체의 이해를 어렵게 한다.','요지를 정확히 전달하기 위해 맥락에 맞는 어휘 사용이 필요하다.']),
3: ('다음을 듣고, 여자가 하는 말의 요지로 가장 적절한 것을 고르시오.', ['시끄러운 음악은 불안감을 더욱 증가시킨다.','개인의 성향은 음악에 대한 취향에서 드러난다.','배경 음악은 사람들의 대화 방식에 영향을 미친다.','작업 중 음악 감상은 사람들의 집중력을 떨어뜨린다.','음악은 듣는 사람에게 특정 경험과 기억을 상기시킨다.']),
4: ('대화를 듣고, 그림에서 대화의 내용과 일치하지 않는 것을 고르시오.', None),
5: ('대화를 듣고, 남자가 할 일로 가장 적절한 것을 고르시오.', ['악기 옮기기','마이크 충전하기','마실 물 가져오기','여분의 배터리 챙기기','행사 안내 방송 요청하기']),
6: ('대화를 듣고, 여자가 지불할 금액을 고르시오. [3점]', ['$27','$35','$36','$40','$45']),
7: ('대화를 듣고, 남자가 Stand-up Comedy Show에 갈 수 없는 이유를 고르시오.', ['직장 동료 송별회가 있어서','대학원 야간 수업이 있어서','회사 프로젝트를 준비해야 해서','가족과 저녁 식사를 하기로 해서','스트레스로 인해 몸이 좋지 않아서']),
8: ('대화를 듣고, Big Wave Surfing Class에 관해 언급되지 않은 것을 고르시오.', ['장소','소요 시간','최대 수강 인원','수강료','등록 방법']),
9: ('Ironveil Castle Tour에 관한 다음 내용을 듣고, 일치하지 않는 것을 고르시오.', ['오전 10시부터 투어가 있다.','왕가의 정원에서부터 성탑까지 진행된다.','가이드는 왕과 왕비에 대한 이야기를 들려준다.','기념품으로 책갈피를 받게 된다.','티켓은 현장 구매가 가능하다.']),
10: ('다음 표를 보면서 대화를 듣고, 두 사람이 구입할 빨래 바구니를 고르시오.', None),
11: ('대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오.', ["I think I’ll be done before lunch time.","Let’s go over the slides together next week.","It takes too long to get a response from you.","I’ll start making my slides when you’re done.","You must memorize the script for the presentation."]),
12: ('대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오.', ["I set the tables before everyone arrived.","I wonder if we can change to the smaller room.","I’m afraid they’ve arrived too late at the dinner.","I’ll call the restaurant to update the reservation.","I haven’t decided which restaurant to choose yet."]),
13: ('대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오.', ["Sure. You should rest to get over your fatigue.","Of course. I can send you the schedule I made.","Yes, I’ll consider that the next time I plan a trip.","Good. I’d like to try a guided tour like the one you took.","Actually, we canceled most of our plans because of rain."]),
14: ('대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오. [3점]', ["Look! People wrote positive reviews about my pizza.","Don’t worry. There are so many pizza places around here.","Well, I always put photos of the restaurant in the reviews.","Oh, no. I shouldn’t have spent so much time on social media.","Great. That could let more people know about my restaurant."]),
15: ('다음 상황 설명을 듣고, Emily가 Ryan에게 할 말로 가장 적절한 것을 고르시오. [3점]', ["We’d better close the booth before it gets too late.","Let’s get some rest first and walk around in an hour.","Why don’t we walk quickly to see as many booths as we can?","We should come up with fun activities to attract more visitors.","How about choosing a few booths we like and enjoying them more?"]),
}
Q16 = ('여자가 하는 말의 주제로 가장 적절한 것은?', ['importance of colors in company logos','various ways to display emotion through colors','color-related expressions used in the economy','influence of product colors on economic outcomes','color preferences depending on cultural backgrounds'])
Q17 = ('언급된 색깔이 아닌 것은?', ['red','blue','green','white','orange'])
TABLE10 = '| | Product | Size | Material | Price | Handles |\n| :-: | :-: | :-: | :-: | :-: | :-: |\n| ① | A | Small | Wood | $22 | ◯ |\n| ② | B | Medium | Plastic | $28 | ◯ |\n| ③ | C | Medium | Stainless Steel | $33 | ☓ |\n| ④ | D | Large | Stainless Steel | $38 | ◯ |\n| ⑤ | E | Large | Wood | $42 | ☓ |'
ANSLINE = {
11: "W: I think I’ll be done before lunch time.",
12: "M: I’ll call the restaurant to update the reservation.",
13: "W: Of course. I can send you the schedule I made.",
14: "M: Great. That could let more people know about my restaurant.",
15: "Emily: How about choosing a few booths we like and enjoying them more?",
}

def load_sc(path='/home/claude/m5/lp.txt'):
    t = open(path).read().replace('­', '-')
    parts = re.split(r'\n(\d{1,2})번\n', t)
    SC = {}
    for i in range(1, len(parts) - 1, 2):
        n = int(parts[i]); body = parts[i + 1].split('16번부터')[0]
        if n in (16, 17) and n in SC: continue
        lines = [l.strip() for l in body.split('\n')]
        out = []
        for l in lines:
            if not l or l.startswith('(10 seconds)') or re.match(r'^\d+$', l) or l.startswith('16번부터') or l.startswith('다시 한 번') or l.startswith('이제 듣기'): continue
            if '고르시오' in l or l.endswith('것은?') or l.startswith('16번과'): continue
            if re.match(r'^(M|W|Emily):\s*$', l): continue
            if re.match(r'^(M|W):', l) or l.startswith('[') or not out: out.append(l)
            else: out[-1] += ' ' + l
        if n == 16:
            # 두 번 반복되는 담화 — 앞의 한 번만
            txt = '\n'.join(out); k = txt.find('W: Hello, students.', 5)
            out = [txt[:k].strip()] if k > 0 else out
        if n in ANSLINE: out.append(ANSLINE[n])
        if out and n <= 15: SC[n] = '\n'.join(out)
    a = t.find('16번과 17번'); b = t.find('다시 한 번 듣겠습니다', a)
    seg = t[a:b].split('\n')[2:]
    SC[16] = ' '.join(l.strip() for l in seg if l.strip())
    return SC

KO = {
1: """[차임벨이 울린다.]
여: 방문객 여러분, 안녕하세요. Roseydale 공원 관리 사무소에서 안내 말씀 드립니다. 모든 분의 안전을 위해 자전거를 타시는 분들은 공원 안에 게시된 제한 속도를 지켜 주시기 바랍니다. 저희 공원은 걷고, 달리고, 자전거를 타는 많은 사람이 이용합니다. 자전거 전용 도로가 지정되어 있더라도 제한 속도를 넘겨 자전거를 타면 자전거 이용자뿐 아니라 다른 사람들에게도 위험할 수 있습니다. 빠르게 달리는 자전거는 갑자기 앞에 사람이 나타났을 때 속도를 줄이지 못해 심각한 부상으로 이어지는 경우가 많습니다. 제한 속도를 지키면 이런 뜻밖의 사고를 막고 공원을 모든 방문객에게 더 안전한 곳으로 만들 수 있습니다. 협조해 주셔서 감사합니다.""",
2: """남: Anna, 너 책 읽으면서 계속 휴대폰을 확인하네.
여: 응. 모르는 단어를 하나하나 다 찾아보고 있어.
남: 매번? 그러면 오히려 글 전체를 따라가기가 어려워질 수 있어.
여: 정말? 단어를 확인하는 게 도움이 될 줄 알았는데.
남: 개별 단어를 이해하는 데는 도움이 되지만 읽기의 흐름을 끊어.
여: 무슨 뜻이야?
남: 단어를 찾으려고 멈추면 글에서 어디까지 읽었는지 놓칠 수 있잖아.
여: 아, 맞아. 문장을 다시 읽어야 할 때가 많아.
남: 바로 그거야. 그리고 그렇게 계속하다 보면 이야기의 요지를 놓칠 수도 있어.
여: 일리가 있네.
남: 그래서 모르는 단어를 매번 확인하면 글 전체를 이해하기가 어려워질 수 있어.
여: 알겠어. 명심할게.""",
3: """여: 여러분, 안녕하세요. Music Insight의 Natalie Brown입니다. 오늘은 배경 음악이 사람들이 서로 이야기하는 방식에 어떤 영향을 미치는지 이야기해 보려고 합니다. 간단히 말해, 배경 음악은 사람들이 소통하는 방식을 바꿀 수 있습니다. 예를 들어, 시끄럽고 빠른 음악이 나올 때 사람들은 흔히 더 빨리 말하고 목소리를 높입니다. 소리가 말소리와 경쟁하기 때문에 대화는 더 짧고 직설적이 됩니다. 반면에 느리고 부드러운 음악은 사람들이 속도를 늦추고 더 부드럽게 말하도록 합니다. 이는 흔히 더 길고 차분한 대화로 이어집니다. 그러니 배경 음악은 단지 분위기만 만드는 것이 아닙니다. 우리가 말하는 방식을 바꿉니다. 이제 잠시 쉬었다가 곧 돌아오겠습니다. 채널 고정해 주세요.""",
4: """남: 좋은 아침이에요, Tania. 지난 주말에 뭐 했어요?
여: 딸을 어린이 초콜릿 체험 교실에 데려갔어요. 이 사진 좀 보세요.
남: 오, 벽에 'A Sweet Day with Chocolate'라고 쓰인 현수막이 있네요.
여: 네, 그게 체험 교실 이름이었어요.
남: 귀엽네요. 줄무늬 앞치마를 입은 여자아이가 따님이에요?
여: 네. 거기서 정말 즐거운 시간을 보냈어요.
남: 아, 그렇군요. 시계 아래 전자레인지를 썼어요?
여: 네. 거기서 초콜릿을 녹였어요.
남: 불을 쓰는 것보다 안전해 보이네요. 탁자 위에 있는 그릇 두 개는 뭐에 쓰는 거예요?
여: 딸이 고른 재료와 초콜릿을 섞는 데 쓰는 거예요. 그리고 선반 위에 별 모양 상자 보이세요?
남: 네. 그게 뭐예요?
여: 초콜릿이 완성되면 그 상자에 넣어서 집에 가져왔어요.
남: 분명 즐거웠겠네요. 저도 우리 아이를 데려가 봐야겠어요.""",
5: """여: Issac, 오늘이 우리 밴드의 첫 교내 버스킹 행사야. 준비 거의 다 됐지?
남: 거의. 마지막으로 몇 가지만 확인하자.
여: 좋아. 방금 마이크를 확인했는데 완전히 충전돼 있어.
남: 잘됐다. 그리고 전원이 더 필요할 경우를 대비해서 내가 여분의 배터리를 가져왔어.
여: 완벽해. 분명히 필요할 거야.
남: 음악실에서 악기는 옮겼어?
여: 응, 다른 멤버들이랑 본관 앞으로 옮겼어.
남: 고마워. 잠깐, 교내 방송반은 행사 안내 방송을 언제 해야 하는지 알고 있어?
여: 응, Jeremy가 점심 전에 해 달라고 부탁했으니까 문제없어.
남: 좋아. 그런데 공연 중에 물이 좀 필요할지도 몰라.
여: 맞다. 완전히 잊고 있었어.
남: 걱정 마. 마실 물은 내가 가져올게.
여: 고마워! 다 준비된 것 같아.""",
6: """남: Dream Bath Shop에 오신 것을 환영합니다! 무엇을 도와드릴까요?
여: 안녕하세요. 엄마께 드릴 수건 세트를 찾고 있어요.
남: 네, 두 종류가 있습니다. 기본 세트는 15달러, 유기농 면으로 만든 프리미엄 세트는 20달러입니다.
여: 엄마가 피부가 민감하셔서 프리미엄 세트 하나로 할게요.
남: 잘 고르셨어요. 더 필요하신 건요?
여: 헤어 트리트먼트도 있나요?
남: 네. 이 보습 헤어 트리트먼트는 10달러입니다. 인기 상품이에요.
여: 좋네요. 하나는 엄마 것, 하나는 제 것으로 두 병 살게요. 그게 다예요.
남: 좋습니다. 그럼 프리미엄 수건 세트 하나와 보습 헤어 트리트먼트 두 병 맞으시죠?
여: 네. 그리고 앱에서 받은 이 쿠폰을 쓸 수 있나요?
남: 물론이죠. 총액에서 10% 할인됩니다.
여: 좋아요! 신용카드로 계산할게요.""",
7: """여: John, 요즘 무척 지쳐 보여. 괜찮아?
남: 응, 회사 프로젝트 준비하느라 바빴어. 스트레스를 풀 방법이 필요해.
여: 그럼 스탠드업 코미디 쇼는 어때? 유명 코미디언 Marvin Krull이 우리 동네에 온대.
남: 정말? 나 그 사람 엄청 좋아하는데. 언제야?
여: 다음 주 금요일 저녁이야. 같이 가자.
남: 아, 이런. 못 갈 것 같아.
여: 왜? 아직 대학원 야간 수업 들어?
남: 그건 문제가 아니야. 학기는 지난주에 끝났어.
여: 전에 말했던 가족 저녁 식사 날이야?
남: 아니, 그건 일요일이야.
여: 그럼 왜 못 가는데?
남: 동료 한 명이 다른 회사로 옮겨서 그 사람 송별회를 하거든.
여: 그렇구나. 다음에 가자.""",
8: """남: 안녕, Lisa. 뭘 보고 있어?
여: Big Wave Surfing Class 전단이야. 들어 볼까 생각 중이야.
남: 오, 나 전에 서핑해 본 적 있어. 정말 재미있었어. 어디서 해?
여: Coral Beach에서 해.
남: 거기 알아. 파도가 정말 좋아.
여: 전단에도 그렇게 쓰여 있어. 그리고 수업은 두 시간이야.
남: 초보자에게는 그 정도면 충분할 것 같아. 그보다 길면 너무 힘들 거야.
여: 일리가 있네. 수업 인원이 중요하다고 생각해? 한 반에 최대 5명이래.
남: 초보자 수업으로는 좋은 인원이야. 강사가 한 명 한 명에게 서핑 기초를 쉽게 가르쳐 줄 수 있잖아. 수강료는 얼마야?
여: 서핑 장비 일체와 간식을 포함해서 1인당 50달러래.
남: 적당하네. 재미있을 거야.""",
9: """남: 청취자 여러분, 안녕하세요! 왕이나 왕비가 되어 고대 성을 거니는 상상을 해 보신 적이 있나요? 그렇다면 Ironveil 성 투어에 참여해 보세요. 오전 10시부터 매시간 투어가 있습니다. 투어는 왕가의 정원에서 시작해 성탑까지 이어집니다. 탑 꼭대기에서는 숨이 멎을 듯한 경치를 볼 수 있습니다. 투어 내내 가이드가 수백 년 전 그곳에 살았던 왕과 왕비에 대한 흥미진진한 이야기를 들려줍니다. 투어가 끝나면 기념품으로 책갈피를 받게 됩니다. 티켓은 1인당 10달러입니다. 투어마다 자리가 한정되어 있으므로 티켓은 반드시 온라인으로 미리 구매해야 합니다. Ironveil 성에서 잊지 못할 추억을 만들 기회를 놓치지 마세요!""",
10: """남: 여보, 새 빨래 바구니가 필요해요.
여: 알아요. 온라인에서 몇 가지 찾아보고 있었어요. 같이 골라 봐요.
남: 좋아요. 바구니 크기가 여러 가지네요.
여: 작은 건 금방 가득 차서 불편할 것 같아요.
남: 맞아요. 그리고 소재도 고를 수 있네요. 전에 쓰던 플라스틱 바구니는 너무 쉽게 깨졌어요.
여: 네. 옷을 많이 담기에는 튼튼하지 않아요.
남: 맞아요. 이건 어때요?
여: 좋아 보이는데 40달러 넘게 쓰는 건 너무 많아요.
남: 동의해요. 이제 두 개가 남았네요.
여: 네. 손잡이가 필요할까요?
남: 물론이죠. 손잡이 없는 바구니는 들고 다니기 힘들 거예요.
여: 좋은 지적이에요. 그럼 우리에게 맞는 건 하나뿐이네요.
남: 좋아요. 그걸로 사요.""",
11: """남: Emily, 내일 발표 슬라이드 준비됐어? 네가 끝내면 내가 모두의 부분을 합칠게.
여: 아, 거의 다 됐어. 마지막으로 한 번만 확인하면 돼.
남: 그렇구나. 얼마나 걸릴 것 같아?
여: 점심시간 전에는 끝날 것 같아.""",
12: """여: Miller 씨, 회사 행사 저녁 식사 예약은 벌써 하셨어요?
남: 네, The Amber 식당에 12명이 쓸 방을 예약했어요.
여: 아, 실은 직원 두 명이 더 온다고 방금 말했어요.
남: 식당에 전화해서 예약을 변경할게요.""",
13: """남: Mindy, 휴일에 부모님과 간 Pine 섬 여행은 어땠어?
여: 정말 좋았어. 부모님이 여행에 무척 만족하셨어.
남: 잘됐다. 뭐 했어?
여: 유적지를 둘러보고, 전통 음식을 먹고, 경치 좋은 전망대에서 사진을 찍었어.
남: 그렇게 많은 활동을 하셨는데 부모님이 힘들어하지 않으셨어?
여: 아니. 그곳을 천천히 즐기실 수 있게 시간을 충분히 드렸거든.
남: 좋네. 여행 전체를 네가 직접 계획했다는 거야?
여: 응, 내가 했어. 부모님이 지치지 않으시도록 단순하게 짜려고 했어.
남: 그렇구나. 사실 나도 이번 여름에 부모님 결혼 40주년 기념으로 Pine 섬 여행을 계획하고 있어.
여: 그럼 이런 여유로운 여행이 부모님께 딱 맞을 것 같아.
남: 그래서 네 여행 계획을 나한테 공유해 줄 수 있을까 해서.
여: 물론이지. 내가 짠 일정을 보내 줄게.""",
14: """[휴대폰이 울린다.]
여: 안녕, Mike. 무슨 일이야?
남: 안녕, Victoria. 네 조언이 필요해. 너 예전에 식당 운영했었지?
여: 응. 무슨 일인데?
남: 지난달에 피자 가게 연 거 알지? 그런데 잘 안 되고 있어.
여: 아, 좀 더 자세히 말해 줄래?
남: 와 본 사람들은 음식을 정말 좋아했는데 손님이 기대만큼 많지 않아.
여: 그럼 관심을 못 받고 있는 게 문제 같아. 사람들의 관심을 끌 무언가를 해야 해.
남: 어떻게? 제안할 만한 거 있어?
여: 사실 요즘 사람들은 온라인 후기에 많이 의존해. 그러니까 후기가 많으면 더 많은 사람이 관심을 가질 수도 있어.
남: 맞아. 그럼 손님들이 후기를 쓰게 하려면 어떻게 해야 할까?
여: 자기 소셜 미디어에 후기를 올리는 사람들에게 사이드 메뉴를 무료로 줄 수 있지.
남: 좋다. 그러면 더 많은 사람이 우리 가게를 알게 될 수 있겠어.""",
15: """남: Emily와 Ryan은 친한 친구이다. 오늘 마을에서 지역 축제가 열려서 Emily와 Ryan은 방과 후에 함께 구경하러 가고 싶어 한다. 축제에 도착하니 흥미로워 보이는 부스가 많다. Ryan은 모든 것을 보고 싶어 해서, 두 사람은 어느 부스에서도 시간을 많이 보내지 않고 계속 돌아다니기만 한다. 그런데 Emily는 축제가 끝나기까지 한 시간 정도밖에 남지 않았다는 것을 깨닫고, 이렇게 해서는 축제를 즐기지 못할 것이라고 걱정한다. 그래서 Emily는 둘 다 관심 있는 부스 몇 곳을 골라 그곳에서 더 많은 시간을 보내자고 제안하고 싶다. 이런 상황에서 Emily가 Ryan에게 할 말로 가장 적절한 것은 무엇인가?
Emily: 우리가 좋아하는 부스 몇 곳을 골라서 더 즐기는 게 어때?""",
16: """여: 학생 여러분, 안녕하세요. 지난 시간에는 일상생활 속 경제에 대해 이야기했습니다. 오늘은 색깔과 관련된 경제 용어 몇 가지를 소개하려고 합니다. 먼저, 정지 표지판처럼 경제에서 빨간색은 흔히 경고와 위험을 나타냅니다. 그래서 어떤 기업이 'in the red(적자 상태)'라면 돈을 잃고 있다는 뜻입니다. 둘째로 파란색이 있습니다. 파란색은 안전하고 믿을 만한 것을 뜻해서, 'blue-chip stock(우량주)'은 투자하기에 안전하다고 여겨지는 크고 안정적인 회사의 주식을 가리킵니다. 다음으로 초록색은 자연과 장기적인 성장과 연결됩니다. 예를 들어 'green investment(녹색 투자)'는 재생 에너지나 전기 자동차처럼 자연을 보호하려는 사업에 투자하는 것입니다. 마지막으로 흰색은 순수함과 정직함을 상징하기 때문에 흔히 합법적인 활동을 가리킵니다. 그래서 'white market(공개 시장)'은 기업들이 정부 규칙을 따르고 제품의 품질을 보장하는 시장입니다. 흥미롭지 않나요? 이제 이 용어들을 더 잘 이해하기 위해 기사 몇 개를 읽어 봅시다.""",
}
VOC = {
1: [('announcement','안내 방송'),('management office','관리 사무소'),('ensure','보장하다'),('posted','게시된'),('speed limit','제한 속도'),('designated','지정된'),('bike lane','자전거 전용 도로'),('injury','부상'),('cooperation','협조')],
2: [('look up','(사전 등에서) 찾아보다'),('follow','(내용을) 따라가다'),('individual','개별의'),('disrupt','방해하다, 끊다'),('flow','흐름'),('lose one’s place','어디까지 읽었는지 잊다'),('main idea','요지'),('unfamiliar','낯선')],
3: [('background music','배경 음악'),('affect','영향을 미치다'),('simply put','간단히 말해'),('raise one’s voice','목소리를 높이다'),('compete with','~와 경쟁하다'),('direct','직설적인'),('gentle','부드러운'),('set the mood','분위기를 만들다'),('stay tuned','채널을 고정하다')],
4: [('workshop','체험 교실'),('banner','현수막'),('striped','줄무늬의'),('apron','앞치마'),('microwave','전자레인지'),('melt','녹이다'),('ingredient','재료'),('star-shaped','별 모양의'),('shelf','선반')],
5: [('busking','버스킹, 거리 공연'),('fully charged','완전히 충전된'),('extra','여분의'),('in case','~할 경우에 대비해'),('instrument','악기'),('main building','본관'),('broadcasting club','방송반'),('announce','안내 방송을 하다')],
6: [('towel set','수건 세트'),('premium','고급의'),('organic cotton','유기농 면'),('sensitive skin','민감한 피부'),('hair treatment','헤어 트리트먼트'),('moisturizing','보습의'),('coupon','쿠폰'),('total','총액')],
7: [('exhausted','기진맥진한'),('relieve stress','스트레스를 풀다'),('stand-up comedy','스탠드업 코미디'),('make it','(시간에) 가다, 참석하다'),('graduate school','대학원'),('semester','학기'),('coworker','동료'),('transfer','옮기다'),('farewell party','송별회')],
8: [('flyer','전단'),('wave','파도'),('beginner','초보자'),('tiring','피곤하게 만드는'),('class size','수업 인원'),('maximum','최대'),('instructor','강사'),('equipment','장비'),('reasonable','적당한')],
9: [('ancient','고대의'),('castle','성'),('royal family','왕가'),('tower','탑'),('breathtaking','숨이 멎을 듯한'),('souvenir','기념품'),('bookmark','책갈피'),('limited','한정된'),('in advance','미리')],
10: [('laundry basket','빨래 바구니'),('option','선택지'),('inconvenient','불편한'),('fill up','가득 차다'),('material','소재'),('durable','튼튼한'),('handle','손잡이'),('match','맞다')],
11: [('presentation','발표'),('slide','슬라이드'),('put together','합치다'),('final check','최종 확인')],
12: [('reservation','예약'),('company event','회사 행사'),('book','예약하다'),('staff member','직원'),('update','변경하다')],
13: [('historic site','유적지'),('traditional','전통의'),('scenic viewpoint','경치 좋은 전망대'),('make sure','반드시 ~하게 하다'),('exhausted','기진맥진한'),('wedding anniversary','결혼기념일'),('relaxing','여유로운'),('share','공유하다')],
14: [('run','운영하다'),('specific','구체적인'),('customer','손님'),('attention','관심'),('attract','끌다'),('rely on','~에 의존하다'),('review','후기'),('encourage','장려하다'),('side menu','사이드 메뉴'),('post','올리다')],
15: [('local festival','지역 축제'),('take place','열리다'),('booth','부스'),('move around','돌아다니다'),('realize','깨닫다'),('worry','걱정하다'),('pick','고르다'),('suggest','제안하다')],
16: [('economics','경제학'),('term','용어'),('signal','나타내다'),('in the red','적자 상태인'),('reliable','믿을 만한'),('blue-chip stock','우량주'),('invest','투자하다'),('long-term growth','장기적 성장'),('renewable energy','재생 에너지'),('legal','합법적인'),('purity','순수함'),('guarantee','보장하다')],
}
