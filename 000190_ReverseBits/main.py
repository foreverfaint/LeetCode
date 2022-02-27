from typing import List


class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0
        i = 0
        while n > 0:
            r = r << 1
            i += 1
            if n % 2 == 1:
                r += 1
            n = n >> 1
        while i < 32:
            r = r << 1
            i += 1
        return r


if __name__ == "__main__":
    sln = Solution()
    # print(sln.reverseBits(0b1))
    # print(sln.reverseBits(0b10))
    # print(sln.reverseBits(0b11))
    # print(sln.reverseBits(0b100))
    print(sln.reverseBits(0b00000010100101000001111010011100))
    # print(sln.reverseBits(0b11111111111111111111111111111101))