from typing import List


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = []
        for i in range(1, len(s)):
            if s[i - 1] != s[i]:
                ans.append((i - 1, i))

        sum_ = len(ans)
        for l in range(4, len(s) + 1, 2):
            tmp = []
            for l, r in ans:
                if l - 1 >=0 and r + 1 < len(s) and s[l - 1] == s[l] and s[r+1] == s[r]:
                    tmp.append((l - 1, r + 1))
            ans= tmp
            sum_ += len(ans)
        return sum_


if __name__ == "__main__":
    sln = Solution()
    print(sln.countBinarySubstrings("1100"))
    # print(sln.countBinarySubstrings("00110011"))
    # print(sln.countBinarySubstrings("10101"))