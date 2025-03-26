def climbStairsMinMoves(n, jumps):
    dp = [None] * (n+1)
    dp[n] = 0

    for i in range(n-1, -1, -1):
        for j in range(1, jumps[i]+1):
            index = i + j
            if 0<=index<=n and dp[index] != None:
                if dp[i] == None:
                    dp[i] = dp[index]
                else:
                    dp[i] = min(dp[i], dp[index])

        if dp[i] != None:
            dp[i] += 1

    return dp[0]


if __name__ == '__main__':
    n = 10
    jumps = [3, 2, 4, 2, 0, 2, 3, 1 ,2,2]

    print(climbStairsMinMoves(n, jumps))
