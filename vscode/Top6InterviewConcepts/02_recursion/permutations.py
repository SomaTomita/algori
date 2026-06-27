"""
Permutations (LeetCode #46)  Medium

重複のない整数配列 nums のすべての順列を返す。

例:
    nums = [1, 2, 3]
    -> [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

順列の数: N! 通り
"""

from typing import List


# ----------------------------------------------------------------------
# 解法 1: 再帰 + 「使用済みフラグ」  ★ 推奨
# ----------------------------------------------------------------------
def permute_with_used(nums: List[int]) -> List[List[int]]:
    """
    各ステップで「まだ使っていない数」から 1 つ選んで current に追加。
    current の長さが N に達したら 1 つの順列が完成。

    時間計算量: O(N * N!)
        - N! 個の順列を生成し、各順列のコピーに O(N)
    空間計算量: O(N)
        - 再帰の深さ N + used 配列 N
        (結果リストのサイズは出力なので別カウント)
    """
    n = len(nums)
    result: List[List[int]] = []
    current: List[int] = []
    used: List[bool] = [False] * n

    def backtrack() -> None:
        # 基底ケース: current が満杯になった
        if len(current) == n:
            result.append(current.copy())   # 必ずコピーを保存
            return

        for i in range(n):
            if used[i]:
                continue

            # 選ぶ
            used[i] = True
            current.append(nums[i])

            # 再帰
            backtrack()

            # 戻す (バックトラック)
            current.pop()
            used[i] = False

    backtrack()
    return result


# ----------------------------------------------------------------------
# 解法 2: 配列を入れ替える方式 (インプレース)
# ----------------------------------------------------------------------
def permute_swap(nums: List[int]) -> List[List[int]]:
    """
    位置 start の要素を、start 以降の各要素と入れ替えながら再帰。
    used 配列を持たずに済むのでメモリ効率が良い。

    時間計算量: O(N * N!)
    空間計算量: O(N)  再帰の深さのみ
    """
    result: List[List[int]] = []
    nums = nums.copy()   # 元の配列を破壊しないために複製
    n = len(nums)

    def backtrack(start: int) -> None:
        if start == n:
            result.append(nums.copy())
            return

        for i in range(start, n):
            nums[start], nums[i] = nums[i], nums[start]   # swap
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]   # swap back

    backtrack(0)
    return result


# ----------------------------------------------------------------------
# どれくらいのサイズで詰むか (実感)
# ----------------------------------------------------------------------
#
# Permutations の出力は N! 個。N の増加に対して爆発的に増える。
#
#   N    | N!              | 体感
#   -----+-----------------+-----------------------
#   5    | 120             | 一瞬
#   8    | 40,320          | 数 ms
#   10   | ~3.6 * 10^6     | 数百 ms
#   12   | ~4.8 * 10^8     | 数十秒
#   15   | ~1.3 * 10^12    | 現実時間で終わらない
#
# LeetCode の制約は N <= 6〜8 程度が多い。
# N が二桁を超えるなら全列挙ではなく別アプローチを疑う。


# ----------------------------------------------------------------------
# 再帰の 3 要素 (解法 1 で確認)
# ----------------------------------------------------------------------
#
# (1) 基底ケース:
#       if len(current) == n:
#           result.append(current.copy())
#           return
#
# (2) 再帰ステップ:
#       backtrack() を呼ぶ前に「選ぶ」処理 (used[i]=True, current.append)
#       これにより「次の階層」では 1 つ選んだ状態から続きを考える
#
# (3) 統合:
#       result というグローバルな箱に貯めていく
#       戻り値ではなく副作用で結果を集めるのは、バックトラック系で典型


