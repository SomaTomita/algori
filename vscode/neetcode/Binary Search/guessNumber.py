"""
Guess Number Higher Or Lower

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:

0:  your guess is equal to the number I picked (i.e. num == pick).
-1: Your guess is higher than the number I picked (i.e. num > pick).
1:  Your guess is lower than the number I picked (i.e. num < pick).

Return the number that I picked.

Example 1:
Input: n = 5, pick = 3
Output: 3

Example 2:
Input: n = 15, pick = 10
Output: 10

Example 3:
Input: n = 1, pick = 1
Output: 1

Constraints:
1 <= pick <= n <= ((2^31)-1)
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


# ------------------------------------------------------------
# テスト用に guess API を持つクラス
# (本番では LeetCode 側で guess() が定義済みのため不要)
# ------------------------------------------------------------
class Solution:
    def __init__(self, pick: int = 0):
        # 本番では使わないコンストラクタ。テスト時に "正解" をセットする用途。
        self._pick = pick

    def guess(self, num: int) -> int:
        if num == self._pick:
            return 0
        return -1 if num > self._pick else 1

    # ------------------------------------------------------------
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            res = self.guess(mid)

            if res > 0:        # 1: mid < pick (推測値が小さい → 右半分へ)
                left = mid + 1
            elif res < 0:      # -1: mid > pick (推測値が大きい → 左半分へ)
                right = mid - 1
            else:              # 0: 正解
                return mid

        return -1              # 制約上ここには来ない


# ------------------------------------------------------------
# 動作確認 (Solution(pick=...) で正解をセットしてからテスト)
# ------------------------------------------------------------
print(Solution(pick=3).guessNumber(5))   # 3
print(Solution(pick=10).guessNumber(15)) # 10
print(Solution(pick=1).guessNumber(1))   # 1

"""
流れ (Example 1): n=5, pick=3

探索範囲: [1, 2, 3, 4, 5]
目標: pick = 3 を見つける

========================================

初期状態: left=1, right=5
Position: │ 1 │ 2 │ 3 │ 4 │ 5 │
            L       ?       R
                  pick=3

========================================

Iteration 1: left=1, right=5
mid = (1 + 5) // 2 = 3
guess(3): 3 == 3 → return 0 (正解)

処理: else節 → return mid = 3 ✓

========================================
"""

"""
流れ (Example 2): n=15, pick=10

Iteration 1: left=1, right=15, mid=8
  guess(8): 8 < 10 → return 1 (mid が小さい)
  処理: left = 8 + 1 = 9
  新探索範囲: [9..15]

Iteration 2: left=9, right=15, mid=12
  guess(12): 12 > 10 → return -1 (mid が大きい)
  処理: right = 12 - 1 = 11
  新探索範囲: [9..11]

Iteration 3: left=9, right=11, mid=10
  guess(10): 10 == 10 → return 0 (正解)
  処理: return 10 ✓
"""

"""
流れ (Example 3): n=1, pick=1

Iteration 1: left=1, right=1, mid=1
  guess(1): return 0 (正解)
  処理: return 1 ✓
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
時間: O(log n)
空間: O(1)

ポイント:
1. 二分探索の最も素直な形。guess() の戻り値 (-1, 0, 1) がそのまま
   「左/正解/右」に対応するので、分岐が綺麗にまとまる。

2. mid = (left + right) // 2 は理論上は OK だが、
   n が 2^31 近い場合 left+right がオーバーフローする言語もある。
   その対策で mid = left + (right - left) // 2 と書くのが安全。
   Python は整数オーバーフローしないのでどちらでもよい。

3. firstBadVersion との違い:
   - firstBadVersion: "条件 (bad) を満たす最小の境界" を探す
     → while left < right, high = mid
   - guessNumber:     "ピンポイントの値" を探す
     → while left <= right, 一致したら即 return
   問題の構造で書き分ける。
"""
