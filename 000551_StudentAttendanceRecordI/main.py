from typing import List


class Solution:
    def checkRecord(self, s: str) -> bool:
        return sum([1 if c == 'A' else 0 for c in s]) < 2 and "LLL" not in s


if __name__ == "__main__":
    sln = Solution()
    print(sln.checkRecord("PPALLP"))
    print(sln.checkRecord("PPALLL"))