"""配列とメモリ基礎: 動かして学ぶサンプル集.

実行:
    python3 examples_array.py
"""

from __future__ import annotations

import sys
import time
from collections import Counter


# ---------------------------------------------------------------------------
# 01_memory_and_ram.md
# ---------------------------------------------------------------------------
def demo_memory_address() -> None:
    # id() はオブジェクトのメモリ上の住所 (整数) を返す関数。
    # 同じ値でも別オブジェクトなら住所は変わる。
    print("== demo_memory_address ==")
    arr = [1, 2, 3, 4, 5]
    print(f"配列のメモリアドレス: {id(arr)}")
    # → 出力例: 配列のメモリアドレス: 4338401024  (実行ごとに数値は変わる)
    print(f"arr[0] のアドレス  : {id(arr[0])}")
    # → 出力例: arr[0] のアドレス  : 4337854768  (整数オブジェクトの場所)
    print(f"arr[1] のアドレス  : {id(arr[1])}")
    # → 出力例: arr[1] のアドレス  : 4337854800
    # ※ Python の小さな整数 (-5〜256) はキャッシュされていて、
    #    別のところで作った 1 や 2 と同じアドレスになることもある。


# ---------------------------------------------------------------------------
# 02_arrays.md - list / array / numpy
# ---------------------------------------------------------------------------
def demo_list_vs_array() -> None:
    # 同じ「[1,2,3,4,5]」でも 3 つの違うコンテナ型で扱える。
    # ・list           : 中身が何でも入る (整数, 文字列, …何でもOK)
    # ・array.array    : 同じ型の数値だけを詰める (省メモリ)
    # ・numpy.ndarray  : 数値演算が高速 (科学計算で定番)
    print("== demo_list_vs_array ==")
    py_list = [1, 2, 3, 4, 5]
    print(f"list      size: {len(py_list)}")
    # → 出力: list      size: 5

    import array

    int_array = array.array("i", [1, 2, 3, 4, 5])
    # "i" は signed int (整数) の意味
    print(f"array     size: {len(int_array)}")
    # → 出力: array     size: 5

    # numpy はオプショナル (未インストールならスキップ)
    try:
        import numpy as np

        np_array = np.array([1, 2, 3, 4, 5])
        print(f"numpy     size: {np_array.size}")
        # → 出力 (numpy あり): numpy     size: 5
    except ImportError:
        print("numpy     size: (numpy 未インストール — スキップ)")
        # → 出力 (numpy なし): numpy     size: (numpy 未インストール — スキップ)


# ---------------------------------------------------------------------------
# 02_arrays.md - 基本操作
# ---------------------------------------------------------------------------
def linear_search(arr: list[int], target: int) -> int:
    # 先頭から順番に target と一致するか見ていくだけ。最大 n 回比較するので O(n)。
    for i, v in enumerate(arr):
        if v == target:
            return i  # 見つかった位置を返す
    return -1  # 最後まで無ければ -1


def demo_array_operations() -> None:
    print("== demo_array_operations ==")
    arr = [1, 2, 3, 4, 5]
    print(f"arr[2]            : {arr[2]}")
    # → 出力: arr[2]            : 3   (インデックス 2 は 0-origin で 3 番目)
    print(f"linear_search(4)  : {linear_search(arr, 4)}")
    # → 出力: linear_search(4)  : 3   (値 4 は arr[3] に存在)

    # ----- ここから arr を順次変えていく。直前の状態を覚えておくのがコツ -----
    arr.append(6)  # 末尾に 6 を追加: [1,2,3,4,5] → [1,2,3,4,5,6]
    print(f"after append(6)   : {arr}")
    # → 出力: after append(6)   : [1, 2, 3, 4, 5, 6]
    arr.insert(2, 10)  # index=2 の位置に 10 を割り込ませる: [1,2,10,3,4,5,6]
    print(f"after insert(2,10): {arr}")
    # → 出力: after insert(2,10): [1, 2, 10, 3, 4, 5, 6]
    arr.pop()  # 末尾を取り除く: [1,2,10,3,4,5,6] → [1,2,10,3,4,5]
    print(f"after pop()       : {arr}")
    # → 出力: after pop()       : [1, 2, 10, 3, 4, 5]
    arr.pop(2)  # index=2 (値 10) を取り除く: [1,2,3,4,5]
    print(f"after pop(2)      : {arr}")
    # → 出力: after pop(2)      : [1, 2, 3, 4, 5]


