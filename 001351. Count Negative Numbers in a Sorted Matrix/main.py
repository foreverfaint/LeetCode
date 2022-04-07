from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])

        ans = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] < 0:
                    ans += w - x
                    break
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
    # print(sln.countNegatives([[3,2],[1,0]]))