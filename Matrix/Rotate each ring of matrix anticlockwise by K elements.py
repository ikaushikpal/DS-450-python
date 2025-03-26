class Solution:
    def rotate_array(self, array, k):
        rev = -1 if k < 0 else 1
        k = (abs(k) % len(array)) * rev
        if k < 0:
            k += len(array)
        k_range = len(array) - k

        array[:k_range], array[k_range:] = array[:k_range][::-1], array[k_range:][::-1]
        array.reverse()
        return array

    def shell_rotate(self, matrix, shell_no, k):
        array = []
        row = len(matrix)
        col = len(matrix[0])
        shell_no -= 1

        # go down the shell
        for i in range(shell_no, row-shell_no):
            array.append(matrix[i][shell_no])
        
        # go right the shell
        for j in range(shell_no+1, col-shell_no):
            array.append(matrix[row-shell_no-1][j])

        # go up the shell
        for i in range(row-shell_no-2, shell_no-1, -1):
            array.append(matrix[i][col-shell_no-1])
        
        # go left the shell
        for j in range(col-shell_no-2, shell_no, -1):
            array.append(matrix[shell_no][j])

        array = self.rotate_array(array, k)
        k = 0

        for i in range(shell_no, row-shell_no):
            matrix[i][shell_no] = array[k]
            k += 1
        
        # go right the shell
        for j in range(shell_no+1, col-shell_no):
            matrix[row-shell_no-1][j] = array[k]
            k += 1

        # go up the shell
        for i in range(row-shell_no-2, shell_no-1, -1):
            matrix[i][col-shell_no-1] = array[k]
            k += 1
        
        # go left the shell
        for j in range(col-shell_no-2, shell_no, -1):
            matrix[shell_no][j] = array[k]
            k += 1
        
        return matrix

    def rotate_matrix(self, matrix, k):
        for i in range(0, len(matrix)//2):
            matrix = self.shell_rotate(matrix, i+1, k)
    
        return matrix

if __name__ == '__main__':
# Input : k = 3
#         mat[4][4] = {{1, 2, 3, 4},
#                     {5, 6, 7, 8},
#                     {9, 10, 11, 12},
#                     {13, 14, 15, 16}}
# Output: 4 8  12 16
#         3 10  6 15
#         2 11  7 14
#         1  5  9 13

    matrix = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]]

    
    mat = Solution().rotate_mat(matrix, 3)

    for row in matrix:
        print(*row)
