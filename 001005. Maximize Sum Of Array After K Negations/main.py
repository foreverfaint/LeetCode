from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        l = len(nums)

        i = 0 
        while i < k and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            if i == l:
                # all the numbers are negatives
                if (k - l) % 2 == 1:
                    nums[l - 1] = -nums[l - 1]
                break

        if i < k and i < l and nums[i] > 0:
            if (k - i) % 2 == 1:
                if i > 0 and abs(nums[i]) > abs(nums[i - 1]):
                    nums[i - 1] = -nums[i - 1]
                else:
                    nums[i] = -nums[i]
        return sum(nums)

        
if __name__ == "__main__":
    sln = Solution()
    print(sln.largestSumAfterKNegations([4,2,3], k = 1))
    print(sln.largestSumAfterKNegations(nums = [3,-1,0,2], k = 3))
    print(sln.largestSumAfterKNegations(nums = [2,-3,-1,5,-4], k = 2))
    print(sln.largestSumAfterKNegations(nums = [-8,3,-5,-3,-5,-2], k = 6))
    print(sln.largestSumAfterKNegations(nums = [-4, -2, -3], k = 4))