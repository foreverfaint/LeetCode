from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        i = 0
        s = 0
        t = sum(nums)
        while i < len(nums):
            s += nums[i]
            if s > t - s:
                return nums[:i + 1]
            i += 1

if __name__ == "__main__":
    sln = Solution()
    print(sln.minSubsequence([4,3,10,9,8]))
    print(sln.minSubsequence([4,4,7,6,7]))
    print(sln.minSubsequence([6]))