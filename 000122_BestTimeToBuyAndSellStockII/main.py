from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, buy = 0, prices[0]
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - buy
                buy = prices[i]
            else:
                buy = prices[i]
        return profit


if __name__ == "__main__":
    sln = Solution()
    print(sln.maxProfit([7,1,5,3,6,4]))
    print(sln.maxProfit([1,2,3,4,5]))
    print(sln.maxProfit([7,6,4,3,1]))