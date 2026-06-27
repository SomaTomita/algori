"""
Fibonacci Number (LeetCode #509)  Easy

フィボナッチ数列の n 番目を求める。
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2)   for n > 1

例:
    n = 4 -> 3   (0, 1, 1, 2, 3)
    n = 10 -> 55

制約 (LeetCode):
    0 <= n <= 30
    ※ 本ファイルでは memo / iter 解法で n=50, 100 でも検算可能
"""

from functools import lru_cache


# ----------------------------------------------------------------------
# 解法 1: ナイーブ再帰  O(2^N)   ※ 学習用、実用 NG
# ----------------------------------------------------------------------
def fib_naive(n: int) -> int:
    """
    定義通りに再帰。同じ部分問題を何度も計算してしまう。

    時間計算量: O(2^N)   実質、二分木の葉まで全部展開する
    空間計算量: O(N)     再帰の深さ

    例: fib(5) の呼び出し木
                fib(5)
              /        \\
          fib(4)       fib(3)
          /    \\       /    \\
       fib(3) fib(2) fib(2) fib(1)
       ...

    fib(2), fib(3) などが何度も登場する。これがメモ化で消せる無駄。
    """
    if n < 2:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# ----------------------------------------------------------------------
# 解法 2: メモ化再帰  O(N)
# ----------------------------------------------------------------------
@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    """
    @lru_cache で結果をキャッシュ。同じ引数で 2 度目以降は即返す。

    時間計算量: O(N)   各 n について「初回だけ」計算する
    空間計算量: O(N)   キャッシュ + 再帰スタック

    手動で書くなら:
        memo = {}
        def f(n):
            if n in memo: return memo[n]
            if n < 2:     return n
            memo[n] = f(n-1) + f(n-2)
            return memo[n]
    """
    if n < 2:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)


# ----------------------------------------------------------------------
# 解法 3: 反復 (ボトムアップ DP)  O(N) 時間, O(1) 空間   ★ 最適
# ----------------------------------------------------------------------
def fib_iter(n: int) -> int:
    """
    必要なのは「直前の 2 つ」だけなので、変数 2 つで十分。
    再帰スタックも消える -> 空間 O(1)。

    時間計算量: O(N)
    空間計算量: O(1)
    """
    if n < 2:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# ----------------------------------------------------------------------
# どれくらい速くなるか (実感)
# ----------------------------------------------------------------------
#
# 呼び出し回数で比較する。
#   - naive は「同じ部分問題」を何度も再計算するので、ほぼ 2^N に近い
#   - memo  は各 n を 1 回だけ計算
#   - iter  は再帰すらせず単純な N ループ
#
#   n     | naive (2^N)         | memo (N)  | iter (N) | 体感
#   ------+---------------------+-----------+----------+------------------
#   10    | ~1,024 ops           | 10 ops    | 10 ops   | どれも一瞬
#   30    | ~10^9 ops            | 30 ops    | 30 ops   | naive: 数秒
#   40    | ~10^12 ops           | 40 ops    | 40 ops   | naive: 数十分以上
#   50    | ~10^15 ops           | 50 ops    | 50 ops   | naive: 一生終わらない
#   1000  | (天文学的)            | 1000 ops  | 1000 ops | naive: 計算不能
#
# 「メモ化」は再帰系アルゴリズムの最重要テクニック。
# 「同じ部分問題が複数回登場する」とき、メモ化で O(N) に落とせる。


# ----------------------------------------------------------------------
# メモ化の本質
# ----------------------------------------------------------------------
#
# 「同じ問い」に「同じ答え」を返すなら、2 回計算する意味は無い。
# fib(3) は何度呼んでも 2。なら最初に計算した 2 を覚えておけば良い。
#
#   naive: 「fib(3) を計算してください」と何度聞かれても毎回計算
#   memo : 「fib(3) を計算してください」と聞かれたら、初回だけ計算し
#          以降は記憶した値を即答
#
# キャッシュという小さなアイデアが、計算量を 2^N から N に圧縮する。
# 動的計画法 (DP) の入口がここにある。


