from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[" "] * 3 for _ in range(3)]
        for i, (y, x) in enumerate(moves):
            board[y][x] = "X" if i % 2 == 0 else "0"

        for i in range(3):
            if board[i][0] != " " and all([board[i][j] == board[i][0] for j in range(3)]):
                return "A" if board[i][0] == "X" else "B"

            if board[0][i] != " " and all([board[j][i] == board[0][i] for j in range(3)]):
                return "A" if board[0][i] == "X" else "B"

        if board[0][0] != " " and all([board[i][i] == board[0][0] for i in range(3)]):
            return "A" if board[0][0] == "X" else "B"

        if board[0][2] != " " and all([board[2 - i][i] == board[0][2] for i in range(3)]):
            return "A" if board[0][2] == "X" else "B"

        return "Draw" if len(moves) == 9 else "Pending"


if __name__ == "__main__":
    sln = Solution()
    print(sln.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
    print(sln.tictactoe([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]))
    print(sln.tictactoe([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]))