"""
Binary Tree Level Order Traversal (BFS)

二分木の各レベル(深さ)ごとに、ノードの値をリストにまとめて返す。

Example:
Input:  root = [3, 9, 20, null, null, 15, 7]
Output: [[3], [9, 20], [15, 7]]

木の形:
        3
       / \
      9   20
          / \
         15   7

レベル 0: [3]
レベル 1: [9, 20]
レベル 2: [15, 7]
"""

from collections import deque
from typing import List, Optional


# ------------------------------------------------------------
# TreeNode (inline)
# ------------------------------------------------------------
class TreeNode:
    def __init__(self, val: int = 0,
                 left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------------
# 解法: BFS (キューを使ってレベルごとに処理)
# ------------------------------------------------------------
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 空の木は空リスト
        if root is None:
            return []

        result: List[List[int]] = []
        q: deque[TreeNode] = deque([root])

        # 例: 木 [3, 9, 20, null, null, 15, 7] のとき
        #   外ループ1: level_size=1 → [3] を取り出し → 子 9, 20 を enqueue
        #             result=[[3]], q=[9, 20]
        #   外ループ2: level_size=2 → [9,20] を取り出し → 20 の子 15, 7 を enqueue
        #             result=[[3],[9,20]], q=[15, 7]
        #   外ループ3: level_size=2 → [15,7] を取り出し → 子なし
        #             result=[[3],[9,20],[15,7]], q=[]
        #   q が空 → ループ終了

        # ポイント: ループの先頭で len(q) を取る
        # → そのループ内で処理するノード数 = 「いま見ているレベルのノード数」
        while q:
            level_size = len(q)
            level_vals: List[int] = []

            for _ in range(level_size):
                node = q.popleft()
                level_vals.append(node.val)
                # 子を enqueue (次のレベル用)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level_vals)

        return result


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
def build_example_tree() -> TreeNode:
    """
    Input: [3, 9, 20, null, null, 15, 7]

            3
           / \
          9   20
              / \
             15   7
    """
    n15 = TreeNode(15)
    n7 = TreeNode(7)
    n20 = TreeNode(20, n15, n7)
    n9 = TreeNode(9)
    return TreeNode(3, n9, n20)


root = build_example_tree()
print(Solution().levelOrder(root))
# → 出力: [[3], [9, 20], [15, 7]]
#   レベル 0: [3] / レベル 1: [9, 20] / レベル 2: [15, 7]


"""
流れ (詳細トレース): root = [3, 9, 20, null, null, 15, 7]

木:
        3
       / \
      9   20
          / \
         15   7

【核心】
  level_size = len(q) は「外ループの先頭で撮るスナップショット」。
  そのレベルのノード数をここで凍結する。for の最中に子 (次レベル) を
  q に追加しても、for は level_size 回しか回らない → いまのレベルだけ
  食べて止まる。追加した子は q に残り、次の外ループへ持ち越される。
  → 「外ループ 1 回 = 1 レベル」を実現する仕掛け。

  記号: q は front(左) → back(右)。 q.popleft() は front から 1 個抜く。

========================================
初期状態
========================================
  q      = [3]
  result = []

========================================
外ループ 1  (Level 0)
========================================
  while q:  → q=[3] は空でない → 入る
  level_size = len(q) = 1      ★このレベルは 1 個に凍結
  level_vals = []
  for _ in range(1):           → 1 回だけ回る

   for 1回目:
     node = q.popleft()   → node=3,  q=[]       (front の 3 が抜けた)
     level_vals.append(3) → level_vals=[3]
     3 の子 9, 20 を append → q=[9, 20]

  result.append([3]) → result = [[3]]

========================================
外ループ 2  (Level 1)
========================================
  while q:  → q=[9, 20] → 入る
  level_size = len(q) = 2      ★このレベルは 2 個に凍結
  level_vals = []
  for _ in range(2):           → 2 回回る

   for 1回目:
     node = q.popleft()   → node=9,  q=[20]
     level_vals=[9]
     9 の子: なし          → q=[20]

   for 2回目:
     node = q.popleft()   → node=20, q=[]
     level_vals=[9, 20]
     20 の子 15, 7 を append → q=[15, 7]

  result.append([9, 20]) → result = [[3], [9, 20]]

  ※ 2回目で 15, 7 を q に足したが、level_size は 2 に凍結済み。
    for はもう回らないので 15, 7 は今回処理されず q に残る。
    → Level 1 に混ざらず、次の外ループ (Level 2) へ持ち越される。

========================================
外ループ 3  (Level 2)
========================================
  while q:  → q=[15, 7] → 入る
  level_size = len(q) = 2
  level_vals = []
  for _ in range(2):           → 2 回回る

   for 1回目:
     node = q.popleft()   → node=15, q=[7]
     level_vals=[15]
     15 の子: なし         → q=[7]

   for 2回目:
     node = q.popleft()   → node=7,  q=[]
     level_vals=[15, 7]
     7 の子: なし          → q=[]

  result.append([15, 7]) → result = [[3], [9, 20], [15, 7]]

========================================
終了
========================================
  while q:  → q=[] (空) → False → ループを抜ける
  return [[3], [9, 20], [15, 7]]   ✓

【2 つの操作の役割】
  level_size = len(q)
      外ループ先頭で「いまのレベルの幅」を固定。これを取らずに毎回
      for _ in range(len(q)) を評価すると、子追加で q が伸びて
      レベルの境界が壊れる (全部 1 レベルに混ざる)。先に凍結 = 仕切り。
  node = q.popleft()
      front から 1 個取り出して node に束ねる (q からは消える)。値を
      level_vals に入れ、子があれば q の後ろへ足す。
      = 「自分を消費しつつ、子を次レベルに予約する」動き。
"""


# ------------------------------------------------------------
# 計算量
# ------------------------------------------------------------
"""
- 時間: O(n)   ※ 各ノードを 1 回ずつ enqueue / dequeue
- 空間: O(w)   ※ w = 木の最大幅 (最も広いレベルのノード数)
                 完全二分木なら w ≒ n/2 = O(n)

ポイント:
1. ループの先頭で `level_size = len(q)` を固定するのが肝。
   → これでそのレベルだけを処理できる (次レベルは別の反復で扱う)。
2. キューは collections.deque を使う。list だと popleft 相当が O(n)。
3. 木は閉路なし → visited 不要。グラフ BFS との違い。
"""
