# BFS (Breadth-First Search)

層ごとに広がっていく探索。

## 訪問順イメージ

キュー(FIFO)で「近いところから順に」訪れる。波紋が広がる感じ。

```
        1            ← Level 0 (訪問順 1)
       / \
      2   3          ← Level 1 (訪問順 2, 3)
     / \   \
    4   5   6        ← Level 2 (訪問順 4, 5, 6)
```

訪問順: `1 → 2 → 3 → 4 → 5 → 6`

DFS なら `1 → 2 → 4 → 5 → 3 → 6`(深く潜る)になる。BFS は **横に進む**。

---

## ツリー版テンプレ (visited 不要)

木は閉路がないので、同じノードに戻ってこない → `visited` は不要。

```python
from collections import deque
def bfs_tree(root):
    q = deque([root])
    while q:
        node = q.popleft()
        # process node
        for child in (node.left, node.right):
            if child:
                q.append(child)
```

## グラフ版テンプレ (visited 必須)

グラフは閉路がありうる → 同じノードを何度も入れないように `visited` を持つ。

```python
from collections import deque
def bfs_graph(start, get_neighbors):
    visited = {start}
    q = deque([start])
    while q:
        node = q.popleft()
        # process node
        for nei in get_neighbors(node):
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
```

---

## ポイント: visited に追加するタイミング

**enqueue 時** (キューに入れる瞬間) に `visited` へ追加する。

```python
# OK (enqueue 時):
if nei not in visited:
    visited.add(nei)   # ← ここで追加
    q.append(nei)

# NG (dequeue 時): 同じノードが複数回 enqueue され重複処理される
node = q.popleft()
visited.add(node)      # ← 遅すぎる
```

理由: dequeue 時に追加すると、まだキュー内にいるノードを「未訪問」とみなして、もう一度 enqueue してしまう。

---

## 計算量

| 量      | 値                                      |
| ------- | --------------------------------------- |
| 時間    | `O(V + E)` (各頂点・各辺を 1 回ずつ)    |
| 空間    | `O(V)` (キュー + visited)               |
| ツリー  | `O(n)` 時間 / `O(w)` 空間 (w = 最大幅)  |

---

## 「これ BFS だな」の見分けポイント

- **最短手数 / 最短ステップ数**: 「最少何手で?」「最短何回で?」
- **レベル順 / 階層ごと**: 二分木のレベル順、距離別グルーピング
- **最近の〇〇**: ある点から最も近いセル / ノード
- **重みなしグラフの最短経路**: 重み 1 の最短路は BFS で OK
- **連結成分の塗り分け**: Flood Fill, Number of Islands など

逆に、**全パターンを試す / 経路の組み合わせ** が欲しい時は DFS / Backtracking。

---

## このディレクトリの実例

- `tree_level_order_traversal.py` — 木をレベル順にリスト化
- `flood_fill.py` — 4 方向の連結領域を塗りつぶし (BFS の各ステップ可視化)
