(() => {
  const $ = (sel) => document.querySelector(sel);

  let { apps, owner } = Store.current();
  apps = apps.map((a) => ({ ...a })); // 원본 APPS를 건드리지 않도록 복사
  let editingId = null;

  const rows = $("#rows");
  const editor = $("#editor");
  const form = $("#form");
  const status = $("#status");
  const ownerInput = $("#ownerInput");

  const escape = (s) =>
    String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

  // 분류 선택지
  $("#catSelect").innerHTML = Object.entries(CATEGORIES)
    .map(([k, v]) => `<option value="${k}">${v.label}</option>`)
    .join("");

  function persist(msg) {
    const ok = Store.save(apps, owner);
    status.textContent = ok ? `✔ ${msg} · 이 브라우저에 저장됨` : "⚠ 브라우저 저장소를 쓸 수 없어요. apps.js로 내려받아 보관하세요.";
    render();
  }

  function render() {
    rows.innerHTML = apps
      .map((a, i) => {
        const cat = CATEGORIES[a.category] || { label: a.category, color: "blue" };
        const link =
          a.url && a.url !== "#"
            ? `<a href="${escape(a.url)}" target="_blank" rel="noopener">열기 ↗</a>`
            : '<span class="muted">미연결</span>';
        return `
        <tr data-id="${escape(a.id)}">
          <td class="order">
            <button data-act="up" ${i === 0 ? "disabled" : ""} aria-label="위로">▲</button>
            <button data-act="down" ${i === apps.length - 1 ? "disabled" : ""} aria-label="아래로">▼</button>
          </td>
          <td><span class="row-emoji">${escape(a.emoji || "📦")}</span><b>${escape(a.name)}</b>${a.isNew ? ' <span class="badge">NEW</span>' : ""}
            <div class="muted row-desc">${escape(a.desc)}</div></td>
          <td><span class="pill t-${cat.color}">${escape(cat.label)}</span></td>
          <td>${a.needsKey ? '<span class="keytag">🔑 필요</span>' : '<span class="keytag free">불필요</span>'}</td>
          <td>${escape(a.author)}</td>
          <td>${link}</td>
          <td class="acts">
            <button class="btn btn--sm btn--ghost" data-act="edit">수정</button>
            <button class="btn btn--sm btn--danger" data-act="del">삭제</button>
          </td>
        </tr>`;
      })
      .join("");
    if (!apps.length) rows.innerHTML = '<tr><td colspan="7" class="muted center">앱이 없어요. “새 앱 추가”를 눌러 시작하세요.</td></tr>';
  }

  function openEditor(app) {
    editingId = app ? app.id : null;
    $("#formTitle").textContent = app ? "앱 수정" : "새 앱 추가";
    form.reset();
    const v = app || { category: Object.keys(CATEGORIES)[0], author: owner, emoji: "", tags: [], url: "" };
    form.name.value = v.name || "";
    form.category.value = v.category;
    form.emoji.value = v.emoji || "";
    form.desc.value = v.desc || "";
    form.tags.value = (v.tags || []).join(", ");
    form.author.value = v.author || owner;
    form.url.value = v.url && v.url !== "#" ? v.url : "";
    form.needsKey.checked = !!v.needsKey;
    form.isNew.checked = !!v.isNew;
    editor.showModal();
    form.name.focus();
  }

  function makeId(name) {
    const base = "app-" + Date.now().toString(36);
    return apps.some((a) => a.id === base) ? base + Math.random().toString(36).slice(2, 5) : base;
  }

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const data = {
      name: form.name.value.trim(),
      category: form.category.value,
      needsKey: form.needsKey.checked,
      emoji: form.emoji.value.trim() || "📦",
      desc: form.desc.value.trim(),
      tags: form.tags.value.split(",").map((t) => t.trim().replace(/^#/, "")).filter(Boolean),
      author: form.author.value.trim() || owner,
      url: form.url.value.trim() || "#",
    };
    if (form.isNew.checked) data.isNew = true;

    if (editingId) {
      const i = apps.findIndex((a) => a.id === editingId);
      apps[i] = { id: editingId, ...data };
      persist(`“${data.name}” 수정`);
    } else {
      apps.unshift({ id: makeId(data.name), ...data });
      persist(`“${data.name}” 추가`);
    }
    editor.close();
  });
  $("#cancelBtn").addEventListener("click", () => editor.close());
  editor.addEventListener("click", (e) => {
    if (e.target === editor) editor.close();
  });

  rows.addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-act]");
    if (!btn) return;
    const id = btn.closest("tr").dataset.id;
    const i = apps.findIndex((a) => a.id === id);
    const app = apps[i];
    switch (btn.dataset.act) {
      case "edit":
        openEditor(app);
        break;
      case "del":
        if (confirm(`“${app.name}” 앱을 목록에서 삭제할까요?`)) {
          apps.splice(i, 1);
          persist(`“${app.name}” 삭제`);
        }
        break;
      case "up":
      case "down": {
        const j = btn.dataset.act === "up" ? i - 1 : i + 1;
        [apps[i], apps[j]] = [apps[j], apps[i]];
        persist("순서 변경");
        break;
      }
    }
  });

  $("#addBtn").addEventListener("click", () => openEditor(null));

  $("#exportBtn").addEventListener("click", () => {
    const blob = new Blob([Store.toAppsJs(apps, owner)], { type: "text/javascript;charset=utf-8" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "apps.js";
    a.click();
    URL.revokeObjectURL(a.href);
    status.textContent = "⬇ apps.js를 내려받았어요. eduhub 폴더의 apps.js를 이 파일로 바꿔 주세요.";
  });

  $("#importFile").addEventListener("change", async (e) => {
    const file = e.target.files[0];
    if (!file) return;
    try {
      const data = Store.parseFile(await file.text());
      if (!confirm(`${data.apps.length}개 앱을 불러와 지금 목록을 바꿀까요?`)) return;
      apps = data.apps;
      if (data.owner) owner = ownerInput.value = data.owner;
      persist(`${file.name} 불러오기`);
    } catch (err) {
      alert("불러오지 못했어요: " + err.message);
    } finally {
      e.target.value = "";
    }
  });

  $("#resetBtn").addEventListener("click", () => {
    if (!confirm("이 브라우저에서 고친 내용을 모두 지우고 apps.js 원래 목록으로 되돌릴까요?")) return;
    Store.clear();
    apps = APPS.map((a) => ({ ...a }));
    owner = ownerInput.value = MY_NAME;
    status.textContent = "↺ apps.js 원래 목록으로 되돌렸어요.";
    render();
  });

  ownerInput.value = owner;
  ownerInput.addEventListener("change", () => {
    owner = ownerInput.value.trim() || MY_NAME;
    persist("기본 제작자 이름 변경");
  });

  if (Store.load()) status.textContent = "✎ 이 브라우저에 저장된 수정본을 불러왔어요.";
  render();
})();
