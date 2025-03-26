from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1 : return 0

        old_sell_state_profit = 0
        old_buy_state_profit = -prices[0]
        old_cooldown_state_profit = 0

        for i in range(1, len(prices)):
            new_buy_state_profit = max(old_buy_state_profit, old_cooldown_state_profit - prices[i])
            new_sell_state_profit = max(old_sell_state_profit, prices[i] + old_buy_state_profit)          
            new_cooldown_state_profit = max(old_sell_state_profit, old_cooldown_state_profit)

            old_sell_state_profit = new_sell_state_profit
            old_buy_state_profit =new_buy_state_profit
            old_cooldown_state_profit =new_cooldown_state_profit


        return old_sell_state_profit


if __name__ == '__main__':
    sol = Solution()

    print(sol.maxProfit([1, 2, 3 ,0, 2]))