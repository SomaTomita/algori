"""
Subsets (LeetCode #78)  Medium

重複のない整数配列 nums の冪集合 (全ての部分集合) を返す。

例:
    nums = [1, 2, 3]
    -> [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
       2^3 = 8 通り

部分集合の数: 2^N 通り
"""

from typing import List


# ----------------------------------------------------------------------
# 解法 1: 再帰 + 「入れる / 入れない」の二択
# ----------------------------------------------------------------------
def subsets_choice(nums: List[int]) -> List[List[int]]:
    """
    各要素について「入れる」「入れない」の 2 択を再帰で全列挙。
    決定木の葉が 2^N 通りの部分集合に対応する。

    時間計算量: O(N * 2^N)   2^N 個の部分集合 × コピー O(N)
    空間計算量: O(N)         再帰の深さ (結果リストは出力扱い)
    """
    result: List[List[int]] = []
    current: List[int] = []
    n = len(nums)

    def backtrack(i: int) -> None:
        if i == n:
            result.append(current.copy())
            return

        # 選択肢 1: nums[i] を入れる
        current.append(nums[i])
        backtrack(i + 1)
        current.pop()

        # 選択肢 2: nums[i] を入れない
        backtrack(i + 1)

    backtrack(0)
    return result


# ----------------------------------------------------------------------
# 解法 2: 再帰 + 「i 以降から追加するものを選ぶ」
# ----------------------------------------------------------------------
def subsets_pick(nums: List[int]) -> List[List[int]]:
    """
    各ステップで「現在の集合を結果に追加 → その後 i 以降から
    1 つ加えて再帰」というスタイル。

    解法 1 との違い:
        解法 1: 決定木の葉 (深さ N の地点) のみを result に入れる
        解法 2: 通過する全ノードを result に入れる
    どちらも 2^N 個になる。

    時間計算量: O(N * 2^N)
    空間計算量: O(N)
    """
    result: List[List[int]] = []
    current: List[int] = []

    def backtrack(start: int) -> None:
        # 通過する全ノードを部分集合として記録
        result.append(current.copy())

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return result


# ----------------------------------------------------------------------
# 解法 3: 反復 (ビットマスク)
# ----------------------------------------------------------------------
def subsets_bitmask(nums: List[int]) -> List[List[int]]:
    """
    2^N 通りのビットパターンを 0..2^N-1 で全列挙。
    各ビットが立っている位置の要素を集める。

    例 N=3, mask=0b101 -> nums[0] と nums[2] を採用 -> [nums[0], nums[2]]

    時間計算量: O(N * 2^N)
    空間計算量: O(1)   再帰スタックを使わない

    再帰が苦手な人には反復のほうが書きやすい。
    """
    n = len(nums)
    result: List[List[int]] = []

    for mask in range(1 << n):   # 1 << n == 2^n
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)

    return result


# ----------------------------------------------------------------------
# どれくらいのサイズで詰むか (実感)
# ----------------------------------------------------------------------
#
# Subsets は出力サイズ自体が 2^N なので、本質的に O(2^N) より速くできない。
# 「どこまでの N が現実的か」だけが問題になる。
#
#   N    | 2^N        | 体感 (現代の PC)
#   -----+------------+-----------------------
#   10   | 1,024      | 一瞬
#   20   | ~10^6      | 数十 ms
#   25   | ~3.3 * 10^7| 数秒
#   30   | ~10^9      | 数十秒〜数分
#   40   | ~10^12     | 現実時間で終わらない
#
# LeetCode の制約は通常 N <= 10〜20 程度。
# それ以上の N では「全列挙したい」というそもそもの設計を疑うサイン。


