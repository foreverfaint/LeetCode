from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self._m = matrix

        h = len(matrix)
        w = len(matrix[0])

        self.s = [[0] * w for _ in range(h)]
        self.s[0][0] = matrix[0][0]

        for x in range(1, w):
            self.s[0][x] = self.s[0][x - 1] + matrix[0][x]

        for y in range(1, h):
            self.s[y][0] = self.s[y - 1][0] + matrix[y][0]

        y = 1
        while y < h:
            x = 1
            while x < w:
                self.s[y][x] = matrix[y][x] + self.s[y - 1][x] + self.s[y][x - 1] - self.s[y - 1][x - 1]
                x += 1
            y += 1

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r = self.s[row2][col2] 
        if row1 > 0:
            r -= self.s[row1 - 1][col2]
        if col1 > 0:
            r -= self.s[row2][col1 - 1] 
        if row1 > 0 and col1 > 0:
            r += self.s[row1 - 1][col1 - 1]
        return r


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        helper = NumMatrix(mat)
        h = len(mat)
        w = len(mat[0])
        answer = [[0] * w for _ in range(h)]
        for y in range(h):
            for x in range(w):
                y_1 = max(0, y - k)
                y_2 = min(h - 1, y + k)
                x_1 = max(0, x - k)
                x_2 = min(w - 1, x + k)
                answer[y][x] = helper.sumRegion(y_1, x_1, y_2, x_2)
        return answer


if __name__ == "__main__":
    sln = Solution()
    print(sln.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1))
    print(sln.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 2))