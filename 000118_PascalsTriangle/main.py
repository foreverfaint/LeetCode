from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r = [list(range(i + 1)) for i in range(numRows)]
        for i in range(numRows):
            for j in range(i + 1):
                if j == 0 or j == i:
                    r[i][j] = 1
                else:
                    r[i][j] = r[i - 1][j - 1] + r[i - 1][j]
        return r


if __name__ == "__main__":
    sln = Solution()
    print(sln.generate(5))
    print(sln.generate(1))