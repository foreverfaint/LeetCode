from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        w = len(image)
        h = len(image[0])

        s = set()

        import queue
        q = queue.Queue()
        q.put_nowait((sr, sc))
        s.add((sr, sc))
        while not q.empty():
            r, c = q.get_nowait()
            image[r][c] = newColor
            
            if r > 0 and image[r - 1][c] == oldColor:
                if (r - 1, c) not in s:
                    q.put_nowait((r - 1, c))
                    s.add((r - 1, c))
            if r + 1 < w and image[r + 1][c] == oldColor:
                if (r + 1, c) not in s:
                    q.put_nowait((r + 1, c))
                    s.add((r + 1, c))
            if c > 0 and image[r][c - 1] == oldColor:
                if (r, c - 1) not in s:
                    q.put_nowait((r, c - 1))
                    s.add((r, c - 1))
            if c + 1 < h and image[r][c + 1] == oldColor:
                if (r, c + 1) not in s:
                    q.put_nowait((r, c + 1))
                    s.add((r, c + 1))

        return image
                


if __name__ == "__main__":
    sln = Solution()
    print(sln.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
    print(sln.floodFill([[0,0,0],[0,0,0]], 0, 0, 2))