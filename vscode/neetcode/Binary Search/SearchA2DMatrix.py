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


# ------------------------------------------------------------
# 失敗例 (target が存在しない)
# ------------------------------------------------------------
print(Solution().searchMatrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15))

"""
流れ: target = 15

PHASE 1: 行特定
初期: top=0, bottom=2

Iteration 1: row = (0+2)//2 = 1, Row 1 = [10..13]
  target(15) > matrix[1][-1](13) → True
  処理: top = 2  (15 は Row 1 より大きい → 下の行へ)

Iteration 2: top=2, bottom=2 → row = 2, Row 2 = [14..40]
  target(15) > matrix[2][-1](40)? → 15 > 40 False
  target(15) < matrix[2][0](14)?  → 15 < 14 False
  else 節 → break  (15 は Row 2 の範囲 [14, 40] の中にあるはず)

Phase 1 結果: row = 2

========================================

PHASE 2: Row 2 = [14, 20, 30, 40] の中で 15 を二分探索

Iteration 1: left=0, right=3, mid=1, matrix[2][1]=20
  15 < 20 → right = 0

Iteration 2: left=0, right=0, mid=0, matrix[2][0]=14
  15 > 14 → left = 1

Iteration 3: left=1, right=0
  ループ条件 left <= right が False → 終了

return False ✓ (15 はどこにもない)
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
m = 行数, n = 列数

時間:
  Phase 1 (行を特定): O(log m)
  Phase 2 (列を特定): O(log n)
  合計: O(log m + log n) = O(log(m * n))

空間: O(1)

ポイント:
1. 「各行はソート済み + 行をまたいでも昇順」という条件があるので、
   行列全体を 1 本の長いソート済み配列とみなせる。
   座標変換 (i, j) <-> idx = i*n + j を使えば 1 段階の二分探索でも書ける。
2. この実装は読みやすさ重視で 2 段階に分けている (行二分探索 → 列二分探索)。
   どちらでも漸近計算量は同じ。
3. break で Phase 1 を抜けた時点で row が確定するが、
   その後 "if not (top <= bottom)" で見つからなかったケースも検出できる。
"""
