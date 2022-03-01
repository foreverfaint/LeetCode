from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        dist = [[float("inf")] * w for _ in range(h)]

        from queue import Queue
        q = Queue()   

        for y in range(h):
            for x in range(w):
                if grid[y][x] == 1:
                    dist[y][x] = 0
                    q.put_nowait((y, x))   

        if q.qsize() == 0 or q.qsize() == h * w:
            return -1
        
        while not q.empty():
            y_, x_ = q.get_nowait()
            v = dist[y_][x_] + 1

            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_y = y_ + dy
                new_x = x_ + dx
                if 0 <= new_y < h and 0 <= new_x < w and dist[new_y][new_x] > v:
                    dist[new_y][new_x] = v
                    q.put_nowait((new_y, new_x))

        from itertools import chain
        return max(chain.from_iterable(dist))


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxDistance([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
    print(sln.maxDistance([[1,0,1],[0,0,0],[1,0,1]]))
    print(sln.maxDistance([[1,0,0],[0,0,0],[0,0,0]]))