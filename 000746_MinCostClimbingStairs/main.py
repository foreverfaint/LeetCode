from typing import List


class Solution:
    def _climb(self, cost, n, m):
        if n <= 1:
            return 0

        if n == 2:
            return min(cost[0], cost[1])

        r = m.get(n)
        if not r:
            r_2 = self._climb(cost, n - 2, m) + cost[n - 2]
            r_1 = self._climb(cost, n - 1, m) + cost[n - 1]
            r = min(r_2, r_1)
            m[n] = r

        return r

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self._climb(cost, len(cost), {})


if __name__ == "__main__":
    sln = Solution()
    print(sln.minCostClimbingStairs([10]))
    print(sln.minCostClimbingStairs([10,15]))
    print(sln.minCostClimbingStairs([10,15,20]))
    print(sln.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))