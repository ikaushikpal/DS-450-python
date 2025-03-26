days = [1,4,6,7,8,20]
costs = [2,7,15]
dp = [float('inf') for _ in range(len(days))]


def f(i, passValid, cost):
    if i == len(days):
        return cost
    
    if dp[i] != float('inf'):
        return dp[i]
    
    if passValid > days[i]:
        return f(i+1, passValid, cost)
    
    dp[i] = min(dp[i], min(f(i+1, days[i] + 1, cost + costs[0]),
                f(i+1, days[i] + 7, cost + costs[1]),
                f(i+1, days[i] + 30, cost + costs[2])))
    
    return dp[i]

# def f(i, passValid, cost):
#     if i == len(days):
#         return cost
    
#     if passValid > days[i]:
#         return f(i+1, passValid, cost)
        
#     return min(f(i+1, days[i] + 1, cost + costs[0]),
#                 f(i+1, days[i] + 7, cost + costs[1]),
#                 f(i+1, days[i] + 30, cost + costs[2]))


print(f(0, 0, 0))