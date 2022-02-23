from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        l = len(nums)
        while j < l:
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1

        while i < l:
            nums[i] = 0
            i += 1


if __name__ == "__main__":
    sln = Solution()
    
    nums = [0,1,0,3,12]
    sln.moveZeroes(nums)
    print(nums)
    
    nums = [0]
    sln.moveZeroes(nums)
    print(nums)