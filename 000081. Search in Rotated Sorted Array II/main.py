from typing import List


class Solution:
    def bs(self, nums, target):
        print(nums, target)
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return nums[low] == target


    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return True

        i = 0
        while i < len(nums) and nums[i] == nums[0]:
            i += 1

        j = i
        while j < len(nums) and nums[j] > nums[0]:
            if nums[j] == target:
                return True
            j += 1

        return False if nums[0] < target or j == len(nums) else self.bs(nums[j:], target)
        

if __name__ == "__main__":
    sln = Solution()
    print(sln.search(nums = [1], target = 0), "False")
    print(sln.search(nums = [3, 1], target = 1), "True")
    print(sln.search(nums = [5, 1, 3], target = 3), "True")
    print(sln.search(nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], target = 2), "True")
    print(sln.search(nums = [1], target = 1), "True")
    print(sln.search(nums = [2,5,6,0,0,1,2], target = 0), "True")
    print(sln.search(nums = [2,5,6,0,0,1,2], target = 3), "False")
    print(sln.search(nums = [1,0,1,1,1], target = 0), "True")