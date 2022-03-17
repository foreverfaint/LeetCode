from typing import List


class MinStack:
    def __init__(self):
        self.q = []

    def push(self, val: int) -> None:
        self.q.append((val, min(val, self.q[-1][1] if self.q else val)))

    def pop(self) -> None:
        self.q = self.q[:-1]

    def top(self) -> int:
        return self.q[-1][0]

    def getMin(self) -> int:
        return self.q[-1][1]


if __name__ == "__main__":
    target = MinStack()
    target.push(-2)
    target.push(0)
    target.push(-3)
    print(target.getMin())
    target.pop()
    print(target.top())
    print(target.getMin())