from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p0_x, p0_y = points[0]
        p1_x, p1_y = points[1]
        p2_x, p2_y = points[2]
        return not (p2_y - p0_y) * (p1_x - p0_x) == (p1_y - p0_y) * (p2_x - p0_x)



if __name__ == "__main__":
    sln = Solution()
    print(sln.isBoomerang([[1,1],[2,3],[3,2]]))
    print(sln.isBoomerang([[1,1],[2,2],[3,3]]))