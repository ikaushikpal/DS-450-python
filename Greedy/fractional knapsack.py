def fractionalKnapsack(profit, weight, W):
    n = len(profit)
    x = []

    for i in range(n):
        x.append((profit[i] / weight[i] , i))

    x.sort(reverse=True)

    j = 0
    total_profit = 0

    while j<n and W:
        frac, i = x[j]
        if weight[i] > W:
            current_weight = W/ weight[i]
        else:
            current_weight = 1

        total_profit +=  (current_weight * profit[i])
        W -= (current_weight * weight[i])

        j += 1
    
    return round(total_profit, 2)



if __name__ == '__main__':
    weights = [2, 3, 5, 7, 1, 4, 1]
    profit = [10, 5, 15, 7, 6, 18, 3]
    W = 15

    res = fractionalKnapsack(profit, weights, W)
    print(res)

    wt = [5, 10, 15, 22, 25]
    val = [30, 40, 45, 66, 90]
    capacity = 60

    res = fractionalKnapsack(val, wt, capacity)
    print(res)