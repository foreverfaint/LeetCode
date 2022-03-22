from typing import List
import string


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        if n == 0:
            return ""
        x = k - (n - 1)
        if x <= 0:
            return None
        x = min(26, x)
        return self.getSmallestString(n - 1, k - x) + string.ascii_lowercase[x - 1]


if __name__ == "__main__":
    sln = Solution()
    print(sln.getSmallestString(3, 27))
    print(sln.getSmallestString(5, 73))