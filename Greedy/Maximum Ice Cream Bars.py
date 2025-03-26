# It is a sweltering summer day, and a boy wants to buy some ice cream bars.

# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 

# Note: The boy can buy the ice cream bars in any order.

# Return the maximum number of ice cream bars the boy can buy with coins coins.

# You must solve the problem by counting sort.


# Example 1:
# Input: costs = [1,3,2,4,1], coins = 7
# Output: 4
# Explanation: The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.


# Example 2:
# Input: costs = [10,6,8,7,7,8], coins = 5
# Output: 0
# Explanation: The boy cannot afford any of the ice cream bars.


# Example 3:
# Input: costs = [1,6,3,1,2,5], coins = 20
# Output: 6
# Explanation: The boy can buy all the ice cream bars for a total price of 1 + 6 + 3 + 1 + 2 + 5 = 18.


from collections import Counter
from typing import List


class Solution:
    def findMinMax(self, nums):
        minn = maxx = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < minn:
                minn = nums[i]
            elif nums[i] > maxx:
                maxx = nums[i]
        return minn, maxx
    
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        minCost, maxCost = self.findMinMax(costs)
        
        if minCost > coins:
            return 0
        
        bucket = Counter(costs)
        maxIceCreamBars = 0
        
        for cost in range(minCost, maxCost + 1):
            if cost in bucket:
                canBuy = min(bucket[cost], coins // cost)
                maxIceCreamBars += canBuy
                coins -= canBuy * cost
        return maxIceCreamBars
# Time Complexity: O(n)
# Space Complexity: O(n)


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxIceCream([1,3,2,4,1], 7))
    print(sol.maxIceCream([10,6,8,7,7,8], 5))
    print(sol.maxIceCream([1,6,3,1,2,5], 20))