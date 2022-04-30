from math import remainder
from typing import List


# Work, but TLE
# class Solution:
#     def maxProfit(self, inventory: List[int], orders: int) -> int:
#         inventory = [-x for x in inventory]
#         import heapq
#         heapq.heapify(inventory)

#         ans = 0
#         while orders > 0:
#             m = heapq.heappop(inventory)
#             ans += m
#             heapq.heappush(inventory, m + 1)
#             orders -= 1
#         return (-ans) % (10 ** 9 + 7)


class Solution:
    def getProfit(self, inventory, above):
        return sum([(x + above) * (x - above + 1) // 2 for x in inventory if x >= above])

    def getBalls(self, inventory, above):
        return sum([x - above + 1 for x in inventory if x >= above])

    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory = sorted(inventory, reverse=True)
        ans = 0
        low = 1
        high = inventory[0]
        while low < high:
            mid = (low + high) // 2
            balls = self.getBalls(inventory, mid)
            # print(f"low={low}, mid={mid}, high={high}, balls={balls} < orders={orders}")
            if balls <= orders:
                high = mid
            else:
                low = mid + 1
        
        balls = self.getBalls(inventory, low)
        if balls - orders > 0:
            low = low + 1
        leftBalls = abs(balls - orders)

        ans = self.getProfit(inventory, low)
        ans += leftBalls * (low - 1)
        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxProfit(inventory = [1000000000], orders = 1000000000))
    print(sln.maxProfit(inventory = [2,5], orders = 4))
    print(sln.maxProfit(inventory = [3,5], orders = 6))