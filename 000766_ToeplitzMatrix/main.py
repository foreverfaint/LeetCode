from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        h = len(matrix)
        w = len(matrix[0])

        for start_x in range(w):
            a = matrix[0][start_x]
            if any([a != matrix[y][x] for y, x in enumerate(range(start_x, w)) if y < h]):
                return False

        for start_y in range(1, h):
            a = matrix[start_y][0]
            if any([a != matrix[y][x] for x, y in enumerate(range(start_y, h)) if x < w]):
                return False

        return True



if __name__ == "__main__":
    sln = Solution()
    print(sln.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(sln.isToeplitzMatrix([[1,2],[2,2]]))