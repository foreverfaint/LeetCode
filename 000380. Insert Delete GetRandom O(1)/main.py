from typing import List
import random


class RandomizedSet:
    def __init__(self):
        self.index = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        self.data.append(val)
        self.index[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.index:
            loc = self.index[val]
            self.data[loc], self.data[-1] = self.data[-1], self.data[loc]
            self.index[self.data[loc]] = loc
            del self.index[val]
            self.data = self.data[:-1]
            return True
        return False

    def getRandom(self) -> int:
        i = random.randint(0, len(self.index) - 1)
        return self.data[i]


if __name__ == "__main__":
    sln = None
    res = []
    for i, (cmd, args) in enumerate(zip(
        # ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
        # [[], [1], [2], [2], [], [1], [2], []]
["RandomizedSet","insert","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"],
[[],[0],[0],[-1],[0],[],[],[],[],[],[],[],[],[],[]]
    )):
        if i == 0:
            sln = RandomizedSet()
            res.append(None)
        else:
            res.append(eval(f"sln.{cmd}(*{args})"))
            print(sln.index, sln.data)
    print(res)