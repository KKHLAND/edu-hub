(() => {
  const $ = (sel) => document.querySelector(sel);
  const $$ = (sel) => document.querySelectorAll(sel);

  const grid = $("#grid");
  const empty = $("#empty");
  const searchInput = $("#searchInput");
  const modal = $("#modal");
  const modalBody = $("#modalBody");

  // 관리 페이지(admin.html)에서 고친 임시 저장본이 있으면 그것을 보여줌
  const { apps: BASE_APPS, isDraft } = Store.current();
  // 내 앱: 선생님이 직접 추가한 앱 (이 브라우저에만 저장) — 공용 목록 앞에 붙여 보여줌
  let myApps = Store.loadMine();
  let APP_LIST = [];
  const rebuildList = () => {
    APP_LIST = [...myApps.map((a) => ({ ...a, mine: true })), ...BASE_APPS];
  };
  rebuildList();
  if (isDraft) {
    document.body.insertAdjacentHTML(
      "afterbegin",
      '<div class="draft-bar">✎ 관리 페이지에서 고친 목록을 <b>이 브라우저에서만</b> 미리 보는 중입니다. 모두에게 반영하려면 <a href="admin.html">앱 관리</a>에서 apps.js를 내려받아 교체하세요.</div>'
    );
  }

  const state = { key: "all", filter: "all", query: "" };

  const KEY_LABELS = { all: "전체 앱", key: "🔑 API 키 필요", free: "✅ 키 없이 사용" };
  const matchesKey = (app) =>
    state.key === "all" || (state.key === "key" ? app.needsKey : !app.needsKey);
  const catOf = (app) => CATEGORIES[app.category] || { label: app.category || "기타", color: "blue" };

  const escape = (s) =>
    String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  // 분류 카드 아이콘 (48×48 선 그림)
  const ICONS = {
    plan: '<rect x="8" y="12" width="32" height="28" rx="3"/><path d="M8 20h32M16 7v9M32 7v9M15 28h6M27 28h6M15 34h6"/>',
    exam: '<path d="M14 6h14l8 8v28H14z"/><path d="M28 6v8h8M19 23h12M19 29h12M19 35h7"/>',
    review: '<circle cx="21" cy="21" r="12"/><path d="m30 30 10 10M15 21l4 4 8-8"/>',
    cutoff: '<path d="M8 40h32M8 40V8"/><path d="M8 30h32M8 20h32" stroke-dasharray="3 4"/><path d="M14 36c6-2 8-14 14-18s8-6 12-6"/>',
    grading: '<path d="M10 25l9 9 19-20"/><circle cx="24" cy="24" r="19"/>',
    analysis: '<path d="M8 40h32M14 34V24M22 34V14M30 34V20M38 34V10"/>',
    record: '<path d="M32 7l9 9-22 22H10v-9z"/><path d="M27 12l9 9M10 42h30"/>',
    tools: '<rect x="8" y="8" width="13" height="13" rx="3"/><rect x="27" y="8" width="13" height="13" rx="3"/><rect x="8" y="27" width="13" height="13" rx="3"/><path d="M33.5 27v13M27 33.5h13"/>',
  };
  const CAT_ORDER = Object.keys(CATEGORIES);
  const catRank = (app) => {
    const i = CAT_ORDER.indexOf(app.category);
    return i < 0 ? CAT_ORDER.length : i;
  };

  // 메뉴·분류 카드·칩을 CATEGORIES 순서대로 만들기
  const catEntries = Object.entries(CATEGORIES);
  $("#navMenu").insertAdjacentHTML(
    "beforeend",
    catEntries.map(([k, c]) => `<a href="#apps" data-filter="${k}">${escape(c.short || c.label)}</a>`).join("")
  );
  $("#cats").innerHTML = catEntries
    .map(
      ([k, c]) => `
      <button class="cat" data-filter="${k}">
        <span class="cat__icon c-${c.color}"><svg viewBox="0 0 48 48">${ICONS[k] || ICONS.tools}</svg></span>
        <strong><em class="t-${c.color}">${escape(c.label)}</em></strong>
        <small>${escape(c.hint || "")}</small>
      </button>`
    )
    .join("");
  $("#chips").insertAdjacentHTML(
    "beforeend",
    catEntries.map(([k, c]) => `<button class="chip" data-filter="${k}">${escape(c.short || c.label)}</button>`).join("") +
      '<button class="chip chip--mine" data-filter="mine" hidden>⭐ 내 앱</button>'
  );

  function matches(app) {
    if (!matchesKey(app)) return false;
    if (state.filter === "mine") {
      if (!app.mine) return false;
    } else if (state.filter !== "all" && app.category !== state.filter) return false;
    if (!state.query) return true;
    const q = state.query.toLowerCase();
    const haystack = [app.name, app.desc, app.author, catOf(app).label, ...(app.tags || [])]
      .join(" ")
      .toLowerCase();
    return haystack.includes(q);
  }

  function render() {
    const list = APP_LIST.filter(matches).sort((a, b) => catRank(a) - catRank(b));
    empty.hidden = list.length > 0;
    renderLabels();

    grid.innerHTML = list
      .map((app) => {
        const cat = catOf(app);
        return `
        <article class="card" data-id="${escape(app.id)}" tabindex="0">
          <div class="card__top">
            <span class="card__emoji c-${cat.color}">${escape(app.emoji)}</span>
            <span class="card__badges">
              ${app.mine ? '<span class="badge badge--mine">내 앱</span>' : ""}
              ${app.isNew ? '<span class="badge">NEW</span>' : ""}
              ${app.needsKey ? '<span class="keytag" title="Gemini API 키 필요">🔑 API 키</span>' : '<span class="keytag free">키 불필요</span>'}
            </span>
          </div>
          <h3 class="card__name">${escape(app.name)}</h3>
          <p class="card__desc">${escape(app.desc)}</p>
          <div class="card__tags">${(app.tags || []).map((t) => `<span>#${escape(t)}</span>`).join("")}</div>
          <div class="card__foot">
            <span class="pill t-${cat.color}">${escape(cat.label)}</span>
            <span class="card__author">${escape(app.author)}</span>
          </div>
        </article>`;
      })
      .join("");
  }

  // 1단계(키 필요 여부)에서 앱이 없는 분류는 흐리게 표시하고 목록 제목 갱신
  function renderLabels() {
    const inKey = APP_LIST.filter(matchesKey);
    $$(".cat, .chip").forEach((el) => {
      const f = el.dataset.filter;
      const has = f === "mine" ? inKey.some((a) => a.mine) : inKey.some((a) => a.category === f);
      el.classList.toggle("is-empty", f !== "all" && !has);
    });
    $(".chip--mine").hidden = !myApps.length;
    $("#exportMineBtn").hidden = !myApps.length;
    const catLabel =
      state.filter === "all" ? "" : ` · ${state.filter === "mine" ? "내 앱" : CATEGORIES[state.filter].label}`;
    $("#appTitle").textContent = KEY_LABELS[state.key] + catLabel;
  }

  function setKey(key) {
    state.key = key;
    $$(".keyseg__btn").forEach((el) => el.classList.toggle("is-active", el.dataset.key === key));
    $("#keyNote").hidden = key !== "key";
    render();
  }

  function setFilter(filter, scroll = false) {
    state.filter = filter;
    $$("[data-filter]").forEach((el) => el.classList.toggle("is-active", el.dataset.filter === filter));
    render();
    if (scroll) $("#apps").scrollIntoView({ behavior: "smooth", block: "start" });
  }

  function openModal(id) {
    const app = APP_LIST.find((a) => a.id === id);
    if (!app) return;
    const cat = catOf(app);
    modalBody.innerHTML = `
      <span class="card__emoji lg c-${cat.color}">${escape(app.emoji)}</span>
      <span class="pill t-${cat.color}">${escape(cat.label)}</span>
      ${
        app.needsKey
          ? '<p class="keynote">🔑 이 앱은 <b>Gemini API 키</b>가 필요해요. <a href="https://aistudio.google.com/apikey" target="_blank" rel="noopener">키 발급받기 ↗</a></p>'
          : '<p class="keynote free">✅ API 키 없이 바로 쓸 수 있어요.</p>'
      }
      <h3>${escape(app.name)}</h3>
      <p>${escape(app.desc)}</p>
      <div class="card__tags">${(app.tags || []).map((t) => `<span>#${escape(t)}</span>`).join("")}</div>
      <p class="muted">제작: ${escape(app.author)}</p>
      ${
        /^https?:\/\//i.test(app.url || "")
          ? `<a class="btn" href="${escape(app.url)}" target="_blank" rel="noopener">앱 열기 ↗</a>`
          : `<span class="btn is-disabled">링크 준비 중</span>`
      }
      ${
        app.mine
          ? `<div class="mine-acts">
              <button class="btn btn--ghost btn--sm" data-mine="edit" data-id="${escape(app.id)}">수정</button>
              <button class="btn btn--danger btn--sm" data-mine="del" data-id="${escape(app.id)}">삭제</button>
            </div>`
          : ""
      }`;
    modal.showModal();
  }

  // 1단계: API 키 필요 여부
  $$(".keyseg__btn").forEach((el) => el.addEventListener("click", () => setKey(el.dataset.key)));

  // 2단계: 카테고리 카드 / 칩 / 상단 메뉴
  $$(".cat, .chip").forEach((el) =>
    el.addEventListener("click", () => setFilter(el.dataset.filter, el.classList.contains("cat")))
  );
  $$("#navMenu a").forEach((el) =>
    el.addEventListener("click", (e) => {
      e.preventDefault();
      $("#navMenu").classList.remove("is-open");
      if (el.dataset.filter === "all") {
        setFilter("all");
        window.scrollTo({ top: 0, behavior: "smooth" });
      } else {
        setFilter(el.dataset.filter, true);
      }
    })
  );

  // 검색
  searchInput.addEventListener("input", (e) => {
    state.query = e.target.value.trim();
    render();
  });
  searchInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") $("#apps").scrollIntoView({ behavior: "smooth" });
  });
  $("#navSearchBtn").addEventListener("click", () => {
    searchInput.scrollIntoView({ behavior: "smooth", block: "center" });
    setTimeout(() => searchInput.focus(), 350);
  });

  // 카드 클릭 → 상세
  grid.addEventListener("click", (e) => {
    const card = e.target.closest(".card");
    if (card) openModal(card.dataset.id);
  });
  grid.addEventListener("keydown", (e) => {
    const card = e.target.closest(".card");
    if (card && (e.key === "Enter" || e.key === " ")) {
      e.preventDefault();
      openModal(card.dataset.id);
    }
  });
  modal.addEventListener("click", (e) => {
    if (e.target === modal) modal.close();
  });

  // 모바일 메뉴
  $("#navToggle").addEventListener("click", () => $("#navMenu").classList.toggle("is-open"));

  // 스크롤 시 헤더 그림자 / 맨 위로 버튼
  const toTop = $("#toTop");
  window.addEventListener("scroll", () => {
    const y = window.scrollY;
    $("#nav").classList.toggle("is-scrolled", y > 10);
    toTop.classList.toggle("is-visible", y > 400);
  });
  toTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));

  // ---------- 내 앱 추가·수정·삭제 (심사 없이 이 브라우저에 바로 저장) ----------
  const myEditor = $("#myEditor");
  const myForm = $("#myForm");
  let editingId = null;

  $("#myCatSelect").innerHTML = catEntries
    .map(([k, c]) => `<option value="${k}">${escape(c.label)}</option>`)
    .join("");

  function persistMine() {
    if (!Store.saveMine(myApps)) alert("브라우저 저장소를 쓸 수 없어요. 시크릿 창이거나 저장이 막혀 있는지 확인해 주세요.");
    rebuildList();
    render();
  }

  function openMyEditor(app) {
    editingId = app ? app.id : null;
    $("#myFormTitle").textContent = app ? "내 앱 수정" : "내 앱 추가";
    myForm.reset();
    const v = app || { category: CAT_ORDER[CAT_ORDER.length - 1] };
    myForm.name.value = v.name || "";
    myForm.url.value = v.url || "";
    myForm.category.value = v.category;
    myForm.emoji.value = v.emoji || "";
    myForm.desc.value = v.desc || "";
    myForm.tags.value = (v.tags || []).join(", ");
    myForm.author.value = v.author || (myApps[0] && myApps[0].author) || "";
    myForm.needsKey.checked = !!v.needsKey;
    myEditor.showModal();
    myForm.name.focus();
  }

  myForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const url = myForm.url.value.trim();
    if (!/^https?:\/\//i.test(url)) {
      alert("앱 주소는 http:// 또는 https:// 로 시작해야 해요.");
      return;
    }
    const data = {
      name: myForm.name.value.trim(),
      category: myForm.category.value,
      needsKey: myForm.needsKey.checked,
      emoji: myForm.emoji.value.trim() || "📦",
      desc: myForm.desc.value.trim(),
      tags: myForm.tags.value.split(",").map((t) => t.trim().replace(/^#/, "")).filter(Boolean),
      author: myForm.author.value.trim(),
      url,
    };
    if (editingId) {
      const i = myApps.findIndex((a) => a.id === editingId);
      myApps[i] = { id: editingId, ...data };
    } else {
      myApps.unshift({ id: "my-" + Date.now().toString(36), ...data });
    }
    myEditor.close();
    persistMine();
    setKey("all");
    setFilter("mine", true);
  });
  $("#myCancelBtn").addEventListener("click", () => myEditor.close());
  myEditor.addEventListener("click", (e) => {
    if (e.target === myEditor) myEditor.close();
  });
  $("#addMyAppBtn").addEventListener("click", () => openMyEditor(null));

  // 상세 창의 수정/삭제 버튼
  modalBody.addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-mine]");
    if (!btn) return;
    const app = myApps.find((a) => a.id === btn.dataset.id);
    if (!app) return;
    modal.close();
    if (btn.dataset.mine === "edit") {
      openMyEditor(app);
    } else if (confirm(`“${app.name}” 앱을 내 목록에서 삭제할까요?`)) {
      myApps = myApps.filter((a) => a.id !== app.id);
      persistMine();
      if (!myApps.length && state.filter === "mine") setFilter("all");
    }
  });

  // 다른 컴퓨터·브라우저로 옮길 수 있게 파일로 백업/불러오기
  $("#exportMineBtn").addEventListener("click", () => {
    const blob = new Blob([JSON.stringify(myApps, null, 2)], { type: "application/json;charset=utf-8" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "eduhub-my-apps.json";
    a.click();
    URL.revokeObjectURL(a.href);
  });
  $("#importMine").addEventListener("change", async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    try {
      const incoming = Store.parseFile(await file.text()).apps.filter((a) => a && a.name && a.url);
      const known = new Set(myApps.map((a) => a.id));
      const added = incoming
        .filter((a) => !known.has(a.id))
        .map((a) => ({
          ...a,
          id: String(a.id || "").startsWith("my-") ? a.id : "my-" + Math.random().toString(36).slice(2, 9),
          mine: undefined,
        }));
      myApps = [...added, ...myApps];
      persistMine();
      alert(`${added.length}개 앱을 내 목록에 추가했어요.`);
      if (added.length) setFilter("mine", true);
    } catch (err) {
      alert("불러오지 못했어요: " + err.message);
    } finally {
      e.target.value = "";
    }
  });

  render();
})();
