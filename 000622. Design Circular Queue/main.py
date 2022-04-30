from typing import List


class MyCircularQueue:

    def __init__(self, k: int):
        self.head = 0
        self.tail = 0
        self.data = [None] * k
        self.size = 0
        
    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.data[self.tail] = value
            self.tail = (self.tail + 1) % len(self.data)
            self.size += 1
            return True
        return False

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % len(self.data)
        self.size -= 1
        return True
        
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.data[self.head]
        
    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.data[(self.tail - 1) % len(self.data)]

    def isEmpty(self) -> bool:
        return self.size == 0
        
    def isFull(self) -> bool:
        return self.size == len(self.data)


if __name__ == "__main__":
    sln = None
    res = []
    for i, (cmd, args) in enumerate(zip(
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"],
[[3], [1], [2], [3], [4], [], [], [], [4], []]
    )):
        if i == 0:
            sln = MyCircularQueue(*args)
            res.append(None)
        else:
            res.append(eval(f"sln.{cmd}(*{args})"))
            print(f"sln.{cmd}(*{args})", "=>", sln.data, sln.head, sln.tail, res[-1])
    print(res)