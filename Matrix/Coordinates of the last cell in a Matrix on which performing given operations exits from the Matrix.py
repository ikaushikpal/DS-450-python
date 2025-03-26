# Given a binary matrix of dimensions N * M. One can perform the given operation into the matrix.

# If the value of matrix[i][j] is 0, then traverse in the same direction and check the next value.
# If the value of matrix[i][j] is 1, then update matrix[i][j] to 0 and change the current direction from up, right, down, or left to the directions right, down, left, and up respectively.
# Initially you start from cell(0, 0), moving in right direction.

# The task is to find the indices of the matrix  which leads to outside the matrix from the traversal of the given matrix from the cell (0, 0) by performing the operations.

# Example 1:

# Input:
# matrix[][] = {{0,1},
#               {1,0}}

# Output: (1,1)
# Explanation:


# Example 2:

# Input: 
# matrix[][] = {{0, 1, 1, 1, 0},
#                    {1, 0, 1, 0, 1},
#               {1, 1, 1, 0, 0}}

# Output: (2,0)
# Explanation: We will leave the grid after visiting the index (2,0).


class Solution:
    def endPoints(self, mat, m, n):
        dX = [-1, 0, 1, 0]
        dY = [0, 1, 0, -1]
        
        direction = 1
        x = y = 0
        ans = (0, 0)
        
        while 0<=x<m and 0<=y<n:
            if mat[x][y] == 1:
                direction = (direction + 1) % 4
                
            mat[x][y] = 0
            ans = (x, y)
            x += dX[direction]
            y += dY[direction]
        return ans
# Time Complexity: O(m*n)
# Space Complexity: O(1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.endPoints([[0,1], [1,0]], 2, 2))
    print(sol.endPoints([[0, 1, 1, 1, 0], [1, 0, 1, 0, 1], [1, 1, 1, 0, 0]], 3, 5))
    
        