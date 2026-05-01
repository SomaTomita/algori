"""
Merge K Sorted Linked Lists
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:
Input: lists = [[1,2,4],[1,3,5],[3,6]]
Output: [1,1,2,3,3,4,5,6]

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
0 <= lists.length <= 1000
0 <= lists[i].length <= 100
-1000 <= lists[i][j] <= 1000
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List


class MergeSolution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 空のリストや空の配列の場合の処理
        if not lists or len(lists) == 0:
            return None

        # リストが1つになるまで繰り返し
        while len(lists) > 1:
            mergedLists = []

            # リストを2つずつペアにしてマージ
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))

            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        """2つのソート済みリストをマージ"""
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # 残りの要素を追加
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next


print(
    MergeSolution().mergeKLists(
        [
            ListNode(1, ListNode(4, ListNode(5))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(2, ListNode(6)),
        ]
    )
)

"""
初期状態: lists = [リスト1, リスト2, リスト3]
         [1->4->5], [1->3->4], [2->6]

=== 1回目のwhile len(lists) > 1ループ ===
len(lists) = 3 > 1 なので継続
mergedLists = []

for i in range(0, 3, 2): # i = 0, 2

i=0の時:
  l1 = lists[0] = [1->4->5]
  l2 = lists[1] = [1->3->4]
  mergeList(l1, l2)の実行:
    - 1 < 1 False → l2を選択 → [1]
    - 1 < 3 True  → l1を選択 → [1->1]
    - 4 < 3 False → l2を選択 → [1->1->3]
    - 4 < 4 False → l2を選択 → [1->1->3->4]
    - 4 < None    → l1の残り → [1->1->3->4->4->5]
  結果: [1->1->3->4->4->5]
  mergedLists.append([1->1->3->4->4->5])

i=2の時:
  l1 = lists[2] = [2->6]
  l2 = None (i+1=3 >= len(lists))
  mergeList([2->6], None) = [2->6]
  mergedLists.append([2->6])

lists = mergedLists = [[1->1->3->4->4->5], [2->6]]

=== 2回目のwhile len(lists) > 1ループ ===
len(lists) = 2 > 1 なので継続
mergedLists = []

for i in range(0, 2, 2): # i = 0

i=0の時:
  l1 = [1->1->3->4->4->5]
  l2 = [2->6]
  mergeList(l1, l2)の実行:
    - 1 < 2 True  → l1を選択 → [1]
    - 1 < 2 True  → l1を選択 → [1->1]
    - 3 < 2 False → l2を選択 → [1->1->2]
    - 3 < 6 True  → l1を選択 → [1->1->2->3]
    - 4 < 6 True  → l1を選択 → [1->1->2->3->4]
    - 4 < 6 True  → l1を選択 → [1->1->2->3->4->4]
    - 5 < 6 True  → l1を選択 → [1->1->2->3->4->4->5]
    - None < 6    → l2の残り → [1->1->2->3->4->4->5->6]
  結果: [1->1->2->3->4->4->5->6]
  mergedLists.append([1->1->2->3->4->4->5->6])

lists = [[1->1->2->3->4->4->5->6]]

=== 3回目のwhile len(lists) > 1の条件チェック ===
len(lists) = 1 なので終了

return lists[0] = [1->1->2->3->4->4->5->6]
"""
