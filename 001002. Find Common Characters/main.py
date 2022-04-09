
from typing import List


class Solution:
    def foo(self, word):
        m = {}
        for c in word:
            m.setdefault(c, 0)
            m[c] += 1
        return m

    def commonChars(self, words: List[str]) -> List[str]:
        m_list = [self.foo(w) for w in words]
        import itertools
        ans = []
        for c in set(list(itertools.chain(*[list(m.keys()) for m in m_list]))):
            f = min([m.get(c, 0) for m in m_list])
            while f > 0:
                ans.append(c)
                f -= 1
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.commonChars(["bella","label","roller"]))
    print(sln.commonChars(["cool","lock","cook"]))