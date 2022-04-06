from typing import List


class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_ = max(nums)
        min_ = min(nums)
        return 0 if max_ - min_ < 2*k else (max_ - min_ - 2 *k)


if __name__ == "__main__":
    sln = Solution()
    print(sln.smallestRangeI(nums = [1], k = 0))
    print(sln.smallestRangeI(nums = [0,10], k = 2))
    print(sln.smallestRangeI(nums = [1,3,6], k = 3))