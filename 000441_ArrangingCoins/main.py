from typing import List


class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        s = i
        while s < n:
            i += 1
            s += i
        return i if s == n else i - 1


if __name__ == "__main__":
    sln = Solution()
    print(sln.arrangeCoins(0))
    print(sln.arrangeCoins(1))
    print(sln.arrangeCoins(3))
    print(sln.arrangeCoins(5))
    print(sln.arrangeCoins(8))