# ----------------------------------------------------------------------
# 【コールスタック版】 fib_naive(5) を「潜る(呼ぶ)/戻る(return)」で追う
#   ★backtracking との違い★ : 戻るとき pop ではなく「数値が返る」。
#   current のような共有状態は無く、各 fib は独立に数を返し、呼んだ側が a+b に使う。
# ----------------------------------------------------------------------
"""
fib(5) を呼ぶところから。各呼び出しは n<2 で return n (基底)、それ以外は
fib(n-1)+fib(n-2) を return。左 fib(n-1) を最後まで計算してから右 fib(n-2)。

depth 0: fib(5)  5≥2 → fib(4)+fib(3) が要る。まず左 fib(4)
         fib(4) ───┐  ★潜る
                    │
depth 1: fib(4) ◀──┘  4≥2 → fib(3)+fib(2)。まず fib(3)
         fib(3) ───┐  ★潜る
                    │
depth 2: fib(3) ◀──┘  3≥2 → fib(2)+fib(1)。まず fib(2)
         fib(2) ───┐  ★潜る
                    │
depth 3: fib(2) ◀──┘  2≥2 → fib(1)+fib(0)。まず fib(1)
         fib(1) ───┐  ★潜る
                    │
depth 4: fib(1) ◀──┘  1<2 → return 1  (基底ケース)
         ─ 値1 を返す ─┐  ★戻る
                        │
depth 3: a=1 を受取 ◀──┘  次に右 fib(0)
         fib(0) ───┐  ★潜る
                    │
depth 4: fib(0) ◀──┘  0<2 → return 0  (基底)
         ─ 値0 ─┐  ★戻る
                 │
depth 3: b=0 ◀──┘  fib(2)=a+b=1+0=1 → return 1
         ─ 値1 ─┐  ★戻る
                 │
depth 2: a=1 ◀──┘  次に右 fib(1)→1(基底,潜って戻る)。fib(3)=1+1=2 → return 2
         ─ 値2 ─┐  ★戻る
                 │
depth 1: a=2 ◀──┘  次に右 fib(2) ← ★ここで fib(2) を「また」計算(2回目)
         fib(2) → fib(1)=1 と fib(0)=0 → 1。fib(4)=a+b=2+1=3 → return 3
         ─ 値3 ─┐  ★戻る
                 │
depth 0: a=3 ◀──┘  次に右 fib(3) ← ★fib(3) も「また」計算(2回目)
         fib(3) → fib(2)=1 と fib(1)=1 → 2。fib(5)=a+b=3+2=5 → return 5

→ fib(5) = 5

----------------------------------------------------------------
読み方の軸 3 つ:

(1) ★backtracking(generate_strings/permutations/subsets)との決定的な違い★
    あちらは ★戻る で path.pop() し、答えは result に副作用でためた。
    fib は ★戻る で「数値が返り」、呼んだ側がその値を a+b に使う。
    戻り値そのものが部分問題の答え。共有する current は無い。

(2) 評価順は深さ優先・左優先。左の fib(n-1) の木を最後まで計算しきってから
    右 fib(n-2) に進む。一番深い基底(fib(1),fib(0))から値が積み上がる。

(3) ★印 = 再計算。この1回の fib(5) で fib(2) を3回、fib(3) を2回計算している。
    n が増えると再計算が指数的に増える(O(2^N))。これがメモ化で消せる無駄。
    fib_memo は一度返した値を覚えて2回目以降は即 return → O(N)。
    (末尾の動作確認で naive と memo の呼び出し回数の差が数字で見える)
"""


# ----------------------------------------------------------------------
# 再帰 vs 反復 の使い分け
# ----------------------------------------------------------------------
#
# - メモ化再帰 (トップダウン): 自然な定義に近い。読みやすい
#       fib(n) = fib(n-1) + fib(n-2) のまま書ける
# - 反復 (ボトムアップ):       スタックを消費しない。空間 O(1) も可能
#       Python の再帰上限 (デフォルト 1,000) に当たらない
#
# n=10,000 のような巨大な n では再帰版は RecursionError になる。
# 実務やコンテストでは、計算量が同じなら反復のほうが堅牢。


