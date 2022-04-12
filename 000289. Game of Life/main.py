from typing import List


class Solution:
    def count(self, m, n, y, x, r_0, r_1, r_2):
        live_neighbour = 0
        
        for d_y, d_x, r in [
            (-1, -1, r_0), (-1, 0, r_0), (-1, 1, r_0),
            (0, -1, r_1), (0, 1, r_1),
            (1, -1, r_2), (1, 0, r_2), (1, 1, r_2),
        ]:
            y_ = y + d_y
            x_ = x + d_x
            if 0 <= y_ < m and 0 <= x_ < n and r[x_] == 1:
                live_neighbour += 1

        return live_neighbour

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        r_0 = None
        r_1 = [x for x in board[0]]
        for y in range(m):
            r_2 = [x for x in board[y + 1]] if y + 1 < m else None
            for x in range(n):
                live_neighbour = self.count(m, n, y, x, r_0, r_1, r_2)
                if board[y][x] == 0 and live_neighbour == 3:
                    board[y][x] = 1
                elif board[y][x] == 1 and (live_neighbour < 2 or live_neighbour > 3):
                    board[y][x] = 0
            r_0 = r_1
            r_1 = r_2        


if __name__ == "__main__":
    sln = Solution()

    board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    sln.gameOfLife(board)
    print(board)

    board = [[1,1],[1,0]]
    sln.gameOfLife(board)
    print(board) 