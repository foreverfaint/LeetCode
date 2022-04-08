from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        h = len(strs)
        w = len(strs[0])
        col = 0
        for x in range(w):
            last = strs[0][x]
            for y in range(1, h):
                if strs[y][x] < last:
                    col += 1
                    break
                last = strs[y][x]

        return col


if __name__ == "__main__":
    sln = Solution()
    print(sln.minDeletionSize(["cba","daf","ghi"]))
    print(sln.minDeletionSize(["a","b"]))
    print(sln.minDeletionSize(["zyx","wvu","tsr"]))