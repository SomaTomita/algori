"""
Maximum Depth of Binary Tree (LeetCode 104)

二分木のルートから一番遠い葉までのノード数を返す。

例:
    root = [3, 9, 20, null, null, 15, 7]

           3
          / \
         9   20
            /  \
           15   7

    → maxDepth = 3  (3 → 20 → 15 / 3 → 20 → 7)


メンタルモデル: "max(left, right) + 1"
----------------------------------------
- 自分の最大深さ = (左部分木の最大深さ と 右部分木の最大深さ の大きい方) + 自分自身 (=1)
- 葉の左右は None (深さ 0) → 葉自身は 0 + 1 = 1
- ベースケース: None なら 0 を返す (まだノードがない高さ 0)

  深さ = "下にあるノード列の最長"
  だから子から戻ってきた値の MAX を取る。
  そこに自分を 1 段ぶん足して上に返す。

これが DFS の基本リズム:
  ① ベースケース で打ち切り
  ② 子を再帰呼び出し
  ③ 子の結果を集約 して 自分の結果を作って返す
"""

from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


# ------------------------------------------------------------
# 解法: 再帰 DFS
# ------------------------------------------------------------
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ベースケース: 空 (None) なら深さ 0
        if root is None:
            return 0
        # 子の深さを再帰で取得
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        # 自分自身の 1 段ぶんを加えて返す
        # 例: 根=3, 左部分木の深さ=1, 右部分木の深さ=2 のとき
        #     return 1 + max(1, 2) = 3
        return 1 + max(left, right)


# ------------------------------------------------------------
# 例題用の木を作る
# ------------------------------------------------------------
def build_example_tree() -> TreeNode:
    """
    [3, 9, 20, null, null, 15, 7] を作る

           3
          / \
         9   20
            /  \
           15   7
    """
    n15 = TreeNode(15)
    n7 = TreeNode(7)
    n20 = TreeNode(20, n15, n7)
    n9 = TreeNode(9)
    n3 = TreeNode(3, n9, n20)
    return n3


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
if __name__ == "__main__":
    root = build_example_tree()
    print("maxDepth =", Solution().maxDepth(root))
    # → 出力: maxDepth = 3
    #   (3 → 20 → 15 または 3 → 20 → 7 の経路長 = 3 ノード)

    # 単一ノード
    print("single node =", Solution().maxDepth(TreeNode(1)))
    # → 出力: single node = 1
    #   (ノード 1 つだけなので深さ 1)

    # 空木
    print("empty tree =", Solution().maxDepth(None))
    # → 出力: empty tree = 0
    #   (None ならベースケースで 0 を返す)


# ------------------------------------------------------------
# 再帰呼び出しツリー (ASCII)
# ------------------------------------------------------------
"""
入力: [3, 9, 20, null, null, 15, 7]

         3
        / \
       9   20
          /  \
         15   7

呼び出しの流れ (DFS は左から潜る):

maxDepth(3)
├── maxDepth(9)              ← 左の子
│   ├── maxDepth(None) → 0   (左の子の左)
│   ├── maxDepth(None) → 0   (左の子の右)
│   └── return 1 + max(0,0) = 1
│
├── maxDepth(20)             ← 右の子
│   ├── maxDepth(15)
│   │   ├── maxDepth(None) → 0
│   │   ├── maxDepth(None) → 0
│   │   └── return 1 + max(0,0) = 1
│   ├── maxDepth(7)
│   │   ├── maxDepth(None) → 0
│   │   ├── maxDepth(None) → 0
│   │   └── return 1 + max(0,0) = 1
│   └── return 1 + max(1,1) = 2
│
└── return 1 + max(1, 2) = 3   ← 答え


スタックの動き (call stack のスナップショット):

時刻 t1: [maxDepth(3), maxDepth(9)]
         9 が None,None を見て 1 を返す → ポップ
時刻 t2: [maxDepth(3), maxDepth(20), maxDepth(15)]
時刻 t3: [maxDepth(3), maxDepth(20), maxDepth(7)]
時刻 t4: [maxDepth(3)]                ← 20 が 2 を返した直後
最終  : [] (3 が 3 を返して終了)

どの時点でも 同時に積まれる関数フレーム数 = 木の高さ h
→ 空間計算量 O(h)


計算量:
- 時間: O(n)  各ノードを 1 回ずつ訪問
- 空間: O(h)  最深時の再帰スタック (バランス木なら O(log n)、偏った木なら O(n))
"""
