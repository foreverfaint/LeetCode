from typing import List


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        if n == 1:
            return True

        while n > 1:
            if n % 3 == 0:
                n = n // 3
                continue
            return False

        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.isPowerOfThree(27))
    print(sln.isPowerOfThree(0))
    print(sln.isPowerOfThree(9))
    print(sln.isPowerOfThree(1))
    print(sln.isPowerOfThree(2))
    print(sln.isPowerOfThree(4))