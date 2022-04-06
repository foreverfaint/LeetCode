from typing import List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        area1 = sum([max(row) for row in grid])
        area2 = sum([len([val for val in row if val > 0]) for row in grid])
        area3 = 0
        for x in range(len(grid[0])):
            max_ = 0
            for y in range(len(grid)):
                max_ = max(max_, grid[y][x])
            area3 += max_
        return area1 + area2 + area3


if __name__ == "__main__":
    sln = Solution() 
    print(sln.projectionArea([[1,2],[3,4]]))
    print(sln.projectionArea([[2]]))
    print(sln.projectionArea([[1,0],[0,2]]))