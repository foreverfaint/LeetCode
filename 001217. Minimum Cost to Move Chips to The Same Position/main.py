from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = len([p for p in position if p % 2 == 1])
        even = len([p for p in position if p % 2 == 0])
        return min(odd, even)


if __name__ == "__main__":
    sln = Solution()
    print(sln.minCostToMoveChips([1,2,3]))
    print(sln.minCostToMoveChips([2,2,2,3,3]))
    print(sln.minCostToMoveChips([1,1000000000]))