from typing import List
import heapq

class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]
            
    def add(self, val):
        self.nums.append(val)
        self.nums = sorted(self.nums, reverse=True)[:self.k]
        return self.nums[-1]


if __name__ == "__main__":
    sln = KthLargest(3, [4, 5, 8, 2])
    print(sln.add(3))
    print(sln.add(5))
    print(sln.add(10))
    print(sln.add(9))
    print(sln.add(4))