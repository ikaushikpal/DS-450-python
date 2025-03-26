# Given a square matrix mat, return the sum of the matrix diagonals.

# Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 

# Example 1:
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.


# Example 2:
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8


# Example 3:
# Input: mat = [[5]]
# Output: 5


from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        N = len(mat)
        total = 0
        
        for i in range(N):
            total += mat[i][i] + mat[i][-i-1]
        
        if N & 1:
            total -= mat[N >> 1][N >> 1]
        return total
# Time Complexity: O(N)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))
    print(sol.diagonalSum([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]))
    print(sol.diagonalSum([[5]]))

