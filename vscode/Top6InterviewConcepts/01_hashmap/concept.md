# Hashmap（ハッシュマップ）

## 一言でいうと

**「キーから値を O(1) で引き出せる箱」**。Python では `dict`、`set` が代表例。

## なぜ最重要なのか

面接の 6 大概念のうち、Hashmap は「単独で問題を解くケース」と「他の解法の補助として使うケース」の **両方で頻出する**。
Sliding Window でも DFS でも、Hashmap を組み合わせることで O(N²) → O(N) に落ちる問題が大量にある。

## 計算量

| 操作 | 平均 | 最悪 |
| ---- | ---- | ---- |
| 挿入 | O(1) | O(N) |
| 検索 | O(1) | O(N) |
| 削除 | O(1) | O(N) |

- 平均 O(1) は **償却計算量**（amortized）。内部で衝突 (collision) が起きるとリハッシュが走るが、長期的には 1 操作あたり O(1) に収束する。
- 面接では「O(1) です」と答えれば十分。よほど深堀りされない限り amortized の話は不要。

## Python での主なデータ構造

```python
# dict: キーと値のペア
counts = {"apple": 3, "banana": 2}

# set: 値だけ（重複なし）
seen = {1, 2, 3}

# defaultdict: キーが無いとき自動で初期値
from collections import defaultdict
groups = defaultdict(list)
groups["a"].append(1)  # KeyError にならない

# Counter: 要素の出現回数を数える専用
from collections import Counter
c = Counter("mississippi")
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})
```

## 「Hashmap で解ける」と気付くサイン

1. **「ある値が存在するか？」** を高速に確認したい
   - 例: 重複検出、既出チェック
2. **「ある値の出現回数」** を数えたい
   - 例: アナグラム判定、頻度カウント
3. **「2 つの値の組み合わせ」** を探したい
   - 例: Two Sum（合計が target になるペア）
4. **「インデックスや位置の対応関係」** を覚えておきたい
   - 例: 「最後に出現した位置」を記録して Sliding Window と組み合わせる

## キーにできるもの・できないもの

```python
# OK: イミュータブルな型
d = {}
d[1] = "ok"
d["str"] = "ok"
d[(1, 2)] = "tuple もキーにできる"

# NG: ミュータブルな型はキーにできない
d[[1, 2]] = "list はエラー"  # TypeError: unhashable type: 'list'
d[{1, 2}] = "set もエラー"    # TypeError
```

ハッシュ可能 = `hash(x)` を呼べる = 値が変わらないことが保証されている。

## アンチパターン

### NG 1: in 演算子をリストに使う

```python
# ダメ: O(N) になる
nums = [1, 2, 3, 4, 5]
if 3 in nums:  # 線形探索
    ...

# OK: set にしておけば O(1)
nums_set = set(nums)
if 3 in nums_set:
    ...
```

### NG 2: 不要に dict.keys() を回す

```python
# 冗長
for key in d.keys():
    ...

# シンプル
for key in d:
    ...
```

### NG 3: 値を取り出してから存在チェック

```python
# 古典的な KeyError ハンドリング
if key in d:
    val = d[key]
else:
    val = default

# よりシンプル
val = d.get(key, default)
```

## 代表問題

- **Two Sum**（このフォルダ `two_sum.py`）
- Group Anagrams
- Contains Duplicate
- Valid Anagram
- Longest Consecutive Sequence

## このフォルダで学ぶ問題

`two_sum.py` を参照。ナイーブ O(N²) 解法から Hashmap で O(N) に落とす過程を、計算量とともに解説する。
