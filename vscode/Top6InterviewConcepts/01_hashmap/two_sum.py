"""
Two Sum (LeetCode #1)

整数配列 nums と整数 target が与えられる。
合計が target になる 2 つの要素のインデックスを返す。

例:
    nums = [2, 7, 11, 15], target = 9
    -> [0, 1]   # nums[0] + nums[1] == 2 + 7 == 9

制約:
    - 答えはちょうど 1 組存在する
    - 同じ要素を 2 回使ってはいけない
"""

from typing import List


# ----------------------------------------------------------------------
# 解法 1: ブルートフォース O(N^2)
# ----------------------------------------------------------------------
def two_sum_brute(nums: List[int], target: int) -> List[int]:
    """
    すべてのペアを総当たり。
    時間計算量: O(N^2)
    空間計算量: O(1)
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ----------------------------------------------------------------------
# 解法 2: Hashmap で O(N)
# ----------------------------------------------------------------------
def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
    """
    「target - 現在値」が過去に出てきていれば、その時点でペア成立。
    過去に見た値 -> インデックス を dict に記録しておく。

    時間計算量: O(N)   各要素を 1 回だけ走査
    空間計算量: O(N)   最悪 N 個の要素を dict に格納

    なぜ O(1) で「過去に出たか」を判定できるか:
        dict のキー検索は平均 O(1)。これが Hashmap の本質。
    """
    seen: dict[int, int] = {}  # value -> index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


# ----------------------------------------------------------------------
# どれくらい速くなるか (実感)
# ----------------------------------------------------------------------
#
# 「比較した回数」で比べてみる。
#   - brute   は 2 重ループなので おおよそ N * N 回
#   - hashmap は 1 重ループなので おおよそ N 回
#
#   入力サイズ N   | brute (N^2)        | hashmap (N)   | 体感
#   ---------------+--------------------+---------------+-----------------
#   10             | 100 回              | 10 回          | どっちも一瞬
#   1,000          | 1,000,000 回        | 1,000 回       | brute でも数十ミリ秒
#   100,000        | 10,000,000,000 回   | 100,000 回     | brute は数分 / hashmap は一瞬
#
# ※「10,000,000,000 回」のような巨大ループは、LeetCode などでは
#    制限時間 (大抵 1〜2 秒) を超えてしまい "TLE" (Time Limit Exceeded)
#    と判定される。実務でも実質的に使い物にならないサイズ。
#
# ポイント:
#   Hashmap で「過去に見た値」を O(1) で参照できるおかげで、
#   2 重ループを 1 重ループに畳める。これが面接で頻出する
#   「O(N^2) -> O(N) リダクション」の典型パターン。


# ----------------------------------------------------------------------
# list との比較
# ----------------------------------------------------------------------
#
#   seen_list = [2, 7, 11, 15]
#   if 7 in seen_list:   # O(N) ← 先頭から線形探索
#
#   seen_dict = {2: 0, 7: 1, 11: 2, 15: 3}
#   if 7 in seen_dict:   # O(1) ← ハッシュで一発
#
# これが two_sum を O(N^2) から O(N) に落とす本質。


# ----------------------------------------------------------------------
# よくある間違い
# ----------------------------------------------------------------------
#
# 1. 先に全部 dict に入れてから探す
#    -> 同じ値が複数あると、自分自身とペアを組んでしまう危険がある
#
#       例: nums = [3, 3], target = 6
#       seen = {3: 1} を先に作ってから 3 を探すと、i=0 のときに
#       seen[3]=1 が返ってきて [1, 1] になりかねない
#
#    -> 走査しながら「自分より前に見た値」だけを参照する解法 2 が安全
#
# 2. complement = target - num を「自分自身」と比較してしまう
#    -> seen[num] = i を「比較した後に」書くことで自分自身を参照しない
#       解法 2 のコード順序がそうなっている点に注目


# ----------------------------------------------------------------------
# 動作確認
# ----------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
    ]

    for nums, target, expected in test_cases:
        result_brute = two_sum_brute(nums, target)
        result_hash = two_sum_hashmap(nums, target)
        status = "OK" if result_hash == expected else "NG"
        print(f"[{status}] nums={nums}, target={target}")
        print(f"      brute  -> {result_brute}")
        print(f"      hashmap-> {result_hash}  (expected {expected})")


# ----------------------------------------------------------------------
# 動きを見るためのトレース版
# ----------------------------------------------------------------------
# two_sum_hashmap と中身は完全に同じ。各ステップで print するだけ。
# 実際にどう動くか「目で追える」のがコメントの表より分かりやすい。
def two_sum_hashmap_traced(nums: List[int], target: int) -> List[int]:
    print(f"\n--- nums={nums}, target={target} ---")
    seen: dict[int, int] = {}

    for i, num in enumerate(nums):
        complement = target - num
        print(f"i={i}, num={num}, complement = {target} - {num} = {complement}, seen={seen}")

        if complement in seen:
            print(f"  → complement={complement} は seen にある (index={seen[complement]})")
            print(f"  → return [{seen[complement]}, {i}]")
            return [seen[complement], i]

        print(f"  → complement={complement} は seen に無い。seen[{num}]={i} を登録")
        seen[num] = i

    print("  → 最後まで見つからず return []")
    return []


if __name__ == "__main__":
    print("\n========== 動きをトレース ==========")
    for nums, target, _ in test_cases:
        two_sum_hashmap_traced(nums, target)
