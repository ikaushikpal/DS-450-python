# Given a triangle array, return the minimum path sum from top to bottom.

# For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

# Example 1:
# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).


# Example 2:
# Input: triangle = [[-10]]
# Output: -10


from typing import List

# memoized sol
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.memo = {}
        return self.f(triangle, 0, 0)

    def f(self, t, lvl, pv):
        if lvl == len(t) - 1:
            return t[lvl][pv]

        if (lvl, pv) in self.memo:
            return self.memo[(lvl, pv)]

        if pv + 1 < len(t[lvl + 1]):
            self.memo[(lvl, pv)] = t[lvl][pv] + min(self.f(t, lvl + 1, pv), self.f(t, lvl + 1, pv + 1))
        else:
            self.memo[(lvl, pv)] = t[lvl][pv] + self.f(t, lvl + 1, pv)
        
        return self.memo[(lvl, pv)]
    

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = [[float('inf')]*N for _ in range(N)]

        # initialization
        total = 0
        for i in range(N):
            total += triangle[i][0]
            dp[i][0] = total
        
        for i in range(1, N):
            for j in range(1, i+1):
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        
        return min(dp[N-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(sol.minimumTotal(triangle = [[-10]]))
