from typing import List


class Solution:
    def fill_open_land(self, grid):
        h = len(grid)
        w = len(grid[0])

        check = [(0, x) for x in range(w)]
        check += [(h - 1, x) for x in range(w)]
        check += [(y, 0) for y in range(h) if 0 < y < h - 1]
        check += [(y, w - 1) for y in range(h) if 0 < y < h - 1]

        for y, x in check:
            if grid[y][x] != 1:
                continue

            from queue import Queue
            q = Queue()
            q.put_nowait((y, x))
            while not q.empty():
                y_, x_ = q.get_nowait()
                grid[y_][x_] = 0
                if x_ > 0 and grid[y_][x_ - 1] == 1:
                    q.put_nowait((y_, x_ - 1))
                if x_ < w - 1 and grid[y_][x_ + 1] == 1:
                    q.put_nowait((y_, x_ + 1))
                if y_ > 0 and grid[y_ - 1][x_] == 1:
                    q.put_nowait((y_ - 1, x_))
                if y_ < h - 1 and grid[y_ + 1][x_] == 1:
                    q.put_nowait((y_ + 1, x_))

    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.fill_open_land(grid)
        return sum([sum(row) for row in grid])


if __name__ == "__main__":
    sln = Solution()
    print(sln.numEnclaves([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]))
    print(sln.numEnclaves([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]))