from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        seens = set()
        h = len(grid2)
        w = len(grid2[0])
        c = 0
        for y in range(h):
            for x in range(w):
                if grid2[y][x] == 1 and (y, x) not in seens:
                    from queue import Queue
                    q = Queue()
                    q.put_nowait((y, x))

                    flag = True
                    while not q.empty():
                        y_, x_ = q.get_nowait()
                        flag &= grid1[y_][x_] == 1

                        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            new_y = y_ + dy
                            new_x = x_ + dx

                            if (new_y, new_x) in seens:
                                continue
                            seens.add((new_y, new_x))

                            if 0 <= new_y < h and 0 <= new_x < w and grid2[new_y][new_x] == 1:
                                q.put_nowait((new_y, new_x))   

                    c += 1 if flag else 0                   
        return c



if __name__ == "__main__":
    sln = Solution()
    print(sln.countSubIslands(
        [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
        [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    ))
    print(sln.countSubIslands(
        [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], 
        [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    ))