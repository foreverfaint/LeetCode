from typing import List


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        i = 2
        while True:
            x = i ** 2
            if num < x:
                return False

            while num % x == 0:
                num = num // x

            if num == 1:
                return True
            i += 1


if __name__ == "__main__":
    sln = Solution()
    print(sln.isPerfectSquare(16))
    print(sln.isPerfectSquare(14))
    print(sln.isPerfectSquare(81))
    print(sln.isPerfectSquare(2000105819))