# Merge Two Sorted Linked Lists
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted linked list and
#  return the head of the new sorted linked list.

# The new list should be made up of nodes from list1 and list2.

# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,5]
# Output: [1,1,2,3,4,5]

# Example 2:
# Input: list1 = [], list2 = [1,2]
# Output: [1,2]

# Example 3:
# Input: list1 = [], list2 = []
# Output: []

# Constraints:
# 0 <= The length of the each list <= 100.
# -100 <= Node.val <= 100
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # 先頭のダミーノード（結果リストの始まりを固定するため）
        tail = dummy  # 現在の末尾を指すポインタ

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # 残り
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        return dummy.next  # ダミーの次が新しいリストの先頭


# 処理の流れ詳細 (l1=[1,2,4], l2=[1,3,5])

# 初期状態:
# dummy = [0] (ダミーノード)
# tail = dummy (= [0])
# l1 = [1] -> [2] -> [4]
# l2 = [1] -> [3] -> [5]

# 1回目のループ:
# l1.val = 1, l2.val = 1
# 1 <= 1 なので else側: l2を選択
# tail.next = l2 (= [1])
# l2 を [3] -> [5] に進める
# tail を [1] に進める
# 現在のリスト: [0] -> [1]

# 2回目のループ:
# l1.val = 1, l2.val = 3
# 1 < 3 なので if側: l1を選択
# tail.next = l1 (= [1])
# l1 を [2] -> [4] に進める
# tail を [1] に進める
# 現在のリスト: [0] -> [1] -> [1]

# 3回目のループ:
# l1.val = 2, l2.val = 3
# 2 < 3 なので if側: l1を選択
# tail.next = l1 (= [2])
# l1 を [4] に進める
# tail を [2] に進める
# 現在のリスト: [0] -> [1] -> [1] -> [2]

# 4回目のループ:
# l1.val = 4, l2.val = 3
# 4 > 3 なので else側: l2を選択
# tail.next = l2 (= [3])
# l2 を [5] に進める
# tail を [3] に進める
# 現在のリスト: [0] -> [1] -> [1] -> [2] -> [3]

# 5回目のループ:
# l1.val = 4, l2.val = 5
# 4 < 5 なので if側: l1を選択
# tail.next = l1 (= [4])
# l1 を [] に進める
# tail を [4] に進める
# 現在のリスト: [0] -> [1] -> [1] -> [2] -> [3] -> [4]

# ループ終了後:
# l1 = []（空）
# l2 = [5]が残っている
# l2が残っているので、tail.next = l2で残りを接続
# 最終的なリスト: [0] -> [1] -> [1] -> [2] -> [3] -> [4] -> [5]

# 戻り値:
# dummy.next を返す（先頭の[0]を除いた[1]から始まるリスト）
# 結果: [1] -> [1] -> [2] -> [3] -> [4] -> [5]


# ------------------------------------------------------------


# 別解


class Solution:
    def mergeTwoLists_recursive(self, list1: ListNode, list2: ListNode) -> ListNode:
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists_recursive(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists_recursive(list1, list2.next)
            return list2


# ------------------------------------------------------------
# 再帰版の流れ: list1 = [1,2,4], list2 = [1,3,5]
# ------------------------------------------------------------
#
# 呼び出しツリー (上から下へ展開、答えは下から上へ巻き戻る):
#
# merge([1,2,4], [1,3,5])
#   1 < 1 が False なので list2 を選択 → 1(l2).next = merge([1,2,4], [3,5])
#     1 < 3 True → list1 選択 → 1(l1).next = merge([2,4], [3,5])
#       2 < 3 True → list1 選択 → 2.next = merge([4], [3,5])
#         4 < 3 False → list2 選択 → 3.next = merge([4], [5])
#           4 < 5 True → list1 選択 → 4.next = merge([], [5])
#             list1 が空 → return list2 (= [5])
#           ← 4.next = [5] → リスト末尾は 4 → 5
#         ← 3.next = (4 → 5) → 3 → 4 → 5
#       ← 2.next = (3 → 4 → 5) → 2 → 3 → 4 → 5
#     ← 1(l1).next = (2 → 3 → 4 → 5) → 1 → 2 → 3 → 4 → 5
#   ← 1(l2).next = (1 → 2 → 3 → 4 → 5) → 1 → 1 → 2 → 3 → 4 → 5
#
# 最終結果: 1 → 1 → 2 → 3 → 4 → 5
#
# ------------------------------------------------------------
# ベースケース:
#   - 両方とも None なら None
#   - 片方だけ None なら残り片方を返す (= "残りを丸ごと連結する" のと同義)
# 再帰ステップ:
#   - 小さい方の head を取り、その next に "残り両方をマージした結果" を繋ぐ
# ------------------------------------------------------------


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
n = len(l1), m = len(l2)

反復版 (上のクラス):
  時間: O(n + m) — 各ノードを 1 回ずつ訪れる
  空間: O(1)     — 既存ノードを繋ぎ替えるだけ。新しいノードは dummy のみ。

再帰版:
  時間: O(n + m)
  空間: O(n + m) — 再帰スタック (LeetCode の制約 n+m <= 200 なら安全)

ポイント:
1. dummy ノードを使うと "結果リストの先頭がまだ決まっていない" 段階で
   tail の繋ぎ替えが綺麗に書ける。先頭判定の if が要らなくなる典型テク。

2. 反復版は "両方の先頭を比較 → 小さい方を tail に繋ぐ → そっちを 1 個進める"
   の繰り返し。ループを抜けたら "片方は空、もう片方に残りがある" 状態なので
   残りをそのまま tail に繋いで終わり。

3. 安定性: 等値の場合 (l1.val == l2.val) は else 側 (l2 優先) になるが、
   どちらを先にしても結果のソート性は保たれる。
"""
