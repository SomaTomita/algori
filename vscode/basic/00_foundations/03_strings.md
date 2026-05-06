# 文字列 (Strings)

## 文字列 = char の配列 (immutable)

```
s = "hello"

Index :   0    1    2    3    4
Char  :  'h'  'e'  'l'  'l'  'o'
```

ほとんどの言語で文字列は **immutable** (不変)。
書き換えに見えるコードも、内部では **新しい文字列を毎回作成** している。

```
s = "hello"
s += "!"          # 古い "hello" は捨てられ、新しい "hello!" が作られる
```

## O(N²) ループ concat の罠

長さ N の文字列を 1 文字ずつ `+=` で組み立てると、毎回コピーが発生し O(N²)。

### Bad: 文字列を += で結合

```python
result = ""
for c in chars:
    result += c        # 毎回新しい文字列を生成 → O(N^2)
```

```
ループ i: コピーされる文字数
  0  : 0
  1  : 1
  2  : 2
  ...                  → 合計 0+1+...+N = O(N^2)
```

### Good: list に append → join

```python
parts = []
for c in chars:
    parts.append(c)    # O(1)
result = "".join(parts) # 最後にまとめて O(N)
```

実測コードは `examples_string.py` 参照。

## インタビュー頻出パターン

文字列の問題は **sliding window** や **two-pointer** で解けることが多い (後章)。

| パターン            | 例                                       |
| ------------------- | ---------------------------------------- |
| sliding window      | 重複なし最長部分文字列、アナグラム検索   |
| two-pointer         | 回文判定、左右から比較                   |
| ハッシュマップ      | 文字頻度カウント                         |

## いつ使う?

- 文字単位の走査・検索・比較
- パターンマッチ、トークン分割
- 文字列を組み立てるときは **list + join** を使うのが鉄則
