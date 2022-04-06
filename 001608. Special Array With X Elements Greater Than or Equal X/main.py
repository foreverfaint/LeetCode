from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        l = len(nums)
        for i in range(l):
            if i == 0:
                if l <= nums[i]:
                    return l
            elif nums[i - 1] < l - i <= nums[i]:
                return l - i
        return -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.specialArray([3,5]))
    print(sln.specialArray([0,0]))
    print(sln.specialArray([0,4,3,0,4]))
    print(sln.specialArray([3,6,7,7,0]))