// 앱 설치(PWA): 서비스 워커 등록 + '앱 설치' 버튼
(() => {
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => navigator.serviceWorker.register("sw.js").catch(() => {}));
  }

  const btn = document.getElementById("installBtn");
  if (!btn) return;

  const standalone = matchMedia("(display-mode: standalone)").matches || navigator.standalone;
  if (standalone) return; // 이미 설치된 앱으로 열려 있음

  // 크롬·엣지·삼성 인터넷: 브라우저가 설치 가능하다고 알려줄 때 버튼 표시
  let deferred = null;
  window.addEventListener("beforeinstallprompt", (e) => {
    e.preventDefault();
    deferred = e;
    btn.hidden = false;
  });
  window.addEventListener("appinstalled", () => {
    deferred = null;
    btn.hidden = true;
  });

  // 아이폰·아이패드 사파리는 설치 창을 띄울 수 없어 방법을 안내
  const ios = /iphone|ipad|ipod/i.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);
  if (ios) btn.hidden = false;

  btn.addEventListener("click", async () => {
    if (deferred) {
      deferred.prompt();
      await deferred.userChoice;
      deferred = null;
      btn.hidden = true;
    } else if (ios) {
      alert("사파리 아래쪽의 공유 버튼(□↑)을 누른 뒤\n‘홈 화면에 추가’를 선택하면 앱처럼 설치돼요.");
    }
  });
})();
