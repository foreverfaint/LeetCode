from typing import List


class Solution:
    def largestTriangleArea(self, p):
        import itertools
        return max(0.5 * abs(xa*yb + xb*yc + xc*ya - xb*ya - xc*yb - xa*yc)
                   for (xa, ya), (xb, yb), (xc, yc) in itertools.combinations(p, 3))


if __name__ == "__main__":
    sln = Solution()
    print(sln.largestTriangleArea([[0,0],[0,1],[1,0],[0,2],[2,0]]))
    print(sln.largestTriangleArea([[1,0],[0,0],[0,1]]))