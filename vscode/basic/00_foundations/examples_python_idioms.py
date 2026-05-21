"""難しめの Python 文法・イディオム集.

「他人のコードを読んでいて急に止まる」原因になりやすい書き方を集めた。
それぞれ
    1) 1 行版 (本物のコード)
    2) for ループに展開した等価版 (頭の中で再現する用)
    3) なぜそう書くと得かの一言メモ
の 3 点セットで載せている。

実行:
    python3 examples_python_idioms.py
"""

from __future__ import annotations

import functools
import itertools
import sys
from collections import Counter, defaultdict, deque
from operator import itemgetter
from typing import Iterator


# ---------------------------------------------------------------------------
# 1. 内包表記 (list / dict / set / nested)
# ---------------------------------------------------------------------------
def demo_comprehensions() -> None:
    """1 行に圧縮された for ループ。読めるかが分かれ目。"""
    print("== demo_comprehensions ==")

    nums = [1, 2, 3, 4, 5]

    # ----- (1) list 内包: 値を変換する -----
    squared = [x * x for x in nums]
    # 等価:
    #   squared = []
    #   for x in nums:
    #       squared.append(x * x)
    print(f"squared    : {squared}")
    # → 出力: squared    : [1, 4, 9, 16, 25]

    # ----- (2) 条件付き (filter): `if` は for の後ろ -----
    evens = [x for x in nums if x % 2 == 0]
    print(f"evens      : {evens}")
    # → 出力: evens      : [2, 4]

    # ----- (3) if-else を「値の式」として書く: 位置が違う -----
    # 三項演算子 `A if cond else B` を for の前に置くと「変換ルール」になる。
    # filter の `if` (for の後ろ) と区別すること。
    parity = ["even" if x % 2 == 0 else "odd" for x in nums]
    print(f"parity     : {parity}")
    # → 出力: parity     : ['odd', 'even', 'odd', 'even', 'odd']

    # ----- (4) ネスト内包: 行列を作る -----
    size = 3
    matrix = [[i * size + j for j in range(size)] for i in range(size)]
    # 等価:
    #   matrix = []
    #   for i in range(size):       # 外側
    #       row = []
    #       for j in range(size):   # 内側
    #           row.append(i * size + j)
    #       matrix.append(row)
    print(f"matrix     : {matrix}")
    # → 出力: matrix     : [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    # ----- (5) ネスト平坦化: for が 2 つ並ぶ (左から外→内) -----
    flat = [x for row in matrix for x in row]
    # 等価:
    #   flat = []
    #   for row in matrix:
    #       for x in row:
    #           flat.append(x)
    print(f"flat       : {flat}")
    # → 出力: flat       : [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # ----- (6) dict 内包: key:value を一気に作る -----
    sq_map = {x: x * x for x in nums}
    print(f"sq_map     : {sq_map}")
    # → 出力: sq_map     : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # ----- (7) set 内包: 重複は勝手に消える -----
    words = ["apple", "banana", "ant", "berry"]
    initials = {w[0] for w in words}
    print(f"initials   : {sorted(initials)}")
    # → 出力: initials   : ['a', 'b']


# ---------------------------------------------------------------------------
# 2. ジェネレータ式 (lazy 評価)
# ---------------------------------------------------------------------------
def demo_generator_expressions() -> None:
    """[]→() に変えるだけで、メモリに全部載せず逐次生成にできる."""
    print("== demo_generator_expressions ==")

    # list 内包: 100 万個を全部メモリに置く
    big_list = [x * x for x in range(1_000_000)]
    print(f"list 先頭5: {big_list[:5]}")
    # → 出力: list 先頭5: [0, 1, 4, 9, 16]

    # ジェネレータ式: 必要になったら 1 つずつ計算する。 () 注意
    big_gen = (x * x for x in range(1_000_000))
    # ↑ この時点ではまだ何も計算していない (lazy)
    print(f"gen 型    : {type(big_gen).__name__}")
    # → 出力: gen 型    : generator

    # sum() のような関数に直接渡せる (中間 list を作らずに済む = メモリ節約)
    total = sum(x * x for x in range(100))   # () すら省ける場合あり
    print(f"sum 0..99 : {total}")
    # → 出力: sum 0..99 : 328350

    # ジェネレータは 1 度だけ走査できる。再利用したいなら list にする。
    g = (x for x in range(3))
    print(f"first run : {list(g)}")   # → 出力: first run : [0, 1, 2]
    print(f"second run: {list(g)}")   # → 出力: second run: []  (もう空)


