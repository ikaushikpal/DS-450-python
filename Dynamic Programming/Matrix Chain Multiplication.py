def matrixChainMultiplication(matrix):
    INT_MAX = 99999999
    n = len(matrix)
    cost = [[INT_MAX]*n for i in range(n)]

    for i in range(n):
        cost[i][i] = 0
    
    for L in range(1, n-1):
        for i in range(1, n-L):
            j = i+L
            for k in range(i, j):
                new_cost = cost[i][k] + cost[k+1][j] + (matrix[i-1] * matrix[k] * matrix[j])
                cost[i][j] = min(cost[i][j], new_cost)
    
    return cost[1][n-1]


if __name__ == '__main__':
    arr = [40, 20, 30, 10, 40]
    res = matrixChainMultiplication(arr)
    print(f"Minimum No of Multiplications needed = {res}")
