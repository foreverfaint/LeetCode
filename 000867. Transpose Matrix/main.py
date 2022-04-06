from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        h = len(matrix)
        w = len(matrix[0])

        new_matrix = [[0] * h for _ in range(w)]
        for y, row in enumerate(matrix):
            new_x = y
            for x, _ in enumerate(row):
                new_y = x
                new_matrix[new_y][new_x] = matrix[y][x]
        return new_matrix


if __name__ == "__main__":
    sln = Solution()
    print(sln.transpose([[1,2,3],[4,5,6],[7,8,9]]))
    print(sln.transpose(matrix = [[1,2,3],[4,5,6]]))