from typing import List


class Solution:
    def brokenCalc(self, X, Y):
        if X > Y: return X - Y
        if X == Y: return 0
        if Y % 2 == 0:
            return self.brokenCalc(X, Y//2) + 1
        else:
            return self.brokenCalc(X, Y + 1) + 1


if __name__ == "__main__":
    sln = Solution()
    print(sln.brokenCalc(2, 3))
    print(sln.brokenCalc(5, 8))
    print(sln.brokenCalc(3, 10))