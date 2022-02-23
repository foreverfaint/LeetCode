from typing import List


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        c_1 = Counter(iter(ransomNote))
        c_2 = Counter(iter(magazine))
        for c, n1 in c_1.items():
            n2 = c_2.get(c)
            if not n2 or n2 < n1:
                return False
        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.canConstruct("a", "b"))
    print(sln.canConstruct("aa", "ab"))
    print(sln.canConstruct("aa", "aab"))