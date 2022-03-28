from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        import math
        nums = [x * x for x in range(1, math.ceil(math.sqrt(n)) + 1) if x * x <= n]

        m = {0: 0, 1: 1, 2: 2}
        for i in range(2, n + 1):
            s = []
            for x in [x for x in nums if x <= i]:
                s.append(m[i - x])
            m[i] = min(s) + 1

        return m[n]


if __name__ == "__main__":
    sln = Solution()
    print(sln.numSquares(4))
    # print(sln.numSquares(6))
    # print(sln.numSquares(12))
    # print(sln.numSquares(13))