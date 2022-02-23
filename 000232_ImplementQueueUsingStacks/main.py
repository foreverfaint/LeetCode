class MyQueue:
    def __init__(self):
        self._a = []
        self._b = []

    def _pop(self, lst):
        return lst[-1],  lst[:-1]
        
    def push(self, x: int) -> None:
        while self._b:
            last, self._b = self._pop(self._b)
            self._a.append(last)

        self._b.append(x)

        while self._a:
            last, self._a = self._pop(self._a)
            self._b.append(last)

    def pop(self) -> int:
        last, self._b = self._pop(self._b)
        return last

    def peek(self) -> int:
        return self._b[-1]

    def empty(self) -> bool:
        return len(self._b) == 0


if __name__ == "__main__":
    q = MyQueue()
    print(q.push(1))
    print(q.push(2))
    print(q.peek())
    print(q.pop())
    print(q.empty())