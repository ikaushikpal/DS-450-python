def coinChangePer(coins, targetSum):
    dp = [0] * (targetSum+1)
    dp[0] = 1

    for amount in range(1, targetSum+1):
        for coin in coins:
            if coin <= amount:
                reamingAmount = amount - coin
                dp[amount] += dp[reamingAmount]
    
    return dp[targetSum]



if __name__ == '__main__':
    coins = [2, 3, 5, 6]
    targetSum = 10

    print(coinChangePer(coins, targetSum))