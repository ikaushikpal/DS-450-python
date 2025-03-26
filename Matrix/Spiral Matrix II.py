# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.


# Example 1:
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]


# Example 2:
# Input: n = 1
# Output: [[1]]



from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num = 1
        maxx = n * n
        matrix = [[0] * n for _ in range(n)]
        min_row, max_row = 0, n - 1
        min_col, max_col = 0, n - 1

        while min_row <= max_row and min_col <= max_col:
            # first go left to right
            for j in range(min_col, max_col+1):
                if num <= maxx:
                    matrix[min_row][j] = num
                    num += 1
            min_row += 1

            # go down
            for i in range(min_row, max_row+1):
                if num <= maxx:
                    matrix[i][max_col] = num
                    num += 1
            max_col -= 1

            # go right to left
            for j in range(max_col, min_col-1, -1):
                if num <= maxx:
                    matrix[max_row][j] = num
                    num += 1
            max_row -= 1

            # go up
            for i in range(max_row, min_row-1, -1):
                if num <= maxx:
                    matrix[i][min_col] = num
                    num += 1
            min_col += 1

        return matrix



if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(3))