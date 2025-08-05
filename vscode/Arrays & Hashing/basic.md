# 1. メモリ（RAM）の基本概念

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

# 2. 配列（Array）の基本

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

# 3. ハッシュテーブルの基本概念

## 1. ハッシュテーブルの基本概念

### ハッシュテーブルとは何か

- **定義**: キー（Key）と値（Value）のペアを格納するデータ構造。連想配列や辞書、ハッシュマップとも呼ばれる。
- **目的**: 配列の O(n)かかる検索を、平均的に O(1)という非常に高速な時間計算量で行うこと。
- **キーの特徴**: 各キーは一意（ユニーク）でなければならない。

### ハッシュ関数とハッシュ値

ハッシュテーブルの高速なアクセスの裏側では「ハッシュ関数」が働いています。

- **ハッシュ関数**: キーを受け取り、配列のインデックスとして使える数値（ハッシュ値またはハッシュコード）を生成する関数。
- **理想的なハッシュ関数**:
  1.  同じキーからは常に同じハッシュ値を生成する。
  2.  異なるキーからは、できるだけ異なるハッシュ値を生成する（衝突を避ける）。
  3.  高速に計算できる。

```python
# Pythonでのハッシュ値確認例
key1 = "apple"
key2 = "world"
key3 = 100

# hash()関数でどのような数値に変換されるかを確認
print(f"キー'{key1}'のハッシュ値: {hash(key1)}")
print(f"キー'{key2}'のハッシュ値: {hash(key2)}")
print(f"キー'{key3}'のハッシュ値: {hash(key3)}")

# 出力例 (環境によって値は変わります):
# キー'apple'のハッシュ値: -156923321308428335
# キー'world'のハッシュ値: 4689537929841834994
# キー'100'のハッシュ値: 100
```

## 2. ハッシュテーブルの内部構造

ハッシュテーブルは、内部的には「**配列**」と「**ハッシュ関数**」を組み合わせて作られています。

1.  **キーをハッシュ関数に入れる**: `hash("apple")` -> `-1569...`
2.  **ハッシュ値を配列のサイズで割った余りを求める**: `-1569... % 配列サイズ` -> `インデックス 5`
3.  **計算されたインデックスに値を格納**: 内部配列の 5 番目の位置に、"apple"の値を保存する。

この仕組みにより、キーさえ分かれば、値を保存すべき（あるいは値が保存されている）配列のインデックスが一発で計算できるため、高速なアクセスが実現します。

## 3. ハッシュ衝突（Collision）

### ハッシュ衝突とは

- **定義**: 異なるキーから、ハッシュ関数が同じインデックス（ハッシュ値）を生成してしまうこと。
- **例**: `hash("key1") % 10` -> `3`、`hash("key2") % 10` -> `3`
- **問題点**: 配列の同じ場所に複数の値を保存する必要が生じる。

### 衝突の解決策: チェイニング法

最も一般的な解決策が「チェイニング（連鎖法）」です。

- **方法**: ハッシュテーブルの内部配列の各要素を、単なる値ではなく**連結リスト**や**動的配列**にする。
- **動作**:
  1.  衝突が発生したら、同じインデックスの連結リストに新しいキーと値のペアを追加する。
  2.  データを検索する際は、まずインデックスを計算し、そのインデックスにある連結リストを線形探索して目的のキーを見つける。

```python
# チェイニングの概念を簡易的に表現したコード
# 内部配列のサイズを5とする
hash_table = [[] for _ in range(5)]
# 空のリストの配列（[[], [], [], [], []]）

def simple_hash(key, size):
    return len(key) % size # 文字列の長さでハッシュ値を決める簡易的な関数

# データ挿入
keys = ["apple", "banana", "grape", "orange", "mango"]
for key in keys:
    index = simple_hash(key, 5)
    print(f"'{key}' (長さ:{len(key)}) -> index: {index}")
    hash_table[index].append(key) # 衝突を許容してリストに追加

print("\nハッシュテーブルの内部状態:")
for i, bucket in enumerate(hash_table):
    print(f"Index {i}: {bucket}")

# 出力:
# 'apple' (長さ:5) -> index: 0
# 'banana' (長さ:6) -> index: 1
# 'grape' (長さ:5) -> index: 0  <-- "apple"と衝突！
# 'orange' (長さ:6) -> index: 1 <-- "banana"と衝突！
# 'mango' (長さ:5) -> index: 0  <-- "apple", "grape"と衝突！
#
# ハッシュテーブルの内部状態:
# Index 0: ['apple', 'grape', 'mango']
# Index 1: ['banana', 'orange']
# Index 2: []
# Index 3: []
# Index 4: []
```