# ---------------------------------------------------------------------------
# 02_arrays.md - メモリレイアウト & キャッシュ
# ---------------------------------------------------------------------------
def demo_memory_layout() -> None:
    # Python の list は「値そのもの」ではなく「値へのポインタ」を並べて持つ。
    # だから各要素の id() は連続していなくてもよい (中身は別の場所のオブジェクト)。
    print("== demo_memory_layout ==")
    arr = [1, 2, 3, 4, 5]
    for i, v in enumerate(arr):
        print(f"arr[{i}] = {v}, id={id(v)}")
        # → 出力例:
        #     arr[0] = 1, id=4337854768
        #     arr[1] = 2, id=4337854800
        #     arr[2] = 3, id=4337854832
        #     ...   (id の数値は実行ごとに変わる)
    print(f"sys.getsizeof(arr): {sys.getsizeof(arr)} bytes")
    # → 出力例: sys.getsizeof(arr): 104 bytes  (リスト自体のオーバーヘッド込みのサイズ)
    print(f"sys.getsizeof(1)  : {sys.getsizeof(1)} bytes")
    # → 出力例: sys.getsizeof(1)  : 28 bytes   (整数 1 のオブジェクトサイズ)


def demo_cache_efficiency(size: int = 300) -> None:
    """size を小さめにして CI でも高速に走る.

    2 次元配列を「行ごと (row-major)」で読む方が「列ごと (col-major)」で読むより
    速いことを示す。CPU のキャッシュは「連続したメモリ」を一度に取り込むため、
    隣り合う要素にアクセスする方がキャッシュヒット率が上がる。
    """
    print("== demo_cache_efficiency ==")
    # size×size の行列を作る。matrix[i][j] = i*size + j
    matrix = [[i * size + j for j in range(size)] for i in range(size)]

    # ===== 行優先 (row-major): メモリ上で連続したアクセス → 速い =====
    t0 = time.time()
    s = 0
    for i in range(size):  # 外: 行
        for j in range(size):  # 内: 列 (連続して読む)
            s += matrix[i][j]
    row_time = time.time() - t0

    # ===== 列優先 (col-major): 飛び飛びのアクセス → キャッシュミスで遅い =====
    t0 = time.time()
    s = 0
    for j in range(size):  # 外: 列
        for i in range(size):  # 内: 行 (毎回 size 個飛ぶ)
            s += matrix[i][j]
    col_time = time.time() - t0

    print(f"row-major: {row_time:.4f}s")
    # → 出力例: row-major: 0.0089s
    print(f"col-major: {col_time:.4f}s")
    # → 出力例: col-major: 0.0102s
    if row_time > 0:
        print(f"ratio    : {col_time / row_time:.2f}x")
        # → 出力例: ratio    : 1.15x  (col の方が 15% ほど遅い、size を増やすほど差が広がる)


# ---------------------------------------------------------------------------
# 02_arrays.md - 動的配列 / リサイズ
# ---------------------------------------------------------------------------
def demo_dynamic_array(n: int = 12) -> None:
    """list は「容量 > 要素数」になるよう少し余裕を持って確保される。
    サイズが足りなくなると "倍々" のペースで再確保 (resize) が起きる。
    sizeof が階段状に大きくなるのを観察できる。
    """
    print("== demo_dynamic_array ==")
    arr: list[int] = []
    for i in range(n):
        arr.append(i)
        print(f"len={len(arr):2d}  sizeof={sys.getsizeof(arr):3d} bytes")
        # → 出力例 (環境依存):
        #   len= 1  sizeof= 88 bytes  ← ここで容量 4 程度を確保
        #   len= 2  sizeof= 88 bytes
        #   len= 3  sizeof= 88 bytes
        #   len= 4  sizeof= 88 bytes
        #   len= 5  sizeof=120 bytes  ← 容量不足 → 拡張 (バイト数ジャンプ)
        #   len= 6  sizeof=120 bytes
        #   ...
        # 各「ジャンプ」が realloc が発生したタイミング。


