from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = [False] * len(nums)
        num = 0
        for i, digit in enumerate(nums):
            num <<= 1
            num += digit
            if num % 5 == 0:
                ans[i] = True
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.prefixesDivBy5([0,1,1]))
    print(sln.prefixesDivBy5([1,1,1]))