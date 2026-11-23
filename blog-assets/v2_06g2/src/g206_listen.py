# 2026 6월 고2 듣기 1~17 — 발문·선택지·해석·어휘 (교사 작성 해석)
import re
Q = {
1: ('다음을 듣고, 여자가 하는 말의 목적으로 가장 적절한 것을 고르시오.', ['보건실 이용 방법을 설명하려고', '학교 급식 도우미를 모집하려고', '급식 만족도 조사 참여를 독려하려고', '학교 웹사이트 주소 변경을 알려주려고', '학교 구내식당 운영 중단 계획을 공지하려고']),
2: ('대화를 듣고, 남자의 의견으로 가장 적절한 것을 고르시오.', ['꾸준한 복습은 좋은 학습 습관 형성에 필수적이다.', '친구와 함께 공부하는 것은 학습 동기를 높여 준다.', '스스로 문제를 만들어 보는 것은 학습에 도움이 된다.', '약간의 소음 속에서의 학습은 집중력을 길러줄 수 있다.', '다양한 문제를 푸는 것은 문제 해결력 향상에 효과적이다.']),
3: ('다음을 듣고, 여자가 하는 말의 요지로 가장 적절한 것을 고르시오.', ['컴퓨터 화면을 오래 볼 때는 규칙적인 눈의 휴식이 필요하다.', '컴퓨터 사용 후 가벼운 스트레칭은 자세 교정에 도움을 준다.', '눈의 건조 증상을 막으려면 실내 습도를 조절하는 것이 좋다.', '컴퓨터 화면과 눈의 거리를 적절히 유지하는 것이 중요하다.', '숙면을 위해 취침 전 전자기기 사용을 자제해야 한다.']),
4: ('대화를 듣고, 그림에서 대화의 내용과 일치하지 않는 것을 고르시오.', None),
5: ('대화를 듣고, 남자가 할 일로 가장 적절한 것을 고르시오.', ['의자 배치하기', '포스터 부착하기', '강당 청소하기', '마이크 교체하기', '유인물 출력하기']),
6: ('대화를 듣고, 남자가 지불할 금액을 고르시오.', ['$36', '$45', '$50', '$54', '$60']),
7: ('대화를 듣고, 여자가 Sun Beach Cleanup Event에 가지 않은 이유를 고르시오.', ['감기에 걸려서', '조별 발표가 있어서', '동아리 면접을 봐야 해서', '밀린 과제를 끝내야 해서', '삼촌과 점심 식사가 있어서']),
8: ('대화를 듣고, Stonefield Drawing Picnic에 관해 언급되지 않은 것을 고르시오.', ['장소', '날짜', '준비물', '참가비', '기념품']),
9: ('2026 Future Innovation Expo에 관한 다음 내용을 듣고, 일치하지 않는 것을 고르시오.', ['10월 3일부터 5일까지 개최된다.', '올해의 주제는 미래 교통수단이다.', '첫날 오전 11시에 강연이 진행된다.', '자율주행차를 타볼 수 있다.', '티켓은 현장에서 구매할 수 있다.']),
10: ('다음 표를 보면서 대화를 듣고, 남자가 주문할 컴퓨터 마우스를 고르시오.', None),
11: ('대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오.', ['I usually buy my skateboards online.', 'Skateboards are too expensive these days.', 'You should’ve gotten some tips before buying it.', 'You can borrow my new board if you like it so much.', 'I couldn’t ride it anymore because it broke completely.']),
12: ('대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오. [3점]', ['I agree. It might be a good way to motivate me to run.', 'Great idea. That’s the best running route I’ve taken.', 'Right. You should definitely try running a marathon.', 'I’m sorry. I’ve already finished running for today.', 'Don’t worry. I’ll keep you motivated every day.']),
13: ('대화를 듣고, 남자의 마지막 말에 대한 여자의 응답으로 가장 적절한 것을 고르시오. [3점]', ['Great idea! Then I can try it first without buying anything.', 'My pleasure. I don’t need my old camping gear anymore.', 'You’re right. Thanks to you, I enjoyed this camping trip a lot.', 'Too bad. If I were you, I would find a better campsite.', 'I don’t think so. You should’ve booked it in advance.']),
14: ('대화를 듣고, 여자의 마지막 말에 대한 남자의 응답으로 가장 적절한 것을 고르시오.', ['Sorry. You should’ve prepared the handouts earlier.', 'Great. Then I won’t have to worry about printing.', 'No thanks. I’ve already checked the data.', 'That’s odd. My printer is working fine today.', 'Good for you. The presentation turned out great.']),
15: ('다음 상황 설명을 듣고, Ethan이 Chloe에게 할 말로 가장 적절한 것을 고르시오. [3점]', ['Let me send you last year’s film through email.', 'Let’s have students email their videos directly to us.', 'How about using an online platform to edit the videos?', 'You should make a shared folder before collecting the videos.', 'Why don’t we share our ideas with council members online?']),
}
Q16 = ('남자가 하는 말의 주제로 가장 적절한 것은?', ['how colors affect the performance of athletes', 'various colors used in sports brand marketing', 'role of colors in sports team logo design', 'why sports fans prefer certain team colors', 'historical roots of color usage in team uniforms'])
Q17 = ('언급된 색깔이 아닌 것은?', ['red', 'blue', 'purple', 'green', 'black'])
TABLE10 = '| | Model | Price | Color | Connection Type | Silent Click |\n| :-: | :-: | :-: | :-: | :-: | :-: |\n| ① | A | $28 | pink | wired | × |\n| ② | B | $32 | white | wired | ○ |\n| ③ | C | $35 | black | wireless | × |\n| ④ | D | $38 | pink | wireless | ○ |\n| ⑤ | E | $45 | black | wireless | ○ |'
ANSLINE = {
11: "W: I couldn’t ride it anymore because it broke completely.",
12: "M: I agree. It might be a good way to motivate me to run.",
13: "W: Great idea! Then I can try it first without buying anything.",
14: "M: Great. Then I won’t have to worry about printing.",
15: "Ethan: Let’s have students email their videos directly to us.",
}
FIX = [('stripepatterned', 'stripe-patterned'), ('ecofriendly', 'eco-friendly'), ('selfdriving', 'self-driving'),
       ('bestselling', 'best-selling')]


