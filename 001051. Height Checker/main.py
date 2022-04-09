from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        return len([x for x, y in zip(heights, expected) if x != y])


if __name__ == "__main__":
    sln = Solution()
    print(sln.heightChecker([1,1,4,2,1,3]))
    print(sln.heightChecker([5,1,2,3,4]))
    print(sln.heightChecker([1,2,3,4,5]))