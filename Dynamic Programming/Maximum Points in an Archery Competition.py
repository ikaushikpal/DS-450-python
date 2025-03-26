from optparse import Values


class Topdown():
    def knapsack(self, weight, value, n, w):
        self.dp = [[0]*(w+1) for x in range(len(weight) + 1)]

        for i in range(0, max(len(weight), w) + 1):
            if i <= w:
                self.dp[0][i] = 0

            if i <= len(weight):
                self.dp[i][0] = 0

        for i in range(1, n+1):
            for j in range(1, w+1):
                if j >= weight[i - 1]:
                    self.dp[i][j] = max(value[i-1] + self.dp[i-1][j-weight[i-1]], self.dp[i-1][j])
                else:
                    self.dp[i][j] = self.dp[i-1][j]

        print('=' * 50)
        print(weight)
        print('=' * 50)
        for row in self.dp:
            for i in row:
                print(f"{i:>3}", end=' ')
            print()
        print('=' * 50)
        return self.dp[n][w]
    
        
def printknapSack(W, wt, val, n):
    K = [[0 for w in range(W + 1)]
            for i in range(n + 1)]
             
    # Build table K[][] in bottom
    # up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                  + K[i - 1][w - wt[i - 1]],
                               K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]
 
    # stores the result of Knapsack
    res = K[n][W]
    print(res)
     
    w = W
    ans = [0] * 12
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (K[i-1][w]) or from (val[i-1]
        # + K[i-1] [w-wt[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        if res == K[i - 1][w]:
            continue
        else:
            ans[val[i-1]] = wt[i - 1]
             
            # Since this weight is included
            # its value is deducted
            res = res - val[i - 1]
            w = w - wt[i - 1]
    
    return ans


numArrows = 9
aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
weight = [a+1 for a in aliceArrows]
value = [i for i in range(0, 12)]
W = numArrows

print(printknapSack(W, weight, value, 12))