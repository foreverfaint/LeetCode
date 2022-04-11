from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        new_grid = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new_i = (i + ((j + k) // n)) % m
                new_j = (j + k) % n
                new_grid[new_i][new_j] = grid[i][j]
        return new_grid


if __name__ == "__main__":
    sln = Solution()
    print(sln.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1))
    print(sln.shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
    print(sln.shiftGrid(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9))