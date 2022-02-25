from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if len(s) == 1:
            if 'a' <= s[0] <= 'z' or 'A' <= s[0] <= 'Z':
                return [s[0].lower(), s[0].upper()]
            return s[0]

        r = []
        if 'a' <= s[0] <= 'z' or 'A' <= s[0] <= 'Z':
            for sub_s in self.letterCasePermutation(s[1:]):
                r.append(s[0].lower() + sub_s)
                r.append(s[0].upper() + sub_s)
        else:
            for sub_s in self.letterCasePermutation(s[1:]):
                r.append(s[0] + sub_s)
        return r


if __name__ == "__main__":
    sln = Solution()
    print(sln.letterCasePermutation("a1b2"))
    print(sln.letterCasePermutation("3z4"))