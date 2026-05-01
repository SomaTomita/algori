"""
Remove All Adjacent Duplicates In String (LeetCode 1047 - Easy)

You are given a string s.
Remove all adjacent duplicate characters from the string and return the result.

A duplicate removal consists of choosing two adjacent and equal letters and removing them.
We repeatedly make duplicate removals on s until we can no longer.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation:
"abbaca" → "aaca" (remove "bb")
"aaca" → "ca" (remove "aa")

Example 2:
Input: s = "azxxzy"
Output: "ay"
Explanation:
"azxxzy" → "azzy" (remove "xx")
"azzy" → "ay" (remove "zz")

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


print(Solution().removeDuplicates("abbaca"))
"""
流れ: s = "abbaca"

初期: stack = []

========================================

i=0, c='a'
条件: stack が空 → False
処理: stack.append('a')
結果: stack = ['a']
文字列: "a"

========================================

i=1, c='b'
条件: stack[-1]='a' == 'b' ? → False
処理: stack.append('b')
結果: stack = ['a', 'b']
文字列: "ab"

========================================

i=2, c='b'
条件: stack[-1]='b' == 'b' ? → True (重複発見!)
処理: stack.pop() (bを削除)
結果: stack = ['a']
文字列: "a"

========================================

i=3, c='a'
条件: stack[-1]='a' == 'a' ? → True (重複発見!)
処理: stack.pop() (aを削除)
結果: stack = []
文字列: ""

========================================

i=4, c='c'
条件: stack が空 → False
処理: stack.append('c')
結果: stack = ['c']
文字列: "c"

========================================

i=5, c='a'
条件: stack[-1]='c' == 'a' ? → False
処理: stack.append('a')
結果: stack = ['c', 'a']
文字列: "ca"

========================================

最終結果: "ca" ✓

スタックの状態遷移:
[] → ['a'] → ['a','b'] → ['a'] → [] → ['c'] → ['c','a']

========================================
"""


# ------------------------------------------------------------

print(Solution().removeDuplicates("azxxzy"))

"""
流れ: s = "azxxzy"

初期: stack = []

========================================

i=0, c='a'
処理: stack.append('a')
結果: stack = ['a']

========================================

i=1, c='z'
条件: stack[-1]='a' == 'z' ? → False
処理: stack.append('z')
結果: stack = ['a', 'z']

========================================

i=2, c='x'
条件: stack[-1]='z' == 'x' ? → False
処理: stack.append('x')
結果: stack = ['a', 'z', 'x']

========================================

i=3, c='x'
条件: stack[-1]='x' == 'x' ? → True (重複!)
処理: stack.pop()
結果: stack = ['a', 'z']

========================================

i=4, c='z'
条件: stack[-1]='z' == 'z' ? → True (重複!)
処理: stack.pop()
結果: stack = ['a']

========================================

i=5, c='y'
条件: stack[-1]='a' == 'y' ? → False
処理: stack.append('y')
結果: stack = ['a', 'y']

========================================

最終結果: "ay" ✓

スタックの状態遷移:
[] → ['a'] → ['a','z'] → ['a','z','x'] → ['a','z'] → ['a'] → ['a','y']

========================================
"""
