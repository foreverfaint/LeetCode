from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        if n * m != r * c:
            return mat

        new_mat = [list(range(c)) for _ in range(r)]
        i = 0
        l = n * m
        while i < l:
            new_row = i // c
            new_col = i % c
            old_row = i // m
            old_col = i % m
            new_mat[new_row][new_col] = mat[old_row][old_col]
            i += 1
        return new_mat



if __name__ == "__main__":
    sln = Solution()
    # print(sln.matrixReshape([[1,2],[3,4]], 1, 4))
    # print(sln.matrixReshape([[1,2],[3,4]], 2, 4))
    print(sln.matrixReshape([[1,2,3,4]], 2, 2))