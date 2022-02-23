from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for r in matrix:
            if target > r[-1]:
                continue
            if target < r[0]:
                return False
            for c in r:
                if c == target:
                    return True
        return False


if __name__ == "__main__":
    sln = Solution()
    print(sln.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(sln.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))