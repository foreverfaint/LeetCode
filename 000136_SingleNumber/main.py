from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        r = 0
        for x in nums:
            r = r ^ x
        return r


if __name__ == "__main__":
    sln = Solution()
    print(sln.singleNumber([2,2,1]))
    print(sln.singleNumber([4,1,2,1,2]))
    print(sln.singleNumber([1]))