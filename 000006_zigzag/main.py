class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        loc = []
        stride_x = numRows * 2 - 2
        for i, c in enumerate(s):
            n1 = i // stride_x
            n2 = i % stride_x
            if n2 < numRows:
                x = n1 * (numRows - 1)
                y = n2
            else:
                x = n1 * (numRows - 1) + n2 - numRows + 1
                y = numRows * 2 - n2 - 2
            loc.append((x, y, c))

        k = ""
        for r in range(numRows):
            s = ""
            for x, y, c in [xyc for xyc in loc if xyc[1] == r]:
                s += " " * (x - len(s)) + c
                k += c
            # print(s)
        return k


if __name__ == "__main__":
    assert "PAHNAPLSIIGYIR" == Solution().convert("PAYPALISHIRING", 3)
    assert "PINALSIGYAHRPI" == Solution().convert("PAYPALISHIRING", 4)
    assert "A" == Solution().convert("A", 1)