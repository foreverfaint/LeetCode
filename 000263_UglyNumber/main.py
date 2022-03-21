from typing import List


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            print(n)
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            elif n % 5 == 0:
                n = n // 5
            else:
                return False
        return True


if __name__ == "__main__":
    sln = Solution()
    # print(sln.isUgly(6))
    # print(sln.isUgly(1))
    # print(sln.isUgly(14))
    print(sln.isUgly(-2147483648))