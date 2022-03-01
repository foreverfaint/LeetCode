from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while True:
            s = 0
            
            while n > 0:
                digit = n % 10
                s += digit * digit
                n = n // 10

            if s == 1:
                return True

            if s in cache:
                return False

            cache.add(s)

            n = s


if __name__ == "__main__":
    sln = Solution()
    print(sln.isHappy(19))
    print(sln.isHappy(2))