# Climbing Stairs
# You are given an integer n representing the number of steps to reach the top of a staircase.
# You can climb with either 1 or 2 steps at a time.
# Return the number of distinct ways to climb to the top of the staircase.

# Example 1:
# Input: n = 2
# Output: 2
# Explanation:
# 1 + 1 = 2
# 2 = 2

# Example 2:
# Input: n = 3
# Output: 3
# Explanation:
# 1 + 1 + 1 = 3
# 1 + 2 = 3
# 2 + 1 = 3

# Constraints:
# 1 <= n <= 30


class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp

        return one


print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(4))
print(Solution().climbStairs(5))
print(Solution().climbStairs(6))

# 流れ:
# n=5の場合のDynamic Programmingテーブル
#
# ステップ | i | one | two | temp | one+two | 説明
# --------|---|-----|-----|------|---------|--------------------
# 初期値  | - |  1  |  1  |  -   |    -    | base case: n=1, n=2
# ステップ1| 0 |  2  |  1  |  1   |   1+1=2 | n=3の場合の数
# ステップ2| 1 |  3  |  2  |  2   |   2+1=3 | n=4の場合の数
# ステップ3| 2 |  5  |  3  |  3   |   3+2=5 | n=5の場合の数
# ステップ4| 3 |  8  |  5  |  5   |   5+3=8 | n=6の場合の数
#
# n段目への登り方 = (n-1)段目への登り方 + (n-2)段目への登り方
#
# n=5の詳細な流れ:
# 初期: one=1, two=1 (n=1とn=2のベースケース)
# i=0: temp=1, one=1+1=2, two=1 → n=3の答えは2
# i=1: temp=2, one=2+1=3, two=2 → n=4の答えは3
# i=2: temp=3, one=3+2=5, two=3 → n=5の答えは5
# i=3: temp=5, one=5+3=8, two=5 → n=6の答えは8
# 最終的にone=8を返す（ただしn=5なのでi=2で終了し、one=5を返す）
