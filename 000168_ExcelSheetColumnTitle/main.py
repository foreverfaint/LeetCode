from typing import List


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        import string
        m = {i: x for i, x in enumerate(string.ascii_uppercase)}
        s = ""
        while columnNumber > 0:
            d = (columnNumber - 1) % 26
            s = m[d] + s
            columnNumber = (columnNumber - 1) // 26
        return s


if __name__ == "__main__":
    sln = Solution()
    print(sln.convertToTitle(1))
    print(sln.convertToTitle(28))
    print(sln.convertToTitle(701))