from typing import List


class Solution:
    def binaryGap(self, n: int) -> int:
        ans = []
        i = 0
        while n > 0:
            if n % 2 == 1:
                ans.append(i)
            n = n >> 1
            i += 1
        if len(ans) <= 1:
            return 0

        max_ = 0
        for i in range(1, len(ans)):
            max_ = max(max_, ans[i] - ans[i - 1])
        return max_


if __name__ == "__main__":
    sln = Solution()
    print(sln.binaryGap(22))
    print(sln.binaryGap(8))
    print(sln.binaryGap(5))