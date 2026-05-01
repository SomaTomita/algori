# Insertion Sort List
# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:

# Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.

# It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm.
# The partially sorted list (black) initially contains only the first element in the list.
# One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

# Example 1:
# Input: head = [4,2,1,3]
# Output: [1,2,3,4]

# Example 2:
# Input: head = [-1,5,3,4,0]
# Output: [-1,0,3,4,5]

# Constraints:
# The number of nodes in the list is in the range [1, 5000].
# -5000 <= Node.val <= 5000


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = head, head.next

        while curr:
            # ソート済みの場合はスキップ
            if curr.val >= prev.val:
                prev, curr = curr, curr.next
                continue

            # 挿入する位置を探す
            tmp = dummy
            while curr.val > tmp.next.val:
                tmp = tmp.next

            # 挿入する
            prev.next = curr.next
            curr.next = tmp.next
            tmp.next = curr

            curr = prev.next

        return dummy.next


print(Solution().insertionSortList(ListNode(4, ListNode(2, ListNode(1, ListNode(3))))))

# 流れ:
# dummy = ListNode(0, head) [0 -> 4 -> 2 -> 1 -> 3]
# prev = 4, curr = 2

# 1回目のループ
# while -- curr.val >= prev.val → 2 >= 4 ** False
# tmp = dummy (val=0)
# while -- curr.val > tmp.next.val → 2 > 4 ** False (ループに入らない)
# 挿入処理:
# prev.next = curr.next → 4.next = 1 (2を切り離し)
# curr.next = tmp.next → 2.next = 4 (2の次を4に)
# tmp.next = curr → 0.next = 2 (dummyの次を2に)
# curr = prev.next → curr = 1
# 結果: [0 -> 2 -> 4 -> 1 -> 3]

# 2回目のループ
# curr = 1, prev = 4
# while -- curr.val >= prev.val → 1 >= 4 ** False
# tmp = dummy (val=0)
# while -- curr.val > tmp.next.val → 1 > 2 ** False (ループに入らない)
# 挿入処理:
# prev.next = curr.next → 4.next = 3 (1を切り離し)
# curr.next = tmp.next → 1.next = 2 (1の次を2に)
# tmp.next = curr → 0.next = 1 (dummyの次を1に)
# curr = prev.next → curr = 3
# 結果: [0 -> 1 -> 2 -> 4 -> 3]

# 3回目のループ
# curr = 3, prev = 4
# while -- curr.val >= prev.val → 3 >= 4 ** False
# tmp = dummy (val=0)
# while -- curr.val > tmp.next.val → 3 > 1 ** True
#   tmp = tmp.next → tmp = 1
# while -- curr.val > tmp.next.val → 3 > 2 ** True
#   tmp = tmp.next → tmp = 2
# while -- curr.val > tmp.next.val → 3 > 4 ** False (ループ終了)
# 挿入処理:
# prev.next = curr.next → 4.next = None (3を切り離し)
# curr.next = tmp.next → 3.next = 4 (3の次を4に)
# tmp.next = curr → 2.next = 3 (2の次を3に)
# curr = prev.next → curr = None
# 結果: [0 -> 1 -> 2 -> 3 -> 4]

# return dummy.next → [1, 2, 3, 4]


