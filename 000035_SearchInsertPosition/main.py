from typing import List


class Solution:
    def _find(self, nums, low, high, target) -> int:
        if low >= high:
            return (low + 1) if nums[low] < target else low

        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        
        if nums[mid] < target:
            return self._find(nums, mid + 1, high, target)
        
        return self._find(nums, low, mid, target)


    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        return self._find(nums, 0, len(nums) - 1, target)


if __name__ == "__main__":
    sln = Solution()
    print(sln.searchInsert([], 5))
    print(sln.searchInsert([1,3,5,6], 5))
    print(sln.searchInsert([1,3,5,6], 2))
    print(sln.searchInsert([1,3,5,6], 7))