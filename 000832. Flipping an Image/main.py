from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i = 0
            j = len(row) - 1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
            for i in range(len(row)):
                row[i] = 1 - row[i]
        return image


if __name__ == "__main__":
    sln = Solution()
    print(sln.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))
    print(sln.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))