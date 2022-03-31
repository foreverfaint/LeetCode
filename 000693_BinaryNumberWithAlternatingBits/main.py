from typing import List


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        last_bit = None
        while n > 0:
            if last_bit is None:
                last_bit = n % 2
            elif last_bit == n % 2:
                return False
            else:
                last_bit = 1 - last_bit
            n = n >> 1
        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.hasAlternatingBits(5))
    print(sln.hasAlternatingBits(7))
    print(sln.hasAlternatingBits(11))