"""
Min Stack

Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop()         removes the element on the top of the stack.
int top()          gets the top element of the stack.
int getMin()       retrieves the minimum element in the stack.

Each function should run in O(1) time complexity.

Example 1:
Input:  ["MinStack","push",1,"push",2,"push",0,"getMin","pop","top","getMin"]
Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin();  // return 0
minStack.pop();
minStack.top();     // return 2
minStack.getMin();  // return 1

Constraints:
-2^31 <= val <= 2^31 - 1
pop, top and getMin will always be called on non-empty stacks.
"""


# ------------------------------------------------------------
# 解法1: 補助スタック (minStack) を持つ O(1) 解
# ------------------------------------------------------------
class MinStack:
    def __init__(self):
        self.stack = []      # 通常のスタック
        self.minStack = []   # 各時点での最小値を覚えておくスタック

    def push(self, val: int) -> None:
        self.stack.append(val)
        # "今この時点での最小値" を計算してプッシュ
        # minStack が空なら今の val 自身、そうでなければ既存の最小と比較
        cur_min = min(val, self.minStack[-1]) if self.minStack else val
        self.minStack.append(cur_min)

    def pop(self) -> None:
        # 2 つのスタックを同時に pop することで整合性を保つ
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # 最小値はいつでも minStack の頂上に置いてある → O(1)
        return self.minStack[-1]


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
ms = MinStack()
ms.push(5)
ms.push(3)
ms.push(7)
ms.push(2)
print(ms.getMin())  # 2
ms.pop()             # 2 を取り出す
print(ms.getMin())  # 3 (minStack の整合性が崩れていない)
print(ms.top())     # 7

"""
流れ: push(5) → push(3) → push(7) → push(2)

========================================

push(5):
  stack に 5 を append
  minStack: 空 → cur_min = 5
  minStack に 5 を append

  stack    = [5]
  minStack = [5]
                        ←── minStack[-1] = 5 (最小値)

========================================

push(3):
  stack に 3 を append
  minStack: 末尾 5, cur_min = min(3, 5) = 3
  minStack に 3 を append

  stack    = [5, 3]
  minStack = [5, 3]
                        ←── minStack[-1] = 3 (最小値)

========================================

push(7):
  stack に 7 を append
  minStack: 末尾 3, cur_min = min(7, 3) = 3
  minStack に 3 を再 append (最小は変わらないので 3 のまま)

  stack    = [5, 3, 7]
  minStack = [5, 3, 3]
                        ←── minStack[-1] = 3 (最小値)

  ポイント: ここで 7 は最小ではないが、minStack には 3 を積み直す。
            こうすると pop 時に "stack と minStack が必ず同じ高さ" を
            保てるので、整合性が壊れない。

========================================

push(2):
  cur_min = min(2, 3) = 2

  stack    = [5, 3, 7, 2]
  minStack = [5, 3, 3, 2]
                        ←── minStack[-1] = 2 (最小値)

========================================

pop():  (2 を取り除く)
  stack    = [5, 3, 7]
  minStack = [5, 3, 3]

  → getMin() は minStack[-1] = 3 を返す
  → 2 がいなくなった瞬間に最小値は自動で 3 に戻る

========================================

各操作はすべて O(1):
  push    → append 2 回
  pop     → pop 2 回
  top     → stack[-1]
  getMin  → minStack[-1]
"""


# ------------------------------------------------------------
# 解法2: シンプルだが getMin が O(n) になる版 (比較用)
# ------------------------------------------------------------
class SimpleStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # 全要素をループして最小値を探す → O(n)
        min_val = self.stack[0]
        for v in self.stack:
            if v < min_val:
                min_val = v
        return min_val


# ------------------------------------------------------------
# 計算量まとめ
# ------------------------------------------------------------
"""
解法1 (minStack あり):
  push    O(1) / pop    O(1) / top O(1) / getMin O(1)
  空間: O(n)  (stack と minStack で 2n 個の要素)

解法2 (シンプル):
  push    O(1) / pop    O(1) / top O(1) / getMin O(n)
  空間: O(n)

ポイント:
1. 「最小値の履歴」をスタックとして並走させると、pop 時に最小値が
   自動的に 1 つ前の状態に戻る。これが minStack 解の核。
2. push のたびに minStack も必ず 1 個積む (最小が変わらなくても再 append)。
   こうすることで stack と minStack の高さが常に一致し、pop の整合性が崩れない。
3. もし「最小が更新された時だけ minStack に積む」設計にすると、
   pop でその値が抜けた時の戻し処理が複雑になる。常に積む方がシンプル。
"""


# ------------------------------------------------------------
# python 基礎
# ------------------------------------------------------------

# min
a, b = 3, 5
print(min(a, b))  # 出力: 3

# 三項演算子 (x if 条件 else y)
n = 5
result = "OK" if n > 0 else "NG"
print(result)   # "OK"
result2 = "OK" if n < 0 else "NG"
print(result2)  # "NG"
