from typing import List


class Solution:
    def _f(self, nums, low, high):
        if low == high:
            return low
        if low + 1 == high:
            return low if nums[low] > nums[high] else high
        mid = low + (high - low) // 2
        if nums[mid] <= nums[high]:
            return self._f(nums, mid + 1, high)
        if nums[mid] <= nums[low]:
            return self._f(nums, low, mid - 1)
        if nums[high] < nums[mid]:
            return self._f(nums, low, high - 1)
        if nums[low] < nums[mid]:
            return self._f(nums, low + 1, high)

    def findPeakElement(self, nums: List[int]) -> int:
        return self._f(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    sln = Solution()
    print(sln.findPeakElement([1,2,1,2,1]))
    print(sln.findPeakElement([1,2,3,1]))
    print(sln.findPeakElement([1,2,1,3,5,6,4]))