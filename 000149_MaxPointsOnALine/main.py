from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        m = {}
        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i + 1, len(points)):
                x2 = points[j][0]
                y2 = points[j][1]       
                if x2 == x1:
                    k = x1
                    b = "|"
                else:         
                    k = float(y2 - y1) / float(x2 - x1)
                    b = y1 - k * x1
                m.setdefault((k, b), set())
                m[(k, b)].add((x1, y1))
                m[(k, b)].add((x2, y2))
        print(m)
        return max([len(s) for _, s in m.items()])
                


if __name__ == "__main__":
    sln = Solution()
    # print(sln.maxPoints([[1,1],[2,2],[3,3]]))
    # print(sln.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    print(sln.maxPoints([[3,3],[1,4],[1,1],[2,1],[2,2]]))