# ----------------------------------------------------------------------
# 解法 1 の決定木 (nums = [1, 2, 3])
# ----------------------------------------------------------------------
#
#                          []
#                        /    \\
#                  [1]            []           ← 1 を入れる/入れない
#                /     \\        /    \\
#           [1,2]    [1]      [2]      []      ← 2 を入れる/入れない
#           / \\     / \\     / \\     / \\
#       [1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []  ← 3 を入れる/入れない
#
# 葉が 8 個 = 2^3 個 = すべての部分集合。
# 「入れる -> 戻して -> 入れない」がバックトラックの基本動作。


# ----------------------------------------------------------------------
# バックトラックの本質
# ----------------------------------------------------------------------
#
# 「選んで -> 潜って -> 戻す」を再帰で繰り返すと、決定木の全パスを
# 効率良くたどれる。
#
#   current.append(x)   # 選ぶ
#   backtrack(...)      # 潜る
#   current.pop()       # 戻す  ← これを忘れると兄弟枝に汚染が伝わる
#
# Subsets / Permutations / Combinations / Sudoku / N-Queens
# どれも同じ骨格で書ける。


# ----------------------------------------------------------------------
# 【コールスタック版】 解法1 (subsets_choice) で nums=[1,2,3] を追う
#   generate_strings.py と同じ骨格。違いは for ループでなく
#   「入れる を呼ぶ → pop → 入れない を呼ぶ」の2連発で枝分かれする点。
# ----------------------------------------------------------------------
"""
nums=[1,2,3], n=3。current=[] で backtrack(0)。
backtrack(i) は「nums[i] を 入れる / 入れない の2択」。i==n(末尾通過)で1個完成。

depth 0: backtrack(0)  current=[]  i=0
         ┌─ 入れる: append → current=[1]             ……choose 1
         │  backtrack(1) ───┐  ★潜る
         │                   │
depth 1: │  backtrack(1) ◀──┘  current=[1]  i=1
         │  ┌─ 入れる: append → current=[1,2]        ……choose 2
         │  │  backtrack(2) ───┐  ★潜る
         │  │                   │
depth 2: │  │  backtrack(2) ◀──┘  current=[1,2]  i=2
         │  │  ┌─ 入れる: append → current=[1,2,3]   ……choose 3
         │  │  │  backtrack(3) ───┐  ★潜る
         │  │  │                   │
depth 3: │  │  │  backtrack(3) ◀──┘  i==3(末尾)
         │  │  │  result に [1,2,3] 記録 → return ─┐  ★戻る
         │  │  │                                    │
depth 2: │  │  pop 3 ◀──────────────────────────────┘ → [1,2]   ……unchoose 3
         │  │  └─ 入れない: 何も足さず そのまま           ……(3 を入れない)
         │  │     backtrack(3) ───┐  ★潜る (current=[1,2] のまま)
         │  │                      │
depth 3: │  │     backtrack(3) ◀──┘  i==3 → [1,2] 記録 → return
         │  │  (backtrack(2) 終了) return ─┐  ★戻る
         │  │                              │
depth 1: │  pop 2 ◀────────────────────────┘ → [1]   ……unchoose 2
         │  └─ 入れない: そのまま backtrack(2) ───┐  ★潜る (current=[1] のまま)
         │                                        │
depth 2: │     backtrack(2) ◀────────────────────┘  current=[1]  i=2
         │     入れる: append→[1,3]→backtrack(3)→[1,3]記録→pop→[1]
         │     入れない: backtrack(3)→[1] 記録
         │     return
depth 1: │  (backtrack(1) 終了) return ─┐  ★戻る
         │                              │
depth 0: │  pop 1 ◀──────────────────────┘ → []   ……unchoose 1
         │  (入れる側の枝 終わり → [1,2,3],[1,2],[1,3],[1] が出た)
         └─ 入れない: そのまま backtrack(1) ───┐  ★潜る (current=[] のまま)
                                               │
depth 1:    backtrack(1) ◀────────────────────┘  current=[]
            → 同じ形で 2,3 の入れる/入れない → [2,3],[2],[3],[] を記録
         (backtrack(0) 終了)

→ return result = [[1,2,3],[1,2],[1,3],[1],[2,3],[2],[3],[]]   (2^3=8 個)

----------------------------------------------------------------
読み方の軸 3 つ:

(1) 枝分かれが for ループではなく「入れる を呼ぶ → pop → 入れない を呼ぶ」。
    各要素について Yes/No の2本の枝が出る。葉が 2^n 個。

(2) ★重要: 入れる の後の pop で current を元に戻してから 入れない を呼ぶ。
    だから 入れない 側は「nums[i] を足してない」正しい状態で潜れる。
    入れない 側には choose も pop も無い (足してないので戻すものも無い)。

(3) 完成は i==n。「末尾を通過した = 全要素について入れる/入れないを決め終えた」
    の意味。generate_strings の len(path)==n と同じ「もう選ぶものが無い」合図。
"""


