"""
Vanilla Binary Search
ソート済み配列 nums の中から target を探し、見つかれば index、なければ -1 を返す。

時間 O(log n) / 空間 O(1)

ポイント:
- left <= right (等号必須)
- mid = (left + right) // 2
- 等しければ即 return、それ以外は半分捨てる
"""

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """ソート済み配列から target の index を返す。なければ -1。"""
    left, right = 0, len(nums) - 1

    # 例: nums=[-1,0,2,4,6,8], target=4 の動き
    #   step1: left=0, right=5, mid=2, nums[2]=2 < 4 → left=3
    #   step2: left=3, right=5, mid=4, nums[4]=6 > 4 → right=3
    #   step3: left=3, right=3, mid=3, nums[3]=4 == 4 → return 3 ✓
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1   # mid は target より小さい → 右半分へ
        else:
            right = mid - 1  # mid は target より大きい → 左半分へ

    return -1


def binary_search_traced(nums: List[int], target: int) -> int:
    """各 iteration の left/mid/right を ASCII で図示しながら探索する。"""
    left, right = 0, len(nums) - 1
    step = 0

    print(f"\n  nums = {nums}, target = {target}")
    print(f"  index: {' '.join(f'{i:3d}' for i in range(len(nums)))}")
    print(f"  value: {' '.join(f'{v:3d}' for v in nums)}\n")

    while left <= right:
        step += 1
        mid = (left + right) // 2
        _draw(nums, left, mid, right, step)

        if nums[mid] == target:
            print(f"    -> nums[{mid}] == {target} : FOUND at index {mid}\n")
            return mid
        elif nums[mid] < target:
            print(f"    -> nums[{mid}]={nums[mid]} < {target} : left = mid+1 = {mid + 1}")
            left = mid + 1
        else:
            print(f"    -> nums[{mid}]={nums[mid]} > {target} : right = mid-1 = {mid - 1}")
            right = mid - 1

    print(f"    -> left ({left}) > right ({right}) : NOT FOUND\n")
    return -1


def _draw(nums: List[int], left: int, mid: int, right: int, step: int) -> None:
    """ステップごとに L / M / R を矢印付きで描画する。"""
    n = len(nums)
    line = []
    for i in range(n):
        marks = []
        if i == left:
            marks.append("L")
        if i == mid:
            marks.append("M")
        if i == right:
            marks.append("R")
        line.append(",".join(marks).center(3) if marks else "   ")

    print(f"  step {step}: left={left}, mid={mid}, right={right}")
    print(f"  index: {' '.join(f'{i:3d}' for i in range(n))}")
    print(f"  value: {' '.join(f'{v:3d}' for v in nums)}")
    print(f"  mark : {' '.join(line)}")


if __name__ == "__main__":
    # ケース1: 見つかる
    nums = [-1, 0, 2, 4, 6, 8]
    target = 4
    print("=" * 60)
    print(f"Case 1: search {target} in sorted array")
    print("=" * 60)
    # → 期待される標準出力 (一例):
    #   step 1: left=0, mid=2, right=5
    #   index:   0   1   2   3   4   5
    #   value:  -1   0   2   4   6   8
    #   mark :  L            M             R
    #     -> nums[2]=2 < 4 : left = mid+1 = 3
    #   step 2: left=3, mid=4, right=5
    #     -> nums[4]=6 > 4 : right = mid-1 = 3
    #   step 3: left=3, mid=3, right=3
    #     -> nums[3] == 4 : FOUND at index 3
    result = binary_search_traced(nums, target)
    assert result == 3, f"expected 3, got {result}"

    # ケース2: 見つからない
    print("=" * 60)
    print(f"Case 2: search 3 in sorted array (not present)")
    print("=" * 60)
    result = binary_search_traced(nums, 3)
    assert result == -1, f"expected -1, got {result}"

    # ケース3: 端 (最小)
    print("=" * 60)
    print(f"Case 3: search -1 (leftmost)")
    print("=" * 60)
    result = binary_search_traced(nums, -1)
    assert result == 0

    # ケース4: 端 (最大)
    print("=" * 60)
    print(f"Case 4: search 8 (rightmost)")
    print("=" * 60)
    result = binary_search_traced(nums, 8)
    assert result == 5

    # ケース5: 大きめの配列
    print("=" * 60)
    print(f"Case 5: search 21 in 18-element array")
    print("=" * 60)
    big = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 16, 17, 19, 20, 21, 30, 42]
    result = binary_search_traced(big, 21)
    assert result == 15

    print("All assertions passed.")
    # → すべての assert を通過すれば最後に "All assertions passed." が出る。
    #   途中で失敗した場合は AssertionError でその場で停止する。

# 図解の見方:
#
#   index: 0   1   2   3   4   5
#   value:-1   0   2   4   6   8
#   mark : L           M           R    <- step 1
#   value:-1   0   2   4   6   8
#   mark :             L,M  R           <- step 3 (left == mid)
#                          ^^^
#                          target が mid の右にあれば左を捨てる
#
# 範囲 [L..R] が毎回半分になるので、
# n=18 でも log2(18) ≈ 4.2 → 5 ステップで決着がつく。
