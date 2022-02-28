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


if __name__ == "__main__":
    sln = NumMatrix([
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ])
    sln.sumRegion(1, 1, 2, 2)
    sln = NumMatrix([
        [3, 0, 1, 4, 2], 
        [5, 6, 3, 2, 1], 
        [1, 2, 0, 1, 5], 
        [4, 1, 0, 1, 7], 
        [1, 0, 3, 0, 5]
    ])
    print(sln.sumRegion(*[2, 1, 4, 3]))
    print(sln.sumRegion(*[1, 1, 2, 2]))
    print(sln.sumRegion(*[1, 2, 2, 4]))