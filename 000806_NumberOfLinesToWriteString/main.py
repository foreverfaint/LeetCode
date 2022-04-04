from typing import List


class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 0
        sum_width = 0
        for c in s:
            width = widths[ord(c) - ord('a')]
            sum_width += width
            if sum_width > 100:
                lines += 1
                sum_width = width
        return [lines + 1, sum_width]


if __name__ == "__main__":
    sln = Solution()
    print(sln.numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"))
    print(sln.numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))