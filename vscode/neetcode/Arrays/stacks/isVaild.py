"""
Valid Parentheses

You are given a string s consisting of the following characters:
'(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:
- Every open bracket is closed by the same type of close bracket.
- Open brackets are closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:
1 <= s.length <= 1000
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # 閉じカッコ → 対応する開きカッコ のマップ
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                # 閉じカッコ: スタックの一番上が "対応する開きカッコ" か?
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    # 空 or 種類不一致 → 即不正
                    return False
            else:
                # 開きカッコ: 後で対応する閉じを待つためスタックに積む
                stack.append(c)

        # 全て対応が取れていればスタックは空
        return not stack


# ------------------------------------------------------------
# 動作確認 (成功例)
# ------------------------------------------------------------
print(Solution().isValid("([{}])"))  # True

"""
流れ (成功例): s = "([{}])"

初期: stack = []

========================================

i=0, c='('
判定: '(' は closeToOpen のキーか? → False (開きカッコ)
処理: stack.append('(')
結果: stack = ['(']

イメージ:
入力: ( [ { } ] )
       ↑
スタック (下→上): [ '(' ]

========================================

i=1, c='['
判定: '[' は閉じカッコか? → False
処理: stack.append('[')
結果: stack = ['(', '[']

入力: ( [ { } ] )
         ↑
スタック (下→上): [ '(', '[' ]

========================================

i=2, c='{'
処理: stack.append('{')
結果: stack = ['(', '[', '{']

入力: ( [ { } ] )
           ↑
スタック (下→上): [ '(', '[', '{' ]

========================================

i=3, c='}'
判定: '}' は閉じカッコ → closeToOpen['}'] = '{'
チェック: stack[-1] == '{' ? → True (一致!)
処理: stack.pop()
結果: stack = ['(', '[']

入力: ( [ { } ] )
             ↑
スタック (下→上): [ '(', '[' ]

========================================

i=4, c=']'
判定: ']' は閉じカッコ → closeToOpen[']'] = '['
チェック: stack[-1] == '[' ? → True (一致!)
処理: stack.pop()
結果: stack = ['(']

入力: ( [ { } ] )
               ↑
スタック (下→上): [ '(' ]

========================================

i=5, c=')'
判定: ')' は閉じカッコ → closeToOpen[')'] = '('
チェック: stack[-1] == '(' ? → True (一致!)
処理: stack.pop()
結果: stack = []

入力: ( [ { } ] )
                 ↑
スタック (下→上): [ ]

========================================

ループ終了: stack が空
return not stack = not [] = True ✓
"""


# ------------------------------------------------------------
# 動作確認 (失敗例)
# ------------------------------------------------------------
print(Solution().isValid("[(])"))  # False

"""
流れ (失敗例): s = "[(])"

初期: stack = []

========================================

i=0, c='[' → 開き → stack.append('[')
結果: stack = ['[']

========================================

i=1, c='(' → 開き → stack.append('(')
結果: stack = ['[', '(']

入力: [ ( ] )
        ↑
スタック (下→上): [ '[', '(' ]

========================================

i=2, c=']'
判定: ']' は閉じカッコ → closeToOpen[']'] = '['
チェック: stack[-1] == '[' ?
       stack[-1] = '(' なので '(' == '[' → False (不一致!)
処理: return False ✓

"直前に開いたのは '(' なのに ']' で閉じようとした → 順序がおかしい"
"""


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
計算量:
- 時間: O(n) — 各文字を1回ずつ処理。push/pop は O(1)。
- 空間: O(n) — 最悪、全ての文字が開きカッコの場合 (例: "(((((...")
       スタックに n 個積まれる。

ポイント:
1. 「直近に開いたカッコ」と「今来た閉じカッコ」が対応しているかは、
   LIFO (後入れ先出し) なスタックで自然に表現できる。
2. 早期 return False で、不正と確定した瞬間に打ち切れる。
3. 最後に "stack が空か" もチェックしないと、"(((" のような
   "開いたまま閉じない" ケースを見逃す。
"""


# ------------------------------------------------------------
# ------------------------------------------------------------

# python基礎

# 辞書のキーと値のチェック
mapping = {"a": 1, "b": 2, "c": 3}

letter = "b"
if letter in mapping:  # 「letter は mapping のキーかどうかチェック」
    print(mapping[letter])  # キー b の値 2 を取り出す

if letter in mapping.values():
    print("これは出ない")  # b は値ではなくキーなので処理されない

letter2 = "x"
if letter2 in mapping:
    print("これは出ない")  # x はキーじゃないので処理されない
