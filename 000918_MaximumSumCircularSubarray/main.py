from typing import List


class Solution:
    def maxSubArray(self, f, nums: List[int]) -> int:
        l = len(nums)
        global_ = current_ = nums[0]
        i = 1
        while i < l:
            current_ = f(nums[i], current_ + nums[i])
            global_ = f(global_, current_)
            i += 1
        return global_

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_ = self.maxSubArray(max, nums)
        min_ = self.maxSubArray(min, nums)
        if sum(nums) == min_:
            return max_
        return max(max_, sum(nums) - min_)


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxSubarraySumCircular([1,-2,3,-2]))
    print("---")
    print(sln.maxSubarraySumCircular([5,-3,5]))
    print("---")
    print(sln.maxSubarraySumCircular([-3,-2,-3]))
    print("---")
    print(sln.maxSubarraySumCircular([9,-4,-7,9]))