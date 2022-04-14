from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]
            ans += max(abs(x2 - x1), abs(y2 - y1))
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
    print(sln.minTimeToVisitAllPoints([[3,2],[-2,2]]))