from typing import List


class Solution:
    def hammingWeight(self, n: int) -> int:
        r = 0
        while n:
            i = n % 2
            if i == 1:
                r += 1
            n = n >> 1
        return r


if __name__ == "__main__":
    sln = Solution()
    print(sln.hammingWeight(0b00000000000000000000000000001011))
    print(sln.hammingWeight(0b00000000000000000000000010000000))
    print(sln.hammingWeight(0b11111111111111111111111111111101))