# ----------------------------------------------------------------------
# バックトラックの可視化 (nums = [1, 2, 3] の場合)
# ----------------------------------------------------------------------
#
# 各階層で「選ぶ -> 潜る -> 戻す」を繰り返す:
#
# []
# ├── [1]
# │   ├── [1,2]
# │   │   └── [1,2,3] *
# │   └── [1,3]
# │       └── [1,3,2] *
# ├── [2]
# │   ├── [2,1]
# │   │   └── [2,1,3] *
# │   └── [2,3]
# │       └── [2,3,1] *
# └── [3]
#     ├── [3,1]
#     │   └── [3,1,2] *
#     └── [3,2]
#         └── [3,2,1] *
#
# * の地点で result.append される。
# 「選んで潜って戻す」を脳内で再現できれば、再帰 + バックトラックは
# ほとんどの問題で書けるようになる。


# ----------------------------------------------------------------------
# 【コールスタック版】 nums=[1,2,3] を「潜る(呼ぶ)/戻る(return)」で追う
#   generate_strings.py と同じ骨格。違いは「選択肢 = まだ使ってない数」で、
#   used[] フラグで「同じ数の二度使い」を skip する点だけ。
# ----------------------------------------------------------------------
"""
nums=[1,2,3], n=3。current=[] used=[F,F,F] で backtrack(0) を呼ぶところから。
used は [nums[0],nums[1],nums[2]] が使用中かのフラグ。F=未使用 T=使用中。

depth 0: backtrack(0)  current=[] used=[F,F,F]
         len=0 ≠ 3 → for i in 0..2
         ┌─ i=0: used[0]=T, append → current=[1]       ……choose 1
         │  backtrack(1) ───┐  ★潜る
         │                   │
depth 1: │  backtrack(1) ◀──┘  current=[1] used=[T,F,F]
         │  i=0: used[0]=T → skip   ← used の効果（1 を二度使わない）
         │  ┌─ i=1: used[1]=T, append → current=[1,2]  ……choose 2
         │  │  backtrack(2) ───┐  ★潜る
         │  │                   │
depth 2: │  │  backtrack(2) ◀──┘  current=[1,2] used=[T,T,F]
         │  │  i=0 skip, i=1 skip
         │  │  i=2: used[2]=T, append → current=[1,2,3] ……choose 3
         │  │  backtrack(3) ───┐  ★潜る
         │  │                   │
depth 3: │  │  backtrack(3) ◀──┘  current=[1,2,3]
         │  │  len==3 成立！ result に [1,2,3] 記録       ……✓完成
         │  │  return ─────────┐  ★戻る
         │  │                   │
depth 2: │  │  pop 3, used[2]=F ◀┘ → current=[1,2]       ……unchoose 3
         │  │  for 尽きた → return ─┐  ★戻る
         │  │                        │
depth 1: │  pop 2, used[1]=F ◀──────┘ → current=[1]      ……unchoose 2
         │  └─ i=2: used[2]=T, append → current=[1,3]    ……choose 3
         │     backtrack(2) ───┐  ★潜る
         │                      │
depth 2: │     backtrack(2) ◀──┘  current=[1,3] used=[T,F,T]
         │     i=0 skip
         │     i=1: used[1]=T, append → [1,3,2]          ……choose 2
         │     backtrack(3) → [1,3,2] 記録 → return        ……✓完成
         │     pop 2, used[1]=F → current=[1,3]          ……unchoose 2
         │     i=2: used[2]=T → skip
         │     for 尽きた → return
depth 1: │  (backtrack(1) 終了) return ─┐  ★戻る
         │                              │
depth 0: │  pop 1, used[0]=F ◀──────────┘ → current=[]   ……unchoose 1
         │  (i=0 の枝 終わり → [1,2,3],[1,3,2] が出た)
         ├─ i=1: append → current=[2] used=[F,T,F]        ……choose 2
         │   → 同じ形を一段潜って [2,1,3],[2,3,1] を記録 → pop 2 → []
         └─ i=2: append → current=[3] used=[F,F,T]        ……choose 3
             → 同じ形で [3,1,2],[3,2,1] を記録 → pop 3 → []
         for 尽きた → backtrack(0) 終了

→ return result = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

----------------------------------------------------------------
読み方の軸 3 つ:

(1) ★潜る(呼ぶ) と ★戻る(return) は必ずペア。generate_strings と同じ。
    ✓完成 で return → 戻った先で pop(unchoose) という流れも同じ。

(2) generate_strings との唯一の違いは used[]。
    「次に置けるのは まだ使ってない数 だけ」なので、for の頭で
    `if used[i]: continue` で使用中の数を飛ばす。これが順列(N!)を作る要。
    choose で used[i]=True、unchoose で used[i]=False に必ず戻す。

(3) current.append と used[i]=True は1セット、current.pop と used[i]=False も1セット。
    片方だけ戻すと状態がズレて順列が欠ける。
"""


