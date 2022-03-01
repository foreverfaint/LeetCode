from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        h = len(heights)
        w = len(heights[0])
        r = [[0] * w for _ in range(h)]
        from queue import Queue
        q = Queue()

        for x in range(w):
            r[0][x] |= 1
            q.put_nowait((0, x))
            r[h - 1][x] |= 2
            q.put_nowait((h - 1, x))

        for y in range(0, h):
            r[y][0] |= 1
            q.put_nowait((y, 0))
            r[y][w - 1] |= 2
            q.put_nowait((y, w - 1))

        while not q.empty():
            y_, x_ = q.get_nowait()
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_y = y_ + dy
                new_x = x_ + dx
                if 0 <= new_y < h and 0 <= new_x < w and heights[new_y][new_x] >= heights[y_][x_] and r[new_y][new_x] != r[y_][x_]:
                    r[new_y][new_x] |= r[y_][x_]
                    q.put_nowait((new_y, new_x))

        ans = []
        for y in range(h):
            for x in range(w):
                if r[y][x] == 3:
                    ans.append((y, x))
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(sln.pacificAtlantic([[2,1],[1,2]]))