# ----------------------------------------------------------------------
# よくある間違い
# ----------------------------------------------------------------------
#
# 1. result.append(current) でコピー忘れ
#    -> current は共有参照。後で current.pop() すると保存済みも変化
#       必ず current.copy() か current[:] でスナップショットを取る
#
# 2. 「入れる」のあとに pop() を忘れる
#    -> 親に戻る前に状態を戻さないと、兄弟枝に汚染が伝わる
#
# 3. 解法 2 で start を毎回 0 から始める
#    -> 同じ部分集合が複数回出る ([1,2] と [2,1] が別物扱いになる)
#       Subsets では順序を区別しないので start を進める
#
# 4. ビットマスク版で 1 << i のビット位置を逆順にする
#    -> 動くが要素の順序が入れ替わる
#       問題で順序を要求されない場合は OK


# ----------------------------------------------------------------------
# 動作確認
# ----------------------------------------------------------------------
if __name__ == "__main__":
    def normalize(subsets: List[List[int]]) -> set[tuple]:
        return {tuple(sorted(s)) for s in subsets}

    test_cases = [
        ([1, 2, 3], 8),
        ([0], 2),
        ([], 1),
        ([1, 2], 4),
    ]

    for nums, expected_count in test_cases:
        r1 = subsets_choice(nums)
        r2 = subsets_pick(nums)
        r3 = subsets_bitmask(nums)
        ok = (
            len(r1) == len(r2) == len(r3) == expected_count
            and normalize(r1) == normalize(r2) == normalize(r3)
        )
        status = "OK" if ok else "NG"
        print(f"[{status}] nums={nums}  count={len(r1)} (expected {expected_count})")
        for s in sorted(r1, key=lambda x: (len(x), x)):
            print(f"      {s}")


# ----------------------------------------------------------------------
# 動きを見るためのトレース版
# ----------------------------------------------------------------------
# subsets_choice と中身は完全に同じ。各ステップで current の状態を print。
# 「include / exclude」の選択をインデントで可視化する。
def subsets_choice_traced(nums: List[int]) -> List[List[int]]:
    print(f"\n--- nums={nums} ---")
    result: List[List[int]] = []
    current: List[int] = []
    n = len(nums)

    def backtrack(i: int, depth: int) -> None:
        indent = "  " * depth
        if i == n:
            print(f"{indent}葉に到達 → result に追加: {current}")
            result.append(current.copy())
            return

        # 選択肢 1: 入れる
        print(f"{indent}i={i}: nums[{i}]={nums[i]} を入れる → current={current + [nums[i]]}")
        current.append(nums[i])
        backtrack(i + 1, depth + 1)
        current.pop()

        # 選択肢 2: 入れない
        print(f"{indent}i={i}: nums[{i}]={nums[i]} を入れない → current={current}")
        backtrack(i + 1, depth + 1)

    backtrack(0, 0)
    print(f"最終結果: {result}")
    return result


if __name__ == "__main__":
    print("\n========== 動きをトレース (decision tree) ==========")
    subsets_choice_traced([1, 2, 3])
