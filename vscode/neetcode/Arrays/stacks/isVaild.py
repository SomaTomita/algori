# Valid Parentheses
# You are given a string s consisting of
#  the following characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:
# Every open bracket is closed by the same type of close bracket.
# Open brackets are closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.

# Example 1:
# Input: s = "[]"
# Output: true

# Example 2:
# Input: s = "([{}])"
# Output: true

# Example 3:
# Input: s = "[(])"
# Output: false
# Explanation: The brackets are not closed in the correct order.

# Constraints: 1 <= s.length <= 1000


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


s = "([{}])"
print(Solution().isValid(s))
# 流れ:
# s = "({[]})"
# i=0, c='(' → stack = ['(']
# i=1, c='{' → stack = ['(', '{']
# i=2, c='[' → stack = ['(', '{', '[']
# i=3, c=']' → check stack[len(stack)-1] == '[' → OK → pop → stack = ['(', '{']
# i=4, c='}' → check stack[len(stack)-1] == '{' → OK → pop → stack = ['(']
# i=5, c=')' → check stack[len(stack)-1] == '(' → OK → pop → stack = []
# 出力: True

s = "[(])"
print(Solution().isValid(s))
# 流れ:
# s = "[(])"
# i=0, c='[' → stack = ['[']
# i=1, c='(' → stack = ['[', '(']
# i=2, c=']' → check stack[len(stack)-1] == '(' → NG
# 出力: False


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
