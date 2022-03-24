from typing import List


class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
            
        sign = num < 0
        num = abs(num)

        s = ""
        while num > 0:
            s = str(num % 7) + s
            num = num // 7
        return "-" + s if sign else s

if __name__ == "__main__":
    sln = Solution()
    print(sln.convertToBase7(100))
    print(sln.convertToBase7(-7))