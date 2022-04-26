from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        h = len(mat)
        w = len(mat[0])
        presum = [[0] * (w + 1) for _ in range(h + 1)]
        side = 0
        for y in range(1, h + 1):
            for x in range(1, w + 1):
                presum[y][x] = presum[y -1][x] + presum[y][x - 1] - presum[y-1][x-1] + mat[y-1][x-1]
                y_0 = y - side - 1
                x_0 = x - side - 1
                if y_0 >= 0 and x_0 >= 0 and (presum[y][x] - presum[y_0][x] - presum[y][x_0] + presum[y_0][x_0]) <= threshold:
                    side += 1
        return side


if __name__ == "__main__":
    sln = Solution()
    # 3
    print(sln.maxSideLength([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6))
    # 2
    print(sln.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4))
    # 0
    print(sln.maxSideLength(mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1))