# ---------------------------------------------------------------------------
# 3. アンパック / star 式
# ---------------------------------------------------------------------------
def demo_unpacking() -> None:
    """左辺で複数同時に受ける、 * で残りをまとめる、 swap、 splat call."""
    print("== demo_unpacking ==")

    # ----- 多重代入 -----
    a, b, c = [1, 2, 3]
    print(f"a, b, c          : {a}, {b}, {c}")
    # → 出力: a, b, c          : 1, 2, 3

    # ----- swap (一時変数なし) -----
    a, b = b, a
    print(f"after swap a, b  : {a}, {b}")
    # → 出力: after swap a, b  : 2, 1
    # 仕組み: 右辺で先に tuple (b, a) を作ってから左辺に分配する。

    # ----- *rest で残りを list で受ける -----
    head, *rest = [1, 2, 3, 4, 5]
    print(f"head={head}, rest={rest}")
    # → 出力: head=1, rest=[2, 3, 4, 5]

    *init, last = [1, 2, 3, 4, 5]
    print(f"init={init}, last={last}")
    # → 出力: init=[1, 2, 3, 4], last=5

    a, *mid, z = [1, 2, 3, 4, 5]
    print(f"a={a}, mid={mid}, z={z}")
    # → 出力: a=1, mid=[2, 3, 4], z=5

    # ----- 関数呼び出しでの splat: list/tuple を引数列に展開 -----
    def add3(x: int, y: int, z: int) -> int:
        return x + y + z

    args = [10, 20, 30]
    print(f"add3(*args)      : {add3(*args)}")
    # → 出力: add3(*args)      : 60

    kwargs = {"x": 1, "y": 2, "z": 3}
    print(f"add3(**kwargs)   : {add3(**kwargs)}")
    # → 出力: add3(**kwargs)   : 6

    # ----- リテラル中の展開: 結合の代わりに使える -----
    a_list = [1, 2, 3]
    b_list = [4, 5]
    merged = [*a_list, *b_list, 99]   # = [1,2,3,4,5,99]
    print(f"merged           : {merged}")
    # → 出力: merged           : [1, 2, 3, 4, 5, 99]

    d1 = {"a": 1, "b": 2}
    d2 = {"b": 99, "c": 3}                  # b は d2 で上書き
    merged_dict = {**d1, **d2}
    print(f"merged_dict      : {merged_dict}")
    # → 出力: merged_dict      : {'a': 1, 'b': 99, 'c': 3}


