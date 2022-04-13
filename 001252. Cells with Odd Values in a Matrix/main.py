from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        map = [[0] * n for _ in range(m)]
        for index in indices:
            r, c = index
            for x in range(n):
                map[r][x] += 1
            for y in range(m):
                map[y][c] += 1
        return sum([sum([1 for val in row if val % 2 == 1]) for row in map])



if __name__ == "__main__":
    sln = Solution()
    print(sln.oddCells(m = 2, n = 3, indices = [[0,1],[1,1]]))
    print(sln.oddCells(m = 2, n = 2, indices = [[1,1],[0,0]]))