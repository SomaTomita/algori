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


# ------------------------------------------------------------

# 別解: 再帰的にリストを反転


class Solution:
    def reverseList_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList_recursive(head.next)
            head.next.next = head
        head.next = None

        return newHead


print(Solution().reverseList_recursive(Node))

# 処理の流れ:
# 1回目呼び出し: head = Node(0)
#   head.next = Node(1) あり → 再帰呼び出し with head=Node(1)

# 2回目呼び出し: head = Node(1)
#   head.next = Node(2) あり → 再帰呼び出し with head=Node(2)

# 3回目呼び出し: head = Node(2)
#   head.next = Node(3) あり → 再帰呼び出し with head=Node(3)

# 4回目呼び出し: head = Node(3)
#   head.next = None → base case により newHead = Node(3) を返す
#   Node(3).next = None（すでに None）

# 戻り値をたどりながら反転:
# 3回目呼び出し: head = Node(2)
#   newHead = Node(3)
#   head.next.next = head → Node(3).next = Node(2)
#   head.next = None → Node(2).next = None
#   return newHead (= Node(3))

# 2回目呼び出し: head = Node(1)
#   newHead = Node(3)
#   head.next.next = head → Node(2).next = Node(1)
#   head.next = None → Node(1).next = None
#   return newHead (= Node(3))

# 1回目呼び出し: head = Node(0)
#   newHead = Node(3)
#   head.next.next = head → Node(1).next = Node(0)
#   head.next = None → Node(0).next = None
#   return newHead (= Node(3))

# 出力:      Node(3)
# リスト:    3 → 2 → 1 → 0 → None


# ------------------------------------------------------------

# 別解: リストを配列に変換してから反転 (Linked List → Array → Linked List)


def reverseList_list(head: Optional[ListNode]) -> Optional[ListNode]:
    arr = []
    curr = head
    while curr:
        arr.append(curr)
        curr = curr.next

    for i in range(len(arr) - 1, 0, -1):  # 3~0までのインデックスでループ
        arr[i].next = arr[i - 1]
    if arr:
        arr[0].next = None  # 最初のノードのnextをNoneに設定
        return arr[-1]  # 最後のノードを新しいheadとして返す


# 流れ:
# arr = []
# curr = Node(0)
# arr.append(curr) → arr = [Node(0)]
# curr = curr.next → curr = Node(1)
# arr.append(curr) → arr = [Node(0), Node(1)]
# curr = curr.next → curr = Node(2)
# arr.append(curr) → arr = [Node(0), Node(1), Node(2)]
# curr = curr.next → curr = Node(3)
# arr.append(curr) → arr = [Node(0), Node(1), Node(2), Node(3)]
# curr = curr.next → curr = None
# i = 3, arr[i] = Node(3), arr[i-1] = Node(2)
# arr[i].next = arr[i-1] → Node(3).next = Node(2)
# i = 2, arr[i] = Node(2), arr[i-1] = Node(1)
# arr[i].next = arr[i-1] → Node(2).next = Node(1)
# i = 1, arr[i] = Node(1), arr[i-1] = Node(0)
# arr[i].next = arr[i-1] → Node(1).next = Node(0)
# i = 0, arr[i] = Node(0), arr[i-1] = None
# arr[i].next = arr[i-1] → Node(0).next = None
# 出力: Node(3)
# リスト: 3 → 2 → 1 → 0 → None

# ------------------------------------------------------------
# ------------------------------------------------------------

# python基礎

# range(開始値, 終了値, ステップ)の形式
# 5から1まで逆順にカウントダウン
for i in range(5, 0, -1):
    print(i)  # 出力: 5, 4, 3, 2, 1


# リンクドリスト基礎: 作成と表示
def create_linked_list():  # 1 → 2 → 3 → None というリンクドリストを作成
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # ノードを繋げる
    node1.next = node2
    node2.next = node3
    # node3.nextはデフォルトでNone

    return node1  # 先頭のノードを返す


# リンクドリストの表示
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end="")
        if current.next:
            print(" → ", end="")
        current = current.next
    print(" → None")


head = create_linked_list()
print_linked_list(head)  # 出力: 1 → 2 → 3 → None


# ノードの追加例
def add_node(head, val):
    new_node = Node(val)
    if not head:
        return new_node

    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head


# ノードを追加してみる
head = add_node(head, 4)
print("4を追加した後:")
print_linked_list(head)  # 出力: 1 → 2 → 3 → 4 → None
