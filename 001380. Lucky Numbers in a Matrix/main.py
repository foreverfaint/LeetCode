from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r = len(matrix)
        c = len(matrix[0])
        min_ = [float("inf")] * r
        max_ = [0] * c
        for y in range(r):
            for x in range(c):
                min_[y] = min(min_[y], matrix[y][x])
                max_[x] = max(max_[x], matrix[y][x])

        ans = []
        for y in range(r):
            for x in range(c):
                if min_[y] == matrix[y][x] and max_[x] == matrix[y][x]:
                    ans.append(matrix[y][x])
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
    print(sln.luckyNumbers([[1,10,4,2],[9,3,8,7],[15,16,17,12]]))
    print(sln.luckyNumbers([[7,8],[1,2]]))
