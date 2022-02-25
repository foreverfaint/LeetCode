from typing import List


class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0

        r_1 = 1 if s[0] != '0' else 0
        if len(s) == 1:
            return r_1

        r_2 = r_1 
        r_2 += -1 if s[1] == '0' else 0
        r_2 += 1 if 10 <= int(s[:2]) <= 26 else 0
        if len(s) == 2:
            return max(0, r_2)
        
        i = 2
        print(i, r_1, r_2)
        while i < len(s):
            if s[i] == '0' and (s[i - 1] == '0' or s[i - 1] > '2'):
                return 0
            elif s[i - 1] == '0':
                r = r_2
            elif s[i] == '0':
                r = r_1
            else:
                r = r_2 + (r_1 if 10 <= int(s[i-1:i+1]) <= 26 else 0)
            r_1, r_2 = r_2, r
            i += 1
            print(i, r_1, r_2)
        return r


if __name__ == "__main__":
    sln = Solution()

    print(sln.numDecodings("1123"))
    print(sln.numDecodings("1201234"))
    print(sln.numDecodings("00"))
    print(sln.numDecodings("10"))
    print(sln.numDecodings("12"))
    print(sln.numDecodings("226"))
    print(sln.numDecodings("06"))