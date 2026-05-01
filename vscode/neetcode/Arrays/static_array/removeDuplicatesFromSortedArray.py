"""
Remove Duplicates From Sorted Array

You are given an integer array nums sorted in non-decreasing order.
Your task is to remove duplicates from nums in-place so that each element appears only once.
After removing the duplicates, return the number of unique elements, denoted as k,
such that the first k elements of nums contain the unique elements.

Note:
- The order of the unique elements should remain the same as in the original array.
- It is not necessary to consider elements beyond the first k positions of the array.
- To be accepted, the first k elements of nums must contain all the unique elements.
- Return k as the final result.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
"""

from typing import List


# ------------------------------------------------------------
# 解法1: 二ポインタ (in-place)
# ------------------------------------------------------------
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # l: "次にユニーク値を書き込む位置"。常に l <= r を保つ。
        # r: 走査用の右ポインタ
        # nums[0] は必ずユニーク (先頭) なので l=1 から開始
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                # 直前の値と違う = 新しいユニーク値 → 左側に書き写す
                nums[l] = nums[r]
                l += 1
            # 重複の場合は何もしない (l はそのまま、r だけ進む)
        return l


nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]
print(Solution().removeDuplicates(nums))  # 5
print(nums[:5])                            # [0, 1, 2, 3, 4]

"""
流れ (二ポインタ): nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]

初期状態: l = 1, r は 1 から進む
"l の左側 (nums[0..l-1]) は常に "ユニーク値が詰めて並んでいる" 状態を保つ"

Index: │ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │
Value: │ 0 │ 0 │ 1 │ 1 │ 1 │ 2 │ 2 │ 3 │ 4 │
         ✓   l,r

========================================

r=1: nums[1]=0, nums[0]=0 → 等しい (重複)
処理: 何もしない、r だけ進む
状態: l=1 のまま

│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │
│ 0 │ 0 │ 1 │ 1 │ 1 │ 2 │ 2 │ 3 │ 4 │
  ✓   l   r

========================================

r=2: nums[2]=1, nums[1]=0 → 違う (新ユニーク!)
処理: nums[l] = nums[r] → nums[1] = 1, l += 1 → l=2

│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │
│ 0 │ 1 │ 1 │ 1 │ 1 │ 2 │ 2 │ 3 │ 4 │
  ✓   ✓   l,r

========================================

r=3: nums[3]=1, nums[2]=1 → 等しい (重複)
状態: l=2 のまま

│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │
│ 0 │ 1 │ 1 │ 1 │ 1 │ 2 │ 2 │ 3 │ 4 │
  ✓   ✓   l   r

========================================

r=4: nums[4]=1, nums[3]=1 → 等しい (重複)
状態: l=2 のまま

========================================

r=5: nums[5]=2, nums[4]=1 → 違う (新ユニーク!)
処理: nums[2] = 2, l=3

│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │
│ 0 │ 1 │ 2 │ 1 │ 1 │ 2 │ 2 │ 3 │ 4 │
  ✓   ✓   ✓   l       r

========================================

r=6: nums[6]=2, nums[5]=2 → 等しい
状態: l=3 のまま

========================================

r=7: nums[7]=3, nums[6]=2 → 違う (新ユニーク!)
処理: nums[3] = 3, l=4

│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │
│ 0 │ 1 │ 2 │ 3 │ 1 │ 2 │ 2 │ 3 │ 4 │
  ✓   ✓   ✓   ✓   l           r

========================================

r=8: nums[8]=4, nums[7]=3 → 違う (新ユニーク!)
処理: nums[4] = 4, l=5

│ 0 │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │
│ 0 │ 1 │ 2 │ 3 │ 4 │ 2 │ 2 │ 3 │ 4 │
  ✓   ✓   ✓   ✓   ✓             r

========================================

ループ終了: r が末尾を超えた

return l = 5  (先頭5要素 [0,1,2,3,4] がユニーク値)
"l 以降の値はゴミだが、問題文では無視してよいことになっている"
"""

# ------------------------------------------------------------
# 解法2: 非 in-place (新しいリストに詰め直す)
# ------------------------------------------------------------


class SolutionNonInplace:
    def removeDuplicates(self, nums):
        unique = []

        for num in nums:
            # unique が空 or 直前と異なる場合だけ追加
            if not unique or unique[-1] != num:
                unique.append(num)

        return len(unique)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]
print(SolutionNonInplace().removeDuplicates(nums))  # 5

"""
流れ (非 in-place): nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]
unique = []

num=0: unique 空 → append → unique = [0]
num=0: 末尾==0 → スキップ
num=1: 末尾==0, 違う → append → unique = [0, 1]
num=1: 末尾==1 → スキップ
num=1: 末尾==1 → スキップ
num=2: 末尾==1, 違う → append → unique = [0, 1, 2]
num=2: 末尾==2 → スキップ
num=3: 末尾==2, 違う → append → unique = [0, 1, 2, 3]
num=4: 末尾==3, 違う → append → unique = [0, 1, 2, 3, 4]

return 5
"""

# ------------------------------------------------------------
# 解法3: set + sorted を使った別解 (in-place 風)
# ------------------------------------------------------------


class SolutionSet:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique = sorted(set(nums))           # 重複除去 + ソート
        nums[: len(unique)] = unique         # 先頭 k 個に書き戻し
        return len(unique)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]
print(SolutionSet().removeDuplicates(nums))  # 5

"""
流れ:
nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]
set(nums)        = {0, 1, 2, 3, 4}        (順序は不定)
sorted(...)      = [0, 1, 2, 3, 4]        (昇順に並べる)
nums[:5] = ...   → nums = [0, 1, 2, 3, 4]

注意: 一般のソート無し配列ではこの方法は元の順序を保たない可能性があるが、
この問題は最初から非減少順なので結果も自然に同じ並びになる。
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
解法1 (二ポインタ):
  時間: O(n)  ← r が 1 回だけ全体を走査
  空間: O(1)  ← 追加メモリは l と r の整数だけ。in-place の真打。

解法2 (非 in-place):
  時間: O(n)
  空間: O(n)  ← unique 用に新しいリスト

解法3 (set + sorted):
  時間: O(n log n) ← sorted がボトルネック
  空間: O(n)       ← set + sorted の中間結果

ポイント:
1. 「ソート済み配列の重複除去」は二ポインタの典型問題。
   片方が "次の書き込み位置"、もう片方が "走査位置" という役割分担。
2. 重複かどうかの判定は nums[r] != nums[r-1] で十分 (ソート済みなので)。
   未ソートなら set/dict が必要になる。
3. l は r を絶対に追い越さないので、書き込みが読み込み済みの位置を
   壊すことはない (in-place が安全に成立する理由)。
"""


# ------------------------------------------------------------
# python基礎
# ------------------------------------------------------------

# for文とrange
for i in range(1, 5):
    print(i)  # 1 2 3 4

# リストのスライスと置き換え
nums = [10, 20, 30, 40, 50]
nums[1:4] = [99, 88, 77]  # インデックス1〜3を置き換え
print(nums)  # [10, 99, 88, 77, 50]

# 最後の要素にアクセス
nums = [1, 2, 2, 3]
print(nums[-1])  # 3
