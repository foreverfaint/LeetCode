from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        arr = [(sum(row) * 100 + i, i) for i, row in enumerate(mat)]
        import heapq
        heapq.heapify(arr)

        i = 0
        ans = []
        while i < k:
            t = heapq.heappop(arr)
            ans.append(t[1])
            i += 1
        return ans


if __name__ == "__main__":
    sln = Solution()

    print(sln.kWeakestRows([[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], 3))
    print(sln.kWeakestRows([[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]], 2))