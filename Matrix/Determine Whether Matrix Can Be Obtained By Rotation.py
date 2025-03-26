from typing import List


class Solution: 
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        if len(mat) != len(target) or len(mat[0]) != len(target[0]):
            return False

        cond = [True] * 4
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] != target[i][j]: cond[0] = False
                if mat[i][j] != target[j][m-i-1]: cond[1] = False
                if mat[i][j] != target[m-i-1][n-j-1]: cond[2] = False
                if mat[i][j] != target[j][n-i-1]: cond[3] = False
        
        return cond[0] | cond[1] | cond[2] | cond[3]


if __name__ == '__main__':
    mat1 = [[0,1],[1,0]]
    target1 = [[1,0],[0,1]]

    mat2 = [[0,1],[1,1]]
    target2 = [[1,0],[0,1]]

    mat3 = [[0,0,0],[0,1,0],[1,1,1]]
    target3 = [[1,1,1],[0,1,0],[0,0,0]]

    sol = Solution()
    print(sol.findRotation(mat1, target1))
    print(sol.findRotation(mat2, target2))
    print(sol.findRotation(mat3, target3))
