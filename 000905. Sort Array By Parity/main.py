from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] % 2 == 0:
                i += 1
                continue
            while i < j:
                if nums[j] % 2 == 1:
                    j -= 1
                    continue
                break
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == "__main__":
    sln = Solution()
    print(sln.sortArrayByParity([3,1,2,4]))
    print(sln.sortArrayByParity([0]))