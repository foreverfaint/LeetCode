from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        i = -1
        ll = [len(x) for x in strs]
        while True:
            i += 1

            if any(True for l in ll if i >= l):
                break

            c = strs[0][i]
            if any(True for x in strs if x[i] != c):
                break

        return "" if i == 0 else strs[0][:i]


if __name__ == "__main__":
    assert "" == Solution().longestCommonPrefix(["dog","racecar","car"])
    assert "" == Solution().longestCommonPrefix(["","flower","flow"])
    assert "fl" == Solution().longestCommonPrefix(["flower","flow","flight"])