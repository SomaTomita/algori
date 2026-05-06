"""
文字列構築の Bad / Good 比較
- bad : `result += c` で 1 文字ずつ結合 → O(N^2)
- good: list.append → "".join             → O(N)

実行: python3 examples_string.py
"""

from time import perf_counter


def build_with_concat(chars: list[str]) -> str:
    """Bad: O(N^2) - 毎ループで新しい文字列を作る.

    Python の str はイミュータブル (変更不可) なので、`result += c` するたびに
    「今まで作った文字列」をまるごと新しい場所にコピーして 1 文字足す。
    これを N 回繰り返すと総コピー量が 1 + 2 + 3 + … + N = N*(N+1)/2 = O(N²)。
    """
    result = ""
    for c in chars:
        result += c   # ← ここで毎回新しい文字列が作られる (古い result は捨てられる)
    return result


def build_with_join(chars: list[str]) -> str:
    """Good: O(N) - list に詰めて最後に join.

    list.append は平均 O(1)、最後の "".join も O(N) なので合計 O(N)。
    """
    parts: list[str] = []
    for c in chars:
        parts.append(c)
    return "".join(parts)


def measure(label: str, fn, chars: list[str]) -> float:
    # 関数を 1 回呼んで実行時間を返す。出力長が合わなければ assert で警告。
    start = perf_counter()
    out = fn(chars)
    elapsed = perf_counter() - start
    assert len(out) == len(chars), "出力長が入力と一致しません"
    return elapsed


def main() -> None:
    sizes = [1_000, 10_000, 50_000]

    # ===== 表のヘッダー =====
    print("=" * 60)
    print(f"{'N':>8} | {'bad (+=)':>14} | {'good (join)':>14} | {'比率':>8}")
    print("-" * 60)

    for n in sizes:
        chars = ["a"] * n             # "a" を n 個並べた list
        t_bad = measure("bad", build_with_concat, chars)
        t_good = measure("good", build_with_join, chars)
        ratio = t_bad / t_good if t_good > 0 else float("inf")
        print(
            f"{n:>8} | {t_bad * 1000:>11.3f} ms | "
            f"{t_good * 1000:>11.3f} ms | {ratio:>7.1f}x"
        )
        # → 出力例 (時間は環境依存):
        #     1000 |       0.060 ms |       0.050 ms |     1.2x
        #    10000 |       0.770 ms |       0.450 ms |     1.7x
        #    50000 |      18.500 ms |       2.300 ms |     8.0x
        #   ↑ N が 10 倍になるほど bad の方が大きく遅くなっていく (O(N²) の証拠)

    print("=" * 60)
    print("結論: N が大きくなるほど bad は O(N^2) で爆発的に遅くなる")
    # → 出力: 結論: N が大きくなるほど bad は O(N^2) で爆発的に遅くなる


if __name__ == "__main__":
    main()