def load_sc(path='lp_join.txt'):
    t = open(path).read()
    for a, b in FIX: t = t.replace(a, b)
    SC = {}
    parts = re.split(r'\n(?=\d{1,2}\. |\[16~17\])', '\n' + t)
    for p in parts:
        p = p.strip()
        if not p: continue
        if p.startswith('[16~17]'):
            SC[16] = '\n'.join(l for l in p.split('\n')[1:] if l.startswith('M:'))
            continue
        m = re.match(r'(\d{1,2})\. ', p)
        n = int(m.group(1))
        if n > 15: continue
        lines = [l for l in p.split('\n')[1:] if l.strip() and not re.match(r'^(M|W):\s*$', l.strip())]
        if n in ANSLINE: lines.append(ANSLINE[n])
        SC[n] = '\n'.join(lines)
    return SC


KO = {
1: """여: 안녕하세요, Robinson 고등학교 학생 여러분. 교장입니다. 여러분 모두에게 중요한 공지가 있습니다. 대규모 공사로 인해 학교 구내식당을 폐쇄할 계획입니다. 구내식당이 안전 기준을 충족하고 늘어나는 학생 수를 위한 충분한 공간을 마련하려면 대대적인 개선이 필요하기 때문에 이 공사는 꼭 필요합니다. 이번 주 토요일부터 한 달 동안 구내식당을 이용할 수 없습니다. 이번 폐쇄가 여러분의 점심시간 일과에 영향을 주리라는 것을 잘 압니다. 그래서 불편을 최소화하기 위해 신중하게 계획을 세웠습니다. 폐쇄에 관한 최신 소식과 자세한 내용은 학교 웹사이트에서 확인해 주세요. 이해해 주셔서 감사합니다.""",
2: """남: Sarah, 속상해 보이는구나. 무슨 일이니?
여: Johnson 선생님, 역사 시험 공부를 많이 했어요. 교과서를 여러 번 읽었는데도 점수가 낮게 나왔어요.
남: 그렇구나. 공부하면서 직접 문제를 만들어 본 적 있니?
여: 아니요, 없어요. 그게 도움이 되나요?
남: 그럼. 스스로 문제를 만들면 학습에 정말 도움이 돼.
여: 저는 잘 모르는 부분을 더 많이 읽는 게 낫다고 생각했어요.
남: 사실 문제를 만들다 보면 아직 이해하지 못한 것을 찾게 돼. 그렇게 하면 모르는 것을 확인할 수 있지.
여: 그건 생각해 보지 못했어요.
남: 게다가 그렇게 하면 읽은 내용을 깊이 생각하게 돼. 내용을 더 잘 익히는 데 도움이 되지.
여: 정말 일리가 있네요.
남: 그래서 스스로 문제를 만들어 보는 게 도움이 되는 거란다.
여: 알겠어요. 다음번에는 그렇게 해 볼게요.""",
3: """여: 청취자 여러분, 안녕하세요! Daily Health Tips의 Danielle입니다. 직장에서 오랜 시간 컴퓨터 앞에 앉아 계시나요? 오늘은 컴퓨터 화면으로부터 눈에 규칙적인 휴식을 주는 것이 왜 필요한지 이야기하려 합니다. 화면을 너무 오래 보면 안구 건조, 흐린 시야, 두통이 생길 수 있습니다. 이런 증상은 집중하고 생산적으로 일하기 어렵게 만듭니다. 눈에 규칙적인 휴식을 주면 눈이 긴장을 풀고 회복할 수 있습니다. 그러면 시력 문제나 신체적 불편이 줄고 업무 효율이 높아집니다. 다음에 컴퓨터 화면을 오래 보고 있는 자신을 발견하면, 눈을 위해 쉬는 것을 잊지 마세요!""",
4: """남: Williams 선생님, 새 교직원 건강 휴게실을 꾸미고 계신다고 들었어요. 어떻게 되어 가요?
여: 거의 다 됐어요, Thompson 선생님. 여기 사진이에요.
남: 어디 봐요. [잠시 후] 와! 방에 실내 자전거가 있네요.
여: 맞아요. 이 실내 자전거를 타면 건강을 증진하는 데 도움이 될 것 같았어요.
남: 바닥에 있는 줄무늬 매트는 뭐예요?
여: 아, 스트레칭이나 요가를 하고 싶은 사람들을 위한 거예요. 벽에 있는 둥근 거울 보이세요?
남: 네. 자세를 확인하는 데 쓸 수 있겠네요.
여: 바로 그거예요! 이 안마의자 두 개는 어때요?
남: 정말 편안해 보여요.
여: 편해요. 긴 하루를 보낸 뒤 쉴 때 쓸 수 있어요.
남: 좋네요. 탁자 위 꽃병도 정말 마음에 들어요.
여: 계절 꽃이 모두의 기분을 좋게 해 줄 거라고 생각했어요.
남: 빨리 이 방을 써 보고 싶네요!""",
5: """여: 김 선생님, 신입생 오리엔테이션이 내일 아침이에요. 거의 다 왔네요.
남: 네. 모든 게 잘 되면 좋겠어요. 마지막으로 한 번 더 준비한 것을 점검해 봐요.
여: 좋아요. 저는 신입생들이 앉을 의자 배치를 끝냈어요.
남: 좋아요. 저는 강당에 환영 포스터를 이미 붙였어요.
여: 완벽해요. 유인물은 출력하셨어요?
남: 네, 했어요. 오늘 아침에 출력했어요.
여: 그럼 대부분 준비된 것 같네요.
남: 사실 강당에서 마이크를 시험해 봤는데 제대로 작동하지 않았어요.
여: 오리엔테이션 도중에 심각한 문제가 될 수 있겠네요.
남: 걱정 마세요. 제가 교체할게요. 다른 마이크가 있거든요.
여: 고마워요. 그동안 저는 강당이 깨끗한지 확인할게요.""",
6: """여: Jenny’s Flowers에 오신 것을 환영합니다. 무엇을 도와드릴까요?
남: 안녕하세요. 아내 생일에 특별한 걸 사 주고 싶어요. 추천해 주실 만한 게 있나요?
여: 이 생화 바구니는 어떠세요? 두 가지 크기가 있어요.
남: 예쁘네요. 얼마예요?
여: 작은 것은 30달러, 큰 것은 50달러예요.
남: 음, 큰 게 더 좋아 보이네요. 큰 바구니 하나 살게요.
여: 좋은 선택이에요. 바구니에 이 곰 인형도 추가하실 수 있어요. 하나에 5달러밖에 안 해요.
남: 귀엽네요. 두 개 추가할게요.
여: 네. 그럼 곰 인형 두 개가 든 큰 꽃바구니 하나, 맞으시죠?
남: 네. 그리고 이 쿠폰으로 할인받을 수 있나요?
여: 물론이죠. 전체 금액에서 10% 할인받으실 수 있어요.
남: 잘됐네요. 여기 신용카드요.""",
7: """남: Julia, 지난 토요일 Sun Beach 정화 행사에 안 왔더라.
여: 응, 빠져서 마음이 안 좋았어.
남: 몸이 안 좋았나 생각했어. 지난주에 감기 걸렸다고 들었거든.
여: 걸렸었는데, 토요일에는 괜찮았어.
남: 그럼 조별 과제 회의가 있었니?
여: 아니, 그건 사실 금요일이었고 우리 다 끝냈어.
남: 아, 기억났다! 동아리 면접이 있다고 했잖아. 그게 늦게 끝났니?
여: 그건 연기돼서 그것도 이유가 아니었어.
남: 그럼 왜 못 왔어?
여: 그날 삼촌이 오셨어. 삼촌을 뵌 지 오래돼서 같이 점심을 먹었어.
남: 아, 그래서 못 왔구나.""",
8: """여: 안녕, Dave! 뭐 하고 있어?
남: 안녕, Emma. 우리 미술 동아리가 Stonefield Drawing Picnic을 열어서 포스터를 붙이고 있어.
여: 그림 소풍? 재미있겠다. 좀 볼게.
남: Stonefield 공원에서 해. 거기 모여서 소풍도 하고 같이 그림을 그릴 거야. 너도 와.
여: 아, Stonefield 공원은 우리 집이랑 가까워! 10월 22일이네.
남: 응, 맞아. 그날 시간 있어?
여: 아직 계획은 없어. 그런데 참가비가 있다고 쓰여 있네.
남: 응, 5달러밖에 안 해. 그리고 참가만 해도 모두 기념품을 받아.
여: 기념품? 뭔데?
남: 그림 그리기용 미술 도구 세트야. 정말 재미있을 거야. 약속해!
여: 좋다. 꼭 갈게.""",
9: """남: 안녕하세요, 저는 Westbridge 컨벤션 홀의 관리자 Mike입니다. 저희가 2026 Future Innovation Expo를 개최하게 되었음을 알려 드리게 되어 기쁩니다. 박람회는 10월 3일부터 5일까지 열립니다. 올해의 주제는 미래 교통수단입니다. 단돈 20달러로 세계 최고 브랜드들의 최신 차량 기술을 둘러보실 수 있습니다. 첫날 오전 11시에는 이지훈 박사님이 친환경 모빌리티에 관해 강연합니다. 친환경 차량의 미래를 볼 좋은 기회가 될 것입니다. 그리고 진짜 하이라이트가 있습니다. 자율주행차를 타 볼 수 있습니다. 박람회 티켓은 수량이 한정되어 있으니 일찍 구하시는 게 좋습니다. 티켓은 온라인으로만 구매할 수 있습니다. 더 많은 정보는 저희 웹사이트를 방문해 주세요. 감사합니다.""",
10: """남: Mia, 온라인에서 가장 잘 팔리는 컴퓨터 마우스 모델들을 보고 있어. 하나 고르는 것 좀 도와줄래?
여: 물론이지. 같이 보자. 예산은 얼마야?
남: 40달러 미만이면 좋겠어.
여: 그래, 그럼 그보다 비싼 건 빼자. 이제 무슨 색이 좋아?
남: 흰색만 아니면 돼. 쉽게 더러워지거든. 그리고 연결 방식은 잘 모르겠어.
여: 대부분 사람들은 무선이 더 편하다고 해.
남: 그럼 무선으로 할게. 두 가지가 남은 것 같네.
여: 무소음 클릭이 되는 걸 추천해. 딸깍거리는 소리가 크면 신경 쓰일 수 있거든.
남: 맞아. 무소음 클릭이 더 낫겠다.
여: 그렇다면 네 조건에 맞는 모델은 하나뿐이야.
남: 좋아. 그걸로 주문할게.""",
11: """남: 안녕, Linda. 그거 새 스케이트보드야? 멋지다!
여: 고마워, Glen. 최근에 샀어. 예전 보드를 바꿔야 했거든.
남: 예전 보드는 어떻게 됐는데?
여: 완전히 부서져서 더 이상 탈 수 없었어.""",
12: """여: 안녕, Charlie. 지난번에 매일 아침 달리기를 시작했다고 했잖아. 어떻게 돼 가?
남: 음, 몇 주 해 봤는데 혼자서는 의욕을 유지하기가 힘들더라.
여: 바로 그 이유로 나는 지역 달리기 동호회에 가입했어. 너한테도 도움이 될 것 같아.
남: 동감이야. 달리기 의욕을 북돋는 좋은 방법이 될 수도 있겠다.""",
13: """여: 안녕, Max. 너 캠핑 자주 가지?
남: 무슨 일이야, Jamie? 응, 가족이랑 주말마다 캠핑해. 왜 물어?
여: 나도 한번 해 볼까 생각 중이야. 재미있어 보여서.
남: 정말 좋다!
여: 응, 그런데 사야 할 캠핑 장비가 너무 많아서 부담돼.
남: 이해해. 나도 처음엔 필요한 게 아주 많다고 생각했어. 하지만 시작하는 데 모든 게 필요하지는 않아.
여: 정말?
남: 응. 중요한 물건 몇 개만 사서 시작해 보고 어떤지 보면 돼. 나머지는 정말 필요하면 나중에 사면 되고.
여: 그건 할 만하겠다. 그래도 캠핑 장비는 비싸잖아. 몇 개 샀는데 캠핑이 나랑 안 맞으면 어떡해?
남: 음, 확신이 없다면, 이미 장비가 있는 사람이랑 같이 캠핑을 가 보는 건 어때?
여: 좋은 생각이야! 그러면 아무것도 사지 않고 먼저 해 볼 수 있겠다.""",
14: """여: Jason, 내일 회의에서 네가 발표를 맡았다고 들었어.
남: 응, 맞아. 일주일 내내 준비하고 있어.
여: 어떻게 돼 가?
남: 꽤 잘 돼 가. 발표 슬라이드는 다 끝냈어.
여: 잘됐다. 데이터랑 차트는 확인했어?
남: 응, 오늘 아침에 숫자가 맞는지 전부 검토했어.
여: 그럼 거의 준비가 된 것 같네.
남: 나도 그렇게 생각했는데, 걱정되는 게 하나 있어.
여: 아, 정말? 뭔가 잘못됐어?
남: 내 사무실 프린터가 갑자기 고장 나서, 지금 발표 유인물을 출력할 수가 없어.
여: 원하면 내 사무실에서 내가 출력해 줄게.
남: 잘됐다. 그럼 출력 걱정은 안 해도 되겠네.""",
15: """여: Ethan과 Chloe는 학생회 임원입니다. 다가오는 졸업식의 일환으로, 그들은 특별한 영상을 만들고 싶어 합니다. 작년에 그들은 학생들이 찍은 짧은 영상들로 이루어진 영상을 만들었고, 그것은 정말 인기가 많았습니다. 그래서 같은 아이디어를 쓰기로 했습니다. 영상을 모으기 위해 Chloe는 모두가 자유롭게 올릴 수 있도록 작년처럼 온라인 공유 폴더를 만들자고 제안합니다. 하지만 Ethan은 작년에 몇몇 사람들이 허락 없이 영상을 사용해서 문제가 있었던 것을 기억합니다. 그는 그런 일을 피하고 싶습니다. 그래서 Ethan은 Chloe에게 이메일을 이용해 학생들의 영상을 모으자고 제안하고 싶습니다. 이 상황에서, Ethan이 Chloe에게 할 말로 가장 적절한 것은 무엇입니까?
Ethan: 학생들에게 영상을 우리에게 직접 이메일로 보내 달라고 하자.""",
16: """남: 학생 여러분, 안녕하세요. 지난주에 우리는 색깔이 사람들의 기분에 미치는 영향에 대해 간단히 배웠습니다. 오늘은 색깔이 스포츠에서 선수들의 경기력에 영향을 주는 방식을 살펴보겠습니다. 첫째, 빨간색은 선수의 에너지를 끌어올리고 경기 중 더 과감하게 행동하도록 밀어붙일 수 있습니다. 빨간색은 흔히 신체적 노력을 늘리는데, 이것은 빠르거나 공격적인 스포츠에 도움이 될 수 있습니다. 둘째, 접전에서 선수들이 압박 속에서도 침착함을 유지하도록 돕는 데는 파란색이 유용합니다. 파란색은 또한 명료한 사고를 도와 경기에서 더 나은 선택으로 이어질 수 있습니다. 셋째, 초록색은 균형감을 주고 꾸준한 속도를 유지하도록 북돋습니다. 이 색은 스트레스도 줄여 주어, 긴 경기 동안 선수들이 긴장을 풀고 있도록 돕습니다. 마지막으로, 힘과 강한 존재감은 검은색과 연결됩니다. 검은색은 선수들이 경기할 때 더 자신감을 느끼도록 도울 수 있습니다. 이제 스포츠 팀들이 선수들에게 도움이 되도록 이 색깔들을 어떻게 활용하는지 보여 주는 세계 여러 나라의 사례를 살펴봅시다.""",
}

