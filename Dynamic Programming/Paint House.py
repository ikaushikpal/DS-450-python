# Minimize cost of painting N houses such that adjacent houses have different colors

# Given an integer N and a 2D array cost[][3], where cost[i][0], cost[i][1], and cost[i][2] is the cost of painting ith house with colors red, blue, and green respectively, the task is to find the minimum cost to paint all the houses such that no two adjacent houses have the same color.

# Examples:

# Input: N = 3, cost[][3] = {{14, 2, 11}, {11, 14, 5}, {14, 3, 10}}
# Output: 10
# Explanation: 
# Paint house 0 as blue. Cost = 2. Paint house 1 as green. Cost = 5. Paint house 2 as blue. Cost = 3.
# Therefore, the total cost = 2 + 5 + 3 = 10.

# Input: N = 2, cost[][3] = {{1, 2, 3}, {1, 4, 6}}
# Output: 3

class Solution:
    def paintHouse(self, cost):
        n = len(cost)

        if n==0: # if cost array is empty then no house to paint 
            return 0
        
        inclusiveRedPaint = cost[0][0]
        inclusiveBluePaint = cost[0][1]
        inclusiveGreenPaint = cost[0][2]

        for i in range(1, n):
            redCost = cost[i][0]
            blueCost = cost[i][1]
            greenCost = cost[i][2]

            # to color ith house red
            new_inclusiveRedPaint = redCost + min(inclusiveBluePaint, inclusiveGreenPaint)

            # to color ith house blue
            new_inclusiveBluePaint = blueCost + min(new_inclusiveRedPaint, inclusiveGreenPaint)

            # to color ith house green
            new_inclusiveGreenPaint = greenCost + min(inclusiveBluePaint, new_inclusiveRedPaint)

            inclusiveRedPaint = new_inclusiveRedPaint
            inclusiveBluePaint = new_inclusiveBluePaint
            inclusiveGreenPaint = new_inclusiveGreenPaint
        
        return  min(inclusiveRedPaint,
                    inclusiveBluePaint,
                    inclusiveGreenPaint)


if __name__ == '__main__':
    cost = [[14, 2, 11], [11, 14, 5], [14, 3, 10]]
    print(Solution().paintHouse(cost))