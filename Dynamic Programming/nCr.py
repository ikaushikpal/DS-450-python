class Solution:
    def nCrDP(self, n, r):
        dp = [[0]*(r+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(min(i, r)+1):
                # Base Cases
                if j == 0 or j == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
 
        return dp[n][r]

    def nCr(self, n, r):
        # nCr = n!/ (n-r)! * r!
        # nPr = n! /(n-r)!

        # recursive formula
        # nCr = (n-1)C(r-1) + (n-1)Cr

        # nCn = nC0 = 1

        if r>n: # like 10C12 is wrong so return 0 if r > n
             return 0
        
        if r > n - r: # e.g. 10C6 and 10C4 is same why ?
            r = n - r # 10C6 = 10!/(10-6)!*6! = 10!/4! * 6!
        # 10C4 = 10!/(10-4)!*4! = 10!/6! * 4!
        # so 10C6 and 10C4 is same
        # we are ruing loop 0 to r
        # if we reduce r value then we will save little bit computation
        # thats why that if block

        MOD  = 10**9 + 7
        # only for gfg online practice	

        res = 1 
        # base value,, nCn = nC0 = 1

        # after then if block we are sure that r < n
        # nCr = n!/ (n-r)! * r!
        #        n * (n-1)* (n-2)* (n-3)*....*(n-r+1) * (n-r)!
        #      = ---------------------------------------------
        #         (n-r)! * r!

        # cancel out (n-r)! term  
        
        #       n * (n-1)* (n-2)* (n-3)*....*(n-r+1)
        #     = -------------------------------------
        #                       r!
        

        for i in range(r):
            res = res * (n - i) # n * (n-1)* (n-2)* (n-3)*....*(n-r+1)
            res = res // (i + 1) # diving by r!
            
        return res%MOD

if __name__ == '__main__':
    n = 3
    r = 1
    print(Solution().nCrDP(n, r))