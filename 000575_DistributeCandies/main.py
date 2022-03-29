from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = set(candyType)
        half = len(candyType) // 2
        types = len(s)
        return types if types < half else half


if __name__ == "__main__":
    sln = Solution()
    print(sln.distributeCandies([1,1,2,2,3,3]))
    print(sln.distributeCandies([1,1,2,3]))
    print(sln.distributeCandies([6,6,6,6]))