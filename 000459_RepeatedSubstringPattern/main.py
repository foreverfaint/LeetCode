from typing import List


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = 1
        while l <= len(s) // 2:
            if len(s) % l == 0:
                n = len(s) // l
                if s == s[:l] * n:
                    return True
            l += 1
        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.repeatedSubstringPattern("abab"))
    print(sln.repeatedSubstringPattern("aba"))
    print(sln.repeatedSubstringPattern("abcabcabcabc"))