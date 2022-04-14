from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i, n in zip(index, nums):
            target = target[:i] + [n] + target[i:]
        return target

if __name__ == "__main__":
    sln = Solution()
    print(sln.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))
    print(sln.createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
    print(sln.createTargetArray(nums = [1], index = [0]))