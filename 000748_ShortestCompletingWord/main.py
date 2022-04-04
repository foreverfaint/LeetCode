
from typing import List


class Solution:
    def core(self, s):
        return "".join([c for c in s.lower() if 'a' <= c <= 'z'])

    def freq(self, s):
        m = {}
        for c in s:
            m.setdefault(c, 0)
            m[c] += 1
        return m

    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        m = self.freq(self.core(licensePlate))
        for w_f, _, w in sorted([(self.freq(w), len(w), w) for w in words], key=lambda kv: kv[1]):
            if all([w_f.get(c, 0) >= f for c, f in m.items()]):
                return w
        return None



if __name__ == "__main__":
    sln = Solution()
    print(sln.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))
    print(sln.shortestCompletingWord(licensePlate = "1s3 456", words = ["looks","pest","stew","show"]))