# 07. Python 文法チートシート (アルゴリズム読解向け)

LeetCode や教材で頻出する「絶妙に分からない書き方」をまとめる。
**型アノテーション**、**range**、**列挙系**、**コンテナの初期化** が中心。

---

## 1. 型アノテーション (`: 型` の正体)

### 1-1. これは何?

```python
seen: set[int] = set()
```

- `seen` → 変数名
- `: set[int]` → **型アノテーション** (この変数は「int の set」だよというメモ)
- `= set()` → 実体 (空の set を作って代入)

つまり 1 行で **「型の宣言」 + 「値の代入」** をやってる。

### 1-2. 動作には影響しない

Python の型アノテーションは **実行時には無視される** (※ 一部例外あり)。

```python
seen: set[int] = set()
seen.add("hello")    # 型と矛盾するが、Python は普通に動く
```

「動く」けど **mypy / pyright などの型チェッカーが警告を出す** ので、コードの意図を伝える・バグを事前に潰す目的で書く。

### 1-3. アノテーション無しでも書ける

```python
seen = set()           # アノテーション無し (動作は同じ)
seen: set[int] = set() # アノテーション有り (意図が読みやすい)
```

慣習: **アルゴリズム教材では「中身が何なのか」を伝えるために書く** ことが多い。

### 1-4. よく出る型の一覧

| 書き方                    | 意味                          | 初期化例                       |
| ------------------------- | ----------------------------- | ------------------------------ |
| `x: int`                  | 整数                          | `x: int = 0`                   |
| `x: float`                | 浮動小数点                    | `x: float = 0.0`               |
| `x: str`                  | 文字列                        | `x: str = ""`                  |
| `x: bool`                 | 真偽値                        | `x: bool = False`              |
| `xs: list[int]`           | int のリスト                  | `xs: list[int] = []`           |
| `xs: tuple[int, int]`     | (int, int) のタプル           | `xs: tuple[int, int] = (0, 0)` |
| `s: set[int]`             | int の集合                    | `s: set[int] = set()`          |
| `d: dict[str, int]`       | キー: str / 値: int の辞書    | `d: dict[str, int] = {}`       |
| `x: int \| None`          | int か None (どちらでも可)    | `x: int \| None = None`        |
| `f: Callable[[int], int]` | int を受け取り int を返す関数 | `f = lambda x: x + 1`          |

> **メモ**: `set[int]` のような書き方は **Python 3.9 以降**。それより古いと `Set[int]` (`from typing import Set`) を使う。LeetCode は 3.10+ なので新記法でOK。

### 1-5. 関数のアノテーション

```python
def contains_duplicate(nums: list[int]) -> bool:
    ...
```

- `nums: list[int]` → 引数 nums は「int のリスト」
- `-> bool` → 戻り値は bool

これも「動作は変わらない」が「読みやすさ」のために書く。

---

## 2. `range()` の全パターン

`range()` は **「数列を生成する」** 関数。for ループの友達。

### 2-1. 1 引数: `range(n)`

```python
for i in range(5):
    print(i)
# 0, 1, 2, 3, 4   ← 5 は含まない
```

- 開始は **0**
- 終了は **n の手前** (n は入らない)
- 全部で **n 個** の数を生成

### 2-2. 2 引数: `range(start, stop)`

```python
for i in range(2, 6):
    print(i)
# 2, 3, 4, 5      ← 6 は含まない
```

- 開始は `start` (含む)
- 終了は `stop` の手前 (含まない)
- 数は `stop - start` 個

### 2-3. 3 引数: `range(start, stop, step)`

```python
for i in range(0, 10, 2):
    print(i)
# 0, 2, 4, 6, 8   ← step ずつジャンプ
```

```python
for i in range(10, 0, -1):
    print(i)
# 10, 9, 8, ..., 1   ← 逆順 (step が負)
```

### 2-4. アルゴリズムでの頻出パターン

```python
# 配列を全部見る
for i in range(len(nums)):
    print(nums[i])

# 隣同士を比較 (i=0 で nums[-1] とぶつかるのを避ける)
for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        ...

# 全ペアを見る (i < j を保証)
for i in range(n):
    for j in range(i + 1, n):
        ...

# 逆順にループ
for i in range(len(nums) - 1, -1, -1):
    ...
```

