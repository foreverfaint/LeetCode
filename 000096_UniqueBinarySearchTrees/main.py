from typing import List


class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        cnt = [0] * (n + 1)
        cnt[0], cnt[1], cnt[2] = 1, 1, 2
        i = 3
        while i < n + 1:
            for j in range(i):
                cnt[i] += cnt[j] * cnt[i - 1 - j]
            i += 1
        return cnt[n]


if __name__ == "__main__":
    sln = Solution()
    print(sln.numTrees(19))
    print(sln.numTrees(3))
    print(sln.numTrees(1))