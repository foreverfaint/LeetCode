from typing import List, Set


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = set()
        self._gen(r, "", 0, n, n)
        return list(r)

    def _gen(self, result: Set, s: str, sum_s: int, l: int, r: int):
        if sum_s < 0:
            return

        if l == 0 and r == 0:
            result.add(s)
            return

        if l > 0:
            self._gen(result, s + "(", sum_s + 1, l - 1, r)

        if r > 0:
            self._gen(result, s + ")", sum_s - 1, l, r - 1)


if __name__ == "__main__":
    sln = Solution()
    print(sln.generateParenthesis(6))
    print(sln.generateParenthesis(3))
    print(sln.generateParenthesis(1))