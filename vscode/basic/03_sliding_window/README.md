# Sliding Window (スライディングウィンドウ)

> 配列/文字列上に「窓 (window)」を置き、右から要素を入れ左から抜くことで、連続した範囲を O(n) で走査するテクニック。**Two Pointers の発展形** で、両ポインタが同方向 (左→右) に進む。

---

## 1. 2 種類のウィンドウ

| 種類           | サイズ                      | 用途                                 | 典型キーワード                                                |
| -------------- | --------------------------- | ------------------------------------ | ------------------------------------------------------------- |
| **固定サイズ** | 常に `k` で一定             | 長さ k の連続部分の最大/最小/平均    | "subarray of length k", "window size k", "every k consecutive" |
| **動的サイズ** | 条件を満たす範囲で伸縮      | 条件を満たす最長/最短の連続部分      | "longest substring with...", "shortest subarray such that..."  |

---

## 2. 固定サイズ テンプレート

```python
window_sum = sum(arr[:k])     # 最初の窓を作る
best = window_sum
for r in range(k, len(arr)):  # r = 右端を 1 つずつ進める
    l = r - k                 # l = 抜ける左端
    window_sum -= arr[l]      # 左から 1 つ抜く
    window_sum += arr[r]      # 右から 1 つ入れる
    best = max(best, window_sum)
```

ASCII イメージ (`k=3`):

```
[2, 1, 5, 1, 3, 2]
 └──┬──┘            ← l..r の窓を 1 ずつスライド
```

---

## 3. 動的サイズ テンプレート

```python
l = 0
for r in range(len(arr)):
    # 1. arr[r] を窓に入れる
    while window_invalid:        # 条件を破ったら…
        # 2. arr[l] を窓から抜く
        l += 1                   # 左端を縮める
    # 3. 現在の有効な窓で答えを更新
    answer = max(answer, r - l + 1)
```

ASCII イメージ:

```
expand:                  shrink:
l         r              l       r
↓         ↓              ↓       ↓
[a b c a ...]   →   [_ b c a ...]
※ 'a' が重複 → l を進めて窓を縮める
```

---

## 4. 計算量

| 項目 | コスト                                     |
| ---- | ------------------------------------------ |
| 時間 | **O(n)**  ← 各要素は最大 2 回 (入る/抜ける) |
| 空間 | O(1) または O(k) / O(alphabet)             |

ナイーブ O(n·k) や O(n²) を **O(n) に削減できる** のが最大の旨み。

---

## 5. 「これ sliding window だな」の見分けポイント

- 入力が **配列 / 文字列 / 連続した範囲**
- 求めたいのが **連続部分 (subarray / substring)** の何らか (sum, length, count...)
- ヒント: "consecutive", "contiguous", "subarray", "substring", "window of size k"
- 「全パターンを試すと O(n²)」だが、**l と r が後戻りしない** ことに気づけたら sliding window

---

## 6. 実装ファイル

- [`max_subarray_length_k.py`](./max_subarray_length_k.py) — 固定サイズ (長さ k の最大和)
- [`longest_substring_no_repeat.py`](./longest_substring_no_repeat.py) — 動的サイズ (重複なしの最長部分文字列)
