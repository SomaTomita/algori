# LeetCode 準備: 配列と RAM の基礎知識

## 1. メモリ（RAM）の基本概念

### RAM とは何か

- **Random Access Memory**: データを一時的に保存する高速メモリ
- **特徴**: どの位置のデータにも同じ時間でアクセス可能（ランダムアクセス）
- **プログラムとの関係**: 実行中のプログラムとデータが格納される場所

### メモリアドレスの概念

```python
# Pythonでのメモリアドレス確認例
arr = [1, 2, 3, 4, 5]
print(f"配列のメモリアドレス: {id(arr)}")
print(f"最初の要素のアドレス: {id(arr[0])}")
print(f"次の要素のアドレス: {id(arr[1])}")

# 出力例:
# 配列のメモリアドレス: 140234567890128
# 最初の要素のアドレス: 140234567234560
# 次の要素のアドレス: 140234567234592
```

### メモリの階層

1. **CPU キャッシュ**: 最高速（数ナノ秒）
2. **RAM**: 高速（数十ナノ秒）
3. **SSD/HDD**: 低速（ミリ秒）

## 2. 配列（Array）の基本

### 配列とは

- **定義**: 同じ型のデータを連続したメモリ領域に格納するデータ構造
- **インデックス**: 0 から始まる番号で各要素にアクセス
- **固定サイズ**: 一度作成すると基本的にサイズ変更不可（言語によって異なる）

### Python のリスト vs 真の配列

```python
# Pythonのリスト（動的配列）
python_list = [1, 2, 3, 4, 5]
print(f"リストのサイズ: {len(python_list)}")

# 配列ライブラリを使用した真の配列
import array
int_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' = signed int
print(f"配列のサイズ: {len(int_array)}")

# NumPy配列（より配列らしい動作）
import numpy as np
numpy_array = np.array([1, 2, 3, 4, 5])
print(f"NumPy配列のサイズ: {numpy_array.size}")

# 出力例:
# リストのサイズ: 5
# 配列のサイズ: 5
# NumPy配列のサイズ: 5
```

## 3. 配列の基本操作と計算量

### 基本操作の時間計算量

| 操作                | 時間計算量 | 説明                       |
| ------------------- | ---------- | -------------------------- |
| アクセス (読み取り) | O(1)       | インデックスで直接アクセス |
| 検索                | O(n)       | 線形探索が必要             |
| 挿入（末尾）        | O(1)\*     | アモータイズド定数時間     |
| 挿入（任意位置）    | O(n)       | 要素をシフトする必要       |
| 削除（末尾）        | O(1)       | 最後の要素を削除           |
| 削除（任意位置）    | O(n)       | 要素をシフトする必要       |

### 実装例

```python
def array_operations_demo():
    arr = [1, 2, 3, 4, 5]

    # アクセス O(1)
    print(f"インデックス2の要素: {arr[2]}")  # 3

    # 検索 O(n)
    def linear_search(arr, target):
        for i, val in enumerate(arr):
            if val == target:
                return i
        return -1

    index = linear_search(arr, 4)
    print(f"値4のインデックス: {index}")  # 3

    # 挿入（末尾） O(1)
    arr.append(6)
    print(f"末尾追加後: {arr}")  # [1, 2, 3, 4, 5, 6]

    # 挿入（任意位置） O(n)
    arr.insert(2, 10)
    print(f"インデックス2に10挿入: {arr}")  # [1, 2, 10, 3, 4, 5, 6]

    # 削除（末尾） O(1)
    arr.pop()
    print(f"末尾削除後: {arr}")  # [1, 2, 10, 3, 4, 5]

    # 削除（任意位置） O(n)
    arr.pop(2)
    print(f"インデックス2削除後: {arr}")  # [1, 2, 3, 4, 5]

array_operations_demo()

# 出力:
# インデックス2の要素: 3
# 値4のインデックス: 3
# 末尾追加後: [1, 2, 3, 4, 5, 6]
# インデックス2に10挿入: [1, 2, 10, 3, 4, 5, 6]
# 末尾削除後: [1, 2, 10, 3, 4, 5]
# インデックス2削除後: [1, 2, 3, 4, 5]
```

