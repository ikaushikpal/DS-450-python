from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0

        totalProfit = 0
        minStockPrice = prices[0]
        maxStockPrice = prices[0]

        for i in range(1, len(prices)):
            stockPrice = prices[i]

            if stockPrice >= maxStockPrice:
                maxStockPrice = stockPrice

            else:
                totalProfit += maxStockPrice - minStockPrice
                maxStockPrice = minStockPrice = stockPrice

        
        totalProfit += maxStockPrice - minStockPrice

        return totalProfit




if __name__ == '__main__':
    sol = Solution()

    print(sol.maxProfit([7,1,5,3,6,4]))