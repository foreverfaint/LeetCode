
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n in s:
                return n
            s.add(n)


if __name__ == "__main__":
    sln = Solution()
    print(sln.findDuplicate([2,2,2,2,2]))
    print(sln.findDuplicate([1,3,4,2,2]))
    print(sln.findDuplicate([3,1,3,4,2]))