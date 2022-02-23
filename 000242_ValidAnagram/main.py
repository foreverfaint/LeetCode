from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        c_1 = Counter(iter(s))
        c_2 = Counter(iter(t))
        return c_1 == c_2

if __name__ == "__main__":
    sln = Solution()
    print(sln.isAnagram("anagram", "nagaram"))
    print(sln.isAnagram("rat", "car"))