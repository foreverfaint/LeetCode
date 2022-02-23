from typing import List


class Solution:
    m = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    def _gen(self, result: List[str], s: str, digits: str):
        if len(digits) == 0:
            if len(s) > 0:
                result.append(s)
            return

        for c in self.m[digits[0]]:
            self._gen(result, s + c, digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        r = []
        self._gen(r, "", digits)
        return r


if __name__ == "__main__":
    sln = Solution()
    print(sln.letterCombinations("23"))
    print(sln.letterCombinations(""))
    print(sln.letterCombinations("2"))