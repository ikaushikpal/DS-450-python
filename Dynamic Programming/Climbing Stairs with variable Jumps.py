def stairCaseVarJumps(n, jumps):
    dp = [0] * (n+1)
    dp[n] = 1

    for i in range(n-1, -1, -1):
        for j in range(1, jumps[i]+1):
            index = i + j
            if 0<=index<=n:
                dp[i] += dp[index]

    return dp[0]


if __name__ == '__main__':
    n = 6
    jumps = [3, 3, 0, 2, 2 ,3]

    print(stairCaseVarJumps(n, jumps))

    n = int(input())
    jumps = [0] * n
    for i in range(n):
        jumps[i] = int(input())
    
    print(stairCaseVarJumps(n, jumps))
