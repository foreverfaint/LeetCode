from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return all([nums[i] <= nums[i-1] for i in range(1, len(nums))]) or all([nums[i] >= nums[i-1] for i in range(1, len(nums))])

        


if __name__ == "__main__":
    sln = Solution()
    print(sln.isMonotonic([1,2,2,3]))
    print(sln.isMonotonic([6,5,4,4]))
    print(sln.isMonotonic([1,3,2]))