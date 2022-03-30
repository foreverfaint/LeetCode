
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = len(nums)
        s = set()
        dup = None
        sum_ = 0
        for n in nums:
            sum_ += n
            if n in s:
                dup = n
            s.add(n)

        return [dup, (1 + l) * l // 2 - sum_ + dup]


if __name__ == "__main__":
    sln = Solution()
    print(sln.findErrorNums([1,2,2,4]))
    print(sln.findErrorNums([1,1]))