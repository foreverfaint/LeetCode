from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        from collections import deque
        q = deque()
        q.append((rCenter, cCenter))

        visited = set()
        visited.add((rCenter, cCenter))

        ans = []
        while len(q) > 0:
            r, c = q.popleft()
            ans.append([r, c])

            for d_r, d_c in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_r = r + d_r
                new_c = c + d_c
                if 0 <= new_r < rows and 0 <= new_c < cols and (new_r, new_c) not in visited:
                    visited.add((new_r, new_c))
                    q.append((new_r, new_c))
        return ans


if __name__ == "__main__":
    sln = Solution()
    print(sln.allCellsDistOrder(rows = 1, cols = 2, rCenter = 0, cCenter = 0))
    print(sln.allCellsDistOrder(rows = 2, cols = 2, rCenter = 0, cCenter = 1))
    print(sln.allCellsDistOrder(rows = 2, cols = 3, rCenter = 1, cCenter = 2))