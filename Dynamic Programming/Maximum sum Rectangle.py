# Given a 2D matrix M of dimensions RxC. Find the maximum sum submatrix in it.

# Example 1:

# Input:
# R=4
# C=5
# M=[[1,2,-1,-4,-20],
# [-8,-3,4,2,1],
# [3,8,10,1,3],
# [-4,-1,1,7,-6]]
# Output:
# 29
# Explanation:
# The matrix is as follows and the
# blue rectangle denotes the maximum sum
# rectangle.
# Thumbnail

# Example 2:
# Input:
# R=2
# C=2
# M=[[-1,-2],[-3,-4]]
# Output:
# -1
# Explanation:
# Taking only the first cell is the 
# optimal choice.


class Solution:
    def kadaneAlgo(self, array):
        maxSum = float('-inf')
        currSum = float('-inf')

        for i in range(len(array)):
            if array[i] > currSum:
                currSum = array[i]
            else:
                currSum += array[i]
            
            maxSum = max(maxSum, currSum)
        return maxSum
            
    def maximumSumRectangle(self, ROWS, COLS, matrix):
        maxSum = 0
        
        for i in range(COLS):
            rows = [0] * ROWS
            currSum = 0
            for j in range(i, COLS):
                for k in range(ROWS):
                    rows[k] += matrix[k][j]
                currSum += self.kadaneAlgo(rows)
                maxSum = max(maxSum, currSum)

        return maxSum

if __name__ == '__main__':
    matrix = [[1,2,-1,-4,-20],
              [-8,-3,4,2,1],
              [3,8,10,1,3],
              [-4,-1,1,7,-6]]

    s = Solution()
    print(s.maximumSumRectangle(4, 5, matrix))
    print(s.maximumSumRectangle(2, 2, [[-1,-2],[-3,-4]]))