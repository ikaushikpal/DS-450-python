# https://practice.geeksforgeeks.org/problems/maximize-number-of-1s0905/1
# https://www.interviewbit.com/problems/maximum-ones-after-modification/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        j = 0
        i = 0
        countZeros = 0
        result = 0

        while i<n and j < n:
            while j<n and countZeros <= B:
                result = max(result, j-i)
                if A[j] == 0:
                    countZeros += 1               
                j += 1
            
            while i<n and countZeros > B:
                if A[i] == 0:
                    countZeros -= 1
                i += 1
 
        result = max(result, j-i)

        return result



if __name__ == '__main__':
    arr = [ 1, 0, 0, 0, 0, 0, 0 ]
    B = 1

    print(Solution().solve(arr, B))