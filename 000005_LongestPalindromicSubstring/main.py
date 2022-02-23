class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)

        cache = [None for _ in range(l + 1)]
        for l_ in range(1, l + 1):
            if l_ == 1:
                cache[1] = [True for _ in range(0, l)]
            elif l_ == 2:
                cache[2] = [(s[start] == s[start + 1]) for start in range(0, l - 1)]
            else:
                cache[l_] = [((s[start] == s[start + l_ - 1]) and cache[l_ - 2][start + 1]) for start in range(0, l - l_ + 1)]

        for l_ in range(len(cache) - 1, 0, -1):
            for i, flag in enumerate(cache[l_]):
                if flag:
                    r = s[i:i+l_]
                    return r


if __name__ == "__main__":
    assert "b" == Solution().longestPalindrome("b")
    assert "bab" == Solution().longestPalindrome("babad")
    assert "bb" == Solution().longestPalindrome("cbbd")