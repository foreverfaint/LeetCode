from typing import List


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def is_all_lower(s):
            return all(ord('a') <= ord(c) <= ord('z') for c in s)

        def is_all_upper(s):
            return all(ord('A') <= ord(c) <= ord('Z') for c in s)

        return is_all_lower(word) or is_all_upper(word) or (ord('A') <= ord(word[0]) <= ord('Z') and is_all_lower(word[1:]))


if __name__ == "__main__":
    sln = Solution()
    print(sln.detectCapitalUse("USA"))
    print(sln.detectCapitalUse("FlaG"))