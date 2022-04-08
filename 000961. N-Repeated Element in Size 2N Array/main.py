
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 2):
            if nums[i] == nums[i + 1]:
                return nums[i]
            elif nums[i] == nums[i + 2]:
                return nums[i]
            elif nums[i + 1] == nums[i + 2]:
                return nums[i + 1]
        return nums[-1]


if __name__ == "__main__":
    sln = Solution()
    print(sln.repeatedNTimes([1,2,3,3]))
    print(sln.repeatedNTimes([2,1,2,5,3,2]))
    print(sln.repeatedNTimes([5,1,5,2,5,3,5,4]))