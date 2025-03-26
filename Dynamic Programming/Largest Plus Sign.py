# You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

# Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

# An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

 

# Example 1:
# Input: n = 5, mines = [[4,2]]
# Output: 2
# Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.


# Example 2:
# Input: n = 1, mines = [[0,0]]
# Output: 0
# Explanation: There is no plus sign, so return 0.


from typing import List
from copy import deepcopy


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1]*n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0
        
        # prefixSum left to right
        leftToRight = deepcopy(grid)
        for i in range(n):
            for j in range(1, n):
                if grid[i][j] == 0:
                    leftToRight[i][j] = 0
                else:
                    leftToRight[i][j] = leftToRight[i][j-1] + grid[i][j]
        
        # prefixSum right to left
        rightToLeft = deepcopy(grid)
        for i in range(n):
            for j in range(n-2, -1, -1):
                if grid[i][j] == 0:
                    rightToLeft[i][j] = 0
                else:
                    rightToLeft[i][j] = rightToLeft[i][j+1] + grid[i][j]

        # prefixSum top to bottom
        topToBottom = deepcopy(grid)
        for j in range(n):
            for i in range(1, n):
                if grid[i][j] == 0:
                    topToBottom[i][j] = 0
                else:
                    topToBottom[i][j] = topToBottom[i-1][j] + grid[i][j]
        
        # prefixSum bottom to top
        bottomToTop = deepcopy(grid)
        for j in range(n):
            for i in range(n-2, -1, -1):
                if grid[i][j] == 0:
                    bottomToTop[i][j] = 0
                else:
                    bottomToTop[i][j] = bottomToTop[i+1][j] + grid[i][j]
        
        maxLength = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                else:
                    length = min(leftToRight[i][j], rightToLeft[i][j], topToBottom[i][j], bottomToTop[i][j])
                    maxLength = max(maxLength, length)
        return maxLength

if __name__ == '__main__':
    sol = Solution()
    print(sol.orderOfLargestPlusSign(5, [[3,0],[3,3]]))
    print(sol.orderOfLargestPlusSign(5, [[4,2]]))
    print(sol.orderOfLargestPlusSign(1, [[0,0]]))
    print(sol.orderOfLargestPlusSign(3, [[0,0],[0,1],[1,1],[2,0],[2,1],[2,2]]))
