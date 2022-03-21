from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int((n + 1) * n // 2 - sum(nums))


if __name__ == "__main__":
    sln = Solution()
    print(sln.missingNumber([3,0,1]))
    print(sln.missingNumber([0,1]))
    print(sln.missingNumber([9,6,4,2,3,5,7,0,1]))