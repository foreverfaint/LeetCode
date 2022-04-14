from typing import List


class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        for i, n in enumerate(s):
            if n == "6":
                return int(s[:i] + "9" + s[i+1:])
        return num


if __name__ == "__main__":
    sln = Solution()
    print(sln.maximum69Number(9669))
    print(sln.maximum69Number(9996))
    print(sln.maximum69Number(9999))