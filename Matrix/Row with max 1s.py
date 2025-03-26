class Solution:
    def rowWithMax1s(self, arr, rows, cols):
        # lets check if matrix is really contains 1
        FLAG = True
        for i in range(rows):
            if arr[i][cols - 1] == 1:
                FLAG = False
        
        if FLAG: # matrix do not contain 1
            return -1

        # just need to check which row encounter 1 first
        for j in range(cols):
            for i in range(rows):
                if arr[i][j] ==1:
                    return i

