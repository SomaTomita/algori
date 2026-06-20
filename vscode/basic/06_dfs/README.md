# DFS (Depth-First Search)

> 1 本の枝を最後まで掘ってから戻る。再帰 (= call stack) で深さを管理する探索。

## BFS との比較

| 観点         | DFS                          | BFS                              |
| ------------ | ---------------------------- | -------------------------------- |
| 探索順       | 深く潜る → 戻る → 別の枝     | 同じ深さを全部見てから次の深さへ |
| データ構造   | スタック (再帰)              | キュー (deque)                   |
| 用途         | 連結成分, パス全列挙, 木構造 | 最短路 (重みなし), レベル走査    |
| 空間量       | O(h)  ※ h は木の高さ         | O(w)  ※ w は最大幅               |

## ツリー DFS テンプレ

```python
def dfs(node, target):
    if node is None:
        return None
    if node.val == target:
        return node
    return dfs(node.left, target) or dfs(node.right, target)
```

## グラフ DFS テンプレ (visited 必須)

```python
def dfs_graph(start, get_neighbors):
    visited = set()
    def helper(node):
        if node in visited:
            return
        visited.add(node)
        # process node
        for nei in get_neighbors(node):
            helper(nei)
    helper(start)
```

> ツリーは visited 不要 (循環がない)。グラフは visited を入れないと無限ループ。

## 再帰スタックで深さを管理 (call stack のイメージ)

```
dfs(A) を呼ぶと、関数フレームがスタックに積まれる:

  call stack (上から呼び出し順)
  ┌─────────────┐
  │ dfs(D)      │ ← いまここを実行中 (一番深い)
  │ dfs(C)      │   D が return すると C に戻る
  │ dfs(B)      │
  │ dfs(A)      │ ← 最初に呼んだ
  └─────────────┘

A → B → C → D まで潜る
D が None / 葉 / 目的のもの に当たる → return
スタックを 1 段ずつ ポップ して "戻りながら" 別の枝へ
```

つまり「再帰 = スタック上での自動巻き戻し」。明示的に `stack.append/pop` する反復版とまったく等価。

## 計算量

- 時間: O(V + E)  (各ノード/辺を 1 回ずつ訪れる)
- 空間: O(h)      (再帰スタックの最大深さ = 木の高さ)

## "これ DFS だな" の見分けポイント

- 木やグリッドで **連結している領域** を探す  → 例: Number of Islands
- **深さ / 高さ** を求める                    → 例: Max Depth of Binary Tree
- **全パス列挙** / 部分集合 / 順列            → DFS + バックトラッキング
- **存在判定** (この値あるか? このパスあるか?) → 早期 return しやすい DFS
- 再帰で「一度潜って戻る」自然に書ける    → DFS

逆に **最短ステップ** (重みなし) なら BFS を選ぶ。
