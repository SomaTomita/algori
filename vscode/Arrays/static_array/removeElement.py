"""Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.

```
Custom Judge:
The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.
int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.


Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).


Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100
"""

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        # kを更新 (val以外の要素を左に詰める)
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        # 残りの要素を_で埋める (必要ない場合は削除)
        nums[k:] = ["_"] * (len(nums) - k)

        return k


print(Solution().removeElement([3, 2, 2, 3], 3))
# 流れ:
# nums = [3, 2, 2, 3], val = 3
# k = 0
# i = 0, nums[0] = 3, nums[0] != val → nums[0] = nums[0] → k = 1
# i = 1, nums[1] = 2, nums[1] != val → nums[1] = nums[1] → k = 2
# i = 2, nums[2] = 2, nums[2] != val → nums[2] = nums[2] → k = 3
# i = 3, nums[3] = 3, nums[3] == val → k = 3
# nums[3:] = ["_"] * (4 - 3) = ["_"]
# nums = [2, 2, _, _]
# return 2


print(Solution().removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
# 流れ
# nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
# k = 0
# i = 0, nums[0] = 0, nums[0] != val → nums[0] = nums[0] → k = 1
# i = 1, nums[1] = 1, nums[1] != val → nums[1] = nums[1] → k = 2
# i = 2, nums[2] = 2, nums[2] == val → k = 2
# i = 3, nums[3] = 2, nums[3] == val → k = 2
# i = 4, nums[4] = 3, nums[4] != val → nums[2] = nums[4] → k = 3
# i = 5, nums[5] = 0, nums[5] != val → nums[3] = nums[5] → k = 4
# i = 6, nums[6] = 4, nums[6] != val → nums[4] = nums[6] → k = 5
# i = 7, nums[7] = 2, nums[7] == val → k = 5
# nums[5:] = ["_"] * (8 - 5) = ["_", "_", "_"]
# nums = [0, 1, 3, 0, 4, _, _, _]
# return 5
