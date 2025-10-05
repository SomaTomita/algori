"""
Reverse String

Write a function that reverses a string.
The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
1 <= s.length <= 10^5
s[i] is a printable ascii character.
"""

from typing import List


class RecursiveSolution:
    def reverseString(self, s: List[str]) -> None:
        self._helper(s, 0, len(s) - 1)

    def _helper(self, s: List[str], left: int, right: int) -> None:
        if left >= right:
            return

        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1
        self._helper(s, left, right)


print("\n=== Recursion ===")
s2 = ["h", "e", "l", "l", "o"]
RecursiveSolution().reverseString(s2)
print(s2)  # ["o","l","l","e","h"]

"""
Recursionの流れ: s = ["h","e","l","l","o"]

呼び出しツリー:
_helper(s, 0, 4)
  → swap s[0]↔s[4]
  → _helper(s, 1, 3)
      → swap s[1]↔s[3]
      → _helper(s, 2, 2)
          → base case (left >= right)
          → return

========================================

Call 1: _helper(s, 0, 4)
配列状態: ["h","e","l","l","o"]
           L               R
条件: left(0) >= right(4) → False

スワップ: s[0] ↔ s[4]
配列状態: ["o","e","l","l","h"]

再帰呼び出し: _helper(s, 1, 3)

========================================

Call 2: _helper(s, 1, 3)
配列状態: ["o","e","l","l","h"]
               L      R
条件: left(1) >= right(3) → False

スワップ: s[1] ↔ s[3]
配列状態: ["o","l","l","e","h"]

再帰呼び出し: _helper(s, 2, 2)

========================================

Call 3: _helper(s, 2, 2)
配列状態: ["o","l","l","e","h"]
                  L,R
条件: left(2) >= right(2) → True (Base case)

処理: return（何もしない）
"""
