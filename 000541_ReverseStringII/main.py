from audioop import reverse
from typing import List


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        for i in range(len(s)):
            g = i // k
            if g % 2 == 0:
                g_start = g * k
                g_l = min(k, len(s) - g_start) - 1
                # print(g, i, g_start + g_l - (i % k), ans)
                ans += s[g_start + g_l - (i % k)]
            else:
                ans += s[i]
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.reverseStr("abcdefg", 3))
    print(sln.reverseStr("a", 2))
    print(sln.reverseStr("abcdefg", 2))
    print(sln.reverseStr("abcd", 2))