
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        max_global = max_current = 0
        i = 0
        while i < l:
            max_current = max(nums[i], max_current + nums[i])
            max_global = max(max_global, max_current)
            i += 1
        return max_global


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(sln.maxSubArray([1]))
    print(sln.maxSubArray([5,4,-1,7,8]))
    print(sln.maxSubArray([5,-3,5]))