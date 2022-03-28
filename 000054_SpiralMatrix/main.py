from typing import List


class Solution:
    def foo(self, matrix, top, left, height, width, ans):
        # print(top, list(range(left, left + width)))
        for x in range(left, left + width):
            ans.append(matrix[top][x])

        if height == 1:
            return

        # print(list(range(top + 1, top + height)), left+ width - 1)
        for y in range(top + 1, top + height):
            ans.append(matrix[y][left+ width - 1])

        if height == 1:
            return

        # print(top + height - 1, list(range(left + width - 2, left - 1, -1)))
        for x in range(left + width - 2, left - 1, -1):
            ans.append(matrix[top + height - 1][x])

        if width == 1:
            return

        # print(list(range(top + height - 2, top, -1)), left)
        for y in range(top + height - 2, top, -1):
            ans.append(matrix[y][left])

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix)
        m = len(matrix[0])
        x = 0
        y = 0
        h = n
        w = m
        while len(ans) < m * n:
            self.foo(matrix, y, x, h, w, ans)
            x += 1
            y += 1
            w -= 2
            h -= 2
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(sln.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(sln.spiralOrder([[7],[9],[6]]))