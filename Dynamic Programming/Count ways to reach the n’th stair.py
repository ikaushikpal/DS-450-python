def countStairsRecursive(current, destination):
    if current > destination:
        return 0

    if current == destination:
        return 1
    
    return countStairsRecursive(current+1, destination) + countStairsRecursive(current+2, destination)

def countStairsTopDown(current, destination, dp):
    if current > destination:
        return 0

    if current == destination:
        return 1
    
    if dp[current] != -1:
        return dp[current]

    dp[current] = countStairsRecursive(current+1, destination) + countStairsRecursive(current+2, destination)
    return dp[current]

def countStairsBottomUp(destination):
    dp = [-1] * (destination+1)

    dp[0], dp[1] = 1, 1

    for i in range(2, destination+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[destination]


if __name__ == '__main__':
    n = 4
    print(countStairsRecursive(0, n))

    dp = [-1] * (n+1)
    print(countStairsTopDown(0, n, dp))

    print(countStairsBottomUp(n))