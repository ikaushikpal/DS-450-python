from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n <= 1:
            return 0

        left_to_right = [0] * n
        right_to_left = [0] * n
        maxProfit = 0

        # left to right
        # finding max profit we can make after selling stocks till now

        min_till_now = prices[0]

        for i in range(1, n):
            min_till_now = min(min_till_now, prices[i])
            left_to_right[i] = max(left_to_right[i-1], prices[i]-min_till_now)

        # right to left
        # finding max profit we can make if we buy stocks from today and sell later

        max_till_now = prices[n-1]

        for i in range(n-2, -1, -1):
            max_till_now = max(max_till_now, prices[i])
            right_to_left[i] = max(right_to_left[i+1], max_till_now-prices[i])


        # adding left-right and right-left and finding max of them

        for i in range(n):
            total = left_to_right[i] + right_to_left[i]

            maxProfit = max(maxProfit, total)

        
        return maxProfit


if __name__ == '__main__':
    sol = Solution()

    print(sol.maxProfit([3,3,5,0,0,3,1,4]))

    print(sol.maxProfit([1, 2, 3 ,4, 5]))