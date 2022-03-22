from typing import List


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x > 0 or y > 0:
            if x % 2 == 1 and y % 2 == 0:
                cnt += 1
            elif x % 2 == 0 and y % 2 == 1:
                cnt += 1
            x >>= 1
            y >>= 1
        return cnt


if __name__ == "__main__":
    sln = Solution()
    print(sln.hammingDistance(1, 4))
    print(sln.hammingDistance(3, 1))