VOC = {
1: [('principal', '교장'), ('announcement', '공지, 발표'), ('construction', '공사'), ('cafeteria', '구내식당'), ('significant', '상당한'), ('upgrade', '개선, 개량'), ('safety standard', '안전 기준'), ('closure', '폐쇄'), ('impact', '영향을 주다'), ('minimize', '최소화하다')],
2: [('frustrated', '속상한, 좌절한'), ('textbook', '교과서'), ('score', '점수'), ('create', '만들다'), ('check', '확인하다'), ('content', '내용'), ('make sense', '일리가 있다'), ('for oneself', '스스로')],
3: [('regular', '규칙적인'), ('rest', '휴식'), ('dry eyes', '안구 건조'), ('vision', '시력, 시야'), ('symptom', '증상'), ('concentrate', '집중하다'), ('productive', '생산적인'), ('recover', '회복하다'), ('discomfort', '불편'), ('efficiency', '효율')],
4: [('decorate', '꾸미다'), ('staff', '직원'), ('wellness', '건강'), ('exercise bike', '실내 자전거'), ('stripe-patterned', '줄무늬가 있는'), ('posture', '자세'), ('massage chair', '안마의자'), ('vase', '꽃병'), ('seasonal', '계절의'), ('lift one’s mood', '기분을 좋게 하다')],
5: [('freshman', '신입생'), ('orientation', '오리엔테이션'), ('go over', '점검하다'), ('arrange', '배치하다'), ('put up', '붙이다'), ('auditorium', '강당'), ('handout', '유인물'), ('properly', '제대로'), ('replace', '교체하다')],
6: [('recommend', '추천하다'), ('basket', '바구니'), ('fresh flower', '생화'), ('teddy bear', '곰 인형'), ('as well', '또한'), ('cost', '(비용이) 들다'), ('coupon', '쿠폰'), ('discount', '할인'), ('total price', '총액')],
7: [('show up', '나타나다'), ('cleanup', '정화, 청소'), ('feel bad', '마음이 안 좋다'), ('have a cold', '감기에 걸리다'), ('group project', '조별 과제'), ('mention', '말하다, 언급하다'), ('run late', '늦게 끝나다'), ('postpone', '연기하다'), ('keep A from -ing', 'A가 ~하지 못하게 하다'), ('make it', '가다, 참석하다')],
8: [('host', '개최하다'), ('put up', '붙이다, 게시하다'), ('gather', '모이다'), ('free', '한가한'), ('participation fee', '참가비'), ('souvenir', '기념품'), ('art supply', '미술 도구'), ('definitely', '꼭, 반드시')],
9: [('convention hall', '컨벤션 홀'), ('innovation', '혁신'), ('expo', '박람회'), ('theme', '주제'), ('transportation', '교통수단'), ('vehicle', '차량'), ('deliver a lecture', '강연하다'), ('eco-friendly', '친환경적인'), ('self-driving car', '자율주행차'), ('limited', '한정된')],
10: [('best-selling', '가장 잘 팔리는'), ('budget', '예산'), ('prefer', '선호하다'), ('anything but', '~ 외에는 무엇이든'), ('connection type', '연결 방식'), ('wireless', '무선의'), ('convenient', '편리한'), ('silent click', '무소음 클릭'), ('distracting', '신경 쓰이게 하는'), ('meet one’s needs', '요구를 충족시키다')],
11: [('skateboard', '스케이트보드'), ('awesome', '멋진'), ('recently', '최근에'), ('replace', '교체하다'), ('board', '(스케이트)보드'), ('completely', '완전히'), ('borrow', '빌리다')],
12: [('motivated', '의욕이 있는'), ('on one’s own', '혼자서'), ('exact', '바로 그'), ('local', '지역의'), ('benefit from', '~에서 도움을 얻다'), ('motivate', '의욕을 북돋다'), ('route', '경로')],
13: [('camp', '캠핑하다'), ('overwhelmed', '부담을 느끼는'), ('equipment', '장비'), ('get started', '시작하다'), ('item', '물건'), ('the rest', '나머지'), ('doable', '할 만한'), ('expensive', '비싼'), ('gear', '장비')],
14: [('in charge of', '~을 맡은'), ('presentation', '발표'), ('slide', '슬라이드'), ('data', '데이터'), ('chart', '차트'), ('go over', '검토하다'), ('worried', '걱정하는'), ('suddenly', '갑자기'), ('at the moment', '지금은')],
15: [('student council', '학생회'), ('upcoming', '다가오는'), ('graduation ceremony', '졸업식'), ('consist of', '~으로 이루어지다'), ('propose', '제안하다'), ('shared folder', '공유 폴더'), ('upload', '올리다'), ('permission', '허락'), ('avoid', '피하다'), ('collect', '모으다')],
16: [('briefly', '간단히'), ('mood', '기분'), ('influence', '영향을 주다'), ('athlete', '운동선수'), ('performance', '경기력, 성과'), ('boldly', '과감하게'), ('aggressive', '공격적인'), ('under pressure', '압박 속에서'), ('steady pace', '꾸준한 속도'), ('presence', '존재감'), ('confident', '자신감 있는')],
}
