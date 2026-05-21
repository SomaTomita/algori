"""
Contains Duplicate (LeetCode #217)  Easy

整数配列 nums の中に重複する値が 1 つでもあれば True、無ければ False を返す。

例:
    nums = [1, 2, 3, 1] -> True
    nums = [1, 2, 3, 4] -> False

制約:
    - 答えは True / False のどちらか
    - 「同じ値が 2 回以上現れるか?」だけが知りたい (どの index かは不要)
"""

from typing import List


# ----------------------------------------------------------------------
# 解法 1: ブルートフォース O(N^2)
# ----------------------------------------------------------------------
def contains_duplicate_brute(nums: List[int]) -> bool:
    """
    全ペアを比較。
    時間計算量: O(N^2)
    空間計算量: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# ----------------------------------------------------------------------
# 解法 2: ソート O(N log N)
# ----------------------------------------------------------------------
def contains_duplicate_sort(nums: List[int]) -> bool:
    """
    ソートしてから隣同士を比較。同じ値があれば必ず隣接する。
    時間計算量: O(N log N)
    空間計算量: O(N)  ※ sorted は新しいリストを作る
                       元配列を破壊して良いなら nums.sort() で O(1)
    """
    s = sorted(nums)
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            return True
    return False


# ----------------------------------------------------------------------
# 解法 3: Hashmap (set) で O(N)   ★ 推奨
# ----------------------------------------------------------------------
def contains_duplicate_set(nums: List[int]) -> bool:
    """
    走査しながら set に追加。既に入っていればその瞬間 True。
    時間計算量: O(N)   各要素を 1 回ずつ見るだけ
    空間計算量: O(N)   最悪 N 個を set に保持

    なぜ O(1) で「過去に出たか」を判定できるか:
        set の `in` 判定は平均 O(1)。これが Hashmap の本質。
    """
    seen: set[int] = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False


# ----------------------------------------------------------------------
# 解法 4: ワンライナー (実務向け)
# ----------------------------------------------------------------------
def contains_duplicate_oneliner(nums: List[int]) -> bool:
    """
    set にすると重複が消えるので、長さが減れば重複がある。
    中身は解法 3 と同じ O(N)。
    面接では「中で何が起きているか」を説明できないと評価が下がる。
    """
    return len(set(nums)) != len(nums)


# ----------------------------------------------------------------------
# どれくらい速くなるか (実感)
# ----------------------------------------------------------------------
#
# 「比較した回数」で比べてみる。
#   - brute は 2 重ループなので おおよそ N * N 回
#   - sort  は O(N log N)。Python の Timsort は実測でとても速い
#   - set   は 1 重ループなので おおよそ N 回
#
#   入力サイズ N   | brute (N^2)       | sort (N log N) | set (N)        | 体感
#   ---------------+-------------------+----------------+----------------+--------------
#   10             | 100 回             | ~30 回          | 10 回           | どれも一瞬
#   1,000          | 1,000,000 回       | ~10,000 回      | 1,000 回        | brute も数十 ms
#   100,000        | 10,000,000,000 回  | ~1,700,000 回   | 100,000 回      | brute は数分 / set は一瞬
#
# ※ N=100,000 で brute は 10^10 回ループするので LeetCode では確実に
#    TLE (Time Limit Exceeded)。実務でも使い物にならない。
#
# ポイント:
#   「重複の有無」は Hashmap (set) の最も典型的な用途。
#   O(N^2) -> O(N) リダクションは hashmap で「過去に見た」を
#   O(1) 参照できるからこそ実現できる。


# ----------------------------------------------------------------------
# set と list の比較 (なぜ set なのか)
# ----------------------------------------------------------------------
#
#   seen_list = [1, 2, 3]
#   if 2 in seen_list:   # O(N) ← 先頭から線形探索
#
#   seen_set = {1, 2, 3}
#   if 2 in seen_set:    # O(1) ← ハッシュで一発
#
# 「過去に見た値の存在チェック」だけが欲しい時は set が最強。
# 値からインデックスを引きたい時は dict (= two_sum パターン)。


# ----------------------------------------------------------------------
# よくある間違い
# ----------------------------------------------------------------------
#
# 1. ソートのコストを忘れる
#    -> 解法 2 を「O(N) でできた」と説明する人が稀にいる。
#       sorted() は O(N log N)。これがボトルネックになる。
#       なぜ N log N か: 「半分にしながらマージ」を log N 階層、
#         各階層で N 要素触る → N × log N。
#       なぜボトルネックか: 全体の計算量 = 一番遅いステップなので、
#         O(N log N) + O(N) ループ = O(N log N) に支配される。
#       set は「順序を作る」必要がなく「存在チェック」だけなので O(N) で済む。
#
# 2. dict と set を混同する
#    -> 「値の存在チェックだけ」なら set。
#       「値 -> 何か」を覚えるなら dict。
#       両者は同じハッシュ機構の上に乗っているが API が違う。


# ----------------------------------------------------------------------
# 動作確認
# ----------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([1], False),
    ]

    for nums, expected in test_cases:
        r1 = contains_duplicate_brute(nums)
        r2 = contains_duplicate_sort(nums)
        r3 = contains_duplicate_set(nums)
        r4 = contains_duplicate_oneliner(nums)
        ok = r1 == r2 == r3 == r4 == expected
        status = "OK" if ok else "NG"
        print(f"[{status}] nums={nums} -> {r3}  (expected {expected})")


# ----------------------------------------------------------------------
# 動きを見るためのトレース版
# ----------------------------------------------------------------------
# contains_duplicate_set と中身は完全に同じ。各ステップで print するだけ。
def contains_duplicate_set_traced(nums: List[int]) -> bool:
    print(f"\n--- nums={nums} ---")
    seen: set[int] = set()

    for i, x in enumerate(nums):
        print(f"i={i}, x={x}, seen={seen}")

        if x in seen:
            print(f"  → x={x} は seen にある → return True")
            return True

        print(f"  → x={x} は seen に無い。seen に追加")
        seen.add(x)

    print("  → 最後まで重複なし → return False")
    return False


if __name__ == "__main__":
    print("\n========== 動きをトレース ==========")
    for nums, _ in test_cases:
        contains_duplicate_set_traced(nums)
