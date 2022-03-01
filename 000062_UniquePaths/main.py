from typing import List


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        p = [1] * n
        y = 1
        while y < m:
            x = 1
            while x < n:
                p[x] = p[x - 1] + p[x]
                x += 1
            y += 1
        return p[-1]
                



if __name__ == "__main__":
    sln = Solution()
    print(sln.uniquePaths(1, 10))
    print(sln.uniquePaths(3, 7))
    print(sln.uniquePaths(3, 2))