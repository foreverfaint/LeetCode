from typing import List


class Solution:
    def wb(self, w):
        m = {}
        for c in w:
            m.setdefault(c, 0)
            m[c] += 1
        return m

    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_wb = self.wb(chars)
        return sum([len(w) for w in words if all([cnt <= chars_wb.get(c, 0) for c, cnt in self.wb(w).items()])])


if __name__ == "__main__":
    sln = Solution()
    print(sln.countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
    print(sln.countCharacters(words = ["hello","world","leetcode"], chars = "welldonehoneyr"))