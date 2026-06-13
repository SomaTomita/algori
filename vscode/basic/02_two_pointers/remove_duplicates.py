"""
Remove Duplicates from Sorted Array (Two Pointers / Same direction: slow & fast)

Given an integer array `arr` sorted in non-decreasing order, remove the
duplicates in-place so that each unique element appears only once. The
relative order must be kept. Return the number of unique elements `k`.

呼び出し側との約束:
- 配列の先頭 `arr[0:k]` にユニークな値を詰め直す (in-place)
- 戻り値 `k` = ユニーク要素の個数
- `arr[k:]` 以降に何が残っていても気にしない (ゴミ扱い)

Example 1:
Input : arr = [1, 1, 2]
Output: 2,  arr の先頭が [1, 2, ...] になる

Example 2:
Input : arr = [1, 1, 2, 3, 3]
Output: 3,  arr の先頭が [1, 2, 3, ...] になる

Constraints:
- 0 <= len(arr) <= 3 * 10^4
- arr は非減少順 (ソート済み) であること。
"""


# ------------------------------------------------------------
# 解法: slow / fast Two Pointers (同方向)
# ------------------------------------------------------------
class Solution:
    def removeDuplicates(self, arr: list[int]) -> int:
        # 空配列は 0 個 (range(0) は回らず slow が初期値のまま残るので先に弾く)
        if not arr:
            return 0

        # slow = 「確定したユニーク列の最後尾」を指す書き込み役
        # fast = 配列を端から端まで読む偵察役 (for の変数なので毎周かならず +1)
        slow = 0
        # 例: [1, 1, 2, 3, 3] のとき
        #   fast=0: arr[0]=1 vs arr[0]=1 → 同じ → スキップ (slow=0)
        #   fast=1: arr[1]=1 vs arr[0]=1 → 同じ → スキップ (slow=0)
        #   fast=2: arr[2]=2 vs arr[0]=1 → 違う → slow=1, arr[1]=2
        #   fast=3: arr[3]=3 vs arr[1]=2 → 違う → slow=2, arr[2]=3
        #   fast=4: arr[4]=3 vs arr[2]=3 → 同じ → スキップ (slow=2)
        #   return slow + 1 = 3
        for fast in range(len(arr)):
            # 「違ったら」初めて見る新しい値 → ユニーク列を 1 つ伸ばして書き込む
            # (同じときは重複なので何もしない。fast だけが先へ進む)
            if arr[fast] != arr[slow]:
                slow += 1
                arr[slow] = arr[fast]
        # slow は最後のユニーク要素の「インデックス」なので、個数は +1
        return slow + 1


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
arr1 = [1, 1, 2]
k1 = Solution().removeDuplicates(arr1)
print(k1, arr1[:k1])          # → 出力: 2 [1, 2]

arr2 = [1, 1, 2, 3, 3]
k2 = Solution().removeDuplicates(arr2)
print(k2, arr2[:k2])          # → 出力: 3 [1, 2, 3]

arr3 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
k3 = Solution().removeDuplicates(arr3)
print(k3, arr3[:k3])          # → 出力: 5 [0, 1, 2, 3, 4]

print(Solution().removeDuplicates([]))   # → 出力: 0 (空配列)
print(Solution().removeDuplicates([7]))  # → 出力: 1 (要素 1 つ)


"""
流れ: arr = [1, 1, 2, 3, 3]   (len = 5)

  index :  0   1   2   3   4
  array : [1] [1] [2] [3] [3]

========================================

初期: slow = 0

  [1] [1] [2] [3] [3]
   s
   f                       ← fast も 0 から

fast は for の変数なので「毎周かならず +1」。
slow は「違ったとき」だけ +1。だから常に slow <= fast。

----------------------------------------

fast=0: arr[0]=1 vs arr[slow=0]=1 → 違う? No(同じ) → 何もしない

  [1] [1] [2] [3] [3]
   s
   f

----------------------------------------

fast=1: arr[1]=1 vs arr[slow=0]=1 → 違う? No(同じ) → 何もしない (重複なので捨てる)

  [1] [1] [2] [3] [3]
   s
       f

----------------------------------------

fast=2: arr[2]=2 vs arr[slow=0]=1 → 違う? Yes → 新しい値!
        slow += 1 (slow=1), arr[1] = arr[2] = 2

  [1] [2] [2] [3] [3]        ← arr[1] が 1 から 2 へ上書き
       s
           f

----------------------------------------

fast=3: arr[3]=3 vs arr[slow=1]=2 → 違う? Yes → 新しい値!
        slow += 1 (slow=2), arr[2] = arr[3] = 3

  [1] [2] [3] [3] [3]        ← arr[2] が 2 から 3 へ上書き
           s
               f

----------------------------------------

fast=4: arr[4]=3 vs arr[slow=2]=3 → 違う? No(同じ) → 何もしない

  [1] [2] [3] [3] [3]
           s
                   f

----------------------------------------

ループ終了: slow = 2

  ユニーク列 = arr[0 .. slow] = arr[0:3] = [1, 2, 3]   ✓
  後ろの [3, 3] はゴミ (k より後ろなので無視される)

return slow + 1 = 3
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
時間計算量: O(n)
  - fast は配列を 1 回なめるだけ (n 周)
  - slow の更新は各周 O(1)

空間計算量: O(1)
  - ポインタ 2 つしか追加で使わない。新しい配列を作らず in-place で詰める。

ポイント (Why this works):
  1. 「fast が前にいる」は前提ではなく構造上の結果。
     fast は for の変数で無条件に +1、slow は条件付きでしか +1 しない。
     よって常に slow <= fast が成り立つ。
       - fast = 偵察役 (全部読む)
       - slow = 書き込み役 (ユニーク列の最後尾を指す)
     slow と fast に挟まれた範囲が、ちょうど「捨てる重複」になる。

  2. 比較が `arr[fast] != arr[slow]` で済むのは **ソート済み** だから。
     同じ値は必ず隣り合うので「直前のユニーク末尾 1 個」とだけ比べれば
     重複判定が成立する。未ソートだとこの 1 個比較では消せない (要 set など)。

  3. 戻り値は「個数 k」であって配列そのものではない。
     slow はインデックスなので個数にするには +1。`return slow + 1`。
     (元コードにありがちな `return 0` や、fast 基準の `return fast` は誤り。
      fast はループ終了時 len(arr)-1 になっていて重複数と無関係。)
"""
