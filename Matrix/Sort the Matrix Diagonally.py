from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        
        for gap in range(cols):
            i, j = 0, gap
            arr = []
            while i<rows and j <  cols:
                arr.append(mat[i][j])
                i += 1
                j += 1

            arr.sort(reverse=True)

            i, j = 0, gap
            while i<rows and j <  cols:
                mat[i][j] = arr.pop()
                i += 1
                j += 1

        for k in range(1, rows):
            i, j = k, 0
            arr = []
            while i<rows and j <  cols:
                arr.append(mat[i][j])
                i += 1
                j += 1
            
            arr.sort(reverse=True)

            i, j = k, 0
            while i<rows and j <  cols:
                mat[i][j] = arr.pop()
                i += 1
                j += 1

        return mat


def print_mat(mat):
    for row in mat:
        print(*row) 


if __name__ == '__main__':
    mat1 =  [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    mat2 =  [[3,3,1],[2,2,1],[1,1,1]]

    sol = Solution()
    print_mat(sol.diagonalSort(mat1))
    print_mat(sol.diagonalSort(mat2))
