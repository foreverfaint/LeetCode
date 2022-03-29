from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        return sum([n for i, n in enumerate(nums) if i % 2 == 1])


if __name__ == "__main__":
    sln = Solution()
    print(sln.arrayPairSum([1,4,3,2]))
    print(sln.arrayPairSum([6,2,6,5,1,2]))