"""
First Bad Version
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad.
Implement a function to find the first bad version.
You should minimize the number of calls to the API.


Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1


Constraints:
1 <= bad <= n <= 231 - 1
"""


class Solution:
    def __init__(self, first_bad: int):
        self.first_bad = first_bad

    def isBadVersion(self, version: int) -> bool:
        return version >= self.first_bad

    # ------------------------------------------------------------
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n

        while low < high:
            mid = (low + high) // 2

            if self.isBadVersion(mid):
                high = mid
            else:
                low = mid + 1

        return low


print(Solution(4).firstBadVersion(5))
"""
流れ: n=5, bad=4

バージョン状態: [1:good, 2:good, 3:good, 4:bad, 5:bad]
目標: 最初のbadバージョン = 4

========================================

初期状態: left=1, right=5
探索範囲: [1, 2, 3, 4, 5] (全体)
Position: │ 1 │ 2 │ 3 │ 4 │ 5 │
            L           ?   R
                       bad=4

========================================

Iteration 1: left=1, right=5
条件チェック: left(1) < right(5) → True

mid計算: mid = (1 + 5) // 2 = 3
isBadVersion(3) を呼び出し

API判定:
- version = 3, bad = 4
- 3 < 4 なので return false (good)

結果: isBadVersion(3) = false
処理: else節実行 → left = mid + 1 = 4
新探索範囲: [4, 5]

Position: │ 1 │ 2 │ 3 │ 4 │ 5 │
                        L   R

========================================

Iteration 2: left=4, right=5
条件チェック: left(4) < right(5) → True

mid計算: mid = (4 + 5) // 2 = 4
isBadVersion(4) を呼び出し

API判定:
- version = 4, bad = 4
- 4 >= 4 なので return true (bad)

結果: isBadVersion(4) = true
処理: if節実行 → right = mid = 4
新探索範囲: [4, 4]

Position: │ 1 │ 2 │ 3 │ 4 │ 5 │
                       L,R

========================================

Iteration 3: left=4, right=4
条件チェック: left(4) < right(4) → False
while ループ終了

結果: return left = 4 ✓
"""

# ------------------------------------------------------------


print(Solution(1).firstBadVersion(1))
"""
流れ: n=1, bad=1

バージョン状態: [1:bad]
目標: 最初のbadバージョン = 1

========================================

初期状態: low=1, high=1
探索範囲: [1] (1つだけ)
Position: │ 1 │
           L,H

========================================

Iteration 1: low=1, high=1
条件チェック: low(1) < high(1) → False
while ループに入らない

結果: return low = 1 ✓
"""

# ------------------------------------------------------------


print(Solution(7).firstBadVersion(10))
"""
流れ: n=10, bad=7 (例として)

バージョン状態: [1,2,3,4,5,6:good, 7,8,9,10:bad]
目標: 最初のbadバージョン = 7

========================================

初期状態: low=1, high=10
探索範囲: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (全体)
Position: │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │
            L               ?                   H

========================================

Iteration 1: low=1, high=10
条件チェック: low(1) < high(10) → True

mid計算: mid = (1 + 10) // 2 = 5
isBadVersion(5) を呼び出し

API判定:
- version = 5, bad = 7
- 5 < 7 なので return false (good)

結果: isBadVersion(5) = false
処理: else節実行 → low = mid + 1 = 6
新探索範囲: [6, 7, 8, 9, 10]

Position: │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │
                                L   ?           H

========================================

Iteration 2: low=6, high=10
条件チェック: low(6) < high(10) → True

mid計算: mid = (6 + 10) // 2 = 8
isBadVersion(8) を呼び出し

API判定:
- version = 8, bad = 7
- 8 >= 7 なので return true (bad)

結果: isBadVersion(8) = true
処理: if節実行 → high = mid = 8
新探索範囲: [6, 7, 8]

Position: │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │
                                L   ?   H

========================================

Iteration 3: low=6, high=8
条件チェック: low(6) < high(8) → True

mid計算: mid = (6 + 8) // 2 = 7
isBadVersion(7) を呼び出し

API判定:
- version = 7, bad = 7
- 7 >= 7 なので return true (bad)

結果: isBadVersion(7) = true
処理: if節実行 → high = mid = 7
新探索範囲: [6, 7]

Position: │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │
                                L   H

========================================

Iteration 4: low=6, high=7
条件チェック: low(6) < high(7) → True

mid計算: mid = (6 + 7) // 2 = 6
isBadVersion(6) を呼び出し

API判定:
- version = 6, bad = 7
- 6 < 7 なので return false (good)

結果: isBadVersion(6) = false
処理: else節実行 → low = mid + 1 = 7
新探索範囲: [7, 7]

Position: │ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │ 8 │ 9 │10 │
                                   L,H

========================================

Iteration 5: low=7, high=7
条件チェック: low(7) < high(7) → False
while ループ終了

結果: return low = 7 ✓

========================================
"""
