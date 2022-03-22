
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        perimeter = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 0:
                    continue

                new_y = y - 1
                new_x = x
                if new_y < 0 or grid[new_y][new_x] == 0:
                    perimeter += 1
                
                new_y = y + 1
                new_x = x
                if new_y >= h or grid[new_y][new_x] == 0:
                    perimeter += 1

                new_y = y
                new_x = x - 1
                if new_x < 0 or grid[new_y][new_x] == 0:
                    perimeter += 1
                
                new_y = y
                new_x = x + 1
                if new_x >= w or grid[new_y][new_x] == 0:
                    perimeter += 1

        return perimeter


if __name__ == "__main__":
    sln = Solution()
    print(sln.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
    print(sln.islandPerimeter([[1]]))
    print(sln.islandPerimeter([[1,0]]))