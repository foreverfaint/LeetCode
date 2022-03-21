from typing import List


class Solution:
    def countSegments(self, s: str) -> int:
        c = 0
        for i in range(1, len(s)):
            if s[i - 1] != " " and s[i] == " ":
                c += 1

        if s and s[-1] != " ":
            c += 1

        return c


if __name__ == "__main__":
    sln = Solution()
    print(sln.countSegments("Hello, my name is John"))
    print(sln.countSegments("Hello"))
    print(sln.countSegments("Hello "))
    print(sln.countSegments(" Hello"))
    print(sln.countSegments("   "))