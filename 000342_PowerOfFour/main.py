from typing import List


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        if n <= 3:
            return False

        while n > 1:
            if n % 4 == 0:
                n = n >> 2
                continue
            return False

        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.isPowerOfFour(16))
    print(sln.isPowerOfFour(0))
    print(sln.isPowerOfFour(5))
    print(sln.isPowerOfFour(1))
    print(sln.isPowerOfFour(2))
    print(sln.isPowerOfFour(3))