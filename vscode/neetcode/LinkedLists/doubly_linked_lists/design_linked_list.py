"""
Design Linked List

Design your implementation of the linked list. You can choose to use a singly
or doubly linked list. (この実装は doubly linked list)

Implement the MyLinkedList class:
- MyLinkedList()                       Initializes the MyLinkedList object.
- int  get(int index)                  index 番目のノードの値を返す。無効なら -1。
- void addAtHead(int val)              先頭に追加
- void addAtTail(int val)              末尾に追加
- void addAtIndex(int index, int val)  index 番目の "前" に挿入。
                                       index == length なら末尾に追加。
                                       index > length なら無視。
- void deleteAtIndex(int index)        index 番目を削除 (有効なら)

Example:
Input
["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
[[],[1],[3],[1,2],[1],[1],[1]]
Output
[null,null,null,null,2,null,3]

Constraints:
0 <= index, val <= 1000
At most 2000 calls will be made.
"""


# ------------------------------------------------------------
# ノード定義 (双方向)
# ------------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next


# ------------------------------------------------------------
# MyLinkedList: 番兵 (sentinel) 方式の双方向連結リスト
# ------------------------------------------------------------
# 構造:
#
#  left (sentinel) ⇄ node1 ⇄ node2 ⇄ ... ⇄ right (sentinel)
#
# 両端に番兵を置くと、"先頭/末尾だけ特別扱い" が消えて
# 挿入・削除のコードが超シンプルになる。
# ------------------------------------------------------------
class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)         # 先頭の番兵
        self.right = ListNode(0)        # 末尾の番兵
        self.left.next = self.right
        self.right.prev = self.left

    # ----------------------------------------
    def get(self, index: int) -> int:
        # 先頭の "本物のノード" から index 個進む
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        # 末尾の番兵 (right) に到達 = index が範囲外
        if cur and cur != self.right:
            return cur.val
        return -1

    # ----------------------------------------
    def addAtHead(self, val: int) -> None:
        # 番兵 left の "直後" に挿入する形
        node = ListNode(val)
        nxt, prev = self.left.next, self.left

        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    # ----------------------------------------
    def addAtTail(self, val: int) -> None:
        # 番兵 right の "直前" に挿入する形
        node = ListNode(val)
        nxt, prev = self.right, self.right.prev

        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    # ----------------------------------------
    def addAtIndex(self, index: int, val: int) -> None:
        # cur が "index 番目のノード (= 挿入したい位置の右側)" になるまで進む
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        # cur が None = index がリスト長を超えていた → 何もしない
        # cur == self.right の場合は "末尾追加" として有効 (index == 長さ)
        if cur and index == 0:
            node = ListNode(val)
            nxt, prev = cur, cur.prev

            # 4 本のリンクを張り替え
            prev.next = node
            nxt.prev = node
            node.next = nxt
            node.prev = prev

    # ----------------------------------------
    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1

        # 末尾番兵 right はスキップ (= index が範囲外)
        if cur and cur != self.right and index == 0:
            nxt, prev = cur.next, cur.prev
            prev.next = nxt
            nxt.prev = prev

    # ----------------------------------------
    # デバッグ用: 中身をリスト化して可視化
    def to_list(self) -> list:
        result = []
        cur = self.left.next
        while cur and cur != self.right:
            result.append(cur.val)
            cur = cur.next
        return result


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
ll = MyLinkedList()
ll.addAtHead(1)        # [1]
ll.addAtTail(3)        # [1, 3]
ll.addAtIndex(1, 2)    # [1, 2, 3]   index=1 の "前" に 2 を挿入
print(ll.to_list())    # [1, 2, 3]
print(ll.get(1))       # 2
ll.deleteAtIndex(1)    # [1, 3]
print(ll.to_list())    # [1, 3]
print(ll.get(1))       # 3

"""
流れ: 上のテストの内部状態

初期:
  left ⇄ right                              (リスト長: 0)

addAtHead(1):
  left ⇄ [1] ⇄ right                        (長さ 1)

addAtTail(3):
  left ⇄ [1] ⇄ [3] ⇄ right                  (長さ 2)

addAtIndex(1, 2):
  cur をリストの先頭から index=1 ステップ進める → cur = [3]
  [3] の "直前" に新ノード [2] を挿入

  Before:    left ⇄ [1] ⇄ [3] ⇄ right
                          ↑
                    cur = [3], cur.prev = [1]

  挿入処理:
    node = [2]
    prev = cur.prev = [1]
    nxt  = cur      = [3]

    prev.next = node   →  [1].next = [2]
    nxt.prev  = node   →  [3].prev = [2]
    node.next = nxt    →  [2].next = [3]
    node.prev = prev   →  [2].prev = [1]

  After:     left ⇄ [1] ⇄ [2] ⇄ [3] ⇄ right (長さ 3)

get(1):
  先頭から 1 ステップ進む → [2]
  [2] != right なので [2].val = 2 を返す

deleteAtIndex(1):
  先頭から 1 ステップ進む → cur = [2]
  prev = [1], nxt = [3]
  [1].next = [3], [3].prev = [1]

  After:     left ⇄ [1] ⇄ [3] ⇄ right       (長さ 2)

get(1):
  先頭から 1 ステップ進む → [3]
  [3].val = 3 を返す
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
n = リスト長

  get(i)            : O(i)        ← 先頭から i 個辿る
  addAtHead(v)      : O(1)
  addAtTail(v)      : O(1)        ← 末尾の番兵 right を覚えているので即アクセス
  addAtIndex(i, v)  : O(i)        ← 挿入位置まで辿る
  deleteAtIndex(i)  : O(i)

空間: O(n)

ポイント:
1. 番兵 (sentinel) を両端に置くと、ヘッドや末尾の特殊ケースが消える。
   挿入は常に "prev と nxt の間に node を挟む" という同一ロジックで書ける。

2. 双方向 (prev も持つ) にする最大のメリットは
   addAtTail と "ノード自身を見ながらの削除" が O(1) で書けること。
   片方向リストでは末尾追加が O(n) になる。

3. addAtIndex の判定 "if cur and index == 0":
   - cur is None      → index がリスト長を超えた (異常)
   - cur == self.right → index がちょうど長さに等しい (= 末尾追加)
                         この場合も挿入は有効 (right の直前に挟む)
   - cur がそれ以外    → index 番目の位置に挿入 (right ではないので途中)

4. リンクの張り替えは順序が重要:
   先に node の prev/next を設定する書き方でもよいが、
   "外側から内側へ" or "4本まとめて" のどちらかに統一しておくと
   バグりにくい。
"""
