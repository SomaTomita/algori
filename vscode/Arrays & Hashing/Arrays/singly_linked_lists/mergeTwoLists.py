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