print(
    Solution().insertionSortList(
        ListNode(2, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
    )
)

# 流れ:
# 初期状態: [0 -> 2 -> 5 -> 3 -> 4 -> 0]
# prev = 2, curr = 5

# 1回目のループ
# curr.val >= prev.val → 5 >= 2 ** True (スキップ)
# prev, curr = 5, 3

# 2回目のループ
# curr.val >= prev.val → 3 >= 5 ** False
# tmp = dummy (val=0)
# while -- curr.val > tmp.next.val → 3 > 2 ** True
#   tmp = tmp.next → tmp = 2 (val=2)
# while -- curr.val > tmp.next.val → 3 > 5 ** False (ループ終了)
# 挿入処理:
# prev.next = curr.next → 5.next = 4 (3を切り離し)
# curr.next = tmp.next → 3.next = 5 (3の次を5に)
# tmp.next = curr → 2.next = 3 (2の次を3に)
# curr = prev.next → curr = 4
# 結果: [0 -> 2 -> 3 -> 5 -> 4 -> 0]

# 3回目のループ
# curr = 4, prev = 5
# curr.val >= prev.val → 4 >= 5 ** False
# tmp = dummy (val=0)
# while -- curr.val > tmp.next.val → 4 > 2 ** True
#   tmp = tmp.next → tmp = 2 (val=2)
# while -- curr.val > tmp.next.val → 4 > 3 ** True
#   tmp = tmp.next → tmp = 3 (val=3)
# while -- curr.val > tmp.next.val → 4 > 5 ** False (ループ終了)
# 挿入処理:
# prev.next = curr.next → 5.next = 0 (4を切り離し)
# curr.next = tmp.next → 4.next = 5 (4の次を5に)
# tmp.next = curr → 3.next = 4 (3の次を4に)
# curr = prev.next → curr = 0
# 結果: [0 -> 2 -> 3 -> 4 -> 5 -> 0]

# 4回目のループ
# curr = 0, prev = 5
# curr.val >= prev.val → 0 >= 5 ** False
# tmp = dummy (val=0)
# while -- curr.val > tmp.next.val → 0 > 2 ** False (ループに入らない)
# 挿入処理:
# prev.next = curr.next → 5.next = None (0を切り離し)
# curr.next = tmp.next → 0.next = 2 (0の次を2に)
# tmp.next = curr → 0.next = 0 (dummyの次を0に)
# curr = prev.next → curr = None
# 結果: [0 -> 0 -> 2 -> 3 -> 4 -> 5]

# return dummy.next → [0, 2, 3, 4, 5]


# ------------------------------------------------------------
# アルゴリズムの考え方 (図で理解)
# ------------------------------------------------------------
"""
連結リスト版の挿入ソートのキーアイデア:

  dummy → [ソート済み領域] → [未処理領域]
                            ↑      ↑
                          prev   curr

1. curr (未処理の先頭) を見る
2. 既にソート済み領域の最後 (prev) より大きい or 等しいなら、
   そのまま並びを保ってよい → prev, curr を 1 ステップ進める
3. そうでなければ、ソート済み領域を dummy から走査 (tmp) して
   curr が入るべき位置を見つけ、そこに繋ぎ替える
4. 繋ぎ替え後、curr = prev.next (= 元の curr.next) にして次へ

繋ぎ替えの 3 ステップ (curr を tmp の "次" に挿入する):
  prev.next = curr.next  ← curr を未処理領域から外す
  curr.next = tmp.next   ← curr の次を、tmp の元の次に
  tmp.next  = curr       ← tmp の次を curr に

  Before:  ... → tmp → tmp.next → ...   (ソート済み内)
                       ... → prev → curr → curr.next → ...  (途中で curr が拾われる)

  After:   ... → tmp → curr → tmp.next → ...
                       ... → prev → curr.next → ...
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
n = リスト長

時間:
  最良 O(n)    ← 既にソート済みなら "if curr.val >= prev.val" で全部スキップ
  平均 O(n^2)
  最悪 O(n^2)  ← 逆順入力など、毎回先頭付近への挿入が必要

空間: O(1)  ← dummy 以外、新しいノードを作らず既存ノードを繋ぎ替えるだけ

ポイント:
1. 配列の挿入ソートとの違い: ノードを動かすのにシフトが要らないので、
   "挿入位置の発見" 自体は同じ O(i) でも実装が簡潔。

2. dummy ノードを使うことで「先頭への挿入」を特別扱いせずに書ける。
   tmp = dummy から始めれば、curr.val が dummy.next より小さくても
   そのまま tmp.next に繋ぎ替えるだけで済む。

3. 既にソート済みの並び (curr.val >= prev.val) はスキップするのが鍵。
   この最適化があるおかげで、最良ケースが O(n) になる。

4. 安定ソート: 等しい値については元の順序を保つ (>= で判定しているため)。
"""
