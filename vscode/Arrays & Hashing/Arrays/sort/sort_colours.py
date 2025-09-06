"""
Sort Colors
You are given an array nums consisting of n elements where each element is an integer representing a color:

0 represents red
1 represents white
2 represents blue
Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

You must not use any built-in sorting functions to solve this problem.

Example 1:
Input: nums = [1,0,1,2]
Output: [0,1,1,2]

Example 2:
Input: nums = [2,1,0]
Output: [0,1,2]

Constraints:
1 <= nums.length <= 300.
0 <= nums[i] <= 2.
Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0, len(nums) - 1
        i = 0

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
                i += 1  # 0の場合は i を増加
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                # i は増加させない（新しい要素をチェック）
            else:
                i += 1  # 1の場合は i を増加


nums_test = [1, 0, 1, 2]
Solution().sortColors(nums_test)
print(nums_test)


"""
正しい流れ: nums=[1,0,1,2]

初期状態: nums=[1,0,1,2], l=0, r=3, i=0
│ 0 │ 1 │ 2 │ 3 │
│ 1 │ 0 │ 1 │ 2 │
  l,i         r

Step 1: nums[0]=1 (白色)
- else文実行: i++ のみ
- nums=[1,0,1,2], l=0, r=3, i=1
│ 0 │ 1 │ 2 │ 3 │
│ 1 │ 0 │ 1 │ 2 │
  l   i       r

Step 2: nums[1]=0 (赤色)  
- swap(0,1): nums[0]とnums[1]を交換 ← swap(l,i)
- nums=[0,1,1,2], l=1, i=2
│ 0 │ 1 │ 2 │ 3 │
│ 0 │ 1 │ 1 │ 2 │
    l   i     r

Step 3: nums[2]=1 (白色)
- else文実行: i++ のみ  
- nums=[0,1,1,2], l=1, r=3, i=3
│ 0 │ 1 │ 2 │ 3 │
│ 0 │ 1 │ 1 │ 2 │
    l       i,r

Step 4: nums[3]=2 (青色)
- swap(3,3): 自分自身との交換（変化なし）
- nums=[0,1,1,2], l=1, r=2, i=3 (iは変更されない)
│ 0 │ 1 │ 2 │ 3 │
│ 0 │ 1 │ 1 │ 2 │
    l     r   i

Step 5: i=3 > r=2 なのでループ終了

最終結果: [0,1,1,2] ✓
"""
