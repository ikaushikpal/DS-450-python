class Solution:
    def longestCommonSub(self, a, n, b, m):
        dp = [[0]*(m+1) for i in range(n+1)]
        output_string = ''

        for i in range(1, n+1):
            for j in range(1, m+1):
                if a[i-1] == b[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n][m]
        
    def minOperations(self, s1, s2):
        n = len(s1)
        m = len(s2)

        lcs = self.longestCommonSub(s1,n,s2,m)
        insertion = m-lcs
        deletion = n-lcs
        totalOperations = insertion + deletion
        return totalOperations


if __name__ == '__main__':
    str1 = "heap"
    str2 = "pea"

    print(Solution().minOperations(str1, str2))
    # Explanation: 2 deletions and 1 insertion
    # p and h deleted from heap. Then, p is 
    # inserted at the beginning One thing to 
    # note, though p was required yet it was 
    # removed/deleted first from its position 
    # and then it is inserted to some other 
    # position. Thus, p contributes one to the 
    # deletion_count and one to the 
    # insertion_count.

    str1 = "geeksforgeeks"
    str2 = "geeks"
    print(Solution().minOperations(str1, str2))
    # Explanation: 8 insertions