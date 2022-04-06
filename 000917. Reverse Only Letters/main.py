from typing import List


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(iter(s))

        import string
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] in string.ascii_letters and s[j] in string.ascii_letters:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in string.ascii_letters:
                i += 1
            elif s[j] not in string.ascii_letters:
                j -= 1
            else:
                i += 1
                j -= 1
        return "".join(s)


if __name__ == "__main__":
    sln = Solution()
    print(sln.reverseOnlyLetters("ab-cd"))
    print(sln.reverseOnlyLetters("a-bC-dEf-ghIj"))
    print(sln.reverseOnlyLetters("Test1ng-Leet=code-Q!"))