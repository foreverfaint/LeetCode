from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s1 = max(nums)
        nums = [n for n in nums if n != s1]
        if not nums:
            return s1
        s2 = max(nums)
        nums = [n for n in nums if n != s2]
        if not nums:
            return s1
        return max(nums)


if __name__ == "__main__":
    sln = Solution()
    print(sln.thirdMax([3,2,1]))
    print(sln.thirdMax([1,2]))
    print(sln.thirdMax([2,2,3,1]))