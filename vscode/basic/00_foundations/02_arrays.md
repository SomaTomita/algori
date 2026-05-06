# 配列（Array）の基礎

## 配列とは

- **同じ型** のデータを **連続したメモリ** に並べたデータ構造
- インデックスは **0 始まり**
- 真の配列はサイズ固定 (Python の `list` は動的配列)

```
Index :   0   1   2   3   4
        ┌───┬───┬───┬───┬───┐
arr   = │ 1 │ 2 │ 3 │ 4 │ 5 │
        └───┴───┴───┴───┴───┘
```

## Python の list / array / numpy

| 種類           | 中身             | 特徴                         |
| -------------- | ---------------- | ---------------------------- |
| `list`         | 任意型のポインタ | 柔軟・動的リサイズ           |
| `array.array`  | 単一型 C 配列    | 型固定・省メモリ             |
| `numpy.ndarray`| 連続 C 配列      | 数値計算で爆速 (SIMD/BLAS)   |

→ `examples_array.py` の `demo_list_vs_array()` 参照

---

## 基本操作と計算量

| 操作               | 計算量  | メモ                       |
| ------------------ | ------- | -------------------------- |
| アクセス `arr[i]`  | O(1)    | アドレス計算で直行         |
| 線形探索           | O(n)    | 全走査                     |
| 末尾追加 `append`  | O(1)\*  | アモータイズド             |
| 任意位置挿入       | O(n)    | 後ろをシフト               |
| 末尾削除 `pop()`   | O(1)    | 縮めるだけ                 |
| 任意位置削除       | O(n)    | 前にシフト                 |

```
insert(2, 10):                pop(2):
[1,2,3,4,5]                   [1,2,10,3,4,5]
     ↓ shift right                 ↓ shift left
[1,2,10,3,4,5]                [1,2,3,4,5]
```

→ `examples_array.py` の `demo_array_operations()` 参照

---

## メモリレイアウトとキャッシュ効率

連続アクセス (行優先) は CPU キャッシュに乗りやすい。

```
matrix[i][j] を行優先で走査:
  ┌──────────────────────────┐
  │ i=0: j=0 → j=1 → j=2 ... │  ← 連続アドレス (cache hit)
  │ i=1: j=0 → j=1 → j=2 ... │
  └──────────────────────────┘

列優先 matrix[i][j] (j 外, i 内) はストライドが大きく cache miss 多発
```

→ `examples_array.py` の `demo_cache_efficiency()` 参照

---

## 動的配列のリサイズ

`list.append` は容量が尽きると **再確保 + コピー** が走る。
平均 O(1) (アモータイズド) だが、瞬間的には O(n)。

```
capacity 拡張 (例): 0 → 4 → 8 → 16 → 32 → ...

append 時:
  if len == cap:
      new_buf = alloc(cap * 2)   # ← O(n) コピー
      copy(buf → new_buf)
      buf = new_buf
  buf[len++] = x                 # ← O(1)
```

→ `examples_array.py` の `demo_dynamic_array()` / `demo_resize_cost()` 参照

---

## LeetCode 頻出パターン

### 1. Two Pointers

ソート済み配列で和 = target のペア探索。

```
arr = [1, 2, 3, 4, 5, 6]   target = 9
       L              R     1+6=7  → L++
          L           R     2+6=8  → L++
             L        R     3+6=9  ✓
```

### 2. Sliding Window

サイズ k の窓を 1 つずつずらす。再計算は **入る要素 - 出る要素** だけ。

```
arr = [1,4,2,10,23,3,1,0,20]   k=4

[1,4,2,10] 23  3  1  0  20    sum=17
 1 [4,2,10,23] 3  1  0  20    sum=17-1+23=39  ★
 1  4 [2,10,23,3] 1  0  20    sum=39-4+3=38
 ...
```

### 3. 配列の反転による回転

3 回 reverse で k 右回転を O(n)/O(1)。

```
arr = [1,2,3,4,5,6,7]  k=3

reverse(0, n-1)   → [7,6,5,4,3,2,1]
reverse(0, k-1)   → [5,6,7,4,3,2,1]
reverse(k, n-1)   → [5,6,7,1,2,3,4]
```

→ `examples_array.py` の `demo_two_pointers()` / `demo_sliding_window()` / `demo_rotate()` 参照

---

## 配列問題で使う小技

### 頻度カウント

`dict` か `collections.Counter`。
→ `examples_array.py` `demo_frequency()` 参照

### Prefix Sum (累積和)

範囲和を **O(1)** で返す。

```
arr    = [1, 2, 3, 4, 5]
prefix = [0, 1, 3, 6,10,15]   # prefix[i] = arr[0..i-1] の和

sum(arr[L..R]) = prefix[R+1] - prefix[L]
sum(arr[1..3]) = prefix[4] - prefix[1] = 10 - 1 = 9
```

→ `examples_array.py` `demo_prefix_sum()` 参照

---

## デバッグの定石

### 可視化 (バブルソートの過程をプリント)

→ `examples_array.py` `demo_visualize_bubble_sort()` 参照

### 境界値テストのテンプレ

```
ケースに必ず含める:
  - 通常       [1,2,3]
  - 逆順       [3,2,1]
  - 単一要素   [5]
  - 空         []
  - 負の数     [-1,-2,-3]
```

→ `examples_array.py` `demo_boundary_test()` 参照

---

## ベストプラクティス

### in-place で書ける問題は in-place で

```python
# ✅ 追加メモリなし
for i in range(len(arr) // 2):
    arr[i], arr[~i] = arr[~i], arr[i]

# ⚠ 追加で O(n)
arr = arr[::-1]
```

### 安全なアクセス

```python
def safe_get(arr, i):
    return arr[i] if 0 <= i < len(arr) else None
```

→ `examples_array.py` `demo_inplace_reverse()` / `demo_safe_access()` 参照

---

## まとめ

- **時間計算量**: アクセス O(1) / 探索 O(n)
- **空間計算量**: in-place で減らす
- **キャッシュ**: 連続アクセスが正義
- **境界**: 空・1 要素・最大インデックスを必ず確認
