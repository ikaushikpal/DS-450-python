class Solution:
    def CountWays(self, string):
        n = len(string)
        dp = [0] * n
        
        dp[0] = 1

        if int(string[0:2]) <= 26:
            dp[1] = 2
        else:
            dp[1] = 1

        for i in range(2, n):
            if string[i] == '0':
                dp[i] = dp[i-1]
            
            else:
                dp[i] = dp[i-1]
                if string[i-1] != '0':
                    x = int(string[i-1 : i+1])
                    if 1<=x<=26:
                        dp[i] += dp[i-2]
        
        return dp[n-1]


if __name__ == '__main__':
    s = "231011"
    print(Solution().CountWays(s))
