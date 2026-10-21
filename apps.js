// eduhub 앱 데이터
// 새 앱을 추가하려면 아래 배열에 객체 하나를 추가하세요.
// needsKey: true = Gemini API 키가 있어야 쓸 수 있는 앱 / false = 키 없이 바로 쓰는 앱
// category: plan(평가 계획) | exam(문항 출제) | review(출제 문항 검토) | cutoff(분할 점수 시뮬레이터)
//         | grading(평가 및 채점) | analysis(성적 분석) | record(생기부 과세특) | tools(기타 도구)
//   화면에는 아래 CATEGORIES에 적힌 순서대로 분류가 나오고, 앱도 그 순서로 정렬됩니다.
// author: 제작자 이름 — 다른 선생님 앱을 올릴 때 그 선생님 이름으로 적어 주세요.
// url: 실제 앱 주소로 바꿔 주세요. ("#"이면 아직 연결 전)
const MY_NAME = "KKHLAND";

const APPS = [
  // ==================== Gemini API 키 필요 ====================

  // ---------- 평가 계획 ----------
  {
    id: "teaching-plan",
    needsKey: true,
    name: "교수학습 및 평가 운영 계획 생성 시스템",
    category: "plan",
    emoji: "📅",
    desc: "교과별 교수학습 및 평가 운영 계획서를 양식에 맞춰 생성합니다.",
    tags: ["평가계획", "교수학습", "교육과정"],
    author: MY_NAME,
    url: "https://teaching-plan.ai.studio/",
  },

  // ---------- 문항 출제 ----------
  {
    id: "cross-subject-quiz",
    needsKey: true,
    name: "범교과 문항 출제 시스템",
    category: "exam",
    emoji: "🧩",
    desc: "수업 자료를 바탕으로 과목에 상관없이 문항을 생성하는 AI 문항 생성기입니다.",
    tags: ["문항출제", "자료기반", "전과목"],
    author: MY_NAME,
    url: "https://item-gen.ai.studio/",
  },

  // ---------- 출제 문항 검토 ----------
  {
    id: "item-check",
    needsKey: true,
    name: "출제 문항 점검 시스템",
    category: "review",
    emoji: "🔬",
    desc: "Gemini로 시험 문항의 오류, 난이도, 변별도 등을 분석·평가하는 출제 문항 점검 시스템입니다.",
    tags: ["문항점검", "난이도", "변별도", "Gemini"],
    author: MY_NAME,
    url: "https://item-analyser.ai.studio/",
  },

  // ---------- 분할 점수 시뮬레이터 ----------
  {
    id: "cutoff-simulator",
    needsKey: true,
    name: "분할점수 산출 시뮬레이터",
    category: "cutoff",
    emoji: "🎚️",
    desc: "고등학교 문항정보표, 지필평가 등의 데이터를 바탕으로 수정 에벨(Modified Ebel) 방식을 적용해 성취수준별 분할점수를 산출합니다.",
    tags: ["분할점수", "Ebel", "성취수준", "문항정보표"],
    author: MY_NAME,
    url: "https://cut-score-simulator.ai.studio/",
  },

  // ---------- 평가 및 채점 ----------
  {
    id: "essay-grader",
    needsKey: true,
    name: "서논술형 AI 채점 시스템",
    category: "grading",
    emoji: "🖋️",
    desc: "손글씨 답안지(PDF)를 스캔해 올리고 채점기준표(PDF/엑셀/텍스트)와 학생 명렬표를 제공하면 AI가 정교하게 자동 채점합니다.",
    tags: ["서논술형", "손글씨", "AI채점", "명렬표"],
    author: MY_NAME,
    url: "https://essay-greder.ai.studio/",
  },

  // ---------- 생기부 과세특 ----------
  {
    id: "record-500",
    needsKey: true,
    name: "생기부 작성 도우미 (500자)",
    category: "record",
    emoji: "📝",
    desc: "학생 활동 기록을 바탕으로 과목별 세부능력 및 특기사항 등 생기부 관련 자료를 500자 분량으로 생성합니다.",
    tags: ["세특", "생기부", "500자"],
    author: MY_NAME,
    url: "https://report-gen500.ai.studio/",
  },
  {
    id: "record-250",
    needsKey: true,
    name: "생기부 작성 도우미 (250자)",
    category: "record",
    emoji: "🗒️",
    desc: "학생 활동 기록을 바탕으로 과목별 세부능력 및 특기사항 등 생기부 관련 자료를 250자 분량으로 생성합니다.",
    tags: ["세특", "생기부", "250자"],
    author: MY_NAME,
    url: "https://report-gen250.ai.studio/",
  },
  {
    id: "record-mate",
    needsKey: true,
    name: "생기부 메이트",
    category: "record",
    emoji: "✅",
    desc: "AI 기반 맞춤법 검사와 생기부 바이트 계산으로 생기부 글쓰기를 다듬어 줍니다.",
    tags: ["생기부", "맞춤법", "바이트계산"],
    author: MY_NAME,
    url: "https://style-rewriting.ai.studio/",
  },
  {
    id: "worksheet-typer",
    needsKey: true,
    name: "손글씨/음성 타이퍼와 생기부 요약기",
    category: "record",
    emoji: "📄",
    desc: "PDF 손글씨 활동지와 음성을 텍스트로 옮기고 분석해 생활기록부 기재용으로 요약해 줍니다.",
    tags: ["손글씨", "음성", "활동지", "요약", "생기부"],
    author: MY_NAME,
    url: "https://handwrting-summarizer.ai.studio/",
  },
  {
    id: "interview-questions",
    needsKey: true,
    name: "학생부 활동·탐구 면접 질문 생성기",
    category: "record",
    emoji: "🎤",
    desc: "학생부에 기록된 활동명과 지원 분야를 입력하면 학업·탐구·공동체·성찰 역량 평가를 위한 면접 문항과 평가 기준을 만들어 줍니다.",
    tags: ["학생부", "면접", "탐구", "진로"],
    author: MY_NAME,
    url: "https://interview-gen.ai.studio/",
  },
  {
    id: "interview-lab",
    needsKey: true,
    name: "생기부 면접 Lab",
    category: "record",
    emoji: "🎯",
    desc: "학교생활기록부 PDF를 올리고 대학·학과를 고르면 입학사정관 시점의 생기부 리뷰, 맞춤 면접 질문·모범 답변·꼬리질문을 만들고 타이머·음성 답변으로 실전 연습까지 할 수 있습니다. (인적사항은 읽지 않음)",
    tags: ["면접", "학종", "생기부", "모범답변", "실전연습"],
    author: MY_NAME,
    url: "https://interview-gen-sigma.vercel.app",
  },

  // ---------- 기타 도구 ----------
  {
    id: "material-converter",
    needsKey: true,
    name: "학습 자료 자동 변환 시스템",
    category: "tools",
    emoji: "🔄",
    desc: "수업 자료·학습지·판서 사진·손글씨 필기·PDF·hwpx를 올리면 내용은 그대로 두고 제목·문단·표로 정리해 2단/1단 학습지 양식의 hwpx와 PDF로 만들어 줍니다.",
    tags: ["학습자료", "학습지", "hwpx", "손글씨"],
    author: MY_NAME,
    url: "https://auto-typer.ai.studio/",
  },
  {
    id: "slide-script",
    needsKey: true,
    name: "슬라이드 대본 생성기",
    category: "tools",
    emoji: "🎙️",
    desc: "슬라이드(PDF/PPTX)를 올리면 슬라이드마다 영상용 내레이션 대본을 만들고, 원하는 목소리로 바로 미리 들어볼 수 있습니다.",
    tags: ["슬라이드", "대본", "내레이션", "영상"],
    author: MY_NAME,
    url: "https://slide-script-gen.ai.studio/",
  },
  {
    id: "handwriting-ocr",
    needsKey: true,
    name: "손글씨 OCR 스튜디오",
    category: "tools",
    emoji: "✍️",
    desc: "손글씨 사진·스캔본·PDF를 올리면 문맥까지 고려해 손글씨를 판독하고, 마크다운 텍스트나 시험지·활동지 양식의 hwpx 문서로 내보내 줍니다.",
    tags: ["OCR", "손글씨", "hwpx", "활동지"],
    author: MY_NAME,
    url: "https://handwriting-ocr-gold.vercel.app/",
  },

  // ==================== 키 없이 바로 사용 ====================

  // ---------- 문항 출제 ----------
  {
    id: "examform-gen",
    needsKey: false,
    name: "출제안 양식 자동 생성기",
    category: "exam",
    emoji: "🗂️",
    desc: "학교 시험지 양식(.hwpx)을 올리면 표 레이아웃과 서식을 그대로 유지한 채 학교·과목·배점 정보를 채운 새 출제안을 만들어 줍니다.",
    tags: ["출제안", "hwpx", "시험지양식", "배점"],
    author: MY_NAME,
    url: "https://examform-gen.vercel.app",
  },

  // ---------- 성적 분석 ----------
  {
    id: "grade5",
    needsKey: false,
    name: "NEIS 내신 성적 분석기",
    category: "analysis",
    emoji: "📈",
    desc: "NEIS 성적 파일을 순서대로 올리면 5등급제 내신 성적을 과목·반·학생별로 분석하는 대시보드를 보여줍니다.",
    tags: ["NEIS", "5등급", "성적분석", "대시보드"],
    author: MY_NAME,
    url: "https://grade5.vercel.app",
  },

  // ---------- 생기부 과세특 ----------
  {
    id: "report-gen",
    needsKey: false,
    name: "과세특 리포트 생성기",
    category: "record",
    emoji: "🧾",
    desc: "나이스에서 내려받은 과세특 엑셀 파일을 올리면 학생별로 과목을 합쳐 인쇄용 개인 리포트를 만들어 줍니다.",
    tags: ["과세특", "나이스", "리포트", "인쇄"],
    author: MY_NAME,
    url: "https://report-gen-sage.vercel.app",
  },
  {
    id: "style-polishing",
    needsKey: false,
    name: "생기부 AI 티 제거·문체 교정기",
    category: "record",
    emoji: "✨",
    desc: "생기부 초안의 번역투·AI 관용구·접속사 남발·기재 불가 표현을 찾아 '~함' 명사형으로 다듬어 줍니다. 의미와 NEIS 바이트 분량은 그대로 두고, 나이스 엑셀 파일 일괄 교정도 지원합니다.",
    tags: ["생기부", "윤문", "AI티제거", "NEIS", "엑셀일괄"],
    author: MY_NAME,
    url: "https://style-polishing.vercel.app",
  },

  // ---------- 기타 도구 ----------
  {
    id: "textbook-selection",
    needsKey: false,
    name: "검·인정도서 선정 평가표 생성기",
    category: "tools",
    emoji: "📚",
    desc: "과목과 선정 위원을 고르면 2027학년도 검·인정 교과서 선정 평가표를 바로 만들어 줍니다.",
    tags: ["교과서", "검인정", "선정평가표"],
    author: MY_NAME,
    url: "https://textbook-selection.vercel.app",
  },
  {
    id: "textbook-certificate",
    needsKey: false,
    name: "교과서 신청 확인서 생성기",
    category: "tools",
    emoji: "📘",
    desc: "리로스쿨 선택과목 배정 원본 파일을 그대로 올리면 학생별 교과서 신청 확인서를 A4 한 장씩 만들어 줍니다.",
    tags: ["교과서", "리로스쿨", "확인서", "선택과목"],
    author: MY_NAME,
    url: "https://textbook-certificate.vercel.app",
  },
  {
    id: "school-calendar",
    needsKey: false,
    name: "스마트 스쿨 캘린더",
    category: "tools",
    emoji: "📅",
    desc: "학교 학사일정을 달력으로 한눈에 확인할 수 있습니다.",
    tags: ["학사일정", "캘린더"],
    author: MY_NAME,
    url: "https://school-calendar-one.vercel.app",
  },
  {
    id: "smart-planner",
    needsKey: false,
    name: "스마트 플래너",
    category: "tools",
    emoji: "🗓️",
    desc: "주간 목표와 요일별 계획, 수능 D-day를 관리하는 학생용 스마트 플래너입니다.",
    tags: ["플래너", "학생", "주간계획", "D-day"],
    author: MY_NAME,
    url: "https://smart-planner-sandy.vercel.app",
  },
  {
    id: "voca1800",
    needsKey: false,
    name: "EBS VOCA 1800",
    category: "tools",
    emoji: "🔤",
    desc: "EBS VOCA 1800 단어를 Day별 플래시카드로 학습합니다. (영단어→뜻 / 뜻→영단어)",
    tags: ["영어", "단어", "EBS", "플래시카드"],
    author: MY_NAME,
    url: "https://voca1800.vercel.app",
  },
  {
    id: "voca2500",
    needsKey: false,
    name: "EBS VOCA POWER 2500",
    category: "tools",
    emoji: "🅰️",
    desc: "VOCA POWER 고교필수어휘 2500을 Unit별 플래시카드로 학습합니다.",
    tags: ["영어", "단어", "EBS", "플래시카드"],
    author: MY_NAME,
    url: "https://voca2500.vercel.app",
  },
  {
    id: "markitdown-studio",
    needsKey: false,
    name: "마크다운 스튜디오",
    category: "tools",
    emoji: "Ⓜ️",
    desc: "PDF·워드·엑셀·PPT 등 문서를 AI 프롬프트에 바로 쓸 수 있는 마크다운으로 변환합니다. 표 구조를 보존하고 토큰 수도 알려줍니다.",
    tags: ["마크다운", "문서변환", "PDF", "프롬프트"],
    author: MY_NAME,
    url: "https://markitdown-studio-rho.vercel.app",
  },
  {
    id: "slide-cleaner",
    needsKey: false,
    name: "슬라이드 로고 클리너",
    category: "tools",
    emoji: "🧽",
    desc: "NotebookLM 등에서 만든 슬라이드 이미지·PDF의 우측 하단 워터마크를 브라우저 안에서 지워 줍니다. (최대 15장, 서버 전송 없음)",
    tags: ["슬라이드", "워터마크", "NotebookLM", "PDF"],
    author: MY_NAME,
    url: "https://slide-cleaner-eight.vercel.app",
  },
];

// 화면에 나오는 순서 = 아래 순서
// short: 상단 메뉴·분류 칩에 쓰는 짧은 이름 / hint: 분류 카드 아래 설명
const CATEGORIES = {
  plan: { label: "평가 계획", short: "평가 계획", hint: "평가 계획서 작성", color: "amber" },
  exam: { label: "문항 출제", short: "문항 출제", hint: "과목별 출제, 출제안 양식", color: "blue" },
  review: { label: "출제 문항 검토", short: "문항 검토", hint: "오류 점검, 난이도·변별도 분석", color: "indigo" },
  cutoff: { label: "분할 점수 시뮬레이터", short: "분할 점수", hint: "성취도 분할 점수 산출", color: "teal" },
  grading: { label: "평가 및 채점", short: "평가·채점", hint: "서술형·수행평가 채점", color: "pink" },
  analysis: { label: "성적 분석", short: "성적 분석", hint: "NEIS 성적 분석, 통계", color: "purple" },
  record: { label: "생기부 과세특", short: "과세특", hint: "세특 작성, 리포트", color: "green" },
  tools: { label: "기타 도구", short: "기타 도구", hint: "학습자료 제작, 업무 도구", color: "slate" },
};
