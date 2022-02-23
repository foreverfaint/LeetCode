from typing import List


class Solution:
    def _reverse(self, nums, low, high) -> None:
        while low < high:
            t = nums[low]
            nums[low] = nums[high]
            nums[high] = t
            low += 1
            high -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self._reverse(nums, 0, len(nums) - k - 1)
        self._reverse(nums, len(nums) - k, len(nums) - 1)
        self._reverse(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    sln = Solution()

    nums = [1,2,3,4,5,6,7]
    sln.rotate(nums, 3)
    print(nums)
    
    nums = [-1,-100,3,99]
    sln.rotate(nums, 2)
    print(nums)
    
    nums = [1,2,3,4,5,6]
    sln.rotate(nums, 11)
    print(nums)