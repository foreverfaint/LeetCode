from typing import List


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(mat) - 1
        while top < bottom:
            mid = (top + bottom) // 2
            if max(mat[mid]) < max(mat[mid + 1]):
                top = mid + 1
            else:
                bottom = mid
        peak_row = mat[bottom]
        peak_idx = peak_row.index(max(peak_row))
        return [bottom, peak_idx]


if __name__ == "__main__":
    sln = Solution()
    print(sln.findPeakGrid([[1,4],[3,2]]))
    print(sln.findPeakGrid([[10,20,15],[21,30,14],[7,16,32]]))
    print(sln.findPeakGrid([[6, 5, 4],[5, 4, 3], [4, 3, 2]]))