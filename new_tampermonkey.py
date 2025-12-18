// ==UserScript==
// @name         AutoTestAnswering (Romeo) DEBUG badge
// @match        *://*/*
// @grant        none
// @run-at       document-end
// ==/UserScript==

(function () {
  "use strict";

  // 1) console に必ず出す
  console.log("👉 [AutoTestAnswering] スクリプト起動しました: ", location.href);

  // 2) 画面にバッジを出す
  const id = "tm-debug-badge-romeo";
  const old = document.getElementById(id);
  if (old) old.remove();

  const badge = document.createElement("div");
  badge.id = id;
  badge.textContent = "✅ 起動中: " + document.title;
  badge.style.position = "fixed";
  badge.style.right = "10px";
  badge.style.bottom = "10px";
  badge.style.zIndex = "9999999";
  badge.style.background = "red"; // 目立つように赤にしました
  badge.style.color = "white";
  badge.style.padding = "10px";
  badge.style.borderRadius = "5px";
  badge.style.fontSize = "14px";
  badge.style.boxShadow = "0 0 10px rgba(0,0,0,0.5)";
  
  document.body.appendChild(badge);
})();
