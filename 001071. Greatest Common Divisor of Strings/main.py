from typing import List


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)
        import math
        gcd_l = math.gcd(l1, l2)
        gcd_s = str1[:gcd_l]
        return gcd_s if str1 == gcd_s * (l1 // gcd_l) and str2 == gcd_s * (l2 // gcd_l) else ""


if __name__ == "__main__":
    sln = Solution()
    print(sln.gcdOfStrings(str1 = "ABCABC", str2 = "ABC"))
    print(sln.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB"))
    print(sln.gcdOfStrings(str1 = "LEET", str2 = "CODE"))