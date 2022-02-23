
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        i = 1
        j = 1
        l = len(nums)
        c = 1
        n = nums[0]
        while i < l:
            if n != nums[i]:
                nums[j] = nums[i]
                j += 1
                n = nums[i]
                c += 1
            i += 1
        return c


if __name__ == "__main__":
    sln = Solution()

    a = []
    print(a, sln.removeDuplicates(a))

    a = [1,1,2]
    print(a, sln.removeDuplicates(a))

    a = [1,2,3]
    print(a, sln.removeDuplicates(a))

    a = [0,0,1,1,1,2,2,3,3,4]
    print(a, sln.removeDuplicates(a))
