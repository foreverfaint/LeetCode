from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        i = 0
        l = len(nums)
        r = 1
        while i < l:
            if nums[i] == 0:
                return 0
            r *= (1 if nums[i] > 0 else -1)
            i += 1
        return r


if __name__ == "__main__":
    sln = Solution()
    print(sln.arraySign([-1,-2,-3,-4,3,2,1]))
    print(sln.arraySign([1,5,0,2,-3]))
    print(sln.arraySign([-1,1,-1,1,-1]))
