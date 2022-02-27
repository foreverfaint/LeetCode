from typing import List


def _print(grid):
    print("-" * 10)
    for row in grid:
        def _(s):
            if s == "0":
                return ".."
            elif s == "1":
                return "##"
            else:
                return f"{s:02d}"
        print([_(x) for x in row])


class Solution:
    def find_island(self, grid):
        h = len(grid)
        w = len(grid[0])
        n = 0

        for y in range(1, h - 1):
            for x in range(1, w - 1):
                if grid[y][x] != 0:
                    continue

                from queue import Queue
                q = Queue()
                q.put_nowait((y, x))
                while not q.empty():
                    y_, x_ = q.get_nowait()
                    grid[y_][x_] = 2
                    if y_ > 1 and grid[y_ - 1][x_] == 0:
                        q.put_nowait((y_ - 1, x_))
                    if y_ < h - 2 and grid[y_ + 1][x_] == 0:
                        q.put_nowait((y_ + 1, x_))
                    if x_ > 1 and grid[y_][x_ - 1] == 0:
                        q.put_nowait((y_, x_ - 1))
                    if x_ < w - 2 and grid[y_][x_ + 1] == 0:
                        q.put_nowait((y_, x_ + 1))

                n += 1
        
        return n

    def fill_open_land(self, grid):
        h = len(grid)
        w = len(grid[0])

        check = [(0, x) for x in range(w)]
        check += [(h - 1, x) for x in range(w)]
        check += [(y, 0) for y in range(h) if 0 < y < h - 1]
        check += [(y, w - 1) for y in range(h) if 0 < y < h - 1]

        for y, x in check:
            if grid[y][x] != 0:
                continue

            from queue import Queue
            q = Queue()
            q.put_nowait((y, x))
            while not q.empty():
                y_, x_ = q.get_nowait()
                grid[y_][x_] = 1
                if x_ > 0 and grid[y_][x_ - 1] == 0:
                    q.put_nowait((y_, x_ - 1))
                if x_ < w - 1 and grid[y_][x_ + 1] == 0:
                    q.put_nowait((y_, x_ + 1))
                if y_ > 0 and grid[y_ - 1][x_] == 0:
                    q.put_nowait((y_ - 1, x_))
                if y_ < h - 1 and grid[y_ + 1][x_] == 0:
                    q.put_nowait((y_ + 1, x_))

    def closedIsland(self, grid: List[List[int]]) -> int:
        self.fill_open_land(grid)
        _print(grid)
        return self.find_island(grid)



if __name__ == "__main__":
    sln = Solution()
    print(sln.closedIsland([
        [1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]
    ]))
    print(sln.closedIsland([
        [0,0,1,0,0],
        [0,1,0,1,0],
        [0,1,1,1,0]
    ]))
    print(sln.closedIsland([
        [1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [1,0,1,1,1,0,1],
        [1,0,1,0,1,0,1],
        [1,0,1,1,1,0,1],
        [1,0,0,0,0,0,1],
        [1,1,1,1,1,1,1]
    ]))