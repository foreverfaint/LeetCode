from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = len(nums)

        i = 0
        s = 0
        while i < k:
            s += nums[i]
            i += 1
        
        max_s = s
        while i < l:
            s += nums[i]
            s -= nums[i - k]
            max_s = max(max_s, s)
            i += 1

        return max_s / k


if __name__ == "__main__":
    sln = Solution()
    print(sln.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
    print(sln.findMaxAverage(nums = [5], k = 1))
    print(sln.findMaxAverage(nums = [5, 10], k = 1))