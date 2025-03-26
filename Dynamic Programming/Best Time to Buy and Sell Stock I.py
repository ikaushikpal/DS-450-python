class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minValue = 10**5
        
        for price in prices:
            minValue = min(price, minValue)
            maxProfit = max(price - minValue, maxProfit)

        return maxProfit