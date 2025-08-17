# Minimum Stack
# Design a stack class that supports the push, pop, top, and getMin operations.

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# Each function should run in
# O(1) time complexity.

# Example 1:
# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]
# Output: [null,null,null,null,0,null,2,1]

# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(1);
# minStack.push(2);
# minStack.push(0);
# minStack.getMin(); // return 0
# minStack.pop();
# minStack.top();    // return 2
# minStack.getMin(); // return 1
# Constraints:

# -2^31 <= val <= 2^31 - 1.
# pop, top and getMin will always be called on non-empty stacks.


from numpy import stack


class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# 流れ:
# push(5):
#   val = min(5, 5) → 5
#   stack = [5], minStack = [5]
# push(3):
#   val = min(3, 5) → 3
#   stack = [5, 3], minStack = [5, 3]
# push(7):
#   val = min(7, 3) → 3
#   stack = [5, 3, 7], minStack = [5, 3, 3]
# push(2):
#   val = min(2, 3) → 2
#   stack = [5, 3, 7, 2], minStack = [5, 3, 3, 2]


# 別解 : O(n)


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
        # 全要素をループして最小値を探す
        min_val = self.stack[0]  # 初期値はstackの最初の要素
        for v in self.stack:
            if v < min_val:
                min_val = v
        return min_val


# python 基礎

# min
a, b = 3, 5
print(min(a, b))  # 出力: 3


# if else (x if 条件 else y)
n = 5
result = "OK" if n > 0 else "NG"
print(result)  # => "OK"
result2 = "OK" if n < 0 else "NG"
print(result2)  # => "NG"
