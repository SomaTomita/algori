# Hashmaps (ハッシュテーブル)

> キーと値のペアを格納し、平均 O(1) で検索/挿入/削除できるデータ構造。
> Python では組み込みの `dict` / `set` がこれにあたる。

---

## 1. ハッシュテーブルとは

キー (Key) と値 (Value) のペアでデータを管理する「辞書」。
配列の遅い検索 O(n) を、平均 O(1) に短縮する。

```
   key                  bucket (memory slot)
 "banana"  ──hash──▶ 243   ┌────────────┐
                            │ "banana": 5 │   ◀── 値はここに格納
                            └────────────┘
 "apple"   ──hash──▶  17   ┌────────────┐
                            │ "apple": 3  │
                            └────────────┘
```

メールボックスのようなイメージ。各部屋 (bucket) に番号がついていて、
ハッシュ関数が「key → 部屋番号」の地図を一瞬で計算してくれる。

---

## 2. 内部構造

```
key ──▶ hash(key) ──▶ bucket index = hash(key) % 配列サイズ ──▶ 値を保存
```

- **hash function**: 同じキーは常に同じ数値、異なるキーはなるべく違う数値を返す。
- **衝突 (collision)**: 異なるキーが同じインデックスに落ちることがある。
- Python の `dict` は衝突処理 (チェイニング / オープンアドレス) を内部で吸収済み。
  → 利用側は意識しなくてよい。

---

## 3. ハッシュ可能なキー (hashable)

キーは **不変 (immutable)** でなければならない。

|       | OK / NG | 例                  |
| ----- | :-----: | ------------------- |
| int   |    ✓    | `{1: "a"}`          |
| str   |    ✓    | `{"name": "Alice"}` |
| tuple |    ✓    | `{(1, 2): "p"}`     |
| list  |    ✗    | `unhashable type`   |
| dict  |    ✗    | `unhashable type`   |
| set   |    ✗    | `unhashable type`   |

```python
d = {}
d[[1, 2]] = "x"   # TypeError: unhashable type: 'list'
```

---

## 4. 計算量

| 操作   | 平均 | 最悪 (全部衝突) |
| ------ | :--: | :-------------: |
| lookup | O(1) |      O(n)       |
| insert | O(1) |      O(n)       |
| delete | O(1) |      O(n)       |

代わりに空間 O(n) を消費する (時間と空間のトレードオフ)。

---

## 5. 頻度マップ (Frequency Map) パターン

「各要素が何回出現したか」を数える定番パターン。
キー = 要素、値 = 出現回数。

```python
cnt = {}
for item in data:
    cnt[item] = cnt.get(item, 0) + 1
```

詳しくは [`frequency_map.py`](./frequency_map.py) を参照。
`dict.get()` 版 / `defaultdict(int)` 版 / `Counter` 版を比較している。

---

## 6. Two Sum パターン (見たものを記録する)

> 配列の中から、足して target になる 2 つの数のインデックスを返す。

ブルートフォース O(n²) を、ハッシュマップで O(n) に落とす定番テクニック。
「いま見ている数の **相方** (`target - num`) が過去に出たか？」を O(1) で判定する。

```python
seen = {}                       # value → index
for i, num in enumerate(nums):
    if (target - num) in seen:  # 相方が過去にいた
        return [seen[target - num], i]
    seen[num] = i               # いなければ自分を記録
```

詳細なトレース・図解・計算量は [`two_sum.py`](./two_sum.py) を参照。

---

## まとめ

- **強み**: 検索 O(1)、頻度カウント・存在チェック・ペア探索が高速
- **弱み**: 追加メモリ O(n)、キーは hashable 限定、順序保証は実装依存
- **典型問題**: Two Sum / Contains Duplicate / Group Anagrams / Top K Frequent
