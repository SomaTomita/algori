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
      l   i   r

Step 3: nums[2]=1 (白色)
- else文実行: i++ のみ  
- nums=[0,1,1,2], l=1, r=3, i=3
│ 0 │ 1 │ 2 │ 3 │
│ 0 │ 1 │ 1 │ 2 │
      l      i,r

Step 4: nums[3]=2 (青色)
- swap(3,3): 自分自身との交換（変化なし）
- nums=[0,1,1,2], l=1, r=2, i=3 (iは変更されない)
│ 0 │ 1 │ 2 │ 3 │
│ 0 │ 1 │ 1 │ 2 │
      l   r   i

Step 5: i=3 > r=2 なのでループ終了

最終結果: [0,1,1,2] ✓
"""


nums_test = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums_test)
print(nums_test)

"""
詳細な実行流れ: nums = [2, 0, 2, 1, 1, 0]

初期状態: l=0, r=5, i=0
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│ 2 │ 0 │ 2 │ 1 │ 1 │ 0 │
  l,i                 r

========================================

Step 1: nums[0] = 2 (青色)
処理: elif nums[i] == 2 → swap(0, 5)
- swap(0, 5): nums[0]=0, nums[5]=2
- r = r - 1 = 4
- i は変化なし (i=0)

結果: nums=[0, 0, 2, 1, 1, 2], l=0, r=4, i=0
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│ 0 │ 0 │ 2 │ 1 │ 1 │ 2 │
l,i               r  確定

========================================

Step 2: nums[0] = 0 (赤色)
処理: if nums[i] == 0 → swap(0, 0)
- swap(0, 0): 自分自身なので変化なし
- l = l + 1 = 1
- i = i + 1 = 1

結果: nums=[0, 0, 2, 1, 1, 2], l=1, r=4, i=1
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│ 0 │ 0 │ 2 │ 1 │ 1 │ 2 │
確定  l,i          r  確定

========================================

Step 3: nums[1] = 0 (赤色)
処理: if nums[i] == 0 → swap(1, 1)
- swap(1, 1): 自分自身なので変化なし
- l = l + 1 = 2
- i = i + 1 = 2

結果: nums=[0, 0, 2, 1, 1, 2], l=2, r=4, i=2
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│ 0 │ 0 │ 2 │ 1 │ 1 │ 2 │
確定 確定 l,i      r  確定

========================================

Step 4: nums[2] = 2 (青色)
処理: elif nums[i] == 2 → swap(2, 4)
- swap(2, 4): nums[2]=1, nums[4]=2
- r = r - 1 = 3
- i は変化なし (i=2)

結果: nums=[0, 0, 1, 1, 2, 2], l=2, r=3, i=2
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│ 0 │ 0 │ 1 │ 1 │ 2 │ 2 │
確定 確定  l,i  r  確定 確定

========================================

Step 5: nums[2] = 1 (白色)
処理: else → i++
- i = i + 1 = 3

結果: nums=[0, 0, 1, 1, 2, 2], l=2, r=3, i=3
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│ 0 │ 0 │ 1 │ 1 │ 2 │ 2 │
確定 確定  l  i,r 確定 確定


========================================

Step 6: nums[3] = 1 (白色)
処理: else → i++
- i = i + 1 = 4

結果: nums=[0, 0, 1, 1, 2, 2], l=2, r=3, i=4
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│ 0 │ 0 │ 1 │ 1 │ 2 │ 2 │
確定 確定  l   r  i,確定 確定

========================================

終了条件: i=4 > r=3 なのでループ終了

最終結果: [0, 0, 1, 1, 2, 2]
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │
│ 0 │ 0 │ 1 │ 1 │ 2 │ 2 │
"""