def demo_resize_cost(n: int = 10000) -> None:
    """同じ長さの list でも "事前確保 vs 都度 append" でコストが違う。"""
    print("== demo_resize_cost ==")
    arr1 = [0] * n  # 一気に n 個確保 → realloc は 1 回も起きない (速い)
    arr2: list[int] = []
    for i in range(n):  # 都度 append → 内部で何度も realloc が発生する (遅い)
        arr2.append(i)
    print(f"len(arr1)={len(arr1)}, len(arr2)={len(arr2)}")
    # → 出力: len(arr1)=10000, len(arr2)=10000  (見た目は同じ)
    print("どちらも同サイズだが、生成プロセスのコストは異なる")
    # → 出力: どちらも同サイズだが、生成プロセスのコストは異なる


# ---------------------------------------------------------------------------
# 02_arrays.md - LeetCode パターン
# ---------------------------------------------------------------------------
def two_pointers(arr: list[int], target: int) -> list[int]:
    """ソート済み配列で 2 つの和が target になる組を見つける。
    左端と右端から内側へ寄っていく Two Pointers 法。O(n)。
    """
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        # arr=[1,2,3,4,5,6] target=9 のときの動き:
        #   left=0(1), right=5(6) → s=7 < 9 → left を右へ → left=1
        #   left=1(2), right=5(6) → s=8 < 9 → left を右へ → left=2
        #   left=2(3), right=5(6) → s=9 == 9 → 一致! return [2,5]
        if s == target:
            return [left, right]
        if s < target:
            left += 1  # 合計が小さい → 左を大きい値へ動かす
        else:
            right -= 1  # 合計が大きい → 右を小さい値へ動かす
    return [-1, -1]  # 見つからなかった


def demo_two_pointers() -> None:
    print("== demo_two_pointers ==")
    arr = [1, 2, 3, 4, 5, 6]
    print(f"target=9 -> indices {two_pointers(arr, 9)}")
    # → 出力: target=9 -> indices [2, 5]
    #   (arr[2]=3, arr[5]=6, 3+6=9)


def sliding_window_max_sum(arr: list[int], k: int) -> int:
    """長さ k の連続部分配列で最大の合計を返す。
    全部足し直す素朴版は O(n*k) だが、窓を 1 つずつスライドして
    「右端を足す + 左端を抜く」差分更新にすれば O(n)。
    """
    if not arr or k <= 0:
        return 0
    window = sum(arr[:k])  # 最初の窓 (arr[0..k-1]) の合計を作る
    best = window
    # 例: arr=[1,4,2,10,23,3,1,0,20], k=4
    # 初期窓 = [1,4,2,10] → window=17, best=17
    for i in range(k, len(arr)):
        window += arr[i] - arr[i - k]  # 新しい右端を足し、外れた左端を引く
        # i=4: window = 17 + 23 - 1 = 39   窓=[4,2,10,23]    best=39
        # i=5: window = 39 + 3 - 4 = 38   窓=[2,10,23,3]    best=39
        # i=6: window = 38 + 1 - 2 = 37   窓=[10,23,3,1]    best=39
        # i=7: window = 37 + 0 - 10 = 27  窓=[23,3,1,0]     best=39
        # i=8: window = 27 + 20 - 23 = 24 窓=[3,1,0,20]     best=39
        if window > best:
            best = window
    return best


def demo_sliding_window() -> None:
    print("== demo_sliding_window ==")
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    print(f"k=4 max sum -> {sliding_window_max_sum(arr, 4)}")
    # → 出力: k=4 max sum -> 39
    #   (連続 4 要素 [4, 2, 10, 23] の合計が最大)


def rotate_array(arr: list[int], k: int) -> list[int]:
    """配列を右に k 回転させる「3 回 reverse 法」。
    例: [1,2,3,4,5,6,7] を 3 回転 → [5,6,7,1,2,3,4]

    手順 (in-place で空間 O(1)):
      1. 全体を反転                  : [7,6,5,4,3,2,1]
      2. 先頭 k 個を反転            : [5,6,7,4,3,2,1]
      3. 残り n-k 個を反転          : [5,6,7,1,2,3,4]  ← 完成
    """
    n = len(arr)
    if n == 0:
        return arr
    k %= n  # k が n を超えても n の余りだけ意味がある

    def reverse(l: int, r: int) -> None:
        # arr[l..r] を反転 (両端から中央へスワップ)
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    reverse(0, n - 1)  # 全体を反転
    reverse(0, k - 1)  # 先頭 k 個を反転
    reverse(k, n - 1)  # 残りを反転
    return arr


