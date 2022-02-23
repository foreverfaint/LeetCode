class Solution:
    def _reverse(self, s, i, j):
        while i < j:
            t = s[i]
            s[i] = s[j]
            s[j] = t
            i += 1
            j -= 1

    def reverseWords(self, s: str) -> str:
        s = list(iter(s))
        self._reverse(s, 0, len(s) - 1)

        i = 0
        start = 0
        end = 0
        l = len(s)
        while i < l:
            if s[i] != " ":
                if i == 0 or s[i-1] == " ":
                    start = i
            else:
                if i > 0  and s[i - 1] != " ":
                    self._reverse(s, start, i - 1)

            i += 1

        if s[i - 1] != " ":
            self._reverse(s, start, i - 1)

        self._reverse(s, 0, len(s) - 1)
        return "".join(s)


if __name__ == "__main__":
    sln = Solution()
    print(sln.reverseWords("Let's"))
    print(sln.reverseWords("Let's "))
    print(sln.reverseWords("Let's  Go"))
    print(sln.reverseWords("Let's take LeetCode contest"))
    print(sln.reverseWords("God Ding"))