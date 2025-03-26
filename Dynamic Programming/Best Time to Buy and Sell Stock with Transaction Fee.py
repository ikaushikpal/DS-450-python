from typing import *


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1: return 0

        bsp = -prices[0] # bought state profit
        ssp = 0          # sell state profit

        for i in range(1, len(prices)):
            
            bsp_ = max(bsp, ssp-prices[i])
            ssp_ = max(ssp, prices[i]-fee+bsp)

            bsp, ssp = bsp_, ssp_

        return ssp