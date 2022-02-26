from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r = [0] * (rowIndex + 1)
        for y in range(rowIndex + 1):
            for x in range(y, -1, -1):
                if x == 0 or x == y:
                    r[x] = 1
                else:
                    r[x] = r[x - 1] + r[x]
        return r


if __name__ == "__main__":
    sln = Solution()
    print(sln.getRow(3))
    print(sln.getRow(0))
    print(sln.getRow(1))