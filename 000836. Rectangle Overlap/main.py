from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        xA = max(rec1[0], rec2[0])
        yA = max(rec1[1], rec2[1])
        xB = min(rec1[2], rec2[2])
        yB = min(rec1[3], rec2[3])
        # compute the area of intersection rectangle
        return max(0, xB - xA) * max(0, yB - yA) > 0


if __name__ == "__main__":
    sln = Solution()
    print(sln.isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]))
    print(sln.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [1,0,2,1]))
    print(sln.isRectangleOverlap(rec1 = [0,0,1,1], rec2 = [2,2,3,3]))