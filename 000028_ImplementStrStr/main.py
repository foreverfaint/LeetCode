class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(haystack)
        ll = len(needle)

        if ll == 0:
            return 0

        if l < ll:
            return -1

        m = [0 for _ in range(ll)]
        i = 0
        j = 1
        while j < ll:
            if needle[i] != needle[j]:
                if i != 0:
                    i = m[i - 1]
                else:
                    i = 0
                    j += 1
            else:
                m[j] = i + 1
                i += 1
                j += 1

        i = 0
        j = 0
        while i < l and j < ll:
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = m[j - 1]

        return (i - ll) if j == ll else -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.strStr("mississippi", "issip"))
    print(sln.strStr("aaaaaaaaaaaaaaaaaaaa", "acacabacacabacacac"))
    print(sln.strStr("", "ll"))
    print(sln.strStr("hello", ""))
    print(sln.strStr("hello", "llllll"))
    print(sln.strStr("hello", "ll"))
    print(sln.strStr("aaaaa", "bba"))
    print(sln.strStr("mississippi", "issipi"))
