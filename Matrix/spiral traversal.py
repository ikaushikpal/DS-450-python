# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]


class Solution:
    def spiral_traversal(self,matrix, r, c): 
        result = []
        row = len(matrix)
        col = len(matrix[0])
        total_elements = row * col
        count = 0

        k_range = row // 2
        if row%2:
            k_range += 1
            
        for k in range(0, k_range, 1):
            
            # go right side
            for j in range(k, col-k):
                if count < total_elements:
                    result.append(matrix[k][j])
                    count += 1
                
            # go down
            for i in range(k+1, row-k):
                 if count < total_elements:
                    result.append(matrix[i][col-k-1])
                    count += 1
                
            # go left side
            for j in range(col-k-2, k-1, -1):
                if count < total_elements:
                    result.append(matrix[row-k-1][j])
                    count += 1
                
            # go up (leave one cell)
            for i in range(row-k-2, k, -1):
                if count < total_elements:
                    result.append(matrix[i][k])
                    count += 1
            
        return result

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        
        ans = []
        up = left = 0
        right, down = N - 1, M - 1
        
        while up <= down and left <= right:
            for j in range(left, right + 1):
                if len(ans) < M * N:
                    ans.append(matrix[up][j])
            up += 1
            
            for i in range(up, down + 1):
                if len(ans) < M * N:
                    ans.append(matrix[i][right])
            right -= 1
            
            for j in range(right, left-1, -1):
                if len(ans) < M * N:
                    ans.append(matrix[down][j])
            down -= 1
            
            for i in range(down, up-1, -1):
                if len(ans) < M * N:
                    ans.append(matrix[i][left])
            left += 1
        return ans
    
    
if __name__ == '__main__':
    matrix = [[11, 12, 13, 14],
            [21, 22, 23, 24],
            [31, 32, 33, 34]]


    sol = Solution()
    print(sol.spiral_traversal(matrix, 3, 4))
