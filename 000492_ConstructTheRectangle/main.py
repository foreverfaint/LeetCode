from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        import math
        L = math.ceil(math.sqrt(area))
        while L >= area // L:
            if area % L == 0:
                return [L, area // L]
            L += 1


if __name__ == "__main__":
    sln = Solution()
    print(sln.constructRectangle(2))
    print(sln.constructRectangle(4))
    print(sln.constructRectangle(37))
    print(sln.constructRectangle(122122))