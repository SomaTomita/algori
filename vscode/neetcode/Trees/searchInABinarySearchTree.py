"""
Search in a Binary Search Tree

You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]


Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []


Constraints:

The number of nodes in the tree is in the range [1, 5000].
1 <= Node.val <= 10^7
root is a binary search tree.
1 <= val <= 10^7
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------------
# 解法1: 反復(Iterative)
# ------------------------------------------------------------
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # BSTの性質: 左部分木の値 < 親 < 右部分木の値
        # → val と現在ノードの値を比較して、片側だけを探索すればよい (O(log n) 平均)
        cur = root
        while cur is not None:
            if val == cur.val:
                return cur          # 見つかった: そのノード(=部分木)を返す
            elif val < cur.val:
                cur = cur.left      # 探したい値は左側にある
            else:
                cur = cur.right     # 探したい値は右側にある

        return None                 # ループ終了 = 見つからなかった


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
def build_example_tree() -> TreeNode:
    """
    例の木を作る: root = [4,2,7,1,3]

           4
          / \
         2   7
        / \
       1   3
    """
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n2 = TreeNode(2, n1, n3)
    n7 = TreeNode(7)
    n4 = TreeNode(4, n2, n7)
    return n4


def to_list(node: Optional[TreeNode]) -> list:
    """確認用: 部分木をレベル順(BFS)でリスト化"""
    if node is None:
        return []
    result, queue = [], [node]
    while queue:
        cur = queue.pop(0)
        if cur is None:
            result.append(None)
            continue
        result.append(cur.val)
        queue.append(cur.left)
        queue.append(cur.right)
    # 末尾の None を取り除いて見やすくする
    while result and result[-1] is None:
        result.pop()
    return result


root = build_example_tree()
print(to_list(Solution().searchBST(root, 2)))  # [2, 1, 3]
print(to_list(Solution().searchBST(root, 5)))  # []


"""
流れ (成功例): root = [4,2,7,1,3], val = 2

木の形:
        4
       / \
      2   7
     / \
    1   3

========================================

初期状態: cur = 4 (root)

       (4) ← cur
       / \
      2   7
     / \
    1   3

========================================

Iteration 1: cur.val = 4
条件チェック: cur is not None → True, ループ継続

比較: val(2) vs cur.val(4)
→ 2 < 4 なので elif val < cur.val が成立

処理: cur = cur.left = 2
"探索したい値は現在ノードより小さい → 左部分木にある"

        4
       / \
     (2) ← cur
     / \
    1   3

========================================

Iteration 2: cur.val = 2
条件チェック: cur is not None → True, ループ継続

比較: val(2) vs cur.val(2)
→ 2 == 2 なので if val == cur.val が成立

処理: return cur (val=2 のノードをそのまま返す)
このノードを根とする部分木 [2, 1, 3] が答え

        4
       / \
     (2) ← FOUND! ここを根とする部分木を返す
     / \
    1   3

========================================

結果: TreeNode(2, TreeNode(1), TreeNode(3))
to_list で表示すると [2, 1, 3] ✓
"""

# ------------------------------------------------------------

"""
流れ (失敗例): root = [4,2,7,1,3], val = 5

========================================

初期状態: cur = 4

Iteration 1: cur.val = 4
比較: val(5) vs 4 → 5 > 4
処理: cur = cur.right = 7

        4
       / \
      2  (7) ← cur
     / \
    1   3

========================================

Iteration 2: cur.val = 7
比較: val(5) vs 7 → 5 < 7
処理: cur = cur.left = None
"7 より小さいので左に行きたいが、7の左の子は存在しない"

========================================

Iteration 3: cur is None
条件チェック: cur is not None → False
→ while ループ終了

結果: return None (見つからない) ✓
"""


# ------------------------------------------------------------
# 別解: 再帰(Recursion)
# ------------------------------------------------------------
class RecursiveSolution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # ベースケース: 木が空 or 値が一致
        if root is None or root.val == val:
            return root

        # BSTの性質に従って片側だけ再帰
        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


print("\n=== Recursive ===")
root2 = build_example_tree()
print(to_list(RecursiveSolution().searchBST(root2, 2)))  # [2, 1, 3]
print(to_list(RecursiveSolution().searchBST(root2, 5)))  # []


"""
Recursionの流れ: root = [4,2,7,1,3], val = 2

呼び出しツリー:
searchBST(node=4, val=2)
  → 2 < 4 なので searchBST(node=2, val=2)
      → 2 == 2 なので return node(=2)
  ← 戻り値は node(=2)
← 最終的に node(=2) が返る

========================================

Call 1: searchBST(root=Node(4), val=2)
条件チェック1: root is None → False
条件チェック2: root.val(4) == val(2) → False

比較: val(2) < root.val(4) → True
処理: return searchBST(root.left, val) = searchBST(Node(2), 2)

        (4) ← Call 1
        / \
       2   7
      / \
     1   3

========================================

Call 2: searchBST(root=Node(2), val=2)
条件チェック1: root is None → False
条件チェック2: root.val(2) == val(2) → True (一致!)

処理: return root (val=2 のノードを返す)

         4
        / \
      (2) ← Call 2 → return root
       / \
      1   3

========================================

戻り値の伝播:
Call 2 が Node(2) を返す
→ Call 1 が Node(2) を返す
→ 最終的に Node(2) (= 部分木 [2,1,3]) が返る ✓


----------------------------------------
失敗例: searchBST(node=4, val=5)
----------------------------------------

Call 1: searchBST(Node(4), 5)
  4 != 5, 5 > 4 → searchBST(Node(7), 5)

Call 2: searchBST(Node(7), 5)
  7 != 5, 5 < 7 → searchBST(Node(7).left, 5) = searchBST(None, 5)

Call 3: searchBST(None, 5)
  root is None → True (Base case)
  → return None

戻り値の伝播:
Call 3 → None
Call 2 → None
Call 1 → None  ✓
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
計算量:
- 平均: O(log n)  ※ 木がバランスしている場合、毎回半分に絞れる
- 最悪: O(n)      ※ 偏った木 (連結リスト状) になっている場合

空間量:
- 反復解: O(1)    ※ ポインタ cur しか使わない
- 再帰解: O(h)    ※ h = 木の高さ。再帰呼び出しのスタック分

ポイント:
1. 二分探索木(BST) の不変条件 "左 < 親 < 右" を使い、
   毎回片側だけを探索することで二分探索と同じ効率を得る。
2. 通常の二分木探索 (DFS / BFS) は O(n) かかるが、
   BST ではこの性質のおかげで O(log n) (平均) に落ちる。
3. 「ノードを返す = そのノードを根とする部分木を返す」と等価。
   TreeNode は子へのポインタを持つので、根を返せば部分木全体が手に入る。
"""
