
from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        h = len(img)
        w = len(img[0])
        ans = [[0] * w for _ in range(h)]
        for y, row in enumerate(img):
            for x, val in enumerate(row):
                avg = []
                for d_y, d_x in [
                    (-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 0), (0, 1),
                    (1, -1), (1, 0), (1, 1),
                ]:
                    new_y = y + d_y
                    new_x = x + d_x
                    if 0 <= new_y <= h - 1 and 0 <= new_x <= w - 1:
                        avg.append(img[new_y][new_x])
                import math
                ans[y][x] = math.floor(sum(avg) / len(avg))
        return ans
                    


if __name__ == "__main__":
    sln = Solution()

    print(sln.imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))
    print(sln.imageSmoother([[100,200,100],[200,50,200],[100,200,100]]))
    print(sln.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))