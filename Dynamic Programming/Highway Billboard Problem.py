class Solution:
    def highwayBillboard(self, total_length, places, revenue, min_dist):
        n = len(revenue)

        dp = [[0]*(1+total_length) for _ in range(1+n)]

        for i in range(1, n+1):
            for j in range(1, total_length+1):
                if places[i-1] <= j:

                    if j < min_dist+1:
                        dp[i][j] = max(dp[i-1][j], revenue[i-1])

                    else:  
                        dp[i][j] = max(dp[i-1][j], dp[i-1][j-min_dist-1]+revenue[i-1])
                
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][total_length]



if __name__ == '__main__':
    sol = Solution()
    print(sol.highwayBillboard(15, [6, 9, 12, 14], [5, 6, 3, 7], 2))
    print(sol.highwayBillboard(4, [1, 2 ,4], [1, 2 ,3], 2))