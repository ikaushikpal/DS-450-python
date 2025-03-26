def partitionSubsetRecursive(n, k):
    if n >= k: return 1
    if n < k : return 0

    return partitionSubsetRecursive(n-1, k)*k + partitionSubsetRecursive(n-1, k-1)


def partitionSubset(n, k):
    dp = [[0]*(1+k) for _ in range(n+1)]
    
    for j in range(n+1):
        # for first column
        dp[j][0] = 1

        # for second colum
        if j>=1:
            dp[j][1] = 1
    
    for i in range(1, n+1):
        for j in range(2, i+1):
            if j > k : break

            if i==j:
                dp[i][j] = 1
            
            elif i > j:
                dp[i][j] = j*dp[i-1][j] + dp[i-1][j-1]
    
    return dp[n][k]




assert partitionSubset(4, 3)==6, "Invalid results"
assert partitionSubset(3, 2)==3, "Invalid results"
assert partitionSubset(3, 1)==1, "Invalid results"

