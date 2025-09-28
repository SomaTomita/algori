"""
Guess Number Higher Or Lower
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:

0: your guess is equal to the number I picked (i.e. num == pick).
-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
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


class Solution:
    def __init__(self, guess_api):
        self.guess = guess_api.guess

    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = (left + right) // 2
            res = self.guess(mid)

            if res > 0:  # mid < pick (推測値が小さい)
                left = mid + 1  # 右半分を探索
            elif res < 0:  # mid > pick (推測値が大きい)
                right = mid - 1  # 左半分を探索
            else:  # res == 0 (正解!)
                return mid

        return -1  # 理論上ここには到達しない


print(Solution().guessNumber(5))

"""
流れ: n=5, pick=3

探索範囲: [1, 2, 3, 4, 5]
目標: pick = 3 を見つける

========================================

初期状態: left=1, right=5
探索範囲: [1, 2, 3, 4, 5] (全体)
Position: │ 1 │ 2 │ 3 │ 4 │ 5 │
            L       ?       R
                  pick=3

========================================

Iteration 1: left=1, right=5
条件チェック: left(1) <= right(5) → True

mid計算: mid = (1 + 5) // 2 = 3
guess(3) を呼び出し

guess API判定:
- num = 3, pick = 3
- 3 == 3 なので return 0

結果: res = 0 (正解!)
処理: else節実行 → return mid = 3 ✓

========================================
"""

print(Solution().guessNumber(15))

"""
流れ: n=15, pick=10

初期状態: left=1, right=15
探索範囲: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Iteration 1: left=1, right=15, mid=8
guess(8): 8 < 10 → return 1 (推測値が小さい)
処理: left = 8 + 1 = 9
新探索範囲: [9, 10, 11, 12, 13, 14, 15]

Iteration 2: left=9, right=15, mid=12
guess(12): 12 > 10 → return -1 (推測値が大きい)
処理: right = 12 - 1 = 11
新探索範囲: [9, 10, 11]

Iteration 3: left=9, right=11, mid=10
guess(10): 10 == 10 → return 0 (正解!)
処理: return 10 ✓
"""
