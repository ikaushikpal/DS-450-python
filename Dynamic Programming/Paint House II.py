class Solution:
    def paintHouse(self, cost:list, houses:int, colors:int)->int:
        if houses == 0: # no houses to paint
            return 0
        
        if colors == 0: # no colors to paint houses
            return 0
        
        dp = [[0]*colors for _ in range(houses)]
        dp[0] = cost[0]

        for i in range(1, houses):
            MINCOST = 1000000007
            for j in range(colors):
                for k in range(colors):
                    if j != k:
                        MINCOST = min(MINCOST, dp[i-1][k])

                dp[i][j] = cost[i][j] + MINCOST
        
        return min(dp[n-1])
    

if __name__ == "__main__":
    cost = [[1, 5, 7, 2, 1, 4],
            [5, 8, 4, 3, 6, 1],
            [3, 2, 9, 7, 2, 3],
            [1, 2, 4, 9, 1, 7]]
    n, k = len(cost), len(cost[0])
    
    print(Solution().paintHouse(cost, n, k))