### 2-5. `range` は数列を「実体化しない」

```python
r = range(10 ** 9)   # 一瞬で終わる (10 億個作らない)
```

`range` は **必要な時に値を生成する** だけ (遅延評価)。なので巨大な range を作ってもメモリは食わない。

---

## 3. コンテナの初期化と「空判定」

### 3-1. 空のコンテナ

```python
xs: list[int] = []         # 空リスト
ys: list[int] = list()     # 同じ意味

s: set[int] = set()        # 空 set
                            # ※ {} は空 dict なので set にはならない (重要)

d: dict[int, int] = {}     # 空 dict
e: dict[int, int] = dict() # 同じ意味

t: tuple[int, ...] = ()    # 空タプル
```

> **よくある罠**: `s = {}` は **空 dict**。**空 set ではない**。空 set が欲しい時は `set()`。

### 3-2. 1 要素のタプル

```python
t = (1,)    # 1 要素のタプル (カンマが必須)
t = (1)     # ただの int 1 (カッコは無視される)
```

### 3-3. 初期値を入れて作る

```python
zeros: list[int] = [0] * 5     # [0, 0, 0, 0, 0]
grid: list[list[int]] = [[0] * 3 for _ in range(2)]
# [[0, 0, 0], [0, 0, 0]]  ← 2D 配列
```

> **罠**: `[[0] * 3] * 2` は **同じリストの参照を共有する** ので 1 箇所変えると全部変わる。**`[... for _ in range(n)]` が安全**。

---

## 4. 列挙系 (`enumerate`, `zip`)

### 4-1. `enumerate`: index と要素を同時に取る

```python
for i, x in enumerate(["a", "b", "c"]):
    print(i, x)
# 0 a
# 1 b
# 2 c
```

`for i in range(len(arr)): arr[i]` より読みやすい。アルゴリズムの「i 番目の要素を見ながら index も欲しい」時の定番。

### 4-2. `zip`: 複数のリストを横並びに

```python
for a, b in zip([1, 2, 3], ["a", "b", "c"]):
    print(a, b)
# 1 a
# 2 b
# 3 c
```

長さが違う時は **短い方に合わせて止まる**。

---

## 5. アンパック (`*`, `_`)

### 5-1. アンパック代入

```python
a, b = 1, 2          # a=1, b=2
a, b = b, a          # スワップ (Python の名物)

first, *rest = [1, 2, 3, 4]   # first=1, rest=[2, 3, 4]
*init, last = [1, 2, 3, 4]    # init=[1, 2, 3], last=4
```

### 5-2. `_` は「使わない」のサイン

```python
for _ in range(5):   # 5 回繰り返すだけ。i は使わない
    print("hello")
```

`_` は変数名として有効だけど、慣習的に **「使わないよ」のマーク**。

---

## 6. 内包表記 (comprehension)

### 6-1. リスト内包表記

```python
squares = [x * x for x in range(5)]
# [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

等価な for ループ:

```python
squares = []
for x in range(5):
    squares.append(x * x)
