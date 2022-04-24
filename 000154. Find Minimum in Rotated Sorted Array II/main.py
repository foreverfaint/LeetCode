from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        elif l == 2:
            return min(nums[0], nums[1])
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2
        if nums[mid] < nums[0]:
            return min(nums[mid], self.findMin(nums[:mid]))
        return min([nums[0], self.findMin(nums[:mid]), self.findMin(nums[mid+1:])])


if __name__ == "__main__":
    sln = Solution()
    print(sln.findMin([10,1,10,10,10]))
    print(sln.findMin([3,1]))
    print(sln.findMin([1,3,5]))
    print(sln.findMin([2,2,2,0,1]))