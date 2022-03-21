from typing import List


class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
        # if n <= 3:
        #     return True
        # win_0 = True
        # win_1 = True
        # win_2 = True
        # for _ in range(3, n):
        #     win_0, win_1, win_2 = win_1, win_2, (not win_0) or (not win_1) or (not win_2)
        # return win_2


if __name__ == "__main__":
    sln = Solution()
    print(sln.canWinNim(4))
    print(sln.canWinNim(1))
    print(sln.canWinNim(2))
    