from typing import List


class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2:
            return 1

        pro = [0] * (n + 1)
        pro[1] = 1
        pro[2] = 1

        for i in range(3, n + 1):
            for j in range(1, i):
                pro[i] = max(pro[i], j * (i - j), j * pro[i - j])
        return pro[-1]


if __name__ == "__main__":
    sln = Solution()
    print(sln.integerBreak(2))
    print(sln.integerBreak(10))
