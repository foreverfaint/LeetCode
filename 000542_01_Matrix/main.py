from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        h = len(mat)
        w = len(mat[0])

        from queue import Queue
        q = Queue()

        y = 0
        while y < h:
            x = 0
            while x < w:
                if mat[y][x] == 0:
                    q.put_nowait((y, x))
                else:
                    mat[y][x] = float("inf")
                x += 1
            y += 1

        while not q.empty():
            y, x = q.get_nowait()
            for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_y = i + y
                new_x = j + x
                if 0 <= new_y < h and 0 <= new_x < w:
                    if mat[y][x] + 1 < mat[new_y][new_x]:
                        mat[new_y][new_x] = mat[y][x] + 1
                        q.put_nowait((new_y, new_x))

        return mat


if __name__ == "__main__":
    sln = Solution()
    print(sln.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
    print(sln.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))