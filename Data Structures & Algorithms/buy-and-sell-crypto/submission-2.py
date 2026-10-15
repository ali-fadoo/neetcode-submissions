class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minP = prices[0]
        for i in range(len(prices)):
            if prices[i] < minP:
                minP = prices[i]
         
            if profit < prices[i] - minP:
                profit = prices[i] - minP
        return profit


