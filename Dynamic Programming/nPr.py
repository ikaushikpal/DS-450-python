class Solution:
    def nPrDP(self, n, r):
        dp = [[0]*(r+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(min(i, r)+1):
                # Base Cases
                if j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + (dp[i-1][j-1] * j)
                
                if (j < r):
                    dp[i][j+1] = 0
 
        return dp[n][r]

    def nPr(self, n, r):
        # recursive formula
        # P(n, k) = P(n-1, k) + k* P(n-1, k-1)   

        if r > n: # like 10P12 is wrong so return 0 if r > n
            return 0

        res = 1 # base value,, nPn = nP0 = 1

        # nPr = n!/ (n-r)!
        #        n * (n-1)* (n-2)* (n-3)*....*(n-r+1) * (n-r)!
        #      = ---------------------------------------------
        #         (n-r)!

        # cancel out (n-r)! term  
        
        #       = n * (n-1)* (n-2)* (n-3)*....*(n-r+1)             
        

        for i in range(r):
            res = res * (n - i) # n * (n-1)* (n-2)* (n-3)*....*(n-r+1)

        return res


if __name__ == '__main__':
    n = 10
    r = 2
    print(Solution().nPrDP(n, r))