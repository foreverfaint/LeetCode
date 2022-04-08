from typing import List


class Solution:
    def foo(self, s, low, high):
        if len(s) == 0:
            return [low]
        if s[0] == "I":
            return [low] + self.foo(s[1:], low + 1, high)
        return [high] + self.foo(s[1:], low, high - 1)

    def diStringMatch(self, s: str) -> List[int]:
        return self.foo(s, 0, len(s))


if __name__ == "__main__":
    sln = Solution()
    print(sln.diStringMatch("IDID"))
    print(sln.diStringMatch("III"))
    print(sln.diStringMatch("DDI"))