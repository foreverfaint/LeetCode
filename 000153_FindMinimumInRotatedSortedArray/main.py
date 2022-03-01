from typing import List


class Solution:
    def _f(self, nums, low, high):
        if low == high:
            return low
        
        if low + 1 == high:
            return low if nums[low] < nums[high] else high

        # 0, split, low, high
        if nums[low] < nums[0]:
            return self._f(nums, 1, low)

        # 0, low, high, split
        if nums[high] > nums[0]:
            return self._f(nums, high + 1, len(nums) - 1)

        mid = low + (high - low) // 2
        # 0, split, mid, high
        if nums[mid] < nums[0]:
            return self._f(nums, 1, mid)
        
        # 0, mid, split, high
        if nums[0] < nums[mid] and nums[high] < nums[0]:
            return self._f(nums, mid + 1, high)

    def findMin(self, nums: List[int]) -> int:
        return nums[self._f(nums, 0, len(nums) - 1)] if nums[-1] < nums[0] else nums[0]


if __name__ == "__main__":
    sln = Solution()
    print(sln.findMin([4,5,1,2,3]))
    # print(sln.findMin([3,1,2]))
    # print(sln.findMin([3,4,5,1,2]))
    # print(sln.findMin([4,5,6,7,0,1,2]))
    # print(sln.findMin([11,13,15,17]))