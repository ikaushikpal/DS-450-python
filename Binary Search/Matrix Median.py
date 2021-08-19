class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findInMat(self, mat, N, M, key):
        i, j = 0, M-1
        greater = lesser = 0

        while 0 <=i<N and 0 <=j<M:
            if mat[i][j] < key:
                lesser += j+1
                greater += M-j
                i += 1
                
            elif mat[i][j] > key:
                lesser += j+1
                greater += M-j
                i += 1

    def findMedian(self, mat):
        N = len(mat)
        M = len(mat[0])

        arr = [item for sublist in mat for item in sublist]
        arr.sort()
        return arr[len(arr)//2]
