from typing import List


class MyStack:

    def __init__(self):
        from queue import Queue
        self.curr_q = Queue()
        self.next_q = Queue()
        

    def push(self, x: int) -> None:
        self.next_q.put_nowait(x)
        while not self.curr_q.empty():
            y = self.curr_q.get_nowait()
            self.next_q.put_nowait(y)
        self.curr_q, self.next_q = self.next_q, self.curr_q

    def pop(self) -> int:
        return self.curr_q.get_nowait()
        

    def top(self) -> int:
        x = self.pop()
        self.push(x)
        return x
        

    def empty(self) -> bool:
        return self.curr_q.empty()


if __name__ == "__main__":
    sln = MyStack()
    sln.push(1)
    sln.push(2)
    print(sln.top())
    print(sln.pop())
    print(sln.empty())
    print(sln.pop())
    print(sln.empty())