## 4. メモリレイアウトと連続性

### 配列の連続メモリ配置

```python
import sys

def memory_layout_demo():
    # 連続した整数のリスト
    arr = [1, 2, 3, 4, 5]

    print("メモリアドレスの確認:")
    for i, val in enumerate(arr):
        print(f"arr[{i}] = {val}, アドレス: {id(val)}")

    # メモリ使用量の確認
    print(f"\nリスト全体のサイズ: {sys.getsizeof(arr)} bytes")
    print(f"整数1個のサイズ: {sys.getsizeof(1)} bytes")

memory_layout_demo()

# 出力例:
# メモリアドレスの確認:
# arr[0] = 1, アドレス: 140234567234528
# arr[1] = 2, アドレス: 140234567234560
# arr[2] = 3, アドレス: 140234567234592
# arr[3] = 4, アドレス: 140234567234624
# arr[4] = 5, アドレス: 140234567234656
#
# リスト全体のサイズ: 104 bytes
# 整数1個のサイズ: 28 bytes
```

### キャッシュ効率の重要性

```python
import time

def cache_efficiency_demo():
    # 大きな2次元配列を作成
    size = 1000
    matrix = [[i * size + j for j in range(size)] for i in range(size)]

    # 行優先アクセス（キャッシュフレンドリー）
    start = time.time()
    sum_row = 0
    for i in range(size):
        for j in range(size):
            sum_row += matrix[i][j]
    row_time = time.time() - start

    # 列優先アクセス（キャッシュに不利）
    start = time.time()
    sum_col = 0
    for j in range(size):
        for i in range(size):
            sum_col += matrix[i][j]
    col_time = time.time() - start

    print(f"行優先アクセス時間: {row_time:.4f}秒")
    print(f"列優先アクセス時間: {col_time:.4f}秒")
    print(f"比率: {col_time/row_time:.2f}倍")

cache_efficiency_demo()

# 出力例:
# 行優先アクセス時間: 0.1234秒
# 列優先アクセス時間: 0.2156秒
# 比率: 1.75倍
```

## 5. 動的配列 vs 静的配列

### Python リストの内部動作

```python
import sys

def dynamic_array_demo():
    arr = []
    print("動的配列の容量変化:")

    for i in range(20):
        arr.append(i)
        size = sys.getsizeof(arr)
        capacity = len(arr)
        print(f"要素数: {capacity:2d}, メモリサイズ: {size:3d} bytes")

dynamic_array_demo()

# 出力例:
# 動的配列の容量変化:
# 要素数:  1, メモリサイズ:  72 bytes
# 要素数:  2, メモリサイズ:  80 bytes
# 要素数:  3, メモリサイズ:  88 bytes
# 要素数:  4, メモリサイズ:  96 bytes
# 要素数:  5, メモリサイズ: 128 bytes
# 要素数:  6, メモリサイズ: 136 bytes
# 要素数:  7, メモリサイズ: 144 bytes
# 要素数:  8, メモリサイズ: 152 bytes
# 要素数:  9, メモリサイズ: 192 bytes
# 要素数: 10, メモリサイズ: 200 bytes
# 要素数: 11, メモリサイズ: 208 bytes
# 要素数: 12, メモリサイズ: 216 bytes
# 要素数: 13, メモリサイズ: 256 bytes
# 要素数: 14, メモリサイズ: 264 bytes
# 要素数: 15, メモリサイズ: 272 bytes
# 要素数: 16, メモリサイズ: 280 bytes
# 要素数: 17, メモリサイズ: 320 bytes
# 要素数: 18, メモリサイズ: 328 bytes
# 要素数: 19, メモリサイズ: 336 bytes
# 要素数: 20, メモリサイズ: 344 bytes
```

### リサイズのコスト

