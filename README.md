# 📝 キリ概テスト自動解答システム  
Googleスプレッドシートで管理された正答データをもとに、  
LMSテスト画面の入力欄へ自動的に解答を反映する **Tampermonkeyユーザースクリプト** を開発するプロジェクト。

本リポジトリでは、ユーザースクリプト方式のみを採用し、  
その他の方式（拡張機能、ブックマークレット、Pythonなど）は扱わない。

---

## 🎯 1. 研究テーマ  
**Googleスプレッドシートの正答データを用いた、LMSテスト画面への自動解答入力ユーザースクリプトの開発**

---

## 🎯 2. 目的  

1. Googleスプレッドシートに保存された正答データを利用し、  
   LMS（cp.aim.aoyama.ac.jp）上にあるテキスト入力式テストに対して  
   **ユーザースクリプトによって自動入力を行う仕組みを構築する。**

2. 初学者でも導入・実行しやすく、環境依存が少ない  
   **軽量で安定した自動入力ツール** を提供する。

3. 研究として、  
   - 正答データ形式  
   - DOMとの対応づけ  
   - 入力方式  
   の最適化を行い、**ユーザースクリプトだけで完結する合理的な自動化手法**を示す。

---

## 🧩 3. 対象・前提条件  

### ■ 対象ページ  
- 青山学院大学LMS（cp.aim.aoyama.ac.jp）のテキスト入力式テスト  
- 主に `<input type="text">` を用いた設問を想定

### ■ 正答データ  
- Googleスプレッドシート管理  
- 1行＝1問、第一列に正答を入力しておく形式  
- CSVとしてエクスポート、または直接answers配列に貼り付ける

### ■ 実行環境  
- PC版 **Google Chrome**  
- **Tampermonkey拡張** をインストール済みであること

---

## 🛠️ 4. 研究方法（ユーザースクリプト方式のみ）  

### 4.1 全体の流れ  
1. Googleスプレッドシートで正答を整理  
2. 正答を配列（answers）としてスクリプトに貼り付け  
3. テスト画面の入力欄（`input[type="text"]`）を取得  
4. 順番に answers[i] を入力欄へ代入  
5. 完了後ログメッセージを表示

---

### 4.2 正答データ形式（例）

| No | Answer |
|----|--------|
| 1  | love   |
| 2  | peace  |
| 3  | 2025   |

画面上の入力欄の並び順がシートの行番号と対応する  
**シンプルで汎用性の高い方式**を採用する。

---

## 🖥️ 5. ユーザースクリプト（Tampermonkey）実装例  

以下は最小限で動作するサンプル：

```javascript
// ==UserScript==
// @name         Kiri Auto Answer
// @match        https://cp.aim.aoyama.ac.jp/*
// @grant        none
// ==/UserScript==

(function() {
  'use strict';

  // スプレッドシートから貼り付ける正答リスト（例）
  const answers = [
    "love",
    "peace",
    "2025"
  ];

  // input[type="text"] を順番に取得
  const inputs = document.querySelectorAll('input[type="text"]');

  // 順番に自動入力
  inputs.forEach((input, i) => {
    if (i < answers.length) {
      input.value = answers[i];
    }
  });

  console.log("✨ ユーザースクリプトによる自動入力が完了しました！");
})();
