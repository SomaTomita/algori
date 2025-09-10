"""
Binary Search
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.
Implement a function to search for target within nums.
If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn) time.

Example 1:
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3

Example 2:
Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1

Constraints:
1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


print(Solution().search([-1, 0, 2, 4, 6, 8], 4))

"""
流れ: 
nums = [-1, 0, 2, 4, 6, 8], target = 4

配列のインデックスと値:
Index: │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
Value: │-1 │ 0 │ 2 │ 4 │ 6 │ 8 │

========================================

初期状態: left=0, right=5, target=4
探索範囲: [-1, 0, 2, 4, 6, 8] (全体)
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│-1 │ 0 │ 2 │ 4 │ 6 │ 8 │
  L                   R

========================================

Iteration 1: left=0, right=5
条件チェック: left(0) <= right(5) → True, ループ継続

mid計算: mid = (0 + 5) // 2 = 2
nums[mid] = nums[2] = 2

比較: nums[2] = 2 vs target = 4
→ 2 < 4 なので elif nums[mid] < target が成立

処理: left = mid + 1 = 2 + 1 = 3
新しい探索範囲: [4, 6, 8] (右半分)

│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│-1 │ 0 │ 2 │ 4 │ 6 │ 8 │
         mid  L       R

========================================

Iteration 2: left=3, right=5
条件チェック: left(3) <= right(5) → True, ループ継続

mid計算: mid = (3 + 5) // 2 = 4
nums[mid] = nums[4] = 6

比較: nums[4] = 6 vs target = 4
→ 6 > 4 なので else (nums[mid] > target) が成立

処理: right = mid - 1 = 4 - 1 = 3
新しい探索範囲: [4] (左半分)

│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│-1 │ 0 │ 2 │ 4 │ 6 │ 8 │
             L,R  mid

========================================

Iteration 3: left=3, right=3
条件チェック: left(3) <= right(3) → True, ループ継続

mid計算: mid = (3 + 3) // 2 = 3
nums[mid] = nums[3] = 4

比較: nums[3] = 4 vs target = 4
→ 4 == 4 なので if nums[mid] == target が成立

処理: return mid = 3 (目標値発見!)

│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│-1 │ 0 │ 2 │ 4 │ 6 │ 8 │
             L,R
             mid
            FOUND!

========================================

結果: インデックス 3 を返す ✓
"""

# ------------------------------------------------------------

# 失敗例
print(Solution().search([-1, 0, 2, 4, 6, 8], 3))

"""
nums = [-1, 0, 2, 4, 6, 8], target = 3

Iteration 1: left=0, right=5, mid=2
nums[2]=2 < 3 → left=3

Iteration 2: left=3, right=5, mid=4  
nums[4]=6 > 3 → right=3

Iteration 3: left=3, right=3, mid=3
nums[3]=4 > 3 → right=2

Iteration 4: left=3, right=2
条件チェック: left(3) <= right(2) → False
→ while ループ終了

結果: return -1 (見つからない) ✓
"""

# ------------------------------------------------------------


# 別解
class Solution:
    def search_recursive(self, nums: List[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid - 1)

        return binary_search(0, len(nums) - 1)


print(
    Solution().search_recursive(
        [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 16, 17, 19, 20, 21, 30, 42], 21
    )
)

"""========================================

Call 1: binary_search(left=0, right=17)
条件チェック: left(0) <= right(17) → True, 探索継続

mid計算: mid = 0 + (17 - 0) // 2 = 8
nums[mid] = nums[8] = 10

比較: nums[8] = 10 vs target = 21
→ 10 < 21 なので elif nums[mid] < target が成立

処理: return binary_search(mid + 1, right) = binary_search(9, 17)
新しい探索範囲: [11, 13, 16, 17, 19, 20, 21, 30, 42] (右半分)

│  0 │  1 │  2 │  3 │  4 │  5 │  6 │  7 │  8 │  9 │ 10 │ 11 │ 12 │ 13 │ 14 │ 15 │ 16 │ 17 │
│  1 │  2 │  3 │  4 │  5 │  7 │  8 │  9 │ 10 │ 11 │ 13 │ 16 │ 17 │ 19 │ 20 │ 21 │ 30 │ 42 │
  L                                       mid                                           R

========================================

Call 2: binary_search(left=9, right=17)
条件チェック: left(9) <= right(17) → True, 探索継続

mid計算: mid = 9 + (17 - 9) // 2 = 9 + 4 = 13
nums[mid] = nums[13] = 19

比較: nums[13] = 19 vs target = 21
→ 19 < 21 なので elif nums[mid] < target が成立

処理: return binary_search(mid + 1, right) = binary_search(14, 17)
新しい探索範囲: [20, 21, 30, 42] (さらに右半分)

│  0 │  1 │  2 │  3 │  4 │  5 │  6 │  7 │  8 │  9 │ 10 │ 11 │ 12 │ 13 │ 14 │ 15 │ 16 │ 17 │
│  1 │  2 │  3 │  4 │  5 │  7 │  8 │  9 │ 10 │ 11 │ 13 │ 16 │ 17 │ 19 │ 20 │ 21 │ 30 │ 42 │
                                                L                  mid                  R

========================================

Call 3: binary_search(left=14, right=17)
条件チェック: left(14) <= right(17) → True, 探索継続

mid計算: mid = 14 + (17 - 14) // 2 = 14 + 1 = 15
nums[mid] = nums[15] = 21

比較: nums[15] = 21 vs target = 21
→ 21 == 21 なので if nums[mid] == target が成立

処理: return mid = 15 (目標値発見!)

│  0 │  1 │  2 │  3 │  4 │  5 │  6 │  7 │  8 │  9 │ 10 │ 11 │ 12 │ 13 │ 14 │ 15 │ 16 │ 17 │
│  1 │  2 │  3 │  4 │  5 │  7 │  8 │  9 │ 10 │ 11 │ 13 │ 16 │ 17 │ 19 │ 20 │ 21 │ 30 │ 42 │
                                                                         L  mid         R
                                                                           FOUND!

========================================

結果: 15 が返される
Call 3 が 15 を返す → Call 2 が 15 を返す → Call 1 が 15 を返す → 最終的に 15 が返る ✓
"""
