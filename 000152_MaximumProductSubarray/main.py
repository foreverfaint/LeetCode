from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l = len(nums)
        maxp = nums[0]
        minp = nums[0]
        r = nums[0]
        i = 1
        while i < l:
            maxp, minp = max(maxp * nums[i], nums[i], minp * nums[i]), min(maxp * nums[i], nums[i], minp * nums[i])
            r = max(maxp, r)
            i += 1
        return r


if __name__ == "__main__":
    sln = Solution()
    # print(sln.maxProduct([-2,3,-4]))
    print(sln.maxProduct([2,3,-2,4]))
    # print(sln.maxProduct([-2,0,-1]))