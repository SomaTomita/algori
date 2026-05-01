# Merge Strings Alternately
# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.


# Example 1:
# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:
# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:
# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q
# merged: a p b q c   d


# Constraints:
# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0

        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            i += 1
            res.append(word2[j])
            j += 1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)


print(Solution().mergeAlternately("abc", "pqr"))

# 流れ:
# i, j = 0
# len(words1) = 3, len(words2) = 3
# i < len(words1) → 0 < 3 | j < len(words2) → 0 < 3 ---> True
# res = ['a']
# res = ['a', 'p']
# i < len(words1) → 1 < 3 | j < len(words2) → 1 < 3 ---> True
# res = ['a', 'p', 'b']
# res = ['a', 'p', 'b', 'q']
# i < len(words1) → 2 < 3 | j < len(words2) → 2 < 3 ---> True
# res = ['a', 'p', 'b', 'q', 'c']
# i < len(words1) → 3 < 3 | j < len(words2) → 3 < 3 ---> False
# res = ['a', 'p', 'b', 'q', 'c', 'r']

print(Solution().mergeAlternately("ab", "pqrs"))

# 流れ:
# # i, j = 0
# len(words1) = 2, len(words2) = 4
# i < len(words1) → 0 < 2 | j < len(words2) → 0 < 4 ---> True
# res = ['a']
# res = ['a', 'p']
# i < len(words1) → 1 < 2 | j < len(words2) → 1 < 4 ---> True
# res = ['a', 'p', 'b']
# res = ['a', 'p', 'b', 'q']
# i < len(words1) → 2 < 2 | j < len(words2) → 2 < 4 ---> False
# res.append(word2[j:]) # 残りのindex j (2)から最後までを追加
# res = ['a', 'p', 'b', 'q', 'r', 's']


# ------------------------------------------------------------
# ------------------------------------------------------------

# python基礎

# 文字列のスライス
text = "hello world"
print(text[6:])  # "world" - インデックス6から最後まで
print(text[0:])  # "hello world" - 最初から最後まで（全体）
print(text[3:])  # "lo world" - インデックス3から最後まで

# リストのスライス
numbers = [1, 2, 3, 4, 5]
print(numbers[2:])  # [3, 4, 5] - インデックス2から最後まで
print(numbers[0:])  # [1, 2, 3, 4, 5] - 全体
print(numbers[4:])  # [5] - インデックス4から最後まで

# その他のスライス
text = "python"
print(text[:3])  # "pyt" - 最初からインデックス3未満まで
print(text[2:5])  # "tho" - インデックス2からインデックス5未満まで
print(text[::2])  # "pto" - 2つおきに取得
print(text[::-1])  # "nohtyp" - 逆順


# ------------------------------------------------------------
# 図で見るマージ過程
# ------------------------------------------------------------
"""
Example 1: word1 = "abc", word2 = "pqr"

word1: │ a │ b │ c │       i = 0 → 1 → 2 → 3 (出口)
word2: │ p │ q │ r │       j = 0 → 1 → 2 → 3 (出口)

ループ内 (i, j を交互に消費):
  i=0,j=0  → res = [a]            → res = [a, p]    → i=1, j=1
  i=1,j=1  → res = [a, p, b]      → res = [a, p, b, q]  → i=2, j=2
  i=2,j=2  → res = [a, p, b, q, c] → res = [a, p, b, q, c, r] → i=3, j=3

ループ脱出 (i==3 で False)
末尾追加: word1[3:] = "" / word2[3:] = "" → 影響なし
結果: "apbqcr"

----------------------------------------

Example 2: word1 = "ab", word2 = "pqrs"

word1: │ a │ b │           (短い)
word2: │ p │ q │ r │ s │   (長い → 余りが出る)

ループ内:
  i=0,j=0 → [a, p]   → i=1, j=1
  i=1,j=1 → [a, p, b, q] → i=2, j=2

i=2 で while 条件 (i < 2) False、脱出。
末尾追加:
  word1[2:] = ""    → 何も足さない
  word2[2:] = "rs"  → res = [a, p, b, q, "rs"]
"".join(res) = "apbqrs"

注意: res.append("rs") は 1 要素として "rs" を入れるが、
      最後の "".join() がそれを 1 文字ずつ繋いでくれるので OK。
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
n = len(word1), m = len(word2)

時間: O(n + m)  ← 各文字を 1 回触る
空間: O(n + m)  ← 結果文字列の長さぶん

ポイント:
1. 二ポインタ i, j で word1, word2 を独立に進める。
   ループ条件は "両方ともまだ残っているか"。
2. ループ脱出後、片方は必ず空、もう片方に余りがあるかも → スライスで一括追加。
3. Python の文字列は immutable なので、+= で繋ぐと毎回 O(n) かかる。
   res = [] に貯めて最後に "".join(res) するのが定番の高速化。
4. もっと短く書くなら zip_longest を使った 1 行解もある:
     from itertools import zip_longest
     return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=""))
"""
