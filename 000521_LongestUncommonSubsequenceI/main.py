from typing import List


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return max(len(a), len(b))
        return -1 if a == b else len(a)


if __name__ == "__main__":
    sln = Solution()
    print(sln.findLUSlength("aba", "cdc"))
    print(sln.findLUSlength("aaa", "bbb"))
    print(sln.findLUSlength("aaa", "aaa"))
    print(sln.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))
