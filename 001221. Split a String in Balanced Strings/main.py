from typing import List


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l = 0
        r = 0
        ans = 0
        for n in s:
            if n == "L":
                l += 1
            elif n == "R":
                r += 1
            if l == r and l != 0:
                ans += 1
                l = 0
                r = 0
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.balancedStringSplit("RLRRLLRLRL"))
    print(sln.balancedStringSplit("RLLLLRRRLR"))
    print(sln.balancedStringSplit("LLLLRRRR"))