from typing import List


class MyHashSet:
    def __init__(self):
        self.k = 10
        self.nums = [[] for _ in range(self.k)]
        
    def add(self, key: int) -> None:
        h = hash(key) % self.k
        if key not in self.nums[h]:
            self.nums[h].append(key)

    def remove(self, key: int) -> None:
        h = hash(key) % self.k
        if key in self.nums[h]:
            self.nums[h].remove(key)

    def contains(self, key: int) -> bool:
        h = hash(key) % self.k
        return key in self.nums[h]


if __name__ == "__main__":
    sln = MyHashSet()
    sln.add(1)
    sln.add(2)
    print(sln.contains(1))
    print(sln.contains(3))
    sln.add(2)
    print(sln.contains(2))
    sln.remove(2)
    print(sln.contains(2))