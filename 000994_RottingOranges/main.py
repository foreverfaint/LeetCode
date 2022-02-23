
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from queue import Queue
        q = Queue()

        fresh = 0
        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 2:
                    q.put_nowait((y, x))
                elif val == 1:
                    fresh += 1

        h = len(grid)
        w = len(grid[0])
        t = 0
        while not q.empty() and fresh > 0:
            new_q = Queue()
            while not q.empty():
                y, x = q.get_nowait()
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_y = i + y
                    new_x = j + x
                    if 0 <= new_y < h and 0 <= new_x < w:
                        if grid[new_y][new_x] == 1:
                            grid[new_y][new_x] = 2
                            fresh -= 1
                            new_q.put_nowait((new_y, new_x))

            q = new_q
            t += 1

        return t if fresh == 0 else -1


if __name__ == "__main__":
    sln = Solution()
    print(sln.orangesRotting([[0]]))
    print(sln.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(sln.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(sln.orangesRotting([[0,2]]))