from typing import List


class Solution:
    def _search(self, nums, left, right, target) -> int:
        if left == right:
            return -1

        mid = left + (right - left) // 2
        if mid == left:
            return mid if nums[mid] == target else -1

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self._search(nums, mid + 1, right, target)
        return self._search(nums, left, mid, target)

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        return self._search(nums, 0, len(nums), target)


if __name__ == "__main__":
    sln = Solution()
    print(sln.search([], 9))
    print(sln.search([-1], 9))
    print(sln.search([9], 9))
    print(sln.search([-1, 2], 9))
    print(sln.search([2, 9], 2))
    print(sln.search([2, 9], 9))
    print(sln.search([-1,0,3,5,9,12], 9))
    print(sln.search([-1,0,3,5,9,12], 2))