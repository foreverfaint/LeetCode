from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split(" ")
        i = 0
        l = len(words)
        ans = []
        while i < l - 2:
            if words[i] == first and words[i + 1] == second:
                ans.append(words[i + 2])
            i += 1
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good"))
    print(sln.findOcurrences(text = "we will we will rock you", first = "we", second = "will"))
    