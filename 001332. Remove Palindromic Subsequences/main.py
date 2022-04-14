from typing import List


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == s[::-1] else 2


if __name__ == "__main__":
    sln = Solution()
    print(sln.removePalindromeSub("ababa"))
    print(sln.removePalindromeSub("abb"))
    print(sln.removePalindromeSub("baabb"))