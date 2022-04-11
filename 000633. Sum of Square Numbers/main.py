from typing import List


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for x in range(0, c + 1):
            x_2 = x * x
            if x_2 == c or x_2 + x_2 == c:
                # y == 0 or x == y
                return True
            elif x_2 > c:
                return False
            y_2 = c - x_2
            import math
            y = int(math.sqrt(y_2))
            if y * y == y_2:
                return True
        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.judgeSquareSum(0))
    print(sln.judgeSquareSum(1))
    print(sln.judgeSquareSum(5))
    print(sln.judgeSquareSum(3))
    print(sln.judgeSquareSum((2 ** 21) * (2 ** 21)  + (3 ** 21) * (3 ** 21)))