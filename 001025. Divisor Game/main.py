from typing import List


class Solution:
    def divisorGame(self, n: int) -> bool:
        m = [False] * (n + 1)

        for k in range(2, n + 1):
            for i in range(1, k):
                if k % i == 0 and not m[k - i]:
                    m[k] = True
                    break

        return m[n]


if __name__ == "__main__":
    sln = Solution()
    print(sln.divisorGame(2))
    print(sln.divisorGame(3))