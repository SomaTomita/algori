"""
Move Zeroes (Two Pointers / Same direction: slow & fast)

Given an integer array `nums`, move all zeros to the end while keeping the
relative order of the non-zero elements unchanged. Do it in-place without
making a copy of the array.

呼び出し側との約束:
- 配列そのものを書き換える (in-place / 戻り値なし)
- 非ゼロ要素の並び順はそのまま保つ
- ゼロは全部うしろへ寄せる

Example 1:
Input : nums = [2, 0, 4, 0, 9]
Output: [2, 4, 9, 0, 0]

Example 2:
Input : nums = [0, 1, 0, 3, 12]
Output: [1, 3, 12, 0, 0]

Constraints:
- 1 <= len(nums) <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1
"""


# ------------------------------------------------------------
# 解法: slow / fast Two Pointers (同方向 + swap)
# ------------------------------------------------------------
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
nums1 = [2, 0, 4, 0, 9]
Solution().moveZeroes(nums1)
print(nums1)                       # → 出力: [2, 4, 9, 0, 0]

nums2 = [0, 1, 0, 3, 12]
Solution().moveZeroes(nums2)
print(nums2)                       # → 出力: [1, 3, 12, 0, 0]

nums3 = [0]
Solution().moveZeroes(nums3)
print(nums3)                       # → 出力: [0] (要素 1 つ)

nums4 = [1, 2, 3]
Solution().moveZeroes(nums4)
print(nums4)                       # → 出力: [1, 2, 3] (ゼロなし = そのまま)

nums5 = [0, 0, 1]
Solution().moveZeroes(nums5)
print(nums5)                       # → 出力: [1, 0, 0]


"""
登場人物:
  slow = 「次に非ゼロを置く場所」を指す書き込み役。
         slow の手前 nums[0:slow] は確定した非ゼロ列。
  fast = 配列を端から端まで読む偵察役。for の変数なので毎周かならず +1。

非ゼロを見つけたら、確定列の最後尾 (slow) と入れ替えて 1 つ伸ばす。
ゼロのときは何もしない → fast だけ先へ進み、ゼロは後方に取り残される。
戻り値なし。nums を直接書き換えるだけ (in-place)。

----------------------------------------

流れ: nums = [2, 0, 4, 0, 9]   (len = 5)

  index :  0   1   2   3   4
  array : [2] [0] [4] [0] [9]

========================================

初期: slow = 0

  [2] [0] [4] [0] [9]
   s
   f                       ← fast も 0 から

fast は for の変数なので「毎周かならず +1」。
slow は「非ゼロのとき」だけ +1。だから常に slow <= fast。

----------------------------------------

fast=0: nums[0]=2 はゼロ? No → swap(slow=0, fast=0) は自分同士なので変化なし
        slow += 1 (slow=1)

  [2] [0] [4] [0] [9]
       s
       f

----------------------------------------

fast=1: nums[1]=0 はゼロ? Yes → 何もしない (ゼロは取り残す)

  [2] [0] [4] [0] [9]
       s
           f

----------------------------------------

fast=2: nums[2]=4 はゼロ? No → swap(slow=1, fast=2)
        nums[1] と nums[2] を入れ替え, slow += 1 (slow=2)

  [2] [4] [0] [0] [9]        ← nums[1]=0 と nums[2]=4 が入れ替わった
           s
               f

----------------------------------------

fast=3: nums[3]=0 はゼロ? Yes → 何もしない

  [2] [4] [0] [0] [9]
           s
                   f

----------------------------------------

fast=4: nums[4]=9 はゼロ? No → swap(slow=2, fast=4)
        nums[2] と nums[4] を入れ替え, slow += 1 (slow=3)

  [2] [4] [9] [0] [0]        ← nums[2]=0 と nums[4]=9 が入れ替わった
               s
                   f

----------------------------------------

ループ終了: slow = 3

  非ゼロ列 = nums[0:slow] = nums[0:3] = [2, 4, 9]   ✓
  うしろの [0, 0] にゼロが寄った                      ✓
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
時間計算量: O(n)
  - fast は配列を 1 回なめるだけ (n 周)
  - swap も slow の更新も各周 O(1)

空間計算量: O(1)
  - ポインタ 2 つしか追加で使わない。新しい配列を作らず in-place で寄せる。

ポイント (Why this works):
  1. 「fast が前にいる」は前提ではなく構造上の結果。
     fast は for の変数で無条件に +1、slow は非ゼロのときしか +1 しない。
     よって常に slow <= fast が成り立つ。
       - fast = 偵察役 (全部読む)
       - slow = 書き込み役 (確定した非ゼロ列の最後尾の「次」を指す)
     slow と fast に挟まれた範囲が、ちょうど「これまでに見たゼロ」になる。

  2. swap が順序を壊さない理由:
     slow から fast までの間にあるのはゼロだけ。だから非ゼロ要素 (fast) を
     slow へ前送りしても、追い越す相手はゼロのみで、非ゼロ同士の前後関係は
     一切入れ替わらない。結果として相対順序が保たれる。

  3. 「前に詰めてから後ろをゼロ埋め」の 2 パス解法でも正解は出せるが、
     この swap 版は 1 パスで詰めとゼロ寄せを同時に終える。書き込み回数も
     非ゼロの個数ぶんだけで済む。
"""
