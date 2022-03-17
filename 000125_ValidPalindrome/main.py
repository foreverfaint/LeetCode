from typing import List


def isPalindrome(s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            c1 = s[i].lower()
            if not c1.isalnum():
                i += 1
                continue

            c2 = s[j].lower()
            if not c2.isalnum():
                j -= 1
                continue

            if c1 != c2:
                return False

            i += 1
            j -= 1

        return True


if __name__ == "__main__":
    print(isPalindrome("0P"))
    sln = Solution()
    print(sln.isPalindrome("0P"))
    print(sln.isPalindrome("A man, a plan, a canal: Panama"))
    print(sln.isPalindrome("race a car"))
    print(sln.isPalindrome(" "))