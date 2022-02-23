from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        w = len(grid)
        h = len(grid[0])

        newColor = 2

        s = set()
        max_area = 0
        max_color = -1
        for y, row in enumerate(grid):
            for x, oldColor in enumerate(row):
                if oldColor == 0:
                    continue

                if (y, x) in s:
                    continue

                s.add((y, x))

                import queue
                q = queue.Queue()
                q.put_nowait((y, x))

                cur_area = 0

                while not q.empty():
                    r, c = q.get_nowait()
                    grid[r][c] = newColor
                    cur_area += 1
                    if r > 0 and grid[r - 1][c] == oldColor:
                        if (r - 1, c) not in s:
                            q.put_nowait((r - 1, c))
                            s.add((r - 1, c))
                    if r + 1 < w and grid[r + 1][c] == oldColor:
                        if (r + 1, c) not in s:
                            q.put_nowait((r + 1, c))
                            s.add((r + 1, c))
                    if c > 0 and grid[r][c - 1] == oldColor:
                        if (r, c - 1) not in s:
                            q.put_nowait((r, c - 1))
                            s.add((r, c - 1))
                    if c + 1 < h and grid[r][c + 1] == oldColor:
                        if (r, c + 1) not in s:
                            q.put_nowait((r, c + 1))
                            s.add((r, c + 1))

                if cur_area > max_area:
                    max_area = cur_area
                    max_color = newColor

        return max_area

        



if __name__ == "__main__":
    sln = Solution()
    print(sln.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(sln.maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))