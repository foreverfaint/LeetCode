from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        ans = 0
        for y in range(h):
            for x in range(w):
                t = grid[y - 1][x] if y > 0 else 0
                l = grid[y][x - 1] if x > 0 else 0
                b = grid[y + 1][x] if y < h - 1 else 0
                r = grid[y][x + 1] if x < w - 1 else 0
                ans += max(0, grid[y][x] - t) + max(0, grid[y][x] - l) + max(0, grid[y][x] - b) + max(0, grid[y][x] - r) + (2 if grid[y][x] > 0 else 0)
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.surfaceArea([[1,2],[3,4]]))
    print(sln.surfaceArea([[1,1,1],[1,0,1],[1,1,1]]))
    print(sln.surfaceArea([[2,2,2],[2,1,2],[2,2,2]]))