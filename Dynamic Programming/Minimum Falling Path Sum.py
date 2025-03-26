# Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

# A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

# Example 1:
# Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
# Output: 13
# Explanation: There are two falling paths with a minimum sum as shown.


# Example 2:
# Input: matrix = [[-19,57],[-40,-5]]
# Output: -59
# Explanation: The falling path with a minimum sum is shown.


from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        M, N = len(matrix), len(matrix[0])
        
        for i in range(1, M):
            for j in range(N):
                minVal = matrix[i-1][j]
                
                if j - 1 >= 0:
                    minVal = min(minVal, matrix[i-1][j-1])
                if j + 1 < N:
                    minVal = min(minVal, matrix[i-1][j+1])
                
                matrix[i][j] += minVal
        
        return min(matrix[M-1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    print(sol.minFallingPathSum([[-19,57],[-40,-5]]))     