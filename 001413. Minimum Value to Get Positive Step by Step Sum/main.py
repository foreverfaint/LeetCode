from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        acc = [nums[0]]
        for i in range(1, len(nums)):
            acc.append(nums[i] + acc[-1])
        return max(1, 1 - min(acc))


if __name__ == "__main__":
    sln = Solution()
    print(sln.minStartValue([-3,2,-3,4,2]))
    print(sln.minStartValue([1,2]))
    print(sln.minStartValue([1,-2,-3]))