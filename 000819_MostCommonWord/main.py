from typing import List
from re import split


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [w for w in split("\W", paragraph.lower()) if w]
        words = [w for w in words if w not in banned]
        f = {}
        for w in words:
            f.setdefault(w, 0)
            f[w] += 1

        max_w = None
        max_f = 0
        for w, freq in f.items():
            if freq > max_f:
                max_f = freq
                max_w = w
        return max_w


if __name__ == "__main__":
    sln = Solution()
    print(sln.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
    print(sln.mostCommonWord(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
    print(sln.mostCommonWord(paragraph = "a.", banned = []))