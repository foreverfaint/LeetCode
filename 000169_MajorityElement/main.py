from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        n = nums[0]
        c = 1
        i = 1
        while i < l:
            if n is None:
                n = nums[i]
                c = 1
            elif n == nums[i]:
                c += 1
            else:
                c -= 1
                if c == 0:
                    n = None
            i += 1
        return n


if __name__ == "__main__":
    sln = Solution()
    print(sln.majorityElement([3,2,3]))
    print(sln.majorityElement([2,2,1,1,1,2,2]))