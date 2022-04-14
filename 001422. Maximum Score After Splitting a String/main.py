from typing import List


class Solution:
    def maxScore(self, s: str) -> int:
        l = len(s)
        i = 0
        z = []
        o = []
        while i < l:
            b = 0 if len(z) == 0 else z[-1]
            z.append(b + 1 if s[i] == "0" else b)
            b = 0 if len(o) == 0 else o[-1]
            o.append(b + 1 if s[l - i - 1] == "1" else b)
            i += 1
        o.reverse()

        max_ = 0
        for i in range(1, l):
            max_ = max(max_, z[i - 1] + o[i])
        return max_


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxScore("011101"))
    print(sln.maxScore("00111"))
    print(sln.maxScore("1111"))