from typing import List


class Solution:
    def _f(self, nums, target, low, high):
        if low >= high:
            return [-1, -1]

        mid = low + (high - low) // 2

        if nums[mid] > target:
            return self._f(nums, target, low, mid)

        if nums[mid] < target:
            return self._f(nums, target, mid + 1, high)

        l_r = self._f(nums, target, low, mid)[0]
        if l_r == -1:
            l_r = mid

        r_r = self._f(nums, target, mid + 1, high)[1]
        if r_r == -1:
            r_r = mid

        return [l_r, r_r]

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return self._f(nums, target, 0, len(nums))


if __name__ == "__main__":
    sln = Solution()
    print(sln.searchRange([5,7,7,8,8,10], 8))
    print(sln.searchRange([5,7,7,8,8,10], 6))
    print(sln.searchRange([], 0))