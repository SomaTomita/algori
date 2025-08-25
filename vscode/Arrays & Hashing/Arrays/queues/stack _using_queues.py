# Implement Stack Using Queues
# Implement a last-in-first-out (LIFO) stack using only two queues.
# The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively.
# You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

# Example 1:
# Input: ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]

# Output: [null, null, null, 2, 2, false]
# Explanation:
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False

# Constraints:
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, top, and empty.
# All the calls to pop and top are valid.
# Follow-up: Can you implement the stack using only one queue?

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


from collections import deque


class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            first_out = self.q.popleft()
            self.q.append(first_out)
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0


myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top())
print(myStack.pop())
print(myStack.empty())

# popの流れ:
# 初期状態: q = deque([1, 2])

# for _ in range(len(self.q) - 1): の処理
# 1回目: q.popleft()で1を取り出し、push(1)で末尾に追加
# → q = deque([2, 1])

# forループ終了後、q.popleft()で2を取り出して返す
# → q = deque([1])
# return 2


# ------------------------------------------------------------
# ------------------------------------------------------------

# python基礎

# deque: 両端キュー（Double-Ended Queue）の略
# リストと違い、両端での追加・削除が効率的

# 初期化:
d = deque([1, 2, 3])

# 基本操作:
d.append(4)  # 右端に追加: [1, 2, 3, 4]
d.appendleft(0)  # 左端に追加: [0, 1, 2, 3, 4]

d.pop()  # 右端から削除: [0, 1, 2, 3]
d.popleft()  # 左端から削除: [1, 2, 3]

# 要素へのアクセス:
print(d[0])  # 最初の要素: 1
print(d[-1])  # 最後の要素: 3


# キューの実装（First In First Out - FIFO）:
queue = deque()
queue.append(1)  # [1]
queue.append(2)  # [1, 2]
queue.append(3)  # [1, 2, 3]
first_out = queue.popleft()  # 1を取り出す [2, 3]
print(f"First out: {first_out}")  # 1（最初に入れた要素）

# スタックの実装（Last In First Out - LIFO）:
stack = deque()
stack.append(1)  # [1]
stack.append(2)  # [1, 2]
stack.append(3)  # [1, 2, 3]
last_in = stack.pop()  # 3を取り出す [1, 2]
print(f"Last in: {last_in}")  # 3（最後に入れた要素）