```python
def resize_cost_demo():
    """リサイズが発生する時のコストを理解する"""

    # 事前にサイズを知っている場合
    known_size = 10000
    arr1 = [0] * known_size  # 事前確保

    # サイズが不明で徐々に追加する場合
    arr2 = []
    for i in range(known_size):
        arr2.append(i)  # 動的にリサイズ

    print("事前確保 vs 動的リサイズの違いを理解することが重要")
    print("LeetCodeでは通常、入力サイズに応じて適切な初期化を行う")
    print(f"arr1のサイズ: {len(arr1)}")
    print(f"arr2のサイズ: {len(arr2)}")
    print("どちらも同じサイズだが、作成プロセスのコストが異なる")

resize_cost_demo()

# 出力:
# 事前確保 vs 動的リサイズの違いを理解することが重要
# LeetCodeでは通常、入力サイズに応じて適切な初期化を行う
# arr1のサイズ: 10000
# arr2のサイズ: 10000
# どちらも同じサイズだが、作成プロセスのコストが異なる
```

## 6. LeetCode 頻出パターン

### 1. Two Pointers（二重ポインタ）

```python
def two_pointers_example(arr, target):
    """
    ソート済み配列で2つの数の和がtargetになるペアを見つける
    時間計算量: O(n), 空間計算量: O(1)
    """
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]

# テスト
sorted_arr = [1, 2, 3, 4, 5, 6]
result = two_pointers_example(sorted_arr, 9)
print(f"Target 9のペア: インデックス {result}")  # [2, 5] (3 + 6 = 9)

# 出力:
# Target 9のペア: インデックス [2, 5]
```

### 2. Sliding Window（スライディングウィンドウ）

```python
def sliding_window_example(arr, k):
    """
    サイズkの窓で最大値を見つける
    時間計算量: O(n), 空間計算量: O(1)
    """
    if not arr or k <= 0:
        return []

    # 最初のウィンドウの合計
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # ウィンドウをスライド
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# テスト
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
result = sliding_window_example(arr, k)
print(f"サイズ{k}のウィンドウの最大合計: {result}")  # 39

# 出力:
# サイズ4のウィンドウの最大合計: 39
```

### 3. 配列の回転

```python
def rotate_array(arr, k):
    """
    配列をk位置右に回転
    時間計算量: O(n), 空間計算量: O(1)
    """
    n = len(arr)
    k = k % n  # kがnより大きい場合の処理

    # 反転を使った効率的な方法
    def reverse(start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # 全体を反転
    reverse(0, n - 1)
    # 最初のk個を反転
    reverse(0, k - 1)
    # 残りを反転
    reverse(k, n - 1)

    return arr

# テスト
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
result = rotate_array(arr.copy(), k)
print(f"3位置右回転: {result}")  # [5, 6, 7, 1, 2, 3, 4]

# 出力:
# 3位置右回転: [5, 6, 7, 1, 2, 3, 4]
```

## 7. 頻出する配列問題のパターン

### パターン 1: 頻度カウント

```python
def frequency_count_pattern(arr):
    """要素の頻度をカウントする基本パターン"""
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Collectionsモジュール使用版
from collections import Counter
def frequency_count_optimized(arr):
    return Counter(arr)

# テスト
arr = [1, 2, 2, 3, 3, 3, 4]
print(f"頻度カウント: {frequency_count_pattern(arr)}")

# 出力:
# 頻度カウント: {1: 1, 2: 2, 3: 3, 4: 1}
```

### パターン 2: プレフィックス和

```python
def prefix_sum_pattern(arr):
    """累積和を使った範囲クエリの効率化"""
    prefix = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]

    return prefix

def range_sum_query(prefix, left, right):
    """O(1)で範囲[left, right]の和を取得"""
    return prefix[right + 1] - prefix[left]

# テスト
arr = [1, 2, 3, 4, 5]
prefix = prefix_sum_pattern(arr)
print(f"範囲[1, 3]の和: {range_sum_query(prefix, 1, 3)}")  # 2+3+4 = 9

# 出力:
# 範囲[1, 3]の和: 9
```

## 8. 実践的なデバッグテクニック

### 配列の可視化

