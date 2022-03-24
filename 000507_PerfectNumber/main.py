from typing import List


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        import math
        s = 0
        for i in range(1, math.ceil(math.sqrt(num))):
            if num % i == 0:
                if i != num:
                    s += i
                if num // i != num:
                    s += num // i
                if s > num:
                    break
        return s == num


if __name__ == "__main__":
    sln = Solution()
    print(sln.checkPerfectNumber(28))
    print(sln.checkPerfectNumber(7))
    print(sln.checkPerfectNumber(6))