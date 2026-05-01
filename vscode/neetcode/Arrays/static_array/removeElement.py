"""Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
- Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
- The remaining elements of nums are not important as well as the size of nums.
- Return k.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

from typing import List


# ------------------------------------------------------------
# 解法1: 二ポインタ (in-place, 順序保持)
# ------------------------------------------------------------
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k: "次に val 以外の値を書き込む位置"
        # i: 走査ポインタ
        # ループ後、nums[0..k-1] には val 以外の値だけが順序を保って入る
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # ※ 実際の LeetCode では不要だが、視覚化のため余りを "_" で埋める
        nums[k:] = ["_"] * (len(nums) - k)

        return k


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
nums1 = [3, 2, 2, 3]
print(Solution().removeElement(nums1, 3))  # 2
print(nums1)                                # [2, 2, '_', '_']

"""
流れ: nums = [3, 2, 2, 3], val = 3

初期: k = 0
"k の左側 (nums[0..k-1]) は "val 以外の値" だけが詰めて並んでいる状態を保つ"

Index: │ 0 │ 1 │ 2 │ 3 │
Value: │ 3 │ 2 │ 2 │ 3 │
         k,i

========================================

i=0: nums[0]=3 == val(3) → スキップ (k は進まない)

│ 0 │ 1 │ 2 │ 3 │
│ 3 │ 2 │ 2 │ 3 │
  k   i

========================================

i=1: nums[1]=2 != val → nums[k] = nums[i] → nums[0] = 2, k=1

│ 0 │ 1 │ 2 │ 3 │
│ 2 │ 2 │ 2 │ 3 │
  ✓   k,i

========================================

i=2: nums[2]=2 != val → nums[1] = 2, k=2

│ 0 │ 1 │ 2 │ 3 │
│ 2 │ 2 │ 2 │ 3 │
  ✓   ✓   k,i

========================================

i=3: nums[3]=3 == val → スキップ

│ 0 │ 1 │ 2 │ 3 │
│ 2 │ 2 │ 2 │ 3 │
  ✓   ✓   k   i

========================================

ループ終了。
nums[k:] = ['_'] * (4-2) = ['_', '_'] で末尾を埋める

最終 nums = [2, 2, '_', '_']
return k = 2 ✓
"""

# ------------------------------------------------------------

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
print(Solution().removeElement(nums2, 2))  # 5
print(nums2)                                # [0, 1, 3, 0, 4, '_', '_', '_']

"""
流れ: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2

初期: k = 0

Index: │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │
Value: │ 0 │ 1 │ 2 │ 2 │ 3 │ 0 │ 4 │ 2 │
         k,i

i=0: 0 != 2 → nums[0]=0, k=1
i=1: 1 != 2 → nums[1]=1, k=2
i=2: 2 == 2 → スキップ
i=3: 2 == 2 → スキップ
i=4: 3 != 2 → nums[2]=3, k=3
i=5: 0 != 2 → nums[3]=0, k=4
i=6: 4 != 2 → nums[4]=4, k=5
i=7: 2 == 2 → スキップ

ループ終了:
│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │
│ 0 │ 1 │ 3 │ 0 │ 4 │ 0 │ 4 │ 2 │   ← 5 番目以降はゴミだが見ない
  ✓   ✓   ✓   ✓   ✓   k

末尾を '_' で埋め: nums = [0, 1, 3, 0, 4, '_', '_', '_']
return k = 5 ✓
"""


# ------------------------------------------------------------
# 別解: 二ポインタ (順序を保たない高速版)
# ------------------------------------------------------------
"""
順序を保たなくてよい場合は、末尾の "val 以外" を持ってくる方法も使える。
"val が少ない" ケースで書き込み回数が減るのが利点。

  l = 0, r = len(nums) - 1
  while l <= r:
      if nums[l] == val:
          nums[l] = nums[r]   # 末尾の値を持ってくる
          r -= 1               # 末尾を縮める
      else:
          l += 1
  return l

順序が変わってもよい問題 (この LeetCode 27) ではこちらも合法。
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
解法1 (順序保持の二ポインタ):
  時間: O(n)
  空間: O(1)
  特徴: 元の並び順を保つ。書き込み回数は最大 n 回。

別解 (末尾 swap, 順序非保持):
  時間: O(n)
  空間: O(1)
  特徴: val が少ないと書き込み回数が "val 以外の個数" で済むので速い。

ポイント:
1. removeDuplicatesFromSortedArray と同じ "書き込み位置 k と走査 i" の二ポインタ。
   ただし条件が "重複か?" ではなく "削除対象か?" になっている。
2. k は i を絶対に追い越さない (k <= i が常に成立) ので、
   書き込みが未走査の位置を壊さず in-place が成立する。
3. nums[k:] = ['_'] * ... は学習用の見やすさのため。
   LeetCode の判定では "k 以降は何でもよい" のでこの行は本来不要。
"""
