from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = max(prices)
        i = 0
        l = len(prices)
        max_profit = 0
        while i < l:
            if prices[i] < least:
                least = prices[i]
            profile = prices[i] - least
            if profile > max_profit:
                max_profit = profile
            i += 1
        return max_profit


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxProfit([7,1,5,3,6,4]))
    print(sln.maxProfit( [7,6,4,3,1]))