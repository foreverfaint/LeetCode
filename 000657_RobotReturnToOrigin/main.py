from typing import List


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0
        y = 0
        for move in moves:
            if move == "R":
                x += 1
            elif move == "L":
                x -= 1
            elif move == "U":
                y -= 1
            elif move == "D":
                y += 1
        return x == 0 and y == 0


if __name__ == "__main__":
    sln = Solution()
    print(sln.judgeCircle("UD"))
    print(sln.judgeCircle("LL"))