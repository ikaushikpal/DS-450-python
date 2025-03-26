class Solution:
    def FindExitPoint(self, matrix) -> tuple:
        end_i = end_j = 0
        i = j = 0
        row = len(matrix)
        col = len(matrix[0])
        dir = 0
        # 0 -> left to right
        # 1 -> top to bottom
        # 2 -> right to left
        # 3 -> bottom to top
        
        while i>=0 and i<row and j>=0 and j<col:
            end_i, end_j = i, j

            if matrix[i][j] == 1:
                # geeksforgeeks only
                matrix[i][j] = 0
                dir = (dir + 1) % 4
            
            if dir == 0:
                j += 1
            elif dir == 1:
                i += 1
            elif dir == 2:
                j -= 1
            elif dir == 3:
                i -= 1
        
        return (end_i, end_j)

   
if __name__ == '__main__':
    # test case matrix
    matrix  = [[0, 1, 1],
            [1, 0, 1],
           [1, 1, 1],
           [0, 0, 1]]

    print(Solution().FindExitPoint(matrix))
