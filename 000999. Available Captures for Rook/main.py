from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        h = len(board)
        w = len(board[0])

        rock_x = 0
        rock_y = 0
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if val == "R":
                    rock_x = x
                    rock_y = y

        ans = 0

        x = rock_x
        while x >= 0:
            if board[rock_y][x] == "B":
                break
            if board[rock_y][x] == "p":
                ans += 1
                break
            x -= 1
        
        x = rock_x
        while x < w:
            if board[rock_y][x] == "B":
                break
            if board[rock_y][x] == "p":
                ans += 1
                break
            x += 1

        y = rock_y
        while y >= 0:
            if board[y][rock_x] == "B":
                break
            if board[y][rock_x] == "p":
                ans += 1
                break
            y -= 1
        
        y = rock_y
        while y < h:
            if board[y][rock_x] == "B":
                break
            if board[y][rock_x] == "p":
                ans += 1
                break
            y += 1

        return ans




if __name__ == "__main__":
    sln = Solution()
    print(sln.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
    print(sln.numRookCaptures([[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]))
    print(sln.numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]))