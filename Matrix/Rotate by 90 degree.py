class Solution:
    
    #Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, matrix, n):
        # in-place tranpose matrix
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # for clockwise rotate
        # # reverse each row
        # for i in range(n):
        #     matrix[i].reverse()

        # for anticlockwise rotate
        # swap each row with its reverse
        for i in range(0, n//2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        
        return matrix