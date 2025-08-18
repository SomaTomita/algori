# Reverse Linked List
# Given the beginning of a singly linked list head, reverse the list,
#  and return the new beginning of the list.

# Example 1:
# Input: head = [0,1,2,3]
# Output: [3,2,1,0]

# Example 2:
# Input: head = []
# Output: []

# Constraints:
# 0 <= The length of the list <= 1000.
# -1000 <= Node.val <= 1000


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            tempNext = curr.next

            curr.next = prev
            prev = curr
            curr = tempNext

        return prev


Node = ListNode(0, ListNode(1, ListNode(2, ListNode(3))))
# 図解（初期状態）
# head (=Node) → Node(val=0)
#   next → Node(val=1)
#   next → Node(val=2)
#   next → Node(val=3)
#   next → None

print(Solution().reverseList(Node))

# 処理の流れ:
# 初期: prev=None, curr=Node(0)
# 1回目ループ:
#   tempNext = curr.next → Node(1)
#   curr.next = prev → Node(0).next = None
#   prev = curr → prev = Node(0)
#   curr = tempNext → curr = Node(1)
#   リスト状態:
#     反転済み: 0 → None
#     処理中: 1 → 2 → 3 → None
#
# 2回目ループ:
#   tempNext = curr.next → Node(2)
#   curr.next = prev → Node(1).next = Node(0)
#   prev = curr → prev = Node(1)
#   curr = tempNext → curr = Node(2)
#   リスト状態:
#     反転済み: 1 → 0 → None
#     処理中: 2 → 3 → None
#
# 3回目ループ:
#   tempNext = curr.next → Node(3)
#   curr.next = prev → Node(2).next = Node(1)
#   prev = curr → prev = Node(2)
#   curr = tempNext → curr = Node(3)
#   リスト状態:
#     反転済み: 2 → 1 → 0 → None
#     処理中: 3 → None
#
# 4回目ループ:
#   tempNext = curr.next → None
#   curr.next = prev → Node(3).next = Node(2)
#   prev = curr → prev = Node(3)
#   curr = tempNext → curr = None
#   リスト状態:
#     反転済み: 3 → 2 → 1 → 0 → None
#     処理中: None
#
# ループ終了: curr = None
# 出力: prev → 新しい head (Node(3))
# リスト:    3 → 2 → 1 → 0 → None
