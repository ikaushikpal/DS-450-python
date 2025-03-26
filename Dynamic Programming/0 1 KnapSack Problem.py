# recursive solution
# time complexity : O(2^n)
# space complexity : O(1)

def knapsack(weight, value, n, w):
    if n == 0 or w == 0: # if weight arr is empty or total capacity is 0 then return 0
        return 0
    
    if w >= weight[n - 1]:
        return max(value[n-1] + knapsack(weight, value, n-1, w-weight[n-1]), knapsack(weight, value, n-1, w))
    else:
        return knapsack(weight, value, n-1, w)


# memoization solution
# time complexity : O(n*w)
# space complexity : O(n*w)

class Memoization():
    def knapsack(self, weight, value, n, w):
        self.dp = [[-1]*(w+1) for x in range(len(weight) + 1)]
        return self.knapsack_util(weight, value, n, w)
    
    def knapsack_util(self, weight, value, n, w):
        if n == 0 or w == 0:
            return 0

        if self.dp[n][w] != -1:
            return self.dp[n][w]

        if w >= weight[n - 1]:
            self.dp[n][w] = max(value[n-1] + self.knapsack_util(weight, value, n-1, w-weight[n-1]), self.knapsack_util(weight, value, n-1, w))
            return self.dp[n][w] 
        else:
            self.dp[n][w] = self.knapsack_util(weight, value, n-1, w)
            return self.dp[n][w]


# Top-Down(real DP) solution
# time complexity : O(n*w)
# space complexity : O(n*w)

class Topdown():
    def knapsack(self, weight, value, n, w):
        self.dp = [[0]*(w+1) for x in range(len(weight) + 1)]

        for i in range(0, max(len(weight), w) + 1):
            if i <= w:
                self.dp[0][i] = 0

            if i <= len(weight):
                self.dp[i][0] = 0

        return self.knapsack_util(weight, value, n, w)
    
    def knapsack_util(self, weight, value, n, w):
        for i in range(1, n+1):
            for j in range(1, w+1):
                if j >= weight[i - 1]:
                    self.dp[i][j] = max(value[i-1] + self.dp[i-1][j-weight[i-1]], self.dp[i-1][j])
                else:
                    self.dp[i][j] = self.dp[i-1][j]

        return self.dp[n][w]


if __name__=='__main__':
    weight = [1, 3, 4, 5]
    value = [1, 4, 5, 7]
    n = len(weight)
    w = 7

    t = Topdown()
    result = t.knapsack(weight, value, n, w)
    print(f"Maximum Profit we can form = {result}")
