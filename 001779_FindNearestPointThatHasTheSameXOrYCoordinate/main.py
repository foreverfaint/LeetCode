from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        def _f(x_, y_):
            return abs(x - x_) + abs(y - y_)

        valid_points = [(x_, y_, i) for i, (x_, y_) in enumerate(points) if x_ == x or y_ == y]
        if not valid_points:
            return -1
        
        print(valid_points)

        i = 1
        l = len(valid_points)
        min_v = _f(valid_points[0][0], valid_points[0][1])
        min_i = valid_points[0][2]
        while i < l:
            v = _f(valid_points[i][0], valid_points[i][1])
            if v < min_v:
                min_v = v
                min_i = valid_points[i][2]
            i += 1
        return min_i



if __name__ == "__main__":
    sln = Solution()
    print(sln.nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]]))
    print(sln.nearestValidPoint(3, 4, [[3,4]]))
    print(sln.nearestValidPoint(3, 4, [[2,3]]))