from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_l = 0
        max_pos = 0
        max_neg = 0
        for n in nums:
            if n > 0:
                max_pos, max_neg = max_pos + 1, max_neg + 1 if max_neg > 0 else 0
            elif n < 0:
                max_pos, max_neg = max_neg + 1 if max_neg > 0 else 0, max_pos + 1
            else:
                max_pos, max_neg = 0, 0
            max_l = max(max_pos, max_l)
            i += 1

        return max_l


if __name__ == "__main__":
    sln = Solution()
    print(sln.getMaxLen([-1,2]))
    print(sln.getMaxLen([1,-2,-3,4]))
    print(sln.getMaxLen([0,1,-2,-3,-4]))
    print(sln.getMaxLen([-1,-2,-3,0,1]))