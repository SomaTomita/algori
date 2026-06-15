# Binary Search

> 探索範囲を毎ステップ「半分にカット」して、O(n) を O(log n) に落とすテクニック。

---

## 数字当てゲーム (1〜80 を二分)

「1〜80 のどれか当てて」と言われたら、真ん中を聞くのが最速。

```
範囲: 1 ─────────────── 40 ─────────────── 80
        L                M                 R
        "40 より大きい?" → Yes

範囲:                    41 ──── 60 ──── 80
                          L      M       R
        "60 より大きい?" → No

範囲:                    41 ── 50 ── 60
                          L    M     R
        "50 より大きい?" → Yes

...
80 → 40 → 20 → 10 → 5 → 3 → 2 → 1
log2(80) ≈ 6.3 回で 1 つに絞れる
```

毎回半分になるので、`n=80` でも **7 回以内** で確定。これが O(log n) の威力。

---

## Vanilla テンプレ (ソート済み配列で target を探す)

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1   # 右半分へ
        else:
            right = mid - 1  # 左半分へ
    return -1
```

ポイント: `left <= right` (等号必須)、`mid = (left+right)//2`、見つけたら即 return。

---

## Monotonic Condition (一般化)

実は **ソート済み配列でなくても** 使える。条件が「ある点を境に F → T へ一方向に切り替わる」(monotonic) なら OK。

```
index :  0   1   2   3   4   5
cond  : [ F   F   F   T   T   T ]
                     ↑
                  ここが boundary (最初の True)
```

`feasible(i)` が `i` を増やすにつれ「F → T」へしか変わらないなら、二分探索で boundary を見つけられる。

代表例:
- ソート済み配列で `arr[i] >= target` の最小 i (lower_bound)
- Koko Eating Bananas で「速度 k で間に合うか?」
- Min in Rotated Sorted Array で「`nums[i] <= 末尾値` か?」

---

## Find First True テンプレ

```python
def find_first_true(arr):
    left, right = 0, len(arr) - 1
    boundary = -1                 # まだ True を見つけてない印
    while left <= right:
        mid = (left + right) // 2
        if feasible(arr[mid]):    # True なら候補を更新して左へ寄せる
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1        # False なら右へ
    return boundary
```

ポイント: True を見つけたら `boundary = mid` を **記録してから** `right = mid - 1` で左を探す。
取りこぼしは起きない (記録済みなので)。

---

## 計算量

| 操作            | 時間     | 空間  |
| --------------- | -------- | ----- |
| Vanilla 検索    | O(log n) | O(1)  |
| Find First True | O(log n) | O(1)  |

毎ループで範囲が半分 → ループ回数 = log2(n) 回。

---

## 「これ二分探索だな」の見分けポイント

1. **ソート済み配列** で要素を探す/挿入位置を求める → Vanilla テンプレ。
2. **Monotonic な条件** (F...FT...T) があり、「最初の True / 最後の False」の境界が欲しい → Find First True。
3. **最小/最大の境界探し** で「k に対して feasible(k) が単調」(例: 最小の速度・最大の容量) → 答えそのものを二分探索 (parametric search)。
4. ループで O(n) 走査しているが、**順序を保ったまま跳び石的に進めばよい** と気づいたとき。
5. 配列がローテートされている / ピーク / 山型でも、片側に monotonic 性があれば適用可能。