def demo_rotate() -> None:
    print("== demo_rotate ==")
    print(f"rotate by 3 -> {rotate_array([1, 2, 3, 4, 5, 6, 7], 3)}")
    # → 出力: rotate by 3 -> [5, 6, 7, 1, 2, 3, 4]
    #   ([1..7] を 3 回転 → 末尾 3 要素が先頭に来る)


# ---------------------------------------------------------------------------
# 02_arrays.md - 頻度 / Prefix Sum
# ---------------------------------------------------------------------------
def demo_frequency() -> None:
    print("== demo_frequency ==")
    arr = [1, 2, 2, 3, 3, 3, 4]
    # ----- 自前で頻度を数える -----
    # ループの動き:
    #   x=1 → freq={1:1}
    #   x=2 → freq={1:1, 2:1}
    #   x=2 → freq={1:1, 2:2}
    #   x=3 → freq={1:1, 2:2, 3:1}
    #   x=3 → freq={1:1, 2:2, 3:2}
    #   x=3 → freq={1:1, 2:2, 3:3}
    #   x=4 → freq={1:1, 2:2, 3:3, 4:1}
    freq: dict[int, int] = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1  # 未登録キーは 0 扱い → +1
    print(f"manual : {freq}")
    # → 出力: manual : {1: 1, 2: 2, 3: 3, 4: 1}
    print(f"Counter: {dict(Counter(arr))}")
    # → 出力: Counter: {1: 1, 2: 2, 3: 3, 4: 1}   (collections.Counter ならワンライナー)


def build_prefix(arr: list[int]) -> list[int]:
    """累積和 (prefix sum) を作る。pre[i] = arr[0..i-1] の合計。
    pre[0] = 0 を入れておくと、区間和を pre[r+1] - pre[l] で書きやすい。
    """
    pre = [0] * (len(arr) + 1)
    for i, v in enumerate(arr):
        pre[i + 1] = pre[i] + v
    # 例: arr=[1,2,3,4,5]
    #   i=0,v=1: pre=[0,1,0,0,0,0]
    #   i=1,v=2: pre=[0,1,3,0,0,0]
    #   i=2,v=3: pre=[0,1,3,6,0,0]
    #   i=3,v=4: pre=[0,1,3,6,10,0]
    #   i=4,v=5: pre=[0,1,3,6,10,15]
    return pre


def range_sum(prefix: list[int], left: int, right: int) -> int:
    # 区間 [left..right] の和を 1 回の引き算で取得 → O(1)
    return prefix[right + 1] - prefix[left]


def demo_prefix_sum() -> None:
    print("== demo_prefix_sum ==")
    arr = [1, 2, 3, 4, 5]
    pre = build_prefix(arr)
    print(f"prefix={pre}")
    # → 出力: prefix=[0, 1, 3, 6, 10, 15]
    print(f"sum[1..3] = {range_sum(pre, 1, 3)}  (expect 9)")
    # → 出力: sum[1..3] = 9  (expect 9)
    #   (arr[1]+arr[2]+arr[3] = 2+3+4 = 9 を pre[4]-pre[1] = 10-1 = 9 で計算)


# ---------------------------------------------------------------------------
# 02_arrays.md - デバッグ
# ---------------------------------------------------------------------------
def demo_visualize_bubble_sort() -> None:
    """バブルソートを 1 スワップごとに表示する。隣り合う要素を比較して逆順なら入替。"""
    print("== demo_visualize_bubble_sort ==")
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"init  : {arr}")
    # → 出力: init  : [3, 1, 4, 1, 5, 9, 2, 6]
    n = len(arr)
    for i in range(n):  # i = 何周目
        for j in range(n - i - 1):  # 内側: 隣どうしの比較
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"step {i}-{j}: {arr}")
                # → 出力例 (1 周目だけ抜粋):
                #   step 0-0: [1, 3, 4, 1, 5, 9, 2, 6]   (3 と 1 を交換)
                #   step 0-2: [1, 3, 1, 4, 5, 9, 2, 6]   (4 と 1 を交換)
                #   step 0-5: [1, 3, 1, 4, 5, 2, 9, 6]   (9 と 2 を交換)
                #   step 0-6: [1, 3, 1, 4, 5, 2, 6, 9]   (9 と 6 を交換) ← 9 が末尾に確定
    print(f"final : {arr}")
    # → 出力: final : [1, 1, 2, 3, 4, 5, 6, 9]


