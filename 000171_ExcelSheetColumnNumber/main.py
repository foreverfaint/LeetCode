from typing import List


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        import string
        m = {c: i + 1 for i, c in enumerate(string.ascii_uppercase)}
        r = 0
        for c in columnTitle:
            r = r * 26 + m[c]
        return r



if __name__ == "__main__":
    sln = Solution()
    print(sln.titleToNumber("A"))
    print(sln.titleToNumber("AB"))
    print(sln.titleToNumber("ZY"))