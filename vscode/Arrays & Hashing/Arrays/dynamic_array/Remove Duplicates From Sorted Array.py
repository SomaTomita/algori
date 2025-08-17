# Remove Duplicates From Sorted Array
# You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.
# After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

# Note:
# The order of the unique elements should remain the same as in the original array.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain all the unique elements.
# Return k as the final result.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l


nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]
print(Solution().removeDuplicates(nums))

# 流れ:
# l=1, r=1, nums[1]==nums[0] → l=1
# l=1, r=2, nums[2]!=nums[1] → nums[1]=nums[2] → l=2
# l=2, r=3, nums[3]==nums[2] → l=2
# l=2, r=4, nums[4]==nums[3] → l=2
# l=2, r=5, nums[5]!=nums[4] → nums[2]=nums[5] → l=3
# l=3, r=6, nums[6]==nums[5] → l=3
# l=3, r=7, nums[7]!=nums[6] → nums[3]=nums[7] → l=4

# 出力:
# nums[:5] = [0, 1, 2, 3, 4]

# ------------------------------------------------------------

# 非in-place


class Solution:
    def removeDuplicates_non_inplace(self, nums):
        unique = []

        for num in nums:
            # unique が空 or 直前と異なる場合だけ追加
            if not unique or unique[-1] != num:
                unique.append(num)

        return len(unique)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]
print(Solution().removeDuplicates_non_inplace(nums))

# 流れ:
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]
# unique = []
# 0 → unique = [0]
# 0 → 重複なので無視
# 1 → unique = [0, 1]
# 1 → 重複なので無視
# 1 → 重複なので無視
# 2 → unique = [0, 1, 2]
# 2 → 重複なので無視
# 3 → unique = [0, 1, 2, 3]
# 4 → unique = [0, 1, 2, 3, 4]

# ------------------------------------------------------------


# 別解


class Solution:
    def removeDuplicates_with_set(self, nums: list[int]) -> int:
        unique = sorted(set(nums))
        nums[: len(unique)] = unique  # 最初の5個にuniqueを代入
        return len(unique)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 4]
print(Solution().removeDuplicates_with_set(nums))

# 流れ:
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# unique = sorted(set(nums))  -  [0, 1, 2, 3, 4]
# nums[:5] = unique           -   numsは [0, 1, 2, 3, 4,...] になる


# ------------------------------------------------------------
# ------------------------------------------------------------

# python基礎

# for文とrange
for i in range(1, 5):
    print(i)  # 出力: 1 2 3 4

# リストのスライスと置き換え
nums = [10, 20, 30, 40, 50]
nums[1:4] = [99, 88, 77]  # インデックス1〜3を置き換え
print(nums)  # 出力: [10, 99, 88, 77, 50]

# 最後の要素にアクセス
nums = [1, 2, 2, 3]
nums[-1]  # 出力: 3
