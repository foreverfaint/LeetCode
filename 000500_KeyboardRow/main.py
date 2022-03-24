from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set(list("qwertyuiop"))
        s2 = set(list("asdfghjkl"))
        s3 = set(list("zxcvbnm"))

        def _foo(s):
            ss = set(list(s.lower()))
            return len(ss - s1) == 0 or len(ss - s2) == 0 or len(ss - s3) == 0

        return [s for s in words if _foo(s)]


if __name__ == "__main__":
    sln = Solution()
    print(sln.findWords(["Hello","Alaska","Dad","Peace"]))
    print(sln.findWords(["omk"]))
    print(sln.findWords(["adsdf","sfd"]))