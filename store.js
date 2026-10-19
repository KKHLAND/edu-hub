// 관리 페이지에서 고친 앱 목록을 브라우저에 임시 저장하고, apps.js 파일로 내보내는 기능
const Store = (() => {
  const KEY = "eduhub-draft-v1";

  function load() {
    try {
      const raw = localStorage.getItem(KEY);
      if (!raw) return null;
      const data = JSON.parse(raw);
      return Array.isArray(data.apps) ? data : null;
    } catch {
      return null;
    }
  }

  function save(apps, owner) {
    try {
      localStorage.setItem(KEY, JSON.stringify({ apps, owner, savedAt: Date.now() }));
      return true;
    } catch {
      return false;
    }
  }

  function clear() {
    try {
      localStorage.removeItem(KEY);
    } catch {}
  }

  // 사이트가 실제로 보여줄 목록: 임시 저장본이 있으면 그것, 없으면 apps.js
  function current() {
    const draft = load();
    return {
      apps: draft ? draft.apps : APPS,
      owner: draft && draft.owner ? draft.owner : MY_NAME,
      isDraft: !!draft,
    };
  }

  function toAppsJs(apps, owner) {
    const head = `// eduhub 앱 데이터 (관리 페이지에서 내보냄: ${new Date().toLocaleString("ko-KR")})
// 이 파일은 admin.html(앱 관리)에서 고친 뒤 내려받아 교체하는 것을 권장합니다.
// needsKey: true = Gemini API 키가 있어야 쓸 수 있는 앱 / false = 키 없이 바로 쓰는 앱
// category: ${Object.entries(CATEGORIES).map(([k, v]) => `${k}(${v.label})`).join(" | ")}
// url: 실제 앱 주소 ("#"이면 아직 연결 전)
`;
    return (
      head +
      `const MY_NAME = ${JSON.stringify(owner)};\n\n` +
      `const APPS = ${JSON.stringify(apps, null, 2)};\n\n` +
      `const CATEGORIES = ${JSON.stringify(CATEGORIES, null, 2)};\n`
    );
  }

  // 내보낸 apps.js 또는 JSON 파일에서 앱 목록 읽기
  function parseFile(text) {
    const trimmed = text.trim();
    if (trimmed.startsWith("[")) return { apps: JSON.parse(trimmed) };
    if (trimmed.startsWith("{")) return JSON.parse(trimmed);
    const apps = text.match(/const APPS = (\[[\s\S]*?\n\]);/);
    const owner = text.match(/const MY_NAME = (".*?");/);
    if (!apps) throw new Error("앱 목록을 찾지 못했어요. 관리 페이지에서 내보낸 파일인지 확인해 주세요.");
    return { apps: JSON.parse(apps[1]), owner: owner ? JSON.parse(owner[1]) : undefined };
  }

  // ---------- 내 앱: 선생님이 메인 화면에서 직접 추가한 앱 (심사 없이 이 브라우저에만 저장) ----------
  const MY_KEY = "eduhub-my-apps-v1";

  function loadMine() {
    try {
      const data = JSON.parse(localStorage.getItem(MY_KEY) || "[]");
      return Array.isArray(data) ? data : [];
    } catch {
      return [];
    }
  }

  function saveMine(apps) {
    try {
      localStorage.setItem(MY_KEY, JSON.stringify(apps));
      return true;
    } catch {
      return false;
    }
  }

  return { load, save, clear, current, toAppsJs, parseFile, loadMine, saveMine };
})();