# ----------------------------------------------------------------------
# Permutations vs Subsets (姉妹問題の違い)
# ----------------------------------------------------------------------
#
# どちらもバックトラックで全列挙だが、ルールが違う:
#
#   Subsets       : 「順序を区別しない」「全要素は使わない」 -> 2^N 通り
#                   start を進めることで [1,2] と [2,1] を同一視
#   Permutations  : 「順序を区別する」「全要素を使う」       -> N! 通り
#                   used フラグで「同じ要素の二重使用」だけを禁止
#
# つまり、「過去に使った要素を許すか」が両者を分ける本質的な違い。


# ----------------------------------------------------------------------
# よくある間違い
# ----------------------------------------------------------------------
#
# 1. result.append(current) と書く (コピー忘れ)
#    -> current は共有参照なので、後で current.pop() すると保存済みも変化
#       必ず current.copy() か current[:] でスナップショットを取る
#
# 2. used を戻し忘れる
#    -> 「使用済み」のまま次のループに行ってしまい、順列が欠ける
#       「選ぶ操作」と「戻す操作」は必ずセットで書く
#
# 3. 基底ケースで return を書き忘れる
#    -> その後の for ループに進んでしまい、配列外アクセスや誤動作
#
# 4. swap 版で swap back を忘れる
#    -> 配列が破壊されて以降の順列が壊れる
#       「swap → 再帰 → swap back」の 3 行は 1 セット


# ----------------------------------------------------------------------
# 動作確認
# ----------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], 6),
        ([1], 1),
        ([1, 2], 2),
        ([0, 1, 2, 3], 24),
    ]

    for nums, expected_count in test_cases:
        r1 = permute_with_used(nums)
        r2 = permute_swap(nums)
        ok = (
            len(r1) == len(r2) == expected_count
            and sorted(r1) == sorted(r2)
        )
        status = "OK" if ok else "NG"
        print(f"[{status}] nums={nums}  count={len(r1)} (expected {expected_count})")


# ----------------------------------------------------------------------
# 動きを見るためのトレース版
# ----------------------------------------------------------------------
# permute_with_used と中身は完全に同じ。current / used の状態を毎ステップ print。
def permute_with_used_traced(nums: List[int]) -> List[List[int]]:
    print(f"\n--- nums={nums} ---")
    n = len(nums)
    result: List[List[int]] = []
    current: List[int] = []
    used: List[bool] = [False] * n

    def backtrack(depth: int) -> None:
        indent = "  " * depth

        if len(current) == n:
            print(f"{indent}順列完成 → result に追加: {current}")
            result.append(current.copy())
            return

        for i in range(n):
            if used[i]:
                continue

            used[i] = True
            current.append(nums[i])
            print(f"{indent}nums[{i}]={nums[i]} を選ぶ → current={current}, used={used}")

            backtrack(depth + 1)

            current.pop()
            used[i] = False
            print(f"{indent}nums[{i}]={nums[i]} を戻す → current={current}, used={used}")

    backtrack(0)
    print(f"最終結果: {result}")
    return result


if __name__ == "__main__":
    print("\n========== 動きをトレース ==========")
    permute_with_used_traced([1, 2, 3])
