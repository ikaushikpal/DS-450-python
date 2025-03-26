class Solution:
    def countWays(self, n, k):
        if n == 0 or k==0: # if no house to color
            return 0

        if k == 1 and n > 2: # if only 1 color is given to color more than 2 houses
            return 0
        
        if k == 1 and n <= 2: #edge case
            return 1
            
        MOD = 10**9 + 7
        sameTwoColor = 0 # how many ways we can color last 2 fences with same color
        # 0 because only only fence
        diffTwoColor = k # how many ways we can color last 2 fences with different color
        # why k because for every fence it can be any of k color
        totalWays = sameTwoColor + diffTwoColor

        for i in range(n-1):
            sameTwoColor = diffTwoColor
            diffTwoColor = (totalWays * (k-1))%MOD
            totalWays = (sameTwoColor + diffTwoColor)%MOD

        return totalWays%MOD


if __name__ == '__main__':
    n = 5
    k = 3

    print(Solution().countWays(n, k))