from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        h = len(obstacleGrid)
        w = len(obstacleGrid[0])
        p = [0] * w

        for x in range(w):
            p[x] = 0 if obstacleGrid[0][x] == 1 else (p[x - 1] if x > 0 else 1)

        for y in range(1, h):
            for x in range(w):
                if x == 0:
                    p[0] = 0 if obstacleGrid[y][0] == 1 else p[0]
                else:
                    p[x] = 0 if obstacleGrid[y][x] == 1 else (p[x - 1] + p[x])

        return p[-1]


if __name__ == "__main__":
    sln = Solution()
    print(sln.uniquePathsWithObstacles([[0,1,0,0,0],[1,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]))
    print(sln.uniquePathsWithObstacles([[1,0]]))
    print(sln.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
    print(sln.uniquePathsWithObstacles([[0,1],[0,0]]))