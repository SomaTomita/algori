"""Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

Constraints:
n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)  # 長さ 2n の配列を先に確保 (高速化のため)
        for i in range(n):
            ans[i] = nums[i]      # 前半 (0..n-1) に nums をコピー
            ans[i + n] = nums[i]  # 後半 (n..2n-1) にも nums をコピー
        return ans


print(Solution().getConcatenation([1, 2, 1]))
"""
流れ: nums = [1, 2, 1], n = 3

初期状態: ans = [0, 0, 0, 0, 0, 0]  (長さ 2n = 6)

Index: │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
Value: │ 0 │ 0 │ 0 │ 0 │ 0 │ 0 │

========================================

Iteration 1: i = 0
処理1: ans[i] = nums[i] → ans[0] = 1
処理2: ans[i + n] = nums[i] → ans[3] = 1

Index: │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
Value: │ 1 │ 0 │ 0 │ 1 │ 0 │ 0 │
         ↑           ↑
       前半 i=0    後半 i+n=3

========================================

Iteration 2: i = 1
処理1: ans[1] = nums[1] = 2
処理2: ans[4] = nums[1] = 2

Index: │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
Value: │ 1 │ 2 │ 0 │ 1 │ 2 │ 0 │
             ↑           ↑

========================================

Iteration 3: i = 2
処理1: ans[2] = nums[2] = 1
処理2: ans[5] = nums[2] = 1

Index: │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
Value: │ 1 │ 2 │ 1 │ 1 │ 2 │ 1 │
                 ↑           ↑

========================================

最終結果: [1, 2, 1, 1, 2, 1] ✓
"""

print(Solution().getConcatenation([1, 3, 2, 1]))
"""
流れ: nums = [1, 3, 2, 1], n = 4

初期状態: ans = [0]*8 = [0,0,0,0,0,0,0,0]

i=0: ans[0]=1, ans[4]=1 → [1,_,_,_,1,_,_,_]
i=1: ans[1]=3, ans[5]=3 → [1,3,_,_,1,3,_,_]
i=2: ans[2]=2, ans[6]=2 → [1,3,2,_,1,3,2,_]
i=3: ans[3]=1, ans[7]=1 → [1,3,2,1,1,3,2,1]

最終結果: [1, 3, 2, 1, 1, 3, 2, 1] ✓
"""


# ------------------------------------------------------------
# 別解: Pythonの組み込み機能を使う1行解
# ------------------------------------------------------------
class OneLinerSolution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # リストの "+" は連結, "*" は反復。どちらも新しいリストを返す。
        return nums + nums          # = nums * 2 でも同じ


print(OneLinerSolution().getConcatenation([1, 2, 1]))


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
計算量:
- 時間: O(n) — n 要素を 2 回コピーするだけ。実質 2n 操作 = O(n)。
- 空間: O(n) — 戻り値として長さ 2n の配列を新たに作る。
        ※ 入力 nums を除いた "追加" メモリで考えても O(n)。

ポイント:
1. 事前に [0]*(2*n) で枠を確保しておくと、append を繰り返すより速い
   (Python のリストは動的配列で、容量超過時にメモリ再確保が走るため)。
2. ans[i+n] = nums[i] のように一度の i で前半と後半を同時に埋めるので
   ループ回数は n 回で済む (2n 回ではない)。
3. nums + nums は読みやすいが、内部で同じ操作をしている。
   学習目的では index でアクセスする上の書き方の方が動きが見える。
"""
