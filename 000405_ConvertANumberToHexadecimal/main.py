from typing import List


class Solution:
    max_ = 1 << 32

    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        if num < 0:
            num = self.max_ + num

        s = ""
        while num:
            x = num % 16
            s = (str(x) if x < 10 else "abcdef"[(x - 10)]) + s
            num = (num - x) // 16
        return s

    # def toHex(self, num):
    #     ans = []
    #     dic = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
    #     if num == 0:
    #         return "0"
    #     if num < 0:
    #         num = num + 2**32

    #     while num > 0:
    #         digit = num % 16
    #         num = int((num-digit)/16)
    #         print(num)
    #         ans.append(dic[digit] if  digit > 9 and digit < 16 else str(digit))
    #     return "".join(ans[::-1])


if __name__ == "__main__":
    sln = Solution()
    print(sln.toHex(26))
    print(sln.toHex(-1))
    print(sln.toHex(-2))