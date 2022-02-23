from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = len(prices)
        if l <= 1:
            return 0

        buy = -prices[0]
        sell = 0
        cooldown = 0
        i = 1
        while i < l:
            max_buy = max(buy, cooldown - prices[i])
            max_sell = max(sell, buy + prices[i])
            max_cooldown = max(sell, cooldown)

            buy = max_buy
            sell = max_sell
            cooldown = max_cooldown

            i += 1
        return max(sell, cooldown)


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxProfit([1,2,3,0,2]))
    print(sln.maxProfit([1]))
    print(sln.maxProfit([2,1]))
    print(sln.maxProfit([2,1,4]))