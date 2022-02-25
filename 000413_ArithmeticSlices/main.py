from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 3:
            return 0

        n = 0
        i = 2
        diff = nums[1] - nums[0]
        c_diff = 1
        while i < l:
            if nums[i] - nums[i - 1] == diff:
                n += c_diff
                c_diff += 1
            else:
                diff = nums[i] - nums[i - 1]
                c_diff = 1
            i += 1
        return n


if __name__ == "__main__":
    sln = Solution()
    print(sln.numberOfArithmeticSlices([1,2,3,4]))
    print(sln.numberOfArithmeticSlices([1]))