# Given a fence with n posts and k colors, find out the number of ways of painting the fence so that not more than two consecutive fences have the same colors. Since the answer can be large return it modulo 10^9 + 7.


# Example 1:
# Input:
# N=3,  K=2 
# Output: 6
# Explanation: 
# We have following possible combinations:


# Example 2:
# Input:
# N=2,  K=4
# Output: 16

class Memo:
    def helper(self, n, k, ppc, pc):
        if n == 0:
            return 1
        
        c = 0
        for i in range(k):
            if ppc == pc and pc == i:
                continue
            c += self.helper(n-1, k, pc, i)
        return c

    def countWays(self, n, k):
        return self.helper(n, k, None, None)


class Solution:
    def countWays(self, n, k):
        if n == 0 or k==0: # if no house to color
            return 0

        if k == 1 and n > 2: # if only 1 color is given to color more than 2 houses
            return 0
        
        if k == 1 and n <= 2:
            return 1
        
            
        MOD = 10**9 + 7
        sameTwoColor = 0
        diffTwoColor = k
        totalWays = sameTwoColor + diffTwoColor

        for i in range(n-1):
            sameTwoColor = diffTwoColor
            diffTwoColor = (totalWays * (k-1))%MOD
            totalWays = (sameTwoColor + diffTwoColor)%MOD

        return totalWays%MOD
    

if __name__ == '__main__':
    n = 3
    k = 2
    print(Solution().countWays(n, k))
    print(Memo().countWays(2, 4))