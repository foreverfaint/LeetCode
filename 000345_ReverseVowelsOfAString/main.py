from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        ans = list(s)
        while i < j:
            if ans[i] not in "aeiouAEIOU":
                i += 1
            elif ans[j] not in "aeiouAEIOU":
                j -= 1
            else:
                ans[i], ans[j] = ans[j], ans[i]
                i += 1
                j -= 1
        return "".join(ans)



if __name__ == "__main__":
    sln = Solution()
    print(sln.reverseVowels("aA"))
    print(sln.reverseVowels("hello"))
    print(sln.reverseVowels("leetcode"))