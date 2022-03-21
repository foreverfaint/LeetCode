# -*- encoding: utf-8 -*-
from typing import List


def permute(nums):
    if len(nums) == 1:
        yield [nums[0]]
    else:
        for i in range(len(nums)):
            t = nums[i]
            nums[i] = nums[0]
            for arr in permute(nums[1:]):
                yield [t] + arr
            nums[i]  = t


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.ans = list(self.nums)
        
    def reset(self) -> List[int]:
        self.ans = list(self.nums)
        return self.ans 
        

    def shuffle(self) -> List[int]:
        for i in range(len(self.ans) - 1):
           from random import randint
           x = randint(i, len(self.ans) - 1)
           self.ans[i], self.ans[x] = self.ans[x], self.ans[i]
        return self.ans


if __name__ == "__main__":
    sln = Solution([1,2,3])
    print(sln.shuffle())
    print(sln.reset())
    print(sln.shuffle())
