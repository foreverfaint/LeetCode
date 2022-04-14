from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([n for n in nums if len(str(n)) % 2 == 0])


if __name__ == "__main__":
    sln = Solution()
    print(sln.findNumbers([12,345,2,6,7896]))
    print(sln.findNumbers([555,901,482,1771]))