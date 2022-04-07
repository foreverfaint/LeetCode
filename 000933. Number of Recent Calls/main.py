from typing import List


class RecentCounter:
    def __init__(self):
        self.arr = []

    def ping(self, t: int) -> int:
        self.arr.append(t)
        low = t - 3000
        self.arr = [n for n in self.arr if n >= low]
        return len(self.arr)


if __name__ == "__main__":
    sln = RecentCounter()
    print(sln.ping(1))
    print(sln.ping(100))
    print(sln.ping(3001))
    print(sln.ping(3002))