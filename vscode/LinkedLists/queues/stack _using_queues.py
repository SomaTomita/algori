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


# ------------------------------------------------------------

# 別解


class MyStack_2queues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            first_out = self.q1.popleft()
            self.q2.append(first_out)

        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


myStack_2queues = MyStack_2queues()
myStack_2queues.push(1)
myStack_2queues.push(2)
print(myStack_2queues.top())
print(myStack_2queues.pop())
print(myStack_2queues.empty())

# pushの流れ:
# 初期状態: q1 = deque([]), q2 = deque([])
# 1. x = 1 を push する
# 2. q2.append(1) →→ q2 = deque([1])
# 3. while q1: →→ 条件が False なのでスキップ
# 4. q1, q2 = q2, q1 →→ q1 = deque([1]), q2 = deque([])

# 1. x = 2 を push する
# 2. q2.append(2) →→ q2 = deque([2])
# 3. while q1: →→ 条件が False なのでスキップ
# 4. q1, q2 = q2, q1 →→ q1 = deque([1]), q2 = deque([2])

# 1. while q1: →→ 条件が True なので実行
# 2. q2.append(q1.popleft()) →→ q2 = deque([2, 1])
# 3. q1, q2 = q2, q1 →→ q1 = deque([2, 1]), q2 = deque([])
# 4. while q1: →→ 条件が False なのでスキップ
# 5. q1, q2 = q2, q1 →→ q1 = deque([2, 1]), q2 = deque([])


# top:
# 初期状態: q1 = deque([2, 1]), q2 = deque([])
# q1[0] →→ 2


# pop:
# 初期状態: q1 = deque([2, 1]), q2 = deque([])
# q1.popleft() →→ 2
# q1 = deque([1]), q2 = deque([])


# ------------------------------------------------------------
# ------------------------------------------------------------


# スワップの使用例:

# 1. リストの要素のスワップ
arr = [1, 2, 3]
arr[0], arr[2] = arr[2], arr[0]  # [3, 2, 1]

# 2. 辞書のキーと値の反転
dict1 = {"a": 1, "b": 2}
dict2 = {v: k for k, v in dict1.items()}  # {1: 'a', 2: 'b'}

# 3. 変数の値の入れ替え
max_val = 10
min_val = 1
max_val, min_val = min_val, max_val
print(max_val, min_val)  # 1, 10

# 4. 3つの値を循環的にスワップ
x, y, z = 1, 2, 3
x, y, z = z, x, y
print(x, y, z)  # 3, 1, 2
