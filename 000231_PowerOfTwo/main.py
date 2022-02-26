from typing import List


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 2 == 1:
                return False
            n = n >> 1

        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.isPowerOfTwo(1))
    print(sln.isPowerOfTwo(16))
    print(sln.isPowerOfTwo(3))