# ---------------------------------------------------------------------------
# 4. スライス小技
# ---------------------------------------------------------------------------
def demo_slicing_tricks() -> None:
    """`arr[start:stop:step]` の step が見落とされがち."""
    print("== demo_slicing_tricks ==")

    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(f"arr[2:5]   : {arr[2:5]}")
    # → 出力: arr[2:5]   : [2, 3, 4]   (start 含む / stop 含まず)

    print(f"arr[::2]   : {arr[::2]}")
    # → 出力: arr[::2]   : [0, 2, 4, 6, 8]   (1 つおき)

    print(f"arr[1::2]  : {arr[1::2]}")
    # → 出力: arr[1::2]  : [1, 3, 5, 7, 9]   (奇数 index)

    print(f"arr[::-1]  : {arr[::-1]}")
    # → 出力: arr[::-1]  : [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]   (反転)

    print(f"arr[::-2]  : {arr[::-2]}")
    # → 出力: arr[::-2]  : [9, 7, 5, 3, 1]   (後ろから 1 つおき)

    # ----- ~i は -i-1 と同じ → 「末尾から数えるインデックス」 -----
    # 配列の中央スワップで使うと書きやすい。
    s = [10, 20, 30, 40, 50]
    for i in range(len(s) // 2):
        s[i], s[~i] = s[~i], s[i]
        # i=0: s[0] と s[~0]=s[-1] を交換
        # i=1: s[1] と s[~1]=s[-2] を交換
    print(f"reversed s : {s}")
    # → 出力: reversed s : [50, 40, 30, 20, 10]

    # ----- shallow copy: arr[:] -----
    original = [1, 2, 3]
    copy = original[:]
    copy.append(99)
    print(f"original={original}, copy={copy}")
    # → 出力: original=[1, 2, 3], copy=[1, 2, 3, 99]


# ---------------------------------------------------------------------------
# 5. walrus 演算子 := (代入式, 3.8+)
# ---------------------------------------------------------------------------
def demo_walrus() -> None:
    """式の中で代入と評価を同時にする. 過剰使用は読みづらいので狙い撃ちで."""
    print("== demo_walrus ==")

    arr = [1, 2, 3, 4, 5, 6, 7, 8]

    # ----- if の条件で長さを 1 度だけ計算して使い回す -----
    if (n := len(arr)) > 5:
        print(f"len={n} は 5 より大きい")
        # → 出力: len=8 は 5 より大きい

    # ----- while で「読む & チェック」を 1 行に -----
    # 等価コード (walrus なし):
    #   it = iter(arr)
    #   while True:
    #       x = next(it, None)
    #       if x is None or x >= 5:
    #           break
    #       print(x)
    it = iter(arr)
    while (x := next(it, None)) is not None and x < 5:
        print(f"while loop -> {x}")
        # → 出力:
        #   while loop -> 1
        #   while loop -> 2
        #   while loop -> 3
        #   while loop -> 4

    # ----- 内包表記内で計算結果を再利用 -----
    # 重い f(x) を 2 回呼ばないようにする
    def f(x: int) -> int:
        return x * x

    big_squares = [y for x in arr if (y := f(x)) > 10]
    # ↑ y は内包表記の中だけで生きる
    print(f"big_squares: {big_squares}")
    # → 出力: big_squares: [16, 25, 36, 49, 64]


# ---------------------------------------------------------------------------
# 6. f-string のフォーマット指定
# ---------------------------------------------------------------------------
def demo_fstring_formatting() -> None:
    """`{value:spec}` の spec が読めると print デバッグが速い."""
    print("== demo_fstring_formatting ==")

    pi = 3.141592653589793
    print(f"小数 2 桁  : {pi:.2f}")
    # → 出力: 小数 2 桁  : 3.14

    print(f"指数表記   : {pi:.3e}")
    # → 出力: 指数表記   : 3.142e+00

    n = 1234567
    print(f"3 桁区切り : {n:,}")
    # → 出力: 3 桁区切り : 1,234,567

    print(f"2 進数     : {n:b}")
    # → 出力: 2 進数     : 100101101011010000111

    print(f"16 進数    : {n:#x}")
    # → 出力: 16 進数    : 0x12d687

    # ----- 桁揃え (テーブル整形に使う) -----
    rows = [("apple", 100), ("banana", 50), ("blueberry", 220)]
    for name, qty in rows:
        # < 左寄せ, > 右寄せ, ^ 中央寄せ
        print(f"  {name:<10} | {qty:>5}")
        # → 出力:
        #     apple      |   100
        #     banana     |    50
        #     blueberry  |   220

    # ----- 自己ドキュメント = (3.8+): デバッグで超便利 -----
    x = 42
    y = "hello"
    print(f"{x=}, {y=}")
    # → 出力: x=42, y='hello'  (変数名と値を一緒に出す)


# ---------------------------------------------------------------------------
# 7. ソートに key= を渡す (lambda / itemgetter)
# ---------------------------------------------------------------------------
def demo_sort_with_key() -> None:
    """sorted/sort は key= で「比較に使う値」を指定できる."""
    print("== demo_sort_with_key ==")

    people = [
        ("Alice", 30),
        ("Bob", 25),
        ("Carol", 30),
        ("Dave", 22),
    ]

    # ----- lambda で 2 番目の要素 (年齢) でソート -----
    by_age = sorted(people, key=lambda p: p[1])
    print(f"by_age           : {by_age}")
    # → 出力: by_age           : [('Dave', 22), ('Bob', 25), ('Alice', 30), ('Carol', 30)]

    # ----- 同じことを itemgetter で. lambda より速い & 読みやすい -----
    by_age2 = sorted(people, key=itemgetter(1))
    print(f"by_age (getter)  : {by_age2}")
    # → 出力: by_age (getter)  : [('Dave', 22), ('Bob', 25), ('Alice', 30), ('Carol', 30)]

    # ----- 複数キー: 年齢昇順, 同じなら名前昇順 -----
    multi = sorted(people, key=lambda p: (p[1], p[0]))
    print(f"multi key        : {multi}")
    # → 出力: multi key        : [('Dave', 22), ('Bob', 25), ('Alice', 30), ('Carol', 30)]

    # ----- 降順: reverse=True か、 key で - を付ける (数値のみ) -----
    desc = sorted(people, key=lambda p: -p[1])
    print(f"desc by age      : {desc}")
    # → 出力: desc by age      : [('Alice', 30), ('Carol', 30), ('Bob', 25), ('Dave', 22)]

    # ----- 昇順 + 降順を混ぜる: 数値以外でも - は使えないので別解 -----
    # 年齢昇順, 同じなら名前降順 → 名前は negate できないので reverse の組合せで作る
    mixed = sorted(people, key=lambda p: p[0], reverse=True)
    mixed = sorted(mixed, key=lambda p: p[1])  # stable sort なので OK
    print(f"age asc, name dsc: {mixed}")
    # → 出力: age asc, name dsc: [('Dave', 22), ('Bob', 25), ('Carol', 30), ('Alice', 30)]


# ---------------------------------------------------------------------------
# 8. for-else / while-else (break しなければ実行される)
# ---------------------------------------------------------------------------
def demo_for_else() -> None:
    """ループの else は break で抜けなかった時だけ動く. 探索のフラグ代わり."""
    print("== demo_for_else ==")

    arr = [1, 3, 5, 7, 9]
    target = 4

    # ----- 「見つかったら break、見つからなかったら else」 -----
    for x in arr:
        if x == target:
            print(f"見つかった: {x}")
            break
    else:
        print(f"{target} は見つからなかった")
        # → 出力: 4 は見つからなかった

    target = 5
    for x in arr:
        if x == target:
            print(f"見つかった: {x}")
            # → 出力: 見つかった: 5
            break
    else:
        print("こちらは実行されない")


# ---------------------------------------------------------------------------
# 9. 連鎖比較 / 三項演算子 / short-circuit
# ---------------------------------------------------------------------------
def demo_conditional_tricks() -> None:
    print("== demo_conditional_tricks ==")

    # ----- 連鎖比較: 数学の不等式そのまま書ける -----
    x = 5
    if 0 <= x < 10:
        # = (0 <= x) and (x < 10) と同じ
        print(f"{x} は 0 以上 10 未満")
        # → 出力: 5 は 0 以上 10 未満

    # ----- 三項演算子: y = A if cond else B -----
    n = 7
    label = "even" if n % 2 == 0 else "odd"
    print(f"label : {label}")
    # → 出力: label : odd

    # ----- or による「デフォルト値」-----
    name = ""
    display = name or "(no name)"   # 空文字は falsy → 右が選ばれる
    print(f"display: {display}")
    # → 出力: display: (no name)
    # 注意: 0 や [] も falsy なので、 None だけを判定したいときは
    #       `display = name if name is not None else "..."` を使う.

    # ----- and による「ガード」-----
    user: dict | None = {"name": "Alice"}
    upper_name = user and user["name"].upper()
    # user が None なら user (=None) を返して短絡。安全に . にアクセスできる
    print(f"upper_name: {upper_name}")
    # → 出力: upper_name: ALICE


# ---------------------------------------------------------------------------
# 10. デコレータ + lru_cache (メモ化)
# ---------------------------------------------------------------------------
def demo_lru_cache_memoization() -> None:
    """素朴フィボナッチ O(2^n) → @cache で O(n) に."""
    print("== demo_lru_cache_memoization ==")

    @functools.lru_cache(maxsize=None)
    def fib(n: int) -> int:
        # ↑ デコレータは fib = lru_cache(...)(fib) と同義
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    print(f"fib(30) = {fib(30)}")
    # → 出力: fib(30) = 832040

    # キャッシュ効果を確認
    info = fib.cache_info()
    print(f"cache_info: hits={info.hits}, misses={info.misses}")
    # → 出力例: cache_info: hits=28, misses=31


# ---------------------------------------------------------------------------
# 11. ジェネレータ関数 (yield / yield from)
# ---------------------------------------------------------------------------
def demo_yield_basics() -> None:
    """yield を含む関数 = ジェネレータ. 呼んだ瞬間ではなく next() で動く."""
    print("== demo_yield_basics ==")

    def countdown(n: int) -> Iterator[int]:
        # 関数の中に yield があるとジェネレータになる
        while n > 0:
            yield n
            # ↑ ここで一旦止まり、 next() が呼ばれたら次の行から再開する
            n -= 1

    g = countdown(3)
    print(f"type    : {type(g).__name__}")
    # → 出力: type    : generator
    print(f"iterate : {list(g)}")
    # → 出力: iterate : [3, 2, 1]

    # ----- yield from: 別のイテラブルを丸ごと流す -----
    def chain_two(a: list[int], b: list[int]) -> Iterator[int]:
        yield from a
        yield from b
        # 等価:
        #   for x in a: yield x
        #   for x in b: yield x

    print(f"chained : {list(chain_two([1, 2], [9, 8, 7]))}")
    # → 出力: chained : [1, 2, 9, 8, 7]


# ---------------------------------------------------------------------------
# 12. itertools の必修パターン
# ---------------------------------------------------------------------------
def demo_itertools_essentials() -> None:
    """組合せ・直積・累積。 自分で 2 重ループを書く前に検索する."""
    print("== demo_itertools_essentials ==")

    # ----- product: デカルト積. 2 重ループを 1 行で -----
    print(f"product   : {list(itertools.product([1, 2], ['a', 'b']))}")
    # → 出力: product   : [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

    # ----- combinations: 順序なし、 r 個選ぶ全パターン -----
    print(f"combos r=2: {list(itertools.combinations([1, 2, 3, 4], 2))}")
    # → 出力: combos r=2: [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

    # ----- permutations: 順序あり -----
    print(f"perms r=2 : {list(itertools.permutations([1, 2, 3], 2))}")
    # → 出力: perms r=2 : [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

    # ----- accumulate: 累積和 (prefix sum) を 1 行で -----
    print(f"accumulate: {list(itertools.accumulate([1, 2, 3, 4, 5]))}")
    # → 出力: accumulate: [1, 3, 6, 10, 15]

    # ----- chain: 複数のイテラブルを連結 -----
    print(f"chain     : {list(itertools.chain([1, 2], [3, 4], [5]))}")
    # → 出力: chain     : [1, 2, 3, 4, 5]

    # ----- groupby: 連続する同じ値をグループ化 (sort してから使うのが基本) -----
    data = "aaabbbccddaa"
    grouped = [(k, len(list(g))) for k, g in itertools.groupby(data)]
    print(f"groupby   : {grouped}")
    # → 出力: groupby   : [('a', 3), ('b', 3), ('c', 2), ('d', 2), ('a', 2)]


# ---------------------------------------------------------------------------
# 13. collections の必修クラス
# ---------------------------------------------------------------------------
def demo_collections_essentials() -> None:
    print("== demo_collections_essentials ==")

    # ----- Counter: 頻度カウントの 1 行版 -----
    text = "abracadabra"
    cnt = Counter(text)
    print(f"counter      : {dict(cnt)}")
    # → 出力: counter      : {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
    print(f"most_common 2: {cnt.most_common(2)}")
    # → 出力: most_common 2: [('a', 5), ('b', 2)]

    # ----- defaultdict: 未登録 key を自動で初期化 -----
    # dict だと:
    #   if k not in d: d[k] = []
    #   d[k].append(...)
    # と書く必要がある
    groups: dict[str, list[str]] = defaultdict(list)
    for word in ["apple", "ant", "banana", "berry", "cat"]:
        groups[word[0]].append(word)
    print(f"groups       : {dict(groups)}")
    # → 出力: groups       : {'a': ['apple', 'ant'], 'b': ['banana', 'berry'], 'c': ['cat']}

    # ----- deque: 両端 O(1) の追加削除 (BFS / sliding window で必須) -----
    dq: deque[int] = deque([1, 2, 3])
    dq.appendleft(0)        # 先頭追加 O(1)
    dq.append(4)            # 末尾追加 O(1)
    dq.popleft()            # 先頭削除 O(1) → list だと O(n)
    print(f"deque        : {list(dq)}")
    # → 出力: deque        : [1, 2, 3, 4]


# ---------------------------------------------------------------------------
# 14. zip(*matrix) で転置, enumerate(start=...) など
# ---------------------------------------------------------------------------
def demo_zip_transpose() -> None:
    """zip と * の合わせ技で行列の転置が 1 行になる."""
    print("== demo_zip_transpose ==")

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    # zip(*matrix) は zip([1,2,3], [4,5,6], [7,8,9]) と同じ
    # → 各列をペアにして取り出す = 転置
    transposed = [list(row) for row in zip(*matrix)]
    print(f"transposed : {transposed}")
    # → 出力: transposed : [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    # ----- enumerate に start= を渡す -----
    items = ["a", "b", "c"]
    for i, x in enumerate(items, start=1):
        print(f"  no.{i} = {x}")
        # → 出力:
        #     no.1 = a
        #     no.2 = b
        #     no.3 = c


# ---------------------------------------------------------------------------
# 15. ダンダー (__lt__) でクラスをソート可能にする
# ---------------------------------------------------------------------------
def demo_dunder_methods() -> None:
    """`__lt__` を実装すれば sorted() でそのまま並べられる."""
    print("== demo_dunder_methods ==")

    class Task:
        def __init__(self, name: str, priority: int) -> None:
            self.name = name
            self.priority = priority

        def __repr__(self) -> str:
            # print() / repr() で表示される文字列
            return f"Task({self.name!r}, p={self.priority})"

        def __lt__(self, other: "Task") -> bool:
            # sorted() / heapq はこの比較しか使わない
            return self.priority < other.priority

    tasks = [Task("C", 3), Task("A", 1), Task("B", 2)]
    print(f"sorted: {sorted(tasks)}")
    # → 出力: sorted: [Task('A', p=1), Task('B', p=2), Task('C', p=3)]


# ---------------------------------------------------------------------------
# 16. match / case (構造的パターンマッチ, Python 3.10+)
# ---------------------------------------------------------------------------
# このファイルは 3.9 でもパースできるようにしたいので、 match 文の本体は
# 文字列として保持し、 exec() で実行時に評価する。 3.10 未満ではメッセージのみ。
_MATCH_DEMO_SRC = '''
def _describe(x):
    match x:
        case 0:
            return "zero"
        case int() if x < 0:
            return f"negative int {x}"          # ガード付き
        case int():
            return f"positive int {x}"
        case [a, b]:
            return f"pair ({a}, {b})"           # list/tuple の長さ 2 を分解
        case {"name": str() as name}:
            return f"named: {name}"             # dict の構造で分岐
        case _:
            return "something else"             # default
'''


def demo_match_statement() -> None:
    """if/elif の長い分岐を構造で書ける. 値だけでなく『形』でも分岐できる."""
    print("== demo_match_statement ==")
    if sys.version_info < (3, 10):
        print(f"(Python {sys.version_info.major}.{sys.version_info.minor}: skip — match は 3.10+)")
        return
    ns: dict[str, object] = {}
    exec(_MATCH_DEMO_SRC, ns)
    describe = ns["_describe"]
    for v in [0, -3, 7, [1, 2], {"name": "Alice"}, "?"]:
        print(f"  {v!r:>20} -> {describe(v)}")
    # → 出力 (3.10+):
    #                       0 -> zero
    #                      -3 -> negative int -3
    #                       7 -> positive int 7
    #                  [1, 2] -> pair (1, 2)
    #      {'name': 'Alice'} -> named: Alice
    #                     '?' -> something else


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> None:
    demos = [
        demo_comprehensions,
        demo_generator_expressions,
        demo_unpacking,
        demo_slicing_tricks,
        demo_walrus,
        demo_fstring_formatting,
        demo_sort_with_key,
        demo_for_else,
        demo_conditional_tricks,
        demo_lru_cache_memoization,
        demo_yield_basics,
        demo_itertools_essentials,
        demo_collections_essentials,
        demo_zip_transpose,
        demo_dunder_methods,
        demo_match_statement,
    ]
    for fn in demos:
        fn()
        print()


if __name__ == "__main__":
    main()
