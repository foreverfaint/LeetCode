from typing import List


class Solution:
    def generateTheString(self, n: int) -> str:
        return "a" * n if n % 2 == 1 else "a" * (n - 1) + "b"


if __name__ == "__main__":
    sln = Solution()
    print(sln.generateTheString(4))
    print(sln.generateTheString(2))
    print(sln.generateTheString(7))