## 4. ハッシュテーブルの基本操作と計算量

### 基本操作の時間計算量

| 操作     | 平均計算量 | 最悪計算量 | 説明                                                       |
| :------- | :--------- | :--------- | :--------------------------------------------------------- |
| アクセス | O(1)       | O(n)       | キーからインデックスを計算。最悪は全データが衝突した場合。 |
| 検索     | O(1)       | O(n)       | アクセスと同様。                                           |
| 挿入     | O(1)       | O(n)       | アクセスと同様。                                           |
| 削除     | O(1)       | O(n)       | アクセスと同様。                                           |

**なぜ最悪計算量が O(n)なのか？**

- 全てのキーがハッシュ衝突を起こし、内部配列の一つのインデックスに全データが連結リストとして格納された場合、そのリストを最初から最後まで探索する必要があるためです。
- 優れたハッシュ関数と適切なサイズ管理により、この最悪のケースは実用上ほとんど起こりません。

### 実装例 (Python の辞書を使用)

```python
def dict_operations_demo():
    # 挿入 O(1)
    user_ages = {}
    user_ages["alice"] = 30
    user_ages["bob"] = 25
    user_ages["charlie"] = 35
    print(f"挿入後: {user_ages}")

    # アクセス O(1)
    print(f"aliceの年齢: {user_ages['alice']}")

    # 検索 (キーの存在確認) O(1)
    if "bob" in user_ages:
        print("bobは存在します。")

    # 安全なアクセス (getメソッド) O(1)
    # キーが存在しなくてもエラーにならない
    dave_age = user_ages.get("dave", "不明")
    print(f"daveの年齢: {dave_age}")

    # 削除 O(1)
    del user_ages["charlie"]
    print(f"削除後: {user_ages}")

dict_operations_demo()

# 出力:
# 挿入後: {'alice': 30, 'bob': 25, 'charlie': 35}
# aliceの年齢: 30
# bobは存在します。
# daveの年齢: 不明
# 削除後: {'alice': 30, 'bob': 25}
```

## 5. Python の`dict`と`set`

### `dict` (辞書)

- Python に標準で組み込まれている、非常に高度に最適化されたハッシュテーブルです。
- キーと値のペアを扱うほとんどの場面で、`dict`を使えば問題ありません。

### `set` (集合)

- `set`も内部的にはハッシュテーブルで実装されています。
- `dict`との違いは、**値（Value）を持たず、キー（Key）だけを格納する**点です。
- そのため、**要素の重複を許さず、ある要素が存在するかどうかの確認**を O(1)で行いたい場合に最適です。

```python
# setを使った重複チェック
numbers = [1, 1, 2, 5, 8, 9, 9]
unique_numbers = set(numbers)

print(f"元のリスト: {numbers}")
print(f"重複を除いた集合: {unique_numbers}")

# 存在確認
if 5 in unique_numbers:
    print("5は集合の中に存在します。")

# 出力:
# 元のリスト:
# 重複を除いた集合: {1, 2, 5, 8, 9}
# 5は集合の中に存在します。
```

## 6. LeetCode 頻出パターン

### 1. 頻度カウント

- **問題**: 配列や文字列の中に、各要素が何回出現するかを数える。
- **解法**: ハッシュマップを使い、`キー`に要素、`値`に出現回数を格納する。

```python
from collections import Counter

def frequency_count_pattern(s: str):
    # 方法1: dict.get() を使う
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # 方法2: collections.Counter を使う (よりPythonic)
    # freq_optimized = Counter(s)

    return freq

# テスト
text = "hello world"
print(f"'{text}'の文字頻度: {frequency_count_pattern(text)}")

# 出力:
# 'hello world'の文字頻度: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
```

### 2. 見たものを記録する (Two Sum パターン)

- **問題**: 2 つの要素の合計が target になるような インデックスのペア を見つけたい。
  (`target - x` のように、今処理している要素の「相方」が過去に出現したかどうかを高速に知りたい。)
