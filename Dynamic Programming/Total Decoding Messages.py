class Solution:
    def numDecodings(self, string: str) -> int:
        n = len(string)
        
        if string[0] == '0':
            return 0
        
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            if string[i-1] == '0' and string[i] == '0':
                dp[i] = 0
            
            elif string[i-1] == '0' and string[i] != '0':
                dp[i] = dp[i-1]

            elif string[i-1] != '0' and string[i] == '0':
                if int(string[i-1:i+1]) <= 26:
                    if i>=2:
                        dp[i] = dp[i-2]
                    else:
                        dp[i] = 1
                else:
                    dp[i] = 0
            
            else:
                if int(string[i-1:i+1]) <= 26:
                    if i>=2:
                        dp[i] = dp[i-2] + dp[i-1]
                    else:
                        dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-1]
            
        return dp[n-1]


if __name__ == '__main__':
    s = "231011"
    print(Solution().numDecodings(s))
