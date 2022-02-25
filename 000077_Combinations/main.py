from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == 1:
            return [[1]]

        if k == 1:
            return [[x + 1] for x in range(n)]

        r = [[n] + lst for lst in self.combine(n - 1, k -1)]
        if n - 1 >= k:
            r += self.combine(n - 1, k)
        return r


if __name__ == "__main__":
    sln = Solution()
    print(sln.combine(1, 1))
    print(sln.combine(2, 1))
    print(sln.combine(4, 2))