def find_max(arr: list[int]) -> int | None:
    # 空配列なら None、それ以外は max() で最大値を返す
    return max(arr) if arr else None


def demo_boundary_test() -> None:
    """境界条件テスト: 空配列・単一要素・負数も検証。"""
    print("== demo_boundary_test ==")
    cases: list[tuple[list[int], int | None]] = [
        ([1, 2, 3], 3),
        ([3, 2, 1], 3),
        ([5], 5),
        ([], None),
        ([-1, -2, -3], -1),
    ]
    for i, (data, expected) in enumerate(cases, 1):
        got = find_max(data)
        status = "PASS" if got == expected else "FAIL"
        print(f"case{i}: {status}  in={data}  expect={expected}  got={got}")
        # → 出力:
        #   case1: PASS  in=[1, 2, 3]    expect=3     got=3
        #   case2: PASS  in=[3, 2, 1]    expect=3     got=3
        #   case3: PASS  in=[5]          expect=5     got=5
        #   case4: PASS  in=[]           expect=None  got=None
        #   case5: PASS  in=[-1, -2, -3] expect=-1    got=-1


# ---------------------------------------------------------------------------
# 02_arrays.md - ベストプラクティス
# ---------------------------------------------------------------------------
def demo_inplace_reverse() -> None:
    """その場で配列を反転する小技: ~i は -i-1 と同じ → 末尾から数えるインデックス。"""
    print("== demo_inplace_reverse ==")
    arr = [1, 2, 3, 4, 5]
    # ループの動き:
    #   i=0: arr[0] と arr[~0]=arr[-1] を入替 → [5,2,3,4,1]
    #   i=1: arr[1] と arr[~1]=arr[-2] を入替 → [5,4,3,2,1]
    #   i=2: range(2) で終了 (中央 arr[2] は触らなくて OK)
    for i in range(len(arr) // 2):
        arr[i], arr[~i] = arr[~i], arr[i]
    print(f"in-place reverse -> {arr}")
    # → 出力: in-place reverse -> [5, 4, 3, 2, 1]


def safe_get(arr: list[int], i: int) -> int | None:
    # 範囲外なら None を返す (例外を出さない安全版アクセス)
    return arr[i] if 0 <= i < len(arr) else None


def safe_slice(arr: list[int], start: int, end: int) -> list[int]:
    # 範囲を [0, len(arr)] に丸めてからスライス
    start = max(0, start)
    end = min(len(arr), end)
    return arr[start:end]


def demo_safe_access() -> None:
    print("== demo_safe_access ==")
    arr = [10, 20, 30]
    print(f"safe_get(arr, 1)   = {safe_get(arr, 1)}")
    # → 出力: safe_get(arr, 1)   = 20  (arr[1] が普通に取れる)
    print(f"safe_get(arr, 99)  = {safe_get(arr, 99)}")
    # → 出力: safe_get(arr, 99)  = None  (範囲外なのでクラッシュせず None)
    print(f"safe_slice(-1, 99) = {safe_slice(arr, -1, 99)}")
    # → 出力: safe_slice(-1, 99) = [10, 20, 30]
    #   (-1 → 0, 99 → 3 に丸められて全要素が返る)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main() -> None:
    demos = [
        demo_memory_address,
        demo_list_vs_array,
        demo_array_operations,
        demo_memory_layout,
        demo_cache_efficiency,
        demo_dynamic_array,
        demo_resize_cost,
        demo_two_pointers,
        demo_sliding_window,
        demo_rotate,
        demo_frequency,
        demo_prefix_sum,
        demo_visualize_bubble_sort,
        demo_boundary_test,
        demo_inplace_reverse,
        demo_safe_access,
    ]
    for fn in demos:
        fn()
        print()


if __name__ == "__main__":
    main()
