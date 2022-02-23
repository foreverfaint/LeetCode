
class Solution:
    inf = pow(2, 31)

    def reverse(self, x: int) -> int:
        s = str(x)
        neg = False
        if x < 0:
            neg = True
            s = s[1:]

        s = list(iter(s))
        s.reverse()
        s = "".join(s)

        y = int(s)
        if neg:
            return 0 if y > self.inf else -y
        else:
            return 0 if y > (self.inf - 1) else y


if __name__ == "__main__":
    assert 321 == Solution().reverse(123)
    assert -321 == Solution().reverse(-123)
    assert 21== Solution().reverse(120)