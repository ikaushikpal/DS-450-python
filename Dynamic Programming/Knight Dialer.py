# The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares horizontally and one square vertically (with both forming the shape of an L). The possible movements of chess knight are shown in this diagaram:

# A chess knight can move as indicated in the chess diagram below:


# We have a chess knight and a phone pad as shown below, the knight can only stand on a numeric cell (i.e. blue cell).


# Given an integer n, return how many distinct phone numbers of length n we can dial.

# You are allowed to place the knight on any numeric cell initially and then you should perform n - 1 jumps to dial a number of length n. All jumps should be valid knight jumps.

# As the answer may be very large, return the answer modulo 109 + 7.


# Example 1:
# Input: n = 1
# Output: 10
# Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.


# Example 2:
# Input: n = 2
# Output: 20
# Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]


# Example 3:
# Input: n = 3131
# Output: 136006598
# Explanation: Please take care of the mod.


import numpy as np


class Solution:
    def knightDialer(self, n: int) -> int:
        moves = {   
                    0:[4, 6],
                    1:[6, 8], 
                    2:[7, 9], 
                    3:[4, 8], 
                    4:[3, 9, 0], 
                    5:[],
                    6:[1, 7, 0], 
                    7:[2, 6],
                    8:[1, 3],
                    9:[4, 2],             
                }

        dp = [1] * 10
        for _ in range(n-1):
            newDp = [0] * 10
            for j in range(10):
                newDp[j] += sum(dp[k] for k in moves[j]) % 1_000_000_007
            dp = newDp
        
        return sum(dp) % 1_000_000_007
# Time Complexity : O(3 * 10 * N) = O(N)
# Space Complexity : O(10) = O(1)

    def knightDialer(self, N):
        mod = 10**9 + 7
        if N == 1: 
            return 10
        M = np.matrix([[0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                       [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                       [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [1, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]], dtype=np.int64)
        res, N = 1, N - 1
        while N:
            if N & 1:
                res = np.dot(res, M) % mod
                N = N - 1
                
            M = np.dot(M, M) % mod
            N = N >> 1
            
        return np.sum(res, dtype=np.int64) % mod
# Time Complexity: O(10**2 * logN) = O(logN)
# Space Complexity: O(10**2) = O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.knightDialer(2))