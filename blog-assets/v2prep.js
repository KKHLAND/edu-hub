// Tistory 모의고사 해설 등록 도우미 (Chrome / 내장 브라우저 공용)
// 사용: window.__v2 = <이 파일 내용>; await window.__v2(BASE, 'P2', 17, 18, 10)
(async function setup() {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  window.__v2 = async function (BASE, key, day, hour, minute) {
    const ed = tinymce.activeEditor;
    const meta = await fetch(BASE + 'meta.json').then(r => r.json());
    const m = meta[key];
    let html = await fetch(BASE + key + '_티스토리.html').then(r => r.text());
    const files = ['thumb_' + key + '.png', ...m.images];
    const codes = {};
    ed.setContent('<p>&nbsp;</p>');
    for (const f of files) {
      const blob = await fetch(BASE + f).then(r => r.blob());
      const file = new File([blob], f, { type: 'image/png' });
      const before = (ed.getContent().match(/\[##_Image\|[^\]]*?_##\]/g) || []).length;
      const dt = new DataTransfer(); dt.items.add(file);
      ed.selection.select(ed.getBody(), true); ed.selection.collapse(false);
      ed.getBody().dispatchEvent(new ClipboardEvent('paste', { clipboardData: dt, bubbles: true, cancelable: true }));
      let got = null;
      for (let i = 0; i < 120 && !got; i++) {
        await sleep(500);
        const all = ed.getContent().match(/\[##_Image\|[^\]]*?_##\]/g) || [];
        if (all.length > before) got = all[all.length - 1];
      }
      if (!got) throw new Error('upload timeout ' + f);
      codes[f] = got;
    }
    html = html.replace('<!--THUMB-->', '<p>' + codes['thumb_' + key + '.png'] + '</p>');
    html = html.replace(/<!--IMG:([^|]+)\|([^>]*?)-->/g, (_, f, alt) => {
      let c = codes[f];
      if (!c) return '';
      c = c.replace(/"alt":"[^"]*"/, '"alt":"' + alt.replace(/"/g, '') + '"');
      return '<p>' + c + '</p>';
    });
    ed.setContent(html);
    // 제목
    const t = document.querySelector('#post-title-inp, textarea.textarea_tit, input.tf_tit');
    if (t) { t.value = m.title; t.dispatchEvent(new Event('input', { bubbles: true })); }
    window.__meta = { key, day, hour, minute, slug: m.slug, tags: m.tags, title: m.title, thumbUrl: BASE + 'thumb_' + key + '.png' };
    return { imgs: Object.keys(codes).length, left: (ed.getContent().match(/<!--IMG/g) || []).length, title: t && t.value };
  };
})();
