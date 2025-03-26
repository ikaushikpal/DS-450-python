# Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.


# Example 1:
# Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# Output: 8
# Explanation: There are 8 negatives number in the matrix.


# Example 2:
# Input: grid = [[3,2],[1,0]]
# Output: 0


from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        
        countNegative = 0
        j = N - 1
        
        for i in range(M):
            while j >= 0 and grid[i][j] < 0:
                j -= 1
            countNegative += N - j - 1
            j = min(j+1, N-1)
        
        return countNegative
# Time complexity: O(M+N)
# Space complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
    print(sol.countNegatives([[3,2],[1,0]]))