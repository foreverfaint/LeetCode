from typing import List


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while n > 0:
            digit = n % 10
            s += digit
            p *= digit
            n = n // 10
        return p - s


if __name__ == "__main__":
    sln = Solution()
    print(sln.subtractProductAndSum(234))
    print(sln.subtractProductAndSum(4421))