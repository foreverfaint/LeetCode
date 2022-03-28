from typing import List


class Solution:
    def foo(self, mat, target, f_x, f_y):
        for y, row in enumerate(mat):
            for x, val in enumerate(row):
                new_y = f_y(y, x)
                new_x = f_x(y, x)
                if val != target[new_y][new_x]:
                    return False
        return True

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat) - 1
        return self.foo(mat, target, lambda y, x: x, lambda y, x: y) or self.foo(mat, target, lambda y, x: n - y, lambda y, x: x) or self.foo(mat, target, lambda y, x: n - x, lambda y, x: n - y) or self.foo(mat, target, lambda y, x: y, lambda y, x: n - x)



if __name__ == "__main__":
    sln = Solution()
    print(sln.findRotation([[0,1],[1,0]], [[1,0],[0,1]]))
    print(sln.findRotation([[0,1],[1,1]], [[1,0],[0,1]]))
    print(sln.findRotation([[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]]))