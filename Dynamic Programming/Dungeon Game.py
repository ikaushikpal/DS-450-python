# The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

# The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

# Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

# To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

# Return the knight's minimum initial health so that he can rescue the princess.

# Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

 

# Example 1:
# Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
# Output: 7
# Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.


# Example 2:
# Input: dungeon = [[0]]
# Output: 1


from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M, N = len(dungeon), len(dungeon[0])
        
        dp = [[0]*N for _ in range(M)]
        
        for i in range(M-1, -1, -1):
            for j in range(N-1, -1, -1):
                if i == M-1 and j == N-1:
                    dp[i][j] = dungeon[i][j]
                elif i == M-1:
                    dp[i][j] = dp[i][j+1] + dungeon[i][j]
                elif j == N-1:
                    dp[i][j] = dp[i+1][j] + dungeon[i][j]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j]) + dungeon[i][j]
                
                # till now everything is same as minimum sum problem

                # but here to maintain the path with minium negative value
                # need to discard positive value
                dp[i][j] = min(dp[i][j], 0)
        
        return abs(dp[0][0]) + 1
# NOTE:
# https://www.youtube.com/watch?v=4uUGxZXoR5o

# Time Complexity: O(M * N)
# Space Complexity: O(M * N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.calculateMinimumHP(dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]))
    print(sol.calculateMinimumHP(dungeon = [[0]]))