```

### 6-2. set / dict 内包表記

```python
s = {x for x in nums}              # set 内包表記
d = {x: x * x for x in range(5)}   # dict 内包表記
```

`{}` の中に `key: value` があれば dict、無ければ set。

---

## 7. アルゴリズム頻出コンテナ早見表 (3 大 + BFS の deque + top-k の heapq)

| コンテナ | 初期化                   | 追加           | 存在チェック     | 削除                        | 用途                          |
| -------- | ------------------------ | -------------- | ---------------- | --------------------------- | ----------------------------- |
| `list`   | `xs: list[int] = []`     | `xs.append(v)` | `v in xs` (O(N)) | `xs.pop()` / `xs.remove(v)` | 順序あり、index アクセス      |
| `set`    | `s: set[int] = set()`    | `s.add(v)`     | `v in s` (O(1))  | `s.discard(v)`              | 存在チェック・重複除去        |
| `dict`   | `d: dict[str, int] = {}` | `d[k] = v`     | `k in d` (O(1))  | `del d[k]`                  | キーから値を引く (二点和など) |
| `deque`  | `q: deque[int] = deque()` | `q.append(v)`  | `v in q` (O(N))  | `q.popleft()` (O(1))        | BFS のキュー (先入れ先出し)   |
| `heapq`  | `h: list[int] = []`       | `heappush(h,v)`| `v in h` (O(N))  | `heappop(h)` (O(log N))     | top-k・優先度順 (Dijkstra)    |

> **deque**: `from collections import deque` で import する。初期値ありは `deque([root])` のように iterable を渡す (空なら `deque()`)。
> 型注釈は `q: deque[TreeNode]` のように中身の型を書く。
> list でも `append` / `pop` はできるが、先頭取り出し `list.pop(0)` は **O(N)** (全要素が左に詰め直される)。
> front を **O(1)** で抜きたい BFS では `deque.popleft()` を使うのが定石。

> **heapq**: `import heapq` で import する。専用の型は無く **list をそのまま heap として扱う** (だから初期化は `[]`、型注釈も `list[int]`)。
> **min heap がデフォルト**。`heappush(h, v)` / `heappop(h)` で常に**最小**が出る。覗くだけなら `h[0]` で **O(1)**。
> max heap が欲しい時は **符号を反転**して入れる: `heappush(h, -v)` → 取り出しは `-heapq.heappop(h)`。タプルなら `(-priority, payload)`。
> 既存 list の一括 heap 化は `heapq.heapify(h)` で **O(N)** (全部 sort するより速い)。
> `v in h` が **O(N)** なのは中身がただの list だから。heap は「最小を速く出す」専用で、**任意要素の検索は速くない** (そこは set/dict の役目)。詳細は `../08_heaps_priority_queues/README.md`。

---

## 8. つまずきやすい記法まとめ

| 書き方                     | 意味                      | 「あ、これか」のヒント                     |
| -------------------------- | ------------------------- | ------------------------------------------ |
| `seen: set[int] = set()`   | int の空 set              | `set()` でなく `{}` だと dict になる罠注意 |
| `cnt: dict[int, int] = {}` | int→int の空 dict         | `{}` は空 dict、`set()` は空 set           |
| `range(n)`                 | 0 から n-1 まで           | n は**含まない**                           |
| `range(1, n)`              | 1 から n-1 まで           | 最初を 0 でなく 1 にしたい時               |
| `range(n-1, -1, -1)`       | n-1 から 0 まで逆順       | 最後の `-1` が「終端の手前」になるので必要 |
| `enumerate(xs)`            | (index, value) のペア     | `for i, x in ...` で受ける                 |
| `zip(a, b)`                | 2 つを並走                | 長さが違うと短い方で止まる                 |
| `for _ in range(n)`        | n 回繰り返すだけ          | 変数を使わないことの宣言                   |
| `nums[i:j]`                | i から j-1 までの部分配列 | コピーが作られるので O(N)                  |
| `nums[::-1]`               | 逆順コピー                | スライスの 3 番目が step                   |
| `*rest` (関数引数)         | 残り全部を集める          | `def f(a, *rest)`                          |
| `**kwargs`                 | キーワード引数を集める    | `def f(**kw)`                              |

---

## 9. 「これ書ける?」セルフチェック

以下を見て、何をしているか一瞬で読めれば OK。

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}                       # 値 -> index
    for i, x in enumerate(nums):                    # 列挙
        need = target - x
        if need in seen:                            # O(1) 存在チェック
            return [seen[need], i]
        seen[x] = i
    return []
```

読めるべきポイント:

- `list[int]`, `dict[int, int]` の型の意味
- `enumerate(nums)` で index と値を取る
- `in seen` で O(1) チェック
- `seen[x] = i` で dict に追加

---

## 関連

- `04_sets.md` — set の本体機能
- `05_loops_and_control_flow.md` — for/while と range の使い方
- `examples_python_idioms.py` — 動かして確認できるサンプル
- `../../Top6InterviewConcepts/01_hashmap/contains_duplicate.py` — `seen: set[int] = set()` の実例
