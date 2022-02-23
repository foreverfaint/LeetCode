from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        l = len(nums)
        c = 0
        while i < l:
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
                c += 1
            i += 1
        return c


if __name__ == "__main__":
    sln = Solution()
    print(sln.removeElement([1], 1))
    print(sln.removeElement([2], 3))
    print(sln.removeElement([3, 3], 5))
    print(sln.removeElement([3, 3], 3))
    print(sln.removeElement([3,2,2,3], 3))
    print(sln.removeElement([0,1,2,2,3,0,4,2], 2))
