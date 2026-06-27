# 08. Heaps / Priority Queues

「優先度順に出てくるキュー」 = 取り出しのたびに **最小 (or 最大) が決まって出てくる** データ構造。

---

## Min Heap / Max Heap (binary tree のイメージ)

```
Min Heap (親 <= 子)              Max Heap (親 >= 子)

        1                              9
       / \                            / \
      3   5                          7   8
     / \ / \                        / \ / \
    4  8 6  9                      4  3 6  1
   ↑ root が最小                  ↑ root が最大
```

ポイント:
- 形は常に **完全二分木** (左から詰まる)
- 順序は **親と子の関係だけ** 保証 (兄弟同士はバラバラで OK)

---

## 配列での内部表現

二分木をそのまま配列に並べる (index 0 から)。

```
         1 (i=0)
        / \
   3 (i=1) 5 (i=2)
   / \      / \
4(3) 8(4) 6(5) 9(6)

配列: [1, 3, 5, 4, 8, 6, 9]
       0  1  2  3  4  5  6
```

index の関係:
```
parent(i)       = (i - 1) // 2
left_child(i)   = 2*i + 1
right_child(i)  = 2*i + 2
```

---

## Python `heapq` API 早見表 (min heap がデフォルト)

```
heapq.heappush(h, x)   挿入 / sift-up         O(log n)
heapq.heappop(h)       最小値を取り出し       O(log n)
heapq.heapify(arr)     リストを heap 化       O(n)     (ボトムアップで一気に)
heapq.heappushpop(h,x) push してから pop     O(log n)
h[0]                   最小値を見るだけ       O(1)
```

---

## min heap で max heap を作る (Python の定番ハック)

`heapq` には max heap が無いので、**値の符号を反転** して min heap に放り込む。

```python
nums = [3, 1, 4, 1, 5]
heap = [-n for n in nums]   # [-3, -1, -4, -1, -5]
heapq.heapify(heap)
biggest = -heapq.heappop(heap)   # 5
```

タプルを使うときは先頭要素の符号だけ反転すれば OK: `(-priority, payload)`

---

## 計算量サマリ

| 操作 | 時間 |
|------|------|
| push | O(log n) |
| pop  | O(log n) |
| peek (`h[0]`) | O(1) |
| heapify | **O(n)** (sort より速い) |
| top-k (size n の heap) | O(n + k log n) |
| top-k (size k の heap) | O(n log k) ← n が巨大なとき有利 |

---

## 「これ heap だな」の見分けポイント

- **top-k / bottom-k** (k 個だけ欲しい) → 全 sort は無駄, heap で O(n log k)
- **動的中央値** (流れてくるデータの median) → max heap + min heap の二刀流
- **Dijkstra / Prim** など最短経路系 → 「次に処理する最小 cost ノード」を取り出す
- **task scheduler / merge K sorted lists** → 「次に来るやつ」を毎回選ぶ系
- **値そのものより順位 (priority) が大事**な処理全般
