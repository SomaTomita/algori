# basic — データ構造とアルゴリズム入門

Sheldon Chai 氏の DSA コース転写を元にした、章ごとに分割した教材です。
**サクッと visual + コードで基礎の基礎から** をコンセプトにしています。

```
basic/
├── 00_foundations/         ← 土台 (RAM, 配列, 文字列, set, ループ, Big O)
├── 01_hashmaps/            ← 万能の高速検索
├── 02_two_pointers/        ← 線形構造を 1 パスで
├── 03_sliding_window/      ← 連続部分問題
├── 04_binary_search/       ← 半分カット
├── 05_bfs/                 ← レベル順 (最短手数)
├── 06_dfs/                 ← 深さ優先 (再帰)
├── 07_backtracking/        ← DFS + undo
└── 08_heaps_priority_queues/  ← top-k 系
```

## 学習順序の目安

| # | 章 | 何ができるようになる |
|---|---|---|
| 0 | foundations | 計算量を見積もれる |
| 1 | hashmaps | brute force O(n²) を O(n) に落とせる |
| 2 | two_pointers | 線形構造の左右/前後を効率走査 |
| 3 | sliding_window | 連続部分問題が解ける |
| 4 | binary_search | 単調性を見抜いて O(log n) |
| 5 | bfs | 最短手数・レベル順 |
| 6 | dfs | 全探索・木/グラフ走査 |
| 7 | backtracking | 順列・部分集合・パズル |
| 8 | heaps | top-k / 動的中央値 / Dijkstra の準備 |

## 各章の構成

- `README.md` — 概念、図、テンプレート (短く)
- `*.py` — 実例コード + 各 iteration の図解トレース + 計算量

## 関連フォルダ

- `../neetcode/` — LeetCode の個別問題集 (このコースの応用先)
- `../Top6InterviewConcepts/` — 面接頻出 6 パターンの別教材
