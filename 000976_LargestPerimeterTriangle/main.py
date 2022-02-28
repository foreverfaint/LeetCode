from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i = len(nums) - 1
        while i > 1:
            a, b, c = nums[i], nums[i - 1], nums[i - 2]
            if b + c > a:
                return a + b + c
            i -= 1
        return 0


if __name__ == "__main__":
    sln = Solution()