from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        l = len(prices)
        if l < 2:
            return 0

        sell = 0
        buy = -prices[0]
        i = 1
        while i < l:
            max_sell = max(sell, buy + prices[i] - fee)
            max_buy = max(buy, sell - prices[i])
            sell = max_sell
            buy = max_buy
            i += 1
        return sell


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxProfit([1,3,2,8,4,9], 2))
    print(sln.maxProfit([1,3,7,5,10,3], 3))