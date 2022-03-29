from typing import List


class Solution:
    def foo(self, nums):
        nums = sorted(nums)
        dist = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] != dist:
                return False
        return True

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        return [self.foo(nums[l_i: r_i + 1]) for l_i, r_i in zip(l, r)]


if __name__ == "__main__":
    sln = Solution()
    print(sln.checkArithmeticSubarrays(nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]))
    print(sln.checkArithmeticSubarrays([-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]))