- **解法**: ハッシュマップを使い、`キー`に数値、`値`にそのインデックスを格納していく。ループの各ステップで、「相方」がマップに存在するかを O(1)でチェックする。

```python
def two_sum_pattern(nums, target):
    """
    numsの中から、足してtargetになる2つの数のインデックスを返す
    時間計算量: O(n), 空間計算量: O(n)
    """
    seen = {} # {値: インデックス}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# テスト
arr = [2, 7, 11, 15]
target = 9
result = two_sum_pattern(arr, target)
print(f"合計が{target}になるペアのインデックス: {result}")
# 出力:
# 合計が9になるペアのインデックス: [0, 1]

# 流れ:
# seen = {}
# i=0, num=2 → complement = 7 → seenにない → seen = {2: 0}
# i=1, num=7 → complement = 2 → seenにある！→ return [0, 1]


# テスト2
arr = [3, 1, 5, 7, 5, 9]
target = 10
result = two_sum_pattern(arr, target)
print(f"合計が{target}になるペアのインデックス: {result}")
# 出力:
# 合計が10になるペアのインデックス: [0, 3]

# 流れ:
# seen = {}
# i=0, num=3 → complement = 7 → seenに7はない → seen = {3: 0}
# i=1, num=1 → complement = 9 → seenに9はない → seen = {3: 0, 1: 1}
# i=2, num=5 → complement = 5 → seenに5はない → seen = {3: 0, 1: 1, 5: 2}
# i=3, num=7 → complement = 3 → seenに3がある！→ return [0, 3]
#  ※ 5番目のインデックスまで見る前に return される（最初に見つかったペアを返す）
```

### 3. 重複の検出

- **問題**: 配列内に重複した要素があるかどうかを判定する。
- **解法**: `set`の性質（重複を許さない）を利用する。配列を`set`に変換し、元の配列とサイズを比較する。

```python
def contains_duplicate_pattern(nums):
    """
    リストの長さとセットの長さが違えば、重複がある
    時間計算量: O(n), 空間計算量: O(n)
    """
    return len(nums) != len(set(nums))

# テスト
arr1 =
arr2 =
print(f"{arr1}に重複はありますか？ -> {contains_duplicate_pattern(arr1)}")
print(f"{arr2}に重複はありますか？ -> {contains_duplicate_pattern(arr2)}")

# 出力:
#に重複はありますか？ -> True
#に重複はありますか？ -> False
```

## 7. 重要な注意点とベストプラクティス

### キーは不変（Immutable）である必要がある

- `dict`や`set`のキーには、文字列、数値、タプルのような「不変（イミュータブル）」なオブジェクトしか使えません。
- リストや辞書のような「可変（ミュータブル）」なオブジェクトをキーにしようとするとエラーになります。

```python
# 正常な例
my_dict = {}
my_dict["name"] = "Alice"  # stringはOK
my_dict = "Score"     # integerはOK
my_dict[(1, 2)] = "Tuple"  # tupleはOK

# エラーになる例
try:
    my_dict[] = "List" # listはNG
except TypeError as e:
    print(f"エラー: {e}")
# 出力:
# エラー: unhashable type: 'list'
```

### `get()`メソッドの活用

キーが存在しない場合に`KeyError`を発生させる`[]`記法よりも、`get()`メソッドを使う方が安全な場合があります。`get()`はキーが存在しない場合に`None`または指定したデフォルト値を返します。

### 空間と時間のトレードオフ

ハッシュテーブルは、**追加のメモリ空間（空間計算量）を O(n)使う**代わりに、**検索・挿入・削除の時間を O(1)に短縮**するデータ構造です。この「空間を使って時間を買う」というトレードオフは、アルゴリズム設計において非常に重要な概念です。

## まとめ

ハッシュテーブルは、配列の弱点である「検索の遅さ」を克服する強力なデータ構造です。

- **キーと値**のペアでデータを管理。
- **O(1)の高速なアクセス**が最大の強み。
- **追加のメモリ（空間計算量）**が必要になる。
- LeetCode では**頻度カウント、存在チェック、過去のデータの記録**など、非常に多くの問題で活用できる。

ハッシュテーブルを使いこなすことが、コーディング問題を効率的に解くための鍵となります。
