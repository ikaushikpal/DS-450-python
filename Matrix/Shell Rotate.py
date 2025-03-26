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


if __name__ == '__main__':
    matrix = [[11, 12, 13, 14, 15, 16],
            [21, 22, 23, 24, 25, 26],
            [31, 32, 33, 34, 35, 36],
            [41, 42, 43, 44, 45, 46],
            [51, 52, 53, 54, 55, 56],
            [61, 62, 63, 64, 65, 66],]

    
    matrix = Solution().shell_rotate(matrix, 2, 1)

    for row in matrix:
        print(*row)
