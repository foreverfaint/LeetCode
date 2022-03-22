from typing import List


class Solution:
    def findComplement(self, num: int) -> int:
        ans = []
        while num > 0:
            ans.append(1 if num % 2 == 0 else 0)
            num >>= 1

        s = 0
        for i in range(len(ans) - 1, -1, -1):
            s = (s << 1) + ans[i]
        return s


if __name__ == "__main__":
    sln = Solution()
    print(sln.findComplement(5))
    print(sln.findComplement(2))
    print(sln.findComplement(1))