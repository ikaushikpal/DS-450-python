# Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

# A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.

 

# Example 1:
# Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation: 
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.


# Example 2:
# Input: grid = [[7]]
# Output: 7


from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        N = len(grid)
        MAX = float('inf')
        
        currRow = grid[-1].copy()
        
        for i in range(N-2, -1, -1):
            prevRow = currRow
            
            firstMin = secondMin = MAX
            for val in prevRow:
                if val < firstMin:
                    secondMin = firstMin
                    firstMin = val
                elif val < secondMin:
                    secondMin = val
                    
            for j in range(N):
                if prevRow[j] == firstMin:
                    currRow[j] = secondMin + grid[i][j]
                else:
                    currRow[j] = firstMin + grid[i][j]
        return min(currRow)
# Time Complexity: O(N^2)
# Space Complexity: O(N)


if __name__ == '__main__':
    sol = Solution()
    print(sol.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.minFallingPathSum([[7]]))
    