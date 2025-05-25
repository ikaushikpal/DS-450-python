# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

# You have two robots that can collect cherries for you:

# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:

# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.
 
# Example 1:
# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.

# Example 2:
# Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# Output: 28
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
# Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
# Total of cherries: 17 + 11 = 28.
 

# Constraints:
# rows == grid.length
# cols == grid[i].length
# 2 <= rows, cols <= 70
# 0 <= grid[i][j] <= 100


from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        curr = [[0]*COLS for _ in range(COLS)]
        
        # Base case: last row
        for j1 in range(COLS):
            for j2 in range(COLS):
                if j1 == j2:
                    curr[j1][j2] = grid[-1][j1]
                else:
                    curr[j1][j2] = grid[-1][j1] + grid[-1][j2]
        
        # Fill DP table from bottom to top
        for i in range(ROWS-2, -1, -1):
            prev = curr
            newCurr = [[0]*COLS for _ in range(COLS)]

            for j1 in range(COLS):
                for j2 in range(COLS): 
                    maxValue = float('-inf')

                    # Try all 9 possible moves (3 for robot1 × 3 for robot2)
                    for dy1 in range(-1, 2, 1):
                        newJ1 = j1 + dy1

                        if newJ1 < 0 or newJ1 >= COLS:
                            continue

                        for dy2 in range(-1, 2, 1):
                            newJ2 = j2 + dy2

                            if newJ2 < 0 or newJ2 >= COLS:
                                continue

                            # Calculate cherries collected at current position
                            if j1 == j2:  # Same position - collect once
                                cherries = grid[i][j1]
                            else:  # Different positions - collect from both
                                cherries = grid[i][j1] + grid[i][j2]
                            
                            maxValue = max(maxValue, prev[newJ1][newJ2] + cherries)
                    
                    newCurr[j1][j2] = maxValue
            curr = newCurr

        #         According to the problem:
        # Robot 1 starts at (0, 0) - top-left corner
        # Robot 2 starts at (0, COLS-1) - top-right corner

        # So curr[0][COLS-1] gives us the maximum cherries when both robots start at their designated positions and move optimally through the entire grid.
        return curr[0][COLS-1]
# Time Complexity: O(9nm^2)
# Space Complexity: O(2m^2)


if __name__ == '__main__':
    sol = Solution()
    print(sol.cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]))
    print(sol.cherryPickup(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]))