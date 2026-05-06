"""
Big O 体感ベンチマーク
- O(1)        : constant_lookup       (set の in)
- O(log n)    : binary_search_demo    (二分探索)
- O(n)        : single_loop           (1 重ループ)
- O(n log n)  : sort_demo             (組み込みソート)
- O(n^2)      : nested_loop           (二重ループ, n は小さめ)

実行: python3 examples_bigo.py
"""

from __future__ import annotations

import random
from time import perf_counter
from typing import Callable


# --- O(1) ---------------------------------------------------------
def constant_lookup(data: set[int], target: int) -> bool:
    # set の `in` は内部でハッシュ表を引くので、データ量に関係なく一定時間。
    return target in data


# --- O(log n) -----------------------------------------------------
def binary_search_demo(arr: list[int], target: int) -> int:
    # 探索範囲を毎回半分にしていく。N が 10 倍になっても比較回数は ~3.3 増えるだけ。
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1   # mid 以下を捨てて右半分を探す
        else:
            right = mid - 1  # mid 以上を捨てて左半分を探す
    return -1


# --- O(n) ---------------------------------------------------------
def single_loop(arr: list[int]) -> int:
    # 全要素を 1 回ずつ足す。N が 10 倍 → 時間も約 10 倍。
    total = 0
    for x in arr:
        total += x
    return total


# --- O(n log n) ---------------------------------------------------
def sort_demo(arr: list[int]) -> list[int]:
    # Python の sorted は Timsort 実装。比較ベースのソートは下界が O(n log n)。
    return sorted(arr)


# --- O(n^2) -------------------------------------------------------
def nested_loop(arr: list[int]) -> int:
    """全ペア和の最大値 (素朴版).

    二重ループなので比較回数 ~ n*(n-1)/2 = O(n²)。
    N が 10 倍になると時間は約 100 倍に膨らむ。
    """
    best = float("-inf")
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if s > best:
                best = s
    return int(best)


# --- ベンチマーク -------------------------------------------------
def time_call(fn: Callable[[], object]) -> float:
    # fn() を呼んで実行時間 (秒) を返すだけのヘルパ
    start = perf_counter()
    fn()
    return perf_counter() - start


def main() -> None:
    sizes = [1_000, 10_000, 100_000]   # N を 10 倍ずつ増やして比較する

    # ===== ヘッダ行を表示 =====
    print("=" * 78)
    print(
        f"{'N':>8} | {'O(1)':>10} | {'O(log n)':>10} | "
        f"{'O(n)':>10} | {'O(n log n)':>12} | {'O(n^2)':>10}"
    )
    print("-" * 78)

    for n in sizes:
        # 1. テストデータを準備
        arr = list(range(n))
        random.Random(42).shuffle(arr)     # 再現性のため固定 seed でシャッフル
        data_set = set(arr)
        sorted_arr = sorted(arr)

        # 2. それぞれの計算量で同じ N を計測
        t_const = time_call(lambda: constant_lookup(data_set, n - 1))
        t_log = time_call(lambda: binary_search_demo(sorted_arr, n - 1))
        t_lin = time_call(lambda: single_loop(arr))
        t_nlogn = time_call(lambda: sort_demo(arr))

        # O(n^2) は爆発するので n を抑える (N=10^5 なら 10^10 ペア → 数十秒)
        capped = arr[: min(n, 3_000)]
        t_sq = time_call(lambda: nested_loop(capped))
        sq_label = (
            f"{t_sq * 1000:>7.2f} ms"
            if len(capped) == n
            else f"{t_sq * 1000:>6.2f}ms*"  # * は「N をキャップして測った」サイン
        )

        print(
            f"{n:>8} | "
            f"{t_const * 1e6:>7.2f} us | "
            f"{t_log * 1e6:>7.2f} us | "
            f"{t_lin * 1000:>7.3f} ms | "
            f"{t_nlogn * 1000:>9.3f} ms | "
            f"{sq_label:>10}"
        )
        # → 出力例 (時間は環境に依存):
        #     1000 |    0.50 us |    0.79 us |   0.029 ms |     0.171 ms |   85.30 ms*
        #    10000 |    0.50 us |    0.92 us |   0.291 ms |     2.140 ms |  852.40 ms*
        #   100000 |    0.42 us |    1.04 us |   2.910 ms |    24.300 ms |  854.10 ms*
        #
        # 見方:
        #   ・O(1)       行に行ってもほぼ同じ → スケールしない
        #   ・O(n)       N が 10 倍 → 時間も 10 倍
        #   ・O(n^2)     キャップが効いて頭打ちになっている (* 印)

    print("=" * 78)
    print("* = N を 3,000 に制限して計測 (O(n^2) は N=10^5 だと数十秒級)")
    print("ポイント: N を 10x にすると…")
    print("  O(1)       : 変わらない")
    print("  O(log n)   : ほんの少し増える")
    print("  O(n)       : だいたい 10x")
    print("  O(n log n) : 10x よりやや多い")
    print("  O(n^2)     : 100x")
    # → これがそのまま出力される (スケーリング則の暗記用サマリー)


if __name__ == "__main__":
    main()
