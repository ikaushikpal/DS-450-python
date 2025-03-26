class Solution:
    def wave_traversal(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        for j in range(col):
            if not j%2:
                # go down
                for i in range(0, row, 1):
                    print(matrix[i][j], end=' ')
            else:
                # go up
                for i in range(row-1, -1, -1):
                    print(matrix[i][j], end=' ')

        print()



if __name__ == '__main__':
    matrix = [[11, 12, 13, 14],
            [21, 22, 23, 24],
            [31, 32, 33, 34]]


    sol = Solution()
    sol.wave_traversal(matrix)