from typing import List


class Solution:
    def _f(self, s, wordDict, mem) -> bool:
        l = len(s)
        while l >= 1:
            if s[:l] in wordDict:
                if len(s) == l:
                    return True

                ss = s[l:]

                can_break = mem.get(ss)
                if can_break is None:
                    can_break = self._f(ss, wordDict, mem)
                    mem[ss] = can_break

                if can_break:
                    return True
            l -= 1
        return False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = {}
        return self._f(s, set(wordDict), mem)


if __name__ == "__main__":
    sln = Solution()
    print(sln.wordBreak("abcd", ["a","abc", "b", "cd"]))
    print(sln.wordBreak("aaaaaaa", ["aaaa","aaa"]))
    print(sln.wordBreak("leetcode", ["leet","code"]))
    print(sln.wordBreak("applepenapple", ["apple","pen"]))
    print(sln.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))