class Solution:
    inf = pow(2, 31)

    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == "":
            return 0

        neg = False
        if s[0] == "-":
            neg = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        i = 0
        x = 0
        l = len(s)
        while i < l:
            c = s[i]
            if '0' <= c <= '9':
                x = 10 * x + int(c)
            else:
                break
            i += 1

        if neg:
            return -self.inf if x > self.inf else -x
        else:
            return (self.inf - 1) if x > (self.inf - 1) else x


if __name__ == "__main__":
    assert 0 == Solution().myAtoi("")
    assert 42 == Solution().myAtoi("42")
    assert -42 == Solution().myAtoi("   -42")
    assert 4193 == Solution().myAtoi("4193 with words")