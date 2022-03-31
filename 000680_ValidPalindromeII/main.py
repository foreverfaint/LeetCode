from typing import List


class Solution:
    def isPalindrome(self, s: str):
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                break
            i += 1
            j -= 1

        if i >= j:
            return True

        ii = i + 1
        jj = j
        while ii < jj:
            if s[ii] != s[jj]:
                break
            ii += 1
            jj -= 1

        if ii >= jj:
            return True

        ii = i
        jj = j - 1
        while ii < jj:
            if s[ii] != s[jj]:
                return False
            ii += 1
            jj -= 1
        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.validPalindrome("aba"))
    print(sln.validPalindrome("abca"))
    print(sln.validPalindrome("abc"))