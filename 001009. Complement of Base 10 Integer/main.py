from typing import List


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        bits = []
        while n > 0:
            bits.append(1 - n % 2)
            n >>= 1

        bits.reverse()

        ans = 0
        for bit in bits:
            ans <<= 1
            ans += bit
        return ans
        


if __name__ == "__main__":
    sln = Solution()
    print(sln.bitwiseComplement(5))
    print(sln.bitwiseComplement(7))
    print(sln.bitwiseComplement(10))