from typing import List


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum([int(x) for x in str(num)])
        return num


if __name__ == "__main__":
    sln = Solution()
    print(sln.addDigits(38))
    print(sln.addDigits(0))