# ----------------------------------------------------------------------
# よくある間違い
# ----------------------------------------------------------------------
#
# 1. ナイーブ再帰のまま提出して TLE
#    -> n=30 を超えると現実時間で終わらない (実際 LeetCode は n<=30 制約)
#
# 2. メモ化辞書を関数の引数として渡してリセット忘れ
#    -> 別の入力でも前の結果が混ざる。@lru_cache は関数単位で安全
#       手動 dict を使うなら、関数の外でクリアするか、関数の中で初期化する
#
# 3. 反復解で a, b の更新順序を間違える
#    -> a = b; b = a + b; と書くと b が壊れる (a は既に更新済み)
#       タプル unpacking `a, b = b, a + b` で右辺を先に評価させる
#
# 4. base case を `if n == 0: return 0` だけにする
#    -> n=1 のとき再帰で n-2=-1 に潜って無限ループに近い挙動
#       `if n < 2: return n` の形が安全 (0,1 を両方カバー)


# ----------------------------------------------------------------------
# 動作確認
# ----------------------------------------------------------------------
if __name__ == "__main__":
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

    print(f"{'n':>3} {'naive':>8} {'memo':>8} {'iter':>8} {'expected':>10}")
    print("-" * 42)
    for n, exp in enumerate(expected):
        # naive は n が大きいと遅いので 30 まで (今回は 12 まで)
        rn = fib_naive(n) if n <= 30 else None
        rm = fib_memo(n)
        ri = fib_iter(n)
        ok = rm == ri == exp and (rn is None or rn == exp)
        status = "OK" if ok else "NG"
        print(f"{n:>3} {str(rn):>8} {rm:>8} {ri:>8} {exp:>10}  [{status}]")


# ----------------------------------------------------------------------
# 動きを見るためのトレース版
# ----------------------------------------------------------------------
# fib_naive と fib_memo を「呼び出し木」として可視化する。
# 同じ部分問題が何回呼ばれているかが目で見える。
def fib_naive_traced(n: int, depth: int = 0) -> int:
    indent = "  " * depth
    print(f"{indent}fib_naive({n}) を呼び出し")
    if n < 2:
        print(f"{indent}  → return {n}  (基底ケース)")
        return n
    a = fib_naive_traced(n - 1, depth + 1)
    b = fib_naive_traced(n - 2, depth + 1)
    print(f"{indent}fib_naive({n}) = {a} + {b} = {a + b}")
    return a + b


def fib_memo_traced(n: int, memo: dict[int, int] | None = None, depth: int = 0) -> int:
    """手動メモ版。キャッシュヒットしたら「(cached)」と表示。"""
    if memo is None:
        memo = {}
    indent = "  " * depth
    if n in memo:
        print(f"{indent}fib_memo({n}) → {memo[n]}  (cached)")
        return memo[n]
    print(f"{indent}fib_memo({n}) を計算")
    if n < 2:
        memo[n] = n
        print(f"{indent}  → return {n}  (基底ケース)")
        return n
    a = fib_memo_traced(n - 1, memo, depth + 1)
    b = fib_memo_traced(n - 2, memo, depth + 1)
    memo[n] = a + b
    print(f"{indent}fib_memo({n}) = {a} + {b} = {a + b}")
    return memo[n]


if __name__ == "__main__":
    print("\n========== fib_naive(5) の呼び出し木 ==========")
    fib_naive_traced(5)

    print("\n========== fib_memo(5) の呼び出し木 (キャッシュで枝刈り) ==========")
    fib_memo_traced(5)

    # 呼び出し回数の比較
    naive_calls = {"count": 0}
    memo_calls = {"count": 0}

    def fib_naive_counted(n: int) -> int:
        naive_calls["count"] += 1
        if n < 2:
            return n
        return fib_naive_counted(n - 1) + fib_naive_counted(n - 2)

    def fib_memo_counted(n: int, memo: dict[int, int] | None = None) -> int:
        if memo is None:
            memo = {}
        memo_calls["count"] += 1
        if n in memo:
            return memo[n]
        if n < 2:
            memo[n] = n
            return n
        memo[n] = fib_memo_counted(n - 1, memo) + fib_memo_counted(n - 2, memo)
        return memo[n]

    print("\n========== 呼び出し回数の比較 ==========")
    print(f"{'n':>4} {'naive 呼び出し':>16} {'memo 呼び出し':>16}")
    for n in [5, 10, 20, 30]:
        naive_calls["count"] = 0
        memo_calls["count"] = 0
        fib_naive_counted(n)
        fib_memo_counted(n)
        print(f"{n:>4} {naive_calls['count']:>16,} {memo_calls['count']:>16,}")
