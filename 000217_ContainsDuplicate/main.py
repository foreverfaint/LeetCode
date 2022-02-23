from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) == len(set(nums))


if __name__ == "__main__":
    sln = Solution()