from typing import List


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) <= 1:
            return 0

        nums = sorted(nums)
        ans = nums[-1] - nums[0]
        for i in range(1, len(nums)):
            min_ = min(nums[i] - k, nums[0] + k)
            max_ = max(nums[i - 1] + k, nums[-1] - k)
            ans = min(ans, abs(max_ - min_))
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.smallestRangeII(nums = [7,8,8], k = 5))
    print(sln.smallestRangeII(nums = [1], k = 0))
    print(sln.smallestRangeII(nums = [0,10], k = 2))
    print(sln.smallestRangeII(nums = [1,3,6], k = 3))