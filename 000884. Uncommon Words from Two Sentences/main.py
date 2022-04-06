from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wl1 = {}
        for w in s1.split(" "):
            wl1.setdefault(w, 0)
            wl1[w] += 1

        wl2 = {}
        for w in s2.split(" "):
            wl2.setdefault(w, 0)
            wl2[w] += 1

        wl1_ = set([w for w, f in wl1.items() if w not in wl2 and f == 1])
        wl2_ = set([w for w, f in wl2.items() if w not in wl1 and f == 1])
        return wl1_.union(wl2_)


if __name__ == "__main__":
    sln = Solution()
    print(sln.uncommonFromSentences(s1 = "s z z z s", s2 = "s z ejt"))
    print(sln.uncommonFromSentences(s1 = "this apple is sweet", s2 = "this apple is sour"))
    print(sln.uncommonFromSentences(s1 = "apple apple", s2 = "banana"))