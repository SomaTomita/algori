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

## `deque([root])` の中身 — 入るのは「1 個」だけ

まず誤解しやすい点: `root = [3, 9, 20, null, null, 15, 7]` は **木の形を表す LeetCode の表記**であって、コード内に存在するリストではない。実際の `root` は **TreeNode オブジェクト 1 個**(val=3)で、残りのノードは `.left` / `.right` でぶら下がっているだけ。

```
root = TreeNode(3)
  ├─ .left  = TreeNode(9)
  └─ .right = TreeNode(20)
                ├─ .left  = TreeNode(15)
                └─ .right = TreeNode(7)
```

だから `deque([root])` で入るのは **root ノード 1 個だけ**(7 個ではない)。

```python
[root]          # → [ <TreeNode val=3> ]          要素 1 個のリスト (root を包んだだけ)
q = deque([root])
len(q)          # → 1     (3,9,20,... の 7 個じゃない!)
q[0].val        # → 3     中身は root ノード 1 個。ここから木全体に手が届く
```

9,20,15,7 は最初 `q` に入っていない。BFS の最中に `q.append(node.left)` などで少しずつ追加される(外ループ 1 で 9,20、外ループ 2 で 15,7)。

### `[ ]` が必須な理由(罠)

`deque(iterable)` は「iterable の中身を 1 個ずつ入れる」仕様。

```python
deque([3, 9, 20])  # 中身を展開 → int が 3 個入る
deque([root])      # 中身を展開 → root ノード 1 個入る   ← これが今回 (OK)
deque(root)        # TypeError! TreeNode は反復可能でないので展開できず死ぬ (NG)
```

つまり `[root]` の角カッコは「root を 1 要素のリストで包んで、BFS の出発点を 1 個セットする」ための必須要素。`deque(root)` と書くとエラーになる。

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
