"""
Search a 2D Matrix
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true

Example 2:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false

Constraints:
m == matrix.length
n == matrix[i].length 1 <= m, n <= 100
1 <= m, n <= 100
-10000 <= matrix[i][j], target <= 10000
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bottom = 0, ROWS - 1
        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break

        if not (top <= bottom):
            return False

        left, right = 0, COLS - 1
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True

        return False


print(Solution().searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))

"""
流れ: matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target = 10

Matrix Structure:
Row 0: │ 1 │ 2 │ 4 │ 8 │  ← matrix[0][0]=1, matrix[0][-1]=8
Row 1: │10 │11 │12 │13 │  ← matrix[1][0]=10, matrix[1][-1]=13  
Row 2: │14 │20 │30 │40 │  ← matrix[2][0]=14, matrix[2][-1]=40

========================================

PHASE 1: 正しい行を特定 (Row Binary Search)

初期状態: top=0, bottom=2, target=10
探索範囲: Row 0, Row 1, Row 2 (全ての行)

Iteration 1: top=0, bottom=2
条件チェック: top(0) <= bottom(2) → True

row計算: row = (0 + 2) // 2 = 1
検査対象: Row 1 = [10, 11, 12, 13]

判定1: target (10) > matrix[1][-1] (13) ?
→ 10 > 13 → False

判定2: target(10) < matrix[1][0](10) ?  
→ 10 < 10 → False

判定3: else節が実行 → break
→ target(10)は Row 1 の範囲内 [10, 13] の間に存在

Phase 1 結果: row = 1 が確定 ✓
Row 1: [10, 11, 12, 13] でPhase 2を実行

========================================

PHASE 2: Row 1 内でBinary Search

初期状態: left=0, right=3, target=10
探索範囲: [10, 11, 12, 13] (Row 1全体)

Column: │ 0 │ 1 │ 2 │ 3 │
Value:  │10 │11 │12 │13 │
          L           R

Iteration 1: left=0, right=3
条件チェック: left(0) <= right(3) → True
mid計算: mid = (0 + 3) // 2 = 1
matrix[row][mid] = matrix[1][1] = 11

比較: target(10) vs matrix[1][1] (11)
→ 10 < 11 なので elif target < matrix[row][mid] が成立
処理: right = mid - 1 = 1 - 1 = 0
新しい探索範囲: [10] (左半分)

Column: │ 0 │ 1 │ 2 │ 3 │
Value:  │10 │11 │12 │13 │
        L,R  mid

Iteration 2: left=0, right=0
条件チェック: left(0) <= right(0) → True
mid計算: mid = (0 + 0) // 2 = 0
matrix[row][mid] = matrix[1][0] = 10

比較: target(10) vs matrix[1][0](10)
→ 10 == 10 なので else (発見!) が成立
処理: return True ✓
"""