```python
def visualize_array_operations()

# 出力:
# 初期配列: [3, 1, 4, 1, 5, 9, 2, 6]
# インデックス: [0, 1, 2, 3, 4, 5, 6, 7]
# ========================================
# ステップ 0-0: [1, 3, 4, 1, 5, 9, 2, 6]
# ステップ 0-2: [1, 3, 1, 4, 5, 9, 2, 6]
# ステップ 0-5: [1, 3, 1, 4, 5, 2, 9, 6]
# ステップ 0-6: [1, 3, 1, 4, 5, 2, 6, 9]
# ステップ 1-0: [1, 3, 1, 4, 5, 2, 6, 9]
# ステップ 1-2: [1, 1, 3, 4, 5, 2, 6, 9]
# ステップ 1-4: [1, 1, 3, 4, 2, 5, 6, 9]
# ステップ 1-5: [1, 1, 3, 4, 2, 5, 6, 9]
# ステップ 2-1: [1, 1, 3, 4, 2, 5, 6, 9]
# ステップ 2-3: [1, 1, 3, 2, 4, 5, 6, 9]
# ステップ 3-2: [1, 1, 2, 3, 4, 5, 6, 9]
# ========================================
# 最終結果: [1, 1, 2, 3, 4, 5, 6, 9]:
    """配列操作の可視化デバッグ"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6]

    print("初期配列:", arr)
    print("インデックス:", list(range(len(arr))))
    print("=" * 40)

    # バブルソートの可視化例
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(f"ステップ {i}-{j}: {arr}")

    print("=" * 40)
    print("最終結果:", arr)

visualize_array_operations()
```

### 境界値テスト

```python
def boundary_test_template(func, test_cases):
    """境界値テストのテンプレート"""
    for i, (input_data, expected) in enumerate(test_cases):
        result = func(input_data)
        status = "PASS" if result == expected else "FAIL"
        print(f"テスト{i+1}: {status} - 入力:{input_data}, 期待:{expected}, 結果:{result}")

# 例: 最大値を見つける関数のテスト
def find_max(arr):
    return max(arr) if arr else None

test_cases = [
    ([1, 2, 3], 3),        # 通常ケース
    ([3, 2, 1], 3),        # 逆順
    ([5], 5),              # 単一要素
    ([], None),            # 空配列
    ([-1, -2, -3], -1),    # 負の数
]

boundary_test_template(find_max, test_cases)

# 出力:
# テスト1: PASS - 入力:[1, 2, 3], 期待:3, 結果:3
# テスト2: PASS - 入力:[3, 2, 1], 期待:3, 結果:3
# テスト3: PASS - 入力:[5], 期待:5, 結果:5
# テスト4: PASS - 入力:[], 期待:None, 結果:None
# テスト5: PASS - 入力:[-1, -2, -3], 期待:-1, 結果:-1
```

## 9. 重要な注意点とベストプラクティス

### メモリ効率の考慮

```python
# 良い例: 必要最小限のメモリ使用
def memory_efficient_solution(arr):
    # インプレース操作を活用
    for i in range(len(arr) // 2):
        arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    return arr

# 避けるべき例: 不要な追加メモリ使用
def memory_inefficient_solution(arr):
    # 新しい配列を作成（追加O(n)メモリ）
    return arr[::-1]
```

### インデックス範囲エラーの防止

```python
def safe_array_access(arr, index):
    """安全な配列アクセスのパターン"""
    if 0 <= index < len(arr):
        return arr[index]
    else:
        return None  # またはデフォルト値

def safe_range_operation(arr, start, end):
    """安全な範囲操作"""
    start = max(0, start)
    end = min(len(arr), end)
    return arr[start:end]
```

## まとめ

配列と RAM の理解は、効率的なアルゴリズム設計の基盤です。以下の点を常に意識してください：

- **時間計算量**: O(1)アクセス、O(n)探索を理解
- **空間計算量**: メモリ使用量を意識した設計
- **キャッシュ効率**: 連続アクセスパターンの重要性
- **境界条件**: 空配列、単一要素、インデックス範囲
- **インプレース操作**: 追加メモリを使わない解法の検討

これらの基礎をしっかり身につけることで、LeetCode の配列問題により効果的に取り組むことができます。
