from typing import List


class Solution:
    def _isValid(self, iterable) -> bool:
        flag = [False for _ in range(9)]
        for s in iterable:
            if s == ".":
                continue
            digit = int(s) - 1
            if flag[digit]:
                return False
            flag[digit] = True
        return True

    def _iter_row(self, board: List[List[str]], target: int):
        yield from board[target]

    def _iter_col(self, board: List[List[str]], target: int):
        for row in board:
            yield row[target]

    def _iter_block(self, board: List[List[str]], target: int):
        r, c = target // 3, target % 3
        r = r * 3
        c = c * 3
        for i in range(3):
            for j in range(3):
                yield board[r + i][c + j]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not all([self._isValid(self._iter_row(board, i)) for i in range(9)]):
            return False
        if not all([self._isValid(self._iter_col(board, i)) for i in range(9)]):
            return False
        if not all([self._isValid(self._iter_block(board, i)) for i in range(9)]):
            return False
        return True


if __name__ == "__main__":
    sln = Solution()
    print(sln.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))