from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        s = 1
        max_s = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                s += 1
                max_s = max(max_s, s)
            else:
                s = 1
        return max_s


if __name__ == "__main__":
    sln = Solution()
    print(sln.findLengthOfLCIS([1,3,5,4,2,3,4,5]))
    # print(sln.findLengthOfLCIS([1,3,5,4,7]))
    # print(sln.findLengthOfLCIS([2,2,2,2,2]))