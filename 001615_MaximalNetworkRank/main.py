from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        link = set()
        rank = [0] * n
        for road in roads:
            rank[road[0]] += 1
            rank[road[1]] += 1
            link.add((road[0], road[1]))
            link.add((road[1], road[0]))
        
        print(rank)

        max_ = 0
        for st in range(n):
            for ed in range(st + 1, n):
                r = rank[st] + rank[ed] - (1 if (st, ed) in link else 0)
                max_ = max(r, max_)
        return max_


if __name__ == "__main__":
    sln = Solution()
    print(sln.maximalNetworkRank(2, [[1,0]]))
    # print(sln.maximalNetworkRank(4, [[0,1],[0,3],[1,2],[1,3]]))
    # print(sln.maximalNetworkRank(5, [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]))
    # print(sln.maximalNetworkRank(8, [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]))