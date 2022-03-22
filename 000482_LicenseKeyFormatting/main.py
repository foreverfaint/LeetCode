from typing import List
import string

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        alphanumberic = string.ascii_letters + "0123456789"
        c_i = 0
        ans = ""
        for i in range(len(s)):
            p = len(s) - 1 - i
            if s[p] in alphanumberic:
                if c_i % k == 0 and ans != "":
                    ans = "-" + ans
                ans = s[p].upper() + ans
                c_i += 1
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.licenseKeyFormatting("5F3Z-2e-9-w", 4))
    print(sln.licenseKeyFormatting("2-5g-3-J", 2))