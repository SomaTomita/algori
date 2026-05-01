"""
Climbing Stairs

You are given an integer n representing the number of steps to reach the top of a staircase.
You can climb with either 1 or 2 steps at a time.
Return the number of distinct ways to climb to the top of the staircase.

Example 1:
Input: n = 2
Output: 2
Explanation:
1 + 1 = 2
2 = 2

Example 2:
Input: n = 3
Output: 3
Explanation:
1 + 1 + 1 = 3
1 + 2 = 3
2 + 1 = 3

Constraints:
1 <= n <= 30
"""


# ------------------------------------------------------------
# 解法1: ボトムアップ DP (定数空間, Fibonacci スタイル)
# ------------------------------------------------------------
# 漸化式:
#   f(1) = 1, f(2) = 2,
#   f(n) = f(n-1) + f(n-2)   (n 段目には "n-1 段から +1" or "n-2 段から +2")
#
# 実装テク:
#   one, two の 2 変数だけで済む (テーブル不要)。
#   ループ内で one を「次の値」に、two を「今の値」に毎回ローテートする。
#
# 注意 (実装の初期値):
#   one, two = 1, 1 から始め、ループを n-1 回回す。
#   結果として one が "f(n) の答え" を持つように設計されている。
# ------------------------------------------------------------
class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
print(Solution().climbStairs(1))  # 1
print(Solution().climbStairs(2))  # 2
print(Solution().climbStairs(3))  # 3
print(Solution().climbStairs(4))  # 5
print(Solution().climbStairs(5))  # 8
print(Solution().climbStairs(6))  # 13


"""
流れ: n = 5 (答え = 8)

ループ回数: range(n-1) = range(4) = 4 回 (i=0,1,2,3)

初期状態:
  one = 1   ← この時点で "1 段までの登り方の数" を表す
  two = 1   ← 1 つ前の f 値 (今は使い回しのプレースホルダ)

注意: 実装上の (one, two) は "数学の f(n), f(n-1)" にきれいに対応していない。
     ループを回すたびに 1 段ずつ上に登っていく "ローリング 2 変数" と
     見るのが分かりやすい。

========================================

i = 0:
  temp = one        → temp = 1
  one  = one + two  → one = 1 + 1 = 2     (= f(2))
  two  = temp       → two = 1             (= f(1))

  この時点で one は "2 段までの登り方の数 = 2" を表す
  状態: (one, two) = (2, 1)

========================================

i = 1:
  temp = one        → temp = 2
  one  = one + two  → one = 2 + 1 = 3     (= f(3))
  two  = temp       → two = 2             (= f(2))

  状態: (one, two) = (3, 2)
  one は "3 段までの登り方の数 = 3"

========================================

i = 2:
  temp = 3
  one  = 3 + 2 = 5  (= f(4))
  two  = 3          (= f(3))

  状態: (one, two) = (5, 3)
  one は "4 段までの登り方の数 = 5"

========================================

i = 3:
  temp = 5
  one  = 5 + 3 = 8  (= f(5))
  two  = 5          (= f(4))

  状態: (one, two) = (8, 5)
  one は "5 段までの登り方の数 = 8" ← 答え!

========================================

ループ終了。return one = 8 ✓


テーブルで見ると:
   n の値        | 1 | 2 | 3 | 4 | 5  | 6  | 7  | 8  | ...
   登り方の数 f  | 1 | 2 | 3 | 5 | 8  | 13 | 21 | 34 | ...
                  ↑   ↑   ↑   ↑   ↑
                  初期 i=0 i=1 i=2 i=3

ループ i 回目を抜けると、one = f(i + 2) になっている。
n = 5 を求めるには i+2 = 5 → i = 3 まで回す → range(4) = range(n-1) ✓
"""


# ------------------------------------------------------------
# 別解1: 1次元 DP テーブル (理解優先)
# ------------------------------------------------------------
class SolutionDP:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


print(SolutionDP().climbStairs(5))  # 8


# ------------------------------------------------------------
# 別解2: 素朴な再帰 (メモ化なし) — 学習用、本番では遅すぎる
# ------------------------------------------------------------
class SolutionRecursive:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


# print(SolutionRecursive().climbStairs(30))  # 動くが遅い (~ 1.3 億回呼ばれる)


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
解法1 (ローリング 2 変数):
  時間: O(n)
  空間: O(1)  ← one, two の 2 変数だけ

解法2 (1次元 DP):
  時間: O(n)
  空間: O(n)  ← dp 配列

解法3 (素朴な再帰, メモ化なし):
  時間: O(2^n)  ← 同じ部分問題を何度も計算してしまう
  空間: O(n)    ← 再帰スタック
  → メモ化すれば O(n) に落ちる。

ポイント:
1. これは Fibonacci 数列と同じ漸化式 f(n) = f(n-1) + f(n-2) の問題。
   Climbing Stairs の "1 段 or 2 段" の選択が、自然に Fibonacci になる。

2. 「直前 2 つだけあれば次が出せる」関係なので、テーブル全体を覚える必要は
   ない。one, two の 2 変数だけで O(1) 空間にできる (ローリング DP)。

3. (one, two) のローテーションは 3 行で書けるが、Python なら
   `one, two = one + two, one` の 1 行でも同じ動きをする (慣れたらこの書き方が読みやすい)。
"""
