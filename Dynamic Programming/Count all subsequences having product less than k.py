# Given a positive array, find the number of subsequences having product smaller than or equal to K.


# Examples: 
# Input : [1, 2, 3, 4] 
#         k = 10
# Output :11 

# Explanation: The subsequences are {1}, {2}, {3}, {4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {1, 2, 3}, {1, 2, 4}

# Input  : [4, 8, 7, 2] 
#          k = 50
# Output : 9


class Solution:
    def productSubSeqCount(self, arr, k):
        N = len(arr)
        dp = [[0]*(N+1) for _ in range(k+1)]

        for i in range(1, k+1):
            for j in range(1, N + 1):
                dp[i][j] = dp[i][j-1]
                if i >= arr[j-1]:
                    dp[i][j] += dp[i // arr[j-1]][j-1] + 1
        
        return dp[k][N]
# Time Complexity: O(Nk)
# Space Complexity: O(Nk)


if __name__ == '__main__':
    s = Solution()
    print(s.productSubSeqCount([1, 2, 3, 4], 10))
    print(s.productSubSeqCount([4, 8, 7, 2], 50))
