class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = len(prices)-1
        maxValue = prices[i]
        while i >= 1:
            profit = max(profit, maxValue-prices[i-1])
            if prices[i-1] > maxValue:
                maxValue = prices[i-1]
            i -= 1
        return profit