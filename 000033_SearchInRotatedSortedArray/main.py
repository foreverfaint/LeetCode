from typing import List


class Solution:
    def _f(self, nums, low, high, target):
        if low > high:
            return -1
        
        if low == high:
            return low if nums[low] == target else -1

        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            if (target < nums[0]) == (nums[mid] < nums[0]):
                return self._f(nums, low, mid - 1, target)
            return self._f(nums, mid + 1, high, target)
        else:
            if (target < nums[0]) == (nums[mid] < nums[0]):
                return self._f(nums, mid + 1, high, target)
            return self._f(nums, low, mid - 1, target)

    def search(self, nums: List[int], target: int) -> int:
        return self._f(nums, 0, len(nums) - 1, target)


if __name__ == "__main__":
    sln = Solution()
    print(sln.search([4,5,6,7,0,1,2], 0))
    print(sln.search([4,5,6,7,0,1,2], 3))
    print(sln.search([1], 0))