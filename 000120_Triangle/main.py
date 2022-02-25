from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        l = len(triangle)
        if l == 0:
            return 0

        s = [0] * l
        s[0] = triangle[0][0]
        i = 1
        while i < l:
            for j in range(i, -1, -1):
                if j == i:
                    s[j] = s[j - 1] + triangle[i][j]
                elif j == 0:
                    s[j] = s[j] + triangle[i][j]
                else:
                    s[j] = min(s[j - 1], s[j]) + triangle[i][j]
            i += 1
        return min(s)



if __name__ == "__main__":
    sln = Solution()
    print(sln.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(sln.minimumTotal([[-10]]))
    