# Given 3 strings A, B and C, the task is to find the longest common sub-sequence in all three given sequences.

# A = "abcd", B = "efgh", C = "ijkl"
# Output: 0
# Explanation: There's no common subsequence
# in all the strings.


class Solution:
    def LCSof3(self, string1, string2, string3,n1,n2,n3):
        dP2D = [[0]*(n3+1) for i in range(n2+1)] # making n2Xn3 matrix of 0 [2D]
        dp = [dP2D] * (n1+1) # making n1X(n2Xn3) matrix of 0 [3D]

        for i in range(1, n1+1):        #for string1
            for j in range(1, n2+1):    #for string2
                for k in range(1, n3+1):  #for string3

                    if string1[i-1] == string2[j-1] == string3[k-1]:
                        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
        
        return dp[n1][n2][n3]


if __name__ == '__main__':
    X = 'ffmznimkkas'
    Y = 'vwsrenzkycx'
    Z = 'fxtlsgy'

    print(Solution().LCSof3(X, Y, Z, len(X), len(Y), len(Z)))