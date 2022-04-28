from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        if nums[0] > nums[1]:
            return 0

        if nums[n - 2] < nums[n - 1]:
            return n - 1

        low = 1
        high = n - 2
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                high = mid - 1
            elif nums[mid] < nums[mid + 1]:
                low = mid + 1
        return low



if __name__ == "__main__":
    sln = Solution()
    # 1
    print(sln.findPeakElement([1,2,1,2,1]))
    # 2
    print(sln.findPeakElement([1,2,3,1]))
    # 5
    print(sln.findPeakElement([1,2,1,3,5,6,4]))