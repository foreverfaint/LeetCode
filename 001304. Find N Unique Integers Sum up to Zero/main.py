from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [1, -1]
        if n == 3:
            return [1, 0, -1]
        return [n, -n] + self.sumZero(n - 2)


if __name__ == "__main__":
    sln = Solution()
    print(sln.sumZero(5))
    print(sln.sumZero(3))
    print(sln.sumZero(1))