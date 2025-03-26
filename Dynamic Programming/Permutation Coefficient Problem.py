def permutation_coefficient(n, k):
    if k > n:
        return 0
    
    if k==0 or n==k:
        return 1
    
    return (k * permutation_coefficient(n-1,k-1)) + permutation_coefficient(n-1,k)


class Memoization():
    def permutation_coefficient(self, n, k):
        self.dp = [[-1]*(k+1) for x in range(n+1)]
        
        return self.permutation_coefficient_util(n, k)

    def permutation_coefficient_util(self, n, k):
        if k > n:
            return 0
        
        if k==0 or n==k:
            return 1
        
        if self.dp[n][k] != -1:
            return self.dp[n][k]
        
        self.dp[n][k] = self.permutation_coefficient_util(n-1, k) +(k * self.permutation_coefficient_util(n-1,k-1))

        return self.dp[n][k]

class Topdown():
    def permutation_coefficient(self, n, k):
        self.dp = [[1]*(k+1) for x in range(n+1)]
        for i in range(1, k+1):
            self.dp[0][i] = 0

        return self.permutation_coefficient_util(n, k)

    def permutation_coefficient_util(self, n, k):
        for i in range(1, n+1):
            for j in range(1, k+1):
                self.dp[i][j] = (j * self.dp[i-1][j-1]) + self.dp[i-1][j]
    
        return self.dp[n][k]


if __name__ == "__main__": 
    n = 10
    k = 2
    t = Topdown()
    m = Memoization()
    print(m.permutation_coefficient(n, k))