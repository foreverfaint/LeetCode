from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r = list(matrix[0])
        h = len(matrix)
        w = len(r)
        
        y = 1
        while y < h:
            x = 0
            t = [0] * w
            while x < w:
                c = []
                if x > 0:
                    c.append(r[x - 1])
                if x < w - 1:
                    c.append(r[x + 1])
                c.append(r[x])
                t[x] = min(c) + matrix[y][x]
                
                x += 1
            r = t
            y += 1

        return min(r)
        


if __name__ == "__main__":
    sln = Solution()
    print(sln.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    print(sln.minFallingPathSum([[-19,57],[-40,-5]]))
