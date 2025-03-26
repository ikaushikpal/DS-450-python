# https://www.interviewbit.com/problems/max-continuous-series-of-1s/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def maxone(self, A, B):
        n = len(A)
        j = 0
        i = 0
        countZeros = 0
        result = 0

        while i<n and j < n:
            while j<n and countZeros <= B:
                if j-i > result:
                    iIndex = i
                    jIndex = j
                    result = j-i

                if A[j] == 0:
                    countZeros += 1               
                j += 1
            
            while i<n and countZeros > B:
                if A[i] == 0:
                    countZeros -= 1
                i += 1
 
        if j-i > result:
            iIndex = i
            jIndex = j
            result = j-i

        return list(range(iIndex, jIndex))



if __name__ == '__main__':
    arr = [ 1, 1, 0, 1, 1, 0, 0, 1, 1, 1  ]
    B = 1

    print(Solution().maxone(arr, B))