from typing import List


def search(board: List[List[str]], y, x, target) -> bool:
    t = board[y][x]
    board[y][x] = '0'

    try:
        m = len(board)
        n = len(board[0])
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < n and 0 <= new_y < m:
                if board[new_y][new_x] == target[0]:
                    if len(target) == 1 or search(board, new_y, new_x, target[1:]):
                        return True
    finally:
        board[y][x] = t

    return False

class Solution:
    def exist(self, board: List[List[str]], target: str) -> bool:
        m = len(board)
        n = len(board[0])
        for y in range(m):
            for x in range(n):
                if board[y][x] == target[0]:
                    if len(target) == 1 or search(board, y, x, target[1:]):
                        return True
        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.exist([["a"]], "a"))
    print(sln.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
    print(sln.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
    print(sln.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))